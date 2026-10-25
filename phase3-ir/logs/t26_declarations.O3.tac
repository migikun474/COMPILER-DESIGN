============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t26_declarations.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 198 -> 184 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          198 -> 184   (7% fewer)

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
   instructions moved out of loops         0

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

 Code: 174 instruction(s)

    110        r[0] = 4
    111        r[4] = 9
    112        r[8] = 2
    113        r[12] = 4
    114        t67 = &r
    115        t68 = 0
    116        t69 = 0
    117  L3:   if t69 int>= 4 goto L4
    118        t70 = t69 int<< 2
    119        t71 = t67 ptr+ t70
    120        t72 = *t71
    121        t68 = t68 int+ t72
    122        t69 = t69 int+ 1
    123        goto L3
    124  L4:   t73 = &primes
    125        t74 = 0
    126        t75 = 0
    127  L5:   if t75 int>= 4 goto L6
    128        t76 = t75 int<< 2
    129        t77 = t73 ptr+ t76
    130        t78 = *t77
    131        t74 = t74 int+ t78
    132        t75 = t75 int+ 1
    133        goto L5
    134  L6:   t7 = t68 int+ t74
    135        if t7 int<= 100 goto L7
    136        t11 = t7
    137        goto L8
    138  L7:   t11 = 100
    139  L8:   param "%d %d %d\n"
    140        param t7
    141        param 9
    142        param t11
    143        call printf, 4
    144        param "%d %d %d %d\n"
    145        param 24
    146        param 80
    147        param 32
    148        param 16
    149        call printf, 5
    150        param "%d %d %d\n"
    151        param 24
    152        param 2
    153        param 3
    154        call printf, 4
    155        box[0] = 97
    156        box[8] = 1.5
    157        box[16] = 2
    158        box[24] = 98
    159        box[32] = 2.5
    160        box[40] = 4
    161        box[48] = 99
    162        box[56] = 0.0
    163        box[64] = 8
    164        box[72] = 0
    165        t13 = box[16]
    166        t14 = shorttoint t13
    167        t15 = box[40]
    168        t16 = shorttoint t15
    169        t17 = t14 int+ t16
    170        t18 = box[64]
    171        t19 = shorttoint t18
    172        t20 = t17 int+ t19
    173        box[72] = t20
    174        t21 = &box
    175        t22 = t21 ptr+ 48
    176        t23 = box[32]
    177        t24 = t23 double* 2.0
    178        t25 = t22 ptr+ 8
    179        *t25 = t24
    180        t26 = box[72]
    181        t29 = box[48]
    182        t30 = chartoint t29
    183        t31 = stock[8]
    184        t32 = stock[16]
    185        t33 = shorttodouble t32
    186        t34 = t31 double* t33
    187        param "%d %.1f %c %.1f\n"
    188        param t26
    189        param t24
    190        param t30
    191        param t34
    192        call printf, 5
    193        m[0] = 120
    194        m[4] = 1
    195        m[8] = 121
    196        m[10] = 2
    197        m[16] = 3.5
    198        m[24] = 122
    199        copy = m
    200        copy[4] = 100
    201        t36 = m[0]
    202        t37 = chartoint t36
    203        t38 = m[4]
    204        t39 = m[8]
    205        t40 = chartoint t39
    206        t41 = m[10]
    207        t42 = shorttoint t41
    208        t43 = m[16]
    209        t44 = m[24]
    210        t45 = chartoint t44
    211        param "%c %d %c %d %.1f %c %d\n"
    212        param t37
    213        param t38
    214        param t40
    215        param t42
    216        param t43
    217        param t45
    218        param 100
    219        call printf, 8
    220        t47 = &letters
    221        t48 = table[0]
    222        t49 = table[8]
    223        t50 = table[16]
    224        t51 = matrix[20]
    225        t52 = matrix[0]
    226        t53 = t51 int- t52
    227        param "%s %.1f %.1f %.1f %d\n"
    228        param t47
    229        param t48
    230        param t49
    231        param t50
    232        param t53
    233        call printf, 6
    234        grid[0] = 1
    235        grid[4] = 0
    236        grid[8] = 0
    237        grid[12] = 0
    238        grid[16] = 0
    239        grid[20] = 2
    240        grid[24] = 0
    241        grid[28] = 0
    242        grid[32] = 0
    243        grid[36] = 0
    244        grid[40] = 3
    245        grid[44] = 0
    246        trace = 0
    247        i = 0
    248  L9:   if i int>= 3 goto L10
    249        t54 = i int<< 2                     (n2 = 4)
    250        t55 = t54 int+ i
    251        t56 = t55 int<< 2                   (w = 4)
    252        t57 = grid[t56]
    253        trace = trace int+ t57
    254        i = i int+ 1
    255        goto L9
    256  L10:  words[0] = "one"
    257        words[4] = "two"
    258        words[8] = "three"
    259        rows[0] = 97
    260        rows[1] = 98
    261        rows[2] = 0
    262        rows[3] = 0
    263        rows[4] = 0
    264        rows[5] = 0
    265        rows[6] = 99
    266        rows[7] = 100
    267        rows[8] = 101
    268        rows[9] = 0
    269        rows[10] = 0
    270        rows[11] = 0
    271        t60 = words[8]
    272        t61 = rows[8]
    273        t62 = chartoint t61
    274        t63 = &rows
    275        param "%d %s %c %s %d\n"
    276        param trace
    277        param t60
    278        param t62
    279        param t63
    280        param 3
    281        call printf, 6
    282        t66 = 10 int+ kept.17
    283        return t66


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
