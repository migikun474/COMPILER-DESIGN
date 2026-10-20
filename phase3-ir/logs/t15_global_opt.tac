============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t15_global_opt.c
   Optimization  : no optimization
   Result        : Three address code generated: 7 function(s), 138 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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
    102     return g

============================================================================
 FUNCTION branches(int)        (link name _Z8branchesi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 5 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   int                             4       0
   x                local   int                             4       4
   y                local   int                             4       8
   z                local   int                             4      12
   unused           local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36

 Code: 17 instruction(s)

    103       x = 5
    104       if c int!= 0 goto L1
    105       goto L2
    106  L1:  t1 = x int+ 1
    107       y = t1
    108       goto L3
    109  L2:  t2 = x int+ 2
    110       y = t2
    111  L3:  z = 1
    112       if c int!= 0 goto L4
    113       goto L5
    114  L4:  z = 2
    115  L5:  t3 = y int* 100
    116       unused = t3
    117       t4 = x int+ y
    118       t5 = t4 int+ z
    119       return t5

============================================================================
 FUNCTION loop(int)        (link name _Z4loopi)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 5 temporaries, frame 48 bytes

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
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int                             4      40
   t5               temp    int                             4      44

 Code: 18 instruction(s)

    120       step = 3
    121       sum = 0
    122       last = 0
    123       i.10 = 0
    124  L6:  if i.10 int< n goto L7
    125       goto L8
    126  L7:  t1 = sum int+ step
    127       sum = t1
    128       last = i.10
    129       t2 = sum int* 2
    130       scratch = t2
    131       t3 = i.10 int+ 1
    132       i.10 = t3
    133       goto L6
    134  L8:  i.12 = 100
    135       t4 = sum int+ last
    136       t5 = t4 int+ i.12
    137       return t5

============================================================================
 FUNCTION rewritten(int)        (link name _Z9rewritteni)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32

 Code: 15 instruction(s)

    138        b = a
    139        if a int> 3 goto L9
    140        goto L10
    141  L9:   a = 0
    142  L10:  t1 = b int+ a
    143        c = t1
    144        a = 7
    145        a = 8
    146        t2 = call touch(), 0
    147        d = t2
    148        t3 = call touch(), 0
    149        d = t3
    150        t4 = c int+ a
    151        t5 = t4 int+ d
    152        return t5

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

    153     x = 1
    154     y = 2
    155     t1 = &x
    156     p = t1
    157     x = 10
    158     y = 20
    159     t2 = *p
    160     t3 = t2 int+ 1
    161     y = t3
    162     s[0] = 3
    163     s[4] = 4
    164     t4 = s[0]
    165     t5 = y int+ t4
    166     return t5

============================================================================
 FUNCTION jumps(int)        (link name _Z5jumpsi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 5 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   k                local   int                             4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24
   t5               temp    int                             4      28

 Code: 22 instruction(s)

    167        k = 0
    168        t = 9
    169  L11:  t1 = k int+ 1
    170        k = t1
    171        if k int< n goto L12
    172        goto L13
    173  L12:  goto L11
    174  L13:  t2 = n
    175        goto L17
    176  L14:  t = 1
    177        goto L18
    178  L15:  t = 2
    179  L16:  t3 = t int+ 10
    180        t = t3
    181        goto L18
    182        goto L18
    183  L17:  if t2 int== 1 goto L14
    184        if t2 int== 2 goto L15
    185        if t2 int== 3 goto L16
    186  L18:  t4 = k int* 100
    187        t5 = t4 int+ t
    188        return t5

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

    189     param 0
    190     t1 = call branches(int), 1
    191     param 1
    192     t2 = call branches(int), 1
    193     param "%d %d\n"
    194     param t1
    195     param t2
    196     call printf, 3
    197     param 0
    198     t3 = call loop(int), 1
    199     param 1
    200     t4 = call loop(int), 1
    201     param 4
    202     t5 = call loop(int), 1
    203     param "%d %d %d\n"
    204     param t3
    205     param t4
    206     param t5
    207     call printf, 4
    208     param 1
    209     t6 = call rewritten(int), 1
    210     r1 = t6
    211     param 9
    212     t7 = call rewritten(int), 1
    213     r9 = t7
    214     param "%d %d %d\n"
    215     param r1
    216     param r9
    217     param g
    218     call printf, 4
    219     t8 = call viaPointer(), 0
    220     param "%d\n"
    221     param t8
    222     call printf, 2
    223     param 1
    224     t9 = call jumps(int), 1
    225     param 2
    226     t10 = call jumps(int), 1
    227     param 3
    228     t11 = call jumps(int), 1
    229     param 5
    230     t12 = call jumps(int), 1
    231     param "%d %d %d %d\n"
    232     param t9
    233     param t10
    234     param t11
    235     param t12
    236     call printf, 5
    237     return g


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
