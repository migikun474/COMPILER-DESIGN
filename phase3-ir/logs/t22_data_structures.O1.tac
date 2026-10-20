=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t22_data_structures.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 321 -> 285 instruction(s) for 'test/t22_data_structures.c'.

optimization summary (-O1)
    instructions                321 -> 285   (11% fewer)
    constants folded            1
    algebraic simplifications   11
    common subexpressions       7
    copies / constants forwarded 29
    temporaries merged away     13
    dead instructions removed   8
    jumps removed or redirected 15
    unreachable instructions    0

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
 102:   n = t1
 103:   *t1 = v
 104:   t2 = t1 ptr+ 4
 105:   *t2 = head
 106:   return t1

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
 107:     prev = 0
 108: L1: if head ptr== 0 goto L2
 109:     t1 = head ptr+ 4
 110:     t2 = *t1
 111:     next = t2
 112:     *t1 = prev
 113:     prev = head
 114:     head = t2
 115:     goto L1
 116: L2: return prev

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
 117: L3: t1 = *link
 118:     if t1 ptr== 0 goto L5
 119:     t2 = *link
 120:     t3 = *t2
 121:     if t3 int!= v goto L4
 122:     t4 = *link
 123:     dead = t4
 124:     t5 = t4 ptr+ 4
 125:     t6 = *t5
 126:     *link = t6
 127:     param t4
 128:     call free, 1
 129:     goto L3
 130: L4: t7 = *link
 131:     link = t7 ptr+ 4
 132:     goto L3
 133: L5: return

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
 134:     if t ptr!= 0 goto L6
 135:     param 12
 136:     t1 = call malloc, 1
 137:     t = t1
 138:     *t1 = key
 139:     t2 = t1 ptr+ 8
 140:     *t2 = 0
 141:     t3 = t1 ptr+ 4
 142:     *t3 = 0
 143:     goto L8
 144: L6: t4 = *t
 145:     if key int>= t4 goto L7
 146:     t5 = t ptr+ 4
 147:     t6 = *t5
 148:     param t6
 149:     param key
 150:     t7 = call insert(struct Tree *, int), 2
 151:     *t5 = t7
 152:     goto L8
 153: L7: t9 = t ptr+ 8
 154:     t10 = *t9
 155:     param t10
 156:     param key
 157:     t11 = call insert(struct Tree *, int), 2
 158:     *t9 = t11
 159: L8: return t

function inorder(struct Tree *)        link name: _Z7inorderP4Tree
  symbol table (name, kind, type, width, offset)
    t              param  struct Tree *              4      0
    t1             temp   struct Tree *              4      4
    t2             temp   struct Tree *              4      8
    t3             temp   int                        4     12
    t4             temp   struct Tree *              4     16
    t5             temp   struct Tree *              4     20
    total width 24
  code
 160:     if t ptr!= 0 goto L9
 161:     return
 162: L9: t1 = t ptr+ 4
 163:     t2 = *t1
 164:     param t2
 165:     call inorder(struct Tree *), 1
 166:     t3 = *t
 167:     param "%d "
 168:     param t3
 169:     call printf, 2
 170:     t4 = t ptr+ 8
 171:     t5 = *t4
 172:     param t5
 173:     call inorder(struct Tree *), 1
 174:     return

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
 175:      if t ptr!= 0 goto L10
 176:      return 0
 177: L10: t1 = t ptr+ 4
 178:      t2 = *t1
 179:      param t2
 180:      t3 = call height(struct Tree *), 1
 181:      l = t3
 182:      t4 = t ptr+ 8
 183:      t5 = *t4
 184:      param t5
 185:      t6 = call height(struct Tree *), 1
 186:      r = t6
 187:      if t3 int<= t6 goto L11
 188:      t7 = l
 189:      goto L12
 190: L11: t7 = r
 191: L12: t8 = 1 int+ t7
 192:      return t8

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
 193:   t1 = s ptr+ 32
 194:   t2 = *t1
 195:   t3 = t2 int+ 1
 196:   *t1 = t3
 197:   t5 = t2 int<< 2                     (w = 4)
 198:   t6 = s ptr+ t5
 199:   *t6 = v
 200:   return

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
 201:   t1 = s ptr+ 32
 202:   t2 = *t1
 203:   t3 = t2 int- 1
 204:   *t1 = t3
 205:   t5 = t3 int<< 2                     (w = 4)
 206:   t6 = s ptr+ t5
 207:   t7 = *t6
 208:   return t7

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
    total width 484
  code
 209:      list = 0
 210:      i.20 = 1
 211: L13: if i.20 int> 6 goto L14
 212:      t1 = i.20 int* i.20
 213:      t2 = t1 int% 7
 214:      param list
 215:      param t2
 216:      list = call prepend(struct Node *, int), 2
 217:      i.20 = i.20 int+ 1
 218:      goto L13
 219: L14: param list
 220:      list = call reverse(struct Node *), 1
 221:      t6 = &list
 222:      param t6
 223:      param 2
 224:      call removeValue(struct Node **, int), 2
 225:      p = list
 226: L15: if p ptr== 0 goto L16
 227:      t7 = *p
 228:      param "%d "
 229:      param t7
 230:      call printf, 2
 231:      t8 = p ptr+ 4
 232:      p = *t8
 233:      goto L15
 234: L16: param "\n"
 235:      call printf, 1
 236:      root = 0
 237:      keys[0] = 50
 238:      keys[4] = 30
 239:      keys[8] = 70
 240:      keys[12] = 20
 241:      keys[16] = 40
 242:      keys[20] = 60
 243:      keys[24] = 80
 244:      i.24 = 0
 245: L17: if i.24 int>= 7 goto L18
 246:      t10 = i.24 int<< 2                  (w = 4)
 247:      t11 = keys[t10]
 248:      param root
 249:      param t11
 250:      root = call insert(struct Tree *, int), 2
 251:      i.24 = i.24 int+ 1
 252:      goto L17
 253: L18: param root
 254:      param 10
 255:      t14 = call insert(struct Tree *, int), 2
 256:      root = t14
 257:      param t14
 258:      call inorder(struct Tree *), 1
 259:      param t14
 260:      t15 = call height(struct Tree *), 1
 261:      t16 = t14 ptr+ 4
 262:      t17 = *t16
 263:      t18 = t17 ptr+ 4
 264:      t19 = *t18
 265:      t20 = t19 ptr+ 4
 266:      t21 = *t20
 267:      t22 = *t21
 268:      t23 = t14 ptr+ 8
 269:      t24 = *t23
 270:      t25 = t24 ptr+ 4
 271:      t26 = *t25
 272:      t27 = *t26
 273:      param "\n%d %d %d\n"
 274:      param t15
 275:      param t22
 276:      param t27
 277:      call printf, 4
 278:      s[32] = 0
 279:      i.26 = 0
 280: L19: if i.26 int>= 5 goto L20
 281:      t28 = &s
 282:      t29 = i.26 int* 3
 283:      param t28
 284:      param t29
 285:      call push(Stack *, int), 2
 286:      i.26 = i.26 int+ 1
 287:      goto L19
 288: L20: t31 = &s
 289:      param t31
 290:      t32 = call pop(Stack *), 1
 291:      a = t32
 292:      param t31
 293:      t34 = call pop(Stack *), 1
 294:      b = t34
 295:      t35 = s[32]
 296:      param "%d %d %d\n"
 297:      param t32
 298:      param t34
 299:      param t35
 300:      call printf, 4
 301:      rows = 3
 302:      cols = 4
 303:      param 12
 304:      table = call malloc, 1
 305:      r.32 = 0
 306: L21: if r.32 int>= rows goto L24
 307:      t38 = r.32 int<< 2
 308:      t39 = table ptr+ t38
 309:      t40 = cols uint<< 2
 310:      param t40
 311:      t41 = call malloc, 1
 312:      *t39 = t41
 313:      c = 0
 314: L22: if c int>= cols goto L23
 315:      t42 = r.32 int<< 2
 316:      t43 = table ptr+ t42
 317:      t44 = *t43
 318:      t45 = c int<< 2
 319:      t46 = t44 ptr+ t45
 320:      t47 = r.32 int* 10
 321:      t48 = t47 int+ c
 322:      *t46 = t48
 323:      c = c int+ 1
 324:      goto L22
 325: L23: r.32 = r.32 int+ 1
 326:      goto L21
 327: L24: diagonal = 0
 328:      r.35 = 0
 329: L25: if r.35 int>= rows goto L26
 330:      t51 = r.35 int<< 2
 331:      t52 = table ptr+ t51
 332:      t53 = *t52
 333:      t55 = t53 ptr+ t51
 334:      t56 = *t55
 335:      diagonal = diagonal int+ t56
 336:      r.35 = r.35 int+ 1
 337:      goto L25
 338: L26: t59 = rows int- 1
 339:      t60 = t59 int<< 2
 340:      t61 = table ptr+ t60
 341:      t62 = *t61
 342:      t63 = cols int<< 2
 343:      t64 = t62 ptr+ t63
 344:      t65 = t64 ptr- 4
 345:      last = t65
 346:      t66 = *t65
 347:      t67 = table ptr+ 4
 348:      t68 = *t67
 349:      t69 = t68 ptr+ 8
 350:      t70 = *t69
 351:      param "%d %d %d\n"
 352:      param diagonal
 353:      param t66
 354:      param t70
 355:      call printf, 4
 356:      v1 = 1
 357:      v2 = 2
 358:      v3 = 3
 359:      t71 = &v3
 360:      t72 = &v1
 361:      t73 = &v2
 362:      ptrs[0] = t71
 363:      ptrs[4] = t72
 364:      ptrs[8] = t73
 365:      t74 = &ptrs
 366:      pp = t74
 367:      t75 = *t74
 368:      *t75 = 30
 369:      t76 = ptrs[8]
 370:      t77 = *t76
 371:      t78 = t77 int+ 5
 372:      *t76 = t78
 373:      t79 = t74 ptr+ 4
 374:      t80 = *t79
 375:      t81 = *t80
 376:      param "%d %d %d %d\n"
 377:      param v1
 378:      param v2
 379:      param v3
 380:      param t81
 381:      call printf, 5
 382:      param root
 383:      t82 = call height(struct Tree *), 1
 384:      return t82


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
