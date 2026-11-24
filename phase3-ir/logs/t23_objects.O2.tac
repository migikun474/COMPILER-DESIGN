============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 356 -> 300 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          356 -> 300   (15% fewer)

   constants folded                        0
   algebraic simplifications               2
   common subexpressions                  45
   copies / constants forwarded           50
   temporaries merged away                 5
   dead instructions removed              49
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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    class Rect *                    4       4
   t2               temp    class Rect *                    4       8

 Code: 7 instruction(s)

    109     param this                          (this)
    110     call Shape::Shape(), 1
    111     t1 = this ptr+ 4
    112     *t1 = 1
    113     t2 = this ptr+ 8
    114     *t2 = 1
    115     return

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

    116     t1 = this ptr+ 4
    117     *t1 = a
    118     t2 = this ptr+ 8
    119     *t2 = b
    120     return

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

    121     t1 = this ptr+ 4
    122     t2 = *t1
    123     t3 = this ptr+ 8
    124     t4 = *t3
    125     t5 = t2 int* t4
    126     return t5

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

    127     t1 = this ptr+ 4
    128     t2 = *t1
    129     t3 = this ptr+ 8
    130     t4 = *t3
    131     t5 = t2 int+ t4
    132     t6 = t5 int<< 1
    133     return t6

============================================================================
 FUNCTION Square::side(int)        (link name _ZN6Square4sideEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   s                param   int                             4       4

 Code: 5 instruction(s)

    134     param this                          (this)
    135     param s
    136     param s
    137     call Rect::set(int, int), 3
    138     return

============================================================================
 FUNCTION Square::name()        (link name _ZN6Square4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    139     return 81

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    140     *this = 0
    141     t1 = this ptr+ 4
    142     *t1 = 0
    143     return

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

    144     t1 = *this
    145     t2 = *o
    146     t3 = t1 int+ t2
    147     *this = t3
    148     t4 = this ptr+ 4
    149     t5 = *t4
    150     t6 = o ptr+ 4
    151     t7 = *t6
    152     t8 = t5 int+ t7
    153     *t4 = t8
    154     return this

============================================================================
 FUNCTION Point::operator-(const class Point &)        (link name _ZN5PointmiERKS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 9 temporaries, frame 52 bytes

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

 Code: 14 instruction(s)

    155     t1 = &r
    156     param t1                            (this)
    157     call Point::Point(), 1
    158     t2 = *this
    159     t3 = *o
    160     t4 = t2 int- t3
    161     r[0] = t4
    162     t5 = this ptr+ 4
    163     t6 = *t5
    164     t7 = o ptr+ 4
    165     t8 = *t7
    166     t9 = t6 int- t8
    167     r[4] = t9
    168     return r

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

    169       t2 = *this
    170       t4 = t2 int* t2
    171       t5 = this ptr+ 4
    172       t6 = *t5
    173       t9 = t6 int* t6
    174       t10 = t4 int+ t9
    175       t11 = *o
    176       t13 = t11 int* t11
    177       t14 = o ptr+ 4
    178       t15 = *t14
    179       t18 = t15 int* t15
    180       t19 = t13 int+ t18
    181       if t10 int< t19 goto L1
    182       t1 = 0
    183       goto L2
    184  L1:  t1 = 1
    185  L2:  if t1 int!= 0 goto L3
    186       t20 = 0
    187       goto L4
    188  L3:  t20 = 1
    189  L4:  return t20

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

    190       if i int!= 0 goto L5
    191       t1 = this
    192       goto L6
    193  L5:  t1 = this ptr+ 4
    194  L6:  return t1

============================================================================
 FUNCTION at(int, int)        (link name _Z2atii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   p                local   class Point                     8       8
   t1               temp    class Point *                   4      16

 Code: 6 instruction(s)

    195     t1 = &p
    196     param t1                            (this)
    197     call Point::Point(), 1
    198     p[0] = a
    199     p[4] = b
    200     return p

============================================================================
 FUNCTION Segment::set(int, int, int, int)        (link name _ZN7Segment3setEiiii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 3 temporaries, frame 40 bytes

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

 Code: 10 instruction(s)

    201     param a
    202     param b
    203     t1 = call at(int, int), 2
    204     *this = t1
    205     param c
    206     param d
    207     t2 = call at(int, int), 2
    208     t3 = this ptr+ 8
    209     *t3 = t2
    210     return

============================================================================
 FUNCTION Segment::length2()        (link name _ZN7Segment7length2Ev)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t4               temp    int                             4      28
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t9               temp    int                             4      48
   t10              temp    int                             4      52
   (4 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    211     t1 = this ptr+ 8
    212     param t1                            (this)
    213     param this
    214     d = call Point::operator-(const class Point &), 2
    215     t4 = d[0]
    216     t6 = t4 int* t4
    217     t7 = d[4]
    218     t9 = t7 int* t7
    219     t10 = t6 int+ t9
    220     return t10

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

    221     param r                             (this)
    222     t1 = call Rect::area(), 1
    223     t2 = *r
    224     t3 = t1 int+ t2
    225     return t3

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

    226     param s                             (this)
    227     t1 = call Shape::area(), 1
    228     param s                             (this)
    229     t2 = call Shape::name(), 1
    230     t3 = t1 int+ t2
    231     return t3

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

    232     t1 = r ptr+ 4
    233     t2 = *t1
    234     t3 = t2 int+ by
    235     *t1 = t3
    236     t5 = r ptr+ 8
    237     t6 = *t5
    238     t7 = t6 int+ by
    239     *t5 = t7
    240     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 41 temporaries, frame 444 bytes

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
   t6               temp    int                             4     132
   t8               temp    int                             4     140
   t10              temp    int                             4     148
   t13              temp    int                             4     160
   t15              temp    int                             4     168
   t17              temp    int                             4     176
   t18              temp    int                             4     180
   t21              temp    class Rect *                    4     192
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t25              temp    class Rect (*)[2]               4     208
   t26              temp    class Rect (*)[2]               4     212
   t28              temp    int                             4     220
   t31              temp    int                             4     232
   t32              temp    int                             4     236
   t33              temp    int                             4     240
   t35              temp    class Point *                   4     252
   t37              temp    class Point *                   4     264
   t43              temp    class Point &                   4     288
   t47              temp    int &                           4     304
   t49              temp    int &                           4     312
   t50              temp    int                             4     316
   t51              temp    int                             4     320
   t56              temp    int                             4     344
   t57              temp    int                             4     348
   t58              temp    int                             4     352
   t59              temp    int                             4     356
   t62              temp    bool                            1     368
   t63              temp    int                             4     372
   t66              temp    bool                            1     384
   t67              temp    int                             4     388
   t68              temp    class Segment *                 4     392
   t69              temp    class Segment *                 4     396
   t72              temp    int                             4     408
   t73              temp    int                             4     412
   t74              temp    class Rect *                    4     416
   t78              temp    int                             4     432
   t79              temp    int                             4     436
   t80              temp    int                             4     440
   (39 temporaries no longer used after optimization not shown)

 Code: 159 instruction(s)

    241     t1 = &r
    242     param t1                            (this)
    243     call Rect::Rect(), 1
    244     param t1                            (this)
    245     param 3
    246     param 4
    247     call Rect::set(int, int), 3
    248     t3 = &q
    249     param t3                            (this)
    250     call Rect::Rect(), 1
    251     param t3                            (this)
    252     param 5
    253     call Square::side(int), 2
    254     param t1                            (this)
    255     t6 = call Rect::area(), 1
    256     param t3                            (this)
    257     t8 = call Rect::area(), 1
    258     param t3                            (this)
    259     t10 = call Rect::perimeter(), 1
    260     param "%d %d %d %d\n"
    261     param t6
    262     param t8
    263     param t10
    264     param Shape::live
    265     call printf, 5
    266     param t1
    267     t13 = call total(class Rect &), 1
    268     param t3
    269     t15 = call through(class Shape *), 1
    270     param t3                            (this)
    271     t17 = call Square::name(), 1
    272     param t3                            (this)
    273     t18 = call Shape::name(), 1
    274     param "%d %d %c %c\n"
    275     param t13
    276     param t15
    277     param t17
    278     param t18
    279     call printf, 5
    280     param t3
    281     param 1
    282     call grow(class Rect *, int), 2
    283     t21 = t3 ptr+ 4
    284     *t21 = 10
    285     param t3                            (this)
    286     t23 = call Rect::area(), 1
    287     param t3                            (this)
    288     t24 = call Rect::perimeter(), 1
    289     param "%d %d\n"
    290     param t23
    291     param t24
    292     call printf, 3
    293     t25 = &pair
    294     param t25                           (this)
    295     call Rect::Rect(), 1
    296     t26 = t25 ptr+ 12
    297     param t26                           (this)
    298     call Rect::Rect(), 1
    299     pair[16] = 6
    300     param t25                           (this)
    301     t28 = call Rect::area(), 1
    302     param t26                           (this)
    303     t31 = call Rect::area(), 1
    304     t32 = t28 int+ t31
    305     t33 = pair[12]
    306     param "%d %d %d\n"
    307     param t32
    308     param t33
    309     param Shape::live
    310     call printf, 4
    311     param "%d\n"
    312     param Shape::live
    313     call printf, 2
    314     param 3
    315     param 4
    316     a = call at(int, int), 2
    317     t35 = &a
    318     param 1
    319     param 1
    320     b = call at(int, int), 2
    321     t37 = &b
    322     param t35                           (this)
    323     param t37
    324     call Point::operator+=(const class Point &), 2
    325     param t35                           (this)
    326     param t37
    327     t43 = call Point::operator+=(const class Point &), 2
    328     param t43                           (this)
    329     param t37
    330     call Point::operator+=(const class Point &), 2
    331     param t35                           (this)
    332     param 0
    333     t47 = call Point::operator[](int), 2
    334     param t35                           (this)
    335     param 1
    336     t49 = call Point::operator[](int), 2
    337     t50 = *t49
    338     t51 = t50 int<< 1
    339     *t47 = t51
    340     param t35                           (this)
    341     param t37
    342     c = call Point::operator-(const class Point &), 2
    343     t56 = a[0]
    344     t57 = a[4]
    345     t58 = c[0]
    346     t59 = c[4]
    347     param t37                           (this)
    348     param t35
    349     t62 = call Point::operator<(const class Point &), 2
    350     t63 = booltoint t62
    351     param t35                           (this)
    352     param t37
    353     t66 = call Point::operator<(const class Point &), 2
    354     t67 = booltoint t66
    355     param "%d %d %d %d %d %d\n"
    356     param t56
    357     param t57
    358     param t58
    359     param t59
    360     param t63
    361     param t67
    362     call printf, 7
    363     t68 = &s
    364     param t68                           (this)
    365     call Point::Point(), 1
    366     t69 = t68 ptr+ 8
    367     param t69                           (this)
    368     call Point::Point(), 1
    369     param t68                           (this)
    370     param 1
    371     param 2
    372     param 4
    373     param 6
    374     call Segment::set(int, int, int, int), 5
    375     param t68                           (this)
    376     t72 = call Segment::length2(), 1
    377     t73 = s[12]
    378     param "%d %d\n"
    379     param t72
    380     param t73
    381     call printf, 3
    382     t74 = &last
    383     param t74                           (this)
    384     call Rect::Rect(), 1
    385     param t74                           (this)
    386     param 2
    387     param 9
    388     call Rect::set(int, int), 3
    389     param t74                           (this)
    390     t78 = call Rect::area(), 1
    391     param t74                           (this)
    392     t79 = call Shape::area(), 1
    393     t80 = *t74
    394     param "%d %d %d\n"
    395     param t78
    396     param t79
    397     param t80
    398     call printf, 4
    399     return Shape::live


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
