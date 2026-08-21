#ifndef DIAGNOSTICS_H
#define DIAGNOSTICS_H

#include <string>
#include <vector>

struct Diagnostic
{
    int line;
    std::string lexeme;
    std::string message;
};

extern std::vector<Diagnostic> diagnostics;

void reportError(
    int line,
    const std::string &lexeme,
    const std::string &message);

bool hasErrors();

#endif