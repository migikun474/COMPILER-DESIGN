=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t26_declarations.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 198 -> 176 instruction(s) for 'test/t26_declarations.c'.

optimization summary (-O1)
    instructions                198 -> 176   (11% fewer)
    constants folded            8
    algebraic simplifications   3
    common subexpressions       3
    copies / constants forwarded 16
    temporaries merged away     4
    dead instructions removed   11
    jumps removed or redirected 4
    unreachable instructions    2

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
 102: L1: if i int>= 4 goto L2
 103:     t1 = i int<< 2
 104:     t2 = r ptr+ t1
 105:     t3 = *t2
 106:     s = s int+ t3
 107:     i = i int+ 1
 108:     goto L1
 109: L2: return s

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
 110:     r[0] = 4
 111:     r[4] = 9
 112:     r[8] = 2
 113:     r[12] = 4
 114:     t3 = &r
 115:     param t3
 116:     t4 = call sum(const int *), 1
 117:     t5 = &primes
 118:     param t5
 119:     t6 = call sum(const int *), 1
 120:     t7 = t4 int+ t6
 121:     n = t7
 122:     t10 = 9
 123:     if t7 int<= 100 goto L3
 124:     t11 = n
 125:     goto L4
 126: L3: t11 = 100
 127: L4: param "%d %d %d\n"
 128:     param n
 129:     param t10
 130:     param t11
 131:     call printf, 4
 132:     param "%d %d %d %d\n"
 133:     param 24
 134:     param 80
 135:     param 32
 136:     param 16
 137:     call printf, 5
 138:     param "%d %d %d\n"
 139:     param 24
 140:     param 2
 141:     param 3
 142:     call printf, 4
 143:     box[0] = 97
 144:     box[8] = 1.5
 145:     box[16] = 2
 146:     box[24] = 98
 147:     box[32] = 2.5
 148:     box[40] = 4
 149:     box[48] = 99
 150:     box[56] = 0.0
 151:     box[64] = 8
 152:     box[72] = 0
 153:     t13 = box[16]
 154:     t14 = shorttoint t13
 155:     t15 = box[40]
 156:     t16 = shorttoint t15
 157:     t17 = t14 int+ t16
 158:     t18 = box[64]
 159:     t19 = shorttoint t18
 160:     t20 = t17 int+ t19
 161:     box[72] = t20
 162:     t21 = &box
 163:     t22 = t21 ptr+ 48
 164:     it = t22
 165:     t23 = box[32]
 166:     t24 = t23 double* 2.0
 167:     t25 = t22 ptr+ 8
 168:     *t25 = t24
 169:     t26 = box[72]
 170:     t29 = box[48]
 171:     t30 = chartoint t29
 172:     t31 = stock[8]
 173:     t32 = stock[16]
 174:     t33 = shorttodouble t32
 175:     t34 = t31 double* t33
 176:     param "%d %.1f %c %.1f\n"
 177:     param t26
 178:     param t24
 179:     param t30
 180:     param t34
 181:     call printf, 5
 182:     m[0] = 120
 183:     m[4] = 1
 184:     m[8] = 121
 185:     m[10] = 2
 186:     m[16] = 3.5
 187:     m[24] = 122
 188:     copy = m
 189:     copy[4] = 100
 190:     t36 = m[0]
 191:     t37 = chartoint t36
 192:     t38 = m[4]
 193:     t39 = m[8]
 194:     t40 = chartoint t39
 195:     t41 = m[10]
 196:     t42 = shorttoint t41
 197:     t43 = m[16]
 198:     t44 = m[24]
 199:     t45 = chartoint t44
 200:     param "%c %d %c %d %.1f %c %d\n"
 201:     param t37
 202:     param t38
 203:     param t40
 204:     param t42
 205:     param t43
 206:     param t45
 207:     param 100
 208:     call printf, 8
 209:     t47 = &letters
 210:     t48 = table[0]
 211:     t49 = table[8]
 212:     t50 = table[16]
 213:     t51 = matrix[20]
 214:     t52 = matrix[0]
 215:     t53 = t51 int- t52
 216:     param "%s %.1f %.1f %.1f %d\n"
 217:     param t47
 218:     param t48
 219:     param t49
 220:     param t50
 221:     param t53
 222:     call printf, 6
 223:     grid[0] = 1
 224:     grid[4] = 0
 225:     grid[8] = 0
 226:     grid[12] = 0
 227:     grid[16] = 0
 228:     grid[20] = 2
 229:     grid[24] = 0
 230:     grid[28] = 0
 231:     grid[32] = 0
 232:     grid[36] = 0
 233:     grid[40] = 3
 234:     grid[44] = 0
 235:     trace = 0
 236:     i = 0
 237: L5: if i int>= 3 goto L6
 238:     t54 = i int<< 2                     (n2 = 4)
 239:     t55 = t54 int+ i
 240:     t56 = t55 int<< 2                   (w = 4)
 241:     t57 = grid[t56]
 242:     trace = trace int+ t57
 243:     i = i int+ 1
 244:     goto L5
 245: L6: words[0] = "one"
 246:     words[4] = "two"
 247:     words[8] = "three"
 248:     rows[0] = 97
 249:     rows[1] = 98
 250:     rows[2] = 0
 251:     rows[3] = 0
 252:     rows[4] = 0
 253:     rows[5] = 0
 254:     rows[6] = 99
 255:     rows[7] = 100
 256:     rows[8] = 101
 257:     rows[9] = 0
 258:     rows[10] = 0
 259:     rows[11] = 0
 260:     t60 = words[8]
 261:     t61 = rows[8]
 262:     t62 = chartoint t61
 263:     t63 = &rows
 264:     param "%d %s %c %s %d\n"
 265:     param trace
 266:     param t60
 267:     param t62
 268:     param t63
 269:     param 3
 270:     call printf, 6
 271:     sensor = 5
 272:     fast = 10
 273:     t66 = 10 int+ kept.17
 274:     deduced = t66
 275:     return t66


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
