============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_registers.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 135 -> 105 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          135 -> 105   (22% fewer)

   constants folded                       18
   algebraic simplifications               2
   common subexpressions                   1
   copies / constants forwarded           47
   temporaries merged away                 7
   dead instructions removed              19
   jumps removed or redirected             4
   unreachable instructions removed        1

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

 Code: 12 instruction(s)

    100       a = n
    101       b = n int<< 1
    102       c = n int* 3
    103       if n int!= 0 goto L1
    104       return 0
    105  L1:  t3 = n int- 1
    106       param t3
    107       t4 = call depth(int), 1
    108       t5 = t4 int+ a
    109       t6 = t5 int+ b
    110       t7 = t6 int+ c
    111       return t7

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

    112     t1 = a int* 100
    113     t2 = b int* 10
    114     t3 = t1 int+ t2
    115     t4 = t3 int+ c
    116     return t4

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

    117     t1 = *x
    118     t2 = t1 int<< 1
    119     *x = t2
    120     return t2

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

 Code: 84 instruction(s)

    121       v1 = 1
    122       v2 = 2
    123       v3 = 3
    124       v4 = 4
    125       v5 = 5
    126       v6 = 6
    127       v7 = 7
    128       v8 = 8
    129       v9 = 9
    130       v10 = 10
    131       param 5
    132       t1 = call depth(int), 1
    133       s = t1
    134       t11 = t1 int+ 190
    135       s = t11
    136       param "%d %d %d\n"
    137       param t11
    138       param 11
    139       param 30
    140       call printf, 4
    141       x = 3
    142       t14 = &x
    143       param t14
    144       t15 = call twice(int &), 1
    145       tw = t15
    146       t16 = x int+ 1
    147       param x
    148       param t15
    149       param t16
    150       t17 = call three(int, int, int), 3
    151       r = t17
    152       param "%d\n"
    153       param t17
    154       call printf, 2
    155       c = 120
    156       uc = 250
    157       sh = 32760
    158       i = 0
    159  L2:  if i int>= 10 goto L3
    160       t18 = chartoint c
    161       t19 = t18 int+ 1
    162       c = inttochar t19
    163       t21 = uchartoint uc
    164       t22 = t21 int+ 1
    165       uc = inttouchar t22
    166       t24 = shorttoint sh
    167       t25 = t24 int+ 1
    168       sh = inttoshort t25
    169       i = i int+ 1
    170       goto L2
    171  L3:  t28 = chartoint c
    172       t29 = uchartoint uc
    173       t30 = shorttoint sh
    174       t31 = ushorttouint sh
    175       param "%d %d %d %u\n"
    176       param t28
    177       param t29
    178       param t30
    179       param t31
    180       call printf, 5
    181       d1 = 1.5
    182       d2 = 2.5
    183       d3 = 3.5
    184       d4 = 4.5
    185       d5 = 5.5
    186       d6 = 6.5
    187       d7 = 7.5
    188       dt = 62.75
    189       param "%.2f %.2f\n"
    190       param 62.75
    191       param 9.0
    192       call printf, 3
    193       n = 0
    194       t = 0
    195  L4:  t39 = n int* v2
    196       t = t int+ t39
    197       t41 = n int+ 1
    198       n = t41
    199       if t41 int< 5 goto L4
    200       param "%d %d\n"
    201       param t
    202       param v9
    203       call printf, 3
    204       return 0


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
