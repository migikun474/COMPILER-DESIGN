============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : no optimization
   Result        : Three address code generated: 6 function(s), 182 instruction(s)

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

 Symbol table: 14 parameter(s)/local(s), 57 temporaries, frame 436 bytes

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
   t13              temp    int                             4     228
   t14              temp    struct Point *                  4     232
   t15              temp    struct Point *                  4     236
   t16              temp    struct Point *                  4     240
   t17              temp    struct Point *                  4     244
   t18              temp    struct Point *                  4     248
   t19              temp    int                             4     252
   t20              temp    int                             4     256
   t21              temp    struct Point *                  4     260
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
   t32              temp    struct Rect *                   4     308
   t33              temp    struct Point                    8     312
   t34              temp    int                             4     320
   t35              temp    int                             4     324
   t36              temp    struct Rect *                   4     328
   t37              temp    int                             4     332
   t38              temp    Complex                        16     336
   t39              temp    double                          8     352
   t40              temp    double                          8     360
   t41              temp    struct Node *                   4     368
   t42              temp    struct Node *                   4     372
   t43              temp    struct Node *                   4     376
   t44              temp    int                             4     380
   t45              temp    struct Node *                   4     384
   t46              temp    struct Node *                   4     388
   t47              temp    struct Node *                   4     392
   t48              temp    int                             4     396
   t49              temp    int                             4     400
   t50              temp    int                             4     404
   t51              temp    char                            1     408
   t52              temp    int                             4     412
   t53              temp    short                           2     416
   t54              temp    int                             4     420
   t55              temp    int                             4     424
   t56              temp    int                             4     428
   t57              temp    int                             4     432

 Code: 146 instruction(s)

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
    171       pts[t10] = t12
    172       t13 = i int+ 1
    173       i = t13
    174       goto L4
    175  L6:  t14 = &pts
    176       t15 = t14 ptr+ 8
    177       param t15
    178       param 10
    179       call move(struct Point *, int), 2
    180       t16 = &pts
    181       t17 = t16 ptr+ 16
    182       t18 = t17 ptr+ 4
    183       t19 = *t18
    184       t20 = t19 int+ 1
    185       t21 = t17 ptr+ 4
    186       *t21 = t20
    187       t22 = pts[8]
    188       t23 = pts[12]
    189       t24 = pts[20]
    190       param 3
    191       param 4
    192       t25 = call make(int, int), 2
    193       t26 = t25[4]
    194       param "%d %d %d %d\n"
    195       param t22
    196       param t23
    197       param t24
    198       param t26
    199       call printf, 5
    200       t27 = &r
    201       t28 = t27 ptr+ 8
    202       pp = t28
    203       t29 = pp ptr+ 4
    204       t30 = *t29
    205       t31 = t30 int+ 1
    206       *pp = t31
    207       t32 = &r
    208       rp = t32
    209       param 7
    210       param 7
    211       t33 = call make(int, int), 2
    212       *rp = t33
    213       t34 = r[8]
    214       t35 = *rp
    215       t36 = rp ptr+ 12
    216       t37 = *t36
    217       param "%d %d %d\n"
    218       param t34
    219       param t35
    220       param t37
    221       call printf, 4
    222       a[0] = 1.5
    223       a[8] = 2.0
    224       b[0] = 1.0
    225       b[8] = 0.5
    226       param a
    227       param b
    228       t38 = call add(Complex, Complex), 2
    229       c = t38
    230       t39 = c[0]
    231       t40 = c[8]
    232       param "%.1f %.1f\n"
    233       param t39
    234       param t40
    235       call printf, 3
    236       n1[0] = 1
    237       t41 = &n2
    238       n1[4] = t41
    239       n2[0] = 2
    240       t42 = &n3
    241       n2[4] = t42
    242       n3[0] = 3
    243       n3[4] = 0
    244       t43 = &n1
    245       param t43
    246       t44 = call length(struct Node *), 1
    247       t45 = n1[4]
    248       t46 = t45 ptr+ 4
    249       t47 = *t46
    250       t48 = *t47
    251       param "%d %d\n"
    252       param t44
    253       param t48
    254       call printf, 3
    255       k[0] = 1
    256       k[4] = 16909060
    257       k[8] = 0
    258       k[9] = 0
    259       k[10] = 0
    260       k[11] = 0
    261       k[12] = 9
    262       k[9] = 120
    263       t49 = k[0]
    264       t50 = k[4]
    265       t51 = k[9]
    266       t52 = chartoint t51
    267       t53 = k[12]
    268       t54 = shorttoint t53
    269       param "%d %d %c %d %d\n"
    270       param t49
    271       param t50
    272       param t52
    273       param t54
    274       param 16
    275       call printf, 6
    276       zero[0] = 0
    277       zero[4] = 0
    278       t55 = zero[0]
    279       t56 = pts[16]
    280       t57 = t55 int+ t56
    281       return t57


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
