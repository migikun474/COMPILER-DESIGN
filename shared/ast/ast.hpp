#ifndef SHARED_AST_HPP
#define SHARED_AST_HPP

#include <memory>
#include <ostream>
#include <string>
#include <vector>

enum class ASTKind {
    Program,

    VarDecl, ParamDecl, FunctionDecl, FunctionDef, DeclGroup,
    StructDecl, ClassDecl, TypedefDecl,
    ConstructorDef, DestructorDef, InitDeclarator, InitializerList,

    CompoundStmt, IfStmt, WhileStmt, DoWhileStmt, UntilStmt, ForStmt,
    SwitchStmt, CaseStmt, DefaultStmt, LabeledStmt,
    BreakStmt, ContinueStmt, ReturnStmt, GotoStmt, ExprStmt, EmptyStmt,

    BinaryExpr, UnaryExpr, PostfixOpExpr, AssignExpr, TernaryExpr,
    CallExpr, BuiltinCallExpr, MemberExpr, ArrowExpr, ScopeExpr, IndexExpr,
    CastExpr, SizeofExpr, NewExpr, DeleteExpr, CommaExpr,
    ConstructExpr, /* `T(args)`, `T x(args)` and `new T(args)`: build a T from args */
    DesignatedInit, /* `.field = v` / `[3] = v` inside an initializer list */

    IntLiteral, FloatLiteral, CharLiteral, StringLiteral, BoolLiteral,
    Identifier, ThisExpr, TypeNameNode,

    ErrorNode 
};

/* Owned by semantic analysis (phase2b-semantic); only forward-declared
   here so the AST can carry its annotations without this phase
   depending on it. */
namespace sem {
struct Type;
struct Symbol;
}

struct ASTNode;
using ASTNodePtr = std::shared_ptr<ASTNode>;

/* The declared type of a declaration / parameter / cast / sizeof(type) /
   new, exactly as written: specifiers plus declarator shape. The flat
   typeStr strings in labels ("INT_POINTER_ARRAY") lose struct tags,
   array sizes, `...`, unnamed parameters and return types; this keeps
   them. Purely syntactic -- the parser still checks nothing; semantic
   analysis resolves it into a structural sem::Type. Never printed. */
struct ASTTypeExpr {
    std::vector<std::string> specParts; /* same as TypeSpec::parts */
    std::string tagName;                /* struct/class tag, if any */
    std::string typedefName;            /* set when spelled via a TYPE_NAME */
    bool isStatic = false;
    bool isExtern = false;              /* `extern`: declares, does not define */
    bool isRegister = false;
    int storageClasses = 0;             /* how many storage-class keywords (> 1 is an error) */
    bool isConst = false;
    bool isVolatile = false;
    bool isAuto = false;
    bool isTypedef = false;

    int pointerLevel = 0;               /* counts a leading '&' too, see isReference */
    bool isReference = false;           /* declarator began with '&' */
    std::vector<ASTNodePtr> arrayDims;  /* in source order; nullptr for `[]` */
    /* `(...)` grouping, e.g. `int (*pa)[3]`: how many
       of pointerLevel / arrayDims were written *inside* the parentheses,
       which bind tighter than the suffixes after them */
    bool grouped = false;
    int innerPointerLevel = 0;
    int innerArrayCount = 0;
    /* the pointer operators themselves, left to right: '*' pointer, '&'
       reference, 'c'/'v' const/volatile on the pointer just before it --
       `int *const *&r` is "*c*&". ptrOps is outside any `(...)` group,
       innerPtrOps inside it. */
    std::string ptrOps;
    std::string innerPtrOps;
    bool isFunction = false;
    bool isVariadic = false;
    std::vector<std::shared_ptr<ASTTypeExpr>> params;

    std::string className;              /* `Class::member` out-of-class definitions */
    std::string name;                   /* declared name, "" when abstract */
    int nameLine = 0;
    int nameColumn = 0;
};
using ASTTypeExprPtr = std::shared_ptr<ASTTypeExpr>;

struct ASTNode {
    ASTKind kind;
    std::string label;
    int line = 0;
    int column = 0;
    std::vector<std::shared_ptr<ASTNode>> children;

    /* extra syntactic detail, never printed by printAST() */
    ASTTypeExprPtr typeExpr;  /* declarations, params, casts, sizeof(type), new */
    std::string access;       /* "public"/"protected"/"private" on aggregate members
                                 that follow an explicit access specifier */
    std::vector<std::pair<std::string, std::string>> bases; /* ClassDecl: (access, base name) */

    /* filled in by semantic analysis; unused by the parser */
    std::shared_ptr<const sem::Type> semType;
    std::shared_ptr<sem::Symbol> symbol;
    /* an initializer converted by a constructor (`Vec v = other;`): that
       constructor. Kept apart from `symbol`, which stays what the
       expression itself refers to. */
    std::shared_ptr<sem::Symbol> converter;
    bool isLValue = false;
    bool hasConstValue = false;
    long long constValue = 0;
};

/* Unnamed struct/class types (`struct { int x; } p;`,
   `typedef struct { ... } Pt;`, `struct { ... };` inside a struct) get an
   internal tag naming where they were written, "(unnamed at 3:9)" -- the
   way clang spells them. It can never collide with a real tag, and every
   phase keys records by tag, so nothing else has to special-case them. */
std::string anonymousTag(int line, int column);
bool isAnonymousTag(const std::string &tag);

ASTNodePtr mkNode(ASTKind kind, const std::string &label = "");
ASTNodePtr mkNode(ASTKind kind, const std::string &label, std::initializer_list<ASTNodePtr> kids);
void addChild(const ASTNodePtr &parent, const ASTNodePtr &child);

const char *astKindName(ASTKind k);

void printAST(const ASTNodePtr &root, std::ostream &out);

/* root of the whole parsed program's AST, filled in once
   translation_unit finishes reducing. */
extern ASTNodePtr g_astRoot;

#endif
