============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 352 -> 378 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          352 -> 378   (-7% fewer)

   constants folded                        3
   algebraic simplifications               2
   common subexpressions                  82
   copies / constants forwarded          222
   temporaries merged away                 5
   dead instructions removed             173
   jumps removed or redirected             3
   unreachable instructions removed        3
   propagated across blocks                0
   dead assignments removed                3
   calls inlined                          44
   tail calls turned into jumps            0
   common subexpressions across blocks      0

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Shape::live      int                             4  0

 As three address code (initial values, in place before main runs):

    Shape::live = 0

============================================================================
 FUNCTION Shape::Shape()        (link name _ZN5ShapeC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    100     t1 = Shape::live int+ 1
    101     Shape::live = t1
    102     *this = t1
    103     param "Shape %d\n"
    104     param t1
    105     call printf, 2
    106     return

============================================================================
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    107     return 0

============================================================================
 FUNCTION Shape::name()        (link name _ZN5Shape4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    108     return 83

============================================================================
 FUNCTION Rect::Rect()        (link name _ZN4RectC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    class Rect *                    4       4
   t2               temp    class Rect *                    4       8
   t4               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    109     t4 = Shape::live int+ 1
    110     Shape::live = t4
    111     *this = t4
    112     param "Shape %d\n"
    113     param t4
    114     call printf, 2
    115     t1 = this ptr+ 4
    116     *t1 = 1
    117     t2 = this ptr+ 8
    118     *t2 = 1
    119     return

============================================================================
 FUNCTION Rect::set(int, int)        (link name _ZN4Rect3setEii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Rect *                    4      12
   t2               temp    class Rect *                    4      16

 Code: 5 instruction(s)

    120     t1 = this ptr+ 4
    121     *t1 = a
    122     t2 = this ptr+ 8
    123     *t2 = b
    124     return

============================================================================
 FUNCTION Rect::area()        (link name _ZN4Rect4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    class Rect *                    4       4
   t2               temp    int                             4       8
   t3               temp    class Rect *                    4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 6 instruction(s)

    125     t1 = this ptr+ 4
    126     t2 = *t1
    127     t3 = this ptr+ 8
    128     t4 = *t3
    129     t5 = t2 int* t4
    130     return t5

============================================================================
 FUNCTION Rect::perimeter()        (link name _ZN4Rect9perimeterEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    class Rect *                    4       4
   t2               temp    int                             4       8
   t3               temp    class Rect *                    4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24

 Code: 7 instruction(s)

    131     t1 = this ptr+ 4
    132     t2 = *t1
    133     t3 = this ptr+ 8
    134     t4 = *t3
    135     t5 = t2 int+ t4
    136     t6 = t5 int<< 1
    137     return t6

============================================================================
 FUNCTION Square::side(int)        (link name _ZN6Square4sideEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   s                param   int                             4       4
   t4               temp    class Rect *                    4      20
   t5               temp    class Rect *                    4      24
   (3 temporaries no longer used after optimization not shown)

 Code: 5 instruction(s)

    138     t4 = this ptr+ 4
    139     *t4 = s
    140     t5 = this ptr+ 8
    141     *t5 = s
    142     return

============================================================================
 FUNCTION Square::name()        (link name _ZN6Square4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    143     return 81

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    144     *this = 0
    145     t1 = this ptr+ 4
    146     *t1 = 0
    147     return

============================================================================
 FUNCTION Point::operator+=(const class Point &)        (link name _ZN5PointpLERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    class Point *                   4      20
   t5               temp    int                             4      24
   t6               temp    const class Point *             4      28
   t7               temp    int                             4      32
   t8               temp    int                             4      36
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    148     t1 = *this
    149     t2 = *o
    150     t3 = t1 int+ t2
    151     *this = t3
    152     t4 = this ptr+ 4
    153     t5 = *t4
    154     t6 = o ptr+ 4
    155     t7 = *t6
    156     t8 = t5 int+ t7
    157     *t4 = t8
    158     return this

============================================================================
 FUNCTION Point::operator-(const class Point &)        (link name _ZN5PointmiERKS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 10 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   r                local   class Point                     8       8
   t1               temp    class Point *                   4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    class Point *                   4      32
   t6               temp    int                             4      36
   t7               temp    const class Point *             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t11              temp    class Point *                   4      56
   (1 temporary no longer used after optimization not shown)

 Code: 15 instruction(s)

    159     t1 = &r
    160     *t1 = 0
    161     t11 = t1 ptr+ 4
    162     *t11 = 0
    163     t2 = *this
    164     t3 = *o
    165     t4 = t2 int- t3
    166     r[0] = t4
    167     t5 = this ptr+ 4
    168     t6 = *t5
    169     t7 = o ptr+ 4
    170     t8 = *t7
    171     t9 = t6 int- t8
    172     r[4] = t9
    173     return r

============================================================================
 FUNCTION Point::operator<(const class Point &)        (link name _ZN5PointltERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 14 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t4               temp    int                             4      20
   t5               temp    class Point *                   4      24
   t6               temp    int                             4      28
   t9               temp    int                             4      40
   t10              temp    int                             4      44
   t11              temp    int                             4      48
   t13              temp    int                             4      56
   t14              temp    const class Point *             4      60
   t15              temp    int                             4      64
   t18              temp    int                             4      76
   t19              temp    int                             4      80
   t20              temp    bool                            1      84
   (6 temporaries no longer used after optimization not shown)

 Code: 21 instruction(s)

    174       t2 = *this
    175       t4 = t2 int* t2
    176       t5 = this ptr+ 4
    177       t6 = *t5
    178       t9 = t6 int* t6
    179       t10 = t4 int+ t9
    180       t11 = *o
    181       t13 = t11 int* t11
    182       t14 = o ptr+ 4
    183       t15 = *t14
    184       t18 = t15 int* t15
    185       t19 = t13 int+ t18
    186       if t10 int< t19 goto L1
    187       t1 = 0
    188       goto L2
    189  L1:  t1 = 1
    190  L2:  if t1 int!= 0 goto L3
    191       t20 = 0
    192       goto L4
    193  L3:  t20 = 1
    194  L4:  return t20

============================================================================
 FUNCTION Point::operator[](int)        (link name _ZN5PointixEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   i                param   int                             4       4
   t1               temp    int *                           4       8
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    195       if i int!= 0 goto L5
    196       t1 = this
    197       goto L6
    198  L5:  t1 = this ptr+ 4
    199  L6:  return t1

============================================================================
 FUNCTION at(int, int)        (link name _Z2atii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   p                local   class Point                     8       8
   t1               temp    class Point *                   4      16
   t3               temp    class Point *                   4      24
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    200     t1 = &p
    201     *t1 = 0
    202     t3 = t1 ptr+ 4
    203     *t3 = 0
    204     p[0] = a
    205     p[4] = b
    206     return p

============================================================================
 FUNCTION Segment::set(int, int, int, int)        (link name _ZN7Segment3setEiiii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 7 temporaries, frame 80 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   a                param   int                             4       4
   b                param   int                             4       8
   c                param   int                             4      12
   d                param   int                             4      16
   t1               temp    class Point                     8      20
   t2               temp    class Point                     8      28
   t3               temp    class Segment *                 4      36
   t6               temp    class Point                     8      48
   t7               temp    class Point *                   4      56
   t10              temp    class Point                     8      68
   t11              temp    class Point *                   4      76
   (4 temporaries no longer used after optimization not shown)

 Code: 16 instruction(s)

    207     t7 = &t6
    208     param t7                            (this)
    209     call Point::Point(), 1
    210     t6[0] = a
    211     t6[4] = b
    212     t1 = t6
    213     *this = t1
    214     t11 = &t10
    215     param t11                           (this)
    216     call Point::Point(), 1
    217     t10[0] = c
    218     t10[4] = d
    219     t2 = t10
    220     t3 = this ptr+ 8
    221     *t3 = t2
    222     return

============================================================================
 FUNCTION Segment::length2()        (link name _ZN7Segment7length2Ev)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 16 temporaries, frame 104 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t3               temp    int                             4      24
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t12              temp    class Point                     8      60
   t13              temp    class Point *                   4      68
   t14              temp    int                             4      72
   t15              temp    int                             4      76
   t16              temp    int                             4      80
   t17              temp    class Point *                   4      84
   t18              temp    int                             4      88
   t19              temp    const class Point *             4      92
   t20              temp    int                             4      96
   t21              temp    int                             4     100
   (5 temporaries no longer used after optimization not shown)

 Code: 21 instruction(s)

    223     t1 = this ptr+ 8
    224     t13 = &t12
    225     param t13                           (this)
    226     call Point::Point(), 1
    227     t14 = *t1
    228     t15 = *this
    229     t16 = t14 int- t15
    230     t12[0] = t16
    231     t17 = t1 ptr+ 4
    232     t18 = *t17
    233     t19 = this ptr+ 4
    234     t20 = *t19
    235     t21 = t18 int- t20
    236     t12[4] = t21
    237     d = t12
    238     t3 = d[0]
    239     t5 = t3 int* t3
    240     t6 = d[4]
    241     t8 = t6 int* t6
    242     t9 = t5 int+ t8
    243     return t9

============================================================================
 FUNCTION total(class Rect &)        (link name _Z5totalR4Rect)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   class Rect &                    4       0
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t5               temp    class Rect *                    4      20
   t6               temp    int                             4      24
   t7               temp    class Rect *                    4      28
   t8               temp    int                             4      32
   t9               temp    int                             4      36
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    244     t5 = r ptr+ 4
    245     t6 = *t5
    246     t7 = r ptr+ 8
    247     t8 = *t7
    248     t9 = t6 int* t8
    249     t2 = *r
    250     t3 = t9 int+ t2
    251     return t3

============================================================================
 FUNCTION through(class Shape *)        (link name _Z7throughP5Shape)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   class Shape *                   4       0
   (5 temporaries no longer used after optimization not shown)

 Code: 1 instruction(s)

    252     return 83

============================================================================
 FUNCTION grow(class Rect *, int)        (link name _Z4growP4Recti)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   class Rect *                    4       0
   by               param   int                             4       4
   t1               temp    class Rect *                    4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t5               temp    class Rect *                    4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    253     t1 = r ptr+ 4
    254     t2 = *t1
    255     t3 = t2 int+ by
    256     *t1 = t3
    257     t5 = r ptr+ 8
    258     t6 = *t5
    259     t7 = t6 int+ by
    260     *t5 = t7
    261     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 104 temporaries, frame 1144 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   class Rect                     12       0
   q                local   class Square                   12      12
   asShape          local   class Shape *                   4      24
   alias            local   class Rect &                    4      28
   pair             local   class Rect[2]                  24      32
   a                local   class Point                     8      56
   b                local   class Point                     8      64
   c                local   class Point                     8      72
   s                local   class Segment                  16      80
   last             local   class Rect                     12      96
   base             local   class Shape *                   4     108
   t1               temp    class Rect *                    4     112
   t3               temp    class Square *                  4     120
   t25              temp    class Rect (*)[2]               4     208
   t26              temp    class Rect (*)[2]               4     212
   t32              temp    int                             4     236
   t33              temp    int                             4     240
   t36              temp    class Point *                   4     260
   t37              temp    class Point *                   4     264
   t49              temp    int                             4     312
   t53              temp    int                             4     332
   t54              temp    int                             4     336
   t55              temp    int                             4     340
   t56              temp    int                             4     344
   t59              temp    bool                            1     356
   t60              temp    int                             4     360
   t63              temp    bool                            1     372
   t64              temp    int                             4     376
   t65              temp    class Segment *                 4     380
   t66              temp    class Segment *                 4     384
   t70              temp    int                             4     400
   t71              temp    class Rect *                    4     404
   t77              temp    int                             4     428
   t79              temp    class Rect *                    4     436
   t80              temp    class Rect *                    4     440
   t87              temp    class Rect *                    4     468
   t88              temp    class Rect *                    4     472
   t93              temp    int                             4     492
   t95              temp    int                             4     500
   t96              temp    int                             4     504
   t99              temp    int                             4     516
   t101             temp    int                             4     524
   t102             temp    int                             4     528
   t108             temp    int                             4     552
   t109             temp    int                             4     556
   t111             temp    int                             4     564
   t112             temp    int                             4     568
   t113             temp    int                             4     572
   t115             temp    int                             4     580
   t116             temp    int                             4     584
   t117             temp    int                             4     588
   t123             temp    int                             4     612
   t124             temp    int                             4     616
   t126             temp    int                             4     624
   t127             temp    int                             4     628
   t132             temp    int                             4     648
   t133             temp    int                             4     652
   t139             temp    int                             4     676
   t140             temp    int                             4     680
   t142             temp    class Rect *                    4     688
   t143             temp    class Rect *                    4     692
   t145             temp    class Rect *                    4     700
   t146             temp    class Rect *                    4     704
   t149             temp    int                             4     716
   t151             temp    int                             4     724
   t152             temp    int                             4     728
   t155             temp    int                             4     740
   t157             temp    int                             4     748
   t158             temp    int                             4     752
   t161             temp    class Point                     8     764
   t162             temp    class Point *                   4     772
   t165             temp    class Point                     8     784
   t166             temp    class Point *                   4     792
   t169             temp    int                             4     804
   t170             temp    int                             4     808
   t171             temp    int                             4     812
   t172             temp    class Point *                   4     816
   t173             temp    int                             4     820
   t174             temp    const class Point *             4     824
   t175             temp    int                             4     828
   t176             temp    int                             4     832
   t179             temp    int                             4     844
   t180             temp    int                             4     848
   t181             temp    int                             4     852
   t183             temp    int                             4     860
   t185             temp    int                             4     868
   t186             temp    int                             4     872
   t189             temp    int                             4     884
   t190             temp    int                             4     888
   t191             temp    int                             4     892
   t193             temp    int                             4     900
   t195             temp    int                             4     908
   t196             temp    int                             4     912
   t205             temp    class Point                     8     948
   t206             temp    class Point *                   4     956
   t207             temp    int                             4     960
   t208             temp    int                             4     964
   t209             temp    int                             4     968
   t211             temp    int                             4     976
   t213             temp    int                             4     984
   t214             temp    int                             4     988
   t216             temp    class Point *                   4     996
   t218             temp    class Point *                   4    1004
   t224             temp    class Point                     8    1028
   t225             temp    class Point                     8    1036
   t229             temp    class Point                     8    1056
   t230             temp    int                             4    1064
   t231             temp    int                             4    1068
   t232             temp    int                             4    1072
   t233             temp    int                             4    1076
   t234             temp    int                             4    1080
   t236             temp    class Rect *                    4    1088
   t237             temp    class Rect *                    4    1092
   t245             temp    int                             4    1124
   t248             temp    int                             4    1136
   (145 temporaries no longer used after optimization not shown)

 Code: 216 instruction(s)

    262     t1 = &r
    263     param t1                            (this)
    264     call Shape::Shape(), 1
    265     t79 = t1 ptr+ 4
    266     *t79 = 1
    267     t80 = t1 ptr+ 8
    268     *t80 = 1
    269     *t79 = 3
    270     *t80 = 4
    271     t3 = &q
    272     param t3                            (this)
    273     call Shape::Shape(), 1
    274     t87 = t3 ptr+ 4
    275     *t87 = 1
    276     t88 = t3 ptr+ 8
    277     *t88 = 1
    278     param t3                            (this)
    279     param 5
    280     param 5
    281     call Rect::set(int, int), 3
    282     t93 = *t79
    283     t95 = *t80
    284     t96 = t93 int* t95
    285     t99 = *t87
    286     t101 = *t88
    287     t102 = t99 int* t101
    288     t108 = t99 int+ t101
    289     t109 = t108 int<< 1
    290     param "%d %d %d %d\n"
    291     param t96
    292     param t102
    293     param t109
    294     param Shape::live
    295     call printf, 5
    296     param t1                            (this)
    297     t111 = call Rect::area(), 1
    298     t112 = *t1
    299     t113 = t111 int+ t112
    300     param t3                            (this)
    301     t115 = call Shape::area(), 1
    302     param t3                            (this)
    303     t116 = call Shape::name(), 1
    304     t117 = t115 int+ t116
    305     param "%d %d %c %c\n"
    306     param t113
    307     param t117
    308     param 81
    309     param 83
    310     call printf, 5
    311     t123 = *t87
    312     t124 = t123 int+ 1
    313     *t87 = t124
    314     t126 = *t88
    315     t127 = t126 int+ 1
    316     *t88 = t127
    317     *t87 = 10
    318     t132 = *t88
    319     t133 = t132 int* 10
    320     t139 = 10 int+ t132
    321     t140 = t139 int<< 1
    322     param "%d %d\n"
    323     param t133
    324     param t140
    325     call printf, 3
    326     t25 = &pair
    327     param t25                           (this)
    328     call Shape::Shape(), 1
    329     t142 = t25 ptr+ 4
    330     *t142 = 1
    331     t143 = t25 ptr+ 8
    332     *t143 = 1
    333     t26 = t25 ptr+ 12
    334     param t26                           (this)
    335     call Shape::Shape(), 1
    336     t145 = t26 ptr+ 4
    337     *t145 = 1
    338     t146 = t26 ptr+ 8
    339     *t146 = 1
    340     pair[16] = 6
    341     t149 = *t142
    342     t151 = *t143
    343     t152 = t149 int* t151
    344     t155 = *t145
    345     t157 = *t146
    346     t158 = t155 int* t157
    347     t32 = t152 int+ t158
    348     t33 = pair[12]
    349     param "%d %d %d\n"
    350     param t32
    351     param t33
    352     param Shape::live
    353     call printf, 4
    354     param "%d\n"
    355     param Shape::live
    356     call printf, 2
    357     t162 = &t161
    358     param t162                          (this)
    359     call Point::Point(), 1
    360     t161[0] = 3
    361     t161[4] = 4
    362     a = t161
    363     t166 = &t165
    364     param t166                          (this)
    365     call Point::Point(), 1
    366     t165[0] = 1
    367     t165[4] = 1
    368     b = t165
    369     t36 = &a
    370     t37 = &b
    371     t169 = *t36
    372     t170 = *t37
    373     t171 = t169 int+ t170
    374     *t36 = t171
    375     t172 = t36 ptr+ 4
    376     t173 = *t172
    377     t174 = t37 ptr+ 4
    378     t175 = *t174
    379     t176 = t173 int+ t175
    380     *t172 = t176
    381     t179 = *t36
    382     t180 = *t37
    383     t181 = t179 int+ t180
    384     *t36 = t181
    385     t183 = *t172
    386     t185 = *t174
    387     t186 = t183 int+ t185
    388     *t172 = t186
    389     t189 = *t36
    390     t190 = *t37
    391     t191 = t189 int+ t190
    392     *t36 = t191
    393     t193 = *t172
    394     t195 = *t174
    395     t196 = t193 int+ t195
    396     *t172 = t196
    397     t49 = t196 int<< 1
    398     *t36 = t49
    399     t206 = &t205
    400     param t206                          (this)
    401     call Point::Point(), 1
    402     t207 = *t36
    403     t208 = *t37
    404     t209 = t207 int- t208
    405     t205[0] = t209
    406     t211 = *t172
    407     t213 = *t174
    408     t214 = t211 int- t213
    409     t205[4] = t214
    410     c = t205
    411     t53 = a[0]
    412     t54 = a[4]
    413     t55 = c[0]
    414     t56 = c[4]
    415     param t37                           (this)
    416     param t36
    417     t59 = call Point::operator<(const class Point &), 2
    418     t60 = booltoint t59
    419     param t36                           (this)
    420     param t37
    421     t63 = call Point::operator<(const class Point &), 2
    422     t64 = booltoint t63
    423     param "%d %d %d %d %d %d\n"
    424     param t53
    425     param t54
    426     param t55
    427     param t56
    428     param t60
    429     param t64
    430     call printf, 7
    431     t65 = &s
    432     *t65 = 0
    433     t216 = t65 ptr+ 4
    434     *t216 = 0
    435     t66 = t65 ptr+ 8
    436     *t66 = 0
    437     t218 = t66 ptr+ 4
    438     *t218 = 0
    439     param 1
    440     param 2
    441     t224 = call at(int, int), 2
    442     *t65 = t224
    443     param 4
    444     param 6
    445     t225 = call at(int, int), 2
    446     *t66 = t225
    447     param t66                           (this)
    448     param t65
    449     t229 = call Point::operator-(const class Point &), 2
    450     t230 = t229[0]
    451     t231 = t230 int* t230
    452     t232 = t229[4]
    453     t233 = t232 int* t232
    454     t234 = t231 int+ t233
    455     t70 = s[12]
    456     param "%d %d\n"
    457     param t234
    458     param t70
    459     call printf, 3
    460     t71 = &last
    461     param t71                           (this)
    462     call Shape::Shape(), 1
    463     t236 = t71 ptr+ 4
    464     *t236 = 1
    465     t237 = t71 ptr+ 8
    466     *t237 = 1
    467     *t236 = 2
    468     *t237 = 9
    469     t245 = *t236
    470     t248 = t245 int* 9
    471     t77 = *t71
    472     param "%d %d %d\n"
    473     param t248
    474     param 0
    475     param t77
    476     call printf, 4
    477     return Shape::live


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Shape              class_tag     class Shape                -           5    -    0  size 4
   Rect               class_tag     class Rect                 -          15    -    0  size 12, public base Shape
   Square             class_tag     class Square               -          24    -    0  size 12, public base Rect
   Point              class_tag     class Point                -          30    -    0  size 8
   at                 function      class Point (int, int)     -          39    -    4  _Z2atii; defined
   Segment            class_tag     class Segment              -          41    -    0  size 16
   total              function      int (class Rect &)         -          48    -    1  _Z5totalR4Rect; defined
   through            function      int (class Shape *)        -          49    -    1  _Z7throughP5Shape; defined
   grow               function      void (class Rect *, int)   -          50    -    1  _Z4growP4Recti; defined
   main               function      int (void)                 -          52    -    0  defined

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      7    4    5  Shape::id; public, offset 0
   live               field         int                        static      8    4    5  Shape::live; public, static
   Shape              constructor   void (void)                -           9    -    0  _ZN5ShapeC1Ev; public
   area               method        int (void)                 -          10    -    2  _ZN5Shape4areaEv; public, defined
   name               method        int (void)                 -          11    -    2  _ZN5Shape4nameEv; public, defined

 scope: global > class Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  field         int                        member     17    4    7  Rect::w; public, offset 4
   h                  field         int                        member     17    4    5  Rect::h; public, offset 8
   Rect               constructor   void (void)                -          18    -    3  _ZN4RectC1Ev; public
   set                method        void (int, int)            -          19    -    3  _ZN4Rect3setEii; public, defined
   area               method        int (void)                 -          20    -    7  _ZN4Rect4areaEv; public, defined
   perimeter          method        int (void)                 -          21    -    2  _ZN4Rect9perimeterEv; public, defined

 scope: global > class Rect > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      19    4    1  a.1
   b                  parameter     int                        param      19    4    1  b.2

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   side               method        void (int)                 -          26    -    1  _ZN6Square4sideEi; public, defined
   name               method        int (void)                 -          27    -    1  _ZN6Square4nameEv; public, defined

 scope: global > class Square > side()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     int                        param      26    4    2  s.3

 scope: global > class Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     32    4   16  Point::x; public, offset 0
   y                  field         int                        member     32    4   17  Point::y; public, offset 4
   Point              constructor   void (void)                -          33    -    2  _ZN5PointC1Ev; public
   operator+=         method        class Point &(const class Point &) -          34    -    3  _ZN5PointpLERKS_; public, defined
   operator-          method        class Point (const class Point &) -          35    -    2  _ZN5PointmiERKS_; public, defined
   operator<          method        bool (const class Point &) -          36    -    2  _ZN5PointltERKS_; public, defined
   operator[]         method        int &(int)                 -          37    -    2  _ZN5PointixEi; public, defined

 scope: global > class Point > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      34    4    2  o.4

 scope: global > class Point > operator-()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      35    4    2  o.5
   r                  variable      class Point                local      35    8    3  r.6

 scope: global > class Point > operator<()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      36    4    4  o.7

 scope: global > class Point > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      37    4    1  i.8

 scope: global > at()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      39    4    1  a.9
   b                  parameter     int                        param      39    4    1  b.10
   p                  variable      class Point                local      39    8    3  p.11

 scope: global > class Segment
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   from               field         class Point                member     43    8    2  Segment::from; public, offset 0
   to                 field         class Point                member     43    8    3  Segment::to; public, offset 8
   set                method        void (int, int, int, int)  -          44    -    1  _ZN7Segment3setEiiii; public, defined
   length2            method        int (void)                 -          45    -    1  _ZN7Segment7length2Ev; public, defined

 scope: global > class Segment > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      44    4    1  a.12
   b                  parameter     int                        param      44    4    1  b.13
   c                  parameter     int                        param      44    4    1  c.14
   d                  parameter     int                        param      44    4    1  d.15

 scope: global > class Segment > length2()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      class Point                local      45    8    4  d.16

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect &               param      48    4    2  r.17

 scope: global > through()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     class Shape *              param      49    4    2  s.18

 scope: global > grow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect *               param      50    4    2  r.19
   by                 parameter     int                        param      50    4    2  by.20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Rect                 local      53   12    3  r.21
   q                  variable      class Square               local      55   12    9  q.22
   asShape            variable      class Shape *              local      58    4    1  asShape.23
   alias              variable      class Rect &               local      61    4    2  alias.24
   a                  variable      class Point                local      71    8    9  a.26
   b                  variable      class Point                local      71    8    6  b.27
   c                  variable      class Point                local      75    8    2  c.28
   s                  variable      class Segment              local      77   16    3  s.29

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pair               variable      class Rect[2]              local      65   24    4  pair.25
   last               variable      class Rect                 local      82   12    3  last.30
   base               variable      class Shape *              local      84    4    2  base.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Shape: size 4, align 4
    +0  int id  [public]
    static  int live  [public]
class Rect: size 12, align 4
    (base Shape, public)
    +4  int w  [public]
    +8  int h  [public]
class Square: size 12, align 4
    (base Rect, public)
class Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
class Segment: size 16, align 4
    +0  class Point from  [public]
    +8  class Point to  [public]
