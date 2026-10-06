#ifndef SHARED_TOKEN_LOG_HPP
#define SHARED_TOKEN_LOG_HPP

/* The token log: every token the scanner returned, in order, with the
   category the parser finally decided for it (an identifier's category
   is patched once its declaration is known -- `a -> INT`, `f ->
   PROCEDURE`). Parser actions refer to tokens by their index here, which
   is also how AST nodes and symbols recover exact source positions. */

#include <ostream>
#include <string>
#include <vector>

struct TokenRecord {
    std::string lexeme;
    std::string category;
    int line = 0;
    int column = 0;
};

extern std::vector<TokenRecord> g_tokens;

int addTokenRecord(const std::string &lexeme, const std::string &category);
void setCategory(int idx, const std::string &category);

/* the Token / Token_Type table phase 2 prints for a valid program */
void printTokenTable(std::ostream &out);

#endif
