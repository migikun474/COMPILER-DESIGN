============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 97 -> 86 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           97 -> 86   (11% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   8
   copies / constants forwarded           14
   temporaries merged away                 1
   dead instructions removed               9
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   t1               temp    unsigned int (*)[1]             4       4
   t2               temp    class Base *                    4       8
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    100     t1 = &_ZTV4Base
    101     *this = t1
    102     t2 = this ptr+ 4
    103     *t2 = 1
    104     Base::made = Base::made int+ 1
    105     param "Base "
    106     call printf, 1
    107     return

============================================================================
 FUNCTION Base::who()        (link name _ZN4Base3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    108     return 1

============================================================================
 FUNCTION Base::plain()        (link name _ZN4Base5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    109     return 10

============================================================================
 FUNCTION Mid::Mid()        (link name _ZN3MidC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0
   t1               temp    unsigned int (*)[1]             4       4
   t2               temp    class Mid *                     4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    110     param this                          (this)
    111     call Base::Base(), 1
    112     t1 = &_ZTV3Mid
    113     *this = t1
    114     t2 = this ptr+ 4
    115     t3 = *t2
    116     t4 = t3 int+ 1
    117     *t2 = t4
    118     param "Mid "
    119     call printf, 1
    120     return

============================================================================
 FUNCTION Mid::who()        (link name _ZN3Mid3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    121     return 2

============================================================================
 FUNCTION Mid::plain()        (link name _ZN3Mid5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    122     return 20

============================================================================
 FUNCTION Leaf::Leaf()        (link name _ZN4LeafC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   t1               temp    unsigned int (*)[1]             4       4
   t2               temp    class Leaf *                    4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    123     param this                          (this)
    124     call Mid::Mid(), 1
    125     t1 = &_ZTV4Leaf
    126     *this = t1
    127     t2 = this ptr+ 4
    128     t3 = *t2
    129     t4 = t3 int* 10
    130     *t2 = t4
    131     param "Leaf\n"
    132     call printf, 1
    133     return

============================================================================
 FUNCTION Leaf::who()        (link name _ZN4Leaf3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0

 Code: 1 instruction(s)

    134     return 3

============================================================================
 FUNCTION Leaf::operator+=(int)        (link name _ZN4LeafpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   k                param   int                             4       4
   t1               temp    class Leaf *                    4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    135     t1 = this ptr+ 4
    136     t2 = *t1
    137     t3 = t2 int+ k
    138     *t1 = t3
    139     return this

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 15 temporaries, frame 116 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                local   class Leaf                      8       0
   b                local   class Base *                    4       8
   m                local   class Mid *                     4      12
   arr              local   class Mid[2]                   16      16
   t1               temp    class Leaf *                    4      32
   t4               temp    int                             4      44
   t5               temp    unsigned int                    4      48
   t6               temp    unsigned int                    4      52
   t7               temp    int                             4      56
   t8               temp    unsigned int                    4      60
   t9               temp    unsigned int                    4      64
   t10              temp    int                             4      68
   t11              temp    int                             4      72
   t12              temp    int                             4      76
   t14              temp    class Leaf &                    4      84
   t16              temp    int                             4      92
   t17              temp    class Mid (*)[2]                4      96
   t18              temp    class Mid (*)[2]                4     100
   t21              temp    int                             4     112
   (6 temporaries no longer used after optimization not shown)

 Code: 46 instruction(s)

    140     t1 = &l
    141     param t1                            (this)
    142     call Leaf::Leaf(), 1
    143     t4 = l[4]
    144     t5 = *t1
    145     t6 = *t5
    146     param t1                            (this)
    147     t7 = call *t6, 1                    (virtual Base::who())
    148     t8 = *t1
    149     t9 = *t8
    150     param t1                            (this)
    151     t10 = call *t9, 1                   (virtual Mid::who())
    152     param t1                            (this)
    153     t11 = call Base::plain(), 1
    154     param t1                            (this)
    155     t12 = call Mid::plain(), 1
    156     param "%d %d %d %d %d\n"
    157     param t4
    158     param t7
    159     param t10
    160     param t11
    161     param t12
    162     call printf, 6
    163     param t1                            (this)
    164     param 5
    165     t14 = call Leaf::operator+=(int), 2
    166     param t14                           (this)
    167     param 2
    168     call Leaf::operator+=(int), 2
    169     t16 = l[4]
    170     param "%d\n"
    171     param t16
    172     call printf, 2
    173     t17 = &arr
    174     param t17                           (this)
    175     call Mid::Mid(), 1
    176     t18 = t17 ptr+ 8
    177     param t18                           (this)
    178     call Mid::Mid(), 1
    179     param t18                           (this)
    180     t21 = call Mid::who(), 1
    181     param "\n%d %d\n"
    182     param Base::made
    183     param t21
    184     call printf, 3
    185     return 0


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
