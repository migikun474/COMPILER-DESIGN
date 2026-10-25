============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_review_cases.c
   Optimization  : no optimization
   Result        : Three address code generated: 15 function(s), 176 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   class B *                       4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 8 instruction(s)

    127       if p ptr!= 0 goto L1
    128       goto L2
    129  L1:  t2 = *p
    130       t1 = t2
    131       goto L3
    132  L2:  t3 = int- 1
    133       t1 = t3
    134  L3:  return t1

============================================================================
 FUNCTION Cnt::Cnt()        (link name _ZN3CntC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Cnt *                     4       0
   t1               temp    int                             4       4

 Code: 4 instruction(s)

    135     t1 = Cnt::made int+ 1
    136     Cnt::made = t1
    137     *this = Cnt::made
    138     return

============================================================================
 FUNCTION Dog::Dog(int)        (link name _ZN3DogC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   n                param   int                             4       4

 Code: 2 instruction(s)

    139     *this = n
    140     return

============================================================================
 FUNCTION Dog::~Dog()        (link name _ZN3DogD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    141     t1 = *this
    142     param "~Dog(%d)\n"
    143     param t1
    144     call printf, 2
    145     return

============================================================================
 FUNCTION vsum(int, va_list)        (link name _Z4vsumiPv)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               param   va_list                         4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24

 Code: 11 instruction(s)

    146       s = 0
    147  L4:  t1 = n
    148       t2 = n int- 1
    149       n = t2
    150       if t1 int> 0 goto L5
    151       goto L6
    152  L5:  t3 = va_arg ap, int
    153       t4 = s int+ t3
    154       s = t4
    155       goto L4
    156  L6:  return s

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

 Code: 7 instruction(s)

    157     va_start ap, n
    158     param n
    159     param ap
    160     t1 = call vsum(int, va_list), 2
    161     s = t1
    162     va_end ap
    163     return s

============================================================================
 FUNCTION one()        (link name _Z3onev)
============================================================================

 Code: 1 instruction(s)

    164     return 1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 36 temporaries, frame 228 bytes

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
   t2               temp    double                          8      64
   t3               temp    const double *                  4      72
   t4               temp    double                          8      80
   t5               temp    double                          8      88
   t6               temp    const double *                  4      96
   t7               temp    double                          8     104
   t8               temp    class C *                       4     112
   t9               temp    class C *                       4     116
   t10              temp    class B *                       4     120
   t11              temp    class B *                       4     124
   t12              temp    class C *                       4     128
   t13              temp    int                             4     132
   t14              temp    class C *                       4     136
   t15              temp    class C *                       4     140
   t16              temp    int                             4     144
   t17              temp    int                             4     148
   t18              temp    class C *                       4     152
   t19              temp    class B *                       4     156
   t20              temp    int                             4     160
   t21              temp    class C *                       4     164
   t22              temp    int                             4     168
   t23              temp    int                             4     172
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
   t34              temp    class Dog *                     4     216
   t35              temp    class Dog *                     4     220
   t36              temp    class Dog *                     4     224

 Code: 111 instruction(s)

    165        k = 5
    166        t2 = inttodouble k
    167        t1 = t2
    168        t3 = &t1
    169        param t3
    170        t4 = call half(const double &), 1
    171        t5 = 3.0
    172        t6 = &t5
    173        param t6
    174        t7 = call half(const double &), 1
    175        param "%.2f %.2f\n"
    176        param t4
    177        param t7
    178        call printf, 3
    179        t8 = &c
    180        param t8                            (this)
    181        call C::C(), 1
    182        t9 = &c
    183        t10 = t9
    184        if t9 ptr== 0 goto L7
    185        t10 = t9 ptr+ 4
    186  L7:   pb = t10
    187        none = 0
    188        t11 = none
    189        if none ptr== 0 goto L8
    190        t11 = none ptr+ 4
    191  L8:   nb = t11
    192        t12 = &c
    193        param t12                           (this)
    194        t13 = call C::sum(), 1
    195        t14 = &c
    196        t15 = t14 ptr+ 4
    197        param t15                           (this)
    198        t16 = call B::gb(), 1
    199        t17 = *pb
    200        t18 = &c
    201        t19 = t18
    202        if t18 ptr== 0 goto L9
    203        t19 = t18 ptr+ 4
    204  L9:   param t19
    205        t20 = call takeB(class B *), 1
    206        t21 = &c
    207        param t21                           (this)
    208        t22 = call A::ga(), 1
    209        if nb ptr== 0 goto L10
    210        t23 = 0
    211        goto L11
    212  L10:  t23 = 1
    213  L11:  param nb
    214        t24 = call takeB(class B *), 1
    215        param "%d %d %d %d %d %d %d\n"
    216        param t13
    217        param t16
    218        param t17
    219        param t20
    220        param t22
    221        param t23
    222        param t24
    223        call printf, 8
    224        t25 = &first
    225        t26 = c[0]
    226        *t25 = t26
    227        guard = 77
    228        t27 = first[0]
    229        param "%d %d\n"
    230        param t27
    231        param guard
    232        call printf, 3
    233        t28 = &x
    234        param t28                           (this)
    235        call Cnt::Cnt(), 1
    236        t29 = &y
    237        param t29                           (this)
    238        call Cnt::Cnt(), 1
    239        t30 = x[0]
    240        t31 = y[0]
    241        param "%d %d %d\n"
    242        param Cnt::made
    243        param t30
    244        param t31
    245        call printf, 4
    246        param 3
    247        param 1
    248        param 2
    249        param 3
    250        t32 = call total(int, ...), 4
    251        param "%.1f %d\n"
    252        param chosen
    253        param t32
    254        call printf, 3
    255        t33 = &d
    256        param t33                           (this)
    257        param 1
    258        call Dog::Dog(int), 2
    259        if k int!= 0 goto L12
    260        goto L13
    261  L12:  call one(), 0
    262        goto L13
    263  L13:  t34 = &d
    264        param t34                           (this)
    265        call Dog::~Dog(), 1
    266        param "after the block\n"
    267        call printf, 1
    268        t35 = &last
    269        param t35                           (this)
    270        param 2
    271        call Dog::Dog(int), 2
    272        t36 = &last
    273        param t36                           (this)
    274        call Dog::~Dog(), 1
    275        return 0


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
