#include "token/token_log.hpp"

#include <cstdio>

#include "diagnostics/diagnostics.hpp"

std::vector<TokenRecord> g_tokens;

int addTokenRecord(const std::string &lexeme, const std::string &category) {
    g_tokens.push_back({lexeme, category, g_currentLine, g_currentColumn});
    return static_cast<int>(g_tokens.size()) - 1;
}

void setCategory(int idx, const std::string &category) {
    if (idx >= 0 && idx < static_cast<int>(g_tokens.size())) {
        g_tokens[idx].category = category;
    }
}


/* Shared by both the stdout report and the on-disk log, so the two
   never drift apart. */
void printTokenTable(std::ostream &out) {
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
