============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t32_calls_registers.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 121 -> 53 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          121 -> 53   (56% fewer)

   constants folded                       25
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           82
   temporaries merged away                 3
   dead instructions removed              65
   jumps removed or redirected             1
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                7
   calls inlined                          14
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           5

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

 Code: 13 instruction(s)

    100       before = acc int+ n
    101       if n int!= 0 goto L1
    102       return acc
    103  L1:  t2 = n int- 1
    104       t10 = n int* n
    105       t4 = acc int+ t10
    106       param t2
    107       param t4
    108       t5 = call walk(int, int), 2
    109       t6 = t5 int+ before
    110       t7 = t6 int- acc
    111       t8 = t7 int- n
    112       return t8

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
   t16              temp    int                             4     132
   t17              temp    double                          8     136
   t18              temp    int                             4     144
   t69              temp    struct Pair                    16     392
   t70              temp    struct Pair                    16     408
   t71              temp    int                             4     424
   t72              temp    int                             4     428
   t73              temp    double                          8     432
   t74              temp    double                          8     440
   (65 temporaries no longer used after optimization not shown)

 Code: 40 instruction(s)

    113     param "%d\n"
    114     param 12
    115     call printf, 2
    116     param "%.2f\n"
    117     param 10000000071.0
    118     call printf, 2
    119     param "%d\n"
    120     param 152
    121     call printf, 2
    122     param "%d %d %d %d %d %d\n"
    123     param 605
    124     param 11
    125     param 22
    126     param 33
    127     param 44
    128     param 55
    129     call printf, 7
    130     t69[0] = 3
    131     t69[8] = 1.25
    132     t70 = t69
    133     t71 = t70[0]
    134     t72 = t71 int<< 1
    135     t70[0] = t72
    136     t73 = t70[8]
    137     t74 = t73 double* 2.0
    138     t70[8] = t74
    139     p = t70
    140     t16 = p[0]
    141     t17 = p[8]
    142     param "%d %.2f\n"
    143     param t16
    144     param t17
    145     call printf, 3
    146     param 10
    147     param 0
    148     t18 = call walk(int, int), 2
    149     param "%d\n"
    150     param t18
    151     call printf, 2
    152     return 0


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
