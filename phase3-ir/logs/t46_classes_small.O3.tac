============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t46_classes_small.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 97 -> 88 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           97 -> 88   (9% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                  14
   copies / constants forwarded           47
   temporaries merged away                 1
   dead instructions removed              31
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2
   calls inlined                          10
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           4

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
 FUNCTION Mid::Mid()        (link name _ZN3MidC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0
   t1               temp    unsigned int (*)[1]             4       4
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t7               temp    unsigned int (*)[1]             4      28
   t8               temp    class Base *                    4      32
   (3 temporaries no longer used after optimization not shown)

 Code: 15 instruction(s)

    109     t7 = &_ZTV4Base
    110     *this = t7
    111     t8 = this ptr+ 4
    112     *t8 = 1
    113     Base::made = Base::made int+ 1
    114     param "Base "
    115     call printf, 1
    116     t1 = &_ZTV3Mid
    117     *this = t1
    118     t3 = *t8
    119     t4 = t3 int+ 1
    120     *t8 = t4
    121     param "Mid "
    122     call printf, 1
    123     return

============================================================================
 FUNCTION Mid::who()        (link name _ZN3Mid3whoEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Mid *                     4       0

 Code: 1 instruction(s)

    124     return 2

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
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 25 temporaries, frame 228 bytes

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
   t16              temp    int                             4      92
   t17              temp    class Mid (*)[2]                4      96
   t18              temp    class Mid (*)[2]                4     100
   t23              temp    unsigned int (*)[1]             4     120
   t24              temp    class Leaf *                    4     124
   t25              temp    int                             4     128
   t26              temp    int                             4     132
   t32              temp    int                             4     156
   t33              temp    int                             4     160
   t38              temp    int                             4     180
   t40              temp    unsigned int (*)[1]             4     188
   t41              temp    class Mid *                     4     192
   t42              temp    int                             4     196
   t43              temp    int                             4     200
   t46              temp    class Mid *                     4     212
   t47              temp    int                             4     216
   t48              temp    int                             4     220
   (24 temporaries no longer used after optimization not shown)

 Code: 62 instruction(s)

    126     t1 = &l
    127     param t1                            (this)
    128     call Mid::Mid(), 1
    129     t23 = &_ZTV4Leaf
    130     *t1 = t23
    131     t24 = t1 ptr+ 4
    132     t25 = *t24
    133     t26 = t25 int* 10
    134     *t24 = t26
    135     param "Leaf\n"
    136     call printf, 1
    137     t4 = l[4]
    138     t5 = *t1
    139     t6 = *t5
    140     param t1                            (this)
    141     t7 = call *t6, 1                    (virtual Base::who())
    142     t8 = *t1
    143     t9 = *t8
    144     param t1                            (this)
    145     t10 = call *t9, 1                   (virtual Mid::who())
    146     param "%d %d %d %d %d\n"
    147     param t4
    148     param t7
    149     param t10
    150     param 10
    151     param 20
    152     call printf, 6
    153     t32 = *t24
    154     t33 = t32 int+ 5
    155     *t24 = t33
    156     t38 = t33 int+ 2
    157     *t24 = t38
    158     t16 = l[4]
    159     param "%d\n"
    160     param t16
    161     call printf, 2
    162     t17 = &arr
    163     param t17                           (this)
    164     call Base::Base(), 1
    165     t40 = &_ZTV3Mid
    166     *t17 = t40
    167     t41 = t17 ptr+ 4
    168     t42 = *t41
    169     t43 = t42 int+ 1
    170     *t41 = t43
    171     param "Mid "
    172     call printf, 1
    173     t18 = t17 ptr+ 8
    174     param t18                           (this)
    175     call Base::Base(), 1
    176     *t18 = t40
    177     t46 = t18 ptr+ 4
    178     t47 = *t46
    179     t48 = t47 int+ 1
    180     *t46 = t48
    181     param "Mid "
    182     call printf, 1
    183     param "\n%d %d\n"
    184     param Base::made
    185     param 2
    186     call printf, 3
    187     return 0


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
