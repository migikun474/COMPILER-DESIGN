============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_algorithms.c
   Optimization  : no optimization
   Result        : Three address code generated: 6 function(s), 358 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION bubble(int *, int)        (link name _Z6bubblePii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 23 temporaries, frame 112 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   t                local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int *                           4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int *                           4      48
   t9               temp    int                             4      52
   t10              temp    int                             4      56
   t11              temp    int *                           4      60
   t12              temp    int                             4      64
   t13              temp    int                             4      68
   t14              temp    int *                           4      72
   t15              temp    int                             4      76
   t16              temp    int                             4      80
   t17              temp    int *                           4      84
   t18              temp    int                             4      88
   t19              temp    int                             4      92
   t20              temp    int                             4      96
   t21              temp    int *                           4     100
   t22              temp    int                             4     104
   t23              temp    int                             4     108

 Code: 39 instruction(s)

    100       i = 0
    101  L1:  if i int< n goto L2
    102       goto L8
    103  L2:  j = 0
    104  L3:  t1 = j int+ 1
    105       t2 = n int- i
    106       if t1 int< t2 goto L4
    107       goto L7
    108  L4:  t3 = j int* 4
    109       t4 = a ptr+ t3
    110       t5 = *t4
    111       t6 = j int+ 1
    112       t7 = t6 int* 4
    113       t8 = a ptr+ t7
    114       t9 = *t8
    115       if t5 int> t9 goto L5
    116       goto L6
    117  L5:  t10 = j int* 4
    118       t11 = a ptr+ t10
    119       t12 = *t11
    120       t = t12
    121       t13 = j int* 4
    122       t14 = a ptr+ t13
    123       t15 = j int+ 1
    124       t16 = t15 int* 4
    125       t17 = a ptr+ t16
    126       t18 = *t17
    127       *t14 = t18
    128       t19 = j int+ 1
    129       t20 = t19 int* 4
    130       t21 = a ptr+ t20
    131       *t21 = t
    132  L6:  t22 = j int+ 1
    133       j = t22
    134       goto L3
    135  L7:  t23 = i int+ 1
    136       i = t23
    137       goto L1
    138  L8:  return

============================================================================
 FUNCTION quick(int *, int, int)        (link name _Z5quickPiii)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 25 temporaries, frame 128 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   lo               param   int                             4       4
   hi               param   int                             4       8
   p                local   int                             4      12
   i                local   int                             4      16
   j                local   int                             4      20
   t                local   int                             4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int *                           4      40
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t7               temp    int *                           4      52
   t8               temp    int                             4      56
   t9               temp    int                             4      60
   t10              temp    int                             4      64
   t11              temp    int *                           4      68
   t12              temp    int                             4      72
   t13              temp    int                             4      76
   t14              temp    int                             4      80
   t15              temp    int *                           4      84
   t16              temp    int                             4      88
   t17              temp    int                             4      92
   t18              temp    int *                           4      96
   t19              temp    int                             4     100
   t20              temp    int *                           4     104
   t21              temp    int                             4     108
   t22              temp    int                             4     112
   t23              temp    int *                           4     116
   t24              temp    int                             4     120
   t25              temp    int                             4     124

 Code: 58 instruction(s)

    139        if lo int>= hi goto L9
    140        goto L10
    141  L9:   return
    142  L10:  t1 = lo int+ hi
    143        t2 = t1 int/ 2
    144        t3 = t2 int* 4
    145        t4 = a ptr+ t3
    146        t5 = *t4
    147        p = t5
    148        i = lo
    149        j = hi
    150  L11:  if i int<= j goto L12
    151        goto L18
    152  L12:  t6 = i int* 4
    153        t7 = a ptr+ t6
    154        t8 = *t7
    155        if t8 int< p goto L13
    156        goto L14
    157  L13:  t9 = i int+ 1
    158        i = t9
    159        goto L12
    160  L14:  t10 = j int* 4
    161        t11 = a ptr+ t10
    162        t12 = *t11
    163        if t12 int> p goto L15
    164        goto L16
    165  L15:  t13 = j int- 1
    166        j = t13
    167        goto L14
    168  L16:  if i int<= j goto L17
    169        goto L11
    170  L17:  t14 = i int* 4
    171        t15 = a ptr+ t14
    172        t16 = *t15
    173        t = t16
    174        t17 = i int* 4
    175        t18 = a ptr+ t17
    176        t19 = j int* 4
    177        t20 = a ptr+ t19
    178        t21 = *t20
    179        *t18 = t21
    180        t22 = j int* 4
    181        t23 = a ptr+ t22
    182        *t23 = t
    183        t24 = i int+ 1
    184        i = t24
    185        t25 = j int- 1
    186        j = t25
    187        goto L11
    188  L18:  param a
    189        param lo
    190        param j
    191        call quick(int *, int, int), 3
    192        param a
    193        param i
    194        param hi
    195        call quick(int *, int, int), 3
    196        return

============================================================================
 FUNCTION find(int *, int, int)        (link name _Z4findPiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 12 temporaries, frame 72 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   k                param   int                             4       8
   lo               local   int                             4      12
   hi               local   int                             4      16
   m                local   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int *                           4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    int *                           4      52
   t9               temp    int                             4      56
   t10              temp    int                             4      60
   t11              temp    int                             4      64
   t12              temp    int                             4      68

 Code: 27 instruction(s)

    197        lo = 0
    198        t1 = n int- 1
    199        hi = t1
    200  L19:  if lo int<= hi goto L20
    201        goto L25
    202  L20:  t2 = lo int+ hi
    203        t3 = t2 int/ 2
    204        m = t3
    205        t4 = m int* 4
    206        t5 = a ptr+ t4
    207        t6 = *t5
    208        if t6 int== k goto L21
    209        goto L22
    210  L21:  return m
    211  L22:  t7 = m int* 4
    212        t8 = a ptr+ t7
    213        t9 = *t8
    214        if t9 int< k goto L23
    215        goto L24
    216  L23:  t10 = m int+ 1
    217        lo = t10
    218        goto L19
    219  L24:  t11 = m int- 1
    220        hi = t11
    221        goto L19
    222  L25:  t12 = int- 1
    223        return t12

============================================================================
 FUNCTION hanoi(int)        (link name _Z5hanoii)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 11 instruction(s)

    224        if n int== 0 goto L26
    225        goto L27
    226  L26:  t1 = 0
    227        goto L28
    228  L27:  t2 = n int- 1
    229        param t2
    230        t3 = call hanoi(int), 1
    231        t4 = 2 int* t3
    232        t5 = t4 int+ 1
    233        t1 = t5
    234  L28:  return t1

============================================================================
 FUNCTION ack(int, int)        (link name _Z3ackii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 9 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   int                             4       0
   n                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   t8               temp    int                             4      36
   t9               temp    int                             4      40

 Code: 24 instruction(s)

    235        if m int== 0 goto L29
    236        goto L30
    237  L29:  t2 = n int+ 1
    238        t1 = t2
    239        goto L34
    240  L30:  if n int== 0 goto L31
    241        goto L32
    242  L31:  t4 = m int- 1
    243        param t4
    244        param 1
    245        t5 = call ack(int, int), 2
    246        t3 = t5
    247        goto L33
    248  L32:  t6 = m int- 1
    249        t7 = n int- 1
    250        param m
    251        param t7
    252        t8 = call ack(int, int), 2
    253        param t6
    254        param t8
    255        t9 = call ack(int, int), 2
    256        t3 = t9
    257  L33:  t1 = t3
    258  L34:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 60 temporaries, frame 448 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int[8]                         32       0
   b                local   int[8]                         32      32
   i                local   int                             4      64
   j                local   int                             4      68
   k                local   int                             4      72
   m1               local   int[2][2]                      16      76
   m2               local   int[2][2]                      16      92
   p                local   int[2][2]                      16     108
   sieve            local   char[50]                       50     124
   primes           local   int                             4     176
   text             local   char[12]                       12     180
   t                local   char                            1     192
   n                local   int                             4     196
   v                local   int                             4     200
   num              local   char[8]                         8     204
   t1               temp    int *                           4     212
   t2               temp    int *                           4     216
   t3               temp    int                             4     220
   t4               temp    int                             4     224
   t5               temp    int                             4     228
   t6               temp    int                             4     232
   t7               temp    int *                           4     236
   t8               temp    int                             4     240
   t9               temp    int *                           4     244
   t10              temp    int                             4     248
   t11              temp    int                             4     252
   t12              temp    int                             4     256
   t13              temp    int                             4     260
   t14              temp    int                             4     264
   t15              temp    int                             4     268
   t16              temp    int                             4     272
   t17              temp    int                             4     276
   t18              temp    int                             4     280
   t19              temp    int                             4     284
   t20              temp    int                             4     288
   t21              temp    int                             4     292
   t22              temp    int                             4     296
   t23              temp    int                             4     300
   t24              temp    int                             4     304
   t25              temp    int                             4     308
   t26              temp    int                             4     312
   t27              temp    int                             4     316
   t28              temp    int                             4     320
   t29              temp    int                             4     324
   t30              temp    int                             4     328
   t31              temp    int                             4     332
   t32              temp    int                             4     336
   t33              temp    int                             4     340
   t34              temp    int                             4     344
   t35              temp    int                             4     348
   t36              temp    int                             4     352
   t37              temp    int                             4     356
   t38              temp    char                            1     360
   t39              temp    int                             4     364
   t40              temp    int                             4     368
   t41              temp    int                             4     372
   t42              temp    int                             4     376
   t43              temp    char                            1     380
   t44              temp    char                            1     381
   t45              temp    int                             4     384
   t46              temp    int                             4     388
   t47              temp    int                             4     392
   t48              temp    int                             4     396
   t49              temp    int                             4     400
   t50              temp    int                             4     404
   t51              temp    char                            1     408
   t52              temp    int                             4     412
   t53              temp    int                             4     416
   t54              temp    int                             4     420
   t55              temp    char                            1     424
   t56              temp    int                             4     428
   t57              temp    int                             4     432
   t58              temp    int                             4     436
   t59              temp    int                             4     440
   t60              temp    char *                          4     444

 Code: 199 instruction(s)

    259        a[0] = 5
    260        a[4] = 2
    261        a[8] = 9
    262        a[12] = 1
    263        a[16] = 7
    264        a[20] = 3
    265        a[24] = 8
    266        a[28] = 6
    267        b[0] = 4
    268        b[4] = 0
    269        b[8] = 3
    270        b[12] = 9
    271        b[16] = 1
    272        b[20] = 8
    273        b[24] = 2
    274        b[28] = 7
    275        t1 = &a
    276        param t1
    277        param 8
    278        call bubble(int *, int), 2
    279        t2 = &b
    280        param t2
    281        param 0
    282        param 7
    283        call quick(int *, int, int), 3
    284        t3 = a[0]
    285        t4 = a[28]
    286        t5 = b[0]
    287        t6 = b[28]
    288        t7 = &a
    289        param t7
    290        param 8
    291        param 7
    292        t8 = call find(int *, int, int), 3
    293        t9 = &a
    294        param t9
    295        param 8
    296        param 4
    297        t10 = call find(int *, int, int), 3
    298        param "%d %d %d %d %d %d\n"
    299        param t3
    300        param t4
    301        param t5
    302        param t6
    303        param t8
    304        param t10
    305        call printf, 7
    306        param 10
    307        t11 = call hanoi(int), 1
    308        param 2
    309        param 3
    310        t12 = call ack(int, int), 2
    311        param "%d %d\n"
    312        param t11
    313        param t12
    314        call printf, 3
    315        m1[0] = 1
    316        m1[4] = 2
    317        m1[8] = 3
    318        m1[12] = 4
    319        m2[0] = 5
    320        m2[4] = 6
    321        m2[8] = 7
    322        m2[12] = 8
    323        i = 0
    324  L35:  if i int< 2 goto L36
    325        goto L43
    326  L36:  j = 0
    327  L37:  if j int< 2 goto L38
    328        goto L42
    329  L38:  t13 = i int* 2                      (n2 = 2)
    330        t14 = t13 int+ j
    331        t15 = t14 int* 4                    (w = 4)
    332        p[t15] = 0
    333        k = 0
    334  L39:  if k int< 2 goto L40
    335        goto L41
    336  L40:  t16 = i int* 2                      (n2 = 2)
    337        t17 = t16 int+ j
    338        t18 = t17 int* 4                    (w = 4)
    339        t19 = p[t18]
    340        t20 = i int* 2                      (n2 = 2)
    341        t21 = t20 int+ k
    342        t22 = t21 int* 4                    (w = 4)
    343        t23 = m1[t22]
    344        t24 = k int* 2                      (n2 = 2)
    345        t25 = t24 int+ j
    346        t26 = t25 int* 4                    (w = 4)
    347        t27 = m2[t26]
    348        t28 = t23 int* t27
    349        t29 = t19 int+ t28
    350        p[t18] = t29
    351        t30 = k int+ 1
    352        k = t30
    353        goto L39
    354  L41:  t31 = j int+ 1
    355        j = t31
    356        goto L37
    357  L42:  t32 = i int+ 1
    358        i = t32
    359        goto L35
    360  L43:  t33 = p[0]
    361        t34 = p[4]
    362        t35 = p[8]
    363        t36 = p[12]
    364        param "%d %d %d %d\n"
    365        param t33
    366        param t34
    367        param t35
    368        param t36
    369        call printf, 5
    370        primes = 0
    371        i = 0
    372  L44:  if i int< 50 goto L45
    373        goto L46
    374  L45:  sieve[i] = 1
    375        t37 = i int+ 1
    376        i = t37
    377        goto L44
    378  L46:  i = 2
    379  L47:  if i int< 50 goto L48
    380        goto L53
    381  L48:  t38 = sieve[i]
    382        if t38 char!= 0 goto L49
    383        goto L52
    384  L49:  t39 = primes int+ 1
    385        primes = t39
    386        t40 = i int* i
    387        j = t40
    388  L50:  if j int< 50 goto L51
    389        goto L52
    390  L51:  sieve[j] = 0
    391        t41 = j int+ i
    392        j = t41
    393        goto L50
    394  L52:  t42 = i int+ 1
    395        i = t42
    396        goto L47
    397  L53:  text[0] = 99
    398        text[1] = 111
    399        text[2] = 109
    400        text[3] = 112
    401        text[4] = 105
    402        text[5] = 108
    403        text[6] = 101
    404        text[7] = 114
    405        text[8] = 0
    406        text[9] = 0
    407        text[10] = 0
    408        text[11] = 0
    409        i = 0
    410        j = 7
    411  L54:  if i int< j goto L55
    412        goto L56
    413  L55:  t43 = text[i]
    414        t = t43
    415        t44 = text[j]
    416        text[i] = t44
    417        text[j] = t
    418        t45 = i int+ 1
    419        i = t45
    420        t46 = j int- 1
    421        j = t46
    422        goto L54
    423  L56:  n = 9081
    424        v = 0
    425        k = 0
    426  L57:  if n int!= 0 goto L58
    427        goto L59
    428  L58:  t47 = k
    429        t48 = k int+ 1
    430        k = t48
    431        t49 = n int% 10
    432        t50 = 48 int+ t49
    433        t51 = inttochar t50
    434        num[t47] = t51
    435        t52 = n int/ 10
    436        n = t52
    437        goto L57
    438  L59:  t53 = k int- 1
    439        i = t53
    440  L60:  if i int>= 0 goto L61
    441        goto L62
    442  L61:  t54 = v int* 10
    443        t55 = num[i]
    444        t56 = chartoint t55
    445        t57 = t56 int- 48
    446        t58 = t54 int+ t57
    447        v = t58
    448        t59 = i int- 1
    449        i = t59
    450        goto L60
    451  L62:  t60 = &text
    452        param "%d %s %d\n"
    453        param primes
    454        param t60
    455        param v
    456        call printf, 4
    457        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   bubble             function      void (int *, int)          -           4    -    1  _Z6bubblePii; defined
   quick              function      void (int *, int, int)     -           5    -    3  _Z5quickPiii; defined
   find               function      int (int *, int, int)      -          11    -    2  _Z4findPiii; defined
   hanoi              function      int (int)                  -          12    -    2  _Z5hanoii; defined
   ack                function      int (int, int)             -          13    -    4  _Z3ackii; defined
   main               function      int (void)                 -          14    -    0  defined

 scope: global > bubble()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       4    4    6  a.1
   n                  parameter     int                        param       4    4    2  n.2
   i                  variable      int                        local       4    4    4  i.3
   j                  variable      int                        local       4    4    9  j.4

 scope: global > bubble() > for > for body > for > for body > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local       4    4    1  t.5

 scope: global > quick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       5    4    9  a.6
   lo                 parameter     int                        param       5    4    4  lo.7
   hi                 parameter     int                        param       5    4    4  hi.8
   p                  variable      int                        local       7    4    2  p.9
   i                  variable      int                        local       7    4    8  i.10
   j                  variable      int                        local       7    4    8  j.11

 scope: global > quick() > while > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local       8    4    1  t.12

 scope: global > find()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param      11    4    2  a.13
   n                  parameter     int                        param      11    4    1  n.14
   k                  parameter     int                        param      11    4    2  k.15
   lo                 variable      int                        local      11    4    3  lo.16
   hi                 variable      int                        local      11    4    3  hi.17

 scope: global > find() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  variable      int                        local      11    4    5  m.18

 scope: global > hanoi()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      12    4    2  n.19

 scope: global > ack()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int                        param      13    4    4  m.20
   n                  parameter     int                        param      13    4    3  n.21

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int[8]                     local      15   32    5  a.22
   b                  variable      int[8]                     local      15   32    3  b.23
   i                  variable      int                        local      15    4   26  i.24
   j                  variable      int                        local      15    4   15  j.25
   k                  variable      int                        local      15    4    8  k.26
   m1                 variable      int[2][2]                  local      19   16    1  m1.27
   m2                 variable      int[2][2]                  local      19   16    1  m2.28
   p                  variable      int[2][2]                  local      19   16    6  p.29
   sieve              variable      char[50]                   local      22   50    3  sieve.30
   primes             variable      int                        local      22    4    2  primes.31
   text               variable      char[12]                   local      25   12    5  text.32
   t                  variable      char                       local      25    1    2  t.33
   n                  variable      int                        local      27    4    3  n.34
   v                  variable      int                        local      27    4    3  v.35
   num                variable      char[8]                    local      27    8    2  num.36

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
