============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_runtime.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 119 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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
    108     t6 = 10000000000 llong* t5
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

 Symbol table: 6 parameter(s)/local(s), 24 temporaries, frame 268 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   big              local   long long                       8       0
   other            local   long long                       8       8
   s                local   struct Big                     32      16
   x                local   double                          8      48
   r                local   double                          8      56
   i                local   int                             4      64
   t1               temp    long long                       8      72
   t2               temp    long long                       8      80
   t3               temp    unsigned long long              8      88
   t4               temp    long long                       8      96
   t5               temp    long long                       8     104
   t6               temp    double                          8     112
   t7               temp    double                          8     120
   t8               temp    int                             4     128
   t9               temp    double                          8     136
   t10              temp    int                             4     144
   t11              temp    int                             4     148
   t12              temp    double                          8     152
   t13              temp    struct Big                     32     160
   t14              temp    double                          8     192
   t15              temp    int                             4     200
   t16              temp    char                            1     204
   t17              temp    int                             4     208
   t18              temp    long long                       8     216
   t19              temp    double                          8     224
   t20              temp    double                          8     232
   t21              temp    double                          8     240
   t22              temp    double                          8     248
   t23              temp    double                          8     256
   t24              temp    int                             4     264

 Code: 93 instruction(s)

    126       big = 123456789012345
    127       other = 987654321098
    128       t1 = llong- big
    129       t2 = t1 llong/ 7
    130       t3 = big ullong* 3
    131       t4 = big llong- other
    132       t5 = llong~ other
    133       param "%lld %lld %llu %lld %lld\n"
    134       param big
    135       param t2
    136       param t3
    137       param t4
    138       param t5
    139       call printf, 6
    140       t6 = llongtodouble big
    141       t7 = double- 2.7
    142       t8 = doubletoint t7
    143       param "%.1f %lld %d\n"
    144       param t6
    145       param 39900000000
    146       param t8
    147       call printf, 4
    148       t9 = double- 2.5
    149       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%d]\n"
    150       param 3.14159
    151       param t9
    152       param 7.125
    153       param 0.5
    154       param 2
    155       call printf, 6
    156       t10 = int- 42
    157       t11 = int- 42
    158       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%c] [%%]\n"
    159       param t10
    160       param 42
    161       param t11
    162       param 255
    163       param 255
    164       param 8
    165       param 122
    166       call printf, 8
    167       t12 = 2.0 double/ 3.0
    168       param "%e %E %g %g %.3g\n"
    169       param 12345.678
    170       param 0.000123
    171       param 1e+05
    172       param 1e-05
    173       param t12
    174       call printf, 6
    175       param 2
    176       t13 = call make(int), 1
    177       s = t13
    178       t14 = s[0]
    179       t15 = s[16]
    180       t16 = s[20]
    181       t17 = chartoint t16
    182       t18 = s[24]
    183       param s
    184       param 2.0
    185       param 97
    186       param 5
    187       t19 = call weigh(struct Big, double, char, int), 4
    188       param "%.1f %d %c %lld %.1f\n"
    189       param t14
    190       param t15
    191       param t17
    192       param t18
    193       param t19
    194       call printf, 6
    195       param 1
    196       param 2.5
    197       param 3
    198       param "Z"
    199       t20 = call mix(int, double, long long, char *), 4
    200       param "%.2f\n"
    201       param t20
    202       call printf, 2
    203       x = 2.0
    204       r = 1.0
    205       i = 0
    206  L1:  if i int< 20 goto L2
    207       goto L3
    208  L2:  t21 = x double/ r
    209       t22 = r double+ t21
    210       t23 = t22 double/ 2.0
    211       r = t23
    212       t24 = i int+ 1
    213       i = t24
    214       goto L1
    215  L3:  param "%.10f\n"
    216       param r
    217       call printf, 2
    218       return 0


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
