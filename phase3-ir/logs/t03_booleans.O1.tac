============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 163 -> 91 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          163 -> 91   (44% fewer)

   calls inlined                           0
   constants folded                       15
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           32
   temporaries merged away                 3
   dead instructions removed              12
   jumps removed or redirected            35
   unreachable instructions removed       20

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 13 temporaries, frame 160 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   e                local   int                             4      16
   f                local   int                             4      20
   x                local   int                             4      24
   y                local   int                             4      28
   t                local   int                             4      32
   p                local   bool                            1      36
   q                local   bool                            1      37
   i                local   int                             4      40
   n                local   int                             4      44
   t14              temp    int                             4     100
   t15              temp    int                             4     104
   t16              temp    int                             4     108
   t17              temp    int                             4     112
   t18              temp    int                             4     116
   t19              temp    bool                            1     120
   t20              temp    int                             4     124
   t21              temp    bool                            1     128
   t22              temp    int                             4     132
   t23              temp    int                             4     136
   t24              temp    int                             4     140
   t25              temp    int                             4     144
   t26              temp    int                             4     148
   (15 temporaries no longer used after optimization not shown)

 Code: 91 instruction(s)

    100        a = 1
    101        b = 2
    102        c = 5
    103        d = 4
    104        e = 6
    105        f = 7
    106        x = 1
    107        y = 0
    108        param "%d %d %d %d\n"
    109        param 1
    110        param 0
    111        param 0
    112        param 1
    113        call printf, 5
    114        t = 2
    115        goto L1
    116  L1:   t15 = 1
    117        if t15 int== 1 goto L2
    118        t14 = 0
    119        goto L3
    120  L2:   t14 = 1
    121  L3:   if c int> d goto L4
    122        t16 = 0
    123        goto L5
    124  L4:   t16 = 1
    125  L5:   t17 = t16 int* 10
    126        param "%d %d %d\n"
    127        param t
    128        param t14
    129        param t17
    130        call printf, 4
    131        if c int> d goto L6
    132        t18 = 0
    133        goto L7
    134  L6:   t18 = 1
    135  L7:   if t18 int!= 0 goto L8
    136        t19 = 0
    137        goto L9
    138  L8:   t19 = 1
    139  L9:   p = t19
    140        if t19 bool== 0 goto L10
    141        t20 = 0
    142        goto L11
    143  L10:  t20 = 1
    144  L11:  if t20 int!= 0 goto L12
    145        t21 = 0
    146        goto L13
    147  L12:  t21 = 1
    148  L13:  q = t21
    149        t22 = booltoint p
    150        t23 = booltoint t21
    151        if p bool== 0 goto L14
    152        if q bool== 0 goto L15
    153  L14:  t24 = 0
    154        goto L16
    155  L15:  t24 = 1
    156  L16:  if p bool!= 0 goto L17
    157        if q bool!= 0 goto L17
    158        t25 = 0
    159        goto L18
    160  L17:  t25 = 1
    161  L18:  param "%d %d %d %d\n"
    162        param t22
    163        param t23
    164        param t24
    165        param t25
    166        call printf, 5
    167        i = 0
    168        n = 0
    169  L19:  if i int>= 10 goto L20
    170        if i int> 6 goto L20
    171        if n int> 20 goto L20
    172        t26 = i
    173        i = i int+ 1
    174        n = n int+ t26
    175        goto L19
    176  L20:  param "%d %d\n"
    177        param i
    178        param n
    179        call printf, 3
    180        if a int>= b goto L21
    181        if c int!= d goto L22
    182  L21:  param "wrong\n"
    183        call printf, 1
    184        goto L23
    185  L22:  param "right\n"
    186        call printf, 1
    187  L23:  if a int== 0 goto L24
    188        param "t\n"
    189        call printf, 1
    190  L24:  return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           4    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       5    4    6  a.1
   b                  variable      int                        local       5    4    5  b.2
   c                  variable      int                        local       5    4    7  c.3
   d                  variable      int                        local       5    4    6  d.4
   e                  variable      int                        local       5    4    3  e.5
   f                  variable      int                        local       5    4    3  f.6
   x                  variable      int                        local       6    4    2  x.7
   y                  variable      int                        local       7    4    1  y.8
   t                  variable      int                        local       9    4    1  t.9
   p                  variable      bool                       local      11    1    4  p.10
   q                  variable      bool                       local      11    1    3  q.11
   i                  variable      int                        local      13    4    4  i.12
   n                  variable      int                        local      13    4    3  n.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

1 0 0 1
2 1 10
1 0 1 1
7 21
right
t

   exit code 0, 117 instructions executed
