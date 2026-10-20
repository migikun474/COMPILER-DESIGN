=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t32_class_features.c
Optimization : no optimization

Three address code generated: 26 function(s), 268 instruction(s) for 'test/t32_class_features.c'.

function Point::Point(int)        link name: _ZN5PointC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    a              param  int                        4      4
    t1             temp   class Point *              4      8
    t2             temp   int                        4     12
    t3             temp   class Point *              4     16
    total width 20
  code
 100:   *this = a
 101:   t1 = this ptr+ 4
 102:   t2 = a int* 2
 103:   t3 = this ptr+ 4
 104:   *t3 = t2
 105:   param "(P%d) "
 106:   param a
 107:   call printf, 2
 108:   return

function Point::Point(int, int)        link name: _ZN5PointC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Point *              4     12
    t2             temp   class Point *              4     16
    total width 20
  code
 109:   *this = a
 110:   t1 = this ptr+ 4
 111:   t2 = this ptr+ 4
 112:   *t2 = b
 113:   return

function Point::sum()        link name: _ZNK5Point3sumEv
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    t1             temp   int                        4      4
    t2             temp   class Point *              4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 114:   t1 = *this
 115:   t2 = this ptr+ 4
 116:   t3 = *t2
 117:   t4 = t1 int+ t3
 118:   return t4

function Line::Line(class Point, class Point, int &)        link name: _ZN4LineC1E5PointS0_Ri
  symbol table (name, kind, type, width, offset)
    this           param  class Line *               4      0
    a              param  class Point                8      4
    b              param  class Point                8     12
    u              param  int &                      4     20
    t1             temp   class Line *               4     24
    t2             temp   class Line *               4     28
    t3             temp   class Line *               4     32
    t4             temp   class Line *               4     36
    t5             temp   class Line *               4     40
    t6             temp   class Line *               4     44
    t7             temp   int *                      4     48
    t8             temp   int                        4     52
    t9             temp   int                        4     56
    total width 60
  code
 119:   *this = a
 120:   t1 = this ptr+ 8
 121:   *t1 = b
 122:   t2 = this ptr+ 16
 123:   t3 = this ptr+ 16
 124:   *t3 = u
 125:   t4 = this ptr+ 20
 126:   t5 = this ptr+ 20
 127:   *t5 = 0
 128:   t6 = this ptr+ 16
 129:   t7 = *t6
 130:   t8 = *t7
 131:   t9 = t8 int+ 1
 132:   *t7 = t9
 133:   return

function Line::length()        link name: _ZNK4Line6lengthEv
  symbol table (name, kind, type, width, offset)
    this           param  class Line *               4      0
    t1             temp   class Line *               4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 134:   t1 = this ptr+ 8
 135:   t2 = *t1
 136:   t3 = *this
 137:   t4 = t2 int- t3
 138:   return t4

function Line::width()        link name: _ZNK4Line5widthEv
  symbol table (name, kind, type, width, offset)
    this           param  class Line *               4      0
    t1             temp   class Line *               4      4
    t2             temp   int                        4      8
    total width 12
  code
 139:   t1 = this ptr+ 20
 140:   t2 = *t1
 141:   return t2

function peek(const class Line &)        link name: _Z4peekRK4Line
  symbol table (name, kind, type, width, offset)
    l              param  const class Line &         4      0
    t1             temp   const class Line *         4      4
    t2             temp   int                        4      8
    t3             temp   const class Line *         4     12
    t4             temp   int                        4     16
    t5             temp   int                        4     20
    total width 24
  code
 142:   t1 = l ptr+ 4
 143:   t2 = *t1
 144:   t3 = l ptr+ 12
 145:   t4 = *t3
 146:   t5 = t2 int+ t4
 147:   return t5

function Inspector::look(class Line &)        link name: _ZN9Inspector4lookER4Line
  symbol table (name, kind, type, width, offset)
    this           param  class Inspector *          4      0
    l              param  class Line &               4      4
    t1             temp   class Line *               4      8
    t2             temp   class Line *               4     12
    t3             temp   int *                      4     16
    t4             temp   int                        4     20
    t5             temp   class Line *               4     24
    t6             temp   int                        4     28
    t7             temp   int                        4     32
    total width 36
  code
 148:   t1 = l ptr+ 20
 149:   *t1 = 9
 150:   t2 = l ptr+ 16
 151:   t3 = *t2
 152:   t4 = *t3
 153:   t5 = l ptr+ 20
 154:   t6 = *t5
 155:   t7 = t4 int+ t6
 156:   return t7

function Counter::Counter()        link name: _ZN7CounterC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    total width 4
  code
 157:   *this = 0
 158:   return

function Counter::get()        link name: _ZNK7Counter3getEv
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    t1             temp   int                        4      4
    total width 8
  code
 159:   t1 = *this
 160:   return t1

function Counter::get()        link name: _ZN7Counter3getEv
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 161:   t1 = *this
 162:   t2 = t1 int+ 100
 163:   return t2

function Counter::add(int)        link name: _ZN7Counter3addEi
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    k              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 164:   t1 = *this
 165:   t2 = t1 int+ k
 166:   *this = t2
 167:   return

function Meters::Meters(int)        link name: _ZN6MetersC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Meters *             4      0
    x              param  int                        4      4
    total width 8
  code
 168:   *this = x
 169:   return

function useMeters(class Meters)        link name: _Z9useMeters6Meters
  symbol table (name, kind, type, width, offset)
    m              param  class Meters               4      0
    t1             temp   int                        4      4
    total width 8
  code
 170:   t1 = m[0]
 171:   return t1

function Box::Box(int)        link name: _ZN3BoxC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Box *                4      0
    a              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 172:   *this = a
 173:   t1 = *this
 174:   param "[+%d] "
 175:   param t1
 176:   call printf, 2
 177:   return

function Box::Box(const class Box &)        link name: _ZN3BoxC1ERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Box *                4      0
    o              param  const class Box &          4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 178:   t1 = *o
 179:   t2 = t1 int+ 100
 180:   *this = t2
 181:   t3 = *this
 182:   param "[copy %d] "
 183:   param t3
 184:   call printf, 2
 185:   return

function Box::~Box()        link name: _ZN3BoxD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Box *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 186:   t1 = *this
 187:   param "[-%d] "
 188:   param t1
 189:   call printf, 2
 190:   return

function byValue(class Box)        link name: _Z7byValue3Box
  symbol table (name, kind, type, width, offset)
    b              param  class Box                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 191:   t1 = b[0]
 192:   return t1

function byRef(const class Box &)        link name: _Z5byRefRK3Box
  symbol table (name, kind, type, width, offset)
    b              param  const class Box &          4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 193:   t1 = *b
 194:   t2 = t1 int* 2
 195:   return t2

function makeBox(int)        link name: _Z7makeBoxi
  symbol table (name, kind, type, width, offset)
    k              param  int                        4      0
    t1             temp   class Box                  4      4
    t2             temp   class Box *                4      8
    t3             temp   int                        4     12
    total width 16
  code
 196:   t2 = &t1
 197:   t3 = k int* 3
 198:   param t2                            (this)
 199:   param t3
 200:   call Box::Box(int), 2
 201:   return t1

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    total width 4
  code
 202:   return a

function pick(class Box)        link name: _Z4pick3Box
  symbol table (name, kind, type, width, offset)
    b              param  class Box                  4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 203:   t1 = b[0]
 204:   t2 = t1 int+ 1000
 205:   return t2

function Base::Base(int)        link name: _ZN4BaseC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Base *               4      0
    t              param  int                        4      4
    total width 8
  code
 206:   *this = t
 207:   param "<B%d> "
 208:   param t
 209:   call printf, 2
 210:   return

function Derived::Derived(int)        link name: _ZN7DerivedC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Derived *            4      0
    e              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   class Derived *            4     12
    t3             temp   class Derived *            4     16
    total width 20
  code
 211:   t1 = e int* 10
 212:   param this                          (this)
 213:   param t1
 214:   call Base::Base(int), 2
 215:   t2 = this ptr+ 4
 216:   t3 = this ptr+ 4
 217:   *t3 = e
 218:   param "<D%d> "
 219:   param e
 220:   call printf, 2
 221:   return

function area(class Point)        link name: _Z4area5Point
  symbol table (name, kind, type, width, offset)
    p              param  class Point                8      0
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 222:   t1 = p[0]
 223:   t2 = p[4]
 224:   t3 = t1 int* t2
 225:   return t3

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    uses           local  int                        4      0
    l              local  class Line                24      4
    in             local  class Inspector            1     28
    seen           local  int                        4     32
    c              local  class Counter              4     36
    rc             local  const class Counter &      4     40
    m              local  class Meters               4     44
    b              local  class Box                  4     48
    d              local  class Derived              8     52
    a              local  int                        4     60
    sum            local  int                        4     64
    t1             temp   class Line *               4     68
    t2             temp   class Point                8     72
    t3             temp   class Point *              4     80
    t4             temp   class Point                8     84
    t5             temp   class Point *              4     92
    t6             temp   int *                      4     96
    t7             temp   class Line *               4    100
    t8             temp   int                        4    104
    t9             temp   class Line *               4    108
    t10            temp   int                        4    112
    t11            temp   class Line *               4    116
    t12            temp   int                        4    120
    t13            temp   class Inspector *          4    124
    t14            temp   class Line *               4    128
    t15            temp   int                        4    132
    t16            temp   class Line *               4    136
    t17            temp   int                        4    140
    t18            temp   class Counter *            4    144
    t19            temp   class Counter *            4    148
    t20            temp   class Counter *            4    152
    t21            temp   class Counter *            4    156
    t22            temp   int                        4    160
    t23            temp   int                        4    164
    t24            temp   class Meters *             4    168
    t25            temp   int                        4    172
    t26            temp   class Box                  4    176
    t27            temp   class Box *                4    180
    t28            temp   int                        4    184
    t29            temp   class Box *                4    188
    t30            temp   class Box                  4    192
    t31            temp   class Box *                4    196
    t32            temp   class Box *                4    200
    t33            temp   int                        4    204
    t34            temp   class Box *                4    208
    t35            temp   int                        4    212
    t36            temp   class Box                  4    216
    t37            temp   class Box *                4    220
    t38            temp   class Box *                4    224
    t39            temp   int                        4    228
    t40            temp   class Derived *            4    232
    t41            temp   class Point                8    236
    t42            temp   class Point *              4    244
    t43            temp   int                        4    248
    t44            temp   class Point                8    252
    t45            temp   class Point *              4    260
    t46            temp   class Point *              4    264
    t47            temp   int                        4    268
    t48            temp   int                        4    272
    t49            temp   int                        4    276
    t50            temp   class Box *                4    280
    total width 284
  code
 226:   uses = 0
 227:   t1 = &l
 228:   t3 = &t2
 229:   param t3                            (this)
 230:   param 1
 231:   param 5
 232:   call Point::Point(int, int), 3
 233:   t5 = &t4
 234:   param t5                            (this)
 235:   param 4
 236:   call Point::Point(int), 2
 237:   t6 = &uses
 238:   param t1                            (this)
 239:   param t2
 240:   param t4
 241:   param t6
 242:   call Line::Line(class Point, class Point, int &), 4
 243:   t7 = &l
 244:   param t7                            (this)
 245:   t8 = call Line::length(), 1
 246:   t9 = &l
 247:   param t9                            (this)
 248:   t10 = call Line::width(), 1
 249:   t11 = &l
 250:   param t11
 251:   t12 = call peek(const class Line &), 1
 252:   param "| %d %d %d %d\n"
 253:   param t8
 254:   param t10
 255:   param t12
 256:   param uses
 257:   call printf, 5
 258:   t13 = &in
 259:   t14 = &l
 260:   param t13                           (this)
 261:   param t14
 262:   t15 = call Inspector::look(class Line &), 2
 263:   seen = t15
 264:   t16 = &l
 265:   param t16                           (this)
 266:   t17 = call Line::width(), 1
 267:   param "%d %d\n"
 268:   param seen
 269:   param t17
 270:   call printf, 3
 271:   t18 = &c
 272:   param t18                           (this)
 273:   call Counter::Counter(), 1
 274:   t19 = &c
 275:   rc = t19
 276:   t20 = &c
 277:   param t20                           (this)
 278:   param 3
 279:   call Counter::add(int), 2
 280:   t21 = &c
 281:   param t21                           (this)
 282:   t22 = call Counter::get(), 1
 283:   param rc                            (this)
 284:   t23 = call Counter::get(), 1
 285:   param "%d %d\n"
 286:   param t22
 287:   param t23
 288:   call printf, 3
 289:   t24 = &m
 290:   param t24                           (this)
 291:   param 7
 292:   call Meters::Meters(int), 2
 293:   param m
 294:   t25 = call useMeters(class Meters), 1
 295:   param "%d\n"
 296:   param t25
 297:   call printf, 2
 298:   t27 = &t26
 299:   param t27                           (this)
 300:   param 5
 301:   call Box::Box(int), 2
 302:   param t26
 303:   t28 = call byValue(class Box), 1
 304:   param "%d | "
 305:   param t28
 306:   call printf, 2
 307:   t29 = &t26
 308:   param t29                           (this)
 309:   call Box::~Box(), 1
 310:   t31 = &t30
 311:   param t31                           (this)
 312:   param 6
 313:   call Box::Box(int), 2
 314:   t32 = &t30
 315:   param t32
 316:   t33 = call byRef(const class Box &), 1
 317:   param "%d | "
 318:   param t33
 319:   call printf, 2
 320:   t34 = &t30
 321:   param t34                           (this)
 322:   call Box::~Box(), 1
 323:   param 7
 324:   t35 = call pick(int), 1
 325:   param "%d | "
 326:   param t35
 327:   call printf, 2
 328:   param 4
 329:   t36 = call makeBox(int), 1
 330:   t37 = &t36
 331:   b = t36
 332:   t38 = &b
 333:   t39 = b[0]
 334:   param "%d\n"
 335:   param t39
 336:   call printf, 2
 337:   t40 = &d
 338:   param t40                           (this)
 339:   param 3
 340:   call Derived::Derived(int), 2
 341:   t42 = &t41
 342:   param t42                           (this)
 343:   param 6
 344:   call Point::Point(int), 2
 345:   param t41
 346:   t43 = call area(class Point), 1
 347:   a = t43
 348:   t45 = &t44
 349:   param t45                           (this)
 350:   param 2
 351:   call Point::Point(int), 2
 352:   t46 = &t44
 353:   param t46                           (this)
 354:   t47 = call Point::sum(), 1
 355:   sum = t47
 356:   t48 = d[0]
 357:   t49 = d[4]
 358:   param "%d %d | %d %d\n"
 359:   param t48
 360:   param t49
 361:   param a
 362:   param sum
 363:   call printf, 5
 364:   t50 = &b
 365:   param t50                           (this)
 366:   call Box::~Box(), 1
 367:   return 0


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Point              class_tag      class Point                -        global                         6     -     0     Point                -                        size 8
Point::x           field          int                        member   global > class Point           8     4     4     Point::x             -                        public, offset 0
Point::y           field          int                        member   global > class Point           8     4     4     Point::y             -                        public, offset 4
Point::Point       constructor    void (int)                 -        global > class Point           9     -     3     _ZN5PointC1Ei        _ZN5PointC1Ei            public
Point::Point       constructor    void (int, int)            -        global > class Point           10    -     1     _ZN5PointC1Eii       _ZN5PointC1Eii           public
Point::sum         method         int (void) const           -        global > class Point           11    -     1     _ZNK5Point3sumEv     _ZNK5Point3sumEv         public, defined
a                  parameter      int                        param    global > class Point > Point() 9     4     3     a.1                  -                        
a                  parameter      int                        param    global > class Point > Point() 10    4     1     a.2                  -                        
b                  parameter      int                        param    global > class Point > Point() 10    4     1     b.3                  -                        
Line               class_tag      class Line                 -        global                         14    -     0     Line                 -                        size 24
Line::from         field          class Point                member   global > class Line            15    8     2     Line::from           -                        private, offset 0
Line::to           field          class Point                member   global > class Line            15    8     2     Line::to             -                        private, offset 8
Line::uses         field          int &                      member   global > class Line            16    4     2     Line::uses           -                        private, offset 16
Line::count        field          int                        member   global > class Line            17    4     3     Line::count          -                        private, offset 20
Line::Line         constructor    void (class Point, class Point, int &) -        global > class Line            19    -     1     _ZN4LineC1E5PointS0_Ri _ZN4LineC1E5PointS0_Ri   public
Line::length       method         int (void) const           -        global > class Line            20    -     1     _ZNK4Line6lengthEv   _ZNK4Line6lengthEv       public, defined
Line::width        method         int (void) const           -        global > class Line            21    -     2     _ZNK4Line5widthEv    _ZNK4Line5widthEv        public, defined
peek               function       int (const class Line &)   -        global                         22    -     1     _Z4peekRK4Line       _Z4peekRK4Line           defined
a                  parameter      class Point                param    global > class Line > Line()   19    8     1     a.4                  -                        
b                  parameter      class Point                param    global > class Line > Line()   19    8     1     b.5                  -                        
u                  parameter      int &                      param    global > class Line > Line()   19    4     2     u.6                  -                        
l                  parameter      const class Line &         param    global > peek()                26    4     2     l.7                  -                        
Inspector          class_tag      class Inspector            -        global                         28    -     0     Inspector            -                        size 1
Inspector::look    method         int (class Line &)         -        global > class Inspector       30    -     1     _ZN9Inspector4lookER4Line _ZN9Inspector4lookER4Line public, defined
l                  parameter      class Line &               param    global > class Inspector > look() 30    4     3     l.8                  -                        
Counter            class_tag      class Counter              -        global                         33    -     0     Counter              -                        size 4
Counter::n         field          int                        member   global > class Counter         34    4     3     Counter::n           -                        private, offset 0
Counter::Counter   constructor    void (void)                -        global > class Counter         36    -     1     _ZN7CounterC1Ev      _ZN7CounterC1Ev          public
Counter::get       method         int (void) const           -        global > class Counter         37    -     1     _ZNK7Counter3getEv   _ZNK7Counter3getEv       public, defined
Counter::get       method         int (void)                 -        global > class Counter         38    -     1     _ZN7Counter3getEv    _ZN7Counter3getEv        public, defined
Counter::add       method         void (int)                 -        global > class Counter         39    -     1     _ZN7Counter3addEi    _ZN7Counter3addEi        public, defined
k                  parameter      int                        param    global > class Counter > add() 39    4     1     k.9                  -                        
Meters             class_tag      class Meters               -        global                         42    -     0     Meters               -                        size 4
Meters::v          field          int                        member   global > class Meters          44    4     1     Meters::v            -                        public, offset 0
Meters::Meters     constructor    void (int)                 -        global > class Meters          45    -     1     _ZN6MetersC1Ei       _ZN6MetersC1Ei           public
x                  parameter      int                        param    global > class Meters > Meters() 45    4     1     x.10                 -                        
useMeters          function       int (class Meters)         -        global                         47    -     1     _Z9useMeters6Meters  _Z9useMeters6Meters      defined
m                  parameter      class Meters               param    global > useMeters()           47    4     1     m.11                 -                        
Box                class_tag      class Box                  -        global                         49    -     0     Box                  -                        size 4
Box::w             field          int                        member   global > class Box             51    4     8     Box::w               -                        public, offset 0
Box::Box           constructor    void (int)                 -        global > class Box             52    -     3     _ZN3BoxC1Ei          _ZN3BoxC1Ei              public
Box::Box           constructor    void (const class Box &)   -        global > class Box             53    -     0     _ZN3BoxC1ERKS_       _ZN3BoxC1ERKS_           public
Box::~Box          destructor     void (void)                -        global > class Box             54    -     0     _ZN3BoxD1Ev          _ZN3BoxD1Ev              public
a                  parameter      int                        param    global > class Box > Box()     52    4     1     a.12                 -                        
o                  parameter      const class Box &          param    global > class Box > Box()     53    4     1     o.13                 -                        
byValue            function       int (class Box)            -        global                         56    -     1     _Z7byValue3Box       _Z7byValue3Box           defined
b                  parameter      class Box                  param    global > byValue()             56    4     1     b.14                 -                        
byRef              function       int (const class Box &)    -        global                         57    -     1     _Z5byRefRK3Box       _Z5byRefRK3Box           defined
b                  parameter      const class Box &          param    global > byRef()               57    4     1     b.15                 -                        
makeBox            function       class Box (int)            -        global                         58    -     1     _Z7makeBoxi          _Z7makeBoxi              defined
k                  parameter      int                        param    global > makeBox()             58    4     1     k.16                 -                        
pick               function       int (int)                  -        global                         59    -     1     _Z4picki             _Z4picki                 defined
a                  parameter      int                        param    global > pick()                59    4     1     a.17                 -                        
pick               function       int (class Box)            -        global                         60    -     0     _Z4pick3Box          _Z4pick3Box              defined
b                  parameter      class Box                  param    global > pick()                60    4     1     b.18                 -                        
Base               class_tag      class Base                 -        global                         62    -     0     Base                 -                        size 4
Base::tag          field          int                        member   global > class Base            64    4     1     Base::tag            -                        public, offset 0
Base::Base         constructor    void (int)                 -        global > class Base            65    -     1     _ZN4BaseC1Ei         _ZN4BaseC1Ei             public
t                  parameter      int                        param    global > class Base > Base()   65    4     2     t.19                 -                        
Derived            class_tag      class Derived              -        global                         67    -     0     Derived              -                        size 8, public base Base
Derived::extra     field          int                        member   global > class Derived         69    4     1     Derived::extra       -                        public, offset 4
Derived::Derived   constructor    void (int)                 -        global > class Derived         70    -     1     _ZN7DerivedC1Ei      _ZN7DerivedC1Ei          public
e                  parameter      int                        param    global > class Derived > Derived() 70    4     3     e.20                 -                        
area               function       int (class Point)          -        global                         73    -     1     _Z4area5Point        _Z4area5Point            defined
p                  parameter      class Point                param    global > area()                73    8     2     p.21                 -                        
main               function       int (void)                 -        global                         75    -     0     main                 main                     defined
uses               variable       int                        local    global > main()                76    4     2     uses.22              -                        
l                  variable       class Line                 local    global > main()                77    24    5     l.23                 -                        
in                 variable       class Inspector            local    global > main()                79    1     1     in.24                -                        
seen               variable       int                        local    global > main()                80    4     1     seen.25              -                        
c                  variable       class Counter              local    global > main()                83    4     3     c.26                 -                        
rc                 variable       const class Counter &      local    global > main()                84    4     1     rc.27                -                        
m                  variable       class Meters               local    global > main()                88    4     1     m.28                 -                        
b                  variable       class Box                  local    global > main()                93    4     1     b.29                 -                        
d                  variable       class Derived              local    global > main()                96    8     2     d.30                 -                        
a                  variable       int                        local    global > main()                97    4     1     a.31                 -                        
sum                variable       int                        local    global > main()                98    4     1     sum.32               -                        

=== Record Layouts ===
class Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
class Line: size 24, align 4
    +0  class Point from  [private]
    +8  class Point to  [private]
    +16  int & uses  [private]
    +20  int count  [private]
class Inspector: size 1, align 1
class Counter: size 4, align 4
    +0  int n  [private]
class Meters: size 4, align 4
    +0  int v  [public]
class Box: size 4, align 4
    +0  int w  [public]
class Base: size 4, align 4
    +0  int tag  [public]
class Derived: size 8, align 4
    (base Base, public)
    +4  int extra  [public]
