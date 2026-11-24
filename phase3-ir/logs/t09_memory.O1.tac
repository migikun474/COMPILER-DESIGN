============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t09_memory.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 157 -> 130 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          157 -> 130   (17% fewer)

   constants folded                        4
   algebraic simplifications               3
   common subexpressions                  10
   copies / constants forwarded           31
   temporaries merged away                 7
   dead instructions removed              14
   jumps removed or redirected             6
   unreachable instructions removed        0

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
    103     *t1 = v
    104     t2 = t1 ptr+ 4
    105     *t2 = h
    106     return t1

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

 Code: 123 instruction(s)

    107        list = 0
    108        rev = 0
    109        i = 1
    110  L1:   if i int> 5 goto L2
    111        param list
    112        param i
    113        list = call push(struct Node *, int), 2
    114        i = i int+ 1
    115        goto L1
    116  L2:   if list ptr== 0 goto L3
    117        t3 = list ptr+ 4
    118        t4 = *t3
    119        n.7 = t4
    120        *t3 = rev
    121        rev = list
    122        list = t4
    123        goto L2
    124  L3:   s = 0
    125        list = rev
    126  L4:   if list ptr== 0 goto L5
    127        t6 = s int* 10
    128        t7 = *list
    129        s = t6 int+ t7
    130        t9 = list ptr+ 4
    131        list = *t9
    132        goto L4
    133  L5:   param "%d\n"
    134        param s
    135        call printf, 2
    136  L6:   if rev ptr== 0 goto L7
    137        t11 = rev ptr+ 4
    138        t12 = *t11
    139        n.9 = t12
    140        param rev
    141        call free, 1
    142        rev = t12
    143        goto L6
    144  L7:   param 12
    145        rows = call malloc, 1
    146        i = 0
    147  L8:   if i int>= 3 goto L9
    148        t15 = i int<< 2
    149        t16 = rows ptr+ t15
    150        param 4
    151        param 4
    152        t17 = call calloc, 2
    153        *t16 = t17
    154        t22 = t17 ptr+ t15
    155        t23 = i int+ 1
    156        *t22 = t23
    157        i = t23
    158        goto L8
    159  L9:   t25 = rows ptr+ 8
    160        t26 = *t25
    161        t27 = t26 ptr+ 8
    162        t28 = *t27
    163        t29 = rows ptr+ 4
    164        t30 = *t29
    165        t31 = *t30
    166        t32 = *rows
    167        t33 = *t32
    168        t36 = t30 ptr+ 4
    169        t37 = *t36
    170        t38 = t33 int+ t37
    171        param "%d %d %d\n"
    172        param t28
    173        param t31
    174        param t38
    175        call printf, 4
    176        param 8
    177        t40 = call malloc, 1
    178        g = t40
    179        *t40 = 11
    180        t41 = t40 ptr+ 4
    181        *t41 = 22
    182        param t40
    183        param 200
    184        t43 = call realloc, 2
    185        g = t43
    186        param t43
    187        param 8
    188        t45 = call realloc, 2
    189        g = t45
    190        t46 = *t45
    191        t47 = t45 ptr+ 4
    192        t48 = *t47
    193        param "%d %d\n"
    194        param t46
    195        param t48
    196        call printf, 3
    197        param 100
    198        t49 = call malloc, 1
    199        a = t49
    200        param t49
    201        call free, 1
    202        param 100
    203        t50 = call malloc, 1
    204        b = t50
    205        if t49 ptr== t50 goto L10
    206        t51 = 0
    207        goto L11
    208  L10:  t51 = 1
    209  L11:  param "%d\n"
    210        param t51
    211        call printf, 2
    212        total = 0
    213        i = 0
    214  L12:  if i int>= 30000 goto L13
    215        param 400
    216        t52 = call malloc, 1
    217        t = t52
    218        t53 = t52 ptr+ 396
    219        *t53 = i
    220        t56 = inttollong i
    221        total = total llong+ t56
    222        param t52
    223        call free, 1
    224        i = i int+ 1
    225        goto L12
    226  L13:  param "%lld\n"
    227        param total
    228        call printf, 2
    229        return 0


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
