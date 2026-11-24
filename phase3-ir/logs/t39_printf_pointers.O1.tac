============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t39_printf_pointers.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 40 -> 36 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           40 -> 36   (10% fewer)

   calls inlined                           0
   constants folded                        4
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           23
   temporaries merged away                 0
   dead instructions removed               4
   jumps removed or redirected             0
   unreachable instructions removed        0

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

 Code: 36 instruction(s)

    100     none = 0
    101     small = 16
    102     mid = 305441741
    103     big = 3735928559
    104     top = 3735928559
    105     one = 1
    106     param "[%p] [%p] [%p] [%p] [%p]\n"
    107     param 0
    108     param 16
    109     param 305441741
    110     param 3735928559
    111     param 1
    112     call printf, 6
    113     param "[%12p] [%-12p] [%3p]\n"
    114     param 305441741
    115     param 305441741
    116     param 305441741
    117     call printf, 4
    118     param "[%10p] [%-10p] [%2p]\n"
    119     param 0
    120     param 0
    121     param 0
    122     call printf, 4
    123     param "%p and %d and %p\n"
    124     param 16
    125     param 42
    126     param 255
    127     call printf, 4
    128     p = 24
    129     c = 305441744
    130     param "%p %p %d\n"
    131     param 24
    132     param 305441744
    133     param 2
    134     call printf, 4
    135     return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

[(nil)] [0x10] [0x1234abcd] [0xdeadbeef] [0x1]
[  0x1234abcd] [0x1234abcd  ] [0x1234abcd]
[     (nil)] [(nil)     ] [(nil)]
0x10 and 42 and 0xff
0x18 0x1234abd0 2

   exit code 0, 36 instructions executed
