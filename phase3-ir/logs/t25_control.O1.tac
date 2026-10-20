============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t25_control.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 298 -> 235 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          298 -> 235   (21% fewer)

   constants folded                        1
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            8
   temporaries merged away                14
   dead instructions removed               1
   jumps removed or redirected            49
   unreachable instructions removed       13

============================================================================
 FUNCTION classify(const char *)        (link name _Z8classifyPKc)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 11 temporaries, frame 64 bytes

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
   t10              temp    int                             4      52
   t11              temp    int                             4      56
   (1 temporary no longer used after optimization not shown)

 Code: 50 instruction(s)

    100        state = 0
    101  L1:   t1 = *s
    102        if t1 char== 0 goto L17
    103        t2 = *s
    104        c = t2
    105        t4 = chartoint t2
    106        if t4 int< 48 goto L2
    107        t5 = chartoint c
    108        if t5 int<= 57 goto L3
    109  L2:   t3 = 0
    110        goto L4
    111  L3:   t3 = 1
    112  L4:   digit = t3
    113        t7 = chartoint c
    114        if t7 int< 97 goto L5
    115        t8 = chartoint c
    116        if t8 int<= 122 goto L6
    117  L5:   t9 = chartoint c
    118        if t9 int== 95 goto L6
    119        t6 = 0
    120        goto L7
    121  L6:   t6 = 1
    122  L7:   letter = t6
    123        t10 = state
    124        goto L15
    125  L8:   if digit int== 0 goto L9
    126        state = 1
    127        goto L16
    128  L9:   if letter int== 0 goto L10
    129        state = 3
    130        goto L16
    131  L10:  return 0
    132  L11:  t11 = chartoint c
    133        if t11 int!= 46 goto L12
    134        state = 2
    135        goto L16
    136  L12:  if digit int!= 0 goto L16
    137        return 0
    138  L13:  if digit int!= 0 goto L16
    139        return 0
    140  L14:  if digit int!= 0 goto L16
    141        if letter int!= 0 goto L16
    142        return 0
    143  L15:  if t10 int== 0 goto L8
    144        if t10 int== 1 goto L11
    145        if t10 int== 2 goto L13
    146        if t10 int== 3 goto L14
    147  L16:  s = s ptr+ 1
    148        goto L1
    149  L17:  return state

============================================================================
 FUNCTION daysIn(int, int)        (link name _Z6daysInii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   month            param   int                             4       0
   year             param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24

 Code: 20 instruction(s)

    150        t1 = month
    151        goto L25
    152  L18:  return 30
    153  L19:  t3 = year int% 4
    154        if t3 int!= 0 goto L20
    155        t4 = year int% 100
    156        if t4 int!= 0 goto L21
    157  L20:  t5 = year int% 400
    158        if t5 int!= 0 goto L22
    159  L21:  t2 = 29
    160        goto L23
    161  L22:  t2 = 28
    162  L23:  return t2
    163  L24:  return 31
    164  L25:  if t1 int== 4 goto L18
    165        if t1 int== 6 goto L18
    166        if t1 int== 9 goto L18
    167        if t1 int== 11 goto L18
    168        if t1 int== 2 goto L19
    169        goto L24

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

    170        if score int< 90 goto L26
    171        t1 = "A"
    172        goto L31
    173  L26:  if score int< 75 goto L27
    174        t2 = "B"
    175        goto L30
    176  L27:  if score int< 60 goto L28
    177        t3 = "C"
    178        goto L29
    179  L28:  t3 = "F"
    180  L29:  t2 = t3
    181  L30:  t1 = t2
    182  L31:  return t1

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

    183        i = 1
    184  L32:  if i int>= 10 goto L35
    185        j = i
    186  L33:  if j int>= 10 goto L34
    187        t1 = i int* j
    188        if t1 int== target goto L36
    189        j = j int+ 1
    190        goto L33
    191  L34:  i = i int+ 1
    192        goto L32
    193  L35:  return -1
    194  L36:  t5 = i int* 10
    195        t6 = t5 int+ j
    196        return t6

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

 Code: 138 instruction(s)

    197        param "1234"
    198        t1 = call classify(const char *), 1
    199        param "12.5"
    200        t2 = call classify(const char *), 1
    201        param "x_9"
    202        t3 = call classify(const char *), 1
    203        param "9x"
    204        t4 = call classify(const char *), 1
    205        param ""
    206        t5 = call classify(const char *), 1
    207        param "%d %d %d %d %d\n"
    208        param t1
    209        param t2
    210        param t3
    211        param t4
    212        param t5
    213        call printf, 6
    214        param 2
    215        param 2024
    216        t6 = call daysIn(int, int), 2
    217        param 2
    218        param 1900
    219        t7 = call daysIn(int, int), 2
    220        param 2
    221        param 2000
    222        t8 = call daysIn(int, int), 2
    223        param 11
    224        param 2023
    225        t9 = call daysIn(int, int), 2
    226        param "%d %d %d %d\n"
    227        param t6
    228        param t7
    229        param t8
    230        param t9
    231        call printf, 5
    232        param 95
    233        t10 = call grade(int), 1
    234        param 80
    235        t11 = call grade(int), 1
    236        param 60
    237        t12 = call grade(int), 1
    238        param 10
    239        t13 = call grade(int), 1
    240        param "%s %s %s %s\n"
    241        param t10
    242        param t11
    243        param t12
    244        param t13
    245        call printf, 5
    246        param 24
    247        t14 = call firstPair(int), 1
    248        param 49
    249        t15 = call firstPair(int), 1
    250        param 97
    251        t16 = call firstPair(int), 1
    252        param "%d %d %d\n"
    253        param t14
    254        param t15
    255        param t16
    256        call printf, 4
    257        triangle = 0
    258        skipped = 0
    259        i = 1
    260  L37:  if i int> 6 goto L42
    261        if i int!= 4 goto L38
    262        skipped = skipped int+ 1
    263        goto L41
    264  L38:  j = 1
    265  L39:  if j int> 6 goto L41
    266        if j int> i goto L41
    267        t18 = i int+ j
    268        t19 = t18 int% 2
    269        if t19 int!= 0 goto L40
    270        t20 = i int* j
    271        triangle = triangle int+ t20
    272  L40:  j = j int+ 1
    273        goto L39
    274  L41:  i = i int+ 1
    275        goto L37
    276  L42:  param "%d %d\n"
    277        param triangle
    278        param skipped
    279        call printf, 3
    280        n = 0
    281        digits = 0
    282        value = 90210
    283  L43:  digits = digits int+ 1
    284        t25 = value int/ 10
    285        value = t25
    286        if t25 int!= 0 goto L43
    287  L44:  t26 = n int* n
    288        if t26 int> 200 goto L45
    289        n = n int+ 1
    290        goto L44
    291  L45:  a = 0
    292        b = 10
    293  L46:  if a int>= b goto L47
    294        a = a int+ 1
    295        b = b int- 1
    296        goto L46
    297  L47:  t30 = a int+ 1
    298        a = t30
    299        t31 = b int+ 2
    300        b = t31
    301        t32 = t30 int+ t31
    302        c = t32
    303        param "%d %d %d %d %d\n"
    304        param digits
    305        param n
    306        param t30
    307        param t31
    308        param t32
    309        call printf, 6
    310        steps = 0
    311        k = 27
    312  L48:  if k int== 1 goto L51
    313        t34 = k int% 2
    314        if t34 int== 0 goto L49
    315        t35 = k int* 3
    316        t33 = t35 int+ 1
    317        goto L50
    318  L49:  t33 = k int/ 2
    319  L50:  k = t33
    320        t38 = steps int+ 1
    321        steps = t38
    322        if t38 int<= 200 goto L48
    323  L51:  countdown = 3
    324  L52:  t39 = countdown
    325        countdown = countdown int- 1
    326        if t39 int<= 0 goto L53
    327        param "%d "
    328        param countdown
    329        call printf, 2
    330        goto L52
    331  L53:  param "\n%d\n"
    332        param steps
    333        call printf, 2
    334        return digits


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
