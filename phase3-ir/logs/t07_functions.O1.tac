============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 184 -> 165 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          184 -> 165   (10% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   3
   copies / constants forwarded            6
   temporaries merged away                 9
   dead instructions removed               3
   jumps removed or redirected             7
   unreachable instructions removed        0

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    100       if n int!= 0 goto L1
    101       t1 = 1
    102       goto L2
    103  L1:  t2 = n int- 1
    104       param t2
    105       t1 = call odd(int), 1
    106  L2:  return t1

============================================================================
 FUNCTION odd(int)        (link name _Z3oddi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    107       if n int!= 0 goto L3
    108       t1 = 0
    109       goto L4
    110  L3:  t2 = n int- 1
    111       param t2
    112       t1 = call even(int), 1
    113  L4:  return t1

============================================================================
 FUNCTION fib(int)        (link name _Z3fibi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    114       if n int>= 2 goto L5
    115       t1 = n
    116       goto L6
    117  L5:  t2 = n int- 1
    118       param t2
    119       t3 = call fib(int), 1
    120       t4 = n int- 2
    121       param t4
    122       t5 = call fib(int), 1
    123       t1 = t3 int+ t5
    124  L6:  return t1

============================================================================
 FUNCTION gcd(int, int)        (link name _Z3gcdii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    125       if b int!= 0 goto L7
    126       t1 = a
    127       goto L8
    128  L7:  t2 = a int% b
    129       param b
    130       param t2
    131       t1 = call gcd(int, int), 2
    132  L8:  return t1

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0

 Code: 1 instruction(s)

    133     return 1

============================================================================
 FUNCTION pick(double)        (link name _Z4pickd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   double                          8       0

 Code: 1 instruction(s)

    134     return 2

============================================================================
 FUNCTION pick(const char *)        (link name _Z4pickPKc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0

 Code: 1 instruction(s)

    135     return 3

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

    136     t1 = *a
    137     t = t1
    138     t2 = *b
    139     *a = t2
    140     *b = t1
    141     return

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

    142     t1 = *p
    143     t2 = t1 ptr+ 4
    144     *p = t2
    145     return

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

 Code: 7 instruction(s)

    146        t2 = *a
    147        t3 = *b
    148        if t2 int<= t3 goto L9
    149        t1 = a
    150        goto L10
    151  L9:   t1 = b
    152  L10:  return t1

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

    153     t1 = *v
    154     t2 = t1 double/ 2.0
    155     return t2

============================================================================
 FUNCTION sumv(va_list, int)        (link name _Z4sumvPvi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   ap               param   va_list                         4       0
   n                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t3               temp    int                             4      20
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    156        s = 0
    157  L11:  t1 = n
    158        n = n int- 1
    159        if t1 int== 0 goto L12
    160        t3 = va_arg ap, int
    161        s = s int+ t3
    162        goto L11
    163  L12:  return s

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

    164     va_start ap, n
    165     param ap
    166     param n
    167     t1 = call sumv(va_list, int), 2
    168     s = t1
    169     va_end ap
    170     return t1

============================================================================
 FUNCTION avg(int, ...)        (link name _Z3avgiz)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 64 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   t                local   double                          8       8
   i                local   int                             4      16
   t1               temp    double                          8      24
   t4               temp    double                          8      48
   t5               temp    double                          8      56
   (2 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    171        va_start ap, n
    172        t = 0.0
    173        i = 0
    174  L13:  if i int>= n goto L14
    175        t1 = va_arg ap, double
    176        t = t double+ t1
    177        i = i int+ 1
    178        goto L13
    179  L14:  va_end ap
    180        t4 = inttodouble n
    181        t5 = t double/ t4
    182        return t5

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    183     t1 = c.26 int+ 1
    184     c.26 = t1
    185     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 18 temporaries, frame 140 bytes

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
   t9               temp    int *                           4      60
   t11              temp    int *                           4      68
   t12              temp    int **                          4      72
   t15              temp    int &                           4      84
   t16              temp    int                             4      88
   t17              temp    double                          8      96
   t18              temp    const double *                  4     104
   t19              temp    double                          8     112
   t20              temp    int                             4     120
   t21              temp    double                          8     128
   t22              temp    int                             4     136
   (4 temporaries no longer used after optimization not shown)

 Code: 79 instruction(s)

    186     param 10
    187     t1 = call even(int), 1
    188     param 7
    189     t2 = call odd(int), 1
    190     param 15
    191     t3 = call fib(int), 1
    192     param 84
    193     param 36
    194     t4 = call gcd(int, int), 2
    195     param "%d %d %d %d\n"
    196     param t1
    197     param t2
    198     param t3
    199     param t4
    200     call printf, 5
    201     param 1
    202     t5 = call pick(int), 1
    203     param 1.0
    204     t6 = call pick(double), 1
    205     param "s"
    206     t7 = call pick(const char *), 1
    207     param "%d %d %d\n"
    208     param t5
    209     param t6
    210     param t7
    211     call printf, 4
    212     a = 1
    213     b = 2
    214     arr[0] = 7
    215     arr[4] = 8
    216     arr[8] = 9
    217     p = &arr
    218     t9 = &a
    219     ra = t9
    220     *t9 = 30
    221     t11 = &b
    222     param t9
    223     param t11
    224     call swap(int &, int &), 2
    225     t12 = &p
    226     param t12
    227     call advance(int *&), 1
    228     param t9
    229     param t11
    230     t15 = call bigger(int &, int &), 2
    231     *t15 = 40
    232     t16 = *p
    233     t17 = 5.0
    234     t18 = &t17
    235     param t18
    236     t19 = call half(const double &), 1
    237     param "%d %d %d %.1f\n"
    238     param a
    239     param b
    240     param t16
    241     param t19
    242     call printf, 5
    243     param 4
    244     param 1
    245     param 2
    246     param 3
    247     param 4
    248     t20 = call sum(int, ...), 5
    249     param 3
    250     param 1.0
    251     param 2.0
    252     param 4.5
    253     t21 = call avg(int, ...), 4
    254     param "%d %.2f\n"
    255     param t20
    256     param t21
    257     call printf, 3
    258     call counter(), 0
    259     call counter(), 0
    260     t22 = call counter(), 0
    261     param "%d\n"
    262     param t22
    263     call printf, 2
    264     return 0


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
