=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t29_registers.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 314 -> 267 instruction(s) for 'test/t29_registers.c'.

optimization summary (-O1)
    instructions                314 -> 267   (14% fewer)
    constants folded            1
    algebraic simplifications   3
    common subexpressions       6
    copies / constants forwarded 21
    temporaries merged away     27
    dead instructions removed   7
    jumps removed or redirected 13
    unreachable instructions    2

function depth(int)        link name: _Z5depthi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    a              local  int                        4      4
    b              local  int                        4      8
    c              local  int                        4     12
    below          local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    t8             temp   int                        4     48
    total width 52
  code
 100:     t1 = n int<< 1
 101:     a = t1
 102:     t2 = n int+ 7
 103:     b = t2
 104:     c = t1 int- t2
 105:     if n int!= 0 goto L1
 106:     return 1
 107: L1: t4 = n int- 1
 108:     param t4
 109:     t5 = call depth(int), 1
 110:     below = t5
 111:     t6 = a int+ b
 112:     t7 = t6 int+ c
 113:     t8 = t7 int+ t5
 114:     return t8

function many(int)        link name: _Z4manyi
  symbol table (name, kind, type, width, offset)
    x              param  int                        4      0
    a              local  int                        4      4
    b              local  int                        4      8
    c              local  int                        4     12
    d              local  int                        4     16
    e              local  int                        4     20
    f              local  int                        4     24
    g              local  int                        4     28
    h              local  int                        4     32
    i              local  int                        4     36
    j              local  int                        4     40
    k              local  int                        4     44
    l              local  int                        4     48
    s              local  int                        4     52
    t              local  int                        4     56
    t1             temp   int                        4     60
    t2             temp   int                        4     64
    t3             temp   int                        4     68
    t4             temp   int                        4     72
    t5             temp   int                        4     76
    t6             temp   int                        4     80
    t7             temp   int                        4     84
    t8             temp   int                        4     88
    t9             temp   int                        4     92
    t10            temp   int                        4     96
    t11            temp   int                        4    100
    t12            temp   int                        4    104
    t13            temp   int                        4    108
    t14            temp   int                        4    112
    t15            temp   int                        4    116
    t16            temp   int                        4    120
    t17            temp   int                        4    124
    t18            temp   int                        4    128
    t19            temp   int                        4    132
    t20            temp   int                        4    136
    t21            temp   int                        4    140
    t22            temp   int                        4    144
    t23            temp   int                        4    148
    t24            temp   int                        4    152
    t25            temp   int                        4    156
    t26            temp   int                        4    160
    t27            temp   int                        4    164
    t28            temp   int                        4    168
    t29            temp   int                        4    172
    t30            temp   int                        4    176
    t31            temp   int                        4    180
    t32            temp   int                        4    184
    t33            temp   int                        4    188
    t34            temp   int                        4    192
    t35            temp   int                        4    196
    t36            temp   int                        4    200
    t37            temp   int                        4    204
    t38            temp   int                        4    208
    total width 212
  code
 115:     a = x int+ 1
 116:     b = x int+ 2
 117:     c = x int+ 3
 118:     d = x int+ 4
 119:     e = x int+ 5
 120:     f = x int+ 6
 121:     g = x int+ 7
 122:     h = x int+ 8
 123:     i = x int+ 9
 124:     j = x int+ 10
 125:     k = x int+ 11
 126:     l = x int+ 12
 127:     s = 0
 128:     t = 0
 129: L2: if t int>= 3 goto L3
 130:     t13 = a int* b
 131:     t14 = c int* d
 132:     t15 = t13 int+ t14
 133:     t16 = e int* f
 134:     t17 = t15 int+ t16
 135:     t18 = g int* h
 136:     t19 = t17 int+ t18
 137:     t20 = i int* j
 138:     t21 = t19 int+ t20
 139:     t22 = k int* l
 140:     t23 = t21 int+ t22
 141:     t24 = t23 int+ t
 142:     s = s int+ t24
 143:     t = t int+ 1
 144:     goto L2
 145: L3: t27 = s int+ a
 146:     t28 = t27 int+ b
 147:     t29 = t28 int+ c
 148:     t30 = t29 int+ d
 149:     t31 = t30 int+ e
 150:     t32 = t31 int+ f
 151:     t33 = t32 int+ g
 152:     t34 = t33 int+ h
 153:     t35 = t34 int+ i
 154:     t36 = t35 int+ j
 155:     t37 = t36 int+ k
 156:     t38 = t37 int+ l
 157:     return t38

function three(int, int, int)        link name: _Z5threeiii
  symbol table (name, kind, type, width, offset)
    p              param  int                        4      0
    q              param  int                        4      4
    r              param  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    total width 28
  code
 158:   t1 = p int* 100
 159:   t2 = q int* 10
 160:   t3 = t1 int+ t2
 161:   t4 = t3 int+ r
 162:   return t4

function twice(int)        link name: _Z5twicei
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 163:   t1 = v int<< 1
 164:   return t1

function arguments(int, int, int)        link name: _Z9argumentsiii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    c              param  int                        4      8
    x              local  int                        4     12
    y              local  int                        4     16
    z              local  int                        4     20
    t1             temp   int                        4     24
    t2             temp   int                        4     28
    t3             temp   int                        4     32
    t4             temp   int                        4     36
    t5             temp   int                        4     40
    t6             temp   int                        4     44
    t7             temp   int                        4     48
    t8             temp   int                        4     52
    t9             temp   int                        4     56
    t10            temp   int                        4     60
    t11            temp   int                        4     64
    total width 68
  code
 165:   t1 = a int+ 1
 166:   x = t1
 167:   param b
 168:   t2 = call twice(int), 1
 169:   t3 = c int- 1
 170:   param t1
 171:   param t2
 172:   param t3
 173:   t4 = call three(int, int, int), 3
 174:   y = t4
 175:   param a
 176:   t5 = call twice(int), 1
 177:   param b
 178:   t6 = call twice(int), 1
 179:   param t6
 180:   t7 = call twice(int), 1
 181:   param c
 182:   t8 = call twice(int), 1
 183:   t9 = t8 int+ t1
 184:   param t5
 185:   param t7
 186:   param t9
 187:   t10 = call three(int, int, int), 3
 188:   z = t10
 189:   t11 = t4 int+ t10
 190:   return t11

function characters(const char *)        link name: _Z10charactersPKc
  symbol table (name, kind, type, width, offset)
    s              param  const char *               4      0
    c              local  char                       1      4
    u              local  unsigned char              1      5
    h              local  short                      2      6
    any            local  bool                       1      8
    signs          local  int                        4     12
    i              local  int                        4     16
    same           local  unsigned char              1     20
    t1             temp   const char *               4     24
    t2             temp   char                       1     28
    t3             temp   int                        4     32
    t4             temp   const char *               4     36
    t5             temp   char                       1     40
    t6             temp   int                        4     44
    t7             temp   int                        4     48
    t8             temp   char                       1     52
    t9             temp   int                        4     56
    t10            temp   const char *               4     60
    t11            temp   char                       1     64
    t12            temp   int                        4     68
    t13            temp   int                        4     72
    t14            temp   unsigned char              1     76
    t15            temp   int                        4     80
    t16            temp   int                        4     84
    t17            temp   const char *               4     88
    t18            temp   char                       1     92
    t19            temp   int                        4     96
    t20            temp   int                        4    100
    t21            temp   short                      2    104
    t22            temp   int                        4    108
    t23            temp   int                        4    112
    t24            temp   int                        4    116
    t25            temp   const char *               4    120
    t26            temp   char                       1    124
    t27            temp   int                        4    128
    t28            temp   bool                       1    132
    t29            temp   int                        4    136
    t30            temp   int                        4    140
    t31            temp   int                        4    144
    t32            temp   int                        4    148
    t33            temp   int                        4    152
    t34            temp   int                        4    156
    t35            temp   int                        4    160
    t36            temp   int                        4    164
    t37            temp   int                        4    168
    t38            temp   int                        4    172
    t39            temp   int                        4    176
    t40            temp   int                        4    180
    t41            temp   int                        4    184
    total width 188
  code
 191:      c = 0
 192:      u = 0
 193:      h = 0
 194:      any = 0
 195:      signs = 0
 196:      i = 0
 197: L4:  t1 = s ptr+ i
 198:      t2 = *t1
 199:      if t2 char== 0 goto L10
 200:      t3 = chartoint c
 201:      t4 = s ptr+ i
 202:      t5 = *t4
 203:      t6 = chartoint t5
 204:      t7 = t3 int+ t6
 205:      t8 = inttochar t7
 206:      c = t8
 207:      t9 = uchartoint u
 208:      t13 = t9 int+ t6
 209:      u = inttouchar t13
 210:      t15 = shorttoint h
 211:      t16 = t15 int* 31
 212:      t20 = t16 int+ t6
 213:      h = inttoshort t20
 214:      t22 = chartoint t8
 215:      if t22 int>= 0 goto L5
 216:      signs = signs int+ 1
 217: L5:  if any bool!= 0 goto L6
 218:      t25 = s ptr+ i
 219:      t26 = *t25
 220:      t27 = chartoint t26
 221:      if t27 int== 122 goto L6
 222:      t24 = 0
 223:      goto L7
 224: L6:  t24 = 1
 225: L7:  if t24 int!= 0 goto L8
 226:      t28 = 0
 227:      goto L9
 228: L8:  t28 = 1
 229: L9:  any = t28
 230:      i = i int+ 1
 231:      goto L4
 232: L10: same = c
 233:      t30 = chartoint c
 234:      t31 = uchartoint u
 235:      t32 = t31 int<< 1
 236:      t33 = t30 int+ t32
 237:      t34 = shorttoint h
 238:      t35 = t33 int+ t34
 239:      t36 = signs int* 1000
 240:      t37 = t35 int+ t36
 241:      t38 = booltoint any
 242:      t39 = t37 int+ t38
 243:      t40 = uchartoint c
 244:      t41 = t39 int+ t40
 245:      return t41

function half(double)        link name: _Z4halfd
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    t1             temp   double                     8      8
    total width 16
  code
 246:   t1 = v double/ 2.0
 247:   return t1

function numbers(int)        link name: _Z7numbersi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    a              local  double                     8      8
    b              local  double                     8     16
    c              local  double                     8     24
    d              local  double                     8     32
    e              local  double                     8     40
    f              local  double                     8     48
    g              local  double                     8     56
    total          local  double                     8     64
    small          local  float                      4     72
    i              local  int                        4     76
    t1             temp   double                     8     80
    t2             temp   double                     8     88
    t3             temp   double                     8     96
    t4             temp   double                     8    104
    t5             temp   double                     8    112
    t6             temp   double                     8    120
    t7             temp   double                     8    128
    t8             temp   double                     8    136
    t9             temp   double                     8    144
    t10            temp   double                     8    152
    t11            temp   float                      4    160
    t12            temp   int                        4    164
    t13            temp   double                     8    168
    t14            temp   double                     8    176
    t15            temp   double                     8    184
    t16            temp   double                     8    192
    total width 200
  code
 248:      a = 1.5
 249:      b = 2.5
 250:      c = 0.25
 251:      d = 4.0
 252:      e = 0.125
 253:      f = 8.0
 254:      g = 16.5
 255:      total = 0.0
 256:      small = 0.5
 257:      i = 0
 258: L11: if i int>= n goto L12
 259:      t1 = a double* b
 260:      t2 = c double* d
 261:      t3 = t1 double+ t2
 262:      t4 = e double* f
 263:      t5 = t3 double+ t4
 264:      t6 = t5 double+ g
 265:      t7 = total double+ t6
 266:      total = t7
 267:      param t7
 268:      t8 = call half(double), 1
 269:      t9 = floattodouble small
 270:      t10 = t8 double+ t9
 271:      total = t10
 272:      small = small float* 1.5
 273:      if t10 double> 1e+03 goto L12
 274:      i = i int+ 1
 275:      goto L11
 276: L12: t13 = total double+ a
 277:      t14 = t13 double+ g
 278:      t15 = floattodouble small
 279:      t16 = t14 double+ t15
 280:      return t16

function jumps(int)        link name: _Z5jumpsi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    i              local  int                        4      4
    s              local  int                        4      8
    last           local  int                        4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    t5             temp   int                        4     32
    t6             temp   int                        4     36
    total width 40
  code
 281:      i = 0
 282:      s = 0
 283:      last = -1
 284: L13: if i int>= n goto L14
 285:      t2 = i int* i
 286:      s = s int+ t2
 287:      last = i
 288:      i = i int+ 1
 289:      goto L13
 290: L14: t5 = s int* 10
 291:      t6 = t5 int+ last
 292:      return t6

function mixed(int)        link name: _Z5mixedi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    before         local  int                        4      4
    sum            local  int                        4      8
    i              local  int                        4     12
    inside         local  int                        4     16
    after          local  int                        4     20
    t1             temp   int                        4     24
    t2             temp   int                        4     28
    t3             temp   int                        4     32
    t4             temp   int                        4     36
    t5             temp   int                        4     40
    t6             temp   int                        4     44
    t7             temp   int                        4     48
    t8             temp   int                        4     52
    t9             temp   int                        4     56
    total width 60
  code
 293:      before = n int* 3
 294:      sum = 0
 295:      i = 0
 296: L15: if i int>= n goto L18
 297:      t2 = i int* before
 298:      inside = t2
 299:      t3 = t2 int% 7
 300:      t4 = sum int+ t3
 301:      sum = t4
 302:      if t4 int<= 50 goto L16
 303:      sum = sum int- before
 304:      goto L17
 305: L16: param i
 306:      t6 = call twice(int), 1
 307:      sum = sum int+ t6
 308: L17: i = i int+ 1
 309:      goto L15
 310: L18: t9 = sum int+ before
 311:      after = t9
 312:      return t9

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    t2             temp   int                        4      4
    t3             temp   int                        4      8
    t4             temp   int                        4     12
    t5             temp   int                        4     16
    t6             temp   int                        4     20
    t7             temp   double                     8     24
    t8             temp   double                     8     32
    t9             temp   double                     8     40
    t10            temp   int                        4     48
    t11            temp   int                        4     52
    t12            temp   int                        4     56
    t13            temp   int                        4     60
    t14            temp   int                        4     64
    total width 68
  code
 313:   param 5
 314:   t1 = call depth(int), 1
 315:   param 3
 316:   t2 = call many(int), 1
 317:   param "%d %d\n"
 318:   param t1
 319:   param t2
 320:   call printf, 3
 321:   param 1
 322:   param 2
 323:   param 3
 324:   t3 = call arguments(int, int, int), 3
 325:   param 4
 326:   param 0
 327:   param 9
 328:   t4 = call arguments(int, int, int), 3
 329:   param "%d %d\n"
 330:   param t3
 331:   param t4
 332:   call printf, 3
 333:   param "register allocation"
 334:   t5 = call characters(const char *), 1
 335:   param "zzzzzzzzzzzzzzzzzzzz"
 336:   t6 = call characters(const char *), 1
 337:   param "%d %d\n"
 338:   param t5
 339:   param t6
 340:   call printf, 3
 341:   param 0
 342:   t7 = call numbers(int), 1
 343:   param 3
 344:   t8 = call numbers(int), 1
 345:   param 40
 346:   t9 = call numbers(int), 1
 347:   param "%.4f %.4f %.4f\n"
 348:   param t7
 349:   param t8
 350:   param t9
 351:   call printf, 4
 352:   param 0
 353:   t10 = call jumps(int), 1
 354:   param 5
 355:   t11 = call jumps(int), 1
 356:   param 9
 357:   t12 = call mixed(int), 1
 358:   param "%d %d %d\n"
 359:   param t10
 360:   param t11
 361:   param t12
 362:   call printf, 4
 363:   param 3
 364:   t13 = call jumps(int), 1
 365:   t14 = t13 int% 100
 366:   return t14


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
depth              function       int (int)                  -        global                         7     -     2     _Z5depthi            _Z5depthi                defined
n                  parameter      int                        param    global > depth()               7     4     4     n.1                  -                        
a                  variable       int                        local    global > depth()               8     4     2     a.2                  -                        
b                  variable       int                        local    global > depth()               8     4     2     b.3                  -                        
c                  variable       int                        local    global > depth()               8     4     1     c.4                  -                        
below              variable       int                        local    global > depth()               10    4     1     below.5              -                        
many               function       int (int)                  -        global                         14    -     1     _Z4manyi             _Z4manyi                 defined
x                  parameter      int                        param    global > many()                14    4     12    x.6                  -                        
a                  variable       int                        local    global > many()                15    4     2     a.7                  -                        
b                  variable       int                        local    global > many()                15    4     2     b.8                  -                        
c                  variable       int                        local    global > many()                15    4     2     c.9                  -                        
d                  variable       int                        local    global > many()                15    4     2     d.10                 -                        
e                  variable       int                        local    global > many()                15    4     2     e.11                 -                        
f                  variable       int                        local    global > many()                15    4     2     f.12                 -                        
g                  variable       int                        local    global > many()                16    4     2     g.13                 -                        
h                  variable       int                        local    global > many()                16    4     2     h.14                 -                        
i                  variable       int                        local    global > many()                16    4     2     i.15                 -                        
j                  variable       int                        local    global > many()                16    4     2     j.16                 -                        
k                  variable       int                        local    global > many()                16    4     2     k.17                 -                        
l                  variable       int                        local    global > many()                16    4     2     l.18                 -                        
s                  variable       int                        local    global > many()                17    4     2     s.19                 -                        
t                  variable       int                        local    global > many() > for          18    4     3     t.20                 -                        
three              function       int (int, int, int)        -        global                         22    -     2     _Z5threeiii          _Z5threeiii              defined
p                  parameter      int                        param    global > three()               22    4     1     p.21                 -                        
q                  parameter      int                        param    global > three()               22    4     1     q.22                 -                        
r                  parameter      int                        param    global > three()               22    4     1     r.23                 -                        
twice              function       int (int)                  -        global                         23    -     6     _Z5twicei            _Z5twicei                defined
v                  parameter      int                        param    global > twice()               23    4     1     v.24                 -                        
arguments          function       int (int, int, int)        -        global                         24    -     2     _Z9argumentsiii      _Z9argumentsiii          defined
a                  parameter      int                        param    global > arguments()           24    4     2     a.25                 -                        
b                  parameter      int                        param    global > arguments()           24    4     2     b.26                 -                        
c                  parameter      int                        param    global > arguments()           24    4     2     c.27                 -                        
x                  variable       int                        local    global > arguments()           25    4     2     x.28                 -                        
y                  variable       int                        local    global > arguments()           26    4     1     y.29                 -                        
z                  variable       int                        local    global > arguments()           27    4     1     z.30                 -                        
characters         function       int (const char *)         -        global                         31    -     2     _Z10charactersPKc    _Z10charactersPKc        defined
s                  parameter      const char *               param    global > characters()          31    4     5     s.31                 -                        
c                  variable       char                       local    global > characters()          32    1     5     c.32                 -                        
u                  variable       unsigned char              local    global > characters()          33    1     3     u.33                 -                        
h                  variable       short                      local    global > characters()          34    2     3     h.34                 -                        
any                variable       bool                       local    global > characters()          35    1     3     any.35               -                        
signs              variable       int                        local    global > characters()          36    4     2     signs.36             -                        
i                  variable       int                        local    global > characters() > for    37    4     6     i.37                 -                        
same               variable       unsigned char              local    global > characters()          44    1     1     same.38              -                        
half               function       double (double)            -        global                         48    -     1     _Z4halfd             _Z4halfd                 defined
v                  parameter      double                     param    global > half()                48    8     1     v.39                 -                        
numbers            function       double (int)               -        global                         49    -     3     _Z7numbersi          _Z7numbersi              defined
n                  parameter      int                        param    global > numbers()             49    4     1     n.40                 -                        
a                  variable       double                     local    global > numbers()             50    8     2     a.41                 -                        
b                  variable       double                     local    global > numbers()             50    8     1     b.42                 -                        
c                  variable       double                     local    global > numbers()             50    8     1     c.43                 -                        
d                  variable       double                     local    global > numbers()             50    8     1     d.44                 -                        
e                  variable       double                     local    global > numbers()             50    8     1     e.45                 -                        
f                  variable       double                     local    global > numbers()             50    8     1     f.46                 -                        
g                  variable       double                     local    global > numbers()             50    8     2     g.47                 -                        
total              variable       double                     local    global > numbers()             50    8     5     total.48             -                        
small              variable       float                      local    global > numbers()             51    4     4     small.49             -                        
i                  variable       int                        local    global > numbers() > for       52    4     2     i.50                 -                        
jumps              function       int (int)                  -        global                         61    -     3     _Z5jumpsi            _Z5jumpsi                defined
n                  parameter      int                        param    global > jumps()               61    4     1     n.51                 -                        
done               label          -                          -        global > jumps()               69    -     1     _Z5jumpsi.done       -                        
top                label          -                          -        global > jumps()               63    -     1     _Z5jumpsi.top        -                        
i                  variable       int                        local    global > jumps()               62    4     5     i.52                 -                        
s                  variable       int                        local    global > jumps()               62    4     2     s.53                 -                        
last               variable       int                        local    global > jumps()               62    4     2     last.54              -                        
mixed              function       int (int)                  -        global                         73    -     1     _Z5mixedi            _Z5mixedi                defined
n                  parameter      int                        param    global > mixed()               73    4     2     n.55                 -                        
before             variable       int                        local    global > mixed()               74    4     3     before.56            -                        
sum                variable       int                        local    global > mixed()               74    4     5     sum.57               -                        
i                  variable       int                        local    global > mixed() > for         75    4     4     i.58                 -                        
inside             variable       int                        local    global > mixed() > for > for body 76    4     1     inside.59            -                        
after              variable       int                        local    global > mixed()               81    4     1     after.60             -                        
main               function       int (void)                 -        global                         85    -     0     main                 main                     defined

=== Record Layouts ===
(no records)
