=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t23_objects.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 378 -> 391 instruction(s) for 'test/t23_objects.c'.

optimization summary (-O3)
    instructions                378 -> 391   (-3% fewer)
    constants folded            3
    algebraic simplifications   2
    common subexpressions       87
    copies / constants forwarded 230
    temporaries merged away     5
    dead instructions removed   183
    jumps removed or redirected 3
    unreachable instructions    3
    propagated across blocks    0
    dead assignments removed    3
    calls inlined               45
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

globals (name, type, width, initial value)
    Shape::live    int                        4  0

function Shape::Shape()        link name: _ZN5ShapeC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 100:   t1 = Shape::live int+ 1
 101:   Shape::live = t1
 102:   *this = t1
 103:   param "Shape %d\n"
 104:   param t1
 105:   call printf, 2
 106:   return

function Shape::~Shape()        link name: _ZN5ShapeD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 107:   t1 = *this
 108:   param "~Shape %d\n"
 109:   param t1
 110:   call printf, 2
 111:   Shape::live = Shape::live int- 1
 112:   return

function Shape::area()        link name: _ZN5Shape4areaEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 113:   return 0

function Shape::name()        link name: _ZN5Shape4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 114:   return 83

function Rect::Rect(int, int)        link name: _ZN4RectC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Rect *               4     12
    t2             temp   class Rect *               4     16
    t3             temp   class Shape *              4     20
    t4             temp   int                        4     24
    total width 28
  code
 115:   t4 = Shape::live int+ 1
 116:   Shape::live = t4
 117:   *this = t4
 118:   param "Shape %d\n"
 119:   param t4
 120:   call printf, 2
 121:   t1 = this ptr+ 4
 122:   *t1 = a
 123:   t2 = this ptr+ 8
 124:   *t2 = b
 125:   return

function Rect::Rect()        link name: _ZN4RectC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    t1             temp   class Rect *               4      4
    t2             temp   class Rect *               4      8
    t3             temp   class Shape *              4     12
    t4             temp   int                        4     16
    total width 20
  code
 126:   t4 = Shape::live int+ 1
 127:   Shape::live = t4
 128:   *this = t4
 129:   param "Shape %d\n"
 130:   param t4
 131:   call printf, 2
 132:   t1 = this ptr+ 4
 133:   *t1 = 1
 134:   t2 = this ptr+ 8
 135:   *t2 = 1
 136:   return

function Rect::area()        link name: _ZN4Rect4areaEv
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    t1             temp   class Rect *               4      4
    t2             temp   int                        4      8
    t3             temp   class Rect *               4     12
    t4             temp   int                        4     16
    t5             temp   int                        4     20
    total width 24
  code
 137:   t1 = this ptr+ 4
 138:   t2 = *t1
 139:   t3 = this ptr+ 8
 140:   t4 = *t3
 141:   t5 = t2 int* t4
 142:   return t5

function Rect::perimeter()        link name: _ZN4Rect9perimeterEv
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    t1             temp   class Rect *               4      4
    t2             temp   int                        4      8
    t3             temp   class Rect *               4     12
    t4             temp   int                        4     16
    t5             temp   int                        4     20
    t6             temp   int                        4     24
    total width 28
  code
 143:   t1 = this ptr+ 4
 144:   t2 = *t1
 145:   t3 = this ptr+ 8
 146:   t4 = *t3
 147:   t5 = t2 int+ t4
 148:   t6 = t5 int<< 1
 149:   return t6

function Square::Square(int)        link name: _ZN6SquareC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    side           param  int                        4      4
    t1             temp   class Square *             4      8
    t2             temp   class Square *             4     12
    t3             temp   class Rect *               4     16
    t4             temp   class Rect *               4     20
    t5             temp   class Rect *               4     24
    total width 28
  code
 150:   param this                          (this)
 151:   call Shape::Shape(), 1
 152:   t4 = this ptr+ 4
 153:   *t4 = 1
 154:   t5 = this ptr+ 8
 155:   *t5 = 1
 156:   *t4 = side
 157:   *t5 = side
 158:   return

function Square::name()        link name: _ZN6Square4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 159:   return 81

function Point::Point(int, int)        link name: _ZN5PointC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Point *              4     12
    total width 16
  code
 160:   *this = a
 161:   t1 = this ptr+ 4
 162:   *t1 = b
 163:   return

function Point::Point()        link name: _ZN5PointC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    t1             temp   class Point *              4      4
    total width 8
  code
 164:   *this = 0
 165:   t1 = this ptr+ 4
 166:   *t1 = 0
 167:   return

function Point::operator+=(const class Point &)        link name: _ZN5PointpLERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    o              param  const class Point &        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   class Point *              4     20
    t5             temp   int                        4     24
    t6             temp   const class Point *        4     28
    t7             temp   int                        4     32
    t8             temp   int                        4     36
    t9             temp   class Point *              4     40
    total width 44
  code
 168:   t1 = *this
 169:   t2 = *o
 170:   t3 = t1 int+ t2
 171:   *this = t3
 172:   t4 = this ptr+ 4
 173:   t5 = *t4
 174:   t6 = o ptr+ 4
 175:   t7 = *t6
 176:   t8 = t5 int+ t7
 177:   *t4 = t8
 178:   return this

function Point::operator-(const class Point &)        link name: _ZN5PointmiERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    o              param  const class Point &        4      4
    t1             temp   class Point                8      8
    t2             temp   class Point *              4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    t5             temp   int                        4     28
    t6             temp   class Point *              4     32
    t7             temp   int                        4     36
    t8             temp   const class Point *        4     40
    t9             temp   int                        4     44
    t10            temp   int                        4     48
    t11            temp   class Point *              4     52
    t12            temp   int                        4     56
    t13            temp   int                        4     60
    t14            temp   class Point *              4     64
    total width 68
  code
 179:   t2 = &t1
 180:   t3 = *this
 181:   t4 = *o
 182:   t5 = t3 int- t4
 183:   t6 = this ptr+ 4
 184:   t7 = *t6
 185:   t8 = o ptr+ 4
 186:   t9 = *t8
 187:   t10 = t7 int- t9
 188:   *t2 = t5
 189:   t14 = t2 ptr+ 4
 190:   *t14 = t10
 191:   return t1

function Point::operator<(const class Point &)        link name: _ZN5PointltERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    o              param  const class Point &        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   class Point *              4     24
    t6             temp   int                        4     28
    t7             temp   class Point *              4     32
    t8             temp   int                        4     36
    t9             temp   int                        4     40
    t10            temp   int                        4     44
    t11            temp   int                        4     48
    t12            temp   int                        4     52
    t13            temp   int                        4     56
    t14            temp   const class Point *        4     60
    t15            temp   int                        4     64
    t16            temp   const class Point *        4     68
    t17            temp   int                        4     72
    t18            temp   int                        4     76
    t19            temp   int                        4     80
    t20            temp   bool                       1     84
    total width 88
  code
 192:     t2 = *this
 193:     t4 = t2 int* t2
 194:     t5 = this ptr+ 4
 195:     t6 = *t5
 196:     t9 = t6 int* t6
 197:     t10 = t4 int+ t9
 198:     t11 = *o
 199:     t13 = t11 int* t11
 200:     t14 = o ptr+ 4
 201:     t15 = *t14
 202:     t18 = t15 int* t15
 203:     t19 = t13 int+ t18
 204:     if t10 int< t19 goto L1
 205:     t1 = 0
 206:     goto L2
 207: L1: t1 = 1
 208: L2: if t1 int!= 0 goto L3
 209:     t20 = 0
 210:     goto L4
 211: L3: t20 = 1
 212: L4: return t20

function Point::operator[](int)        link name: _ZN5PointixEi
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    i              param  int                        4      4
    t1             temp   int *                      4      8
    t2             temp   class Point *              4     12
    total width 16
  code
 213:     if i int!= 0 goto L5
 214:     t1 = this
 215:     goto L6
 216: L5: t1 = this ptr+ 4
 217: L6: return t1

function Segment::Segment(int, int, int, int)        link name: _ZN7SegmentC1Eiiii
  symbol table (name, kind, type, width, offset)
    this           param  class Segment *            4      0
    a              param  int                        4      4
    b              param  int                        4      8
    c              param  int                        4     12
    d              param  int                        4     16
    t1             temp   class Segment *            4     20
    t2             temp   class Point                8     24
    t3             temp   class Point *              4     32
    t4             temp   class Point                8     36
    t5             temp   class Point *              4     44
    t6             temp   class Segment *            4     48
    t7             temp   class Point *              4     52
    t8             temp   class Point *              4     56
    t9             temp   class Point *              4     60
    t10            temp   class Point *              4     64
    t11            temp   class Point *              4     68
    t12            temp   int                        4     72
    t13            temp   int                        4     76
    t14            temp   class Point *              4     80
    t15            temp   class Point *              4     84
    t16            temp   int                        4     88
    t17            temp   int                        4     92
    t18            temp   class Point *              4     96
    total width 100
  code
 218:   *this = 0
 219:   t8 = this ptr+ 4
 220:   *t8 = 0
 221:   t1 = this ptr+ 8
 222:   *t1 = 0
 223:   t10 = t1 ptr+ 4
 224:   *t10 = 0
 225:   t3 = &t2
 226:   *t3 = a
 227:   t14 = t3 ptr+ 4
 228:   *t14 = b
 229:   *this = t2
 230:   t5 = &t4
 231:   *t5 = c
 232:   t18 = t5 ptr+ 4
 233:   *t18 = d
 234:   *t1 = t4
 235:   return

function Segment::length2()        link name: _ZN7Segment7length2Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Segment *            4      0
    d              local  class Point                8      4
    t1             temp   class Segment *            4     12
    t2             temp   class Point                8     16
    t3             temp   class Point *              4     24
    t4             temp   class Point *              4     28
    t5             temp   int                        4     32
    t6             temp   int                        4     36
    t7             temp   int                        4     40
    t8             temp   int                        4     44
    t9             temp   int                        4     48
    t10            temp   int                        4     52
    t11            temp   int                        4     56
    t12            temp   class Point *              4     60
    t13            temp   const class Point &        4     64
    t14            temp   class Point                8     68
    t15            temp   class Point *              4     76
    t16            temp   int                        4     80
    t17            temp   int                        4     84
    t18            temp   int                        4     88
    t19            temp   class Point *              4     92
    t20            temp   int                        4     96
    t21            temp   const class Point *        4    100
    t22            temp   int                        4    104
    t23            temp   int                        4    108
    total width 112
  code
 236:   t1 = this ptr+ 8
 237:   t15 = &t14
 238:   t16 = *t1
 239:   t17 = *this
 240:   t18 = t16 int- t17
 241:   t19 = t1 ptr+ 4
 242:   t20 = *t19
 243:   t21 = this ptr+ 4
 244:   t22 = *t21
 245:   t23 = t20 int- t22
 246:   param t15                           (this)
 247:   param t18
 248:   param t23
 249:   call Point::Point(int, int), 3
 250:   d = t14
 251:   t5 = d[0]
 252:   t7 = t5 int* t5
 253:   t8 = d[4]
 254:   t10 = t8 int* t8
 255:   t11 = t7 int+ t10
 256:   return t11

function total(class Rect &)        link name: _Z5totalR4Rect
  symbol table (name, kind, type, width, offset)
    r              param  class Rect &               4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   class Rect *               4     16
    t5             temp   class Rect *               4     20
    t6             temp   int                        4     24
    t7             temp   class Rect *               4     28
    t8             temp   int                        4     32
    t9             temp   int                        4     36
    total width 40
  code
 257:   t5 = r ptr+ 4
 258:   t6 = *t5
 259:   t7 = r ptr+ 8
 260:   t8 = *t7
 261:   t9 = t6 int* t8
 262:   t2 = *r
 263:   t3 = t9 int+ t2
 264:   return t3

function through(class Shape *)        link name: _Z7throughP5Shape
  symbol table (name, kind, type, width, offset)
    s              param  class Shape *              4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   class Shape *              4     16
    t5             temp   class Shape *              4     20
    total width 24
  code
 265:   return 83

function grow(class Rect *, int)        link name: _Z4growP4Recti
  symbol table (name, kind, type, width, offset)
    r              param  class Rect *               4      0
    by             param  int                        4      4
    t1             temp   class Rect *               4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   class Rect *               4     20
    t5             temp   class Rect *               4     24
    t6             temp   int                        4     28
    t7             temp   int                        4     32
    t8             temp   class Rect *               4     36
    total width 40
  code
 266:   t1 = r ptr+ 4
 267:   t2 = *t1
 268:   t3 = t2 int+ by
 269:   *t1 = t3
 270:   t5 = r ptr+ 8
 271:   t6 = *t5
 272:   t7 = t6 int+ by
 273:   *t5 = t7
 274:   return

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    r              local  class Rect                12      0
    q              local  class Square              12     12
    asShape        local  class Shape *              4     24
    alias          local  class Rect &               4     28
    pair           local  class Rect[2]             24     32
    a              local  class Point                8     56
    b              local  class Point                8     64
    c              local  class Point                8     72
    s              local  class Segment             16     80
    last           local  class Rect                12     96
    base           local  class Shape *              4    108
    t1             temp   class Rect *               4    112
    t2             temp   class Square *             4    116
    t3             temp   class Rect *               4    120
    t4             temp   int                        4    124
    t5             temp   class Square *             4    128
    t6             temp   int                        4    132
    t7             temp   class Square *             4    136
    t8             temp   int                        4    140
    t9             temp   class Square *             4    144
    t10            temp   class Rect *               4    148
    t11            temp   int                        4    152
    t12            temp   class Square *             4    156
    t13            temp   int                        4    160
    t14            temp   class Square *             4    164
    t15            temp   int                        4    168
    t16            temp   int                        4    172
    t17            temp   class Square *             4    176
    t18            temp   class Square *             4    180
    t19            temp   class Rect *               4    184
    t20            temp   class Square *             4    188
    t21            temp   int                        4    192
    t22            temp   int                        4    196
    t23            temp   class Rect (*)[2]          4    200
    t24            temp   class Rect (*)[2]          4    204
    t25            temp   class Rect *               4    208
    t26            temp   int                        4    212
    t27            temp   class Rect *               4    216
    t28            temp   class Rect *               4    220
    t29            temp   int                        4    224
    t30            temp   int                        4    228
    t31            temp   int                        4    232
    t32            temp   class Rect *               4    236
    t33            temp   class Rect *               4    240
    t34            temp   class Rect *               4    244
    t35            temp   class Point *              4    248
    t36            temp   class Point *              4    252
    t37            temp   class Point *              4    256
    t38            temp   class Point *              4    260
    t39            temp   class Point &              4    264
    t40            temp   class Point *              4    268
    t41            temp   class Point *              4    272
    t42            temp   class Point &              4    276
    t43            temp   class Point *              4    280
    t44            temp   class Point &              4    284
    t45            temp   class Point *              4    288
    t46            temp   int &                      4    292
    t47            temp   class Point *              4    296
    t48            temp   int &                      4    300
    t49            temp   int                        4    304
    t50            temp   int                        4    308
    t51            temp   class Point *              4    312
    t52            temp   class Point *              4    316
    t53            temp   class Point                8    320
    t54            temp   class Point *              4    328
    t55            temp   class Point *              4    332
    t56            temp   int                        4    336
    t57            temp   int                        4    340
    t58            temp   int                        4    344
    t59            temp   int                        4    348
    t60            temp   class Point *              4    352
    t61            temp   class Point *              4    356
    t62            temp   bool                       1    360
    t63            temp   int                        4    364
    t64            temp   class Point *              4    368
    t65            temp   class Point *              4    372
    t66            temp   bool                       1    376
    t67            temp   int                        4    380
    t68            temp   class Segment *            4    384
    t69            temp   class Segment *            4    388
    t70            temp   int                        4    392
    t71            temp   int                        4    396
    t72            temp   class Rect *               4    400
    t73            temp   class Rect *               4    404
    t74            temp   class Rect *               4    408
    t75            temp   int                        4    412
    t76            temp   int                        4    416
    t77            temp   int                        4    420
    t78            temp   class Rect *               4    424
    t79            temp   int                        4    428
    t80            temp   class Square *             4    432
    t81            temp   class Rect *               4    436
    t82            temp   class Rect *               4    440
    t83            temp   int                        4    444
    t84            temp   int                        4    448
    t85            temp   class Rect *               4    452
    t86            temp   class Rect *               4    456
    t87            temp   class Square *             4    460
    t88            temp   int                        4    464
    t89            temp   class Square *             4    468
    t90            temp   class Square *             4    472
    t91            temp   class Rect *               4    476
    t92            temp   class Rect *               4    480
    t93            temp   int                        4    484
    t94            temp   class Rect *               4    488
    t95            temp   int                        4    492
    t96            temp   int                        4    496
    t97            temp   class Rect *               4    500
    t98            temp   class Rect *               4    504
    t99            temp   int                        4    508
    t100           temp   class Rect *               4    512
    t101           temp   int                        4    516
    t102           temp   int                        4    520
    t103           temp   class Rect *               4    524
    t104           temp   class Rect *               4    528
    t105           temp   int                        4    532
    t106           temp   class Rect *               4    536
    t107           temp   int                        4    540
    t108           temp   int                        4    544
    t109           temp   int                        4    548
    t110           temp   class Rect &               4    552
    t111           temp   int                        4    556
    t112           temp   int                        4    560
    t113           temp   int                        4    564
    t114           temp   class Shape *              4    568
    t115           temp   int                        4    572
    t116           temp   int                        4    576
    t117           temp   int                        4    580
    t118           temp   class Square *             4    584
    t119           temp   class Shape *              4    588
    t120           temp   class Rect *               4    592
    t121           temp   int                        4    596
    t122           temp   class Rect *               4    600
    t123           temp   int                        4    604
    t124           temp   int                        4    608
    t125           temp   class Rect *               4    612
    t126           temp   int                        4    616
    t127           temp   int                        4    620
    t128           temp   class Rect *               4    624
    t129           temp   class Rect *               4    628
    t130           temp   int                        4    632
    t131           temp   class Rect *               4    636
    t132           temp   int                        4    640
    t133           temp   int                        4    644
    t134           temp   class Rect *               4    648
    t135           temp   class Rect *               4    652
    t136           temp   int                        4    656
    t137           temp   class Rect *               4    660
    t138           temp   int                        4    664
    t139           temp   int                        4    668
    t140           temp   int                        4    672
    t141           temp   class Rect *               4    676
    t142           temp   class Rect *               4    680
    t143           temp   class Rect *               4    684
    t144           temp   class Rect *               4    688
    t145           temp   class Rect *               4    692
    t146           temp   class Rect *               4    696
    t147           temp   class Rect *               4    700
    t148           temp   class Rect *               4    704
    t149           temp   int                        4    708
    t150           temp   class Rect *               4    712
    t151           temp   int                        4    716
    t152           temp   int                        4    720
    t153           temp   class Rect *               4    724
    t154           temp   class Rect *               4    728
    t155           temp   int                        4    732
    t156           temp   class Rect *               4    736
    t157           temp   int                        4    740
    t158           temp   int                        4    744
    t159           temp   class Shape *              4    748
    t160           temp   int                        4    752
    t161           temp   class Shape *              4    756
    t162           temp   int                        4    760
    t163           temp   class Point *              4    764
    t164           temp   int                        4    768
    t165           temp   int                        4    772
    t166           temp   class Point *              4    776
    t167           temp   class Point *              4    780
    t168           temp   int                        4    784
    t169           temp   int                        4    788
    t170           temp   class Point *              4    792
    t171           temp   class Point *              4    796
    t172           temp   const class Point &        4    800
    t173           temp   int                        4    804
    t174           temp   int                        4    808
    t175           temp   int                        4    812
    t176           temp   class Point *              4    816
    t177           temp   int                        4    820
    t178           temp   const class Point *        4    824
    t179           temp   int                        4    828
    t180           temp   int                        4    832
    t181           temp   class Point *              4    836
    t182           temp   const class Point &        4    840
    t183           temp   int                        4    844
    t184           temp   int                        4    848
    t185           temp   int                        4    852
    t186           temp   class Point *              4    856
    t187           temp   int                        4    860
    t188           temp   const class Point *        4    864
    t189           temp   int                        4    868
    t190           temp   int                        4    872
    t191           temp   class Point *              4    876
    t192           temp   const class Point &        4    880
    t193           temp   int                        4    884
    t194           temp   int                        4    888
    t195           temp   int                        4    892
    t196           temp   class Point *              4    896
    t197           temp   int                        4    900
    t198           temp   const class Point *        4    904
    t199           temp   int                        4    908
    t200           temp   int                        4    912
    t201           temp   class Point *              4    916
    t202           temp   int                        4    920
    t203           temp   int *                      4    924
    t204           temp   class Point *              4    928
    t205           temp   int                        4    932
    t206           temp   int *                      4    936
    t207           temp   class Point *              4    940
    t208           temp   const class Point &        4    944
    t209           temp   class Point                8    948
    t210           temp   class Point *              4    956
    t211           temp   int                        4    960
    t212           temp   int                        4    964
    t213           temp   int                        4    968
    t214           temp   class Point *              4    972
    t215           temp   int                        4    976
    t216           temp   const class Point *        4    980
    t217           temp   int                        4    984
    t218           temp   int                        4    988
    t219           temp   class Segment *            4    992
    t220           temp   class Segment *            4    996
    t221           temp   class Point                8   1000
    t222           temp   class Point                8   1008
    t223           temp   int                        4   1016
    t224           temp   int                        4   1020
    t225           temp   int                        4   1024
    t226           temp   int                        4   1028
    t227           temp   int                        4   1032
    t228           temp   class Rect *               4   1036
    t229           temp   int                        4   1040
    t230           temp   int                        4   1044
    t231           temp   class Rect *               4   1048
    t232           temp   class Rect *               4   1052
    t233           temp   class Rect *               4   1056
    t234           temp   class Rect *               4   1060
    t235           temp   int                        4   1064
    t236           temp   class Rect *               4   1068
    t237           temp   int                        4   1072
    t238           temp   int                        4   1076
    t239           temp   class Shape *              4   1080
    t240           temp   class Shape *              4   1084
    t241           temp   int                        4   1088
    t242           temp   class Shape *              4   1092
    t243           temp   int                        4   1096
    t244           temp   class Shape *              4   1100
    t245           temp   int                        4   1104
    total width 1108
  code
 275:   t1 = &r
 276:   param t1                            (this)
 277:   call Shape::Shape(), 1
 278:   t85 = t1 ptr+ 4
 279:   *t85 = 3
 280:   t86 = t1 ptr+ 8
 281:   *t86 = 4
 282:   t2 = &q
 283:   param t2                            (this)
 284:   call Rect::Rect(), 1
 285:   t89 = t2 ptr+ 4
 286:   *t89 = 5
 287:   t90 = t2 ptr+ 8
 288:   *t90 = 5
 289:   t93 = *t85
 290:   t95 = *t86
 291:   t96 = t93 int* t95
 292:   t99 = *t89
 293:   t102 = t99 int* 5
 294:   t108 = t99 int+ 5
 295:   t109 = t108 int<< 1
 296:   param "%d %d %d %d\n"
 297:   param t96
 298:   param t102
 299:   param t109
 300:   param Shape::live
 301:   call printf, 5
 302:   param t1                            (this)
 303:   t111 = call Rect::area(), 1
 304:   t112 = *t1
 305:   t113 = t111 int+ t112
 306:   param t2                            (this)
 307:   t115 = call Shape::area(), 1
 308:   param t2                            (this)
 309:   t116 = call Shape::name(), 1
 310:   t117 = t115 int+ t116
 311:   param "%d %d %c %c\n"
 312:   param t113
 313:   param t117
 314:   param 81
 315:   param 83
 316:   call printf, 5
 317:   t123 = *t89
 318:   t124 = t123 int+ 1
 319:   *t89 = t124
 320:   t126 = *t90
 321:   t127 = t126 int+ 1
 322:   *t90 = t127
 323:   *t89 = 10
 324:   t132 = *t90
 325:   t133 = t132 int* 10
 326:   t139 = 10 int+ t132
 327:   t140 = t139 int<< 1
 328:   param "%d %d\n"
 329:   param t133
 330:   param t140
 331:   call printf, 3
 332:   t23 = &pair
 333:   param t23                           (this)
 334:   call Shape::Shape(), 1
 335:   t142 = t23 ptr+ 4
 336:   *t142 = 1
 337:   t143 = t23 ptr+ 8
 338:   *t143 = 1
 339:   t24 = t23 ptr+ 12
 340:   param t24                           (this)
 341:   call Shape::Shape(), 1
 342:   t145 = t24 ptr+ 4
 343:   *t145 = 1
 344:   t146 = t24 ptr+ 8
 345:   *t146 = 1
 346:   pair[16] = 6
 347:   t149 = *t142
 348:   t151 = *t143
 349:   t152 = t149 int* t151
 350:   t155 = *t145
 351:   t157 = *t146
 352:   t158 = t155 int* t157
 353:   t30 = t152 int+ t158
 354:   t31 = pair[12]
 355:   param "%d %d %d\n"
 356:   param t30
 357:   param t31
 358:   param Shape::live
 359:   call printf, 4
 360:   t160 = *t24
 361:   param "~Shape %d\n"
 362:   param t160
 363:   call printf, 2
 364:   Shape::live = Shape::live int- 1
 365:   t162 = *t23
 366:   param "~Shape %d\n"
 367:   param t162
 368:   call printf, 2
 369:   Shape::live = Shape::live int- 1
 370:   param "%d\n"
 371:   param Shape::live
 372:   call printf, 2
 373:   t35 = &a
 374:   *t35 = 3
 375:   t166 = t35 ptr+ 4
 376:   *t166 = 4
 377:   t36 = &b
 378:   *t36 = 1
 379:   t170 = t36 ptr+ 4
 380:   *t170 = 1
 381:   t173 = *t35
 382:   t174 = *t36
 383:   t175 = t173 int+ t174
 384:   *t35 = t175
 385:   t177 = *t166
 386:   t179 = *t170
 387:   t180 = t177 int+ t179
 388:   *t166 = t180
 389:   t183 = *t35
 390:   t184 = *t36
 391:   t185 = t183 int+ t184
 392:   *t35 = t185
 393:   t187 = *t166
 394:   t189 = *t170
 395:   t190 = t187 int+ t189
 396:   *t166 = t190
 397:   t193 = *t35
 398:   t194 = *t36
 399:   t195 = t193 int+ t194
 400:   *t35 = t195
 401:   t197 = *t166
 402:   t199 = *t170
 403:   t200 = t197 int+ t199
 404:   *t166 = t200
 405:   t50 = t200 int<< 1
 406:   *t35 = t50
 407:   t210 = &t209
 408:   t212 = *t36
 409:   t213 = t50 int- t212
 410:   t215 = *t166
 411:   t217 = *t170
 412:   t218 = t215 int- t217
 413:   param t210                          (this)
 414:   param t213
 415:   param t218
 416:   call Point::Point(int, int), 3
 417:   c = t209
 418:   t56 = a[0]
 419:   t57 = a[4]
 420:   t58 = c[0]
 421:   t59 = c[4]
 422:   param t36                           (this)
 423:   param t35
 424:   t62 = call Point::operator<(const class Point &), 2
 425:   t63 = booltoint t62
 426:   param t35                           (this)
 427:   param t36
 428:   t66 = call Point::operator<(const class Point &), 2
 429:   t67 = booltoint t66
 430:   param "%d %d %d %d %d %d\n"
 431:   param t56
 432:   param t57
 433:   param t58
 434:   param t59
 435:   param t63
 436:   param t67
 437:   call printf, 7
 438:   t68 = &s
 439:   param t68                           (this)
 440:   param 1
 441:   param 2
 442:   param 4
 443:   param 6
 444:   call Segment::Segment(int, int, int, int), 5
 445:   t220 = t68 ptr+ 8
 446:   param t220                          (this)
 447:   param t68
 448:   t222 = call Point::operator-(const class Point &), 2
 449:   t223 = t222[0]
 450:   t224 = t223 int* t223
 451:   t225 = t222[4]
 452:   t226 = t225 int* t225
 453:   t227 = t224 int+ t226
 454:   t71 = s[12]
 455:   param "%d %d\n"
 456:   param t227
 457:   param t71
 458:   call printf, 3
 459:   t72 = &last
 460:   param t72                           (this)
 461:   call Shape::Shape(), 1
 462:   t231 = t72 ptr+ 4
 463:   *t231 = 2
 464:   t232 = t72 ptr+ 8
 465:   *t232 = 9
 466:   t235 = *t231
 467:   t238 = t235 int* 9
 468:   t77 = *t72
 469:   param "%d %d %d\n"
 470:   param t238
 471:   param 0
 472:   param t77
 473:   call printf, 4
 474:   t241 = *t72
 475:   param "~Shape %d\n"
 476:   param t241
 477:   call printf, 2
 478:   Shape::live = Shape::live int- 1
 479:   t79 = Shape::live
 480:   t243 = *t2
 481:   param "~Shape %d\n"
 482:   param t243
 483:   call printf, 2
 484:   Shape::live = Shape::live int- 1
 485:   t245 = *t1
 486:   param "~Shape %d\n"
 487:   param t245
 488:   call printf, 2
 489:   Shape::live = Shape::live int- 1
 490:   return t79


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Shape              class_tag      class Shape                -        global                         6     -     0     Shape                -                        size 4
Shape::id          field          int                        member   global > class Shape           8     4     6     Shape::id            -                        public, offset 0
Shape::live        field          int                        static   global > class Shape           9     4     6     Shape::live          -                        public, static
Shape::Shape       constructor    void (void)                -        global > class Shape           10    -     2     _ZN5ShapeC1Ev        _ZN5ShapeC1Ev            public
Shape::~Shape      destructor     void (void)                -        global > class Shape           11    -     0     _ZN5ShapeD1Ev        _ZN5ShapeD1Ev            public
Shape::area        method         int (void)                 -        global > class Shape           12    -     2     _ZN5Shape4areaEv     _ZN5Shape4areaEv         public, defined
Shape::name        method         int (void)                 -        global > class Shape           13    -     2     _ZN5Shape4nameEv     _ZN5Shape4nameEv         public, defined
Rect               class_tag      class Rect                 -        global                         17    -     0     Rect                 -                        size 12, public base Shape
Rect::w            field          int                        member   global > class Rect            19    4     8     Rect::w              -                        public, offset 4
Rect::h            field          int                        member   global > class Rect            19    4     6     Rect::h              -                        public, offset 8
Rect::Rect         constructor    void (int, int)            -        global > class Rect            20    -     2     _ZN4RectC1Eii        _ZN4RectC1Eii            public
Rect::Rect         constructor    void (void)                -        global > class Rect            21    -     2     _ZN4RectC1Ev         _ZN4RectC1Ev             public
Rect::area         method         int (void)                 -        global > class Rect            22    -     7     _ZN4Rect4areaEv      _ZN4Rect4areaEv          public, defined
Rect::perimeter    method         int (void)                 -        global > class Rect            23    -     2     _ZN4Rect9perimeterEv _ZN4Rect9perimeterEv     public, defined
a                  parameter      int                        param    global > class Rect > Rect()   20    4     1     a.1                  -                        
b                  parameter      int                        param    global > class Rect > Rect()   20    4     1     b.2                  -                        
Square             class_tag      class Square               -        global                         26    -     0     Square               -                        size 12, public base Rect
Square::Square     constructor    void (int)                 -        global > class Square          28    -     1     _ZN6SquareC1Ei       _ZN6SquareC1Ei           public
Square::name       method         int (void)                 -        global > class Square          29    -     1     _ZN6Square4nameEv    _ZN6Square4nameEv        public, defined
side               parameter      int                        param    global > class Square > Square() 28    4     2     side.3               -                        
Point              class_tag      class Point                -        global                         32    -     0     Point                -                        size 8
Point::x           field          int                        member   global > class Point           34    4     15    Point::x             -                        public, offset 0
Point::y           field          int                        member   global > class Point           34    4     16    Point::y             -                        public, offset 4
Point::Point       constructor    void (int, int)            -        global > class Point           35    -     5     _ZN5PointC1Eii       _ZN5PointC1Eii           public
Point::Point       constructor    void (void)                -        global > class Point           36    -     2     _ZN5PointC1Ev        _ZN5PointC1Ev            public
Point::operator+=  method         class Point &(const class Point &) -        global > class Point           37    -     3     _ZN5PointpLERKS_     _ZN5PointpLERKS_         public, defined
Point::operator-   method         class Point (const class Point &) -        global > class Point           38    -     2     _ZN5PointmiERKS_     _ZN5PointmiERKS_         public, defined
Point::operator<   method         bool (const class Point &) -        global > class Point           39    -     2     _ZN5PointltERKS_     _ZN5PointltERKS_         public, defined
Point::operator[]  method         int &(int)                 -        global > class Point           40    -     2     _ZN5PointixEi        _ZN5PointixEi            public, defined
a                  parameter      int                        param    global > class Point > Point() 35    4     1     a.4                  -                        
b                  parameter      int                        param    global > class Point > Point() 35    4     1     b.5                  -                        
o                  parameter      const class Point &        param    global > class Point > operator+=() 37    4     2     o.6                  -                        
o                  parameter      const class Point &        param    global > class Point > operator-() 38    4     2     o.7                  -                        
o                  parameter      const class Point &        param    global > class Point > operator<() 39    4     4     o.8                  -                        
i                  parameter      int                        param    global > class Point > operator[]() 40    4     1     i.9                  -                        
Segment            class_tag      class Segment              -        global                         43    -     0     Segment              -                        size 16
Segment::from      field          class Point                member   global > class Segment         45    8     2     Segment::from        -                        public, offset 0
Segment::to        field          class Point                member   global > class Segment         45    8     3     Segment::to          -                        public, offset 8
Segment::Segment   constructor    void (int, int, int, int)  -        global > class Segment         46    -     1     _ZN7SegmentC1Eiiii   _ZN7SegmentC1Eiiii       public
Segment::length2   method         int (void)                 -        global > class Segment         47    -     1     _ZN7Segment7length2Ev _ZN7Segment7length2Ev    public, defined
a                  parameter      int                        param    global > class Segment > Segment() 46    4     1     a.10                 -                        
b                  parameter      int                        param    global > class Segment > Segment() 46    4     1     b.11                 -                        
c                  parameter      int                        param    global > class Segment > Segment() 46    4     1     c.12                 -                        
d                  parameter      int                        param    global > class Segment > Segment() 46    4     1     d.13                 -                        
d                  variable       class Point                local    global > class Segment > length2() 47    8     4     d.14                 -                        
total              function       int (class Rect &)         -        global                         50    -     1     _Z5totalR4Rect       _Z5totalR4Rect           defined
r                  parameter      class Rect &               param    global > total()               50    4     2     r.15                 -                        
through            function       int (class Shape *)        -        global                         51    -     1     _Z7throughP5Shape    _Z7throughP5Shape        defined
s                  parameter      class Shape *              param    global > through()             51    4     2     s.16                 -                        
grow               function       void (class Rect *, int)   -        global                         52    -     1     _Z4growP4Recti       _Z4growP4Recti           defined
r                  parameter      class Rect *               param    global > grow()                52    4     2     r.17                 -                        
by                 parameter      int                        param    global > grow()                52    4     2     by.18                -                        
main               function       int (void)                 -        global                         54    -     0     main                 main                     defined
r                  variable       class Rect                 local    global > main()                55    12    2     r.19                 -                        
q                  variable       class Square               local    global > main()                56    12    8     q.20                 -                        
asShape            variable       class Shape *              local    global > main()                58    4     1     asShape.21           -                        
alias              variable       class Rect &               local    global > main()                61    4     2     alias.22             -                        
pair               variable       class Rect[2]              local    global > main() > block        65    24    4     pair.23              -                        
a                  variable       class Point                local    global > main()                71    8     9     a.24                 -                        
b                  variable       class Point                local    global > main()                71    8     6     b.25                 -                        
c                  variable       class Point                local    global > main()                75    8     2     c.26                 -                        
s                  variable       class Segment              local    global > main()                77    16    2     s.27                 -                        
last               variable       class Rect                 local    global > main() > block        81    12    2     last.28              -                        
base               variable       class Shape *              local    global > main() > block        82    4     2     base.29              -                        

=== Record Layouts ===
class Shape: size 4, align 4
    +0  int id  [public]
    static  int live  [public]
class Rect: size 12, align 4
    (base Shape, public)
    +4  int w  [public]
    +8  int h  [public]
class Square: size 12, align 4
    (base Rect, public)
class Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
class Segment: size 16, align 4
    +0  class Point from  [public]
    +8  class Point to  [public]
