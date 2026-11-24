============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_o3.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 122 -> 91 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          122 -> 91   (25% fewer)

   constants folded                        7
   algebraic simplifications               0
   common subexpressions                   1
   copies / constants forwarded           35
   temporaries merged away                 5
   dead instructions removed              24
   jumps removed or redirected            10
   unreachable instructions removed        8
   propagated across blocks                4
   dead assignments removed                6
   calls inlined                          10
   tail calls turned into jumps            1
   common subexpressions across blocks      0
   loops unrolled                          4
   unreachable functions removed           7

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

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

    100       if n int> 1 goto L1
    101       t1 = 1
    102       goto L2
    103  L1:  t2 = n int- 1
    104       param t2
    105       t3 = call fact(int), 1
    106       t1 = n int* t3
    107  L2:  return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 23 temporaries, frame 232 bytes

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
   t46              temp    int                             4     208
   t47              temp    int                             4     212
   t48              temp    int                             4     216
   t50              temp    int                             4     224
   (28 temporaries no longer used after optimization not shown)

 Code: 83 instruction(s)

    108        t22 = calls int+ 1
    109        calls = t22
    110        t23 = 1 int+ t22
    111        calls = t23
    112        t26 = 1 int+ t23
    113        t3 = t23 int+ t26
    114        v = 3
    115        t4 = &v
    116        t28 = *t4
    117        t29 = t28 int+ 1
    118        *t4 = t29
    119        p[0] = 5
    120        p[4] = 6
    121        param "%d %d %d %d %d\n"
    122        param 49
    123        param 0
    124        param 9
    125        param t3
    126        param calls
    127        call printf, 6
    128        t38 = p
    129        t38[0] = 0
    130        t39 = t38[4]
    131        t10 = p[0]
    132        param 6
    133        t11 = call fact(int), 1
    134        param "%d %d %d %d\n"
    135        param v
    136        param t39
    137        param t10
    138        param t11
    139        call printf, 5
    140        t40 = 7
    141        t41 = 3
    142  L3:   if t40 int<= 0 goto L4
    143        t42 = t41 int- 1
    144        t43 = t40 int- 1
    145        t40 = t42
    146        t41 = t43
    147        if t42 int<= 0 goto L4
    148        t42 = t41 int- 1
    149        t43 = t40 int- 1
    150        t40 = t42
    151        t41 = t43
    152        goto L3
    153  L4:   t44 = 0
    154        t46 = 0
    155  L5:   if t44 int<= 0 goto L6
    156        t47 = 100 int/ 0
    157        t46 = t46 int+ t47
    158        t44 = t44 int- 1
    159        if t44 int<= 0 goto L6
    160        t47 = 100 int/ 0
    161        t46 = t46 int+ t47
    162        t44 = t44 int- 1
    163        goto L5
    164  L6:   t48 = 3
    165        t50 = 0
    166  L7:   if t48 int<= 0 goto L8
    167        t50 = t50 int+ 25
    168        t48 = t48 int- 1
    169        if t48 int<= 0 goto L8
    170        t50 = t50 int+ 25
    171        t48 = t48 int- 1
    172        goto L7
    173  L8:   param "%d %d %d\n"
    174        param t41
    175        param t46
    176        param t50
    177        call printf, 4
    178        t15 = v int* 3
    179        if t15 int<= 10 goto L9
    180        t16 = v int* 3
    181        t = t16 int+ 1
    182        goto L10
    183  L9:   t18 = v int* 3
    184        t = t18 int- 1
    185  L10:  v = 100
    186        param "%d %d\n"
    187        param t
    188        param 300
    189        call printf, 3
    190        return 0


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
