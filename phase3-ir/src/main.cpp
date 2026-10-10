/* tac_generator: lexer -> parser -> semantic analysis (phases 2 and 2b,
   unchanged) -> three address code. TAC is only generated for a program
   with no lexical, syntax or semantic errors.

     tac_generator file.c              print the TAC (also written to logs/file.tac)
     tac_generator --run file.c [args] print the TAC, then execute it
     tac_generator --run -q file.c     execute only: the program's own output
     tac_generator -O1 file.c          optimize (-O2: also across basic blocks); with
                                       --run the program is run before and after
                                       and must behave the same                    */
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
#include "irgen.h"
#include "opt.h"
#include "parser.tab.hpp"
#include "preprocessor/preprocessor.hpp"
#include "semantic.h"
#include "symbol_table/symbol_table.hpp"
#include "tac.h"

extern FILE *yyin;
namespace fs = std::filesystem;

static void writeLog(const std::string &sourceFile, const std::string &status, const std::string &body,
                     const std::string &suffix = ".tac") {
    fs::create_directories("logs");
    std::ofstream log("logs/" + fs::path(sourceFile).stem().string() + suffix);
    if (!log) return;
    log << "=========================================\n";
    log << "         THREE ADDRESS CODE\n";
    log << "=========================================\n\n";
    log << "Source File : " << sourceFile << "\n\n";
    log << status << "\n\n" << body;
}

int main(int argc, char **argv) {
    const char *path = nullptr;
    bool runIt = false, quiet = false;
    int level = 0;
    std::vector<std::string> programArgs;
    for (int i = 1; i < argc; ++i) {
        if (!path && !std::strcmp(argv[i], "--run")) runIt = true;
        else if (!path && !std::strcmp(argv[i], "-q")) quiet = true;
        else if (!path && !std::strcmp(argv[i], "-O1")) level = 1;
        else if (!path && !std::strcmp(argv[i], "-O2")) level = 2;
        else if (!path && !std::strcmp(argv[i], "-O3")) level = 3;
        else if (!path && !std::strcmp(argv[i], "-O0")) level = 0;
        else if (!path) path = argv[i];
        else programArgs.push_back(argv[i]); /* passed to the program's main */
    }
    if (!path) {
        fprintf(stderr, "Usage: %s [-O1|-O2|-O3] [--run [-q]] <source-file> [program arguments]\n"
                        "  -O1    optimize inside basic blocks\n"
                        "  -O2    -O1 plus constant/copy propagation and dead assignments across blocks\n"
                        "  -O3    -O2 plus inlining, tail recursion, global common subexpressions, loop-invariant code motion\n"
                        "  --run  execute the generated code with the TAC interpreter\n"
                        "  -q     with --run: print only what the program prints\n", argv[0]);
        return 1;
    }
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
        reportDiagnostic(lastLine, 1, "",
                         "parser could not recover after the preceding error(s) -- the rest of the file was not analyzed",
                         "Fatal error");
    }
    bool color = useColor(stderr);
    bool syntaxFailed = hasErrors();

    sem::SymbolTable table;
    if (!syntaxFailed) {
        sem::SemanticAnalyzer analyzer(table);
        analyzer.analyze(g_astRoot);
    }
    std::stable_sort(g_diagnostics.begin(), g_diagnostics.end(), [](const Diagnostic &a, const Diagnostic &b) {
        return a.line != b.line ? a.line < b.line : a.column < b.column;
    });
    std::ostringstream plain, shown;
    for (const auto &d : g_diagnostics) {
        printDiagnostic(plain, path, d, false);
        printDiagnostic(shown, path, d, color);
    }
    if (hasErrors()) {
        std::string status = std::string(syntaxFailed ? "Syntax analysis" : "Semantic analysis") + " failed: " +
                             std::to_string(errorDiagnostics().size()) + " error(s); no code was generated.";
        fprintf(stderr, "%s\n\n%s", status.c_str(), shown.str().c_str());
        writeLog(path, status, plain.str());
        return 1;
    }
    if (!g_diagnostics.empty()) { /* warnings */
        fputs(shown.str().c_str(), stderr);
        fflush(stderr);
    }

    tac::Generator generator(table);
    tac::Program program = generator.generate(g_astRoot);
    if (!program.unsupported.empty()) {
        for (const auto &u : program.unsupported) fprintf(stderr, "code generation error: %s\n", u.c_str());
        return 1;
    }
    size_t instructions = 0;
    for (const auto &fn : program.functions) instructions += fn.quads.size();
    std::string status = "Three address code generated: " + std::to_string(program.functions.size()) +
                         " function(s), " + std::to_string(instructions) + " instruction(s) for '" + std::string(path) + "'.";
    std::ostringstream body;
    tac::printProgram(program, body);
    tac::Program raw = program; /* kept to compare behaviour with the optimized code */
    if (level > 0) {
        tac::OptStats stats = tac::optimize(program, level);
        body.str("");
        tac::printStats(stats, body);
        tac::printProgram(program, body);
        status = "Optimized three address code (-O" + std::to_string(level) + "): " + std::to_string(stats.before) +
                 " -> " + std::to_string(stats.after) + " instruction(s) for '" + std::string(path) + "'.";
    }
    if (!quiet) printf("%s\n\n%s", status.c_str(), body.str().c_str());
    writeLog(path, status, body.str(), level > 0 ? ".O" + std::to_string(level) + ".tac" : ".tac");
    if (!runIt) return 0;

    bool readsInput = false;
    for (const auto &fn : program.functions)
        for (const auto &q : fn.quads) readsInput = readsInput || q.calleeName == "scanf";
    std::string input;
    if (readsInput) input.assign(std::istreambuf_iterator<char>(std::cin), std::istreambuf_iterator<char>());
    programArgs.insert(programArgs.begin(), fs::path(path).stem().string());
    tac::RunResult result = tac::run(program, programArgs, input);
    if (!quiet) printf("=== program output ===\n");
    fputs(result.output.c_str(), stdout);
    fflush(stdout);
    if (!result.error.empty()) {
        fprintf(stderr, "\nrun-time error: %s\n", result.error.c_str());
        return 2;
    }
    const char *newline = !result.output.empty() && result.output.back() != '\n' ? "\n" : "";
    if (level > 0) { /* the optimizer's own check: same output, same exit code */
        tac::RunResult before = tac::run(raw, programArgs, input);
        if (before.output != result.output || before.exitCode != result.exitCode || before.error != result.error) {
            fprintf(stderr, "%sOPTIMIZER BUG: the optimized program behaves differently (exit %d, was %d)\n", newline,
                    result.exitCode, before.exitCode);
            return 3;
        }
        fprintf(stderr, "%s[exit code %d, %lld instructions executed; %lld without -O%d: %lld%% fewer]\n", newline,
                result.exitCode, result.executed, before.executed, level,
                before.executed ? 100 * (before.executed - result.executed) / before.executed : 0);
        return result.exitCode;
    }
    fprintf(stderr, "%s[exit code %d, %lld instructions executed]\n", newline, result.exitCode, result.executed);
    return result.exitCode;
}
