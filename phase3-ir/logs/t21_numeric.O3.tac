============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t21_numeric.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 213 -> 135 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          213 -> 135   (36% fewer)

   constants folded                       48
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           83
   temporaries merged away                18
   dead instructions removed              57
   jumps removed or redirected            14
   unreachable instructions removed       15
   propagated across blocks                7
   dead assignments removed               17
   calls inlined                          11
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          8
   unreachable functions removed           7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 28 temporaries, frame 804 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   double                          8       0
   e                local   double                          8       8
   f                local   double                          8      16
   g                local   float                           4      24
   i                local   int                             4      28
   u                local   unsigned int                    4      32
   c                local   char                            1      36
   mixed            local   double                          8      40
   narrowed         local   float                           4      48
   total            local   double                          8      56
   step             local   double                          8      64
   fsum             local   float                           4      72
   k                local   int                             4      76
   tiny             local   double                          8      80
   huge             local   double                          8      88
   t8               temp    double                          8     152
   t35              temp    double                          8     352
   t38              temp    float                           4     376
   t39              temp    float                           4     380
   t42              temp    double                          8     392
   t43              temp    float                           4     400
   t44              temp    float                           4     404
   t45              temp    double                          8     408
   t50              temp    double                          8     448
   t51              temp    int                             4     456
   t52              temp    double                          8     464
   t53              temp    double                          8     472
   t55              temp    double                          8     488
   t56              temp    double                          8     496
   t57              temp    int                             4     504
   t58              temp    int                             4     508
   t59              temp    int                             4     512
   t60              temp    double                          8     520
   t61              temp    double                          8     528
   t64              temp    int                             4     552
   t65              temp    double                          8     560
   t66              temp    int                             4     568
   t92              temp    double                          8     752
   t93              temp    int                             4     760
   t94              temp    double                          8     768
   t95              temp    double                          8     776
   t97              temp    double                          8     792
   t98              temp    int                             4     800
   (70 temporaries no longer used after optimization not shown)

 Code: 135 instruction(s)

    100        param "%.3f %.3f %.3f %.4f\n"
    101        param 2.5
    102        param 3.0
    103        param 3.5
    104        param 0.3333333432674408
    105        call printf, 5
    106        t50 = 1.0
    107        t51 = 0
    108  L1:   if t51 int>= 20 goto L2
    109        t52 = 2.0 double/ t50
    110        t53 = t50 double+ t52
    111        t50 = t53 double/ 2.0
    112        t51 = t51 int+ 1
    113        if t51 int>= 20 goto L2
    114        t52 = 2.0 double/ t50
    115        t53 = t50 double+ t52
    116        t50 = t53 double/ 2.0
    117        t51 = t51 int+ 1
    118        goto L1
    119  L2:   t55 = 0.0
    120        t56 = 1.0
    121        t57 = 0
    122  L3:   if t57 int>= 1000 goto L4
    123        t58 = t57 int<< 1
    124        t59 = t58 int+ 1
    125        t60 = inttodouble t59
    126        t61 = t56 double/ t60
    127        t55 = t55 double+ t61
    128        t56 = double- t56
    129        t57 = t57 int+ 1
    130        if t57 int>= 1000 goto L4
    131        t58 = t57 int<< 1
    132        t59 = t58 int+ 1
    133        t60 = inttodouble t59
    134        t61 = t56 double/ t60
    135        t55 = t55 double+ t61
    136        t56 = double- t56
    137        t57 = t57 int+ 1
    138        goto L3
    139  L4:   t8 = 4.0 double* t55
    140        t64 = 6
    141        t65 = 1.0
    142  L5:   t66 = t64
    143        t64 = t64 int- 1
    144        if t66 int<= 0 goto L6
    145        t65 = t65 double* 1.5
    146        t66 = t64
    147        t64 = t64 int- 1
    148        if t66 int<= 0 goto L6
    149        t65 = t65 double* 1.5
    150        goto L5
    151  L6:   param "%.5f %.4f %.2f\n"
    152        param t50
    153        param t8
    154        param t65
    155        call printf, 4
    156        param "%.3f %.2f %.2f\n"
    157        param 2.6666667461395264
    158        param 3.25
    159        param -2.0
    160        call printf, 4
    161        param "%d %d %d %d\n"
    162        param 3
    163        param -3
    164        param 2
    165        param 9
    166        call printf, 5
    167        param "%d %d %d %d\n"
    168        param 0
    169        param 1
    170        param 0
    171        param 1
    172        call printf, 5
    173        param "%.1f %.1f %d\n"
    174        param 4000000071.5
    175        param 16777216.0
    176        param 0
    177        call printf, 4
    178        total = 0.0
    179        step = 0.25
    180  L7:   if step double< 2.0 goto L8
    181        goto L9
    182  L8:   t35 = step double* step
    183        total = total double+ t35
    184        step = step double+ 0.25
    185        goto L7
    186  L9:   param "%.4f\n"
    187        param total
    188        call printf, 2
    189        fsum = 0.0
    190        k = 1
    191  L10:  if k int> 10 goto L11
    192        t38 = inttofloat k
    193        t39 = 1.0 float/ t38
    194        fsum = fsum float+ t39
    195        k = k int+ 1
    196        if k int> 10 goto L11
    197        t38 = inttofloat k
    198        t39 = 1.0 float/ t38
    199        fsum = fsum float+ t39
    200        k = k int+ 1
    201        goto L10
    202  L11:  t42 = floattodouble fsum
    203        t43 = float- fsum
    204        t44 = t43 float* 2.0
    205        t45 = floattodouble t44
    206        param "%.4f %.2f\n"
    207        param t42
    208        param t45
    209        call printf, 3
    210        param "%.6f %.1f %.3f\n"
    211        param 0.001
    212        param 2.5e+06
    213        param 2.5e+03
    214        call printf, 4
    215        t92 = 40.5
    216        t93 = 0
    217  L12:  if t93 int>= 20 goto L13
    218        t94 = 81.0 double/ t92
    219        t95 = t92 double+ t94
    220        t92 = t95 double/ 2.0
    221        t93 = t93 int+ 1
    222        if t93 int>= 20 goto L13
    223        t94 = 81.0 double/ t92
    224        t95 = t92 double+ t94
    225        t92 = t95 double/ 2.0
    226        t93 = t93 int+ 1
    227        goto L12
    228  L13:  if t92 double< 0.0 goto L14
    229        goto L15
    230  L14:  t97 = t92 double- 0.5
    231        goto L16
    232  L15:  t97 = t92 double+ 0.5
    233  L16:  t98 = doubletoint t97
    234        return t98


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   absolute           function      double (double)            -           4    -    1  _Z8absoluted; defined
   root               function      double (double)            -           6    -    2  _Z4rootd; defined
   series             function      double (int)               -          12    -    1  _Z6seriesi; defined
   power              function      double (double, int)       -          18    -    1  _Z5powerdi; defined
   average            function      float (float, float, float) -          19    -    1  _Z7averagefff; defined
   roundToInt         function      int (double)               -          20    -    4  _Z10roundToIntd; defined
   poly               function      double (double)            -          22    -    1  _Z4polyd; defined
   main               function      int (void)                 -          24    -    0  defined

 scope: global > absolute()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param       4    8    3  v.1

 scope: global > root()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param       6    8    2  v.2
   guess              variable      double                     local       7    8    4  guess.3

 scope: global > root() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       8    4    2  i.4

 scope: global > series()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   terms              parameter     int                        param      12    4    1  terms.5
   sum                variable      double                     local      13    8    2  sum.6
   sign               variable      double                     local      13    8    3  sign.7

 scope: global > series() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      14    4    3  i.8

 scope: global > power()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   base               parameter     double                     param      18    8    1  base.9
   n                  parameter     int                        param      18    4    1  n.10
   r                  variable      double                     local      18    8    2  r.11

 scope: global > average()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     float                      param      19    4    1  a.12
   b                  parameter     float                      param      19    4    1  b.13
   c                  parameter     float                      param      19    4    1  c.14

 scope: global > roundToInt()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param      20    8    3  v.15

 scope: global > poly()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     double                     param      22    8    3  x.16

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      double                     local      25    8    2  d.17
   e                  variable      double                     local      25    8    2  e.18
   f                  variable      double                     local      25    8    1  f.19
   g                  variable      float                      local      26    4    2  g.20
   i                  variable      int                        local      33    4    2  i.21
   u                  variable      unsigned int               local      34    4    1  u.22
   c                  variable      char                       local      35    1    1  c.23
   mixed              variable      double                     local      36    8    1  mixed.24
   narrowed           variable      float                      local      37    4    1  narrowed.25
   total              variable      double                     local      40    8    2  total.26
   fsum               variable      float                      local      43    4    3  fsum.28
   tiny               variable      double                     local      46    8    2  tiny.30
   huge               variable      double                     local      46    8    2  huge.31

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   step               variable      double                     local      41    8    4  step.27
   k                  variable      int                        local      44    4    3  k.29

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
