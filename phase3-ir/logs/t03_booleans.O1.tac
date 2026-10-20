============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 234 -> 167 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          234 -> 167   (28% fewer)

   constants folded                       12
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           25
   temporaries merged away                 3
   dead instructions removed               5
   jumps removed or redirected            34
   unreachable instructions removed       22

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

============================================================================
 FUNCTION yes()        (link name _Z3yesv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    100     calls = calls int+ 1
    101     return 1

============================================================================
 FUNCTION no()        (link name _Z2nov)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   (1 temporary no longer used after optimization not shown)

 Code: 2 instruction(s)

    102     calls = calls int+ 1
    103     return 0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 31 temporaries, frame 208 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   e                local   int                             4      16
   f                local   int                             4      20
   r                local   int                             4      24
   x                local   int                             4      28
   z                local   double                          8      32
   ch               local   char                            1      40
   p                local   int *                           4      44
   flag             local   bool                            1      48
   both             local   bool                            1      49
   big              local   unsigned int                    4      52
   minus            local   int                             4      56
   t3               temp    int                             4      68
   t4               temp    int                             4      72
   t5               temp    int                             4      76
   t6               temp    int                             4      80
   t7               temp    int                             4      84
   t8               temp    int                             4      88
   t9               temp    int                             4      92
   t10              temp    int                             4      96
   t11              temp    int                             4     100
   t12              temp    int                             4     104
   t13              temp    int                             4     108
   t14              temp    int                             4     112
   t15              temp    int                             4     116
   t16              temp    int                             4     120
   t17              temp    int                             4     124
   t18              temp    int                             4     128
   t19              temp    int                             4     132
   t20              temp    int                             4     136
   t21              temp    int                             4     140
   t22              temp    int                             4     144
   t23              temp    int                             4     148
   t24              temp    int                             4     152
   t25              temp    int                             4     156
   t26              temp    int                             4     160
   t27              temp    int                             4     164
   t28              temp    int                             4     168
   t29              temp    bool                            1     172
   t30              temp    int                             4     176
   t31              temp    bool                            1     180
   t32              temp    int                             4     184
   t33              temp    int                             4     188
   (6 temporaries no longer used after optimization not shown)

 Code: 163 instruction(s)

    104        a = 1
    105        b = 2
    106        c = 3
    107        d = 4
    108        e = 5
    109        f = 6
    110        r = 1
    111        param "%d\n"
    112        param 1
    113        call printf, 2
    114        r = 0
    115        t3 = 1
    116        t4 = 1
    117        t5 = 0
    118        if b int>= 2 goto L1
    119        t6 = 0
    120        goto L2
    121  L1:   t6 = 1
    122  L2:   if b int<= 1 goto L3
    123        t7 = 0
    124        goto L4
    125  L3:   t7 = 1
    126  L4:   param "%d %d %d %d %d %d\n"
    127        param r
    128        param t3
    129        param t4
    130        param t5
    131        param t6
    132        param t7
    133        call printf, 7
    134        calls = 0
    135        t8 = call no(), 0
    136        if t8 int== 0 goto L5
    137        t9 = call yes(), 0
    138        if t9 int== 0 goto L5
    139        param "no\n"
    140        call printf, 1
    141  L5:   param "calls after &&: %d\n"
    142        param calls
    143        call printf, 2
    144        calls = 0
    145        t10 = call yes(), 0
    146        if t10 int!= 0 goto L6
    147        t11 = call no(), 0
    148        if t11 int== 0 goto L7
    149  L6:   param "or taken\n"
    150        call printf, 1
    151  L7:   param "calls after ||: %d\n"
    152        param calls
    153        call printf, 2
    154        calls = 0
    155        t13 = call no(), 0
    156        if t13 int!= 0 goto L8
    157        t14 = call yes(), 0
    158        if t14 int== 0 goto L9
    159  L8:   t15 = call no(), 0
    160        if t15 int== 0 goto L10
    161  L9:   t12 = 0
    162        goto L11
    163  L10:  t12 = 1
    164  L11:  r = t12
    165        param "%d %d\n"
    166        param t12
    167        param calls
    168        call printf, 3
    169        x = 0
    170        z = 0.5
    171        ch = 0
    172        p = 0
    173        t16 = 1
    174        t17 = 0
    175        t18 = 1
    176        t19 = 1
    177        if c int!= 0 goto L12
    178        t20 = 0
    179        goto L13
    180  L12:  t20 = 1
    181  L13:  param "%d %d %d %d %d\n"
    182        param t16
    183        param t17
    184        param t18
    185        param t19
    186        param t20
    187        call printf, 6
    188        if z double!= 0.0 goto L14
    189        goto L15
    190  L14:  param "double is true\n"
    191        call printf, 1
    192  L15:  if p ptr!= 0 goto L16
    193        param "null pointer is false\n"
    194        call printf, 1
    195  L16:  if a int< b goto L17
    196        t21 = 0
    197        goto L18
    198  L17:  t21 = 1
    199  L18:  if b int< c goto L19
    200        t22 = 0
    201        goto L20
    202  L19:  t22 = 1
    203  L20:  t23 = t21 int+ t22
    204        if c int< a goto L21
    205        t24 = 0
    206        goto L22
    207  L21:  t24 = 1
    208  L22:  t25 = t23 int+ t24
    209        r = t25
    210        param "%d\n"
    211        param t25
    212        call printf, 2
    213        if a int== 0 goto L23
    214        if b int!= 0 goto L24
    215  L23:  t26 = 0
    216        goto L25
    217  L24:  t26 = 1
    218  L25:  r = t26
    219        if x int!= 0 goto L26
    220        if ch char!= 0 goto L26
    221        t27 = 0
    222        goto L27
    223  L26:  t27 = 1
    224  L27:  param "%d %d\n"
    225        param r
    226        param t27
    227        call printf, 3
    228        if c int> a goto L28
    229        t28 = 0
    230        goto L29
    231  L28:  t28 = 1
    232  L29:  if t28 int!= 0 goto L30
    233        t29 = 0
    234        goto L31
    235  L30:  t29 = 1
    236  L31:  flag = t29
    237        if t29 bool== 0 goto L32
    238        if d int!= 0 goto L33
    239  L32:  t30 = 0
    240        goto L34
    241  L33:  t30 = 1
    242  L34:  if t30 int!= 0 goto L35
    243        t31 = 0
    244        goto L36
    245  L35:  t31 = 1
    246  L36:  both = t31
    247        t32 = booltoint flag
    248        t33 = booltoint t31
    249        param "%d %d\n"
    250        param t32
    251        param t33
    252        call printf, 3
    253  L37:  if x int>= 3 goto L38
    254        if x int== 2 goto L38
    255        x = x int+ 1
    256        goto L37
    257  L38:  param "%d\n"
    258        param x
    259        call printf, 2
    260        big = 4000000000
    261        minus = -1
    262        param "%d %d\n"
    263        param 1
    264        param 1
    265        call printf, 3
    266        return r


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      4    4    8  
   yes                function      int (void)                 -           5    -    3  _Z3yesv; defined
   no                 function      int (void)                 -           6    -    4  _Z2nov; defined
   main               function      int (void)                 -           8    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       9    4    9  a.1
   b                  variable      int                        local       9    4    8  b.2
   c                  variable      int                        local       9    4    5  c.3
   d                  variable      int                        local       9    4    2  d.4
   e                  variable      int                        local       9    4    1  e.5
   f                  variable      int                        local       9    4    1  f.6
   r                  variable      int                        local      10    4   10  r.7
   x                  variable      int                        local      25    4    6  x.8
   z                  variable      double                     local      26    8    2  z.9
   ch                 variable      char                       local      27    1    2  ch.10
   p                  variable      int *                      local      28    4    2  p.11
   flag               variable      bool                       local      36    1    2  flag.12
   both               variable      bool                       local      37    1    1  both.13
   big                variable      unsigned int               local      41    4    1  big.14
   minus              variable      int                        local      42    4    1  minus.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
