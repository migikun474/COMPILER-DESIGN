=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t06_structs.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 187 -> 186 instruction(s) for 'test/t06_structs.c'.

optimization summary (-O3)
    instructions                187 -> 186   (0% fewer)
    constants folded            1
    algebraic simplifications   1
    common subexpressions       6
    copies / constants forwarded 23
    temporaries merged away     5
    dead instructions removed   22
    jumps removed or redirected 2
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    2
    calls inlined               7
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

globals (name, type, width, initial value)
    origin         struct Point               8  { +0: 3, +4: 4 }

function make(int, int)        link name: _Z4makeii
  symbol table (name, kind, type, width, offset)
    x              param  int                        4      0
    y              param  int                        4      4
    p              local  struct Point               8      8
    total width 16
  code
 100:   p[0] = x
 101:   p[4] = y
 102:   return p

function area(struct Rect)        link name: _Z4area4Rect
  symbol table (name, kind, type, width, offset)
    r              param  struct Rect               20      0
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    t8             temp   int                        4     48
    total width 52
  code
 103:   t1 = r[8]
 104:   t2 = r[0]
 105:   t3 = t1 int- t2
 106:   r[8] = t3
 107:   t5 = r[12]
 108:   t6 = r[4]
 109:   t7 = t5 int- t6
 110:   t8 = t3 int* t7
 111:   return t8

function move(struct Point *, int)        link name: _Z4moveP5Pointi
  symbol table (name, kind, type, width, offset)
    p              param  struct Point *             4      0
    dx             param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 112:   t1 = *p
 113:   t2 = t1 int+ dx
 114:   *p = t2
 115:   return

function add(Complex, Complex)        link name: _Z3add7ComplexS_
  symbol table (name, kind, type, width, offset)
    a              param  Complex                   16      0
    b              param  Complex                   16     16
    c              local  Complex                   16     32
    t1             temp   double                     8     48
    t2             temp   double                     8     56
    t3             temp   double                     8     64
    t4             temp   double                     8     72
    t5             temp   double                     8     80
    t6             temp   double                     8     88
    total width 96
  code
 116:   t1 = a[0]
 117:   t2 = b[0]
 118:   t3 = t1 double+ t2
 119:   c[0] = t3
 120:   t4 = a[8]
 121:   t5 = b[8]
 122:   t6 = t4 double+ t5
 123:   c[8] = t6
 124:   return c

function length(struct Node *)        link name: _Z6lengthP4Node
  symbol table (name, kind, type, width, offset)
    head           param  struct Node *              4      0
    n              local  int                        4      4
    t1             temp   int                        4      8
    t2             temp   struct Node *              4     12
    t3             temp   struct Node *              4     16
    total width 20
  code
 125:     n = 0
 126: L1: if head ptr== 0 goto L2
 127:     n = n int+ 1
 128:     t2 = head ptr+ 4
 129:     head = *t2
 130:     goto L1
 131: L2: return n

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    r              local  struct Rect               20      0
    copy           local  struct Rect               20     20
    pts            local  struct Point[3]           24     40
    i              local  int                        4     64
    pp             local  struct Point *             4     68
    rp             local  struct Rect *              4     72
    a              local  Complex                   16     80
    b              local  Complex                   16     96
    c              local  Complex                   16    112
    n1             local  struct Node                8    128
    n2             local  struct Node                8    136
    n3             local  struct Node                8    144
    k              local  struct Packet             16    152
    zero           local  struct Point               8    168
    t1             temp   int                        4    176
    t2             temp   int                        4    180
    t3             temp   int                        4    184
    t4             temp   char                       1    188
    t5             temp   int                        4    192
    t6             temp   int                        4    196
    t7             temp   int                        4    200
    t8             temp   int                        4    204
    t9             temp   int                        4    208
    t10            temp   int                        4    212
    t11            temp   int                        4    216
    t12            temp   struct Point               8    220
    t13            temp   struct Point *             4    228
    t14            temp   int                        4    232
    t15            temp   struct Point *             4    236
    t16            temp   struct Point *             4    240
    t17            temp   struct Point *             4    244
    t18            temp   struct Point *             4    248
    t19            temp   struct Point *             4    252
    t20            temp   int                        4    256
    t21            temp   int                        4    260
    t22            temp   struct Point *             4    264
    t23            temp   int                        4    268
    t24            temp   int                        4    272
    t25            temp   int                        4    276
    t26            temp   struct Point               8    280
    t27            temp   struct Point *             4    288
    t28            temp   int                        4    292
    t29            temp   struct Point *             4    296
    t30            temp   struct Point *             4    300
    t31            temp   struct Point *             4    304
    t32            temp   int                        4    308
    t33            temp   int                        4    312
    t34            temp   struct Rect *              4    316
    t35            temp   struct Point               8    320
    t36            temp   struct Point *             4    328
    t37            temp   int                        4    332
    t38            temp   int                        4    336
    t39            temp   struct Rect *              4    340
    t40            temp   int                        4    344
    t41            temp   Complex                   16    352
    t42            temp   Complex *                  4    368
    t43            temp   Complex *                  4    372
    t44            temp   double                     8    376
    t45            temp   double                     8    384
    t46            temp   struct Node *              4    392
    t47            temp   struct Node *              4    396
    t48            temp   struct Node *              4    400
    t49            temp   int                        4    404
    t50            temp   struct Node *              4    408
    t51            temp   struct Node *              4    412
    t52            temp   struct Node *              4    416
    t53            temp   int                        4    420
    t54            temp   int                        4    424
    t55            temp   int                        4    428
    t56            temp   char                       1    432
    t57            temp   int                        4    436
    t58            temp   short                      2    440
    t59            temp   int                        4    444
    t60            temp   int                        4    448
    t61            temp   int                        4    452
    t62            temp   int                        4    456
    t63            temp   struct Rect               20    460
    t64            temp   int                        4    480
    t65            temp   int                        4    484
    t66            temp   int                        4    488
    t67            temp   int                        4    492
    t68            temp   int                        4    496
    t69            temp   int                        4    500
    t70            temp   int                        4    504
    t71            temp   int                        4    508
    t72            temp   int                        4    512
    t73            temp   struct Point               8    516
    t74            temp   struct Point *             4    524
    t75            temp   int                        4    528
    t76            temp   int                        4    532
    t77            temp   int                        4    536
    t78            temp   int                        4    540
    t79            temp   int                        4    544
    t80            temp   struct Point               8    548
    t81            temp   int                        4    556
    t82            temp   int                        4    560
    t83            temp   struct Point               8    564
    t84            temp   Complex                   16    576
    t85            temp   Complex                   16    592
    t86            temp   double                     8    608
    t87            temp   double                     8    616
    t88            temp   double                     8    624
    t89            temp   Complex                   16    632
    t90            temp   double                     8    648
    t91            temp   double                     8    656
    t92            temp   double                     8    664
    t93            temp   struct Node *              4    672
    t94            temp   int                        4    676
    t95            temp   struct Node *              4    680
    total width 684
  code
 132:     r[0] = 1
 133:     r[4] = 2
 134:     r[8] = 5
 135:     r[12] = 8
 136:     r[16] = 114
 137:     copy = r
 138:     copy[0] = 100
 139:     t1 = r[0]
 140:     t63 = r
 141:     t64 = t63[8]
 142:     t65 = t63[0]
 143:     t66 = t64 int- t65
 144:     t63[8] = t66
 145:     t67 = t63[12]
 146:     t68 = t63[4]
 147:     t69 = t67 int- t68
 148:     t70 = t66 int* t69
 149:     t4 = r[16]
 150:     t5 = chartoint t4
 151:     param "%d %d %d %c\n"
 152:     param t1
 153:     param 100
 154:     param t70
 155:     param t5
 156:     call printf, 5
 157:     t6 = r[8]
 158:     t7 = origin[0]
 159:     t8 = origin[4]
 160:     t9 = t7 int* t8
 161:     param "%d %d\n"
 162:     param t6
 163:     param t9
 164:     call printf, 3
 165:     i = 0
 166: L3: if i int>= 3 goto L4
 167:     t10 = i int<< 3                     (w = 8)
 168:     t11 = i int* i
 169:     t73[0] = i
 170:     t73[4] = t11
 171:     t12 = t73
 172:     pts[t10] = t12
 173:     i = i int+ 1
 174:     goto L3
 175: L4: t15 = &pts
 176:     t16 = t15 ptr+ 8
 177:     t76 = *t16
 178:     t77 = t76 int+ 10
 179:     *t16 = t77
 180:     t18 = t15 ptr+ 16
 181:     t19 = t18 ptr+ 4
 182:     t20 = *t19
 183:     t21 = t20 int+ 1
 184:     *t19 = t21
 185:     t23 = pts[8]
 186:     t24 = pts[12]
 187:     t25 = pts[20]
 188:     t80[0] = 3
 189:     t80[4] = 4
 190:     t26 = t80
 191:     t28 = t26[4]
 192:     param "%d %d %d %d\n"
 193:     param t23
 194:     param t24
 195:     param t25
 196:     param t28
 197:     call printf, 5
 198:     t29 = &r
 199:     t30 = t29 ptr+ 8
 200:     t31 = t30 ptr+ 4
 201:     t32 = *t31
 202:     t33 = t32 int+ 1
 203:     *t30 = t33
 204:     t83[0] = 7
 205:     t83[4] = 7
 206:     t35 = t83
 207:     *t29 = t35
 208:     t37 = r[8]
 209:     t38 = *t29
 210:     t39 = t29 ptr+ 12
 211:     t40 = *t39
 212:     param "%d %d %d\n"
 213:     param t37
 214:     param t38
 215:     param t40
 216:     call printf, 4
 217:     a[0] = 1.5
 218:     a[8] = 2.0
 219:     b[0] = 1.0
 220:     b[8] = 0.5
 221:     t84 = a
 222:     t85 = b
 223:     t86 = t84[0]
 224:     t87 = t85[0]
 225:     t88 = t86 double+ t87
 226:     t89[0] = t88
 227:     t90 = t84[8]
 228:     t91 = t85[8]
 229:     t92 = t90 double+ t91
 230:     t89[8] = t92
 231:     c = t89
 232:     t44 = c[0]
 233:     t45 = c[8]
 234:     param "%.1f %.1f\n"
 235:     param t44
 236:     param t45
 237:     call printf, 3
 238:     n1[0] = 1
 239:     t46 = &n2
 240:     n1[4] = t46
 241:     n2[0] = 2
 242:     t47 = &n3
 243:     n2[4] = t47
 244:     n3[0] = 3
 245:     n3[4] = 0
 246:     t93 = &n1
 247:     t94 = 0
 248: L5: if t93 ptr== 0 goto L6
 249:     t94 = t94 int+ 1
 250:     t95 = t93 ptr+ 4
 251:     t93 = *t95
 252:     goto L5
 253: L6: t50 = n1[4]
 254:     t51 = t50 ptr+ 4
 255:     t52 = *t51
 256:     t53 = *t52
 257:     param "%d %d\n"
 258:     param t94
 259:     param t53
 260:     call printf, 3
 261:     k[0] = 1
 262:     k[4] = 16909060
 263:     k[8] = 0
 264:     k[9] = 0
 265:     k[10] = 0
 266:     k[11] = 0
 267:     k[12] = 9
 268:     k[9] = 120
 269:     t54 = k[0]
 270:     t55 = k[4]
 271:     t58 = k[12]
 272:     t59 = shorttoint t58
 273:     param "%d %d %c %d %d\n"
 274:     param t54
 275:     param t55
 276:     param 120
 277:     param t59
 278:     param 16
 279:     call printf, 6
 280:     zero[0] = 0
 281:     zero[4] = 0
 282:     t60 = zero[0]
 283:     t61 = pts[16]
 284:     t62 = t60 int+ t61
 285:     return t62


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Point              struct_tag     struct Point               -        global                         5     -     0     Point                -                        size 8
Point::x           field          int                        member   global > struct Point          5     4     16    Point::x             -                        public, offset 0
Point::y           field          int                        member   global > struct Point          5     4     9     Point::y             -                        public, offset 4
Rect               struct_tag     struct Rect                -        global                         6     -     0     Rect                 -                        size 20
Rect::low          field          struct Point               member   global > struct Rect           6     8     7     Rect::low            -                        public, offset 0
Rect::high         field          struct Point               member   global > struct Rect           6     8     8     Rect::high           -                        public, offset 8
Rect::tag          field          char                       member   global > struct Rect           6     1     1     Rect::tag            -                        public, offset 16
Node               struct_tag     struct Node                -        global                         7     -     0     Node                 -                        size 8
Node::value        field          int                        member   global > struct Node           7     4     4     Node::value          -                        public, offset 0
Node::next         field          struct Node *              member   global > struct Node           7     4     6     Node::next           -                        public, offset 4
(unnamed at 8:9)   struct_tag     struct (unnamed at 8:9)    -        global                         8     -     0     (unnamed at 8:9)     -                        size 16
(unnamed at 8:9)::re field          double                     member   global > struct (unnamed at 8:9) 8     8     4     (unnamed at 8:9)::re -                        public, offset 0
(unnamed at 8:9)::im field          double                     member   global > struct (unnamed at 8:9) 8     8     4     (unnamed at 8:9)::im -                        public, offset 8
Complex            typedef        Complex                    -        global                         8     -     0     Complex              -                        
Packet             struct_tag     struct Packet              -        global                         9     -     0     Packet               -                        size 16
Packet::kind       field          int                        member   global > struct Packet         10    4     1     Packet::kind         -                        public, offset 0
(unnamed at 11:5)  struct_tag     struct (unnamed at 11:5)   -        global                         11    -     0     (unnamed at 11:5)    -                        size 8
(unnamed at 11:5)::word field          int                        member   global > struct Packet > struct (unnamed at 11:5) 11    4     0     (unnamed at 11:5)::word -                        public, offset 0
(unnamed at 11:5)::bytes field          char[4]                    member   global > struct Packet > struct (unnamed at 11:5) 11    4     0     (unnamed at 11:5)::bytes -                        public, offset 4
(unnamed)          field          struct (unnamed at 11:5)   member   global > struct Packet         11    8     0     Packet::(unnamed at 11:5) -                        public, offset 4
Packet::tail       field          short                      member   global > struct Packet         12    2     1     Packet::tail         -                        public, offset 12
make               function       struct Point (int, int)    -        global                         15    -     3     _Z4makeii            _Z4makeii                defined
x                  parameter      int                        param    global > make()                15    4     1     x.1                  -                        
y                  parameter      int                        param    global > make()                15    4     1     y.2                  -                        
p                  variable       struct Point               local    global > make()                16    8     1     p.3                  -                        
area               function       int (struct Rect)          -        global                         20    -     1     _Z4area4Rect         _Z4area4Rect             defined
r                  parameter      struct Rect                param    global > area()                20    20    6     r.4                  -                        
move               function       void (struct Point *, int) -        global                         25    -     1     _Z4moveP5Pointi      _Z4moveP5Pointi          defined
p                  parameter      struct Point *             param    global > move()                25    4     1     p.5                  -                        
dx                 parameter      int                        param    global > move()                25    4     1     dx.6                 -                        
add                function       Complex (Complex, Complex) -        global                         27    -     1     _Z3add7ComplexS_     _Z3add7ComplexS_         defined
a                  parameter      Complex                    param    global > add()                 27    16    2     a.7                  -                        
b                  parameter      Complex                    param    global > add()                 27    16    2     b.8                  -                        
c                  variable       Complex                    local    global > add()                 28    16    3     c.9                  -                        
length             function       int (struct Node *)        -        global                         34    -     1     _Z6lengthP4Node      _Z6lengthP4Node          defined
head               parameter      struct Node *              param    global > length()              34    4     3     head.10              -                        
n                  variable       int                        local    global > length()              35    4     2     n.11                 -                        
origin             variable       struct Point               global   global                         40    8     2     origin               -                        
main               function       int (void)                 -        global                         42    -     0     main                 main                     defined
r                  variable       struct Rect                local    global > main()                43    20    8     r.12                 -                        
copy               variable       struct Rect                local    global > main()                44    20    3     copy.13              -                        
pts                variable       struct Point[3]            local    global > main()                50    24    7     pts.14               -                        
i                  variable       int                        local    global > main() > for          51    4     6     i.15                 -                        
pp                 variable       struct Point *             local    global > main()                56    4     2     pp.16                -                        
rp                 variable       struct Rect *              local    global > main()                58    4     3     rp.17                -                        
a                  variable       Complex                    local    global > main()                62    16    1     a.18                 -                        
b                  variable       Complex                    local    global > main()                62    16    1     b.19                 -                        
c                  variable       Complex                    local    global > main()                63    16    2     c.20                 -                        
n1                 variable       struct Node                local    global > main()                66    8     4     n1.21                -                        
n2                 variable       struct Node                local    global > main()                66    8     3     n2.22                -                        
n3                 variable       struct Node                local    global > main()                66    8     3     n3.23                -                        
k                  variable       struct Packet              local    global > main()                72    16    5     k.24                 -                        
zero               variable       struct Point               local    global > main()                75    8     1     zero.25              -                        

=== Record Layouts ===
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
