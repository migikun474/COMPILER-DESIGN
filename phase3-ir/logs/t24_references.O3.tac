============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t24_references.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 217 -> 199 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          217 -> 199   (8% fewer)

   constants folded                        6
   algebraic simplifications               7
   common subexpressions                  12
   copies / constants forwarded           75
   temporaries merged away                 1
   dead instructions removed              52
   jumps removed or redirected             3
   unreachable instructions removed        0
   propagated across blocks                5
   dead assignments removed               12
   calls inlined                          11
   tail calls turned into jumps            0
   common subexpressions across blocks      8
   instructions moved out of loops         0

============================================================================
 FUNCTION deposit(struct Account &, double)        (link name _Z7depositR7Accountd)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   struct Account &                4       0
   amount           param   double                          8       8
   t1               temp    struct Account *                4      16
   t2               temp    double                          8      24
   t3               temp    double                          8      32
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    100     t1 = a ptr+ 8
    101     t2 = *t1
    102     t3 = t2 double+ amount
    103     *t1 = t3
    104     return

============================================================================
 FUNCTION peek(const struct Account &)        (link name _Z4peekRK7Account)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   const struct Account &          4       0
   t1               temp    const struct Account *          4       4
   t2               temp    double                          8       8

 Code: 3 instruction(s)

    105     t1 = a ptr+ 8
    106     t2 = *t1
    107     return t2

============================================================================
 FUNCTION richer(struct Account &, struct Account &)        (link name _Z6richerR7AccountS0_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   struct Account &                4       0
   b                param   struct Account &                4       4
   t1               temp    struct Account *                4       8
   t2               temp    struct Account *                4      12
   t3               temp    double                          8      16
   t4               temp    struct Account *                4      24
   t5               temp    double                          8      32

 Code: 10 instruction(s)

    108       t2 = a ptr+ 8
    109       t3 = *t2
    110       t4 = b ptr+ 8
    111       t5 = *t4
    112       if t3 double>= t5 goto L1
    113       goto L2
    114  L1:  t1 = a
    115       goto L3
    116  L2:  t1 = b
    117  L3:  return t1

============================================================================
 FUNCTION minmax(const int *, int, int &, int &)        (link name _Z6minmaxPKiiRiS1_)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 9 temporaries, frame 84 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   values           param   const int *                     4       0
   n                param   int                             4       4
   lo               param   int &                           4       8
   hi               param   int &                           4      12
   i                local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    const int *                     4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t8               temp    int                             4      48
   t11              temp    int                             4      60
   t12              temp    int                             4      64
   t15              temp    int                             4      76
   (7 temporaries no longer used after optimization not shown)

 Code: 20 instruction(s)

    118       t1 = *values
    119       *hi = t1
    120       *lo = t1
    121       i = 1
    122  L4:  if i int>= n goto L7
    123       t2 = i int<< 2
    124       t3 = values ptr+ t2
    125       t4 = *t3
    126       t5 = *lo
    127       if t4 int>= t5 goto L5
    128       t8 = *t3
    129       *lo = t8
    130  L5:  t11 = *t3
    131       t12 = *hi
    132       if t11 int<= t12 goto L6
    133       t15 = *t3
    134       *hi = t15
    135  L6:  i = i int+ 1
    136       goto L4
    137  L7:  return

============================================================================
 FUNCTION advance(int *&, int)        (link name _Z7advanceRPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int *&                          4       0
   steps            param   int                             4       4
   t1               temp    int *                           4       8
   t2               temp    int                             4      12
   t3               temp    int *                           4      16

 Code: 5 instruction(s)

    138     t1 = *p
    139     t2 = steps int<< 2
    140     t3 = t1 ptr+ t2
    141     *p = t3
    142     return

============================================================================
 FUNCTION element(int *, int)        (link name _Z7elementPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   i                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int *                           4      12

 Code: 3 instruction(s)

    143     t1 = i int<< 2
    144     t2 = a ptr+ t1
    145     return t2

============================================================================
 FUNCTION scale(const int &, const double &)        (link name _Z5scaleRKiRKd)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   const int &                     4       0
   factor           param   const double &                  4       4
   t1               temp    int                             4       8
   t2               temp    double                          8      16
   t3               temp    double                          8      24
   t4               temp    double                          8      32
   t5               temp    int                             4      40

 Code: 6 instruction(s)

    146     t1 = *v
    147     t2 = inttodouble t1
    148     t3 = *factor
    149     t4 = t2 double* t3
    150     t5 = doubletoint t4
    151     return t5

============================================================================
 FUNCTION rotate(int &, int &, int &)        (link name _Z6rotateRiS_S_)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int &                           4       0
   b                param   int &                           4       4
   c                param   int &                           4       8
   t                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24

 Code: 7 instruction(s)

    152     t1 = *a
    153     t2 = *b
    154     *a = t2
    155     t3 = *c
    156     *b = t3
    157     *c = t1
    158     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 17 parameter(s)/local(s), 73 temporaries, frame 740 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   z                local   int                             4       8
   rx               local   int &                           4      12
   rrx              local   int &                           4      16
   data             local   int[5]                         20      20
   lo               local   int                             4      40
   hi               local   int                             4      44
   p                local   int *                           4      48
   a                local   struct Account                 16      56
   b                local   struct Account                 16      72
   best             local   struct Account &                4      88
   limit            local   const int                       4      92
   rate             local   const double                    8      96
   small            local   short                           2     104
   msg              local   const char *                    4     108
   first            local   const char &                    4     112
   t1               temp    int *                           4     116
   t2               temp    int                             4     120
   t3               temp    int                             4     124
   t5               temp    int *                           4     132
   t6               temp    int *                           4     136
   t7               temp    int                             4     140
   t9               temp    int *                           4     148
   t10              temp    int *                           4     152
   t11              temp    int *                           4     156
   t16              temp    int                             4     176
   t17              temp    int                             4     180
   t19              temp    int **                          4     188
   t20              temp    int                             4     192
   t21              temp    int                             4     196
   t22              temp    int                             4     200
   t23              temp    int                             4     204
   t24              temp    int                             4     208
   t25              temp    struct Account *                4     212
   t27              temp    struct Account *                4     220
   t29              temp    struct Account *                4     228
   t30              temp    double                          8     232
   t31              temp    double                          8     240
   t36              temp    double                          8     264
   t37              temp    double                          8     272
   t38              temp    int                             4     280
   t40              temp    const int *                     4     296
   t41              temp    const double *                  4     300
   t43              temp    int                             4     308
   t45              temp    const int *                     4     316
   t46              temp    double                          8     320
   t47              temp    const double *                  4     328
   t49              temp    int                             4     336
   t51              temp    const int *                     4     344
   t52              temp    double                          8     352
   t53              temp    const double *                  4     360
   t55              temp    char                            1     368
   t56              temp    int                             4     372
   t57              temp    const char *                    4     376
   t58              temp    char                            1     380
   t59              temp    int                             4     384
   t60              temp    int                             4     388
   t61              temp    int                             4     392
   t66              temp    int                             4     412
   t67              temp    int                             4     416
   t71              temp    int *                           4     432
   t78              temp    int *                           4     460
   t80              temp    int *                           4     468
   t83              temp    struct Account *                4     488
   t84              temp    double                          8     496
   t85              temp    double                          8     504
   t90              temp    struct Account *                4     536
   t91              temp    double                          8     544
   t92              temp    struct Account *                4     552
   t96              temp    double                          8     568
   t98              temp    double                          8     584
   t99              temp    struct Account *                4     592
   t101             temp    const struct Account *          4     600
   t102             temp    double                          8     608
   t105             temp    int                             4     624
   t106             temp    double                          8     632
   t107             temp    double                          8     640
   t108             temp    double                          8     648
   t109             temp    int                             4     656
   t112             temp    int                             4     668
   t113             temp    double                          8     672
   t114             temp    double                          8     680
   t115             temp    double                          8     688
   t116             temp    int                             4     696
   t119             temp    int                             4     708
   t120             temp    double                          8     712
   t121             temp    double                          8     720
   t122             temp    double                          8     728
   t123             temp    int                             4     736
   (50 temporaries no longer used after optimization not shown)

 Code: 140 instruction(s)

    159        x = 1
    160        y = 2
    161        z = 3
    162        t1 = &x
    163        t2 = *t1
    164        t3 = t2 int+ 10
    165        *t1 = t3
    166        t5 = &y
    167        t6 = &z
    168        t66 = *t5
    169        *t1 = t66
    170        t67 = *t6
    171        *t5 = t67
    172        *t6 = t3
    173        t7 = *t1
    174        param "%d %d %d %d\n"
    175        param x
    176        param y
    177        param z
    178        param t7
    179        call printf, 5
    180        data[0] = 8
    181        data[4] = -3
    182        data[8] = 15
    183        data[12] = 0
    184        data[16] = 7
    185        t9 = &data
    186        t10 = &lo
    187        t11 = &hi
    188        param t9
    189        param 5
    190        param t10
    191        param t11
    192        call minmax(const int *, int, int &, int &), 4
    193        t71 = t9 ptr+ 12
    194        *t71 = 99
    195        t16 = *t9
    196        t17 = t16 int+ 1
    197        *t9 = t17
    198        p = t9
    199        t19 = &p
    200        t78 = *t19
    201        t80 = t78 ptr+ 8
    202        *t19 = t80
    203        t20 = *p
    204        t21 = t20 int+ 1
    205        *p = t21
    206        t22 = data[12]
    207        t23 = data[0]
    208        t24 = data[8]
    209        param "%d %d %d %d %d\n"
    210        param lo
    211        param hi
    212        param t22
    213        param t23
    214        param t24
    215        call printf, 6
    216        a[0] = 1
    217        a[8] = 100.5
    218        b[0] = 2
    219        b[8] = 2.5e+02
    220        t25 = &a
    221        t83 = t25 ptr+ 8
    222        t84 = *t83
    223        t85 = t84 double+ 2e+02
    224        *t83 = t85
    225        t27 = &b
    226        t90 = t27 ptr+ 8
    227        t91 = *t90
    228        if t85 double>= t91 goto L8
    229        goto L9
    230  L8:   t92 = t25
    231        goto L10
    232  L9:   t92 = t27
    233  L10:  t29 = t92 ptr+ 8
    234        t30 = *t29
    235        t31 = t30 double- 5e+01
    236        *t29 = t31
    237        t96 = *t83
    238        t98 = *t90
    239        if t96 double>= t98 goto L11
    240        goto L12
    241  L11:  t99 = t25
    242        goto L13
    243  L12:  t99 = t27
    244  L13:  t36 = a[8]
    245        t37 = b[8]
    246        t38 = *t99
    247        t101 = t99 ptr+ 8
    248        t102 = *t101
    249        param "%.1f %.1f %d %.1f\n"
    250        param t36
    251        param t37
    252        param t38
    253        param t102
    254        call printf, 5
    255        limit = 40
    256        rate = 1.25
    257        t40 = &limit
    258        t41 = &rate
    259        t105 = *t40
    260        t106 = inttodouble t105
    261        t107 = *t41
    262        t108 = t106 double* t107
    263        t109 = doubletoint t108
    264        t43 = 7
    265        t45 = &t43
    266        t46 = 2.0
    267        t47 = &t46
    268        t112 = *t45
    269        t113 = inttodouble t112
    270        t114 = *t47
    271        t115 = t113 double* t114
    272        t116 = doubletoint t115
    273        t49 = 7
    274        t51 = &t49
    275        t52 = 0.5
    276        t53 = &t52
    277        t119 = *t51
    278        t120 = inttodouble t119
    279        t121 = *t53
    280        t122 = t120 double* t121
    281        t123 = doubletoint t122
    282        param "%d %d %d\n"
    283        param t109
    284        param t116
    285        param t123
    286        call printf, 4
    287        t55 = *"const data"
    288        t56 = chartoint t55
    289        t57 = "const data" ptr+ 6
    290        t58 = *t57
    291        t59 = chartoint t58
    292        param "%c %c\n"
    293        param t56
    294        param t59
    295        call printf, 3
    296        t60 = *t1
    297        t61 = t60 int+ lo
    298        return t61


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Account            struct_tag    struct Account             -           5    -    0  size 16
   deposit            function      void (struct Account &, double) -           7    -    1  _Z7depositR7Accountd; defined
   peek               function      double (const struct Account &) -           8    -    1  _Z4peekRK7Account; defined
   richer             function      struct Account &(struct Account &, struct Account &) -           9    -    2  _Z6richerR7AccountS0_; defined
   minmax             function      void (const int *, int, int &, int &) -          11    -    1  _Z6minmaxPKiiRiS1_; defined
   advance            function      void (int *&, int)         -          19    -    1  _Z7advanceRPii; defined
   element            function      int &(int *, int)          -          20    -    2  _Z7elementPii; defined
   scale              function      int (const int &, const double &) -          21    -    3  _Z5scaleRKiRKd; defined
   rotate             function      void (int &, int &, int &) -          22    -    1  _Z6rotateRiS_S_; defined
   main               function      int (void)                 -          24    -    0  defined

 scope: global > struct Account
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      5    4    1  Account::id; public, offset 0
   balance            field         double                     member      5    8    7  Account::balance; public, offset 8

 scope: global > deposit()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     struct Account &           param       7    4    1  a.1
   amount             parameter     double                     param       7    8    1  amount.2

 scope: global > peek()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     const struct Account &     param       8    4    1  a.3

 scope: global > richer()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     struct Account &           param       9    4    2  a.4
   b                  parameter     struct Account &           param       9    4    2  b.5

 scope: global > minmax()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   values             parameter     const int *                param      11    4    5  values.6
   n                  parameter     int                        param      11    4    1  n.7
   lo                 parameter     int &                      param      11    4    3  lo.8
   hi                 parameter     int &                      param      11    4    3  hi.9

 scope: global > minmax() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      13    4    6  i.10

 scope: global > advance()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *&                     param      19    4    1  p.11
   steps              parameter     int                        param      19    4    1  steps.12

 scope: global > element()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param      20    4    1  a.13
   i                  parameter     int                        param      20    4    1  i.14

 scope: global > scale()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const int &                param      21    4    1  v.15
   factor             parameter     const double &             param      21    4    1  factor.16

 scope: global > rotate()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      22    4    2  a.17
   b                  parameter     int &                      param      22    4    2  b.18
   c                  parameter     int &                      param      22    4    2  c.19
   t                  variable      int                        local      22    4    1  t.20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      25    4    3  x.21
   y                  variable      int                        local      25    4    2  y.22
   z                  variable      int                        local      25    4    2  z.23
   rx                 variable      int &                      local      26    4    3  rx.24
   rrx                variable      int &                      local      27    4    1  rrx.25
   data               variable      int[5]                     local      32   20    7  data.26
   lo                 variable      int                        local      32    4    3  lo.27
   hi                 variable      int                        local      32    4    2  hi.28
   p                  variable      int *                      local      36    4    2  p.29
   a                  variable      struct Account             local      41   16    4  a.30
   b                  variable      struct Account             local      41   16    3  b.31
   best               variable      struct Account &           local      44    4    2  best.32
   limit              variable      const int                  local      47    4    1  limit.33; value 40
   rate               variable      const double               local      48    8    1  rate.34
   small              variable      short                      local      49    2    1  small.35
   msg                variable      const char *               local      51    4    2  msg.36
   first              variable      const char &               local      52    4    1  first.37

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Account: size 16, align 8
    +0  int id  [public]
    +8  double balance  [public]
