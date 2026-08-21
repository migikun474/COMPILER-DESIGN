#include "ast.h"

extern int g_currentLine; /* declared in common.h; avoids a circular include */

ASTNodePtr mkNode(ASTKind kind, const std::string &label) {
    auto n = std::make_shared<ASTNode>();
    n->kind = kind;
    n->label = label;
    n->line = g_currentLine;
    return n;
}

ASTNodePtr mkNode(ASTKind kind, const std::string &label, std::initializer_list<ASTNodePtr> kids) {
    auto n = mkNode(kind, label);
    for (auto &k : kids) {
        if (k) n->children.push_back(k);
    }
    return n;
}

void addChild(const ASTNodePtr &parent, const ASTNodePtr &child) {
    if (parent && child) parent->children.push_back(child);
}

const char *astKindName(ASTKind k) {
    switch (k) {
        case ASTKind::Program: return "Program";
        case ASTKind::VarDecl: return "VarDecl";
        case ASTKind::ParamDecl: return "ParamDecl";
        case ASTKind::FunctionDecl: return "FunctionDecl";
        case ASTKind::FunctionDef: return "FunctionDef";
        case ASTKind::DeclGroup: return "DeclGroup";
        case ASTKind::StructDecl: return "StructDecl";
        case ASTKind::UnionDecl: return "UnionDecl";
        case ASTKind::ClassDecl: return "ClassDecl";
        case ASTKind::EnumDecl: return "EnumDecl";
        case ASTKind::Enumerator: return "Enumerator";
        case ASTKind::TypedefDecl: return "TypedefDecl";
        case ASTKind::ConstructorDef: return "ConstructorDef";
        case ASTKind::DestructorDef: return "DestructorDef";
        case ASTKind::InitDeclarator: return "InitDeclarator";
        case ASTKind::InitializerList: return "InitializerList";
        case ASTKind::CompoundStmt: return "CompoundStmt";
        case ASTKind::IfStmt: return "IfStmt";
        case ASTKind::WhileStmt: return "WhileStmt";
        case ASTKind::DoWhileStmt: return "DoWhileStmt";
        case ASTKind::UntilStmt: return "UntilStmt";
        case ASTKind::ForStmt: return "ForStmt";
        case ASTKind::SwitchStmt: return "SwitchStmt";
        case ASTKind::CaseStmt: return "CaseStmt";
        case ASTKind::DefaultStmt: return "DefaultStmt";
        case ASTKind::LabeledStmt: return "LabeledStmt";
        case ASTKind::BreakStmt: return "BreakStmt";
        case ASTKind::ContinueStmt: return "ContinueStmt";
        case ASTKind::ReturnStmt: return "ReturnStmt";
        case ASTKind::GotoStmt: return "GotoStmt";
        case ASTKind::ExprStmt: return "ExprStmt";
        case ASTKind::EmptyStmt: return "EmptyStmt";
        case ASTKind::BinaryExpr: return "BinaryExpr";
        case ASTKind::UnaryExpr: return "UnaryExpr";
        case ASTKind::PostfixOpExpr: return "PostfixOpExpr";
        case ASTKind::AssignExpr: return "AssignExpr";
        case ASTKind::TernaryExpr: return "TernaryExpr";
        case ASTKind::CallExpr: return "CallExpr";
        case ASTKind::BuiltinCallExpr: return "BuiltinCallExpr";
        case ASTKind::MemberExpr: return "MemberExpr";
        case ASTKind::ArrowExpr: return "ArrowExpr";
        case ASTKind::ScopeExpr: return "ScopeExpr";
        case ASTKind::IndexExpr: return "IndexExpr";
        case ASTKind::CastExpr: return "CastExpr";
        case ASTKind::SizeofExpr: return "SizeofExpr";
        case ASTKind::NewExpr: return "NewExpr";
        case ASTKind::DeleteExpr: return "DeleteExpr";
        case ASTKind::LambdaExpr: return "LambdaExpr";
        case ASTKind::CommaExpr: return "CommaExpr";
        case ASTKind::IntLiteral: return "IntLiteral";
        case ASTKind::FloatLiteral: return "FloatLiteral";
        case ASTKind::CharLiteral: return "CharLiteral";
        case ASTKind::StringLiteral: return "StringLiteral";
        case ASTKind::BoolLiteral: return "BoolLiteral";
        case ASTKind::Identifier: return "Identifier";
        case ASTKind::ThisExpr: return "ThisExpr";
        case ASTKind::TypeNameNode: return "TypeName";
    }
    return "?";
}

static void printNode(const ASTNodePtr &node, std::ostream &out,
                       const std::string &prefix, bool isLast) {
    if (!node) return;
    out << prefix << (isLast ? "`-- " : "|-- ") << astKindName(node->kind);
    if (!node->label.empty()) out << " \"" << node->label << "\"";
    out << "\n";

    std::string childPrefix = prefix + (isLast ? "    " : "|   ");
    for (size_t i = 0; i < node->children.size(); ++i) {
        printNode(node->children[i], out, childPrefix, i + 1 == node->children.size());
    }
}

void printAST(const ASTNodePtr &root, std::ostream &out) {
    if (!root) {
        out << "(empty tree)\n";
        return;
    }
    out << astKindName(root->kind);
    if (!root->label.empty()) out << " \"" << root->label << "\"";
    out << "\n";
    for (size_t i = 0; i < root->children.size(); ++i) {
        printNode(root->children[i], out, "", i + 1 == root->children.size());
    }
}
