#ifndef PARSER_VALUE_H
#define PARSER_VALUE_H

/* The parser's semantic value: Bison is told (via %define
   api.value.type) to use ParserValue as YYSTYPE for every terminal and
   nonterminal, instead of a %union. TypeSpec and DeclInfo accumulate a
   declaration's specifiers and declarator while it is being reduced. */

#include <string>
#include <utility>
#include <vector>

#include "ast/ast.hpp"

/* =====================================================================
   4. TYPE / DECLARATOR ACCUMULATORS
   ---------------------------------------------------------------------
   Built up while reducing declaration_specifiers / declarator rules.
   ===================================================================== */
struct TypeSpec {
    std::vector<std::string> parts; /* e.g. {"UNSIGNED","LONG"} or {"STRUCT"} */
    std::string tagName; /* the specific struct/class tag, e.g. "Point" --
                             `parts` only ever records the generic "STRUCT"/
                             "CLASS", so this is what actually lets a
                             later `p.x` be traced back to a specific
                             aggregate's member list */
    std::string typedefName; /* the TYPE_NAME spelling, when the type came
                                 from one (typedef alias or a tag used
                                 directly as a type) -- lets semantic
                                 analysis resolve it itself */
    bool isTypedefStorage = false;
    bool isStatic = false;
    bool isExtern = false;
    int storageClasses = 0;     /* static/extern/typedef keywords seen */
    bool isConst = false;
    bool isAuto = false;
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
                                      tells `int (*fp)(...)` (a pointer to a
                                      function, which the language does not have:
                                      the grammar rejects it) from `int *f(...)`
                                      (a function returning a pointer) */
    bool isReference = false;           /* declarator began with '&' */
    bool isVariadic = false;            /* parameter list ended in `...` */
    bool grouped = false;               /* see ASTTypeExpr::grouped */
    int innerPointerLevel = 0;
    int innerArrayCount = 0;
    std::string ptrOps;                 /* see ASTTypeExpr::ptrOps */
    std::string innerPtrOps;
    std::vector<ASTNodePtr> arrayDims;  /* one per `[...]`, nullptr for `[]` */
    ASTTypeExprPtr typeExpr;            /* only meaningful for a param entry */
    ASTNodePtr ctorInit;                /* `T x(args)`: a ConstructExpr */
};

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
    std::vector<std::pair<std::string, std::string>> bases; /* (access, name) of base classes */
};

#endif
