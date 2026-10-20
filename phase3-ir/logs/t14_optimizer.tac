============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 248 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  1

============================================================================
 FUNCTION bump()        (link name _Z4bumpv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    100     t1 = g int+ 10
    101     g = t1
    102     return g

============================================================================
 FUNCTION set(int *, int)        (link name _Z3setPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int *                           4       0
   v                param   int                             4       4

 Code: 2 instruction(s)

    103     *p = v
    104     return

============================================================================
 FUNCTION twice(int &)        (link name _Z5twiceRi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   int &                           4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    105     t1 = *r
    106     t2 = t1 int* 2
    107     *r = t2
    108     return

============================================================================
 FUNCTION fold()        (link name _Z4foldv)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 21 temporaries, frame 128 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   double                          8      16
   u                local   unsigned int                    4      24
   ch               local   char                            1      28
   t1               temp    int                             4      32
   t2               temp    int                             4      36
   t3               temp    int                             4      40
   t4               temp    int                             4      44
   t5               temp    int                             4      48
   t6               temp    int                             4      52
   t7               temp    double                          8      56
   t8               temp    double                          8      64
   t9               temp    double                          8      72
   t10              temp    unsigned int                    4      80
   t11              temp    int                             4      84
   t12              temp    char                            1      88
   t13              temp    int                             4      92
   t14              temp    int                             4      96
   t15              temp    int                             4     100
   t16              temp    int                             4     104
   t17              temp    int                             4     108
   t18              temp    unsigned int                    4     112
   t19              temp    int                             4     116
   t20              temp    int                             4     120
   t21              temp    int                             4     124

 Code: 35 instruction(s)

    109       t1 = 4 int* 2
    110       t2 = 3 int+ t1
    111       a = t2
    112       t3 = a int<< 1
    113       t4 = t3 int- 6
    114       b = t4
    115       t5 = b int/ 4
    116       t6 = t5 int% 3
    117       c = t6
    118       t7 = 1.5 double* 2.0
    119       t8 = inttodouble a
    120       t9 = t7 double+ t8
    121       d = t9
    122       t10 = 4000000000 uint+ 500000000
    123       u = t10
    124       t11 = 97 int+ 300
    125       t12 = inttochar t11
    126       ch = t12
    127       goto L1
    128       a = 99
    129  L1:  goto L2
    130  L2:  t13 = b int+ 1
    131       b = t13
    132  L3:  goto L4
    133       c = 99
    134       goto L3
    135  L4:  t14 = a int+ b
    136       t15 = t14 int+ c
    137       t16 = doubletoint d
    138       t17 = t15 int+ t16
    139       t18 = u uint% 1000
    140       t19 = t17 int+ t18
    141       t20 = chartoint ch
    142       t21 = t19 int+ t20
    143       return t21

============================================================================
 FUNCTION common(int, int)        (link name _Z6commonii)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 23 temporaries, frame 124 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   y                param   int                             4       4
   a                local   int                             4       8
   b                local   int                             4      12
   c                local   int                             4      16
   d                local   int                             4      20
   e                local   int                             4      24
   f                local   int                             4      28
   t1               temp    int                             4      32
   t2               temp    int                             4      36
   t3               temp    int                             4      40
   t4               temp    int                             4      44
   t5               temp    int                             4      48
   t6               temp    int                             4      52
   t7               temp    int                             4      56
   t8               temp    int                             4      60
   t9               temp    int                             4      64
   t10              temp    int                             4      68
   t11              temp    int                             4      72
   t12              temp    int                             4      76
   t13              temp    int                             4      80
   t14              temp    int                             4      84
   t15              temp    int                             4      88
   t16              temp    int                             4      92
   t17              temp    int                             4      96
   t18              temp    int                             4     100
   t19              temp    int                             4     104
   t20              temp    int                             4     108
   t21              temp    int                             4     112
   t22              temp    int                             4     116
   t23              temp    int                             4     120

 Code: 31 instruction(s)

    144     t1 = x int* y
    145     t2 = t1 int+ 3
    146     a = t2
    147     t3 = x int* y
    148     t4 = t3 int+ 3
    149     b = t4
    150     t5 = x int+ y
    151     t6 = x int+ y
    152     t7 = t5 int* t6
    153     c = t7
    154     t8 = y int+ x
    155     d = t8
    156     t9 = x int* 8
    157     t10 = y int* 1
    158     t11 = t9 int+ t10
    159     t12 = t11 int+ 0
    160     t13 = x int/ 1
    161     t14 = t12 int+ t13
    162     t15 = t14 int- 0
    163     e = t15
    164     t16 = x int+ 1
    165     x = t16
    166     t17 = x int* y
    167     t18 = t17 int+ 3
    168     f = t18
    169     t19 = a int+ b
    170     t20 = t19 int+ c
    171     t21 = t20 int+ d
    172     t22 = t21 int+ e
    173     t23 = t22 int+ f
    174     return t23

============================================================================
 FUNCTION aliasing()        (link name _Z8aliasingv)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 33 temporaries, frame 192 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   p                local   int *                           4       8
   a                local   int                             4      12
   b                local   int                             4      16
   c                local   int                             4      20
   r                local   int &                           4      24
   d                local   int                             4      28
   arr              local   int[3]                         12      32
   i                local   int                             4      44
   e                local   int                             4      48
   f                local   int                             4      52
   q                local   int *                           4      56
   t1               temp    int *                           4      60
   t2               temp    int                             4      64
   t3               temp    int                             4      68
   t4               temp    int *                           4      72
   t5               temp    int                             4      76
   t6               temp    int *                           4      80
   t7               temp    int                             4      84
   t8               temp    int                             4      88
   t9               temp    int                             4      92
   t10              temp    int *                           4      96
   t11              temp    int                             4     100
   t12              temp    int                             4     104
   t13              temp    int                             4     108
   t14              temp    int                             4     112
   t15              temp    int                             4     116
   t16              temp    int                             4     120
   t17              temp    int                             4     124
   t18              temp    int                             4     128
   t19              temp    int                             4     132
   t20              temp    int                             4     136
   t21              temp    int (*)[3]                      4     140
   t22              temp    int *                           4     144
   t23              temp    int                             4     148
   t24              temp    int                             4     152
   t25              temp    int                             4     156
   t26              temp    int                             4     160
   t27              temp    int                             4     164
   t28              temp    int                             4     168
   t29              temp    int                             4     172
   t30              temp    int                             4     176
   t31              temp    int                             4     180
   t32              temp    int                             4     184
   t33              temp    int                             4     188

 Code: 58 instruction(s)

    175     x = 5
    176     y = 7
    177     t1 = &x
    178     p = t1
    179     t2 = x int+ y
    180     a = t2
    181     *p = 20
    182     t3 = x int+ y
    183     b = t3
    184     t4 = &y
    185     param t4
    186     param 1
    187     call set(int *, int), 2
    188     t5 = x int+ y
    189     c = t5
    190     t6 = &x
    191     r = t6
    192     t7 = *r
    193     t8 = t7 int+ 1
    194     *r = t8
    195     t9 = x int+ y
    196     d = t9
    197     t10 = &x
    198     param t10
    199     call twice(int &), 1
    200     arr[0] = 1
    201     arr[4] = 2
    202     arr[8] = 3
    203     i = 1
    204     t11 = i int* 4                      (w = 4)
    205     t12 = arr[t11]
    206     t13 = i int* 4                      (w = 4)
    207     t14 = arr[t13]
    208     t15 = t12 int+ t14
    209     e = t15
    210     t16 = i int* 4                      (w = 4)
    211     arr[t16] = 9
    212     t17 = i int* 4                      (w = 4)
    213     t18 = arr[t17]
    214     t19 = arr[4]
    215     t20 = t18 int+ t19
    216     f = t20
    217     t21 = &arr
    218     q = t21
    219     t22 = q ptr+ 8
    220     *t22 = 4
    221     t23 = b int* 2
    222     t24 = a int+ t23
    223     t25 = c int* 3
    224     t26 = t24 int+ t25
    225     t27 = d int* 5
    226     t28 = t26 int+ t27
    227     t29 = t28 int+ e
    228     t30 = t29 int+ f
    229     t31 = t30 int+ x
    230     t32 = arr[8]
    231     t33 = t31 int+ t32
    232     return t33

============================================================================
 FUNCTION globals()        (link name _Z7globalsv)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 11 temporaries, frame 68 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   v                local   int                             4      16
   e                local   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   t10              temp    int                             4      60
   t11              temp    int                             4      64

 Code: 20 instruction(s)

    233     t1 = g int+ 1
    234     a = t1
    235     t2 = g int+ 1
    236     b = t2
    237     call bump(), 0
    238     t3 = g int+ 1
    239     c = t3
    240     g = 2
    241     t4 = g int+ 1
    242     d = t4
    243     v = 3
    244     t5 = v int+ v
    245     e = t5
    246     t6 = a int+ b
    247     t7 = t6 int+ c
    248     t8 = t7 int+ d
    249     t9 = t8 int+ e
    250     t10 = call bump(), 0
    251     t11 = t9 int+ t10
    252     return t11

============================================================================
 FUNCTION flow(int)        (link name _Z4flowi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 9 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   k                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48

 Code: 36 instruction(s)

    253        s = 0
    254        i = 0
    255  L5:   if i int< n goto L6
    256        goto L12
    257  L6:   t1 = n int* 2
    258        k = t1
    259        t2 = i int% 2
    260        if t2 int== 0 goto L7
    261        goto L8
    262  L7:   t3 = s int+ k
    263        s = t3
    264        goto L9
    265  L8:   t4 = s int- 1
    266        s = t4
    267  L9:   if s int> 1000 goto L10
    268        goto L11
    269  L10:  t5 = int- 1
    270        return t5
    271  L11:  t6 = i int+ 1
    272        i = t6
    273        goto L5
    274  L12:  t7 = n
    275        goto L16
    276  L13:  t8 = s int+ 1
    277        s = t8
    278  L14:  t9 = s int+ 2
    279        s = t9
    280        goto L17
    281  L15:  s = 0
    282        goto L17
    283  L16:  if t7 int== 3 goto L13
    284        if t7 int== 4 goto L14
    285        goto L15
    286  L17:  return s
    287        s = 12345
    288        return s

============================================================================
 FUNCTION divide(int, int)        (link name _Z6divideii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 7 instruction(s)

    289        if b int== 0 goto L18
    290        goto L19
    291  L18:  t1 = 0
    292        goto L20
    293  L19:  t2 = a int/ b
    294        t1 = t2
    295  L20:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 12 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   total            local   int                             4       0
   zero             local   int                             4       4
   x                local   double                          8       8
   y                local   double                          8      16
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   t10              temp    double                          8      64
   t11              temp    double                          8      72
   t12              temp    double                          8      80

 Code: 52 instruction(s)

    296     t1 = call fold(), 0
    297     param "%d\n"
    298     param t1
    299     call printf, 2
    300     param 3
    301     param 4
    302     t2 = call common(int, int), 2
    303     param "%d\n"
    304     param t2
    305     call printf, 2
    306     t3 = call aliasing(), 0
    307     param "%d\n"
    308     param t3
    309     call printf, 2
    310     t4 = call globals(), 0
    311     total = t4
    312     param "%d %d\n"
    313     param total
    314     param g
    315     call printf, 3
    316     param 3
    317     t5 = call flow(int), 1
    318     param 4
    319     t6 = call flow(int), 1
    320     param 5
    321     t7 = call flow(int), 1
    322     param "%d %d %d\n"
    323     param t5
    324     param t6
    325     param t7
    326     call printf, 4
    327     zero = 0
    328     param 1
    329     param zero
    330     t8 = call divide(int, int), 2
    331     param 9
    332     param 3
    333     t9 = call divide(int, int), 2
    334     param "%d %d\n"
    335     param t8
    336     param t9
    337     call printf, 3
    338     x = 0.0
    339     t10 = double- x
    340     y = t10
    341     t11 = y double+ 0.0
    342     t12 = x double* 1.0
    343     param "%.1f %.1f\n"
    344     param t11
    345     param t12
    346     call printf, 3
    347     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      6    4    9  
   bump               function      int (void)                 -           7    -    2  _Z4bumpv; defined
   set                function      void (int *, int)          -           8    -    1  _Z3setPii; defined
   twice              function      void (int &)               -           9    -    1  _Z5twiceRi; defined
   fold               function      int (void)                 -          11    -    1  _Z4foldv; defined
   common             function      int (int, int)             -          22    -    1  _Z6commonii; defined
   aliasing           function      int (void)                 -          31    -    1  _Z8aliasingv; defined
   globals            function      int (void)                 -          53    -    1  _Z7globalsv; defined
   flow               function      int (int)                  -          65    -    3  _Z4flowi; defined
   divide             function      int (int, int)             -          82    -    2  _Z6divideii; defined
   main               function      int (void)                 -          84    -    0  defined

 scope: global > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *                      param       8    4    1  p.1
   v                  parameter     int                        param       8    4    1  v.2

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param       9    4    2  r.3

 scope: global > fold()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      12    4    4  a.4
   b                  variable      int                        local      12    4    4  b.5
   c                  variable      int                        local      12    4    2  c.6
   d                  variable      double                     local      13    8    1  d.7
   u                  variable      unsigned int               local      14    4    1  u.8
   ch                 variable      char                       local      15    1    1  ch.9

 scope: global > common()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      22    4   10  x.10
   y                  parameter     int                        param      22    4    7  y.11
   a                  variable      int                        local      23    4    1  a.12
   b                  variable      int                        local      23    4    1  b.13
   c                  variable      int                        local      24    4    1  c.14
   d                  variable      int                        local      24    4    1  d.15
   e                  variable      int                        local      25    4    1  e.16
   f                  variable      int                        local      27    4    1  f.17

 scope: global > aliasing()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      32    4    8  x.18
   y                  variable      int                        local      32    4    5  y.19
   p                  variable      int *                      local      33    4    1  p.20
   a                  variable      int                        local      34    4    1  a.21
   b                  variable      int                        local      36    4    1  b.22
   c                  variable      int                        local      38    4    1  c.23
   r                  variable      int &                      local      39    4    2  r.24
   d                  variable      int                        local      41    4    1  d.25
   arr                variable      int[3]                     local      43   12    7  arr.26
   i                  variable      int                        local      44    4    4  i.27
   e                  variable      int                        local      45    4    1  e.28
   f                  variable      int                        local      47    4    1  f.29
   q                  variable      int *                      local      48    4    1  q.30

 scope: global > globals()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      54    4    1  a.31
   b                  variable      int                        local      55    4    1  b.32
   c                  variable      int                        local      57    4    1  c.33
   d                  variable      int                        local      59    4    1  d.34
   v                  variable      int                        local      60    4    2  v.35
   e                  variable      int                        local      61    4    1  e.36

 scope: global > flow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      65    4    3  n.37
   s                  variable      int                        local      66    4    9  s.38

 scope: global > flow() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      67    4    3  i.39

 scope: global > flow() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      68    4    1  k.40

 scope: global > divide()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      82    4    1  a.41
   b                  parameter     int                        param      82    4    2  b.42

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      88    4    1  total.43
   zero               variable      int                        local      91    4    1  zero.44
   x                  variable      double                     local      93    8    2  x.45
   y                  variable      double                     local      93    8    1  y.46

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
