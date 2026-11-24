============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : no optimization
   Result        : Three address code generated: 14 function(s), 200 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4
   t2               temp    int                             4       8

 Code: 6 instruction(s)

    104     *this = 0
    105     t1 = this ptr+ 4
    106     *t1 = 0
    107     t2 = Vec::made int+ 1
    108     Vec::made = t2
    109     return

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

    110     t1 = &r
    111     param t1                            (this)
    112     call Vec::Vec(), 1
    113     t2 = *this
    114     t3 = *o
    115     t4 = t2 int+ t3
    116     r[0] = t4
    117     t5 = this ptr+ 4
    118     t6 = *t5
    119     t7 = o ptr+ 4
    120     t8 = *t7
    121     t9 = t6 int+ t8
    122     r[4] = t9
    123     return r

============================================================================
 FUNCTION Vec::operator+=(int)        (link name _ZN3VecpLEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    class Vec *                     4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   t6               temp    class Vec *                     4      28

 Code: 9 instruction(s)

    124     t1 = *this
    125     t2 = t1 int+ k
    126     *this = t2
    127     t3 = this ptr+ 4
    128     t4 = *t3
    129     t5 = t4 int+ k
    130     t6 = this ptr+ 4
    131     *t6 = t5
    132     return this

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

 Code: 14 instruction(s)

    133       t2 = *this
    134       t3 = *o
    135       if t2 int== t3 goto L1
    136       goto L2
    137  L1:  t4 = this ptr+ 4
    138       t5 = *t4
    139       t6 = o ptr+ 4
    140       t7 = *t6
    141       if t5 int== t7 goto L3
    142       goto L2
    143  L2:  t1 = 0
    144       goto L4
    145  L3:  t1 = 1
    146  L4:  return t1

============================================================================
 FUNCTION Vec::operator[](int)        (link name _ZN3VecixEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   i                param   int                             4       4
   t1               temp    int *                           4       8
   t2               temp    class Vec *                     4      12

 Code: 7 instruction(s)

    147       if i int== 0 goto L5
    148       goto L6
    149  L5:  t1 = this
    150       goto L7
    151  L6:  t2 = this ptr+ 4
    152       t1 = t2
    153  L7:  return t1

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

    154     t1 = *this
    155     t2 = t1 int* k
    156     return t2

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

    157     t1 = *v
    158     t2 = t1 int* 100
    159     t3 = v ptr+ 4
    160     t4 = *t3
    161     t5 = t2 int+ t4
    162     return t5

============================================================================
 FUNCTION Base::Base()        (link name _ZN4BaseC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 4 instruction(s)

    163     *this = 1
    164     param "Base "
    165     call printf, 1
    166     return

============================================================================
 FUNCTION Base::area()        (link name _ZN4Base4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    167     return 10

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

    168     param this                          (this)
    169     call Base::Base(), 1
    170     t1 = this ptr+ 4
    171     param t1                            (this)
    172     call Part::Part(), 1
    173     t2 = *this
    174     t3 = t2 int+ 1
    175     *this = t3
    176     param "Shape\n"
    177     call printf, 1
    178     return

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

    179     param this                          (this)
    180     t1 = call Base::area(), 1
    181     t2 = *this
    182     t3 = t1 int+ t2
    183     return t3

============================================================================
 FUNCTION twice(class Vec)        (link name _Z5twice3Vec)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   class Vec                       8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 5 instruction(s)

    184     t1 = v[0]
    185     t2 = t1 int* 2
    186     v[0] = t2
    187     t3 = v[0]
    188     return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 44 temporaries, frame 248 bytes

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
   t3               temp    class Shape *                   4      72
   t4               temp    int                             4      76
   t5               temp    int                             4      80
   t6               temp    int                             4      84
   t7               temp    class Vec *                     4      88
   t8               temp    class Vec *                     4      92
   t9               temp    class Vec *                     4      96
   t10              temp    class Vec &                     4     100
   t11              temp    class Vec *                     4     104
   t12              temp    class Vec *                     4     108
   t13              temp    class Vec                       8     112
   t14              temp    class Vec *                     4     120
   t15              temp    int &                           4     124
   t16              temp    int                             4     128
   t17              temp    class Vec *                     4     132
   t18              temp    int &                           4     136
   t19              temp    int                             4     140
   t20              temp    class Vec *                     4     144
   t21              temp    class Vec *                     4     148
   t22              temp    int                             4     152
   t23              temp    class Vec *                     4     156
   t24              temp    int                             4     160
   t25              temp    int                             4     164
   t26              temp    int                             4     168
   t27              temp    class Vec *                     4     172
   t28              temp    int &                           4     176
   t29              temp    class Plain *                   4     180
   t30              temp    int                             4     184
   t31              temp    class Vec *                     4     188
   t32              temp    int                             4     192
   t33              temp    class Vec                       8     196
   t34              temp    class Vec *                     4     204
   t35              temp    int                             4     208
   t36              temp    int                             4     212
   t37              temp    class Vec (*)[3]                4     216
   t38              temp    class Vec (*)[3]                4     220
   t39              temp    class Vec (*)[3]                4     224
   t40              temp    class Vec *                     4     228
   t41              temp    class Vec *                     4     232
   t42              temp    class Vec &                     4     236
   t43              temp    int                             4     240
   t44              temp    int                             4     244

 Code: 111 instruction(s)

    189     t1 = &origin
    190     param t1                            (this)
    191     call Vec::Vec(), 1
    192     t2 = &s
    193     param t2                            (this)
    194     call Shape::Shape(), 1
    195     t3 = &s
    196     param t3                            (this)
    197     t4 = call Shape::area(), 1
    198     t5 = s[4]
    199     t6 = s[0]
    200     param "%d %d %d\n"
    201     param t4
    202     param t5
    203     param t6
    204     call printf, 4
    205     t7 = &a
    206     param t7                            (this)
    207     call Vec::Vec(), 1
    208     t8 = &b
    209     param t8                            (this)
    210     call Vec::Vec(), 1
    211     t9 = &a
    212     param t9                            (this)
    213     param 3
    214     t10 = call Vec::operator+=(int), 2
    215     b[0] = 1
    216     b[4] = 2
    217     t11 = &a
    218     t12 = &b
    219     param t11                           (this)
    220     param t12
    221     t13 = call Vec::operator+(class Vec &), 2
    222     c = t13
    223     t14 = &c
    224     param t14                           (this)
    225     param 0
    226     t15 = call Vec::operator[](int), 2
    227     t16 = *t15
    228     t17 = &c
    229     param t17                           (this)
    230     param 1
    231     t18 = call Vec::operator[](int), 2
    232     t19 = *t18
    233     t20 = &c
    234     t21 = &a
    235     param t20                           (this)
    236     param t21
    237     t22 = call Vec::operator==(class Vec &), 2
    238     t23 = &c
    239     param t23
    240     t24 = call peek(class Vec &), 1
    241     param "%d %d %d %d\n"
    242     param t16
    243     param t19
    244     param t22
    245     param t24
    246     call printf, 5
    247     param c
    248     t25 = call twice(class Vec), 1
    249     t26 = c[0]
    250     param "%d %d\n"
    251     param t25
    252     param t26
    253     call printf, 3
    254     t27 = &c
    255     param t27                           (this)
    256     param 1
    257     t28 = call Vec::operator[](int), 2
    258     *t28 = 9
    259     t29 = &pl
    260     param t29                           (this)
    261     call Base::Base(), 1
    262     t30 = c[4]
    263     t31 = &c
    264     param t31                           (this)
    265     param 3
    266     t32 = call Vec::operator()(int), 2
    267     t34 = &t33
    268     param t34                           (this)
    269     call Vec::Vec(), 1
    270     t35 = t33[0]
    271     t36 = pl[0]
    272     param "%d %d %d %d\n"
    273     param t30
    274     param t32
    275     param t35
    276     param t36
    277     call printf, 5
    278     t37 = &many
    279     param t37                           (this)
    280     call Vec::Vec(), 1
    281     t38 = t37 ptr+ 8
    282     param t38                           (this)
    283     call Vec::Vec(), 1
    284     t39 = t37 ptr+ 16
    285     param t39                           (this)
    286     call Vec::Vec(), 1
    287     t40 = &many
    288     t41 = t40 ptr+ 16
    289     param t41                           (this)
    290     param 5
    291     t42 = call Vec::operator+=(int), 2
    292     t43 = many[20]
    293     t44 = origin[0]
    294     param "%d %d %d\n"
    295     param t43
    296     param Vec::made
    297     param t44
    298     call printf, 4
    299     return 0


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
