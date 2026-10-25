============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_global_opt.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 138 -> 139 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          138 -> 139   (0% fewer)

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
   instructions moved out of loops         0

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

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   t1               temp    int                             4      16
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   (2 temporaries no longer used after optimization not shown)

 Code: 11 instruction(s)

    124       b = a
    125       if a int<= 3 goto L6
    126       a = 0
    127  L6:  t1 = b int+ a
    128       t6 = g int+ 1
    129       g = t6
    130       t7 = t6 int+ 1
    131       g = t7
    132       t4 = t1 int+ 8
    133       t5 = t4 int+ t7
    134       return t5

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

    135     x = 1
    136     t1 = &x
    137     x = 10
    138     t2 = *t1
    139     t3 = t2 int+ 1
    140     s[0] = 3
    141     s[4] = 4
    142     t4 = s[0]
    143     t5 = t3 int+ t4
    144     return t5

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

    145        k = 0
    146        t = 9
    147  L7:   t1 = k int+ 1
    148        k = t1
    149        if t1 int< n goto L7
    150        goto L11
    151  L8:   t = 1
    152        goto L12
    153  L9:   t = 2
    154  L10:  t = t int+ 10
    155        goto L12
    156  L11:  if n int== 1 goto L8
    157        if n int== 2 goto L9
    158        if n int== 3 goto L10
    159  L12:  t4 = t1 int* 100
    160        t5 = t4 int+ t
    161        return t5

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
   t57              temp    struct (unnamed at 44:5)        8     232
   t58              temp    int                             4     240
   t59              temp    int                             4     244
   (29 temporaries no longer used after optimization not shown)

 Code: 77 instruction(s)

    162        param "%d %d\n"
    163        param 13
    164        param 13
    165        call printf, 3
    166        t24 = 0
    167        t25 = 0
    168        t26 = 0
    169  L13:  if t26 int>= 0 goto L14
    170        t24 = t24 int+ 3
    171        t25 = t26
    172        t26 = t26 int+ 1
    173        goto L13
    174  L14:  t27 = t24 int+ t25
    175        t3 = t27 int+ 100
    176        t30 = 0
    177        t31 = 0
    178        t32 = 0
    179  L15:  if t32 int>= 1 goto L16
    180        t30 = t30 int+ 3
    181        t31 = t32
    182        t32 = t32 int+ 1
    183        goto L15
    184  L16:  t33 = t30 int+ t31
    185        t4 = t33 int+ 100
    186        t36 = 0
    187        t37 = 0
    188        t38 = 0
    189  L17:  if t38 int>= 4 goto L18
    190        t36 = t36 int+ 3
    191        t37 = t38
    192        t38 = t38 int+ 1
    193        goto L17
    194  L18:  t39 = t36 int+ t37
    195        t40 = t39 int+ 100
    196        param "%d %d %d\n"
    197        param t3
    198        param t4
    199        param t40
    200        call printf, 4
    201        call touch(), 0
    202        t44 = call touch(), 0
    203        t6 = 10 int+ t44
    204        call touch(), 0
    205        t50 = call touch(), 0
    206        t52 = 17 int+ t50
    207        param "%d %d %d\n"
    208        param t6
    209        param t52
    210        param g
    211        call printf, 4
    212        t53 = 1
    213        t54 = &t53
    214        t53 = 10
    215        t55 = *t54
    216        t56 = t55 int+ 1
    217        t57[0] = 3
    218        t57[4] = 4
    219        t58 = t57[0]
    220        t59 = t56 int+ t58
    221        param "%d\n"
    222        param t59
    223        call printf, 2
    224        param 1
    225        t9 = call jumps(int), 1
    226        param 2
    227        t10 = call jumps(int), 1
    228        param 3
    229        t11 = call jumps(int), 1
    230        param 5
    231        t12 = call jumps(int), 1
    232        param "%d %d %d %d\n"
    233        param t9
    234        param t10
    235        param t11
    236        param t12
    237        call printf, 5
    238        return g


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
