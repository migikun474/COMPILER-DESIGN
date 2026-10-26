============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 248 -> 183 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          248 -> 183   (26% fewer)

   constants folded                       32
   algebraic simplifications               8
   common subexpressions                  10
   copies / constants forwarded           92
   temporaries merged away                 8
   dead instructions removed              45
   jumps removed or redirected            10
   unreachable instructions removed        4

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

 Code: 8 instruction(s)

    109     a = 11
    110     b = 16
    111     c = 1
    112     d = 14.0
    113     u = 205032704
    114     ch = -115
    115     b = 17
    116     return 632

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

 Code: 23 instruction(s)

    117     t1 = x int* y
    118     t2 = t1 int+ 3
    119     a = t2
    120     b = t2
    121     t5 = x int+ y
    122     t7 = t5 int* t5
    123     c = t7
    124     d = t5
    125     t9 = x int<< 3
    126     t11 = t9 int+ y
    127     t14 = t11 int+ x
    128     e = t14
    129     t16 = x int+ 1
    130     x = t16
    131     t17 = t16 int* y
    132     t18 = t17 int+ 3
    133     f = t18
    134     t19 = t2 int+ t2
    135     t20 = t19 int+ t7
    136     t21 = t20 int+ t5
    137     t22 = t21 int+ t14
    138     t23 = t22 int+ t18
    139     return t23

============================================================================
 FUNCTION aliasing()        (link name _Z8aliasingv)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 23 temporaries, frame 192 bytes

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
   (10 temporaries no longer used after optimization not shown)

 Code: 48 instruction(s)

    140     x = 5
    141     y = 7
    142     t1 = &x
    143     p = t1
    144     t2 = x int+ 7
    145     a = t2
    146     *t1 = 20
    147     t3 = x int+ y
    148     b = t3
    149     t4 = &y
    150     param t4
    151     param 1
    152     call set(int *, int), 2
    153     t5 = x int+ y
    154     c = t5
    155     r = t1
    156     t7 = *t1
    157     t8 = t7 int+ 1
    158     *t1 = t8
    159     t9 = x int+ y
    160     d = t9
    161     param t1
    162     call twice(int &), 1
    163     arr[0] = 1
    164     arr[4] = 2
    165     arr[8] = 3
    166     i = 1
    167     t12 = arr[4]
    168     t15 = t12 int+ t12
    169     e = t15
    170     arr[4] = 9
    171     f = 18
    172     t21 = &arr
    173     q = t21
    174     t22 = t21 ptr+ 8
    175     *t22 = 4
    176     t23 = t3 int<< 1
    177     t24 = t2 int+ t23
    178     t25 = t5 int* 3
    179     t26 = t24 int+ t25
    180     t27 = t9 int* 5
    181     t28 = t26 int+ t27
    182     t29 = t28 int+ t15
    183     t30 = t29 int+ 18
    184     t31 = t30 int+ x
    185     t32 = arr[8]
    186     t33 = t31 int+ t32
    187     return t33

============================================================================
 FUNCTION globals()        (link name _Z7globalsv)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 8 temporaries, frame 68 bytes

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
   t10              temp    int                             4      60
   t11              temp    int                             4      64
   (3 temporaries no longer used after optimization not shown)

 Code: 17 instruction(s)

    188     t1 = g int+ 1
    189     a = t1
    190     b = t1
    191     call bump(), 0
    192     t3 = g int+ 1
    193     c = t3
    194     g = 2
    195     d = 3
    196     v = 3
    197     e = 6
    198     t6 = t1 int+ t1
    199     t7 = t6 int+ t3
    200     t8 = t7 int+ 3
    201     t9 = t8 int+ 6
    202     t10 = call bump(), 0
    203     t11 = t9 int+ t10
    204     return t11

============================================================================
 FUNCTION flow(int)        (link name _Z4flowi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 2 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   k                local   int                             4      12
   t2               temp    int                             4      20
   t7               temp    int                             4      40
   (7 temporaries no longer used after optimization not shown)

 Code: 24 instruction(s)

    205        s = 0
    206        i = 0
    207  L1:   if i int>= n goto L5
    208        k = n int<< 1
    209        t2 = i int% 2
    210        if t2 int!= 0 goto L2
    211        s = s int+ k
    212        goto L3
    213  L2:   s = s int- 1
    214  L3:   if s int<= 1000 goto L4
    215        return -1
    216  L4:   i = i int+ 1
    217        goto L1
    218  L5:   t7 = n
    219        goto L9
    220  L6:   s = s int+ 1
    221  L7:   s = s int+ 2
    222        goto L10
    223  L8:   s = 0
    224        goto L10
    225  L9:   if t7 int== 3 goto L6
    226        if t7 int== 4 goto L7
    227        goto L8
    228  L10:  return s

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

    229        if b int!= 0 goto L11
    230        t1 = 0
    231        goto L12
    232  L11:  t1 = a int/ b
    233  L12:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 9 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   total            local   int                             4       0
   zero             local   int                             4       4
   x                local   double                          8       8
   y                local   double                          8      16
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   (3 temporaries no longer used after optimization not shown)

 Code: 49 instruction(s)

    234     t1 = call fold(), 0
    235     param "%d\n"
    236     param t1
    237     call printf, 2
    238     param 3
    239     param 4
    240     t2 = call common(int, int), 2
    241     param "%d\n"
    242     param t2
    243     call printf, 2
    244     t3 = call aliasing(), 0
    245     param "%d\n"
    246     param t3
    247     call printf, 2
    248     t4 = call globals(), 0
    249     total = t4
    250     param "%d %d\n"
    251     param t4
    252     param g
    253     call printf, 3
    254     param 3
    255     t5 = call flow(int), 1
    256     param 4
    257     t6 = call flow(int), 1
    258     param 5
    259     t7 = call flow(int), 1
    260     param "%d %d %d\n"
    261     param t5
    262     param t6
    263     param t7
    264     call printf, 4
    265     zero = 0
    266     param 1
    267     param 0
    268     t8 = call divide(int, int), 2
    269     param 9
    270     param 3
    271     t9 = call divide(int, int), 2
    272     param "%d %d\n"
    273     param t8
    274     param t9
    275     call printf, 3
    276     x = 0.0
    277     y = 0.0
    278     param "%.1f %.1f\n"
    279     param 0.0
    280     param 0.0
    281     call printf, 3
    282     return 0


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
