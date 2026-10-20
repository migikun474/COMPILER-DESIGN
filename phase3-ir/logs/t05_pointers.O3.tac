=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t05_pointers.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 188 -> 157 instruction(s) for 'test/t05_pointers.c'.

optimization summary (-O3)
    instructions                188 -> 157   (16% fewer)
    constants folded            3
    algebraic simplifications   0
    common subexpressions       8
    copies / constants forwarded 43
    temporaries merged away     5
    dead instructions removed   16
    jumps removed or redirected 3
    unreachable instructions    0
    propagated across blocks    4
    dead assignments removed    16
    calls inlined               2
    tail calls turned to jumps  0
    common across blocks        5
    moved out of loops          0

function swap(int *, int *)        link name: _Z4swapPiS_
  symbol table (name, kind, type, width, offset)
    a              param  int *                      4      0
    b              param  int *                      4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    total width 20
  code
 100:   t1 = *a
 101:   t2 = *b
 102:   *a = t2
 103:   *b = t1
 104:   return

function sum(int *, int *)        link name: _Z3sumPiS_
  symbol table (name, kind, type, width, offset)
    first          param  int *                      4      0
    last           param  int *                      4      4
    s              local  int                        4      8
    t1             temp   int *                      4     12
    t2             temp   int *                      4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    total width 28
  code
 105:     s = 0
 106: L1: if first ptr>= last goto L2
 107:     t1 = first
 108:     first = first ptr+ 4
 109:     t3 = *t1
 110:     s = s int+ t3
 111:     goto L1
 112: L2: return s

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    x              local  int                        4      0
    y              local  int                        4      4
    p              local  int *                      4      8
    pp             local  int **                     4     12
    ppp            local  int ***                    4     16
    arr            local  int[5]                    20     20
    q              local  int *                      4     40
    gap            local  int                        4     44
    raw            local  void *                     4     48
    back           local  int *                      4     52
    bytes          local  char *                     4     56
    grid           local  int[2][3]                 24     60
    row            local  int (*)[3]                 4     84
    d              local  double                     8     88
    dp             local  double *                   4     96
    text           local  char[8]                    8    100
    t              local  char *                     4    108
    t1             temp   int *                      4    112
    t2             temp   int **                     4    116
    t3             temp   int ***                    4    120
    t4             temp   int                        4    124
    t5             temp   int *                      4    128
    t6             temp   int                        4    132
    t7             temp   int **                     4    136
    t8             temp   int *                      4    140
    t9             temp   int                        4    144
    t10            temp   int *                      4    148
    t11            temp   int **                     4    152
    t12            temp   int *                      4    156
    t13            temp   int                        4    160
    t14            temp   int                        4    164
    t15            temp   int *                      4    168
    t16            temp   int *                      4    172
    t17            temp   int (*)[5]                 4    176
    t18            temp   int *                      4    180
    t19            temp   int *                      4    184
    t20            temp   int (*)[5]                 4    188
    t21            temp   int *                      4    192
    t22            temp   int                        4    196
    t23            temp   int                        4    200
    t24            temp   int                        4    204
    t25            temp   int (*)[5]                 4    208
    t26            temp   int (*)[5]                 4    212
    t27            temp   int *                      4    216
    t28            temp   int                        4    220
    t29            temp   int *                      4    224
    t30            temp   int *                      4    228
    t31            temp   int *                      4    232
    t32            temp   int                        4    236
    t33            temp   int                        4    240
    t34            temp   int                        4    244
    t35            temp   int *                      4    248
    t36            temp   int                        4    252
    t37            temp   int (*)[5]                 4    256
    t38            temp   int *                      4    260
    t39            temp   int                        4    264
    t40            temp   int                        4    268
    t41            temp   int (*)[5]                 4    272
    t42            temp   int *                      4    276
    t43            temp   int                        4    280
    t44            temp   int (*)[5]                 4    284
    t45            temp   int                        4    288
    t46            temp   int (*)[5]                 4    292
    t47            temp   int *                      4    296
    t48            temp   int *                      4    300
    t49            temp   int *                      4    304
    t50            temp   char                       1    308
    t51            temp   int                        4    312
    t52            temp   int (*)[2][3]              4    316
    t53            temp   int (*)[3]                 4    320
    t54            temp   int (*)[3]                 4    324
    t55            temp   int                        4    328
    t56            temp   int                        4    332
    t57            temp   int *                      4    336
    t58            temp   double *                   4    340
    t59            temp   double                     8    344
    t60            temp   double                     8    352
    t61            temp   char (*)[8]                4    360
    t62            temp   char                       1    364
    t63            temp   char *                     4    368
    t64            temp   char (*)[8]                4    372
    t65            temp   int                        4    376
    t66            temp   char *                     4    380
    t67            temp   char                       1    384
    t68            temp   int                        4    388
    t69            temp   int                        4    392
    t70            temp   int *                      4    396
    t71            temp   int *                      4    400
    t72            temp   int                        4    404
    t73            temp   int                        4    408
    t74            temp   int *                      4    412
    t75            temp   int *                      4    416
    t76            temp   int                        4    420
    t77            temp   int *                      4    424
    t78            temp   int                        4    428
    total width 432
  code
 113:      x = 5
 114:      y = 6
 115:      t1 = &x
 116:      p = t1
 117:      t2 = &p
 118:      pp = t2
 119:      t3 = &pp
 120:      t4 = *p
 121:      t5 = *t2
 122:      t6 = *t5
 123:      t7 = *t3
 124:      t8 = *t7
 125:      t9 = *t8
 126:      param "%d %d %d\n"
 127:      param t4
 128:      param t6
 129:      param t9
 130:      call printf, 4
 131:      t10 = *pp
 132:      *t10 = 9
 133:      t11 = *t3
 134:      t12 = *t11
 135:      t13 = *t12
 136:      t14 = t13 int+ 1
 137:      *t12 = t14
 138:      t16 = &y
 139:      t72 = *t1
 140:      t73 = *t16
 141:      *t1 = t73
 142:      *t16 = t72
 143:      param "%d %d\n"
 144:      param x
 145:      param y
 146:      call printf, 3
 147:      arr[0] = 10
 148:      arr[4] = 20
 149:      arr[8] = 30
 150:      arr[12] = 40
 151:      arr[16] = 50
 152:      t17 = &arr
 153:      t18 = t17 ptr+ 8
 154:      t19 = t18 ptr- 4
 155:      t21 = t17 ptr+ 16
 156:      t22 = t21 ptr- t19
 157:      t23 = t22 int/ 4
 158:      t24 = *t19
 159:      t27 = t17 ptr+ 20
 160:      t74 = t17
 161:      t76 = 0
 162: L3:  if t74 ptr>= t27 goto L4
 163:      t77 = t74
 164:      t74 = t74 ptr+ 4
 165:      t78 = *t77
 166:      t76 = t76 int+ t78
 167:      goto L3
 168: L4:  param "%d %d %d\n"
 169:      param t24
 170:      param t23
 171:      param t76
 172:      call printf, 4
 173:      t29 = t19 ptr+ 4
 174:      t30 = t29 ptr- 4
 175:      t31 = t30 ptr+ 8
 176:      t32 = *t31
 177:      t35 = t31 ptr+ -4
 178:      t36 = *t35
 179:      t39 = *t21
 180:      param "%d %d %d\n"
 181:      param t32
 182:      param t36
 183:      param t39
 184:      call printf, 4
 185:      t42 = t17 ptr+ 12
 186:      if t31 ptr== t42 goto L5
 187:      t40 = 0
 188:      goto L6
 189: L5:  t40 = 1
 190: L6:  if t31 ptr!= t17 goto L7
 191:      t43 = 0
 192:      goto L8
 193: L7:  t43 = 1
 194: L8:  if t31 ptr< t21 goto L9
 195:      t45 = 0
 196:      goto L10
 197: L9:  t45 = 1
 198: L10: param "%d %d %d\n"
 199:      param t40
 200:      param t43
 201:      param t45
 202:      call printf, 4
 203:      *t1 = 258
 204:      t50 = *t16
 205:      t51 = chartoint t50
 206:      param "%d %d\n"
 207:      param x
 208:      param t51
 209:      call printf, 3
 210:      grid[0] = 1
 211:      grid[4] = 2
 212:      grid[8] = 3
 213:      grid[12] = 4
 214:      grid[16] = 5
 215:      grid[20] = 6
 216:      t52 = &grid
 217:      t53 = t52 ptr+ 12
 218:      t54 = t53 ptr+ 8
 219:      t55 = *t54
 220:      t56 = *t53
 221:      param "%d %d\n"
 222:      param t55
 223:      param t56
 224:      call printf, 3
 225:      p = 0
 226:      p = t16
 227:      d = 2.5
 228:      t58 = &d
 229:      t59 = *t58
 230:      t60 = t59 double* 2.0
 231:      *t58 = t60
 232:      text[0] = 112
 233:      text[1] = 111
 234:      text[2] = 105
 235:      text[3] = 110
 236:      text[4] = 116
 237:      text[5] = 101
 238:      text[6] = 114
 239:      text[7] = 0
 240:      t = &text
 241: L11: t62 = *t
 242:      if t62 char== 0 goto L12
 243:      t = t ptr+ 1
 244:      goto L11
 245: L12: t64 = &text
 246:      t65 = t ptr- t64
 247:      t66 = t ptr- 1
 248:      t67 = *t66
 249:      t68 = chartoint t67
 250:      param "%.1f %d %c\n"
 251:      param d
 252:      param t65
 253:      param t68
 254:      call printf, 4
 255:      t69 = *p
 256:      return t69


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
swap               function       void (int *, int *)        -        global                         4     -     1     _Z4swapPiS_          _Z4swapPiS_              defined
a                  parameter      int *                      param    global > swap()                4     4     2     a.1                  -                        
b                  parameter      int *                      param    global > swap()                4     4     2     b.2                  -                        
t                  variable       int                        local    global > swap()                5     4     1     t.3                  -                        
sum                function       int (int *, int *)         -        global                         10    -     1     _Z3sumPiS_           _Z3sumPiS_               defined
first              parameter      int *                      param    global > sum()                 10    4     2     first.4              -                        
last               parameter      int *                      param    global > sum()                 10    4     1     last.5               -                        
s                  variable       int                        local    global > sum()                 11    4     2     s.6                  -                        
main               function       int (void)                 -        global                         16    -     0     main                 main                     defined
x                  variable       int                        local    global > main()                17    4     5     x.7                  -                        
y                  variable       int                        local    global > main()                17    4     4     y.8                  -                        
p                  variable       int *                      local    global > main()                18    4     6     p.9                  -                        
pp                 variable       int **                     local    global > main()                19    4     3     pp.10                -                        
ppp                variable       int ***                    local    global > main()                20    4     2     ppp.11               -                        
arr                variable       int[5]                     local    global > main()                27    20    8     arr.12               -                        
q                  variable       int *                      local    global > main()                28    4     12    q.13                 -                        
gap                variable       int                        local    global > main()                30    4     1     gap.14               -                        
raw                variable       void *                     local    global > main()                38    4     1     raw.15               -                        
back               variable       int *                      local    global > main()                39    4     1     back.16              -                        
bytes              variable       char *                     local    global > main()                40    4     1     bytes.17             -                        
grid               variable       int[2][3]                  local    global > main()                44    24    1     grid.18              -                        
row                variable       int (*)[3]                 local    global > main()                45    4     4     row.19               -                        
d                  variable       double                     local    global > main()                51    8     2     d.20                 -                        
dp                 variable       double *                   local    global > main()                51    4     2     dp.21                -                        
text               variable       char[8]                    local    global > main()                53    8     2     text.22              -                        
t                  variable       char *                     local    global > main()                54    4     4     t.23                 -                        

=== Record Layouts ===
(no records)
