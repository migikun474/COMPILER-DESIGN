=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t17_strings.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 348 -> 285 instruction(s) for 'test/t17_strings.c'.

optimization summary (-O1)
    instructions                348 -> 285   (18% fewer)
    constants folded            3
    algebraic simplifications   3
    common subexpressions       10
    copies / constants forwarded 16
    temporaries merged away     23
    dead instructions removed   13
    jumps removed or redirected 26
    unreachable instructions    2

function length(const char *)        link name: _Z6lengthPKc
  symbol table (name, kind, type, width, offset)
    s              param  const char *               4      0
    n              local  int                        4      4
    t1             temp   const char *               4      8
    t2             temp   char                       1     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    total width 24
  code
 100:     n = 0
 101: L1: t1 = s ptr+ n
 102:     t2 = *t1
 103:     t3 = chartoint t2
 104:     if t3 int== 0 goto L2
 105:     n = n int+ 1
 106:     goto L1
 107: L2: return n

function copy(char *, const char *)        link name: _Z4copyPcPKc
  symbol table (name, kind, type, width, offset)
    to             param  char *                     4      0
    from           param  const char *               4      4
    t1             temp   char *                     4      8
    t2             temp   char *                     4     12
    t3             temp   const char *               4     16
    t4             temp   const char *               4     20
    t5             temp   char                       1     24
    t6             temp   int                        4     28
    total width 32
  code
 108: L3: t1 = to
 109:     to = to ptr+ 1
 110:     t3 = from
 111:     from = from ptr+ 1
 112:     t5 = *t3
 113:     *t1 = t5
 114:     t6 = chartoint t5
 115:     if t6 int!= 0 goto L3
 116:     return

function compare(const char *, const char *)        link name: _Z7comparePKcS0_
  symbol table (name, kind, type, width, offset)
    a              param  const char *               4      0
    b              param  const char *               4      4
    t1             temp   char                       1      8
    t2             temp   char                       1      9
    t3             temp   int                        4     12
    t4             temp   char                       1     16
    t5             temp   int                        4     20
    t6             temp   const char *               4     24
    t7             temp   const char *               4     28
    t8             temp   char                       1     32
    t9             temp   int                        4     36
    t10            temp   char                       1     40
    t11            temp   int                        4     44
    t12            temp   int                        4     48
    total width 52
  code
 117: L4: t1 = *a
 118:     if t1 char== 0 goto L5
 119:     t2 = *a
 120:     t3 = chartoint t2
 121:     t4 = *b
 122:     t5 = chartoint t4
 123:     if t3 int!= t5 goto L5
 124:     a = a ptr+ 1
 125:     b = b ptr+ 1
 126:     goto L4
 127: L5: t8 = *a
 128:     t9 = chartoint t8
 129:     t10 = *b
 130:     t11 = chartoint t10
 131:     t12 = t9 int- t11
 132:     return t12

function reverse(char *)        link name: _Z7reversePc
  symbol table (name, kind, type, width, offset)
    s              param  char *                     4      0
    i              local  int                        4      4
    j              local  int                        4      8
    t              local  char                       1     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   char *                     4     24
    t4             temp   char                       1     28
    t5             temp   char *                     4     32
    t6             temp   char *                     4     36
    t7             temp   char                       1     40
    t8             temp   char *                     4     44
    t9             temp   int                        4     48
    t10            temp   int                        4     52
    total width 56
  code
 133:     i = 0
 134:     param s
 135:     t1 = call length(const char *), 1
 136:     j = t1 int- 1
 137: L6: if i int>= j goto L7
 138:     t3 = s ptr+ i
 139:     t4 = *t3
 140:     t = t4
 141:     t6 = s ptr+ j
 142:     t7 = *t6
 143:     *t3 = t7
 144:     *t6 = t4
 145:     i = i int+ 1
 146:     j = j int- 1
 147:     goto L6
 148: L7: return

function find(const char *, char)        link name: _Z4findPKcc
  symbol table (name, kind, type, width, offset)
    text           param  const char *               4      0
    c              param  char                       1      4
    i              local  int                        4      8
    t1             temp   const char *               4     12
    t2             temp   char                       1     16
    t3             temp   const char *               4     20
    t4             temp   char                       1     24
    t5             temp   int                        4     28
    t6             temp   int                        4     32
    t7             temp   int                        4     36
    t8             temp   int                        4     40
    total width 44
  code
 149:      i = 0
 150: L8:  t1 = text ptr+ i
 151:      t2 = *t1
 152:      if t2 char== 0 goto L10
 153:      t3 = text ptr+ i
 154:      t4 = *t3
 155:      t5 = chartoint t4
 156:      t6 = chartoint c
 157:      if t5 int!= t6 goto L9
 158:      return i
 159: L9:  i = i int+ 1
 160:      goto L8
 161: L10: return -1

function toNumber(const char *)        link name: _Z8toNumberPKc
  symbol table (name, kind, type, width, offset)
    s              param  const char *               4      0
    sign           local  int                        4      4
    v              local  int                        4      8
    t1             temp   char                       1     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   const char *               4     24
    t5             temp   char                       1     28
    t6             temp   int                        4     32
    t7             temp   char                       1     36
    t8             temp   int                        4     40
    t9             temp   int                        4     44
    t10            temp   char                       1     48
    t11            temp   int                        4     52
    t12            temp   int                        4     56
    t13            temp   int                        4     60
    t14            temp   const char *               4     64
    t15            temp   int                        4     68
    total width 72
  code
 162:      sign = 1
 163:      v = 0
 164:      t1 = *s
 165:      t2 = chartoint t1
 166:      if t2 int!= 45 goto L11
 167:      sign = -1
 168:      s = s ptr+ 1
 169: L11: t5 = *s
 170:      t6 = chartoint t5
 171:      if t6 int< 48 goto L12
 172:      t7 = *s
 173:      t8 = chartoint t7
 174:      if t8 int> 57 goto L12
 175:      t9 = v int* 10
 176:      t10 = *s
 177:      t11 = chartoint t10
 178:      t12 = t11 int- 48
 179:      v = t9 int+ t12
 180:      s = s ptr+ 1
 181:      goto L11
 182: L12: t15 = sign int* v
 183:      return t15

function toText(int, char *)        link name: _Z6toTextiPc
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    out            param  char *                     4      4
    tmp            local  char[12]                  12      8
    n              local  int                        4     20
    neg            local  int                        4     24
    t1             temp   int                        4     28
    t2             temp   int                        4     32
    t3             temp   int                        4     36
    t4             temp   int                        4     40
    t5             temp   int                        4     44
    t6             temp   int                        4     48
    t7             temp   char                       1     52
    t8             temp   int                        4     56
    t9             temp   int                        4     60
    t10            temp   int                        4     64
    t11            temp   char *                     4     68
    t12            temp   char *                     4     72
    t13            temp   int                        4     76
    t14            temp   char                       1     80
    total width 84
  code
 184:      n = 0
 185:      if v int< 0 goto L13
 186:      t1 = 0
 187:      goto L14
 188: L13: t1 = 1
 189: L14: neg = t1
 190:      if t1 int== 0 goto L15
 191:      v = int- v
 192: L15: t3 = n
 193:      n = n int+ 1
 194:      t5 = v int% 10
 195:      t6 = 48 int+ t5
 196:      t7 = inttochar t6
 197:      tmp[t3] = t7
 198:      t8 = v int/ 10
 199:      v = t8
 200:      if t8 int> 0 goto L15
 201:      if neg int== 0 goto L16
 202:      t9 = n
 203:      n = n int+ 1
 204:      tmp[t9] = 45
 205: L16: if n int<= 0 goto L17
 206:      t11 = out
 207:      out = out ptr+ 1
 208:      t13 = n int- 1
 209:      n = t13
 210:      t14 = tmp[t13]
 211:      *t11 = t14
 212:      goto L16
 213: L17: *out = 0
 214:      return

function isPalindrome(const char *)        link name: _Z12isPalindromePKc
  symbol table (name, kind, type, width, offset)
    s              param  const char *               4      0
    i              local  int                        4      4
    j              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    t5             temp   const char *               4     28
    t6             temp   char                       1     32
    t7             temp   int                        4     36
    t8             temp   int                        4     40
    t9             temp   int                        4     44
    t10            temp   const char *               4     48
    t11            temp   char                       1     52
    t12            temp   int                        4     56
    total width 60
  code
 215:      i = 0
 216:      param s
 217:      t1 = call length(const char *), 1
 218:      j = t1 int- 1
 219: L18: if i int>= j goto L19
 220:      t3 = i
 221:      i = i int+ 1
 222:      t5 = s ptr+ t3
 223:      t6 = *t5
 224:      t7 = chartoint t6
 225:      t8 = j
 226:      j = j int- 1
 227:      t10 = s ptr+ t8
 228:      t11 = *t10
 229:      t12 = chartoint t11
 230:      if t7 int== t12 goto L18
 231:      return 0
 232: L19: return 1

function countWords(const char *)        link name: _Z10countWordsPKc
  symbol table (name, kind, type, width, offset)
    s              param  const char *               4      0
    words          local  int                        4      4
    inside         local  int                        4      8
    t1             temp   char                       1     12
    t2             temp   char                       1     13
    t3             temp   int                        4     16
    t4             temp   char                       1     20
    t5             temp   int                        4     24
    t6             temp   int                        4     28
    t7             temp   const char *               4     32
    total width 36
  code
 233:      words = 0
 234:      inside = 0
 235: L20: t1 = *s
 236:      if t1 char== 0 goto L24
 237:      t2 = *s
 238:      t3 = chartoint t2
 239:      if t3 int== 32 goto L21
 240:      t4 = *s
 241:      t5 = chartoint t4
 242:      if t5 int!= 9 goto L22
 243: L21: inside = 0
 244:      goto L23
 245: L22: if inside int!= 0 goto L23
 246:      inside = 1
 247:      words = words int+ 1
 248: L23: s = s ptr+ 1
 249:      goto L20
 250: L24: return words

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    buf            local  char[32]                  32      0
    num            local  char[16]                  16     32
    names          local  const char *[3]           12     48
    smallest       local  int                        4     60
    i.32           local  int                        4     64
    upper          local  char[8]                    8     68
    i.34           local  int                        4     76
    t1             temp   char (*)[32]               4     80
    t2             temp   char (*)[32]               4     84
    t3             temp   char (*)[32]               4     88
    t4             temp   int                        4     92
    t5             temp   char (*)[32]               4     96
    t6             temp   char (*)[32]               4    100
    t7             temp   char (*)[32]               4    104
    t8             temp   int                        4    108
    t9             temp   char (*)[32]               4    112
    t10            temp   int                        4    116
    t11            temp   int                        4    120
    t12            temp   int                        4    124
    t13            temp   int                        4    128
    t14            temp   int                        4    132
    t15            temp   int                        4    136
    t16            temp   int                        4    140
    t17            temp   const char *               4    144
    t18            temp   int                        4    148
    t19            temp   const char *               4    152
    t20            temp   int                        4    156
    t21            temp   int                        4    160
    t22            temp   int                        4    164
    t23            temp   const char *               4    168
    t24            temp   const char *               4    172
    t25            temp   const char *               4    176
    t26            temp   char                       1    180
    t27            temp   int                        4    184
    t28            temp   int                        4    188
    t29            temp   char (*)[16]               4    192
    t30            temp   char (*)[16]               4    196
    t31            temp   char (*)[16]               4    200
    t32            temp   int                        4    204
    t33            temp   int                        4    208
    t34            temp   int                        4    212
    t35            temp   int                        4    216
    t36            temp   int                        4    220
    t37            temp   int                        4    224
    t38            temp   char                       1    228
    t39            temp   char                       1    229
    t40            temp   int                        4    232
    t41            temp   char                       1    236
    t42            temp   int                        4    240
    t43            temp   char                       1    244
    t44            temp   int                        4    248
    t45            temp   int                        4    252
    t46            temp   int                        4    256
    t47            temp   char                       1    260
    t48            temp   int                        4    264
    t49            temp   char (*)[8]                4    268
    t50            temp   const char *               4    272
    t51            temp   int                        4    276
    t52            temp   char                       1    280
    t53            temp   int                        4    284
    t54            temp   int                        4    288
    total width 292
  code
 251:      names[0] = "delta"
 252:      names[4] = "alpha"
 253:      names[8] = "charlie"
 254:      t1 = &buf
 255:      param t1
 256:      param "compiler"
 257:      call copy(char *, const char *), 2
 258:      param t1
 259:      t4 = call length(const char *), 1
 260:      param "%s %d\n"
 261:      param t1
 262:      param t4
 263:      call printf, 3
 264:      param t1
 265:      call reverse(char *), 1
 266:      param t1
 267:      param 112
 268:      t8 = call find(const char *, char), 2
 269:      param t1
 270:      param 122
 271:      t10 = call find(const char *, char), 2
 272:      param "%s %d %d\n"
 273:      param t1
 274:      param t8
 275:      param t10
 276:      call printf, 4
 277:      param "abc"
 278:      param "abd"
 279:      t12 = call compare(const char *, const char *), 2
 280:      if t12 int< 0 goto L25
 281:      t11 = 0
 282:      goto L26
 283: L25: t11 = 1
 284: L26: param "abc"
 285:      param "abc"
 286:      t13 = call compare(const char *, const char *), 2
 287:      param "b"
 288:      param "abc"
 289:      t15 = call compare(const char *, const char *), 2
 290:      if t15 int> 0 goto L27
 291:      t14 = 0
 292:      goto L28
 293: L27: t14 = 1
 294: L28: param "%d %d %d\n"
 295:      param t11
 296:      param t13
 297:      param t14
 298:      call printf, 4
 299:      smallest = 0
 300:      i.32 = 1
 301: L29: if i.32 int>= 3 goto L31
 302:      t16 = i.32 int<< 2                  (w = 4)
 303:      t17 = names[t16]
 304:      t18 = smallest int<< 2              (w = 4)
 305:      t19 = names[t18]
 306:      param t17
 307:      param t19
 308:      t20 = call compare(const char *, const char *), 2
 309:      if t20 int>= 0 goto L30
 310:      smallest = i.32
 311: L30: i.32 = i.32 int+ 1
 312:      goto L29
 313: L31: t22 = smallest int<< 2              (w = 4)
 314:      t23 = names[t22]
 315:      t24 = names[8]
 316:      t25 = t24 ptr+ 3
 317:      t26 = *t25
 318:      t27 = chartoint t26
 319:      param "%s %c\n"
 320:      param t23
 321:      param t27
 322:      call printf, 3
 323:      t29 = &num
 324:      param -40213
 325:      param t29
 326:      call toText(int, char *), 2
 327:      param t29
 328:      t32 = call toNumber(const char *), 1
 329:      t33 = t32 int+ 1
 330:      param "77x"
 331:      t34 = call toNumber(const char *), 1
 332:      param "%s %d %d\n"
 333:      param t29
 334:      param t33
 335:      param t34
 336:      call printf, 4
 337:      param "level"
 338:      t35 = call isPalindrome(const char *), 1
 339:      param "lever"
 340:      t36 = call isPalindrome(const char *), 1
 341:      param "  the quick  brown fox "
 342:      t37 = call countWords(const char *), 1
 343:      param "%d %d %d\n"
 344:      param t35
 345:      param t36
 346:      param t37
 347:      call printf, 4
 348:      upper[0] = 109
 349:      upper[1] = 105
 350:      upper[2] = 120
 351:      upper[3] = 101
 352:      upper[4] = 100
 353:      upper[5] = 0
 354:      upper[6] = 0
 355:      upper[7] = 0
 356:      i.34 = 0
 357: L32: t38 = upper[i.34]
 358:      if t38 char== 0 goto L34
 359:      t39 = upper[i.34]
 360:      t40 = chartoint t39
 361:      if t40 int< 97 goto L33
 362:      t41 = upper[i.34]
 363:      t42 = chartoint t41
 364:      if t42 int> 122 goto L33
 365:      t43 = upper[i.34]
 366:      t44 = chartoint t43
 367:      t45 = t44 int- 97
 368:      t46 = t45 int+ 65
 369:      t47 = inttochar t46
 370:      upper[i.34] = t47
 371: L33: i.34 = i.34 int+ 1
 372:      goto L32
 373: L34: t49 = &upper
 374:      param "%s %d\n"
 375:      param t49
 376:      param 8
 377:      call printf, 3
 378:      t50 = names[4]
 379:      param t50
 380:      t51 = call length(const char *), 1
 381:      t52 = buf[0]
 382:      t53 = chartoint t52
 383:      t54 = t51 int+ t53
 384:      return t54


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
length             function       int (const char *)         -        global                         5     -     4     _Z6lengthPKc         _Z6lengthPKc             defined
s                  parameter      const char *               param    global > length()              5     4     1     s.1                  -                        
n                  variable       int                        local    global > length()              5     4     3     n.2                  -                        
copy               function       void (char *, const char *) -        global                         7     -     1     _Z4copyPcPKc         _Z4copyPcPKc             defined
to                 parameter      char *                     param    global > copy()                7     4     1     to.3                 -                        
from               parameter      const char *               param    global > copy()                7     4     1     from.4               -                        
compare            function       int (const char *, const char *) -        global                         9     -     4     _Z7comparePKcS0_     _Z7comparePKcS0_         defined
a                  parameter      const char *               param    global > compare()             9     4     4     a.5                  -                        
b                  parameter      const char *               param    global > compare()             9     4     3     b.6                  -                        
reverse            function       void (char *)              -        global                         14    -     1     _Z7reversePc         _Z7reversePc             defined
s                  parameter      char *                     param    global > reverse()             14    4     5     s.7                  -                        
i                  variable       int                        local    global > reverse()             15    4     4     i.8                  -                        
j                  variable       int                        local    global > reverse()             15    4     4     j.9                  -                        
t                  variable       char                       local    global > reverse() > while     16    1     1     t.10                 -                        
find               function       int (const char *, char)   -        global                         19    -     2     _Z4findPKcc          _Z4findPKcc              defined
text               parameter      const char *               param    global > find()                19    4     2     text.11              -                        
c                  parameter      char                       param    global > find()                19    1     1     c.12                 -                        
i                  variable       int                        local    global > find() > for          20    4     4     i.13                 -                        
toNumber           function       int (const char *)         -        global                         24    -     2     _Z8toNumberPKc       _Z8toNumberPKc           defined
s                  parameter      const char *               param    global > toNumber()            24    4     6     s.14                 -                        
sign               variable       int                        local    global > toNumber()            25    4     2     sign.15              -                        
v                  variable       int                        local    global > toNumber()            25    4     3     v.16                 -                        
toText             function       void (int, char *)         -        global                         31    -     1     _Z6toTextiPc         _Z6toTextiPc             defined
v                  parameter      int                        param    global > toText()              31    4     6     v.17                 -                        
out                parameter      char *                     param    global > toText()              31    4     2     out.18               -                        
tmp                variable       char[12]                   local    global > toText()              32    12    3     tmp.19               -                        
n                  variable       int                        local    global > toText()              33    4     4     n.20                 -                        
neg                variable       int                        local    global > toText()              33    4     2     neg.21               -                        
isPalindrome       function       int (const char *)         -        global                         41    -     2     _Z12isPalindromePKc  _Z12isPalindromePKc      defined
s                  parameter      const char *               param    global > isPalindrome()        41    4     3     s.22                 -                        
i                  variable       int                        local    global > isPalindrome()        42    4     2     i.23                 -                        
j                  variable       int                        local    global > isPalindrome()        42    4     2     j.24                 -                        
countWords         function       int (const char *)         -        global                         47    -     1     _Z10countWordsPKc    _Z10countWordsPKc        defined
s                  parameter      const char *               param    global > countWords()          47    4     4     s.25                 -                        
words              variable       int                        local    global > countWords()          48    4     2     words.26             -                        
inside             variable       int                        local    global > countWords()          48    4     3     inside.27            -                        
main               function       int (void)                 -        global                         56    -     0     main                 main                     defined
buf                variable       char[32]                   local    global > main()                57    32    8     buf.28               -                        
num                variable       char[16]                   local    global > main()                57    16    3     num.29               -                        
names              variable       const char *[3]            local    global > main()                58    12    5     names.30             -                        
smallest           variable       int                        local    global > main()                64    4     3     smallest.31          -                        
i                  variable       int                        local    global > main() > for          65    4     4     i.32                 -                        
upper              variable       char[8]                    local    global > main()                70    8     7     upper.33             -                        
i                  variable       int                        local    global > main() > for          71    4     6     i.34                 -                        

=== Record Layouts ===
(no records)
