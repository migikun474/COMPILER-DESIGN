============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t19_scopes.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 98 -> 64 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           98 -> 64   (34% fewer)

   constants folded                        6
   algebraic simplifications               1
   common subexpressions                   0
   copies / constants forwarded           39
   temporaries merged away                 7
   dead instructions removed              16
   jumps removed or redirected             2
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed               15
   calls inlined                          11
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          2
   unreachable functions removed           6

----------------------------------------------------------------------------
 GLOBALS: 5 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   x                int                             4  100
   counter          int                             4  0
   hidden           int                             4  7
   n.1              int                             4  10
   calls.2          int                             4  0

 As three address code (initial values, in place before main runs):

    x = 100
    counter = 0
    hidden = 7
    n.1 = 10
    calls.2 = 0               (zero-initialized)

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 15 temporaries, frame 152 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x.12             local   int                             4       0
   n1               local   int                             4       4
   n2               local   int                             4       8
   a                local   int                             4      12
   b                local   int                             4      16
   c                local   int                             4      20
   counter.18       local   int                             4      24
   t17              temp    int                             4      92
   t18              temp    int                             4      96
   t19              temp    int                             4     100
   t20              temp    int                             4     104
   t21              temp    int                             4     108
   t22              temp    int                             4     112
   t23              temp    int                             4     116
   t24              temp    int                             4     120
   t25              temp    int                             4     124
   t26              temp    int                             4     128
   t27              temp    int                             4     132
   t28              temp    int                             4     136
   t29              temp    int                             4     140
   t30              temp    int                             4     144
   t31              temp    int                             4     148
   (16 temporaries no longer used after optimization not shown)

 Code: 64 instruction(s)

    100       t17 = x int+ hidden
    101       param "%d %d %d\n"
    102       param 12
    103       param t17
    104       param x
    105       call printf, 4
    106       x = x int+ 1
    107       counter = counter int+ 1
    108       x = x int+ 1
    109       counter = counter int+ 1
    110       t18 = x int+ hidden
    111       param "%d %d %d\n"
    112       param 5
    113       param t18
    114       param counter
    115       call printf, 4
    116       t19 = n.1 int+ 5
    117       n.1 = t19
    118       t20 = t19 int+ 5
    119       n.1 = t20
    120       param "%d %d\n"
    121       param t19
    122       param t20
    123       call printf, 3
    124       t21 = calls.2 int+ 1
    125       calls.2 = t21
    126       t22 = t21 int<< 1
    127       t23 = t21 int+ 1
    128       calls.2 = t23
    129       t24 = t23 int<< 1
    130       t25 = t23 int+ 1
    131       calls.2 = t25
    132       t26 = t25 int<< 1
    133       param "%d %d %d\n"
    134       param t22
    135       param t24
    136       param t26
    137       call printf, 4
    138       t27 = 0
    139       t28 = 0
    140  L1:  if t28 int>= 3 goto L4
    141       t29 = t28 int* t28
    142       t30 = 10
    143  L2:  if t30 int>= 12 goto L3
    144       t27 = t27 int+ t30
    145       t30 = t30 int+ 1
    146       if t30 int>= 12 goto L3
    147       t27 = t27 int+ t30
    148       t30 = t30 int+ 1
    149       goto L2
    150  L3:  t27 = t27 int+ t29
    151       t28 = t28 int+ 1
    152       goto L1
    153  L4:  t31 = t27 int+ 50
    154       param "%d\n"
    155       param t31
    156       call printf, 2
    157       param "%d\n"
    158       param -2
    159       call printf, 2
    160       param "%d\n"
    161       param counter
    162       call printf, 2
    163       return 5


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        global      4    4    4  
   counter            variable      int                        global      5    4    3  
   hidden             variable      int                        global      6    4    1  static
   next               function      int (void)                 -           8    -    2  _Z4nextv; defined
   twice              function      int (void)                 -           9    -    3  _Z5twicev; defined
   shadow             function      int (int)                  -          11    -    1  _Z6shadowi; defined
   useGlobal          function      int (void)                 -          25    -    2  _Z9useGlobalv; defined
   changeGlobal       function      void (void)                -          27    -    2  _Z12changeGlobalv; defined
   loops              function      int (void)                 -          29    -    1  _Z5loopsv; defined
   main               function      int (void)                 -          40    -    0  defined

 scope: global > next()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static      8    4    2  n.1; static

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        static      9    4    2  calls.2; static

 scope: global > shadow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      11    4    2  x.3
   r                  variable      int                        local      12    4    4  r.4

 scope: global > shadow() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      14    4    2  x.5

 scope: global > shadow() > block > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      17    4    1  x.6

 scope: global > loops()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      30    4    3  total.7
   i                  variable      int                        local      36    4    1  i.11

 scope: global > loops() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      31    4    4  i.8

 scope: global > loops() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i2                 variable      int                        local      32    4    1  i2.9

 scope: global > loops() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      33    4    3  i.10

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      44    4    2  x.12
   n1                 variable      int                        local      46    4    1  n1.13
   n2                 variable      int                        local      46    4    1  n2.14
   a                  variable      int                        local      48    4    1  a.15
   b                  variable      int                        local      48    4    1  b.16
   c                  variable      int                        local      48    4    1  c.17

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   counter            variable      int                        local      52    4    2  counter.18

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
