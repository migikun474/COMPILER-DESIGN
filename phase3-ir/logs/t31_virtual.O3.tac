=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t31_virtual.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 386 -> 460 instruction(s) for 'test/t31_virtual.c'.

optimization summary (-O3)
    instructions                386 -> 460   (-19% fewer)
    constants folded            0
    algebraic simplifications   8
    common subexpressions       28
    copies / constants forwarded 127
    temporaries merged away     3
    dead instructions removed   73
    jumps removed or redirected 2
    unreachable instructions    0
    propagated across blocks    7
    dead assignments removed    6
    calls inlined               23
    tail calls turned to jumps  0
    common across blocks        10
    moved out of loops          0

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
    t10            temp   class Animal *             4     44
    t11            temp   int                        4     48
    t12            temp   unsigned int (*)[4]        4     52
    t13            temp   class Animal *             4     56
    t14            temp   unsigned int *             4     60
    t15            temp   void *                     4     64
    t16            temp   unsigned int *             4     68
    t17            temp   int                        4     72
    t18            temp   class Animal *             4     76
    t19            temp   const char *               4     80
    total width 84
  code
 144:   t12 = &_ZTV6Animal
 145:   *this = t12
 146:   t13 = this ptr+ 4
 147:   *t13 = 4
 148:   t14 = *this
 149:   t15 = *t14
 150:   t16 = t14 ptr+ 4
 151:   t17 = *t16
 152:   t18 = this ptr+ t17
 153:   param t18                           (this)
 154:   t19 = call *t15, 1                  (virtual Animal::name())
 155:   param "[A %s] "
 156:   param t19
 157:   call printf, 2
 158:   t1 = &_ZTV3Dog
 159:   *this = t1
 160:   t2 = this ptr+ 8
 161:   *t2 = b
 162:   t4 = *this
 163:   t5 = *t4
 164:   t6 = t4 ptr+ 4
 165:   t7 = *t6
 166:   t8 = this ptr+ t7
 167:   param t8                            (this)
 168:   t9 = call *t5, 1                    (virtual Dog::name())
 169:   param "[D %s] "
 170:   param t9
 171:   call printf, 2
 172:   return

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
    t8             temp   class Animal *             4     32
    t9             temp   unsigned int (*)[4]        4     36
    t10            temp   void *                     4     40
    t11            temp   unsigned int *             4     44
    t12            temp   int                        4     48
    t13            temp   class Animal *             4     52
    t14            temp   const char *               4     56
    total width 60
  code
 173:   t1 = &_ZTV3Dog
 174:   *this = t1
 175:   t3 = *t1
 176:   t4 = t1 ptr+ 4
 177:   t5 = *t4
 178:   t6 = this ptr+ t5
 179:   param t6                            (this)
 180:   t7 = call *t3, 1                    (virtual Dog::name())
 181:   param "[~D %s] "
 182:   param t7
 183:   call printf, 2
 184:   t9 = &_ZTV6Animal
 185:   *this = t9
 186:   t10 = *t9
 187:   t11 = t9 ptr+ 4
 188:   t12 = *t11
 189:   t13 = this ptr+ t12
 190:   param t13                           (this)
 191:   t14 = call *t10, 1                  (virtual Animal::name())
 192:   param "[~A %s] "
 193:   param t14
 194:   call printf, 2
 195:   return

function Dog::name()        link name: _ZNK3Dog4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    total width 4
  code
 196:   return "dog"

function Dog::speed()        link name: _ZN3Dog5speedEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    total width 16
  code
 197:   t1 = this ptr+ 8
 198:   t2 = *t1
 199:   t3 = 12 int+ t2
 200:   return t3

function Puppy::Puppy()        link name: _ZN5PuppyC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Puppy *              4      0
    t1             temp   unsigned int (*)[4]        4      4
    total width 8
  code
 201:   param this                          (this)
 202:   param 1
 203:   call Dog::Dog(int), 2
 204:   t1 = &_ZTV5Puppy
 205:   *this = t1
 206:   return

function Puppy::name()        link name: _ZNK5Puppy4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Puppy *              4      0
    total width 4
  code
 207:   return "puppy"

function Swimmer::Swimmer()        link name: _ZN7SwimmerC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Swimmer *            4      0
    t1             temp   unsigned int (*)[4]        4      4
    t2             temp   class Swimmer *            4      8
    t3             temp   class Swimmer *            4     12
    total width 16
  code
 208:   t1 = &_ZTV7Swimmer
 209:   *this = t1
 210:   t2 = this ptr+ 4
 211:   *t2 = 3
 212:   return

function Swimmer::swim()        link name: _ZN7Swimmer4swimEv
  symbol table (name, kind, type, width, offset)
    this           param  class Swimmer *            4      0
    t1             temp   class Swimmer *            4      4
    t2             temp   int                        4      8
    total width 12
  code
 213:   t1 = this ptr+ 4
 214:   t2 = *t1
 215:   return t2

function Swimmer::dive(int)        link name: _ZN7Swimmer4diveEi
  symbol table (name, kind, type, width, offset)
    this           param  class Swimmer *            4      0
    m              param  int                        4      4
    t1             temp   class Swimmer *            4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 216:   t1 = this ptr+ 4
 217:   t2 = *t1
 218:   t3 = t2 int+ m
 219:   return t3

function Seal::Seal()        link name: _ZN4SealC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Seal *               4      0
    t1             temp   class Seal *               4      4
    t2             temp   unsigned int (*)[6]        4      8
    t3             temp   unsigned int (*)[4]        4     12
    t4             temp   class Seal *               4     16
    t5             temp   class Seal *               4     20
    t6             temp   class Seal *               4     24
    t7             temp   class Animal *             4     28
    t8             temp   int                        4     32
    t9             temp   unsigned int (*)[4]        4     36
    t10            temp   class Animal *             4     40
    t11            temp   unsigned int *             4     44
    t12            temp   void *                     4     48
    t13            temp   unsigned int *             4     52
    t14            temp   int                        4     56
    t15            temp   class Animal *             4     60
    t16            temp   const char *               4     64
    t17            temp   class Swimmer *            4     68
    t18            temp   unsigned int (*)[4]        4     72
    t19            temp   class Swimmer *            4     76
    total width 80
  code
 220:   t9 = &_ZTV6Animal
 221:   *this = t9
 222:   t10 = this ptr+ 4
 223:   *t10 = 0
 224:   t11 = *this
 225:   t12 = *t11
 226:   t13 = t11 ptr+ 4
 227:   t14 = *t13
 228:   t15 = this ptr+ t14
 229:   param t15                           (this)
 230:   t16 = call *t12, 1                  (virtual Animal::name())
 231:   param "[A %s] "
 232:   param t16
 233:   call printf, 2
 234:   t1 = this ptr+ 8
 235:   t18 = &_ZTV7Swimmer
 236:   *t1 = t18
 237:   t19 = t1 ptr+ 4
 238:   *t19 = 3
 239:   t2 = &_ZTV4Seal
 240:   *this = t2
 241:   t3 = &_ZTV4Seal_8
 242:   *t1 = t3
 243:   t5 = this ptr+ 16
 244:   *t5 = 7
 245:   return

function Seal::name()        link name: _ZNK4Seal4nameEv
  symbol table (name, kind, type, width, offset)
    this           param  class Seal *               4      0
    total width 4
  code
 246:   return "seal"

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
 247:   t1 = this ptr+ 16
 248:   t2 = *t1
 249:   t3 = t2 int<< 1
 250:   t4 = this ptr+ 12
 251:   t5 = *t4
 252:   t6 = t3 int+ t5
 253:   return t6

function Shape::sides()        link name: _ZN5Shape5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 254:   return 0

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
 255:   t1 = *this
 256:   t2 = *t1
 257:   t3 = t1 ptr+ 4
 258:   t4 = *t3
 259:   t5 = this ptr+ t4
 260:   param t5                            (this)
 261:   t6 = call *t2, 1                    (virtual Shape::area())
 262:   t7 = t6 int<< 1
 263:   return t7

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
 264:   t1 = &_ZTV5Shape
 265:   *this = t1
 266:   t2 = &_ZTV4Rect
 267:   *this = t2
 268:   t3 = this ptr+ 4
 269:   *t3 = a
 270:   t5 = this ptr+ 8
 271:   *t5 = b
 272:   return

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
 273:   t1 = this ptr+ 4
 274:   t2 = *t1
 275:   t3 = this ptr+ 8
 276:   t4 = *t3
 277:   t5 = t2 int* t4
 278:   return t5

function Rect::sides()        link name: _ZN4Rect5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Rect *               4      0
    total width 4
  code
 279:   return 4

function Square::Square(int)        link name: _ZN6SquareC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    s              param  int                        4      4
    t1             temp   unsigned int (*)[4]        4      8
    t2             temp   class Rect *               4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   unsigned int (*)[4]        4     24
    t6             temp   unsigned int (*)[4]        4     28
    t7             temp   class Rect *               4     32
    t8             temp   class Rect *               4     36
    total width 40
  code
 280:   t5 = &_ZTV5Shape
 281:   *this = t5
 282:   t6 = &_ZTV4Rect
 283:   *this = t6
 284:   t7 = this ptr+ 4
 285:   *t7 = s
 286:   t8 = this ptr+ 8
 287:   *t8 = s
 288:   t1 = &_ZTV6Square
 289:   *this = t1
 290:   return

function Square::area()        link name: _ZN6Square4areaEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   class Rect *               4     12
    t4             temp   class Rect *               4     16
    t5             temp   int                        4     20
    t6             temp   class Rect *               4     24
    t7             temp   int                        4     28
    t8             temp   int                        4     32
    total width 36
  code
 291:   t4 = this ptr+ 4
 292:   t5 = *t4
 293:   t6 = this ptr+ 8
 294:   t7 = *t6
 295:   t8 = t5 int* t7
 296:   t2 = t8 int+ 1
 297:   return t2

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
 298:   t1 = *s
 299:   t2 = *t1
 300:   t3 = t1 ptr+ 4
 301:   t4 = *t3
 302:   t5 = s ptr+ t4
 303:   param t5                            (this)
 304:   t6 = call *t2, 1                    (virtual Shape::area())
 305:   t7 = *s
 306:   t8 = t7 ptr+ 8
 307:   t9 = *t8
 308:   t10 = t7 ptr+ 12
 309:   t11 = *t10
 310:   t12 = s ptr+ t11
 311:   param t12                           (this)
 312:   t13 = call *t9, 1                   (virtual Shape::sides())
 313:   t14 = t6 int+ t13
 314:   return t14

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
 315:   t1 = *a
 316:   t2 = t1 ptr+ 8
 317:   t3 = *t2
 318:   t4 = t1 ptr+ 12
 319:   t5 = *t4
 320:   t6 = a ptr+ t5
 321:   param t6                            (this)
 322:   t7 = call *t3, 1                    (virtual Animal::speed())
 323:   return t7

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
    t92            temp   class Puppy *              4    484
    t93            temp   unsigned int (*)[4]        4    488
    t94            temp   class Seal *               4    492
    t95            temp   class Seal *               4    496
    t96            temp   unsigned int (*)[6]        4    500
    t97            temp   unsigned int (*)[4]        4    504
    t98            temp   class Seal *               4    508
    t99            temp   class Animal *             4    512
    t100           temp   unsigned int *             4    516
    t101           temp   unsigned int *             4    520
    t102           temp   void *                     4    524
    t103           temp   unsigned int *             4    528
    t104           temp   int                        4    532
    t105           temp   class Animal *             4    536
    t106           temp   int                        4    540
    t107           temp   int                        4    544
    t108           temp   class Animal *             4    548
    t109           temp   int                        4    552
    t110           temp   int                        4    556
    t111           temp   class Animal *             4    560
    t112           temp   unsigned int *             4    564
    t113           temp   unsigned int *             4    568
    t114           temp   void *                     4    572
    t115           temp   unsigned int *             4    576
    t116           temp   int                        4    580
    t117           temp   class Animal *             4    584
    t118           temp   int                        4    588
    t119           temp   class Animal *             4    592
    t120           temp   class Animal *             4    596
    t121           temp   int                        4    600
    t122           temp   class Animal *             4    604
    t123           temp   class Animal *             4    608
    t124           temp   int                        4    612
    t125           temp   class Animal *             4    616
    t126           temp   class Animal *             4    620
    t127           temp   class Animal *             4    624
    t128           temp   int                        4    628
    t129           temp   class Animal *             4    632
    t130           temp   class Animal *             4    636
    t131           temp   class Animal *             4    640
    t132           temp   int                        4    644
    t133           temp   class Rect *               4    648
    t134           temp   int                        4    652
    t135           temp   int                        4    656
    t136           temp   unsigned int (*)[4]        4    660
    t137           temp   unsigned int (*)[4]        4    664
    t138           temp   class Rect *               4    668
    t139           temp   class Rect *               4    672
    t140           temp   class Square *             4    676
    t141           temp   int                        4    680
    t142           temp   unsigned int (*)[4]        4    684
    t143           temp   class Shape *              4    688
    t144           temp   unsigned int *             4    692
    t145           temp   void *                     4    696
    t146           temp   unsigned int *             4    700
    t147           temp   int                        4    704
    t148           temp   class Shape *              4    708
    t149           temp   int                        4    712
    t150           temp   int                        4    716
    t151           temp   class Animal *             4    720
    t152           temp   unsigned int (*)[4]        4    724
    t153           temp   void *                     4    728
    t154           temp   unsigned int *             4    732
    t155           temp   int                        4    736
    t156           temp   class Animal *             4    740
    t157           temp   const char *               4    744
    t158           temp   class Animal *             4    748
    t159           temp   unsigned int (*)[4]        4    752
    t160           temp   void *                     4    756
    t161           temp   unsigned int *             4    760
    t162           temp   int                        4    764
    t163           temp   class Animal *             4    768
    t164           temp   const char *               4    772
    t165           temp   class Dog *                4    776
    t166           temp   unsigned int (*)[4]        4    780
    t167           temp   void *                     4    784
    t168           temp   unsigned int *             4    788
    t169           temp   int                        4    792
    t170           temp   class Dog *                4    796
    t171           temp   const char *               4    800
    t172           temp   class Dog *                4    804
    t173           temp   unsigned int (*)[4]        4    808
    t174           temp   void *                     4    812
    t175           temp   unsigned int *             4    816
    t176           temp   int                        4    820
    t177           temp   class Dog *                4    824
    t178           temp   const char *               4    828
    total width 832
  code
 324:     t1 = &d
 325:     param t1                            (this)
 326:     param 5
 327:     call Dog::Dog(int), 2
 328:     param "\n"
 329:     call printf, 1
 330:     t2 = &p
 331:     param t2                            (this)
 332:     param 1
 333:     call Dog::Dog(int), 2
 334:     t93 = &_ZTV5Puppy
 335:     *t2 = t93
 336:     param "\n"
 337:     call printf, 1
 338:     zoo[0] = t1
 339:     zoo[4] = t2
 340:     zoo[8] = 0
 341:     t5 = &s
 342:     param t5                            (this)
 343:     param 0
 344:     call Animal::Animal(int), 2
 345:     t95 = t5 ptr+ 8
 346:     param t95                           (this)
 347:     call Swimmer::Swimmer(), 1
 348:     t96 = &_ZTV4Seal
 349:     *t5 = t96
 350:     t97 = &_ZTV4Seal_8
 351:     *t95 = t97
 352:     t98 = t5 ptr+ 16
 353:     *t98 = 7
 354:     zoo[8] = t5
 355:     param "\n"
 356:     call printf, 1
 357:     i.13 = 0
 358: L1: if i.13 int>= 3 goto L2
 359:     t7 = i.13 int<< 2                   (w = 4)
 360:     t8 = zoo[t7]
 361:     t9 = *t8
 362:     t10 = *t9
 363:     t11 = t9 ptr+ 4
 364:     t12 = *t11
 365:     t13 = t8 ptr+ t12
 366:     param t13                           (this)
 367:     t14 = call *t10, 1                  (virtual Animal::name())
 368:     t16 = zoo[t7]
 369:     t17 = *t16
 370:     t18 = t17 ptr+ 8
 371:     t19 = *t18
 372:     t20 = t17 ptr+ 12
 373:     t21 = *t20
 374:     t22 = t16 ptr+ t21
 375:     param t22                           (this)
 376:     t23 = call *t19, 1                  (virtual Animal::speed())
 377:     t25 = zoo[t7]
 378:     t100 = *t25
 379:     t101 = t100 ptr+ 8
 380:     t102 = *t101
 381:     t103 = t100 ptr+ 12
 382:     t104 = *t103
 383:     t105 = t25 ptr+ t104
 384:     param t105                          (this)
 385:     t106 = call *t102, 1                (virtual Animal::speed())
 386:     t107 = t106 int* 10
 387:     t108 = t25 ptr+ 4
 388:     t109 = *t108
 389:     t110 = t107 int+ t109
 390:     param "%s %d %d | "
 391:     param t14
 392:     param t23
 393:     param t110
 394:     call printf, 4
 395:     i.13 = i.13 int+ 1
 396:     goto L1
 397: L2: param "\n"
 398:     call printf, 1
 399:     t29 = t5
 400:     if t5 ptr== 0 goto L3
 401:     t29 = t95
 402: L3: t30 = *t29
 403:     t31 = *t30
 404:     t32 = t30 ptr+ 4
 405:     t33 = *t32
 406:     t34 = t29 ptr+ t33
 407:     param t34                           (this)
 408:     t35 = call *t31, 1                  (virtual Swimmer::swim())
 409:     t36 = *t29
 410:     t37 = t36 ptr+ 8
 411:     t38 = *t37
 412:     t39 = t36 ptr+ 12
 413:     t40 = *t39
 414:     t41 = t29 ptr+ t40
 415:     param t41                           (this)
 416:     param 2
 417:     t42 = call *t38, 2                  (virtual Swimmer::dive(int))
 418:     t112 = *t5
 419:     t113 = t112 ptr+ 8
 420:     t114 = *t113
 421:     t115 = t112 ptr+ 12
 422:     t116 = *t115
 423:     t117 = t5 ptr+ t116
 424:     param t117                          (this)
 425:     t118 = call *t114, 1                (virtual Animal::speed())
 426:     param "%d %d %d\n"
 427:     param t35
 428:     param t42
 429:     param t118
 430:     call printf, 4
 431:     t46 = *t2
 432:     t47 = *t46
 433:     t48 = t46 ptr+ 4
 434:     t49 = *t48
 435:     t50 = t2 ptr+ t49
 436:     param t50                           (this)
 437:     t51 = call *t47, 1                  (virtual Animal::name())
 438:     t120 = t2 ptr+ 4
 439:     t121 = *t120
 440:     t123 = t1 ptr+ 4
 441:     t124 = *t123
 442:     param "%s %d %d\n"
 443:     param t51
 444:     param t121
 445:     param t124
 446:     call printf, 4
 447:     copy = d[0]
 448:     t56 = &copy
 449:     t57 = &_ZTV6Animal
 450:     *t56 = t57
 451:     t127 = t56 ptr+ 4
 452:     t128 = *t127
 453:     param "%s %d\n"
 454:     param "animal"
 455:     param t128
 456:     call printf, 3
 457:     t62 = p[0]
 458:     t64 = *t56
 459:     copy = t62
 460:     *t56 = t64
 461:     t132 = *t127
 462:     param "%s %d\n"
 463:     param "animal"
 464:     param t132
 465:     call printf, 3
 466:     t69 = &r
 467:     t136 = &_ZTV5Shape
 468:     *t69 = t136
 469:     t137 = &_ZTV4Rect
 470:     *t69 = t137
 471:     t138 = t69 ptr+ 4
 472:     *t138 = 2
 473:     t139 = t69 ptr+ 8
 474:     *t139 = 3
 475:     t70 = &sq
 476:     param t70                           (this)
 477:     param 4
 478:     param 4
 479:     call Rect::Rect(int, int), 3
 480:     t142 = &_ZTV6Square
 481:     *t70 = t142
 482:     shapes[0] = t69
 483:     shapes[4] = t70
 484:     i.20 = 0
 485: L4: if i.20 int>= 2 goto L5
 486:     t73 = i.20 int<< 2                  (w = 4)
 487:     t74 = shapes[t73]
 488:     t75 = *t74
 489:     t76 = *t75
 490:     t77 = t75 ptr+ 4
 491:     t78 = *t77
 492:     t79 = t74 ptr+ t78
 493:     param t79                           (this)
 494:     t80 = call *t76, 1                  (virtual Shape::area())
 495:     t82 = shapes[t73]
 496:     t144 = *t82
 497:     t145 = *t144
 498:     t146 = t144 ptr+ 4
 499:     t147 = *t146
 500:     t148 = t82 ptr+ t147
 501:     param t148                          (this)
 502:     t149 = call *t145, 1                (virtual Shape::area())
 503:     t150 = t149 int<< 1
 504:     t85 = shapes[t73]
 505:     param t85
 506:     t86 = call total(class Shape &), 1
 507:     param "%d %d %d | "
 508:     param t80
 509:     param t150
 510:     param t86
 511:     call printf, 4
 512:     i.20 = i.20 int+ 1
 513:     goto L4
 514: L5: param "\n"
 515:     call printf, 1
 516:     *t56 = t57
 517:     t153 = *t57
 518:     t154 = t57 ptr+ 4
 519:     t155 = *t154
 520:     t156 = t56 ptr+ t155
 521:     param t156                          (this)
 522:     t157 = call *t153, 1                (virtual Animal::name())
 523:     param "[~A %s] "
 524:     param t157
 525:     call printf, 2
 526:     *t5 = t57
 527:     t160 = *t57
 528:     t162 = *t154
 529:     t163 = t5 ptr+ t162
 530:     param t163                          (this)
 531:     t164 = call *t160, 1                (virtual Animal::name())
 532:     param "[~A %s] "
 533:     param t164
 534:     call printf, 2
 535:     t166 = &_ZTV3Dog
 536:     *t2 = t166
 537:     t167 = *t166
 538:     t168 = t166 ptr+ 4
 539:     t169 = *t168
 540:     t170 = t2 ptr+ t169
 541:     param t170                          (this)
 542:     t171 = call *t167, 1                (virtual Dog::name())
 543:     param "[~D %s] "
 544:     param t171
 545:     call printf, 2
 546:     param t2                            (this)
 547:     call Animal::~Animal(), 1
 548:     *t1 = t166
 549:     t174 = *t166
 550:     t176 = *t168
 551:     t177 = t1 ptr+ t176
 552:     param t177                          (this)
 553:     t178 = call *t174, 1                (virtual Dog::name())
 554:     param "[~D %s] "
 555:     param t178
 556:     call printf, 2
 557:     param t1                            (this)
 558:     call Animal::~Animal(), 1
 559:     return 0


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
