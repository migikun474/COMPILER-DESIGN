#include <cstdio>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "ast/ast.hpp"
#include "diagnostics/diagnostics.hpp"
#include "parser.tab.hpp"
#include "preprocessor/preprocessor.hpp"
#include "symbol_table/symbol_table.hpp"
#include "token/token_log.hpp"

extern FILE *yyin;
namespace fs = std::filesystem;

static void writeLog(const std::string &sourceFile) {
    fs::create_directories("logs");
    std::string logfile = "logs/" + fs::path(sourceFile).stem().string() + ".log";
    FILE *log = fopen(logfile.c_str(), "w");
    if (!log) return;

    fprintf(log, "=========================================\n");
    fprintf(log, "        SYNTAX ANALYSIS REPORT\n");
    fprintf(log, "=========================================\n\n");
    fprintf(log, "Source File : %s\n\n", sourceFile.c_str());

    if (!hasErrors()) {
        fprintf(log, "No errors found.\n\n");
        for (const auto &w : warningDiagnostics()) {
            std::ostringstream one;
            printDiagnostic(one, sourceFile, w, /*color=*/false);
            fprintf(log, "%s", one.str().c_str());
        }

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
        fprintf(log, "Total Errors : %zu\n", errorDiagnostics().size());

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

    /* the scanner reads the preprocessed text (#define, #include, #if ...) */
    FILE *f = openPreprocessed(argv[1]);
    if (!f) {
        fprintf(stderr, "Error: could not open file '%s'\n", argv[1]);
        return 1;
    }

    yyin = f;
    pushScope("global");
    int parseResult = yyparse();
    resolvePendingReferences();
    fclose(f);

    /* yyparse() returns 1 when panic-mode recovery itself fails --
       e.g. a second syntax error arrives before three tokens have been
       successfully shifted since the last one, or recovery can't find
       any ';'/'}' the stack will accept before EOF. When that happens
       Bison just stops: everything after the last successfully parsed
       construct is silently missing from the AST/log, with nothing
       saying why. Surface it explicitly instead of leaving that as a
       silent truncation -- this is a real, reachable failure mode of
       the grammar's two-rule (`error ';'` / `error '}'`) recovery, not
       a hypothetical one; see test20_syntax_errors_cascading_recovery.c. */
    if (parseResult != 0) {
        int lastLine = g_diagnostics.empty() ? g_currentLine : g_diagnostics.back().line;
        reportDiagnostic(lastLine, 1, "",
                          "parser could not recover after the preceding error(s) -- "
                          "the rest of the file was not analyzed",
                          "Fatal error");
    }

    writeLog(argv[1]);

    if (hasErrors()) {
        bool color = useColor(stderr);
        fprintf(stderr, "Syntax analysis failed: %zu error(s) found in '%s'.\n\n",
                errorDiagnostics().size(), argv[1]);
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
    if (!g_diagnostics.empty()) { /* preprocessor warnings */
        std::ostringstream warns;
        for (const auto &w : g_diagnostics) printDiagnostic(warns, argv[1], w, useColor(stderr));
        fputs(warns.str().c_str(), stderr);
        fflush(stderr);
    }

    printTokenTable(std::cout);

    printf("\n=== Abstract Syntax Tree ===\n");
    printAST(g_astRoot, std::cout);

    printSymbolTable(std::cout);

    return 0;
}
