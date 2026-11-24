============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 184 -> 180 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          184 -> 180   (2% fewer)

   calls inlined                          14
   constants folded                        4
   algebraic simplifications               0
   common subexpressions                   4
   copies / constants forwarded           34
   temporaries merged away                10
   dead instructions removed              23
   jumps removed or redirected             9
   unreachable instructions removed        4

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

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 13 instruction(s)

    100       if n int!= 0 goto L1
    101       t1 = 1
    102       goto L4
    103  L1:  t2 = n int- 1
    104       t4 = t2
    105       if t2 int!= 0 goto L2
    106       t5 = 0
    107       goto L3
    108  L2:  t6 = t4 int- 1
    109       param t6
    110       t5 = call even(int), 1
    111  L3:  t1 = t5
    112  L4:  return t1

============================================================================
 FUNCTION odd(int)        (link name _Z3oddi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 13 instruction(s)

    113       if n int!= 0 goto L5
    114       t1 = 0
    115       goto L8
    116  L5:  t2 = n int- 1
    117       t4 = t2
    118       if t2 int!= 0 goto L6
    119       t5 = 1
    120       goto L7
    121  L6:  t6 = t4 int- 1
    122       param t6
    123       t5 = call odd(int), 1
    124  L7:  t1 = t5
    125  L8:  return t1

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

    126        if n int>= 2 goto L9
    127        t1 = n
    128        goto L10
    129  L9:   t2 = n int- 1
    130        param t2
    131        t3 = call fib(int), 1
    132        t4 = n int- 2
    133        param t4
    134        t5 = call fib(int), 1
    135        t1 = t3 int+ t5
    136  L10:  return t1

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

    137        if b int!= 0 goto L11
    138        t1 = a
    139        goto L12
    140  L11:  t2 = a int% b
    141        param b
    142        param t2
    143        t1 = call gcd(int, int), 2
    144  L12:  return t1

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0

 Code: 1 instruction(s)

    145     return 1

============================================================================
 FUNCTION pick(double)        (link name _Z4pickd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   double                          8       0

 Code: 1 instruction(s)

    146     return 2

============================================================================
 FUNCTION pick(const char *)        (link name _Z4pickPKc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   const char *                    4       0

 Code: 1 instruction(s)

    147     return 3

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

    148     t1 = *a
    149     t = t1
    150     t2 = *b
    151     *a = t2
    152     *b = t1
    153     return

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

    154     t1 = *p
    155     t2 = t1 ptr+ 4
    156     *p = t2
    157     return

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

    158        t2 = *a
    159        t3 = *b
    160        if t2 int<= t3 goto L13
    161        t1 = a
    162        goto L14
    163  L13:  t1 = b
    164  L14:  return t1

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

    165     t1 = *v
    166     t2 = t1 double/ 2.0
    167     return t2

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

    168        s = 0
    169  L15:  t1 = n
    170        n = n int- 1
    171        if t1 int== 0 goto L16
    172        t3 = va_arg ap, int
    173        s = s int+ t3
    174        goto L15
    175  L16:  return s

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
    182     return t1

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

    183        va_start ap, n
    184        t = 0.0
    185        i = 0
    186  L17:  if i int>= n goto L18
    187        t1 = va_arg ap, double
    188        t = t double+ t1
    189        i = i int+ 1
    190        goto L17
    191  L18:  va_end ap
    192        t4 = inttodouble n
    193        t5 = t double/ t4
    194        return t5

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    195     t1 = c.26 int+ 1
    196     c.26 = t1
    197     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 25 temporaries, frame 268 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   arr              local   int[3]                         12       8
   p                local   int *                           4      20
   ra               local   int &                           4      24
   t1               temp    int                             4      28
   t3               temp    int                             4      36
   t4               temp    int                             4      40
   t9               temp    int *                           4      60
   t11              temp    int *                           4      68
   t12              temp    int **                          4      72
   t16              temp    int                             4      88
   t17              temp    double                          8      96
   t18              temp    const double *                  4     104
   t20              temp    int                             4     120
   t21              temp    double                          8     128
   t27              temp    int                             4     156
   t36              temp    int                             4     196
   t38              temp    int *                           4     204
   t39              temp    int *                           4     208
   t40              temp    int &                           4     212
   t41              temp    int &                           4     216
   t42              temp    int                             4     220
   t43              temp    int                             4     224
   t44              temp    int *                           4     228
   t46              temp    double                          8     240
   t47              temp    double                          8     248
   t48              temp    int                             4     256
   t49              temp    int                             4     260
   t50              temp    int                             4     264
   (25 temporaries no longer used after optimization not shown)

 Code: 82 instruction(s)

    198        param 9
    199        t1 = call odd(int), 1
    200        param 6
    201        t27 = call even(int), 1
    202        param 15
    203        t3 = call fib(int), 1
    204        param 84
    205        param 36
    206        t4 = call gcd(int, int), 2
    207        param "%d %d %d %d\n"
    208        param t1
    209        param t27
    210        param t3
    211        param t4
    212        call printf, 5
    213        param "%d %d %d\n"
    214        param 1
    215        param 2
    216        param 3
    217        call printf, 4
    218        a = 1
    219        b = 2
    220        arr[0] = 7
    221        arr[4] = 8
    222        arr[8] = 9
    223        p = &arr
    224        t9 = &a
    225        ra = t9
    226        *t9 = 30
    227        t11 = &b
    228        t36 = *t11
    229        *t9 = t36
    230        *t11 = 30
    231        t12 = &p
    232        t38 = *t12
    233        t39 = t38 ptr+ 4
    234        *t12 = t39
    235        t40 = t9
    236        t41 = t11
    237        t42 = *t9
    238        t43 = *t11
    239        if t42 int<= t43 goto L19
    240        t44 = t40
    241        goto L20
    242  L19:  t44 = t41
    243  L20:  *t44 = 40
    244        t16 = *p
    245        t17 = 5.0
    246        t18 = &t17
    247        t46 = *t18
    248        t47 = t46 double/ 2.0
    249        param "%d %d %d %.1f\n"
    250        param a
    251        param b
    252        param t16
    253        param t47
    254        call printf, 5
    255        param 4
    256        param 1
    257        param 2
    258        param 3
    259        param 4
    260        t20 = call sum(int, ...), 5
    261        param 3
    262        param 1.0
    263        param 2.0
    264        param 4.5
    265        t21 = call avg(int, ...), 4
    266        param "%d %.2f\n"
    267        param t20
    268        param t21
    269        call printf, 3
    270        t48 = c.26 int+ 1
    271        c.26 = t48
    272        t49 = t48 int+ 1
    273        c.26 = t49
    274        t50 = t49 int+ 1
    275        c.26 = t50
    276        param "%d\n"
    277        param t50
    278        call printf, 2
    279        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

1 1 610 12
1 2 3
2 40 8 2.5
10 2.50
3

   exit code 0, 13052 instructions executed
