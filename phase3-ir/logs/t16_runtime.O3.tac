============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_runtime.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 310 -> 222 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          310 -> 222   (28% fewer)

   constants folded                       51
   algebraic simplifications               1
   common subexpressions                   1
   copies / constants forwarded          114
   temporaries merged away                 5
   dead instructions removed              58
   jumps removed or redirected             9
   unreachable instructions removed       10
   propagated across blocks                1
   dead assignments removed               16
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          2
   unreachable functions removed           1

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

 Code: 24 instruction(s)

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
    110       if i int>= 5 goto L2
    111       t3 = i int<< 2                      (w = 4)
    112       t4 = 8 int+ t3
    113       t5 = k int+ i
    114       b[t4] = t5
    115       i = i int+ 1
    116       goto L1
    117  L2:  t7 = 65 int+ k
    118       t8 = inttochar t7
    119       b[28] = t8
    120       t9 = inttollong k
    121       t10 = t9 llong* 10000000000
    122       b[32] = t10
    123       return b

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

 Code: 22 instruction(s)

    124       va_start ap, count
    125       total = 0.0
    126       i = 0
    127  L3:  if i int>= count goto L4
    128       t1 = va_arg ap, double
    129       total = total double+ t1
    130       i = i int+ 1
    131       if i int>= count goto L4
    132       t1 = va_arg ap, double
    133       total = total double+ t1
    134       i = i int+ 1
    135       goto L3
    136  L4:  t4 = va_arg ap, llong
    137       t5 = va_arg ap, ptr
    138       va_end ap
    139       param "%s %lld\n"
    140       param t5
    141       param t4
    142       call printf, 3
    143       t6 = inttodouble count
    144       t7 = total double/ t6
    145       return t7

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

    146       if n int!= 0 goto L5
    147       t1 = 1
    148       goto L6
    149  L5:  t2 = n int- 1
    150       param base
    151       param t2
    152       t3 = call power(long long, int), 2
    153       t1 = base llong* t3
    154  L6:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 35 temporaries, frame 856 bytes

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
   t22              temp    long long                       8     312
   t50              temp    double                          8     552
   t51              temp    int                             4     560
   t53              temp    char                            1     568
   t54              temp    int                             4     572
   t55              temp    long long                       8     576
   t57              temp    double                          8     592
   t59              temp    void *                          4     604
   t60              temp    int *                           4     608
   t61              temp    int *                           4     612
   t63              temp    void *                          4     620
   t64              temp    void *                          4     624
   t65              temp    int                             4     628
   t66              temp    int *                           4     632
   t67              temp    int                             4     636
   t68              temp    int                             4     640
   t69              temp    int *                           4     644
   t70              temp    int                             4     648
   t71              temp    int                             4     652
   t72              temp    int                             4     656
   t73              temp    int *                           4     660
   t74              temp    int                             4     664
   t75              temp    int                             4     668
   t78              temp    struct Big                     40     688
   t82              temp    double                          8     752
   t83              temp    double                          8     760
   t84              temp    int                             4     768
   t85              temp    double                          8     776
   t86              temp    double                          8     784
   t88              temp    double                          8     800
   t89              temp    long long                       8     808
   t90              temp    long long                       8     816
   t91              temp    double                          8     824
   t92              temp    double                          8     832
   t94              temp    double                          8     848
   (59 temporaries no longer used after optimization not shown)

 Code: 167 instruction(s)

    155       param "%lld %lld %lld\n"
    156       param 123455801358024
    157       param 123457776666666
    158       param 370370367037035
    159       call printf, 4
    160       param "%lld %lld %lld %lld\n"
    161       param 123456789012
    162       param 345
    163       param -124999
    164       param 986541666
    165       call printf, 5
    166       param "%lld %lld\n"
    167       param -141093474
    168       param -3
    169       call printf, 3
    170       param "%llu %llu %llu\n"
    171       param 1800000000000000000
    172       param 0
    173       param 2250000000000000000
    174       call printf, 4
    175       param "%lld %lld %lld %lld\n"
    176       param 3950617248395040
    177       param 964506164158
    178       param -61728396
    179       param 1099511627776
    180       call printf, 5
    181       param "%d %d %d %d\n"
    182       param 1
    183       param 1
    184       param 1
    185       param 1
    186       call printf, 5
    187       param 3
    188       param 30
    189       t22 = call power(long long, int), 2
    190       param "%lld %llx\n"
    191       param t22
    192       param 18000000000000000000
    193       call printf, 3
    194       param "%lld %lld\n"
    195       param -123456789012345
    196       param -123456789012346
    197       call printf, 3
    198       param "%.1f %.1f %.1f %.1f\n"
    199       param -7.0
    200       param 3e+09
    201       param 123456789012345.0
    202       param 3e+09
    203       call printf, 5
    204       param "%d %u %lld %d\n"
    205       param 3
    206       param 3000000000
    207       param 12345678901
    208       param -2
    209       call printf, 5
    210       param "%lld %d %d\n"
    211       param -5000000000
    212       param -56
    213       param 4464
    214       call printf, 4
    215       param "%.2f %.2f %.2f %.2f %d\n"
    216       param 3.75
    217       param 3.375
    218       param 0.6666666865348816
    219       param -1.5
    220       param 1
    221       call printf, 6
    222       param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n"
    223       param 3.14159
    224       param -2.5
    225       param 7.125
    226       param 2.5
    227       param 0.1
    228       call printf, 6
    229       param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n"
    230       param -42
    231       param 42
    232       param -42
    233       param 255
    234       param 255
    235       param 8
    236       param "ab"
    237       param "cd"
    238       param 122
    239       call printf, 10
    240       param "[%*d] [%.*f] [%3s]\n"
    241       param 6
    242       param 12
    243       param 2
    244       param 1.23456
    245       param "long string"
    246       call printf, 6
    247       param 2
    248       s = call make(int), 1
    249       t = s
    250       t[24] = 100
    251       t50 = s[0]
    252       t51 = s[24]
    253       t53 = s[28]
    254       t54 = chartoint t53
    255       t55 = s[32]
    256       param "%.1f %d %d %c %lld\n"
    257       param t50
    258       param t51
    259       param 100
    260       param t54
    261       param t55
    262       call printf, 6
    263       t78 = s
    264       t82 = t78[0]
    265       t83 = t82 double* 2.0
    266       t84 = t78[24]
    267       t85 = inttodouble t84
    268       t86 = t83 double+ t85
    269       t88 = t86 double+ 97.0
    270       t89 = t78[32]
    271       t90 = t89 llong/ 1000000000
    272       t91 = llongtodouble t90
    273       t92 = t88 double+ t91
    274       t94 = t92 double+ 5.0
    275       param "%.1f\n"
    276       param t94
    277       call printf, 2
    278       param 3
    279       param 1.0
    280       param 2.5
    281       param 4.0
    282       param 77
    283       param "tail"
    284       t57 = call average(int, ...), 6
    285       param "%.2f\n"
    286       param t57
    287       call printf, 2
    288       param 12
    289       t59 = call malloc, 1
    290       *t59 = 1
    291       t60 = t59 ptr+ 4
    292       *t60 = 2
    293       t61 = t59 ptr+ 8
    294       *t61 = 3
    295       param t59
    296       param 24
    297       t63 = call realloc, 2
    298       param 4
    299       param 4
    300       t64 = call calloc, 2
    301       t65 = *t63
    302       t66 = t63 ptr+ 4
    303       t67 = *t66
    304       t68 = t65 int+ t67
    305       t69 = t63 ptr+ 8
    306       t70 = *t69
    307       t71 = t68 int+ t70
    308       t72 = *t64
    309       t73 = t64 ptr+ 12
    310       t74 = *t73
    311       if t63 ptr!= t64 goto L7
    312       t75 = 0
    313       goto L8
    314  L7:  t75 = 1
    315  L8:  param "%d %d %d %d\n"
    316       param t71
    317       param t72
    318       param t74
    319       param t75
    320       call printf, 5
    321       return 45


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

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Big: size 40, align 8
    +0  double d  [public]
    +8  int[5] n  [public]
    +28  char tag  [public]
    +32  long long w  [public]
