#ifndef REPORT_H
#define REPORT_H

#include <ostream>

#include "ast/ast.hpp"

namespace sem {

/* the parser's tree, each node followed by what semantic analysis
   attached to it: <type>, lvalue, constant value, resolved symbol */
void printAnnotatedAST(const ASTNodePtr &root, std::ostream &out);

} // namespace sem

#endif
