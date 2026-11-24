============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t41_loop_edges.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 119 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION count(int)        (link name _Z5counti)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   c                local   int                             4       4
   i                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20

 Code: 11 instruction(s)

    100       c = 0
    101       i = 0
    102  L1:  if i int< n goto L2
    103       goto L3
    104  L2:  t1 = c int* 2
    105       t2 = t1 int+ 1
    106       c = t2
    107       t3 = i int+ 1
    108       i = t3
    109       goto L1
    110  L3:  return c

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 23 temporaries, frame 128 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   int                             4       0
   w                local   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   found            local   int                             4      16
   skipped          local   int                             4      20
   k                local   int                             4      24
   total            local   int                             4      28
   s                local   int                             4      32
   t1               temp    int                             4      36
   t2               temp    int                             4      40
   t3               temp    int                             4      44
   t4               temp    int                             4      48
   t5               temp    int                             4      52
   t6               temp    int                             4      56
   t7               temp    int                             4      60
   t8               temp    int                             4      64
   t9               temp    int                             4      68
   t10              temp    int                             4      72
   t11              temp    int                             4      76
   t12              temp    int                             4      80
   t13              temp    int                             4      84
   t14              temp    int                             4      88
   t15              temp    int                             4      92
   t16              temp    int                             4      96
   t17              temp    int                             4     100
   t18              temp    int                             4     104
   t19              temp    int                             4     108
   t20              temp    int                             4     112
   t21              temp    int                             4     116
   t22              temp    int                             4     120
   t23              temp    int                             4     124

 Code: 108 instruction(s)

    111        param 0
    112        t1 = call count(int), 1
    113        param 1
    114        t2 = call count(int), 1
    115        param 2
    116        t3 = call count(int), 1
    117        param 3
    118        t4 = call count(int), 1
    119        param 7
    120        t5 = call count(int), 1
    121        param "%d %d %d %d %d\n"
    122        param t1
    123        param t2
    124        param t3
    125        param t4
    126        param t5
    127        call printf, 6
    128        d = 0
    129  L4:   t6 = d int+ 1
    130        d = t6
    131        if d int< 0 goto L4
    132        goto L5
    133  L5:   w = 10
    134  L6:   if w int< 10 goto L7
    135        goto L8
    136  L7:   t7 = w int+ 1
    137        w = t7
    138        goto L6
    139  L8:   param "%d %d\n"
    140        param d
    141        param w
    142        call printf, 3
    143        t8 = int- 1
    144        found = t8
    145        skipped = 0
    146        i = 0
    147  L9:   if i int< 5 goto L10
    148        goto L19
    149  L10:  if found int< 0 goto L11
    150        goto L19
    151  L11:  j = 0
    152  L12:  if j int< 5 goto L13
    153        goto L18
    154  L13:  if j int== 1 goto L14
    155        goto L15
    156  L14:  t9 = skipped int+ 1
    157        skipped = t9
    158        goto L17
    159  L15:  t10 = i int* j
    160        if t10 int== 6 goto L16
    161        goto L17
    162  L16:  t11 = i int* 10
    163        t12 = t11 int+ j
    164        found = t12
    165        goto L18
    166  L17:  t13 = j int+ 1
    167        j = t13
    168        goto L12
    169  L18:  t14 = i int+ 1
    170        i = t14
    171        goto L9
    172  L19:  param "%d %d %d\n"
    173        param found
    174        param i
    175        param skipped
    176        call printf, 4
    177        k = 0
    178        total = 0
    179  L20:  t15 = total int+ k
    180        total = t15
    181        t16 = k int+ 1
    182        k = t16
    183        if t16 int< 5 goto L21
    184        goto L22
    185  L21:  goto L20
    186  L22:  param "%d\n"
    187        param total
    188        call printf, 2
    189        s = 0
    190        i = 0
    191  L23:  if i int< 8 goto L24
    192        goto L32
    193  L24:  t17 = i int% 4
    194        t18 = t17
    195        goto L29
    196  L25:  goto L31
    197  L26:  t19 = s int+ 1
    198        s = t19
    199        goto L30
    200  L27:  t20 = s int+ 10
    201        s = t20
    202  L28:  t21 = s int+ 100
    203        s = t21
    204        goto L30
    205        goto L30
    206  L29:  if t18 int== 0 goto L25
    207        if t18 int== 1 goto L26
    208        if t18 int== 2 goto L27
    209        if t18 int== 3 goto L28
    210  L30:  t22 = s int+ 1000
    211        s = t22
    212  L31:  t23 = i int+ 1
    213        i = t23
    214        goto L23
    215  L32:  param "%d\n"
    216        param s
    217        call printf, 2
    218        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   count              function      int (int)                  -           5    -    5  _Z5counti; defined
   main               function      int (void)                 -           6    -    0  defined

 scope: global > count()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       5    4    1  n.1
   c                  variable      int                        local       5    4    3  c.2
   i                  variable      int                        local       5    4    3  i.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   again              label         -                          -          21    -    1  main.again
   d                  variable      int                        local       8    4    3  d.4
   w                  variable      int                        local      10    4    3  w.5
   i                  variable      int                        local      13    4   10  i.6
   j                  variable      int                        local      13    4    6  j.7
   found              variable      int                        local      13    4    3  found.8
   skipped            variable      int                        local      13    4    2  skipped.9
   k                  variable      int                        local      20    4    2  k.10
   total              variable      int                        local      20    4    2  total.11
   s                  variable      int                        local      25    4    5  s.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
