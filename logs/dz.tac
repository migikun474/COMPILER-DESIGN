============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : /tmp/claude-1000/-home-amirishetty-parsing-stage/d23148d6-4d07-435e-b985-82ec05b0bcc4/scratchpad/dz.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 9 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   t1               temp    int                             4       8

 Code: 9 instruction(s)

    100     a = 5
    101     b = 0
    102     param "x\n"
    103     call printf, 1
    104     t1 = a int/ b
    105     param "%d\n"
    106     param t1
    107     call printf, 2
    108     return 3


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
   a                  variable      int                        local       1    4    1  a.1
   b                  variable      int                        local       1    4    1  b.2

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
