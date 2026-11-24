============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 129 -> 128 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          129 -> 128   (0% fewer)

   constants folded                        1
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded            9
   temporaries merged away                 6
   dead instructions removed               7
   jumps removed or redirected             4
   unreachable instructions removed        0
   propagated across blocks                2
   dead assignments removed                2
   calls inlined                           2
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          4
   unreachable functions removed           2

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   zero             int[5]                         20  0

 As three address code (initial values, in place before main runs):

    zero[...] = 0                  (zero-initialized)

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 35 temporaries, frame 304 bytes

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
   (13 temporaries no longer used after optimization not shown)

 Code: 128 instruction(s)

    100       a[0] = 4
    101       a[4] = 8
    102       a[8] = 0
    103       a[12] = 0
    104       a[16] = 1
    105       a[20] = 0
    106       m[0] = 1
    107       m[4] = 2
    108       m[8] = 3
    109       m[12] = 4
    110       m[16] = 5
    111       m[20] = 6
    112       m[24] = 7
    113       m[28] = 8
    114       m[32] = 9
    115       cube[0] = 1
    116       cube[4] = 2
    117       cube[8] = 3
    118       cube[12] = 4
    119       cube[16] = 5
    120       cube[20] = 6
    121       cube[24] = 7
    122       cube[28] = 8
    123       t1 = &a
    124       t36 = 0
    125       t37 = 0
    126  L1:  if t37 int>= 6 goto L2
    127       t38 = t37 int<< 2
    128       t39 = t1 ptr+ t38
    129       t40 = *t39
    130       t36 = t36 int+ t40
    131       t37 = t37 int+ 1
    132       if t37 int>= 6 goto L2
    133       t38 = t37 int<< 2
    134       t39 = t1 ptr+ t38
    135       t40 = *t39
    136       t36 = t36 int+ t40
    137       t37 = t37 int+ 1
    138       goto L1
    139  L2:  t3 = a[12]
    140       t4 = a[16]
    141       t6 = t1 ptr+ 8
    142       t7 = *t6
    143       param "%d %d %d %d\n"
    144       param t36
    145       param t3
    146       param t4
    147       param t7
    148       call printf, 5
    149       t8 = &m
    150       t42 = *t8
    151       t43 = t8 ptr+ 16
    152       t44 = *t43
    153       t45 = t42 int+ t44
    154       t46 = t8 ptr+ 32
    155       t47 = *t46
    156       t48 = t45 int+ t47
    157       t10 = m[24]
    158       t11 = m[8]
    159       t12 = t10 int* t11
    160       t13 = cube[20]
    161       param "%d %d %d\n"
    162       param t48
    163       param t12
    164       param t13
    165       call printf, 4
    166       s = 0
    167       i = 0
    168  L3:  if i int>= 3 goto L6
    169       j = 0
    170  L4:  if j int>= 3 goto L5
    171       t14 = i int* 3                      (n2 = 3)
    172       t15 = t14 int+ j
    173       t16 = t15 int<< 2                   (w = 4)
    174       m[t16] = t15
    175       j = j int+ 1
    176       if j int>= 3 goto L5
    177       t14 = i int* 3                      (n2 = 3)
    178       t15 = t14 int+ j
    179       t16 = t15 int<< 2                   (w = 4)
    180       m[t16] = t15
    181       j = j int+ 1
    182       goto L4
    183  L5:  i = i int+ 1
    184       goto L3
    185  L6:  i = 0
    186  L7:  if i int>= 3 goto L8
    187       t21 = i int* 3                      (n2 = 3)
    188       t22 = 2 int- i
    189       t23 = t21 int+ t22
    190       t24 = t23 int<< 2                   (w = 4)
    191       t25 = m[t24]
    192       s = s int+ t25
    193       i = i int+ 1
    194       if i int>= 3 goto L8
    195       t21 = i int* 3                      (n2 = 3)
    196       t22 = 2 int- i
    197       t23 = t21 int+ t22
    198       t24 = t23 int<< 2                   (w = 4)
    199       t25 = m[t24]
    200       s = s int+ t25
    201       i = i int+ 1
    202       goto L7
    203  L8:  t28 = zero[12]
    204       t29 = "xyz" ptr+ 1
    205       t30 = *t29
    206       t31 = chartoint t30
    207       param "%d %d %c\n"
    208       param s
    209       param t28
    210       param t31
    211       call printf, 4
    212       word[0] = 104
    213       word[1] = 101
    214       word[2] = 121
    215       word[3] = 0
    216       word[4] = 0
    217       word[5] = 0
    218       word[6] = 0
    219       word[7] = 0
    220       word[3] = 33
    221       t32 = &word
    222       param "%s %d %d\n"
    223       param t32
    224       param 8
    225       param 3
    226       call printf, 4
    227       return 0


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
