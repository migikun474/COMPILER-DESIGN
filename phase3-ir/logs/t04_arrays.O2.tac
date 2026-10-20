============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 248 -> 214 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          248 -> 214   (13% fewer)

   constants folded                        6
   algebraic simplifications               7
   common subexpressions                   6
   copies / constants forwarded           17
   temporaries merged away                11
   dead instructions removed              12
   jumps removed or redirected             9
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   squares          int[5]                         20  0
   table            int[2][3]                      24  { +0: 1, +4: 2, +8: 3, +12: 4, +16: 5, +20: 6 }

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

 Symbol table: 13 parameter(s)/local(s), 61 temporaries, frame 600 bytes

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
   t46              temp    char (*)[6]                     4     444
   t47              temp    char (*)[8]                     4     448
   t49              temp    int                             4     456
   t50              temp    int                             4     460
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
   (18 temporaries no longer used after optimization not shown)

 Code: 185 instruction(s)

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
    144  L10:  if j int>= 3 goto L11
    145        t4 = i int* 3                       (n2 = 3)
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
    156  L14:  if j int>= 3 goto L17
    157        k = 0
    158  L15:  if k int>= 4 goto L16
    159        t11 = i int* 3                      (n2 = 3)
    160        t12 = t11 int+ j
    161        t13 = t12 int<< 2                   (n3 = 4)
    162        t14 = t13 int+ k
    163        t15 = t14 int<< 2                   (w = 4)
    164        t16 = i int* 100
    165        t17 = j int* 10
    166        t18 = t16 int+ t17
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
    180        param t27
    181        param 5
    182        t28 = call total(int *, int), 2
    183        param "%d %d %d %d %d\n"
    184        param t23
    185        param t24
    186        param t25
    187        param t26
    188        param t28
    189        call printf, 6
    190        t29 = squares[16]
    191        t30 = &squares
    192        param t30
    193        param 5
    194        t31 = call total(int *, int), 2
    195        t32 = &m
    196        param t32
    197        param 3
    198        t33 = call trace(int (*)[3], int), 2
    199        param "%d %d %d\n"
    200        param t29
    201        param t31
    202        param t33
    203        call printf, 4
    204        t34 = cube[92]
    205        t35 = cube[24]
    206        t36 = m[28]
    207        param "%d %d %d\n"
    208        param t34
    209        param t35
    210        param t36
    211        call printf, 4
    212        t37 = table[20]
    213        t38 = table[4]
    214        t39 = table[12]
    215        t40 = t38 int+ t39
    216        param "%d %d\n"
    217        param t37
    218        param t40
    219        call printf, 3
    220        flat[0] = 1
    221        flat[4] = 2
    222        flat[8] = 3
    223        flat[12] = 4
    224        sparse[0] = 0
    225        sparse[4] = 7
    226        sparse[8] = 0
    227        sparse[12] = 0
    228        sparse[16] = 9
    229        sparse[20] = 0
    230        sized[0] = 5
    231        sized[4] = 6
    232        sized[8] = 7
    233        sized[12] = 8
    234        t41 = flat[8]
    235        t42 = sparse[4]
    236        t43 = sparse[16]
    237        t44 = sparse[20]
    238        param "%d %d %d %d %d\n"
    239        param t41
    240        param t42
    241        param t43
    242        param t44
    243        param 4
    244        call printf, 6
    245        word[0] = 104
    246        word[1] = 101
    247        word[2] = 108
    248        word[3] = 108
    249        word[4] = 111
    250        word[5] = 0
    251        buf[0] = 97
    252        buf[1] = 98
    253        buf[2] = 0
    254        buf[3] = 0
    255        buf[4] = 0
    256        buf[5] = 0
    257        buf[6] = 0
    258        buf[7] = 0
    259        word[0] = 106
    260        buf[2] = 99
    261        t46 = &word
    262        t47 = &buf
    263        param t46
    264        t49 = call length(char *), 1
    265        param "wide world"
    266        t50 = call length(char *), 1
    267        param "%s %s %s %d %d\n"
    268        param t46
    269        param t47
    270        param "wide world"
    271        param t49
    272        param t50
    273        call printf, 6
    274        avg[0] = 1.5
    275        avg[8] = 2.5
    276        avg[16] = 0.0
    277        t51 = avg[0]
    278        t52 = avg[8]
    279        t53 = t51 double+ t52
    280        t54 = t53 double/ 2.0
    281        avg[16] = t54
    282        param "%.2f\n"
    283        param t54
    284        call printf, 2
    285        t59 = a[4]
    286        t62 = a[12]
    287        t63 = t59 int+ t62
    288        a[8] = t63
    289        t64 = a[0]
    290        t65 = t64 int<< 2                   (w = 4)
    291        t66 = a[t65]
    292        t67 = t66 int+ 10
    293        a[t65] = t67
    294        t68 = a[8]
    295        t69 = a[4]
    296        param "%d %d\n"
    297        param t68
    298        param t69
    299        call printf, 3
    300        t71 = t27 ptr+ 4
    301        t72 = *t71
    302        t73 = "literal" ptr+ 2
    303        t74 = *t73
    304        t75 = chartoint t74
    305        t77 = *t46
    306        t78 = chartoint t77
    307        param "%d %c %c\n"
    308        param t72
    309        param t75
    310        param t78
    311        call printf, 4
    312        t79 = m[16]
    313        return t79


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
