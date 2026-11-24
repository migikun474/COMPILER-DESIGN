============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t09_memory.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 157 -> 165 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          157 -> 165   (-5% fewer)

   constants folded                        4
   algebraic simplifications               3
   common subexpressions                  10
   copies / constants forwarded           36
   temporaries merged away                 7
   dead instructions removed              16
   jumps removed or redirected             6
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                9
   calls inlined                           1
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          6
   unreachable functions removed           1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 39 temporaries, frame 308 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   list             local   struct Node *                   4       0
   rev              local   struct Node *                   4       4
   i                local   int                             4       8
   n.7              local   struct Node *                   4      12
   s                local   int                             4      16
   n.9              local   struct Node *                   4      20
   rows             local   int **                          4      24
   g                local   int *                           4      28
   a                local   char *                          4      32
   b                local   char *                          4      36
   total            local   long long                       8      40
   t                local   int *                           4      48
   t3               temp    struct Node *                   4      60
   t4               temp    struct Node *                   4      64
   t6               temp    int                             4      72
   t7               temp    int                             4      76
   t9               temp    struct Node *                   4      84
   t11              temp    struct Node *                   4      92
   t12              temp    struct Node *                   4      96
   t15              temp    int                             4     108
   t16              temp    int **                          4     112
   t17              temp    void *                          4     116
   t22              temp    int *                           4     136
   t23              temp    int                             4     140
   t25              temp    int **                          4     148
   t26              temp    int *                           4     152
   t27              temp    int *                           4     156
   t28              temp    int                             4     160
   t29              temp    int **                          4     164
   t30              temp    int *                           4     168
   t31              temp    int                             4     172
   t32              temp    int *                           4     176
   t33              temp    int                             4     180
   t36              temp    int *                           4     192
   t37              temp    int                             4     196
   t38              temp    int                             4     200
   t40              temp    void *                          4     208
   t41              temp    int *                           4     212
   t43              temp    void *                          4     220
   t45              temp    void *                          4     228
   t46              temp    int                             4     232
   t47              temp    int *                           4     236
   t48              temp    int                             4     240
   t49              temp    void *                          4     244
   t50              temp    void *                          4     248
   t51              temp    int                             4     252
   t52              temp    void *                          4     256
   t53              temp    int *                           4     260
   t56              temp    long long                       8     272
   t61              temp    void *                          4     300
   t62              temp    struct Node *                   4     304
   (23 temporaries no longer used after optimization not shown)

 Code: 165 instruction(s)

    100        list = 0
    101        rev = 0
    102        i = 1
    103  L1:   if i int> 5 goto L2
    104        param 8
    105        t61 = call malloc, 1
    106        *t61 = i
    107        t62 = t61 ptr+ 4
    108        *t62 = list
    109        list = t61
    110        i = i int+ 1
    111        if i int> 5 goto L2
    112        param 8
    113        t61 = call malloc, 1
    114        *t61 = i
    115        t62 = t61 ptr+ 4
    116        *t62 = list
    117        list = t61
    118        i = i int+ 1
    119        goto L1
    120  L2:   if list ptr== 0 goto L3
    121        t3 = list ptr+ 4
    122        t4 = *t3
    123        *t3 = rev
    124        rev = list
    125        list = t4
    126        if t4 ptr== 0 goto L3
    127        t3 = list ptr+ 4
    128        t4 = *t3
    129        *t3 = rev
    130        rev = list
    131        list = t4
    132        goto L2
    133  L3:   s = 0
    134        list = rev
    135  L4:   if list ptr== 0 goto L5
    136        t6 = s int* 10
    137        t7 = *list
    138        s = t6 int+ t7
    139        t9 = list ptr+ 4
    140        list = *t9
    141        if list ptr== 0 goto L5
    142        t6 = s int* 10
    143        t7 = *list
    144        s = t6 int+ t7
    145        t9 = list ptr+ 4
    146        list = *t9
    147        goto L4
    148  L5:   param "%d\n"
    149        param s
    150        call printf, 2
    151  L6:   if rev ptr== 0 goto L7
    152        t11 = rev ptr+ 4
    153        t12 = *t11
    154        param rev
    155        call free, 1
    156        rev = t12
    157        if t12 ptr== 0 goto L7
    158        t11 = rev ptr+ 4
    159        t12 = *t11
    160        param rev
    161        call free, 1
    162        rev = t12
    163        goto L6
    164  L7:   param 12
    165        rows = call malloc, 1
    166        i = 0
    167  L8:   if i int>= 3 goto L9
    168        t15 = i int<< 2
    169        t16 = rows ptr+ t15
    170        param 4
    171        param 4
    172        t17 = call calloc, 2
    173        *t16 = t17
    174        t22 = t17 ptr+ t15
    175        t23 = i int+ 1
    176        *t22 = t23
    177        i = t23
    178        if t23 int>= 3 goto L9
    179        t15 = i int<< 2
    180        t16 = rows ptr+ t15
    181        param 4
    182        param 4
    183        t17 = call calloc, 2
    184        *t16 = t17
    185        t22 = t17 ptr+ t15
    186        t23 = i int+ 1
    187        *t22 = t23
    188        i = t23
    189        goto L8
    190  L9:   t25 = rows ptr+ 8
    191        t26 = *t25
    192        t27 = t26 ptr+ 8
    193        t28 = *t27
    194        t29 = rows ptr+ 4
    195        t30 = *t29
    196        t31 = *t30
    197        t32 = *rows
    198        t33 = *t32
    199        t36 = t30 ptr+ 4
    200        t37 = *t36
    201        t38 = t33 int+ t37
    202        param "%d %d %d\n"
    203        param t28
    204        param t31
    205        param t38
    206        call printf, 4
    207        param 8
    208        t40 = call malloc, 1
    209        *t40 = 11
    210        t41 = t40 ptr+ 4
    211        *t41 = 22
    212        param t40
    213        param 200
    214        t43 = call realloc, 2
    215        param t43
    216        param 8
    217        t45 = call realloc, 2
    218        t46 = *t45
    219        t47 = t45 ptr+ 4
    220        t48 = *t47
    221        param "%d %d\n"
    222        param t46
    223        param t48
    224        call printf, 3
    225        param 100
    226        t49 = call malloc, 1
    227        param t49
    228        call free, 1
    229        param 100
    230        t50 = call malloc, 1
    231        if t49 ptr== t50 goto L10
    232        t51 = 0
    233        goto L11
    234  L10:  t51 = 1
    235  L11:  param "%d\n"
    236        param t51
    237        call printf, 2
    238        total = 0
    239        i = 0
    240  L12:  if i int>= 30000 goto L13
    241        param 400
    242        t52 = call malloc, 1
    243        t53 = t52 ptr+ 396
    244        *t53 = i
    245        t56 = inttollong i
    246        total = total llong+ t56
    247        param t52
    248        call free, 1
    249        i = i int+ 1
    250        if i int>= 30000 goto L13
    251        param 400
    252        t52 = call malloc, 1
    253        t53 = t52 ptr+ 396
    254        *t53 = i
    255        t56 = inttollong i
    256        total = total llong+ t56
    257        param t52
    258        call free, 1
    259        i = i int+ 1
    260        goto L12
    261  L13:  param "%lld\n"
    262        param total
    263        call printf, 2
    264        return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Node               struct_tag    struct Node                -           5    -    0  size 8
   push               function      struct Node *(struct Node *, int) -           6    -    1  _Z4pushP4Nodei; defined
   main               function      int (void)                 -           7    -    0  defined

 scope: global > struct Node
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  field         int                        member      5    4    2  Node::v; public, offset 0
   next               field         struct Node *              member      5    4    5  Node::next; public, offset 4

 scope: global > push()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   h                  parameter     struct Node *              param       6    4    1  h.1
   v                  parameter     int                        param       6    4    1  v.2
   n                  variable      struct Node *              local       6    4    3  n.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   list               variable      struct Node *              local       8    4   12  list.4
   rev                variable      struct Node *              local       8    4    7  rev.5
   i                  variable      int                        local       9    4   15  i.6
   s                  variable      int                        local      12    4    3  s.8
   rows               variable      int **                     local      16    4    6  rows.10
   g                  variable      int *                      local      19    4    8  g.11
   a                  variable      char *                     local      24    4    2  a.12
   b                  variable      char *                     local      26    4    1  b.13
   total              variable      long long                  local      28    8    2  total.14

 scope: global > main() > while
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      struct Node *              local      11    4    1  n.7
   n                  variable      struct Node *              local      15    4    1  n.9

 scope: global > main() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  variable      int *                      local      29    4    3  t.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct Node: size 8, align 4
    +0  int v  [public]
    +4  struct Node * next  [public]
