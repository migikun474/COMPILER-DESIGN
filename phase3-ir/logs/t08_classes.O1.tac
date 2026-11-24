============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 200 -> 180 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          200 -> 180   (10% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                  14
   copies / constants forwarded           14
   temporaries merged away                 3
   dead instructions removed              16
   jumps removed or redirected             3
   unreachable instructions removed        0

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Vec::made        int                             4  0
   origin           class Vec                       8  0

 As three address code (initial values, in place before main runs):

    Vec::made = 0
    origin[...] = 0                (zero-initialized)

============================================================================
 FUNCTION Part::Part()        (link name _ZN4PartC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Part *                    4       0

 Code: 4 instruction(s)

    100     *this = 7
    101     param "Part "
    102     call printf, 1
    103     return

============================================================================
 FUNCTION Vec::Vec()        (link name _ZN3VecC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    104     *this = 0
    105     t1 = this ptr+ 4
    106     *t1 = 0
    107     Vec::made = Vec::made int+ 1
    108     return

============================================================================
 FUNCTION Vec::operator+(class Vec &)        (link name _ZN3VecplERS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 9 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec &                     4       4
   r                local   class Vec                       8       8
   t1               temp    class Vec *                     4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    class Vec *                     4      32
   t6               temp    int                             4      36
   t7               temp    class Vec *                     4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48

 Code: 14 instruction(s)

    109     t1 = &r
    110     param t1                            (this)
    111     call Vec::Vec(), 1
    112     t2 = *this
    113     t3 = *o
    114     t4 = t2 int+ t3
    115     r[0] = t4
    116     t5 = this ptr+ 4
    117     t6 = *t5
    118     t7 = o ptr+ 4
    119     t8 = *t7
    120     t9 = t6 int+ t8
    121     r[4] = t9
    122     return r

============================================================================
 FUNCTION Vec::operator+=(int)        (link name _ZN3VecpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    class Vec *                     4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    123     t1 = *this
    124     t2 = t1 int+ k
    125     *this = t2
    126     t3 = this ptr+ 4
    127     t4 = *t3
    128     t5 = t4 int+ k
    129     *t3 = t5
    130     return this

============================================================================
 FUNCTION Vec::operator==(class Vec &)        (link name _ZN3VeceqERS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec &                     4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    class Vec *                     4      20
   t5               temp    int                             4      24
   t6               temp    class Vec *                     4      28
   t7               temp    int                             4      32

 Code: 12 instruction(s)

    131       t2 = *this
    132       t3 = *o
    133       if t2 int!= t3 goto L1
    134       t4 = this ptr+ 4
    135       t5 = *t4
    136       t6 = o ptr+ 4
    137       t7 = *t6
    138       if t5 int== t7 goto L2
    139  L1:  t1 = 0
    140       goto L3
    141  L2:  t1 = 1
    142  L3:  return t1

============================================================================
 FUNCTION Vec::operator[](int)        (link name _ZN3VecixEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   i                param   int                             4       4
   t1               temp    int *                           4       8
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    143       if i int!= 0 goto L4
    144       t1 = this
    145       goto L5
    146  L4:  t1 = this ptr+ 4
    147  L5:  return t1

============================================================================
 FUNCTION Vec::operator()(int)        (link name _ZN3VecclEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 3 instruction(s)

    148     t1 = *this
    149     t2 = t1 int* k
    150     return t2

============================================================================
 FUNCTION peek(class Vec &)        (link name _Z4peekR3Vec)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   class Vec &                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    class Vec *                     4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 6 instruction(s)

    151     t1 = *v
    152     t2 = t1 int* 100
    153     t3 = v ptr+ 4
    154     t4 = *t3
    155     t5 = t2 int+ t4
    156     return t5

============================================================================
 FUNCTION Base::Base()        (link name _ZN4BaseC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 4 instruction(s)

    157     *this = 1
    158     param "Base "
    159     call printf, 1
    160     return

============================================================================
 FUNCTION Base::area()        (link name _ZN4Base4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    161     return 10

============================================================================
 FUNCTION Shape::Shape()        (link name _ZN5ShapeC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    class Shape *                   4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 11 instruction(s)

    162     param this                          (this)
    163     call Base::Base(), 1
    164     t1 = this ptr+ 4
    165     param t1                            (this)
    166     call Part::Part(), 1
    167     t2 = *this
    168     t3 = t2 int+ 1
    169     *this = t3
    170     param "Shape\n"
    171     call printf, 1
    172     return

============================================================================
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 5 instruction(s)

    173     param this                          (this)
    174     t1 = call Base::area(), 1
    175     t2 = *this
    176     t3 = t1 int+ t2
    177     return t3

============================================================================
 FUNCTION twice(class Vec)        (link name _Z5twice3Vec)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   class Vec                       8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    178     t1 = v[0]
    179     t2 = t1 int<< 1
    180     v[0] = t2
    181     return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 29 temporaries, frame 248 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                local   class Shape                     8       0
   a                local   class Vec                       8       8
   b                local   class Vec                       8      16
   c                local   class Vec                       8      24
   pl               local   class Plain                     8      32
   many             local   class Vec[3]                   24      40
   t1               temp    class Vec *                     4      64
   t2               temp    class Shape *                   4      68
   t4               temp    int                             4      76
   t5               temp    int                             4      80
   t6               temp    int                             4      84
   t7               temp    class Vec *                     4      88
   t8               temp    class Vec *                     4      92
   t14              temp    class Vec *                     4     120
   t15              temp    int &                           4     124
   t16              temp    int                             4     128
   t18              temp    int &                           4     136
   t19              temp    int                             4     140
   t22              temp    int                             4     152
   t24              temp    int                             4     160
   t25              temp    int                             4     164
   t26              temp    int                             4     168
   t28              temp    int &                           4     176
   t29              temp    class Plain *                   4     180
   t30              temp    int                             4     184
   t32              temp    int                             4     192
   t33              temp    class Vec                       8     196
   t34              temp    class Vec *                     4     204
   t35              temp    int                             4     208
   t36              temp    int                             4     212
   t37              temp    class Vec (*)[3]                4     216
   t38              temp    class Vec (*)[3]                4     220
   t39              temp    class Vec (*)[3]                4     224
   t43              temp    int                             4     240
   t44              temp    int                             4     244
   (15 temporaries no longer used after optimization not shown)

 Code: 98 instruction(s)

    182     t1 = &origin
    183     param t1                            (this)
    184     call Vec::Vec(), 1
    185     t2 = &s
    186     param t2                            (this)
    187     call Shape::Shape(), 1
    188     param t2                            (this)
    189     t4 = call Shape::area(), 1
    190     t5 = s[4]
    191     t6 = s[0]
    192     param "%d %d %d\n"
    193     param t4
    194     param t5
    195     param t6
    196     call printf, 4
    197     t7 = &a
    198     param t7                            (this)
    199     call Vec::Vec(), 1
    200     t8 = &b
    201     param t8                            (this)
    202     call Vec::Vec(), 1
    203     param t7                            (this)
    204     param 3
    205     call Vec::operator+=(int), 2
    206     b[0] = 1
    207     b[4] = 2
    208     param t7                            (this)
    209     param t8
    210     c = call Vec::operator+(class Vec &), 2
    211     t14 = &c
    212     param t14                           (this)
    213     param 0
    214     t15 = call Vec::operator[](int), 2
    215     t16 = *t15
    216     param t14                           (this)
    217     param 1
    218     t18 = call Vec::operator[](int), 2
    219     t19 = *t18
    220     param t14                           (this)
    221     param t7
    222     t22 = call Vec::operator==(class Vec &), 2
    223     param t14
    224     t24 = call peek(class Vec &), 1
    225     param "%d %d %d %d\n"
    226     param t16
    227     param t19
    228     param t22
    229     param t24
    230     call printf, 5
    231     param c
    232     t25 = call twice(class Vec), 1
    233     t26 = c[0]
    234     param "%d %d\n"
    235     param t25
    236     param t26
    237     call printf, 3
    238     param t14                           (this)
    239     param 1
    240     t28 = call Vec::operator[](int), 2
    241     *t28 = 9
    242     t29 = &pl
    243     param t29                           (this)
    244     call Base::Base(), 1
    245     t30 = c[4]
    246     param t14                           (this)
    247     param 3
    248     t32 = call Vec::operator()(int), 2
    249     t34 = &t33
    250     param t34                           (this)
    251     call Vec::Vec(), 1
    252     t35 = t33[0]
    253     t36 = pl[0]
    254     param "%d %d %d %d\n"
    255     param t30
    256     param t32
    257     param t35
    258     param t36
    259     call printf, 5
    260     t37 = &many
    261     param t37                           (this)
    262     call Vec::Vec(), 1
    263     t38 = t37 ptr+ 8
    264     param t38                           (this)
    265     call Vec::Vec(), 1
    266     t39 = t37 ptr+ 16
    267     param t39                           (this)
    268     call Vec::Vec(), 1
    269     param t39                           (this)
    270     param 5
    271     call Vec::operator+=(int), 2
    272     t43 = many[20]
    273     t44 = origin[0]
    274     param "%d %d %d\n"
    275     param t43
    276     param Vec::made
    277     param t44
    278     call printf, 4
    279     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Part               class_tag     class Part                 -           6    -    0  size 4
   Vec                class_tag     class Vec                  -           7    -    0  size 8
   peek               function      int (class Vec &)          -          17    -    1  _Z4peekR3Vec; defined
   Base               class_tag     class Base                 -          21    -    0  size 4
   Plain              class_tag     class Plain                -          22    -    0  size 8, public base Base
   Shape              class_tag     class Shape                -          23    -    0  size 8, public base Base
   origin             variable      class Vec                  global     29    8    1  
   twice              function      int (class Vec)            -          30    -    1  _Z5twice3Vec; defined
   main               function      int (void)                 -          31    -    0  defined

 scope: global > class Part
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      6    4    2  Part::id; public, offset 0
   Part               constructor   void (void)                -           6    -    0  _ZN4PartC1Ev; public

 scope: global > class Vec
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      9    4   17  Vec::x; public, offset 0
   y                  field         int                        member      9    4   12  Vec::y; public, offset 4
   made               field         int                        static     10    4    2  Vec::made; public, static
   Vec                constructor   void (void)                -          11    -    6  _ZN3VecC1Ev; public
   operator+          method        class Vec (class Vec &)    -          12    -    1  _ZN3VecplERS_; public, defined
   operator+=         method        class Vec &(int)           -          13    -    2  _ZN3VecpLEi; public, defined
   operator==         method        int (class Vec &)          -          14    -    1  _ZN3VeceqERS_; public, defined
   operator[]         method        int &(int)                 -          15    -    3  _ZN3VecixEi; public, defined
   operator()         method        int (int)                  -          16    -    1  _ZN3VecclEi; public, defined

 scope: global > class Vec > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec &                param      12    4    2  o.1
   r                  variable      class Vec                  local      12    8    3  r.2

 scope: global > class Vec > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      13    4    2  k.3

 scope: global > class Vec > operator==()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec &                param      14    4    2  o.4

 scope: global > class Vec > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      15    4    1  i.5

 scope: global > class Vec > operator()()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      16    4    1  k.6

 scope: global > peek()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     class Vec &                param      20    4    2  v.7

 scope: global > class Base
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  field         int                        member     21    4    6  Base::b; public, offset 0
   Base               constructor   void (void)                -          21    -    0  _ZN4BaseC1Ev; public
   area               method        int (void)                 -          21    -    1  _ZN4Base4areaEv; public, defined

 scope: global > class Plain
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   extra              field         int                        member     22    4    0  Plain::extra; public, offset 4

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  field         class Part                 member     25    4    1  Shape::p; public, offset 4
   Shape              constructor   void (void)                -          26    -    1  _ZN5ShapeC1Ev; public
   area               method        int (void)                 -          27    -    1  _ZN5Shape4areaEv; public, defined

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     class Vec                  param      30    8    3  v.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  variable      class Shape                local      32    8    3  s.9
   a                  variable      class Vec                  local      34    8    3  a.10
   b                  variable      class Vec                  local      34    8    3  b.11
   c                  variable      class Vec                  local      37    8    9  c.12
   pl                 variable      class Plain                local      41    8    1  pl.13
   many               variable      class Vec[3]               local      43   24    2  many.14

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Part: size 4, align 4
    +0  int id  [public]
class Vec: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
    static  int made  [public]
class Base: size 4, align 4
    +0  int b  [public]
class Plain: size 8, align 4
    (base Base, public)
    +4  int extra  [public]
class Shape: size 8, align 4
    (base Base, public)
    +4  class Part p  [public]
