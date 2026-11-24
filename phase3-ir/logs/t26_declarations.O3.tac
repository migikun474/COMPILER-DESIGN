============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t26_declarations.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 198 -> 193 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          198 -> 193   (2% fewer)

   constants folded                        8
   algebraic simplifications               3
   common subexpressions                   3
   copies / constants forwarded           17
   temporaries merged away                 6
   dead instructions removed              12
   jumps removed or redirected             4
   unreachable instructions removed        2
   propagated across blocks                4
   dead assignments removed                7
   calls inlined                           2
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          4
   unreachable functions removed           1

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
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 14 parameter(s)/local(s), 60 temporaries, frame 632 bytes

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
   t47              temp    char *                          4     492
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
   t63              temp    char *                          4     568
   t66              temp    int                             4     580
   t67              temp    const int *                     4     584
   t68              temp    int                             4     588
   t69              temp    int                             4     592
   t70              temp    int                             4     596
   t71              temp    const int *                     4     600
   t72              temp    int                             4     604
   t73              temp    const int *                     4     608
   t74              temp    int                             4     612
   t75              temp    int                             4     616
   t76              temp    int                             4     620
   t77              temp    const int *                     4     624
   t78              temp    int                             4     628
   (18 temporaries no longer used after optimization not shown)

 Code: 193 instruction(s)

    100       r[0] = 4
    101       r[4] = 9
    102       r[8] = 2
    103       r[12] = 4
    104       t67 = &r
    105       t68 = 0
    106       t69 = 0
    107  L1:  if t69 int>= 4 goto L2
    108       t70 = t69 int<< 2
    109       t71 = t67 ptr+ t70
    110       t72 = *t71
    111       t68 = t68 int+ t72
    112       t69 = t69 int+ 1
    113       if t69 int>= 4 goto L2
    114       t70 = t69 int<< 2
    115       t71 = t67 ptr+ t70
    116       t72 = *t71
    117       t68 = t68 int+ t72
    118       t69 = t69 int+ 1
    119       goto L1
    120  L2:  t73 = &primes
    121       t74 = 0
    122       t75 = 0
    123  L3:  if t75 int>= 4 goto L4
    124       t76 = t75 int<< 2
    125       t77 = t73 ptr+ t76
    126       t78 = *t77
    127       t74 = t74 int+ t78
    128       t75 = t75 int+ 1
    129       if t75 int>= 4 goto L4
    130       t76 = t75 int<< 2
    131       t77 = t73 ptr+ t76
    132       t78 = *t77
    133       t74 = t74 int+ t78
    134       t75 = t75 int+ 1
    135       goto L3
    136  L4:  t7 = t68 int+ t74
    137       if t7 int<= 100 goto L5
    138       t11 = t7
    139       goto L6
    140  L5:  t11 = 100
    141  L6:  param "%d %d %d\n"
    142       param t7
    143       param 9
    144       param t11
    145       call printf, 4
    146       param "%d %d %d %d\n"
    147       param 24
    148       param 80
    149       param 32
    150       param 16
    151       call printf, 5
    152       param "%d %d %d\n"
    153       param 24
    154       param 2
    155       param 3
    156       call printf, 4
    157       box[0] = 97
    158       box[8] = 1.5
    159       box[16] = 2
    160       box[24] = 98
    161       box[32] = 2.5
    162       box[40] = 4
    163       box[48] = 99
    164       box[56] = 0.0
    165       box[64] = 8
    166       box[72] = 0
    167       t13 = box[16]
    168       t14 = shorttoint t13
    169       t15 = box[40]
    170       t16 = shorttoint t15
    171       t17 = t14 int+ t16
    172       t18 = box[64]
    173       t19 = shorttoint t18
    174       t20 = t17 int+ t19
    175       box[72] = t20
    176       t21 = &box
    177       t22 = t21 ptr+ 48
    178       t23 = box[32]
    179       t24 = t23 double* 2.0
    180       t25 = t22 ptr+ 8
    181       *t25 = t24
    182       t26 = box[72]
    183       t29 = box[48]
    184       t30 = chartoint t29
    185       t31 = stock[8]
    186       t32 = stock[16]
    187       t33 = shorttodouble t32
    188       t34 = t31 double* t33
    189       param "%d %.1f %c %.1f\n"
    190       param t26
    191       param t24
    192       param t30
    193       param t34
    194       call printf, 5
    195       m[0] = 120
    196       m[4] = 1
    197       m[8] = 121
    198       m[10] = 2
    199       m[16] = 3.5
    200       m[24] = 122
    201       copy = m
    202       copy[4] = 100
    203       t36 = m[0]
    204       t37 = chartoint t36
    205       t38 = m[4]
    206       t39 = m[8]
    207       t40 = chartoint t39
    208       t41 = m[10]
    209       t42 = shorttoint t41
    210       t43 = m[16]
    211       t44 = m[24]
    212       t45 = chartoint t44
    213       param "%c %d %c %d %.1f %c %d\n"
    214       param t37
    215       param t38
    216       param t40
    217       param t42
    218       param t43
    219       param t45
    220       param 100
    221       call printf, 8
    222       t47 = &letters
    223       t48 = table[0]
    224       t49 = table[8]
    225       t50 = table[16]
    226       t51 = matrix[20]
    227       t52 = matrix[0]
    228       t53 = t51 int- t52
    229       param "%s %.1f %.1f %.1f %d\n"
    230       param t47
    231       param t48
    232       param t49
    233       param t50
    234       param t53
    235       call printf, 6
    236       grid[0] = 1
    237       grid[4] = 0
    238       grid[8] = 0
    239       grid[12] = 0
    240       grid[16] = 0
    241       grid[20] = 2
    242       grid[24] = 0
    243       grid[28] = 0
    244       grid[32] = 0
    245       grid[36] = 0
    246       grid[40] = 3
    247       grid[44] = 0
    248       trace = 0
    249       i = 0
    250  L7:  if i int>= 3 goto L8
    251       t54 = i int<< 2                     (n2 = 4)
    252       t55 = t54 int+ i
    253       t56 = t55 int<< 2                   (w = 4)
    254       t57 = grid[t56]
    255       trace = trace int+ t57
    256       i = i int+ 1
    257       if i int>= 3 goto L8
    258       t54 = i int<< 2                     (n2 = 4)
    259       t55 = t54 int+ i
    260       t56 = t55 int<< 2                   (w = 4)
    261       t57 = grid[t56]
    262       trace = trace int+ t57
    263       i = i int+ 1
    264       goto L7
    265  L8:  words[0] = "one"
    266       words[4] = "two"
    267       words[8] = "three"
    268       rows[0] = 97
    269       rows[1] = 98
    270       rows[2] = 0
    271       rows[3] = 0
    272       rows[4] = 0
    273       rows[5] = 0
    274       rows[6] = 99
    275       rows[7] = 100
    276       rows[8] = 101
    277       rows[9] = 0
    278       rows[10] = 0
    279       rows[11] = 0
    280       t60 = words[8]
    281       t61 = rows[8]
    282       t62 = chartoint t61
    283       t63 = &rows
    284       param "%d %s %c %s %d\n"
    285       param trace
    286       param t60
    287       param t62
    288       param t63
    289       param 3
    290       call printf, 6
    291       t66 = 10 int+ kept.17
    292       return t66


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Number             typedef       int                        -           5    -    0  
   Row                typedef       int[4]                     -           6    -    0  
   (unnamed at 7:9)   struct_tag    struct (unnamed at 7:9)    -           7    -    0  size 24
   Item               typedef       Item                       -           7    -    0  
   (unnamed at 8:9)   struct_tag    struct (unnamed at 8:9)    -           8    -    0  size 80
   Box                typedef       Box                        -           8    -    0  
   Mixed              struct_tag    struct Mixed               -           9    -    0  size 32
   primes             variable      const int[4]               global     11   16    1  
   matrix             variable      int[2][3]                  global     12   24    5  
   letters            variable      char[3]                    global     13    3    2  
   stock              variable      Item                       global     14   24    2  
   table              variable      double[3]                  global     15   24    3  
   sum                function      int (const int *)          -          17    -    2  _Z3sumPKi; defined
   main               function      int (void)                 -          19    -    0  defined

 scope: global > struct (unnamed at 7:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   tag                field         char                       member      7    1    1  (unnamed at 7:9)::tag; public, offset 0
   weight             field         double                     member      7    8    4  (unnamed at 7:9)::weight; public, offset 8
   count              field         short                      member      7    2    4  (unnamed at 7:9)::count; public, offset 16

 scope: global > struct (unnamed at 8:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   first              field         Item                       member      8   24    1  (unnamed at 8:9)::first; public, offset 0
   rest               field         Item[2]                    member      8   48    5  (unnamed at 8:9)::rest; public, offset 24
   total              field         int                        member      8    4    2  (unnamed at 8:9)::total; public, offset 72

 scope: global > struct Mixed
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         char                       member      9    1    1  Mixed::a; public, offset 0
   b                  field         int                        member      9    4    3  Mixed::b; public, offset 4
   c                  field         char                       member      9    1    1  Mixed::c; public, offset 8
   d                  field         short                      member      9    2    1  Mixed::d; public, offset 10
   e                  field         double                     member      9    8    1  Mixed::e; public, offset 16
   f                  field         char                       member      9    1    1  Mixed::f; public, offset 24

 scope: global > sum()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     const int *                param      17    4    1  r.1
   s                  variable      int                        local      17    4    2  s.2

 scope: global > sum() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      17    4    3  i.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      int[4]                     local      20   16    1  r.4
   n                  variable      int                        local      21    4    3  n.5
   box                variable      Box                        local      26   80    8  box.6
   it                 variable      Item *                     local      28    4    2  it.7
   m                  variable      struct Mixed               local      32   32    7  m.8
   copy               variable      struct Mixed               local      33   32    2  copy.9
   grid               variable      int[3][4]                  local      38   48    1  grid.10
   trace              variable      int                        local      39    4    2  trace.11
   words              variable      const char *[3]            local      41   12    3  words.13
   rows               variable      char[2][6]                 local      42   12    2  rows.14
   sensor             variable      int                        local      44    4    1  sensor.15
   fast               variable      int                        local      45    4    1  fast.16
   kept               variable      int                        static     46    4    1  kept.17; static
   deduced            variable      int                        local      47    4    1  deduced.18

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      40    4    4  i.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct (unnamed at 7:9): size 24, align 8
    +0  char tag  [public]
    +8  double weight  [public]
    +16  short count  [public]
struct (unnamed at 8:9): size 80, align 8
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
