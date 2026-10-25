============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : no optimization
   Result        : Three address code generated: 6 function(s), 187 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

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

 Symbol table: 1 parameter(s)/local(s), 8 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                param   struct Rect                    20       0
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48

 Code: 10 instruction(s)

    103     t1 = r[8]
    104     t2 = r[0]
    105     t3 = t1 int- t2
    106     r[8] = t3
    107     t4 = r[8]
    108     t5 = r[12]
    109     t6 = r[4]
    110     t7 = t5 int- t6
    111     t8 = t4 int* t7
    112     return t8

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

    113     t1 = *p
    114     t2 = t1 int+ dx
    115     *p = t2
    116     return

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

    117     t1 = a[0]
    118     t2 = b[0]
    119     t3 = t1 double+ t2
    120     c[0] = t3
    121     t4 = a[8]
    122     t5 = b[8]
    123     t6 = t4 double+ t5
    124     c[8] = t6
    125     return c

============================================================================
 FUNCTION length(struct Node *)        (link name _Z6lengthP4Node)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   head             param   struct Node *                   4       0
   n                local   int                             4       4
   t1               temp    int                             4       8
   t2               temp    struct Node *                   4      12
   t3               temp    struct Node *                   4      16

 Code: 10 instruction(s)

    126       n = 0
    127  L1:  if head ptr!= 0 goto L2
    128       goto L3
    129  L2:  t1 = n int+ 1
    130       n = t1
    131       t2 = head ptr+ 4
    132       t3 = *t2
    133       head = t3
    134       goto L1
    135  L3:  return n

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 14 parameter(s)/local(s), 62 temporaries, frame 460 bytes

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
   t2               temp    int                             4     180
   t3               temp    int                             4     184
   t4               temp    char                            1     188
   t5               temp    int                             4     192
   t6               temp    int                             4     196
   t7               temp    int                             4     200
   t8               temp    int                             4     204
   t9               temp    int                             4     208
   t10              temp    int                             4     212
   t11              temp    int                             4     216
   t12              temp    struct Point                    8     220
   t13              temp    struct Point *                  4     228
   t14              temp    int                             4     232
   t15              temp    struct Point *                  4     236
   t16              temp    struct Point *                  4     240
   t17              temp    struct Point *                  4     244
   t18              temp    struct Point *                  4     248
   t19              temp    struct Point *                  4     252
   t20              temp    int                             4     256
   t21              temp    int                             4     260
   t22              temp    struct Point *                  4     264
   t23              temp    int                             4     268
   t24              temp    int                             4     272
   t25              temp    int                             4     276
   t26              temp    struct Point                    8     280
   t27              temp    struct Point *                  4     288
   t28              temp    int                             4     292
   t29              temp    struct Point *                  4     296
   t30              temp    struct Point *                  4     300
   t31              temp    struct Point *                  4     304
   t32              temp    int                             4     308
   t33              temp    int                             4     312
   t34              temp    struct Rect *                   4     316
   t35              temp    struct Point                    8     320
   t36              temp    struct Point *                  4     328
   t37              temp    int                             4     332
   t38              temp    int                             4     336
   t39              temp    struct Rect *                   4     340
   t40              temp    int                             4     344
   t41              temp    Complex                        16     352
   t42              temp    Complex *                       4     368
   t43              temp    Complex *                       4     372
   t44              temp    double                          8     376
   t45              temp    double                          8     384
   t46              temp    struct Node *                   4     392
   t47              temp    struct Node *                   4     396
   t48              temp    struct Node *                   4     400
   t49              temp    int                             4     404
   t50              temp    struct Node *                   4     408
   t51              temp    struct Node *                   4     412
   t52              temp    struct Node *                   4     416
   t53              temp    int                             4     420
   t54              temp    int                             4     424
   t55              temp    int                             4     428
   t56              temp    char                            1     432
   t57              temp    int                             4     436
   t58              temp    short                           2     440
   t59              temp    int                             4     444
   t60              temp    int                             4     448
   t61              temp    int                             4     452
   t62              temp    int                             4     456

 Code: 151 instruction(s)

    136       r[0] = 1
    137       r[4] = 2
    138       r[8] = 5
    139       r[12] = 8
    140       r[16] = 114
    141       copy = r
    142       copy[0] = 100
    143       t1 = r[0]
    144       t2 = copy[0]
    145       param r
    146       t3 = call area(struct Rect), 1
    147       t4 = r[16]
    148       t5 = chartoint t4
    149       param "%d %d %d %c\n"
    150       param t1
    151       param t2
    152       param t3
    153       param t5
    154       call printf, 5
    155       t6 = r[8]
    156       t7 = origin[0]
    157       t8 = origin[4]
    158       t9 = t7 int* t8
    159       param "%d %d\n"
    160       param t6
    161       param t9
    162       call printf, 3
    163       i = 0
    164  L4:  if i int< 3 goto L5
    165       goto L6
    166  L5:  t10 = i int* 8                      (w = 8)
    167       t11 = i int* i
    168       param i
    169       param t11
    170       t12 = call make(int, int), 2
    171       t13 = &t12
    172       pts[t10] = t12
    173       t14 = i int+ 1
    174       i = t14
    175       goto L4
    176  L6:  t15 = &pts
    177       t16 = t15 ptr+ 8
    178       param t16
    179       param 10
    180       call move(struct Point *, int), 2
    181       t17 = &pts
    182       t18 = t17 ptr+ 16
    183       t19 = t18 ptr+ 4
    184       t20 = *t19
    185       t21 = t20 int+ 1
    186       t22 = t18 ptr+ 4
    187       *t22 = t21
    188       t23 = pts[8]
    189       t24 = pts[12]
    190       t25 = pts[20]
    191       param 3
    192       param 4
    193       t26 = call make(int, int), 2
    194       t27 = &t26
    195       t28 = t26[4]
    196       param "%d %d %d %d\n"
    197       param t23
    198       param t24
    199       param t25
    200       param t28
    201       call printf, 5
    202       t29 = &r
    203       t30 = t29 ptr+ 8
    204       pp = t30
    205       t31 = pp ptr+ 4
    206       t32 = *t31
    207       t33 = t32 int+ 1
    208       *pp = t33
    209       t34 = &r
    210       rp = t34
    211       param 7
    212       param 7
    213       t35 = call make(int, int), 2
    214       t36 = &t35
    215       *rp = t35
    216       t37 = r[8]
    217       t38 = *rp
    218       t39 = rp ptr+ 12
    219       t40 = *t39
    220       param "%d %d %d\n"
    221       param t37
    222       param t38
    223       param t40
    224       call printf, 4
    225       a[0] = 1.5
    226       a[8] = 2.0
    227       b[0] = 1.0
    228       b[8] = 0.5
    229       param a
    230       param b
    231       t41 = call add(Complex, Complex), 2
    232       t42 = &t41
    233       c = t41
    234       t43 = &c
    235       t44 = c[0]
    236       t45 = c[8]
    237       param "%.1f %.1f\n"
    238       param t44
    239       param t45
    240       call printf, 3
    241       n1[0] = 1
    242       t46 = &n2
    243       n1[4] = t46
    244       n2[0] = 2
    245       t47 = &n3
    246       n2[4] = t47
    247       n3[0] = 3
    248       n3[4] = 0
    249       t48 = &n1
    250       param t48
    251       t49 = call length(struct Node *), 1
    252       t50 = n1[4]
    253       t51 = t50 ptr+ 4
    254       t52 = *t51
    255       t53 = *t52
    256       param "%d %d\n"
    257       param t49
    258       param t53
    259       call printf, 3
    260       k[0] = 1
    261       k[4] = 16909060
    262       k[8] = 0
    263       k[9] = 0
    264       k[10] = 0
    265       k[11] = 0
    266       k[12] = 9
    267       k[9] = 120
    268       t54 = k[0]
    269       t55 = k[4]
    270       t56 = k[9]
    271       t57 = chartoint t56
    272       t58 = k[12]
    273       t59 = shorttoint t58
    274       param "%d %d %c %d %d\n"
    275       param t54
    276       param t55
    277       param t57
    278       param t59
    279       param 16
    280       call printf, 6
    281       zero[0] = 0
    282       zero[4] = 0
    283       t60 = zero[0]
    284       t61 = pts[16]
    285       t62 = t60 int+ t61
    286       return t62


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Point              struct_tag    struct Point               -           5    -    0  size 8
   Rect               struct_tag    struct Rect                -           6    -    0  size 20
   Node               struct_tag    struct Node                -           7    -    0  size 8
   (unnamed at 8:9)   struct_tag    struct (unnamed at 8:9)    -           8    -    0  size 16
   Complex            typedef       Complex                    -           8    -    0  
   Packet             struct_tag    struct Packet              -           9    -    0  size 16
   (unnamed at 11:5)  struct_tag    struct (unnamed at 11:5)   -          11    -    0  size 8
   make               function      struct Point (int, int)    -          15    -    3  _Z4makeii; defined
   area               function      int (struct Rect)          -          20    -    1  _Z4area4Rect; defined
   move               function      void (struct Point *, int) -          25    -    1  _Z4moveP5Pointi; defined
   add                function      Complex (Complex, Complex) -          27    -    1  _Z3add7ComplexS_; defined
   length             function      int (struct Node *)        -          34    -    1  _Z6lengthP4Node; defined
   origin             variable      struct Point               global     40    8    2  
   main               function      int (void)                 -          42    -    0  defined

 scope: global > struct Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      5    4   16  Point::x; public, offset 0
   y                  field         int                        member      5    4    9  Point::y; public, offset 4

 scope: global > struct Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   low                field         struct Point               member      6    8    7  Rect::low; public, offset 0
   high               field         struct Point               member      6    8    8  Rect::high; public, offset 8
   tag                field         char                       member      6    1    1  Rect::tag; public, offset 16

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   value              field         int                        member      7    4    4  Node::value; public, offset 0
   next               field         struct Node *              member      7    4    6  Node::next; public, offset 4

 scope: global > struct (unnamed at 8:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   re                 field         double                     member      8    8    4  (unnamed at 8:9)::re; public, offset 0
   im                 field         double                     member      8    8    4  (unnamed at 8:9)::im; public, offset 8

 scope: global > struct Packet
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   kind               field         int                        member     10    4    1  Packet::kind; public, offset 0
   (unnamed)          field         struct (unnamed at 11:5)   member     11    8    0  Packet::(unnamed at 11:5); public, offset 4
   tail               field         short                      member     12    2    1  Packet::tail; public, offset 12

 scope: global > struct Packet > struct (unnamed at 11:5)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   word               field         int                        member     11    4    0  (unnamed at 11:5)::word; public, offset 0
   bytes              field         char[4]                    member     11    4    0  (unnamed at 11:5)::bytes; public, offset 4

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      15    4    1  x.1
   y                  parameter     int                        param      15    4    1  y.2
   p                  variable      struct Point               local      16    8    1  p.3

 scope: global > area()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     struct Rect                param      20   20    6  r.4

 scope: global > move()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Point *             param      25    4    1  p.5
   dx                 parameter     int                        param      25    4    1  dx.6

 scope: global > add()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     Complex                    param      27   16    2  a.7
   b                  parameter     Complex                    param      27   16    2  b.8
   c                  variable      Complex                    local      28   16    3  c.9

 scope: global > length()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param      34    4    3  head.10
   n                  variable      int                        local      35    4    2  n.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      struct Rect                local      43   20    8  r.12
   copy               variable      struct Rect                local      44   20    3  copy.13
   pts                variable      struct Point[3]            local      50   24    7  pts.14
   pp                 variable      struct Point *             local      56    4    2  pp.16
   rp                 variable      struct Rect *              local      58    4    3  rp.17
   a                  variable      Complex                    local      62   16    1  a.18
   b                  variable      Complex                    local      62   16    1  b.19
   c                  variable      Complex                    local      63   16    2  c.20
   n1                 variable      struct Node                local      66    8    4  n1.21
   n2                 variable      struct Node                local      66    8    3  n2.22
   n3                 variable      struct Node                local      66    8    3  n3.23
   k                  variable      struct Packet              local      72   16    5  k.24
   zero               variable      struct Point               local      75    8    1  zero.25

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      51    4    6  i.15

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
struct (unnamed at 8:9): size 16, align 8
    +0  double re  [public]
    +8  double im  [public]
struct Packet: size 16, align 4
    +0  int kind  [public]
    +4  struct (unnamed at 11:5)   [public]
    +12  short tail  [public]
    +4  int word  [public]  (from the unnamed member)
    +8  char[4] bytes  [public]  (from the unnamed member)
struct (unnamed at 11:5): size 8, align 4
    +0  int word  [public]
    +4  char[4] bytes  [public]
