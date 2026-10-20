=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t08_classes.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 306 -> 272 instruction(s) for 'test/t08_classes.c'.

optimization summary (-O2)
    instructions                306 -> 272   (11% fewer)
    constants folded            0
    algebraic simplifications   0
    common subexpressions       20
    copies / constants forwarded 22
    temporaries merged away     4
    dead instructions removed   27
    jumps removed or redirected 3
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    2

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
 123:   Dog::made = Dog::made int+ 1
 124:   t5 = *t2
 125:   param "Dog(%d)\n"
 126:   param t5
 127:   call printf, 2
 128:   return

function Dog::Dog()        link name: _ZN3DogC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   class Dog *                4      8
    t3             temp   int                        4     12
    total width 16
  code
 129:   param this                          (this)
 130:   call Animal::Animal(), 1
 131:   t1 = this ptr+ 8
 132:   param t1                            (this)
 133:   call Tag::Tag(), 1
 134:   t2 = this ptr+ 4
 135:   *t2 = 0
 136:   Dog::made = Dog::made int+ 1
 137:   param "Dog()\n"
 138:   call printf, 1
 139:   return

function Dog::~Dog()        link name: _ZN3DogD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   class Dog *                4     12
    total width 16
  code
 140:   t1 = this ptr+ 4
 141:   t2 = *t1
 142:   param "~Dog(%d)\n"
 143:   param t2
 144:   call printf, 2
 145:   t3 = this ptr+ 8
 146:   param t3                            (this)
 147:   call Tag::~Tag(), 1
 148:   param this                          (this)
 149:   call Animal::~Animal(), 1
 150:   return

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
 151:   t1 = this ptr+ 4
 152:   t2 = *t1
 153:   t3 = t2 int* 7
 154:   t4 = *this
 155:   t5 = t3 int+ t4
 156:   t6 = this ptr+ 8
 157:   t7 = *t6
 158:   t8 = t5 int+ t7
 159:   return t8

function Dog::total()        link name: _ZN3Dog5totalEv
  code
 160:   return Dog::made

function Dog::birthday()        link name: _ZN3Dog8birthdayEv
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   class Dog *                4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   class Dog *                4     16
    total width 20
  code
 161:   t1 = this ptr+ 4
 162:   t2 = *t1
 163:   t3 = t2 int+ 1
 164:   *t1 = t3
 165:   return

function Vec::Vec(int, int)        link name: _ZN3VecC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Vec *                4     12
    total width 16
  code
 166:   *this = a
 167:   t1 = this ptr+ 4
 168:   *t1 = b
 169:   return

function Vec::Vec()        link name: _ZN3VecC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   class Vec *                4      4
    total width 8
  code
 170:   *this = 0
 171:   t1 = this ptr+ 4
 172:   *t1 = 0
 173:   return

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
 174:   t2 = &t1
 175:   t3 = *this
 176:   t4 = o[0]
 177:   t5 = t3 int+ t4
 178:   t6 = this ptr+ 4
 179:   t7 = *t6
 180:   t8 = o[4]
 181:   t9 = t7 int+ t8
 182:   param t2                            (this)
 183:   param t5
 184:   param t9
 185:   call Vec::Vec(int, int), 3
 186:   return t1

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
 187:   t2 = &t1
 188:   t3 = *this
 189:   t4 = int- t3
 190:   t5 = this ptr+ 4
 191:   t6 = *t5
 192:   t7 = int- t6
 193:   param t2                            (this)
 194:   param t4
 195:   param t7
 196:   call Vec::Vec(int, int), 3
 197:   return t1

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
 198:     t2 = *this
 199:     t3 = o[0]
 200:     if t2 int!= t3 goto L1
 201:     t4 = this ptr+ 4
 202:     t5 = *t4
 203:     t6 = o[4]
 204:     if t5 int== t6 goto L2
 205: L1: t1 = 0
 206:     goto L3
 207: L2: t1 = 1
 208: L3: return t1

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
 209:     if i int!= 0 goto L4
 210:     t1 = *this
 211:     goto L5
 212: L4: t3 = this ptr+ 4
 213:     t1 = *t3
 214: L5: return t1

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
 215:   t1 = *this
 216:   t2 = o[0]
 217:   t3 = t1 int+ t2
 218:   *this = t3
 219:   t4 = this ptr+ 4
 220:   t5 = *t4
 221:   t6 = o[4]
 222:   t7 = t5 int+ t6
 223:   *t4 = t7
 224:   return this

function Vec::operator++()        link name: _ZN3VecppEv
  symbol table (name, kind, type, width, offset)
    this           param  class Vec *                4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 225:   t1 = *this
 226:   t2 = t1 int+ 1
 227:   *this = t2
 228:   return this

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
 229:   t1 = *this
 230:   t2 = t1 int* k
 231:   t3 = this ptr+ 4
 232:   t4 = *t3
 233:   t5 = t2 int+ t4
 234:   return t5

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
 235:   t1 = *this
 236:   t2 = o[0]
 237:   t3 = t1 int* t2
 238:   t4 = this ptr+ 4
 239:   t5 = *t4
 240:   t6 = o[4]
 241:   t7 = t5 int* t6
 242:   t8 = t3 int+ t7
 243:   return t8

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
 244:   t2 = &t1
 245:   t3 = v[0]
 246:   t4 = t3 int* k
 247:   t5 = v[4]
 248:   t6 = t5 int* k
 249:   param t2                            (this)
 250:   param t4
 251:   param t6
 252:   call Vec::Vec(int, int), 3
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
    total width 312
  code
 254:   t1 = &rex
 255:   param t1                            (this)
 256:   param 3
 257:   call Dog::Dog(int), 2
 258:   param t1                            (this)
 259:   call Dog::birthday(), 1
 260:   param t1                            (this)
 261:   t4 = call Dog::human(), 1
 262:   param t1                            (this)
 263:   t6 = call Animal::count(), 1
 264:   t7 = call Dog::total(), 0
 265:   param "%d %d %d\n"
 266:   param t4
 267:   param t6
 268:   param t7
 269:   call printf, 4
 270:   t9 = *t1
 271:   param "%d\n"
 272:   param t9
 273:   call printf, 2
 274:   param t1                            (this)
 275:   call Dog::~Dog(), 1
 276:   param "--\n"
 277:   call printf, 1
 278:   t11 = &other
 279:   param t11                           (this)
 280:   param 5
 281:   call Dog::Dog(int), 2
 282:   param t11                           (this)
 283:   t13 = call Dog::human(), 1
 284:   param "%d %d\n"
 285:   param t13
 286:   param Dog::made
 287:   call printf, 3
 288:   param t11                           (this)
 289:   call Dog::~Dog(), 1
 290:   param "--\n"
 291:   call printf, 1
 292:   t15 = &a
 293:   param t15                           (this)
 294:   param 1
 295:   param 2
 296:   call Vec::Vec(int, int), 3
 297:   t16 = &b
 298:   param t16                           (this)
 299:   param 3
 300:   param 4
 301:   call Vec::Vec(int, int), 3
 302:   t17 = &c
 303:   param t17                           (this)
 304:   call Vec::Vec(), 1
 305:   param t15                           (this)
 306:   param b
 307:   t19 = call Vec::operator+(class Vec), 2
 308:   c = t19
 309:   param t17                           (this)
 310:   t22 = call Vec::operator-(), 1
 311:   d = t22
 312:   param a
 313:   param 3
 314:   t25 = call operator*(class Vec, int), 2
 315:   e = t25
 316:   param t15                           (this)
 317:   param b
 318:   call Vec::operator+=(class Vec), 2
 319:   param t15                           (this)
 320:   call Vec::operator++(), 1
 321:   t32 = c[0]
 322:   t33 = c[4]
 323:   t34 = d[0]
 324:   t35 = e[4]
 325:   t36 = a[0]
 326:   t37 = a[4]
 327:   param "%d %d %d %d %d %d\n"
 328:   param t32
 329:   param t33
 330:   param t34
 331:   param t35
 332:   param t36
 333:   param t37
 334:   call printf, 7
 335:   param t15                           (this)
 336:   param b
 337:   t39 = call Vec::operator==(class Vec), 2
 338:   param t17                           (this)
 339:   param c
 340:   t41 = call Vec::operator==(class Vec), 2
 341:   param t15                           (this)
 342:   param 0
 343:   t43 = call Vec::operator[](int), 2
 344:   param t15                           (this)
 345:   param 2
 346:   t45 = call Vec::operator()(int), 2
 347:   param t15                           (this)
 348:   param b
 349:   t47 = call Vec::dot(class Vec), 2
 350:   param "%d %d %d %d %d\n"
 351:   param t39
 352:   param t41
 353:   param t43
 354:   param t45
 355:   param t47
 356:   call printf, 6
 357:   t48 = &row
 358:   param t48                           (this)
 359:   call Vec::Vec(), 1
 360:   t49 = t48 ptr+ 8
 361:   param t49                           (this)
 362:   call Vec::Vec(), 1
 363:   row[8] = 9
 364:   t50 = row[0]
 365:   param "%d %d\n"
 366:   param t50
 367:   param 9
 368:   call printf, 3
 369:   t52 = c[0]
 370:   t53 = 7 int+ t52
 371:   return t53


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
