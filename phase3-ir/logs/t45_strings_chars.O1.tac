============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t45_strings_chars.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 173 -> 211 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          173 -> 211   (-21% fewer)

   calls inlined                           6
   constants folded                        2
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded            6
   temporaries merged away                13
   dead instructions removed               6
   jumps removed or redirected             8
   unreachable instructions removed        1

============================================================================
 FUNCTION len(const char *)        (link name _Z3lenPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   n                local   int                             4       4
   t1               temp    const char *                    4       8
   t3               temp    char                            1      16
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    100       n = 0
    101  L1:  t1 = s
    102       s = s ptr+ 1
    103       t3 = *t1
    104       if t3 char== 0 goto L2
    105       n = n int+ 1
    106       goto L1
    107  L2:  return n

============================================================================
 FUNCTION copy(char *, const char *)        (link name _Z4copyPcPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                param   char *                          4       0
   s                param   const char *                    4       4
   t1               temp    char *                          4       8
   t3               temp    const char *                    4      16
   t5               temp    char                            1      24
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    108  L3:  t1 = d
    109       d = d ptr+ 1
    110       t3 = s
    111       s = s ptr+ 1
    112       t5 = *t3
    113       *t1 = t5
    114       if t5 char!= 0 goto L3
    115       return

============================================================================
 FUNCTION cmp(const char *, const char *)        (link name _Z3cmpPKcS0_)
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

    116  L4:  t1 = *a
    117       if t1 char== 0 goto L5
    118       t2 = *a
    119       t3 = chartoint t2
    120       t4 = *b
    121       t5 = chartoint t4
    122       if t3 int!= t5 goto L5
    123       a = a ptr+ 1
    124       b = b ptr+ 1
    125       goto L4
    126  L5:  t8 = *a
    127       t9 = chartoint t8
    128       t10 = *b
    129       t11 = chartoint t10
    130       t12 = t9 int- t11
    131       return t12

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 82 temporaries, frame 444 bytes

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
   t3               temp    int                             4      76
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
   t31              temp    const char *                    4     184
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
   (13 temporaries no longer used after optimization not shown)

 Code: 179 instruction(s)

    132        t1 = &buf
    133        t47 = t1
    134        t48 = "Hello\tWorld\n"
    135  L6:   t49 = t47
    136        t47 = t47 ptr+ 1
    137        t50 = t48
    138        t48 = t48 ptr+ 1
    139        t51 = *t50
    140        *t49 = t51
    141        if t51 char!= 0 goto L6
    142        t52 = t1
    143        t53 = 0
    144  L7:   t54 = t52
    145        t52 = t52 ptr+ 1
    146        t55 = *t54
    147        if t55 char== 0 goto L8
    148        t53 = t53 int+ 1
    149        goto L7
    150  L8:   t3 = t53
    151        t5 = buf[5]
    152        t6 = chartoint t5
    153        if t6 int== 9 goto L9
    154        t4 = 0
    155        goto L10
    156  L9:   t4 = 1
    157  L10:  t56 = &buf
    158        t57 = 0
    159  L11:  t58 = t56
    160        t56 = t56 ptr+ 1
    161        t59 = *t58
    162        if t59 char== 0 goto L12
    163        t57 = t57 int+ 1
    164        goto L11
    165  L12:  t10 = t57 int- 1
    166        t11 = buf[t10]
    167        t12 = chartoint t11
    168        if t12 int== 10 goto L13
    169        t7 = 0
    170        goto L14
    171  L13:  t7 = 1
    172  L14:  param "%d %d %d\n"
    173        param t3
    174        param t4
    175        param t7
    176        call printf, 4
    177        t60 = "abc"
    178        t61 = "abd"
    179  L15:  t62 = *t60
    180        if t62 char== 0 goto L16
    181        t63 = *t60
    182        t64 = chartoint t63
    183        t65 = *t61
    184        t66 = chartoint t65
    185        if t64 int!= t66 goto L16
    186        t60 = t60 ptr+ 1
    187        t61 = t61 ptr+ 1
    188        goto L15
    189  L16:  t67 = *t60
    190        t68 = chartoint t67
    191        t69 = *t61
    192        t70 = chartoint t69
    193        t71 = t68 int- t70
    194        if t71 int< 0 goto L17
    195        t13 = 0
    196        goto L18
    197  L17:  t13 = 1
    198  L18:  t72 = "abc"
    199        t73 = "abc"
    200  L19:  t74 = *t72
    201        if t74 char== 0 goto L20
    202        t75 = *t72
    203        t76 = chartoint t75
    204        t77 = *t73
    205        t78 = chartoint t77
    206        if t76 int!= t78 goto L20
    207        t72 = t72 ptr+ 1
    208        t73 = t73 ptr+ 1
    209        goto L19
    210  L20:  t79 = *t72
    211        t80 = chartoint t79
    212        t81 = *t73
    213        t82 = chartoint t81
    214        t15 = t80 int- t82
    215        t84 = "b"
    216        t85 = "a"
    217  L21:  t86 = *t84
    218        if t86 char== 0 goto L22
    219        t87 = *t84
    220        t88 = chartoint t87
    221        t89 = *t85
    222        t90 = chartoint t89
    223        if t88 int!= t90 goto L22
    224        t84 = t84 ptr+ 1
    225        t85 = t85 ptr+ 1
    226        goto L21
    227  L22:  t91 = *t84
    228        t92 = chartoint t91
    229        t93 = *t85
    230        t94 = chartoint t93
    231        t95 = t92 int- t94
    232        if t95 int> 0 goto L23
    233        t16 = 0
    234        goto L24
    235  L23:  t16 = 1
    236  L24:  param "%d %d %d\n"
    237        param t13
    238        param t15
    239        param t16
    240        call printf, 4
    241        up[0] = 109
    242        up[1] = 105
    243        up[2] = 112
    244        up[3] = 115
    245        up[4] = 0
    246        up[5] = 0
    247        up[6] = 0
    248        up[7] = 0
    249        i = 0
    250  L25:  t18 = up[i]
    251        if t18 char== 0 goto L26
    252        t19 = up[i]
    253        t20 = chartoint t19
    254        t21 = t20 int- 97
    255        t22 = t21 int+ 65
    256        t23 = inttochar t22
    257        up[i] = t23
    258        i = i int+ 1
    259        goto L25
    260  L26:  t25 = &up
    261        param "%s %c %c\n"
    262        param t25
    263        param 98
    264        param 97
    265        call printf, 4
    266        digits = "40213"
    267        value = 0
    268        i = 0
    269  L27:  t28 = digits ptr+ i
    270        t29 = *t28
    271        if t29 char== 0 goto L28
    272        t30 = value int* 10
    273        t31 = digits ptr+ i
    274        t32 = *t31
    275        t33 = chartoint t32
    276        t34 = t33 int- 48
    277        value = t30 int+ t34
    278        i = i int+ 1
    279        goto L27
    280  L28:  n = 0
    281        v = value
    282  L29:  if v int<= 0 goto L30
    283        t37 = n
    284        n = n int+ 1
    285        t39 = v int% 10
    286        t40 = 48 int+ t39
    287        t41 = inttochar t40
    288        out[t37] = t41
    289        v = v int/ 10
    290        goto L29
    291  L30:  out[n] = 0
    292        t43 = &out
    293        param "%d %s\n"
    294        param value
    295        param t43
    296        call printf, 3
    297        param "[%5s] [%-5s] [%.2s] [%c]\n"
    298        param "ab"
    299        param "ab"
    300        param "abcdef"
    301        param 81
    302        call printf, 5
    303        t44 = "quote\"d" ptr+ 5
    304        t45 = *t44
    305        t46 = chartoint t45
    306        param "%d %d\n"
    307        param 92
    308        param t46
    309        call printf, 3
    310        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

12 1 1
1 0 1
MIPS b a
40213 31204
[   ab] [ab   ] [ab] [Q]
92 34

   exit code 0, 547 instructions executed
