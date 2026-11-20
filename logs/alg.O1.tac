============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : /tmp/claude-1000/-home-amirishetty-parsing-stage/d23148d6-4d07-435e-b985-82ec05b0bcc4/scratchpad/alg.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 22 -> 15 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           22 -> 15   (31% fewer)

   constants folded                        1
   algebraic simplifications               6
   common subexpressions                   0
   copies / constants forwarded           16
   temporaries merged away                 0
   dead instructions removed               7
   jumps removed or redirected             0
   unreachable instructions removed        0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   t1               temp    int *                           4       8
   t2               temp    int                             4      12
   (7 temporaries no longer used after optimization not shown)

 Code: 15 instruction(s)

    100     t1 = &x
    101     param "%d"
    102     param t1
    103     call scanf, 2
    104     t2 = x int+ 1
    105     y = t2
    106     param "%d %d %d %d %d %d\n"
    107     param 0
    108     param 0
    109     param t2
    110     param 0
    111     param -1
    112     param 0
    113     call printf, 7
    114     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           1    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local       1    4    2  x.1
   y                  variable      int                        local       1    4    9  y.2

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
