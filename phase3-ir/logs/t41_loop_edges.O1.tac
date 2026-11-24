============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t41_loop_edges.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 119 -> 125 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          119 -> 125   (-5% fewer)

   calls inlined                           5
   constants folded                        1
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            3
   temporaries merged away                14
   dead instructions removed               2
   jumps removed or redirected            12
   unreachable instructions removed        3

============================================================================
 FUNCTION count(int)        (link name _Z5counti)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   c                local   int                             4       4
   i                local   int                             4       8
   t1               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    100       c = 0
    101       i = 0
    102  L1:  if i int>= n goto L2
    103       t1 = c int<< 1
    104       c = t1 int+ 1
    105       i = i int+ 1
    106       goto L1
    107  L2:  return c

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 29 temporaries, frame 208 bytes

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
   t1               temp    int                             4      36
   t2               temp    int                             4      40
   t3               temp    int                             4      44
   t4               temp    int                             4      48
   t6               temp    int                             4      56
   t10              temp    int                             4      72
   t11              temp    int                             4      76
   t16              temp    int                             4      96
   t18              temp    int                             4     104
   t24              temp    int                             4     128
   t25              temp    int                             4     132
   t26              temp    int                             4     136
   t27              temp    int                             4     140
   t28              temp    int                             4     144
   t29              temp    int                             4     148
   t30              temp    int                             4     152
   t31              temp    int                             4     156
   t32              temp    int                             4     160
   t33              temp    int                             4     164
   t34              temp    int                             4     168
   t35              temp    int                             4     172
   t36              temp    int                             4     176
   t37              temp    int                             4     180
   t38              temp    int                             4     184
   t39              temp    int                             4     188
   t40              temp    int                             4     192
   t41              temp    int                             4     196
   t42              temp    int                             4     200
   t43              temp    int                             4     204
   (14 temporaries no longer used after optimization not shown)

 Code: 117 instruction(s)

    108        t24 = 0
    109        t25 = 0
    110        t26 = 0
    111  L3:   if t26 int>= t24 goto L4
    112        t27 = t25 int<< 1
    113        t25 = t27 int+ 1
    114        t26 = t26 int+ 1
    115        goto L3
    116  L4:   t1 = t25
    117        t28 = 1
    118        t29 = 0
    119        t30 = 0
    120  L5:   if t30 int>= t28 goto L6
    121        t31 = t29 int<< 1
    122        t29 = t31 int+ 1
    123        t30 = t30 int+ 1
    124        goto L5
    125  L6:   t2 = t29
    126        t32 = 2
    127        t33 = 0
    128        t34 = 0
    129  L7:   if t34 int>= t32 goto L8
    130        t35 = t33 int<< 1
    131        t33 = t35 int+ 1
    132        t34 = t34 int+ 1
    133        goto L7
    134  L8:   t3 = t33
    135        t36 = 3
    136        t37 = 0
    137        t38 = 0
    138  L9:   if t38 int>= t36 goto L10
    139        t39 = t37 int<< 1
    140        t37 = t39 int+ 1
    141        t38 = t38 int+ 1
    142        goto L9
    143  L10:  t4 = t37
    144        t40 = 7
    145        t41 = 0
    146        t42 = 0
    147  L11:  if t42 int>= t40 goto L12
    148        t43 = t41 int<< 1
    149        t41 = t43 int+ 1
    150        t42 = t42 int+ 1
    151        goto L11
    152  L12:  param "%d %d %d %d %d\n"
    153        param t1
    154        param t2
    155        param t3
    156        param t4
    157        param t41
    158        call printf, 6
    159        d = 0
    160  L13:  t6 = d int+ 1
    161        d = t6
    162        if t6 int< 0 goto L13
    163        w = 10
    164  L14:  if w int>= 10 goto L15
    165        w = w int+ 1
    166        goto L14
    167  L15:  param "%d %d\n"
    168        param d
    169        param w
    170        call printf, 3
    171        found = -1
    172        skipped = 0
    173        i = 0
    174  L16:  if i int>= 5 goto L21
    175        if found int>= 0 goto L21
    176        j = 0
    177  L17:  if j int>= 5 goto L20
    178        if j int!= 1 goto L18
    179        skipped = skipped int+ 1
    180        goto L19
    181  L18:  t10 = i int* j
    182        if t10 int!= 6 goto L19
    183        t11 = i int* 10
    184        found = t11 int+ j
    185        goto L20
    186  L19:  j = j int+ 1
    187        goto L17
    188  L20:  i = i int+ 1
    189        goto L16
    190  L21:  param "%d %d %d\n"
    191        param found
    192        param i
    193        param skipped
    194        call printf, 4
    195        k = 0
    196        total = 0
    197  L22:  total = total int+ k
    198        t16 = k int+ 1
    199        k = t16
    200        if t16 int< 5 goto L22
    201        param "%d\n"
    202        param total
    203        call printf, 2
    204        s = 0
    205        i = 0
    206  L23:  if i int>= 8 goto L30
    207        t18 = i int% 4
    208        goto L27
    209  L24:  s = s int+ 1
    210        goto L28
    211  L25:  s = s int+ 10
    212  L26:  s = s int+ 100
    213        goto L28
    214  L27:  if t18 int== 0 goto L29
    215        if t18 int== 1 goto L24
    216        if t18 int== 2 goto L25
    217        if t18 int== 3 goto L26
    218  L28:  s = s int+ 1000
    219  L29:  i = i int+ 1
    220        goto L23
    221  L30:  param "%d\n"
    222        param s
    223        call printf, 2
    224        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

0 1 3 7 127
1 10
23 3 3
10
6422

   exit code 0, 330 instructions executed
