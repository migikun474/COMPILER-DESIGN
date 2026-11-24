============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_o3.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 122 -> 107 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          122 -> 107   (12% fewer)

   constants folded                        2
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            6
   temporaries merged away                 5
   dead instructions removed               2
   jumps removed or redirected             6
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

============================================================================
 FUNCTION sq(int)        (link name _Z2sqi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    100     t1 = v int* v
    101     return t1

============================================================================
 FUNCTION clamp(int, int, int)        (link name _Z5clampiii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   lo               param   int                             4       4
   hi               param   int                             4       8

 Code: 5 instruction(s)

    102       if v int>= lo goto L1
    103       return lo
    104  L1:  if v int<= hi goto L2
    105       return hi
    106  L2:  return v

============================================================================
 FUNCTION counted(int)        (link name _Z7countedi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    107     t1 = calls int+ 1
    108     calls = t1
    109     t2 = v int+ t1
    110     return t2

============================================================================
 FUNCTION inc(int &)        (link name _Z3incRi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   int &                           4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    111     t1 = *r
    112     t2 = t1 int+ 1
    113     *r = t2
    114     return

============================================================================
 FUNCTION sumP(struct P)        (link name _Z4sumP1P)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct P                        8       0
   t1               temp    int                             4       8

 Code: 3 instruction(s)

    115     p[0] = 0
    116     t1 = p[4]
    117     return t1

============================================================================
 FUNCTION fact(int)        (link name _Z4facti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    118       if n int> 1 goto L3
    119       t1 = 1
    120       goto L4
    121  L3:  t2 = n int- 1
    122       param t2
    123       t3 = call fact(int), 1
    124       t1 = n int* t3
    125  L4:  return t1

============================================================================
 FUNCTION down(int, int)        (link name _Z4downii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16

 Code: 8 instruction(s)

    126       if a int> 0 goto L5
    127       return b
    128  L5:  t1 = b int- 1
    129       t2 = a int- 1
    130       param t1
    131       param t2
    132       t3 = call down(int, int), 2
    133       return t3

============================================================================
 FUNCTION divide(int, int)        (link name _Z6divideii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   d                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    134       s = 0
    135  L6:  if n int<= 0 goto L7
    136       t1 = 100 int/ d
    137       s = s int+ t1
    138       n = n int- 1
    139       goto L6
    140  L7:  return s

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 16 temporaries, frame 104 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   int                             4       0
   v                local   int                             4       4
   p                local   struct P                        8       8
   x                local   int                             4      16
   t                local   int                             4      20
   t1               temp    int                             4      24
   t2               temp    int                             4      28
   t3               temp    int                             4      32
   t4               temp    int *                           4      36
   t5               temp    int                             4      40
   t7               temp    int                             4      48
   t8               temp    int                             4      52
   t9               temp    int                             4      56
   t10              temp    int                             4      60
   t11              temp    int                             4      64
   t12              temp    int                             4      68
   t13              temp    int                             4      72
   t14              temp    int                             4      76
   t15              temp    int                             4      80
   t16              temp    int                             4      84
   t18              temp    int                             4      92
   (4 temporaries no longer used after optimization not shown)

 Code: 66 instruction(s)

    141       param 1
    142       t1 = call counted(int), 1
    143       param 1
    144       t2 = call counted(int), 1
    145       t3 = t1 int+ t2
    146       v = 3
    147       t4 = &v
    148       param t4
    149       call inc(int &), 1
    150       p[0] = 5
    151       p[4] = 6
    152       param 7
    153       t5 = call sq(int), 1
    154       param -4
    155       param 0
    156       param 9
    157       t7 = call clamp(int, int, int), 3
    158       param 50
    159       param 0
    160       param 9
    161       t8 = call clamp(int, int, int), 3
    162       param "%d %d %d %d %d\n"
    163       param t5
    164       param t7
    165       param t8
    166       param t3
    167       param calls
    168       call printf, 6
    169       param p
    170       t9 = call sumP(struct P), 1
    171       t10 = p[0]
    172       param 6
    173       t11 = call fact(int), 1
    174       param "%d %d %d %d\n"
    175       param v
    176       param t9
    177       param t10
    178       param t11
    179       call printf, 5
    180       param 7
    181       param 3
    182       t12 = call down(int, int), 2
    183       param 0
    184       param 0
    185       t13 = call divide(int, int), 2
    186       param 3
    187       param 4
    188       t14 = call divide(int, int), 2
    189       param "%d %d %d\n"
    190       param t12
    191       param t13
    192       param t14
    193       call printf, 4
    194       t15 = v int* 3
    195       if t15 int<= 10 goto L8
    196       t16 = v int* 3
    197       t = t16 int+ 1
    198       goto L9
    199  L8:  t18 = v int* 3
    200       t = t18 int- 1
    201  L9:  v = 100
    202       param "%d %d\n"
    203       param t
    204       param 300
    205       call printf, 3
    206       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   P                  struct_tag    struct P                   -           6    -    0  size 8
   calls              variable      int                        global      7    4    3  
   sq                 function      int (int)                  -           8    -    1  _Z2sqi; defined
   clamp              function      int (int, int, int)        -           9    -    2  _Z5clampiii; defined
   counted            function      int (int)                  -          10    -    2  _Z7countedi; defined
   inc                function      void (int &)               -          11    -    1  _Z3incRi; defined
   sumP               function      int (struct P)             -          12    -    1  _Z4sumP1P; defined
   fact               function      int (int)                  -          13    -    2  _Z4facti; defined
   down               function      int (int, int)             -          14    -    2  _Z4downii; defined
   divide             function      int (int, int)             -          15    -    2  _Z6divideii; defined
   main               function      int (void)                 -          16    -    0  defined

 scope: global > struct P
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member      6    4    2  P::a; public, offset 0
   b                  field         int                        member      6    4    1  P::b; public, offset 4

 scope: global > sq()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       8    4    2  v.1

 scope: global > clamp()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       9    4    3  v.2
   lo                 parameter     int                        param       9    4    2  lo.3
   hi                 parameter     int                        param       9    4    2  hi.4

 scope: global > counted()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      10    4    1  v.5

 scope: global > inc()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     int &                      param      11    4    1  r.6

 scope: global > sumP()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct P                   param      12    8    2  p.7

 scope: global > fact()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      13    4    3  n.8

 scope: global > down()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      14    4    2  a.9
   b                  parameter     int                        param      14    4    2  b.10

 scope: global > divide()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      15    4    2  n.11
   d                  parameter     int                        param      15    4    1  d.12
   s                  variable      int                        local      15    4    2  s.13

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      int                        local      17    4    1  r.14
   v                  variable      int                        local      18    4    7  v.15
   p                  variable      struct P                   local      20    8    2  p.16
   x                  variable      int                        local      24    4    1  x.17
   t                  variable      int                        local      24    4    3  t.18

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct P: size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
