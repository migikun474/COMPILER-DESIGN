============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 125 -> 76 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          125 -> 76   (39% fewer)

   constants folded                       14
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded           39
   temporaries merged away                 8
   dead instructions removed              16
   jumps removed or redirected             6
   unreachable instructions removed        4
   propagated across blocks                1
   dead assignments removed               19
   calls inlined                           4
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          1
   unreachable functions removed           2

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  5
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    g = 5
    calls = 0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 26 parameter(s)/local(s), 14 temporaries, frame 264 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   big              local   int                             4       0
   w                local   int                             4       4
   x                local   int                             4       8
   y                local   int                             4      12
   s1               local   int                             4      16
   s2               local   int                             4      20
   s3               local   int                             4      24
   p                local   int *                           4      28
   s4               local   int                             4      32
   h                local   int                             4      36
   s5               local   int                             4      40
   a                local   int[3]                         12      44
   i                local   int                             4      56
   e1               local   int                             4      60
   z                local   int                             4      64
   k                local   int                             4      68
   step             local   int                             4      72
   acc              local   int                             4      76
   same             local   int                             4      80
   all              local   int                             4      84
   some             local   int                             4      88
   cmp              local   int                             4      92
   ignored          local   int                             4      96
   dead             local   int                             4     100
   m                local   int[2]                          8     104
   r                local   int                             4     112
   t7               temp    int                             4     140
   t9               temp    int                             4     148
   t10              temp    int                             4     152
   t11              temp    int *                           4     156
   t12              temp    int                             4     160
   t13              temp    int                             4     164
   t14              temp    int *                           4     168
   t15              temp    int                             4     172
   t17              temp    int                             4     180
   t18              temp    int                             4     184
   t31              temp    int                             4     236
   t32              temp    int                             4     240
   t34              temp    int                             4     248
   t35              temp    int                             4     252
   (23 temporaries no longer used after optimization not shown)

 Code: 76 instruction(s)

    100       param "%d %d %d\n"
    101       param -2
    102       param -1073741824
    103       param 17
    104       call printf, 4
    105       x = 4
    106       y = 6
    107       t7 = x int+ 6
    108       t9 = x int* 6
    109       t10 = t9 int+ 2
    110       t11 = &x
    111       *t11 = 10
    112       t12 = x int+ y
    113       h = g
    114       calls = calls int+ 1
    115       t32 = g int+ 1
    116       g = t32
    117       t13 = t32 int+ h
    118       t14 = &y
    119       t34 = *t14
    120       t35 = t34 int+ 100
    121       *t14 = t35
    122       t15 = x int+ y
    123       param "%d %d %d %d %d %d\n"
    124       param t7
    125       param t7
    126       param t10
    127       param t12
    128       param t13
    129       param t15
    130       call printf, 7
    131       a[0] = 1
    132       a[4] = 2
    133       a[8] = 3
    134       t17 = a[4]
    135       t18 = t17 int<< 1
    136       a[4] = 9
    137       param "%d %d\n"
    138       param t18
    139       param 18
    140       call printf, 3
    141       if calls int== 0 goto L1
    142       z = 1
    143       goto L2
    144  L1:  z = 2
    145  L2:  k = 0
    146       acc = 0
    147  L3:  if k int>= 5 goto L4
    148       acc = acc int+ 3
    149       k = k int+ 1
    150       if k int>= 5 goto L4
    151       acc = acc int+ 3
    152       k = k int+ 1
    153       goto L3
    154  L4:  same = x
    155       some = x int| 4
    156       calls = calls int+ 1
    157       g = g int+ 1
    158       param "%d %d %d %d\n"
    159       param same
    160       param -1
    161       param some
    162       param 3
    163       call printf, 5
    164       calls = calls int+ 1
    165       g = g int+ 1
    166       m[0] = 42
    167       t31 = 42 int+ calls
    168       param "%d %d %d %d %d\n"
    169       param z
    170       param acc
    171       param k
    172       param 8
    173       param t31
    174       call printf, 6
    175       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      7    4    5  
   calls              variable      int                        global      8    4    3  
   touch              function      int (void)                 -           9    -    3  _Z5touchv; defined
   bump               function      void (int &)               -          10    -    1  _Z4bumpRi; defined
   main               function      int (void)                 -          11    -    0  defined

 scope: global > bump()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param      10    4    2  r.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   big                variable      int                        local      12    4    1  big.2
   w                  variable      int                        local      12    4    2  w.3
   x                  variable      int                        local      15    4   14  x.4
   y                  variable      int                        local      15    4    6  y.5
   s1                 variable      int                        local      16    4    1  s1.6
   s2                 variable      int                        local      16    4    1  s2.7
   s3                 variable      int                        local      16    4    1  s3.8
   p                  variable      int *                      local      17    4    1  p.9
   s4                 variable      int                        local      19    4    1  s4.10
   h                  variable      int                        local      20    4    1  h.11
   s5                 variable      int                        local      22    4    1  s5.12
   a                  variable      int[3]                     local      25   12    3  a.13
   i                  variable      int                        local      25    4    2  i.14
   e1                 variable      int                        local      26    4    1  e1.15
   z                  variable      int                        local      29    4    3  z.16
   k                  variable      int                        local      31    4    3  k.17
   step               variable      int                        local      31    4    1  step.18
   acc                variable      int                        local      31    4    2  acc.19
   same               variable      int                        local      33    4    1  same.20
   all                variable      int                        local      33    4    1  all.21
   some               variable      int                        local      33    4    1  some.22
   cmp                variable      int                        local      33    4    3  cmp.23
   ignored            variable      int                        local      36    4    0  ignored.24
   dead               variable      int                        local      38    4    2  dead.25
   m                  variable      int[2]                     local      41    8    2  m.26
   r                  variable      int                        local      43    4    1  r.27

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
