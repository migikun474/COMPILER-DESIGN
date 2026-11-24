============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t45_strings_chars.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 173 -> 151 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          173 -> 151   (12% fewer)

   constants folded                        2
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded            3
   temporaries merged away                11
   dead instructions removed               3
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

 Symbol table: 8 parameter(s)/local(s), 38 temporaries, frame 248 bytes

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
   (8 temporaries no longer used after optimization not shown)

 Code: 119 instruction(s)

    132        t1 = &buf
    133        param t1
    134        param "Hello\tWorld\n"
    135        call copy(char *, const char *), 2
    136        param t1
    137        t3 = call len(const char *), 1
    138        t5 = buf[5]
    139        t6 = chartoint t5
    140        if t6 int== 9 goto L6
    141        t4 = 0
    142        goto L7
    143  L6:   t4 = 1
    144  L7:   t8 = &buf
    145        param t8
    146        t9 = call len(const char *), 1
    147        t10 = t9 int- 1
    148        t11 = buf[t10]
    149        t12 = chartoint t11
    150        if t12 int== 10 goto L8
    151        t7 = 0
    152        goto L9
    153  L8:   t7 = 1
    154  L9:   param "%d %d %d\n"
    155        param t3
    156        param t4
    157        param t7
    158        call printf, 4
    159        param "abc"
    160        param "abd"
    161        t14 = call cmp(const char *, const char *), 2
    162        if t14 int< 0 goto L10
    163        t13 = 0
    164        goto L11
    165  L10:  t13 = 1
    166  L11:  param "abc"
    167        param "abc"
    168        t15 = call cmp(const char *, const char *), 2
    169        param "b"
    170        param "a"
    171        t17 = call cmp(const char *, const char *), 2
    172        if t17 int> 0 goto L12
    173        t16 = 0
    174        goto L13
    175  L12:  t16 = 1
    176  L13:  param "%d %d %d\n"
    177        param t13
    178        param t15
    179        param t16
    180        call printf, 4
    181        up[0] = 109
    182        up[1] = 105
    183        up[2] = 112
    184        up[3] = 115
    185        up[4] = 0
    186        up[5] = 0
    187        up[6] = 0
    188        up[7] = 0
    189        i = 0
    190  L14:  t18 = up[i]
    191        if t18 char== 0 goto L15
    192        t19 = up[i]
    193        t20 = chartoint t19
    194        t21 = t20 int- 97
    195        t22 = t21 int+ 65
    196        t23 = inttochar t22
    197        up[i] = t23
    198        i = i int+ 1
    199        goto L14
    200  L15:  t25 = &up
    201        param "%s %c %c\n"
    202        param t25
    203        param 98
    204        param 97
    205        call printf, 4
    206        digits = "40213"
    207        value = 0
    208        i = 0
    209  L16:  t28 = digits ptr+ i
    210        t29 = *t28
    211        if t29 char== 0 goto L17
    212        t30 = value int* 10
    213        t31 = digits ptr+ i
    214        t32 = *t31
    215        t33 = chartoint t32
    216        t34 = t33 int- 48
    217        value = t30 int+ t34
    218        i = i int+ 1
    219        goto L16
    220  L17:  n = 0
    221        v = value
    222  L18:  if v int<= 0 goto L19
    223        t37 = n
    224        n = n int+ 1
    225        t39 = v int% 10
    226        t40 = 48 int+ t39
    227        t41 = inttochar t40
    228        out[t37] = t41
    229        v = v int/ 10
    230        goto L18
    231  L19:  out[n] = 0
    232        t43 = &out
    233        param "%d %s\n"
    234        param value
    235        param t43
    236        call printf, 3
    237        param "[%5s] [%-5s] [%.2s] [%c]\n"
    238        param "ab"
    239        param "ab"
    240        param "abcdef"
    241        param 81
    242        call printf, 5
    243        t44 = "quote\"d" ptr+ 5
    244        t45 = *t44
    245        t46 = chartoint t45
    246        param "%d %d\n"
    247        param 92
    248        param t46
    249        call printf, 3
    250        return 0


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
