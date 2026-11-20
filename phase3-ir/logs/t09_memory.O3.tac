============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t09_memory.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 151 -> 155 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          151 -> 155   (-2% fewer)

   constants folded                        5
   algebraic simplifications               6
   common subexpressions                   3
   copies / constants forwarded           32
   temporaries merged away                 9
   dead instructions removed              11
   jumps removed or redirected             5
   unreachable instructions removed        0
   propagated across blocks                9
   dead assignments removed                6
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      1
   loops unrolled                          5
   unreachable functions removed           1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 44 temporaries, frame 328 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                local   int                             4       0
   a                local   int *                           4       4
   i.6              local   int                             4       8
   z                local   int *                           4      12
   i.8              local   int                             4      16
   list             local   struct Node *                   4      20
   i.10             local   int                             4      24
   sum              local   int                             4      28
   p                local   struct Node *                   4      32
   dead             local   struct Node *                   4      36
   d                local   double *                        4      40
   one              local   int *                           4      44
   text             local   char *                          4      48
   t3               temp    int                             4      60
   t4               temp    int *                           4      64
   t5               temp    int                             4      68
   t7               temp    void *                          4      76
   t8               temp    int *                           4      80
   t9               temp    int                             4      84
   t10              temp    int *                           4      88
   t11              temp    int                             4      92
   t12              temp    int                             4      96
   t13              temp    int *                           4     100
   t18              temp    int                             4     120
   t19              temp    int *                           4     124
   t20              temp    int                             4     128
   t21              temp    int                             4     132
   t22              temp    int *                           4     136
   t23              temp    int                             4     140
   t24              temp    int                             4     144
   t26              temp    int *                           4     152
   t27              temp    int                             4     156
   t28              temp    int *                           4     160
   t29              temp    int                             4     164
   t31              temp    int                             4     172
   t32              temp    int                             4     176
   t33              temp    int                             4     180
   t36              temp    int                             4     192
   t38              temp    struct Node *                   4     200
   t40              temp    struct Node *                   4     208
   t41              temp    struct Node *                   4     212
   t42              temp    int                             4     216
   t43              temp    struct Node *                   4     220
   t46              temp    void *                          4     232
   t47              temp    double *                        4     236
   t48              temp    double                          8     240
   t51              temp    double                          8     264
   t52              temp    double *                        4     272
   t53              temp    void *                          4     276
   t54              temp    void *                          4     280
   t55              temp    char *                          4     284
   t56              temp    char *                          4     288
   t58              temp    double                          8     296
   t59              temp    int                             4     304
   t60              temp    int                             4     308
   t63              temp    void *                          4     320
   t64              temp    struct Node *                   4     324
   (20 temporaries no longer used after optimization not shown)

 Code: 155 instruction(s)

    100        param 20
    101        a = call malloc, 1
    102        i.6 = 0
    103  L1:   if i.6 int>= 5 goto L2
    104        t3 = i.6 int<< 2
    105        t4 = a ptr+ t3
    106        t5 = i.6 int* i.6
    107        *t4 = t5
    108        i.6 = i.6 int+ 1
    109        if i.6 int>= 5 goto L2
    110        t3 = i.6 int<< 2
    111        t4 = a ptr+ t3
    112        t5 = i.6 int* i.6
    113        *t4 = t5
    114        i.6 = i.6 int+ 1
    115        goto L1
    116  L2:   param 5
    117        param 4
    118        t7 = call calloc, 2
    119        t8 = a ptr+ 16
    120        t9 = *t8
    121        t10 = t7 ptr+ 4
    122        t11 = *t10
    123        t12 = t9 int+ t11
    124        t13 = t7 ptr+ 8
    125        *t13 = t12
    126        param a
    127        param 40
    128        a = call realloc, 2
    129        i.8 = 5
    130  L3:   if i.8 int>= 10 goto L4
    131        t18 = i.8 int<< 2
    132        t19 = a ptr+ t18
    133        t20 = i.8 int- 5
    134        t21 = t20 int<< 2
    135        t22 = a ptr+ t21
    136        t23 = *t22
    137        t24 = t23 int+ 100
    138        *t19 = t24
    139        i.8 = i.8 int+ 1
    140        if i.8 int>= 10 goto L4
    141        t18 = i.8 int<< 2
    142        t19 = a ptr+ t18
    143        t20 = i.8 int- 5
    144        t21 = t20 int<< 2
    145        t22 = a ptr+ t21
    146        t23 = *t22
    147        t24 = t23 int+ 100
    148        *t19 = t24
    149        i.8 = i.8 int+ 1
    150        goto L3
    151  L4:   t26 = a ptr+ 16
    152        t27 = *t26
    153        t28 = a ptr+ 36
    154        t29 = *t28
    155        t31 = *t13
    156        t32 = *t7
    157        param "%d %d %d %d\n"
    158        param t27
    159        param t29
    160        param t31
    161        param t32
    162        call printf, 5
    163        list = 0
    164        i.10 = 1
    165  L5:   if i.10 int> 4 goto L6
    166        t33 = i.10 int* 10
    167        param 8
    168        t63 = call malloc, 1
    169        *t63 = t33
    170        t64 = t63 ptr+ 4
    171        *t64 = list
    172        list = t63
    173        i.10 = i.10 int+ 1
    174        if i.10 int> 4 goto L6
    175        t33 = i.10 int* 10
    176        param 8
    177        t63 = call malloc, 1
    178        *t63 = t33
    179        t64 = t63 ptr+ 4
    180        *t64 = list
    181        list = t63
    182        i.10 = i.10 int+ 1
    183        goto L5
    184  L6:   sum = 0
    185        p = list
    186  L7:   if p ptr== 0 goto L8
    187        t36 = *p
    188        sum = sum int+ t36
    189        t38 = p ptr+ 4
    190        p = *t38
    191        if p ptr== 0 goto L8
    192        t36 = *p
    193        sum = sum int+ t36
    194        t38 = p ptr+ 4
    195        p = *t38
    196        goto L7
    197  L8:   t40 = list ptr+ 4
    198        t41 = *t40
    199        t42 = *t41
    200        param "%d %d\n"
    201        param sum
    202        param t42
    203        call printf, 3
    204  L9:   if list ptr== 0 goto L10
    205        dead = list
    206        t43 = list ptr+ 4
    207        list = *t43
    208        param dead
    209        call free, 1
    210        if list ptr== 0 goto L10
    211        dead = list
    212        t43 = list ptr+ 4
    213        list = *t43
    214        param dead
    215        call free, 1
    216        goto L9
    217  L10:  param 24
    218        t46 = call malloc, 1
    219        *t46 = 1.5
    220        t47 = t46 ptr+ 8
    221        *t47 = 2.5
    222        t48 = *t46
    223        t51 = t48 double+ 2.5
    224        t52 = t46 ptr+ 16
    225        *t52 = t51
    226        param 4
    227        t53 = call malloc, 1
    228        *t53 = 42
    229        param 8
    230        t54 = call malloc, 1
    231        *t54 = 111
    232        t55 = t54 ptr+ 1
    233        *t55 = 107
    234        t56 = t54 ptr+ 2
    235        *t56 = 0
    236        t58 = *t52
    237        t59 = *t53
    238        param "%.1f %d %s\n"
    239        param t58
    240        param t59
    241        param t54
    242        call printf, 4
    243        param t46
    244        call free, 1
    245        param t53
    246        call free, 1
    247        param t54
    248        call free, 1
    249        param a
    250        call free, 1
    251        param t7
    252        call free, 1
    253        t60 = sum int/ 10
    254        return t60


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Node               struct_tag    struct Node                -           4    -    0  size 8
   push               function      struct Node *(struct Node *, int) -           6    -    1  _Z4pushP4Nodei; defined
   main               function      int (void)                 -          13    -    0  defined

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   value              field         int                        member      4    4    3  Node::value; public, offset 0
   next               field         struct Node *              member      4    4    4  Node::next; public, offset 4

 scope: global > push()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   head               parameter     struct Node *              param       6    4    1  head.1
   v                  parameter     int                        param       6    4    1  v.2
   n                  variable      struct Node *              local       7    4    3  n.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        local      14    4    7  n.4
   a                  variable      int *                      local      15    4    9  a.5
   z                  variable      int *                      local      17    4    5  z.7
   list               variable      struct Node *              local      23    4    8  list.9
   sum                variable      int                        local      25    4    3  sum.11
   d                  variable      double *                   local      34    4    7  d.14
   one                variable      int *                      local      36    4    3  one.15
   text               variable      char *                     local      38    4    5  text.16

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      16    4    5  i.6
   i                  variable      int                        local      20    4    4  i.8
   i                  variable      int                        local      24    4    3  i.10
   p                  variable      struct Node *              local      26    4    4  p.12

 scope: global > main() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   dead               variable      struct Node *              local      29    4    1  dead.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Node: size 8, align 4
    +0  int value  [public]
    +4  struct Node * next  [public]
