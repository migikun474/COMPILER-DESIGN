============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t41_loop_edges.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 119 -> 91 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          119 -> 91   (23% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            2
   temporaries merged away                14
   dead instructions removed               1
   jumps removed or redirected            12
   unreachable instructions removed        3
   propagated across blocks                1
   dead assignments removed                0

============================================================================
 FUNCTION count(int)        (link name _Z5counti)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   c                local   int                             4       4
   i                local   int                             4       8
   t1               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    100       c = 0
    101       i = 0
    102  L1:  if i int>= n goto L2
    103       t1 = c int<< 1
    104       c = t1 int+ 1
    105       i = i int+ 1
    106       goto L1
    107  L2:  return c

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 9 parameter(s)/local(s), 10 temporaries, frame 128 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   int                             4       0
   w                local   int                             4       4
   i                local   int                             4       8
   j                local   int                             4      12
   found            local   int                             4      16
   skipped          local   int                             4      20
   k                local   int                             4      24
   total            local   int                             4      28
   s                local   int                             4      32
   t1               temp    int                             4      36
   t2               temp    int                             4      40
   t3               temp    int                             4      44
   t4               temp    int                             4      48
   t5               temp    int                             4      52
   t6               temp    int                             4      56
   t10              temp    int                             4      72
   t11              temp    int                             4      76
   t16              temp    int                             4      96
   t18              temp    int                             4     104
   (13 temporaries no longer used after optimization not shown)

 Code: 83 instruction(s)

    108        param 0
    109        t1 = call count(int), 1
    110        param 1
    111        t2 = call count(int), 1
    112        param 2
    113        t3 = call count(int), 1
    114        param 3
    115        t4 = call count(int), 1
    116        param 7
    117        t5 = call count(int), 1
    118        param "%d %d %d %d %d\n"
    119        param t1
    120        param t2
    121        param t3
    122        param t4
    123        param t5
    124        call printf, 6
    125        d = 0
    126  L3:   t6 = d int+ 1
    127        d = t6
    128        if t6 int< 0 goto L3
    129        w = 10
    130  L4:   if w int>= 10 goto L5
    131        w = w int+ 1
    132        goto L4
    133  L5:   param "%d %d\n"
    134        param t6
    135        param w
    136        call printf, 3
    137        found = -1
    138        skipped = 0
    139        i = 0
    140  L6:   if i int>= 5 goto L11
    141        if found int>= 0 goto L11
    142        j = 0
    143  L7:   if j int>= 5 goto L10
    144        if j int!= 1 goto L8
    145        skipped = skipped int+ 1
    146        goto L9
    147  L8:   t10 = i int* j
    148        if t10 int!= 6 goto L9
    149        t11 = i int* 10
    150        found = t11 int+ j
    151        goto L10
    152  L9:   j = j int+ 1
    153        goto L7
    154  L10:  i = i int+ 1
    155        goto L6
    156  L11:  param "%d %d %d\n"
    157        param found
    158        param i
    159        param skipped
    160        call printf, 4
    161        k = 0
    162        total = 0
    163  L12:  total = total int+ k
    164        t16 = k int+ 1
    165        k = t16
    166        if t16 int< 5 goto L12
    167        param "%d\n"
    168        param total
    169        call printf, 2
    170        s = 0
    171        i = 0
    172  L13:  if i int>= 8 goto L20
    173        t18 = i int% 4
    174        goto L17
    175  L14:  s = s int+ 1
    176        goto L18
    177  L15:  s = s int+ 10
    178  L16:  s = s int+ 100
    179        goto L18
    180  L17:  if t18 int== 0 goto L19
    181        if t18 int== 1 goto L14
    182        if t18 int== 2 goto L15
    183        if t18 int== 3 goto L16
    184  L18:  s = s int+ 1000
    185  L19:  i = i int+ 1
    186        goto L13
    187  L20:  param "%d\n"
    188        param s
    189        call printf, 2
    190        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   count              function      int (int)                  -           5    -    5  _Z5counti; defined
   main               function      int (void)                 -           6    -    0  defined

 scope: global > count()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       5    4    1  n.1
   c                  variable      int                        local       5    4    3  c.2
   i                  variable      int                        local       5    4    3  i.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   again              label         -                          -          21    -    1  main.again
   d                  variable      int                        local       8    4    3  d.4
   w                  variable      int                        local      10    4    3  w.5
   i                  variable      int                        local      13    4   10  i.6
   j                  variable      int                        local      13    4    6  j.7
   found              variable      int                        local      13    4    3  found.8
   skipped            variable      int                        local      13    4    2  skipped.9
   k                  variable      int                        local      20    4    2  k.10
   total              variable      int                        local      20    4    2  total.11
   s                  variable      int                        local      25    4    5  s.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
