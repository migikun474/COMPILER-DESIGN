============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : /tmp/claude-1000/-home-amirishetty-parsing-stage/d23148d6-4d07-435e-b985-82ec05b0bcc4/scratchpad/dfe.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 13 -> 9 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           13 -> 9   (30% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            3
   temporaries merged away                 0
   dead instructions removed               2
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                0
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   unreachable functions removed           2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   t1               temp    int *                           4       4
   t4               temp    int                             4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    100     t1 = &x
    101     param "%d"
    102     param t1
    103     call scanf, 2
    104     t4 = x int* x
    105     param "%d\n"
    106     param t4
    107     call printf, 2
    108     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   sq                 function      int (int)                  -           1    -    1  _Z2sqi; defined
   unused             function      int (int)                  -           2    -    0  _Z6unusedi; defined
   main               function      int (void)                 -           3    -    0  defined

 scope: global > sq()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       1    4    2  v.1

 scope: global > unused()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       2    4    1  v.2

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local       3    4    2  x.3

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
