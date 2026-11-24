============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t38_free_list.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 201 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION build(int)        (link name _Z5buildi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   head             local   struct Node *                   4       4
   i                local   int                             4       8
   p                local   struct Node *                   4      12
   t1               temp    void *                          4      16
   t2               temp    struct Node *                   4      20
   t3               temp    int                             4      24

 Code: 15 instruction(s)

    100       head = 0
    101       i = 1
    102  L1:  if i int<= n goto L2
    103       goto L3
    104  L2:  param 8
    105       t1 = call malloc, 1
    106       p = t1
    107       *p = i
    108       t2 = p ptr+ 4
    109       *t2 = head
    110       head = p
    111       t3 = i int+ 1
    112       i = t3
    113       goto L1
    114  L3:  return head

============================================================================
 FUNCTION total(struct Node *)        (link name _Z5totalP4Node)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   struct Node *                   4       0
   s                local   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    struct Node *                   4      16
   t4               temp    struct Node *                   4      20

 Code: 11 instruction(s)

    115       s = 0
    116  L4:  if p ptr!= 0 goto L5
    117       goto L6
    118  L5:  t1 = *p
    119       t2 = s int+ t1
    120       s = t2
    121       t3 = p ptr+ 4
    122       t4 = *t3
    123       p = t4
    124       goto L4
    125  L6:  return s

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

 Code: 10 instruction(s)

    126  L7:  if p ptr!= 0 goto L8
    127       goto L9
    128  L8:  t1 = p ptr+ 4
    129       t2 = *t1
    130       n = t2
    131       param p
    132       call free, 1
    133       p = n
    134       goto L7
    135  L9:  return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 49 temporaries, frame 260 bytes

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
   t8               temp    int *                           4      84
   t9               temp    int                             4      88
   t10              temp    int                             4      92
   t11              temp    long long                       8      96
   t12              temp    long long                       8     104
   t13              temp    int                             4     112
   t14              temp    struct Node *                   4     116
   t15              temp    int                             4     120
   t16              temp    struct Node *                   4     124
   t17              temp    int                             4     128
   t18              temp    void *                          4     132
   t19              temp    int                             4     136
   t20              temp    int *                           4     140
   t21              temp    int                             4     144
   t22              temp    void *                          4     148
   t23              temp    int                             4     152
   t24              temp    int *                           4     156
   t25              temp    int                             4     160
   t26              temp    int                             4     164
   t27              temp    int                             4     168
   t28              temp    unsigned int                    4     172
   t29              temp    void *                          4     176
   t30              temp    int                             4     180
   t31              temp    int *                           4     184
   t32              temp    int                             4     188
   t33              temp    int                             4     192
   t34              temp    unsigned int                    4     196
   t35              temp    void *                          4     200
   t36              temp    int                             4     204
   t37              temp    int                             4     208
   t38              temp    int *                           4     212
   t39              temp    int                             4     216
   t40              temp    int                             4     220
   t41              temp    int                             4     224
   t42              temp    int *                           4     228
   t43              temp    int                             4     232
   t44              temp    int                             4     236
   t45              temp    int                             4     240
   t46              temp    unsigned int                    4     244
   t47              temp    void *                          4     248
   t48              temp    int *                           4     252
   t49              temp    int                             4     256

 Code: 165 instruction(s)

    136        param 1000
    137        t1 = call malloc, 1
    138        a = t1
    139        *a = 120
    140        param a
    141        call free, 1
    142        param 1000
    143        t2 = call malloc, 1
    144        b = t2
    145        if a ptr== b goto L10
    146        t3 = 0
    147        goto L11
    148  L10:  t3 = 1
    149  L11:  param "reused %d\n"
    150        param t3
    151        call printf, 2
    152        param b
    153        call free, 1
    154        sum = 0
    155        i = 0
    156  L12:  if i int< 50000 goto L13
    157        goto L14
    158  L13:  param 300
    159        t4 = call malloc, 1
    160        p = t4
    161        *p = i
    162        t5 = i int* 2
    163        t6 = p ptr+ 296
    164        *t6 = t5
    165        t7 = *p
    166        t8 = p ptr+ 296
    167        t9 = *t8
    168        t10 = t7 int+ t9
    169        t11 = inttollong t10
    170        t12 = sum llong+ t11
    171        sum = t12
    172        param p
    173        call free, 1
    174        t13 = i int+ 1
    175        i = t13
    176        goto L12
    177  L14:  param "loop %lld\n"
    178        param sum
    179        call printf, 2
    180        param 100
    181        t14 = call build(int), 1
    182        list = t14
    183        param list
    184        t15 = call total(struct Node *), 1
    185        param "list %d\n"
    186        param t15
    187        call printf, 2
    188        param list
    189        call release(struct Node *), 1
    190        param 200
    191        t16 = call build(int), 1
    192        list = t16
    193        param list
    194        t17 = call total(struct Node *), 1
    195        param "list %d\n"
    196        param t17
    197        call printf, 2
    198        param list
    199        call release(struct Node *), 1
    200        param 64
    201        t18 = call malloc, 1
    202        dirty = t18
    203        k = 0
    204  L15:  if k int< 16 goto L16
    205        goto L17
    206  L16:  t19 = k int* 4
    207        t20 = dirty ptr+ t19
    208        *t20 = 99
    209        t21 = k int+ 1
    210        k = t21
    211        goto L15
    212  L17:  param dirty
    213        call free, 1
    214        param 16
    215        param 4
    216        t22 = call calloc, 2
    217        clean = t22
    218        nonzero = 0
    219        k = 0
    220  L18:  if k int< 16 goto L19
    221        goto L22
    222  L19:  t23 = k int* 4
    223        t24 = clean ptr+ t23
    224        t25 = *t24
    225        if t25 int!= 0 goto L20
    226        goto L21
    227  L20:  t26 = nonzero int+ 1
    228        nonzero = t26
    229  L21:  t27 = k int+ 1
    230        k = t27
    231        goto L18
    232  L22:  param "calloc %d\n"
    233        param nonzero
    234        call printf, 2
    235        param clean
    236        call free, 1
    237        t28 = 4 uint* 4
    238        param t28
    239        t29 = call malloc, 1
    240        grow = t29
    241        n = 4
    242        k = 0
    243  L23:  if k int< 4 goto L24
    244        goto L25
    245  L24:  t30 = k int* 4
    246        t31 = grow ptr+ t30
    247        *t31 = k
    248        t32 = k int+ 1
    249        k = t32
    250        goto L23
    251  L25:  if n int< 64 goto L26
    252        goto L30
    253  L26:  t33 = 2 int* n
    254        t34 = t33 uint* 4
    255        param grow
    256        param t34
    257        t35 = call realloc, 2
    258        grow = t35
    259        k = n
    260  L27:  t36 = 2 int* n
    261        if k int< t36 goto L28
    262        goto L29
    263  L28:  t37 = k int* 4
    264        t38 = grow ptr+ t37
    265        *t38 = k
    266        t39 = k int+ 1
    267        k = t39
    268        goto L27
    269  L29:  t40 = 2 int* n
    270        n = t40
    271        goto L25
    272  L30:  gsum = 0
    273        k = 0
    274  L31:  if k int< n goto L32
    275        goto L33
    276  L32:  t41 = k int* 4
    277        t42 = grow ptr+ t41
    278        t43 = *t42
    279        t44 = gsum int+ t43
    280        gsum = t44
    281        t45 = k int+ 1
    282        k = t45
    283        goto L31
    284  L33:  t46 = 8 uint* 4
    285        param grow
    286        param t46
    287        t47 = call realloc, 2
    288        grow = t47
    289        t48 = grow ptr+ 28
    290        t49 = *t48
    291        param "realloc %d %d %d\n"
    292        param n
    293        param gsum
    294        param t49
    295        call printf, 4
    296        param grow
    297        call free, 1
    298        param 0
    299        call free, 1
    300        return 0


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
