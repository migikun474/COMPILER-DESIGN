============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 200 -> 152 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          200 -> 152   (24% fewer)

   constants folded                        3
   algebraic simplifications               1
   common subexpressions                  20
   copies / constants forwarded           87
   temporaries merged away                 3
   dead instructions removed              64
   jumps removed or redirected             6
   unreachable instructions removed        5
   propagated across blocks                2
   dead assignments removed                2
   calls inlined                          24
   tail calls turned into jumps            0
   common subexpressions across blocks      3
   loops unrolled                          0
   unreachable functions removed           9

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
 FUNCTION Base::Base()        (link name _ZN4BaseC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 4 instruction(s)

    109     *this = 1
    110     param "Base "
    111     call printf, 1
    112     return

============================================================================
 FUNCTION Base::area()        (link name _ZN4Base4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Base *                    4       0

 Code: 1 instruction(s)

    113     return 10

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 6 parameter(s)/local(s), 64 temporaries, frame 576 bytes

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
   t87              temp    int                             4     420
   t89              temp    int                             4     428
   t91              temp    int                             4     436
   t92              temp    int                             4     440
   t94              temp    int                             4     448
   t95              temp    int                             4     452
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
   (60 temporaries no longer used after optimization not shown)

 Code: 138 instruction(s)

    114       t1 = &origin
    115       *t1 = 0
    116       t46 = t1 ptr+ 4
    117       *t46 = 0
    118       Vec::made = Vec::made int+ 1
    119       t2 = &s
    120       param t2                            (this)
    121       call Base::Base(), 1
    122       t48 = t2 ptr+ 4
    123       param t48                           (this)
    124       call Part::Part(), 1
    125       t49 = *t2
    126       t50 = t49 int+ 1
    127       *t2 = t50
    128       param "Shape\n"
    129       call printf, 1
    130       param t2                            (this)
    131       t52 = call Base::area(), 1
    132       t53 = *t2
    133       t54 = t52 int+ t53
    134       t5 = s[4]
    135       t6 = s[0]
    136       param "%d %d %d\n"
    137       param t54
    138       param t5
    139       param t6
    140       call printf, 4
    141       t7 = &a
    142       *t7 = 0
    143       t56 = t7 ptr+ 4
    144       *t56 = 0
    145       Vec::made = Vec::made int+ 1
    146       t8 = &b
    147       *t8 = 0
    148       t58 = t8 ptr+ 4
    149       *t58 = 0
    150       Vec::made = Vec::made int+ 1
    151       t61 = *t7
    152       t62 = t61 int+ 3
    153       *t7 = t62
    154       t64 = *t56
    155       t65 = t64 int+ 3
    156       *t56 = t65
    157       b[0] = 1
    158       b[4] = 2
    159       t69 = &t68
    160       param t69                           (this)
    161       call Vec::Vec(), 1
    162       t70 = *t7
    163       t71 = *t8
    164       t72 = t70 int+ t71
    165       t68[0] = t72
    166       t74 = *t56
    167       t76 = *t58
    168       t77 = t74 int+ t76
    169       t68[4] = t77
    170       c = t68
    171       t14 = &c
    172       t16 = *t14
    173       t83 = t14 ptr+ 4
    174       t19 = *t83
    175       t87 = *t7
    176       if t16 int!= t87 goto L1
    177       t89 = *t83
    178       t91 = *t56
    179       if t89 int== t91 goto L2
    180  L1:  t92 = 0
    181       goto L3
    182  L2:  t92 = 1
    183  L3:  t94 = *t14
    184       t95 = t94 int* 100
    185       t97 = *t83
    186       t98 = t95 int+ t97
    187       param "%d %d %d %d\n"
    188       param t16
    189       param t19
    190       param t92
    191       param t98
    192       call printf, 5
    193       t99 = c
    194       t100 = t99[0]
    195       t101 = t100 int<< 1
    196       t99[0] = t101
    197       t26 = c[0]
    198       param "%d %d\n"
    199       param t101
    200       param t26
    201       call printf, 3
    202       *t83 = 9
    203       t29 = &pl
    204       *t29 = 1
    205       param "Base "
    206       call printf, 1
    207       t30 = c[4]
    208       t108 = *t14
    209       t109 = t108 int* 3
    210       t34 = &t33
    211       *t34 = 0
    212       t111 = t34 ptr+ 4
    213       *t111 = 0
    214       Vec::made = Vec::made int+ 1
    215       t35 = t33[0]
    216       t36 = pl[0]
    217       param "%d %d %d %d\n"
    218       param t30
    219       param t109
    220       param t35
    221       param t36
    222       call printf, 5
    223       t37 = &many
    224       *t37 = 0
    225       t113 = t37 ptr+ 4
    226       *t113 = 0
    227       Vec::made = Vec::made int+ 1
    228       t38 = t37 ptr+ 8
    229       *t38 = 0
    230       t115 = t38 ptr+ 4
    231       *t115 = 0
    232       Vec::made = Vec::made int+ 1
    233       t39 = t37 ptr+ 16
    234       *t39 = 0
    235       t117 = t39 ptr+ 4
    236       *t117 = 0
    237       Vec::made = Vec::made int+ 1
    238       t120 = *t39
    239       t121 = t120 int+ 5
    240       *t39 = t121
    241       t123 = *t117
    242       t124 = t123 int+ 5
    243       *t117 = t124
    244       t43 = many[20]
    245       t44 = origin[0]
    246       param "%d %d %d\n"
    247       param t43
    248       param Vec::made
    249       param t44
    250       call printf, 4
    251       return 0


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
