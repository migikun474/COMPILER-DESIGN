============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t01_expressions.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 193 -> 69 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          193 -> 69   (64% fewer)

   constants folded                       68
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded          123
   temporaries merged away                 2
   dead instructions removed              68
   jumps removed or redirected            10
   unreachable instructions removed        8
   propagated across blocks               14
   dead assignments removed               35

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 22 parameter(s)/local(s), 1 temporary, frame 432 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   x                local   int                             4      12
   d                local   double                          8      16
   f                local   float                           4      24
   back             local   int                             4      28
   u                local   unsigned int                    4      32
   v                local   int                             4      36
   bits             local   int                             4      40
   t                local   int                             4      44
   i                local   int                             4      48
   j                local   int                             4      52
   k                local   int                             4      56
   m                local   int                             4      60
   ch               local   char                            1      64
   uch              local   unsigned char                   1      65
   sh               local   short                           2      66
   z                local   int                             4      68
   w                local   int                             4      72
   q                local   int                             4      76
   dd               local   double                          8      80
   t28              temp    int                             4     232
   (71 temporaries no longer used after optimization not shown)

 Code: 69 instruction(s)

    100       param "%d %d %d %d %d\n"
    101       param -12
    102       param 13
    103       param 27
    104       param 3
    105       param 1
    106       call printf, 6
    107       param "%.2f %.1f %d %.3f\n"
    108       param 3.5
    109       param 3.0
    110       param 4
    111       param 2.3333332538604736
    112       call printf, 5
    113       param "%u %u %d\n"
    114       param 4294967295
    115       param 7
    116       param 5
    117       call printf, 4
    118       bits = 0
    119       t = 182
    120  L1:  if t int== 0 goto L2
    121       t28 = t int& 1
    122       bits = bits int+ t28
    123       t = t int>> 1
    124       goto L1
    125  L2:  param "%d %d %d %x %x\n"
    126       param bits
    127       param 0
    128       param 1
    129       param 73
    130       param 73
    131       call printf, 6
    132       param "%d\n"
    133       param 7
    134       call printf, 2
    135       param "%d %d %d\n"
    136       param 5
    137       param 6
    138       param 10
    139       call printf, 4
    140       param "%d %d %d\n"
    141       param 12
    142       param 10
    143       param 2
    144       call printf, 4
    145       param "%d %d %d\n"
    146       param 4
    147       param 8
    148       param 1
    149       call printf, 4
    150       param "%d %d %d %d\n"
    151       param -126
    152       param 44
    153       param 1
    154       param 74
    155       call printf, 5
    156       param "%d %d\n"
    157       param -4
    158       param 7
    159       call printf, 3
    160       param "%d %d %d %d %.2f %d\n"
    161       param 0
    162       param 5
    163       param 6
    164       param 2
    165       param 2.0
    166       param 0
    167       call printf, 7
    168       return 0


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
   a                  variable      int                        local       6    4   10  a.1
   b                  variable      int                        local       6    4   10  b.2
   c                  variable      int                        local       6    4    6  c.3
   x                  variable      int                        local       6    4   14  x.4
   d                  variable      double                     local       9    8    2  d.5
   f                  variable      float                      local      10    4    1  f.6
   back               variable      int                        local      11    4    1  back.7
   u                  variable      unsigned int               local      13    4    3  u.8
   v                  variable      int                        local      15    4    5  v.9
   bits               variable      int                        local      16    4    2  bits.10
   t                  variable      int                        local      16    4    3  t.11
   i                  variable      int                        local      22    4    6  i.12
   j                  variable      int                        local      22    4    1  j.13
   k                  variable      int                        local      22    4    1  k.14
   m                  variable      int                        local      24    4    1  m.15
   ch                 variable      char                       local      27    1    2  ch.16
   uch                variable      unsigned char              local      28    1    1  uch.17
   sh                 variable      short                      local      29    2    1  sh.18
   z                  variable      int                        local      32    4    1  z.19
   w                  variable      int                        local      32    4    1  w.20
   q                  variable      int                        local      32    4    1  q.21
   dd                 variable      double                     local      33    8    1  dd.22

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
