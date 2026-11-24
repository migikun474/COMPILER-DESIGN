============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t42_statics_globals.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 75 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 0 parameter(s)/local(s), 2 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0
   t2               temp    int                             4       4

 Code: 4 instruction(s)

    100     t1 = n.1
    101     t2 = n.1 int+ 1
    102     n.1 = t2
    103     return t1

============================================================================
 FUNCTION depth(int)        (link name _Z5depthi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   k                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16

 Code: 11 instruction(s)

    104       t1 = calls.3 int+ 1
    105       calls.3 = t1
    106       if k int== 0 goto L1
    107       goto L2
    108  L1:  t2 = calls.3
    109       goto L3
    110  L2:  t3 = k int- 1
    111       param t3
    112       t4 = call depth(int), 1
    113       t2 = t4
    114  L3:  return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 20 temporaries, frame 96 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n1               local   int                             4       0
   n2               local   int                             4       4
   n3               local   int                             4       8
   p                local   int *                           4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
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

 Code: 60 instruction(s)

    115       t1 = call next(), 0
    116       n1 = t1
    117       t2 = call next(), 0
    118       n2 = t2
    119       t3 = call next(), 0
    120       n3 = t3
    121       param "%d %d %d\n"
    122       param n1
    123       param n2
    124       param n3
    125       call printf, 4
    126       param 4
    127       t4 = call depth(int), 1
    128       param "%d\n"
    129       param t4
    130       call printf, 2
    131       t5 = table[0]
    132       t6 = table[4]
    133       t7 = table[8]
    134       t8 = table[20]
    135       param "%d %d %d %d\n"
    136       param t5
    137       param t6
    138       param t7
    139       param t8
    140       call printf, 5
    141       t9 = origin[0]
    142       t10 = origin[4]
    143       t11 = pts[8]
    144       t12 = pts[12]
    145       t13 = pts[16]
    146       param "%d %d %d %d %d\n"
    147       param t9
    148       param t10
    149       param t11
    150       param t12
    151       param t13
    152       call printf, 6
    153       t14 = names[0]
    154       t15 = names[4]
    155       t17 = names[8]
    156       if t17 ptr== 0 goto L4
    157       t16 = 0
    158       goto L5
    159  L4:  t16 = 1
    160  L5:  param "%s %s %d\n"
    161       param t14
    162       param t15
    163       param t16
    164       call printf, 4
    165       t18 = &total
    166       p = t18
    167       *p = 42
    168       t19 = table[0]
    169       t20 = total int+ t19
    170       total = t20
    171       param "%d\n"
    172       param total
    173       call printf, 2
    174       return 0


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
