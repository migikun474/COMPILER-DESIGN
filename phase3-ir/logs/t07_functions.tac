=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t07_functions.c
Optimization : no optimization

Three address code generated: 17 function(s), 182 instruction(s) for 'test/t07_functions.c'.

globals (name, type, width, initial value)
    calls.25       int                        4  0
    global         int                        4  10
    ratio          double                     8  2.5

function fact(int)        link name: _Z4facti
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 100:     if n int<= 1 goto L1
 101:     goto L2
 102: L1: t1 = 1
 103:     goto L3
 104: L2: t2 = n int- 1
 105:     param t2
 106:     t3 = call fact(int), 1
 107:     t4 = n int* t3
 108:     t1 = t4
 109: L3: return t1

function fib(int)        link name: _Z3fibi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    t5             temp   int                        4     20
    total width 24
  code
 110:     if n int< 2 goto L4
 111:     goto L5
 112: L4: return n
 113: L5: t1 = n int- 1
 114:     param t1
 115:     t2 = call fib(int), 1
 116:     t3 = n int- 2
 117:     param t3
 118:     t4 = call fib(int), 1
 119:     t5 = t2 int+ t4
 120:     return t5

function gcd(int, int)        link name: _Z3gcdii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    total width 16
  code
 121: L6: if b int!= 0 goto L7
 122:     goto L8
 123: L7: t1 = a int% b
 124:     t = t1
 125:     a = b
 126:     b = t
 127:     goto L6
 128: L8: return a

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    total width 4
  code
 129:   return 1

function pick(double)        link name: _Z4pickd
  symbol table (name, kind, type, width, offset)
    a              param  double                     8      0
    total width 8
  code
 130:   return 2

function pick(char *)        link name: _Z4pickPc
  symbol table (name, kind, type, width, offset)
    s              param  char *                     4      0
    total width 4
  code
 131:   return 3

function pick(int, int)        link name: _Z4pickii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    total width 8
  code
 132:   return 4

function bump(int &)        link name: _Z4bumpRi
  symbol table (name, kind, type, width, offset)
    r              param  int &                      4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 133:   t1 = *r
 134:   t2 = t1 int+ 1
 135:   *r = t2
 136:   return

function exchange(int &, int &)        link name: _Z8exchangeRiS_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    total width 20
  code
 137:   t1 = *a
 138:   t = t1
 139:   t2 = *b
 140:   *a = t2
 141:   *b = t
 142:   return

function largest(int &, int &)        link name: _Z7largestRiS_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 143:      t1 = *a
 144:      t2 = *b
 145:      if t1 int> t2 goto L9
 146:      goto L10
 147: L9:  return a
 148: L10: return b

function half(const double &)        link name: _Z4halfRKd
  symbol table (name, kind, type, width, offset)
    v              param  const double &             4      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    total width 24
  code
 149:   t1 = *v
 150:   t2 = t1 double/ 2.0
 151:   return t2

function sum(int, ...)        link name: _Z3sumiz
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    ap             local  va_list                    4      4
    s              local  int                        4      8
    i              local  int                        4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    total width 28
  code
 152:      va_start ap, n
 153:      s = 0
 154:      i = 0
 155: L11: if i int< n goto L12
 156:      goto L13
 157: L12: t1 = va_arg ap, int
 158:      t2 = s int+ t1
 159:      s = t2
 160:      t3 = i int+ 1
 161:      i = t3
 162:      goto L11
 163: L13: va_end ap
 164:      return s

function mix(int, ...)        link name: _Z3mixiz
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    ap             local  va_list                    4      4
    s              local  double                     8      8
    t1             temp   double                     8     16
    t2             temp   int                        4     24
    t3             temp   double                     8     32
    t4             temp   double                     8     40
    total width 48
  code
 165:   va_start ap, n
 166:   t1 = va_arg ap, double
 167:   t2 = va_arg ap, int
 168:   t3 = inttodouble t2
 169:   t4 = t1 double+ t3
 170:   s = t4
 171:   va_end ap
 172:   return s

function counter()        link name: _Z7counterv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 173:   t1 = calls.25 int+ 1
 174:   calls.25 = t1
 175:   return calls.25

function scale(int)        link name: _Z5scalei
  symbol table (name, kind, type, width, offset)
    k              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 176:   t1 = global int* k
 177:   global = t1
 178:   return

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    text           local  char[4]                    4      0
    x              local  int                        4      4
    y              local  int                        4      8
    alias          local  int &                      4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    t5             temp   int                        4     32
    t6             temp   int                        4     36
    t7             temp   char (*)[4]                4     40
    t8             temp   int                        4     44
    t9             temp   int                        4     48
    t10            temp   int                        4     52
    t11            temp   int *                      4     56
    t12            temp   int *                      4     60
    t13            temp   int *                      4     64
    t14            temp   int *                      4     68
    t15            temp   int                        4     72
    t16            temp   int                        4     76
    t17            temp   int *                      4     80
    t18            temp   int *                      4     84
    t19            temp   int &                      4     88
    t20            temp   double                     8     96
    t21            temp   const double *             4    104
    t22            temp   double                     8    112
    t23            temp   int                        4    120
    t24            temp   int                        4    124
    t25            temp   double                     8    128
    t26            temp   int                        4    136
    t27            temp   double                     8    144
    t28            temp   double                     8    152
    t29            temp   int                        4    160
    total width 164
  code
 179:   param 6
 180:   t1 = call fact(int), 1
 181:   param 10
 182:   t2 = call fib(int), 1
 183:   param 84
 184:   param 36
 185:   t3 = call gcd(int, int), 2
 186:   param 4
 187:   t4 = call later(int), 1
 188:   param "%d %d %d %d\n"
 189:   param t1
 190:   param t2
 191:   param t3
 192:   param t4
 193:   call printf, 5
 194:   text[0] = 97
 195:   text[1] = 98
 196:   text[2] = 99
 197:   text[3] = 0
 198:   param 1
 199:   t5 = call pick(int), 1
 200:   param 2.5
 201:   t6 = call pick(double), 1
 202:   t7 = &text
 203:   param t7
 204:   t8 = call pick(char *), 1
 205:   param 1
 206:   param 2
 207:   t9 = call pick(int, int), 2
 208:   param 99
 209:   t10 = call pick(int), 1
 210:   param "%d %d %d %d %d\n"
 211:   param t5
 212:   param t6
 213:   param t8
 214:   param t9
 215:   param t10
 216:   call printf, 6
 217:   x = 5
 218:   y = 9
 219:   t11 = &x
 220:   param t11
 221:   call bump(int &), 1
 222:   t12 = &x
 223:   t13 = &y
 224:   param t12
 225:   param t13
 226:   call exchange(int &, int &), 2
 227:   t14 = &x
 228:   alias = t14
 229:   t15 = *alias
 230:   t16 = t15 int+ 100
 231:   *alias = t16
 232:   t17 = &x
 233:   t18 = &y
 234:   param t17
 235:   param t18
 236:   t19 = call largest(int &, int &), 2
 237:   *t19 = 0
 238:   t20 = 5.0
 239:   t21 = &t20
 240:   param t21
 241:   t22 = call half(const double &), 1
 242:   param "%d %d %.2f\n"
 243:   param x
 244:   param y
 245:   param t22
 246:   call printf, 4
 247:   param 3
 248:   param 10
 249:   param 20
 250:   param 30
 251:   t23 = call sum(int, ...), 4
 252:   param 0
 253:   t24 = call sum(int, ...), 1
 254:   param 2
 255:   param 1.5
 256:   param 4
 257:   t25 = call mix(int, ...), 3
 258:   param "%d %d %.1f\n"
 259:   param t23
 260:   param t24
 261:   param t25
 262:   call printf, 4
 263:   call counter(), 0
 264:   call counter(), 0
 265:   t26 = call counter(), 0
 266:   param "%d\n"
 267:   param t26
 268:   call printf, 2
 269:   param 3
 270:   call scale(int), 1
 271:   t27 = inttodouble global
 272:   t28 = ratio double* t27
 273:   param "%d %.1f\n"
 274:   param global
 275:   param t28
 276:   call printf, 3
 277:   param 1
 278:   t29 = call later(int), 1
 279:   return t29

function later(int)        link name: _Z5lateri
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 280:   t1 = n int* 11
 281:   return t1


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
later              function       int (int)                  -        global                         6     -     2     _Z5lateri            _Z5lateri                defined
fact               function       int (int)                  -        global                         8     -     2     _Z4facti             _Z4facti                 defined
n                  parameter      int                        param    global > fact()                8     4     3     n.1                  -                        
fib                function       int (int)                  -        global                         9     -     3     _Z3fibi              _Z3fibi                  defined
n                  parameter      int                        param    global > fib()                 9     4     4     n.2                  -                        
gcd                function       int (int, int)             -        global                         10    -     1     _Z3gcdii             _Z3gcdii                 defined
a                  parameter      int                        param    global > gcd()                 10    4     3     a.3                  -                        
b                  parameter      int                        param    global > gcd()                 10    4     4     b.4                  -                        
t                  variable       int                        local    global > gcd() > while         10    4     1     t.5                  -                        
pick               function       int (int)                  -        global                         12    -     2     _Z4picki             _Z4picki                 defined
a                  parameter      int                        param    global > pick()                12    4     0     a.6                  -                        
pick               function       int (double)               -        global                         13    -     1     _Z4pickd             _Z4pickd                 defined
a                  parameter      double                     param    global > pick()                13    8     0     a.7                  -                        
pick               function       int (char *)               -        global                         14    -     1     _Z4pickPc            _Z4pickPc                defined
s                  parameter      char *                     param    global > pick()                14    4     0     s.8                  -                        
pick               function       int (int, int)             -        global                         15    -     1     _Z4pickii            _Z4pickii                defined
a                  parameter      int                        param    global > pick()                15    4     0     a.9                  -                        
b                  parameter      int                        param    global > pick()                15    4     0     b.10                 -                        
bump               function       void (int &)               -        global                         17    -     1     _Z4bumpRi            _Z4bumpRi                defined
r                  parameter      int &                      param    global > bump()                17    4     2     r.11                 -                        
exchange           function       void (int &, int &)        -        global                         18    -     1     _Z8exchangeRiS_      _Z8exchangeRiS_          defined
a                  parameter      int &                      param    global > exchange()            18    4     2     a.12                 -                        
b                  parameter      int &                      param    global > exchange()            18    4     2     b.13                 -                        
t                  variable       int                        local    global > exchange()            18    4     1     t.14                 -                        
largest            function       int &(int &, int &)        -        global                         19    -     1     _Z7largestRiS_       _Z7largestRiS_           defined
a                  parameter      int &                      param    global > largest()             19    4     2     a.15                 -                        
b                  parameter      int &                      param    global > largest()             19    4     2     b.16                 -                        
half               function       double (const double &)    -        global                         20    -     1     _Z4halfRKd           _Z4halfRKd               defined
v                  parameter      const double &             param    global > half()                20    4     1     v.17                 -                        
sum                function       int (int, ...)             -        global                         22    -     2     _Z3sumiz             _Z3sumiz                 defined
n                  parameter      int                        param    global > sum()                 22    4     2     n.18                 -                        
ap                 variable       va_list                    local    global > sum()                 23    4     3     ap.19                -                        
s                  variable       int                        local    global > sum()                 25    4     2     s.20                 -                        
i                  variable       int                        local    global > sum() > for           26    4     2     i.21                 -                        
mix                function       double (int, ...)          -        global                         31    -     1     _Z3mixiz             _Z3mixiz                 defined
n                  parameter      int                        param    global > mix()                 31    4     1     n.22                 -                        
ap                 variable       va_list                    local    global > mix()                 32    4     4     ap.23                -                        
s                  variable       double                     local    global > mix()                 34    8     1     s.24                 -                        
counter            function       int (void)                 -        global                         39    -     3     _Z7counterv          _Z7counterv              defined
calls              variable       int                        static   global > counter()             40    4     2     calls.25             -                        static
global             variable       int                        global   global                         45    4     4     global               -                        
ratio              variable       double                     global   global                         46    8     1     ratio                -                        
scale              function       void (int)                 -        global                         47    -     1     _Z5scalei            _Z5scalei                defined
k                  parameter      int                        param    global > scale()               47    4     1     k.26                 -                        
main               function       int (void)                 -        global                         49    -     0     main                 main                     defined
text               variable       char[4]                    local    global > main()                51    4     1     text.27              -                        
x                  variable       int                        local    global > main()                54    4     5     x.28                 -                        
y                  variable       int                        local    global > main()                54    4     3     y.29                 -                        
alias              variable       int &                      local    global > main()                57    4     2     alias.30             -                        
n                  parameter      int                        param    global > later()               70    4     1     n.31                 -                        

=== Record Layouts ===
(no records)
