============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t41_loop_edges.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 119 -> 159 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          119 -> 159   (-33% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            3
   temporaries merged away                14
   dead instructions removed               2
   jumps removed or redirected            12
   unreachable instructions removed        3
   propagated across blocks               10
   dead assignments removed                9
   calls inlined                           5
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          9
   unreachable functions removed           1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 20 temporaries, frame 208 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   int                             4       0
   w                local   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   found            local   int                             4      16
   skipped          local   int                             4      20
   k                local   int                             4      24
   total            local   int                             4      28
   s                local   int                             4      32
   t6               temp    int                             4      56
   t10              temp    int                             4      72
   t11              temp    int                             4      76
   t16              temp    int                             4      96
   t18              temp    int                             4     104
   t25              temp    int                             4     132
   t26              temp    int                             4     136
   t27              temp    int                             4     140
   t29              temp    int                             4     148
   t30              temp    int                             4     152
   t31              temp    int                             4     156
   t33              temp    int                             4     164
   t34              temp    int                             4     168
   t35              temp    int                             4     172
   t37              temp    int                             4     180
   t38              temp    int                             4     184
   t39              temp    int                             4     188
   t41              temp    int                             4     196
   t42              temp    int                             4     200
   t43              temp    int                             4     204
   (23 temporaries no longer used after optimization not shown)

 Code: 159 instruction(s)

    100        t25 = 0
    101        t26 = 0
    102  L1:   if t26 int>= 0 goto L2
    103        t27 = t25 int<< 1
    104        t25 = t27 int+ 1
    105        t26 = t26 int+ 1
    106        if t26 int>= 0 goto L2
    107        t27 = t25 int<< 1
    108        t25 = t27 int+ 1
    109        t26 = t26 int+ 1
    110        goto L1
    111  L2:   t29 = 0
    112        t30 = 0
    113  L3:   if t30 int>= 1 goto L4
    114        t31 = t29 int<< 1
    115        t29 = t31 int+ 1
    116        t30 = t30 int+ 1
    117        if t30 int>= 1 goto L4
    118        t31 = t29 int<< 1
    119        t29 = t31 int+ 1
    120        t30 = t30 int+ 1
    121        goto L3
    122  L4:   t33 = 0
    123        t34 = 0
    124  L5:   if t34 int>= 2 goto L6
    125        t35 = t33 int<< 1
    126        t33 = t35 int+ 1
    127        t34 = t34 int+ 1
    128        if t34 int>= 2 goto L6
    129        t35 = t33 int<< 1
    130        t33 = t35 int+ 1
    131        t34 = t34 int+ 1
    132        goto L5
    133  L6:   t37 = 0
    134        t38 = 0
    135  L7:   if t38 int>= 3 goto L8
    136        t39 = t37 int<< 1
    137        t37 = t39 int+ 1
    138        t38 = t38 int+ 1
    139        if t38 int>= 3 goto L8
    140        t39 = t37 int<< 1
    141        t37 = t39 int+ 1
    142        t38 = t38 int+ 1
    143        goto L7
    144  L8:   t41 = 0
    145        t42 = 0
    146  L9:   if t42 int>= 7 goto L10
    147        t43 = t41 int<< 1
    148        t41 = t43 int+ 1
    149        t42 = t42 int+ 1
    150        if t42 int>= 7 goto L10
    151        t43 = t41 int<< 1
    152        t41 = t43 int+ 1
    153        t42 = t42 int+ 1
    154        goto L9
    155  L10:  param "%d %d %d %d %d\n"
    156        param t25
    157        param t29
    158        param t33
    159        param t37
    160        param t41
    161        call printf, 6
    162        d = 0
    163  L11:  t6 = d int+ 1
    164        d = t6
    165        if t6 int< 0 goto L11
    166        w = 10
    167  L12:  if w int>= 10 goto L13
    168        w = w int+ 1
    169        if w int>= 10 goto L13
    170        w = w int+ 1
    171        goto L12
    172  L13:  param "%d %d\n"
    173        param t6
    174        param w
    175        call printf, 3
    176        found = -1
    177        skipped = 0
    178        i = 0
    179  L14:  if i int>= 5 goto L23
    180        if found int>= 0 goto L23
    181        j = 0
    182  L15:  if j int>= 5 goto L18
    183        if j int!= 1 goto L16
    184        skipped = skipped int+ 1
    185        goto L17
    186  L16:  t10 = i int* j
    187        if t10 int!= 6 goto L17
    188        t11 = i int* 10
    189        found = t11 int+ j
    190        goto L18
    191  L17:  j = j int+ 1
    192        goto L15
    193  L18:  i = i int+ 1
    194        if i int>= 5 goto L23
    195        if found int>= 0 goto L23
    196        j = 0
    197  L19:  if j int>= 5 goto L22
    198        if j int!= 1 goto L20
    199        skipped = skipped int+ 1
    200        goto L21
    201  L20:  t10 = i int* j
    202        if t10 int!= 6 goto L21
    203        t11 = i int* 10
    204        found = t11 int+ j
    205        goto L22
    206  L21:  j = j int+ 1
    207        goto L19
    208  L22:  i = i int+ 1
    209        goto L14
    210  L23:  param "%d %d %d\n"
    211        param found
    212        param i
    213        param skipped
    214        call printf, 4
    215        k = 0
    216        total = 0
    217  L24:  total = total int+ k
    218        t16 = k int+ 1
    219        k = t16
    220        if t16 int< 5 goto L24
    221        param "%d\n"
    222        param total
    223        call printf, 2
    224        s = 0
    225        i = 0
    226  L25:  if i int>= 8 goto L38
    227        t18 = i int% 4
    228        goto L29
    229  L26:  s = s int+ 1
    230        goto L30
    231  L27:  s = s int+ 10
    232  L28:  s = s int+ 100
    233        goto L30
    234  L29:  if t18 int== 0 goto L31
    235        if t18 int== 1 goto L26
    236        if t18 int== 2 goto L27
    237        if t18 int== 3 goto L28
    238  L30:  s = s int+ 1000
    239  L31:  i = i int+ 1
    240        if i int>= 8 goto L38
    241        t18 = i int% 4
    242        goto L35
    243  L32:  s = s int+ 1
    244        goto L36
    245  L33:  s = s int+ 10
    246  L34:  s = s int+ 100
    247        goto L36
    248  L35:  if t18 int== 0 goto L37
    249        if t18 int== 1 goto L32
    250        if t18 int== 2 goto L33
    251        if t18 int== 3 goto L34
    252  L36:  s = s int+ 1000
    253  L37:  i = i int+ 1
    254        goto L25
    255  L38:  param "%d\n"
    256        param s
    257        call printf, 2
    258        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   count              function      int (int)                  -           5    -    5  _Z5counti; defined
   main               function      int (void)                 -           6    -    0  defined

 scope: global > count()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       5    4    1  n.1
   c                  variable      int                        local       5    4    3  c.2
   i                  variable      int                        local       5    4    3  i.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   again              label         -                          -          21    -    1  main.again
   d                  variable      int                        local       8    4    3  d.4
   w                  variable      int                        local      10    4    3  w.5
   i                  variable      int                        local      13    4   10  i.6
   j                  variable      int                        local      13    4    6  j.7
   found              variable      int                        local      13    4    3  found.8
   skipped            variable      int                        local      13    4    2  skipped.9
   k                  variable      int                        local      20    4    2  k.10
   total              variable      int                        local      20    4    2  total.11
   s                  variable      int                        local      25    4    5  s.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
