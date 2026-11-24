============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 184 -> 157 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          184 -> 157   (14% fewer)

   constants folded                        4
   algebraic simplifications               0
   common subexpressions                   4
   copies / constants forwarded           37
   temporaries merged away                11
   dead instructions removed              24
   jumps removed or redirected            10
   unreachable instructions removed        4
   propagated across blocks                5
   dead assignments removed                8
   calls inlined                          15
   tail calls turned into jumps            1
   common subexpressions across blocks      0
   loops unrolled                          4
   unreachable functions removed           9

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

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t5               temp    int                             4      20
   t6               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    100       if n int!= 0 goto L1
    101       t1 = 1
    102       goto L4
    103  L1:  t2 = n int- 1
    104       if t2 int!= 0 goto L2
    105       t5 = 0
    106       goto L3
    107  L2:  t6 = t2 int- 1
    108       param t6
    109       t5 = call even(int), 1
    110  L3:  t1 = t5
    111  L4:  return t1

============================================================================
 FUNCTION odd(int)        (link name _Z3oddi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t5               temp    int                             4      20
   t6               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    112       if n int!= 0 goto L5
    113       t1 = 0
    114       goto L8
    115  L5:  t2 = n int- 1
    116       if t2 int!= 0 goto L6
    117       t5 = 1
    118       goto L7
    119  L6:  t6 = t2 int- 1
    120       param t6
    121       t5 = call odd(int), 1
    122  L7:  t1 = t5
    123  L8:  return t1

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

    124        if n int>= 2 goto L9
    125        t1 = n
    126        goto L10
    127  L9:   t2 = n int- 1
    128        param t2
    129        t3 = call fib(int), 1
    130        t4 = n int- 2
    131        param t4
    132        t5 = call fib(int), 1
    133        t1 = t3 int+ t5
    134  L10:  return t1

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

 Code: 13 instruction(s)

    135        s = 0
    136  L11:  t1 = n
    137        n = n int- 1
    138        if t1 int== 0 goto L12
    139        t3 = va_arg ap, int
    140        s = s int+ t3
    141        t1 = n
    142        n = n int- 1
    143        if t1 int== 0 goto L12
    144        t3 = va_arg ap, int
    145        s = s int+ t3
    146        goto L11
    147  L12:  return s

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

    148     va_start ap, n
    149     param ap
    150     param n
    151     t1 = call sumv(va_list, int), 2
    152     va_end ap
    153     return t1

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

 Code: 16 instruction(s)

    154        va_start ap, n
    155        t = 0.0
    156        i = 0
    157  L13:  if i int>= n goto L14
    158        t1 = va_arg ap, double
    159        t = t double+ t1
    160        i = i int+ 1
    161        if i int>= n goto L14
    162        t1 = va_arg ap, double
    163        t = t double+ t1
    164        i = i int+ 1
    165        goto L13
    166  L14:  va_end ap
    167        t4 = inttodouble n
    168        t5 = t double/ t4
    169        return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 25 temporaries, frame 276 bytes

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
   t9               temp    int *                           4      60
   t11              temp    int *                           4      68
   t12              temp    int **                          4      72
   t16              temp    int                             4      88
   t17              temp    double                          8      96
   t18              temp    const double *                  4     104
   t20              temp    int                             4     120
   t21              temp    double                          8     128
   t29              temp    int                             4     164
   t30              temp    int                             4     168
   t31              temp    int                             4     172
   t38              temp    int                             4     208
   t40              temp    int *                           4     216
   t41              temp    int *                           4     220
   t44              temp    int                             4     232
   t45              temp    int                             4     236
   t46              temp    int *                           4     240
   t48              temp    double                          8     248
   t49              temp    double                          8     256
   t50              temp    int                             4     264
   t51              temp    int                             4     268
   t52              temp    int                             4     272
   (27 temporaries no longer used after optimization not shown)

 Code: 87 instruction(s)

    170        param 9
    171        t1 = call odd(int), 1
    172        param 6
    173        t2 = call even(int), 1
    174        param 15
    175        t3 = call fib(int), 1
    176        t29 = 84
    177        t30 = 36
    178  L15:  if t30 int== 0 goto L16
    179        t31 = t29 int% t30
    180        t29 = t30
    181        t30 = t31
    182        if t31 int== 0 goto L16
    183        t31 = t29 int% t30
    184        t29 = t30
    185        t30 = t31
    186        goto L15
    187  L16:  param "%d %d %d %d\n"
    188        param t1
    189        param t2
    190        param t3
    191        param t29
    192        call printf, 5
    193        param "%d %d %d\n"
    194        param 1
    195        param 2
    196        param 3
    197        call printf, 4
    198        a = 1
    199        b = 2
    200        arr[0] = 7
    201        arr[4] = 8
    202        arr[8] = 9
    203        p = &arr
    204        t9 = &a
    205        *t9 = 30
    206        t11 = &b
    207        t38 = *t11
    208        *t9 = t38
    209        *t11 = 30
    210        t12 = &p
    211        t40 = *t12
    212        t41 = t40 ptr+ 4
    213        *t12 = t41
    214        t44 = *t9
    215        t45 = *t11
    216        if t44 int<= t45 goto L17
    217        t46 = t9
    218        goto L18
    219  L17:  t46 = t11
    220  L18:  *t46 = 40
    221        t16 = *p
    222        t17 = 5.0
    223        t18 = &t17
    224        t48 = *t18
    225        t49 = t48 double/ 2.0
    226        param "%d %d %d %.1f\n"
    227        param a
    228        param b
    229        param t16
    230        param t49
    231        call printf, 5
    232        param 4
    233        param 1
    234        param 2
    235        param 3
    236        param 4
    237        t20 = call sum(int, ...), 5
    238        param 3
    239        param 1.0
    240        param 2.0
    241        param 4.5
    242        t21 = call avg(int, ...), 4
    243        param "%d %.2f\n"
    244        param t20
    245        param t21
    246        call printf, 3
    247        t50 = c.26 int+ 1
    248        c.26 = t50
    249        t51 = t50 int+ 1
    250        c.26 = t51
    251        t52 = t51 int+ 1
    252        c.26 = t52
    253        param "%d\n"
    254        param t52
    255        call printf, 2
    256        return 0


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
