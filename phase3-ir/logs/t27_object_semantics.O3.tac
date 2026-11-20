============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 172 -> 170 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          172 -> 170   (1% fewer)

   constants folded                        1
   algebraic simplifications               2
   common subexpressions                   4
   copies / constants forwarded           35
   temporaries merged away                10
   dead instructions removed              27
   jumps removed or redirected             6
   unreachable instructions removed        1
   propagated across blocks                2
   dead assignments removed                3
   calls inlined                          14
   tail calls turned into jumps            0
   common subexpressions across blocks      2

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
 FUNCTION take(class Counted)        (link name _Z4take7Counted)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted                   4       0
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    102     c[0] = 50
    103     return 50

============================================================================
 FUNCTION give(class Counted &)        (link name _Z4giveR7Counted)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted &                 4       0
   t1               temp    class Counted                   4       4

 Code: 2 instruction(s)

    104     t1 = *c
    105     return t1

============================================================================
 FUNCTION fresh(int)        (link name _Z5freshi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   local            local   class Counted                   4       4
   t1               temp    class Counted *                 4       8
   (1 temporary no longer used after optimization not shown)

 Code: 4 instruction(s)

    106     t1 = &local
    107     *t1 = 1
    108     local[0] = x
    109     return local

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4

 Code: 6 instruction(s)

    110     t1 = this ptr+ 4
    111     *t1 = 0
    112     *this = 42
    113     param "Dog()\n"
    114     call printf, 1
    115     return

============================================================================
 FUNCTION peek(const class Dog &)        (link name _Z4peekRK3Dog)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                param   const class Dog &               4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    116     t1 = *d
    117     return t1

============================================================================
 FUNCTION sum(const int *)        (link name _Z3sumPKi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   const int *                     4       0
   s                local   int                             4       4
   i                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    const int *                     4      16
   t3               temp    int                             4      20
   (2 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    118       s = 0
    119       i = 0
    120  L1:  if i int>= 4 goto L2
    121       t1 = i int<< 2
    122       t2 = r ptr+ t1
    123       t3 = *t2
    124       s = s int+ t3
    125       i = i int+ 1
    126       goto L1
    127  L2:  return s

============================================================================
 FUNCTION richer(struct Account &, struct Account &)        (link name _Z6richerR7AccountS0_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   struct Account &                4       0
   b                param   struct Account &                4       4
   t1               temp    struct Account *                4       8
   t2               temp    struct Account *                4      12
   t3               temp    double                          8      16
   t4               temp    struct Account *                4      24
   t5               temp    double                          8      32

 Code: 10 instruction(s)

    128       t2 = a ptr+ 8
    129       t3 = *t2
    130       t4 = b ptr+ 8
    131       t5 = *t4
    132       if t3 double>= t5 goto L3
    133       goto L4
    134  L3:  t1 = a
    135       goto L5
    136  L4:  t1 = b
    137  L5:  return t1

============================================================================
 FUNCTION pick(int, int &, int &)        (link name _Z4pickiRiS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   which            param   int                             4       0
   a                param   int &                           4       4
   b                param   int &                           4       8
   t1               temp    int *                           4      12

 Code: 5 instruction(s)

    138       if which int== 0 goto L6
    139       t1 = a
    140       goto L7
    141  L6:  t1 = b
    142  L7:  return t1

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

 Code: 127 instruction(s)

    143        t1 = &keeper
    144        t47 = t1 ptr+ 4
    145        *t47 = 0
    146        *t1 = 42
    147        param "Dog()\n"
    148        call printf, 1
    149        param "start of main\n"
    150        call printf, 1
    151        t2 = &a
    152        *t2 = 1
    153        t49 = a
    154        t49[0] = 50
    155        t4 = a[0]
    156        param "%d %d\n"
    157        param 50
    158        param t4
    159        call printf, 3
    160        b = *t2
    161        b[0] = 7
    162        t54 = &t53
    163        param t54                           (this)
    164        call Counted::Counted(), 1
    165        t53[0] = 5
    166        c = t53
    167        t8 = a[0]
    168        t9 = b[0]
    169        t10 = c[0]
    170        param "%d %d %d\n"
    171        param t8
    172        param t9
    173        param t10
    174        call printf, 4
    175        x = 1
    176        y = 2
    177        if x int<= 2 goto L8
    178        t11 = &x
    179        goto L9
    180  L8:   t11 = &y
    181  L9:   *t11 = 20
    182        if x int>= y goto L10
    183        t14 = &x
    184        goto L11
    185  L10:  t14 = &y
    186  L11:  *t14 = 10
    187        t17 = &x
    188        t20 = *t17
    189        t21 = t20 int+ 5
    190        *t17 = t21
    191        p[0] = 1
    192        p[8] = 10.5
    193        q[0] = 2
    194        q[8] = 99.0
    195        t22 = &p
    196        t23 = &q
    197        t61 = t22 ptr+ 8
    198        t62 = *t61
    199        t63 = t23 ptr+ 8
    200        t64 = *t63
    201        if t62 double>= t64 goto L12
    202        goto L13
    203  L12:  t65 = t22
    204        goto L14
    205  L13:  t65 = t23
    206  L14:  t25 = t65 ptr+ 8
    207        t26 = *t25
    208        t27 = t26 double- 9.0
    209        *t25 = t27
    210        t29 = p[8]
    211        t30 = q[8]
    212        param "%d %d %.1f %.1f\n"
    213        param x
    214        param y
    215        param t29
    216        param t30
    217        call printf, 5
    218        t66 = &primes
    219        t67 = 0
    220        t68 = 0
    221  L15:  if t68 int>= 4 goto L16
    222        t69 = t68 int<< 2
    223        t70 = t66 ptr+ t69
    224        t71 = *t70
    225        t67 = t67 int+ t71
    226        t68 = t68 int+ 1
    227        goto L15
    228  L16:  param "%d\n"
    229        param t67
    230        call printf, 2
    231        t33 = &pack
    232        t73 = t33 ptr+ 4
    233        *t73 = 0
    234        *t33 = 42
    235        param "Dog()\n"
    236        call printf, 1
    237        t34 = t33 ptr+ 8
    238        t75 = t34 ptr+ 4
    239        *t75 = 0
    240        *t34 = 42
    241        param "Dog()\n"
    242        call printf, 1
    243        t35 = t33 ptr+ 16
    244        t77 = t35 ptr+ 4
    245        *t77 = 0
    246        *t35 = 42
    247        param "Dog()\n"
    248        call printf, 1
    249        i = 0
    250  L17:  if i int>= 3 goto L18
    251        t36 = i int<< 3                     (w = 8)
    252        t37 = t36 int+ 4
    253        t38 = i int+ 1
    254        pack[t37] = t38
    255        i = t38
    256        goto L17
    257  L18:  t40 = pack[20]
    258        t79 = *t33
    259        param "%d %d\n"
    260        param t40
    261        param t79
    262        call printf, 3
    263        t43 = keeper[4]
    264        t81 = *t1
    265        param "%d %d\n"
    266        param t43
    267        param t81
    268        call printf, 3
    269        return 0


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
