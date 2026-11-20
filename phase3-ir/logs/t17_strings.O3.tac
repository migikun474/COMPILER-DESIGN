============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_strings.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 348 -> 451 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          348 -> 451   (-29% fewer)

   constants folded                        5
   algebraic simplifications               3
   common subexpressions                  10
   copies / constants forwarded           28
   temporaries merged away                25
   dead instructions removed              23
   jumps removed or redirected            26
   unreachable instructions removed        2
   propagated across blocks               10
   dead assignments removed               10
   calls inlined                          12
   tail calls turned into jumps            0
   common subexpressions across blocks      1
   loops unrolled                         16
   unreachable functions removed           4

============================================================================
 FUNCTION length(const char *)        (link name _Z6lengthPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   n                local   int                             4       4
   t1               temp    const char *                    4       8
   t2               temp    char                            1      12
   t3               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 13 instruction(s)

    100       n = 0
    101  L1:  t1 = s ptr+ n
    102       t2 = *t1
    103       t3 = chartoint t2
    104       if t3 int== 0 goto L2
    105       n = n int+ 1
    106       t1 = s ptr+ n
    107       t2 = *t1
    108       t3 = chartoint t2
    109       if t3 int== 0 goto L2
    110       n = n int+ 1
    111       goto L1
    112  L2:  return n

============================================================================
 FUNCTION toNumber(const char *)        (link name _Z8toNumberPKc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 11 temporaries, frame 72 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   sign             local   int                             4       4
   v                local   int                             4       8
   t1               temp    char                            1      12
   t2               temp    int                             4      16
   t5               temp    char                            1      28
   t6               temp    int                             4      32
   t7               temp    char                            1      36
   t8               temp    int                             4      40
   t9               temp    int                             4      44
   t10              temp    char                            1      48
   t11              temp    int                             4      52
   t12              temp    int                             4      56
   t15              temp    int                             4      68
   (4 temporaries no longer used after optimization not shown)

 Code: 34 instruction(s)

    113       sign = 1
    114       v = 0
    115       t1 = *s
    116       t2 = chartoint t1
    117       if t2 int!= 45 goto L3
    118       sign = -1
    119       s = s ptr+ 1
    120  L3:  t5 = *s
    121       t6 = chartoint t5
    122       if t6 int< 48 goto L4
    123       t7 = *s
    124       t8 = chartoint t7
    125       if t8 int> 57 goto L4
    126       t9 = v int* 10
    127       t10 = *s
    128       t11 = chartoint t10
    129       t12 = t11 int- 48
    130       v = t9 int+ t12
    131       s = s ptr+ 1
    132       t5 = *s
    133       t6 = chartoint t5
    134       if t6 int< 48 goto L4
    135       t7 = *s
    136       t8 = chartoint t7
    137       if t8 int> 57 goto L4
    138       t9 = v int* 10
    139       t10 = *s
    140       t11 = chartoint t10
    141       t12 = t11 int- 48
    142       v = t9 int+ t12
    143       s = s ptr+ 1
    144       goto L3
    145  L4:  t15 = sign int* v
    146       return t15

============================================================================
 FUNCTION toText(int, char *)        (link name _Z6toTextiPc)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 10 temporaries, frame 84 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   out              param   char *                          4       4
   tmp              local   char[12]                       12       8
   n                local   int                             4      20
   neg              local   int                             4      24
   t1               temp    int                             4      28
   t3               temp    int                             4      36
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t7               temp    char                            1      52
   t8               temp    int                             4      56
   t9               temp    int                             4      60
   t11              temp    char *                          4      68
   t13              temp    int                             4      76
   t14              temp    char                            1      80
   (4 temporaries no longer used after optimization not shown)

 Code: 37 instruction(s)

    147       n = 0
    148       if v int< 0 goto L5
    149       t1 = 0
    150       goto L6
    151  L5:  t1 = 1
    152  L6:  if t1 int== 0 goto L7
    153       v = int- v
    154  L7:  t3 = n
    155       n = n int+ 1
    156       t5 = v int% 10
    157       t6 = 48 int+ t5
    158       t7 = inttochar t6
    159       tmp[t3] = t7
    160       t8 = v int/ 10
    161       v = t8
    162       if t8 int> 0 goto L7
    163       if t1 int== 0 goto L8
    164       t9 = n
    165       n = n int+ 1
    166       tmp[t9] = 45
    167  L8:  if n int<= 0 goto L9
    168       t11 = out
    169       out = out ptr+ 1
    170       t13 = n int- 1
    171       n = t13
    172       t14 = tmp[t13]
    173       *t11 = t14
    174       if t13 int<= 0 goto L9
    175       t11 = out
    176       out = out ptr+ 1
    177       t13 = n int- 1
    178       n = t13
    179       t14 = tmp[t13]
    180       *t11 = t14
    181       goto L8
    182  L9:  *out = 0
    183       return

============================================================================
 FUNCTION isPalindrome(const char *)        (link name _Z12isPalindromePKc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 12 temporaries, frame 80 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   i                local   int                             4       4
   j                local   int                             4       8
   t3               temp    int                             4      20
   t5               temp    const char *                    4      28
   t6               temp    char                            1      32
   t7               temp    int                             4      36
   t8               temp    int                             4      40
   t10              temp    const char *                    4      48
   t11              temp    char                            1      52
   t12              temp    int                             4      56
   t14              temp    int                             4      64
   t15              temp    const char *                    4      68
   t16              temp    char                            1      72
   t17              temp    int                             4      76
   (5 temporaries no longer used after optimization not shown)

 Code: 28 instruction(s)

    184        i = 0
    185        t14 = 0
    186  L10:  t15 = s ptr+ t14
    187        t16 = *t15
    188        t17 = chartoint t16
    189        if t17 int== 0 goto L11
    190        t14 = t14 int+ 1
    191        t15 = s ptr+ t14
    192        t16 = *t15
    193        t17 = chartoint t16
    194        if t17 int== 0 goto L11
    195        t14 = t14 int+ 1
    196        goto L10
    197  L11:  j = t14 int- 1
    198  L12:  if i int>= j goto L13
    199        t3 = i
    200        i = i int+ 1
    201        t5 = s ptr+ t3
    202        t6 = *t5
    203        t7 = chartoint t6
    204        t8 = j
    205        j = j int- 1
    206        t10 = s ptr+ t8
    207        t11 = *t10
    208        t12 = chartoint t11
    209        if t7 int== t12 goto L12
    210        return 0
    211  L13:  return 1

============================================================================
 FUNCTION countWords(const char *)        (link name _Z10countWordsPKc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   words            local   int                             4       4
   inside           local   int                             4       8
   t1               temp    char                            1      12
   t2               temp    char                            1      13
   t3               temp    int                             4      16
   t4               temp    char                            1      20
   t5               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 32 instruction(s)

    212        words = 0
    213        inside = 0
    214  L14:  t1 = *s
    215        if t1 char== 0 goto L21
    216        t2 = *s
    217        t3 = chartoint t2
    218        if t3 int== 32 goto L15
    219        t4 = *s
    220        t5 = chartoint t4
    221        if t5 int!= 9 goto L16
    222  L15:  inside = 0
    223        goto L17
    224  L16:  if inside int!= 0 goto L17
    225        inside = 1
    226        words = words int+ 1
    227  L17:  s = s ptr+ 1
    228        t1 = *s
    229        if t1 char== 0 goto L21
    230        t2 = *s
    231        t3 = chartoint t2
    232        if t3 int== 32 goto L18
    233        t4 = *s
    234        t5 = chartoint t4
    235        if t5 int!= 9 goto L19
    236  L18:  inside = 0
    237        goto L20
    238  L19:  if inside int!= 0 goto L20
    239        inside = 1
    240        words = words int+ 1
    241  L20:  s = s ptr+ 1
    242        goto L14
    243  L21:  return words

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 116 temporaries, frame 644 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   buf              local   char[32]                       32       0
   num              local   char[16]                       16      32
   names            local   const char *[3]                12      48
   smallest         local   int                             4      60
   i.32             local   int                             4      64
   upper            local   char[8]                         8      68
   i.34             local   int                             4      76
   t1               temp    char *                          4      80
   t8               temp    int                             4     108
   t10              temp    int                             4     116
   t11              temp    int                             4     120
   t13              temp    int                             4     128
   t14              temp    int                             4     132
   t16              temp    int                             4     140
   t17              temp    const char *                    4     144
   t18              temp    int                             4     148
   t19              temp    const char *                    4     152
   t22              temp    int                             4     164
   t23              temp    const char *                    4     168
   t24              temp    const char *                    4     172
   t25              temp    const char *                    4     176
   t26              temp    char                            1     180
   t27              temp    int                             4     184
   t29              temp    char *                          4     192
   t32              temp    int                             4     204
   t33              temp    int                             4     208
   t34              temp    int                             4     212
   t35              temp    int                             4     216
   t36              temp    int                             4     220
   t37              temp    int                             4     224
   t38              temp    char                            1     228
   t39              temp    char                            1     229
   t40              temp    int                             4     232
   t41              temp    char                            1     236
   t42              temp    int                             4     240
   t43              temp    char                            1     244
   t44              temp    int                             4     248
   t45              temp    int                             4     252
   t46              temp    int                             4     256
   t47              temp    char                            1     260
   t49              temp    char *                          4     268
   t52              temp    char                            1     280
   t53              temp    int                             4     284
   t54              temp    int                             4     288
   t55              temp    char *                          4     292
   t56              temp    const char *                    4     296
   t57              temp    char *                          4     300
   t58              temp    const char *                    4     304
   t59              temp    char                            1     308
   t60              temp    int                             4     312
   t62              temp    int                             4     320
   t63              temp    const char *                    4     324
   t64              temp    char                            1     328
   t65              temp    int                             4     332
   t67              temp    int                             4     340
   t68              temp    int                             4     344
   t69              temp    int                             4     348
   t70              temp    char *                          4     352
   t71              temp    char                            1     356
   t72              temp    char *                          4     360
   t73              temp    char                            1     364
   t76              temp    int                             4     376
   t77              temp    const char *                    4     380
   t78              temp    char                            1     384
   t79              temp    char                            1     388
   t80              temp    int                             4     392
   t84              temp    int                             4     408
   t85              temp    const char *                    4     412
   t86              temp    char                            1     416
   t87              temp    char                            1     420
   t88              temp    int                             4     424
   t90              temp    const char *                    4     432
   t91              temp    const char *                    4     436
   t92              temp    char                            1     440
   t93              temp    char                            1     444
   t94              temp    int                             4     448
   t95              temp    char                            1     452
   t96              temp    int                             4     456
   t97              temp    char                            1     460
   t98              temp    int                             4     464
   t99              temp    char                            1     468
   t100             temp    int                             4     472
   t101             temp    int                             4     476
   t102             temp    const char *                    4     480
   t103             temp    const char *                    4     484
   t104             temp    char                            1     488
   t105             temp    char                            1     492
   t106             temp    int                             4     496
   t107             temp    char                            1     500
   t108             temp    int                             4     504
   t109             temp    char                            1     508
   t110             temp    int                             4     512
   t111             temp    char                            1     516
   t112             temp    int                             4     520
   t114             temp    const char *                    4     528
   t115             temp    const char *                    4     532
   t116             temp    char                            1     536
   t117             temp    char                            1     540
   t118             temp    int                             4     544
   t119             temp    char                            1     548
   t120             temp    int                             4     552
   t121             temp    char                            1     556
   t122             temp    int                             4     560
   t123             temp    char                            1     564
   t124             temp    int                             4     568
   t125             temp    int                             4     572
   t126             temp    const char *                    4     576
   t127             temp    const char *                    4     580
   t128             temp    char                            1     584
   t129             temp    char                            1     588
   t130             temp    int                             4     592
   t131             temp    char                            1     596
   t132             temp    int                             4     600
   t133             temp    char                            1     604
   t134             temp    int                             4     608
   t135             temp    char                            1     612
   t136             temp    int                             4     616
   t137             temp    int                             4     620
   t138             temp    const char *                    4     624
   t139             temp    int                             4     628
   t140             temp    const char *                    4     632
   t141             temp    char                            1     636
   t142             temp    int                             4     640
   (26 temporaries no longer used after optimization not shown)

 Code: 307 instruction(s)

    244        names[0] = "delta"
    245        names[4] = "alpha"
    246        names[8] = "charlie"
    247        t1 = &buf
    248        t55 = t1
    249        t56 = "compiler"
    250  L22:  t57 = t55
    251        t55 = t55 ptr+ 1
    252        t58 = t56
    253        t56 = t56 ptr+ 1
    254        t59 = *t58
    255        *t57 = t59
    256        t60 = chartoint t59
    257        if t60 int!= 0 goto L22
    258        t62 = 0
    259  L23:  t63 = t1 ptr+ t62
    260        t64 = *t63
    261        t65 = chartoint t64
    262        if t65 int== 0 goto L24
    263        t62 = t62 int+ 1
    264        t63 = t1 ptr+ t62
    265        t64 = *t63
    266        t65 = chartoint t64
    267        if t65 int== 0 goto L24
    268        t62 = t62 int+ 1
    269        goto L23
    270  L24:  param "%s %d\n"
    271        param t1
    272        param t62
    273        call printf, 3
    274        t67 = 0
    275        param t1
    276        t68 = call length(const char *), 1
    277        t69 = t68 int- 1
    278  L25:  if t67 int>= t69 goto L26
    279        t70 = t1 ptr+ t67
    280        t71 = *t70
    281        t72 = t1 ptr+ t69
    282        t73 = *t72
    283        *t70 = t73
    284        *t72 = t71
    285        t67 = t67 int+ 1
    286        t69 = t69 int- 1
    287        if t67 int>= t69 goto L26
    288        t70 = t1 ptr+ t67
    289        t71 = *t70
    290        t72 = t1 ptr+ t69
    291        t73 = *t72
    292        *t70 = t73
    293        *t72 = t71
    294        t67 = t67 int+ 1
    295        t69 = t69 int- 1
    296        goto L25
    297  L26:  t76 = 0
    298  L27:  t77 = t1 ptr+ t76
    299        t78 = *t77
    300        if t78 char== 0 goto L29
    301        t79 = *t77
    302        t80 = chartoint t79
    303        if t80 int!= 112 goto L28
    304        t8 = t76
    305        goto L30
    306  L28:  t76 = t76 int+ 1
    307        goto L27
    308  L29:  t8 = -1
    309  L30:  t84 = 0
    310  L31:  t85 = t1 ptr+ t84
    311        t86 = *t85
    312        if t86 char== 0 goto L33
    313        t87 = *t85
    314        t88 = chartoint t87
    315        if t88 int!= 122 goto L32
    316        t10 = t84
    317        goto L34
    318  L32:  t84 = t84 int+ 1
    319        goto L31
    320  L33:  t10 = -1
    321  L34:  param "%s %d %d\n"
    322        param t1
    323        param t8
    324        param t10
    325        call printf, 4
    326        t90 = "abc"
    327        t91 = "abd"
    328  L35:  t92 = *t90
    329        if t92 char== 0 goto L36
    330        t93 = *t90
    331        t94 = chartoint t93
    332        t95 = *t91
    333        t96 = chartoint t95
    334        if t94 int!= t96 goto L36
    335        t90 = t90 ptr+ 1
    336        t91 = t91 ptr+ 1
    337        t92 = *t90
    338        if t92 char== 0 goto L36
    339        t93 = *t90
    340        t94 = chartoint t93
    341        t95 = *t91
    342        t96 = chartoint t95
    343        if t94 int!= t96 goto L36
    344        t90 = t90 ptr+ 1
    345        t91 = t91 ptr+ 1
    346        goto L35
    347  L36:  t97 = *t90
    348        t98 = chartoint t97
    349        t99 = *t91
    350        t100 = chartoint t99
    351        t101 = t98 int- t100
    352        if t101 int< 0 goto L37
    353        t11 = 0
    354        goto L38
    355  L37:  t11 = 1
    356  L38:  t102 = "abc"
    357        t103 = "abc"
    358  L39:  t104 = *t102
    359        if t104 char== 0 goto L40
    360        t105 = *t102
    361        t106 = chartoint t105
    362        t107 = *t103
    363        t108 = chartoint t107
    364        if t106 int!= t108 goto L40
    365        t102 = t102 ptr+ 1
    366        t103 = t103 ptr+ 1
    367        t104 = *t102
    368        if t104 char== 0 goto L40
    369        t105 = *t102
    370        t106 = chartoint t105
    371        t107 = *t103
    372        t108 = chartoint t107
    373        if t106 int!= t108 goto L40
    374        t102 = t102 ptr+ 1
    375        t103 = t103 ptr+ 1
    376        goto L39
    377  L40:  t109 = *t102
    378        t110 = chartoint t109
    379        t111 = *t103
    380        t112 = chartoint t111
    381        t13 = t110 int- t112
    382        t114 = "b"
    383        t115 = "abc"
    384  L41:  t116 = *t114
    385        if t116 char== 0 goto L42
    386        t117 = *t114
    387        t118 = chartoint t117
    388        t119 = *t115
    389        t120 = chartoint t119
    390        if t118 int!= t120 goto L42
    391        t114 = t114 ptr+ 1
    392        t115 = t115 ptr+ 1
    393        t116 = *t114
    394        if t116 char== 0 goto L42
    395        t117 = *t114
    396        t118 = chartoint t117
    397        t119 = *t115
    398        t120 = chartoint t119
    399        if t118 int!= t120 goto L42
    400        t114 = t114 ptr+ 1
    401        t115 = t115 ptr+ 1
    402        goto L41
    403  L42:  t121 = *t114
    404        t122 = chartoint t121
    405        t123 = *t115
    406        t124 = chartoint t123
    407        t125 = t122 int- t124
    408        if t125 int> 0 goto L43
    409        t14 = 0
    410        goto L44
    411  L43:  t14 = 1
    412  L44:  param "%d %d %d\n"
    413        param t11
    414        param t13
    415        param t14
    416        call printf, 4
    417        smallest = 0
    418        i.32 = 1
    419  L45:  if i.32 int>= 3 goto L49
    420        t16 = i.32 int<< 2                  (w = 4)
    421        t17 = names[t16]
    422        t18 = smallest int<< 2              (w = 4)
    423        t19 = names[t18]
    424        t126 = t17
    425        t127 = t19
    426  L46:  t128 = *t126
    427        if t128 char== 0 goto L47
    428        t129 = *t126
    429        t130 = chartoint t129
    430        t131 = *t127
    431        t132 = chartoint t131
    432        if t130 int!= t132 goto L47
    433        t126 = t126 ptr+ 1
    434        t127 = t127 ptr+ 1
    435        t128 = *t126
    436        if t128 char== 0 goto L47
    437        t129 = *t126
    438        t130 = chartoint t129
    439        t131 = *t127
    440        t132 = chartoint t131
    441        if t130 int!= t132 goto L47
    442        t126 = t126 ptr+ 1
    443        t127 = t127 ptr+ 1
    444        goto L46
    445  L47:  t133 = *t126
    446        t134 = chartoint t133
    447        t135 = *t127
    448        t136 = chartoint t135
    449        t137 = t134 int- t136
    450        if t137 int>= 0 goto L48
    451        smallest = i.32
    452  L48:  i.32 = i.32 int+ 1
    453        goto L45
    454  L49:  t22 = smallest int<< 2              (w = 4)
    455        t23 = names[t22]
    456        t24 = names[8]
    457        t25 = t24 ptr+ 3
    458        t26 = *t25
    459        t27 = chartoint t26
    460        param "%s %c\n"
    461        param t23
    462        param t27
    463        call printf, 3
    464        t29 = &num
    465        param -40213
    466        param t29
    467        call toText(int, char *), 2
    468        param t29
    469        t32 = call toNumber(const char *), 1
    470        t33 = t32 int+ 1
    471        param "77x"
    472        t34 = call toNumber(const char *), 1
    473        param "%s %d %d\n"
    474        param t29
    475        param t33
    476        param t34
    477        call printf, 4
    478        param "level"
    479        t35 = call isPalindrome(const char *), 1
    480        param "lever"
    481        t36 = call isPalindrome(const char *), 1
    482        param "  the quick  brown fox "
    483        t37 = call countWords(const char *), 1
    484        param "%d %d %d\n"
    485        param t35
    486        param t36
    487        param t37
    488        call printf, 4
    489        upper[0] = 109
    490        upper[1] = 105
    491        upper[2] = 120
    492        upper[3] = 101
    493        upper[4] = 100
    494        upper[5] = 0
    495        upper[6] = 0
    496        upper[7] = 0
    497        i.34 = 0
    498  L50:  t38 = upper[i.34]
    499        if t38 char== 0 goto L53
    500        t39 = upper[i.34]
    501        t40 = chartoint t39
    502        if t40 int< 97 goto L51
    503        t41 = upper[i.34]
    504        t42 = chartoint t41
    505        if t42 int> 122 goto L51
    506        t43 = upper[i.34]
    507        t44 = chartoint t43
    508        t45 = t44 int- 97
    509        t46 = t45 int+ 65
    510        t47 = inttochar t46
    511        upper[i.34] = t47
    512  L51:  i.34 = i.34 int+ 1
    513        t38 = upper[i.34]
    514        if t38 char== 0 goto L53
    515        t39 = upper[i.34]
    516        t40 = chartoint t39
    517        if t40 int< 97 goto L52
    518        t41 = upper[i.34]
    519        t42 = chartoint t41
    520        if t42 int> 122 goto L52
    521        t43 = upper[i.34]
    522        t44 = chartoint t43
    523        t45 = t44 int- 97
    524        t46 = t45 int+ 65
    525        t47 = inttochar t46
    526        upper[i.34] = t47
    527  L52:  i.34 = i.34 int+ 1
    528        goto L50
    529  L53:  t49 = &upper
    530        param "%s %d\n"
    531        param t49
    532        param 8
    533        call printf, 3
    534        t138 = names[4]
    535        t139 = 0
    536  L54:  t140 = t138 ptr+ t139
    537        t141 = *t140
    538        t142 = chartoint t141
    539        if t142 int== 0 goto L55
    540        t139 = t139 int+ 1
    541        t140 = t138 ptr+ t139
    542        t141 = *t140
    543        t142 = chartoint t141
    544        if t142 int== 0 goto L55
    545        t139 = t139 int+ 1
    546        goto L54
    547  L55:  t52 = buf[0]
    548        t53 = chartoint t52
    549        t54 = t139 int+ t53
    550        return t54


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   length             function      int (const char *)         -           4    -    4  _Z6lengthPKc; defined
   copy               function      void (char *, const char *) -           6    -    1  _Z4copyPcPKc; defined
   compare            function      int (const char *, const char *) -           8    -    4  _Z7comparePKcS0_; defined
   reverse            function      void (char *)              -          13    -    1  _Z7reversePc; defined
   find               function      int (const char *, char)   -          18    -    2  _Z4findPKcc; defined
   toNumber           function      int (const char *)         -          23    -    2  _Z8toNumberPKc; defined
   toText             function      void (int, char *)         -          30    -    1  _Z6toTextiPc; defined
   isPalindrome       function      int (const char *)         -          40    -    2  _Z12isPalindromePKc; defined
   countWords         function      int (const char *)         -          46    -    1  _Z10countWordsPKc; defined
   main               function      int (void)                 -          55    -    0  defined

 scope: global > length()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param       4    4    1  s.1
   n                  variable      int                        local       4    4    3  n.2

 scope: global > copy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   to                 parameter     char *                     param       6    4    1  to.3
   from               parameter     const char *               param       6    4    1  from.4

 scope: global > compare()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     const char *               param       8    4    4  a.5
   b                  parameter     const char *               param       8    4    3  b.6

 scope: global > reverse()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     char *                     param      13    4    5  s.7
   i                  variable      int                        local      14    4    4  i.8
   j                  variable      int                        local      14    4    4  j.9

 scope: global > reverse() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      char                       local      15    1    1  t.10

 scope: global > find()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   text               parameter     const char *               param      18    4    2  text.11
   c                  parameter     char                       param      18    1    1  c.12

 scope: global > find() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      19    4    4  i.13

 scope: global > toNumber()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      23    4    6  s.14
   sign               variable      int                        local      24    4    2  sign.15
   v                  variable      int                        local      24    4    3  v.16

 scope: global > toText()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      30    4    6  v.17
   out                parameter     char *                     param      30    4    2  out.18
   tmp                variable      char[12]                   local      31   12    3  tmp.19
   n                  variable      int                        local      32    4    4  n.20
   neg                variable      int                        local      32    4    2  neg.21

 scope: global > isPalindrome()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      40    4    3  s.22
   i                  variable      int                        local      41    4    2  i.23
   j                  variable      int                        local      41    4    2  j.24

 scope: global > countWords()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      46    4    4  s.25
   words              variable      int                        local      47    4    2  words.26
   inside             variable      int                        local      47    4    3  inside.27

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   buf                variable      char[32]                   local      56   32    8  buf.28
   num                variable      char[16]                   local      56   16    3  num.29
   names              variable      const char *[3]            local      57   12    5  names.30
   smallest           variable      int                        local      63    4    3  smallest.31
   upper              variable      char[8]                    local      69    8    7  upper.33

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      64    4    4  i.32
   i                  variable      int                        local      70    4    6  i.34

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
