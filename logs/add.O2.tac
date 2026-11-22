============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : docs/examples/add.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 11 -> 8 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           11 -> 8   (27% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            4
   temporaries merged away                 0
   dead instructions removed               0
   jumps removed or redirected             0
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                3

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   global           int                             4  0

 As three address code (initial values, in place before main runs):

    global = 0                (zero-initialized)

============================================================================
 FUNCTION add(int, int)        (link name _Z3addii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   result           local   int                             4       8
   t1               temp    int                             4      12

 Code: 2 instruction(s)

    100     t1 = a int+ b
    101     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x.4              local   int                             4       0
   x.5              local   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 6 instruction(s)

    102     param 3
    103     param 4
    104     t1 = call add(int, int), 2
    105     global = t1
    106     t2 = t1 int+ 2
    107     return t2


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   global             variable      int                        global      1    4    2  
   add                function      int (int, int)             -           3    -    1  _Z3addii; defined
   main               function      int (void)                 -           9    -    0  defined

 scope: global > add()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param       3    4    1  a.1
   b                  parameter     int                        param       3    4    1  b.2
   result             variable      int                        local       4    4    2  result.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      10    4    1  x.4

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      12    4    1  x.5

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
