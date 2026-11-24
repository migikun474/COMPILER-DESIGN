============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : no optimization
   Result        : Three address code generated: 10 function(s), 172 instruction(s)

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

 Symbol table: 10 parameter(s)/local(s), 45 temporaries, frame 284 bytes

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
   t7               temp    class Counted                   4     108
   t8               temp    int                             4     112
   t9               temp    int                             4     116
   t10              temp    int                             4     120
   t11              temp    int *                           4     124
   t12              temp    int *                           4     128
   t13              temp    int *                           4     132
   t14              temp    int *                           4     136
   t15              temp    int *                           4     140
   t16              temp    int *                           4     144
   t17              temp    int *                           4     148
   t18              temp    int *                           4     152
   t19              temp    int &                           4     156
   t20              temp    int                             4     160
   t21              temp    int                             4     164
   t22              temp    struct Account *                4     168
   t23              temp    struct Account *                4     172
   t24              temp    struct Account &                4     176
   t25              temp    struct Account *                4     180
   t26              temp    double                          8     184
   t27              temp    double                          8     192
   t28              temp    struct Account *                4     200
   t29              temp    double                          8     208
   t30              temp    double                          8     216
   t31              temp    const int *                     4     224
   t32              temp    int                             4     228
   t33              temp    class Dog (*)[3]                4     232
   t34              temp    class Dog (*)[3]                4     236
   t35              temp    class Dog (*)[3]                4     240
   t36              temp    int                             4     244
   t37              temp    int                             4     248
   t38              temp    int                             4     252
   t39              temp    int                             4     256
   t40              temp    int                             4     260
   t41              temp    class Dog *                     4     264
   t42              temp    int                             4     268
   t43              temp    int                             4     272
   t44              temp    class Dog *                     4     276
   t45              temp    int                             4     280

 Code: 123 instruction(s)

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
    168        b[0] = 7
    169        param 5
    170        t7 = call fresh(int), 1
    171        c = t7
    172        t8 = a[0]
    173        t9 = b[0]
    174        t10 = c[0]
    175        param "%d %d %d\n"
    176        param t8
    177        param t9
    178        param t10
    179        call printf, 4
    180        x = 1
    181        y = 2
    182        if x int> y goto L10
    183        goto L11
    184  L10:  t12 = &x
    185        t11 = t12
    186        goto L12
    187  L11:  t13 = &y
    188        t11 = t13
    189  L12:  r = t11
    190        *r = 20
    191        if x int< y goto L13
    192        goto L14
    193  L13:  t15 = &x
    194        t14 = t15
    195        goto L15
    196  L14:  t16 = &y
    197        t14 = t16
    198  L15:  *t14 = 10
    199        t17 = &x
    200        t18 = &y
    201        param 1
    202        param t17
    203        param t18
    204        t19 = call pick(int, int &, int &), 3
    205        t20 = *t19
    206        t21 = t20 int+ 5
    207        *t19 = t21
    208        p[0] = 1
    209        p[8] = 10.5
    210        q[0] = 2
    211        q[8] = 99.0
    212        t22 = &p
    213        t23 = &q
    214        param t22
    215        param t23
    216        t24 = call richer(struct Account &, struct Account &), 2
    217        t25 = t24 ptr+ 8
    218        t26 = *t25
    219        t27 = t26 double- 9.0
    220        t28 = t24 ptr+ 8
    221        *t28 = t27
    222        t29 = p[8]
    223        t30 = q[8]
    224        param "%d %d %.1f %.1f\n"
    225        param x
    226        param y
    227        param t29
    228        param t30
    229        call printf, 5
    230        t31 = &primes
    231        param t31
    232        t32 = call sum(const int *), 1
    233        param "%d\n"
    234        param t32
    235        call printf, 2
    236        t33 = &pack
    237        param t33                           (this)
    238        call Dog::Dog(), 1
    239        t34 = t33 ptr+ 8
    240        param t34                           (this)
    241        call Dog::Dog(), 1
    242        t35 = t33 ptr+ 16
    243        param t35                           (this)
    244        call Dog::Dog(), 1
    245        i = 0
    246  L16:  if i int< 3 goto L17
    247        goto L18
    248  L17:  t36 = i int* 8                      (w = 8)
    249        t37 = t36 int+ 4
    250        t38 = i int+ 1
    251        pack[t37] = t38
    252        t39 = i int+ 1
    253        i = t39
    254        goto L16
    255  L18:  t40 = pack[20]
    256        t41 = &pack
    257        param t41
    258        t42 = call peek(const class Dog &), 1
    259        param "%d %d\n"
    260        param t40
    261        param t42
    262        call printf, 3
    263        t43 = keeper[4]
    264        t44 = &keeper
    265        param t44
    266        t45 = call peek(const class Dog &), 1
    267        param "%d %d\n"
    268        param t43
    269        param t45
    270        call printf, 3
    271        return 0


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
