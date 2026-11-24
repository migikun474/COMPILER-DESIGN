============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 80 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Base::made       int                             4  0

 As three address code (initial values, in place before main runs):

    Base::made = 0

============================================================================
 FUNCTION Base::Base()        (link name _ZN4BaseC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   t1               temp    int                             4       4

 Code: 6 instruction(s)

    100     *this = 1
    101     t1 = Base::made int+ 1
    102     Base::made = t1
    103     param "Base "
    104     call printf, 1
    105     return

============================================================================
 FUNCTION Base::who()        (link name _ZN4Base3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    106     return 1

============================================================================
 FUNCTION Base::plain()        (link name _ZN4Base5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    107     return 10

============================================================================
 FUNCTION Mid::Mid()        (link name _ZN3MidC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 8 instruction(s)

    108     param this                          (this)
    109     call Base::Base(), 1
    110     t1 = *this
    111     t2 = t1 int+ 1
    112     *this = t2
    113     param "Mid "
    114     call printf, 1
    115     return

============================================================================
 FUNCTION Mid::who()        (link name _ZN3Mid3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    116     return 2

============================================================================
 FUNCTION Mid::plain()        (link name _ZN3Mid5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    117     return 20

============================================================================
 FUNCTION Leaf::Leaf()        (link name _ZN4LeafC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 8 instruction(s)

    118     param this                          (this)
    119     call Mid::Mid(), 1
    120     t1 = *this
    121     t2 = t1 int* 10
    122     *this = t2
    123     param "Leaf\n"
    124     call printf, 1
    125     return

============================================================================
 FUNCTION Leaf::who()        (link name _ZN4Leaf3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0

 Code: 1 instruction(s)

    126     return 3

============================================================================
 FUNCTION Leaf::operator+=(int)        (link name _ZN4LeafpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 4 instruction(s)

    127     t1 = *this
    128     t2 = t1 int+ k
    129     *this = t2
    130     return this

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 17 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                local   class Leaf                      4       0
   b                local   class Base *                    4       4
   m                local   class Mid *                     4       8
   arr              local   class Mid[2]                    8      12
   t1               temp    class Leaf *                    4      20
   t2               temp    class Leaf *                    4      24
   t3               temp    class Leaf *                    4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   t9               temp    class Leaf *                    4      52
   t10              temp    class Leaf &                    4      56
   t11              temp    class Leaf &                    4      60
   t12              temp    int                             4      64
   t13              temp    class Mid (*)[2]                4      68
   t14              temp    class Mid (*)[2]                4      72
   t15              temp    class Mid *                     4      76
   t16              temp    class Mid *                     4      80
   t17              temp    int                             4      84

 Code: 49 instruction(s)

    131     t1 = &l
    132     param t1                            (this)
    133     call Leaf::Leaf(), 1
    134     t2 = &l
    135     b = t2
    136     t3 = &l
    137     m = t3
    138     t4 = l[0]
    139     param b                             (this)
    140     t5 = call Base::who(), 1
    141     param m                             (this)
    142     t6 = call Mid::who(), 1
    143     param b                             (this)
    144     t7 = call Base::plain(), 1
    145     param m                             (this)
    146     t8 = call Mid::plain(), 1
    147     param "%d %d %d %d %d\n"
    148     param t4
    149     param t5
    150     param t6
    151     param t7
    152     param t8
    153     call printf, 6
    154     t9 = &l
    155     param t9                            (this)
    156     param 5
    157     t10 = call Leaf::operator+=(int), 2
    158     param t10                           (this)
    159     param 2
    160     t11 = call Leaf::operator+=(int), 2
    161     t12 = l[0]
    162     param "%d\n"
    163     param t12
    164     call printf, 2
    165     t13 = &arr
    166     param t13                           (this)
    167     call Mid::Mid(), 1
    168     t14 = t13 ptr+ 4
    169     param t14                           (this)
    170     call Mid::Mid(), 1
    171     t15 = &arr
    172     t16 = t15 ptr+ 4
    173     param t16                           (this)
    174     t17 = call Mid::who(), 1
    175     param "\n%d %d\n"
    176     param Base::made
    177     param t17
    178     call printf, 3
    179     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Base               class_tag     class Base                 -           6    -    0  size 4
   Mid                class_tag     class Mid                  -          15    -    0  size 4, public base Base
   Leaf               class_tag     class Leaf                 -          21    -    0  size 4, public base Mid
   main               function      int (void)                 -          27    -    0  defined

 scope: global > class Base
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   made               field         int                        static      8    4    2  Base::made; public, static
   v                  field         int                        member      9    4    9  Base::v; public, offset 0
   Base               constructor   void (void)                -          10    -    0  _ZN4BaseC1Ev; public
   who                method        int (void)                 -          11    -    1  _ZN4Base3whoEv; public, defined
   plain              method        int (void)                 -          12    -    1  _ZN4Base5plainEv; public, defined

 scope: global > class Mid
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Mid                constructor   void (void)                -          17    -    1  _ZN3MidC1Ev; public
   who                method        int (void)                 -          18    -    2  _ZN3Mid3whoEv; public, defined
   plain              method        int (void)                 -          19    -    1  _ZN3Mid5plainEv; public, defined

 scope: global > class Leaf
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Leaf               constructor   void (void)                -          23    -    1  _ZN4LeafC1Ev; public
   who                method        int (void)                 -          24    -    0  _ZN4Leaf3whoEv; public, defined
   operator+=         method        class Leaf &(int)          -          25    -    2  _ZN4LeafpLEi; public, defined

 scope: global > class Leaf > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      25    4    1  k.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   l                  variable      class Leaf                 local      28    4    5  l.2
   b                  variable      class Base *               local      29    4    2  b.3
   m                  variable      class Mid *                local      30    4    2  m.4
   arr                variable      class Mid[2]               local      34    8    1  arr.5

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Base: size 4, align 4
    static  int made  [public]
    +0  int v  [public]
class Mid: size 4, align 4
    (base Base, public)
class Leaf: size 4, align 4
    (base Mid, public)
