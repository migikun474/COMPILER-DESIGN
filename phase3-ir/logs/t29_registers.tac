=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t29_registers.c
Optimization : no optimization

Three address code generated: 11 function(s), 314 instruction(s) for 'test/t29_registers.c'.

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
 100:     t1 = n int* 2
 101:     a = t1
 102:     t2 = n int+ 7
 103:     b = t2
 104:     t3 = a int- b
 105:     c = t3
 106:     if n int== 0 goto L1
 107:     goto L2
 108: L1: return 1
 109: L2: t4 = n int- 1
 110:     param t4
 111:     t5 = call depth(int), 1
 112:     below = t5
 113:     t6 = a int+ b
 114:     t7 = t6 int+ c
 115:     t8 = t7 int+ below
 116:     return t8

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
 117:     t1 = x int+ 1
 118:     a = t1
 119:     t2 = x int+ 2
 120:     b = t2
 121:     t3 = x int+ 3
 122:     c = t3
 123:     t4 = x int+ 4
 124:     d = t4
 125:     t5 = x int+ 5
 126:     e = t5
 127:     t6 = x int+ 6
 128:     f = t6
 129:     t7 = x int+ 7
 130:     g = t7
 131:     t8 = x int+ 8
 132:     h = t8
 133:     t9 = x int+ 9
 134:     i = t9
 135:     t10 = x int+ 10
 136:     j = t10
 137:     t11 = x int+ 11
 138:     k = t11
 139:     t12 = x int+ 12
 140:     l = t12
 141:     s = 0
 142:     t = 0
 143: L3: if t int< 3 goto L4
 144:     goto L5
 145: L4: t13 = a int* b
 146:     t14 = c int* d
 147:     t15 = t13 int+ t14
 148:     t16 = e int* f
 149:     t17 = t15 int+ t16
 150:     t18 = g int* h
 151:     t19 = t17 int+ t18
 152:     t20 = i int* j
 153:     t21 = t19 int+ t20
 154:     t22 = k int* l
 155:     t23 = t21 int+ t22
 156:     t24 = t23 int+ t
 157:     t25 = s int+ t24
 158:     s = t25
 159:     t26 = t int+ 1
 160:     t = t26
 161:     goto L3
 162: L5: t27 = s int+ a
 163:     t28 = t27 int+ b
 164:     t29 = t28 int+ c
 165:     t30 = t29 int+ d
 166:     t31 = t30 int+ e
 167:     t32 = t31 int+ f
 168:     t33 = t32 int+ g
 169:     t34 = t33 int+ h
 170:     t35 = t34 int+ i
 171:     t36 = t35 int+ j
 172:     t37 = t36 int+ k
 173:     t38 = t37 int+ l
 174:     return t38

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
 175:   t1 = p int* 100
 176:   t2 = q int* 10
 177:   t3 = t1 int+ t2
 178:   t4 = t3 int+ r
 179:   return t4

function twice(int)        link name: _Z5twicei
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 180:   t1 = v int* 2
 181:   return t1

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
 182:   t1 = a int+ 1
 183:   x = t1
 184:   param b
 185:   t2 = call twice(int), 1
 186:   t3 = c int- 1
 187:   param x
 188:   param t2
 189:   param t3
 190:   t4 = call three(int, int, int), 3
 191:   y = t4
 192:   param a
 193:   t5 = call twice(int), 1
 194:   param b
 195:   t6 = call twice(int), 1
 196:   param t6
 197:   t7 = call twice(int), 1
 198:   param c
 199:   t8 = call twice(int), 1
 200:   t9 = t8 int+ x
 201:   param t5
 202:   param t7
 203:   param t9
 204:   t10 = call three(int, int, int), 3
 205:   z = t10
 206:   t11 = y int+ z
 207:   return t11

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
 208:      c = 0
 209:      u = 0
 210:      h = 0
 211:      any = 0
 212:      signs = 0
 213:      i = 0
 214: L6:  t1 = s ptr+ i
 215:      t2 = *t1
 216:      if t2 char!= 0 goto L7
 217:      goto L16
 218: L7:  t3 = chartoint c
 219:      t4 = s ptr+ i
 220:      t5 = *t4
 221:      t6 = chartoint t5
 222:      t7 = t3 int+ t6
 223:      t8 = inttochar t7
 224:      c = t8
 225:      t9 = uchartoint u
 226:      t10 = s ptr+ i
 227:      t11 = *t10
 228:      t12 = chartoint t11
 229:      t13 = t9 int+ t12
 230:      t14 = inttouchar t13
 231:      u = t14
 232:      t15 = shorttoint h
 233:      t16 = t15 int* 31
 234:      t17 = s ptr+ i
 235:      t18 = *t17
 236:      t19 = chartoint t18
 237:      t20 = t16 int+ t19
 238:      t21 = inttoshort t20
 239:      h = t21
 240:      t22 = chartoint c
 241:      if t22 int< 0 goto L8
 242:      goto L9
 243: L8:  t23 = signs int+ 1
 244:      signs = t23
 245: L9:  if any bool!= 0 goto L12
 246:      goto L10
 247: L10: t25 = s ptr+ i
 248:      t26 = *t25
 249:      t27 = chartoint t26
 250:      if t27 int== 122 goto L12
 251:      goto L11
 252: L11: t24 = 0
 253:      goto L13
 254: L12: t24 = 1
 255: L13: if t24 int!= 0 goto L14
 256:      t28 = 0
 257:      goto L15
 258: L14: t28 = 1
 259: L15: any = t28
 260:      t29 = i int+ 1
 261:      i = t29
 262:      goto L6
 263: L16: same = c
 264:      t30 = chartoint c
 265:      t31 = uchartoint u
 266:      t32 = t31 int* 2
 267:      t33 = t30 int+ t32
 268:      t34 = shorttoint h
 269:      t35 = t33 int+ t34
 270:      t36 = signs int* 1000
 271:      t37 = t35 int+ t36
 272:      t38 = booltoint any
 273:      t39 = t37 int+ t38
 274:      t40 = uchartoint same
 275:      t41 = t39 int+ t40
 276:      return t41

function half(double)        link name: _Z4halfd
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    t1             temp   double                     8      8
    total width 16
  code
 277:   t1 = v double/ 2.0
 278:   return t1

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
 279:      a = 1.5
 280:      b = 2.5
 281:      c = 0.25
 282:      d = 4.0
 283:      e = 0.125
 284:      f = 8.0
 285:      g = 16.5
 286:      total = 0.0
 287:      small = 0.5
 288:      i = 0
 289: L17: if i int< n goto L18
 290:      goto L21
 291: L18: t1 = a double* b
 292:      t2 = c double* d
 293:      t3 = t1 double+ t2
 294:      t4 = e double* f
 295:      t5 = t3 double+ t4
 296:      t6 = t5 double+ g
 297:      t7 = total double+ t6
 298:      total = t7
 299:      param total
 300:      t8 = call half(double), 1
 301:      t9 = floattodouble small
 302:      t10 = t8 double+ t9
 303:      total = t10
 304:      t11 = small float* 1.5
 305:      small = t11
 306:      if total double> 1e+03 goto L19
 307:      goto L20
 308: L19: goto L21
 309: L20: t12 = i int+ 1
 310:      i = t12
 311:      goto L17
 312: L21: t13 = total double+ a
 313:      t14 = t13 double+ g
 314:      t15 = floattodouble small
 315:      t16 = t14 double+ t15
 316:      return t16

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
 317:      i = 0
 318:      s = 0
 319:      t1 = int- 1
 320:      last = t1
 321: L22: if i int>= n goto L23
 322:      goto L24
 323: L23: goto L25
 324: L24: t2 = i int* i
 325:      t3 = s int+ t2
 326:      s = t3
 327:      last = i
 328:      t4 = i int+ 1
 329:      i = t4
 330:      goto L22
 331: L25: t5 = s int* 10
 332:      t6 = t5 int+ last
 333:      return t6

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
 334:      t1 = n int* 3
 335:      before = t1
 336:      sum = 0
 337:      i = 0
 338: L26: if i int< n goto L27
 339:      goto L31
 340: L27: t2 = i int* before
 341:      inside = t2
 342:      t3 = inside int% 7
 343:      t4 = sum int+ t3
 344:      sum = t4
 345:      if sum int> 50 goto L28
 346:      goto L29
 347: L28: t5 = sum int- before
 348:      sum = t5
 349:      goto L30
 350: L29: param i
 351:      t6 = call twice(int), 1
 352:      t7 = sum int+ t6
 353:      sum = t7
 354: L30: t8 = i int+ 1
 355:      i = t8
 356:      goto L26
 357: L31: t9 = sum int+ before
 358:      after = t9
 359:      return after

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
 360:   param 5
 361:   t1 = call depth(int), 1
 362:   param 3
 363:   t2 = call many(int), 1
 364:   param "%d %d\n"
 365:   param t1
 366:   param t2
 367:   call printf, 3
 368:   param 1
 369:   param 2
 370:   param 3
 371:   t3 = call arguments(int, int, int), 3
 372:   param 4
 373:   param 0
 374:   param 9
 375:   t4 = call arguments(int, int, int), 3
 376:   param "%d %d\n"
 377:   param t3
 378:   param t4
 379:   call printf, 3
 380:   param "register allocation"
 381:   t5 = call characters(const char *), 1
 382:   param "zzzzzzzzzzzzzzzzzzzz"
 383:   t6 = call characters(const char *), 1
 384:   param "%d %d\n"
 385:   param t5
 386:   param t6
 387:   call printf, 3
 388:   param 0
 389:   t7 = call numbers(int), 1
 390:   param 3
 391:   t8 = call numbers(int), 1
 392:   param 40
 393:   t9 = call numbers(int), 1
 394:   param "%.4f %.4f %.4f\n"
 395:   param t7
 396:   param t8
 397:   param t9
 398:   call printf, 4
 399:   param 0
 400:   t10 = call jumps(int), 1
 401:   param 5
 402:   t11 = call jumps(int), 1
 403:   param 9
 404:   t12 = call mixed(int), 1
 405:   param "%d %d %d\n"
 406:   param t10
 407:   param t11
 408:   param t12
 409:   call printf, 4
 410:   param 3
 411:   t13 = call jumps(int), 1
 412:   t14 = t13 int% 100
 413:   return t14


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
