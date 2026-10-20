=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t26_declarations.c
Optimization : no optimization

Three address code generated: 2 function(s), 198 instruction(s) for 'test/t26_declarations.c'.

globals (name, type, width, initial value)
    primes         const int[4]              16  { +0: 2, +4: 3, +8: 5, +12: 7 }
    matrix         int[2][3]                 24  { +0: 1, +4: 2, +8: 3, +12: 4, +16: 5, +20: 6 }
    letters        char[3]                    3  { +0: 111, +1: 107, +2: 0 }
    stock          Item                      24  { +0: 115, +8: 2.5, +16: 3 }
    table          double[3]                 24  { +16: 9.5, +0: 1.5 }
    kept.17        int                        4  3

function sum(const int *)        link name: _Z3sumPKi
  symbol table (name, kind, type, width, offset)
    r              param  const int *                4      0
    s              local  int                        4      4
    i              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   const int *                4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    t5             temp   int                        4     28
    total width 32
  code
 100:     s = 0
 101:     i = 0
 102: L1: if i int< 4 goto L2
 103:     goto L3
 104: L2: t1 = i int* 4
 105:     t2 = r ptr+ t1
 106:     t3 = *t2
 107:     t4 = s int+ t3
 108:     s = t4
 109:     t5 = i int+ 1
 110:     i = t5
 111:     goto L1
 112: L3: return s

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    r              local  int[4]                    16      0
    n              local  int                        4     16
    box            local  Box                       80     24
    it             local  Item *                     4    104
    m              local  struct Mixed              32    112
    copy           local  struct Mixed              32    144
    grid           local  int[3][4]                 48    176
    trace          local  int                        4    224
    i              local  int                        4    228
    words          local  const char *[3]           12    232
    rows           local  char[2][6]                12    244
    sensor         local  int                        4    256
    fast           local  int                        4    260
    deduced        local  int                        4    264
    t1             temp   int                        4    268
    t2             temp   int                        4    272
    t3             temp   int (*)[4]                 4    276
    t4             temp   int                        4    280
    t5             temp   const int (*)[4]           4    284
    t6             temp   int                        4    288
    t7             temp   int                        4    292
    t8             temp   int                        4    296
    t9             temp   int                        4    300
    t10            temp   int                        4    304
    t11            temp   int                        4    308
    t12            temp   unsigned int               4    312
    t13            temp   short                      2    316
    t14            temp   int                        4    320
    t15            temp   short                      2    324
    t16            temp   int                        4    328
    t17            temp   int                        4    332
    t18            temp   short                      2    336
    t19            temp   int                        4    340
    t20            temp   int                        4    344
    t21            temp   Item *                     4    348
    t22            temp   Item *                     4    352
    t23            temp   double                     8    360
    t24            temp   double                     8    368
    t25            temp   Item *                     4    376
    t26            temp   int                        4    380
    t27            temp   Item *                     4    384
    t28            temp   double                     8    392
    t29            temp   char                       1    400
    t30            temp   int                        4    404
    t31            temp   double                     8    408
    t32            temp   short                      2    416
    t33            temp   double                     8    424
    t34            temp   double                     8    432
    t35            temp   struct Mixed *             4    440
    t36            temp   char                       1    444
    t37            temp   int                        4    448
    t38            temp   int                        4    452
    t39            temp   char                       1    456
    t40            temp   int                        4    460
    t41            temp   short                      2    464
    t42            temp   int                        4    468
    t43            temp   double                     8    472
    t44            temp   char                       1    480
    t45            temp   int                        4    484
    t46            temp   int                        4    488
    t47            temp   char (*)[3]                4    492
    t48            temp   double                     8    496
    t49            temp   double                     8    504
    t50            temp   double                     8    512
    t51            temp   int                        4    520
    t52            temp   int                        4    524
    t53            temp   int                        4    528
    t54            temp   int                        4    532
    t55            temp   int                        4    536
    t56            temp   int                        4    540
    t57            temp   int                        4    544
    t58            temp   int                        4    548
    t59            temp   int                        4    552
    t60            temp   const char *               4    556
    t61            temp   char                       1    560
    t62            temp   int                        4    564
    t63            temp   char (*)[6]                4    568
    t64            temp   unsigned int               4    572
    t65            temp   int                        4    576
    t66            temp   int                        4    580
    total width 584
  code
 113:      t1 = 2 int* 2
 114:      if 3 int> 9 goto L4
 115:      goto L5
 116: L4:  t2 = 3
 117:      goto L6
 118: L5:  t2 = 9
 119: L6:  r[0] = t1
 120:      r[4] = t2
 121:      r[8] = 2
 122:      r[12] = 4
 123:      t3 = &r
 124:      param t3
 125:      t4 = call sum(const int *), 1
 126:      t5 = &primes
 127:      param t5
 128:      t6 = call sum(const int *), 1
 129:      t7 = t4 int+ t6
 130:      n = t7
 131:      t8 = 1 int+ 2
 132:      t9 = 1 int+ 2
 133:      t10 = t8 int* t9
 134:      if n int> 100 goto L7
 135:      goto L8
 136: L7:  t11 = n
 137:      goto L9
 138: L8:  t11 = 100
 139: L9:  param "%d %d %d\n"
 140:      param n
 141:      param t10
 142:      param t11
 143:      call printf, 4
 144:      param "%d %d %d %d\n"
 145:      param 24
 146:      param 80
 147:      param 32
 148:      param 16
 149:      call printf, 5
 150:      t12 = 24 uint/ 12
 151:      param "%d %d %d\n"
 152:      param 24
 153:      param t12
 154:      param 3
 155:      call printf, 4
 156:      box[0] = 97
 157:      box[8] = 1.5
 158:      box[16] = 2
 159:      box[24] = 98
 160:      box[32] = 2.5
 161:      box[40] = 4
 162:      box[48] = 99
 163:      box[56] = 0.0
 164:      box[64] = 8
 165:      box[72] = 0
 166:      t13 = box[16]
 167:      t14 = shorttoint t13
 168:      t15 = box[40]
 169:      t16 = shorttoint t15
 170:      t17 = t14 int+ t16
 171:      t18 = box[64]
 172:      t19 = shorttoint t18
 173:      t20 = t17 int+ t19
 174:      box[72] = t20
 175:      t21 = &box
 176:      t22 = t21 ptr+ 48
 177:      it = t22
 178:      t23 = box[32]
 179:      t24 = t23 double* 2.0
 180:      t25 = it ptr+ 8
 181:      *t25 = t24
 182:      t26 = box[72]
 183:      t27 = it ptr+ 8
 184:      t28 = *t27
 185:      t29 = box[48]
 186:      t30 = chartoint t29
 187:      t31 = stock[8]
 188:      t32 = stock[16]
 189:      t33 = shorttodouble t32
 190:      t34 = t31 double* t33
 191:      param "%d %.1f %c %.1f\n"
 192:      param t26
 193:      param t28
 194:      param t30
 195:      param t34
 196:      call printf, 5
 197:      m[0] = 120
 198:      m[4] = 1
 199:      m[8] = 121
 200:      m[10] = 2
 201:      m[16] = 3.5
 202:      m[24] = 122
 203:      copy = m
 204:      t35 = &copy
 205:      copy[4] = 100
 206:      t36 = m[0]
 207:      t37 = chartoint t36
 208:      t38 = m[4]
 209:      t39 = m[8]
 210:      t40 = chartoint t39
 211:      t41 = m[10]
 212:      t42 = shorttoint t41
 213:      t43 = m[16]
 214:      t44 = m[24]
 215:      t45 = chartoint t44
 216:      t46 = copy[4]
 217:      param "%c %d %c %d %.1f %c %d\n"
 218:      param t37
 219:      param t38
 220:      param t40
 221:      param t42
 222:      param t43
 223:      param t45
 224:      param t46
 225:      call printf, 8
 226:      t47 = &letters
 227:      t48 = table[0]
 228:      t49 = table[8]
 229:      t50 = table[16]
 230:      t51 = matrix[20]
 231:      t52 = matrix[0]
 232:      t53 = t51 int- t52
 233:      param "%s %.1f %.1f %.1f %d\n"
 234:      param t47
 235:      param t48
 236:      param t49
 237:      param t50
 238:      param t53
 239:      call printf, 6
 240:      grid[0] = 1
 241:      grid[4] = 0
 242:      grid[8] = 0
 243:      grid[12] = 0
 244:      grid[16] = 0
 245:      grid[20] = 2
 246:      grid[24] = 0
 247:      grid[28] = 0
 248:      grid[32] = 0
 249:      grid[36] = 0
 250:      grid[40] = 3
 251:      grid[44] = 0
 252:      trace = 0
 253:      i = 0
 254: L10: if i int< 3 goto L11
 255:      goto L12
 256: L11: t54 = i int* 4                      (n2 = 4)
 257:      t55 = t54 int+ i
 258:      t56 = t55 int* 4                    (w = 4)
 259:      t57 = grid[t56]
 260:      t58 = trace int+ t57
 261:      trace = t58
 262:      t59 = i int+ 1
 263:      i = t59
 264:      goto L10
 265: L12: words[0] = "one"
 266:      words[4] = "two"
 267:      words[8] = "three"
 268:      rows[0] = 97
 269:      rows[1] = 98
 270:      rows[2] = 0
 271:      rows[3] = 0
 272:      rows[4] = 0
 273:      rows[5] = 0
 274:      rows[6] = 99
 275:      rows[7] = 100
 276:      rows[8] = 101
 277:      rows[9] = 0
 278:      rows[10] = 0
 279:      rows[11] = 0
 280:      t60 = words[8]
 281:      t61 = rows[8]
 282:      t62 = chartoint t61
 283:      t63 = &rows
 284:      t64 = 12 uint/ 4
 285:      param "%d %s %c %s %d\n"
 286:      param trace
 287:      param t60
 288:      param t62
 289:      param t63
 290:      param t64
 291:      call printf, 6
 292:      sensor = 5
 293:      t65 = sensor int* 2
 294:      fast = t65
 295:      t66 = fast int+ kept.17
 296:      deduced = t66
 297:      return deduced


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Number             typedef        int                        -        global                         15    -     0     Number               -                        
Row                typedef        int[4]                     -        global                         16    -     0     Row                  -                        
(unnamed at 17:9)  struct_tag     struct (unnamed at 17:9)   -        global                         17    -     0     (unnamed at 17:9)    -                        size 24
(unnamed at 17:9)::tag field          char                       member   global > struct (unnamed at 17:9) 17    1     1     (unnamed at 17:9)::tag -                        public, offset 0
(unnamed at 17:9)::weight field          double                     member   global > struct (unnamed at 17:9) 17    8     4     (unnamed at 17:9)::weight -                        public, offset 8
(unnamed at 17:9)::count field          short                      member   global > struct (unnamed at 17:9) 17    2     4     (unnamed at 17:9)::count -                        public, offset 16
Item               typedef        Item                       -        global                         17    -     0     Item                 -                        
(unnamed at 18:9)  struct_tag     struct (unnamed at 18:9)   -        global                         18    -     0     (unnamed at 18:9)    -                        size 80
(unnamed at 18:9)::first field          Item                       member   global > struct (unnamed at 18:9) 18    24    1     (unnamed at 18:9)::first -                        public, offset 0
(unnamed at 18:9)::rest field          Item[2]                    member   global > struct (unnamed at 18:9) 18    48    5     (unnamed at 18:9)::rest -                        public, offset 24
(unnamed at 18:9)::total field          int                        member   global > struct (unnamed at 18:9) 18    4     2     (unnamed at 18:9)::total -                        public, offset 72
Box                typedef        Box                        -        global                         18    -     0     Box                  -                        
Mixed              struct_tag     struct Mixed               -        global                         19    -     0     Mixed                -                        size 32
Mixed::a           field          char                       member   global > struct Mixed          19    1     1     Mixed::a             -                        public, offset 0
Mixed::b           field          int                        member   global > struct Mixed          19    4     3     Mixed::b             -                        public, offset 4
Mixed::c           field          char                       member   global > struct Mixed          19    1     1     Mixed::c             -                        public, offset 8
Mixed::d           field          short                      member   global > struct Mixed          19    2     1     Mixed::d             -                        public, offset 10
Mixed::e           field          double                     member   global > struct Mixed          19    8     1     Mixed::e             -                        public, offset 16
Mixed::f           field          char                       member   global > struct Mixed          19    1     1     Mixed::f             -                        public, offset 24
primes             variable       const int[4]               global   global                         21    16    1     primes               -                        
matrix             variable       int[2][3]                  global   global                         22    24    5     matrix               -                        
letters            variable       char[3]                    global   global                         23    3     2     letters              -                        
stock              variable       Item                       global   global                         24    24    2     stock                -                        
table              variable       double[3]                  global   global                         25    24    3     table                -                        
sum                function       int (const int *)          -        global                         27    -     2     _Z3sumPKi            _Z3sumPKi                defined
r                  parameter      const int *                param    global > sum()                 27    4     1     r.1                  -                        
s                  variable       int                        local    global > sum()                 27    4     2     s.2                  -                        
i                  variable       int                        local    global > sum() > for           27    4     3     i.3                  -                        
main               function       int (void)                 -        global                         29    -     0     main                 main                     defined
r                  variable       int[4]                     local    global > main()                30    16    1     r.4                  -                        
n                  variable       int                        local    global > main()                31    4     3     n.5                  -                        
box                variable       Box                        local    global > main()                36    80    8     box.6                -                        
it                 variable       Item *                     local    global > main()                38    4     2     it.7                 -                        
m                  variable       struct Mixed               local    global > main()                42    32    7     m.8                  -                        
copy               variable       struct Mixed               local    global > main()                43    32    2     copy.9               -                        
grid               variable       int[3][4]                  local    global > main()                48    48    1     grid.10              -                        
trace              variable       int                        local    global > main()                49    4     2     trace.11             -                        
i                  variable       int                        local    global > main() > for          50    4     4     i.12                 -                        
words              variable       const char *[3]            local    global > main()                51    12    3     words.13             -                        
rows               variable       char[2][6]                 local    global > main()                52    12    2     rows.14              -                        
sensor             variable       int                        local    global > main()                54    4     1     sensor.15            -                        
fast               variable       int                        local    global > main()                55    4     1     fast.16              -                        
kept               variable       int                        static   global > main()                56    4     1     kept.17              -                        static
deduced            variable       int                        local    global > main()                57    4     1     deduced.18           -                        

=== Record Layouts ===
struct (unnamed at 17:9): size 24, align 8
    +0  char tag  [public]
    +8  double weight  [public]
    +16  short count  [public]
struct (unnamed at 18:9): size 80, align 8
    +0  Item first  [public]
    +24  Item[2] rest  [public]
    +72  int total  [public]
struct Mixed: size 32, align 8
    +0  char a  [public]
    +4  int b  [public]
    +8  char c  [public]
    +10  short d  [public]
    +16  double e  [public]
    +24  char f  [public]
