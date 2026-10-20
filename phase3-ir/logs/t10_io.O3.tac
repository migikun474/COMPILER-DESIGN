============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t10_io.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 68 -> 55 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           68 -> 55   (19% fewer)

   constants folded                        6
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           10
   temporaries merged away                 2
   dead instructions removed               7
   jumps removed or redirected             1
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                3
   calls inlined                           0
   tail calls turned into jumps            0
   common subexpressions across blocks      1
   instructions moved out of loops         1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 8 temporaries, frame 136 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                local   int                             4       0
   total            local   int                             4       4
   scale            local   double                          8       8
   name             local   char[16]                       16      16
   grade            local   char                            1      32
   i                local   int                             4      36
   v                local   int                             4      40
   f                local   float                           4      44
   c                local   char                            1      48
   s                local   short                           2      50
   t1               temp    int *                           4      52
   t2               temp    double *                        4      56
   t3               temp    char (*)[16]                    4      60
   t4               temp    char *                          4      64
   t5               temp    int *                           4      68
   t9               temp    int                             4      84
   t10              temp    double                          8      88
   t11              temp    double                          8      96
   (9 temporaries no longer used after optimization not shown)

 Code: 55 instruction(s)

    100       total = 0
    101       t1 = &n
    102       t2 = &scale
    103       t3 = &name
    104       t4 = &grade
    105       param "%d %lf %15s %c"
    106       param t1
    107       param t2
    108       param t3
    109       param t4
    110       call scanf, 5
    111       i = 0
    112       t5 = &v
    113  L1:  if i int>= n goto L2
    114       param "%d"
    115       param t5
    116       call scanf, 2
    117       total = total int+ v
    118       i = i int+ 1
    119       goto L1
    120  L2:  t9 = chartoint grade
    121       t10 = inttodouble total
    122       t11 = t10 double* scale
    123       param "%s %c %d %.2f\n"
    124       param t3
    125       param t9
    126       param total
    127       param t11
    128       call printf, 5
    129       param "[%5d] [%-5d] [%05d] [%x] [%o] [%c] [%%]\n"
    130       param 42
    131       param 42
    132       param 42
    133       param 255
    134       param 8
    135       param 122
    136       call printf, 7
    137       param "[%8.3f] [%-8.1f] [%10s] [%-6s] [%.3s]\n"
    138       param 3.14159
    139       param 2.5
    140       param "right"
    141       param "left"
    142       param "truncated"
    143       call printf, 6
    144       param "%u %lld %d\n"
    145       param 3000000000
    146       param 9000000000
    147       param -5
    148       call printf, 4
    149       param "%.2f %c %d\n"
    150       param 1.25
    151       param 113
    152       param -3
    153       call printf, 4
    154       return total


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
   n                  variable      int                        local       5    4    2  n.1
   total              variable      int                        local       5    4    4  total.2
   scale              variable      double                     local       6    8    2  scale.3
   name               variable      char[16]                   local       7   16    2  name.4
   grade              variable      char                       local       8    1    2  grade.5
   f                  variable      float                      local      19    4    1  f.8
   c                  variable      char                       local      20    1    1  c.9
   s                  variable      short                      local      21    2    1  s.10

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      10    4    2  i.6

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  variable      int                        local      11    4    2  v.7

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
