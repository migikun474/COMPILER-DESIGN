=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t16_runtime.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 311 -> 238 instruction(s) for 'test/t16_runtime.c'.

optimization summary (-O1)
    instructions                311 -> 238   (23% fewer)
    constants folded            47
    algebraic simplifications   1
    common subexpressions       1
    copies / constants forwarded 106
    temporaries merged away     4
    dead instructions removed   51
    jumps removed or redirected 9
    unreachable instructions    10

function make(int)        link name: _Z4makei
  symbol table (name, kind, type, width, offset)
    k              param  int                        4      0
    b              local  struct Big                40      8
    i              local  int                        4     48
    t1             temp   double                     8     56
    t2             temp   double                     8     64
    t3             temp   int                        4     72
    t4             temp   int                        4     76
    t5             temp   int                        4     80
    t6             temp   int                        4     84
    t7             temp   int                        4     88
    t8             temp   char                       1     92
    t9             temp   long long                  8     96
    t10            temp   long long                  8    104
    total width 112
  code
 100:     t1 = inttodouble k
 101:     t2 = t1 double* 1.5
 102:     b[0] = t2
 103:     i = 0
 104: L1: if i int>= 5 goto L2
 105:     t3 = i int<< 2                      (w = 4)
 106:     t4 = 8 int+ t3
 107:     t5 = k int+ i
 108:     b[t4] = t5
 109:     i = i int+ 1
 110:     goto L1
 111: L2: t7 = 65 int+ k
 112:     t8 = inttochar t7
 113:     b[28] = t8
 114:     t9 = inttollong k
 115:     t10 = t9 llong* 10000000000
 116:     b[32] = t10
 117:     return b

function weigh(struct Big, double, char, long long)        link name: _Z5weigh3Bigdcx
  symbol table (name, kind, type, width, offset)
    b              param  struct Big                40      0
    scale          param  double                     8     40
    c              param  char                       1     48
    extra          param  long long                  8     56
    t1             temp   double                     8     64
    t2             temp   double                     8     72
    t3             temp   int                        4     80
    t4             temp   double                     8     88
    t5             temp   double                     8     96
    t6             temp   double                     8    104
    t7             temp   double                     8    112
    t8             temp   long long                  8    120
    t9             temp   long long                  8    128
    t10            temp   double                     8    136
    t11            temp   double                     8    144
    t12            temp   double                     8    152
    t13            temp   double                     8    160
    total width 168
  code
 118:   t1 = b[0]
 119:   t2 = t1 double* scale
 120:   t3 = b[24]
 121:   t4 = inttodouble t3
 122:   t5 = t2 double+ t4
 123:   t6 = chartodouble c
 124:   t7 = t5 double+ t6
 125:   t8 = b[32]
 126:   t9 = t8 llong/ 1000000000
 127:   t10 = llongtodouble t9
 128:   t11 = t7 double+ t10
 129:   t12 = llongtodouble extra
 130:   t13 = t11 double+ t12
 131:   return t13

function average(int, ...)        link name: _Z7averageiz
  symbol table (name, kind, type, width, offset)
    count          param  int                        4      0
    ap             local  va_list                    4      4
    total          local  double                     8      8
    i              local  int                        4     16
    tail           local  long long                  8     24
    label          local  char *                     4     32
    t1             temp   double                     8     40
    t2             temp   double                     8     48
    t3             temp   int                        4     56
    t4             temp   long long                  8     64
    t5             temp   char *                     4     72
    t6             temp   double                     8     80
    t7             temp   double                     8     88
    total width 96
  code
 132:     va_start ap, count
 133:     total = 0.0
 134:     i = 0
 135: L3: if i int>= count goto L4
 136:     t1 = va_arg ap, double
 137:     total = total double+ t1
 138:     i = i int+ 1
 139:     goto L3
 140: L4: t4 = va_arg ap, llong
 141:     tail = t4
 142:     t5 = va_arg ap, ptr
 143:     label = t5
 144:     va_end ap
 145:     param "%s %lld\n"
 146:     param t5
 147:     param t4
 148:     call printf, 3
 149:     t6 = inttodouble count
 150:     t7 = total double/ t6
 151:     return t7

function power(long long, int)        link name: _Z5powerxi
  symbol table (name, kind, type, width, offset)
    base           param  long long                  8      0
    n              param  int                        4      8
    t1             temp   long long                  8     16
    t2             temp   int                        4     24
    t3             temp   long long                  8     32
    t4             temp   long long                  8     40
    total width 48
  code
 152:     if n int!= 0 goto L5
 153:     t1 = 1
 154:     goto L6
 155: L5: t2 = n int- 1
 156:     param base
 157:     param t2
 158:     t3 = call power(long long, int), 2
 159:     t1 = base llong* t3
 160: L6: return t1

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    a              local  long long                  8      0
    b              local  long long                  8      8
    u              local  unsigned long long         8     16
    i              local  int                        4     24
    big            local  unsigned int               4     28
    d              local  double                     8     32
    e              local  double                     8     40
    f              local  double                     8     48
    fl             local  float                      4     56
    x              local  float                      4     60
    y              local  float                      4     64
    s              local  struct Big                40     72
    t              local  struct Big                40    112
    p              local  int *                      4    152
    z              local  int *                      4    156
    t1             temp   long long                  8    160
    t2             temp   long long                  8    168
    t3             temp   long long                  8    176
    t4             temp   long long                  8    184
    t5             temp   long long                  8    192
    t6             temp   long long                  8    200
    t7             temp   long long                  8    208
    t8             temp   long long                  8    216
    t9             temp   long long                  8    224
    t10            temp   long long                  8    232
    t11            temp   unsigned long long         8    240
    t12            temp   unsigned long long         8    248
    t13            temp   unsigned long long         8    256
    t14            temp   long long                  8    264
    t15            temp   long long                  8    272
    t16            temp   long long                  8    280
    t17            temp   long long                  8    288
    t18            temp   int                        4    296
    t19            temp   int                        4    300
    t20            temp   int                        4    304
    t21            temp   int                        4    308
    t22            temp   long long                  8    312
    t23            temp   long long                  8    320
    t24            temp   long long                  8    328
    t25            temp   int                        4    336
    t26            temp   double                     8    344
    t27            temp   double                     8    352
    t28            temp   double                     8    360
    t29            temp   float                      4    368
    t30            temp   double                     8    376
    t31            temp   double                     8    384
    t32            temp   int                        4    392
    t33            temp   double                     8    400
    t34            temp   long long                  8    408
    t35            temp   float                      4    416
    t36            temp   double                     8    424
    t37            temp   float                      4    432
    t38            temp   double                     8    440
    t39            temp   float                      4    448
    t40            temp   double                     8    456
    t41            temp   float                      4    464
    t42            temp   double                     8    472
    t43            temp   int                        4    480
    t44            temp   double                     8    488
    t45            temp   int                        4    496
    t46            temp   int                        4    500
    t47            temp   struct Big                40    504
    t48            temp   struct Big *               4    544
    t49            temp   struct Big *               4    548
    t50            temp   struct Big *               4    552
    t51            temp   double                     8    560
    t52            temp   int                        4    568
    t53            temp   int                        4    572
    t54            temp   char                       1    576
    t55            temp   int                        4    580
    t56            temp   long long                  8    584
    t57            temp   double                     8    592
    t58            temp   double                     8    600
    t59            temp   unsigned int               4    608
    t60            temp   void *                     4    612
    t61            temp   int *                      4    616
    t62            temp   int *                      4    620
    t63            temp   unsigned int               4    624
    t64            temp   void *                     4    628
    t65            temp   void *                     4    632
    t66            temp   int                        4    636
    t67            temp   int *                      4    640
    t68            temp   int                        4    644
    t69            temp   int                        4    648
    t70            temp   int *                      4    652
    t71            temp   int                        4    656
    t72            temp   int                        4    660
    t73            temp   int                        4    664
    t74            temp   int *                      4    668
    t75            temp   int                        4    672
    t76            temp   int                        4    676
    t77            temp   long long                  8    680
    t78            temp   int                        4    688
    total width 692
  code
 161:     a = 123456789012345
 162:     b = -987654321
 163:     u = 18000000000000000000
 164:     param "%lld %lld %lld\n"
 165:     param 123455801358024
 166:     param 123457776666666
 167:     param 370370367037035
 168:     call printf, 4
 169:     param "%lld %lld %lld %lld\n"
 170:     param 123456789012
 171:     param 345
 172:     param -124999
 173:     param 986541666
 174:     call printf, 5
 175:     param "%lld %lld\n"
 176:     param -141093474
 177:     param -3
 178:     call printf, 3
 179:     param "%llu %llu %llu\n"
 180:     param 1800000000000000000
 181:     param 0
 182:     param 2250000000000000000
 183:     call printf, 4
 184:     param "%lld %lld %lld %lld\n"
 185:     param 3950617248395040
 186:     param 964506164158
 187:     param -61728396
 188:     param 1099511627776
 189:     call printf, 5
 190:     param "%d %d %d %d\n"
 191:     param 1
 192:     param 1
 193:     param 1
 194:     param 1
 195:     call printf, 5
 196:     param 3
 197:     param 30
 198:     t22 = call power(long long, int), 2
 199:     param "%lld %llx\n"
 200:     param t22
 201:     param 18000000000000000000
 202:     call printf, 3
 203:     param "%lld %lld\n"
 204:     param -123456789012345
 205:     param -123456789012346
 206:     call printf, 3
 207:     i = -7
 208:     big = 3000000000
 209:     d = -7.0
 210:     e = 3e+09
 211:     f = 123456789012345.0
 212:     fl = 3e+09
 213:     param "%.1f %.1f %.1f %.1f\n"
 214:     param -7.0
 215:     param 3e+09
 216:     param 123456789012345.0
 217:     param 3e+09
 218:     call printf, 5
 219:     param "%d %u %lld %d\n"
 220:     param 3
 221:     param 3000000000
 222:     param 12345678901
 223:     param -2
 224:     call printf, 5
 225:     param "%lld %d %d\n"
 226:     param -5000000000
 227:     param -56
 228:     param 4464
 229:     call printf, 4
 230:     x = 1.5
 231:     y = 2.25
 232:     param "%.2f %.2f %.2f %.2f %d\n"
 233:     param 3.75
 234:     param 3.375
 235:     param 0.6666666865348816
 236:     param -1.5
 237:     param 1
 238:     call printf, 6
 239:     param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n"
 240:     param 3.14159
 241:     param -2.5
 242:     param 7.125
 243:     param 2.5
 244:     param 0.1
 245:     call printf, 6
 246:     param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n"
 247:     param -42
 248:     param 42
 249:     param -42
 250:     param 255
 251:     param 255
 252:     param 8
 253:     param "ab"
 254:     param "cd"
 255:     param 122
 256:     call printf, 10
 257:     param "[%*d] [%.*f] [%3s]\n"
 258:     param 6
 259:     param 12
 260:     param 2
 261:     param 1.23456
 262:     param "long string"
 263:     call printf, 6
 264:     param 2
 265:     t47 = call make(int), 1
 266:     s = t47
 267:     t = s
 268:     t[24] = 100
 269:     t51 = s[0]
 270:     t52 = s[24]
 271:     t54 = s[28]
 272:     t55 = chartoint t54
 273:     t56 = s[32]
 274:     param "%.1f %d %d %c %lld\n"
 275:     param t51
 276:     param t52
 277:     param 100
 278:     param t55
 279:     param t56
 280:     call printf, 6
 281:     param s
 282:     param 2.0
 283:     param 97
 284:     param 5
 285:     t57 = call weigh(struct Big, double, char, long long), 4
 286:     param "%.1f\n"
 287:     param t57
 288:     call printf, 2
 289:     param 3
 290:     param 1.0
 291:     param 2.5
 292:     param 4.0
 293:     param 77
 294:     param "tail"
 295:     t58 = call average(int, ...), 6
 296:     param "%.2f\n"
 297:     param t58
 298:     call printf, 2
 299:     param 12
 300:     t60 = call malloc, 1
 301:     p = t60
 302:     *t60 = 1
 303:     t61 = t60 ptr+ 4
 304:     *t61 = 2
 305:     t62 = t60 ptr+ 8
 306:     *t62 = 3
 307:     param t60
 308:     param 24
 309:     t64 = call realloc, 2
 310:     p = t64
 311:     param 4
 312:     param 4
 313:     t65 = call calloc, 2
 314:     z = t65
 315:     t66 = *t64
 316:     t67 = t64 ptr+ 4
 317:     t68 = *t67
 318:     t69 = t66 int+ t68
 319:     t70 = t64 ptr+ 8
 320:     t71 = *t70
 321:     t72 = t69 int+ t71
 322:     t73 = *t65
 323:     t74 = t65 ptr+ 12
 324:     t75 = *t74
 325:     if t64 ptr!= t65 goto L7
 326:     t76 = 0
 327:     goto L8
 328: L7: t76 = 1
 329: L8: param "%d %d %d %d\n"
 330:     param t72
 331:     param t73
 332:     param t75
 333:     param t76
 334:     call printf, 5
 335:     t77 = a llong% 100
 336:     t78 = llongtoint t77
 337:     return t78


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Big                struct_tag     struct Big                 -        global                         8     -     0     Big                  -                        size 40
Big::d             field          double                     member   global > struct Big            8     8     3     Big::d               -                        public, offset 0
Big::n             field          int[5]                     member   global > struct Big            8     20    5     Big::n               -                        public, offset 8
Big::tag           field          char                       member   global > struct Big            8     1     2     Big::tag             -                        public, offset 28
Big::w             field          long long                  member   global > struct Big            8     8     3     Big::w               -                        public, offset 32
make               function       struct Big (int)           -        global                         10    -     1     _Z4makei             _Z4makei                 defined
k                  parameter      int                        param    global > make()                10    4     4     k.1                  -                        
b                  variable       struct Big                 local    global > make()                11    40    5     b.2                  -                        
i                  variable       int                        local    global > make() > for          13    4     4     i.3                  -                        
weigh              function       double (struct Big, double, char, long long) -        global                         19    -     1     _Z5weigh3Bigdcx      _Z5weigh3Bigdcx          defined
b                  parameter      struct Big                 param    global > weigh()               19    40    3     b.4                  -                        
scale              parameter      double                     param    global > weigh()               19    8     1     scale.5              -                        
c                  parameter      char                       param    global > weigh()               19    1     1     c.6                  -                        
extra              parameter      long long                  param    global > weigh()               19    8     1     extra.7              -                        
average            function       double (int, ...)          -        global                         23    -     1     _Z7averageiz         _Z7averageiz             defined
count              parameter      int                        param    global > average()             23    4     3     count.8              -                        
ap                 variable       va_list                    local    global > average()             24    4     5     ap.9                 -                        
total              variable       double                     local    global > average()             26    8     2     total.10             -                        
i                  variable       int                        local    global > average() > for       27    4     2     i.11                 -                        
tail               variable       long long                  local    global > average()             28    8     1     tail.12              -                        
label              variable       char *                     local    global > average()             29    4     1     label.13             -                        
power              function       long long (long long, int) -        global                         35    -     2     _Z5powerxi           _Z5powerxi               defined
base               parameter      long long                  param    global > power()               35    8     2     base.14              -                        
n                  parameter      int                        param    global > power()               35    4     2     n.15                 -                        
main               function       int (void)                 -        global                         37    -     0     main                 main                     defined
a                  variable       long long                  local    global > main()                38    8     17    a.16                 -                        
b                  variable       long long                  local    global > main()                38    8     9     b.17                 -                        
u                  variable       unsigned long long         local    global > main()                39    8     5     u.18                 -                        
i                  variable       int                        local    global > main()                49    4     1     i.19                 -                        
big                variable       unsigned int               local    global > main()                50    4     2     big.20               -                        
d                  variable       double                     local    global > main()                51    8     1     d.21                 -                        
e                  variable       double                     local    global > main()                51    8     1     e.22                 -                        
f                  variable       double                     local    global > main()                51    8     1     f.23                 -                        
fl                 variable       float                      local    global > main()                52    4     1     fl.24                -                        
x                  variable       float                      local    global > main()                56    4     5     x.25                 -                        
y                  variable       float                      local    global > main()                56    4     4     y.26                 -                        
s                  variable       struct Big                 local    global > main()                63    40    6     s.27                 -                        
t                  variable       struct Big                 local    global > main()                64    40    2     t.28                 -                        
p                  variable       int *                      local    global > main()                70    4     9     p.29                 -                        
z                  variable       int *                      local    global > main()                73    4     3     z.30                 -                        

=== Record Layouts ===
struct Big: size 40, align 8
    +0  double d  [public]
    +8  int[5] n  [public]
    +28  char tag  [public]
    +32  long long w  [public]
