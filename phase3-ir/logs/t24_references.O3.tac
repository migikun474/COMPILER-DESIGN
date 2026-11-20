============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t24_references.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 217 -> 174 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          217 -> 174   (19% fewer)

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
   loops unrolled                          1
   unreachable functions removed           7

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

 Code: 34 instruction(s)

    100       t1 = *values
    101       *hi = t1
    102       *lo = t1
    103       i = 1
    104  L1:  if i int>= n goto L6
    105       t2 = i int<< 2
    106       t3 = values ptr+ t2
    107       t4 = *t3
    108       t5 = *lo
    109       if t4 int>= t5 goto L2
    110       t8 = *t3
    111       *lo = t8
    112  L2:  t11 = *t3
    113       t12 = *hi
    114       if t11 int<= t12 goto L3
    115       t15 = *t3
    116       *hi = t15
    117  L3:  i = i int+ 1
    118       if i int>= n goto L6
    119       t2 = i int<< 2
    120       t3 = values ptr+ t2
    121       t4 = *t3
    122       t5 = *lo
    123       if t4 int>= t5 goto L4
    124       t8 = *t3
    125       *lo = t8
    126  L4:  t11 = *t3
    127       t12 = *hi
    128       if t11 int<= t12 goto L5
    129       t15 = *t3
    130       *hi = t15
    131  L5:  i = i int+ 1
    132       goto L1
    133  L6:  return

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

    134        x = 1
    135        y = 2
    136        z = 3
    137        t1 = &x
    138        t2 = *t1
    139        t3 = t2 int+ 10
    140        *t1 = t3
    141        t5 = &y
    142        t6 = &z
    143        t66 = *t5
    144        *t1 = t66
    145        t67 = *t6
    146        *t5 = t67
    147        *t6 = t3
    148        t7 = *t1
    149        param "%d %d %d %d\n"
    150        param x
    151        param y
    152        param z
    153        param t7
    154        call printf, 5
    155        data[0] = 8
    156        data[4] = -3
    157        data[8] = 15
    158        data[12] = 0
    159        data[16] = 7
    160        t9 = &data
    161        t10 = &lo
    162        t11 = &hi
    163        param t9
    164        param 5
    165        param t10
    166        param t11
    167        call minmax(const int *, int, int &, int &), 4
    168        t71 = t9 ptr+ 12
    169        *t71 = 99
    170        t16 = *t9
    171        t17 = t16 int+ 1
    172        *t9 = t17
    173        p = t9
    174        t19 = &p
    175        t78 = *t19
    176        t80 = t78 ptr+ 8
    177        *t19 = t80
    178        t20 = *p
    179        t21 = t20 int+ 1
    180        *p = t21
    181        t22 = data[12]
    182        t23 = data[0]
    183        t24 = data[8]
    184        param "%d %d %d %d %d\n"
    185        param lo
    186        param hi
    187        param t22
    188        param t23
    189        param t24
    190        call printf, 6
    191        a[0] = 1
    192        a[8] = 100.5
    193        b[0] = 2
    194        b[8] = 2.5e+02
    195        t25 = &a
    196        t83 = t25 ptr+ 8
    197        t84 = *t83
    198        t85 = t84 double+ 2e+02
    199        *t83 = t85
    200        t27 = &b
    201        t90 = t27 ptr+ 8
    202        t91 = *t90
    203        if t85 double>= t91 goto L7
    204        goto L8
    205  L7:   t92 = t25
    206        goto L9
    207  L8:   t92 = t27
    208  L9:   t29 = t92 ptr+ 8
    209        t30 = *t29
    210        t31 = t30 double- 5e+01
    211        *t29 = t31
    212        t96 = *t83
    213        t98 = *t90
    214        if t96 double>= t98 goto L10
    215        goto L11
    216  L10:  t99 = t25
    217        goto L12
    218  L11:  t99 = t27
    219  L12:  t36 = a[8]
    220        t37 = b[8]
    221        t38 = *t99
    222        t101 = t99 ptr+ 8
    223        t102 = *t101
    224        param "%.1f %.1f %d %.1f\n"
    225        param t36
    226        param t37
    227        param t38
    228        param t102
    229        call printf, 5
    230        limit = 40
    231        rate = 1.25
    232        t40 = &limit
    233        t41 = &rate
    234        t105 = *t40
    235        t106 = inttodouble t105
    236        t107 = *t41
    237        t108 = t106 double* t107
    238        t109 = doubletoint t108
    239        t43 = 7
    240        t45 = &t43
    241        t46 = 2.0
    242        t47 = &t46
    243        t112 = *t45
    244        t113 = inttodouble t112
    245        t114 = *t47
    246        t115 = t113 double* t114
    247        t116 = doubletoint t115
    248        t49 = 7
    249        t51 = &t49
    250        t52 = 0.5
    251        t53 = &t52
    252        t119 = *t51
    253        t120 = inttodouble t119
    254        t121 = *t53
    255        t122 = t120 double* t121
    256        t123 = doubletoint t122
    257        param "%d %d %d\n"
    258        param t109
    259        param t116
    260        param t123
    261        call printf, 4
    262        t55 = *"const data"
    263        t56 = chartoint t55
    264        t57 = "const data" ptr+ 6
    265        t58 = *t57
    266        t59 = chartoint t58
    267        param "%c %c\n"
    268        param t56
    269        param t59
    270        call printf, 3
    271        t60 = *t1
    272        t61 = t60 int+ lo
    273        return t61


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Account            struct_tag    struct Account             -           4    -    0  size 16
   deposit            function      void (struct Account &, double) -           6    -    1  _Z7depositR7Accountd; defined
   peek               function      double (const struct Account &) -           7    -    1  _Z4peekRK7Account; defined
   richer             function      struct Account &(struct Account &, struct Account &) -           8    -    2  _Z6richerR7AccountS0_; defined
   minmax             function      void (const int *, int, int &, int &) -          10    -    1  _Z6minmaxPKiiRiS1_; defined
   advance            function      void (int *&, int)         -          18    -    1  _Z7advanceRPii; defined
   element            function      int &(int *, int)          -          19    -    2  _Z7elementPii; defined
   scale              function      int (const int &, const double &) -          20    -    3  _Z5scaleRKiRKd; defined
   rotate             function      void (int &, int &, int &) -          21    -    1  _Z6rotateRiS_S_; defined
   main               function      int (void)                 -          23    -    0  defined

 scope: global > struct Account
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      4    4    1  Account::id; public, offset 0
   balance            field         double                     member      4    8    7  Account::balance; public, offset 8

 scope: global > deposit()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     struct Account &           param       6    4    1  a.1
   amount             parameter     double                     param       6    8    1  amount.2

 scope: global > peek()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     const struct Account &     param       7    4    1  a.3

 scope: global > richer()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     struct Account &           param       8    4    2  a.4
   b                  parameter     struct Account &           param       8    4    2  b.5

 scope: global > minmax()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   values             parameter     const int *                param      10    4    5  values.6
   n                  parameter     int                        param      10    4    1  n.7
   lo                 parameter     int &                      param      10    4    3  lo.8
   hi                 parameter     int &                      param      10    4    3  hi.9

 scope: global > minmax() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      12    4    6  i.10

 scope: global > advance()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *&                     param      18    4    1  p.11
   steps              parameter     int                        param      18    4    1  steps.12

 scope: global > element()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param      19    4    1  a.13
   i                  parameter     int                        param      19    4    1  i.14

 scope: global > scale()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const int &                param      20    4    1  v.15
   factor             parameter     const double &             param      20    4    1  factor.16

 scope: global > rotate()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      21    4    2  a.17
   b                  parameter     int &                      param      21    4    2  b.18
   c                  parameter     int &                      param      21    4    2  c.19
   t                  variable      int                        local      21    4    1  t.20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      24    4    3  x.21
   y                  variable      int                        local      24    4    2  y.22
   z                  variable      int                        local      24    4    2  z.23
   rx                 variable      int &                      local      25    4    3  rx.24
   rrx                variable      int &                      local      26    4    1  rrx.25
   data               variable      int[5]                     local      31   20    7  data.26
   lo                 variable      int                        local      31    4    3  lo.27
   hi                 variable      int                        local      31    4    2  hi.28
   p                  variable      int *                      local      35    4    2  p.29
   a                  variable      struct Account             local      40   16    4  a.30
   b                  variable      struct Account             local      40   16    3  b.31
   best               variable      struct Account &           local      43    4    2  best.32
   limit              variable      const int                  local      46    4    1  limit.33; value 40
   rate               variable      const double               local      47    8    1  rate.34
   small              variable      short                      local      48    2    1  small.35
   msg                variable      const char *               local      50    4    2  msg.36
   first              variable      const char &               local      51    4    1  first.37

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Account: size 16, align 8
    +0  int id  [public]
    +8  double balance  [public]
