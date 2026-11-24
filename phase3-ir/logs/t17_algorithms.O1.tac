============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_algorithms.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 358 -> 292 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          358 -> 292   (18% fewer)

   calls inlined                           0
   constants folded                        1
   algebraic simplifications              24
   common subexpressions                  12
   copies / constants forwarded           17
   temporaries merged away                29
   dead instructions removed              13
   jumps removed or redirected            24
   unreachable instructions removed        0

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

 Code: 29 instruction(s)

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
    117       t = t12
    118       t15 = j int+ 1
    119       t16 = t15 int<< 2
    120       t17 = a ptr+ t16
    121       t18 = *t17
    122       *t11 = t18
    123       *t17 = t12
    124  L3:  j = j int+ 1
    125       goto L2
    126  L4:  i = i int+ 1
    127       goto L1
    128  L5:  return

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

 Code: 44 instruction(s)

    129        if lo int< hi goto L6
    130        return
    131  L6:   t1 = lo int+ hi
    132        t2 = t1 int/ 2
    133        t3 = t2 int<< 2
    134        t4 = a ptr+ t3
    135        p = *t4
    136        i = lo
    137        j = hi
    138  L7:   if i int> j goto L11
    139  L8:   t6 = i int<< 2
    140        t7 = a ptr+ t6
    141        t8 = *t7
    142        if t8 int>= p goto L9
    143        i = i int+ 1
    144        goto L8
    145  L9:   t10 = j int<< 2
    146        t11 = a ptr+ t10
    147        t12 = *t11
    148        if t12 int<= p goto L10
    149        j = j int- 1
    150        goto L9
    151  L10:  if i int> j goto L7
    152        t14 = i int<< 2
    153        t15 = a ptr+ t14
    154        t16 = *t15
    155        t = t16
    156        t19 = j int<< 2
    157        t20 = a ptr+ t19
    158        t21 = *t20
    159        *t15 = t21
    160        *t20 = t16
    161        i = i int+ 1
    162        j = j int- 1
    163        goto L7
    164  L11:  param a
    165        param lo
    166        param j
    167        call quick(int *, int, int), 3
    168        param a
    169        param i
    170        param hi
    171        call quick(int *, int, int), 3
    172        return

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

 Code: 20 instruction(s)

    173        lo = 0
    174        hi = n int- 1
    175  L12:  if lo int> hi goto L15
    176        t2 = lo int+ hi
    177        t3 = t2 int/ 2
    178        m = t3
    179        t4 = t3 int<< 2
    180        t5 = a ptr+ t4
    181        t6 = *t5
    182        if t6 int!= k goto L13
    183        return m
    184  L13:  t7 = m int<< 2
    185        t8 = a ptr+ t7
    186        t9 = *t8
    187        if t9 int>= k goto L14
    188        lo = m int+ 1
    189        goto L12
    190  L14:  hi = m int- 1
    191        goto L12
    192  L15:  return -1

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

    193        if n int!= 0 goto L16
    194        t1 = 0
    195        goto L17
    196  L16:  t2 = n int- 1
    197        param t2
    198        t3 = call hanoi(int), 1
    199        t4 = t3 int<< 1
    200        t1 = t4 int+ 1
    201  L17:  return t1

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

    202        if m int!= 0 goto L18
    203        t1 = n int+ 1
    204        goto L21
    205  L18:  if n int!= 0 goto L19
    206        t4 = m int- 1
    207        param t4
    208        param 1
    209        t3 = call ack(int, int), 2
    210        goto L20
    211  L19:  t6 = m int- 1
    212        t7 = n int- 1
    213        param m
    214        param t7
    215        t8 = call ack(int, int), 2
    216        param t6
    217        param t8
    218        t3 = call ack(int, int), 2
    219  L20:  t1 = t3
    220  L21:  return t1

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

 Code: 171 instruction(s)

    221        a[0] = 5
    222        a[4] = 2
    223        a[8] = 9
    224        a[12] = 1
    225        a[16] = 7
    226        a[20] = 3
    227        a[24] = 8
    228        a[28] = 6
    229        b[0] = 4
    230        b[4] = 0
    231        b[8] = 3
    232        b[12] = 9
    233        b[16] = 1
    234        b[20] = 8
    235        b[24] = 2
    236        b[28] = 7
    237        t1 = &a
    238        param t1
    239        param 8
    240        call bubble(int *, int), 2
    241        t2 = &b
    242        param t2
    243        param 0
    244        param 7
    245        call quick(int *, int, int), 3
    246        t3 = a[0]
    247        t4 = a[28]
    248        t5 = b[0]
    249        t6 = b[28]
    250        param t1
    251        param 8
    252        param 7
    253        t8 = call find(int *, int, int), 3
    254        param t1
    255        param 8
    256        param 4
    257        t10 = call find(int *, int, int), 3
    258        param "%d %d %d %d %d %d\n"
    259        param t3
    260        param t4
    261        param t5
    262        param t6
    263        param t8
    264        param t10
    265        call printf, 7
    266        param 10
    267        t11 = call hanoi(int), 1
    268        param 2
    269        param 3
    270        t12 = call ack(int, int), 2
    271        param "%d %d\n"
    272        param t11
    273        param t12
    274        call printf, 3
    275        m1[0] = 1
    276        m1[4] = 2
    277        m1[8] = 3
    278        m1[12] = 4
    279        m2[0] = 5
    280        m2[4] = 6
    281        m2[8] = 7
    282        m2[12] = 8
    283        i = 0
    284  L22:  if i int>= 2 goto L27
    285        j = 0
    286  L23:  if j int>= 2 goto L26
    287        t13 = i int<< 1                     (n2 = 2)
    288        t14 = t13 int+ j
    289        t15 = t14 int<< 2                   (w = 4)
    290        p[t15] = 0
    291        k = 0
    292  L24:  if k int>= 2 goto L25
    293        t16 = i int<< 1                     (n2 = 2)
    294        t17 = t16 int+ j
    295        t18 = t17 int<< 2                   (w = 4)
    296        t19 = p[t18]
    297        t21 = t16 int+ k
    298        t22 = t21 int<< 2                   (w = 4)
    299        t23 = m1[t22]
    300        t24 = k int<< 1                     (n2 = 2)
    301        t25 = t24 int+ j
    302        t26 = t25 int<< 2                   (w = 4)
    303        t27 = m2[t26]
    304        t28 = t23 int* t27
    305        t29 = t19 int+ t28
    306        p[t18] = t29
    307        k = k int+ 1
    308        goto L24
    309  L25:  j = j int+ 1
    310        goto L23
    311  L26:  i = i int+ 1
    312        goto L22
    313  L27:  t33 = p[0]
    314        t34 = p[4]
    315        t35 = p[8]
    316        t36 = p[12]
    317        param "%d %d %d %d\n"
    318        param t33
    319        param t34
    320        param t35
    321        param t36
    322        call printf, 5
    323        primes = 0
    324        i = 0
    325  L28:  if i int>= 50 goto L29
    326        sieve[i] = 1
    327        i = i int+ 1
    328        goto L28
    329  L29:  i = 2
    330  L30:  if i int>= 50 goto L33
    331        t38 = sieve[i]
    332        if t38 char== 0 goto L32
    333        primes = primes int+ 1
    334        j = i int* i
    335  L31:  if j int>= 50 goto L32
    336        sieve[j] = 0
    337        j = j int+ i
    338        goto L31
    339  L32:  i = i int+ 1
    340        goto L30
    341  L33:  text[0] = 99
    342        text[1] = 111
    343        text[2] = 109
    344        text[3] = 112
    345        text[4] = 105
    346        text[5] = 108
    347        text[6] = 101
    348        text[7] = 114
    349        text[8] = 0
    350        text[9] = 0
    351        text[10] = 0
    352        text[11] = 0
    353        i = 0
    354        j = 7
    355  L34:  if i int>= j goto L35
    356        t43 = text[i]
    357        t = t43
    358        t44 = text[j]
    359        text[i] = t44
    360        text[j] = t43
    361        i = i int+ 1
    362        j = j int- 1
    363        goto L34
    364  L35:  n = 9081
    365        v = 0
    366        k = 0
    367  L36:  if n int== 0 goto L37
    368        t47 = k
    369        k = k int+ 1
    370        t49 = n int% 10
    371        t50 = 48 int+ t49
    372        t51 = inttochar t50
    373        num[t47] = t51
    374        n = n int/ 10
    375        goto L36
    376  L37:  i = k int- 1
    377  L38:  if i int< 0 goto L39
    378        t54 = v int* 10
    379        t55 = num[i]
    380        t56 = chartoint t55
    381        t57 = t56 int- 48
    382        v = t54 int+ t57
    383        i = i int- 1
    384        goto L38
    385  L39:  t60 = &text
    386        param "%d %s %d\n"
    387        param primes
    388        param t60
    389        param v
    390        call printf, 4
    391        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

1 9 0 9 5 -1
1023 9
19 22 43 50
15 relipmoc 9081

   exit code 0, 2519 instructions executed
