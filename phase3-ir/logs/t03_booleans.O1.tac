============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 163 -> 114 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          163 -> 114   (30% fewer)

   constants folded                        6
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           17
   temporaries merged away                 3
   dead instructions removed               4
   jumps removed or redirected            30
   unreachable instructions removed       13

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 21 temporaries, frame 160 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   e                local   int                             4      16
   f                local   int                             4      20
   x                local   int                             4      24
   y                local   int                             4      28
   t                local   int                             4      32
   p                local   bool                            1      36
   q                local   bool                            1      37
   i                local   int                             4      40
   n                local   int                             4      44
   t5               temp    int                             4      64
   t6               temp    int                             4      68
   t7               temp    int                             4      72
   t8               temp    int                             4      76
   t9               temp    int                             4      80
   t10              temp    int                             4      84
   t11              temp    int                             4      88
   t12              temp    int                             4      92
   t14              temp    int                             4     100
   t15              temp    int                             4     104
   t16              temp    int                             4     108
   t17              temp    int                             4     112
   t18              temp    int                             4     116
   t19              temp    bool                            1     120
   t20              temp    int                             4     124
   t21              temp    bool                            1     128
   t22              temp    int                             4     132
   t23              temp    int                             4     136
   t24              temp    int                             4     140
   t25              temp    int                             4     144
   t26              temp    int                             4     148
   (7 temporaries no longer used after optimization not shown)

 Code: 114 instruction(s)

    100        a = 1
    101        b = 2
    102        c = 5
    103        d = 4
    104        e = 6
    105        f = 7
    106        x = 1
    107        y = 0
    108        param "%d %d %d %d\n"
    109        param 1
    110        param 0
    111        param 0
    112        param 1
    113        call printf, 5
    114        goto L1
    115  L1:   t5 = 1
    116        if b int!= 2 goto L2
    117        t6 = 0
    118        goto L3
    119  L2:   t6 = 1
    120  L3:   t7 = t5 int+ t6
    121        if c int>= 5 goto L4
    122        t8 = 0
    123        goto L5
    124  L4:   t8 = 1
    125  L5:   t9 = t7 int+ t8
    126        if d int<= 3 goto L6
    127        t10 = 0
    128        goto L7
    129  L6:   t10 = 1
    130  L7:   t11 = t9 int+ t10
    131        if e int> f goto L8
    132        t12 = 0
    133        goto L9
    134  L8:   t12 = 1
    135  L9:   t = t11 int+ t12
    136        if a int< b goto L10
    137        t15 = 0
    138        goto L11
    139  L10:  t15 = 1
    140  L11:  if t15 int== 1 goto L12
    141        t14 = 0
    142        goto L13
    143  L12:  t14 = 1
    144  L13:  if c int> d goto L14
    145        t16 = 0
    146        goto L15
    147  L14:  t16 = 1
    148  L15:  t17 = t16 int* 10
    149        param "%d %d %d\n"
    150        param t
    151        param t14
    152        param t17
    153        call printf, 4
    154        if c int> d goto L16
    155        t18 = 0
    156        goto L17
    157  L16:  t18 = 1
    158  L17:  if t18 int!= 0 goto L18
    159        t19 = 0
    160        goto L19
    161  L18:  t19 = 1
    162  L19:  p = t19
    163        if t19 bool== 0 goto L20
    164        t20 = 0
    165        goto L21
    166  L20:  t20 = 1
    167  L21:  if t20 int!= 0 goto L22
    168        t21 = 0
    169        goto L23
    170  L22:  t21 = 1
    171  L23:  q = t21
    172        t22 = booltoint p
    173        t23 = booltoint t21
    174        if p bool== 0 goto L24
    175        if q bool== 0 goto L25
    176  L24:  t24 = 0
    177        goto L26
    178  L25:  t24 = 1
    179  L26:  if p bool!= 0 goto L27
    180        if q bool!= 0 goto L27
    181        t25 = 0
    182        goto L28
    183  L27:  t25 = 1
    184  L28:  param "%d %d %d %d\n"
    185        param t22
    186        param t23
    187        param t24
    188        param t25
    189        call printf, 5
    190        i = 0
    191        n = 0
    192  L29:  if i int>= 10 goto L30
    193        if i int> 6 goto L30
    194        if n int> 20 goto L30
    195        t26 = i
    196        i = i int+ 1
    197        n = n int+ t26
    198        goto L29
    199  L30:  param "%d %d\n"
    200        param i
    201        param n
    202        call printf, 3
    203        if a int>= b goto L31
    204        if c int!= d goto L32
    205  L31:  param "wrong\n"
    206        call printf, 1
    207        goto L33
    208  L32:  param "right\n"
    209        call printf, 1
    210  L33:  if a int== 0 goto L34
    211        param "t\n"
    212        call printf, 1
    213  L34:  return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           4    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       5    4    6  a.1
   b                  variable      int                        local       5    4    5  b.2
   c                  variable      int                        local       5    4    7  c.3
   d                  variable      int                        local       5    4    6  d.4
   e                  variable      int                        local       5    4    3  e.5
   f                  variable      int                        local       5    4    3  f.6
   x                  variable      int                        local       6    4    2  x.7
   y                  variable      int                        local       7    4    1  y.8
   t                  variable      int                        local       9    4    1  t.9
   p                  variable      bool                       local      11    1    4  p.10
   q                  variable      bool                       local      11    1    3  q.11
   i                  variable      int                        local      13    4    4  i.12
   n                  variable      int                        local      13    4    3  n.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
