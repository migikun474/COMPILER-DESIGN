=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t28_o3.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 313 -> 282 instruction(s) for 'test/t28_o3.c'.

optimization summary (-O3)
    instructions                313 -> 282   (9% fewer)
    constants folded            29
    algebraic simplifications   7
    common subexpressions       10
    copies / constants forwarded 105
    temporaries merged away     19
    dead instructions removed   72
    jumps removed or redirected 27
    unreachable instructions    21
    propagated across blocks    16
    dead assignments removed    27
    calls inlined               21
    tail calls turned to jumps  3
    common across blocks        3
    moved out of loops          5

globals (name, type, width, initial value)
    calls          int                        4  0

function square(int)        link name: _Z6squarei
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 100:   t1 = v int* v
 101:   return t1

function clamp(int, int, int)        link name: _Z5clampiii
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    lo             param  int                        4      4
    hi             param  int                        4      8
    total width 12
  code
 102:     if v int>= lo goto L1
 103:     return lo
 104: L1: if v int<= hi goto L2
 105:     return hi
 106: L2: return v

function counted(int)        link name: _Z7countedi
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 107:   t1 = calls int+ 1
 108:   calls = t1
 109:   t2 = v int+ t1
 110:   return t2

function bump(int &, int)        link name: _Z4bumpRii
  symbol table (name, kind, type, width, offset)
    r              param  int &                      4      0
    by             param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 111:   t1 = *r
 112:   t2 = t1 int+ by
 113:   *r = t2
 114:   return

function total(struct Pair)        link name: _Z5total4Pair
  symbol table (name, kind, type, width, offset)
    p              param  struct Pair                8      0
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    total width 28
  code
 115:   t1 = p[0]
 116:   t2 = t1 int+ 1
 117:   p[0] = t2
 118:   t4 = p[4]
 119:   t5 = t2 int+ t4
 120:   return t5

function fact(int)        link name: _Z4facti
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 121:     if n int> 1 goto L3
 122:     t1 = 1
 123:     goto L4
 124: L3: t2 = n int- 1
 125:     param t2
 126:     t3 = call fact(int), 1
 127:     t1 = n int* t3
 128: L4: return t1

function gcd(int, int)        link name: _Z3gcdii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    total width 24
  code
 129: L5: if b int!= 0 goto L6
 130:     return a
 131: L6: t1 = a int% b
 132:     a = b
 133:     b = t1
 134:     goto L5

function sumTo(int, int)        link name: _Z5sumToii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    acc            param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    total width 28
  code
 135: L7: if n int!= 0 goto L8
 136:     return acc
 137: L8: t1 = n int- 1
 138:     t2 = acc int+ n
 139:     n = t1
 140:     acc = t2
 141:     goto L7

function countDown(int)        link name: _Z9countDowni
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    total width 16
  code
 142: L9:  if n int> 0 goto L10
 143:      return 0
 144: L10: n = n int- 2
 145:      goto L9

function invariant(int, int)        link name: _Z9invariantii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    k              param  int                        4      4
    s              local  int                        4      8
    i              local  int                        4     12
    scale          local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    total width 48
  code
 146:      s = 0
 147:      i = 0
 148:      t1 = k int* 3
 149:      t2 = t1 int+ 1
 150: L11: if i int>= n goto L13
 151:      t3 = i int* t2
 152:      s = s int+ t3
 153:      if i int== 2 goto L12
 154:      s = s int+ t1
 155: L12: i = i int+ 1
 156:      goto L11
 157: L13: return s

function notInvariant(int)        link name: _Z12notInvarianti
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    s              local  int                        4      4
    k              local  int                        4      8
    i              local  int                        4     12
    v              local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    total width 36
  code
 158:      s = 0
 159:      k = 1
 160:      i = 0
 161: L14: if i int>= n goto L15
 162:      t1 = k int* 3
 163:      s = s int+ t1
 164:      k = k int+ i
 165:      i = i int+ 1
 166:      goto L14
 167: L15: return s

function zeroTrips(int, int)        link name: _Z9zeroTripsii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    d              param  int                        4      4
    s              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    total width 24
  code
 168:      s = 7
 169: L16: if n int<= 0 goto L17
 170:      t1 = 100 int/ d
 171:      s = s int+ t1
 172:      n = n int- 1
 173:      goto L16
 174: L17: return s

function nested(int, int)        link name: _Z6nestedii
  symbol table (name, kind, type, width, offset)
    rows           param  int                        4      0
    cols           param  int                        4      4
    grid           local  int[4][5]                 80      8
    s              local  int                        4     88
    r.32           local  int                        4     92
    c.33           local  int                        4     96
    r.34           local  int                        4    100
    c.35           local  int                        4    104
    t1             temp   int                        4    108
    t2             temp   int                        4    112
    t3             temp   int                        4    116
    t4             temp   int                        4    120
    t5             temp   int                        4    124
    t6             temp   int                        4    128
    t7             temp   int                        4    132
    t8             temp   int                        4    136
    t9             temp   int                        4    140
    t10            temp   int                        4    144
    t11            temp   int                        4    148
    t12            temp   int                        4    152
    t13            temp   int                        4    156
    t14            temp   int                        4    160
    total width 164
  code
 175:      s = 0
 176:      r.32 = 0
 177: L18: if r.32 int>= rows goto L21
 178:      c.33 = 0
 179:      t1 = r.32 int* 5                    (n2 = 5)
 180:      t4 = r.32 int* cols
 181: L19: if c.33 int>= cols goto L20
 182:      t2 = t1 int+ c.33
 183:      t3 = t2 int<< 2                     (w = 4)
 184:      t5 = t4 int+ c.33
 185:      grid[t3] = t5
 186:      c.33 = c.33 int+ 1
 187:      goto L19
 188: L20: r.32 = r.32 int+ 1
 189:      goto L18
 190: L21: r.34 = 0
 191: L22: if r.34 int>= rows goto L25
 192:      c.35 = 0
 193:      t8 = r.34 int* 5                    (n2 = 5)
 194: L23: if c.35 int>= cols goto L24
 195:      t9 = t8 int+ c.35
 196:      t10 = t9 int<< 2                    (w = 4)
 197:      t11 = grid[t10]
 198:      s = s int+ t11
 199:      c.35 = c.35 int+ 1
 200:      goto L23
 201: L24: r.34 = r.34 int+ 1
 202:      goto L22
 203: L25: return s

function shared(int, int, int)        link name: _Z6sharediii
  symbol table (name, kind, type, width, offset)
    x              param  int                        4      0
    y              param  int                        4      4
    flag           param  int                        4      8
    a              local  int                        4     12
    b              local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    t8             temp   int                        4     48
    t9             temp   int                        4     52
    t10            temp   int                        4     56
    t11            temp   int                        4     60
    total width 64
  code
 204:      t1 = x int* y
 205:      a = t1 int+ 2
 206:      if flag int== 0 goto L26
 207:      b = a
 208:      goto L27
 209: L26: t5 = x int+ 1
 210:      x = t5
 211:      t6 = t5 int* y
 212:      b = t6 int+ 2
 213: L27: t8 = a int* 1000
 214:      t9 = t8 int+ b
 215:      t10 = x int* y
 216:      t11 = t9 int+ t10
 217:      return t11

function memory(int)        link name: _Z6memoryi
  symbol table (name, kind, type, width, offset)
    i              param  int                        4      0
    arr            local  int[4]                    16      4
    p              local  int *                      4     20
    q              local  int *                      4     24
    a              local  int                        4     28
    b              local  int                        4     32
    c              local  int                        4     36
    t1             temp   int *                      4     40
    t2             temp   int *                      4     44
    t3             temp   int (*)[4]                 4     48
    t4             temp   int                        4     52
    t5             temp   int                        4     56
    t6             temp   int                        4     60
    t7             temp   int                        4     64
    t8             temp   int                        4     68
    t9             temp   int                        4     72
    t10            temp   int *                      4     76
    t11            temp   int                        4     80
    t12            temp   int                        4     84
    t13            temp   int                        4     88
    t14            temp   int                        4     92
    t15            temp   int                        4     96
    t16            temp   int                        4    100
    total width 104
  code
 218:   arr[0] = 1
 219:   arr[4] = 2
 220:   arr[8] = 3
 221:   arr[12] = 4
 222:   t1 = &arr
 223:   t2 = t1 ptr+ 4
 224:   t4 = i int<< 2                      (w = 4)
 225:   arr[t4] = 10
 226:   *t2 = 20
 227:   t8 = arr[t4]
 228:   t10 = t1 ptr+ t4
 229:   *t10 = 30
 230:   t12 = arr[t4]
 231:   t13 = *t2
 232:   t14 = t12 int+ t13
 233:   t15 = 10 int+ t8
 234:   t16 = t15 int+ t14
 235:   return t16

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    x              local  int                        4      0
    p              local  struct Pair                8      4
    t              local  int                        4     12
    c1             local  int                        4     16
    c2             local  int                        4     20
    c3             local  int                        4     24
    t1             temp   int *                      4     28
    t2             temp   int                        4     32
    t3             temp   int                        4     36
    t4             temp   int                        4     40
    t5             temp   int                        4     44
    t6             temp   int                        4     48
    t7             temp   int                        4     52
    t8             temp   int                        4     56
    t9             temp   int                        4     60
    t10            temp   int                        4     64
    t11            temp   int                        4     68
    t12            temp   int                        4     72
    t13            temp   int                        4     76
    t14            temp   int                        4     80
    t15            temp   int                        4     84
    t16            temp   int                        4     88
    t17            temp   int                        4     92
    t18            temp   int                        4     96
    t19            temp   int                        4    100
    t20            temp   int                        4    104
    t21            temp   int                        4    108
    t22            temp   int                        4    112
    t23            temp   int                        4    116
    t24            temp   int                        4    120
    t25            temp   int                        4    124
    t26            temp   int                        4    128
    t27            temp   int                        4    132
    t28            temp   int                        4    136
    t29            temp   int                        4    140
    t30            temp   int                        4    144
    t31            temp   int                        4    148
    t32            temp   int                        4    152
    t33            temp   int &                      4    156
    t34            temp   int                        4    160
    t35            temp   int                        4    164
    t36            temp   int                        4    168
    t37            temp   struct Pair                8    172
    t38            temp   int                        4    180
    t39            temp   int                        4    184
    t40            temp   int                        4    188
    t41            temp   int                        4    192
    t42            temp   struct Pair                8    196
    t43            temp   int                        4    204
    t44            temp   int                        4    208
    t45            temp   int                        4    212
    t46            temp   int                        4    216
    t47            temp   int                        4    220
    t48            temp   int                        4    224
    t49            temp   int                        4    228
    t50            temp   int                        4    232
    t51            temp   int                        4    236
    t52            temp   int                        4    240
    t53            temp   int                        4    244
    t54            temp   int                        4    248
    t55            temp   int                        4    252
    t56            temp   int                        4    256
    t57            temp   int                        4    260
    t58            temp   int                        4    264
    t59            temp   int                        4    268
    t60            temp   int                        4    272
    t61            temp   int                        4    276
    t62            temp   int                        4    280
    t63            temp   int                        4    284
    t64            temp   int                        4    288
    t65            temp   int                        4    292
    t66            temp   int                        4    296
    t67            temp   int                        4    300
    t68            temp   int                        4    304
    t69            temp   int                        4    308
    t70            temp   int                        4    312
    t71            temp   int                        4    316
    t72            temp   int                        4    320
    t73            temp   int                        4    324
    t74            temp   int                        4    328
    t75            temp   int                        4    332
    t76            temp   int                        4    336
    t77            temp   int                        4    340
    t78            temp   int                        4    344
    t79            temp   int                        4    348
    t80            temp   int                        4    352
    t81            temp   int                        4    356
    t82            temp   int                        4    360
    t83            temp   int                        4    364
    t84            temp   int                        4    368
    t85            temp   int                        4    372
    t86            temp   int                        4    376
    t87            temp   int                        4    380
    t88            temp   int                        4    384
    t89            temp   int                        4    388
    t90            temp   int                        4    392
    t91            temp   int                        4    396
    t92            temp   int                        4    400
    t93            temp   int                        4    404
    t94            temp   int                        4    408
    t95            temp   int                        4    412
    t96            temp   int                        4    416
    t97            temp   int                        4    420
    t98            temp   int                        4    424
    t99            temp   int                        4    428
    t100           temp   int                        4    432
    t101           temp   int                        4    436
    t102           temp   int                        4    440
    t103           temp   int                        4    444
    t104           temp   int                        4    448
    t105           temp   int                        4    452
    t106           temp   int                        4    456
    t107           temp   int                        4    460
    t108           temp   int                        4    464
    t109           temp   int                        4    468
    t110           temp   int                        4    472
    t111           temp   int                        4    476
    t112           temp   int                        4    480
    t113           temp   int                        4    484
    t114           temp   int                        4    488
    t115           temp   int                        4    492
    t116           temp   int                        4    496
    t117           temp   int                        4    500
    t118           temp   int                        4    504
    t119           temp   int                        4    508
    t120           temp   int                        4    512
    t121           temp   int                        4    516
    t122           temp   int                        4    520
    t123           temp   int                        4    524
    t124           temp   int                        4    528
    t125           temp   int                        4    532
    t126           temp   int                        4    536
    total width 540
  code
 236:      x = 5
 237:      t1 = &x
 238:      t35 = *t1
 239:      t36 = t35 int+ 9
 240:      *t1 = t36
 241:      p[0] = 1
 242:      p[4] = 2
 243:      t37 = p
 244:      t38 = t37[0]
 245:      t39 = t38 int+ 1
 246:      t37[0] = t39
 247:      t40 = t37[4]
 248:      t41 = t39 int+ t40
 249:      t42 = p
 250:      t43 = t42[0]
 251:      t44 = t43 int+ 1
 252:      t42[0] = t44
 253:      t45 = t42[4]
 254:      t46 = t44 int+ t45
 255:      t5 = t41 int+ t46
 256:      t6 = p[0]
 257:      param "%d %d %d %d %d\n"
 258:      param x
 259:      param t5
 260:      param t6
 261:      param 0
 262:      param 13
 263:      call printf, 6
 264:      t57 = calls int+ 1
 265:      calls = t57
 266:      t58 = 1 int+ t57
 267:      calls = t58
 268:      t61 = 1 int+ t58
 269:      calls = t61
 270:      t64 = 1 int+ t61
 271:      param 6
 272:      t15 = call fact(int), 1
 273:      param "%d %d %d %d %d\n"
 274:      param t58
 275:      param t61
 276:      param t64
 277:      param calls
 278:      param t15
 279:      call printf, 6
 280:      t65 = 1071
 281:      t66 = 462
 282: L28: if t66 int== 0 goto L29
 283:      t67 = t65 int% t66
 284:      t65 = t66
 285:      t66 = t67
 286:      goto L28
 287: L29: t68 = 17
 288:      t69 = 5
 289: L30: if t69 int== 0 goto L31
 290:      t70 = t68 int% t69
 291:      t68 = t69
 292:      t69 = t70
 293:      goto L30
 294: L31: t71 = 100
 295:      t72 = 0
 296: L32: if t71 int== 0 goto L33
 297:      t73 = t71 int- 1
 298:      t74 = t72 int+ t71
 299:      t71 = t73
 300:      t72 = t74
 301:      goto L32
 302: L33: t75 = 9
 303: L34: if t75 int<= 0 goto L35
 304:      t75 = t75 int- 2
 305:      goto L34
 306: L35: param "%d %d %d %d\n"
 307:      param t65
 308:      param t68
 309:      param t72
 310:      param 0
 311:      call printf, 5
 312:      t78 = 0
 313:      t79 = 0
 314: L36: if t79 int>= 5 goto L38
 315:      t82 = t79 int* 7
 316:      t78 = t78 int+ t82
 317:      if t79 int== 2 goto L37
 318:      t78 = t78 int+ 6
 319: L37: t79 = t79 int+ 1
 320:      goto L36
 321: L38: t85 = 0
 322:      t86 = 0
 323: L39: if t86 int>= 0 goto L41
 324:      t89 = t86 int* 28
 325:      t85 = t85 int+ t89
 326:      if t86 int== 2 goto L40
 327:      t85 = t85 int+ 27
 328: L40: t86 = t86 int+ 1
 329:      goto L39
 330: L41: t91 = 0
 331:      t92 = 1
 332:      t93 = 0
 333: L42: if t93 int>= 5 goto L43
 334:      t94 = t92 int* 3
 335:      t91 = t91 int+ t94
 336:      t92 = t92 int+ t93
 337:      t93 = t93 int+ 1
 338:      goto L42
 339: L43: t95 = 0
 340:      t97 = 7
 341: L44: if t95 int<= 0 goto L45
 342:      t98 = 100 int/ 0
 343:      t97 = t97 int+ t98
 344:      t95 = t95 int- 1
 345:      goto L44
 346: L45: param "%d %d %d %d\n"
 347:      param t78
 348:      param t85
 349:      param t91
 350:      param t97
 351:      call printf, 5
 352:      t99 = 3
 353:      t101 = 7
 354: L46: if t99 int<= 0 goto L47
 355:      t101 = t101 int+ 25
 356:      t99 = t99 int- 1
 357:      goto L46
 358: L47: param 4
 359:      param 5
 360:      t25 = call nested(int, int), 2
 361:      param 2
 362:      param 3
 363:      t26 = call nested(int, int), 2
 364:      param "%d %d %d\n"
 365:      param t101
 366:      param t25
 367:      param t26
 368:      call printf, 4
 369:      param "%d %d\n"
 370:      param 14026
 371:      param 14034
 372:      call printf, 3
 373:      param 1
 374:      t29 = call memory(int), 1
 375:      param 2
 376:      t30 = call memory(int), 1
 377:      param "%d %d\n"
 378:      param t29
 379:      param t30
 380:      call printf, 3
 381:      return calls


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
calls              variable       int                        global   global                         6     4     4     calls                -                        
square             function       int (int)                  -        global                         7     -     1     _Z6squarei           _Z6squarei               defined
v                  parameter      int                        param    global > square()              7     4     2     v.1                  -                        
clamp              function       int (int, int, int)        -        global                         8     -     3     _Z5clampiii          _Z5clampiii              defined
v                  parameter      int                        param    global > clamp()               8     4     3     v.2                  -                        
lo                 parameter      int                        param    global > clamp()               8     4     2     lo.3                 -                        
hi                 parameter      int                        param    global > clamp()               8     4     2     hi.4                 -                        
counted            function       int (int)                  -        global                         9     -     3     _Z7countedi          _Z7countedi              defined
v                  parameter      int                        param    global > counted()             9     4     1     v.5                  -                        
bump               function       void (int &, int)          -        global                         10    -     1     _Z4bumpRii           _Z4bumpRii               defined
r                  parameter      int &                      param    global > bump()                10    4     1     r.6                  -                        
by                 parameter      int                        param    global > bump()                10    4     1     by.7                 -                        
Pair               struct_tag     struct Pair                -        global                         11    -     0     Pair                 -                        size 8
Pair::a            field          int                        member   global > struct Pair           11    4     3     Pair::a              -                        public, offset 0
Pair::b            field          int                        member   global > struct Pair           11    4     1     Pair::b              -                        public, offset 4
total              function       int (struct Pair)          -        global                         12    -     2     _Z5total4Pair        _Z5total4Pair            defined
p                  parameter      struct Pair                param    global > total()               12    8     3     p.8                  -                        
fact               function       int (int)                  -        global                         13    -     2     _Z4facti             _Z4facti                 defined
n                  parameter      int                        param    global > fact()                13    4     3     n.9                  -                        
gcd                function       int (int, int)             -        global                         15    -     3     _Z3gcdii             _Z3gcdii                 defined
a                  parameter      int                        param    global > gcd()                 15    4     2     a.10                 -                        
b                  parameter      int                        param    global > gcd()                 15    4     3     b.11                 -                        
sumTo              function       int (int, int)             -        global                         16    -     2     _Z5sumToii           _Z5sumToii               defined
n                  parameter      int                        param    global > sumTo()               16    4     3     n.12                 -                        
acc                parameter      int                        param    global > sumTo()               16    4     2     acc.13               -                        
countDown          function       int (int)                  -        global                         17    -     2     _Z9countDowni        _Z9countDowni            defined
n                  parameter      int                        param    global > countDown()           17    4     2     n.14                 -                        
invariant          function       int (int, int)             -        global                         19    -     2     _Z9invariantii       _Z9invariantii           defined
n                  parameter      int                        param    global > invariant()           19    4     1     n.15                 -                        
k                  parameter      int                        param    global > invariant()           19    4     2     k.16                 -                        
s                  variable       int                        local    global > invariant()           20    4     3     s.17                 -                        
i                  variable       int                        local    global > invariant() > for     21    4     4     i.18                 -                        
scale              variable       int                        local    global > invariant() > for > for body 22    4     1     scale.19             -                        
notInvariant       function       int (int)                  -        global                         30    -     1     _Z12notInvarianti    _Z12notInvarianti        defined
n                  parameter      int                        param    global > notInvariant()        30    4     1     n.20                 -                        
s                  variable       int                        local    global > notInvariant()        31    4     2     s.21                 -                        
k                  variable       int                        local    global > notInvariant()        31    4     3     k.22                 -                        
i                  variable       int                        local    global > notInvariant() > for  32    4     3     i.23                 -                        
v                  variable       int                        local    global > notInvariant() > for > for body 33    4     1     v.24                 -                        
zeroTrips          function       int (int, int)             -        global                         40    -     2     _Z9zeroTripsii       _Z9zeroTripsii           defined
n                  parameter      int                        param    global > zeroTrips()           40    4     2     n.25                 -                        
d                  parameter      int                        param    global > zeroTrips()           40    4     1     d.26                 -                        
s                  variable       int                        local    global > zeroTrips()           41    4     2     s.27                 -                        
nested             function       int (int, int)             -        global                         46    -     2     _Z6nestedii          _Z6nestedii              defined
rows               parameter      int                        param    global > nested()              46    4     2     rows.28              -                        
cols               parameter      int                        param    global > nested()              46    4     3     cols.29              -                        
grid               variable       int[4][5]                  local    global > nested()              47    80    2     grid.30              -                        
s                  variable       int                        local    global > nested()              47    4     2     s.31                 -                        
r                  variable       int                        local    global > nested() > for        48    4     4     r.32                 -                        
c                  variable       int                        local    global > nested() > for > for body > for 49    4     4     c.33                 -                        
r                  variable       int                        local    global > nested() > for        50    4     3     r.34                 -                        
c                  variable       int                        local    global > nested() > for > for body > for 51    4     3     c.35                 -                        
shared             function       int (int, int, int)        -        global                         55    -     2     _Z6sharediii         _Z6sharediii             defined
x                  parameter      int                        param    global > shared()              55    4     6     x.36                 -                        
y                  parameter      int                        param    global > shared()              55    4     4     y.37                 -                        
flag               parameter      int                        param    global > shared()              55    4     1     flag.38              -                        
a                  variable       int                        local    global > shared()              56    4     1     a.39                 -                        
b                  variable       int                        local    global > shared()              56    4     3     b.40                 -                        
memory             function       int (int)                  -        global                         62    -     2     _Z6memoryi           _Z6memoryi               defined
i                  parameter      int                        param    global > memory()              62    4     5     i.41                 -                        
arr                variable       int[4]                     local    global > memory()              63    16    6     arr.42               -                        
p                  variable       int *                      local    global > memory()              64    4     2     p.43                 -                        
q                  variable       int *                      local    global > memory()              64    4     1     q.44                 -                        
a                  variable       int                        local    global > memory()              66    4     1     a.45                 -                        
b                  variable       int                        local    global > memory()              68    4     1     b.46                 -                        
c                  variable       int                        local    global > memory()              70    4     1     c.47                 -                        
main               function       int (void)                 -        global                         74    -     0     main                 main                     defined
x                  variable       int                        local    global > main()                75    4     2     x.48                 -                        
p                  variable       struct Pair                local    global > main()                77    8     3     p.49                 -                        
t                  variable       int                        local    global > main()                78    4     1     t.50                 -                        
c1                 variable       int                        local    global > main()                80    4     1     c1.51                -                        
c2                 variable       int                        local    global > main()                80    4     1     c2.52                -                        
c3                 variable       int                        local    global > main()                80    4     1     c3.53                -                        

=== Record Layouts ===
struct Pair: size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
