============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t32_calls_registers.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 120 -> 85 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          120 -> 85   (29% fewer)

   calls inlined                          14
   constants folded                       25
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           83
   temporaries merged away                 3
   dead instructions removed              64
   jumps removed or redirected             1
   unreachable instructions removed        0

============================================================================
 FUNCTION many(int, int, int, int, int, int)        (link name _Z4manyiiiiii)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 5 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   c                param   int                             4       8
   d                param   int                             4      12
   e                param   int                             4      16
   f                param   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int                             4      36
   t5               temp    int                             4      40

 Code: 6 instruction(s)

    100     t1 = a int- b
    101     t2 = c int* d
    102     t3 = t1 int+ t2
    103     t4 = t3 int- e
    104     t5 = t4 int+ f
    105     return t5

============================================================================
 FUNCTION mixed(char, double, int, long long)        (link name _Z5mixedcdix)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 6 temporaries, frame 80 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   char                            1       0
   d                param   double                          8       8
   i                param   int                             4      16
   w                param   long long                       8      24
   t1               temp    double                          8      32
   t2               temp    double                          8      40
   t3               temp    double                          8      48
   t4               temp    double                          8      56
   t5               temp    double                          8      64
   t6               temp    double                          8      72

 Code: 7 instruction(s)

    106     t1 = chartodouble c
    107     t2 = inttodouble i
    108     t3 = d double* t2
    109     t4 = t1 double+ t3
    110     t5 = llongtodouble w
    111     t6 = t4 double+ t5
    112     return t6

============================================================================
 FUNCTION make(int, double)        (link name _Z4makeid)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 0 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   y                param   double                          8       8
   p                local   struct Pair                    16      16

 Code: 3 instruction(s)

    113     p[0] = x
    114     p[8] = y
    115     return p

============================================================================
 FUNCTION twice(struct Pair)        (link name _Z5twice4Pair)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Pair                    16       0
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    double                          8      24
   t4               temp    double                          8      32

 Code: 7 instruction(s)

    116     t1 = p[0]
    117     t2 = t1 int<< 1
    118     p[0] = t2
    119     t3 = p[8]
    120     t4 = t3 double* 2.0
    121     p[8] = t4
    122     return p

============================================================================
 FUNCTION sq(int)        (link name _Z2sqi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    123     t1 = v int* v
    124     return t1

============================================================================
 FUNCTION walk(int, int)        (link name _Z4walkii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 7 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   acc              param   int                             4       4
   before           local   int                             4       8
   r                local   int                             4      12
   t2               temp    int                             4      20
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t10              temp    int                             4      52
   (3 temporaries no longer used after optimization not shown)

 Code: 14 instruction(s)

    125       before = acc int+ n
    126       if n int!= 0 goto L1
    127       return acc
    128  L1:  t2 = n int- 1
    129       t10 = n int* n
    130       t4 = acc int+ t10
    131       param t2
    132       param t4
    133       t5 = call walk(int, int), 2
    134       r = t5
    135       t6 = t5 int+ before
    136       t7 = t6 int- acc
    137       t8 = t7 int- n
    138       return t8

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 9 temporaries, frame 448 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   keep1            local   int                             4       0
   keep2            local   int                             4       4
   keep3            local   int                             4       8
   keep4            local   int                             4      12
   keep5            local   int                             4      16
   s                local   int                             4      20
   p                local   struct Pair                    16      24
   t15              temp    int                             4     128
   t16              temp    double                          8     136
   t17              temp    int                             4     144
   t68              temp    struct Pair                    16     392
   t69              temp    struct Pair                    16     408
   t70              temp    int                             4     424
   t71              temp    int                             4     428
   t72              temp    double                          8     432
   t73              temp    double                          8     440
   (64 temporaries no longer used after optimization not shown)

 Code: 46 instruction(s)

    139     param "%d\n"
    140     param 12
    141     call printf, 2
    142     param "%.2f\n"
    143     param 10000000071.0
    144     call printf, 2
    145     param "%d\n"
    146     param 152
    147     call printf, 2
    148     keep1 = 11
    149     keep2 = 22
    150     keep3 = 33
    151     keep4 = 44
    152     keep5 = 55
    153     s = 605
    154     param "%d %d %d %d %d %d\n"
    155     param 605
    156     param 11
    157     param 22
    158     param 33
    159     param 44
    160     param 55
    161     call printf, 7
    162     t68[0] = 3
    163     t68[8] = 1.25
    164     t69 = t68
    165     t70 = t69[0]
    166     t71 = t70 int<< 1
    167     t69[0] = t71
    168     t72 = t69[8]
    169     t73 = t72 double* 2.0
    170     t69[8] = t73
    171     p = t69
    172     t15 = p[0]
    173     t16 = p[8]
    174     param "%d %.2f\n"
    175     param t15
    176     param t16
    177     call printf, 3
    178     param 10
    179     param 0
    180     t17 = call walk(int, int), 2
    181     param "%d\n"
    182     param t17
    183     call printf, 2
    184     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Pair               struct_tag    struct Pair                -           5    -    0  size 16
   many               function      int (int, int, int, int, int, int) -           6    -    2  _Z4manyiiiiii; defined
   mixed              function      double (char, double, int, long long) -           7    -    1  _Z5mixedcdix; defined
   make               function      struct Pair (int, double)  -           8    -    1  _Z4makeid; defined
   twice              function      struct Pair (struct Pair)  -           9    -    1  _Z5twice4Pair; defined
   sq                 function      int (int)                  -          10    -    9  _Z2sqi; defined
   walk               function      int (int, int)             -          11    -    2  _Z4walkii; defined
   main               function      int (void)                 -          17    -    0  defined

 scope: global > struct Pair
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      5    4    4  Pair::x; public, offset 0
   y                  field         double                     member      5    8    4  Pair::y; public, offset 8

 scope: global > many()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param       6    4    1  a.1
   b                  parameter     int                        param       6    4    1  b.2
   c                  parameter     int                        param       6    4    1  c.3
   d                  parameter     int                        param       6    4    1  d.4
   e                  parameter     int                        param       6    4    1  e.5
   f                  parameter     int                        param       6    4    1  f.6

 scope: global > mixed()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     char                       param       7    1    1  c.7
   d                  parameter     double                     param       7    8    1  d.8
   i                  parameter     int                        param       7    4    1  i.9
   w                  parameter     long long                  param       7    8    1  w.10

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param       8    4    1  x.11
   y                  parameter     double                     param       8    8    1  y.12
   p                  variable      struct Pair                local       8   16    3  p.13

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Pair                param       9   16    5  p.14

 scope: global > sq()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      10    4    2  v.15

 scope: global > walk()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      11    4    5  n.16
   acc                parameter     int                        param      11    4    4  acc.17
   before             variable      int                        local      12    4    1  before.18
   r                  variable      int                        local      14    4    1  r.19

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   keep1              variable      int                        local      21    4    2  keep1.20
   keep2              variable      int                        local      21    4    2  keep2.21
   keep3              variable      int                        local      21    4    1  keep3.22
   keep4              variable      int                        local      21    4    1  keep4.23
   keep5              variable      int                        local      21    4    1  keep5.24
   s                  variable      int                        local      22    4    1  s.25
   p                  variable      struct Pair                local      24   16    2  p.26

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Pair: size 16, align 8
    +0  int x  [public]
    +8  double y  [public]

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

12
10000000071.00
152
605 11 22 33 44 55
6 2.50
385

   exit code 0, 179 instructions executed
