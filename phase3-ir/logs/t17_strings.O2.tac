=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t17_strings.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 348 -> 283 instruction(s) for 'test/t17_strings.c'.

optimization summary (-O2)
    instructions                348 -> 283   (18% fewer)
    constants folded            3
    algebraic simplifications   3
    common subexpressions       10
    copies / constants forwarded 16
    temporaries merged away     23
    dead instructions removed   13
    jumps removed or redirected 26
    unreachable instructions    2
    propagated across blocks    1
    dead assignments removed    2

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
 140:     t6 = s ptr+ j
 141:     t7 = *t6
 142:     *t3 = t7
 143:     *t6 = t4
 144:     i = i int+ 1
 145:     j = j int- 1
 146:     goto L6
 147: L7: return

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
 148:      i = 0
 149: L8:  t1 = text ptr+ i
 150:      t2 = *t1
 151:      if t2 char== 0 goto L10
 152:      t3 = text ptr+ i
 153:      t4 = *t3
 154:      t5 = chartoint t4
 155:      t6 = chartoint c
 156:      if t5 int!= t6 goto L9
 157:      return i
 158: L9:  i = i int+ 1
 159:      goto L8
 160: L10: return -1

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
 161:      sign = 1
 162:      v = 0
 163:      t1 = *s
 164:      t2 = chartoint t1
 165:      if t2 int!= 45 goto L11
 166:      sign = -1
 167:      s = s ptr+ 1
 168: L11: t5 = *s
 169:      t6 = chartoint t5
 170:      if t6 int< 48 goto L12
 171:      t7 = *s
 172:      t8 = chartoint t7
 173:      if t8 int> 57 goto L12
 174:      t9 = v int* 10
 175:      t10 = *s
 176:      t11 = chartoint t10
 177:      t12 = t11 int- 48
 178:      v = t9 int+ t12
 179:      s = s ptr+ 1
 180:      goto L11
 181: L12: t15 = sign int* v
 182:      return t15

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
 183:      n = 0
 184:      if v int< 0 goto L13
 185:      t1 = 0
 186:      goto L14
 187: L13: t1 = 1
 188: L14: if t1 int== 0 goto L15
 189:      v = int- v
 190: L15: t3 = n
 191:      n = n int+ 1
 192:      t5 = v int% 10
 193:      t6 = 48 int+ t5
 194:      t7 = inttochar t6
 195:      tmp[t3] = t7
 196:      t8 = v int/ 10
 197:      v = t8
 198:      if t8 int> 0 goto L15
 199:      if t1 int== 0 goto L16
 200:      t9 = n
 201:      n = n int+ 1
 202:      tmp[t9] = 45
 203: L16: if n int<= 0 goto L17
 204:      t11 = out
 205:      out = out ptr+ 1
 206:      t13 = n int- 1
 207:      n = t13
 208:      t14 = tmp[t13]
 209:      *t11 = t14
 210:      goto L16
 211: L17: *out = 0
 212:      return

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
 213:      i = 0
 214:      param s
 215:      t1 = call length(const char *), 1
 216:      j = t1 int- 1
 217: L18: if i int>= j goto L19
 218:      t3 = i
 219:      i = i int+ 1
 220:      t5 = s ptr+ t3
 221:      t6 = *t5
 222:      t7 = chartoint t6
 223:      t8 = j
 224:      j = j int- 1
 225:      t10 = s ptr+ t8
 226:      t11 = *t10
 227:      t12 = chartoint t11
 228:      if t7 int== t12 goto L18
 229:      return 0
 230: L19: return 1

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
 231:      words = 0
 232:      inside = 0
 233: L20: t1 = *s
 234:      if t1 char== 0 goto L24
 235:      t2 = *s
 236:      t3 = chartoint t2
 237:      if t3 int== 32 goto L21
 238:      t4 = *s
 239:      t5 = chartoint t4
 240:      if t5 int!= 9 goto L22
 241: L21: inside = 0
 242:      goto L23
 243: L22: if inside int!= 0 goto L23
 244:      inside = 1
 245:      words = words int+ 1
 246: L23: s = s ptr+ 1
 247:      goto L20
 248: L24: return words

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
 249:      names[0] = "delta"
 250:      names[4] = "alpha"
 251:      names[8] = "charlie"
 252:      t1 = &buf
 253:      param t1
 254:      param "compiler"
 255:      call copy(char *, const char *), 2
 256:      param t1
 257:      t4 = call length(const char *), 1
 258:      param "%s %d\n"
 259:      param t1
 260:      param t4
 261:      call printf, 3
 262:      param t1
 263:      call reverse(char *), 1
 264:      param t1
 265:      param 112
 266:      t8 = call find(const char *, char), 2
 267:      param t1
 268:      param 122
 269:      t10 = call find(const char *, char), 2
 270:      param "%s %d %d\n"
 271:      param t1
 272:      param t8
 273:      param t10
 274:      call printf, 4
 275:      param "abc"
 276:      param "abd"
 277:      t12 = call compare(const char *, const char *), 2
 278:      if t12 int< 0 goto L25
 279:      t11 = 0
 280:      goto L26
 281: L25: t11 = 1
 282: L26: param "abc"
 283:      param "abc"
 284:      t13 = call compare(const char *, const char *), 2
 285:      param "b"
 286:      param "abc"
 287:      t15 = call compare(const char *, const char *), 2
 288:      if t15 int> 0 goto L27
 289:      t14 = 0
 290:      goto L28
 291: L27: t14 = 1
 292: L28: param "%d %d %d\n"
 293:      param t11
 294:      param t13
 295:      param t14
 296:      call printf, 4
 297:      smallest = 0
 298:      i.32 = 1
 299: L29: if i.32 int>= 3 goto L31
 300:      t16 = i.32 int<< 2                  (w = 4)
 301:      t17 = names[t16]
 302:      t18 = smallest int<< 2              (w = 4)
 303:      t19 = names[t18]
 304:      param t17
 305:      param t19
 306:      t20 = call compare(const char *, const char *), 2
 307:      if t20 int>= 0 goto L30
 308:      smallest = i.32
 309: L30: i.32 = i.32 int+ 1
 310:      goto L29
 311: L31: t22 = smallest int<< 2              (w = 4)
 312:      t23 = names[t22]
 313:      t24 = names[8]
 314:      t25 = t24 ptr+ 3
 315:      t26 = *t25
 316:      t27 = chartoint t26
 317:      param "%s %c\n"
 318:      param t23
 319:      param t27
 320:      call printf, 3
 321:      t29 = &num
 322:      param -40213
 323:      param t29
 324:      call toText(int, char *), 2
 325:      param t29
 326:      t32 = call toNumber(const char *), 1
 327:      t33 = t32 int+ 1
 328:      param "77x"
 329:      t34 = call toNumber(const char *), 1
 330:      param "%s %d %d\n"
 331:      param t29
 332:      param t33
 333:      param t34
 334:      call printf, 4
 335:      param "level"
 336:      t35 = call isPalindrome(const char *), 1
 337:      param "lever"
 338:      t36 = call isPalindrome(const char *), 1
 339:      param "  the quick  brown fox "
 340:      t37 = call countWords(const char *), 1
 341:      param "%d %d %d\n"
 342:      param t35
 343:      param t36
 344:      param t37
 345:      call printf, 4
 346:      upper[0] = 109
 347:      upper[1] = 105
 348:      upper[2] = 120
 349:      upper[3] = 101
 350:      upper[4] = 100
 351:      upper[5] = 0
 352:      upper[6] = 0
 353:      upper[7] = 0
 354:      i.34 = 0
 355: L32: t38 = upper[i.34]
 356:      if t38 char== 0 goto L34
 357:      t39 = upper[i.34]
 358:      t40 = chartoint t39
 359:      if t40 int< 97 goto L33
 360:      t41 = upper[i.34]
 361:      t42 = chartoint t41
 362:      if t42 int> 122 goto L33
 363:      t43 = upper[i.34]
 364:      t44 = chartoint t43
 365:      t45 = t44 int- 97
 366:      t46 = t45 int+ 65
 367:      t47 = inttochar t46
 368:      upper[i.34] = t47
 369: L33: i.34 = i.34 int+ 1
 370:      goto L32
 371: L34: t49 = &upper
 372:      param "%s %d\n"
 373:      param t49
 374:      param 8
 375:      call printf, 3
 376:      t50 = names[4]
 377:      param t50
 378:      t51 = call length(const char *), 1
 379:      t52 = buf[0]
 380:      t53 = chartoint t52
 381:      t54 = t51 int+ t53
 382:      return t54


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
