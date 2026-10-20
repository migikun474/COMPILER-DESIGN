=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t31_virtual.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 386 -> 358 instruction(s) for 'test/t31_virtual.c'.

optimization summary (-O1)
    instructions                386 -> 358   (7% fewer)
    constants folded            0
    algebraic simplifications   8
    common subexpressions       23
    copies / constants forwarded 33
    temporaries merged away     3
    dead instructions removed   23
    jumps removed or redirected 2
    unreachable instructions    0

globals (name, type, width, initial value)
    _ZTV6Animal    unsigned int[4]           16  { +0: &Animal::name(), +4: 0, +8: &Animal::speed(), +12: 0 }
    _ZTV3Dog       unsigned int[4]           16  { +0: &Dog::name(), +4: 0, +8: &Dog::speed(), +12: 0 }
    _ZTV5Puppy     unsigned int[4]           16  { +0: &Puppy::name(), +4: 0, +8: &Dog::speed(), +12: 0 }
    _ZTV7Swimmer   unsigned int[4]           16  { +0: &Swimmer::swim(), +4: 0, +8: &Swimmer::dive(int), +12: 0 }
    _ZTV4Seal      unsigned int[6]           24  { +0: &Seal::name(), +4: 0, +8: &Animal::speed(), +12: 0, +16: &Seal::swim(), +20: 0 }
    _ZTV4Seal_8    unsigned int[4]           16  { +0: &Seal::swim(), +4: -8, +8: &Swimmer::dive(int), +12: 0 }
    _ZTV5Shape     unsigned int[4]           16  { +0: 0, +4: 0, +8: &Shape::sides(), +12: 0 }
    _ZTV4Rect      unsigned int[4]           16  { +0: &Rect::area(), +4: 0, +8: &Rect::sides(), +12: 0 }
    _ZTV6Square    unsigned int[4]           16  { +0: &Square::area(), +4: 0, +8: &Rect::sides(), +12: 0 }

function Animal::Animal(int)        link name: _ZN6AnimalC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    n              param  int                        4      4
    t1             temp   unsigned int (*)[4]        4      8
    t2             temp   class Animal *             4     12
    t3             temp   class Animal *             4     16
    t4             temp   unsigned int *             4     20
    t5             temp   void *                     4     24
    t6             temp   unsigned int *             4     28
    t7             temp   int                        4     32
    t8             temp   class Animal *             4     36
    t9             temp   const char *               4     40
    total width 44
  code
 100:   t1 = &_ZTV6Animal
 101:   *this = t1
 102:   t2 = this ptr+ 4
 103:   *t2 = n
 104:   t4 = *this
 105:   t5 = *t4
 106:   t6 = t4 ptr+ 4
 107:   t7 = *t6
 108:   t8 = this ptr+ t7
 109:   param t8                            (this)
 110:   t9 = call *t5, 1                    (virtual Animal::name())
 111:   param "[A %s] "
 112:   param t9
 113:   call printf, 2
 114:   return

function Animal::~Animal()        link name: _ZN6AnimalD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    t1             temp   unsigned int (*)[4]        4      4
    t2             temp   unsigned int *             4      8
    t3             temp   void *                     4     12
    t4             temp   unsigned int *             4     16
    t5             temp   int                        4     20
    t6             temp   class Animal *             4     24
    t7             temp   const char *               4     28
    total width 32
  code
 115:   t1 = &_ZTV6Animal
 116:   *this = t1
 117:   t3 = *t1
 118:   t4 = t1 ptr+ 4
 119:   t5 = *t4
 120:   t6 = this ptr+ t5
 121:   param t6                            (this)
 122:   t7 = call *t3, 1                    (virtual Animal::name())
 123:   param "[~A %s] "
 124:   param t7
 125:   call printf, 2
 126:   return

function Animal::name()        link name: _ZNK6Animal4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    total width 4
  code
 127:   return "animal"

function Animal::speed()        link name: _ZN6Animal5speedEv
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    t1             temp   class Animal *             4      4
    t2             temp   int                        4      8
    total width 12
  code
 128:   t1 = this ptr+ 4
 129:   t2 = *t1
 130:   return t2

function Animal::describe()        link name: _ZN6Animal8describeEv
  symbol table (name, kind, type, width, offset)
    this           param  class Animal *             4      0
    t1             temp   unsigned int *             4      4
    t2             temp   unsigned int *             4      8
    t3             temp   void *                     4     12
    t4             temp   unsigned int *             4     16
    t5             temp   int                        4     20
    t6             temp   class Animal *             4     24
    t7             temp   int                        4     28
    t8             temp   int                        4     32
    t9             temp   class Animal *             4     36
    t10            temp   int                        4     40
    t11            temp   int                        4     44
    total width 48
  code
 131:   t1 = *this
 132:   t2 = t1 ptr+ 8
 133:   t3 = *t2
 134:   t4 = t1 ptr+ 12
 135:   t5 = *t4
 136:   t6 = this ptr+ t5
 137:   param t6                            (this)
 138:   t7 = call *t3, 1                    (virtual Animal::speed())
 139:   t8 = t7 int* 10
 140:   t9 = this ptr+ 4
 141:   t10 = *t9
 142:   t11 = t8 int+ t10
 143:   return t11

function Dog::Dog(int)        link name: _ZN3DogC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    b              param  int                        4      4
    t1             temp   unsigned int (*)[4]        4      8
    t2             temp   class Dog *                4     12
    t3             temp   class Dog *                4     16
    t4             temp   unsigned int *             4     20
    t5             temp   void *                     4     24
    t6             temp   unsigned int *             4     28
    t7             temp   int                        4     32
    t8             temp   class Dog *                4     36
    t9             temp   const char *               4     40
    total width 44
  code
 144:   param this                          (this)
 145:   param 4
 146:   call Animal::Animal(int), 2
 147:   t1 = &_ZTV3Dog
 148:   *this = t1
 149:   t2 = this ptr+ 8
 150:   *t2 = b
 151:   t4 = *this
 152:   t5 = *t4
 153:   t6 = t4 ptr+ 4
 154:   t7 = *t6
 155:   t8 = this ptr+ t7
 156:   param t8                            (this)
 157:   t9 = call *t5, 1                    (virtual Dog::name())
 158:   param "[D %s] "
 159:   param t9
 160:   call printf, 2
 161:   return

function Dog::~Dog()        link name: _ZN3DogD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   unsigned int (*)[4]        4      4
    t2             temp   unsigned int *             4      8
    t3             temp   void *                     4     12
    t4             temp   unsigned int *             4     16
    t5             temp   int                        4     20
    t6             temp   class Dog *                4     24
    t7             temp   const char *               4     28
    total width 32
  code
 162:   t1 = &_ZTV3Dog
 163:   *this = t1
 164:   t3 = *t1
 165:   t4 = t1 ptr+ 4
 166:   t5 = *t4
 167:   t6 = this ptr+ t5
 168:   param t6                            (this)
 169:   t7 = call *t3, 1                    (virtual Dog::name())
 170:   param "[~D %s] "
 171:   param t7
 172:   call printf, 2
 173:   param this                          (this)
 174:   call Animal::~Animal(), 1
 175:   return

function Dog::name()        link name: _ZNK3Dog4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    total width 4
  code
 176:   return "dog"

function Dog::speed()        link name: _ZN3Dog5speedEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    total width 16
  code
 177:   t1 = this ptr+ 8
 178:   t2 = *t1
 179:   t3 = 12 int+ t2
 180:   return t3

function Puppy::Puppy()        link name: _ZN5PuppyC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Puppy *              4      0
    t1             temp   unsigned int (*)[4]        4      4
    total width 8
  code
 181:   param this                          (this)
 182:   param 1
 183:   call Dog::Dog(int), 2
 184:   t1 = &_ZTV5Puppy
 185:   *this = t1
 186:   return

function Puppy::name()        link name: _ZNK5Puppy4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Puppy *              4      0
    total width 4
  code
 187:   return "puppy"

function Swimmer::Swimmer()        link name: _ZN7SwimmerC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Swimmer *            4      0
    t1             temp   unsigned int (*)[4]        4      4
    t2             temp   class Swimmer *            4      8
    t3             temp   class Swimmer *            4     12
    total width 16
  code
 188:   t1 = &_ZTV7Swimmer
 189:   *this = t1
 190:   t2 = this ptr+ 4
 191:   *t2 = 3
 192:   return

function Swimmer::swim()        link name: _ZN7Swimmer4swimEv
  symbol table (name, kind, type, width, offset)
    this           param  class Swimmer *            4      0
    t1             temp   class Swimmer *            4      4
    t2             temp   int                        4      8
    total width 12
  code
 193:   t1 = this ptr+ 4
 194:   t2 = *t1
 195:   return t2

function Swimmer::dive(int)        link name: _ZN7Swimmer4diveEi
  symbol table (name, kind, type, width, offset)
    this           param  class Swimmer *            4      0
    m              param  int                        4      4
    t1             temp   class Swimmer *            4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 196:   t1 = this ptr+ 4
 197:   t2 = *t1
 198:   t3 = t2 int+ m
 199:   return t3

function Seal::Seal()        link name: _ZN4SealC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Seal *               4      0
    t1             temp   class Seal *               4      4
    t2             temp   unsigned int (*)[6]        4      8
    t3             temp   unsigned int (*)[4]        4     12
    t4             temp   class Seal *               4     16
    t5             temp   class Seal *               4     20
    t6             temp   class Seal *               4     24
    total width 28
  code
 200:   param this                          (this)
 201:   param 0
 202:   call Animal::Animal(int), 2
 203:   t1 = this ptr+ 8
 204:   param t1                            (this)
 205:   call Swimmer::Swimmer(), 1
 206:   t2 = &_ZTV4Seal
 207:   *this = t2
 208:   t3 = &_ZTV4Seal_8
 209:   *t1 = t3
 210:   t5 = this ptr+ 16
 211:   *t5 = 7
 212:   return

function Seal::name()        link name: _ZNK4Seal4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Seal *               4      0
    total width 4
  code
 213:   return "seal"

function Seal::swim()        link name: _ZN4Seal4swimEv
  symbol table (name, kind, type, width, offset)
    this           param  class Seal *               4      0
    t1             temp   class Seal *               4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   class Seal *               4     16
    t5             temp   int                        4     20
    t6             temp   int                        4     24
    total width 28
  code
 214:   t1 = this ptr+ 16
 215:   t2 = *t1
 216:   t3 = t2 int<< 1
 217:   t4 = this ptr+ 12
 218:   t5 = *t4
 219:   t6 = t3 int+ t5
 220:   return t6

function Shape::sides()        link name: _ZN5Shape5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 221:   return 0

function Shape::twice()        link name: _ZN5Shape5twiceEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    t1             temp   unsigned int *             4      4
    t2             temp   void *                     4      8
    t3             temp   unsigned int *             4     12
    t4             temp   int                        4     16
    t5             temp   class Shape *              4     20
    t6             temp   int                        4     24
    t7             temp   int                        4     28
    total width 32
  code
 222:   t1 = *this
 223:   t2 = *t1
 224:   t3 = t1 ptr+ 4
 225:   t4 = *t3
 226:   t5 = this ptr+ t4
 227:   param t5                            (this)
 228:   t6 = call *t2, 1                    (virtual Shape::area())
 229:   t7 = t6 int<< 1
 230:   return t7

function Rect::Rect(int, int)        link name: _ZN4RectC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   unsigned int (*)[4]        4     12
    t2             temp   unsigned int (*)[4]        4     16
    t3             temp   class Rect *               4     20
    t4             temp   class Rect *               4     24
    t5             temp   class Rect *               4     28
    t6             temp   class Rect *               4     32
    total width 36
  code
 231:   t1 = &_ZTV5Shape
 232:   *this = t1
 233:   t2 = &_ZTV4Rect
 234:   *this = t2
 235:   t3 = this ptr+ 4
 236:   *t3 = a
 237:   t5 = this ptr+ 8
 238:   *t5 = b
 239:   return

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
 240:   t1 = this ptr+ 4
 241:   t2 = *t1
 242:   t3 = this ptr+ 8
 243:   t4 = *t3
 244:   t5 = t2 int* t4
 245:   return t5

function Rect::sides()        link name: _ZN4Rect5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    total width 4
  code
 246:   return 4

function Square::Square(int)        link name: _ZN6SquareC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    s              param  int                        4      4
    t1             temp   unsigned int (*)[4]        4      8
    total width 12
  code
 247:   param this                          (this)
 248:   param s
 249:   param s
 250:   call Rect::Rect(int, int), 3
 251:   t1 = &_ZTV6Square
 252:   *this = t1
 253:   return

function Square::area()        link name: _ZN6Square4areaEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 254:   param this                          (this)
 255:   t1 = call Rect::area(), 1
 256:   t2 = t1 int+ 1
 257:   return t2

function total(class Shape &)        link name: _Z5totalR5Shape
  symbol table (name, kind, type, width, offset)
    s              param  class Shape &              4      0
    t1             temp   unsigned int *             4      4
    t2             temp   void *                     4      8
    t3             temp   unsigned int *             4     12
    t4             temp   int                        4     16
    t5             temp   class Shape *              4     20
    t6             temp   int                        4     24
    t7             temp   unsigned int *             4     28
    t8             temp   unsigned int *             4     32
    t9             temp   void *                     4     36
    t10            temp   unsigned int *             4     40
    t11            temp   int                        4     44
    t12            temp   class Shape *              4     48
    t13            temp   int                        4     52
    t14            temp   int                        4     56
    total width 60
  code
 258:   t1 = *s
 259:   t2 = *t1
 260:   t3 = t1 ptr+ 4
 261:   t4 = *t3
 262:   t5 = s ptr+ t4
 263:   param t5                            (this)
 264:   t6 = call *t2, 1                    (virtual Shape::area())
 265:   t7 = *s
 266:   t8 = t7 ptr+ 8
 267:   t9 = *t8
 268:   t10 = t7 ptr+ 12
 269:   t11 = *t10
 270:   t12 = s ptr+ t11
 271:   param t12                           (this)
 272:   t13 = call *t9, 1                   (virtual Shape::sides())
 273:   t14 = t6 int+ t13
 274:   return t14

function race(class Animal *)        link name: _Z4raceP6Animal
  symbol table (name, kind, type, width, offset)
    a              param  class Animal *             4      0
    t1             temp   unsigned int *             4      4
    t2             temp   unsigned int *             4      8
    t3             temp   void *                     4     12
    t4             temp   unsigned int *             4     16
    t5             temp   int                        4     20
    t6             temp   class Animal *             4     24
    t7             temp   int                        4     28
    total width 32
  code
 275:   t1 = *a
 276:   t2 = t1 ptr+ 8
 277:   t3 = *t2
 278:   t4 = t1 ptr+ 12
 279:   t5 = *t4
 280:   t6 = a ptr+ t5
 281:   param t6                            (this)
 282:   t7 = call *t3, 1                    (virtual Animal::speed())
 283:   return t7

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    d              local  class Dog                 12      0
    p              local  class Puppy               12     12
    zoo            local  class Animal *[3]         12     24
    s              local  class Seal                20     36
    i.13           local  int                        4     56
    w              local  class Swimmer *            4     60
    ref            local  class Animal &             4     64
    copy           local  class Animal               8     68
    r              local  class Rect                12     76
    sq             local  class Square              12     88
    shapes         local  class Shape *[2]           8    100
    i.20           local  int                        4    108
    t1             temp   class Dog *                4    112
    t2             temp   class Puppy *              4    116
    t3             temp   class Dog *                4    120
    t4             temp   class Puppy *              4    124
    t5             temp   class Seal *               4    128
    t6             temp   class Seal *               4    132
    t7             temp   int                        4    136
    t8             temp   class Animal *             4    140
    t9             temp   unsigned int *             4    144
    t10            temp   void *                     4    148
    t11            temp   unsigned int *             4    152
    t12            temp   int                        4    156
    t13            temp   class Animal *             4    160
    t14            temp   const char *               4    164
    t15            temp   int                        4    168
    t16            temp   class Animal *             4    172
    t17            temp   unsigned int *             4    176
    t18            temp   unsigned int *             4    180
    t19            temp   void *                     4    184
    t20            temp   unsigned int *             4    188
    t21            temp   int                        4    192
    t22            temp   class Animal *             4    196
    t23            temp   int                        4    200
    t24            temp   int                        4    204
    t25            temp   class Animal *             4    208
    t26            temp   int                        4    212
    t27            temp   int                        4    216
    t28            temp   class Seal *               4    220
    t29            temp   class Swimmer *            4    224
    t30            temp   unsigned int *             4    228
    t31            temp   void *                     4    232
    t32            temp   unsigned int *             4    236
    t33            temp   int                        4    240
    t34            temp   class Swimmer *            4    244
    t35            temp   int                        4    248
    t36            temp   unsigned int *             4    252
    t37            temp   unsigned int *             4    256
    t38            temp   void *                     4    260
    t39            temp   unsigned int *             4    264
    t40            temp   int                        4    268
    t41            temp   class Swimmer *            4    272
    t42            temp   int                        4    276
    t43            temp   class Seal *               4    280
    t44            temp   int                        4    284
    t45            temp   class Puppy *              4    288
    t46            temp   unsigned int *             4    292
    t47            temp   void *                     4    296
    t48            temp   unsigned int *             4    300
    t49            temp   int                        4    304
    t50            temp   class Animal *             4    308
    t51            temp   const char *               4    312
    t52            temp   int                        4    316
    t53            temp   class Dog *                4    320
    t54            temp   int                        4    324
    t55            temp   class Animal               8    328
    t56            temp   class Animal *             4    336
    t57            temp   unsigned int (*)[4]        4    340
    t58            temp   class Animal *             4    344
    t59            temp   const char *               4    348
    t60            temp   class Animal *             4    352
    t61            temp   int                        4    356
    t62            temp   class Animal               8    360
    t63            temp   class Animal *             4    368
    t64            temp   unsigned int *             4    372
    t65            temp   class Animal *             4    376
    t66            temp   const char *               4    380
    t67            temp   class Animal *             4    384
    t68            temp   int                        4    388
    t69            temp   class Rect *               4    392
    t70            temp   class Square *             4    396
    t71            temp   class Rect *               4    400
    t72            temp   class Square *             4    404
    t73            temp   int                        4    408
    t74            temp   class Shape *              4    412
    t75            temp   unsigned int *             4    416
    t76            temp   void *                     4    420
    t77            temp   unsigned int *             4    424
    t78            temp   int                        4    428
    t79            temp   class Shape *              4    432
    t80            temp   int                        4    436
    t81            temp   int                        4    440
    t82            temp   class Shape *              4    444
    t83            temp   int                        4    448
    t84            temp   int                        4    452
    t85            temp   class Shape *              4    456
    t86            temp   int                        4    460
    t87            temp   int                        4    464
    t88            temp   class Animal *             4    468
    t89            temp   class Seal *               4    472
    t90            temp   class Puppy *              4    476
    t91            temp   class Dog *                4    480
    total width 484
  code
 284:     t1 = &d
 285:     param t1                            (this)
 286:     param 5
 287:     call Dog::Dog(int), 2
 288:     param "\n"
 289:     call printf, 1
 290:     t2 = &p
 291:     param t2                            (this)
 292:     call Puppy::Puppy(), 1
 293:     param "\n"
 294:     call printf, 1
 295:     zoo[0] = t1
 296:     zoo[4] = t2
 297:     zoo[8] = 0
 298:     t5 = &s
 299:     param t5                            (this)
 300:     call Seal::Seal(), 1
 301:     zoo[8] = t5
 302:     param "\n"
 303:     call printf, 1
 304:     i.13 = 0
 305: L1: if i.13 int>= 3 goto L2
 306:     t7 = i.13 int<< 2                   (w = 4)
 307:     t8 = zoo[t7]
 308:     t9 = *t8
 309:     t10 = *t9
 310:     t11 = t9 ptr+ 4
 311:     t12 = *t11
 312:     t13 = t8 ptr+ t12
 313:     param t13                           (this)
 314:     t14 = call *t10, 1                  (virtual Animal::name())
 315:     t16 = zoo[t7]
 316:     t17 = *t16
 317:     t18 = t17 ptr+ 8
 318:     t19 = *t18
 319:     t20 = t17 ptr+ 12
 320:     t21 = *t20
 321:     t22 = t16 ptr+ t21
 322:     param t22                           (this)
 323:     t23 = call *t19, 1                  (virtual Animal::speed())
 324:     t25 = zoo[t7]
 325:     param t25                           (this)
 326:     t26 = call Animal::describe(), 1
 327:     param "%s %d %d | "
 328:     param t14
 329:     param t23
 330:     param t26
 331:     call printf, 4
 332:     i.13 = i.13 int+ 1
 333:     goto L1
 334: L2: param "\n"
 335:     call printf, 1
 336:     t28 = &s
 337:     t29 = t28
 338:     if t28 ptr== 0 goto L3
 339:     t29 = t28 ptr+ 8
 340: L3: w = t29
 341:     t30 = *t29
 342:     t31 = *t30
 343:     t32 = t30 ptr+ 4
 344:     t33 = *t32
 345:     t34 = t29 ptr+ t33
 346:     param t34                           (this)
 347:     t35 = call *t31, 1                  (virtual Swimmer::swim())
 348:     t36 = *t29
 349:     t37 = t36 ptr+ 8
 350:     t38 = *t37
 351:     t39 = t36 ptr+ 12
 352:     t40 = *t39
 353:     t41 = t29 ptr+ t40
 354:     param t41                           (this)
 355:     param 2
 356:     t42 = call *t38, 2                  (virtual Swimmer::dive(int))
 357:     t43 = &s
 358:     param t43
 359:     t44 = call race(class Animal *), 1
 360:     param "%d %d %d\n"
 361:     param t35
 362:     param t42
 363:     param t44
 364:     call printf, 4
 365:     t45 = &p
 366:     ref = t45
 367:     t46 = *t45
 368:     t47 = *t46
 369:     t48 = t46 ptr+ 4
 370:     t49 = *t48
 371:     t50 = t45 ptr+ t49
 372:     param t50                           (this)
 373:     t51 = call *t47, 1                  (virtual Animal::name())
 374:     param t45                           (this)
 375:     t52 = call Animal::speed(), 1
 376:     t53 = &d
 377:     param t53                           (this)
 378:     t54 = call Animal::speed(), 1
 379:     param "%s %d %d\n"
 380:     param t51
 381:     param t52
 382:     param t54
 383:     call printf, 4
 384:     copy = d[0]
 385:     t56 = &copy
 386:     t57 = &_ZTV6Animal
 387:     *t56 = t57
 388:     param t56                           (this)
 389:     t59 = call Animal::name(), 1
 390:     param t56                           (this)
 391:     t61 = call Animal::speed(), 1
 392:     param "%s %d\n"
 393:     param t59
 394:     param t61
 395:     call printf, 3
 396:     t62 = p[0]
 397:     t64 = *t56
 398:     copy = t62
 399:     *t56 = t64
 400:     param t56                           (this)
 401:     t66 = call Animal::name(), 1
 402:     param t56                           (this)
 403:     t68 = call Animal::speed(), 1
 404:     param "%s %d\n"
 405:     param t66
 406:     param t68
 407:     call printf, 3
 408:     t69 = &r
 409:     param t69                           (this)
 410:     param 2
 411:     param 3
 412:     call Rect::Rect(int, int), 3
 413:     t70 = &sq
 414:     param t70                           (this)
 415:     param 4
 416:     call Square::Square(int), 2
 417:     shapes[0] = t69
 418:     shapes[4] = t70
 419:     i.20 = 0
 420: L4: if i.20 int>= 2 goto L5
 421:     t73 = i.20 int<< 2                  (w = 4)
 422:     t74 = shapes[t73]
 423:     t75 = *t74
 424:     t76 = *t75
 425:     t77 = t75 ptr+ 4
 426:     t78 = *t77
 427:     t79 = t74 ptr+ t78
 428:     param t79                           (this)
 429:     t80 = call *t76, 1                  (virtual Shape::area())
 430:     t82 = shapes[t73]
 431:     param t82                           (this)
 432:     t83 = call Shape::twice(), 1
 433:     t85 = shapes[t73]
 434:     param t85
 435:     t86 = call total(class Shape &), 1
 436:     param "%d %d %d | "
 437:     param t80
 438:     param t83
 439:     param t86
 440:     call printf, 4
 441:     i.20 = i.20 int+ 1
 442:     goto L4
 443: L5: param "\n"
 444:     call printf, 1
 445:     t88 = &copy
 446:     param t88                           (this)
 447:     call Animal::~Animal(), 1
 448:     t89 = &s
 449:     param t89                           (this)
 450:     call Animal::~Animal(), 1
 451:     t90 = &p
 452:     param t90                           (this)
 453:     call Dog::~Dog(), 1
 454:     t91 = &d
 455:     param t91                           (this)
 456:     call Dog::~Dog(), 1
 457:     return 0


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Animal             class_tag      class Animal               -        global                         6     -     0     Animal               -                        size 8
Animal::legs       field          int                        member   global > class Animal          8     4     2     Animal::legs         -                        public, offset 4
Animal::Animal     constructor    void (int)                 -        global > class Animal          9     -     2     _ZN6AnimalC1Ei       _ZN6AnimalC1Ei           public
Animal::~Animal    destructor     void (void)                -        global > class Animal          10    -     0     _ZN6AnimalD1Ev       _ZN6AnimalD1Ev           public
Animal::name       method         const char *(void) const   -        global > class Animal          11    -     6     _ZNK6Animal4nameEv   _ZNK6Animal4nameEv       public, defined
Animal::speed      method         int (void)                 -        global > class Animal          12    -     7     _ZN6Animal5speedEv   _ZN6Animal5speedEv       public, defined
Animal::describe   method         int (void)                 -        global > class Animal          13    -     1     _ZN6Animal8describeEv _ZN6Animal8describeEv    public, defined
n                  parameter      int                        param    global > class Animal > Animal() 9     4     1     n.1                  -                        
Dog                class_tag      class Dog                  -        global                         16    -     0     Dog                  -                        size 12, public base Animal
Dog::bark          field          int                        member   global > class Dog             18    4     1     Dog::bark            -                        public, offset 8
Dog::Dog           constructor    void (int)                 -        global > class Dog             19    -     2     _ZN3DogC1Ei          _ZN3DogC1Ei              public
Dog::~Dog          destructor     void (void)                -        global > class Dog             20    -     0     _ZN3DogD1Ev          _ZN3DogD1Ev              public
Dog::name          method         const char *(void) const   -        global > class Dog             21    -     2     _ZNK3Dog4nameEv      _ZNK3Dog4nameEv          public, defined
Dog::speed         method         int (void)                 -        global > class Dog             22    -     0     _ZN3Dog5speedEv      _ZN3Dog5speedEv          public, defined
b                  parameter      int                        param    global > class Dog > Dog()     19    4     1     b.2                  -                        
Puppy              class_tag      class Puppy                -        global                         25    -     0     Puppy                -                        size 12, public base Dog
Puppy::Puppy       constructor    void (void)                -        global > class Puppy           27    -     1     _ZN5PuppyC1Ev        _ZN5PuppyC1Ev            public
Puppy::name        method         const char *(void) const   -        global > class Puppy           28    -     0     _ZNK5Puppy4nameEv    _ZNK5Puppy4nameEv        public, defined
Swimmer            class_tag      class Swimmer              -        global                         31    -     0     Swimmer              -                        size 8
Swimmer::depth     field          int                        member   global > class Swimmer         33    4     3     Swimmer::depth       -                        public, offset 4
Swimmer::Swimmer   constructor    void (void)                -        global > class Swimmer         34    -     1     _ZN7SwimmerC1Ev      _ZN7SwimmerC1Ev          public
Swimmer::swim      method         int (void)                 -        global > class Swimmer         35    -     1     _ZN7Swimmer4swimEv   _ZN7Swimmer4swimEv       public, defined
Swimmer::dive      method         int (int)                  -        global > class Swimmer         36    -     1     _ZN7Swimmer4diveEi   _ZN7Swimmer4diveEi       public, defined
m                  parameter      int                        param    global > class Swimmer > dive() 36    4     1     m.3                  -                        
Seal               class_tag      class Seal                 -        global                         39    -     0     Seal                 -                        size 20, public base Animal, public base Swimmer
Seal::fat          field          int                        member   global > class Seal            41    4     1     Seal::fat            -                        public, offset 16
Seal::Seal         constructor    void (void)                -        global > class Seal            42    -     1     _ZN4SealC1Ev         _ZN4SealC1Ev             public
Seal::name         method         const char *(void) const   -        global > class Seal            43    -     0     _ZNK4Seal4nameEv     _ZNK4Seal4nameEv         public, defined
Seal::swim         method         int (void)                 -        global > class Seal            44    -     0     _ZN4Seal4swimEv      _ZN4Seal4swimEv          public, defined
Shape              class_tag      class Shape                -        global                         47    -     0     Shape                -                        size 4
Shape::area        method         int (void)                 -        global > class Shape           49    -     3     _ZN5Shape4areaEv     _ZN5Shape4areaEv         public, declared only
Shape::sides       method         int (void)                 -        global > class Shape           50    -     1     _ZN5Shape5sidesEv    _ZN5Shape5sidesEv        public, defined
Shape::twice       method         int (void)                 -        global > class Shape           51    -     1     _ZN5Shape5twiceEv    _ZN5Shape5twiceEv        public, defined
Rect               class_tag      class Rect                 -        global                         53    -     0     Rect                 -                        size 12, public base Shape
Rect::w            field          int                        member   global > class Rect            55    4     1     Rect::w              -                        public, offset 4
Rect::h            field          int                        member   global > class Rect            55    4     1     Rect::h              -                        public, offset 8
Rect::Rect         constructor    void (int, int)            -        global > class Rect            56    -     2     _ZN4RectC1Eii        _ZN4RectC1Eii            public
Rect::area         method         int (void)                 -        global > class Rect            57    -     1     _ZN4Rect4areaEv      _ZN4Rect4areaEv          public, defined
Rect::sides        method         int (void)                 -        global > class Rect            58    -     0     _ZN4Rect5sidesEv     _ZN4Rect5sidesEv         public, defined
a                  parameter      int                        param    global > class Rect > Rect()   56    4     1     a.4                  -                        
b                  parameter      int                        param    global > class Rect > Rect()   56    4     1     b.5                  -                        
Square             class_tag      class Square               -        global                         60    -     0     Square               -                        size 12, public base Rect
Square::Square     constructor    void (int)                 -        global > class Square          62    -     1     _ZN6SquareC1Ei       _ZN6SquareC1Ei           public
Square::area       method         int (void)                 -        global > class Square          63    -     0     _ZN6Square4areaEv    _ZN6Square4areaEv        public, defined
s                  parameter      int                        param    global > class Square > Square() 62    4     2     s.6                  -                        
total              function       int (class Shape &)        -        global                         66    -     1     _Z5totalR5Shape      _Z5totalR5Shape          defined
s                  parameter      class Shape &              param    global > total()               66    4     2     s.7                  -                        
race               function       int (class Animal *)       -        global                         67    -     1     _Z4raceP6Animal      _Z4raceP6Animal          defined
a                  parameter      class Animal *             param    global > race()                67    4     1     a.8                  -                        
main               function       int (void)                 -        global                         69    -     0     main                 main                     defined
d                  variable       class Dog                  local    global > main()                70    12    3     d.9                  -                        
p                  variable       class Puppy                local    global > main()                72    12    3     p.10                 -                        
zoo                variable       class Animal *[3]          local    global > main()                74    12    4     zoo.11               -                        
s                  variable       class Seal                 local    global > main()                75    20    3     s.12                 -                        
i                  variable       int                        local    global > main() > for          78    4     5     i.13                 -                        
w                  variable       class Swimmer *            local    global > main()                80    4     2     w.14                 -                        
ref                variable       class Animal &             local    global > main()                82    4     2     ref.15               -                        
copy               variable       class Animal               local    global > main()                84    8     5     copy.16              -                        
r                  variable       class Rect                 local    global > main()                88    12    1     r.17                 -                        
sq                 variable       class Square               local    global > main()                89    12    1     sq.18                -                        
shapes             variable       class Shape *[2]           local    global > main()                90    8     3     shapes.19            -                        
i                  variable       int                        local    global > main() > for          91    4     5     i.20                 -                        

=== Record Layouts ===
class Animal: size 8, align 4
    +4  int legs  [public]
class Dog: size 12, align 4
    (base Animal, public)
    +8  int bark  [public]
class Puppy: size 12, align 4
    (base Dog, public)
class Swimmer: size 8, align 4
    +4  int depth  [public]
class Seal: size 20, align 4
    (base Animal, public)
    (base Swimmer, public)
    +16  int fat  [public]
class Shape: size 4, align 4
class Rect: size 12, align 4
    (base Shape, public)
    +4  int w  [public]
    +8  int h  [public]
class Square: size 12, align 4
    (base Rect, public)
