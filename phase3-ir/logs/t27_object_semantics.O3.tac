============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 174 -> 141 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          174 -> 141   (18% fewer)

   constants folded                        1
   algebraic simplifications               2
   common subexpressions                   4
   copies / constants forwarded           36
   temporaries merged away                10
   dead instructions removed              29
   jumps removed or redirected             6
   unreachable instructions removed        1
   propagated across blocks                2
   dead assignments removed                3
   calls inlined                          14
   tail calls turned into jumps            0
   common subexpressions across blocks      2
   loops unrolled                          3
   unreachable functions removed           8

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   keeper           class Dog                       8  0
   primes           const int[4]                   16  { +0: 2, +4: 3, +8: 5, +12: 7 }

 As three address code (initial values, in place before main runs):

    keeper[...] = 0                (zero-initialized)
    primes[0] = 2
    primes[4] = 3
    primes[8] = 5
    primes[12] = 7

============================================================================
 FUNCTION Counted::Counted()        (link name _ZN7CountedC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counted *                 4       0

 Code: 2 instruction(s)

    100     *this = 1
    101     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 46 temporaries, frame 452 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   class Counted                   4       0
   b                local   class Counted                   4       4
   c                local   class Counted                   4       8
   x                local   int                             4      12
   y                local   int                             4      16
   r                local   int &                           4      20
   p                local   struct Account                 16      24
   q                local   struct Account                 16      40
   pack             local   class Dog[3]                   24      56
   i                local   int                             4      80
   t1               temp    class Dog *                     4      84
   t2               temp    class Counted *                 4      88
   t4               temp    int                             4      96
   t10              temp    int                             4     120
   t11              temp    int                             4     124
   t12              temp    int                             4     128
   t13              temp    int *                           4     132
   t16              temp    int *                           4     144
   t19              temp    int *                           4     156
   t22              temp    int                             4     168
   t23              temp    int                             4     172
   t24              temp    struct Account *                4     176
   t25              temp    struct Account *                4     180
   t27              temp    struct Account *                4     188
   t28              temp    double                          8     192
   t29              temp    double                          8     200
   t31              temp    double                          8     216
   t32              temp    double                          8     224
   t35              temp    class Dog (*)[3]                4     240
   t36              temp    class Dog (*)[3]                4     244
   t37              temp    class Dog (*)[3]                4     248
   t38              temp    int                             4     252
   t39              temp    int                             4     256
   t40              temp    int                             4     260
   t42              temp    int                             4     268
   t45              temp    int                             4     280
   t49              temp    class Dog *                     4     296
   t51              temp    class Counted                   4     304
   t55              temp    class Counted                   4     320
   t56              temp    class Counted *                 4     324
   t63              temp    struct Account *                4     352
   t64              temp    double                          8     360
   t65              temp    struct Account *                4     368
   t66              temp    double                          8     376
   t67              temp    struct Account *                4     384
   t68              temp    const int *                     4     388
   t69              temp    int                             4     392
   t70              temp    int                             4     396
   t71              temp    int                             4     400
   t72              temp    const int *                     4     404
   t73              temp    int                             4     408
   t75              temp    class Dog *                     4     416
   t77              temp    class Dog *                     4     424
   t79              temp    class Dog *                     4     432
   t81              temp    int                             4     440
   t83              temp    int                             4     448
   (37 temporaries no longer used after optimization not shown)

 Code: 139 instruction(s)

    102        t1 = &keeper
    103        t49 = t1 ptr+ 4
    104        *t49 = 0
    105        *t1 = 42
    106        param "Dog()\n"
    107        call printf, 1
    108        param "start of main\n"
    109        call printf, 1
    110        t2 = &a
    111        *t2 = 1
    112        t51 = a
    113        t51[0] = 50
    114        t4 = a[0]
    115        param "%d %d\n"
    116        param 50
    117        param t4
    118        call printf, 3
    119        b = *t2
    120        b[0] = 7
    121        t56 = &t55
    122        param t56                           (this)
    123        call Counted::Counted(), 1
    124        t55[0] = 5
    125        c = t55
    126        t10 = a[0]
    127        t11 = b[0]
    128        t12 = c[0]
    129        param "%d %d %d\n"
    130        param t10
    131        param t11
    132        param t12
    133        call printf, 4
    134        x = 1
    135        y = 2
    136        if x int<= 2 goto L1
    137        t13 = &x
    138        goto L2
    139  L1:   t13 = &y
    140  L2:   *t13 = 20
    141        if x int>= y goto L3
    142        t16 = &x
    143        goto L4
    144  L3:   t16 = &y
    145  L4:   *t16 = 10
    146        t19 = &x
    147        t22 = *t19
    148        t23 = t22 int+ 5
    149        *t19 = t23
    150        p[0] = 1
    151        p[8] = 10.5
    152        q[0] = 2
    153        q[8] = 99.0
    154        t24 = &p
    155        t25 = &q
    156        t63 = t24 ptr+ 8
    157        t64 = *t63
    158        t65 = t25 ptr+ 8
    159        t66 = *t65
    160        if t64 double>= t66 goto L5
    161        goto L6
    162  L5:   t67 = t24
    163        goto L7
    164  L6:   t67 = t25
    165  L7:   t27 = t67 ptr+ 8
    166        t28 = *t27
    167        t29 = t28 double- 9.0
    168        *t27 = t29
    169        t31 = p[8]
    170        t32 = q[8]
    171        param "%d %d %.1f %.1f\n"
    172        param x
    173        param y
    174        param t31
    175        param t32
    176        call printf, 5
    177        t68 = &primes
    178        t69 = 0
    179        t70 = 0
    180  L8:   if t70 int>= 4 goto L9
    181        t71 = t70 int<< 2
    182        t72 = t68 ptr+ t71
    183        t73 = *t72
    184        t69 = t69 int+ t73
    185        t70 = t70 int+ 1
    186        if t70 int>= 4 goto L9
    187        t71 = t70 int<< 2
    188        t72 = t68 ptr+ t71
    189        t73 = *t72
    190        t69 = t69 int+ t73
    191        t70 = t70 int+ 1
    192        goto L8
    193  L9:   param "%d\n"
    194        param t69
    195        call printf, 2
    196        t35 = &pack
    197        t75 = t35 ptr+ 4
    198        *t75 = 0
    199        *t35 = 42
    200        param "Dog()\n"
    201        call printf, 1
    202        t36 = t35 ptr+ 8
    203        t77 = t36 ptr+ 4
    204        *t77 = 0
    205        *t36 = 42
    206        param "Dog()\n"
    207        call printf, 1
    208        t37 = t35 ptr+ 16
    209        t79 = t37 ptr+ 4
    210        *t79 = 0
    211        *t37 = 42
    212        param "Dog()\n"
    213        call printf, 1
    214        i = 0
    215  L10:  if i int>= 3 goto L11
    216        t38 = i int<< 3                     (w = 8)
    217        t39 = t38 int+ 4
    218        t40 = i int+ 1
    219        pack[t39] = t40
    220        i = t40
    221        if t40 int>= 3 goto L11
    222        t38 = i int<< 3                     (w = 8)
    223        t39 = t38 int+ 4
    224        t40 = i int+ 1
    225        pack[t39] = t40
    226        i = t40
    227        goto L10
    228  L11:  t42 = pack[20]
    229        t81 = *t35
    230        param "%d %d\n"
    231        param t42
    232        param t81
    233        call printf, 3
    234        t45 = keeper[4]
    235        t83 = *t1
    236        param "%d %d\n"
    237        param t45
    238        param t83
    239        call printf, 3
    240        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Counted            class_tag     class Counted              -           7    -    0  size 4
   take               function      int (class Counted)        -          12    -    1  _Z4take7Counted; defined
   give               function      class Counted (class Counted &) -          13    -    1  _Z4giveR7Counted; defined
   fresh              function      class Counted (int)        -          14    -    1  _Z5freshi; defined
   Dog                class_tag     class Dog                  -          16    -    0  size 8
   peek               function      int (const class Dog &)    -          21    -    2  _Z4peekRK3Dog; defined
   keeper             variable      class Dog                  global     24    8    2  
   Row                typedef       int[4]                     -          26    -    0  
   primes             variable      const int[4]               global     27   16    1  
   sum                function      int (const int *)          -          28    -    1  _Z3sumPKi; defined
   Account            struct_tag    struct Account             -          30    -    0  size 16
   richer             function      struct Account &(struct Account &, struct Account &) -          31    -    1  _Z6richerR7AccountS0_; defined
   pick               function      int &(int, int &, int &)   -          32    -    1  _Z4pickiRiS_; defined
   main               function      int (void)                 -          34    -    0  defined

 scope: global > class Counted
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  field         int                        member      9    4    9  Counted::v; public, offset 0
   Counted            constructor   void (void)                -          10    -    2  _ZN7CountedC1Ev; public

 scope: global > take()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Counted              param      12    4    2  c.1

 scope: global > give()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Counted &            param      13    4    1  c.2

 scope: global > fresh()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      14    4    1  x.3
   local              variable      class Counted              local      14    4    2  local.4

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   secret             field         int                        member     17    4    2  Dog::secret; private, offset 0
   id                 field         int                        member     19    4    4  Dog::id; public, offset 4
   Dog                constructor   void (void)                -          20    -    2  _ZN3DogC1Ev; public

 scope: global > peek()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  parameter     const class Dog &          param      23    4    1  d.5

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     const int *                param      28    4    1  r.6
   s                  variable      int                        local      28    4    2  s.7

 scope: global > sum() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      28    4    3  i.8

 scope: global > struct Account
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     30    4    0  Account::id; public, offset 0
   balance            field         double                     member     30    8    5  Account::balance; public, offset 8

 scope: global > richer()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     struct Account &           param      31    4    2  a.9
   b                  parameter     struct Account &           param      31    4    2  b.10

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   which              parameter     int                        param      32    4    1  which.11
   a                  parameter     int &                      param      32    4    1  a.12
   b                  parameter     int &                      param      32    4    1  b.13

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      class Counted              local      36    4    4  a.14
   b                  variable      class Counted              local      38    4    2  b.15
   c                  variable      class Counted              local      40    4    1  c.16
   x                  variable      int                        local      43    4    6  x.17
   y                  variable      int                        local      43    4    6  y.18
   r                  variable      int &                      local      44    4    1  r.19
   p                  variable      struct Account             local      48   16    2  p.20
   q                  variable      struct Account             local      48   16    2  q.21

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pack               variable      class Dog[3]               local      54   24    3  pack.22

 scope: global > main() > block > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      55    4    4  i.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Counted: size 4, align 4
    +0  int v  [public]
class Dog: size 8, align 4
    +0  int secret  [private]
    +4  int id  [public]
struct Account: size 16, align 8
    +0  int id  [public]
    +8  double balance  [public]
