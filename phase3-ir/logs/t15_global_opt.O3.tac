============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_global_opt.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 138 -> 109 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          138 -> 109   (21% fewer)

   constants folded                       16
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           41
   temporaries merged away                12
   dead instructions removed              25
   jumps removed or redirected            10
   unreachable instructions removed        7
   propagated across blocks               11
   dead assignments removed               20
   calls inlined                          10
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          4
   unreachable functions removed           4

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

    103       k = 0
    104       t = 9
    105  L1:  t1 = k int+ 1
    106       k = t1
    107       if t1 int< n goto L1
    108       goto L5
    109  L2:  t = 1
    110       goto L6
    111  L3:  t = 2
    112  L4:  t = t int+ 10
    113       goto L6
    114  L5:  if n int== 1 goto L2
    115       if n int== 2 goto L3
    116       if n int== 3 goto L4
    117  L6:  t4 = t1 int* 100
    118       t5 = t4 int+ t
    119       return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 30 temporaries, frame 248 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r1               local   int                             4       0
   r9               local   int                             4       4
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t6               temp    int                             4      28
   t9               temp    int                             4      40
   t10              temp    int                             4      44
   t11              temp    int                             4      48
   t12              temp    int                             4      52
   t24              temp    int                             4     100
   t25              temp    int                             4     104
   t26              temp    int                             4     108
   t27              temp    int                             4     112
   t30              temp    int                             4     124
   t31              temp    int                             4     128
   t32              temp    int                             4     132
   t33              temp    int                             4     136
   t36              temp    int                             4     148
   t37              temp    int                             4     152
   t38              temp    int                             4     156
   t39              temp    int                             4     160
   t40              temp    int                             4     164
   t44              temp    int                             4     180
   t50              temp    int                             4     204
   t52              temp    int                             4     212
   t53              temp    int                             4     216
   t54              temp    int *                           4     220
   t55              temp    int                             4     224
   t56              temp    int                             4     228
   t57              temp    struct (unnamed at 43:5)        8     232
   t58              temp    int                             4     240
   t59              temp    int                             4     244
   (29 temporaries no longer used after optimization not shown)

 Code: 89 instruction(s)

    120        param "%d %d\n"
    121        param 13
    122        param 13
    123        call printf, 3
    124        t24 = 0
    125        t25 = 0
    126        t26 = 0
    127  L7:   if t26 int>= 0 goto L8
    128        t24 = t24 int+ 3
    129        t25 = t26
    130        t26 = t26 int+ 1
    131        if t26 int>= 0 goto L8
    132        t24 = t24 int+ 3
    133        t25 = t26
    134        t26 = t26 int+ 1
    135        goto L7
    136  L8:   t27 = t24 int+ t25
    137        t3 = t27 int+ 100
    138        t30 = 0
    139        t31 = 0
    140        t32 = 0
    141  L9:   if t32 int>= 1 goto L10
    142        t30 = t30 int+ 3
    143        t31 = t32
    144        t32 = t32 int+ 1
    145        if t32 int>= 1 goto L10
    146        t30 = t30 int+ 3
    147        t31 = t32
    148        t32 = t32 int+ 1
    149        goto L9
    150  L10:  t33 = t30 int+ t31
    151        t4 = t33 int+ 100
    152        t36 = 0
    153        t37 = 0
    154        t38 = 0
    155  L11:  if t38 int>= 4 goto L12
    156        t36 = t36 int+ 3
    157        t37 = t38
    158        t38 = t38 int+ 1
    159        if t38 int>= 4 goto L12
    160        t36 = t36 int+ 3
    161        t37 = t38
    162        t38 = t38 int+ 1
    163        goto L11
    164  L12:  t39 = t36 int+ t37
    165        t40 = t39 int+ 100
    166        param "%d %d %d\n"
    167        param t3
    168        param t4
    169        param t40
    170        call printf, 4
    171        call touch(), 0
    172        t44 = call touch(), 0
    173        t6 = 10 int+ t44
    174        call touch(), 0
    175        t50 = call touch(), 0
    176        t52 = 17 int+ t50
    177        param "%d %d %d\n"
    178        param t6
    179        param t52
    180        param g
    181        call printf, 4
    182        t53 = 1
    183        t54 = &t53
    184        t53 = 10
    185        t55 = *t54
    186        t56 = t55 int+ 1
    187        t57[0] = 3
    188        t57[4] = 4
    189        t58 = t57[0]
    190        t59 = t56 int+ t58
    191        param "%d\n"
    192        param t59
    193        call printf, 2
    194        param 1
    195        t9 = call jumps(int), 1
    196        param 2
    197        t10 = call jumps(int), 1
    198        param 3
    199        t11 = call jumps(int), 1
    200        param 5
    201        t12 = call jumps(int), 1
    202        param "%d %d %d %d\n"
    203        param t9
    204        param t10
    205        param t11
    206        param t12
    207        call printf, 5
    208        return g


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      4    4    4  
   touch              function      int (void)                 -           5    -    2  _Z5touchv; defined
   branches           function      int (int)                  -           7    -    2  _Z8branchesi; defined
   loop               function      int (int)                  -          16    -    3  _Z4loopi; defined
   rewritten          function      int (int)                  -          27    -    2  _Z9rewritteni; defined
   viaPointer         function      int (void)                 -          37    -    1  _Z10viaPointerv; defined
   jumps              function      int (int)                  -          48    -    4  _Z5jumpsi; defined
   main               function      int (void)                 -          61    -    0  defined

 scope: global > branches()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     int                        param       7    4    2  c.1
   x                  variable      int                        local       8    4    3  x.2
   y                  variable      int                        local       8    4    4  y.3
   z                  variable      int                        local      10    4    2  z.4
   unused             variable      int                        local      12    4    0  unused.5

 scope: global > loop()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      16    4    1  n.6
   step               variable      int                        local      17    4    1  step.7
   sum                variable      int                        local      17    4    3  sum.8
   last               variable      int                        local      17    4    2  last.9
   i                  variable      int                        local      23    4    1  i.12

 scope: global > loop() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      18    4    3  i.10

 scope: global > loop() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   scratch            variable      int                        local      21    4    0  scratch.11

 scope: global > rewritten()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      27    4    7  a.13
   b                  variable      int                        local      28    4    1  b.14
   c                  variable      int                        local      30    4    1  c.15
   d                  variable      int                        local      32    4    2  d.16

 scope: global > viaPointer()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      38    4    2  x.17
   y                  variable      int                        local      38    4    3  y.18
   p                  variable      int *                      local      39    4    1  p.19
   (unnamed at 43:5)  struct_tag    struct (unnamed at 43:5)   -          43    -    0  size 8
   s                  variable      struct (unnamed at 43:5)   local      43    8    3  s.20

 scope: global > viaPointer() > struct (unnamed at 43:5)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member     43    4    2  (unnamed at 43:5)::a; public, offset 0
   b                  field         int                        member     43    4    1  (unnamed at 43:5)::b; public, offset 4

 scope: global > jumps()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      48    4    2  n.21
   again              label         -                          -          50    -    1  _Z5jumpsi.again
   k                  variable      int                        local      49    4    3  k.22
   t                  variable      int                        local      49    4    5  t.23

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r1                 variable      int                        local      64    4    1  r1.24
   r9                 variable      int                        local      64    4    1  r9.25

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct (unnamed at 43:5): size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
