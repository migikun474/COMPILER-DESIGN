============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t31_short_circuit.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 136 -> 97 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          136 -> 97   (28% fewer)

   constants folded                        7
   algebraic simplifications               1
   common subexpressions                   1
   copies / constants forwarded           27
   temporaries merged away                 4
   dead instructions removed               9
   jumps removed or redirected            12
   unreachable instructions removed        1
   propagated across blocks                2
   dead assignments removed               14

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

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 3 instruction(s)

    100     t1 = calls int* 10
    101     calls = t1 int+ v
    102     return v

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 22 temporaries, frame 200 bytes

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
   t16              temp    int                             4     124
   t23              temp    int                             4     152
   t24              temp    int                             4     156
   t27              temp    int                             4     168
   t28              temp    int                             4     172
   t29              temp    int                             4     176
   t30              temp    int                             4     180
   t32              temp    int                             4     188
   t34              temp    int                             4     196
   (12 temporaries no longer used after optimization not shown)

 Code: 94 instruction(s)

    103        param 0
    104        t2 = call t(int), 1
    105        if t2 int== 0 goto L1
    106        param 1
    107        t3 = call t(int), 1
    108        if t3 int!= 0 goto L2
    109  L1:   t1 = 0
    110        goto L3
    111  L2:   t1 = 1
    112  L3:   param 2
    113        t5 = call t(int), 1
    114        if t5 int!= 0 goto L4
    115        param 3
    116        t6 = call t(int), 1
    117        if t6 int!= 0 goto L4
    118        t4 = 0
    119        goto L5
    120  L4:   t4 = 1
    121  L5:   param 0
    122        t8 = call t(int), 1
    123        if t8 int!= 0 goto L6
    124        param 4
    125        t9 = call t(int), 1
    126        if t9 int== 0 goto L7
    127  L6:   param 5
    128        t10 = call t(int), 1
    129        if t10 int!= 0 goto L8
    130        param 6
    131        t11 = call t(int), 1
    132        if t11 int!= 0 goto L8
    133  L7:   t7 = 0
    134        goto L9
    135  L8:   t7 = 1
    136  L9:   param "%d %d %d %d\n"
    137        param t1
    138        param t4
    139        param t7
    140        param calls
    141        call printf, 5
    142        calls = 0
    143        param 1
    144        t13 = call t(int), 1
    145        if t13 int== 0 goto L10
    146        param 7
    147        t12 = call t(int), 1
    148        goto L11
    149  L10:  param 8
    150        t12 = call t(int), 1
    151  L11:  param 0
    152        call t(int), 1
    153        param 9
    154        t16 = call t(int), 1
    155        param "%d %d %d\n"
    156        param t12
    157        param t16
    158        param calls
    159        call printf, 4
    160        param "%d %d %d\n"
    161        param 0
    162        param -4
    163        param 8
    164        call printf, 4
    165        arr[0] = 10
    166        arr[4] = 20
    167        arr[8] = 30
    168        arr[12] = 40
    169        arr[16] = 50
    170        t23 = arr[4]
    171        t24 = t23 int+ 5
    172        arr[4] = t24
    173        t27 = arr[12]
    174        t28 = t27 int<< 1
    175        arr[12] = t28
    176        t29 = arr[4]
    177        t30 = arr[8]
    178        param "%d %d %d %d\n"
    179        param t29
    180        param t30
    181        param t28
    182        param 3
    183        call printf, 5
    184        n = 0
    185        k = 0
    186  L12:  t32 = n
    187        n = n int+ 1
    188        if t32 int>= 5 goto L13
    189        t34 = k int+ n
    190        k = t34
    191        if t34 int< 9 goto L12
    192  L13:  param "%d %d\n"
    193        param n
    194        param k
    195        call printf, 3
    196        return 0


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
