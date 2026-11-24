============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t09_memory.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 157 -> 121 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          157 -> 121   (22% fewer)

   constants folded                        4
   algebraic simplifications               3
   common subexpressions                  10
   copies / constants forwarded           31
   temporaries merged away                 7
   dead instructions removed              14
   jumps removed or redirected             6
   unreachable instructions removed        0
   propagated across blocks                0
   dead assignments removed                9

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

 Code: 6 instruction(s)

    100     param 8
    101     t1 = call malloc, 1
    102     *t1 = v
    103     t2 = t1 ptr+ 4
    104     *t2 = h
    105     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 37 temporaries, frame 292 bytes

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
   (21 temporaries no longer used after optimization not shown)

 Code: 115 instruction(s)

    106        list = 0
    107        rev = 0
    108        i = 1
    109  L1:   if i int> 5 goto L2
    110        param list
    111        param i
    112        list = call push(struct Node *, int), 2
    113        i = i int+ 1
    114        goto L1
    115  L2:   if list ptr== 0 goto L3
    116        t3 = list ptr+ 4
    117        t4 = *t3
    118        *t3 = rev
    119        rev = list
    120        list = t4
    121        goto L2
    122  L3:   s = 0
    123        list = rev
    124  L4:   if list ptr== 0 goto L5
    125        t6 = s int* 10
    126        t7 = *list
    127        s = t6 int+ t7
    128        t9 = list ptr+ 4
    129        list = *t9
    130        goto L4
    131  L5:   param "%d\n"
    132        param s
    133        call printf, 2
    134  L6:   if rev ptr== 0 goto L7
    135        t11 = rev ptr+ 4
    136        t12 = *t11
    137        param rev
    138        call free, 1
    139        rev = t12
    140        goto L6
    141  L7:   param 12
    142        rows = call malloc, 1
    143        i = 0
    144  L8:   if i int>= 3 goto L9
    145        t15 = i int<< 2
    146        t16 = rows ptr+ t15
    147        param 4
    148        param 4
    149        t17 = call calloc, 2
    150        *t16 = t17
    151        t22 = t17 ptr+ t15
    152        t23 = i int+ 1
    153        *t22 = t23
    154        i = t23
    155        goto L8
    156  L9:   t25 = rows ptr+ 8
    157        t26 = *t25
    158        t27 = t26 ptr+ 8
    159        t28 = *t27
    160        t29 = rows ptr+ 4
    161        t30 = *t29
    162        t31 = *t30
    163        t32 = *rows
    164        t33 = *t32
    165        t36 = t30 ptr+ 4
    166        t37 = *t36
    167        t38 = t33 int+ t37
    168        param "%d %d %d\n"
    169        param t28
    170        param t31
    171        param t38
    172        call printf, 4
    173        param 8
    174        t40 = call malloc, 1
    175        *t40 = 11
    176        t41 = t40 ptr+ 4
    177        *t41 = 22
    178        param t40
    179        param 200
    180        t43 = call realloc, 2
    181        param t43
    182        param 8
    183        t45 = call realloc, 2
    184        t46 = *t45
    185        t47 = t45 ptr+ 4
    186        t48 = *t47
    187        param "%d %d\n"
    188        param t46
    189        param t48
    190        call printf, 3
    191        param 100
    192        t49 = call malloc, 1
    193        param t49
    194        call free, 1
    195        param 100
    196        t50 = call malloc, 1
    197        if t49 ptr== t50 goto L10
    198        t51 = 0
    199        goto L11
    200  L10:  t51 = 1
    201  L11:  param "%d\n"
    202        param t51
    203        call printf, 2
    204        total = 0
    205        i = 0
    206  L12:  if i int>= 30000 goto L13
    207        param 400
    208        t52 = call malloc, 1
    209        t53 = t52 ptr+ 396
    210        *t53 = i
    211        t56 = inttollong i
    212        total = total llong+ t56
    213        param t52
    214        call free, 1
    215        i = i int+ 1
    216        goto L12
    217  L13:  param "%lld\n"
    218        param total
    219        call printf, 2
    220        return 0


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
