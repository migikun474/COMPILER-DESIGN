#ifndef LOGGER_H
#define LOGGER_H

#include "diagnostics.h"
#include <string>

void writeLexerLog(
    const std::string &sourceFile,
    const std::vector<Diagnostic> &diagnostics);

#endif