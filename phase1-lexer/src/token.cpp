#include "token.h"

std::vector<Token> tokens;

void addToken(
    const std::string &type,
    const std::string &lexeme)
{
    tokens.push_back(
    {
        lexeme,
        type
    });
}