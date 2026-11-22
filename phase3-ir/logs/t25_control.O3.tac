============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t25_control.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 298 -> 255 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          298 -> 255   (14% fewer)

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
   loops unrolled                          8
   unreachable functions removed           2

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

 Code: 195 instruction(s)

    160        param "1234"
    161        t1 = call classify(const char *), 1
    162        param "12.5"
    163        t2 = call classify(const char *), 1
    164        param "x_9"
    165        t3 = call classify(const char *), 1
    166        param "9x"
    167        t4 = call classify(const char *), 1
    168        param ""
    169        t5 = call classify(const char *), 1
    170        param "%d %d %d %d %d\n"
    171        param t1
    172        param t2
    173        param t3
    174        param t4
    175        param t5
    176        call printf, 6
    177        param 2
    178        param 2024
    179        t6 = call daysIn(int, int), 2
    180        param 2
    181        param 1900
    182        t7 = call daysIn(int, int), 2
    183        param 2
    184        param 2000
    185        t8 = call daysIn(int, int), 2
    186        param 11
    187        param 2023
    188        t9 = call daysIn(int, int), 2
    189        param "%d %d %d %d\n"
    190        param t6
    191        param t7
    192        param t8
    193        param t9
    194        call printf, 5
    195        param "%s %s %s %s\n"
    196        param "A"
    197        param "B"
    198        param "C"
    199        param "F"
    200        call printf, 5
    201        t58 = 1
    202  L25:  if t58 int>= 10 goto L28
    203        t59 = t58
    204  L26:  if t59 int>= 10 goto L27
    205        t60 = t58 int* t59
    206        if t60 int== 24 goto L29
    207        t59 = t59 int+ 1
    208        if t59 int>= 10 goto L27
    209        t60 = t58 int* t59
    210        if t60 int== 24 goto L29
    211        t59 = t59 int+ 1
    212        goto L26
    213  L27:  t58 = t58 int+ 1
    214        goto L25
    215  L28:  t14 = -1
    216        goto L30
    217  L29:  t61 = t58 int* 10
    218        t14 = t61 int+ t59
    219  L30:  t64 = 1
    220  L31:  if t64 int>= 10 goto L34
    221        t65 = t64
    222  L32:  if t65 int>= 10 goto L33
    223        t66 = t64 int* t65
    224        if t66 int== 49 goto L35
    225        t65 = t65 int+ 1
    226        if t65 int>= 10 goto L33
    227        t66 = t64 int* t65
    228        if t66 int== 49 goto L35
    229        t65 = t65 int+ 1
    230        goto L32
    231  L33:  t64 = t64 int+ 1
    232        goto L31
    233  L34:  t15 = -1
    234        goto L36
    235  L35:  t67 = t64 int* 10
    236        t15 = t67 int+ t65
    237  L36:  t70 = 1
    238  L37:  if t70 int>= 10 goto L40
    239        t71 = t70
    240  L38:  if t71 int>= 10 goto L39
    241        t72 = t70 int* t71
    242        if t72 int== 97 goto L41
    243        t71 = t71 int+ 1
    244        if t71 int>= 10 goto L39
    245        t72 = t70 int* t71
    246        if t72 int== 97 goto L41
    247        t71 = t71 int+ 1
    248        goto L38
    249  L39:  t70 = t70 int+ 1
    250        goto L37
    251  L40:  t16 = -1
    252        goto L42
    253  L41:  t73 = t70 int* 10
    254        t16 = t73 int+ t71
    255  L42:  param "%d %d %d\n"
    256        param t14
    257        param t15
    258        param t16
    259        call printf, 4
    260        triangle = 0
    261        skipped = 0
    262        i = 1
    263  L43:  if i int> 6 goto L49
    264        if i int!= 4 goto L44
    265        skipped = skipped int+ 1
    266        goto L48
    267  L44:  j = 1
    268  L45:  if j int> 6 goto L48
    269        if j int> i goto L48
    270        t18 = i int+ j
    271        t19 = t18 int% 2
    272        if t19 int!= 0 goto L46
    273        t20 = i int* j
    274        triangle = triangle int+ t20
    275  L46:  j = j int+ 1
    276        if j int> 6 goto L48
    277        if j int> i goto L48
    278        t18 = i int+ j
    279        t19 = t18 int% 2
    280        if t19 int!= 0 goto L47
    281        t20 = i int* j
    282        triangle = triangle int+ t20
    283  L47:  j = j int+ 1
    284        goto L45
    285  L48:  i = i int+ 1
    286        goto L43
    287  L49:  param "%d %d\n"
    288        param triangle
    289        param skipped
    290        call printf, 3
    291        n = 0
    292        digits = 0
    293        value = 90210
    294  L50:  digits = digits int+ 1
    295        t25 = value int/ 10
    296        value = t25
    297        if t25 int!= 0 goto L50
    298  L51:  t26 = n int* n
    299        if t26 int> 200 goto L52
    300        n = n int+ 1
    301        t26 = n int* n
    302        if t26 int> 200 goto L52
    303        n = n int+ 1
    304        goto L51
    305  L52:  a = 0
    306        b = 10
    307  L53:  if a int>= b goto L54
    308        a = a int+ 1
    309        b = b int- 1
    310        if a int>= b goto L54
    311        a = a int+ 1
    312        b = b int- 1
    313        goto L53
    314  L54:  t30 = a int+ 1
    315        t31 = b int+ 2
    316        t32 = t30 int+ t31
    317        param "%d %d %d %d %d\n"
    318        param digits
    319        param n
    320        param t30
    321        param t31
    322        param t32
    323        call printf, 6
    324        steps = 0
    325        k = 27
    326  L55:  if k int== 1 goto L58
    327        t34 = k int% 2
    328        if t34 int== 0 goto L56
    329        t35 = k int* 3
    330        t33 = t35 int+ 1
    331        goto L57
    332  L56:  t33 = k int/ 2
    333  L57:  k = t33
    334        t38 = steps int+ 1
    335        steps = t38
    336        if t38 int<= 200 goto L55
    337  L58:  countdown = 3
    338  L59:  t39 = countdown
    339        countdown = countdown int- 1
    340        if t39 int<= 0 goto L60
    341        param "%d "
    342        param countdown
    343        call printf, 2
    344        t39 = countdown
    345        countdown = countdown int- 1
    346        if t39 int<= 0 goto L60
    347        param "%d "
    348        param countdown
    349        call printf, 2
    350        goto L59
    351  L60:  param "\n%d\n"
    352        param steps
    353        call printf, 2
    354        return digits


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   classify           function      int (const char *)         -           5    -    5  _Z8classifyPKc; defined
   daysIn             function      int (int, int)             -          31    -    4  _Z6daysInii; defined
   grade              function      const char *(int)          -          39    -    4  _Z5gradei; defined
   firstPair          function      int (int)                  -          43    -    3  _Z9firstPairi; defined
   main               function      int (void)                 -          53    -    0  defined

 scope: global > classify()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     const char *               param       5    4    3  s.1
   state              variable      int                        local       6    4    5  state.2

 scope: global > classify() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      char                       local       8    1    6  c.3
   digit              variable      int                        local       9    4    4  digit.4
   letter             variable      int                        local       9    4    2  letter.5

 scope: global > daysIn()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   month              parameter     int                        param      31    4    1  month.6
   year               parameter     int                        param      31    4    3  year.7

 scope: global > grade()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   score              parameter     int                        param      39    4    3  score.8

 scope: global > firstPair()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   target             parameter     int                        param      43    4    1  target.9
   found              label         -                          -          49    -    1  _Z9firstPairi.found
   i                  variable      int                        local      44    4    6  i.10
   j                  variable      int                        local      44    4    5  j.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   triangle           variable      int                        local      59    4    2  triangle.12
   skipped            variable      int                        local      59    4    2  skipped.13
   n                  variable      int                        local      70    4    4  n.16
   digits             variable      int                        local      70    4    3  digits.17
   value              variable      int                        local      70    4    2  value.18
   a                  variable      int                        local      73    4    6  a.19
   b                  variable      int                        local      73    4    6  b.20
   c                  variable      int                        local      73    4    2  c.21
   steps              variable      int                        local      78    4    2  steps.22
   k                  variable      int                        local      78    4    5  k.23
   countdown          variable      int                        local      84    4    2  countdown.24

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      60    4    6  i.14

 scope: global > main() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      62    4    5  j.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
