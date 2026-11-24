============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t40_aliasing.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 86 -> 76 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           86 -> 76   (11% fewer)

   constants folded                        3
   algebraic simplifications               1
   common subexpressions                   6
   copies / constants forwarded           21
   temporaries merged away                 1
   dead instructions removed               9
   jumps removed or redirected             0
   unreachable instructions removed        0

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

 Symbol table: 0 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    100     g = g int+ 10
    101     return

============================================================================
 FUNCTION setp(int *, int)        (link name _Z4setpPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int *                           4       0
   v                param   int                             4       4

 Code: 2 instruction(s)

    102     *p = v
    103     return

============================================================================
 FUNCTION swap(int *, int *)        (link name _Z4swapPiS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   b                param   int *                           4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16

 Code: 6 instruction(s)

    104     t1 = *a
    105     t = t1
    106     t2 = *b
    107     *a = t2
    108     *b = t1
    109     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 12 temporaries, frame 148 bytes

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
   (9 temporaries no longer used after optimization not shown)

 Code: 66 instruction(s)

    110     x = 5
    111     t1 = &x
    112     p = t1
    113     y = 6
    114     *t1 = 100
    115     t3 = x int+ 1
    116     z = t3
    117     param "%d %d\n"
    118     param 6
    119     param t3
    120     call printf, 3
    121     q = t1
    122     *t1 = 7
    123     t6 = x int<< 1
    124     param "%d %d\n"
    125     param 7
    126     param t6
    127     call printf, 3
    128     a[0] = 1
    129     a[4] = 2
    130     a[8] = 3
    131     a[12] = 4
    132     t7 = &a
    133     t8 = t7 ptr+ 8
    134     e = t8
    135     i = 2
    136     t10 = a[8]
    137     before = t10
    138     *t8 = 9
    139     t12 = a[8]
    140     t15 = t12 int+ 9
    141     param "%d %d %d\n"
    142     param t10
    143     param t12
    144     param t15
    145     call printf, 4
    146     h = g
    147     call bump(), 0
    148     param "%d %d\n"
    149     param h
    150     param g
    151     call printf, 3
    152     v = 3
    153     t16 = &v
    154     param t16
    155     param 4
    156     call setp(int *, int), 2
    157     t17 = v int* v
    158     param "%d\n"
    159     param t17
    160     call printf, 2
    161     m = 1
    162     n = 2
    163     t18 = &m
    164     t19 = &n
    165     param t18
    166     param t19
    167     call swap(int *, int *), 2
    168     param t18
    169     param t18
    170     call swap(int *, int *), 2
    171     param "%d %d\n"
    172     param m
    173     param n
    174     call printf, 3
    175     return 0


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
