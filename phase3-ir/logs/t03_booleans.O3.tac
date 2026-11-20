============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 234 -> 69 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          234 -> 69   (70% fewer)

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
   loops unrolled                          1
   unreachable functions removed           2

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

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

 Code: 69 instruction(s)

    100       param "%d\n"
    101       param 1
    102       call printf, 2
    103       param "%d %d %d %d %d %d\n"
    104       param 0
    105       param 1
    106       param 1
    107       param 0
    108       param 1
    109       param 0
    110       call printf, 7
    111       calls = 0
    112       calls = 1
    113       param "calls after &&: %d\n"
    114       param 1
    115       call printf, 2
    116       calls = 0
    117       calls = 1
    118       param "or taken\n"
    119       call printf, 1
    120       param "calls after ||: %d\n"
    121       param calls
    122       call printf, 2
    123       calls = 0
    124       calls = 1
    125       calls = 2
    126       calls = 3
    127       param "%d %d\n"
    128       param 1
    129       param 3
    130       call printf, 3
    131       x = 0
    132       param "%d %d %d %d %d\n"
    133       param 1
    134       param 0
    135       param 1
    136       param 1
    137       param 1
    138       call printf, 6
    139       param "double is true\n"
    140       call printf, 1
    141       param "null pointer is false\n"
    142       call printf, 1
    143       param "%d\n"
    144       param 2
    145       call printf, 2
    146       param "%d %d\n"
    147       param 1
    148       param 0
    149       call printf, 3
    150       param "%d %d\n"
    151       param 1
    152       param 1
    153       call printf, 3
    154  L1:  if x int>= 3 goto L2
    155       if x int== 2 goto L2
    156       x = x int+ 1
    157       if x int>= 3 goto L2
    158       if x int== 2 goto L2
    159       x = x int+ 1
    160       goto L1
    161  L2:  param "%d\n"
    162       param x
    163       call printf, 2
    164       param "%d %d\n"
    165       param 1
    166       param 1
    167       call printf, 3
    168       return 1


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      3    4    8  
   yes                function      int (void)                 -           4    -    3  _Z3yesv; defined
   no                 function      int (void)                 -           5    -    4  _Z2nov; defined
   main               function      int (void)                 -           7    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       8    4    9  a.1
   b                  variable      int                        local       8    4    8  b.2
   c                  variable      int                        local       8    4    5  c.3
   d                  variable      int                        local       8    4    2  d.4
   e                  variable      int                        local       8    4    1  e.5
   f                  variable      int                        local       8    4    1  f.6
   r                  variable      int                        local       9    4   10  r.7
   x                  variable      int                        local      24    4    6  x.8
   z                  variable      double                     local      25    8    2  z.9
   ch                 variable      char                       local      26    1    2  ch.10
   p                  variable      int *                      local      27    4    2  p.11
   flag               variable      bool                       local      35    1    2  flag.12
   both               variable      bool                       local      36    1    1  both.13
   big                variable      unsigned int               local      40    4    1  big.14
   minus              variable      int                        local      41    4    1  minus.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
