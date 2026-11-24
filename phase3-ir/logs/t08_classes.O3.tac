============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 265 -> 205 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          265 -> 205   (22% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                  28
   copies / constants forwarded           98
   temporaries merged away                 9
   dead instructions removed              74
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

 Symbol table: 10 parameter(s)/local(s), 94 temporaries, frame 828 bytes

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
   t14              temp    class Vec *                     4     144
   t17              temp    class Vec *                     4     160
   t29              temp    int                             4     220
   t30              temp    int                             4     224
   t31              temp    int                             4     228
   t32              temp    int                             4     232
   t33              temp    int                             4     236
   t34              temp    int                             4     240
   t45              temp    class Vec (*)[2]                4     284
   t46              temp    class Vec (*)[2]                4     288
   t47              temp    int                             4     292
   t49              temp    int                             4     300
   t50              temp    int                             4     304
   t52              temp    class Dog *                     4     312
   t53              temp    class Dog *                     4     316
   t56              temp    int                             4     328
   t57              temp    int                             4     332
   t61              temp    int                             4     348
   t62              temp    int                             4     352
   t63              temp    int                             4     356
   t65              temp    int                             4     364
   t66              temp    int                             4     368
   t70              temp    class Dog *                     4     384
   t71              temp    class Dog *                     4     388
   t74              temp    int                             4     400
   t75              temp    int                             4     404
   t76              temp    int                             4     408
   t77              temp    int                             4     412
   t79              temp    int                             4     420
   t80              temp    int                             4     424
   t83              temp    class Vec                       8     436
   t84              temp    class Vec *                     4     444
   t87              temp    class Vec                       8     456
   t88              temp    class Vec *                     4     464
   t90              temp    class Vec *                     4     472
   t92              temp    class Vec                       8     480
   t93              temp    class Vec                       8     488
   t94              temp    class Vec *                     4     496
   t95              temp    int                             4     500
   t96              temp    int                             4     504
   t97              temp    int                             4     508
   t98              temp    class Vec *                     4     512
   t99              temp    int                             4     516
   t100             temp    int                             4     520
   t101             temp    int                             4     524
   t103             temp    class Vec                       8     532
   t104             temp    class Vec *                     4     540
   t105             temp    int                             4     544
   t106             temp    int                             4     548
   t108             temp    int                             4     556
   t109             temp    int                             4     560
   t110             temp    class Vec                       8     564
   t112             temp    int                             4     576
   t113             temp    int                             4     580
   t114             temp    int                             4     584
   t115             temp    int                             4     588
   t118             temp    class Vec                       8     604
   t119             temp    int                             4     612
   t120             temp    int                             4     616
   t121             temp    int                             4     620
   t123             temp    int                             4     628
   t124             temp    int                             4     632
   t125             temp    int                             4     636
   t127             temp    int                             4     644
   t128             temp    int                             4     648
   t130             temp    class Vec                       8     656
   t131             temp    int                             4     664
   t132             temp    int                             4     668
   t134             temp    int                             4     676
   t135             temp    int                             4     680
   t136             temp    int                             4     684
   t138             temp    class Vec                       8     692
   t139             temp    int                             4     700
   t140             temp    int                             4     704
   t142             temp    int                             4     712
   t143             temp    int                             4     716
   t144             temp    int                             4     720
   t147             temp    int                             4     732
   t152             temp    int                             4     752
   t154             temp    int                             4     760
   t155             temp    int                             4     764
   t157             temp    class Vec                       8     772
   t158             temp    int                             4     780
   t159             temp    int                             4     784
   t160             temp    int                             4     788
   t162             temp    int                             4     796
   t163             temp    int                             4     800
   t164             temp    int                             4     804
   t165             temp    int                             4     808
   t167             temp    class Vec *                     4     816
   t169             temp    class Vec *                     4     824
   (75 temporaries no longer used after optimization not shown)

 Code: 186 instruction(s)

    119       t1 = &rex
    120       param t1                            (this)
    121       call Animal::Animal(), 1
    122       t52 = t1 ptr+ 8
    123       param t52                           (this)
    124       call Tag::Tag(), 1
    125       t53 = t1 ptr+ 4
    126       *t53 = 0
    127       Dog::made = Dog::made int+ 1
    128       param "Dog()\n"
    129       call printf, 1
    130       rex[4] = 3
    131       t56 = *t53
    132       t57 = t56 int+ 1
    133       *t53 = t57
    134       t61 = t57 int* 7
    135       t62 = *t1
    136       t63 = t61 int+ t62
    137       t65 = *t52
    138       t66 = t63 int+ t65
    139       param "%d %d %d\n"
    140       param t66
    141       param t62
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
    153       t70 = t10 ptr+ 8
    154       param t70                           (this)
    155       call Tag::Tag(), 1
    156       t71 = t10 ptr+ 4
    157       *t71 = 0
    158       Dog::made = Dog::made int+ 1
    159       param "Dog()\n"
    160       call printf, 1
    161       other[4] = 5
    162       t74 = *t71
    163       t75 = t74 int* 7
    164       t76 = *t10
    165       t77 = t75 int+ t76
    166       t79 = *t70
    167       t80 = t77 int+ t79
    168       param "%d %d\n"
    169       param t80
    170       param Dog::made
    171       call printf, 3
    172       param "--\n"
    173       call printf, 1
    174       t84 = &t83
    175       param t84                           (this)
    176       call Vec::Vec(), 1
    177       t83[0] = 1
    178       t83[4] = 2
    179       a = t83
    180       t14 = &a
    181       t88 = &t87
    182       param t88                           (this)
    183       call Vec::Vec(), 1
    184       t87[0] = 3
    185       t87[4] = 4
    186       b = t87
    187       t17 = &c
    188       *t17 = 0
    189       t90 = t17 ptr+ 4
    190       *t90 = 0
    191       t92 = b
    192       t94 = &t93
    193       param t94                           (this)
    194       call Vec::Vec(), 1
    195       t95 = *t14
    196       t96 = t92[0]
    197       t97 = t95 int+ t96
    198       t93[0] = t97
    199       t98 = t14 ptr+ 4
    200       t99 = *t98
    201       t100 = t92[4]
    202       t101 = t99 int+ t100
    203       t93[4] = t101
    204       c = t93
    205       t104 = &t103
    206       param t104                          (this)
    207       call Vec::Vec(), 1
    208       t105 = *t17
    209       t106 = int- t105
    210       t103[0] = t106
    211       t108 = *t90
    212       t109 = int- t108
    213       t103[4] = t109
    214       d = t103
    215       t110 = a
    216       t112 = t110[0]
    217       t113 = t112 int* 3
    218       t114 = t110[4]
    219       t115 = t114 int* 3
    220       param t113
    221       param t115
    222       e = call make(int, int), 2
    223       t118 = b
    224       t119 = *t14
    225       t120 = t118[0]
    226       t121 = t119 int+ t120
    227       *t14 = t121
    228       t123 = *t98
    229       t124 = t118[4]
    230       t125 = t123 int+ t124
    231       *t98 = t125
    232       t127 = *t14
    233       t128 = t127 int+ 1
    234       *t14 = t128
    235       t29 = c[0]
    236       t30 = c[4]
    237       t31 = d[0]
    238       t32 = e[4]
    239       t33 = a[0]
    240       t34 = a[4]
    241       param "%d %d %d %d %d %d\n"
    242       param t29
    243       param t30
    244       param t31
    245       param t32
    246       param t33
    247       param t34
    248       call printf, 7
    249       t130 = b
    250       t131 = *t14
    251       t132 = t130[0]
    252       if t131 int!= t132 goto L1
    253       t134 = *t98
    254       t135 = t130[4]
    255       if t134 int== t135 goto L2
    256  L1:  t136 = 0
    257       goto L3
    258  L2:  t136 = 1
    259  L3:  t138 = c
    260       t139 = *t17
    261       t140 = t138[0]
    262       if t139 int!= t140 goto L4
    263       t142 = *t90
    264       t143 = t138[4]
    265       if t142 int== t143 goto L5
    266  L4:  t144 = 0
    267       goto L6
    268  L5:  t144 = 1
    269  L6:  t147 = *t14
    270       t152 = t147 int<< 1
    271       t154 = *t98
    272       t155 = t152 int+ t154
    273       t157 = b
    274       t158 = *t14
    275       t159 = t157[0]
    276       t160 = t158 int* t159
    277       t162 = *t98
    278       t163 = t157[4]
    279       t164 = t162 int* t163
    280       t165 = t160 int+ t164
    281       param "%d %d %d %d %d\n"
    282       param t136
    283       param t144
    284       param t147
    285       param t155
    286       param t165
    287       call printf, 6
    288       t45 = &row
    289       *t45 = 0
    290       t167 = t45 ptr+ 4
    291       *t167 = 0
    292       t46 = t45 ptr+ 8
    293       *t46 = 0
    294       t169 = t46 ptr+ 4
    295       *t169 = 0
    296       row[8] = 9
    297       t47 = row[0]
    298       param "%d %d\n"
    299       param t47
    300       param 9
    301       call printf, 3
    302       t49 = c[0]
    303       t50 = 7 int+ t49
    304       return t50


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
