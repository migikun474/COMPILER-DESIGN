=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t08_classes.c
Optimization : no optimization

Three address code generated: 23 function(s), 306 instruction(s) for 'test/t08_classes.c'.

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
    total width 28
  code
 116:   param this                          (this)
 117:   call Animal::Animal(), 1
 118:   t1 = this ptr+ 8
 119:   param t1                            (this)
 120:   call Tag::Tag(), 1
 121:   t2 = this ptr+ 4
 122:   *t2 = a
 123:   t3 = Dog::made int+ 1
 124:   Dog::made = t3
 125:   t4 = this ptr+ 4
 126:   t5 = *t4
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
    total width 16
  code
 131:   param this                          (this)
 132:   call Animal::Animal(), 1
 133:   t1 = this ptr+ 8
 134:   param t1                            (this)
 135:   call Tag::Tag(), 1
 136:   t2 = this ptr+ 4
 137:   *t2 = 0
 138:   t3 = Dog::made int+ 1
 139:   Dog::made = t3
 140:   param "Dog()\n"
 141:   call printf, 1
 142:   return

function Dog::~Dog()        link name: _ZN3DogD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   class Dog *                4     12
    total width 16
  code
 143:   t1 = this ptr+ 4
 144:   t2 = *t1
 145:   param "~Dog(%d)\n"
 146:   param t2
 147:   call printf, 2
 148:   t3 = this ptr+ 8
 149:   param t3                            (this)
 150:   call Tag::~Tag(), 1
 151:   param this                          (this)
 152:   call Animal::~Animal(), 1
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
 167:   t4 = this ptr+ 4
 168:   *t4 = t3
 169:   return

function Vec::Vec(int, int)        link name: _ZN3VecC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Vec *                4     12
    total width 16
  code
 170:   *this = a
 171:   t1 = this ptr+ 4
 172:   *t1 = b
 173:   return

function Vec::Vec()        link name: _ZN3VecC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   class Vec *                4      4
    total width 8
  code
 174:   *this = 0
 175:   t1 = this ptr+ 4
 176:   *t1 = 0
 177:   return

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
    total width 52
  code
 178:   t2 = &t1
 179:   t3 = *this
 180:   t4 = o[0]
 181:   t5 = t3 int+ t4
 182:   t6 = this ptr+ 4
 183:   t7 = *t6
 184:   t8 = o[4]
 185:   t9 = t7 int+ t8
 186:   param t2                            (this)
 187:   param t5
 188:   param t9
 189:   call Vec::Vec(int, int), 3
 190:   return t1

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
    total width 36
  code
 191:   t2 = &t1
 192:   t3 = *this
 193:   t4 = int- t3
 194:   t5 = this ptr+ 4
 195:   t6 = *t5
 196:   t7 = int- t6
 197:   param t2                            (this)
 198:   param t4
 199:   param t7
 200:   call Vec::Vec(int, int), 3
 201:   return t1

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
 202:     t2 = *this
 203:     t3 = o[0]
 204:     if t2 int== t3 goto L1
 205:     goto L2
 206: L1: t4 = this ptr+ 4
 207:     t5 = *t4
 208:     t6 = o[4]
 209:     if t5 int== t6 goto L3
 210:     goto L2
 211: L2: t1 = 0
 212:     goto L4
 213: L3: t1 = 1
 214: L4: return t1

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
 215:     if i int== 0 goto L5
 216:     goto L6
 217: L5: t2 = *this
 218:     t1 = t2
 219:     goto L7
 220: L6: t3 = this ptr+ 4
 221:     t4 = *t3
 222:     t1 = t4
 223: L7: return t1

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
 224:   t1 = *this
 225:   t2 = o[0]
 226:   t3 = t1 int+ t2
 227:   *this = t3
 228:   t4 = this ptr+ 4
 229:   t5 = *t4
 230:   t6 = o[4]
 231:   t7 = t5 int+ t6
 232:   t8 = this ptr+ 4
 233:   *t8 = t7
 234:   return this

function Vec::operator++()        link name: _ZN3VecppEv
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 235:   t1 = *this
 236:   t2 = t1 int+ 1
 237:   *this = t2
 238:   return this

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
 239:   t1 = *this
 240:   t2 = t1 int* k
 241:   t3 = this ptr+ 4
 242:   t4 = *t3
 243:   t5 = t2 int+ t4
 244:   return t5

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
 245:   t1 = *this
 246:   t2 = o[0]
 247:   t3 = t1 int* t2
 248:   t4 = this ptr+ 4
 249:   t5 = *t4
 250:   t6 = o[4]
 251:   t7 = t5 int* t6
 252:   t8 = t3 int+ t7
 253:   return t8

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
    total width 40
  code
 254:   t2 = &t1
 255:   t3 = v[0]
 256:   t4 = t3 int* k
 257:   t5 = v[4]
 258:   t6 = t5 int* k
 259:   param t2                            (this)
 260:   param t4
 261:   param t6
 262:   call Vec::Vec(int, int), 3
 263:   return t1

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
    total width 312
  code
 264:   t1 = &rex
 265:   param t1                            (this)
 266:   param 3
 267:   call Dog::Dog(int), 2
 268:   t2 = &rex
 269:   param t2                            (this)
 270:   call Dog::birthday(), 1
 271:   t3 = &rex
 272:   param t3                            (this)
 273:   t4 = call Dog::human(), 1
 274:   t5 = &rex
 275:   param t5                            (this)
 276:   t6 = call Animal::count(), 1
 277:   t7 = call Dog::total(), 0
 278:   param "%d %d %d\n"
 279:   param t4
 280:   param t6
 281:   param t7
 282:   call printf, 4
 283:   t8 = &rex
 284:   base = t8
 285:   t9 = *base
 286:   param "%d\n"
 287:   param t9
 288:   call printf, 2
 289:   t10 = &rex
 290:   param t10                           (this)
 291:   call Dog::~Dog(), 1
 292:   param "--\n"
 293:   call printf, 1
 294:   t11 = &other
 295:   param t11                           (this)
 296:   param 5
 297:   call Dog::Dog(int), 2
 298:   t12 = &other
 299:   param t12                           (this)
 300:   t13 = call Dog::human(), 1
 301:   param "%d %d\n"
 302:   param t13
 303:   param Dog::made
 304:   call printf, 3
 305:   t14 = &other
 306:   param t14                           (this)
 307:   call Dog::~Dog(), 1
 308:   param "--\n"
 309:   call printf, 1
 310:   t15 = &a
 311:   param t15                           (this)
 312:   param 1
 313:   param 2
 314:   call Vec::Vec(int, int), 3
 315:   t16 = &b
 316:   param t16                           (this)
 317:   param 3
 318:   param 4
 319:   call Vec::Vec(int, int), 3
 320:   t17 = &c
 321:   param t17                           (this)
 322:   call Vec::Vec(), 1
 323:   t18 = &a
 324:   param t18                           (this)
 325:   param b
 326:   t19 = call Vec::operator+(class Vec), 2
 327:   t20 = &t19
 328:   c = t19
 329:   t21 = &c
 330:   param t21                           (this)
 331:   t22 = call Vec::operator-(), 1
 332:   t23 = &t22
 333:   d = t22
 334:   t24 = &d
 335:   param a
 336:   param 3
 337:   t25 = call operator*(class Vec, int), 2
 338:   t26 = &t25
 339:   e = t25
 340:   t27 = &e
 341:   t28 = &a
 342:   param t28                           (this)
 343:   param b
 344:   t29 = call Vec::operator+=(class Vec), 2
 345:   t30 = &a
 346:   param t30                           (this)
 347:   t31 = call Vec::operator++(), 1
 348:   t32 = c[0]
 349:   t33 = c[4]
 350:   t34 = d[0]
 351:   t35 = e[4]
 352:   t36 = a[0]
 353:   t37 = a[4]
 354:   param "%d %d %d %d %d %d\n"
 355:   param t32
 356:   param t33
 357:   param t34
 358:   param t35
 359:   param t36
 360:   param t37
 361:   call printf, 7
 362:   t38 = &a
 363:   param t38                           (this)
 364:   param b
 365:   t39 = call Vec::operator==(class Vec), 2
 366:   t40 = &c
 367:   param t40                           (this)
 368:   param c
 369:   t41 = call Vec::operator==(class Vec), 2
 370:   t42 = &a
 371:   param t42                           (this)
 372:   param 0
 373:   t43 = call Vec::operator[](int), 2
 374:   t44 = &a
 375:   param t44                           (this)
 376:   param 2
 377:   t45 = call Vec::operator()(int), 2
 378:   t46 = &a
 379:   param t46                           (this)
 380:   param b
 381:   t47 = call Vec::dot(class Vec), 2
 382:   param "%d %d %d %d %d\n"
 383:   param t39
 384:   param t41
 385:   param t43
 386:   param t45
 387:   param t47
 388:   call printf, 6
 389:   t48 = &row
 390:   param t48                           (this)
 391:   call Vec::Vec(), 1
 392:   t49 = t48 ptr+ 8
 393:   param t49                           (this)
 394:   call Vec::Vec(), 1
 395:   row[8] = 9
 396:   t50 = row[0]
 397:   t51 = row[8]
 398:   param "%d %d\n"
 399:   param t50
 400:   param t51
 401:   call printf, 3
 402:   w = 7
 403:   t52 = c[0]
 404:   t53 = w int+ t52
 405:   return t53


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
