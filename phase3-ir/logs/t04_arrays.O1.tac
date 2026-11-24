============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 129 -> 128 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          129 -> 128   (0% fewer)

   calls inlined                           2
   constants folded                        1
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded            9
   temporaries merged away                 6
   dead instructions removed               7
   jumps removed or redirected             4
   unreachable instructions removed        0

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   zero             int[5]                         20  0

 As three address code (initial values, in place before main runs):

    zero[...] = 0                  (zero-initialized)

============================================================================
 FUNCTION sum(int *, int)        (link name _Z3sumPii)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int *                           4      20
   t3               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    100       s = 0
    101       i = 0
    102  L1:  if i int>= n goto L2
    103       t1 = i int<< 2
    104       t2 = a ptr+ t1
    105       t3 = *t2
    106       s = s int+ t3
    107       i = i int+ 1
    108       goto L1
    109  L2:  return s

============================================================================
 FUNCTION trace(int (*)[3])        (link name _Z5tracePA3_i)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   m                param   int (*)[3]                      4       0
   t1               temp    int                             4       4
   t2               temp    int (*)[3]                      4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int (*)[3]                      4      20
   t6               temp    int                             4      24
   t7               temp    int                             4      28

 Code: 8 instruction(s)

    110     t1 = *m
    111     t2 = m ptr+ 16
    112     t3 = *t2
    113     t4 = t1 int+ t3
    114     t5 = m ptr+ 32
    115     t6 = *t5
    116     t7 = t4 int+ t6
    117     return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 37 temporaries, frame 304 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int[6]                         24       0
   m                local   int[3][3]                      36      24
   cube             local   int[2][2][2]                   32      60
   i                local   int                             4      92
   j                local   int                             4      96
   s                local   int                             4     100
   word             local   char[8]                         8     104
   t1               temp    int *                           4     112
   t3               temp    int                             4     120
   t4               temp    int                             4     124
   t6               temp    int *                           4     132
   t7               temp    int                             4     136
   t8               temp    int (*)[3]                      4     140
   t10              temp    int                             4     148
   t11              temp    int                             4     152
   t12              temp    int                             4     156
   t13              temp    int                             4     160
   t14              temp    int                             4     164
   t15              temp    int                             4     168
   t16              temp    int                             4     172
   t21              temp    int                             4     192
   t22              temp    int                             4     196
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t25              temp    int                             4     208
   t28              temp    int                             4     220
   t29              temp    char *                          4     224
   t30              temp    char                            1     228
   t31              temp    int                             4     232
   t32              temp    char *                          4     236
   t34              temp    int *                           4     244
   t35              temp    int                             4     248
   t36              temp    int                             4     252
   t37              temp    int                             4     256
   t38              temp    int                             4     260
   t39              temp    int *                           4     264
   t40              temp    int                             4     268
   t42              temp    int                             4     276
   t43              temp    int (*)[3]                      4     280
   t44              temp    int                             4     284
   t45              temp    int                             4     288
   t46              temp    int (*)[3]                      4     292
   t47              temp    int                             4     296
   t48              temp    int                             4     300
   (11 temporaries no longer used after optimization not shown)

 Code: 110 instruction(s)

    118        a[0] = 4
    119        a[4] = 8
    120        a[8] = 0
    121        a[12] = 0
    122        a[16] = 1
    123        a[20] = 0
    124        m[0] = 1
    125        m[4] = 2
    126        m[8] = 3
    127        m[12] = 4
    128        m[16] = 5
    129        m[20] = 6
    130        m[24] = 7
    131        m[28] = 8
    132        m[32] = 9
    133        cube[0] = 1
    134        cube[4] = 2
    135        cube[8] = 3
    136        cube[12] = 4
    137        cube[16] = 5
    138        cube[20] = 6
    139        cube[24] = 7
    140        cube[28] = 8
    141        t1 = &a
    142        t34 = t1
    143        t35 = 6
    144        t36 = 0
    145        t37 = 0
    146  L3:   if t37 int>= t35 goto L4
    147        t38 = t37 int<< 2
    148        t39 = t34 ptr+ t38
    149        t40 = *t39
    150        t36 = t36 int+ t40
    151        t37 = t37 int+ 1
    152        goto L3
    153  L4:   t3 = a[12]
    154        t4 = a[16]
    155        t6 = t1 ptr+ 8
    156        t7 = *t6
    157        param "%d %d %d %d\n"
    158        param t36
    159        param t3
    160        param t4
    161        param t7
    162        call printf, 5
    163        t8 = &m
    164        t42 = *t8
    165        t43 = t8 ptr+ 16
    166        t44 = *t43
    167        t45 = t42 int+ t44
    168        t46 = t8 ptr+ 32
    169        t47 = *t46
    170        t48 = t45 int+ t47
    171        t10 = m[24]
    172        t11 = m[8]
    173        t12 = t10 int* t11
    174        t13 = cube[20]
    175        param "%d %d %d\n"
    176        param t48
    177        param t12
    178        param t13
    179        call printf, 4
    180        s = 0
    181        i = 0
    182  L5:   if i int>= 3 goto L8
    183        j = 0
    184  L6:   if j int>= 3 goto L7
    185        t14 = i int* 3                      (n2 = 3)
    186        t15 = t14 int+ j
    187        t16 = t15 int<< 2                   (w = 4)
    188        m[t16] = t15
    189        j = j int+ 1
    190        goto L6
    191  L7:   i = i int+ 1
    192        goto L5
    193  L8:   i = 0
    194  L9:   if i int>= 3 goto L10
    195        t21 = i int* 3                      (n2 = 3)
    196        t22 = 2 int- i
    197        t23 = t21 int+ t22
    198        t24 = t23 int<< 2                   (w = 4)
    199        t25 = m[t24]
    200        s = s int+ t25
    201        i = i int+ 1
    202        goto L9
    203  L10:  t28 = zero[12]
    204        t29 = "xyz" ptr+ 1
    205        t30 = *t29
    206        t31 = chartoint t30
    207        param "%d %d %c\n"
    208        param s
    209        param t28
    210        param t31
    211        call printf, 4
    212        word[0] = 104
    213        word[1] = 101
    214        word[2] = 121
    215        word[3] = 0
    216        word[4] = 0
    217        word[5] = 0
    218        word[6] = 0
    219        word[7] = 0
    220        word[3] = 33
    221        t32 = &word
    222        param "%s %d %d\n"
    223        param t32
    224        param 8
    225        param 3
    226        call printf, 4
    227        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   zero               variable      int[5]                     global      6   20    1  
   sum                function      int (int *, int)           -           7    -    1  _Z3sumPii; defined
   trace              function      int (int (*)[3])           -           8    -    1  _Z5tracePA3_i; defined
   main               function      int (void)                 -           9    -    0  defined

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       7    4    1  a.1
   n                  parameter     int                        param       7    4    1  n.2
   s                  variable      int                        local       7    4    2  s.3
   i                  variable      int                        local       7    4    4  i.4

 scope: global > trace()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   m                  parameter     int (*)[3]                 param       8    4    3  m.5

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int[6]                     local      10   24    4  a.6
   m                  variable      int[3][3]                  local      11   36    7  m.7
   cube               variable      int[2][2][2]               local      12   32    1  cube.8
   i                  variable      int                        local      15    4   10  i.9
   j                  variable      int                        local      15    4    5  j.10
   s                  variable      int                        local      15    4    2  s.11
   word               variable      char[8]                    local      19    8    3  word.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

13 0 1 0
15 21 6
12 0 y
hey! 8 3

   exit code 0, 233 instructions executed
