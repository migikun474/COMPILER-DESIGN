#include "diagnostics.h"

std::vector<Diagnostic> diagnostics;

void reportError(
    int line,
    const std::string &lexeme,
    const std::string &message)
{
    diagnostics.push_back(
    {
        line,
        lexeme,
        message
    });
}

bool hasErrors()
{
    return !diagnostics.empty();
}