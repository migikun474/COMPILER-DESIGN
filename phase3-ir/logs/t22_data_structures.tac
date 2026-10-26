============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t22_data_structures.c
   Optimization  : no optimization
   Result        : Three address code generated: 9 function(s), 321 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION prepend(struct Node *, int)        (link name _Z7prependP4Nodei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   head             param   struct Node *                   4       0
   v                param   int                             4       4
   n                local   struct Node *                   4       8
   t1               temp    void *                          4      12
   t2               temp    struct Node *                   4      16

 Code: 7 instruction(s)

    100     param 8
    101     t1 = call malloc, 1
    102     n = t1
    103     *n = v
    104     t2 = n ptr+ 4
    105     *t2 = head
    106     return n

============================================================================
 FUNCTION reverse(struct Node *)        (link name _Z7reverseP4Node)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 3 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   head             param   struct Node *                   4       0
   prev             local   struct Node *                   4       4
   next             local   struct Node *                   4       8
   t1               temp    struct Node *                   4      12
   t2               temp    struct Node *                   4      16
   t3               temp    struct Node *                   4      20

 Code: 12 instruction(s)

    107       prev = 0
    108  L1:  if head ptr!= 0 goto L2
    109       goto L3
    110  L2:  t1 = head ptr+ 4
    111       t2 = *t1
    112       next = t2
    113       t3 = head ptr+ 4
    114       *t3 = prev
    115       prev = head
    116       head = next
    117       goto L1
    118  L3:  return prev

============================================================================
 FUNCTION removeValue(struct Node **, int)        (link name _Z11removeValuePP4Nodei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   link             param   struct Node **                  4       0
   v                param   int                             4       4
   dead             local   struct Node *                   4       8
   t1               temp    struct Node *                   4      12
   t2               temp    struct Node *                   4      16
   t3               temp    int                             4      20
   t4               temp    struct Node *                   4      24
   t5               temp    struct Node *                   4      28
   t6               temp    struct Node *                   4      32
   t7               temp    struct Node *                   4      36
   t8               temp    struct Node *                   4      40

 Code: 20 instruction(s)

    119  L4:  t1 = *link
    120       if t1 ptr!= 0 goto L5
    121       goto L8
    122  L5:  t2 = *link
    123       t3 = *t2
    124       if t3 int== v goto L6
    125       goto L7
    126  L6:  t4 = *link
    127       dead = t4
    128       t5 = dead ptr+ 4
    129       t6 = *t5
    130       *link = t6
    131       param dead
    132       call free, 1
    133       goto L4
    134  L7:  t7 = *link
    135       t8 = t7 ptr+ 4
    136       link = t8
    137       goto L4
    138  L8:  return

============================================================================
 FUNCTION insert(struct Tree *, int)        (link name _Z6insertP4Treei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 12 temporaries, frame 56 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   struct Tree *                   4       0
   key              param   int                             4       4
   t1               temp    void *                          4       8
   t2               temp    struct Tree *                   4      12
   t3               temp    struct Tree *                   4      16
   t4               temp    int                             4      20
   t5               temp    struct Tree *                   4      24
   t6               temp    struct Tree *                   4      28
   t7               temp    struct Tree *                   4      32
   t8               temp    struct Tree *                   4      36
   t9               temp    struct Tree *                   4      40
   t10              temp    struct Tree *                   4      44
   t11              temp    struct Tree *                   4      48
   t12              temp    struct Tree *                   4      52

 Code: 30 instruction(s)

    139        if t ptr!= 0 goto L10
    140        goto L9
    141  L9:   param 12
    142        t1 = call malloc, 1
    143        t = t1
    144        *t = key
    145        t2 = t ptr+ 8
    146        *t2 = 0
    147        t3 = t ptr+ 4
    148        *t3 = 0
    149        goto L13
    150  L10:  t4 = *t
    151        if key int< t4 goto L11
    152        goto L12
    153  L11:  t5 = t ptr+ 4
    154        t6 = *t5
    155        param t6
    156        param key
    157        t7 = call insert(struct Tree *, int), 2
    158        t8 = t ptr+ 4
    159        *t8 = t7
    160        goto L13
    161  L12:  t9 = t ptr+ 8
    162        t10 = *t9
    163        param t10
    164        param key
    165        t11 = call insert(struct Tree *, int), 2
    166        t12 = t ptr+ 8
    167        *t12 = t11
    168  L13:  return t

============================================================================
 FUNCTION inorder(struct Tree *)        (link name _Z7inorderP4Tree)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   struct Tree *                   4       0
   t1               temp    struct Tree *                   4       4
   t2               temp    struct Tree *                   4       8
   t3               temp    int                             4      12
   t4               temp    struct Tree *                   4      16
   t5               temp    struct Tree *                   4      20

 Code: 16 instruction(s)

    169        if t ptr!= 0 goto L15
    170        goto L14
    171  L14:  return
    172  L15:  t1 = t ptr+ 4
    173        t2 = *t1
    174        param t2
    175        call inorder(struct Tree *), 1
    176        t3 = *t
    177        param "%d "
    178        param t3
    179        call printf, 2
    180        t4 = t ptr+ 8
    181        t5 = *t4
    182        param t5
    183        call inorder(struct Tree *), 1
    184        return

============================================================================
 FUNCTION height(struct Tree *)        (link name _Z6heightP4Tree)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   struct Tree *                   4       0
   l                local   int                             4       4
   r                local   int                             4       8
   t1               temp    struct Tree *                   4      12
   t2               temp    struct Tree *                   4      16
   t3               temp    int                             4      20
   t4               temp    struct Tree *                   4      24
   t5               temp    struct Tree *                   4      28
   t6               temp    int                             4      32
   t7               temp    int                             4      36
   t8               temp    int                             4      40

 Code: 20 instruction(s)

    185        if t ptr!= 0 goto L17
    186        goto L16
    187  L16:  return 0
    188  L17:  t1 = t ptr+ 4
    189        t2 = *t1
    190        param t2
    191        t3 = call height(struct Tree *), 1
    192        l = t3
    193        t4 = t ptr+ 8
    194        t5 = *t4
    195        param t5
    196        t6 = call height(struct Tree *), 1
    197        r = t6
    198        if l int> r goto L18
    199        goto L19
    200  L18:  t7 = l
    201        goto L20
    202  L19:  t7 = r
    203  L20:  t8 = 1 int+ t7
    204        return t8

============================================================================
 FUNCTION push(Stack *, int)        (link name _Z4pushP5Stacki)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   Stack *                         4       0
   v                param   int                             4       4
   t1               temp    Stack *                         4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    Stack *                         4      20
   t5               temp    int                             4      24
   t6               temp    Stack *                         4      28

 Code: 9 instruction(s)

    205     t1 = s ptr+ 32
    206     t2 = *t1
    207     t3 = t2 int+ 1
    208     t4 = s ptr+ 32
    209     *t4 = t3
    210     t5 = t2 int* 4                      (w = 4)
    211     t6 = s ptr+ t5
    212     *t6 = v
    213     return

============================================================================
 FUNCTION pop(Stack *)        (link name _Z3popP5Stack)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   Stack *                         4       0
   t1               temp    Stack *                         4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    Stack *                         4      16
   t5               temp    int                             4      20
   t6               temp    Stack *                         4      24
   t7               temp    int                             4      28

 Code: 9 instruction(s)

    214     t1 = s ptr+ 32
    215     t2 = *t1
    216     t3 = t2 int- 1
    217     t4 = s ptr+ 32
    218     *t4 = t3
    219     t5 = t3 int* 4                      (w = 4)
    220     t6 = s ptr+ t5
    221     t7 = *t6
    222     return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 23 parameter(s)/local(s), 82 temporaries, frame 484 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   list             local   struct Node *                   4       0
   i.20             local   int                             4       4
   p                local   struct Node *                   4       8
   root             local   struct Tree *                   4      12
   keys             local   int[7]                         28      16
   i.24             local   int                             4      44
   s                local   Stack                          36      48
   i.26             local   int                             4      84
   a                local   int                             4      88
   b                local   int                             4      92
   rows             local   int                             4      96
   cols             local   int                             4     100
   table            local   int **                          4     104
   r.32             local   int                             4     108
   c                local   int                             4     112
   diagonal         local   int                             4     116
   r.35             local   int                             4     120
   last             local   int *                           4     124
   v1               local   int                             4     128
   v2               local   int                             4     132
   v3               local   int                             4     136
   ptrs             local   int *[3]                       12     140
   pp               local   int **                          4     152
   t1               temp    int                             4     156
   t2               temp    int                             4     160
   t3               temp    struct Node *                   4     164
   t4               temp    int                             4     168
   t5               temp    struct Node *                   4     172
   t6               temp    struct Node **                  4     176
   t7               temp    int                             4     180
   t8               temp    struct Node *                   4     184
   t9               temp    struct Node *                   4     188
   t10              temp    int                             4     192
   t11              temp    int                             4     196
   t12              temp    struct Tree *                   4     200
   t13              temp    int                             4     204
   t14              temp    struct Tree *                   4     208
   t15              temp    int                             4     212
   t16              temp    struct Tree *                   4     216
   t17              temp    struct Tree *                   4     220
   t18              temp    struct Tree *                   4     224
   t19              temp    struct Tree *                   4     228
   t20              temp    struct Tree *                   4     232
   t21              temp    struct Tree *                   4     236
   t22              temp    int                             4     240
   t23              temp    struct Tree *                   4     244
   t24              temp    struct Tree *                   4     248
   t25              temp    struct Tree *                   4     252
   t26              temp    struct Tree *                   4     256
   t27              temp    int                             4     260
   t28              temp    Stack *                         4     264
   t29              temp    int                             4     268
   t30              temp    int                             4     272
   t31              temp    Stack *                         4     276
   t32              temp    int                             4     280
   t33              temp    Stack *                         4     284
   t34              temp    int                             4     288
   t35              temp    int                             4     292
   t36              temp    unsigned int                    4     296
   t37              temp    void *                          4     300
   t38              temp    int                             4     304
   t39              temp    int **                          4     308
   t40              temp    unsigned int                    4     312
   t41              temp    void *                          4     316
   t42              temp    int                             4     320
   t43              temp    int **                          4     324
   t44              temp    int *                           4     328
   t45              temp    int                             4     332
   t46              temp    int *                           4     336
   t47              temp    int                             4     340
   t48              temp    int                             4     344
   t49              temp    int                             4     348
   t50              temp    int                             4     352
   t51              temp    int                             4     356
   t52              temp    int **                          4     360
   t53              temp    int *                           4     364
   t54              temp    int                             4     368
   t55              temp    int *                           4     372
   t56              temp    int                             4     376
   t57              temp    int                             4     380
   t58              temp    int                             4     384
   t59              temp    int                             4     388
   t60              temp    int                             4     392
   t61              temp    int **                          4     396
   t62              temp    int *                           4     400
   t63              temp    int                             4     404
   t64              temp    int *                           4     408
   t65              temp    int *                           4     412
   t66              temp    int                             4     416
   t67              temp    int **                          4     420
   t68              temp    int *                           4     424
   t69              temp    int *                           4     428
   t70              temp    int                             4     432
   t71              temp    int *                           4     436
   t72              temp    int *                           4     440
   t73              temp    int *                           4     444
   t74              temp    int **                          4     448
   t75              temp    int *                           4     452
   t76              temp    int *                           4     456
   t77              temp    int                             4     460
   t78              temp    int                             4     464
   t79              temp    int **                          4     468
   t80              temp    int *                           4     472
   t81              temp    int                             4     476
   t82              temp    int                             4     480

 Code: 198 instruction(s)

    223        list = 0
    224        i.20 = 1
    225  L21:  if i.20 int<= 6 goto L22
    226        goto L23
    227  L22:  t1 = i.20 int* i.20
    228        t2 = t1 int% 7
    229        param list
    230        param t2
    231        t3 = call prepend(struct Node *, int), 2
    232        list = t3
    233        t4 = i.20 int+ 1
    234        i.20 = t4
    235        goto L21
    236  L23:  param list
    237        t5 = call reverse(struct Node *), 1
    238        list = t5
    239        t6 = &list
    240        param t6
    241        param 2
    242        call removeValue(struct Node **, int), 2
    243        p = list
    244  L24:  if p ptr!= 0 goto L25
    245        goto L26
    246  L25:  t7 = *p
    247        param "%d "
    248        param t7
    249        call printf, 2
    250        t8 = p ptr+ 4
    251        t9 = *t8
    252        p = t9
    253        goto L24
    254  L26:  param "\n"
    255        call printf, 1
    256        root = 0
    257        keys[0] = 50
    258        keys[4] = 30
    259        keys[8] = 70
    260        keys[12] = 20
    261        keys[16] = 40
    262        keys[20] = 60
    263        keys[24] = 80
    264        i.24 = 0
    265  L27:  if i.24 int< 7 goto L28
    266        goto L29
    267  L28:  t10 = i.24 int* 4                   (w = 4)
    268        t11 = keys[t10]
    269        param root
    270        param t11
    271        t12 = call insert(struct Tree *, int), 2
    272        root = t12
    273        t13 = i.24 int+ 1
    274        i.24 = t13
    275        goto L27
    276  L29:  param root
    277        param 10
    278        t14 = call insert(struct Tree *, int), 2
    279        root = t14
    280        param root
    281        call inorder(struct Tree *), 1
    282        param root
    283        t15 = call height(struct Tree *), 1
    284        t16 = root ptr+ 4
    285        t17 = *t16
    286        t18 = t17 ptr+ 4
    287        t19 = *t18
    288        t20 = t19 ptr+ 4
    289        t21 = *t20
    290        t22 = *t21
    291        t23 = root ptr+ 8
    292        t24 = *t23
    293        t25 = t24 ptr+ 4
    294        t26 = *t25
    295        t27 = *t26
    296        param "\n%d %d %d\n"
    297        param t15
    298        param t22
    299        param t27
    300        call printf, 4
    301        s[32] = 0
    302        i.26 = 0
    303  L30:  if i.26 int< 5 goto L31
    304        goto L32
    305  L31:  t28 = &s
    306        t29 = i.26 int* 3
    307        param t28
    308        param t29
    309        call push(Stack *, int), 2
    310        t30 = i.26 int+ 1
    311        i.26 = t30
    312        goto L30
    313  L32:  t31 = &s
    314        param t31
    315        t32 = call pop(Stack *), 1
    316        a = t32
    317        t33 = &s
    318        param t33
    319        t34 = call pop(Stack *), 1
    320        b = t34
    321        t35 = s[32]
    322        param "%d %d %d\n"
    323        param a
    324        param b
    325        param t35
    326        call printf, 4
    327        rows = 3
    328        cols = 4
    329        t36 = rows uint* 4
    330        param t36
    331        t37 = call malloc, 1
    332        table = t37
    333        r.32 = 0
    334  L33:  if r.32 int< rows goto L34
    335        goto L38
    336  L34:  t38 = r.32 int* 4
    337        t39 = table ptr+ t38
    338        t40 = cols uint* 4
    339        param t40
    340        t41 = call malloc, 1
    341        *t39 = t41
    342        c = 0
    343  L35:  if c int< cols goto L36
    344        goto L37
    345  L36:  t42 = r.32 int* 4
    346        t43 = table ptr+ t42
    347        t44 = *t43
    348        t45 = c int* 4
    349        t46 = t44 ptr+ t45
    350        t47 = r.32 int* 10
    351        t48 = t47 int+ c
    352        *t46 = t48
    353        t49 = c int+ 1
    354        c = t49
    355        goto L35
    356  L37:  t50 = r.32 int+ 1
    357        r.32 = t50
    358        goto L33
    359  L38:  diagonal = 0
    360        r.35 = 0
    361  L39:  if r.35 int< rows goto L40
    362        goto L41
    363  L40:  t51 = r.35 int* 4
    364        t52 = table ptr+ t51
    365        t53 = *t52
    366        t54 = r.35 int* 4
    367        t55 = t53 ptr+ t54
    368        t56 = *t55
    369        t57 = diagonal int+ t56
    370        diagonal = t57
    371        t58 = r.35 int+ 1
    372        r.35 = t58
    373        goto L39
    374  L41:  t59 = rows int- 1
    375        t60 = t59 int* 4
    376        t61 = table ptr+ t60
    377        t62 = *t61
    378        t63 = cols int* 4
    379        t64 = t62 ptr+ t63
    380        t65 = t64 ptr- 4
    381        last = t65
    382        t66 = *last
    383        t67 = table ptr+ 4
    384        t68 = *t67
    385        t69 = t68 ptr+ 8
    386        t70 = *t69
    387        param "%d %d %d\n"
    388        param diagonal
    389        param t66
    390        param t70
    391        call printf, 4
    392        v1 = 1
    393        v2 = 2
    394        v3 = 3
    395        t71 = &v3
    396        t72 = &v1
    397        t73 = &v2
    398        ptrs[0] = t71
    399        ptrs[4] = t72
    400        ptrs[8] = t73
    401        t74 = &ptrs
    402        pp = t74
    403        t75 = *pp
    404        *t75 = 30
    405        t76 = ptrs[8]
    406        t77 = *t76
    407        t78 = t77 int+ 5
    408        *t76 = t78
    409        t79 = pp ptr+ 4
    410        t80 = *t79
    411        t81 = *t80
    412        param "%d %d %d %d\n"
    413        param v1
    414        param v2
    415        param v3
    416        param t81
    417        call printf, 5
    418        param root
    419        t82 = call height(struct Tree *), 1
    420        return t82


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Node               struct_tag    struct Node                -           6    -    0  size 8
   Tree               struct_tag    struct Tree                -           7    -    0  size 12
   (unnamed at 8:9)   struct_tag    struct (unnamed at 8:9)    -           8    -    0  size 36
   Stack              typedef       Stack                      -           8    -    0  
   prepend            function      struct Node *(struct Node *, int) -          10    -    1  _Z7prependP4Nodei; defined
   reverse            function      struct Node *(struct Node *) -          17    -    1  _Z7reverseP4Node; defined
   removeValue        function      void (struct Node **, int) -          28    -    1  _Z11removeValuePP4Nodei; defined
   insert             function      struct Tree *(struct Tree *, int) -          35    -    4  _Z6insertP4Treei; defined
   inorder            function      void (struct Tree *)       -          45    -    3  _Z7inorderP4Tree; defined
   height             function      int (struct Tree *)        -          52    -    4  _Z6heightP4Tree; defined
   push               function      void (Stack *, int)        -          58    -    1  _Z4pushP5Stacki; defined
   pop                function      int (Stack *)              -          59    -    2  _Z3popP5Stack; defined
   main               function      int (void)                 -          61    -    0  defined

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   value              field         int                        member      6    4    3  Node::value; public, offset 0
   next               field         struct Node *              member      6    4    6  Node::next; public, offset 4

 scope: global > struct Tree
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   key                field         int                        member      7    4    5  Tree::key; public, offset 0
   left               field         struct Tree *              member      7    4    9  Tree::left; public, offset 4
   right              field         struct Tree *              member      7    4    6  Tree::right; public, offset 8

 scope: global > struct (unnamed at 8:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   items              field         int[8]                     member      8   32    2  (unnamed at 8:9)::items; public, offset 0
   top                field         int                        member      8    4    4  (unnamed at 8:9)::top; public, offset 32

 scope: global > prepend()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param      10    4    1  head.1
   v                  parameter     int                        param      10    4    1  v.2
   n                  variable      struct Node *              local      11    4    3  n.3

 scope: global > reverse()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param      17    4    5  head.4
   prev               variable      struct Node *              local      18    4    3  prev.5

 scope: global > reverse() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   next               variable      struct Node *              local      20    4    1  next.6

 scope: global > removeValue()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   link               parameter     struct Node **             param      28    4    6  link.7
   v                  parameter     int                        param      28    4    1  v.8

 scope: global > removeValue() > while > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   dead               variable      struct Node *              local      30    4    2  dead.9

 scope: global > insert()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     struct Tree *              param      35    4   11  t.10
   key                parameter     int                        param      35    4    4  key.11

 scope: global > inorder()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     struct Tree *              param      45    4    4  t.12

 scope: global > height()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     struct Tree *              param      52    4    3  t.13
   l                  variable      int                        local      54    4    2  l.14
   r                  variable      int                        local      54    4    2  r.15

 scope: global > push()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     Stack *                    param      58    4    2  s.16
   v                  parameter     int                        param      58    4    1  v.17

 scope: global > pop()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     Stack *                    param      59    4    2  s.18

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   list               variable      struct Node *              local      62    4    6  list.19
   root               variable      struct Tree *              local      69    4    9  root.22
   keys               variable      int[7]                     local      70   28    1  keys.23
   s                  variable      Stack                      local      76   36    5  s.25
   a                  variable      int                        local      79    4    1  a.27
   b                  variable      int                        local      79    4    1  b.28
   rows               variable      int                        local      82    4    4  rows.29
   cols               variable      int                        local      82    4    3  cols.30
   table              variable      int **                     local      83    4    5  table.31
   diagonal           variable      int                        local      88    4    2  diagonal.34
   last               variable      int *                      local      90    4    1  last.36
   v1                 variable      int                        local      93    4    2  v1.37
   v2                 variable      int                        local      93    4    2  v2.38
   v3                 variable      int                        local      93    4    2  v3.39
   ptrs               variable      int *[3]                   local      94   12    2  ptrs.40
   pp                 variable      int **                     local      95    4    2  pp.41

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      63    4    4  i.20
   p                  variable      struct Node *              local      66    4    4  p.21
   i                  variable      int                        local      71    4    3  i.24
   i                  variable      int                        local      78    4    3  i.26
   r                  variable      int                        local      84    4    5  r.32
   r                  variable      int                        local      89    4    4  r.35

 scope: global > main() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        local      86    4    4  c.33

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

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
