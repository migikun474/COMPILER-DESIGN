============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 248 -> 145 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          248 -> 145   (41% fewer)

   constants folded                       51
   algebraic simplifications               8
   common subexpressions                  11
   copies / constants forwarded          140
   temporaries merged away                 8
   dead instructions removed              79
   jumps removed or redirected            13
   unreachable instructions removed        8
   propagated across blocks                2
   dead assignments removed               35
   calls inlined                           9
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         1

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  1

 As three address code (initial values, in place before main runs):

    g = 1

============================================================================
 FUNCTION bump()        (link name _Z4bumpv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    100     t1 = g int+ 10
    101     g = t1
    102     return t1

============================================================================
 FUNCTION set(int *, int)        (link name _Z3setPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int *                           4       0
   v                param   int                             4       4

 Code: 2 instruction(s)

    103     *p = v
    104     return

============================================================================
 FUNCTION twice(int &)        (link name _Z5twiceRi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   int &                           4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    105     t1 = *r
    106     t2 = t1 int<< 1
    107     *r = t2
    108     return

============================================================================
 FUNCTION fold()        (link name _Z4foldv)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 0 temporaries, frame 128 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   double                          8      16
   u                local   unsigned int                    4      24
   ch               local   char                            1      28
   (21 temporaries no longer used after optimization not shown)

 Code: 1 instruction(s)

    109     return 632

============================================================================
 FUNCTION common(int, int)        (link name _Z6commonii)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 15 temporaries, frame 124 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   y                param   int                             4       4
   a                local   int                             4       8
   b                local   int                             4      12
   c                local   int                             4      16
   d                local   int                             4      20
   e                local   int                             4      24
   f                local   int                             4      28
   t1               temp    int                             4      32
   t2               temp    int                             4      36
   t5               temp    int                             4      48
   t7               temp    int                             4      56
   t9               temp    int                             4      64
   t11              temp    int                             4      72
   t14              temp    int                             4      84
   t16              temp    int                             4      92
   t17              temp    int                             4      96
   t18              temp    int                             4     100
   t19              temp    int                             4     104
   t20              temp    int                             4     108
   t21              temp    int                             4     112
   t22              temp    int                             4     116
   t23              temp    int                             4     120
   (8 temporaries no longer used after optimization not shown)

 Code: 16 instruction(s)

    110     t1 = x int* y
    111     t2 = t1 int+ 3
    112     t5 = x int+ y
    113     t7 = t5 int* t5
    114     t9 = x int<< 3
    115     t11 = t9 int+ y
    116     t14 = t11 int+ x
    117     t16 = x int+ 1
    118     t17 = t16 int* y
    119     t18 = t17 int+ 3
    120     t19 = t2 int+ t2
    121     t20 = t19 int+ t7
    122     t21 = t20 int+ t5
    123     t22 = t21 int+ t14
    124     t23 = t22 int+ t18
    125     return t23

============================================================================
 FUNCTION aliasing()        (link name _Z8aliasingv)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 24 temporaries, frame 212 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   p                local   int *                           4       8
   a                local   int                             4      12
   b                local   int                             4      16
   c                local   int                             4      20
   r                local   int &                           4      24
   d                local   int                             4      28
   arr              local   int[3]                         12      32
   i                local   int                             4      44
   e                local   int                             4      48
   f                local   int                             4      52
   q                local   int *                           4      56
   t1               temp    int *                           4      60
   t2               temp    int                             4      64
   t3               temp    int                             4      68
   t4               temp    int *                           4      72
   t5               temp    int                             4      76
   t7               temp    int                             4      84
   t8               temp    int                             4      88
   t9               temp    int                             4      92
   t12              temp    int                             4     104
   t15              temp    int                             4     116
   t21              temp    int *                           4     140
   t22              temp    int *                           4     144
   t23              temp    int                             4     148
   t24              temp    int                             4     152
   t25              temp    int                             4     156
   t26              temp    int                             4     160
   t27              temp    int                             4     164
   t28              temp    int                             4     168
   t29              temp    int                             4     172
   t30              temp    int                             4     176
   t31              temp    int                             4     180
   t32              temp    int                             4     184
   t33              temp    int                             4     188
   t38              temp    int                             4     208
   (14 temporaries no longer used after optimization not shown)

 Code: 36 instruction(s)

    126     x = 5
    127     y = 7
    128     t1 = &x
    129     t2 = x int+ 7
    130     *t1 = 20
    131     t3 = x int+ y
    132     t4 = &y
    133     *t4 = 1
    134     t5 = x int+ y
    135     t7 = *t1
    136     t8 = t7 int+ 1
    137     *t1 = t8
    138     t9 = x int+ y
    139     t38 = t8 int<< 1
    140     *t1 = t38
    141     arr[0] = 1
    142     arr[4] = 2
    143     arr[8] = 3
    144     t12 = arr[4]
    145     t15 = t12 int+ t12
    146     arr[4] = 9
    147     t21 = &arr
    148     t22 = t21 ptr+ 8
    149     *t22 = 4
    150     t23 = t3 int<< 1
    151     t24 = t2 int+ t23
    152     t25 = t5 int* 3
    153     t26 = t24 int+ t25
    154     t27 = t9 int* 5
    155     t28 = t26 int+ t27
    156     t29 = t28 int+ t15
    157     t30 = t29 int+ 18
    158     t31 = t30 int+ x
    159     t32 = arr[8]
    160     t33 = t31 int+ t32
    161     return t33

============================================================================
 FUNCTION globals()        (link name _Z7globalsv)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 8 temporaries, frame 76 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   v                local   int                             4      16
   e                local   int                             4      20
   t1               temp    int                             4      24
   t3               temp    int                             4      32
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   t11              temp    int                             4      64
   t12              temp    int                             4      68
   (5 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    162     t1 = g int+ 1
    163     t12 = g int+ 10
    164     g = t12
    165     t3 = t12 int+ 1
    166     g = 2
    167     t6 = t1 int+ t1
    168     t7 = t6 int+ t3
    169     t8 = t7 int+ 3
    170     t9 = t8 int+ 6
    171     g = 12
    172     t11 = t9 int+ 12
    173     return t11

============================================================================
 FUNCTION flow(int)        (link name _Z4flowi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 1 temporary, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   k                local   int                             4      12
   t2               temp    int                             4      20
   (8 temporaries no longer used after optimization not shown)

 Code: 22 instruction(s)

    174       s = 0
    175       i = 0
    176       k = n int<< 1
    177  L1:  if i int>= n goto L8
    178       t2 = i int% 2
    179       if t2 int!= 0 goto L2
    180       s = s int+ k
    181       goto L3
    182  L2:  s = s int- 1
    183  L3:  if s int<= 1000 goto L4
    184       return -1
    185  L4:  i = i int+ 1
    186       goto L1
    187  L5:  s = s int+ 1
    188  L6:  s = s int+ 2
    189       goto L9
    190  L7:  s = 0
    191       goto L9
    192  L8:  if n int== 3 goto L5
    193       if n int== 4 goto L6
    194       goto L7
    195  L9:  return s

============================================================================
 FUNCTION divide(int, int)        (link name _Z6divideii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t1               temp    int                             4       8
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    196        if b int!= 0 goto L10
    197        t1 = 0
    198        goto L11
    199  L10:  t1 = a int/ b
    200  L11:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 12 temporaries, frame 212 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   total            local   int                             4       0
   zero             local   int                             4       4
   x                local   double                          8       8
   y                local   double                          8      16
   t3               temp    int                             4      32
   t5               temp    int                             4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t30              temp    int                             4     156
   t31              temp    int                             4     160
   t32              temp    int                             4     164
   t33              temp    int                             4     168
   t34              temp    int                             4     172
   t35              temp    int                             4     176
   t36              temp    int                             4     180
   t37              temp    int                             4     184
   (31 temporaries no longer used after optimization not shown)

 Code: 44 instruction(s)

    201     param "%d\n"
    202     param 632
    203     call printf, 2
    204     param "%d\n"
    205     param 136
    206     call printf, 2
    207     t3 = call aliasing(), 0
    208     param "%d\n"
    209     param t3
    210     call printf, 2
    211     t30 = g int+ 1
    212     call bump(), 0
    213     t31 = g int+ 1
    214     g = 2
    215     t32 = t30 int+ t30
    216     t33 = t32 int+ t31
    217     t34 = t33 int+ 3
    218     t35 = t34 int+ 6
    219     t36 = call bump(), 0
    220     t37 = t35 int+ t36
    221     param "%d %d\n"
    222     param t37
    223     param g
    224     call printf, 3
    225     param 3
    226     t5 = call flow(int), 1
    227     param 4
    228     t6 = call flow(int), 1
    229     param 5
    230     t7 = call flow(int), 1
    231     param "%d %d %d\n"
    232     param t5
    233     param t6
    234     param t7
    235     call printf, 4
    236     param "%d %d\n"
    237     param 0
    238     param 3
    239     call printf, 3
    240     param "%.1f %.1f\n"
    241     param 0.0
    242     param 0.0
    243     call printf, 3
    244     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      6    4    9  
   bump               function      int (void)                 -           7    -    2  _Z4bumpv; defined
   set                function      void (int *, int)          -           8    -    1  _Z3setPii; defined
   twice              function      void (int &)               -           9    -    1  _Z5twiceRi; defined
   fold               function      int (void)                 -          11    -    1  _Z4foldv; defined
   common             function      int (int, int)             -          22    -    1  _Z6commonii; defined
   aliasing           function      int (void)                 -          31    -    1  _Z8aliasingv; defined
   globals            function      int (void)                 -          53    -    1  _Z7globalsv; defined
   flow               function      int (int)                  -          65    -    3  _Z4flowi; defined
   divide             function      int (int, int)             -          82    -    2  _Z6divideii; defined
   main               function      int (void)                 -          84    -    0  defined

 scope: global > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *                      param       8    4    1  p.1
   v                  parameter     int                        param       8    4    1  v.2

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param       9    4    2  r.3

 scope: global > fold()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      12    4    4  a.4
   b                  variable      int                        local      12    4    4  b.5
   c                  variable      int                        local      12    4    2  c.6
   d                  variable      double                     local      13    8    1  d.7
   u                  variable      unsigned int               local      14    4    1  u.8
   ch                 variable      char                       local      15    1    1  ch.9

 scope: global > common()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      22    4   10  x.10
   y                  parameter     int                        param      22    4    7  y.11
   a                  variable      int                        local      23    4    1  a.12
   b                  variable      int                        local      23    4    1  b.13
   c                  variable      int                        local      24    4    1  c.14
   d                  variable      int                        local      24    4    1  d.15
   e                  variable      int                        local      25    4    1  e.16
   f                  variable      int                        local      27    4    1  f.17

 scope: global > aliasing()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      32    4    8  x.18
   y                  variable      int                        local      32    4    5  y.19
   p                  variable      int *                      local      33    4    1  p.20
   a                  variable      int                        local      34    4    1  a.21
   b                  variable      int                        local      36    4    1  b.22
   c                  variable      int                        local      38    4    1  c.23
   r                  variable      int &                      local      39    4    2  r.24
   d                  variable      int                        local      41    4    1  d.25
   arr                variable      int[3]                     local      43   12    7  arr.26
   i                  variable      int                        local      44    4    4  i.27
   e                  variable      int                        local      45    4    1  e.28
   f                  variable      int                        local      47    4    1  f.29
   q                  variable      int *                      local      48    4    1  q.30

 scope: global > globals()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      54    4    1  a.31
   b                  variable      int                        local      55    4    1  b.32
   c                  variable      int                        local      57    4    1  c.33
   d                  variable      int                        local      59    4    1  d.34
   v                  variable      int                        local      60    4    2  v.35
   e                  variable      int                        local      61    4    1  e.36

 scope: global > flow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      65    4    3  n.37
   s                  variable      int                        local      66    4    9  s.38

 scope: global > flow() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      67    4    3  i.39

 scope: global > flow() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      68    4    1  k.40

 scope: global > divide()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      82    4    1  a.41
   b                  parameter     int                        param      82    4    2  b.42

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      88    4    1  total.43
   zero               variable      int                        local      91    4    1  zero.44
   x                  variable      double                     local      93    8    2  x.45
   y                  variable      double                     local      93    8    1  y.46

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
