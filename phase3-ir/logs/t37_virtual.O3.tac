============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t37_virtual.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 370 -> 349 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          370 -> 349   (5% fewer)

   constants folded                        7
   algebraic simplifications               4
   common subexpressions                  34
   copies / constants forwarded          140
   temporaries merged away                 8
   dead instructions removed              92
   jumps removed or redirected             2
   unreachable instructions removed        0
   propagated across blocks                1
   dead assignments removed                3
   calls inlined                          24
   tail calls turned into jumps            0
   common subexpressions across blocks      3
   loops unrolled                          2
   unreachable functions removed           8

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
 FUNCTION Rect::Rect()        (link name _ZN4RectC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 8 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    unsigned int (*)[6]             4       4
   t2               temp    class Rect *                    4       8
   t3               temp    class Rect *                    4      12
   t5               temp    unsigned int (*)[5]             4      20
   t6               temp    class Shape *                   4      24
   t7               temp    unsigned int                    4      28
   t8               temp    unsigned int                    4      32
   t9               temp    int                             4      36
   (1 temporary no longer used after optimization not shown)

 Code: 18 instruction(s)

    122     t5 = &_ZTV5Shape
    123     *this = t5
    124     t6 = this ptr+ 4
    125     *t6 = 1
    126     t7 = *this
    127     t8 = *t7
    128     param this                          (this)
    129     t9 = call *t8, 1                    (virtual Shape::tag())
    130     param "Shape() sees %d\n"
    131     param t9
    132     call printf, 2
    133     t1 = &_ZTV4Rect
    134     *this = t1
    135     t2 = this ptr+ 8
    136     *t2 = 2
    137     t3 = this ptr+ 12
    138     *t3 = 3
    139     return

============================================================================
 FUNCTION Rect::tag()        (link name _ZN4Rect3tagEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0

 Code: 1 instruction(s)

    140     return 20

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

    141     t1 = this ptr+ 8
    142     t2 = *t1
    143     t3 = this ptr+ 12
    144     t4 = *t3
    145     t5 = t2 int* t4
    146     return t5

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

    147     t1 = this ptr+ 8
    148     t2 = *t1
    149     t3 = this ptr+ 12
    150     t4 = *t3
    151     t5 = t2 int+ t4
    152     t6 = t5 int<< 1
    153     return t6

============================================================================
 FUNCTION Square::tag()        (link name _ZN6Square3tagEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    154     return 30

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

    155     t1 = this ptr+ 8
    156     t2 = *t1
    157     t3 = t2 int<< 2
    158     return t3

============================================================================
 FUNCTION Square::scale(int, int, double, int)        (link name _ZN6Square5scaleEiidi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 5 temporaries, frame 76 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   k                param   int                             4       4
   m                param   int                             4       8
   f                param   double                          8      16
   n                param   int                             4      24
   t2               temp    int                             4      32
   t8               temp    int                             4      60
   t9               temp    int                             4      64
   t10              temp    int                             4      68
   t11              temp    int                             4      72
   (6 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    159     t8 = k int+ m
    160     t9 = doubletoint f
    161     t10 = t8 int+ t9
    162     t11 = t10 int+ n
    163     t2 = 100 int+ t11
    164     return t2

============================================================================
 FUNCTION Square::pick(double)        (link name _ZN6Square4pickEd)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   x                param   double                          8       8
   (1 temporary no longer used after optimization not shown)

 Code: 1 instruction(s)

    165     return -1

============================================================================
 FUNCTION Counter::step()        (link name _ZN7Counter4stepEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   t1               temp    class Counter *                 4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (3 temporaries no longer used after optimization not shown)

 Code: 5 instruction(s)

    166     t1 = this ptr+ 4
    167     t2 = *t1
    168     t3 = t2 int+ 1
    169     *t1 = t3
    170     return t3

============================================================================
 FUNCTION Counter::operator+=(int)        (link name _ZN7CounterpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   k                param   int                             4       4
   t1               temp    class Counter *                 4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    171     t1 = this ptr+ 4
    172     t2 = *t1
    173     t3 = t2 int+ k
    174     *t1 = t3
    175     return this

============================================================================
 FUNCTION Fast::step()        (link name _ZN4Fast4stepEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Fast *                    4       0
   t1               temp    class Fast *                    4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (3 temporaries no longer used after optimization not shown)

 Code: 5 instruction(s)

    176     t1 = this ptr+ 4
    177     t2 = *t1
    178     t3 = t2 int+ 10
    179     *t1 = t3
    180     return t3

============================================================================
 FUNCTION Fast::operator+=(int)        (link name _ZN4FastpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Fast *                    4       0
   k                param   int                             4       4
   t1               temp    class Fast *                    4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   (1 temporary no longer used after optimization not shown)

 Code: 6 instruction(s)

    181     t1 = this ptr+ 4
    182     t2 = *t1
    183     t3 = k int* 100
    184     t4 = t2 int+ t3
    185     *t1 = t4
    186     return this

============================================================================
 FUNCTION depth(class Rect *, int)        (link name _Z5depthP4Recti)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   class Rect *                    4       0
   n                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    unsigned int                    4      12
   t3               temp    unsigned int *                  4      16
   t4               temp    unsigned int                    4      20
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   (2 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    187       if n int!= 0 goto L1
    188       t2 = *p
    189       t3 = t2 ptr+ 20
    190       t4 = *t3
    191       param p                             (this)
    192       t1 = call *t4, 1                    (virtual Rect::perimeter())
    193       goto L2
    194  L1:  t6 = n int- 1
    195       param p
    196       param t6
    197       t7 = call depth(class Rect *, int), 2
    198       t1 = t7 int+ 1
    199  L2:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 122 temporaries, frame 964 bytes

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
   t26              temp    unsigned int                    4     200
   t27              temp    unsigned int *                  4     204
   t28              temp    unsigned int                    4     208
   t29              temp    int                             4     212
   t32              temp    unsigned int                    4     224
   t33              temp    unsigned int                    4     228
   t34              temp    int                             4     232
   t35              temp    unsigned int                    4     236
   t36              temp    unsigned int *                  4     240
   t37              temp    unsigned int                    4     244
   t38              temp    int                             4     248
   t41              temp    unsigned int                    4     260
   t42              temp    unsigned int *                  4     264
   t43              temp    unsigned int                    4     268
   t44              temp    int                             4     272
   t45              temp    unsigned int                    4     276
   t46              temp    unsigned int *                  4     280
   t47              temp    unsigned int                    4     284
   t48              temp    int                             4     288
   t51              temp    class Shape *                   4     300
   t52              temp    unsigned int                    4     304
   t53              temp    unsigned int *                  4     308
   t54              temp    unsigned int                    4     312
   t55              temp    int                             4     316
   t57              temp    class Rect *                    4     336
   t63              temp    class Rect *                    4     360
   t64              temp    unsigned int                    4     364
   t69              temp    int                             4     384
   t72              temp    class Rect                     16     408
   t73              temp    class Rect *                    4     424
   t78              temp    int                             4     444
   t79              temp    class Fast *                    4     448
   t80              temp    unsigned int (*)[2]             4     452
   t81              temp    unsigned int (*)[2]             4     456
   t83              temp    unsigned int                    4     464
   t84              temp    unsigned int                    4     468
   t85              temp    unsigned int                    4     472
   t86              temp    unsigned int *                  4     476
   t87              temp    unsigned int                    4     480
   t89              temp    class Counter *                 4     488
   t92              temp    int                             4     500
   t93              temp    int                             4     504
   t95              temp    unsigned int (*)[6]             4     512
   t96              temp    class Square *                  4     516
   t97              temp    class Square *                  4     520
   t99              temp    unsigned int (*)[6]             4     528
   t100             temp    class Rect *                    4     532
   t101             temp    class Rect *                    4     536
   t104             temp    class Square *                  4     548
   t105             temp    class Square *                  4     552
   t106             temp    class Shape **                  4     556
   t108             temp    int                             4     564
   t109             temp    int                             4     568
   t110             temp    int                             4     572
   t111             temp    class Shape **                  4     576
   t112             temp    class Shape *                   4     580
   t113             temp    unsigned int                    4     584
   t114             temp    unsigned int *                  4     588
   t115             temp    unsigned int                    4     592
   t116             temp    int                             4     596
   t118             temp    unsigned int                    4     604
   t119             temp    unsigned int                    4     608
   t120             temp    int                             4     612
   t121             temp    int                             4     616
   t122             temp    unsigned int                    4     620
   t123             temp    unsigned int *                  4     624
   t124             temp    unsigned int                    4     628
   t125             temp    int                             4     632
   t126             temp    int                             4     636
   t128             temp    unsigned int                    4     644
   t129             temp    unsigned int                    4     648
   t130             temp    int                             4     652
   t131             temp    int                             4     656
   t132             temp    unsigned int                    4     660
   t133             temp    unsigned int *                  4     664
   t134             temp    unsigned int                    4     668
   t135             temp    int                             4     672
   t136             temp    int                             4     676
   t138             temp    unsigned int                    4     684
   t139             temp    unsigned int *                  4     688
   t140             temp    unsigned int                    4     692
   t141             temp    int                             4     696
   t142             temp    int                             4     700
   t145             temp    int                             4     712
   t147             temp    int                             4     720
   t148             temp    int                             4     724
   t149             temp    int                             4     728
   t165             temp    class Rect *                    4     808
   t166             temp    int                             4     812
   t167             temp    class Rect *                    4     816
   t168             temp    int                             4     820
   t169             temp    int                             4     824
   t170             temp    int                             4     828
   t174             temp    class Rect *                    4     844
   t175             temp    class Rect *                    4     848
   t178             temp    int                             4     860
   t179             temp    int                             4     864
   t181             temp    class Rect                     16     872
   t182             temp    class Rect *                    4     888
   t184             temp    int                             4     896
   t188             temp    class Rect *                    4     924
   t189             temp    int                             4     928
   t190             temp    class Rect *                    4     932
   t191             temp    int                             4     936
   t192             temp    int                             4     940
   t193             temp    int                             4     944
   t195             temp    class Counter *                 4     952
   t196             temp    int                             4     956
   t197             temp    int                             4     960
   (75 temporaries no longer used after optimization not shown)

 Code: 249 instruction(s)

    200       t1 = &g
    201       param t1                            (this)
    202       call Rect::Rect(), 1
    203       t95 = &_ZTV6Square
    204       *t1 = t95
    205       t96 = t1 ptr+ 8
    206       *t96 = 4
    207       t97 = t1 ptr+ 12
    208       *t97 = 4
    209       t2 = &r
    210       param t2                            (this)
    211       call Shape::Shape(), 1
    212       t99 = &_ZTV4Rect
    213       *t2 = t99
    214       t100 = t2 ptr+ 8
    215       *t100 = 2
    216       t101 = t2 ptr+ 12
    217       *t101 = 3
    218       t3 = &q
    219       param t3                            (this)
    220       call Rect::Rect(), 1
    221       *t3 = t95
    222       t104 = t3 ptr+ 8
    223       *t104 = 4
    224       t105 = t3 ptr+ 12
    225       *t105 = 4
    226       shapes[0] = t2
    227       shapes[4] = t3
    228       shapes[8] = t1
    229       t7 = shapes[0]
    230       t8 = *t7
    231       t9 = t8 ptr+ 4
    232       t10 = *t9
    233       param t7                            (this)
    234       t11 = call *t10, 1                  (virtual Shape::area())
    235       t12 = shapes[4]
    236       t13 = *t12
    237       t14 = t13 ptr+ 4
    238       t15 = *t14
    239       param t12                           (this)
    240       t16 = call *t15, 1                  (virtual Shape::area())
    241       t106 = &shapes
    242       t108 = 0
    243       t109 = 0
    244  L3:  if t109 int>= 3 goto L4
    245       t110 = t109 int<< 2
    246       t111 = t106 ptr+ t110
    247       t112 = *t111
    248       t113 = *t112
    249       t114 = t113 ptr+ 4
    250       t115 = *t114
    251       param t112                          (this)
    252       t116 = call *t115, 1                (virtual Shape::area())
    253       t108 = t108 int+ t116
    254       t109 = t109 int+ 1
    255       if t109 int>= 3 goto L4
    256       t110 = t109 int<< 2
    257       t111 = t106 ptr+ t110
    258       t112 = *t111
    259       t113 = *t112
    260       t114 = t113 ptr+ 4
    261       t115 = *t114
    262       param t112                          (this)
    263       t116 = call *t115, 1                (virtual Shape::area())
    264       t108 = t108 int+ t116
    265       t109 = t109 int+ 1
    266       goto L3
    267  L4:  param "%d %d %d\n"
    268       param t11
    269       param t16
    270       param t108
    271       call printf, 4
    272       t118 = *t2
    273       t119 = *t118
    274       param t2                            (this)
    275       t120 = call *t119, 1                (virtual Shape::tag())
    276       t121 = t120 int* 1000
    277       t122 = *t2
    278       t123 = t122 ptr+ 4
    279       t124 = *t123
    280       param t2                            (this)
    281       t125 = call *t124, 1                (virtual Shape::area())
    282       t126 = t121 int+ t125
    283       t128 = *t3
    284       t129 = *t128
    285       param t3                            (this)
    286       t130 = call *t129, 1                (virtual Shape::tag())
    287       t131 = t130 int* 1000
    288       t132 = *t3
    289       t133 = t132 ptr+ 4
    290       t134 = *t133
    291       param t3                            (this)
    292       t135 = call *t134, 1                (virtual Shape::area())
    293       t136 = t131 int+ t135
    294       t138 = *t3
    295       t139 = t138 ptr+ 4
    296       t140 = *t139
    297       param t3                            (this)
    298       t141 = call *t140, 1                (virtual Shape::area())
    299       t142 = t141 int<< 1
    300       param "%d %d %d\n"
    301       param t126
    302       param t136
    303       param t142
    304       call printf, 4
    305       t26 = *t3
    306       t27 = t26 ptr+ 20
    307       t28 = *t27
    308       param t3                            (this)
    309       t29 = call *t28, 1                  (virtual Rect::perimeter())
    310       t145 = *t104
    311       t147 = *t105
    312       t148 = t145 int+ t147
    313       t149 = t148 int<< 1
    314       t32 = *t3
    315       t33 = *t32
    316       param t3                            (this)
    317       t34 = call *t33, 1                  (virtual Rect::tag())
    318       param "%d %d %d %d\n"
    319       param t29
    320       param t149
    321       param 2
    322       param t34
    323       call printf, 5
    324       t35 = *t3
    325       t36 = t35 ptr+ 8
    326       t37 = *t36
    327       param t3                            (this)
    328       param 1
    329       param 2
    330       param 3.5
    331       param 4
    332       t38 = call *t37, 5                  (virtual Shape::scale(int, int, double, int))
    333       param "%d %d\n"
    334       param t38
    335       param 10
    336       call printf, 3
    337       t41 = *t3
    338       t42 = t41 ptr+ 12
    339       t43 = *t42
    340       param t3                            (this)
    341       param 5
    342       t44 = call *t43, 2                  (virtual Shape::pick(int))
    343       t45 = *t3
    344       t46 = t45 ptr+ 16
    345       t47 = *t46
    346       param t3                            (this)
    347       param 2.5
    348       t48 = call *t47, 2                  (virtual Shape::pick(double))
    349       t51 = shapes[0]
    350       t52 = *t51
    351       t53 = t52 ptr+ 12
    352       t54 = *t53
    353       param t51                           (this)
    354       param 7
    355       t55 = call *t54, 2                  (virtual Shape::pick(int))
    356       param "%d %d %d %d\n"
    357       param t44
    358       param t48
    359       param 5
    360       param t55
    361       call printf, 5
    362       copy = *t3
    363       t57 = &copy
    364       *t57 = t99
    365       t165 = t57 ptr+ 8
    366       t166 = *t165
    367       t167 = t57 ptr+ 12
    368       t168 = *t167
    369       t169 = t166 int+ t168
    370       t170 = t169 int<< 1
    371       param "%d %d\n"
    372       param t170
    373       param 20
    374       call printf, 3
    375       t63 = &r2
    376       param t63                           (this)
    377       call Shape::Shape(), 1
    378       *t63 = t99
    379       t174 = t63 ptr+ 8
    380       *t174 = 2
    381       t175 = t63 ptr+ 12
    382       *t175 = 3
    383       r2[8] = 9
    384       t64 = *t3
    385       *t3 = r2
    386       *t3 = t64
    387       t178 = *t104
    388       t179 = t178 int<< 2
    389       t69 = q[8]
    390       param "%d %d %d\n"
    391       param t179
    392       param 30
    393       param t69
    394       call printf, 4
    395       t181 = *t3
    396       t182 = &t181
    397       *t182 = t99
    398       param t182                          (this)
    399       t184 = call Rect::perimeter(), 1
    400       t72 = *t3
    401       t73 = &t72
    402       *t73 = t99
    403       t188 = t73 ptr+ 8
    404       t189 = *t188
    405       t190 = t73 ptr+ 12
    406       t191 = *t190
    407       t192 = t189 int+ t191
    408       t193 = t192 int<< 1
    409       param "%d %d\n"
    410       param t184
    411       param t193
    412       call printf, 3
    413       param t3
    414       param 5
    415       t78 = call depth(class Rect *, int), 2
    416       param "%d\n"
    417       param t78
    418       call printf, 2
    419       t79 = &f
    420       t80 = &_ZTV7Counter
    421       *t79 = t80
    422       t81 = &_ZTV4Fast
    423       *t79 = t81
    424       f[4] = 0
    425       t83 = *t79
    426       t84 = *t83
    427       param t79                           (this)
    428       call *t84, 1                        (virtual Counter::step())
    429       t85 = *t79
    430       t86 = t85 ptr+ 4
    431       t87 = *t86
    432       param t79                           (this)
    433       param 2
    434       call *t87, 2                        (virtual Counter::operator+=(int))
    435       t89 = &plainC
    436       *t89 = t80
    437       plainC[4] = 0
    438       t195 = t89 ptr+ 4
    439       t196 = *t195
    440       t197 = t196 int+ 1
    441       *t195 = t197
    442       t92 = f[4]
    443       t93 = plainC[4]
    444       param "%d %d\n"
    445       param t92
    446       param t93
    447       call printf, 3
    448       return 0


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
