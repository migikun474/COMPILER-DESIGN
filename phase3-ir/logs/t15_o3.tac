============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_o3.c
   Optimization  : no optimization
   Result        : Three address code generated: 9 function(s), 122 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Code: 7 instruction(s)

    102       if v int< lo goto L1
    103       goto L2
    104  L1:  return lo
    105  L2:  if v int> hi goto L3
    106       goto L4
    107  L3:  return hi
    108  L4:  return v

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

    109     t1 = calls int+ 1
    110     calls = t1
    111     t2 = v int+ calls
    112     return t2

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

    113     t1 = *r
    114     t2 = t1 int+ 1
    115     *r = t2
    116     return

============================================================================
 FUNCTION sumP(struct P)        (link name _Z4sumP1P)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct P                        8       0
   t1               temp    int                             4       8

 Code: 3 instruction(s)

    117     p[0] = 0
    118     t1 = p[4]
    119     return t1

============================================================================
 FUNCTION fact(int)        (link name _Z4facti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16

 Code: 10 instruction(s)

    120       if n int<= 1 goto L5
    121       goto L6
    122  L5:  t1 = 1
    123       goto L7
    124  L6:  t2 = n int- 1
    125       param t2
    126       t3 = call fact(int), 1
    127       t4 = n int* t3
    128       t1 = t4
    129  L7:  return t1

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

 Code: 9 instruction(s)

    130       if a int<= 0 goto L8
    131       goto L9
    132  L8:  return b
    133  L9:  t1 = b int- 1
    134       t2 = a int- 1
    135       param t1
    136       param t2
    137       t3 = call down(int, int), 2
    138       return t3

============================================================================
 FUNCTION divide(int, int)        (link name _Z6divideii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   d                param   int                             4       4
   s                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20

 Code: 10 instruction(s)

    139        s = 0
    140  L10:  if n int> 0 goto L11
    141        goto L12
    142  L11:  t1 = 100 int/ d
    143        t2 = s int+ t1
    144        s = t2
    145        t3 = n int- 1
    146        n = t3
    147        goto L10
    148  L12:  return s

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 20 temporaries, frame 104 bytes

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
   t6               temp    int                             4      44
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
   t17              temp    int                             4      88
   t18              temp    int                             4      92
   t19              temp    int                             4      96
   t20              temp    int                             4     100

 Code: 73 instruction(s)

    149        param 1
    150        t1 = call counted(int), 1
    151        param 1
    152        t2 = call counted(int), 1
    153        t3 = t1 int+ t2
    154        r = t3
    155        v = 3
    156        t4 = &v
    157        param t4
    158        call inc(int &), 1
    159        p[0] = 5
    160        p[4] = 6
    161        param 7
    162        t5 = call sq(int), 1
    163        t6 = int- 4
    164        param t6
    165        param 0
    166        param 9
    167        t7 = call clamp(int, int, int), 3
    168        param 50
    169        param 0
    170        param 9
    171        t8 = call clamp(int, int, int), 3
    172        param "%d %d %d %d %d\n"
    173        param t5
    174        param t7
    175        param t8
    176        param r
    177        param calls
    178        call printf, 6
    179        param p
    180        t9 = call sumP(struct P), 1
    181        t10 = p[0]
    182        param 6
    183        t11 = call fact(int), 1
    184        param "%d %d %d %d\n"
    185        param v
    186        param t9
    187        param t10
    188        param t11
    189        call printf, 5
    190        param 7
    191        param 3
    192        t12 = call down(int, int), 2
    193        param 0
    194        param 0
    195        t13 = call divide(int, int), 2
    196        param 3
    197        param 4
    198        t14 = call divide(int, int), 2
    199        param "%d %d %d\n"
    200        param t12
    201        param t13
    202        param t14
    203        call printf, 4
    204        t15 = v int* 3
    205        x = t15
    206        if x int> 10 goto L13
    207        goto L14
    208  L13:  t16 = v int* 3
    209        t17 = t16 int+ 1
    210        t = t17
    211        goto L15
    212  L14:  t18 = v int* 3
    213        t19 = t18 int- 1
    214        t = t19
    215  L15:  v = 100
    216        t20 = v int* 3
    217        param "%d %d\n"
    218        param t
    219        param t20
    220        call printf, 3
    221        return 0


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
