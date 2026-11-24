============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t16_runtime.c
   Optimization  : no optimization
   Result        : Three address code generated: 5 function(s), 316 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION make(int)        (link name _Z4makei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 10 temporaries, frame 112 bytes

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
   t6               temp    int                             4      84
   t7               temp    int                             4      88
   t8               temp    char                            1      92
   t9               temp    long long                       8      96
   t10              temp    long long                       8     104

 Code: 20 instruction(s)

    100       t1 = inttodouble k
    101       t2 = t1 double* 1.5
    102       b[0] = t2
    103       i = 0
    104  L1:  if i int< 5 goto L2
    105       goto L3
    106  L2:  t3 = i int* 4                       (w = 4)
    107       t4 = 8 int+ t3
    108       t5 = k int+ i
    109       b[t4] = t5
    110       t6 = i int+ 1
    111       i = t6
    112       goto L1
    113  L3:  t7 = 65 int+ k
    114       t8 = inttochar t7
    115       b[28] = t8
    116       t9 = inttollong k
    117       t10 = 10000000000 llong* t9
    118       b[32] = t10
    119       return b

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

    120     t1 = b[0]
    121     t2 = t1 double* scale
    122     t3 = b[24]
    123     t4 = inttodouble t3
    124     t5 = t2 double+ t4
    125     t6 = chartodouble c
    126     t7 = t5 double+ t6
    127     t8 = b[32]
    128     t9 = t8 llong/ 1000000000
    129     t10 = llongtodouble t9
    130     t11 = t7 double+ t10
    131     t12 = llongtodouble extra
    132     t13 = t11 double+ t12
    133     return t13

============================================================================
 FUNCTION average(int, ...)        (link name _Z7averageiz)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 7 temporaries, frame 96 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   count            param   int                             4       0
   ap               local   va_list                         4       4
   total            local   double                          8       8
   i                local   int                             4      16
   tail             local   long long                       8      24
   label            local   char *                          4      32
   t1               temp    double                          8      40
   t2               temp    double                          8      48
   t3               temp    int                             4      56
   t4               temp    long long                       8      64
   t5               temp    char *                          4      72
   t6               temp    double                          8      80
   t7               temp    double                          8      88

 Code: 23 instruction(s)

    134       va_start ap, count
    135       total = 0.0
    136       i = 0
    137  L4:  if i int< count goto L5
    138       goto L6
    139  L5:  t1 = va_arg ap, double
    140       t2 = total double+ t1
    141       total = t2
    142       t3 = i int+ 1
    143       i = t3
    144       goto L4
    145  L6:  t4 = va_arg ap, llong
    146       tail = t4
    147       t5 = va_arg ap, ptr
    148       label = t5
    149       va_end ap
    150       param "%s %lld\n"
    151       param label
    152       param tail
    153       call printf, 3
    154       t6 = inttodouble count
    155       t7 = total double/ t6
    156       return t7

============================================================================
 FUNCTION power(long long, int)        (link name _Z5powerxi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   base             param   long long                       8       0
   n                param   int                             4       8
   t1               temp    long long                       8      16
   t2               temp    int                             4      24
   t3               temp    long long                       8      32
   t4               temp    long long                       8      40

 Code: 11 instruction(s)

    157       if n int== 0 goto L7
    158       goto L8
    159  L7:  t1 = 1
    160       goto L9
    161  L8:  t2 = n int- 1
    162       param base
    163       param t2
    164       t3 = call power(long long, int), 2
    165       t4 = base llong* t3
    166       t1 = t4
    167  L9:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 16 parameter(s)/local(s), 77 temporaries, frame 692 bytes

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
   t1               temp    long long                       8     168
   t2               temp    long long                       8     176
   t3               temp    long long                       8     184
   t4               temp    long long                       8     192
   t5               temp    long long                       8     200
   t6               temp    long long                       8     208
   t7               temp    long long                       8     216
   t8               temp    long long                       8     224
   t9               temp    long long                       8     232
   t10              temp    long long                       8     240
   t11              temp    unsigned long long              8     248
   t12              temp    unsigned long long              8     256
   t13              temp    unsigned long long              8     264
   t14              temp    long long                       8     272
   t15              temp    long long                       8     280
   t16              temp    long long                       8     288
   t17              temp    long long                       8     296
   t18              temp    int                             4     304
   t19              temp    int                             4     308
   t20              temp    int                             4     312
   t21              temp    int                             4     316
   t22              temp    long long                       8     320
   t23              temp    long long                       8     328
   t24              temp    long long                       8     336
   t25              temp    int                             4     344
   t26              temp    double                          8     352
   t27              temp    double                          8     360
   t28              temp    double                          8     368
   t29              temp    float                           4     376
   t30              temp    double                          8     384
   t31              temp    double                          8     392
   t32              temp    int                             4     400
   t33              temp    double                          8     408
   t34              temp    long long                       8     416
   t35              temp    float                           4     424
   t36              temp    double                          8     432
   t37              temp    float                           4     440
   t38              temp    double                          8     448
   t39              temp    float                           4     456
   t40              temp    double                          8     464
   t41              temp    float                           4     472
   t42              temp    double                          8     480
   t43              temp    int                             4     488
   t44              temp    double                          8     496
   t45              temp    int                             4     504
   t46              temp    int                             4     508
   t47              temp    struct Big                     40     512
   t48              temp    struct Big *                    4     552
   t49              temp    struct Big *                    4     556
   t50              temp    double                          8     560
   t51              temp    int                             4     568
   t52              temp    int                             4     572
   t53              temp    char                            1     576
   t54              temp    int                             4     580
   t55              temp    long long                       8     584
   t56              temp    double                          8     592
   t57              temp    double                          8     600
   t58              temp    unsigned int                    4     608
   t59              temp    void *                          4     612
   t60              temp    int *                           4     616
   t61              temp    int *                           4     620
   t62              temp    unsigned int                    4     624
   t63              temp    void *                          4     628
   t64              temp    void *                          4     632
   t65              temp    int                             4     636
   t66              temp    int *                           4     640
   t67              temp    int                             4     644
   t68              temp    int                             4     648
   t69              temp    int *                           4     652
   t70              temp    int                             4     656
   t71              temp    int                             4     660
   t72              temp    int                             4     664
   t73              temp    int *                           4     668
   t74              temp    int                             4     672
   t75              temp    int                             4     676
   t76              temp    long long                       8     680
   t77              temp    int                             4     688

 Code: 248 instruction(s)

    168        a = 123456789012345
    169        t1 = llong- 987654321
    170        b = t1
    171        u = 18000000000000000000
    172        t2 = a llong+ b
    173        t3 = a llong- b
    174        t4 = a llong* 3
    175        param "%lld %lld %lld\n"
    176        param t2
    177        param t3
    178        param t4
    179        call printf, 4
    180        t5 = a llong/ 1000
    181        t6 = a llong% 1000
    182        t7 = a llong/ b
    183        t8 = a llong% b
    184        param "%lld %lld %lld %lld\n"
    185        param t5
    186        param t6
    187        param t7
    188        param t8
    189        call printf, 5
    190        t9 = b llong/ 7
    191        t10 = b llong% 7
    192        param "%lld %lld\n"
    193        param t9
    194        param t10
    195        call printf, 3
    196        t11 = u ullong/ 10
    197        t12 = u ullong% 1000
    198        t13 = u ullong>> 3
    199        param "%llu %llu %llu\n"
    200        param t11
    201        param t12
    202        param t13
    203        call printf, 4
    204        t14 = a llong<< 5
    205        t15 = a llong>> 7
    206        t16 = b llong>> 4
    207        t17 = 1 llong<< 40
    208        param "%lld %lld %lld %lld\n"
    209        param t14
    210        param t15
    211        param t16
    212        param t17
    213        call printf, 5
    214        if a llong> b goto L10
    215        t18 = 0
    216        goto L11
    217  L10:  t18 = 1
    218  L11:  if b llong< 0 goto L12
    219        t19 = 0
    220        goto L13
    221  L12:  t19 = 1
    222  L13:  if a llong== a goto L14
    223        t20 = 0
    224        goto L15
    225  L14:  t20 = 1
    226  L15:  if u ullong> a goto L16
    227        t21 = 0
    228        goto L17
    229  L16:  t21 = 1
    230  L17:  param "%d %d %d %d\n"
    231        param t18
    232        param t19
    233        param t20
    234        param t21
    235        call printf, 5
    236        param 3
    237        param 30
    238        t22 = call power(long long, int), 2
    239        param "%lld %llx\n"
    240        param t22
    241        param u
    242        call printf, 3
    243        t23 = llong- a
    244        t24 = llong~ a
    245        param "%lld %lld\n"
    246        param t23
    247        param t24
    248        call printf, 3
    249        t25 = int- 7
    250        i = t25
    251        big = 3000000000
    252        t26 = inttodouble i
    253        d = t26
    254        t27 = uinttodouble big
    255        e = t27
    256        t28 = llongtodouble a
    257        f = t28
    258        t29 = uinttofloat big
    259        fl = t29
    260        t30 = floattodouble fl
    261        param "%.1f %.1f %.1f %.1f\n"
    262        param d
    263        param e
    264        param f
    265        param t30
    266        call printf, 5
    267        t31 = double- 2.5
    268        t32 = doubletoint t31
    269        param "%d %u %lld %d\n"
    270        param 3
    271        param 3000000000
    272        param 12345678901
    273        param t32
    274        call printf, 5
    275        t33 = double- 5e+09
    276        t34 = doubletollong t33
    277        param "%lld %d %d\n"
    278        param t34
    279        param -56
    280        param 4464
    281        call printf, 4
    282        x = 1.5
    283        y = 2.25
    284        t35 = x float+ y
    285        t36 = floattodouble t35
    286        t37 = x float* y
    287        t38 = floattodouble t37
    288        t39 = x float/ y
    289        t40 = floattodouble t39
    290        t41 = float- x
    291        t42 = floattodouble t41
    292        if x float< y goto L18
    293        t43 = 0
    294        goto L19
    295  L18:  t43 = 1
    296  L19:  param "%.2f %.2f %.2f %.2f %d\n"
    297        param t36
    298        param t38
    299        param t40
    300        param t42
    301        param t43
    302        call printf, 6
    303        t44 = double- 2.5
    304        param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n"
    305        param 3.14159
    306        param t44
    307        param 7.125
    308        param 2.5
    309        param 0.1
    310        call printf, 6
    311        t45 = int- 42
    312        t46 = int- 42
    313        param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n"
    314        param t45
    315        param 42
    316        param t46
    317        param 255
    318        param 255
    319        param 8
    320        param "ab"
    321        param "cd"
    322        param 122
    323        call printf, 10
    324        param "[%*d] [%.*f] [%3s]\n"
    325        param 6
    326        param 12
    327        param 2
    328        param 1.23456
    329        param "long string"
    330        call printf, 6
    331        param 2
    332        t47 = call make(int), 1
    333        s = t47
    334        t48 = &s
    335        t = s
    336        t49 = &t
    337        t[24] = 100
    338        t50 = s[0]
    339        t51 = s[24]
    340        t52 = t[24]
    341        t53 = s[28]
    342        t54 = chartoint t53
    343        t55 = s[32]
    344        param "%.1f %d %d %c %lld\n"
    345        param t50
    346        param t51
    347        param t52
    348        param t54
    349        param t55
    350        call printf, 6
    351        param s
    352        param 2.0
    353        param 97
    354        param 5
    355        t56 = call weigh(struct Big, double, char, long long), 4
    356        param "%.1f\n"
    357        param t56
    358        call printf, 2
    359        param 3
    360        param 1.0
    361        param 2.5
    362        param 4.0
    363        param 77
    364        param "tail"
    365        t57 = call average(int, ...), 6
    366        param "%.2f\n"
    367        param t57
    368        call printf, 2
    369        t58 = 3 uint* 4
    370        param t58
    371        t59 = call malloc, 1
    372        p = t59
    373        *p = 1
    374        t60 = p ptr+ 4
    375        *t60 = 2
    376        t61 = p ptr+ 8
    377        *t61 = 3
    378        t62 = 6 uint* 4
    379        param p
    380        param t62
    381        t63 = call realloc, 2
    382        p = t63
    383        param 4
    384        param 4
    385        t64 = call calloc, 2
    386        z = t64
    387        t65 = *p
    388        t66 = p ptr+ 4
    389        t67 = *t66
    390        t68 = t65 int+ t67
    391        t69 = p ptr+ 8
    392        t70 = *t69
    393        t71 = t68 int+ t70
    394        t72 = *z
    395        t73 = z ptr+ 12
    396        t74 = *t73
    397        if p ptr!= z goto L20
    398        t75 = 0
    399        goto L21
    400  L20:  t75 = 1
    401  L21:  param "%d %d %d %d\n"
    402        param t71
    403        param t72
    404        param t74
    405        param t75
    406        call printf, 5
    407        none = 0
    408        param "[%p] [%8p] [%-8p]\n"
    409        param none
    410        param none
    411        param none
    412        call printf, 4
    413        t76 = a llong% 100
    414        t77 = llongtoint t76
    415        return t77


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
