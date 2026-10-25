============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 187 -> 168 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          187 -> 168   (10% fewer)

   constants folded                        1
   algebraic simplifications               1
   common subexpressions                   6
   copies / constants forwarded           12
   temporaries merged away                 3
   dead instructions removed              12
   jumps removed or redirected             2
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                2

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

 Symbol table: 14 parameter(s)/local(s), 50 temporaries, frame 460 bytes

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
   t15              temp    struct Point *                  4     236
   t16              temp    struct Point *                  4     240
   t18              temp    struct Point *                  4     248
   t19              temp    struct Point *                  4     252
   t20              temp    int                             4     256
   t21              temp    int                             4     260
   t23              temp    int                             4     268
   t24              temp    int                             4     272
   t25              temp    int                             4     276
   t26              temp    struct Point                    8     280
   t28              temp    int                             4     292
   t29              temp    struct Point *                  4     296
   t30              temp    struct Point *                  4     300
   t31              temp    struct Point *                  4     304
   t32              temp    int                             4     308
   t33              temp    int                             4     312
   t35              temp    struct Point                    8     320
   t37              temp    int                             4     332
   t38              temp    int                             4     336
   t39              temp    struct Rect *                   4     340
   t40              temp    int                             4     344
   t41              temp    Complex                        16     352
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
   t58              temp    short                           2     440
   t59              temp    int                             4     444
   t60              temp    int                             4     448
   t61              temp    int                             4     452
   t62              temp    int                             4     456
   (12 temporaries no longer used after optimization not shown)

 Code: 136 instruction(s)

    132       r[0] = 1
    133       r[4] = 2
    134       r[8] = 5
    135       r[12] = 8
    136       r[16] = 114
    137       copy = r
    138       copy[0] = 100
    139       t1 = r[0]
    140       param r
    141       t3 = call area(struct Rect), 1
    142       t4 = r[16]
    143       t5 = chartoint t4
    144       param "%d %d %d %c\n"
    145       param t1
    146       param 100
    147       param t3
    148       param t5
    149       call printf, 5
    150       t6 = r[8]
    151       t7 = origin[0]
    152       t8 = origin[4]
    153       t9 = t7 int* t8
    154       param "%d %d\n"
    155       param t6
    156       param t9
    157       call printf, 3
    158       i = 0
    159  L3:  if i int>= 3 goto L4
    160       t10 = i int<< 3                     (w = 8)
    161       t11 = i int* i
    162       param i
    163       param t11
    164       t12 = call make(int, int), 2
    165       pts[t10] = t12
    166       i = i int+ 1
    167       goto L3
    168  L4:  t15 = &pts
    169       t16 = t15 ptr+ 8
    170       param t16
    171       param 10
    172       call move(struct Point *, int), 2
    173       t18 = t15 ptr+ 16
    174       t19 = t18 ptr+ 4
    175       t20 = *t19
    176       t21 = t20 int+ 1
    177       *t19 = t21
    178       t23 = pts[8]
    179       t24 = pts[12]
    180       t25 = pts[20]
    181       param 3
    182       param 4
    183       t26 = call make(int, int), 2
    184       t28 = t26[4]
    185       param "%d %d %d %d\n"
    186       param t23
    187       param t24
    188       param t25
    189       param t28
    190       call printf, 5
    191       t29 = &r
    192       t30 = t29 ptr+ 8
    193       t31 = t30 ptr+ 4
    194       t32 = *t31
    195       t33 = t32 int+ 1
    196       *t30 = t33
    197       param 7
    198       param 7
    199       t35 = call make(int, int), 2
    200       *t29 = t35
    201       t37 = r[8]
    202       t38 = *t29
    203       t39 = t29 ptr+ 12
    204       t40 = *t39
    205       param "%d %d %d\n"
    206       param t37
    207       param t38
    208       param t40
    209       call printf, 4
    210       a[0] = 1.5
    211       a[8] = 2.0
    212       b[0] = 1.0
    213       b[8] = 0.5
    214       param a
    215       param b
    216       t41 = call add(Complex, Complex), 2
    217       c = t41
    218       t44 = c[0]
    219       t45 = c[8]
    220       param "%.1f %.1f\n"
    221       param t44
    222       param t45
    223       call printf, 3
    224       n1[0] = 1
    225       t46 = &n2
    226       n1[4] = t46
    227       n2[0] = 2
    228       t47 = &n3
    229       n2[4] = t47
    230       n3[0] = 3
    231       n3[4] = 0
    232       t48 = &n1
    233       param t48
    234       t49 = call length(struct Node *), 1
    235       t50 = n1[4]
    236       t51 = t50 ptr+ 4
    237       t52 = *t51
    238       t53 = *t52
    239       param "%d %d\n"
    240       param t49
    241       param t53
    242       call printf, 3
    243       k[0] = 1
    244       k[4] = 16909060
    245       k[8] = 0
    246       k[9] = 0
    247       k[10] = 0
    248       k[11] = 0
    249       k[12] = 9
    250       k[9] = 120
    251       t54 = k[0]
    252       t55 = k[4]
    253       t58 = k[12]
    254       t59 = shorttoint t58
    255       param "%d %d %c %d %d\n"
    256       param t54
    257       param t55
    258       param 120
    259       param t59
    260       param 16
    261       call printf, 6
    262       zero[0] = 0
    263       zero[4] = 0
    264       t60 = zero[0]
    265       t61 = pts[16]
    266       t62 = t60 int+ t61
    267       return t62


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
