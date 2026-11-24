============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t38_free_list.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 201 -> 256 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          201 -> 256   (-27% fewer)

   constants folded                        2
   algebraic simplifications              10
   common subexpressions                   2
   copies / constants forwarded           30
   temporaries merged away                17
   dead instructions removed               6
   jumps removed or redirected            11
   unreachable instructions removed        0
   propagated across blocks                5
   dead assignments removed               12
   calls inlined                           6
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                         15
   unreachable functions removed           3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 49 temporaries, frame 356 bytes

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
   t51              temp    struct Node *                   4     264
   t52              temp    int                             4     268
   t53              temp    void *                          4     272
   t54              temp    struct Node *                   4     276
   t55              temp    struct Node *                   4     280
   t56              temp    int                             4     284
   t57              temp    int                             4     288
   t58              temp    struct Node *                   4     292
   t59              temp    struct Node *                   4     296
   t60              temp    struct Node *                   4     300
   t61              temp    struct Node *                   4     304
   t63              temp    struct Node *                   4     312
   t64              temp    int                             4     316
   t65              temp    void *                          4     320
   t66              temp    struct Node *                   4     324
   t67              temp    struct Node *                   4     328
   t68              temp    int                             4     332
   t69              temp    int                             4     336
   t70              temp    struct Node *                   4     340
   t71              temp    struct Node *                   4     344
   t72              temp    struct Node *                   4     348
   t73              temp    struct Node *                   4     352
   (24 temporaries no longer used after optimization not shown)

 Code: 256 instruction(s)

    100        param 1000
    101        t1 = call malloc, 1
    102        *t1 = 120
    103        param t1
    104        call free, 1
    105        param 1000
    106        t2 = call malloc, 1
    107        if t1 ptr== t2 goto L1
    108        t3 = 0
    109        goto L2
    110  L1:   t3 = 1
    111  L2:   param "reused %d\n"
    112        param t3
    113        call printf, 2
    114        param t2
    115        call free, 1
    116        sum = 0
    117        i = 0
    118  L3:   if i int>= 50000 goto L4
    119        param 300
    120        t4 = call malloc, 1
    121        *t4 = i
    122        t5 = i int<< 1
    123        t6 = t4 ptr+ 296
    124        *t6 = t5
    125        t7 = *t4
    126        t10 = t7 int+ t5
    127        t11 = inttollong t10
    128        sum = sum llong+ t11
    129        param t4
    130        call free, 1
    131        i = i int+ 1
    132        if i int>= 50000 goto L4
    133        param 300
    134        t4 = call malloc, 1
    135        *t4 = i
    136        t5 = i int<< 1
    137        t6 = t4 ptr+ 296
    138        *t6 = t5
    139        t7 = *t4
    140        t10 = t7 int+ t5
    141        t11 = inttollong t10
    142        sum = sum llong+ t11
    143        param t4
    144        call free, 1
    145        i = i int+ 1
    146        goto L3
    147  L4:   param "loop %lld\n"
    148        param sum
    149        call printf, 2
    150        t51 = 0
    151        t52 = 1
    152  L5:   if t52 int> 100 goto L6
    153        param 8
    154        t53 = call malloc, 1
    155        *t53 = t52
    156        t54 = t53 ptr+ 4
    157        *t54 = t51
    158        t51 = t53
    159        t52 = t52 int+ 1
    160        if t52 int> 100 goto L6
    161        param 8
    162        t53 = call malloc, 1
    163        *t53 = t52
    164        t54 = t53 ptr+ 4
    165        *t54 = t51
    166        t51 = t53
    167        t52 = t52 int+ 1
    168        goto L5
    169  L6:   t55 = t51
    170        t56 = 0
    171  L7:   if t55 ptr== 0 goto L8
    172        t57 = *t55
    173        t56 = t56 int+ t57
    174        t58 = t55 ptr+ 4
    175        t55 = *t58
    176        if t55 ptr== 0 goto L8
    177        t57 = *t55
    178        t56 = t56 int+ t57
    179        t58 = t55 ptr+ 4
    180        t55 = *t58
    181        goto L7
    182  L8:   param "list %d\n"
    183        param t56
    184        call printf, 2
    185        t59 = t51
    186  L9:   if t59 ptr== 0 goto L10
    187        t60 = t59 ptr+ 4
    188        t61 = *t60
    189        param t59
    190        call free, 1
    191        t59 = t61
    192        if t61 ptr== 0 goto L10
    193        t60 = t59 ptr+ 4
    194        t61 = *t60
    195        param t59
    196        call free, 1
    197        t59 = t61
    198        goto L9
    199  L10:  t63 = 0
    200        t64 = 1
    201  L11:  if t64 int> 200 goto L12
    202        param 8
    203        t65 = call malloc, 1
    204        *t65 = t64
    205        t66 = t65 ptr+ 4
    206        *t66 = t63
    207        t63 = t65
    208        t64 = t64 int+ 1
    209        if t64 int> 200 goto L12
    210        param 8
    211        t65 = call malloc, 1
    212        *t65 = t64
    213        t66 = t65 ptr+ 4
    214        *t66 = t63
    215        t63 = t65
    216        t64 = t64 int+ 1
    217        goto L11
    218  L12:  t67 = t63
    219        t68 = 0
    220  L13:  if t67 ptr== 0 goto L14
    221        t69 = *t67
    222        t68 = t68 int+ t69
    223        t70 = t67 ptr+ 4
    224        t67 = *t70
    225        if t67 ptr== 0 goto L14
    226        t69 = *t67
    227        t68 = t68 int+ t69
    228        t70 = t67 ptr+ 4
    229        t67 = *t70
    230        goto L13
    231  L14:  param "list %d\n"
    232        param t68
    233        call printf, 2
    234        t71 = t63
    235  L15:  if t71 ptr== 0 goto L16
    236        t72 = t71 ptr+ 4
    237        t73 = *t72
    238        param t71
    239        call free, 1
    240        t71 = t73
    241        if t73 ptr== 0 goto L16
    242        t72 = t71 ptr+ 4
    243        t73 = *t72
    244        param t71
    245        call free, 1
    246        t71 = t73
    247        goto L15
    248  L16:  param 64
    249        dirty = call malloc, 1
    250        k = 0
    251  L17:  if k int>= 16 goto L18
    252        t19 = k int<< 2
    253        t20 = dirty ptr+ t19
    254        *t20 = 99
    255        k = k int+ 1
    256        if k int>= 16 goto L18
    257        t19 = k int<< 2
    258        t20 = dirty ptr+ t19
    259        *t20 = 99
    260        k = k int+ 1
    261        goto L17
    262  L18:  param dirty
    263        call free, 1
    264        param 16
    265        param 4
    266        clean = call calloc, 2
    267        nonzero = 0
    268        k = 0
    269  L19:  if k int>= 16 goto L22
    270        t23 = k int<< 2
    271        t24 = clean ptr+ t23
    272        t25 = *t24
    273        if t25 int== 0 goto L20
    274        nonzero = nonzero int+ 1
    275  L20:  k = k int+ 1
    276        if k int>= 16 goto L22
    277        t23 = k int<< 2
    278        t24 = clean ptr+ t23
    279        t25 = *t24
    280        if t25 int== 0 goto L21
    281        nonzero = nonzero int+ 1
    282  L21:  k = k int+ 1
    283        goto L19
    284  L22:  param "calloc %d\n"
    285        param nonzero
    286        call printf, 2
    287        param clean
    288        call free, 1
    289        param 16
    290        grow = call malloc, 1
    291        n = 4
    292        k = 0
    293  L23:  if k int>= 4 goto L24
    294        t30 = k int<< 2
    295        t31 = grow ptr+ t30
    296        *t31 = k
    297        k = k int+ 1
    298        if k int>= 4 goto L24
    299        t30 = k int<< 2
    300        t31 = grow ptr+ t30
    301        *t31 = k
    302        k = k int+ 1
    303        goto L23
    304  L24:  if n int>= 64 goto L27
    305        t33 = n int<< 1
    306        t34 = t33 uint<< 2
    307        param grow
    308        param t34
    309        grow = call realloc, 2
    310        k = n
    311  L25:  t36 = n int<< 1
    312        if k int>= t36 goto L26
    313        t37 = k int<< 2
    314        t38 = grow ptr+ t37
    315        *t38 = k
    316        k = k int+ 1
    317        t36 = n int<< 1
    318        if k int>= t36 goto L26
    319        t37 = k int<< 2
    320        t38 = grow ptr+ t37
    321        *t38 = k
    322        k = k int+ 1
    323        goto L25
    324  L26:  n = n int<< 1
    325        goto L24
    326  L27:  gsum = 0
    327        k = 0
    328  L28:  if k int>= n goto L29
    329        t41 = k int<< 2
    330        t42 = grow ptr+ t41
    331        t43 = *t42
    332        gsum = gsum int+ t43
    333        k = k int+ 1
    334        if k int>= n goto L29
    335        t41 = k int<< 2
    336        t42 = grow ptr+ t41
    337        t43 = *t42
    338        gsum = gsum int+ t43
    339        k = k int+ 1
    340        goto L28
    341  L29:  param grow
    342        param 32
    343        t47 = call realloc, 2
    344        t48 = t47 ptr+ 28
    345        t49 = *t48
    346        param "realloc %d %d %d\n"
    347        param n
    348        param gsum
    349        param t49
    350        call printf, 4
    351        param t47
    352        call free, 1
    353        param 0
    354        call free, 1
    355        return 0


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
