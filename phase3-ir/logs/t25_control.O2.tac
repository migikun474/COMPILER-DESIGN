============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t25_control.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 298 -> 227 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          298 -> 227   (23% fewer)

   constants folded                        1
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            8
   temporaries merged away                14
   dead instructions removed               1
   jumps removed or redirected            50
   unreachable instructions removed       13
   propagated across blocks               20
   dead assignments removed                8

============================================================================
 FUNCTION classify(const char *)        (link name _Z8classifyPKc)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 10 temporaries, frame 64 bytes

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
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t11              temp    int                             4      56
   (2 temporaries no longer used after optimization not shown)

 Code: 46 instruction(s)

    100        state = 0
    101  L1:   t1 = *s
    102        if t1 char== 0 goto L16
    103        t2 = *s
    104        t4 = chartoint t2
    105        if t4 int< 48 goto L2
    106        t5 = chartoint t2
    107        if t5 int<= 57 goto L3
    108  L2:   t3 = 0
    109        goto L4
    110  L3:   t3 = 1
    111  L4:   t7 = chartoint t2
    112        if t7 int< 97 goto L5
    113        t8 = chartoint t2
    114        if t8 int<= 122 goto L6
    115  L5:   t9 = chartoint t2
    116        if t9 int== 95 goto L6
    117        t6 = 0
    118        goto L14
    119  L6:   t6 = 1
    120        goto L14
    121  L7:   if t3 int== 0 goto L8
    122        state = 1
    123        goto L15
    124  L8:   if t6 int== 0 goto L9
    125        state = 3
    126        goto L15
    127  L9:   return 0
    128  L10:  t11 = chartoint t2
    129        if t11 int!= 46 goto L11
    130        state = 2
    131        goto L15
    132  L11:  if t3 int!= 0 goto L15
    133        return 0
    134  L12:  if t3 int!= 0 goto L15
    135        return 0
    136  L13:  if t3 int!= 0 goto L15
    137        if t6 int!= 0 goto L15
    138        return 0
    139  L14:  if state int== 0 goto L7
    140        if state int== 1 goto L10
    141        if state int== 2 goto L12
    142        if state int== 3 goto L13
    143  L15:  s = s ptr+ 1
    144        goto L1
    145  L16:  return state

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

    146        goto L24
    147  L17:  return 30
    148  L18:  t3 = year int% 4
    149        if t3 int!= 0 goto L19
    150        t4 = year int% 100
    151        if t4 int!= 0 goto L20
    152  L19:  t5 = year int% 400
    153        if t5 int!= 0 goto L21
    154  L20:  t2 = 29
    155        goto L22
    156  L21:  t2 = 28
    157  L22:  return t2
    158  L23:  return 31
    159  L24:  if month int== 4 goto L17
    160        if month int== 6 goto L17
    161        if month int== 9 goto L17
    162        if month int== 11 goto L17
    163        if month int== 2 goto L18
    164        goto L23

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

    165        if score int< 90 goto L25
    166        t1 = "A"
    167        goto L30
    168  L25:  if score int< 75 goto L26
    169        t2 = "B"
    170        goto L29
    171  L26:  if score int< 60 goto L27
    172        t3 = "C"
    173        goto L28
    174  L27:  t3 = "F"
    175  L28:  t2 = t3
    176  L29:  t1 = t2
    177  L30:  return t1

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

    178        i = 1
    179  L31:  if i int>= 10 goto L34
    180        j = i
    181  L32:  if j int>= 10 goto L33
    182        t1 = i int* j
    183        if t1 int== target goto L35
    184        j = j int+ 1
    185        goto L32
    186  L33:  i = i int+ 1
    187        goto L31
    188  L34:  return -1
    189  L35:  t5 = i int* 10
    190        t6 = t5 int+ j
    191        return t6

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 29 temporaries, frame 212 bytes

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
   t10              temp    const char *                    4      88
   t11              temp    const char *                    4      92
   t12              temp    const char *                    4      96
   t13              temp    const char *                    4     100
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
   (11 temporaries no longer used after optimization not shown)

 Code: 135 instruction(s)

    192        param "1234"
    193        t1 = call classify(const char *), 1
    194        param "12.5"
    195        t2 = call classify(const char *), 1
    196        param "x_9"
    197        t3 = call classify(const char *), 1
    198        param "9x"
    199        t4 = call classify(const char *), 1
    200        param ""
    201        t5 = call classify(const char *), 1
    202        param "%d %d %d %d %d\n"
    203        param t1
    204        param t2
    205        param t3
    206        param t4
    207        param t5
    208        call printf, 6
    209        param 2
    210        param 2024
    211        t6 = call daysIn(int, int), 2
    212        param 2
    213        param 1900
    214        t7 = call daysIn(int, int), 2
    215        param 2
    216        param 2000
    217        t8 = call daysIn(int, int), 2
    218        param 11
    219        param 2023
    220        t9 = call daysIn(int, int), 2
    221        param "%d %d %d %d\n"
    222        param t6
    223        param t7
    224        param t8
    225        param t9
    226        call printf, 5
    227        param 95
    228        t10 = call grade(int), 1
    229        param 80
    230        t11 = call grade(int), 1
    231        param 60
    232        t12 = call grade(int), 1
    233        param 10
    234        t13 = call grade(int), 1
    235        param "%s %s %s %s\n"
    236        param t10
    237        param t11
    238        param t12
    239        param t13
    240        call printf, 5
    241        param 24
    242        t14 = call firstPair(int), 1
    243        param 49
    244        t15 = call firstPair(int), 1
    245        param 97
    246        t16 = call firstPair(int), 1
    247        param "%d %d %d\n"
    248        param t14
    249        param t15
    250        param t16
    251        call printf, 4
    252        triangle = 0
    253        skipped = 0
    254        i = 1
    255  L36:  if i int> 6 goto L41
    256        if i int!= 4 goto L37
    257        skipped = skipped int+ 1
    258        goto L40
    259  L37:  j = 1
    260  L38:  if j int> 6 goto L40
    261        if j int> i goto L40
    262        t18 = i int+ j
    263        t19 = t18 int% 2
    264        if t19 int!= 0 goto L39
    265        t20 = i int* j
    266        triangle = triangle int+ t20
    267  L39:  j = j int+ 1
    268        goto L38
    269  L40:  i = i int+ 1
    270        goto L36
    271  L41:  param "%d %d\n"
    272        param triangle
    273        param skipped
    274        call printf, 3
    275        n = 0
    276        digits = 0
    277        value = 90210
    278  L42:  digits = digits int+ 1
    279        t25 = value int/ 10
    280        value = t25
    281        if t25 int!= 0 goto L42
    282  L43:  t26 = n int* n
    283        if t26 int> 200 goto L44
    284        n = n int+ 1
    285        goto L43
    286  L44:  a = 0
    287        b = 10
    288  L45:  if a int>= b goto L46
    289        a = a int+ 1
    290        b = b int- 1
    291        goto L45
    292  L46:  t30 = a int+ 1
    293        t31 = b int+ 2
    294        t32 = t30 int+ t31
    295        param "%d %d %d %d %d\n"
    296        param digits
    297        param n
    298        param t30
    299        param t31
    300        param t32
    301        call printf, 6
    302        steps = 0
    303        k = 27
    304  L47:  if k int== 1 goto L50
    305        t34 = k int% 2
    306        if t34 int== 0 goto L48
    307        t35 = k int* 3
    308        t33 = t35 int+ 1
    309        goto L49
    310  L48:  t33 = k int/ 2
    311  L49:  k = t33
    312        t38 = steps int+ 1
    313        steps = t38
    314        if t38 int<= 200 goto L47
    315  L50:  countdown = 3
    316  L51:  t39 = countdown
    317        countdown = countdown int- 1
    318        if t39 int<= 0 goto L52
    319        param "%d "
    320        param countdown
    321        call printf, 2
    322        goto L51
    323  L52:  param "\n%d\n"
    324        param steps
    325        call printf, 2
    326        return digits


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
