============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t22_data_structures.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 321 -> 330 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          321 -> 330   (-2% fewer)

   constants folded                        5
   algebraic simplifications              11
   common subexpressions                   9
   copies / constants forwarded           49
   temporaries merged away                15
   dead instructions removed              22
   jumps removed or redirected            15
   unreachable instructions removed        1
   propagated across blocks               10
   dead assignments removed               13
   calls inlined                           6
   tail calls turned into jumps            1
   common subexpressions across blocks      0
   loops unrolled                         10
   unreachable functions removed           5

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

    100       if t ptr!= 0 goto L1
    101       param 12
    102       t1 = call malloc, 1
    103       t = t1
    104       *t1 = key
    105       t2 = t1 ptr+ 8
    106       *t2 = 0
    107       t3 = t1 ptr+ 4
    108       *t3 = 0
    109       goto L3
    110  L1:  t4 = *t
    111       if key int>= t4 goto L2
    112       t5 = t ptr+ 4
    113       t6 = *t5
    114       param t6
    115       param key
    116       t7 = call insert(struct Tree *, int), 2
    117       *t5 = t7
    118       goto L3
    119  L2:  t9 = t ptr+ 8
    120       t10 = *t9
    121       param t10
    122       param key
    123       t11 = call insert(struct Tree *, int), 2
    124       *t9 = t11
    125  L3:  return t

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

    126  L4:  if t ptr!= 0 goto L5
    127       return
    128  L5:  t1 = t ptr+ 4
    129       t2 = *t1
    130       param t2
    131       call inorder(struct Tree *), 1
    132       t3 = *t
    133       param "%d "
    134       param t3
    135       call printf, 2
    136       t4 = t ptr+ 8
    137       t = *t4
    138       goto L4

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

    139       if t ptr!= 0 goto L6
    140       return 0
    141  L6:  t1 = t ptr+ 4
    142       t2 = *t1
    143       param t2
    144       t3 = call height(struct Tree *), 1
    145       t4 = t ptr+ 8
    146       t5 = *t4
    147       param t5
    148       t6 = call height(struct Tree *), 1
    149       if t3 int<= t6 goto L7
    150       t7 = t3
    151       goto L8
    152  L7:  t7 = t6
    153  L8:  t8 = 1 int+ t7
    154       return t8

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

 Code: 275 instruction(s)

    155        list = 0
    156        i.20 = 1
    157  L9:   if i.20 int> 6 goto L10
    158        t1 = i.20 int* i.20
    159        t2 = t1 int% 7
    160        t83 = list
    161        param 8
    162        t85 = call malloc, 1
    163        *t85 = t2
    164        t86 = t85 ptr+ 4
    165        *t86 = t83
    166        list = t85
    167        i.20 = i.20 int+ 1
    168        if i.20 int> 6 goto L10
    169        t1 = i.20 int* i.20
    170        t2 = t1 int% 7
    171        t83 = list
    172        param 8
    173        t85 = call malloc, 1
    174        *t85 = t2
    175        t86 = t85 ptr+ 4
    176        *t86 = t83
    177        list = t85
    178        i.20 = i.20 int+ 1
    179        goto L9
    180  L10:  t87 = list
    181        t88 = 0
    182  L11:  if t87 ptr== 0 goto L12
    183        t89 = t87 ptr+ 4
    184        t90 = *t89
    185        *t89 = t88
    186        t88 = t87
    187        t87 = t90
    188        if t90 ptr== 0 goto L12
    189        t89 = t87 ptr+ 4
    190        t90 = *t89
    191        *t89 = t88
    192        t88 = t87
    193        t87 = t90
    194        goto L11
    195  L12:  list = t88
    196        t91 = &list
    197  L13:  t93 = *t91
    198        if t93 ptr== 0 goto L17
    199        t94 = *t91
    200        t95 = *t94
    201        if t95 int!= 2 goto L14
    202        t96 = *t91
    203        t97 = t96 ptr+ 4
    204        t98 = *t97
    205        *t91 = t98
    206        param t96
    207        call free, 1
    208        goto L13
    209  L14:  t99 = *t91
    210        t91 = t99 ptr+ 4
    211  L15:  t93 = *t91
    212        if t93 ptr== 0 goto L17
    213        t94 = *t91
    214        t95 = *t94
    215        if t95 int!= 2 goto L16
    216        t96 = *t91
    217        t97 = t96 ptr+ 4
    218        t98 = *t97
    219        *t91 = t98
    220        param t96
    221        call free, 1
    222        goto L15
    223  L16:  t99 = *t91
    224        t91 = t99 ptr+ 4
    225        goto L13
    226  L17:  p = list
    227  L18:  if p ptr== 0 goto L19
    228        t7 = *p
    229        param "%d "
    230        param t7
    231        call printf, 2
    232        t8 = p ptr+ 4
    233        p = *t8
    234        if p ptr== 0 goto L19
    235        t7 = *p
    236        param "%d "
    237        param t7
    238        call printf, 2
    239        t8 = p ptr+ 4
    240        p = *t8
    241        goto L18
    242  L19:  param "\n"
    243        call printf, 1
    244        root = 0
    245        keys[0] = 50
    246        keys[4] = 30
    247        keys[8] = 70
    248        keys[12] = 20
    249        keys[16] = 40
    250        keys[20] = 60
    251        keys[24] = 80
    252        i.24 = 0
    253  L20:  if i.24 int>= 7 goto L21
    254        t10 = i.24 int<< 2                  (w = 4)
    255        t11 = keys[t10]
    256        param root
    257        param t11
    258        root = call insert(struct Tree *, int), 2
    259        i.24 = i.24 int+ 1
    260        if i.24 int>= 7 goto L21
    261        t10 = i.24 int<< 2                  (w = 4)
    262        t11 = keys[t10]
    263        param root
    264        param t11
    265        root = call insert(struct Tree *, int), 2
    266        i.24 = i.24 int+ 1
    267        goto L20
    268  L21:  param root
    269        param 10
    270        t14 = call insert(struct Tree *, int), 2
    271        param t14
    272        call inorder(struct Tree *), 1
    273        param t14
    274        t15 = call height(struct Tree *), 1
    275        t16 = t14 ptr+ 4
    276        t17 = *t16
    277        t18 = t17 ptr+ 4
    278        t19 = *t18
    279        t20 = t19 ptr+ 4
    280        t21 = *t20
    281        t22 = *t21
    282        t23 = t14 ptr+ 8
    283        t24 = *t23
    284        t25 = t24 ptr+ 4
    285        t26 = *t25
    286        t27 = *t26
    287        param "\n%d %d %d\n"
    288        param t15
    289        param t22
    290        param t27
    291        call printf, 4
    292        s[32] = 0
    293        i.26 = 0
    294  L22:  if i.26 int>= 5 goto L23
    295        t28 = &s
    296        t29 = i.26 int* 3
    297        t102 = t28 ptr+ 32
    298        t103 = *t102
    299        t104 = t103 int+ 1
    300        *t102 = t104
    301        t105 = t103 int<< 2                 (w = 4)
    302        t106 = t28 ptr+ t105
    303        *t106 = t29
    304        i.26 = i.26 int+ 1
    305        if i.26 int>= 5 goto L23
    306        t28 = &s
    307        t29 = i.26 int* 3
    308        t102 = t28 ptr+ 32
    309        t103 = *t102
    310        t104 = t103 int+ 1
    311        *t102 = t104
    312        t105 = t103 int<< 2                 (w = 4)
    313        t106 = t28 ptr+ t105
    314        *t106 = t29
    315        i.26 = i.26 int+ 1
    316        goto L22
    317  L23:  t31 = &s
    318        t108 = t31 ptr+ 32
    319        t109 = *t108
    320        t110 = t109 int- 1
    321        *t108 = t110
    322        t111 = t110 int<< 2                 (w = 4)
    323        t112 = t31 ptr+ t111
    324        t113 = *t112
    325        t117 = t110 int- 1
    326        *t108 = t117
    327        t118 = t117 int<< 2                 (w = 4)
    328        t119 = t31 ptr+ t118
    329        t120 = *t119
    330        t35 = s[32]
    331        param "%d %d %d\n"
    332        param t113
    333        param t120
    334        param t35
    335        call printf, 4
    336        param 12
    337        table = call malloc, 1
    338        r.32 = 0
    339  L24:  if r.32 int>= 3 goto L27
    340        t38 = r.32 int<< 2
    341        t39 = table ptr+ t38
    342        param 16
    343        t41 = call malloc, 1
    344        *t39 = t41
    345        c = 0
    346  L25:  if c int>= 4 goto L26
    347        t42 = r.32 int<< 2
    348        t43 = table ptr+ t42
    349        t44 = *t43
    350        t45 = c int<< 2
    351        t46 = t44 ptr+ t45
    352        t47 = r.32 int* 10
    353        t48 = t47 int+ c
    354        *t46 = t48
    355        c = c int+ 1
    356        if c int>= 4 goto L26
    357        t42 = r.32 int<< 2
    358        t43 = table ptr+ t42
    359        t44 = *t43
    360        t45 = c int<< 2
    361        t46 = t44 ptr+ t45
    362        t47 = r.32 int* 10
    363        t48 = t47 int+ c
    364        *t46 = t48
    365        c = c int+ 1
    366        goto L25
    367  L26:  r.32 = r.32 int+ 1
    368        goto L24
    369  L27:  diagonal = 0
    370        r.35 = 0
    371  L28:  if r.35 int>= 3 goto L29
    372        t51 = r.35 int<< 2
    373        t52 = table ptr+ t51
    374        t53 = *t52
    375        t55 = t53 ptr+ t51
    376        t56 = *t55
    377        diagonal = diagonal int+ t56
    378        r.35 = r.35 int+ 1
    379        if r.35 int>= 3 goto L29
    380        t51 = r.35 int<< 2
    381        t52 = table ptr+ t51
    382        t53 = *t52
    383        t55 = t53 ptr+ t51
    384        t56 = *t55
    385        diagonal = diagonal int+ t56
    386        r.35 = r.35 int+ 1
    387        goto L28
    388  L29:  t61 = table ptr+ 8
    389        t62 = *t61
    390        t64 = t62 ptr+ 16
    391        t65 = t64 ptr- 4
    392        t66 = *t65
    393        t67 = table ptr+ 4
    394        t68 = *t67
    395        t69 = t68 ptr+ 8
    396        t70 = *t69
    397        param "%d %d %d\n"
    398        param diagonal
    399        param t66
    400        param t70
    401        call printf, 4
    402        v1 = 1
    403        v2 = 2
    404        v3 = 3
    405        t71 = &v3
    406        t72 = &v1
    407        t73 = &v2
    408        ptrs[0] = t71
    409        ptrs[4] = t72
    410        ptrs[8] = t73
    411        t74 = &ptrs
    412        t75 = *t74
    413        *t75 = 30
    414        t76 = ptrs[8]
    415        t77 = *t76
    416        t78 = t77 int+ 5
    417        *t76 = t78
    418        t79 = t74 ptr+ 4
    419        t80 = *t79
    420        t81 = *t80
    421        param "%d %d %d %d\n"
    422        param v1
    423        param v2
    424        param v3
    425        param t81
    426        call printf, 5
    427        param t14
    428        t82 = call height(struct Tree *), 1
    429        return t82


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
