============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 140 -> 129 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          140 -> 129   (7% fewer)

   constants folded                        3
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            7
   temporaries merged away                10
   dead instructions removed               2
   jumps removed or redirected            28
   unreachable instructions removed       15
   propagated across blocks               13
   dead assignments removed                1
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          5
   unreachable functions removed           1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 5 temporaries, frame 84 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   i                local   int                             4       0
   total            local   int                             4       4
   n                local   int                             4       8
   fact             local   int                             4      12
   j                local   int                             4      16
   count            local   int                             4      20
   x                local   int                             4      24
   t5               temp    int                             4      44
   t7               temp    int                             4      52
   t11              temp    int                             4      68
   t12              temp    int                             4      72
   t14              temp    int                             4      80
   (9 temporaries no longer used after optimization not shown)

 Code: 129 instruction(s)

    100        total = 0
    101        i = 0
    102  L1:   if i int>= 10 goto L4
    103        if i int== 2 goto L2
    104        if i int== 8 goto L4
    105        total = total int+ i
    106  L2:   i = i int+ 1
    107        if i int>= 10 goto L4
    108        if i int== 2 goto L3
    109        if i int== 8 goto L4
    110        total = total int+ i
    111  L3:   i = i int+ 1
    112        goto L1
    113  L4:   param "for: %d %d\n"
    114        param i
    115        param total
    116        call printf, 3
    117        n = 5
    118        fact = 1
    119  L5:   if n int<= 1 goto L6
    120        fact = fact int* n
    121        n = n int- 1
    122        if n int<= 1 goto L6
    123        fact = fact int* n
    124        n = n int- 1
    125        goto L5
    126  L6:   param "while: %d\n"
    127        param fact
    128        call printf, 2
    129  L7:   t5 = n int+ 3
    130        n = t5
    131        if t5 int< 10 goto L7
    132        param "do: %d\n"
    133        param t5
    134        call printf, 2
    135  L8:   if n int>= 20 goto L9
    136        n = n int+ 4
    137        if n int>= 20 goto L9
    138        n = n int+ 4
    139        goto L8
    140  L9:   param "until: %d\n"
    141        param n
    142        call printf, 2
    143        i = 0
    144  L10:  if i int>= 6 goto L25
    145        t14 = i
    146        goto L15
    147  L11:  t7 = 100
    148        goto L17
    149  L12:  t14 = i int+ 10
    150  L13:  t14 = t14 int<< 1
    151        goto L16
    152  L14:  t14 = -1
    153        goto L16
    154  L15:  if i int== 0 goto L11
    155        if i int== 1 goto L12
    156        if i int== 2 goto L12
    157        if i int== 3 goto L13
    158        goto L14
    159  L16:  t7 = t14
    160  L17:  param "%d "
    161        param t7
    162        call printf, 2
    163        i = i int+ 1
    164        if i int>= 6 goto L25
    165        t14 = i
    166        goto L22
    167  L18:  t7 = 100
    168        goto L24
    169  L19:  t14 = i int+ 10
    170  L20:  t14 = t14 int<< 1
    171        goto L23
    172  L21:  t14 = -1
    173        goto L23
    174  L22:  if i int== 0 goto L18
    175        if i int== 1 goto L19
    176        if i int== 2 goto L19
    177        if i int== 3 goto L20
    178        goto L21
    179  L23:  t7 = t14
    180  L24:  param "%d "
    181        param t7
    182        call printf, 2
    183        i = i int+ 1
    184        goto L10
    185  L25:  param "\n"
    186        call printf, 1
    187        i = 0
    188  L26:  if i int>= 3 goto L29
    189        j = 0
    190  L27:  if j int>= 3 goto L28
    191        if j int> i goto L28
    192        param "%d%d "
    193        param i
    194        param j
    195        call printf, 3
    196        j = j int+ 1
    197        if j int>= 3 goto L28
    198        if j int> i goto L28
    199        param "%d%d "
    200        param i
    201        param j
    202        call printf, 3
    203        j = j int+ 1
    204        goto L27
    205  L28:  i = i int+ 1
    206        goto L26
    207  L29:  param "\n"
    208        call printf, 1
    209        count = 0
    210  L30:  t11 = count int+ 1
    211        count = t11
    212        if t11 int< 4 goto L30
    213        if t11 int== 4 goto L31
    214        count = 99
    215  L31:  param "goto: %d\n"
    216        param count
    217        call printf, 2
    218        x = 3
    219        param "medium\n"
    220        call printf, 1
    221  L32:  t12 = x int- 1
    222        x = t12
    223        if t12 int== 1 goto L32
    224        if t12 int> 0 goto L32
    225        param "x: %d\n"
    226        param t12
    227        call printf, 2
    228        return total


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   classify           function      int (int)                  -           3    -    1  _Z8classifyi; defined
   main               function      int (void)                 -          14    -    0  defined

 scope: global > classify()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       3    4    7  n.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   again              label         -                          -          45    -    1  main.again
   done               label         -                          -          50    -    1  main.done
   i                  variable      int                        local      15    4   16  i.2
   total              variable      int                        local      15    4    3  total.3
   n                  variable      int                        local      23    4   11  n.4
   fact               variable      int                        local      23    4    3  fact.5
   count              variable      int                        local      44    4    5  count.7
   x                  variable      int                        local      53    4    6  x.8

 scope: global > main() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   j                  variable      int                        local      37    4    4  j.6

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
