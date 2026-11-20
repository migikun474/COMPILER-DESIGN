============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t07_functions.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 182 -> 132 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          182 -> 132   (27% fewer)

   constants folded                        2
   algebraic simplifications               0
   common subexpressions                   6
   copies / constants forwarded           40
   temporaries merged away                 5
   dead instructions removed              31
   jumps removed or redirected             5
   unreachable instructions removed        0
   propagated across blocks                2
   dead assignments removed                6
   calls inlined                          16
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          3
   unreachable functions removed          12

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

 Code: 14 instruction(s)

    118       va_start ap, n
    119       s = 0
    120       i = 0
    121  L4:  if i int>= n goto L5
    122       t1 = va_arg ap, int
    123       s = s int+ t1
    124       i = i int+ 1
    125       if i int>= n goto L5
    126       t1 = va_arg ap, int
    127       s = s int+ t1
    128       i = i int+ 1
    129       goto L4
    130  L5:  va_end ap
    131       return s

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

    132     va_start ap, n
    133     t1 = va_arg ap, double
    134     t2 = va_arg ap, int
    135     t3 = inttodouble t2
    136     t4 = t1 double+ t3
    137     va_end ap
    138     return t4

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

 Code: 93 instruction(s)

    139       param 6
    140       t1 = call fact(int), 1
    141       param 10
    142       t2 = call fib(int), 1
    143       t30 = 84
    144       t31 = 36
    145  L6:  if t31 int== 0 goto L7
    146       t32 = t30 int% t31
    147       t30 = t31
    148       t31 = t32
    149       if t32 int== 0 goto L7
    150       t32 = t30 int% t31
    151       t30 = t31
    152       t31 = t32
    153       goto L6
    154  L7:  param "%d %d %d %d\n"
    155       param t1
    156       param t2
    157       param t30
    158       param 44
    159       call printf, 5
    160       text[0] = 97
    161       text[1] = 98
    162       text[2] = 99
    163       text[3] = 0
    164       param "%d %d %d %d %d\n"
    165       param 1
    166       param 2
    167       param 3
    168       param 4
    169       param 1
    170       call printf, 6
    171       x = 5
    172       y = 9
    173       t11 = &x
    174       t42 = *t11
    175       t43 = t42 int+ 1
    176       *t11 = t43
    177       t13 = &y
    178       t47 = *t13
    179       *t11 = t47
    180       *t13 = t43
    181       t15 = *t11
    182       t16 = t15 int+ 100
    183       *t11 = t16
    184       t51 = *t13
    185       if t16 int<= t51 goto L8
    186       t19 = t11
    187       goto L9
    188  L8:  t19 = t13
    189  L9:  *t19 = 0
    190       t20 = 5.0
    191       t21 = &t20
    192       t53 = *t21
    193       t54 = t53 double/ 2.0
    194       param "%d %d %.2f\n"
    195       param x
    196       param y
    197       param t54
    198       call printf, 4
    199       param 3
    200       param 10
    201       param 20
    202       param 30
    203       t23 = call sum(int, ...), 4
    204       param 0
    205       t24 = call sum(int, ...), 1
    206       param 2
    207       param 1.5
    208       param 4
    209       t25 = call mix(int, ...), 3
    210       param "%d %d %.1f\n"
    211       param t23
    212       param t24
    213       param t25
    214       call printf, 4
    215       t55 = calls.25 int+ 1
    216       calls.25 = t55
    217       t56 = t55 int+ 1
    218       calls.25 = t56
    219       t57 = t56 int+ 1
    220       calls.25 = t57
    221       param "%d\n"
    222       param t57
    223       call printf, 2
    224       global = global int* 3
    225       t27 = inttodouble global
    226       t28 = ratio double* t27
    227       param "%d %.1f\n"
    228       param global
    229       param t28
    230       call printf, 3
    231       return 11


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   later              function      int (int)                  -           4    -    2  _Z5lateri; defined
   fact               function      int (int)                  -           6    -    2  _Z4facti; defined
   fib                function      int (int)                  -           7    -    3  _Z3fibi; defined
   gcd                function      int (int, int)             -           8    -    1  _Z3gcdii; defined
   pick               function      int (int)                  -          10    -    2  _Z4picki; defined
   pick               function      int (double)               -          11    -    1  _Z4pickd; defined
   pick               function      int (char *)               -          12    -    1  _Z4pickPc; defined
   pick               function      int (int, int)             -          13    -    1  _Z4pickii; defined
   bump               function      void (int &)               -          15    -    1  _Z4bumpRi; defined
   exchange           function      void (int &, int &)        -          16    -    1  _Z8exchangeRiS_; defined
   largest            function      int &(int &, int &)        -          17    -    1  _Z7largestRiS_; defined
   half               function      double (const double &)    -          18    -    1  _Z4halfRKd; defined
   sum                function      int (int, ...)             -          20    -    2  _Z3sumiz; defined
   mix                function      double (int, ...)          -          29    -    1  _Z3mixiz; defined
   counter            function      int (void)                 -          37    -    3  _Z7counterv; defined
   global             variable      int                        global     43    4    4  
   ratio              variable      double                     global     44    8    1  
   scale              function      void (int)                 -          45    -    1  _Z5scalei; defined
   main               function      int (void)                 -          47    -    0  defined

 scope: global > fact()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       6    4    3  n.1

 scope: global > fib()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       7    4    4  n.2

 scope: global > gcd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param       8    4    3  a.3
   b                  parameter     int                        param       8    4    4  b.4

 scope: global > gcd() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int                        local       8    4    1  t.5

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      10    4    0  a.6
   a                  parameter     double                     param      11    8    0  a.7
   s                  parameter     char *                     param      12    4    0  s.8
   a                  parameter     int                        param      13    4    0  a.9
   b                  parameter     int                        param      13    4    0  b.10

 scope: global > bump()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param      15    4    2  r.11

 scope: global > exchange()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      16    4    2  a.12
   b                  parameter     int &                      param      16    4    2  b.13
   t                  variable      int                        local      16    4    1  t.14

 scope: global > largest()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int &                      param      17    4    2  a.15
   b                  parameter     int &                      param      17    4    2  b.16

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const double &             param      18    4    1  v.17

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      20    4    2  n.18
   ap                 variable      va_list                    local      21    4    3  ap.19
   s                  variable      int                        local      23    4    2  s.20

 scope: global > sum() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      24    4    2  i.21

 scope: global > mix()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      29    4    1  n.22
   ap                 variable      va_list                    local      30    4    4  ap.23
   s                  variable      double                     local      32    8    1  s.24

 scope: global > counter()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        static     38    4    2  calls.25; static

 scope: global > scale()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      45    4    1  k.26

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   text               variable      char[4]                    local      49    4    1  text.27
   x                  variable      int                        local      52    4    5  x.28
   y                  variable      int                        local      52    4    3  y.29
   alias              variable      int &                      local      55    4    2  alias.30

 scope: global > later()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      68    4    1  n.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
