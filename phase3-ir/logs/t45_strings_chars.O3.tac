============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t45_strings_chars.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 173 -> 239 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          173 -> 239   (-38% fewer)

   constants folded                        2
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded            8
   temporaries merged away                12
   dead instructions removed               8
   jumps removed or redirected             8
   unreachable instructions removed        1
   propagated across blocks                3
   dead assignments removed                2
   calls inlined                           6
   tail calls turned into jumps            0
   common subexpressions across blocks      2
   loops unrolled                         10
   unreachable functions removed           3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 80 temporaries, frame 444 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   buf              local   char[32]                       32       0
   up               local   char[8]                         8      32
   i                local   int                             4      40
   digits           local   const char *                    4      44
   value            local   int                             4      48
   out              local   char[8]                         8      52
   n                local   int                             4      60
   v                local   int                             4      64
   t1               temp    char *                          4      68
   t4               temp    int                             4      80
   t5               temp    char                            1      84
   t6               temp    int                             4      88
   t7               temp    int                             4      92
   t10              temp    int                             4     104
   t11              temp    char                            1     108
   t12              temp    int                             4     112
   t13              temp    int                             4     116
   t15              temp    int                             4     124
   t16              temp    int                             4     128
   t18              temp    char                            1     136
   t19              temp    char                            1     137
   t20              temp    int                             4     140
   t21              temp    int                             4     144
   t22              temp    int                             4     148
   t23              temp    char                            1     152
   t25              temp    char *                          4     160
   t28              temp    const char *                    4     172
   t29              temp    char                            1     176
   t30              temp    int                             4     180
   t32              temp    char                            1     188
   t33              temp    int                             4     192
   t34              temp    int                             4     196
   t37              temp    int                             4     208
   t39              temp    int                             4     216
   t40              temp    int                             4     220
   t41              temp    char                            1     224
   t43              temp    char *                          4     232
   t44              temp    char *                          4     236
   t45              temp    char                            1     240
   t46              temp    int                             4     244
   t47              temp    char *                          4     248
   t48              temp    const char *                    4     252
   t49              temp    char *                          4     256
   t50              temp    const char *                    4     260
   t51              temp    char                            1     264
   t52              temp    const char *                    4     268
   t53              temp    int                             4     272
   t54              temp    const char *                    4     276
   t55              temp    char                            1     280
   t56              temp    const char *                    4     284
   t57              temp    int                             4     288
   t58              temp    const char *                    4     292
   t59              temp    char                            1     296
   t60              temp    const char *                    4     300
   t61              temp    const char *                    4     304
   t62              temp    char                            1     308
   t63              temp    char                            1     312
   t64              temp    int                             4     316
   t65              temp    char                            1     320
   t66              temp    int                             4     324
   t67              temp    char                            1     328
   t68              temp    int                             4     332
   t69              temp    char                            1     336
   t70              temp    int                             4     340
   t71              temp    int                             4     344
   t72              temp    const char *                    4     348
   t73              temp    const char *                    4     352
   t74              temp    char                            1     356
   t75              temp    char                            1     360
   t76              temp    int                             4     364
   t77              temp    char                            1     368
   t78              temp    int                             4     372
   t79              temp    char                            1     376
   t80              temp    int                             4     380
   t81              temp    char                            1     384
   t82              temp    int                             4     388
   t84              temp    const char *                    4     396
   t85              temp    const char *                    4     400
   t86              temp    char                            1     404
   t87              temp    char                            1     408
   t88              temp    int                             4     412
   t89              temp    char                            1     416
   t90              temp    int                             4     420
   t91              temp    char                            1     424
   t92              temp    int                             4     428
   t93              temp    char                            1     432
   t94              temp    int                             4     436
   t95              temp    int                             4     440
   (15 temporaries no longer used after optimization not shown)

 Code: 239 instruction(s)

    100        t1 = &buf
    101        t47 = t1
    102        t48 = "Hello\tWorld\n"
    103  L1:   t49 = t47
    104        t47 = t47 ptr+ 1
    105        t50 = t48
    106        t48 = t48 ptr+ 1
    107        t51 = *t50
    108        *t49 = t51
    109        if t51 char!= 0 goto L1
    110        t52 = t1
    111        t53 = 0
    112  L2:   t54 = t52
    113        t52 = t52 ptr+ 1
    114        t55 = *t54
    115        if t55 char== 0 goto L3
    116        t53 = t53 int+ 1
    117        t54 = t52
    118        t52 = t52 ptr+ 1
    119        t55 = *t54
    120        if t55 char== 0 goto L3
    121        t53 = t53 int+ 1
    122        goto L2
    123  L3:   t5 = buf[5]
    124        t6 = chartoint t5
    125        if t6 int== 9 goto L4
    126        t4 = 0
    127        goto L5
    128  L4:   t4 = 1
    129  L5:   t56 = t1
    130        t57 = 0
    131  L6:   t58 = t56
    132        t56 = t56 ptr+ 1
    133        t59 = *t58
    134        if t59 char== 0 goto L7
    135        t57 = t57 int+ 1
    136        t58 = t56
    137        t56 = t56 ptr+ 1
    138        t59 = *t58
    139        if t59 char== 0 goto L7
    140        t57 = t57 int+ 1
    141        goto L6
    142  L7:   t10 = t57 int- 1
    143        t11 = buf[t10]
    144        t12 = chartoint t11
    145        if t12 int== 10 goto L8
    146        t7 = 0
    147        goto L9
    148  L8:   t7 = 1
    149  L9:   param "%d %d %d\n"
    150        param t53
    151        param t4
    152        param t7
    153        call printf, 4
    154        t60 = "abc"
    155        t61 = "abd"
    156  L10:  t62 = *t60
    157        if t62 char== 0 goto L11
    158        t63 = *t60
    159        t64 = chartoint t63
    160        t65 = *t61
    161        t66 = chartoint t65
    162        if t64 int!= t66 goto L11
    163        t60 = t60 ptr+ 1
    164        t61 = t61 ptr+ 1
    165        t62 = *t60
    166        if t62 char== 0 goto L11
    167        t63 = *t60
    168        t64 = chartoint t63
    169        t65 = *t61
    170        t66 = chartoint t65
    171        if t64 int!= t66 goto L11
    172        t60 = t60 ptr+ 1
    173        t61 = t61 ptr+ 1
    174        goto L10
    175  L11:  t67 = *t60
    176        t68 = chartoint t67
    177        t69 = *t61
    178        t70 = chartoint t69
    179        t71 = t68 int- t70
    180        if t71 int< 0 goto L12
    181        t13 = 0
    182        goto L13
    183  L12:  t13 = 1
    184  L13:  t72 = "abc"
    185        t73 = "abc"
    186  L14:  t74 = *t72
    187        if t74 char== 0 goto L15
    188        t75 = *t72
    189        t76 = chartoint t75
    190        t77 = *t73
    191        t78 = chartoint t77
    192        if t76 int!= t78 goto L15
    193        t72 = t72 ptr+ 1
    194        t73 = t73 ptr+ 1
    195        t74 = *t72
    196        if t74 char== 0 goto L15
    197        t75 = *t72
    198        t76 = chartoint t75
    199        t77 = *t73
    200        t78 = chartoint t77
    201        if t76 int!= t78 goto L15
    202        t72 = t72 ptr+ 1
    203        t73 = t73 ptr+ 1
    204        goto L14
    205  L15:  t79 = *t72
    206        t80 = chartoint t79
    207        t81 = *t73
    208        t82 = chartoint t81
    209        t15 = t80 int- t82
    210        t84 = "b"
    211        t85 = "a"
    212  L16:  t86 = *t84
    213        if t86 char== 0 goto L17
    214        t87 = *t84
    215        t88 = chartoint t87
    216        t89 = *t85
    217        t90 = chartoint t89
    218        if t88 int!= t90 goto L17
    219        t84 = t84 ptr+ 1
    220        t85 = t85 ptr+ 1
    221        t86 = *t84
    222        if t86 char== 0 goto L17
    223        t87 = *t84
    224        t88 = chartoint t87
    225        t89 = *t85
    226        t90 = chartoint t89
    227        if t88 int!= t90 goto L17
    228        t84 = t84 ptr+ 1
    229        t85 = t85 ptr+ 1
    230        goto L16
    231  L17:  t91 = *t84
    232        t92 = chartoint t91
    233        t93 = *t85
    234        t94 = chartoint t93
    235        t95 = t92 int- t94
    236        if t95 int> 0 goto L18
    237        t16 = 0
    238        goto L19
    239  L18:  t16 = 1
    240  L19:  param "%d %d %d\n"
    241        param t13
    242        param t15
    243        param t16
    244        call printf, 4
    245        up[0] = 109
    246        up[1] = 105
    247        up[2] = 112
    248        up[3] = 115
    249        up[4] = 0
    250        up[5] = 0
    251        up[6] = 0
    252        up[7] = 0
    253        i = 0
    254  L20:  t18 = up[i]
    255        if t18 char== 0 goto L21
    256        t19 = up[i]
    257        t20 = chartoint t19
    258        t21 = t20 int- 97
    259        t22 = t21 int+ 65
    260        t23 = inttochar t22
    261        up[i] = t23
    262        i = i int+ 1
    263        t18 = up[i]
    264        if t18 char== 0 goto L21
    265        t19 = up[i]
    266        t20 = chartoint t19
    267        t21 = t20 int- 97
    268        t22 = t21 int+ 65
    269        t23 = inttochar t22
    270        up[i] = t23
    271        i = i int+ 1
    272        goto L20
    273  L21:  t25 = &up
    274        param "%s %c %c\n"
    275        param t25
    276        param 98
    277        param 97
    278        call printf, 4
    279        value = 0
    280        i = 0
    281  L22:  t28 = "40213" ptr+ i
    282        t29 = *t28
    283        if t29 char== 0 goto L23
    284        t30 = value int* 10
    285        t32 = *t28
    286        t33 = chartoint t32
    287        t34 = t33 int- 48
    288        value = t30 int+ t34
    289        i = i int+ 1
    290        t28 = "40213" ptr+ i
    291        t29 = *t28
    292        if t29 char== 0 goto L23
    293        t30 = value int* 10
    294        t32 = *t28
    295        t33 = chartoint t32
    296        t34 = t33 int- 48
    297        value = t30 int+ t34
    298        i = i int+ 1
    299        goto L22
    300  L23:  n = 0
    301        v = value
    302  L24:  if v int<= 0 goto L25
    303        t37 = n
    304        n = n int+ 1
    305        t39 = v int% 10
    306        t40 = 48 int+ t39
    307        t41 = inttochar t40
    308        out[t37] = t41
    309        v = v int/ 10
    310        if v int<= 0 goto L25
    311        t37 = n
    312        n = n int+ 1
    313        t39 = v int% 10
    314        t40 = 48 int+ t39
    315        t41 = inttochar t40
    316        out[t37] = t41
    317        v = v int/ 10
    318        goto L24
    319  L25:  out[n] = 0
    320        t43 = &out
    321        param "%d %s\n"
    322        param value
    323        param t43
    324        call printf, 3
    325        param "[%5s] [%-5s] [%.2s] [%c]\n"
    326        param "ab"
    327        param "ab"
    328        param "abcdef"
    329        param 81
    330        call printf, 5
    331        t44 = "quote\"d" ptr+ 5
    332        t45 = *t44
    333        t46 = chartoint t45
    334        param "%d %d\n"
    335        param 92
    336        param t46
    337        call printf, 3
    338        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   len                function      int (const char *)         -           5    -    2  _Z3lenPKc; defined
   copy               function      void (char *, const char *) -           6    -    1  _Z4copyPcPKc; defined
   cmp                function      int (const char *, const char *) -           7    -    3  _Z3cmpPKcS0_; defined
   main               function      int (void)                 -           8    -    0  defined

 scope: global > len()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param       5    4    1  s.1
   n                  variable      int                        local       5    4    2  n.2

 scope: global > copy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  parameter     char *                     param       6    4    1  d.3
   s                  parameter     const char *               param       6    4    1  s.4

 scope: global > cmp()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     const char *               param       7    4    4  a.5
   b                  parameter     const char *               param       7    4    3  b.6

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   buf                variable      char[32]                   local       9   32    5  buf.7
   up                 variable      char[8]                    local      13    8    4  up.8
   i                  variable      int                        local      14    4    9  i.9
   digits             variable      const char *               local      17    4    2  digits.10
   value              variable      int                        local      18    4    4  value.11
   out                variable      char[8]                    local      20    8    3  out.12
   n                  variable      int                        local      21    4    2  n.13
   v                  variable      int                        local      21    4    3  v.14

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
