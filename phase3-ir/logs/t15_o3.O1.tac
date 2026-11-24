============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_o3.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 122 -> 113 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          122 -> 113   (7% fewer)

   calls inlined                           9
   constants folded                        6
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded           31
   temporaries merged away                 5
   dead instructions removed              21
   jumps removed or redirected             9
   unreachable instructions removed        7

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

 Symbol table: 5 parameter(s)/local(s), 24 temporaries, frame 216 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   int                             4       0
   v                local   int                             4       4
   p                local   struct P                        8       8
   x                local   int                             4      16
   t                local   int                             4      20
   t3               temp    int                             4      32
   t4               temp    int *                           4      36
   t10              temp    int                             4      60
   t11              temp    int                             4      64
   t12              temp    int                             4      68
   t13              temp    int                             4      72
   t15              temp    int                             4      80
   t16              temp    int                             4      84
   t18              temp    int                             4      92
   t22              temp    int                             4     108
   t23              temp    int                             4     112
   t26              temp    int                             4     124
   t28              temp    int                             4     132
   t29              temp    int                             4     136
   t38              temp    struct P                        8     172
   t39              temp    int                             4     180
   t40              temp    int                             4     184
   t41              temp    int                             4     188
   t42              temp    int                             4     192
   t43              temp    int                             4     196
   t44              temp    int                             4     200
   t45              temp    int                             4     204
   t46              temp    int                             4     208
   t47              temp    int                             4     212
   (23 temporaries no longer used after optimization not shown)

 Code: 72 instruction(s)

    141        t22 = calls int+ 1
    142        calls = t22
    143        t23 = 1 int+ t22
    144        calls = t23
    145        t26 = 1 int+ t23
    146        t3 = t23 int+ t26
    147        r = t3
    148        v = 3
    149        t4 = &v
    150        t28 = *t4
    151        t29 = t28 int+ 1
    152        *t4 = t29
    153        p[0] = 5
    154        p[4] = 6
    155        param "%d %d %d %d %d\n"
    156        param 49
    157        param 0
    158        param 9
    159        param t3
    160        param calls
    161        call printf, 6
    162        t38 = p
    163        t38[0] = 0
    164        t39 = t38[4]
    165        t10 = p[0]
    166        param 6
    167        t11 = call fact(int), 1
    168        param "%d %d %d %d\n"
    169        param v
    170        param t39
    171        param t10
    172        param t11
    173        call printf, 5
    174        param 7
    175        param 3
    176        t12 = call down(int, int), 2
    177        t40 = 0
    178        t41 = 0
    179        t42 = 0
    180  L8:   if t40 int<= 0 goto L9
    181        t43 = 100 int/ t41
    182        t42 = t42 int+ t43
    183        t40 = t40 int- 1
    184        goto L8
    185  L9:   t13 = t42
    186        t44 = 3
    187        t45 = 4
    188        t46 = 0
    189  L10:  if t44 int<= 0 goto L11
    190        t47 = 100 int/ t45
    191        t46 = t46 int+ t47
    192        t44 = t44 int- 1
    193        goto L10
    194  L11:  param "%d %d %d\n"
    195        param t12
    196        param t13
    197        param t46
    198        call printf, 4
    199        t15 = v int* 3
    200        x = t15
    201        if t15 int<= 10 goto L12
    202        t16 = v int* 3
    203        t = t16 int+ 1
    204        goto L13
    205  L12:  t18 = v int* 3
    206        t = t18 int- 1
    207  L13:  v = 100
    208        param "%d %d\n"
    209        param t
    210        param 300
    211        call printf, 3
    212        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

49 0 9 5 2
4 6 5 720
4 0 75
13 300

   exit code 0, 134 instructions executed
