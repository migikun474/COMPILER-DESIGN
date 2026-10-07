#ifndef OPT_H
#define OPT_H

/* =====================================================================
   TAC OPTIMIZER
   ---------------------------------------------------------------------
   -O1: local optimizations. Each function is cut into basic blocks
   (Dragon Book 8.4) and every block is optimized on its own by value
   numbering -- the hash-table form of the block's DAG (8.5, 6.1.2): a
   value number is a DAG node, and two instructions that get the same
   number compute the same value. That one mechanism gives constant
   folding, algebraic simplification, copy propagation and common
   subexpression elimination. Around it: dead temporaries are removed,
   and jumps are cleaned up (jump to the next instruction, jump to a
   jump, a conditional jump over a jump, unreachable code).

   Nothing here may change what a program prints or returns: the test
   suite runs every program before and after and compares.
   ===================================================================== */

#include <ostream>

#include "tac.h"

namespace tac {

struct OptStats {
    int before = 0, after = 0; /* instructions in the program */
    int folded = 0;            /* constant operations computed at compile time */
    int simplified = 0;        /* x + 0, x * 1, x * 8 -> x << 3, ... */
    int common = 0;            /* common subexpressions reused */
    int copies = 0;            /* operands replaced by an earlier name or a constant */
    int coalesced = 0;         /* `t = a + b ; x = t` written as `x = a + b` */
    int dead = 0;              /* instructions whose result was never used */
    int jumps = 0;             /* jumps removed, redirected or inverted */
    int unreachable = 0;       /* instructions no path reaches */
};

OptStats optimize(Program &program, int level);
void printStats(const OptStats &s, std::ostream &out);

} // namespace tac

#endif
