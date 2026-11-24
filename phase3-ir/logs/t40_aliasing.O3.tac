============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t40_aliasing.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 86 -> 58 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           86 -> 58   (32% fewer)

   constants folded                        3
   algebraic simplifications               1
   common subexpressions                   7
   copies / constants forwarded           32
   temporaries merged away                 1
   dead instructions removed              16
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                8
   calls inlined                           4
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           3

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  1

 As three address code (initial values, in place before main runs):

    g = 1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 15 temporaries, frame 188 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   p                local   int *                           4       4
   y                local   int                             4       8
   z                local   int                             4      12
   q                local   int *                           4      16
   a                local   int[4]                         16      20
   e                local   int *                           4      36
   i                local   int                             4      40
   before           local   int                             4      44
   h                local   int                             4      48
   v                local   int                             4      52
   m                local   int                             4      56
   n                local   int                             4      60
   t1               temp    int *                           4      64
   t3               temp    int                             4      72
   t6               temp    int                             4      84
   t7               temp    int *                           4      88
   t8               temp    int *                           4      92
   t10              temp    int                             4     100
   t12              temp    int                             4     108
   t15              temp    int                             4     120
   t16              temp    int *                           4     124
   t17              temp    int                             4     128
   t18              temp    int *                           4     132
   t19              temp    int *                           4     136
   t26              temp    int                             4     164
   t27              temp    int                             4     168
   t30              temp    int                             4     180
   (16 temporaries no longer used after optimization not shown)

 Code: 58 instruction(s)

    100     x = 5
    101     t1 = &x
    102     *t1 = 100
    103     t3 = x int+ 1
    104     param "%d %d\n"
    105     param 6
    106     param t3
    107     call printf, 3
    108     *t1 = 7
    109     t6 = x int<< 1
    110     param "%d %d\n"
    111     param 7
    112     param t6
    113     call printf, 3
    114     a[0] = 1
    115     a[4] = 2
    116     a[8] = 3
    117     a[12] = 4
    118     t7 = &a
    119     t8 = t7 ptr+ 8
    120     t10 = a[8]
    121     *t8 = 9
    122     t12 = a[8]
    123     t15 = t12 int+ 9
    124     param "%d %d %d\n"
    125     param t10
    126     param t12
    127     param t15
    128     call printf, 4
    129     h = g
    130     g = g int+ 10
    131     param "%d %d\n"
    132     param h
    133     param g
    134     call printf, 3
    135     v = 3
    136     t16 = &v
    137     *t16 = 4
    138     t17 = v int* v
    139     param "%d\n"
    140     param t17
    141     call printf, 2
    142     m = 1
    143     n = 2
    144     t18 = &m
    145     t19 = &n
    146     t26 = *t18
    147     t27 = *t19
    148     *t18 = t27
    149     *t19 = t26
    150     t30 = *t18
    151     *t18 = t30
    152     *t18 = t30
    153     param "%d %d\n"
    154     param m
    155     param n
    156     call printf, 3
    157     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      5    4    4  
   bump               function      void (void)                -           6    -    1  _Z4bumpv; defined
   setp               function      void (int *, int)          -           7    -    1  _Z4setpPii; defined
   swap               function      void (int *, int *)        -           8    -    2  _Z4swapPiS_; defined
   main               function      int (void)                 -           9    -    0  defined

 scope: global > setp()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *                      param       7    4    1  p.1
   v                  parameter     int                        param       7    4    1  v.2

 scope: global > swap()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       8    4    2  a.3
   b                  parameter     int *                      param       8    4    2  b.4
   t                  variable      int                        local       8    4    1  t.5

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      10    4    5  x.6
   p                  variable      int *                      local      11    4    2  p.7
   y                  variable      int                        local      12    4    1  y.8
   z                  variable      int                        local      14    4    1  z.9
   q                  variable      int *                      local      16    4    1  q.10
   a                  variable      int[4]                     local      19   16    4  a.11
   e                  variable      int *                      local      20    4    2  e.12
   i                  variable      int                        local      21    4    2  i.13
   before             variable      int                        local      21    4    1  before.14
   h                  variable      int                        local      24    4    1  h.15
   v                  variable      int                        local      27    4    3  v.16
   m                  variable      int                        local      30    4    4  m.17
   n                  variable      int                        local      30    4    2  n.18

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
