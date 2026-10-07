/* tac_generator: lexer -> parser -> semantic analysis (phases 2 and 2b,
   unchanged) -> three address code. TAC is only generated for a program
   with no lexical, syntax or semantic errors.

     tac_generator file.c              print the TAC (also written to logs/file.tac)
     tac_generator --run file.c [args] print the TAC, then execute it
     tac_generator --run -q file.c     execute only: the program's own output   */
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
#include "parser.tab.hpp"
#include "preprocessor/preprocessor.hpp"
#include "semantic.h"
#include "symbol_table/symbol_table.hpp"
#include "tac.h"

extern FILE *yyin;
namespace fs = std::filesystem;

static void writeLog(const std::string &sourceFile, const std::string &status, const std::string &body) {
    fs::create_directories("logs");
    std::ofstream log("logs/" + fs::path(sourceFile).stem().string() + ".tac");
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
    std::vector<std::string> programArgs;
    for (int i = 1; i < argc; ++i) {
        if (!path && !std::strcmp(argv[i], "--run")) runIt = true;
        else if (!path && !std::strcmp(argv[i], "-q")) quiet = true;
        else if (!path) path = argv[i];
        else programArgs.push_back(argv[i]); /* passed to the program's main */
    }
    if (!path) {
        fprintf(stderr, "Usage: %s [--run [-q]] <source-file> [program arguments]\n"
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
    if (!quiet) printf("%s\n\n%s", status.c_str(), body.str().c_str());
    writeLog(path, status, body.str());
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
    fprintf(stderr, "%s[exit code %d, %lld instructions executed]\n",
            !result.output.empty() && result.output.back() != '\n' ? "\n" : "", result.exitCode, result.executed);
    return result.exitCode;
}
