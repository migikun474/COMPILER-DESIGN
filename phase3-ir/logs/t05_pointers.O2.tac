=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t05_pointers.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 188 -> 156 instruction(s) for 'test/t05_pointers.c'.

optimization summary (-O2)
    instructions                188 -> 156   (17% fewer)
    constants folded            3
    algebraic simplifications   0
    common subexpressions       8
    copies / constants forwarded 32
    temporaries merged away     5
    dead instructions removed   9
    jumps removed or redirected 3
    unreachable instructions    0
    propagated across blocks    2
    dead assignments removed    14

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
    total width 396
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
 139:      param t1
 140:      param t16
 141:      call swap(int *, int *), 2
 142:      param "%d %d\n"
 143:      param x
 144:      param y
 145:      call printf, 3
 146:      arr[0] = 10
 147:      arr[4] = 20
 148:      arr[8] = 30
 149:      arr[12] = 40
 150:      arr[16] = 50
 151:      t17 = &arr
 152:      t18 = t17 ptr+ 8
 153:      t19 = t18 ptr- 4
 154:      t21 = t17 ptr+ 16
 155:      t22 = t21 ptr- t19
 156:      t23 = t22 int/ 4
 157:      t24 = *t19
 158:      t27 = t17 ptr+ 20
 159:      param t17
 160:      param t27
 161:      t28 = call sum(int *, int *), 2
 162:      param "%d %d %d\n"
 163:      param t24
 164:      param t23
 165:      param t28
 166:      call printf, 4
 167:      t29 = t19 ptr+ 4
 168:      t30 = t29 ptr- 4
 169:      t31 = t30 ptr+ 8
 170:      t32 = *t31
 171:      t35 = t31 ptr+ -4
 172:      t36 = *t35
 173:      t39 = *t21
 174:      param "%d %d %d\n"
 175:      param t32
 176:      param t36
 177:      param t39
 178:      call printf, 4
 179:      t42 = t17 ptr+ 12
 180:      if t31 ptr== t42 goto L3
 181:      t40 = 0
 182:      goto L4
 183: L3:  t40 = 1
 184: L4:  t44 = &arr
 185:      if t31 ptr!= t44 goto L5
 186:      t43 = 0
 187:      goto L6
 188: L5:  t43 = 1
 189: L6:  t46 = &arr
 190:      t47 = t46 ptr+ 16
 191:      if t31 ptr< t47 goto L7
 192:      t45 = 0
 193:      goto L8
 194: L7:  t45 = 1
 195: L8:  param "%d %d %d\n"
 196:      param t40
 197:      param t43
 198:      param t45
 199:      call printf, 4
 200:      t48 = &x
 201:      t49 = &y
 202:      *t48 = 258
 203:      t50 = *t49
 204:      t51 = chartoint t50
 205:      param "%d %d\n"
 206:      param x
 207:      param t51
 208:      call printf, 3
 209:      grid[0] = 1
 210:      grid[4] = 2
 211:      grid[8] = 3
 212:      grid[12] = 4
 213:      grid[16] = 5
 214:      grid[20] = 6
 215:      t52 = &grid
 216:      t53 = t52 ptr+ 12
 217:      t54 = t53 ptr+ 8
 218:      t55 = *t54
 219:      t56 = *t53
 220:      param "%d %d\n"
 221:      param t55
 222:      param t56
 223:      call printf, 3
 224:      p = 0
 225:      p = t49
 226:      d = 2.5
 227:      t58 = &d
 228:      t59 = *t58
 229:      t60 = t59 double* 2.0
 230:      *t58 = t60
 231:      text[0] = 112
 232:      text[1] = 111
 233:      text[2] = 105
 234:      text[3] = 110
 235:      text[4] = 116
 236:      text[5] = 101
 237:      text[6] = 114
 238:      text[7] = 0
 239:      t = &text
 240: L9:  t62 = *t
 241:      if t62 char== 0 goto L10
 242:      t = t ptr+ 1
 243:      goto L9
 244: L10: t64 = &text
 245:      t65 = t ptr- t64
 246:      t66 = t ptr- 1
 247:      t67 = *t66
 248:      t68 = chartoint t67
 249:      param "%.1f %d %c\n"
 250:      param d
 251:      param t65
 252:      param t68
 253:      call printf, 4
 254:      t69 = *p
 255:      return t69


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
