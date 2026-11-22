============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : /tmp/claude-1000/-home-amirishetty-parsing-stage/d23148d6-4d07-435e-b985-82ec05b0bcc4/scratchpad/audit/self.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 17 -> 11 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           17 -> 11   (35% fewer)

   constants folded                        1
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            2
   temporaries merged away                 2
   dead instructions removed               0
   jumps removed or redirected             1
   unreachable instructions removed        1
   propagated across blocks                0
   dead assignments removed                2
   calls inlined                           0
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   z                local   int                             4       8
   t1               temp    int *                           4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    100     t1 = &x
    101     param "%d"
    102     param t1
    103     call scanf, 2
    104     z = x int+ 1
    105     y = z int+ 1
    106     param "%d %d\n"
    107     param z
    108     param y
    109     call printf, 3
    110     return 0


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
   x                  variable      int                        local       2    4    2  x.1
   y                  variable      int                        local       2    4    3  y.2
   z                  variable      int                        local       4    4    4  z.3

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
