============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t30_int_edges.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 99 -> 55 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           99 -> 55   (44% fewer)

   constants folded                       38
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           63
   temporaries merged away                 0
   dead instructions removed              38
   jumps removed or redirected             2
   unreachable instructions removed        4

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 0 temporaries, frame 184 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   big              local   int                             4       8
   small            local   int                             4      12
   u                local   unsigned int                    4      16
   c                local   char                            1      20
   uc               local   unsigned char                   1      21
   s                local   short                           2      22
   us               local   unsigned short                  2      24
   x                local   int                             4      28
   (38 temporaries no longer used after optimization not shown)

 Code: 55 instruction(s)

    100     a = -7
    101     b = 2
    102     big = 2147483647
    103     small = -2147483648
    104     param "%d %d %d %d\n"
    105     param -3
    106     param -1
    107     param -3
    108     param 1
    109     call printf, 5
    110     param "%d %d %d\n"
    111     param -3
    112     param -2
    113     param -2
    114     call printf, 4
    115     param "%d %d %u %u\n"
    116     param -4
    117     param -28
    118     param 15
    119     param 2147483648
    120     call printf, 5
    121     u = 0
    122     u = 4294967295
    123     param "%u %u %d\n"
    124     param 4294967295
    125     param 1
    126     param 2147483647
    127     call printf, 4
    128     c = -56
    129     uc = 200
    130     s = -25536
    131     us = 4464
    132     param "%d %d %d %d\n"
    133     param -56
    134     param 200
    135     param -25536
    136     param 4464
    137     call printf, 5
    138     param "%d %d\n"
    139     param 0
    140     param 1
    141     call printf, 3
    142     param "%d %d %u\n"
    143     param 2147483647
    144     param -2147483648
    145     param 2147483648
    146     call printf, 4
    147     x = 1000
    148     x = 3000000
    149     param "%d %d %d\n"
    150     param 3000000
    151     param 0
    152     param 149
    153     call printf, 4
    154     return 0


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
   a                  variable      int                        local       6    4    6  a.1
   b                  variable      int                        local       6    4    3  b.2
   big                variable      int                        local       6    4    2  big.3
   small              variable      int                        local       6    4    1  small.4
   u                  variable      unsigned int               local      10    4    5  u.5
   c                  variable      char                       local      13    1    1  c.6
   uc                 variable      unsigned char              local      14    1    1  uc.7
   s                  variable      short                      local      15    2    1  s.8
   us                 variable      unsigned short             local      16    2    1  us.9
   x                  variable      int                        local      20    4    6  x.10

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
