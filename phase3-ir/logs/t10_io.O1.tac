============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t10_io.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 68 -> 59 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           68 -> 59   (13% fewer)

   constants folded                        6
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded            9
   temporaries merged away                 2
   dead instructions removed               6
   jumps removed or redirected             1
   unreachable instructions removed        0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 9 temporaries, frame 136 bytes

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
   t8               temp    char (*)[16]                    4      80
   t9               temp    int                             4      84
   t10              temp    double                          8      88
   t11              temp    double                          8      96
   (8 temporaries no longer used after optimization not shown)

 Code: 59 instruction(s)

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
    112  L1:  if i int>= n goto L2
    113       t5 = &v
    114       param "%d"
    115       param t5
    116       call scanf, 2
    117       total = total int+ v
    118       i = i int+ 1
    119       goto L1
    120  L2:  t8 = &name
    121       t9 = chartoint grade
    122       t10 = inttodouble total
    123       t11 = t10 double* scale
    124       param "%s %c %d %.2f\n"
    125       param t8
    126       param t9
    127       param total
    128       param t11
    129       call printf, 5
    130       param "[%5d] [%-5d] [%05d] [%x] [%o] [%c] [%%]\n"
    131       param 42
    132       param 42
    133       param 42
    134       param 255
    135       param 8
    136       param 122
    137       call printf, 7
    138       param "[%8.3f] [%-8.1f] [%10s] [%-6s] [%.3s]\n"
    139       param 3.14159
    140       param 2.5
    141       param "right"
    142       param "left"
    143       param "truncated"
    144       call printf, 6
    145       param "%u %lld %d\n"
    146       param 3000000000
    147       param 9000000000
    148       param -5
    149       call printf, 4
    150       f = 1.25
    151       c = 113
    152       s = -3
    153       param "%.2f %c %d\n"
    154       param 1.25
    155       param 113
    156       param -3
    157       call printf, 4
    158       return total


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
