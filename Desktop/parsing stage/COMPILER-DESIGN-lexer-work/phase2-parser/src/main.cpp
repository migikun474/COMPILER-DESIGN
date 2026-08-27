#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unistd.h> /* isatty, fileno -- used to decide whether to colorize */

#include "ast.h"
#include "common.h"
#include "parser.tab.hpp"

extern FILE *yyin;
namespace fs = std::filesystem;

/* Minimal ANSI color set, GCC/Clang-flavored: bold location, red
   "error", bold message, bold-red caret. Only ever used when writing
   to an actual terminal (see useColor()) -- the log file always stays
   plain text, since escape codes in a saved file are just noise to
   anyone reading it in an editor. */
namespace col {
    constexpr const char *RESET = "\033[0m";
    constexpr const char *BOLD  = "\033[1m";
    constexpr const char *RED   = "\033[1;31m";
    constexpr const char *GREEN = "\033[1;32m";
}

static bool useColor(FILE *f) {
    return isatty(fileno(f)) != 0;
}

/* Reads the whole source file into g_sourceLines, one entry per line
   (no trailing '\n'), so diagnostics can show a GCC/Clang-style
   source snippet under each error instead of just a line number. */
static void loadSourceLines(const std::string &path) {
    std::ifstream f(path);
    std::string line;
    while (std::getline(f, line)) g_sourceLines.push_back(line);
}

/* Prints one diagnostic the way GCC/Clang do: a location line, the
   actual source line, and a caret under the exact column -- instead
   of just "Line 3: syntax error". Shared by both the colorized
   terminal output and the plain-text log file. */
/* Clang-style "fix-it": if the Bison message ends in "expecting 'X'"
   for exactly one literal token X (not "expecting 'X' or 'Y'", which
   is genuinely ambiguous -- we're not going to guess which one the
   programmer meant), pull out that literal so a suggested insertion
   can be shown under the caret. Returns "" when there's nothing safe
   to suggest. */
static std::string singleExpectedLiteral(const std::string &message) {
    size_t pos = message.rfind("expecting ");
    if (pos == std::string::npos) return "";
    std::string tail = message.substr(pos + std::string("expecting ").size());
    if (tail.find(" or ") != std::string::npos) return ""; /* ambiguous, don't guess */
    if (tail.size() < 3 || tail.front() != '\'') return "";  /* not a literal token */
    size_t close = tail.find('\'', 1);
    if (close == std::string::npos) return "";
    return tail.substr(1, close - 1);
}

static void printDiagnostic(std::ostream &out, const std::string &sourceFile,
                             const Diagnostic &d, bool color) {
    std::string label = d.kind; /* "Syntax error" / "Lexical error" */
    if (!label.empty()) label[0] = static_cast<char>(std::tolower(label[0]));

    if (color) {
        out << col::BOLD << sourceFile << ":" << d.line << ":" << d.column << ": "
            << col::RESET << col::RED << label << ": " << col::RESET
            << col::BOLD << d.message << col::RESET << "\n";
    } else {
        out << sourceFile << ":" << d.line << ":" << d.column << ": "
            << label << ": " << d.message << "\n";
    }

    if (d.line >= 1 && d.line <= static_cast<int>(g_sourceLines.size())) {
        const std::string &srcLine = g_sourceLines[d.line - 1];
        std::string lineNumStr = std::to_string(d.line);
        std::string gutter(lineNumStr.size(), ' ');

        out << " " << lineNumStr << " | " << srcLine << "\n";

        std::string indent;
        for (int i = 1; i < d.column; ++i) {
            bool wasTab = (i - 1 < static_cast<int>(srcLine.size())) && srcLine[i - 1] == '\t';
            indent += wasTab ? '\t' : ' ';
        }

        out << " " << gutter << " | " << indent;
        if (color) out << col::RED << col::BOLD << "^" << col::RESET << "\n";
        else out << "^\n";

        /* Clang-style fix-it: suggest the missing token, in a
           different color from the error itself -- only when Bison's
           message named exactly one unambiguous literal to insert. */
        std::string fixit = singleExpectedLiteral(d.message);
        if (!fixit.empty()) {
            out << " " << gutter << " | ";
            if (color) {
                out << col::GREEN << "note: insert '" << fixit << "' here" << col::RESET << "\n";
            } else {
                out << "note: insert '" << fixit << "' here\n";
            }
        }
    }
    out << "\n";
}

static std::string qualifiersFor(const SymbolTableEntry &e) {
    std::string q;
    if (e.isStatic) q += "static ";
    if (e.isConst) q += "const ";
    if (e.isVolatile) q += "volatile ";
    if (e.pointerLevel > 0) q += std::string(e.pointerLevel, '*') + " ";
    if (e.arrayLevel > 0) q += "[]" + std::string(e.arrayLevel > 1 ? std::to_string(e.arrayLevel) : "") + " ";
    if (!q.empty()) q.pop_back(); /* trailing space */
    return q;
}

static std::string signatureFor(const SymbolTableEntry &e) {
    if (e.kind != SymKind::PROCEDURE && e.returnType.empty()) return "";
    std::string sig = e.returnType.empty() ? "?" : e.returnType;
    sig += " (";
    for (size_t i = 0; i < e.paramTypes.size(); ++i) {
        if (i) sig += ", ";
        sig += e.paramTypes[i];
    }
    sig += ")";
    return sig;
}

/* Shared by both the stdout report and the on-disk log, so the two
   never drift apart. */
static void printTokenTable(std::ostream &out) {
    char header[64];
    snprintf(header, sizeof(header), "%-30s %-20s\n", "Token", "Token_Type");
    out << header;
    snprintf(header, sizeof(header), "%-30s %-20s\n", "-----", "----------");
    out << header;
    for (const auto &t : g_tokens) {
        char line[128];
        snprintf(line, sizeof(line), "%-30s %-20s\n", t.lexeme.c_str(), t.category.c_str());
        out << line;
    }
}

static void printSymbolTable(std::ostream &out) {
    out << "\n=== Symbol Table ===\n";
    char header[256];
    snprintf(header, sizeof(header), "%-20s %-14s %-6s %-28s %-16s %-24s %-9s %-22s %s\n",
             "Name", "Kind", "Line", "Scope", "Type", "Qualifiers", "Uses", "Signature", "Mangled Name");
    out << header;
    snprintf(header, sizeof(header), "%-20s %-14s %-6s %-28s %-16s %-24s %-9s %-22s %s\n",
             "----", "----", "----", "-----", "----", "----------", "----", "---------", "------------");
    out << header;
    for (const auto &e : g_symbolTable) {
        char line[512];
        snprintf(line, sizeof(line), "%-20s %-14s %-6d %-28s %-16s %-24s %-9d %-22s %s\n",
                 e.qualifiedName.c_str(), symKindName(e.kind).c_str(), e.declLine,
                 e.scopePath.c_str(), e.typeStr.c_str(), qualifiersFor(e).c_str(),
                 e.useCount, signatureFor(e).c_str(), e.mangledName.c_str());
        out << line;
    }
}

static void writeLog(const std::string &sourceFile) {
    fs::create_directories("logs");
    std::string logfile = "logs/" + fs::path(sourceFile).stem().string() + ".log";
    FILE *log = fopen(logfile.c_str(), "w");
    if (!log) return;

    fprintf(log, "=========================================\n");
    fprintf(log, "        SYNTAX ANALYSIS REPORT\n");
    fprintf(log, "=========================================\n\n");
    fprintf(log, "Source File : %s\n\n", sourceFile.c_str());

    if (g_diagnostics.empty()) {
        fprintf(log, "No errors found.\n\n");

        std::ostringstream tokens;
        printTokenTable(tokens);
        fprintf(log, "--- Token / Token_Type ---\n%s\n", tokens.str().c_str());

        std::ostringstream ast;
        printAST(g_astRoot, ast);
        fprintf(log, "--- Abstract Syntax Tree ---\n%s\n", ast.str().c_str());

        std::ostringstream syms;
        printSymbolTable(syms);
        fprintf(log, "%s", syms.str().c_str());
    } else {
        std::ostringstream diags;
        for (const auto &d : g_diagnostics) {
            printDiagnostic(diags, sourceFile, d, /*color=*/false);
        }
        fprintf(log, "%s", diags.str().c_str());
        fprintf(log, "-----------------------------------------\n");
        fprintf(log, "Total Errors : %zu\n", g_diagnostics.size());

        if (g_astRoot && !g_astRoot->children.empty()) {
            fprintf(log, "\n--- Partial AST (best-effort; each broken construct shows as ErrorNode) ---\n");
            std::ostringstream ast;
            printAST(g_astRoot, ast);
            fprintf(log, "%s", ast.str().c_str());
        }
    }
    fclose(log);
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <source-file>\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        fprintf(stderr, "Error: could not open file '%s'\n", argv[1]);
        return 1;
    }

    loadSourceLines(argv[1]);

    yyin = f;
    pushScope("global");
    yyparse();
    fclose(f);

    writeLog(argv[1]);

    if (hasErrors()) {
        bool color = useColor(stderr);
        fprintf(stderr, "Syntax analysis failed: %zu error(s) found in '%s'.\n\n",
                g_diagnostics.size(), argv[1]);
        std::ostringstream diags;
        for (const auto &d : g_diagnostics) {
            printDiagnostic(diags, argv[1], d, color);
        }
        fputs(diags.str().c_str(), stderr);

        if (g_astRoot && !g_astRoot->children.empty()) {
            fprintf(stderr, "--- Partial AST (best-effort; each broken construct shows as ErrorNode) ---\n");
            printAST(g_astRoot, std::cerr);
            fprintf(stderr, "\n");
        }

        fprintf(stderr, "Report written to logs/%s.log\n",
                fs::path(argv[1]).stem().string().c_str());
        return 1;
    }

    printf("Syntax analysis successful: no errors found in '%s'.\n\n", argv[1]);

    printTokenTable(std::cout);

    printf("\n=== Abstract Syntax Tree ===\n");
    printAST(g_astRoot, std::cout);

    printSymbolTable(std::cout);

    return 0;
}
