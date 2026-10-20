============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t30_temporaries.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 522 -> 451 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          522 -> 451   (13% fewer)

   constants folded                        3
   algebraic simplifications               0
   common subexpressions                  51
   copies / constants forwarded           69
   temporaries merged away                 6
   dead instructions removed              59
   jumps removed or redirected             6
   unreachable instructions removed        0

============================================================================
 FUNCTION Tag::Tag(int)        (link name _ZN3TagC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   n                param   int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    100     *this = n
    101     param "+%d "
    102     param n
    103     call printf, 2
    104     return

============================================================================
 FUNCTION Tag::~Tag()        (link name _ZN3TagD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    105     t1 = *this
    106     param "-%d "
    107     param t1
    108     call printf, 2
    109     return

============================================================================
 FUNCTION Tag::value()        (link name _ZN3Tag5valueEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    110     t1 = *this
    111     t2 = t1 int* 10
    112     return t2

============================================================================
 FUNCTION Tag::operator+(const class Tag &)        (link name _ZN3TagplERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   o                param   const class Tag &               4       4
   t1               temp    class Tag                       4       8
   t2               temp    class Tag *                     4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24

 Code: 8 instruction(s)

    113     t2 = &t1
    114     t3 = *this
    115     t4 = *o
    116     t5 = t3 int+ t4
    117     param t2                            (this)
    118     param t5
    119     call Tag::Tag(int), 2
    120     return t1

============================================================================
 FUNCTION Copy::Copy(int)        (link name _ZN4CopyC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Copy *                    4       0
   n                param   int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    121     *this = n
    122     param "+c%d "
    123     param n
    124     call printf, 2
    125     return

============================================================================
 FUNCTION Copy::Copy(const class Copy &)        (link name _ZN4CopyC1ERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Copy *                    4       0
   o                param   const class Copy &              4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    126     t1 = *o
    127     t2 = t1 int+ 100
    128     *this = t2
    129     param "copy%d "
    130     param t2
    131     call printf, 2
    132     return

============================================================================
 FUNCTION Copy::~Copy()        (link name _ZN4CopyD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Copy *                    4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    133     t1 = *this
    134     param "-c%d "
    135     param t1
    136     call printf, 2
    137     return

============================================================================
 FUNCTION make(int)        (link name _Z4makei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    class Tag                       4       4
   t2               temp    class Tag *                     4       8

 Code: 5 instruction(s)

    138     t2 = &t1
    139     param t2                            (this)
    140     param n
    141     call Tag::Tag(int), 2
    142     return t1

============================================================================
 FUNCTION named(int)        (link name _Z5namedi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t                local   class Tag                       4       4
   t1               temp    class Tag *                     4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 8 instruction(s)

    143     t1 = &t
    144     param t1                            (this)
    145     param n
    146     call Tag::Tag(int), 2
    147     t2 = t[0]
    148     t3 = t2 int+ 1
    149     t[0] = t3
    150     return t

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   which            param   int                             4       0
   a                local   class Tag                       4       4
   b                local   class Tag                       4       8
   t1               temp    class Tag *                     4      12
   t2               temp    class Tag *                     4      16
   t3               temp    class Tag                       4      20
   t4               temp    class Tag *                     4      24
   t5               temp    class Tag *                     4      28
   t6               temp    class Tag                       4      32
   t7               temp    class Tag *                     4      36
   t8               temp    class Tag *                     4      40

 Code: 25 instruction(s)

    151       t1 = &a
    152       param t1                            (this)
    153       param 40
    154       call Tag::Tag(int), 2
    155       t2 = &b
    156       param t2                            (this)
    157       param 41
    158       call Tag::Tag(int), 2
    159       if which int== 0 goto L1
    160       t3 = a
    161       t4 = &b
    162       param t4                            (this)
    163       call Tag::~Tag(), 1
    164       t5 = &a
    165       param t5                            (this)
    166       call Tag::~Tag(), 1
    167       return t3
    168  L1:  t6 = b
    169       t7 = &b
    170       param t7                            (this)
    171       call Tag::~Tag(), 1
    172       t8 = &a
    173       param t8                            (this)
    174       call Tag::~Tag(), 1
    175       return t6

============================================================================
 FUNCTION byValue(class Tag)        (link name _Z7byValue3Tag)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   class Tag                       4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    176     t1 = t[0]
    177     return t1

============================================================================
 FUNCTION byRef(const class Tag &)        (link name _Z5byRefRK3Tag)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   const class Tag &               4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    178     t1 = *t
    179     return t1

============================================================================
 FUNCTION copied(class Copy)        (link name _Z6copied4Copy)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Copy                      4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    180     t1 = c[0]
    181     return t1

============================================================================
 FUNCTION makeCopy(int)        (link name _Z8makeCopyi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    class Copy                      4       4
   t2               temp    class Copy *                    4       8

 Code: 5 instruction(s)

    182     t2 = &t1
    183     param t2                            (this)
    184     param n
    185     call Copy::Copy(int), 2
    186     return t1

============================================================================
 FUNCTION sameCopy(class Copy)        (link name _Z8sameCopy4Copy)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Copy                      4       0
   t1               temp    class Copy                      4       4
   t2               temp    class Copy *                    4       8
   t3               temp    class Copy *                    4      12

 Code: 6 instruction(s)

    187     t2 = &t1
    188     t3 = &c
    189     param t2                            (this)
    190     param t3
    191     call Copy::Copy(const class Copy &), 2
    192     return t1

============================================================================
 FUNCTION Shape::sides()        (link name _ZN5Shape5sidesEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    193     return 0

============================================================================
 FUNCTION Shape::kind()        (link name _ZN5Shape4kindEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    194     return 1

============================================================================
 FUNCTION Square::sides()        (link name _ZN6Square5sidesEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    195     return 4

============================================================================
 FUNCTION Square::kind()        (link name _ZN6Square4kindEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    196     return 2

============================================================================
 FUNCTION mix(long long, long long, int)        (link name _Z3mixxxi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 9 temporaries, frame 136 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   long long                       8       0
   b                param   long long                       8       8
   n                param   int                             4      16
   sum              local   long long                       8      24
   i                local   int                             4      32
   t1               temp    long long                       8      40
   t2               temp    long long                       8      48
   t3               temp    long long                       8      56
   t4               temp    long long                       8      64
   t5               temp    long long                       8      72
   t7               temp    long long                       8      88
   t8               temp    long long                       8      96
   t11              temp    long long                       8     120
   t12              temp    long long                       8     128
   (3 temporaries no longer used after optimization not shown)

 Code: 18 instruction(s)

    197       sum = 0
    198       i = 0
    199  L2:  if i int>= n goto L3
    200       t1 = inttollong i
    201       t2 = a llong* t1
    202       t3 = sum llong+ t2
    203       t4 = b llong^ sum
    204       t5 = t3 llong- t4
    205       sum = t5
    206       a = a llong+ 4294967296
    207       t7 = llong- b
    208       t8 = t5 llong& 65535
    209       b = t7 llong+ t8
    210       i = i int+ 1
    211       goto L2
    212  L3:  t11 = sum llong+ a
    213       t12 = t11 llong- b
    214       return t12

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 95 temporaries, frame 700 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                local   int                             4       0
   kept             local   class Tag                       4       4
   sum              local   class Tag                       4       8
   i                local   int                             4      12
   n                local   class Tag                       4      16
   r                local   const class Tag &               4      20
   c                local   class Copy                      4      24
   d                local   class Copy                      4      28
   e                local   class Copy                      4      32
   q                local   class Square                    1      36
   p                local   class Shape *                   4      40
   m                local   long long                       8      48
   inner            local   class Tag                       4      56
   t1               temp    class Tag                       4      60
   t2               temp    class Tag *                     4      64
   t4               temp    class Tag                       4      72
   t5               temp    class Tag *                     4      76
   t7               temp    class Tag                       4      84
   t8               temp    class Tag *                     4      88
   t10              temp    int                             4      96
   t11              temp    class Tag                       4     100
   t12              temp    class Tag *                     4     104
   t14              temp    int                             4     112
   t15              temp    int                             4     116
   t18              temp    class Tag                       4     128
   t20              temp    class Tag *                     4     136
   t22              temp    class Tag                       4     144
   t23              temp    class Tag *                     4     148
   t25              temp    class Tag                       4     156
   t27              temp    class Tag *                     4     164
   t29              temp    int                             4     172
   t32              temp    class Tag                       4     184
   t33              temp    class Tag *                     4     188
   t36              temp    class Tag                       4     200
   t37              temp    class Tag *                     4     204
   t38              temp    int                             4     208
   t41              temp    class Tag                       4     220
   t42              temp    class Tag *                     4     224
   t43              temp    int                             4     228
   t45              temp    class Tag                       4     236
   t46              temp    class Tag *                     4     240
   t47              temp    int                             4     244
   t49              temp    class Tag                       4     252
   t50              temp    class Tag *                     4     256
   t52              temp    int                             4     264
   t54              temp    class Tag                       4     272
   t55              temp    class Tag *                     4     276
   t57              temp    int                             4     284
   t59              temp    int                             4     292
   t60              temp    class Tag                       4     296
   t61              temp    class Tag *                     4     300
   t62              temp    int                             4     304
   t64              temp    class Tag                       4     312
   t65              temp    class Tag *                     4     316
   t67              temp    int                             4     324
   t70              temp    int                             4     336
   t71              temp    class Tag                       4     340
   t72              temp    class Tag *                     4     344
   t75              temp    class Tag                       4     356
   t76              temp    class Tag *                     4     360
   t79              temp    class Tag                       4     372
   t81              temp    class Tag *                     4     380
   t82              temp    int                             4     384
   t83              temp    class Tag                       4     388
   t84              temp    class Tag *                     4     392
   t85              temp    int                             4     396
   t87              temp    class Tag                       4     404
   t88              temp    class Tag *                     4     408
   t89              temp    int                             4     412
   t90              temp    int                             4     416
   t92              temp    class Tag                       4     424
   t93              temp    class Tag *                     4     428
   t95              temp    int                             4     436
   t96              temp    class Tag                       4     440
   t97              temp    class Tag *                     4     444
   t99              temp    int                             4     452
   t100             temp    class Copy *                    4     456
   t101             temp    class Copy                      4     460
   t102             temp    class Copy *                    4     464
   t104             temp    int                             4     472
   t106             temp    class Copy                      4     480
   t107             temp    class Copy *                    4     484
   t108             temp    int                             4     488
   t110             temp    class Copy                      4     496
   t112             temp    class Copy *                    4     504
   t113             temp    int                             4     508
   t114             temp    class Copy                      4     512
   t115             temp    class Copy *                    4     516
   t117             temp    class Copy                      4     524
   t119             temp    class Copy *                    4     532
   t121             temp    int                             4     540
   t122             temp    class Square *                  4     544
   t124             temp    int                             4     552
   t126             temp    int                             4     560
   t127             temp    int                             4     564
   t128             temp    int                             4     568
   t130             temp    int                             4     576
   t132             temp    int                             4     584
   t133             temp    long long                       8     592
   t137             temp    long long                       8     624
   t138             temp    class Tag *                     4     632
   t140             temp    int                             4     640
   t141             temp    class Tag                       4     644
   t142             temp    class Tag *                     4     648
   t144             temp    int                             4     656
   t145             temp    int                             4     660
   t153             temp    class Tag *                     4     692
   t154             temp    class Tag *                     4     696
   (59 temporaries no longer used after optimization not shown)

 Code: 336 instruction(s)

    215       t2 = &t1
    216       param t2                            (this)
    217       param 1
    218       call Tag::Tag(int), 2
    219       param t2                            (this)
    220       call Tag::~Tag(), 1
    221       param "| "
    222       call printf, 1
    223       param 2
    224       t4 = call make(int), 1
    225       t5 = &t4
    226       param t5                            (this)
    227       call Tag::~Tag(), 1
    228       param "| "
    229       call printf, 1
    230       t8 = &t7
    231       param t8                            (this)
    232       param 3
    233       call Tag::Tag(int), 2
    234       param t8                            (this)
    235       t10 = call Tag::value(), 1
    236       param 4
    237       t11 = call make(int), 1
    238       t12 = &t11
    239       param t12                           (this)
    240       t14 = call Tag::value(), 1
    241       t15 = t10 int+ t14
    242       v = t15
    243       param t12                           (this)
    244       call Tag::~Tag(), 1
    245       param t8                            (this)
    246       call Tag::~Tag(), 1
    247       param "%d | "
    248       param t15
    249       call printf, 2
    250       param 5
    251       t18 = call make(int), 1
    252       kept = t18
    253       t20 = &kept
    254       param "| "
    255       call printf, 1
    256       t23 = &t22
    257       param t23                           (this)
    258       param 6
    259       call Tag::Tag(int), 2
    260       param t20                           (this)
    261       param t23
    262       t25 = call Tag::operator+(const class Tag &), 2
    263       sum = t25
    264       t27 = &sum
    265       param t23                           (this)
    266       call Tag::~Tag(), 1
    267       t29 = sum[0]
    268       param "%d | "
    269       param t29
    270       call printf, 2
    271       param t20                           (this)
    272       param t27
    273       t32 = call Tag::operator+(const class Tag &), 2
    274       t33 = &t32
    275       param t33                           (this)
    276       param t20
    277       t36 = call Tag::operator+(const class Tag &), 2
    278       t37 = &t36
    279       t38 = t36[0]
    280       v = t38
    281       param t37                           (this)
    282       call Tag::~Tag(), 1
    283       param t33                           (this)
    284       call Tag::~Tag(), 1
    285       param "%d | "
    286       param t38
    287       call printf, 2
    288       t42 = &t41
    289       param t42                           (this)
    290       param 10
    291       call Tag::Tag(int), 2
    292       param t41
    293       t43 = call byValue(class Tag), 1
    294       v = t43
    295       param t42                           (this)
    296       call Tag::~Tag(), 1
    297       param "%d | "
    298       param t43
    299       call printf, 2
    300       t45 = kept
    301       t46 = &t45
    302       param t45
    303       t47 = call byValue(class Tag), 1
    304       v = t47
    305       param t46                           (this)
    306       call Tag::~Tag(), 1
    307       param "%d | "
    308       param t47
    309       call printf, 2
    310       t50 = &t49
    311       param t50                           (this)
    312       param 11
    313       call Tag::Tag(int), 2
    314       param t50
    315       t52 = call byRef(const class Tag &), 1
    316       v = t52
    317       param t50                           (this)
    318       call Tag::~Tag(), 1
    319       param "%d | "
    320       param t52
    321       call printf, 2
    322       t55 = &t54
    323       param t55                           (this)
    324       param 12
    325       call Tag::Tag(int), 2
    326       param t55
    327       t57 = call byRef(const class Tag &), 1
    328       param t55                           (this)
    329       call Tag::~Tag(), 1
    330       if t57 int<= 5 goto L4
    331       param "if "
    332       call printf, 1
    333  L4:  param "| "
    334       call printf, 1
    335       i = 0
    336  L5:  if i int>= 2 goto L6
    337       t59 = 13 int+ i
    338       param t59
    339       t60 = call make(int), 1
    340       t61 = &t60
    341       t62 = t60[0]
    342       param t61                           (this)
    343       call Tag::~Tag(), 1
    344       if t62 int<= 0 goto L6
    345       param "body "
    346       call printf, 1
    347       t65 = &t64
    348       param t65                           (this)
    349       param 20
    350       call Tag::Tag(int), 2
    351       param t65
    352       t67 = call byRef(const class Tag &), 1
    353       i = i int+ t67
    354       param t65                           (this)
    355       call Tag::~Tag(), 1
    356       goto L5
    357  L6:  param "| "
    358       call printf, 1
    359       if v int<= 0 goto L7
    360       t72 = &t71
    361       param t72                           (this)
    362       param 21
    363       call Tag::Tag(int), 2
    364       t70 = t71[0]
    365       param t72                           (this)
    366       call Tag::~Tag(), 1
    367       goto L8
    368  L7:  t76 = &t75
    369       param t76                           (this)
    370       param 22
    371       call Tag::Tag(int), 2
    372       t70 = t75[0]
    373       param t76                           (this)
    374       call Tag::~Tag(), 1
    375  L8:  v = t70
    376       param "%d | "
    377       param t70
    378       call printf, 2
    379       param 30
    380       t79 = call named(int), 1
    381       n = t79
    382       t81 = &n
    383       t82 = n[0]
    384       param "%d | "
    385       param t82
    386       call printf, 2
    387       param 1
    388       t83 = call pick(int), 1
    389       t84 = &t83
    390       t85 = t83[0]
    391       v = t85
    392       param t84                           (this)
    393       call Tag::~Tag(), 1
    394       param 0
    395       t87 = call pick(int), 1
    396       t88 = &t87
    397       t89 = t87[0]
    398       t90 = t85 int+ t89
    399       v = t90
    400       param t88                           (this)
    401       call Tag::~Tag(), 1
    402       param "%d | "
    403       param t90
    404       call printf, 2
    405       t93 = &t92
    406       param t93                           (this)
    407       param 50
    408       call Tag::Tag(int), 2
    409       r = t93
    410       t95 = *t93
    411       param "%d | "
    412       param t95
    413       call printf, 2
    414       t97 = &t96
    415       param t97                           (this)
    416       param 60
    417       call Tag::Tag(int), 2
    418       kept = t96
    419       param t97                           (this)
    420       call Tag::~Tag(), 1
    421       t99 = kept[0]
    422       param "%d\n"
    423       param t99
    424       call printf, 2
    425       t100 = &c
    426       param t100                          (this)
    427       param 1
    428       call Copy::Copy(int), 2
    429       param "| "
    430       call printf, 1
    431       t102 = &t101
    432       param t102                          (this)
    433       param t100
    434       call Copy::Copy(const class Copy &), 2
    435       param t101
    436       t104 = call copied(class Copy), 1
    437       v = t104
    438       param t102                          (this)
    439       call Copy::~Copy(), 1
    440       param "%d | "
    441       param t104
    442       call printf, 2
    443       t107 = &t106
    444       param t107                          (this)
    445       param 2
    446       call Copy::Copy(int), 2
    447       param t106
    448       t108 = call copied(class Copy), 1
    449       v = t108
    450       param t107                          (this)
    451       call Copy::~Copy(), 1
    452       param "%d | "
    453       param t108
    454       call printf, 2
    455       param 3
    456       t110 = call makeCopy(int), 1
    457       d = t110
    458       t112 = &d
    459       t113 = d[0]
    460       param "%d | "
    461       param t113
    462       call printf, 2
    463       t115 = &t114
    464       param t115                          (this)
    465       param t100
    466       call Copy::Copy(const class Copy &), 2
    467       param t114
    468       t117 = call sameCopy(class Copy), 1
    469       e = t117
    470       t119 = &e
    471       param t115                          (this)
    472       call Copy::~Copy(), 1
    473       t121 = e[0]
    474       param "%d\n"
    475       param t121
    476       call printf, 2
    477       t122 = &q
    478       p = t122
    479       param t122                          (this)
    480       t124 = call Square::sides(), 1
    481       param t122                          (this)
    482       t126 = call Shape::sides(), 1
    483       param t122                          (this)
    484       t127 = call Shape::sides(), 1
    485       param t122                          (this)
    486       t128 = call Shape::sides(), 1
    487       param t122                          (this)
    488       t130 = call Square::kind(), 1
    489       param t122                          (this)
    490       t132 = call Shape::kind(), 1
    491       param "%d %d %d %d %d %d\n"
    492       param t124
    493       param t126
    494       param t127
    495       param t128
    496       param t130
    497       param t132
    498       call printf, 7
    499       param 3
    500       param 5
    501       param 20
    502       t133 = call mix(long long, long long, int), 3
    503       m = t133
    504       param -7
    505       param 1099511627776
    506       param 9
    507       t137 = call mix(long long, long long, int), 3
    508       param "%lld %lld\n"
    509       param t133
    510       param t137
    511       call printf, 3
    512       t138 = &inner
    513       param t138                          (this)
    514       param 70
    515       call Tag::Tag(int), 2
    516       param t138
    517       t140 = call byRef(const class Tag &), 1
    518       t142 = &t141
    519       param t142                          (this)
    520       param 71
    521       call Tag::Tag(int), 2
    522       param t142
    523       t144 = call byRef(const class Tag &), 1
    524       t145 = t140 int+ t144
    525       param "%d "
    526       param t145
    527       call printf, 2
    528       param t142                          (this)
    529       call Tag::~Tag(), 1
    530       param t138                          (this)
    531       call Tag::~Tag(), 1
    532       param "end\n"
    533       call printf, 1
    534       param t119                          (this)
    535       call Copy::~Copy(), 1
    536       param t112                          (this)
    537       call Copy::~Copy(), 1
    538       param t100                          (this)
    539       call Copy::~Copy(), 1
    540       param t93                           (this)
    541       call Tag::~Tag(), 1
    542       param t81                           (this)
    543       call Tag::~Tag(), 1
    544       t153 = &sum
    545       param t153                          (this)
    546       call Tag::~Tag(), 1
    547       t154 = &kept
    548       param t154                          (this)
    549       call Tag::~Tag(), 1
    550       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Tag                class_tag     class Tag                  -           7    -    0  size 4
   Copy               class_tag     class Copy                 -          16    -    0  size 4
   make               function      class Tag (int)            -          24    -    4  _Z4makei; defined
   named              function      class Tag (int)            -          25    -    1  _Z5namedi; defined
   pick               function      class Tag (int)            -          30    -    2  _Z4picki; defined
   byValue            function      int (class Tag)            -          36    -    2  _Z7byValue3Tag; defined
   byRef              function      int (const class Tag &)    -          37    -    5  _Z5byRefRK3Tag; defined
   copied             function      int (class Copy)           -          38    -    2  _Z6copied4Copy; defined
   makeCopy           function      class Copy (int)           -          39    -    1  _Z8makeCopyi; defined
   sameCopy           function      class Copy (class Copy)    -          40    -    1  _Z8sameCopy4Copy; defined
   Shape              class_tag     class Shape                -          42    -    0  size 1
   Square             class_tag     class Square               -          47    -    0  size 1, public base Shape
   mix                function      long long (long long, long long, int) -          53    -    2  _Z3mixxxi; defined
   main               function      int (void)                 -          63    -    0  defined

 scope: global > class Tag
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      9    4   20  Tag::id; public, offset 0
   Tag                constructor   void (int)                 -          10    -   18  _ZN3TagC1Ei; public
   ~Tag               destructor    void (void)                -          11    -    0  _ZN3TagD1Ev; public
   value              method        int (void)                 -          12    -    2  _ZN3Tag5valueEv; public, defined
   operator+          method        class Tag (const class Tag &) -          13    -    3  _ZN3TagplERKS_; public, defined

 scope: global > class Tag > Tag()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      10    4    1  n.1

 scope: global > class Tag > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Tag &          param      13    4    1  o.2

 scope: global > class Copy
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     18    4    9  Copy::id; public, offset 0
   Copy               constructor   void (int)                 -          19    -    3  _ZN4CopyC1Ei; public
   Copy               constructor   void (const class Copy &)  -          20    -    0  _ZN4CopyC1ERKS_; public
   ~Copy              destructor    void (void)                -          21    -    0  _ZN4CopyD1Ev; public

 scope: global > class Copy > Copy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      19    4    1  n.3
   o                  parameter     const class Copy &         param      20    4    1  o.4

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      24    4    1  n.5

 scope: global > named()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      25    4    1  n.6
   t                  variable      class Tag                  local      26    4    3  t.7

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   which              parameter     int                        param      30    4    1  which.8
   a                  variable      class Tag                  local      31    4    1  a.9
   b                  variable      class Tag                  local      32    4    1  b.10

 scope: global > byValue()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     class Tag                  param      36    4    1  t.11

 scope: global > byRef()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     const class Tag &          param      37    4    1  t.12

 scope: global > copied()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Copy                 param      38    4    1  c.13

 scope: global > makeCopy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      39    4    1  n.14

 scope: global > sameCopy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Copy                 param      40    4    1  c.15

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   sides              method        int (void)                 -          44    -    3  _ZN5Shape5sidesEv; public, defined
   kind               method        int (void)                 -          45    -    1  _ZN5Shape4kindEv; public, defined

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   sides              method        int (void)                 -          49    -    1  _ZN6Square5sidesEv; public, defined
   kind               method        int (void)                 -          50    -    1  _ZN6Square4kindEv; public, defined

 scope: global > mix()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     long long                  param      53    8    4  a.16
   b                  parameter     long long                  param      53    8    4  b.17
   n                  parameter     int                        param      53    4    1  n.18
   sum                variable      long long                  local      54    8    5  sum.19

 scope: global > mix() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      55    4    3  i.20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  variable      int                        local      68    4   20  v.21
   kept               variable      class Tag                  local      70    4    6  kept.22
   sum                variable      class Tag                  local      72    4    2  sum.23
   n                  variable      class Tag                  local      88    4    1  n.25
   r                  variable      const class Tag &          local      93    4    1  r.26
   c                  variable      class Copy                 local      98    4    2  c.27
   d                  variable      class Copy                 local     104    4    1  d.28
   e                  variable      class Copy                 local     106    4    1  e.29
   q                  variable      class Square               local     109    1    5  q.30
   p                  variable      class Shape *              local     110    4    2  p.31
   m                  variable      long long                  local     113    8    1  m.32

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      84    4    4  i.24

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   inner              variable      class Tag                  local     116    4    1  inner.33

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Tag: size 4, align 4
    +0  int id  [public]
class Copy: size 4, align 4
    +0  int id  [public]
class Shape: size 1, align 1
class Square: size 1, align 1
    (base Shape, public)
