=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t25_control.c
Optimization : no optimization

Three address code generated: 5 function(s), 298 instruction(s) for 'test/t25_control.c'.

function classify(const char *)        link name: _Z8classifyPKc
  symbol table (name, kind, type, width, offset)
    s              param  const char *               4      0
    state          local  int                        4      4
    c              local  char                       1      8
    digit          local  int                        4     12
    letter         local  int                        4     16
    t1             temp   char                       1     20
    t2             temp   char                       1     21
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    t5             temp   int                        4     32
    t6             temp   int                        4     36
    t7             temp   int                        4     40
    t8             temp   int                        4     44
    t9             temp   int                        4     48
    t10            temp   int                        4     52
    t11            temp   int                        4     56
    t12            temp   const char *               4     60
    total width 64
  code
 100:      state = 0
 101: L1:  t1 = *s
 102:      if t1 char!= 0 goto L2
 103:      goto L32
 104: L2:  t2 = *s
 105:      c = t2
 106:      t4 = chartoint c
 107:      if t4 int>= 48 goto L3
 108:      goto L4
 109: L3:  t5 = chartoint c
 110:      if t5 int<= 57 goto L5
 111:      goto L4
 112: L4:  t3 = 0
 113:      goto L6
 114: L5:  t3 = 1
 115: L6:  digit = t3
 116:      t7 = chartoint c
 117:      if t7 int>= 97 goto L7
 118:      goto L8
 119: L7:  t8 = chartoint c
 120:      if t8 int<= 122 goto L10
 121:      goto L8
 122: L8:  t9 = chartoint c
 123:      if t9 int== 95 goto L10
 124:      goto L9
 125: L9:  t6 = 0
 126:      goto L11
 127: L10: t6 = 1
 128: L11: letter = t6
 129:      t10 = state
 130:      goto L30
 131: L12: if digit int!= 0 goto L13
 132:      goto L14
 133: L13: state = 1
 134:      goto L17
 135: L14: if letter int!= 0 goto L15
 136:      goto L16
 137: L15: state = 3
 138:      goto L17
 139: L16: return 0
 140: L17: goto L31
 141: L18: t11 = chartoint c
 142:      if t11 int== 46 goto L19
 143:      goto L20
 144: L19: state = 2
 145:      goto L22
 146: L20: if digit int!= 0 goto L22
 147:      goto L21
 148: L21: return 0
 149: L22: goto L31
 150: L23: if digit int!= 0 goto L25
 151:      goto L24
 152: L24: return 0
 153: L25: goto L31
 154: L26: if digit int!= 0 goto L29
 155:      goto L27
 156: L27: if letter int!= 0 goto L29
 157:      goto L28
 158: L28: return 0
 159: L29: goto L31
 160:      goto L31
 161: L30: if t10 int== 0 goto L12
 162:      if t10 int== 1 goto L18
 163:      if t10 int== 2 goto L23
 164:      if t10 int== 3 goto L26
 165: L31: t12 = s ptr+ 1
 166:      s = t12
 167:      goto L1
 168: L32: return state

function daysIn(int, int)        link name: _Z6daysInii
  symbol table (name, kind, type, width, offset)
    month          param  int                        4      0
    year           param  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    total width 28
  code
 169:      t1 = month
 170:      goto L41
 171: L33: return 30
 172: L34: t3 = year int% 4
 173:      if t3 int== 0 goto L35
 174:      goto L36
 175: L35: t4 = year int% 100
 176:      if t4 int!= 0 goto L37
 177:      goto L36
 178: L36: t5 = year int% 400
 179:      if t5 int== 0 goto L37
 180:      goto L38
 181: L37: t2 = 29
 182:      goto L39
 183: L38: t2 = 28
 184: L39: return t2
 185: L40: return 31
 186:      goto L42
 187: L41: if t1 int== 4 goto L33
 188:      if t1 int== 6 goto L33
 189:      if t1 int== 9 goto L33
 190:      if t1 int== 11 goto L33
 191:      if t1 int== 2 goto L34
 192:      goto L40
 193: L42: return

function grade(int)        link name: _Z5gradei
  symbol table (name, kind, type, width, offset)
    score          param  int                        4      0
    t1             temp   char *                     4      4
    t2             temp   char *                     4      8
    t3             temp   char *                     4     12
    total width 16
  code
 194:      if score int>= 90 goto L43
 195:      goto L44
 196: L43: t1 = "A"
 197:      goto L51
 198: L44: if score int>= 75 goto L45
 199:      goto L46
 200: L45: t2 = "B"
 201:      goto L50
 202: L46: if score int>= 60 goto L47
 203:      goto L48
 204: L47: t3 = "C"
 205:      goto L49
 206: L48: t3 = "F"
 207: L49: t2 = t3
 208: L50: t1 = t2
 209: L51: return t1

function firstPair(int)        link name: _Z9firstPairi
  symbol table (name, kind, type, width, offset)
    target         param  int                        4      0
    i              local  int                        4      4
    j              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    t5             temp   int                        4     28
    t6             temp   int                        4     32
    total width 36
  code
 210:      i = 1
 211: L52: if i int< 10 goto L53
 212:      goto L59
 213: L53: j = i
 214: L54: if j int< 10 goto L55
 215:      goto L58
 216: L55: t1 = i int* j
 217:      if t1 int== target goto L56
 218:      goto L57
 219: L56: goto L60
 220: L57: t2 = j int+ 1
 221:      j = t2
 222:      goto L54
 223: L58: t3 = i int+ 1
 224:      i = t3
 225:      goto L52
 226: L59: t4 = int- 1
 227:      return t4
 228: L60: t5 = i int* 10
 229:      t6 = t5 int+ j
 230:      return t6

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    triangle       local  int                        4      0
    skipped        local  int                        4      4
    i              local  int                        4      8
    j              local  int                        4     12
    n              local  int                        4     16
    digits         local  int                        4     20
    value          local  int                        4     24
    a              local  int                        4     28
    b              local  int                        4     32
    c              local  int                        4     36
    steps          local  int                        4     40
    k              local  int                        4     44
    countdown      local  int                        4     48
    t1             temp   int                        4     52
    t2             temp   int                        4     56
    t3             temp   int                        4     60
    t4             temp   int                        4     64
    t5             temp   int                        4     68
    t6             temp   int                        4     72
    t7             temp   int                        4     76
    t8             temp   int                        4     80
    t9             temp   int                        4     84
    t10            temp   const char *               4     88
    t11            temp   const char *               4     92
    t12            temp   const char *               4     96
    t13            temp   const char *               4    100
    t14            temp   int                        4    104
    t15            temp   int                        4    108
    t16            temp   int                        4    112
    t17            temp   int                        4    116
    t18            temp   int                        4    120
    t19            temp   int                        4    124
    t20            temp   int                        4    128
    t21            temp   int                        4    132
    t22            temp   int                        4    136
    t23            temp   int                        4    140
    t24            temp   int                        4    144
    t25            temp   int                        4    148
    t26            temp   int                        4    152
    t27            temp   int                        4    156
    t28            temp   int                        4    160
    t29            temp   int                        4    164
    t30            temp   int                        4    168
    t31            temp   int                        4    172
    t32            temp   int                        4    176
    t33            temp   int                        4    180
    t34            temp   int                        4    184
    t35            temp   int                        4    188
    t36            temp   int                        4    192
    t37            temp   int                        4    196
    t38            temp   int                        4    200
    t39            temp   int                        4    204
    t40            temp   int                        4    208
    total width 212
  code
 231:      param "1234"
 232:      t1 = call classify(const char *), 1
 233:      param "12.5"
 234:      t2 = call classify(const char *), 1
 235:      param "x_9"
 236:      t3 = call classify(const char *), 1
 237:      param "9x"
 238:      t4 = call classify(const char *), 1
 239:      param ""
 240:      t5 = call classify(const char *), 1
 241:      param "%d %d %d %d %d\n"
 242:      param t1
 243:      param t2
 244:      param t3
 245:      param t4
 246:      param t5
 247:      call printf, 6
 248:      param 2
 249:      param 2024
 250:      t6 = call daysIn(int, int), 2
 251:      param 2
 252:      param 1900
 253:      t7 = call daysIn(int, int), 2
 254:      param 2
 255:      param 2000
 256:      t8 = call daysIn(int, int), 2
 257:      param 11
 258:      param 2023
 259:      t9 = call daysIn(int, int), 2
 260:      param "%d %d %d %d\n"
 261:      param t6
 262:      param t7
 263:      param t8
 264:      param t9
 265:      call printf, 5
 266:      param 95
 267:      t10 = call grade(int), 1
 268:      param 80
 269:      t11 = call grade(int), 1
 270:      param 60
 271:      t12 = call grade(int), 1
 272:      param 10
 273:      t13 = call grade(int), 1
 274:      param "%s %s %s %s\n"
 275:      param t10
 276:      param t11
 277:      param t12
 278:      param t13
 279:      call printf, 5
 280:      param 24
 281:      t14 = call firstPair(int), 1
 282:      param 49
 283:      t15 = call firstPair(int), 1
 284:      param 97
 285:      t16 = call firstPair(int), 1
 286:      param "%d %d %d\n"
 287:      param t14
 288:      param t15
 289:      param t16
 290:      call printf, 4
 291:      triangle = 0
 292:      skipped = 0
 293:      i = 1
 294: L61: if i int<= 6 goto L62
 295:      goto L73
 296: L62: if i int== 4 goto L63
 297:      goto L64
 298: L63: t17 = skipped int+ 1
 299:      skipped = t17
 300:      goto L72
 301: L64: j = 1
 302: L65: if j int<= 6 goto L66
 303:      goto L72
 304: L66: if j int> i goto L67
 305:      goto L68
 306: L67: goto L72
 307: L68: t18 = i int+ j
 308:      t19 = t18 int% 2
 309:      if t19 int!= 0 goto L69
 310:      goto L70
 311: L69: goto L71
 312: L70: t20 = i int* j
 313:      t21 = triangle int+ t20
 314:      triangle = t21
 315: L71: t22 = j int+ 1
 316:      j = t22
 317:      goto L65
 318: L72: t23 = i int+ 1
 319:      i = t23
 320:      goto L61
 321: L73: param "%d %d\n"
 322:      param triangle
 323:      param skipped
 324:      call printf, 3
 325:      n = 0
 326:      digits = 0
 327:      value = 90210
 328: L74: t24 = digits int+ 1
 329:      digits = t24
 330:      t25 = value int/ 10
 331:      value = t25
 332:      if value int!= 0 goto L74
 333:      goto L75
 334: L75: t26 = n int* n
 335:      if t26 int> 200 goto L77
 336:      goto L76
 337: L76: t27 = n int+ 1
 338:      n = t27
 339:      goto L75
 340: L77: a = 0
 341:      b = 10
 342: L78: if a int< b goto L79
 343:      goto L80
 344: L79: t28 = a int+ 1
 345:      a = t28
 346:      t29 = b int- 1
 347:      b = t29
 348:      goto L78
 349: L80: t30 = a int+ 1
 350:      a = t30
 351:      t31 = b int+ 2
 352:      b = t31
 353:      t32 = a int+ b
 354:      c = t32
 355:      param "%d %d %d %d %d\n"
 356:      param digits
 357:      param n
 358:      param a
 359:      param b
 360:      param c
 361:      call printf, 6
 362:      steps = 0
 363:      k = 27
 364: L81: goto L82
 365: L82: if k int== 1 goto L83
 366:      goto L84
 367: L83: goto L89
 368: L84: t34 = k int% 2
 369:      if t34 int!= 0 goto L85
 370:      goto L86
 371: L85: t35 = 3 int* k
 372:      t36 = t35 int+ 1
 373:      t33 = t36
 374:      goto L87
 375: L86: t37 = k int/ 2
 376:      t33 = t37
 377: L87: k = t33
 378:      t38 = steps int+ 1
 379:      steps = t38
 380:      if t38 int> 200 goto L88
 381:      goto L81
 382: L88: goto L89
 383:      goto L81
 384: L89: countdown = 3
 385: L90: t39 = countdown
 386:      t40 = countdown int- 1
 387:      countdown = t40
 388:      if t39 int> 0 goto L91
 389:      goto L92
 390: L91: param "%d "
 391:      param countdown
 392:      call printf, 2
 393:      goto L90
 394: L92: param "\n%d\n"
 395:      param steps
 396:      call printf, 2
 397:      return digits


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
classify           function       int (const char *)         -        global                         9     -     5     _Z8classifyPKc       _Z8classifyPKc           defined
s                  parameter      const char *               param    global > classify()            9     4     3     s.1                  -                        
state              variable       int                        local    global > classify()            10    4     5     state.2              -                        
c                  variable       char                       local    global > classify() > for > for body 12    1     6     c.3                  -                        
digit              variable       int                        local    global > classify() > for > for body 13    4     4     digit.4              -                        
letter             variable       int                        local    global > classify() > for > for body 13    4     2     letter.5             -                        
daysIn             function       int (int, int)             -        global                         35    -     4     _Z6daysInii          _Z6daysInii              defined
month              parameter      int                        param    global > daysIn()              35    4     1     month.6              -                        
year               parameter      int                        param    global > daysIn()              35    4     3     year.7               -                        
grade              function       const char *(int)          -        global                         43    -     4     _Z5gradei            _Z5gradei                defined
score              parameter      int                        param    global > grade()               43    4     3     score.8              -                        
firstPair          function       int (int)                  -        global                         47    -     3     _Z9firstPairi        _Z9firstPairi            defined
target             parameter      int                        param    global > firstPair()           47    4     1     target.9             -                        
found              label          -                          -        global > firstPair()           53    -     1     _Z9firstPairi.found  -                        
i                  variable       int                        local    global > firstPair()           48    4     6     i.10                 -                        
j                  variable       int                        local    global > firstPair()           48    4     5     j.11                 -                        
main               function       int (void)                 -        global                         57    -     0     main                 main                     defined
triangle           variable       int                        local    global > main()                63    4     2     triangle.12          -                        
skipped            variable       int                        local    global > main()                63    4     2     skipped.13           -                        
i                  variable       int                        local    global > main() > for          64    4     6     i.14                 -                        
j                  variable       int                        local    global > main() > for > for body > for 66    4     5     j.15                 -                        
n                  variable       int                        local    global > main()                74    4     4     n.16                 -                        
digits             variable       int                        local    global > main()                74    4     3     digits.17            -                        
value              variable       int                        local    global > main()                74    4     2     value.18             -                        
a                  variable       int                        local    global > main()                77    4     6     a.19                 -                        
b                  variable       int                        local    global > main()                77    4     6     b.20                 -                        
c                  variable       int                        local    global > main()                77    4     2     c.21                 -                        
steps              variable       int                        local    global > main()                82    4     2     steps.22             -                        
k                  variable       int                        local    global > main()                82    4     5     k.23                 -                        
countdown          variable       int                        local    global > main()                88    4     2     countdown.24         -                        

=== Record Layouts ===
(no records)
