============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t14_optimizer.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 248 -> 105 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          248 -> 105   (57% fewer)

   constants folded                       51
   algebraic simplifications               8
   common subexpressions                  11
   copies / constants forwarded          140
   temporaries merged away                 8
   dead instructions removed              79
   jumps removed or redirected            13
   unreachable instructions removed        8
   propagated across blocks                2
   dead assignments removed               35
   calls inlined                           9
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           6

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  1

 As three address code (initial values, in place before main runs):

    g = 1

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
    102     return t1

============================================================================
 FUNCTION aliasing()        (link name _Z8aliasingv)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 24 temporaries, frame 212 bytes

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
   t7               temp    int                             4      84
   t8               temp    int                             4      88
   t9               temp    int                             4      92
   t12              temp    int                             4     104
   t15              temp    int                             4     116
   t21              temp    int *                           4     140
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
   t38              temp    int                             4     208
   (14 temporaries no longer used after optimization not shown)

 Code: 36 instruction(s)

    103     x = 5
    104     y = 7
    105     t1 = &x
    106     t2 = x int+ 7
    107     *t1 = 20
    108     t3 = x int+ y
    109     t4 = &y
    110     *t4 = 1
    111     t5 = x int+ y
    112     t7 = *t1
    113     t8 = t7 int+ 1
    114     *t1 = t8
    115     t9 = x int+ y
    116     t38 = t8 int<< 1
    117     *t1 = t38
    118     arr[0] = 1
    119     arr[4] = 2
    120     arr[8] = 3
    121     t12 = arr[4]
    122     t15 = t12 int+ t12
    123     arr[4] = 9
    124     t21 = &arr
    125     t22 = t21 ptr+ 8
    126     *t22 = 4
    127     t23 = t3 int<< 1
    128     t24 = t2 int+ t23
    129     t25 = t5 int* 3
    130     t26 = t24 int+ t25
    131     t27 = t9 int* 5
    132     t28 = t26 int+ t27
    133     t29 = t28 int+ t15
    134     t30 = t29 int+ 18
    135     t31 = t30 int+ x
    136     t32 = arr[8]
    137     t33 = t31 int+ t32
    138     return t33

============================================================================
 FUNCTION flow(int)        (link name _Z4flowi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 1 temporary, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   k                local   int                             4      12
   t2               temp    int                             4      20
   (8 temporaries no longer used after optimization not shown)

 Code: 22 instruction(s)

    139       s = 0
    140       i = 0
    141  L1:  if i int>= n goto L8
    142       k = n int<< 1
    143       t2 = i int% 2
    144       if t2 int!= 0 goto L2
    145       s = s int+ k
    146       goto L3
    147  L2:  s = s int- 1
    148  L3:  if s int<= 1000 goto L4
    149       return -1
    150  L4:  i = i int+ 1
    151       goto L1
    152  L5:  s = s int+ 1
    153  L6:  s = s int+ 2
    154       goto L9
    155  L7:  s = 0
    156       goto L9
    157  L8:  if n int== 3 goto L5
    158       if n int== 4 goto L6
    159       goto L7
    160  L9:  return s

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 12 temporaries, frame 212 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   total            local   int                             4       0
   zero             local   int                             4       4
   x                local   double                          8       8
   y                local   double                          8      16
   t3               temp    int                             4      32
   t5               temp    int                             4      40
   t6               temp    int                             4      44
   t7               temp    int                             4      48
   t30              temp    int                             4     156
   t31              temp    int                             4     160
   t32              temp    int                             4     164
   t33              temp    int                             4     168
   t34              temp    int                             4     172
   t35              temp    int                             4     176
   t36              temp    int                             4     180
   t37              temp    int                             4     184
   (31 temporaries no longer used after optimization not shown)

 Code: 44 instruction(s)

    161     param "%d\n"
    162     param 632
    163     call printf, 2
    164     param "%d\n"
    165     param 136
    166     call printf, 2
    167     t3 = call aliasing(), 0
    168     param "%d\n"
    169     param t3
    170     call printf, 2
    171     t30 = g int+ 1
    172     call bump(), 0
    173     t31 = g int+ 1
    174     g = 2
    175     t32 = t30 int+ t30
    176     t33 = t32 int+ t31
    177     t34 = t33 int+ 3
    178     t35 = t34 int+ 6
    179     t36 = call bump(), 0
    180     t37 = t35 int+ t36
    181     param "%d %d\n"
    182     param t37
    183     param g
    184     call printf, 3
    185     param 3
    186     t5 = call flow(int), 1
    187     param 4
    188     t6 = call flow(int), 1
    189     param 5
    190     t7 = call flow(int), 1
    191     param "%d %d %d\n"
    192     param t5
    193     param t6
    194     param t7
    195     call printf, 4
    196     param "%d %d\n"
    197     param 0
    198     param 3
    199     call printf, 3
    200     param "%.1f %.1f\n"
    201     param 0.0
    202     param 0.0
    203     call printf, 3
    204     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      5    4    9  
   bump               function      int (void)                 -           6    -    2  _Z4bumpv; defined
   set                function      void (int *, int)          -           7    -    1  _Z3setPii; defined
   twice              function      void (int &)               -           8    -    1  _Z5twiceRi; defined
   fold               function      int (void)                 -          10    -    1  _Z4foldv; defined
   common             function      int (int, int)             -          21    -    1  _Z6commonii; defined
   aliasing           function      int (void)                 -          30    -    1  _Z8aliasingv; defined
   globals            function      int (void)                 -          52    -    1  _Z7globalsv; defined
   flow               function      int (int)                  -          64    -    3  _Z4flowi; defined
   divide             function      int (int, int)             -          81    -    2  _Z6divideii; defined
   main               function      int (void)                 -          83    -    0  defined

 scope: global > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *                      param       7    4    1  p.1
   v                  parameter     int                        param       7    4    1  v.2

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param       8    4    2  r.3

 scope: global > fold()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      11    4    4  a.4
   b                  variable      int                        local      11    4    4  b.5
   c                  variable      int                        local      11    4    2  c.6
   d                  variable      double                     local      12    8    1  d.7
   u                  variable      unsigned int               local      13    4    1  u.8
   ch                 variable      char                       local      14    1    1  ch.9

 scope: global > common()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      21    4   10  x.10
   y                  parameter     int                        param      21    4    7  y.11
   a                  variable      int                        local      22    4    1  a.12
   b                  variable      int                        local      22    4    1  b.13
   c                  variable      int                        local      23    4    1  c.14
   d                  variable      int                        local      23    4    1  d.15
   e                  variable      int                        local      24    4    1  e.16
   f                  variable      int                        local      26    4    1  f.17

 scope: global > aliasing()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      31    4    8  x.18
   y                  variable      int                        local      31    4    5  y.19
   p                  variable      int *                      local      32    4    1  p.20
   a                  variable      int                        local      33    4    1  a.21
   b                  variable      int                        local      35    4    1  b.22
   c                  variable      int                        local      37    4    1  c.23
   r                  variable      int &                      local      38    4    2  r.24
   d                  variable      int                        local      40    4    1  d.25
   arr                variable      int[3]                     local      42   12    7  arr.26
   i                  variable      int                        local      43    4    4  i.27
   e                  variable      int                        local      44    4    1  e.28
   f                  variable      int                        local      46    4    1  f.29
   q                  variable      int *                      local      47    4    1  q.30

 scope: global > globals()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      53    4    1  a.31
   b                  variable      int                        local      54    4    1  b.32
   c                  variable      int                        local      56    4    1  c.33
   d                  variable      int                        local      58    4    1  d.34
   v                  variable      int                        local      59    4    2  v.35
   e                  variable      int                        local      60    4    1  e.36

 scope: global > flow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      64    4    3  n.37
   s                  variable      int                        local      65    4    9  s.38

 scope: global > flow() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      66    4    3  i.39

 scope: global > flow() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      67    4    1  k.40

 scope: global > divide()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      81    4    1  a.41
   b                  parameter     int                        param      81    4    2  b.42

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      87    4    1  total.43
   zero               variable      int                        local      90    4    1  zero.44
   x                  variable      double                     local      92    8    2  x.45
   y                  variable      double                     local      92    8    1  y.46

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
