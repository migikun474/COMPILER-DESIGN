============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_registers.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 135 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION depth(int)        (link name _Z5depthi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 7 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   a                local   int                             4       4
   b                local   int                             4       8
   c                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40

 Code: 15 instruction(s)

    100       a = n
    101       t1 = n int* 2
    102       b = t1
    103       t2 = n int* 3
    104       c = t2
    105       if n int== 0 goto L1
    106       goto L2
    107  L1:  return 0
    108  L2:  t3 = n int- 1
    109       param t3
    110       t4 = call depth(int), 1
    111       t5 = t4 int+ a
    112       t6 = t5 int+ b
    113       t7 = t6 int+ c
    114       return t7

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

    115     t1 = a int* 100
    116     t2 = b int* 10
    117     t3 = t1 int+ t2
    118     t4 = t3 int+ c
    119     return t4

============================================================================
 FUNCTION twice(int &)        (link name _Z5twiceRi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int &                           4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 5 instruction(s)

    120     t1 = *x
    121     t2 = t1 int* 2
    122     *x = t2
    123     t3 = *x
    124     return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 28 parameter(s)/local(s), 41 temporaries, frame 332 bytes

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
   t2               temp    int                             4     140
   t3               temp    int                             4     144
   t4               temp    int                             4     148
   t5               temp    int                             4     152
   t6               temp    int                             4     156
   t7               temp    int                             4     160
   t8               temp    int                             4     164
   t9               temp    int                             4     168
   t10              temp    int                             4     172
   t11              temp    int                             4     176
   t12              temp    int                             4     180
   t13              temp    int                             4     184
   t14              temp    int *                           4     188
   t15              temp    int                             4     192
   t16              temp    int                             4     196
   t17              temp    int                             4     200
   t18              temp    int                             4     204
   t19              temp    int                             4     208
   t20              temp    char                            1     212
   t21              temp    int                             4     216
   t22              temp    int                             4     220
   t23              temp    unsigned char                   1     224
   t24              temp    int                             4     228
   t25              temp    int                             4     232
   t26              temp    short                           2     236
   t27              temp    int                             4     240
   t28              temp    int                             4     244
   t29              temp    int                             4     248
   t30              temp    int                             4     252
   t31              temp    unsigned int                    4     256
   t32              temp    double                          8     264
   t33              temp    double                          8     272
   t34              temp    double                          8     280
   t35              temp    double                          8     288
   t36              temp    double                          8     296
   t37              temp    double                          8     304
   t38              temp    double                          8     312
   t39              temp    int                             4     320
   t40              temp    int                             4     324
   t41              temp    int                             4     328

 Code: 110 instruction(s)

    125       v1 = 1
    126       v2 = 2
    127       v3 = 3
    128       v4 = 4
    129       v5 = 5
    130       v6 = 6
    131       v7 = 7
    132       v8 = 8
    133       v9 = 9
    134       v10 = 10
    135       param 5
    136       t1 = call depth(int), 1
    137       s = t1
    138       t2 = v1 int* v2
    139       t3 = v3 int* v4
    140       t4 = t2 int+ t3
    141       t5 = v5 int* v6
    142       t6 = t4 int+ t5
    143       t7 = v7 int* v8
    144       t8 = t6 int+ t7
    145       t9 = v9 int* v10
    146       t10 = t8 int+ t9
    147       t11 = s int+ t10
    148       s = t11
    149       t12 = v1 int+ v10
    150       t13 = v5 int* v6
    151       param "%d %d %d\n"
    152       param s
    153       param t12
    154       param t13
    155       call printf, 4
    156       x = 3
    157       t14 = &x
    158       param t14
    159       t15 = call twice(int &), 1
    160       tw = t15
    161       t16 = x int+ 1
    162       param x
    163       param tw
    164       param t16
    165       t17 = call three(int, int, int), 3
    166       r = t17
    167       param "%d\n"
    168       param r
    169       call printf, 2
    170       c = 120
    171       uc = 250
    172       sh = 32760
    173       i = 0
    174  L3:  if i int< 10 goto L4
    175       goto L5
    176  L4:  t18 = chartoint c
    177       t19 = t18 int+ 1
    178       t20 = inttochar t19
    179       c = t20
    180       t21 = uchartoint uc
    181       t22 = t21 int+ 1
    182       t23 = inttouchar t22
    183       uc = t23
    184       t24 = shorttoint sh
    185       t25 = t24 int+ 1
    186       t26 = inttoshort t25
    187       sh = t26
    188       t27 = i int+ 1
    189       i = t27
    190       goto L3
    191  L5:  t28 = chartoint c
    192       t29 = uchartoint uc
    193       t30 = shorttoint sh
    194       t31 = ushorttouint sh
    195       param "%d %d %d %u\n"
    196       param t28
    197       param t29
    198       param t30
    199       param t31
    200       call printf, 5
    201       d1 = 1.5
    202       d2 = 2.5
    203       d3 = 3.5
    204       d4 = 4.5
    205       d5 = 5.5
    206       d6 = 6.5
    207       d7 = 7.5
    208       t32 = d1 double* d2
    209       t33 = d3 double* d4
    210       t34 = t32 double+ t33
    211       t35 = d5 double* d6
    212       t36 = t34 double+ t35
    213       t37 = t36 double+ d7
    214       dt = t37
    215       t38 = d1 double+ d7
    216       param "%.2f %.2f\n"
    217       param dt
    218       param t38
    219       call printf, 3
    220       n = 0
    221       t = 0
    222  L6:  t39 = n int* v2
    223       t40 = t int+ t39
    224       t = t40
    225       t41 = n int+ 1
    226       n = t41
    227       if t41 int< 5 goto L7
    228       goto L8
    229  L7:  goto L6
    230  L8:  param "%d %d\n"
    231       param t
    232       param v9
    233       call printf, 3
    234       return 0


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
