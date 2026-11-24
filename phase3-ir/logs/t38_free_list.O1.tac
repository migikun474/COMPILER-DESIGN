============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t38_free_list.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 201 -> 169 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          201 -> 169   (15% fewer)

   constants folded                        2
   algebraic simplifications              10
   common subexpressions                   2
   copies / constants forwarded           23
   temporaries merged away                17
   dead instructions removed               4
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

 Code: 139 instruction(s)

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
    169        param 100
    170        t14 = call build(int), 1
    171        list = t14
    172        param t14
    173        t15 = call total(struct Node *), 1
    174        param "list %d\n"
    175        param t15
    176        call printf, 2
    177        param t14
    178        call release(struct Node *), 1
    179        param 200
    180        t16 = call build(int), 1
    181        list = t16
    182        param t16
    183        t17 = call total(struct Node *), 1
    184        param "list %d\n"
    185        param t17
    186        call printf, 2
    187        param t16
    188        call release(struct Node *), 1
    189        param 64
    190        dirty = call malloc, 1
    191        k = 0
    192  L11:  if k int>= 16 goto L12
    193        t19 = k int<< 2
    194        t20 = dirty ptr+ t19
    195        *t20 = 99
    196        k = k int+ 1
    197        goto L11
    198  L12:  param dirty
    199        call free, 1
    200        param 16
    201        param 4
    202        clean = call calloc, 2
    203        nonzero = 0
    204        k = 0
    205  L13:  if k int>= 16 goto L15
    206        t23 = k int<< 2
    207        t24 = clean ptr+ t23
    208        t25 = *t24
    209        if t25 int== 0 goto L14
    210        nonzero = nonzero int+ 1
    211  L14:  k = k int+ 1
    212        goto L13
    213  L15:  param "calloc %d\n"
    214        param nonzero
    215        call printf, 2
    216        param clean
    217        call free, 1
    218        param 16
    219        grow = call malloc, 1
    220        n = 4
    221        k = 0
    222  L16:  if k int>= 4 goto L17
    223        t30 = k int<< 2
    224        t31 = grow ptr+ t30
    225        *t31 = k
    226        k = k int+ 1
    227        goto L16
    228  L17:  if n int>= 64 goto L20
    229        t33 = n int<< 1
    230        t34 = t33 uint<< 2
    231        param grow
    232        param t34
    233        grow = call realloc, 2
    234        k = n
    235  L18:  t36 = n int<< 1
    236        if k int>= t36 goto L19
    237        t37 = k int<< 2
    238        t38 = grow ptr+ t37
    239        *t38 = k
    240        k = k int+ 1
    241        goto L18
    242  L19:  n = n int<< 1
    243        goto L17
    244  L20:  gsum = 0
    245        k = 0
    246  L21:  if k int>= n goto L22
    247        t41 = k int<< 2
    248        t42 = grow ptr+ t41
    249        t43 = *t42
    250        gsum = gsum int+ t43
    251        k = k int+ 1
    252        goto L21
    253  L22:  param grow
    254        param 32
    255        t47 = call realloc, 2
    256        grow = t47
    257        t48 = t47 ptr+ 28
    258        t49 = *t48
    259        param "realloc %d %d %d\n"
    260        param n
    261        param gsum
    262        param t49
    263        call printf, 4
    264        param t47
    265        call free, 1
    266        param 0
    267        call free, 1
    268        return 0


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
