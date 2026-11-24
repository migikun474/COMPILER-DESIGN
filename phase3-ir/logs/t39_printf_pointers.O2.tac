============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t39_printf_pointers.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 40 -> 28 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           40 -> 28   (30% fewer)

   constants folded                        4
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           23
   temporaries merged away                 0
   dead instructions removed               4
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                8

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 0 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   none             local   int *                           4       0
   small            local   int *                           4       4
   mid              local   char *                          4       8
   big              local   unsigned int                    4      12
   top              local   double *                        4      16
   one              local   void *                          4      20
   p                local   int *                           4      24
   c                local   char *                          4      28
   (4 temporaries no longer used after optimization not shown)

 Code: 28 instruction(s)

    100     param "[%p] [%p] [%p] [%p] [%p]\n"
    101     param 0
    102     param 16
    103     param 305441741
    104     param 3735928559
    105     param 1
    106     call printf, 6
    107     param "[%12p] [%-12p] [%3p]\n"
    108     param 305441741
    109     param 305441741
    110     param 305441741
    111     call printf, 4
    112     param "[%10p] [%-10p] [%2p]\n"
    113     param 0
    114     param 0
    115     param 0
    116     call printf, 4
    117     param "%p and %d and %p\n"
    118     param 16
    119     param 42
    120     param 255
    121     call printf, 4
    122     param "%p %p %d\n"
    123     param 24
    124     param 305441744
    125     param 2
    126     call printf, 4
    127     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           6    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   none               variable      int *                      local       7    4    4  none.1
   small              variable      int *                      local       8    4    4  small.2
   mid                variable      char *                     local       9    4    5  mid.3
   big                variable      unsigned int               local      10    4    1  big.4
   top                variable      double *                   local      11    4    1  top.5
   one                variable      void *                     local      12    4    1  one.6
   p                  variable      int *                      local      17    4    2  p.7
   c                  variable      char *                     local      18    4    1  c.8

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
