============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 172 -> 141 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          172 -> 141   (18% fewer)

   constants folded                        1
   algebraic simplifications               2
   common subexpressions                   4
   copies / constants forwarded           36
   temporaries merged away                10
   dead instructions removed              27
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

 Symbol table: 10 parameter(s)/local(s), 46 temporaries, frame 444 bytes

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
   t8               temp    int                             4     112
   t9               temp    int                             4     116
   t10              temp    int                             4     120
   t11              temp    int *                           4     124
   t14              temp    int *                           4     136
   t17              temp    int *                           4     148
   t20              temp    int                             4     160
   t21              temp    int                             4     164
   t22              temp    struct Account *                4     168
   t23              temp    struct Account *                4     172
   t25              temp    struct Account *                4     180
   t26              temp    double                          8     184
   t27              temp    double                          8     192
   t29              temp    double                          8     208
   t30              temp    double                          8     216
   t33              temp    class Dog (*)[3]                4     232
   t34              temp    class Dog (*)[3]                4     236
   t35              temp    class Dog (*)[3]                4     240
   t36              temp    int                             4     244
   t37              temp    int                             4     248
   t38              temp    int                             4     252
   t40              temp    int                             4     260
   t43              temp    int                             4     272
   t47              temp    class Dog *                     4     288
   t49              temp    class Counted                   4     296
   t53              temp    class Counted                   4     312
   t54              temp    class Counted *                 4     316
   t61              temp    struct Account *                4     344
   t62              temp    double                          8     352
   t63              temp    struct Account *                4     360
   t64              temp    double                          8     368
   t65              temp    struct Account *                4     376
   t66              temp    const int *                     4     380
   t67              temp    int                             4     384
   t68              temp    int                             4     388
   t69              temp    int                             4     392
   t70              temp    const int *                     4     396
   t71              temp    int                             4     400
   t73              temp    class Dog *                     4     408
   t75              temp    class Dog *                     4     416
   t77              temp    class Dog *                     4     424
   t79              temp    int                             4     432
   t81              temp    int                             4     440
   (35 temporaries no longer used after optimization not shown)

 Code: 139 instruction(s)

    102        t1 = &keeper
    103        t47 = t1 ptr+ 4
    104        *t47 = 0
    105        *t1 = 42
    106        param "Dog()\n"
    107        call printf, 1
    108        param "start of main\n"
    109        call printf, 1
    110        t2 = &a
    111        *t2 = 1
    112        t49 = a
    113        t49[0] = 50
    114        t4 = a[0]
    115        param "%d %d\n"
    116        param 50
    117        param t4
    118        call printf, 3
    119        b = *t2
    120        b[0] = 7
    121        t54 = &t53
    122        param t54                           (this)
    123        call Counted::Counted(), 1
    124        t53[0] = 5
    125        c = t53
    126        t8 = a[0]
    127        t9 = b[0]
    128        t10 = c[0]
    129        param "%d %d %d\n"
    130        param t8
    131        param t9
    132        param t10
    133        call printf, 4
    134        x = 1
    135        y = 2
    136        if x int<= 2 goto L1
    137        t11 = &x
    138        goto L2
    139  L1:   t11 = &y
    140  L2:   *t11 = 20
    141        if x int>= y goto L3
    142        t14 = &x
    143        goto L4
    144  L3:   t14 = &y
    145  L4:   *t14 = 10
    146        t17 = &x
    147        t20 = *t17
    148        t21 = t20 int+ 5
    149        *t17 = t21
    150        p[0] = 1
    151        p[8] = 10.5
    152        q[0] = 2
    153        q[8] = 99.0
    154        t22 = &p
    155        t23 = &q
    156        t61 = t22 ptr+ 8
    157        t62 = *t61
    158        t63 = t23 ptr+ 8
    159        t64 = *t63
    160        if t62 double>= t64 goto L5
    161        goto L6
    162  L5:   t65 = t22
    163        goto L7
    164  L6:   t65 = t23
    165  L7:   t25 = t65 ptr+ 8
    166        t26 = *t25
    167        t27 = t26 double- 9.0
    168        *t25 = t27
    169        t29 = p[8]
    170        t30 = q[8]
    171        param "%d %d %.1f %.1f\n"
    172        param x
    173        param y
    174        param t29
    175        param t30
    176        call printf, 5
    177        t66 = &primes
    178        t67 = 0
    179        t68 = 0
    180  L8:   if t68 int>= 4 goto L9
    181        t69 = t68 int<< 2
    182        t70 = t66 ptr+ t69
    183        t71 = *t70
    184        t67 = t67 int+ t71
    185        t68 = t68 int+ 1
    186        if t68 int>= 4 goto L9
    187        t69 = t68 int<< 2
    188        t70 = t66 ptr+ t69
    189        t71 = *t70
    190        t67 = t67 int+ t71
    191        t68 = t68 int+ 1
    192        goto L8
    193  L9:   param "%d\n"
    194        param t67
    195        call printf, 2
    196        t33 = &pack
    197        t73 = t33 ptr+ 4
    198        *t73 = 0
    199        *t33 = 42
    200        param "Dog()\n"
    201        call printf, 1
    202        t34 = t33 ptr+ 8
    203        t75 = t34 ptr+ 4
    204        *t75 = 0
    205        *t34 = 42
    206        param "Dog()\n"
    207        call printf, 1
    208        t35 = t33 ptr+ 16
    209        t77 = t35 ptr+ 4
    210        *t77 = 0
    211        *t35 = 42
    212        param "Dog()\n"
    213        call printf, 1
    214        i = 0
    215  L10:  if i int>= 3 goto L11
    216        t36 = i int<< 3                     (w = 8)
    217        t37 = t36 int+ 4
    218        t38 = i int+ 1
    219        pack[t37] = t38
    220        i = t38
    221        if t38 int>= 3 goto L11
    222        t36 = i int<< 3                     (w = 8)
    223        t37 = t36 int+ 4
    224        t38 = i int+ 1
    225        pack[t37] = t38
    226        i = t38
    227        goto L10
    228  L11:  t40 = pack[20]
    229        t79 = *t33
    230        param "%d %d\n"
    231        param t40
    232        param t79
    233        call printf, 3
    234        t43 = keeper[4]
    235        t81 = *t1
    236        param "%d %d\n"
    237        param t43
    238        param t81
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
