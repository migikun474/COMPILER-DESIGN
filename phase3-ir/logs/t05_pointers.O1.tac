=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t05_pointers.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 188 -> 170 instruction(s) for 'test/t05_pointers.c'.

optimization summary (-O1)
    instructions                188 -> 170   (9% fewer)
    constants folded            3
    algebraic simplifications   0
    common subexpressions       8
    copies / constants forwarded 32
    temporaries merged away     5
    dead instructions removed   9
    jumps removed or redirected 3
    unreachable instructions    0

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
 101:   t = t1
 102:   t2 = *b
 103:   *a = t2
 104:   *b = t1
 105:   return

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
 106:     s = 0
 107: L1: if first ptr>= last goto L2
 108:     t1 = first
 109:     first = first ptr+ 4
 110:     t3 = *t1
 111:     s = s int+ t3
 112:     goto L1
 113: L2: return s

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
    total width 396
  code
 114:      x = 5
 115:      y = 6
 116:      t1 = &x
 117:      p = t1
 118:      t2 = &p
 119:      pp = t2
 120:      t3 = &pp
 121:      ppp = t3
 122:      t4 = *p
 123:      t5 = *t2
 124:      t6 = *t5
 125:      t7 = *t3
 126:      t8 = *t7
 127:      t9 = *t8
 128:      param "%d %d %d\n"
 129:      param t4
 130:      param t6
 131:      param t9
 132:      call printf, 4
 133:      t10 = *pp
 134:      *t10 = 9
 135:      t11 = *t3
 136:      t12 = *t11
 137:      t13 = *t12
 138:      t14 = t13 int+ 1
 139:      *t12 = t14
 140:      t16 = &y
 141:      param t1
 142:      param t16
 143:      call swap(int *, int *), 2
 144:      param "%d %d\n"
 145:      param x
 146:      param y
 147:      call printf, 3
 148:      arr[0] = 10
 149:      arr[4] = 20
 150:      arr[8] = 30
 151:      arr[12] = 40
 152:      arr[16] = 50
 153:      t17 = &arr
 154:      t18 = t17 ptr+ 8
 155:      q = t18
 156:      t19 = t18 ptr- 4
 157:      q = t19
 158:      t21 = t17 ptr+ 16
 159:      t22 = t21 ptr- t19
 160:      t23 = t22 int/ 4
 161:      gap = t23
 162:      t24 = *t19
 163:      t27 = t17 ptr+ 20
 164:      param t17
 165:      param t27
 166:      t28 = call sum(int *, int *), 2
 167:      param "%d %d %d\n"
 168:      param t24
 169:      param t23
 170:      param t28
 171:      call printf, 4
 172:      t29 = t19 ptr+ 4
 173:      q = t29
 174:      t30 = t29 ptr- 4
 175:      q = t30
 176:      t31 = t30 ptr+ 8
 177:      q = t31
 178:      t32 = *t31
 179:      t35 = t31 ptr+ -4
 180:      t36 = *t35
 181:      t39 = *t21
 182:      param "%d %d %d\n"
 183:      param t32
 184:      param t36
 185:      param t39
 186:      call printf, 4
 187:      t42 = t17 ptr+ 12
 188:      if t31 ptr== t42 goto L3
 189:      t40 = 0
 190:      goto L4
 191: L3:  t40 = 1
 192: L4:  t44 = &arr
 193:      if q ptr!= t44 goto L5
 194:      t43 = 0
 195:      goto L6
 196: L5:  t43 = 1
 197: L6:  t46 = &arr
 198:      t47 = t46 ptr+ 16
 199:      if q ptr< t47 goto L7
 200:      t45 = 0
 201:      goto L8
 202: L7:  t45 = 1
 203: L8:  param "%d %d %d\n"
 204:      param t40
 205:      param t43
 206:      param t45
 207:      call printf, 4
 208:      t48 = &x
 209:      raw = t48
 210:      back = t48
 211:      t49 = &y
 212:      bytes = t49
 213:      *t48 = 258
 214:      t50 = *t49
 215:      t51 = chartoint t50
 216:      param "%d %d\n"
 217:      param x
 218:      param t51
 219:      call printf, 3
 220:      grid[0] = 1
 221:      grid[4] = 2
 222:      grid[8] = 3
 223:      grid[12] = 4
 224:      grid[16] = 5
 225:      grid[20] = 6
 226:      t52 = &grid
 227:      row = t52
 228:      t53 = t52 ptr+ 12
 229:      row = t53
 230:      t54 = t53 ptr+ 8
 231:      t55 = *t54
 232:      t56 = *t53
 233:      param "%d %d\n"
 234:      param t55
 235:      param t56
 236:      call printf, 3
 237:      p = 0
 238:      p = t49
 239:      d = 2.5
 240:      t58 = &d
 241:      dp = t58
 242:      t59 = *t58
 243:      t60 = t59 double* 2.0
 244:      *t58 = t60
 245:      text[0] = 112
 246:      text[1] = 111
 247:      text[2] = 105
 248:      text[3] = 110
 249:      text[4] = 116
 250:      text[5] = 101
 251:      text[6] = 114
 252:      text[7] = 0
 253:      t = &text
 254: L9:  t62 = *t
 255:      if t62 char== 0 goto L10
 256:      t = t ptr+ 1
 257:      goto L9
 258: L10: t64 = &text
 259:      t65 = t ptr- t64
 260:      t66 = t ptr- 1
 261:      t67 = *t66
 262:      t68 = chartoint t67
 263:      param "%.1f %d %c\n"
 264:      param d
 265:      param t65
 266:      param t68
 267:      call printf, 4
 268:      t69 = *p
 269:      return t69


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
