============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_algorithms.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 401 -> 329 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          401 -> 329   (17% fewer)

   constants folded                        4
   algebraic simplifications              24
   common subexpressions                  13
   copies / constants forwarded           20
   temporaries merged away                27
   dead instructions removed              17
   jumps removed or redirected            28
   unreachable instructions removed        1

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   moves            int                             4  0

============================================================================
 FUNCTION bubble(int *, int)        (link name _Z6bubblePii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 17 temporaries, frame 116 bytes

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
   t4               temp    int                             4      32
   t5               temp    int *                           4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   t9               temp    int *                           4      52
   t10              temp    int                             4      56
   t11              temp    int                             4      60
   t12              temp    int *                           4      64
   t13              temp    int                             4      68
   t16              temp    int                             4      80
   t17              temp    int                             4      84
   t18              temp    int *                           4      88
   t19              temp    int                             4      92
   (7 temporaries no longer used after optimization not shown)

 Code: 30 instruction(s)

    100       i = 0
    101  L1:  t1 = n int- 1
    102       if i int>= t1 goto L5
    103       j = 0
    104  L2:  t2 = n int- 1
    105       t3 = t2 int- i
    106       if j int>= t3 goto L4
    107       t4 = j int<< 2
    108       t5 = a ptr+ t4
    109       t6 = *t5
    110       t7 = j int+ 1
    111       t8 = t7 int<< 2
    112       t9 = a ptr+ t8
    113       t10 = *t9
    114       if t6 int<= t10 goto L3
    115       t11 = j int<< 2
    116       t12 = a ptr+ t11
    117       t13 = *t12
    118       t = t13
    119       t16 = j int+ 1
    120       t17 = t16 int<< 2
    121       t18 = a ptr+ t17
    122       t19 = *t18
    123       *t12 = t19
    124       *t18 = t13
    125  L3:  j = j int+ 1
    126       goto L2
    127  L4:  i = i int+ 1
    128       goto L1
    129  L5:  return

============================================================================
 FUNCTION quick(int *, int, int)        (link name _Z5quickPiii)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 16 temporaries, frame 128 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   lo               param   int                             4       4
   hi               param   int                             4       8
   pivot            local   int                             4      12
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

    130        if lo int< hi goto L6
    131        return
    132  L6:   t1 = lo int+ hi
    133        t2 = t1 int/ 2
    134        t3 = t2 int<< 2
    135        t4 = a ptr+ t3
    136        pivot = *t4
    137        i = lo
    138        j = hi
    139  L7:   if i int> j goto L11
    140  L8:   t6 = i int<< 2
    141        t7 = a ptr+ t6
    142        t8 = *t7
    143        if t8 int>= pivot goto L9
    144        i = i int+ 1
    145        goto L8
    146  L9:   t10 = j int<< 2
    147        t11 = a ptr+ t10
    148        t12 = *t11
    149        if t12 int<= pivot goto L10
    150        j = j int- 1
    151        goto L9
    152  L10:  if i int> j goto L7
    153        t14 = i int<< 2
    154        t15 = a ptr+ t14
    155        t16 = *t15
    156        t = t16
    157        t19 = j int<< 2
    158        t20 = a ptr+ t19
    159        t21 = *t20
    160        *t15 = t21
    161        *t20 = t16
    162        i = i int+ 1
    163        j = j int- 1
    164        goto L7
    165  L11:  param a
    166        param lo
    167        param j
    168        call quick(int *, int, int), 3
    169        param a
    170        param i
    171        param hi
    172        call quick(int *, int, int), 3
    173        return

============================================================================
 FUNCTION search(int *, int, int)        (link name _Z6searchPiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 9 temporaries, frame 76 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   key              param   int                             4       8
   lo               local   int                             4      12
   hi               local   int                             4      16
   mid              local   int                             4      20
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40
   t6               temp    int *                           4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int *                           4      56
   t10              temp    int                             4      60
   (4 temporaries no longer used after optimization not shown)

 Code: 21 instruction(s)

    174        lo = 0
    175        hi = n int- 1
    176  L12:  if lo int> hi goto L15
    177        t2 = hi int- lo
    178        t3 = t2 int/ 2
    179        t4 = lo int+ t3
    180        mid = t4
    181        t5 = t4 int<< 2
    182        t6 = a ptr+ t5
    183        t7 = *t6
    184        if t7 int!= key goto L13
    185        return mid
    186  L13:  t8 = mid int<< 2
    187        t9 = a ptr+ t8
    188        t10 = *t9
    189        if t10 int>= key goto L14
    190        lo = mid int+ 1
    191        goto L12
    192  L14:  hi = mid int- 1
    193        goto L12
    194  L15:  return -1

============================================================================
 FUNCTION hanoi(int, int, int, int)        (link name _Z5hanoiiiii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 1 temporary, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   from             param   int                             4       4
   to               param   int                             4       8
   via              param   int                             4      12
   t1               temp    int                             4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 15 instruction(s)

    195        if n int!= 0 goto L16
    196        return
    197  L16:  t1 = n int- 1
    198        param t1
    199        param from
    200        param via
    201        param to
    202        call hanoi(int, int, int, int), 4
    203        moves = moves int+ 1
    204        param t1
    205        param via
    206        param to
    207        param from
    208        call hanoi(int, int, int, int), 4
    209        return

============================================================================
 FUNCTION ackermann(int, int)        (link name _Z9ackermannii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 36 bytes

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

 Code: 18 instruction(s)

    210        if m int!= 0 goto L17
    211        t1 = n int+ 1
    212        return t1
    213  L17:  if n int!= 0 goto L18
    214        t2 = m int- 1
    215        param t2
    216        param 1
    217        t3 = call ackermann(int, int), 2
    218        return t3
    219  L18:  t4 = m int- 1
    220        t5 = n int- 1
    221        param m
    222        param t5
    223        t6 = call ackermann(int, int), 2
    224        param t4
    225        param t6
    226        t7 = call ackermann(int, int), 2
    227        return t7

============================================================================
 FUNCTION multiply(int (*)[3], int (*)[2], int (*)[2])        (link name _Z8multiplyPA3_iPA2_iS2_)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 20 temporaries, frame 120 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int (*)[3]                      4       0
   b                param   int (*)[2]                      4       4
   c                param   int (*)[2]                      4       8
   i                local   int                             4      12
   j                local   int                             4      16
   k                local   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int (*)[2]                      4      28
   t3               temp    int                             4      32
   t4               temp    int (*)[2]                      4      36
   t5               temp    int                             4      40
   t6               temp    int (*)[2]                      4      44
   t7               temp    int                             4      48
   t8               temp    int (*)[2]                      4      52
   t9               temp    int                             4      56
   t10              temp    int                             4      60
   t11              temp    int (*)[3]                      4      64
   t12              temp    int                             4      68
   t13              temp    int (*)[3]                      4      72
   t14              temp    int                             4      76
   t15              temp    int                             4      80
   t16              temp    int (*)[2]                      4      84
   t18              temp    int (*)[2]                      4      92
   t19              temp    int                             4      96
   t20              temp    int                             4     100
   t21              temp    int                             4     104
   (4 temporaries no longer used after optimization not shown)

 Code: 35 instruction(s)

    228        i = 0
    229  L19:  if i int>= 2 goto L24
    230        j = 0
    231  L20:  if j int>= 2 goto L23
    232        t1 = i int<< 3
    233        t2 = c ptr+ t1
    234        t3 = j int<< 2                      (w = 4)
    235        t4 = t2 ptr+ t3
    236        *t4 = 0
    237        k = 0
    238  L21:  if k int>= 3 goto L22
    239        t5 = i int<< 3
    240        t6 = c ptr+ t5
    241        t7 = j int<< 2                      (w = 4)
    242        t8 = t6 ptr+ t7
    243        t9 = *t8
    244        t10 = i int* 12
    245        t11 = a ptr+ t10
    246        t12 = k int<< 2                     (w = 4)
    247        t13 = t11 ptr+ t12
    248        t14 = *t13
    249        t15 = k int<< 3
    250        t16 = b ptr+ t15
    251        t18 = t16 ptr+ t7
    252        t19 = *t18
    253        t20 = t14 int* t19
    254        t21 = t9 int+ t20
    255        *t8 = t21
    256        k = k int+ 1
    257        goto L21
    258  L22:  j = j int+ 1
    259        goto L20
    260  L23:  i = i int+ 1
    261        goto L19
    262  L24:  return

============================================================================
 FUNCTION primes(int)        (link name _Z6primesi)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 1 temporary, frame 148 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   limit            param   int                             4       0
   composite        local   char[101]                     101       4
   count            local   int                             4     108
   i.34             local   int                             4     112
   i.35             local   int                             4     116
   j                local   int                             4     120
   t2               temp    char                            1     128
   (5 temporaries no longer used after optimization not shown)

 Code: 19 instruction(s)

    263        count = 0
    264        i.34 = 0
    265  L25:  if i.34 int> limit goto L26
    266        composite[i.34] = 0
    267        i.34 = i.34 int+ 1
    268        goto L25
    269  L26:  i.35 = 2
    270  L27:  if i.35 int> limit goto L30
    271        t2 = composite[i.35]
    272        if t2 char!= 0 goto L29
    273        count = count int+ 1
    274        j = i.35 int* i.35
    275  L28:  if j int> limit goto L29
    276        composite[j] = 1
    277        j = j int+ i.35
    278        goto L28
    279  L29:  i.35 = i.35 int+ 1
    280        goto L27
    281  L30:  return count

============================================================================
 FUNCTION power(int, int)        (link name _Z5powerii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   base             param   int                             4       0
   exp              param   int                             4       4
   result           local   int                             4       8
   t1               temp    int                             4      12
   (3 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    282        result = 1
    283  L31:  if exp int<= 0 goto L33
    284        t1 = exp int& 1
    285        if t1 int== 0 goto L32
    286        result = result int* base
    287  L32:  base = base int* base
    288        exp = exp int>> 1
    289        goto L31
    290  L33:  return result

============================================================================
 FUNCTION collatz(int)        (link name _Z7collatzi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   steps            local   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   (3 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    291        steps = 0
    292  L34:  if n int== 1 goto L37
    293        t2 = n int% 2
    294        if t2 int== 0 goto L35
    295        t3 = n int* 3
    296        t1 = t3 int+ 1
    297        goto L36
    298  L35:  t1 = n int/ 2
    299  L36:  n = t1
    300        steps = steps int+ 1
    301        goto L34
    302  L37:  return steps

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 24 temporaries, frame 260 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int[8]                         32       0
   b                local   int[8]                         32      32
   i.44             local   int                             4      64
   i.45             local   int                             4      68
   x                local   int[2][3]                      24      72
   y                local   int[3][2]                      24      96
   z                local   int[2][2]                      16     120
   t3               temp    int (*)[8]                      4     144
   t4               temp    int (*)[8]                      4     148
   t5               temp    int                             4     152
   t6               temp    int                             4     156
   t8               temp    int                             4     164
   t9               temp    int                             4     168
   t11              temp    int (*)[8]                      4     176
   t12              temp    int                             4     180
   t14              temp    int                             4     188
   t15              temp    int (*)[8]                      4     192
   t17              temp    int                             4     200
   t18              temp    int                             4     204
   t19              temp    int                             4     208
   t20              temp    int (*)[2][3]                   4     212
   t21              temp    int (*)[3][2]                   4     216
   t22              temp    int (*)[2][2]                   4     220
   t23              temp    int                             4     224
   t24              temp    int                             4     228
   t25              temp    int                             4     232
   t26              temp    int                             4     236
   t27              temp    int                             4     240
   t28              temp    int                             4     244
   t29              temp    int                             4     248
   t31              temp    int                             4     256
   (7 temporaries no longer used after optimization not shown)

 Code: 126 instruction(s)

    303        a[0] = 42
    304        a[4] = 7
    305        a[8] = 19
    306        a[12] = 3
    307        a[16] = 25
    308        a[20] = 7
    309        a[24] = 88
    310        a[28] = 1
    311        b[0] = 5
    312        b[4] = -2
    313        b[8] = 9
    314        b[12] = 0
    315        b[16] = 9
    316        b[20] = 14
    317        b[24] = -7
    318        b[28] = 3
    319        t3 = &a
    320        param t3
    321        param 8
    322        call bubble(int *, int), 2
    323        t4 = &b
    324        param t4
    325        param 0
    326        param 7
    327        call quick(int *, int, int), 3
    328        i.44 = 0
    329  L38:  if i.44 int>= 8 goto L39
    330        t5 = i.44 int<< 2                   (w = 4)
    331        t6 = a[t5]
    332        param "%d "
    333        param t6
    334        call printf, 2
    335        i.44 = i.44 int+ 1
    336        goto L38
    337  L39:  param "\n"
    338        call printf, 1
    339        i.45 = 0
    340  L40:  if i.45 int>= 8 goto L41
    341        t8 = i.45 int<< 2                   (w = 4)
    342        t9 = b[t8]
    343        param "%d "
    344        param t9
    345        call printf, 2
    346        i.45 = i.45 int+ 1
    347        goto L40
    348  L41:  t11 = &a
    349        param t11
    350        param 8
    351        param 25
    352        t12 = call search(int *, int, int), 3
    353        param t11
    354        param 8
    355        param 26
    356        t14 = call search(int *, int, int), 3
    357        t15 = &b
    358        param t15
    359        param 8
    360        param -7
    361        t17 = call search(int *, int, int), 3
    362        param "\n%d %d %d\n"
    363        param t12
    364        param t14
    365        param t17
    366        call printf, 4
    367        param 6
    368        param 1
    369        param 3
    370        param 2
    371        call hanoi(int, int, int, int), 4
    372        param 2
    373        param 3
    374        t18 = call ackermann(int, int), 2
    375        param 27
    376        t19 = call collatz(int), 1
    377        param "%d %d %d\n"
    378        param moves
    379        param t18
    380        param t19
    381        call printf, 4
    382        x[0] = 1
    383        x[4] = 2
    384        x[8] = 3
    385        x[12] = 4
    386        x[16] = 5
    387        x[20] = 6
    388        y[0] = 7
    389        y[4] = 8
    390        y[8] = 9
    391        y[12] = 10
    392        y[16] = 11
    393        y[20] = 12
    394        t20 = &x
    395        t21 = &y
    396        t22 = &z
    397        param t20
    398        param t21
    399        param t22
    400        call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
    401        t23 = z[0]
    402        t24 = z[4]
    403        t25 = z[8]
    404        t26 = z[12]
    405        param "%d %d %d %d\n"
    406        param t23
    407        param t24
    408        param t25
    409        param t26
    410        call printf, 5
    411        param 100
    412        t27 = call primes(int), 1
    413        param 3
    414        param 13
    415        t28 = call power(int, int), 2
    416        param 2
    417        param 10
    418        t29 = call power(int, int), 2
    419        param "%d %d %d\n"
    420        param t27
    421        param t28
    422        param t29
    423        call printf, 4
    424        param t11
    425        param 8
    426        param 88
    427        t31 = call search(int *, int, int), 3
    428        return t31


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   bubble             function      void (int *, int)          -           4    -    1  _Z6bubblePii; defined
   quick              function      void (int *, int, int)     -          10    -    3  _Z5quickPiii; defined
   search             function      int (int *, int, int)      -          22    -    4  _Z6searchPiii; defined
   moves              variable      int                        global     32    4    2  
   hanoi              function      void (int, int, int, int)  -          33    -    3  _Z5hanoiiiii; defined
   ackermann          function      int (int, int)             -          40    -    4  _Z9ackermannii; defined
   multiply           function      void (int (*)[3], int (*)[2], int (*)[2]) -          46    -    1  _Z8multiplyPA3_iPA2_iS2_; defined
   primes             function      int (int)                  -          54    -    1  _Z6primesi; defined
   power              function      int (int, int)             -          66    -    2  _Z5powerii; defined
   collatz            function      int (int)                  -          76    -    1  _Z7collatzi; defined
   main               function      int (void)                 -          78    -    0  defined

 scope: global > bubble()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       4    4    6  a.1
   n                  parameter     int                        param       4    4    2  n.2

 scope: global > bubble() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       5    4    3  i.3

 scope: global > bubble() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local       6    4    8  j.4

 scope: global > bubble() > for > for body > for > for body > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local       7    4    1  t.5

 scope: global > quick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param      10    4    9  a.6
   lo                 parameter     int                        param      10    4    4  lo.7
   hi                 parameter     int                        param      10    4    4  hi.8
   pivot              variable      int                        local      12    4    2  pivot.9
   i                  variable      int                        local      12    4    8  i.10
   j                  variable      int                        local      12    4    8  j.11

 scope: global > quick() > while > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local      16    4    1  t.12

 scope: global > search()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param      22    4    2  a.13
   n                  parameter     int                        param      22    4    1  n.14
   key                parameter     int                        param      22    4    2  key.15
   lo                 variable      int                        local      23    4    4  lo.16
   hi                 variable      int                        local      23    4    3  hi.17

 scope: global > search() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   mid                variable      int                        local      25    4    5  mid.18

 scope: global > hanoi()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      33    4    3  n.19
   from               parameter     int                        param      33    4    2  from.20
   to                 parameter     int                        param      33    4    2  to.21
   via                parameter     int                        param      33    4    2  via.22

 scope: global > ackermann()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int                        param      40    4    4  m.23
   n                  parameter     int                        param      40    4    3  n.24

 scope: global > multiply()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int (*)[3]                 param      46    4    1  a.25
   b                  parameter     int (*)[2]                 param      46    4    1  b.26
   c                  parameter     int (*)[2]                 param      46    4    2  c.27

 scope: global > multiply() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      47    4    5  i.28

 scope: global > multiply() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      48    4    5  j.29

 scope: global > multiply() > for > for body > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      50    4    4  k.30

 scope: global > primes()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   limit              parameter     int                        param      54    4    3  limit.31
   composite          variable      char[101]                  local      55  101    3  composite.32
   count              variable      int                        local      56    4    2  count.33

 scope: global > primes() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      57    4    3  i.34
   i                  variable      int                        local      58    4    6  i.35

 scope: global > primes() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      61    4    3  j.36

 scope: global > power()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   base               parameter     int                        param      66    4    3  base.37
   exp                parameter     int                        param      66    4    3  exp.38
   result             variable      int                        local      67    4    2  result.39

 scope: global > collatz()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      76    4    5  n.40
   steps              variable      int                        local      76    4    2  steps.41

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int[8]                     local      79   32    5  a.42
   b                  variable      int[8]                     local      79   32    3  b.43
   x                  variable      int[2][3]                  local      88   24    1  x.46
   y                  variable      int[3][2]                  local      88   24    1  y.47
   z                  variable      int[2][2]                  local      88   16    5  z.48

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      82    4    3  i.44
   i                  variable      int                        local      84    4    3  i.45

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
