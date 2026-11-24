============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t42_statics_globals.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 75 -> 74 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           75 -> 74   (1% fewer)

   calls inlined                           3
   constants folded                        0
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           11
   temporaries merged away                 3
   dead instructions removed               3
   jumps removed or redirected             1
   unreachable instructions removed        0

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
 FUNCTION next()        (link name _Z4nextv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0
   (1 temporary no longer used after optimization not shown)

 Code: 3 instruction(s)

    100     t1 = n.1
    101     n.1 = n.1 int+ 1
    102     return t1

============================================================================
 FUNCTION depth(int)        (link name _Z5depthi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    103       calls.3 = calls.3 int+ 1
    104       if k int!= 0 goto L1
    105       t2 = calls.3
    106       goto L2
    107  L1:  t3 = k int- 1
    108       param t3
    109       t2 = call depth(int), 1
    110  L2:  return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 20 temporaries, frame 108 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n1               local   int                             4       0
   n2               local   int                             4       4
   n3               local   int                             4       8
   p                local   int *                           4      12
   t4               temp    int                             4      28
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
   (3 temporaries no longer used after optimization not shown)

 Code: 63 instruction(s)

    111       t21 = n.1
    112       n.1 = n.1 int+ 1
    113       n1 = t21
    114       t22 = n.1
    115       n.1 = n.1 int+ 1
    116       n2 = t22
    117       t23 = n.1
    118       n.1 = n.1 int+ 1
    119       n3 = t23
    120       param "%d %d %d\n"
    121       param t21
    122       param t22
    123       param t23
    124       call printf, 4
    125       param 4
    126       t4 = call depth(int), 1
    127       param "%d\n"
    128       param t4
    129       call printf, 2
    130       t5 = table[0]
    131       t6 = table[4]
    132       t7 = table[8]
    133       t8 = table[20]
    134       param "%d %d %d %d\n"
    135       param t5
    136       param t6
    137       param t7
    138       param t8
    139       call printf, 5
    140       t9 = origin[0]
    141       t10 = origin[4]
    142       t11 = pts[8]
    143       t12 = pts[12]
    144       t13 = pts[16]
    145       param "%d %d %d %d %d\n"
    146       param t9
    147       param t10
    148       param t11
    149       param t12
    150       param t13
    151       call printf, 6
    152       t14 = names[0]
    153       t15 = names[4]
    154       t17 = names[8]
    155       if t17 ptr== 0 goto L3
    156       t16 = 0
    157       goto L4
    158  L3:  t16 = 1
    159  L4:  param "%s %s %d\n"
    160       param t14
    161       param t15
    162       param t16
    163       call printf, 4
    164       t18 = &total
    165       p = t18
    166       *t18 = 42
    167       t19 = table[0]
    168       t20 = total int+ t19
    169       total = t20
    170       param "%d\n"
    171       param t20
    172       call printf, 2
    173       return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

100 101 102
5
5 6 0 0
3 0 3 0 0
zero one 1
47

   exit code 0, 90 instructions executed
