============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t31_virtual.c
   Optimization  : no optimization
   Result        : Three address code generated: 27 function(s), 386 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 9 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   _ZTV6Animal      unsigned int[4]                16  { +0: &Animal::name(), +4: 0, +8: &Animal::speed(), +12: 0 }
   _ZTV3Dog         unsigned int[4]                16  { +0: &Dog::name(), +4: 0, +8: &Dog::speed(), +12: 0 }
   _ZTV5Puppy       unsigned int[4]                16  { +0: &Puppy::name(), +4: 0, +8: &Dog::speed(), +12: 0 }
   _ZTV7Swimmer     unsigned int[4]                16  { +0: &Swimmer::swim(), +4: 0, +8: &Swimmer::dive(int), +12: 0 }
   _ZTV4Seal        unsigned int[6]                24  { +0: &Seal::name(), +4: 0, +8: &Animal::speed(), +12: 0, +16: &Seal::swim(), +20: 0 }
   _ZTV4Seal_8      unsigned int[4]                16  { +0: &Seal::swim(), +4: -8, +8: &Swimmer::dive(int), +12: 0 }
   _ZTV5Shape       unsigned int[4]                16  { +0: 0, +4: 0, +8: &Shape::sides(), +12: 0 }
   _ZTV4Rect        unsigned int[4]                16  { +0: &Rect::area(), +4: 0, +8: &Rect::sides(), +12: 0 }
   _ZTV6Square      unsigned int[4]                16  { +0: &Square::area(), +4: 0, +8: &Rect::sides(), +12: 0 }

============================================================================
 FUNCTION Animal::Animal(int)        (link name _ZN6AnimalC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 9 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   n                param   int                             4       4
   t1               temp    unsigned int (*)[4]             4       8
   t2               temp    class Animal *                  4      12
   t3               temp    class Animal *                  4      16
   t4               temp    unsigned int *                  4      20
   t5               temp    void *                          4      24
   t6               temp    unsigned int *                  4      28
   t7               temp    int                             4      32
   t8               temp    class Animal *                  4      36
   t9               temp    const char *                    4      40

 Code: 16 instruction(s)

    100     t1 = &_ZTV6Animal
    101     *this = t1
    102     t2 = this ptr+ 4
    103     t3 = this ptr+ 4
    104     *t3 = n
    105     t4 = *this
    106     t5 = *t4
    107     t6 = t4 ptr+ 4
    108     t7 = *t6
    109     t8 = this ptr+ t7
    110     param t8                            (this)
    111     t9 = call *t5, 1                    (virtual Animal::name())
    112     param "[A %s] "
    113     param t9
    114     call printf, 2
    115     return

============================================================================
 FUNCTION Animal::~Animal()        (link name _ZN6AnimalD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   t1               temp    unsigned int (*)[4]             4       4
   t2               temp    unsigned int *                  4       8
   t3               temp    void *                          4      12
   t4               temp    unsigned int *                  4      16
   t5               temp    int                             4      20
   t6               temp    class Animal *                  4      24
   t7               temp    const char *                    4      28

 Code: 13 instruction(s)

    116     t1 = &_ZTV6Animal
    117     *this = t1
    118     t2 = *this
    119     t3 = *t2
    120     t4 = t2 ptr+ 4
    121     t5 = *t4
    122     t6 = this ptr+ t5
    123     param t6                            (this)
    124     t7 = call *t3, 1                    (virtual Animal::name())
    125     param "[~A %s] "
    126     param t7
    127     call printf, 2
    128     return

============================================================================
 FUNCTION Animal::name()        (link name _ZNK6Animal4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0

 Code: 1 instruction(s)

    129     return "animal"

============================================================================
 FUNCTION Animal::speed()        (link name _ZN6Animal5speedEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   t1               temp    class Animal *                  4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    130     t1 = this ptr+ 4
    131     t2 = *t1
    132     return t2

============================================================================
 FUNCTION Animal::describe()        (link name _ZN6Animal8describeEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 11 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   t1               temp    unsigned int *                  4       4
   t2               temp    unsigned int *                  4       8
   t3               temp    void *                          4      12
   t4               temp    unsigned int *                  4      16
   t5               temp    int                             4      20
   t6               temp    class Animal *                  4      24
   t7               temp    int                             4      28
   t8               temp    int                             4      32
   t9               temp    class Animal *                  4      36
   t10              temp    int                             4      40
   t11              temp    int                             4      44

 Code: 13 instruction(s)

    133     t1 = *this
    134     t2 = t1 ptr+ 8
    135     t3 = *t2
    136     t4 = t1 ptr+ 12
    137     t5 = *t4
    138     t6 = this ptr+ t5
    139     param t6                            (this)
    140     t7 = call *t3, 1                    (virtual Animal::speed())
    141     t8 = t7 int* 10
    142     t9 = this ptr+ 4
    143     t10 = *t9
    144     t11 = t8 int+ t10
    145     return t11

============================================================================
 FUNCTION Dog::Dog(int)        (link name _ZN3DogC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 9 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   b                param   int                             4       4
   t1               temp    unsigned int (*)[4]             4       8
   t2               temp    class Dog *                     4      12
   t3               temp    class Dog *                     4      16
   t4               temp    unsigned int *                  4      20
   t5               temp    void *                          4      24
   t6               temp    unsigned int *                  4      28
   t7               temp    int                             4      32
   t8               temp    class Dog *                     4      36
   t9               temp    const char *                    4      40

 Code: 19 instruction(s)

    146     param this                          (this)
    147     param 4
    148     call Animal::Animal(int), 2
    149     t1 = &_ZTV3Dog
    150     *this = t1
    151     t2 = this ptr+ 8
    152     t3 = this ptr+ 8
    153     *t3 = b
    154     t4 = *this
    155     t5 = *t4
    156     t6 = t4 ptr+ 4
    157     t7 = *t6
    158     t8 = this ptr+ t7
    159     param t8                            (this)
    160     t9 = call *t5, 1                    (virtual Dog::name())
    161     param "[D %s] "
    162     param t9
    163     call printf, 2
    164     return

============================================================================
 FUNCTION Dog::~Dog()        (link name _ZN3DogD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    unsigned int (*)[4]             4       4
   t2               temp    unsigned int *                  4       8
   t3               temp    void *                          4      12
   t4               temp    unsigned int *                  4      16
   t5               temp    int                             4      20
   t6               temp    class Dog *                     4      24
   t7               temp    const char *                    4      28

 Code: 15 instruction(s)

    165     t1 = &_ZTV3Dog
    166     *this = t1
    167     t2 = *this
    168     t3 = *t2
    169     t4 = t2 ptr+ 4
    170     t5 = *t4
    171     t6 = this ptr+ t5
    172     param t6                            (this)
    173     t7 = call *t3, 1                    (virtual Dog::name())
    174     param "[~D %s] "
    175     param t7
    176     call printf, 2
    177     param this                          (this)
    178     call Animal::~Animal(), 1
    179     return

============================================================================
 FUNCTION Dog::name()        (link name _ZNK3Dog4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0

 Code: 1 instruction(s)

    180     return "dog"

============================================================================
 FUNCTION Dog::speed()        (link name _ZN3Dog5speedEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 4 instruction(s)

    181     t1 = this ptr+ 8
    182     t2 = *t1
    183     t3 = 12 int+ t2
    184     return t3

============================================================================
 FUNCTION Puppy::Puppy()        (link name _ZN5PuppyC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Puppy *                   4       0
   t1               temp    unsigned int (*)[4]             4       4

 Code: 6 instruction(s)

    185     param this                          (this)
    186     param 1
    187     call Dog::Dog(int), 2
    188     t1 = &_ZTV5Puppy
    189     *this = t1
    190     return

============================================================================
 FUNCTION Puppy::name()        (link name _ZNK5Puppy4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Puppy *                   4       0

 Code: 1 instruction(s)

    191     return "puppy"

============================================================================
 FUNCTION Swimmer::Swimmer()        (link name _ZN7SwimmerC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Swimmer *                 4       0
   t1               temp    unsigned int (*)[4]             4       4
   t2               temp    class Swimmer *                 4       8
   t3               temp    class Swimmer *                 4      12

 Code: 6 instruction(s)

    192     t1 = &_ZTV7Swimmer
    193     *this = t1
    194     t2 = this ptr+ 4
    195     t3 = this ptr+ 4
    196     *t3 = 3
    197     return

============================================================================
 FUNCTION Swimmer::swim()        (link name _ZN7Swimmer4swimEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Swimmer *                 4       0
   t1               temp    class Swimmer *                 4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    198     t1 = this ptr+ 4
    199     t2 = *t1
    200     return t2

============================================================================
 FUNCTION Swimmer::dive(int)        (link name _ZN7Swimmer4diveEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Swimmer *                 4       0
   m                param   int                             4       4
   t1               temp    class Swimmer *                 4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 4 instruction(s)

    201     t1 = this ptr+ 4
    202     t2 = *t1
    203     t3 = t2 int+ m
    204     return t3

============================================================================
 FUNCTION Seal::Seal()        (link name _ZN4SealC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Seal *                    4       0
   t1               temp    class Seal *                    4       4
   t2               temp    unsigned int (*)[6]             4       8
   t3               temp    unsigned int (*)[4]             4      12
   t4               temp    class Seal *                    4      16
   t5               temp    class Seal *                    4      20
   t6               temp    class Seal *                    4      24

 Code: 15 instruction(s)

    205     param this                          (this)
    206     param 0
    207     call Animal::Animal(int), 2
    208     t1 = this ptr+ 8
    209     param t1                            (this)
    210     call Swimmer::Swimmer(), 1
    211     t2 = &_ZTV4Seal
    212     *this = t2
    213     t3 = &_ZTV4Seal_8
    214     t4 = this ptr+ 8
    215     *t4 = t3
    216     t5 = this ptr+ 16
    217     t6 = this ptr+ 16
    218     *t6 = 7
    219     return

============================================================================
 FUNCTION Seal::name()        (link name _ZNK4Seal4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Seal *                    4       0

 Code: 1 instruction(s)

    220     return "seal"

============================================================================
 FUNCTION Seal::swim()        (link name _ZN4Seal4swimEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Seal *                    4       0
   t1               temp    class Seal *                    4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    class Seal *                    4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24

 Code: 7 instruction(s)

    221     t1 = this ptr+ 16
    222     t2 = *t1
    223     t3 = t2 int* 2
    224     t4 = this ptr+ 12
    225     t5 = *t4
    226     t6 = t3 int+ t5
    227     return t6

============================================================================
 FUNCTION Shape::sides()        (link name _ZN5Shape5sidesEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    228     return 0

============================================================================
 FUNCTION Shape::twice()        (link name _ZN5Shape5twiceEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    unsigned int *                  4       4
   t2               temp    void *                          4       8
   t3               temp    unsigned int *                  4      12
   t4               temp    int                             4      16
   t5               temp    class Shape *                   4      20
   t6               temp    int                             4      24
   t7               temp    int                             4      28

 Code: 9 instruction(s)

    229     t1 = *this
    230     t2 = *t1
    231     t3 = t1 ptr+ 4
    232     t4 = *t3
    233     t5 = this ptr+ t4
    234     param t5                            (this)
    235     t6 = call *t2, 1                    (virtual Shape::area())
    236     t7 = t6 int* 2
    237     return t7

============================================================================
 FUNCTION Rect::Rect(int, int)        (link name _ZN4RectC1Eii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 6 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    unsigned int (*)[4]             4      12
   t2               temp    unsigned int (*)[4]             4      16
   t3               temp    class Rect *                    4      20
   t4               temp    class Rect *                    4      24
   t5               temp    class Rect *                    4      28
   t6               temp    class Rect *                    4      32

 Code: 11 instruction(s)

    238     t1 = &_ZTV5Shape
    239     *this = t1
    240     t2 = &_ZTV4Rect
    241     *this = t2
    242     t3 = this ptr+ 4
    243     t4 = this ptr+ 4
    244     *t4 = a
    245     t5 = this ptr+ 8
    246     t6 = this ptr+ 8
    247     *t6 = b
    248     return

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

    249     t1 = this ptr+ 4
    250     t2 = *t1
    251     t3 = this ptr+ 8
    252     t4 = *t3
    253     t5 = t2 int* t4
    254     return t5

============================================================================
 FUNCTION Rect::sides()        (link name _ZN4Rect5sidesEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0

 Code: 1 instruction(s)

    255     return 4

============================================================================
 FUNCTION Square::Square(int)        (link name _ZN6SquareC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   s                param   int                             4       4
   t1               temp    unsigned int (*)[4]             4       8

 Code: 7 instruction(s)

    256     param this                          (this)
    257     param s
    258     param s
    259     call Rect::Rect(int, int), 3
    260     t1 = &_ZTV6Square
    261     *this = t1
    262     return

============================================================================
 FUNCTION Square::area()        (link name _ZN6Square4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    263     param this                          (this)
    264     t1 = call Rect::area(), 1
    265     t2 = t1 int+ 1
    266     return t2

============================================================================
 FUNCTION total(class Shape &)        (link name _Z5totalR5Shape)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 14 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   class Shape &                   4       0
   t1               temp    unsigned int *                  4       4
   t2               temp    void *                          4       8
   t3               temp    unsigned int *                  4      12
   t4               temp    int                             4      16
   t5               temp    class Shape *                   4      20
   t6               temp    int                             4      24
   t7               temp    unsigned int *                  4      28
   t8               temp    unsigned int *                  4      32
   t9               temp    void *                          4      36
   t10              temp    unsigned int *                  4      40
   t11              temp    int                             4      44
   t12              temp    class Shape *                   4      48
   t13              temp    int                             4      52
   t14              temp    int                             4      56

 Code: 17 instruction(s)

    267     t1 = *s
    268     t2 = *t1
    269     t3 = t1 ptr+ 4
    270     t4 = *t3
    271     t5 = s ptr+ t4
    272     param t5                            (this)
    273     t6 = call *t2, 1                    (virtual Shape::area())
    274     t7 = *s
    275     t8 = t7 ptr+ 8
    276     t9 = *t8
    277     t10 = t7 ptr+ 12
    278     t11 = *t10
    279     t12 = s ptr+ t11
    280     param t12                           (this)
    281     t13 = call *t9, 1                   (virtual Shape::sides())
    282     t14 = t6 int+ t13
    283     return t14

============================================================================
 FUNCTION race(class Animal *)        (link name _Z4raceP6Animal)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   class Animal *                  4       0
   t1               temp    unsigned int *                  4       4
   t2               temp    unsigned int *                  4       8
   t3               temp    void *                          4      12
   t4               temp    unsigned int *                  4      16
   t5               temp    int                             4      20
   t6               temp    class Animal *                  4      24
   t7               temp    int                             4      28

 Code: 9 instruction(s)

    284     t1 = *a
    285     t2 = t1 ptr+ 8
    286     t3 = *t2
    287     t4 = t1 ptr+ 12
    288     t5 = *t4
    289     t6 = a ptr+ t5
    290     param t6                            (this)
    291     t7 = call *t3, 1                    (virtual Animal::speed())
    292     return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 91 temporaries, frame 484 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   class Dog                      12       0
   p                local   class Puppy                    12      12
   zoo              local   class Animal *[3]              12      24
   s                local   class Seal                     20      36
   i.13             local   int                             4      56
   w                local   class Swimmer *                 4      60
   ref              local   class Animal &                  4      64
   copy             local   class Animal                    8      68
   r                local   class Rect                     12      76
   sq               local   class Square                   12      88
   shapes           local   class Shape *[2]                8     100
   i.20             local   int                             4     108
   t1               temp    class Dog *                     4     112
   t2               temp    class Puppy *                   4     116
   t3               temp    class Dog *                     4     120
   t4               temp    class Puppy *                   4     124
   t5               temp    class Seal *                    4     128
   t6               temp    class Seal *                    4     132
   t7               temp    int                             4     136
   t8               temp    class Animal *                  4     140
   t9               temp    unsigned int *                  4     144
   t10              temp    void *                          4     148
   t11              temp    unsigned int *                  4     152
   t12              temp    int                             4     156
   t13              temp    class Animal *                  4     160
   t14              temp    const char *                    4     164
   t15              temp    int                             4     168
   t16              temp    class Animal *                  4     172
   t17              temp    unsigned int *                  4     176
   t18              temp    unsigned int *                  4     180
   t19              temp    void *                          4     184
   t20              temp    unsigned int *                  4     188
   t21              temp    int                             4     192
   t22              temp    class Animal *                  4     196
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t25              temp    class Animal *                  4     208
   t26              temp    int                             4     212
   t27              temp    int                             4     216
   t28              temp    class Seal *                    4     220
   t29              temp    class Swimmer *                 4     224
   t30              temp    unsigned int *                  4     228
   t31              temp    void *                          4     232
   t32              temp    unsigned int *                  4     236
   t33              temp    int                             4     240
   t34              temp    class Swimmer *                 4     244
   t35              temp    int                             4     248
   t36              temp    unsigned int *                  4     252
   t37              temp    unsigned int *                  4     256
   t38              temp    void *                          4     260
   t39              temp    unsigned int *                  4     264
   t40              temp    int                             4     268
   t41              temp    class Swimmer *                 4     272
   t42              temp    int                             4     276
   t43              temp    class Seal *                    4     280
   t44              temp    int                             4     284
   t45              temp    class Puppy *                   4     288
   t46              temp    unsigned int *                  4     292
   t47              temp    void *                          4     296
   t48              temp    unsigned int *                  4     300
   t49              temp    int                             4     304
   t50              temp    class Animal *                  4     308
   t51              temp    const char *                    4     312
   t52              temp    int                             4     316
   t53              temp    class Dog *                     4     320
   t54              temp    int                             4     324
   t55              temp    class Animal                    8     328
   t56              temp    class Animal *                  4     336
   t57              temp    unsigned int (*)[4]             4     340
   t58              temp    class Animal *                  4     344
   t59              temp    const char *                    4     348
   t60              temp    class Animal *                  4     352
   t61              temp    int                             4     356
   t62              temp    class Animal                    8     360
   t63              temp    class Animal *                  4     368
   t64              temp    unsigned int *                  4     372
   t65              temp    class Animal *                  4     376
   t66              temp    const char *                    4     380
   t67              temp    class Animal *                  4     384
   t68              temp    int                             4     388
   t69              temp    class Rect *                    4     392
   t70              temp    class Square *                  4     396
   t71              temp    class Rect *                    4     400
   t72              temp    class Square *                  4     404
   t73              temp    int                             4     408
   t74              temp    class Shape *                   4     412
   t75              temp    unsigned int *                  4     416
   t76              temp    void *                          4     420
   t77              temp    unsigned int *                  4     424
   t78              temp    int                             4     428
   t79              temp    class Shape *                   4     432
   t80              temp    int                             4     436
   t81              temp    int                             4     440
   t82              temp    class Shape *                   4     444
   t83              temp    int                             4     448
   t84              temp    int                             4     452
   t85              temp    class Shape *                   4     456
   t86              temp    int                             4     460
   t87              temp    int                             4     464
   t88              temp    class Animal *                  4     468
   t89              temp    class Seal *                    4     472
   t90              temp    class Puppy *                   4     476
   t91              temp    class Dog *                     4     480

 Code: 193 instruction(s)

    293       t1 = &d
    294       param t1                            (this)
    295       param 5
    296       call Dog::Dog(int), 2
    297       param "\n"
    298       call printf, 1
    299       t2 = &p
    300       param t2                            (this)
    301       call Puppy::Puppy(), 1
    302       param "\n"
    303       call printf, 1
    304       t3 = &d
    305       t4 = &p
    306       zoo[0] = t3
    307       zoo[4] = t4
    308       zoo[8] = 0
    309       t5 = &s
    310       param t5                            (this)
    311       call Seal::Seal(), 1
    312       t6 = &s
    313       zoo[8] = t6
    314       param "\n"
    315       call printf, 1
    316       i.13 = 0
    317  L1:  if i.13 int< 3 goto L2
    318       goto L3
    319  L2:  t7 = i.13 int* 4                    (w = 4)
    320       t8 = zoo[t7]
    321       t9 = *t8
    322       t10 = *t9
    323       t11 = t9 ptr+ 4
    324       t12 = *t11
    325       t13 = t8 ptr+ t12
    326       param t13                           (this)
    327       t14 = call *t10, 1                  (virtual Animal::name())
    328       t15 = i.13 int* 4                   (w = 4)
    329       t16 = zoo[t15]
    330       t17 = *t16
    331       t18 = t17 ptr+ 8
    332       t19 = *t18
    333       t20 = t17 ptr+ 12
    334       t21 = *t20
    335       t22 = t16 ptr+ t21
    336       param t22                           (this)
    337       t23 = call *t19, 1                  (virtual Animal::speed())
    338       t24 = i.13 int* 4                   (w = 4)
    339       t25 = zoo[t24]
    340       param t25                           (this)
    341       t26 = call Animal::describe(), 1
    342       param "%s %d %d | "
    343       param t14
    344       param t23
    345       param t26
    346       call printf, 4
    347       t27 = i.13 int+ 1
    348       i.13 = t27
    349       goto L1
    350  L3:  param "\n"
    351       call printf, 1
    352       t28 = &s
    353       t29 = t28
    354       if t28 ptr== 0 goto L4
    355       t29 = t28 ptr+ 8
    356  L4:  w = t29
    357       t30 = *w
    358       t31 = *t30
    359       t32 = t30 ptr+ 4
    360       t33 = *t32
    361       t34 = w ptr+ t33
    362       param t34                           (this)
    363       t35 = call *t31, 1                  (virtual Swimmer::swim())
    364       t36 = *w
    365       t37 = t36 ptr+ 8
    366       t38 = *t37
    367       t39 = t36 ptr+ 12
    368       t40 = *t39
    369       t41 = w ptr+ t40
    370       param t41                           (this)
    371       param 2
    372       t42 = call *t38, 2                  (virtual Swimmer::dive(int))
    373       t43 = &s
    374       param t43
    375       t44 = call race(class Animal *), 1
    376       param "%d %d %d\n"
    377       param t35
    378       param t42
    379       param t44
    380       call printf, 4
    381       t45 = &p
    382       ref = t45
    383       t46 = *ref
    384       t47 = *t46
    385       t48 = t46 ptr+ 4
    386       t49 = *t48
    387       t50 = ref ptr+ t49
    388       param t50                           (this)
    389       t51 = call *t47, 1                  (virtual Animal::name())
    390       param ref                           (this)
    391       t52 = call Animal::speed(), 1
    392       t53 = &d
    393       param t53                           (this)
    394       t54 = call Animal::speed(), 1
    395       param "%s %d %d\n"
    396       param t51
    397       param t52
    398       param t54
    399       call printf, 4
    400       t55 = d[0]
    401       copy = t55
    402       t56 = &copy
    403       t57 = &_ZTV6Animal
    404       *t56 = t57
    405       t58 = &copy
    406       param t58                           (this)
    407       t59 = call Animal::name(), 1
    408       t60 = &copy
    409       param t60                           (this)
    410       t61 = call Animal::speed(), 1
    411       param "%s %d\n"
    412       param t59
    413       param t61
    414       call printf, 3
    415       t62 = p[0]
    416       t63 = &copy
    417       t64 = *t63
    418       copy = t62
    419       *t63 = t64
    420       t65 = &copy
    421       param t65                           (this)
    422       t66 = call Animal::name(), 1
    423       t67 = &copy
    424       param t67                           (this)
    425       t68 = call Animal::speed(), 1
    426       param "%s %d\n"
    427       param t66
    428       param t68
    429       call printf, 3
    430       t69 = &r
    431       param t69                           (this)
    432       param 2
    433       param 3
    434       call Rect::Rect(int, int), 3
    435       t70 = &sq
    436       param t70                           (this)
    437       param 4
    438       call Square::Square(int), 2
    439       t71 = &r
    440       t72 = &sq
    441       shapes[0] = t71
    442       shapes[4] = t72
    443       i.20 = 0
    444  L5:  if i.20 int< 2 goto L6
    445       goto L7
    446  L6:  t73 = i.20 int* 4                   (w = 4)
    447       t74 = shapes[t73]
    448       t75 = *t74
    449       t76 = *t75
    450       t77 = t75 ptr+ 4
    451       t78 = *t77
    452       t79 = t74 ptr+ t78
    453       param t79                           (this)
    454       t80 = call *t76, 1                  (virtual Shape::area())
    455       t81 = i.20 int* 4                   (w = 4)
    456       t82 = shapes[t81]
    457       param t82                           (this)
    458       t83 = call Shape::twice(), 1
    459       t84 = i.20 int* 4                   (w = 4)
    460       t85 = shapes[t84]
    461       param t85
    462       t86 = call total(class Shape &), 1
    463       param "%d %d %d | "
    464       param t80
    465       param t83
    466       param t86
    467       call printf, 4
    468       t87 = i.20 int+ 1
    469       i.20 = t87
    470       goto L5
    471  L7:  param "\n"
    472       call printf, 1
    473       t88 = &copy
    474       param t88                           (this)
    475       call Animal::~Animal(), 1
    476       t89 = &s
    477       param t89                           (this)
    478       call Animal::~Animal(), 1
    479       t90 = &p
    480       param t90                           (this)
    481       call Dog::~Dog(), 1
    482       t91 = &d
    483       param t91                           (this)
    484       call Dog::~Dog(), 1
    485       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Animal             class_tag     class Animal               -           6    -    0  size 8
   Dog                class_tag     class Dog                  -          16    -    0  size 12, public base Animal
   Puppy              class_tag     class Puppy                -          25    -    0  size 12, public base Dog
   Swimmer            class_tag     class Swimmer              -          31    -    0  size 8
   Seal               class_tag     class Seal                 -          39    -    0  size 20, public base Animal, public base Swimmer
   Shape              class_tag     class Shape                -          47    -    0  size 4
   Rect               class_tag     class Rect                 -          53    -    0  size 12, public base Shape
   Square             class_tag     class Square               -          60    -    0  size 12, public base Rect
   total              function      int (class Shape &)        -          66    -    1  _Z5totalR5Shape; defined
   race               function      int (class Animal *)       -          67    -    1  _Z4raceP6Animal; defined
   main               function      int (void)                 -          69    -    0  defined

 scope: global > class Animal
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   legs               field         int                        member      8    4    2  Animal::legs; public, offset 4
   Animal             constructor   void (int)                 -           9    -    2  _ZN6AnimalC1Ei; public
   ~Animal            destructor    void (void)                -          10    -    0  _ZN6AnimalD1Ev; public
   name               method        const char *(void) const   -          11    -    6  _ZNK6Animal4nameEv; public, defined
   speed              method        int (void)                 -          12    -    7  _ZN6Animal5speedEv; public, defined
   describe           method        int (void)                 -          13    -    1  _ZN6Animal8describeEv; public, defined

 scope: global > class Animal > Animal()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       9    4    1  n.1

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   bark               field         int                        member     18    4    1  Dog::bark; public, offset 8
   Dog                constructor   void (int)                 -          19    -    2  _ZN3DogC1Ei; public
   ~Dog               destructor    void (void)                -          20    -    0  _ZN3DogD1Ev; public
   name               method        const char *(void) const   -          21    -    2  _ZNK3Dog4nameEv; public, defined
   speed              method        int (void)                 -          22    -    0  _ZN3Dog5speedEv; public, defined

 scope: global > class Dog > Dog()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  parameter     int                        param      19    4    1  b.2

 scope: global > class Puppy
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Puppy              constructor   void (void)                -          27    -    1  _ZN5PuppyC1Ev; public
   name               method        const char *(void) const   -          28    -    0  _ZNK5Puppy4nameEv; public, defined

 scope: global > class Swimmer
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   depth              field         int                        member     33    4    3  Swimmer::depth; public, offset 4
   Swimmer            constructor   void (void)                -          34    -    1  _ZN7SwimmerC1Ev; public
   swim               method        int (void)                 -          35    -    1  _ZN7Swimmer4swimEv; public, defined
   dive               method        int (int)                  -          36    -    1  _ZN7Swimmer4diveEi; public, defined

 scope: global > class Swimmer > dive()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int                        param      36    4    1  m.3

 scope: global > class Seal
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   fat                field         int                        member     41    4    1  Seal::fat; public, offset 16
   Seal               constructor   void (void)                -          42    -    1  _ZN4SealC1Ev; public
   name               method        const char *(void) const   -          43    -    0  _ZNK4Seal4nameEv; public, defined
   swim               method        int (void)                 -          44    -    0  _ZN4Seal4swimEv; public, defined

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   area               method        int (void)                 -          49    -    3  _ZN5Shape4areaEv; public, declared only
   sides              method        int (void)                 -          50    -    1  _ZN5Shape5sidesEv; public, defined
   twice              method        int (void)                 -          51    -    1  _ZN5Shape5twiceEv; public, defined

 scope: global > class Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  field         int                        member     55    4    1  Rect::w; public, offset 4
   h                  field         int                        member     55    4    1  Rect::h; public, offset 8
   Rect               constructor   void (int, int)            -          56    -    2  _ZN4RectC1Eii; public
   area               method        int (void)                 -          57    -    1  _ZN4Rect4areaEv; public, defined
   sides              method        int (void)                 -          58    -    0  _ZN4Rect5sidesEv; public, defined

 scope: global > class Rect > Rect()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      56    4    1  a.4
   b                  parameter     int                        param      56    4    1  b.5

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Square             constructor   void (int)                 -          62    -    1  _ZN6SquareC1Ei; public
   area               method        int (void)                 -          63    -    0  _ZN6Square4areaEv; public, defined

 scope: global > class Square > Square()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     int                        param      62    4    2  s.6

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     class Shape &              param      66    4    2  s.7

 scope: global > race()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     class Animal *             param      67    4    1  a.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      class Dog                  local      70   12    3  d.9
   p                  variable      class Puppy                local      72   12    3  p.10
   zoo                variable      class Animal *[3]          local      74   12    4  zoo.11
   s                  variable      class Seal                 local      75   20    3  s.12
   w                  variable      class Swimmer *            local      80    4    2  w.14
   ref                variable      class Animal &             local      82    4    2  ref.15
   copy               variable      class Animal               local      84    8    5  copy.16
   r                  variable      class Rect                 local      88   12    1  r.17
   sq                 variable      class Square               local      89   12    1  sq.18
   shapes             variable      class Shape *[2]           local      90    8    3  shapes.19

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      78    4    5  i.13
   i                  variable      int                        local      91    4    5  i.20

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Animal: size 8, align 4
    +4  int legs  [public]
class Dog: size 12, align 4
    (base Animal, public)
    +8  int bark  [public]
class Puppy: size 12, align 4
    (base Dog, public)
class Swimmer: size 8, align 4
    +4  int depth  [public]
class Seal: size 20, align 4
    (base Animal, public)
    (base Swimmer, public)
    +16  int fat  [public]
class Shape: size 4, align 4
class Rect: size 12, align 4
    (base Shape, public)
    +4  int w  [public]
    +8  int h  [public]
class Square: size 12, align 4
    (base Rect, public)
