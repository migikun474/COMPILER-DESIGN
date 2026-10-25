============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_review_cases.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 176 -> 148 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          176 -> 148   (15% fewer)

   constants folded                        5
   algebraic simplifications               0
   common subexpressions                   5
   copies / constants forwarded           18
   temporaries merged away                 3
   dead instructions removed               7
   jumps removed or redirected             6
   unreachable instructions removed        3
   propagated across blocks                5
   dead assignments removed                8

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Cnt::made        int                             4  5
   chosen           double                          8  2.5

 As three address code (initial values, in place before main runs):

    Cnt::made = 5
    chosen = 2.5

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class C *                       4       0
   t1               temp    class C *                       4       4
   t2               temp    class C *                       4       8

 Code: 8 instruction(s)

    111     param this                          (this)
    112     call A::A(), 1
    113     t1 = this ptr+ 4
    114     param t1                            (this)
    115     call B::B(), 1
    116     t2 = this ptr+ 8
    117     *t2 = 3
    118     return

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

    119     t1 = *this
    120     t2 = this ptr+ 4
    121     t3 = *t2
    122     t4 = t1 int+ t3
    123     t5 = this ptr+ 8
    124     t6 = *t5
    125     t7 = t4 int+ t6
    126     return t7

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

    127       if p ptr== 0 goto L1
    128       t1 = *p
    129       goto L2
    130  L1:  t1 = -1
    131  L2:  return t1

============================================================================
 FUNCTION Cnt::Cnt()        (link name _ZN3CntC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Cnt *                     4       0
   t1               temp    int                             4       4

 Code: 4 instruction(s)

    132     t1 = Cnt::made int+ 1
    133     Cnt::made = t1
    134     *this = t1
    135     return

============================================================================
 FUNCTION Dog::Dog(int)        (link name _ZN3DogC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   n                param   int                             4       4

 Code: 2 instruction(s)

    136     *this = n
    137     return

============================================================================
 FUNCTION Dog::~Dog()        (link name _ZN3DogD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    138     t1 = *this
    139     param "~Dog(%d)\n"
    140     param t1
    141     call printf, 2
    142     return

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

    143       s = 0
    144  L3:  t1 = n
    145       n = n int- 1
    146       if t1 int<= 0 goto L4
    147       t3 = va_arg ap, int
    148       s = s int+ t3
    149       goto L3
    150  L4:  return s

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

    151     va_start ap, n
    152     param n
    153     param ap
    154     t1 = call vsum(int, va_list), 2
    155     va_end ap
    156     return t1

============================================================================
 FUNCTION one()        (link name _Z3onev)
============================================================================

 Code: 1 instruction(s)

    157     return 1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 28 temporaries, frame 228 bytes

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
   t4               temp    double                          8      80
   t5               temp    double                          8      88
   t6               temp    const double *                  4      96
   t7               temp    double                          8     104
   t8               temp    class C *                       4     112
   t10              temp    class B *                       4     120
   t12              temp    class C *                       4     128
   t13              temp    int                             4     132
   t15              temp    class C *                       4     140
   t16              temp    int                             4     144
   t17              temp    int                             4     148
   t19              temp    class B *                       4     156
   t20              temp    int                             4     160
   t21              temp    class C *                       4     164
   t22              temp    int                             4     168
   t24              temp    int                             4     176
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
   (8 temporaries no longer used after optimization not shown)

 Code: 90 instruction(s)

    158       t1 = 5.0
    159       t3 = &t1
    160       param t3
    161       t4 = call half(const double &), 1
    162       t5 = 3.0
    163       t6 = &t5
    164       param t6
    165       t7 = call half(const double &), 1
    166       param "%.2f %.2f\n"
    167       param t4
    168       param t7
    169       call printf, 3
    170       t8 = &c
    171       param t8                            (this)
    172       call C::C(), 1
    173       t10 = t8
    174       if t8 ptr== 0 goto L5
    175       t10 = t8 ptr+ 4
    176  L5:  t12 = &c
    177       param t12                           (this)
    178       t13 = call C::sum(), 1
    179       t15 = t12 ptr+ 4
    180       param t15                           (this)
    181       t16 = call B::gb(), 1
    182       t17 = *t10
    183       t19 = t12
    184       if t12 ptr== 0 goto L6
    185       t19 = t12 ptr+ 4
    186  L6:  param t19
    187       t20 = call takeB(class B *), 1
    188       t21 = &c
    189       param t21                           (this)
    190       t22 = call A::ga(), 1
    191       param 0
    192       t24 = call takeB(class B *), 1
    193       param "%d %d %d %d %d %d %d\n"
    194       param t13
    195       param t16
    196       param t17
    197       param t20
    198       param t22
    199       param 1
    200       param t24
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
    211       param t28                           (this)
    212       call Cnt::Cnt(), 1
    213       t29 = &y
    214       param t29                           (this)
    215       call Cnt::Cnt(), 1
    216       t30 = x[0]
    217       t31 = y[0]
    218       param "%d %d %d\n"
    219       param Cnt::made
    220       param t30
    221       param t31
    222       call printf, 4
    223       param 3
    224       param 1
    225       param 2
    226       param 3
    227       t32 = call total(int, ...), 4
    228       param "%.1f %d\n"
    229       param chosen
    230       param t32
    231       call printf, 3
    232       t33 = &d
    233       param t33                           (this)
    234       param 1
    235       call Dog::Dog(int), 2
    236       call one(), 0
    237       param t33                           (this)
    238       call Dog::~Dog(), 1
    239       param "after the block\n"
    240       call printf, 1
    241       t35 = &last
    242       param t35                           (this)
    243       param 2
    244       call Dog::Dog(int), 2
    245       param t35                           (this)
    246       call Dog::~Dog(), 1
    247       return 0


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
