#ifndef INTERP_H
#define INTERP_H

/* =====================================================================
   TAC INTERPRETER
   ---------------------------------------------------------------------
   Executes a tac::Program directly, with the MIPS32 data model (4-byte
   int and pointers, the frame offsets of each function's symbol table,
   byte-addressed memory). It is the correctness check for the code
   generator and, later, for the optimizer: optimized and unoptimized
   TAC must print the same output and return the same exit code, and
   the count of executed instructions measures what an optimization
   gained.
   ===================================================================== */

#include <string>
#include <vector>

#include "tac.h"

namespace tac {

struct RunResult {
    int exitCode = 0;
    long long executed = 0; /* instructions executed */
    std::string output;     /* everything the program printed */
    std::string error;      /* a run-time error (invalid memory access, division by zero, ...) */
};

/* runs `main`; `input` is what scanf reads */
RunResult run(const Program &program, const std::vector<std::string> &args, const std::string &input);

} // namespace tac

#endif
