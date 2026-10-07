#ifndef DECLARATORS_H
#define DECLARATORS_H

/* Turning a reduced declaration into AST nodes and symbol-table entries:
   the declared type's printable string and ASTTypeExpr snapshot, node
   positions taken from tokens, and registration of variables,
   functions, typedefs, constructors and destructors. */

#include <string>
#include <vector>

#include "ast/ast.hpp"
#include "parser_value.h"

std::string computeTypeStr(const TypeSpec &ts, int pointerLevel, int arrayLevel);

/* Snapshot of a specifier list + declarator as an ASTTypeExpr, for
   attaching to the AST node that declares it (see ast.h). */
ASTTypeExprPtr makeTypeExpr(const TypeSpec &ts, const DeclInfo &d);

/* Moves a node's line/column to where token `tokIdx` starts. mkNode()
   stamps whatever token was scanned last, which for a bottom-up parse
   is usually the lookahead *after* the construct; diagnostics from later
   phases want the construct's own position. Returns the node. */
ASTNodePtr atToken(const ASTNodePtr &n, int tokIdx);
ASTNodePtr atNode(const ASTNodePtr &n, const ASTNodePtr &from);

/* Registers a fully-formed declarator (variable / function / typedef)
   against the current scope, patches its token-record category, and
   returns the AST node representing this one declaration (VarDecl /
   FunctionDecl / TypedefDecl), or nullptr for an abstract declarator
   with nothing to register. */
/* the internal tag of an unnamed struct/class whose keyword
   is token `tokIdx` (see anonymousTag() in ast.hpp) */
std::string anonymousTagAt(int tokIdx);
/* the parameters' type expressions, for mangle() */
std::vector<ASTTypeExprPtr> paramExprs(const std::vector<DeclInfo> &params);
ASTNodePtr registerDeclarator(DeclInfo &d, TypeSpec &ts);

/* Builds a ConstructorDef / DestructorDef node and records the callable
   in the symbol table. `body` is null for a declaration inside the class
   (`Dog(int n);`), whose definition then appears outside it
   (`Dog::Dog(int n) { ... }`); `className` names the class either way. */
ASTNodePtr makeConstructorNode(const std::string &name, int nameIdx, const std::vector<DeclInfo> &params,
                               bool variadic, const std::string &className, const ASTNodePtr &body);
ASTNodePtr makeDestructorNode(const std::string &name, int nameIdx, const std::string &className,
                              const ASTNodePtr &body);

#endif
