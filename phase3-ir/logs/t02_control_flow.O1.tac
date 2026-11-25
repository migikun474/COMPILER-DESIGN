============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 204 -> 157 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          204 -> 157   (23% fewer)

   calls inlined                           1
   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            3
   temporaries merged away                23
   dead instructions removed               0
   jumps removed or redirected            36
   unreachable instructions removed       10

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

 Code: 15 instruction(s)

    100       t1 = chartoint c
    101       if t1 int< 48 goto L1
    102       t2 = chartoint c
    103       if t2 int> 57 goto L1
    104       return 1
    105  L1:  t3 = chartoint c
    106       if t3 int< 97 goto L2
    107       t4 = chartoint c
    108       if t4 int<= 122 goto L3
    109  L2:  t5 = chartoint c
    110       if t5 int< 65 goto L4
    111       t6 = chartoint c
    112       if t6 int> 90 goto L4
    113  L3:  return 2
    114  L4:  return 0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 18 parameter(s)/local(s), 20 temporaries, frame 244 bytes

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
   t4               temp    int                             4      84
   t10              temp    int                             4     108
   t11              temp    int                             4     112
   t13              temp    int                             4     120
   t17              temp    int                             4     136
   t24              temp    int                             4     164
   t25              temp    int                             4     168
   t26              temp    int                             4     172
   t30              temp    const char *                    4     188
   t31              temp    char                            1     192
   t32              temp    const char *                    4     196
   t33              temp    char                            1     200
   t37              temp    char                            1     216
   t38              temp    int                             4     220
   t39              temp    int                             4     224
   t40              temp    int                             4     228
   t41              temp    int                             4     232
   t42              temp    int                             4     236
   t43              temp    int                             4     240
   (23 temporaries no longer used after optimization not shown)

 Code: 142 instruction(s)

    115        s = 0
    116        i = 0
    117  L5:   if i int>= 5 goto L6
    118        t1 = i
    119        i = i int+ 1
    120        s = s int+ t1
    121        goto L5
    122  L6:   t4 = s int<< 1
    123        s = t4
    124        if t4 int< 100 goto L6
    125        k.4 = 0
    126  L7:   if k.4 int>= 3 goto L8
    127        s = s int- k.4
    128        k.4 = k.4 int+ 1
    129        goto L7
    130  L8:   i = 0
    131  L9:   if i int>= 4 goto L10
    132        i = i int+ 1
    133        goto L9
    134  L10:  u = 0
    135  L11:  if u int>= 4 goto L12
    136        u = u int+ 1
    137        goto L11
    138  L12:  param "%d %d\n"
    139        param s
    140        param u
    141        call printf, 3
    142        never = 0
    143        steps = 0
    144        odd = 0
    145        cells = 0
    146        rows = 0
    147  L13:  if steps int== 10 goto L14
    148        t10 = steps int+ 1
    149        steps = t10
    150        t11 = t10 int% 2
    151        if t11 int== 0 goto L13
    152        if steps int> 7 goto L14
    153        odd = odd int+ steps
    154        goto L13
    155  L14:  if rows int>= 3 goto L17
    156        if cells int> 4 goto L17
    157        c.11 = 0
    158  L15:  t13 = rows int+ 1
    159        if c.11 int== t13 goto L16
    160        cells = cells int+ 1
    161        c.11 = c.11 int+ 1
    162        goto L15
    163  L16:  rows = rows int+ 1
    164        goto L14
    165  L17:  param "%d %d %d %d %d\n"
    166        param never
    167        param steps
    168        param odd
    169        param rows
    170        param cells
    171        call printf, 6
    172        out = 0
    173        i = 0
    174  L18:  if i int>= 6 goto L26
    175        t17 = i
    176        goto L23
    177  L19:  out = out int+ 1
    178  L20:  out = out int+ 10
    179        goto L24
    180  L21:  out = out int+ 100
    181  L22:  out = out int+ 1000
    182        goto L25
    183  L23:  if t17 int== 0 goto L19
    184        if t17 int== 1 goto L19
    185        if t17 int== 4 goto L21
    186        if t17 int== 5 goto L22
    187        goto L20
    188  L24:  out = out int+ 5
    189  L25:  i = i int+ 1
    190        goto L18
    191  L26:  param "%d\n"
    192        param out
    193        call printf, 2
    194        c.14 = 0
    195        hit = 0
    196        r = 0
    197  L27:  if r int>= 4 goto L31
    198        c.14 = 0
    199  L28:  if c.14 int>= 4 goto L30
    200        if c.14 int> r goto L30
    201        t24 = r int+ c.14
    202        t25 = t24 int% 2
    203        if t25 int!= 0 goto L29
    204        t26 = r int* c.14
    205        if t26 int== 4 goto L31
    206        hit = hit int+ 1
    207  L29:  c.14 = c.14 int+ 1
    208        goto L28
    209  L30:  r = r int+ 1
    210        goto L27
    211  L31:  param "%d %d %d\n"
    212        param hit
    213        param r
    214        param c.14
    215        call printf, 4
    216        text = "ab 12 x9;"
    217        state = 0
    218        words = 0
    219        i = 0
    220  L32:  t30 = text ptr+ i
    221        t31 = *t30
    222        if t31 char== 0 goto L40
    223        t32 = text ptr+ i
    224        t33 = *t32
    225        t37 = t33
    226        t38 = chartoint t33
    227        if t38 int< 48 goto L33
    228        t39 = chartoint t37
    229        if t39 int> 57 goto L33
    230        k.19 = 1
    231        goto L37
    232  L33:  t40 = chartoint t37
    233        if t40 int< 97 goto L34
    234        t41 = chartoint t37
    235        if t41 int<= 122 goto L35
    236  L34:  t42 = chartoint t37
    237        if t42 int< 65 goto L36
    238        t43 = chartoint t37
    239        if t43 int> 90 goto L36
    240  L35:  k.19 = 2
    241        goto L37
    242  L36:  k.19 = 0
    243  L37:  if state int!= 0 goto L38
    244        if k.19 int== 0 goto L38
    245        words = words int+ 1
    246        state = 1
    247        goto L39
    248  L38:  if state int!= 1 goto L39
    249        if k.19 int!= 0 goto L39
    250        state = 0
    251  L39:  i = i int+ 1
    252        goto L32
    253  L40:  param "%d\n"
    254        param words
    255        call printf, 2
    256        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

157 4
0 9 16 3 6
2162
3 2 2
3

   exit code 0, 546 instructions executed
