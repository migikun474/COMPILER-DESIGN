=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t16_runtime.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 311 -> 220 instruction(s) for 'test/t16_runtime.c'.

optimization summary (-O2)
    instructions                311 -> 220   (29% fewer)
    constants folded            49
    algebraic simplifications   1
    common subexpressions       1
    copies / constants forwarded 108
    temporaries merged away     4
    dead instructions removed   53
    jumps removed or redirected 9
    unreachable instructions    10
    propagated across blocks    1
    dead assignments removed    16

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
 141:     t5 = va_arg ap, ptr
 142:     va_end ap
 143:     param "%s %lld\n"
 144:     param t5
 145:     param t4
 146:     call printf, 3
 147:     t6 = inttodouble count
 148:     t7 = total double/ t6
 149:     return t7

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
 150:     if n int!= 0 goto L5
 151:     t1 = 1
 152:     goto L6
 153: L5: t2 = n int- 1
 154:     param base
 155:     param t2
 156:     t3 = call power(long long, int), 2
 157:     t1 = base llong* t3
 158: L6: return t1

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
 159:     param "%lld %lld %lld\n"
 160:     param 123455801358024
 161:     param 123457776666666
 162:     param 370370367037035
 163:     call printf, 4
 164:     param "%lld %lld %lld %lld\n"
 165:     param 123456789012
 166:     param 345
 167:     param -124999
 168:     param 986541666
 169:     call printf, 5
 170:     param "%lld %lld\n"
 171:     param -141093474
 172:     param -3
 173:     call printf, 3
 174:     param "%llu %llu %llu\n"
 175:     param 1800000000000000000
 176:     param 0
 177:     param 2250000000000000000
 178:     call printf, 4
 179:     param "%lld %lld %lld %lld\n"
 180:     param 3950617248395040
 181:     param 964506164158
 182:     param -61728396
 183:     param 1099511627776
 184:     call printf, 5
 185:     param "%d %d %d %d\n"
 186:     param 1
 187:     param 1
 188:     param 1
 189:     param 1
 190:     call printf, 5
 191:     param 3
 192:     param 30
 193:     t22 = call power(long long, int), 2
 194:     param "%lld %llx\n"
 195:     param t22
 196:     param 18000000000000000000
 197:     call printf, 3
 198:     param "%lld %lld\n"
 199:     param -123456789012345
 200:     param -123456789012346
 201:     call printf, 3
 202:     param "%.1f %.1f %.1f %.1f\n"
 203:     param -7.0
 204:     param 3e+09
 205:     param 123456789012345.0
 206:     param 3e+09
 207:     call printf, 5
 208:     param "%d %u %lld %d\n"
 209:     param 3
 210:     param 3000000000
 211:     param 12345678901
 212:     param -2
 213:     call printf, 5
 214:     param "%lld %d %d\n"
 215:     param -5000000000
 216:     param -56
 217:     param 4464
 218:     call printf, 4
 219:     param "%.2f %.2f %.2f %.2f %d\n"
 220:     param 3.75
 221:     param 3.375
 222:     param 0.6666666865348816
 223:     param -1.5
 224:     param 1
 225:     call printf, 6
 226:     param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n"
 227:     param 3.14159
 228:     param -2.5
 229:     param 7.125
 230:     param 2.5
 231:     param 0.1
 232:     call printf, 6
 233:     param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n"
 234:     param -42
 235:     param 42
 236:     param -42
 237:     param 255
 238:     param 255
 239:     param 8
 240:     param "ab"
 241:     param "cd"
 242:     param 122
 243:     call printf, 10
 244:     param "[%*d] [%.*f] [%3s]\n"
 245:     param 6
 246:     param 12
 247:     param 2
 248:     param 1.23456
 249:     param "long string"
 250:     call printf, 6
 251:     param 2
 252:     t47 = call make(int), 1
 253:     s = t47
 254:     t = s
 255:     t[24] = 100
 256:     t51 = s[0]
 257:     t52 = s[24]
 258:     t54 = s[28]
 259:     t55 = chartoint t54
 260:     t56 = s[32]
 261:     param "%.1f %d %d %c %lld\n"
 262:     param t51
 263:     param t52
 264:     param 100
 265:     param t55
 266:     param t56
 267:     call printf, 6
 268:     param s
 269:     param 2.0
 270:     param 97
 271:     param 5
 272:     t57 = call weigh(struct Big, double, char, long long), 4
 273:     param "%.1f\n"
 274:     param t57
 275:     call printf, 2
 276:     param 3
 277:     param 1.0
 278:     param 2.5
 279:     param 4.0
 280:     param 77
 281:     param "tail"
 282:     t58 = call average(int, ...), 6
 283:     param "%.2f\n"
 284:     param t58
 285:     call printf, 2
 286:     param 12
 287:     t60 = call malloc, 1
 288:     *t60 = 1
 289:     t61 = t60 ptr+ 4
 290:     *t61 = 2
 291:     t62 = t60 ptr+ 8
 292:     *t62 = 3
 293:     param t60
 294:     param 24
 295:     t64 = call realloc, 2
 296:     param 4
 297:     param 4
 298:     t65 = call calloc, 2
 299:     t66 = *t64
 300:     t67 = t64 ptr+ 4
 301:     t68 = *t67
 302:     t69 = t66 int+ t68
 303:     t70 = t64 ptr+ 8
 304:     t71 = *t70
 305:     t72 = t69 int+ t71
 306:     t73 = *t65
 307:     t74 = t65 ptr+ 12
 308:     t75 = *t74
 309:     if t64 ptr!= t65 goto L7
 310:     t76 = 0
 311:     goto L8
 312: L7: t76 = 1
 313: L8: param "%d %d %d %d\n"
 314:     param t72
 315:     param t73
 316:     param t75
 317:     param t76
 318:     call printf, 5
 319:     return 45


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
