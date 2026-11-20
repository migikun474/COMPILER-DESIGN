============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t05_pointers.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 188 -> 152 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          188 -> 152   (19% fewer)

   constants folded                        3
   algebraic simplifications               0
   common subexpressions                   8
   copies / constants forwarded           43
   temporaries merged away                 5
   dead instructions removed              16
   jumps removed or redirected             3
   unreachable instructions removed        0
   propagated across blocks                4
   dead assignments removed               16
   calls inlined                           2
   tail calls turned into jumps            0
   common subexpressions across blocks      5
   loops unrolled                          3
   unreachable functions removed           2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 17 parameter(s)/local(s), 57 temporaries, frame 432 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   p                local   int *                           4       8
   pp               local   int **                          4      12
   ppp              local   int ***                         4      16
   arr              local   int[5]                         20      20
   q                local   int *                           4      40
   gap              local   int                             4      44
   raw              local   void *                          4      48
   back             local   int *                           4      52
   bytes            local   char *                          4      56
   grid             local   int[2][3]                      24      60
   row              local   int (*)[3]                      4      84
   d                local   double                          8      88
   dp               local   double *                        4      96
   text             local   char[8]                         8     100
   t                local   char *                          4     108
   t1               temp    int *                           4     112
   t2               temp    int **                          4     116
   t3               temp    int ***                         4     120
   t4               temp    int                             4     124
   t5               temp    int *                           4     128
   t6               temp    int                             4     132
   t7               temp    int **                          4     136
   t8               temp    int *                           4     140
   t9               temp    int                             4     144
   t10              temp    int *                           4     148
   t11              temp    int **                          4     152
   t12              temp    int *                           4     156
   t13              temp    int                             4     160
   t14              temp    int                             4     164
   t16              temp    int *                           4     172
   t17              temp    int *                           4     176
   t18              temp    int *                           4     180
   t19              temp    int *                           4     184
   t21              temp    int *                           4     192
   t22              temp    int                             4     196
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t27              temp    int *                           4     216
   t29              temp    int *                           4     224
   t30              temp    int *                           4     228
   t31              temp    int *                           4     232
   t32              temp    int                             4     236
   t35              temp    int *                           4     248
   t36              temp    int                             4     252
   t39              temp    int                             4     264
   t40              temp    int                             4     268
   t42              temp    int *                           4     276
   t43              temp    int                             4     280
   t45              temp    int                             4     288
   t50              temp    char                            1     308
   t51              temp    int                             4     312
   t52              temp    int (*)[3]                      4     316
   t53              temp    int (*)[3]                      4     320
   t54              temp    int (*)[3]                      4     324
   t55              temp    int                             4     328
   t56              temp    int                             4     332
   t58              temp    double *                        4     340
   t59              temp    double                          8     344
   t60              temp    double                          8     352
   t62              temp    char                            1     364
   t64              temp    char *                          4     372
   t65              temp    int                             4     376
   t66              temp    char *                          4     380
   t67              temp    char                            1     384
   t68              temp    int                             4     388
   t69              temp    int                             4     392
   t72              temp    int                             4     404
   t73              temp    int                             4     408
   t74              temp    int *                           4     412
   t76              temp    int                             4     420
   t77              temp    int *                           4     424
   t78              temp    int                             4     428
   (21 temporaries no longer used after optimization not shown)

 Code: 152 instruction(s)

    100        x = 5
    101        y = 6
    102        t1 = &x
    103        p = t1
    104        t2 = &p
    105        pp = t2
    106        t3 = &pp
    107        t4 = *p
    108        t5 = *t2
    109        t6 = *t5
    110        t7 = *t3
    111        t8 = *t7
    112        t9 = *t8
    113        param "%d %d %d\n"
    114        param t4
    115        param t6
    116        param t9
    117        call printf, 4
    118        t10 = *pp
    119        *t10 = 9
    120        t11 = *t3
    121        t12 = *t11
    122        t13 = *t12
    123        t14 = t13 int+ 1
    124        *t12 = t14
    125        t16 = &y
    126        t72 = *t1
    127        t73 = *t16
    128        *t1 = t73
    129        *t16 = t72
    130        param "%d %d\n"
    131        param x
    132        param y
    133        call printf, 3
    134        arr[0] = 10
    135        arr[4] = 20
    136        arr[8] = 30
    137        arr[12] = 40
    138        arr[16] = 50
    139        t17 = &arr
    140        t18 = t17 ptr+ 8
    141        t19 = t18 ptr- 4
    142        t21 = t17 ptr+ 16
    143        t22 = t21 ptr- t19
    144        t23 = t22 int/ 4
    145        t24 = *t19
    146        t27 = t17 ptr+ 20
    147        t74 = t17
    148        t76 = 0
    149  L1:   if t74 ptr>= t27 goto L2
    150        t77 = t74
    151        t74 = t74 ptr+ 4
    152        t78 = *t77
    153        t76 = t76 int+ t78
    154        if t74 ptr>= t27 goto L2
    155        t77 = t74
    156        t74 = t74 ptr+ 4
    157        t78 = *t77
    158        t76 = t76 int+ t78
    159        goto L1
    160  L2:   param "%d %d %d\n"
    161        param t24
    162        param t23
    163        param t76
    164        call printf, 4
    165        t29 = t19 ptr+ 4
    166        t30 = t29 ptr- 4
    167        t31 = t30 ptr+ 8
    168        t32 = *t31
    169        t35 = t31 ptr+ -4
    170        t36 = *t35
    171        t39 = *t21
    172        param "%d %d %d\n"
    173        param t32
    174        param t36
    175        param t39
    176        call printf, 4
    177        t42 = t17 ptr+ 12
    178        if t31 ptr== t42 goto L3
    179        t40 = 0
    180        goto L4
    181  L3:   t40 = 1
    182  L4:   if t31 ptr!= t17 goto L5
    183        t43 = 0
    184        goto L6
    185  L5:   t43 = 1
    186  L6:   if t31 ptr< t21 goto L7
    187        t45 = 0
    188        goto L8
    189  L7:   t45 = 1
    190  L8:   param "%d %d %d\n"
    191        param t40
    192        param t43
    193        param t45
    194        call printf, 4
    195        *t1 = 258
    196        t50 = *t16
    197        t51 = chartoint t50
    198        param "%d %d\n"
    199        param x
    200        param t51
    201        call printf, 3
    202        grid[0] = 1
    203        grid[4] = 2
    204        grid[8] = 3
    205        grid[12] = 4
    206        grid[16] = 5
    207        grid[20] = 6
    208        t52 = &grid
    209        t53 = t52 ptr+ 12
    210        t54 = t53 ptr+ 8
    211        t55 = *t54
    212        t56 = *t53
    213        param "%d %d\n"
    214        param t55
    215        param t56
    216        call printf, 3
    217        p = 0
    218        p = t16
    219        d = 2.5
    220        t58 = &d
    221        t59 = *t58
    222        t60 = t59 double* 2.0
    223        *t58 = t60
    224        text[0] = 112
    225        text[1] = 111
    226        text[2] = 105
    227        text[3] = 110
    228        text[4] = 116
    229        text[5] = 101
    230        text[6] = 114
    231        text[7] = 0
    232        t = &text
    233  L9:   t62 = *t
    234        if t62 char== 0 goto L10
    235        t = t ptr+ 1
    236        t62 = *t
    237        if t62 char== 0 goto L10
    238        t = t ptr+ 1
    239        goto L9
    240  L10:  t64 = &text
    241        t65 = t ptr- t64
    242        t66 = t ptr- 1
    243        t67 = *t66
    244        t68 = chartoint t67
    245        param "%.1f %d %c\n"
    246        param d
    247        param t65
    248        param t68
    249        call printf, 4
    250        t69 = *p
    251        return t69


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   swap               function      void (int *, int *)        -           3    -    1  _Z4swapPiS_; defined
   sum                function      int (int *, int *)         -           9    -    1  _Z3sumPiS_; defined
   main               function      int (void)                 -          15    -    0  defined

 scope: global > swap()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       3    4    2  a.1
   b                  parameter     int *                      param       3    4    2  b.2
   t                  variable      int                        local       4    4    1  t.3

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   first              parameter     int *                      param       9    4    2  first.4
   last               parameter     int *                      param       9    4    1  last.5
   s                  variable      int                        local      10    4    2  s.6

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      16    4    5  x.7
   y                  variable      int                        local      16    4    4  y.8
   p                  variable      int *                      local      17    4    6  p.9
   pp                 variable      int **                     local      18    4    3  pp.10
   ppp                variable      int ***                    local      19    4    2  ppp.11
   arr                variable      int[5]                     local      26   20    8  arr.12
   q                  variable      int *                      local      27    4   12  q.13
   gap                variable      int                        local      29    4    1  gap.14
   raw                variable      void *                     local      37    4    1  raw.15
   back               variable      int *                      local      38    4    1  back.16
   bytes              variable      char *                     local      39    4    1  bytes.17
   grid               variable      int[2][3]                  local      43   24    1  grid.18
   row                variable      int (*)[3]                 local      44    4    4  row.19
   d                  variable      double                     local      50    8    2  d.20
   dp                 variable      double *                   local      50    4    2  dp.21
   text               variable      char[8]                    local      52    8    2  text.22
   t                  variable      char *                     local      53    4    4  t.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
