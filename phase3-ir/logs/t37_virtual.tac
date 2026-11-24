============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t37_virtual.c
   Optimization  : no optimization
   Result        : Three address code generated: 27 function(s), 370 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 6 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                class Square                   16  0
   _ZTV5Shape       unsigned int[5]                20  { +0: &Shape::tag(), +4: 0, +8: &Shape::scale(int, int, double, int), +12: &Shape::pick(int), +16: &Shape::pick(double) }
   _ZTV4Rect        unsigned int[6]                24  { +0: &Rect::tag(), +4: &Rect::area(), +8: &Shape::scale(int, int, double, int), +12: &Shape::pick(int), +16: &Shape::pick(double), +20: &Rect::perimeter() }
   _ZTV6Square      unsigned int[6]                24  { +0: &Square::tag(), +4: &Rect::area(), +8: &Square::scale(int, int, double, int), +12: &Shape::pick(int), +16: &Square::pick(double), +20: &Square::perimeter() }
   _ZTV7Counter     unsigned int[2]                 8  { +0: &Counter::step(), +4: &Counter::operator+=(int) }
   _ZTV4Fast        unsigned int[2]                 8  { +0: &Fast::step(), +4: &Fast::operator+=(int) }

 As three address code (initial values, in place before main runs):

    g[...] = 0                     (zero-initialized)
    _ZTV5Shape[0] = &Shape::tag()
    _ZTV5Shape[4] = 0
    _ZTV5Shape[8] = &Shape::scale(int, int, double, int)
    _ZTV5Shape[12] = &Shape::pick(int)
    _ZTV5Shape[16] = &Shape::pick(double)
    _ZTV4Rect[0] = &Rect::tag()
    _ZTV4Rect[4] = &Rect::area()
    _ZTV4Rect[8] = &Shape::scale(int, int, double, int)
    _ZTV4Rect[12] = &Shape::pick(int)
    _ZTV4Rect[16] = &Shape::pick(double)
    _ZTV4Rect[20] = &Rect::perimeter()
    _ZTV6Square[0] = &Square::tag()
    _ZTV6Square[4] = &Rect::area()
    _ZTV6Square[8] = &Square::scale(int, int, double, int)
    _ZTV6Square[12] = &Shape::pick(int)
    _ZTV6Square[16] = &Square::pick(double)
    _ZTV6Square[20] = &Square::perimeter()
    _ZTV7Counter[0] = &Counter::step()
    _ZTV7Counter[4] = &Counter::operator+=(int)
    _ZTV4Fast[0] = &Fast::step()
    _ZTV4Fast[4] = &Fast::operator+=(int)

============================================================================
 FUNCTION Shape::Shape()        (link name _ZN5ShapeC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    unsigned int (*)[5]             4       4
   t2               temp    class Shape *                   4       8
   t3               temp    unsigned int                    4      12
   t4               temp    unsigned int                    4      16
   t5               temp    int                             4      20

 Code: 12 instruction(s)

    100     t1 = &_ZTV5Shape
    101     *this = t1
    102     t2 = this ptr+ 4
    103     *t2 = 1
    104     t3 = *this
    105     t4 = *t3
    106     param this                          (this)
    107     t5 = call *t4, 1                    (virtual Shape::tag())
    108     param "Shape() sees %d\n"
    109     param t5
    110     call printf, 2
    111     return

============================================================================
 FUNCTION Shape::tag()        (link name _ZN5Shape3tagEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    112     return 10

============================================================================
 FUNCTION Shape::scale(int, int, double, int)        (link name _ZN5Shape5scaleEiidi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 4 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   k                param   int                             4       4
   m                param   int                             4       8
   f                param   double                          8      16
   n                param   int                             4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int                             4      40

 Code: 5 instruction(s)

    113     t1 = k int+ m
    114     t2 = doubletoint f
    115     t3 = t1 int+ t2
    116     t4 = t3 int+ n
    117     return t4

============================================================================
 FUNCTION Shape::pick(int)        (link name _ZN5Shape4pickEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   x                param   int                             4       4

 Code: 1 instruction(s)

    118     return x

============================================================================
 FUNCTION Shape::pick(double)        (link name _ZN5Shape4pickEd)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   x                param   double                          8       8
   t1               temp    double                          8      16
   t2               temp    int                             4      24

 Code: 3 instruction(s)

    119     t1 = x double* 2.0
    120     t2 = doubletoint t1
    121     return t2

============================================================================
 FUNCTION Shape::describe()        (link name _ZN5Shape8describeEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 9 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    unsigned int                    4       4
   t2               temp    unsigned int                    4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    unsigned int                    4      20
   t6               temp    unsigned int *                  4      24
   t7               temp    unsigned int                    4      28
   t8               temp    int                             4      32
   t9               temp    int                             4      36

 Code: 12 instruction(s)

    122     t1 = *this
    123     t2 = *t1
    124     param this                          (this)
    125     t3 = call *t2, 1                    (virtual Shape::tag())
    126     t4 = t3 int* 1000
    127     t5 = *this
    128     t6 = t5 ptr+ 4
    129     t7 = *t6
    130     param this                          (this)
    131     t8 = call *t7, 1                    (virtual Shape::area())
    132     t9 = t4 int+ t8
    133     return t9

============================================================================
 FUNCTION Shape::plain()        (link name _ZN5Shape5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    134     return 1

============================================================================
 FUNCTION Rect::Rect()        (link name _ZN4RectC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    unsigned int (*)[6]             4       4
   t2               temp    class Rect *                    4       8
   t3               temp    class Rect *                    4      12

 Code: 9 instruction(s)

    135     param this                          (this)
    136     call Shape::Shape(), 1
    137     t1 = &_ZTV4Rect
    138     *this = t1
    139     t2 = this ptr+ 8
    140     *t2 = 2
    141     t3 = this ptr+ 12
    142     *t3 = 3
    143     return

============================================================================
 FUNCTION Rect::tag()        (link name _ZN4Rect3tagEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0

 Code: 1 instruction(s)

    144     return 20

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

    145     t1 = this ptr+ 8
    146     t2 = *t1
    147     t3 = this ptr+ 12
    148     t4 = *t3
    149     t5 = t2 int* t4
    150     return t5

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

    151     t1 = this ptr+ 8
    152     t2 = *t1
    153     t3 = this ptr+ 12
    154     t4 = *t3
    155     t5 = t2 int+ t4
    156     t6 = 2 int* t5
    157     return t6

============================================================================
 FUNCTION Rect::plain()        (link name _ZN4Rect5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0

 Code: 1 instruction(s)

    158     return 2

============================================================================
 FUNCTION Square::Square()        (link name _ZN6SquareC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   t1               temp    unsigned int (*)[6]             4       4
   t2               temp    class Square *                  4       8
   t3               temp    class Square *                  4      12

 Code: 9 instruction(s)

    159     param this                          (this)
    160     call Rect::Rect(), 1
    161     t1 = &_ZTV6Square
    162     *this = t1
    163     t2 = this ptr+ 8
    164     *t2 = 4
    165     t3 = this ptr+ 12
    166     *t3 = 4
    167     return

============================================================================
 FUNCTION Square::tag()        (link name _ZN6Square3tagEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    168     return 30

============================================================================
 FUNCTION Square::perimeter()        (link name _ZN6Square9perimeterEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   t1               temp    class Square *                  4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 4 instruction(s)

    169     t1 = this ptr+ 8
    170     t2 = *t1
    171     t3 = 4 int* t2
    172     return t3

============================================================================
 FUNCTION Square::scale(int, int, double, int)        (link name _ZN6Square5scaleEiidi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 2 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   k                param   int                             4       4
   m                param   int                             4       8
   f                param   double                          8      16
   n                param   int                             4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32

 Code: 8 instruction(s)

    173     param this                          (this)
    174     param k
    175     param m
    176     param f
    177     param n
    178     t1 = call Shape::scale(int, int, double, int), 5
    179     t2 = 100 int+ t1
    180     return t2

============================================================================
 FUNCTION Square::pick(double)        (link name _ZN6Square4pickEd)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   x                param   double                          8       8
   t1               temp    int                             4      16

 Code: 2 instruction(s)

    181     t1 = int- 1
    182     return t1

============================================================================
 FUNCTION Counter::step()        (link name _ZN7Counter4stepEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   t1               temp    class Counter *                 4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    class Counter *                 4      16
   t5               temp    class Counter *                 4      20
   t6               temp    int                             4      24

 Code: 8 instruction(s)

    183     t1 = this ptr+ 4
    184     t2 = *t1
    185     t3 = t2 int+ 1
    186     t4 = this ptr+ 4
    187     *t4 = t3
    188     t5 = this ptr+ 4
    189     t6 = *t5
    190     return t6

============================================================================
 FUNCTION Counter::operator+=(int)        (link name _ZN7CounterpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   k                param   int                             4       4
   t1               temp    class Counter *                 4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    class Counter *                 4      20

 Code: 6 instruction(s)

    191     t1 = this ptr+ 4
    192     t2 = *t1
    193     t3 = t2 int+ k
    194     t4 = this ptr+ 4
    195     *t4 = t3
    196     return this

============================================================================
 FUNCTION Fast::step()        (link name _ZN4Fast4stepEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Fast *                    4       0
   t1               temp    class Fast *                    4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    class Fast *                    4      16
   t5               temp    class Fast *                    4      20
   t6               temp    int                             4      24

 Code: 8 instruction(s)

    197     t1 = this ptr+ 4
    198     t2 = *t1
    199     t3 = t2 int+ 10
    200     t4 = this ptr+ 4
    201     *t4 = t3
    202     t5 = this ptr+ 4
    203     t6 = *t5
    204     return t6

============================================================================
 FUNCTION Fast::operator+=(int)        (link name _ZN4FastpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Fast *                    4       0
   k                param   int                             4       4
   t1               temp    class Fast *                    4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    class Fast *                    4      24

 Code: 7 instruction(s)

    205     t1 = this ptr+ 4
    206     t2 = *t1
    207     t3 = 100 int* k
    208     t4 = t2 int+ t3
    209     t5 = this ptr+ 4
    210     *t5 = t4
    211     return this

============================================================================
 FUNCTION area2(class Shape &)        (link name _Z5area2R5Shape)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   class Shape &                   4       0
   t1               temp    unsigned int                    4       4
   t2               temp    unsigned int *                  4       8
   t3               temp    unsigned int                    4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 7 instruction(s)

    212     t1 = *s
    213     t2 = t1 ptr+ 4
    214     t3 = *t2
    215     param s                             (this)
    216     t4 = call *t3, 1                    (virtual Shape::area())
    217     t5 = t4 int* 2
    218     return t5

============================================================================
 FUNCTION perim(class Rect)        (link name _Z5perim4Rect)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   class Rect                     16       0
   t1               temp    class Rect *                    4      16
   t2               temp    unsigned int (*)[6]             4      20
   t3               temp    class Rect *                    4      24
   t4               temp    int                             4      28

 Code: 7 instruction(s)

    219     t1 = &r
    220     t2 = &_ZTV4Rect
    221     *t1 = t2
    222     t3 = &r
    223     param t3                            (this)
    224     t4 = call Rect::perimeter(), 1
    225     return t4

============================================================================
 FUNCTION copyOf(class Rect &)        (link name _Z6copyOfR4Rect)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   class Rect &                    4       0
   t1               temp    class Rect                     16       4

 Code: 2 instruction(s)

    226     t1 = *r
    227     return t1

============================================================================
 FUNCTION sum(class Shape **, int)        (link name _Z3sumPP5Shapei)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 9 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   all              param   class Shape **                  4       0
   n                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    class Shape **                  4      20
   t3               temp    class Shape *                   4      24
   t4               temp    unsigned int                    4      28
   t5               temp    unsigned int *                  4      32
   t6               temp    unsigned int                    4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48

 Code: 18 instruction(s)

    228       s = 0
    229       i = 0
    230  L1:  if i int< n goto L2
    231       goto L3
    232  L2:  t1 = i int* 4
    233       t2 = all ptr+ t1
    234       t3 = *t2
    235       t4 = *t3
    236       t5 = t4 ptr+ 4
    237       t6 = *t5
    238       param t3                            (this)
    239       t7 = call *t6, 1                    (virtual Shape::area())
    240       t8 = s int+ t7
    241       s = t8
    242       t9 = i int+ 1
    243       i = t9
    244       goto L1
    245  L3:  return s

============================================================================
 FUNCTION depth(class Rect *, int)        (link name _Z5depthP4Recti)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 8 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   class Rect *                    4       0
   n                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    unsigned int                    4      12
   t3               temp    unsigned int *                  4      16
   t4               temp    unsigned int                    4      20
   t5               temp    int                             4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   t8               temp    int                             4      36

 Code: 16 instruction(s)

    246       if n int== 0 goto L4
    247       goto L5
    248  L4:  t2 = *p
    249       t3 = t2 ptr+ 20
    250       t4 = *t3
    251       param p                             (this)
    252       t5 = call *t4, 1                    (virtual Rect::perimeter())
    253       t1 = t5
    254       goto L6
    255  L5:  t6 = n int- 1
    256       param p
    257       param t6
    258       t7 = call depth(class Rect *, int), 2
    259       t8 = t7 int+ 1
    260       t1 = t8
    261  L6:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 93 temporaries, frame 508 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   class Rect                     16       0
   q                local   class Square                   16      16
   shapes           local   class Shape *[3]               12      32
   rp               local   class Rect *                    4      44
   copy             local   class Rect                     16      48
   r2               local   class Rect                     16      64
   f                local   class Fast                      8      80
   c                local   class Counter &                 4      88
   plainC           local   class Counter                   8      92
   t1               temp    class Square *                  4     100
   t2               temp    class Rect *                    4     104
   t3               temp    class Square *                  4     108
   t4               temp    class Rect *                    4     112
   t5               temp    class Square *                  4     116
   t6               temp    class Square *                  4     120
   t7               temp    class Shape *                   4     124
   t8               temp    unsigned int                    4     128
   t9               temp    unsigned int *                  4     132
   t10              temp    unsigned int                    4     136
   t11              temp    int                             4     140
   t12              temp    class Shape *                   4     144
   t13              temp    unsigned int                    4     148
   t14              temp    unsigned int *                  4     152
   t15              temp    unsigned int                    4     156
   t16              temp    int                             4     160
   t17              temp    class Shape **                  4     164
   t18              temp    int                             4     168
   t19              temp    class Rect *                    4     172
   t20              temp    int                             4     176
   t21              temp    class Square *                  4     180
   t22              temp    int                             4     184
   t23              temp    class Square *                  4     188
   t24              temp    int                             4     192
   t25              temp    class Square *                  4     196
   t26              temp    unsigned int                    4     200
   t27              temp    unsigned int *                  4     204
   t28              temp    unsigned int                    4     208
   t29              temp    int                             4     212
   t30              temp    int                             4     216
   t31              temp    int                             4     220
   t32              temp    unsigned int                    4     224
   t33              temp    unsigned int                    4     228
   t34              temp    int                             4     232
   t35              temp    unsigned int                    4     236
   t36              temp    unsigned int *                  4     240
   t37              temp    unsigned int                    4     244
   t38              temp    int                             4     248
   t39              temp    class Rect *                    4     252
   t40              temp    int                             4     256
   t41              temp    unsigned int                    4     260
   t42              temp    unsigned int *                  4     264
   t43              temp    unsigned int                    4     268
   t44              temp    int                             4     272
   t45              temp    unsigned int                    4     276
   t46              temp    unsigned int *                  4     280
   t47              temp    unsigned int                    4     284
   t48              temp    int                             4     288
   t49              temp    class Rect *                    4     292
   t50              temp    int                             4     296
   t51              temp    class Shape *                   4     300
   t52              temp    unsigned int                    4     304
   t53              temp    unsigned int *                  4     308
   t54              temp    unsigned int                    4     312
   t55              temp    int                             4     316
   t56              temp    class Rect                     16     320
   t57              temp    class Rect *                    4     336
   t58              temp    unsigned int (*)[6]             4     340
   t59              temp    class Rect *                    4     344
   t60              temp    int                             4     348
   t61              temp    class Rect *                    4     352
   t62              temp    int                             4     356
   t63              temp    class Rect *                    4     360
   t64              temp    unsigned int                    4     364
   t65              temp    class Square *                  4     368
   t66              temp    int                             4     372
   t67              temp    class Square *                  4     376
   t68              temp    int                             4     380
   t69              temp    int                             4     384
   t70              temp    class Rect                     16     388
   t71              temp    int                             4     404
   t72              temp    class Rect                     16     408
   t73              temp    class Rect *                    4     424
   t74              temp    unsigned int (*)[6]             4     428
   t75              temp    class Rect *                    4     432
   t76              temp    int                             4     436
   t77              temp    class Square *                  4     440
   t78              temp    int                             4     444
   t79              temp    class Fast *                    4     448
   t80              temp    unsigned int (*)[2]             4     452
   t81              temp    unsigned int (*)[2]             4     456
   t82              temp    class Fast *                    4     460
   t83              temp    unsigned int                    4     464
   t84              temp    unsigned int                    4     468
   t85              temp    unsigned int                    4     472
   t86              temp    unsigned int *                  4     476
   t87              temp    unsigned int                    4     480
   t88              temp    class Counter &                 4     484
   t89              temp    class Counter *                 4     488
   t90              temp    unsigned int (*)[2]             4     492
   t91              temp    class Counter *                 4     496
   t92              temp    int                             4     500
   t93              temp    int                             4     504

 Code: 208 instruction(s)

    262     t1 = &g
    263     param t1                            (this)
    264     call Square::Square(), 1
    265     t2 = &r
    266     param t2                            (this)
    267     call Rect::Rect(), 1
    268     t3 = &q
    269     param t3                            (this)
    270     call Square::Square(), 1
    271     t4 = &r
    272     shapes[0] = t4
    273     t5 = &q
    274     shapes[4] = t5
    275     t6 = &g
    276     shapes[8] = t6
    277     t7 = shapes[0]
    278     t8 = *t7
    279     t9 = t8 ptr+ 4
    280     t10 = *t9
    281     param t7                            (this)
    282     t11 = call *t10, 1                  (virtual Shape::area())
    283     t12 = shapes[4]
    284     t13 = *t12
    285     t14 = t13 ptr+ 4
    286     t15 = *t14
    287     param t12                           (this)
    288     t16 = call *t15, 1                  (virtual Shape::area())
    289     t17 = &shapes
    290     param t17
    291     param 3
    292     t18 = call sum(class Shape **, int), 2
    293     param "%d %d %d\n"
    294     param t11
    295     param t16
    296     param t18
    297     call printf, 4
    298     t19 = &r
    299     param t19                           (this)
    300     t20 = call Shape::describe(), 1
    301     t21 = &q
    302     param t21                           (this)
    303     t22 = call Shape::describe(), 1
    304     t23 = &q
    305     param t23
    306     t24 = call area2(class Shape &), 1
    307     param "%d %d %d\n"
    308     param t20
    309     param t22
    310     param t24
    311     call printf, 4
    312     t25 = &q
    313     rp = t25
    314     t26 = *rp
    315     t27 = t26 ptr+ 20
    316     t28 = *t27
    317     param rp                            (this)
    318     t29 = call *t28, 1                  (virtual Rect::perimeter())
    319     param rp                            (this)
    320     t30 = call Rect::perimeter(), 1
    321     param rp                            (this)
    322     t31 = call Rect::plain(), 1
    323     t32 = *rp
    324     t33 = *t32
    325     param rp                            (this)
    326     t34 = call *t33, 1                  (virtual Rect::tag())
    327     param "%d %d %d %d\n"
    328     param t29
    329     param t30
    330     param t31
    331     param t34
    332     call printf, 5
    333     t35 = *rp
    334     t36 = t35 ptr+ 8
    335     t37 = *t36
    336     param rp                            (this)
    337     param 1
    338     param 2
    339     param 3.5
    340     param 4
    341     t38 = call *t37, 5                  (virtual Shape::scale(int, int, double, int))
    342     t39 = &r
    343     param t39                           (this)
    344     param 1
    345     param 2
    346     param 3.5
    347     param 4
    348     t40 = call Shape::scale(int, int, double, int), 5
    349     param "%d %d\n"
    350     param t38
    351     param t40
    352     call printf, 3
    353     t41 = *rp
    354     t42 = t41 ptr+ 12
    355     t43 = *t42
    356     param rp                            (this)
    357     param 5
    358     t44 = call *t43, 2                  (virtual Shape::pick(int))
    359     t45 = *rp
    360     t46 = t45 ptr+ 16
    361     t47 = *t46
    362     param rp                            (this)
    363     param 2.5
    364     t48 = call *t47, 2                  (virtual Shape::pick(double))
    365     t49 = &r
    366     param t49                           (this)
    367     param 2.5
    368     t50 = call Shape::pick(double), 2
    369     t51 = shapes[0]
    370     t52 = *t51
    371     t53 = t52 ptr+ 12
    372     t54 = *t53
    373     param t51                           (this)
    374     param 7
    375     t55 = call *t54, 2                  (virtual Shape::pick(int))
    376     param "%d %d %d %d\n"
    377     param t44
    378     param t48
    379     param t50
    380     param t55
    381     call printf, 5
    382     t56 = *rp
    383     copy = t56
    384     t57 = &copy
    385     t58 = &_ZTV4Rect
    386     *t57 = t58
    387     t59 = &copy
    388     param t59                           (this)
    389     t60 = call Rect::perimeter(), 1
    390     t61 = &copy
    391     param t61                           (this)
    392     t62 = call Rect::tag(), 1
    393     param "%d %d\n"
    394     param t60
    395     param t62
    396     call printf, 3
    397     t63 = &r2
    398     param t63                           (this)
    399     call Rect::Rect(), 1
    400     r2[8] = 9
    401     t64 = *rp
    402     *rp = r2
    403     *rp = t64
    404     t65 = &q
    405     param t65                           (this)
    406     t66 = call Square::perimeter(), 1
    407     t67 = &q
    408     param t67                           (this)
    409     t68 = call Square::tag(), 1
    410     t69 = q[8]
    411     param "%d %d %d\n"
    412     param t66
    413     param t68
    414     param t69
    415     call printf, 4
    416     t70 = *rp
    417     param t70
    418     t71 = call perim(class Rect), 1
    419     param rp
    420     t72 = call copyOf(class Rect &), 1
    421     t73 = &t72
    422     t74 = &_ZTV4Rect
    423     *t73 = t74
    424     t75 = &t72
    425     param t75                           (this)
    426     t76 = call Rect::perimeter(), 1
    427     param "%d %d\n"
    428     param t71
    429     param t76
    430     call printf, 3
    431     t77 = &q
    432     param t77
    433     param 5
    434     t78 = call depth(class Rect *, int), 2
    435     param "%d\n"
    436     param t78
    437     call printf, 2
    438     t79 = &f
    439     t80 = &_ZTV7Counter
    440     *t79 = t80
    441     t81 = &_ZTV4Fast
    442     *t79 = t81
    443     f[4] = 0
    444     t82 = &f
    445     c = t82
    446     t83 = *c
    447     t84 = *t83
    448     param c                             (this)
    449     call *t84, 1                        (virtual Counter::step())
    450     t85 = *c
    451     t86 = t85 ptr+ 4
    452     t87 = *t86
    453     param c                             (this)
    454     param 2
    455     t88 = call *t87, 2                  (virtual Counter::operator+=(int))
    456     t89 = &plainC
    457     t90 = &_ZTV7Counter
    458     *t89 = t90
    459     plainC[4] = 0
    460     t91 = &plainC
    461     param t91                           (this)
    462     call Counter::step(), 1
    463     t92 = f[4]
    464     t93 = plainC[4]
    465     param "%d %d\n"
    466     param t92
    467     param t93
    468     call printf, 3
    469     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Shape              class_tag     class Shape                -           9    -    0  size 8
   Rect               class_tag     class Rect                 -          21    -    0  size 16, public base Shape
   Square             class_tag     class Square               -          30    -    0  size 16, public base Rect
   Counter            class_tag     class Counter              -          38    -    0  size 8
   Fast               class_tag     class Fast                 -          44    -    0  size 8, public base Counter
   g                  variable      class Square               global     49   16    1  
   area2              function      int (class Shape &)        -          51    -    1  _Z5area2R5Shape; defined
   perim              function      int (class Rect)           -          52    -    1  _Z5perim4Rect; defined
   copyOf             function      class Rect (class Rect &)  -          53    -    1  _Z6copyOfR4Rect; defined
   sum                function      int (class Shape **, int)  -          54    -    1  _Z3sumPP5Shapei; defined
   depth              function      int (class Rect *, int)    -          55    -    2  _Z5depthP4Recti; defined
   main               function      int (void)                 -          57    -    0  defined

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     11    4    1  Shape::id; public, offset 4
   Shape              constructor   void (void)                -          12    -    0  _ZN5ShapeC1Ev; public
   tag                method        int (void)                 -          13    -    2  _ZN5Shape3tagEv; public, virtual, slot 0, defined
   area               method        int (void)                 -          14    -    5  _ZN5Shape4areaEv; public, pure virtual, slot 1
   scale              method        int (int, int, double, int) -          15    -    3  _ZN5Shape5scaleEiidi; public, virtual, slot 2, defined
   pick               method        int (int)                  -          16    -    2  _ZN5Shape4pickEi; public, virtual, slot 3, defined
   pick               method        int (double)               -          17    -    2  _ZN5Shape4pickEd; public, virtual, slot 4, defined
   describe           method        int (void)                 -          18    -    2  _ZN5Shape8describeEv; public, defined
   plain              method        int (void)                 -          19    -    0  _ZN5Shape5plainEv; public, defined

 scope: global > class Shape > scale()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      15    4    1  k.1
   m                  parameter     int                        param      15    4    1  m.2
   f                  parameter     double                     param      15    8    1  f.3
   n                  parameter     int                        param      15    4    1  n.4

 scope: global > class Shape > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      16    4    1  x.5
   x                  parameter     double                     param      17    8    1  x.6

 scope: global > class Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  field         int                        member     23    4    7  Rect::w; public, offset 8
   h                  field         int                        member     23    4    4  Rect::h; public, offset 12
   Rect               constructor   void (void)                -          24    -    2  _ZN4RectC1Ev; public
   tag                method        int (void)                 -          25    -    2  _ZN4Rect3tagEv; public, virtual, slot 0, defined
   area               method        int (void)                 -          26    -    0  _ZN4Rect4areaEv; public, virtual, slot 1, defined
   perimeter          method        int (void)                 -          27    -    6  _ZN4Rect9perimeterEv; public, virtual, slot 5, defined
   plain              method        int (void)                 -          28    -    1  _ZN4Rect5plainEv; public, defined

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Square             constructor   void (void)                -          32    -    2  _ZN6SquareC1Ev; public
   tag                method        int (void)                 -          33    -    1  _ZN6Square3tagEv; public, virtual, slot 0, defined
   perimeter          method        int (void)                 -          34    -    1  _ZN6Square9perimeterEv; public, virtual, slot 5, defined
   scale              method        int (int, int, double, int) -          35    -    0  _ZN6Square5scaleEiidi; public, virtual, slot 2, defined
   pick               method        int (double)               -          36    -    0  _ZN6Square4pickEd; public, virtual, slot 4, defined

 scope: global > class Square > scale()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      35    4    1  k.7
   m                  parameter     int                        param      35    4    1  m.8
   f                  parameter     double                     param      35    8    1  f.9
   n                  parameter     int                        param      35    4    1  n.10

 scope: global > class Square > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     double                     param      36    8    0  x.11

 scope: global > class Counter
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  field         int                        member     40    4   14  Counter::n; public, offset 4
   step               method        int (void)                 -          41    -    2  _ZN7Counter4stepEv; public, virtual, slot 0, defined
   operator+=         method        class Counter &(int)       -          42    -    1  _ZN7CounterpLEi; public, virtual, slot 1, defined

 scope: global > class Counter > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      42    4    1  k.12

 scope: global > class Fast
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   step               method        int (void)                 -          46    -    0  _ZN4Fast4stepEv; public, virtual, slot 0, defined
   operator+=         method        class Counter &(int)       -          47    -    0  _ZN4FastpLEi; public, virtual, slot 1, defined

 scope: global > class Fast > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      47    4    1  k.13

 scope: global > area2()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     class Shape &              param      51    4    1  s.14

 scope: global > perim()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect                 param      52   16    1  r.15

 scope: global > copyOf()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect &               param      53    4    1  r.16

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   all                parameter     class Shape **             param      54    4    1  all.17
   n                  parameter     int                        param      54    4    1  n.18
   s                  variable      int                        local      54    4    2  s.19
   i                  variable      int                        local      54    4    4  i.20

 scope: global > depth()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     class Rect *               param      55    4    2  p.21
   n                  parameter     int                        param      55    4    2  n.22

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Rect                 local      58   16    4  r.23
   q                  variable      class Square               local      59   16    8  q.24
   shapes             variable      class Shape *[3]           local      60   12    7  shapes.25
   rp                 variable      class Rect *               local      64    4   11  rp.26
   copy               variable      class Rect                 local      68   16    2  copy.27
   r2                 variable      class Rect                 local      70   16    2  r2.28
   f                  variable      class Fast                 local      76    8    3  f.29
   c                  variable      class Counter &            local      78    4    2  c.30
   plainC             variable      class Counter              local      81    8    3  plainC.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Shape: size 8, align 4
    +0  vtable pointer
    slot 0: Shape::tag
    slot 1: Shape::area  (pure)
    slot 2: Shape::scale
    slot 3: Shape::pick
    slot 4: Shape::pick
    (abstract)
    +4  int id  [public]
class Rect: size 16, align 4
    (base Shape, public)
    slot 0: Rect::tag
    slot 1: Rect::area
    slot 2: Shape::scale
    slot 3: Shape::pick
    slot 4: Shape::pick
    slot 5: Rect::perimeter
    +8  int w  [public]
    +12  int h  [public]
class Square: size 16, align 4
    (base Rect, public)
    slot 0: Square::tag
    slot 1: Rect::area
    slot 2: Square::scale
    slot 3: Shape::pick
    slot 4: Square::pick
    slot 5: Square::perimeter
class Counter: size 8, align 4
    +0  vtable pointer
    slot 0: Counter::step
    slot 1: Counter::operator+=
    +4  int n  [public]
class Fast: size 8, align 4
    (base Counter, public)
    slot 0: Fast::step
    slot 1: Fast::operator+=
