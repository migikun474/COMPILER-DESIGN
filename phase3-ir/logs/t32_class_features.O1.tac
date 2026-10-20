=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t32_class_features.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 268 -> 244 instruction(s) for 'test/t32_class_features.c'.

optimization summary (-O1)
    instructions                268 -> 244   (8% fewer)
    constants folded            0
    algebraic simplifications   2
    common subexpressions       23
    copies / constants forwarded 27
    temporaries merged away     0
    dead instructions removed   24
    jumps removed or redirected 0
    unreachable instructions    0

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
 102:   t2 = a int<< 1
 103:   *t1 = t2
 104:   param "(P%d) "
 105:   param a
 106:   call printf, 2
 107:   return

function Point::Point(int, int)        link name: _ZN5PointC1Eii
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    a              param  int                        4      4
    b              param  int                        4      8
    t1             temp   class Point *              4     12
    t2             temp   class Point *              4     16
    total width 20
  code
 108:   *this = a
 109:   t1 = this ptr+ 4
 110:   *t1 = b
 111:   return

function Point::sum()        link name: _ZNK5Point3sumEv
  symbol table (name, kind, type, width, offset)
    this           param  class Point *              4      0
    t1             temp   int                        4      4
    t2             temp   class Point *              4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 112:   t1 = *this
 113:   t2 = this ptr+ 4
 114:   t3 = *t2
 115:   t4 = t1 int+ t3
 116:   return t4

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
 117:   *this = a
 118:   t1 = this ptr+ 8
 119:   *t1 = b
 120:   t2 = this ptr+ 16
 121:   *t2 = u
 122:   t4 = this ptr+ 20
 123:   *t4 = 0
 124:   t7 = *t2
 125:   t8 = *t7
 126:   t9 = t8 int+ 1
 127:   *t7 = t9
 128:   return

function Line::length()        link name: _ZNK4Line6lengthEv
  symbol table (name, kind, type, width, offset)
    this           param  class Line *               4      0
    t1             temp   class Line *               4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 129:   t1 = this ptr+ 8
 130:   t2 = *t1
 131:   t3 = *this
 132:   t4 = t2 int- t3
 133:   return t4

function Line::width()        link name: _ZNK4Line5widthEv
  symbol table (name, kind, type, width, offset)
    this           param  class Line *               4      0
    t1             temp   class Line *               4      4
    t2             temp   int                        4      8
    total width 12
  code
 134:   t1 = this ptr+ 20
 135:   t2 = *t1
 136:   return t2

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
 137:   t1 = l ptr+ 4
 138:   t2 = *t1
 139:   t3 = l ptr+ 12
 140:   t4 = *t3
 141:   t5 = t2 int+ t4
 142:   return t5

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
 143:   t1 = l ptr+ 20
 144:   *t1 = 9
 145:   t2 = l ptr+ 16
 146:   t3 = *t2
 147:   t4 = *t3
 148:   t7 = t4 int+ 9
 149:   return t7

function Counter::Counter()        link name: _ZN7CounterC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    total width 4
  code
 150:   *this = 0
 151:   return

function Counter::get()        link name: _ZNK7Counter3getEv
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    t1             temp   int                        4      4
    total width 8
  code
 152:   t1 = *this
 153:   return t1

function Counter::get()        link name: _ZN7Counter3getEv
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 154:   t1 = *this
 155:   t2 = t1 int+ 100
 156:   return t2

function Counter::add(int)        link name: _ZN7Counter3addEi
  symbol table (name, kind, type, width, offset)
    this           param  class Counter *            4      0
    k              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 157:   t1 = *this
 158:   t2 = t1 int+ k
 159:   *this = t2
 160:   return

function Meters::Meters(int)        link name: _ZN6MetersC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Meters *             4      0
    x              param  int                        4      4
    total width 8
  code
 161:   *this = x
 162:   return

function useMeters(class Meters)        link name: _Z9useMeters6Meters
  symbol table (name, kind, type, width, offset)
    m              param  class Meters               4      0
    t1             temp   int                        4      4
    total width 8
  code
 163:   t1 = m[0]
 164:   return t1

function Box::Box(int)        link name: _ZN3BoxC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Box *                4      0
    a              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 165:   *this = a
 166:   param "[+%d] "
 167:   param a
 168:   call printf, 2
 169:   return

function Box::Box(const class Box &)        link name: _ZN3BoxC1ERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Box *                4      0
    o              param  const class Box &          4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 170:   t1 = *o
 171:   t2 = t1 int+ 100
 172:   *this = t2
 173:   param "[copy %d] "
 174:   param t2
 175:   call printf, 2
 176:   return

function Box::~Box()        link name: _ZN3BoxD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Box *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 177:   t1 = *this
 178:   param "[-%d] "
 179:   param t1
 180:   call printf, 2
 181:   return

function byValue(class Box)        link name: _Z7byValue3Box
  symbol table (name, kind, type, width, offset)
    b              param  class Box                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 182:   t1 = b[0]
 183:   return t1

function byRef(const class Box &)        link name: _Z5byRefRK3Box
  symbol table (name, kind, type, width, offset)
    b              param  const class Box &          4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 184:   t1 = *b
 185:   t2 = t1 int<< 1
 186:   return t2

function makeBox(int)        link name: _Z7makeBoxi
  symbol table (name, kind, type, width, offset)
    k              param  int                        4      0
    t1             temp   class Box                  4      4
    t2             temp   class Box *                4      8
    t3             temp   int                        4     12
    total width 16
  code
 187:   t2 = &t1
 188:   t3 = k int* 3
 189:   param t2                            (this)
 190:   param t3
 191:   call Box::Box(int), 2
 192:   return t1

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    total width 4
  code
 193:   return a

function pick(class Box)        link name: _Z4pick3Box
  symbol table (name, kind, type, width, offset)
    b              param  class Box                  4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 194:   t1 = b[0]
 195:   t2 = t1 int+ 1000
 196:   return t2

function Base::Base(int)        link name: _ZN4BaseC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Base *               4      0
    t              param  int                        4      4
    total width 8
  code
 197:   *this = t
 198:   param "<B%d> "
 199:   param t
 200:   call printf, 2
 201:   return

function Derived::Derived(int)        link name: _ZN7DerivedC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Derived *            4      0
    e              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   class Derived *            4     12
    t3             temp   class Derived *            4     16
    total width 20
  code
 202:   t1 = e int* 10
 203:   param this                          (this)
 204:   param t1
 205:   call Base::Base(int), 2
 206:   t2 = this ptr+ 4
 207:   *t2 = e
 208:   param "<D%d> "
 209:   param e
 210:   call printf, 2
 211:   return

function area(class Point)        link name: _Z4area5Point
  symbol table (name, kind, type, width, offset)
    p              param  class Point                8      0
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 212:   t1 = p[0]
 213:   t2 = p[4]
 214:   t3 = t1 int* t2
 215:   return t3

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
 216:   uses = 0
 217:   t1 = &l
 218:   t3 = &t2
 219:   param t3                            (this)
 220:   param 1
 221:   param 5
 222:   call Point::Point(int, int), 3
 223:   t5 = &t4
 224:   param t5                            (this)
 225:   param 4
 226:   call Point::Point(int), 2
 227:   t6 = &uses
 228:   param t1                            (this)
 229:   param t2
 230:   param t4
 231:   param t6
 232:   call Line::Line(class Point, class Point, int &), 4
 233:   param t1                            (this)
 234:   t8 = call Line::length(), 1
 235:   param t1                            (this)
 236:   t10 = call Line::width(), 1
 237:   param t1
 238:   t12 = call peek(const class Line &), 1
 239:   param "| %d %d %d %d\n"
 240:   param t8
 241:   param t10
 242:   param t12
 243:   param uses
 244:   call printf, 5
 245:   t13 = &in
 246:   param t13                           (this)
 247:   param t1
 248:   t15 = call Inspector::look(class Line &), 2
 249:   seen = t15
 250:   param t1                            (this)
 251:   t17 = call Line::width(), 1
 252:   param "%d %d\n"
 253:   param t15
 254:   param t17
 255:   call printf, 3
 256:   t18 = &c
 257:   param t18                           (this)
 258:   call Counter::Counter(), 1
 259:   rc = t18
 260:   param t18                           (this)
 261:   param 3
 262:   call Counter::add(int), 2
 263:   param t18                           (this)
 264:   t22 = call Counter::get(), 1
 265:   param t18                           (this)
 266:   t23 = call Counter::get(), 1
 267:   param "%d %d\n"
 268:   param t22
 269:   param t23
 270:   call printf, 3
 271:   t24 = &m
 272:   param t24                           (this)
 273:   param 7
 274:   call Meters::Meters(int), 2
 275:   param m
 276:   t25 = call useMeters(class Meters), 1
 277:   param "%d\n"
 278:   param t25
 279:   call printf, 2
 280:   t27 = &t26
 281:   param t27                           (this)
 282:   param 5
 283:   call Box::Box(int), 2
 284:   param t26
 285:   t28 = call byValue(class Box), 1
 286:   param "%d | "
 287:   param t28
 288:   call printf, 2
 289:   param t27                           (this)
 290:   call Box::~Box(), 1
 291:   t31 = &t30
 292:   param t31                           (this)
 293:   param 6
 294:   call Box::Box(int), 2
 295:   param t31
 296:   t33 = call byRef(const class Box &), 1
 297:   param "%d | "
 298:   param t33
 299:   call printf, 2
 300:   param t31                           (this)
 301:   call Box::~Box(), 1
 302:   param 7
 303:   t35 = call pick(int), 1
 304:   param "%d | "
 305:   param t35
 306:   call printf, 2
 307:   param 4
 308:   t36 = call makeBox(int), 1
 309:   b = t36
 310:   t38 = &b
 311:   t39 = b[0]
 312:   param "%d\n"
 313:   param t39
 314:   call printf, 2
 315:   t40 = &d
 316:   param t40                           (this)
 317:   param 3
 318:   call Derived::Derived(int), 2
 319:   t42 = &t41
 320:   param t42                           (this)
 321:   param 6
 322:   call Point::Point(int), 2
 323:   param t41
 324:   t43 = call area(class Point), 1
 325:   a = t43
 326:   t45 = &t44
 327:   param t45                           (this)
 328:   param 2
 329:   call Point::Point(int), 2
 330:   param t45                           (this)
 331:   t47 = call Point::sum(), 1
 332:   sum = t47
 333:   t48 = d[0]
 334:   t49 = d[4]
 335:   param "%d %d | %d %d\n"
 336:   param t48
 337:   param t49
 338:   param t43
 339:   param t47
 340:   call printf, 5
 341:   param t38                           (this)
 342:   call Box::~Box(), 1
 343:   return 0


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
