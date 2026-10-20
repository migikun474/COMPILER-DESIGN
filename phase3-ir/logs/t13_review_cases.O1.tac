=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t13_review_cases.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 176 -> 162 instruction(s) for 'test/t13_review_cases.c'.

optimization summary (-O1)
    instructions                176 -> 162   (7% fewer)
    constants folded            3
    algebraic simplifications   0
    common subexpressions       4
    copies / constants forwarded 16
    temporaries merged away     3
    dead instructions removed   5
    jumps removed or redirected 5
    unreachable instructions    1

globals (name, type, width, initial value)
    Cnt::made      int                        4  5
    chosen         double                     8  2.5

function half(const double &)        link name: _Z4halfRKd
  symbol table (name, kind, type, width, offset)
    v              param  const double &             4      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    total width 24
  code
 100:   t1 = *v
 101:   t2 = t1 double/ 2.0
 102:   return t2

function A::A()        link name: _ZN1AC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class A *                  4      0
    total width 4
  code
 103:   *this = 1
 104:   return

function A::ga()        link name: _ZN1A2gaEv
  symbol table (name, kind, type, width, offset)
    this           param  class A *                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 105:   t1 = *this
 106:   return t1

function B::B()        link name: _ZN1BC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class B *                  4      0
    total width 4
  code
 107:   *this = 2
 108:   return

function B::gb()        link name: _ZN1B2gbEv
  symbol table (name, kind, type, width, offset)
    this           param  class B *                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 109:   t1 = *this
 110:   return t1

function C::C()        link name: _ZN1CC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class C *                  4      0
    t1             temp   class C *                  4      4
    t2             temp   class C *                  4      8
    total width 12
  code
 111:   param this                          (this)
 112:   call A::A(), 1
 113:   t1 = this ptr+ 4
 114:   param t1                            (this)
 115:   call B::B(), 1
 116:   t2 = this ptr+ 8
 117:   *t2 = 3
 118:   return

function C::sum()        link name: _ZN1C3sumEv
  symbol table (name, kind, type, width, offset)
    this           param  class C *                  4      0
    t1             temp   int                        4      4
    t2             temp   class C *                  4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    t5             temp   class C *                  4     20
    t6             temp   int                        4     24
    t7             temp   int                        4     28
    total width 32
  code
 119:   t1 = *this
 120:   t2 = this ptr+ 4
 121:   t3 = *t2
 122:   t4 = t1 int+ t3
 123:   t5 = this ptr+ 8
 124:   t6 = *t5
 125:   t7 = t4 int+ t6
 126:   return t7

function takeB(class B *)        link name: _Z5takeBP1B
  symbol table (name, kind, type, width, offset)
    p              param  class B *                  4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    total width 16
  code
 127:     if p ptr== 0 goto L1
 128:     t1 = *p
 129:     goto L2
 130: L1: t1 = -1
 131: L2: return t1

function Cnt::Cnt()        link name: _ZN3CntC1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Cnt *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 132:   t1 = Cnt::made int+ 1
 133:   Cnt::made = t1
 134:   *this = t1
 135:   return

function Dog::Dog(int)        link name: _ZN3DogC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    n              param  int                        4      4
    total width 8
  code
 136:   *this = n
 137:   return

function Dog::~Dog()        link name: _ZN3DogD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Dog *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 138:   t1 = *this
 139:   param "~Dog(%d)\n"
 140:   param t1
 141:   call printf, 2
 142:   return

function vsum(int, va_list)        link name: _Z4vsumiPv
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    ap             param  va_list                    4      4
    s              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    total width 28
  code
 143:     s = 0
 144: L3: t1 = n
 145:     n = n int- 1
 146:     if t1 int<= 0 goto L4
 147:     t3 = va_arg ap, int
 148:     s = s int+ t3
 149:     goto L3
 150: L4: return s

function total(int, ...)        link name: _Z5totaliz
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    ap             local  va_list                    4      4
    s              local  int                        4      8
    t1             temp   int                        4     12
    total width 16
  code
 151:   va_start ap, n
 152:   param n
 153:   param ap
 154:   t1 = call vsum(int, va_list), 2
 155:   s = t1
 156:   va_end ap
 157:   return t1

function one()        link name: _Z3onev
  code
 158:   return 1

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    k              local  int                        4      0
    c              local  class C                   12      4
    pb             local  class B *                  4     16
    none           local  class C *                  4     20
    nb             local  class B *                  4     24
    first          local  class A                    4     28
    guard          local  int                        4     32
    x              local  class Cnt                  4     36
    y              local  class Cnt                  4     40
    d              local  class Dog                  4     44
    last           local  class Dog                  4     48
    t1             temp   double                     8     56
    t2             temp   double                     8     64
    t3             temp   const double *             4     72
    t4             temp   double                     8     80
    t5             temp   double                     8     88
    t6             temp   const double *             4     96
    t7             temp   double                     8    104
    t8             temp   class C *                  4    112
    t9             temp   class C *                  4    116
    t10            temp   class B *                  4    120
    t11            temp   class B *                  4    124
    t12            temp   class C *                  4    128
    t13            temp   int                        4    132
    t14            temp   class C *                  4    136
    t15            temp   class C *                  4    140
    t16            temp   int                        4    144
    t17            temp   int                        4    148
    t18            temp   class C *                  4    152
    t19            temp   class B *                  4    156
    t20            temp   int                        4    160
    t21            temp   class C *                  4    164
    t22            temp   int                        4    168
    t23            temp   int                        4    172
    t24            temp   int                        4    176
    t25            temp   class A *                  4    180
    t26            temp   class A                    4    184
    t27            temp   int                        4    188
    t28            temp   class Cnt *                4    192
    t29            temp   class Cnt *                4    196
    t30            temp   int                        4    200
    t31            temp   int                        4    204
    t32            temp   int                        4    208
    t33            temp   class Dog *                4    212
    t34            temp   class Dog *                4    216
    t35            temp   class Dog *                4    220
    t36            temp   class Dog *                4    224
    total width 228
  code
 159:     k = 5
 160:     t1 = 5.0
 161:     t3 = &t1
 162:     param t3
 163:     t4 = call half(const double &), 1
 164:     t5 = 3.0
 165:     t6 = &t5
 166:     param t6
 167:     t7 = call half(const double &), 1
 168:     param "%.2f %.2f\n"
 169:     param t4
 170:     param t7
 171:     call printf, 3
 172:     t8 = &c
 173:     param t8                            (this)
 174:     call C::C(), 1
 175:     t9 = t8
 176:     t10 = t8
 177:     if t8 ptr== 0 goto L5
 178:     t10 = t9 ptr+ 4
 179: L5: pb = t10
 180:     none = 0
 181:     nb = 0
 182:     t12 = &c
 183:     param t12                           (this)
 184:     t13 = call C::sum(), 1
 185:     t15 = t12 ptr+ 4
 186:     param t15                           (this)
 187:     t16 = call B::gb(), 1
 188:     t17 = *t10
 189:     t18 = t12
 190:     t19 = t12
 191:     if t12 ptr== 0 goto L6
 192:     t19 = t18 ptr+ 4
 193: L6: param t19
 194:     t20 = call takeB(class B *), 1
 195:     t21 = &c
 196:     param t21                           (this)
 197:     t22 = call A::ga(), 1
 198:     if nb ptr== 0 goto L7
 199:     t23 = 0
 200:     goto L8
 201: L7: t23 = 1
 202: L8: param nb
 203:     t24 = call takeB(class B *), 1
 204:     param "%d %d %d %d %d %d %d\n"
 205:     param t13
 206:     param t16
 207:     param t17
 208:     param t20
 209:     param t22
 210:     param t23
 211:     param t24
 212:     call printf, 8
 213:     t25 = &first
 214:     t26 = c[0]
 215:     *t25 = t26
 216:     guard = 77
 217:     t27 = first[0]
 218:     param "%d %d\n"
 219:     param t27
 220:     param 77
 221:     call printf, 3
 222:     t28 = &x
 223:     param t28                           (this)
 224:     call Cnt::Cnt(), 1
 225:     t29 = &y
 226:     param t29                           (this)
 227:     call Cnt::Cnt(), 1
 228:     t30 = x[0]
 229:     t31 = y[0]
 230:     param "%d %d %d\n"
 231:     param Cnt::made
 232:     param t30
 233:     param t31
 234:     call printf, 4
 235:     param 3
 236:     param 1
 237:     param 2
 238:     param 3
 239:     t32 = call total(int, ...), 4
 240:     param "%.1f %d\n"
 241:     param chosen
 242:     param t32
 243:     call printf, 3
 244:     t33 = &d
 245:     param t33                           (this)
 246:     param 1
 247:     call Dog::Dog(int), 2
 248:     if k int== 0 goto L9
 249:     call one(), 0
 250: L9: t34 = &d
 251:     param t34                           (this)
 252:     call Dog::~Dog(), 1
 253:     param "after the block\n"
 254:     call printf, 1
 255:     t35 = &last
 256:     param t35                           (this)
 257:     param 2
 258:     call Dog::Dog(int), 2
 259:     param t35                           (this)
 260:     call Dog::~Dog(), 1
 261:     return 0


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
half               function       double (const double &)    -        global                         6     -     2     _Z4halfRKd           _Z4halfRKd               defined
v                  parameter      const double &             param    global > half()                6     4     1     v.1                  -                        
A                  class_tag      class A                    -        global                         8     -     0     A                    -                        size 4
A::a               field          int                        member   global > class A               8     4     4     A::a                 -                        public, offset 0
A::A               constructor    void (void)                -        global > class A               8     -     1     _ZN1AC1Ev            _ZN1AC1Ev                public
A::ga              method         int (void)                 -        global > class A               8     -     1     _ZN1A2gaEv           _ZN1A2gaEv               public, defined
B                  class_tag      class B                    -        global                         9     -     0     B                    -                        size 4
B::b               field          int                        member   global > class B               9     4     5     B::b                 -                        public, offset 0
B::B               constructor    void (void)                -        global > class B               9     -     1     _ZN1BC1Ev            _ZN1BC1Ev                public
B::gb              method         int (void)                 -        global > class B               9     -     1     _ZN1B2gbEv           _ZN1B2gbEv               public, defined
C                  class_tag      class C                    -        global                         10    -     0     C                    -                        size 12, public base A, public base B
C::c               field          int                        member   global > class C               12    4     2     C::c                 -                        public, offset 8
C::C               constructor    void (void)                -        global > class C               13    -     1     _ZN1CC1Ev            _ZN1CC1Ev                public
C::sum             method         int (void)                 -        global > class C               14    -     1     _ZN1C3sumEv          _ZN1C3sumEv              public, defined
takeB              function       int (class B *)            -        global                         16    -     2     _Z5takeBP1B          _Z5takeBP1B              defined
p                  parameter      class B *                  param    global > takeB()               16    4     2     p.2                  -                        
Cnt                class_tag      class Cnt                  -        global                         18    -     0     Cnt                  -                        size 4
Cnt::made          field          int                        static   global > class Cnt             20    4     3     Cnt::made            -                        public, static
Cnt::id            field          int                        member   global > class Cnt             21    4     3     Cnt::id              -                        public, offset 0
Cnt::Cnt           constructor    void (void)                -        global > class Cnt             22    -     2     _ZN3CntC1Ev          _ZN3CntC1Ev              public
Dog                class_tag      class Dog                  -        global                         26    -     0     Dog                  -                        size 4
Dog::id            field          int                        member   global > class Dog             28    4     2     Dog::id              -                        public, offset 0
Dog::Dog           constructor    void (int)                 -        global > class Dog             29    -     2     _ZN3DogC1Ei          _ZN3DogC1Ei              public
Dog::~Dog          destructor     void (void)                -        global > class Dog             30    -     0     _ZN3DogD1Ev          _ZN3DogD1Ev              public
n                  parameter      int                        param    global > class Dog > Dog()     29    4     1     n.3                  -                        
chosen             variable       double                     global   global                         33    8     1     chosen               -                        
vsum               function       int (int, va_list)         -        global                         35    -     1     _Z4vsumiPv           _Z4vsumiPv               defined
n                  parameter      int                        param    global > vsum()                35    4     1     n.4                  -                        
ap                 parameter      va_list                    param    global > vsum()                35    4     1     ap.5                 -                        
s                  variable       int                        local    global > vsum()                36    4     2     s.6                  -                        
total              function       int (int, ...)             -        global                         40    -     1     _Z5totaliz           _Z5totaliz               defined
n                  parameter      int                        param    global > total()               40    4     2     n.7                  -                        
ap                 variable       va_list                    local    global > total()               41    4     3     ap.8                 -                        
s                  variable       int                        local    global > total()               43    4     1     s.9                  -                        
one                function       int (void)                 -        global                         48    -     1     _Z3onev              _Z3onev                  defined
main               function       int (void)                 -        global                         50    -     0     main                 main                     defined
k                  variable       int                        local    global > main()                51    4     2     k.10                 -                        
c                  variable       class C                    local    global > main()                54    12    6     c.11                 -                        
pb                 variable       class B *                  local    global > main()                55    4     1     pb.12                -                        
none               variable       class C *                  local    global > main()                56    4     1     none.13              -                        
nb                 variable       class B *                  local    global > main()                57    4     2     nb.14                -                        
first              variable       class A                    local    global > main()                59    4     1     first.15             -                        
guard              variable       int                        local    global > main()                60    4     1     guard.16             -                        
x                  variable       class Cnt                  local    global > main()                63    4     1     x.17                 -                        
y                  variable       class Cnt                  local    global > main()                63    4     1     y.18                 -                        
d                  variable       class Dog                  local    global > main() > block        68    4     0     d.19                 -                        
last               variable       class Dog                  local    global > main() > block        73    4     0     last.20              -                        

=== Record Layouts ===
class A: size 4, align 4
    +0  int a  [public]
class B: size 4, align 4
    +0  int b  [public]
class C: size 12, align 4
    (base A, public)
    (base B, public)
    +8  int c  [public]
class Cnt: size 4, align 4
    static  int made  [public]
    +0  int id  [public]
class Dog: size 4, align 4
    +0  int id  [public]
