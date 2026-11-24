============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_registers.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 135 -> 85 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          135 -> 85   (37% fewer)

   constants folded                       18
   algebraic simplifications               3
   common subexpressions                   1
   copies / constants forwarded           54
   temporaries merged away                 7
   dead instructions removed              25
   jumps removed or redirected             4
   unreachable instructions removed        1
   propagated across blocks                3
   dead assignments removed               23
   calls inlined                           2
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          1
   unreachable functions removed           2

============================================================================
 FUNCTION depth(int)        (link name _Z5depthi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   a                local   int                             4       4
   b                local   int                             4       8
   c                local   int                             4      12
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   (2 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    100       b = n int<< 1
    101       c = n int* 3
    102       if n int!= 0 goto L1
    103       return 0
    104  L1:  t3 = n int- 1
    105       param t3
    106       t4 = call depth(int), 1
    107       t5 = t4 int+ n
    108       t6 = t5 int+ b
    109       t7 = t6 int+ c
    110       return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 28 parameter(s)/local(s), 22 temporaries, frame 372 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v1               local   int                             4       0
   v2               local   int                             4       4
   v3               local   int                             4       8
   v4               local   int                             4      12
   v5               local   int                             4      16
   v6               local   int                             4      20
   v7               local   int                             4      24
   v8               local   int                             4      28
   v9               local   int                             4      32
   v10              local   int                             4      36
   s                local   int                             4      40
   x                local   int                             4      44
   tw               local   int                             4      48
   r                local   int                             4      52
   c                local   char                            1      56
   uc               local   unsigned char                   1      57
   sh               local   short                           2      58
   i                local   int                             4      60
   d1               local   double                          8      64
   d2               local   double                          8      72
   d3               local   double                          8      80
   d4               local   double                          8      88
   d5               local   double                          8      96
   d6               local   double                          8     104
   d7               local   double                          8     112
   dt               local   double                          8     120
   n                local   int                             4     128
   t                local   int                             4     132
   t1               temp    int                             4     136
   t11              temp    int                             4     176
   t14              temp    int *                           4     188
   t16              temp    int                             4     196
   t18              temp    int                             4     204
   t19              temp    int                             4     208
   t21              temp    int                             4     216
   t22              temp    int                             4     220
   t24              temp    int                             4     228
   t25              temp    int                             4     232
   t28              temp    int                             4     244
   t29              temp    int                             4     248
   t30              temp    int                             4     252
   t31              temp    unsigned int                    4     256
   t39              temp    int                             4     320
   t41              temp    int                             4     328
   t43              temp    int                             4     336
   t44              temp    int                             4     340
   t48              temp    int                             4     356
   t49              temp    int                             4     360
   t50              temp    int                             4     364
   t51              temp    int                             4     368
   (29 temporaries no longer used after optimization not shown)

 Code: 74 instruction(s)

    111       param 5
    112       t1 = call depth(int), 1
    113       t11 = t1 int+ 190
    114       param "%d %d %d\n"
    115       param t11
    116       param 11
    117       param 30
    118       call printf, 4
    119       x = 3
    120       t14 = &x
    121       t43 = *t14
    122       t44 = t43 int<< 1
    123       *t14 = t44
    124       t16 = x int+ 1
    125       t48 = x int* 100
    126       t49 = t44 int* 10
    127       t50 = t48 int+ t49
    128       t51 = t50 int+ t16
    129       param "%d\n"
    130       param t51
    131       call printf, 2
    132       c = 120
    133       uc = 250
    134       sh = 32760
    135       i = 0
    136  L2:  if i int>= 10 goto L3
    137       t18 = chartoint c
    138       t19 = t18 int+ 1
    139       c = inttochar t19
    140       t21 = uchartoint uc
    141       t22 = t21 int+ 1
    142       uc = inttouchar t22
    143       t24 = shorttoint sh
    144       t25 = t24 int+ 1
    145       sh = inttoshort t25
    146       i = i int+ 1
    147       if i int>= 10 goto L3
    148       t18 = chartoint c
    149       t19 = t18 int+ 1
    150       c = inttochar t19
    151       t21 = uchartoint uc
    152       t22 = t21 int+ 1
    153       uc = inttouchar t22
    154       t24 = shorttoint sh
    155       t25 = t24 int+ 1
    156       sh = inttoshort t25
    157       i = i int+ 1
    158       goto L2
    159  L3:  t28 = chartoint c
    160       t29 = uchartoint uc
    161       t30 = shorttoint sh
    162       t31 = ushorttouint sh
    163       param "%d %d %d %u\n"
    164       param t28
    165       param t29
    166       param t30
    167       param t31
    168       call printf, 5
    169       param "%.2f %.2f\n"
    170       param 62.75
    171       param 9.0
    172       call printf, 3
    173       n = 0
    174       t = 0
    175  L4:  t39 = n int<< 1
    176       t = t int+ t39
    177       t41 = n int+ 1
    178       n = t41
    179       if t41 int< 5 goto L4
    180       param "%d %d\n"
    181       param t
    182       param 9
    183       call printf, 3
    184       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   depth              function      int (int)                  -           5    -    2  _Z5depthi; defined
   three              function      int (int, int, int)        -           6    -    1  _Z5threeiii; defined
   twice              function      int (int &)                -           7    -    1  _Z5twiceRi; defined
   main               function      int (void)                 -           8    -    0  defined

 scope: global > depth()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       5    4    5  n.1
   a                  variable      int                        local       5    4    1  a.2
   b                  variable      int                        local       5    4    1  b.3
   c                  variable      int                        local       5    4    1  c.4

 scope: global > three()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param       6    4    1  a.5
   b                  parameter     int                        param       6    4    1  b.6
   c                  parameter     int                        param       6    4    1  c.7

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int &                      param       7    4    3  x.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   loop               label         -                          -          25    -    1  main.loop
   v1                 variable      int                        local       9    4    2  v1.9
   v2                 variable      int                        local       9    4    2  v2.10
   v3                 variable      int                        local       9    4    1  v3.11
   v4                 variable      int                        local       9    4    1  v4.12
   v5                 variable      int                        local       9    4    2  v5.13
   v6                 variable      int                        local       9    4    2  v6.14
   v7                 variable      int                        local       9    4    1  v7.15
   v8                 variable      int                        local       9    4    1  v8.16
   v9                 variable      int                        local       9    4    2  v9.17
   v10                variable      int                        local       9    4    2  v10.18
   s                  variable      int                        local      10    4    2  s.19
   x                  variable      int                        local      13    4    3  x.20
   tw                 variable      int                        local      14    4    1  tw.21
   r                  variable      int                        local      15    4    1  r.22
   c                  variable      char                       local      17    1    2  c.23
   uc                 variable      unsigned char              local      17    1    2  uc.24
   sh                 variable      short                      local      17    2    3  sh.25
   i                  variable      int                        local      18    4    3  i.26
   d1                 variable      double                     local      21    8    2  d1.27
   d2                 variable      double                     local      21    8    1  d2.28
   d3                 variable      double                     local      21    8    1  d3.29
   d4                 variable      double                     local      21    8    1  d4.30
   d5                 variable      double                     local      21    8    1  d5.31
   d6                 variable      double                     local      21    8    1  d6.32
   d7                 variable      double                     local      21    8    2  d7.33
   dt                 variable      double                     local      22    8    1  dt.34
   n                  variable      int                        local      24    4    2  n.35
   t                  variable      int                        local      24    4    2  t.36

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
