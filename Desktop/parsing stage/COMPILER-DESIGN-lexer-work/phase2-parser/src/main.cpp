#include <cstdio>
#include <cstdlib>
#include <filesystem>
#include <iostream>
#include <sstream>
#include <string>

#include "ast.h"
#include "common.h"
#include "parser.tab.hpp"

extern FILE *yyin;
namespace fs = std::filesystem;

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
    if (e.kind != SymKind::PROCEDURE) return "";
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
static void printSymbolTable(std::ostream &out) {
    out << "\n=== Symbol Table ===\n";
    char header[256];
    snprintf(header, sizeof(header), "%-20s %-14s %-6s %-16s %-24s %-9s %-22s %s\n",
             "Name", "Kind", "Line", "Type", "Qualifiers", "Uses", "Signature", "Mangled Name");
    out << header;
    snprintf(header, sizeof(header), "%-20s %-14s %-6s %-16s %-24s %-9s %-22s %s\n",
             "----", "----", "----", "----", "----------", "----", "---------", "------------");
    out << header;
    for (const auto &e : g_symbolTable) {
        char line[512];
        snprintf(line, sizeof(line), "%-20s %-14s %-6d %-16s %-24s %-9d %-22s %s\n",
                 e.qualifiedName.c_str(), symKindName(e.kind).c_str(), e.declLine,
                 e.typeStr.c_str(), qualifiersFor(e).c_str(), e.useCount,
                 signatureFor(e).c_str(), e.mangledName.c_str());
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

        std::ostringstream ast;
        printAST(g_astRoot, ast);
        fprintf(log, "--- Abstract Syntax Tree ---\n%s\n", ast.str().c_str());

        std::ostringstream syms;
        printSymbolTable(syms);
        fprintf(log, "%s", syms.str().c_str());
    } else {
        int count = 1;
        for (const auto &d : g_diagnostics) {
            fprintf(log, "[%d]\n", count++);
            fprintf(log, "Kind    : %s\n", d.kind.c_str());
            fprintf(log, "Line    : %d\n", d.line);
            fprintf(log, "Near    : %s\n", d.near_text.c_str());
            fprintf(log, "Message : %s\n\n", d.message.c_str());
        }
        fprintf(log, "-----------------------------------------\n");
        fprintf(log, "Total Errors : %zu\n", g_diagnostics.size());
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

    yyin = f;
    pushScope(); /* global scope */
    yyparse();
    fclose(f);

    writeLog(argv[1]);

    if (hasErrors()) {
        fprintf(stderr, "Syntax analysis failed: %zu error(s) found in '%s'.\n",
                g_diagnostics.size(), argv[1]);
        for (const auto &d : g_diagnostics) {
            fprintf(stderr, "Line %d: %s: %s (near '%s')\n",
                    d.line, d.kind.c_str(), d.message.c_str(), d.near_text.c_str());
        }
        fprintf(stderr, "Report written to logs/%s.log\n",
                fs::path(argv[1]).stem().string().c_str());
        return 1;
    }

    printf("Syntax analysis successful: no errors found in '%s'.\n\n", argv[1]);

    printf("%-30s %-20s\n", "Token", "Token_Type");
    printf("%-30s %-20s\n", "-----", "----------");
    for (const auto &t : g_tokens) {
        printf("%-30s %-20s\n", t.lexeme.c_str(), t.category.c_str());
    }

    printf("\n=== Abstract Syntax Tree ===\n");
    printAST(g_astRoot, std::cout);

    printSymbolTable(std::cout);

    return 0;
}
