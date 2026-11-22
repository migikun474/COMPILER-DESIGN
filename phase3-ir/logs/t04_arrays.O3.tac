============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 248 -> 264 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          248 -> 264   (-6% fewer)

   constants folded                        6
   algebraic simplifications               7
   common subexpressions                   6
   copies / constants forwarded           20
   temporaries merged away                13
   dead instructions removed              15
   jumps removed or redirected             9
   unreachable instructions removed        0
   propagated across blocks                8
   dead assignments removed               10
   calls inlined                           5
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                         11
   unreachable functions removed           3

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   squares          int[5]                         20  0
   table            int[2][3]                      24  { +0: 1, +4: 2, +8: 3, +12: 4, +16: 5, +20: 6 }

 As three address code (initial values, in place before main runs):

    squares[...] = 0               (zero-initialized)
    table[0] = 1
    table[4] = 2
    table[8] = 3
    table[12] = 4
    table[16] = 5
    table[20] = 6

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 79 temporaries, frame 724 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int[5]                         20       0
   m                local   int[3][3]                      36      20
   cube             local   int[2][3][4]                   96      56
   i                local   int                             4     152
   j                local   int                             4     156
   k                local   int                             4     160
   flat             local   int[2][2]                      16     164
   sparse           local   int[6]                         24     180
   sized            local   int[4]                         16     204
   word             local   char[6]                         6     220
   buf              local   char[8]                         8     226
   lit              local   char *                          4     236
   avg              local   double[3]                      24     240
   t1               temp    int                             4     264
   t2               temp    int                             4     268
   t4               temp    int                             4     276
   t5               temp    int                             4     280
   t6               temp    int                             4     284
   t11              temp    int                             4     304
   t12              temp    int                             4     308
   t13              temp    int                             4     312
   t14              temp    int                             4     316
   t15              temp    int                             4     320
   t16              temp    int                             4     324
   t17              temp    int                             4     328
   t18              temp    int                             4     332
   t19              temp    int                             4     336
   t23              temp    int                             4     352
   t24              temp    int                             4     356
   t25              temp    int                             4     360
   t26              temp    int                             4     364
   t27              temp    int *                           4     368
   t29              temp    int                             4     376
   t34              temp    int                             4     396
   t35              temp    int                             4     400
   t36              temp    int                             4     404
   t37              temp    int                             4     408
   t38              temp    int                             4     412
   t39              temp    int                             4     416
   t40              temp    int                             4     420
   t41              temp    int                             4     424
   t42              temp    int                             4     428
   t43              temp    int                             4     432
   t44              temp    int                             4     436
   t46              temp    char *                          4     444
   t47              temp    char *                          4     448
   t51              temp    double                          8     464
   t52              temp    double                          8     472
   t53              temp    double                          8     480
   t54              temp    double                          8     488
   t59              temp    int                             4     516
   t62              temp    int                             4     528
   t63              temp    int                             4     532
   t64              temp    int                             4     536
   t65              temp    int                             4     540
   t66              temp    int                             4     544
   t67              temp    int                             4     548
   t68              temp    int                             4     552
   t69              temp    int                             4     556
   t71              temp    int *                           4     564
   t72              temp    int                             4     568
   t73              temp    char *                          4     572
   t74              temp    char                            1     576
   t75              temp    int                             4     580
   t77              temp    char                            1     588
   t78              temp    int                             4     592
   t79              temp    int                             4     596
   t82              temp    int                             4     608
   t83              temp    int                             4     612
   t84              temp    int                             4     616
   t85              temp    int *                           4     620
   t86              temp    int                             4     624
   t87              temp    int *                           4     628
   t89              temp    int                             4     636
   t90              temp    int                             4     640
   t91              temp    int                             4     644
   t92              temp    int *                           4     648
   t93              temp    int                             4     652
   t94              temp    int (*)[3]                      4     656
   t96              temp    int                             4     664
   t97              temp    int                             4     668
   t98              temp    int                             4     672
   t99              temp    int (*)[3]                      4     676
   t100             temp    int                             4     680
   t101             temp    int (*)[3]                      4     684
   t102             temp    int                             4     688
   t104             temp    int                             4     696
   t105             temp    char *                          4     700
   t106             temp    char                            1     704
   t108             temp    int                             4     712
   t109             temp    char *                          4     716
   t110             temp    char                            1     720
   (31 temporaries no longer used after optimization not shown)

 Code: 264 instruction(s)

    100        a[0] = 1
    101        a[4] = 2
    102        a[8] = 3
    103        a[12] = 0
    104        a[16] = 0
    105        i = 0
    106  L1:   if i int>= 5 goto L2
    107        t1 = i int<< 2                      (w = 4)
    108        t2 = i int* i
    109        squares[t1] = t2
    110        i = i int+ 1
    111        if i int>= 5 goto L2
    112        t1 = i int<< 2                      (w = 4)
    113        t2 = i int* i
    114        squares[t1] = t2
    115        i = i int+ 1
    116        goto L1
    117  L2:   i = 0
    118  L3:   if i int>= 3 goto L6
    119        j = 0
    120  L4:   if j int>= 3 goto L5
    121        t4 = i int* 3                       (n2 = 3)
    122        t5 = t4 int+ j
    123        t6 = t5 int<< 2                     (w = 4)
    124        m[t6] = t5
    125        j = j int+ 1
    126        if j int>= 3 goto L5
    127        t4 = i int* 3                       (n2 = 3)
    128        t5 = t4 int+ j
    129        t6 = t5 int<< 2                     (w = 4)
    130        m[t6] = t5
    131        j = j int+ 1
    132        goto L4
    133  L5:   i = i int+ 1
    134        goto L3
    135  L6:   i = 0
    136  L7:   if i int>= 2 goto L12
    137        j = 0
    138  L8:   if j int>= 3 goto L11
    139        k = 0
    140  L9:   if k int>= 4 goto L10
    141        t11 = i int* 3                      (n2 = 3)
    142        t12 = t11 int+ j
    143        t13 = t12 int<< 2                   (n3 = 4)
    144        t14 = t13 int+ k
    145        t15 = t14 int<< 2                   (w = 4)
    146        t16 = i int* 100
    147        t17 = j int* 10
    148        t18 = t16 int+ t17
    149        t19 = t18 int+ k
    150        cube[t15] = t19
    151        k = k int+ 1
    152        if k int>= 4 goto L10
    153        t11 = i int* 3                      (n2 = 3)
    154        t12 = t11 int+ j
    155        t13 = t12 int<< 2                   (n3 = 4)
    156        t14 = t13 int+ k
    157        t15 = t14 int<< 2                   (w = 4)
    158        t16 = i int* 100
    159        t17 = j int* 10
    160        t18 = t16 int+ t17
    161        t19 = t18 int+ k
    162        cube[t15] = t19
    163        k = k int+ 1
    164        goto L9
    165  L10:  j = j int+ 1
    166        goto L8
    167  L11:  i = i int+ 1
    168        goto L7
    169  L12:  t23 = a[0]
    170        t24 = a[8]
    171        t25 = a[12]
    172        t26 = a[16]
    173        t27 = &a
    174        t82 = 0
    175        t83 = 0
    176  L13:  if t83 int>= 5 goto L14
    177        t84 = t83 int<< 2
    178        t85 = t27 ptr+ t84
    179        t86 = *t85
    180        t82 = t82 int+ t86
    181        t83 = t83 int+ 1
    182        if t83 int>= 5 goto L14
    183        t84 = t83 int<< 2
    184        t85 = t27 ptr+ t84
    185        t86 = *t85
    186        t82 = t82 int+ t86
    187        t83 = t83 int+ 1
    188        goto L13
    189  L14:  param "%d %d %d %d %d\n"
    190        param t23
    191        param t24
    192        param t25
    193        param t26
    194        param t82
    195        call printf, 6
    196        t29 = squares[16]
    197        t87 = &squares
    198        t89 = 0
    199        t90 = 0
    200  L15:  if t90 int>= 5 goto L16
    201        t91 = t90 int<< 2
    202        t92 = t87 ptr+ t91
    203        t93 = *t92
    204        t89 = t89 int+ t93
    205        t90 = t90 int+ 1
    206        if t90 int>= 5 goto L16
    207        t91 = t90 int<< 2
    208        t92 = t87 ptr+ t91
    209        t93 = *t92
    210        t89 = t89 int+ t93
    211        t90 = t90 int+ 1
    212        goto L15
    213  L16:  t94 = &m
    214        t96 = 0
    215        t97 = 0
    216  L17:  if t97 int>= 3 goto L18
    217        t98 = t97 int* 12
    218        t99 = t94 ptr+ t98
    219        t100 = t97 int<< 2                  (w = 4)
    220        t101 = t99 ptr+ t100
    221        t102 = *t101
    222        t96 = t96 int+ t102
    223        t97 = t97 int+ 1
    224        if t97 int>= 3 goto L18
    225        t98 = t97 int* 12
    226        t99 = t94 ptr+ t98
    227        t100 = t97 int<< 2                  (w = 4)
    228        t101 = t99 ptr+ t100
    229        t102 = *t101
    230        t96 = t96 int+ t102
    231        t97 = t97 int+ 1
    232        goto L17
    233  L18:  param "%d %d %d\n"
    234        param t29
    235        param t89
    236        param t96
    237        call printf, 4
    238        t34 = cube[92]
    239        t35 = cube[24]
    240        t36 = m[28]
    241        param "%d %d %d\n"
    242        param t34
    243        param t35
    244        param t36
    245        call printf, 4
    246        t37 = table[20]
    247        t38 = table[4]
    248        t39 = table[12]
    249        t40 = t38 int+ t39
    250        param "%d %d\n"
    251        param t37
    252        param t40
    253        call printf, 3
    254        flat[0] = 1
    255        flat[4] = 2
    256        flat[8] = 3
    257        flat[12] = 4
    258        sparse[0] = 0
    259        sparse[4] = 7
    260        sparse[8] = 0
    261        sparse[12] = 0
    262        sparse[16] = 9
    263        sparse[20] = 0
    264        sized[0] = 5
    265        sized[4] = 6
    266        sized[8] = 7
    267        sized[12] = 8
    268        t41 = flat[8]
    269        t42 = sparse[4]
    270        t43 = sparse[16]
    271        t44 = sparse[20]
    272        param "%d %d %d %d %d\n"
    273        param t41
    274        param t42
    275        param t43
    276        param t44
    277        param 4
    278        call printf, 6
    279        word[0] = 104
    280        word[1] = 101
    281        word[2] = 108
    282        word[3] = 108
    283        word[4] = 111
    284        word[5] = 0
    285        buf[0] = 97
    286        buf[1] = 98
    287        buf[2] = 0
    288        buf[3] = 0
    289        buf[4] = 0
    290        buf[5] = 0
    291        buf[6] = 0
    292        buf[7] = 0
    293        word[0] = 106
    294        buf[2] = 99
    295        t46 = &word
    296        t47 = &buf
    297        t104 = 0
    298  L19:  t105 = t46 ptr+ t104
    299        t106 = *t105
    300        if t106 char== 0 goto L20
    301        t104 = t104 int+ 1
    302        t105 = t46 ptr+ t104
    303        t106 = *t105
    304        if t106 char== 0 goto L20
    305        t104 = t104 int+ 1
    306        goto L19
    307  L20:  t108 = 0
    308  L21:  t109 = "wide world" ptr+ t108
    309        t110 = *t109
    310        if t110 char== 0 goto L22
    311        t108 = t108 int+ 1
    312        t109 = "wide world" ptr+ t108
    313        t110 = *t109
    314        if t110 char== 0 goto L22
    315        t108 = t108 int+ 1
    316        goto L21
    317  L22:  param "%s %s %s %d %d\n"
    318        param t46
    319        param t47
    320        param "wide world"
    321        param t104
    322        param t108
    323        call printf, 6
    324        avg[0] = 1.5
    325        avg[8] = 2.5
    326        avg[16] = 0.0
    327        t51 = avg[0]
    328        t52 = avg[8]
    329        t53 = t51 double+ t52
    330        t54 = t53 double/ 2.0
    331        avg[16] = t54
    332        param "%.2f\n"
    333        param t54
    334        call printf, 2
    335        t59 = a[4]
    336        t62 = a[12]
    337        t63 = t59 int+ t62
    338        a[8] = t63
    339        t64 = a[0]
    340        t65 = t64 int<< 2                   (w = 4)
    341        t66 = a[t65]
    342        t67 = t66 int+ 10
    343        a[t65] = t67
    344        t68 = a[8]
    345        t69 = a[4]
    346        param "%d %d\n"
    347        param t68
    348        param t69
    349        call printf, 3
    350        t71 = t27 ptr+ 4
    351        t72 = *t71
    352        t73 = "literal" ptr+ 2
    353        t74 = *t73
    354        t75 = chartoint t74
    355        t77 = *t46
    356        t78 = chartoint t77
    357        param "%d %c %c\n"
    358        param t72
    359        param t75
    360        param t78
    361        call printf, 4
    362        t79 = m[16]
    363        return t79


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              function      int (int *, int)           -           3    -    2  _Z5totalPii; defined
   trace              function      int (int (*)[3], int)      -           9    -    1  _Z5tracePA3_ii; defined
   length             function      int (char *)               -          15    -    2  _Z6lengthPc; defined
   squares            variable      int[5]                     global     21   20    3  
   table              variable      int[2][3]                  global     22   24    3  
   main               function      int (void)                 -          24    -    0  defined

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       3    4    1  a.1
   n                  parameter     int                        param       3    4    1  n.2
   s                  variable      int                        local       4    4    2  s.3

 scope: global > total() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       5    4    3  i.4

 scope: global > trace()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int (*)[3]                 param       9    4    1  m.5
   n                  parameter     int                        param       9    4    1  n.6
   s                  variable      int                        local      10    4    2  s.7

 scope: global > trace() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      11    4    4  i.8

 scope: global > length()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     char *                     param      15    4    1  s.9
   n                  variable      int                        local      16    4    3  n.10

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int[5]                     local      25   20   13  a.11
   m                  variable      int[3][3]                  local      26   36    4  m.12
   cube               variable      int[2][3][4]               local      27   96    3  cube.13
   i                  variable      int                        local      28    4   20  i.14
   j                  variable      int                        local      28    4   10  j.15
   k                  variable      int                        local      28    4    5  k.16
   flat               variable      int[2][2]                  local      40   16    1  flat.17
   sparse             variable      int[6]                     local      41   24    3  sparse.18
   sized              variable      int[4]                     local      42   16    2  sized.19
   word               variable      char[6]                    local      45    6    4  word.20
   buf                variable      char[8]                    local      46    8    2  buf.21
   lit                variable      char *                     local      47    4    2  lit.22
   avg                variable      double[3]                  local      52   24    4  avg.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
