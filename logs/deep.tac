============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : /tmp/claude-1000/-home-amirishetty-parsing-stage/d23148d6-4d07-435e-b985-82ec05b0bcc4/scratchpad/deep.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 18 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION f(int)        (link name _Z1fi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 8 instruction(s)

    100       if n int== 0 goto L1
    101       goto L2
    102  L1:  return 0
    103  L2:  t1 = n int- 1
    104       param t1
    105       t2 = call f(int), 1
    106       t3 = 1 int+ t2
    107       return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                local   int                             4       0
   t1               temp    int *                           4       4
   t2               temp    int                             4       8

 Code: 10 instruction(s)

    108     t1 = &n
    109     param "%d"
    110     param t1
    111     call scanf, 2
    112     param n
    113     t2 = call f(int), 1
    114     param "%d\n"
    115     param t2
    116     call printf, 2
    117     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   f                  function      int (int)                  -           1    -    2  _Z1fi; defined
   main               function      int (void)                 -           2    -    0  defined

 scope: global > f()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       1    4    2  n.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        local       2    4    2  n.2

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
