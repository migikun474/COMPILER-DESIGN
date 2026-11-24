============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t05_pointers.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 104 -> 93 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          104 -> 93   (10% fewer)

   calls inlined                           1
   constants folded                        0
   algebraic simplifications               1
   common subexpressions                   3
   copies / constants forwarded           19
   temporaries merged away                 4
   dead instructions removed               6
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

 Symbol table: 15 parameter(s)/local(s), 30 temporaries, frame 252 bytes

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
   (10 temporaries no longer used after optimization not shown)

 Code: 91 instruction(s)

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
    112       *pp = t6
    113       t7 = *p
    114       t9 = *t6
    115       param "%d %d %d\n"
    116       param x
    117       param t7
    118       param t9
    119       call printf, 4
    120       a[0] = 10
    121       a[4] = 20
    122       a[8] = 30
    123       a[12] = 40
    124       a[16] = 50
    125       t10 = &a
    126       t11 = t10 ptr+ 4
    127       q = t11
    128       t13 = t10 ptr+ 16
    129       r = t13
    130       t14 = *t11
    131       t15 = t11 ptr+ 8
    132       t16 = *t15
    133       t17 = t13 ptr- t11
    134       t18 = t17 int/ 4
    135       if t13 ptr> t11 goto L1
    136       t19 = 0
    137       goto L2
    138  L1:  t19 = 1
    139  L2:  param "%d %d %d %d\n"
    140       param t14
    141       param t16
    142       param t18
    143       param t19
    144       call printf, 5
    145       t20 = q ptr+ 8
    146       q = t20
    147       t22 = t20 ptr- 4
    148       q = t22
    149       *t20 = 7
    150       t23 = a[12]
    151       t24 = *t22
    152       param "%d %d\n"
    153       param t23
    154       param t24
    155       call printf, 3
    156       t25 = &a
    157       t26 = t25 ptr+ 8
    158       v = t26
    159       back = t26
    160       t27 = *t26
    161       param "%d\n"
    162       param t27
    163       call printf, 2
    164       row[0] = 1
    165       row[4] = 2
    166       row[8] = 3
    167       t28 = &row
    168       pa = t28
    169       t29 = t28 ptr+ 8
    170       t30 = *t29
    171       param "%d %d\n"
    172       param t30
    173       param 12
    174       call printf, 3
    175       t31 = &x
    176       t32 = &y
    177       list[0] = t31
    178       list[4] = t32
    179       list[8] = t25
    180       s = 0
    181       i = 0
    182  L3:  if i int>= 3 goto L4
    183       t34 = i int<< 2                     (w = 4)
    184       t35 = list[t34]
    185       t36 = *t35
    186       s = s int+ t36
    187       i = i int+ 1
    188       goto L3
    189  L4:  param "%d\n"
    190       param s
    191       call printf, 2
    192       return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

4 9 9
20 40 3 1
7 30
30
3 12
23

   exit code 0, 104 instructions executed
