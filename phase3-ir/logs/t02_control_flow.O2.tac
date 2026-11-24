============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 158 -> 109 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          158 -> 109   (31% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            1
   temporaries merged away                18
   dead instructions removed               0
   jumps removed or redirected            25
   unreachable instructions removed        7
   propagated across blocks                6
   dead assignments removed                2

============================================================================
 FUNCTION kind(char)        (link name _Z4kindc)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   char                            1       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    int                             4      24

 Code: 15 instruction(s)

    100       t1 = chartoint c
    101       if t1 int< 48 goto L1
    102       t2 = chartoint c
    103       if t2 int> 57 goto L1
    104       return 1
    105  L1:  t3 = chartoint c
    106       if t3 int< 97 goto L2
    107       t4 = chartoint c
    108       if t4 int<= 122 goto L3
    109  L2:  t5 = chartoint c
    110       if t5 int< 65 goto L4
    111       t6 = chartoint c
    112       if t6 int> 90 goto L4
    113  L3:  return 2
    114  L4:  return 0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 9 temporaries, frame 160 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                local   int                             4       0
   i                local   int                             4       4
   k.4              local   int                             4       8
   u                local   int                             4      12
   out              local   int                             4      16
   r                local   int                             4      20
   c                local   int                             4      24
   hit              local   int                             4      28
   text             local   const char *                    4      32
   state            local   int                             4      36
   words            local   int                             4      40
   k.13             local   int                             4      44
   t1               temp    int                             4      48
   t4               temp    int                             4      60
   t16              temp    int                             4     108
   t17              temp    int                             4     112
   t18              temp    int                             4     116
   t22              temp    const char *                    4     132
   t23              temp    char                            1     136
   t24              temp    const char *                    4     140
   t25              temp    char                            1     144
   (19 temporaries no longer used after optimization not shown)

 Code: 94 instruction(s)

    115        s = 0
    116        i = 0
    117  L5:   if i int>= 5 goto L6
    118        t1 = i
    119        i = i int+ 1
    120        s = s int+ t1
    121        goto L5
    122  L6:   t4 = s int<< 1
    123        s = t4
    124        if t4 int< 100 goto L6
    125        k.4 = 0
    126  L7:   if k.4 int>= 3 goto L8
    127        s = s int- k.4
    128        k.4 = k.4 int+ 1
    129        goto L7
    130  L8:   i = 0
    131  L9:   if i int>= 4 goto L10
    132        i = i int+ 1
    133        goto L9
    134  L10:  u = 0
    135  L11:  if u int>= 4 goto L12
    136        u = u int+ 1
    137        goto L11
    138  L12:  param "%d %d\n"
    139        param s
    140        param u
    141        call printf, 3
    142        out = 0
    143        i = 0
    144  L13:  if i int>= 6 goto L21
    145        goto L18
    146  L14:  out = out int+ 1
    147  L15:  out = out int+ 10
    148        goto L19
    149  L16:  out = out int+ 100
    150  L17:  out = out int+ 1000
    151        goto L20
    152  L18:  if i int== 0 goto L14
    153        if i int== 1 goto L14
    154        if i int== 4 goto L16
    155        if i int== 5 goto L17
    156        goto L15
    157  L19:  out = out int+ 5
    158  L20:  i = i int+ 1
    159        goto L13
    160  L21:  param "%d\n"
    161        param out
    162        call printf, 2
    163        c = 0
    164        hit = 0
    165        r = 0
    166  L22:  if r int>= 4 goto L26
    167        c = 0
    168  L23:  if c int>= 4 goto L25
    169        if c int> r goto L25
    170        t16 = r int+ c
    171        t17 = t16 int% 2
    172        if t17 int!= 0 goto L24
    173        t18 = r int* c
    174        if t18 int== 4 goto L26
    175        hit = hit int+ 1
    176  L24:  c = c int+ 1
    177        goto L23
    178  L25:  r = r int+ 1
    179        goto L22
    180  L26:  param "%d %d %d\n"
    181        param hit
    182        param r
    183        param c
    184        call printf, 4
    185        state = 0
    186        words = 0
    187        i = 0
    188  L27:  t22 = "ab 12 x9;" ptr+ i
    189        t23 = *t22
    190        if t23 char== 0 goto L30
    191        t24 = "ab 12 x9;" ptr+ i
    192        t25 = *t24
    193        param t25
    194        k.13 = call kind(char), 1
    195        if state int!= 0 goto L28
    196        if k.13 int== 0 goto L28
    197        words = words int+ 1
    198        state = 1
    199        goto L29
    200  L28:  if state int!= 1 goto L29
    201        if k.13 int!= 0 goto L29
    202        state = 0
    203  L29:  i = i int+ 1
    204        goto L27
    205  L30:  param "%d\n"
    206        param words
    207        call printf, 2
    208        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               function      int (char)                 -           4    -    1  _Z4kindc; defined
   main               function      int (void)                 -           9    -    0  defined

 scope: global > kind()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     char                       param       4    1    6  c.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   done               label         -                          -          37    -    1  main.done
   s                  variable      int                        local      10    4    5  s.2
   i                  variable      int                        local      10    4   13  i.3
   u                  variable      int                        local      15    4    3  u.5
   out                variable      int                        local      18    4    6  out.6
   r                  variable      int                        local      29    4    7  r.7
   c                  variable      int                        local      29    4    7  c.8
   hit                variable      int                        local      29    4    2  hit.9
   text               variable      const char *               local      39    4    2  text.10
   state              variable      int                        local      40    4    4  state.11
   words              variable      int                        local      40    4    2  words.12

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      13    4    3  k.4

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  variable      int                        local      42    4    2  k.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
