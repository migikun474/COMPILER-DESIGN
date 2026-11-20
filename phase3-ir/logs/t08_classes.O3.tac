============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 261 -> 318 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          261 -> 318   (-21% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                  27
   copies / constants forwarded           97
   temporaries merged away                 9
   dead instructions removed              70
   jumps removed or redirected             4
   unreachable instructions removed        2
   propagated across blocks                3
   dead assignments removed                5
   calls inlined                          28
   tail calls turned into jumps            0
   common subexpressions across blocks      3

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Dog::made        int                             4  0

 As three address code (initial values, in place before main runs):

    Dog::made = 0

============================================================================
 FUNCTION Animal::Animal()        (link name _ZN6AnimalC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0

 Code: 4 instruction(s)

    100     *this = 4
    101     param "Animal()\n"
    102     call printf, 1
    103     return

============================================================================
 FUNCTION Animal::count()        (link name _ZN6Animal5countEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    104     t1 = *this
    105     return t1

============================================================================
 FUNCTION Tag::Tag()        (link name _ZN3TagC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0

 Code: 4 instruction(s)

    106     *this = 7
    107     param "Tag()\n"
    108     call printf, 1
    109     return

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    class Dog *                     4       8
   (3 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    110     *this = 4
    111     param "Animal()\n"
    112     call printf, 1
    113     t1 = this ptr+ 8
    114     *t1 = 7
    115     param "Tag()\n"
    116     call printf, 1
    117     t2 = this ptr+ 4
    118     *t2 = 0
    119     Dog::made = Dog::made int+ 1
    120     param "Dog()\n"
    121     call printf, 1
    122     return

============================================================================
 FUNCTION Dog::human()        (link name _ZN3Dog5humanEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 8 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    class Dog *                     4      24
   t7               temp    int                             4      28
   t8               temp    int                             4      32

 Code: 9 instruction(s)

    123     t1 = this ptr+ 4
    124     t2 = *t1
    125     t3 = t2 int* 7
    126     t4 = *this
    127     t5 = t3 int+ t4
    128     t6 = this ptr+ 8
    129     t7 = *t6
    130     t8 = t5 int+ t7
    131     return t8

============================================================================
 FUNCTION Dog::total()        (link name _ZN3Dog5totalEv)
============================================================================

 Code: 1 instruction(s)

    132     return Dog::made

============================================================================
 FUNCTION Dog::birthday()        (link name _ZN3Dog8birthdayEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    133     t1 = this ptr+ 4
    134     t2 = *t1
    135     t3 = t2 int+ 1
    136     *t1 = t3
    137     return

============================================================================
 FUNCTION Vec::Vec()        (link name _ZN3VecC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4

 Code: 4 instruction(s)

    138     *this = 0
    139     t1 = this ptr+ 4
    140     *t1 = 0
    141     return

============================================================================
 FUNCTION Vec::operator+(class Vec)        (link name _ZN3VecplES_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 9 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   r                local   class Vec                       8      12
   t1               temp    class Vec *                     4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    class Vec *                     4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   t10              temp    class Vec *                     4      56
   (1 temporary no longer used after optimization not shown)

 Code: 14 instruction(s)

    142     t1 = &r
    143     *t1 = 0
    144     t10 = t1 ptr+ 4
    145     *t10 = 0
    146     t2 = *this
    147     t3 = o[0]
    148     t4 = t2 int+ t3
    149     r[0] = t4
    150     t5 = this ptr+ 4
    151     t6 = *t5
    152     t7 = o[4]
    153     t8 = t6 int+ t7
    154     r[4] = t8
    155     return r

============================================================================
 FUNCTION Vec::operator-()        (link name _ZN3VecmiEv)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   r                local   class Vec                       8       4
   t1               temp    class Vec *                     4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   t8               temp    class Vec *                     4      40
   (1 temporary no longer used after optimization not shown)

 Code: 12 instruction(s)

    156     t1 = &r
    157     *t1 = 0
    158     t8 = t1 ptr+ 4
    159     *t8 = 0
    160     t2 = *this
    161     t3 = int- t2
    162     r[0] = t3
    163     t4 = this ptr+ 4
    164     t5 = *t4
    165     t6 = int- t5
    166     r[4] = t6
    167     return r

============================================================================
 FUNCTION Vec::operator==(class Vec)        (link name _ZN3VeceqES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32

 Code: 11 instruction(s)

    168       t2 = *this
    169       t3 = o[0]
    170       if t2 int!= t3 goto L1
    171       t4 = this ptr+ 4
    172       t5 = *t4
    173       t6 = o[4]
    174       if t5 int== t6 goto L2
    175  L1:  t1 = 0
    176       goto L3
    177  L2:  t1 = 1
    178  L3:  return t1

============================================================================
 FUNCTION Vec::operator[](int)        (link name _ZN3VecixEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   i                param   int                             4       4
   t1               temp    int                             4       8
   t3               temp    class Vec *                     4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    179       if i int!= 0 goto L4
    180       t1 = *this
    181       goto L5
    182  L4:  t3 = this ptr+ 4
    183       t1 = *t3
    184  L5:  return t1

============================================================================
 FUNCTION Vec::operator+=(class Vec)        (link name _ZN3VecpLES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   t7               temp    int                             4      36
   (1 temporary no longer used after optimization not shown)

 Code: 10 instruction(s)

    185     t1 = *this
    186     t2 = o[0]
    187     t3 = t1 int+ t2
    188     *this = t3
    189     t4 = this ptr+ 4
    190     t5 = *t4
    191     t6 = o[4]
    192     t7 = t5 int+ t6
    193     *t4 = t7
    194     return this

============================================================================
 FUNCTION Vec::operator++()        (link name _ZN3VecppEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    195     t1 = *this
    196     t2 = t1 int+ 1
    197     *this = t2
    198     return this

============================================================================
 FUNCTION Vec::operator()(int)        (link name _ZN3VecclEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    class Vec *                     4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24

 Code: 6 instruction(s)

    199     t1 = *this
    200     t2 = t1 int* k
    201     t3 = this ptr+ 4
    202     t4 = *t3
    203     t5 = t2 int+ t4
    204     return t5

============================================================================
 FUNCTION Vec::dot(class Vec)        (link name _ZN3Vec3dotES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   t7               temp    int                             4      36
   t8               temp    int                             4      40

 Code: 9 instruction(s)

    205     t1 = *this
    206     t2 = o[0]
    207     t3 = t1 int* t2
    208     t4 = this ptr+ 4
    209     t5 = *t4
    210     t6 = o[4]
    211     t7 = t5 int* t6
    212     t8 = t3 int+ t7
    213     return t8

============================================================================
 FUNCTION make(int, int)        (link name _Z4makeii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   v                local   class Vec                       8       8
   t1               temp    class Vec *                     4      16
   t3               temp    class Vec *                     4      24
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    214     t1 = &v
    215     *t1 = 0
    216     t3 = t1 ptr+ 4
    217     *t3 = 0
    218     v[0] = a
    219     v[4] = b
    220     return v

============================================================================
 FUNCTION operator*(class Vec, int)        (link name _Zml3Veci)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   class Vec                       8       0
   k                param   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24
   t5               temp    class Vec                       8      28
   t8               temp    class Vec                       8      44
   t9               temp    class Vec *                     4      52
   (2 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    221     t1 = v[0]
    222     t2 = t1 int* k
    223     t3 = v[4]
    224     t4 = t3 int* k
    225     t9 = &t8
    226     param t9                            (this)
    227     call Vec::Vec(), 1
    228     t8[0] = t2
    229     t8[4] = t4
    230     t5 = t8
    231     return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 94 temporaries, frame 812 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   rex              local   class Dog                      12       0
   base             local   class Animal *                  4      12
   other            local   class Dog                      12      16
   a                local   class Vec                       8      28
   b                local   class Vec                       8      36
   c                local   class Vec                       8      44
   d                local   class Vec                       8      52
   e                local   class Vec                       8      60
   row              local   class Vec[2]                   16      68
   w                local   int                             4      84
   t1               temp    class Dog *                     4      88
   t9               temp    int                             4     120
   t10              temp    class Dog *                     4     124
   t15              temp    class Vec *                     4     152
   t16              temp    class Vec *                     4     156
   t25              temp    int                             4     204
   t26              temp    int                             4     208
   t27              temp    int                             4     212
   t28              temp    int                             4     216
   t29              temp    int                             4     220
   t30              temp    int                             4     224
   t41              temp    class Vec (*)[2]                4     268
   t42              temp    class Vec (*)[2]                4     272
   t43              temp    int                             4     276
   t45              temp    int                             4     284
   t46              temp    int                             4     288
   t48              temp    class Dog *                     4     296
   t49              temp    class Dog *                     4     300
   t52              temp    int                             4     312
   t53              temp    int                             4     316
   t57              temp    int                             4     332
   t58              temp    int                             4     336
   t59              temp    int                             4     340
   t61              temp    int                             4     348
   t62              temp    int                             4     352
   t66              temp    class Dog *                     4     368
   t67              temp    class Dog *                     4     372
   t70              temp    int                             4     384
   t71              temp    int                             4     388
   t72              temp    int                             4     392
   t73              temp    int                             4     396
   t75              temp    int                             4     404
   t76              temp    int                             4     408
   t79              temp    class Vec                       8     420
   t80              temp    class Vec *                     4     428
   t83              temp    class Vec                       8     440
   t84              temp    class Vec *                     4     448
   t86              temp    class Vec *                     4     456
   t88              temp    class Vec                       8     464
   t89              temp    class Vec                       8     472
   t90              temp    class Vec *                     4     480
   t91              temp    int                             4     484
   t92              temp    int                             4     488
   t93              temp    int                             4     492
   t94              temp    class Vec *                     4     496
   t95              temp    int                             4     500
   t96              temp    int                             4     504
   t97              temp    int                             4     508
   t99              temp    class Vec                       8     516
   t100             temp    class Vec *                     4     524
   t101             temp    int                             4     528
   t102             temp    int                             4     532
   t104             temp    int                             4     540
   t105             temp    int                             4     544
   t106             temp    class Vec                       8     548
   t108             temp    int                             4     560
   t109             temp    int                             4     564
   t110             temp    int                             4     568
   t111             temp    int                             4     572
   t114             temp    class Vec                       8     588
   t115             temp    int                             4     596
   t116             temp    int                             4     600
   t117             temp    int                             4     604
   t119             temp    int                             4     612
   t120             temp    int                             4     616
   t121             temp    int                             4     620
   t123             temp    int                             4     628
   t124             temp    int                             4     632
   t126             temp    class Vec                       8     640
   t127             temp    int                             4     648
   t128             temp    int                             4     652
   t130             temp    int                             4     660
   t131             temp    int                             4     664
   t132             temp    int                             4     668
   t134             temp    class Vec                       8     676
   t135             temp    int                             4     684
   t136             temp    int                             4     688
   t138             temp    int                             4     696
   t139             temp    int                             4     700
   t140             temp    int                             4     704
   t143             temp    int                             4     716
   t148             temp    int                             4     736
   t150             temp    int                             4     744
   t151             temp    int                             4     748
   t153             temp    class Vec                       8     756
   t154             temp    int                             4     764
   t155             temp    int                             4     768
   t156             temp    int                             4     772
   t158             temp    int                             4     780
   t159             temp    int                             4     784
   t160             temp    int                             4     788
   t161             temp    int                             4     792
   t163             temp    class Vec *                     4     800
   t165             temp    class Vec *                     4     808
   (71 temporaries no longer used after optimization not shown)

 Code: 186 instruction(s)

    232        t1 = &rex
    233        param t1                            (this)
    234        call Animal::Animal(), 1
    235        t48 = t1 ptr+ 8
    236        param t48                           (this)
    237        call Tag::Tag(), 1
    238        t49 = t1 ptr+ 4
    239        *t49 = 0
    240        Dog::made = Dog::made int+ 1
    241        param "Dog()\n"
    242        call printf, 1
    243        rex[4] = 3
    244        t52 = *t49
    245        t53 = t52 int+ 1
    246        *t49 = t53
    247        t57 = t53 int* 7
    248        t58 = *t1
    249        t59 = t57 int+ t58
    250        t61 = *t48
    251        t62 = t59 int+ t61
    252        param "%d %d %d\n"
    253        param t62
    254        param t58
    255        param Dog::made
    256        call printf, 4
    257        t9 = *t1
    258        param "%d\n"
    259        param t9
    260        call printf, 2
    261        param "--\n"
    262        call printf, 1
    263        t10 = &other
    264        param t10                           (this)
    265        call Animal::Animal(), 1
    266        t66 = t10 ptr+ 8
    267        param t66                           (this)
    268        call Tag::Tag(), 1
    269        t67 = t10 ptr+ 4
    270        *t67 = 0
    271        Dog::made = Dog::made int+ 1
    272        param "Dog()\n"
    273        call printf, 1
    274        other[4] = 5
    275        t70 = *t67
    276        t71 = t70 int* 7
    277        t72 = *t10
    278        t73 = t71 int+ t72
    279        t75 = *t66
    280        t76 = t73 int+ t75
    281        param "%d %d\n"
    282        param t76
    283        param Dog::made
    284        call printf, 3
    285        param "--\n"
    286        call printf, 1
    287        t80 = &t79
    288        param t80                           (this)
    289        call Vec::Vec(), 1
    290        t79[0] = 1
    291        t79[4] = 2
    292        a = t79
    293        t84 = &t83
    294        param t84                           (this)
    295        call Vec::Vec(), 1
    296        t83[0] = 3
    297        t83[4] = 4
    298        b = t83
    299        t15 = &c
    300        *t15 = 0
    301        t86 = t15 ptr+ 4
    302        *t86 = 0
    303        t16 = &a
    304        t88 = b
    305        t90 = &t89
    306        param t90                           (this)
    307        call Vec::Vec(), 1
    308        t91 = *t16
    309        t92 = t88[0]
    310        t93 = t91 int+ t92
    311        t89[0] = t93
    312        t94 = t16 ptr+ 4
    313        t95 = *t94
    314        t96 = t88[4]
    315        t97 = t95 int+ t96
    316        t89[4] = t97
    317        c = t89
    318        t100 = &t99
    319        param t100                          (this)
    320        call Vec::Vec(), 1
    321        t101 = *t15
    322        t102 = int- t101
    323        t99[0] = t102
    324        t104 = *t86
    325        t105 = int- t104
    326        t99[4] = t105
    327        d = t99
    328        t106 = a
    329        t108 = t106[0]
    330        t109 = t108 int* 3
    331        t110 = t106[4]
    332        t111 = t110 int* 3
    333        param t109
    334        param t111
    335        e = call make(int, int), 2
    336        t114 = b
    337        t115 = *t16
    338        t116 = t114[0]
    339        t117 = t115 int+ t116
    340        *t16 = t117
    341        t119 = *t94
    342        t120 = t114[4]
    343        t121 = t119 int+ t120
    344        *t94 = t121
    345        t123 = *t16
    346        t124 = t123 int+ 1
    347        *t16 = t124
    348        t25 = c[0]
    349        t26 = c[4]
    350        t27 = d[0]
    351        t28 = e[4]
    352        t29 = a[0]
    353        t30 = a[4]
    354        param "%d %d %d %d %d %d\n"
    355        param t25
    356        param t26
    357        param t27
    358        param t28
    359        param t29
    360        param t30
    361        call printf, 7
    362        t126 = b
    363        t127 = *t16
    364        t128 = t126[0]
    365        if t127 int!= t128 goto L6
    366        t130 = *t94
    367        t131 = t126[4]
    368        if t130 int== t131 goto L7
    369  L6:   t132 = 0
    370        goto L8
    371  L7:   t132 = 1
    372  L8:   t134 = c
    373        t135 = *t15
    374        t136 = t134[0]
    375        if t135 int!= t136 goto L9
    376        t138 = *t86
    377        t139 = t134[4]
    378        if t138 int== t139 goto L10
    379  L9:   t140 = 0
    380        goto L11
    381  L10:  t140 = 1
    382  L11:  t143 = *t16
    383        t148 = t143 int<< 1
    384        t150 = *t94
    385        t151 = t148 int+ t150
    386        t153 = b
    387        t154 = *t16
    388        t155 = t153[0]
    389        t156 = t154 int* t155
    390        t158 = *t94
    391        t159 = t153[4]
    392        t160 = t158 int* t159
    393        t161 = t156 int+ t160
    394        param "%d %d %d %d %d\n"
    395        param t132
    396        param t140
    397        param t143
    398        param t151
    399        param t161
    400        call printf, 6
    401        t41 = &row
    402        *t41 = 0
    403        t163 = t41 ptr+ 4
    404        *t163 = 0
    405        t42 = t41 ptr+ 8
    406        *t42 = 0
    407        t165 = t42 ptr+ 4
    408        *t165 = 0
    409        row[8] = 9
    410        t43 = row[0]
    411        param "%d %d\n"
    412        param t43
    413        param 9
    414        call printf, 3
    415        t45 = c[0]
    416        t46 = 7 int+ t45
    417        return t46


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Animal             class_tag     class Animal               -           5    -    0  size 4
   Tag                class_tag     class Tag                  -          12    -    0  size 4
   Dog                class_tag     class Dog                  -          18    -    0  size 12, public base Animal
   Vec                class_tag     class Vec                  -          31    -    0  size 8
   make               function      class Vec (int, int)       -          45    -    3  _Z4makeii; defined
   operator*          function      class Vec (class Vec, int) -          46    -    1  _Zml3Veci; defined
   main               function      int (void)                 -          48    -    0  defined

 scope: global > class Animal
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   legs               field         int                        member      7    4    4  Animal::legs; public, offset 0
   Animal             constructor   void (void)                -           8    -    0  _ZN6AnimalC1Ev; public
   count              method        int (void)                 -           9    -    1  _ZN6Animal5countEv; public, defined

 scope: global > class Tag
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     14    4    2  Tag::id; public, offset 0
   Tag                constructor   void (void)                -          15    -    0  _ZN3TagC1Ev; public

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   age                field         int                        member     20    4    6  Dog::age; public, offset 4
   tag                field         class Tag                  member     21    4    1  Dog::tag; public, offset 8
   made               field         int                        static     22    4    3  Dog::made; public, static
   Dog                constructor   void (void)                -          23    -    2  _ZN3DogC1Ev; public
   human              method        int (void)                 -          24    -    2  _ZN3Dog5humanEv; public, defined
   birthday           method        void (void)                -          25    -    1  _ZN3Dog8birthdayEv; public, defined
   total              method        int (void)                 -          26    -    1  _ZN3Dog5totalEv; public, static, defined

 scope: global > class Vec
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     33    4   24  Vec::x; public, offset 0
   y                  field         int                        member     34    4   19  Vec::y; public, offset 4
   Vec                constructor   void (void)                -          35    -    5  _ZN3VecC1Ev; public
   operator+          method        class Vec (class Vec)      -          36    -    1  _ZN3VecplES_; public, defined
   operator-          method        class Vec (void)           -          37    -    1  _ZN3VecmiEv; public, defined
   operator==         method        int (class Vec)            -          38    -    2  _ZN3VeceqES_; public, defined
   operator[]         method        int (int)                  -          39    -    1  _ZN3VecixEi; public, defined
   operator+=         method        class Vec &(class Vec)     -          40    -    1  _ZN3VecpLES_; public, defined
   operator++         method        class Vec &(void)          -          41    -    1  _ZN3VecppEv; public, defined
   operator()         method        int (int)                  -          42    -    1  _ZN3VecclEi; public, defined
   dot                method        int (class Vec)            -          43    -    1  _ZN3Vec3dotES_; public, defined

 scope: global > class Vec > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      36    8    2  o.1
   r                  variable      class Vec                  local      36    8    3  r.2

 scope: global > class Vec > operator-()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Vec                  local      37    8    3  r.3

 scope: global > class Vec > operator==()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      38    8    2  o.4

 scope: global > class Vec > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      39    4    1  i.5

 scope: global > class Vec > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      40    8    2  o.6

 scope: global > class Vec > operator()()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      42    4    1  k.7

 scope: global > class Vec > dot()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      43    8    2  o.8

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      45    4    1  a.9
   b                  parameter     int                        param      45    4    1  b.10
   v                  variable      class Vec                  local      45    8    3  v.11

 scope: global > operator*()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     class Vec                  param      46    8    2  v.12
   k                  parameter     int                        param      46    4    2  k.13

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   rex                variable      class Dog                  local      50   12    5  rex.14
   base               variable      class Animal *             local      54    4    1  base.15
   other              variable      class Dog                  local      59   12    2  other.16

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      class Vec                  local      65    8   10  a.17
   b                  variable      class Vec                  local      65    8    4  b.18
   c                  variable      class Vec                  local      65    8    7  c.19
   d                  variable      class Vec                  local      67    8    1  d.20
   e                  variable      class Vec                  local      68    8    1  e.21
   row                variable      class Vec[2]               local      73   16    3  row.22
   w                  variable      int                        local      76    4    1  w.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Animal: size 4, align 4
    +0  int legs  [public]
class Tag: size 4, align 4
    +0  int id  [public]
class Dog: size 12, align 4
    (base Animal, public)
    +4  int age  [public]
    +8  class Tag tag  [public]
    static  int made  [public]
class Vec: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
