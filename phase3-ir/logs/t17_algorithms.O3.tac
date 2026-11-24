============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_algorithms.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 358 -> 342 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          358 -> 342   (4% fewer)

   constants folded                        1
   algebraic simplifications              24
   common subexpressions                  12
   copies / constants forwarded           36
   temporaries merged away                29
   dead instructions removed              29
   jumps removed or redirected            24
   unreachable instructions removed        1
   propagated across blocks                5
   dead assignments removed                5
   calls inlined                           0
   tail calls turned into jumps            1
   common subexpressions across blocks     12
   loops unrolled                          9
   unreachable functions removed           0

============================================================================
 FUNCTION bubble(int *, int)        (link name _Z6bubblePii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 10 temporaries, frame 112 bytes

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
   t7               temp    int                             4      44
   t8               temp    int *                           4      48
   t9               temp    int                             4      52
   t12              temp    int                             4      64
   t18              temp    int                             4      88
   (13 temporaries no longer used after optimization not shown)

 Code: 37 instruction(s)

    100       i = 0
    101  L1:  if i int>= n goto L6
    102       j = 0
    103  L2:  t1 = j int+ 1
    104       t2 = n int- i
    105       if t1 int>= t2 goto L5
    106       t3 = j int<< 2
    107       t4 = a ptr+ t3
    108       t5 = *t4
    109       t7 = t1 int<< 2
    110       t8 = a ptr+ t7
    111       t9 = *t8
    112       if t5 int<= t9 goto L3
    113       t12 = *t4
    114       t18 = *t8
    115       *t4 = t18
    116       *t8 = t12
    117  L3:  j = j int+ 1
    118       t1 = j int+ 1
    119       t2 = n int- i
    120       if t1 int>= t2 goto L5
    121       t3 = j int<< 2
    122       t4 = a ptr+ t3
    123       t5 = *t4
    124       t7 = t1 int<< 2
    125       t8 = a ptr+ t7
    126       t9 = *t8
    127       if t5 int<= t9 goto L4
    128       t12 = *t4
    129       t18 = *t8
    130       *t4 = t18
    131       *t8 = t12
    132  L4:  j = j int+ 1
    133       goto L2
    134  L5:  i = i int+ 1
    135       goto L1
    136  L6:  return

============================================================================
 FUNCTION quick(int *, int, int)        (link name _Z5quickPiii)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 12 temporaries, frame 140 bytes

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
   t6               temp    int                             4      48
   t7               temp    int *                           4      52
   t8               temp    int                             4      56
   t10              temp    int                             4      64
   t11              temp    int *                           4      68
   t12              temp    int                             4      72
   t16              temp    int                             4      88
   t21              temp    int                             4     108
   (16 temporaries no longer used after optimization not shown)

 Code: 46 instruction(s)

    137  L7:   if lo int< hi goto L8
    138        return
    139  L8:   t1 = lo int+ hi
    140        t2 = t1 int/ 2
    141        t3 = t2 int<< 2
    142        t4 = a ptr+ t3
    143        p = *t4
    144        i = lo
    145        j = hi
    146  L9:   if i int> j goto L13
    147  L10:  t6 = i int<< 2
    148        t7 = a ptr+ t6
    149        t8 = *t7
    150        if t8 int>= p goto L11
    151        i = i int+ 1
    152        t6 = i int<< 2
    153        t7 = a ptr+ t6
    154        t8 = *t7
    155        if t8 int>= p goto L11
    156        i = i int+ 1
    157        goto L10
    158  L11:  t10 = j int<< 2
    159        t11 = a ptr+ t10
    160        t12 = *t11
    161        if t12 int<= p goto L12
    162        j = j int- 1
    163        t10 = j int<< 2
    164        t11 = a ptr+ t10
    165        t12 = *t11
    166        if t12 int<= p goto L12
    167        j = j int- 1
    168        goto L11
    169  L12:  if i int> j goto L9
    170        t16 = *t7
    171        t21 = *t11
    172        *t7 = t21
    173        *t11 = t16
    174        i = i int+ 1
    175        j = j int- 1
    176        goto L9
    177  L13:  param a
    178        param lo
    179        param j
    180        call quick(int *, int, int), 3
    181        lo = i
    182        goto L7

============================================================================
 FUNCTION find(int *, int, int)        (link name _Z4findPiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 6 temporaries, frame 72 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   k                param   int                             4       8
   lo               local   int                             4      12
   hi               local   int                             4      16
   m                local   int                             4      20
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int *                           4      40
   t6               temp    int                             4      44
   t9               temp    int                             4      56
   (6 temporaries no longer used after optimization not shown)

 Code: 17 instruction(s)

    183        lo = 0
    184        hi = n int- 1
    185  L14:  if lo int> hi goto L17
    186        t2 = lo int+ hi
    187        t3 = t2 int/ 2
    188        t4 = t3 int<< 2
    189        t5 = a ptr+ t4
    190        t6 = *t5
    191        if t6 int!= k goto L15
    192        return t3
    193  L15:  t9 = *t5
    194        if t9 int>= k goto L16
    195        lo = t3 int+ 1
    196        goto L14
    197  L16:  hi = t3 int- 1
    198        goto L14
    199  L17:  return -1

============================================================================
 FUNCTION hanoi(int)        (link name _Z5hanoii)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 9 instruction(s)

    200        if n int!= 0 goto L18
    201        t1 = 0
    202        goto L19
    203  L18:  t2 = n int- 1
    204        param t2
    205        t3 = call hanoi(int), 1
    206        t4 = t3 int<< 1
    207        t1 = t4 int+ 1
    208  L19:  return t1

============================================================================
 FUNCTION ack(int, int)        (link name _Z3ackii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   int                             4       0
   n                param   int                             4       4
   t1               temp    int                             4       8
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   t8               temp    int                             4      36
   (3 temporaries no longer used after optimization not shown)

 Code: 19 instruction(s)

    209        if m int!= 0 goto L20
    210        t1 = n int+ 1
    211        goto L23
    212  L20:  if n int!= 0 goto L21
    213        t4 = m int- 1
    214        param t4
    215        param 1
    216        t3 = call ack(int, int), 2
    217        goto L22
    218  L21:  t6 = m int- 1
    219        t7 = n int- 1
    220        param m
    221        param t7
    222        t8 = call ack(int, int), 2
    223        param t6
    224        param t8
    225        t3 = call ack(int, int), 2
    226  L22:  t1 = t3
    227  L23:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 42 temporaries, frame 448 bytes

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
   t8               temp    int                             4     240
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
   t21              temp    int                             4     292
   t22              temp    int                             4     296
   t23              temp    int                             4     300
   t24              temp    int                             4     304
   t25              temp    int                             4     308
   t26              temp    int                             4     312
   t27              temp    int                             4     316
   t28              temp    int                             4     320
   t29              temp    int                             4     324
   t33              temp    int                             4     340
   t34              temp    int                             4     344
   t35              temp    int                             4     348
   t36              temp    int                             4     352
   t38              temp    char                            1     360
   t43              temp    char                            1     380
   t44              temp    char                            1     381
   t47              temp    int                             4     392
   t49              temp    int                             4     400
   t50              temp    int                             4     404
   t51              temp    char                            1     408
   t54              temp    int                             4     420
   t55              temp    char                            1     424
   t56              temp    int                             4     428
   t57              temp    int                             4     432
   t60              temp    char *                          4     444
   (18 temporaries no longer used after optimization not shown)

 Code: 214 instruction(s)

    228        a[0] = 5
    229        a[4] = 2
    230        a[8] = 9
    231        a[12] = 1
    232        a[16] = 7
    233        a[20] = 3
    234        a[24] = 8
    235        a[28] = 6
    236        b[0] = 4
    237        b[4] = 0
    238        b[8] = 3
    239        b[12] = 9
    240        b[16] = 1
    241        b[20] = 8
    242        b[24] = 2
    243        b[28] = 7
    244        t1 = &a
    245        param t1
    246        param 8
    247        call bubble(int *, int), 2
    248        t2 = &b
    249        param t2
    250        param 0
    251        param 7
    252        call quick(int *, int, int), 3
    253        t3 = a[0]
    254        t4 = a[28]
    255        t5 = b[0]
    256        t6 = b[28]
    257        param t1
    258        param 8
    259        param 7
    260        t8 = call find(int *, int, int), 3
    261        param t1
    262        param 8
    263        param 4
    264        t10 = call find(int *, int, int), 3
    265        param "%d %d %d %d %d %d\n"
    266        param t3
    267        param t4
    268        param t5
    269        param t6
    270        param t8
    271        param t10
    272        call printf, 7
    273        param 10
    274        t11 = call hanoi(int), 1
    275        param 2
    276        param 3
    277        t12 = call ack(int, int), 2
    278        param "%d %d\n"
    279        param t11
    280        param t12
    281        call printf, 3
    282        m1[0] = 1
    283        m1[4] = 2
    284        m1[8] = 3
    285        m1[12] = 4
    286        m2[0] = 5
    287        m2[4] = 6
    288        m2[8] = 7
    289        m2[12] = 8
    290        i = 0
    291  L24:  if i int>= 2 goto L29
    292        j = 0
    293  L25:  if j int>= 2 goto L28
    294        t13 = i int<< 1                     (n2 = 2)
    295        t14 = t13 int+ j
    296        t15 = t14 int<< 2                   (w = 4)
    297        p[t15] = 0
    298        k = 0
    299  L26:  if k int>= 2 goto L27
    300        t16 = i int<< 1                     (n2 = 2)
    301        t17 = t16 int+ j
    302        t18 = t17 int<< 2                   (w = 4)
    303        t19 = p[t18]
    304        t21 = t16 int+ k
    305        t22 = t21 int<< 2                   (w = 4)
    306        t23 = m1[t22]
    307        t24 = k int<< 1                     (n2 = 2)
    308        t25 = t24 int+ j
    309        t26 = t25 int<< 2                   (w = 4)
    310        t27 = m2[t26]
    311        t28 = t23 int* t27
    312        t29 = t19 int+ t28
    313        p[t18] = t29
    314        k = k int+ 1
    315        if k int>= 2 goto L27
    316        t16 = i int<< 1                     (n2 = 2)
    317        t17 = t16 int+ j
    318        t18 = t17 int<< 2                   (w = 4)
    319        t19 = p[t18]
    320        t21 = t16 int+ k
    321        t22 = t21 int<< 2                   (w = 4)
    322        t23 = m1[t22]
    323        t24 = k int<< 1                     (n2 = 2)
    324        t25 = t24 int+ j
    325        t26 = t25 int<< 2                   (w = 4)
    326        t27 = m2[t26]
    327        t28 = t23 int* t27
    328        t29 = t19 int+ t28
    329        p[t18] = t29
    330        k = k int+ 1
    331        goto L26
    332  L27:  j = j int+ 1
    333        goto L25
    334  L28:  i = i int+ 1
    335        goto L24
    336  L29:  t33 = p[0]
    337        t34 = p[4]
    338        t35 = p[8]
    339        t36 = p[12]
    340        param "%d %d %d %d\n"
    341        param t33
    342        param t34
    343        param t35
    344        param t36
    345        call printf, 5
    346        primes = 0
    347        i = 0
    348  L30:  if i int>= 50 goto L31
    349        sieve[i] = 1
    350        i = i int+ 1
    351        if i int>= 50 goto L31
    352        sieve[i] = 1
    353        i = i int+ 1
    354        goto L30
    355  L31:  i = 2
    356  L32:  if i int>= 50 goto L35
    357        t38 = sieve[i]
    358        if t38 char== 0 goto L34
    359        primes = primes int+ 1
    360        j = i int* i
    361  L33:  if j int>= 50 goto L34
    362        sieve[j] = 0
    363        j = j int+ i
    364        if j int>= 50 goto L34
    365        sieve[j] = 0
    366        j = j int+ i
    367        goto L33
    368  L34:  i = i int+ 1
    369        goto L32
    370  L35:  text[0] = 99
    371        text[1] = 111
    372        text[2] = 109
    373        text[3] = 112
    374        text[4] = 105
    375        text[5] = 108
    376        text[6] = 101
    377        text[7] = 114
    378        text[8] = 0
    379        text[9] = 0
    380        text[10] = 0
    381        text[11] = 0
    382        i = 0
    383        j = 7
    384  L36:  if i int>= j goto L37
    385        t43 = text[i]
    386        t44 = text[j]
    387        text[i] = t44
    388        text[j] = t43
    389        i = i int+ 1
    390        j = j int- 1
    391        if i int>= j goto L37
    392        t43 = text[i]
    393        t44 = text[j]
    394        text[i] = t44
    395        text[j] = t43
    396        i = i int+ 1
    397        j = j int- 1
    398        goto L36
    399  L37:  n = 9081
    400        v = 0
    401        k = 0
    402  L38:  if n int== 0 goto L39
    403        t47 = k
    404        k = k int+ 1
    405        t49 = n int% 10
    406        t50 = 48 int+ t49
    407        t51 = inttochar t50
    408        num[t47] = t51
    409        n = n int/ 10
    410        if n int== 0 goto L39
    411        t47 = k
    412        k = k int+ 1
    413        t49 = n int% 10
    414        t50 = 48 int+ t49
    415        t51 = inttochar t50
    416        num[t47] = t51
    417        n = n int/ 10
    418        goto L38
    419  L39:  i = k int- 1
    420  L40:  if i int< 0 goto L41
    421        t54 = v int* 10
    422        t55 = num[i]
    423        t56 = chartoint t55
    424        t57 = t56 int- 48
    425        v = t54 int+ t57
    426        i = i int- 1
    427        if i int< 0 goto L41
    428        t54 = v int* 10
    429        t55 = num[i]
    430        t56 = chartoint t55
    431        t57 = t56 int- 48
    432        v = t54 int+ t57
    433        i = i int- 1
    434        goto L40
    435  L41:  t60 = &text
    436        param "%d %s %d\n"
    437        param primes
    438        param t60
    439        param v
    440        call printf, 4
    441        return 0


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
