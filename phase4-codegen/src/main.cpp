/* mips_generator: the combined driver. source -> (phases 2, 2b, 3
   unchanged) -> TAC -> MIPS assembly for SPIM, written to standard output;
   a stage flag stops earlier and prints that stage instead (D40).

     mips_generator [-O1] file.c > file.s
     spim -file file.s [program arguments]
     mips_generator --tokens|--ast|--symbols file.c
     mips_generator [-O1] --tac file.c
     mips_generator [-O1] --run file.c [program arguments] < input          */
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
#include "interp.h"
#include "token/token_log.hpp"
#include "irgen.h"
#include "mips.h"
#include "opt.h"
#include "parser.tab.hpp"
#include "semantic.h"
#include "symbol_table/symbol_table.hpp"

extern FILE *yyin;
namespace fs = std::filesystem;

int main(int argc, char **argv) {
    const char *path = nullptr;
    int level = 0;
    std::string stage;   /* "" = MIPS; tokens, ast, symbols, tac, run */
    std::vector<std::string> programArgs;
    for (int i = 1; i < argc; ++i) {
        if (path) { programArgs.push_back(argv[i]); continue; } /* after the file: arguments for --run */
        if (!std::strcmp(argv[i], "-O1")) level = 1;
        else if (!std::strcmp(argv[i], "-O0")) level = 0;
        else if (!std::strcmp(argv[i], "--tokens") || !std::strcmp(argv[i], "--ast") || !std::strcmp(argv[i], "--symbols") ||
                 !std::strcmp(argv[i], "--tac") || !std::strcmp(argv[i], "--run"))
            stage = argv[i] + 2;
        else if (argv[i][0] == '-') {
            fprintf(stderr, "unknown option '%s' (the only optimization level is -O1)\n", argv[i]);
            return 1;
        } else path = argv[i];
    }
    if (!path) {
        fprintf(stderr, "Usage: %s [-O1] [stage] <source-file> [program arguments]\n"
                        "  (the assembly is written to standard output)\n"
                        "  stage: stop after a phase and print it instead of the assembly\n"
                        "    --tokens   the token table          --ast   the syntax tree\n"
                        "    --symbols  the semantic symbol table --tac   the three-address code\n"
                        "    --run      run the TAC with the interpreter (stdin is the program's input)\n", argv[0]);
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

    FILE *f = openSource(path);
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
    if (stage == "tokens" || stage == "ast") {
        if (stage == "tokens") printTokenTable(std::cout);
        else printAST(g_astRoot, std::cout);
        std::ostringstream errs;
        for (const auto &d : g_diagnostics) printDiagnostic(errs, path, d, useColor(stderr));
        fputs(errs.str().c_str(), stderr);
        return syntaxFailed ? 1 : 0;
    }
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
    for (const auto &w : tac::uninitializedReads(program))
        fprintf(stderr, "%s:%s: warning: %s [uninitialized]\n", path, displayLine(w.first).c_str(), w.second.c_str());
    if (stage == "symbols") {
        sem::printSemanticSymbolTable(table, std::cout);
        return 0;
    }
    if (level > 0) tac::optimize(program);
    if (stage == "tac") {
        tac::printProgram(program, std::cout);
        return 0;
    }
    if (stage == "run") {
        std::stringstream input;
        input << std::cin.rdbuf();
        tac::RunResult r = tac::run(program, programArgs, input.str());
        fputs(r.output.c_str(), stdout);
        if (!r.error.empty()) {
            fprintf(stderr, "\nrun-time error: %s\n", r.error.c_str());
            return 2;
        }
        return r.exitCode;
    }
    std::string assembly = mips::generate(program, runtime.str(), level > 0);
    fputs(assembly.c_str(), stdout);
    /* also logs/<file>.s, or <file>.O1.s: runnable as it is */
    fs::create_directories("logs");
    std::string suffix = level > 0 ? ".O1.s" : ".s";
    std::ofstream log("logs/" + fs::path(path).stem().string() + suffix);
    log << "# =========================================================================\n"
        << "#  MIPS ASSEMBLY  --  run with: spim -file <this file>\n"
        << "# =========================================================================\n"
        << "#  Source file  : " << path << "\n"
        << "#  Optimization : " << (level > 0 ? "-O1 (TAC optimizations inside basic blocks, constants inside instructions)" : "no optimization") << "\n"
        << "# =========================================================================\n\n"
        << assembly;
    return 0;
}
