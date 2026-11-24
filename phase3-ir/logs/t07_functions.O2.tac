============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 184 -> 162 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          184 -> 162   (11% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   3
   copies / constants forwarded            6
   temporaries merged away                 9
   dead instructions removed               3
   jumps removed or redirected             7
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                3

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

 Code: 5 instruction(s)

    136     t1 = *a
    137     t2 = *b
    138     *a = t2
    139     *b = t1
    140     return

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

    141     t1 = *p
    142     t2 = t1 ptr+ 4
    143     *p = t2
    144     return

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

    145        t2 = *a
    146        t3 = *b
    147        if t2 int<= t3 goto L9
    148        t1 = a
    149        goto L10
    150  L9:   t1 = b
    151  L10:  return t1

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

    152     t1 = *v
    153     t2 = t1 double/ 2.0
    154     return t2

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

    155        s = 0
    156  L11:  t1 = n
    157        n = n int- 1
    158        if t1 int== 0 goto L12
    159        t3 = va_arg ap, int
    160        s = s int+ t3
    161        goto L11
    162  L12:  return s

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

 Code: 6 instruction(s)

    163     va_start ap, n
    164     param ap
    165     param n
    166     t1 = call sumv(va_list, int), 2
    167     va_end ap
    168     return t1

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

    169        va_start ap, n
    170        t = 0.0
    171        i = 0
    172  L13:  if i int>= n goto L14
    173        t1 = va_arg ap, double
    174        t = t double+ t1
    175        i = i int+ 1
    176        goto L13
    177  L14:  va_end ap
    178        t4 = inttodouble n
    179        t5 = t double/ t4
    180        return t5

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    181     t1 = c.26 int+ 1
    182     c.26 = t1
    183     return t1

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

 Code: 78 instruction(s)

    184     param 10
    185     t1 = call even(int), 1
    186     param 7
    187     t2 = call odd(int), 1
    188     param 15
    189     t3 = call fib(int), 1
    190     param 84
    191     param 36
    192     t4 = call gcd(int, int), 2
    193     param "%d %d %d %d\n"
    194     param t1
    195     param t2
    196     param t3
    197     param t4
    198     call printf, 5
    199     param 1
    200     t5 = call pick(int), 1
    201     param 1.0
    202     t6 = call pick(double), 1
    203     param "s"
    204     t7 = call pick(const char *), 1
    205     param "%d %d %d\n"
    206     param t5
    207     param t6
    208     param t7
    209     call printf, 4
    210     a = 1
    211     b = 2
    212     arr[0] = 7
    213     arr[4] = 8
    214     arr[8] = 9
    215     p = &arr
    216     t9 = &a
    217     *t9 = 30
    218     t11 = &b
    219     param t9
    220     param t11
    221     call swap(int &, int &), 2
    222     t12 = &p
    223     param t12
    224     call advance(int *&), 1
    225     param t9
    226     param t11
    227     t15 = call bigger(int &, int &), 2
    228     *t15 = 40
    229     t16 = *p
    230     t17 = 5.0
    231     t18 = &t17
    232     param t18
    233     t19 = call half(const double &), 1
    234     param "%d %d %d %.1f\n"
    235     param a
    236     param b
    237     param t16
    238     param t19
    239     call printf, 5
    240     param 4
    241     param 1
    242     param 2
    243     param 3
    244     param 4
    245     t20 = call sum(int, ...), 5
    246     param 3
    247     param 1.0
    248     param 2.0
    249     param 4.5
    250     t21 = call avg(int, ...), 4
    251     param "%d %.2f\n"
    252     param t20
    253     param t21
    254     call printf, 3
    255     call counter(), 0
    256     call counter(), 0
    257     t22 = call counter(), 0
    258     param "%d\n"
    259     param t22
    260     call printf, 2
    261     return 0


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
