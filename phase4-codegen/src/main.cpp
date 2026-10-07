/* mips_generator: source -> (phases 2, 2b, 3 unchanged) -> TAC -> MIPS
   assembly for SPIM, written to standard output.

     mips_generator [-O1|-O2] file.c > file.s
     spim -file file.s [program arguments]                                  */
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
#include "irgen.h"
#include "mips.h"
#include "opt.h"
#include "parser.tab.hpp"
#include "preprocessor/preprocessor.hpp"
#include "semantic.h"
#include "symbol_table/symbol_table.hpp"

extern FILE *yyin;
namespace fs = std::filesystem;

int main(int argc, char **argv) {
    const char *path = nullptr;
    int level = 0;
    for (int i = 1; i < argc; ++i) {
        if (!std::strcmp(argv[i], "-O1")) level = 1;
        else if (!std::strcmp(argv[i], "-O2")) level = 2;
        else if (!std::strcmp(argv[i], "-O0")) level = 0;
        else path = argv[i];
    }
    if (!path) {
        fprintf(stderr, "Usage: %s [-O1|-O2] <source-file>     (the assembly is written to standard output)\n", argv[0]);
        return 1;
    }
    /* the run-time library sits beside the executable */
    std::error_code ec;
    fs::path self = fs::canonical("/proc/self/exe", ec);
    std::ifstream rt((ec ? fs::path(argv[0]) : self).parent_path() / "runtime" / "runtime.s");
    if (!rt) {
        fprintf(stderr, "Error: runtime/runtime.s not found beside the executable\n");
        return 1;
    }
    std::stringstream runtime;
    runtime << rt.rdbuf();

    FILE *f = openPreprocessed(path);
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
        reportDiagnostic(lastLine, 1, "", "parser could not recover after the preceding error(s)", "Fatal error");
    }
    bool syntaxFailed = hasErrors();
    sem::SymbolTable table;
    if (!syntaxFailed) {
        sem::SemanticAnalyzer analyzer(table);
        analyzer.analyze(g_astRoot);
    }
    std::stable_sort(g_diagnostics.begin(), g_diagnostics.end(), [](const Diagnostic &a, const Diagnostic &b) {
        return a.line != b.line ? a.line < b.line : a.column < b.column;
    });
    std::ostringstream shown;
    for (const auto &d : g_diagnostics) printDiagnostic(shown, path, d, useColor(stderr));
    fputs(shown.str().c_str(), stderr);
    if (hasErrors()) {
        fprintf(stderr, "%s analysis failed: %zu error(s); no code was generated.\n", syntaxFailed ? "Syntax" : "Semantic",
                errorDiagnostics().size());
        return 1;
    }
    tac::Generator generator(table);
    tac::Program program = generator.generate(g_astRoot);
    if (!program.unsupported.empty()) {
        for (const auto &u : program.unsupported) fprintf(stderr, "code generation error: %s\n", u.c_str());
        return 1;
    }
    if (level > 0) tac::optimize(program, level);
    fputs(mips::generate(program, runtime.str()).c_str(), stdout);
    return 0;
}
