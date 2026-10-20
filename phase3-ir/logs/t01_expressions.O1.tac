============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t01_expressions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 199 -> 112 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          199 -> 112   (43% fewer)

   constants folded                       77
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded          172
   temporaries merged away                 0
   dead instructions removed              79
   jumps removed or redirected             4
   unreachable instructions removed        4

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

 Code: 112 instruction(s)

    100     a = 7
    101     b = 3
    102     c = 12
    103     param "%d %d %d %d %d\n"
    104     param 12
    105     param 4
    106     param 21
    107     param 2
    108     param 1
    109     call printf, 6
    110     c = -42
    111     param "%d\n"
    112     param -42
    113     call printf, 2
    114     d = 1.5
    115     f = 2.5
    116     d = 15.5
    117     f = 7.5
    118     truncated = 7
    119     param "%.2f %.2f %d\n"
    120     param 15.5
    121     param 7.5
    122     param 7
    123     call printf, 4
    124     u = 7
    125     u = 33
    126     neg = -16
    127     param "%u %d %d %d\n"
    128     param 33
    129     param -4
    130     param -5
    131     param -1
    132     call printf, 5
    133     param "%d %d %d %d\n"
    134     param 3
    135     param 7
    136     param 4
    137     param -8
    138     call printf, 5
    139     ch = 65
    140     ch = 67
    141     s = 300
    142     s = 600
    143     big = 100000
    144     big = 10000000007
    145     param "%c %d %d %lld\n"
    146     param 67
    147     param 67
    148     param 600
    149     param 10000000007
    150     call printf, 5
    151     a = 12
    152     b = 2
    153     c = -84
    154     a = 4
    155     b = 16
    156     c = 0
    157     a = 12
    158     b = 0
    159     c = 5
    160     d = 15.0
    161     d = 3e+01
    162     param "%d %d %d %.1f\n"
    163     param 12
    164     param 0
    165     param 5
    166     param 3e+01
    167     call printf, 5
    168     i = 5
    169     i = 6
    170     j = 6
    171     param "%d %d\n"
    172     param 6
    173     param 6
    174     call printf, 3
    175     i = 7
    176     j = 14
    177     param "%d %d\n"
    178     param 7
    179     param 14
    180     call printf, 3
    181     i = 6
    182     i = 5
    183     j = 2
    184     j = 3
    185     i = 7
    186     param "%d %d\n"
    187     param 7
    188     param 3
    189     call printf, 3
    190     big2 = 12
    191     mixed = 2.5
    192     param "%d %.1f\n"
    193     param 12
    194     param 2.5
    195     call printf, 3
    196     param "%d %d %d\n"
    197     param 4
    198     param 8
    199     param 1
    200     call printf, 4
    201     param "%d %.3f %d\n"
    202     param 3
    203     param 3.0
    204     param 65
    205     call printf, 4
    206     wraps = 250
    207     wraps = 4
    208     param "%d\n"
    209     param 4
    210     call printf, 2
    211     return 12


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
