============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t36_enums.c
   Optimization  : no optimization
   Result        : Three address code generated: 6 function(s), 97 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   table            int[7]                         28  0

 As three address code (initial values, in place before main runs):

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
 FUNCTION next(enum Color)        (link name _Z4next5Color)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   enum Color                      4       0
   t1               temp    enum Color                      4       4
   t2               temp    enum Color                      4       8

 Code: 11 instruction(s)

    113        if c int== 6 goto L6
    114        goto L7
    115  L6:   t1 = 0
    116        goto L11
    117  L7:   if c int== 0 goto L8
    118        goto L9
    119  L8:   t2 = 5
    120        goto L10
    121  L9:   t2 = 6
    122  L10:  t1 = t2
    123  L11:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 18 temporaries, frame 116 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                local   enum Color                      4       0
   d                local   enum Color                      4       4
   l                local   Level                           4       8
   n                local   int                             4      12
   big              local   bool                            1      16
   e                local   enum Color                      4      20
   size             local   enum (unnamed at 30:5)          4      24
   t                local   struct Tagged                   8      28
   steps            local   int                             4      36
   walk             local   enum Color                      4      40
   t1               temp    int                             4      44
   t2               temp    int                             4      48
   t3               temp    bool                            1      52
   t4               temp    enum Color                      4      56
   t5               temp    const char *                    4      60
   t6               temp    const char *                    4      64
   t7               temp    int                             4      68
   t8               temp    int                             4      72
   t9               temp    int                             4      76
   t10              temp    int                             4      80
   t11              temp    enum Color                      4      84
   t12              temp    int                             4      88
   t13              temp    enum Color                      4      92
   t14              temp    int                             4      96
   t15              temp    enum Color                      4     100
   t16              temp    const char *                    4     104
   t17              temp    int                             4     108
   t18              temp    int                             4     112

 Code: 73 instruction(s)

    124        c = 6
    125        d = 5
    126        l = 1
    127        t1 = c int+ 1
    128        n = t1
    129        if c int> 5 goto L12
    130        t2 = 0
    131        goto L13
    132  L12:  t2 = 1
    133  L13:  if t2 int!= 0 goto L14
    134        t3 = 0
    135        goto L15
    136  L14:  t3 = 1
    137  L15:  big = t3
    138        if n int> 3 goto L16
    139        goto L17
    140  L16:  t4 = 6
    141        goto L18
    142  L17:  t4 = 0
    143  L18:  e = t4
    144        size = 16
    145        t[0] = 5
    146        t[4] = 42
    147        param c
    148        t5 = call name(enum Color), 1
    149        param d
    150        t6 = call name(enum Color), 1
    151        t7 = booltoint big
    152        param c
    153        t8 = call show(enum Color), 1
    154        param 5
    155        t9 = call show(int), 1
    156        param l
    157        t10 = call show(Level), 1
    158        param "%s %s %d %d %d %d %d\n"
    159        param t5
    160        param t6
    161        param n
    162        param t7
    163        param t8
    164        param t9
    165        param t10
    166        call printf, 8
    167        t11 = t[0]
    168        t12 = t[4]
    169        param "%d %d %d %d %d\n"
    170        param e
    171        param size
    172        param t11
    173        param t12
    174        param 28
    175        call printf, 6
    176        steps = 0
    177        walk = 0
    178  L19:  param walk
    179        t13 = call next(enum Color), 1
    180        walk = t13
    181        t14 = steps int+ 1
    182        steps = t14
    183        if walk int!= 0 goto L19
    184        goto L20
    185  L20:  param 5
    186        t15 = call next(enum Color), 1
    187        param t15
    188        t16 = call name(enum Color), 1
    189        t17 = 0 int+ 5
    190        t18 = t17 int+ 6
    191        param "%d %s %d\n"
    192        param steps
    193        param t16
    194        param t18
    195        call printf, 4
    196        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Color              enum_tag      enum Color                 -           6    -    0  
   Red                enumerator    enum Color                 -           6    -    7  value 0
   Green              enumerator    enum Color                 -           6    -    6  value 5
   Blue               enumerator    enum Color                 -           6    -    5  value 6
   (unnamed at 7:9)   enum_tag      enum (unnamed at 7:9)      -           7    -    0  
   Lo                 enumerator    Level                      -           7    -    0  value 0
   Hi                 enumerator    Level                      -           7    -    1  value 1
   Level              typedef       Level                      -           7    -    0  
   Tagged             struct_tag    struct Tagged              -           8    -    0  size 8
   table              variable      int[7]                     global      9   28    1  
   show               function      int (int)                  -          11    -    1  _Z4showi; defined
   show               function      int (enum Color)           -          12    -    1  _Z4show5Color; defined
   show               function      int (Level)                -          13    -    1  _Z4show5Level; defined
   name               function      const char *(enum Color)   -          14    -    3  _Z4name5Color; defined
   next               function      enum Color (enum Color)    -          21    -    2  _Z4next5Color; defined
   main               function      int (void)                 -          23    -    0  defined

 scope: global > struct Tagged
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               field         enum Color                 member      8    4    1  Tagged::kind; public, offset 0
   value              field         int                        member      8    4    1  Tagged::value; public, offset 4

 scope: global > show()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      11    4    0  x.1
   c                  parameter     enum Color                 param      12    4    0  c.2
   l                  parameter     Level                      param      13    4    0  l.3

 scope: global > name()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     enum Color                 param      14    4    1  c.4

 scope: global > next()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     enum Color                 param      21    4    2  c.5

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      enum Color                 local      24    4    4  c.6
   d                  variable      enum Color                 local      25    4    1  d.7
   l                  variable      Level                      local      26    4    1  l.8
   n                  variable      int                        local      27    4    2  n.9
   big                variable      bool                       local      28    1    1  big.10
   e                  variable      enum Color                 local      29    4    1  e.11
   (unnamed at 30:5)  enum_tag      enum (unnamed at 30:5)     -          30    -    0  
   Small              enumerator    enum (unnamed at 30:5)     -          30    -    1  value 4
   Large              enumerator    enum (unnamed at 30:5)     -          30    -    1  value 16
   size               variable      enum (unnamed at 30:5)     local      30    4    1  size.12
   t                  variable      struct Tagged              local      31    8    2  t.13
   steps              variable      int                        local      34    4    2  steps.14
   walk               variable      enum Color                 local      35    4    3  walk.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Tagged: size 8, align 4
    +0  enum Color kind  [public]
    +4  int value  [public]
enum Color: int
    Red = 0
    Green = 5
    Blue = 6
Level: int
    Lo = 0
    Hi = 1
enum (unnamed at 30:5): int
    Small = 4
    Large = 16
