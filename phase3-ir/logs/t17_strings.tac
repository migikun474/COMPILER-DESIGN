============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t17_strings.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 348 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION length(const char *)        (link name _Z6lengthPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   n                local   int                             4       4
   t1               temp    const char *                    4       8
   t2               temp    char                            1      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20

 Code: 10 instruction(s)

    100       n = 0
    101  L1:  t1 = s ptr+ n
    102       t2 = *t1
    103       t3 = chartoint t2
    104       if t3 int!= 0 goto L2
    105       goto L3
    106  L2:  t4 = n int+ 1
    107       n = t4
    108       goto L1
    109  L3:  return n

============================================================================
 FUNCTION copy(char *, const char *)        (link name _Z4copyPcPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   to               param   char *                          4       0
   from             param   const char *                    4       4
   t1               temp    char *                          4       8
   t2               temp    char *                          4      12
   t3               temp    const char *                    4      16
   t4               temp    const char *                    4      20
   t5               temp    char                            1      24
   t6               temp    int                             4      28

 Code: 13 instruction(s)

    110  L4:  t1 = to
    111       t2 = to ptr+ 1
    112       to = t2
    113       t3 = from
    114       t4 = from ptr+ 1
    115       from = t4
    116       t5 = *t3
    117       *t1 = t5
    118       t6 = chartoint t5
    119       if t6 int!= 0 goto L5
    120       goto L6
    121  L5:  goto L4
    122  L6:  return

============================================================================
 FUNCTION compare(const char *, const char *)        (link name _Z7comparePKcS0_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 12 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   const char *                    4       0
   b                param   const char *                    4       4
   t1               temp    char                            1       8
   t2               temp    char                            1       9
   t3               temp    int                             4      12
   t4               temp    char                            1      16
   t5               temp    int                             4      20
   t6               temp    const char *                    4      24
   t7               temp    const char *                    4      28
   t8               temp    char                            1      32
   t9               temp    int                             4      36
   t10              temp    char                            1      40
   t11              temp    int                             4      44
   t12              temp    int                             4      48

 Code: 20 instruction(s)

    123  L7:   t1 = *a
    124        if t1 char!= 0 goto L8
    125        goto L10
    126  L8:   t2 = *a
    127        t3 = chartoint t2
    128        t4 = *b
    129        t5 = chartoint t4
    130        if t3 int== t5 goto L9
    131        goto L10
    132  L9:   t6 = a ptr+ 1
    133        a = t6
    134        t7 = b ptr+ 1
    135        b = t7
    136        goto L7
    137  L10:  t8 = *a
    138        t9 = chartoint t8
    139        t10 = *b
    140        t11 = chartoint t10
    141        t12 = t9 int- t11
    142        return t12

============================================================================
 FUNCTION reverse(char *)        (link name _Z7reversePc)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 10 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0
   i                local   int                             4       4
   j                local   int                             4       8
   t                local   char                            1      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    char *                          4      24
   t4               temp    char                            1      28
   t5               temp    char *                          4      32
   t6               temp    char *                          4      36
   t7               temp    char                            1      40
   t8               temp    char *                          4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52

 Code: 22 instruction(s)

    143        i = 0
    144        param s
    145        t1 = call length(const char *), 1
    146        t2 = t1 int- 1
    147        j = t2
    148  L11:  if i int< j goto L12
    149        goto L13
    150  L12:  t3 = s ptr+ i
    151        t4 = *t3
    152        t = t4
    153        t5 = s ptr+ i
    154        t6 = s ptr+ j
    155        t7 = *t6
    156        *t5 = t7
    157        t8 = s ptr+ j
    158        *t8 = t
    159        t9 = i int+ 1
    160        i = t9
    161        t10 = j int- 1
    162        j = t10
    163        goto L11
    164  L13:  return

============================================================================
 FUNCTION find(const char *, char)        (link name _Z4findPKcc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   text             param   const char *                    4       0
   c                param   char                            1       4
   i                local   int                             4       8
   t1               temp    const char *                    4      12
   t2               temp    char                            1      16
   t3               temp    const char *                    4      20
   t4               temp    char                            1      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   t7               temp    int                             4      36
   t8               temp    int                             4      40

 Code: 17 instruction(s)

    165        i = 0
    166  L14:  t1 = text ptr+ i
    167        t2 = *t1
    168        if t2 char!= 0 goto L15
    169        goto L18
    170  L15:  t3 = text ptr+ i
    171        t4 = *t3
    172        t5 = chartoint t4
    173        t6 = chartoint c
    174        if t5 int== t6 goto L16
    175        goto L17
    176  L16:  return i
    177  L17:  t7 = i int+ 1
    178        i = t7
    179        goto L14
    180  L18:  t8 = int- 1
    181        return t8

============================================================================
 FUNCTION toNumber(const char *)        (link name _Z8toNumberPKc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 15 temporaries, frame 72 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   sign             local   int                             4       4
   v                local   int                             4       8
   t1               temp    char                            1      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    const char *                    4      24
   t5               temp    char                            1      28
   t6               temp    int                             4      32
   t7               temp    char                            1      36
   t8               temp    int                             4      40
   t9               temp    int                             4      44
   t10              temp    char                            1      48
   t11              temp    int                             4      52
   t12              temp    int                             4      56
   t13              temp    int                             4      60
   t14              temp    const char *                    4      64
   t15              temp    int                             4      68

 Code: 29 instruction(s)

    182        sign = 1
    183        v = 0
    184        t1 = *s
    185        t2 = chartoint t1
    186        if t2 int== 45 goto L19
    187        goto L20
    188  L19:  t3 = int- 1
    189        sign = t3
    190        t4 = s ptr+ 1
    191        s = t4
    192  L20:  t5 = *s
    193        t6 = chartoint t5
    194        if t6 int>= 48 goto L21
    195        goto L23
    196  L21:  t7 = *s
    197        t8 = chartoint t7
    198        if t8 int<= 57 goto L22
    199        goto L23
    200  L22:  t9 = v int* 10
    201        t10 = *s
    202        t11 = chartoint t10
    203        t12 = t11 int- 48
    204        t13 = t9 int+ t12
    205        v = t13
    206        t14 = s ptr+ 1
    207        s = t14
    208        goto L20
    209  L23:  t15 = sign int* v
    210        return t15

============================================================================
 FUNCTION toText(int, char *)        (link name _Z6toTextiPc)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 14 temporaries, frame 84 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   out              param   char *                          4       4
   tmp              local   char[12]                       12       8
   n                local   int                             4      20
   neg              local   int                             4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int                             4      40
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t7               temp    char                            1      52
   t8               temp    int                             4      56
   t9               temp    int                             4      60
   t10              temp    int                             4      64
   t11              temp    char *                          4      68
   t12              temp    char *                          4      72
   t13              temp    int                             4      76
   t14              temp    char                            1      80

 Code: 39 instruction(s)

    211        n = 0
    212        if v int< 0 goto L24
    213        t1 = 0
    214        goto L25
    215  L24:  t1 = 1
    216  L25:  neg = t1
    217        if neg int!= 0 goto L26
    218        goto L27
    219  L26:  t2 = int- v
    220        v = t2
    221  L27:  t3 = n
    222        t4 = n int+ 1
    223        n = t4
    224        t5 = v int% 10
    225        t6 = 48 int+ t5
    226        t7 = inttochar t6
    227        tmp[t3] = t7
    228        t8 = v int/ 10
    229        v = t8
    230        if v int> 0 goto L27
    231        goto L28
    232  L28:  if neg int!= 0 goto L29
    233        goto L30
    234  L29:  t9 = n
    235        t10 = n int+ 1
    236        n = t10
    237        tmp[t9] = 45
    238  L30:  if n int> 0 goto L31
    239        goto L32
    240  L31:  t11 = out
    241        t12 = out ptr+ 1
    242        out = t12
    243        t13 = n int- 1
    244        n = t13
    245        t14 = tmp[t13]
    246        *t11 = t14
    247        goto L30
    248  L32:  *out = 0
    249        return

============================================================================
 FUNCTION isPalindrome(const char *)        (link name _Z12isPalindromePKc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 12 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   i                local   int                             4       4
   j                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24
   t5               temp    const char *                    4      28
   t6               temp    char                            1      32
   t7               temp    int                             4      36
   t8               temp    int                             4      40
   t9               temp    int                             4      44
   t10              temp    const char *                    4      48
   t11              temp    char                            1      52
   t12              temp    int                             4      56

 Code: 24 instruction(s)

    250        i = 0
    251        param s
    252        t1 = call length(const char *), 1
    253        t2 = t1 int- 1
    254        j = t2
    255  L33:  if i int< j goto L34
    256        goto L36
    257  L34:  t3 = i
    258        t4 = i int+ 1
    259        i = t4
    260        t5 = s ptr+ t3
    261        t6 = *t5
    262        t7 = chartoint t6
    263        t8 = j
    264        t9 = j int- 1
    265        j = t9
    266        t10 = s ptr+ t8
    267        t11 = *t10
    268        t12 = chartoint t11
    269        if t7 int!= t12 goto L35
    270        goto L33
    271  L35:  return 0
    272        goto L33
    273  L36:  return 1

============================================================================
 FUNCTION countWords(const char *)        (link name _Z10countWordsPKc)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 7 temporaries, frame 36 bytes

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
   t6               temp    int                             4      28
   t7               temp    const char *                    4      32

 Code: 24 instruction(s)

    274        words = 0
    275        inside = 0
    276  L37:  t1 = *s
    277        if t1 char!= 0 goto L38
    278        goto L44
    279  L38:  t2 = *s
    280        t3 = chartoint t2
    281        if t3 int== 32 goto L40
    282        goto L39
    283  L39:  t4 = *s
    284        t5 = chartoint t4
    285        if t5 int== 9 goto L40
    286        goto L41
    287  L40:  inside = 0
    288        goto L43
    289  L41:  if inside int!= 0 goto L43
    290        goto L42
    291  L42:  inside = 1
    292        t6 = words int+ 1
    293        words = t6
    294  L43:  t7 = s ptr+ 1
    295        s = t7
    296        goto L37
    297  L44:  return words

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 54 temporaries, frame 292 bytes

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
   t2               temp    char *                          4      84
   t3               temp    char *                          4      88
   t4               temp    int                             4      92
   t5               temp    char *                          4      96
   t6               temp    char *                          4     100
   t7               temp    char *                          4     104
   t8               temp    int                             4     108
   t9               temp    char *                          4     112
   t10              temp    int                             4     116
   t11              temp    int                             4     120
   t12              temp    int                             4     124
   t13              temp    int                             4     128
   t14              temp    int                             4     132
   t15              temp    int                             4     136
   t16              temp    int                             4     140
   t17              temp    const char *                    4     144
   t18              temp    int                             4     148
   t19              temp    const char *                    4     152
   t20              temp    int                             4     156
   t21              temp    int                             4     160
   t22              temp    int                             4     164
   t23              temp    const char *                    4     168
   t24              temp    const char *                    4     172
   t25              temp    const char *                    4     176
   t26              temp    char                            1     180
   t27              temp    int                             4     184
   t28              temp    int                             4     188
   t29              temp    char *                          4     192
   t30              temp    char *                          4     196
   t31              temp    char *                          4     200
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
   t48              temp    int                             4     264
   t49              temp    char *                          4     268
   t50              temp    const char *                    4     272
   t51              temp    int                             4     276
   t52              temp    char                            1     280
   t53              temp    int                             4     284
   t54              temp    int                             4     288

 Code: 150 instruction(s)

    298        names[0] = "delta"
    299        names[4] = "alpha"
    300        names[8] = "charlie"
    301        t1 = &buf
    302        param t1
    303        param "compiler"
    304        call copy(char *, const char *), 2
    305        t2 = &buf
    306        t3 = &buf
    307        param t3
    308        t4 = call length(const char *), 1
    309        param "%s %d\n"
    310        param t2
    311        param t4
    312        call printf, 3
    313        t5 = &buf
    314        param t5
    315        call reverse(char *), 1
    316        t6 = &buf
    317        t7 = &buf
    318        param t7
    319        param 112
    320        t8 = call find(const char *, char), 2
    321        t9 = &buf
    322        param t9
    323        param 122
    324        t10 = call find(const char *, char), 2
    325        param "%s %d %d\n"
    326        param t6
    327        param t8
    328        param t10
    329        call printf, 4
    330        param "abc"
    331        param "abd"
    332        t12 = call compare(const char *, const char *), 2
    333        if t12 int< 0 goto L45
    334        t11 = 0
    335        goto L46
    336  L45:  t11 = 1
    337  L46:  param "abc"
    338        param "abc"
    339        t13 = call compare(const char *, const char *), 2
    340        param "b"
    341        param "abc"
    342        t15 = call compare(const char *, const char *), 2
    343        if t15 int> 0 goto L47
    344        t14 = 0
    345        goto L48
    346  L47:  t14 = 1
    347  L48:  param "%d %d %d\n"
    348        param t11
    349        param t13
    350        param t14
    351        call printf, 4
    352        smallest = 0
    353        i.32 = 1
    354  L49:  if i.32 int< 3 goto L50
    355        goto L53
    356  L50:  t16 = i.32 int* 4                   (w = 4)
    357        t17 = names[t16]
    358        t18 = smallest int* 4               (w = 4)
    359        t19 = names[t18]
    360        param t17
    361        param t19
    362        t20 = call compare(const char *, const char *), 2
    363        if t20 int< 0 goto L51
    364        goto L52
    365  L51:  smallest = i.32
    366  L52:  t21 = i.32 int+ 1
    367        i.32 = t21
    368        goto L49
    369  L53:  t22 = smallest int* 4               (w = 4)
    370        t23 = names[t22]
    371        t24 = names[8]
    372        t25 = t24 ptr+ 3
    373        t26 = *t25
    374        t27 = chartoint t26
    375        param "%s %c\n"
    376        param t23
    377        param t27
    378        call printf, 3
    379        t28 = int- 40213
    380        t29 = &num
    381        param t28
    382        param t29
    383        call toText(int, char *), 2
    384        t30 = &num
    385        t31 = &num
    386        param t31
    387        t32 = call toNumber(const char *), 1
    388        t33 = t32 int+ 1
    389        param "77x"
    390        t34 = call toNumber(const char *), 1
    391        param "%s %d %d\n"
    392        param t30
    393        param t33
    394        param t34
    395        call printf, 4
    396        param "level"
    397        t35 = call isPalindrome(const char *), 1
    398        param "lever"
    399        t36 = call isPalindrome(const char *), 1
    400        param "  the quick  brown fox "
    401        t37 = call countWords(const char *), 1
    402        param "%d %d %d\n"
    403        param t35
    404        param t36
    405        param t37
    406        call printf, 4
    407        upper[0] = 109
    408        upper[1] = 105
    409        upper[2] = 120
    410        upper[3] = 101
    411        upper[4] = 100
    412        upper[5] = 0
    413        upper[6] = 0
    414        upper[7] = 0
    415        i.34 = 0
    416  L54:  t38 = upper[i.34]
    417        if t38 char!= 0 goto L55
    418        goto L59
    419  L55:  t39 = upper[i.34]
    420        t40 = chartoint t39
    421        if t40 int>= 97 goto L56
    422        goto L58
    423  L56:  t41 = upper[i.34]
    424        t42 = chartoint t41
    425        if t42 int<= 122 goto L57
    426        goto L58
    427  L57:  t43 = upper[i.34]
    428        t44 = chartoint t43
    429        t45 = t44 int- 97
    430        t46 = t45 int+ 65
    431        t47 = inttochar t46
    432        upper[i.34] = t47
    433  L58:  t48 = i.34 int+ 1
    434        i.34 = t48
    435        goto L54
    436  L59:  t49 = &upper
    437        param "%s %d\n"
    438        param t49
    439        param 8
    440        call printf, 3
    441        t50 = names[4]
    442        param t50
    443        t51 = call length(const char *), 1
    444        t52 = buf[0]
    445        t53 = chartoint t52
    446        t54 = t51 int+ t53
    447        return t54


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
