#include "scanner_support.h"

#include <cctype>
#include <cstring>
#include <string>

#include "diagnostics/diagnostics.hpp" /* g_sourceLines */

bool g_afterTypeKeyword = false;
int g_bracketDepth = 0;
static int g_declaratorListDepth = -1; /* -1: not inside an init-declarator list */

void markDeclaratorList() { g_declaratorListDepth = g_bracketDepth; }
void endDeclaratorList() { g_declaratorListDepth = -1; }
bool inDeclaratorListAt(int bracketDepth) { return g_declaratorListDepth >= 0 && g_declaratorListDepth == bracketDepth; }

/* ---- bounded source lookahead (see scanner_support.h) ---- */
namespace {
class SourcePeek {
  public:
    SourcePeek(int line, int column) : line_(line - 1), col_(column - 1) {}

    /* the next token's text; numbers come back as "#num", string/char
       literals as "#str", end of input as "" */
    std::string next() {
        skipSpaceAndComments();
        if (line_ >= static_cast<int>(g_sourceLines.size())) return "";
        const std::string &l = g_sourceLines[line_];
        char c = l[col_];
        if (std::isalpha(static_cast<unsigned char>(c)) || c == '_') {
            size_t start = col_;
            while (col_ < static_cast<int>(l.size()) && (std::isalnum(static_cast<unsigned char>(l[col_])) || l[col_] == '_')) ++col_;
            return l.substr(start, col_ - start);
        }
        if (std::isdigit(static_cast<unsigned char>(c)) || (c == '.' && col_ + 1 < static_cast<int>(l.size()) &&
                                                            std::isdigit(static_cast<unsigned char>(l[col_ + 1])))) {
            while (col_ < static_cast<int>(l.size()) && (std::isalnum(static_cast<unsigned char>(l[col_])) || l[col_] == '.')) ++col_;
            return "#num";
        }
        if (c == '"' || c == '\'') {
            ++col_;
            while (col_ < static_cast<int>(l.size()) && l[col_] != c) col_ += (l[col_] == '\\') ? 2 : 1;
            ++col_;
            return "#str";
        }
        static const char *multi[] = {"<<=", ">>=", "...", "->", "::", "++", "--", "<<", ">>", "<=", ">=", "==", "!=",
                                      "&&", "||", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^="};
        for (const char *m : multi) {
            size_t n = std::strlen(m);
            if (l.compare(col_, n, m) == 0) {
                col_ += static_cast<int>(n);
                return m;
            }
        }
        ++col_;
        return std::string(1, c);
    }

  private:
    int line_, col_;
    void skipSpaceAndComments() {
        while (line_ < static_cast<int>(g_sourceLines.size())) {
            const std::string &l = g_sourceLines[line_];
            if (col_ >= static_cast<int>(l.size())) { ++line_; col_ = 0; continue; }
            if (std::isspace(static_cast<unsigned char>(l[col_]))) { ++col_; continue; }
            if (l.compare(col_, 2, "//") == 0) { ++line_; col_ = 0; continue; }
            if (l.compare(col_, 2, "/*") == 0) {
                col_ += 2;
                while (line_ < static_cast<int>(g_sourceLines.size())) {
                    size_t end = g_sourceLines[line_].find("*/", col_);
                    if (end != std::string::npos) { col_ = static_cast<int>(end) + 2; break; }
                    ++line_;
                    col_ = 0;
                }
                continue;
            }
            return;
        }
    }
};

/* skips to the token after the bracket matching the one just consumed */
std::string afterMatching(SourcePeek &p, int depth) {
    for (std::string t = p.next(); !t.empty(); t = p.next()) {
        if (t == "(" || t == "[" || t == "{") ++depth;
        else if (t == ")" || t == "]" || t == "}") {
            if (--depth == 0) return p.next();
        }
    }
    return "";
}
} // namespace

bool parenGroupIsExpression(int line, int column) {
    SourcePeek p(line, column);
    if (p.next() != "(") return false;
    std::string first = p.next();
    if (first == ")" ) return true;                       /* `T()` */
    if (first == "#num" || first == "#str") return true;  /* `T(4)` */
    static const char *exprOnly[] = {"this", "sizeof", "new", "delete", "true", "false", "printf", "scanf",
                                     "malloc", "calloc", "realloc", "va_arg"};
    for (const char *w : exprOnly) {
        if (first == w) return true;
    }
    bool declaratorStart = first == "*" || first == "&" || first == "(" || first == "::" ||
                           std::isalpha(static_cast<unsigned char>(first[0])) || first[0] == '_';
    if (!declaratorStart) return true;                    /* `T(-x)`, `T(!x)` */
    /* could be a declarator: decide by what follows the ')' */
    std::string after = afterMatching(p, first == "(" ? 2 : 1);
    static const char *declFollow[] = {";", ",", "=", "[", "(", ")", "{", ":", ""};
    for (const char *f : declFollow) {
        if (after == f) return false;
    }
    return true;                                          /* `T(a).x`, `T(a) + 1` */
}

bool abstractDeclaratorGroup(int line, int column) {
    SourcePeek p(line, column);
    std::string t = p.next();
    if (t != "*" && t != "&" && t != "(" && t != "[") return false;
    int depth = 1; /* the '(' the scanner just matched */
    for (; !t.empty(); t = p.next()) {
        if (t == "(") {
            ++depth;
        } else if (t == ")") {
            if (--depth == 0) return true;
        } else if (!(t == "*" || t == "&" || t == "[" || t == "]" || t == "#num" || t == "const" || t == "volatile")) {
            return false;
        }
    }
    return false;
}

