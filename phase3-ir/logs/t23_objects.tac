============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : no optimization
   Result        : Three address code generated: 21 function(s), 352 instruction(s)

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

 Symbol table: 2 parameter(s)/local(s), 9 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Segment *                 4       0
   d                local   class Point                     8       4
   t1               temp    class Segment *                 4      12
   t2               temp    class Point                     8      16
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48

 Code: 13 instruction(s)

    221     t1 = this ptr+ 8
    222     param t1                            (this)
    223     param this
    224     t2 = call Point::operator-(const class Point &), 2
    225     d = t2
    226     t3 = d[0]
    227     t4 = d[0]
    228     t5 = t3 int* t4
    229     t6 = d[4]
    230     t7 = d[4]
    231     t8 = t6 int* t7
    232     t9 = t5 int+ t8
    233     return t9

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

    234     param r                             (this)
    235     t1 = call Rect::area(), 1
    236     t2 = *r
    237     t3 = t1 int+ t2
    238     return t3

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

    239     param s                             (this)
    240     t1 = call Shape::area(), 1
    241     param s                             (this)
    242     t2 = call Shape::name(), 1
    243     t3 = t1 int+ t2
    244     return t3

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

    245     t1 = r ptr+ 4
    246     t2 = *t1
    247     t3 = t2 int+ by
    248     t4 = r ptr+ 4
    249     *t4 = t3
    250     t5 = r ptr+ 8
    251     t6 = *t5
    252     t7 = t6 int+ by
    253     t8 = r ptr+ 8
    254     *t8 = t7
    255     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 77 temporaries, frame 432 bytes

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
   t35              temp    class Point                     8     252
   t36              temp    class Point *                   4     260
   t37              temp    class Point *                   4     264
   t38              temp    class Point &                   4     268
   t39              temp    class Point *                   4     272
   t40              temp    class Point *                   4     276
   t41              temp    class Point &                   4     280
   t42              temp    class Point *                   4     284
   t43              temp    class Point &                   4     288
   t44              temp    class Point *                   4     292
   t45              temp    int &                           4     296
   t46              temp    class Point *                   4     300
   t47              temp    int &                           4     304
   t48              temp    int                             4     308
   t49              temp    int                             4     312
   t50              temp    class Point *                   4     316
   t51              temp    class Point *                   4     320
   t52              temp    class Point                     8     324
   t53              temp    int                             4     332
   t54              temp    int                             4     336
   t55              temp    int                             4     340
   t56              temp    int                             4     344
   t57              temp    class Point *                   4     348
   t58              temp    class Point *                   4     352
   t59              temp    bool                            1     356
   t60              temp    int                             4     360
   t61              temp    class Point *                   4     364
   t62              temp    class Point *                   4     368
   t63              temp    bool                            1     372
   t64              temp    int                             4     376
   t65              temp    class Segment *                 4     380
   t66              temp    class Segment *                 4     384
   t67              temp    class Segment *                 4     388
   t68              temp    class Segment *                 4     392
   t69              temp    int                             4     396
   t70              temp    int                             4     400
   t71              temp    class Rect *                    4     404
   t72              temp    class Rect *                    4     408
   t73              temp    class Rect *                    4     412
   t74              temp    class Rect *                    4     416
   t75              temp    int                             4     420
   t76              temp    int                             4     424
   t77              temp    int                             4     428

 Code: 196 instruction(s)

    256     t1 = &r
    257     param t1                            (this)
    258     call Rect::Rect(), 1
    259     t2 = &r
    260     param t2                            (this)
    261     param 3
    262     param 4
    263     call Rect::set(int, int), 3
    264     t3 = &q
    265     param t3                            (this)
    266     call Rect::Rect(), 1
    267     t4 = &q
    268     param t4                            (this)
    269     param 5
    270     call Square::side(int), 2
    271     t5 = &r
    272     param t5                            (this)
    273     t6 = call Rect::area(), 1
    274     t7 = &q
    275     param t7                            (this)
    276     t8 = call Rect::area(), 1
    277     t9 = &q
    278     param t9                            (this)
    279     t10 = call Rect::perimeter(), 1
    280     param "%d %d %d %d\n"
    281     param t6
    282     param t8
    283     param t10
    284     param Shape::live
    285     call printf, 5
    286     t11 = &q
    287     asShape = t11
    288     t12 = &r
    289     param t12
    290     t13 = call total(class Rect &), 1
    291     t14 = &q
    292     param t14
    293     t15 = call through(class Shape *), 1
    294     t16 = &q
    295     param t16                           (this)
    296     t17 = call Square::name(), 1
    297     param asShape                       (this)
    298     t18 = call Shape::name(), 1
    299     param "%d %d %c %c\n"
    300     param t13
    301     param t15
    302     param t17
    303     param t18
    304     call printf, 5
    305     t19 = &q
    306     param t19
    307     param 1
    308     call grow(class Rect *, int), 2
    309     t20 = &q
    310     alias = t20
    311     t21 = alias ptr+ 4
    312     *t21 = 10
    313     t22 = &q
    314     param t22                           (this)
    315     t23 = call Rect::area(), 1
    316     param alias                         (this)
    317     t24 = call Rect::perimeter(), 1
    318     param "%d %d\n"
    319     param t23
    320     param t24
    321     call printf, 3
    322     t25 = &pair
    323     param t25                           (this)
    324     call Rect::Rect(), 1
    325     t26 = t25 ptr+ 12
    326     param t26                           (this)
    327     call Rect::Rect(), 1
    328     pair[16] = 6
    329     t27 = &pair
    330     param t27                           (this)
    331     t28 = call Rect::area(), 1
    332     t29 = &pair
    333     t30 = t29 ptr+ 12
    334     param t30                           (this)
    335     t31 = call Rect::area(), 1
    336     t32 = t28 int+ t31
    337     t33 = pair[12]
    338     param "%d %d %d\n"
    339     param t32
    340     param t33
    341     param Shape::live
    342     call printf, 4
    343     param "%d\n"
    344     param Shape::live
    345     call printf, 2
    346     param 3
    347     param 4
    348     t34 = call at(int, int), 2
    349     a = t34
    350     param 1
    351     param 1
    352     t35 = call at(int, int), 2
    353     b = t35
    354     t36 = &a
    355     t37 = &b
    356     param t36                           (this)
    357     param t37
    358     t38 = call Point::operator+=(const class Point &), 2
    359     t39 = &a
    360     t40 = &b
    361     param t39                           (this)
    362     param t40
    363     t41 = call Point::operator+=(const class Point &), 2
    364     t42 = &b
    365     param t41                           (this)
    366     param t42
    367     t43 = call Point::operator+=(const class Point &), 2
    368     t44 = &a
    369     param t44                           (this)
    370     param 0
    371     t45 = call Point::operator[](int), 2
    372     t46 = &a
    373     param t46                           (this)
    374     param 1
    375     t47 = call Point::operator[](int), 2
    376     t48 = *t47
    377     t49 = t48 int* 2
    378     *t45 = t49
    379     t50 = &a
    380     t51 = &b
    381     param t50                           (this)
    382     param t51
    383     t52 = call Point::operator-(const class Point &), 2
    384     c = t52
    385     t53 = a[0]
    386     t54 = a[4]
    387     t55 = c[0]
    388     t56 = c[4]
    389     t57 = &b
    390     t58 = &a
    391     param t57                           (this)
    392     param t58
    393     t59 = call Point::operator<(const class Point &), 2
    394     t60 = booltoint t59
    395     t61 = &a
    396     t62 = &b
    397     param t61                           (this)
    398     param t62
    399     t63 = call Point::operator<(const class Point &), 2
    400     t64 = booltoint t63
    401     param "%d %d %d %d %d %d\n"
    402     param t53
    403     param t54
    404     param t55
    405     param t56
    406     param t60
    407     param t64
    408     call printf, 7
    409     t65 = &s
    410     param t65                           (this)
    411     call Point::Point(), 1
    412     t66 = t65 ptr+ 8
    413     param t66                           (this)
    414     call Point::Point(), 1
    415     t67 = &s
    416     param t67                           (this)
    417     param 1
    418     param 2
    419     param 4
    420     param 6
    421     call Segment::set(int, int, int, int), 5
    422     t68 = &s
    423     param t68                           (this)
    424     t69 = call Segment::length2(), 1
    425     t70 = s[12]
    426     param "%d %d\n"
    427     param t69
    428     param t70
    429     call printf, 3
    430     t71 = &last
    431     param t71                           (this)
    432     call Rect::Rect(), 1
    433     t72 = &last
    434     param t72                           (this)
    435     param 2
    436     param 9
    437     call Rect::set(int, int), 3
    438     t73 = &last
    439     base = t73
    440     t74 = &last
    441     param t74                           (this)
    442     t75 = call Rect::area(), 1
    443     param base                          (this)
    444     t76 = call Shape::area(), 1
    445     t77 = *base
    446     param "%d %d %d\n"
    447     param t75
    448     param t76
    449     param t77
    450     call printf, 4
    451     return Shape::live


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
