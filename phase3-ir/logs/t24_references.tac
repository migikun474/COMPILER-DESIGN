============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t24_references.c
   Optimization  : no optimization
   Result        : Three address code generated: 9 function(s), 217 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION deposit(struct Account &, double)        (link name _Z7depositR7Accountd)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   struct Account &                4       0
   amount           param   double                          8       8
   t1               temp    struct Account *                4      16
   t2               temp    double                          8      24
   t3               temp    double                          8      32
   t4               temp    struct Account *                4      40

 Code: 6 instruction(s)

    100     t1 = a ptr+ 8
    101     t2 = *t1
    102     t3 = t2 double+ amount
    103     t4 = a ptr+ 8
    104     *t4 = t3
    105     return

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

    106     t1 = a ptr+ 8
    107     t2 = *t1
    108     return t2

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

    109       t2 = a ptr+ 8
    110       t3 = *t2
    111       t4 = b ptr+ 8
    112       t5 = *t4
    113       if t3 double>= t5 goto L1
    114       goto L2
    115  L1:  t1 = a
    116       goto L3
    117  L2:  t1 = b
    118  L3:  return t1

============================================================================
 FUNCTION minmax(const int *, int, int &, int &)        (link name _Z6minmaxPKiiRiS1_)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 16 temporaries, frame 84 bytes

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
   t6               temp    int                             4      40
   t7               temp    const int *                     4      44
   t8               temp    int                             4      48
   t9               temp    int                             4      52
   t10              temp    const int *                     4      56
   t11              temp    int                             4      60
   t12              temp    int                             4      64
   t13              temp    int                             4      68
   t14              temp    const int *                     4      72
   t15              temp    int                             4      76
   t16              temp    int                             4      80

 Code: 30 instruction(s)

    119        t1 = *values
    120        *hi = t1
    121        *lo = t1
    122        i = 1
    123  L4:   if i int< n goto L5
    124        goto L10
    125  L5:   t2 = i int* 4
    126        t3 = values ptr+ t2
    127        t4 = *t3
    128        t5 = *lo
    129        if t4 int< t5 goto L6
    130        goto L7
    131  L6:   t6 = i int* 4
    132        t7 = values ptr+ t6
    133        t8 = *t7
    134        *lo = t8
    135  L7:   t9 = i int* 4
    136        t10 = values ptr+ t9
    137        t11 = *t10
    138        t12 = *hi
    139        if t11 int> t12 goto L8
    140        goto L9
    141  L8:   t13 = i int* 4
    142        t14 = values ptr+ t13
    143        t15 = *t14
    144        *hi = t15
    145  L9:   t16 = i int+ 1
    146        i = t16
    147        goto L4
    148  L10:  return

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

    149     t1 = *p
    150     t2 = steps int* 4
    151     t3 = t1 ptr+ t2
    152     *p = t3
    153     return

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

    154     t1 = i int* 4
    155     t2 = a ptr+ t1
    156     return t2

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

    157     t1 = *v
    158     t2 = inttodouble t1
    159     t3 = *factor
    160     t4 = t2 double* t3
    161     t5 = doubletoint t4
    162     return t5

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

 Code: 8 instruction(s)

    163     t1 = *a
    164     t = t1
    165     t2 = *b
    166     *a = t2
    167     t3 = *c
    168     *b = t3
    169     *c = t
    170     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 17 parameter(s)/local(s), 61 temporaries, frame 396 bytes

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
   t4               temp    int *                           4     128
   t5               temp    int *                           4     132
   t6               temp    int *                           4     136
   t7               temp    int                             4     140
   t8               temp    int                             4     144
   t9               temp    int *                           4     148
   t10              temp    int *                           4     152
   t11              temp    int *                           4     156
   t12              temp    int *                           4     160
   t13              temp    int &                           4     164
   t14              temp    int *                           4     168
   t15              temp    int &                           4     172
   t16              temp    int                             4     176
   t17              temp    int                             4     180
   t18              temp    int *                           4     184
   t19              temp    int **                          4     188
   t20              temp    int                             4     192
   t21              temp    int                             4     196
   t22              temp    int                             4     200
   t23              temp    int                             4     204
   t24              temp    int                             4     208
   t25              temp    struct Account *                4     212
   t26              temp    struct Account *                4     216
   t27              temp    struct Account *                4     220
   t28              temp    struct Account &                4     224
   t29              temp    struct Account *                4     228
   t30              temp    double                          8     232
   t31              temp    double                          8     240
   t32              temp    struct Account *                4     248
   t33              temp    struct Account *                4     252
   t34              temp    struct Account *                4     256
   t35              temp    struct Account &                4     260
   t36              temp    double                          8     264
   t37              temp    double                          8     272
   t38              temp    int                             4     280
   t39              temp    double                          8     288
   t40              temp    const int *                     4     296
   t41              temp    const double *                  4     300
   t42              temp    int                             4     304
   t43              temp    int                             4     308
   t44              temp    int                             4     312
   t45              temp    const int *                     4     316
   t46              temp    double                          8     320
   t47              temp    const double *                  4     328
   t48              temp    int                             4     332
   t49              temp    int                             4     336
   t50              temp    int                             4     340
   t51              temp    const int *                     4     344
   t52              temp    double                          8     352
   t53              temp    const double *                  4     360
   t54              temp    int                             4     364
   t55              temp    char                            1     368
   t56              temp    int                             4     372
   t57              temp    const char *                    4     376
   t58              temp    char                            1     380
   t59              temp    int                             4     384
   t60              temp    int                             4     388
   t61              temp    int                             4     392

 Code: 146 instruction(s)

    171     x = 1
    172     y = 2
    173     z = 3
    174     t1 = &x
    175     rx = t1
    176     rrx = rx
    177     t2 = *rrx
    178     t3 = t2 int+ 10
    179     *rrx = t3
    180     t4 = &x
    181     t5 = &y
    182     t6 = &z
    183     param t4
    184     param t5
    185     param t6
    186     call rotate(int &, int &, int &), 3
    187     t7 = *rx
    188     param "%d %d %d %d\n"
    189     param x
    190     param y
    191     param z
    192     param t7
    193     call printf, 5
    194     t8 = int- 3
    195     data[0] = 8
    196     data[4] = t8
    197     data[8] = 15
    198     data[12] = 0
    199     data[16] = 7
    200     t9 = &data
    201     t10 = &lo
    202     t11 = &hi
    203     param t9
    204     param 5
    205     param t10
    206     param t11
    207     call minmax(const int *, int, int &, int &), 4
    208     t12 = &data
    209     param t12
    210     param 3
    211     t13 = call element(int *, int), 2
    212     *t13 = 99
    213     t14 = &data
    214     param t14
    215     param 0
    216     t15 = call element(int *, int), 2
    217     t16 = *t15
    218     t17 = t16 int+ 1
    219     *t15 = t17
    220     t18 = &data
    221     p = t18
    222     t19 = &p
    223     param t19
    224     param 2
    225     call advance(int *&, int), 2
    226     t20 = *p
    227     t21 = t20 int+ 1
    228     *p = t21
    229     t22 = data[12]
    230     t23 = data[0]
    231     t24 = data[8]
    232     param "%d %d %d %d %d\n"
    233     param lo
    234     param hi
    235     param t22
    236     param t23
    237     param t24
    238     call printf, 6
    239     a[0] = 1
    240     a[8] = 100.5
    241     b[0] = 2
    242     b[8] = 2.5e+02
    243     t25 = &a
    244     param t25
    245     param 2e+02
    246     call deposit(struct Account &, double), 2
    247     t26 = &a
    248     t27 = &b
    249     param t26
    250     param t27
    251     t28 = call richer(struct Account &, struct Account &), 2
    252     t29 = t28 ptr+ 8
    253     t30 = *t29
    254     t31 = t30 double- 5e+01
    255     t32 = t28 ptr+ 8
    256     *t32 = t31
    257     t33 = &a
    258     t34 = &b
    259     param t33
    260     param t34
    261     t35 = call richer(struct Account &, struct Account &), 2
    262     best = t35
    263     t36 = a[8]
    264     t37 = b[8]
    265     t38 = *best
    266     param best
    267     t39 = call peek(const struct Account &), 1
    268     param "%.1f %.1f %d %.1f\n"
    269     param t36
    270     param t37
    271     param t38
    272     param t39
    273     call printf, 5
    274     limit = 40
    275     rate = 1.25
    276     small = 7
    277     t40 = &limit
    278     t41 = &rate
    279     param t40
    280     param t41
    281     t42 = call scale(const int &, const double &), 2
    282     t44 = shorttoint small
    283     t43 = t44
    284     t45 = &t43
    285     t46 = 2.0
    286     t47 = &t46
    287     param t45
    288     param t47
    289     t48 = call scale(const int &, const double &), 2
    290     t50 = 3 int+ 4
    291     t49 = t50
    292     t51 = &t49
    293     t52 = 0.5
    294     t53 = &t52
    295     param t51
    296     param t53
    297     t54 = call scale(const int &, const double &), 2
    298     param "%d %d %d\n"
    299     param t42
    300     param t48
    301     param t54
    302     call printf, 4
    303     msg = "const data"
    304     first = msg
    305     t55 = *first
    306     t56 = chartoint t55
    307     t57 = msg ptr+ 6
    308     t58 = *t57
    309     t59 = chartoint t58
    310     param "%c %c\n"
    311     param t56
    312     param t59
    313     call printf, 3
    314     t60 = *rx
    315     t61 = t60 int+ lo
    316     return t61


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
