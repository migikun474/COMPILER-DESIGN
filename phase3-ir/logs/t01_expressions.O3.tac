============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t01_expressions.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 199 -> 69 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          199 -> 69   (65% fewer)

   constants folded                       77
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded          172
   temporaries merged away                 0
   dead instructions removed              79
   jumps removed or redirected             4
   unreachable instructions removed        4
   propagated across blocks                0
   dead assignments removed               43
   calls inlined                           0
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 16 parameter(s)/local(s), 0 temporaries, frame 464 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   double                          8      16
   f                local   float                           4      24
   truncated        local   int                             4      28
   u                local   unsigned int                    4      32
   neg              local   int                             4      36
   ch               local   char                            1      40
   s                local   short                           2      42
   big              local   long long                       8      48
   i                local   int                             4      56
   j                local   int                             4      60
   big2             local   int                             4      64
   mixed            local   double                          8      72
   wraps            local   unsigned char                   1      80
   (79 temporaries no longer used after optimization not shown)

 Code: 69 instruction(s)

    100     param "%d %d %d %d %d\n"
    101     param 12
    102     param 4
    103     param 21
    104     param 2
    105     param 1
    106     call printf, 6
    107     param "%d\n"
    108     param -42
    109     call printf, 2
    110     param "%.2f %.2f %d\n"
    111     param 15.5
    112     param 7.5
    113     param 7
    114     call printf, 4
    115     param "%u %d %d %d\n"
    116     param 33
    117     param -4
    118     param -5
    119     param -1
    120     call printf, 5
    121     param "%d %d %d %d\n"
    122     param 3
    123     param 7
    124     param 4
    125     param -8
    126     call printf, 5
    127     param "%c %d %d %lld\n"
    128     param 67
    129     param 67
    130     param 600
    131     param 10000000007
    132     call printf, 5
    133     param "%d %d %d %.1f\n"
    134     param 12
    135     param 0
    136     param 5
    137     param 3e+01
    138     call printf, 5
    139     param "%d %d\n"
    140     param 6
    141     param 6
    142     call printf, 3
    143     param "%d %d\n"
    144     param 7
    145     param 14
    146     call printf, 3
    147     param "%d %d\n"
    148     param 7
    149     param 3
    150     call printf, 3
    151     param "%d %.1f\n"
    152     param 12
    153     param 2.5
    154     call printf, 3
    155     param "%d %d %d\n"
    156     param 4
    157     param 8
    158     param 1
    159     call printf, 4
    160     param "%d %.3f %d\n"
    161     param 3
    162     param 3.0
    163     param 65
    164     call printf, 4
    165     param "%d\n"
    166     param 4
    167     call printf, 2
    168     return 12


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
   a                  variable      int                        local       6    4   24  a.1
   b                  variable      int                        local       6    4   20  b.2
   c                  variable      int                        local       6    4    8  c.3
   d                  variable      double                     local      12    8    7  d.4
   f                  variable      float                      local      13    4    3  f.5
   truncated          variable      int                        local      16    4    1  truncated.6
   u                  variable      unsigned int               local      19    4    5  u.7
   neg                variable      int                        local      21    4    3  neg.8
   ch                 variable      char                       local      25    1    4  ch.9
   s                  variable      short                      local      27    2    3  s.10
   big                variable      long long                  local      29    8    4  big.11
   i                  variable      int                        local      36    4    8  i.12
   j                  variable      int                        local      36    4    8  j.13
   big2               variable      int                        local      45    4    1  big2.14
   mixed              variable      double                     local      46    8    1  mixed.15
   wraps              variable      unsigned char              local      50    1    3  wraps.16

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
