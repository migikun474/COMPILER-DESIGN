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

   -O2 adds two optimizations across basic blocks, each a data-flow
   analysis over the function's flow graph (Dragon Book 9.2):
     - global constant and copy propagation (forward; a fact holds at a
       block's entry only if it holds at the end of every predecessor);
     - dead assignment elimination (backward live-variable analysis:
       `x = ...` is removed when x is not read again on any path).
   After each, -O1 runs again on the result until nothing changes.

   -O3 adds, on top of -O2:
     - inlining of small functions (at most 16 instructions, not
       recursive, not variadic) and tail recursion turned into a jump;
     - common subexpressions across blocks (available expressions);
     - loop-invariant code motion (natural loops from dominators).

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
    int level = 1;
    int global = 0;            /* -O2: operands replaced using facts from other blocks */
    int deadAssignments = 0;   /* -O2: assignments to variables never read afterwards */
    int inlined = 0;           /* -O3: calls replaced by the callee's body */
    int tailCalls = 0;         /* -O3: `return f(...)` in f turned into a jump */
    int globalCommon = 0;      /* -O3: expressions reused from another block */
    int hoisted = 0;           /* -O3: instructions moved in front of a loop */
};

OptStats optimize(Program &program, int level);
void printStats(const OptStats &s, std::ostream &out);

} // namespace tac

#endif
