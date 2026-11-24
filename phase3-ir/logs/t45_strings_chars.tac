============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t45_strings_chars.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 173 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION len(const char *)        (link name _Z3lenPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0
   n                local   int                             4       4
   t1               temp    const char *                    4       8
   t2               temp    const char *                    4      12
   t3               temp    char                            1      16
   t4               temp    int                             4      20

 Code: 11 instruction(s)

    100       n = 0
    101  L1:  t1 = s
    102       t2 = s ptr+ 1
    103       s = t2
    104       t3 = *t1
    105       if t3 char!= 0 goto L2
    106       goto L3
    107  L2:  t4 = n int+ 1
    108       n = t4
    109       goto L1
    110  L3:  return n

============================================================================
 FUNCTION copy(char *, const char *)        (link name _Z4copyPcPKc)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                param   char *                          4       0
   s                param   const char *                    4       4
   t1               temp    char *                          4       8
   t2               temp    char *                          4      12
   t3               temp    const char *                    4      16
   t4               temp    const char *                    4      20
   t5               temp    char                            1      24

 Code: 12 instruction(s)

    111  L4:  t1 = d
    112       t2 = d ptr+ 1
    113       d = t2
    114       t3 = s
    115       t4 = s ptr+ 1
    116       s = t4
    117       t5 = *t3
    118       *t1 = t5
    119       if t5 char!= 0 goto L5
    120       goto L6
    121  L5:  goto L4
    122  L6:  return

============================================================================
 FUNCTION cmp(const char *, const char *)        (link name _Z3cmpPKcS0_)
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
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 46 temporaries, frame 248 bytes

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
   t2               temp    char *                          4      72
   t3               temp    int                             4      76
   t4               temp    int                             4      80
   t5               temp    char                            1      84
   t6               temp    int                             4      88
   t7               temp    int                             4      92
   t8               temp    char *                          4      96
   t9               temp    int                             4     100
   t10              temp    int                             4     104
   t11              temp    char                            1     108
   t12              temp    int                             4     112
   t13              temp    int                             4     116
   t14              temp    int                             4     120
   t15              temp    int                             4     124
   t16              temp    int                             4     128
   t17              temp    int                             4     132
   t18              temp    char                            1     136
   t19              temp    char                            1     137
   t20              temp    int                             4     140
   t21              temp    int                             4     144
   t22              temp    int                             4     148
   t23              temp    char                            1     152
   t24              temp    int                             4     156
   t25              temp    char *                          4     160
   t26              temp    int                             4     164
   t27              temp    int                             4     168
   t28              temp    const char *                    4     172
   t29              temp    char                            1     176
   t30              temp    int                             4     180
   t31              temp    const char *                    4     184
   t32              temp    char                            1     188
   t33              temp    int                             4     192
   t34              temp    int                             4     196
   t35              temp    int                             4     200
   t36              temp    int                             4     204
   t37              temp    int                             4     208
   t38              temp    int                             4     212
   t39              temp    int                             4     216
   t40              temp    int                             4     220
   t41              temp    char                            1     224
   t42              temp    int                             4     228
   t43              temp    char *                          4     232
   t44              temp    char *                          4     236
   t45              temp    char                            1     240
   t46              temp    int                             4     244

 Code: 130 instruction(s)

    143        t1 = &buf
    144        param t1
    145        param "Hello\tWorld\n"
    146        call copy(char *, const char *), 2
    147        t2 = &buf
    148        param t2
    149        t3 = call len(const char *), 1
    150        t5 = buf[5]
    151        t6 = chartoint t5
    152        if t6 int== 9 goto L11
    153        t4 = 0
    154        goto L12
    155  L11:  t4 = 1
    156  L12:  t8 = &buf
    157        param t8
    158        t9 = call len(const char *), 1
    159        t10 = t9 int- 1
    160        t11 = buf[t10]
    161        t12 = chartoint t11
    162        if t12 int== 10 goto L13
    163        t7 = 0
    164        goto L14
    165  L13:  t7 = 1
    166  L14:  param "%d %d %d\n"
    167        param t3
    168        param t4
    169        param t7
    170        call printf, 4
    171        param "abc"
    172        param "abd"
    173        t14 = call cmp(const char *, const char *), 2
    174        if t14 int< 0 goto L15
    175        t13 = 0
    176        goto L16
    177  L15:  t13 = 1
    178  L16:  param "abc"
    179        param "abc"
    180        t15 = call cmp(const char *, const char *), 2
    181        param "b"
    182        param "a"
    183        t17 = call cmp(const char *, const char *), 2
    184        if t17 int> 0 goto L17
    185        t16 = 0
    186        goto L18
    187  L17:  t16 = 1
    188  L18:  param "%d %d %d\n"
    189        param t13
    190        param t15
    191        param t16
    192        call printf, 4
    193        up[0] = 109
    194        up[1] = 105
    195        up[2] = 112
    196        up[3] = 115
    197        up[4] = 0
    198        up[5] = 0
    199        up[6] = 0
    200        up[7] = 0
    201        i = 0
    202  L19:  t18 = up[i]
    203        if t18 char!= 0 goto L20
    204        goto L21
    205  L20:  t19 = up[i]
    206        t20 = chartoint t19
    207        t21 = t20 int- 97
    208        t22 = t21 int+ 65
    209        t23 = inttochar t22
    210        up[i] = t23
    211        t24 = i int+ 1
    212        i = t24
    213        goto L19
    214  L21:  t25 = &up
    215        t26 = 97 int+ 1
    216        t27 = 122 int- 25
    217        param "%s %c %c\n"
    218        param t25
    219        param t26
    220        param t27
    221        call printf, 4
    222        digits = "40213"
    223        value = 0
    224        i = 0
    225  L22:  t28 = digits ptr+ i
    226        t29 = *t28
    227        if t29 char!= 0 goto L23
    228        goto L24
    229  L23:  t30 = value int* 10
    230        t31 = digits ptr+ i
    231        t32 = *t31
    232        t33 = chartoint t32
    233        t34 = t33 int- 48
    234        t35 = t30 int+ t34
    235        value = t35
    236        t36 = i int+ 1
    237        i = t36
    238        goto L22
    239  L24:  n = 0
    240        v = value
    241  L25:  if v int> 0 goto L26
    242        goto L27
    243  L26:  t37 = n
    244        t38 = n int+ 1
    245        n = t38
    246        t39 = v int% 10
    247        t40 = 48 int+ t39
    248        t41 = inttochar t40
    249        out[t37] = t41
    250        t42 = v int/ 10
    251        v = t42
    252        goto L25
    253  L27:  out[n] = 0
    254        t43 = &out
    255        param "%d %s\n"
    256        param value
    257        param t43
    258        call printf, 3
    259        param "[%5s] [%-5s] [%.2s] [%c]\n"
    260        param "ab"
    261        param "ab"
    262        param "abcdef"
    263        param 81
    264        call printf, 5
    265        t44 = "quote\"d" ptr+ 5
    266        t45 = *t44
    267        t46 = chartoint t45
    268        param "%d %d\n"
    269        param 92
    270        param t46
    271        call printf, 3
    272        return 0


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
