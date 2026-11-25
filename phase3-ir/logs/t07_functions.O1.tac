============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 188 -> 200 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          188 -> 200   (-6% fewer)

   calls inlined                          17
   constants folded                        4
   algebraic simplifications               1
   common subexpressions                   4
   copies / constants forwarded           37
   temporaries merged away                13
   dead instructions removed              27
   jumps removed or redirected             9
   unreachable instructions removed        4

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   c.25             int                             4  0

 As three address code (initial values, in place before main runs):

    c.25 = 0

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
 FUNCTION sumv(int *, int)        (link name _Z4sumvPii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int *                           4       0
   n                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t3               temp    int *                           4      20
   t5               temp    int                             4      28
   (3 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    168        s = 0
    169  L15:  t1 = n
    170        n = n int- 1
    171        if t1 int== 0 goto L16
    172        t3 = v
    173        v = v ptr+ 4
    174        t5 = *t3
    175        s = s int+ t5
    176        goto L15
    177  L16:  return s

============================================================================
 FUNCTION sum(int *, int)        (link name _Z3sumPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int *                           4       0
   n                param   int                             4       4
   t2               temp    int *                           4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   t6               temp    int *                           4      28
   t7               temp    int                             4      32
   (1 temporary no longer used after optimization not shown)

 Code: 12 instruction(s)

    178        t2 = v
    179        t3 = n
    180        t4 = 0
    181  L17:  t5 = t3
    182        t3 = t3 int- 1
    183        if t5 int== 0 goto L18
    184        t6 = t2
    185        t2 = t2 ptr+ 4
    186        t7 = *t6
    187        t4 = t4 int+ t7
    188        goto L17
    189  L18:  return t4

============================================================================
 FUNCTION avg(double *, int)        (link name _Z3avgPdi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 72 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   double *                        4       0
   n                param   int                             4       4
   t                local   double                          8       8
   i                local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    double *                        4      24
   t3               temp    double                          8      32
   t6               temp    double                          8      56
   t7               temp    double                          8      64
   (2 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    190        t = 0.0
    191        i = 0
    192  L19:  if i int>= n goto L20
    193        t1 = i int<< 3
    194        t2 = v ptr+ t1
    195        t3 = *t2
    196        t = t double+ t3
    197        i = i int+ 1
    198        goto L19
    199  L20:  t6 = inttodouble n
    200        t7 = t double/ t6
    201        return t7

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    202     t1 = c.25 int+ 1
    203     c.25 = t1
    204     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 34 temporaries, frame 388 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   arr              local   int[3]                         12       8
   p                local   int *                           4      20
   ra               local   int &                           4      24
   nums             local   int[4]                         16      28
   ds               local   double[3]                      24      48
   t1               temp    int                             4      72
   t3               temp    int                             4      80
   t4               temp    int                             4      84
   t9               temp    int *                           4     104
   t11              temp    int *                           4     112
   t12              temp    int **                          4     116
   t16              temp    int                             4     132
   t17              temp    double                          8     136
   t18              temp    const double *                  4     144
   t20              temp    int *                           4     160
   t21              temp    int                             4     164
   t29              temp    int                             4     204
   t38              temp    int                             4     244
   t40              temp    int *                           4     252
   t41              temp    int *                           4     256
   t42              temp    int &                           4     260
   t43              temp    int &                           4     264
   t44              temp    int                             4     268
   t45              temp    int                             4     272
   t46              temp    int *                           4     276
   t48              temp    double                          8     288
   t49              temp    double                          8     296
   t53              temp    double *                        4     316
   t54              temp    int                             4     320
   t55              temp    double                          8     328
   t56              temp    int                             4     336
   t57              temp    int                             4     340
   t58              temp    double *                        4     344
   t59              temp    double                          8     352
   t60              temp    double                          8     360
   t61              temp    double                          8     368
   t62              temp    int                             4     376
   t63              temp    int                             4     380
   t64              temp    int                             4     384
   (30 temporaries no longer used after optimization not shown)

 Code: 95 instruction(s)

    205        param 9
    206        t1 = call odd(int), 1
    207        param 6
    208        t29 = call even(int), 1
    209        param 15
    210        t3 = call fib(int), 1
    211        param 84
    212        param 36
    213        t4 = call gcd(int, int), 2
    214        param "%d %d %d %d\n"
    215        param t1
    216        param t29
    217        param t3
    218        param t4
    219        call printf, 5
    220        param "%d %d %d\n"
    221        param 1
    222        param 2
    223        param 3
    224        call printf, 4
    225        a = 1
    226        b = 2
    227        arr[0] = 7
    228        arr[4] = 8
    229        arr[8] = 9
    230        p = &arr
    231        t9 = &a
    232        ra = t9
    233        *t9 = 30
    234        t11 = &b
    235        t38 = *t11
    236        *t9 = t38
    237        *t11 = 30
    238        t12 = &p
    239        t40 = *t12
    240        t41 = t40 ptr+ 4
    241        *t12 = t41
    242        t42 = t9
    243        t43 = t11
    244        t44 = *t9
    245        t45 = *t11
    246        if t44 int<= t45 goto L21
    247        t46 = t42
    248        goto L22
    249  L21:  t46 = t43
    250  L22:  *t46 = 40
    251        t16 = *p
    252        t17 = 5.0
    253        t18 = &t17
    254        t48 = *t18
    255        t49 = t48 double/ 2.0
    256        param "%d %d %d %.1f\n"
    257        param a
    258        param b
    259        param t16
    260        param t49
    261        call printf, 5
    262        nums[0] = 1
    263        nums[4] = 2
    264        nums[8] = 3
    265        nums[12] = 4
    266        ds[0] = 1.0
    267        ds[8] = 2.0
    268        ds[16] = 4.5
    269        t20 = &nums
    270        param t20
    271        param 4
    272        t21 = call sumv(int *, int), 2
    273        t53 = &ds
    274        t54 = 3
    275        t55 = 0.0
    276        t56 = 0
    277  L23:  if t56 int>= t54 goto L24
    278        t57 = t56 int<< 3
    279        t58 = t53 ptr+ t57
    280        t59 = *t58
    281        t55 = t55 double+ t59
    282        t56 = t56 int+ 1
    283        goto L23
    284  L24:  t60 = inttodouble t54
    285        t61 = t55 double/ t60
    286        param "%d %.2f\n"
    287        param t21
    288        param t61
    289        call printf, 3
    290        t62 = c.25 int+ 1
    291        c.25 = t62
    292        t63 = t62 int+ 1
    293        c.25 = t63
    294        t64 = t63 int+ 1
    295        c.25 = t64
    296        param "%d\n"
    297        param t64
    298        call printf, 2
    299        return 0


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
   sumv               function      int (int *, int)           -          17    -    1  _Z4sumvPii; defined
   sum                function      int (int *, int)           -          18    -    1  _Z3sumPii; defined
   avg                function      double (double *, int)     -          19    -    1  _Z3avgPdi; defined
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
   v                  parameter     int *                      param      17    4    1  v.16
   n                  parameter     int                        param      17    4    1  n.17
   s                  variable      int                        local      17    4    2  s.18

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int *                      param      18    4    1  v.19
   n                  parameter     int                        param      18    4    1  n.20

 scope: global > avg()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     double *                   param      19    4    1  v.21
   n                  parameter     int                        param      19    4    2  n.22
   t                  variable      double                     local      19    8    2  t.23
   i                  variable      int                        local      19    4    4  i.24

 scope: global > counter()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        static     20    4    1  c.25; static

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      24    4    4  a.26
   b                  variable      int                        local      24    4    3  b.27
   arr                variable      int[3]                     local      24   12    1  arr.28
   p                  variable      int *                      local      24    4    2  p.29
   ra                 variable      int &                      local      25    4    1  ra.30
   nums               variable      int[4]                     local      31   16    1  nums.31
   ds                 variable      double[3]                  local      32   24    1  ds.32

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

   exit code 0, 13058 instructions executed
