=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t09_memory.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 151 -> 123 instruction(s) for 'test/t09_memory.c'.

optimization summary (-O2)
    instructions                151 -> 123   (18% fewer)
    constants folded            5
    algebraic simplifications   6
    common subexpressions       3
    copies / constants forwarded 29
    temporaries merged away     9
    dead instructions removed   8
    jumps removed or redirected 5
    unreachable instructions    0
    propagated across blocks    9
    dead assignments removed    6

function push(struct Node *, int)        link name: _Z4pushP4Nodei
  symbol table (name, kind, type, width, offset)
    head           param  struct Node *              4      0
    v              param  int                        4      4
    n              local  struct Node *              4      8
    t1             temp   void *                     4     12
    t2             temp   struct Node *              4     16
    total width 20
  code
 100:   param 8
 101:   t1 = call malloc, 1
 102:   *t1 = v
 103:   t2 = t1 ptr+ 4
 104:   *t2 = head
 105:   return t1

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    n              local  int                        4      0
    a              local  int *                      4      4
    i.6            local  int                        4      8
    z              local  int *                      4     12
    i.8            local  int                        4     16
    list           local  struct Node *              4     20
    i.10           local  int                        4     24
    sum            local  int                        4     28
    p              local  struct Node *              4     32
    dead           local  struct Node *              4     36
    d              local  double *                   4     40
    one            local  int *                      4     44
    text           local  char *                     4     48
    t1             temp   unsigned int               4     52
    t2             temp   void *                     4     56
    t3             temp   int                        4     60
    t4             temp   int *                      4     64
    t5             temp   int                        4     68
    t6             temp   int                        4     72
    t7             temp   void *                     4     76
    t8             temp   int *                      4     80
    t9             temp   int                        4     84
    t10            temp   int *                      4     88
    t11            temp   int                        4     92
    t12            temp   int                        4     96
    t13            temp   int *                      4    100
    t14            temp   int                        4    104
    t15            temp   unsigned int               4    108
    t16            temp   void *                     4    112
    t17            temp   int                        4    116
    t18            temp   int                        4    120
    t19            temp   int *                      4    124
    t20            temp   int                        4    128
    t21            temp   int                        4    132
    t22            temp   int *                      4    136
    t23            temp   int                        4    140
    t24            temp   int                        4    144
    t25            temp   int                        4    148
    t26            temp   int *                      4    152
    t27            temp   int                        4    156
    t28            temp   int *                      4    160
    t29            temp   int                        4    164
    t30            temp   int *                      4    168
    t31            temp   int                        4    172
    t32            temp   int                        4    176
    t33            temp   int                        4    180
    t34            temp   struct Node *              4    184
    t35            temp   int                        4    188
    t36            temp   int                        4    192
    t37            temp   int                        4    196
    t38            temp   struct Node *              4    200
    t39            temp   struct Node *              4    204
    t40            temp   struct Node *              4    208
    t41            temp   struct Node *              4    212
    t42            temp   int                        4    216
    t43            temp   struct Node *              4    220
    t44            temp   struct Node *              4    224
    t45            temp   unsigned int               4    228
    t46            temp   void *                     4    232
    t47            temp   double *                   4    236
    t48            temp   double                     8    240
    t49            temp   double *                   4    248
    t50            temp   double                     8    256
    t51            temp   double                     8    264
    t52            temp   double *                   4    272
    t53            temp   void *                     4    276
    t54            temp   void *                     4    280
    t55            temp   char *                     4    284
    t56            temp   char *                     4    288
    t57            temp   double *                   4    292
    t58            temp   double                     8    296
    t59            temp   int                        4    304
    t60            temp   int                        4    308
    total width 312
  code
 106:      param 20
 107:      a = call malloc, 1
 108:      i.6 = 0
 109: L1:  if i.6 int>= 5 goto L2
 110:      t3 = i.6 int<< 2
 111:      t4 = a ptr+ t3
 112:      t5 = i.6 int* i.6
 113:      *t4 = t5
 114:      i.6 = i.6 int+ 1
 115:      goto L1
 116: L2:  param 5
 117:      param 4
 118:      t7 = call calloc, 2
 119:      t8 = a ptr+ 16
 120:      t9 = *t8
 121:      t10 = t7 ptr+ 4
 122:      t11 = *t10
 123:      t12 = t9 int+ t11
 124:      t13 = t7 ptr+ 8
 125:      *t13 = t12
 126:      param a
 127:      param 40
 128:      a = call realloc, 2
 129:      i.8 = 5
 130: L3:  if i.8 int>= 10 goto L4
 131:      t18 = i.8 int<< 2
 132:      t19 = a ptr+ t18
 133:      t20 = i.8 int- 5
 134:      t21 = t20 int<< 2
 135:      t22 = a ptr+ t21
 136:      t23 = *t22
 137:      t24 = t23 int+ 100
 138:      *t19 = t24
 139:      i.8 = i.8 int+ 1
 140:      goto L3
 141: L4:  t26 = a ptr+ 16
 142:      t27 = *t26
 143:      t28 = a ptr+ 36
 144:      t29 = *t28
 145:      t30 = t7 ptr+ 8
 146:      t31 = *t30
 147:      t32 = *t7
 148:      param "%d %d %d %d\n"
 149:      param t27
 150:      param t29
 151:      param t31
 152:      param t32
 153:      call printf, 5
 154:      list = 0
 155:      i.10 = 1
 156: L5:  if i.10 int> 4 goto L6
 157:      t33 = i.10 int* 10
 158:      param list
 159:      param t33
 160:      list = call push(struct Node *, int), 2
 161:      i.10 = i.10 int+ 1
 162:      goto L5
 163: L6:  sum = 0
 164:      p = list
 165: L7:  if p ptr== 0 goto L8
 166:      t36 = *p
 167:      sum = sum int+ t36
 168:      t38 = p ptr+ 4
 169:      p = *t38
 170:      goto L7
 171: L8:  t40 = list ptr+ 4
 172:      t41 = *t40
 173:      t42 = *t41
 174:      param "%d %d\n"
 175:      param sum
 176:      param t42
 177:      call printf, 3
 178: L9:  if list ptr== 0 goto L10
 179:      dead = list
 180:      t43 = list ptr+ 4
 181:      list = *t43
 182:      param dead
 183:      call free, 1
 184:      goto L9
 185: L10: param 24
 186:      t46 = call malloc, 1
 187:      *t46 = 1.5
 188:      t47 = t46 ptr+ 8
 189:      *t47 = 2.5
 190:      t48 = *t46
 191:      t51 = t48 double+ 2.5
 192:      t52 = t46 ptr+ 16
 193:      *t52 = t51
 194:      param 4
 195:      t53 = call malloc, 1
 196:      *t53 = 42
 197:      param 8
 198:      t54 = call malloc, 1
 199:      *t54 = 111
 200:      t55 = t54 ptr+ 1
 201:      *t55 = 107
 202:      t56 = t54 ptr+ 2
 203:      *t56 = 0
 204:      t58 = *t52
 205:      t59 = *t53
 206:      param "%.1f %d %s\n"
 207:      param t58
 208:      param t59
 209:      param t54
 210:      call printf, 4
 211:      param t46
 212:      call free, 1
 213:      param t53
 214:      call free, 1
 215:      param t54
 216:      call free, 1
 217:      param a
 218:      call free, 1
 219:      param t7
 220:      call free, 1
 221:      t60 = sum int/ 10
 222:      return t60


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Node               struct_tag     struct Node                -        global                         6     -     0     Node                 -                        size 8
Node::value        field          int                        member   global > struct Node           6     4     3     Node::value          -                        public, offset 0
Node::next         field          struct Node *              member   global > struct Node           6     4     4     Node::next           -                        public, offset 4
push               function       struct Node *(struct Node *, int) -        global                         8     -     1     _Z4pushP4Nodei       _Z4pushP4Nodei           defined
head               parameter      struct Node *              param    global > push()                8     4     1     head.1               -                        
v                  parameter      int                        param    global > push()                8     4     1     v.2                  -                        
n                  variable       struct Node *              local    global > push()                9     4     3     n.3                  -                        
main               function       int (void)                 -        global                         15    -     0     main                 main                     defined
n                  variable       int                        local    global > main()                16    4     7     n.4                  -                        
a                  variable       int *                      local    global > main()                17    4     9     a.5                  -                        
i                  variable       int                        local    global > main() > for          18    4     5     i.6                  -                        
z                  variable       int *                      local    global > main()                19    4     5     z.7                  -                        
i                  variable       int                        local    global > main() > for          22    4     4     i.8                  -                        
list               variable       struct Node *              local    global > main()                25    4     8     list.9               -                        
i                  variable       int                        local    global > main() > for          26    4     3     i.10                 -                        
sum                variable       int                        local    global > main()                27    4     3     sum.11               -                        
p                  variable       struct Node *              local    global > main() > for          28    4     4     p.12                 -                        
dead               variable       struct Node *              local    global > main() > while        31    4     1     dead.13              -                        
d                  variable       double *                   local    global > main()                36    4     7     d.14                 -                        
one                variable       int *                      local    global > main()                38    4     3     one.15               -                        
text               variable       char *                     local    global > main()                40    4     5     text.16              -                        

=== Record Layouts ===
struct Node: size 8, align 4
    +0  int value  [public]
    +4  struct Node * next  [public]
