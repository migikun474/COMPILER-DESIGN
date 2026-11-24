============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_scopes_enums.c
   Optimization  : no optimization
   Result        : Three address code generated: 8 function(s), 92 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x.3              param   int                             4       0
   r                local   int                             4       4
   x.5              local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20

 Code: 7 instruction(s)

    103     r = x.3
    104     x.5 = 50
    105     t1 = r int+ x.5
    106     r = t1
    107     t2 = call globalX(), 0
    108     t3 = r int+ t2
    109     return t3

============================================================================
 FUNCTION countA()        (link name _Z6countAv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    110     t1 = n.6 int+ 1
    111     n.6 = t1
    112     return t1

============================================================================
 FUNCTION countB()        (link name _Z6countBv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    113     t1 = n.7 int+ 1
    114     n.7 = t1
    115     return t1

============================================================================
 FUNCTION name(enum Color)        (link name _Z4name5Color)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   enum Color                      4       0
   t1               temp    int                             4       4

 Code: 10 instruction(s)

    116       t1 = c
    117       goto L4
    118  L1:  return "red"
    119  L2:  return "green"
    120  L3:  return "blue"
    121       goto L5
    122  L4:  if t1 int== 0 goto L1
    123       if t1 int== 5 goto L2
    124       goto L3
    125  L5:  return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 13 temporaries, frame 100 bytes

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
   t1               temp    int                             4      44
   t2               temp    double                          8      48
   t3               temp    int                             4      56
   t4               temp    int                             4      60
   t5               temp    int                             4      64
   t6               temp    int                             4      68
   t7               temp    int                             4      72
   t8               temp    int                             4      76
   t9               temp    int                             4      80
   t10              temp    const char *                    4      84
   t11              temp    const char *                    4      88
   t12              temp    int                             4      92
   t13              temp    int                             4      96

 Code: 66 instruction(s)

    126       param 3
    127       t1 = call hide(int), 1
    128       t2 = floattodouble part
    129       param "%d %d %.2f %.2f %.1f\n"
    130       param t1
    131       param x
    132       param rate
    133       param t2
    134       param chosen
    135       call printf, 6
    136       total = 0
    137       i.10 = 0
    138  L6:  if i.10 int< 3 goto L7
    139       goto L8
    140  L7:  i.11 = 7
    141       t3 = total int+ i.11
    142       total = t3
    143       t4 = i.10 int+ 1
    144       i.10 = t4
    145       goto L6
    146  L8:  param "%d %d\n"
    147       param total
    148       param i.10
    149       call printf, 3
    150       before = x
    151       x.13 = 40
    152       param "%d %d\n"
    153       param before
    154       param x.13
    155       call printf, 3
    156       call countA(), 0
    157       call countB(), 0
    158       call countA(), 0
    159       t5 = call countA(), 0
    160       t6 = call countB(), 0
    161       param "%d %d\n"
    162       param t5
    163       param t6
    164       call printf, 3
    165       r[0] = 1
    166       r[4] = 2
    167       r[8] = 3
    168       t7 = r[0]
    169       t8 = r[8]
    170       t9 = t7 int+ t8
    171       n.15 = t9
    172       c = 6
    173       l = 1
    174       param c
    175       t10 = call name(enum Color), 1
    176       param 5
    177       t11 = call name(enum Color), 1
    178       param c
    179       t12 = call show(enum Color), 1
    180       param 3
    181       t13 = call show(int), 1
    182       param "%d %s %s %d %d %d %d\n"
    183       param n.15
    184       param t10
    185       param t11
    186       param 6
    187       param t12
    188       param t13
    189       param l
    190       call printf, 8
    191       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Color              enum_tag      enum Color                 -           5    -    0  
   Red                enumerator    enum Color                 -           5    -    1  value 0
   Green              enumerator    enum Color                 -           5    -    2  value 5
   Blue               enumerator    enum Color                 -           5    -    1  value 6
   (unnamed at 6:9)   enum_tag      enum (unnamed at 6:9)      -           6    -    0  
   Lo                 enumerator    Level                      -           6    -    0  value 0
   Hi                 enumerator    Level                      -           6    -    1  value 1
   Level              typedef       Level                      -           6    -    0  
   Number             typedef       int                        -           7    -    0  
   Row                typedef       int[3]                     -           8    -    0  
   x                  variable      int                        global      9    4    3  
   rate               variable      double                     global     10    8    1  
   part               variable      float                      global     11    4    1  
   chosen             variable      double                     global     12    8    1  
   show               function      int (int)                  -          13    -    1  _Z4showi; defined
   show               function      int (enum Color)           -          14    -    1  _Z4show5Color; defined
   globalX            function      int (void)                 -          15    -    1  _Z7globalXv; defined
   hide               function      int (int)                  -          16    -    1  _Z4hidei; defined
   countA             function      int (void)                 -          17    -    3  _Z6countAv; defined
   countB             function      int (void)                 -          18    -    2  _Z6countBv; defined
   name               function      const char *(enum Color)   -          19    -    2  _Z4name5Color; defined
   main               function      int (void)                 -          20    -    0  defined

 scope: global > show()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      13    4    0  v.1
   c                  parameter     enum Color                 param      14    4    0  c.2

 scope: global > hide()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      16    4    1  x.3
   r                  variable      int                        local      16    4    2  r.4

 scope: global > hide() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      16    4    1  x.5

 scope: global > countA()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static     17    4    1  n.6; static

 scope: global > countB()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static     18    4    1  n.7; static

 scope: global > name()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     enum Color                 param      19    4    1  c.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      22    4    2  total.9
   i                  variable      int                        local      22    4    4  i.10
   before             variable      int                        local      25    4    1  before.12
   x                  variable      int                        local      26    4    1  x.13
   r                  variable      int[3]                     local      30   12    2  r.14
   n                  variable      int                        local      31    4    1  n.15
   c                  variable      enum Color                 local      32    4    2  c.16
   l                  variable      Level                      local      33    4    1  l.17

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      23    4    1  i.11

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
