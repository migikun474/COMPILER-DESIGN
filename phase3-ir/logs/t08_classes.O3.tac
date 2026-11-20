============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 261 -> 205 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          261 -> 205   (21% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                  27
   copies / constants forwarded           97
   temporaries merged away                 9
   dead instructions removed              70
   jumps removed or redirected             4
   unreachable instructions removed        2
   propagated across blocks                3
   dead assignments removed                5
   calls inlined                          28
   tail calls turned into jumps            0
   common subexpressions across blocks      3
   loops unrolled                          0
   unreachable functions removed          14

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Dog::made        int                             4  0

 As three address code (initial values, in place before main runs):

    Dog::made = 0

============================================================================
 FUNCTION Animal::Animal()        (link name _ZN6AnimalC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0

 Code: 4 instruction(s)

    100     *this = 4
    101     param "Animal()\n"
    102     call printf, 1
    103     return

============================================================================
 FUNCTION Tag::Tag()        (link name _ZN3TagC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0

 Code: 4 instruction(s)

    104     *this = 7
    105     param "Tag()\n"
    106     call printf, 1
    107     return

============================================================================
 FUNCTION Vec::Vec()        (link name _ZN3VecC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4

 Code: 4 instruction(s)

    108     *this = 0
    109     t1 = this ptr+ 4
    110     *t1 = 0
    111     return

============================================================================
 FUNCTION make(int, int)        (link name _Z4makeii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   v                local   class Vec                       8       8
   t1               temp    class Vec *                     4      16
   t3               temp    class Vec *                     4      24
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    112     t1 = &v
    113     *t1 = 0
    114     t3 = t1 ptr+ 4
    115     *t3 = 0
    116     v[0] = a
    117     v[4] = b
    118     return v

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 94 temporaries, frame 812 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   rex              local   class Dog                      12       0
   base             local   class Animal *                  4      12
   other            local   class Dog                      12      16
   a                local   class Vec                       8      28
   b                local   class Vec                       8      36
   c                local   class Vec                       8      44
   d                local   class Vec                       8      52
   e                local   class Vec                       8      60
   row              local   class Vec[2]                   16      68
   w                local   int                             4      84
   t1               temp    class Dog *                     4      88
   t9               temp    int                             4     120
   t10              temp    class Dog *                     4     124
   t15              temp    class Vec *                     4     152
   t16              temp    class Vec *                     4     156
   t25              temp    int                             4     204
   t26              temp    int                             4     208
   t27              temp    int                             4     212
   t28              temp    int                             4     216
   t29              temp    int                             4     220
   t30              temp    int                             4     224
   t41              temp    class Vec (*)[2]                4     268
   t42              temp    class Vec (*)[2]                4     272
   t43              temp    int                             4     276
   t45              temp    int                             4     284
   t46              temp    int                             4     288
   t48              temp    class Dog *                     4     296
   t49              temp    class Dog *                     4     300
   t52              temp    int                             4     312
   t53              temp    int                             4     316
   t57              temp    int                             4     332
   t58              temp    int                             4     336
   t59              temp    int                             4     340
   t61              temp    int                             4     348
   t62              temp    int                             4     352
   t66              temp    class Dog *                     4     368
   t67              temp    class Dog *                     4     372
   t70              temp    int                             4     384
   t71              temp    int                             4     388
   t72              temp    int                             4     392
   t73              temp    int                             4     396
   t75              temp    int                             4     404
   t76              temp    int                             4     408
   t79              temp    class Vec                       8     420
   t80              temp    class Vec *                     4     428
   t83              temp    class Vec                       8     440
   t84              temp    class Vec *                     4     448
   t86              temp    class Vec *                     4     456
   t88              temp    class Vec                       8     464
   t89              temp    class Vec                       8     472
   t90              temp    class Vec *                     4     480
   t91              temp    int                             4     484
   t92              temp    int                             4     488
   t93              temp    int                             4     492
   t94              temp    class Vec *                     4     496
   t95              temp    int                             4     500
   t96              temp    int                             4     504
   t97              temp    int                             4     508
   t99              temp    class Vec                       8     516
   t100             temp    class Vec *                     4     524
   t101             temp    int                             4     528
   t102             temp    int                             4     532
   t104             temp    int                             4     540
   t105             temp    int                             4     544
   t106             temp    class Vec                       8     548
   t108             temp    int                             4     560
   t109             temp    int                             4     564
   t110             temp    int                             4     568
   t111             temp    int                             4     572
   t114             temp    class Vec                       8     588
   t115             temp    int                             4     596
   t116             temp    int                             4     600
   t117             temp    int                             4     604
   t119             temp    int                             4     612
   t120             temp    int                             4     616
   t121             temp    int                             4     620
   t123             temp    int                             4     628
   t124             temp    int                             4     632
   t126             temp    class Vec                       8     640
   t127             temp    int                             4     648
   t128             temp    int                             4     652
   t130             temp    int                             4     660
   t131             temp    int                             4     664
   t132             temp    int                             4     668
   t134             temp    class Vec                       8     676
   t135             temp    int                             4     684
   t136             temp    int                             4     688
   t138             temp    int                             4     696
   t139             temp    int                             4     700
   t140             temp    int                             4     704
   t143             temp    int                             4     716
   t148             temp    int                             4     736
   t150             temp    int                             4     744
   t151             temp    int                             4     748
   t153             temp    class Vec                       8     756
   t154             temp    int                             4     764
   t155             temp    int                             4     768
   t156             temp    int                             4     772
   t158             temp    int                             4     780
   t159             temp    int                             4     784
   t160             temp    int                             4     788
   t161             temp    int                             4     792
   t163             temp    class Vec *                     4     800
   t165             temp    class Vec *                     4     808
   (71 temporaries no longer used after optimization not shown)

 Code: 186 instruction(s)

    119       t1 = &rex
    120       param t1                            (this)
    121       call Animal::Animal(), 1
    122       t48 = t1 ptr+ 8
    123       param t48                           (this)
    124       call Tag::Tag(), 1
    125       t49 = t1 ptr+ 4
    126       *t49 = 0
    127       Dog::made = Dog::made int+ 1
    128       param "Dog()\n"
    129       call printf, 1
    130       rex[4] = 3
    131       t52 = *t49
    132       t53 = t52 int+ 1
    133       *t49 = t53
    134       t57 = t53 int* 7
    135       t58 = *t1
    136       t59 = t57 int+ t58
    137       t61 = *t48
    138       t62 = t59 int+ t61
    139       param "%d %d %d\n"
    140       param t62
    141       param t58
    142       param Dog::made
    143       call printf, 4
    144       t9 = *t1
    145       param "%d\n"
    146       param t9
    147       call printf, 2
    148       param "--\n"
    149       call printf, 1
    150       t10 = &other
    151       param t10                           (this)
    152       call Animal::Animal(), 1
    153       t66 = t10 ptr+ 8
    154       param t66                           (this)
    155       call Tag::Tag(), 1
    156       t67 = t10 ptr+ 4
    157       *t67 = 0
    158       Dog::made = Dog::made int+ 1
    159       param "Dog()\n"
    160       call printf, 1
    161       other[4] = 5
    162       t70 = *t67
    163       t71 = t70 int* 7
    164       t72 = *t10
    165       t73 = t71 int+ t72
    166       t75 = *t66
    167       t76 = t73 int+ t75
    168       param "%d %d\n"
    169       param t76
    170       param Dog::made
    171       call printf, 3
    172       param "--\n"
    173       call printf, 1
    174       t80 = &t79
    175       param t80                           (this)
    176       call Vec::Vec(), 1
    177       t79[0] = 1
    178       t79[4] = 2
    179       a = t79
    180       t84 = &t83
    181       param t84                           (this)
    182       call Vec::Vec(), 1
    183       t83[0] = 3
    184       t83[4] = 4
    185       b = t83
    186       t15 = &c
    187       *t15 = 0
    188       t86 = t15 ptr+ 4
    189       *t86 = 0
    190       t16 = &a
    191       t88 = b
    192       t90 = &t89
    193       param t90                           (this)
    194       call Vec::Vec(), 1
    195       t91 = *t16
    196       t92 = t88[0]
    197       t93 = t91 int+ t92
    198       t89[0] = t93
    199       t94 = t16 ptr+ 4
    200       t95 = *t94
    201       t96 = t88[4]
    202       t97 = t95 int+ t96
    203       t89[4] = t97
    204       c = t89
    205       t100 = &t99
    206       param t100                          (this)
    207       call Vec::Vec(), 1
    208       t101 = *t15
    209       t102 = int- t101
    210       t99[0] = t102
    211       t104 = *t86
    212       t105 = int- t104
    213       t99[4] = t105
    214       d = t99
    215       t106 = a
    216       t108 = t106[0]
    217       t109 = t108 int* 3
    218       t110 = t106[4]
    219       t111 = t110 int* 3
    220       param t109
    221       param t111
    222       e = call make(int, int), 2
    223       t114 = b
    224       t115 = *t16
    225       t116 = t114[0]
    226       t117 = t115 int+ t116
    227       *t16 = t117
    228       t119 = *t94
    229       t120 = t114[4]
    230       t121 = t119 int+ t120
    231       *t94 = t121
    232       t123 = *t16
    233       t124 = t123 int+ 1
    234       *t16 = t124
    235       t25 = c[0]
    236       t26 = c[4]
    237       t27 = d[0]
    238       t28 = e[4]
    239       t29 = a[0]
    240       t30 = a[4]
    241       param "%d %d %d %d %d %d\n"
    242       param t25
    243       param t26
    244       param t27
    245       param t28
    246       param t29
    247       param t30
    248       call printf, 7
    249       t126 = b
    250       t127 = *t16
    251       t128 = t126[0]
    252       if t127 int!= t128 goto L1
    253       t130 = *t94
    254       t131 = t126[4]
    255       if t130 int== t131 goto L2
    256  L1:  t132 = 0
    257       goto L3
    258  L2:  t132 = 1
    259  L3:  t134 = c
    260       t135 = *t15
    261       t136 = t134[0]
    262       if t135 int!= t136 goto L4
    263       t138 = *t86
    264       t139 = t134[4]
    265       if t138 int== t139 goto L5
    266  L4:  t140 = 0
    267       goto L6
    268  L5:  t140 = 1
    269  L6:  t143 = *t16
    270       t148 = t143 int<< 1
    271       t150 = *t94
    272       t151 = t148 int+ t150
    273       t153 = b
    274       t154 = *t16
    275       t155 = t153[0]
    276       t156 = t154 int* t155
    277       t158 = *t94
    278       t159 = t153[4]
    279       t160 = t158 int* t159
    280       t161 = t156 int+ t160
    281       param "%d %d %d %d %d\n"
    282       param t132
    283       param t140
    284       param t143
    285       param t151
    286       param t161
    287       call printf, 6
    288       t41 = &row
    289       *t41 = 0
    290       t163 = t41 ptr+ 4
    291       *t163 = 0
    292       t42 = t41 ptr+ 8
    293       *t42 = 0
    294       t165 = t42 ptr+ 4
    295       *t165 = 0
    296       row[8] = 9
    297       t43 = row[0]
    298       param "%d %d\n"
    299       param t43
    300       param 9
    301       call printf, 3
    302       t45 = c[0]
    303       t46 = 7 int+ t45
    304       return t46


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Animal             class_tag     class Animal               -           5    -    0  size 4
   Tag                class_tag     class Tag                  -          12    -    0  size 4
   Dog                class_tag     class Dog                  -          18    -    0  size 12, public base Animal
   Vec                class_tag     class Vec                  -          31    -    0  size 8
   make               function      class Vec (int, int)       -          45    -    3  _Z4makeii; defined
   operator*          function      class Vec (class Vec, int) -          46    -    1  _Zml3Veci; defined
   main               function      int (void)                 -          48    -    0  defined

 scope: global > class Animal
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   legs               field         int                        member      7    4    4  Animal::legs; public, offset 0
   Animal             constructor   void (void)                -           8    -    0  _ZN6AnimalC1Ev; public
   count              method        int (void)                 -           9    -    1  _ZN6Animal5countEv; public, defined

 scope: global > class Tag
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     14    4    2  Tag::id; public, offset 0
   Tag                constructor   void (void)                -          15    -    0  _ZN3TagC1Ev; public

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   age                field         int                        member     20    4    6  Dog::age; public, offset 4
   tag                field         class Tag                  member     21    4    1  Dog::tag; public, offset 8
   made               field         int                        static     22    4    3  Dog::made; public, static
   Dog                constructor   void (void)                -          23    -    2  _ZN3DogC1Ev; public
   human              method        int (void)                 -          24    -    2  _ZN3Dog5humanEv; public, defined
   birthday           method        void (void)                -          25    -    1  _ZN3Dog8birthdayEv; public, defined
   total              method        int (void)                 -          26    -    1  _ZN3Dog5totalEv; public, static, defined

 scope: global > class Vec
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     33    4   24  Vec::x; public, offset 0
   y                  field         int                        member     34    4   19  Vec::y; public, offset 4
   Vec                constructor   void (void)                -          35    -    5  _ZN3VecC1Ev; public
   operator+          method        class Vec (class Vec)      -          36    -    1  _ZN3VecplES_; public, defined
   operator-          method        class Vec (void)           -          37    -    1  _ZN3VecmiEv; public, defined
   operator==         method        int (class Vec)            -          38    -    2  _ZN3VeceqES_; public, defined
   operator[]         method        int (int)                  -          39    -    1  _ZN3VecixEi; public, defined
   operator+=         method        class Vec &(class Vec)     -          40    -    1  _ZN3VecpLES_; public, defined
   operator++         method        class Vec &(void)          -          41    -    1  _ZN3VecppEv; public, defined
   operator()         method        int (int)                  -          42    -    1  _ZN3VecclEi; public, defined
   dot                method        int (class Vec)            -          43    -    1  _ZN3Vec3dotES_; public, defined

 scope: global > class Vec > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      36    8    2  o.1
   r                  variable      class Vec                  local      36    8    3  r.2

 scope: global > class Vec > operator-()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Vec                  local      37    8    3  r.3

 scope: global > class Vec > operator==()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      38    8    2  o.4

 scope: global > class Vec > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      39    4    1  i.5

 scope: global > class Vec > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      40    8    2  o.6

 scope: global > class Vec > operator()()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      42    4    1  k.7

 scope: global > class Vec > dot()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      43    8    2  o.8

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      45    4    1  a.9
   b                  parameter     int                        param      45    4    1  b.10
   v                  variable      class Vec                  local      45    8    3  v.11

 scope: global > operator*()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     class Vec                  param      46    8    2  v.12
   k                  parameter     int                        param      46    4    2  k.13

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   rex                variable      class Dog                  local      50   12    5  rex.14
   base               variable      class Animal *             local      54    4    1  base.15
   other              variable      class Dog                  local      59   12    2  other.16

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      class Vec                  local      65    8   10  a.17
   b                  variable      class Vec                  local      65    8    4  b.18
   c                  variable      class Vec                  local      65    8    7  c.19
   d                  variable      class Vec                  local      67    8    1  d.20
   e                  variable      class Vec                  local      68    8    1  e.21
   row                variable      class Vec[2]               local      73   16    3  row.22
   w                  variable      int                        local      76    4    1  w.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Animal: size 4, align 4
    +0  int legs  [public]
class Tag: size 4, align 4
    +0  int id  [public]
class Dog: size 12, align 4
    (base Animal, public)
    +4  int age  [public]
    +8  class Tag tag  [public]
    static  int made  [public]
class Vec: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
