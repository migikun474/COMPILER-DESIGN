=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t07_functions.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 182 -> 158 instruction(s) for 'test/t07_functions.c'.

optimization summary (-O3)
    instructions                182 -> 158   (13% fewer)
    constants folded            2
    algebraic simplifications   0
    common subexpressions       6
    copies / constants forwarded 38
    temporaries merged away     5
    dead instructions removed   31
    jumps removed or redirected 5
    unreachable instructions    0
    propagated across blocks    2
    dead assignments removed    6
    calls inlined               16
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

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
    t30            temp   int                        4    164
    t31            temp   int                        4    168
    t32            temp   int                        4    172
    t33            temp   int                        4    176
    t34            temp   int                        4    180
    t35            temp   int                        4    184
    t36            temp   double                     8    192
    t37            temp   char *                     4    200
    t38            temp   int                        4    204
    t39            temp   int                        4    208
    t40            temp   int                        4    212
    t41            temp   int &                      4    216
    t42            temp   int                        4    220
    t43            temp   int                        4    224
    t44            temp   int &                      4    228
    t45            temp   int &                      4    232
    t46            temp   int                        4    236
    t47            temp   int                        4    240
    t48            temp   int &                      4    244
    t49            temp   int &                      4    248
    t50            temp   int                        4    252
    t51            temp   int                        4    256
    t52            temp   const double &             4    260
    t53            temp   double                     8    264
    t54            temp   double                     8    272
    t55            temp   int                        4    280
    t56            temp   int                        4    284
    t57            temp   int                        4    288
    t58            temp   int                        4    292
    t59            temp   int                        4    296
    t60            temp   int                        4    300
    total width 304
  code
 167:      param 6
 168:      t1 = call fact(int), 1
 169:      param 10
 170:      t2 = call fib(int), 1
 171:      t30 = 84
 172:      t31 = 36
 173: L9:  if t31 int== 0 goto L10
 174:      t32 = t30 int% t31
 175:      t30 = t31
 176:      t31 = t32
 177:      goto L9
 178: L10: param "%d %d %d %d\n"
 179:      param t1
 180:      param t2
 181:      param t30
 182:      param 44
 183:      call printf, 5
 184:      text[0] = 97
 185:      text[1] = 98
 186:      text[2] = 99
 187:      text[3] = 0
 188:      param "%d %d %d %d %d\n"
 189:      param 1
 190:      param 2
 191:      param 3
 192:      param 4
 193:      param 1
 194:      call printf, 6
 195:      x = 5
 196:      y = 9
 197:      t11 = &x
 198:      t42 = *t11
 199:      t43 = t42 int+ 1
 200:      *t11 = t43
 201:      t13 = &y
 202:      t47 = *t13
 203:      *t11 = t47
 204:      *t13 = t43
 205:      t15 = *t11
 206:      t16 = t15 int+ 100
 207:      *t11 = t16
 208:      t51 = *t13
 209:      if t16 int<= t51 goto L11
 210:      t19 = t11
 211:      goto L12
 212: L11: t19 = t13
 213: L12: *t19 = 0
 214:      t20 = 5.0
 215:      t21 = &t20
 216:      t53 = *t21
 217:      t54 = t53 double/ 2.0
 218:      param "%d %d %.2f\n"
 219:      param x
 220:      param y
 221:      param t54
 222:      call printf, 4
 223:      param 3
 224:      param 10
 225:      param 20
 226:      param 30
 227:      t23 = call sum(int, ...), 4
 228:      param 0
 229:      t24 = call sum(int, ...), 1
 230:      param 2
 231:      param 1.5
 232:      param 4
 233:      t25 = call mix(int, ...), 3
 234:      param "%d %d %.1f\n"
 235:      param t23
 236:      param t24
 237:      param t25
 238:      call printf, 4
 239:      t55 = calls.25 int+ 1
 240:      calls.25 = t55
 241:      t56 = t55 int+ 1
 242:      calls.25 = t56
 243:      t57 = t56 int+ 1
 244:      calls.25 = t57
 245:      param "%d\n"
 246:      param t57
 247:      call printf, 2
 248:      global = global int* 3
 249:      t27 = inttodouble global
 250:      t28 = ratio double* t27
 251:      param "%d %.1f\n"
 252:      param global
 253:      param t28
 254:      call printf, 3
 255:      return 11

function later(int)        link name: _Z5lateri
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 256:   t1 = n int* 11
 257:   return t1


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
