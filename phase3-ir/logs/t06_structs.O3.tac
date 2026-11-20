============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 182 -> 186 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          182 -> 186   (-2% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                   6
   copies / constants forwarded           23
   temporaries merged away                 5
   dead instructions removed              17
   jumps removed or redirected             2
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2
   calls inlined                           7
   tail calls turned into jumps            0
   common subexpressions across blocks      0

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   origin           struct Point                    8  { +0: 3, +4: 4 }

 As three address code (initial values, in place before main runs):

    origin[0] = 3
    origin[4] = 4

============================================================================
 FUNCTION make(int, int)        (link name _Z4makeii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 0 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                param   int                             4       0
   y                param   int                             4       4
   p                local   struct Point                    8       8

 Code: 3 instruction(s)

    100     p[0] = x
    101     p[4] = y
    102     return p

============================================================================
 FUNCTION area(struct Rect)        (link name _Z4area4Rect)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   struct Rect                    20       0
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48
   (1 temporary no longer used after optimization not shown)

 Code: 9 instruction(s)

    103     t1 = r[8]
    104     t2 = r[0]
    105     t3 = t1 int- t2
    106     r[8] = t3
    107     t5 = r[12]
    108     t6 = r[4]
    109     t7 = t5 int- t6
    110     t8 = t3 int* t7
    111     return t8

============================================================================
 FUNCTION move(struct Point *, int)        (link name _Z4moveP5Pointi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Point *                  4       0
   dx               param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12

 Code: 4 instruction(s)

    112     t1 = *p
    113     t2 = t1 int+ dx
    114     *p = t2
    115     return

============================================================================
 FUNCTION add(Complex, Complex)        (link name _Z3add7ComplexS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 6 temporaries, frame 96 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   Complex                        16       0
   b                param   Complex                        16      16
   c                local   Complex                        16      32
   t1               temp    double                          8      48
   t2               temp    double                          8      56
   t3               temp    double                          8      64
   t4               temp    double                          8      72
   t5               temp    double                          8      80
   t6               temp    double                          8      88

 Code: 9 instruction(s)

    116     t1 = a[0]
    117     t2 = b[0]
    118     t3 = t1 double+ t2
    119     c[0] = t3
    120     t4 = a[8]
    121     t5 = b[8]
    122     t6 = t4 double+ t5
    123     c[8] = t6
    124     return c

============================================================================
 FUNCTION length(struct Node *)        (link name _Z6lengthP4Node)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   head             param   struct Node *                   4       0
   n                local   int                             4       4
   t2               temp    struct Node *                   4      12
   (2 temporaries no longer used after optimization not shown)

 Code: 7 instruction(s)

    125       n = 0
    126  L1:  if head ptr== 0 goto L2
    127       n = n int+ 1
    128       t2 = head ptr+ 4
    129       head = *t2
    130       goto L1
    131  L2:  return n

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 14 parameter(s)/local(s), 71 temporaries, frame 660 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   struct Rect                    20       0
   copy             local   struct Rect                    20      20
   pts              local   struct Point[3]                24      40
   i                local   int                             4      64
   pp               local   struct Point *                  4      68
   rp               local   struct Rect *                   4      72
   a                local   Complex                        16      80
   b                local   Complex                        16      96
   c                local   Complex                        16     112
   n1               local   struct Node                     8     128
   n2               local   struct Node                     8     136
   n3               local   struct Node                     8     144
   k                local   struct Packet                  16     152
   zero             local   struct Point                    8     168
   t1               temp    int                             4     176
   t4               temp    char                            1     188
   t5               temp    int                             4     192
   t6               temp    int                             4     196
   t7               temp    int                             4     200
   t8               temp    int                             4     204
   t9               temp    int                             4     208
   t10              temp    int                             4     212
   t11              temp    int                             4     216
   t12              temp    struct Point                    8     220
   t14              temp    struct Point *                  4     232
   t15              temp    struct Point *                  4     236
   t17              temp    struct Point *                  4     244
   t18              temp    struct Point *                  4     248
   t19              temp    int                             4     252
   t20              temp    int                             4     256
   t22              temp    int                             4     264
   t23              temp    int                             4     268
   t24              temp    int                             4     272
   t25              temp    struct Point                    8     276
   t26              temp    int                             4     284
   t27              temp    struct Point *                  4     288
   t28              temp    struct Point *                  4     292
   t29              temp    struct Point *                  4     296
   t30              temp    int                             4     300
   t31              temp    int                             4     304
   t33              temp    struct Point                    8     312
   t34              temp    int                             4     320
   t35              temp    int                             4     324
   t36              temp    struct Rect *                   4     328
   t37              temp    int                             4     332
   t39              temp    double                          8     352
   t40              temp    double                          8     360
   t41              temp    struct Node *                   4     368
   t42              temp    struct Node *                   4     372
   t45              temp    struct Node *                   4     384
   t46              temp    struct Node *                   4     388
   t47              temp    struct Node *                   4     392
   t48              temp    int                             4     396
   t49              temp    int                             4     400
   t50              temp    int                             4     404
   t53              temp    short                           2     416
   t54              temp    int                             4     420
   t55              temp    int                             4     424
   t56              temp    int                             4     428
   t57              temp    int                             4     432
   t58              temp    struct Rect                    20     436
   t59              temp    int                             4     456
   t60              temp    int                             4     460
   t61              temp    int                             4     464
   t62              temp    int                             4     468
   t63              temp    int                             4     472
   t64              temp    int                             4     476
   t65              temp    int                             4     480
   t68              temp    struct Point                    8     492
   t71              temp    int                             4     508
   t72              temp    int                             4     512
   t75              temp    struct Point                    8     524
   t78              temp    struct Point                    8     540
   t79              temp    Complex                        16     552
   t80              temp    Complex                        16     568
   t81              temp    double                          8     584
   t82              temp    double                          8     592
   t83              temp    double                          8     600
   t84              temp    Complex                        16     608
   t85              temp    double                          8     624
   t86              temp    double                          8     632
   t87              temp    double                          8     640
   t88              temp    struct Node *                   4     648
   t89              temp    int                             4     652
   t90              temp    struct Node *                   4     656
   (19 temporaries no longer used after optimization not shown)

 Code: 154 instruction(s)

    132       r[0] = 1
    133       r[4] = 2
    134       r[8] = 5
    135       r[12] = 8
    136       r[16] = 114
    137       copy = r
    138       copy[0] = 100
    139       t1 = r[0]
    140       t58 = r
    141       t59 = t58[8]
    142       t60 = t58[0]
    143       t61 = t59 int- t60
    144       t58[8] = t61
    145       t62 = t58[12]
    146       t63 = t58[4]
    147       t64 = t62 int- t63
    148       t65 = t61 int* t64
    149       t4 = r[16]
    150       t5 = chartoint t4
    151       param "%d %d %d %c\n"
    152       param t1
    153       param 100
    154       param t65
    155       param t5
    156       call printf, 5
    157       t6 = r[8]
    158       t7 = origin[0]
    159       t8 = origin[4]
    160       t9 = t7 int* t8
    161       param "%d %d\n"
    162       param t6
    163       param t9
    164       call printf, 3
    165       i = 0
    166  L3:  if i int>= 3 goto L4
    167       t10 = i int<< 3                     (w = 8)
    168       t11 = i int* i
    169       t68[0] = i
    170       t68[4] = t11
    171       t12 = t68
    172       pts[t10] = t12
    173       i = i int+ 1
    174       goto L3
    175  L4:  t14 = &pts
    176       t15 = t14 ptr+ 8
    177       t71 = *t15
    178       t72 = t71 int+ 10
    179       *t15 = t72
    180       t17 = t14 ptr+ 16
    181       t18 = t17 ptr+ 4
    182       t19 = *t18
    183       t20 = t19 int+ 1
    184       *t18 = t20
    185       t22 = pts[8]
    186       t23 = pts[12]
    187       t24 = pts[20]
    188       t75[0] = 3
    189       t75[4] = 4
    190       t25 = t75
    191       t26 = t25[4]
    192       param "%d %d %d %d\n"
    193       param t22
    194       param t23
    195       param t24
    196       param t26
    197       call printf, 5
    198       t27 = &r
    199       t28 = t27 ptr+ 8
    200       t29 = t28 ptr+ 4
    201       t30 = *t29
    202       t31 = t30 int+ 1
    203       *t28 = t31
    204       t78[0] = 7
    205       t78[4] = 7
    206       t33 = t78
    207       *t27 = t33
    208       t34 = r[8]
    209       t35 = *t27
    210       t36 = t27 ptr+ 12
    211       t37 = *t36
    212       param "%d %d %d\n"
    213       param t34
    214       param t35
    215       param t37
    216       call printf, 4
    217       a[0] = 1.5
    218       a[8] = 2.0
    219       b[0] = 1.0
    220       b[8] = 0.5
    221       t79 = a
    222       t80 = b
    223       t81 = t79[0]
    224       t82 = t80[0]
    225       t83 = t81 double+ t82
    226       t84[0] = t83
    227       t85 = t79[8]
    228       t86 = t80[8]
    229       t87 = t85 double+ t86
    230       t84[8] = t87
    231       c = t84
    232       t39 = c[0]
    233       t40 = c[8]
    234       param "%.1f %.1f\n"
    235       param t39
    236       param t40
    237       call printf, 3
    238       n1[0] = 1
    239       t41 = &n2
    240       n1[4] = t41
    241       n2[0] = 2
    242       t42 = &n3
    243       n2[4] = t42
    244       n3[0] = 3
    245       n3[4] = 0
    246       t88 = &n1
    247       t89 = 0
    248  L5:  if t88 ptr== 0 goto L6
    249       t89 = t89 int+ 1
    250       t90 = t88 ptr+ 4
    251       t88 = *t90
    252       goto L5
    253  L6:  t45 = n1[4]
    254       t46 = t45 ptr+ 4
    255       t47 = *t46
    256       t48 = *t47
    257       param "%d %d\n"
    258       param t89
    259       param t48
    260       call printf, 3
    261       k[0] = 1
    262       k[4] = 16909060
    263       k[8] = 0
    264       k[9] = 0
    265       k[10] = 0
    266       k[11] = 0
    267       k[12] = 9
    268       k[9] = 120
    269       t49 = k[0]
    270       t50 = k[4]
    271       t53 = k[12]
    272       t54 = shorttoint t53
    273       param "%d %d %c %d %d\n"
    274       param t49
    275       param t50
    276       param 120
    277       param t54
    278       param 16
    279       call printf, 6
    280       zero[0] = 0
    281       zero[4] = 0
    282       t55 = zero[0]
    283       t56 = pts[16]
    284       t57 = t55 int+ t56
    285       return t57


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Point              struct_tag    struct Point               -           4    -    0  size 8
   Rect               struct_tag    struct Rect                -           5    -    0  size 20
   Node               struct_tag    struct Node                -           6    -    0  size 8
   (unnamed at 7:9)   struct_tag    struct (unnamed at 7:9)    -           7    -    0  size 16
   Complex            typedef       Complex                    -           7    -    0  
   Packet             struct_tag    struct Packet              -           8    -    0  size 16
   (unnamed at 10:5)  struct_tag    struct (unnamed at 10:5)   -          10    -    0  size 8
   make               function      struct Point (int, int)    -          14    -    3  _Z4makeii; defined
   area               function      int (struct Rect)          -          19    -    1  _Z4area4Rect; defined
   move               function      void (struct Point *, int) -          24    -    1  _Z4moveP5Pointi; defined
   add                function      Complex (Complex, Complex) -          26    -    1  _Z3add7ComplexS_; defined
   length             function      int (struct Node *)        -          33    -    1  _Z6lengthP4Node; defined
   origin             variable      struct Point               global     39    8    2  
   main               function      int (void)                 -          41    -    0  defined

 scope: global > struct Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      4    4   16  Point::x; public, offset 0
   y                  field         int                        member      4    4    9  Point::y; public, offset 4

 scope: global > struct Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   low                field         struct Point               member      5    8    7  Rect::low; public, offset 0
   high               field         struct Point               member      5    8    8  Rect::high; public, offset 8
   tag                field         char                       member      5    1    1  Rect::tag; public, offset 16

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   value              field         int                        member      6    4    4  Node::value; public, offset 0
   next               field         struct Node *              member      6    4    6  Node::next; public, offset 4

 scope: global > struct (unnamed at 7:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   re                 field         double                     member      7    8    4  (unnamed at 7:9)::re; public, offset 0
   im                 field         double                     member      7    8    4  (unnamed at 7:9)::im; public, offset 8

 scope: global > struct Packet
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               field         int                        member      9    4    1  Packet::kind; public, offset 0
   (unnamed)          field         struct (unnamed at 10:5)   member     10    8    0  Packet::(unnamed at 10:5); public, offset 4
   tail               field         short                      member     11    2    1  Packet::tail; public, offset 12

 scope: global > struct Packet > struct (unnamed at 10:5)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   word               field         int                        member     10    4    0  (unnamed at 10:5)::word; public, offset 0
   bytes              field         char[4]                    member     10    4    0  (unnamed at 10:5)::bytes; public, offset 4

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      14    4    1  x.1
   y                  parameter     int                        param      14    4    1  y.2
   p                  variable      struct Point               local      15    8    1  p.3

 scope: global > area()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     struct Rect                param      19   20    6  r.4

 scope: global > move()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Point *             param      24    4    1  p.5
   dx                 parameter     int                        param      24    4    1  dx.6

 scope: global > add()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     Complex                    param      26   16    2  a.7
   b                  parameter     Complex                    param      26   16    2  b.8
   c                  variable      Complex                    local      27   16    3  c.9

 scope: global > length()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param      33    4    3  head.10
   n                  variable      int                        local      34    4    2  n.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      struct Rect                local      42   20    8  r.12
   copy               variable      struct Rect                local      43   20    3  copy.13
   pts                variable      struct Point[3]            local      49   24    7  pts.14
   pp                 variable      struct Point *             local      55    4    2  pp.16
   rp                 variable      struct Rect *              local      57    4    3  rp.17
   a                  variable      Complex                    local      61   16    1  a.18
   b                  variable      Complex                    local      61   16    1  b.19
   c                  variable      Complex                    local      62   16    2  c.20
   n1                 variable      struct Node                local      65    8    4  n1.21
   n2                 variable      struct Node                local      65    8    3  n2.22
   n3                 variable      struct Node                local      65    8    3  n3.23
   k                  variable      struct Packet              local      71   16    5  k.24
   zero               variable      struct Point               local      74    8    1  zero.25

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      50    4    6  i.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
struct Rect: size 20, align 4
    +0  struct Point low  [public]
    +8  struct Point high  [public]
    +16  char tag  [public]
struct Node: size 8, align 4
    +0  int value  [public]
    +4  struct Node * next  [public]
struct (unnamed at 7:9): size 16, align 8
    +0  double re  [public]
    +8  double im  [public]
struct Packet: size 16, align 4
    +0  int kind  [public]
    +4  struct (unnamed at 10:5)   [public]
    +12  short tail  [public]
    +4  int word  [public]  (from the unnamed member)
    +8  char[4] bytes  [public]  (from the unnamed member)
struct (unnamed at 10:5): size 8, align 4
    +0  int word  [public]
    +4  char[4] bytes  [public]
