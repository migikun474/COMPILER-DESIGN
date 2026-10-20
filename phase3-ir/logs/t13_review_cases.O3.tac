============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_review_cases.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 176 -> 147 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          176 -> 147   (16% fewer)

   constants folded                        6
   algebraic simplifications               0
   common subexpressions                   9
   copies / constants forwarded           56
   temporaries merged away                 5
   dead instructions removed              34
   jumps removed or redirected             7
   unreachable instructions removed        5
   propagated across blocks               10
   dead assignments removed               13
   calls inlined                          17
   tail calls turned into jumps            0
   common subexpressions across blocks      6
   instructions moved out of loops         0

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Cnt::made        int                             4  5
   chosen           double                          8  2.5

============================================================================
 FUNCTION half(const double &)        (link name _Z4halfRKd)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   const double &                  4       0
   t1               temp    double                          8       8
   t2               temp    double                          8      16

 Code: 3 instruction(s)

    100     t1 = *v
    101     t2 = t1 double/ 2.0
    102     return t2

============================================================================
 FUNCTION A::A()        (link name _ZN1AC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class A *                       4       0

 Code: 2 instruction(s)

    103     *this = 1
    104     return

============================================================================
 FUNCTION A::ga()        (link name _ZN1A2gaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class A *                       4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    105     t1 = *this
    106     return t1

============================================================================
 FUNCTION B::B()        (link name _ZN1BC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class B *                       4       0

 Code: 2 instruction(s)

    107     *this = 2
    108     return

============================================================================
 FUNCTION B::gb()        (link name _ZN1B2gbEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class B *                       4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    109     t1 = *this
    110     return t1

============================================================================
 FUNCTION C::C()        (link name _ZN1CC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class C *                       4       0
   t1               temp    class C *                       4       4
   t2               temp    class C *                       4       8
   (2 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    111     *this = 1
    112     t1 = this ptr+ 4
    113     *t1 = 2
    114     t2 = this ptr+ 8
    115     *t2 = 3
    116     return

============================================================================
 FUNCTION C::sum()        (link name _ZN1C3sumEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class C *                       4       0
   t1               temp    int                             4       4
   t2               temp    class C *                       4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    class C *                       4      20
   t6               temp    int                             4      24
   t7               temp    int                             4      28

 Code: 8 instruction(s)

    117     t1 = *this
    118     t2 = this ptr+ 4
    119     t3 = *t2
    120     t4 = t1 int+ t3
    121     t5 = this ptr+ 8
    122     t6 = *t5
    123     t7 = t4 int+ t6
    124     return t7

============================================================================
 FUNCTION takeB(class B *)        (link name _Z5takeBP1B)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   class B *                       4       0
   t1               temp    int                             4       4
   (2 temporaries no longer used after optimization not shown)

 Code: 5 instruction(s)

    125       if p ptr== 0 goto L1
    126       t1 = *p
    127       goto L2
    128  L1:  t1 = -1
    129  L2:  return t1

============================================================================
 FUNCTION Cnt::Cnt()        (link name _ZN3CntC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Cnt *                     4       0
   t1               temp    int                             4       4

 Code: 4 instruction(s)

    130     t1 = Cnt::made int+ 1
    131     Cnt::made = t1
    132     *this = t1
    133     return

============================================================================
 FUNCTION Dog::Dog(int)        (link name _ZN3DogC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   n                param   int                             4       4

 Code: 2 instruction(s)

    134     *this = n
    135     return

============================================================================
 FUNCTION Dog::~Dog()        (link name _ZN3DogD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    136     t1 = *this
    137     param "~Dog(%d)\n"
    138     param t1
    139     call printf, 2
    140     return

============================================================================
 FUNCTION vsum(int, va_list)        (link name _Z4vsumiPv)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               param   va_list                         4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t3               temp    int                             4      20
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    141       s = 0
    142  L3:  t1 = n
    143       n = n int- 1
    144       if t1 int<= 0 goto L4
    145       t3 = va_arg ap, int
    146       s = s int+ t3
    147       goto L3
    148  L4:  return s

============================================================================
 FUNCTION total(int, ...)        (link name _Z5totaliz)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   s                local   int                             4       8
   t1               temp    int                             4      12

 Code: 6 instruction(s)

    149     va_start ap, n
    150     param n
    151     param ap
    152     t1 = call vsum(int, va_list), 2
    153     va_end ap
    154     return t1

============================================================================
 FUNCTION one()        (link name _Z3onev)
============================================================================

 Code: 1 instruction(s)

    155     return 1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 33 temporaries, frame 396 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                local   int                             4       0
   c                local   class C                        12       4
   pb               local   class B *                       4      16
   none             local   class C *                       4      20
   nb               local   class B *                       4      24
   first            local   class A                         4      28
   guard            local   int                             4      32
   x                local   class Cnt                       4      36
   y                local   class Cnt                       4      40
   d                local   class Dog                       4      44
   last             local   class Dog                       4      48
   t1               temp    double                          8      56
   t3               temp    const double *                  4      72
   t5               temp    double                          8      88
   t6               temp    const double *                  4      96
   t8               temp    class C *                       4     112
   t10              temp    class B *                       4     120
   t13              temp    int                             4     132
   t17              temp    int                             4     148
   t19              temp    class B *                       4     156
   t22              temp    int                             4     168
   t25              temp    class A *                       4     180
   t26              temp    class A                         4     184
   t27              temp    int                             4     188
   t28              temp    class Cnt *                     4     192
   t29              temp    class Cnt *                     4     196
   t30              temp    int                             4     200
   t31              temp    int                             4     204
   t32              temp    int                             4     208
   t33              temp    class Dog *                     4     212
   t35              temp    class Dog *                     4     220
   t38              temp    double                          8     232
   t39              temp    double                          8     240
   t41              temp    double                          8     256
   t42              temp    double                          8     264
   t44              temp    class C *                       4     276
   t45              temp    class C *                       4     280
   t47              temp    int                             4     288
   t49              temp    int                             4     296
   t50              temp    int                             4     300
   t52              temp    int                             4     308
   t57              temp    int                             4     328
   t63              temp    int                             4     352
   t65              temp    int                             4     360
   (40 temporaries no longer used after optimization not shown)

 Code: 91 instruction(s)

    156       t1 = 5.0
    157       t3 = &t1
    158       t38 = *t3
    159       t39 = t38 double/ 2.0
    160       t5 = 3.0
    161       t6 = &t5
    162       t41 = *t6
    163       t42 = t41 double/ 2.0
    164       param "%.2f %.2f\n"
    165       param t39
    166       param t42
    167       call printf, 3
    168       t8 = &c
    169       param t8                            (this)
    170       call A::A(), 1
    171       t44 = t8 ptr+ 4
    172       param t44                           (this)
    173       call B::B(), 1
    174       t45 = t8 ptr+ 8
    175       *t45 = 3
    176       t10 = t8
    177       if t8 ptr== 0 goto L5
    178       t10 = t44
    179  L5:  t47 = *t8
    180       t49 = *t44
    181       t50 = t47 int+ t49
    182       t52 = *t45
    183       t13 = t50 int+ t52
    184       t17 = *t10
    185       t19 = t8
    186       if t8 ptr== 0 goto L6
    187       t19 = t44
    188  L6:  if t19 ptr== 0 goto L7
    189       t57 = *t19
    190       goto L8
    191  L7:  t57 = -1
    192  L8:  t22 = *t8
    193       param "%d %d %d %d %d %d %d\n"
    194       param t13
    195       param t49
    196       param t17
    197       param t57
    198       param t22
    199       param 1
    200       param -1
    201       call printf, 8
    202       t25 = &first
    203       t26 = c[0]
    204       *t25 = t26
    205       t27 = first[0]
    206       param "%d %d\n"
    207       param t27
    208       param 77
    209       call printf, 3
    210       t28 = &x
    211       t63 = Cnt::made int+ 1
    212       Cnt::made = t63
    213       *t28 = t63
    214       t29 = &y
    215       t65 = Cnt::made int+ 1
    216       Cnt::made = t65
    217       *t29 = t65
    218       t30 = x[0]
    219       t31 = y[0]
    220       param "%d %d %d\n"
    221       param Cnt::made
    222       param t30
    223       param t31
    224       call printf, 4
    225       param 3
    226       param 1
    227       param 2
    228       param 3
    229       t32 = call total(int, ...), 4
    230       param "%.1f %d\n"
    231       param chosen
    232       param t32
    233       call printf, 3
    234       t33 = &d
    235       *t33 = 1
    236       param "~Dog(%d)\n"
    237       param 1
    238       call printf, 2
    239       param "after the block\n"
    240       call printf, 1
    241       t35 = &last
    242       *t35 = 2
    243       param "~Dog(%d)\n"
    244       param 2
    245       call printf, 2
    246       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   half               function      double (const double &)    -           6    -    2  _Z4halfRKd; defined
   A                  class_tag     class A                    -           8    -    0  size 4
   B                  class_tag     class B                    -           9    -    0  size 4
   C                  class_tag     class C                    -          10    -    0  size 12, public base A, public base B
   takeB              function      int (class B *)            -          16    -    2  _Z5takeBP1B; defined
   Cnt                class_tag     class Cnt                  -          18    -    0  size 4
   Dog                class_tag     class Dog                  -          26    -    0  size 4
   chosen             variable      double                     global     33    8    1  
   vsum               function      int (int, va_list)         -          35    -    1  _Z4vsumiPv; defined
   total              function      int (int, ...)             -          40    -    1  _Z5totaliz; defined
   one                function      int (void)                 -          48    -    1  _Z3onev; defined
   main               function      int (void)                 -          50    -    0  defined

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const double &             param       6    4    1  v.1

 scope: global > class A
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member      8    4    4  A::a; public, offset 0
   A                  constructor   void (void)                -           8    -    1  _ZN1AC1Ev; public
   ga                 method        int (void)                 -           8    -    1  _ZN1A2gaEv; public, defined

 scope: global > class B
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  field         int                        member      9    4    5  B::b; public, offset 0
   B                  constructor   void (void)                -           9    -    1  _ZN1BC1Ev; public
   gb                 method        int (void)                 -           9    -    1  _ZN1B2gbEv; public, defined

 scope: global > class C
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  field         int                        member     12    4    2  C::c; public, offset 8
   C                  constructor   void (void)                -          13    -    1  _ZN1CC1Ev; public
   sum                method        int (void)                 -          14    -    1  _ZN1C3sumEv; public, defined

 scope: global > takeB()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     class B *                  param      16    4    2  p.2

 scope: global > class Cnt
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   made               field         int                        static     20    4    3  Cnt::made; public, static
   id                 field         int                        member     21    4    3  Cnt::id; public, offset 0
   Cnt                constructor   void (void)                -          22    -    2  _ZN3CntC1Ev; public

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     28    4    2  Dog::id; public, offset 0
   Dog                constructor   void (int)                 -          29    -    2  _ZN3DogC1Ei; public
   ~Dog               destructor    void (void)                -          30    -    0  _ZN3DogD1Ev; public

 scope: global > class Dog > Dog()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      29    4    1  n.3

 scope: global > vsum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      35    4    1  n.4
   ap                 parameter     va_list                    param      35    4    1  ap.5
   s                  variable      int                        local      36    4    2  s.6

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      40    4    2  n.7
   ap                 variable      va_list                    local      41    4    3  ap.8
   s                  variable      int                        local      43    4    1  s.9

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      51    4    2  k.10
   c                  variable      class C                    local      54   12    6  c.11
   pb                 variable      class B *                  local      55    4    1  pb.12
   none               variable      class C *                  local      56    4    1  none.13
   nb                 variable      class B *                  local      57    4    2  nb.14
   first              variable      class A                    local      59    4    1  first.15
   guard              variable      int                        local      60    4    1  guard.16
   x                  variable      class Cnt                  local      63    4    1  x.17
   y                  variable      class Cnt                  local      63    4    1  y.18

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      class Dog                  local      68    4    0  d.19
   last               variable      class Dog                  local      73    4    0  last.20

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class A: size 4, align 4
    +0  int a  [public]
class B: size 4, align 4
    +0  int b  [public]
class C: size 12, align 4
    (base A, public)
    (base B, public)
    +8  int c  [public]
class Cnt: size 4, align 4
    static  int made  [public]
    +0  int id  [public]
class Dog: size 4, align 4
    +0  int id  [public]
