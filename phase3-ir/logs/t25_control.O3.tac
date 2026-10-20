============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t25_control.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 298 -> 250 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          298 -> 250   (16% fewer)

   constants folded                       10
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           35
   temporaries merged away                17
   dead instructions removed              22
   jumps removed or redirected            59
   unreachable instructions removed       40
   propagated across blocks               25
   dead assignments removed               12
   calls inlined                           7
   tail calls turned into jumps            0
   common subexpressions across blocks      5
   instructions moved out of loops         0

============================================================================
 FUNCTION classify(const char *)        (link name _Z8classifyPKc)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 5 temporaries, frame 64 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   state            local   int                             4       4
   c                local   char                            1       8
   digit            local   int                             4      12
   letter           local   int                             4      16
   t1               temp    char                            1      20
   t2               temp    char                            1      21
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t6               temp    int                             4      36
   (7 temporaries no longer used after optimization not shown)

 Code: 41 instruction(s)

    100        state = 0
    101  L1:   t1 = *s
    102        if t1 char== 0 goto L16
    103        t2 = *s
    104        t4 = chartoint t2
    105        if t4 int< 48 goto L2
    106        if t4 int<= 57 goto L3
    107  L2:   t3 = 0
    108        goto L4
    109  L3:   t3 = 1
    110  L4:   if t4 int< 97 goto L5
    111        if t4 int<= 122 goto L6
    112  L5:   if t4 int== 95 goto L6
    113        t6 = 0
    114        goto L14
    115  L6:   t6 = 1
    116        goto L14
    117  L7:   if t3 int== 0 goto L8
    118        state = 1
    119        goto L15
    120  L8:   if t6 int== 0 goto L9
    121        state = 3
    122        goto L15
    123  L9:   return 0
    124  L10:  if t4 int!= 46 goto L11
    125        state = 2
    126        goto L15
    127  L11:  if t3 int!= 0 goto L15
    128        return 0
    129  L12:  if t3 int!= 0 goto L15
    130        return 0
    131  L13:  if t3 int!= 0 goto L15
    132        if t6 int!= 0 goto L15
    133        return 0
    134  L14:  if state int== 0 goto L7
    135        if state int== 1 goto L10
    136        if state int== 2 goto L12
    137        if state int== 3 goto L13
    138  L15:  s = s ptr+ 1
    139        goto L1
    140  L16:  return state

============================================================================
 FUNCTION daysIn(int, int)        (link name _Z6daysInii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   month            param   int                             4       0
   year             param   int                             4       4
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 19 instruction(s)

    141        goto L24
    142  L17:  return 30
    143  L18:  t3 = year int% 4
    144        if t3 int!= 0 goto L19
    145        t4 = year int% 100
    146        if t4 int!= 0 goto L20
    147  L19:  t5 = year int% 400
    148        if t5 int!= 0 goto L21
    149  L20:  t2 = 29
    150        goto L22
    151  L21:  t2 = 28
    152  L22:  return t2
    153  L23:  return 31
    154  L24:  if month int== 4 goto L17
    155        if month int== 6 goto L17
    156        if month int== 9 goto L17
    157        if month int== 11 goto L17
    158        if month int== 2 goto L18
    159        goto L23

============================================================================
 FUNCTION grade(int)        (link name _Z5gradei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   score            param   int                             4       0
   t1               temp    char *                          4       4
   t2               temp    char *                          4       8
   t3               temp    char *                          4      12

 Code: 13 instruction(s)

    160        if score int< 90 goto L25
    161        t1 = "A"
    162        goto L30
    163  L25:  if score int< 75 goto L26
    164        t2 = "B"
    165        goto L29
    166  L26:  if score int< 60 goto L27
    167        t3 = "C"
    168        goto L28
    169  L27:  t3 = "F"
    170  L28:  t2 = t3
    171  L29:  t1 = t2
    172  L30:  return t1

============================================================================
 FUNCTION firstPair(int)        (link name _Z9firstPairi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   target           param   int                             4       0
   i                local   int                             4       4
   j                local   int                             4       8
   t1               temp    int                             4      12
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   (3 temporaries no longer used after optimization not shown)

 Code: 14 instruction(s)

    173        i = 1
    174  L31:  if i int>= 10 goto L34
    175        j = i
    176  L32:  if j int>= 10 goto L33
    177        t1 = i int* j
    178        if t1 int== target goto L35
    179        j = j int+ 1
    180        goto L32
    181  L33:  i = i int+ 1
    182        goto L31
    183  L34:  return -1
    184  L35:  t5 = i int* 10
    185        t6 = t5 int+ j
    186        return t6

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 37 temporaries, frame 348 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   triangle         local   int                             4       0
   skipped          local   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   n                local   int                             4      16
   digits           local   int                             4      20
   value            local   int                             4      24
   a                local   int                             4      28
   b                local   int                             4      32
   c                local   int                             4      36
   steps            local   int                             4      40
   k                local   int                             4      44
   countdown        local   int                             4      48
   t1               temp    int                             4      52
   t2               temp    int                             4      56
   t3               temp    int                             4      60
   t4               temp    int                             4      64
   t5               temp    int                             4      68
   t6               temp    int                             4      72
   t7               temp    int                             4      76
   t8               temp    int                             4      80
   t9               temp    int                             4      84
   t14              temp    int                             4     104
   t15              temp    int                             4     108
   t16              temp    int                             4     112
   t18              temp    int                             4     120
   t19              temp    int                             4     124
   t20              temp    int                             4     128
   t25              temp    int                             4     148
   t26              temp    int                             4     152
   t30              temp    int                             4     168
   t31              temp    int                             4     172
   t32              temp    int                             4     176
   t33              temp    int                             4     180
   t34              temp    int                             4     184
   t35              temp    int                             4     188
   t38              temp    int                             4     200
   t39              temp    int                             4     204
   t58              temp    int                             4     280
   t59              temp    int                             4     284
   t60              temp    int                             4     288
   t61              temp    int                             4     292
   t64              temp    int                             4     304
   t65              temp    int                             4     308
   t66              temp    int                             4     312
   t67              temp    int                             4     316
   t70              temp    int                             4     328
   t71              temp    int                             4     332
   t72              temp    int                             4     336
   t73              temp    int                             4     340
   (37 temporaries no longer used after optimization not shown)

 Code: 163 instruction(s)

    187        param "1234"
    188        t1 = call classify(const char *), 1
    189        param "12.5"
    190        t2 = call classify(const char *), 1
    191        param "x_9"
    192        t3 = call classify(const char *), 1
    193        param "9x"
    194        t4 = call classify(const char *), 1
    195        param ""
    196        t5 = call classify(const char *), 1
    197        param "%d %d %d %d %d\n"
    198        param t1
    199        param t2
    200        param t3
    201        param t4
    202        param t5
    203        call printf, 6
    204        param 2
    205        param 2024
    206        t6 = call daysIn(int, int), 2
    207        param 2
    208        param 1900
    209        t7 = call daysIn(int, int), 2
    210        param 2
    211        param 2000
    212        t8 = call daysIn(int, int), 2
    213        param 11
    214        param 2023
    215        t9 = call daysIn(int, int), 2
    216        param "%d %d %d %d\n"
    217        param t6
    218        param t7
    219        param t8
    220        param t9
    221        call printf, 5
    222        param "%s %s %s %s\n"
    223        param "A"
    224        param "B"
    225        param "C"
    226        param "F"
    227        call printf, 5
    228        t58 = 1
    229  L36:  if t58 int>= 10 goto L39
    230        t59 = t58
    231  L37:  if t59 int>= 10 goto L38
    232        t60 = t58 int* t59
    233        if t60 int== 24 goto L40
    234        t59 = t59 int+ 1
    235        goto L37
    236  L38:  t58 = t58 int+ 1
    237        goto L36
    238  L39:  t14 = -1
    239        goto L41
    240  L40:  t61 = t58 int* 10
    241        t14 = t61 int+ t59
    242  L41:  t64 = 1
    243  L42:  if t64 int>= 10 goto L45
    244        t65 = t64
    245  L43:  if t65 int>= 10 goto L44
    246        t66 = t64 int* t65
    247        if t66 int== 49 goto L46
    248        t65 = t65 int+ 1
    249        goto L43
    250  L44:  t64 = t64 int+ 1
    251        goto L42
    252  L45:  t15 = -1
    253        goto L47
    254  L46:  t67 = t64 int* 10
    255        t15 = t67 int+ t65
    256  L47:  t70 = 1
    257  L48:  if t70 int>= 10 goto L51
    258        t71 = t70
    259  L49:  if t71 int>= 10 goto L50
    260        t72 = t70 int* t71
    261        if t72 int== 97 goto L52
    262        t71 = t71 int+ 1
    263        goto L49
    264  L50:  t70 = t70 int+ 1
    265        goto L48
    266  L51:  t16 = -1
    267        goto L53
    268  L52:  t73 = t70 int* 10
    269        t16 = t73 int+ t71
    270  L53:  param "%d %d %d\n"
    271        param t14
    272        param t15
    273        param t16
    274        call printf, 4
    275        triangle = 0
    276        skipped = 0
    277        i = 1
    278  L54:  if i int> 6 goto L59
    279        if i int!= 4 goto L55
    280        skipped = skipped int+ 1
    281        goto L58
    282  L55:  j = 1
    283  L56:  if j int> 6 goto L58
    284        if j int> i goto L58
    285        t18 = i int+ j
    286        t19 = t18 int% 2
    287        if t19 int!= 0 goto L57
    288        t20 = i int* j
    289        triangle = triangle int+ t20
    290  L57:  j = j int+ 1
    291        goto L56
    292  L58:  i = i int+ 1
    293        goto L54
    294  L59:  param "%d %d\n"
    295        param triangle
    296        param skipped
    297        call printf, 3
    298        n = 0
    299        digits = 0
    300        value = 90210
    301  L60:  digits = digits int+ 1
    302        t25 = value int/ 10
    303        value = t25
    304        if t25 int!= 0 goto L60
    305  L61:  t26 = n int* n
    306        if t26 int> 200 goto L62
    307        n = n int+ 1
    308        goto L61
    309  L62:  a = 0
    310        b = 10
    311  L63:  if a int>= b goto L64
    312        a = a int+ 1
    313        b = b int- 1
    314        goto L63
    315  L64:  t30 = a int+ 1
    316        t31 = b int+ 2
    317        t32 = t30 int+ t31
    318        param "%d %d %d %d %d\n"
    319        param digits
    320        param n
    321        param t30
    322        param t31
    323        param t32
    324        call printf, 6
    325        steps = 0
    326        k = 27
    327  L65:  if k int== 1 goto L68
    328        t34 = k int% 2
    329        if t34 int== 0 goto L66
    330        t35 = k int* 3
    331        t33 = t35 int+ 1
    332        goto L67
    333  L66:  t33 = k int/ 2
    334  L67:  k = t33
    335        t38 = steps int+ 1
    336        steps = t38
    337        if t38 int<= 200 goto L65
    338  L68:  countdown = 3
    339  L69:  t39 = countdown
    340        countdown = countdown int- 1
    341        if t39 int<= 0 goto L70
    342        param "%d "
    343        param countdown
    344        call printf, 2
    345        goto L69
    346  L70:  param "\n%d\n"
    347        param steps
    348        call printf, 2
    349        return digits


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   classify           function      int (const char *)         -           9    -    5  _Z8classifyPKc; defined
   daysIn             function      int (int, int)             -          35    -    4  _Z6daysInii; defined
   grade              function      const char *(int)          -          43    -    4  _Z5gradei; defined
   firstPair          function      int (int)                  -          47    -    3  _Z9firstPairi; defined
   main               function      int (void)                 -          57    -    0  defined

 scope: global > classify()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param       9    4    3  s.1
   state              variable      int                        local      10    4    5  state.2

 scope: global > classify() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      char                       local      12    1    6  c.3
   digit              variable      int                        local      13    4    4  digit.4
   letter             variable      int                        local      13    4    2  letter.5

 scope: global > daysIn()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   month              parameter     int                        param      35    4    1  month.6
   year               parameter     int                        param      35    4    3  year.7

 scope: global > grade()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   score              parameter     int                        param      43    4    3  score.8

 scope: global > firstPair()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   target             parameter     int                        param      47    4    1  target.9
   found              label         -                          -          53    -    1  _Z9firstPairi.found
   i                  variable      int                        local      48    4    6  i.10
   j                  variable      int                        local      48    4    5  j.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   triangle           variable      int                        local      63    4    2  triangle.12
   skipped            variable      int                        local      63    4    2  skipped.13
   n                  variable      int                        local      74    4    4  n.16
   digits             variable      int                        local      74    4    3  digits.17
   value              variable      int                        local      74    4    2  value.18
   a                  variable      int                        local      77    4    6  a.19
   b                  variable      int                        local      77    4    6  b.20
   c                  variable      int                        local      77    4    2  c.21
   steps              variable      int                        local      82    4    2  steps.22
   k                  variable      int                        local      82    4    5  k.23
   countdown          variable      int                        local      88    4    2  countdown.24

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      64    4    6  i.14

 scope: global > main() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      66    4    5  j.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
