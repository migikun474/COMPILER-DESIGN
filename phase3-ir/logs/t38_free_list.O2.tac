============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t38_free_list.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 201 -> 161 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                          201 -> 161   (19% fewer)

   constants folded                        2
   algebraic simplifications              10
   common subexpressions                   2
   copies / constants forwarded           23
   temporaries merged away                17
   dead instructions removed               4
   jumps removed or redirected            11
   unreachable instructions removed        0
   propagated across blocks                1
   dead assignments removed                8

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

 Code: 12 instruction(s)

    100       head = 0
    101       i = 1
    102  L1:  if i int> n goto L2
    103       param 8
    104       t1 = call malloc, 1
    105       *t1 = i
    106       t2 = t1 ptr+ 4
    107       *t2 = head
    108       head = t1
    109       i = i int+ 1
    110       goto L1
    111  L2:  return head

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

    112       s = 0
    113  L3:  if p ptr== 0 goto L4
    114       t1 = *p
    115       s = s int+ t1
    116       t3 = p ptr+ 4
    117       p = *t3
    118       goto L3
    119  L4:  return s

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

 Code: 8 instruction(s)

    120  L5:  if p ptr== 0 goto L6
    121       t1 = p ptr+ 4
    122       t2 = *t1
    123       param p
    124       call free, 1
    125       p = t2
    126       goto L5
    127  L6:  return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 31 temporaries, frame 260 bytes

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
   t15              temp    int                             4     120
   t16              temp    struct Node *                   4     124
   t17              temp    int                             4     128
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
   (18 temporaries no longer used after optimization not shown)

 Code: 133 instruction(s)

    128        param 1000
    129        t1 = call malloc, 1
    130        *t1 = 120
    131        param t1
    132        call free, 1
    133        param 1000
    134        t2 = call malloc, 1
    135        if t1 ptr== t2 goto L7
    136        t3 = 0
    137        goto L8
    138  L7:   t3 = 1
    139  L8:   param "reused %d\n"
    140        param t3
    141        call printf, 2
    142        param t2
    143        call free, 1
    144        sum = 0
    145        i = 0
    146  L9:   if i int>= 50000 goto L10
    147        param 300
    148        t4 = call malloc, 1
    149        *t4 = i
    150        t5 = i int<< 1
    151        t6 = t4 ptr+ 296
    152        *t6 = t5
    153        t7 = *t4
    154        t10 = t7 int+ t5
    155        t11 = inttollong t10
    156        sum = sum llong+ t11
    157        param t4
    158        call free, 1
    159        i = i int+ 1
    160        goto L9
    161  L10:  param "loop %lld\n"
    162        param sum
    163        call printf, 2
    164        param 100
    165        t14 = call build(int), 1
    166        param t14
    167        t15 = call total(struct Node *), 1
    168        param "list %d\n"
    169        param t15
    170        call printf, 2
    171        param t14
    172        call release(struct Node *), 1
    173        param 200
    174        t16 = call build(int), 1
    175        param t16
    176        t17 = call total(struct Node *), 1
    177        param "list %d\n"
    178        param t17
    179        call printf, 2
    180        param t16
    181        call release(struct Node *), 1
    182        param 64
    183        dirty = call malloc, 1
    184        k = 0
    185  L11:  if k int>= 16 goto L12
    186        t19 = k int<< 2
    187        t20 = dirty ptr+ t19
    188        *t20 = 99
    189        k = k int+ 1
    190        goto L11
    191  L12:  param dirty
    192        call free, 1
    193        param 16
    194        param 4
    195        clean = call calloc, 2
    196        nonzero = 0
    197        k = 0
    198  L13:  if k int>= 16 goto L15
    199        t23 = k int<< 2
    200        t24 = clean ptr+ t23
    201        t25 = *t24
    202        if t25 int== 0 goto L14
    203        nonzero = nonzero int+ 1
    204  L14:  k = k int+ 1
    205        goto L13
    206  L15:  param "calloc %d\n"
    207        param nonzero
    208        call printf, 2
    209        param clean
    210        call free, 1
    211        param 16
    212        grow = call malloc, 1
    213        n = 4
    214        k = 0
    215  L16:  if k int>= 4 goto L17
    216        t30 = k int<< 2
    217        t31 = grow ptr+ t30
    218        *t31 = k
    219        k = k int+ 1
    220        goto L16
    221  L17:  if n int>= 64 goto L20
    222        t33 = n int<< 1
    223        t34 = t33 uint<< 2
    224        param grow
    225        param t34
    226        grow = call realloc, 2
    227        k = n
    228  L18:  t36 = n int<< 1
    229        if k int>= t36 goto L19
    230        t37 = k int<< 2
    231        t38 = grow ptr+ t37
    232        *t38 = k
    233        k = k int+ 1
    234        goto L18
    235  L19:  n = n int<< 1
    236        goto L17
    237  L20:  gsum = 0
    238        k = 0
    239  L21:  if k int>= n goto L22
    240        t41 = k int<< 2
    241        t42 = grow ptr+ t41
    242        t43 = *t42
    243        gsum = gsum int+ t43
    244        k = k int+ 1
    245        goto L21
    246  L22:  param grow
    247        param 32
    248        t47 = call realloc, 2
    249        t48 = t47 ptr+ 28
    250        t49 = *t48
    251        param "realloc %d %d %d\n"
    252        param n
    253        param gsum
    254        param t49
    255        call printf, 4
    256        param t47
    257        call free, 1
    258        param 0
    259        call free, 1
    260        return 0


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
