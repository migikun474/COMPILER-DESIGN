============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t36_enums.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 97 -> 100 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           97 -> 100   (-3% fewer)

   calls inlined                           8
   constants folded                        9
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           34
   temporaries merged away                 1
   dead instructions removed              21
   jumps removed or redirected             9
   unreachable instructions removed       12

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
 FUNCTION next(enum Color)        (link name _Z4next5Color)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   enum Color                      4       0
   t1               temp    enum Color                      4       4
   t2               temp    enum Color                      4       8

 Code: 9 instruction(s)

    111       if c int!= 6 goto L5
    112       t1 = 0
    113       goto L8
    114  L5:  if c int!= 0 goto L6
    115       t2 = 5
    116       goto L7
    117  L6:  t2 = 6
    118  L7:  t1 = t2
    119  L8:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 11 temporaries, frame 176 bytes

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
   t5               temp    const char *                    4      60
   t6               temp    const char *                    4      64
   t11              temp    enum Color                      4      84
   t12              temp    int                             4      88
   t16              temp    const char *                    4     104
   t20              temp    int                             4     120
   t22              temp    int                             4     128
   t26              temp    enum Color                      4     144
   t27              temp    enum Color                      4     148
   t28              temp    enum Color                      4     152
   t33              temp    int                             4     172
   (22 temporaries no longer used after optimization not shown)

 Code: 80 instruction(s)

    120        c = 6
    121        d = 5
    122        l = 1
    123        n = 7
    124        big = 1
    125        e = 6
    126        size = 16
    127        t[0] = 5
    128        t[4] = 42
    129        t20 = 6
    130        goto L12
    131  L9:   t5 = "red"
    132        goto L13
    133  L10:  t5 = "green"
    134        goto L13
    135  L11:  t5 = "blue"
    136        goto L13
    137  L12:  if t20 int== 0 goto L9
    138        if t20 int== 5 goto L10
    139        goto L11
    140  L13:  t22 = 5
    141        goto L17
    142  L14:  t6 = "red"
    143        goto L18
    144  L15:  t6 = "green"
    145        goto L18
    146  L16:  t6 = "blue"
    147        goto L18
    148  L17:  if t22 int== 0 goto L14
    149        if t22 int== 5 goto L15
    150        goto L16
    151  L18:  param "%s %s %d %d %d %d %d\n"
    152        param t5
    153        param t6
    154        param 7
    155        param 1
    156        param 2
    157        param 1
    158        param 3
    159        call printf, 8
    160        t11 = t[0]
    161        t12 = t[4]
    162        param "%d %d %d %d %d\n"
    163        param 6
    164        param 16
    165        param t11
    166        param t12
    167        param 28
    168        call printf, 6
    169        steps = 0
    170        walk = 0
    171  L19:  t26 = walk
    172        if walk int!= 6 goto L20
    173        t27 = 0
    174        goto L23
    175  L20:  if t26 int!= 0 goto L21
    176        t28 = 5
    177        goto L22
    178  L21:  t28 = 6
    179  L22:  t27 = t28
    180  L23:  walk = t27
    181        steps = steps int+ 1
    182        if t27 int!= 0 goto L19
    183        t33 = 6
    184        goto L27
    185  L24:  t16 = "red"
    186        goto L28
    187  L25:  t16 = "green"
    188        goto L28
    189  L26:  t16 = "blue"
    190        goto L28
    191  L27:  if t33 int== 0 goto L24
    192        if t33 int== 5 goto L25
    193        goto L26
    194  L28:  param "%d %s %d\n"
    195        param steps
    196        param t16
    197        param 11
    198        call printf, 4
    199        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

blue green 7 1 2 1 3
6 16 5 42 28
3 blue 11

   exit code 0, 79 instructions executed
