============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 129 -> 115 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          129 -> 115   (10% fewer)

   constants folded                        1
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded            4
   temporaries merged away                 6
   dead instructions removed               4
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

 Symbol table: 7 parameter(s)/local(s), 25 temporaries, frame 244 bytes

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
   t2               temp    int                             4     116
   t3               temp    int                             4     120
   t4               temp    int                             4     124
   t6               temp    int *                           4     132
   t7               temp    int                             4     136
   t8               temp    int (*)[3]                      4     140
   t9               temp    int                             4     144
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
   (8 temporaries no longer used after optimization not shown)

 Code: 97 instruction(s)

    118       a[0] = 4
    119       a[4] = 8
    120       a[8] = 0
    121       a[12] = 0
    122       a[16] = 1
    123       a[20] = 0
    124       m[0] = 1
    125       m[4] = 2
    126       m[8] = 3
    127       m[12] = 4
    128       m[16] = 5
    129       m[20] = 6
    130       m[24] = 7
    131       m[28] = 8
    132       m[32] = 9
    133       cube[0] = 1
    134       cube[4] = 2
    135       cube[8] = 3
    136       cube[12] = 4
    137       cube[16] = 5
    138       cube[20] = 6
    139       cube[24] = 7
    140       cube[28] = 8
    141       t1 = &a
    142       param t1
    143       param 6
    144       t2 = call sum(int *, int), 2
    145       t3 = a[12]
    146       t4 = a[16]
    147       t6 = t1 ptr+ 8
    148       t7 = *t6
    149       param "%d %d %d %d\n"
    150       param t2
    151       param t3
    152       param t4
    153       param t7
    154       call printf, 5
    155       t8 = &m
    156       param t8
    157       t9 = call trace(int (*)[3]), 1
    158       t10 = m[24]
    159       t11 = m[8]
    160       t12 = t10 int* t11
    161       t13 = cube[20]
    162       param "%d %d %d\n"
    163       param t9
    164       param t12
    165       param t13
    166       call printf, 4
    167       s = 0
    168       i = 0
    169  L3:  if i int>= 3 goto L6
    170       j = 0
    171  L4:  if j int>= 3 goto L5
    172       t14 = i int* 3                      (n2 = 3)
    173       t15 = t14 int+ j
    174       t16 = t15 int<< 2                   (w = 4)
    175       m[t16] = t15
    176       j = j int+ 1
    177       goto L4
    178  L5:  i = i int+ 1
    179       goto L3
    180  L6:  i = 0
    181  L7:  if i int>= 3 goto L8
    182       t21 = i int* 3                      (n2 = 3)
    183       t22 = 2 int- i
    184       t23 = t21 int+ t22
    185       t24 = t23 int<< 2                   (w = 4)
    186       t25 = m[t24]
    187       s = s int+ t25
    188       i = i int+ 1
    189       goto L7
    190  L8:  t28 = zero[12]
    191       t29 = "xyz" ptr+ 1
    192       t30 = *t29
    193       t31 = chartoint t30
    194       param "%d %d %c\n"
    195       param s
    196       param t28
    197       param t31
    198       call printf, 4
    199       word[0] = 104
    200       word[1] = 101
    201       word[2] = 121
    202       word[3] = 0
    203       word[4] = 0
    204       word[5] = 0
    205       word[6] = 0
    206       word[7] = 0
    207       word[3] = 33
    208       t32 = &word
    209       param "%s %d %d\n"
    210       param t32
    211       param 8
    212       param 3
    213       call printf, 4
    214       return 0


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
