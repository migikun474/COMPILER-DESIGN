============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t28_o3.c
   Optimization  : no optimization
   Result        : Three address code generated: 16 function(s), 313 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

============================================================================
 FUNCTION square(int)        (link name _Z6squarei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    100     t1 = v int* v
    101     return t1

============================================================================
 FUNCTION clamp(int, int, int)        (link name _Z5clampiii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   lo               param   int                             4       4
   hi               param   int                             4       8

 Code: 7 instruction(s)

    102       if v int< lo goto L1
    103       goto L2
    104  L1:  return lo
    105  L2:  if v int> hi goto L3
    106       goto L4
    107  L3:  return hi
    108  L4:  return v

============================================================================
 FUNCTION counted(int)        (link name _Z7countedi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    109     t1 = calls int+ 1
    110     calls = t1
    111     t2 = v int+ calls
    112     return t2

============================================================================
 FUNCTION bump(int &, int)        (link name _Z4bumpRii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   int &                           4       0
   by               param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 4 instruction(s)

    113     t1 = *r
    114     t2 = t1 int+ by
    115     *r = t2
    116     return

============================================================================
 FUNCTION total(struct Pair)        (link name _Z5total4Pair)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Pair                     8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24

 Code: 7 instruction(s)

    117     t1 = p[0]
    118     t2 = t1 int+ 1
    119     p[0] = t2
    120     t3 = p[0]
    121     t4 = p[4]
    122     t5 = t3 int+ t4
    123     return t5

============================================================================
 FUNCTION fact(int)        (link name _Z4facti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16

 Code: 10 instruction(s)

    124       if n int<= 1 goto L5
    125       goto L6
    126  L5:  t1 = 1
    127       goto L7
    128  L6:  t2 = n int- 1
    129       param t2
    130       t3 = call fact(int), 1
    131       t4 = n int* t3
    132       t1 = t4
    133  L7:  return t1

============================================================================
 FUNCTION gcd(int, int)        (link name _Z3gcdii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 8 instruction(s)

    134       if b int== 0 goto L8
    135       goto L9
    136  L8:  return a
    137  L9:  t1 = a int% b
    138       param b
    139       param t1
    140       t2 = call gcd(int, int), 2
    141       return t2

============================================================================
 FUNCTION sumTo(int, int)        (link name _Z5sumToii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   acc              param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 9 instruction(s)

    142        if n int== 0 goto L10
    143        goto L11
    144  L10:  return acc
    145  L11:  t1 = n int- 1
    146        t2 = acc int+ n
    147        param t1
    148        param t2
    149        t3 = call sumTo(int, int), 2
    150        return t3

============================================================================
 FUNCTION countDown(int)        (link name _Z9countDowni)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 7 instruction(s)

    151        if n int<= 0 goto L12
    152        goto L13
    153  L12:  return 0
    154  L13:  t1 = n int- 2
    155        param t1
    156        t2 = call countDown(int), 1
    157        return t2

============================================================================
 FUNCTION invariant(int, int)        (link name _Z9invariantii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 7 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   k                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   scale            local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44

 Code: 20 instruction(s)

    158        s = 0
    159        i = 0
    160  L14:  if i int< n goto L15
    161        goto L19
    162  L15:  t1 = k int* 3
    163        t2 = t1 int+ 1
    164        scale = t2
    165        t3 = i int* scale
    166        t4 = s int+ t3
    167        s = t4
    168        if i int== 2 goto L16
    169        goto L17
    170  L16:  goto L18
    171  L17:  t5 = k int* 3
    172        t6 = s int+ t5
    173        s = t6
    174  L18:  t7 = i int+ 1
    175        i = t7
    176        goto L14
    177  L19:  return s

============================================================================
 FUNCTION notInvariant(int)        (link name _Z12notInvarianti)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 4 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   s                local   int                             4       4
   k                local   int                             4       8
   i                local   int                             4      12
   v                local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32

 Code: 15 instruction(s)

    178        s = 0
    179        k = 1
    180        i = 0
    181  L20:  if i int< n goto L21
    182        goto L22
    183  L21:  t1 = k int* 3
    184        v = t1
    185        t2 = s int+ v
    186        s = t2
    187        t3 = k int+ i
    188        k = t3
    189        t4 = i int+ 1
    190        i = t4
    191        goto L20
    192  L22:  return s

============================================================================
 FUNCTION zeroTrips(int, int)        (link name _Z9zeroTripsii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   d                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20

 Code: 10 instruction(s)

    193        s = 7
    194  L23:  if n int> 0 goto L24
    195        goto L25
    196  L24:  t1 = 100 int/ d
    197        t2 = s int+ t1
    198        s = t2
    199        t3 = n int- 1
    200        n = t3
    201        goto L23
    202  L25:  return s

============================================================================
 FUNCTION nested(int, int)        (link name _Z6nestedii)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 14 temporaries, frame 164 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   rows             param   int                             4       0
   cols             param   int                             4       4
   grid             local   int[4][5]                      80       8
   s                local   int                             4      88
   r.32             local   int                             4      92
   c.33             local   int                             4      96
   r.34             local   int                             4     100
   c.35             local   int                             4     104
   t1               temp    int                             4     108
   t2               temp    int                             4     112
   t3               temp    int                             4     116
   t4               temp    int                             4     120
   t5               temp    int                             4     124
   t6               temp    int                             4     128
   t7               temp    int                             4     132
   t8               temp    int                             4     136
   t9               temp    int                             4     140
   t10              temp    int                             4     144
   t11              temp    int                             4     148
   t12              temp    int                             4     152
   t13              temp    int                             4     156
   t14              temp    int                             4     160

 Code: 38 instruction(s)

    203        s = 0
    204        r.32 = 0
    205  L26:  if r.32 int< rows goto L27
    206        goto L31
    207  L27:  c.33 = 0
    208  L28:  if c.33 int< cols goto L29
    209        goto L30
    210  L29:  t1 = r.32 int* 5                    (n2 = 5)
    211        t2 = t1 int+ c.33
    212        t3 = t2 int* 4                      (w = 4)
    213        t4 = r.32 int* cols
    214        t5 = t4 int+ c.33
    215        grid[t3] = t5
    216        t6 = c.33 int+ 1
    217        c.33 = t6
    218        goto L28
    219  L30:  t7 = r.32 int+ 1
    220        r.32 = t7
    221        goto L26
    222  L31:  r.34 = 0
    223  L32:  if r.34 int< rows goto L33
    224        goto L37
    225  L33:  c.35 = 0
    226  L34:  if c.35 int< cols goto L35
    227        goto L36
    228  L35:  t8 = r.34 int* 5                    (n2 = 5)
    229        t9 = t8 int+ c.35
    230        t10 = t9 int* 4                     (w = 4)
    231        t11 = grid[t10]
    232        t12 = s int+ t11
    233        s = t12
    234        t13 = c.35 int+ 1
    235        c.35 = t13
    236        goto L34
    237  L36:  t14 = r.34 int+ 1
    238        r.34 = t14
    239        goto L32
    240  L37:  return s

============================================================================
 FUNCTION shared(int, int, int)        (link name _Z6sharediii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 11 temporaries, frame 64 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   y                param   int                             4       4
   flag             param   int                             4       8
   a                local   int                             4      12
   b                local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   t9               temp    int                             4      52
   t10              temp    int                             4      56
   t11              temp    int                             4      60

 Code: 19 instruction(s)

    241        t1 = x int* y
    242        t2 = t1 int+ 2
    243        a = t2
    244        if flag int!= 0 goto L38
    245        goto L39
    246  L38:  t3 = x int* y
    247        t4 = t3 int+ 2
    248        b = t4
    249        goto L40
    250  L39:  t5 = x int+ 1
    251        x = t5
    252        t6 = x int* y
    253        t7 = t6 int+ 2
    254        b = t7
    255  L40:  t8 = a int* 1000
    256        t9 = t8 int+ b
    257        t10 = x int* y
    258        t11 = t9 int+ t10
    259        return t11

============================================================================
 FUNCTION memory(int)        (link name _Z6memoryi)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 16 temporaries, frame 104 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   i                param   int                             4       0
   arr              local   int[4]                         16       4
   p                local   int *                           4      20
   q                local   int *                           4      24
   a                local   int                             4      28
   b                local   int                             4      32
   c                local   int                             4      36
   t1               temp    int *                           4      40
   t2               temp    int *                           4      44
   t3               temp    int *                           4      48
   t4               temp    int                             4      52
   t5               temp    int                             4      56
   t6               temp    int                             4      60
   t7               temp    int                             4      64
   t8               temp    int                             4      68
   t9               temp    int                             4      72
   t10              temp    int *                           4      76
   t11              temp    int                             4      80
   t12              temp    int                             4      84
   t13              temp    int                             4      88
   t14              temp    int                             4      92
   t15              temp    int                             4      96
   t16              temp    int                             4     100

 Code: 29 instruction(s)

    260     arr[0] = 1
    261     arr[4] = 2
    262     arr[8] = 3
    263     arr[12] = 4
    264     t1 = &arr
    265     t2 = t1 ptr+ 4
    266     p = t2
    267     t3 = &arr
    268     q = t3
    269     t4 = i int* 4                       (w = 4)
    270     arr[t4] = 10
    271     t5 = i int* 4                       (w = 4)
    272     t6 = arr[t5]
    273     a = t6
    274     *p = 20
    275     t7 = i int* 4                       (w = 4)
    276     t8 = arr[t7]
    277     b = t8
    278     t9 = i int* 4
    279     t10 = q ptr+ t9
    280     *t10 = 30
    281     t11 = i int* 4                      (w = 4)
    282     t12 = arr[t11]
    283     t13 = *p
    284     t14 = t12 int+ t13
    285     c = t14
    286     t15 = a int+ b
    287     t16 = t15 int+ c
    288     return t16

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 30 temporaries, frame 148 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   p                local   struct Pair                     8       4
   t                local   int                             4      12
   c1               local   int                             4      16
   c2               local   int                             4      20
   c3               local   int                             4      24
   t1               temp    int *                           4      28
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int                             4      40
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t7               temp    int                             4      52
   t8               temp    int                             4      56
   t9               temp    int                             4      60
   t10              temp    int                             4      64
   t11              temp    int                             4      68
   t12              temp    int                             4      72
   t13              temp    int                             4      76
   t14              temp    int                             4      80
   t15              temp    int                             4      84
   t16              temp    int                             4      88
   t17              temp    int                             4      92
   t18              temp    int                             4      96
   t19              temp    int                             4     100
   t20              temp    int                             4     104
   t21              temp    int                             4     108
   t22              temp    int                             4     112
   t23              temp    int                             4     116
   t24              temp    int                             4     120
   t25              temp    int                             4     124
   t26              temp    int                             4     128
   t27              temp    int                             4     132
   t28              temp    int                             4     136
   t29              temp    int                             4     140
   t30              temp    int                             4     144

 Code: 124 instruction(s)

    289     x = 5
    290     t1 = &x
    291     param 3
    292     t2 = call square(int), 1
    293     param t1
    294     param t2
    295     call bump(int &, int), 2
    296     p[0] = 1
    297     p[4] = 2
    298     param p
    299     t3 = call total(struct Pair), 1
    300     param p
    301     t4 = call total(struct Pair), 1
    302     t5 = t3 int+ t4
    303     t = t5
    304     t6 = p[0]
    305     t7 = int- 5
    306     param t7
    307     param 0
    308     param 9
    309     t8 = call clamp(int, int, int), 3
    310     param 50
    311     param 0
    312     param 9
    313     t9 = call clamp(int, int, int), 3
    314     param 4
    315     param 0
    316     param 9
    317     t10 = call clamp(int, int, int), 3
    318     t11 = t9 int+ t10
    319     param "%d %d %d %d %d\n"
    320     param x
    321     param t
    322     param t6
    323     param t8
    324     param t11
    325     call printf, 6
    326     param 1
    327     t12 = call counted(int), 1
    328     c1 = t12
    329     param 1
    330     t13 = call counted(int), 1
    331     c2 = t13
    332     param 1
    333     t14 = call counted(int), 1
    334     c3 = t14
    335     param 6
    336     t15 = call fact(int), 1
    337     param "%d %d %d %d %d\n"
    338     param c1
    339     param c2
    340     param c3
    341     param calls
    342     param t15
    343     call printf, 6
    344     param 1071
    345     param 462
    346     t16 = call gcd(int, int), 2
    347     param 17
    348     param 5
    349     t17 = call gcd(int, int), 2
    350     param 100
    351     param 0
    352     t18 = call sumTo(int, int), 2
    353     param 9
    354     t19 = call countDown(int), 1
    355     param "%d %d %d %d\n"
    356     param t16
    357     param t17
    358     param t18
    359     param t19
    360     call printf, 5
    361     param 5
    362     param 2
    363     t20 = call invariant(int, int), 2
    364     param 0
    365     param 9
    366     t21 = call invariant(int, int), 2
    367     param 5
    368     t22 = call notInvariant(int), 1
    369     param 0
    370     param 0
    371     t23 = call zeroTrips(int, int), 2
    372     param "%d %d %d %d\n"
    373     param t20
    374     param t21
    375     param t22
    376     param t23
    377     call printf, 5
    378     param 3
    379     param 4
    380     t24 = call zeroTrips(int, int), 2
    381     param 4
    382     param 5
    383     t25 = call nested(int, int), 2
    384     param 2
    385     param 3
    386     t26 = call nested(int, int), 2
    387     param "%d %d %d\n"
    388     param t24
    389     param t25
    390     param t26
    391     call printf, 4
    392     param 3
    393     param 4
    394     param 1
    395     t27 = call shared(int, int, int), 3
    396     param 3
    397     param 4
    398     param 0
    399     t28 = call shared(int, int, int), 3
    400     param "%d %d\n"
    401     param t27
    402     param t28
    403     call printf, 3
    404     param 1
    405     t29 = call memory(int), 1
    406     param 2
    407     t30 = call memory(int), 1
    408     param "%d %d\n"
    409     param t29
    410     param t30
    411     call printf, 3
    412     return calls


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      6    4    4  
   square             function      int (int)                  -           7    -    1  _Z6squarei; defined
   clamp              function      int (int, int, int)        -           8    -    3  _Z5clampiii; defined
   counted            function      int (int)                  -           9    -    3  _Z7countedi; defined
   bump               function      void (int &, int)          -          10    -    1  _Z4bumpRii; defined
   Pair               struct_tag    struct Pair                -          11    -    0  size 8
   total              function      int (struct Pair)          -          12    -    2  _Z5total4Pair; defined
   fact               function      int (int)                  -          13    -    2  _Z4facti; defined
   gcd                function      int (int, int)             -          15    -    3  _Z3gcdii; defined
   sumTo              function      int (int, int)             -          16    -    2  _Z5sumToii; defined
   countDown          function      int (int)                  -          17    -    2  _Z9countDowni; defined
   invariant          function      int (int, int)             -          19    -    2  _Z9invariantii; defined
   notInvariant       function      int (int)                  -          30    -    1  _Z12notInvarianti; defined
   zeroTrips          function      int (int, int)             -          40    -    2  _Z9zeroTripsii; defined
   nested             function      int (int, int)             -          46    -    2  _Z6nestedii; defined
   shared             function      int (int, int, int)        -          55    -    2  _Z6sharediii; defined
   memory             function      int (int)                  -          62    -    2  _Z6memoryi; defined
   main               function      int (void)                 -          74    -    0  defined

 scope: global > square()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       7    4    2  v.1

 scope: global > clamp()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       8    4    3  v.2
   lo                 parameter     int                        param       8    4    2  lo.3
   hi                 parameter     int                        param       8    4    2  hi.4

 scope: global > counted()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       9    4    1  v.5

 scope: global > bump()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param      10    4    1  r.6
   by                 parameter     int                        param      10    4    1  by.7

 scope: global > struct Pair
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member     11    4    3  Pair::a; public, offset 0
   b                  field         int                        member     11    4    1  Pair::b; public, offset 4

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Pair                param      12    8    3  p.8

 scope: global > fact()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      13    4    3  n.9

 scope: global > gcd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      15    4    2  a.10
   b                  parameter     int                        param      15    4    3  b.11

 scope: global > sumTo()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      16    4    3  n.12
   acc                parameter     int                        param      16    4    2  acc.13

 scope: global > countDown()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      17    4    2  n.14

 scope: global > invariant()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      19    4    1  n.15
   k                  parameter     int                        param      19    4    2  k.16
   s                  variable      int                        local      20    4    3  s.17

 scope: global > invariant() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      21    4    4  i.18

 scope: global > invariant() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   scale              variable      int                        local      22    4    1  scale.19

 scope: global > notInvariant()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      30    4    1  n.20
   s                  variable      int                        local      31    4    2  s.21
   k                  variable      int                        local      31    4    3  k.22

 scope: global > notInvariant() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      32    4    3  i.23

 scope: global > notInvariant() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  variable      int                        local      33    4    1  v.24

 scope: global > zeroTrips()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      40    4    2  n.25
   d                  parameter     int                        param      40    4    1  d.26
   s                  variable      int                        local      41    4    2  s.27

 scope: global > nested()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   rows               parameter     int                        param      46    4    2  rows.28
   cols               parameter     int                        param      46    4    3  cols.29
   grid               variable      int[4][5]                  local      47   80    2  grid.30
   s                  variable      int                        local      47    4    2  s.31

 scope: global > nested() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      int                        local      48    4    4  r.32
   r                  variable      int                        local      50    4    3  r.34

 scope: global > nested() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        local      49    4    4  c.33
   c                  variable      int                        local      51    4    3  c.35

 scope: global > shared()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      55    4    6  x.36
   y                  parameter     int                        param      55    4    4  y.37
   flag               parameter     int                        param      55    4    1  flag.38
   a                  variable      int                        local      56    4    1  a.39
   b                  variable      int                        local      56    4    3  b.40

 scope: global > memory()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      62    4    5  i.41
   arr                variable      int[4]                     local      63   16    6  arr.42
   p                  variable      int *                      local      64    4    2  p.43
   q                  variable      int *                      local      64    4    1  q.44
   a                  variable      int                        local      66    4    1  a.45
   b                  variable      int                        local      68    4    1  b.46
   c                  variable      int                        local      70    4    1  c.47

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      75    4    2  x.48
   p                  variable      struct Pair                local      77    8    3  p.49
   t                  variable      int                        local      78    4    1  t.50
   c1                 variable      int                        local      80    4    1  c1.51
   c2                 variable      int                        local      80    4    1  c2.52
   c3                 variable      int                        local      80    4    1  c3.53

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Pair: size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
