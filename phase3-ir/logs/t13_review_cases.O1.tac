============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_review_cases.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 150 -> 130 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          150 -> 130   (13% fewer)

   constants folded                        4
   algebraic simplifications               0
   common subexpressions                   6
   copies / constants forwarded           18
   temporaries merged away                 3
   dead instructions removed               9
   jumps removed or redirected             5
   unreachable instructions removed        2

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

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class B *                       4       0
   t1               temp    class B *                       4       4

 Code: 5 instruction(s)

    107     param this                          (this)
    108     call A::A(), 1
    109     t1 = this ptr+ 4
    110     *t1 = 2
    111     return

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

    112     t1 = this ptr+ 4
    113     t2 = *t1
    114     return t2

============================================================================
 FUNCTION C::C()        (link name _ZN1CC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class C *                       4       0
   t1               temp    class C *                       4       4

 Code: 5 instruction(s)

    115     param this                          (this)
    116     call B::B(), 1
    117     t1 = this ptr+ 8
    118     *t1 = 3
    119     return

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

    120     t1 = *this
    121     t2 = this ptr+ 4
    122     t3 = *t2
    123     t4 = t1 int+ t3
    124     t5 = this ptr+ 8
    125     t6 = *t5
    126     t7 = t4 int+ t6
    127     return t7

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

    128       if p ptr== 0 goto L1
    129       t2 = p ptr+ 4
    130       t1 = *t2
    131       goto L2
    132  L1:  t1 = -1
    133  L2:  return t1

============================================================================
 FUNCTION Cnt::Cnt()        (link name _ZN3CntC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Cnt *                     4       0
   t1               temp    int                             4       4

 Code: 4 instruction(s)

    134     t1 = Cnt::made int+ 1
    135     Cnt::made = t1
    136     *this = t1
    137     return

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

    138       s = 0
    139  L3:  t1 = n
    140       n = n int- 1
    141       if t1 int<= 0 goto L4
    142       t3 = va_arg ap, int
    143       s = s int+ t3
    144       goto L3
    145  L4:  return s

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

    146     va_start ap, n
    147     param n
    148     param ap
    149     t1 = call vsum(int, va_list), 2
    150     s = t1
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

 Symbol table: 9 parameter(s)/local(s), 21 temporaries, frame 192 bytes

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
   t4               temp    double                          8      72
   t5               temp    double                          8      80
   t6               temp    const double *                  4      88
   t7               temp    double                          8      96
   t8               temp    class C *                       4     104
   t11              temp    int                             4     116
   t13              temp    int                             4     124
   t14              temp    class B *                       4     128
   t15              temp    int                             4     132
   t17              temp    int                             4     140
   t19              temp    int                             4     148
   t21              temp    int                             4     156
   t22              temp    class A *                       4     160
   t23              temp    int                             4     164
   t25              temp    class Cnt *                     4     172
   t26              temp    class Cnt *                     4     176
   t27              temp    int                             4     180
   t28              temp    int                             4     184
   t29              temp    int                             4     188
   (8 temporaries no longer used after optimization not shown)

 Code: 76 instruction(s)

    154     k = 5
    155     t1 = 5.0
    156     t3 = &t1
    157     param t3
    158     t4 = call half(const double &), 1
    159     t5 = 3.0
    160     t6 = &t5
    161     param t6
    162     t7 = call half(const double &), 1
    163     param "%.2f %.2f\n"
    164     param t4
    165     param t7
    166     call printf, 3
    167     t8 = &c
    168     param t8                            (this)
    169     call C::C(), 1
    170     pb = t8
    171     none = 0
    172     nb = 0
    173     param t8                            (this)
    174     t11 = call C::sum(), 1
    175     param t8                            (this)
    176     t13 = call B::gb(), 1
    177     t14 = t8 ptr+ 4
    178     t15 = *t14
    179     param t8
    180     t17 = call takeB(class B *), 1
    181     param t8                            (this)
    182     t19 = call A::ga(), 1
    183     param 0
    184     t21 = call takeB(class B *), 1
    185     param "%d %d %d %d %d %d %d\n"
    186     param t11
    187     param t13
    188     param t15
    189     param t17
    190     param t19
    191     param 1
    192     param t21
    193     call printf, 8
    194     t22 = &first
    195     param t22                           (this)
    196     call A::A(), 1
    197     t23 = c[0]
    198     first[0] = t23
    199     guard = 77
    200     param "%d %d\n"
    201     param t23
    202     param 77
    203     call printf, 3
    204     t25 = &x
    205     param t25                           (this)
    206     call Cnt::Cnt(), 1
    207     t26 = &y
    208     param t26                           (this)
    209     call Cnt::Cnt(), 1
    210     t27 = x[0]
    211     t28 = y[0]
    212     param "%d %d %d\n"
    213     param Cnt::made
    214     param t27
    215     param t28
    216     call printf, 4
    217     param 3
    218     param 1
    219     param 2
    220     param 3
    221     t29 = call total(int, ...), 4
    222     param "%.1f %d\n"
    223     param chosen
    224     param t29
    225     call printf, 3
    226     call one(), 0
    227     param "after the block\n"
    228     call printf, 1
    229     return 0


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
