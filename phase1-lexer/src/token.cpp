#include "token.h"

std::vector<Token> tokens;

void addToken(
    TokenType type,
    const std::string &lexeme)
{
    tokens.push_back(
    {
        lexeme,
        type
    });
}
