============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t05_pointers.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 104 -> 96 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          104 -> 96   (7% fewer)

   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   2
   copies / constants forwarded           16
   temporaries merged away                 4
   dead instructions removed               3
   jumps removed or redirected             1
   unreachable instructions removed        0

============================================================================
 FUNCTION redirect(int **, int *)        (link name _Z8redirectPPiS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   pp               param   int **                          4       0
   to               param   int *                           4       4

 Code: 2 instruction(s)

    100     *pp = to
    101     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 31 temporaries, frame 244 bytes

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
   t8               temp    int *                           4     120
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
   t20              temp    int *                           4     168
   t22              temp    int *                           4     176
   t23              temp    int                             4     180
   t24              temp    int                             4     184
   t25              temp    int *                           4     188
   t26              temp    int *                           4     192
   t27              temp    int                             4     196
   t28              temp    int (*)[3]                      4     200
   t29              temp    int (*)[3]                      4     204
   t30              temp    int                             4     208
   t31              temp    int *                           4     212
   t32              temp    int *                           4     216
   t34              temp    int                             4     224
   t35              temp    int *                           4     228
   t36              temp    int                             4     232
   (7 temporaries no longer used after optimization not shown)

 Code: 94 instruction(s)

    102       x = 3
    103       y = 9
    104       p = &x
    105       pp = &p
    106       t3 = &pp
    107       ppp = t3
    108       t4 = *t3
    109       t5 = *t4
    110       *t5 = 4
    111       t6 = &y
    112       param pp
    113       param t6
    114       call redirect(int **, int *), 2
    115       t7 = *p
    116       t8 = *pp
    117       t9 = *t8
    118       param "%d %d %d\n"
    119       param x
    120       param t7
    121       param t9
    122       call printf, 4
    123       a[0] = 10
    124       a[4] = 20
    125       a[8] = 30
    126       a[12] = 40
    127       a[16] = 50
    128       t10 = &a
    129       t11 = t10 ptr+ 4
    130       q = t11
    131       t13 = t10 ptr+ 16
    132       r = t13
    133       t14 = *t11
    134       t15 = t11 ptr+ 8
    135       t16 = *t15
    136       t17 = t13 ptr- t11
    137       t18 = t17 int/ 4
    138       if t13 ptr> t11 goto L1
    139       t19 = 0
    140       goto L2
    141  L1:  t19 = 1
    142  L2:  param "%d %d %d %d\n"
    143       param t14
    144       param t16
    145       param t18
    146       param t19
    147       call printf, 5
    148       t20 = q ptr+ 8
    149       q = t20
    150       t22 = t20 ptr- 4
    151       q = t22
    152       *t20 = 7
    153       t23 = a[12]
    154       t24 = *t22
    155       param "%d %d\n"
    156       param t23
    157       param t24
    158       call printf, 3
    159       t25 = &a
    160       t26 = t25 ptr+ 8
    161       v = t26
    162       back = t26
    163       t27 = *t26
    164       param "%d\n"
    165       param t27
    166       call printf, 2
    167       row[0] = 1
    168       row[4] = 2
    169       row[8] = 3
    170       t28 = &row
    171       pa = t28
    172       t29 = t28 ptr+ 8
    173       t30 = *t29
    174       param "%d %d\n"
    175       param t30
    176       param 12
    177       call printf, 3
    178       t31 = &x
    179       t32 = &y
    180       list[0] = t31
    181       list[4] = t32
    182       list[8] = t25
    183       s = 0
    184       i = 0
    185  L3:  if i int>= 3 goto L4
    186       t34 = i int<< 2                     (w = 4)
    187       t35 = list[t34]
    188       t36 = *t35
    189       s = s int+ t36
    190       i = i int+ 1
    191       goto L3
    192  L4:  param "%d\n"
    193       param s
    194       call printf, 2
    195       return 0


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
