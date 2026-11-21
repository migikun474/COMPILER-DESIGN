============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t35_loop_shapes.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 67 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 16 temporaries, frame 80 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                local   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   k                local   int                             4      12
   t1               temp    int *                           4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52
   t11              temp    int                             4      56
   t12              temp    int                             4      60
   t13              temp    int                             4      64
   t14              temp    int                             4      68
   t15              temp    int                             4      72
   t16              temp    int                             4      76

 Code: 67 instruction(s)

    100        s = 0
    101        k = 0
    102        t1 = &n
    103        param "%d"
    104        param t1
    105        call scanf, 2
    106        i = 0
    107  L1:   if i int< n goto L2
    108        goto L8
    109  L2:   if i int== 7 goto L3
    110        goto L4
    111  L3:   goto L8
    112  L4:   t2 = i int% 2
    113        if t2 int!= 0 goto L5
    114        goto L6
    115  L5:   goto L7
    116  L6:   t3 = s int+ i
    117        s = t3
    118  L7:   t4 = i int+ 1
    119        i = t4
    120        goto L1
    121  L8:   if k int< n goto L9
    122        goto L15
    123  L9:   t5 = k int% 3
    124        t6 = t5
    125        goto L13
    126  L10:  t7 = s int+ 1
    127        s = t7
    128        goto L14
    129  L11:  t8 = s int+ 2
    130        s = t8
    131        goto L14
    132  L12:  t9 = s int- 1
    133        s = t9
    134        goto L14
    135  L13:  if t6 int== 0 goto L10
    136        if t6 int== 1 goto L11
    137        goto L12
    138  L14:  t10 = k int+ 1
    139        k = t10
    140        goto L8
    141  L15:  t11 = s int+ 10
    142        s = t11
    143        t12 = n int- 1
    144        n = t12
    145        if t12 int> 0 goto L15
    146        goto L16
    147  L16:  i = 0
    148  L17:  if i int< 3 goto L18
    149        goto L22
    150  L18:  k = 0
    151  L19:  if k int< 2 goto L20
    152        goto L21
    153  L20:  t13 = i int* k
    154        t14 = s int+ t13
    155        s = t14
    156        t15 = k int+ 1
    157        k = t15
    158        goto L19
    159  L21:  t16 = i int+ 1
    160        i = t16
    161        goto L17
    162  L22:  param "%d %d\n"
    163        param s
    164        param i
    165        call printf, 3
    166        return 0


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
   n                  variable      int                        local       5    4    4  n.1
   s                  variable      int                        local       5    4    7  s.2
   i                  variable      int                        local       5    4   11  i.3
   k                  variable      int                        local       5    4    7  k.4

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
