#ifndef TOKEN_H
#define TOKEN_H

#include <string>
#include <vector>

#include "token_type.hpp"

struct Token
{
    std::string lexeme;
    TokenType type;
};

extern std::vector<Token> tokens;

void addToken(
    TokenType type,
    const std::string &lexeme);

#endif
