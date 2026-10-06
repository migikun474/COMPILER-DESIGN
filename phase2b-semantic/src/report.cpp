#include "report.h"

#include <string>

#include "symbol_table/symbol_table.hpp"

namespace sem {

static std::string annotation(const ASTNodePtr &n) {
    std::string a;
    if (n->semType) a += "  <" + typeToString(n->semType) + ">";
    if (n->isLValue) a += " lvalue";
    if (n->hasConstValue) a += " =" + std::to_string(n->constValue);
    if (n->symbol) {
        const Symbol &s = *n->symbol;
        a += "  -> " + (s.uniqueName.empty() ? s.name : s.uniqueName) + " (" + symbolKindName(s.kind);
        if (s.storage != Storage::None) a += ", " + storageName(s.storage);
        a += ")";
    }
    return a;
}

static void printNode(const ASTNodePtr &n, std::ostream &out, const std::string &prefix, bool last) {
    if (!n) return;
    out << prefix << (last ? "`-- " : "|-- ") << astKindName(n->kind);
    if (!n->label.empty()) out << " \"" << n->label << "\"";
    out << annotation(n) << "\n";
    std::string childPrefix = prefix + (last ? "    " : "|   ");
    for (size_t i = 0; i < n->children.size(); ++i) {
        printNode(n->children[i], out, childPrefix, i + 1 == n->children.size());
    }
}

void printAnnotatedAST(const ASTNodePtr &root, std::ostream &out) {
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

} // namespace sem
