/* semantic_analyzer: lexer -> parser (phase2-parser, unchanged) ->
   semantic analysis. Semantic analysis only runs on a syntactically
   valid program; with syntax/lexical errors it reports those exactly as
   phase 2 does and stops, since types cannot be checked on a partial
   tree without a cascade of bogus errors. */
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "ast/ast.hpp"
#include "diagnostics/diagnostics.hpp"
#include "parser.tab.hpp"
#include "preprocessor/preprocessor.hpp"
#include "report.h"
#include "semantic.h"
#include "symbol_table/symbol_table.hpp"

extern FILE *yyin;
namespace fs = std::filesystem;

static void writeLog(const std::string &sourceFile, const std::string &diagnostics, const std::string &status,
                     const std::string &details) {
    fs::create_directories("logs");
    std::ofstream log("logs/" + fs::path(sourceFile).stem().string() + ".log");
    if (!log) return;
    log << "=========================================\n";
    log << "       SEMANTIC ANALYSIS REPORT\n";
    log << "=========================================\n\n";
    log << "Source File : " << sourceFile << "\n\n";
    log << status << "\n\n";
    if (!diagnostics.empty()) log << diagnostics;
    log << details;
}

int main(int argc, char **argv) {
    bool quiet = false;
    const char *path = nullptr;
    for (int i = 1; i < argc; ++i) {
        if (!std::strcmp(argv[i], "-q")) quiet = true;
        else path = argv[i];
    }
    if (!path) {
        fprintf(stderr, "Usage: %s [-q] <source-file>\n  -q  print only the verdict and diagnostics\n", argv[0]);
        return 1;
    }
    FILE *f = openPreprocessed(path); /* #define, #include, #if ... */
    if (!f) {
        fprintf(stderr, "Error: could not open file '%s'\n", path);
        return 1;
    }
    yyin = f;
    pushScope("global");
    int parseResult = yyparse();
    resolvePendingReferences();
    fclose(f);
    if (parseResult != 0) {
        int lastLine = g_diagnostics.empty() ? g_currentLine : g_diagnostics.back().line;
        reportDiagnostic(lastLine, 1, "",
                         "parser could not recover after the preceding error(s) -- the rest of the file was not analyzed",
                         "Fatal error");
    }
    bool color = useColor(stderr);

    if (hasErrors()) { /* preprocessor / lexical / syntax errors: semantics cannot run */
        std::ostringstream plain, shown;
        for (const auto &d : g_diagnostics) {
            printDiagnostic(plain, path, d, false);
            printDiagnostic(shown, path, d, color);
        }
        bool preprocessing = false;
        for (const auto &d : g_diagnostics) preprocessing = preprocessing || d.kind == "Preprocessor error";
        std::string status = std::string(preprocessing ? "Preprocessing" : "Syntax analysis") + " failed: " +
                             std::to_string(errorDiagnostics().size()) + " error(s); semantic analysis was not run.";
        fprintf(stderr, "%s\n\n%s", status.c_str(), shown.str().c_str());
        writeLog(path, plain.str(), status, "");
        return 1;
    }

    sem::SymbolTable table;
    sem::SemanticAnalyzer analyzer(table);
    analyzer.analyze(g_astRoot);

    std::stable_sort(g_diagnostics.begin(), g_diagnostics.end(), [](const Diagnostic &a, const Diagnostic &b) {
        return a.line != b.line ? a.line < b.line : a.column < b.column;
    });
    std::ostringstream plain, shown;
    for (const auto &d : g_diagnostics) {
        printDiagnostic(plain, path, d, false);
        printDiagnostic(shown, path, d, color);
    }
    int errors = static_cast<int>(errorDiagnostics().size());
    int warnings = static_cast<int>(warningDiagnostics().size()); /* semantic + preprocessor */
    std::string counts = std::to_string(errors) + " error(s), " + std::to_string(warnings) + " warning(s)";

    std::ostringstream details;
    if (errors == 0) {
        details << "=== Annotated AST ===\n";
        sem::printAnnotatedAST(g_astRoot, details);
        details << "\n=== Semantic Symbol Table ===\n";
        sem::printSemanticSymbolTable(table, details);
        details << "\n=== Record Layouts (MIPS32) ===\n";
        sem::printRecordLayouts(table, details);
    }

    if (errors) {
        std::string status = "Semantic analysis failed: " + counts + " in '" + std::string(path) + "'.";
        fprintf(stderr, "%s\n\n%s", status.c_str(), shown.str().c_str());
        writeLog(path, plain.str(), status, "");
        return 1;
    }
    std::string status = "Semantic analysis successful: " + counts + " in '" + std::string(path) + "'.";
    printf("%s\n\n", status.c_str());
    if (warnings) {
        fputs(shown.str().c_str(), stderr);
        fflush(stderr);
    }
    if (!quiet) fputs(details.str().c_str(), stdout);
    writeLog(path, plain.str(), status, details.str());
    return 0;
}
