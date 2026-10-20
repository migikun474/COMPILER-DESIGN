=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t07_functions.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 182 -> 169 instruction(s) for 'test/t07_functions.c'.

optimization summary (-O1)
    instructions                182 -> 169   (7% fewer)
    constants folded            0
    algebraic simplifications   0
    common subexpressions       4
    copies / constants forwarded 10
    temporaries merged away     4
    dead instructions removed   4
    jumps removed or redirected 5
    unreachable instructions    0

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
 100:     if n int> 1 goto L1
 101:     t1 = 1
 102:     goto L2
 103: L1: t2 = n int- 1
 104:     param t2
 105:     t3 = call fact(int), 1
 106:     t1 = n int* t3
 107: L2: return t1

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
 108:     if n int>= 2 goto L3
 109:     return n
 110: L3: t1 = n int- 1
 111:     param t1
 112:     t2 = call fib(int), 1
 113:     t3 = n int- 2
 114:     param t3
 115:     t4 = call fib(int), 1
 116:     t5 = t2 int+ t4
 117:     return t5

function gcd(int, int)        link name: _Z3gcdii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    total width 16
  code
 118: L4: if b int== 0 goto L5
 119:     t1 = a int% b
 120:     t = t1
 121:     a = b
 122:     b = t1
 123:     goto L4
 124: L5: return a

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    total width 4
  code
 125:   return 1

function pick(double)        link name: _Z4pickd
  symbol table (name, kind, type, width, offset)
    a              param  double                     8      0
    total width 8
  code
 126:   return 2

function pick(char *)        link name: _Z4pickPc
  symbol table (name, kind, type, width, offset)
    s              param  char *                     4      0
    total width 4
  code
 127:   return 3

function pick(int, int)        link name: _Z4pickii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    total width 8
  code
 128:   return 4

function bump(int &)        link name: _Z4bumpRi
  symbol table (name, kind, type, width, offset)
    r              param  int &                      4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 129:   t1 = *r
 130:   t2 = t1 int+ 1
 131:   *r = t2
 132:   return

function exchange(int &, int &)        link name: _Z8exchangeRiS_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    total width 20
  code
 133:   t1 = *a
 134:   t = t1
 135:   t2 = *b
 136:   *a = t2
 137:   *b = t1
 138:   return

function largest(int &, int &)        link name: _Z7largestRiS_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 139:     t1 = *a
 140:     t2 = *b
 141:     if t1 int<= t2 goto L6
 142:     return a
 143: L6: return b

function half(const double &)        link name: _Z4halfRKd
  symbol table (name, kind, type, width, offset)
    v              param  const double &             4      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    total width 24
  code
 144:   t1 = *v
 145:   t2 = t1 double/ 2.0
 146:   return t2

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
 147:     va_start ap, n
 148:     s = 0
 149:     i = 0
 150: L7: if i int>= n goto L8
 151:     t1 = va_arg ap, int
 152:     s = s int+ t1
 153:     i = i int+ 1
 154:     goto L7
 155: L8: va_end ap
 156:     return s

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
 157:   va_start ap, n
 158:   t1 = va_arg ap, double
 159:   t2 = va_arg ap, int
 160:   t3 = inttodouble t2
 161:   t4 = t1 double+ t3
 162:   s = t4
 163:   va_end ap
 164:   return t4

function counter()        link name: _Z7counterv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 165:   t1 = calls.25 int+ 1
 166:   calls.25 = t1
 167:   return t1

function scale(int)        link name: _Z5scalei
  symbol table (name, kind, type, width, offset)
    k              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 168:   global = global int* k
 169:   return

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
 170:   param 6
 171:   t1 = call fact(int), 1
 172:   param 10
 173:   t2 = call fib(int), 1
 174:   param 84
 175:   param 36
 176:   t3 = call gcd(int, int), 2
 177:   param 4
 178:   t4 = call later(int), 1
 179:   param "%d %d %d %d\n"
 180:   param t1
 181:   param t2
 182:   param t3
 183:   param t4
 184:   call printf, 5
 185:   text[0] = 97
 186:   text[1] = 98
 187:   text[2] = 99
 188:   text[3] = 0
 189:   param 1
 190:   t5 = call pick(int), 1
 191:   param 2.5
 192:   t6 = call pick(double), 1
 193:   t7 = &text
 194:   param t7
 195:   t8 = call pick(char *), 1
 196:   param 1
 197:   param 2
 198:   t9 = call pick(int, int), 2
 199:   param 99
 200:   t10 = call pick(int), 1
 201:   param "%d %d %d %d %d\n"
 202:   param t5
 203:   param t6
 204:   param t8
 205:   param t9
 206:   param t10
 207:   call printf, 6
 208:   x = 5
 209:   y = 9
 210:   t11 = &x
 211:   param t11
 212:   call bump(int &), 1
 213:   t13 = &y
 214:   param t11
 215:   param t13
 216:   call exchange(int &, int &), 2
 217:   alias = t11
 218:   t15 = *t11
 219:   t16 = t15 int+ 100
 220:   *t11 = t16
 221:   param t11
 222:   param t13
 223:   t19 = call largest(int &, int &), 2
 224:   *t19 = 0
 225:   t20 = 5.0
 226:   t21 = &t20
 227:   param t21
 228:   t22 = call half(const double &), 1
 229:   param "%d %d %.2f\n"
 230:   param x
 231:   param y
 232:   param t22
 233:   call printf, 4
 234:   param 3
 235:   param 10
 236:   param 20
 237:   param 30
 238:   t23 = call sum(int, ...), 4
 239:   param 0
 240:   t24 = call sum(int, ...), 1
 241:   param 2
 242:   param 1.5
 243:   param 4
 244:   t25 = call mix(int, ...), 3
 245:   param "%d %d %.1f\n"
 246:   param t23
 247:   param t24
 248:   param t25
 249:   call printf, 4
 250:   call counter(), 0
 251:   call counter(), 0
 252:   t26 = call counter(), 0
 253:   param "%d\n"
 254:   param t26
 255:   call printf, 2
 256:   param 3
 257:   call scale(int), 1
 258:   t27 = inttodouble global
 259:   t28 = ratio double* t27
 260:   param "%d %.1f\n"
 261:   param global
 262:   param t28
 263:   call printf, 3
 264:   param 1
 265:   t29 = call later(int), 1
 266:   return t29

function later(int)        link name: _Z5lateri
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 267:   t1 = n int* 11
 268:   return t1


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
