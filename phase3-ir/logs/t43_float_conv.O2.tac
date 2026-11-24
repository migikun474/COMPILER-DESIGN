============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t43_float_conv.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 76 -> 32 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           76 -> 32   (57% fewer)

   constants folded                       24
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           39
   temporaries merged away                 0
   dead instructions removed              24
   jumps removed or redirected             4
   unreachable instructions removed        6
   propagated across blocks                0
   dead assignments removed               11

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

 Code: 32 instruction(s)

    100     param "%d %d %d %d\n"
    101     param -3
    102     param 3
    103     param 0
    104     param 2
    105     call printf, 5
    106     param "%.1f %.1f %.3f\n"
    107     param 3.0
    108     param 3.5
    109     param 0.3333333333333333
    110     call printf, 4
    111     param "%.6f %.2f %.0f %.0f\n"
    112     param 0.3333333432674408
    113     param 2.675
    114     param 0.5
    115     param 1.5
    116     call printf, 5
    117     param "%d %d %d\n"
    118     param 1
    119     param 1
    120     param 1
    121     call printf, 4
    122     param "%.0f %u\n"
    123     param 4e+09
    124     param 2000000000
    125     call printf, 3
    126     param "%d %.2e %g\n"
    127     param 666666666
    128     param 12345.678
    129     param 0.0001
    130     call printf, 4
    131     return 0


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
