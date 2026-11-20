============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_review_cases.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 150 -> 125 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          150 -> 125   (16% fewer)

   constants folded                        5
   algebraic simplifications               0
   common subexpressions                  12
   copies / constants forwarded           46
   temporaries merged away                 5
   dead instructions removed              32
   jumps removed or redirected             6
   unreachable instructions removed        5
   propagated across blocks                3
   dead assignments removed                9
   calls inlined                          14
   tail calls turned into jumps            0
   common subexpressions across blocks      1

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

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class B *                       4       0
   t1               temp    class B *                       4       4
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    107     *this = 1
    108     t1 = this ptr+ 4
    109     *t1 = 2
    110     return

============================================================================
 FUNCTION B::gb()        (link name _ZN1B2gbEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class B *                       4       0
   t1               temp    class B *                       4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    111     t1 = this ptr+ 4
    112     t2 = *t1
    113     return t2

============================================================================
 FUNCTION C::C()        (link name _ZN1CC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class C *                       4       0
   t1               temp    class C *                       4       4
   t3               temp    class B *                       4      12
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    114     param this                          (this)
    115     call A::A(), 1
    116     t3 = this ptr+ 4
    117     *t3 = 2
    118     t1 = this ptr+ 8
    119     *t1 = 3
    120     return

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

    121     t1 = *this
    122     t2 = this ptr+ 4
    123     t3 = *t2
    124     t4 = t1 int+ t3
    125     t5 = this ptr+ 8
    126     t6 = *t5
    127     t7 = t4 int+ t6
    128     return t7

============================================================================
 FUNCTION takeB(class B *)        (link name _Z5takeBP1B)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   class B *                       4       0
   t1               temp    int                             4       4
   t2               temp    class B *                       4       8
   (2 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    129       if p ptr== 0 goto L1
    130       t2 = p ptr+ 4
    131       t1 = *t2
    132       goto L2
    133  L1:  t1 = -1
    134  L2:  return t1

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
    137     *this = t1
    138     return

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

    139       s = 0
    140  L3:  t1 = n
    141       n = n int- 1
    142       if t1 int<= 0 goto L4
    143       t3 = va_arg ap, int
    144       s = s int+ t3
    145       goto L3
    146  L4:  return s

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

    147     va_start ap, n
    148     param n
    149     param ap
    150     t1 = call vsum(int, va_list), 2
    151     va_end ap
    152     return t1

============================================================================
 FUNCTION one()        (link name _Z3onev)
============================================================================

 Code: 1 instruction(s)

    153     return 1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 26 temporaries, frame 344 bytes

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
   t1               temp    double                          8      48
   t3               temp    const double *                  4      64
   t5               temp    double                          8      80
   t6               temp    const double *                  4      88
   t8               temp    class C *                       4     104
   t11              temp    int                             4     116
   t19              temp    int                             4     148
   t22              temp    class A *                       4     160
   t23              temp    int                             4     164
   t25              temp    class Cnt *                     4     172
   t26              temp    class Cnt *                     4     176
   t27              temp    int                             4     180
   t28              temp    int                             4     184
   t29              temp    int                             4     188
   t31              temp    double                          8     200
   t32              temp    double                          8     208
   t34              temp    double                          8     224
   t35              temp    double                          8     232
   t37              temp    class C *                       4     244
   t39              temp    int                             4     252
   t40              temp    class C *                       4     256
   t41              temp    int                             4     260
   t42              temp    int                             4     264
   t51              temp    int                             4     300
   t59              temp    int                             4     332
   t61              temp    int                             4     340
   (35 temporaries no longer used after optimization not shown)

 Code: 71 instruction(s)

    154       t1 = 5.0
    155       t3 = &t1
    156       t31 = *t3
    157       t32 = t31 double/ 2.0
    158       t5 = 3.0
    159       t6 = &t5
    160       t34 = *t6
    161       t35 = t34 double/ 2.0
    162       param "%.2f %.2f\n"
    163       param t32
    164       param t35
    165       call printf, 3
    166       t8 = &c
    167       param t8                            (this)
    168       call B::B(), 1
    169       t37 = t8 ptr+ 8
    170       *t37 = 3
    171       t39 = *t8
    172       t40 = t8 ptr+ 4
    173       t41 = *t40
    174       t42 = t39 int+ t41
    175       t11 = t42 int+ 3
    176       if t8 ptr== 0 goto L5
    177       t51 = *t40
    178       goto L6
    179  L5:  t51 = -1
    180  L6:  t19 = *t8
    181       param "%d %d %d %d %d %d %d\n"
    182       param t11
    183       param t41
    184       param t41
    185       param t51
    186       param t19
    187       param 1
    188       param -1
    189       call printf, 8
    190       t22 = &first
    191       *t22 = 1
    192       t23 = c[0]
    193       first[0] = t23
    194       param "%d %d\n"
    195       param t23
    196       param 77
    197       call printf, 3
    198       t25 = &x
    199       t59 = Cnt::made int+ 1
    200       Cnt::made = t59
    201       *t25 = t59
    202       t26 = &y
    203       t61 = Cnt::made int+ 1
    204       Cnt::made = t61
    205       *t26 = t61
    206       t27 = x[0]
    207       t28 = y[0]
    208       param "%d %d %d\n"
    209       param Cnt::made
    210       param t27
    211       param t28
    212       call printf, 4
    213       param 3
    214       param 1
    215       param 2
    216       param 3
    217       t29 = call total(int, ...), 4
    218       param "%.1f %d\n"
    219       param chosen
    220       param t29
    221       call printf, 3
    222       param "after the block\n"
    223       call printf, 1
    224       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   half               function      double (const double &)    -           4    -    2  _Z4halfRKd; defined
   A                  class_tag     class A                    -           6    -    0  size 4
   B                  class_tag     class B                    -           7    -    0  size 8, public base A
   C                  class_tag     class C                    -           8    -    0  size 12, public base B
   takeB              function      int (class B *)            -          14    -    2  _Z5takeBP1B; defined
   Cnt                class_tag     class Cnt                  -          16    -    0  size 4
   chosen             variable      double                     global     25    8    1  
   vsum               function      int (int, va_list)         -          27    -    1  _Z4vsumiPv; defined
   total              function      int (int, ...)             -          32    -    1  _Z5totaliz; defined
   one                function      int (void)                 -          40    -    1  _Z3onev; defined
   main               function      int (void)                 -          42    -    0  defined

 scope: global > half()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     const double &             param       4    4    1  v.1

 scope: global > class A
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member      6    4    6  A::a; public, offset 0
   A                  constructor   void (void)                -           6    -    1  _ZN1AC1Ev; public
   ga                 method        int (void)                 -           6    -    1  _ZN1A2gaEv; public, defined

 scope: global > class B
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   b                  field         int                        member      7    4    5  B::b; public, offset 4
   B                  constructor   void (void)                -           7    -    0  _ZN1BC1Ev; public
   gb                 method        int (void)                 -           7    -    1  _ZN1B2gbEv; public, defined

 scope: global > class C
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  field         int                        member     10    4    2  C::c; public, offset 8
   C                  constructor   void (void)                -          11    -    1  _ZN1CC1Ev; public
   sum                method        int (void)                 -          12    -    1  _ZN1C3sumEv; public, defined

 scope: global > takeB()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     class B *                  param      14    4    2  p.2

 scope: global > class Cnt
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   made               field         int                        static     18    4    3  Cnt::made; public, static
   id                 field         int                        member     19    4    3  Cnt::id; public, offset 0
   Cnt                constructor   void (void)                -          20    -    2  _ZN3CntC1Ev; public

 scope: global > vsum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      27    4    1  n.3
   ap                 parameter     va_list                    param      27    4    1  ap.4
   s                  variable      int                        local      28    4    2  s.5

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      32    4    2  n.6
   ap                 variable      va_list                    local      33    4    3  ap.7
   s                  variable      int                        local      35    4    1  s.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      43    4    2  k.9
   c                  variable      class C                    local      46   12    6  c.10
   pb                 variable      class B *                  local      47    4    1  pb.11
   none               variable      class C *                  local      48    4    1  none.12
   nb                 variable      class B *                  local      49    4    2  nb.13
   first              variable      class A                    local      51    4    2  first.14
   guard              variable      int                        local      53    4    1  guard.15
   x                  variable      class Cnt                  local      56    4    1  x.16
   y                  variable      class Cnt                  local      56    4    1  y.17

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class A: size 4, align 4
    +0  int a  [public]
class B: size 8, align 4
    (base A, public)
    +4  int b  [public]
class C: size 12, align 4
    (base B, public)
    +8  int c  [public]
class Cnt: size 4, align 4
    static  int made  [public]
    +0  int id  [public]
