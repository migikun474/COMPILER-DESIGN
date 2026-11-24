============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t30_int_edges.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 99 -> 43 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           99 -> 43   (56% fewer)

   constants folded                       38
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           63
   temporaries merged away                 0
   dead instructions removed              38
   jumps removed or redirected             2
   unreachable instructions removed        4
   propagated across blocks                0
   dead assignments removed               12

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

 Code: 43 instruction(s)

    100     param "%d %d %d %d\n"
    101     param -3
    102     param -1
    103     param -3
    104     param 1
    105     call printf, 5
    106     param "%d %d %d\n"
    107     param -3
    108     param -2
    109     param -2
    110     call printf, 4
    111     param "%d %d %u %u\n"
    112     param -4
    113     param -28
    114     param 15
    115     param 2147483648
    116     call printf, 5
    117     param "%u %u %d\n"
    118     param 4294967295
    119     param 1
    120     param 2147483647
    121     call printf, 4
    122     param "%d %d %d %d\n"
    123     param -56
    124     param 200
    125     param -25536
    126     param 4464
    127     call printf, 5
    128     param "%d %d\n"
    129     param 0
    130     param 1
    131     call printf, 3
    132     param "%d %d %u\n"
    133     param 2147483647
    134     param -2147483648
    135     param 2147483648
    136     call printf, 4
    137     param "%d %d %d\n"
    138     param 3000000
    139     param 0
    140     param 149
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
