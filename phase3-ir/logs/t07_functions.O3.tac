============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 182 -> 158 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          182 -> 158   (13% fewer)

   constants folded                        2
   algebraic simplifications               0
   common subexpressions                   6
   copies / constants forwarded           38
   temporaries merged away                 5
   dead instructions removed              31
   jumps removed or redirected             5
   unreachable instructions removed        0
   propagated across blocks                2
   dead assignments removed                6
   calls inlined                          16
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         0

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

 Code: 6 instruction(s)

    118  L4:  if b int== 0 goto L5
    119       t1 = a int% b
    120       a = b
    121       b = t1
    122       goto L4
    123  L5:  return a

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0

 Code: 1 instruction(s)

    124     return 1

============================================================================
 FUNCTION pick(double)        (link name _Z4pickd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   double                          8       0

 Code: 1 instruction(s)

    125     return 2

============================================================================
 FUNCTION pick(char *)        (link name _Z4pickPc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   char *                          4       0

 Code: 1 instruction(s)

    126     return 3

============================================================================
 FUNCTION pick(int, int)        (link name _Z4pickii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4

 Code: 1 instruction(s)

    127     return 4

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

    128     t1 = *r
    129     t2 = t1 int+ 1
    130     *r = t2
    131     return

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

 Code: 5 instruction(s)

    132     t1 = *a
    133     t2 = *b
    134     *a = t2
    135     *b = t1
    136     return

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

    137       t1 = *a
    138       t2 = *b
    139       if t1 int<= t2 goto L6
    140       return a
    141  L6:  return b

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

    142     t1 = *v
    143     t2 = t1 double/ 2.0
    144     return t2

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

    145       va_start ap, n
    146       s = 0
    147       i = 0
    148  L7:  if i int>= n goto L8
    149       t1 = va_arg ap, int
    150       s = s int+ t1
    151       i = i int+ 1
    152       goto L7
    153  L8:  va_end ap
    154       return s

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

 Code: 7 instruction(s)

    155     va_start ap, n
    156     t1 = va_arg ap, double
    157     t2 = va_arg ap, int
    158     t3 = inttodouble t2
    159     t4 = t1 double+ t3
    160     va_end ap
    161     return t4

============================================================================
 FUNCTION counter()        (link name _Z7counterv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    162     t1 = calls.25 int+ 1
    163     calls.25 = t1
    164     return t1

============================================================================
 FUNCTION scale(int)        (link name _Z5scalei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    165     global = global int* k
    166     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 26 temporaries, frame 304 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   text             local   char[4]                         4       0
   x                local   int                             4       4
   y                local   int                             4       8
   alias            local   int &                           4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t11              temp    int *                           4      56
   t13              temp    int *                           4      64
   t15              temp    int                             4      72
   t16              temp    int                             4      76
   t19              temp    int &                           4      88
   t20              temp    double                          8      96
   t21              temp    const double *                  4     104
   t23              temp    int                             4     120
   t24              temp    int                             4     124
   t25              temp    double                          8     128
   t27              temp    double                          8     144
   t28              temp    double                          8     152
   t30              temp    int                             4     164
   t31              temp    int                             4     168
   t32              temp    int                             4     172
   t42              temp    int                             4     220
   t43              temp    int                             4     224
   t47              temp    int                             4     240
   t51              temp    int                             4     256
   t53              temp    double                          8     264
   t54              temp    double                          8     272
   t55              temp    int                             4     280
   t56              temp    int                             4     284
   t57              temp    int                             4     288
   (34 temporaries no longer used after optimization not shown)

 Code: 89 instruction(s)

    167        param 6
    168        t1 = call fact(int), 1
    169        param 10
    170        t2 = call fib(int), 1
    171        t30 = 84
    172        t31 = 36
    173  L9:   if t31 int== 0 goto L10
    174        t32 = t30 int% t31
    175        t30 = t31
    176        t31 = t32
    177        goto L9
    178  L10:  param "%d %d %d %d\n"
    179        param t1
    180        param t2
    181        param t30
    182        param 44
    183        call printf, 5
    184        text[0] = 97
    185        text[1] = 98
    186        text[2] = 99
    187        text[3] = 0
    188        param "%d %d %d %d %d\n"
    189        param 1
    190        param 2
    191        param 3
    192        param 4
    193        param 1
    194        call printf, 6
    195        x = 5
    196        y = 9
    197        t11 = &x
    198        t42 = *t11
    199        t43 = t42 int+ 1
    200        *t11 = t43
    201        t13 = &y
    202        t47 = *t13
    203        *t11 = t47
    204        *t13 = t43
    205        t15 = *t11
    206        t16 = t15 int+ 100
    207        *t11 = t16
    208        t51 = *t13
    209        if t16 int<= t51 goto L11
    210        t19 = t11
    211        goto L12
    212  L11:  t19 = t13
    213  L12:  *t19 = 0
    214        t20 = 5.0
    215        t21 = &t20
    216        t53 = *t21
    217        t54 = t53 double/ 2.0
    218        param "%d %d %.2f\n"
    219        param x
    220        param y
    221        param t54
    222        call printf, 4
    223        param 3
    224        param 10
    225        param 20
    226        param 30
    227        t23 = call sum(int, ...), 4
    228        param 0
    229        t24 = call sum(int, ...), 1
    230        param 2
    231        param 1.5
    232        param 4
    233        t25 = call mix(int, ...), 3
    234        param "%d %d %.1f\n"
    235        param t23
    236        param t24
    237        param t25
    238        call printf, 4
    239        t55 = calls.25 int+ 1
    240        calls.25 = t55
    241        t56 = t55 int+ 1
    242        calls.25 = t56
    243        t57 = t56 int+ 1
    244        calls.25 = t57
    245        param "%d\n"
    246        param t57
    247        call printf, 2
    248        global = global int* 3
    249        t27 = inttodouble global
    250        t28 = ratio double* t27
    251        param "%d %.1f\n"
    252        param global
    253        param t28
    254        call printf, 3
    255        return 11

============================================================================
 FUNCTION later(int)        (link name _Z5lateri)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    256     t1 = n int* 11
    257     return t1


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
