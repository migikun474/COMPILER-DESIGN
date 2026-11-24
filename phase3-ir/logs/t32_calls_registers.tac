============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t32_calls_registers.c
   Optimization  : no optimization
   Result        : Three address code generated: 7 function(s), 121 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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
    117     t2 = t1 int* 2
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

 Symbol table: 4 parameter(s)/local(s), 8 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   acc              param   int                             4       4
   before           local   int                             4       8
   r                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44

 Code: 17 instruction(s)

    125       t1 = acc int+ n
    126       before = t1
    127       if n int== 0 goto L1
    128       goto L2
    129  L1:  return acc
    130  L2:  t2 = n int- 1
    131       param n
    132       t3 = call sq(int), 1
    133       t4 = acc int+ t3
    134       param t2
    135       param t4
    136       t5 = call walk(int, int), 2
    137       r = t5
    138       t6 = r int+ before
    139       t7 = t6 int- acc
    140       t8 = t7 int- n
    141       return t8

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 18 temporaries, frame 148 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   keep1            local   int                             4       0
   keep2            local   int                             4       4
   keep3            local   int                             4       8
   keep4            local   int                             4      12
   keep5            local   int                             4      16
   s                local   int                             4      20
   p                local   struct Pair                    16      24
   t1               temp    int                             4      40
   t2               temp    double                          8      48
   t3               temp    int                             4      56
   t4               temp    int                             4      60
   t5               temp    int                             4      64
   t6               temp    int                             4      68
   t7               temp    int                             4      72
   t8               temp    int                             4      76
   t9               temp    int                             4      80
   t10              temp    int                             4      84
   t11              temp    int                             4      88
   t12              temp    int                             4      92
   t13              temp    struct Pair                    16      96
   t14              temp    struct Pair                    16     112
   t15              temp    struct Pair *                   4     128
   t16              temp    int                             4     132
   t17              temp    double                          8     136
   t18              temp    int                             4     144

 Code: 79 instruction(s)

    142     param 1
    143     param 2
    144     param 3
    145     param 4
    146     param 5
    147     param 6
    148     t1 = call many(int, int, int, int, int, int), 6
    149     param "%d\n"
    150     param t1
    151     call printf, 2
    152     param 65
    153     param 1.5
    154     param 4
    155     param 10000000000
    156     t2 = call mixed(char, double, int, long long), 4
    157     param "%.2f\n"
    158     param t2
    159     call printf, 2
    160     param 1
    161     t3 = call sq(int), 1
    162     param 2
    163     t4 = call sq(int), 1
    164     param 3
    165     t5 = call sq(int), 1
    166     param 4
    167     t6 = call sq(int), 1
    168     param 5
    169     t7 = call sq(int), 1
    170     param 6
    171     t8 = call sq(int), 1
    172     param t3
    173     param t4
    174     param t5
    175     param t6
    176     param t7
    177     param t8
    178     t9 = call many(int, int, int, int, int, int), 6
    179     param "%d\n"
    180     param t9
    181     call printf, 2
    182     keep1 = 11
    183     keep2 = 22
    184     keep3 = 33
    185     keep4 = 44
    186     keep5 = 55
    187     param keep1
    188     t10 = call sq(int), 1
    189     param keep2
    190     t11 = call sq(int), 1
    191     t12 = t10 int+ t11
    192     s = t12
    193     param "%d %d %d %d %d %d\n"
    194     param s
    195     param keep1
    196     param keep2
    197     param keep3
    198     param keep4
    199     param keep5
    200     call printf, 7
    201     param 3
    202     param 1.25
    203     t13 = call make(int, double), 2
    204     param t13
    205     t14 = call twice(struct Pair), 1
    206     p = t14
    207     t15 = &p
    208     t16 = p[0]
    209     t17 = p[8]
    210     param "%d %.2f\n"
    211     param t16
    212     param t17
    213     call printf, 3
    214     param 10
    215     param 0
    216     t18 = call walk(int, int), 2
    217     param "%d\n"
    218     param t18
    219     call printf, 2
    220     return 0


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
