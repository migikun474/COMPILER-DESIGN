============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_algorithms.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 401 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 5 parameter(s)/local(s), 24 temporaries, frame 116 bytes

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
   t14              temp    int                             4      72
   t15              temp    int *                           4      76
   t16              temp    int                             4      80
   t17              temp    int                             4      84
   t18              temp    int *                           4      88
   t19              temp    int                             4      92
   t20              temp    int                             4      96
   t21              temp    int                             4     100
   t22              temp    int *                           4     104
   t23              temp    int                             4     108
   t24              temp    int                             4     112

 Code: 40 instruction(s)

    100       i = 0
    101  L1:  t1 = n int- 1
    102       if i int< t1 goto L2
    103       goto L8
    104  L2:  j = 0
    105  L3:  t2 = n int- 1
    106       t3 = t2 int- i
    107       if j int< t3 goto L4
    108       goto L7
    109  L4:  t4 = j int* 4
    110       t5 = a ptr+ t4
    111       t6 = *t5
    112       t7 = j int+ 1
    113       t8 = t7 int* 4
    114       t9 = a ptr+ t8
    115       t10 = *t9
    116       if t6 int> t10 goto L5
    117       goto L6
    118  L5:  t11 = j int* 4
    119       t12 = a ptr+ t11
    120       t13 = *t12
    121       t = t13
    122       t14 = j int* 4
    123       t15 = a ptr+ t14
    124       t16 = j int+ 1
    125       t17 = t16 int* 4
    126       t18 = a ptr+ t17
    127       t19 = *t18
    128       *t15 = t19
    129       t20 = j int+ 1
    130       t21 = t20 int* 4
    131       t22 = a ptr+ t21
    132       *t22 = t
    133  L6:  t23 = j int+ 1
    134       j = t23
    135       goto L3
    136  L7:  t24 = i int+ 1
    137       i = t24
    138       goto L1
    139  L8:  return

============================================================================
 FUNCTION quick(int *, int, int)        (link name _Z5quickPiii)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 25 temporaries, frame 128 bytes

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

    140        if lo int>= hi goto L9
    141        goto L10
    142  L9:   return
    143  L10:  t1 = lo int+ hi
    144        t2 = t1 int/ 2
    145        t3 = t2 int* 4
    146        t4 = a ptr+ t3
    147        t5 = *t4
    148        pivot = t5
    149        i = lo
    150        j = hi
    151  L11:  if i int<= j goto L12
    152        goto L18
    153  L12:  t6 = i int* 4
    154        t7 = a ptr+ t6
    155        t8 = *t7
    156        if t8 int< pivot goto L13
    157        goto L14
    158  L13:  t9 = i int+ 1
    159        i = t9
    160        goto L12
    161  L14:  t10 = j int* 4
    162        t11 = a ptr+ t10
    163        t12 = *t11
    164        if t12 int> pivot goto L15
    165        goto L16
    166  L15:  t13 = j int- 1
    167        j = t13
    168        goto L14
    169  L16:  if i int<= j goto L17
    170        goto L11
    171  L17:  t14 = i int* 4
    172        t15 = a ptr+ t14
    173        t16 = *t15
    174        t = t16
    175        t17 = i int* 4
    176        t18 = a ptr+ t17
    177        t19 = j int* 4
    178        t20 = a ptr+ t19
    179        t21 = *t20
    180        *t18 = t21
    181        t22 = j int* 4
    182        t23 = a ptr+ t22
    183        *t23 = t
    184        t24 = i int+ 1
    185        i = t24
    186        t25 = j int- 1
    187        j = t25
    188        goto L11
    189  L18:  param a
    190        param lo
    191        param j
    192        call quick(int *, int, int), 3
    193        param a
    194        param i
    195        param hi
    196        call quick(int *, int, int), 3
    197        return

============================================================================
 FUNCTION search(int *, int, int)        (link name _Z6searchPiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 13 temporaries, frame 76 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   key              param   int                             4       8
   lo               local   int                             4      12
   hi               local   int                             4      16
   mid              local   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40
   t6               temp    int *                           4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int *                           4      56
   t10              temp    int                             4      60
   t11              temp    int                             4      64
   t12              temp    int                             4      68
   t13              temp    int                             4      72

 Code: 28 instruction(s)

    198        lo = 0
    199        t1 = n int- 1
    200        hi = t1
    201  L19:  if lo int<= hi goto L20
    202        goto L25
    203  L20:  t2 = hi int- lo
    204        t3 = t2 int/ 2
    205        t4 = lo int+ t3
    206        mid = t4
    207        t5 = mid int* 4
    208        t6 = a ptr+ t5
    209        t7 = *t6
    210        if t7 int== key goto L21
    211        goto L22
    212  L21:  return mid
    213  L22:  t8 = mid int* 4
    214        t9 = a ptr+ t8
    215        t10 = *t9
    216        if t10 int< key goto L23
    217        goto L24
    218  L23:  t11 = mid int+ 1
    219        lo = t11
    220        goto L19
    221  L24:  t12 = mid int- 1
    222        hi = t12
    223        goto L19
    224  L25:  t13 = int- 1
    225        return t13

============================================================================
 FUNCTION hanoi(int, int, int, int)        (link name _Z5hanoiiiii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   from             param   int                             4       4
   to               param   int                             4       8
   via              param   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24

 Code: 18 instruction(s)

    226        if n int== 0 goto L26
    227        goto L27
    228  L26:  return
    229  L27:  t1 = n int- 1
    230        param t1
    231        param from
    232        param via
    233        param to
    234        call hanoi(int, int, int, int), 4
    235        t2 = moves int+ 1
    236        moves = t2
    237        t3 = n int- 1
    238        param t3
    239        param via
    240        param to
    241        param from
    242        call hanoi(int, int, int, int), 4
    243        return

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

 Code: 20 instruction(s)

    244        if m int== 0 goto L28
    245        goto L29
    246  L28:  t1 = n int+ 1
    247        return t1
    248  L29:  if n int== 0 goto L30
    249        goto L31
    250  L30:  t2 = m int- 1
    251        param t2
    252        param 1
    253        t3 = call ackermann(int, int), 2
    254        return t3
    255  L31:  t4 = m int- 1
    256        t5 = n int- 1
    257        param m
    258        param t5
    259        t6 = call ackermann(int, int), 2
    260        param t4
    261        param t6
    262        t7 = call ackermann(int, int), 2
    263        return t7

============================================================================
 FUNCTION multiply(int (*)[3], int (*)[2], int (*)[2])        (link name _Z8multiplyPA3_iPA2_iS2_)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 24 temporaries, frame 120 bytes

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
   t17              temp    int                             4      88
   t18              temp    int (*)[2]                      4      92
   t19              temp    int                             4      96
   t20              temp    int                             4     100
   t21              temp    int                             4     104
   t22              temp    int                             4     108
   t23              temp    int                             4     112
   t24              temp    int                             4     116

 Code: 42 instruction(s)

    264        i = 0
    265  L32:  if i int< 2 goto L33
    266        goto L40
    267  L33:  j = 0
    268  L34:  if j int< 2 goto L35
    269        goto L39
    270  L35:  t1 = i int* 8
    271        t2 = c ptr+ t1
    272        t3 = j int* 4                       (w = 4)
    273        t4 = t2 ptr+ t3
    274        *t4 = 0
    275        k = 0
    276  L36:  if k int< 3 goto L37
    277        goto L38
    278  L37:  t5 = i int* 8
    279        t6 = c ptr+ t5
    280        t7 = j int* 4                       (w = 4)
    281        t8 = t6 ptr+ t7
    282        t9 = *t8
    283        t10 = i int* 12
    284        t11 = a ptr+ t10
    285        t12 = k int* 4                      (w = 4)
    286        t13 = t11 ptr+ t12
    287        t14 = *t13
    288        t15 = k int* 8
    289        t16 = b ptr+ t15
    290        t17 = j int* 4                      (w = 4)
    291        t18 = t16 ptr+ t17
    292        t19 = *t18
    293        t20 = t14 int* t19
    294        t21 = t9 int+ t20
    295        *t8 = t21
    296        t22 = k int+ 1
    297        k = t22
    298        goto L36
    299  L38:  t23 = j int+ 1
    300        j = t23
    301        goto L34
    302  L39:  t24 = i int+ 1
    303        i = t24
    304        goto L32
    305  L40:  return

============================================================================
 FUNCTION primes(int)        (link name _Z6primesi)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 6 temporaries, frame 148 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   limit            param   int                             4       0
   composite        local   char[101]                     101       4
   count            local   int                             4     108
   i.34             local   int                             4     112
   i.35             local   int                             4     116
   j                local   int                             4     120
   t1               temp    int                             4     124
   t2               temp    char                            1     128
   t3               temp    int                             4     132
   t4               temp    int                             4     136
   t5               temp    int                             4     140
   t6               temp    int                             4     144

 Code: 29 instruction(s)

    306        count = 0
    307        i.34 = 0
    308  L41:  if i.34 int<= limit goto L42
    309        goto L43
    310  L42:  composite[i.34] = 0
    311        t1 = i.34 int+ 1
    312        i.34 = t1
    313        goto L41
    314  L43:  i.35 = 2
    315  L44:  if i.35 int<= limit goto L45
    316        goto L51
    317  L45:  t2 = composite[i.35]
    318        if t2 char!= 0 goto L46
    319        goto L47
    320  L46:  goto L50
    321  L47:  t3 = count int+ 1
    322        count = t3
    323        t4 = i.35 int* i.35
    324        j = t4
    325  L48:  if j int<= limit goto L49
    326        goto L50
    327  L49:  composite[j] = 1
    328        t5 = j int+ i.35
    329        j = t5
    330        goto L48
    331  L50:  t6 = i.35 int+ 1
    332        i.35 = t6
    333        goto L44
    334  L51:  return count

============================================================================
 FUNCTION power(int, int)        (link name _Z5powerii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   base             param   int                             4       0
   exp              param   int                             4       4
   result           local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24

 Code: 14 instruction(s)

    335        result = 1
    336  L52:  if exp int> 0 goto L53
    337        goto L56
    338  L53:  t1 = exp int& 1
    339        if t1 int!= 0 goto L54
    340        goto L55
    341  L54:  t2 = result int* base
    342        result = t2
    343  L55:  t3 = base int* base
    344        base = t3
    345        t4 = exp int>> 1
    346        exp = t4
    347        goto L52
    348  L56:  return result

============================================================================
 FUNCTION collatz(int)        (link name _Z7collatzi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   steps            local   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   t6               temp    int                             4      28

 Code: 17 instruction(s)

    349        steps = 0
    350  L57:  if n int!= 1 goto L58
    351        goto L62
    352  L58:  t2 = n int% 2
    353        if t2 int!= 0 goto L59
    354        goto L60
    355  L59:  t3 = 3 int* n
    356        t4 = t3 int+ 1
    357        t1 = t4
    358        goto L61
    359  L60:  t5 = n int/ 2
    360        t1 = t5
    361  L61:  n = t1
    362        t6 = steps int+ 1
    363        steps = t6
    364        goto L57
    365  L62:  return steps

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 31 temporaries, frame 260 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int[8]                         32       0
   b                local   int[8]                         32      32
   i.44             local   int                             4      64
   i.45             local   int                             4      68
   x                local   int[2][3]                      24      72
   y                local   int[3][2]                      24      96
   z                local   int[2][2]                      16     120
   t1               temp    int                             4     136
   t2               temp    int                             4     140
   t3               temp    int (*)[8]                      4     144
   t4               temp    int (*)[8]                      4     148
   t5               temp    int                             4     152
   t6               temp    int                             4     156
   t7               temp    int                             4     160
   t8               temp    int                             4     164
   t9               temp    int                             4     168
   t10              temp    int                             4     172
   t11              temp    int (*)[8]                      4     176
   t12              temp    int                             4     180
   t13              temp    int (*)[8]                      4     184
   t14              temp    int                             4     188
   t15              temp    int (*)[8]                      4     192
   t16              temp    int                             4     196
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
   t30              temp    int (*)[8]                      4     252
   t31              temp    int                             4     256

 Code: 135 instruction(s)

    366        a[0] = 42
    367        a[4] = 7
    368        a[8] = 19
    369        a[12] = 3
    370        a[16] = 25
    371        a[20] = 7
    372        a[24] = 88
    373        a[28] = 1
    374        t1 = int- 2
    375        t2 = int- 7
    376        b[0] = 5
    377        b[4] = t1
    378        b[8] = 9
    379        b[12] = 0
    380        b[16] = 9
    381        b[20] = 14
    382        b[24] = t2
    383        b[28] = 3
    384        t3 = &a
    385        param t3
    386        param 8
    387        call bubble(int *, int), 2
    388        t4 = &b
    389        param t4
    390        param 0
    391        param 7
    392        call quick(int *, int, int), 3
    393        i.44 = 0
    394  L63:  if i.44 int< 8 goto L64
    395        goto L65
    396  L64:  t5 = i.44 int* 4                    (w = 4)
    397        t6 = a[t5]
    398        param "%d "
    399        param t6
    400        call printf, 2
    401        t7 = i.44 int+ 1
    402        i.44 = t7
    403        goto L63
    404  L65:  param "\n"
    405        call printf, 1
    406        i.45 = 0
    407  L66:  if i.45 int< 8 goto L67
    408        goto L68
    409  L67:  t8 = i.45 int* 4                    (w = 4)
    410        t9 = b[t8]
    411        param "%d "
    412        param t9
    413        call printf, 2
    414        t10 = i.45 int+ 1
    415        i.45 = t10
    416        goto L66
    417  L68:  t11 = &a
    418        param t11
    419        param 8
    420        param 25
    421        t12 = call search(int *, int, int), 3
    422        t13 = &a
    423        param t13
    424        param 8
    425        param 26
    426        t14 = call search(int *, int, int), 3
    427        t15 = &b
    428        t16 = int- 7
    429        param t15
    430        param 8
    431        param t16
    432        t17 = call search(int *, int, int), 3
    433        param "\n%d %d %d\n"
    434        param t12
    435        param t14
    436        param t17
    437        call printf, 4
    438        param 6
    439        param 1
    440        param 3
    441        param 2
    442        call hanoi(int, int, int, int), 4
    443        param 2
    444        param 3
    445        t18 = call ackermann(int, int), 2
    446        param 27
    447        t19 = call collatz(int), 1
    448        param "%d %d %d\n"
    449        param moves
    450        param t18
    451        param t19
    452        call printf, 4
    453        x[0] = 1
    454        x[4] = 2
    455        x[8] = 3
    456        x[12] = 4
    457        x[16] = 5
    458        x[20] = 6
    459        y[0] = 7
    460        y[4] = 8
    461        y[8] = 9
    462        y[12] = 10
    463        y[16] = 11
    464        y[20] = 12
    465        t20 = &x
    466        t21 = &y
    467        t22 = &z
    468        param t20
    469        param t21
    470        param t22
    471        call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
    472        t23 = z[0]
    473        t24 = z[4]
    474        t25 = z[8]
    475        t26 = z[12]
    476        param "%d %d %d %d\n"
    477        param t23
    478        param t24
    479        param t25
    480        param t26
    481        call printf, 5
    482        param 100
    483        t27 = call primes(int), 1
    484        param 3
    485        param 13
    486        t28 = call power(int, int), 2
    487        param 2
    488        param 10
    489        t29 = call power(int, int), 2
    490        param "%d %d %d\n"
    491        param t27
    492        param t28
    493        param t29
    494        call printf, 4
    495        t30 = &a
    496        param t30
    497        param 8
    498        param 88
    499        t31 = call search(int *, int, int), 3
    500        return t31


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
