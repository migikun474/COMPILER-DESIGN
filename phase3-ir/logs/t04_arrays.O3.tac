============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 248 -> 242 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          248 -> 242   (2% fewer)

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
   instructions moved out of loops         7

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
 FUNCTION total(int *, int)        (link name _Z5totalPii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int *                           4      20
   t3               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    100       s = 0
    101       i = 0
    102  L1:  if i int>= n goto L2
    103       t1 = i int<< 2
    104       t2 = a ptr+ t1
    105       t3 = *t2
    106       s = s int+ t3
    107       i = i int+ 1
    108       goto L1
    109  L2:  return s

============================================================================
 FUNCTION trace(int (*)[3], int)        (link name _Z5tracePA3_ii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   int (*)[3]                      4       0
   n                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int (*)[3]                      4      20
   t3               temp    int                             4      24
   t4               temp    int (*)[3]                      4      28
   t5               temp    int                             4      32
   (2 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    110       s = 0
    111       i = 0
    112  L3:  if i int>= n goto L4
    113       t1 = i int* 12
    114       t2 = m ptr+ t1
    115       t3 = i int<< 2                      (w = 4)
    116       t4 = t2 ptr+ t3
    117       t5 = *t4
    118       s = s int+ t5
    119       i = i int+ 1
    120       goto L3
    121  L4:  return s

============================================================================
 FUNCTION length(char *)        (link name _Z6lengthPc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0
   n                local   int                             4       4
   t1               temp    char *                          4       8
   t2               temp    char                            1      12
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    122       n = 0
    123  L5:  t1 = s ptr+ n
    124       t2 = *t1
    125       if t2 char== 0 goto L6
    126       n = n int+ 1
    127       goto L5
    128  L6:  return n

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

 Code: 213 instruction(s)

    129        a[0] = 1
    130        a[4] = 2
    131        a[8] = 3
    132        a[12] = 0
    133        a[16] = 0
    134        i = 0
    135  L7:   if i int>= 5 goto L8
    136        t1 = i int<< 2                      (w = 4)
    137        t2 = i int* i
    138        squares[t1] = t2
    139        i = i int+ 1
    140        goto L7
    141  L8:   i = 0
    142  L9:   if i int>= 3 goto L12
    143        j = 0
    144        t4 = i int* 3                       (n2 = 3)
    145  L10:  if j int>= 3 goto L11
    146        t5 = t4 int+ j
    147        t6 = t5 int<< 2                     (w = 4)
    148        m[t6] = t5
    149        j = j int+ 1
    150        goto L10
    151  L11:  i = i int+ 1
    152        goto L9
    153  L12:  i = 0
    154  L13:  if i int>= 2 goto L18
    155        j = 0
    156        t11 = i int* 3                      (n2 = 3)
    157        t16 = i int* 100
    158  L14:  if j int>= 3 goto L17
    159        k = 0
    160        t12 = t11 int+ j
    161        t13 = t12 int<< 2                   (n3 = 4)
    162        t17 = j int* 10
    163        t18 = t16 int+ t17
    164  L15:  if k int>= 4 goto L16
    165        t14 = t13 int+ k
    166        t15 = t14 int<< 2                   (w = 4)
    167        t19 = t18 int+ k
    168        cube[t15] = t19
    169        k = k int+ 1
    170        goto L15
    171  L16:  j = j int+ 1
    172        goto L14
    173  L17:  i = i int+ 1
    174        goto L13
    175  L18:  t23 = a[0]
    176        t24 = a[8]
    177        t25 = a[12]
    178        t26 = a[16]
    179        t27 = &a
    180        t82 = 0
    181        t83 = 0
    182  L19:  if t83 int>= 5 goto L20
    183        t84 = t83 int<< 2
    184        t85 = t27 ptr+ t84
    185        t86 = *t85
    186        t82 = t82 int+ t86
    187        t83 = t83 int+ 1
    188        goto L19
    189  L20:  param "%d %d %d %d %d\n"
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
    200  L21:  if t90 int>= 5 goto L22
    201        t91 = t90 int<< 2
    202        t92 = t87 ptr+ t91
    203        t93 = *t92
    204        t89 = t89 int+ t93
    205        t90 = t90 int+ 1
    206        goto L21
    207  L22:  t94 = &m
    208        t96 = 0
    209        t97 = 0
    210  L23:  if t97 int>= 3 goto L24
    211        t98 = t97 int* 12
    212        t99 = t94 ptr+ t98
    213        t100 = t97 int<< 2                  (w = 4)
    214        t101 = t99 ptr+ t100
    215        t102 = *t101
    216        t96 = t96 int+ t102
    217        t97 = t97 int+ 1
    218        goto L23
    219  L24:  param "%d %d %d\n"
    220        param t29
    221        param t89
    222        param t96
    223        call printf, 4
    224        t34 = cube[92]
    225        t35 = cube[24]
    226        t36 = m[28]
    227        param "%d %d %d\n"
    228        param t34
    229        param t35
    230        param t36
    231        call printf, 4
    232        t37 = table[20]
    233        t38 = table[4]
    234        t39 = table[12]
    235        t40 = t38 int+ t39
    236        param "%d %d\n"
    237        param t37
    238        param t40
    239        call printf, 3
    240        flat[0] = 1
    241        flat[4] = 2
    242        flat[8] = 3
    243        flat[12] = 4
    244        sparse[0] = 0
    245        sparse[4] = 7
    246        sparse[8] = 0
    247        sparse[12] = 0
    248        sparse[16] = 9
    249        sparse[20] = 0
    250        sized[0] = 5
    251        sized[4] = 6
    252        sized[8] = 7
    253        sized[12] = 8
    254        t41 = flat[8]
    255        t42 = sparse[4]
    256        t43 = sparse[16]
    257        t44 = sparse[20]
    258        param "%d %d %d %d %d\n"
    259        param t41
    260        param t42
    261        param t43
    262        param t44
    263        param 4
    264        call printf, 6
    265        word[0] = 104
    266        word[1] = 101
    267        word[2] = 108
    268        word[3] = 108
    269        word[4] = 111
    270        word[5] = 0
    271        buf[0] = 97
    272        buf[1] = 98
    273        buf[2] = 0
    274        buf[3] = 0
    275        buf[4] = 0
    276        buf[5] = 0
    277        buf[6] = 0
    278        buf[7] = 0
    279        word[0] = 106
    280        buf[2] = 99
    281        t46 = &word
    282        t47 = &buf
    283        t104 = 0
    284  L25:  t105 = t46 ptr+ t104
    285        t106 = *t105
    286        if t106 char== 0 goto L26
    287        t104 = t104 int+ 1
    288        goto L25
    289  L26:  t108 = 0
    290  L27:  t109 = "wide world" ptr+ t108
    291        t110 = *t109
    292        if t110 char== 0 goto L28
    293        t108 = t108 int+ 1
    294        goto L27
    295  L28:  param "%s %s %s %d %d\n"
    296        param t46
    297        param t47
    298        param "wide world"
    299        param t104
    300        param t108
    301        call printf, 6
    302        avg[0] = 1.5
    303        avg[8] = 2.5
    304        avg[16] = 0.0
    305        t51 = avg[0]
    306        t52 = avg[8]
    307        t53 = t51 double+ t52
    308        t54 = t53 double/ 2.0
    309        avg[16] = t54
    310        param "%.2f\n"
    311        param t54
    312        call printf, 2
    313        t59 = a[4]
    314        t62 = a[12]
    315        t63 = t59 int+ t62
    316        a[8] = t63
    317        t64 = a[0]
    318        t65 = t64 int<< 2                   (w = 4)
    319        t66 = a[t65]
    320        t67 = t66 int+ 10
    321        a[t65] = t67
    322        t68 = a[8]
    323        t69 = a[4]
    324        param "%d %d\n"
    325        param t68
    326        param t69
    327        call printf, 3
    328        t71 = t27 ptr+ 4
    329        t72 = *t71
    330        t73 = "literal" ptr+ 2
    331        t74 = *t73
    332        t75 = chartoint t74
    333        t77 = *t46
    334        t78 = chartoint t77
    335        param "%d %c %c\n"
    336        param t72
    337        param t75
    338        param t78
    339        call printf, 4
    340        t79 = m[16]
    341        return t79


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              function      int (int *, int)           -           4    -    2  _Z5totalPii; defined
   trace              function      int (int (*)[3], int)      -          10    -    1  _Z5tracePA3_ii; defined
   length             function      int (char *)               -          16    -    2  _Z6lengthPc; defined
   squares            variable      int[5]                     global     22   20    3  
   table              variable      int[2][3]                  global     23   24    3  
   main               function      int (void)                 -          25    -    0  defined

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       4    4    1  a.1
   n                  parameter     int                        param       4    4    1  n.2
   s                  variable      int                        local       5    4    2  s.3

 scope: global > total() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       6    4    3  i.4

 scope: global > trace()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int (*)[3]                 param      10    4    1  m.5
   n                  parameter     int                        param      10    4    1  n.6
   s                  variable      int                        local      11    4    2  s.7

 scope: global > trace() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      12    4    4  i.8

 scope: global > length()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     char *                     param      16    4    1  s.9
   n                  variable      int                        local      17    4    3  n.10

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int[5]                     local      26   20   13  a.11
   m                  variable      int[3][3]                  local      27   36    4  m.12
   cube               variable      int[2][3][4]               local      28   96    3  cube.13
   i                  variable      int                        local      29    4   20  i.14
   j                  variable      int                        local      29    4   10  j.15
   k                  variable      int                        local      29    4    5  k.16
   flat               variable      int[2][2]                  local      41   16    1  flat.17
   sparse             variable      int[6]                     local      42   24    3  sparse.18
   sized              variable      int[4]                     local      43   16    2  sized.19
   word               variable      char[6]                    local      46    6    4  word.20
   buf                variable      char[8]                    local      47    8    2  buf.21
   lit                variable      char *                     local      48    4    2  lit.22
   avg                variable      double[3]                  local      53   24    4  avg.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
