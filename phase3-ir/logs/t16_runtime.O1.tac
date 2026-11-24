============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_runtime.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 314 -> 243 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          314 -> 243   (22% fewer)

   constants folded                       47
   algebraic simplifications               1
   common subexpressions                   1
   copies / constants forwarded          109
   temporaries merged away                 5
   dead instructions removed              48
   jumps removed or redirected             9
   unreachable instructions removed       10

============================================================================
 FUNCTION make(int)        (link name _Z4makei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 9 temporaries, frame 112 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   b                local   struct Big                     40       8
   i                local   int                             4      48
   t1               temp    double                          8      56
   t2               temp    double                          8      64
   t3               temp    int                             4      72
   t4               temp    int                             4      76
   t5               temp    int                             4      80
   t7               temp    int                             4      88
   t8               temp    char                            1      92
   t9               temp    long long                       8      96
   t10              temp    long long                       8     104
   (1 temporary no longer used after optimization not shown)

 Code: 18 instruction(s)

    100       t1 = inttodouble k
    101       t2 = t1 double* 1.5
    102       b[0] = t2
    103       i = 0
    104  L1:  if i int>= 5 goto L2
    105       t3 = i int<< 2                      (w = 4)
    106       t4 = 8 int+ t3
    107       t5 = k int+ i
    108       b[t4] = t5
    109       i = i int+ 1
    110       goto L1
    111  L2:  t7 = 65 int+ k
    112       t8 = inttochar t7
    113       b[28] = t8
    114       t9 = inttollong k
    115       t10 = t9 llong* 10000000000
    116       b[32] = t10
    117       return b

============================================================================
 FUNCTION weigh(struct Big, double, char, long long)        (link name _Z5weigh3Bigdcx)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 13 temporaries, frame 168 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   b                param   struct Big                     40       0
   scale            param   double                          8      40
   c                param   char                            1      48
   extra            param   long long                       8      56
   t1               temp    double                          8      64
   t2               temp    double                          8      72
   t3               temp    int                             4      80
   t4               temp    double                          8      88
   t5               temp    double                          8      96
   t6               temp    double                          8     104
   t7               temp    double                          8     112
   t8               temp    long long                       8     120
   t9               temp    long long                       8     128
   t10              temp    double                          8     136
   t11              temp    double                          8     144
   t12              temp    double                          8     152
   t13              temp    double                          8     160

 Code: 14 instruction(s)

    118     t1 = b[0]
    119     t2 = t1 double* scale
    120     t3 = b[24]
    121     t4 = inttodouble t3
    122     t5 = t2 double+ t4
    123     t6 = chartodouble c
    124     t7 = t5 double+ t6
    125     t8 = b[32]
    126     t9 = t8 llong/ 1000000000
    127     t10 = llongtodouble t9
    128     t11 = t7 double+ t10
    129     t12 = llongtodouble extra
    130     t13 = t11 double+ t12
    131     return t13

============================================================================
 FUNCTION average(int, ...)        (link name _Z7averageiz)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 5 temporaries, frame 96 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   count            param   int                             4       0
   ap               local   va_list                         4       4
   total            local   double                          8       8
   i                local   int                             4      16
   tail             local   long long                       8      24
   label            local   char *                          4      32
   t1               temp    double                          8      40
   t4               temp    long long                       8      64
   t5               temp    char *                          4      72
   t6               temp    double                          8      80
   t7               temp    double                          8      88
   (2 temporaries no longer used after optimization not shown)

 Code: 20 instruction(s)

    132       va_start ap, count
    133       total = 0.0
    134       i = 0
    135  L3:  if i int>= count goto L4
    136       t1 = va_arg ap, double
    137       total = total double+ t1
    138       i = i int+ 1
    139       goto L3
    140  L4:  t4 = va_arg ap, llong
    141       tail = t4
    142       t5 = va_arg ap, ptr
    143       label = t5
    144       va_end ap
    145       param "%s %lld\n"
    146       param t5
    147       param t4
    148       call printf, 3
    149       t6 = inttodouble count
    150       t7 = total double/ t6
    151       return t7

============================================================================
 FUNCTION power(long long, int)        (link name _Z5powerxi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   base             param   long long                       8       0
   n                param   int                             4       8
   t1               temp    long long                       8      16
   t2               temp    int                             4      24
   t3               temp    long long                       8      32
   (1 temporary no longer used after optimization not shown)

 Code: 9 instruction(s)

    152       if n int!= 0 goto L5
    153       t1 = 1
    154       goto L6
    155  L5:  t2 = n int- 1
    156       param base
    157       param t2
    158       t3 = call power(long long, int), 2
    159       t1 = base llong* t3
    160  L6:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 16 parameter(s)/local(s), 26 temporaries, frame 684 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   long long                       8       0
   b                local   long long                       8       8
   u                local   unsigned long long              8      16
   i                local   int                             4      24
   big              local   unsigned int                    4      28
   d                local   double                          8      32
   e                local   double                          8      40
   f                local   double                          8      48
   fl               local   float                           4      56
   x                local   float                           4      60
   y                local   float                           4      64
   s                local   struct Big                     40      72
   t                local   struct Big                     40     112
   p                local   int *                           4     152
   z                local   int *                           4     156
   none             local   int *                           4     160
   t22              temp    long long                       8     320
   t48              temp    double                          8     552
   t49              temp    int                             4     560
   t51              temp    char                            1     568
   t52              temp    int                             4     572
   t53              temp    long long                       8     576
   t54              temp    double                          8     584
   t55              temp    double                          8     592
   t57              temp    void *                          4     604
   t58              temp    int *                           4     608
   t59              temp    int *                           4     612
   t61              temp    void *                          4     620
   t62              temp    void *                          4     624
   t63              temp    int                             4     628
   t64              temp    int *                           4     632
   t65              temp    int                             4     636
   t66              temp    int                             4     640
   t67              temp    int *                           4     644
   t68              temp    int                             4     648
   t69              temp    int                             4     652
   t70              temp    int                             4     656
   t71              temp    int *                           4     660
   t72              temp    int                             4     664
   t73              temp    int                             4     668
   t74              temp    long long                       8     672
   t75              temp    int                             4     680
   (49 temporaries no longer used after optimization not shown)

 Code: 182 instruction(s)

    161       a = 123456789012345
    162       b = -987654321
    163       u = 18000000000000000000
    164       param "%lld %lld %lld\n"
    165       param 123455801358024
    166       param 123457776666666
    167       param 370370367037035
    168       call printf, 4
    169       param "%lld %lld %lld %lld\n"
    170       param 123456789012
    171       param 345
    172       param -124999
    173       param 986541666
    174       call printf, 5
    175       param "%lld %lld\n"
    176       param -141093474
    177       param -3
    178       call printf, 3
    179       param "%llu %llu %llu\n"
    180       param 1800000000000000000
    181       param 0
    182       param 2250000000000000000
    183       call printf, 4
    184       param "%lld %lld %lld %lld\n"
    185       param 3950617248395040
    186       param 964506164158
    187       param -61728396
    188       param 1099511627776
    189       call printf, 5
    190       param "%d %d %d %d\n"
    191       param 1
    192       param 1
    193       param 1
    194       param 1
    195       call printf, 5
    196       param 3
    197       param 30
    198       t22 = call power(long long, int), 2
    199       param "%lld %llx\n"
    200       param t22
    201       param 18000000000000000000
    202       call printf, 3
    203       param "%lld %lld\n"
    204       param -123456789012345
    205       param -123456789012346
    206       call printf, 3
    207       i = -7
    208       big = 3000000000
    209       d = -7.0
    210       e = 3e+09
    211       f = 123456789012345.0
    212       fl = 3e+09
    213       param "%.1f %.1f %.1f %.1f\n"
    214       param -7.0
    215       param 3e+09
    216       param 123456789012345.0
    217       param 3e+09
    218       call printf, 5
    219       param "%d %u %lld %d\n"
    220       param 3
    221       param 3000000000
    222       param 12345678901
    223       param -2
    224       call printf, 5
    225       param "%lld %d %d\n"
    226       param -5000000000
    227       param -56
    228       param 4464
    229       call printf, 4
    230       x = 1.5
    231       y = 2.25
    232       param "%.2f %.2f %.2f %.2f %d\n"
    233       param 3.75
    234       param 3.375
    235       param 0.6666666865348816
    236       param -1.5
    237       param 1
    238       call printf, 6
    239       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n"
    240       param 3.14159
    241       param -2.5
    242       param 7.125
    243       param 2.5
    244       param 0.1
    245       call printf, 6
    246       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n"
    247       param -42
    248       param 42
    249       param -42
    250       param 255
    251       param 255
    252       param 8
    253       param "ab"
    254       param "cd"
    255       param 122
    256       call printf, 10
    257       param "[%*d] [%.*f] [%3s]\n"
    258       param 6
    259       param 12
    260       param 2
    261       param 1.23456
    262       param "long string"
    263       call printf, 6
    264       param 2
    265       s = call make(int), 1
    266       t = s
    267       t[24] = 100
    268       t48 = s[0]
    269       t49 = s[24]
    270       t51 = s[28]
    271       t52 = chartoint t51
    272       t53 = s[32]
    273       param "%.1f %d %d %c %lld\n"
    274       param t48
    275       param t49
    276       param 100
    277       param t52
    278       param t53
    279       call printf, 6
    280       param s
    281       param 2.0
    282       param 97
    283       param 5
    284       t54 = call weigh(struct Big, double, char, long long), 4
    285       param "%.1f\n"
    286       param t54
    287       call printf, 2
    288       param 3
    289       param 1.0
    290       param 2.5
    291       param 4.0
    292       param 77
    293       param "tail"
    294       t55 = call average(int, ...), 6
    295       param "%.2f\n"
    296       param t55
    297       call printf, 2
    298       param 12
    299       t57 = call malloc, 1
    300       p = t57
    301       *t57 = 1
    302       t58 = t57 ptr+ 4
    303       *t58 = 2
    304       t59 = t57 ptr+ 8
    305       *t59 = 3
    306       param t57
    307       param 24
    308       t61 = call realloc, 2
    309       p = t61
    310       param 4
    311       param 4
    312       t62 = call calloc, 2
    313       z = t62
    314       t63 = *t61
    315       t64 = t61 ptr+ 4
    316       t65 = *t64
    317       t66 = t63 int+ t65
    318       t67 = t61 ptr+ 8
    319       t68 = *t67
    320       t69 = t66 int+ t68
    321       t70 = *t62
    322       t71 = t62 ptr+ 12
    323       t72 = *t71
    324       if t61 ptr!= t62 goto L7
    325       t73 = 0
    326       goto L8
    327  L7:  t73 = 1
    328  L8:  param "%d %d %d %d\n"
    329       param t69
    330       param t70
    331       param t72
    332       param t73
    333       call printf, 5
    334       none = 0
    335       param "[%p] [%8p] [%-8p]\n"
    336       param 0
    337       param 0
    338       param 0
    339       call printf, 4
    340       t74 = a llong% 100
    341       t75 = llongtoint t74
    342       return t75


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Big                struct_tag    struct Big                 -           5    -    0  size 40
   make               function      struct Big (int)           -           7    -    1  _Z4makei; defined
   weigh              function      double (struct Big, double, char, long long) -          16    -    1  _Z5weigh3Bigdcx; defined
   average            function      double (int, ...)          -          20    -    1  _Z7averageiz; defined
   power              function      long long (long long, int) -          32    -    2  _Z5powerxi; defined
   main               function      int (void)                 -          34    -    0  defined

 scope: global > struct Big
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  field         double                     member      5    8    3  Big::d; public, offset 0
   n                  field         int[5]                     member      5   20    5  Big::n; public, offset 8
   tag                field         char                       member      5    1    2  Big::tag; public, offset 28
   w                  field         long long                  member      5    8    3  Big::w; public, offset 32

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param       7    4    4  k.1
   b                  variable      struct Big                 local       8   40    5  b.2

 scope: global > make() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      10    4    4  i.3

 scope: global > weigh()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  parameter     struct Big                 param      16   40    3  b.4
   scale              parameter     double                     param      16    8    1  scale.5
   c                  parameter     char                       param      16    1    1  c.6
   extra              parameter     long long                  param      16    8    1  extra.7

 scope: global > average()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   count              parameter     int                        param      20    4    3  count.8
   ap                 variable      va_list                    local      21    4    5  ap.9
   total              variable      double                     local      23    8    2  total.10
   tail               variable      long long                  local      25    8    1  tail.12
   label              variable      char *                     local      26    4    1  label.13

 scope: global > average() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      24    4    2  i.11

 scope: global > power()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   base               parameter     long long                  param      32    8    2  base.14
   n                  parameter     int                        param      32    4    2  n.15

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      long long                  local      35    8   17  a.16
   b                  variable      long long                  local      35    8    9  b.17
   u                  variable      unsigned long long         local      36    8    5  u.18
   i                  variable      int                        local      46    4    1  i.19
   big                variable      unsigned int               local      47    4    2  big.20
   d                  variable      double                     local      48    8    1  d.21
   e                  variable      double                     local      48    8    1  e.22
   f                  variable      double                     local      48    8    1  f.23
   fl                 variable      float                      local      49    4    1  fl.24
   x                  variable      float                      local      53    4    5  x.25
   y                  variable      float                      local      53    4    4  y.26
   s                  variable      struct Big                 local      60   40    6  s.27
   t                  variable      struct Big                 local      61   40    2  t.28
   p                  variable      int *                      local      67    4    9  p.29
   z                  variable      int *                      local      70    4    3  z.30
   none               variable      int *                      local      72    4    3  none.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Big: size 40, align 8
    +0  double d  [public]
    +8  int[5] n  [public]
    +28  char tag  [public]
    +32  long long w  [public]
