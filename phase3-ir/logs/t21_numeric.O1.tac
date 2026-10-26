============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t21_numeric.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 213 -> 157 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          213 -> 157   (26% fewer)

   constants folded                       25
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           42
   temporaries merged away                15
   dead instructions removed              25
   jumps removed or redirected             8
   unreachable instructions removed        7

============================================================================
 FUNCTION absolute(double)        (link name _Z8absoluted)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   double                          8       0
   t1               temp    double                          8       8
   (1 temporary no longer used after optimization not shown)

 Code: 6 instruction(s)

    100       if v double< 0.0 goto L1
    101       goto L2
    102  L1:  t1 = double- v
    103       goto L3
    104  L2:  t1 = v
    105  L3:  return t1

============================================================================
 FUNCTION root(double)        (link name _Z4rootd)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   double                          8       0
   guess            local   double                          8       8
   i                local   int                             4      16
   t2               temp    double                          8      32
   t3               temp    double                          8      40
   (3 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    106       guess = v double/ 2.0
    107       i = 0
    108  L4:  if i int>= 20 goto L5
    109       t2 = v double/ guess
    110       t3 = guess double+ t2
    111       guess = t3 double/ 2.0
    112       i = i int+ 1
    113       goto L4
    114  L5:  return guess

============================================================================
 FUNCTION series(int)        (link name _Z6seriesi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   terms            param   int                             4       0
   sum              local   double                          8       8
   sign             local   double                          8      16
   i                local   int                             4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32
   t3               temp    double                          8      40
   t4               temp    double                          8      48
   t8               temp    double                          8      80
   (3 temporaries no longer used after optimization not shown)

 Code: 14 instruction(s)

    115       sum = 0.0
    116       sign = 1.0
    117       i = 0
    118  L6:  if i int>= terms goto L7
    119       t1 = i int<< 1
    120       t2 = t1 int+ 1
    121       t3 = inttodouble t2
    122       t4 = sign double/ t3
    123       sum = sum double+ t4
    124       sign = double- sign
    125       i = i int+ 1
    126       goto L6
    127  L7:  t8 = 4.0 double* sum
    128       return t8

============================================================================
 FUNCTION power(double, int)        (link name _Z5powerdi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   base             param   double                          8       0
   n                param   int                             4       8
   r                local   double                          8      16
   t1               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    129       r = 1.0
    130  L8:  t1 = n
    131       n = n int- 1
    132       if t1 int<= 0 goto L9
    133       r = r double* base
    134       goto L8
    135  L9:  return r

============================================================================
 FUNCTION average(float, float, float)        (link name _Z7averagefff)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   float                           4       0
   b                param   float                           4       4
   c                param   float                           4       8
   t1               temp    float                           4      12
   t2               temp    float                           4      16
   t3               temp    float                           4      20

 Code: 4 instruction(s)

    136     t1 = a float+ b
    137     t2 = t1 float+ c
    138     t3 = t2 float/ 3.0
    139     return t3

============================================================================
 FUNCTION roundToInt(double)        (link name _Z10roundToIntd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   double                          8       0
   t1               temp    double                          8       8
   t4               temp    int                             4      32
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    140        if v double< 0.0 goto L10
    141        goto L11
    142  L10:  t1 = v double- 0.5
    143        goto L12
    144  L11:  t1 = v double+ 0.5
    145  L12:  t4 = doubletoint t1
    146        return t4

============================================================================
 FUNCTION poly(double)        (link name _Z4polyd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   double                          8       0
   t1               temp    double                          8       8
   t2               temp    double                          8      16
   t3               temp    double                          8      24
   t4               temp    double                          8      32
   t5               temp    double                          8      40
   t6               temp    double                          8      48

 Code: 7 instruction(s)

    147     t1 = 2.0 double* x
    148     t2 = t1 double- 3.0
    149     t3 = t2 double* x
    150     t4 = t3 double+ 0.5
    151     t5 = t4 double* x
    152     t6 = t5 double- 7.0
    153     return t6

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 19 temporaries, frame 436 bytes

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
   t7               temp    double                          8     144
   t8               temp    double                          8     152
   t9               temp    double                          8     160
   t10              temp    float                           4     168
   t11              temp    double                          8     176
   t13              temp    double                          8     192
   t14              temp    double                          8     200
   t15              temp    int                             4     208
   t17              temp    int                             4     224
   t18              temp    int                             4     228
   t35              temp    double                          8     352
   t38              temp    float                           4     376
   t39              temp    float                           4     380
   t42              temp    double                          8     392
   t43              temp    float                           4     400
   t44              temp    float                           4     404
   t45              temp    double                          8     408
   t47              temp    double                          8     424
   t48              temp    int                             4     432
   (29 temporaries no longer used after optimization not shown)

 Code: 103 instruction(s)

    154        d = 2.5
    155        e = 3.0
    156        f = 3.5
    157        g = 0.33333334
    158        param "%.3f %.3f %.3f %.4f\n"
    159        param 2.5
    160        param 3.0
    161        param 3.5
    162        param 0.3333333432674408
    163        call printf, 5
    164        param 2.0
    165        t7 = call root(double), 1
    166        param 1000
    167        t8 = call series(int), 1
    168        param 1.5
    169        param 6
    170        t9 = call power(double, int), 2
    171        param "%.5f %.4f %.2f\n"
    172        param t7
    173        param t8
    174        param t9
    175        call printf, 4
    176        param 1.5
    177        param 2.5
    178        param 4.0
    179        t10 = call average(float, float, float), 3
    180        t11 = floattodouble t10
    181        param -3.25
    182        t13 = call absolute(double), 1
    183        param 2.0
    184        t14 = call poly(double), 1
    185        param "%.3f %.2f %.2f\n"
    186        param t11
    187        param t13
    188        param t14
    189        call printf, 4
    190        param 2.5
    191        t15 = call roundToInt(double), 1
    192        param -2.5
    193        t17 = call roundToInt(double), 1
    194        param 2.4
    195        t18 = call roundToInt(double), 1
    196        param "%d %d %d %d\n"
    197        param t15
    198        param t17
    199        param t18
    200        param 9
    201        call printf, 5
    202        param "%d %d %d %d\n"
    203        param 0
    204        param 1
    205        param 0
    206        param 1
    207        call printf, 5
    208        i = 7
    209        u = 4000000000
    210        c = 65
    211        mixed = 4000000071.5
    212        narrowed = 16777216.0
    213        param "%.1f %.1f %d\n"
    214        param 4000000071.5
    215        param 16777216.0
    216        param 0
    217        call printf, 4
    218        total = 0.0
    219        step = 0.25
    220  L13:  if step double< 2.0 goto L14
    221        goto L15
    222  L14:  t35 = step double* step
    223        total = total double+ t35
    224        step = step double+ 0.25
    225        goto L13
    226  L15:  param "%.4f\n"
    227        param total
    228        call printf, 2
    229        fsum = 0.0
    230        k = 1
    231  L16:  if k int> 10 goto L17
    232        t38 = inttofloat k
    233        t39 = 1.0 float/ t38
    234        fsum = fsum float+ t39
    235        k = k int+ 1
    236        goto L16
    237  L17:  t42 = floattodouble fsum
    238        t43 = float- fsum
    239        t44 = t43 float* 2.0
    240        t45 = floattodouble t44
    241        param "%.4f %.2f\n"
    242        param t42
    243        param t45
    244        call printf, 3
    245        tiny = 0.001
    246        huge = 2.5e+06
    247        param "%.6f %.1f %.3f\n"
    248        param 0.001
    249        param 2.5e+06
    250        param 2.5e+03
    251        call printf, 4
    252        param 81.0
    253        t47 = call root(double), 1
    254        param t47
    255        t48 = call roundToInt(double), 1
    256        return t48


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   absolute           function      double (double)            -           5    -    1  _Z8absoluted; defined
   root               function      double (double)            -           7    -    2  _Z4rootd; defined
   series             function      double (int)               -          13    -    1  _Z6seriesi; defined
   power              function      double (double, int)       -          19    -    1  _Z5powerdi; defined
   average            function      float (float, float, float) -          20    -    1  _Z7averagefff; defined
   roundToInt         function      int (double)               -          21    -    4  _Z10roundToIntd; defined
   poly               function      double (double)            -          23    -    1  _Z4polyd; defined
   main               function      int (void)                 -          25    -    0  defined

 scope: global > absolute()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param       5    8    3  v.1

 scope: global > root()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param       7    8    2  v.2
   guess              variable      double                     local       8    8    4  guess.3

 scope: global > root() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       9    4    2  i.4

 scope: global > series()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   terms              parameter     int                        param      13    4    1  terms.5
   sum                variable      double                     local      14    8    2  sum.6
   sign               variable      double                     local      14    8    3  sign.7

 scope: global > series() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      15    4    3  i.8

 scope: global > power()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   base               parameter     double                     param      19    8    1  base.9
   n                  parameter     int                        param      19    4    1  n.10
   r                  variable      double                     local      19    8    2  r.11

 scope: global > average()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     float                      param      20    4    1  a.12
   b                  parameter     float                      param      20    4    1  b.13
   c                  parameter     float                      param      20    4    1  c.14

 scope: global > roundToInt()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double                     param      21    8    3  v.15

 scope: global > poly()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     double                     param      23    8    3  x.16

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      double                     local      26    8    2  d.17
   e                  variable      double                     local      26    8    2  e.18
   f                  variable      double                     local      26    8    1  f.19
   g                  variable      float                      local      27    4    2  g.20
   i                  variable      int                        local      34    4    2  i.21
   u                  variable      unsigned int               local      35    4    1  u.22
   c                  variable      char                       local      36    1    1  c.23
   mixed              variable      double                     local      37    8    1  mixed.24
   narrowed           variable      float                      local      38    4    1  narrowed.25
   total              variable      double                     local      41    8    2  total.26
   fsum               variable      float                      local      44    4    3  fsum.28
   tiny               variable      double                     local      47    8    2  tiny.30
   huge               variable      double                     local      47    8    2  huge.31

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   step               variable      double                     local      42    8    4  step.27
   k                  variable      int                        local      45    4    3  k.29

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
