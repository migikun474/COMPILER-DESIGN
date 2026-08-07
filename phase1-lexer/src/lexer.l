/*
 * lexer.l
 * Lexical analyzer for the C-like source language.
 *
 * Covers:
 *  - basic features: all arithmetic/logical operators, if-else, for, while,
 *    do-while, switch-case, int/char arrays, pointers, structures, printf/
 *    scanf (as ordinary identifiers), function calls with arguments, goto,
 *    break, continue, static
 *  - advanced features: variable-argument calls (...), dynamic memory
 *    allocation (malloc/free are identifiers, keyword 'typedef' supported),
 *    command line input (argc/argv are identifiers, no new tokens needed),
 *    reference (&), until loop, multi-level pointers (*), multi-dimensional
 *    arrays ([ ][ ]).
 *
 * Behaviour:
 *  - If the whole input is lexically clean, prints a Lexeme/Token table.
 *  - If any lexical errors are found, prints every error found (with line
 *    number) instead of the table.
 */

%option noyywrap
%option yylineno

%{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <utility>

/* collected results */
static std::vector<std::pair<std::string,std::string>> tokens;   /* lexeme, token */
static std::vector<std::string> lex_errors;                      /* formatted error messages */

static void addToken(const char* tokName, const char* lexeme) {
    tokens.push_back(std::make_pair(std::string(lexeme), std::string(tokName)));
}

static void addError(int line, const std::string& msg) {
    lex_errors.push_back("Line " + std::to_string(line) + ": " + msg);
}

/* buffer used while scanning strings/chars/comments that may run to EOF */
static std::string strbuf;
static int tokStartLine;
%}

DIGIT       [0-9]
LETTER      [a-zA-Z_]
ID          {LETTER}({LETTER}|{DIGIT})*
HEXDIGIT    [0-9a-fA-F]

%x STRSTATE
%x CHRSTATE
%x COMMENTSTATE

%%

"/*"                            { tokStartLine = yylineno; BEGIN(COMMENTSTATE); }
<COMMENTSTATE>"*/"               { BEGIN(INITIAL); }
<COMMENTSTATE>\n                 { /* keep counting via yylineno automatically */ }
<COMMENTSTATE><<EOF>>            {
                                    addError(tokStartLine, "unterminated block comment '/*'");
                                    BEGIN(INITIAL);
                                    yyterminate();
                                  }
<COMMENTSTATE>.                  { /* skip comment body */ }

"//"[^\n]*                       { /* line comment, skip */ }

 /* ---- keywords ---- */
"int"|"char"|"float"|"double"|"void"|"struct"|"typedef"|"static"|"if"|"else"|"for"|"while"|"do"|"until"|"switch"|"case"|"default"|"break"|"continue"|"goto"|"return"   { addToken("keyword", yytext); }

 /* ---- string literals ---- */
\"                                { strbuf = "\""; tokStartLine = yylineno; BEGIN(STRSTATE); }
<STRSTATE>\\.                     { strbuf += yytext; }
<STRSTATE>\"                      { strbuf += "\""; addToken("string_literal", strbuf.c_str()); BEGIN(INITIAL); }
<STRSTATE>\n                      { addError(tokStartLine, "unterminated string literal " + strbuf); BEGIN(INITIAL); yyless(0); }
<STRSTATE><<EOF>>                 { addError(tokStartLine, "unterminated string literal " + strbuf); BEGIN(INITIAL); yyterminate(); }
<STRSTATE>.                       { strbuf += yytext; }

 /* ---- char literals ---- */
'                                  { strbuf = "'"; tokStartLine = yylineno; BEGIN(CHRSTATE); }
<CHRSTATE>\\.                     { strbuf += yytext; }
<CHRSTATE>'                       { strbuf += "'"; addToken("char_constant", strbuf.c_str()); BEGIN(INITIAL); }
<CHRSTATE>\n                      { addError(tokStartLine, "unterminated char literal " + strbuf); BEGIN(INITIAL); yyless(0); }
<CHRSTATE><<EOF>>                 { addError(tokStartLine, "unterminated char literal " + strbuf); BEGIN(INITIAL); yyterminate(); }
<CHRSTATE>.                       { strbuf += yytext; }

 /* ---- numeric constants ---- */
0[xX]{HEXDIGIT}+                                          { addToken("integer_constant", yytext); }
{DIGIT}+\.{DIGIT}+([eE][+-]?{DIGIT}+)?[fF]?               { addToken("float_constant", yytext); }
{DIGIT}+[eE][+-]?{DIGIT}+[fF]?                             { addToken("float_constant", yytext); }
{DIGIT}+                                                   { addToken("integer_constant", yytext); }
{DIGIT}+{LETTER}({LETTER}|{DIGIT})*                        { addError(yylineno, std::string("invalid numeric literal '") + yytext + "'"); }
{DIGIT}+\.{DIGIT}*{LETTER}({LETTER}|{DIGIT})*              { addError(yylineno, std::string("invalid numeric literal '") + yytext + "'"); }

 /* ---- identifiers ---- */
{ID}                              { addToken("identifier", yytext); }

 /* ---- multi-character operators (longest first) ---- */
"..."                              { addToken("ellipsis", yytext); }
"->"                               { addToken("operator", yytext); }
"++"                               { addToken("operator", yytext); }
"--"                               { addToken("operator", yytext); }
"<<="                              { addToken("operator", yytext); }
">>="                              { addToken("operator", yytext); }
"<<"                               { addToken("operator", yytext); }
">>"                               { addToken("operator", yytext); }
"<="                               { addToken("operator", yytext); }
">="                               { addToken("operator", yytext); }
"=="                               { addToken("operator", yytext); }
"!="                               { addToken("operator", yytext); }
"&&"                               { addToken("operator", yytext); }
"||"                               { addToken("operator", yytext); }
"+="                               { addToken("operator", yytext); }
"-="                               { addToken("operator", yytext); }
"*="                               { addToken("operator", yytext); }
"/="                               { addToken("operator", yytext); }
"%="                               { addToken("operator", yytext); }
"&="                               { addToken("operator", yytext); }
"|="                               { addToken("operator", yytext); }
"^="                               { addToken("operator", yytext); }

 /* ---- single-character operators ---- */
[+\-*/%=<>!&|^~.,?:]              { addToken("operator", yytext); }

 /* ---- punctuation ---- */
[(){}\[\];]                       { addToken("punctuation", yytext); }

[ \t\r]+                          { /* skip whitespace */ }
\n                                 { /* newline: yylineno auto-increments */ }

.                                  { addError(yylineno, std::string("illegal character '") + yytext + "'"); }

%%

int main(int argc, char** argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <source-file>\n", argv[0]);
        return 1;
    }
    FILE* f = fopen(argv[1], "r");
    if (!f) {
        fprintf(stderr, "Error: could not open file '%s'\n", argv[1]);
        return 1;
    }
    yyin = f;
    yylex();
    fclose(f);

    if (!lex_errors.empty()) {
        printf("Lexical error(s) found in %s:\n", argv[1]);
        for (auto& e : lex_errors) {
            printf("  %s\n", e.c_str());
        }
        return 1;
    }

    printf("%-30s %-20s\n", "Lexeme", "Token");
    printf("%-30s %-20s\n", "------", "-----");
    for (auto& t : tokens) {
        printf("%-30s %-20s\n", t.first.c_str(), t.second.c_str());
    }
    return 0;
}
