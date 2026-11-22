============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t13_review_cases.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 150 -> 94 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          150 -> 94   (37% fewer)

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
   loops unrolled                          1
   unreachable functions removed           9

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
 FUNCTION B::B()        (link name _ZN1BC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class B *                       4       0
   t1               temp    class B *                       4       4
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    100     *this = 1
    101     t1 = this ptr+ 4
    102     *t1 = 2
    103     return

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

 Code: 13 instruction(s)

    104       s = 0
    105  L1:  t1 = n
    106       n = n int- 1
    107       if t1 int<= 0 goto L2
    108       t3 = va_arg ap, int
    109       s = s int+ t3
    110       t1 = n
    111       n = n int- 1
    112       if t1 int<= 0 goto L2
    113       t3 = va_arg ap, int
    114       s = s int+ t3
    115       goto L1
    116  L2:  return s

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

    117     va_start ap, n
    118     param n
    119     param ap
    120     t1 = call vsum(int, va_list), 2
    121     va_end ap
    122     return t1

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

    123       t1 = 5.0
    124       t3 = &t1
    125       t31 = *t3
    126       t32 = t31 double/ 2.0
    127       t5 = 3.0
    128       t6 = &t5
    129       t34 = *t6
    130       t35 = t34 double/ 2.0
    131       param "%.2f %.2f\n"
    132       param t32
    133       param t35
    134       call printf, 3
    135       t8 = &c
    136       param t8                            (this)
    137       call B::B(), 1
    138       t37 = t8 ptr+ 8
    139       *t37 = 3
    140       t39 = *t8
    141       t40 = t8 ptr+ 4
    142       t41 = *t40
    143       t42 = t39 int+ t41
    144       t11 = t42 int+ 3
    145       if t8 ptr== 0 goto L3
    146       t51 = *t40
    147       goto L4
    148  L3:  t51 = -1
    149  L4:  t19 = *t8
    150       param "%d %d %d %d %d %d %d\n"
    151       param t11
    152       param t41
    153       param t41
    154       param t51
    155       param t19
    156       param 1
    157       param -1
    158       call printf, 8
    159       t22 = &first
    160       *t22 = 1
    161       t23 = c[0]
    162       first[0] = t23
    163       param "%d %d\n"
    164       param t23
    165       param 77
    166       call printf, 3
    167       t25 = &x
    168       t59 = Cnt::made int+ 1
    169       Cnt::made = t59
    170       *t25 = t59
    171       t26 = &y
    172       t61 = Cnt::made int+ 1
    173       Cnt::made = t61
    174       *t26 = t61
    175       t27 = x[0]
    176       t28 = y[0]
    177       param "%d %d %d\n"
    178       param Cnt::made
    179       param t27
    180       param t28
    181       call printf, 4
    182       param 3
    183       param 1
    184       param 2
    185       param 3
    186       t29 = call total(int, ...), 4
    187       param "%.1f %d\n"
    188       param chosen
    189       param t29
    190       call printf, 3
    191       param "after the block\n"
    192       call printf, 1
    193       return 0


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
