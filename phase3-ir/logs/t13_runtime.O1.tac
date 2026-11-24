============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_runtime.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 127 -> 114 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          127 -> 114   (10% fewer)

   calls inlined                           2
   constants folded                       20
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           38
   temporaries merged away                 3
   dead instructions removed              25
   jumps removed or redirected             1
   unreachable instructions removed        0

============================================================================
 FUNCTION make(int)        (link name _Z4makei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 80 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   b                local   struct Big                     32       8
   t1               temp    double                          8      40
   t2               temp    double                          8      48
   t3               temp    int                             4      56
   t4               temp    char                            1      60
   t5               temp    long long                       8      64
   t6               temp    long long                       8      72

 Code: 11 instruction(s)

    100     t1 = inttodouble k
    101     t2 = t1 double* 1.5
    102     b[0] = t2
    103     b[16] = k
    104     t3 = 65 int+ k
    105     t4 = inttochar t3
    106     b[20] = t4
    107     t5 = inttollong k
    108     t6 = t5 llong* 10000000000
    109     b[24] = t6
    110     return b

============================================================================
 FUNCTION weigh(struct Big, double, char, int)        (link name _Z5weigh3Bigdci)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 6 temporaries, frame 96 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   b                param   struct Big                     32       0
   f                param   double                          8      32
   c                param   char                            1      40
   i                param   int                             4      44
   t1               temp    double                          8      48
   t2               temp    double                          8      56
   t3               temp    double                          8      64
   t4               temp    double                          8      72
   t5               temp    double                          8      80
   t6               temp    double                          8      88

 Code: 7 instruction(s)

    111     t1 = b[0]
    112     t2 = t1 double* f
    113     t3 = chartodouble c
    114     t4 = t2 double+ t3
    115     t5 = inttodouble i
    116     t6 = t4 double+ t5
    117     return t6

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

 Code: 16 instruction(s)

    118     va_start ap, n
    119     t1 = va_arg ap, double
    120     d = t1
    121     t2 = va_arg ap, llong
    122     w = t2
    123     t3 = va_arg ap, ptr
    124     s = t3
    125     va_end ap
    126     t4 = llongtodouble t2
    127     t5 = t1 double+ t4
    128     t6 = *t3
    129     t7 = chartodouble t6
    130     t8 = t5 double+ t7
    131     t9 = inttodouble n
    132     t10 = t8 double+ t9
    133     return t10

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

 Code: 80 instruction(s)

    134       big = 123456789012345
    135       other = 987654321098
    136       param "%lld %lld %llu %lld %lld\n"
    137       param 123456789012345
    138       param -17636684144620
    139       param 370370367037035
    140       param 122469134691247
    141       param -987654321099
    142       call printf, 6
    143       param "%.1f %lld %d\n"
    144       param 123456789012345.0
    145       param 39900000000
    146       param -2
    147       call printf, 4
    148       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%d]\n"
    149       param 3.14159
    150       param -2.5
    151       param 7.125
    152       param 0.5
    153       param 2
    154       call printf, 6
    155       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%c] [%%]\n"
    156       param -42
    157       param 42
    158       param -42
    159       param 255
    160       param 255
    161       param 8
    162       param 122
    163       call printf, 8
    164       param "%e %E %g %g %.3g\n"
    165       param 12345.678
    166       param 0.000123
    167       param 1e+05
    168       param 1e-05
    169       param 0.6666666666666666
    170       call printf, 6
    171       t28[0] = 3.0
    172       t28[16] = 2
    173       t28[20] = 67
    174       t28[24] = 20000000000
    175       s = t28
    176       t14 = s[0]
    177       t15 = s[16]
    178       t16 = s[20]
    179       t17 = chartoint t16
    180       t18 = s[24]
    181       t33 = s
    182       t37 = t33[0]
    183       t38 = t37 double* 2.0
    184       t40 = t38 double+ 97.0
    185       t42 = t40 double+ 5.0
    186       param "%.1f %d %c %lld %.1f\n"
    187       param t14
    188       param t15
    189       param t17
    190       param t18
    191       param t42
    192       call printf, 6
    193       param 1
    194       param 2.5
    195       param 3
    196       param "Z"
    197       t20 = call mix(int, ...), 4
    198       param "%.2f\n"
    199       param t20
    200       call printf, 2
    201       x = 2.0
    202       r = 1.0
    203       i = 0
    204  L1:  if i int>= 20 goto L2
    205       t21 = x double/ r
    206       t22 = r double+ t21
    207       r = t22 double/ 2.0
    208       i = i int+ 1
    209       goto L1
    210  L2:  param "%.10f\n"
    211       param r
    212       call printf, 2
    213       return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

123456789012345 -17636684144620 370370367037035 122469134691247 -987654321099
123456789012345.0 39900000000 -2
[  3.14] [-2.500  ] [00007.12] [0] [2]
[  -42] [42   ] [-0042] [ff] [FF] [10] [z] [%]
1.234568e+04 1.230000E-04 100000 1e-05 0.667
3.0 2 C 20000000000 108.0
96.50
1.4142135624

   exit code 0, 211 instructions executed
