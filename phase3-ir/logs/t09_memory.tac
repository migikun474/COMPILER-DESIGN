=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t09_memory.c
Optimization : no optimization

Three address code generated: 2 function(s), 151 instruction(s) for 'test/t09_memory.c'.

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
 102:   n = t1
 103:   *n = v
 104:   t2 = n ptr+ 4
 105:   *t2 = head
 106:   return n

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
 107:      n = 5
 108:      t1 = n uint* 4
 109:      param t1
 110:      t2 = call malloc, 1
 111:      a = t2
 112:      i.6 = 0
 113: L1:  if i.6 int< n goto L2
 114:      goto L3
 115: L2:  t3 = i.6 int* 4
 116:      t4 = a ptr+ t3
 117:      t5 = i.6 int* i.6
 118:      *t4 = t5
 119:      t6 = i.6 int+ 1
 120:      i.6 = t6
 121:      goto L1
 122: L3:  param n
 123:      param 4
 124:      t7 = call calloc, 2
 125:      z = t7
 126:      t8 = a ptr+ 16
 127:      t9 = *t8
 128:      t10 = z ptr+ 4
 129:      t11 = *t10
 130:      t12 = t9 int+ t11
 131:      t13 = z ptr+ 8
 132:      *t13 = t12
 133:      t14 = 2 int* n
 134:      t15 = t14 uint* 4
 135:      param a
 136:      param t15
 137:      t16 = call realloc, 2
 138:      a = t16
 139:      i.8 = n
 140: L4:  t17 = 2 int* n
 141:      if i.8 int< t17 goto L5
 142:      goto L6
 143: L5:  t18 = i.8 int* 4
 144:      t19 = a ptr+ t18
 145:      t20 = i.8 int- n
 146:      t21 = t20 int* 4
 147:      t22 = a ptr+ t21
 148:      t23 = *t22
 149:      t24 = t23 int+ 100
 150:      *t19 = t24
 151:      t25 = i.8 int+ 1
 152:      i.8 = t25
 153:      goto L4
 154: L6:  t26 = a ptr+ 16
 155:      t27 = *t26
 156:      t28 = a ptr+ 36
 157:      t29 = *t28
 158:      t30 = z ptr+ 8
 159:      t31 = *t30
 160:      t32 = *z
 161:      param "%d %d %d %d\n"
 162:      param t27
 163:      param t29
 164:      param t31
 165:      param t32
 166:      call printf, 5
 167:      list = 0
 168:      i.10 = 1
 169: L7:  if i.10 int<= 4 goto L8
 170:      goto L9
 171: L8:  t33 = i.10 int* 10
 172:      param list
 173:      param t33
 174:      t34 = call push(struct Node *, int), 2
 175:      list = t34
 176:      t35 = i.10 int+ 1
 177:      i.10 = t35
 178:      goto L7
 179: L9:  sum = 0
 180:      p = list
 181: L10: if p ptr!= 0 goto L11
 182:      goto L12
 183: L11: t36 = *p
 184:      t37 = sum int+ t36
 185:      sum = t37
 186:      t38 = p ptr+ 4
 187:      t39 = *t38
 188:      p = t39
 189:      goto L10
 190: L12: t40 = list ptr+ 4
 191:      t41 = *t40
 192:      t42 = *t41
 193:      param "%d %d\n"
 194:      param sum
 195:      param t42
 196:      call printf, 3
 197: L13: if list ptr!= 0 goto L14
 198:      goto L15
 199: L14: dead = list
 200:      t43 = list ptr+ 4
 201:      t44 = *t43
 202:      list = t44
 203:      param dead
 204:      call free, 1
 205:      goto L13
 206: L15: t45 = 3 uint* 8
 207:      param t45
 208:      t46 = call malloc, 1
 209:      d = t46
 210:      *d = 1.5
 211:      t47 = d ptr+ 8
 212:      *t47 = 2.5
 213:      t48 = *d
 214:      t49 = d ptr+ 8
 215:      t50 = *t49
 216:      t51 = t48 double+ t50
 217:      t52 = d ptr+ 16
 218:      *t52 = t51
 219:      param 4
 220:      t53 = call malloc, 1
 221:      one = t53
 222:      *one = 42
 223:      param 8
 224:      t54 = call malloc, 1
 225:      text = t54
 226:      *text = 111
 227:      t55 = text ptr+ 1
 228:      *t55 = 107
 229:      t56 = text ptr+ 2
 230:      *t56 = 0
 231:      t57 = d ptr+ 16
 232:      t58 = *t57
 233:      t59 = *one
 234:      param "%.1f %d %s\n"
 235:      param t58
 236:      param t59
 237:      param text
 238:      call printf, 4
 239:      param d
 240:      call free, 1
 241:      param one
 242:      call free, 1
 243:      param text
 244:      call free, 1
 245:      param a
 246:      call free, 1
 247:      param z
 248:      call free, 1
 249:      t60 = sum int/ 10
 250:      return t60


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
