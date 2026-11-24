============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 158 -> 111 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          158 -> 111   (29% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            1
   temporaries merged away                18
   dead instructions removed               0
   jumps removed or redirected            25
   unreachable instructions removed        7

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

 Symbol table: 12 parameter(s)/local(s), 10 temporaries, frame 160 bytes

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
   t9               temp    int                             4      80
   t16              temp    int                             4     108
   t17              temp    int                             4     112
   t18              temp    int                             4     116
   t22              temp    const char *                    4     132
   t23              temp    char                            1     136
   t24              temp    const char *                    4     140
   t25              temp    char                            1     144
   (18 temporaries no longer used after optimization not shown)

 Code: 96 instruction(s)

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
    145        t9 = i
    146        goto L18
    147  L14:  out = out int+ 1
    148  L15:  out = out int+ 10
    149        goto L19
    150  L16:  out = out int+ 100
    151  L17:  out = out int+ 1000
    152        goto L20
    153  L18:  if t9 int== 0 goto L14
    154        if t9 int== 1 goto L14
    155        if t9 int== 4 goto L16
    156        if t9 int== 5 goto L17
    157        goto L15
    158  L19:  out = out int+ 5
    159  L20:  i = i int+ 1
    160        goto L13
    161  L21:  param "%d\n"
    162        param out
    163        call printf, 2
    164        c = 0
    165        hit = 0
    166        r = 0
    167  L22:  if r int>= 4 goto L26
    168        c = 0
    169  L23:  if c int>= 4 goto L25
    170        if c int> r goto L25
    171        t16 = r int+ c
    172        t17 = t16 int% 2
    173        if t17 int!= 0 goto L24
    174        t18 = r int* c
    175        if t18 int== 4 goto L26
    176        hit = hit int+ 1
    177  L24:  c = c int+ 1
    178        goto L23
    179  L25:  r = r int+ 1
    180        goto L22
    181  L26:  param "%d %d %d\n"
    182        param hit
    183        param r
    184        param c
    185        call printf, 4
    186        text = "ab 12 x9;"
    187        state = 0
    188        words = 0
    189        i = 0
    190  L27:  t22 = text ptr+ i
    191        t23 = *t22
    192        if t23 char== 0 goto L30
    193        t24 = text ptr+ i
    194        t25 = *t24
    195        param t25
    196        k.13 = call kind(char), 1
    197        if state int!= 0 goto L28
    198        if k.13 int== 0 goto L28
    199        words = words int+ 1
    200        state = 1
    201        goto L29
    202  L28:  if state int!= 1 goto L29
    203        if k.13 int!= 0 goto L29
    204        state = 0
    205  L29:  i = i int+ 1
    206        goto L27
    207  L30:  param "%d\n"
    208        param words
    209        call printf, 2
    210        return 0


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
