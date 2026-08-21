%option noyywrap
%option yylineno
%option nounput
%option noinput

%{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <unordered_map>

#include "common.h"
#include "parser.tab.hpp"

static std::string strbuf;
static int litStartLine;

/* Record + classify a token in one step, keep the scanner-side globals
   (used by yyerror for accurate positions) in sync, and hand the
   lexeme/index pair to the parser via yylval. */
static int emit(int tokcode, const std::string &defaultCategory) {
    g_currentLine = yylineno;
    g_lastText = yytext;
    yylval.str = yytext;
    yylval.idx = addTokenRecord(yytext, defaultCategory);
    return tokcode;
}

/* Punctuation/operator tokens are logged too (so they still show up in
   the final token table) but never get their category patched later. */
static int emitOp(int tokcode, const std::string &name) {
    return emit(tokcode, name);
}

/* Like emit(), but for tokens (strings/char literals) whose full text
   was accumulated into strbuf rather than sitting in yytext. */
static int emitText(int tokcode, const std::string &text, const std::string &category) {
    g_currentLine = yylineno;
    g_lastText = text;
    yylval.str = text;
    yylval.idx = addTokenRecord(text, category);
    return tokcode;
}

static const std::unordered_map<std::string, int> keyword_map = {
    {"int", INT}, {"char", CHAR}, {"float", FLOAT}, {"double", DOUBLE},
    {"void", VOID}, {"short", SHORT}, {"long", LONG}, {"signed", SIGNED},
    {"unsigned", UNSIGNED},
    {"struct", STRUCT}, {"enum", ENUM}, {"union", UNION}, {"class", CLASS},
    {"public", PUBLIC}, {"private", PRIVATE}, {"protected", PROTECTED},
    {"this", THIS},
    {"static", STATIC}, {"typedef", TYPEDEF}, {"auto", AUTO},
    {"if", IF}, {"else", ELSE}, {"for", FOR}, {"while", WHILE}, {"do", DO},
    {"until", UNTIL}, {"switch", SWITCH}, {"case", CASE}, {"default", DEFAULT},
    {"break", BREAK}, {"continue", CONTINUE}, {"goto", GOTO}, {"return", RETURN},
    {"printf", PRINTF}, {"scanf", SCANF},
    {"malloc", MALLOC}, {"free", FREE}, {"calloc", CALLOC}, {"realloc", REALLOC},
    {"FILE", FILE_KW}, {"fopen", FOPEN}, {"fclose", FCLOSE}, {"fread", FREAD},
    {"fwrite", FWRITE}, {"fprintf", FPRINTF}, {"fscanf", FSCANF},
    {"fgets", FGETS}, {"fputs", FPUTS}, {"feof", FEOF},
    {"true", TRUE_TOK}, {"false", FALSE_TOK},
    {"bool", BOOL}, {"const", CONST}, {"volatile", VOLATILE},
    {"sizeof", SIZEOF}, {"new", NEW}, {"delete", DELETE},
};
static const std::unordered_map<std::string, std::string> single_char_names = {
    {"+", "plus_op"}, {"-", "minus_op"}, {"*", "star_op"}, {"/", "divide_op"},
    {"%", "mod_op"}, {"=", "assign_op"}, {"<", "lt_op"}, {">", "gt_op"},
    {"!", "logical_not_op"}, {"&", "ampersand_op"}, {"|", "pipe_op"},
    {"^", "caret_op"}, {"~", "tilde_op"}, {".", "dot_op"}, {",", "comma_op"},
    {"?", "question_op"}, {":", "colon_op"},
    {"(", "open_paren_op"}, {")", "close_paren_op"},
    {"{", "open_brace_op"}, {"}", "close_brace_op"},
    {"[", "open_bracket_op"}, {"]", "close_bracket_op"},
    {";", "semicolon_op"},
};
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

"/*"                  { litStartLine = yylineno; BEGIN(COMMENTSTATE); }
<COMMENTSTATE>"*/"     { BEGIN(INITIAL); }
<COMMENTSTATE>\n       { }
<COMMENTSTATE><<EOF>>  { reportDiagnostic(litStartLine, "/*", "Unterminated block comment", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<COMMENTSTATE>.        { }

"//"[^\n]*             { }

{ID} {
    auto it = keyword_map.find(yytext);
    if (it != keyword_map.end()) {
        return emit(it->second, yytext);
    }
    if (g_typedefNames.count(yytext)) {
        return emit(TYPE_NAME, "TYPEDEF");
    }
    return emit(IDENTIFIER, "IDENTIFIER");
}

\"                     { strbuf = "\""; litStartLine = yylineno; BEGIN(STRSTATE); }
<STRSTATE>\\.          { strbuf += yytext; }
<STRSTATE>\"           { strbuf += "\""; BEGIN(INITIAL); return emitText(STRING_LITERAL, strbuf, "STRING_LITERAL"); }
<STRSTATE>\n           { reportDiagnostic(litStartLine, strbuf, "Unterminated string literal", "Lexical error"); BEGIN(INITIAL); yyless(0); }
<STRSTATE><<EOF>>      { reportDiagnostic(litStartLine, strbuf, "Unterminated string literal", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<STRSTATE>.            { strbuf += yytext; }

'                      { strbuf = "'"; litStartLine = yylineno; BEGIN(CHRSTATE); }
<CHRSTATE>\\.          { strbuf += yytext; }
<CHRSTATE>'            { strbuf += "'"; BEGIN(INITIAL); return emitText(CHAR_LITERAL, strbuf, "CHAR_LITERAL"); }
<CHRSTATE>\n           { reportDiagnostic(litStartLine, strbuf, "Unterminated character literal", "Lexical error"); BEGIN(INITIAL); yyless(0); }
<CHRSTATE><<EOF>>      { reportDiagnostic(litStartLine, strbuf, "Unterminated character literal", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<CHRSTATE>.            { strbuf += yytext; }

0[xX]{HEXDIGIT}+{INT_SUFFIX}?          { return emit(INT_LITERAL, "INT_LITERAL"); }
0[bB][01]+{INT_SUFFIX}?                { return emit(INT_LITERAL, "INT_LITERAL"); }
0[0-7]+{INT_SUFFIX}?                   { return emit(INT_LITERAL, "INT_LITERAL"); }
{FRAC}([eE][+-]?{DIGIT}+)?[fF]?        { return emit(FLOAT_LITERAL, "FLOAT_LITERAL"); }
{DIGIT}+[eE][+-]?{DIGIT}+[fF]?         { return emit(FLOAT_LITERAL, "FLOAT_LITERAL"); }
{DIGIT}+{INT_SUFFIX}?                  { return emit(INT_LITERAL, "INT_LITERAL"); }

"..."   { return emitOp(ELLIPSIS, "ellipsis_op"); }
"::"    { return emitOp(SCOPE_RES, "scope_resolution_op"); }
"->"    { return emitOp(ARROW, "arrow_op"); }
"++"    { return emitOp(INC, "increment_op"); }
"--"    { return emitOp(DEC, "decrement_op"); }
"<<="   { return emitOp(SHL_ASSIGN, "lshift_assign_op"); }
">>="   { return emitOp(SHR_ASSIGN, "rshift_assign_op"); }
"<<"    { return emitOp(SHL, "lshift_op"); }
">>"    { return emitOp(SHR, "rshift_op"); }
"<="    { return emitOp(LE_OP, "le_op"); }
">="    { return emitOp(GE_OP, "ge_op"); }
"=="    { return emitOp(EQ_OP, "eq_op"); }
"!="    { return emitOp(NE_OP, "ne_op"); }
"&&"    { return emitOp(AND_OP, "logical_and_op"); }
"||"    { return emitOp(OR_OP, "logical_or_op"); }
"+="    { return emitOp(PLUS_ASSIGN, "plus_assign_op"); }
"-="    { return emitOp(MINUS_ASSIGN, "minus_assign_op"); }
"*="    { return emitOp(MUL_ASSIGN, "star_assign_op"); }
"/="    { return emitOp(DIV_ASSIGN, "divide_assign_op"); }
"%="    { return emitOp(MOD_ASSIGN, "mod_assign_op"); }
"&="    { return emitOp(AND_ASSIGN, "ampersand_assign_op"); }
"|="    { return emitOp(OR_ASSIGN, "pipe_assign_op"); }
"^="    { return emitOp(XOR_ASSIGN, "caret_assign_op"); }

[+\-*/%=<>!&|^~.,?:(){}\[\]\;] {
    auto it = single_char_names.find(yytext);
    std::string name = (it != single_char_names.end()) ? it->second : std::string(yytext);
    return emitOp((unsigned char)yytext[0], name);
}

[ \t\r]+  { }
\n        { }

.  { reportDiagnostic(yylineno, yytext, "Illegal character", "Lexical error"); }

%%
