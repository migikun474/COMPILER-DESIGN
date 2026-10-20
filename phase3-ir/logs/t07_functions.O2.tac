=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t07_functions.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 182 -> 165 instruction(s) for 'test/t07_functions.c'.

optimization summary (-O2)
    instructions                182 -> 165   (9% fewer)
    constants folded            0
    algebraic simplifications   0
    common subexpressions       4
    copies / constants forwarded 10
    temporaries merged away     4
    dead instructions removed   4
    jumps removed or redirected 5
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    4

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
 120:     a = b
 121:     b = t1
 122:     goto L4
 123: L5: return a

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    total width 4
  code
 124:   return 1

function pick(double)        link name: _Z4pickd
  symbol table (name, kind, type, width, offset)
    a              param  double                     8      0
    total width 8
  code
 125:   return 2

function pick(char *)        link name: _Z4pickPc
  symbol table (name, kind, type, width, offset)
    s              param  char *                     4      0
    total width 4
  code
 126:   return 3

function pick(int, int)        link name: _Z4pickii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    total width 8
  code
 127:   return 4

function bump(int &)        link name: _Z4bumpRi
  symbol table (name, kind, type, width, offset)
    r              param  int &                      4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 128:   t1 = *r
 129:   t2 = t1 int+ 1
 130:   *r = t2
 131:   return

function exchange(int &, int &)        link name: _Z8exchangeRiS_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    total width 20
  code
 132:   t1 = *a
 133:   t2 = *b
 134:   *a = t2
 135:   *b = t1
 136:   return

function largest(int &, int &)        link name: _Z7largestRiS_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 137:     t1 = *a
 138:     t2 = *b
 139:     if t1 int<= t2 goto L6
 140:     return a
 141: L6: return b

function half(const double &)        link name: _Z4halfRKd
  symbol table (name, kind, type, width, offset)
    v              param  const double &             4      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    total width 24
  code
 142:   t1 = *v
 143:   t2 = t1 double/ 2.0
 144:   return t2

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
 145:     va_start ap, n
 146:     s = 0
 147:     i = 0
 148: L7: if i int>= n goto L8
 149:     t1 = va_arg ap, int
 150:     s = s int+ t1
 151:     i = i int+ 1
 152:     goto L7
 153: L8: va_end ap
 154:     return s

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
 155:   va_start ap, n
 156:   t1 = va_arg ap, double
 157:   t2 = va_arg ap, int
 158:   t3 = inttodouble t2
 159:   t4 = t1 double+ t3
 160:   va_end ap
 161:   return t4

function counter()        link name: _Z7counterv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 162:   t1 = calls.25 int+ 1
 163:   calls.25 = t1
 164:   return t1

function scale(int)        link name: _Z5scalei
  symbol table (name, kind, type, width, offset)
    k              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 165:   global = global int* k
 166:   return

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
 167:   param 6
 168:   t1 = call fact(int), 1
 169:   param 10
 170:   t2 = call fib(int), 1
 171:   param 84
 172:   param 36
 173:   t3 = call gcd(int, int), 2
 174:   param 4
 175:   t4 = call later(int), 1
 176:   param "%d %d %d %d\n"
 177:   param t1
 178:   param t2
 179:   param t3
 180:   param t4
 181:   call printf, 5
 182:   text[0] = 97
 183:   text[1] = 98
 184:   text[2] = 99
 185:   text[3] = 0
 186:   param 1
 187:   t5 = call pick(int), 1
 188:   param 2.5
 189:   t6 = call pick(double), 1
 190:   t7 = &text
 191:   param t7
 192:   t8 = call pick(char *), 1
 193:   param 1
 194:   param 2
 195:   t9 = call pick(int, int), 2
 196:   param 99
 197:   t10 = call pick(int), 1
 198:   param "%d %d %d %d %d\n"
 199:   param t5
 200:   param t6
 201:   param t8
 202:   param t9
 203:   param t10
 204:   call printf, 6
 205:   x = 5
 206:   y = 9
 207:   t11 = &x
 208:   param t11
 209:   call bump(int &), 1
 210:   t13 = &y
 211:   param t11
 212:   param t13
 213:   call exchange(int &, int &), 2
 214:   t15 = *t11
 215:   t16 = t15 int+ 100
 216:   *t11 = t16
 217:   param t11
 218:   param t13
 219:   t19 = call largest(int &, int &), 2
 220:   *t19 = 0
 221:   t20 = 5.0
 222:   t21 = &t20
 223:   param t21
 224:   t22 = call half(const double &), 1
 225:   param "%d %d %.2f\n"
 226:   param x
 227:   param y
 228:   param t22
 229:   call printf, 4
 230:   param 3
 231:   param 10
 232:   param 20
 233:   param 30
 234:   t23 = call sum(int, ...), 4
 235:   param 0
 236:   t24 = call sum(int, ...), 1
 237:   param 2
 238:   param 1.5
 239:   param 4
 240:   t25 = call mix(int, ...), 3
 241:   param "%d %d %.1f\n"
 242:   param t23
 243:   param t24
 244:   param t25
 245:   call printf, 4
 246:   call counter(), 0
 247:   call counter(), 0
 248:   t26 = call counter(), 0
 249:   param "%d\n"
 250:   param t26
 251:   call printf, 2
 252:   param 3
 253:   call scale(int), 1
 254:   t27 = inttodouble global
 255:   t28 = ratio double* t27
 256:   param "%d %.1f\n"
 257:   param global
 258:   param t28
 259:   call printf, 3
 260:   param 1
 261:   t29 = call later(int), 1
 262:   return t29

function later(int)        link name: _Z5lateri
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 263:   t1 = n int* 11
 264:   return t1


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
