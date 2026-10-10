#ifndef MIPS_H
#define MIPS_H

/* =====================================================================
   MIPS CODE GENERATION (for the SPIM simulator)
   ---------------------------------------------------------------------
   One TAC instruction becomes a short, fixed sequence of MIPS
   instructions: operands are loaded from memory into scratch registers,
   the operation is done, the result is stored back. Nothing lives in a
   register between two TAC instructions (no register allocation yet).

   Frame of a function (the stack grows downwards):

        arguments ...           8($fp), 12($fp), ...   pushed by the caller
        saved $ra               4($fp)
        saved $fp               0($fp)      <- $fp
        locals and temporaries  -4($fp), -8($fp), ...
                                            <- $sp

   Calls: every argument goes on the stack, first argument at the lowest
   address; the result comes back in $v0 ($v0/$v1 for long long, $f0 for
   float and double; a struct comes back as its address in $v0 and is
   copied at once). The caller removes the arguments.
   ===================================================================== */

#include <string>

#include "tac.h"

namespace mips {

/* the whole assembly file: data, code, then the run-time library.
   `optimize` turns on the machine-level improvements: registers for the
   most used names, constants inside instructions, a peephole pass. */
std::string generate(const tac::Program &program, const std::string &runtime, bool optimize);

} // namespace mips

#endif
