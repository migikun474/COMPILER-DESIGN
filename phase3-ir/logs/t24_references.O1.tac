=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t24_references.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 217 -> 201 instruction(s) for 'test/t24_references.c'.

optimization summary (-O1)
    instructions                217 -> 201   (7% fewer)
    constants folded            3
    algebraic simplifications   6
    common subexpressions       9
    copies / constants forwarded 24
    temporaries merged away     1
    dead instructions removed   12
    jumps removed or redirected 3
    unreachable instructions    0

function deposit(struct Account &, double)        link name: _Z7depositR7Accountd
  symbol table (name, kind, type, width, offset)
    a              param  struct Account &           4      0
    amount         param  double                     8      8
    t1             temp   struct Account *           4     16
    t2             temp   double                     8     24
    t3             temp   double                     8     32
    t4             temp   struct Account *           4     40
    total width 44
  code
 100:   t1 = a ptr+ 8
 101:   t2 = *t1
 102:   t3 = t2 double+ amount
 103:   *t1 = t3
 104:   return

function peek(const struct Account &)        link name: _Z4peekRK7Account
  symbol table (name, kind, type, width, offset)
    a              param  const struct Account &     4      0
    t1             temp   const struct Account *     4      4
    t2             temp   double                     8      8
    total width 16
  code
 105:   t1 = a ptr+ 8
 106:   t2 = *t1
 107:   return t2

function richer(struct Account &, struct Account &)        link name: _Z6richerR7AccountS0_
  symbol table (name, kind, type, width, offset)
    a              param  struct Account &           4      0
    b              param  struct Account &           4      4
    t1             temp   struct Account *           4      8
    t2             temp   struct Account *           4     12
    t3             temp   double                     8     16
    t4             temp   struct Account *           4     24
    t5             temp   double                     8     32
    total width 40
  code
 108:     t2 = a ptr+ 8
 109:     t3 = *t2
 110:     t4 = b ptr+ 8
 111:     t5 = *t4
 112:     if t3 double>= t5 goto L1
 113:     goto L2
 114: L1: t1 = a
 115:     goto L3
 116: L2: t1 = b
 117: L3: return t1

function minmax(const int *, int, int &, int &)        link name: _Z6minmaxPKiiRiS1_
  symbol table (name, kind, type, width, offset)
    values         param  const int *                4      0
    n              param  int                        4      4
    lo             param  int &                      4      8
    hi             param  int &                      4     12
    i              local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   const int *                4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   const int *                4     44
    t8             temp   int                        4     48
    t9             temp   int                        4     52
    t10            temp   const int *                4     56
    t11            temp   int                        4     60
    t12            temp   int                        4     64
    t13            temp   int                        4     68
    t14            temp   const int *                4     72
    t15            temp   int                        4     76
    t16            temp   int                        4     80
    total width 84
  code
 118:     t1 = *values
 119:     *hi = t1
 120:     *lo = t1
 121:     i = 1
 122: L4: if i int>= n goto L7
 123:     t2 = i int<< 2
 124:     t3 = values ptr+ t2
 125:     t4 = *t3
 126:     t5 = *lo
 127:     if t4 int>= t5 goto L5
 128:     t6 = i int<< 2
 129:     t7 = values ptr+ t6
 130:     t8 = *t7
 131:     *lo = t8
 132: L5: t9 = i int<< 2
 133:     t10 = values ptr+ t9
 134:     t11 = *t10
 135:     t12 = *hi
 136:     if t11 int<= t12 goto L6
 137:     t13 = i int<< 2
 138:     t14 = values ptr+ t13
 139:     t15 = *t14
 140:     *hi = t15
 141: L6: i = i int+ 1
 142:     goto L4
 143: L7: return

function advance(int *&, int)        link name: _Z7advanceRPii
  symbol table (name, kind, type, width, offset)
    p              param  int *&                     4      0
    steps          param  int                        4      4
    t1             temp   int *                      4      8
    t2             temp   int                        4     12
    t3             temp   int *                      4     16
    total width 20
  code
 144:   t1 = *p
 145:   t2 = steps int<< 2
 146:   t3 = t1 ptr+ t2
 147:   *p = t3
 148:   return

function element(int *, int)        link name: _Z7elementPii
  symbol table (name, kind, type, width, offset)
    a              param  int *                      4      0
    i              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int *                      4     12
    total width 16
  code
 149:   t1 = i int<< 2
 150:   t2 = a ptr+ t1
 151:   return t2

function scale(const int &, const double &)        link name: _Z5scaleRKiRKd
  symbol table (name, kind, type, width, offset)
    v              param  const int &                4      0
    factor         param  const double &             4      4
    t1             temp   int                        4      8
    t2             temp   double                     8     16
    t3             temp   double                     8     24
    t4             temp   double                     8     32
    t5             temp   int                        4     40
    total width 44
  code
 152:   t1 = *v
 153:   t2 = inttodouble t1
 154:   t3 = *factor
 155:   t4 = t2 double* t3
 156:   t5 = doubletoint t4
 157:   return t5

function rotate(int &, int &, int &)        link name: _Z6rotateRiS_S_
  symbol table (name, kind, type, width, offset)
    a              param  int &                      4      0
    b              param  int &                      4      4
    c              param  int &                      4      8
    t              local  int                        4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    total width 28
  code
 158:   t1 = *a
 159:   t = t1
 160:   t2 = *b
 161:   *a = t2
 162:   t3 = *c
 163:   *b = t3
 164:   *c = t1
 165:   return

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    x              local  int                        4      0
    y              local  int                        4      4
    z              local  int                        4      8
    rx             local  int &                      4     12
    rrx            local  int &                      4     16
    data           local  int[5]                    20     20
    lo             local  int                        4     40
    hi             local  int                        4     44
    p              local  int *                      4     48
    a              local  struct Account            16     56
    b              local  struct Account            16     72
    best           local  struct Account &           4     88
    limit          local  const int                  4     92
    rate           local  const double               8     96
    small          local  short                      2    104
    msg            local  const char *               4    108
    first          local  const char &               4    112
    t1             temp   int *                      4    116
    t2             temp   int                        4    120
    t3             temp   int                        4    124
    t4             temp   int *                      4    128
    t5             temp   int *                      4    132
    t6             temp   int *                      4    136
    t7             temp   int                        4    140
    t8             temp   int                        4    144
    t9             temp   int (*)[5]                 4    148
    t10            temp   int *                      4    152
    t11            temp   int *                      4    156
    t12            temp   int (*)[5]                 4    160
    t13            temp   int &                      4    164
    t14            temp   int (*)[5]                 4    168
    t15            temp   int &                      4    172
    t16            temp   int                        4    176
    t17            temp   int                        4    180
    t18            temp   int (*)[5]                 4    184
    t19            temp   int **                     4    188
    t20            temp   int                        4    192
    t21            temp   int                        4    196
    t22            temp   int                        4    200
    t23            temp   int                        4    204
    t24            temp   int                        4    208
    t25            temp   struct Account *           4    212
    t26            temp   struct Account *           4    216
    t27            temp   struct Account *           4    220
    t28            temp   struct Account &           4    224
    t29            temp   struct Account *           4    228
    t30            temp   double                     8    232
    t31            temp   double                     8    240
    t32            temp   struct Account *           4    248
    t33            temp   struct Account *           4    252
    t34            temp   struct Account *           4    256
    t35            temp   struct Account &           4    260
    t36            temp   double                     8    264
    t37            temp   double                     8    272
    t38            temp   int                        4    280
    t39            temp   double                     8    288
    t40            temp   const int *                4    296
    t41            temp   const double *             4    300
    t42            temp   int                        4    304
    t43            temp   int                        4    308
    t44            temp   int                        4    312
    t45            temp   const int *                4    316
    t46            temp   double                     8    320
    t47            temp   const double *             4    328
    t48            temp   int                        4    332
    t49            temp   int                        4    336
    t50            temp   int                        4    340
    t51            temp   const int *                4    344
    t52            temp   double                     8    352
    t53            temp   const double *             4    360
    t54            temp   int                        4    364
    t55            temp   char                       1    368
    t56            temp   int                        4    372
    t57            temp   const char *               4    376
    t58            temp   char                       1    380
    t59            temp   int                        4    384
    t60            temp   int                        4    388
    t61            temp   int                        4    392
    total width 396
  code
 166:   x = 1
 167:   y = 2
 168:   z = 3
 169:   t1 = &x
 170:   rx = t1
 171:   rrx = t1
 172:   t2 = *t1
 173:   t3 = t2 int+ 10
 174:   *t1 = t3
 175:   t5 = &y
 176:   t6 = &z
 177:   param t1
 178:   param t5
 179:   param t6
 180:   call rotate(int &, int &, int &), 3
 181:   t7 = *t1
 182:   param "%d %d %d %d\n"
 183:   param x
 184:   param y
 185:   param z
 186:   param t7
 187:   call printf, 5
 188:   data[0] = 8
 189:   data[4] = -3
 190:   data[8] = 15
 191:   data[12] = 0
 192:   data[16] = 7
 193:   t9 = &data
 194:   t10 = &lo
 195:   t11 = &hi
 196:   param t9
 197:   param 5
 198:   param t10
 199:   param t11
 200:   call minmax(const int *, int, int &, int &), 4
 201:   param t9
 202:   param 3
 203:   t13 = call element(int *, int), 2
 204:   *t13 = 99
 205:   param t9
 206:   param 0
 207:   t15 = call element(int *, int), 2
 208:   t16 = *t15
 209:   t17 = t16 int+ 1
 210:   *t15 = t17
 211:   p = t9
 212:   t19 = &p
 213:   param t19
 214:   param 2
 215:   call advance(int *&, int), 2
 216:   t20 = *p
 217:   t21 = t20 int+ 1
 218:   *p = t21
 219:   t22 = data[12]
 220:   t23 = data[0]
 221:   t24 = data[8]
 222:   param "%d %d %d %d %d\n"
 223:   param lo
 224:   param hi
 225:   param t22
 226:   param t23
 227:   param t24
 228:   call printf, 6
 229:   a[0] = 1
 230:   a[8] = 100.5
 231:   b[0] = 2
 232:   b[8] = 2.5e+02
 233:   t25 = &a
 234:   param t25
 235:   param 2e+02
 236:   call deposit(struct Account &, double), 2
 237:   t27 = &b
 238:   param t25
 239:   param t27
 240:   t28 = call richer(struct Account &, struct Account &), 2
 241:   t29 = t28 ptr+ 8
 242:   t30 = *t29
 243:   t31 = t30 double- 5e+01
 244:   *t29 = t31
 245:   param t25
 246:   param t27
 247:   t35 = call richer(struct Account &, struct Account &), 2
 248:   best = t35
 249:   t36 = a[8]
 250:   t37 = b[8]
 251:   t38 = *t35
 252:   param t35
 253:   t39 = call peek(const struct Account &), 1
 254:   param "%.1f %.1f %d %.1f\n"
 255:   param t36
 256:   param t37
 257:   param t38
 258:   param t39
 259:   call printf, 5
 260:   limit = 40
 261:   rate = 1.25
 262:   small = 7
 263:   t40 = &limit
 264:   t41 = &rate
 265:   param t40
 266:   param t41
 267:   t42 = call scale(const int &, const double &), 2
 268:   t43 = 7
 269:   t45 = &t43
 270:   t46 = 2.0
 271:   t47 = &t46
 272:   param t45
 273:   param t47
 274:   t48 = call scale(const int &, const double &), 2
 275:   t49 = 7
 276:   t51 = &t49
 277:   t52 = 0.5
 278:   t53 = &t52
 279:   param t51
 280:   param t53
 281:   t54 = call scale(const int &, const double &), 2
 282:   param "%d %d %d\n"
 283:   param t42
 284:   param t48
 285:   param t54
 286:   call printf, 4
 287:   msg = "const data"
 288:   first = "const data"
 289:   t55 = *"const data"
 290:   t56 = chartoint t55
 291:   t57 = "const data" ptr+ 6
 292:   t58 = *t57
 293:   t59 = chartoint t58
 294:   param "%c %c\n"
 295:   param t56
 296:   param t59
 297:   call printf, 3
 298:   t60 = *t1
 299:   t61 = t60 int+ lo
 300:   return t61


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Account            struct_tag     struct Account             -        global                         5     -     0     Account              -                        size 16
Account::id        field          int                        member   global > struct Account        5     4     1     Account::id          -                        public, offset 0
Account::balance   field          double                     member   global > struct Account        5     8     7     Account::balance     -                        public, offset 8
deposit            function       void (struct Account &, double) -        global                         7     -     1     _Z7depositR7Accountd _Z7depositR7Accountd     defined
a                  parameter      struct Account &           param    global > deposit()             7     4     1     a.1                  -                        
amount             parameter      double                     param    global > deposit()             7     8     1     amount.2             -                        
peek               function       double (const struct Account &) -        global                         8     -     1     _Z4peekRK7Account    _Z4peekRK7Account        defined
a                  parameter      const struct Account &     param    global > peek()                8     4     1     a.3                  -                        
richer             function       struct Account &(struct Account &, struct Account &) -        global                         9     -     2     _Z6richerR7AccountS0_ _Z6richerR7AccountS0_    defined
a                  parameter      struct Account &           param    global > richer()              9     4     2     a.4                  -                        
b                  parameter      struct Account &           param    global > richer()              9     4     2     b.5                  -                        
minmax             function       void (const int *, int, int &, int &) -        global                         11    -     1     _Z6minmaxPKiiRiS1_   _Z6minmaxPKiiRiS1_       defined
values             parameter      const int *                param    global > minmax()              11    4     5     values.6             -                        
n                  parameter      int                        param    global > minmax()              11    4     1     n.7                  -                        
lo                 parameter      int &                      param    global > minmax()              11    4     3     lo.8                 -                        
hi                 parameter      int &                      param    global > minmax()              11    4     3     hi.9                 -                        
i                  variable       int                        local    global > minmax() > for        13    4     6     i.10                 -                        
advance            function       void (int *&, int)         -        global                         19    -     1     _Z7advanceRPii       _Z7advanceRPii           defined
p                  parameter      int *&                     param    global > advance()             19    4     1     p.11                 -                        
steps              parameter      int                        param    global > advance()             19    4     1     steps.12             -                        
element            function       int &(int *, int)          -        global                         20    -     2     _Z7elementPii        _Z7elementPii            defined
a                  parameter      int *                      param    global > element()             20    4     1     a.13                 -                        
i                  parameter      int                        param    global > element()             20    4     1     i.14                 -                        
scale              function       int (const int &, const double &) -        global                         21    -     3     _Z5scaleRKiRKd       _Z5scaleRKiRKd           defined
v                  parameter      const int &                param    global > scale()               21    4     1     v.15                 -                        
factor             parameter      const double &             param    global > scale()               21    4     1     factor.16            -                        
rotate             function       void (int &, int &, int &) -        global                         22    -     1     _Z6rotateRiS_S_      _Z6rotateRiS_S_          defined
a                  parameter      int &                      param    global > rotate()              22    4     2     a.17                 -                        
b                  parameter      int &                      param    global > rotate()              22    4     2     b.18                 -                        
c                  parameter      int &                      param    global > rotate()              22    4     2     c.19                 -                        
t                  variable       int                        local    global > rotate()              22    4     1     t.20                 -                        
main               function       int (void)                 -        global                         24    -     0     main                 main                     defined
x                  variable       int                        local    global > main()                25    4     3     x.21                 -                        
y                  variable       int                        local    global > main()                25    4     2     y.22                 -                        
z                  variable       int                        local    global > main()                25    4     2     z.23                 -                        
rx                 variable       int &                      local    global > main()                26    4     3     rx.24                -                        
rrx                variable       int &                      local    global > main()                27    4     1     rrx.25               -                        
data               variable       int[5]                     local    global > main()                32    20    7     data.26              -                        
lo                 variable       int                        local    global > main()                32    4     3     lo.27                -                        
hi                 variable       int                        local    global > main()                32    4     2     hi.28                -                        
p                  variable       int *                      local    global > main()                36    4     2     p.29                 -                        
a                  variable       struct Account             local    global > main()                41    16    4     a.30                 -                        
b                  variable       struct Account             local    global > main()                41    16    3     b.31                 -                        
best               variable       struct Account &           local    global > main()                44    4     2     best.32              -                        
limit              variable       const int                  local    global > main()                47    4     1     limit.33             -                        value 40
rate               variable       const double               local    global > main()                48    8     1     rate.34              -                        
small              variable       short                      local    global > main()                49    2     1     small.35             -                        
msg                variable       const char *               local    global > main()                51    4     2     msg.36               -                        
first              variable       const char &               local    global > main()                52    4     1     first.37             -                        

=== Record Layouts ===
struct Account: size 16, align 8
    +0  int id  [public]
    +8  double balance  [public]
