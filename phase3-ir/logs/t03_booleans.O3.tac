============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 234 -> 70 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          234 -> 70   (70% fewer)

   constants folded                       45
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           57
   temporaries merged away                 3
   dead instructions removed              28
   jumps removed or redirected            52
   unreachable instructions removed       53
   propagated across blocks               30
   dead assignments removed               26
   calls inlined                           7
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         0

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

============================================================================
 FUNCTION yes()        (link name _Z3yesv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    100     calls = calls int+ 1
    101     return 1

============================================================================
 FUNCTION no()        (link name _Z2nov)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    102     calls = calls int+ 1
    103     return 0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 0 temporaries, frame 208 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   e                local   int                             4      16
   f                local   int                             4      20
   r                local   int                             4      24
   x                local   int                             4      28
   z                local   double                          8      32
   ch               local   char                            1      40
   p                local   int *                           4      44
   flag             local   bool                            1      48
   both             local   bool                            1      49
   big              local   unsigned int                    4      52
   minus            local   int                             4      56
   (37 temporaries no longer used after optimization not shown)

 Code: 66 instruction(s)

    104       param "%d\n"
    105       param 1
    106       call printf, 2
    107       param "%d %d %d %d %d %d\n"
    108       param 0
    109       param 1
    110       param 1
    111       param 0
    112       param 1
    113       param 0
    114       call printf, 7
    115       calls = 0
    116       calls = 1
    117       param "calls after &&: %d\n"
    118       param 1
    119       call printf, 2
    120       calls = 0
    121       calls = 1
    122       param "or taken\n"
    123       call printf, 1
    124       param "calls after ||: %d\n"
    125       param calls
    126       call printf, 2
    127       calls = 0
    128       calls = 1
    129       calls = 2
    130       calls = 3
    131       param "%d %d\n"
    132       param 1
    133       param 3
    134       call printf, 3
    135       x = 0
    136       param "%d %d %d %d %d\n"
    137       param 1
    138       param 0
    139       param 1
    140       param 1
    141       param 1
    142       call printf, 6
    143       param "double is true\n"
    144       call printf, 1
    145       param "null pointer is false\n"
    146       call printf, 1
    147       param "%d\n"
    148       param 2
    149       call printf, 2
    150       param "%d %d\n"
    151       param 1
    152       param 0
    153       call printf, 3
    154       param "%d %d\n"
    155       param 1
    156       param 1
    157       call printf, 3
    158  L1:  if x int>= 3 goto L2
    159       if x int== 2 goto L2
    160       x = x int+ 1
    161       goto L1
    162  L2:  param "%d\n"
    163       param x
    164       call printf, 2
    165       param "%d %d\n"
    166       param 1
    167       param 1
    168       call printf, 3
    169       return 1


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      4    4    8  
   yes                function      int (void)                 -           5    -    3  _Z3yesv; defined
   no                 function      int (void)                 -           6    -    4  _Z2nov; defined
   main               function      int (void)                 -           8    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       9    4    9  a.1
   b                  variable      int                        local       9    4    8  b.2
   c                  variable      int                        local       9    4    5  c.3
   d                  variable      int                        local       9    4    2  d.4
   e                  variable      int                        local       9    4    1  e.5
   f                  variable      int                        local       9    4    1  f.6
   r                  variable      int                        local      10    4   10  r.7
   x                  variable      int                        local      25    4    6  x.8
   z                  variable      double                     local      26    8    2  z.9
   ch                 variable      char                       local      27    1    2  ch.10
   p                  variable      int *                      local      28    4    2  p.11
   flag               variable      bool                       local      36    1    2  flag.12
   both               variable      bool                       local      37    1    1  both.13
   big                variable      unsigned int               local      41    4    1  big.14
   minus              variable      int                        local      42    4    1  minus.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
