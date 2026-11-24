============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t05_pointers.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 104 -> 86 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          104 -> 86   (17% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   3
   copies / constants forwarded           24
   temporaries merged away                 4
   dead instructions removed               9
   jumps removed or redirected             1
   unreachable instructions removed        0
   propagated across blocks                1
   dead assignments removed                8
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      3
   loops unrolled                          1
   unreachable functions removed           1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 27 temporaries, frame 252 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   y                local   int                             4       4
   p                local   int *                           4       8
   pp               local   int **                          4      12
   ppp              local   int ***                         4      16
   a                local   int[5]                         20      20
   q                local   int *                           4      40
   r                local   int *                           4      44
   v                local   void *                          4      48
   back             local   int *                           4      52
   row              local   int[3]                         12      56
   pa               local   int (*)[3]                      4      68
   list             local   int *[3]                       12      72
   s                local   int                             4      84
   i                local   int                             4      88
   t3               temp    int ***                         4     100
   t4               temp    int **                          4     104
   t5               temp    int *                           4     108
   t6               temp    int *                           4     112
   t7               temp    int                             4     116
   t9               temp    int                             4     124
   t10              temp    int *                           4     128
   t11              temp    int *                           4     132
   t13              temp    int *                           4     140
   t14              temp    int                             4     144
   t15              temp    int *                           4     148
   t16              temp    int                             4     152
   t17              temp    int                             4     156
   t18              temp    int                             4     160
   t19              temp    int                             4     164
   t22              temp    int *                           4     176
   t23              temp    int                             4     180
   t24              temp    int                             4     184
   t26              temp    int *                           4     192
   t27              temp    int                             4     196
   t28              temp    int (*)[3]                      4     200
   t29              temp    int (*)[3]                      4     204
   t30              temp    int                             4     208
   t31              temp    int *                           4     212
   t34              temp    int                             4     224
   t35              temp    int *                           4     228
   t36              temp    int                             4     232
   (13 temporaries no longer used after optimization not shown)

 Code: 86 instruction(s)

    100       x = 3
    101       y = 9
    102       p = &x
    103       pp = &p
    104       t3 = &pp
    105       t4 = *t3
    106       t5 = *t4
    107       *t5 = 4
    108       t6 = &y
    109       *pp = t6
    110       t7 = *p
    111       t9 = *t6
    112       param "%d %d %d\n"
    113       param x
    114       param t7
    115       param t9
    116       call printf, 4
    117       a[0] = 10
    118       a[4] = 20
    119       a[8] = 30
    120       a[12] = 40
    121       a[16] = 50
    122       t10 = &a
    123       t11 = t10 ptr+ 4
    124       t13 = t10 ptr+ 16
    125       t14 = *t11
    126       t15 = t11 ptr+ 8
    127       t16 = *t15
    128       t17 = t13 ptr- t11
    129       t18 = t17 int/ 4
    130       if t13 ptr> t11 goto L1
    131       t19 = 0
    132       goto L2
    133  L1:  t19 = 1
    134  L2:  param "%d %d %d %d\n"
    135       param t14
    136       param t16
    137       param t18
    138       param t19
    139       call printf, 5
    140       t22 = t15 ptr- 4
    141       *t15 = 7
    142       t23 = a[12]
    143       t24 = *t22
    144       param "%d %d\n"
    145       param t23
    146       param t24
    147       call printf, 3
    148       t26 = t10 ptr+ 8
    149       t27 = *t26
    150       param "%d\n"
    151       param t27
    152       call printf, 2
    153       row[0] = 1
    154       row[4] = 2
    155       row[8] = 3
    156       t28 = &row
    157       t29 = t28 ptr+ 8
    158       t30 = *t29
    159       param "%d %d\n"
    160       param t30
    161       param 12
    162       call printf, 3
    163       t31 = &x
    164       list[0] = t31
    165       list[4] = t6
    166       list[8] = t10
    167       s = 0
    168       i = 0
    169  L3:  if i int>= 3 goto L4
    170       t34 = i int<< 2                     (w = 4)
    171       t35 = list[t34]
    172       t36 = *t35
    173       s = s int+ t36
    174       i = i int+ 1
    175       if i int>= 3 goto L4
    176       t34 = i int<< 2                     (w = 4)
    177       t35 = list[t34]
    178       t36 = *t35
    179       s = s int+ t36
    180       i = i int+ 1
    181       goto L3
    182  L4:  param "%d\n"
    183       param s
    184       call printf, 2
    185       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   redirect           function      void (int **, int *)       -           4    -    1  _Z8redirectPPiS_; defined
   main               function      int (void)                 -           5    -    0  defined

 scope: global > redirect()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pp                 parameter     int **                     param       4    4    1  pp.1
   to                 parameter     int *                      param       4    4    1  to.2

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local       6    4    3  x.3
   y                  variable      int                        local       6    4    2  y.4
   p                  variable      int *                      local       7    4    2  p.5
   pp                 variable      int **                     local       7    4    3  pp.6
   ppp                variable      int ***                    local       7    4    1  ppp.7
   a                  variable      int[5]                     local      11   20    5  a.8
   q                  variable      int *                      local      12    4    7  q.9
   r                  variable      int *                      local      12    4    2  r.10
   v                  variable      void *                     local      17    4    1  v.11
   back               variable      int *                      local      18    4    1  back.12
   row                variable      int[3]                     local      20   12    1  row.13
   pa                 variable      int (*)[3]                 local      21    4    2  pa.14
   list               variable      int *[3]                   local      23   12    1  list.15
   s                  variable      int                        local      24    4    2  s.16
   i                  variable      int                        local      24    4    4  i.17

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
