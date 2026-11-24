============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 200 -> 227 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          200 -> 227   (-13% fewer)

   calls inlined                          24
   constants folded                        3
   algebraic simplifications               1
   common subexpressions                  20
   copies / constants forwarded           83
   temporaries merged away                 3
   dead instructions removed              61
   jumps removed or redirected             6
   unreachable instructions removed        5

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

 Symbol table: 3 parameter(s)/local(s), 10 temporaries, frame 60 bytes

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
   t11              temp    class Vec *                     4      56
   (1 temporary no longer used after optimization not shown)

 Code: 16 instruction(s)

    109     t1 = &r
    110     *t1 = 0
    111     t11 = t1 ptr+ 4
    112     *t11 = 0
    113     Vec::made = Vec::made int+ 1
    114     t2 = *this
    115     t3 = *o
    116     t4 = t2 int+ t3
    117     r[0] = t4
    118     t5 = this ptr+ 4
    119     t6 = *t5
    120     t7 = o ptr+ 4
    121     t8 = *t7
    122     t9 = t6 int+ t8
    123     r[4] = t9
    124     return r

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

    125     t1 = *this
    126     t2 = t1 int+ k
    127     *this = t2
    128     t3 = this ptr+ 4
    129     t4 = *t3
    130     t5 = t4 int+ k
    131     *t3 = t5
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

 Code: 12 instruction(s)

    133       t2 = *this
    134       t3 = *o
    135       if t2 int!= t3 goto L1
    136       t4 = this ptr+ 4
    137       t5 = *t4
    138       t6 = o ptr+ 4
    139       t7 = *t6
    140       if t5 int== t7 goto L2
    141  L1:  t1 = 0
    142       goto L3
    143  L2:  t1 = 1
    144  L3:  return t1

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

    145       if i int!= 0 goto L4
    146       t1 = this
    147       goto L5
    148  L4:  t1 = this ptr+ 4
    149  L5:  return t1

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

    150     t1 = *this
    151     t2 = t1 int* k
    152     return t2

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

    153     t1 = *v
    154     t2 = t1 int* 100
    155     t3 = v ptr+ 4
    156     t4 = *t3
    157     t5 = t2 int+ t4
    158     return t5

============================================================================
 FUNCTION Base::Base()        (link name _ZN4BaseC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 4 instruction(s)

    159     *this = 1
    160     param "Base "
    161     call printf, 1
    162     return

============================================================================
 FUNCTION Base::area()        (link name _ZN4Base4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    163     return 10

============================================================================
 FUNCTION Shape::Shape()        (link name _ZN5ShapeC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    class Shape *                   4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    164     *this = 1
    165     param "Base "
    166     call printf, 1
    167     t1 = this ptr+ 4
    168     *t1 = 7
    169     param "Part "
    170     call printf, 1
    171     t2 = *this
    172     t3 = t2 int+ 1
    173     *this = t3
    174     param "Shape\n"
    175     call printf, 1
    176     return

============================================================================
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 3 instruction(s)

    177     t2 = *this
    178     t3 = 10 int+ t2
    179     return t3

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

    180     t1 = v[0]
    181     t2 = t1 int<< 1
    182     v[0] = t2
    183     return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 69 temporaries, frame 576 bytes

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
   t5               temp    int                             4      80
   t6               temp    int                             4      84
   t7               temp    class Vec *                     4      88
   t8               temp    class Vec *                     4      92
   t14              temp    class Vec *                     4     120
   t16              temp    int                             4     128
   t19              temp    int                             4     140
   t26              temp    int                             4     168
   t29              temp    class Plain *                   4     180
   t30              temp    int                             4     184
   t33              temp    class Vec                       8     196
   t34              temp    class Vec *                     4     204
   t35              temp    int                             4     208
   t36              temp    int                             4     212
   t37              temp    class Vec (*)[3]                4     216
   t38              temp    class Vec (*)[3]                4     220
   t39              temp    class Vec (*)[3]                4     224
   t43              temp    int                             4     240
   t44              temp    int                             4     244
   t46              temp    class Vec *                     4     252
   t48              temp    class Shape *                   4     260
   t49              temp    int                             4     264
   t50              temp    int                             4     268
   t52              temp    int                             4     276
   t53              temp    int                             4     280
   t54              temp    int                             4     284
   t56              temp    class Vec *                     4     292
   t58              temp    class Vec *                     4     300
   t61              temp    int                             4     312
   t62              temp    int                             4     316
   t64              temp    int                             4     324
   t65              temp    int                             4     328
   t68              temp    class Vec                       8     340
   t69              temp    class Vec *                     4     348
   t70              temp    int                             4     352
   t71              temp    int                             4     356
   t72              temp    int                             4     360
   t74              temp    int                             4     368
   t76              temp    int                             4     376
   t77              temp    int                             4     380
   t83              temp    int *                           4     404
   t84              temp    class Vec *                     4     408
   t85              temp    class Vec &                     4     412
   t87              temp    int                             4     420
   t88              temp    class Vec *                     4     424
   t89              temp    int                             4     428
   t90              temp    class Vec *                     4     432
   t91              temp    int                             4     436
   t92              temp    int                             4     440
   t94              temp    int                             4     448
   t95              temp    int                             4     452
   t96              temp    class Vec *                     4     456
   t97              temp    int                             4     460
   t98              temp    int                             4     464
   t99              temp    class Vec                       8     468
   t100             temp    int                             4     476
   t101             temp    int                             4     480
   t108             temp    int                             4     508
   t109             temp    int                             4     512
   t111             temp    class Vec *                     4     520
   t113             temp    class Vec *                     4     528
   t115             temp    class Vec *                     4     536
   t117             temp    class Vec *                     4     544
   t120             temp    int                             4     556
   t121             temp    int                             4     560
   t123             temp    int                             4     568
   t124             temp    int                             4     572
   (55 temporaries no longer used after optimization not shown)

 Code: 143 instruction(s)

    184       t1 = &origin
    185       *t1 = 0
    186       t46 = t1 ptr+ 4
    187       *t46 = 0
    188       Vec::made = Vec::made int+ 1
    189       t2 = &s
    190       param t2                            (this)
    191       call Base::Base(), 1
    192       t48 = t2 ptr+ 4
    193       param t48                           (this)
    194       call Part::Part(), 1
    195       t49 = *t2
    196       t50 = t49 int+ 1
    197       *t2 = t50
    198       param "Shape\n"
    199       call printf, 1
    200       param t2                            (this)
    201       t52 = call Base::area(), 1
    202       t53 = *t2
    203       t54 = t52 int+ t53
    204       t5 = s[4]
    205       t6 = s[0]
    206       param "%d %d %d\n"
    207       param t54
    208       param t5
    209       param t6
    210       call printf, 4
    211       t7 = &a
    212       *t7 = 0
    213       t56 = t7 ptr+ 4
    214       *t56 = 0
    215       Vec::made = Vec::made int+ 1
    216       t8 = &b
    217       *t8 = 0
    218       t58 = t8 ptr+ 4
    219       *t58 = 0
    220       Vec::made = Vec::made int+ 1
    221       t61 = *t7
    222       t62 = t61 int+ 3
    223       *t7 = t62
    224       t64 = *t56
    225       t65 = t64 int+ 3
    226       *t56 = t65
    227       b[0] = 1
    228       b[4] = 2
    229       t69 = &t68
    230       param t69                           (this)
    231       call Vec::Vec(), 1
    232       t70 = *t7
    233       t71 = *t8
    234       t72 = t70 int+ t71
    235       t68[0] = t72
    236       t74 = *t56
    237       t76 = *t58
    238       t77 = t74 int+ t76
    239       t68[4] = t77
    240       c = t68
    241       t14 = &c
    242       t16 = *t14
    243       t83 = t14 ptr+ 4
    244       t19 = *t83
    245       t84 = t14
    246       t85 = t7
    247       t87 = *t7
    248       if t16 int!= t87 goto L6
    249       t88 = t84 ptr+ 4
    250       t89 = *t88
    251       t90 = t85 ptr+ 4
    252       t91 = *t90
    253       if t89 int== t91 goto L7
    254  L6:  t92 = 0
    255       goto L8
    256  L7:  t92 = 1
    257  L8:  t94 = *t14
    258       t95 = t94 int* 100
    259       t96 = t14 ptr+ 4
    260       t97 = *t96
    261       t98 = t95 int+ t97
    262       param "%d %d %d %d\n"
    263       param t16
    264       param t19
    265       param t92
    266       param t98
    267       call printf, 5
    268       t99 = c
    269       t100 = t99[0]
    270       t101 = t100 int<< 1
    271       t99[0] = t101
    272       t26 = c[0]
    273       param "%d %d\n"
    274       param t101
    275       param t26
    276       call printf, 3
    277       *t96 = 9
    278       t29 = &pl
    279       *t29 = 1
    280       param "Base "
    281       call printf, 1
    282       t30 = c[4]
    283       t108 = *t14
    284       t109 = t108 int* 3
    285       t34 = &t33
    286       *t34 = 0
    287       t111 = t34 ptr+ 4
    288       *t111 = 0
    289       Vec::made = Vec::made int+ 1
    290       t35 = t33[0]
    291       t36 = pl[0]
    292       param "%d %d %d %d\n"
    293       param t30
    294       param t109
    295       param t35
    296       param t36
    297       call printf, 5
    298       t37 = &many
    299       *t37 = 0
    300       t113 = t37 ptr+ 4
    301       *t113 = 0
    302       Vec::made = Vec::made int+ 1
    303       t38 = t37 ptr+ 8
    304       *t38 = 0
    305       t115 = t38 ptr+ 4
    306       *t115 = 0
    307       Vec::made = Vec::made int+ 1
    308       t39 = t37 ptr+ 16
    309       *t39 = 0
    310       t117 = t39 ptr+ 4
    311       *t117 = 0
    312       Vec::made = Vec::made int+ 1
    313       t120 = *t39
    314       t121 = t120 int+ 5
    315       *t39 = t121
    316       t123 = *t117
    317       t124 = t123 int+ 5
    318       *t117 = t124
    319       t43 = many[20]
    320       t44 = origin[0]
    321       param "%d %d %d\n"
    322       param t43
    323       param Vec::made
    324       param t44
    325       call printf, 4
    326       return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

Base Part Shape
12 7 2
4 5 0 405
8 4
Base 9 12 0 1
5 8 0

   exit code 0, 151 instructions executed
