============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t39_printf_pointers.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 40 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 8 parameter(s)/local(s), 4 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   none             local   int *                           4       0
   small            local   int *                           4       4
   mid              local   char *                          4       8
   big              local   unsigned int                    4      12
   top              local   double *                        4      16
   one              local   void *                          4      20
   p                local   int *                           4      24
   c                local   char *                          4      28
   t1               temp    int *                           4      32
   t2               temp    char *                          4      36
   t3               temp    int                             4      40
   t4               temp    int                             4      44

 Code: 40 instruction(s)

    100     none = 0
    101     small = 16
    102     mid = 305441741
    103     big = 3735928559
    104     top = big
    105     one = 1
    106     param "[%p] [%p] [%p] [%p] [%p]\n"
    107     param none
    108     param small
    109     param mid
    110     param top
    111     param one
    112     call printf, 6
    113     param "[%12p] [%-12p] [%3p]\n"
    114     param mid
    115     param mid
    116     param mid
    117     call printf, 4
    118     param "[%10p] [%-10p] [%2p]\n"
    119     param none
    120     param none
    121     param none
    122     call printf, 4
    123     param "%p and %d and %p\n"
    124     param small
    125     param 42
    126     param 255
    127     call printf, 4
    128     t1 = small ptr+ 8
    129     p = t1
    130     t2 = mid ptr+ 3
    131     c = t2
    132     t3 = p ptr- small
    133     t4 = t3 int/ 4
    134     param "%p %p %d\n"
    135     param p
    136     param c
    137     param t4
    138     call printf, 4
    139     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           6    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   none               variable      int *                      local       7    4    4  none.1
   small              variable      int *                      local       8    4    4  small.2
   mid                variable      char *                     local       9    4    5  mid.3
   big                variable      unsigned int               local      10    4    1  big.4
   top                variable      double *                   local      11    4    1  top.5
   one                variable      void *                     local      12    4    1  one.6
   p                  variable      int *                      local      17    4    2  p.7
   c                  variable      char *                     local      18    4    1  c.8

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
