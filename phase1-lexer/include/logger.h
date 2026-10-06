#ifndef LOGGER_H
#define LOGGER_H

#include <string>

#include "diagnostics/diagnostics.hpp"

/* writes logs/<file>.log from the shared diagnostics list */
void writeLexerLog(const std::string &sourceFile);

#endif
