============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 234 -> 84 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          234 -> 84   (64% fewer)

   constants folded                       33
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           42
   temporaries merged away                 3
   dead instructions removed              20
   jumps removed or redirected            49
   unreachable instructions removed       46
   propagated across blocks               30
   dead assignments removed               26

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

 Symbol table: 15 parameter(s)/local(s), 8 temporaries, frame 208 bytes

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
   t8               temp    int                             4      88
   t9               temp    int                             4      92
   t10              temp    int                             4      96
   t11              temp    int                             4     100
   t12              temp    int                             4     104
   t13              temp    int                             4     108
   t14              temp    int                             4     112
   t15              temp    int                             4     116
   (29 temporaries no longer used after optimization not shown)

 Code: 80 instruction(s)

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
    116       t8 = call no(), 0
    117       if t8 int== 0 goto L1
    118       t9 = call yes(), 0
    119       if t9 int== 0 goto L1
    120       param "no\n"
    121       call printf, 1
    122  L1:  param "calls after &&: %d\n"
    123       param calls
    124       call printf, 2
    125       calls = 0
    126       t10 = call yes(), 0
    127       if t10 int!= 0 goto L2
    128       t11 = call no(), 0
    129       if t11 int== 0 goto L3
    130  L2:  param "or taken\n"
    131       call printf, 1
    132  L3:  param "calls after ||: %d\n"
    133       param calls
    134       call printf, 2
    135       calls = 0
    136       t13 = call no(), 0
    137       if t13 int!= 0 goto L4
    138       t14 = call yes(), 0
    139       if t14 int== 0 goto L5
    140  L4:  t15 = call no(), 0
    141       if t15 int== 0 goto L6
    142  L5:  t12 = 0
    143       goto L7
    144  L6:  t12 = 1
    145  L7:  param "%d %d\n"
    146       param t12
    147       param calls
    148       call printf, 3
    149       x = 0
    150       param "%d %d %d %d %d\n"
    151       param 1
    152       param 0
    153       param 1
    154       param 1
    155       param 1
    156       call printf, 6
    157       param "double is true\n"
    158       call printf, 1
    159       param "null pointer is false\n"
    160       call printf, 1
    161       param "%d\n"
    162       param 2
    163       call printf, 2
    164       param "%d %d\n"
    165       param 1
    166       param 0
    167       call printf, 3
    168       param "%d %d\n"
    169       param 1
    170       param 1
    171       call printf, 3
    172  L8:  if x int>= 3 goto L9
    173       if x int== 2 goto L9
    174       x = x int+ 1
    175       goto L8
    176  L9:  param "%d\n"
    177       param x
    178       call printf, 2
    179       param "%d %d\n"
    180       param 1
    181       param 1
    182       call printf, 3
    183       return 1


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
