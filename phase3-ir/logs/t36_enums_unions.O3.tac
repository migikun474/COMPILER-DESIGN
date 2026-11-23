============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t36_enums_unions.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 171 -> 120 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          171 -> 120   (29% fewer)

   constants folded                       11
   algebraic simplifications               5
   common subexpressions                   3
   copies / constants forwarded           42
   temporaries merged away                 4
   dead instructions removed              22
   jumps removed or redirected            15
   unreachable instructions removed       20
   propagated across blocks                6
   dead assignments removed               17
   calls inlined                           7
   tail calls turned into jumps            0
   common subexpressions across blocks      2
   loops unrolled                          2
   unreachable functions removed           6

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
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 21 parameter(s)/local(s), 41 temporaries, frame 388 bytes

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
   t34              temp    unsigned char                   1     240
   t35              temp    int                             4     244
   t38              temp    unsigned char                   1     256
   t39              temp    int                             4     260
   t40              temp    int                             4     264
   t43              temp    int                             4     276
   t44              temp    union Word *                    4     280
   t46              temp    double                          8     288
   t52              temp    union Word                      4     316
   t53              temp    int                             4     320
   t54              temp    unsigned int                    4     324
   t56              temp    unsigned char                   1     332
   t57              temp    int                             4     336
   t58              temp    union Word *                    4     340
   t59              temp    unsigned char                   1     344
   t60              temp    int                             4     348
   t61              temp    int                             4     352
   t62              temp    union Word *                    4     356
   t63              temp    unsigned char                   1     360
   t64              temp    int                             4     364
   t65              temp    int                             4     368
   t66              temp    union Word *                    4     372
   t67              temp    unsigned char                   1     376
   t68              temp    int                             4     380
   t69              temp    int                             4     384
   (28 temporaries no longer used after optimization not shown)

 Code: 120 instruction(s)

    100       t[0] = 5
    101       t[4] = 42
    102       param "%s %s %d %d %d %d %d\n"
    103       param "blue"
    104       param "green"
    105       param 7
    106       param 1
    107       param 2
    108       param 1
    109       param 3
    110       call printf, 8
    111       t11 = t[0]
    112       t12 = t[4]
    113       param "%d %d %d %d %d\n"
    114       param 6
    115       param 16
    116       param t11
    117       param t12
    118       param 28
    119       call printf, 6
    120       w[0] = 1078530011
    121       t13 = w[0]
    122       w[0] = 2.0
    123       t14 = w[0]
    124       w[0] = 7
    125       w[0] = 1
    126       t18 = w[0]
    127       w[2] = 2
    128       t19 = w[0]
    129       t52 = w
    130       t53 = t52[0]
    131       t54 = t53 uint^ 2147483648
    132       t52[0] = t54
    133       fl = t52
    134       g[0] = -1.5
    135       t22 = g[0]
    136       t23 = floattodouble t13
    137       t24 = fl[0]
    138       param "%.4f %x %d %x %x %x %x\n"
    139       param t23
    140       param t14
    141       param 14
    142       param t18
    143       param t19
    144       param t24
    145       param t22
    146       call printf, 8
    147       s = 0
    148       k = 0
    149  L1:  if k int>= 3 goto L2
    150       t25 = k int<< 2                     (w = 4)
    151       t26 = k int<< 8
    152       t27 = t26 int+ 1
    153       arr[t25] = t27
    154       k = k int+ 1
    155       if k int>= 3 goto L2
    156       t25 = k int<< 2                     (w = 4)
    157       t26 = k int<< 8
    158       t27 = t26 int+ 1
    159       arr[t25] = t27
    160       k = k int+ 1
    161       goto L1
    162  L2:  k = 0
    163  L3:  if k int>= 3 goto L6
    164       t29 = k int<< 2                     (w = 4)
    165       t30 = t29 int+ 1
    166       t31 = arr[t30]
    167       t32 = uchartoint t31
    168       if t32 int<= 0 goto L4
    169       t34 = arr[t29]
    170       t35 = uchartoint t34
    171       t38 = arr[t30]
    172       t39 = uchartoint t38
    173       t40 = t35 int+ t39
    174       s = s int+ t40
    175  L4:  k = k int+ 1
    176       if k int>= 3 goto L6
    177       t29 = k int<< 2                     (w = 4)
    178       t30 = t29 int+ 1
    179       t31 = arr[t30]
    180       t32 = uchartoint t31
    181       if t32 int<= 0 goto L5
    182       t34 = arr[t29]
    183       t35 = uchartoint t34
    184       t38 = arr[t30]
    185       t39 = uchartoint t38
    186       t40 = t35 int+ t39
    187       s = s int+ t40
    188  L5:  k = k int+ 1
    189       goto L3
    190  L6:  x[0] = 1.0
    191       t43 = x[4]
    192       x[0] = 5
    193       x[0] = 0
    194       x[4] = 1073741824
    195       t44 = &w
    196       t56 = *t44
    197       t57 = uchartoint t56
    198       t58 = t44 ptr+ 1
    199       t59 = *t58
    200       t60 = uchartoint t59
    201       t61 = t57 int+ t60
    202       t62 = t44 ptr+ 2
    203       t63 = *t62
    204       t64 = uchartoint t63
    205       t65 = t61 int+ t64
    206       t66 = t44 ptr+ 3
    207       t67 = *t66
    208       t68 = uchartoint t67
    209       t69 = t65 int+ t68
    210       t46 = x[0]
    211       param "%d %d %x %.1f %d %d\n"
    212       param s
    213       param t69
    214       param t43
    215       param t46
    216       param 8
    217       param 4
    218       call printf, 7
    219       return 0


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
