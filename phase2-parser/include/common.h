#ifndef COMMON_H
#define COMMON_H

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

#include "ast.h"

/* =====================================================================
   1. TOKEN RECORD LOG
   ---------------------------------------------------------------------
   Every token the scanner produces is appended here, in the exact order
   it was seen, with a "category" string that is initially just a
   generic default (e.g. "IDENTIFIER", "int", "plus_op" ...). For
   identifiers/type-names, the PARSER later goes back and *patches* the
   category of that specific slot once it has figured out -- from the
   grammar context and the symbol table -- what that identifier actually
   is (a variable of type X, a procedure, a struct tag, a label, ...).
   This is how the final table can show `a -> INT` or `a -> PROCEDURE`
   instead of a blanket `identifier` for every name.
   ===================================================================== */
struct TokenRecord {
    std::string lexeme;
    std::string category;
    int line = 0;
};

extern std::vector<TokenRecord> g_tokens;

int addTokenRecord(const std::string &lexeme, const std::string &category);
void setCategory(int idx, const std::string &category);

/* =====================================================================
   2. DIAGNOSTICS (lexical + syntax errors found while scanning/parsing)
   ===================================================================== */
struct Diagnostic {
    int line;
    int column;
    std::string near_text;
    std::string message;
    std::string kind; /* "Lexical error" | "Syntax error" */
};

extern std::vector<Diagnostic> g_diagnostics;

/* The source file's lines, 0-indexed (g_sourceLines[0] is line 1), used
   to print a GCC/Clang-style snippet + caret under each diagnostic.
   Populated once in main() before parsing starts. */
extern std::vector<std::string> g_sourceLines;

void reportDiagnostic(int line, int column, const std::string &near_text,
                       const std::string &message, const std::string &kind);
bool hasErrors();

/* A short, human-readable label for the ErrorNode placed in the AST at
   a recovery point -- built from whichever diagnostic was just
   recorded (the one that triggered this recovery), so the tree shows
   *what* went wrong right where the broken construct would have been,
   not just the token recovery happened to resynchronize on. */
std::string lastErrorLabel();

/* =====================================================================
   3. SYMBOL TABLE
   ---------------------------------------------------------------------
   A stack of scopes (global scope at index 0). Each scope maps a name
   to a Symbol describing what role that name plays and the classified
   "type_type" string that should be printed for it.
   ===================================================================== */
enum class SymKind {
    VARIABLE,
    PROCEDURE,
    PARAMETER,
    STRUCT_TAG,
    UNION_TAG,
    ENUM_TAG,
    CLASS_TAG,
    TYPEDEF_NAME,
    ENUM_CONST,
    LABEL
};

struct Symbol {
    SymKind kind;
    std::string typeStr; /* what to print in the Token_Type column */
    std::string mangledName; /* only set for PROCEDURE/CONSTRUCTOR/DESTRUCTOR */
    int flatIndex = -1; /* this symbol's slot in g_symbolTable, so a later
                            *use* of the name (see recordUsage()) can find
                            its way back to the permanent record and bump
                            its usage count -- scopes get destroyed on
                            popScope(), so this Symbol itself can't be
                            held onto past that point, but the index into
                            the never-shrinking g_symbolTable is safe to. */
};

/* Everything optional that can be known about a symbol at the point it's
   declared. Bundled into one struct (rather than a long parameter list)
   so most call sites -- labels, enum constants, struct/class/enum/union
   tags, parameters -- can just ignore it and get sensible defaults,
   while the ones that have this information on hand (variables,
   functions, constructors, destructors) can fill in what they know. */
struct SymbolDeclInfo {
    int tokenIdx = -1; /* index into g_tokens; used to recover an accurate
                           declaration line via g_tokens[tokenIdx].line */
    bool isStatic = false;
    bool isConst = false;
    bool isVolatile = false;
    int pointerLevel = 0;
    int arrayLevel = 0;
    std::string returnType;              /* callables only */
    std::vector<std::string> paramTypes; /* callables only */
    std::string mangledName;
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

/* Sets the label the *next* pushScope() call (that doesn't get an
   explicit one of its own) should use. Exists so a parent construct
   (if/while/for/switch) can label the scope that compound_stmt is
   about to push on its behalf, without threading an inherited
   attribute through the grammar. */
void hintScope(const std::string &label);

/* "global > main() > if > while" -- every currently-open scope's
   label, joined in nesting order. Captured once per symbol at
   declaration time into SymbolTableEntry::scopePath. */
std::string currentScopePath();

void declareSymbol(const std::string &name, SymKind kind, const std::string &typeStr,
                    const SymbolDeclInfo &extra = SymbolDeclInfo());
const Symbol *lookupSymbol(const std::string &name);

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

/* Enters/leaves an aggregate body (struct/union/class), so members
   declared inside it can be reported with a qualified
   "ClassName::member" name and so function mangling can nest the
   enclosing class the way real name-mangling schemes do. Nesting
   isn't supported (this language has no nested classes/structs), so
   it's a single "current aggregate" slot, not a stack.

   `kind` is "struct"/"union"/"class" and is what actually lets the
   symbol table tell a struct member apart from a class member --
   previously this was called enterClass() and used identically for
   all three aggregate types, meaning that distinction wasn't tracked
   anywhere at all. */
void enterClass(const std::string &className, const std::string &kind = "class");
void leaveClass();
std::string currentClassName(); /* "" when not inside a struct/union/class body */
std::string currentAggregateKind(); /* "struct"/"union"/"class"/"" */

/* Call immediately after pushing an aggregate body's own scope (right
   after enterClass()), so declareSymbol() can tell "declared directly
   as a member" (this exact scope depth) apart from "declared inside a
   member function's own body" (a deeper scope, reached again while
   enterClass()/leaveClass() are still bracketing the whole aggregate).
   Without this, a plain local variable inside a method would get
   incorrectly tagged as a struct/class member too. */
void markAggregateMemberDepth();

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
    std::string ownerAggregateKind; /* "struct"/"union"/"class"/"" -- which kind
                                        of aggregate this member belongs to, ""
                                        for anything that isn't a member at all
                                        (a plain local variable, a free function) */
    int declLine = 0;
    bool isStatic = false;
    bool isConst = false;
    bool isVolatile = false;
    int pointerLevel = 0;
    int arrayLevel = 0;
    std::string returnType;              /* callables only */
    std::vector<std::string> paramTypes; /* callables only */
    int useCount = 0; /* how many times this name was referenced after
                          being declared -- see recordUsage() */
};
extern std::vector<SymbolTableEntry> g_symbolTable;

/* =====================================================================
   4b. NAME MANGLING
   ---------------------------------------------------------------------
   A simplified, Itanium-ABI-*inspired* (not spec-compliant) mangling:
   _Z<len><name>[N<len><Class>E]<param-codes | v>
   e.g. add(int,int)        -> _Z3addii
        Dog::bark()         -> _ZN3Dog4barkEv
   Good enough to demonstrate the concept -- overload-distinguishing,
   deterministic, reversible-in-spirit -- without trying to be a
   drop-in-compatible ABI implementation, which is out of scope for a
   syntax-analysis pass with no real type system behind it.
   ===================================================================== */
std::string mangle(const std::string &name, const std::vector<std::string> &paramTypes,
                    const std::string &className = "");

/* set of names currently known to be typedef'd -- consulted by the
   scanner itself so it can hand the parser a TYPE_NAME token instead of
   a plain IDENTIFIER for those names (the classic "lexer hack" needed
   to parse `MyInt x;` without a full type-inference pass). */
extern std::unordered_set<std::string> g_typedefNames;

/* =====================================================================
   4. TYPE / DECLARATOR ACCUMULATORS
   ---------------------------------------------------------------------
   Built up while reducing declaration_specifiers / declarator rules.
   ===================================================================== */
struct TypeSpec {
    std::vector<std::string> parts; /* e.g. {"UNSIGNED","LONG"} or {"STRUCT"} */
    bool isTypedefStorage = false;
    bool isStatic = false;
    bool isConst = false;
    bool isVolatile = false;
};

struct DeclInfo {
    std::string name;
    int nameIdx = -1;
    int pointerLevel = 0;
    int arrayLevel = 0;
    bool isFunction = false;
    std::vector<DeclInfo> params; /* only meaningful when isFunction */
    std::string typeStr;          /* only meaningful for a param entry */
    ASTNodePtr initExpr;          /* `= expr` initializer, if any */
    std::string className;        /* set for `Class::member(...)` out-of-class
                                      definitions, empty otherwise */
    bool wasParenGrouped = false; /* set by direct_declarator: '(' declarator ')' --
                                      distinguishes `int (*fp)(...)` (a function-
                                      POINTER VARIABLE, whose pointer sits inside the
                                      parens) from `int *f(...)` (a function whose
                                      RETURN TYPE is a pointer, where the pointer is
                                      outside/before the whole declarator). Without
                                      this, both looked identical (isFunction=true,
                                      pointerLevel>0) and the former was wrongly
                                      classified as a PROCEDURE instead of a
                                      variable. */
    bool isFunctionPointer = false;
};

std::string computeTypeStr(const TypeSpec &ts, int pointerLevel, int arrayLevel);

/* What to print for a TYPE_NAME token: "TYPEDEF" for a genuine
   typedef alias, or the tag's own category (CLASS/STRUCT/UNION/ENUM)
   when the name is really a class/struct/union/enum tag being used
   directly as a type (as C++ allows, unlike plain C). */
std::string categoryForTypeName(const Symbol *s);

/* Human-readable name for a SymKind, for printing the symbol table. */
std::string symKindName(SymKind k);

/* Registers a fully-formed declarator (variable / function / typedef)
   against the current scope, patches its token-record category, and
   returns the AST node representing this one declaration (VarDecl /
   FunctionDecl / TypedefDecl), or nullptr for an abstract declarator
   with nothing to register. */
ASTNodePtr registerDeclarator(DeclInfo &d, TypeSpec &ts);

/* =====================================================================
   5. PARSER VALUE TYPE
   ---------------------------------------------------------------------
   Bison is told (via %define api.value.type) to use this single struct
   as YYSTYPE for every terminal and nonterminal, instead of a %union.
   ===================================================================== */
struct ParserValue {
    std::string str; /* raw token text, when relevant */
    int idx = -1;     /* index into g_tokens, for IDENTIFIER/TYPE_NAME */
    TypeSpec typeSpec;
    DeclInfo decl;
    std::vector<DeclInfo> paramList;
    ASTNodePtr node;                    /* this rule's AST subtree, if any */
    std::vector<ASTNodePtr> nodeList;   /* for comma-separated node lists */
};

/* root of the whole parsed program's AST, filled in once
   translation_unit finishes reducing. */
extern ASTNodePtr g_astRoot;

/* current line / column / lexeme, updated by the scanner on every
   token, so yyerror() can report an accurate location for syntax
   errors -- column is the 1-based column the token STARTS at. */
extern int g_currentLine;
extern int g_currentColumn;
extern std::string g_lastText;

#endif
