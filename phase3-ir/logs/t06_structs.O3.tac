============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 182 -> 166 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          182 -> 166   (8% fewer)

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
   loops unrolled                          3
   unreachable functions removed           5

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

 Code: 166 instruction(s)

    100       r[0] = 1
    101       r[4] = 2
    102       r[8] = 5
    103       r[12] = 8
    104       r[16] = 114
    105       copy = r
    106       copy[0] = 100
    107       t1 = r[0]
    108       t58 = r
    109       t59 = t58[8]
    110       t60 = t58[0]
    111       t61 = t59 int- t60
    112       t58[8] = t61
    113       t62 = t58[12]
    114       t63 = t58[4]
    115       t64 = t62 int- t63
    116       t65 = t61 int* t64
    117       t4 = r[16]
    118       t5 = chartoint t4
    119       param "%d %d %d %c\n"
    120       param t1
    121       param 100
    122       param t65
    123       param t5
    124       call printf, 5
    125       t6 = r[8]
    126       t7 = origin[0]
    127       t8 = origin[4]
    128       t9 = t7 int* t8
    129       param "%d %d\n"
    130       param t6
    131       param t9
    132       call printf, 3
    133       i = 0
    134  L1:  if i int>= 3 goto L2
    135       t10 = i int<< 3                     (w = 8)
    136       t11 = i int* i
    137       t68[0] = i
    138       t68[4] = t11
    139       t12 = t68
    140       pts[t10] = t12
    141       i = i int+ 1
    142       if i int>= 3 goto L2
    143       t10 = i int<< 3                     (w = 8)
    144       t11 = i int* i
    145       t68[0] = i
    146       t68[4] = t11
    147       t12 = t68
    148       pts[t10] = t12
    149       i = i int+ 1
    150       goto L1
    151  L2:  t14 = &pts
    152       t15 = t14 ptr+ 8
    153       t71 = *t15
    154       t72 = t71 int+ 10
    155       *t15 = t72
    156       t17 = t14 ptr+ 16
    157       t18 = t17 ptr+ 4
    158       t19 = *t18
    159       t20 = t19 int+ 1
    160       *t18 = t20
    161       t22 = pts[8]
    162       t23 = pts[12]
    163       t24 = pts[20]
    164       t75[0] = 3
    165       t75[4] = 4
    166       t25 = t75
    167       t26 = t25[4]
    168       param "%d %d %d %d\n"
    169       param t22
    170       param t23
    171       param t24
    172       param t26
    173       call printf, 5
    174       t27 = &r
    175       t28 = t27 ptr+ 8
    176       t29 = t28 ptr+ 4
    177       t30 = *t29
    178       t31 = t30 int+ 1
    179       *t28 = t31
    180       t78[0] = 7
    181       t78[4] = 7
    182       t33 = t78
    183       *t27 = t33
    184       t34 = r[8]
    185       t35 = *t27
    186       t36 = t27 ptr+ 12
    187       t37 = *t36
    188       param "%d %d %d\n"
    189       param t34
    190       param t35
    191       param t37
    192       call printf, 4
    193       a[0] = 1.5
    194       a[8] = 2.0
    195       b[0] = 1.0
    196       b[8] = 0.5
    197       t79 = a
    198       t80 = b
    199       t81 = t79[0]
    200       t82 = t80[0]
    201       t83 = t81 double+ t82
    202       t84[0] = t83
    203       t85 = t79[8]
    204       t86 = t80[8]
    205       t87 = t85 double+ t86
    206       t84[8] = t87
    207       c = t84
    208       t39 = c[0]
    209       t40 = c[8]
    210       param "%.1f %.1f\n"
    211       param t39
    212       param t40
    213       call printf, 3
    214       n1[0] = 1
    215       t41 = &n2
    216       n1[4] = t41
    217       n2[0] = 2
    218       t42 = &n3
    219       n2[4] = t42
    220       n3[0] = 3
    221       n3[4] = 0
    222       t88 = &n1
    223       t89 = 0
    224  L3:  if t88 ptr== 0 goto L4
    225       t89 = t89 int+ 1
    226       t90 = t88 ptr+ 4
    227       t88 = *t90
    228       if t88 ptr== 0 goto L4
    229       t89 = t89 int+ 1
    230       t90 = t88 ptr+ 4
    231       t88 = *t90
    232       goto L3
    233  L4:  t45 = n1[4]
    234       t46 = t45 ptr+ 4
    235       t47 = *t46
    236       t48 = *t47
    237       param "%d %d\n"
    238       param t89
    239       param t48
    240       call printf, 3
    241       k[0] = 1
    242       k[4] = 16909060
    243       k[8] = 0
    244       k[9] = 0
    245       k[10] = 0
    246       k[11] = 0
    247       k[12] = 9
    248       k[9] = 120
    249       t49 = k[0]
    250       t50 = k[4]
    251       t53 = k[12]
    252       t54 = shorttoint t53
    253       param "%d %d %c %d %d\n"
    254       param t49
    255       param t50
    256       param 120
    257       param t54
    258       param 16
    259       call printf, 6
    260       zero[0] = 0
    261       zero[4] = 0
    262       t55 = zero[0]
    263       t56 = pts[16]
    264       t57 = t55 int+ t56
    265       return t57


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
