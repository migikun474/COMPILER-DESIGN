============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t38_free_list.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 201 -> 215 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          201 -> 215   (-6% fewer)

   calls inlined                           6
   constants folded                        2
   algebraic simplifications              10
   common subexpressions                   2
   copies / constants forwarded           29
   temporaries merged away                17
   dead instructions removed              10
   jumps removed or redirected            11
   unreachable instructions removed        0

============================================================================
 FUNCTION build(int)        (link name _Z5buildi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   head             local   struct Node *                   4       4
   i                local   int                             4       8
   p                local   struct Node *                   4      12
   t1               temp    void *                          4      16
   t2               temp    struct Node *                   4      20
   (1 temporary no longer used after optimization not shown)

 Code: 13 instruction(s)

    100       head = 0
    101       i = 1
    102  L1:  if i int> n goto L2
    103       param 8
    104       t1 = call malloc, 1
    105       p = t1
    106       *t1 = i
    107       t2 = t1 ptr+ 4
    108       *t2 = head
    109       head = t1
    110       i = i int+ 1
    111       goto L1
    112  L2:  return head

============================================================================
 FUNCTION total(struct Node *)        (link name _Z5totalP4Node)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Node *                   4       0
   s                local   int                             4       4
   t1               temp    int                             4       8
   t3               temp    struct Node *                   4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 8 instruction(s)

    113       s = 0
    114  L3:  if p ptr== 0 goto L4
    115       t1 = *p
    116       s = s int+ t1
    117       t3 = p ptr+ 4
    118       p = *t3
    119       goto L3
    120  L4:  return s

============================================================================
 FUNCTION release(struct Node *)        (link name _Z7releaseP4Node)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Node *                   4       0
   n                local   struct Node *                   4       4
   t1               temp    struct Node *                   4       8
   t2               temp    struct Node *                   4      12

 Code: 9 instruction(s)

    121  L5:  if p ptr== 0 goto L6
    122       t1 = p ptr+ 4
    123       t2 = *t1
    124       n = t2
    125       param p
    126       call free, 1
    127       p = t2
    128       goto L5
    129  L6:  return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 53 temporaries, frame 372 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   char *                          4       0
   b                local   char *                          4       4
   sum              local   long long                       8       8
   i                local   int                             4      16
   k                local   int                             4      20
   p                local   int *                           4      24
   list             local   struct Node *                   4      28
   dirty            local   int *                           4      32
   clean            local   int *                           4      36
   nonzero          local   int                             4      40
   grow             local   int *                           4      44
   n                local   int                             4      48
   gsum             local   int                             4      52
   t1               temp    void *                          4      56
   t2               temp    void *                          4      60
   t3               temp    int                             4      64
   t4               temp    void *                          4      68
   t5               temp    int                             4      72
   t6               temp    int *                           4      76
   t7               temp    int                             4      80
   t10              temp    int                             4      92
   t11              temp    long long                       8      96
   t14              temp    struct Node *                   4     116
   t16              temp    struct Node *                   4     124
   t19              temp    int                             4     136
   t20              temp    int *                           4     140
   t23              temp    int                             4     152
   t24              temp    int *                           4     156
   t25              temp    int                             4     160
   t30              temp    int                             4     180
   t31              temp    int *                           4     184
   t33              temp    int                             4     192
   t34              temp    unsigned int                    4     196
   t36              temp    int                             4     204
   t37              temp    int                             4     208
   t38              temp    int *                           4     212
   t41              temp    int                             4     224
   t42              temp    int *                           4     228
   t43              temp    int                             4     232
   t47              temp    void *                          4     248
   t48              temp    int *                           4     252
   t49              temp    int                             4     256
   t50              temp    int                             4     260
   t51              temp    struct Node *                   4     264
   t52              temp    int                             4     268
   t53              temp    void *                          4     272
   t55              temp    struct Node *                   4     280
   t56              temp    struct Node *                   4     284
   t57              temp    int                             4     288
   t58              temp    int                             4     292
   t59              temp    struct Node *                   4     296
   t60              temp    struct Node *                   4     300
   t61              temp    struct Node *                   4     304
   t62              temp    struct Node *                   4     308
   t64              temp    int                             4     316
   t65              temp    struct Node *                   4     320
   t66              temp    int                             4     324
   t67              temp    void *                          4     328
   t69              temp    struct Node *                   4     336
   t70              temp    struct Node *                   4     340
   t71              temp    int                             4     344
   t72              temp    int                             4     348
   t73              temp    struct Node *                   4     352
   t74              temp    struct Node *                   4     356
   t75              temp    struct Node *                   4     360
   t76              temp    struct Node *                   4     364
   (24 temporaries no longer used after optimization not shown)

 Code: 185 instruction(s)

    130        param 1000
    131        t1 = call malloc, 1
    132        a = t1
    133        *t1 = 120
    134        param t1
    135        call free, 1
    136        param 1000
    137        t2 = call malloc, 1
    138        b = t2
    139        if t1 ptr== t2 goto L7
    140        t3 = 0
    141        goto L8
    142  L7:   t3 = 1
    143  L8:   param "reused %d\n"
    144        param t3
    145        call printf, 2
    146        param b
    147        call free, 1
    148        sum = 0
    149        i = 0
    150  L9:   if i int>= 50000 goto L10
    151        param 300
    152        t4 = call malloc, 1
    153        p = t4
    154        *t4 = i
    155        t5 = i int<< 1
    156        t6 = t4 ptr+ 296
    157        *t6 = t5
    158        t7 = *t4
    159        t10 = t7 int+ t5
    160        t11 = inttollong t10
    161        sum = sum llong+ t11
    162        param t4
    163        call free, 1
    164        i = i int+ 1
    165        goto L9
    166  L10:  param "loop %lld\n"
    167        param sum
    168        call printf, 2
    169        t50 = 100
    170        t51 = 0
    171        t52 = 1
    172  L11:  if t52 int> t50 goto L12
    173        param 8
    174        t53 = call malloc, 1
    175        *t53 = t52
    176        t55 = t53 ptr+ 4
    177        *t55 = t51
    178        t51 = t53
    179        t52 = t52 int+ 1
    180        goto L11
    181  L12:  t14 = t51
    182        list = t51
    183        t56 = t51
    184        t57 = 0
    185  L13:  if t56 ptr== 0 goto L14
    186        t58 = *t56
    187        t57 = t57 int+ t58
    188        t59 = t56 ptr+ 4
    189        t56 = *t59
    190        goto L13
    191  L14:  param "list %d\n"
    192        param t57
    193        call printf, 2
    194        t60 = t14
    195  L15:  if t60 ptr== 0 goto L16
    196        t61 = t60 ptr+ 4
    197        t62 = *t61
    198        param t60
    199        call free, 1
    200        t60 = t62
    201        goto L15
    202  L16:  t64 = 200
    203        t65 = 0
    204        t66 = 1
    205  L17:  if t66 int> t64 goto L18
    206        param 8
    207        t67 = call malloc, 1
    208        *t67 = t66
    209        t69 = t67 ptr+ 4
    210        *t69 = t65
    211        t65 = t67
    212        t66 = t66 int+ 1
    213        goto L17
    214  L18:  t16 = t65
    215        list = t65
    216        t70 = t65
    217        t71 = 0
    218  L19:  if t70 ptr== 0 goto L20
    219        t72 = *t70
    220        t71 = t71 int+ t72
    221        t73 = t70 ptr+ 4
    222        t70 = *t73
    223        goto L19
    224  L20:  param "list %d\n"
    225        param t71
    226        call printf, 2
    227        t74 = t16
    228  L21:  if t74 ptr== 0 goto L22
    229        t75 = t74 ptr+ 4
    230        t76 = *t75
    231        param t74
    232        call free, 1
    233        t74 = t76
    234        goto L21
    235  L22:  param 64
    236        dirty = call malloc, 1
    237        k = 0
    238  L23:  if k int>= 16 goto L24
    239        t19 = k int<< 2
    240        t20 = dirty ptr+ t19
    241        *t20 = 99
    242        k = k int+ 1
    243        goto L23
    244  L24:  param dirty
    245        call free, 1
    246        param 16
    247        param 4
    248        clean = call calloc, 2
    249        nonzero = 0
    250        k = 0
    251  L25:  if k int>= 16 goto L27
    252        t23 = k int<< 2
    253        t24 = clean ptr+ t23
    254        t25 = *t24
    255        if t25 int== 0 goto L26
    256        nonzero = nonzero int+ 1
    257  L26:  k = k int+ 1
    258        goto L25
    259  L27:  param "calloc %d\n"
    260        param nonzero
    261        call printf, 2
    262        param clean
    263        call free, 1
    264        param 16
    265        grow = call malloc, 1
    266        n = 4
    267        k = 0
    268  L28:  if k int>= 4 goto L29
    269        t30 = k int<< 2
    270        t31 = grow ptr+ t30
    271        *t31 = k
    272        k = k int+ 1
    273        goto L28
    274  L29:  if n int>= 64 goto L32
    275        t33 = n int<< 1
    276        t34 = t33 uint<< 2
    277        param grow
    278        param t34
    279        grow = call realloc, 2
    280        k = n
    281  L30:  t36 = n int<< 1
    282        if k int>= t36 goto L31
    283        t37 = k int<< 2
    284        t38 = grow ptr+ t37
    285        *t38 = k
    286        k = k int+ 1
    287        goto L30
    288  L31:  n = n int<< 1
    289        goto L29
    290  L32:  gsum = 0
    291        k = 0
    292  L33:  if k int>= n goto L34
    293        t41 = k int<< 2
    294        t42 = grow ptr+ t41
    295        t43 = *t42
    296        gsum = gsum int+ t43
    297        k = k int+ 1
    298        goto L33
    299  L34:  param grow
    300        param 32
    301        t47 = call realloc, 2
    302        grow = t47
    303        t48 = t47 ptr+ 28
    304        t49 = *t48
    305        param "realloc %d %d %d\n"
    306        param n
    307        param gsum
    308        param t49
    309        call printf, 4
    310        param t47
    311        call free, 1
    312        param 0
    313        call free, 1
    314        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Node               struct_tag    struct Node                -           6    -    0  size 8
   build              function      struct Node *(int)         -           8    -    2  _Z5buildi; defined
   total              function      int (struct Node *)        -          19    -    2  _Z5totalP4Node; defined
   release            function      void (struct Node *)       -          20    -    2  _Z7releaseP4Node; defined
   main               function      int (void)                 -          22    -    0  defined

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   value              field         int                        member      6    4    2  Node::value; public, offset 0
   next               field         struct Node *              member      6    4    3  Node::next; public, offset 4

 scope: global > build()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       8    4    1  n.1
   head               variable      struct Node *              local       9    4    3  head.2
   i                  variable      int                        local      10    4    4  i.3

 scope: global > build() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  variable      struct Node *              local      12    4    3  p.4

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Node *              param      19    4    4  p.5
   s                  variable      int                        local      19    4    2  s.6

 scope: global > release()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     struct Node *              param      20    4    4  p.7

 scope: global > release() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      struct Node *              local      20    4    1  n.8

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      char *                     local      23    4    3  a.9
   b                  variable      char *                     local      26    4    2  b.10
   sum                variable      long long                  local      30    8    2  sum.11
   i                  variable      int                        local      31    4    5  i.12
   k                  variable      int                        local      31    4   22  k.13
   list               variable      struct Node *              local      41    4    5  list.15
   dirty              variable      int *                      local      48    4    2  dirty.16
   clean              variable      int *                      local      51    4    2  clean.17
   nonzero            variable      int                        local      52    4    2  nonzero.18
   grow               variable      int *                      local      57    4    9  grow.19
   n                  variable      int                        local      58    4    8  n.20
   gsum               variable      int                        local      65    4    2  gsum.21

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  variable      int *                      local      33    4    5  p.14

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Node: size 8, align 4
    +0  int value  [public]
    +4  struct Node * next  [public]

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

reused 1
loop 3749925000
list 5050
list 20100
calloc 0
realloc 64 2016 7

   exit code 0, 807836 instructions executed
