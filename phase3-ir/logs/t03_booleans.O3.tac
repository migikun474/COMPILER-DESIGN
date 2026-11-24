============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 163 -> 41 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          163 -> 41   (74% fewer)

   constants folded                       30
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           37
   temporaries merged away                 3
   dead instructions removed              18
   jumps removed or redirected            46
   unreachable instructions removed       40
   propagated across blocks               26
   dead assignments removed               17
   calls inlined                           0
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          1
   unreachable functions removed           0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 1 temporary, frame 160 bytes

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
   t26              temp    int                             4     148
   (27 temporaries no longer used after optimization not shown)

 Code: 41 instruction(s)

    100       param "%d %d %d %d\n"
    101       param 1
    102       param 0
    103       param 0
    104       param 1
    105       call printf, 5
    106       param "%d %d %d\n"
    107       param 2
    108       param 1
    109       param 10
    110       call printf, 4
    111       param "%d %d %d %d\n"
    112       param 1
    113       param 0
    114       param 1
    115       param 1
    116       call printf, 5
    117       i = 0
    118       n = 0
    119  L1:  if i int>= 10 goto L2
    120       if i int> 6 goto L2
    121       if n int> 20 goto L2
    122       t26 = i
    123       i = i int+ 1
    124       n = n int+ t26
    125       if i int>= 10 goto L2
    126       if i int> 6 goto L2
    127       if n int> 20 goto L2
    128       t26 = i
    129       i = i int+ 1
    130       n = n int+ t26
    131       goto L1
    132  L2:  param "%d %d\n"
    133       param i
    134       param n
    135       call printf, 3
    136       param "right\n"
    137       call printf, 1
    138       param "t\n"
    139       call printf, 1
    140       return 0


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
