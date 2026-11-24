============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 163 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 28 temporaries, frame 160 bytes

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
   t1               temp    int                             4      48
   t2               temp    int                             4      52
   t3               temp    int                             4      56
   t4               temp    int                             4      60
   t5               temp    int                             4      64
   t6               temp    int                             4      68
   t7               temp    int                             4      72
   t8               temp    int                             4      76
   t9               temp    int                             4      80
   t10              temp    int                             4      84
   t11              temp    int                             4      88
   t12              temp    int                             4      92
   t13              temp    int                             4      96
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
   t27              temp    int                             4     152
   t28              temp    int                             4     156

 Code: 163 instruction(s)

    100        a = 1
    101        b = 2
    102        c = 5
    103        d = 4
    104        e = 6
    105        f = 7
    106        if a int< b goto L4
    107        goto L1
    108  L1:   if c int< d goto L2
    109        goto L3
    110  L2:   if e int< f goto L4
    111        goto L3
    112  L3:   t1 = 0
    113        goto L5
    114  L4:   t1 = 1
    115  L5:   x = t1
    116        if a int> b goto L7
    117        goto L6
    118  L6:   if c int< d goto L7
    119        goto L8
    120  L7:   if e int< f goto L9
    121        goto L8
    122  L8:   t2 = 0
    123        goto L10
    124  L9:   t2 = 1
    125  L10:  y = t2
    126        if x int!= 0 goto L11
    127        goto L12
    128  L11:  t3 = 0
    129        goto L13
    130  L12:  t3 = 1
    131  L13:  if c int!= 0 goto L15
    132        goto L14
    133  L14:  t4 = 0
    134        goto L16
    135  L15:  t4 = 1
    136  L16:  param "%d %d %d %d\n"
    137        param x
    138        param y
    139        param t3
    140        param t4
    141        call printf, 5
    142        if a int== 1 goto L17
    143        t5 = 0
    144        goto L18
    145  L17:  t5 = 1
    146  L18:  if b int!= 2 goto L19
    147        t6 = 0
    148        goto L20
    149  L19:  t6 = 1
    150  L20:  t7 = t5 int+ t6
    151        if c int>= 5 goto L21
    152        t8 = 0
    153        goto L22
    154  L21:  t8 = 1
    155  L22:  t9 = t7 int+ t8
    156        if d int<= 3 goto L23
    157        t10 = 0
    158        goto L24
    159  L23:  t10 = 1
    160  L24:  t11 = t9 int+ t10
    161        if e int> f goto L25
    162        t12 = 0
    163        goto L26
    164  L25:  t12 = 1
    165  L26:  t13 = t11 int+ t12
    166        t = t13
    167        if a int< b goto L27
    168        t15 = 0
    169        goto L28
    170  L27:  t15 = 1
    171  L28:  if t15 int== 1 goto L29
    172        t14 = 0
    173        goto L30
    174  L29:  t14 = 1
    175  L30:  if c int> d goto L31
    176        t16 = 0
    177        goto L32
    178  L31:  t16 = 1
    179  L32:  t17 = t16 int* 10
    180        param "%d %d %d\n"
    181        param t
    182        param t14
    183        param t17
    184        call printf, 4
    185        if c int> d goto L33
    186        t18 = 0
    187        goto L34
    188  L33:  t18 = 1
    189  L34:  if t18 int!= 0 goto L35
    190        t19 = 0
    191        goto L36
    192  L35:  t19 = 1
    193  L36:  p = t19
    194        if p bool!= 0 goto L37
    195        goto L38
    196  L37:  t20 = 0
    197        goto L39
    198  L38:  t20 = 1
    199  L39:  if t20 int!= 0 goto L40
    200        t21 = 0
    201        goto L41
    202  L40:  t21 = 1
    203  L41:  q = t21
    204        t22 = booltoint p
    205        t23 = booltoint q
    206        if p bool!= 0 goto L42
    207        goto L43
    208  L42:  if q bool!= 0 goto L43
    209        goto L44
    210  L43:  t24 = 0
    211        goto L45
    212  L44:  t24 = 1
    213  L45:  if p bool!= 0 goto L48
    214        goto L46
    215  L46:  if q bool!= 0 goto L48
    216        goto L47
    217  L47:  t25 = 0
    218        goto L49
    219  L48:  t25 = 1
    220  L49:  param "%d %d %d %d\n"
    221        param t22
    222        param t23
    223        param t24
    224        param t25
    225        call printf, 5
    226        i = 0
    227        n = 0
    228  L50:  if i int< 10 goto L51
    229        goto L54
    230  L51:  if i int> 6 goto L54
    231        goto L52
    232  L52:  if n int> 20 goto L54
    233        goto L53
    234  L53:  t26 = i
    235        t27 = i int+ 1
    236        i = t27
    237        t28 = n int+ t26
    238        n = t28
    239        goto L50
    240  L54:  param "%d %d\n"
    241        param i
    242        param n
    243        call printf, 3
    244        if a int< b goto L55
    245        goto L56
    246  L55:  if c int== d goto L56
    247        goto L57
    248  L56:  param "wrong\n"
    249        call printf, 1
    250        goto L58
    251  L57:  param "right\n"
    252        call printf, 1
    253  L58:  goto L59
    254  L59:  if a int!= 0 goto L60
    255        goto L61
    256  L60:  param "t\n"
    257        call printf, 1
    258  L61:  goto L62
    259        param "never\n"
    260        call printf, 1
    261        goto L61
    262  L62:  return 0


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
