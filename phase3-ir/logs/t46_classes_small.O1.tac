============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 80 -> 85 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           80 -> 85   (-6% fewer)

   calls inlined                          12
   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   6
   copies / constants forwarded           36
   temporaries merged away                 1
   dead instructions removed              27
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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   (1 temporary no longer used after optimization not shown)

 Code: 10 instruction(s)

    107     *this = 1
    108     Base::made = Base::made int+ 1
    109     param "Base "
    110     call printf, 1
    111     t1 = *this
    112     t2 = t1 int+ 1
    113     *this = t2
    114     param "Mid "
    115     call printf, 1
    116     return

============================================================================
 FUNCTION Mid::who()        (link name _ZN3Mid3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    117     return 2

============================================================================
 FUNCTION Mid::plain()        (link name _ZN3Mid5plainEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    118     return 20

============================================================================
 FUNCTION Leaf::Leaf()        (link name _ZN4LeafC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   (1 temporary no longer used after optimization not shown)

 Code: 13 instruction(s)

    119     param this                          (this)
    120     call Base::Base(), 1
    121     t4 = *this
    122     t5 = t4 int+ 1
    123     *this = t5
    124     param "Mid "
    125     call printf, 1
    126     t1 = *this
    127     t2 = t1 int* 10
    128     *this = t2
    129     param "Leaf\n"
    130     call printf, 1
    131     return

============================================================================
 FUNCTION Leaf::who()        (link name _ZN4Leaf3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Leaf *                    4       0

 Code: 1 instruction(s)

    132     return 3

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

    133     t1 = *this
    134     t2 = t1 int+ k
    135     *this = t2
    136     return this

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 14 temporaries, frame 176 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                local   class Leaf                      4       0
   b                local   class Base *                    4       4
   m                local   class Mid *                     4       8
   arr              local   class Mid[2]                    8      12
   t1               temp    class Leaf *                    4      20
   t4               temp    int                             4      32
   t12              temp    int                             4      64
   t13              temp    class Mid (*)[2]                4      68
   t14              temp    class Mid (*)[2]                4      72
   t19              temp    int                             4      92
   t20              temp    int                             4      96
   t27              temp    int                             4     124
   t28              temp    int                             4     128
   t32              temp    int                             4     144
   t34              temp    int                             4     152
   t35              temp    int                             4     156
   t37              temp    int                             4     164
   t38              temp    int                             4     168
   (25 temporaries no longer used after optimization not shown)

 Code: 48 instruction(s)

    137     t1 = &l
    138     param t1                            (this)
    139     call Mid::Mid(), 1
    140     t19 = *t1
    141     t20 = t19 int* 10
    142     *t1 = t20
    143     param "Leaf\n"
    144     call printf, 1
    145     b = t1
    146     m = t1
    147     t4 = l[0]
    148     param "%d %d %d %d %d\n"
    149     param t4
    150     param 1
    151     param 2
    152     param 10
    153     param 20
    154     call printf, 6
    155     t27 = *t1
    156     t28 = t27 int+ 5
    157     *t1 = t28
    158     t32 = t28 int+ 2
    159     *t1 = t32
    160     t12 = l[0]
    161     param "%d\n"
    162     param t12
    163     call printf, 2
    164     t13 = &arr
    165     param t13                           (this)
    166     call Base::Base(), 1
    167     t34 = *t13
    168     t35 = t34 int+ 1
    169     *t13 = t35
    170     param "Mid "
    171     call printf, 1
    172     t14 = t13 ptr+ 4
    173     param t14                           (this)
    174     call Base::Base(), 1
    175     t37 = *t14
    176     t38 = t37 int+ 1
    177     *t14 = t38
    178     param "Mid "
    179     call printf, 1
    180     param "\n%d %d\n"
    181     param Base::made
    182     param 2
    183     call printf, 3
    184     return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

Base Mid Leaf
20 1 2 10 20
27
Base Mid Base Mid 
3 2

   exit code 0, 68 instructions executed
