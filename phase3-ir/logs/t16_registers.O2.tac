============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_registers.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 135 -> 82 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          135 -> 82   (39% fewer)

   constants folded                       18
   algebraic simplifications               3
   common subexpressions                   1
   copies / constants forwarded           47
   temporaries merged away                 7
   dead instructions removed              19
   jumps removed or redirected             4
   unreachable instructions removed        1
   propagated across blocks                3
   dead assignments removed               23

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
 FUNCTION three(int, int, int)        (link name _Z5threeiii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   c                param   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24

 Code: 5 instruction(s)

    111     t1 = a int* 100
    112     t2 = b int* 10
    113     t3 = t1 int+ t2
    114     t4 = t3 int+ c
    115     return t4

============================================================================
 FUNCTION twice(int &)        (link name _Z5twiceRi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int &                           4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    116     t1 = *x
    117     t2 = t1 int<< 1
    118     *x = t2
    119     return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 28 parameter(s)/local(s), 18 temporaries, frame 332 bytes

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
   t15              temp    int                             4     192
   t16              temp    int                             4     196
   t17              temp    int                             4     200
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
   (23 temporaries no longer used after optimization not shown)

 Code: 62 instruction(s)

    120       param 5
    121       t1 = call depth(int), 1
    122       t11 = t1 int+ 190
    123       param "%d %d %d\n"
    124       param t11
    125       param 11
    126       param 30
    127       call printf, 4
    128       x = 3
    129       t14 = &x
    130       param t14
    131       t15 = call twice(int &), 1
    132       t16 = x int+ 1
    133       param x
    134       param t15
    135       param t16
    136       t17 = call three(int, int, int), 3
    137       param "%d\n"
    138       param t17
    139       call printf, 2
    140       c = 120
    141       uc = 250
    142       sh = 32760
    143       i = 0
    144  L2:  if i int>= 10 goto L3
    145       t18 = chartoint c
    146       t19 = t18 int+ 1
    147       c = inttochar t19
    148       t21 = uchartoint uc
    149       t22 = t21 int+ 1
    150       uc = inttouchar t22
    151       t24 = shorttoint sh
    152       t25 = t24 int+ 1
    153       sh = inttoshort t25
    154       i = i int+ 1
    155       goto L2
    156  L3:  t28 = chartoint c
    157       t29 = uchartoint uc
    158       t30 = shorttoint sh
    159       t31 = ushorttouint sh
    160       param "%d %d %d %u\n"
    161       param t28
    162       param t29
    163       param t30
    164       param t31
    165       call printf, 5
    166       param "%.2f %.2f\n"
    167       param 62.75
    168       param 9.0
    169       call printf, 3
    170       n = 0
    171       t = 0
    172  L4:  t39 = n int<< 1
    173       t = t int+ t39
    174       t41 = n int+ 1
    175       n = t41
    176       if t41 int< 5 goto L4
    177       param "%d %d\n"
    178       param t
    179       param 9
    180       call printf, 3
    181       return 0


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
