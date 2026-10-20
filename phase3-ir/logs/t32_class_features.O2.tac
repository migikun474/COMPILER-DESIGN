============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t32_class_features.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 268 -> 240 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          268 -> 240   (10% fewer)

   constants folded                        0
   algebraic simplifications               2
   common subexpressions                  23
   copies / constants forwarded           27
   temporaries merged away                 0
   dead instructions removed              24
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                4

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

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   t1               temp    class Box                       4       4
   t2               temp    class Box *                     4       8
   t3               temp    int                             4      12

 Code: 6 instruction(s)

    187     t2 = &t1
    188     t3 = k int* 3
    189     param t2                            (this)
    190     param t3
    191     call Box::Box(int), 2
    192     return t1

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0

 Code: 1 instruction(s)

    193     return a

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

    194     t1 = b[0]
    195     t2 = t1 int+ 1000
    196     return t2

============================================================================
 FUNCTION Base::Base(int)        (link name _ZN4BaseC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   t                param   int                             4       4

 Code: 5 instruction(s)

    197     *this = t
    198     param "<B%d> "
    199     param t
    200     call printf, 2
    201     return

============================================================================
 FUNCTION Derived::Derived(int)        (link name _ZN7DerivedC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Derived *                 4       0
   e                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    class Derived *                 4      12
   (1 temporary no longer used after optimization not shown)

 Code: 10 instruction(s)

    202     t1 = e int* 10
    203     param this                          (this)
    204     param t1
    205     call Base::Base(int), 2
    206     t2 = this ptr+ 4
    207     *t2 = e
    208     param "<D%d> "
    209     param e
    210     call printf, 2
    211     return

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

    212     t1 = p[0]
    213     t2 = p[4]
    214     t3 = t1 int* t2
    215     return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 36 temporaries, frame 284 bytes

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
   t8               temp    int                             4     104
   t10              temp    int                             4     112
   t12              temp    int                             4     120
   t13              temp    class Inspector *               4     124
   t15              temp    int                             4     132
   t17              temp    int                             4     140
   t18              temp    class Counter *                 4     144
   t22              temp    int                             4     160
   t23              temp    int                             4     164
   t24              temp    class Meters *                  4     168
   t25              temp    int                             4     172
   t26              temp    class Box                       4     176
   t27              temp    class Box *                     4     180
   t28              temp    int                             4     184
   t30              temp    class Box                       4     192
   t31              temp    class Box *                     4     196
   t33              temp    int                             4     204
   t35              temp    int                             4     212
   t36              temp    class Box                       4     216
   t38              temp    class Box *                     4     224
   t39              temp    int                             4     228
   t40              temp    class Derived *                 4     232
   t41              temp    class Point                     8     236
   t42              temp    class Point *                   4     244
   t43              temp    int                             4     248
   t44              temp    class Point                     8     252
   t45              temp    class Point *                   4     260
   t47              temp    int                             4     268
   t48              temp    int                             4     272
   t49              temp    int                             4     276
   (14 temporaries no longer used after optimization not shown)

 Code: 124 instruction(s)

    216     uses = 0
    217     t1 = &l
    218     t3 = &t2
    219     param t3                            (this)
    220     param 1
    221     param 5
    222     call Point::Point(int, int), 3
    223     t5 = &t4
    224     param t5                            (this)
    225     param 4
    226     call Point::Point(int), 2
    227     t6 = &uses
    228     param t1                            (this)
    229     param t2
    230     param t4
    231     param t6
    232     call Line::Line(class Point, class Point, int &), 4
    233     param t1                            (this)
    234     t8 = call Line::length(), 1
    235     param t1                            (this)
    236     t10 = call Line::width(), 1
    237     param t1
    238     t12 = call peek(const class Line &), 1
    239     param "| %d %d %d %d\n"
    240     param t8
    241     param t10
    242     param t12
    243     param uses
    244     call printf, 5
    245     t13 = &in
    246     param t13                           (this)
    247     param t1
    248     t15 = call Inspector::look(class Line &), 2
    249     param t1                            (this)
    250     t17 = call Line::width(), 1
    251     param "%d %d\n"
    252     param t15
    253     param t17
    254     call printf, 3
    255     t18 = &c
    256     param t18                           (this)
    257     call Counter::Counter(), 1
    258     param t18                           (this)
    259     param 3
    260     call Counter::add(int), 2
    261     param t18                           (this)
    262     t22 = call Counter::get(), 1
    263     param t18                           (this)
    264     t23 = call Counter::get(), 1
    265     param "%d %d\n"
    266     param t22
    267     param t23
    268     call printf, 3
    269     t24 = &m
    270     param t24                           (this)
    271     param 7
    272     call Meters::Meters(int), 2
    273     param m
    274     t25 = call useMeters(class Meters), 1
    275     param "%d\n"
    276     param t25
    277     call printf, 2
    278     t27 = &t26
    279     param t27                           (this)
    280     param 5
    281     call Box::Box(int), 2
    282     param t26
    283     t28 = call byValue(class Box), 1
    284     param "%d | "
    285     param t28
    286     call printf, 2
    287     param t27                           (this)
    288     call Box::~Box(), 1
    289     t31 = &t30
    290     param t31                           (this)
    291     param 6
    292     call Box::Box(int), 2
    293     param t31
    294     t33 = call byRef(const class Box &), 1
    295     param "%d | "
    296     param t33
    297     call printf, 2
    298     param t31                           (this)
    299     call Box::~Box(), 1
    300     param 7
    301     t35 = call pick(int), 1
    302     param "%d | "
    303     param t35
    304     call printf, 2
    305     param 4
    306     t36 = call makeBox(int), 1
    307     b = t36
    308     t38 = &b
    309     t39 = b[0]
    310     param "%d\n"
    311     param t39
    312     call printf, 2
    313     t40 = &d
    314     param t40                           (this)
    315     param 3
    316     call Derived::Derived(int), 2
    317     t42 = &t41
    318     param t42                           (this)
    319     param 6
    320     call Point::Point(int), 2
    321     param t41
    322     t43 = call area(class Point), 1
    323     t45 = &t44
    324     param t45                           (this)
    325     param 2
    326     call Point::Point(int), 2
    327     param t45                           (this)
    328     t47 = call Point::sum(), 1
    329     t48 = d[0]
    330     t49 = d[4]
    331     param "%d %d | %d %d\n"
    332     param t48
    333     param t49
    334     param t43
    335     param t47
    336     call printf, 5
    337     param t38                           (this)
    338     call Box::~Box(), 1
    339     return 0


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
