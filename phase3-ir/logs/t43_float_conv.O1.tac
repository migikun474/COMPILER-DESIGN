============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t43_float_conv.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 76 -> 43 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           76 -> 43   (43% fewer)

   constants folded                       24
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           39
   temporaries merged away                 0
   dead instructions removed              24
   jumps removed or redirected             4
   unreachable instructions removed        6

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 0 temporaries, frame 244 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   double                          8       0
   e                local   double                          8       8
   f                local   float                           4      16
   i                local   int                             4      20
   h                local   double                          8      24
   q                local   double                          8      32
   third            local   float                           4      40
   u                local   unsigned int                    4      44
   ud               local   double                          8      48
   big              local   double                          8      56
   back             local   int                             4      64
   (24 temporaries no longer used after optimization not shown)

 Code: 43 instruction(s)

    100     d = -3.99
    101     e = 3.99
    102     f = 2.5
    103     param "%d %d %d %d\n"
    104     param -3
    105     param 3
    106     param 0
    107     param 2
    108     call printf, 5
    109     i = 7
    110     h = 3.0
    111     q = 3.5
    112     param "%.1f %.1f %.3f\n"
    113     param 3.0
    114     param 3.5
    115     param 0.3333333333333333
    116     call printf, 4
    117     third = 0.33333334
    118     param "%.6f %.2f %.0f %.0f\n"
    119     param 0.3333333432674408
    120     param 2.675
    121     param 0.5
    122     param 1.5
    123     call printf, 5
    124     param "%d %d %d\n"
    125     param 1
    126     param 1
    127     param 1
    128     call printf, 4
    129     u = 4000000000
    130     ud = 4e+09
    131     param "%.0f %u\n"
    132     param 4e+09
    133     param 2000000000
    134     call printf, 3
    135     big = 1e+09
    136     back = 666666666
    137     param "%d %.2e %g\n"
    138     param 666666666
    139     param 12345.678
    140     param 0.0001
    141     call printf, 4
    142     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           5    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      double                     local       6    8    1  d.1
   e                  variable      double                     local       6    8    1  e.2
   f                  variable      float                      local       7    4    1  f.3
   i                  variable      int                        local       9    4    4  i.4
   h                  variable      double                     local      10    8    1  h.5
   q                  variable      double                     local      10    8    1  q.6
   third              variable      float                      local      12    4    1  third.7
   u                  variable      unsigned int               local      15    4    1  u.8
   ud                 variable      double                     local      16    8    2  ud.9
   big                variable      double                     local      18    8    1  big.10
   back               variable      int                        local      19    4    1  back.11

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
