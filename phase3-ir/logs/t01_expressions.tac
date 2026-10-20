=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t01_expressions.c
Optimization : no optimization

Three address code generated: 1 function(s), 199 instruction(s) for 'test/t01_expressions.c'.

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    a              local  int                        4      0
    b              local  int                        4      4
    c              local  int                        4      8
    d              local  double                     8     16
    f              local  float                      4     24
    truncated      local  int                        4     28
    u              local  unsigned int               4     32
    neg            local  int                        4     36
    ch             local  char                       1     40
    s              local  short                      2     42
    big            local  long long                  8     48
    i              local  int                        4     56
    j              local  int                        4     60
    big2           local  int                        4     64
    mixed          local  double                     8     72
    wraps          local  unsigned char              1     80
    t1             temp   int                        4     84
    t2             temp   int                        4     88
    t3             temp   int                        4     92
    t4             temp   int                        4     96
    t5             temp   int                        4    100
    t6             temp   int                        4    104
    t7             temp   int                        4    108
    t8             temp   int                        4    112
    t9             temp   int                        4    116
    t10            temp   int                        4    120
    t11            temp   int                        4    124
    t12            temp   int                        4    128
    t13            temp   int                        4    132
    t14            temp   int                        4    136
    t15            temp   int                        4    140
    t16            temp   int                        4    144
    t17            temp   double                     8    152
    t18            temp   double                     8    160
    t19            temp   float                      4    168
    t20            temp   float                      4    172
    t21            temp   double                     8    176
    t22            temp   int                        4    184
    t23            temp   double                     8    192
    t24            temp   unsigned int               4    200
    t25            temp   unsigned int               4    204
    t26            temp   unsigned int               4    208
    t27            temp   unsigned int               4    212
    t28            temp   unsigned int               4    216
    t29            temp   int                        4    220
    t30            temp   int                        4    224
    t31            temp   int                        4    228
    t32            temp   int                        4    232
    t33            temp   int                        4    236
    t34            temp   int                        4    240
    t35            temp   int                        4    244
    t36            temp   int                        4    248
    t37            temp   int                        4    252
    t38            temp   int                        4    256
    t39            temp   char                       1    260
    t40            temp   int                        4    264
    t41            temp   int                        4    268
    t42            temp   short                      2    272
    t43            temp   long long                  8    280
    t44            temp   long long                  8    288
    t45            temp   long long                  8    296
    t46            temp   int                        4    304
    t47            temp   int                        4    308
    t48            temp   int                        4    312
    t49            temp   int                        4    316
    t50            temp   int                        4    320
    t51            temp   int                        4    324
    t52            temp   int                        4    328
    t53            temp   int                        4    332
    t54            temp   int                        4    336
    t55            temp   int                        4    340
    t56            temp   int                        4    344
    t57            temp   int                        4    348
    t58            temp   double                     8    352
    t59            temp   double                     8    360
    t60            temp   int                        4    368
    t61            temp   int                        4    372
    t62            temp   int                        4    376
    t63            temp   int                        4    380
    t64            temp   int                        4    384
    t65            temp   int                        4    388
    t66            temp   int                        4    392
    t67            temp   int                        4    396
    t68            temp   int                        4    400
    t69            temp   int                        4    404
    t70            temp   int                        4    408
    t71            temp   double                     8    416
    t72            temp   double                     8    424
    t73            temp   double                     8    432
    t74            temp   int                        4    440
    t75            temp   int                        4    444
    t76            temp   unsigned char              1    448
    t77            temp   int                        4    452
    t78            temp   int                        4    456
    t79            temp   int                        4    460
    total width 464
  code
 100:     a = 7
 101:     b = 3
 102:     t1 = b int* 2
 103:     t2 = a int+ t1
 104:     t3 = a int/ b
 105:     t4 = t2 int- t3
 106:     t5 = a int% b
 107:     t6 = t4 int+ t5
 108:     c = t6
 109:     t7 = a int- b
 110:     t8 = a int* b
 111:     t9 = a int/ b
 112:     t10 = a int% b
 113:     param "%d %d %d %d %d\n"
 114:     param c
 115:     param t7
 116:     param t8
 117:     param t9
 118:     param t10
 119:     call printf, 6
 120:     t11 = int- a
 121:     t12 = b int* t11
 122:     t13 = int- a
 123:     t14 = b int* t13
 124:     t15 = t12 int+ t14
 125:     c = t15
 126:     param "%d\n"
 127:     param c
 128:     call printf, 2
 129:     d = 1.5
 130:     f = 2.5
 131:     t16 = a int* 2
 132:     t17 = inttodouble t16
 133:     t18 = d double+ t17
 134:     d = t18
 135:     t19 = inttofloat b
 136:     t20 = f float* t19
 137:     f = t20
 138:     t21 = d double/ 2.0
 139:     t22 = doubletoint t21
 140:     truncated = t22
 141:     t23 = floattodouble f
 142:     param "%.2f %.2f %d\n"
 143:     param d
 144:     param t23
 145:     param truncated
 146:     call printf, 4
 147:     u = 7
 148:     t24 = u uint/ 3
 149:     t25 = u uint<< 2
 150:     t26 = t24 uint+ t25
 151:     t27 = u uint>> 1
 152:     t28 = t26 uint+ t27
 153:     u = t28
 154:     t29 = int- 16
 155:     neg = t29
 156:     t30 = neg int>> 2
 157:     t31 = neg int/ 3
 158:     t32 = neg int% 3
 159:     param "%u %d %d %d\n"
 160:     param u
 161:     param t30
 162:     param t31
 163:     param t32
 164:     call printf, 5
 165:     t33 = a int& b
 166:     t34 = a int| b
 167:     t35 = a int^ b
 168:     t36 = int~ a
 169:     param "%d %d %d %d\n"
 170:     param t33
 171:     param t34
 172:     param t35
 173:     param t36
 174:     call printf, 5
 175:     ch = 65
 176:     t37 = chartoint ch
 177:     t38 = t37 int+ 2
 178:     t39 = inttochar t38
 179:     ch = t39
 180:     s = 300
 181:     t40 = shorttoint s
 182:     t41 = t40 int* 2
 183:     t42 = inttoshort t41
 184:     s = t42
 185:     big = 100000
 186:     t43 = big llong* big
 187:     t44 = inttollong a
 188:     t45 = t43 llong+ t44
 189:     big = t45
 190:     t46 = chartoint ch
 191:     t47 = chartoint ch
 192:     t48 = shorttoint s
 193:     param "%c %d %d %lld\n"
 194:     param t46
 195:     param t47
 196:     param t48
 197:     param big
 198:     call printf, 5
 199:     t49 = a int+ 5
 200:     a = t49
 201:     t50 = b int- 1
 202:     b = t50
 203:     t51 = c int* 2
 204:     c = t51
 205:     t52 = a int/ 3
 206:     a = t52
 207:     t53 = b int<< 3
 208:     b = t53
 209:     t54 = c int% 7
 210:     c = t54
 211:     t55 = a int| 8
 212:     a = t55
 213:     t56 = b int& 12
 214:     b = t56
 215:     t57 = c int^ 5
 216:     c = t57
 217:     t58 = d double- 0.5
 218:     d = t58
 219:     t59 = d double* 2.0
 220:     d = t59
 221:     param "%d %d %d %.1f\n"
 222:     param a
 223:     param b
 224:     param c
 225:     param d
 226:     call printf, 5
 227:     i = 5
 228:     t60 = i
 229:     t61 = i int+ 1
 230:     i = t61
 231:     t62 = t60 int+ 1
 232:     j = t62
 233:     param "%d %d\n"
 234:     param i
 235:     param j
 236:     call printf, 3
 237:     t63 = i int+ 1
 238:     i = t63
 239:     t64 = t63 int* 2
 240:     j = t64
 241:     param "%d %d\n"
 242:     param i
 243:     param j
 244:     call printf, 3
 245:     t65 = i
 246:     t66 = i int- 1
 247:     i = t66
 248:     t67 = i int- 1
 249:     i = t67
 250:     t68 = t65 int- t67
 251:     j = t68
 252:     j = 3
 253:     t69 = j int+ 4
 254:     i = t69
 255:     param "%d %d\n"
 256:     param i
 257:     param j
 258:     call printf, 3
 259:     if a int> b goto L1
 260:     goto L2
 261: L1: t70 = a
 262:     goto L3
 263: L2: t70 = b
 264: L3: big2 = t70
 265:     if a int> 100 goto L4
 266:     goto L5
 267: L4: t71 = 1.0
 268:     goto L6
 269: L5: t71 = 2.5
 270: L6: mixed = t71
 271:     param "%d %.1f\n"
 272:     param big2
 273:     param mixed
 274:     call printf, 3
 275:     param "%d %d %d\n"
 276:     param 4
 277:     param 8
 278:     param 1
 279:     call printf, 4
 280:     t72 = inttodouble a
 281:     t73 = t72 double/ 4.0
 282:     param "%d %.3f %d\n"
 283:     param 3
 284:     param t73
 285:     param 65
 286:     call printf, 4
 287:     wraps = 250
 288:     t74 = uchartoint wraps
 289:     t75 = t74 int+ 10
 290:     t76 = inttouchar t75
 291:     wraps = t76
 292:     t77 = uchartoint wraps
 293:     param "%d\n"
 294:     param t77
 295:     call printf, 2
 296:     t78 = a int+ b
 297:     t79 = t78 int% 256
 298:     return t79


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
main               function       int (void)                 -        global                         5     -     0     main                 main                     defined
a                  variable       int                        local    global > main()                6     4     24    a.1                  -                        
b                  variable       int                        local    global > main()                6     4     20    b.2                  -                        
c                  variable       int                        local    global > main()                6     4     8     c.3                  -                        
d                  variable       double                     local    global > main()                12    8     7     d.4                  -                        
f                  variable       float                      local    global > main()                13    4     3     f.5                  -                        
truncated          variable       int                        local    global > main()                16    4     1     truncated.6          -                        
u                  variable       unsigned int               local    global > main()                19    4     5     u.7                  -                        
neg                variable       int                        local    global > main()                21    4     3     neg.8                -                        
ch                 variable       char                       local    global > main()                25    1     4     ch.9                 -                        
s                  variable       short                      local    global > main()                27    2     3     s.10                 -                        
big                variable       long long                  local    global > main()                29    8     4     big.11               -                        
i                  variable       int                        local    global > main()                36    4     8     i.12                 -                        
j                  variable       int                        local    global > main()                36    4     8     j.13                 -                        
big2               variable       int                        local    global > main()                45    4     1     big2.14              -                        
mixed              variable       double                     local    global > main()                46    8     1     mixed.15             -                        
wraps              variable       unsigned char              local    global > main()                50    1     3     wraps.16             -                        

=== Record Layouts ===
(no records)
