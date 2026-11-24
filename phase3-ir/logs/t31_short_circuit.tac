============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t31_short_circuit.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 136 instruction(s)

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
 FUNCTION t(int)        (link name _Z1ti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    100     t1 = calls int* 10
    101     t2 = t1 int+ v
    102     calls = t2
    103     return v

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 34 temporaries, frame 200 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r1               local   int                             4       0
   r2               local   int                             4       4
   r3               local   int                             4       8
   r4               local   int                             4      12
   r5               local   int                             4      16
   a                local   int                             4      20
   b                local   int                             4      24
   c                local   int                             4      28
   arr              local   int[5]                         20      32
   i                local   int                             4      52
   n                local   int                             4      56
   k                local   int                             4      60
   t1               temp    int                             4      64
   t2               temp    int                             4      68
   t3               temp    int                             4      72
   t4               temp    int                             4      76
   t5               temp    int                             4      80
   t6               temp    int                             4      84
   t7               temp    int                             4      88
   t8               temp    int                             4      92
   t9               temp    int                             4      96
   t10              temp    int                             4     100
   t11              temp    int                             4     104
   t12              temp    int                             4     108
   t13              temp    int                             4     112
   t14              temp    int                             4     116
   t15              temp    int                             4     120
   t16              temp    int                             4     124
   t17              temp    int                             4     128
   t18              temp    int                             4     132
   t19              temp    int                             4     136
   t20              temp    int                             4     140
   t21              temp    int                             4     144
   t22              temp    int                             4     148
   t23              temp    int                             4     152
   t24              temp    int                             4     156
   t25              temp    int                             4     160
   t26              temp    int                             4     164
   t27              temp    int                             4     168
   t28              temp    int                             4     172
   t29              temp    int                             4     176
   t30              temp    int                             4     180
   t31              temp    int                             4     184
   t32              temp    int                             4     188
   t33              temp    int                             4     192
   t34              temp    int                             4     196

 Code: 132 instruction(s)

    104        param 0
    105        t2 = call t(int), 1
    106        if t2 int!= 0 goto L1
    107        goto L2
    108  L1:   param 1
    109        t3 = call t(int), 1
    110        if t3 int!= 0 goto L3
    111        goto L2
    112  L2:   t1 = 0
    113        goto L4
    114  L3:   t1 = 1
    115  L4:   r1 = t1
    116        param 2
    117        t5 = call t(int), 1
    118        if t5 int!= 0 goto L7
    119        goto L5
    120  L5:   param 3
    121        t6 = call t(int), 1
    122        if t6 int!= 0 goto L7
    123        goto L6
    124  L6:   t4 = 0
    125        goto L8
    126  L7:   t4 = 1
    127  L8:   r2 = t4
    128        param 0
    129        t8 = call t(int), 1
    130        if t8 int!= 0 goto L10
    131        goto L9
    132  L9:   param 4
    133        t9 = call t(int), 1
    134        if t9 int!= 0 goto L10
    135        goto L12
    136  L10:  param 5
    137        t10 = call t(int), 1
    138        if t10 int!= 0 goto L13
    139        goto L11
    140  L11:  param 6
    141        t11 = call t(int), 1
    142        if t11 int!= 0 goto L13
    143        goto L12
    144  L12:  t7 = 0
    145        goto L14
    146  L13:  t7 = 1
    147  L14:  r3 = t7
    148        param "%d %d %d %d\n"
    149        param r1
    150        param r2
    151        param r3
    152        param calls
    153        call printf, 5
    154        calls = 0
    155        param 1
    156        t13 = call t(int), 1
    157        if t13 int!= 0 goto L15
    158        goto L16
    159  L15:  param 7
    160        t14 = call t(int), 1
    161        t12 = t14
    162        goto L17
    163  L16:  param 8
    164        t15 = call t(int), 1
    165        t12 = t15
    166  L17:  r4 = t12
    167        param 0
    168        call t(int), 1
    169        param 9
    170        t16 = call t(int), 1
    171        r5 = t16
    172        param "%d %d %d\n"
    173        param r4
    174        param r5
    175        param calls
    176        call printf, 4
    177        c = 4
    178        b = 4
    179        a = 4
    180        t17 = c int* 2
    181        c = t17
    182        t18 = b int- t17
    183        b = t18
    184        t19 = a int+ t18
    185        a = t19
    186        param "%d %d %d\n"
    187        param a
    188        param b
    189        param c
    190        call printf, 4
    191        arr[0] = 10
    192        arr[4] = 20
    193        arr[8] = 30
    194        arr[12] = 40
    195        arr[16] = 50
    196        i = 1
    197        t20 = i
    198        t21 = i int+ 1
    199        i = t21
    200        t22 = t20 int* 4                    (w = 4)
    201        t23 = arr[t22]
    202        t24 = t23 int+ 5
    203        arr[t22] = t24
    204        t25 = i int+ 1
    205        i = t25
    206        t26 = t25 int* 4                    (w = 4)
    207        t27 = arr[t26]
    208        t28 = t27 int* 2
    209        arr[t26] = t28
    210        t29 = arr[4]
    211        t30 = arr[8]
    212        t31 = arr[12]
    213        param "%d %d %d %d\n"
    214        param t29
    215        param t30
    216        param t31
    217        param i
    218        call printf, 5
    219        n = 0
    220        k = 0
    221  L18:  t32 = n
    222        t33 = n int+ 1
    223        n = t33
    224        if t32 int< 5 goto L19
    225        goto L21
    226  L19:  t34 = k int+ n
    227        k = t34
    228        if t34 int< 9 goto L20
    229        goto L21
    230  L20:  goto L18
    231  L21:  param "%d %d\n"
    232        param n
    233        param k
    234        call printf, 3
    235        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      5    4    5  
   t                  function      int (int)                  -           6    -   13  _Z1ti; defined
   main               function      int (void)                 -           7    -    0  defined

 scope: global > t()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       6    4    2  v.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r1                 variable      int                        local       8    4    1  r1.2
   r2                 variable      int                        local       9    4    1  r2.3
   r3                 variable      int                        local      10    4    1  r3.4
   r4                 variable      int                        local      13    4    1  r4.5
   r5                 variable      int                        local      14    4    1  r5.6
   a                  variable      int                        local      16    4    3  a.7
   b                  variable      int                        local      16    4    3  b.8
   c                  variable      int                        local      16    4    3  c.9
   arr                variable      int[5]                     local      20   20    5  arr.10
   i                  variable      int                        local      21    4    3  i.11
   n                  variable      int                        local      25    4    3  n.12
   k                  variable      int                        local      25    4    2  k.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
