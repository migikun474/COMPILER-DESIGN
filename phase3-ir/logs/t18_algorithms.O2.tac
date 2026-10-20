=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t18_algorithms.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 401 -> 326 instruction(s) for 'test/t18_algorithms.c'.

optimization summary (-O2)
    instructions                401 -> 326   (18% fewer)
    constants folded            4
    algebraic simplifications   24
    common subexpressions       13
    copies / constants forwarded 20
    temporaries merged away     27
    dead instructions removed   17
    jumps removed or redirected 28
    unreachable instructions    1
    propagated across blocks    4
    dead assignments removed    3

globals (name, type, width, initial value)
    moves          int                        4  0

function bubble(int *, int)        link name: _Z6bubblePii
  symbol table (name, kind, type, width, offset)
    a              param  int *                      4      0
    n              param  int                        4      4
    i              local  int                        4      8
    j              local  int                        4     12
    t              local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int *                      4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    t8             temp   int                        4     48
    t9             temp   int *                      4     52
    t10            temp   int                        4     56
    t11            temp   int                        4     60
    t12            temp   int *                      4     64
    t13            temp   int                        4     68
    t14            temp   int                        4     72
    t15            temp   int *                      4     76
    t16            temp   int                        4     80
    t17            temp   int                        4     84
    t18            temp   int *                      4     88
    t19            temp   int                        4     92
    t20            temp   int                        4     96
    t21            temp   int                        4    100
    t22            temp   int *                      4    104
    t23            temp   int                        4    108
    t24            temp   int                        4    112
    total width 116
  code
 100:     i = 0
 101: L1: t1 = n int- 1
 102:     if i int>= t1 goto L5
 103:     j = 0
 104: L2: t2 = n int- 1
 105:     t3 = t2 int- i
 106:     if j int>= t3 goto L4
 107:     t4 = j int<< 2
 108:     t5 = a ptr+ t4
 109:     t6 = *t5
 110:     t7 = j int+ 1
 111:     t8 = t7 int<< 2
 112:     t9 = a ptr+ t8
 113:     t10 = *t9
 114:     if t6 int<= t10 goto L3
 115:     t11 = j int<< 2
 116:     t12 = a ptr+ t11
 117:     t13 = *t12
 118:     t16 = j int+ 1
 119:     t17 = t16 int<< 2
 120:     t18 = a ptr+ t17
 121:     t19 = *t18
 122:     *t12 = t19
 123:     *t18 = t13
 124: L3: j = j int+ 1
 125:     goto L2
 126: L4: i = i int+ 1
 127:     goto L1
 128: L5: return

function quick(int *, int, int)        link name: _Z5quickPiii
  symbol table (name, kind, type, width, offset)
    a              param  int *                      4      0
    lo             param  int                        4      4
    hi             param  int                        4      8
    pivot          local  int                        4     12
    i              local  int                        4     16
    j              local  int                        4     20
    t              local  int                        4     24
    t1             temp   int                        4     28
    t2             temp   int                        4     32
    t3             temp   int                        4     36
    t4             temp   int *                      4     40
    t5             temp   int                        4     44
    t6             temp   int                        4     48
    t7             temp   int *                      4     52
    t8             temp   int                        4     56
    t9             temp   int                        4     60
    t10            temp   int                        4     64
    t11            temp   int *                      4     68
    t12            temp   int                        4     72
    t13            temp   int                        4     76
    t14            temp   int                        4     80
    t15            temp   int *                      4     84
    t16            temp   int                        4     88
    t17            temp   int                        4     92
    t18            temp   int *                      4     96
    t19            temp   int                        4    100
    t20            temp   int *                      4    104
    t21            temp   int                        4    108
    t22            temp   int                        4    112
    t23            temp   int *                      4    116
    t24            temp   int                        4    120
    t25            temp   int                        4    124
    total width 128
  code
 129:      if lo int< hi goto L6
 130:      return
 131: L6:  t1 = lo int+ hi
 132:      t2 = t1 int/ 2
 133:      t3 = t2 int<< 2
 134:      t4 = a ptr+ t3
 135:      pivot = *t4
 136:      i = lo
 137:      j = hi
 138: L7:  if i int> j goto L11
 139: L8:  t6 = i int<< 2
 140:      t7 = a ptr+ t6
 141:      t8 = *t7
 142:      if t8 int>= pivot goto L9
 143:      i = i int+ 1
 144:      goto L8
 145: L9:  t10 = j int<< 2
 146:      t11 = a ptr+ t10
 147:      t12 = *t11
 148:      if t12 int<= pivot goto L10
 149:      j = j int- 1
 150:      goto L9
 151: L10: if i int> j goto L7
 152:      t14 = i int<< 2
 153:      t15 = a ptr+ t14
 154:      t16 = *t15
 155:      t19 = j int<< 2
 156:      t20 = a ptr+ t19
 157:      t21 = *t20
 158:      *t15 = t21
 159:      *t20 = t16
 160:      i = i int+ 1
 161:      j = j int- 1
 162:      goto L7
 163: L11: param a
 164:      param lo
 165:      param j
 166:      call quick(int *, int, int), 3
 167:      param a
 168:      param i
 169:      param hi
 170:      call quick(int *, int, int), 3
 171:      return

function search(int *, int, int)        link name: _Z6searchPiii
  symbol table (name, kind, type, width, offset)
    a              param  int *                      4      0
    n              param  int                        4      4
    key            param  int                        4      8
    lo             local  int                        4     12
    hi             local  int                        4     16
    mid            local  int                        4     20
    t1             temp   int                        4     24
    t2             temp   int                        4     28
    t3             temp   int                        4     32
    t4             temp   int                        4     36
    t5             temp   int                        4     40
    t6             temp   int *                      4     44
    t7             temp   int                        4     48
    t8             temp   int                        4     52
    t9             temp   int *                      4     56
    t10            temp   int                        4     60
    t11            temp   int                        4     64
    t12            temp   int                        4     68
    t13            temp   int                        4     72
    total width 76
  code
 172:      lo = 0
 173:      hi = n int- 1
 174: L12: if lo int> hi goto L15
 175:      t2 = hi int- lo
 176:      t3 = t2 int/ 2
 177:      t4 = lo int+ t3
 178:      t5 = t4 int<< 2
 179:      t6 = a ptr+ t5
 180:      t7 = *t6
 181:      if t7 int!= key goto L13
 182:      return t4
 183: L13: t8 = t4 int<< 2
 184:      t9 = a ptr+ t8
 185:      t10 = *t9
 186:      if t10 int>= key goto L14
 187:      lo = t4 int+ 1
 188:      goto L12
 189: L14: hi = t4 int- 1
 190:      goto L12
 191: L15: return -1

function hanoi(int, int, int, int)        link name: _Z5hanoiiiii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    from           param  int                        4      4
    to             param  int                        4      8
    via            param  int                        4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    total width 28
  code
 192:      if n int!= 0 goto L16
 193:      return
 194: L16: t1 = n int- 1
 195:      param t1
 196:      param from
 197:      param via
 198:      param to
 199:      call hanoi(int, int, int, int), 4
 200:      moves = moves int+ 1
 201:      param t1
 202:      param via
 203:      param to
 204:      param from
 205:      call hanoi(int, int, int, int), 4
 206:      return

function ackermann(int, int)        link name: _Z9ackermannii
  symbol table (name, kind, type, width, offset)
    m              param  int                        4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    t6             temp   int                        4     28
    t7             temp   int                        4     32
    total width 36
  code
 207:      if m int!= 0 goto L17
 208:      t1 = n int+ 1
 209:      return t1
 210: L17: if n int!= 0 goto L18
 211:      t2 = m int- 1
 212:      param t2
 213:      param 1
 214:      t3 = call ackermann(int, int), 2
 215:      return t3
 216: L18: t4 = m int- 1
 217:      t5 = n int- 1
 218:      param m
 219:      param t5
 220:      t6 = call ackermann(int, int), 2
 221:      param t4
 222:      param t6
 223:      t7 = call ackermann(int, int), 2
 224:      return t7

function multiply(int (*)[3], int (*)[2], int (*)[2])        link name: _Z8multiplyPA3_iPA2_iS2_
  symbol table (name, kind, type, width, offset)
    a              param  int (*)[3]                 4      0
    b              param  int (*)[2]                 4      4
    c              param  int (*)[2]                 4      8
    i              local  int                        4     12
    j              local  int                        4     16
    k              local  int                        4     20
    t1             temp   int                        4     24
    t2             temp   int (*)[2]                 4     28
    t3             temp   int                        4     32
    t4             temp   int (*)[2]                 4     36
    t5             temp   int                        4     40
    t6             temp   int (*)[2]                 4     44
    t7             temp   int                        4     48
    t8             temp   int (*)[2]                 4     52
    t9             temp   int                        4     56
    t10            temp   int                        4     60
    t11            temp   int (*)[3]                 4     64
    t12            temp   int                        4     68
    t13            temp   int (*)[3]                 4     72
    t14            temp   int                        4     76
    t15            temp   int                        4     80
    t16            temp   int (*)[2]                 4     84
    t17            temp   int                        4     88
    t18            temp   int (*)[2]                 4     92
    t19            temp   int                        4     96
    t20            temp   int                        4    100
    t21            temp   int                        4    104
    t22            temp   int                        4    108
    t23            temp   int                        4    112
    t24            temp   int                        4    116
    total width 120
  code
 225:      i = 0
 226: L19: if i int>= 2 goto L24
 227:      j = 0
 228: L20: if j int>= 2 goto L23
 229:      t1 = i int<< 3
 230:      t2 = c ptr+ t1
 231:      t3 = j int<< 2                      (w = 4)
 232:      t4 = t2 ptr+ t3
 233:      *t4 = 0
 234:      k = 0
 235: L21: if k int>= 3 goto L22
 236:      t5 = i int<< 3
 237:      t6 = c ptr+ t5
 238:      t7 = j int<< 2                      (w = 4)
 239:      t8 = t6 ptr+ t7
 240:      t9 = *t8
 241:      t10 = i int* 12
 242:      t11 = a ptr+ t10
 243:      t12 = k int<< 2                     (w = 4)
 244:      t13 = t11 ptr+ t12
 245:      t14 = *t13
 246:      t15 = k int<< 3
 247:      t16 = b ptr+ t15
 248:      t18 = t16 ptr+ t7
 249:      t19 = *t18
 250:      t20 = t14 int* t19
 251:      t21 = t9 int+ t20
 252:      *t8 = t21
 253:      k = k int+ 1
 254:      goto L21
 255: L22: j = j int+ 1
 256:      goto L20
 257: L23: i = i int+ 1
 258:      goto L19
 259: L24: return

function primes(int)        link name: _Z6primesi
  symbol table (name, kind, type, width, offset)
    limit          param  int                        4      0
    composite      local  char[101]                101      4
    count          local  int                        4    108
    i.34           local  int                        4    112
    i.35           local  int                        4    116
    j              local  int                        4    120
    t1             temp   int                        4    124
    t2             temp   char                       1    128
    t3             temp   int                        4    132
    t4             temp   int                        4    136
    t5             temp   int                        4    140
    t6             temp   int                        4    144
    total width 148
  code
 260:      count = 0
 261:      i.34 = 0
 262: L25: if i.34 int> limit goto L26
 263:      composite[i.34] = 0
 264:      i.34 = i.34 int+ 1
 265:      goto L25
 266: L26: i.35 = 2
 267: L27: if i.35 int> limit goto L30
 268:      t2 = composite[i.35]
 269:      if t2 char!= 0 goto L29
 270:      count = count int+ 1
 271:      j = i.35 int* i.35
 272: L28: if j int> limit goto L29
 273:      composite[j] = 1
 274:      j = j int+ i.35
 275:      goto L28
 276: L29: i.35 = i.35 int+ 1
 277:      goto L27
 278: L30: return count

function power(int, int)        link name: _Z5powerii
  symbol table (name, kind, type, width, offset)
    base           param  int                        4      0
    exp            param  int                        4      4
    result         local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    total width 28
  code
 279:      result = 1
 280: L31: if exp int<= 0 goto L33
 281:      t1 = exp int& 1
 282:      if t1 int== 0 goto L32
 283:      result = result int* base
 284: L32: base = base int* base
 285:      exp = exp int>> 1
 286:      goto L31
 287: L33: return result

function collatz(int)        link name: _Z7collatzi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    steps          local  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    t6             temp   int                        4     28
    total width 32
  code
 288:      steps = 0
 289: L34: if n int== 1 goto L37
 290:      t2 = n int% 2
 291:      if t2 int== 0 goto L35
 292:      t3 = n int* 3
 293:      t1 = t3 int+ 1
 294:      goto L36
 295: L35: t1 = n int/ 2
 296: L36: n = t1
 297:      steps = steps int+ 1
 298:      goto L34
 299: L37: return steps

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    a              local  int[8]                    32      0
    b              local  int[8]                    32     32
    i.44           local  int                        4     64
    i.45           local  int                        4     68
    x              local  int[2][3]                 24     72
    y              local  int[3][2]                 24     96
    z              local  int[2][2]                 16    120
    t1             temp   int                        4    136
    t2             temp   int                        4    140
    t3             temp   int (*)[8]                 4    144
    t4             temp   int (*)[8]                 4    148
    t5             temp   int                        4    152
    t6             temp   int                        4    156
    t7             temp   int                        4    160
    t8             temp   int                        4    164
    t9             temp   int                        4    168
    t10            temp   int                        4    172
    t11            temp   int (*)[8]                 4    176
    t12            temp   int                        4    180
    t13            temp   int (*)[8]                 4    184
    t14            temp   int                        4    188
    t15            temp   int (*)[8]                 4    192
    t16            temp   int                        4    196
    t17            temp   int                        4    200
    t18            temp   int                        4    204
    t19            temp   int                        4    208
    t20            temp   int (*)[2][3]              4    212
    t21            temp   int (*)[3][2]              4    216
    t22            temp   int (*)[2][2]              4    220
    t23            temp   int                        4    224
    t24            temp   int                        4    228
    t25            temp   int                        4    232
    t26            temp   int                        4    236
    t27            temp   int                        4    240
    t28            temp   int                        4    244
    t29            temp   int                        4    248
    t30            temp   int (*)[8]                 4    252
    t31            temp   int                        4    256
    total width 260
  code
 300:      a[0] = 42
 301:      a[4] = 7
 302:      a[8] = 19
 303:      a[12] = 3
 304:      a[16] = 25
 305:      a[20] = 7
 306:      a[24] = 88
 307:      a[28] = 1
 308:      b[0] = 5
 309:      b[4] = -2
 310:      b[8] = 9
 311:      b[12] = 0
 312:      b[16] = 9
 313:      b[20] = 14
 314:      b[24] = -7
 315:      b[28] = 3
 316:      t3 = &a
 317:      param t3
 318:      param 8
 319:      call bubble(int *, int), 2
 320:      t4 = &b
 321:      param t4
 322:      param 0
 323:      param 7
 324:      call quick(int *, int, int), 3
 325:      i.44 = 0
 326: L38: if i.44 int>= 8 goto L39
 327:      t5 = i.44 int<< 2                   (w = 4)
 328:      t6 = a[t5]
 329:      param "%d "
 330:      param t6
 331:      call printf, 2
 332:      i.44 = i.44 int+ 1
 333:      goto L38
 334: L39: param "\n"
 335:      call printf, 1
 336:      i.45 = 0
 337: L40: if i.45 int>= 8 goto L41
 338:      t8 = i.45 int<< 2                   (w = 4)
 339:      t9 = b[t8]
 340:      param "%d "
 341:      param t9
 342:      call printf, 2
 343:      i.45 = i.45 int+ 1
 344:      goto L40
 345: L41: t11 = &a
 346:      param t11
 347:      param 8
 348:      param 25
 349:      t12 = call search(int *, int, int), 3
 350:      param t11
 351:      param 8
 352:      param 26
 353:      t14 = call search(int *, int, int), 3
 354:      t15 = &b
 355:      param t15
 356:      param 8
 357:      param -7
 358:      t17 = call search(int *, int, int), 3
 359:      param "\n%d %d %d\n"
 360:      param t12
 361:      param t14
 362:      param t17
 363:      call printf, 4
 364:      param 6
 365:      param 1
 366:      param 3
 367:      param 2
 368:      call hanoi(int, int, int, int), 4
 369:      param 2
 370:      param 3
 371:      t18 = call ackermann(int, int), 2
 372:      param 27
 373:      t19 = call collatz(int), 1
 374:      param "%d %d %d\n"
 375:      param moves
 376:      param t18
 377:      param t19
 378:      call printf, 4
 379:      x[0] = 1
 380:      x[4] = 2
 381:      x[8] = 3
 382:      x[12] = 4
 383:      x[16] = 5
 384:      x[20] = 6
 385:      y[0] = 7
 386:      y[4] = 8
 387:      y[8] = 9
 388:      y[12] = 10
 389:      y[16] = 11
 390:      y[20] = 12
 391:      t20 = &x
 392:      t21 = &y
 393:      t22 = &z
 394:      param t20
 395:      param t21
 396:      param t22
 397:      call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
 398:      t23 = z[0]
 399:      t24 = z[4]
 400:      t25 = z[8]
 401:      t26 = z[12]
 402:      param "%d %d %d %d\n"
 403:      param t23
 404:      param t24
 405:      param t25
 406:      param t26
 407:      call printf, 5
 408:      param 100
 409:      t27 = call primes(int), 1
 410:      param 3
 411:      param 13
 412:      t28 = call power(int, int), 2
 413:      param 2
 414:      param 10
 415:      t29 = call power(int, int), 2
 416:      param "%d %d %d\n"
 417:      param t27
 418:      param t28
 419:      param t29
 420:      call printf, 4
 421:      param t11
 422:      param 8
 423:      param 88
 424:      t31 = call search(int *, int, int), 3
 425:      return t31


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
bubble             function       void (int *, int)          -        global                         4     -     1     _Z6bubblePii         _Z6bubblePii             defined
a                  parameter      int *                      param    global > bubble()              4     4     6     a.1                  -                        
n                  parameter      int                        param    global > bubble()              4     4     2     n.2                  -                        
i                  variable       int                        local    global > bubble() > for        5     4     3     i.3                  -                        
j                  variable       int                        local    global > bubble() > for > for body > for 6     4     8     j.4                  -                        
t                  variable       int                        local    global > bubble() > for > for body > for > for body > if 7     4     1     t.5                  -                        
quick              function       void (int *, int, int)     -        global                         10    -     3     _Z5quickPiii         _Z5quickPiii             defined
a                  parameter      int *                      param    global > quick()               10    4     9     a.6                  -                        
lo                 parameter      int                        param    global > quick()               10    4     4     lo.7                 -                        
hi                 parameter      int                        param    global > quick()               10    4     4     hi.8                 -                        
pivot              variable       int                        local    global > quick()               12    4     2     pivot.9              -                        
i                  variable       int                        local    global > quick()               12    4     8     i.10                 -                        
j                  variable       int                        local    global > quick()               12    4     8     j.11                 -                        
t                  variable       int                        local    global > quick() > while > if  16    4     1     t.12                 -                        
search             function       int (int *, int, int)      -        global                         22    -     4     _Z6searchPiii        _Z6searchPiii            defined
a                  parameter      int *                      param    global > search()              22    4     2     a.13                 -                        
n                  parameter      int                        param    global > search()              22    4     1     n.14                 -                        
key                parameter      int                        param    global > search()              22    4     2     key.15               -                        
lo                 variable       int                        local    global > search()              23    4     4     lo.16                -                        
hi                 variable       int                        local    global > search()              23    4     3     hi.17                -                        
mid                variable       int                        local    global > search() > while      25    4     5     mid.18               -                        
moves              variable       int                        global   global                         32    4     2     moves                -                        
hanoi              function       void (int, int, int, int)  -        global                         33    -     3     _Z5hanoiiiii         _Z5hanoiiiii             defined
n                  parameter      int                        param    global > hanoi()               33    4     3     n.19                 -                        
from               parameter      int                        param    global > hanoi()               33    4     2     from.20              -                        
to                 parameter      int                        param    global > hanoi()               33    4     2     to.21                -                        
via                parameter      int                        param    global > hanoi()               33    4     2     via.22               -                        
ackermann          function       int (int, int)             -        global                         40    -     4     _Z9ackermannii       _Z9ackermannii           defined
m                  parameter      int                        param    global > ackermann()           40    4     4     m.23                 -                        
n                  parameter      int                        param    global > ackermann()           40    4     3     n.24                 -                        
multiply           function       void (int (*)[3], int (*)[2], int (*)[2]) -        global                         46    -     1     _Z8multiplyPA3_iPA2_iS2_ _Z8multiplyPA3_iPA2_iS2_ defined
a                  parameter      int (*)[3]                 param    global > multiply()            46    4     1     a.25                 -                        
b                  parameter      int (*)[2]                 param    global > multiply()            46    4     1     b.26                 -                        
c                  parameter      int (*)[2]                 param    global > multiply()            46    4     2     c.27                 -                        
i                  variable       int                        local    global > multiply() > for      47    4     5     i.28                 -                        
j                  variable       int                        local    global > multiply() > for > for body > for 48    4     5     j.29                 -                        
k                  variable       int                        local    global > multiply() > for > for body > for > for body > for 50    4     4     k.30                 -                        
primes             function       int (int)                  -        global                         54    -     1     _Z6primesi           _Z6primesi               defined
limit              parameter      int                        param    global > primes()              54    4     3     limit.31             -                        
composite          variable       char[101]                  local    global > primes()              55    101   3     composite.32         -                        
count              variable       int                        local    global > primes()              56    4     2     count.33             -                        
i                  variable       int                        local    global > primes() > for        57    4     3     i.34                 -                        
i                  variable       int                        local    global > primes() > for        58    4     6     i.35                 -                        
j                  variable       int                        local    global > primes() > for > for body > for 61    4     3     j.36                 -                        
power              function       int (int, int)             -        global                         66    -     2     _Z5powerii           _Z5powerii               defined
base               parameter      int                        param    global > power()               66    4     3     base.37              -                        
exp                parameter      int                        param    global > power()               66    4     3     exp.38               -                        
result             variable       int                        local    global > power()               67    4     2     result.39            -                        
collatz            function       int (int)                  -        global                         76    -     1     _Z7collatzi          _Z7collatzi              defined
n                  parameter      int                        param    global > collatz()             76    4     5     n.40                 -                        
steps              variable       int                        local    global > collatz()             76    4     2     steps.41             -                        
main               function       int (void)                 -        global                         78    -     0     main                 main                     defined
a                  variable       int[8]                     local    global > main()                79    32    5     a.42                 -                        
b                  variable       int[8]                     local    global > main()                79    32    3     b.43                 -                        
i                  variable       int                        local    global > main() > for          82    4     3     i.44                 -                        
i                  variable       int                        local    global > main() > for          84    4     3     i.45                 -                        
x                  variable       int[2][3]                  local    global > main()                88    24    1     x.46                 -                        
y                  variable       int[3][2]                  local    global > main()                88    24    1     y.47                 -                        
z                  variable       int[2][2]                  local    global > main()                88    16    5     z.48                 -                        

=== Record Layouts ===
(no records)
