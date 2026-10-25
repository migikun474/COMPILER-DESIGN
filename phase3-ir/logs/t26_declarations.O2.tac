============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t26_declarations.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 198 -> 170 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          198 -> 170   (14% fewer)

   constants folded                        8
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded           16
   temporaries merged away                 4
   dead instructions removed              11
   jumps removed or redirected             4
   unreachable instructions removed        2
   propagated across blocks                3
   dead assignments removed                6

----------------------------------------------------------------------------
 GLOBALS: 6 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   primes           const int[4]                   16  { +0: 2, +4: 3, +8: 5, +12: 7 }
   matrix           int[2][3]                      24  { +0: 1, +4: 2, +8: 3, +12: 4, +16: 5, +20: 6 }
   letters          char[3]                         3  { +0: 111, +1: 107, +2: 0 }
   stock            Item                           24  { +0: 115, +8: 2.5, +16: 3 }
   table            double[3]                      24  { +16: 9.5, +0: 1.5 }
   kept.17          int                             4  3

 As three address code (initial values, in place before main runs):

    primes[0] = 2
    primes[4] = 3
    primes[8] = 5
    primes[12] = 7
    matrix[0] = 1
    matrix[4] = 2
    matrix[8] = 3
    matrix[12] = 4
    matrix[16] = 5
    matrix[20] = 6
    letters[0] = 111
    letters[1] = 107
    letters[2] = 0
    stock[0] = 115
    stock[8] = 2.5
    stock[16] = 3
    table[16] = 9.5
    table[0] = 1.5
    kept.17 = 3

============================================================================
 FUNCTION sum(const int *)        (link name _Z3sumPKi)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   const int *                     4       0
   s                local   int                             4       4
   i                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    const int *                     4      16
   t3               temp    int                             4      20
   (2 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    100       s = 0
    101       i = 0
    102  L1:  if i int>= 4 goto L2
    103       t1 = i int<< 2
    104       t2 = r ptr+ t1
    105       t3 = *t2
    106       s = s int+ t3
    107       i = i int+ 1
    108       goto L1
    109  L2:  return s

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 14 parameter(s)/local(s), 52 temporaries, frame 584 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   int[4]                         16       0
   n                local   int                             4      16
   box              local   Box                            80      24
   it               local   Item *                          4     104
   m                local   struct Mixed                   32     112
   copy             local   struct Mixed                   32     144
   grid             local   int[3][4]                      48     176
   trace            local   int                             4     224
   i                local   int                             4     228
   words            local   const char *[3]                12     232
   rows             local   char[2][6]                     12     244
   sensor           local   int                             4     256
   fast             local   int                             4     260
   deduced          local   int                             4     264
   t3               temp    int (*)[4]                      4     276
   t4               temp    int                             4     280
   t5               temp    const int (*)[4]                4     284
   t6               temp    int                             4     288
   t7               temp    int                             4     292
   t11              temp    int                             4     308
   t13              temp    short                           2     316
   t14              temp    int                             4     320
   t15              temp    short                           2     324
   t16              temp    int                             4     328
   t17              temp    int                             4     332
   t18              temp    short                           2     336
   t19              temp    int                             4     340
   t20              temp    int                             4     344
   t21              temp    Item *                          4     348
   t22              temp    Item *                          4     352
   t23              temp    double                          8     360
   t24              temp    double                          8     368
   t25              temp    Item *                          4     376
   t26              temp    int                             4     380
   t29              temp    char                            1     400
   t30              temp    int                             4     404
   t31              temp    double                          8     408
   t32              temp    short                           2     416
   t33              temp    double                          8     424
   t34              temp    double                          8     432
   t36              temp    char                            1     444
   t37              temp    int                             4     448
   t38              temp    int                             4     452
   t39              temp    char                            1     456
   t40              temp    int                             4     460
   t41              temp    short                           2     464
   t42              temp    int                             4     468
   t43              temp    double                          8     472
   t44              temp    char                            1     480
   t45              temp    int                             4     484
   t47              temp    char (*)[3]                     4     492
   t48              temp    double                          8     496
   t49              temp    double                          8     504
   t50              temp    double                          8     512
   t51              temp    int                             4     520
   t52              temp    int                             4     524
   t53              temp    int                             4     528
   t54              temp    int                             4     532
   t55              temp    int                             4     536
   t56              temp    int                             4     540
   t57              temp    int                             4     544
   t60              temp    const char *                    4     556
   t61              temp    char                            1     560
   t62              temp    int                             4     564
   t63              temp    char (*)[6]                     4     568
   t66              temp    int                             4     580
   (14 temporaries no longer used after optimization not shown)

 Code: 160 instruction(s)

    110       r[0] = 4
    111       r[4] = 9
    112       r[8] = 2
    113       r[12] = 4
    114       t3 = &r
    115       param t3
    116       t4 = call sum(const int *), 1
    117       t5 = &primes
    118       param t5
    119       t6 = call sum(const int *), 1
    120       t7 = t4 int+ t6
    121       if t7 int<= 100 goto L3
    122       t11 = t7
    123       goto L4
    124  L3:  t11 = 100
    125  L4:  param "%d %d %d\n"
    126       param t7
    127       param 9
    128       param t11
    129       call printf, 4
    130       param "%d %d %d %d\n"
    131       param 24
    132       param 80
    133       param 32
    134       param 16
    135       call printf, 5
    136       param "%d %d %d\n"
    137       param 24
    138       param 2
    139       param 3
    140       call printf, 4
    141       box[0] = 97
    142       box[8] = 1.5
    143       box[16] = 2
    144       box[24] = 98
    145       box[32] = 2.5
    146       box[40] = 4
    147       box[48] = 99
    148       box[56] = 0.0
    149       box[64] = 8
    150       box[72] = 0
    151       t13 = box[16]
    152       t14 = shorttoint t13
    153       t15 = box[40]
    154       t16 = shorttoint t15
    155       t17 = t14 int+ t16
    156       t18 = box[64]
    157       t19 = shorttoint t18
    158       t20 = t17 int+ t19
    159       box[72] = t20
    160       t21 = &box
    161       t22 = t21 ptr+ 48
    162       t23 = box[32]
    163       t24 = t23 double* 2.0
    164       t25 = t22 ptr+ 8
    165       *t25 = t24
    166       t26 = box[72]
    167       t29 = box[48]
    168       t30 = chartoint t29
    169       t31 = stock[8]
    170       t32 = stock[16]
    171       t33 = shorttodouble t32
    172       t34 = t31 double* t33
    173       param "%d %.1f %c %.1f\n"
    174       param t26
    175       param t24
    176       param t30
    177       param t34
    178       call printf, 5
    179       m[0] = 120
    180       m[4] = 1
    181       m[8] = 121
    182       m[10] = 2
    183       m[16] = 3.5
    184       m[24] = 122
    185       copy = m
    186       copy[4] = 100
    187       t36 = m[0]
    188       t37 = chartoint t36
    189       t38 = m[4]
    190       t39 = m[8]
    191       t40 = chartoint t39
    192       t41 = m[10]
    193       t42 = shorttoint t41
    194       t43 = m[16]
    195       t44 = m[24]
    196       t45 = chartoint t44
    197       param "%c %d %c %d %.1f %c %d\n"
    198       param t37
    199       param t38
    200       param t40
    201       param t42
    202       param t43
    203       param t45
    204       param 100
    205       call printf, 8
    206       t47 = &letters
    207       t48 = table[0]
    208       t49 = table[8]
    209       t50 = table[16]
    210       t51 = matrix[20]
    211       t52 = matrix[0]
    212       t53 = t51 int- t52
    213       param "%s %.1f %.1f %.1f %d\n"
    214       param t47
    215       param t48
    216       param t49
    217       param t50
    218       param t53
    219       call printf, 6
    220       grid[0] = 1
    221       grid[4] = 0
    222       grid[8] = 0
    223       grid[12] = 0
    224       grid[16] = 0
    225       grid[20] = 2
    226       grid[24] = 0
    227       grid[28] = 0
    228       grid[32] = 0
    229       grid[36] = 0
    230       grid[40] = 3
    231       grid[44] = 0
    232       trace = 0
    233       i = 0
    234  L5:  if i int>= 3 goto L6
    235       t54 = i int<< 2                     (n2 = 4)
    236       t55 = t54 int+ i
    237       t56 = t55 int<< 2                   (w = 4)
    238       t57 = grid[t56]
    239       trace = trace int+ t57
    240       i = i int+ 1
    241       goto L5
    242  L6:  words[0] = "one"
    243       words[4] = "two"
    244       words[8] = "three"
    245       rows[0] = 97
    246       rows[1] = 98
    247       rows[2] = 0
    248       rows[3] = 0
    249       rows[4] = 0
    250       rows[5] = 0
    251       rows[6] = 99
    252       rows[7] = 100
    253       rows[8] = 101
    254       rows[9] = 0
    255       rows[10] = 0
    256       rows[11] = 0
    257       t60 = words[8]
    258       t61 = rows[8]
    259       t62 = chartoint t61
    260       t63 = &rows
    261       param "%d %s %c %s %d\n"
    262       param trace
    263       param t60
    264       param t62
    265       param t63
    266       param 3
    267       call printf, 6
    268       t66 = 10 int+ kept.17
    269       return t66


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Number             typedef       int                        -          15    -    0  
   Row                typedef       int[4]                     -          16    -    0  
   (unnamed at 17:9)  struct_tag    struct (unnamed at 17:9)   -          17    -    0  size 24
   Item               typedef       Item                       -          17    -    0  
   (unnamed at 18:9)  struct_tag    struct (unnamed at 18:9)   -          18    -    0  size 80
   Box                typedef       Box                        -          18    -    0  
   Mixed              struct_tag    struct Mixed               -          19    -    0  size 32
   primes             variable      const int[4]               global     21   16    1  
   matrix             variable      int[2][3]                  global     22   24    5  
   letters            variable      char[3]                    global     23    3    2  
   stock              variable      Item                       global     24   24    2  
   table              variable      double[3]                  global     25   24    3  
   sum                function      int (const int *)          -          27    -    2  _Z3sumPKi; defined
   main               function      int (void)                 -          29    -    0  defined

 scope: global > struct (unnamed at 17:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   tag                field         char                       member     17    1    1  (unnamed at 17:9)::tag; public, offset 0
   weight             field         double                     member     17    8    4  (unnamed at 17:9)::weight; public, offset 8
   count              field         short                      member     17    2    4  (unnamed at 17:9)::count; public, offset 16

 scope: global > struct (unnamed at 18:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   first              field         Item                       member     18   24    1  (unnamed at 18:9)::first; public, offset 0
   rest               field         Item[2]                    member     18   48    5  (unnamed at 18:9)::rest; public, offset 24
   total              field         int                        member     18    4    2  (unnamed at 18:9)::total; public, offset 72

 scope: global > struct Mixed
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         char                       member     19    1    1  Mixed::a; public, offset 0
   b                  field         int                        member     19    4    3  Mixed::b; public, offset 4
   c                  field         char                       member     19    1    1  Mixed::c; public, offset 8
   d                  field         short                      member     19    2    1  Mixed::d; public, offset 10
   e                  field         double                     member     19    8    1  Mixed::e; public, offset 16
   f                  field         char                       member     19    1    1  Mixed::f; public, offset 24

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     const int *                param      27    4    1  r.1
   s                  variable      int                        local      27    4    2  s.2

 scope: global > sum() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      27    4    3  i.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      int[4]                     local      30   16    1  r.4
   n                  variable      int                        local      31    4    3  n.5
   box                variable      Box                        local      36   80    8  box.6
   it                 variable      Item *                     local      38    4    2  it.7
   m                  variable      struct Mixed               local      42   32    7  m.8
   copy               variable      struct Mixed               local      43   32    2  copy.9
   grid               variable      int[3][4]                  local      48   48    1  grid.10
   trace              variable      int                        local      49    4    2  trace.11
   words              variable      const char *[3]            local      51   12    3  words.13
   rows               variable      char[2][6]                 local      52   12    2  rows.14
   sensor             variable      int                        local      54    4    1  sensor.15
   fast               variable      int                        local      55    4    1  fast.16
   kept               variable      int                        static     56    4    1  kept.17; static
   deduced            variable      int                        local      57    4    1  deduced.18

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      50    4    4  i.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct (unnamed at 17:9): size 24, align 8
    +0  char tag  [public]
    +8  double weight  [public]
    +16  short count  [public]
struct (unnamed at 18:9): size 80, align 8
    +0  Item first  [public]
    +24  Item[2] rest  [public]
    +72  int total  [public]
struct Mixed: size 32, align 8
    +0  char a  [public]
    +4  int b  [public]
    +8  char c  [public]
    +10  short d  [public]
    +16  double e  [public]
    +24  char f  [public]
