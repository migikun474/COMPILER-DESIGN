=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t08_classes.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 306 -> 355 instruction(s) for 'test/t08_classes.c'.

optimization summary (-O3)
    instructions                306 -> 355   (-16% fewer)
    constants folded            1
    algebraic simplifications   1
    common subexpressions       36
    copies / constants forwarded 124
    temporaries merged away     8
    dead instructions removed   98
    jumps removed or redirected 4
    unreachable instructions    2
    propagated across blocks    3
    dead assignments removed    5
    calls inlined               33
    tail calls turned to jumps  0
    common across blocks        3
    moved out of loops          0

globals (name, type, width, initial value)
    Dog::made      int                        4  0

function Animal::Animal()        link name: _ZN6AnimalC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    total width 4
  code
 100:   *this = 4
 101:   param "Animal()\n"
 102:   call printf, 1
 103:   return

function Animal::~Animal()        link name: _ZN6AnimalD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    total width 4
  code
 104:   param "~Animal()\n"
 105:   call printf, 1
 106:   return

function Animal::count()        link name: _ZN6Animal5countEv
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    t1             temp   int                        4      4
    total width 8
  code
 107:   t1 = *this
 108:   return t1

function Tag::Tag()        link name: _ZN3TagC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    total width 4
  code
 109:   *this = 7
 110:   param "Tag()\n"
 111:   call printf, 1
 112:   return

function Tag::~Tag()        link name: _ZN3TagD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    total width 4
  code
 113:   param "~Tag()\n"
 114:   call printf, 1
 115:   return

function Dog::Dog(int)        link name: _ZN3DogC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    a              param  int                        4      4
    t1             temp   class Dog *                4      8
    t2             temp   class Dog *                4     12
    t3             temp   int                        4     16
    t4             temp   class Dog *                4     20
    t5             temp   int                        4     24
    t6             temp   class Animal *             4     28
    t7             temp   class Tag *                4     32
    total width 36
  code
 116:   *this = 4
 117:   param "Animal()\n"
 118:   call printf, 1
 119:   t1 = this ptr+ 8
 120:   *t1 = 7
 121:   param "Tag()\n"
 122:   call printf, 1
 123:   t2 = this ptr+ 4
 124:   *t2 = a
 125:   Dog::made = Dog::made int+ 1
 126:   t5 = *t2
 127:   param "Dog(%d)\n"
 128:   param t5
 129:   call printf, 2
 130:   return

function Dog::Dog()        link name: _ZN3DogC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   class Dog *                4      8
    t3             temp   int                        4     12
    t4             temp   class Animal *             4     16
    t5             temp   class Tag *                4     20
    total width 24
  code
 131:   *this = 4
 132:   param "Animal()\n"
 133:   call printf, 1
 134:   t1 = this ptr+ 8
 135:   *t1 = 7
 136:   param "Tag()\n"
 137:   call printf, 1
 138:   t2 = this ptr+ 4
 139:   *t2 = 0
 140:   Dog::made = Dog::made int+ 1
 141:   param "Dog()\n"
 142:   call printf, 1
 143:   return

function Dog::~Dog()        link name: _ZN3DogD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   class Dog *                4     12
    t4             temp   class Tag *                4     16
    t5             temp   class Animal *             4     20
    total width 24
  code
 144:   t1 = this ptr+ 4
 145:   t2 = *t1
 146:   param "~Dog(%d)\n"
 147:   param t2
 148:   call printf, 2
 149:   param "~Tag()\n"
 150:   call printf, 1
 151:   param "~Animal()\n"
 152:   call printf, 1
 153:   return

function Dog::human()        link name: _ZN3Dog5humanEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    t5             temp   int                        4     20
    t6             temp   class Dog *                4     24
    t7             temp   int                        4     28
    t8             temp   int                        4     32
    total width 36
  code
 154:   t1 = this ptr+ 4
 155:   t2 = *t1
 156:   t3 = t2 int* 7
 157:   t4 = *this
 158:   t5 = t3 int+ t4
 159:   t6 = this ptr+ 8
 160:   t7 = *t6
 161:   t8 = t5 int+ t7
 162:   return t8

function Dog::total()        link name: _ZN3Dog5totalEv
  code
 163:   return Dog::made

function Dog::birthday()        link name: _ZN3Dog8birthdayEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   class Dog *                4     16
    total width 20
  code
 164:   t1 = this ptr+ 4
 165:   t2 = *t1
 166:   t3 = t2 int+ 1
 167:   *t1 = t3
 168:   return

function Vec::Vec(int, int)        link name: _ZN3VecC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Vec *                4     12
    total width 16
  code
 169:   *this = a
 170:   t1 = this ptr+ 4
 171:   *t1 = b
 172:   return

function Vec::Vec()        link name: _ZN3VecC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   class Vec *                4      4
    total width 8
  code
 173:   *this = 0
 174:   t1 = this ptr+ 4
 175:   *t1 = 0
 176:   return

function Vec::operator+(class Vec)        link name: _ZN3VecplES_
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    o              param  class Vec                  8      4
    t1             temp   class Vec                  8     12
    t2             temp   class Vec *                4     20
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    t5             temp   int                        4     32
    t6             temp   class Vec *                4     36
    t7             temp   int                        4     40
    t8             temp   int                        4     44
    t9             temp   int                        4     48
    t10            temp   class Vec *                4     52
    t11            temp   int                        4     56
    t12            temp   int                        4     60
    t13            temp   class Vec *                4     64
    total width 68
  code
 177:   t2 = &t1
 178:   t3 = *this
 179:   t4 = o[0]
 180:   t5 = t3 int+ t4
 181:   t6 = this ptr+ 4
 182:   t7 = *t6
 183:   t8 = o[4]
 184:   t9 = t7 int+ t8
 185:   *t2 = t5
 186:   t13 = t2 ptr+ 4
 187:   *t13 = t9
 188:   return t1

function Vec::operator-()        link name: _ZN3VecmiEv
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   class Vec                  8      4
    t2             temp   class Vec *                4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   class Vec *                4     24
    t6             temp   int                        4     28
    t7             temp   int                        4     32
    t8             temp   class Vec *                4     36
    t9             temp   int                        4     40
    t10            temp   int                        4     44
    t11            temp   class Vec *                4     48
    total width 52
  code
 189:   t2 = &t1
 190:   t3 = *this
 191:   t4 = int- t3
 192:   t5 = this ptr+ 4
 193:   t6 = *t5
 194:   t7 = int- t6
 195:   *t2 = t4
 196:   t11 = t2 ptr+ 4
 197:   *t11 = t7
 198:   return t1

function Vec::operator==(class Vec)        link name: _ZN3VeceqES_
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    o              param  class Vec                  8      4
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   class Vec *                4     24
    t5             temp   int                        4     28
    t6             temp   int                        4     32
    total width 36
  code
 199:     t2 = *this
 200:     t3 = o[0]
 201:     if t2 int!= t3 goto L1
 202:     t4 = this ptr+ 4
 203:     t5 = *t4
 204:     t6 = o[4]
 205:     if t5 int== t6 goto L2
 206: L1: t1 = 0
 207:     goto L3
 208: L2: t1 = 1
 209: L3: return t1

function Vec::operator[](int)        link name: _ZN3VecixEi
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    i              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   class Vec *                4     16
    t4             temp   int                        4     20
    total width 24
  code
 210:     if i int!= 0 goto L4
 211:     t1 = *this
 212:     goto L5
 213: L4: t3 = this ptr+ 4
 214:     t1 = *t3
 215: L5: return t1

function Vec::operator+=(class Vec)        link name: _ZN3VecpLES_
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    o              param  class Vec                  8      4
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   class Vec *                4     24
    t5             temp   int                        4     28
    t6             temp   int                        4     32
    t7             temp   int                        4     36
    t8             temp   class Vec *                4     40
    total width 44
  code
 216:   t1 = *this
 217:   t2 = o[0]
 218:   t3 = t1 int+ t2
 219:   *this = t3
 220:   t4 = this ptr+ 4
 221:   t5 = *t4
 222:   t6 = o[4]
 223:   t7 = t5 int+ t6
 224:   *t4 = t7
 225:   return this

function Vec::operator++()        link name: _ZN3VecppEv
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 226:   t1 = *this
 227:   t2 = t1 int+ 1
 228:   *this = t2
 229:   return this

function Vec::operator()(int)        link name: _ZN3VecclEi
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    k              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   class Vec *                4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    total width 28
  code
 230:   t1 = *this
 231:   t2 = t1 int* k
 232:   t3 = this ptr+ 4
 233:   t4 = *t3
 234:   t5 = t2 int+ t4
 235:   return t5

function Vec::dot(class Vec)        link name: _ZN3Vec3dotES_
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    o              param  class Vec                  8      4
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   class Vec *                4     24
    t5             temp   int                        4     28
    t6             temp   int                        4     32
    t7             temp   int                        4     36
    t8             temp   int                        4     40
    total width 44
  code
 236:   t1 = *this
 237:   t2 = o[0]
 238:   t3 = t1 int* t2
 239:   t4 = this ptr+ 4
 240:   t5 = *t4
 241:   t6 = o[4]
 242:   t7 = t5 int* t6
 243:   t8 = t3 int+ t7
 244:   return t8

function operator*(class Vec, int)        link name: _Zml3Veci
  symbol table (name, kind, type, width, offset)
    v              param  class Vec                  8      0
    k              param  int                        4      8
    t1             temp   class Vec                  8     12
    t2             temp   class Vec *                4     20
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    t5             temp   int                        4     32
    t6             temp   int                        4     36
    t7             temp   class Vec *                4     40
    t8             temp   int                        4     44
    t9             temp   int                        4     48
    t10            temp   class Vec *                4     52
    total width 56
  code
 245:   t2 = &t1
 246:   t3 = v[0]
 247:   t4 = t3 int* k
 248:   t5 = v[4]
 249:   t6 = t5 int* k
 250:   *t2 = t4
 251:   t10 = t2 ptr+ 4
 252:   *t10 = t6
 253:   return t1

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    rex            local  class Dog                 12      0
    base           local  class Animal *             4     12
    other          local  class Dog                 12     16
    a              local  class Vec                  8     28
    b              local  class Vec                  8     36
    c              local  class Vec                  8     44
    d              local  class Vec                  8     52
    e              local  class Vec                  8     60
    row            local  class Vec[2]              16     68
    w              local  int                        4     84
    t1             temp   class Dog *                4     88
    t2             temp   class Dog *                4     92
    t3             temp   class Dog *                4     96
    t4             temp   int                        4    100
    t5             temp   class Dog *                4    104
    t6             temp   int                        4    108
    t7             temp   int                        4    112
    t8             temp   class Dog *                4    116
    t9             temp   int                        4    120
    t10            temp   class Dog *                4    124
    t11            temp   class Dog *                4    128
    t12            temp   class Dog *                4    132
    t13            temp   int                        4    136
    t14            temp   class Dog *                4    140
    t15            temp   class Vec *                4    144
    t16            temp   class Vec *                4    148
    t17            temp   class Vec *                4    152
    t18            temp   class Vec *                4    156
    t19            temp   class Vec                  8    160
    t20            temp   class Vec *                4    168
    t21            temp   class Vec *                4    172
    t22            temp   class Vec                  8    176
    t23            temp   class Vec *                4    184
    t24            temp   class Vec *                4    188
    t25            temp   class Vec                  8    192
    t26            temp   class Vec *                4    200
    t27            temp   class Vec *                4    204
    t28            temp   class Vec *                4    208
    t29            temp   class Vec &                4    212
    t30            temp   class Vec *                4    216
    t31            temp   class Vec &                4    220
    t32            temp   int                        4    224
    t33            temp   int                        4    228
    t34            temp   int                        4    232
    t35            temp   int                        4    236
    t36            temp   int                        4    240
    t37            temp   int                        4    244
    t38            temp   class Vec *                4    248
    t39            temp   int                        4    252
    t40            temp   class Vec *                4    256
    t41            temp   int                        4    260
    t42            temp   class Vec *                4    264
    t43            temp   int                        4    268
    t44            temp   class Vec *                4    272
    t45            temp   int                        4    276
    t46            temp   class Vec *                4    280
    t47            temp   int                        4    284
    t48            temp   class Vec (*)[2]           4    288
    t49            temp   class Vec (*)[2]           4    292
    t50            temp   int                        4    296
    t51            temp   int                        4    300
    t52            temp   int                        4    304
    t53            temp   int                        4    308
    t54            temp   class Dog *                4    312
    t55            temp   int                        4    316
    t56            temp   class Dog *                4    320
    t57            temp   class Dog *                4    324
    t58            temp   int                        4    328
    t59            temp   class Dog *                4    332
    t60            temp   class Dog *                4    336
    t61            temp   int                        4    340
    t62            temp   int                        4    344
    t63            temp   class Dog *                4    348
    t64            temp   class Dog *                4    352
    t65            temp   int                        4    356
    t66            temp   int                        4    360
    t67            temp   int                        4    364
    t68            temp   int                        4    368
    t69            temp   class Dog *                4    372
    t70            temp   int                        4    376
    t71            temp   int                        4    380
    t72            temp   class Animal *             4    384
    t73            temp   int                        4    388
    t74            temp   class Dog *                4    392
    t75            temp   class Dog *                4    396
    t76            temp   int                        4    400
    t77            temp   class Dog *                4    404
    t78            temp   class Dog *                4    408
    t79            temp   int                        4    412
    t80            temp   class Dog *                4    416
    t81            temp   class Dog *                4    420
    t82            temp   int                        4    424
    t83            temp   class Dog *                4    428
    t84            temp   class Dog *                4    432
    t85            temp   int                        4    436
    t86            temp   int                        4    440
    t87            temp   int                        4    444
    t88            temp   int                        4    448
    t89            temp   class Dog *                4    452
    t90            temp   int                        4    456
    t91            temp   int                        4    460
    t92            temp   class Dog *                4    464
    t93            temp   class Dog *                4    468
    t94            temp   int                        4    472
    t95            temp   class Dog *                4    476
    t96            temp   class Vec *                4    480
    t97            temp   int                        4    484
    t98            temp   int                        4    488
    t99            temp   class Vec *                4    492
    t100           temp   class Vec *                4    496
    t101           temp   int                        4    500
    t102           temp   int                        4    504
    t103           temp   class Vec *                4    508
    t104           temp   class Vec *                4    512
    t105           temp   class Vec *                4    516
    t106           temp   class Vec *                4    520
    t107           temp   class Vec                  8    524
    t108           temp   class Vec                  8    532
    t109           temp   class Vec *                4    540
    t110           temp   int                        4    544
    t111           temp   int                        4    548
    t112           temp   int                        4    552
    t113           temp   class Vec *                4    556
    t114           temp   int                        4    560
    t115           temp   int                        4    564
    t116           temp   int                        4    568
    t117           temp   class Vec *                4    572
    t118           temp   class Vec                  8    576
    t119           temp   class Vec *                4    584
    t120           temp   int                        4    588
    t121           temp   int                        4    592
    t122           temp   class Vec *                4    596
    t123           temp   int                        4    600
    t124           temp   int                        4    604
    t125           temp   class Vec                  8    608
    t126           temp   int                        4    616
    t127           temp   class Vec                  8    620
    t128           temp   class Vec *                4    628
    t129           temp   int                        4    632
    t130           temp   int                        4    636
    t131           temp   int                        4    640
    t132           temp   int                        4    644
    t133           temp   class Vec *                4    648
    t134           temp   class Vec                  8    652
    t135           temp   int                        4    660
    t136           temp   int                        4    664
    t137           temp   int                        4    668
    t138           temp   class Vec *                4    672
    t139           temp   int                        4    676
    t140           temp   int                        4    680
    t141           temp   int                        4    684
    t142           temp   class Vec *                4    688
    t143           temp   int                        4    692
    t144           temp   int                        4    696
    t145           temp   class Vec *                4    700
    t146           temp   class Vec                  8    704
    t147           temp   int                        4    712
    t148           temp   int                        4    716
    t149           temp   class Vec *                4    720
    t150           temp   int                        4    724
    t151           temp   int                        4    728
    t152           temp   int                        4    732
    t153           temp   class Vec *                4    736
    t154           temp   class Vec                  8    740
    t155           temp   int                        4    748
    t156           temp   int                        4    752
    t157           temp   class Vec *                4    756
    t158           temp   int                        4    760
    t159           temp   int                        4    764
    t160           temp   int                        4    768
    t161           temp   class Vec *                4    772
    t162           temp   int                        4    776
    t163           temp   int                        4    780
    t164           temp   class Vec *                4    784
    t165           temp   class Vec *                4    788
    t166           temp   int                        4    792
    t167           temp   int                        4    796
    t168           temp   int                        4    800
    t169           temp   class Vec *                4    804
    t170           temp   int                        4    808
    t171           temp   int                        4    812
    t172           temp   class Vec *                4    816
    t173           temp   class Vec                  8    820
    t174           temp   int                        4    828
    t175           temp   int                        4    832
    t176           temp   int                        4    836
    t177           temp   class Vec *                4    840
    t178           temp   int                        4    844
    t179           temp   int                        4    848
    t180           temp   int                        4    852
    t181           temp   int                        4    856
    t182           temp   class Vec *                4    860
    t183           temp   class Vec *                4    864
    t184           temp   class Vec *                4    868
    t185           temp   class Vec *                4    872
    total width 876
  code
 254:      t1 = &rex
 255:      param t1                            (this)
 256:      call Animal::Animal(), 1
 257:      t56 = t1 ptr+ 8
 258:      param t56                           (this)
 259:      call Tag::Tag(), 1
 260:      t57 = t1 ptr+ 4
 261:      *t57 = 3
 262:      Dog::made = Dog::made int+ 1
 263:      t58 = *t57
 264:      param "Dog(%d)\n"
 265:      param t58
 266:      call printf, 2
 267:      t61 = *t57
 268:      t62 = t61 int+ 1
 269:      *t57 = t62
 270:      t66 = t62 int* 7
 271:      t67 = *t1
 272:      t68 = t66 int+ t67
 273:      t70 = *t56
 274:      t71 = t68 int+ t70
 275:      param "%d %d %d\n"
 276:      param t71
 277:      param t67
 278:      param Dog::made
 279:      call printf, 4
 280:      t9 = *t1
 281:      param "%d\n"
 282:      param t9
 283:      call printf, 2
 284:      t76 = *t57
 285:      param "~Dog(%d)\n"
 286:      param t76
 287:      call printf, 2
 288:      param t56                           (this)
 289:      call Tag::~Tag(), 1
 290:      param t1                            (this)
 291:      call Animal::~Animal(), 1
 292:      param "--\n"
 293:      call printf, 1
 294:      t11 = &other
 295:      param t11                           (this)
 296:      call Animal::Animal(), 1
 297:      t80 = t11 ptr+ 8
 298:      param t80                           (this)
 299:      call Tag::Tag(), 1
 300:      t81 = t11 ptr+ 4
 301:      *t81 = 5
 302:      Dog::made = Dog::made int+ 1
 303:      t82 = *t81
 304:      param "Dog(%d)\n"
 305:      param t82
 306:      call printf, 2
 307:      t85 = *t81
 308:      t86 = t85 int* 7
 309:      t87 = *t11
 310:      t88 = t86 int+ t87
 311:      t90 = *t80
 312:      t91 = t88 int+ t90
 313:      param "%d %d\n"
 314:      param t91
 315:      param Dog::made
 316:      call printf, 3
 317:      t94 = *t81
 318:      param "~Dog(%d)\n"
 319:      param t94
 320:      call printf, 2
 321:      param t80                           (this)
 322:      call Tag::~Tag(), 1
 323:      param t11                           (this)
 324:      call Animal::~Animal(), 1
 325:      param "--\n"
 326:      call printf, 1
 327:      t15 = &a
 328:      *t15 = 1
 329:      t99 = t15 ptr+ 4
 330:      *t99 = 2
 331:      t16 = &b
 332:      *t16 = 3
 333:      t103 = t16 ptr+ 4
 334:      *t103 = 4
 335:      t17 = &c
 336:      *t17 = 0
 337:      t105 = t17 ptr+ 4
 338:      *t105 = 0
 339:      t107 = b
 340:      t109 = &t108
 341:      t110 = *t15
 342:      t111 = t107[0]
 343:      t112 = t110 int+ t111
 344:      t114 = *t99
 345:      t115 = t107[4]
 346:      t116 = t114 int+ t115
 347:      param t109                          (this)
 348:      param t112
 349:      param t116
 350:      call Vec::Vec(int, int), 3
 351:      c = t108
 352:      t119 = &t118
 353:      t120 = *t17
 354:      t121 = int- t120
 355:      t123 = *t105
 356:      t124 = int- t123
 357:      param t119                          (this)
 358:      param t121
 359:      param t124
 360:      call Vec::Vec(int, int), 3
 361:      d = t118
 362:      t125 = a
 363:      t128 = &t127
 364:      t129 = t125[0]
 365:      t130 = t129 int* 3
 366:      t131 = t125[4]
 367:      t132 = t131 int* 3
 368:      param t128                          (this)
 369:      param t130
 370:      param t132
 371:      call Vec::Vec(int, int), 3
 372:      e = t127
 373:      t134 = b
 374:      t135 = *t15
 375:      t136 = t134[0]
 376:      t137 = t135 int+ t136
 377:      *t15 = t137
 378:      t139 = *t99
 379:      t140 = t134[4]
 380:      t141 = t139 int+ t140
 381:      *t99 = t141
 382:      t143 = *t15
 383:      t144 = t143 int+ 1
 384:      *t15 = t144
 385:      t32 = c[0]
 386:      t33 = c[4]
 387:      t34 = d[0]
 388:      t35 = e[4]
 389:      t36 = a[0]
 390:      t37 = a[4]
 391:      param "%d %d %d %d %d %d\n"
 392:      param t32
 393:      param t33
 394:      param t34
 395:      param t35
 396:      param t36
 397:      param t37
 398:      call printf, 7
 399:      t146 = b
 400:      t147 = *t15
 401:      t148 = t146[0]
 402:      if t147 int!= t148 goto L6
 403:      t150 = *t99
 404:      t151 = t146[4]
 405:      if t150 int== t151 goto L7
 406: L6:  t152 = 0
 407:      goto L8
 408: L7:  t152 = 1
 409: L8:  t154 = c
 410:      t155 = *t17
 411:      t156 = t154[0]
 412:      if t155 int!= t156 goto L9
 413:      t158 = *t105
 414:      t159 = t154[4]
 415:      if t158 int== t159 goto L10
 416: L9:  t160 = 0
 417:      goto L11
 418: L10: t160 = 1
 419: L11: t163 = *t15
 420:      t168 = t163 int<< 1
 421:      t170 = *t99
 422:      t171 = t168 int+ t170
 423:      t173 = b
 424:      t174 = *t15
 425:      t175 = t173[0]
 426:      t176 = t174 int* t175
 427:      t178 = *t99
 428:      t179 = t173[4]
 429:      t180 = t178 int* t179
 430:      t181 = t176 int+ t180
 431:      param "%d %d %d %d %d\n"
 432:      param t152
 433:      param t160
 434:      param t163
 435:      param t171
 436:      param t181
 437:      call printf, 6
 438:      t48 = &row
 439:      *t48 = 0
 440:      t183 = t48 ptr+ 4
 441:      *t183 = 0
 442:      t49 = t48 ptr+ 8
 443:      *t49 = 0
 444:      t185 = t49 ptr+ 4
 445:      *t185 = 0
 446:      row[8] = 9
 447:      t50 = row[0]
 448:      param "%d %d\n"
 449:      param t50
 450:      param 9
 451:      call printf, 3
 452:      t52 = c[0]
 453:      t53 = 7 int+ t52
 454:      return t53


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Animal             class_tag      class Animal               -        global                         5     -     0     Animal               -                        size 4
Animal::legs       field          int                        member   global > class Animal          7     4     4     Animal::legs         -                        public, offset 0
Animal::Animal     constructor    void (void)                -        global > class Animal          8     -     2     _ZN6AnimalC1Ev       _ZN6AnimalC1Ev           public
Animal::~Animal    destructor     void (void)                -        global > class Animal          9     -     0     _ZN6AnimalD1Ev       _ZN6AnimalD1Ev           public
Animal::count      method         int (void)                 -        global > class Animal          10    -     1     _ZN6Animal5countEv   _ZN6Animal5countEv       public, defined
Tag                class_tag      class Tag                  -        global                         13    -     0     Tag                  -                        size 4
Tag::id            field          int                        member   global > class Tag             15    4     2     Tag::id              -                        public, offset 0
Tag::Tag           constructor    void (void)                -        global > class Tag             16    -     2     _ZN3TagC1Ev          _ZN3TagC1Ev              public
Tag::~Tag          destructor     void (void)                -        global > class Tag             17    -     0     _ZN3TagD1Ev          _ZN3TagD1Ev              public
Dog                class_tag      class Dog                  -        global                         20    -     0     Dog                  -                        size 12, public base Animal
Dog::age           field          int                        member   global > class Dog             22    4     7     Dog::age             -                        public, offset 4
Dog::tag           field          class Tag                  member   global > class Dog             23    4     1     Dog::tag             -                        public, offset 8
Dog::made          field          int                        static   global > class Dog             24    4     4     Dog::made            -                        public, static
Dog::Dog           constructor    void (int)                 -        global > class Dog             25    -     2     _ZN3DogC1Ei          _ZN3DogC1Ei              public
Dog::Dog           constructor    void (void)                -        global > class Dog             26    -     0     _ZN3DogC1Ev          _ZN3DogC1Ev              public
Dog::~Dog          destructor     void (void)                -        global > class Dog             27    -     0     _ZN3DogD1Ev          _ZN3DogD1Ev              public
Dog::human         method         int (void)                 -        global > class Dog             28    -     2     _ZN3Dog5humanEv      _ZN3Dog5humanEv          public, defined
Dog::birthday      method         void (void)                -        global > class Dog             29    -     1     _ZN3Dog8birthdayEv   _ZN3Dog8birthdayEv       public, defined
Dog::total         method         int (void)                 -        global > class Dog             30    -     1     _ZN3Dog5totalEv      _ZN3Dog5totalEv          public, static, defined
a                  parameter      int                        param    global > class Dog > Dog()     25    4     1     a.1                  -                        
Vec                class_tag      class Vec                  -        global                         35    -     0     Vec                  -                        size 8
Vec::x             field          int                        member   global > class Vec             37    4     22    Vec::x               -                        public, offset 0
Vec::y             field          int                        member   global > class Vec             38    4     17    Vec::y               -                        public, offset 4
Vec::Vec           constructor    void (int, int)            -        global > class Vec             39    -     5     _ZN3VecC1Eii         _ZN3VecC1Eii             public
Vec::Vec           constructor    void (void)                -        global > class Vec             40    -     2     _ZN3VecC1Ev          _ZN3VecC1Ev              public
Vec::operator+     method         class Vec (class Vec)      -        global > class Vec             41    -     1     _ZN3VecplES_         _ZN3VecplES_             public, defined
Vec::operator-     method         class Vec (void)           -        global > class Vec             42    -     1     _ZN3VecmiEv          _ZN3VecmiEv              public, defined
Vec::operator==    method         int (class Vec)            -        global > class Vec             43    -     2     _ZN3VeceqES_         _ZN3VeceqES_             public, defined
Vec::operator[]    method         int (int)                  -        global > class Vec             44    -     1     _ZN3VecixEi          _ZN3VecixEi              public, defined
Vec::operator+=    method         class Vec &(class Vec)     -        global > class Vec             45    -     1     _ZN3VecpLES_         _ZN3VecpLES_             public, defined
Vec::operator++    method         class Vec &(void)          -        global > class Vec             46    -     1     _ZN3VecppEv          _ZN3VecppEv              public, defined
Vec::operator()    method         int (int)                  -        global > class Vec             47    -     1     _ZN3VecclEi          _ZN3VecclEi              public, defined
Vec::dot           method         int (class Vec)            -        global > class Vec             48    -     1     _ZN3Vec3dotES_       _ZN3Vec3dotES_           public, defined
a                  parameter      int                        param    global > class Vec > Vec()     39    4     1     a.2                  -                        
b                  parameter      int                        param    global > class Vec > Vec()     39    4     1     b.3                  -                        
o                  parameter      class Vec                  param    global > class Vec > operator+() 41    8     2     o.4                  -                        
o                  parameter      class Vec                  param    global > class Vec > operator==() 43    8     2     o.5                  -                        
i                  parameter      int                        param    global > class Vec > operator[]() 44    4     1     i.6                  -                        
o                  parameter      class Vec                  param    global > class Vec > operator+=() 45    8     2     o.7                  -                        
k                  parameter      int                        param    global > class Vec > operator()() 47    4     1     k.8                  -                        
o                  parameter      class Vec                  param    global > class Vec > dot()     48    8     2     o.9                  -                        
operator*          function       class Vec (class Vec, int) -        global                         50    -     1     _Zml3Veci            _Zml3Veci                defined
v                  parameter      class Vec                  param    global > operator*()           50    8     2     v.10                 -                        
k                  parameter      int                        param    global > operator*()           50    4     2     k.11                 -                        
main               function       int (void)                 -        global                         52    -     0     main                 main                     defined
rex                variable       class Dog                  local    global > main() > block        54    12    4     rex.12               -                        
base               variable       class Animal *             local    global > main() > block        57    4     1     base.13              -                        
other              variable       class Dog                  local    global > main() > block        62    12    1     other.14             -                        
a                  variable       class Vec                  local    global > main()                67    8     10    a.15                 -                        
b                  variable       class Vec                  local    global > main()                67    8     4     b.16                 -                        
c                  variable       class Vec                  local    global > main()                67    8     7     c.17                 -                        
d                  variable       class Vec                  local    global > main()                69    8     1     d.18                 -                        
e                  variable       class Vec                  local    global > main()                70    8     1     e.19                 -                        
row                variable       class Vec[2]               local    global > main()                75    16    3     row.20               -                        
w                  variable       int                        local    global > main()                78    4     1     w.21                 -                        

=== Record Layouts ===
class Animal: size 4, align 4
    +0  int legs  [public]
class Tag: size 4, align 4
    +0  int id  [public]
class Dog: size 12, align 4
    (base Animal, public)
    +4  int age  [public]
    +8  class Tag tag  [public]
    static  int made  [public]
class Vec: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
