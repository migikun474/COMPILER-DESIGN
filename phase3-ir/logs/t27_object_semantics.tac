============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : no optimization
   Result        : Three address code generated: 15 function(s), 213 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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
    125     t2 = t1 int* 2
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

 Symbol table: 3 parameter(s)/local(s), 5 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   const int *                     4       0
   s                local   int                             4       4
   i                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    const int *                     4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24
   t5               temp    int                             4      28

 Code: 13 instruction(s)

    139       s = 0
    140       i = 0
    141  L1:  if i int< 4 goto L2
    142       goto L3
    143  L2:  t1 = i int* 4
    144       t2 = r ptr+ t1
    145       t3 = *t2
    146       t4 = s int+ t3
    147       s = t4
    148       t5 = i int+ 1
    149       i = t5
    150       goto L1
    151  L3:  return s

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

    152       t2 = a ptr+ 8
    153       t3 = *t2
    154       t4 = b ptr+ 8
    155       t5 = *t4
    156       if t3 double>= t5 goto L4
    157       goto L5
    158  L4:  t1 = a
    159       goto L6
    160  L5:  t1 = b
    161  L6:  return t1

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

 Code: 6 instruction(s)

    162       if which int!= 0 goto L7
    163       goto L8
    164  L7:  t1 = a
    165       goto L9
    166  L8:  t1 = b
    167  L9:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 55 temporaries, frame 328 bytes

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
   t5               temp    class Counted *                 4     104
   t6               temp    int                             4     108
   t7               temp    class Counted *                 4     112
   t8               temp    class Counted                   4     116
   t9               temp    class Counted *                 4     120
   t10              temp    class Counted *                 4     124
   t11              temp    class Counted                   4     128
   t12              temp    class Counted *                 4     132
   t13              temp    class Counted *                 4     136
   t14              temp    int                             4     140
   t15              temp    int                             4     144
   t16              temp    int                             4     148
   t17              temp    class Other *                   4     152
   t18              temp    class Vec *                     4     156
   t19              temp    class Vec *                     4     160
   t20              temp    int                             4     164
   t21              temp    int                             4     168
   t22              temp    int *                           4     172
   t23              temp    int *                           4     176
   t24              temp    int *                           4     180
   t25              temp    int *                           4     184
   t26              temp    int *                           4     188
   t27              temp    int *                           4     192
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
   t39              temp    struct Account *                4     248
   t40              temp    double                          8     256
   t41              temp    double                          8     264
   t42              temp    const int *                     4     272
   t43              temp    int                             4     276
   t44              temp    class Dog (*)[3]                4     280
   t45              temp    class Dog (*)[3]                4     284
   t46              temp    class Dog (*)[3]                4     288
   t47              temp    int                             4     292
   t48              temp    int                             4     296
   t49              temp    int                             4     300
   t50              temp    class Dog *                     4     304
   t51              temp    class Dog *                     4     308
   t52              temp    class Dog *                     4     312
   t53              temp    class Dog *                     4     316
   t54              temp    class Dog *                     4     320
   t55              temp    class Dog *                     4     324

 Code: 145 instruction(s)

    168        t1 = &keeper
    169        param t1                            (this)
    170        param 9
    171        call Dog::Dog(int), 2
    172        t2 = &a
    173        param t2                            (this)
    174        param 1
    175        call Counted::Counted(int), 2
    176        t4 = &t3
    177        t5 = &a
    178        param t4                            (this)
    179        param t5
    180        call Counted::Counted(const class Counted &), 2
    181        param t3
    182        t6 = call take(class Counted), 1
    183        param "%d\n"
    184        param t6
    185        call printf, 2
    186        t7 = &a
    187        param t7
    188        t8 = call give(class Counted &), 1
    189        t9 = &t8
    190        b = t8
    191        t10 = &b
    192        param 5
    193        t11 = call fresh(int), 1
    194        t12 = &t11
    195        c = t11
    196        t13 = &c
    197        t14 = a[0]
    198        t15 = b[0]
    199        t16 = c[0]
    200        param "%d %d %d\n"
    201        param t14
    202        param t15
    203        param t16
    204        call printf, 4
    205        t17 = &o
    206        param t17                           (this)
    207        call Other::Other(), 1
    208        t18 = &f
    209        param t18                           (this)
    210        param o
    211        call Vec::Vec(class Other), 2
    212        t19 = &g
    213        param t19                           (this)
    214        param 5
    215        call Vec::Vec(int), 2
    216        t20 = f[0]
    217        t21 = g[0]
    218        param "%d %d\n"
    219        param t20
    220        param t21
    221        call printf, 3
    222        x = 1
    223        y = 2
    224        if x int> y goto L10
    225        goto L11
    226  L10:  t23 = &x
    227        t22 = t23
    228        goto L12
    229  L11:  t24 = &y
    230        t22 = t24
    231  L12:  r = t22
    232        *r = 20
    233        if x int< y goto L13
    234        goto L14
    235  L13:  t26 = &x
    236        t25 = t26
    237        goto L15
    238  L14:  t27 = &y
    239        t25 = t27
    240  L15:  *t25 = 10
    241        t28 = &x
    242        t29 = &y
    243        param 1
    244        param t28
    245        param t29
    246        t30 = call pick(int, int &, int &), 3
    247        t31 = *t30
    248        t32 = t31 int+ 5
    249        *t30 = t32
    250        p[0] = 1
    251        p[8] = 10.5
    252        q[0] = 2
    253        q[8] = 99.0
    254        t33 = &p
    255        t34 = &q
    256        param t33
    257        param t34
    258        t35 = call richer(struct Account &, struct Account &), 2
    259        t36 = t35 ptr+ 8
    260        t37 = *t36
    261        t38 = t37 double- 9.0
    262        t39 = t35 ptr+ 8
    263        *t39 = t38
    264        t40 = p[8]
    265        t41 = q[8]
    266        param "%d %d %.1f %.1f\n"
    267        param x
    268        param y
    269        param t40
    270        param t41
    271        call printf, 5
    272        t42 = &primes
    273        param t42
    274        t43 = call sum(const int *), 1
    275        param "%d\n"
    276        param t43
    277        call printf, 2
    278        t44 = &pack
    279        param t44                           (this)
    280        call Dog::Dog(), 1
    281        t45 = t44 ptr+ 4
    282        param t45                           (this)
    283        call Dog::Dog(), 1
    284        t46 = t44 ptr+ 8
    285        param t46                           (this)
    286        call Dog::Dog(), 1
    287        i = 0
    288  L16:  if i int< 3 goto L17
    289        goto L18
    290  L17:  t47 = i int* 4                      (w = 4)
    291        t48 = i int+ 1
    292        pack[t47] = t48
    293        t49 = i int+ 1
    294        i = t49
    295        goto L16
    296  L18:  t50 = &pack
    297        t51 = t50 ptr+ 8
    298        param t51                           (this)
    299        call Dog::~Dog(), 1
    300        t52 = &pack
    301        t53 = t52 ptr+ 4
    302        param t53                           (this)
    303        call Dog::~Dog(), 1
    304        t54 = &pack
    305        param t54                           (this)
    306        call Dog::~Dog(), 1
    307        param "end of main\n"
    308        call printf, 1
    309        t55 = &keeper
    310        param t55                           (this)
    311        call Dog::~Dog(), 1
    312        return 0


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
