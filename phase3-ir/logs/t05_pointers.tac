============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t05_pointers.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 188 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION swap(int *, int *)        (link name _Z4swapPiS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   b                param   int *                           4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16

 Code: 6 instruction(s)

    100     t1 = *a
    101     t = t1
    102     t2 = *b
    103     *a = t2
    104     *b = t
    105     return

============================================================================
 FUNCTION sum(int *, int *)        (link name _Z3sumPiS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   first            param   int *                           4       0
   last             param   int *                           4       4
   s                local   int                             4       8
   t1               temp    int *                           4      12
   t2               temp    int *                           4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24

 Code: 11 instruction(s)

    106       s = 0
    107  L1:  if first ptr< last goto L2
    108       goto L3
    109  L2:  t1 = first
    110       t2 = first ptr+ 4
    111       first = t2
    112       t3 = *t1
    113       t4 = s int+ t3
    114       s = t4
    115       goto L1
    116  L3:  return s

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 17 parameter(s)/local(s), 69 temporaries, frame 396 bytes

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
   t15              temp    int *                           4     168
   t16              temp    int *                           4     172
   t17              temp    int *                           4     176
   t18              temp    int *                           4     180
   t19              temp    int *                           4     184
   t20              temp    int *                           4     188
   t21              temp    int *                           4     192
   t22              temp    int                             4     196
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t25              temp    int *                           4     208
   t26              temp    int *                           4     212
   t27              temp    int *                           4     216
   t28              temp    int                             4     220
   t29              temp    int *                           4     224
   t30              temp    int *                           4     228
   t31              temp    int *                           4     232
   t32              temp    int                             4     236
   t33              temp    int                             4     240
   t34              temp    int                             4     244
   t35              temp    int *                           4     248
   t36              temp    int                             4     252
   t37              temp    int *                           4     256
   t38              temp    int *                           4     260
   t39              temp    int                             4     264
   t40              temp    int                             4     268
   t41              temp    int *                           4     272
   t42              temp    int *                           4     276
   t43              temp    int                             4     280
   t44              temp    int *                           4     284
   t45              temp    int                             4     288
   t46              temp    int *                           4     292
   t47              temp    int *                           4     296
   t48              temp    int *                           4     300
   t49              temp    int *                           4     304
   t50              temp    char                            1     308
   t51              temp    int                             4     312
   t52              temp    int (*)[3]                      4     316
   t53              temp    int (*)[3]                      4     320
   t54              temp    int (*)[3]                      4     324
   t55              temp    int                             4     328
   t56              temp    int                             4     332
   t57              temp    int *                           4     336
   t58              temp    double *                        4     340
   t59              temp    double                          8     344
   t60              temp    double                          8     352
   t61              temp    char *                          4     360
   t62              temp    char                            1     364
   t63              temp    char *                          4     368
   t64              temp    char *                          4     372
   t65              temp    int                             4     376
   t66              temp    char *                          4     380
   t67              temp    char                            1     384
   t68              temp    int                             4     388
   t69              temp    int                             4     392

 Code: 171 instruction(s)

    117        x = 5
    118        y = 6
    119        t1 = &x
    120        p = t1
    121        t2 = &p
    122        pp = t2
    123        t3 = &pp
    124        ppp = t3
    125        t4 = *p
    126        t5 = *pp
    127        t6 = *t5
    128        t7 = *ppp
    129        t8 = *t7
    130        t9 = *t8
    131        param "%d %d %d\n"
    132        param t4
    133        param t6
    134        param t9
    135        call printf, 4
    136        t10 = *pp
    137        *t10 = 9
    138        t11 = *ppp
    139        t12 = *t11
    140        t13 = *t12
    141        t14 = t13 int+ 1
    142        *t12 = t14
    143        t15 = &x
    144        t16 = &y
    145        param t15
    146        param t16
    147        call swap(int *, int *), 2
    148        param "%d %d\n"
    149        param x
    150        param y
    151        call printf, 3
    152        arr[0] = 10
    153        arr[4] = 20
    154        arr[8] = 30
    155        arr[12] = 40
    156        arr[16] = 50
    157        t17 = &arr
    158        t18 = t17 ptr+ 8
    159        q = t18
    160        t19 = q ptr- 4
    161        q = t19
    162        t20 = &arr
    163        t21 = t20 ptr+ 16
    164        t22 = t21 ptr- q
    165        t23 = t22 int/ 4
    166        gap = t23
    167        t24 = *q
    168        t25 = &arr
    169        t26 = &arr
    170        t27 = t26 ptr+ 20
    171        param t25
    172        param t27
    173        t28 = call sum(int *, int *), 2
    174        param "%d %d %d\n"
    175        param t24
    176        param gap
    177        param t28
    178        call printf, 4
    179        t29 = q ptr+ 4
    180        q = t29
    181        t30 = q ptr- 4
    182        q = t30
    183        t31 = q ptr+ 8
    184        q = t31
    185        t32 = *q
    186        t33 = int- 1
    187        t34 = t33 int* 4
    188        t35 = q ptr+ t34
    189        t36 = *t35
    190        t37 = &arr
    191        t38 = t37 ptr+ 16
    192        t39 = *t38
    193        param "%d %d %d\n"
    194        param t32
    195        param t36
    196        param t39
    197        call printf, 4
    198        t41 = &arr
    199        t42 = t41 ptr+ 12
    200        if q ptr== t42 goto L4
    201        t40 = 0
    202        goto L5
    203  L4:   t40 = 1
    204  L5:   t44 = &arr
    205        if q ptr!= t44 goto L6
    206        t43 = 0
    207        goto L7
    208  L6:   t43 = 1
    209  L7:   t46 = &arr
    210        t47 = t46 ptr+ 16
    211        if q ptr< t47 goto L8
    212        t45 = 0
    213        goto L9
    214  L8:   t45 = 1
    215  L9:   param "%d %d %d\n"
    216        param t40
    217        param t43
    218        param t45
    219        call printf, 4
    220        t48 = &x
    221        raw = t48
    222        back = raw
    223        t49 = &y
    224        bytes = t49
    225        *back = 258
    226        t50 = *bytes
    227        t51 = chartoint t50
    228        param "%d %d\n"
    229        param x
    230        param t51
    231        call printf, 3
    232        grid[0] = 1
    233        grid[4] = 2
    234        grid[8] = 3
    235        grid[12] = 4
    236        grid[16] = 5
    237        grid[20] = 6
    238        t52 = &grid
    239        row = t52
    240        t53 = row ptr+ 12
    241        row = t53
    242        t54 = row ptr+ 8
    243        t55 = *t54
    244        t56 = *row
    245        param "%d %d\n"
    246        param t55
    247        param t56
    248        call printf, 3
    249        p = 0
    250        if p ptr!= 0 goto L11
    251        goto L10
    252  L10:  t57 = &y
    253        p = t57
    254  L11:  d = 2.5
    255        t58 = &d
    256        dp = t58
    257        t59 = *dp
    258        t60 = t59 double* 2.0
    259        *dp = t60
    260        text[0] = 112
    261        text[1] = 111
    262        text[2] = 105
    263        text[3] = 110
    264        text[4] = 116
    265        text[5] = 101
    266        text[6] = 114
    267        text[7] = 0
    268        t61 = &text
    269        t = t61
    270  L12:  t62 = *t
    271        if t62 char!= 0 goto L13
    272        goto L14
    273  L13:  t63 = t ptr+ 1
    274        t = t63
    275        goto L12
    276  L14:  t64 = &text
    277        t65 = t ptr- t64
    278        t66 = t ptr- 1
    279        t67 = *t66
    280        t68 = chartoint t67
    281        param "%.1f %d %c\n"
    282        param d
    283        param t65
    284        param t68
    285        call printf, 4
    286        t69 = *p
    287        return t69


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   swap               function      void (int *, int *)        -           4    -    1  _Z4swapPiS_; defined
   sum                function      int (int *, int *)         -          10    -    1  _Z3sumPiS_; defined
   main               function      int (void)                 -          16    -    0  defined

 scope: global > swap()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       4    4    2  a.1
   b                  parameter     int *                      param       4    4    2  b.2
   t                  variable      int                        local       5    4    1  t.3

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   first              parameter     int *                      param      10    4    2  first.4
   last               parameter     int *                      param      10    4    1  last.5
   s                  variable      int                        local      11    4    2  s.6

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      17    4    5  x.7
   y                  variable      int                        local      17    4    4  y.8
   p                  variable      int *                      local      18    4    6  p.9
   pp                 variable      int **                     local      19    4    3  pp.10
   ppp                variable      int ***                    local      20    4    2  ppp.11
   arr                variable      int[5]                     local      27   20    8  arr.12
   q                  variable      int *                      local      28    4   12  q.13
   gap                variable      int                        local      30    4    1  gap.14
   raw                variable      void *                     local      38    4    1  raw.15
   back               variable      int *                      local      39    4    1  back.16
   bytes              variable      char *                     local      40    4    1  bytes.17
   grid               variable      int[2][3]                  local      44   24    1  grid.18
   row                variable      int (*)[3]                 local      45    4    4  row.19
   d                  variable      double                     local      51    8    2  d.20
   dp                 variable      double *                   local      51    4    2  dp.21
   text               variable      char[8]                    local      53    8    2  text.22
   t                  variable      char *                     local      54    4    4  t.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
