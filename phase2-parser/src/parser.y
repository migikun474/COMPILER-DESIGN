%code requires {
    #include "parser_value.h"
}

%define api.value.type {ParserValue}
%define parse.error verbose
/* every ambiguity in this grammar is resolved explicitly (see the
   precedence block); a new conflict fails the build instead of being
   settled silently by Bison's defaults */
%expect 0
%locations

%code {
    #include <cstdio>
    #include <cctype>
    #include <cstring>
    #include <string>

    #include "declarators.h"
    #include "diagnostics/diagnostics.hpp"
    #include "scanner_support.h"
    #include "symbol_table/symbol_table.hpp"
    #include "token/token_log.hpp"
    #include "token/token_type.hpp"
    extern int yylex();
    extern FILE *yyin;
    extern int yylineno;
    void yyerror(const char *s);

    /* `T(args)` as an expression: ConstructExpr whose typeExpr names T
       (a type keyword, a typedef, or a class/struct used as a type) */
    static ASTNodePtr makeFunctionalCast(const std::string &name, int idx, const std::vector<ASTNodePtr> &args) {
        auto n = atToken(mkNode(ASTKind::ConstructExpr, name), idx);
        TypeSpec ts;
        auto kw = reserved_word(name);
        if (kw.has_value()) {
            std::string part = name;
            for (auto &ch : part) ch = static_cast<char>(toupper(static_cast<unsigned char>(ch)));
            ts.parts.push_back(part);
        } else {
            const Symbol *s = lookupTypeSymbol(name);
            setCategory(idx, categoryForTypeName(s));
            ts.parts.push_back(s ? s->typeStr : "INT");
            ts.typedefName = name;
        }
        n->typeExpr = makeTypeExpr(ts, DeclInfo());
        for (auto &a : args) addChild(n, a);
        return n;
    }

}

/* ---- keywords ---- */
%token INT CHAR FLOAT DOUBLE VOID SHORT LONG SIGNED UNSIGNED
%token STRUCT CLASS
%token PUBLIC PRIVATE PROTECTED THIS
%token STATIC TYPEDEF AUTO EXTERN REGISTER CONST VOLATILE
%token IF ELSE FOR WHILE DO UNTIL SWITCH CASE DEFAULT
%token BREAK CONTINUE GOTO RETURN
%token PRINTF SCANF MALLOC FREE CALLOC REALLOC
%token BOOL
%token NEW DELETE SIZEOF
%token VA_LIST VA_START VA_ARG VA_END
%token OPERATOR
%token DELETE_ARRAY /* `delete[]`, one token (see scanner.l) */
%token FCAST        /* a type name / type keyword starting `T(...)` that can only be an
                       expression (`Dog(4).bark();`), decided by the scanner's lookahead */
%token ABSTRACT_LPAREN /* '(' after a type that opens a nameless declarator: `int (*)[3]` */

/* ---- literals / names ---- */
%token IDENTIFIER TYPE_NAME
%token INT_LITERAL FLOAT_LITERAL CHAR_LITERAL STRING_LITERAL BOOL_LITERAL

/* ---- multi-character operators ---- */
%token ARROW ELLIPSIS SCOPE_RES
%token INC DEC
%token SHL SHR
%token LE_OP GE_OP EQ_OP NE_OP
%token AND_OP OR_OP
%token PLUS_ASSIGN MINUS_ASSIGN MUL_ASSIGN DIV_ASSIGN MOD_ASSIGN
%token AND_ASSIGN OR_ASSIGN XOR_ASSIGN SHL_ASSIGN SHR_ASSIGN

/* ---- precedence (lowest to highest); resolves the classic ambiguous
   flat expression grammar below, same technique the K&R yacc grammar
   for C uses ---- */
%precedence PREFER_EXPRESSION /* lowest: see type_name_specifier */
/* `new T * x`: the type in a new-expression is the longest sequence of
   `*`s that follows (C++ [expr.new]/3), so `new int * x` is `(new int*) x`
   -- an error, exactly as in g++ -- never `(new int) * x`. Rules ending
   a new_type_id carry this precedence, lower than '*', so the '*' is
   shifted into the type. */
%precedence NEW_TYPE_END
%right '=' PLUS_ASSIGN MINUS_ASSIGN MUL_ASSIGN DIV_ASSIGN MOD_ASSIGN AND_ASSIGN OR_ASSIGN XOR_ASSIGN SHL_ASSIGN SHR_ASSIGN
%right '?' ':'
%left OR_OP
%left AND_OP
%left '|'
%left '^'
%left '&'
%left EQ_OP NE_OP
%left '<' '>' LE_OP GE_OP
%left SHL SHR
%left '+' '-'
%left '*' '/' '%'
%right UMINUS ADDR DEREF CAST '!' '~' INC DEC
%left '.' ARROW SCOPE_RES '(' '['
/* `sizeof (T) * x` is `(sizeof(T)) * x`: in C, `sizeof ( type-name )`
   is complete at its ')' -- a following `* x`, `& x`, `+ x` or `- x` is
   a binary operator, never the operand of a cast `(T) *x`. Bison's
   default (shift) got these four conflicts backwards. */
%precedence SIZEOF_TYPE
/* `T(...)` is ambiguous where both a declaration and an expression may
   start. C++ settles it in favour of the declaration, and so does this
   grammar: `T` followed by '(' at the start of a statement, or as the
   first thing in a `(...)` after a declarator, is a type. These two
   precedences make that choice explicit instead of a silent default. */
%precedence TYPE_NAME INT CHAR FLOAT DOUBLE VOID BOOL SHORT LONG SIGNED UNSIGNED
%precedence PREFER_DECLARATION
%nonassoc IFX
%nonassoc ELSE

%%

translation_unit
    : /* empty */ {
          $$.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = $$.node;
      }
    | translation_unit external_decl {
          $$ = $1;
          addChild($$.node, $2.node);
          g_astRoot = $$.node;
      }
    ;

external_decl
    : function_definition { $$.node = $1.node; }
    | declaration { $$.node = $1.node; }
    | out_of_class_special { $$.node = $1.node; }
    | error ';'  { $$.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
    | error '}'  { $$.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
    ;

declaration
    : declaration_specifiers init_declarator_list_opt ';' {
          endDeclaratorList();
          std::vector<ASTNodePtr> declNodes;
          for (auto &d : $2.paramList) {
              auto n = registerDeclarator(d, $1.typeSpec);
              if (n) declNodes.push_back(n);
          }
          if (declNodes.empty()) {
              $$.node = $1.node; /* bare struct/class declaration */
              /* `struct { int i; float f; };` inside a struct: its members
                 are the enclosing struct's (an anonymous member) */
              if (isAnonymousTag($1.typeSpec.tagName) && $1.node) {
                  if (atAggregateMemberLevel())
                      addAnonymousMember(currentClassName(), $1.typeSpec.tagName);
                  $1.node->typeExpr = makeTypeExpr($1.typeSpec, DeclInfo());
              }
          } else if (declNodes.size() == 1 && !$1.node) {
              $$.node = declNodes[0];
          } else {
              auto grp = mkNode(ASTKind::DeclGroup);
              if ($1.node) addChild(grp, $1.node);
              for (auto &n : declNodes) addChild(grp, n);
              $$.node = grp;
          }
      }
    ;

declaration_specifiers
    : declaration_specifiers storage_or_type_specifier {
          $$ = $1;
          for (auto &p : $2.typeSpec.parts) $$.typeSpec.parts.push_back(p);
          if ($2.typeSpec.isStatic) $$.typeSpec.isStatic = true;
          if ($2.typeSpec.isTypedefStorage) $$.typeSpec.isTypedefStorage = true;
          if ($2.typeSpec.isExtern) $$.typeSpec.isExtern = true;
          if ($2.typeSpec.isRegister) $$.typeSpec.isRegister = true;
          $$.typeSpec.storageClasses += $2.typeSpec.storageClasses;
          if ($2.typeSpec.isConst) $$.typeSpec.isConst = true;
          if ($2.typeSpec.isVolatile) $$.typeSpec.isVolatile = true;
          if ($2.typeSpec.isAuto) $$.typeSpec.isAuto = true;
          if (!$2.typeSpec.tagName.empty()) $$.typeSpec.tagName = $2.typeSpec.tagName;
          if (!$2.typeSpec.typedefName.empty()) $$.typeSpec.typedefName = $2.typeSpec.typedefName;
          if ($2.node) $$.node = $2.node;
      }
    | storage_or_type_specifier { $$ = $1; }
    ;

storage_or_type_specifier
    : STATIC   { $$.typeSpec.isStatic = true; $$.typeSpec.storageClasses = 1; }
    | EXTERN   { $$.typeSpec.isExtern = true; $$.typeSpec.storageClasses = 1; }
    | REGISTER { $$.typeSpec.isRegister = true; $$.typeSpec.storageClasses = 1; }
    | AUTO     { $$ = ParserValue(); $$.typeSpec.isAuto = true; }
    | TYPEDEF  { $$.typeSpec.isTypedefStorage = true; $$.typeSpec.storageClasses = 1; }
    | CONST    { $$.typeSpec.isConst = true; } /* now actually tracked -- see Symbol/SymbolTableEntry */
    | VOLATILE { $$.typeSpec.isVolatile = true; }
    | type_specifier { $$ = $1; }
    ;

type_specifier
    : INT      { $$.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
    | CHAR     { $$.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
    | FLOAT    { $$.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
    | DOUBLE   { $$.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
    | VOID     { $$.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
    | BOOL     { $$.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
    | SHORT    { $$.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
    | LONG     { $$.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
    | SIGNED   { $$.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
    | UNSIGNED { $$.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
    | VA_LIST  { $$.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
    | TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          $$.typeSpec.typedefName = $1.str;
          if (s && (s->kind == SymKind::STRUCT_TAG || s->kind == SymKind::CLASS_TAG)) {
              $$.typeSpec.tagName = $1.str; /* "Dog d;" -- Dog referenced directly,
                                                without repeating class/struct */
          } else if (s && s->kind == SymKind::TYPEDEF_NAME && s->typeExpr && s->typeExpr->pointerLevel == 0 &&
                     s->typeExpr->arrayDims.empty() && !s->typeExpr->isFunction) {
              $$.typeSpec.tagName = s->typeExpr->tagName; /* `Pt p;` with `typedef struct {...} Pt;`:
                                                              p.x resolves through the struct */
          }
      }
    | struct_or_class_specifier { $$ = $1; }
    ;

/* the tag being defined: a fresh name, or one that is already a type name
   (an inner-scope definition hiding an outer one, or a redefinition --
   which semantic analysis reports) */
tag_name
    : IDENTIFIER { $$ = $1; }
    | TYPE_NAME  { $$ = $1; }
    ;

struct_or_class_specifier
    : STRUCT tag_name {
          declareSymbol($2.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{$2.idx});
          setCategory($2.idx, "STRUCT");
          enterClass($2.str, "struct");
      } '{' { pushScope("struct " + $2.str); markAggregateMemberDepth(); } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("STRUCT");
          $$.typeSpec.tagName = $2.str;
          addTypeName($2.str); /* usable as a type from here on, but
                                             NOT inside its own body -- lets
                                             constructors/destructors keep
                                             matching the class's own name as
                                             a plain IDENTIFIER */
          auto node = atToken(mkNode(ASTKind::StructDecl, $2.str), $2.idx);
          for (auto &m : $6.nodeList) addChild(node, m);
          $$.node = node;
      }
    /* unnamed: `struct { int x, y; } p;`, `typedef struct { ... } Pt;`,
       or an anonymous member `struct S { struct { int lo, hi; }; };`.
       The tag is made up from the position (anonymousTag()). */
    | STRUCT '{' {
          $$.str = anonymousTagAt($1.idx);
          declareSymbol($$.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{$1.idx});
          enterClass($$.str, "struct");
          pushScope("struct " + $$.str);
          markAggregateMemberDepth();
      } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("STRUCT");
          $$.typeSpec.tagName = $3.str;
          auto node = atToken(mkNode(ASTKind::StructDecl, $3.str), $1.idx);
          for (auto &m : $4.nodeList) addChild(node, m);
          $$.node = node;
      }
    | STRUCT IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "STRUCT");
          $$.typeSpec.parts.push_back("STRUCT");
          $$.typeSpec.tagName = $2.str;
      }
    | STRUCT TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("STRUCT");
          $$.typeSpec.tagName = $2.str;
      }
    | CLASS tag_name {
          declareSymbol($2.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{$2.idx});
          setCategory($2.idx, "CLASS");
          enterClass($2.str, "class");
      } inheritance_opt '{' { pushScope("class " + $2.str); markAggregateMemberDepth(); } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("CLASS");
          $$.typeSpec.tagName = $2.str;
          addTypeName($2.str);
          std::string label = $2.str;
          if (!$4.str.empty()) label += " : " + $4.str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, label), $2.idx);
          node->bases = $4.bases;
          for (auto &m : $7.nodeList) addChild(node, m);
          $$.node = node;
      }
    | CLASS '{' {
          $$.str = anonymousTagAt($1.idx);
          declareSymbol($$.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{$1.idx});
          enterClass($$.str, "class");
          pushScope("class " + $$.str);
          markAggregateMemberDepth();
      } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("CLASS");
          $$.typeSpec.tagName = $3.str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, $3.str), $1.idx);
          for (auto &m : $4.nodeList) addChild(node, m);
          $$.node = node;
      }
    | CLASS IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "CLASS");
          $$.typeSpec.parts.push_back("CLASS");
          $$.typeSpec.tagName = $2.str;
      }
    | CLASS TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("CLASS");
          $$.typeSpec.tagName = $2.str;
      }
    ;

member_decl_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | member_decl_list { $$ = $1; }
    ;

inheritance_opt
    : /* empty */ { $$ = ParserValue(); }
    | ':' inheritance_specifier_list { $$.str = $2.str; $$.bases = $2.bases; }
    ;

inheritance_specifier_list
    : inheritance_specifier { $$.str = $1.str; }
    | inheritance_specifier_list ',' inheritance_specifier {
          $$.str = $1.str + ", " + $3.str;
          for (auto &b : $3.bases) $$.bases.push_back(b);
      }
    ;

inheritance_specifier
    : access_specifier IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "CLASS");
          $$.str = $2.str;
          $$.bases = {{$1.str, $2.str}};
      }
    | access_specifier TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.str = $2.str;
          $$.bases = {{$1.str, $2.str}};
      }
    | IDENTIFIER {
          const Symbol *s = lookupSymbol($1.str);
          setCategory($1.idx, s ? s->typeStr : "CLASS");
          $$.str = $1.str;
          $$.bases = {{"", $1.str}};
      }
    | TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.str = $1.str;
          $$.bases = {{"", $1.str}};
      }
    ;

/* $$.str carries the most recent access specifier, which is stamped
   onto every following member's node (ASTNode::access). */
member_decl_list
    : member_item {
          $$.str.clear();
          if ($1.node) $$.nodeList.push_back($1.node);
          else if ($1.str == "public" || $1.str == "private" || $1.str == "protected") $$.str = $1.str;
      }
    | member_decl_list member_item {
          $$ = $1;
          if ($2.node) {
              if (!$$.str.empty()) $2.node->access = $$.str;
              $$.nodeList.push_back($2.node);
          } else if ($2.str == "public" || $2.str == "private" || $2.str == "protected") {
              $$.str = $2.str;
          }
      }
    ;

member_item
    : declaration { $$.node = $1.node; }
    | function_definition { $$.node = $1.node; }
    | access_specifier ':' { $$ = ParserValue(); $$.str = $1.str; }
    | constructor_def { $$.node = $1.node; }
    | destructor_def { $$.node = $1.node; }
    ;

/* `Name(params)` inside a class: a constructor, either defined here or
   only declared (then defined outside as `Name::Name(params) {...}`).
   The head pushes the parameter scope; whichever rule finishes it pops. */
constructor_head
    : IDENTIFIER '(' { pushScope(currentClassName() + "::" + $1.str + "()"); } parameter_list_opt ')' {
          setCategory($1.idx, "CONSTRUCTOR");
          for (auto &p : $4.paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
          $$ = $1;
          $$.paramList = $4.paramList;
          $$.decl.isVariadic = $4.decl.isVariadic;
      }
    ;

constructor_def
    : constructor_head compound_stmt {
          popScope();
          $$.node = makeConstructorNode($1.str, $1.idx, $1.paramList, $1.decl.isVariadic, currentClassName(), $2.node);
      }
    | constructor_head ';' {
          popScope();
          $$.node = makeConstructorNode($1.str, $1.idx, $1.paramList, $1.decl.isVariadic, currentClassName(), nullptr);
      }
    ;

destructor_head
    : '~' IDENTIFIER '(' ')' {
          setCategory($2.idx, "DESTRUCTOR");
          pushScope(currentClassName() + "::~" + $2.str + "()");
          $$ = $2;
      }
    ;

destructor_def
    : destructor_head compound_stmt {
          popScope();
          $$.node = makeDestructorNode($1.str, $1.idx, currentClassName(), $2.node);
      }
    | destructor_head ';' {
          popScope();
          $$.node = makeDestructorNode($1.str, $1.idx, currentClassName(), nullptr);
      }
    ;

/* `Dog::Dog(int n) { ... }` / `Dog::~Dog() { ... }` after the class */
out_of_class_special
    : TYPE_NAME SCOPE_RES TYPE_NAME '(' {
          setCategory($1.idx, categoryForTypeName(lookupTypeSymbol($1.str)));
          enterClass($1.str);
          pushScope($1.str + "::" + $3.str + "()");
      } parameter_list_opt ')' {
          setCategory($3.idx, "CONSTRUCTOR");
          for (auto &p : $6.paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      } compound_stmt {
          popScope();
          $$.node = makeConstructorNode($3.str, $3.idx, $6.paramList, $6.decl.isVariadic, $1.str, $9.node);
          leaveClass();
      }
    | TYPE_NAME SCOPE_RES '~' TYPE_NAME '(' ')' {
          setCategory($1.idx, categoryForTypeName(lookupTypeSymbol($1.str)));
          setCategory($4.idx, "DESTRUCTOR");
          enterClass($1.str);
          pushScope($1.str + "::~" + $4.str + "()");
      } compound_stmt {
          popScope();
          $$.node = makeDestructorNode($4.str, $4.idx, $1.str, $8.node);
          leaveClass();
      }
    ;

access_specifier
    : PUBLIC
    | PRIVATE
    | PROTECTED
    ;

init_declarator_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | init_declarator_list { $$ = $1; }
    ;

init_declarator_list
    : init_declarator { $$.paramList.push_back($1.decl); markDeclaratorList(); }
    | init_declarator_list ',' init_declarator { $$ = $1; $$.paramList.push_back($3.decl); markDeclaratorList(); }
    ;

init_declarator
    : declarator { $$.decl = $1.decl; }
    | declarator '=' initializer { $$.decl = $1.decl; $$.decl.initExpr = $3.node; }
    ;

initializer
    : assignment_expr { $$.node = $1.node; }
    | '{' '}' { $$.node = atToken(mkNode(ASTKind::InitializerList), $1.idx); }
    | '{' initializer_list '}' {
          auto n = atToken(mkNode(ASTKind::InitializerList), $1.idx);
          for (auto &c : $2.nodeList) addChild(n, c);
          $$.node = n;
      }
    | '{' initializer_list ',' '}' {
          auto n = atToken(mkNode(ASTKind::InitializerList), $1.idx);
          for (auto &c : $2.nodeList) addChild(n, c);
          $$.node = n;
      }
    ;

initializer_list
    : initializer_item { $$.nodeList.push_back($1.node); }
    | initializer_list ',' initializer_item { $$ = $1; $$.nodeList.push_back($3.node); }
    ;

initializer_item
    : initializer { $$.node = $1.node; }
    | '.' IDENTIFIER '=' initializer {
          $$.node = atToken(mkNode(ASTKind::DesignatedInit, "." + $2.str, {$4.node}), $2.idx);
      }
    | '[' constant_expr ']' '=' initializer {
          $$.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {$2.node, $5.node}), $1.idx);
      }
    ;

pointer
    : '*'              { $$.decl.pointerLevel = 1; $$.decl.ptrOps = "*"; }
    | '&'              { $$.decl.pointerLevel = 1; $$.decl.isReference = true; $$.decl.ptrOps = "&"; }
    | pointer '*'      { $$ = $1; $$.decl.pointerLevel++; $$.decl.ptrOps += "*"; }
    | pointer '&'      { $$ = $1; $$.decl.pointerLevel++; $$.decl.ptrOps += "&"; } /* `int *&r` */
    | pointer CONST    { $$ = $1; $$.decl.ptrOps += "c"; }                       /* `int *const p` */
    | pointer VOLATILE { $$ = $1; $$.decl.ptrOps += "v"; }
    ;

declarator
    : pointer direct_declarator {
          $$ = $2;
          $$.decl.pointerLevel += $1.decl.pointerLevel;
          if ($1.decl.isReference) $$.decl.isReference = true;
          $$.decl.ptrOps = $1.decl.ptrOps + $2.decl.ptrOps;
      }
    | direct_declarator { $$ = $1; }
    ;

/* a declarator without a name: `int *`, `char *[]`, `int (*)[3]` --
   for unnamed parameters and in casts / sizeof / new */
abstract_declarator
    : pointer { $$ = $1; }
    | pointer direct_abstract_declarator {
          $$ = $2;
          $$.decl.pointerLevel += $1.decl.pointerLevel;
          if ($1.decl.isReference) $$.decl.isReference = true;
          $$.decl.ptrOps = $1.decl.ptrOps + $2.decl.ptrOps;
      }
    | direct_abstract_declarator { $$ = $1; }
    ;

direct_abstract_declarator
    : ABSTRACT_LPAREN abstract_declarator ')' {
          $$ = $2;
          $$.decl.wasParenGrouped = true;
          $$.decl.grouped = true;
          $$.decl.innerPointerLevel = $2.decl.pointerLevel;
          $$.decl.innerArrayCount = static_cast<int>($2.decl.arrayDims.size());
          $$.decl.innerPtrOps = $2.decl.ptrOps;
          $$.decl.ptrOps.clear();
      }
    | '[' ']' { $$ = ParserValue(); $$.decl.arrayLevel = 1; $$.decl.arrayDims.push_back(nullptr); }
    | '[' assignment_expr ']' { $$ = ParserValue(); $$.decl.arrayLevel = 1; $$.decl.arrayDims.push_back($2.node); }
    | direct_abstract_declarator '[' ']' { $$ = $1; $$.decl.arrayLevel++; $$.decl.arrayDims.push_back(nullptr); }
    | direct_abstract_declarator '[' assignment_expr ']' { $$ = $1; $$.decl.arrayLevel++; $$.decl.arrayDims.push_back($3.node); }
    ;

direct_declarator
    : IDENTIFIER {
          $$.decl.name = $1.str;
          $$.decl.nameIdx = $1.idx;
      }
    | IDENTIFIER SCOPE_RES IDENTIFIER {
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, s ? s->typeStr : "CLASS");
          $$.decl.name = $3.str;
          $$.decl.nameIdx = $3.idx;
          $$.decl.className = $1.str;
      }
    | TYPE_NAME SCOPE_RES IDENTIFIER {
          /* the common case in practice: an out-of-class method
             definition (Dog::bark(...) {...}) is almost always
             written AFTER the class's closing '}', by which point
             its name is already TYPE_NAME, not IDENTIFIER (see the
             typedef lexer-hack note above) */
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.decl.name = $3.str;
          $$.decl.nameIdx = $3.idx;
          $$.decl.className = $1.str;
      }
    | '(' declarator ')' {
          $$ = $2;
          $$.decl.wasParenGrouped = true;
          $$.decl.grouped = true;
          $$.decl.innerPointerLevel = $2.decl.pointerLevel;
          $$.decl.innerArrayCount = static_cast<int>($2.decl.arrayDims.size());
          $$.decl.innerPtrOps = $2.decl.ptrOps;
          $$.decl.ptrOps.clear();
      }
    | operator_function_id {
          $$.decl.name = $1.str;
          $$.decl.nameIdx = $1.idx;
      }
    | IDENTIFIER SCOPE_RES operator_function_id {
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, s ? s->typeStr : "CLASS");
          $$.decl.name = $3.str;
          $$.decl.nameIdx = $3.idx;
          $$.decl.className = $1.str;
      }
    | TYPE_NAME SCOPE_RES operator_function_id {
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.decl.name = $3.str;
          $$.decl.nameIdx = $3.idx;
          $$.decl.className = $1.str;
      }
    | direct_declarator '(' param_scope parameter_list_opt ')' {
          $$ = $1;
          if ($1.decl.wasParenGrouped && $1.decl.pointerLevel > 0) {
              /* `int (*fp)(int)` would declare a pointer to a function;
                 the language has no function pointers, so a parameter
                 list cannot follow a parenthesized pointer declarator */
              popScope();
              yyerror("syntax error, unexpected '(' after a parenthesized pointer declarator");
              YYERROR;
          }
          $$.decl.isFunction = true;
          $$.decl.wasParenGrouped = false; /* consumed */
          $$.decl.params = $4.paramList;
          $$.decl.isVariadic = $4.decl.isVariadic;
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
    | direct_declarator '(' constructor_args ')' {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          $$ = $1;
          auto n = atToken(mkNode(ASTKind::ConstructExpr, $1.decl.name), $2.idx);
          for (auto &a : $3.nodeList) addChild(n, a);
          $$.decl.ctorInit = n;
      }
    | direct_declarator '[' ']' { $$ = $1; $$.decl.arrayLevel++; $$.decl.arrayDims.push_back(nullptr); }
    | direct_declarator '[' assignment_expr ']' { $$ = $1; $$.decl.arrayLevel++; $$.decl.arrayDims.push_back($3.node); }
    ;

/* `operator+`, `operator==`, `operator[]`, ... as a function name */
operator_function_id
    : OPERATOR overloadable_operator { $$ = $1; $$.str = "operator" + $2.str; }
    ;

overloadable_operator
    : '+' { $$.str = "+"; } | '-' { $$.str = "-"; } | '*' { $$.str = "*"; } | '/' { $$.str = "/"; }
    | '%' { $$.str = "%"; } | '^' { $$.str = "^"; } | '&' { $$.str = "&"; } | '|' { $$.str = "|"; }
    | '~' { $$.str = "~"; } | '!' { $$.str = "!"; } | '=' { $$.str = "="; } | '<' { $$.str = "<"; }
    | '>' { $$.str = ">"; } | EQ_OP { $$.str = "=="; } | NE_OP { $$.str = "!="; } | LE_OP { $$.str = "<="; }
    | GE_OP { $$.str = ">="; } | AND_OP { $$.str = "&&"; } | OR_OP { $$.str = "||"; } | SHL { $$.str = "<<"; }
    | SHR { $$.str = ">>"; } | INC { $$.str = "++"; } | DEC { $$.str = "--"; }
    | PLUS_ASSIGN { $$.str = "+="; } | MINUS_ASSIGN { $$.str = "-="; } | MUL_ASSIGN { $$.str = "*="; }
    | DIV_ASSIGN { $$.str = "/="; } | MOD_ASSIGN { $$.str = "%="; } | AND_ASSIGN { $$.str = "&="; }
    | OR_ASSIGN { $$.str = "|="; } | XOR_ASSIGN { $$.str = "^="; } | SHL_ASSIGN { $$.str = "<<="; }
    | SHR_ASSIGN { $$.str = ">>="; } | '[' ']' { $$.str = "[]"; } | '(' ')' { $$.str = "()"; }
    ;

/* the parameter list's own scope, only used to keep parameter names out
   of the enclosing scope while it is scanned; function_definition
   re-declares them in the real body scope */
param_scope
    : /* empty */ %prec PREFER_DECLARATION { pushScope(); }
    ;

constructor_args
    : assignment_expr { $$.nodeList.push_back($1.node); }
    | constructor_args ',' assignment_expr { $$ = $1; $$.nodeList.push_back($3.node); }
    ;

parameter_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | parameter_list { $$ = $1; }
    ;

parameter_list
    : parameter_decl {
          if ($1.decl.nameIdx >= 0 || !$1.decl.typeStr.empty()) $$.paramList.push_back($1.decl);
          $$.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
    | parameter_list ',' parameter_decl {
          $$ = $1;
          $$.paramList.push_back($3.decl);
      }
    | parameter_list ',' ELLIPSIS { $$ = $1; $$.decl.isVariadic = true; }
    ;

parameter_decl
    : declaration_specifiers declarator {
          $$.decl = $2.decl;
          $$.decl.typeStr = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, $2.decl.arrayLevel);
          $$.decl.typeExpr = makeTypeExpr($1.typeSpec, $$.decl);
      }
    | declaration_specifiers abstract_declarator {
          $$.decl = $2.decl;
          $$.decl.typeStr = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, $2.decl.arrayLevel);
          $$.decl.typeExpr = makeTypeExpr($1.typeSpec, $$.decl);
      }
    | declaration_specifiers {
          $$.decl = DeclInfo();
          $$.decl.typeStr = computeTypeStr($1.typeSpec, 0, 0);
          $$.decl.typeExpr = makeTypeExpr($1.typeSpec, $$.decl);
      }
    ;

function_definition
    : declaration_specifiers declarator {
          bool outOfClass = !$2.decl.className.empty();
          if (outOfClass) enterClass($2.decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : $2.decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle($2.decl.name, paramExprs($2.decl.params), $2.decl.isVariadic, currentClassName());
          std::string returnType = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, $2.decl.arrayLevel);
          SymbolDeclInfo extra;
          extra.tokenIdx = $2.decl.nameIdx;
          extra.isStatic = $1.typeSpec.isStatic;
          extra.isConst = $1.typeSpec.isConst;
          extra.isVolatile = $1.typeSpec.isVolatile;
          extra.pointerLevel = $2.decl.pointerLevel;
          extra.arrayLevel = $2.decl.arrayLevel;
          extra.returnType = returnType;
          extra.paramTypes = paramTypes;
          extra.mangledName = mangled;
          declareSymbol($2.decl.name, SymKind::PROCEDURE, "PROCEDURE", extra);
          setCategory($2.decl.nameIdx, "PROCEDURE");
          /* deliberately NOT calling leaveClass() here for the
             out-of-class case (Dog::bark() {...}) -- class context
             needs to stay active through the whole body, so `this`
             used inside it is correctly recognized as valid. Left at
             the very end, in the final action, once the body is
             fully parsed. */
          pushScope($2.decl.name + "()");
          for (auto &p : $2.decl.params) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      } '{' block_item_list_opt '}' {
          popScope();
          bool outOfClass = !$2.decl.className.empty();
          /* currentClassName() is still correctly set here for the
             out-of-class case -- it was never left, see above -- so
             no need to re-enter it just to compute the mangled name
             again. */
          std::vector<std::string> paramTypes;
          for (auto &p : $2.decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle($2.decl.name, paramExprs($2.decl.params), $2.decl.isVariadic, currentClassName());
          if (outOfClass) leaveClass();
          auto node = atToken(mkNode(ASTKind::FunctionDef, $2.decl.name + " : " + mangled), $2.decl.nameIdx);
          node->typeExpr = makeTypeExpr($1.typeSpec, $2.decl);
          for (auto &p : $2.decl.params) {
              if (!p.name.empty()) {
                  auto pn = atToken(mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr), p.nameIdx);
                  pn->typeExpr = p.typeExpr;
                  addChild(node, pn);
              }
          }
          auto body = atToken(mkNode(ASTKind::CompoundStmt), $4.idx);
          for (auto &s : $5.nodeList) addChild(body, s);
          addChild(node, body);
          $$.node = node;
      }
    ;

statement
    : compound_stmt { $$.node = $1.node; }
    | expr_stmt { $$.node = $1.node; }
    | selection_stmt { $$.node = $1.node; }
    | iteration_stmt { $$.node = $1.node; }
    | jump_stmt { $$.node = $1.node; }
    | labeled_stmt { $$.node = $1.node; }
    | declaration { $$.node = $1.node; }
    | error ';' { $$.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
    | error '}' { $$.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
    ;

compound_stmt
    : '{' { pushScope(); } block_item_list_opt '}' {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), $1.idx);
          for (auto &s : $3.nodeList) addChild(n, s);
          $$.node = n;
      }
    ;

block_item_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | block_item_list { $$ = $1; }
    ;

block_item_list
    : statement { if ($1.node) $$.nodeList.push_back($1.node); }
    | block_item_list statement { $$ = $1; if ($2.node) $$.nodeList.push_back($2.node); }
    ;

expr_stmt
    : ';' { $$.node = atToken(mkNode(ASTKind::EmptyStmt), $1.idx); }
    | expr ';' { $$.node = atNode(mkNode(ASTKind::ExprStmt, "", {$1.node}), $1.node); }
    ;

selection_stmt
    : IF '(' expr ')' statement %prec IFX {
          $$.node = atToken(mkNode(ASTKind::IfStmt, "", {$3.node, $5.node}), $1.idx);
      }
    | IF '(' expr ')' statement ELSE statement {
          $$.node = atToken(mkNode(ASTKind::IfStmt, "", {$3.node, $5.node, $7.node}), $1.idx);
      }
    | SWITCH '(' expr ')' { hintScope("switch"); } compound_stmt {
          $$.node = atToken(mkNode(ASTKind::SwitchStmt, "", {$3.node, $6.node}), $1.idx);
      }
    ;

labeled_stmt
    : CASE constant_expr ':' statement {
          $$.node = atToken(mkNode(ASTKind::CaseStmt, "", {$2.node, $4.node}), $1.idx);
      }
    | DEFAULT ':' statement {
          $$.node = atToken(mkNode(ASTKind::DefaultStmt, "", {$3.node}), $1.idx);
      }
    | IDENTIFIER ':' statement {
          declareSymbol($1.str, SymKind::LABEL, "LABEL", SymbolDeclInfo{$1.idx});
          setCategory($1.idx, "LABEL");
          $$.node = atToken(mkNode(ASTKind::LabeledStmt, $1.str, {$3.node}), $1.idx);
      }
    ;

iteration_stmt
    : WHILE '(' expr ')' statement {
          $$.node = atToken(mkNode(ASTKind::WhileStmt, "", {$3.node, $5.node}), $1.idx);
      }
    | DO statement WHILE '(' expr ')' ';' {
          $$.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {$2.node, $5.node}), $1.idx);
      }
    /* Local recovery for a broken tail. Without these, Bison's error
       recovery popped back to the state right after `do`, accepted
       `error` there as the loop *body*, and then waited for a `while`
       that never came -- losing the rest of the file (test16). */
    | DO statement WHILE '(' expr ')' error {
          /* only the ';' is missing: resume right at the next statement */
          $$.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
    | DO statement error ';' {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          $$.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
    | UNTIL '(' expr ')' statement {
          $$.node = atToken(mkNode(ASTKind::UntilStmt, "", {$3.node, $5.node}), $1.idx);
      }
    | for_open expr_stmt expr_stmt for_incr_opt ')' statement {
          popScope();
          $$.node = atToken(mkNode(ASTKind::ForStmt, "", {$2.node, $3.node, $4.node, $6.node}), $1.idx);
      }
    | for_open declaration expr_stmt for_incr_opt ')' statement {
          popScope();
          $$.node = atToken(mkNode(ASTKind::ForStmt, "", {$2.node, $3.node, $4.node, $6.node}), $1.idx);
      }
    ;

/* opens the for statement's scope before either form is recognised, so
   `for (T x ...` vs `for (T(...) ...` never forces an early choice */
for_open
    : FOR '(' { pushScope("for"); $$ = $1; }
    ;

for_incr_opt
    : /* empty */ { $$ = ParserValue(); }
    | expr { $$.node = $1.node; }
    ;

jump_stmt
    : BREAK ';' { $$.node = atToken(mkNode(ASTKind::BreakStmt), $1.idx); }
    | CONTINUE ';' { $$.node = atToken(mkNode(ASTKind::ContinueStmt), $1.idx); }
    | RETURN ';' { $$.node = atToken(mkNode(ASTKind::ReturnStmt), $1.idx); }
    | RETURN expr ';' { $$.node = atToken(mkNode(ASTKind::ReturnStmt, "", {$2.node}), $1.idx); }
    | GOTO IDENTIFIER ';' {
          const Symbol *s = lookupSymbol($2.str);
          if (s) setCategory($2.idx, "LABEL");
          else queuePendingReference($2.idx, $2.str, /*isLabel=*/true);
          recordUsage(s);
          $$.node = atToken(mkNode(ASTKind::GotoStmt, $2.str), $2.idx);
      }
    ;

expr
    : assignment_expr { $$.node = $1.node; }
    | expr ',' assignment_expr { $$.node = atToken(mkNode(ASTKind::CommaExpr, "", {$1.node, $3.node}), $2.idx); }
    ;

assignment_expr
    : binary_expr { $$.node = $1.node; }
    | unary_expr assign_op assignment_expr {
          $$.node = atToken(mkNode(ASTKind::AssignExpr, $2.str, {$1.node, $3.node}), $2.idx);
      }
    ;

assign_op
    : '='          { $$.str = "="; }
    | PLUS_ASSIGN  { $$.str = "+="; }
    | MINUS_ASSIGN { $$.str = "-="; }
    | MUL_ASSIGN   { $$.str = "*="; }
    | DIV_ASSIGN   { $$.str = "/="; }
    | MOD_ASSIGN   { $$.str = "%="; }
    | AND_ASSIGN   { $$.str = "&="; }
    | OR_ASSIGN    { $$.str = "|="; }
    | XOR_ASSIGN   { $$.str = "^="; }
    | SHL_ASSIGN   { $$.str = "<<="; }
    | SHR_ASSIGN   { $$.str = ">>="; }
    ;

constant_expr
    : binary_expr { $$.node = $1.node; }
    ;

binary_expr
    : binary_expr OR_OP binary_expr  { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {$1.node, $3.node}), $2.idx); }
    | binary_expr AND_OP binary_expr { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {$1.node, $3.node}), $2.idx); }
    | binary_expr '|' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {$1.node, $3.node}), $2.idx); }
    | binary_expr '^' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {$1.node, $3.node}), $2.idx); }
    | binary_expr '&' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {$1.node, $3.node}), $2.idx); }
    | binary_expr EQ_OP binary_expr  { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {$1.node, $3.node}), $2.idx); }
    | binary_expr NE_OP binary_expr  { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {$1.node, $3.node}), $2.idx); }
    | binary_expr '<' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {$1.node, $3.node}), $2.idx); }
    | binary_expr '>' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {$1.node, $3.node}), $2.idx); }
    | binary_expr LE_OP binary_expr  { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {$1.node, $3.node}), $2.idx); }
    | binary_expr GE_OP binary_expr  { $$.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {$1.node, $3.node}), $2.idx); }
    | binary_expr SHL binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {$1.node, $3.node}), $2.idx); }
    | binary_expr SHR binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {$1.node, $3.node}), $2.idx); }
    | binary_expr '+' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {$1.node, $3.node}), $2.idx); }
    | binary_expr '-' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {$1.node, $3.node}), $2.idx); }
    | binary_expr '*' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {$1.node, $3.node}), $2.idx); }
    | binary_expr '/' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {$1.node, $3.node}), $2.idx); }
    | binary_expr '%' binary_expr    { $$.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {$1.node, $3.node}), $2.idx); }
    | binary_expr '?' expr ':' binary_expr {
          $$.node = atToken(mkNode(ASTKind::TernaryExpr, "", {$1.node, $3.node, $5.node}), $2.idx);
      }
    | unary_expr { $$.node = $1.node; }
    ;

unary_expr
    : postfix_expr { $$.node = $1.node; }
    | INC unary_expr { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {$2.node}), $1.idx); }
    | DEC unary_expr { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {$2.node}), $1.idx); }
    | '&' unary_expr %prec ADDR  { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {$2.node}), $1.idx); }
    | '*' unary_expr %prec DEREF { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {$2.node}), $1.idx); }
    | '+' unary_expr %prec UMINUS { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {$2.node}), $1.idx); }
    | '-' unary_expr %prec UMINUS { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {$2.node}), $1.idx); }
    | '!' unary_expr { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {$2.node}), $1.idx); }
    | '~' unary_expr { $$.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {$2.node}), $1.idx); }
    | '(' type_name ')' unary_expr %prec CAST {
          $$.node = atToken(mkNode(ASTKind::CastExpr, $2.str, {$4.node}), $1.idx);
          $$.node->typeExpr = makeTypeExpr($2.typeSpec, $2.decl);
      }
    | SIZEOF unary_expr %prec CAST { $$.node = atToken(mkNode(ASTKind::SizeofExpr, "", {$2.node}), $1.idx); }
    | SIZEOF '(' type_name ')' %prec SIZEOF_TYPE {
          $$.node = atToken(mkNode(ASTKind::SizeofExpr, $3.str), $1.idx);
          $$.node->typeExpr = makeTypeExpr($3.typeSpec, $3.decl);
      }
    | NEW new_type_id {
          $$.node = atToken(mkNode(ASTKind::NewExpr, $2.str), $1.idx);
          $$.node->typeExpr = makeTypeExpr($2.typeSpec, $2.decl);
      }
    | NEW new_type_id '(' constructor_args_opt ')' {
          $$.node = atToken(mkNode(ASTKind::NewExpr, $2.str), $1.idx);
          $$.node->typeExpr = makeTypeExpr($2.typeSpec, $2.decl);
          auto c = atToken(mkNode(ASTKind::ConstructExpr, $2.str), $3.idx);
          c->typeExpr = $$.node->typeExpr;
          for (auto &a : $4.nodeList) addChild(c, a);
          addChild($$.node, c);
      }
    | DELETE unary_expr { $$.node = atToken(mkNode(ASTKind::DeleteExpr, "", {$2.node}), $1.idx); }
    | DELETE_ARRAY unary_expr { $$.node = atToken(mkNode(ASTKind::DeleteExpr, "[]", {$2.node}), $1.idx); }
    ;

type_name
    : type_name_specifiers {
          $$.str = computeTypeStr($1.typeSpec, 0, 0);
          $$.decl = DeclInfo();
      }
    | type_name_specifiers abstract_declarator {
          $$.str = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, $2.decl.arrayLevel);
          $$.decl = $2.decl;
      }
    ;

/* the type in `new T`, `new T *`, `new T[n]`: only pointers and array
   sizes, so a following '(' is always the constructor arguments */
new_type_id
    : type_name_specifiers %prec NEW_TYPE_END {
          $$.str = computeTypeStr($1.typeSpec, 0, 0);
          $$.decl = DeclInfo();
      }
    | type_name_specifiers new_pointer %prec NEW_TYPE_END {
          $$.str = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, 0);
          $$.decl = $2.decl;
      }
    | type_name_specifiers new_array_dims {
          $$.str = computeTypeStr($1.typeSpec, 0, $2.decl.arrayLevel);
          $$.decl = $2.decl;
      }
    | type_name_specifiers new_pointer new_array_dims {
          $$.str = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, $3.decl.arrayLevel);
          $$.decl = $3.decl;
          $$.decl.pointerLevel = $2.decl.pointerLevel;
          $$.decl.ptrOps = $2.decl.ptrOps;
      }
    ;

new_pointer
    : '*'             { $$.decl = DeclInfo(); $$.decl.pointerLevel = 1; $$.decl.ptrOps = "*"; }
    | new_pointer '*' { $$ = $1; $$.decl.pointerLevel++; $$.decl.ptrOps += "*"; }
    ;

/* the first size of `new T[n]` may be any expression (checked later) */
new_array_dims
    : '[' expr ']' { $$.decl = DeclInfo(); $$.decl.arrayLevel = 1; $$.decl.arrayDims.push_back($2.node); }
    | new_array_dims '[' expr ']' { $$ = $1; $$.decl.arrayLevel++; $$.decl.arrayDims.push_back($3.node); }
    ;

type_name_specifiers
    : type_name_specifiers type_name_specifier {
          $$ = $1;
          for (auto &p : $2.typeSpec.parts) $$.typeSpec.parts.push_back(p);
          if ($2.typeSpec.isConst) $$.typeSpec.isConst = true;
          if ($2.typeSpec.isVolatile) $$.typeSpec.isVolatile = true;
          if (!$2.typeSpec.tagName.empty()) $$.typeSpec.tagName = $2.typeSpec.tagName;
          if (!$2.typeSpec.typedefName.empty()) $$.typeSpec.typedefName = $2.typeSpec.typedefName;
      }
    | type_name_specifier { $$ = $1; }
    ;

type_name_specifier
    : INT      %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("INT"); }
    | CHAR     %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("CHAR"); }
    | FLOAT    %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("FLOAT"); }
    | DOUBLE   %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("DOUBLE"); }
    | VOID     %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("VOID"); }
    | BOOL     %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("BOOL"); }
    | SHORT    %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("SHORT"); }
    | LONG     %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("LONG"); }
    | SIGNED   %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("SIGNED"); }
    | UNSIGNED %prec PREFER_EXPRESSION { $$.typeSpec.parts.push_back("UNSIGNED"); }
    | VA_LIST  { $$.typeSpec.parts.push_back("VA_LIST"); }
    | CONST    { $$ = ParserValue(); $$.typeSpec.isConst = true; }
    | VOLATILE { $$ = ParserValue(); $$.typeSpec.isVolatile = true; }
    | TYPE_NAME %prec PREFER_EXPRESSION {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          $$.typeSpec.typedefName = $1.str;
      }
    | STRUCT IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "STRUCT");
          $$.typeSpec.parts.push_back("STRUCT");
          $$.typeSpec.tagName = $2.str;
      }
    | STRUCT TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("STRUCT");
          $$.typeSpec.tagName = $2.str;
      }
    | CLASS IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "CLASS");
          $$.typeSpec.parts.push_back("CLASS");
          $$.typeSpec.tagName = $2.str;
      }
    | CLASS TYPE_NAME {
          const Symbol *s = lookupTypeSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("CLASS");
          $$.typeSpec.tagName = $2.str;
      }
    ;

postfix_expr
    : primary_expr { $$.node = $1.node; }
    | postfix_expr '[' expr ']' { $$.node = atToken(mkNode(ASTKind::IndexExpr, "", {$1.node, $3.node}), $2.idx); }
    | postfix_expr '(' argument_list_opt ')' {
          auto n = atNode(mkNode(ASTKind::CallExpr, "", {$1.node}), $1.node);
          for (auto &a : $3.nodeList) addChild(n, a);

          if ($1.node && $1.node->kind == ASTKind::Identifier) {
              const std::string &calleeName = $1.node->label;
              if (isOverloaded(calleeName)) {
                  std::vector<std::string> argTypes;
                  bool allKnown = true;
                  for (auto &a : $3.nodeList) {
                      std::string t = inferExprType(a);
                      if (t.empty()) { allKnown = false; break; }
                      argTypes.push_back(t);
                  }
                  const Symbol *matched = allKnown ? lookupOverload(calleeName, argTypes) : nullptr;
                  if (matched) {
                      recordUsage(matched);
                      n->label = matched->mangledName; /* which overload this
                                                            call actually
                                                            resolved to */
                  } else {
                      /* couldn't confidently type every argument, or none
                         matched exactly -- fall back rather than guess */
                      recordUsage(lookupSymbol(calleeName));
                  }
              }
              /* not overloaded: primary_expr's IDENTIFIER handling
                 already called recordUsage() for this exact occurrence
                 (it only defers/skips that when the name IS
                 overloaded) -- calling it again here would double-count
                 every non-overloaded call, which is the common case. */
          }

          $$.node = n;
      }
    | postfix_expr '.' IDENTIFIER {
          if ($1.node && $1.node->kind == ASTKind::Identifier) {
              const Symbol *base = lookupSymbol($1.node->label);
              if (base && !base->aggregateTagName.empty()) {
                  const SymbolTableEntry *member = findMember(base->aggregateTagName, $3.str);
                  if (member) setCategory($3.idx, member->typeStr);
              }
          }
          $$.node = atToken(mkNode(ASTKind::MemberExpr, $3.str, {$1.node}), $3.idx);
      }
    | postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          $$.node = atToken(mkNode(ASTKind::MemberExpr, $5.str, {$1.node}), $5.idx);
          $$.node->typeExpr = std::make_shared<ASTTypeExpr>();
          $$.node->typeExpr->className = $3.str;
      }
    | postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER {
          $$.node = atToken(mkNode(ASTKind::ArrowExpr, $5.str, {$1.node}), $5.idx);
          $$.node->typeExpr = std::make_shared<ASTTypeExpr>();
          $$.node->typeExpr->className = $3.str;
      }
    | postfix_expr ARROW IDENTIFIER {
          if ($1.node && $1.node->kind == ASTKind::Identifier) {
              const Symbol *base = lookupSymbol($1.node->label);
              if (base && !base->aggregateTagName.empty()) {
                  const SymbolTableEntry *member = findMember(base->aggregateTagName, $3.str);
                  if (member) setCategory($3.idx, member->typeStr);
              }
          }
          $$.node = atToken(mkNode(ASTKind::ArrowExpr, $3.str, {$1.node}), $3.idx);
      }
    | postfix_expr SCOPE_RES IDENTIFIER { $$.node = atToken(mkNode(ASTKind::ScopeExpr, $3.str, {$1.node}), $3.idx); }
    | postfix_expr INC { $$.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {$1.node}), $2.idx); }
    | postfix_expr DEC { $$.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {$1.node}), $2.idx); }
    | builtin_call { $$.node = $1.node; }
    ;

builtin_call
    : PRINTF '(' argument_list_opt ')'  { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), $1.idx);  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | SCANF '(' argument_list_opt ')'   { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), $1.idx);   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | MALLOC '(' argument_list_opt ')'  { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), $1.idx);  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FREE '(' argument_list_opt ')'    { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), $1.idx);    for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | CALLOC '(' argument_list_opt ')'  { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), $1.idx);  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | REALLOC '(' argument_list_opt ')' { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), $1.idx); for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | VA_START '(' argument_list_opt ')' { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), $1.idx); for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | VA_ARG '(' argument_list_opt ')'   { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), $1.idx);   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | VA_END '(' argument_list_opt ')'   { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), $1.idx);   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    ;

constructor_args_opt
    : /* empty */ { $$ = ParserValue(); }
    | constructor_args { $$ = $1; }
    ;

argument_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | argument_list { $$ = $1; }
    ;

argument_list
    : argument { $$.nodeList.push_back($1.node); }
    | argument_list ',' argument { $$ = $1; $$.nodeList.push_back($3.node); }
    ;

argument
    : assignment_expr { $$.node = $1.node; }
    | type_name {
          $$.node = mkNode(ASTKind::TypeNameNode, $1.str);
          $$.node->typeExpr = makeTypeExpr($1.typeSpec, $1.decl);
      }
    ;

primary_expr
    : IDENTIFIER {
          const Symbol *s = lookupSymbol($1.str);
          if (s) setCategory($1.idx, s->typeStr);
          else queuePendingReference($1.idx, $1.str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded($1.str))) {
              recordUsage(s);
          }
          $$.node = atToken(mkNode(ASTKind::Identifier, $1.str), $1.idx);
      }
    | INT_LITERAL    { $$.node = atToken(mkNode(ASTKind::IntLiteral, $1.str), $1.idx); }
    | FLOAT_LITERAL  { $$.node = atToken(mkNode(ASTKind::FloatLiteral, $1.str), $1.idx); }
    | CHAR_LITERAL   { $$.node = atToken(mkNode(ASTKind::CharLiteral, $1.str), $1.idx); }
    | string_literal { $$.node = $1.node; }
    | BOOL_LITERAL { $$.node = atToken(mkNode(ASTKind::BoolLiteral, $1.str), $1.idx); }
    | THIS { $$.node = atToken(mkNode(ASTKind::ThisExpr), $1.idx); }
    | TYPE_NAME '(' constructor_args_opt ')' {
          /* `Dog(4)`: a temporary object (for a scalar type, a cast) */
          $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList);
      }
    | FCAST '(' constructor_args_opt ')' {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList);
      }
    /* `int(x)`, `double(n)`: functional casts. Where a declaration could
       also start (`int (x);`), the declaration wins -- see %precedence. */
    | INT '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | CHAR '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | FLOAT '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | DOUBLE '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | VOID '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | BOOL '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | SHORT '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | LONG '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | SIGNED '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | UNSIGNED '(' constructor_args_opt ')' { $$.node = makeFunctionalCast($1.str, $1.idx, $3.nodeList); }
    | TYPE_NAME SCOPE_RES IDENTIFIER {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, $1.str), $1.idx);
          $$.node = atToken(mkNode(ASTKind::ScopeExpr, $3.str, {base}), $3.idx);
      }
    | '(' expr ')' { $$.node = $2.node; }
    ;

/* adjacent literals are one string, as in C: "adj" "acent" == "adjacent" */
string_literal
    : STRING_LITERAL { $$.node = atToken(mkNode(ASTKind::StringLiteral, $1.str), $1.idx); }
    | string_literal STRING_LITERAL {
          $$ = $1;
          std::string &text = $$.node->label;
          text = text.substr(0, text.size() - 1) + $2.str.substr(1);
      }
    ;

%%

void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
