============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t29_registers.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 314 -> 288 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          314 -> 288   (8% fewer)

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
   loops unrolled                          7
   unreachable functions removed           4

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

 Code: 58 instruction(s)

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
    141       if t int>= 3 goto L3
    142       t13 = a int* b
    143       t14 = c int* d
    144       t15 = t13 int+ t14
    145       t16 = e int* f
    146       t17 = t15 int+ t16
    147       t18 = g int* h
    148       t19 = t17 int+ t18
    149       t20 = i int* j
    150       t21 = t19 int+ t20
    151       t22 = k int* l
    152       t23 = t21 int+ t22
    153       t24 = t23 int+ t
    154       s = s int+ t24
    155       t = t int+ 1
    156       goto L2
    157  L3:  t27 = s int+ a
    158       t28 = t27 int+ b
    159       t29 = t28 int+ c
    160       t30 = t29 int+ d
    161       t31 = t30 int+ e
    162       t32 = t31 int+ f
    163       t33 = t32 int+ g
    164       t34 = t33 int+ h
    165       t35 = t34 int+ i
    166       t36 = t35 int+ j
    167       t37 = t36 int+ k
    168       t38 = t37 int+ l
    169       return t38

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

    170     t1 = a int+ 1
    171     t13 = b int<< 1
    172     t3 = c int- 1
    173     t17 = t1 int* 100
    174     t18 = t13 int* 10
    175     t19 = t17 int+ t18
    176     t20 = t19 int+ t3
    177     t22 = a int<< 1
    178     t26 = t13 int<< 1
    179     t28 = c int<< 1
    180     t9 = t28 int+ t1
    181     t32 = t22 int* 100
    182     t33 = t26 int* 10
    183     t34 = t32 int+ t33
    184     t35 = t34 int+ t9
    185     t11 = t20 int+ t35
    186     return t11

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

    187        c = 0
    188        u = 0
    189        h = 0
    190        any = 0
    191        signs = 0
    192        i = 0
    193  L4:   t1 = s ptr+ i
    194        t2 = *t1
    195        if t2 char== 0 goto L10
    196        t3 = chartoint c
    197        t5 = *t1
    198        t6 = chartoint t5
    199        t7 = t3 int+ t6
    200        t8 = inttochar t7
    201        c = t8
    202        t9 = uchartoint u
    203        t13 = t9 int+ t6
    204        u = inttouchar t13
    205        t15 = shorttoint h
    206        t16 = t15 int* 31
    207        t20 = t16 int+ t6
    208        h = inttoshort t20
    209        t22 = chartoint t8
    210        if t22 int>= 0 goto L5
    211        signs = signs int+ 1
    212  L5:   if any bool!= 0 goto L6
    213        t26 = *t1
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

 Code: 27 instruction(s)

    239        total = 0.0
    240        small = 0.5
    241        i = 0
    242  L11:  if i int>= n goto L12
    243        t7 = total double+ 22.25
    244        t18 = t7 double/ 2.0
    245        t9 = floattodouble small
    246        t10 = t18 double+ t9
    247        total = t10
    248        small = small float* 1.5
    249        if t10 double> 1e+03 goto L12
    250        i = i int+ 1
    251        if i int>= n goto L12
    252        t7 = total double+ 22.25
    253        t18 = t7 double/ 2.0
    254        t9 = floattodouble small
    255        t10 = t18 double+ t9
    256        total = t10
    257        small = small float* 1.5
    258        if t10 double> 1e+03 goto L12
    259        i = i int+ 1
    260        goto L11
    261  L12:  t13 = total double+ 1.5
    262        t14 = t13 double+ 16.5
    263        t15 = floattodouble small
    264        t16 = t14 double+ t15
    265        return t16

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

 Code: 26 instruction(s)

    266        before = n int* 3
    267        sum = 0
    268        i = 0
    269  L13:  if i int>= n goto L18
    270        t2 = i int* before
    271        t3 = t2 int% 7
    272        t4 = sum int+ t3
    273        if t4 int<= 50 goto L14
    274        sum = t4 int- before
    275        goto L15
    276  L14:  t11 = i int<< 1
    277        sum = t4 int+ t11
    278  L15:  i = i int+ 1
    279        if i int>= n goto L18
    280        t2 = i int* before
    281        t3 = t2 int% 7
    282        t4 = sum int+ t3
    283        if t4 int<= 50 goto L16
    284        sum = t4 int- before
    285        goto L17
    286  L16:  t11 = i int<< 1
    287        sum = t4 int+ t11
    288  L17:  i = i int+ 1
    289        goto L13
    290  L18:  t9 = sum int+ before
    291        return t9

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

 Code: 96 instruction(s)

    292        param 5
    293        t1 = call depth(int), 1
    294        param 3
    295        t2 = call many(int), 1
    296        param "%d %d\n"
    297        param t1
    298        param t2
    299        call printf, 3
    300        param 1
    301        param 2
    302        param 3
    303        t3 = call arguments(int, int, int), 3
    304        param 4
    305        param 0
    306        param 9
    307        t4 = call arguments(int, int, int), 3
    308        param "%d %d\n"
    309        param t3
    310        param t4
    311        call printf, 3
    312        param "register allocation"
    313        t5 = call characters(const char *), 1
    314        param "zzzzzzzzzzzzzzzzzzzz"
    315        t6 = call characters(const char *), 1
    316        param "%d %d\n"
    317        param t5
    318        param t6
    319        call printf, 3
    320        param 0
    321        t7 = call numbers(int), 1
    322        param 3
    323        t8 = call numbers(int), 1
    324        param 40
    325        t9 = call numbers(int), 1
    326        param "%.4f %.4f %.4f\n"
    327        param t7
    328        param t8
    329        param t9
    330        call printf, 4
    331        t16 = 0
    332        t17 = 0
    333        t18 = -1
    334  L19:  if t16 int>= 0 goto L20
    335        t19 = t16 int* t16
    336        t17 = t17 int+ t19
    337        t18 = t16
    338        t16 = t16 int+ 1
    339        if t16 int>= 0 goto L20
    340        t19 = t16 int* t16
    341        t17 = t17 int+ t19
    342        t18 = t16
    343        t16 = t16 int+ 1
    344        goto L19
    345  L20:  t20 = t17 int* 10
    346        t10 = t20 int+ t18
    347        t23 = 0
    348        t24 = 0
    349        t25 = -1
    350  L21:  if t23 int>= 5 goto L22
    351        t26 = t23 int* t23
    352        t24 = t24 int+ t26
    353        t25 = t23
    354        t23 = t23 int+ 1
    355        if t23 int>= 5 goto L22
    356        t26 = t23 int* t23
    357        t24 = t24 int+ t26
    358        t25 = t23
    359        t23 = t23 int+ 1
    360        goto L21
    361  L22:  t27 = t24 int* 10
    362        t28 = t27 int+ t25
    363        param 9
    364        t12 = call mixed(int), 1
    365        param "%d %d %d\n"
    366        param t10
    367        param t28
    368        param t12
    369        call printf, 4
    370        t30 = 0
    371        t31 = 0
    372        t32 = -1
    373  L23:  if t30 int>= 3 goto L24
    374        t33 = t30 int* t30
    375        t31 = t31 int+ t33
    376        t32 = t30
    377        t30 = t30 int+ 1
    378        if t30 int>= 3 goto L24
    379        t33 = t30 int* t30
    380        t31 = t31 int+ t33
    381        t32 = t30
    382        t30 = t30 int+ 1
    383        goto L23
    384  L24:  t34 = t31 int* 10
    385        t35 = t34 int+ t32
    386        t14 = t35 int% 100
    387        return t14


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   depth              function      int (int)                  -           6    -    2  _Z5depthi; defined
   many               function      int (int)                  -          13    -    1  _Z4manyi; defined
   three              function      int (int, int, int)        -          21    -    2  _Z5threeiii; defined
   twice              function      int (int)                  -          22    -    6  _Z5twicei; defined
   arguments          function      int (int, int, int)        -          23    -    2  _Z9argumentsiii; defined
   characters         function      int (const char *)         -          30    -    2  _Z10charactersPKc; defined
   half               function      double (double)            -          47    -    1  _Z4halfd; defined
   numbers            function      double (int)               -          48    -    3  _Z7numbersi; defined
   jumps              function      int (int)                  -          60    -    3  _Z5jumpsi; defined
   mixed              function      int (int)                  -          72    -    1  _Z5mixedi; defined
   main               function      int (void)                 -          84    -    0  defined

 scope: global > depth()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       6    4    4  n.1
   a                  variable      int                        local       7    4    2  a.2
   b                  variable      int                        local       7    4    2  b.3
   c                  variable      int                        local       7    4    1  c.4
   below              variable      int                        local       9    4    1  below.5

 scope: global > many()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      13    4   12  x.6
   a                  variable      int                        local      14    4    2  a.7
   b                  variable      int                        local      14    4    2  b.8
   c                  variable      int                        local      14    4    2  c.9
   d                  variable      int                        local      14    4    2  d.10
   e                  variable      int                        local      14    4    2  e.11
   f                  variable      int                        local      14    4    2  f.12
   g                  variable      int                        local      15    4    2  g.13
   h                  variable      int                        local      15    4    2  h.14
   i                  variable      int                        local      15    4    2  i.15
   j                  variable      int                        local      15    4    2  j.16
   k                  variable      int                        local      15    4    2  k.17
   l                  variable      int                        local      15    4    2  l.18
   s                  variable      int                        local      16    4    2  s.19

 scope: global > many() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local      17    4    3  t.20

 scope: global > three()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int                        param      21    4    1  p.21
   q                  parameter     int                        param      21    4    1  q.22
   r                  parameter     int                        param      21    4    1  r.23

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      22    4    1  v.24

 scope: global > arguments()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      23    4    2  a.25
   b                  parameter     int                        param      23    4    2  b.26
   c                  parameter     int                        param      23    4    2  c.27
   x                  variable      int                        local      24    4    2  x.28
   y                  variable      int                        local      25    4    1  y.29
   z                  variable      int                        local      26    4    1  z.30

 scope: global > characters()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      30    4    5  s.31
   c                  variable      char                       local      31    1    5  c.32
   u                  variable      unsigned char              local      32    1    3  u.33
   h                  variable      short                      local      33    2    3  h.34
   any                variable      bool                       local      34    1    3  any.35
   signs              variable      int                        local      35    4    2  signs.36
   same               variable      unsigned char              local      43    1    1  same.38

 scope: global > characters() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      36    4    6  i.37

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param      47    8    1  v.39

 scope: global > numbers()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      48    4    1  n.40
   a                  variable      double                     local      49    8    2  a.41
   b                  variable      double                     local      49    8    1  b.42
   c                  variable      double                     local      49    8    1  c.43
   d                  variable      double                     local      49    8    1  d.44
   e                  variable      double                     local      49    8    1  e.45
   f                  variable      double                     local      49    8    1  f.46
   g                  variable      double                     local      49    8    2  g.47
   total              variable      double                     local      49    8    5  total.48
   small              variable      float                      local      50    4    4  small.49

 scope: global > numbers() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      51    4    2  i.50

 scope: global > jumps()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      60    4    1  n.51
   done               label         -                          -          68    -    1  _Z5jumpsi.done
   top                label         -                          -          62    -    1  _Z5jumpsi.top
   i                  variable      int                        local      61    4    5  i.52
   s                  variable      int                        local      61    4    2  s.53
   last               variable      int                        local      61    4    2  last.54

 scope: global > mixed()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      72    4    2  n.55
   before             variable      int                        local      73    4    3  before.56
   sum                variable      int                        local      73    4    5  sum.57
   after              variable      int                        local      80    4    1  after.60

 scope: global > mixed() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      74    4    4  i.58

 scope: global > mixed() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   inside             variable      int                        local      75    4    1  inside.59

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
