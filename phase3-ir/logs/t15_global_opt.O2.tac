============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_global_opt.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 138 -> 107 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          138 -> 107   (22% fewer)

   constants folded                        2
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           11
   temporaries merged away                 8
   dead instructions removed               0
   jumps removed or redirected             6
   unreachable instructions removed        2
   propagated across blocks                8
   dead assignments removed               17

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  0

 As three address code (initial values, in place before main runs):

    g = 0

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

 Code: 10 instruction(s)

    103       if c int== 0 goto L1
    104       y = 6
    105       goto L2
    106  L1:  y = 7
    107  L2:  z = 1
    108       if c int== 0 goto L3
    109       z = 2
    110  L3:  t4 = 5 int+ y
    111       t5 = t4 int+ z
    112       return t5

============================================================================
 FUNCTION loop(int)        (link name _Z4loopi)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 2 temporaries, frame 48 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   step             local   int                             4       4
   sum              local   int                             4       8
   last             local   int                             4      12
   i.10             local   int                             4      16
   scratch          local   int                             4      20
   i.12             local   int                             4      24
   t4               temp    int                             4      40
   t5               temp    int                             4      44
   (3 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    113       sum = 0
    114       last = 0
    115       i.10 = 0
    116  L4:  if i.10 int>= n goto L5
    117       sum = sum int+ 3
    118       last = i.10
    119       i.10 = i.10 int+ 1
    120       goto L4
    121  L5:  t4 = sum int+ last
    122       t5 = t4 int+ 100
    123       return t5

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

 Code: 9 instruction(s)

    124       b = a
    125       if a int<= 3 goto L6
    126       a = 0
    127  L6:  t1 = b int+ a
    128       call touch(), 0
    129       t3 = call touch(), 0
    130       t4 = t1 int+ 8
    131       t5 = t4 int+ t3
    132       return t5

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

 Code: 10 instruction(s)

    133     x = 1
    134     t1 = &x
    135     x = 10
    136     t2 = *t1
    137     t3 = t2 int+ 1
    138     s[0] = 3
    139     s[4] = 4
    140     t4 = s[0]
    141     t5 = t3 int+ t4
    142     return t5

============================================================================
 FUNCTION jumps(int)        (link name _Z5jumpsi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   k                local   int                             4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t4               temp    int                             4      24
   t5               temp    int                             4      28
   (2 temporaries no longer used after optimization not shown)

 Code: 17 instruction(s)

    143        k = 0
    144        t = 9
    145  L7:   t1 = k int+ 1
    146        k = t1
    147        if t1 int< n goto L7
    148        goto L11
    149  L8:   t = 1
    150        goto L12
    151  L9:   t = 2
    152  L10:  t = t int+ 10
    153        goto L12
    154  L11:  if n int== 1 goto L8
    155        if n int== 2 goto L9
    156        if n int== 3 goto L10
    157  L12:  t4 = t1 int* 100
    158        t5 = t4 int+ t
    159        return t5

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

 Code: 47 instruction(s)

    160     param 0
    161     t1 = call branches(int), 1
    162     param 1
    163     t2 = call branches(int), 1
    164     param "%d %d\n"
    165     param t1
    166     param t2
    167     call printf, 3
    168     param 0
    169     t3 = call loop(int), 1
    170     param 1
    171     t4 = call loop(int), 1
    172     param 4
    173     t5 = call loop(int), 1
    174     param "%d %d %d\n"
    175     param t3
    176     param t4
    177     param t5
    178     call printf, 4
    179     param 1
    180     t6 = call rewritten(int), 1
    181     param 9
    182     t7 = call rewritten(int), 1
    183     param "%d %d %d\n"
    184     param t6
    185     param t7
    186     param g
    187     call printf, 4
    188     t8 = call viaPointer(), 0
    189     param "%d\n"
    190     param t8
    191     call printf, 2
    192     param 1
    193     t9 = call jumps(int), 1
    194     param 2
    195     t10 = call jumps(int), 1
    196     param 3
    197     t11 = call jumps(int), 1
    198     param 5
    199     t12 = call jumps(int), 1
    200     param "%d %d %d %d\n"
    201     param t9
    202     param t10
    203     param t11
    204     param t12
    205     call printf, 5
    206     return g


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
