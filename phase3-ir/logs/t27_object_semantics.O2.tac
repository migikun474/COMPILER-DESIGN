============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t27_object_semantics.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 172 -> 154 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          172 -> 154   (10% fewer)

   constants folded                        0
   algebraic simplifications               2
   common subexpressions                   4
   copies / constants forwarded            6
   temporaries merged away                 8
   dead instructions removed               4
   jumps removed or redirected             5
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                1

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

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   local            local   class Counted                   4       4
   t1               temp    class Counted *                 4       8

 Code: 5 instruction(s)

    106     t1 = &local
    107     param t1                            (this)
    108     call Counted::Counted(), 1
    109     local[0] = x
    110     return local

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4

 Code: 6 instruction(s)

    111     t1 = this ptr+ 4
    112     *t1 = 0
    113     *this = 42
    114     param "Dog()\n"
    115     call printf, 1
    116     return

============================================================================
 FUNCTION peek(const class Dog &)        (link name _Z4peekRK3Dog)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                param   const class Dog &               4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    117     t1 = *d
    118     return t1

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

    119       s = 0
    120       i = 0
    121  L1:  if i int>= 4 goto L2
    122       t1 = i int<< 2
    123       t2 = r ptr+ t1
    124       t3 = *t2
    125       s = s int+ t3
    126       i = i int+ 1
    127       goto L1
    128  L2:  return s

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

    129       t2 = a ptr+ 8
    130       t3 = *t2
    131       t4 = b ptr+ 8
    132       t5 = *t4
    133       if t3 double>= t5 goto L3
    134       goto L4
    135  L3:  t1 = a
    136       goto L5
    137  L4:  t1 = b
    138  L5:  return t1

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

    139       if which int== 0 goto L6
    140       t1 = a
    141       goto L7
    142  L6:  t1 = b
    143  L7:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 36 temporaries, frame 284 bytes

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
   t8               temp    int                             4     112
   t9               temp    int                             4     116
   t10              temp    int                             4     120
   t11              temp    int *                           4     124
   t14              temp    int *                           4     136
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
   t40              temp    int                             4     260
   t41              temp    class Dog *                     4     264
   t42              temp    int                             4     268
   t43              temp    int                             4     272
   t44              temp    class Dog *                     4     276
   t45              temp    int                             4     280
   (9 temporaries no longer used after optimization not shown)

 Code: 110 instruction(s)

    144        t1 = &keeper
    145        param t1                            (this)
    146        call Dog::Dog(), 1
    147        param "start of main\n"
    148        call printf, 1
    149        t2 = &a
    150        param t2                            (this)
    151        call Counted::Counted(), 1
    152        param a
    153        t3 = call take(class Counted), 1
    154        t4 = a[0]
    155        param "%d %d\n"
    156        param t3
    157        param t4
    158        call printf, 3
    159        param t2
    160        b = call give(class Counted &), 1
    161        b[0] = 7
    162        param 5
    163        c = call fresh(int), 1
    164        t8 = a[0]
    165        t9 = b[0]
    166        t10 = c[0]
    167        param "%d %d %d\n"
    168        param t8
    169        param t9
    170        param t10
    171        call printf, 4
    172        x = 1
    173        y = 2
    174        if x int<= 2 goto L8
    175        t11 = &x
    176        goto L9
    177  L8:   t11 = &y
    178  L9:   *t11 = 20
    179        if x int>= y goto L10
    180        t14 = &x
    181        goto L11
    182  L10:  t14 = &y
    183  L11:  *t14 = 10
    184        t17 = &x
    185        t18 = &y
    186        param 1
    187        param t17
    188        param t18
    189        t19 = call pick(int, int &, int &), 3
    190        t20 = *t19
    191        t21 = t20 int+ 5
    192        *t19 = t21
    193        p[0] = 1
    194        p[8] = 10.5
    195        q[0] = 2
    196        q[8] = 99.0
    197        t22 = &p
    198        t23 = &q
    199        param t22
    200        param t23
    201        t24 = call richer(struct Account &, struct Account &), 2
    202        t25 = t24 ptr+ 8
    203        t26 = *t25
    204        t27 = t26 double- 9.0
    205        *t25 = t27
    206        t29 = p[8]
    207        t30 = q[8]
    208        param "%d %d %.1f %.1f\n"
    209        param x
    210        param y
    211        param t29
    212        param t30
    213        call printf, 5
    214        t31 = &primes
    215        param t31
    216        t32 = call sum(const int *), 1
    217        param "%d\n"
    218        param t32
    219        call printf, 2
    220        t33 = &pack
    221        param t33                           (this)
    222        call Dog::Dog(), 1
    223        t34 = t33 ptr+ 8
    224        param t34                           (this)
    225        call Dog::Dog(), 1
    226        t35 = t33 ptr+ 16
    227        param t35                           (this)
    228        call Dog::Dog(), 1
    229        i = 0
    230  L12:  if i int>= 3 goto L13
    231        t36 = i int<< 3                     (w = 8)
    232        t37 = t36 int+ 4
    233        t38 = i int+ 1
    234        pack[t37] = t38
    235        i = t38
    236        goto L12
    237  L13:  t40 = pack[20]
    238        t41 = &pack
    239        param t41
    240        t42 = call peek(const class Dog &), 1
    241        param "%d %d\n"
    242        param t40
    243        param t42
    244        call printf, 3
    245        t43 = keeper[4]
    246        t44 = &keeper
    247        param t44
    248        t45 = call peek(const class Dog &), 1
    249        param "%d %d\n"
    250        param t43
    251        param t45
    252        call printf, 3
    253        return 0


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
