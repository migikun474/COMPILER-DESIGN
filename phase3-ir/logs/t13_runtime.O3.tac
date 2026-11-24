============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_runtime.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 127 -> 95 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          127 -> 95   (25% fewer)

   constants folded                       20
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           38
   temporaries merged away                 3
   dead instructions removed              25
   jumps removed or redirected             1
   unreachable instructions removed        0
   propagated across blocks                1
   dead assignments removed                6
   calls inlined                           2
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          1
   unreachable functions removed           2

============================================================================
 FUNCTION mix(int, ...)        (link name _Z3mixiz)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 10 temporaries, frame 112 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   d                local   double                          8       8
   w                local   long long                       8      16
   s                local   char *                          4      24
   t1               temp    double                          8      32
   t2               temp    long long                       8      40
   t3               temp    char *                          4      48
   t4               temp    double                          8      56
   t5               temp    double                          8      64
   t6               temp    char                            1      72
   t7               temp    double                          8      80
   t8               temp    double                          8      88
   t9               temp    double                          8      96
   t10              temp    double                          8     104

 Code: 13 instruction(s)

    100     va_start ap, n
    101     t1 = va_arg ap, double
    102     t2 = va_arg ap, llong
    103     t3 = va_arg ap, ptr
    104     va_end ap
    105     t4 = llongtodouble t2
    106     t5 = t1 double+ t4
    107     t6 = *t3
    108     t7 = chartodouble t6
    109     t8 = t5 double+ t7
    110     t9 = inttodouble n
    111     t10 = t8 double+ t9
    112     return t10

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 14 temporaries, frame 440 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   big              local   long long                       8       0
   other            local   long long                       8       8
   s                local   struct Big                     32      16
   x                local   double                          8      48
   r                local   double                          8      56
   i                local   int                             4      64
   t14              temp    double                          8     192
   t15              temp    int                             4     200
   t16              temp    char                            1     204
   t17              temp    int                             4     208
   t18              temp    long long                       8     216
   t20              temp    double                          8     232
   t21              temp    double                          8     240
   t22              temp    double                          8     248
   t28              temp    struct Big                     32     288
   t33              temp    struct Big                     32     344
   t37              temp    double                          8     392
   t38              temp    double                          8     400
   t40              temp    double                          8     416
   t42              temp    double                          8     432
   (28 temporaries no longer used after optimization not shown)

 Code: 82 instruction(s)

    113       param "%lld %lld %llu %lld %lld\n"
    114       param 123456789012345
    115       param -17636684144620
    116       param 370370367037035
    117       param 122469134691247
    118       param -987654321099
    119       call printf, 6
    120       param "%.1f %lld %d\n"
    121       param 123456789012345.0
    122       param 39900000000
    123       param -2
    124       call printf, 4
    125       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%d]\n"
    126       param 3.14159
    127       param -2.5
    128       param 7.125
    129       param 0.5
    130       param 2
    131       call printf, 6
    132       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%c] [%%]\n"
    133       param -42
    134       param 42
    135       param -42
    136       param 255
    137       param 255
    138       param 8
    139       param 122
    140       call printf, 8
    141       param "%e %E %g %g %.3g\n"
    142       param 12345.678
    143       param 0.000123
    144       param 1e+05
    145       param 1e-05
    146       param 0.6666666666666666
    147       call printf, 6
    148       t28[0] = 3.0
    149       t28[16] = 2
    150       t28[20] = 67
    151       t28[24] = 20000000000
    152       s = t28
    153       t14 = s[0]
    154       t15 = s[16]
    155       t16 = s[20]
    156       t17 = chartoint t16
    157       t18 = s[24]
    158       t33 = s
    159       t37 = t33[0]
    160       t38 = t37 double* 2.0
    161       t40 = t38 double+ 97.0
    162       t42 = t40 double+ 5.0
    163       param "%.1f %d %c %lld %.1f\n"
    164       param t14
    165       param t15
    166       param t17
    167       param t18
    168       param t42
    169       call printf, 6
    170       param 1
    171       param 2.5
    172       param 3
    173       param "Z"
    174       t20 = call mix(int, ...), 4
    175       param "%.2f\n"
    176       param t20
    177       call printf, 2
    178       r = 1.0
    179       i = 0
    180  L1:  if i int>= 20 goto L2
    181       t21 = 2.0 double/ r
    182       t22 = r double+ t21
    183       r = t22 double/ 2.0
    184       i = i int+ 1
    185       if i int>= 20 goto L2
    186       t21 = 2.0 double/ r
    187       t22 = r double+ t21
    188       r = t22 double/ 2.0
    189       i = i int+ 1
    190       goto L1
    191  L2:  param "%.10f\n"
    192       param r
    193       call printf, 2
    194       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Big                struct_tag    struct Big                 -           5    -    0  size 32
   make               function      struct Big (int)           -           6    -    1  _Z4makei; defined
   weigh              function      double (struct Big, double, char, int) -           7    -    1  _Z5weigh3Bigdci; defined
   mix                function      double (int, ...)          -           8    -    1  _Z3mixiz; defined
   main               function      int (void)                 -          14    -    0  defined

 scope: global > struct Big
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  field         double                     member      5    8    3  Big::d; public, offset 0
   n                  field         int[3]                     member      5   12    2  Big::n; public, offset 8
   tag                field         char                       member      5    1    2  Big::tag; public, offset 20
   w                  field         long long                  member      5    8    2  Big::w; public, offset 24

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param       6    4    4  k.1
   b                  variable      struct Big                 local       6   32    5  b.2

 scope: global > weigh()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  parameter     struct Big                 param       7   32    1  b.3
   f                  parameter     double                     param       7    8    1  f.4
   c                  parameter     char                       param       7    1    1  c.5
   i                  parameter     int                        param       7    4    1  i.6

 scope: global > mix()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       8    4    2  n.7
   ap                 variable      va_list                    local       9    4    5  ap.8
   d                  variable      double                     local      10    8    1  d.9
   w                  variable      long long                  local      10    8    1  w.10
   s                  variable      char *                     local      10    4    1  s.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   big                variable      long long                  local      15    8    5  big.12
   other              variable      long long                  local      16    8    2  other.13
   s                  variable      struct Big                 local      22   32    5  s.14
   x                  variable      double                     local      25    8    1  x.15
   r                  variable      double                     local      25    8    4  r.16
   i                  variable      int                        local      26    4    3  i.17

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Big: size 32, align 8
    +0  double d  [public]
    +8  int[3] n  [public]
    +20  char tag  [public]
    +24  long long w  [public]
