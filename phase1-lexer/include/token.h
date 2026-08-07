#ifndef TOKEN_H
#define TOKEN_H

#include <string>
#include <vector>

struct Token
{
    std::string lexeme;
    std::string type;
};

extern std::vector<Token> tokens;

void addToken(
    const std::string &type,
    const std::string &lexeme);

#endif