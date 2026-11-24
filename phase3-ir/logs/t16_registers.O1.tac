============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_registers.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 135 -> 106 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          135 -> 106   (21% fewer)

   calls inlined                           2
   constants folded                       18
   algebraic simplifications               2
   common subexpressions                   1
   copies / constants forwarded           56
   temporaries merged away                 7
   dead instructions removed              25
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

 Code: 85 instruction(s)

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
    143       t43 = *t14
    144       t44 = t43 int<< 1
    145       *t14 = t44
    146       tw = t44
    147       t16 = x int+ 1
    148       t48 = x int* 100
    149       t49 = t44 int* 10
    150       t50 = t48 int+ t49
    151       t51 = t50 int+ t16
    152       r = t51
    153       param "%d\n"
    154       param t51
    155       call printf, 2
    156       c = 120
    157       uc = 250
    158       sh = 32760
    159       i = 0
    160  L2:  if i int>= 10 goto L3
    161       t18 = chartoint c
    162       t19 = t18 int+ 1
    163       c = inttochar t19
    164       t21 = uchartoint uc
    165       t22 = t21 int+ 1
    166       uc = inttouchar t22
    167       t24 = shorttoint sh
    168       t25 = t24 int+ 1
    169       sh = inttoshort t25
    170       i = i int+ 1
    171       goto L2
    172  L3:  t28 = chartoint c
    173       t29 = uchartoint uc
    174       t30 = shorttoint sh
    175       t31 = ushorttouint sh
    176       param "%d %d %d %u\n"
    177       param t28
    178       param t29
    179       param t30
    180       param t31
    181       call printf, 5
    182       d1 = 1.5
    183       d2 = 2.5
    184       d3 = 3.5
    185       d4 = 4.5
    186       d5 = 5.5
    187       d6 = 6.5
    188       d7 = 7.5
    189       dt = 62.75
    190       param "%.2f %.2f\n"
    191       param 62.75
    192       param 9.0
    193       call printf, 3
    194       n = 0
    195       t = 0
    196  L4:  t39 = n int* v2
    197       t = t int+ t39
    198       t41 = n int+ 1
    199       n = t41
    200       if t41 int< 5 goto L4
    201       param "%d %d\n"
    202       param t
    203       param v9
    204       call printf, 3
    205       return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

280 11 30
667
-126 4 -32766 32770
62.75 9.00
20 9

   exit code 0, 274 instructions executed
