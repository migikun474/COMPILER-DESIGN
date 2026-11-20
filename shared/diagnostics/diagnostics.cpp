#include "diagnostics/diagnostics.hpp"

#include <cctype>
#include <cstdio>
#include <fstream>
#include <unistd.h> /* isatty, fileno -- used to decide whether to colorize */

std::vector<Diagnostic> g_diagnostics;
int g_currentLine = 1;
int g_currentColumn = 1;
std::string g_lastText;
std::vector<std::string> g_sourceLines;

void reportDiagnostic(int line, int column, const std::string &near_text,
                       const std::string &message, const std::string &kind) {
    g_diagnostics.push_back({line, column, near_text, message, kind});
}

bool isWarning(const Diagnostic &d) { return d.kind.find("warning") != std::string::npos; }

bool hasErrors() {
    for (const auto &d : g_diagnostics) {
        if (!isWarning(d)) return true;
    }
    return false;
}

FILE *openSource(const std::string &path) {
    std::ifstream in(path);
    if (!in) return nullptr;
    g_sourceLines.clear();
    for (std::string line; std::getline(in, line);) g_sourceLines.push_back(line);
    return std::fopen(path.c_str(), "r");
}

std::string displayLine(int line) { return std::to_string(line); }

std::vector<Diagnostic> errorDiagnostics() {
    std::vector<Diagnostic> out;
    for (const auto &d : g_diagnostics) {
        if (!isWarning(d)) out.push_back(d);
    }
    return out;
}

std::vector<Diagnostic> warningDiagnostics() {
    std::vector<Diagnostic> out;
    for (const auto &d : g_diagnostics) {
        if (isWarning(d)) out.push_back(d);
    }
    return out;
}

std::string lastErrorLabel() {
    if (g_diagnostics.empty()) return "";
    const auto &d = g_diagnostics.back();
    return "line " + std::to_string(d.line) + ": near '" + d.near_text + "'";
}

namespace col {
    constexpr const char *RESET = "\033[0m";
    constexpr const char *BOLD  = "\033[1m";
    constexpr const char *RED   = "\033[1;31m";
    constexpr const char *GREEN = "\033[1;32m";
    constexpr const char *MAGENTA = "\033[1;35m";
}

bool useColor(FILE *f) {
    return isatty(fileno(f)) != 0;
}

void loadSourceLines(const std::string &path) {
    std::ifstream f(path);
    std::string line;
    while (std::getline(f, line)) g_sourceLines.push_back(line);
}

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

void printDiagnostic(std::ostream &out, const std::string &sourceFile,
                             const Diagnostic &d, bool color) {
    std::string label = d.kind; /* "Syntax error" / "Lexical error" */
    if (!label.empty()) label[0] = static_cast<char>(std::tolower(label[0]));

    bool isWarning = d.kind.find("warning") != std::string::npos;
    const std::string &file = sourceFile;
    int shownLine = d.line;
    if (color) {
        out << col::BOLD << file << ":" << shownLine << ":" << d.column << ": "
            << col::RESET << (isWarning ? col::MAGENTA : col::RED) << label << ": " << col::RESET
            << col::BOLD << d.message << col::RESET << "\n";
    } else {
        out << file << ":" << shownLine << ":" << d.column << ": "
            << label << ": " << d.message << "\n";
    }

    if (d.line >= 1 && d.line <= static_cast<int>(g_sourceLines.size())) {
        const std::string &srcLine = g_sourceLines[d.line - 1];
        std::string lineNumStr = std::to_string(shownLine);
        std::string gutter(lineNumStr.size(), ' ');

        out << " " << lineNumStr << " | " << srcLine << "\n";

        std::string indent;
        for (int i = 1; i < d.column; ++i) {
            bool wasTab = (i - 1 < static_cast<int>(srcLine.size())) && srcLine[i - 1] == '\t';
            indent += wasTab ? '\t' : ' ';
        }

        out << " " << gutter << " | " << indent;
        if (color) out << (isWarning ? col::MAGENTA : col::RED) << col::BOLD << "^" << col::RESET << "\n";
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
