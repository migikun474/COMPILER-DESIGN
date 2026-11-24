============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 97 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 4 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Base::made       int                             4  0
   _ZTV4Base        unsigned int[1]                 4  { +0: &Base::who() }
   _ZTV3Mid         unsigned int[1]                 4  { +0: &Mid::who() }
   _ZTV4Leaf        unsigned int[1]                 4  { +0: &Leaf::who() }

 As three address code (initial values, in place before main runs):

    Base::made = 0
    _ZTV4Base[0] = &Base::who()
    _ZTV3Mid[0] = &Mid::who()
    _ZTV4Leaf[0] = &Leaf::who()

============================================================================
 FUNCTION Base::Base()        (link name _ZN4BaseC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   t1               temp    unsigned int (*)[1]             4       4
   t2               temp    class Base *                    4       8
   t3               temp    int                             4      12

 Code: 9 instruction(s)

    100     t1 = &_ZTV4Base
    101     *this = t1
    102     t2 = this ptr+ 4
    103     *t2 = 1
    104     t3 = Base::made int+ 1
    105     Base::made = t3
    106     param "Base "
    107     call printf, 1
    108     return

============================================================================
 FUNCTION Base::who()        (link name _ZN4Base3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    109     return 1

============================================================================
 FUNCTION Base::plain()        (link name _ZN4Base5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    110     return 10

============================================================================
 FUNCTION Mid::Mid()        (link name _ZN3MidC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0
   t1               temp    unsigned int (*)[1]             4       4
   t2               temp    class Mid *                     4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    class Mid *                     4      20

 Code: 12 instruction(s)

    111     param this                          (this)
    112     call Base::Base(), 1
    113     t1 = &_ZTV3Mid
    114     *this = t1
    115     t2 = this ptr+ 4
    116     t3 = *t2
    117     t4 = t3 int+ 1
    118     t5 = this ptr+ 4
    119     *t5 = t4
    120     param "Mid "
    121     call printf, 1
    122     return

============================================================================
 FUNCTION Mid::who()        (link name _ZN3Mid3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    123     return 2

============================================================================
 FUNCTION Mid::plain()        (link name _ZN3Mid5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    124     return 20

============================================================================
 FUNCTION Leaf::Leaf()        (link name _ZN4LeafC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   t1               temp    unsigned int (*)[1]             4       4
   t2               temp    class Leaf *                    4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    class Leaf *                    4      20

 Code: 12 instruction(s)

    125     param this                          (this)
    126     call Mid::Mid(), 1
    127     t1 = &_ZTV4Leaf
    128     *this = t1
    129     t2 = this ptr+ 4
    130     t3 = *t2
    131     t4 = t3 int* 10
    132     t5 = this ptr+ 4
    133     *t5 = t4
    134     param "Leaf\n"
    135     call printf, 1
    136     return

============================================================================
 FUNCTION Leaf::who()        (link name _ZN4Leaf3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0

 Code: 1 instruction(s)

    137     return 3

============================================================================
 FUNCTION Leaf::operator+=(int)        (link name _ZN4LeafpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   k                param   int                             4       4
   t1               temp    class Leaf *                    4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    class Leaf *                    4      20

 Code: 6 instruction(s)

    138     t1 = this ptr+ 4
    139     t2 = *t1
    140     t3 = t2 int+ k
    141     t4 = this ptr+ 4
    142     *t4 = t3
    143     return this

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 21 temporaries, frame 116 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                local   class Leaf                      8       0
   b                local   class Base *                    4       8
   m                local   class Mid *                     4      12
   arr              local   class Mid[2]                   16      16
   t1               temp    class Leaf *                    4      32
   t2               temp    class Leaf *                    4      36
   t3               temp    class Leaf *                    4      40
   t4               temp    int                             4      44
   t5               temp    unsigned int                    4      48
   t6               temp    unsigned int                    4      52
   t7               temp    int                             4      56
   t8               temp    unsigned int                    4      60
   t9               temp    unsigned int                    4      64
   t10              temp    int                             4      68
   t11              temp    int                             4      72
   t12              temp    int                             4      76
   t13              temp    class Leaf *                    4      80
   t14              temp    class Leaf &                    4      84
   t15              temp    class Leaf &                    4      88
   t16              temp    int                             4      92
   t17              temp    class Mid (*)[2]                4      96
   t18              temp    class Mid (*)[2]                4     100
   t19              temp    class Mid *                     4     104
   t20              temp    class Mid *                     4     108
   t21              temp    int                             4     112

 Code: 53 instruction(s)

    144     t1 = &l
    145     param t1                            (this)
    146     call Leaf::Leaf(), 1
    147     t2 = &l
    148     b = t2
    149     t3 = &l
    150     m = t3
    151     t4 = l[4]
    152     t5 = *b
    153     t6 = *t5
    154     param b                             (this)
    155     t7 = call *t6, 1                    (virtual Base::who())
    156     t8 = *m
    157     t9 = *t8
    158     param m                             (this)
    159     t10 = call *t9, 1                   (virtual Mid::who())
    160     param b                             (this)
    161     t11 = call Base::plain(), 1
    162     param m                             (this)
    163     t12 = call Mid::plain(), 1
    164     param "%d %d %d %d %d\n"
    165     param t4
    166     param t7
    167     param t10
    168     param t11
    169     param t12
    170     call printf, 6
    171     t13 = &l
    172     param t13                           (this)
    173     param 5
    174     t14 = call Leaf::operator+=(int), 2
    175     param t14                           (this)
    176     param 2
    177     t15 = call Leaf::operator+=(int), 2
    178     t16 = l[4]
    179     param "%d\n"
    180     param t16
    181     call printf, 2
    182     t17 = &arr
    183     param t17                           (this)
    184     call Mid::Mid(), 1
    185     t18 = t17 ptr+ 8
    186     param t18                           (this)
    187     call Mid::Mid(), 1
    188     t19 = &arr
    189     t20 = t19 ptr+ 8
    190     param t20                           (this)
    191     t21 = call Mid::who(), 1
    192     param "\n%d %d\n"
    193     param Base::made
    194     param t21
    195     call printf, 3
    196     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Base               class_tag     class Base                 -           5    -    0  size 8
   Mid                class_tag     class Mid                  -          14    -    0  size 8, public base Base
   Leaf               class_tag     class Leaf                 -          20    -    0  size 8, public base Mid
   main               function      int (void)                 -          26    -    0  defined

 scope: global > class Base
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   made               field         int                        static      7    4    2  Base::made; public, static
   v                  field         int                        member      8    4    9  Base::v; public, offset 4
   Base               constructor   void (void)                -           9    -    0  _ZN4BaseC1Ev; public
   who                method        int (void)                 -          10    -    1  _ZN4Base3whoEv; public, virtual, slot 0, defined
   plain              method        int (void)                 -          11    -    1  _ZN4Base5plainEv; public, defined

 scope: global > class Mid
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Mid                constructor   void (void)                -          16    -    1  _ZN3MidC1Ev; public
   who                method        int (void)                 -          17    -    2  _ZN3Mid3whoEv; public, virtual, slot 0, defined
   plain              method        int (void)                 -          18    -    1  _ZN3Mid5plainEv; public, defined

 scope: global > class Leaf
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Leaf               constructor   void (void)                -          22    -    1  _ZN4LeafC1Ev; public
   who                method        int (void)                 -          23    -    0  _ZN4Leaf3whoEv; public, virtual, slot 0, defined
   operator+=         method        class Leaf &(int)          -          24    -    2  _ZN4LeafpLEi; public, defined

 scope: global > class Leaf > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      24    4    1  k.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   l                  variable      class Leaf                 local      27    8    5  l.2
   b                  variable      class Base *               local      28    4    2  b.3
   m                  variable      class Mid *                local      29    4    2  m.4
   arr                variable      class Mid[2]               local      33   16    1  arr.5

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Base: size 8, align 4
    +0  vtable pointer
    slot 0: Base::who
    static  int made  [public]
    +4  int v  [public]
class Mid: size 8, align 4
    (base Base, public)
    slot 0: Mid::who
class Leaf: size 8, align 4
    (base Mid, public)
    slot 0: Leaf::who
