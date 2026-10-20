============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_global_opt.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 138 -> 124 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          138 -> 124   (10% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           11
   temporaries merged away                 7
   dead instructions removed               0
   jumps removed or redirected             6
   unreachable instructions removed        2

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  0

============================================================================
 FUNCTION touch()        (link name _Z5touchv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    100     t1 = g int+ 1
    101     g = t1
    102     return t1

============================================================================
 FUNCTION branches(int)        (link name _Z8branchesi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 2 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   int                             4       0
   x                local   int                             4       4
   y                local   int                             4       8
   z                local   int                             4      12
   unused           local   int                             4      16
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   (3 temporaries no longer used after optimization not shown)

 Code: 12 instruction(s)

    103       x = 5
    104       if c int== 0 goto L1
    105       y = x int+ 1
    106       goto L2
    107  L1:  y = x int+ 2
    108  L2:  z = 1
    109       if c int== 0 goto L3
    110       z = 2
    111  L3:  unused = y int* 100
    112       t4 = x int+ y
    113       t5 = t4 int+ z
    114       return t5

============================================================================
 FUNCTION loop(int)        (link name _Z4loopi)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 3 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   step             local   int                             4       4
   sum              local   int                             4       8
   last             local   int                             4      12
   i.10             local   int                             4      16
   scratch          local   int                             4      20
   i.12             local   int                             4      24
   t1               temp    int                             4      28
   t4               temp    int                             4      40
   t5               temp    int                             4      44
   (2 temporaries no longer used after optimization not shown)

 Code: 15 instruction(s)

    115       step = 3
    116       sum = 0
    117       last = 0
    118       i.10 = 0
    119  L4:  if i.10 int>= n goto L5
    120       t1 = sum int+ step
    121       sum = t1
    122       last = i.10
    123       scratch = t1 int<< 1
    124       i.10 = i.10 int+ 1
    125       goto L4
    126  L5:  i.12 = 100
    127       t4 = sum int+ last
    128       t5 = t4 int+ 100
    129       return t5

============================================================================
 FUNCTION rewritten(int)        (link name _Z9rewritteni)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 4 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   t1               temp    int                             4      16
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   (1 temporary no longer used after optimization not shown)

 Code: 13 instruction(s)

    130       b = a
    131       if a int<= 3 goto L6
    132       a = 0
    133  L6:  t1 = b int+ a
    134       c = t1
    135       a = 7
    136       a = 8
    137       d = call touch(), 0
    138       t3 = call touch(), 0
    139       d = t3
    140       t4 = t1 int+ 8
    141       t5 = t4 int+ t3
    142       return t5

============================================================================
 FUNCTION viaPointer()        (link name _Z10viaPointerv)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   p                local   int *                           4       8
   s                local   struct (unnamed at 44:5)        8      12
   t1               temp    int *                           4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36

 Code: 14 instruction(s)

    143     x = 1
    144     y = 2
    145     t1 = &x
    146     p = t1
    147     x = 10
    148     y = 20
    149     t2 = *t1
    150     t3 = t2 int+ 1
    151     y = t3
    152     s[0] = 3
    153     s[4] = 4
    154     t4 = s[0]
    155     t5 = t3 int+ t4
    156     return t5

============================================================================
 FUNCTION jumps(int)        (link name _Z5jumpsi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 4 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   k                local   int                             4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t4               temp    int                             4      24
   t5               temp    int                             4      28
   (1 temporary no longer used after optimization not shown)

 Code: 18 instruction(s)

    157        k = 0
    158        t = 9
    159  L7:   t1 = k int+ 1
    160        k = t1
    161        if t1 int< n goto L7
    162        t2 = n
    163        goto L11
    164  L8:   t = 1
    165        goto L12
    166  L9:   t = 2
    167  L10:  t = t int+ 10
    168        goto L12
    169  L11:  if t2 int== 1 goto L8
    170        if t2 int== 2 goto L9
    171        if t2 int== 3 goto L10
    172  L12:  t4 = k int* 100
    173        t5 = t4 int+ t
    174        return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 12 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r1               local   int                             4       0
   r9               local   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32
   t8               temp    int                             4      36
   t9               temp    int                             4      40
   t10              temp    int                             4      44
   t11              temp    int                             4      48
   t12              temp    int                             4      52

 Code: 49 instruction(s)

    175     param 0
    176     t1 = call branches(int), 1
    177     param 1
    178     t2 = call branches(int), 1
    179     param "%d %d\n"
    180     param t1
    181     param t2
    182     call printf, 3
    183     param 0
    184     t3 = call loop(int), 1
    185     param 1
    186     t4 = call loop(int), 1
    187     param 4
    188     t5 = call loop(int), 1
    189     param "%d %d %d\n"
    190     param t3
    191     param t4
    192     param t5
    193     call printf, 4
    194     param 1
    195     t6 = call rewritten(int), 1
    196     r1 = t6
    197     param 9
    198     t7 = call rewritten(int), 1
    199     r9 = t7
    200     param "%d %d %d\n"
    201     param t6
    202     param t7
    203     param g
    204     call printf, 4
    205     t8 = call viaPointer(), 0
    206     param "%d\n"
    207     param t8
    208     call printf, 2
    209     param 1
    210     t9 = call jumps(int), 1
    211     param 2
    212     t10 = call jumps(int), 1
    213     param 3
    214     t11 = call jumps(int), 1
    215     param 5
    216     t12 = call jumps(int), 1
    217     param "%d %d %d %d\n"
    218     param t9
    219     param t10
    220     param t11
    221     param t12
    222     call printf, 5
    223     return g


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      5    4    4  
   touch              function      int (void)                 -           6    -    2  _Z5touchv; defined
   branches           function      int (int)                  -           8    -    2  _Z8branchesi; defined
   loop               function      int (int)                  -          17    -    3  _Z4loopi; defined
   rewritten          function      int (int)                  -          28    -    2  _Z9rewritteni; defined
   viaPointer         function      int (void)                 -          38    -    1  _Z10viaPointerv; defined
   jumps              function      int (int)                  -          49    -    4  _Z5jumpsi; defined
   main               function      int (void)                 -          62    -    0  defined

 scope: global > branches()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     int                        param       8    4    2  c.1
   x                  variable      int                        local       9    4    3  x.2
   y                  variable      int                        local       9    4    4  y.3
   z                  variable      int                        local      11    4    2  z.4
   unused             variable      int                        local      13    4    0  unused.5

 scope: global > loop()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      17    4    1  n.6
   step               variable      int                        local      18    4    1  step.7
   sum                variable      int                        local      18    4    3  sum.8
   last               variable      int                        local      18    4    2  last.9
   i                  variable      int                        local      24    4    1  i.12

 scope: global > loop() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      19    4    3  i.10

 scope: global > loop() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   scratch            variable      int                        local      22    4    0  scratch.11

 scope: global > rewritten()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      28    4    7  a.13
   b                  variable      int                        local      29    4    1  b.14
   c                  variable      int                        local      31    4    1  c.15
   d                  variable      int                        local      33    4    2  d.16

 scope: global > viaPointer()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      39    4    2  x.17
   y                  variable      int                        local      39    4    3  y.18
   p                  variable      int *                      local      40    4    1  p.19
   (unnamed at 44:5)  struct_tag    struct (unnamed at 44:5)   -          44    -    0  size 8
   s                  variable      struct (unnamed at 44:5)   local      44    8    3  s.20

 scope: global > viaPointer() > struct (unnamed at 44:5)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member     44    4    2  (unnamed at 44:5)::a; public, offset 0
   b                  field         int                        member     44    4    1  (unnamed at 44:5)::b; public, offset 4

 scope: global > jumps()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      49    4    2  n.21
   again              label         -                          -          51    -    1  _Z5jumpsi.again
   k                  variable      int                        local      50    4    3  k.22
   t                  variable      int                        local      50    4    5  t.23

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r1                 variable      int                        local      65    4    1  r1.24
   r9                 variable      int                        local      65    4    1  r9.25

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct (unnamed at 44:5): size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
