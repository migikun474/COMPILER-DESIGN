============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 80 -> 61 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           80 -> 61   (23% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   6
   copies / constants forwarded           36
   temporaries merged away                 1
   dead instructions removed              27
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2
   calls inlined                          12
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           7

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

    105     *this = 1
    106     Base::made = Base::made int+ 1
    107     param "Base "
    108     call printf, 1
    109     t1 = *this
    110     t2 = t1 int+ 1
    111     *this = t2
    112     param "Mid "
    113     call printf, 1
    114     return

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

 Code: 46 instruction(s)

    115     t1 = &l
    116     param t1                            (this)
    117     call Mid::Mid(), 1
    118     t19 = *t1
    119     t20 = t19 int* 10
    120     *t1 = t20
    121     param "Leaf\n"
    122     call printf, 1
    123     t4 = l[0]
    124     param "%d %d %d %d %d\n"
    125     param t4
    126     param 1
    127     param 2
    128     param 10
    129     param 20
    130     call printf, 6
    131     t27 = *t1
    132     t28 = t27 int+ 5
    133     *t1 = t28
    134     t32 = t28 int+ 2
    135     *t1 = t32
    136     t12 = l[0]
    137     param "%d\n"
    138     param t12
    139     call printf, 2
    140     t13 = &arr
    141     param t13                           (this)
    142     call Base::Base(), 1
    143     t34 = *t13
    144     t35 = t34 int+ 1
    145     *t13 = t35
    146     param "Mid "
    147     call printf, 1
    148     t14 = t13 ptr+ 4
    149     param t14                           (this)
    150     call Base::Base(), 1
    151     t37 = *t14
    152     t38 = t37 int+ 1
    153     *t14 = t38
    154     param "Mid "
    155     call printf, 1
    156     param "\n%d %d\n"
    157     param Base::made
    158     param 2
    159     call printf, 3
    160     return 0


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
