============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 174 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted                   4       0
   t1               temp    int                             4       4

 Code: 3 instruction(s)

    102     c[0] = 50
    103     t1 = c[0]
    104     return t1

============================================================================
 FUNCTION give(class Counted &)        (link name _Z4giveR7Counted)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Counted &                 4       0
   t1               temp    class Counted                   4       4

 Code: 2 instruction(s)

    105     t1 = *c
    106     return t1

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

    107     t1 = &local
    108     param t1                            (this)
    109     call Counted::Counted(), 1
    110     local[0] = x
    111     return local

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4

 Code: 6 instruction(s)

    112     t1 = this ptr+ 4
    113     *t1 = 0
    114     *this = 42
    115     param "Dog()\n"
    116     call printf, 1
    117     return

============================================================================
 FUNCTION peek(const class Dog &)        (link name _Z4peekRK3Dog)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                param   const class Dog &               4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    118     t1 = *d
    119     return t1

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

    120       s = 0
    121       i = 0
    122  L1:  if i int< 4 goto L2
    123       goto L3
    124  L2:  t1 = i int* 4
    125       t2 = r ptr+ t1
    126       t3 = *t2
    127       t4 = s int+ t3
    128       s = t4
    129       t5 = i int+ 1
    130       i = t5
    131       goto L1
    132  L3:  return s

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

    133       t2 = a ptr+ 8
    134       t3 = *t2
    135       t4 = b ptr+ 8
    136       t5 = *t4
    137       if t3 double>= t5 goto L4
    138       goto L5
    139  L4:  t1 = a
    140       goto L6
    141  L5:  t1 = b
    142  L6:  return t1

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

    143       if which int!= 0 goto L7
    144       goto L8
    145  L7:  t1 = a
    146       goto L9
    147  L8:  t1 = b
    148  L9:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 47 temporaries, frame 292 bytes

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
   t3               temp    int                             4      92
   t4               temp    int                             4      96
   t5               temp    class Counted *                 4     100
   t6               temp    class Counted                   4     104
   t7               temp    class Counted *                 4     108
   t8               temp    class Counted                   4     112
   t9               temp    class Counted *                 4     116
   t10              temp    int                             4     120
   t11              temp    int                             4     124
   t12              temp    int                             4     128
   t13              temp    int *                           4     132
   t14              temp    int *                           4     136
   t15              temp    int *                           4     140
   t16              temp    int *                           4     144
   t17              temp    int *                           4     148
   t18              temp    int *                           4     152
   t19              temp    int *                           4     156
   t20              temp    int *                           4     160
   t21              temp    int &                           4     164
   t22              temp    int                             4     168
   t23              temp    int                             4     172
   t24              temp    struct Account *                4     176
   t25              temp    struct Account *                4     180
   t26              temp    struct Account &                4     184
   t27              temp    struct Account *                4     188
   t28              temp    double                          8     192
   t29              temp    double                          8     200
   t30              temp    struct Account *                4     208
   t31              temp    double                          8     216
   t32              temp    double                          8     224
   t33              temp    const int *                     4     232
   t34              temp    int                             4     236
   t35              temp    class Dog (*)[3]                4     240
   t36              temp    class Dog (*)[3]                4     244
   t37              temp    class Dog (*)[3]                4     248
   t38              temp    int                             4     252
   t39              temp    int                             4     256
   t40              temp    int                             4     260
   t41              temp    int                             4     264
   t42              temp    int                             4     268
   t43              temp    class Dog *                     4     272
   t44              temp    int                             4     276
   t45              temp    int                             4     280
   t46              temp    class Dog *                     4     284
   t47              temp    int                             4     288

 Code: 125 instruction(s)

    149        t1 = &keeper
    150        param t1                            (this)
    151        call Dog::Dog(), 1
    152        param "start of main\n"
    153        call printf, 1
    154        t2 = &a
    155        param t2                            (this)
    156        call Counted::Counted(), 1
    157        param a
    158        t3 = call take(class Counted), 1
    159        t4 = a[0]
    160        param "%d %d\n"
    161        param t3
    162        param t4
    163        call printf, 3
    164        t5 = &a
    165        param t5
    166        t6 = call give(class Counted &), 1
    167        b = t6
    168        t7 = &b
    169        b[0] = 7
    170        param 5
    171        t8 = call fresh(int), 1
    172        c = t8
    173        t9 = &c
    174        t10 = a[0]
    175        t11 = b[0]
    176        t12 = c[0]
    177        param "%d %d %d\n"
    178        param t10
    179        param t11
    180        param t12
    181        call printf, 4
    182        x = 1
    183        y = 2
    184        if x int> y goto L10
    185        goto L11
    186  L10:  t14 = &x
    187        t13 = t14
    188        goto L12
    189  L11:  t15 = &y
    190        t13 = t15
    191  L12:  r = t13
    192        *r = 20
    193        if x int< y goto L13
    194        goto L14
    195  L13:  t17 = &x
    196        t16 = t17
    197        goto L15
    198  L14:  t18 = &y
    199        t16 = t18
    200  L15:  *t16 = 10
    201        t19 = &x
    202        t20 = &y
    203        param 1
    204        param t19
    205        param t20
    206        t21 = call pick(int, int &, int &), 3
    207        t22 = *t21
    208        t23 = t22 int+ 5
    209        *t21 = t23
    210        p[0] = 1
    211        p[8] = 10.5
    212        q[0] = 2
    213        q[8] = 99.0
    214        t24 = &p
    215        t25 = &q
    216        param t24
    217        param t25
    218        t26 = call richer(struct Account &, struct Account &), 2
    219        t27 = t26 ptr+ 8
    220        t28 = *t27
    221        t29 = t28 double- 9.0
    222        t30 = t26 ptr+ 8
    223        *t30 = t29
    224        t31 = p[8]
    225        t32 = q[8]
    226        param "%d %d %.1f %.1f\n"
    227        param x
    228        param y
    229        param t31
    230        param t32
    231        call printf, 5
    232        t33 = &primes
    233        param t33
    234        t34 = call sum(const int *), 1
    235        param "%d\n"
    236        param t34
    237        call printf, 2
    238        t35 = &pack
    239        param t35                           (this)
    240        call Dog::Dog(), 1
    241        t36 = t35 ptr+ 8
    242        param t36                           (this)
    243        call Dog::Dog(), 1
    244        t37 = t35 ptr+ 16
    245        param t37                           (this)
    246        call Dog::Dog(), 1
    247        i = 0
    248  L16:  if i int< 3 goto L17
    249        goto L18
    250  L17:  t38 = i int* 8                      (w = 8)
    251        t39 = t38 int+ 4
    252        t40 = i int+ 1
    253        pack[t39] = t40
    254        t41 = i int+ 1
    255        i = t41
    256        goto L16
    257  L18:  t42 = pack[20]
    258        t43 = &pack
    259        param t43
    260        t44 = call peek(const class Dog &), 1
    261        param "%d %d\n"
    262        param t42
    263        param t44
    264        call printf, 3
    265        t45 = keeper[4]
    266        t46 = &keeper
    267        param t46
    268        t47 = call peek(const class Dog &), 1
    269        param "%d %d\n"
    270        param t45
    271        param t47
    272        call printf, 3
    273        return 0


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
