============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_algorithms.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 401 -> 325 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          401 -> 325   (18% fewer)

   constants folded                        4
   algebraic simplifications              24
   common subexpressions                  18
   copies / constants forwarded           53
   temporaries merged away                28
   dead instructions removed              46
   jumps removed or redirected            28
   unreachable instructions removed        5
   propagated across blocks               10
   dead assignments removed                8
   calls inlined                           3
   tail calls turned into jumps            4
   common subexpressions across blocks     13
   instructions moved out of loops        11

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   moves            int                             4  0

 As three address code (initial values, in place before main runs):

    moves = 0

============================================================================
 FUNCTION bubble(int *, int)        (link name _Z6bubblePii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 11 temporaries, frame 116 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   t                local   int                             4      16
   t1               temp    int                             4      20
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int *                           4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   t9               temp    int *                           4      52
   t10              temp    int                             4      56
   t13              temp    int                             4      68
   t19              temp    int                             4      92
   (13 temporaries no longer used after optimization not shown)

 Code: 23 instruction(s)

    100       i = 0
    101       t1 = n int- 1
    102  L1:  if i int>= t1 goto L5
    103       j = 0
    104       t3 = t1 int- i
    105  L2:  if j int>= t3 goto L4
    106       t4 = j int<< 2
    107       t5 = a ptr+ t4
    108       t6 = *t5
    109       t7 = j int+ 1
    110       t8 = t7 int<< 2
    111       t9 = a ptr+ t8
    112       t10 = *t9
    113       if t6 int<= t10 goto L3
    114       t13 = *t5
    115       t19 = *t9
    116       *t5 = t19
    117       *t9 = t13
    118  L3:  j = j int+ 1
    119       goto L2
    120  L4:  i = i int+ 1
    121       goto L1
    122  L5:  return

============================================================================
 FUNCTION quick(int *, int, int)        (link name _Z5quickPiii)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 12 temporaries, frame 140 bytes

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
   t16              temp    int                             4      88
   t21              temp    int                             4     108
   (16 temporaries no longer used after optimization not shown)

 Code: 36 instruction(s)

    123  L6:   if lo int< hi goto L7
    124        return
    125  L7:   t1 = lo int+ hi
    126        t2 = t1 int/ 2
    127        t3 = t2 int<< 2
    128        t4 = a ptr+ t3
    129        pivot = *t4
    130        i = lo
    131        j = hi
    132  L8:   if i int> j goto L12
    133  L9:   t6 = i int<< 2
    134        t7 = a ptr+ t6
    135        t8 = *t7
    136        if t8 int>= pivot goto L10
    137        i = i int+ 1
    138        goto L9
    139  L10:  t10 = j int<< 2
    140        t11 = a ptr+ t10
    141        t12 = *t11
    142        if t12 int<= pivot goto L11
    143        j = j int- 1
    144        goto L10
    145  L11:  if i int> j goto L8
    146        t16 = *t7
    147        t21 = *t11
    148        *t7 = t21
    149        *t11 = t16
    150        i = i int+ 1
    151        j = j int- 1
    152        goto L8
    153  L12:  param a
    154        param lo
    155        param j
    156        call quick(int *, int, int), 3
    157        lo = i
    158        goto L6

============================================================================
 FUNCTION search(int *, int, int)        (link name _Z6searchPiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 7 temporaries, frame 76 bytes

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
   t10              temp    int                             4      60
   (6 temporaries no longer used after optimization not shown)

 Code: 18 instruction(s)

    159        lo = 0
    160        hi = n int- 1
    161  L13:  if lo int> hi goto L16
    162        t2 = hi int- lo
    163        t3 = t2 int/ 2
    164        t4 = lo int+ t3
    165        t5 = t4 int<< 2
    166        t6 = a ptr+ t5
    167        t7 = *t6
    168        if t7 int!= key goto L14
    169        return t4
    170  L14:  t10 = *t6
    171        if t10 int>= key goto L15
    172        lo = t4 int+ 1
    173        goto L13
    174  L15:  hi = t4 int- 1
    175        goto L13
    176  L16:  return -1

============================================================================
 FUNCTION hanoi(int, int, int, int)        (link name _Z5hanoiiiii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 2 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   from             param   int                             4       4
   to               param   int                             4       8
   via              param   int                             4      12
   t1               temp    int                             4      16
   t7               temp    int                             4      40
   (5 temporaries no longer used after optimization not shown)

 Code: 14 instruction(s)

    177  L17:  if n int!= 0 goto L18
    178        return
    179  L18:  t1 = n int- 1
    180        param t1
    181        param from
    182        param via
    183        param to
    184        call hanoi(int, int, int, int), 4
    185        moves = moves int+ 1
    186        t7 = from
    187        n = t1
    188        from = via
    189        via = t7
    190        goto L17

============================================================================
 FUNCTION ackermann(int, int)        (link name _Z9ackermannii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   int                             4       0
   n                param   int                             4       4
   t1               temp    int                             4       8
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   t6               temp    int                             4      28
   (7 temporaries no longer used after optimization not shown)

 Code: 15 instruction(s)

    191  L19:  if m int!= 0 goto L20
    192        t1 = n int+ 1
    193        return t1
    194  L20:  if n int!= 0 goto L21
    195        m = m int- 1
    196        n = 1
    197        goto L19
    198  L21:  t4 = m int- 1
    199        t5 = n int- 1
    200        param m
    201        param t5
    202        t6 = call ackermann(int, int), 2
    203        m = t4
    204        n = t6
    205        goto L19

============================================================================
 FUNCTION multiply(int (*)[3], int (*)[2], int (*)[2])        (link name _Z8multiplyPA3_iPA2_iS2_)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 16 temporaries, frame 120 bytes

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
   (8 temporaries no longer used after optimization not shown)

 Code: 31 instruction(s)

    206        i = 0
    207  L22:  if i int>= 2 goto L27
    208        j = 0
    209        t1 = i int<< 3
    210        t2 = c ptr+ t1
    211        t10 = i int* 12
    212        t11 = a ptr+ t10
    213  L23:  if j int>= 2 goto L26
    214        t3 = j int<< 2                      (w = 4)
    215        t4 = t2 ptr+ t3
    216        *t4 = 0
    217        k = 0
    218  L24:  if k int>= 3 goto L25
    219        t9 = *t4
    220        t12 = k int<< 2                     (w = 4)
    221        t13 = t11 ptr+ t12
    222        t14 = *t13
    223        t15 = k int<< 3
    224        t16 = b ptr+ t15
    225        t18 = t16 ptr+ t3
    226        t19 = *t18
    227        t20 = t14 int* t19
    228        t21 = t9 int+ t20
    229        *t4 = t21
    230        k = k int+ 1
    231        goto L24
    232  L25:  j = j int+ 1
    233        goto L23
    234  L26:  i = i int+ 1
    235        goto L22
    236  L27:  return

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

    237        count = 0
    238        i.34 = 0
    239  L28:  if i.34 int> limit goto L29
    240        composite[i.34] = 0
    241        i.34 = i.34 int+ 1
    242        goto L28
    243  L29:  i.35 = 2
    244  L30:  if i.35 int> limit goto L33
    245        t2 = composite[i.35]
    246        if t2 char!= 0 goto L32
    247        count = count int+ 1
    248        j = i.35 int* i.35
    249  L31:  if j int> limit goto L32
    250        composite[j] = 1
    251        j = j int+ i.35
    252        goto L31
    253  L32:  i.35 = i.35 int+ 1
    254        goto L30
    255  L33:  return count

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

    256        result = 1
    257  L34:  if exp int<= 0 goto L36
    258        t1 = exp int& 1
    259        if t1 int== 0 goto L35
    260        result = result int* base
    261  L35:  base = base int* base
    262        exp = exp int>> 1
    263        goto L34
    264  L36:  return result

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

    265        steps = 0
    266  L37:  if n int== 1 goto L40
    267        t2 = n int% 2
    268        if t2 int== 0 goto L38
    269        t3 = n int* 3
    270        t1 = t3 int+ 1
    271        goto L39
    272  L38:  t1 = n int/ 2
    273  L39:  n = t1
    274        steps = steps int+ 1
    275        goto L37
    276  L40:  return steps

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 32 temporaries, frame 312 bytes

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
   t12              temp    int                             4     180
   t14              temp    int                             4     188
   t17              temp    int                             4     200
   t18              temp    int                             4     204
   t20              temp    int (*)[2][3]                   4     212
   t21              temp    int (*)[3][2]                   4     216
   t22              temp    int (*)[2][2]                   4     220
   t23              temp    int                             4     224
   t24              temp    int                             4     228
   t25              temp    int                             4     232
   t26              temp    int                             4     236
   t27              temp    int                             4     240
   t31              temp    int                             4     256
   t32              temp    int                             4     260
   t33              temp    int                             4     264
   t34              temp    int                             4     268
   t35              temp    int                             4     272
   t36              temp    int                             4     276
   t37              temp    int                             4     280
   t38              temp    int                             4     284
   t39              temp    int                             4     288
   t40              temp    int                             4     292
   t41              temp    int                             4     296
   t42              temp    int                             4     300
   t43              temp    int                             4     304
   t44              temp    int                             4     308
   (12 temporaries no longer used after optimization not shown)

 Code: 148 instruction(s)

    277        a[0] = 42
    278        a[4] = 7
    279        a[8] = 19
    280        a[12] = 3
    281        a[16] = 25
    282        a[20] = 7
    283        a[24] = 88
    284        a[28] = 1
    285        b[0] = 5
    286        b[4] = -2
    287        b[8] = 9
    288        b[12] = 0
    289        b[16] = 9
    290        b[20] = 14
    291        b[24] = -7
    292        b[28] = 3
    293        t3 = &a
    294        param t3
    295        param 8
    296        call bubble(int *, int), 2
    297        t4 = &b
    298        param t4
    299        param 0
    300        param 7
    301        call quick(int *, int, int), 3
    302        i.44 = 0
    303  L41:  if i.44 int>= 8 goto L42
    304        t5 = i.44 int<< 2                   (w = 4)
    305        t6 = a[t5]
    306        param "%d "
    307        param t6
    308        call printf, 2
    309        i.44 = i.44 int+ 1
    310        goto L41
    311  L42:  param "\n"
    312        call printf, 1
    313        i.45 = 0
    314  L43:  if i.45 int>= 8 goto L44
    315        t8 = i.45 int<< 2                   (w = 4)
    316        t9 = b[t8]
    317        param "%d "
    318        param t9
    319        call printf, 2
    320        i.45 = i.45 int+ 1
    321        goto L43
    322  L44:  param t3
    323        param 8
    324        param 25
    325        t12 = call search(int *, int, int), 3
    326        param t3
    327        param 8
    328        param 26
    329        t14 = call search(int *, int, int), 3
    330        param t4
    331        param 8
    332        param -7
    333        t17 = call search(int *, int, int), 3
    334        param "\n%d %d %d\n"
    335        param t12
    336        param t14
    337        param t17
    338        call printf, 4
    339        param 6
    340        param 1
    341        param 3
    342        param 2
    343        call hanoi(int, int, int, int), 4
    344        param 2
    345        param 3
    346        t18 = call ackermann(int, int), 2
    347        t32 = 27
    348        t33 = 0
    349  L45:  if t32 int== 1 goto L48
    350        t34 = t32 int% 2
    351        if t34 int== 0 goto L46
    352        t35 = t32 int* 3
    353        t36 = t35 int+ 1
    354        goto L47
    355  L46:  t36 = t32 int/ 2
    356  L47:  t32 = t36
    357        t33 = t33 int+ 1
    358        goto L45
    359  L48:  param "%d %d %d\n"
    360        param moves
    361        param t18
    362        param t33
    363        call printf, 4
    364        x[0] = 1
    365        x[4] = 2
    366        x[8] = 3
    367        x[12] = 4
    368        x[16] = 5
    369        x[20] = 6
    370        y[0] = 7
    371        y[4] = 8
    372        y[8] = 9
    373        y[12] = 10
    374        y[16] = 11
    375        y[20] = 12
    376        t20 = &x
    377        t21 = &y
    378        t22 = &z
    379        param t20
    380        param t21
    381        param t22
    382        call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
    383        t23 = z[0]
    384        t24 = z[4]
    385        t25 = z[8]
    386        t26 = z[12]
    387        param "%d %d %d %d\n"
    388        param t23
    389        param t24
    390        param t25
    391        param t26
    392        call printf, 5
    393        param 100
    394        t27 = call primes(int), 1
    395        t37 = 3
    396        t38 = 13
    397        t39 = 1
    398  L49:  if t38 int<= 0 goto L51
    399        t40 = t38 int& 1
    400        if t40 int== 0 goto L50
    401        t39 = t39 int* t37
    402  L50:  t37 = t37 int* t37
    403        t38 = t38 int>> 1
    404        goto L49
    405  L51:  t41 = 2
    406        t42 = 10
    407        t43 = 1
    408  L52:  if t42 int<= 0 goto L54
    409        t44 = t42 int& 1
    410        if t44 int== 0 goto L53
    411        t43 = t43 int* t41
    412  L53:  t41 = t41 int* t41
    413        t42 = t42 int>> 1
    414        goto L52
    415  L54:  param "%d %d %d\n"
    416        param t27
    417        param t39
    418        param t43
    419        call printf, 4
    420        param t3
    421        param 8
    422        param 88
    423        t31 = call search(int *, int, int), 3
    424        return t31


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
