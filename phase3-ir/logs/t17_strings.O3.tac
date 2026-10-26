============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_strings.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 348 -> 395 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          348 -> 395   (-13% fewer)

   constants folded                        5
   algebraic simplifications               3
   common subexpressions                  10
   copies / constants forwarded           27
   temporaries merged away                25
   dead instructions removed              23
   jumps removed or redirected            26
   unreachable instructions removed        2
   propagated across blocks               10
   dead assignments removed               10
   calls inlined                          12
   tail calls turned into jumps            0
   common subexpressions across blocks      1
   instructions moved out of loops         1

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

 Code: 8 instruction(s)

    100       n = 0
    101  L1:  t1 = s ptr+ n
    102       t2 = *t1
    103       t3 = chartoint t2
    104       if t3 int== 0 goto L2
    105       n = n int+ 1
    106       goto L1
    107  L2:  return n

============================================================================
 FUNCTION copy(char *, const char *)        (link name _Z4copyPcPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   to               param   char *                          4       0
   from             param   const char *                    4       4
   t1               temp    char *                          4       8
   t3               temp    const char *                    4      16
   t5               temp    char                            1      24
   t6               temp    int                             4      28
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    108  L3:  t1 = to
    109       to = to ptr+ 1
    110       t3 = from
    111       from = from ptr+ 1
    112       t5 = *t3
    113       *t1 = t5
    114       t6 = chartoint t5
    115       if t6 int!= 0 goto L3
    116       return

============================================================================
 FUNCTION compare(const char *, const char *)        (link name _Z7comparePKcS0_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 10 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   const char *                    4       0
   b                param   const char *                    4       4
   t1               temp    char                            1       8
   t2               temp    char                            1       9
   t3               temp    int                             4      12
   t4               temp    char                            1      16
   t5               temp    int                             4      20
   t8               temp    char                            1      32
   t9               temp    int                             4      36
   t10              temp    char                            1      40
   t11              temp    int                             4      44
   t12              temp    int                             4      48
   (2 temporaries no longer used after optimization not shown)

 Code: 16 instruction(s)

    117  L4:  t1 = *a
    118       if t1 char== 0 goto L5
    119       t2 = *a
    120       t3 = chartoint t2
    121       t4 = *b
    122       t5 = chartoint t4
    123       if t3 int!= t5 goto L5
    124       a = a ptr+ 1
    125       b = b ptr+ 1
    126       goto L4
    127  L5:  t8 = *a
    128       t9 = chartoint t8
    129       t10 = *b
    130       t11 = chartoint t10
    131       t12 = t9 int- t11
    132       return t12

============================================================================
 FUNCTION reverse(char *)        (link name _Z7reversePc)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 8 temporaries, frame 76 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0
   i                local   int                             4       4
   j                local   int                             4       8
   t                local   char                            1      12
   t3               temp    char *                          4      24
   t4               temp    char                            1      28
   t6               temp    char *                          4      36
   t7               temp    char                            1      40
   t12              temp    int                             4      60
   t13              temp    const char *                    4      64
   t14              temp    char                            1      68
   t15              temp    int                             4      72
   (7 temporaries no longer used after optimization not shown)

 Code: 20 instruction(s)

    133       i = 0
    134       t12 = 0
    135  L6:  t13 = s ptr+ t12
    136       t14 = *t13
    137       t15 = chartoint t14
    138       if t15 int== 0 goto L7
    139       t12 = t12 int+ 1
    140       goto L6
    141  L7:  j = t12 int- 1
    142  L8:  if i int>= j goto L9
    143       t3 = s ptr+ i
    144       t4 = *t3
    145       t6 = s ptr+ j
    146       t7 = *t6
    147       *t3 = t7
    148       *t6 = t4
    149       i = i int+ 1
    150       j = j int- 1
    151       goto L8
    152  L9:  return

============================================================================
 FUNCTION find(const char *, char)        (link name _Z4findPKcc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 5 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   text             param   const char *                    4       0
   c                param   char                            1       4
   i                local   int                             4       8
   t1               temp    const char *                    4      12
   t2               temp    char                            1      16
   t4               temp    char                            1      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   (3 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    153        i = 0
    154        t6 = chartoint c
    155  L10:  t1 = text ptr+ i
    156        t2 = *t1
    157        if t2 char== 0 goto L12
    158        t4 = *t1
    159        t5 = chartoint t4
    160        if t5 int!= t6 goto L11
    161        return i
    162  L11:  i = i int+ 1
    163        goto L10
    164  L12:  return -1

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

 Code: 22 instruction(s)

    165        sign = 1
    166        v = 0
    167        t1 = *s
    168        t2 = chartoint t1
    169        if t2 int!= 45 goto L13
    170        sign = -1
    171        s = s ptr+ 1
    172  L13:  t5 = *s
    173        t6 = chartoint t5
    174        if t6 int< 48 goto L14
    175        t7 = *s
    176        t8 = chartoint t7
    177        if t8 int> 57 goto L14
    178        t9 = v int* 10
    179        t10 = *s
    180        t11 = chartoint t10
    181        t12 = t11 int- 48
    182        v = t9 int+ t12
    183        s = s ptr+ 1
    184        goto L13
    185  L14:  t15 = sign int* v
    186        return t15

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

 Code: 30 instruction(s)

    187        n = 0
    188        if v int< 0 goto L15
    189        t1 = 0
    190        goto L16
    191  L15:  t1 = 1
    192  L16:  if t1 int== 0 goto L17
    193        v = int- v
    194  L17:  t3 = n
    195        n = n int+ 1
    196        t5 = v int% 10
    197        t6 = 48 int+ t5
    198        t7 = inttochar t6
    199        tmp[t3] = t7
    200        t8 = v int/ 10
    201        v = t8
    202        if t8 int> 0 goto L17
    203        if t1 int== 0 goto L18
    204        t9 = n
    205        n = n int+ 1
    206        tmp[t9] = 45
    207  L18:  if n int<= 0 goto L19
    208        t11 = out
    209        out = out ptr+ 1
    210        t13 = n int- 1
    211        n = t13
    212        t14 = tmp[t13]
    213        *t11 = t14
    214        goto L18
    215  L19:  *out = 0
    216        return

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

 Code: 23 instruction(s)

    217        i = 0
    218        t14 = 0
    219  L20:  t15 = s ptr+ t14
    220        t16 = *t15
    221        t17 = chartoint t16
    222        if t17 int== 0 goto L21
    223        t14 = t14 int+ 1
    224        goto L20
    225  L21:  j = t14 int- 1
    226  L22:  if i int>= j goto L23
    227        t3 = i
    228        i = i int+ 1
    229        t5 = s ptr+ t3
    230        t6 = *t5
    231        t7 = chartoint t6
    232        t8 = j
    233        j = j int- 1
    234        t10 = s ptr+ t8
    235        t11 = *t10
    236        t12 = chartoint t11
    237        if t7 int== t12 goto L22
    238        return 0
    239  L23:  return 1

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

 Code: 18 instruction(s)

    240        words = 0
    241        inside = 0
    242  L24:  t1 = *s
    243        if t1 char== 0 goto L28
    244        t2 = *s
    245        t3 = chartoint t2
    246        if t3 int== 32 goto L25
    247        t4 = *s
    248        t5 = chartoint t4
    249        if t5 int!= 9 goto L26
    250  L25:  inside = 0
    251        goto L27
    252  L26:  if inside int!= 0 goto L27
    253        inside = 1
    254        words = words int+ 1
    255  L27:  s = s ptr+ 1
    256        goto L24
    257  L28:  return words

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
   t78              temp    const char *                    4     384
   t79              temp    char                            1     388
   t80              temp    char                            1     392
   t81              temp    int                             4     396
   t84              temp    int                             4     408
   t86              temp    const char *                    4     416
   t87              temp    char                            1     420
   t88              temp    char                            1     424
   t89              temp    int                             4     428
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

 Code: 237 instruction(s)

    258        names[0] = "delta"
    259        names[4] = "alpha"
    260        names[8] = "charlie"
    261        t1 = &buf
    262        t55 = t1
    263        t56 = "compiler"
    264  L29:  t57 = t55
    265        t55 = t55 ptr+ 1
    266        t58 = t56
    267        t56 = t56 ptr+ 1
    268        t59 = *t58
    269        *t57 = t59
    270        t60 = chartoint t59
    271        if t60 int!= 0 goto L29
    272        t62 = 0
    273  L30:  t63 = t1 ptr+ t62
    274        t64 = *t63
    275        t65 = chartoint t64
    276        if t65 int== 0 goto L31
    277        t62 = t62 int+ 1
    278        goto L30
    279  L31:  param "%s %d\n"
    280        param t1
    281        param t62
    282        call printf, 3
    283        t67 = 0
    284        param t1
    285        t68 = call length(const char *), 1
    286        t69 = t68 int- 1
    287  L32:  if t67 int>= t69 goto L33
    288        t70 = t1 ptr+ t67
    289        t71 = *t70
    290        t72 = t1 ptr+ t69
    291        t73 = *t72
    292        *t70 = t73
    293        *t72 = t71
    294        t67 = t67 int+ 1
    295        t69 = t69 int- 1
    296        goto L32
    297  L33:  t76 = 0
    298  L34:  t78 = t1 ptr+ t76
    299        t79 = *t78
    300        if t79 char== 0 goto L36
    301        t80 = *t78
    302        t81 = chartoint t80
    303        if t81 int!= 112 goto L35
    304        t8 = t76
    305        goto L37
    306  L35:  t76 = t76 int+ 1
    307        goto L34
    308  L36:  t8 = -1
    309  L37:  t84 = 0
    310  L38:  t86 = t1 ptr+ t84
    311        t87 = *t86
    312        if t87 char== 0 goto L40
    313        t88 = *t86
    314        t89 = chartoint t88
    315        if t89 int!= 122 goto L39
    316        t10 = t84
    317        goto L41
    318  L39:  t84 = t84 int+ 1
    319        goto L38
    320  L40:  t10 = -1
    321  L41:  param "%s %d %d\n"
    322        param t1
    323        param t8
    324        param t10
    325        call printf, 4
    326        t90 = "abc"
    327        t91 = "abd"
    328  L42:  t92 = *t90
    329        if t92 char== 0 goto L43
    330        t93 = *t90
    331        t94 = chartoint t93
    332        t95 = *t91
    333        t96 = chartoint t95
    334        if t94 int!= t96 goto L43
    335        t90 = t90 ptr+ 1
    336        t91 = t91 ptr+ 1
    337        goto L42
    338  L43:  t97 = *t90
    339        t98 = chartoint t97
    340        t99 = *t91
    341        t100 = chartoint t99
    342        t101 = t98 int- t100
    343        if t101 int< 0 goto L44
    344        t11 = 0
    345        goto L45
    346  L44:  t11 = 1
    347  L45:  t102 = "abc"
    348        t103 = "abc"
    349  L46:  t104 = *t102
    350        if t104 char== 0 goto L47
    351        t105 = *t102
    352        t106 = chartoint t105
    353        t107 = *t103
    354        t108 = chartoint t107
    355        if t106 int!= t108 goto L47
    356        t102 = t102 ptr+ 1
    357        t103 = t103 ptr+ 1
    358        goto L46
    359  L47:  t109 = *t102
    360        t110 = chartoint t109
    361        t111 = *t103
    362        t112 = chartoint t111
    363        t13 = t110 int- t112
    364        t114 = "b"
    365        t115 = "abc"
    366  L48:  t116 = *t114
    367        if t116 char== 0 goto L49
    368        t117 = *t114
    369        t118 = chartoint t117
    370        t119 = *t115
    371        t120 = chartoint t119
    372        if t118 int!= t120 goto L49
    373        t114 = t114 ptr+ 1
    374        t115 = t115 ptr+ 1
    375        goto L48
    376  L49:  t121 = *t114
    377        t122 = chartoint t121
    378        t123 = *t115
    379        t124 = chartoint t123
    380        t125 = t122 int- t124
    381        if t125 int> 0 goto L50
    382        t14 = 0
    383        goto L51
    384  L50:  t14 = 1
    385  L51:  param "%d %d %d\n"
    386        param t11
    387        param t13
    388        param t14
    389        call printf, 4
    390        smallest = 0
    391        i.32 = 1
    392  L52:  if i.32 int>= 3 goto L56
    393        t16 = i.32 int<< 2                  (w = 4)
    394        t17 = names[t16]
    395        t18 = smallest int<< 2              (w = 4)
    396        t19 = names[t18]
    397        t126 = t17
    398        t127 = t19
    399  L53:  t128 = *t126
    400        if t128 char== 0 goto L54
    401        t129 = *t126
    402        t130 = chartoint t129
    403        t131 = *t127
    404        t132 = chartoint t131
    405        if t130 int!= t132 goto L54
    406        t126 = t126 ptr+ 1
    407        t127 = t127 ptr+ 1
    408        goto L53
    409  L54:  t133 = *t126
    410        t134 = chartoint t133
    411        t135 = *t127
    412        t136 = chartoint t135
    413        t137 = t134 int- t136
    414        if t137 int>= 0 goto L55
    415        smallest = i.32
    416  L55:  i.32 = i.32 int+ 1
    417        goto L52
    418  L56:  t22 = smallest int<< 2              (w = 4)
    419        t23 = names[t22]
    420        t24 = names[8]
    421        t25 = t24 ptr+ 3
    422        t26 = *t25
    423        t27 = chartoint t26
    424        param "%s %c\n"
    425        param t23
    426        param t27
    427        call printf, 3
    428        t29 = &num
    429        param -40213
    430        param t29
    431        call toText(int, char *), 2
    432        param t29
    433        t32 = call toNumber(const char *), 1
    434        t33 = t32 int+ 1
    435        param "77x"
    436        t34 = call toNumber(const char *), 1
    437        param "%s %d %d\n"
    438        param t29
    439        param t33
    440        param t34
    441        call printf, 4
    442        param "level"
    443        t35 = call isPalindrome(const char *), 1
    444        param "lever"
    445        t36 = call isPalindrome(const char *), 1
    446        param "  the quick  brown fox "
    447        t37 = call countWords(const char *), 1
    448        param "%d %d %d\n"
    449        param t35
    450        param t36
    451        param t37
    452        call printf, 4
    453        upper[0] = 109
    454        upper[1] = 105
    455        upper[2] = 120
    456        upper[3] = 101
    457        upper[4] = 100
    458        upper[5] = 0
    459        upper[6] = 0
    460        upper[7] = 0
    461        i.34 = 0
    462  L57:  t38 = upper[i.34]
    463        if t38 char== 0 goto L59
    464        t39 = upper[i.34]
    465        t40 = chartoint t39
    466        if t40 int< 97 goto L58
    467        t41 = upper[i.34]
    468        t42 = chartoint t41
    469        if t42 int> 122 goto L58
    470        t43 = upper[i.34]
    471        t44 = chartoint t43
    472        t45 = t44 int- 97
    473        t46 = t45 int+ 65
    474        t47 = inttochar t46
    475        upper[i.34] = t47
    476  L58:  i.34 = i.34 int+ 1
    477        goto L57
    478  L59:  t49 = &upper
    479        param "%s %d\n"
    480        param t49
    481        param 8
    482        call printf, 3
    483        t138 = names[4]
    484        t139 = 0
    485  L60:  t140 = t138 ptr+ t139
    486        t141 = *t140
    487        t142 = chartoint t141
    488        if t142 int== 0 goto L61
    489        t139 = t139 int+ 1
    490        goto L60
    491  L61:  t52 = buf[0]
    492        t53 = chartoint t52
    493        t54 = t139 int+ t53
    494        return t54


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   length             function      int (const char *)         -           5    -    4  _Z6lengthPKc; defined
   copy               function      void (char *, const char *) -           7    -    1  _Z4copyPcPKc; defined
   compare            function      int (const char *, const char *) -           9    -    4  _Z7comparePKcS0_; defined
   reverse            function      void (char *)              -          14    -    1  _Z7reversePc; defined
   find               function      int (const char *, char)   -          19    -    2  _Z4findPKcc; defined
   toNumber           function      int (const char *)         -          24    -    2  _Z8toNumberPKc; defined
   toText             function      void (int, char *)         -          31    -    1  _Z6toTextiPc; defined
   isPalindrome       function      int (const char *)         -          41    -    2  _Z12isPalindromePKc; defined
   countWords         function      int (const char *)         -          47    -    1  _Z10countWordsPKc; defined
   main               function      int (void)                 -          56    -    0  defined

 scope: global > length()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param       5    4    1  s.1
   n                  variable      int                        local       5    4    3  n.2

 scope: global > copy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   to                 parameter     char *                     param       7    4    1  to.3
   from               parameter     const char *               param       7    4    1  from.4

 scope: global > compare()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     const char *               param       9    4    4  a.5
   b                  parameter     const char *               param       9    4    3  b.6

 scope: global > reverse()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     char *                     param      14    4    5  s.7
   i                  variable      int                        local      15    4    4  i.8
   j                  variable      int                        local      15    4    4  j.9

 scope: global > reverse() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      char                       local      16    1    1  t.10

 scope: global > find()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   text               parameter     const char *               param      19    4    2  text.11
   c                  parameter     char                       param      19    1    1  c.12

 scope: global > find() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      20    4    4  i.13

 scope: global > toNumber()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      24    4    6  s.14
   sign               variable      int                        local      25    4    2  sign.15
   v                  variable      int                        local      25    4    3  v.16

 scope: global > toText()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      31    4    6  v.17
   out                parameter     char *                     param      31    4    2  out.18
   tmp                variable      char[12]                   local      32   12    3  tmp.19
   n                  variable      int                        local      33    4    4  n.20
   neg                variable      int                        local      33    4    2  neg.21

 scope: global > isPalindrome()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      41    4    3  s.22
   i                  variable      int                        local      42    4    2  i.23
   j                  variable      int                        local      42    4    2  j.24

 scope: global > countWords()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param      47    4    4  s.25
   words              variable      int                        local      48    4    2  words.26
   inside             variable      int                        local      48    4    3  inside.27

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   buf                variable      char[32]                   local      57   32    8  buf.28
   num                variable      char[16]                   local      57   16    3  num.29
   names              variable      const char *[3]            local      58   12    5  names.30
   smallest           variable      int                        local      64    4    3  smallest.31
   upper              variable      char[8]                    local      70    8    7  upper.33

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      65    4    4  i.32
   i                  variable      int                        local      71    4    6  i.34

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
