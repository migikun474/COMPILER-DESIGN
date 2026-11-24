============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t01_expressions.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 193 -> 125 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          193 -> 125   (35% fewer)

   constants folded                       56
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded          111
   temporaries merged away                 2
   dead instructions removed              56
   jumps removed or redirected             7
   unreachable instructions removed        4

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 22 parameter(s)/local(s), 14 temporaries, frame 432 bytes

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
   t31              temp    int                             4     244
   t32              temp    int                             4     248
   t33              temp    int                             4     252
   t36              temp    int                             4     264
   t37              temp    int                             4     268
   t38              temp    int                             4     272
   t55              temp    int                             4     340
   t56              temp    int                             4     344
   t57              temp    int                             4     348
   t69              temp    double                          8     400
   t70              temp    double                          8     408
   t71              temp    double                          8     416
   t72              temp    double                          8     424
   (58 temporaries no longer used after optimization not shown)

 Code: 125 instruction(s)

    100       a = 7
    101       b = 2
    102       c = 3
    103       x = -12
    104       param "%d %d %d %d %d\n"
    105       param -12
    106       param 13
    107       param 27
    108       param 3
    109       param 1
    110       call printf, 6
    111       d = 7.0
    112       f = 3.0
    113       back = 4
    114       param "%.2f %.1f %d %.3f\n"
    115       param 3.5
    116       param 3.0
    117       param 4
    118       param 2.3333332538604736
    119       call printf, 5
    120       u = 10
    121       param "%u %u %d\n"
    122       param 4294967295
    123       param 7
    124       param 5
    125       call printf, 4
    126       v = 182
    127       bits = 0
    128       t = 182
    129  L1:  if t int== 0 goto L2
    130       t28 = t int& 1
    131       bits = bits int+ t28
    132       t = t int>> 1
    133       goto L1
    134  L2:  t32 = v int- 1
    135       t33 = v int& t32
    136       if t33 int== 0 goto L3
    137       t31 = 0
    138       goto L4
    139  L3:  t31 = 1
    140  L4:  t36 = v int^ 255
    141       t37 = int~ v
    142       t38 = t37 int& 255
    143       param "%d %d %d %x %x\n"
    144       param bits
    145       param t31
    146       param 1
    147       param t36
    148       param t38
    149       call printf, 6
    150       x = 5
    151       x = 8
    152       x = 7
    153       x = 28
    154       x = 9
    155       x = 4
    156       x = 32
    157       x = 16
    158       x = 17
    159       x = 1
    160       x = 7
    161       param "%d\n"
    162       param 7
    163       call printf, 2
    164       i = 5
    165       i = 6
    166       j = 6
    167       i = 5
    168       k = 10
    169       param "%d %d %d\n"
    170       param 5
    171       param 6
    172       param 10
    173       call printf, 4
    174       i = 3
    175       m = 12
    176       t55 = 10
    177       if a int>= b goto L5
    178       t56 = a
    179       goto L8
    180  L5:  if b int>= c goto L6
    181       t57 = b
    182       goto L7
    183  L6:  t57 = c
    184  L7:  t56 = t57
    185  L8:  param "%d %d %d\n"
    186       param m
    187       param t55
    188       param t56
    189       call printf, 4
    190       param "%d %d %d\n"
    191       param 4
    192       param 8
    193       param 1
    194       call printf, 4
    195       ch = -126
    196       uch = 44
    197       sh = 1
    198       param "%d %d %d %d\n"
    199       param -126
    200       param 44
    201       param 1
    202       param 74
    203       call printf, 5
    204       param "%d %d\n"
    205       param -4
    206       param 7
    207       call printf, 3
    208       z = 0
    209       w = 5
    210       q = 6
    211       t69 = inttodouble a
    212       t70 = t69 double/ 2.0
    213       t71 = t70 double- 0.25
    214       dd = t71
    215       t72 = t71 double- 1.25
    216       param "%d %d %d %d %.2f %d\n"
    217       param 0
    218       param 5
    219       param 6
    220       param 2
    221       param t72
    222       param 0
    223       call printf, 7
    224       return 0


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
