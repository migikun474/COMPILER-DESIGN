============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t36_enums_unions.c
   Optimization  : no optimization
   Result        : Three address code generated: 7 function(s), 172 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Code: 10 instruction(s)

    103       t1 = c
    104       goto L4
    105  L1:  return "red"
    106  L2:  return "green"
    107  L3:  return "blue"
    108       goto L5
    109  L4:  if t1 int== 0 goto L1
    110       if t1 int== 5 goto L2
    111       goto L3
    112  L5:  return

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

    113     t1 = w[0]
    114     t2 = t1 uint^ 2147483648
    115     w[0] = t2
    116     return w

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

    117     t1 = *p
    118     t2 = uchartoint t1
    119     t3 = p ptr+ 1
    120     t4 = *t3
    121     t5 = uchartoint t4
    122     t6 = t2 int+ t5
    123     t7 = p ptr+ 2
    124     t8 = *t7
    125     t9 = uchartoint t8
    126     t10 = t6 int+ t9
    127     t11 = p ptr+ 3
    128     t12 = *t11
    129     t13 = uchartoint t12
    130     t14 = t10 int+ t13
    131     return t14

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 21 parameter(s)/local(s), 47 temporaries, frame 296 bytes

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
   t1               temp    int                             4     100
   t2               temp    int                             4     104
   t3               temp    bool                            1     108
   t4               temp    enum Color                      4     112
   t5               temp    const char *                    4     116
   t6               temp    const char *                    4     120
   t7               temp    int                             4     124
   t8               temp    int                             4     128
   t9               temp    int                             4     132
   t10              temp    int                             4     136
   t11              temp    enum Color                      4     140
   t12              temp    int                             4     144
   t13              temp    float                           4     148
   t14              temp    int                             4     152
   t15              temp    int                             4     156
   t16              temp    int                             4     160
   t17              temp    int                             4     164
   t18              temp    int                             4     168
   t19              temp    int                             4     172
   t20              temp    union Word                      4     176
   t21              temp    union Word *                    4     180
   t22              temp    float                           4     184
   t23              temp    int                             4     188
   t24              temp    double                          8     192
   t25              temp    int                             4     200
   t26              temp    int                             4     204
   t27              temp    int                             4     208
   t28              temp    int                             4     212
   t29              temp    int                             4     216
   t30              temp    int                             4     220
   t31              temp    int                             4     224
   t32              temp    unsigned char                   1     228
   t33              temp    int                             4     232
   t34              temp    int                             4     236
   t35              temp    unsigned char                   1     240
   t36              temp    int                             4     244
   t37              temp    int                             4     248
   t38              temp    int                             4     252
   t39              temp    unsigned char                   1     256
   t40              temp    int                             4     260
   t41              temp    int                             4     264
   t42              temp    int                             4     268
   t43              temp    int                             4     272
   t44              temp    int                             4     276
   t45              temp    union Word *                    4     280
   t46              temp    int                             4     284
   t47              temp    double                          8     288

 Code: 140 instruction(s)

    132        c = 6
    133        d = 5
    134        l = 1
    135        t1 = c int+ 1
    136        n = t1
    137        if c int> 5 goto L6
    138        t2 = 0
    139        goto L7
    140  L6:   t2 = 1
    141  L7:   if t2 int!= 0 goto L8
    142        t3 = 0
    143        goto L9
    144  L8:   t3 = 1
    145  L9:   big = t3
    146        if n int> 3 goto L10
    147        goto L11
    148  L10:  t4 = 6
    149        goto L12
    150  L11:  t4 = 0
    151  L12:  e = t4
    152        size = 16
    153        t[0] = 5
    154        t[4] = 42
    155        param c
    156        t5 = call name(enum Color), 1
    157        param d
    158        t6 = call name(enum Color), 1
    159        t7 = booltoint big
    160        param c
    161        t8 = call show(enum Color), 1
    162        param 5
    163        t9 = call show(int), 1
    164        param l
    165        t10 = call show(Level), 1
    166        param "%s %s %d %d %d %d %d\n"
    167        param t5
    168        param t6
    169        param n
    170        param t7
    171        param t8
    172        param t9
    173        param t10
    174        call printf, 8
    175        t11 = t[0]
    176        t12 = t[4]
    177        param "%d %d %d %d %d\n"
    178        param e
    179        param size
    180        param t11
    181        param t12
    182        param 28
    183        call printf, 6
    184        w[0] = 1078530011
    185        t13 = w[0]
    186        f1 = t13
    187        w[0] = 2.0
    188        t14 = w[0]
    189        i1 = t14
    190        w[0] = 7
    191        t15 = w[0]
    192        t16 = w[0]
    193        t17 = t15 int+ t16
    194        i2 = t17
    195        w[0] = 1
    196        t18 = w[0]
    197        i3 = t18
    198        w[2] = 2
    199        t19 = w[0]
    200        i4 = t19
    201        param w
    202        t20 = call flip(union Word), 1
    203        fl = t20
    204        t21 = &fl
    205        t22 = float- 1.5
    206        g[0] = t22
    207        t23 = g[0]
    208        gb = t23
    209        t24 = floattodouble f1
    210        t25 = fl[0]
    211        param "%.4f %x %d %x %x %x %x\n"
    212        param t24
    213        param i1
    214        param i2
    215        param i3
    216        param i4
    217        param t25
    218        param gb
    219        call printf, 8
    220        s = 0
    221        k = 0
    222  L13:  if k int< 3 goto L14
    223        goto L15
    224  L14:  t26 = k int* 4                      (w = 4)
    225        t27 = k int* 256
    226        t28 = t27 int+ 1
    227        arr[t26] = t28
    228        t29 = k int+ 1
    229        k = t29
    230        goto L13
    231  L15:  k = 0
    232  L16:  if k int< 3 goto L17
    233        goto L20
    234  L17:  t30 = k int* 4                      (w = 4)
    235        t31 = t30 int+ 1
    236        t32 = arr[t31]
    237        t33 = uchartoint t32
    238        if t33 int> 0 goto L18
    239        goto L19
    240  L18:  t34 = k int* 4                      (w = 4)
    241        t35 = arr[t34]
    242        t36 = uchartoint t35
    243        t37 = k int* 4                      (w = 4)
    244        t38 = t37 int+ 1
    245        t39 = arr[t38]
    246        t40 = uchartoint t39
    247        t41 = t36 int+ t40
    248        t42 = s int+ t41
    249        s = t42
    250  L19:  t43 = k int+ 1
    251        k = t43
    252        goto L16
    253  L20:  x[0] = 1.0
    254        t44 = x[4]
    255        hi = t44
    256        x[0] = 5
    257        x[0] = 0
    258        x[4] = 1073741824
    259        t45 = &w
    260        param t45
    261        t46 = call sumBytes(union Word *), 1
    262        t47 = x[0]
    263        param "%d %d %x %.1f %d %d\n"
    264        param s
    265        param t46
    266        param hi
    267        param t47
    268        param 8
    269        param 4
    270        call printf, 7
    271        return 0


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
