============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 158 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION kind(char)        (link name _Z4kindc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   char                            1       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24

 Code: 24 instruction(s)

    100       t1 = chartoint c
    101       if t1 int>= 48 goto L1
    102       goto L3
    103  L1:  t2 = chartoint c
    104       if t2 int<= 57 goto L2
    105       goto L3
    106  L2:  return 1
    107       goto L9
    108  L3:  t3 = chartoint c
    109       if t3 int>= 97 goto L4
    110       goto L5
    111  L4:  t4 = chartoint c
    112       if t4 int<= 122 goto L7
    113       goto L5
    114  L5:  t5 = chartoint c
    115       if t5 int>= 65 goto L6
    116       goto L8
    117  L6:  t6 = chartoint c
    118       if t6 int<= 90 goto L7
    119       goto L8
    120  L7:  return 2
    121       goto L9
    122  L8:  return 0
    123  L9:  return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 28 temporaries, frame 160 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                local   int                             4       0
   i                local   int                             4       4
   k.4              local   int                             4       8
   u                local   int                             4      12
   out              local   int                             4      16
   r                local   int                             4      20
   c                local   int                             4      24
   hit              local   int                             4      28
   text             local   const char *                    4      32
   state            local   int                             4      36
   words            local   int                             4      40
   k.13             local   int                             4      44
   t1               temp    int                             4      48
   t2               temp    int                             4      52
   t3               temp    int                             4      56
   t4               temp    int                             4      60
   t5               temp    int                             4      64
   t6               temp    int                             4      68
   t7               temp    int                             4      72
   t8               temp    int                             4      76
   t9               temp    int                             4      80
   t10              temp    int                             4      84
   t11              temp    int                             4      88
   t12              temp    int                             4      92
   t13              temp    int                             4      96
   t14              temp    int                             4     100
   t15              temp    int                             4     104
   t16              temp    int                             4     108
   t17              temp    int                             4     112
   t18              temp    int                             4     116
   t19              temp    int                             4     120
   t20              temp    int                             4     124
   t21              temp    int                             4     128
   t22              temp    const char *                    4     132
   t23              temp    char                            1     136
   t24              temp    const char *                    4     140
   t25              temp    char                            1     144
   t26              temp    int                             4     148
   t27              temp    int                             4     152
   t28              temp    int                             4     156

 Code: 134 instruction(s)

    124        s = 0
    125        i = 0
    126  L10:  if i int< 5 goto L11
    127        goto L12
    128  L11:  t1 = i
    129        t2 = i int+ 1
    130        i = t2
    131        t3 = s int+ t1
    132        s = t3
    133        goto L10
    134  L12:  t4 = s int* 2
    135        s = t4
    136        if s int< 100 goto L12
    137        goto L13
    138  L13:  k.4 = 0
    139  L14:  if k.4 int< 3 goto L15
    140        goto L16
    141  L15:  t5 = s int- k.4
    142        s = t5
    143        t6 = k.4 int+ 1
    144        k.4 = t6
    145        goto L14
    146  L16:  i = 0
    147  L17:  if i int< 4 goto L18
    148        goto L19
    149  L18:  t7 = i int+ 1
    150        i = t7
    151        goto L17
    152  L19:  u = 0
    153  L20:  if u int>= 4 goto L22
    154        goto L21
    155  L21:  t8 = u int+ 1
    156        u = t8
    157        goto L20
    158  L22:  param "%d %d\n"
    159        param s
    160        param u
    161        call printf, 3
    162        out = 0
    163        i = 0
    164  L23:  if i int< 6 goto L24
    165        goto L32
    166  L24:  t9 = i
    167        goto L29
    168  L25:  t10 = out int+ 1
    169        out = t10
    170  L26:  t11 = out int+ 10
    171        out = t11
    172        goto L30
    173  L27:  t12 = out int+ 100
    174        out = t12
    175  L28:  t13 = out int+ 1000
    176        out = t13
    177        goto L31
    178        goto L30
    179  L29:  if t9 int== 0 goto L25
    180        if t9 int== 1 goto L25
    181        if t9 int== 4 goto L27
    182        if t9 int== 5 goto L28
    183        goto L26
    184  L30:  t14 = out int+ 5
    185        out = t14
    186  L31:  t15 = i int+ 1
    187        i = t15
    188        goto L23
    189  L32:  param "%d\n"
    190        param out
    191        call printf, 2
    192        c = 0
    193        hit = 0
    194        r = 0
    195  L33:  if r int< 4 goto L34
    196        goto L45
    197  L34:  c = 0
    198  L35:  if c int< 4 goto L36
    199        goto L44
    200  L36:  if c int> r goto L37
    201        goto L38
    202  L37:  goto L44
    203  L38:  t16 = r int+ c
    204        t17 = t16 int% 2
    205        if t17 int!= 0 goto L39
    206        goto L40
    207  L39:  goto L43
    208  L40:  t18 = r int* c
    209        if t18 int== 4 goto L41
    210        goto L42
    211  L41:  goto L45
    212  L42:  t19 = hit int+ 1
    213        hit = t19
    214  L43:  t20 = c int+ 1
    215        c = t20
    216        goto L35
    217  L44:  t21 = r int+ 1
    218        r = t21
    219        goto L33
    220  L45:  param "%d %d %d\n"
    221        param hit
    222        param r
    223        param c
    224        call printf, 4
    225        text = "ab 12 x9;"
    226        state = 0
    227        words = 0
    228        i = 0
    229  L46:  t22 = text ptr+ i
    230        t23 = *t22
    231        if t23 char!= 0 goto L47
    232        goto L54
    233  L47:  t24 = text ptr+ i
    234        t25 = *t24
    235        param t25
    236        t26 = call kind(char), 1
    237        k.13 = t26
    238        if state int== 0 goto L48
    239        goto L50
    240  L48:  if k.13 int!= 0 goto L49
    241        goto L50
    242  L49:  t27 = words int+ 1
    243        words = t27
    244        state = 1
    245        goto L53
    246  L50:  if state int== 1 goto L51
    247        goto L53
    248  L51:  if k.13 int!= 0 goto L53
    249        goto L52
    250  L52:  state = 0
    251  L53:  t28 = i int+ 1
    252        i = t28
    253        goto L46
    254  L54:  param "%d\n"
    255        param words
    256        call printf, 2
    257        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               function      int (char)                 -           4    -    1  _Z4kindc; defined
   main               function      int (void)                 -           9    -    0  defined

 scope: global > kind()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     char                       param       4    1    6  c.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   done               label         -                          -          37    -    1  main.done
   s                  variable      int                        local      10    4    5  s.2
   i                  variable      int                        local      10    4   13  i.3
   u                  variable      int                        local      15    4    3  u.5
   out                variable      int                        local      18    4    6  out.6
   r                  variable      int                        local      29    4    7  r.7
   c                  variable      int                        local      29    4    7  c.8
   hit                variable      int                        local      29    4    2  hit.9
   text               variable      const char *               local      39    4    2  text.10
   state              variable      int                        local      40    4    4  state.11
   words              variable      int                        local      40    4    2  words.12

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      13    4    3  k.4

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      42    4    2  k.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
