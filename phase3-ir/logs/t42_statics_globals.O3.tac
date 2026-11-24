============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t42_statics_globals.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 75 -> 64 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           75 -> 64   (14% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           10
   temporaries merged away                 4
   dead instructions removed               5
   jumps removed or redirected             1
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                4
   calls inlined                           4
   tail calls turned into jumps            1
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           2

----------------------------------------------------------------------------
 GLOBALS: 7 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   table            int[6]                         24  { +0: 5, +4: 6 }
   origin           struct Point                    8  { +0: 3 }
   pts              struct Point[3]                24  { +0: 1, +4: 2, +8: 3 }
   names            const char *[3]                12  { +0: "zero", +4: "one" }
   total            int                             4  0
   n.1              int                             4  100
   calls.3          int                             4  0

 As three address code (initial values, in place before main runs):

    table[0] = 5
    table[4] = 6
    origin[0] = 3
    pts[0] = 1
    pts[4] = 2
    pts[8] = 3
    names[0] = "zero"
    names[4] = "one"
    total = 0                 (zero-initialized)
    n.1 = 100
    calls.3 = 0               (zero-initialized)

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 21 temporaries, frame 116 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n1               local   int                             4       0
   n2               local   int                             4       4
   n3               local   int                             4       8
   p                local   int *                           4      12
   t5               temp    int                             4      32
   t6               temp    int                             4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t10              temp    int                             4      52
   t11              temp    int                             4      56
   t12              temp    int                             4      60
   t13              temp    int                             4      64
   t14              temp    const char *                    4      68
   t15              temp    const char *                    4      72
   t16              temp    int                             4      76
   t17              temp    const char *                    4      80
   t18              temp    int *                           4      84
   t19              temp    int                             4      88
   t20              temp    int                             4      92
   t21              temp    int                             4      96
   t22              temp    int                             4     100
   t23              temp    int                             4     104
   t24              temp    int                             4     108
   t25              temp    int                             4     112
   (4 temporaries no longer used after optimization not shown)

 Code: 64 instruction(s)

    100       t21 = n.1
    101       n.1 = n.1 int+ 1
    102       t22 = n.1
    103       n.1 = n.1 int+ 1
    104       t23 = n.1
    105       n.1 = n.1 int+ 1
    106       param "%d %d %d\n"
    107       param t21
    108       param t22
    109       param t23
    110       call printf, 4
    111       t24 = 4
    112  L1:  calls.3 = calls.3 int+ 1
    113       if t24 int!= 0 goto L2
    114       t25 = calls.3
    115       goto L3
    116  L2:  t24 = t24 int- 1
    117       goto L1
    118  L3:  param "%d\n"
    119       param t25
    120       call printf, 2
    121       t5 = table[0]
    122       t6 = table[4]
    123       t7 = table[8]
    124       t8 = table[20]
    125       param "%d %d %d %d\n"
    126       param t5
    127       param t6
    128       param t7
    129       param t8
    130       call printf, 5
    131       t9 = origin[0]
    132       t10 = origin[4]
    133       t11 = pts[8]
    134       t12 = pts[12]
    135       t13 = pts[16]
    136       param "%d %d %d %d %d\n"
    137       param t9
    138       param t10
    139       param t11
    140       param t12
    141       param t13
    142       call printf, 6
    143       t14 = names[0]
    144       t15 = names[4]
    145       t17 = names[8]
    146       if t17 ptr== 0 goto L4
    147       t16 = 0
    148       goto L5
    149  L4:  t16 = 1
    150  L5:  param "%s %s %d\n"
    151       param t14
    152       param t15
    153       param t16
    154       call printf, 4
    155       t18 = &total
    156       *t18 = 42
    157       t19 = table[0]
    158       t20 = total int+ t19
    159       total = t20
    160       param "%d\n"
    161       param t20
    162       call printf, 2
    163       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Point              struct_tag    struct Point               -           4    -    0  size 8
   table              variable      int[6]                     global      5   24    5  
   origin             variable      struct Point               global      6    8    2  
   pts                variable      struct Point[3]            global      7   24    3  
   names              variable      const char *[3]            global      8   12    3  
   total              variable      int                        global      9    4    3  
   next               function      int (void)                 -          10    -    3  _Z4nextv; defined
   depth              function      int (int)                  -          11    -    2  _Z5depthi; defined
   main               function      int (void)                 -          12    -    0  defined

 scope: global > struct Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      4    4    3  Point::x; public, offset 0
   y                  field         int                        member      4    4    2  Point::y; public, offset 4

 scope: global > next()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static     10    4    1  n.1; static

 scope: global > depth()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      11    4    2  k.2
   calls              variable      int                        static     11    4    2  calls.3; static

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n1                 variable      int                        local      13    4    1  n1.4
   n2                 variable      int                        local      13    4    1  n2.5
   n3                 variable      int                        local      13    4    1  n3.6
   p                  variable      int *                      local      19    4    1  p.7

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
