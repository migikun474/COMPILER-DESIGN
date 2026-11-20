============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_algorithms.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 401 -> 330 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          401 -> 330   (17% fewer)

   constants folded                        4
   algebraic simplifications              24
   common subexpressions                  13
   copies / constants forwarded           51
   temporaries merged away                28
   dead instructions removed              45
   jumps removed or redirected            28
   unreachable instructions removed        5
   propagated across blocks                5
   dead assignments removed                4
   calls inlined                           3
   tail calls turned into jumps            4
   common subexpressions across blocks     13

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

 Symbol table: 5 parameter(s)/local(s), 12 temporaries, frame 116 bytes

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
   t13              temp    int                             4      68
   t19              temp    int                             4      92
   (12 temporaries no longer used after optimization not shown)

 Code: 24 instruction(s)

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
    115       t13 = *t5
    116       t19 = *t9
    117       *t5 = t19
    118       *t9 = t13
    119  L3:  j = j int+ 1
    120       goto L2
    121  L4:  i = i int+ 1
    122       goto L1
    123  L5:  return

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

    124  L6:   if lo int< hi goto L7
    125        return
    126  L7:   t1 = lo int+ hi
    127        t2 = t1 int/ 2
    128        t3 = t2 int<< 2
    129        t4 = a ptr+ t3
    130        pivot = *t4
    131        i = lo
    132        j = hi
    133  L8:   if i int> j goto L12
    134  L9:   t6 = i int<< 2
    135        t7 = a ptr+ t6
    136        t8 = *t7
    137        if t8 int>= pivot goto L10
    138        i = i int+ 1
    139        goto L9
    140  L10:  t10 = j int<< 2
    141        t11 = a ptr+ t10
    142        t12 = *t11
    143        if t12 int<= pivot goto L11
    144        j = j int- 1
    145        goto L10
    146  L11:  if i int> j goto L8
    147        t16 = *t7
    148        t21 = *t11
    149        *t7 = t21
    150        *t11 = t16
    151        i = i int+ 1
    152        j = j int- 1
    153        goto L8
    154  L12:  param a
    155        param lo
    156        param j
    157        call quick(int *, int, int), 3
    158        lo = i
    159        goto L6

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

    160        lo = 0
    161        hi = n int- 1
    162  L13:  if lo int> hi goto L16
    163        t2 = hi int- lo
    164        t3 = t2 int/ 2
    165        t4 = lo int+ t3
    166        t5 = t4 int<< 2
    167        t6 = a ptr+ t5
    168        t7 = *t6
    169        if t7 int!= key goto L14
    170        return t4
    171  L14:  t10 = *t6
    172        if t10 int>= key goto L15
    173        lo = t4 int+ 1
    174        goto L13
    175  L15:  hi = t4 int- 1
    176        goto L13
    177  L16:  return -1

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

    178  L17:  if n int!= 0 goto L18
    179        return
    180  L18:  t1 = n int- 1
    181        param t1
    182        param from
    183        param via
    184        param to
    185        call hanoi(int, int, int, int), 4
    186        moves = moves int+ 1
    187        t7 = from
    188        n = t1
    189        from = via
    190        via = t7
    191        goto L17

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

    192  L19:  if m int!= 0 goto L20
    193        t1 = n int+ 1
    194        return t1
    195  L20:  if n int!= 0 goto L21
    196        m = m int- 1
    197        n = 1
    198        goto L19
    199  L21:  t4 = m int- 1
    200        t5 = n int- 1
    201        param m
    202        param t5
    203        t6 = call ackermann(int, int), 2
    204        m = t4
    205        n = t6
    206        goto L19

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

    207        i = 0
    208  L22:  if i int>= 2 goto L27
    209        j = 0
    210  L23:  if j int>= 2 goto L26
    211        t1 = i int<< 3
    212        t2 = c ptr+ t1
    213        t3 = j int<< 2                      (w = 4)
    214        t4 = t2 ptr+ t3
    215        *t4 = 0
    216        k = 0
    217  L24:  if k int>= 3 goto L25
    218        t5 = i int<< 3
    219        t6 = c ptr+ t5
    220        t7 = j int<< 2                      (w = 4)
    221        t8 = t6 ptr+ t7
    222        t9 = *t8
    223        t10 = i int* 12
    224        t11 = a ptr+ t10
    225        t12 = k int<< 2                     (w = 4)
    226        t13 = t11 ptr+ t12
    227        t14 = *t13
    228        t15 = k int<< 3
    229        t16 = b ptr+ t15
    230        t18 = t16 ptr+ t7
    231        t19 = *t18
    232        t20 = t14 int* t19
    233        t21 = t9 int+ t20
    234        *t8 = t21
    235        k = k int+ 1
    236        goto L24
    237  L25:  j = j int+ 1
    238        goto L23
    239  L26:  i = i int+ 1
    240        goto L22
    241  L27:  return

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

    242        count = 0
    243        i.34 = 0
    244  L28:  if i.34 int> limit goto L29
    245        composite[i.34] = 0
    246        i.34 = i.34 int+ 1
    247        goto L28
    248  L29:  i.35 = 2
    249  L30:  if i.35 int> limit goto L33
    250        t2 = composite[i.35]
    251        if t2 char!= 0 goto L32
    252        count = count int+ 1
    253        j = i.35 int* i.35
    254  L31:  if j int> limit goto L32
    255        composite[j] = 1
    256        j = j int+ i.35
    257        goto L31
    258  L32:  i.35 = i.35 int+ 1
    259        goto L30
    260  L33:  return count

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

    261        result = 1
    262  L34:  if exp int<= 0 goto L36
    263        t1 = exp int& 1
    264        if t1 int== 0 goto L35
    265        result = result int* base
    266  L35:  base = base int* base
    267        exp = exp int>> 1
    268        goto L34
    269  L36:  return result

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

    270        steps = 0
    271  L37:  if n int== 1 goto L40
    272        t2 = n int% 2
    273        if t2 int== 0 goto L38
    274        t3 = n int* 3
    275        t1 = t3 int+ 1
    276        goto L39
    277  L38:  t1 = n int/ 2
    278  L39:  n = t1
    279        steps = steps int+ 1
    280        goto L37
    281  L40:  return steps

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
   t3               temp    int *                           4     144
   t4               temp    int *                           4     148
   t5               temp    int                             4     152
   t6               temp    int                             4     156
   t8               temp    int                             4     164
   t9               temp    int                             4     168
   t12              temp    int                             4     180
   t14              temp    int                             4     188
   t17              temp    int                             4     200
   t18              temp    int                             4     204
   t20              temp    int (*)[3]                      4     212
   t21              temp    int (*)[2]                      4     216
   t22              temp    int (*)[2]                      4     220
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

    282        a[0] = 42
    283        a[4] = 7
    284        a[8] = 19
    285        a[12] = 3
    286        a[16] = 25
    287        a[20] = 7
    288        a[24] = 88
    289        a[28] = 1
    290        b[0] = 5
    291        b[4] = -2
    292        b[8] = 9
    293        b[12] = 0
    294        b[16] = 9
    295        b[20] = 14
    296        b[24] = -7
    297        b[28] = 3
    298        t3 = &a
    299        param t3
    300        param 8
    301        call bubble(int *, int), 2
    302        t4 = &b
    303        param t4
    304        param 0
    305        param 7
    306        call quick(int *, int, int), 3
    307        i.44 = 0
    308  L41:  if i.44 int>= 8 goto L42
    309        t5 = i.44 int<< 2                   (w = 4)
    310        t6 = a[t5]
    311        param "%d "
    312        param t6
    313        call printf, 2
    314        i.44 = i.44 int+ 1
    315        goto L41
    316  L42:  param "\n"
    317        call printf, 1
    318        i.45 = 0
    319  L43:  if i.45 int>= 8 goto L44
    320        t8 = i.45 int<< 2                   (w = 4)
    321        t9 = b[t8]
    322        param "%d "
    323        param t9
    324        call printf, 2
    325        i.45 = i.45 int+ 1
    326        goto L43
    327  L44:  param t3
    328        param 8
    329        param 25
    330        t12 = call search(int *, int, int), 3
    331        param t3
    332        param 8
    333        param 26
    334        t14 = call search(int *, int, int), 3
    335        param t4
    336        param 8
    337        param -7
    338        t17 = call search(int *, int, int), 3
    339        param "\n%d %d %d\n"
    340        param t12
    341        param t14
    342        param t17
    343        call printf, 4
    344        param 6
    345        param 1
    346        param 3
    347        param 2
    348        call hanoi(int, int, int, int), 4
    349        param 2
    350        param 3
    351        t18 = call ackermann(int, int), 2
    352        t32 = 27
    353        t33 = 0
    354  L45:  if t32 int== 1 goto L48
    355        t34 = t32 int% 2
    356        if t34 int== 0 goto L46
    357        t35 = t32 int* 3
    358        t36 = t35 int+ 1
    359        goto L47
    360  L46:  t36 = t32 int/ 2
    361  L47:  t32 = t36
    362        t33 = t33 int+ 1
    363        goto L45
    364  L48:  param "%d %d %d\n"
    365        param moves
    366        param t18
    367        param t33
    368        call printf, 4
    369        x[0] = 1
    370        x[4] = 2
    371        x[8] = 3
    372        x[12] = 4
    373        x[16] = 5
    374        x[20] = 6
    375        y[0] = 7
    376        y[4] = 8
    377        y[8] = 9
    378        y[12] = 10
    379        y[16] = 11
    380        y[20] = 12
    381        t20 = &x
    382        t21 = &y
    383        t22 = &z
    384        param t20
    385        param t21
    386        param t22
    387        call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
    388        t23 = z[0]
    389        t24 = z[4]
    390        t25 = z[8]
    391        t26 = z[12]
    392        param "%d %d %d %d\n"
    393        param t23
    394        param t24
    395        param t25
    396        param t26
    397        call printf, 5
    398        param 100
    399        t27 = call primes(int), 1
    400        t37 = 3
    401        t38 = 13
    402        t39 = 1
    403  L49:  if t38 int<= 0 goto L51
    404        t40 = t38 int& 1
    405        if t40 int== 0 goto L50
    406        t39 = t39 int* t37
    407  L50:  t37 = t37 int* t37
    408        t38 = t38 int>> 1
    409        goto L49
    410  L51:  t41 = 2
    411        t42 = 10
    412        t43 = 1
    413  L52:  if t42 int<= 0 goto L54
    414        t44 = t42 int& 1
    415        if t44 int== 0 goto L53
    416        t43 = t43 int* t41
    417  L53:  t41 = t41 int* t41
    418        t42 = t42 int>> 1
    419        goto L52
    420  L54:  param "%d %d %d\n"
    421        param t27
    422        param t39
    423        param t43
    424        call printf, 4
    425        param t3
    426        param 8
    427        param 88
    428        t31 = call search(int *, int, int), 3
    429        return t31


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   bubble             function      void (int *, int)          -           3    -    1  _Z6bubblePii; defined
   quick              function      void (int *, int, int)     -           9    -    3  _Z5quickPiii; defined
   search             function      int (int *, int, int)      -          21    -    4  _Z6searchPiii; defined
   moves              variable      int                        global     31    4    2  
   hanoi              function      void (int, int, int, int)  -          32    -    3  _Z5hanoiiiii; defined
   ackermann          function      int (int, int)             -          39    -    4  _Z9ackermannii; defined
   multiply           function      void (int (*)[3], int (*)[2], int (*)[2]) -          45    -    1  _Z8multiplyPA3_iPA2_iS2_; defined
   primes             function      int (int)                  -          53    -    1  _Z6primesi; defined
   power              function      int (int, int)             -          65    -    2  _Z5powerii; defined
   collatz            function      int (int)                  -          75    -    1  _Z7collatzi; defined
   main               function      int (void)                 -          77    -    0  defined

 scope: global > bubble()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       3    4    6  a.1
   n                  parameter     int                        param       3    4    2  n.2

 scope: global > bubble() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       4    4    3  i.3

 scope: global > bubble() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local       5    4    8  j.4

 scope: global > bubble() > for > for body > for > for body > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local       6    4    1  t.5

 scope: global > quick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       9    4    9  a.6
   lo                 parameter     int                        param       9    4    4  lo.7
   hi                 parameter     int                        param       9    4    4  hi.8
   pivot              variable      int                        local      11    4    2  pivot.9
   i                  variable      int                        local      11    4    8  i.10
   j                  variable      int                        local      11    4    8  j.11

 scope: global > quick() > while > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local      15    4    1  t.12

 scope: global > search()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param      21    4    2  a.13
   n                  parameter     int                        param      21    4    1  n.14
   key                parameter     int                        param      21    4    2  key.15
   lo                 variable      int                        local      22    4    4  lo.16
   hi                 variable      int                        local      22    4    3  hi.17

 scope: global > search() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   mid                variable      int                        local      24    4    5  mid.18

 scope: global > hanoi()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      32    4    3  n.19
   from               parameter     int                        param      32    4    2  from.20
   to                 parameter     int                        param      32    4    2  to.21
   via                parameter     int                        param      32    4    2  via.22

 scope: global > ackermann()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int                        param      39    4    4  m.23
   n                  parameter     int                        param      39    4    3  n.24

 scope: global > multiply()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int (*)[3]                 param      45    4    1  a.25
   b                  parameter     int (*)[2]                 param      45    4    1  b.26
   c                  parameter     int (*)[2]                 param      45    4    2  c.27

 scope: global > multiply() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      46    4    5  i.28

 scope: global > multiply() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      47    4    5  j.29

 scope: global > multiply() > for > for body > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      49    4    4  k.30

 scope: global > primes()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   limit              parameter     int                        param      53    4    3  limit.31
   composite          variable      char[101]                  local      54  101    3  composite.32
   count              variable      int                        local      55    4    2  count.33

 scope: global > primes() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      56    4    3  i.34
   i                  variable      int                        local      57    4    6  i.35

 scope: global > primes() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      60    4    3  j.36

 scope: global > power()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   base               parameter     int                        param      65    4    3  base.37
   exp                parameter     int                        param      65    4    3  exp.38
   result             variable      int                        local      66    4    2  result.39

 scope: global > collatz()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      75    4    5  n.40
   steps              variable      int                        local      75    4    2  steps.41

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int[8]                     local      78   32    5  a.42
   b                  variable      int[8]                     local      78   32    3  b.43
   x                  variable      int[2][3]                  local      87   24    1  x.46
   y                  variable      int[3][2]                  local      87   24    1  y.47
   z                  variable      int[2][2]                  local      87   16    5  z.48

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      81    4    3  i.44
   i                  variable      int                        local      83    4    3  i.45

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
