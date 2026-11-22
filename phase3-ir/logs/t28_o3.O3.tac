============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t28_o3.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 313 -> 255 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          313 -> 255   (18% fewer)

   constants folded                       29
   algebraic simplifications               7
   common subexpressions                  10
   copies / constants forwarded          108
   temporaries merged away                19
   dead instructions removed              72
   jumps removed or redirected            27
   unreachable instructions removed       21
   propagated across blocks               16
   dead assignments removed               27
   calls inlined                          21
   tail calls turned into jumps            3
   common subexpressions across blocks      3
   loops unrolled                         14
   unreachable functions removed          12

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

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

    100       if n int> 1 goto L1
    101       t1 = 1
    102       goto L2
    103  L1:  t2 = n int- 1
    104       param t2
    105       t3 = call fact(int), 1
    106       t1 = n int* t3
    107  L2:  return t1

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

 Code: 44 instruction(s)

    108        s = 0
    109        r.32 = 0
    110  L3:   if r.32 int>= rows goto L6
    111        c.33 = 0
    112  L4:   if c.33 int>= cols goto L5
    113        t1 = r.32 int* 5                    (n2 = 5)
    114        t2 = t1 int+ c.33
    115        t3 = t2 int<< 2                     (w = 4)
    116        t4 = r.32 int* cols
    117        t5 = t4 int+ c.33
    118        grid[t3] = t5
    119        c.33 = c.33 int+ 1
    120        if c.33 int>= cols goto L5
    121        t1 = r.32 int* 5                    (n2 = 5)
    122        t2 = t1 int+ c.33
    123        t3 = t2 int<< 2                     (w = 4)
    124        t4 = r.32 int* cols
    125        t5 = t4 int+ c.33
    126        grid[t3] = t5
    127        c.33 = c.33 int+ 1
    128        goto L4
    129  L5:   r.32 = r.32 int+ 1
    130        goto L3
    131  L6:   r.34 = 0
    132  L7:   if r.34 int>= rows goto L10
    133        c.35 = 0
    134  L8:   if c.35 int>= cols goto L9
    135        t8 = r.34 int* 5                    (n2 = 5)
    136        t9 = t8 int+ c.35
    137        t10 = t9 int<< 2                    (w = 4)
    138        t11 = grid[t10]
    139        s = s int+ t11
    140        c.35 = c.35 int+ 1
    141        if c.35 int>= cols goto L9
    142        t8 = r.34 int* 5                    (n2 = 5)
    143        t9 = t8 int+ c.35
    144        t10 = t9 int<< 2                    (w = 4)
    145        t11 = grid[t10]
    146        s = s int+ t11
    147        c.35 = c.35 int+ 1
    148        goto L8
    149  L9:   r.34 = r.34 int+ 1
    150        goto L7
    151  L10:  return s

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

    152     arr[0] = 1
    153     arr[4] = 2
    154     arr[8] = 3
    155     arr[12] = 4
    156     t1 = &arr
    157     t2 = t1 ptr+ 4
    158     t4 = i int<< 2                      (w = 4)
    159     arr[t4] = 10
    160     *t2 = 20
    161     t8 = arr[t4]
    162     t10 = t1 ptr+ t4
    163     *t10 = 30
    164     t12 = arr[t4]
    165     t13 = *t2
    166     t14 = t12 int+ t13
    167     t15 = 10 int+ t8
    168     t16 = t15 int+ t14
    169     return t16

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 50 temporaries, frame 540 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   p                local   struct Pair                     8       4
   t                local   int                             4      12
   c1               local   int                             4      16
   c2               local   int                             4      20
   c3               local   int                             4      24
   t1               temp    int *                           4      28
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t15              temp    int                             4      84
   t25              temp    int                             4     124
   t26              temp    int                             4     128
   t29              temp    int                             4     140
   t30              temp    int                             4     144
   t35              temp    int                             4     164
   t36              temp    int                             4     168
   t37              temp    struct Pair                     8     172
   t38              temp    int                             4     180
   t39              temp    int                             4     184
   t40              temp    int                             4     188
   t41              temp    int                             4     192
   t42              temp    struct Pair                     8     196
   t43              temp    int                             4     204
   t44              temp    int                             4     208
   t45              temp    int                             4     212
   t46              temp    int                             4     216
   t57              temp    int                             4     260
   t58              temp    int                             4     264
   t61              temp    int                             4     276
   t64              temp    int                             4     288
   t65              temp    int                             4     292
   t66              temp    int                             4     296
   t67              temp    int                             4     300
   t68              temp    int                             4     304
   t69              temp    int                             4     308
   t70              temp    int                             4     312
   t71              temp    int                             4     316
   t72              temp    int                             4     320
   t73              temp    int                             4     324
   t74              temp    int                             4     328
   t75              temp    int                             4     332
   t78              temp    int                             4     344
   t79              temp    int                             4     348
   t82              temp    int                             4     360
   t85              temp    int                             4     372
   t86              temp    int                             4     376
   t89              temp    int                             4     388
   t91              temp    int                             4     396
   t92              temp    int                             4     400
   t93              temp    int                             4     404
   t94              temp    int                             4     408
   t95              temp    int                             4     412
   t97              temp    int                             4     420
   t98              temp    int                             4     424
   t99              temp    int                             4     428
   t101             temp    int                             4     436
   (76 temporaries no longer used after optimization not shown)

 Code: 185 instruction(s)

    170        x = 5
    171        t1 = &x
    172        t35 = *t1
    173        t36 = t35 int+ 9
    174        *t1 = t36
    175        p[0] = 1
    176        p[4] = 2
    177        t37 = p
    178        t38 = t37[0]
    179        t39 = t38 int+ 1
    180        t37[0] = t39
    181        t40 = t37[4]
    182        t41 = t39 int+ t40
    183        t42 = p
    184        t43 = t42[0]
    185        t44 = t43 int+ 1
    186        t42[0] = t44
    187        t45 = t42[4]
    188        t46 = t44 int+ t45
    189        t5 = t41 int+ t46
    190        t6 = p[0]
    191        param "%d %d %d %d %d\n"
    192        param x
    193        param t5
    194        param t6
    195        param 0
    196        param 13
    197        call printf, 6
    198        t57 = calls int+ 1
    199        calls = t57
    200        t58 = 1 int+ t57
    201        calls = t58
    202        t61 = 1 int+ t58
    203        calls = t61
    204        t64 = 1 int+ t61
    205        param 6
    206        t15 = call fact(int), 1
    207        param "%d %d %d %d %d\n"
    208        param t58
    209        param t61
    210        param t64
    211        param calls
    212        param t15
    213        call printf, 6
    214        t65 = 1071
    215        t66 = 462
    216  L11:  if t66 int== 0 goto L12
    217        t67 = t65 int% t66
    218        t65 = t66
    219        t66 = t67
    220        if t67 int== 0 goto L12
    221        t67 = t65 int% t66
    222        t65 = t66
    223        t66 = t67
    224        goto L11
    225  L12:  t68 = 17
    226        t69 = 5
    227  L13:  if t69 int== 0 goto L14
    228        t70 = t68 int% t69
    229        t68 = t69
    230        t69 = t70
    231        if t70 int== 0 goto L14
    232        t70 = t68 int% t69
    233        t68 = t69
    234        t69 = t70
    235        goto L13
    236  L14:  t71 = 100
    237        t72 = 0
    238  L15:  if t71 int== 0 goto L16
    239        t73 = t71 int- 1
    240        t74 = t72 int+ t71
    241        t71 = t73
    242        t72 = t74
    243        if t73 int== 0 goto L16
    244        t73 = t71 int- 1
    245        t74 = t72 int+ t71
    246        t71 = t73
    247        t72 = t74
    248        goto L15
    249  L16:  t75 = 9
    250  L17:  if t75 int<= 0 goto L18
    251        t75 = t75 int- 2
    252        if t75 int<= 0 goto L18
    253        t75 = t75 int- 2
    254        goto L17
    255  L18:  param "%d %d %d %d\n"
    256        param t65
    257        param t68
    258        param t72
    259        param 0
    260        call printf, 5
    261        t78 = 0
    262        t79 = 0
    263  L19:  if t79 int>= 5 goto L22
    264        t82 = t79 int* 7
    265        t78 = t78 int+ t82
    266        if t79 int== 2 goto L20
    267        t78 = t78 int+ 6
    268  L20:  t79 = t79 int+ 1
    269        if t79 int>= 5 goto L22
    270        t82 = t79 int* 7
    271        t78 = t78 int+ t82
    272        if t79 int== 2 goto L21
    273        t78 = t78 int+ 6
    274  L21:  t79 = t79 int+ 1
    275        goto L19
    276  L22:  t85 = 0
    277        t86 = 0
    278  L23:  if t86 int>= 0 goto L26
    279        t89 = t86 int* 28
    280        t85 = t85 int+ t89
    281        if t86 int== 2 goto L24
    282        t85 = t85 int+ 27
    283  L24:  t86 = t86 int+ 1
    284        if t86 int>= 0 goto L26
    285        t89 = t86 int* 28
    286        t85 = t85 int+ t89
    287        if t86 int== 2 goto L25
    288        t85 = t85 int+ 27
    289  L25:  t86 = t86 int+ 1
    290        goto L23
    291  L26:  t91 = 0
    292        t92 = 1
    293        t93 = 0
    294  L27:  if t93 int>= 5 goto L28
    295        t94 = t92 int* 3
    296        t91 = t91 int+ t94
    297        t92 = t92 int+ t93
    298        t93 = t93 int+ 1
    299        if t93 int>= 5 goto L28
    300        t94 = t92 int* 3
    301        t91 = t91 int+ t94
    302        t92 = t92 int+ t93
    303        t93 = t93 int+ 1
    304        goto L27
    305  L28:  t95 = 0
    306        t97 = 7
    307  L29:  if t95 int<= 0 goto L30
    308        t98 = 100 int/ 0
    309        t97 = t97 int+ t98
    310        t95 = t95 int- 1
    311        if t95 int<= 0 goto L30
    312        t98 = 100 int/ 0
    313        t97 = t97 int+ t98
    314        t95 = t95 int- 1
    315        goto L29
    316  L30:  param "%d %d %d %d\n"
    317        param t78
    318        param t85
    319        param t91
    320        param t97
    321        call printf, 5
    322        t99 = 3
    323        t101 = 7
    324  L31:  if t99 int<= 0 goto L32
    325        t101 = t101 int+ 25
    326        t99 = t99 int- 1
    327        if t99 int<= 0 goto L32
    328        t101 = t101 int+ 25
    329        t99 = t99 int- 1
    330        goto L31
    331  L32:  param 4
    332        param 5
    333        t25 = call nested(int, int), 2
    334        param 2
    335        param 3
    336        t26 = call nested(int, int), 2
    337        param "%d %d %d\n"
    338        param t101
    339        param t25
    340        param t26
    341        call printf, 4
    342        param "%d %d\n"
    343        param 14026
    344        param 14034
    345        call printf, 3
    346        param 1
    347        t29 = call memory(int), 1
    348        param 2
    349        t30 = call memory(int), 1
    350        param "%d %d\n"
    351        param t29
    352        param t30
    353        call printf, 3
    354        return calls


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      5    4    4  
   square             function      int (int)                  -           6    -    1  _Z6squarei; defined
   clamp              function      int (int, int, int)        -           7    -    3  _Z5clampiii; defined
   counted            function      int (int)                  -           8    -    3  _Z7countedi; defined
   bump               function      void (int &, int)          -           9    -    1  _Z4bumpRii; defined
   Pair               struct_tag    struct Pair                -          10    -    0  size 8
   total              function      int (struct Pair)          -          11    -    2  _Z5total4Pair; defined
   fact               function      int (int)                  -          12    -    2  _Z4facti; defined
   gcd                function      int (int, int)             -          14    -    3  _Z3gcdii; defined
   sumTo              function      int (int, int)             -          15    -    2  _Z5sumToii; defined
   countDown          function      int (int)                  -          16    -    2  _Z9countDowni; defined
   invariant          function      int (int, int)             -          18    -    2  _Z9invariantii; defined
   notInvariant       function      int (int)                  -          29    -    1  _Z12notInvarianti; defined
   zeroTrips          function      int (int, int)             -          39    -    2  _Z9zeroTripsii; defined
   nested             function      int (int, int)             -          45    -    2  _Z6nestedii; defined
   shared             function      int (int, int, int)        -          54    -    2  _Z6sharediii; defined
   memory             function      int (int)                  -          61    -    2  _Z6memoryi; defined
   main               function      int (void)                 -          73    -    0  defined

 scope: global > square()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       6    4    2  v.1

 scope: global > clamp()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       7    4    3  v.2
   lo                 parameter     int                        param       7    4    2  lo.3
   hi                 parameter     int                        param       7    4    2  hi.4

 scope: global > counted()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       8    4    1  v.5

 scope: global > bump()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param       9    4    1  r.6
   by                 parameter     int                        param       9    4    1  by.7

 scope: global > struct Pair
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member     10    4    3  Pair::a; public, offset 0
   b                  field         int                        member     10    4    1  Pair::b; public, offset 4

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Pair                param      11    8    3  p.8

 scope: global > fact()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      12    4    3  n.9

 scope: global > gcd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      14    4    2  a.10
   b                  parameter     int                        param      14    4    3  b.11

 scope: global > sumTo()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      15    4    3  n.12
   acc                parameter     int                        param      15    4    2  acc.13

 scope: global > countDown()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      16    4    2  n.14

 scope: global > invariant()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      18    4    1  n.15
   k                  parameter     int                        param      18    4    2  k.16
   s                  variable      int                        local      19    4    3  s.17

 scope: global > invariant() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      20    4    4  i.18

 scope: global > invariant() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   scale              variable      int                        local      21    4    1  scale.19

 scope: global > notInvariant()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      29    4    1  n.20
   s                  variable      int                        local      30    4    2  s.21
   k                  variable      int                        local      30    4    3  k.22

 scope: global > notInvariant() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      31    4    3  i.23

 scope: global > notInvariant() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  variable      int                        local      32    4    1  v.24

 scope: global > zeroTrips()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      39    4    2  n.25
   d                  parameter     int                        param      39    4    1  d.26
   s                  variable      int                        local      40    4    2  s.27

 scope: global > nested()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   rows               parameter     int                        param      45    4    2  rows.28
   cols               parameter     int                        param      45    4    3  cols.29
   grid               variable      int[4][5]                  local      46   80    2  grid.30
   s                  variable      int                        local      46    4    2  s.31

 scope: global > nested() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      int                        local      47    4    4  r.32
   r                  variable      int                        local      49    4    3  r.34

 scope: global > nested() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        local      48    4    4  c.33
   c                  variable      int                        local      50    4    3  c.35

 scope: global > shared()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      54    4    6  x.36
   y                  parameter     int                        param      54    4    4  y.37
   flag               parameter     int                        param      54    4    1  flag.38
   a                  variable      int                        local      55    4    1  a.39
   b                  variable      int                        local      55    4    3  b.40

 scope: global > memory()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      61    4    5  i.41
   arr                variable      int[4]                     local      62   16    6  arr.42
   p                  variable      int *                      local      63    4    2  p.43
   q                  variable      int *                      local      63    4    1  q.44
   a                  variable      int                        local      65    4    1  a.45
   b                  variable      int                        local      67    4    1  b.46
   c                  variable      int                        local      69    4    1  c.47

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      74    4    2  x.48
   p                  variable      struct Pair                local      76    8    3  p.49
   t                  variable      int                        local      77    4    1  t.50
   c1                 variable      int                        local      79    4    1  c1.51
   c2                 variable      int                        local      79    4    1  c2.52
   c3                 variable      int                        local      79    4    1  c3.53

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Pair: size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
