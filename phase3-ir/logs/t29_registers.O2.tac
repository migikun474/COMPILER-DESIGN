============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t29_registers.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 314 -> 243 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          314 -> 243   (22% fewer)

   constants folded                        7
   algebraic simplifications               3
   common subexpressions                   6
   copies / constants forwarded           27
   temporaries merged away                27
   dead instructions removed              13
   jumps removed or redirected            13
   unreachable instructions removed        2
   propagated across blocks               13
   dead assignments removed               18

============================================================================
 FUNCTION depth(int)        (link name _Z5depthi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 7 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   a                local   int                             4       4
   b                local   int                             4       8
   c                local   int                             4      12
   below            local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   (1 temporary no longer used after optimization not shown)

 Code: 12 instruction(s)

    100       t1 = n int<< 1
    101       t2 = n int+ 7
    102       c = t1 int- t2
    103       if n int!= 0 goto L1
    104       return 1
    105  L1:  t4 = n int- 1
    106       param t4
    107       t5 = call depth(int), 1
    108       t6 = t1 int+ t2
    109       t7 = t6 int+ c
    110       t8 = t7 int+ t5
    111       return t8

============================================================================
 FUNCTION many(int)        (link name _Z4manyi)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 24 temporaries, frame 212 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   a                local   int                             4       4
   b                local   int                             4       8
   c                local   int                             4      12
   d                local   int                             4      16
   e                local   int                             4      20
   f                local   int                             4      24
   g                local   int                             4      28
   h                local   int                             4      32
   i                local   int                             4      36
   j                local   int                             4      40
   k                local   int                             4      44
   l                local   int                             4      48
   s                local   int                             4      52
   t                local   int                             4      56
   t13              temp    int                             4     108
   t14              temp    int                             4     112
   t15              temp    int                             4     116
   t16              temp    int                             4     120
   t17              temp    int                             4     124
   t18              temp    int                             4     128
   t19              temp    int                             4     132
   t20              temp    int                             4     136
   t21              temp    int                             4     140
   t22              temp    int                             4     144
   t23              temp    int                             4     148
   t24              temp    int                             4     152
   t27              temp    int                             4     164
   t28              temp    int                             4     168
   t29              temp    int                             4     172
   t30              temp    int                             4     176
   t31              temp    int                             4     180
   t32              temp    int                             4     184
   t33              temp    int                             4     188
   t34              temp    int                             4     192
   t35              temp    int                             4     196
   t36              temp    int                             4     200
   t37              temp    int                             4     204
   t38              temp    int                             4     208
   (14 temporaries no longer used after optimization not shown)

 Code: 43 instruction(s)

    112       a = x int+ 1
    113       b = x int+ 2
    114       c = x int+ 3
    115       d = x int+ 4
    116       e = x int+ 5
    117       f = x int+ 6
    118       g = x int+ 7
    119       h = x int+ 8
    120       i = x int+ 9
    121       j = x int+ 10
    122       k = x int+ 11
    123       l = x int+ 12
    124       s = 0
    125       t = 0
    126  L2:  if t int>= 3 goto L3
    127       t13 = a int* b
    128       t14 = c int* d
    129       t15 = t13 int+ t14
    130       t16 = e int* f
    131       t17 = t15 int+ t16
    132       t18 = g int* h
    133       t19 = t17 int+ t18
    134       t20 = i int* j
    135       t21 = t19 int+ t20
    136       t22 = k int* l
    137       t23 = t21 int+ t22
    138       t24 = t23 int+ t
    139       s = s int+ t24
    140       t = t int+ 1
    141       goto L2
    142  L3:  t27 = s int+ a
    143       t28 = t27 int+ b
    144       t29 = t28 int+ c
    145       t30 = t29 int+ d
    146       t31 = t30 int+ e
    147       t32 = t31 int+ f
    148       t33 = t32 int+ g
    149       t34 = t33 int+ h
    150       t35 = t34 int+ i
    151       t36 = t35 int+ j
    152       t37 = t36 int+ k
    153       t38 = t37 int+ l
    154       return t38

============================================================================
 FUNCTION three(int, int, int)        (link name _Z5threeiii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int                             4       0
   q                param   int                             4       4
   r                param   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24

 Code: 5 instruction(s)

    155     t1 = p int* 100
    156     t2 = q int* 10
    157     t3 = t1 int+ t2
    158     t4 = t3 int+ r
    159     return t4

============================================================================
 FUNCTION twice(int)        (link name _Z5twicei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    160     t1 = v int<< 1
    161     return t1

============================================================================
 FUNCTION arguments(int, int, int)        (link name _Z9argumentsiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 11 temporaries, frame 68 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   c                param   int                             4       8
   x                local   int                             4      12
   y                local   int                             4      16
   z                local   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   t10              temp    int                             4      60
   t11              temp    int                             4      64

 Code: 23 instruction(s)

    162     t1 = a int+ 1
    163     param b
    164     t2 = call twice(int), 1
    165     t3 = c int- 1
    166     param t1
    167     param t2
    168     param t3
    169     t4 = call three(int, int, int), 3
    170     param a
    171     t5 = call twice(int), 1
    172     param b
    173     t6 = call twice(int), 1
    174     param t6
    175     t7 = call twice(int), 1
    176     param c
    177     t8 = call twice(int), 1
    178     t9 = t8 int+ t1
    179     param t5
    180     param t7
    181     param t9
    182     t10 = call three(int, int, int), 3
    183     t11 = t4 int+ t10
    184     return t11

============================================================================
 FUNCTION characters(const char *)        (link name _Z10charactersPKc)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 31 temporaries, frame 188 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   c                local   char                            1       4
   u                local   unsigned char                   1       5
   h                local   short                           2       6
   any              local   bool                            1       8
   signs            local   int                             4      12
   i                local   int                             4      16
   same             local   unsigned char                   1      20
   t1               temp    const char *                    4      24
   t2               temp    char                            1      28
   t3               temp    int                             4      32
   t4               temp    const char *                    4      36
   t5               temp    char                            1      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    char                            1      52
   t9               temp    int                             4      56
   t13              temp    int                             4      72
   t15              temp    int                             4      80
   t16              temp    int                             4      84
   t20              temp    int                             4     100
   t22              temp    int                             4     108
   t24              temp    int                             4     116
   t25              temp    const char *                    4     120
   t26              temp    char                            1     124
   t27              temp    int                             4     128
   t28              temp    bool                            1     132
   t30              temp    int                             4     140
   t31              temp    int                             4     144
   t32              temp    int                             4     148
   t33              temp    int                             4     152
   t34              temp    int                             4     156
   t35              temp    int                             4     160
   t36              temp    int                             4     164
   t37              temp    int                             4     168
   t38              temp    int                             4     172
   t39              temp    int                             4     176
   t40              temp    int                             4     180
   t41              temp    int                             4     184
   (10 temporaries no longer used after optimization not shown)

 Code: 54 instruction(s)

    185        c = 0
    186        u = 0
    187        h = 0
    188        any = 0
    189        signs = 0
    190        i = 0
    191  L4:   t1 = s ptr+ i
    192        t2 = *t1
    193        if t2 char== 0 goto L10
    194        t3 = chartoint c
    195        t4 = s ptr+ i
    196        t5 = *t4
    197        t6 = chartoint t5
    198        t7 = t3 int+ t6
    199        t8 = inttochar t7
    200        c = t8
    201        t9 = uchartoint u
    202        t13 = t9 int+ t6
    203        u = inttouchar t13
    204        t15 = shorttoint h
    205        t16 = t15 int* 31
    206        t20 = t16 int+ t6
    207        h = inttoshort t20
    208        t22 = chartoint t8
    209        if t22 int>= 0 goto L5
    210        signs = signs int+ 1
    211  L5:   if any bool!= 0 goto L6
    212        t25 = s ptr+ i
    213        t26 = *t25
    214        t27 = chartoint t26
    215        if t27 int== 122 goto L6
    216        t24 = 0
    217        goto L7
    218  L6:   t24 = 1
    219  L7:   if t24 int!= 0 goto L8
    220        t28 = 0
    221        goto L9
    222  L8:   t28 = 1
    223  L9:   any = t28
    224        i = i int+ 1
    225        goto L4
    226  L10:  t30 = chartoint c
    227        t31 = uchartoint u
    228        t32 = t31 int<< 1
    229        t33 = t30 int+ t32
    230        t34 = shorttoint h
    231        t35 = t33 int+ t34
    232        t36 = signs int* 1000
    233        t37 = t35 int+ t36
    234        t38 = booltoint any
    235        t39 = t37 int+ t38
    236        t40 = uchartoint c
    237        t41 = t39 int+ t40
    238        return t41

============================================================================
 FUNCTION half(double)        (link name _Z4halfd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   double                          8       0
   t1               temp    double                          8       8

 Code: 2 instruction(s)

    239     t1 = v double/ 2.0
    240     return t1

============================================================================
 FUNCTION numbers(int)        (link name _Z7numbersi)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 8 temporaries, frame 200 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   a                local   double                          8       8
   b                local   double                          8      16
   c                local   double                          8      24
   d                local   double                          8      32
   e                local   double                          8      40
   f                local   double                          8      48
   g                local   double                          8      56
   total            local   double                          8      64
   small            local   float                           4      72
   i                local   int                             4      76
   t7               temp    double                          8     128
   t8               temp    double                          8     136
   t9               temp    double                          8     144
   t10              temp    double                          8     152
   t13              temp    double                          8     168
   t14              temp    double                          8     176
   t15              temp    double                          8     184
   t16              temp    double                          8     192
   (8 temporaries no longer used after optimization not shown)

 Code: 19 instruction(s)

    241        total = 0.0
    242        small = 0.5
    243        i = 0
    244  L11:  if i int>= n goto L12
    245        t7 = total double+ 22.25
    246        param t7
    247        t8 = call half(double), 1
    248        t9 = floattodouble small
    249        t10 = t8 double+ t9
    250        total = t10
    251        small = small float* 1.5
    252        if t10 double> 1e+03 goto L12
    253        i = i int+ 1
    254        goto L11
    255  L12:  t13 = total double+ 1.5
    256        t14 = t13 double+ 16.5
    257        t15 = floattodouble small
    258        t16 = t14 double+ t15
    259        return t16

============================================================================
 FUNCTION jumps(int)        (link name _Z5jumpsi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   i                local   int                             4       4
   s                local   int                             4       8
   last             local   int                             4      12
   t2               temp    int                             4      20
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   (3 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    260        i = 0
    261        s = 0
    262        last = -1
    263  L13:  if i int>= n goto L14
    264        t2 = i int* i
    265        s = s int+ t2
    266        last = i
    267        i = i int+ 1
    268        goto L13
    269  L14:  t5 = s int* 10
    270        t6 = t5 int+ last
    271        return t6

============================================================================
 FUNCTION mixed(int)        (link name _Z5mixedi)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 5 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   before           local   int                             4       4
   sum              local   int                             4       8
   i                local   int                             4      12
   inside           local   int                             4      16
   after            local   int                             4      20
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t6               temp    int                             4      44
   t9               temp    int                             4      56
   (4 temporaries no longer used after optimization not shown)

 Code: 17 instruction(s)

    272        before = n int* 3
    273        sum = 0
    274        i = 0
    275  L15:  if i int>= n goto L18
    276        t2 = i int* before
    277        t3 = t2 int% 7
    278        t4 = sum int+ t3
    279        if t4 int<= 50 goto L16
    280        sum = t4 int- before
    281        goto L17
    282  L16:  param i
    283        t6 = call twice(int), 1
    284        sum = t4 int+ t6
    285  L17:  i = i int+ 1
    286        goto L15
    287  L18:  t9 = sum int+ before
    288        return t9

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 14 temporaries, frame 68 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0
   t2               temp    int                             4       4
   t3               temp    int                             4       8
   t4               temp    int                             4      12
   t5               temp    int                             4      16
   t6               temp    int                             4      20
   t7               temp    double                          8      24
   t8               temp    double                          8      32
   t9               temp    double                          8      40
   t10              temp    int                             4      48
   t11              temp    int                             4      52
   t12              temp    int                             4      56
   t13              temp    int                             4      60
   t14              temp    int                             4      64

 Code: 54 instruction(s)

    289     param 5
    290     t1 = call depth(int), 1
    291     param 3
    292     t2 = call many(int), 1
    293     param "%d %d\n"
    294     param t1
    295     param t2
    296     call printf, 3
    297     param 1
    298     param 2
    299     param 3
    300     t3 = call arguments(int, int, int), 3
    301     param 4
    302     param 0
    303     param 9
    304     t4 = call arguments(int, int, int), 3
    305     param "%d %d\n"
    306     param t3
    307     param t4
    308     call printf, 3
    309     param "register allocation"
    310     t5 = call characters(const char *), 1
    311     param "zzzzzzzzzzzzzzzzzzzz"
    312     t6 = call characters(const char *), 1
    313     param "%d %d\n"
    314     param t5
    315     param t6
    316     call printf, 3
    317     param 0
    318     t7 = call numbers(int), 1
    319     param 3
    320     t8 = call numbers(int), 1
    321     param 40
    322     t9 = call numbers(int), 1
    323     param "%.4f %.4f %.4f\n"
    324     param t7
    325     param t8
    326     param t9
    327     call printf, 4
    328     param 0
    329     t10 = call jumps(int), 1
    330     param 5
    331     t11 = call jumps(int), 1
    332     param 9
    333     t12 = call mixed(int), 1
    334     param "%d %d %d\n"
    335     param t10
    336     param t11
    337     param t12
    338     call printf, 4
    339     param 3
    340     t13 = call jumps(int), 1
    341     t14 = t13 int% 100
    342     return t14


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   depth              function      int (int)                  -           7    -    2  _Z5depthi; defined
   many               function      int (int)                  -          14    -    1  _Z4manyi; defined
   three              function      int (int, int, int)        -          22    -    2  _Z5threeiii; defined
   twice              function      int (int)                  -          23    -    6  _Z5twicei; defined
   arguments          function      int (int, int, int)        -          24    -    2  _Z9argumentsiii; defined
   characters         function      int (const char *)         -          31    -    2  _Z10charactersPKc; defined
   half               function      double (double)            -          48    -    1  _Z4halfd; defined
   numbers            function      double (int)               -          49    -    3  _Z7numbersi; defined
   jumps              function      int (int)                  -          61    -    3  _Z5jumpsi; defined
   mixed              function      int (int)                  -          73    -    1  _Z5mixedi; defined
   main               function      int (void)                 -          85    -    0  defined

 scope: global > depth()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       7    4    4  n.1
   a                  variable      int                        local       8    4    2  a.2
   b                  variable      int                        local       8    4    2  b.3
   c                  variable      int                        local       8    4    1  c.4
   below              variable      int                        local      10    4    1  below.5

 scope: global > many()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      14    4   12  x.6
   a                  variable      int                        local      15    4    2  a.7
   b                  variable      int                        local      15    4    2  b.8
   c                  variable      int                        local      15    4    2  c.9
   d                  variable      int                        local      15    4    2  d.10
   e                  variable      int                        local      15    4    2  e.11
   f                  variable      int                        local      15    4    2  f.12
   g                  variable      int                        local      16    4    2  g.13
   h                  variable      int                        local      16    4    2  h.14
   i                  variable      int                        local      16    4    2  i.15
   j                  variable      int                        local      16    4    2  j.16
   k                  variable      int                        local      16    4    2  k.17
   l                  variable      int                        local      16    4    2  l.18
   s                  variable      int                        local      17    4    2  s.19

 scope: global > many() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local      18    4    3  t.20

 scope: global > three()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int                        param      22    4    1  p.21
   q                  parameter     int                        param      22    4    1  q.22
   r                  parameter     int                        param      22    4    1  r.23

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      23    4    1  v.24

 scope: global > arguments()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      24    4    2  a.25
   b                  parameter     int                        param      24    4    2  b.26
   c                  parameter     int                        param      24    4    2  c.27
   x                  variable      int                        local      25    4    2  x.28
   y                  variable      int                        local      26    4    1  y.29
   z                  variable      int                        local      27    4    1  z.30

 scope: global > characters()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      31    4    5  s.31
   c                  variable      char                       local      32    1    5  c.32
   u                  variable      unsigned char              local      33    1    3  u.33
   h                  variable      short                      local      34    2    3  h.34
   any                variable      bool                       local      35    1    3  any.35
   signs              variable      int                        local      36    4    2  signs.36
   same               variable      unsigned char              local      44    1    1  same.38

 scope: global > characters() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      37    4    6  i.37

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param      48    8    1  v.39

 scope: global > numbers()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      49    4    1  n.40
   a                  variable      double                     local      50    8    2  a.41
   b                  variable      double                     local      50    8    1  b.42
   c                  variable      double                     local      50    8    1  c.43
   d                  variable      double                     local      50    8    1  d.44
   e                  variable      double                     local      50    8    1  e.45
   f                  variable      double                     local      50    8    1  f.46
   g                  variable      double                     local      50    8    2  g.47
   total              variable      double                     local      50    8    5  total.48
   small              variable      float                      local      51    4    4  small.49

 scope: global > numbers() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      52    4    2  i.50

 scope: global > jumps()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      61    4    1  n.51
   done               label         -                          -          69    -    1  _Z5jumpsi.done
   top                label         -                          -          63    -    1  _Z5jumpsi.top
   i                  variable      int                        local      62    4    5  i.52
   s                  variable      int                        local      62    4    2  s.53
   last               variable      int                        local      62    4    2  last.54

 scope: global > mixed()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      73    4    2  n.55
   before             variable      int                        local      74    4    3  before.56
   sum                variable      int                        local      74    4    5  sum.57
   after              variable      int                        local      81    4    1  after.60

 scope: global > mixed() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      75    4    4  i.58

 scope: global > mixed() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   inside             variable      int                        local      76    4    1  inside.59

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
