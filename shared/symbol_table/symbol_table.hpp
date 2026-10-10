#ifndef SHARED_SYMBOL_TABLE_HPP
#define SHARED_SYMBOL_TABLE_HPP

/* =====================================================================
   SYMBOL TABLES -- everything symbol-table related, in one module
   ---------------------------------------------------------------------
   Part 1, parse-time table (global namespace): the scoped table the
     parser maintains *while* parsing, to classify identifiers for the
     token log (`a -> INT`, `f -> PROCEDURE`), resolve overloads by
     argument shape, and drive the scanner's typedef "lexer hack" (the
     scoped table of names that are currently types). Its scopes are
     discarded as they close; a flat, append-only copy (g_symbolTable) is
     kept for the report. Name mangling lives here too.

   Part 2, semantic table (namespace sem): the persistent, typed table
     built by semantic analysis and handed to later phases.

   Printers for both tables are at the end of each part.
   ===================================================================== */

#include <memory>
#include <ostream>
#include <string>
#include <unordered_map>
#include <vector>

#include "ast/ast.hpp"
#include "types/types.hpp"

/* =====================================================================
   PART 1 -- PARSE-TIME SYMBOL TABLE
   ===================================================================== */

enum class SymKind {
    VARIABLE,
    PROCEDURE,
    PARAMETER,
    STRUCT_TAG,
    CLASS_TAG,
    TYPEDEF_NAME,
    LABEL
};

struct SymbolTableEntry; 

struct Symbol {
    SymKind kind;
    std::string typeStr; /* what to print in the Token_Type column */
    std::string mangledName; /* only set for PROCEDURE/CONSTRUCTOR/DESTRUCTOR */
    std::string aggregateTagName; 
    int flatIndex = -1; 
    ASTTypeExprPtr typeExpr; /* TYPEDEF_NAME: what the alias names (for mangling) */
};

struct SymbolDeclInfo {
    int tokenIdx = -1; /* index into g_tokens; used to recover an accurate
                           declaration line via g_tokens[tokenIdx].line */
    bool isStatic = false;
    bool isConst = false;
    int pointerLevel = 0;
    int arrayLevel = 0;
    std::string returnType;              /* callables only */
    std::vector<std::string> paramTypes; /* callables only */
    std::string mangledName;
    std::string aggregateTagName; /* set only for a variable of struct/class
                                      type -- see Symbol::aggregateTagName */
    ASTTypeExprPtr typeExpr;      /* typedefs: the aliased type */
};

/* Pushes a new scope. `label` names what this scope actually *is* --
   "main()", "if", "while", "class Dog" -- so a symbol's location can
   be reported as a readable path (see currentScopePath()) rather than
   a bare nesting-depth number. If label is empty, pushScope() first
   checks for a pending hint set by hintScope() (used by callers that
   push the scope one grammar rule away from where they know what
   it's for, e.g. selection_stmt hinting "if" right before the
   generic `statement` nonterminal reduces into compound_stmt's own
   pushScope()); if there's no hint either, it falls back to the
   generic label "block". */
void pushScope(const std::string &label = "");
void popScope();

void hintScope(const std::string &label);

std::string currentScopePath();

void queuePendingReference(int tokenIdx, const std::string &name, bool isLabel);

void resolvePendingReferences();

const SymbolTableEntry *findMember(const std::string &tagName, const std::string &memberName);

void declareSymbol(const std::string &name, SymKind kind, const std::string &typeStr,
                    const SymbolDeclInfo &extra = SymbolDeclInfo());
const Symbol *lookupSymbol(const std::string &name);
/* like lookupSymbol(), but only typedefs and struct/class tags
   -- what a TYPE_NAME token means even where a same-named constructor or
   variable is also visible */
const Symbol *lookupTypeSymbol(const std::string &name);

bool isOverloaded(const std::string &name);

/* Best-effort type of an already-built expression subtree, used only
   to match call arguments against candidate overloads -- literals and
   bare identifiers are inferred; anything more complex (a binary
   expression, a nested call, a member access, ...) deliberately
   returns "" rather than guess, since resolving to the wrong overload
   would be worse than not resolving at all. */
std::string inferExprType(const ASTNodePtr &node);

/* Scans every PROCEDURE-kind overload of `name` at the scope where it
   lives for one whose parameter types exactly match argTypes. Falls
   back to the most recently declared overload (not an error) if no
   exact match is found -- this is the same "best effort, never wrong,
   never a hard failure" contract every other resolution in this
   analyzer follows. */
const Symbol *lookupOverload(const std::string &name, const std::vector<std::string> &argTypes);

/* Looks up `name` in the current scope chain (same rules as
   lookupSymbol) and, if found, increments that symbol's usage count in
   the flat table. Called wherever an identifier is *used* rather than
   *declared* (a reference in an expression, a goto's target label).
   This only counts textual references -- it is not control-flow or
   reachability analysis, so it can't tell a live use from a dead one;
   it's bookkeeping, not a semantic check.

   Prefer the Symbol* overload when the caller has already called
   lookupSymbol() itself (almost always true -- the same identifier
   typically needs classifying via lookupSymbol() right before
   recording its use) so the scope chain isn't walked twice for the
   same name. */
void recordUsage(const std::string &name);
void recordUsage(const Symbol *s);

/* Enters/leaves an aggregate body (struct/class), so members
   declared inside it can be reported with a qualified
   "ClassName::member" name and so function mangling can nest the
   enclosing class the way real name-mangling schemes do. Aggregates
   nest (`struct A { struct B { int x; } b; int y; };`), so this is a
   stack: leaveClass() returns to the enclosing aggregate's context, and
   `y` above is still A's member.

   `kind` is "struct"/"class" and is what lets the symbol table tell a
   struct member apart from a class member. */
void enterClass(const std::string &className, const std::string &kind = "class");
void leaveClass();
std::string currentClassName(); /* "" when not inside a struct/class body */
std::string currentAggregateKind(); /* "struct"/"class"/"" */

/* Call immediately after pushing an aggregate body's own scope (right
   after enterClass()), so declareSymbol() can tell "declared directly
   as a member" (this exact scope depth) apart from "declared inside a
   member function's own body" (a deeper scope, reached again while
   enterClass()/leaveClass() are still bracketing the whole aggregate).
   Without this, a plain local variable inside a method would get
   incorrectly tagged as a struct/class member too. */
void markAggregateMemberDepth();
/* true directly inside an aggregate body (not in a member function's body) */
bool atAggregateMemberLevel();

/* Unnamed aggregates (tags made by anonymousTag(), see ast.hpp).
   `typedef struct { ... } Pt;` names the type Pt -- the first typedef
   wins, as in C++ -- which is what mangling uses. An unnamed member
   (`struct S { struct { int i; float f; }; };`) is registered with its
   enclosing tag so findMember("S", "i") finds `i`. */
void nameAnonymousTag(const std::string &tag, const std::string &typedefName);
std::string anonymousTagName(const std::string &tag); /* "" if none */
void addAnonymousMember(const std::string &outerTag, const std::string &anonTag);

/* ---------------------------------------------------------------------
   FLAT SYMBOL TABLE (for reporting)
   ---------------------------------------------------------------------
   pushScope()/popScope() above give the parser correctly-scoped,
   shadow-respecting lookup during parsing, but scopes are discarded
   once popped, so nothing would be left to print at the end. This is
   a second, append-only record of every symbol ever declared, kept
   purely so the driver can print a symbol table once parsing
   finishes. It plays no role in name resolution. */
struct SymbolTableEntry {
    std::string name;
    std::string qualifiedName; /* "ClassName::name" for class members */
    SymKind kind;
    std::string typeStr;
    std::string mangledName; /* empty unless kind is a callable */
    int scopeDepth;
    std::string scopePath; /* "global > main() > if" -- see currentScopePath() */
    std::string ownerAggregateKind; /* "struct"/"class"/"" -- which kind
                                        of aggregate this member belongs to, ""
                                        for anything that isn't a member at all
                                        (a plain local variable, a free function) */
    int declLine = 0;
    bool isStatic = false;
    bool isConst = false;
    int pointerLevel = 0;
    int arrayLevel = 0;
    std::string returnType;              /* callables only */
    std::vector<std::string> paramTypes; /* callables only */
    int useCount = 0; /* how many times this name was referenced after
                          being declared -- see recordUsage() */
};
extern std::vector<SymbolTableEntry> g_symbolTable;

/* =====================================================================
   4b. NAME MANGLING -- Itanium C++ ABI (what g++ and clang emit)
   ---------------------------------------------------------------------
   A function's link name encodes its name, its class and its parameter
   types, so every overload gets its own symbol:

     add(int, int)                 _Z3addii
     area(struct Point const *)    _Z4areaPK5Point
     Dog::bark()                   _ZN3Dog4barkEv
     Dog::Dog(Dog const &)         _ZN3DogC1ERKS_      (C1 / D1: complete-object
     Dog::~Dog()                   _ZN3DogD1Ev          constructor / destructor)
     Dog::operator+(Dog const &)   _ZN3DogplERKS_      (Itanium operator codes)
     printf-like f(char const *, ...)  _Z1fPKcz

   Parameter types are the real, resolved types: typedefs are replaced by
   what they name, struct/class types appear by tag, top-level const is
   dropped and arrays decay to pointers, exactly as the ABI requires.
   Repeated components use the ABI's substitutions (`S_`, `S0_`, ...:
   `f(Point *, Point *)` is _Z1fP5PointS0_). Target-specific choice:
   `va_list` is MIPS o32's `void *`. `main` is never mangled.

   The encoder works on sem::Type. The semantic phase hands it resolved
   types; the parser builds the same types structurally from the
   declaration (parseTimeType), so both symbol tables show the same name.
   ===================================================================== */
std::string mangle(const std::string &name, const std::vector<sem::TypePtr> &params, bool variadic,
                   const std::string &className = "");
/* the parser's entry point: parameters as written (ASTTypeExpr) */
std::string mangle(const std::string &name, const std::vector<ASTTypeExprPtr> &params, bool variadic,
                   const std::string &className = "");
/* a type as the parser sees it: specifiers, tags, typedefs (through this
   table), pointers, references, arrays and function types -- no checks,
   that is the semantic phase's job. Parameters decay like in C. */
sem::TypePtr parseTimeType(const ASTTypeExpr &te, bool isParam);

/* Names currently usable as types -- typedefs and struct/class tags --
   consulted by the scanner so it can hand the parser a
   TYPE_NAME token instead of a plain IDENTIFIER (the classic "lexer
   hack" needed to parse `MyInt x;` without type inference). Scoped like
   every other declaration: pushed/popped with pushScope()/popScope(), so
   a struct defined inside a function stops being a type name when the
   function ends, and an inner `int T;` hides an outer typedef `T`. */
void addTypeName(const std::string &name);  /* in the current scope */
void hideTypeName(const std::string &name); /* declared as a non-type here */
bool isTypeName(const std::string &name);

/* What to print for a TYPE_NAME token: "TYPEDEF" for a genuine
   typedef alias, or the tag's own category (CLASS/STRUCT) when the name
   is really a class/struct tag being used directly as a type (as C++
   allows, unlike plain C). */
std::string categoryForTypeName(const Symbol *s);

/* Human-readable name for a SymKind, for printing the symbol table. */
std::string symKindName(SymKind k);

/* the parser's symbol table report (Name / Kind / Line / Scope / Type /
   Qualifiers / Uses / Signature / Mangled Name) */
void printSymbolTable(std::ostream &out);

/* =====================================================================
   PART 2 -- SEMANTIC SYMBOL TABLE
   A tree of scopes (Dragon Book 2.7's chained tables), but *persistent*:
   leaving a scope only pops it off the active stack, it is never
   destroyed. Every scope and every symbol therefore survives the pass,
   so TAC/MIPS generation can walk the same table -- each AST
   declaration/use node points at its Symbol, each Symbol knows its
   scope, storage class and type, and each function knows its
   parameters and locals.

   Lookup follows the most-closely-nested rule over the *active* stack,
   which is exactly "visible at this program point", not "exists
   somewhere". Record (struct/class) scopes are part of the chain while
   a member function body is analysed, so members resolve as implicit
   this->member, including members inherited from base classes.

   Ordinary identifiers and struct/class tags live in
   separate namespaces per scope, as in C.
   ===================================================================== */

struct ASTNode;

namespace sem {

enum class SymbolKind { Variable, Parameter, Function, Field, Typedef, Label, Tag };

enum class Storage {
    None,     /* functions, typedefs, tags, labels */
    Global,   /* file-scope object: lives in .data/.bss */
    Static,   /* `static` local or `static` class member: also .data/.bss */
    Local,    /* automatic: lives in the stack frame */
    Param,    /* parameter: passed in a register / the frame */
    Member    /* non-static data member: an offset into its record */
};

struct Symbol {
    std::string name;
    std::string uniqueName;   /* program-wide unique, usable as a TAC name:
                                 globals keep their name, functions their
                                 (mangled) link name, locals get "name.N" */
    SymbolKind kind = SymbolKind::Variable;
    TypePtr type;
    Storage storage = Storage::None;

    int scopeId = -1;
    std::string scopePath;    /* "global > main() > block" */
    int line = 0;
    int column = 0;

    bool isConstant = false;  /* const-qualified object with a known value */
    long long constValue = 0;
    bool hasInitializer = false;
    int useCount = 0;
    int evaluatedUses = 0;    /* uses outside `sizeof`: these need a definition */

    /* functions (incl. methods / constructors / destructors) */
    bool isDefined = false;   /* functions: body seen; objects: defined here, not just
                                 declared `extern` */
    bool isStatic = false;    /* `static` function / member */
    bool isMethod = false;
    bool isConstructor = false;
    bool isDestructor = false;
    std::string mangledName;
    std::vector<SymbolPtr> params; /* in order; unnamed ones too */
    std::vector<SymbolPtr> locals; /* every local / static local in the body */
    int bodyScopeId = -1;

    /* members */
    RecordInfo *ownerRecord = nullptr;
    Access access = Access::Public;
    long long offset = -1;    /* data members: byte offset in the record */

    /* tags */
    std::shared_ptr<RecordInfo> record;

    const ASTNode *declNode = nullptr;
};

enum class ScopeKind { Global, Function, Block, Record };

struct Scope {
    int id = 0;
    int parent = -1;
    int depth = 0;
    ScopeKind kind = ScopeKind::Block;
    std::string label;
    std::unordered_map<std::string, std::vector<SymbolPtr>> names; /* vector: overloads */
    std::unordered_map<std::string, SymbolPtr> tags;
    std::vector<SymbolPtr> ordered;  /* declaration order, tags included */
    RecordInfo *record = nullptr;    /* ScopeKind::Record */
    Symbol *function = nullptr;      /* ScopeKind::Function: the owner */
};

struct Lookup {
    std::vector<SymbolPtr> symbols;  /* empty = not visible */
    int scopeId = -1;                /* where found */
    bool viaRecord = false;          /* found as a member of an enclosing class */
    MemberLookup member;             /* set when viaRecord */
};

class SymbolTable {
  public:
    SymbolTable();

    int enterScope(ScopeKind kind, const std::string &label, RecordInfo *record = nullptr,
                   Symbol *function = nullptr);
    void exitScope();
    /* re-activates an existing scope (e.g. a class's member scope while an
       out-of-class method body is analysed) */
    void reenterScope(int id);

    Scope &current();
    Scope &scope(int id);
    const std::vector<Scope> &scopes() const { return scopes_; }
    const std::vector<int> &activeStack() const { return stack_; }
    std::string pathOf(int scopeId) const;

    /* adds to the current scope (or `scopeId`); fills scopeId/scopePath/
       uniqueName */
    void declare(const SymbolPtr &s);
    void declareIn(int scopeId, const SymbolPtr &s);
    /* recorded in `scopeId` (and allSymbols) but invisible to lookup():
       labels, unnamed parameters, constructors */
    void declareHidden(int scopeId, const SymbolPtr &s);
    void declareTag(const SymbolPtr &s);
    void declareTagIn(int scopeId, const SymbolPtr &s);

    /* current scope only (redeclaration checks) */
    std::vector<SymbolPtr> lookupLocal(const std::string &name) const;
    SymbolPtr lookupTagLocal(const std::string &name) const;
    /* full visibility */
    Lookup lookup(const std::string &name) const;
    SymbolPtr lookupTag(const std::string &name) const;

    /* every symbol ever declared, in declaration order */
    const std::vector<SymbolPtr> &allSymbols() const { return all_; }

    /* temporarily makes only the global scope active (used to declare a
       forward-referenced function in file scope) */
    std::vector<int> saveAndResetToGlobal();
    void restoreStack(const std::vector<int> &saved);

  private:
    std::vector<Scope> scopes_;
    std::vector<int> stack_;
    std::vector<SymbolPtr> all_;
    int nextUnique_ = 0;
    void assignNames(int scopeId, const SymbolPtr &s);
};

std::string symbolKindName(SymbolKind k);
std::string storageName(Storage s);

/* every symbol of every scope, with its structural type and storage */
void printSemanticSymbolTable(const SymbolTable &st, std::ostream &out);

/* MIPS32 size/alignment/field offsets of every complete struct/class */
void printRecordLayouts(const SymbolTable &st, std::ostream &out);

} // namespace sem

#endif
