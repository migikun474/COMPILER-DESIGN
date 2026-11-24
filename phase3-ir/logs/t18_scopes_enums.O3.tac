============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t18_scopes_enums.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 92 -> 55 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           92 -> 55   (40% fewer)

   constants folded                        5
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded           22
   temporaries merged away                 4
   dead instructions removed              13
   jumps removed or redirected             9
   unreachable instructions removed       14
   propagated across blocks                6
   dead assignments removed               12
   calls inlined                          11
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          1
   unreachable functions removed           6

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
 FUNCTION globalX()        (link name _Z7globalXv)
============================================================================

 Code: 1 instruction(s)

    100     return x

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 8 temporaries, frame 152 bytes

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
   t16              temp    int                             4     108
   t17              temp    int                             4     112
   t20              temp    int                             4     124
   t21              temp    int                             4     128
   t22              temp    int                             4     132
   (18 temporaries no longer used after optimization not shown)

 Code: 54 instruction(s)

    101       t16 = call globalX(), 0
    102       t17 = 53 int+ t16
    103       t2 = floattodouble part
    104       param "%d %d %.2f %.2f %.1f\n"
    105       param t17
    106       param x
    107       param rate
    108       param t2
    109       param chosen
    110       call printf, 6
    111       total = 0
    112       i.10 = 0
    113  L1:  if i.10 int>= 3 goto L2
    114       total = total int+ 7
    115       i.10 = i.10 int+ 1
    116       if i.10 int>= 3 goto L2
    117       total = total int+ 7
    118       i.10 = i.10 int+ 1
    119       goto L1
    120  L2:  param "%d %d\n"
    121       param total
    122       param i.10
    123       call printf, 3
    124       param "%d %d\n"
    125       param x
    126       param 40
    127       call printf, 3
    128       n.6 = n.6 int+ 1
    129       n.7 = n.7 int+ 1
    130       t20 = n.6 int+ 1
    131       n.6 = t20
    132       t21 = t20 int+ 1
    133       n.6 = t21
    134       t22 = n.7 int+ 1
    135       n.7 = t22
    136       param "%d %d\n"
    137       param t21
    138       param t22
    139       call printf, 3
    140       r[0] = 1
    141       r[4] = 2
    142       r[8] = 3
    143       t7 = r[0]
    144       t9 = t7 int+ 3
    145       param "%d %s %s %d %d %d %d\n"
    146       param t9
    147       param "blue"
    148       param "green"
    149       param 6
    150       param 2
    151       param 1
    152       param 1
    153       call printf, 8
    154       return 0


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
