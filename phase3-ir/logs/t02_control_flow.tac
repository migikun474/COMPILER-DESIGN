============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 204 instruction(s)

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

 Symbol table: 18 parameter(s)/local(s), 36 temporaries, frame 216 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                local   int                             4       0
   i                local   int                             4       4
   k.4              local   int                             4       8
   u                local   int                             4      12
   never            local   int                             4      16
   steps            local   int                             4      20
   odd              local   int                             4      24
   cells            local   int                             4      28
   rows             local   int                             4      32
   c.11             local   int                             4      36
   out              local   int                             4      40
   r                local   int                             4      44
   c.14             local   int                             4      48
   hit              local   int                             4      52
   text             local   const char *                    4      56
   state            local   int                             4      60
   words            local   int                             4      64
   k.19             local   int                             4      68
   t1               temp    int                             4      72
   t2               temp    int                             4      76
   t3               temp    int                             4      80
   t4               temp    int                             4      84
   t5               temp    int                             4      88
   t6               temp    int                             4      92
   t7               temp    int                             4      96
   t8               temp    int                             4     100
   t9               temp    int                             4     104
   t10              temp    int                             4     108
   t11              temp    int                             4     112
   t12              temp    int                             4     116
   t13              temp    int                             4     120
   t14              temp    int                             4     124
   t15              temp    int                             4     128
   t16              temp    int                             4     132
   t17              temp    int                             4     136
   t18              temp    int                             4     140
   t19              temp    int                             4     144
   t20              temp    int                             4     148
   t21              temp    int                             4     152
   t22              temp    int                             4     156
   t23              temp    int                             4     160
   t24              temp    int                             4     164
   t25              temp    int                             4     168
   t26              temp    int                             4     172
   t27              temp    int                             4     176
   t28              temp    int                             4     180
   t29              temp    int                             4     184
   t30              temp    const char *                    4     188
   t31              temp    char                            1     192
   t32              temp    const char *                    4     196
   t33              temp    char                            1     200
   t34              temp    int                             4     204
   t35              temp    int                             4     208
   t36              temp    int                             4     212

 Code: 180 instruction(s)

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
    162        never = 0
    163        steps = 0
    164        odd = 0
    165        cells = 0
    166        rows = 0
    167  L23:  goto L24
    168        t9 = never int+ 1
    169        never = t9
    170        goto L23
    171  L24:  if steps int== 10 goto L30
    172        goto L25
    173  L25:  t10 = steps int+ 1
    174        steps = t10
    175        t11 = steps int% 2
    176        if t11 int== 0 goto L26
    177        goto L27
    178  L26:  goto L24
    179  L27:  if steps int> 7 goto L28
    180        goto L29
    181  L28:  goto L30
    182  L29:  t12 = odd int+ steps
    183        odd = t12
    184        goto L24
    185  L30:  if rows int>= 3 goto L36
    186        goto L31
    187  L31:  if cells int> 4 goto L36
    188        goto L32
    189  L32:  c.11 = 0
    190  L33:  t13 = rows int+ 1
    191        if c.11 int== t13 goto L35
    192        goto L34
    193  L34:  t14 = cells int+ 1
    194        cells = t14
    195        t15 = c.11 int+ 1
    196        c.11 = t15
    197        goto L33
    198  L35:  t16 = rows int+ 1
    199        rows = t16
    200        goto L30
    201  L36:  param "%d %d %d %d %d\n"
    202        param never
    203        param steps
    204        param odd
    205        param rows
    206        param cells
    207        call printf, 6
    208        out = 0
    209        i = 0
    210  L37:  if i int< 6 goto L38
    211        goto L46
    212  L38:  t17 = i
    213        goto L43
    214  L39:  t18 = out int+ 1
    215        out = t18
    216  L40:  t19 = out int+ 10
    217        out = t19
    218        goto L44
    219  L41:  t20 = out int+ 100
    220        out = t20
    221  L42:  t21 = out int+ 1000
    222        out = t21
    223        goto L45
    224        goto L44
    225  L43:  if t17 int== 0 goto L39
    226        if t17 int== 1 goto L39
    227        if t17 int== 4 goto L41
    228        if t17 int== 5 goto L42
    229        goto L40
    230  L44:  t22 = out int+ 5
    231        out = t22
    232  L45:  t23 = i int+ 1
    233        i = t23
    234        goto L37
    235  L46:  param "%d\n"
    236        param out
    237        call printf, 2
    238        c.14 = 0
    239        hit = 0
    240        r = 0
    241  L47:  if r int< 4 goto L48
    242        goto L59
    243  L48:  c.14 = 0
    244  L49:  if c.14 int< 4 goto L50
    245        goto L58
    246  L50:  if c.14 int> r goto L51
    247        goto L52
    248  L51:  goto L58
    249  L52:  t24 = r int+ c.14
    250        t25 = t24 int% 2
    251        if t25 int!= 0 goto L53
    252        goto L54
    253  L53:  goto L57
    254  L54:  t26 = r int* c.14
    255        if t26 int== 4 goto L55
    256        goto L56
    257  L55:  goto L59
    258  L56:  t27 = hit int+ 1
    259        hit = t27
    260  L57:  t28 = c.14 int+ 1
    261        c.14 = t28
    262        goto L49
    263  L58:  t29 = r int+ 1
    264        r = t29
    265        goto L47
    266  L59:  param "%d %d %d\n"
    267        param hit
    268        param r
    269        param c.14
    270        call printf, 4
    271        text = "ab 12 x9;"
    272        state = 0
    273        words = 0
    274        i = 0
    275  L60:  t30 = text ptr+ i
    276        t31 = *t30
    277        if t31 char!= 0 goto L61
    278        goto L68
    279  L61:  t32 = text ptr+ i
    280        t33 = *t32
    281        param t33
    282        t34 = call kind(char), 1
    283        k.19 = t34
    284        if state int== 0 goto L62
    285        goto L64
    286  L62:  if k.19 int!= 0 goto L63
    287        goto L64
    288  L63:  t35 = words int+ 1
    289        words = t35
    290        state = 1
    291        goto L67
    292  L64:  if state int== 1 goto L65
    293        goto L67
    294  L65:  if k.19 int!= 0 goto L67
    295        goto L66
    296  L66:  state = 0
    297  L67:  t36 = i int+ 1
    298        i = t36
    299        goto L60
    300  L68:  param "%d\n"
    301        param words
    302        call printf, 2
    303        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               function      int (char)                 -           6    -    1  _Z4kindc; defined
   main               function      int (void)                 -          11    -    0  defined

 scope: global > kind()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     char                       param       6    1    6  c.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   done               label         -                          -          53    -    1  main.done
   s                  variable      int                        local      12    4    5  s.2
   i                  variable      int                        local      12    4   13  i.3
   u                  variable      int                        local      17    4    3  u.5
   never              variable      int                        local      20    4    2  never.6
   steps              variable      int                        local      20    4    6  steps.7
   odd                variable      int                        local      20    4    2  odd.8
   cells              variable      int                        local      20    4    3  cells.9
   rows               variable      int                        local      20    4    4  rows.10
   out                variable      int                        local      34    4    6  out.12
   r                  variable      int                        local      45    4    7  r.13
   c                  variable      int                        local      45    4    7  c.14
   hit                variable      int                        local      45    4    2  hit.15
   text               variable      const char *               local      55    4    2  text.16
   state              variable      int                        local      56    4    4  state.17
   words              variable      int                        local      56    4    2  words.18

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      15    4    3  k.4

 scope: global > main() > until
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        local      29    4    2  c.11

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      58    4    2  k.19

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
