=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t06_structs.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 187 -> 170 instruction(s) for 'test/t06_structs.c'.

optimization summary (-O1)
    instructions                187 -> 170   (9% fewer)
    constants folded            1
    algebraic simplifications   1
    common subexpressions       6
    copies / constants forwarded 12
    temporaries merged away     3
    dead instructions removed   12
    jumps removed or redirected 2
    unreachable instructions    0

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
    total width 460
  code
 132:     r[0] = 1
 133:     r[4] = 2
 134:     r[8] = 5
 135:     r[12] = 8
 136:     r[16] = 114
 137:     copy = r
 138:     copy[0] = 100
 139:     t1 = r[0]
 140:     param r
 141:     t3 = call area(struct Rect), 1
 142:     t4 = r[16]
 143:     t5 = chartoint t4
 144:     param "%d %d %d %c\n"
 145:     param t1
 146:     param 100
 147:     param t3
 148:     param t5
 149:     call printf, 5
 150:     t6 = r[8]
 151:     t7 = origin[0]
 152:     t8 = origin[4]
 153:     t9 = t7 int* t8
 154:     param "%d %d\n"
 155:     param t6
 156:     param t9
 157:     call printf, 3
 158:     i = 0
 159: L3: if i int>= 3 goto L4
 160:     t10 = i int<< 3                     (w = 8)
 161:     t11 = i int* i
 162:     param i
 163:     param t11
 164:     t12 = call make(int, int), 2
 165:     pts[t10] = t12
 166:     i = i int+ 1
 167:     goto L3
 168: L4: t15 = &pts
 169:     t16 = t15 ptr+ 8
 170:     param t16
 171:     param 10
 172:     call move(struct Point *, int), 2
 173:     t18 = t15 ptr+ 16
 174:     t19 = t18 ptr+ 4
 175:     t20 = *t19
 176:     t21 = t20 int+ 1
 177:     *t19 = t21
 178:     t23 = pts[8]
 179:     t24 = pts[12]
 180:     t25 = pts[20]
 181:     param 3
 182:     param 4
 183:     t26 = call make(int, int), 2
 184:     t28 = t26[4]
 185:     param "%d %d %d %d\n"
 186:     param t23
 187:     param t24
 188:     param t25
 189:     param t28
 190:     call printf, 5
 191:     t29 = &r
 192:     t30 = t29 ptr+ 8
 193:     pp = t30
 194:     t31 = t30 ptr+ 4
 195:     t32 = *t31
 196:     t33 = t32 int+ 1
 197:     *t30 = t33
 198:     rp = t29
 199:     param 7
 200:     param 7
 201:     t35 = call make(int, int), 2
 202:     *t29 = t35
 203:     t37 = r[8]
 204:     t38 = *t29
 205:     t39 = t29 ptr+ 12
 206:     t40 = *t39
 207:     param "%d %d %d\n"
 208:     param t37
 209:     param t38
 210:     param t40
 211:     call printf, 4
 212:     a[0] = 1.5
 213:     a[8] = 2.0
 214:     b[0] = 1.0
 215:     b[8] = 0.5
 216:     param a
 217:     param b
 218:     t41 = call add(Complex, Complex), 2
 219:     c = t41
 220:     t44 = c[0]
 221:     t45 = c[8]
 222:     param "%.1f %.1f\n"
 223:     param t44
 224:     param t45
 225:     call printf, 3
 226:     n1[0] = 1
 227:     t46 = &n2
 228:     n1[4] = t46
 229:     n2[0] = 2
 230:     t47 = &n3
 231:     n2[4] = t47
 232:     n3[0] = 3
 233:     n3[4] = 0
 234:     t48 = &n1
 235:     param t48
 236:     t49 = call length(struct Node *), 1
 237:     t50 = n1[4]
 238:     t51 = t50 ptr+ 4
 239:     t52 = *t51
 240:     t53 = *t52
 241:     param "%d %d\n"
 242:     param t49
 243:     param t53
 244:     call printf, 3
 245:     k[0] = 1
 246:     k[4] = 16909060
 247:     k[8] = 0
 248:     k[9] = 0
 249:     k[10] = 0
 250:     k[11] = 0
 251:     k[12] = 9
 252:     k[9] = 120
 253:     t54 = k[0]
 254:     t55 = k[4]
 255:     t58 = k[12]
 256:     t59 = shorttoint t58
 257:     param "%d %d %c %d %d\n"
 258:     param t54
 259:     param t55
 260:     param 120
 261:     param t59
 262:     param 16
 263:     call printf, 6
 264:     zero[0] = 0
 265:     zero[4] = 0
 266:     t60 = zero[0]
 267:     t61 = pts[16]
 268:     t62 = t60 int+ t61
 269:     return t62


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
