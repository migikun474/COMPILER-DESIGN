============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : no optimization
   Result        : Three address code generated: 22 function(s), 378 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 8 instruction(s)

    100     t1 = Shape::live int+ 1
    101     Shape::live = t1
    102     *this = t1
    103     t2 = *this
    104     param "Shape %d\n"
    105     param t2
    106     call printf, 2
    107     return

============================================================================
 FUNCTION Shape::~Shape()        (link name _ZN5ShapeD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 7 instruction(s)

    108     t1 = *this
    109     param "~Shape %d\n"
    110     param t1
    111     call printf, 2
    112     t2 = Shape::live int- 1
    113     Shape::live = t2
    114     return

============================================================================
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    115     return 0

============================================================================
 FUNCTION Shape::name()        (link name _ZN5Shape4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    116     return 83

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

    117     param this                          (this)
    118     call Shape::Shape(), 1
    119     t1 = this ptr+ 4
    120     *t1 = a
    121     t2 = this ptr+ 8
    122     *t2 = b
    123     return

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

    124     param this                          (this)
    125     call Shape::Shape(), 1
    126     t1 = this ptr+ 4
    127     *t1 = 1
    128     t2 = this ptr+ 8
    129     *t2 = 1
    130     return

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

    131     t1 = this ptr+ 4
    132     t2 = *t1
    133     t3 = this ptr+ 8
    134     t4 = *t3
    135     t5 = t2 int* t4
    136     return t5

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

    137     t1 = this ptr+ 4
    138     t2 = *t1
    139     t3 = this ptr+ 8
    140     t4 = *t3
    141     t5 = t2 int+ t4
    142     t6 = 2 int* t5
    143     return t6

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

    144     param this                          (this)
    145     call Rect::Rect(), 1
    146     t1 = this ptr+ 4
    147     *t1 = side
    148     t2 = this ptr+ 8
    149     *t2 = side
    150     return

============================================================================
 FUNCTION Square::name()        (link name _ZN6Square4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    151     return 81

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

    152     *this = a
    153     t1 = this ptr+ 4
    154     *t1 = b
    155     return

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    156     *this = 0
    157     t1 = this ptr+ 4
    158     *t1 = 0
    159     return

============================================================================
 FUNCTION Point::operator+=(const class Point &)        (link name _ZN5PointpLERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 9 temporaries, frame 44 bytes

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
   t9               temp    class Point *                   4      40

 Code: 12 instruction(s)

    160     t1 = *this
    161     t2 = *o
    162     t3 = t1 int+ t2
    163     *this = t3
    164     t4 = this ptr+ 4
    165     t5 = *t4
    166     t6 = o ptr+ 4
    167     t7 = *t6
    168     t8 = t5 int+ t7
    169     t9 = this ptr+ 4
    170     *t9 = t8
    171     return this

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

    172     t2 = &t1
    173     t3 = *this
    174     t4 = *o
    175     t5 = t3 int- t4
    176     t6 = this ptr+ 4
    177     t7 = *t6
    178     t8 = o ptr+ 4
    179     t9 = *t8
    180     t10 = t7 int- t9
    181     param t2                            (this)
    182     param t5
    183     param t10
    184     call Point::Point(int, int), 3
    185     return t1

============================================================================
 FUNCTION Point::operator<(const class Point &)        (link name _ZN5PointltERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 20 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    class Point *                   4      24
   t6               temp    int                             4      28
   t7               temp    class Point *                   4      32
   t8               temp    int                             4      36
   t9               temp    int                             4      40
   t10              temp    int                             4      44
   t11              temp    int                             4      48
   t12              temp    int                             4      52
   t13              temp    int                             4      56
   t14              temp    const class Point *             4      60
   t15              temp    int                             4      64
   t16              temp    const class Point *             4      68
   t17              temp    int                             4      72
   t18              temp    int                             4      76
   t19              temp    int                             4      80
   t20              temp    bool                            1      84

 Code: 27 instruction(s)

    186       t2 = *this
    187       t3 = *this
    188       t4 = t2 int* t3
    189       t5 = this ptr+ 4
    190       t6 = *t5
    191       t7 = this ptr+ 4
    192       t8 = *t7
    193       t9 = t6 int* t8
    194       t10 = t4 int+ t9
    195       t11 = *o
    196       t12 = *o
    197       t13 = t11 int* t12
    198       t14 = o ptr+ 4
    199       t15 = *t14
    200       t16 = o ptr+ 4
    201       t17 = *t16
    202       t18 = t15 int* t17
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

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   i                param   int                             4       4
   t1               temp    int *                           4       8
   t2               temp    class Point *                   4      12

 Code: 7 instruction(s)

    213       if i int== 0 goto L5
    214       goto L6
    215  L5:  t1 = this
    216       goto L7
    217  L6:  t2 = this ptr+ 4
    218       t1 = t2
    219  L7:  return t1

============================================================================
 FUNCTION Segment::Segment(int, int, int, int)        (link name _ZN7SegmentC1Eiiii)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 6 temporaries, frame 52 bytes

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
   t6               temp    class Segment *                 4      48

 Code: 19 instruction(s)

    220     param this                          (this)
    221     call Point::Point(), 1
    222     t1 = this ptr+ 8
    223     param t1                            (this)
    224     call Point::Point(), 1
    225     t3 = &t2
    226     param t3                            (this)
    227     param a
    228     param b
    229     call Point::Point(int, int), 3
    230     *this = t2
    231     t5 = &t4
    232     param t5                            (this)
    233     param c
    234     param d
    235     call Point::Point(int, int), 3
    236     t6 = this ptr+ 8
    237     *t6 = t4
    238     return

============================================================================
 FUNCTION Segment::length2()        (link name _ZN7Segment7length2Ev)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 11 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t2               temp    class Point                     8      16
   t3               temp    class Point *                   4      24
   t4               temp    class Point *                   4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52
   t11              temp    int                             4      56

 Code: 15 instruction(s)

    239     t1 = this ptr+ 8
    240     param t1                            (this)
    241     param this
    242     t2 = call Point::operator-(const class Point &), 2
    243     t3 = &t2
    244     d = t2
    245     t4 = &d
    246     t5 = d[0]
    247     t6 = d[0]
    248     t7 = t5 int* t6
    249     t8 = d[4]
    250     t9 = d[4]
    251     t10 = t8 int* t9
    252     t11 = t7 int+ t10
    253     return t11

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

    254     param r                             (this)
    255     t1 = call Rect::area(), 1
    256     t2 = *r
    257     t3 = t1 int+ t2
    258     return t3

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

    259     param s                             (this)
    260     t1 = call Shape::area(), 1
    261     param s                             (this)
    262     t2 = call Shape::name(), 1
    263     t3 = t1 int+ t2
    264     return t3

============================================================================
 FUNCTION grow(class Rect *, int)        (link name _Z4growP4Recti)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 8 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   class Rect *                    4       0
   by               param   int                             4       4
   t1               temp    class Rect *                    4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    class Rect *                    4      20
   t5               temp    class Rect *                    4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   t8               temp    class Rect *                    4      36

 Code: 11 instruction(s)

    265     t1 = r ptr+ 4
    266     t2 = *t1
    267     t3 = t2 int+ by
    268     t4 = r ptr+ 4
    269     *t4 = t3
    270     t5 = r ptr+ 8
    271     t6 = *t5
    272     t7 = t6 int+ by
    273     t8 = r ptr+ 8
    274     *t8 = t7
    275     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 81 temporaries, frame 440 bytes

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
   t3               temp    class Rect *                    4     120
   t4               temp    int                             4     124
   t5               temp    class Square *                  4     128
   t6               temp    int                             4     132
   t7               temp    class Square *                  4     136
   t8               temp    int                             4     140
   t9               temp    class Square *                  4     144
   t10              temp    class Rect *                    4     148
   t11              temp    int                             4     152
   t12              temp    class Square *                  4     156
   t13              temp    int                             4     160
   t14              temp    class Square *                  4     164
   t15              temp    int                             4     168
   t16              temp    int                             4     172
   t17              temp    class Square *                  4     176
   t18              temp    class Square *                  4     180
   t19              temp    class Rect *                    4     184
   t20              temp    class Square *                  4     188
   t21              temp    int                             4     192
   t22              temp    int                             4     196
   t23              temp    class Rect (*)[2]               4     200
   t24              temp    class Rect (*)[2]               4     204
   t25              temp    class Rect *                    4     208
   t26              temp    int                             4     212
   t27              temp    class Rect *                    4     216
   t28              temp    class Rect *                    4     220
   t29              temp    int                             4     224
   t30              temp    int                             4     228
   t31              temp    int                             4     232
   t32              temp    class Rect *                    4     236
   t33              temp    class Rect *                    4     240
   t34              temp    class Rect *                    4     244
   t35              temp    class Point *                   4     248
   t36              temp    class Point *                   4     252
   t37              temp    class Point *                   4     256
   t38              temp    class Point *                   4     260
   t39              temp    class Point &                   4     264
   t40              temp    class Point *                   4     268
   t41              temp    class Point *                   4     272
   t42              temp    class Point &                   4     276
   t43              temp    class Point *                   4     280
   t44              temp    class Point &                   4     284
   t45              temp    class Point *                   4     288
   t46              temp    int &                           4     292
   t47              temp    class Point *                   4     296
   t48              temp    int &                           4     300
   t49              temp    int                             4     304
   t50              temp    int                             4     308
   t51              temp    class Point *                   4     312
   t52              temp    class Point *                   4     316
   t53              temp    class Point                     8     320
   t54              temp    class Point *                   4     328
   t55              temp    class Point *                   4     332
   t56              temp    int                             4     336
   t57              temp    int                             4     340
   t58              temp    int                             4     344
   t59              temp    int                             4     348
   t60              temp    class Point *                   4     352
   t61              temp    class Point *                   4     356
   t62              temp    bool                            1     360
   t63              temp    int                             4     364
   t64              temp    class Point *                   4     368
   t65              temp    class Point *                   4     372
   t66              temp    bool                            1     376
   t67              temp    int                             4     380
   t68              temp    class Segment *                 4     384
   t69              temp    class Segment *                 4     388
   t70              temp    int                             4     392
   t71              temp    int                             4     396
   t72              temp    class Rect *                    4     400
   t73              temp    class Rect *                    4     404
   t74              temp    class Rect *                    4     408
   t75              temp    int                             4     412
   t76              temp    int                             4     416
   t77              temp    int                             4     420
   t78              temp    class Rect *                    4     424
   t79              temp    int                             4     428
   t80              temp    class Square *                  4     432
   t81              temp    class Rect *                    4     436

 Code: 202 instruction(s)

    276     t1 = &r
    277     param t1                            (this)
    278     param 3
    279     param 4
    280     call Rect::Rect(int, int), 3
    281     t2 = &q
    282     param t2                            (this)
    283     param 5
    284     call Square::Square(int), 2
    285     t3 = &r
    286     param t3                            (this)
    287     t4 = call Rect::area(), 1
    288     t5 = &q
    289     param t5                            (this)
    290     t6 = call Rect::area(), 1
    291     t7 = &q
    292     param t7                            (this)
    293     t8 = call Rect::perimeter(), 1
    294     param "%d %d %d %d\n"
    295     param t4
    296     param t6
    297     param t8
    298     param Shape::live
    299     call printf, 5
    300     t9 = &q
    301     asShape = t9
    302     t10 = &r
    303     param t10
    304     t11 = call total(class Rect &), 1
    305     t12 = &q
    306     param t12
    307     t13 = call through(class Shape *), 1
    308     t14 = &q
    309     param t14                           (this)
    310     t15 = call Square::name(), 1
    311     param asShape                       (this)
    312     t16 = call Shape::name(), 1
    313     param "%d %d %c %c\n"
    314     param t11
    315     param t13
    316     param t15
    317     param t16
    318     call printf, 5
    319     t17 = &q
    320     param t17
    321     param 1
    322     call grow(class Rect *, int), 2
    323     t18 = &q
    324     alias = t18
    325     t19 = alias ptr+ 4
    326     *t19 = 10
    327     t20 = &q
    328     param t20                           (this)
    329     t21 = call Rect::area(), 1
    330     param alias                         (this)
    331     t22 = call Rect::perimeter(), 1
    332     param "%d %d\n"
    333     param t21
    334     param t22
    335     call printf, 3
    336     t23 = &pair
    337     param t23                           (this)
    338     call Rect::Rect(), 1
    339     t24 = t23 ptr+ 12
    340     param t24                           (this)
    341     call Rect::Rect(), 1
    342     pair[16] = 6
    343     t25 = &pair
    344     param t25                           (this)
    345     t26 = call Rect::area(), 1
    346     t27 = &pair
    347     t28 = t27 ptr+ 12
    348     param t28                           (this)
    349     t29 = call Rect::area(), 1
    350     t30 = t26 int+ t29
    351     t31 = pair[12]
    352     param "%d %d %d\n"
    353     param t30
    354     param t31
    355     param Shape::live
    356     call printf, 4
    357     t32 = &pair
    358     t33 = t32 ptr+ 12
    359     param t33                           (this)
    360     call Shape::~Shape(), 1
    361     t34 = &pair
    362     param t34                           (this)
    363     call Shape::~Shape(), 1
    364     param "%d\n"
    365     param Shape::live
    366     call printf, 2
    367     t35 = &a
    368     param t35                           (this)
    369     param 3
    370     param 4
    371     call Point::Point(int, int), 3
    372     t36 = &b
    373     param t36                           (this)
    374     param 1
    375     param 1
    376     call Point::Point(int, int), 3
    377     t37 = &a
    378     t38 = &b
    379     param t37                           (this)
    380     param t38
    381     t39 = call Point::operator+=(const class Point &), 2
    382     t40 = &a
    383     t41 = &b
    384     param t40                           (this)
    385     param t41
    386     t42 = call Point::operator+=(const class Point &), 2
    387     t43 = &b
    388     param t42                           (this)
    389     param t43
    390     t44 = call Point::operator+=(const class Point &), 2
    391     t45 = &a
    392     param t45                           (this)
    393     param 0
    394     t46 = call Point::operator[](int), 2
    395     t47 = &a
    396     param t47                           (this)
    397     param 1
    398     t48 = call Point::operator[](int), 2
    399     t49 = *t48
    400     t50 = t49 int* 2
    401     *t46 = t50
    402     t51 = &a
    403     t52 = &b
    404     param t51                           (this)
    405     param t52
    406     t53 = call Point::operator-(const class Point &), 2
    407     t54 = &t53
    408     c = t53
    409     t55 = &c
    410     t56 = a[0]
    411     t57 = a[4]
    412     t58 = c[0]
    413     t59 = c[4]
    414     t60 = &b
    415     t61 = &a
    416     param t60                           (this)
    417     param t61
    418     t62 = call Point::operator<(const class Point &), 2
    419     t63 = booltoint t62
    420     t64 = &a
    421     t65 = &b
    422     param t64                           (this)
    423     param t65
    424     t66 = call Point::operator<(const class Point &), 2
    425     t67 = booltoint t66
    426     param "%d %d %d %d %d %d\n"
    427     param t56
    428     param t57
    429     param t58
    430     param t59
    431     param t63
    432     param t67
    433     call printf, 7
    434     t68 = &s
    435     param t68                           (this)
    436     param 1
    437     param 2
    438     param 4
    439     param 6
    440     call Segment::Segment(int, int, int, int), 5
    441     t69 = &s
    442     param t69                           (this)
    443     t70 = call Segment::length2(), 1
    444     t71 = s[12]
    445     param "%d %d\n"
    446     param t70
    447     param t71
    448     call printf, 3
    449     t72 = &last
    450     param t72                           (this)
    451     param 2
    452     param 9
    453     call Rect::Rect(int, int), 3
    454     t73 = &last
    455     base = t73
    456     t74 = &last
    457     param t74                           (this)
    458     t75 = call Rect::area(), 1
    459     param base                          (this)
    460     t76 = call Shape::area(), 1
    461     t77 = *base
    462     param "%d %d %d\n"
    463     param t75
    464     param t76
    465     param t77
    466     call printf, 4
    467     t78 = &last
    468     param t78                           (this)
    469     call Shape::~Shape(), 1
    470     t79 = Shape::live
    471     t80 = &q
    472     param t80                           (this)
    473     call Shape::~Shape(), 1
    474     t81 = &r
    475     param t81                           (this)
    476     call Shape::~Shape(), 1
    477     return t79


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
