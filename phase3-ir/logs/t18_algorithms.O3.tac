============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_algorithms.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 401 -> 395 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          401 -> 395   (1% fewer)

   constants folded                        4
   algebraic simplifications              24
   common subexpressions                  13
   copies / constants forwarded           53
   temporaries merged away                28
   dead instructions removed              45
   jumps removed or redirected            28
   unreachable instructions removed        5
   propagated across blocks                5
   dead assignments removed                4
   calls inlined                           3
   tail calls turned into jumps            4
   common subexpressions across blocks     13
   loops unrolled                         13
   unreachable functions removed           2

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

 Code: 40 instruction(s)

    100       i = 0
    101  L1:  t1 = n int- 1
    102       if i int>= t1 goto L6
    103       j = 0
    104  L2:  t2 = n int- 1
    105       t3 = t2 int- i
    106       if j int>= t3 goto L5
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
    120       t2 = n int- 1
    121       t3 = t2 int- i
    122       if j int>= t3 goto L5
    123       t4 = j int<< 2
    124       t5 = a ptr+ t4
    125       t6 = *t5
    126       t7 = j int+ 1
    127       t8 = t7 int<< 2
    128       t9 = a ptr+ t8
    129       t10 = *t9
    130       if t6 int<= t10 goto L4
    131       t13 = *t5
    132       t19 = *t9
    133       *t5 = t19
    134       *t9 = t13
    135  L4:  j = j int+ 1
    136       goto L2
    137  L5:  i = i int+ 1
    138       goto L1
    139  L6:  return

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

 Code: 46 instruction(s)

    140  L7:   if lo int< hi goto L8
    141        return
    142  L8:   t1 = lo int+ hi
    143        t2 = t1 int/ 2
    144        t3 = t2 int<< 2
    145        t4 = a ptr+ t3
    146        pivot = *t4
    147        i = lo
    148        j = hi
    149  L9:   if i int> j goto L13
    150  L10:  t6 = i int<< 2
    151        t7 = a ptr+ t6
    152        t8 = *t7
    153        if t8 int>= pivot goto L11
    154        i = i int+ 1
    155        t6 = i int<< 2
    156        t7 = a ptr+ t6
    157        t8 = *t7
    158        if t8 int>= pivot goto L11
    159        i = i int+ 1
    160        goto L10
    161  L11:  t10 = j int<< 2
    162        t11 = a ptr+ t10
    163        t12 = *t11
    164        if t12 int<= pivot goto L12
    165        j = j int- 1
    166        t10 = j int<< 2
    167        t11 = a ptr+ t10
    168        t12 = *t11
    169        if t12 int<= pivot goto L12
    170        j = j int- 1
    171        goto L11
    172  L12:  if i int> j goto L9
    173        t16 = *t7
    174        t21 = *t11
    175        *t7 = t21
    176        *t11 = t16
    177        i = i int+ 1
    178        j = j int- 1
    179        goto L9
    180  L13:  param a
    181        param lo
    182        param j
    183        call quick(int *, int, int), 3
    184        lo = i
    185        goto L7

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

    186        lo = 0
    187        hi = n int- 1
    188  L14:  if lo int> hi goto L17
    189        t2 = hi int- lo
    190        t3 = t2 int/ 2
    191        t4 = lo int+ t3
    192        t5 = t4 int<< 2
    193        t6 = a ptr+ t5
    194        t7 = *t6
    195        if t7 int!= key goto L15
    196        return t4
    197  L15:  t10 = *t6
    198        if t10 int>= key goto L16
    199        lo = t4 int+ 1
    200        goto L14
    201  L16:  hi = t4 int- 1
    202        goto L14
    203  L17:  return -1

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

    204  L18:  if n int!= 0 goto L19
    205        return
    206  L19:  t1 = n int- 1
    207        param t1
    208        param from
    209        param via
    210        param to
    211        call hanoi(int, int, int, int), 4
    212        moves = moves int+ 1
    213        t7 = from
    214        n = t1
    215        from = via
    216        via = t7
    217        goto L18

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

    218  L20:  if m int!= 0 goto L21
    219        t1 = n int+ 1
    220        return t1
    221  L21:  if n int!= 0 goto L22
    222        m = m int- 1
    223        n = 1
    224        goto L20
    225  L22:  t4 = m int- 1
    226        t5 = n int- 1
    227        param m
    228        param t5
    229        t6 = call ackermann(int, int), 2
    230        m = t4
    231        n = t6
    232        goto L20

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

 Code: 54 instruction(s)

    233        i = 0
    234  L23:  if i int>= 2 goto L28
    235        j = 0
    236  L24:  if j int>= 2 goto L27
    237        t1 = i int<< 3
    238        t2 = c ptr+ t1
    239        t3 = j int<< 2                      (w = 4)
    240        t4 = t2 ptr+ t3
    241        *t4 = 0
    242        k = 0
    243  L25:  if k int>= 3 goto L26
    244        t5 = i int<< 3
    245        t6 = c ptr+ t5
    246        t7 = j int<< 2                      (w = 4)
    247        t8 = t6 ptr+ t7
    248        t9 = *t8
    249        t10 = i int* 12
    250        t11 = a ptr+ t10
    251        t12 = k int<< 2                     (w = 4)
    252        t13 = t11 ptr+ t12
    253        t14 = *t13
    254        t15 = k int<< 3
    255        t16 = b ptr+ t15
    256        t18 = t16 ptr+ t7
    257        t19 = *t18
    258        t20 = t14 int* t19
    259        t21 = t9 int+ t20
    260        *t8 = t21
    261        k = k int+ 1
    262        if k int>= 3 goto L26
    263        t5 = i int<< 3
    264        t6 = c ptr+ t5
    265        t7 = j int<< 2                      (w = 4)
    266        t8 = t6 ptr+ t7
    267        t9 = *t8
    268        t10 = i int* 12
    269        t11 = a ptr+ t10
    270        t12 = k int<< 2                     (w = 4)
    271        t13 = t11 ptr+ t12
    272        t14 = *t13
    273        t15 = k int<< 3
    274        t16 = b ptr+ t15
    275        t18 = t16 ptr+ t7
    276        t19 = *t18
    277        t20 = t14 int* t19
    278        t21 = t9 int+ t20
    279        *t8 = t21
    280        k = k int+ 1
    281        goto L25
    282  L26:  j = j int+ 1
    283        goto L24
    284  L27:  i = i int+ 1
    285        goto L23
    286  L28:  return

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

 Code: 25 instruction(s)

    287        count = 0
    288        i.34 = 0
    289  L29:  if i.34 int> limit goto L30
    290        composite[i.34] = 0
    291        i.34 = i.34 int+ 1
    292        if i.34 int> limit goto L30
    293        composite[i.34] = 0
    294        i.34 = i.34 int+ 1
    295        goto L29
    296  L30:  i.35 = 2
    297  L31:  if i.35 int> limit goto L34
    298        t2 = composite[i.35]
    299        if t2 char!= 0 goto L33
    300        count = count int+ 1
    301        j = i.35 int* i.35
    302  L32:  if j int> limit goto L33
    303        composite[j] = 1
    304        j = j int+ i.35
    305        if j int> limit goto L33
    306        composite[j] = 1
    307        j = j int+ i.35
    308        goto L32
    309  L33:  i.35 = i.35 int+ 1
    310        goto L31
    311  L34:  return count

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

 Code: 183 instruction(s)

    312        a[0] = 42
    313        a[4] = 7
    314        a[8] = 19
    315        a[12] = 3
    316        a[16] = 25
    317        a[20] = 7
    318        a[24] = 88
    319        a[28] = 1
    320        b[0] = 5
    321        b[4] = -2
    322        b[8] = 9
    323        b[12] = 0
    324        b[16] = 9
    325        b[20] = 14
    326        b[24] = -7
    327        b[28] = 3
    328        t3 = &a
    329        param t3
    330        param 8
    331        call bubble(int *, int), 2
    332        t4 = &b
    333        param t4
    334        param 0
    335        param 7
    336        call quick(int *, int, int), 3
    337        i.44 = 0
    338  L35:  if i.44 int>= 8 goto L36
    339        t5 = i.44 int<< 2                   (w = 4)
    340        t6 = a[t5]
    341        param "%d "
    342        param t6
    343        call printf, 2
    344        i.44 = i.44 int+ 1
    345        if i.44 int>= 8 goto L36
    346        t5 = i.44 int<< 2                   (w = 4)
    347        t6 = a[t5]
    348        param "%d "
    349        param t6
    350        call printf, 2
    351        i.44 = i.44 int+ 1
    352        goto L35
    353  L36:  param "\n"
    354        call printf, 1
    355        i.45 = 0
    356  L37:  if i.45 int>= 8 goto L38
    357        t8 = i.45 int<< 2                   (w = 4)
    358        t9 = b[t8]
    359        param "%d "
    360        param t9
    361        call printf, 2
    362        i.45 = i.45 int+ 1
    363        if i.45 int>= 8 goto L38
    364        t8 = i.45 int<< 2                   (w = 4)
    365        t9 = b[t8]
    366        param "%d "
    367        param t9
    368        call printf, 2
    369        i.45 = i.45 int+ 1
    370        goto L37
    371  L38:  param t3
    372        param 8
    373        param 25
    374        t12 = call search(int *, int, int), 3
    375        param t3
    376        param 8
    377        param 26
    378        t14 = call search(int *, int, int), 3
    379        param t4
    380        param 8
    381        param -7
    382        t17 = call search(int *, int, int), 3
    383        param "\n%d %d %d\n"
    384        param t12
    385        param t14
    386        param t17
    387        call printf, 4
    388        param 6
    389        param 1
    390        param 3
    391        param 2
    392        call hanoi(int, int, int, int), 4
    393        param 2
    394        param 3
    395        t18 = call ackermann(int, int), 2
    396        t32 = 27
    397        t33 = 0
    398  L39:  if t32 int== 1 goto L44
    399        t34 = t32 int% 2
    400        if t34 int== 0 goto L40
    401        t35 = t32 int* 3
    402        t36 = t35 int+ 1
    403        goto L41
    404  L40:  t36 = t32 int/ 2
    405  L41:  t32 = t36
    406        t33 = t33 int+ 1
    407        if t36 int== 1 goto L44
    408        t34 = t32 int% 2
    409        if t34 int== 0 goto L42
    410        t35 = t32 int* 3
    411        t36 = t35 int+ 1
    412        goto L43
    413  L42:  t36 = t32 int/ 2
    414  L43:  t32 = t36
    415        t33 = t33 int+ 1
    416        goto L39
    417  L44:  param "%d %d %d\n"
    418        param moves
    419        param t18
    420        param t33
    421        call printf, 4
    422        x[0] = 1
    423        x[4] = 2
    424        x[8] = 3
    425        x[12] = 4
    426        x[16] = 5
    427        x[20] = 6
    428        y[0] = 7
    429        y[4] = 8
    430        y[8] = 9
    431        y[12] = 10
    432        y[16] = 11
    433        y[20] = 12
    434        t20 = &x
    435        t21 = &y
    436        t22 = &z
    437        param t20
    438        param t21
    439        param t22
    440        call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
    441        t23 = z[0]
    442        t24 = z[4]
    443        t25 = z[8]
    444        t26 = z[12]
    445        param "%d %d %d %d\n"
    446        param t23
    447        param t24
    448        param t25
    449        param t26
    450        call printf, 5
    451        param 100
    452        t27 = call primes(int), 1
    453        t37 = 3
    454        t38 = 13
    455        t39 = 1
    456  L45:  if t38 int<= 0 goto L48
    457        t40 = t38 int& 1
    458        if t40 int== 0 goto L46
    459        t39 = t39 int* t37
    460  L46:  t37 = t37 int* t37
    461        t38 = t38 int>> 1
    462        if t38 int<= 0 goto L48
    463        t40 = t38 int& 1
    464        if t40 int== 0 goto L47
    465        t39 = t39 int* t37
    466  L47:  t37 = t37 int* t37
    467        t38 = t38 int>> 1
    468        goto L45
    469  L48:  t41 = 2
    470        t42 = 10
    471        t43 = 1
    472  L49:  if t42 int<= 0 goto L52
    473        t44 = t42 int& 1
    474        if t44 int== 0 goto L50
    475        t43 = t43 int* t41
    476  L50:  t41 = t41 int* t41
    477        t42 = t42 int>> 1
    478        if t42 int<= 0 goto L52
    479        t44 = t42 int& 1
    480        if t44 int== 0 goto L51
    481        t43 = t43 int* t41
    482  L51:  t41 = t41 int* t41
    483        t42 = t42 int>> 1
    484        goto L49
    485  L52:  param "%d %d %d\n"
    486        param t27
    487        param t39
    488        param t43
    489        call printf, 4
    490        param t3
    491        param 8
    492        param 88
    493        t31 = call search(int *, int, int), 3
    494        return t31


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
