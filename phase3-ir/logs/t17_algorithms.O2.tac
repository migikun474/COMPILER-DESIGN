============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_algorithms.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 358 -> 288 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          358 -> 288   (19% fewer)

   constants folded                        1
   algebraic simplifications              24
   common subexpressions                  12
   copies / constants forwarded           17
   temporaries merged away                29
   dead instructions removed              13
   jumps removed or redirected            24
   unreachable instructions removed        0
   propagated across blocks                4
   dead assignments removed                4

============================================================================
 FUNCTION bubble(int *, int)        (link name _Z6bubblePii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 16 temporaries, frame 112 bytes

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
   t15              temp    int                             4      76
   t16              temp    int                             4      80
   t17              temp    int *                           4      84
   t18              temp    int                             4      88
   (7 temporaries no longer used after optimization not shown)

 Code: 28 instruction(s)

    100       i = 0
    101  L1:  if i int>= n goto L5
    102       j = 0
    103  L2:  t1 = j int+ 1
    104       t2 = n int- i
    105       if t1 int>= t2 goto L4
    106       t3 = j int<< 2
    107       t4 = a ptr+ t3
    108       t5 = *t4
    109       t6 = j int+ 1
    110       t7 = t6 int<< 2
    111       t8 = a ptr+ t7
    112       t9 = *t8
    113       if t5 int<= t9 goto L3
    114       t10 = j int<< 2
    115       t11 = a ptr+ t10
    116       t12 = *t11
    117       t15 = j int+ 1
    118       t16 = t15 int<< 2
    119       t17 = a ptr+ t16
    120       t18 = *t17
    121       *t11 = t18
    122       *t17 = t12
    123  L3:  j = j int+ 1
    124       goto L2
    125  L4:  i = i int+ 1
    126       goto L1
    127  L5:  return

============================================================================
 FUNCTION quick(int *, int, int)        (link name _Z5quickPiii)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 16 temporaries, frame 128 bytes

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
   t14              temp    int                             4      80
   t15              temp    int *                           4      84
   t16              temp    int                             4      88
   t19              temp    int                             4     100
   t20              temp    int *                           4     104
   t21              temp    int                             4     108
   (9 temporaries no longer used after optimization not shown)

 Code: 43 instruction(s)

    128        if lo int< hi goto L6
    129        return
    130  L6:   t1 = lo int+ hi
    131        t2 = t1 int/ 2
    132        t3 = t2 int<< 2
    133        t4 = a ptr+ t3
    134        p = *t4
    135        i = lo
    136        j = hi
    137  L7:   if i int> j goto L11
    138  L8:   t6 = i int<< 2
    139        t7 = a ptr+ t6
    140        t8 = *t7
    141        if t8 int>= p goto L9
    142        i = i int+ 1
    143        goto L8
    144  L9:   t10 = j int<< 2
    145        t11 = a ptr+ t10
    146        t12 = *t11
    147        if t12 int<= p goto L10
    148        j = j int- 1
    149        goto L9
    150  L10:  if i int> j goto L7
    151        t14 = i int<< 2
    152        t15 = a ptr+ t14
    153        t16 = *t15
    154        t19 = j int<< 2
    155        t20 = a ptr+ t19
    156        t21 = *t20
    157        *t15 = t21
    158        *t20 = t16
    159        i = i int+ 1
    160        j = j int- 1
    161        goto L7
    162  L11:  param a
    163        param lo
    164        param j
    165        call quick(int *, int, int), 3
    166        param a
    167        param i
    168        param hi
    169        call quick(int *, int, int), 3
    170        return

============================================================================
 FUNCTION find(int *, int, int)        (link name _Z4findPiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 8 temporaries, frame 72 bytes

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
   t7               temp    int                             4      48
   t8               temp    int *                           4      52
   t9               temp    int                             4      56
   (4 temporaries no longer used after optimization not shown)

 Code: 19 instruction(s)

    171        lo = 0
    172        hi = n int- 1
    173  L12:  if lo int> hi goto L15
    174        t2 = lo int+ hi
    175        t3 = t2 int/ 2
    176        t4 = t3 int<< 2
    177        t5 = a ptr+ t4
    178        t6 = *t5
    179        if t6 int!= k goto L13
    180        return t3
    181  L13:  t7 = t3 int<< 2
    182        t8 = a ptr+ t7
    183        t9 = *t8
    184        if t9 int>= k goto L14
    185        lo = t3 int+ 1
    186        goto L12
    187  L14:  hi = t3 int- 1
    188        goto L12
    189  L15:  return -1

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

    190        if n int!= 0 goto L16
    191        t1 = 0
    192        goto L17
    193  L16:  t2 = n int- 1
    194        param t2
    195        t3 = call hanoi(int), 1
    196        t4 = t3 int<< 1
    197        t1 = t4 int+ 1
    198  L17:  return t1

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

    199        if m int!= 0 goto L18
    200        t1 = n int+ 1
    201        goto L21
    202  L18:  if n int!= 0 goto L19
    203        t4 = m int- 1
    204        param t4
    205        param 1
    206        t3 = call ack(int, int), 2
    207        goto L20
    208  L19:  t6 = m int- 1
    209        t7 = n int- 1
    210        param m
    211        param t7
    212        t8 = call ack(int, int), 2
    213        param t6
    214        param t8
    215        t3 = call ack(int, int), 2
    216  L20:  t1 = t3
    217  L21:  return t1

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

 Code: 170 instruction(s)

    218        a[0] = 5
    219        a[4] = 2
    220        a[8] = 9
    221        a[12] = 1
    222        a[16] = 7
    223        a[20] = 3
    224        a[24] = 8
    225        a[28] = 6
    226        b[0] = 4
    227        b[4] = 0
    228        b[8] = 3
    229        b[12] = 9
    230        b[16] = 1
    231        b[20] = 8
    232        b[24] = 2
    233        b[28] = 7
    234        t1 = &a
    235        param t1
    236        param 8
    237        call bubble(int *, int), 2
    238        t2 = &b
    239        param t2
    240        param 0
    241        param 7
    242        call quick(int *, int, int), 3
    243        t3 = a[0]
    244        t4 = a[28]
    245        t5 = b[0]
    246        t6 = b[28]
    247        param t1
    248        param 8
    249        param 7
    250        t8 = call find(int *, int, int), 3
    251        param t1
    252        param 8
    253        param 4
    254        t10 = call find(int *, int, int), 3
    255        param "%d %d %d %d %d %d\n"
    256        param t3
    257        param t4
    258        param t5
    259        param t6
    260        param t8
    261        param t10
    262        call printf, 7
    263        param 10
    264        t11 = call hanoi(int), 1
    265        param 2
    266        param 3
    267        t12 = call ack(int, int), 2
    268        param "%d %d\n"
    269        param t11
    270        param t12
    271        call printf, 3
    272        m1[0] = 1
    273        m1[4] = 2
    274        m1[8] = 3
    275        m1[12] = 4
    276        m2[0] = 5
    277        m2[4] = 6
    278        m2[8] = 7
    279        m2[12] = 8
    280        i = 0
    281  L22:  if i int>= 2 goto L27
    282        j = 0
    283  L23:  if j int>= 2 goto L26
    284        t13 = i int<< 1                     (n2 = 2)
    285        t14 = t13 int+ j
    286        t15 = t14 int<< 2                   (w = 4)
    287        p[t15] = 0
    288        k = 0
    289  L24:  if k int>= 2 goto L25
    290        t16 = i int<< 1                     (n2 = 2)
    291        t17 = t16 int+ j
    292        t18 = t17 int<< 2                   (w = 4)
    293        t19 = p[t18]
    294        t21 = t16 int+ k
    295        t22 = t21 int<< 2                   (w = 4)
    296        t23 = m1[t22]
    297        t24 = k int<< 1                     (n2 = 2)
    298        t25 = t24 int+ j
    299        t26 = t25 int<< 2                   (w = 4)
    300        t27 = m2[t26]
    301        t28 = t23 int* t27
    302        t29 = t19 int+ t28
    303        p[t18] = t29
    304        k = k int+ 1
    305        goto L24
    306  L25:  j = j int+ 1
    307        goto L23
    308  L26:  i = i int+ 1
    309        goto L22
    310  L27:  t33 = p[0]
    311        t34 = p[4]
    312        t35 = p[8]
    313        t36 = p[12]
    314        param "%d %d %d %d\n"
    315        param t33
    316        param t34
    317        param t35
    318        param t36
    319        call printf, 5
    320        primes = 0
    321        i = 0
    322  L28:  if i int>= 50 goto L29
    323        sieve[i] = 1
    324        i = i int+ 1
    325        goto L28
    326  L29:  i = 2
    327  L30:  if i int>= 50 goto L33
    328        t38 = sieve[i]
    329        if t38 char== 0 goto L32
    330        primes = primes int+ 1
    331        j = i int* i
    332  L31:  if j int>= 50 goto L32
    333        sieve[j] = 0
    334        j = j int+ i
    335        goto L31
    336  L32:  i = i int+ 1
    337        goto L30
    338  L33:  text[0] = 99
    339        text[1] = 111
    340        text[2] = 109
    341        text[3] = 112
    342        text[4] = 105
    343        text[5] = 108
    344        text[6] = 101
    345        text[7] = 114
    346        text[8] = 0
    347        text[9] = 0
    348        text[10] = 0
    349        text[11] = 0
    350        i = 0
    351        j = 7
    352  L34:  if i int>= j goto L35
    353        t43 = text[i]
    354        t44 = text[j]
    355        text[i] = t44
    356        text[j] = t43
    357        i = i int+ 1
    358        j = j int- 1
    359        goto L34
    360  L35:  n = 9081
    361        v = 0
    362        k = 0
    363  L36:  if n int== 0 goto L37
    364        t47 = k
    365        k = k int+ 1
    366        t49 = n int% 10
    367        t50 = 48 int+ t49
    368        t51 = inttochar t50
    369        num[t47] = t51
    370        n = n int/ 10
    371        goto L36
    372  L37:  i = k int- 1
    373  L38:  if i int< 0 goto L39
    374        t54 = v int* 10
    375        t55 = num[i]
    376        t56 = chartoint t55
    377        t57 = t56 int- 48
    378        v = t54 int+ t57
    379        i = i int- 1
    380        goto L38
    381  L39:  t60 = &text
    382        param "%d %s %d\n"
    383        param primes
    384        param t60
    385        param v
    386        call printf, 4
    387        return 0


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
