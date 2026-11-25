============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_runtime.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 119 -> 105 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          119 -> 105   (11% fewer)

   calls inlined                           3
   constants folded                       23
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           43
   temporaries merged away                 3
   dead instructions removed              33
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
 FUNCTION mix(int, double, long long, char *)        (link name _Z3mixidxPc)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 7 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   d                param   double                          8       8
   w                param   long long                       8      16
   s                param   char *                          4      24
   t1               temp    double                          8      32
   t2               temp    double                          8      40
   t3               temp    char                            1      48
   t4               temp    double                          8      56
   t5               temp    double                          8      64
   t6               temp    double                          8      72
   t7               temp    double                          8      80

 Code: 8 instruction(s)

    118     t1 = llongtodouble w
    119     t2 = d double+ t1
    120     t3 = *s
    121     t4 = chartodouble t3
    122     t5 = t2 double+ t4
    123     t6 = inttodouble n
    124     t7 = t5 double+ t6
    125     return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 17 temporaries, frame 528 bytes

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
   t21              temp    double                          8     240
   t22              temp    double                          8     248
   t28              temp    struct Big                     32     288
   t33              temp    struct Big                     32     344
   t37              temp    double                          8     392
   t38              temp    double                          8     400
   t40              temp    double                          8     416
   t42              temp    double                          8     432
   t49              temp    char                            1     488
   t50              temp    double                          8     496
   t51              temp    double                          8     504
   t53              temp    double                          8     520
   (36 temporaries no longer used after optimization not shown)

 Code: 79 instruction(s)

    126       big = 123456789012345
    127       other = 987654321098
    128       param "%lld %lld %llu %lld %lld\n"
    129       param 123456789012345
    130       param -17636684144620
    131       param 370370367037035
    132       param 122469134691247
    133       param -987654321099
    134       call printf, 6
    135       param "%.1f %lld %d\n"
    136       param 123456789012345.0
    137       param 39900000000
    138       param -2
    139       call printf, 4
    140       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%d]\n"
    141       param 3.14159
    142       param -2.5
    143       param 7.125
    144       param 0.5
    145       param 2
    146       call printf, 6
    147       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%c] [%%]\n"
    148       param -42
    149       param 42
    150       param -42
    151       param 255
    152       param 255
    153       param 8
    154       param 122
    155       call printf, 8
    156       param "%e %E %g %g %.3g\n"
    157       param 12345.678
    158       param 0.000123
    159       param 1e+05
    160       param 1e-05
    161       param 0.6666666666666666
    162       call printf, 6
    163       t28[0] = 3.0
    164       t28[16] = 2
    165       t28[20] = 67
    166       t28[24] = 20000000000
    167       s = t28
    168       t14 = s[0]
    169       t15 = s[16]
    170       t16 = s[20]
    171       t17 = chartoint t16
    172       t18 = s[24]
    173       t33 = s
    174       t37 = t33[0]
    175       t38 = t37 double* 2.0
    176       t40 = t38 double+ 97.0
    177       t42 = t40 double+ 5.0
    178       param "%.1f %d %c %lld %.1f\n"
    179       param t14
    180       param t15
    181       param t17
    182       param t18
    183       param t42
    184       call printf, 6
    185       t49 = *"Z"
    186       t50 = chartodouble t49
    187       t51 = 5.5 double+ t50
    188       t53 = t51 double+ 1.0
    189       param "%.2f\n"
    190       param t53
    191       call printf, 2
    192       x = 2.0
    193       r = 1.0
    194       i = 0
    195  L1:  if i int>= 20 goto L2
    196       t21 = x double/ r
    197       t22 = r double+ t21
    198       r = t22 double/ 2.0
    199       i = i int+ 1
    200       goto L1
    201  L2:  param "%.10f\n"
    202       param r
    203       call printf, 2
    204       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Big                struct_tag    struct Big                 -           5    -    0  size 32
   make               function      struct Big (int)           -           6    -    1  _Z4makei; defined
   weigh              function      double (struct Big, double, char, int) -           7    -    1  _Z5weigh3Bigdci; defined
   mix                function      double (int, double, long long, char *) -           8    -    1  _Z3mixidxPc; defined
   main               function      int (void)                 -           9    -    0  defined

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
   n                  parameter     int                        param       8    4    1  n.7
   d                  parameter     double                     param       8    8    1  d.8
   w                  parameter     long long                  param       8    8    1  w.9
   s                  parameter     char *                     param       8    4    1  s.10

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   big                variable      long long                  local      10    8    5  big.11
   other              variable      long long                  local      11    8    2  other.12
   s                  variable      struct Big                 local      17   32    5  s.13
   x                  variable      double                     local      20    8    1  x.14
   r                  variable      double                     local      20    8    4  r.15
   i                  variable      int                        local      21    4    3  i.16

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

   exit code 0, 194 instructions executed
