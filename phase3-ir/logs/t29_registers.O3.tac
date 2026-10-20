============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t29_registers.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 314 -> 260 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          314 -> 260   (17% fewer)

   constants folded                        7
   algebraic simplifications               3
   common subexpressions                   7
   copies / constants forwarded           54
   temporaries merged away                28
   dead instructions removed              39
   jumps removed or redirected            13
   unreachable instructions removed        2
   propagated across blocks               17
   dead assignments removed               22
   calls inlined                          12
   tail calls turned into jumps            0
   common subexpressions across blocks      2
   instructions moved out of loops        11

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
    126       t13 = a int* b
    127       t14 = c int* d
    128       t15 = t13 int+ t14
    129       t16 = e int* f
    130       t17 = t15 int+ t16
    131       t18 = g int* h
    132       t19 = t17 int+ t18
    133       t20 = i int* j
    134       t21 = t19 int+ t20
    135       t22 = k int* l
    136       t23 = t21 int+ t22
    137  L2:  if t int>= 3 goto L3
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

 Symbol table: 6 parameter(s)/local(s), 16 temporaries, frame 164 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   c                param   int                             4       8
   x                local   int                             4      12
   y                local   int                             4      16
   z                local   int                             4      20
   t1               temp    int                             4      24
   t3               temp    int                             4      32
   t9               temp    int                             4      56
   t11              temp    int                             4      64
   t13              temp    int                             4      72
   t17              temp    int                             4      88
   t18              temp    int                             4      92
   t19              temp    int                             4      96
   t20              temp    int                             4     100
   t22              temp    int                             4     108
   t26              temp    int                             4     124
   t28              temp    int                             4     132
   t32              temp    int                             4     148
   t33              temp    int                             4     152
   t34              temp    int                             4     156
   t35              temp    int                             4     160
   (19 temporaries no longer used after optimization not shown)

 Code: 17 instruction(s)

    162     t1 = a int+ 1
    163     t13 = b int<< 1
    164     t3 = c int- 1
    165     t17 = t1 int* 100
    166     t18 = t13 int* 10
    167     t19 = t17 int+ t18
    168     t20 = t19 int+ t3
    169     t22 = a int<< 1
    170     t26 = t13 int<< 1
    171     t28 = c int<< 1
    172     t9 = t28 int+ t1
    173     t32 = t22 int* 100
    174     t33 = t26 int* 10
    175     t34 = t32 int+ t33
    176     t35 = t34 int+ t9
    177     t11 = t20 int+ t35
    178     return t11

============================================================================
 FUNCTION characters(const char *)        (link name _Z10charactersPKc)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 29 temporaries, frame 188 bytes

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
   (12 temporaries no longer used after optimization not shown)

 Code: 52 instruction(s)

    179        c = 0
    180        u = 0
    181        h = 0
    182        any = 0
    183        signs = 0
    184        i = 0
    185  L4:   t1 = s ptr+ i
    186        t2 = *t1
    187        if t2 char== 0 goto L10
    188        t3 = chartoint c
    189        t5 = *t1
    190        t6 = chartoint t5
    191        t7 = t3 int+ t6
    192        t8 = inttochar t7
    193        c = t8
    194        t9 = uchartoint u
    195        t13 = t9 int+ t6
    196        u = inttouchar t13
    197        t15 = shorttoint h
    198        t16 = t15 int* 31
    199        t20 = t16 int+ t6
    200        h = inttoshort t20
    201        t22 = chartoint t8
    202        if t22 int>= 0 goto L5
    203        signs = signs int+ 1
    204  L5:   if any bool!= 0 goto L6
    205        t26 = *t1
    206        t27 = chartoint t26
    207        if t27 int== 122 goto L6
    208        t24 = 0
    209        goto L7
    210  L6:   t24 = 1
    211  L7:   if t24 int!= 0 goto L8
    212        t28 = 0
    213        goto L9
    214  L8:   t28 = 1
    215  L9:   any = t28
    216        i = i int+ 1
    217        goto L4
    218  L10:  t30 = chartoint c
    219        t31 = uchartoint u
    220        t32 = t31 int<< 1
    221        t33 = t30 int+ t32
    222        t34 = shorttoint h
    223        t35 = t33 int+ t34
    224        t36 = signs int* 1000
    225        t37 = t35 int+ t36
    226        t38 = booltoint any
    227        t39 = t37 int+ t38
    228        t40 = uchartoint c
    229        t41 = t39 int+ t40
    230        return t41

============================================================================
 FUNCTION half(double)        (link name _Z4halfd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   double                          8       0
   t1               temp    double                          8       8

 Code: 2 instruction(s)

    231     t1 = v double/ 2.0
    232     return t1

============================================================================
 FUNCTION numbers(int)        (link name _Z7numbersi)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 8 temporaries, frame 216 bytes

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
   t9               temp    double                          8     144
   t10              temp    double                          8     152
   t13              temp    double                          8     168
   t14              temp    double                          8     176
   t15              temp    double                          8     184
   t16              temp    double                          8     192
   t18              temp    double                          8     208
   (10 temporaries no longer used after optimization not shown)

 Code: 18 instruction(s)

    233        total = 0.0
    234        small = 0.5
    235        i = 0
    236  L11:  if i int>= n goto L12
    237        t7 = total double+ 22.25
    238        t18 = t7 double/ 2.0
    239        t9 = floattodouble small
    240        t10 = t18 double+ t9
    241        total = t10
    242        small = small float* 1.5
    243        if t10 double> 1e+03 goto L12
    244        i = i int+ 1
    245        goto L11
    246  L12:  t13 = total double+ 1.5
    247        t14 = t13 double+ 16.5
    248        t15 = floattodouble small
    249        t16 = t14 double+ t15
    250        return t16

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

    251        i = 0
    252        s = 0
    253        last = -1
    254  L13:  if i int>= n goto L14
    255        t2 = i int* i
    256        s = s int+ t2
    257        last = i
    258        i = i int+ 1
    259        goto L13
    260  L14:  t5 = s int* 10
    261        t6 = t5 int+ last
    262        return t6

============================================================================
 FUNCTION mixed(int)        (link name _Z5mixedi)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 5 temporaries, frame 68 bytes

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
   t9               temp    int                             4      56
   t11              temp    int                             4      64
   (6 temporaries no longer used after optimization not shown)

 Code: 16 instruction(s)

    263        before = n int* 3
    264        sum = 0
    265        i = 0
    266  L15:  if i int>= n goto L18
    267        t2 = i int* before
    268        t3 = t2 int% 7
    269        t4 = sum int+ t3
    270        if t4 int<= 50 goto L16
    271        sum = t4 int- before
    272        goto L17
    273  L16:  t11 = i int<< 1
    274        sum = t4 int+ t11
    275  L17:  i = i int+ 1
    276        goto L15
    277  L18:  t9 = sum int+ before
    278        return t9

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 29 temporaries, frame 152 bytes

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
   t12              temp    int                             4      56
   t14              temp    int                             4      64
   t16              temp    int                             4      72
   t17              temp    int                             4      76
   t18              temp    int                             4      80
   t19              temp    int                             4      84
   t20              temp    int                             4      88
   t23              temp    int                             4     100
   t24              temp    int                             4     104
   t25              temp    int                             4     108
   t26              temp    int                             4     112
   t27              temp    int                             4     116
   t28              temp    int                             4     120
   t30              temp    int                             4     128
   t31              temp    int                             4     132
   t32              temp    int                             4     136
   t33              temp    int                             4     140
   t34              temp    int                             4     144
   t35              temp    int                             4     148
   (6 temporaries no longer used after optimization not shown)

 Code: 81 instruction(s)

    279        param 5
    280        t1 = call depth(int), 1
    281        param 3
    282        t2 = call many(int), 1
    283        param "%d %d\n"
    284        param t1
    285        param t2
    286        call printf, 3
    287        param 1
    288        param 2
    289        param 3
    290        t3 = call arguments(int, int, int), 3
    291        param 4
    292        param 0
    293        param 9
    294        t4 = call arguments(int, int, int), 3
    295        param "%d %d\n"
    296        param t3
    297        param t4
    298        call printf, 3
    299        param "register allocation"
    300        t5 = call characters(const char *), 1
    301        param "zzzzzzzzzzzzzzzzzzzz"
    302        t6 = call characters(const char *), 1
    303        param "%d %d\n"
    304        param t5
    305        param t6
    306        call printf, 3
    307        param 0
    308        t7 = call numbers(int), 1
    309        param 3
    310        t8 = call numbers(int), 1
    311        param 40
    312        t9 = call numbers(int), 1
    313        param "%.4f %.4f %.4f\n"
    314        param t7
    315        param t8
    316        param t9
    317        call printf, 4
    318        t16 = 0
    319        t17 = 0
    320        t18 = -1
    321  L19:  if t16 int>= 0 goto L20
    322        t19 = t16 int* t16
    323        t17 = t17 int+ t19
    324        t18 = t16
    325        t16 = t16 int+ 1
    326        goto L19
    327  L20:  t20 = t17 int* 10
    328        t10 = t20 int+ t18
    329        t23 = 0
    330        t24 = 0
    331        t25 = -1
    332  L21:  if t23 int>= 5 goto L22
    333        t26 = t23 int* t23
    334        t24 = t24 int+ t26
    335        t25 = t23
    336        t23 = t23 int+ 1
    337        goto L21
    338  L22:  t27 = t24 int* 10
    339        t28 = t27 int+ t25
    340        param 9
    341        t12 = call mixed(int), 1
    342        param "%d %d %d\n"
    343        param t10
    344        param t28
    345        param t12
    346        call printf, 4
    347        t30 = 0
    348        t31 = 0
    349        t32 = -1
    350  L23:  if t30 int>= 3 goto L24
    351        t33 = t30 int* t30
    352        t31 = t31 int+ t33
    353        t32 = t30
    354        t30 = t30 int+ 1
    355        goto L23
    356  L24:  t34 = t31 int* 10
    357        t35 = t34 int+ t32
    358        t14 = t35 int% 100
    359        return t14


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
