%option noyywrap
%option yylineno
%option nounput
%option noinput

%{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>

#include "common.h"
#include "parser.tab.hpp"
#include "token_type.hpp"
#include "token_converter.hpp"

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

/* Like emit(), but for tokens (strings/char literals) whose full text
   was accumulated into strbuf rather than sitting in yytext. */
static int emitText(int tokcode, const std::string &text, const std::string &category) {
    g_currentLine = yylineno;
    g_lastText = text;
    yylval.str = text;
    yylval.idx = addTokenRecord(text, category);
    return tokcode;
}

/* Looks a matched keyword or operator up in the SHARED tables (see
   shared/include/token_type.hpp) and emits it -- this is what lets
   phase1-lexer and phase2-parser agree on both "is this a keyword"
   and "what do we call it" without either one hand-maintaining its
   own copy of that list. */
static int emitShared(TokenType t) {
    return emit(to_bison_token(t), to_string(t));
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

"/*"                  { litStartLine = yylineno; BEGIN(COMMENTSTATE); }
<COMMENTSTATE>"*/"     { BEGIN(INITIAL); }
<COMMENTSTATE>\n       { }
<COMMENTSTATE><<EOF>>  { reportDiagnostic(litStartLine, "/*", "Unterminated block comment", "Lexical error"); BEGIN(INITIAL); yyterminate(); }
<COMMENTSTATE>.        { }

"//"[^\n]*             { }

 /* identifiers AND keywords share one rule, exactly like phase1-lexer:
    the matched text is looked up in the shared reserved_word() table;
    if it's not a keyword, it's either a previously-seen typedef/class
    name (the lexer hack -- phase1 has no equivalent, since it has no
    parser feeding scope information back) or a plain identifier. */
{ID} {
    auto kw = reserved_word(yytext);
    if (kw.has_value()) {
        return emitShared(kw.value());
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

 /* Every operator -- multi- and single-character alike -- funnels
    through one lookup against the shared operator_map via
    operator_token(), exactly like phase1-lexer's single consolidated
    operator rule. Flex's own longest-match rule already guarantees
    "<<=" wins over "<<" over "<" whenever the longer form is actually
    present, regardless of how many separate patterns are listed here
    or that they all share one action (chained via "|" fall-through);
    listing them longest-first below is for readability only. */
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
    reportDiagnostic(yylineno, yytext, "Illegal character", "Lexical error");
}

[ \t\r]+  { }
\n        { }

.  { reportDiagnostic(yylineno, yytext, "Illegal character", "Lexical error"); }

%%
