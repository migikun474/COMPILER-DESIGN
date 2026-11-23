============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t36_enums_unions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 171 -> 142 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          171 -> 142   (16% fewer)

   constants folded                        7
   algebraic simplifications               5
   common subexpressions                   3
   copies / constants forwarded           29
   temporaries merged away                 4
   dead instructions removed              10
   jumps removed or redirected             7
   unreachable instructions removed        8

----------------------------------------------------------------------------
 GLOBALS: 2 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                union Word                      4  0
   table            int[7]                         28  0

 As three address code (initial values, in place before main runs):

    g[...] = 0                     (zero-initialized)
    table[...] = 0                 (zero-initialized)

============================================================================
 FUNCTION show(int)        (link name _Z4showi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0

 Code: 1 instruction(s)

    100     return 1

============================================================================
 FUNCTION show(enum Color)        (link name _Z4show5Color)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   enum Color                      4       0

 Code: 1 instruction(s)

    101     return 2

============================================================================
 FUNCTION show(Level)        (link name _Z4show5Level)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   l                param   Level                           4       0

 Code: 1 instruction(s)

    102     return 3

============================================================================
 FUNCTION name(enum Color)        (link name _Z4name5Color)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   enum Color                      4       0
   t1               temp    int                             4       4

 Code: 8 instruction(s)

    103       t1 = c
    104       goto L4
    105  L1:  return "red"
    106  L2:  return "green"
    107  L3:  return "blue"
    108  L4:  if t1 int== 0 goto L1
    109       if t1 int== 5 goto L2
    110       goto L3

============================================================================
 FUNCTION flip(union Word)        (link name _Z4flip4Word)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   w                param   union Word                      4       0
   t1               temp    int                             4       4
   t2               temp    unsigned int                    4       8

 Code: 4 instruction(s)

    111     t1 = w[0]
    112     t2 = t1 uint^ 2147483648
    113     w[0] = t2
    114     return w

============================================================================
 FUNCTION sumBytes(union Word *)        (link name _Z8sumBytesP4Word)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 14 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   union Word *                    4       0
   t1               temp    unsigned char                   1       4
   t2               temp    int                             4       8
   t3               temp    union Word *                    4      12
   t4               temp    unsigned char                   1      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24
   t7               temp    union Word *                    4      28
   t8               temp    unsigned char                   1      32
   t9               temp    int                             4      36
   t10              temp    int                             4      40
   t11              temp    union Word *                    4      44
   t12              temp    unsigned char                   1      48
   t13              temp    int                             4      52
   t14              temp    int                             4      56

 Code: 15 instruction(s)

    115     t1 = *p
    116     t2 = uchartoint t1
    117     t3 = p ptr+ 1
    118     t4 = *t3
    119     t5 = uchartoint t4
    120     t6 = t2 int+ t5
    121     t7 = p ptr+ 2
    122     t8 = *t7
    123     t9 = uchartoint t8
    124     t10 = t6 int+ t9
    125     t11 = p ptr+ 3
    126     t12 = *t11
    127     t13 = uchartoint t12
    128     t14 = t10 int+ t13
    129     return t14

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 21 parameter(s)/local(s), 32 temporaries, frame 296 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                local   enum Color                      4       0
   d                local   enum Color                      4       4
   l                local   Level                           4       8
   n                local   int                             4      12
   big              local   bool                            1      16
   e                local   enum Color                      4      20
   size             local   enum (unnamed at 35:5)          4      24
   t                local   struct Tagged                   8      28
   w                local   union Word                      4      36
   f1               local   float                           4      40
   i1               local   int                             4      44
   i2               local   int                             4      48
   i3               local   int                             4      52
   i4               local   int                             4      56
   fl               local   union Word                      4      60
   gb               local   int                             4      64
   arr              local   union Word[3]                  12      68
   k                local   int                             4      80
   s                local   int                             4      84
   x                local   union Wide                      8      88
   hi               local   int                             4      96
   t5               temp    const char *                    4     116
   t6               temp    const char *                    4     120
   t8               temp    int                             4     128
   t9               temp    int                             4     132
   t10              temp    int                             4     136
   t11              temp    enum Color                      4     140
   t12              temp    int                             4     144
   t13              temp    float                           4     148
   t14              temp    int                             4     152
   t18              temp    int                             4     168
   t19              temp    int                             4     172
   t22              temp    int                             4     184
   t23              temp    double                          8     192
   t24              temp    int                             4     200
   t25              temp    int                             4     204
   t26              temp    int                             4     208
   t27              temp    int                             4     212
   t29              temp    int                             4     220
   t30              temp    int                             4     224
   t31              temp    unsigned char                   1     228
   t32              temp    int                             4     232
   t33              temp    int                             4     236
   t34              temp    unsigned char                   1     240
   t35              temp    int                             4     244
   t37              temp    int                             4     252
   t38              temp    unsigned char                   1     256
   t39              temp    int                             4     260
   t40              temp    int                             4     264
   t43              temp    int                             4     276
   t44              temp    union Word *                    4     280
   t45              temp    int                             4     284
   t46              temp    double                          8     288
   (14 temporaries no longer used after optimization not shown)

 Code: 112 instruction(s)

    130       c = 6
    131       d = 5
    132       l = 1
    133       n = 7
    134       big = 1
    135       e = 6
    136       size = 16
    137       t[0] = 5
    138       t[4] = 42
    139       param 6
    140       t5 = call name(enum Color), 1
    141       param 5
    142       t6 = call name(enum Color), 1
    143       param 6
    144       t8 = call show(enum Color), 1
    145       param 5
    146       t9 = call show(int), 1
    147       param 1
    148       t10 = call show(Level), 1
    149       param "%s %s %d %d %d %d %d\n"
    150       param t5
    151       param t6
    152       param 7
    153       param 1
    154       param t8
    155       param t9
    156       param t10
    157       call printf, 8
    158       t11 = t[0]
    159       t12 = t[4]
    160       param "%d %d %d %d %d\n"
    161       param 6
    162       param 16
    163       param t11
    164       param t12
    165       param 28
    166       call printf, 6
    167       w[0] = 1078530011
    168       t13 = w[0]
    169       f1 = t13
    170       w[0] = 2.0
    171       t14 = w[0]
    172       i1 = t14
    173       w[0] = 7
    174       i2 = 14
    175       w[0] = 1
    176       t18 = w[0]
    177       i3 = t18
    178       w[2] = 2
    179       t19 = w[0]
    180       i4 = t19
    181       param w
    182       fl = call flip(union Word), 1
    183       g[0] = -1.5
    184       t22 = g[0]
    185       gb = t22
    186       t23 = floattodouble t13
    187       t24 = fl[0]
    188       param "%.4f %x %d %x %x %x %x\n"
    189       param t23
    190       param t14
    191       param 14
    192       param t18
    193       param t19
    194       param t24
    195       param t22
    196       call printf, 8
    197       s = 0
    198       k = 0
    199  L5:  if k int>= 3 goto L6
    200       t25 = k int<< 2                     (w = 4)
    201       t26 = k int<< 8
    202       t27 = t26 int+ 1
    203       arr[t25] = t27
    204       k = k int+ 1
    205       goto L5
    206  L6:  k = 0
    207  L7:  if k int>= 3 goto L9
    208       t29 = k int<< 2                     (w = 4)
    209       t30 = t29 int+ 1
    210       t31 = arr[t30]
    211       t32 = uchartoint t31
    212       if t32 int<= 0 goto L8
    213       t33 = k int<< 2                     (w = 4)
    214       t34 = arr[t33]
    215       t35 = uchartoint t34
    216       t37 = t33 int+ 1
    217       t38 = arr[t37]
    218       t39 = uchartoint t38
    219       t40 = t35 int+ t39
    220       s = s int+ t40
    221  L8:  k = k int+ 1
    222       goto L7
    223  L9:  x[0] = 1.0
    224       t43 = x[4]
    225       hi = t43
    226       x[0] = 5
    227       x[0] = 0
    228       x[4] = 1073741824
    229       t44 = &w
    230       param t44
    231       t45 = call sumBytes(union Word *), 1
    232       t46 = x[0]
    233       param "%d %d %x %.1f %d %d\n"
    234       param s
    235       param t45
    236       param t43
    237       param t46
    238       param 8
    239       param 4
    240       call printf, 7
    241       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Color              enum_tag      enum Color                 -           7    -    0  
   Red                enumerator    enum Color                 -           7    -    2  value 0
   Green              enumerator    enum Color                 -           7    -    3  value 5
   Blue               enumerator    enum Color                 -           7    -    2  value 6
   (unnamed at 8:9)   enum_tag      enum (unnamed at 8:9)      -           8    -    0  
   Lo                 enumerator    Level                      -           8    -    0  value 0
   Hi                 enumerator    Level                      -           8    -    1  value 1
   Level              typedef       Level                      -           8    -    0  
   Word               union_tag     union Word                 -           9    -    0  size 4
   Wide               union_tag     union Wide                 -          10    -    0  size 8
   Tagged             struct_tag    struct Tagged              -          11    -    0  size 8
   g                  variable      union Word                 global     12    4    2  
   table              variable      int[7]                     global     13   28    1  
   show               function      int (int)                  -          15    -    1  _Z4showi; defined
   show               function      int (enum Color)           -          16    -    1  _Z4show5Color; defined
   show               function      int (Level)                -          17    -    1  _Z4show5Level; defined
   name               function      const char *(enum Color)   -          18    -    2  _Z4name5Color; defined
   flip               function      union Word (union Word)    -          25    -    1  _Z4flip4Word; defined
   sumBytes           function      int (union Word *)         -          26    -    1  _Z8sumBytesP4Word; defined
   main               function      int (void)                 -          28    -    0  defined

 scope: global > union Word
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  field         int                        member      9    4   13  Word::i; public, offset 0
   f                  field         float                      member      9    4    3  Word::f; public, offset 0
   b                  field         unsigned char[4]           member      9    4    8  Word::b; public, offset 0
   h                  field         short[2]                   member      9    4    1  Word::h; public, offset 0

 scope: global > union Wide
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  field         double                     member     10    8    2  Wide::d; public, offset 0
   ll                 field         long long                  member     10    8    1  Wide::ll; public, offset 0
   half               field         int[2]                     member     10    8    3  Wide::half; public, offset 0

 scope: global > struct Tagged
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               field         enum Color                 member     11    4    1  Tagged::kind; public, offset 0
   v                  field         union Word                 member     11    4    1  Tagged::v; public, offset 4

 scope: global > show()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      15    4    0  x.1
   c                  parameter     enum Color                 param      16    4    0  c.2
   l                  parameter     Level                      param      17    4    0  l.3

 scope: global > name()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     enum Color                 param      18    4    1  c.4

 scope: global > flip()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  parameter     union Word                 param      25    4    3  w.5

 scope: global > sumBytes()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     union Word *               param      26    4    4  p.6

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      enum Color                 local      29    4    4  c.7
   d                  variable      enum Color                 local      30    4    1  d.8
   l                  variable      Level                      local      31    4    1  l.9
   n                  variable      int                        local      32    4    2  n.10
   big                variable      bool                       local      33    1    1  big.11
   e                  variable      enum Color                 local      34    4    1  e.12
   (unnamed at 35:5)  enum_tag      enum (unnamed at 35:5)     -          35    -    0  
   Small              enumerator    enum (unnamed at 35:5)     -          35    -    1  value 4
   Large              enumerator    enum (unnamed at 35:5)     -          35    -    1  value 16
   size               variable      enum (unnamed at 35:5)     local      35    4    1  size.13
   t                  variable      struct Tagged              local      36    8    2  t.14
   w                  variable      union Word                 local      40    4   13  w.15
   f1                 variable      float                      local      42    4    1  f1.16
   i1                 variable      int                        local      44    4    1  i1.17
   i2                 variable      int                        local      46    4    1  i2.18
   i3                 variable      int                        local      48    4    1  i3.19
   i4                 variable      int                        local      50    4    1  i4.20
   fl                 variable      union Word                 local      51    4    1  fl.21
   gb                 variable      int                        local      53    4    1  gb.22
   arr                variable      union Word[3]              local      56   12    4  arr.23
   k                  variable      int                        local      57    4   11  k.24
   s                  variable      int                        local      57    4    2  s.25
   x                  variable      union Wide                 local      60    8    6  x.26
   hi                 variable      int                        local      62    4    1  hi.27

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

union Word: size 4, align 4
    +0  int i  [public]
    +0  float f  [public]
    +0  unsigned char[4] b  [public]
    +0  short[2] h  [public]
union Wide: size 8, align 8
    +0  double d  [public]
    +0  long long ll  [public]
    +0  int[2] half  [public]
struct Tagged: size 8, align 4
    +0  enum Color kind  [public]
    +4  union Word v  [public]
enum Color: int
    Red = 0
    Green = 5
    Blue = 6
Level: int
    Lo = 0
    Hi = 1
enum (unnamed at 35:5): int
    Small = 4
    Large = 16
