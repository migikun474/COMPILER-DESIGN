============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t35_loop_shapes.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 67 -> 70 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           67 -> 70   (-4% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            0
   temporaries merged away                11
   dead instructions removed               0
   jumps removed or redirected             9
   unreachable instructions removed        2
   propagated across blocks                0
   dead assignments removed                0
   calls inlined                           0
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          3
   unreachable functions removed           0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 80 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                local   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   k                local   int                             4      12
   t1               temp    int *                           4      16
   t2               temp    int                             4      20
   t6               temp    int                             4      36
   t12              temp    int                             4      60
   t13              temp    int                             4      64
   (11 temporaries no longer used after optimization not shown)

 Code: 70 instruction(s)

    100        s = 0
    101        k = 0
    102        t1 = &n
    103        param "%d"
    104        param t1
    105        call scanf, 2
    106        i = 0
    107  L1:   if i int>= n goto L4
    108        if i int== 7 goto L4
    109        t2 = i int% 2
    110        if t2 int!= 0 goto L2
    111        s = s int+ i
    112  L2:   i = i int+ 1
    113        if i int>= n goto L4
    114        if i int== 7 goto L4
    115        t2 = i int% 2
    116        if t2 int!= 0 goto L3
    117        s = s int+ i
    118  L3:   i = i int+ 1
    119        goto L1
    120  L4:   if k int>= n goto L15
    121        t6 = k int% 3
    122        goto L8
    123  L5:   s = s int+ 1
    124        goto L9
    125  L6:   s = s int+ 2
    126        goto L9
    127  L7:   s = s int- 1
    128        goto L9
    129  L8:   if t6 int== 0 goto L5
    130        if t6 int== 1 goto L6
    131        goto L7
    132  L9:   k = k int+ 1
    133        if k int>= n goto L15
    134        t6 = k int% 3
    135        goto L13
    136  L10:  s = s int+ 1
    137        goto L14
    138  L11:  s = s int+ 2
    139        goto L14
    140  L12:  s = s int- 1
    141        goto L14
    142  L13:  if t6 int== 0 goto L10
    143        if t6 int== 1 goto L11
    144        goto L12
    145  L14:  k = k int+ 1
    146        goto L4
    147  L15:  s = s int+ 10
    148        t12 = n int- 1
    149        n = t12
    150        if t12 int> 0 goto L15
    151        i = 0
    152  L16:  if i int>= 3 goto L19
    153        k = 0
    154  L17:  if k int>= 2 goto L18
    155        t13 = i int* k
    156        s = s int+ t13
    157        k = k int+ 1
    158        if k int>= 2 goto L18
    159        t13 = i int* k
    160        s = s int+ t13
    161        k = k int+ 1
    162        goto L17
    163  L18:  i = i int+ 1
    164        goto L16
    165  L19:  param "%d %d\n"
    166        param s
    167        param i
    168        call printf, 3
    169        return 0


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
