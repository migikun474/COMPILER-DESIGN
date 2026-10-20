=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t22_data_structures.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 321 -> 299 instruction(s) for 'test/t22_data_structures.c'.

optimization summary (-O3)
    instructions                321 -> 299   (6% fewer)
    constants folded            5
    algebraic simplifications   11
    common subexpressions       11
    copies / constants forwarded 53
    temporaries merged away     15
    dead instructions removed   25
    jumps removed or redirected 15
    unreachable instructions    1
    propagated across blocks    11
    dead assignments removed    14
    calls inlined               6
    tail calls turned to jumps  1
    common across blocks        2
    moved out of loops          5

function prepend(struct Node *, int)        link name: _Z7prependP4Nodei
  symbol table (name, kind, type, width, offset)
    head           param  struct Node *              4      0
    v              param  int                        4      4
    n              local  struct Node *              4      8
    t1             temp   void *                     4     12
    t2             temp   struct Node *              4     16
    total width 20
  code
 100:   param 8
 101:   t1 = call malloc, 1
 102:   *t1 = v
 103:   t2 = t1 ptr+ 4
 104:   *t2 = head
 105:   return t1

function reverse(struct Node *)        link name: _Z7reverseP4Node
  symbol table (name, kind, type, width, offset)
    head           param  struct Node *              4      0
    prev           local  struct Node *              4      4
    next           local  struct Node *              4      8
    t1             temp   struct Node *              4     12
    t2             temp   struct Node *              4     16
    t3             temp   struct Node *              4     20
    total width 24
  code
 106:     prev = 0
 107: L1: if head ptr== 0 goto L2
 108:     t1 = head ptr+ 4
 109:     t2 = *t1
 110:     *t1 = prev
 111:     prev = head
 112:     head = t2
 113:     goto L1
 114: L2: return prev

function removeValue(struct Node **, int)        link name: _Z11removeValuePP4Nodei
  symbol table (name, kind, type, width, offset)
    link           param  struct Node **             4      0
    v              param  int                        4      4
    dead           local  struct Node *              4      8
    t1             temp   struct Node *              4     12
    t2             temp   struct Node *              4     16
    t3             temp   int                        4     20
    t4             temp   struct Node *              4     24
    t5             temp   struct Node *              4     28
    t6             temp   struct Node *              4     32
    t7             temp   struct Node *              4     36
    t8             temp   struct Node *              4     40
    total width 44
  code
 115: L3: t1 = *link
 116:     if t1 ptr== 0 goto L5
 117:     t2 = *link
 118:     t3 = *t2
 119:     if t3 int!= v goto L4
 120:     t4 = *link
 121:     t5 = t4 ptr+ 4
 122:     t6 = *t5
 123:     *link = t6
 124:     param t4
 125:     call free, 1
 126:     goto L3
 127: L4: t7 = *link
 128:     link = t7 ptr+ 4
 129:     goto L3
 130: L5: return

function insert(struct Tree *, int)        link name: _Z6insertP4Treei
  symbol table (name, kind, type, width, offset)
    t              param  struct Tree *              4      0
    key            param  int                        4      4
    t1             temp   void *                     4      8
    t2             temp   struct Tree *              4     12
    t3             temp   struct Tree *              4     16
    t4             temp   int                        4     20
    t5             temp   struct Tree *              4     24
    t6             temp   struct Tree *              4     28
    t7             temp   struct Tree *              4     32
    t8             temp   struct Tree *              4     36
    t9             temp   struct Tree *              4     40
    t10            temp   struct Tree *              4     44
    t11            temp   struct Tree *              4     48
    t12            temp   struct Tree *              4     52
    total width 56
  code
 131:     if t ptr!= 0 goto L6
 132:     param 12
 133:     t1 = call malloc, 1
 134:     t = t1
 135:     *t1 = key
 136:     t2 = t1 ptr+ 8
 137:     *t2 = 0
 138:     t3 = t1 ptr+ 4
 139:     *t3 = 0
 140:     goto L8
 141: L6: t4 = *t
 142:     if key int>= t4 goto L7
 143:     t5 = t ptr+ 4
 144:     t6 = *t5
 145:     param t6
 146:     param key
 147:     t7 = call insert(struct Tree *, int), 2
 148:     *t5 = t7
 149:     goto L8
 150: L7: t9 = t ptr+ 8
 151:     t10 = *t9
 152:     param t10
 153:     param key
 154:     t11 = call insert(struct Tree *, int), 2
 155:     *t9 = t11
 156: L8: return t

function inorder(struct Tree *)        link name: _Z7inorderP4Tree
  symbol table (name, kind, type, width, offset)
    t              param  struct Tree *              4      0
    t1             temp   struct Tree *              4      4
    t2             temp   struct Tree *              4      8
    t3             temp   int                        4     12
    t4             temp   struct Tree *              4     16
    t5             temp   struct Tree *              4     20
    t6             temp   struct Tree *              4     24
    total width 28
  code
 157: L9:  if t ptr!= 0 goto L10
 158:      return
 159: L10: t1 = t ptr+ 4
 160:      t2 = *t1
 161:      param t2
 162:      call inorder(struct Tree *), 1
 163:      t3 = *t
 164:      param "%d "
 165:      param t3
 166:      call printf, 2
 167:      t4 = t ptr+ 8
 168:      t = *t4
 169:      goto L9

function height(struct Tree *)        link name: _Z6heightP4Tree
  symbol table (name, kind, type, width, offset)
    t              param  struct Tree *              4      0
    l              local  int                        4      4
    r              local  int                        4      8
    t1             temp   struct Tree *              4     12
    t2             temp   struct Tree *              4     16
    t3             temp   int                        4     20
    t4             temp   struct Tree *              4     24
    t5             temp   struct Tree *              4     28
    t6             temp   int                        4     32
    t7             temp   int                        4     36
    t8             temp   int                        4     40
    total width 44
  code
 170:      if t ptr!= 0 goto L11
 171:      return 0
 172: L11: t1 = t ptr+ 4
 173:      t2 = *t1
 174:      param t2
 175:      t3 = call height(struct Tree *), 1
 176:      t4 = t ptr+ 8
 177:      t5 = *t4
 178:      param t5
 179:      t6 = call height(struct Tree *), 1
 180:      if t3 int<= t6 goto L12
 181:      t7 = t3
 182:      goto L13
 183: L12: t7 = t6
 184: L13: t8 = 1 int+ t7
 185:      return t8

function push(Stack *, int)        link name: _Z4pushP5Stacki
  symbol table (name, kind, type, width, offset)
    s              param  Stack *                    4      0
    v              param  int                        4      4
    t1             temp   Stack *                    4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   Stack *                    4     20
    t5             temp   int                        4     24
    t6             temp   Stack *                    4     28
    total width 32
  code
 186:   t1 = s ptr+ 32
 187:   t2 = *t1
 188:   t3 = t2 int+ 1
 189:   *t1 = t3
 190:   t5 = t2 int<< 2                     (w = 4)
 191:   t6 = s ptr+ t5
 192:   *t6 = v
 193:   return

function pop(Stack *)        link name: _Z3popP5Stack
  symbol table (name, kind, type, width, offset)
    s              param  Stack *                    4      0
    t1             temp   Stack *                    4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   Stack *                    4     16
    t5             temp   int                        4     20
    t6             temp   Stack *                    4     24
    t7             temp   int                        4     28
    total width 32
  code
 194:   t1 = s ptr+ 32
 195:   t2 = *t1
 196:   t3 = t2 int- 1
 197:   *t1 = t3
 198:   t5 = t3 int<< 2                     (w = 4)
 199:   t6 = s ptr+ t5
 200:   t7 = *t6
 201:   return t7

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    list           local  struct Node *              4      0
    i.20           local  int                        4      4
    p              local  struct Node *              4      8
    root           local  struct Tree *              4     12
    keys           local  int[7]                    28     16
    i.24           local  int                        4     44
    s              local  Stack                     36     48
    i.26           local  int                        4     84
    a              local  int                        4     88
    b              local  int                        4     92
    rows           local  int                        4     96
    cols           local  int                        4    100
    table          local  int **                     4    104
    r.32           local  int                        4    108
    c              local  int                        4    112
    diagonal       local  int                        4    116
    r.35           local  int                        4    120
    last           local  int *                      4    124
    v1             local  int                        4    128
    v2             local  int                        4    132
    v3             local  int                        4    136
    ptrs           local  int *[3]                  12    140
    pp             local  int **                     4    152
    t1             temp   int                        4    156
    t2             temp   int                        4    160
    t3             temp   struct Node *              4    164
    t4             temp   int                        4    168
    t5             temp   struct Node *              4    172
    t6             temp   struct Node **             4    176
    t7             temp   int                        4    180
    t8             temp   struct Node *              4    184
    t9             temp   struct Node *              4    188
    t10            temp   int                        4    192
    t11            temp   int                        4    196
    t12            temp   struct Tree *              4    200
    t13            temp   int                        4    204
    t14            temp   struct Tree *              4    208
    t15            temp   int                        4    212
    t16            temp   struct Tree *              4    216
    t17            temp   struct Tree *              4    220
    t18            temp   struct Tree *              4    224
    t19            temp   struct Tree *              4    228
    t20            temp   struct Tree *              4    232
    t21            temp   struct Tree *              4    236
    t22            temp   int                        4    240
    t23            temp   struct Tree *              4    244
    t24            temp   struct Tree *              4    248
    t25            temp   struct Tree *              4    252
    t26            temp   struct Tree *              4    256
    t27            temp   int                        4    260
    t28            temp   Stack *                    4    264
    t29            temp   int                        4    268
    t30            temp   int                        4    272
    t31            temp   Stack *                    4    276
    t32            temp   int                        4    280
    t33            temp   Stack *                    4    284
    t34            temp   int                        4    288
    t35            temp   int                        4    292
    t36            temp   unsigned int               4    296
    t37            temp   void *                     4    300
    t38            temp   int                        4    304
    t39            temp   int **                     4    308
    t40            temp   unsigned int               4    312
    t41            temp   void *                     4    316
    t42            temp   int                        4    320
    t43            temp   int **                     4    324
    t44            temp   int *                      4    328
    t45            temp   int                        4    332
    t46            temp   int *                      4    336
    t47            temp   int                        4    340
    t48            temp   int                        4    344
    t49            temp   int                        4    348
    t50            temp   int                        4    352
    t51            temp   int                        4    356
    t52            temp   int **                     4    360
    t53            temp   int *                      4    364
    t54            temp   int                        4    368
    t55            temp   int *                      4    372
    t56            temp   int                        4    376
    t57            temp   int                        4    380
    t58            temp   int                        4    384
    t59            temp   int                        4    388
    t60            temp   int                        4    392
    t61            temp   int **                     4    396
    t62            temp   int *                      4    400
    t63            temp   int                        4    404
    t64            temp   int *                      4    408
    t65            temp   int *                      4    412
    t66            temp   int                        4    416
    t67            temp   int **                     4    420
    t68            temp   int *                      4    424
    t69            temp   int *                      4    428
    t70            temp   int                        4    432
    t71            temp   int *                      4    436
    t72            temp   int *                      4    440
    t73            temp   int *                      4    444
    t74            temp   int *(*)[3]                4    448
    t75            temp   int *                      4    452
    t76            temp   int *                      4    456
    t77            temp   int                        4    460
    t78            temp   int                        4    464
    t79            temp   int **                     4    468
    t80            temp   int *                      4    472
    t81            temp   int                        4    476
    t82            temp   int                        4    480
    t83            temp   struct Node *              4    484
    t84            temp   int                        4    488
    t85            temp   void *                     4    492
    t86            temp   struct Node *              4    496
    t87            temp   struct Node *              4    500
    t88            temp   struct Node *              4    504
    t89            temp   struct Node *              4    508
    t90            temp   struct Node *              4    512
    t91            temp   struct Node **             4    516
    t92            temp   int                        4    520
    t93            temp   struct Node *              4    524
    t94            temp   struct Node *              4    528
    t95            temp   int                        4    532
    t96            temp   struct Node *              4    536
    t97            temp   struct Node *              4    540
    t98            temp   struct Node *              4    544
    t99            temp   struct Node *              4    548
    t100           temp   Stack *                    4    552
    t101           temp   int                        4    556
    t102           temp   Stack *                    4    560
    t103           temp   int                        4    564
    t104           temp   int                        4    568
    t105           temp   int                        4    572
    t106           temp   Stack *                    4    576
    t107           temp   Stack *                    4    580
    t108           temp   Stack *                    4    584
    t109           temp   int                        4    588
    t110           temp   int                        4    592
    t111           temp   int                        4    596
    t112           temp   Stack *                    4    600
    t113           temp   int                        4    604
    t114           temp   Stack *                    4    608
    t115           temp   Stack *                    4    612
    t116           temp   int                        4    616
    t117           temp   int                        4    620
    t118           temp   int                        4    624
    t119           temp   Stack *                    4    628
    t120           temp   int                        4    632
    total width 636
  code
 202:      list = 0
 203:      i.20 = 1
 204: L14: if i.20 int> 6 goto L15
 205:      t1 = i.20 int* i.20
 206:      t2 = t1 int% 7
 207:      t83 = list
 208:      param 8
 209:      t85 = call malloc, 1
 210:      *t85 = t2
 211:      t86 = t85 ptr+ 4
 212:      *t86 = t83
 213:      list = t85
 214:      i.20 = i.20 int+ 1
 215:      goto L14
 216: L15: t87 = list
 217:      t88 = 0
 218: L16: if t87 ptr== 0 goto L17
 219:      t89 = t87 ptr+ 4
 220:      t90 = *t89
 221:      *t89 = t88
 222:      t88 = t87
 223:      t87 = t90
 224:      goto L16
 225: L17: list = t88
 226:      t91 = &list
 227: L18: t93 = *t91
 228:      if t93 ptr== 0 goto L20
 229:      t94 = *t91
 230:      t95 = *t94
 231:      if t95 int!= 2 goto L19
 232:      t96 = *t91
 233:      t97 = t96 ptr+ 4
 234:      t98 = *t97
 235:      *t91 = t98
 236:      param t96
 237:      call free, 1
 238:      goto L18
 239: L19: t99 = *t91
 240:      t91 = t99 ptr+ 4
 241:      goto L18
 242: L20: p = list
 243: L21: if p ptr== 0 goto L22
 244:      t7 = *p
 245:      param "%d "
 246:      param t7
 247:      call printf, 2
 248:      t8 = p ptr+ 4
 249:      p = *t8
 250:      goto L21
 251: L22: param "\n"
 252:      call printf, 1
 253:      root = 0
 254:      keys[0] = 50
 255:      keys[4] = 30
 256:      keys[8] = 70
 257:      keys[12] = 20
 258:      keys[16] = 40
 259:      keys[20] = 60
 260:      keys[24] = 80
 261:      i.24 = 0
 262: L23: if i.24 int>= 7 goto L24
 263:      t10 = i.24 int<< 2                  (w = 4)
 264:      t11 = keys[t10]
 265:      param root
 266:      param t11
 267:      root = call insert(struct Tree *, int), 2
 268:      i.24 = i.24 int+ 1
 269:      goto L23
 270: L24: param root
 271:      param 10
 272:      t14 = call insert(struct Tree *, int), 2
 273:      param t14
 274:      call inorder(struct Tree *), 1
 275:      param t14
 276:      t15 = call height(struct Tree *), 1
 277:      t16 = t14 ptr+ 4
 278:      t17 = *t16
 279:      t18 = t17 ptr+ 4
 280:      t19 = *t18
 281:      t20 = t19 ptr+ 4
 282:      t21 = *t20
 283:      t22 = *t21
 284:      t23 = t14 ptr+ 8
 285:      t24 = *t23
 286:      t25 = t24 ptr+ 4
 287:      t26 = *t25
 288:      t27 = *t26
 289:      param "\n%d %d %d\n"
 290:      param t15
 291:      param t22
 292:      param t27
 293:      call printf, 4
 294:      s[32] = 0
 295:      i.26 = 0
 296:      t28 = &s
 297:      t102 = t28 ptr+ 32
 298: L25: if i.26 int>= 5 goto L26
 299:      t29 = i.26 int* 3
 300:      t103 = *t102
 301:      t104 = t103 int+ 1
 302:      *t102 = t104
 303:      t105 = t103 int<< 2                 (w = 4)
 304:      t106 = t28 ptr+ t105
 305:      *t106 = t29
 306:      i.26 = i.26 int+ 1
 307:      goto L25
 308: L26: t109 = *t102
 309:      t110 = t109 int- 1
 310:      *t102 = t110
 311:      t111 = t110 int<< 2                 (w = 4)
 312:      t112 = t28 ptr+ t111
 313:      t113 = *t112
 314:      t117 = t110 int- 1
 315:      *t102 = t117
 316:      t118 = t117 int<< 2                 (w = 4)
 317:      t119 = t28 ptr+ t118
 318:      t120 = *t119
 319:      t35 = s[32]
 320:      param "%d %d %d\n"
 321:      param t113
 322:      param t120
 323:      param t35
 324:      call printf, 4
 325:      param 12
 326:      table = call malloc, 1
 327:      r.32 = 0
 328: L27: if r.32 int>= 3 goto L30
 329:      t38 = r.32 int<< 2
 330:      t39 = table ptr+ t38
 331:      param 16
 332:      t41 = call malloc, 1
 333:      *t39 = t41
 334:      c = 0
 335:      t47 = r.32 int* 10
 336: L28: if c int>= 4 goto L29
 337:      t44 = *t39
 338:      t45 = c int<< 2
 339:      t46 = t44 ptr+ t45
 340:      t48 = t47 int+ c
 341:      *t46 = t48
 342:      c = c int+ 1
 343:      goto L28
 344: L29: r.32 = r.32 int+ 1
 345:      goto L27
 346: L30: diagonal = 0
 347:      r.35 = 0
 348: L31: if r.35 int>= 3 goto L32
 349:      t51 = r.35 int<< 2
 350:      t52 = table ptr+ t51
 351:      t53 = *t52
 352:      t55 = t53 ptr+ t51
 353:      t56 = *t55
 354:      diagonal = diagonal int+ t56
 355:      r.35 = r.35 int+ 1
 356:      goto L31
 357: L32: t61 = table ptr+ 8
 358:      t62 = *t61
 359:      t64 = t62 ptr+ 16
 360:      t65 = t64 ptr- 4
 361:      t66 = *t65
 362:      t67 = table ptr+ 4
 363:      t68 = *t67
 364:      t69 = t68 ptr+ 8
 365:      t70 = *t69
 366:      param "%d %d %d\n"
 367:      param diagonal
 368:      param t66
 369:      param t70
 370:      call printf, 4
 371:      v1 = 1
 372:      v2 = 2
 373:      v3 = 3
 374:      t71 = &v3
 375:      t72 = &v1
 376:      t73 = &v2
 377:      ptrs[0] = t71
 378:      ptrs[4] = t72
 379:      ptrs[8] = t73
 380:      t74 = &ptrs
 381:      t75 = *t74
 382:      *t75 = 30
 383:      t76 = ptrs[8]
 384:      t77 = *t76
 385:      t78 = t77 int+ 5
 386:      *t76 = t78
 387:      t79 = t74 ptr+ 4
 388:      t80 = *t79
 389:      t81 = *t80
 390:      param "%d %d %d %d\n"
 391:      param v1
 392:      param v2
 393:      param v3
 394:      param t81
 395:      call printf, 5
 396:      param t14
 397:      t82 = call height(struct Tree *), 1
 398:      return t82


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Node               struct_tag     struct Node                -        global                         6     -     0     Node                 -                        size 8
Node::value        field          int                        member   global > struct Node           6     4     3     Node::value          -                        public, offset 0
Node::next         field          struct Node *              member   global > struct Node           6     4     6     Node::next           -                        public, offset 4
Tree               struct_tag     struct Tree                -        global                         7     -     0     Tree                 -                        size 12
Tree::key          field          int                        member   global > struct Tree           7     4     5     Tree::key            -                        public, offset 0
Tree::left         field          struct Tree *              member   global > struct Tree           7     4     9     Tree::left           -                        public, offset 4
Tree::right        field          struct Tree *              member   global > struct Tree           7     4     6     Tree::right          -                        public, offset 8
(unnamed at 8:9)   struct_tag     struct (unnamed at 8:9)    -        global                         8     -     0     (unnamed at 8:9)     -                        size 36
(unnamed at 8:9)::items field          int[8]                     member   global > struct (unnamed at 8:9) 8     32    2     (unnamed at 8:9)::items -                        public, offset 0
(unnamed at 8:9)::top field          int                        member   global > struct (unnamed at 8:9) 8     4     4     (unnamed at 8:9)::top -                        public, offset 32
Stack              typedef        Stack                      -        global                         8     -     0     Stack                -                        
prepend            function       struct Node *(struct Node *, int) -        global                         10    -     1     _Z7prependP4Nodei    _Z7prependP4Nodei        defined
head               parameter      struct Node *              param    global > prepend()             10    4     1     head.1               -                        
v                  parameter      int                        param    global > prepend()             10    4     1     v.2                  -                        
n                  variable       struct Node *              local    global > prepend()             11    4     3     n.3                  -                        
reverse            function       struct Node *(struct Node *) -        global                         17    -     1     _Z7reverseP4Node     _Z7reverseP4Node         defined
head               parameter      struct Node *              param    global > reverse()             17    4     5     head.4               -                        
prev               variable       struct Node *              local    global > reverse()             18    4     3     prev.5               -                        
next               variable       struct Node *              local    global > reverse() > while     20    4     1     next.6               -                        
removeValue        function       void (struct Node **, int) -        global                         28    -     1     _Z11removeValuePP4Nodei _Z11removeValuePP4Nodei  defined
link               parameter      struct Node **             param    global > removeValue()         28    4     6     link.7               -                        
v                  parameter      int                        param    global > removeValue()         28    4     1     v.8                  -                        
dead               variable       struct Node *              local    global > removeValue() > while > if 30    4     2     dead.9               -                        
insert             function       struct Tree *(struct Tree *, int) -        global                         35    -     4     _Z6insertP4Treei     _Z6insertP4Treei         defined
t                  parameter      struct Tree *              param    global > insert()              35    4     11    t.10                 -                        
key                parameter      int                        param    global > insert()              35    4     4     key.11               -                        
inorder            function       void (struct Tree *)       -        global                         45    -     3     _Z7inorderP4Tree     _Z7inorderP4Tree         defined
t                  parameter      struct Tree *              param    global > inorder()             45    4     4     t.12                 -                        
height             function       int (struct Tree *)        -        global                         52    -     4     _Z6heightP4Tree      _Z6heightP4Tree          defined
t                  parameter      struct Tree *              param    global > height()              52    4     3     t.13                 -                        
l                  variable       int                        local    global > height()              54    4     2     l.14                 -                        
r                  variable       int                        local    global > height()              54    4     2     r.15                 -                        
push               function       void (Stack *, int)        -        global                         58    -     1     _Z4pushP5Stacki      _Z4pushP5Stacki          defined
s                  parameter      Stack *                    param    global > push()                58    4     2     s.16                 -                        
v                  parameter      int                        param    global > push()                58    4     1     v.17                 -                        
pop                function       int (Stack *)              -        global                         59    -     2     _Z3popP5Stack        _Z3popP5Stack            defined
s                  parameter      Stack *                    param    global > pop()                 59    4     2     s.18                 -                        
main               function       int (void)                 -        global                         61    -     0     main                 main                     defined
list               variable       struct Node *              local    global > main()                62    4     6     list.19              -                        
i                  variable       int                        local    global > main() > for          63    4     4     i.20                 -                        
p                  variable       struct Node *              local    global > main() > for          66    4     4     p.21                 -                        
root               variable       struct Tree *              local    global > main()                69    4     9     root.22              -                        
keys               variable       int[7]                     local    global > main()                70    28    1     keys.23              -                        
i                  variable       int                        local    global > main() > for          71    4     3     i.24                 -                        
s                  variable       Stack                      local    global > main()                76    36    5     s.25                 -                        
i                  variable       int                        local    global > main() > for          78    4     3     i.26                 -                        
a                  variable       int                        local    global > main()                79    4     1     a.27                 -                        
b                  variable       int                        local    global > main()                79    4     1     b.28                 -                        
rows               variable       int                        local    global > main()                82    4     4     rows.29              -                        
cols               variable       int                        local    global > main()                82    4     3     cols.30              -                        
table              variable       int **                     local    global > main()                83    4     5     table.31             -                        
r                  variable       int                        local    global > main() > for          84    4     5     r.32                 -                        
c                  variable       int                        local    global > main() > for > for body > for 86    4     4     c.33                 -                        
diagonal           variable       int                        local    global > main()                88    4     2     diagonal.34          -                        
r                  variable       int                        local    global > main() > for          89    4     4     r.35                 -                        
last               variable       int *                      local    global > main()                90    4     1     last.36              -                        
v1                 variable       int                        local    global > main()                93    4     2     v1.37                -                        
v2                 variable       int                        local    global > main()                93    4     2     v2.38                -                        
v3                 variable       int                        local    global > main()                93    4     2     v3.39                -                        
ptrs               variable       int *[3]                   local    global > main()                94    12    2     ptrs.40              -                        
pp                 variable       int **                     local    global > main()                95    4     2     pp.41                -                        

=== Record Layouts ===
struct Node: size 8, align 4
    +0  int value  [public]
    +4  struct Node * next  [public]
struct Tree: size 12, align 4
    +0  int key  [public]
    +4  struct Tree * left  [public]
    +8  struct Tree * right  [public]
struct (unnamed at 8:9): size 36, align 4
    +0  int[8] items  [public]
    +32  int top  [public]
