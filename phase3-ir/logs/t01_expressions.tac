============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t01_expressions.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 193 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 22 parameter(s)/local(s), 72 temporaries, frame 432 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   x                local   int                             4      12
   d                local   double                          8      16
   f                local   float                           4      24
   back             local   int                             4      28
   u                local   unsigned int                    4      32
   v                local   int                             4      36
   bits             local   int                             4      40
   t                local   int                             4      44
   i                local   int                             4      48
   j                local   int                             4      52
   k                local   int                             4      56
   m                local   int                             4      60
   ch               local   char                            1      64
   uch              local   unsigned char                   1      65
   sh               local   short                           2      66
   z                local   int                             4      68
   w                local   int                             4      72
   q                local   int                             4      76
   dd               local   double                          8      80
   t1               temp    int                             4      88
   t2               temp    int                             4      92
   t3               temp    int                             4      96
   t4               temp    int                             4     100
   t5               temp    int                             4     104
   t6               temp    int                             4     108
   t7               temp    int                             4     112
   t8               temp    int                             4     116
   t9               temp    int                             4     120
   t10              temp    int                             4     124
   t11              temp    int                             4     128
   t12              temp    double                          8     136
   t13              temp    int                             4     144
   t14              temp    float                           4     148
   t15              temp    double                          8     152
   t16              temp    double                          8     160
   t17              temp    int                             4     168
   t18              temp    double                          8     176
   t19              temp    double                          8     184
   t20              temp    double                          8     192
   t21              temp    float                           4     200
   t22              temp    float                           4     204
   t23              temp    double                          8     208
   t24              temp    unsigned int                    4     216
   t25              temp    unsigned int                    4     220
   t26              temp    unsigned int                    4     224
   t27              temp    unsigned int                    4     228
   t28              temp    int                             4     232
   t29              temp    int                             4     236
   t30              temp    int                             4     240
   t31              temp    int                             4     244
   t32              temp    int                             4     248
   t33              temp    int                             4     252
   t34              temp    int                             4     256
   t35              temp    int                             4     260
   t36              temp    int                             4     264
   t37              temp    int                             4     268
   t38              temp    int                             4     272
   t39              temp    int                             4     276
   t40              temp    int                             4     280
   t41              temp    int                             4     284
   t42              temp    int                             4     288
   t43              temp    int                             4     292
   t44              temp    int                             4     296
   t45              temp    int                             4     300
   t46              temp    int                             4     304
   t47              temp    int                             4     308
   t48              temp    int                             4     312
   t49              temp    int                             4     316
   t50              temp    int                             4     320
   t51              temp    int                             4     324
   t52              temp    int                             4     328
   t53              temp    int                             4     332
   t54              temp    int                             4     336
   t55              temp    int                             4     340
   t56              temp    int                             4     344
   t57              temp    int                             4     348
   t58              temp    int                             4     352
   t59              temp    int                             4     356
   t60              temp    int                             4     360
   t61              temp    int                             4     364
   t62              temp    int                             4     368
   t63              temp    char                            1     372
   t64              temp    int                             4     376
   t65              temp    int                             4     380
   t66              temp    int                             4     384
   t67              temp    int                             4     388
   t68              temp    unsigned int                    4     392
   t69              temp    double                          8     400
   t70              temp    double                          8     408
   t71              temp    double                          8     416
   t72              temp    double                          8     424

 Code: 193 instruction(s)

    100        a = 7
    101        b = 2
    102        c = 3
    103        t1 = int- c
    104        t2 = b int* t1
    105        t3 = int- c
    106        t4 = b int* t3
    107        t5 = t2 int+ t4
    108        x = t5
    109        t6 = b int* c
    110        t7 = a int+ t6
    111        t8 = a int+ b
    112        t9 = t8 int* c
    113        t10 = a int/ b
    114        t11 = a int% b
    115        param "%d %d %d %d %d\n"
    116        param x
    117        param t7
    118        param t9
    119        param t10
    120        param t11
    121        call printf, 6
    122        t12 = inttodouble a
    123        d = t12
    124        t13 = a int/ 2
    125        t14 = inttofloat t13
    126        f = t14
    127        t15 = d double/ 2.0
    128        t16 = t15 double+ 0.75
    129        t17 = doubletoint t16
    130        back = t17
    131        t18 = inttodouble b
    132        t19 = d double/ t18
    133        t20 = floattodouble f
    134        t21 = inttofloat a
    135        t22 = t21 float/ 3.0
    136        t23 = floattodouble t22
    137        param "%.2f %.1f %d %.3f\n"
    138        param t19
    139        param t20
    140        param back
    141        param t23
    142        call printf, 5
    143        u = 10
    144        t24 = u uint- 11
    145        t25 = u uint* 3
    146        t26 = t25 uint/ 4
    147        t27 = u uint>> 1
    148        param "%u %u %d\n"
    149        param t24
    150        param t26
    151        param t27
    152        call printf, 4
    153        v = 182
    154        bits = 0
    155        t = v
    156  L1:   if t int!= 0 goto L2
    157        goto L3
    158  L2:   t28 = t int& 1
    159        t29 = bits int+ t28
    160        bits = t29
    161        t30 = t int>> 1
    162        t = t30
    163        goto L1
    164  L3:   t32 = v int- 1
    165        t33 = v int& t32
    166        if t33 int== 0 goto L4
    167        t31 = 0
    168        goto L5
    169  L4:   t31 = 1
    170  L5:   t35 = 64 int& 63
    171        if t35 int== 0 goto L6
    172        t34 = 0
    173        goto L7
    174  L6:   t34 = 1
    175  L7:   t36 = v int^ 255
    176        t37 = int~ v
    177        t38 = t37 int& 255
    178        param "%d %d %d %x %x\n"
    179        param bits
    180        param t31
    181        param t34
    182        param t36
    183        param t38
    184        call printf, 6
    185        x = 5
    186        t39 = x int+ 3
    187        x = t39
    188        t40 = x int- 1
    189        x = t40
    190        t41 = x int* 4
    191        x = t41
    192        t42 = x int/ 3
    193        x = t42
    194        t43 = x int% 5
    195        x = t43
    196        t44 = x int<< 3
    197        x = t44
    198        t45 = x int>> 1
    199        x = t45
    200        t46 = x int| 1
    201        x = t46
    202        t47 = x int& 13
    203        x = t47
    204        t48 = x int^ 6
    205        x = t48
    206        param "%d\n"
    207        param x
    208        call printf, 2
    209        i = 5
    210        t49 = i
    211        t50 = i int+ 1
    212        i = t50
    213        t51 = t49 int+ 1
    214        j = t51
    215        t52 = i int- 1
    216        i = t52
    217        t53 = t52 int* 2
    218        k = t53
    219        param "%d %d %d\n"
    220        param i
    221        param j
    222        param k
    223        call printf, 4
    224        i = 3
    225        t54 = i int* 4
    226        m = t54
    227        if i int> 2 goto L8
    228        goto L9
    229  L8:   t55 = 10
    230        goto L10
    231  L9:   t55 = 20
    232  L10:  if a int< b goto L11
    233        goto L12
    234  L11:  t56 = a
    235        goto L16
    236  L12:  if b int< c goto L13
    237        goto L14
    238  L13:  t57 = b
    239        goto L15
    240  L14:  t57 = c
    241  L15:  t56 = t57
    242  L16:  param "%d %d %d\n"
    243        param m
    244        param t55
    245        param t56
    246        call printf, 4
    247        param "%d %d %d\n"
    248        param 4
    249        param 8
    250        param 1
    251        call printf, 4
    252        ch = -126
    253        uch = 44
    254        sh = 1
    255        t58 = chartoint ch
    256        t59 = uchartoint uch
    257        t60 = shorttoint sh
    258        t61 = chartoint ch
    259        t62 = t61 int+ 200
    260        t63 = inttochar t62
    261        t64 = chartoint t63
    262        param "%d %d %d %d\n"
    263        param t58
    264        param t59
    265        param t60
    266        param t64
    267        call printf, 5
    268        t65 = int- 7
    269        t66 = t65 int>> 1
    270        t67 = int- 8
    271        t68 = t67 uint>> 29
    272        param "%d %d\n"
    273        param t66
    274        param t68
    275        call printf, 3
    276        z = 0
    277        w = 5
    278        q = 6
    279        t69 = inttodouble a
    280        t70 = t69 double/ 2.0
    281        t71 = t70 double- 0.25
    282        dd = t71
    283        t72 = dd double- 1.25
    284        param "%d %d %d %d %.2f %d\n"
    285        param z
    286        param w
    287        param q
    288        param 2
    289        param t72
    290        param 0
    291        call printf, 7
    292        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           5    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       6    4   10  a.1
   b                  variable      int                        local       6    4   10  b.2
   c                  variable      int                        local       6    4    6  c.3
   x                  variable      int                        local       6    4   14  x.4
   d                  variable      double                     local       9    8    2  d.5
   f                  variable      float                      local      10    4    1  f.6
   back               variable      int                        local      11    4    1  back.7
   u                  variable      unsigned int               local      13    4    3  u.8
   v                  variable      int                        local      15    4    5  v.9
   bits               variable      int                        local      16    4    2  bits.10
   t                  variable      int                        local      16    4    3  t.11
   i                  variable      int                        local      22    4    6  i.12
   j                  variable      int                        local      22    4    1  j.13
   k                  variable      int                        local      22    4    1  k.14
   m                  variable      int                        local      24    4    1  m.15
   ch                 variable      char                       local      27    1    2  ch.16
   uch                variable      unsigned char              local      28    1    1  uch.17
   sh                 variable      short                      local      29    2    1  sh.18
   z                  variable      int                        local      32    4    1  z.19
   w                  variable      int                        local      32    4    1  w.20
   q                  variable      int                        local      32    4    1  q.21
   dd                 variable      double                     local      33    8    1  dd.22

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
