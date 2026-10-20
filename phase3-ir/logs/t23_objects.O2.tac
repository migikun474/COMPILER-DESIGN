============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 378 -> 320 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          378 -> 320   (15% fewer)

   constants folded                        0
   algebraic simplifications               2
   common subexpressions                  48
   copies / constants forwarded           53
   temporaries merged away                 2
   dead instructions removed              54
   jumps removed or redirected             1
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                3

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Shape::live      int                             4  0

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

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Rect *                    4      12
   t2               temp    class Rect *                    4      16

 Code: 7 instruction(s)

    115     param this                          (this)
    116     call Shape::Shape(), 1
    117     t1 = this ptr+ 4
    118     *t1 = a
    119     t2 = this ptr+ 8
    120     *t2 = b
    121     return

============================================================================
 FUNCTION Rect::Rect()        (link name _ZN4RectC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    class Rect *                    4       4
   t2               temp    class Rect *                    4       8

 Code: 7 instruction(s)

    122     param this                          (this)
    123     call Shape::Shape(), 1
    124     t1 = this ptr+ 4
    125     *t1 = 1
    126     t2 = this ptr+ 8
    127     *t2 = 1
    128     return

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

    129     t1 = this ptr+ 4
    130     t2 = *t1
    131     t3 = this ptr+ 8
    132     t4 = *t3
    133     t5 = t2 int* t4
    134     return t5

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

    135     t1 = this ptr+ 4
    136     t2 = *t1
    137     t3 = this ptr+ 8
    138     t4 = *t3
    139     t5 = t2 int+ t4
    140     t6 = t5 int<< 1
    141     return t6

============================================================================
 FUNCTION Square::Square(int)        (link name _ZN6SquareC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   side             param   int                             4       4
   t1               temp    class Square *                  4       8
   t2               temp    class Square *                  4      12

 Code: 7 instruction(s)

    142     param this                          (this)
    143     call Rect::Rect(), 1
    144     t1 = this ptr+ 4
    145     *t1 = side
    146     t2 = this ptr+ 8
    147     *t2 = side
    148     return

============================================================================
 FUNCTION Square::name()        (link name _ZN6Square4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    149     return 81

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

    150     *this = a
    151     t1 = this ptr+ 4
    152     *t1 = b
    153     return

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    154     *this = 0
    155     t1 = this ptr+ 4
    156     *t1 = 0
    157     return

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

    158     t1 = *this
    159     t2 = *o
    160     t3 = t1 int+ t2
    161     *this = t3
    162     t4 = this ptr+ 4
    163     t5 = *t4
    164     t6 = o ptr+ 4
    165     t7 = *t6
    166     t8 = t5 int+ t7
    167     *t4 = t8
    168     return this

============================================================================
 FUNCTION Point::operator-(const class Point &)        (link name _ZN5PointmiERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 10 temporaries, frame 52 bytes

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

 Code: 14 instruction(s)

    169     t2 = &t1
    170     t3 = *this
    171     t4 = *o
    172     t5 = t3 int- t4
    173     t6 = this ptr+ 4
    174     t7 = *t6
    175     t8 = o ptr+ 4
    176     t9 = *t8
    177     t10 = t7 int- t9
    178     param t2                            (this)
    179     param t5
    180     param t10
    181     call Point::Point(int, int), 3
    182     return t1

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

    183       t2 = *this
    184       t4 = t2 int* t2
    185       t5 = this ptr+ 4
    186       t6 = *t5
    187       t9 = t6 int* t6
    188       t10 = t4 int+ t9
    189       t11 = *o
    190       t13 = t11 int* t11
    191       t14 = o ptr+ 4
    192       t15 = *t14
    193       t18 = t15 int* t15
    194       t19 = t13 int+ t18
    195       if t10 int< t19 goto L1
    196       t1 = 0
    197       goto L2
    198  L1:  t1 = 1
    199  L2:  if t1 int!= 0 goto L3
    200       t20 = 0
    201       goto L4
    202  L3:  t20 = 1
    203  L4:  return t20

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

    204       if i int!= 0 goto L5
    205       t1 = this
    206       goto L6
    207  L5:  t1 = this ptr+ 4
    208  L6:  return t1

============================================================================
 FUNCTION Segment::Segment(int, int, int, int)        (link name _ZN7SegmentC1Eiiii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 5 temporaries, frame 52 bytes

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
   (1 temporary no longer used after optimization not shown)

 Code: 18 instruction(s)

    209     param this                          (this)
    210     call Point::Point(), 1
    211     t1 = this ptr+ 8
    212     param t1                            (this)
    213     call Point::Point(), 1
    214     t3 = &t2
    215     param t3                            (this)
    216     param a
    217     param b
    218     call Point::Point(int, int), 3
    219     *this = t2
    220     t5 = &t4
    221     param t5                            (this)
    222     param c
    223     param d
    224     call Point::Point(int, int), 3
    225     *t1 = t4
    226     return

============================================================================
 FUNCTION Segment::length2()        (link name _ZN7Segment7length2Ev)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t2               temp    class Point                     8      16
   t5               temp    int                             4      32
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t10              temp    int                             4      52
   t11              temp    int                             4      56
   (4 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    227     t1 = this ptr+ 8
    228     param t1                            (this)
    229     param this
    230     t2 = call Point::operator-(const class Point &), 2
    231     d = t2
    232     t5 = d[0]
    233     t7 = t5 int* t5
    234     t8 = d[4]
    235     t10 = t8 int* t8
    236     t11 = t7 int+ t10
    237     return t11

============================================================================
 FUNCTION total(class Rect &)        (link name _Z5totalR4Rect)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   class Rect &                    4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 5 instruction(s)

    238     param r                             (this)
    239     t1 = call Rect::area(), 1
    240     t2 = *r
    241     t3 = t1 int+ t2
    242     return t3

============================================================================
 FUNCTION through(class Shape *)        (link name _Z7throughP5Shape)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   class Shape *                   4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 6 instruction(s)

    243     param s                             (this)
    244     t1 = call Shape::area(), 1
    245     param s                             (this)
    246     t2 = call Shape::name(), 1
    247     t3 = t1 int+ t2
    248     return t3

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

    249     t1 = r ptr+ 4
    250     t2 = *t1
    251     t3 = t2 int+ by
    252     *t1 = t3
    253     t5 = r ptr+ 8
    254     t6 = *t5
    255     t7 = t6 int+ by
    256     *t5 = t7
    257     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 42 temporaries, frame 440 bytes

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
   t4               temp    int                             4     124
   t6               temp    int                             4     132
   t8               temp    int                             4     140
   t11              temp    int                             4     152
   t13              temp    int                             4     160
   t15              temp    int                             4     168
   t16              temp    int                             4     172
   t19              temp    class Rect *                    4     184
   t21              temp    int                             4     192
   t22              temp    int                             4     196
   t23              temp    class Rect (*)[2]               4     200
   t24              temp    class Rect (*)[2]               4     204
   t26              temp    int                             4     212
   t29              temp    int                             4     224
   t30              temp    int                             4     228
   t31              temp    int                             4     232
   t35              temp    class Point *                   4     248
   t36              temp    class Point *                   4     252
   t42              temp    class Point &                   4     276
   t46              temp    int &                           4     292
   t48              temp    int &                           4     300
   t49              temp    int                             4     304
   t50              temp    int                             4     308
   t53              temp    class Point                     8     320
   t56              temp    int                             4     336
   t57              temp    int                             4     340
   t58              temp    int                             4     344
   t59              temp    int                             4     348
   t62              temp    bool                            1     360
   t63              temp    int                             4     364
   t66              temp    bool                            1     376
   t67              temp    int                             4     380
   t68              temp    class Segment *                 4     384
   t70              temp    int                             4     392
   t71              temp    int                             4     396
   t72              temp    class Rect *                    4     400
   t75              temp    int                             4     412
   t76              temp    int                             4     416
   t77              temp    int                             4     420
   t79              temp    int                             4     428
   (39 temporaries no longer used after optimization not shown)

 Code: 162 instruction(s)

    258     t1 = &r
    259     param t1                            (this)
    260     param 3
    261     param 4
    262     call Rect::Rect(int, int), 3
    263     t2 = &q
    264     param t2                            (this)
    265     param 5
    266     call Square::Square(int), 2
    267     param t1                            (this)
    268     t4 = call Rect::area(), 1
    269     param t2                            (this)
    270     t6 = call Rect::area(), 1
    271     param t2                            (this)
    272     t8 = call Rect::perimeter(), 1
    273     param "%d %d %d %d\n"
    274     param t4
    275     param t6
    276     param t8
    277     param Shape::live
    278     call printf, 5
    279     param t1
    280     t11 = call total(class Rect &), 1
    281     param t2
    282     t13 = call through(class Shape *), 1
    283     param t2                            (this)
    284     t15 = call Square::name(), 1
    285     param t2                            (this)
    286     t16 = call Shape::name(), 1
    287     param "%d %d %c %c\n"
    288     param t11
    289     param t13
    290     param t15
    291     param t16
    292     call printf, 5
    293     param t2
    294     param 1
    295     call grow(class Rect *, int), 2
    296     t19 = t2 ptr+ 4
    297     *t19 = 10
    298     param t2                            (this)
    299     t21 = call Rect::area(), 1
    300     param t2                            (this)
    301     t22 = call Rect::perimeter(), 1
    302     param "%d %d\n"
    303     param t21
    304     param t22
    305     call printf, 3
    306     t23 = &pair
    307     param t23                           (this)
    308     call Rect::Rect(), 1
    309     t24 = t23 ptr+ 12
    310     param t24                           (this)
    311     call Rect::Rect(), 1
    312     pair[16] = 6
    313     param t23                           (this)
    314     t26 = call Rect::area(), 1
    315     param t24                           (this)
    316     t29 = call Rect::area(), 1
    317     t30 = t26 int+ t29
    318     t31 = pair[12]
    319     param "%d %d %d\n"
    320     param t30
    321     param t31
    322     param Shape::live
    323     call printf, 4
    324     param t24                           (this)
    325     call Shape::~Shape(), 1
    326     param t23                           (this)
    327     call Shape::~Shape(), 1
    328     param "%d\n"
    329     param Shape::live
    330     call printf, 2
    331     t35 = &a
    332     param t35                           (this)
    333     param 3
    334     param 4
    335     call Point::Point(int, int), 3
    336     t36 = &b
    337     param t36                           (this)
    338     param 1
    339     param 1
    340     call Point::Point(int, int), 3
    341     param t35                           (this)
    342     param t36
    343     call Point::operator+=(const class Point &), 2
    344     param t35                           (this)
    345     param t36
    346     t42 = call Point::operator+=(const class Point &), 2
    347     param t42                           (this)
    348     param t36
    349     call Point::operator+=(const class Point &), 2
    350     param t35                           (this)
    351     param 0
    352     t46 = call Point::operator[](int), 2
    353     param t35                           (this)
    354     param 1
    355     t48 = call Point::operator[](int), 2
    356     t49 = *t48
    357     t50 = t49 int<< 1
    358     *t46 = t50
    359     param t35                           (this)
    360     param t36
    361     t53 = call Point::operator-(const class Point &), 2
    362     c = t53
    363     t56 = a[0]
    364     t57 = a[4]
    365     t58 = c[0]
    366     t59 = c[4]
    367     param t36                           (this)
    368     param t35
    369     t62 = call Point::operator<(const class Point &), 2
    370     t63 = booltoint t62
    371     param t35                           (this)
    372     param t36
    373     t66 = call Point::operator<(const class Point &), 2
    374     t67 = booltoint t66
    375     param "%d %d %d %d %d %d\n"
    376     param t56
    377     param t57
    378     param t58
    379     param t59
    380     param t63
    381     param t67
    382     call printf, 7
    383     t68 = &s
    384     param t68                           (this)
    385     param 1
    386     param 2
    387     param 4
    388     param 6
    389     call Segment::Segment(int, int, int, int), 5
    390     param t68                           (this)
    391     t70 = call Segment::length2(), 1
    392     t71 = s[12]
    393     param "%d %d\n"
    394     param t70
    395     param t71
    396     call printf, 3
    397     t72 = &last
    398     param t72                           (this)
    399     param 2
    400     param 9
    401     call Rect::Rect(int, int), 3
    402     param t72                           (this)
    403     t75 = call Rect::area(), 1
    404     param t72                           (this)
    405     t76 = call Shape::area(), 1
    406     t77 = *t72
    407     param "%d %d %d\n"
    408     param t75
    409     param t76
    410     param t77
    411     call printf, 4
    412     param t72                           (this)
    413     call Shape::~Shape(), 1
    414     t79 = Shape::live
    415     param t2                            (this)
    416     call Shape::~Shape(), 1
    417     param t1                            (this)
    418     call Shape::~Shape(), 1
    419     return t79


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
