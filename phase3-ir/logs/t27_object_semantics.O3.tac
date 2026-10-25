============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 213 -> 202 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          213 -> 202   (5% fewer)

   constants folded                        2
   algebraic simplifications               3
   common subexpressions                   7
   copies / constants forwarded           52
   temporaries merged away                 9
   dead instructions removed              48
   jumps removed or redirected             6
   unreachable instructions removed        1
   propagated across blocks                2
   dead assignments removed                3
   calls inlined                          21
   tail calls turned into jumps            0
   common subexpressions across blocks      4
   instructions moved out of loops         0

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   keeper           class Dog                       4  0
   primes           const int[4]                   16  { +0: 2, +4: 3, +8: 5, +12: 7 }

 As three address code (initial values, in place before main runs):

    keeper[...] = 0                (zero-initialized)
    primes[0] = 2
    primes[4] = 3
    primes[8] = 5
    primes[12] = 7

============================================================================
 FUNCTION Counted::Counted(int)        (link name _ZN7CountedC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counted *                 4       0
   x                param   int                             4       4

 Code: 2 instruction(s)

    100     *this = x
    101     return

============================================================================
 FUNCTION Counted::Counted(const class Counted &)        (link name _ZN7CountedC1ERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Counted *                 4       0
   o                param   const class Counted &           4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 8 instruction(s)

    102     t1 = *o
    103     t2 = t1 int+ 100
    104     *this = t2
    105     t3 = *o
    106     param "copy of %d\n"
    107     param t3
    108     call printf, 2
    109     return

============================================================================
 FUNCTION take(class Counted)        (link name _Z4take7Counted)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted                   4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    110     t1 = c[0]
    111     return t1

============================================================================
 FUNCTION give(class Counted &)        (link name _Z4giveR7Counted)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted &                 4       0
   t1               temp    class Counted                   4       4
   t2               temp    class Counted *                 4       8
   t5               temp    int                             4      20
   t6               temp    int                             4      24
   t7               temp    int                             4      28
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    112     t2 = &t1
    113     t5 = *c
    114     t6 = t5 int+ 100
    115     *t2 = t6
    116     t7 = *c
    117     param "copy of %d\n"
    118     param t7
    119     call printf, 2
    120     return t1

============================================================================
 FUNCTION fresh(int)        (link name _Z5freshi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   local            local   class Counted                   4       4
   t1               temp    class Counted *                 4       8
   (2 temporaries no longer used after optimization not shown)

 Code: 3 instruction(s)

    121     t1 = &local
    122     *t1 = x
    123     return local

============================================================================
 FUNCTION Other::Other()        (link name _ZN5OtherC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Other *                   4       0

 Code: 2 instruction(s)

    124     *this = 7
    125     return

============================================================================
 FUNCTION Vec::Vec(class Other)        (link name _ZN3VecC1E5Other)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Other                     4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 4 instruction(s)

    126     t1 = o[0]
    127     t2 = t1 int<< 1
    128     *this = t2
    129     return

============================================================================
 FUNCTION Vec::Vec(int)        (link name _ZN3VecC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4

 Code: 2 instruction(s)

    130     *this = k
    131     return

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0

 Code: 2 instruction(s)

    132     *this = 0
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
    137     param "~Dog %d\n"
    138     param t1
    139     call printf, 2
    140     return

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

    141       s = 0
    142       i = 0
    143  L1:  if i int>= 4 goto L2
    144       t1 = i int<< 2
    145       t2 = r ptr+ t1
    146       t3 = *t2
    147       s = s int+ t3
    148       i = i int+ 1
    149       goto L1
    150  L2:  return s

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

    151       t2 = a ptr+ 8
    152       t3 = *t2
    153       t4 = b ptr+ 8
    154       t5 = *t4
    155       if t3 double>= t5 goto L3
    156       goto L4
    157  L3:  t1 = a
    158       goto L5
    159  L4:  t1 = b
    160  L5:  return t1

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

    161       if which int== 0 goto L6
    162       t1 = a
    163       goto L7
    164  L6:  t1 = b
    165  L7:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 54 temporaries, frame 552 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   class Counted                   4       0
   b                local   class Counted                   4       4
   c                local   class Counted                   4       8
   o                local   class Other                     4      12
   f                local   class Vec                       4      16
   g                local   class Vec                       4      20
   x                local   int                             4      24
   y                local   int                             4      28
   r                local   int &                           4      32
   p                local   struct Account                 16      40
   q                local   struct Account                 16      56
   pack             local   class Dog[3]                   12      72
   i                local   int                             4      84
   t1               temp    class Dog *                     4      88
   t2               temp    class Counted *                 4      92
   t3               temp    class Counted                   4      96
   t4               temp    class Counted *                 4     100
   t14              temp    int                             4     140
   t15              temp    int                             4     144
   t16              temp    int                             4     148
   t17              temp    class Other *                   4     152
   t18              temp    class Vec *                     4     156
   t19              temp    class Vec *                     4     160
   t20              temp    int                             4     164
   t21              temp    int                             4     168
   t22              temp    int *                           4     172
   t25              temp    int *                           4     184
   t28              temp    int *                           4     196
   t31              temp    int                             4     208
   t32              temp    int                             4     212
   t33              temp    struct Account *                4     216
   t34              temp    struct Account *                4     220
   t36              temp    struct Account *                4     228
   t37              temp    double                          8     232
   t38              temp    double                          8     240
   t40              temp    double                          8     256
   t41              temp    double                          8     264
   t44              temp    class Dog (*)[3]                4     280
   t45              temp    class Dog (*)[3]                4     284
   t46              temp    class Dog (*)[3]                4     288
   t47              temp    int                             4     292
   t48              temp    int                             4     296
   t64              temp    int                             4     360
   t65              temp    class Counted                   4     364
   t66              temp    int                             4     368
   t68              temp    class Counted                   4     376
   t69              temp    class Counted *                 4     380
   t71              temp    class Counted                   4     388
   t72              temp    class Counted *                 4     392
   t75              temp    class Other                     4     404
   t76              temp    int                             4     408
   t77              temp    int                             4     412
   t86              temp    struct Account *                4     448
   t87              temp    double                          8     456
   t88              temp    struct Account *                4     464
   t89              temp    double                          8     472
   t90              temp    struct Account *                4     480
   t91              temp    const int *                     4     484
   t92              temp    int                             4     488
   t93              temp    int                             4     492
   t94              temp    int                             4     496
   t95              temp    const int *                     4     500
   t96              temp    int                             4     504
   t101             temp    int                             4     524
   t103             temp    int                             4     532
   t105             temp    int                             4     540
   t107             temp    int                             4     548
   (53 temporaries no longer used after optimization not shown)

 Code: 136 instruction(s)

    166        t1 = &keeper
    167        *t1 = 9
    168        t2 = &a
    169        *t2 = 1
    170        t4 = &t3
    171        *t4 = 101
    172        t64 = *t2
    173        param "copy of %d\n"
    174        param t64
    175        call printf, 2
    176        t65 = t3
    177        t66 = t65[0]
    178        param "%d\n"
    179        param t66
    180        call printf, 2
    181        t69 = &t68
    182        param t69                           (this)
    183        param t2
    184        call Counted::Counted(const class Counted &), 2
    185        b = t68
    186        t72 = &t71
    187        param t72                           (this)
    188        param 5
    189        call Counted::Counted(int), 2
    190        c = t71
    191        t14 = a[0]
    192        t15 = b[0]
    193        t16 = c[0]
    194        param "%d %d %d\n"
    195        param t14
    196        param t15
    197        param t16
    198        call printf, 4
    199        t17 = &o
    200        *t17 = 7
    201        t18 = &f
    202        t75 = o
    203        t76 = t75[0]
    204        t77 = t76 int<< 1
    205        *t18 = t77
    206        t19 = &g
    207        *t19 = 5
    208        t20 = f[0]
    209        t21 = g[0]
    210        param "%d %d\n"
    211        param t20
    212        param t21
    213        call printf, 3
    214        x = 1
    215        y = 2
    216        if x int<= 2 goto L8
    217        t22 = &x
    218        goto L9
    219  L8:   t22 = &y
    220  L9:   *t22 = 20
    221        if x int>= y goto L10
    222        t25 = &x
    223        goto L11
    224  L10:  t25 = &y
    225  L11:  *t25 = 10
    226        t28 = &x
    227        t31 = *t28
    228        t32 = t31 int+ 5
    229        *t28 = t32
    230        p[0] = 1
    231        p[8] = 10.5
    232        q[0] = 2
    233        q[8] = 99.0
    234        t33 = &p
    235        t34 = &q
    236        t86 = t33 ptr+ 8
    237        t87 = *t86
    238        t88 = t34 ptr+ 8
    239        t89 = *t88
    240        if t87 double>= t89 goto L12
    241        goto L13
    242  L12:  t90 = t33
    243        goto L14
    244  L13:  t90 = t34
    245  L14:  t36 = t90 ptr+ 8
    246        t37 = *t36
    247        t38 = t37 double- 9.0
    248        *t36 = t38
    249        t40 = p[8]
    250        t41 = q[8]
    251        param "%d %d %.1f %.1f\n"
    252        param x
    253        param y
    254        param t40
    255        param t41
    256        call printf, 5
    257        t91 = &primes
    258        t92 = 0
    259        t93 = 0
    260  L15:  if t93 int>= 4 goto L16
    261        t94 = t93 int<< 2
    262        t95 = t91 ptr+ t94
    263        t96 = *t95
    264        t92 = t92 int+ t96
    265        t93 = t93 int+ 1
    266        goto L15
    267  L16:  param "%d\n"
    268        param t92
    269        call printf, 2
    270        t44 = &pack
    271        *t44 = 0
    272        t45 = t44 ptr+ 4
    273        *t45 = 0
    274        t46 = t44 ptr+ 8
    275        *t46 = 0
    276        i = 0
    277  L17:  if i int>= 3 goto L18
    278        t47 = i int<< 2                     (w = 4)
    279        t48 = i int+ 1
    280        pack[t47] = t48
    281        i = t48
    282        goto L17
    283  L18:  t101 = *t46
    284        param "~Dog %d\n"
    285        param t101
    286        call printf, 2
    287        t103 = *t45
    288        param "~Dog %d\n"
    289        param t103
    290        call printf, 2
    291        t105 = *t44
    292        param "~Dog %d\n"
    293        param t105
    294        call printf, 2
    295        param "end of main\n"
    296        call printf, 1
    297        t107 = *t1
    298        param "~Dog %d\n"
    299        param t107
    300        call printf, 2
    301        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Counted            class_tag     class Counted              -           7    -    0  size 4
   take               function      int (class Counted)        -          13    -    1  _Z4take7Counted; defined
   give               function      class Counted (class Counted &) -          14    -    1  _Z4giveR7Counted; defined
   fresh              function      class Counted (int)        -          15    -    1  _Z5freshi; defined
   Other              class_tag     class Other                -          17    -    0  size 4
   Vec                class_tag     class Vec                  -          18    -    0  size 4
   Dog                class_tag     class Dog                  -          25    -    0  size 4
   keeper             variable      class Dog                  global     32    4    0  
   Row                typedef       int[4]                     -          34    -    0  
   primes             variable      const int[4]               global     35   16    1  
   sum                function      int (const int *)          -          36    -    1  _Z3sumPKi; defined
   Account            struct_tag    struct Account             -          38    -    0  size 16
   richer             function      struct Account &(struct Account &, struct Account &) -          39    -    1  _Z6richerR7AccountS0_; defined
   pick               function      int &(int, int &, int &)   -          40    -    1  _Z4pickiRiS_; defined
   main               function      int (void)                 -          42    -    0  defined

 scope: global > class Counted
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  field         int                        member      9    4    8  Counted::v; public, offset 0
   Counted            constructor   void (int)                 -          10    -    2  _ZN7CountedC1Ei; public
   Counted            constructor   void (const class Counted &) -          11    -    0  _ZN7CountedC1ERKS_; public

 scope: global > class Counted > Counted()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      10    4    1  x.1
   o                  parameter     const class Counted &      param      11    4    2  o.2

 scope: global > take()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Counted              param      13    4    1  c.3

 scope: global > give()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Counted &            param      14    4    1  c.4

 scope: global > fresh()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      15    4    1  x.5
   local              variable      class Counted              local      15    4    1  local.6

 scope: global > class Other
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  field         int                        member     17    4    2  Other::n; public, offset 0
   Other              constructor   void (void)                -          17    -    1  _ZN5OtherC1Ev; public

 scope: global > class Vec
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     20    4    4  Vec::x; public, offset 0
   Vec                constructor   void (class Other)         -          21    -    1  _ZN3VecC1E5Other; public
   Vec                constructor   void (int)                 -          22    -    1  _ZN3VecC1Ei; public

 scope: global > class Vec > Vec()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Other                param      21    4    1  o.7
   k                  parameter     int                        param      22    4    1  k.8

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     27    4    4  Dog::id; public, offset 0
   Dog                constructor   void (void)                -          28    -    1  _ZN3DogC1Ev; public
   Dog                constructor   void (int)                 -          29    -    1  _ZN3DogC1Ei; public
   ~Dog               destructor    void (void)                -          30    -    0  _ZN3DogD1Ev; public

 scope: global > class Dog > Dog()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      29    4    1  n.9

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     const int *                param      36    4    1  r.10
   s                  variable      int                        local      36    4    2  s.11

 scope: global > sum() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      36    4    3  i.12

 scope: global > struct Account
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     38    4    0  Account::id; public, offset 0
   balance            field         double                     member     38    8    5  Account::balance; public, offset 8

 scope: global > richer()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     struct Account &           param      39    4    2  a.13
   b                  parameter     struct Account &           param      39    4    2  b.14

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   which              parameter     int                        param      40    4    1  which.15
   a                  parameter     int &                      param      40    4    1  a.16
   b                  parameter     int &                      param      40    4    1  b.17

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      class Counted              local      43    4    3  a.18
   b                  variable      class Counted              local      45    4    1  b.19
   c                  variable      class Counted              local      46    4    1  c.20
   o                  variable      class Other                local      49    4    1  o.21
   f                  variable      class Vec                  local      50    4    1  f.22
   g                  variable      class Vec                  local      50    4    1  g.23
   x                  variable      int                        local      53    4    6  x.24
   y                  variable      int                        local      53    4    6  y.25
   r                  variable      int &                      local      54    4    1  r.26
   p                  variable      struct Account             local      58   16    2  p.27
   q                  variable      struct Account             local      58   16    2  q.28

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pack               variable      class Dog[3]               local      64   12    1  pack.29

 scope: global > main() > block > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      65    4    4  i.30

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Counted: size 4, align 4
    +0  int v  [public]
class Other: size 4, align 4
    +0  int n  [public]
class Vec: size 4, align 4
    +0  int x  [public]
class Dog: size 4, align 4
    +0  int id  [public]
struct Account: size 16, align 8
    +0  int id  [public]
    +8  double balance  [public]
