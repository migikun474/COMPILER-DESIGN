============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 80 -> 74 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           80 -> 74   (7% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   5
   copies / constants forwarded            9
   temporaries merged away                 1
   dead instructions removed               6
   jumps removed or redirected             0
   unreachable instructions removed        0

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

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    100     *this = 1
    101     Base::made = Base::made int+ 1
    102     param "Base "
    103     call printf, 1
    104     return

============================================================================
 FUNCTION Base::who()        (link name _ZN4Base3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    105     return 1

============================================================================
 FUNCTION Base::plain()        (link name _ZN4Base5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    106     return 10

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

    107     param this                          (this)
    108     call Base::Base(), 1
    109     t1 = *this
    110     t2 = t1 int+ 1
    111     *this = t2
    112     param "Mid "
    113     call printf, 1
    114     return

============================================================================
 FUNCTION Mid::who()        (link name _ZN3Mid3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    115     return 2

============================================================================
 FUNCTION Mid::plain()        (link name _ZN3Mid5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    116     return 20

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

    117     param this                          (this)
    118     call Mid::Mid(), 1
    119     t1 = *this
    120     t2 = t1 int* 10
    121     *this = t2
    122     param "Leaf\n"
    123     call printf, 1
    124     return

============================================================================
 FUNCTION Leaf::who()        (link name _ZN4Leaf3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0

 Code: 1 instruction(s)

    125     return 3

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

    126     t1 = *this
    127     t2 = t1 int+ k
    128     *this = t2
    129     return this

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 11 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                local   class Leaf                      4       0
   b                local   class Base *                    4       4
   m                local   class Mid *                     4       8
   arr              local   class Mid[2]                    8      12
   t1               temp    class Leaf *                    4      20
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   t10              temp    class Leaf &                    4      56
   t12              temp    int                             4      64
   t13              temp    class Mid (*)[2]                4      68
   t14              temp    class Mid (*)[2]                4      72
   t17              temp    int                             4      84
   (6 temporaries no longer used after optimization not shown)

 Code: 44 instruction(s)

    130     t1 = &l
    131     param t1                            (this)
    132     call Leaf::Leaf(), 1
    133     b = t1
    134     m = t1
    135     t4 = l[0]
    136     param t1                            (this)
    137     t5 = call Base::who(), 1
    138     param t1                            (this)
    139     t6 = call Mid::who(), 1
    140     param t1                            (this)
    141     t7 = call Base::plain(), 1
    142     param t1                            (this)
    143     t8 = call Mid::plain(), 1
    144     param "%d %d %d %d %d\n"
    145     param t4
    146     param t5
    147     param t6
    148     param t7
    149     param t8
    150     call printf, 6
    151     param t1                            (this)
    152     param 5
    153     t10 = call Leaf::operator+=(int), 2
    154     param t10                           (this)
    155     param 2
    156     call Leaf::operator+=(int), 2
    157     t12 = l[0]
    158     param "%d\n"
    159     param t12
    160     call printf, 2
    161     t13 = &arr
    162     param t13                           (this)
    163     call Mid::Mid(), 1
    164     t14 = t13 ptr+ 4
    165     param t14                           (this)
    166     call Mid::Mid(), 1
    167     param t14                           (this)
    168     t17 = call Mid::who(), 1
    169     param "\n%d %d\n"
    170     param Base::made
    171     param t17
    172     call printf, 3
    173     return 0


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
