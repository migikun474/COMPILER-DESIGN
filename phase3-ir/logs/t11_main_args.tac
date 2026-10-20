============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t11_main_args.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 31 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main(int, char **)        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 10 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   argc             param   int                             4       0
   argv             param   char **                         4       4
   letters          local   int                             4       8
   i                local   int                             4      12
   s                local   char *                          4      16
   t1               temp    int                             4      20
   t2               temp    char **                         4      24
   t3               temp    char *                          4      28
   t4               temp    char                            1      32
   t5               temp    int                             4      36
   t6               temp    char *                          4      40
   t7               temp    int                             4      44
   t8               temp    char **                         4      48
   t9               temp    char *                          4      52
   t10              temp    int                             4      56

 Code: 31 instruction(s)

    100       letters = 0
    101       i = 1
    102  L1:  if i int< argc goto L2
    103       goto L6
    104  L2:  t1 = i int* 4
    105       t2 = argv ptr+ t1
    106       t3 = *t2
    107       s = t3
    108  L3:  t4 = *s
    109       if t4 char!= 0 goto L4
    110       goto L5
    111  L4:  t5 = letters int+ 1
    112       letters = t5
    113       t6 = s ptr+ 1
    114       s = t6
    115       goto L3
    116  L5:  t7 = i int* 4
    117       t8 = argv ptr+ t7
    118       t9 = *t8
    119       param "%d: %s\n"
    120       param i
    121       param t9
    122       call printf, 3
    123       t10 = i int+ 1
    124       i = t10
    125       goto L1
    126  L6:  param "%d %d\n"
    127       param argc
    128       param letters
    129       call printf, 3
    130       return argc


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (int, char **)         -           4    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   argc               parameter     int                        param       4    4    3  argc.1
   argv               parameter     char **                    param       4    4    2  argv.2
   letters            variable      int                        local       5    4    2  letters.3

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       6    4    5  i.4

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  variable      char *                     local       7    4    2  s.5

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
