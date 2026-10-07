#ifndef SEMANTIC_H
#define SEMANTIC_H

/* =====================================================================
   SEMANTIC ANALYZER
   ---------------------------------------------------------------------
   One recursive walk over the parser's AST, in source order -- an
   L-attributed syntax-directed definition evaluated over the tree
   (Dragon Book 5.x): declarations push types *down* into the symbol
   table, expressions synthesize their type *up* (6.5). Every node it
   visits is annotated in place:

     expression nodes   semType, isLValue, hasConstValue/constValue
     identifier / call /
     member / decl nodes symbol (the resolved declaration; for calls,
                        the overload actually chosen)

   so TAC generation can lower the same tree without re-deriving any of
   it. Errors go through the parser's own diagnostics list
   (reportDiagnostic) with kind "Semantic error" / "Semantic warning",
   and an expression that already failed gets TypeKind::Error, which
   every rule accepts silently -- one mistake, one message.

   Ordering rules (documented language decisions):
     - objects, types and tags are declare-before-use (C);
     - file-scope *functions* may be called before their declaration,
       matching the forward-reference resolution phase 2 already
       performs (test10/test23); they are declared on first use;
     - inside a class body every member is visible to every method body
       (bodies are checked after the class is complete, as in C++);
     - labels have function scope, so `goto` may jump forward.
   ===================================================================== */

#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

#include "ast/ast.hpp"
#include "symbol_table/symbol_table.hpp"
#include "types/types.hpp"

namespace sem {

class SemanticAnalyzer {
  public:
    explicit SemanticAnalyzer(SymbolTable &table) : st(table) {}

    void analyze(const ASTNodePtr &root);
    int errorCount() const { return errors; }
    int warningCount() const { return warnings; }

  private:
    enum class DeclCtx { Global, Local, Member };

    struct SwitchCtx {
        TypePtr subject;
        std::map<long long, int> caseLines; /* value -> line of its case */
        int defaultLine = 0;
    };

    /* one per function / method body being analysed */
    struct FunctionCtx {
        Symbol *fn = nullptr;
        std::string name;                /* for messages */
        TypePtr ret;
        bool isConstructorLike = false;  /* constructor / destructor: no value returns */
        bool sawValueReturn = false;
        std::vector<char> breakables;    /* 'L' loop, 'S' switch, innermost last */
        int loopDepth = 0;
        std::vector<SwitchCtx> switches;
        std::map<std::string, const ASTNode *> labels;
        RecordInfo *cls = nullptr;       /* enclosing class of a method body */
        bool isStaticMethod = false;
    };

    SymbolTable &st;
    int errors = 0;
    int warnings = 0;
    std::set<std::string> reported;      /* de-duplicates identical messages */
    std::vector<FunctionCtx> fns;

    /* forward references to file-scope functions */
    std::unordered_map<std::string, std::vector<ASTNodePtr>> topFunctions;
    std::unordered_map<std::string, int> topVariableLines;
    std::set<const ASTNode *> signatureDone;

    /* ---- diagnostics ---- */
    void error(const ASTNode *at, const std::string &msg, const std::string &category);
    void error(int line, int column, const std::string &msg, const std::string &category);
    void warning(const ASTNode *at, const std::string &msg, const std::string &category);
    void warning(int line, int column, const std::string &msg, const std::string &category);

    FunctionCtx *fn() { return fns.empty() ? nullptr : &fns.back(); }
    RecordInfo *currentClass();

    /* ---- types ---- */
    struct Resolved {
        TypePtr type;
        bool isAuto = false;   /* `auto x = ...`: deduce from the initializer */
    };
    Resolved resolveType(const ASTTypeExpr &te, const ASTNode *at, bool isParam);
    TypePtr resolveSpecifiers(const ASTTypeExpr &te, const ASTNode *at, bool &isAuto);
    TypePtr resolveTag(const ASTTypeExpr &te, const std::string &kindPart, const ASTNode *at);
    std::vector<TypePtr> resolveParams(const ASTTypeExpr &te, const ASTNode *at);
    long long arrayDimension(const ASTNodePtr &dim, const ASTNode *at);

    /* ---- declarations ---- */
    void prescan(const ASTNodePtr &root);
    void declaration(const ASTNodePtr &n, DeclCtx ctx);
    SymbolPtr variable(const ASTNodePtr &n, DeclCtx ctx);
    void typedefDecl(const ASTNodePtr &n);
    SymbolPtr functionSignature(const ASTNodePtr &n, DeclCtx ctx, bool isDefinition);
    void functionDefinition(const ASTNodePtr &n, DeclCtx ctx);
    void functionBody(const ASTNodePtr &n, const SymbolPtr &fnSym, RecordInfo *cls);
    void outOfClassDefinition(const ASTNodePtr &n);
    void recordDefinition(const ASTNodePtr &n);
    void checkMainSignature(const SymbolPtr &s, const ASTNode *at);
    int unevaluated = 0; /* inside `sizeof`: uses there need no definition */
    bool hoistFunction(const std::string &name);
    int declScopeForTags();
    void checkInitializer(const TypePtr &target, const ASTNodePtr &init, bool requireConstant,
                          const std::string &what);
    bool isConstantInitializer(const ASTNodePtr &n);
    /* the index of a `[i] = v` designator: an integer constant expression
       >= 0, evaluated once; -1 after reporting an error */
    long long designatorIndex(const ASTNodePtr &designator);
    SymbolPtr makeParamSymbol(const ASTTypeExprPtr &pte, const TypePtr &t, const ASTNode *at);

    /* ---- statements ---- */
    void statement(const ASTNodePtr &n);
    void subStatement(const ASTNodePtr &n, const std::string &scopeLabel);
    void blockItems(const ASTNodePtr &block);
    void condition(const ASTNodePtr &n, const std::string &construct);
    void collectLabels(const ASTNodePtr &n, FunctionCtx &ctx);
    void returnStatement(const ASTNodePtr &n);

    /* ---- expressions ---- */
    TypePtr expr(const ASTNodePtr &n);
    TypePtr value(const ASTNodePtr &n); /* expr() then decay */
    TypePtr identifier(const ASTNodePtr &n);
    TypePtr binary(const ASTNodePtr &n);
    TypePtr unary(const ASTNodePtr &n);
    TypePtr assignment(const ASTNodePtr &n);
    TypePtr ternary(const ASTNodePtr &n);
    TypePtr call(const ASTNodePtr &n);
    TypePtr builtinCall(const ASTNodePtr &n);
    TypePtr member(const ASTNodePtr &n, bool arrow, bool calleePosition);
    TypePtr scopeMember(const ASTNodePtr &n);
    TypePtr index(const ASTNodePtr &n);
    TypePtr cast(const ASTNodePtr &n);
    TypePtr sizeofExpr(const ASTNodePtr &n);

    bool isNullPointerConstant(const ASTNodePtr &n);
    bool checkModifiable(const ASTNodePtr &n, const std::string &what);
    /* implicit conversion of `e`'s value to `target` in context `ctx`
       ("assign", "initialize", "return", "argument"); reports on failure */
    bool convertible(const TypePtr &target, const ASTNodePtr &e, const std::string &message);
    void checkConstantConversion(const TypePtr &target, const ASTNodePtr &e);
    /* gcc's -Wsequence-point over every full expression (sequencing.cpp) */
    void checkSequencing(const ASTNodePtr &root);
    Conversion argumentConversion(const TypePtr &param, const ASTNodePtr &arg);
    SymbolPtr resolveOverload(const std::string &name, const std::vector<SymbolPtr> &candidates,
                              const std::vector<ASTNodePtr> &args, const ASTNode *at);
    TypePtr checkCallArgs(const TypePtr &fnType, const std::string &name,
                          const std::vector<ASTNodePtr> &args, const ASTNode *at);
    TypePtr callResult(const TypePtr &fnType);
    void checkAccess(const MemberLookup &ml, RecordInfo *namingClass, const std::string &name,
                     const ASTNode *at);
    void checkFormat(const std::string &fn, const std::vector<ASTNodePtr> &args, size_t fmtIndex,
                     bool isScanf, const ASTNode *at);
    void foldBinary(const ASTNodePtr &n, const std::string &op);

    /* ---- constructors, operator overloading, va_*, new (cxx.cpp) ---- */
    /* overload resolution among `rec`'s constructors (plus the implicit
       default/copy constructors); returns the user constructor chosen */
    SymbolPtr construct(RecordInfo *rec, const std::vector<ASTNodePtr> &args, const ASTNode *at);
    void defaultConstruct(const TypePtr &t, const ASTNode *at);
    void constructorInit(const TypePtr &target, const ASTNodePtr &init, const std::string &what);
    TypePtr constructExpr(const ASTNodePtr &n);
    TypePtr newExpr(const ASTNodePtr &n);
    void outOfClassSpecial(const ASTNodePtr &n);
    void checkOperatorDeclaration(const SymbolPtr &s, const ASTNode *at);
    bool anyViable(const std::vector<SymbolPtr> &candidates, const std::vector<ASTNodePtr> &args);
    /* `a + b`, `-a`, `a[i]`, `a(...)`, `a = b` with a class operand: resolves
       `operator<op>` (member or free). False when no such operator exists. */
    bool overloadedOperator(const ASTNodePtr &n, const std::string &op, const std::vector<ASTNodePtr> &operands,
                            TypePtr &result);
    TypePtr varargBuiltin(const ASTNodePtr &n);
};

std::string describeSignature(const SymbolPtr &fnSym);

} // namespace sem

#endif
