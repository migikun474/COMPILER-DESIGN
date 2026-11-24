============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_scopes_enums.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 92 -> 102 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           92 -> 102   (-10% fewer)

   calls inlined                          11
   constants folded                        1
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded           24
   temporaries merged away                 4
   dead instructions removed              16
   jumps removed or redirected             1
   unreachable instructions removed        2

----------------------------------------------------------------------------
 GLOBALS: 6 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   x                int                             4  1
   rate             double                          8  5.0
   part             float                           4  1.25
   chosen           double                          8  2.5
   n.6              int                             4  0
   n.7              int                             4  10

 As three address code (initial values, in place before main runs):

    x = 1
    rate = 5.0
    part = 1.25
    chosen = 2.5
    n.6 = 0                   (zero-initialized)
    n.7 = 10

============================================================================
 FUNCTION show(int)        (link name _Z4showi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0

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
 FUNCTION globalX()        (link name _Z7globalXv)
============================================================================

 Code: 1 instruction(s)

    102     return x

============================================================================
 FUNCTION hide(int)        (link name _Z4hidei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x.3              param   int                             4       0
   r                local   int                             4       4
   x.5              local   int                             4       8
   t1               temp    int                             4      12
   t3               temp    int                             4      20
   (1 temporary no longer used after optimization not shown)

 Code: 6 instruction(s)

    103     r = x.3
    104     x.5 = 50
    105     t1 = x.3 int+ 50
    106     r = t1
    107     t3 = t1 int+ x
    108     return t3

============================================================================
 FUNCTION countA()        (link name _Z6countAv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    109     t1 = n.6 int+ 1
    110     n.6 = t1
    111     return t1

============================================================================
 FUNCTION countB()        (link name _Z6countBv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    112     t1 = n.7 int+ 1
    113     n.7 = t1
    114     return t1

============================================================================
 FUNCTION name(enum Color)        (link name _Z4name5Color)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   enum Color                      4       0
   t1               temp    int                             4       4

 Code: 8 instruction(s)

    115       t1 = c
    116       goto L4
    117  L1:  return "red"
    118  L2:  return "green"
    119  L3:  return "blue"
    120  L4:  if t1 int== 0 goto L1
    121       if t1 int== 5 goto L2
    122       goto L3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 12 temporaries, frame 168 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   total            local   int                             4       0
   i.10             local   int                             4       4
   i.11             local   int                             4       8
   before           local   int                             4      12
   x.13             local   int                             4      16
   r                local   int[3]                         12      20
   n.15             local   int                             4      32
   c                local   enum Color                      4      36
   l                local   Level                           4      40
   t2               temp    double                          8      48
   t7               temp    int                             4      72
   t9               temp    int                             4      80
   t10              temp    const char *                    4      84
   t11              temp    const char *                    4      88
   t18              temp    int                             4     116
   t19              temp    int                             4     120
   t22              temp    int                             4     132
   t23              temp    int                             4     136
   t24              temp    int                             4     140
   t26              temp    int                             4     148
   t28              temp    int                             4     156
   (18 temporaries no longer used after optimization not shown)

 Code: 79 instruction(s)

    123        t18 = call globalX(), 0
    124        t19 = 53 int+ t18
    125        t2 = floattodouble part
    126        param "%d %d %.2f %.2f %.1f\n"
    127        param t19
    128        param x
    129        param rate
    130        param t2
    131        param chosen
    132        call printf, 6
    133        total = 0
    134        i.10 = 0
    135  L5:   if i.10 int>= 3 goto L6
    136        i.11 = 7
    137        total = total int+ 7
    138        i.10 = i.10 int+ 1
    139        goto L5
    140  L6:   param "%d %d\n"
    141        param total
    142        param i.10
    143        call printf, 3
    144        before = x
    145        x.13 = 40
    146        param "%d %d\n"
    147        param x
    148        param 40
    149        call printf, 3
    150        n.6 = n.6 int+ 1
    151        n.7 = n.7 int+ 1
    152        t22 = n.6 int+ 1
    153        n.6 = t22
    154        t23 = t22 int+ 1
    155        n.6 = t23
    156        t24 = n.7 int+ 1
    157        n.7 = t24
    158        param "%d %d\n"
    159        param t23
    160        param t24
    161        call printf, 3
    162        r[0] = 1
    163        r[4] = 2
    164        r[8] = 3
    165        t7 = r[0]
    166        t9 = t7 int+ 3
    167        n.15 = t9
    168        c = 6
    169        l = 1
    170        t26 = 6
    171        goto L10
    172  L7:   t10 = "red"
    173        goto L11
    174  L8:   t10 = "green"
    175        goto L11
    176  L9:   t10 = "blue"
    177        goto L11
    178  L10:  if t26 int== 0 goto L7
    179        if t26 int== 5 goto L8
    180        goto L9
    181  L11:  t28 = 5
    182        goto L15
    183  L12:  t11 = "red"
    184        goto L16
    185  L13:  t11 = "green"
    186        goto L16
    187  L14:  t11 = "blue"
    188        goto L16
    189  L15:  if t28 int== 0 goto L12
    190        if t28 int== 5 goto L13
    191        goto L14
    192  L16:  param "%d %s %s %d %d %d %d\n"
    193        param t9
    194        param t10
    195        param t11
    196        param 6
    197        param 2
    198        param 1
    199        param 1
    200        call printf, 8
    201        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Color              enum_tag      enum Color                 -           7    -    0  
   Red                enumerator    enum Color                 -           7    -    1  value 0
   Green              enumerator    enum Color                 -           7    -    2  value 5
   Blue               enumerator    enum Color                 -           7    -    1  value 6
   (unnamed at 8:9)   enum_tag      enum (unnamed at 8:9)      -           8    -    0  
   Lo                 enumerator    Level                      -           8    -    0  value 0
   Hi                 enumerator    Level                      -           8    -    1  value 1
   Level              typedef       Level                      -           8    -    0  
   Number             typedef       int                        -           9    -    0  
   Row                typedef       int[3]                     -          10    -    0  
   x                  variable      int                        global     11    4    3  
   rate               variable      double                     global     12    8    1  
   part               variable      float                      global     13    4    1  
   chosen             variable      double                     global     14    8    1  
   show               function      int (int)                  -          15    -    1  _Z4showi; defined
   show               function      int (enum Color)           -          16    -    1  _Z4show5Color; defined
   globalX            function      int (void)                 -          17    -    1  _Z7globalXv; defined
   hide               function      int (int)                  -          18    -    1  _Z4hidei; defined
   countA             function      int (void)                 -          19    -    3  _Z6countAv; defined
   countB             function      int (void)                 -          20    -    2  _Z6countBv; defined
   name               function      const char *(enum Color)   -          21    -    2  _Z4name5Color; defined
   main               function      int (void)                 -          22    -    0  defined

 scope: global > show()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      15    4    0  v.1
   c                  parameter     enum Color                 param      16    4    0  c.2

 scope: global > hide()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      18    4    1  x.3
   r                  variable      int                        local      18    4    2  r.4

 scope: global > hide() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      18    4    1  x.5

 scope: global > countA()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static     19    4    1  n.6; static

 scope: global > countB()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static     20    4    1  n.7; static

 scope: global > name()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     enum Color                 param      21    4    1  c.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      24    4    2  total.9
   i                  variable      int                        local      24    4    4  i.10
   before             variable      int                        local      27    4    1  before.12
   x                  variable      int                        local      28    4    1  x.13
   r                  variable      int[3]                     local      32   12    2  r.14
   n                  variable      int                        local      33    4    1  n.15
   c                  variable      enum Color                 local      34    4    2  c.16
   l                  variable      Level                      local      35    4    1  l.17

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      25    4    1  i.11

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

enum Color: int
    Red = 0
    Green = 5
    Blue = 6
Level: int
    Lo = 0
    Hi = 1

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

54 1 5.00 1.25 2.5
21 3
1 40
3 12
4 blue green 6 2 1 1

   exit code 0, 82 instructions executed
