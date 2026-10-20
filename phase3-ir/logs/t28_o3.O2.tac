=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t28_o3.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 313 -> 261 instruction(s) for 'test/t28_o3.c'.

optimization summary (-O2)
    instructions                313 -> 261   (16% fewer)
    constants folded            1
    algebraic simplifications   7
    common subexpressions       7
    copies / constants forwarded 22
    temporaries merged away     17
    dead instructions removed   8
    jumps removed or redirected 16
    unreachable instructions    1
    propagated across blocks    0
    dead assignments removed    11

globals (name, type, width, initial value)
    calls          int                        4  0

function square(int)        link name: _Z6squarei
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    total width 8
  code
 100:   t1 = v int* v
 101:   return t1

function clamp(int, int, int)        link name: _Z5clampiii
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    lo             param  int                        4      4
    hi             param  int                        4      8
    total width 12
  code
 102:     if v int>= lo goto L1
 103:     return lo
 104: L1: if v int<= hi goto L2
 105:     return hi
 106: L2: return v

function counted(int)        link name: _Z7countedi
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 107:   t1 = calls int+ 1
 108:   calls = t1
 109:   t2 = v int+ t1
 110:   return t2

function bump(int &, int)        link name: _Z4bumpRii
  symbol table (name, kind, type, width, offset)
    r              param  int &                      4      0
    by             param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 111:   t1 = *r
 112:   t2 = t1 int+ by
 113:   *r = t2
 114:   return

function total(struct Pair)        link name: _Z5total4Pair
  symbol table (name, kind, type, width, offset)
    p              param  struct Pair                8      0
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    total width 28
  code
 115:   t1 = p[0]
 116:   t2 = t1 int+ 1
 117:   p[0] = t2
 118:   t4 = p[4]
 119:   t5 = t2 int+ t4
 120:   return t5

function fact(int)        link name: _Z4facti
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 121:     if n int> 1 goto L3
 122:     t1 = 1
 123:     goto L4
 124: L3: t2 = n int- 1
 125:     param t2
 126:     t3 = call fact(int), 1
 127:     t1 = n int* t3
 128: L4: return t1

function gcd(int, int)        link name: _Z3gcdii
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    total width 16
  code
 129:     if b int!= 0 goto L5
 130:     return a
 131: L5: t1 = a int% b
 132:     param b
 133:     param t1
 134:     t2 = call gcd(int, int), 2
 135:     return t2

function sumTo(int, int)        link name: _Z5sumToii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    acc            param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 136:     if n int!= 0 goto L6
 137:     return acc
 138: L6: t1 = n int- 1
 139:     t2 = acc int+ n
 140:     param t1
 141:     param t2
 142:     t3 = call sumTo(int, int), 2
 143:     return t3

function countDown(int)        link name: _Z9countDowni
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 144:     if n int> 0 goto L7
 145:     return 0
 146: L7: t1 = n int- 2
 147:     param t1
 148:     t2 = call countDown(int), 1
 149:     return t2

function invariant(int, int)        link name: _Z9invariantii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    k              param  int                        4      4
    s              local  int                        4      8
    i              local  int                        4     12
    scale          local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    total width 48
  code
 150:      s = 0
 151:      i = 0
 152: L8:  if i int>= n goto L10
 153:      t1 = k int* 3
 154:      t2 = t1 int+ 1
 155:      t3 = i int* t2
 156:      s = s int+ t3
 157:      if i int== 2 goto L9
 158:      t5 = k int* 3
 159:      s = s int+ t5
 160: L9:  i = i int+ 1
 161:      goto L8
 162: L10: return s

function notInvariant(int)        link name: _Z12notInvarianti
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    s              local  int                        4      4
    k              local  int                        4      8
    i              local  int                        4     12
    v              local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    total width 36
  code
 163:      s = 0
 164:      k = 1
 165:      i = 0
 166: L11: if i int>= n goto L12
 167:      t1 = k int* 3
 168:      s = s int+ t1
 169:      k = k int+ i
 170:      i = i int+ 1
 171:      goto L11
 172: L12: return s

function zeroTrips(int, int)        link name: _Z9zeroTripsii
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    d              param  int                        4      4
    s              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    total width 24
  code
 173:      s = 7
 174: L13: if n int<= 0 goto L14
 175:      t1 = 100 int/ d
 176:      s = s int+ t1
 177:      n = n int- 1
 178:      goto L13
 179: L14: return s

function nested(int, int)        link name: _Z6nestedii
  symbol table (name, kind, type, width, offset)
    rows           param  int                        4      0
    cols           param  int                        4      4
    grid           local  int[4][5]                 80      8
    s              local  int                        4     88
    r.32           local  int                        4     92
    c.33           local  int                        4     96
    r.34           local  int                        4    100
    c.35           local  int                        4    104
    t1             temp   int                        4    108
    t2             temp   int                        4    112
    t3             temp   int                        4    116
    t4             temp   int                        4    120
    t5             temp   int                        4    124
    t6             temp   int                        4    128
    t7             temp   int                        4    132
    t8             temp   int                        4    136
    t9             temp   int                        4    140
    t10            temp   int                        4    144
    t11            temp   int                        4    148
    t12            temp   int                        4    152
    t13            temp   int                        4    156
    t14            temp   int                        4    160
    total width 164
  code
 180:      s = 0
 181:      r.32 = 0
 182: L15: if r.32 int>= rows goto L18
 183:      c.33 = 0
 184: L16: if c.33 int>= cols goto L17
 185:      t1 = r.32 int* 5                    (n2 = 5)
 186:      t2 = t1 int+ c.33
 187:      t3 = t2 int<< 2                     (w = 4)
 188:      t4 = r.32 int* cols
 189:      t5 = t4 int+ c.33
 190:      grid[t3] = t5
 191:      c.33 = c.33 int+ 1
 192:      goto L16
 193: L17: r.32 = r.32 int+ 1
 194:      goto L15
 195: L18: r.34 = 0
 196: L19: if r.34 int>= rows goto L22
 197:      c.35 = 0
 198: L20: if c.35 int>= cols goto L21
 199:      t8 = r.34 int* 5                    (n2 = 5)
 200:      t9 = t8 int+ c.35
 201:      t10 = t9 int<< 2                    (w = 4)
 202:      t11 = grid[t10]
 203:      s = s int+ t11
 204:      c.35 = c.35 int+ 1
 205:      goto L20
 206: L21: r.34 = r.34 int+ 1
 207:      goto L19
 208: L22: return s

function shared(int, int, int)        link name: _Z6sharediii
  symbol table (name, kind, type, width, offset)
    x              param  int                        4      0
    y              param  int                        4      4
    flag           param  int                        4      8
    a              local  int                        4     12
    b              local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    t7             temp   int                        4     44
    t8             temp   int                        4     48
    t9             temp   int                        4     52
    t10            temp   int                        4     56
    t11            temp   int                        4     60
    total width 64
  code
 209:      t1 = x int* y
 210:      a = t1 int+ 2
 211:      if flag int== 0 goto L23
 212:      t3 = x int* y
 213:      b = t3 int+ 2
 214:      goto L24
 215: L23: t5 = x int+ 1
 216:      x = t5
 217:      t6 = t5 int* y
 218:      b = t6 int+ 2
 219: L24: t8 = a int* 1000
 220:      t9 = t8 int+ b
 221:      t10 = x int* y
 222:      t11 = t9 int+ t10
 223:      return t11

function memory(int)        link name: _Z6memoryi
  symbol table (name, kind, type, width, offset)
    i              param  int                        4      0
    arr            local  int[4]                    16      4
    p              local  int *                      4     20
    q              local  int *                      4     24
    a              local  int                        4     28
    b              local  int                        4     32
    c              local  int                        4     36
    t1             temp   int *                      4     40
    t2             temp   int *                      4     44
    t3             temp   int (*)[4]                 4     48
    t4             temp   int                        4     52
    t5             temp   int                        4     56
    t6             temp   int                        4     60
    t7             temp   int                        4     64
    t8             temp   int                        4     68
    t9             temp   int                        4     72
    t10            temp   int *                      4     76
    t11            temp   int                        4     80
    t12            temp   int                        4     84
    t13            temp   int                        4     88
    t14            temp   int                        4     92
    t15            temp   int                        4     96
    t16            temp   int                        4    100
    total width 104
  code
 224:   arr[0] = 1
 225:   arr[4] = 2
 226:   arr[8] = 3
 227:   arr[12] = 4
 228:   t1 = &arr
 229:   t2 = t1 ptr+ 4
 230:   t4 = i int<< 2                      (w = 4)
 231:   arr[t4] = 10
 232:   *t2 = 20
 233:   t8 = arr[t4]
 234:   t10 = t1 ptr+ t4
 235:   *t10 = 30
 236:   t12 = arr[t4]
 237:   t13 = *t2
 238:   t14 = t12 int+ t13
 239:   t15 = 10 int+ t8
 240:   t16 = t15 int+ t14
 241:   return t16

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    x              local  int                        4      0
    p              local  struct Pair                8      4
    t              local  int                        4     12
    c1             local  int                        4     16
    c2             local  int                        4     20
    c3             local  int                        4     24
    t1             temp   int *                      4     28
    t2             temp   int                        4     32
    t3             temp   int                        4     36
    t4             temp   int                        4     40
    t5             temp   int                        4     44
    t6             temp   int                        4     48
    t7             temp   int                        4     52
    t8             temp   int                        4     56
    t9             temp   int                        4     60
    t10            temp   int                        4     64
    t11            temp   int                        4     68
    t12            temp   int                        4     72
    t13            temp   int                        4     76
    t14            temp   int                        4     80
    t15            temp   int                        4     84
    t16            temp   int                        4     88
    t17            temp   int                        4     92
    t18            temp   int                        4     96
    t19            temp   int                        4    100
    t20            temp   int                        4    104
    t21            temp   int                        4    108
    t22            temp   int                        4    112
    t23            temp   int                        4    116
    t24            temp   int                        4    120
    t25            temp   int                        4    124
    t26            temp   int                        4    128
    t27            temp   int                        4    132
    t28            temp   int                        4    136
    t29            temp   int                        4    140
    t30            temp   int                        4    144
    total width 148
  code
 242:   x = 5
 243:   t1 = &x
 244:   param 3
 245:   t2 = call square(int), 1
 246:   param t1
 247:   param t2
 248:   call bump(int &, int), 2
 249:   p[0] = 1
 250:   p[4] = 2
 251:   param p
 252:   t3 = call total(struct Pair), 1
 253:   param p
 254:   t4 = call total(struct Pair), 1
 255:   t5 = t3 int+ t4
 256:   t6 = p[0]
 257:   param -5
 258:   param 0
 259:   param 9
 260:   t8 = call clamp(int, int, int), 3
 261:   param 50
 262:   param 0
 263:   param 9
 264:   t9 = call clamp(int, int, int), 3
 265:   param 4
 266:   param 0
 267:   param 9
 268:   t10 = call clamp(int, int, int), 3
 269:   t11 = t9 int+ t10
 270:   param "%d %d %d %d %d\n"
 271:   param x
 272:   param t5
 273:   param t6
 274:   param t8
 275:   param t11
 276:   call printf, 6
 277:   param 1
 278:   t12 = call counted(int), 1
 279:   param 1
 280:   t13 = call counted(int), 1
 281:   param 1
 282:   t14 = call counted(int), 1
 283:   param 6
 284:   t15 = call fact(int), 1
 285:   param "%d %d %d %d %d\n"
 286:   param t12
 287:   param t13
 288:   param t14
 289:   param calls
 290:   param t15
 291:   call printf, 6
 292:   param 1071
 293:   param 462
 294:   t16 = call gcd(int, int), 2
 295:   param 17
 296:   param 5
 297:   t17 = call gcd(int, int), 2
 298:   param 100
 299:   param 0
 300:   t18 = call sumTo(int, int), 2
 301:   param 9
 302:   t19 = call countDown(int), 1
 303:   param "%d %d %d %d\n"
 304:   param t16
 305:   param t17
 306:   param t18
 307:   param t19
 308:   call printf, 5
 309:   param 5
 310:   param 2
 311:   t20 = call invariant(int, int), 2
 312:   param 0
 313:   param 9
 314:   t21 = call invariant(int, int), 2
 315:   param 5
 316:   t22 = call notInvariant(int), 1
 317:   param 0
 318:   param 0
 319:   t23 = call zeroTrips(int, int), 2
 320:   param "%d %d %d %d\n"
 321:   param t20
 322:   param t21
 323:   param t22
 324:   param t23
 325:   call printf, 5
 326:   param 3
 327:   param 4
 328:   t24 = call zeroTrips(int, int), 2
 329:   param 4
 330:   param 5
 331:   t25 = call nested(int, int), 2
 332:   param 2
 333:   param 3
 334:   t26 = call nested(int, int), 2
 335:   param "%d %d %d\n"
 336:   param t24
 337:   param t25
 338:   param t26
 339:   call printf, 4
 340:   param 3
 341:   param 4
 342:   param 1
 343:   t27 = call shared(int, int, int), 3
 344:   param 3
 345:   param 4
 346:   param 0
 347:   t28 = call shared(int, int, int), 3
 348:   param "%d %d\n"
 349:   param t27
 350:   param t28
 351:   call printf, 3
 352:   param 1
 353:   t29 = call memory(int), 1
 354:   param 2
 355:   t30 = call memory(int), 1
 356:   param "%d %d\n"
 357:   param t29
 358:   param t30
 359:   call printf, 3
 360:   return calls


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
calls              variable       int                        global   global                         6     4     4     calls                -                        
square             function       int (int)                  -        global                         7     -     1     _Z6squarei           _Z6squarei               defined
v                  parameter      int                        param    global > square()              7     4     2     v.1                  -                        
clamp              function       int (int, int, int)        -        global                         8     -     3     _Z5clampiii          _Z5clampiii              defined
v                  parameter      int                        param    global > clamp()               8     4     3     v.2                  -                        
lo                 parameter      int                        param    global > clamp()               8     4     2     lo.3                 -                        
hi                 parameter      int                        param    global > clamp()               8     4     2     hi.4                 -                        
counted            function       int (int)                  -        global                         9     -     3     _Z7countedi          _Z7countedi              defined
v                  parameter      int                        param    global > counted()             9     4     1     v.5                  -                        
bump               function       void (int &, int)          -        global                         10    -     1     _Z4bumpRii           _Z4bumpRii               defined
r                  parameter      int &                      param    global > bump()                10    4     1     r.6                  -                        
by                 parameter      int                        param    global > bump()                10    4     1     by.7                 -                        
Pair               struct_tag     struct Pair                -        global                         11    -     0     Pair                 -                        size 8
Pair::a            field          int                        member   global > struct Pair           11    4     3     Pair::a              -                        public, offset 0
Pair::b            field          int                        member   global > struct Pair           11    4     1     Pair::b              -                        public, offset 4
total              function       int (struct Pair)          -        global                         12    -     2     _Z5total4Pair        _Z5total4Pair            defined
p                  parameter      struct Pair                param    global > total()               12    8     3     p.8                  -                        
fact               function       int (int)                  -        global                         13    -     2     _Z4facti             _Z4facti                 defined
n                  parameter      int                        param    global > fact()                13    4     3     n.9                  -                        
gcd                function       int (int, int)             -        global                         15    -     3     _Z3gcdii             _Z3gcdii                 defined
a                  parameter      int                        param    global > gcd()                 15    4     2     a.10                 -                        
b                  parameter      int                        param    global > gcd()                 15    4     3     b.11                 -                        
sumTo              function       int (int, int)             -        global                         16    -     2     _Z5sumToii           _Z5sumToii               defined
n                  parameter      int                        param    global > sumTo()               16    4     3     n.12                 -                        
acc                parameter      int                        param    global > sumTo()               16    4     2     acc.13               -                        
countDown          function       int (int)                  -        global                         17    -     2     _Z9countDowni        _Z9countDowni            defined
n                  parameter      int                        param    global > countDown()           17    4     2     n.14                 -                        
invariant          function       int (int, int)             -        global                         19    -     2     _Z9invariantii       _Z9invariantii           defined
n                  parameter      int                        param    global > invariant()           19    4     1     n.15                 -                        
k                  parameter      int                        param    global > invariant()           19    4     2     k.16                 -                        
s                  variable       int                        local    global > invariant()           20    4     3     s.17                 -                        
i                  variable       int                        local    global > invariant() > for     21    4     4     i.18                 -                        
scale              variable       int                        local    global > invariant() > for > for body 22    4     1     scale.19             -                        
notInvariant       function       int (int)                  -        global                         30    -     1     _Z12notInvarianti    _Z12notInvarianti        defined
n                  parameter      int                        param    global > notInvariant()        30    4     1     n.20                 -                        
s                  variable       int                        local    global > notInvariant()        31    4     2     s.21                 -                        
k                  variable       int                        local    global > notInvariant()        31    4     3     k.22                 -                        
i                  variable       int                        local    global > notInvariant() > for  32    4     3     i.23                 -                        
v                  variable       int                        local    global > notInvariant() > for > for body 33    4     1     v.24                 -                        
zeroTrips          function       int (int, int)             -        global                         40    -     2     _Z9zeroTripsii       _Z9zeroTripsii           defined
n                  parameter      int                        param    global > zeroTrips()           40    4     2     n.25                 -                        
d                  parameter      int                        param    global > zeroTrips()           40    4     1     d.26                 -                        
s                  variable       int                        local    global > zeroTrips()           41    4     2     s.27                 -                        
nested             function       int (int, int)             -        global                         46    -     2     _Z6nestedii          _Z6nestedii              defined
rows               parameter      int                        param    global > nested()              46    4     2     rows.28              -                        
cols               parameter      int                        param    global > nested()              46    4     3     cols.29              -                        
grid               variable       int[4][5]                  local    global > nested()              47    80    2     grid.30              -                        
s                  variable       int                        local    global > nested()              47    4     2     s.31                 -                        
r                  variable       int                        local    global > nested() > for        48    4     4     r.32                 -                        
c                  variable       int                        local    global > nested() > for > for body > for 49    4     4     c.33                 -                        
r                  variable       int                        local    global > nested() > for        50    4     3     r.34                 -                        
c                  variable       int                        local    global > nested() > for > for body > for 51    4     3     c.35                 -                        
shared             function       int (int, int, int)        -        global                         55    -     2     _Z6sharediii         _Z6sharediii             defined
x                  parameter      int                        param    global > shared()              55    4     6     x.36                 -                        
y                  parameter      int                        param    global > shared()              55    4     4     y.37                 -                        
flag               parameter      int                        param    global > shared()              55    4     1     flag.38              -                        
a                  variable       int                        local    global > shared()              56    4     1     a.39                 -                        
b                  variable       int                        local    global > shared()              56    4     3     b.40                 -                        
memory             function       int (int)                  -        global                         62    -     2     _Z6memoryi           _Z6memoryi               defined
i                  parameter      int                        param    global > memory()              62    4     5     i.41                 -                        
arr                variable       int[4]                     local    global > memory()              63    16    6     arr.42               -                        
p                  variable       int *                      local    global > memory()              64    4     2     p.43                 -                        
q                  variable       int *                      local    global > memory()              64    4     1     q.44                 -                        
a                  variable       int                        local    global > memory()              66    4     1     a.45                 -                        
b                  variable       int                        local    global > memory()              68    4     1     b.46                 -                        
c                  variable       int                        local    global > memory()              70    4     1     c.47                 -                        
main               function       int (void)                 -        global                         74    -     0     main                 main                     defined
x                  variable       int                        local    global > main()                75    4     2     x.48                 -                        
p                  variable       struct Pair                local    global > main()                77    8     3     p.49                 -                        
t                  variable       int                        local    global > main()                78    4     1     t.50                 -                        
c1                 variable       int                        local    global > main()                80    4     1     c1.51                -                        
c2                 variable       int                        local    global > main()                80    4     1     c2.52                -                        
c3                 variable       int                        local    global > main()                80    4     1     c3.53                -                        

=== Record Layouts ===
struct Pair: size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
