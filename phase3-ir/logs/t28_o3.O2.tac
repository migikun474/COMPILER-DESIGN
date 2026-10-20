============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t28_o3.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 313 -> 261 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          313 -> 261   (16% fewer)

   constants folded                        1
   algebraic simplifications               7
   common subexpressions                   7
   copies / constants forwarded           22
   temporaries merged away                17
   dead instructions removed               8
   jumps removed or redirected            16
   unreachable instructions removed        1
   propagated across blocks                0
   dead assignments removed               11

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

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

 Code: 5 instruction(s)

    102       if v int>= lo goto L1
    103       return lo
    104  L1:  if v int<= hi goto L2
    105       return hi
    106  L2:  return v

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

    107     t1 = calls int+ 1
    108     calls = t1
    109     t2 = v int+ t1
    110     return t2

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

    111     t1 = *r
    112     t2 = t1 int+ by
    113     *r = t2
    114     return

============================================================================
 FUNCTION total(struct Pair)        (link name _Z5total4Pair)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Pair                     8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 6 instruction(s)

    115     t1 = p[0]
    116     t2 = t1 int+ 1
    117     p[0] = t2
    118     t4 = p[4]
    119     t5 = t2 int+ t4
    120     return t5

============================================================================
 FUNCTION fact(int)        (link name _Z4facti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    121       if n int> 1 goto L3
    122       t1 = 1
    123       goto L4
    124  L3:  t2 = n int- 1
    125       param t2
    126       t3 = call fact(int), 1
    127       t1 = n int* t3
    128  L4:  return t1

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

 Code: 7 instruction(s)

    129       if b int!= 0 goto L5
    130       return a
    131  L5:  t1 = a int% b
    132       param b
    133       param t1
    134       t2 = call gcd(int, int), 2
    135       return t2

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

 Code: 8 instruction(s)

    136       if n int!= 0 goto L6
    137       return acc
    138  L6:  t1 = n int- 1
    139       t2 = acc int+ n
    140       param t1
    141       param t2
    142       t3 = call sumTo(int, int), 2
    143       return t3

============================================================================
 FUNCTION countDown(int)        (link name _Z9countDowni)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 6 instruction(s)

    144       if n int> 0 goto L7
    145       return 0
    146  L7:  t1 = n int- 2
    147       param t1
    148       t2 = call countDown(int), 1
    149       return t2

============================================================================
 FUNCTION invariant(int, int)        (link name _Z9invariantii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 4 temporaries, frame 48 bytes

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
   t5               temp    int                             4      36
   (3 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    150        s = 0
    151        i = 0
    152  L8:   if i int>= n goto L10
    153        t1 = k int* 3
    154        t2 = t1 int+ 1
    155        t3 = i int* t2
    156        s = s int+ t3
    157        if i int== 2 goto L9
    158        t5 = k int* 3
    159        s = s int+ t5
    160  L9:   i = i int+ 1
    161        goto L8
    162  L10:  return s

============================================================================
 FUNCTION notInvariant(int)        (link name _Z12notInvarianti)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 1 temporary, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   s                local   int                             4       4
   k                local   int                             4       8
   i                local   int                             4      12
   v                local   int                             4      16
   t1               temp    int                             4      20
   (3 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    163        s = 0
    164        k = 1
    165        i = 0
    166  L11:  if i int>= n goto L12
    167        t1 = k int* 3
    168        s = s int+ t1
    169        k = k int+ i
    170        i = i int+ 1
    171        goto L11
    172  L12:  return s

============================================================================
 FUNCTION zeroTrips(int, int)        (link name _Z9zeroTripsii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   d                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    173        s = 7
    174  L13:  if n int<= 0 goto L14
    175        t1 = 100 int/ d
    176        s = s int+ t1
    177        n = n int- 1
    178        goto L13
    179  L14:  return s

============================================================================
 FUNCTION nested(int, int)        (link name _Z6nestedii)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 9 temporaries, frame 164 bytes

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
   t8               temp    int                             4     136
   t9               temp    int                             4     140
   t10              temp    int                             4     144
   t11              temp    int                             4     148
   (5 temporaries no longer used after optimization not shown)

 Code: 29 instruction(s)

    180        s = 0
    181        r.32 = 0
    182  L15:  if r.32 int>= rows goto L18
    183        c.33 = 0
    184  L16:  if c.33 int>= cols goto L17
    185        t1 = r.32 int* 5                    (n2 = 5)
    186        t2 = t1 int+ c.33
    187        t3 = t2 int<< 2                     (w = 4)
    188        t4 = r.32 int* cols
    189        t5 = t4 int+ c.33
    190        grid[t3] = t5
    191        c.33 = c.33 int+ 1
    192        goto L16
    193  L17:  r.32 = r.32 int+ 1
    194        goto L15
    195  L18:  r.34 = 0
    196  L19:  if r.34 int>= rows goto L22
    197        c.35 = 0
    198  L20:  if c.35 int>= cols goto L21
    199        t8 = r.34 int* 5                    (n2 = 5)
    200        t9 = t8 int+ c.35
    201        t10 = t9 int<< 2                    (w = 4)
    202        t11 = grid[t10]
    203        s = s int+ t11
    204        c.35 = c.35 int+ 1
    205        goto L20
    206  L21:  r.34 = r.34 int+ 1
    207        goto L19
    208  L22:  return s

============================================================================
 FUNCTION shared(int, int, int)        (link name _Z6sharediii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 8 temporaries, frame 64 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   y                param   int                             4       4
   flag             param   int                             4       8
   a                local   int                             4      12
   b                local   int                             4      16
   t1               temp    int                             4      20
   t3               temp    int                             4      28
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t8               temp    int                             4      48
   t9               temp    int                             4      52
   t10              temp    int                             4      56
   t11              temp    int                             4      60
   (3 temporaries no longer used after optimization not shown)

 Code: 15 instruction(s)

    209        t1 = x int* y
    210        a = t1 int+ 2
    211        if flag int== 0 goto L23
    212        t3 = x int* y
    213        b = t3 int+ 2
    214        goto L24
    215  L23:  t5 = x int+ 1
    216        x = t5
    217        t6 = t5 int* y
    218        b = t6 int+ 2
    219  L24:  t8 = a int* 1000
    220        t9 = t8 int+ b
    221        t10 = x int* y
    222        t11 = t9 int+ t10
    223        return t11

============================================================================
 FUNCTION memory(int)        (link name _Z6memoryi)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 10 temporaries, frame 104 bytes

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
   t4               temp    int                             4      52
   t8               temp    int                             4      68
   t10              temp    int *                           4      76
   t12              temp    int                             4      84
   t13              temp    int                             4      88
   t14              temp    int                             4      92
   t15              temp    int                             4      96
   t16              temp    int                             4     100
   (6 temporaries no longer used after optimization not shown)

 Code: 18 instruction(s)

    224     arr[0] = 1
    225     arr[4] = 2
    226     arr[8] = 3
    227     arr[12] = 4
    228     t1 = &arr
    229     t2 = t1 ptr+ 4
    230     t4 = i int<< 2                      (w = 4)
    231     arr[t4] = 10
    232     *t2 = 20
    233     t8 = arr[t4]
    234     t10 = t1 ptr+ t4
    235     *t10 = 30
    236     t12 = arr[t4]
    237     t13 = *t2
    238     t14 = t12 int+ t13
    239     t15 = 10 int+ t8
    240     t16 = t15 int+ t14
    241     return t16

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 29 temporaries, frame 148 bytes

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
   (1 temporary no longer used after optimization not shown)

 Code: 119 instruction(s)

    242     x = 5
    243     t1 = &x
    244     param 3
    245     t2 = call square(int), 1
    246     param t1
    247     param t2
    248     call bump(int &, int), 2
    249     p[0] = 1
    250     p[4] = 2
    251     param p
    252     t3 = call total(struct Pair), 1
    253     param p
    254     t4 = call total(struct Pair), 1
    255     t5 = t3 int+ t4
    256     t6 = p[0]
    257     param -5
    258     param 0
    259     param 9
    260     t8 = call clamp(int, int, int), 3
    261     param 50
    262     param 0
    263     param 9
    264     t9 = call clamp(int, int, int), 3
    265     param 4
    266     param 0
    267     param 9
    268     t10 = call clamp(int, int, int), 3
    269     t11 = t9 int+ t10
    270     param "%d %d %d %d %d\n"
    271     param x
    272     param t5
    273     param t6
    274     param t8
    275     param t11
    276     call printf, 6
    277     param 1
    278     t12 = call counted(int), 1
    279     param 1
    280     t13 = call counted(int), 1
    281     param 1
    282     t14 = call counted(int), 1
    283     param 6
    284     t15 = call fact(int), 1
    285     param "%d %d %d %d %d\n"
    286     param t12
    287     param t13
    288     param t14
    289     param calls
    290     param t15
    291     call printf, 6
    292     param 1071
    293     param 462
    294     t16 = call gcd(int, int), 2
    295     param 17
    296     param 5
    297     t17 = call gcd(int, int), 2
    298     param 100
    299     param 0
    300     t18 = call sumTo(int, int), 2
    301     param 9
    302     t19 = call countDown(int), 1
    303     param "%d %d %d %d\n"
    304     param t16
    305     param t17
    306     param t18
    307     param t19
    308     call printf, 5
    309     param 5
    310     param 2
    311     t20 = call invariant(int, int), 2
    312     param 0
    313     param 9
    314     t21 = call invariant(int, int), 2
    315     param 5
    316     t22 = call notInvariant(int), 1
    317     param 0
    318     param 0
    319     t23 = call zeroTrips(int, int), 2
    320     param "%d %d %d %d\n"
    321     param t20
    322     param t21
    323     param t22
    324     param t23
    325     call printf, 5
    326     param 3
    327     param 4
    328     t24 = call zeroTrips(int, int), 2
    329     param 4
    330     param 5
    331     t25 = call nested(int, int), 2
    332     param 2
    333     param 3
    334     t26 = call nested(int, int), 2
    335     param "%d %d %d\n"
    336     param t24
    337     param t25
    338     param t26
    339     call printf, 4
    340     param 3
    341     param 4
    342     param 1
    343     t27 = call shared(int, int, int), 3
    344     param 3
    345     param 4
    346     param 0
    347     t28 = call shared(int, int, int), 3
    348     param "%d %d\n"
    349     param t27
    350     param t28
    351     call printf, 3
    352     param 1
    353     t29 = call memory(int), 1
    354     param 2
    355     t30 = call memory(int), 1
    356     param "%d %d\n"
    357     param t29
    358     param t30
    359     call printf, 3
    360     return calls


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
