============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : no optimization
   Result        : Three address code generated: 21 function(s), 356 instruction(s)

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
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    108     return 0

============================================================================
 FUNCTION Shape::name()        (link name _ZN5Shape4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    109     return 83

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

    110     param this                          (this)
    111     call Shape::Shape(), 1
    112     t1 = this ptr+ 4
    113     *t1 = 1
    114     t2 = this ptr+ 8
    115     *t2 = 1
    116     return

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

    117     t1 = this ptr+ 4
    118     *t1 = a
    119     t2 = this ptr+ 8
    120     *t2 = b
    121     return

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

    122     t1 = this ptr+ 4
    123     t2 = *t1
    124     t3 = this ptr+ 8
    125     t4 = *t3
    126     t5 = t2 int* t4
    127     return t5

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

    128     t1 = this ptr+ 4
    129     t2 = *t1
    130     t3 = this ptr+ 8
    131     t4 = *t3
    132     t5 = t2 int+ t4
    133     t6 = 2 int* t5
    134     return t6

============================================================================
 FUNCTION Square::side(int)        (link name _ZN6Square4sideEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   s                param   int                             4       4

 Code: 5 instruction(s)

    135     param this                          (this)
    136     param s
    137     param s
    138     call Rect::set(int, int), 3
    139     return

============================================================================
 FUNCTION Square::name()        (link name _ZN6Square4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    140     return 81

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    141     *this = 0
    142     t1 = this ptr+ 4
    143     *t1 = 0
    144     return

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

    145     t1 = *this
    146     t2 = *o
    147     t3 = t1 int+ t2
    148     *this = t3
    149     t4 = this ptr+ 4
    150     t5 = *t4
    151     t6 = o ptr+ 4
    152     t7 = *t6
    153     t8 = t5 int+ t7
    154     t9 = this ptr+ 4
    155     *t9 = t8
    156     return this

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

    157     t1 = &r
    158     param t1                            (this)
    159     call Point::Point(), 1
    160     t2 = *this
    161     t3 = *o
    162     t4 = t2 int- t3
    163     r[0] = t4
    164     t5 = this ptr+ 4
    165     t6 = *t5
    166     t7 = o ptr+ 4
    167     t8 = *t7
    168     t9 = t6 int- t8
    169     r[4] = t9
    170     return r

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

    171       t2 = *this
    172       t3 = *this
    173       t4 = t2 int* t3
    174       t5 = this ptr+ 4
    175       t6 = *t5
    176       t7 = this ptr+ 4
    177       t8 = *t7
    178       t9 = t6 int* t8
    179       t10 = t4 int+ t9
    180       t11 = *o
    181       t12 = *o
    182       t13 = t11 int* t12
    183       t14 = o ptr+ 4
    184       t15 = *t14
    185       t16 = o ptr+ 4
    186       t17 = *t16
    187       t18 = t15 int* t17
    188       t19 = t13 int+ t18
    189       if t10 int< t19 goto L1
    190       t1 = 0
    191       goto L2
    192  L1:  t1 = 1
    193  L2:  if t1 int!= 0 goto L3
    194       t20 = 0
    195       goto L4
    196  L3:  t20 = 1
    197  L4:  return t20

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

    198       if i int== 0 goto L5
    199       goto L6
    200  L5:  t1 = this
    201       goto L7
    202  L6:  t2 = this ptr+ 4
    203       t1 = t2
    204  L7:  return t1

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

    205     t1 = &p
    206     param t1                            (this)
    207     call Point::Point(), 1
    208     p[0] = a
    209     p[4] = b
    210     return p

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

    211     param a
    212     param b
    213     t1 = call at(int, int), 2
    214     *this = t1
    215     param c
    216     param d
    217     t2 = call at(int, int), 2
    218     t3 = this ptr+ 8
    219     *t3 = t2
    220     return

============================================================================
 FUNCTION Segment::length2()        (link name _ZN7Segment7length2Ev)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 10 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t2               temp    class Point                     8      16
   t3               temp    class Point *                   4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52

 Code: 14 instruction(s)

    221     t1 = this ptr+ 8
    222     param t1                            (this)
    223     param this
    224     t2 = call Point::operator-(const class Point &), 2
    225     d = t2
    226     t3 = &d
    227     t4 = d[0]
    228     t5 = d[0]
    229     t6 = t4 int* t5
    230     t7 = d[4]
    231     t8 = d[4]
    232     t9 = t7 int* t8
    233     t10 = t6 int+ t9
    234     return t10

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

    235     param r                             (this)
    236     t1 = call Rect::area(), 1
    237     t2 = *r
    238     t3 = t1 int+ t2
    239     return t3

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

    240     param s                             (this)
    241     t1 = call Shape::area(), 1
    242     param s                             (this)
    243     t2 = call Shape::name(), 1
    244     t3 = t1 int+ t2
    245     return t3

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

    246     t1 = r ptr+ 4
    247     t2 = *t1
    248     t3 = t2 int+ by
    249     t4 = r ptr+ 4
    250     *t4 = t3
    251     t5 = r ptr+ 8
    252     t6 = *t5
    253     t7 = t6 int+ by
    254     t8 = r ptr+ 8
    255     *t8 = t7
    256     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 80 temporaries, frame 444 bytes

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
   t2               temp    class Rect *                    4     116
   t3               temp    class Square *                  4     120
   t4               temp    class Square *                  4     124
   t5               temp    class Rect *                    4     128
   t6               temp    int                             4     132
   t7               temp    class Square *                  4     136
   t8               temp    int                             4     140
   t9               temp    class Square *                  4     144
   t10              temp    int                             4     148
   t11              temp    class Square *                  4     152
   t12              temp    class Rect *                    4     156
   t13              temp    int                             4     160
   t14              temp    class Square *                  4     164
   t15              temp    int                             4     168
   t16              temp    class Square *                  4     172
   t17              temp    int                             4     176
   t18              temp    int                             4     180
   t19              temp    class Square *                  4     184
   t20              temp    class Square *                  4     188
   t21              temp    class Rect *                    4     192
   t22              temp    class Square *                  4     196
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t25              temp    class Rect (*)[2]               4     208
   t26              temp    class Rect (*)[2]               4     212
   t27              temp    class Rect *                    4     216
   t28              temp    int                             4     220
   t29              temp    class Rect *                    4     224
   t30              temp    class Rect *                    4     228
   t31              temp    int                             4     232
   t32              temp    int                             4     236
   t33              temp    int                             4     240
   t34              temp    class Point                     8     244
   t35              temp    class Point *                   4     252
   t36              temp    class Point                     8     256
   t37              temp    class Point *                   4     264
   t38              temp    class Point *                   4     268
   t39              temp    class Point *                   4     272
   t40              temp    class Point &                   4     276
   t41              temp    class Point *                   4     280
   t42              temp    class Point *                   4     284
   t43              temp    class Point &                   4     288
   t44              temp    class Point *                   4     292
   t45              temp    class Point &                   4     296
   t46              temp    class Point *                   4     300
   t47              temp    int &                           4     304
   t48              temp    class Point *                   4     308
   t49              temp    int &                           4     312
   t50              temp    int                             4     316
   t51              temp    int                             4     320
   t52              temp    class Point *                   4     324
   t53              temp    class Point *                   4     328
   t54              temp    class Point                     8     332
   t55              temp    class Point *                   4     340
   t56              temp    int                             4     344
   t57              temp    int                             4     348
   t58              temp    int                             4     352
   t59              temp    int                             4     356
   t60              temp    class Point *                   4     360
   t61              temp    class Point *                   4     364
   t62              temp    bool                            1     368
   t63              temp    int                             4     372
   t64              temp    class Point *                   4     376
   t65              temp    class Point *                   4     380
   t66              temp    bool                            1     384
   t67              temp    int                             4     388
   t68              temp    class Segment *                 4     392
   t69              temp    class Segment *                 4     396
   t70              temp    class Segment *                 4     400
   t71              temp    class Segment *                 4     404
   t72              temp    int                             4     408
   t73              temp    int                             4     412
   t74              temp    class Rect *                    4     416
   t75              temp    class Rect *                    4     420
   t76              temp    class Rect *                    4     424
   t77              temp    class Rect *                    4     428
   t78              temp    int                             4     432
   t79              temp    int                             4     436
   t80              temp    int                             4     440

 Code: 199 instruction(s)

    257     t1 = &r
    258     param t1                            (this)
    259     call Rect::Rect(), 1
    260     t2 = &r
    261     param t2                            (this)
    262     param 3
    263     param 4
    264     call Rect::set(int, int), 3
    265     t3 = &q
    266     param t3                            (this)
    267     call Rect::Rect(), 1
    268     t4 = &q
    269     param t4                            (this)
    270     param 5
    271     call Square::side(int), 2
    272     t5 = &r
    273     param t5                            (this)
    274     t6 = call Rect::area(), 1
    275     t7 = &q
    276     param t7                            (this)
    277     t8 = call Rect::area(), 1
    278     t9 = &q
    279     param t9                            (this)
    280     t10 = call Rect::perimeter(), 1
    281     param "%d %d %d %d\n"
    282     param t6
    283     param t8
    284     param t10
    285     param Shape::live
    286     call printf, 5
    287     t11 = &q
    288     asShape = t11
    289     t12 = &r
    290     param t12
    291     t13 = call total(class Rect &), 1
    292     t14 = &q
    293     param t14
    294     t15 = call through(class Shape *), 1
    295     t16 = &q
    296     param t16                           (this)
    297     t17 = call Square::name(), 1
    298     param asShape                       (this)
    299     t18 = call Shape::name(), 1
    300     param "%d %d %c %c\n"
    301     param t13
    302     param t15
    303     param t17
    304     param t18
    305     call printf, 5
    306     t19 = &q
    307     param t19
    308     param 1
    309     call grow(class Rect *, int), 2
    310     t20 = &q
    311     alias = t20
    312     t21 = alias ptr+ 4
    313     *t21 = 10
    314     t22 = &q
    315     param t22                           (this)
    316     t23 = call Rect::area(), 1
    317     param alias                         (this)
    318     t24 = call Rect::perimeter(), 1
    319     param "%d %d\n"
    320     param t23
    321     param t24
    322     call printf, 3
    323     t25 = &pair
    324     param t25                           (this)
    325     call Rect::Rect(), 1
    326     t26 = t25 ptr+ 12
    327     param t26                           (this)
    328     call Rect::Rect(), 1
    329     pair[16] = 6
    330     t27 = &pair
    331     param t27                           (this)
    332     t28 = call Rect::area(), 1
    333     t29 = &pair
    334     t30 = t29 ptr+ 12
    335     param t30                           (this)
    336     t31 = call Rect::area(), 1
    337     t32 = t28 int+ t31
    338     t33 = pair[12]
    339     param "%d %d %d\n"
    340     param t32
    341     param t33
    342     param Shape::live
    343     call printf, 4
    344     param "%d\n"
    345     param Shape::live
    346     call printf, 2
    347     param 3
    348     param 4
    349     t34 = call at(int, int), 2
    350     a = t34
    351     t35 = &a
    352     param 1
    353     param 1
    354     t36 = call at(int, int), 2
    355     b = t36
    356     t37 = &b
    357     t38 = &a
    358     t39 = &b
    359     param t38                           (this)
    360     param t39
    361     t40 = call Point::operator+=(const class Point &), 2
    362     t41 = &a
    363     t42 = &b
    364     param t41                           (this)
    365     param t42
    366     t43 = call Point::operator+=(const class Point &), 2
    367     t44 = &b
    368     param t43                           (this)
    369     param t44
    370     t45 = call Point::operator+=(const class Point &), 2
    371     t46 = &a
    372     param t46                           (this)
    373     param 0
    374     t47 = call Point::operator[](int), 2
    375     t48 = &a
    376     param t48                           (this)
    377     param 1
    378     t49 = call Point::operator[](int), 2
    379     t50 = *t49
    380     t51 = t50 int* 2
    381     *t47 = t51
    382     t52 = &a
    383     t53 = &b
    384     param t52                           (this)
    385     param t53
    386     t54 = call Point::operator-(const class Point &), 2
    387     c = t54
    388     t55 = &c
    389     t56 = a[0]
    390     t57 = a[4]
    391     t58 = c[0]
    392     t59 = c[4]
    393     t60 = &b
    394     t61 = &a
    395     param t60                           (this)
    396     param t61
    397     t62 = call Point::operator<(const class Point &), 2
    398     t63 = booltoint t62
    399     t64 = &a
    400     t65 = &b
    401     param t64                           (this)
    402     param t65
    403     t66 = call Point::operator<(const class Point &), 2
    404     t67 = booltoint t66
    405     param "%d %d %d %d %d %d\n"
    406     param t56
    407     param t57
    408     param t58
    409     param t59
    410     param t63
    411     param t67
    412     call printf, 7
    413     t68 = &s
    414     param t68                           (this)
    415     call Point::Point(), 1
    416     t69 = t68 ptr+ 8
    417     param t69                           (this)
    418     call Point::Point(), 1
    419     t70 = &s
    420     param t70                           (this)
    421     param 1
    422     param 2
    423     param 4
    424     param 6
    425     call Segment::set(int, int, int, int), 5
    426     t71 = &s
    427     param t71                           (this)
    428     t72 = call Segment::length2(), 1
    429     t73 = s[12]
    430     param "%d %d\n"
    431     param t72
    432     param t73
    433     call printf, 3
    434     t74 = &last
    435     param t74                           (this)
    436     call Rect::Rect(), 1
    437     t75 = &last
    438     param t75                           (this)
    439     param 2
    440     param 9
    441     call Rect::set(int, int), 3
    442     t76 = &last
    443     base = t76
    444     t77 = &last
    445     param t77                           (this)
    446     t78 = call Rect::area(), 1
    447     param base                          (this)
    448     t79 = call Shape::area(), 1
    449     t80 = *base
    450     param "%d %d %d\n"
    451     param t78
    452     param t79
    453     param t80
    454     call printf, 4
    455     return Shape::live


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
