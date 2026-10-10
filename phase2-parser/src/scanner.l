%option noyywrap
%option yylineno
%option nounput
%option noinput

%{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

#include "diagnostics/diagnostics.hpp"
#include "parser.tab.hpp"
#include "scanner_support.h"
#include "symbol_table/symbol_table.hpp"
#include "token/token_log.hpp"
#include "token/token_type.hpp"
#include "token_converter.hpp"

static std::string strbuf;
static int litStartLine;
static int litStartCol;
static int g_col = 1;
static int g_tokStartCol = 1;
#define YY_USER_ACTION { g_tokStartCol = g_col; g_col += yyleng; }

static int g_prevToken = 0; /* the previously returned token code */

static int emit(int tokcode, const std::string &defaultCategory) {
    if (tokcode != '*' && tokcode != '&' && tokcode != '(' && tokcode != CONST)
        g_afterTypeKeyword = false;
    if (tokcode == '(' || tokcode == '[' || tokcode == '{' || tokcode == ABSTRACT_LPAREN)
        ++g_bracketDepth;
    else if (tokcode == ')' || tokcode == ']' || tokcode == '}') --g_bracketDepth;
    else if (tokcode == ';' && inDeclaratorListAt(g_bracketDepth)) endDeclaratorList();
    g_prevToken = tokcode;
    g_currentLine = yylineno;
    g_currentColumn = g_tokStartCol;
    g_lastText = yytext;
    yylval.str = yytext;
    yylval.idx = addTokenRecord(yytext, defaultCategory);
    return tokcode;
}

static int emitText(int tokcode, const std::string &text, const std::string &category) {
    g_afterTypeKeyword = false;
    g_prevToken = tokcode;
    g_currentLine = yylineno;
    g_currentColumn = litStartCol; /* the opening quote's column, not the closing one */
    g_lastText = text;
    yylval.str = text;
    yylval.idx = addTokenRecord(text, category);
    return tokcode;
}

static int emitShared(TokenType t) {
    return emit(to_bison_token(t), to_string(t));
}

/* Inside its own body a class/struct name is a type too (`Node
   *next;`), except right before '(' where it names a constructor
   (`Node(int v)`, `~Node()`); everywhere else typedef'd names and
   already-defined tags are TYPE_NAME (the classic lexer hack). */
/* Tokens after which a type before '(' is a declaration specifier /
   declarator name, never the start of a functional cast:
   `Dog::Dog(...)`, `~Dog()`, `struct S (...)`, `unsigned int (x)` */
static bool typePositionAfter(int tok) {
    switch (tok) {
        case SCOPE_RES: case '~': case STRUCT: case CLASS: case OPERATOR:
        case INT: case CHAR: case FLOAT: case DOUBLE: case VOID: case BOOL: case SHORT: case LONG:
        case SIGNED: case UNSIGNED: case TYPE_NAME: case STATIC: case TYPEDEF: case AUTO: case CONST:
        case EXTERN: case VA_LIST:
            return true;
        default:
            return false;
    }
}

static bool isSimpleTypeKeyword(TokenType t) {
    switch (t) {
        case TokenType::INT: case TokenType::CHAR: case TokenType::FLOAT: case TokenType::DOUBLE:
        case TokenType::VOID: case TokenType::BOOL: case TokenType::SHORT: case TokenType::LONG:
        case TokenType::SIGNED: case TokenType::UNSIGNED:
            return true;
        default:
            return false;
    }
}

static int identifierOrKeyword(bool beforeParen) {
    auto kw = reserved_word(yytext);
    /* `T(...)` that can only be an expression -- `Dog(4).bark();`,
       `int(x) + 1;` -- is announced as FCAST, so a statement may start
       with it (LALR(1) alone would have to guess at the '(') */
    bool typeHere = kw.has_value() ? isSimpleTypeKeyword(kw.value())
                                   : (isTypeName(yytext) && !g_afterTypeKeyword);
    if (beforeParen && typeHere && !typePositionAfter(g_prevToken) &&
        parenGroupIsExpression(yylineno, g_col)) {
        return emit(FCAST, kw.has_value() ? to_string(kw.value()) : "TYPEDEF");
    }
    if (kw.has_value()) {
        return emitShared(kw.value());
    }
    if (isTypeName(yytext) && !g_afterTypeKeyword &&
        !(g_prevToken == ',' && inDeclaratorListAt(g_bracketDepth))) {
        return emit(TYPE_NAME, "TYPEDEF");
    }
    if (!beforeParen && !currentClassName().empty() && currentClassName() == yytext) {
        return emit(TYPE_NAME, "TYPEDEF");
    }
    return emit(IDENTIFIER, "IDENTIFIER");
}
%}

DIGIT       [0-9]
LETTER      [a-zA-Z_]
ID          {LETTER}({LETTER}|{DIGIT})*
HEXDIGIT    [0-9a-fA-F]
LSUF        (l|L)
LLSUF       (ll|LL)
USUF        (u|U)
INT_SUFFIX  ({USUF}({LLSUF}|{LSUF})?|({LLSUF}|{LSUF}){USUF}?)
FRAC        ({DIGIT}+\.{DIGIT}*|\.{DIGIT}+)

%x STRSTATE
%x CHRSTATE
%x COMMENTSTATE

%%

"/*"                  { litStartLine = yylineno; litStartCol = g_tokStartCol; BEGIN(COMMENTSTATE); }
<COMMENTSTATE>"*/"     { BEGIN(INITIAL); }
<COMMENTSTATE>\n       { g_col = 1; }
<COMMENTSTATE><<EOF>>  { reportDiagnostic(litStartLine, litStartCol, "/*", "Unterminated block comment", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<COMMENTSTATE>.        { }

"//"[^\n]*             { }

{ID}/[ \t]*"(" { return identifierOrKeyword(/*beforeParen=*/true); }
{ID}             { return identifierOrKeyword(/*beforeParen=*/false); }

\"                     { strbuf = "\""; litStartLine = yylineno; litStartCol = g_tokStartCol; BEGIN(STRSTATE); }
<STRSTATE>\\.          { strbuf += yytext; }
<STRSTATE>\"           { strbuf += "\""; BEGIN(INITIAL); return emitText(STRING_LITERAL, strbuf, "STRING_LITERAL"); }
<STRSTATE>\n           { reportDiagnostic(litStartLine, litStartCol, strbuf, "Unterminated string literal", "Lexical error"); BEGIN(INITIAL); yyless(0); }
<STRSTATE><<EOF>>      { reportDiagnostic(litStartLine, litStartCol, strbuf, "Unterminated string literal", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<STRSTATE>.            { strbuf += yytext; }

'                      { strbuf = "'"; litStartLine = yylineno; litStartCol = g_tokStartCol; BEGIN(CHRSTATE); }
<CHRSTATE>\\.          { strbuf += yytext; }
<CHRSTATE>'            { strbuf += "'"; BEGIN(INITIAL); return emitText(CHAR_LITERAL, strbuf, "CHAR_LITERAL"); }
<CHRSTATE>\n           { reportDiagnostic(litStartLine, litStartCol, strbuf, "Unterminated character literal", "Lexical error"); BEGIN(INITIAL); yyless(0); }
<CHRSTATE><<EOF>>      { reportDiagnostic(litStartLine, litStartCol, strbuf, "Unterminated character literal", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<CHRSTATE>.            { strbuf += yytext; }

0[xX]{HEXDIGIT}+{INT_SUFFIX}?          { return emit(INT_LITERAL, "INT_LITERAL"); }
0[bB][01]+{INT_SUFFIX}?                { return emit(INT_LITERAL, "INT_LITERAL"); }
0[0-7]+{INT_SUFFIX}?                   { return emit(INT_LITERAL, "INT_LITERAL"); }
{FRAC}([eE][+-]?{DIGIT}+)?[fF]?        { return emit(FLOAT_LITERAL, "FLOAT_LITERAL"); }
{DIGIT}+[eE][+-]?{DIGIT}+[fF]?         { return emit(FLOAT_LITERAL, "FLOAT_LITERAL"); }
{DIGIT}+{INT_SUFFIX}?                  { return emit(INT_LITERAL, "INT_LITERAL"); }

"(" {
    /* `(*)` / `(&)` right after a type: a nameless declarator, as in
       `sizeof(int (*)[3])`, never the argument list of `int(...)` */
    if ((typePositionAfter(g_prevToken) || g_prevToken == '*' || g_prevToken == '&') && abstractDeclaratorGroup(yylineno, g_col)) {
        return emit(ABSTRACT_LPAREN, to_string(operator_token("(").value()));
    }
    return emitShared(operator_token("(").value());
}

"..."   |
"::"    |
"->"    |
"++"    |
"--"    |
"<<="   |
">>="   |
"<<"    |
">>"    |
"<="    |
">="    |
"=="    |
"!="    |
"&&"    |
"||"    |
"+="    |
"-="    |
"*="    |
"/="    |
"%="    |
"&="    |
"|="    |
"^="    |
[+\-*/%=<>!&|^~.,?:(){}\[\]\;] {
    auto op = operator_token(yytext);
    if (op.has_value()) {
        return emitShared(op.value());
    }
    reportDiagnostic(yylineno, g_tokStartCol, yytext, "Illegal character", "Lexical error");
}

[ \t\r]+  { }
\n        { g_col = 1; }

.  { reportDiagnostic(yylineno, g_tokStartCol, yytext, "Illegal character", "Lexical error"); }

%%
