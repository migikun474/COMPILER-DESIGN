/*
 * lexer.l
 * Lexical analyzer for this project's custom C-like source language.
 *
 * Covers:
 *  - basic features: all arithmetic/logical operators, if-else, for, while,
 *    do-while, switch-case, int/char arrays, pointers, structures, printf/
 *    scanf, function calls with arguments, goto, break, continue, static
 *  - advanced features: variable-argument calls (...), dynamic memory
 *    allocation (malloc/free/calloc/realloc), command line input (argc/argv
 *    are identifiers, no new tokens needed), reference (&), until loop,
 *    multi-level pointers (*), multi-dimensional arrays ([ ][ ]), and the
 *    short/long/signed/unsigned type modifiers.
 *
 * Keyword categories (see the "keywords" rules below): this language
 * deliberately diverges from real C in these places:
 *   1. printf, scanf, malloc, free, calloc, realloc, FILE, fopen, fclose,
 *      fread, fwrite, fprintf, fscanf, fgets, fputs, feof are RESERVED
 *      KEYWORDS, not ordinary identifiers as they are in real C. Using
 *      any of these names as a variable/function name is therefore a
 *      syntax error in this language, unlike in standard C.
 *   2. until is a reserved keyword (standard C has no until loop).
 * Keywords are tagged with a specific category (type_keyword,
 * struct_keyword, enum_keyword, union_keyword, storage_keyword,
 * control_keyword, io_keyword, memory_keyword, file_keyword) instead of
 * one flat "keyword" token, so a later symbol-table / semantic-analysis
 * phase doesn't have to re-classify them.
 *
 * Behaviour:
 *  - If the whole input is lexically clean, prints a Lexeme/Token table.
 *  - If any lexical errors are found, prints every error found (with line
 *    number) instead of the table.
 */

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

 /* integer suffixes: u/U (unsigned), l/L (long), ll/LL (long long),
    in either order, matching the real-C grammar -- ll/LL must be the
    SAME case (lL / Ll are not valid and fall through to the malformed-
    literal catch-all below via maximal munch, since they're left
    unconsumed here and that rule greedily eats all trailing letters) */
LSUF        (l|L)
LLSUF       (ll|LL)
USUF        (u|U)
INT_SUFFIX  ({USUF}({LLSUF}|{LSUF})?|({LLSUF}|{LSUF}){USUF}?)

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

 /* ---- keywords, split by category so the parser/symbol-table phase
    doesn't have to re-classify a flat "keyword" bucket later ----
    NOTE: this language intentionally diverges from real C on two points:
      1. printf/scanf/malloc/free/calloc/realloc are RESERVED KEYWORDS
         here (io_keyword / memory_keyword), not ordinary identifiers.
         This is a deliberate language-design choice, unlike real C
         where they're just <stdio.h>/<stdlib.h> library functions.
      2. until is a reserved keyword (real C has no until loop). */

 /* type keywords: primitive types + size/sign modifiers */
"int"|"char"|"float"|"double"|"void"|"short"|"long"|"signed"|"unsigned"    { addToken("type_keyword", yytext); }

 /* struct/enum/union: kept separate from type_keyword since all three
    introduce a user-defined composite type (member list / enumerator
    list), not a primitive one -- symbol-table handling for these differs
    from handling a plain int/char/etc. */
"struct"                                                                   { addToken("struct_keyword", yytext); }
"enum"                                                                     { addToken("enum_keyword", yytext); }
"union"                                                                    { addToken("union_keyword", yytext); }

 /* storage-class keywords */
"static"|"typedef"                                                        { addToken("storage_keyword", yytext); }

 /* control-flow keywords */
"if"|"else"|"for"|"while"|"do"|"until"|"switch"|"case"|"default"|"break"|"continue"|"goto"|"return"   { addToken("control_keyword", yytext); }

 /* I/O keywords (custom to this language, see note above) */
"printf"|"scanf"                                                          { addToken("io_keyword", yytext); }

 /* dynamic-memory keywords (custom to this language, see note above) */
"malloc"|"free"|"calloc"|"realloc"                                        { addToken("memory_keyword", yytext); }

 /* file-manipulation keywords (custom to this language, see note above --
    real C treats FILE/fopen/fclose/etc. as ordinary <stdio.h> library
    identifiers, not reserved words) */
"FILE"|"fopen"|"fclose"|"fread"|"fwrite"|"fprintf"|"fscanf"|"fgets"|"fputs"|"feof"   { addToken("file_keyword", yytext); }

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

<STRSTATE>\"                      { strbuf += "\""; if (!litHadError) addToken("string_literal", strbuf.c_str()); BEGIN(INITIAL); }
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
                                           addToken("char_constant", strbuf.c_str());
                                       }
                                       BEGIN(INITIAL);
                                   }
<CHRSTATE>\n                      { reportError( tokStartLine,  strbuf,  "Unterminated character literal"); BEGIN(INITIAL); yyless(0); }
<CHRSTATE><<EOF>>                 { reportError( tokStartLine,  strbuf,  "Unterminated character literal"); BEGIN(INITIAL); yyterminate(); }
<CHRSTATE>.                       { strbuf += yytext; chrCharCount++; }

 /* ---- numeric constants ---- */
0[xX]{HEXDIGIT}+{INT_SUFFIX}?                              { addToken("integer_constant", yytext); }
0{OCTDIGIT}+{INT_SUFFIX}?                                   { addToken("integer_constant", yytext); }
0[0-9]*[89][0-9]*                                           { reportError(yylineno, yytext, "Invalid octal literal: digits 8/9 not allowed after a leading 0"); }
{DIGIT}+\.{DIGIT}+([eE][+-]?{DIGIT}+)?[fF]?               { addToken("float_constant", yytext); }
{DIGIT}+[eE][+-]?{DIGIT}+[fF]?                             { addToken("float_constant", yytext); }
{DIGIT}+{INT_SUFFIX}?                                       { addToken("integer_constant", yytext); }

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
               t.type.c_str());
    }

    return 0;
}
