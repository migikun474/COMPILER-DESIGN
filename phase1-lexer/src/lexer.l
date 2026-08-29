%option noyywrap
%option yylineno
%option nounput
%option noinput

%{
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <utility>

#include "diagnostics.h"
#include "logger.h"
#include "token.h"
#include "token_type.hpp"

/* buffer used while scanning strings/chars/comments that may run to EOF */
static std::string strbuf;
static int tokStartLine;
static bool litHadError;
static int chrCharCount;   /* how many actual characters seen in the
                               current char literal (an escape counts
                               as ONE character, e.g. '\n' has 1) */

static const char* SIMPLE_ESCAPES = "ntr\\'\"abfv?";

static void invalidEscape(const char* text, int line) {
    reportError(line, text, "Invalid escape sequence");
    litHadError = true;
}
%}

DIGIT       [0-9]
LETTER      [a-zA-Z_]
ID          {LETTER}({LETTER}|{DIGIT})*
HEXDIGIT    [0-9a-fA-F]
OCTDIGIT    [0-7]
BINDIGIT    [01]

 /* integer suffixes: u/U (unsigned), l/L (long), ll/LL (long long),
    in either order, matching the real-C grammar -- ll/LL must be the
    SAME case (lL / Ll are not valid; see the design-decision note in
    the numeric-constants rules below for what happens to those now) */
LSUF        (l|L)
LLSUF       (ll|LL)
USUF        (u|U)
INT_SUFFIX  ({USUF}({LLSUF}|{LSUF})?|({LLSUF}|{LSUF}){USUF}?)

 /* fractional part of a float: digits on EITHER side of the dot are
    optional, but not both -- covers 5.5, 5., and .5. A lone "." (no
    digit on either side) matches neither alternative and correctly
    falls through to the "." operator rule further down. */
FRAC        ({DIGIT}+\.{DIGIT}*|\.{DIGIT}+)

%x STRSTATE
%x CHRSTATE
%x COMMENTSTATE

%%

"/*"                            { tokStartLine = yylineno; BEGIN(COMMENTSTATE); }
<COMMENTSTATE>"*/"               { BEGIN(INITIAL); }
<COMMENTSTATE>\n                 { /* keep counting via yylineno automatically */ }
<COMMENTSTATE><<EOF>>            {
                                    reportError( tokStartLine,  "/*",  "Unterminated block comment");
                                    BEGIN(INITIAL);
                                    yyterminate();
                                  }
<COMMENTSTATE>.                  { /* skip comment body */ }

"//"[^\n]*                       { /* line comment, skip */ }

 /* ---- identifiers AND keywords share one rule: the matched text is
    looked up in reserved_word() (keyword_map in token_type.cpp); if
    found, that keyword's specific TokenType is used, otherwise it's a
    plain IDENTIFIER. See the file header for why this replaces the
    old per-category flex-alternation rules. ---- */
{ID}                              {
                                       auto kw = reserved_word(yytext);
                                       if (kw.has_value()) {
                                           addToken(kw.value(), yytext);
                                       } else {
                                           addToken(TokenType::IDENTIFIER, yytext);
                                       }
                                   }

 /* ---- string literals ---- */
\"                                { strbuf = "\""; tokStartLine = yylineno; litHadError = false; BEGIN(STRSTATE); }

 /* ---- char literals ---- */
'                                  { strbuf = "'"; tokStartLine = yylineno; litHadError = false; chrCharCount = 0; BEGIN(CHRSTATE); }

 /* ---- escape sequences: rules shared by strings and char literals.
    Ordered most-specific first so maximal munch does the right thing:
    a well-formed "\x41" or "\101" is consumed whole by the valid rules
    below; a malformed "\xz" or "\89" falls through to the 2-char
    "\x"/"\8"/"\9" rules instead, which flag it precisely. ---- */
<STRSTATE,CHRSTATE>\\[0-7]{1,3}     { strbuf += yytext; chrCharCount++; }
<STRSTATE,CHRSTATE>\\x{HEXDIGIT}+   { strbuf += yytext; chrCharCount++; }
<STRSTATE,CHRSTATE>\\x              { invalidEscape(yytext, yylineno); strbuf += yytext; chrCharCount++; }
<STRSTATE,CHRSTATE>\\[89]           { invalidEscape(yytext, yylineno); strbuf += yytext; chrCharCount++; }
<STRSTATE,CHRSTATE>\\.              {
                                        if (strchr(SIMPLE_ESCAPES, yytext[1]) == nullptr) invalidEscape(yytext, yylineno);
                                        strbuf += yytext;
                                        chrCharCount++;
                                     }

<STRSTATE>\"                      { strbuf += "\""; if (!litHadError) addToken(TokenType::STRING_LITERAL, strbuf); BEGIN(INITIAL); }
<STRSTATE>\n                      {reportError(  tokStartLine,  strbuf, "Unterminated string literal"); BEGIN(INITIAL); yyless(0); }
<STRSTATE><<EOF>>                 {reportError(  tokStartLine,  strbuf, "Unterminated string literal"); BEGIN(INITIAL); yyterminate(); }
<STRSTATE>.                       { strbuf += yytext; }

<CHRSTATE>'                       {
                                       strbuf += "'";
                                       if (chrCharCount == 0) {
                                           reportError(tokStartLine, strbuf, "Empty character literal");
                                       } else if (chrCharCount > 1) {
                                           reportError(tokStartLine, strbuf, "Too many characters in character literal");
                                       } else if (!litHadError) {
                                           addToken(TokenType::CHAR_LITERAL, strbuf);
                                       }
                                       BEGIN(INITIAL);
                                   }
<CHRSTATE>\n                      { reportError( tokStartLine,  strbuf,  "Unterminated character literal"); BEGIN(INITIAL); yyless(0); }
<CHRSTATE><<EOF>>                 { reportError( tokStartLine,  strbuf,  "Unterminated character literal"); BEGIN(INITIAL); yyterminate(); }
<CHRSTATE>.                       { strbuf += yytext; chrCharCount++; }

 /* ---- numeric constants ---- */
0[xX]{HEXDIGIT}+{INT_SUFFIX}?                              { addToken(TokenType::INT_LITERAL, yytext); }
0[xX]({LETTER}({LETTER}|{DIGIT})*)?                         { reportError(yylineno, yytext, "Invalid hex literal: expected at least one hex digit after 0x"); }
0[bB]{BINDIGIT}+{INT_SUFFIX}?                               { addToken(TokenType::INT_LITERAL, yytext); }
0[bB][0-9]*[2-9][0-9]*                                      { reportError(yylineno, yytext, "Invalid binary literal: only digits 0/1 allowed after 0b"); }
0[bB]({LETTER}({LETTER}|{DIGIT})*)?                         { reportError(yylineno, yytext, "Invalid binary literal: expected at least one binary digit after 0b"); }
0{OCTDIGIT}+{INT_SUFFIX}?                                   { addToken(TokenType::INT_LITERAL, yytext); }
0[0-9]*[89][0-9]*                                           { reportError(yylineno, yytext, "Invalid octal literal: digits 8/9 not allowed after a leading 0"); }
{FRAC}([eE][+-]?{DIGIT}+)?[fF]?                             { addToken(TokenType::FLOAT_LITERAL, yytext); }
{DIGIT}+[eE][+-]?{DIGIT}+[fF]?                             { addToken(TokenType::FLOAT_LITERAL, yytext); }
{DIGIT}+{INT_SUFFIX}?                                       { addToken(TokenType::INT_LITERAL, yytext); }

 /* ---- multi-character operators (longest first). Flex's longest-match
    already disambiguates these declaratively -- e.g. "<<=" always wins
    over "<<" over "<" whenever the longer form is actually present --
    so order here is for readability, not correctness. Each assigns its
    own precise TokenType directly (no table lookup needed, since the
    pattern itself already identifies exactly which operator matched). ---- */
"..."                              { addToken(TokenType::ELLIPSIS_OP, yytext); }
"::"                               { addToken(TokenType::SCOPE_RESOLUTION_OP, yytext); }
"->"                               { addToken(TokenType::ARROW_OP, yytext); }
"++"                               { addToken(TokenType::INCREMENT_OP, yytext); }
"--"                               { addToken(TokenType::DECREMENT_OP, yytext); }
"<<="                              { addToken(TokenType::LSHIFT_ASSIGN_OP, yytext); }
">>="                              { addToken(TokenType::RSHIFT_ASSIGN_OP, yytext); }
"<<"                               { addToken(TokenType::LSHIFT_OP, yytext); }
">>"                               { addToken(TokenType::RSHIFT_OP, yytext); }
"<="                               { addToken(TokenType::LE_OP, yytext); }
">="                               { addToken(TokenType::GE_OP, yytext); }
"=="                               { addToken(TokenType::EQ_OP, yytext); }
"!="                               { addToken(TokenType::NE_OP, yytext); }
"&&"                               { addToken(TokenType::LOGICAL_AND_OP, yytext); }
"||"                               { addToken(TokenType::LOGICAL_OR_OP, yytext); }
"+="                               { addToken(TokenType::PLUS_ASSIGN_OP, yytext); }
"-="                               { addToken(TokenType::MINUS_ASSIGN_OP, yytext); }
"*="                               { addToken(TokenType::STAR_ASSIGN_OP, yytext); }
"/="                               { addToken(TokenType::DIVIDE_ASSIGN_OP, yytext); }
"%="                               { addToken(TokenType::MOD_ASSIGN_OP, yytext); }
"&="                               { addToken(TokenType::AMPERSAND_ASSIGN_OP, yytext); }
"|="                               { addToken(TokenType::PIPE_ASSIGN_OP, yytext); }
"^="                               { addToken(TokenType::CARET_ASSIGN_OP, yytext); }

 /* ---- single-character operators AND punctuation, in one rule: since
    several different characters share this one pattern, the specific
    TokenType is resolved via operator_token() (operator_map) at match
    time, mirroring how the reference handles this. ---- */
[+\-*/%=<>!&|^~.,?:(){}\[\]\;]    {
                                        auto op = operator_token(yytext);
                                        if (op.has_value()) {
                                            addToken(op.value(), yytext);
                                        } else {
                                            reportError(yylineno, yytext, "Illegal character");
                                        }
                                   }

[ \t\r]+                          { /* skip whitespace */ }
\n                                 { /* newline: yylineno auto-increments */ }

.                                  { reportError(  yylineno,  yytext,  "Illegal character"); }

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

    writeLexerLog(argv[1], diagnostics);

    if (hasErrors()) {
        fprintf(stderr, "Lexical analysis failed: %zu error(s) found in '%s'.\n",
                diagnostics.size(), argv[1]);
        for (const auto &d : diagnostics) {
            fprintf(stderr, "Line %d: %s (near '%s')\n",
                    d.line, d.message.c_str(), d.lexeme.c_str());
        }
        return 1;
    }

    printf("%-30s %-20s\n", "Lexeme", "Token");
    printf("%-30s %-20s\n", "------", "-----");

    for (const auto &t : tokens) {
        printf("%-30s %-20s\n",
               t.lexeme.c_str(),
               to_string(t.type).c_str());
    }

    return 0;
}
