============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : no optimization
   Result        : Three address code generated: 17 function(s), 182 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 3 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls.25         int                             4  0
   global           int                             4  10
   ratio            double                          8  2.5

 As three address code (initial values, in place before main runs):

    calls.25 = 0
    global = 10
    ratio = 2.5

============================================================================
 FUNCTION fact(int)        (link name _Z4facti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16

 Code: 10 instruction(s)

    100       if n int<= 1 goto L1
    101       goto L2
    102  L1:  t1 = 1
    103       goto L3
    104  L2:  t2 = n int- 1
    105       param t2
    106       t3 = call fact(int), 1
    107       t4 = n int* t3
    108       t1 = t4
    109  L3:  return t1

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

 Code: 11 instruction(s)

    110       if n int< 2 goto L4
    111       goto L5
    112  L4:  return n
    113  L5:  t1 = n int- 1
    114       param t1
    115       t2 = call fib(int), 1
    116       t3 = n int- 2
    117       param t3
    118       t4 = call fib(int), 1
    119       t5 = t2 int+ t4
    120       return t5

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

 Code: 8 instruction(s)

    121  L6:  if b int!= 0 goto L7
    122       goto L8
    123  L7:  t1 = a int% b
    124       t = t1
    125       a = b
    126       b = t
    127       goto L6
    128  L8:  return a

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0

 Code: 1 instruction(s)

    129     return 1

============================================================================
 FUNCTION pick(double)        (link name _Z4pickd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   double                          8       0

 Code: 1 instruction(s)

    130     return 2

============================================================================
 FUNCTION pick(char *)        (link name _Z4pickPc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0

 Code: 1 instruction(s)

    131     return 3

============================================================================
 FUNCTION pick(int, int)        (link name _Z4pickii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4

 Code: 1 instruction(s)

    132     return 4

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

    133     t1 = *r
    134     t2 = t1 int+ 1
    135     *r = t2
    136     return

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

    137     t1 = *a
    138     t = t1
    139     t2 = *b
    140     *a = t2
    141     *b = t
    142     return

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

 Code: 6 instruction(s)

    143        t1 = *a
    144        t2 = *b
    145        if t1 int> t2 goto L9
    146        goto L10
    147  L9:   return a
    148  L10:  return b

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

    149     t1 = *v
    150     t2 = t1 double/ 2.0
    151     return t2

============================================================================
 FUNCTION sum(int, ...)        (link name _Z3sumiz)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24

 Code: 13 instruction(s)

    152        va_start ap, n
    153        s = 0
    154        i = 0
    155  L11:  if i int< n goto L12
    156        goto L13
    157  L12:  t1 = va_arg ap, int
    158        t2 = s int+ t1
    159        s = t2
    160        t3 = i int+ 1
    161        i = t3
    162        goto L11
    163  L13:  va_end ap
    164        return s

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

    165     va_start ap, n
    166     t1 = va_arg ap, double
    167     t2 = va_arg ap, int
    168     t3 = inttodouble t2
    169     t4 = t1 double+ t3
    170     s = t4
    171     va_end ap
    172     return s

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    173     t1 = calls.25 int+ 1
    174     calls.25 = t1
    175     return calls.25

============================================================================
 FUNCTION scale(int)        (link name _Z5scalei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   t1               temp    int                             4       4

 Code: 3 instruction(s)

    176     t1 = global int* k
    177     global = t1
    178     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 29 temporaries, frame 164 bytes

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
   t7               temp    char *                          4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52
   t11              temp    int *                           4      56
   t12              temp    int *                           4      60
   t13              temp    int *                           4      64
   t14              temp    int *                           4      68
   t15              temp    int                             4      72
   t16              temp    int                             4      76
   t17              temp    int *                           4      80
   t18              temp    int *                           4      84
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

 Code: 101 instruction(s)

    179     param 6
    180     t1 = call fact(int), 1
    181     param 10
    182     t2 = call fib(int), 1
    183     param 84
    184     param 36
    185     t3 = call gcd(int, int), 2
    186     param 4
    187     t4 = call later(int), 1
    188     param "%d %d %d %d\n"
    189     param t1
    190     param t2
    191     param t3
    192     param t4
    193     call printf, 5
    194     text[0] = 97
    195     text[1] = 98
    196     text[2] = 99
    197     text[3] = 0
    198     param 1
    199     t5 = call pick(int), 1
    200     param 2.5
    201     t6 = call pick(double), 1
    202     t7 = &text
    203     param t7
    204     t8 = call pick(char *), 1
    205     param 1
    206     param 2
    207     t9 = call pick(int, int), 2
    208     param 99
    209     t10 = call pick(int), 1
    210     param "%d %d %d %d %d\n"
    211     param t5
    212     param t6
    213     param t8
    214     param t9
    215     param t10
    216     call printf, 6
    217     x = 5
    218     y = 9
    219     t11 = &x
    220     param t11
    221     call bump(int &), 1
    222     t12 = &x
    223     t13 = &y
    224     param t12
    225     param t13
    226     call exchange(int &, int &), 2
    227     t14 = &x
    228     alias = t14
    229     t15 = *alias
    230     t16 = t15 int+ 100
    231     *alias = t16
    232     t17 = &x
    233     t18 = &y
    234     param t17
    235     param t18
    236     t19 = call largest(int &, int &), 2
    237     *t19 = 0
    238     t20 = 5.0
    239     t21 = &t20
    240     param t21
    241     t22 = call half(const double &), 1
    242     param "%d %d %.2f\n"
    243     param x
    244     param y
    245     param t22
    246     call printf, 4
    247     param 3
    248     param 10
    249     param 20
    250     param 30
    251     t23 = call sum(int, ...), 4
    252     param 0
    253     t24 = call sum(int, ...), 1
    254     param 2
    255     param 1.5
    256     param 4
    257     t25 = call mix(int, ...), 3
    258     param "%d %d %.1f\n"
    259     param t23
    260     param t24
    261     param t25
    262     call printf, 4
    263     call counter(), 0
    264     call counter(), 0
    265     t26 = call counter(), 0
    266     param "%d\n"
    267     param t26
    268     call printf, 2
    269     param 3
    270     call scale(int), 1
    271     t27 = inttodouble global
    272     t28 = ratio double* t27
    273     param "%d %.1f\n"
    274     param global
    275     param t28
    276     call printf, 3
    277     param 1
    278     t29 = call later(int), 1
    279     return t29

============================================================================
 FUNCTION later(int)        (link name _Z5lateri)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    280     t1 = n int* 11
    281     return t1


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
