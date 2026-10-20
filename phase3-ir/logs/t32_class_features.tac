============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t32_class_features.c
   Optimization  : no optimization
   Result        : Three address code generated: 26 function(s), 268 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION Point::Point(int)        (link name _ZN5PointC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   a                param   int                             4       4
   t1               temp    class Point *                   4       8
   t2               temp    int                             4      12
   t3               temp    class Point *                   4      16

 Code: 9 instruction(s)

    100     *this = a
    101     t1 = this ptr+ 4
    102     t2 = a int* 2
    103     t3 = this ptr+ 4
    104     *t3 = t2
    105     param "(P%d) "
    106     param a
    107     call printf, 2
    108     return

============================================================================
 FUNCTION Point::Point(int, int)        (link name _ZN5PointC1Eii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Point *                   4      12
   t2               temp    class Point *                   4      16

 Code: 5 instruction(s)

    109     *this = a
    110     t1 = this ptr+ 4
    111     t2 = this ptr+ 4
    112     *t2 = b
    113     return

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

    114     t1 = *this
    115     t2 = this ptr+ 4
    116     t3 = *t2
    117     t4 = t1 int+ t3
    118     return t4

============================================================================
 FUNCTION Line::Line(class Point, class Point, int &)        (link name _ZN4LineC1E5PointS0_Ri)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 9 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Line *                    4       0
   a                param   class Point                     8       4
   b                param   class Point                     8      12
   u                param   int &                           4      20
   t1               temp    class Line *                    4      24
   t2               temp    class Line *                    4      28
   t3               temp    class Line *                    4      32
   t4               temp    class Line *                    4      36
   t5               temp    class Line *                    4      40
   t6               temp    class Line *                    4      44
   t7               temp    int *                           4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56

 Code: 15 instruction(s)

    119     *this = a
    120     t1 = this ptr+ 8
    121     *t1 = b
    122     t2 = this ptr+ 16
    123     t3 = this ptr+ 16
    124     *t3 = u
    125     t4 = this ptr+ 20
    126     t5 = this ptr+ 20
    127     *t5 = 0
    128     t6 = this ptr+ 16
    129     t7 = *t6
    130     t8 = *t7
    131     t9 = t8 int+ 1
    132     *t7 = t9
    133     return

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

    134     t1 = this ptr+ 8
    135     t2 = *t1
    136     t3 = *this
    137     t4 = t2 int- t3
    138     return t4

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

    139     t1 = this ptr+ 20
    140     t2 = *t1
    141     return t2

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

    142     t1 = l ptr+ 4
    143     t2 = *t1
    144     t3 = l ptr+ 12
    145     t4 = *t3
    146     t5 = t2 int+ t4
    147     return t5

============================================================================
 FUNCTION Inspector::look(class Line &)        (link name _ZN9Inspector4lookER4Line)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Inspector *               4       0
   l                param   class Line &                    4       4
   t1               temp    class Line *                    4       8
   t2               temp    class Line *                    4      12
   t3               temp    int *                           4      16
   t4               temp    int                             4      20
   t5               temp    class Line *                    4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32

 Code: 9 instruction(s)

    148     t1 = l ptr+ 20
    149     *t1 = 9
    150     t2 = l ptr+ 16
    151     t3 = *t2
    152     t4 = *t3
    153     t5 = l ptr+ 20
    154     t6 = *t5
    155     t7 = t4 int+ t6
    156     return t7

============================================================================
 FUNCTION Counter::Counter()        (link name _ZN7CounterC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0

 Code: 2 instruction(s)

    157     *this = 0
    158     return

============================================================================
 FUNCTION Counter::get()        (link name _ZNK7Counter3getEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counter *                 4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    159     t1 = *this
    160     return t1

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

    161     t1 = *this
    162     t2 = t1 int+ 100
    163     return t2

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

    164     t1 = *this
    165     t2 = t1 int+ k
    166     *this = t2
    167     return

============================================================================
 FUNCTION Meters::Meters(int)        (link name _ZN6MetersC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Meters *                  4       0
   x                param   int                             4       4

 Code: 2 instruction(s)

    168     *this = x
    169     return

============================================================================
 FUNCTION useMeters(class Meters)        (link name _Z9useMeters6Meters)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   class Meters                    4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    170     t1 = m[0]
    171     return t1

============================================================================
 FUNCTION Box::Box(int)        (link name _ZN3BoxC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Box *                     4       0
   a                param   int                             4       4
   t1               temp    int                             4       8

 Code: 6 instruction(s)

    172     *this = a
    173     t1 = *this
    174     param "[+%d] "
    175     param t1
    176     call printf, 2
    177     return

============================================================================
 FUNCTION Box::Box(const class Box &)        (link name _ZN3BoxC1ERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Box *                     4       0
   o                param   const class Box &               4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 8 instruction(s)

    178     t1 = *o
    179     t2 = t1 int+ 100
    180     *this = t2
    181     t3 = *this
    182     param "[copy %d] "
    183     param t3
    184     call printf, 2
    185     return

============================================================================
 FUNCTION Box::~Box()        (link name _ZN3BoxD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Box *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    186     t1 = *this
    187     param "[-%d] "
    188     param t1
    189     call printf, 2
    190     return

============================================================================
 FUNCTION byValue(class Box)        (link name _Z7byValue3Box)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   b                param   class Box                       4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    191     t1 = b[0]
    192     return t1

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

    193     t1 = *b
    194     t2 = t1 int* 2
    195     return t2

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

    196     t2 = &t1
    197     t3 = k int* 3
    198     param t2                            (this)
    199     param t3
    200     call Box::Box(int), 2
    201     return t1

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0

 Code: 1 instruction(s)

    202     return a

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

    203     t1 = b[0]
    204     t2 = t1 int+ 1000
    205     return t2

============================================================================
 FUNCTION Base::Base(int)        (link name _ZN4BaseC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   t                param   int                             4       4

 Code: 5 instruction(s)

    206     *this = t
    207     param "<B%d> "
    208     param t
    209     call printf, 2
    210     return

============================================================================
 FUNCTION Derived::Derived(int)        (link name _ZN7DerivedC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Derived *                 4       0
   e                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    class Derived *                 4      12
   t3               temp    class Derived *                 4      16

 Code: 11 instruction(s)

    211     t1 = e int* 10
    212     param this                          (this)
    213     param t1
    214     call Base::Base(int), 2
    215     t2 = this ptr+ 4
    216     t3 = this ptr+ 4
    217     *t3 = e
    218     param "<D%d> "
    219     param e
    220     call printf, 2
    221     return

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

    222     t1 = p[0]
    223     t2 = p[4]
    224     t3 = t1 int* t2
    225     return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 50 temporaries, frame 284 bytes

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
   t7               temp    class Line *                    4     100
   t8               temp    int                             4     104
   t9               temp    class Line *                    4     108
   t10              temp    int                             4     112
   t11              temp    class Line *                    4     116
   t12              temp    int                             4     120
   t13              temp    class Inspector *               4     124
   t14              temp    class Line *                    4     128
   t15              temp    int                             4     132
   t16              temp    class Line *                    4     136
   t17              temp    int                             4     140
   t18              temp    class Counter *                 4     144
   t19              temp    class Counter *                 4     148
   t20              temp    class Counter *                 4     152
   t21              temp    class Counter *                 4     156
   t22              temp    int                             4     160
   t23              temp    int                             4     164
   t24              temp    class Meters *                  4     168
   t25              temp    int                             4     172
   t26              temp    class Box                       4     176
   t27              temp    class Box *                     4     180
   t28              temp    int                             4     184
   t29              temp    class Box *                     4     188
   t30              temp    class Box                       4     192
   t31              temp    class Box *                     4     196
   t32              temp    class Box *                     4     200
   t33              temp    int                             4     204
   t34              temp    class Box *                     4     208
   t35              temp    int                             4     212
   t36              temp    class Box                       4     216
   t37              temp    class Box *                     4     220
   t38              temp    class Box *                     4     224
   t39              temp    int                             4     228
   t40              temp    class Derived *                 4     232
   t41              temp    class Point                     8     236
   t42              temp    class Point *                   4     244
   t43              temp    int                             4     248
   t44              temp    class Point                     8     252
   t45              temp    class Point *                   4     260
   t46              temp    class Point *                   4     264
   t47              temp    int                             4     268
   t48              temp    int                             4     272
   t49              temp    int                             4     276
   t50              temp    class Box *                     4     280

 Code: 142 instruction(s)

    226     uses = 0
    227     t1 = &l
    228     t3 = &t2
    229     param t3                            (this)
    230     param 1
    231     param 5
    232     call Point::Point(int, int), 3
    233     t5 = &t4
    234     param t5                            (this)
    235     param 4
    236     call Point::Point(int), 2
    237     t6 = &uses
    238     param t1                            (this)
    239     param t2
    240     param t4
    241     param t6
    242     call Line::Line(class Point, class Point, int &), 4
    243     t7 = &l
    244     param t7                            (this)
    245     t8 = call Line::length(), 1
    246     t9 = &l
    247     param t9                            (this)
    248     t10 = call Line::width(), 1
    249     t11 = &l
    250     param t11
    251     t12 = call peek(const class Line &), 1
    252     param "| %d %d %d %d\n"
    253     param t8
    254     param t10
    255     param t12
    256     param uses
    257     call printf, 5
    258     t13 = &in
    259     t14 = &l
    260     param t13                           (this)
    261     param t14
    262     t15 = call Inspector::look(class Line &), 2
    263     seen = t15
    264     t16 = &l
    265     param t16                           (this)
    266     t17 = call Line::width(), 1
    267     param "%d %d\n"
    268     param seen
    269     param t17
    270     call printf, 3
    271     t18 = &c
    272     param t18                           (this)
    273     call Counter::Counter(), 1
    274     t19 = &c
    275     rc = t19
    276     t20 = &c
    277     param t20                           (this)
    278     param 3
    279     call Counter::add(int), 2
    280     t21 = &c
    281     param t21                           (this)
    282     t22 = call Counter::get(), 1
    283     param rc                            (this)
    284     t23 = call Counter::get(), 1
    285     param "%d %d\n"
    286     param t22
    287     param t23
    288     call printf, 3
    289     t24 = &m
    290     param t24                           (this)
    291     param 7
    292     call Meters::Meters(int), 2
    293     param m
    294     t25 = call useMeters(class Meters), 1
    295     param "%d\n"
    296     param t25
    297     call printf, 2
    298     t27 = &t26
    299     param t27                           (this)
    300     param 5
    301     call Box::Box(int), 2
    302     param t26
    303     t28 = call byValue(class Box), 1
    304     param "%d | "
    305     param t28
    306     call printf, 2
    307     t29 = &t26
    308     param t29                           (this)
    309     call Box::~Box(), 1
    310     t31 = &t30
    311     param t31                           (this)
    312     param 6
    313     call Box::Box(int), 2
    314     t32 = &t30
    315     param t32
    316     t33 = call byRef(const class Box &), 1
    317     param "%d | "
    318     param t33
    319     call printf, 2
    320     t34 = &t30
    321     param t34                           (this)
    322     call Box::~Box(), 1
    323     param 7
    324     t35 = call pick(int), 1
    325     param "%d | "
    326     param t35
    327     call printf, 2
    328     param 4
    329     t36 = call makeBox(int), 1
    330     t37 = &t36
    331     b = t36
    332     t38 = &b
    333     t39 = b[0]
    334     param "%d\n"
    335     param t39
    336     call printf, 2
    337     t40 = &d
    338     param t40                           (this)
    339     param 3
    340     call Derived::Derived(int), 2
    341     t42 = &t41
    342     param t42                           (this)
    343     param 6
    344     call Point::Point(int), 2
    345     param t41
    346     t43 = call area(class Point), 1
    347     a = t43
    348     t45 = &t44
    349     param t45                           (this)
    350     param 2
    351     call Point::Point(int), 2
    352     t46 = &t44
    353     param t46                           (this)
    354     t47 = call Point::sum(), 1
    355     sum = t47
    356     t48 = d[0]
    357     t49 = d[4]
    358     param "%d %d | %d %d\n"
    359     param t48
    360     param t49
    361     param a
    362     param sum
    363     call printf, 5
    364     t50 = &b
    365     param t50                           (this)
    366     call Box::~Box(), 1
    367     return 0


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
