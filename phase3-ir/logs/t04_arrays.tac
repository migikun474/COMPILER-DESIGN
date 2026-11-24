============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t04_arrays.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 129 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   n                param   int                             4       4
   s                local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int *                           4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32

 Code: 13 instruction(s)

    100       s = 0
    101       i = 0
    102  L1:  if i int< n goto L2
    103       goto L3
    104  L2:  t1 = i int* 4
    105       t2 = a ptr+ t1
    106       t3 = *t2
    107       t4 = s int+ t3
    108       s = t4
    109       t5 = i int+ 1
    110       i = t5
    111       goto L1
    112  L3:  return s

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

    113     t1 = *m
    114     t2 = m ptr+ 16
    115     t3 = *t2
    116     t4 = t1 int+ t3
    117     t5 = m ptr+ 32
    118     t6 = *t5
    119     t7 = t4 int+ t6
    120     return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 33 temporaries, frame 244 bytes

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
   t5               temp    int *                           4     128
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
   t17              temp    int                             4     176
   t18              temp    int                             4     180
   t19              temp    int                             4     184
   t20              temp    int                             4     188
   t21              temp    int                             4     192
   t22              temp    int                             4     196
   t23              temp    int                             4     200
   t24              temp    int                             4     204
   t25              temp    int                             4     208
   t26              temp    int                             4     212
   t27              temp    int                             4     216
   t28              temp    int                             4     220
   t29              temp    char *                          4     224
   t30              temp    char                            1     228
   t31              temp    int                             4     232
   t32              temp    char *                          4     236
   t33              temp    int                             4     240

 Code: 108 instruction(s)

    121        a[0] = 4
    122        a[4] = 8
    123        a[8] = 0
    124        a[12] = 0
    125        a[16] = 1
    126        a[20] = 0
    127        m[0] = 1
    128        m[4] = 2
    129        m[8] = 3
    130        m[12] = 4
    131        m[16] = 5
    132        m[20] = 6
    133        m[24] = 7
    134        m[28] = 8
    135        m[32] = 9
    136        cube[0] = 1
    137        cube[4] = 2
    138        cube[8] = 3
    139        cube[12] = 4
    140        cube[16] = 5
    141        cube[20] = 6
    142        cube[24] = 7
    143        cube[28] = 8
    144        t1 = &a
    145        param t1
    146        param 6
    147        t2 = call sum(int *, int), 2
    148        t3 = a[12]
    149        t4 = a[16]
    150        t5 = &a
    151        t6 = t5 ptr+ 8
    152        t7 = *t6
    153        param "%d %d %d %d\n"
    154        param t2
    155        param t3
    156        param t4
    157        param t7
    158        call printf, 5
    159        t8 = &m
    160        param t8
    161        t9 = call trace(int (*)[3]), 1
    162        t10 = m[24]
    163        t11 = m[8]
    164        t12 = t10 int* t11
    165        t13 = cube[20]
    166        param "%d %d %d\n"
    167        param t9
    168        param t12
    169        param t13
    170        call printf, 4
    171        s = 0
    172        i = 0
    173  L4:   if i int< 3 goto L5
    174        goto L9
    175  L5:   j = 0
    176  L6:   if j int< 3 goto L7
    177        goto L8
    178  L7:   t14 = i int* 3                      (n2 = 3)
    179        t15 = t14 int+ j
    180        t16 = t15 int* 4                    (w = 4)
    181        t17 = i int* 3
    182        t18 = t17 int+ j
    183        m[t16] = t18
    184        t19 = j int+ 1
    185        j = t19
    186        goto L6
    187  L8:   t20 = i int+ 1
    188        i = t20
    189        goto L4
    190  L9:   i = 0
    191  L10:  if i int< 3 goto L11
    192        goto L12
    193  L11:  t21 = i int* 3                      (n2 = 3)
    194        t22 = 2 int- i
    195        t23 = t21 int+ t22
    196        t24 = t23 int* 4                    (w = 4)
    197        t25 = m[t24]
    198        t26 = s int+ t25
    199        s = t26
    200        t27 = i int+ 1
    201        i = t27
    202        goto L10
    203  L12:  t28 = zero[12]
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
    222        t33 = 36 int/ 12
    223        param "%s %d %d\n"
    224        param t32
    225        param 8
    226        param t33
    227        call printf, 4
    228        return 0


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
