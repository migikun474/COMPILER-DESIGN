============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 125 -> 101 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          125 -> 101   (19% fewer)

   calls inlined                           4
   constants folded                       14
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded           39
   temporaries merged away                 7
   dead instructions removed              16
   jumps removed or redirected             6
   unreachable instructions removed        4

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
 FUNCTION touch()        (link name _Z5touchv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t2               temp    int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    100     calls = calls int+ 1
    101     t2 = g int+ 1
    102     g = t2
    103     return t2

============================================================================
 FUNCTION bump(int &)        (link name _Z4bumpRi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   int &                           4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    104     t1 = *r
    105     t2 = t1 int+ 100
    106     *r = t2
    107     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 26 parameter(s)/local(s), 15 temporaries, frame 264 bytes

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
   t36              temp    int                             4     256
   (22 temporaries no longer used after optimization not shown)

 Code: 93 instruction(s)

    108       big = 2147483647
    109       w = 2147483647
    110       param "%d %d %d\n"
    111       param -2
    112       param -1073741824
    113       param 17
    114       call printf, 4
    115       x = 4
    116       y = 6
    117       t7 = x int+ 6
    118       s1 = t7
    119       s2 = t7
    120       t9 = x int* 6
    121       t10 = t9 int+ 2
    122       s3 = t10
    123       t11 = &x
    124       p = t11
    125       *t11 = 10
    126       t12 = x int+ y
    127       s4 = t12
    128       h = g
    129       calls = calls int+ 1
    130       t32 = g int+ 1
    131       g = t32
    132       t13 = t32 int+ h
    133       s5 = t13
    134       t14 = &y
    135       t34 = *t14
    136       t35 = t34 int+ 100
    137       *t14 = t35
    138       t15 = x int+ y
    139       param "%d %d %d %d %d %d\n"
    140       param t7
    141       param t7
    142       param t10
    143       param t12
    144       param t13
    145       param t15
    146       call printf, 7
    147       a[0] = 1
    148       a[4] = 2
    149       a[8] = 3
    150       i = 1
    151       t17 = a[4]
    152       t18 = t17 int<< 1
    153       e1 = t18
    154       a[4] = 9
    155       param "%d %d\n"
    156       param t18
    157       param 18
    158       call printf, 3
    159       if calls int== 0 goto L1
    160       z = 1
    161       goto L2
    162  L1:  z = 2
    163  L2:  k = 0
    164       step = 3
    165       acc = 0
    166  L3:  if k int>= 5 goto L4
    167       acc = acc int+ step
    168       k = k int+ 1
    169       goto L3
    170  L4:  same = x
    171       all = -1
    172       some = x int| 4
    173       cmp = 0
    174       cmp = 1
    175       cmp = 3
    176       calls = calls int+ 1
    177       t36 = g int+ 1
    178       g = t36
    179       ignored = t36
    180       param "%d %d %d %d\n"
    181       param same
    182       param -1
    183       param some
    184       param 3
    185       call printf, 5
    186       dead = 7
    187       dead = 8
    188       calls = calls int+ 1
    189       g = g int+ 1
    190       m[0] = 42
    191       r = 42
    192       t31 = 42 int+ calls
    193       param "%d %d %d %d %d\n"
    194       param z
    195       param acc
    196       param k
    197       param 8
    198       param t31
    199       call printf, 6
    200       return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

-2 -1073741824 17
10 10 26 16 11 116
4 18
10 -1 14 3
1 15 5 8 45

   exit code 0, 109 instructions executed
