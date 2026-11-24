============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t02_control_flow.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 158 -> 138 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          158 -> 138   (12% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded            8
   temporaries merged away                18
   dead instructions removed               5
   jumps removed or redirected            25
   unreachable instructions removed        7
   propagated across blocks               11
   dead assignments removed                4
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      6
   loops unrolled                          6
   unreachable functions removed           1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 9 temporaries, frame 168 bytes

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
   t25              temp    char                            1     144
   t30              temp    int                             4     164
   (21 temporaries no longer used after optimization not shown)

 Code: 138 instruction(s)

    100        s = 0
    101        i = 0
    102  L1:   if i int>= 5 goto L2
    103        t1 = i
    104        i = i int+ 1
    105        s = s int+ t1
    106        if i int>= 5 goto L2
    107        t1 = i
    108        i = i int+ 1
    109        s = s int+ t1
    110        goto L1
    111  L2:   t4 = s int<< 1
    112        s = t4
    113        if t4 int< 100 goto L2
    114        k.4 = 0
    115  L3:   if k.4 int>= 3 goto L4
    116        s = s int- k.4
    117        k.4 = k.4 int+ 1
    118        if k.4 int>= 3 goto L4
    119        s = s int- k.4
    120        k.4 = k.4 int+ 1
    121        goto L3
    122  L4:   i = 0
    123  L5:   if i int>= 4 goto L6
    124        i = i int+ 1
    125        if i int>= 4 goto L6
    126        i = i int+ 1
    127        goto L5
    128  L6:   u = 0
    129  L7:   if u int>= 4 goto L8
    130        u = u int+ 1
    131        if u int>= 4 goto L8
    132        u = u int+ 1
    133        goto L7
    134  L8:   param "%d %d\n"
    135        param s
    136        param u
    137        call printf, 3
    138        out = 0
    139        i = 0
    140  L9:   if i int>= 6 goto L24
    141        goto L14
    142  L10:  out = out int+ 1
    143  L11:  out = out int+ 10
    144        goto L15
    145  L12:  out = out int+ 100
    146  L13:  out = out int+ 1000
    147        goto L16
    148  L14:  if i int== 0 goto L10
    149        if i int== 1 goto L10
    150        if i int== 4 goto L12
    151        if i int== 5 goto L13
    152        goto L11
    153  L15:  out = out int+ 5
    154  L16:  i = i int+ 1
    155        if i int>= 6 goto L24
    156        goto L21
    157  L17:  out = out int+ 1
    158  L18:  out = out int+ 10
    159        goto L22
    160  L19:  out = out int+ 100
    161  L20:  out = out int+ 1000
    162        goto L23
    163  L21:  if i int== 0 goto L17
    164        if i int== 1 goto L17
    165        if i int== 4 goto L19
    166        if i int== 5 goto L20
    167        goto L18
    168  L22:  out = out int+ 5
    169  L23:  i = i int+ 1
    170        goto L9
    171  L24:  param "%d\n"
    172        param out
    173        call printf, 2
    174        c = 0
    175        hit = 0
    176        r = 0
    177  L25:  if r int>= 4 goto L30
    178        c = 0
    179  L26:  if c int>= 4 goto L29
    180        if c int> r goto L29
    181        t16 = r int+ c
    182        t17 = t16 int% 2
    183        if t17 int!= 0 goto L27
    184        t18 = r int* c
    185        if t18 int== 4 goto L30
    186        hit = hit int+ 1
    187  L27:  c = c int+ 1
    188        if c int>= 4 goto L29
    189        if c int> r goto L29
    190        t16 = r int+ c
    191        t17 = t16 int% 2
    192        if t17 int!= 0 goto L28
    193        t18 = r int* c
    194        if t18 int== 4 goto L30
    195        hit = hit int+ 1
    196  L28:  c = c int+ 1
    197        goto L26
    198  L29:  r = r int+ 1
    199        goto L25
    200  L30:  param "%d %d %d\n"
    201        param hit
    202        param r
    203        param c
    204        call printf, 4
    205        state = 0
    206        words = 0
    207        i = 0
    208  L31:  t22 = "ab 12 x9;" ptr+ i
    209        t23 = *t22
    210        if t23 char== 0 goto L39
    211        t25 = *t22
    212        t30 = chartoint t25
    213        if t30 int< 48 goto L32
    214        if t30 int> 57 goto L32
    215        k.13 = 1
    216        goto L36
    217  L32:  if t30 int< 97 goto L33
    218        if t30 int<= 122 goto L34
    219  L33:  if t30 int< 65 goto L35
    220        if t30 int> 90 goto L35
    221  L34:  k.13 = 2
    222        goto L36
    223  L35:  k.13 = 0
    224  L36:  if state int!= 0 goto L37
    225        if k.13 int== 0 goto L37
    226        words = words int+ 1
    227        state = 1
    228        goto L38
    229  L37:  if state int!= 1 goto L38
    230        if k.13 int!= 0 goto L38
    231        state = 0
    232  L38:  i = i int+ 1
    233        goto L31
    234  L39:  param "%d\n"
    235        param words
    236        call printf, 2
    237        return 0


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
