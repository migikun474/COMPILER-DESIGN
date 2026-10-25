============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 378 -> 391 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          378 -> 391   (-3% fewer)

   constants folded                        3
   algebraic simplifications               2
   common subexpressions                  87
   copies / constants forwarded          230
   temporaries merged away                 5
   dead instructions removed             183
   jumps removed or redirected             3
   unreachable instructions removed        3
   propagated across blocks                0
   dead assignments removed                3
   calls inlined                          45
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         0

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
 FUNCTION Shape::~Shape()        (link name _ZN5ShapeD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 6 instruction(s)

    107     t1 = *this
    108     param "~Shape %d\n"
    109     param t1
    110     call printf, 2
    111     Shape::live = Shape::live int- 1
    112     return

============================================================================
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    113     return 0

============================================================================
 FUNCTION Shape::name()        (link name _ZN5Shape4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    114     return 83

============================================================================
 FUNCTION Rect::Rect(int, int)        (link name _ZN4RectC1Eii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Rect *                    4      12
   t2               temp    class Rect *                    4      16
   t4               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    115     t4 = Shape::live int+ 1
    116     Shape::live = t4
    117     *this = t4
    118     param "Shape %d\n"
    119     param t4
    120     call printf, 2
    121     t1 = this ptr+ 4
    122     *t1 = a
    123     t2 = this ptr+ 8
    124     *t2 = b
    125     return

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

    126     t4 = Shape::live int+ 1
    127     Shape::live = t4
    128     *this = t4
    129     param "Shape %d\n"
    130     param t4
    131     call printf, 2
    132     t1 = this ptr+ 4
    133     *t1 = 1
    134     t2 = this ptr+ 8
    135     *t2 = 1
    136     return

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

    137     t1 = this ptr+ 4
    138     t2 = *t1
    139     t3 = this ptr+ 8
    140     t4 = *t3
    141     t5 = t2 int* t4
    142     return t5

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

    143     t1 = this ptr+ 4
    144     t2 = *t1
    145     t3 = this ptr+ 8
    146     t4 = *t3
    147     t5 = t2 int+ t4
    148     t6 = t5 int<< 1
    149     return t6

============================================================================
 FUNCTION Square::Square(int)        (link name _ZN6SquareC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   side             param   int                             4       4
   t4               temp    class Rect *                    4      20
   t5               temp    class Rect *                    4      24
   (3 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    150     param this                          (this)
    151     call Shape::Shape(), 1
    152     t4 = this ptr+ 4
    153     *t4 = 1
    154     t5 = this ptr+ 8
    155     *t5 = 1
    156     *t4 = side
    157     *t5 = side
    158     return

============================================================================
 FUNCTION Square::name()        (link name _ZN6Square4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    159     return 81

============================================================================
 FUNCTION Point::Point(int, int)        (link name _ZN5PointC1Eii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Point *                   4      12

 Code: 4 instruction(s)

    160     *this = a
    161     t1 = this ptr+ 4
    162     *t1 = b
    163     return

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    164     *this = 0
    165     t1 = this ptr+ 4
    166     *t1 = 0
    167     return

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

    168     t1 = *this
    169     t2 = *o
    170     t3 = t1 int+ t2
    171     *this = t3
    172     t4 = this ptr+ 4
    173     t5 = *t4
    174     t6 = o ptr+ 4
    175     t7 = *t6
    176     t8 = t5 int+ t7
    177     *t4 = t8
    178     return this

============================================================================
 FUNCTION Point::operator-(const class Point &)        (link name _ZN5PointmiERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 11 temporaries, frame 68 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   t1               temp    class Point                     8       8
   t2               temp    class Point *                   4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24
   t5               temp    int                             4      28
   t6               temp    class Point *                   4      32
   t7               temp    int                             4      36
   t8               temp    const class Point *             4      40
   t9               temp    int                             4      44
   t10              temp    int                             4      48
   t14              temp    class Point *                   4      64
   (3 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    179     t2 = &t1
    180     t3 = *this
    181     t4 = *o
    182     t5 = t3 int- t4
    183     t6 = this ptr+ 4
    184     t7 = *t6
    185     t8 = o ptr+ 4
    186     t9 = *t8
    187     t10 = t7 int- t9
    188     *t2 = t5
    189     t14 = t2 ptr+ 4
    190     *t14 = t10
    191     return t1

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

    192       t2 = *this
    193       t4 = t2 int* t2
    194       t5 = this ptr+ 4
    195       t6 = *t5
    196       t9 = t6 int* t6
    197       t10 = t4 int+ t9
    198       t11 = *o
    199       t13 = t11 int* t11
    200       t14 = o ptr+ 4
    201       t15 = *t14
    202       t18 = t15 int* t15
    203       t19 = t13 int+ t18
    204       if t10 int< t19 goto L1
    205       t1 = 0
    206       goto L2
    207  L1:  t1 = 1
    208  L2:  if t1 int!= 0 goto L3
    209       t20 = 0
    210       goto L4
    211  L3:  t20 = 1
    212  L4:  return t20

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

    213       if i int!= 0 goto L5
    214       t1 = this
    215       goto L6
    216  L5:  t1 = this ptr+ 4
    217  L6:  return t1

============================================================================
 FUNCTION Segment::Segment(int, int, int, int)        (link name _ZN7SegmentC1Eiiii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 9 temporaries, frame 100 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   a                param   int                             4       4
   b                param   int                             4       8
   c                param   int                             4      12
   d                param   int                             4      16
   t1               temp    class Segment *                 4      20
   t2               temp    class Point                     8      24
   t3               temp    class Point *                   4      32
   t4               temp    class Point                     8      36
   t5               temp    class Point *                   4      44
   t8               temp    class Point *                   4      56
   t10              temp    class Point *                   4      64
   t14              temp    class Point *                   4      80
   t18              temp    class Point *                   4      96
   (9 temporaries no longer used after optimization not shown)

 Code: 18 instruction(s)

    218     *this = 0
    219     t8 = this ptr+ 4
    220     *t8 = 0
    221     t1 = this ptr+ 8
    222     *t1 = 0
    223     t10 = t1 ptr+ 4
    224     *t10 = 0
    225     t3 = &t2
    226     *t3 = a
    227     t14 = t3 ptr+ 4
    228     *t14 = b
    229     *this = t2
    230     t5 = &t4
    231     *t5 = c
    232     t18 = t5 ptr+ 4
    233     *t18 = d
    234     *t1 = t4
    235     return

============================================================================
 FUNCTION Segment::length2()        (link name _ZN7Segment7length2Ev)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 16 temporaries, frame 112 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t5               temp    int                             4      32
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t10              temp    int                             4      52
   t11              temp    int                             4      56
   t14              temp    class Point                     8      68
   t15              temp    class Point *                   4      76
   t16              temp    int                             4      80
   t17              temp    int                             4      84
   t18              temp    int                             4      88
   t19              temp    class Point *                   4      92
   t20              temp    int                             4      96
   t21              temp    const class Point *             4     100
   t22              temp    int                             4     104
   t23              temp    int                             4     108
   (7 temporaries no longer used after optimization not shown)

 Code: 21 instruction(s)

    236     t1 = this ptr+ 8
    237     t15 = &t14
    238     t16 = *t1
    239     t17 = *this
    240     t18 = t16 int- t17
    241     t19 = t1 ptr+ 4
    242     t20 = *t19
    243     t21 = this ptr+ 4
    244     t22 = *t21
    245     t23 = t20 int- t22
    246     param t15                           (this)
    247     param t18
    248     param t23
    249     call Point::Point(int, int), 3
    250     d = t14
    251     t5 = d[0]
    252     t7 = t5 int* t5
    253     t8 = d[4]
    254     t10 = t8 int* t8
    255     t11 = t7 int+ t10
    256     return t11

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

    257     t5 = r ptr+ 4
    258     t6 = *t5
    259     t7 = r ptr+ 8
    260     t8 = *t7
    261     t9 = t6 int* t8
    262     t2 = *r
    263     t3 = t9 int+ t2
    264     return t3

============================================================================
 FUNCTION through(class Shape *)        (link name _Z7throughP5Shape)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   class Shape *                   4       0
   (5 temporaries no longer used after optimization not shown)

 Code: 1 instruction(s)

    265     return 83

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

    266     t1 = r ptr+ 4
    267     t2 = *t1
    268     t3 = t2 int+ by
    269     *t1 = t3
    270     t5 = r ptr+ 8
    271     t6 = *t5
    272     t7 = t6 int+ by
    273     *t5 = t7
    274     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 100 temporaries, frame 1108 bytes

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
   t2               temp    class Square *                  4     116
   t23              temp    class Rect (*)[2]               4     200
   t24              temp    class Rect (*)[2]               4     204
   t30              temp    int                             4     228
   t31              temp    int                             4     232
   t35              temp    class Point *                   4     248
   t36              temp    class Point *                   4     252
   t50              temp    int                             4     308
   t56              temp    int                             4     336
   t57              temp    int                             4     340
   t58              temp    int                             4     344
   t59              temp    int                             4     348
   t62              temp    bool                            1     360
   t63              temp    int                             4     364
   t66              temp    bool                            1     376
   t67              temp    int                             4     380
   t68              temp    class Segment *                 4     384
   t71              temp    int                             4     396
   t72              temp    class Rect *                    4     400
   t77              temp    int                             4     420
   t79              temp    int                             4     428
   t85              temp    class Rect *                    4     452
   t86              temp    class Rect *                    4     456
   t89              temp    class Square *                  4     468
   t90              temp    class Square *                  4     472
   t93              temp    int                             4     484
   t95              temp    int                             4     492
   t96              temp    int                             4     496
   t99              temp    int                             4     508
   t102             temp    int                             4     520
   t108             temp    int                             4     544
   t109             temp    int                             4     548
   t111             temp    int                             4     556
   t112             temp    int                             4     560
   t113             temp    int                             4     564
   t115             temp    int                             4     572
   t116             temp    int                             4     576
   t117             temp    int                             4     580
   t123             temp    int                             4     604
   t124             temp    int                             4     608
   t126             temp    int                             4     616
   t127             temp    int                             4     620
   t132             temp    int                             4     640
   t133             temp    int                             4     644
   t139             temp    int                             4     668
   t140             temp    int                             4     672
   t142             temp    class Rect *                    4     680
   t143             temp    class Rect *                    4     684
   t145             temp    class Rect *                    4     692
   t146             temp    class Rect *                    4     696
   t149             temp    int                             4     708
   t151             temp    int                             4     716
   t152             temp    int                             4     720
   t155             temp    int                             4     732
   t157             temp    int                             4     740
   t158             temp    int                             4     744
   t160             temp    int                             4     752
   t162             temp    int                             4     760
   t166             temp    class Point *                   4     776
   t170             temp    class Point *                   4     792
   t173             temp    int                             4     804
   t174             temp    int                             4     808
   t175             temp    int                             4     812
   t177             temp    int                             4     820
   t179             temp    int                             4     828
   t180             temp    int                             4     832
   t183             temp    int                             4     844
   t184             temp    int                             4     848
   t185             temp    int                             4     852
   t187             temp    int                             4     860
   t189             temp    int                             4     868
   t190             temp    int                             4     872
   t193             temp    int                             4     884
   t194             temp    int                             4     888
   t195             temp    int                             4     892
   t197             temp    int                             4     900
   t199             temp    int                             4     908
   t200             temp    int                             4     912
   t209             temp    class Point                     8     948
   t210             temp    class Point *                   4     956
   t212             temp    int                             4     964
   t213             temp    int                             4     968
   t215             temp    int                             4     976
   t217             temp    int                             4     984
   t218             temp    int                             4     988
   t220             temp    class Segment *                 4     996
   t222             temp    class Point                     8    1008
   t223             temp    int                             4    1016
   t224             temp    int                             4    1020
   t225             temp    int                             4    1024
   t226             temp    int                             4    1028
   t227             temp    int                             4    1032
   t231             temp    class Rect *                    4    1048
   t232             temp    class Rect *                    4    1052
   t235             temp    int                             4    1064
   t238             temp    int                             4    1076
   t241             temp    int                             4    1088
   t243             temp    int                             4    1096
   t245             temp    int                             4    1104
   (145 temporaries no longer used after optimization not shown)

 Code: 216 instruction(s)

    275     t1 = &r
    276     param t1                            (this)
    277     call Shape::Shape(), 1
    278     t85 = t1 ptr+ 4
    279     *t85 = 3
    280     t86 = t1 ptr+ 8
    281     *t86 = 4
    282     t2 = &q
    283     param t2                            (this)
    284     call Rect::Rect(), 1
    285     t89 = t2 ptr+ 4
    286     *t89 = 5
    287     t90 = t2 ptr+ 8
    288     *t90 = 5
    289     t93 = *t85
    290     t95 = *t86
    291     t96 = t93 int* t95
    292     t99 = *t89
    293     t102 = t99 int* 5
    294     t108 = t99 int+ 5
    295     t109 = t108 int<< 1
    296     param "%d %d %d %d\n"
    297     param t96
    298     param t102
    299     param t109
    300     param Shape::live
    301     call printf, 5
    302     param t1                            (this)
    303     t111 = call Rect::area(), 1
    304     t112 = *t1
    305     t113 = t111 int+ t112
    306     param t2                            (this)
    307     t115 = call Shape::area(), 1
    308     param t2                            (this)
    309     t116 = call Shape::name(), 1
    310     t117 = t115 int+ t116
    311     param "%d %d %c %c\n"
    312     param t113
    313     param t117
    314     param 81
    315     param 83
    316     call printf, 5
    317     t123 = *t89
    318     t124 = t123 int+ 1
    319     *t89 = t124
    320     t126 = *t90
    321     t127 = t126 int+ 1
    322     *t90 = t127
    323     *t89 = 10
    324     t132 = *t90
    325     t133 = t132 int* 10
    326     t139 = 10 int+ t132
    327     t140 = t139 int<< 1
    328     param "%d %d\n"
    329     param t133
    330     param t140
    331     call printf, 3
    332     t23 = &pair
    333     param t23                           (this)
    334     call Shape::Shape(), 1
    335     t142 = t23 ptr+ 4
    336     *t142 = 1
    337     t143 = t23 ptr+ 8
    338     *t143 = 1
    339     t24 = t23 ptr+ 12
    340     param t24                           (this)
    341     call Shape::Shape(), 1
    342     t145 = t24 ptr+ 4
    343     *t145 = 1
    344     t146 = t24 ptr+ 8
    345     *t146 = 1
    346     pair[16] = 6
    347     t149 = *t142
    348     t151 = *t143
    349     t152 = t149 int* t151
    350     t155 = *t145
    351     t157 = *t146
    352     t158 = t155 int* t157
    353     t30 = t152 int+ t158
    354     t31 = pair[12]
    355     param "%d %d %d\n"
    356     param t30
    357     param t31
    358     param Shape::live
    359     call printf, 4
    360     t160 = *t24
    361     param "~Shape %d\n"
    362     param t160
    363     call printf, 2
    364     Shape::live = Shape::live int- 1
    365     t162 = *t23
    366     param "~Shape %d\n"
    367     param t162
    368     call printf, 2
    369     Shape::live = Shape::live int- 1
    370     param "%d\n"
    371     param Shape::live
    372     call printf, 2
    373     t35 = &a
    374     *t35 = 3
    375     t166 = t35 ptr+ 4
    376     *t166 = 4
    377     t36 = &b
    378     *t36 = 1
    379     t170 = t36 ptr+ 4
    380     *t170 = 1
    381     t173 = *t35
    382     t174 = *t36
    383     t175 = t173 int+ t174
    384     *t35 = t175
    385     t177 = *t166
    386     t179 = *t170
    387     t180 = t177 int+ t179
    388     *t166 = t180
    389     t183 = *t35
    390     t184 = *t36
    391     t185 = t183 int+ t184
    392     *t35 = t185
    393     t187 = *t166
    394     t189 = *t170
    395     t190 = t187 int+ t189
    396     *t166 = t190
    397     t193 = *t35
    398     t194 = *t36
    399     t195 = t193 int+ t194
    400     *t35 = t195
    401     t197 = *t166
    402     t199 = *t170
    403     t200 = t197 int+ t199
    404     *t166 = t200
    405     t50 = t200 int<< 1
    406     *t35 = t50
    407     t210 = &t209
    408     t212 = *t36
    409     t213 = t50 int- t212
    410     t215 = *t166
    411     t217 = *t170
    412     t218 = t215 int- t217
    413     param t210                          (this)
    414     param t213
    415     param t218
    416     call Point::Point(int, int), 3
    417     c = t209
    418     t56 = a[0]
    419     t57 = a[4]
    420     t58 = c[0]
    421     t59 = c[4]
    422     param t36                           (this)
    423     param t35
    424     t62 = call Point::operator<(const class Point &), 2
    425     t63 = booltoint t62
    426     param t35                           (this)
    427     param t36
    428     t66 = call Point::operator<(const class Point &), 2
    429     t67 = booltoint t66
    430     param "%d %d %d %d %d %d\n"
    431     param t56
    432     param t57
    433     param t58
    434     param t59
    435     param t63
    436     param t67
    437     call printf, 7
    438     t68 = &s
    439     param t68                           (this)
    440     param 1
    441     param 2
    442     param 4
    443     param 6
    444     call Segment::Segment(int, int, int, int), 5
    445     t220 = t68 ptr+ 8
    446     param t220                          (this)
    447     param t68
    448     t222 = call Point::operator-(const class Point &), 2
    449     t223 = t222[0]
    450     t224 = t223 int* t223
    451     t225 = t222[4]
    452     t226 = t225 int* t225
    453     t227 = t224 int+ t226
    454     t71 = s[12]
    455     param "%d %d\n"
    456     param t227
    457     param t71
    458     call printf, 3
    459     t72 = &last
    460     param t72                           (this)
    461     call Shape::Shape(), 1
    462     t231 = t72 ptr+ 4
    463     *t231 = 2
    464     t232 = t72 ptr+ 8
    465     *t232 = 9
    466     t235 = *t231
    467     t238 = t235 int* 9
    468     t77 = *t72
    469     param "%d %d %d\n"
    470     param t238
    471     param 0
    472     param t77
    473     call printf, 4
    474     t241 = *t72
    475     param "~Shape %d\n"
    476     param t241
    477     call printf, 2
    478     Shape::live = Shape::live int- 1
    479     t79 = Shape::live
    480     t243 = *t2
    481     param "~Shape %d\n"
    482     param t243
    483     call printf, 2
    484     Shape::live = Shape::live int- 1
    485     t245 = *t1
    486     param "~Shape %d\n"
    487     param t245
    488     call printf, 2
    489     Shape::live = Shape::live int- 1
    490     return t79


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Shape              class_tag     class Shape                -           6    -    0  size 4
   Rect               class_tag     class Rect                 -          17    -    0  size 12, public base Shape
   Square             class_tag     class Square               -          26    -    0  size 12, public base Rect
   Point              class_tag     class Point                -          32    -    0  size 8
   Segment            class_tag     class Segment              -          43    -    0  size 16
   total              function      int (class Rect &)         -          50    -    1  _Z5totalR4Rect; defined
   through            function      int (class Shape *)        -          51    -    1  _Z7throughP5Shape; defined
   grow               function      void (class Rect *, int)   -          52    -    1  _Z4growP4Recti; defined
   main               function      int (void)                 -          54    -    0  defined

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      8    4    6  Shape::id; public, offset 0
   live               field         int                        static      9    4    6  Shape::live; public, static
   Shape              constructor   void (void)                -          10    -    2  _ZN5ShapeC1Ev; public
   ~Shape             destructor    void (void)                -          11    -    0  _ZN5ShapeD1Ev; public
   area               method        int (void)                 -          12    -    2  _ZN5Shape4areaEv; public, defined
   name               method        int (void)                 -          13    -    2  _ZN5Shape4nameEv; public, defined

 scope: global > class Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  field         int                        member     19    4    8  Rect::w; public, offset 4
   h                  field         int                        member     19    4    6  Rect::h; public, offset 8
   Rect               constructor   void (int, int)            -          20    -    2  _ZN4RectC1Eii; public
   Rect               constructor   void (void)                -          21    -    2  _ZN4RectC1Ev; public
   area               method        int (void)                 -          22    -    7  _ZN4Rect4areaEv; public, defined
   perimeter          method        int (void)                 -          23    -    2  _ZN4Rect9perimeterEv; public, defined

 scope: global > class Rect > Rect()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      20    4    1  a.1
   b                  parameter     int                        param      20    4    1  b.2

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Square             constructor   void (int)                 -          28    -    1  _ZN6SquareC1Ei; public
   name               method        int (void)                 -          29    -    1  _ZN6Square4nameEv; public, defined

 scope: global > class Square > Square()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   side               parameter     int                        param      28    4    2  side.3

 scope: global > class Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     34    4   15  Point::x; public, offset 0
   y                  field         int                        member     34    4   16  Point::y; public, offset 4
   Point              constructor   void (int, int)            -          35    -    5  _ZN5PointC1Eii; public
   Point              constructor   void (void)                -          36    -    2  _ZN5PointC1Ev; public
   operator+=         method        class Point &(const class Point &) -          37    -    3  _ZN5PointpLERKS_; public, defined
   operator-          method        class Point (const class Point &) -          38    -    2  _ZN5PointmiERKS_; public, defined
   operator<          method        bool (const class Point &) -          39    -    2  _ZN5PointltERKS_; public, defined
   operator[]         method        int &(int)                 -          40    -    2  _ZN5PointixEi; public, defined

 scope: global > class Point > Point()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      35    4    1  a.4
   b                  parameter     int                        param      35    4    1  b.5

 scope: global > class Point > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      37    4    2  o.6

 scope: global > class Point > operator-()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      38    4    2  o.7

 scope: global > class Point > operator<()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      39    4    4  o.8

 scope: global > class Point > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      40    4    1  i.9

 scope: global > class Segment
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   from               field         class Point                member     45    8    2  Segment::from; public, offset 0
   to                 field         class Point                member     45    8    3  Segment::to; public, offset 8
   Segment            constructor   void (int, int, int, int)  -          46    -    1  _ZN7SegmentC1Eiiii; public
   length2            method        int (void)                 -          47    -    1  _ZN7Segment7length2Ev; public, defined

 scope: global > class Segment > Segment()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      46    4    1  a.10
   b                  parameter     int                        param      46    4    1  b.11
   c                  parameter     int                        param      46    4    1  c.12
   d                  parameter     int                        param      46    4    1  d.13

 scope: global > class Segment > length2()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      class Point                local      47    8    4  d.14

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect &               param      50    4    2  r.15

 scope: global > through()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     class Shape *              param      51    4    2  s.16

 scope: global > grow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect *               param      52    4    2  r.17
   by                 parameter     int                        param      52    4    2  by.18

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Rect                 local      55   12    2  r.19
   q                  variable      class Square               local      56   12    8  q.20
   asShape            variable      class Shape *              local      58    4    1  asShape.21
   alias              variable      class Rect &               local      61    4    2  alias.22
   a                  variable      class Point                local      71    8    9  a.24
   b                  variable      class Point                local      71    8    6  b.25
   c                  variable      class Point                local      75    8    2  c.26
   s                  variable      class Segment              local      77   16    2  s.27

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pair               variable      class Rect[2]              local      65   24    4  pair.23
   last               variable      class Rect                 local      81   12    2  last.28
   base               variable      class Shape *              local      82    4    2  base.29

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
