============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : no optimization
   Result        : Three address code generated: 16 function(s), 184 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   c.26             int                             4  0

 As three address code (initial values, in place before main runs):

    c.26 = 0

============================================================================
 FUNCTION even(int)        (link name _Z4eveni)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 9 instruction(s)

    100       if n int== 0 goto L1
    101       goto L2
    102  L1:  t1 = 1
    103       goto L3
    104  L2:  t2 = n int- 1
    105       param t2
    106       t3 = call odd(int), 1
    107       t1 = t3
    108  L3:  return t1

============================================================================
 FUNCTION odd(int)        (link name _Z3oddi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 9 instruction(s)

    109       if n int== 0 goto L4
    110       goto L5
    111  L4:  t1 = 0
    112       goto L6
    113  L5:  t2 = n int- 1
    114       param t2
    115       t3 = call even(int), 1
    116       t1 = t3
    117  L6:  return t1

============================================================================
 FUNCTION fib(int)        (link name _Z3fibi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24

 Code: 13 instruction(s)

    118       if n int< 2 goto L7
    119       goto L8
    120  L7:  t1 = n
    121       goto L9
    122  L8:  t2 = n int- 1
    123       param t2
    124       t3 = call fib(int), 1
    125       t4 = n int- 2
    126       param t4
    127       t5 = call fib(int), 1
    128       t6 = t3 int+ t5
    129       t1 = t6
    130  L9:  return t1

============================================================================
 FUNCTION gcd(int, int)        (link name _Z3gcdii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 10 instruction(s)

    131        if b int== 0 goto L10
    132        goto L11
    133  L10:  t1 = a
    134        goto L12
    135  L11:  t2 = a int% b
    136        param b
    137        param t2
    138        t3 = call gcd(int, int), 2
    139        t1 = t3
    140  L12:  return t1

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0

 Code: 1 instruction(s)

    141     return 1

============================================================================
 FUNCTION pick(double)        (link name _Z4pickd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   double                          8       0

 Code: 1 instruction(s)

    142     return 2

============================================================================
 FUNCTION pick(const char *)        (link name _Z4pickPKc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0

 Code: 1 instruction(s)

    143     return 3

============================================================================
 FUNCTION swap(int &, int &)        (link name _Z4swapRiS_)
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

    144     t1 = *a
    145     t = t1
    146     t2 = *b
    147     *a = t2
    148     *b = t
    149     return

============================================================================
 FUNCTION advance(int *&)        (link name _Z7advanceRPi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int *&                          4       0
   t1               temp    int *                           4       4
   t2               temp    int *                           4       8

 Code: 4 instruction(s)

    150     t1 = *p
    151     t2 = t1 ptr+ 4
    152     *p = t2
    153     return

============================================================================
 FUNCTION bigger(int &, int &)        (link name _Z6biggerRiS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int &                           4       0
   b                param   int &                           4       4
   t1               temp    int *                           4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 8 instruction(s)

    154        t2 = *a
    155        t3 = *b
    156        if t2 int> t3 goto L13
    157        goto L14
    158  L13:  t1 = a
    159        goto L15
    160  L14:  t1 = b
    161  L15:  return t1

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

    162     t1 = *v
    163     t2 = t1 double/ 2.0
    164     return t2

============================================================================
 FUNCTION sumv(va_list, int)        (link name _Z4sumvPvi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   ap               param   va_list                         4       0
   n                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24

 Code: 11 instruction(s)

    165        s = 0
    166  L16:  t1 = n
    167        t2 = n int- 1
    168        n = t2
    169        if t1 int!= 0 goto L17
    170        goto L18
    171  L17:  t3 = va_arg ap, int
    172        t4 = s int+ t3
    173        s = t4
    174        goto L16
    175  L18:  return s

============================================================================
 FUNCTION sum(int, ...)        (link name _Z3sumiz)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   s                local   int                             4       8
   t1               temp    int                             4      12

 Code: 7 instruction(s)

    176     va_start ap, n
    177     param ap
    178     param n
    179     t1 = call sumv(va_list, int), 2
    180     s = t1
    181     va_end ap
    182     return s

============================================================================
 FUNCTION avg(int, ...)        (link name _Z3avgiz)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 64 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   t                local   double                          8       8
   i                local   int                             4      16
   t1               temp    double                          8      24
   t2               temp    double                          8      32
   t3               temp    int                             4      40
   t4               temp    double                          8      48
   t5               temp    double                          8      56

 Code: 15 instruction(s)

    183        va_start ap, n
    184        t = 0.0
    185        i = 0
    186  L19:  if i int< n goto L20
    187        goto L21
    188  L20:  t1 = va_arg ap, double
    189        t2 = t double+ t1
    190        t = t2
    191        t3 = i int+ 1
    192        i = t3
    193        goto L19
    194  L21:  va_end ap
    195        t4 = inttodouble n
    196        t5 = t double/ t4
    197        return t5

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    198     t1 = c.26 int+ 1
    199     c.26 = t1
    200     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 22 temporaries, frame 140 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   arr              local   int[3]                         12       8
   p                local   int *                           4      20
   ra               local   int &                           4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int                             4      40
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t7               temp    int                             4      52
   t8               temp    int *                           4      56
   t9               temp    int *                           4      60
   t10              temp    int *                           4      64
   t11              temp    int *                           4      68
   t12              temp    int **                          4      72
   t13              temp    int *                           4      76
   t14              temp    int *                           4      80
   t15              temp    int &                           4      84
   t16              temp    int                             4      88
   t17              temp    double                          8      96
   t18              temp    const double *                  4     104
   t19              temp    double                          8     112
   t20              temp    int                             4     120
   t21              temp    double                          8     128
   t22              temp    int                             4     136

 Code: 83 instruction(s)

    201     param 10
    202     t1 = call even(int), 1
    203     param 7
    204     t2 = call odd(int), 1
    205     param 15
    206     t3 = call fib(int), 1
    207     param 84
    208     param 36
    209     t4 = call gcd(int, int), 2
    210     param "%d %d %d %d\n"
    211     param t1
    212     param t2
    213     param t3
    214     param t4
    215     call printf, 5
    216     param 1
    217     t5 = call pick(int), 1
    218     param 1.0
    219     t6 = call pick(double), 1
    220     param "s"
    221     t7 = call pick(const char *), 1
    222     param "%d %d %d\n"
    223     param t5
    224     param t6
    225     param t7
    226     call printf, 4
    227     a = 1
    228     b = 2
    229     arr[0] = 7
    230     arr[4] = 8
    231     arr[8] = 9
    232     t8 = &arr
    233     p = t8
    234     t9 = &a
    235     ra = t9
    236     *ra = 30
    237     t10 = &a
    238     t11 = &b
    239     param t10
    240     param t11
    241     call swap(int &, int &), 2
    242     t12 = &p
    243     param t12
    244     call advance(int *&), 1
    245     t13 = &a
    246     t14 = &b
    247     param t13
    248     param t14
    249     t15 = call bigger(int &, int &), 2
    250     *t15 = 40
    251     t16 = *p
    252     t17 = 5.0
    253     t18 = &t17
    254     param t18
    255     t19 = call half(const double &), 1
    256     param "%d %d %d %.1f\n"
    257     param a
    258     param b
    259     param t16
    260     param t19
    261     call printf, 5
    262     param 4
    263     param 1
    264     param 2
    265     param 3
    266     param 4
    267     t20 = call sum(int, ...), 5
    268     param 3
    269     param 1.0
    270     param 2.0
    271     param 4.5
    272     t21 = call avg(int, ...), 4
    273     param "%d %.2f\n"
    274     param t20
    275     param t21
    276     call printf, 3
    277     call counter(), 0
    278     call counter(), 0
    279     t22 = call counter(), 0
    280     param "%d\n"
    281     param t22
    282     call printf, 2
    283     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   odd                function      int (int)                  -           5    -    2  _Z3oddi; defined
   even               function      int (int)                  -           6    -    2  _Z4eveni; defined
   fib                function      int (int)                  -           8    -    3  _Z3fibi; defined
   gcd                function      int (int, int)             -           9    -    2  _Z3gcdii; defined
   pick               function      int (int)                  -          10    -    1  _Z4picki; defined
   pick               function      int (double)               -          11    -    1  _Z4pickd; defined
   pick               function      int (const char *)         -          12    -    1  _Z4pickPKc; defined
   swap               function      void (int &, int &)        -          13    -    1  _Z4swapRiS_; defined
   advance            function      void (int *&)              -          14    -    1  _Z7advanceRPi; defined
   bigger             function      int &(int &, int &)        -          15    -    1  _Z6biggerRiS_; defined
   half               function      double (const double &)    -          16    -    1  _Z4halfRKd; defined
   sumv               function      int (va_list, int)         -          17    -    1  _Z4sumvPvi; defined
   sum                function      int (int, ...)             -          18    -    1  _Z3sumiz; defined
   avg                function      double (int, ...)          -          19    -    1  _Z3avgiz; defined
   counter            function      int (void)                 -          20    -    3  _Z7counterv; defined
   main               function      int (void)                 -          21    -    0  defined

 scope: global > even()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       6    4    2  n.1

 scope: global > odd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       7    4    2  n.2

 scope: global > fib()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       8    4    4  n.3

 scope: global > gcd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param       9    4    2  a.4
   b                  parameter     int                        param       9    4    3  b.5

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      10    4    0  x.6
   x                  parameter     double                     param      11    8    0  x.7
   s                  parameter     const char *               param      12    4    0  s.8

 scope: global > swap()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      13    4    2  a.9
   b                  parameter     int &                      param      13    4    2  b.10
   t                  variable      int                        local      13    4    1  t.11

 scope: global > advance()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *&                     param      14    4    1  p.12

 scope: global > bigger()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      15    4    2  a.13
   b                  parameter     int &                      param      15    4    2  b.14

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const double &             param      16    4    1  v.15

 scope: global > sumv()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   ap                 parameter     va_list                    param      17    4    1  ap.16
   n                  parameter     int                        param      17    4    1  n.17
   s                  variable      int                        local      17    4    2  s.18

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      18    4    2  n.19
   ap                 variable      va_list                    local      18    4    3  ap.20
   s                  variable      int                        local      18    4    1  s.21

 scope: global > avg()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      19    4    3  n.22
   ap                 variable      va_list                    local      19    4    3  ap.23
   t                  variable      double                     local      19    8    2  t.24
   i                  variable      int                        local      19    4    3  i.25

 scope: global > counter()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        static     20    4    1  c.26; static

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      24    4    4  a.27
   b                  variable      int                        local      24    4    3  b.28
   arr                variable      int[3]                     local      24   12    1  arr.29
   p                  variable      int *                      local      24    4    2  p.30
   ra                 variable      int &                      local      25    4    1  ra.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
