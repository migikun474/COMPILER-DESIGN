%code requires {
    #include "common.h"
}

%define api.value.type {ParserValue}
%define parse.error verbose
%locations

%code {
    #include <cstdio>
    #include <cstring>
    #include <string>
    extern int yylex();
    extern FILE *yyin;
    extern int yylineno;
    void yyerror(const char *s);
}

/* ---- keywords ---- */
%token INT CHAR FLOAT DOUBLE VOID SHORT LONG SIGNED UNSIGNED
%token STRUCT ENUM UNION CLASS
%token PUBLIC PRIVATE PROTECTED THIS
%token STATIC TYPEDEF AUTO CONST VOLATILE
%token IF ELSE FOR WHILE DO UNTIL SWITCH CASE DEFAULT
%token BREAK CONTINUE GOTO RETURN
%token PRINTF SCANF MALLOC FREE CALLOC REALLOC
%token FILE_KW FOPEN FCLOSE FREAD FWRITE FPRINTF FSCANF FGETS FPUTS FEOF
%token BOOL
%token NEW DELETE SIZEOF

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
%nonassoc IFX
%nonassoc ELSE

%%

/* ======================================================================
   TRANSLATION UNIT
   ====================================================================== */
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
    | error ';'  { yyerrok; }
    | error '}'  { yyerrok; }
    ;

/* ======================================================================
   DECLARATIONS
   ====================================================================== */
declaration
    : declaration_specifiers init_declarator_list_opt ';' {
          std::vector<ASTNodePtr> declNodes;
          for (auto &d : $2.paramList) {
              auto n = registerDeclarator(d, $1.typeSpec);
              if (n) declNodes.push_back(n);
          }
          if (declNodes.empty()) {
              $$.node = $1.node; /* bare struct/class/enum/union declaration */
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
          if ($2.typeSpec.isConst) $$.typeSpec.isConst = true;
          if ($2.typeSpec.isVolatile) $$.typeSpec.isVolatile = true;
          if ($2.node) $$.node = $2.node;
      }
    | storage_or_type_specifier { $$ = $1; }
    ;

storage_or_type_specifier
    : STATIC   { $$.typeSpec.isStatic = true; }
    | AUTO     { $$ = ParserValue(); }
    | TYPEDEF  { $$.typeSpec.isTypedefStorage = true; }
    | CONST    { $$.typeSpec.isConst = true; } /* now actually tracked -- see Symbol/SymbolTableEntry */
    | VOLATILE { $$.typeSpec.isVolatile = true; }
    | type_specifier { $$ = $1; }
    ;

type_specifier
    : INT      { $$.typeSpec.parts.push_back("INT"); }
    | CHAR     { $$.typeSpec.parts.push_back("CHAR"); }
    | FLOAT    { $$.typeSpec.parts.push_back("FLOAT"); }
    | DOUBLE   { $$.typeSpec.parts.push_back("DOUBLE"); }
    | VOID     { $$.typeSpec.parts.push_back("VOID"); }
    | BOOL     { $$.typeSpec.parts.push_back("BOOL"); }
    | SHORT    { $$.typeSpec.parts.push_back("SHORT"); }
    | LONG     { $$.typeSpec.parts.push_back("LONG"); }
    | SIGNED   { $$.typeSpec.parts.push_back("SIGNED"); }
    | UNSIGNED { $$.typeSpec.parts.push_back("UNSIGNED"); }
    | FILE_KW  { $$.typeSpec.parts.push_back("FILE"); }
    | TYPE_NAME {
          const Symbol *s = lookupSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back(s ? s->typeStr : "INT");
      }
    | struct_or_class_specifier { $$ = $1; }
    ;

struct_or_class_specifier
    : STRUCT IDENTIFIER {
          declareSymbol($2.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{$2.idx});
          setCategory($2.idx, "STRUCT");
          enterClass($2.str);
      } '{' { pushScope(); } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("STRUCT");
          g_typedefNames.insert($2.str); /* usable as a type from here on, but
                                             NOT inside its own body -- lets
                                             constructors/destructors keep
                                             matching the class's own name as
                                             a plain IDENTIFIER */
          auto node = mkNode(ASTKind::StructDecl, $2.str);
          for (auto &m : $6.nodeList) addChild(node, m);
          $$.node = node;
      }
    | STRUCT IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "STRUCT");
          $$.typeSpec.parts.push_back("STRUCT");
      }
    | STRUCT TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("STRUCT");
      }
    | UNION IDENTIFIER {
          declareSymbol($2.str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{$2.idx});
          setCategory($2.idx, "UNION");
          enterClass($2.str);
      } '{' { pushScope(); } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("UNION");
          g_typedefNames.insert($2.str);
          auto node = mkNode(ASTKind::UnionDecl, $2.str);
          for (auto &m : $6.nodeList) addChild(node, m);
          $$.node = node;
      }
    | UNION IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "UNION");
          $$.typeSpec.parts.push_back("UNION");
      }
    | UNION TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("UNION");
      }
    | CLASS IDENTIFIER {
          declareSymbol($2.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{$2.idx});
          setCategory($2.idx, "CLASS");
          enterClass($2.str);
      } inheritance_opt '{' { pushScope(); } member_decl_list_opt '}' {
          popScope(); leaveClass();
          $$.typeSpec.parts.push_back("CLASS");
          g_typedefNames.insert($2.str);
          std::string label = $2.str;
          if (!$4.str.empty()) label += " : " + $4.str;
          auto node = mkNode(ASTKind::ClassDecl, label);
          for (auto &m : $7.nodeList) addChild(node, m);
          $$.node = node;
      }
    | CLASS IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "CLASS");
          $$.typeSpec.parts.push_back("CLASS");
      }
    | CLASS TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("CLASS");
      }
    | ENUM IDENTIFIER {
          declareSymbol($2.str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{$2.idx});
          setCategory($2.idx, "ENUM");
      } '{' enumerator_list '}' {
          $$.typeSpec.parts.push_back("ENUM");
          g_typedefNames.insert($2.str);
          auto node = mkNode(ASTKind::EnumDecl, $2.str);
          for (auto &e : $5.nodeList) addChild(node, e);
          $$.node = node;
      }
    | ENUM IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "ENUM");
          $$.typeSpec.parts.push_back("ENUM");
      }
    | ENUM TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("ENUM");
      }
    ;

member_decl_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | member_decl_list { $$ = $1; }
    ;

inheritance_opt
    : /* empty */ { $$ = ParserValue(); }
    | ':' inheritance_specifier_list { $$.str = $2.str; }
    ;

inheritance_specifier_list
    : inheritance_specifier { $$.str = $1.str; }
    | inheritance_specifier_list ',' inheritance_specifier { $$.str = $1.str + ", " + $3.str; }
    ;

inheritance_specifier
    : access_specifier IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "CLASS");
          $$.str = $2.str;
      }
    | access_specifier TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.str = $2.str;
      }
    | IDENTIFIER {
          const Symbol *s = lookupSymbol($1.str);
          setCategory($1.idx, s ? s->typeStr : "CLASS");
          $$.str = $1.str;
      }
    | TYPE_NAME {
          const Symbol *s = lookupSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.str = $1.str;
      }
    ;

member_decl_list
    : member_item { if ($1.node) $$.nodeList.push_back($1.node); }
    | member_decl_list member_item { $$ = $1; if ($2.node) $$.nodeList.push_back($2.node); }
    ;

member_item
    : declaration { $$.node = $1.node; }
    | function_definition { $$.node = $1.node; }
    | access_specifier ':' { $$ = ParserValue(); }
    | constructor_def { $$.node = $1.node; }
    | destructor_def { $$.node = $1.node; }
    ;

constructor_def
    : IDENTIFIER '(' { pushScope(); } parameter_list_opt ')' {
          setCategory($1.idx, "CONSTRUCTOR");
          for (auto &p : $4.paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      } compound_stmt {
          popScope();
          std::vector<std::string> paramTypes;
          for (auto &p : $4.paramList) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle($1.str, paramTypes, currentClassName());
          SymbolDeclInfo extra;
          extra.tokenIdx = $1.idx;
          extra.returnType = "VOID";
          extra.paramTypes = paramTypes;
          extra.mangledName = mangled;
          declareSymbol($1.str, SymKind::PROCEDURE, "CONSTRUCTOR", extra);
          auto node = mkNode(ASTKind::ConstructorDef, $1.str + " : " + mangled);
          for (auto &p : $4.paramList) {
              if (!p.name.empty()) addChild(node, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
          }
          addChild(node, $7.node);
          $$.node = node;
      }
    ;

destructor_def
    : '~' IDENTIFIER '(' ')' {
          setCategory($2.idx, "DESTRUCTOR");
          pushScope();
      } compound_stmt {
          popScope();
          std::string mangled = mangle("~" + $2.str, {}, currentClassName());
          SymbolDeclInfo extra;
          extra.tokenIdx = $2.idx;
          extra.returnType = "VOID";
          extra.mangledName = mangled;
          declareSymbol("~" + $2.str, SymKind::PROCEDURE, "DESTRUCTOR", extra);
          auto node = mkNode(ASTKind::DestructorDef, $2.str + " : " + mangled);
          addChild(node, $6.node);
          $$.node = node;
      }
    ;

access_specifier
    : PUBLIC
    | PRIVATE
    | PROTECTED
    ;

enumerator_list
    : enumerator { $$.nodeList.push_back($1.node); }
    | enumerator_list ',' enumerator { $$ = $1; $$.nodeList.push_back($3.node); }
    ;

enumerator
    : IDENTIFIER {
          declareSymbol($1.str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{$1.idx});
          setCategory($1.idx, "ENUM_CONSTANT");
          $$.node = mkNode(ASTKind::Enumerator, $1.str);
      }
    | IDENTIFIER '=' constant_expr {
          declareSymbol($1.str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{$1.idx});
          setCategory($1.idx, "ENUM_CONSTANT");
          $$.node = mkNode(ASTKind::Enumerator, $1.str, {$3.node});
      }
    ;

init_declarator_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | init_declarator_list { $$ = $1; }
    ;

init_declarator_list
    : init_declarator { $$.paramList.push_back($1.decl); }
    | init_declarator_list ',' init_declarator { $$ = $1; $$.paramList.push_back($3.decl); }
    ;

init_declarator
    : declarator { $$.decl = $1.decl; }
    | declarator '=' initializer { $$.decl = $1.decl; $$.decl.initExpr = $3.node; }
    ;

initializer
    : assignment_expr { $$.node = $1.node; }
    | '{' initializer_list '}' {
          auto n = mkNode(ASTKind::InitializerList);
          for (auto &c : $2.nodeList) addChild(n, c);
          $$.node = n;
      }
    | '{' initializer_list ',' '}' {
          auto n = mkNode(ASTKind::InitializerList);
          for (auto &c : $2.nodeList) addChild(n, c);
          $$.node = n;
      }
    ;

initializer_list
    : initializer { $$.nodeList.push_back($1.node); }
    | initializer_list ',' initializer { $$ = $1; $$.nodeList.push_back($3.node); }
    ;

/* ======================================================================
   DECLARATORS
   ====================================================================== */
pointer
    : '*'         { $$.decl.pointerLevel = 1; }
    | '&'         { $$.decl.pointerLevel = 1; }
    | pointer '*' { $$ = $1; $$.decl.pointerLevel++; }
    ;

pointer_opt
    : /* empty */ { $$.decl.pointerLevel = 0; }
    | pointer     { $$ = $1; }
    ;

declarator
    : pointer direct_declarator {
          $$ = $2;
          $$.decl.pointerLevel += $1.decl.pointerLevel;
      }
    | direct_declarator { $$ = $1; }
    ;

direct_declarator
    : IDENTIFIER {
          $$.decl.name = $1.str;
          $$.decl.nameIdx = $1.idx;
      }
    | IDENTIFIER SCOPE_RES IDENTIFIER {
          const Symbol *s = lookupSymbol($1.str);
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
          const Symbol *s = lookupSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.decl.name = $3.str;
          $$.decl.nameIdx = $3.idx;
          $$.decl.className = $1.str;
      }
    | '(' declarator ')' { $$ = $2; $$.decl.wasParenGrouped = true; }
    | direct_declarator '(' { pushScope(); } parameter_list_opt ')' {
          $$ = $1;
          if ($1.decl.wasParenGrouped && $1.decl.pointerLevel > 0) {
              /* `int (*fp)(int, int)` -- fp is a VARIABLE of function-
                 pointer type, not a function declaration. */
              $$.decl.isFunctionPointer = true;
          } else {
              $$.decl.isFunction = true;
          }
          $$.decl.wasParenGrouped = false; /* consumed */
          $$.decl.params = $4.paramList;
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
    | direct_declarator '[' ']' { $$ = $1; $$.decl.arrayLevel++; }
    | direct_declarator '[' assignment_expr ']' { $$ = $1; $$.decl.arrayLevel++; }
    ;

parameter_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | parameter_list { $$ = $1; }
    ;

parameter_list
    : parameter_decl { if ($1.decl.nameIdx >= 0 || !$1.decl.typeStr.empty()) $$.paramList.push_back($1.decl); }
    | parameter_list ',' parameter_decl {
          $$ = $1;
          $$.paramList.push_back($3.decl);
      }
    | parameter_list ',' ELLIPSIS { $$ = $1; }
    ;

parameter_decl
    : declaration_specifiers declarator {
          $$.decl = $2.decl;
          $$.decl.typeStr = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, $2.decl.arrayLevel);
      }
    | declaration_specifiers {
          $$.decl.typeStr = computeTypeStr($1.typeSpec, 0, 0);
      }
    ;

/* ======================================================================
   FUNCTION DEFINITIONS
   ====================================================================== */
function_definition
    : declaration_specifiers declarator {
          bool outOfClass = !$2.decl.className.empty();
          if (outOfClass) enterClass($2.decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : $2.decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle($2.decl.name, paramTypes, currentClassName());
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
          if (outOfClass) leaveClass();
          pushScope();
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
          if (outOfClass) enterClass($2.decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : $2.decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle($2.decl.name, paramTypes, currentClassName());
          if (outOfClass) leaveClass();
          auto node = mkNode(ASTKind::FunctionDef, $2.decl.name + " : " + mangled);
          for (auto &p : $2.decl.params) {
              if (!p.name.empty()) addChild(node, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
          }
          auto body = mkNode(ASTKind::CompoundStmt);
          for (auto &s : $5.nodeList) addChild(body, s);
          addChild(node, body);
          $$.node = node;
      }
    ;

/* ======================================================================
   STATEMENTS
   ====================================================================== */
statement
    : compound_stmt { $$.node = $1.node; }
    | expr_stmt { $$.node = $1.node; }
    | selection_stmt { $$.node = $1.node; }
    | iteration_stmt { $$.node = $1.node; }
    | jump_stmt { $$.node = $1.node; }
    | labeled_stmt { $$.node = $1.node; }
    | declaration { $$.node = $1.node; }
    | error ';' { yyerrok; }
    ;

compound_stmt
    : '{' { pushScope(); } block_item_list_opt '}' {
          popScope();
          auto n = mkNode(ASTKind::CompoundStmt);
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
    : ';' { $$.node = mkNode(ASTKind::EmptyStmt); }
    | expr ';' { $$.node = mkNode(ASTKind::ExprStmt, "", {$1.node}); }
    ;

selection_stmt
    : IF '(' expr ')' statement %prec IFX {
          $$.node = mkNode(ASTKind::IfStmt, "", {$3.node, $5.node});
      }
    | IF '(' expr ')' statement ELSE statement {
          $$.node = mkNode(ASTKind::IfStmt, "", {$3.node, $5.node, $7.node});
      }
    | SWITCH '(' expr ')' compound_stmt {
          $$.node = mkNode(ASTKind::SwitchStmt, "", {$3.node, $5.node});
      }
    ;

labeled_stmt
    : CASE constant_expr ':' statement {
          $$.node = mkNode(ASTKind::CaseStmt, "", {$2.node, $4.node});
      }
    | DEFAULT ':' statement {
          $$.node = mkNode(ASTKind::DefaultStmt, "", {$3.node});
      }
    | IDENTIFIER ':' statement {
          declareSymbol($1.str, SymKind::LABEL, "LABEL", SymbolDeclInfo{$1.idx});
          setCategory($1.idx, "LABEL");
          $$.node = mkNode(ASTKind::LabeledStmt, $1.str, {$3.node});
      }
    ;

iteration_stmt
    : WHILE '(' expr ')' statement {
          $$.node = mkNode(ASTKind::WhileStmt, "", {$3.node, $5.node});
      }
    | DO statement WHILE '(' expr ')' ';' {
          $$.node = mkNode(ASTKind::DoWhileStmt, "", {$2.node, $5.node});
      }
    | UNTIL '(' expr ')' statement {
          $$.node = mkNode(ASTKind::UntilStmt, "", {$3.node, $5.node});
      }
    | FOR '(' expr_stmt expr_stmt for_incr_opt ')' statement {
          $$.node = mkNode(ASTKind::ForStmt, "", {$3.node, $4.node, $5.node, $7.node});
      }
    | FOR '(' { pushScope(); } declaration expr_stmt for_incr_opt ')' statement {
          popScope();
          $$.node = mkNode(ASTKind::ForStmt, "", {$4.node, $5.node, $6.node, $8.node});
      }
    ;

for_incr_opt
    : /* empty */ { $$ = ParserValue(); }
    | expr { $$.node = $1.node; }
    ;

jump_stmt
    : BREAK ';' { $$.node = mkNode(ASTKind::BreakStmt); }
    | CONTINUE ';' { $$.node = mkNode(ASTKind::ContinueStmt); }
    | RETURN ';' { $$.node = mkNode(ASTKind::ReturnStmt); }
    | RETURN expr ';' { $$.node = mkNode(ASTKind::ReturnStmt, "", {$2.node}); }
    | GOTO IDENTIFIER ';' {
          const Symbol *s = lookupSymbol($2.str);
          if (s) setCategory($2.idx, "LABEL");
          recordUsage($2.str);
          $$.node = mkNode(ASTKind::GotoStmt, $2.str);
      }
    ;

/* ======================================================================
   EXPRESSIONS
   ---------------------------------------------------------------------
   A flat, ambiguous-looking binary_expr grammar disambiguated purely by
   the %left/%right precedence table above -- the same well-known trick
   the reference K&R yacc grammar for C uses to avoid writing a dozen
   separate precedence-layer nonterminals.
   ====================================================================== */
expr
    : assignment_expr { $$.node = $1.node; }
    | expr ',' assignment_expr { $$.node = mkNode(ASTKind::CommaExpr, "", {$1.node, $3.node}); }
    ;

assignment_expr
    : binary_expr { $$.node = $1.node; }
    | unary_expr assign_op assignment_expr {
          $$.node = mkNode(ASTKind::AssignExpr, $2.str, {$1.node, $3.node});
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
    : binary_expr OR_OP binary_expr  { $$.node = mkNode(ASTKind::BinaryExpr, "||", {$1.node, $3.node}); }
    | binary_expr AND_OP binary_expr { $$.node = mkNode(ASTKind::BinaryExpr, "&&", {$1.node, $3.node}); }
    | binary_expr '|' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "|", {$1.node, $3.node}); }
    | binary_expr '^' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "^", {$1.node, $3.node}); }
    | binary_expr '&' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "&", {$1.node, $3.node}); }
    | binary_expr EQ_OP binary_expr  { $$.node = mkNode(ASTKind::BinaryExpr, "==", {$1.node, $3.node}); }
    | binary_expr NE_OP binary_expr  { $$.node = mkNode(ASTKind::BinaryExpr, "!=", {$1.node, $3.node}); }
    | binary_expr '<' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "<", {$1.node, $3.node}); }
    | binary_expr '>' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, ">", {$1.node, $3.node}); }
    | binary_expr LE_OP binary_expr  { $$.node = mkNode(ASTKind::BinaryExpr, "<=", {$1.node, $3.node}); }
    | binary_expr GE_OP binary_expr  { $$.node = mkNode(ASTKind::BinaryExpr, ">=", {$1.node, $3.node}); }
    | binary_expr SHL binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "<<", {$1.node, $3.node}); }
    | binary_expr SHR binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, ">>", {$1.node, $3.node}); }
    | binary_expr '+' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "+", {$1.node, $3.node}); }
    | binary_expr '-' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "-", {$1.node, $3.node}); }
    | binary_expr '*' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "*", {$1.node, $3.node}); }
    | binary_expr '/' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "/", {$1.node, $3.node}); }
    | binary_expr '%' binary_expr    { $$.node = mkNode(ASTKind::BinaryExpr, "%", {$1.node, $3.node}); }
    | binary_expr '?' expr ':' binary_expr {
          $$.node = mkNode(ASTKind::TernaryExpr, "", {$1.node, $3.node, $5.node});
      }
    | unary_expr { $$.node = $1.node; }
    ;

unary_expr
    : postfix_expr { $$.node = $1.node; }
    | INC unary_expr { $$.node = mkNode(ASTKind::UnaryExpr, "++(pre)", {$2.node}); }
    | DEC unary_expr { $$.node = mkNode(ASTKind::UnaryExpr, "--(pre)", {$2.node}); }
    | '&' unary_expr %prec ADDR  { $$.node = mkNode(ASTKind::UnaryExpr, "&", {$2.node}); }
    | '*' unary_expr %prec DEREF { $$.node = mkNode(ASTKind::UnaryExpr, "*", {$2.node}); }
    | '+' unary_expr %prec UMINUS { $$.node = mkNode(ASTKind::UnaryExpr, "+", {$2.node}); }
    | '-' unary_expr %prec UMINUS { $$.node = mkNode(ASTKind::UnaryExpr, "-", {$2.node}); }
    | '!' unary_expr { $$.node = mkNode(ASTKind::UnaryExpr, "!", {$2.node}); }
    | '~' unary_expr { $$.node = mkNode(ASTKind::UnaryExpr, "~", {$2.node}); }
    | '(' type_name ')' unary_expr %prec CAST {
          $$.node = mkNode(ASTKind::CastExpr, $2.str, {$4.node});
      }
    | SIZEOF unary_expr %prec CAST { $$.node = mkNode(ASTKind::SizeofExpr, "", {$2.node}); }
    | SIZEOF '(' type_name ')' { $$.node = mkNode(ASTKind::SizeofExpr, $3.str); }
    | NEW type_name { $$.node = mkNode(ASTKind::NewExpr, $2.str); }
    | DELETE unary_expr { $$.node = mkNode(ASTKind::DeleteExpr, "", {$2.node}); }
    ;

type_name
    : type_name_specifiers pointer_opt {
          $$.str = computeTypeStr($1.typeSpec, $2.decl.pointerLevel, 0);
      }
    ;

type_name_specifiers
    : type_name_specifiers type_name_specifier {
          $$ = $1;
          for (auto &p : $2.typeSpec.parts) $$.typeSpec.parts.push_back(p);
      }
    | type_name_specifier { $$ = $1; }
    ;

/* Restricted specifier set for cast/sizeof/new type-names: primitives,
   qualifiers, typedef names, and *references* to an existing struct/
   union/class/enum tag -- deliberately NOT the body-declaring forms
   ("struct S { ... }"), which would otherwise make a type-name able to
   swallow an entire class body and collide with statement parsing. */
type_name_specifier
    : INT      { $$.typeSpec.parts.push_back("INT"); }
    | CHAR     { $$.typeSpec.parts.push_back("CHAR"); }
    | FLOAT    { $$.typeSpec.parts.push_back("FLOAT"); }
    | DOUBLE   { $$.typeSpec.parts.push_back("DOUBLE"); }
    | VOID     { $$.typeSpec.parts.push_back("VOID"); }
    | BOOL     { $$.typeSpec.parts.push_back("BOOL"); }
    | SHORT    { $$.typeSpec.parts.push_back("SHORT"); }
    | LONG     { $$.typeSpec.parts.push_back("LONG"); }
    | SIGNED   { $$.typeSpec.parts.push_back("SIGNED"); }
    | UNSIGNED { $$.typeSpec.parts.push_back("UNSIGNED"); }
    | FILE_KW  { $$.typeSpec.parts.push_back("FILE"); }
    | CONST    { $$ = ParserValue(); }
    | VOLATILE { $$ = ParserValue(); }
    | TYPE_NAME {
          const Symbol *s = lookupSymbol($1.str);
          setCategory($1.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back(s ? s->typeStr : "INT");
      }
    | STRUCT IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "STRUCT");
          $$.typeSpec.parts.push_back("STRUCT");
      }
    | STRUCT TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("STRUCT");
      }
    | UNION IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "UNION");
          $$.typeSpec.parts.push_back("UNION");
      }
    | UNION TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("UNION");
      }
    | CLASS IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "CLASS");
          $$.typeSpec.parts.push_back("CLASS");
      }
    | CLASS TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("CLASS");
      }
    | ENUM IDENTIFIER {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, s ? s->typeStr : "ENUM");
          $$.typeSpec.parts.push_back("ENUM");
      }
    | ENUM TYPE_NAME {
          const Symbol *s = lookupSymbol($2.str);
          setCategory($2.idx, categoryForTypeName(s));
          $$.typeSpec.parts.push_back("ENUM");
      }
    ;

postfix_expr
    : primary_expr { $$.node = $1.node; }
    | postfix_expr '[' expr ']' { $$.node = mkNode(ASTKind::IndexExpr, "", {$1.node, $3.node}); }
    | postfix_expr '(' argument_list_opt ')' {
          auto n = mkNode(ASTKind::CallExpr, "", {$1.node});
          for (auto &a : $3.nodeList) addChild(n, a);
          $$.node = n;
      }
    | postfix_expr '.' IDENTIFIER { $$.node = mkNode(ASTKind::MemberExpr, $3.str, {$1.node}); }
    | postfix_expr ARROW IDENTIFIER { $$.node = mkNode(ASTKind::ArrowExpr, $3.str, {$1.node}); }
    | postfix_expr SCOPE_RES IDENTIFIER { $$.node = mkNode(ASTKind::ScopeExpr, $3.str, {$1.node}); }
    | postfix_expr INC { $$.node = mkNode(ASTKind::PostfixOpExpr, "++", {$1.node}); }
    | postfix_expr DEC { $$.node = mkNode(ASTKind::PostfixOpExpr, "--", {$1.node}); }
    | builtin_call { $$.node = $1.node; }
    ;

builtin_call
    : PRINTF '(' argument_list_opt ')'  { auto n = mkNode(ASTKind::BuiltinCallExpr, "printf");  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | SCANF '(' argument_list_opt ')'   { auto n = mkNode(ASTKind::BuiltinCallExpr, "scanf");   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | MALLOC '(' argument_list_opt ')'  { auto n = mkNode(ASTKind::BuiltinCallExpr, "malloc");  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FREE '(' argument_list_opt ')'    { auto n = mkNode(ASTKind::BuiltinCallExpr, "free");    for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | CALLOC '(' argument_list_opt ')'  { auto n = mkNode(ASTKind::BuiltinCallExpr, "calloc");  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | REALLOC '(' argument_list_opt ')' { auto n = mkNode(ASTKind::BuiltinCallExpr, "realloc"); for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FOPEN '(' argument_list_opt ')'   { auto n = mkNode(ASTKind::BuiltinCallExpr, "fopen");   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FCLOSE '(' argument_list_opt ')'  { auto n = mkNode(ASTKind::BuiltinCallExpr, "fclose");  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FREAD '(' argument_list_opt ')'   { auto n = mkNode(ASTKind::BuiltinCallExpr, "fread");   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FWRITE '(' argument_list_opt ')'  { auto n = mkNode(ASTKind::BuiltinCallExpr, "fwrite");  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FPRINTF '(' argument_list_opt ')' { auto n = mkNode(ASTKind::BuiltinCallExpr, "fprintf"); for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FSCANF '(' argument_list_opt ')'  { auto n = mkNode(ASTKind::BuiltinCallExpr, "fscanf");  for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FGETS '(' argument_list_opt ')'   { auto n = mkNode(ASTKind::BuiltinCallExpr, "fgets");   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FPUTS '(' argument_list_opt ')'   { auto n = mkNode(ASTKind::BuiltinCallExpr, "fputs");   for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
    | FEOF '(' argument_list_opt ')'    { auto n = mkNode(ASTKind::BuiltinCallExpr, "feof");    for (auto &a : $3.nodeList) addChild(n, a); $$.node = n; }
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
    | type_name { $$.node = mkNode(ASTKind::TypeNameNode, $1.str); }
    ;

primary_expr
    : IDENTIFIER {
          const Symbol *s = lookupSymbol($1.str);
          if (s) setCategory($1.idx, s->typeStr);
          recordUsage($1.str);
          $$.node = mkNode(ASTKind::Identifier, $1.str);
      }
    | INT_LITERAL    { $$.node = mkNode(ASTKind::IntLiteral, $1.str); }
    | FLOAT_LITERAL  { $$.node = mkNode(ASTKind::FloatLiteral, $1.str); }
    | CHAR_LITERAL   { $$.node = mkNode(ASTKind::CharLiteral, $1.str); }
    | STRING_LITERAL { $$.node = mkNode(ASTKind::StringLiteral, $1.str); }
    | BOOL_LITERAL { $$.node = mkNode(ASTKind::BoolLiteral, $1.str); }
    | THIS { $$.node = mkNode(ASTKind::ThisExpr); }
    | '(' expr ')' { $$.node = $2.node; }
    | lambda_expr { $$.node = $1.node; }
    ;

lambda_expr
    : '[' capture_list_opt ']' '(' { pushScope(); } parameter_list_opt ')' {
          for (auto &p : $6.paramList) {
              if (p.nameIdx >= 0) {
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, SymbolDeclInfo{p.nameIdx});
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      } compound_stmt {
          popScope();
          auto n = mkNode(ASTKind::LambdaExpr, $2.str);
          for (auto &p : $6.paramList) {
              if (!p.name.empty()) addChild(n, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
          }
          addChild(n, $9.node);
          $$.node = n;
      }
    ;

capture_list_opt
    : /* empty */ { $$ = ParserValue(); }
    | capture_list { $$ = $1; }
    ;

capture_list
    : capture { $$.str = $1.str; }
    | capture_list ',' capture { $$.str = $1.str + ", " + $3.str; }
    ;

capture
    : IDENTIFIER { $$.str = $1.str; }
    | '&' IDENTIFIER { $$.str = "&" + $2.str; }
    | '&' { $$.str = "&"; }
    | '=' { $$.str = "="; }
    ;

%%

void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_lastText, s, "Syntax error");
}
