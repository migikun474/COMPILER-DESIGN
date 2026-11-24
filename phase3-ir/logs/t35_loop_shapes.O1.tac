============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t35_loop_shapes.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 67 -> 47 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           67 -> 47   (29% fewer)

   calls inlined                           0
   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            0
   temporaries merged away                11
   dead instructions removed               0
   jumps removed or redirected             9
   unreachable instructions removed        2

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

 Code: 47 instruction(s)

    100        s = 0
    101        k = 0
    102        t1 = &n
    103        param "%d"
    104        param t1
    105        call scanf, 2
    106        i = 0
    107  L1:   if i int>= n goto L3
    108        if i int== 7 goto L3
    109        t2 = i int% 2
    110        if t2 int!= 0 goto L2
    111        s = s int+ i
    112  L2:   i = i int+ 1
    113        goto L1
    114  L3:   if k int>= n goto L9
    115        t6 = k int% 3
    116        goto L7
    117  L4:   s = s int+ 1
    118        goto L8
    119  L5:   s = s int+ 2
    120        goto L8
    121  L6:   s = s int- 1
    122        goto L8
    123  L7:   if t6 int== 0 goto L4
    124        if t6 int== 1 goto L5
    125        goto L6
    126  L8:   k = k int+ 1
    127        goto L3
    128  L9:   s = s int+ 10
    129        t12 = n int- 1
    130        n = t12
    131        if t12 int> 0 goto L9
    132        i = 0
    133  L10:  if i int>= 3 goto L13
    134        k = 0
    135  L11:  if k int>= 2 goto L12
    136        t13 = i int* k
    137        s = s int+ t13
    138        k = k int+ 1
    139        goto L11
    140  L12:  i = i int+ 1
    141        goto L10
    142  L13:  param "%d %d\n"
    143        param s
    144        param i
    145        call printf, 3
    146        return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

111 3

   exit code 0, 225 instructions executed
