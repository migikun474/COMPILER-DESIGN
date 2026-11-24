============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_runtime.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 127 instruction(s)

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
    126     t4 = llongtodouble w
    127     t5 = d double+ t4
    128     t6 = *s
    129     t7 = chartodouble t6
    130     t8 = t5 double+ t7
    131     t9 = inttodouble n
    132     t10 = t8 double+ t9
    133     return t10

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

    134       big = 123456789012345
    135       other = 987654321098
    136       t1 = llong- big
    137       t2 = t1 llong/ 7
    138       t3 = big ullong* 3
    139       t4 = big llong- other
    140       t5 = llong~ other
    141       param "%lld %lld %llu %lld %lld\n"
    142       param big
    143       param t2
    144       param t3
    145       param t4
    146       param t5
    147       call printf, 6
    148       t6 = llongtodouble big
    149       t7 = double- 2.7
    150       t8 = doubletoint t7
    151       param "%.1f %lld %d\n"
    152       param t6
    153       param 39900000000
    154       param t8
    155       call printf, 4
    156       t9 = double- 2.5
    157       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%d]\n"
    158       param 3.14159
    159       param t9
    160       param 7.125
    161       param 0.5
    162       param 2
    163       call printf, 6
    164       t10 = int- 42
    165       t11 = int- 42
    166       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%c] [%%]\n"
    167       param t10
    168       param 42
    169       param t11
    170       param 255
    171       param 255
    172       param 8
    173       param 122
    174       call printf, 8
    175       t12 = 2.0 double/ 3.0
    176       param "%e %E %g %g %.3g\n"
    177       param 12345.678
    178       param 0.000123
    179       param 1e+05
    180       param 1e-05
    181       param t12
    182       call printf, 6
    183       param 2
    184       t13 = call make(int), 1
    185       s = t13
    186       t14 = s[0]
    187       t15 = s[16]
    188       t16 = s[20]
    189       t17 = chartoint t16
    190       t18 = s[24]
    191       param s
    192       param 2.0
    193       param 97
    194       param 5
    195       t19 = call weigh(struct Big, double, char, int), 4
    196       param "%.1f %d %c %lld %.1f\n"
    197       param t14
    198       param t15
    199       param t17
    200       param t18
    201       param t19
    202       call printf, 6
    203       param 1
    204       param 2.5
    205       param 3
    206       param "Z"
    207       t20 = call mix(int, ...), 4
    208       param "%.2f\n"
    209       param t20
    210       call printf, 2
    211       x = 2.0
    212       r = 1.0
    213       i = 0
    214  L1:  if i int< 20 goto L2
    215       goto L3
    216  L2:  t21 = x double/ r
    217       t22 = r double+ t21
    218       t23 = t22 double/ 2.0
    219       r = t23
    220       t24 = i int+ 1
    221       i = t24
    222       goto L1
    223  L3:  param "%.10f\n"
    224       param r
    225       call printf, 2
    226       return 0


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
