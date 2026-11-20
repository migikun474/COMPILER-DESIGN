============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : /tmp/claude-1000/-home-amirishetty-parsing-stage/d23148d6-4d07-435e-b985-82ec05b0bcc4/scratchpad/unr.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 30 -> 31 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           30 -> 31   (-3% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            0
   temporaries merged away                 5
   dead instructions removed               0
   jumps removed or redirected             3
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                0
   calls inlined                           0
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          2
   unreachable functions removed           0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 1 temporary, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                local   int                             4       0
   s                local   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   t1               temp    int *                           4      16
   (5 temporaries no longer used after optimization not shown)

 Code: 31 instruction(s)

    100       s = 0
    101       t1 = &n
    102       param "%d"
    103       param t1
    104       call scanf, 2
    105       i = 0
    106  L1:  if i int>= n goto L2
    107       s = s int+ i
    108       i = i int+ 1
    109       if i int>= n goto L2
    110       s = s int+ i
    111       i = i int+ 1
    112       goto L1
    113  L2:  j = 0
    114  L3:  if j int>= n goto L7
    115       if j int!= 3 goto L4
    116       j = j int+ 1
    117       goto L3
    118  L4:  s = s int+ 2
    119       j = j int+ 1
    120  L5:  if j int>= n goto L7
    121       if j int!= 3 goto L6
    122       j = j int+ 1
    123       goto L5
    124  L6:  s = s int+ 2
    125       j = j int+ 1
    126       goto L3
    127  L7:  param "%d\n"
    128       param s
    129       call printf, 2
    130       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           1    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        local       2    4    3  n.1
   s                  variable      int                        local       2    4    5  s.2
   i                  variable      int                        local       2    4    4  i.3
   j                  variable      int                        local       5    4    4  j.4

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
