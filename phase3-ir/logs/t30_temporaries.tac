=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t30_temporaries.c
Optimization : no optimization

Three address code generated: 21 function(s), 522 instruction(s) for 'test/t30_temporaries.c'.

function Tag::Tag(int)        link name: _ZN3TagC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 100:   *this = n
 101:   t1 = *this
 102:   param "+%d "
 103:   param t1
 104:   call printf, 2
 105:   return

function Tag::~Tag()        link name: _ZN3TagD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 106:   t1 = *this
 107:   param "-%d "
 108:   param t1
 109:   call printf, 2
 110:   return

function Tag::value()        link name: _ZN3Tag5valueEv
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 111:   t1 = *this
 112:   t2 = t1 int* 10
 113:   return t2

function Tag::operator+(const class Tag &)        link name: _ZN3TagplERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    o              param  const class Tag &          4      4
    t1             temp   class Tag                  4      8
    t2             temp   class Tag *                4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    total width 28
  code
 114:   t2 = &t1
 115:   t3 = *this
 116:   t4 = *o
 117:   t5 = t3 int+ t4
 118:   param t2                            (this)
 119:   param t5
 120:   call Tag::Tag(int), 2
 121:   return t1

function Copy::Copy(int)        link name: _ZN4CopyC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 122:   *this = n
 123:   t1 = *this
 124:   param "+c%d "
 125:   param t1
 126:   call printf, 2
 127:   return

function Copy::Copy(const class Copy &)        link name: _ZN4CopyC1ERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    o              param  const class Copy &         4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 128:   t1 = *o
 129:   t2 = t1 int+ 100
 130:   *this = t2
 131:   t3 = *this
 132:   param "copy%d "
 133:   param t3
 134:   call printf, 2
 135:   return

function Copy::~Copy()        link name: _ZN4CopyD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    t1             temp   int                        4      4
    total width 8
  code
 136:   t1 = *this
 137:   param "-c%d "
 138:   param t1
 139:   call printf, 2
 140:   return

function make(int)        link name: _Z4makei
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   class Tag                  4      4
    t2             temp   class Tag *                4      8
    total width 12
  code
 141:   t2 = &t1
 142:   param t2                            (this)
 143:   param n
 144:   call Tag::Tag(int), 2
 145:   return t1

function named(int)        link name: _Z5namedi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t              local  class Tag                  4      4
    t1             temp   class Tag *                4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 146:   t1 = &t
 147:   param t1                            (this)
 148:   param n
 149:   call Tag::Tag(int), 2
 150:   t2 = t[0]
 151:   t3 = t2 int+ 1
 152:   t[0] = t3
 153:   return t

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    which          param  int                        4      0
    a              local  class Tag                  4      4
    b              local  class Tag                  4      8
    t1             temp   class Tag *                4     12
    t2             temp   class Tag *                4     16
    t3             temp   class Tag                  4     20
    t4             temp   class Tag *                4     24
    t5             temp   class Tag *                4     28
    t6             temp   class Tag                  4     32
    t7             temp   class Tag *                4     36
    t8             temp   class Tag *                4     40
    total width 44
  code
 154:     t1 = &a
 155:     param t1                            (this)
 156:     param 40
 157:     call Tag::Tag(int), 2
 158:     t2 = &b
 159:     param t2                            (this)
 160:     param 41
 161:     call Tag::Tag(int), 2
 162:     if which int!= 0 goto L1
 163:     goto L2
 164: L1: t3 = a
 165:     t4 = &b
 166:     param t4                            (this)
 167:     call Tag::~Tag(), 1
 168:     t5 = &a
 169:     param t5                            (this)
 170:     call Tag::~Tag(), 1
 171:     return t3
 172: L2: t6 = b
 173:     t7 = &b
 174:     param t7                            (this)
 175:     call Tag::~Tag(), 1
 176:     t8 = &a
 177:     param t8                            (this)
 178:     call Tag::~Tag(), 1
 179:     return t6

function byValue(class Tag)        link name: _Z7byValue3Tag
  symbol table (name, kind, type, width, offset)
    t              param  class Tag                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 180:   t1 = t[0]
 181:   return t1

function byRef(const class Tag &)        link name: _Z5byRefRK3Tag
  symbol table (name, kind, type, width, offset)
    t              param  const class Tag &          4      0
    t1             temp   int                        4      4
    total width 8
  code
 182:   t1 = *t
 183:   return t1

function copied(class Copy)        link name: _Z6copied4Copy
  symbol table (name, kind, type, width, offset)
    c              param  class Copy                 4      0
    t1             temp   int                        4      4
    total width 8
  code
 184:   t1 = c[0]
 185:   return t1

function makeCopy(int)        link name: _Z8makeCopyi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   class Copy                 4      4
    t2             temp   class Copy *               4      8
    total width 12
  code
 186:   t2 = &t1
 187:   param t2                            (this)
 188:   param n
 189:   call Copy::Copy(int), 2
 190:   return t1

function sameCopy(class Copy)        link name: _Z8sameCopy4Copy
  symbol table (name, kind, type, width, offset)
    c              param  class Copy                 4      0
    t1             temp   class Copy                 4      4
    t2             temp   class Copy *               4      8
    t3             temp   class Copy *               4     12
    total width 16
  code
 191:   t2 = &t1
 192:   t3 = &c
 193:   param t2                            (this)
 194:   param t3
 195:   call Copy::Copy(const class Copy &), 2
 196:   return t1

function Shape::sides()        link name: _ZN5Shape5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 197:   return 0

function Shape::kind()        link name: _ZN5Shape4kindEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 198:   return 1

function Square::sides()        link name: _ZN6Square5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 199:   return 4

function Square::kind()        link name: _ZN6Square4kindEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 200:   return 2

function mix(long long, long long, int)        link name: _Z3mixxxi
  symbol table (name, kind, type, width, offset)
    a              param  long long                  8      0
    b              param  long long                  8      8
    n              param  int                        4     16
    sum            local  long long                  8     24
    i              local  int                        4     32
    t1             temp   long long                  8     40
    t2             temp   long long                  8     48
    t3             temp   long long                  8     56
    t4             temp   long long                  8     64
    t5             temp   long long                  8     72
    t6             temp   long long                  8     80
    t7             temp   long long                  8     88
    t8             temp   long long                  8     96
    t9             temp   long long                  8    104
    t10            temp   int                        4    112
    t11            temp   long long                  8    120
    t12            temp   long long                  8    128
    total width 136
  code
 201:     sum = 0
 202:     i = 0
 203: L3: if i int< n goto L4
 204:     goto L5
 205: L4: t1 = inttollong i
 206:     t2 = a llong* t1
 207:     t3 = sum llong+ t2
 208:     t4 = b llong^ sum
 209:     t5 = t3 llong- t4
 210:     sum = t5
 211:     t6 = a llong+ 4294967296
 212:     a = t6
 213:     t7 = llong- b
 214:     t8 = sum llong& 65535
 215:     t9 = t7 llong+ t8
 216:     b = t9
 217:     t10 = i int+ 1
 218:     i = t10
 219:     goto L3
 220: L5: t11 = sum llong+ a
 221:     t12 = t11 llong- b
 222:     return t12

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    v              local  int                        4      0
    kept           local  class Tag                  4      4
    sum            local  class Tag                  4      8
    i              local  int                        4     12
    n              local  class Tag                  4     16
    r              local  const class Tag &          4     20
    c              local  class Copy                 4     24
    d              local  class Copy                 4     28
    e              local  class Copy                 4     32
    q              local  class Square               1     36
    p              local  class Shape *              4     40
    m              local  long long                  8     48
    inner          local  class Tag                  4     56
    t1             temp   class Tag                  4     60
    t2             temp   class Tag *                4     64
    t3             temp   class Tag *                4     68
    t4             temp   class Tag                  4     72
    t5             temp   class Tag *                4     76
    t6             temp   class Tag *                4     80
    t7             temp   class Tag                  4     84
    t8             temp   class Tag *                4     88
    t9             temp   class Tag *                4     92
    t10            temp   int                        4     96
    t11            temp   class Tag                  4    100
    t12            temp   class Tag *                4    104
    t13            temp   class Tag *                4    108
    t14            temp   int                        4    112
    t15            temp   int                        4    116
    t16            temp   class Tag *                4    120
    t17            temp   class Tag *                4    124
    t18            temp   class Tag                  4    128
    t19            temp   class Tag *                4    132
    t20            temp   class Tag *                4    136
    t21            temp   class Tag *                4    140
    t22            temp   class Tag                  4    144
    t23            temp   class Tag *                4    148
    t24            temp   class Tag *                4    152
    t25            temp   class Tag                  4    156
    t26            temp   class Tag *                4    160
    t27            temp   class Tag *                4    164
    t28            temp   class Tag *                4    168
    t29            temp   int                        4    172
    t30            temp   class Tag *                4    176
    t31            temp   class Tag *                4    180
    t32            temp   class Tag                  4    184
    t33            temp   class Tag *                4    188
    t34            temp   class Tag *                4    192
    t35            temp   class Tag *                4    196
    t36            temp   class Tag                  4    200
    t37            temp   class Tag *                4    204
    t38            temp   int                        4    208
    t39            temp   class Tag *                4    212
    t40            temp   class Tag *                4    216
    t41            temp   class Tag                  4    220
    t42            temp   class Tag *                4    224
    t43            temp   int                        4    228
    t44            temp   class Tag *                4    232
    t45            temp   class Tag                  4    236
    t46            temp   class Tag *                4    240
    t47            temp   int                        4    244
    t48            temp   class Tag *                4    248
    t49            temp   class Tag                  4    252
    t50            temp   class Tag *                4    256
    t51            temp   class Tag *                4    260
    t52            temp   int                        4    264
    t53            temp   class Tag *                4    268
    t54            temp   class Tag                  4    272
    t55            temp   class Tag *                4    276
    t56            temp   class Tag *                4    280
    t57            temp   int                        4    284
    t58            temp   class Tag *                4    288
    t59            temp   int                        4    292
    t60            temp   class Tag                  4    296
    t61            temp   class Tag *                4    300
    t62            temp   int                        4    304
    t63            temp   class Tag *                4    308
    t64            temp   class Tag                  4    312
    t65            temp   class Tag *                4    316
    t66            temp   class Tag *                4    320
    t67            temp   int                        4    324
    t68            temp   int                        4    328
    t69            temp   class Tag *                4    332
    t70            temp   int                        4    336
    t71            temp   class Tag                  4    340
    t72            temp   class Tag *                4    344
    t73            temp   int                        4    348
    t74            temp   class Tag *                4    352
    t75            temp   class Tag                  4    356
    t76            temp   class Tag *                4    360
    t77            temp   int                        4    364
    t78            temp   class Tag *                4    368
    t79            temp   class Tag                  4    372
    t80            temp   class Tag *                4    376
    t81            temp   class Tag *                4    380
    t82            temp   int                        4    384
    t83            temp   class Tag                  4    388
    t84            temp   class Tag *                4    392
    t85            temp   int                        4    396
    t86            temp   class Tag *                4    400
    t87            temp   class Tag                  4    404
    t88            temp   class Tag *                4    408
    t89            temp   int                        4    412
    t90            temp   int                        4    416
    t91            temp   class Tag *                4    420
    t92            temp   class Tag                  4    424
    t93            temp   class Tag *                4    428
    t94            temp   class Tag *                4    432
    t95            temp   int                        4    436
    t96            temp   class Tag                  4    440
    t97            temp   class Tag *                4    444
    t98            temp   class Tag *                4    448
    t99            temp   int                        4    452
    t100           temp   class Copy *               4    456
    t101           temp   class Copy                 4    460
    t102           temp   class Copy *               4    464
    t103           temp   class Copy *               4    468
    t104           temp   int                        4    472
    t105           temp   class Copy *               4    476
    t106           temp   class Copy                 4    480
    t107           temp   class Copy *               4    484
    t108           temp   int                        4    488
    t109           temp   class Copy *               4    492
    t110           temp   class Copy                 4    496
    t111           temp   class Copy *               4    500
    t112           temp   class Copy *               4    504
    t113           temp   int                        4    508
    t114           temp   class Copy                 4    512
    t115           temp   class Copy *               4    516
    t116           temp   class Copy *               4    520
    t117           temp   class Copy                 4    524
    t118           temp   class Copy *               4    528
    t119           temp   class Copy *               4    532
    t120           temp   class Copy *               4    536
    t121           temp   int                        4    540
    t122           temp   class Square *             4    544
    t123           temp   class Square *             4    548
    t124           temp   int                        4    552
    t125           temp   class Square *             4    556
    t126           temp   int                        4    560
    t127           temp   int                        4    564
    t128           temp   int                        4    568
    t129           temp   class Square *             4    572
    t130           temp   int                        4    576
    t131           temp   class Square *             4    580
    t132           temp   int                        4    584
    t133           temp   long long                  8    592
    t134           temp   int                        4    600
    t135           temp   long long                  8    608
    t136           temp   long long                  8    616
    t137           temp   long long                  8    624
    t138           temp   class Tag *                4    632
    t139           temp   class Tag *                4    636
    t140           temp   int                        4    640
    t141           temp   class Tag                  4    644
    t142           temp   class Tag *                4    648
    t143           temp   class Tag *                4    652
    t144           temp   int                        4    656
    t145           temp   int                        4    660
    t146           temp   class Tag *                4    664
    t147           temp   class Tag *                4    668
    t148           temp   class Copy *               4    672
    t149           temp   class Copy *               4    676
    t150           temp   class Copy *               4    680
    t151           temp   class Tag *                4    684
    t152           temp   class Tag *                4    688
    t153           temp   class Tag *                4    692
    t154           temp   class Tag *                4    696
    total width 700
  code
 223:      t2 = &t1
 224:      param t2                            (this)
 225:      param 1
 226:      call Tag::Tag(int), 2
 227:      t3 = &t1
 228:      param t3                            (this)
 229:      call Tag::~Tag(), 1
 230:      param "| "
 231:      call printf, 1
 232:      param 2
 233:      t4 = call make(int), 1
 234:      t5 = &t4
 235:      t6 = &t4
 236:      param t6                            (this)
 237:      call Tag::~Tag(), 1
 238:      param "| "
 239:      call printf, 1
 240:      t8 = &t7
 241:      param t8                            (this)
 242:      param 3
 243:      call Tag::Tag(int), 2
 244:      t9 = &t7
 245:      param t9                            (this)
 246:      t10 = call Tag::value(), 1
 247:      param 4
 248:      t11 = call make(int), 1
 249:      t12 = &t11
 250:      t13 = &t11
 251:      param t13                           (this)
 252:      t14 = call Tag::value(), 1
 253:      t15 = t10 int+ t14
 254:      v = t15
 255:      t16 = &t11
 256:      param t16                           (this)
 257:      call Tag::~Tag(), 1
 258:      t17 = &t7
 259:      param t17                           (this)
 260:      call Tag::~Tag(), 1
 261:      param "%d | "
 262:      param v
 263:      call printf, 2
 264:      param 5
 265:      t18 = call make(int), 1
 266:      t19 = &t18
 267:      kept = t18
 268:      t20 = &kept
 269:      param "| "
 270:      call printf, 1
 271:      t21 = &kept
 272:      t23 = &t22
 273:      param t23                           (this)
 274:      param 6
 275:      call Tag::Tag(int), 2
 276:      t24 = &t22
 277:      param t21                           (this)
 278:      param t24
 279:      t25 = call Tag::operator+(const class Tag &), 2
 280:      t26 = &t25
 281:      sum = t25
 282:      t27 = &sum
 283:      t28 = &t22
 284:      param t28                           (this)
 285:      call Tag::~Tag(), 1
 286:      t29 = sum[0]
 287:      param "%d | "
 288:      param t29
 289:      call printf, 2
 290:      t30 = &kept
 291:      t31 = &sum
 292:      param t30                           (this)
 293:      param t31
 294:      t32 = call Tag::operator+(const class Tag &), 2
 295:      t33 = &t32
 296:      t34 = &t32
 297:      t35 = &kept
 298:      param t34                           (this)
 299:      param t35
 300:      t36 = call Tag::operator+(const class Tag &), 2
 301:      t37 = &t36
 302:      t38 = t36[0]
 303:      v = t38
 304:      t39 = &t36
 305:      param t39                           (this)
 306:      call Tag::~Tag(), 1
 307:      t40 = &t32
 308:      param t40                           (this)
 309:      call Tag::~Tag(), 1
 310:      param "%d | "
 311:      param v
 312:      call printf, 2
 313:      t42 = &t41
 314:      param t42                           (this)
 315:      param 10
 316:      call Tag::Tag(int), 2
 317:      param t41
 318:      t43 = call byValue(class Tag), 1
 319:      v = t43
 320:      t44 = &t41
 321:      param t44                           (this)
 322:      call Tag::~Tag(), 1
 323:      param "%d | "
 324:      param v
 325:      call printf, 2
 326:      t45 = kept
 327:      t46 = &t45
 328:      param t45
 329:      t47 = call byValue(class Tag), 1
 330:      v = t47
 331:      t48 = &t45
 332:      param t48                           (this)
 333:      call Tag::~Tag(), 1
 334:      param "%d | "
 335:      param v
 336:      call printf, 2
 337:      t50 = &t49
 338:      param t50                           (this)
 339:      param 11
 340:      call Tag::Tag(int), 2
 341:      t51 = &t49
 342:      param t51
 343:      t52 = call byRef(const class Tag &), 1
 344:      v = t52
 345:      t53 = &t49
 346:      param t53                           (this)
 347:      call Tag::~Tag(), 1
 348:      param "%d | "
 349:      param v
 350:      call printf, 2
 351:      t55 = &t54
 352:      param t55                           (this)
 353:      param 12
 354:      call Tag::Tag(int), 2
 355:      t56 = &t54
 356:      param t56
 357:      t57 = call byRef(const class Tag &), 1
 358:      t58 = &t54
 359:      param t58                           (this)
 360:      call Tag::~Tag(), 1
 361:      if t57 int> 5 goto L6
 362:      goto L7
 363: L6:  param "if "
 364:      call printf, 1
 365: L7:  param "| "
 366:      call printf, 1
 367:      i = 0
 368: L8:  if i int< 2 goto L9
 369:      goto L11
 370: L9:  t59 = 13 int+ i
 371:      param t59
 372:      t60 = call make(int), 1
 373:      t61 = &t60
 374:      t62 = t60[0]
 375:      t63 = &t60
 376:      param t63                           (this)
 377:      call Tag::~Tag(), 1
 378:      if t62 int> 0 goto L10
 379:      goto L11
 380: L10: param "body "
 381:      call printf, 1
 382:      t65 = &t64
 383:      param t65                           (this)
 384:      param 20
 385:      call Tag::Tag(int), 2
 386:      t66 = &t64
 387:      param t66
 388:      t67 = call byRef(const class Tag &), 1
 389:      t68 = i int+ t67
 390:      i = t68
 391:      t69 = &t64
 392:      param t69                           (this)
 393:      call Tag::~Tag(), 1
 394:      goto L8
 395: L11: param "| "
 396:      call printf, 1
 397:      if v int> 0 goto L12
 398:      goto L13
 399: L12: t72 = &t71
 400:      param t72                           (this)
 401:      param 21
 402:      call Tag::Tag(int), 2
 403:      t73 = t71[0]
 404:      t70 = t73
 405:      t74 = &t71
 406:      param t74                           (this)
 407:      call Tag::~Tag(), 1
 408:      goto L14
 409: L13: t76 = &t75
 410:      param t76                           (this)
 411:      param 22
 412:      call Tag::Tag(int), 2
 413:      t77 = t75[0]
 414:      t70 = t77
 415:      t78 = &t75
 416:      param t78                           (this)
 417:      call Tag::~Tag(), 1
 418: L14: v = t70
 419:      param "%d | "
 420:      param v
 421:      call printf, 2
 422:      param 30
 423:      t79 = call named(int), 1
 424:      t80 = &t79
 425:      n = t79
 426:      t81 = &n
 427:      t82 = n[0]
 428:      param "%d | "
 429:      param t82
 430:      call printf, 2
 431:      param 1
 432:      t83 = call pick(int), 1
 433:      t84 = &t83
 434:      t85 = t83[0]
 435:      v = t85
 436:      t86 = &t83
 437:      param t86                           (this)
 438:      call Tag::~Tag(), 1
 439:      param 0
 440:      t87 = call pick(int), 1
 441:      t88 = &t87
 442:      t89 = t87[0]
 443:      t90 = v int+ t89
 444:      v = t90
 445:      t91 = &t87
 446:      param t91                           (this)
 447:      call Tag::~Tag(), 1
 448:      param "%d | "
 449:      param v
 450:      call printf, 2
 451:      t93 = &t92
 452:      param t93                           (this)
 453:      param 50
 454:      call Tag::Tag(int), 2
 455:      t94 = &t92
 456:      r = t94
 457:      t95 = *r
 458:      param "%d | "
 459:      param t95
 460:      call printf, 2
 461:      t97 = &t96
 462:      param t97                           (this)
 463:      param 60
 464:      call Tag::Tag(int), 2
 465:      kept = t96
 466:      t98 = &t96
 467:      param t98                           (this)
 468:      call Tag::~Tag(), 1
 469:      t99 = kept[0]
 470:      param "%d\n"
 471:      param t99
 472:      call printf, 2
 473:      t100 = &c
 474:      param t100                          (this)
 475:      param 1
 476:      call Copy::Copy(int), 2
 477:      param "| "
 478:      call printf, 1
 479:      t102 = &t101
 480:      t103 = &c
 481:      param t102                          (this)
 482:      param t103
 483:      call Copy::Copy(const class Copy &), 2
 484:      param t101
 485:      t104 = call copied(class Copy), 1
 486:      v = t104
 487:      t105 = &t101
 488:      param t105                          (this)
 489:      call Copy::~Copy(), 1
 490:      param "%d | "
 491:      param v
 492:      call printf, 2
 493:      t107 = &t106
 494:      param t107                          (this)
 495:      param 2
 496:      call Copy::Copy(int), 2
 497:      param t106
 498:      t108 = call copied(class Copy), 1
 499:      v = t108
 500:      t109 = &t106
 501:      param t109                          (this)
 502:      call Copy::~Copy(), 1
 503:      param "%d | "
 504:      param v
 505:      call printf, 2
 506:      param 3
 507:      t110 = call makeCopy(int), 1
 508:      t111 = &t110
 509:      d = t110
 510:      t112 = &d
 511:      t113 = d[0]
 512:      param "%d | "
 513:      param t113
 514:      call printf, 2
 515:      t115 = &t114
 516:      t116 = &c
 517:      param t115                          (this)
 518:      param t116
 519:      call Copy::Copy(const class Copy &), 2
 520:      param t114
 521:      t117 = call sameCopy(class Copy), 1
 522:      t118 = &t117
 523:      e = t117
 524:      t119 = &e
 525:      t120 = &t114
 526:      param t120                          (this)
 527:      call Copy::~Copy(), 1
 528:      t121 = e[0]
 529:      param "%d\n"
 530:      param t121
 531:      call printf, 2
 532:      t122 = &q
 533:      p = t122
 534:      t123 = &q
 535:      param t123                          (this)
 536:      t124 = call Square::sides(), 1
 537:      t125 = &q
 538:      param t125                          (this)
 539:      t126 = call Shape::sides(), 1
 540:      param p                             (this)
 541:      t127 = call Shape::sides(), 1
 542:      param p                             (this)
 543:      t128 = call Shape::sides(), 1
 544:      t129 = &q
 545:      param t129                          (this)
 546:      t130 = call Square::kind(), 1
 547:      t131 = &q
 548:      param t131                          (this)
 549:      t132 = call Shape::kind(), 1
 550:      param "%d %d %d %d %d %d\n"
 551:      param t124
 552:      param t126
 553:      param t127
 554:      param t128
 555:      param t130
 556:      param t132
 557:      call printf, 7
 558:      param 3
 559:      param 5
 560:      param 20
 561:      t133 = call mix(long long, long long, int), 3
 562:      m = t133
 563:      t134 = int- 7
 564:      t135 = inttollong t134
 565:      t136 = 1 llong<< 40
 566:      param t135
 567:      param t136
 568:      param 9
 569:      t137 = call mix(long long, long long, int), 3
 570:      param "%lld %lld\n"
 571:      param m
 572:      param t137
 573:      call printf, 3
 574:      t138 = &inner
 575:      param t138                          (this)
 576:      param 70
 577:      call Tag::Tag(int), 2
 578:      t139 = &inner
 579:      param t139
 580:      t140 = call byRef(const class Tag &), 1
 581:      t142 = &t141
 582:      param t142                          (this)
 583:      param 71
 584:      call Tag::Tag(int), 2
 585:      t143 = &t141
 586:      param t143
 587:      t144 = call byRef(const class Tag &), 1
 588:      t145 = t140 int+ t144
 589:      param "%d "
 590:      param t145
 591:      call printf, 2
 592:      t146 = &t141
 593:      param t146                          (this)
 594:      call Tag::~Tag(), 1
 595:      t147 = &inner
 596:      param t147                          (this)
 597:      call Tag::~Tag(), 1
 598:      param "end\n"
 599:      call printf, 1
 600:      t148 = &e
 601:      param t148                          (this)
 602:      call Copy::~Copy(), 1
 603:      t149 = &d
 604:      param t149                          (this)
 605:      call Copy::~Copy(), 1
 606:      t150 = &c
 607:      param t150                          (this)
 608:      call Copy::~Copy(), 1
 609:      t151 = &t92
 610:      param t151                          (this)
 611:      call Tag::~Tag(), 1
 612:      t152 = &n
 613:      param t152                          (this)
 614:      call Tag::~Tag(), 1
 615:      t153 = &sum
 616:      param t153                          (this)
 617:      call Tag::~Tag(), 1
 618:      t154 = &kept
 619:      param t154                          (this)
 620:      call Tag::~Tag(), 1
 621:      return 0


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Tag                class_tag      class Tag                  -        global                         7     -     0     Tag                  -                        size 4
Tag::id            field          int                        member   global > class Tag             9     4     20    Tag::id              -                        public, offset 0
Tag::Tag           constructor    void (int)                 -        global > class Tag             10    -     18    _ZN3TagC1Ei          _ZN3TagC1Ei              public
Tag::~Tag          destructor     void (void)                -        global > class Tag             11    -     0     _ZN3TagD1Ev          _ZN3TagD1Ev              public
Tag::value         method         int (void)                 -        global > class Tag             12    -     2     _ZN3Tag5valueEv      _ZN3Tag5valueEv          public, defined
Tag::operator+     method         class Tag (const class Tag &) -        global > class Tag             13    -     3     _ZN3TagplERKS_       _ZN3TagplERKS_           public, defined
n                  parameter      int                        param    global > class Tag > Tag()     10    4     1     n.1                  -                        
o                  parameter      const class Tag &          param    global > class Tag > operator+() 13    4     1     o.2                  -                        
Copy               class_tag      class Copy                 -        global                         16    -     0     Copy                 -                        size 4
Copy::id           field          int                        member   global > class Copy            18    4     9     Copy::id             -                        public, offset 0
Copy::Copy         constructor    void (int)                 -        global > class Copy            19    -     3     _ZN4CopyC1Ei         _ZN4CopyC1Ei             public
Copy::Copy         constructor    void (const class Copy &)  -        global > class Copy            20    -     0     _ZN4CopyC1ERKS_      _ZN4CopyC1ERKS_          public
Copy::~Copy        destructor     void (void)                -        global > class Copy            21    -     0     _ZN4CopyD1Ev         _ZN4CopyD1Ev             public
n                  parameter      int                        param    global > class Copy > Copy()   19    4     1     n.3                  -                        
o                  parameter      const class Copy &         param    global > class Copy > Copy()   20    4     1     o.4                  -                        
make               function       class Tag (int)            -        global                         24    -     4     _Z4makei             _Z4makei                 defined
n                  parameter      int                        param    global > make()                24    4     1     n.5                  -                        
named              function       class Tag (int)            -        global                         25    -     1     _Z5namedi            _Z5namedi                defined
n                  parameter      int                        param    global > named()               25    4     1     n.6                  -                        
t                  variable       class Tag                  local    global > named()               26    4     3     t.7                  -                        
pick               function       class Tag (int)            -        global                         30    -     2     _Z4picki             _Z4picki                 defined
which              parameter      int                        param    global > pick()                30    4     1     which.8              -                        
a                  variable       class Tag                  local    global > pick()                31    4     1     a.9                  -                        
b                  variable       class Tag                  local    global > pick()                32    4     1     b.10                 -                        
byValue            function       int (class Tag)            -        global                         36    -     2     _Z7byValue3Tag       _Z7byValue3Tag           defined
t                  parameter      class Tag                  param    global > byValue()             36    4     1     t.11                 -                        
byRef              function       int (const class Tag &)    -        global                         37    -     5     _Z5byRefRK3Tag       _Z5byRefRK3Tag           defined
t                  parameter      const class Tag &          param    global > byRef()               37    4     1     t.12                 -                        
copied             function       int (class Copy)           -        global                         38    -     2     _Z6copied4Copy       _Z6copied4Copy           defined
c                  parameter      class Copy                 param    global > copied()              38    4     1     c.13                 -                        
makeCopy           function       class Copy (int)           -        global                         39    -     1     _Z8makeCopyi         _Z8makeCopyi             defined
n                  parameter      int                        param    global > makeCopy()            39    4     1     n.14                 -                        
sameCopy           function       class Copy (class Copy)    -        global                         40    -     1     _Z8sameCopy4Copy     _Z8sameCopy4Copy         defined
c                  parameter      class Copy                 param    global > sameCopy()            40    4     1     c.15                 -                        
Shape              class_tag      class Shape                -        global                         42    -     0     Shape                -                        size 1
Shape::sides       method         int (void)                 -        global > class Shape           44    -     3     _ZN5Shape5sidesEv    _ZN5Shape5sidesEv        public, defined
Shape::kind        method         int (void)                 -        global > class Shape           45    -     1     _ZN5Shape4kindEv     _ZN5Shape4kindEv         public, defined
Square             class_tag      class Square               -        global                         47    -     0     Square               -                        size 1, public base Shape
Square::sides      method         int (void)                 -        global > class Square          49    -     1     _ZN6Square5sidesEv   _ZN6Square5sidesEv       public, defined
Square::kind       method         int (void)                 -        global > class Square          50    -     1     _ZN6Square4kindEv    _ZN6Square4kindEv        public, defined
mix                function       long long (long long, long long, int) -        global                         53    -     2     _Z3mixxxi            _Z3mixxxi                defined
a                  parameter      long long                  param    global > mix()                 53    8     4     a.16                 -                        
b                  parameter      long long                  param    global > mix()                 53    8     4     b.17                 -                        
n                  parameter      int                        param    global > mix()                 53    4     1     n.18                 -                        
sum                variable       long long                  local    global > mix()                 54    8     5     sum.19               -                        
i                  variable       int                        local    global > mix() > for           55    4     3     i.20                 -                        
main               function       int (void)                 -        global                         63    -     0     main                 main                     defined
v                  variable       int                        local    global > main()                68    4     20    v.21                 -                        
kept               variable       class Tag                  local    global > main()                70    4     6     kept.22              -                        
sum                variable       class Tag                  local    global > main()                72    4     2     sum.23               -                        
i                  variable       int                        local    global > main() > for          84    4     4     i.24                 -                        
n                  variable       class Tag                  local    global > main()                88    4     1     n.25                 -                        
r                  variable       const class Tag &          local    global > main()                93    4     1     r.26                 -                        
c                  variable       class Copy                 local    global > main()                98    4     2     c.27                 -                        
d                  variable       class Copy                 local    global > main()                104   4     1     d.28                 -                        
e                  variable       class Copy                 local    global > main()                106   4     1     e.29                 -                        
q                  variable       class Square               local    global > main()                109   1     5     q.30                 -                        
p                  variable       class Shape *              local    global > main()                110   4     2     p.31                 -                        
m                  variable       long long                  local    global > main()                113   8     1     m.32                 -                        
inner              variable       class Tag                  local    global > main() > block        116   4     1     inner.33             -                        

=== Record Layouts ===
class Tag: size 4, align 4
    +0  int id  [public]
class Copy: size 4, align 4
    +0  int id  [public]
class Shape: size 1, align 1
class Square: size 1, align 1
    (base Shape, public)
