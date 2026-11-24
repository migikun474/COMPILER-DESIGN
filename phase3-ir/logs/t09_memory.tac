============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t09_memory.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 157 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION push(struct Node *, int)        (link name _Z4pushP4Nodei)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   h                param   struct Node *                   4       0
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
    105     *t2 = h
    106     return n

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 58 temporaries, frame 292 bytes

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
   t1               temp    struct Node *                   4      52
   t2               temp    int                             4      56
   t3               temp    struct Node *                   4      60
   t4               temp    struct Node *                   4      64
   t5               temp    struct Node *                   4      68
   t6               temp    int                             4      72
   t7               temp    int                             4      76
   t8               temp    int                             4      80
   t9               temp    struct Node *                   4      84
   t10              temp    struct Node *                   4      88
   t11              temp    struct Node *                   4      92
   t12              temp    struct Node *                   4      96
   t13              temp    unsigned int                    4     100
   t14              temp    void *                          4     104
   t15              temp    int                             4     108
   t16              temp    int **                          4     112
   t17              temp    void *                          4     116
   t18              temp    int                             4     120
   t19              temp    int **                          4     124
   t20              temp    int *                           4     128
   t21              temp    int                             4     132
   t22              temp    int *                           4     136
   t23              temp    int                             4     140
   t24              temp    int                             4     144
   t25              temp    int **                          4     148
   t26              temp    int *                           4     152
   t27              temp    int *                           4     156
   t28              temp    int                             4     160
   t29              temp    int **                          4     164
   t30              temp    int *                           4     168
   t31              temp    int                             4     172
   t32              temp    int *                           4     176
   t33              temp    int                             4     180
   t34              temp    int **                          4     184
   t35              temp    int *                           4     188
   t36              temp    int *                           4     192
   t37              temp    int                             4     196
   t38              temp    int                             4     200
   t39              temp    unsigned int                    4     204
   t40              temp    void *                          4     208
   t41              temp    int *                           4     212
   t42              temp    unsigned int                    4     216
   t43              temp    void *                          4     220
   t44              temp    unsigned int                    4     224
   t45              temp    void *                          4     228
   t46              temp    int                             4     232
   t47              temp    int *                           4     236
   t48              temp    int                             4     240
   t49              temp    void *                          4     244
   t50              temp    void *                          4     248
   t51              temp    int                             4     252
   t52              temp    void *                          4     256
   t53              temp    int *                           4     260
   t54              temp    int *                           4     264
   t55              temp    int                             4     268
   t56              temp    long long                       8     272
   t57              temp    long long                       8     280
   t58              temp    int                             4     288

 Code: 150 instruction(s)

    107        list = 0
    108        rev = 0
    109        i = 1
    110  L1:   if i int<= 5 goto L2
    111        goto L3
    112  L2:   param list
    113        param i
    114        t1 = call push(struct Node *, int), 2
    115        list = t1
    116        t2 = i int+ 1
    117        i = t2
    118        goto L1
    119  L3:   if list ptr!= 0 goto L4
    120        goto L5
    121  L4:   t3 = list ptr+ 4
    122        t4 = *t3
    123        n.7 = t4
    124        t5 = list ptr+ 4
    125        *t5 = rev
    126        rev = list
    127        list = n.7
    128        goto L3
    129  L5:   s = 0
    130        list = rev
    131  L6:   if list ptr!= 0 goto L7
    132        goto L8
    133  L7:   t6 = s int* 10
    134        t7 = *list
    135        t8 = t6 int+ t7
    136        s = t8
    137        t9 = list ptr+ 4
    138        t10 = *t9
    139        list = t10
    140        goto L6
    141  L8:   param "%d\n"
    142        param s
    143        call printf, 2
    144  L9:   if rev ptr!= 0 goto L10
    145        goto L11
    146  L10:  t11 = rev ptr+ 4
    147        t12 = *t11
    148        n.9 = t12
    149        param rev
    150        call free, 1
    151        rev = n.9
    152        goto L9
    153  L11:  t13 = 3 uint* 4
    154        param t13
    155        t14 = call malloc, 1
    156        rows = t14
    157        i = 0
    158  L12:  if i int< 3 goto L13
    159        goto L14
    160  L13:  t15 = i int* 4
    161        t16 = rows ptr+ t15
    162        param 4
    163        param 4
    164        t17 = call calloc, 2
    165        *t16 = t17
    166        t18 = i int* 4
    167        t19 = rows ptr+ t18
    168        t20 = *t19
    169        t21 = i int* 4
    170        t22 = t20 ptr+ t21
    171        t23 = i int+ 1
    172        *t22 = t23
    173        t24 = i int+ 1
    174        i = t24
    175        goto L12
    176  L14:  t25 = rows ptr+ 8
    177        t26 = *t25
    178        t27 = t26 ptr+ 8
    179        t28 = *t27
    180        t29 = rows ptr+ 4
    181        t30 = *t29
    182        t31 = *t30
    183        t32 = *rows
    184        t33 = *t32
    185        t34 = rows ptr+ 4
    186        t35 = *t34
    187        t36 = t35 ptr+ 4
    188        t37 = *t36
    189        t38 = t33 int+ t37
    190        param "%d %d %d\n"
    191        param t28
    192        param t31
    193        param t38
    194        call printf, 4
    195        t39 = 2 uint* 4
    196        param t39
    197        t40 = call malloc, 1
    198        g = t40
    199        *g = 11
    200        t41 = g ptr+ 4
    201        *t41 = 22
    202        t42 = 50 uint* 4
    203        param g
    204        param t42
    205        t43 = call realloc, 2
    206        g = t43
    207        t44 = 2 uint* 4
    208        param g
    209        param t44
    210        t45 = call realloc, 2
    211        g = t45
    212        t46 = *g
    213        t47 = g ptr+ 4
    214        t48 = *t47
    215        param "%d %d\n"
    216        param t46
    217        param t48
    218        call printf, 3
    219        param 100
    220        t49 = call malloc, 1
    221        a = t49
    222        param a
    223        call free, 1
    224        param 100
    225        t50 = call malloc, 1
    226        b = t50
    227        if a ptr== b goto L15
    228        t51 = 0
    229        goto L16
    230  L15:  t51 = 1
    231  L16:  param "%d\n"
    232        param t51
    233        call printf, 2
    234        total = 0
    235        i = 0
    236  L17:  if i int< 30000 goto L18
    237        goto L19
    238  L18:  param 400
    239        t52 = call malloc, 1
    240        t = t52
    241        t53 = t ptr+ 396
    242        *t53 = i
    243        t54 = t ptr+ 396
    244        t55 = *t54
    245        t56 = inttollong t55
    246        t57 = total llong+ t56
    247        total = t57
    248        param t
    249        call free, 1
    250        t58 = i int+ 1
    251        i = t58
    252        goto L17
    253  L19:  param "%lld\n"
    254        param total
    255        call printf, 2
    256        return 0


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
