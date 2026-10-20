============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 213 -> 191 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          213 -> 191   (10% fewer)

   constants folded                        0
   algebraic simplifications               3
   common subexpressions                   6
   copies / constants forwarded            8
   temporaries merged away                 6
   dead instructions removed              10
   jumps removed or redirected             5
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                1

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   keeper           class Dog                       4  0
   primes           const int[4]                   16  { +0: 2, +4: 3, +8: 5, +12: 7 }

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted &                 4       0
   t1               temp    class Counted                   4       4
   t2               temp    class Counted *                 4       8

 Code: 5 instruction(s)

    112     t2 = &t1
    113     param t2                            (this)
    114     param c
    115     call Counted::Counted(const class Counted &), 2
    116     return t1

============================================================================
 FUNCTION fresh(int)        (link name _Z5freshi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   local            local   class Counted                   4       4
   t1               temp    class Counted *                 4       8

 Code: 5 instruction(s)

    117     t1 = &local
    118     param t1                            (this)
    119     param x
    120     call Counted::Counted(int), 2
    121     return local

============================================================================
 FUNCTION Other::Other()        (link name _ZN5OtherC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Other *                   4       0

 Code: 2 instruction(s)

    122     *this = 7
    123     return

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

    124     t1 = o[0]
    125     t2 = t1 int<< 1
    126     *this = t2
    127     return

============================================================================
 FUNCTION Vec::Vec(int)        (link name _ZN3VecC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4

 Code: 2 instruction(s)

    128     *this = k
    129     return

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0

 Code: 2 instruction(s)

    130     *this = 0
    131     return

============================================================================
 FUNCTION Dog::Dog(int)        (link name _ZN3DogC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   n                param   int                             4       4

 Code: 2 instruction(s)

    132     *this = n
    133     return

============================================================================
 FUNCTION Dog::~Dog()        (link name _ZN3DogD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    134     t1 = *this
    135     param "~Dog %d\n"
    136     param t1
    137     call printf, 2
    138     return

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

    139       s = 0
    140       i = 0
    141  L1:  if i int>= 4 goto L2
    142       t1 = i int<< 2
    143       t2 = r ptr+ t1
    144       t3 = *t2
    145       s = s int+ t3
    146       i = i int+ 1
    147       goto L1
    148  L2:  return s

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

    149       t2 = a ptr+ 8
    150       t3 = *t2
    151       t4 = b ptr+ 8
    152       t5 = *t4
    153       if t3 double>= t5 goto L3
    154       goto L4
    155  L3:  t1 = a
    156       goto L5
    157  L4:  t1 = b
    158  L5:  return t1

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

    159       if which int== 0 goto L6
    160       t1 = a
    161       goto L7
    162  L6:  t1 = b
    163  L7:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 41 temporaries, frame 328 bytes

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
   t6               temp    int                             4     108
   t8               temp    class Counted                   4     116
   t11              temp    class Counted                   4     128
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
   t29              temp    int *                           4     200
   t30              temp    int &                           4     204
   t31              temp    int                             4     208
   t32              temp    int                             4     212
   t33              temp    struct Account *                4     216
   t34              temp    struct Account *                4     220
   t35              temp    struct Account &                4     224
   t36              temp    struct Account *                4     228
   t37              temp    double                          8     232
   t38              temp    double                          8     240
   t40              temp    double                          8     256
   t41              temp    double                          8     264
   t42              temp    const int (*)[4]                4     272
   t43              temp    int                             4     276
   t44              temp    class Dog (*)[3]                4     280
   t45              temp    class Dog (*)[3]                4     284
   t46              temp    class Dog (*)[3]                4     288
   t47              temp    int                             4     292
   t48              temp    int                             4     296
   t50              temp    class Dog *                     4     304
   t51              temp    class Dog *                     4     308
   t53              temp    class Dog *                     4     316
   t55              temp    class Dog *                     4     324
   (14 temporaries no longer used after optimization not shown)

 Code: 127 instruction(s)

    164        t1 = &keeper
    165        param t1                            (this)
    166        param 9
    167        call Dog::Dog(int), 2
    168        t2 = &a
    169        param t2                            (this)
    170        param 1
    171        call Counted::Counted(int), 2
    172        t4 = &t3
    173        param t4                            (this)
    174        param t2
    175        call Counted::Counted(const class Counted &), 2
    176        param t3
    177        t6 = call take(class Counted), 1
    178        param "%d\n"
    179        param t6
    180        call printf, 2
    181        param t2
    182        t8 = call give(class Counted &), 1
    183        b = t8
    184        param 5
    185        t11 = call fresh(int), 1
    186        c = t11
    187        t14 = a[0]
    188        t15 = b[0]
    189        t16 = c[0]
    190        param "%d %d %d\n"
    191        param t14
    192        param t15
    193        param t16
    194        call printf, 4
    195        t17 = &o
    196        param t17                           (this)
    197        call Other::Other(), 1
    198        t18 = &f
    199        param t18                           (this)
    200        param o
    201        call Vec::Vec(class Other), 2
    202        t19 = &g
    203        param t19                           (this)
    204        param 5
    205        call Vec::Vec(int), 2
    206        t20 = f[0]
    207        t21 = g[0]
    208        param "%d %d\n"
    209        param t20
    210        param t21
    211        call printf, 3
    212        x = 1
    213        y = 2
    214        if x int<= 2 goto L8
    215        t22 = &x
    216        goto L9
    217  L8:   t22 = &y
    218  L9:   *t22 = 20
    219        if x int>= y goto L10
    220        t25 = &x
    221        goto L11
    222  L10:  t25 = &y
    223  L11:  *t25 = 10
    224        t28 = &x
    225        t29 = &y
    226        param 1
    227        param t28
    228        param t29
    229        t30 = call pick(int, int &, int &), 3
    230        t31 = *t30
    231        t32 = t31 int+ 5
    232        *t30 = t32
    233        p[0] = 1
    234        p[8] = 10.5
    235        q[0] = 2
    236        q[8] = 99.0
    237        t33 = &p
    238        t34 = &q
    239        param t33
    240        param t34
    241        t35 = call richer(struct Account &, struct Account &), 2
    242        t36 = t35 ptr+ 8
    243        t37 = *t36
    244        t38 = t37 double- 9.0
    245        *t36 = t38
    246        t40 = p[8]
    247        t41 = q[8]
    248        param "%d %d %.1f %.1f\n"
    249        param x
    250        param y
    251        param t40
    252        param t41
    253        call printf, 5
    254        t42 = &primes
    255        param t42
    256        t43 = call sum(const int *), 1
    257        param "%d\n"
    258        param t43
    259        call printf, 2
    260        t44 = &pack
    261        param t44                           (this)
    262        call Dog::Dog(), 1
    263        t45 = t44 ptr+ 4
    264        param t45                           (this)
    265        call Dog::Dog(), 1
    266        t46 = t44 ptr+ 8
    267        param t46                           (this)
    268        call Dog::Dog(), 1
    269        i = 0
    270  L12:  if i int>= 3 goto L13
    271        t47 = i int<< 2                     (w = 4)
    272        t48 = i int+ 1
    273        pack[t47] = t48
    274        i = t48
    275        goto L12
    276  L13:  t50 = &pack
    277        t51 = t50 ptr+ 8
    278        param t51                           (this)
    279        call Dog::~Dog(), 1
    280        t53 = t50 ptr+ 4
    281        param t53                           (this)
    282        call Dog::~Dog(), 1
    283        param t50                           (this)
    284        call Dog::~Dog(), 1
    285        param "end of main\n"
    286        call printf, 1
    287        t55 = &keeper
    288        param t55                           (this)
    289        call Dog::~Dog(), 1
    290        return 0


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
