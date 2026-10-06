#ifndef SHARED_DIAGNOSTICS_HPP
#define SHARED_DIAGNOSTICS_HPP

/* Diagnostics shared by every phase: one list that the lexer, the
   parser and semantic analysis all report into, the source text they
   quote from, the scanner's current position, and the GCC/Clang-style
   printer ("file:line:col: kind: message", source line, caret). */

#include <cstdio>
#include <ostream>
#include <string>
#include <vector>

struct Diagnostic {
    int line;
    int column;
    std::string near_text;
    std::string message;
    std::string kind; /* "Lexical error", "Syntax error", "Semantic error",
                          "Fatal error", or "... warning" */
};

extern std::vector<Diagnostic> g_diagnostics;

extern std::vector<std::string> g_sourceLines;

void reportDiagnostic(int line, int column, const std::string &near_text,
                       const std::string &message, const std::string &kind);
/* true when any diagnostic is an error (warnings do not count) */
bool hasErrors();
bool isWarning(const Diagnostic &d);
std::vector<Diagnostic> errorDiagnostics();
std::vector<Diagnostic> warningDiagnostics();

std::string lastErrorLabel();

/* current line / column / lexeme, updated by the scanner on every
   token, so yyerror() can report an accurate location for syntax
   errors -- column is the 1-based column the token STARTS at. */
extern int g_currentLine;
extern int g_currentColumn;
extern std::string g_lastText;


/* ---- where each line came from (filled by the preprocessor) ----
   The lexer and parser see the *preprocessed* text, one line per
   g_sourceLines entry, and every position in the compiler (tokens, AST
   nodes, symbols, diagnostics) is a line of that text. g_lineOrigins
   maps it back to the file and line the user wrote, for display only.
   With no map (or a line beyond it) a line is its own origin. */
struct LineOrigin {
    int file = 0;          /* index into g_sourceFiles; 0 = the main file */
    int line = 0;          /* line in that file */
    std::string text;      /* that line as written */
    bool expanded = false; /* text differs after macro expansion */
};
extern std::vector<std::string> g_sourceFiles; /* [0] = main file, as named on the command line */
extern std::vector<LineOrigin> g_lineOrigins;

/* "12" for line 12 of the main file, "util.h:3" for an included file */
std::string displayLine(int line);

/* true when `f` is a terminal, i.e. ANSI colors are wanted */
bool useColor(FILE *f);

/* fills g_sourceLines, which printDiagnostic() quotes from */
void loadSourceLines(const std::string &path);

/* GCC/Clang-style: "file:line:col: <kind>: message", the source line,
   a caret, and a fix-it note when Bison named one unambiguous token.
   Diagnostics whose kind contains "warning" are colored as warnings. */
void printDiagnostic(std::ostream &out, const std::string &sourceFile,
                     const Diagnostic &d, bool color);

#endif
