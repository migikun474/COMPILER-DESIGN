============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 182 -> 169 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          182 -> 169   (7% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   4
   copies / constants forwarded           10
   temporaries merged away                 4
   dead instructions removed               4
   jumps removed or redirected             5
   unreachable instructions removed        0

----------------------------------------------------------------------------
 GLOBALS: 3 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls.25         int                             4  0
   global           int                             4  10
   ratio            double                          8  2.5

============================================================================
 FUNCTION fact(int)        (link name _Z4facti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    100       if n int> 1 goto L1
    101       t1 = 1
    102       goto L2
    103  L1:  t2 = n int- 1
    104       param t2
    105       t3 = call fact(int), 1
    106       t1 = n int* t3
    107  L2:  return t1

============================================================================
 FUNCTION fib(int)        (link name _Z3fibi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 10 instruction(s)

    108       if n int>= 2 goto L3
    109       return n
    110  L3:  t1 = n int- 1
    111       param t1
    112       t2 = call fib(int), 1
    113       t3 = n int- 2
    114       param t3
    115       t4 = call fib(int), 1
    116       t5 = t2 int+ t4
    117       return t5

============================================================================
 FUNCTION gcd(int, int)        (link name _Z3gcdii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t                local   int                             4       8
   t1               temp    int                             4      12

 Code: 7 instruction(s)

    118  L4:  if b int== 0 goto L5
    119       t1 = a int% b
    120       t = t1
    121       a = b
    122       b = t1
    123       goto L4
    124  L5:  return a

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0

 Code: 1 instruction(s)

    125     return 1

============================================================================
 FUNCTION pick(double)        (link name _Z4pickd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   double                          8       0

 Code: 1 instruction(s)

    126     return 2

============================================================================
 FUNCTION pick(char *)        (link name _Z4pickPc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0

 Code: 1 instruction(s)

    127     return 3

============================================================================
 FUNCTION pick(int, int)        (link name _Z4pickii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4

 Code: 1 instruction(s)

    128     return 4

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

    129     t1 = *r
    130     t2 = t1 int+ 1
    131     *r = t2
    132     return

============================================================================
 FUNCTION exchange(int &, int &)        (link name _Z8exchangeRiS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int &                           4       0
   b                param   int &                           4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16

 Code: 6 instruction(s)

    133     t1 = *a
    134     t = t1
    135     t2 = *b
    136     *a = t2
    137     *b = t1
    138     return

============================================================================
 FUNCTION largest(int &, int &)        (link name _Z7largestRiS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int &                           4       0
   b                param   int &                           4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 5 instruction(s)

    139       t1 = *a
    140       t2 = *b
    141       if t1 int<= t2 goto L6
    142       return a
    143  L6:  return b

============================================================================
 FUNCTION half(const double &)        (link name _Z4halfRKd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   const double &                  4       0
   t1               temp    double                          8       8
   t2               temp    double                          8      16

 Code: 3 instruction(s)

    144     t1 = *v
    145     t2 = t1 double/ 2.0
    146     return t2

============================================================================
 FUNCTION sum(int, ...)        (link name _Z3sumiz)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 1 temporary, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    147       va_start ap, n
    148       s = 0
    149       i = 0
    150  L7:  if i int>= n goto L8
    151       t1 = va_arg ap, int
    152       s = s int+ t1
    153       i = i int+ 1
    154       goto L7
    155  L8:  va_end ap
    156       return s

============================================================================
 FUNCTION mix(int, ...)        (link name _Z3mixiz)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   s                local   double                          8       8
   t1               temp    double                          8      16
   t2               temp    int                             4      24
   t3               temp    double                          8      32
   t4               temp    double                          8      40

 Code: 8 instruction(s)

    157     va_start ap, n
    158     t1 = va_arg ap, double
    159     t2 = va_arg ap, int
    160     t3 = inttodouble t2
    161     t4 = t1 double+ t3
    162     s = t4
    163     va_end ap
    164     return t4

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    165     t1 = calls.25 int+ 1
    166     calls.25 = t1
    167     return t1

============================================================================
 FUNCTION scale(int)        (link name _Z5scalei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    168     global = global int* k
    169     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 25 temporaries, frame 164 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   text             local   char[4]                         4       0
   x                local   int                             4       4
   y                local   int                             4       8
   alias            local   int &                           4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    char (*)[4]                     4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52
   t11              temp    int *                           4      56
   t13              temp    int *                           4      64
   t15              temp    int                             4      72
   t16              temp    int                             4      76
   t19              temp    int &                           4      88
   t20              temp    double                          8      96
   t21              temp    const double *                  4     104
   t22              temp    double                          8     112
   t23              temp    int                             4     120
   t24              temp    int                             4     124
   t25              temp    double                          8     128
   t26              temp    int                             4     136
   t27              temp    double                          8     144
   t28              temp    double                          8     152
   t29              temp    int                             4     160
   (4 temporaries no longer used after optimization not shown)

 Code: 97 instruction(s)

    170     param 6
    171     t1 = call fact(int), 1
    172     param 10
    173     t2 = call fib(int), 1
    174     param 84
    175     param 36
    176     t3 = call gcd(int, int), 2
    177     param 4
    178     t4 = call later(int), 1
    179     param "%d %d %d %d\n"
    180     param t1
    181     param t2
    182     param t3
    183     param t4
    184     call printf, 5
    185     text[0] = 97
    186     text[1] = 98
    187     text[2] = 99
    188     text[3] = 0
    189     param 1
    190     t5 = call pick(int), 1
    191     param 2.5
    192     t6 = call pick(double), 1
    193     t7 = &text
    194     param t7
    195     t8 = call pick(char *), 1
    196     param 1
    197     param 2
    198     t9 = call pick(int, int), 2
    199     param 99
    200     t10 = call pick(int), 1
    201     param "%d %d %d %d %d\n"
    202     param t5
    203     param t6
    204     param t8
    205     param t9
    206     param t10
    207     call printf, 6
    208     x = 5
    209     y = 9
    210     t11 = &x
    211     param t11
    212     call bump(int &), 1
    213     t13 = &y
    214     param t11
    215     param t13
    216     call exchange(int &, int &), 2
    217     alias = t11
    218     t15 = *t11
    219     t16 = t15 int+ 100
    220     *t11 = t16
    221     param t11
    222     param t13
    223     t19 = call largest(int &, int &), 2
    224     *t19 = 0
    225     t20 = 5.0
    226     t21 = &t20
    227     param t21
    228     t22 = call half(const double &), 1
    229     param "%d %d %.2f\n"
    230     param x
    231     param y
    232     param t22
    233     call printf, 4
    234     param 3
    235     param 10
    236     param 20
    237     param 30
    238     t23 = call sum(int, ...), 4
    239     param 0
    240     t24 = call sum(int, ...), 1
    241     param 2
    242     param 1.5
    243     param 4
    244     t25 = call mix(int, ...), 3
    245     param "%d %d %.1f\n"
    246     param t23
    247     param t24
    248     param t25
    249     call printf, 4
    250     call counter(), 0
    251     call counter(), 0
    252     t26 = call counter(), 0
    253     param "%d\n"
    254     param t26
    255     call printf, 2
    256     param 3
    257     call scale(int), 1
    258     t27 = inttodouble global
    259     t28 = ratio double* t27
    260     param "%d %.1f\n"
    261     param global
    262     param t28
    263     call printf, 3
    264     param 1
    265     t29 = call later(int), 1
    266     return t29

============================================================================
 FUNCTION later(int)        (link name _Z5lateri)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    267     t1 = n int* 11
    268     return t1


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   later              function      int (int)                  -           6    -    2  _Z5lateri; defined
   fact               function      int (int)                  -           8    -    2  _Z4facti; defined
   fib                function      int (int)                  -           9    -    3  _Z3fibi; defined
   gcd                function      int (int, int)             -          10    -    1  _Z3gcdii; defined
   pick               function      int (int)                  -          12    -    2  _Z4picki; defined
   pick               function      int (double)               -          13    -    1  _Z4pickd; defined
   pick               function      int (char *)               -          14    -    1  _Z4pickPc; defined
   pick               function      int (int, int)             -          15    -    1  _Z4pickii; defined
   bump               function      void (int &)               -          17    -    1  _Z4bumpRi; defined
   exchange           function      void (int &, int &)        -          18    -    1  _Z8exchangeRiS_; defined
   largest            function      int &(int &, int &)        -          19    -    1  _Z7largestRiS_; defined
   half               function      double (const double &)    -          20    -    1  _Z4halfRKd; defined
   sum                function      int (int, ...)             -          22    -    2  _Z3sumiz; defined
   mix                function      double (int, ...)          -          31    -    1  _Z3mixiz; defined
   counter            function      int (void)                 -          39    -    3  _Z7counterv; defined
   global             variable      int                        global     45    4    4  
   ratio              variable      double                     global     46    8    1  
   scale              function      void (int)                 -          47    -    1  _Z5scalei; defined
   main               function      int (void)                 -          49    -    0  defined

 scope: global > fact()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       8    4    3  n.1

 scope: global > fib()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       9    4    4  n.2

 scope: global > gcd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      10    4    3  a.3
   b                  parameter     int                        param      10    4    4  b.4

 scope: global > gcd() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local      10    4    1  t.5

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      12    4    0  a.6
   a                  parameter     double                     param      13    8    0  a.7
   s                  parameter     char *                     param      14    4    0  s.8
   a                  parameter     int                        param      15    4    0  a.9
   b                  parameter     int                        param      15    4    0  b.10

 scope: global > bump()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param      17    4    2  r.11

 scope: global > exchange()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      18    4    2  a.12
   b                  parameter     int &                      param      18    4    2  b.13
   t                  variable      int                        local      18    4    1  t.14

 scope: global > largest()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      19    4    2  a.15
   b                  parameter     int &                      param      19    4    2  b.16

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const double &             param      20    4    1  v.17

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      22    4    2  n.18
   ap                 variable      va_list                    local      23    4    3  ap.19
   s                  variable      int                        local      25    4    2  s.20

 scope: global > sum() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      26    4    2  i.21

 scope: global > mix()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      31    4    1  n.22
   ap                 variable      va_list                    local      32    4    4  ap.23
   s                  variable      double                     local      34    8    1  s.24

 scope: global > counter()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        static     40    4    2  calls.25; static

 scope: global > scale()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      47    4    1  k.26

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   text               variable      char[4]                    local      51    4    1  text.27
   x                  variable      int                        local      54    4    5  x.28
   y                  variable      int                        local      54    4    3  y.29
   alias              variable      int &                      local      57    4    2  alias.30

 scope: global > later()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      70    4    1  n.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
