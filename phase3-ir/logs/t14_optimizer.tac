============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 125 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 0 parameter(s)/local(s), 2 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0
   t2               temp    int                             4       4

 Code: 5 instruction(s)

    100     t1 = calls int+ 1
    101     calls = t1
    102     t2 = g int+ 1
    103     g = t2
    104     return g

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

    105     t1 = *r
    106     t2 = t1 int+ 100
    107     *r = t2
    108     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 26 parameter(s)/local(s), 31 temporaries, frame 240 bytes

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
   t1               temp    int                             4     116
   t2               temp    int                             4     120
   t3               temp    int                             4     124
   t4               temp    int                             4     128
   t5               temp    int                             4     132
   t6               temp    int                             4     136
   t7               temp    int                             4     140
   t8               temp    int                             4     144
   t9               temp    int                             4     148
   t10              temp    int                             4     152
   t11              temp    int *                           4     156
   t12              temp    int                             4     160
   t13              temp    int                             4     164
   t14              temp    int *                           4     168
   t15              temp    int                             4     172
   t16              temp    int                             4     176
   t17              temp    int                             4     180
   t18              temp    int                             4     184
   t19              temp    int                             4     188
   t20              temp    int                             4     192
   t21              temp    int                             4     196
   t22              temp    int                             4     200
   t23              temp    int                             4     204
   t24              temp    int                             4     208
   t25              temp    int                             4     212
   t26              temp    int                             4     216
   t27              temp    int                             4     220
   t28              temp    int                             4     224
   t29              temp    int                             4     228
   t30              temp    int                             4     232
   t31              temp    int                             4     236

 Code: 116 instruction(s)

    109        big = 2147483647
    110        t1 = big int+ 0
    111        w = t1
    112        t2 = w int* 2
    113        t3 = w int+ 1
    114        t4 = t3 int/ 2
    115        t5 = 3 int* 4
    116        t6 = t5 int+ 5
    117        param "%d %d %d\n"
    118        param t2
    119        param t4
    120        param t6
    121        call printf, 4
    122        if 2 int> 3 goto L1
    123        goto L2
    124  L1:   param "never\n"
    125        call printf, 1
    126  L2:   x = 4
    127        y = 6
    128        t7 = x int+ y
    129        s1 = t7
    130        t8 = y int+ x
    131        s2 = t8
    132        t9 = x int* y
    133        t10 = t9 int+ 2
    134        s3 = t10
    135        t11 = &x
    136        p = t11
    137        *p = 10
    138        t12 = x int+ y
    139        s4 = t12
    140        h = g
    141        call touch(), 0
    142        t13 = g int+ h
    143        s5 = t13
    144        t14 = &y
    145        param t14
    146        call bump(int &), 1
    147        t15 = x int+ y
    148        param "%d %d %d %d %d %d\n"
    149        param s1
    150        param s2
    151        param s3
    152        param s4
    153        param s5
    154        param t15
    155        call printf, 7
    156        a[0] = 1
    157        a[4] = 2
    158        a[8] = 3
    159        i = 1
    160        t16 = i int* 4                      (w = 4)
    161        t17 = a[t16]
    162        t18 = t17 int* 2
    163        e1 = t18
    164        a[4] = 9
    165        t19 = i int* 4                      (w = 4)
    166        t20 = a[t19]
    167        t21 = t20 int* 2
    168        param "%d %d\n"
    169        param e1
    170        param t21
    171        call printf, 3
    172        if calls int!= 0 goto L3
    173        goto L4
    174  L3:   z = 1
    175        goto L5
    176  L4:   z = 2
    177  L5:   k = 0
    178        step = 3
    179        acc = 0
    180  L6:   if k int< 5 goto L7
    181        goto L8
    182  L7:   t22 = acc int+ step
    183        acc = t22
    184        t23 = k int+ 1
    185        k = t23
    186        goto L6
    187  L8:   t24 = x int| x
    188        same = t24
    189        t25 = int- 1
    190        t26 = x int| t25
    191        all = t26
    192        t27 = x int| 4
    193        some = t27
    194        cmp = 0
    195        if x int<= x goto L9
    196        goto L10
    197  L9:   cmp = 1
    198  L10:  if x int== x goto L11
    199        goto L12
    200  L11:  t28 = cmp int+ 2
    201        cmp = t28
    202  L12:  t29 = call touch(), 0
    203        ignored = t29
    204        param "%d %d %d %d\n"
    205        param same
    206        param all
    207        param some
    208        param cmp
    209        call printf, 5
    210        dead = 7
    211        dead = 8
    212        call touch(), 0
    213        m[0] = 42
    214        t30 = m[0]
    215        r = t30
    216        t31 = r int+ calls
    217        param "%d %d %d %d %d\n"
    218        param z
    219        param acc
    220        param k
    221        param dead
    222        param t31
    223        call printf, 6
    224        return 0


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
