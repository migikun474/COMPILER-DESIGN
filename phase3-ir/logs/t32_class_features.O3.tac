============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t32_class_features.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 268 -> 266 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          268 -> 266   (0% fewer)

   constants folded                        7
   algebraic simplifications               2
   common subexpressions                  33
   copies / constants forwarded          122
   temporaries merged away                 2
   dead instructions removed              95
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                4
   calls inlined                          30
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         0

============================================================================
 FUNCTION Point::Point(int)        (link name _ZN5PointC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   a                param   int                             4       4
   t1               temp    class Point *                   4       8
   t2               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    100     *this = a
    101     t1 = this ptr+ 4
    102     t2 = a int<< 1
    103     *t1 = t2
    104     param "(P%d) "
    105     param a
    106     call printf, 2
    107     return

============================================================================
 FUNCTION Point::Point(int, int)        (link name _ZN5PointC1Eii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Point *                   4      12
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    108     *this = a
    109     t1 = this ptr+ 4
    110     *t1 = b
    111     return

============================================================================
 FUNCTION Point::sum()        (link name _ZNK5Point3sumEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    int                             4       4
   t2               temp    class Point *                   4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16

 Code: 5 instruction(s)

    112     t1 = *this
    113     t2 = this ptr+ 4
    114     t3 = *t2
    115     t4 = t1 int+ t3
    116     return t4

============================================================================
 FUNCTION Line::Line(class Point, class Point, int &)        (link name _ZN4LineC1E5PointS0_Ri)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 6 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Line *                    4       0
   a                param   class Point                     8       4
   b                param   class Point                     8      12
   u                param   int &                           4      20
   t1               temp    class Line *                    4      24
   t2               temp    class Line *                    4      28
   t4               temp    class Line *                    4      36
   t7               temp    int *                           4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   (3 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    117     *this = a
    118     t1 = this ptr+ 8
    119     *t1 = b
    120     t2 = this ptr+ 16
    121     *t2 = u
    122     t4 = this ptr+ 20
    123     *t4 = 0
    124     t7 = *t2
    125     t8 = *t7
    126     t9 = t8 int+ 1
    127     *t7 = t9
    128     return

============================================================================
 FUNCTION Line::length()        (link name _ZNK4Line6lengthEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Line *                    4       0
   t1               temp    class Line *                    4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16

 Code: 5 instruction(s)

    129     t1 = this ptr+ 8
    130     t2 = *t1
    131     t3 = *this
    132     t4 = t2 int- t3
    133     return t4

============================================================================
 FUNCTION Line::width()        (link name _ZNK4Line5widthEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Line *                    4       0
   t1               temp    class Line *                    4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    134     t1 = this ptr+ 20
    135     t2 = *t1
    136     return t2

============================================================================
 FUNCTION peek(const class Line &)        (link name _Z4peekRK4Line)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                param   const class Line &              4       0
   t1               temp    const class Line *              4       4
   t2               temp    int                             4       8
   t3               temp    const class Line *              4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 6 instruction(s)

    137     t1 = l ptr+ 4
    138     t2 = *t1
    139     t3 = l ptr+ 12
    140     t4 = *t3
    141     t5 = t2 int+ t4
    142     return t5

============================================================================
 FUNCTION Inspector::look(class Line &)        (link name _ZN9Inspector4lookER4Line)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Inspector *               4       0
   l                param   class Line &                    4       4
   t1               temp    class Line *                    4       8
   t2               temp    class Line *                    4      12
   t3               temp    int *                           4      16
   t4               temp    int                             4      20
   t7               temp    int                             4      32
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    143     t1 = l ptr+ 20
    144     *t1 = 9
    145     t2 = l ptr+ 16
    146     t3 = *t2
    147     t4 = *t3
    148     t7 = t4 int+ 9
    149     return t7

============================================================================
 FUNCTION Counter::Counter()        (link name _ZN7CounterC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0

 Code: 2 instruction(s)

    150     *this = 0
    151     return

============================================================================
 FUNCTION Counter::get()        (link name _ZNK7Counter3getEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    152     t1 = *this
    153     return t1

============================================================================
 FUNCTION Counter::get()        (link name _ZN7Counter3getEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    154     t1 = *this
    155     t2 = t1 int+ 100
    156     return t2

============================================================================
 FUNCTION Counter::add(int)        (link name _ZN7Counter3addEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 4 instruction(s)

    157     t1 = *this
    158     t2 = t1 int+ k
    159     *this = t2
    160     return

============================================================================
 FUNCTION Meters::Meters(int)        (link name _ZN6MetersC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Meters *                  4       0
   x                param   int                             4       4

 Code: 2 instruction(s)

    161     *this = x
    162     return

============================================================================
 FUNCTION useMeters(class Meters)        (link name _Z9useMeters6Meters)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   class Meters                    4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    163     t1 = m[0]
    164     return t1

============================================================================
 FUNCTION Box::Box(int)        (link name _ZN3BoxC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Box *                     4       0
   a                param   int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    165     *this = a
    166     param "[+%d] "
    167     param a
    168     call printf, 2
    169     return

============================================================================
 FUNCTION Box::Box(const class Box &)        (link name _ZN3BoxC1ERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Box *                     4       0
   o                param   const class Box &               4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    170     t1 = *o
    171     t2 = t1 int+ 100
    172     *this = t2
    173     param "[copy %d] "
    174     param t2
    175     call printf, 2
    176     return

============================================================================
 FUNCTION Box::~Box()        (link name _ZN3BoxD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Box *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    177     t1 = *this
    178     param "[-%d] "
    179     param t1
    180     call printf, 2
    181     return

============================================================================
 FUNCTION byValue(class Box)        (link name _Z7byValue3Box)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   b                param   class Box                       4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    182     t1 = b[0]
    183     return t1

============================================================================
 FUNCTION byRef(const class Box &)        (link name _Z5byRefRK3Box)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   b                param   const class Box &               4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    184     t1 = *b
    185     t2 = t1 int<< 1
    186     return t2

============================================================================
 FUNCTION makeBox(int)        (link name _Z7makeBoxi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   t1               temp    class Box                       4       4
   t2               temp    class Box *                     4       8
   t3               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    187     t2 = &t1
    188     t3 = k int* 3
    189     *t2 = t3
    190     param "[+%d] "
    191     param t3
    192     call printf, 2
    193     return t1

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0

 Code: 1 instruction(s)

    194     return a

============================================================================
 FUNCTION pick(class Box)        (link name _Z4pick3Box)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   b                param   class Box                       4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    195     t1 = b[0]
    196     t2 = t1 int+ 1000
    197     return t2

============================================================================
 FUNCTION Base::Base(int)        (link name _ZN4BaseC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   t                param   int                             4       4

 Code: 5 instruction(s)

    198     *this = t
    199     param "<B%d> "
    200     param t
    201     call printf, 2
    202     return

============================================================================
 FUNCTION Derived::Derived(int)        (link name _ZN7DerivedC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Derived *                 4       0
   e                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    class Derived *                 4      12
   (3 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    203     t1 = e int* 10
    204     *this = t1
    205     param "<B%d> "
    206     param t1
    207     call printf, 2
    208     t2 = this ptr+ 4
    209     *t2 = e
    210     param "<D%d> "
    211     param e
    212     call printf, 2
    213     return

============================================================================
 FUNCTION area(class Point)        (link name _Z4area5Point)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   class Point                     8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 4 instruction(s)

    214     t1 = p[0]
    215     t2 = p[4]
    216     t3 = t1 int* t2
    217     return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 64 temporaries, frame 684 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   uses             local   int                             4       0
   l                local   class Line                     24       4
   in               local   class Inspector                 1      28
   seen             local   int                             4      32
   c                local   class Counter                   4      36
   rc               local   const class Counter &           4      40
   m                local   class Meters                    4      44
   b                local   class Box                       4      48
   d                local   class Derived                   8      52
   a                local   int                             4      60
   sum              local   int                             4      64
   t1               temp    class Line *                    4      68
   t2               temp    class Point                     8      72
   t3               temp    class Point *                   4      80
   t4               temp    class Point                     8      84
   t5               temp    class Point *                   4      92
   t6               temp    int *                           4      96
   t18              temp    class Counter *                 4     144
   t24              temp    class Meters *                  4     168
   t26              temp    class Box                       4     176
   t27              temp    class Box *                     4     180
   t30              temp    class Box                       4     192
   t31              temp    class Box *                     4     196
   t38              temp    class Box *                     4     224
   t39              temp    int                             4     228
   t40              temp    class Derived *                 4     232
   t41              temp    class Point                     8     236
   t42              temp    class Point *                   4     244
   t44              temp    class Point                     8     252
   t45              temp    class Point *                   4     260
   t48              temp    int                             4     272
   t49              temp    int                             4     276
   t54              temp    class Point *                   4     296
   t57              temp    class Point *                   4     308
   t60              temp    class Point                     8     320
   t61              temp    class Point                     8     328
   t63              temp    class Line *                    4     340
   t64              temp    class Line *                    4     344
   t65              temp    class Line *                    4     348
   t66              temp    int *                           4     352
   t67              temp    int                             4     356
   t68              temp    int                             4     360
   t71              temp    int                             4     372
   t72              temp    int                             4     376
   t73              temp    int                             4     380
   t76              temp    int                             4     392
   t78              temp    const class Line *              4     400
   t79              temp    int                             4     404
   t80              temp    const class Line *              4     408
   t81              temp    int                             4     412
   t82              temp    int                             4     416
   t87              temp    int *                           4     436
   t88              temp    int                             4     440
   t89              temp    int                             4     444
   t105             temp    class Meters                    4     508
   t106             temp    int                             4     512
   t109             temp    class Box                       4     524
   t110             temp    int                             4     528
   t112             temp    int                             4     536
   t116             temp    int                             4     552
   t117             temp    int                             4     556
   t119             temp    int                             4     564
   t122             temp    class Box                       4     576
   t123             temp    class Box *                     4     580
   t128             temp    class Derived *                 4     600
   t131             temp    class Point *                   4     612
   t133             temp    class Point                     8     620
   t134             temp    int                             4     628
   t135             temp    int                             4     632
   t136             temp    int                             4     636
   t139             temp    class Point *                   4     648
   t142             temp    int                             4     660
   t144             temp    int                             4     668
   t145             temp    int                             4     672
   t147             temp    int                             4     680
   (83 temporaries no longer used after optimization not shown)

 Code: 148 instruction(s)

    218     uses = 0
    219     t1 = &l
    220     t3 = &t2
    221     *t3 = 1
    222     t54 = t3 ptr+ 4
    223     *t54 = 5
    224     t5 = &t4
    225     *t5 = 4
    226     t57 = t5 ptr+ 4
    227     *t57 = 8
    228     param "(P%d) "
    229     param 4
    230     call printf, 2
    231     t6 = &uses
    232     t60 = t2
    233     t61 = t4
    234     *t1 = t60
    235     t63 = t1 ptr+ 8
    236     *t63 = t61
    237     t64 = t1 ptr+ 16
    238     *t64 = t6
    239     t65 = t1 ptr+ 20
    240     *t65 = 0
    241     t66 = *t64
    242     t67 = *t66
    243     t68 = t67 int+ 1
    244     *t66 = t68
    245     t71 = *t63
    246     t72 = *t1
    247     t73 = t71 int- t72
    248     t76 = *t65
    249     t78 = t1 ptr+ 4
    250     t79 = *t78
    251     t80 = t1 ptr+ 12
    252     t81 = *t80
    253     t82 = t79 int+ t81
    254     param "| %d %d %d %d\n"
    255     param t73
    256     param t76
    257     param t82
    258     param uses
    259     call printf, 5
    260     *t65 = 9
    261     t87 = *t64
    262     t88 = *t87
    263     t89 = t88 int+ 9
    264     param "%d %d\n"
    265     param t89
    266     param 9
    267     call printf, 3
    268     t18 = &c
    269     *t18 = 0
    270     *t18 = 3
    271     param "%d %d\n"
    272     param 103
    273     param 3
    274     call printf, 3
    275     t24 = &m
    276     *t24 = 7
    277     t105 = m
    278     t106 = t105[0]
    279     param "%d\n"
    280     param t106
    281     call printf, 2
    282     t27 = &t26
    283     *t27 = 5
    284     param "[+%d] "
    285     param 5
    286     call printf, 2
    287     t109 = t26
    288     t110 = t109[0]
    289     param "%d | "
    290     param t110
    291     call printf, 2
    292     t112 = *t27
    293     param "[-%d] "
    294     param t112
    295     call printf, 2
    296     t31 = &t30
    297     *t31 = 6
    298     param "[+%d] "
    299     param 6
    300     call printf, 2
    301     t116 = *t31
    302     t117 = t116 int<< 1
    303     param "%d | "
    304     param t117
    305     call printf, 2
    306     t119 = *t31
    307     param "[-%d] "
    308     param t119
    309     call printf, 2
    310     param "%d | "
    311     param 7
    312     call printf, 2
    313     t123 = &t122
    314     param t123                          (this)
    315     param 12
    316     call Box::Box(int), 2
    317     b = t122
    318     t38 = &b
    319     t39 = b[0]
    320     param "%d\n"
    321     param t39
    322     call printf, 2
    323     t40 = &d
    324     param t40                           (this)
    325     param 30
    326     call Base::Base(int), 2
    327     t128 = t40 ptr+ 4
    328     *t128 = 3
    329     param "<D%d> "
    330     param 3
    331     call printf, 2
    332     t42 = &t41
    333     *t42 = 6
    334     t131 = t42 ptr+ 4
    335     *t131 = 12
    336     param "(P%d) "
    337     param 6
    338     call printf, 2
    339     t133 = t41
    340     t134 = t133[0]
    341     t135 = t133[4]
    342     t136 = t134 int* t135
    343     t45 = &t44
    344     *t45 = 2
    345     t139 = t45 ptr+ 4
    346     *t139 = 4
    347     param "(P%d) "
    348     param 2
    349     call printf, 2
    350     t142 = *t45
    351     t144 = *t139
    352     t145 = t142 int+ t144
    353     t48 = d[0]
    354     t49 = d[4]
    355     param "%d %d | %d %d\n"
    356     param t48
    357     param t49
    358     param t136
    359     param t145
    360     call printf, 5
    361     t147 = *t38
    362     param "[-%d] "
    363     param t147
    364     call printf, 2
    365     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Point              class_tag     class Point                -           6    -    0  size 8
   Line               class_tag     class Line                 -          14    -    0  size 24
   peek               function      int (const class Line &)   -          22    -    1  _Z4peekRK4Line; defined
   Inspector          class_tag     class Inspector            -          28    -    0  size 1
   Counter            class_tag     class Counter              -          33    -    0  size 4
   Meters             class_tag     class Meters               -          42    -    0  size 4
   useMeters          function      int (class Meters)         -          47    -    1  _Z9useMeters6Meters; defined
   Box                class_tag     class Box                  -          49    -    0  size 4
   byValue            function      int (class Box)            -          56    -    1  _Z7byValue3Box; defined
   byRef              function      int (const class Box &)    -          57    -    1  _Z5byRefRK3Box; defined
   makeBox            function      class Box (int)            -          58    -    1  _Z7makeBoxi; defined
   pick               function      int (int)                  -          59    -    1  _Z4picki; defined
   pick               function      int (class Box)            -          60    -    0  _Z4pick3Box; defined
   Base               class_tag     class Base                 -          62    -    0  size 4
   Derived            class_tag     class Derived              -          67    -    0  size 8, public base Base
   area               function      int (class Point)          -          73    -    1  _Z4area5Point; defined
   main               function      int (void)                 -          75    -    0  defined

 scope: global > class Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      8    4    4  Point::x; public, offset 0
   y                  field         int                        member      8    4    4  Point::y; public, offset 4
   Point              constructor   void (int)                 -           9    -    3  _ZN5PointC1Ei; public
   Point              constructor   void (int, int)            -          10    -    1  _ZN5PointC1Eii; public
   sum                method        int (void) const           -          11    -    1  _ZNK5Point3sumEv; public, defined

 scope: global > class Point > Point()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param       9    4    3  a.1
   a                  parameter     int                        param      10    4    1  a.2
   b                  parameter     int                        param      10    4    1  b.3

 scope: global > class Line
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   from               field         class Point                member     15    8    2  Line::from; private, offset 0
   to                 field         class Point                member     15    8    2  Line::to; private, offset 8
   uses               field         int &                      member     16    4    2  Line::uses; private, offset 16
   count              field         int                        member     17    4    3  Line::count; private, offset 20
   Line               constructor   void (class Point, class Point, int &) -          19    -    1  _ZN4LineC1E5PointS0_Ri; public
   length             method        int (void) const           -          20    -    1  _ZNK4Line6lengthEv; public, defined
   width              method        int (void) const           -          21    -    2  _ZNK4Line5widthEv; public, defined

 scope: global > class Line > Line()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     class Point                param      19    8    1  a.4
   b                  parameter     class Point                param      19    8    1  b.5
   u                  parameter     int &                      param      19    4    2  u.6

 scope: global > peek()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   l                  parameter     const class Line &         param      26    4    2  l.7

 scope: global > class Inspector
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   look               method        int (class Line &)         -          30    -    1  _ZN9Inspector4lookER4Line; public, defined

 scope: global > class Inspector > look()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   l                  parameter     class Line &               param      30    4    3  l.8

 scope: global > class Counter
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  field         int                        member     34    4    3  Counter::n; private, offset 0
   Counter            constructor   void (void)                -          36    -    1  _ZN7CounterC1Ev; public
   get                method        int (void) const           -          37    -    1  _ZNK7Counter3getEv; public, defined
   get                method        int (void)                 -          38    -    1  _ZN7Counter3getEv; public, defined
   add                method        void (int)                 -          39    -    1  _ZN7Counter3addEi; public, defined

 scope: global > class Counter > add()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      39    4    1  k.9

 scope: global > class Meters
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  field         int                        member     44    4    1  Meters::v; public, offset 0
   Meters             constructor   void (int)                 -          45    -    1  _ZN6MetersC1Ei; public

 scope: global > class Meters > Meters()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      45    4    1  x.10

 scope: global > useMeters()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     class Meters               param      47    4    1  m.11

 scope: global > class Box
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  field         int                        member     51    4    8  Box::w; public, offset 0
   Box                constructor   void (int)                 -          52    -    3  _ZN3BoxC1Ei; public
   Box                constructor   void (const class Box &)   -          53    -    0  _ZN3BoxC1ERKS_; public
   ~Box               destructor    void (void)                -          54    -    0  _ZN3BoxD1Ev; public

 scope: global > class Box > Box()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      52    4    1  a.12
   o                  parameter     const class Box &          param      53    4    1  o.13

 scope: global > byValue()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  parameter     class Box                  param      56    4    1  b.14

 scope: global > byRef()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  parameter     const class Box &          param      57    4    1  b.15

 scope: global > makeBox()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      58    4    1  k.16

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      59    4    1  a.17
   b                  parameter     class Box                  param      60    4    1  b.18

 scope: global > class Base
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   tag                field         int                        member     64    4    1  Base::tag; public, offset 0
   Base               constructor   void (int)                 -          65    -    1  _ZN4BaseC1Ei; public

 scope: global > class Base > Base()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     int                        param      65    4    2  t.19

 scope: global > class Derived
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   extra              field         int                        member     69    4    1  Derived::extra; public, offset 4
   Derived            constructor   void (int)                 -          70    -    1  _ZN7DerivedC1Ei; public

 scope: global > class Derived > Derived()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   e                  parameter     int                        param      70    4    3  e.20

 scope: global > area()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     class Point                param      73    8    2  p.21

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   uses               variable      int                        local      76    4    2  uses.22
   l                  variable      class Line                 local      77   24    5  l.23
   in                 variable      class Inspector            local      79    1    1  in.24
   seen               variable      int                        local      80    4    1  seen.25
   c                  variable      class Counter              local      83    4    3  c.26
   rc                 variable      const class Counter &      local      84    4    1  rc.27
   m                  variable      class Meters               local      88    4    1  m.28
   b                  variable      class Box                  local      93    4    1  b.29
   d                  variable      class Derived              local      96    8    2  d.30
   a                  variable      int                        local      97    4    1  a.31
   sum                variable      int                        local      98    4    1  sum.32

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
class Line: size 24, align 4
    +0  class Point from  [private]
    +8  class Point to  [private]
    +16  int & uses  [private]
    +20  int count  [private]
class Inspector: size 1, align 1
class Counter: size 4, align 4
    +0  int n  [private]
class Meters: size 4, align 4
    +0  int v  [public]
class Box: size 4, align 4
    +0  int w  [public]
class Base: size 4, align 4
    +0  int tag  [public]
class Derived: size 8, align 4
    (base Base, public)
    +4  int extra  [public]
