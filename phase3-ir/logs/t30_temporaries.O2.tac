=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t30_temporaries.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 522 -> 438 instruction(s) for 'test/t30_temporaries.c'.

optimization summary (-O2)
    instructions                522 -> 438   (16% fewer)
    constants folded            3
    algebraic simplifications   0
    common subexpressions       51
    copies / constants forwarded 69
    temporaries merged away     6
    dead instructions removed   59
    jumps removed or redirected 6
    unreachable instructions    0
    propagated across blocks    1
    dead assignments removed    13

function Tag::Tag(int)        link name: _ZN3TagC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 100:   *this = n
 101:   param "+%d "
 102:   param n
 103:   call printf, 2
 104:   return

function Tag::~Tag()        link name: _ZN3TagD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 105:   t1 = *this
 106:   param "-%d "
 107:   param t1
 108:   call printf, 2
 109:   return

function Tag::value()        link name: _ZN3Tag5valueEv
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 110:   t1 = *this
 111:   t2 = t1 int* 10
 112:   return t2

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
 113:   t2 = &t1
 114:   t3 = *this
 115:   t4 = *o
 116:   t5 = t3 int+ t4
 117:   param t2                            (this)
 118:   param t5
 119:   call Tag::Tag(int), 2
 120:   return t1

function Copy::Copy(int)        link name: _ZN4CopyC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 121:   *this = n
 122:   param "+c%d "
 123:   param n
 124:   call printf, 2
 125:   return

function Copy::Copy(const class Copy &)        link name: _ZN4CopyC1ERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    o              param  const class Copy &         4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 126:   t1 = *o
 127:   t2 = t1 int+ 100
 128:   *this = t2
 129:   param "copy%d "
 130:   param t2
 131:   call printf, 2
 132:   return

function Copy::~Copy()        link name: _ZN4CopyD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    t1             temp   int                        4      4
    total width 8
  code
 133:   t1 = *this
 134:   param "-c%d "
 135:   param t1
 136:   call printf, 2
 137:   return

function make(int)        link name: _Z4makei
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   class Tag                  4      4
    t2             temp   class Tag *                4      8
    total width 12
  code
 138:   t2 = &t1
 139:   param t2                            (this)
 140:   param n
 141:   call Tag::Tag(int), 2
 142:   return t1

function named(int)        link name: _Z5namedi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t              local  class Tag                  4      4
    t1             temp   class Tag *                4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 143:   t1 = &t
 144:   param t1                            (this)
 145:   param n
 146:   call Tag::Tag(int), 2
 147:   t2 = t[0]
 148:   t3 = t2 int+ 1
 149:   t[0] = t3
 150:   return t

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
 151:     t1 = &a
 152:     param t1                            (this)
 153:     param 40
 154:     call Tag::Tag(int), 2
 155:     t2 = &b
 156:     param t2                            (this)
 157:     param 41
 158:     call Tag::Tag(int), 2
 159:     if which int== 0 goto L1
 160:     t3 = a
 161:     t4 = &b
 162:     param t4                            (this)
 163:     call Tag::~Tag(), 1
 164:     t5 = &a
 165:     param t5                            (this)
 166:     call Tag::~Tag(), 1
 167:     return t3
 168: L1: t6 = b
 169:     t7 = &b
 170:     param t7                            (this)
 171:     call Tag::~Tag(), 1
 172:     t8 = &a
 173:     param t8                            (this)
 174:     call Tag::~Tag(), 1
 175:     return t6

function byValue(class Tag)        link name: _Z7byValue3Tag
  symbol table (name, kind, type, width, offset)
    t              param  class Tag                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 176:   t1 = t[0]
 177:   return t1

function byRef(const class Tag &)        link name: _Z5byRefRK3Tag
  symbol table (name, kind, type, width, offset)
    t              param  const class Tag &          4      0
    t1             temp   int                        4      4
    total width 8
  code
 178:   t1 = *t
 179:   return t1

function copied(class Copy)        link name: _Z6copied4Copy
  symbol table (name, kind, type, width, offset)
    c              param  class Copy                 4      0
    t1             temp   int                        4      4
    total width 8
  code
 180:   t1 = c[0]
 181:   return t1

function makeCopy(int)        link name: _Z8makeCopyi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   class Copy                 4      4
    t2             temp   class Copy *               4      8
    total width 12
  code
 182:   t2 = &t1
 183:   param t2                            (this)
 184:   param n
 185:   call Copy::Copy(int), 2
 186:   return t1

function sameCopy(class Copy)        link name: _Z8sameCopy4Copy
  symbol table (name, kind, type, width, offset)
    c              param  class Copy                 4      0
    t1             temp   class Copy                 4      4
    t2             temp   class Copy *               4      8
    t3             temp   class Copy *               4     12
    total width 16
  code
 187:   t2 = &t1
 188:   t3 = &c
 189:   param t2                            (this)
 190:   param t3
 191:   call Copy::Copy(const class Copy &), 2
 192:   return t1

function Shape::sides()        link name: _ZN5Shape5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 193:   return 0

function Shape::kind()        link name: _ZN5Shape4kindEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 194:   return 1

function Square::sides()        link name: _ZN6Square5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 195:   return 4

function Square::kind()        link name: _ZN6Square4kindEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 196:   return 2

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
 197:     sum = 0
 198:     i = 0
 199: L2: if i int>= n goto L3
 200:     t1 = inttollong i
 201:     t2 = a llong* t1
 202:     t3 = sum llong+ t2
 203:     t4 = b llong^ sum
 204:     t5 = t3 llong- t4
 205:     sum = t5
 206:     a = a llong+ 4294967296
 207:     t7 = llong- b
 208:     t8 = t5 llong& 65535
 209:     b = t7 llong+ t8
 210:     i = i int+ 1
 211:     goto L2
 212: L3: t11 = sum llong+ a
 213:     t12 = t11 llong- b
 214:     return t12

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
 215:     t2 = &t1
 216:     param t2                            (this)
 217:     param 1
 218:     call Tag::Tag(int), 2
 219:     param t2                            (this)
 220:     call Tag::~Tag(), 1
 221:     param "| "
 222:     call printf, 1
 223:     param 2
 224:     t4 = call make(int), 1
 225:     t5 = &t4
 226:     param t5                            (this)
 227:     call Tag::~Tag(), 1
 228:     param "| "
 229:     call printf, 1
 230:     t8 = &t7
 231:     param t8                            (this)
 232:     param 3
 233:     call Tag::Tag(int), 2
 234:     param t8                            (this)
 235:     t10 = call Tag::value(), 1
 236:     param 4
 237:     t11 = call make(int), 1
 238:     t12 = &t11
 239:     param t12                           (this)
 240:     t14 = call Tag::value(), 1
 241:     t15 = t10 int+ t14
 242:     param t12                           (this)
 243:     call Tag::~Tag(), 1
 244:     param t8                            (this)
 245:     call Tag::~Tag(), 1
 246:     param "%d | "
 247:     param t15
 248:     call printf, 2
 249:     param 5
 250:     t18 = call make(int), 1
 251:     kept = t18
 252:     t20 = &kept
 253:     param "| "
 254:     call printf, 1
 255:     t23 = &t22
 256:     param t23                           (this)
 257:     param 6
 258:     call Tag::Tag(int), 2
 259:     param t20                           (this)
 260:     param t23
 261:     t25 = call Tag::operator+(const class Tag &), 2
 262:     sum = t25
 263:     t27 = &sum
 264:     param t23                           (this)
 265:     call Tag::~Tag(), 1
 266:     t29 = sum[0]
 267:     param "%d | "
 268:     param t29
 269:     call printf, 2
 270:     param t20                           (this)
 271:     param t27
 272:     t32 = call Tag::operator+(const class Tag &), 2
 273:     t33 = &t32
 274:     param t33                           (this)
 275:     param t20
 276:     t36 = call Tag::operator+(const class Tag &), 2
 277:     t37 = &t36
 278:     t38 = t36[0]
 279:     param t37                           (this)
 280:     call Tag::~Tag(), 1
 281:     param t33                           (this)
 282:     call Tag::~Tag(), 1
 283:     param "%d | "
 284:     param t38
 285:     call printf, 2
 286:     t42 = &t41
 287:     param t42                           (this)
 288:     param 10
 289:     call Tag::Tag(int), 2
 290:     param t41
 291:     t43 = call byValue(class Tag), 1
 292:     param t42                           (this)
 293:     call Tag::~Tag(), 1
 294:     param "%d | "
 295:     param t43
 296:     call printf, 2
 297:     t45 = kept
 298:     t46 = &t45
 299:     param t45
 300:     t47 = call byValue(class Tag), 1
 301:     param t46                           (this)
 302:     call Tag::~Tag(), 1
 303:     param "%d | "
 304:     param t47
 305:     call printf, 2
 306:     t50 = &t49
 307:     param t50                           (this)
 308:     param 11
 309:     call Tag::Tag(int), 2
 310:     param t50
 311:     t52 = call byRef(const class Tag &), 1
 312:     param t50                           (this)
 313:     call Tag::~Tag(), 1
 314:     param "%d | "
 315:     param t52
 316:     call printf, 2
 317:     t55 = &t54
 318:     param t55                           (this)
 319:     param 12
 320:     call Tag::Tag(int), 2
 321:     param t55
 322:     t57 = call byRef(const class Tag &), 1
 323:     param t55                           (this)
 324:     call Tag::~Tag(), 1
 325:     if t57 int<= 5 goto L4
 326:     param "if "
 327:     call printf, 1
 328: L4: param "| "
 329:     call printf, 1
 330:     i = 0
 331: L5: if i int>= 2 goto L6
 332:     t59 = 13 int+ i
 333:     param t59
 334:     t60 = call make(int), 1
 335:     t61 = &t60
 336:     t62 = t60[0]
 337:     param t61                           (this)
 338:     call Tag::~Tag(), 1
 339:     if t62 int<= 0 goto L6
 340:     param "body "
 341:     call printf, 1
 342:     t65 = &t64
 343:     param t65                           (this)
 344:     param 20
 345:     call Tag::Tag(int), 2
 346:     param t65
 347:     t67 = call byRef(const class Tag &), 1
 348:     i = i int+ t67
 349:     param t65                           (this)
 350:     call Tag::~Tag(), 1
 351:     goto L5
 352: L6: param "| "
 353:     call printf, 1
 354:     if t52 int<= 0 goto L7
 355:     t72 = &t71
 356:     param t72                           (this)
 357:     param 21
 358:     call Tag::Tag(int), 2
 359:     t70 = t71[0]
 360:     param t72                           (this)
 361:     call Tag::~Tag(), 1
 362:     goto L8
 363: L7: t76 = &t75
 364:     param t76                           (this)
 365:     param 22
 366:     call Tag::Tag(int), 2
 367:     t70 = t75[0]
 368:     param t76                           (this)
 369:     call Tag::~Tag(), 1
 370: L8: param "%d | "
 371:     param t70
 372:     call printf, 2
 373:     param 30
 374:     t79 = call named(int), 1
 375:     n = t79
 376:     t81 = &n
 377:     t82 = n[0]
 378:     param "%d | "
 379:     param t82
 380:     call printf, 2
 381:     param 1
 382:     t83 = call pick(int), 1
 383:     t84 = &t83
 384:     t85 = t83[0]
 385:     param t84                           (this)
 386:     call Tag::~Tag(), 1
 387:     param 0
 388:     t87 = call pick(int), 1
 389:     t88 = &t87
 390:     t89 = t87[0]
 391:     t90 = t85 int+ t89
 392:     param t88                           (this)
 393:     call Tag::~Tag(), 1
 394:     param "%d | "
 395:     param t90
 396:     call printf, 2
 397:     t93 = &t92
 398:     param t93                           (this)
 399:     param 50
 400:     call Tag::Tag(int), 2
 401:     t95 = *t93
 402:     param "%d | "
 403:     param t95
 404:     call printf, 2
 405:     t97 = &t96
 406:     param t97                           (this)
 407:     param 60
 408:     call Tag::Tag(int), 2
 409:     kept = t96
 410:     param t97                           (this)
 411:     call Tag::~Tag(), 1
 412:     t99 = kept[0]
 413:     param "%d\n"
 414:     param t99
 415:     call printf, 2
 416:     t100 = &c
 417:     param t100                          (this)
 418:     param 1
 419:     call Copy::Copy(int), 2
 420:     param "| "
 421:     call printf, 1
 422:     t102 = &t101
 423:     param t102                          (this)
 424:     param t100
 425:     call Copy::Copy(const class Copy &), 2
 426:     param t101
 427:     t104 = call copied(class Copy), 1
 428:     param t102                          (this)
 429:     call Copy::~Copy(), 1
 430:     param "%d | "
 431:     param t104
 432:     call printf, 2
 433:     t107 = &t106
 434:     param t107                          (this)
 435:     param 2
 436:     call Copy::Copy(int), 2
 437:     param t106
 438:     t108 = call copied(class Copy), 1
 439:     param t107                          (this)
 440:     call Copy::~Copy(), 1
 441:     param "%d | "
 442:     param t108
 443:     call printf, 2
 444:     param 3
 445:     t110 = call makeCopy(int), 1
 446:     d = t110
 447:     t112 = &d
 448:     t113 = d[0]
 449:     param "%d | "
 450:     param t113
 451:     call printf, 2
 452:     t115 = &t114
 453:     param t115                          (this)
 454:     param t100
 455:     call Copy::Copy(const class Copy &), 2
 456:     param t114
 457:     t117 = call sameCopy(class Copy), 1
 458:     e = t117
 459:     t119 = &e
 460:     param t115                          (this)
 461:     call Copy::~Copy(), 1
 462:     t121 = e[0]
 463:     param "%d\n"
 464:     param t121
 465:     call printf, 2
 466:     t122 = &q
 467:     param t122                          (this)
 468:     t124 = call Square::sides(), 1
 469:     param t122                          (this)
 470:     t126 = call Shape::sides(), 1
 471:     param t122                          (this)
 472:     t127 = call Shape::sides(), 1
 473:     param t122                          (this)
 474:     t128 = call Shape::sides(), 1
 475:     param t122                          (this)
 476:     t130 = call Square::kind(), 1
 477:     param t122                          (this)
 478:     t132 = call Shape::kind(), 1
 479:     param "%d %d %d %d %d %d\n"
 480:     param t124
 481:     param t126
 482:     param t127
 483:     param t128
 484:     param t130
 485:     param t132
 486:     call printf, 7
 487:     param 3
 488:     param 5
 489:     param 20
 490:     t133 = call mix(long long, long long, int), 3
 491:     param -7
 492:     param 1099511627776
 493:     param 9
 494:     t137 = call mix(long long, long long, int), 3
 495:     param "%lld %lld\n"
 496:     param t133
 497:     param t137
 498:     call printf, 3
 499:     t138 = &inner
 500:     param t138                          (this)
 501:     param 70
 502:     call Tag::Tag(int), 2
 503:     param t138
 504:     t140 = call byRef(const class Tag &), 1
 505:     t142 = &t141
 506:     param t142                          (this)
 507:     param 71
 508:     call Tag::Tag(int), 2
 509:     param t142
 510:     t144 = call byRef(const class Tag &), 1
 511:     t145 = t140 int+ t144
 512:     param "%d "
 513:     param t145
 514:     call printf, 2
 515:     param t142                          (this)
 516:     call Tag::~Tag(), 1
 517:     param t138                          (this)
 518:     call Tag::~Tag(), 1
 519:     param "end\n"
 520:     call printf, 1
 521:     param t119                          (this)
 522:     call Copy::~Copy(), 1
 523:     param t112                          (this)
 524:     call Copy::~Copy(), 1
 525:     param t100                          (this)
 526:     call Copy::~Copy(), 1
 527:     param t93                           (this)
 528:     call Tag::~Tag(), 1
 529:     param t81                           (this)
 530:     call Tag::~Tag(), 1
 531:     t153 = &sum
 532:     param t153                          (this)
 533:     call Tag::~Tag(), 1
 534:     t154 = &kept
 535:     param t154                          (this)
 536:     call Tag::~Tag(), 1
 537:     return 0


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
