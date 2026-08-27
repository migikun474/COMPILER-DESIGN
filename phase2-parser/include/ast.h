#ifndef AST_H
#define AST_H

#include <memory>
#include <ostream>
#include <string>
#include <vector>

/* A single, generic node kind used for the whole tree -- this is a
   syntax analyzer, not a fully-typed AST library, so one node shape
   (kind + label + children) that every grammar rule can populate is
   enough to represent the tree without needing a class hierarchy per
   construct. `label` carries whatever is specific to that node (an
   operator symbol, an identifier name, a literal's text, ...). */
enum class ASTKind {
    Program,

    VarDecl, ParamDecl, FunctionDecl, FunctionDef, DeclGroup,
    StructDecl, UnionDecl, ClassDecl, EnumDecl, Enumerator, TypedefDecl,
    ConstructorDef, DestructorDef, InitDeclarator, InitializerList,

    CompoundStmt, IfStmt, WhileStmt, DoWhileStmt, UntilStmt, ForStmt,
    SwitchStmt, CaseStmt, DefaultStmt, LabeledStmt,
    BreakStmt, ContinueStmt, ReturnStmt, GotoStmt, ExprStmt, EmptyStmt,

    BinaryExpr, UnaryExpr, PostfixOpExpr, AssignExpr, TernaryExpr,
    CallExpr, BuiltinCallExpr, MemberExpr, ArrowExpr, ScopeExpr, IndexExpr,
    CastExpr, SizeofExpr, NewExpr, DeleteExpr, LambdaExpr, CommaExpr,

    IntLiteral, FloatLiteral, CharLiteral, StringLiteral, BoolLiteral,
    Identifier, ThisExpr, TypeNameNode,

    ErrorNode /* placeholder for a statement/declaration that failed to
                 parse -- keeps the AST complete around a mistake
                 instead of leaving a silent hole, the way Roslyn/
                 rust-analyzer-style "resilient" parsers do */
};

struct ASTNode {
    ASTKind kind;
    std::string label;
    int line = 0;
    std::vector<std::shared_ptr<ASTNode>> children;
};
using ASTNodePtr = std::shared_ptr<ASTNode>;

/* Node constructors: with no children, and with a fixed initializer
   list of children (nullptr children -- e.g. an omitted "else" -- are
   silently skipped so the printed tree doesn't show empty branches). */
ASTNodePtr mkNode(ASTKind kind, const std::string &label = "");
ASTNodePtr mkNode(ASTKind kind, const std::string &label, std::initializer_list<ASTNodePtr> kids);
void addChild(const ASTNodePtr &parent, const ASTNodePtr &child);

const char *astKindName(ASTKind k);

/* Pretty-prints the tree using ASCII branch connectors, one node per
   line: KindName ["label"] */
void printAST(const ASTNodePtr &root, std::ostream &out);

#endif
