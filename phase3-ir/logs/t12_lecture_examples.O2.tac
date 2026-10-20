============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t12_lecture_examples.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 49 -> 7 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           49 -> 7   (85% fewer)

   constants folded                       10
   algebraic simplifications               3
   common subexpressions                   1
   copies / constants forwarded           17
   temporaries merged away                 2
   dead instructions removed              12
   jumps removed or redirected            11
   unreachable instructions removed        2
   propagated across blocks               11
   dead assignments removed               14

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 1 temporary, frame 204 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   e                local   int                             4      16
   f                local   int                             4      20
   i                local   int                             4      24
   x                local   int                             4      28
   y                local   int                             4      32
   arr              local   int[10]                        40      36
   m                local   int[3][4]                      48      76
   r                local   double                          8     128
   t12              temp    int                             4     188
   (14 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    100       a = -12
    101  L1:  if a int>= 2 goto L2
    102       a = a int+ 1
    103       goto L1
    104  L2:  t12 = arr[4]
    105       m[24] = t12
    106       return 1


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           3    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       4    4    7  a.1
   b                  variable      int                        local       4    4    6  b.2
   c                  variable      int                        local       4    4    3  c.3
   d                  variable      int                        local       4    4    1  d.4
   e                  variable      int                        local       4    4    1  e.5
   f                  variable      int                        local       4    4    1  f.6
   i                  variable      int                        local       4    4    3  i.7
   x                  variable      int                        local       4    4    4  x.8
   y                  variable      int                        local       4    4    3  y.9
   arr                variable      int[10]                    local       5   40    1  arr.10
   m                  variable      int[3][4]                  local       6   48    1  m.11
   r                  variable      double                     local       7    8    2  r.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
