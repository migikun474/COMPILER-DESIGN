============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 125 -> 94 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          125 -> 94   (24% fewer)

   constants folded                       14
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded           36
   temporaries merged away                 6
   dead instructions removed              15
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

 Symbol table: 26 parameter(s)/local(s), 11 temporaries, frame 240 bytes

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
   (20 temporaries no longer used after optimization not shown)

 Code: 86 instruction(s)

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
    129       call touch(), 0
    130       t13 = g int+ h
    131       s5 = t13
    132       t14 = &y
    133       param t14
    134       call bump(int &), 1
    135       t15 = x int+ y
    136       param "%d %d %d %d %d %d\n"
    137       param t7
    138       param t7
    139       param t10
    140       param t12
    141       param t13
    142       param t15
    143       call printf, 7
    144       a[0] = 1
    145       a[4] = 2
    146       a[8] = 3
    147       i = 1
    148       t17 = a[4]
    149       t18 = t17 int<< 1
    150       e1 = t18
    151       a[4] = 9
    152       param "%d %d\n"
    153       param t18
    154       param 18
    155       call printf, 3
    156       if calls int== 0 goto L1
    157       z = 1
    158       goto L2
    159  L1:  z = 2
    160  L2:  k = 0
    161       step = 3
    162       acc = 0
    163  L3:  if k int>= 5 goto L4
    164       acc = acc int+ step
    165       k = k int+ 1
    166       goto L3
    167  L4:  same = x
    168       all = -1
    169       some = x int| 4
    170       cmp = 0
    171       cmp = 1
    172       cmp = 3
    173       ignored = call touch(), 0
    174       param "%d %d %d %d\n"
    175       param same
    176       param -1
    177       param some
    178       param 3
    179       call printf, 5
    180       dead = 7
    181       dead = 8
    182       call touch(), 0
    183       m[0] = 42
    184       r = 42
    185       t31 = 42 int+ calls
    186       param "%d %d %d %d %d\n"
    187       param z
    188       param acc
    189       param k
    190       param 8
    191       param t31
    192       call printf, 6
    193       return 0


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
