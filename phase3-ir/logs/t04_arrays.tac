============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 248 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int *                           4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32

 Code: 13 instruction(s)

    100       s = 0
    101       i = 0
    102  L1:  if i int< n goto L2
    103       goto L3
    104  L2:  t1 = i int* 4
    105       t2 = a ptr+ t1
    106       t3 = *t2
    107       t4 = s int+ t3
    108       s = t4
    109       t5 = i int+ 1
    110       i = t5
    111       goto L1
    112  L3:  return s

============================================================================
 FUNCTION trace(int (*)[3], int)        (link name _Z5tracePA3_ii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 7 temporaries, frame 44 bytes

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
   t6               temp    int                             4      36
   t7               temp    int                             4      40

 Code: 15 instruction(s)

    113       s = 0
    114       i = 0
    115  L4:  if i int< n goto L5
    116       goto L6
    117  L5:  t1 = i int* 12
    118       t2 = m ptr+ t1
    119       t3 = i int* 4                       (w = 4)
    120       t4 = t2 ptr+ t3
    121       t5 = *t4
    122       t6 = s int+ t5
    123       s = t6
    124       t7 = i int+ 1
    125       i = t7
    126       goto L4
    127  L6:  return s

============================================================================
 FUNCTION length(char *)        (link name _Z6lengthPc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0
   n                local   int                             4       4
   t1               temp    char *                          4       8
   t2               temp    char                            1      12
   t3               temp    int                             4      16

 Code: 9 instruction(s)

    128       n = 0
    129  L7:  t1 = s ptr+ n
    130       t2 = *t1
    131       if t2 char!= 0 goto L8
    132       goto L9
    133  L8:  t3 = n int+ 1
    134       n = t3
    135       goto L7
    136  L9:  return n

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 79 temporaries, frame 600 bytes

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
   t3               temp    int                             4     272
   t4               temp    int                             4     276
   t5               temp    int                             4     280
   t6               temp    int                             4     284
   t7               temp    int                             4     288
   t8               temp    int                             4     292
   t9               temp    int                             4     296
   t10              temp    int                             4     300
   t11              temp    int                             4     304
   t12              temp    int                             4     308
   t13              temp    int                             4     312
   t14              temp    int                             4     316
   t15              temp    int                             4     320
   t16              temp    int                             4     324
   t17              temp    int                             4     328
   t18              temp    int                             4     332
   t19              temp    int                             4     336
   t20              temp    int                             4     340
   t21              temp    int                             4     344
   t22              temp    int                             4     348
   t23              temp    int                             4     352
   t24              temp    int                             4     356
   t25              temp    int                             4     360
   t26              temp    int                             4     364
   t27              temp    int (*)[5]                      4     368
   t28              temp    int                             4     372
   t29              temp    int                             4     376
   t30              temp    int (*)[5]                      4     380
   t31              temp    int                             4     384
   t32              temp    int (*)[3][3]                   4     388
   t33              temp    int                             4     392
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
   t45              temp    unsigned int                    4     440
   t46              temp    char (*)[6]                     4     444
   t47              temp    char (*)[8]                     4     448
   t48              temp    char (*)[6]                     4     452
   t49              temp    int                             4     456
   t50              temp    int                             4     460
   t51              temp    double                          8     464
   t52              temp    double                          8     472
   t53              temp    double                          8     480
   t54              temp    double                          8     488
   t55              temp    double                          8     496
   t56              temp    int                             4     504
   t57              temp    int                             4     508
   t58              temp    int                             4     512
   t59              temp    int                             4     516
   t60              temp    int                             4     520
   t61              temp    int                             4     524
   t62              temp    int                             4     528
   t63              temp    int                             4     532
   t64              temp    int                             4     536
   t65              temp    int                             4     540
   t66              temp    int                             4     544
   t67              temp    int                             4     548
   t68              temp    int                             4     552
   t69              temp    int                             4     556
   t70              temp    int (*)[5]                      4     560
   t71              temp    int *                           4     564
   t72              temp    int                             4     568
   t73              temp    char *                          4     572
   t74              temp    char                            1     576
   t75              temp    int                             4     580
   t76              temp    char (*)[6]                     4     584
   t77              temp    char                            1     588
   t78              temp    int                             4     592
   t79              temp    int                             4     596

 Code: 211 instruction(s)

    137        a[0] = 1
    138        a[4] = 2
    139        a[8] = 3
    140        a[12] = 0
    141        a[16] = 0
    142        i = 0
    143  L10:  if i int< 5 goto L11
    144        goto L12
    145  L11:  t1 = i int* 4                       (w = 4)
    146        t2 = i int* i
    147        squares[t1] = t2
    148        t3 = i int+ 1
    149        i = t3
    150        goto L10
    151  L12:  i = 0
    152  L13:  if i int< 3 goto L14
    153        goto L18
    154  L14:  j = 0
    155  L15:  if j int< 3 goto L16
    156        goto L17
    157  L16:  t4 = i int* 3                       (n2 = 3)
    158        t5 = t4 int+ j
    159        t6 = t5 int* 4                      (w = 4)
    160        t7 = i int* 3
    161        t8 = t7 int+ j
    162        m[t6] = t8
    163        t9 = j int+ 1
    164        j = t9
    165        goto L15
    166  L17:  t10 = i int+ 1
    167        i = t10
    168        goto L13
    169  L18:  i = 0
    170  L19:  if i int< 2 goto L20
    171        goto L27
    172  L20:  j = 0
    173  L21:  if j int< 3 goto L22
    174        goto L26
    175  L22:  k = 0
    176  L23:  if k int< 4 goto L24
    177        goto L25
    178  L24:  t11 = i int* 3                      (n2 = 3)
    179        t12 = t11 int+ j
    180        t13 = t12 int* 4                    (n3 = 4)
    181        t14 = t13 int+ k
    182        t15 = t14 int* 4                    (w = 4)
    183        t16 = i int* 100
    184        t17 = j int* 10
    185        t18 = t16 int+ t17
    186        t19 = t18 int+ k
    187        cube[t15] = t19
    188        t20 = k int+ 1
    189        k = t20
    190        goto L23
    191  L25:  t21 = j int+ 1
    192        j = t21
    193        goto L21
    194  L26:  t22 = i int+ 1
    195        i = t22
    196        goto L19
    197  L27:  t23 = a[0]
    198        t24 = a[8]
    199        t25 = a[12]
    200        t26 = a[16]
    201        t27 = &a
    202        param t27
    203        param 5
    204        t28 = call total(int *, int), 2
    205        param "%d %d %d %d %d\n"
    206        param t23
    207        param t24
    208        param t25
    209        param t26
    210        param t28
    211        call printf, 6
    212        t29 = squares[16]
    213        t30 = &squares
    214        param t30
    215        param 5
    216        t31 = call total(int *, int), 2
    217        t32 = &m
    218        param t32
    219        param 3
    220        t33 = call trace(int (*)[3], int), 2
    221        param "%d %d %d\n"
    222        param t29
    223        param t31
    224        param t33
    225        call printf, 4
    226        t34 = cube[92]
    227        t35 = cube[24]
    228        t36 = m[28]
    229        param "%d %d %d\n"
    230        param t34
    231        param t35
    232        param t36
    233        call printf, 4
    234        t37 = table[20]
    235        t38 = table[4]
    236        t39 = table[12]
    237        t40 = t38 int+ t39
    238        param "%d %d\n"
    239        param t37
    240        param t40
    241        call printf, 3
    242        flat[0] = 1
    243        flat[4] = 2
    244        flat[8] = 3
    245        flat[12] = 4
    246        sparse[0] = 0
    247        sparse[4] = 7
    248        sparse[8] = 0
    249        sparse[12] = 0
    250        sparse[16] = 9
    251        sparse[20] = 0
    252        sized[0] = 5
    253        sized[4] = 6
    254        sized[8] = 7
    255        sized[12] = 8
    256        t41 = flat[8]
    257        t42 = sparse[4]
    258        t43 = sparse[16]
    259        t44 = sparse[20]
    260        t45 = 16 uint/ 4
    261        param "%d %d %d %d %d\n"
    262        param t41
    263        param t42
    264        param t43
    265        param t44
    266        param t45
    267        call printf, 6
    268        word[0] = 104
    269        word[1] = 101
    270        word[2] = 108
    271        word[3] = 108
    272        word[4] = 111
    273        word[5] = 0
    274        buf[0] = 97
    275        buf[1] = 98
    276        buf[2] = 0
    277        buf[3] = 0
    278        buf[4] = 0
    279        buf[5] = 0
    280        buf[6] = 0
    281        buf[7] = 0
    282        lit = "wide world"
    283        word[0] = 106
    284        buf[2] = 99
    285        t46 = &word
    286        t47 = &buf
    287        t48 = &word
    288        param t48
    289        t49 = call length(char *), 1
    290        param lit
    291        t50 = call length(char *), 1
    292        param "%s %s %s %d %d\n"
    293        param t46
    294        param t47
    295        param lit
    296        param t49
    297        param t50
    298        call printf, 6
    299        avg[0] = 1.5
    300        avg[8] = 2.5
    301        avg[16] = 0.0
    302        t51 = avg[0]
    303        t52 = avg[8]
    304        t53 = t51 double+ t52
    305        t54 = t53 double/ 2.0
    306        avg[16] = t54
    307        t55 = avg[16]
    308        param "%.2f\n"
    309        param t55
    310        call printf, 2
    311        i = 2
    312        t56 = i int* 4                      (w = 4)
    313        t57 = i int- 1
    314        t58 = t57 int* 4                    (w = 4)
    315        t59 = a[t58]
    316        t60 = i int+ 1
    317        t61 = t60 int* 4                    (w = 4)
    318        t62 = a[t61]
    319        t63 = t59 int+ t62
    320        a[t56] = t63
    321        t64 = a[0]
    322        t65 = t64 int* 4                    (w = 4)
    323        t66 = a[t65]
    324        t67 = t66 int+ 10
    325        a[t65] = t67
    326        t68 = a[8]
    327        t69 = a[4]
    328        param "%d %d\n"
    329        param t68
    330        param t69
    331        call printf, 3
    332        t70 = &a
    333        t71 = t70 ptr+ 4
    334        t72 = *t71
    335        t73 = "literal" ptr+ 2
    336        t74 = *t73
    337        t75 = chartoint t74
    338        t76 = &word
    339        t77 = *t76
    340        t78 = chartoint t77
    341        param "%d %c %c\n"
    342        param t72
    343        param t75
    344        param t78
    345        call printf, 4
    346        t79 = m[16]
    347        return t79


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
