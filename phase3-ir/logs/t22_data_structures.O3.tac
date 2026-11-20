============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t22_data_structures.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 321 -> 303 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          321 -> 303   (5% fewer)

   constants folded                        5
   algebraic simplifications              11
   common subexpressions                   9
   copies / constants forwarded           47
   temporaries merged away                15
   dead instructions removed              22
   jumps removed or redirected            15
   unreachable instructions removed        1
   propagated across blocks               10
   dead assignments removed               13
   calls inlined                           6
   tail calls turned into jumps            1
   common subexpressions across blocks      0

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

 Code: 6 instruction(s)

    100     param 8
    101     t1 = call malloc, 1
    102     *t1 = v
    103     t2 = t1 ptr+ 4
    104     *t2 = head
    105     return t1

============================================================================
 FUNCTION reverse(struct Node *)        (link name _Z7reverseP4Node)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   head             param   struct Node *                   4       0
   prev             local   struct Node *                   4       4
   next             local   struct Node *                   4       8
   t1               temp    struct Node *                   4      12
   t2               temp    struct Node *                   4      16
   (1 temporary no longer used after optimization not shown)

 Code: 9 instruction(s)

    106       prev = 0
    107  L1:  if head ptr== 0 goto L2
    108       t1 = head ptr+ 4
    109       t2 = *t1
    110       *t1 = prev
    111       prev = head
    112       head = t2
    113       goto L1
    114  L2:  return prev

============================================================================
 FUNCTION removeValue(struct Node **, int)        (link name _Z11removeValuePP4Nodei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 7 temporaries, frame 44 bytes

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
   (1 temporary no longer used after optimization not shown)

 Code: 16 instruction(s)

    115  L3:  t1 = *link
    116       if t1 ptr== 0 goto L5
    117       t2 = *link
    118       t3 = *t2
    119       if t3 int!= v goto L4
    120       t4 = *link
    121       t5 = t4 ptr+ 4
    122       t6 = *t5
    123       *link = t6
    124       param t4
    125       call free, 1
    126       goto L3
    127  L4:  t7 = *link
    128       link = t7 ptr+ 4
    129       goto L3
    130  L5:  return

============================================================================
 FUNCTION insert(struct Tree *, int)        (link name _Z6insertP4Treei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 10 temporaries, frame 56 bytes

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
   t9               temp    struct Tree *                   4      40
   t10              temp    struct Tree *                   4      44
   t11              temp    struct Tree *                   4      48
   (2 temporaries no longer used after optimization not shown)

 Code: 26 instruction(s)

    131       if t ptr!= 0 goto L6
    132       param 12
    133       t1 = call malloc, 1
    134       t = t1
    135       *t1 = key
    136       t2 = t1 ptr+ 8
    137       *t2 = 0
    138       t3 = t1 ptr+ 4
    139       *t3 = 0
    140       goto L8
    141  L6:  t4 = *t
    142       if key int>= t4 goto L7
    143       t5 = t ptr+ 4
    144       t6 = *t5
    145       param t6
    146       param key
    147       t7 = call insert(struct Tree *, int), 2
    148       *t5 = t7
    149       goto L8
    150  L7:  t9 = t ptr+ 8
    151       t10 = *t9
    152       param t10
    153       param key
    154       t11 = call insert(struct Tree *, int), 2
    155       *t9 = t11
    156  L8:  return t

============================================================================
 FUNCTION inorder(struct Tree *)        (link name _Z7inorderP4Tree)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   struct Tree *                   4       0
   t1               temp    struct Tree *                   4       4
   t2               temp    struct Tree *                   4       8
   t3               temp    int                             4      12
   t4               temp    struct Tree *                   4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    157  L9:   if t ptr!= 0 goto L10
    158        return
    159  L10:  t1 = t ptr+ 4
    160        t2 = *t1
    161        param t2
    162        call inorder(struct Tree *), 1
    163        t3 = *t
    164        param "%d "
    165        param t3
    166        call printf, 2
    167        t4 = t ptr+ 8
    168        t = *t4
    169        goto L9

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

 Code: 16 instruction(s)

    170        if t ptr!= 0 goto L11
    171        return 0
    172  L11:  t1 = t ptr+ 4
    173        t2 = *t1
    174        param t2
    175        t3 = call height(struct Tree *), 1
    176        t4 = t ptr+ 8
    177        t5 = *t4
    178        param t5
    179        t6 = call height(struct Tree *), 1
    180        if t3 int<= t6 goto L12
    181        t7 = t3
    182        goto L13
    183  L12:  t7 = t6
    184  L13:  t8 = 1 int+ t7
    185        return t8

============================================================================
 FUNCTION push(Stack *, int)        (link name _Z4pushP5Stacki)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   Stack *                         4       0
   v                param   int                             4       4
   t1               temp    Stack *                         4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t5               temp    int                             4      24
   t6               temp    Stack *                         4      28
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    186     t1 = s ptr+ 32
    187     t2 = *t1
    188     t3 = t2 int+ 1
    189     *t1 = t3
    190     t5 = t2 int<< 2                     (w = 4)
    191     t6 = s ptr+ t5
    192     *t6 = v
    193     return

============================================================================
 FUNCTION pop(Stack *)        (link name _Z3popP5Stack)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 6 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                param   Stack *                         4       0
   t1               temp    Stack *                         4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t5               temp    int                             4      20
   t6               temp    Stack *                         4      24
   t7               temp    int                             4      28
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    194     t1 = s ptr+ 32
    195     t2 = *t1
    196     t3 = t2 int- 1
    197     *t1 = t3
    198     t5 = t3 int<< 2                     (w = 4)
    199     t6 = s ptr+ t5
    200     t7 = *t6
    201     return t7

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 23 parameter(s)/local(s), 90 temporaries, frame 636 bytes

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
   t7               temp    int                             4     180
   t8               temp    struct Node *                   4     184
   t10              temp    int                             4     192
   t11              temp    int                             4     196
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
   t31              temp    Stack *                         4     276
   t35              temp    int                             4     292
   t38              temp    int                             4     304
   t39              temp    int **                          4     308
   t41              temp    void *                          4     316
   t42              temp    int                             4     320
   t43              temp    int **                          4     324
   t44              temp    int *                           4     328
   t45              temp    int                             4     332
   t46              temp    int *                           4     336
   t47              temp    int                             4     340
   t48              temp    int                             4     344
   t51              temp    int                             4     356
   t52              temp    int **                          4     360
   t53              temp    int *                           4     364
   t55              temp    int *                           4     372
   t56              temp    int                             4     376
   t61              temp    int **                          4     396
   t62              temp    int *                           4     400
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
   t83              temp    struct Node *                   4     484
   t85              temp    void *                          4     492
   t86              temp    struct Node *                   4     496
   t87              temp    struct Node *                   4     500
   t88              temp    struct Node *                   4     504
   t89              temp    struct Node *                   4     508
   t90              temp    struct Node *                   4     512
   t91              temp    struct Node **                  4     516
   t93              temp    struct Node *                   4     524
   t94              temp    struct Node *                   4     528
   t95              temp    int                             4     532
   t96              temp    struct Node *                   4     536
   t97              temp    struct Node *                   4     540
   t98              temp    struct Node *                   4     544
   t99              temp    struct Node *                   4     548
   t102             temp    Stack *                         4     560
   t103             temp    int                             4     564
   t104             temp    int                             4     568
   t105             temp    int                             4     572
   t106             temp    Stack *                         4     576
   t108             temp    Stack *                         4     584
   t109             temp    int                             4     588
   t110             temp    int                             4     592
   t111             temp    int                             4     596
   t112             temp    Stack *                         4     600
   t113             temp    int                             4     604
   t117             temp    int                             4     620
   t118             temp    int                             4     624
   t119             temp    Stack *                         4     628
   t120             temp    int                             4     632
   (30 temporaries no longer used after optimization not shown)

 Code: 201 instruction(s)

    202        list = 0
    203        i.20 = 1
    204  L14:  if i.20 int> 6 goto L15
    205        t1 = i.20 int* i.20
    206        t2 = t1 int% 7
    207        t83 = list
    208        param 8
    209        t85 = call malloc, 1
    210        *t85 = t2
    211        t86 = t85 ptr+ 4
    212        *t86 = t83
    213        list = t85
    214        i.20 = i.20 int+ 1
    215        goto L14
    216  L15:  t87 = list
    217        t88 = 0
    218  L16:  if t87 ptr== 0 goto L17
    219        t89 = t87 ptr+ 4
    220        t90 = *t89
    221        *t89 = t88
    222        t88 = t87
    223        t87 = t90
    224        goto L16
    225  L17:  list = t88
    226        t91 = &list
    227  L18:  t93 = *t91
    228        if t93 ptr== 0 goto L20
    229        t94 = *t91
    230        t95 = *t94
    231        if t95 int!= 2 goto L19
    232        t96 = *t91
    233        t97 = t96 ptr+ 4
    234        t98 = *t97
    235        *t91 = t98
    236        param t96
    237        call free, 1
    238        goto L18
    239  L19:  t99 = *t91
    240        t91 = t99 ptr+ 4
    241        goto L18
    242  L20:  p = list
    243  L21:  if p ptr== 0 goto L22
    244        t7 = *p
    245        param "%d "
    246        param t7
    247        call printf, 2
    248        t8 = p ptr+ 4
    249        p = *t8
    250        goto L21
    251  L22:  param "\n"
    252        call printf, 1
    253        root = 0
    254        keys[0] = 50
    255        keys[4] = 30
    256        keys[8] = 70
    257        keys[12] = 20
    258        keys[16] = 40
    259        keys[20] = 60
    260        keys[24] = 80
    261        i.24 = 0
    262  L23:  if i.24 int>= 7 goto L24
    263        t10 = i.24 int<< 2                  (w = 4)
    264        t11 = keys[t10]
    265        param root
    266        param t11
    267        root = call insert(struct Tree *, int), 2
    268        i.24 = i.24 int+ 1
    269        goto L23
    270  L24:  param root
    271        param 10
    272        t14 = call insert(struct Tree *, int), 2
    273        param t14
    274        call inorder(struct Tree *), 1
    275        param t14
    276        t15 = call height(struct Tree *), 1
    277        t16 = t14 ptr+ 4
    278        t17 = *t16
    279        t18 = t17 ptr+ 4
    280        t19 = *t18
    281        t20 = t19 ptr+ 4
    282        t21 = *t20
    283        t22 = *t21
    284        t23 = t14 ptr+ 8
    285        t24 = *t23
    286        t25 = t24 ptr+ 4
    287        t26 = *t25
    288        t27 = *t26
    289        param "\n%d %d %d\n"
    290        param t15
    291        param t22
    292        param t27
    293        call printf, 4
    294        s[32] = 0
    295        i.26 = 0
    296  L25:  if i.26 int>= 5 goto L26
    297        t28 = &s
    298        t29 = i.26 int* 3
    299        t102 = t28 ptr+ 32
    300        t103 = *t102
    301        t104 = t103 int+ 1
    302        *t102 = t104
    303        t105 = t103 int<< 2                 (w = 4)
    304        t106 = t28 ptr+ t105
    305        *t106 = t29
    306        i.26 = i.26 int+ 1
    307        goto L25
    308  L26:  t31 = &s
    309        t108 = t31 ptr+ 32
    310        t109 = *t108
    311        t110 = t109 int- 1
    312        *t108 = t110
    313        t111 = t110 int<< 2                 (w = 4)
    314        t112 = t31 ptr+ t111
    315        t113 = *t112
    316        t117 = t110 int- 1
    317        *t108 = t117
    318        t118 = t117 int<< 2                 (w = 4)
    319        t119 = t31 ptr+ t118
    320        t120 = *t119
    321        t35 = s[32]
    322        param "%d %d %d\n"
    323        param t113
    324        param t120
    325        param t35
    326        call printf, 4
    327        param 12
    328        table = call malloc, 1
    329        r.32 = 0
    330  L27:  if r.32 int>= 3 goto L30
    331        t38 = r.32 int<< 2
    332        t39 = table ptr+ t38
    333        param 16
    334        t41 = call malloc, 1
    335        *t39 = t41
    336        c = 0
    337  L28:  if c int>= 4 goto L29
    338        t42 = r.32 int<< 2
    339        t43 = table ptr+ t42
    340        t44 = *t43
    341        t45 = c int<< 2
    342        t46 = t44 ptr+ t45
    343        t47 = r.32 int* 10
    344        t48 = t47 int+ c
    345        *t46 = t48
    346        c = c int+ 1
    347        goto L28
    348  L29:  r.32 = r.32 int+ 1
    349        goto L27
    350  L30:  diagonal = 0
    351        r.35 = 0
    352  L31:  if r.35 int>= 3 goto L32
    353        t51 = r.35 int<< 2
    354        t52 = table ptr+ t51
    355        t53 = *t52
    356        t55 = t53 ptr+ t51
    357        t56 = *t55
    358        diagonal = diagonal int+ t56
    359        r.35 = r.35 int+ 1
    360        goto L31
    361  L32:  t61 = table ptr+ 8
    362        t62 = *t61
    363        t64 = t62 ptr+ 16
    364        t65 = t64 ptr- 4
    365        t66 = *t65
    366        t67 = table ptr+ 4
    367        t68 = *t67
    368        t69 = t68 ptr+ 8
    369        t70 = *t69
    370        param "%d %d %d\n"
    371        param diagonal
    372        param t66
    373        param t70
    374        call printf, 4
    375        v1 = 1
    376        v2 = 2
    377        v3 = 3
    378        t71 = &v3
    379        t72 = &v1
    380        t73 = &v2
    381        ptrs[0] = t71
    382        ptrs[4] = t72
    383        ptrs[8] = t73
    384        t74 = &ptrs
    385        t75 = *t74
    386        *t75 = 30
    387        t76 = ptrs[8]
    388        t77 = *t76
    389        t78 = t77 int+ 5
    390        *t76 = t78
    391        t79 = t74 ptr+ 4
    392        t80 = *t79
    393        t81 = *t80
    394        param "%d %d %d %d\n"
    395        param v1
    396        param v2
    397        param v3
    398        param t81
    399        call printf, 5
    400        param t14
    401        t82 = call height(struct Tree *), 1
    402        return t82


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Node               struct_tag    struct Node                -           4    -    0  size 8
   Tree               struct_tag    struct Tree                -           5    -    0  size 12
   (unnamed at 6:9)   struct_tag    struct (unnamed at 6:9)    -           6    -    0  size 36
   Stack              typedef       Stack                      -           6    -    0  
   prepend            function      struct Node *(struct Node *, int) -           8    -    1  _Z7prependP4Nodei; defined
   reverse            function      struct Node *(struct Node *) -          15    -    1  _Z7reverseP4Node; defined
   removeValue        function      void (struct Node **, int) -          26    -    1  _Z11removeValuePP4Nodei; defined
   insert             function      struct Tree *(struct Tree *, int) -          33    -    4  _Z6insertP4Treei; defined
   inorder            function      void (struct Tree *)       -          43    -    3  _Z7inorderP4Tree; defined
   height             function      int (struct Tree *)        -          50    -    4  _Z6heightP4Tree; defined
   push               function      void (Stack *, int)        -          56    -    1  _Z4pushP5Stacki; defined
   pop                function      int (Stack *)              -          57    -    2  _Z3popP5Stack; defined
   main               function      int (void)                 -          59    -    0  defined

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   value              field         int                        member      4    4    3  Node::value; public, offset 0
   next               field         struct Node *              member      4    4    6  Node::next; public, offset 4

 scope: global > struct Tree
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   key                field         int                        member      5    4    5  Tree::key; public, offset 0
   left               field         struct Tree *              member      5    4    9  Tree::left; public, offset 4
   right              field         struct Tree *              member      5    4    6  Tree::right; public, offset 8

 scope: global > struct (unnamed at 6:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   items              field         int[8]                     member      6   32    2  (unnamed at 6:9)::items; public, offset 0
   top                field         int                        member      6    4    4  (unnamed at 6:9)::top; public, offset 32

 scope: global > prepend()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param       8    4    1  head.1
   v                  parameter     int                        param       8    4    1  v.2
   n                  variable      struct Node *              local       9    4    3  n.3

 scope: global > reverse()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param      15    4    5  head.4
   prev               variable      struct Node *              local      16    4    3  prev.5

 scope: global > reverse() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   next               variable      struct Node *              local      18    4    1  next.6

 scope: global > removeValue()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   link               parameter     struct Node **             param      26    4    6  link.7
   v                  parameter     int                        param      26    4    1  v.8

 scope: global > removeValue() > while > if
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   dead               variable      struct Node *              local      28    4    2  dead.9

 scope: global > insert()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     struct Tree *              param      33    4   11  t.10
   key                parameter     int                        param      33    4    4  key.11

 scope: global > inorder()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     struct Tree *              param      43    4    4  t.12

 scope: global > height()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     struct Tree *              param      50    4    3  t.13
   l                  variable      int                        local      52    4    2  l.14
   r                  variable      int                        local      52    4    2  r.15

 scope: global > push()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     Stack *                    param      56    4    2  s.16
   v                  parameter     int                        param      56    4    1  v.17

 scope: global > pop()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     Stack *                    param      57    4    2  s.18

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   list               variable      struct Node *              local      60    4    6  list.19
   root               variable      struct Tree *              local      67    4    9  root.22
   keys               variable      int[7]                     local      68   28    1  keys.23
   s                  variable      Stack                      local      74   36    5  s.25
   a                  variable      int                        local      77    4    1  a.27
   b                  variable      int                        local      77    4    1  b.28
   rows               variable      int                        local      80    4    4  rows.29
   cols               variable      int                        local      80    4    3  cols.30
   table              variable      int **                     local      81    4    5  table.31
   diagonal           variable      int                        local      86    4    2  diagonal.34
   last               variable      int *                      local      88    4    1  last.36
   v1                 variable      int                        local      91    4    2  v1.37
   v2                 variable      int                        local      91    4    2  v2.38
   v3                 variable      int                        local      91    4    2  v3.39
   ptrs               variable      int *[3]                   local      92   12    2  ptrs.40
   pp                 variable      int **                     local      93    4    2  pp.41

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      61    4    4  i.20
   p                  variable      struct Node *              local      64    4    4  p.21
   i                  variable      int                        local      69    4    3  i.24
   i                  variable      int                        local      76    4    3  i.26
   r                  variable      int                        local      82    4    5  r.32
   r                  variable      int                        local      87    4    4  r.35

 scope: global > main() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  variable      int                        local      84    4    4  c.33

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
struct (unnamed at 6:9): size 36, align 4
    +0  int[8] items  [public]
    +32  int top  [public]
