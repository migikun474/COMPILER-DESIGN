=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t20_bits.c
Optimization : no optimization

Three address code generated: 7 function(s), 237 instruction(s) for 'test/t20_bits.c'.

function popcount(unsigned int)        link name: _Z8popcountj
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    n              local  int                        4      4
    t1             temp   unsigned int               4      8
    t2             temp   unsigned int               4     12
    t3             temp   unsigned int               4     16
    total width 20
  code
 100:     n = 0
 101: L1: if v uint!= 0 goto L2
 102:     goto L3
 103: L2: t1 = v uint& 1
 104:     t2 = n uint+ t1
 105:     n = t2
 106:     t3 = v uint>> 1
 107:     v = t3
 108:     goto L1
 109: L3: return n

function reverseBits(unsigned int)        link name: _Z11reverseBitsj
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    r              local  unsigned int               4      4
    i              local  int                        4      8
    t1             temp   unsigned int               4     12
    t2             temp   unsigned int               4     16
    t3             temp   unsigned int               4     20
    t4             temp   unsigned int               4     24
    t5             temp   int                        4     28
    total width 32
  code
 110:     r = 0
 111:     i = 0
 112: L4: if i int< 32 goto L5
 113:     goto L6
 114: L5: t1 = r uint<< 1
 115:     t2 = v uint& 1
 116:     t3 = t1 uint| t2
 117:     r = t3
 118:     t4 = v uint>> 1
 119:     v = t4
 120:     t5 = i int+ 1
 121:     i = t5
 122:     goto L4
 123: L6: return r

function isPowerOfTwo(unsigned int)        link name: _Z12isPowerOfTwoj
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    t1             temp   int                        4      4
    t2             temp   unsigned int               4      8
    t3             temp   unsigned int               4     12
    total width 16
  code
 124:      if v uint!= 0 goto L7
 125:      goto L8
 126: L7:  t2 = v uint- 1
 127:      t3 = v uint& t2
 128:      if t3 uint== 0 goto L9
 129:      goto L8
 130: L8:  t1 = 0
 131:      goto L10
 132: L9:  t1 = 1
 133: L10: return t1

function highestBit(unsigned int)        link name: _Z10highestBitj
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    n              local  int                        4      4
    t1             temp   int                        4      8
    t2             temp   unsigned int               4     12
    t3             temp   int                        4     16
    total width 20
  code
 134:      t1 = int- 1
 135:      n = t1
 136: L11: if v uint!= 0 goto L12
 137:      goto L13
 138: L12: t2 = v uint>> 1
 139:      v = t2
 140:      t3 = n int+ 1
 141:      n = t3
 142:      goto L11
 143: L13: return n

function rotl(unsigned int, int)        link name: _Z4rotlji
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    k              param  int                        4      4
    t1             temp   unsigned int               4      8
    t2             temp   int                        4     12
    t3             temp   unsigned int               4     16
    t4             temp   unsigned int               4     20
    total width 24
  code
 144:   t1 = v uint<< k
 145:   t2 = 32 int- k
 146:   t3 = v uint>> t2
 147:   t4 = t1 uint| t3
 148:   return t4

function sign(int)        link name: _Z4signi
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    total width 16
  code
 149:      if v int> 0 goto L14
 150:      t1 = 0
 151:      goto L15
 152: L14: t1 = 1
 153: L15: if v int< 0 goto L16
 154:      t2 = 0
 155:      goto L17
 156: L16: t2 = 1
 157: L17: t3 = t1 int- t2
 158:      return t3

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    u              local  unsigned int               4      0
    big            local  int                        4      4
    small          local  int                        4      8
    wrap           local  unsigned int               4     12
    uc             local  unsigned char              1     16
    sc             local  char                       1     17
    sh             local  short                      2     18
    us             local  unsigned short             2     20
    flags          local  int                        4     24
    c              local  char                       1     28
    t1             temp   int                        4     32
    t2             temp   unsigned int               4     36
    t3             temp   int                        4     40
    t4             temp   int                        4     44
    t5             temp   int                        4     48
    t6             temp   unsigned int               4     52
    t7             temp   unsigned int               4     56
    t8             temp   unsigned int               4     60
    t9             temp   unsigned int               4     64
    t10            temp   unsigned int               4     68
    t11            temp   unsigned int               4     72
    t12            temp   unsigned int               4     76
    t13            temp   int                        4     80
    t14            temp   int                        4     84
    t15            temp   unsigned int               4     88
    t16            temp   int                        4     92
    t17            temp   int                        4     96
    t18            temp   int                        4    100
    t19            temp   unsigned int               4    104
    t20            temp   int                        4    108
    t21            temp   int                        4    112
    t22            temp   short                      2    116
    t23            temp   int                        4    120
    t24            temp   int                        4    124
    t25            temp   unsigned char              1    128
    t26            temp   int                        4    132
    t27            temp   int                        4    136
    t28            temp   char                       1    140
    t29            temp   int                        4    144
    t30            temp   int                        4    148
    t31            temp   short                      2    152
    t32            temp   int                        4    156
    t33            temp   int                        4    160
    t34            temp   unsigned short             2    164
    t35            temp   int                        4    168
    t36            temp   int                        4    172
    t37            temp   int                        4    176
    t38            temp   int                        4    180
    t39            temp   int                        4    184
    t40            temp   int                        4    188
    t41            temp   int                        4    192
    t42            temp   int                        4    196
    t43            temp   int                        4    200
    t44            temp   int                        4    204
    t45            temp   int                        4    208
    t46            temp   int                        4    212
    t47            temp   int                        4    216
    t48            temp   int                        4    220
    t49            temp   int                        4    224
    t50            temp   int                        4    228
    t51            temp   int                        4    232
    t52            temp   int                        4    236
    t53            temp   int                        4    240
    t54            temp   int                        4    244
    t55            temp   int                        4    248
    t56            temp   int                        4    252
    t57            temp   int                        4    256
    t58            temp   int                        4    260
    t59            temp   int                        4    264
    t60            temp   int                        4    268
    t61            temp   int                        4    272
    t62            temp   int                        4    276
    t63            temp   int                        4    280
    t64            temp   int                        4    284
    t65            temp   int                        4    288
    t66            temp   int                        4    292
    t67            temp   int                        4    296
    t68            temp   char                       1    300
    t69            temp   int                        4    304
    t70            temp   int                        4    308
    t71            temp   int                        4    312
    t72            temp   int                        4    316
    t73            temp   int                        4    320
    total width 324
  code
 159:      u = 4042265140
 160:      param u
 161:      t1 = call popcount(unsigned int), 1
 162:      param u
 163:      t2 = call reverseBits(unsigned int), 1
 164:      param 64
 165:      t3 = call isPowerOfTwo(unsigned int), 1
 166:      param 65
 167:      t4 = call isPowerOfTwo(unsigned int), 1
 168:      param 1000
 169:      t5 = call highestBit(unsigned int), 1
 170:      param "%d %x %d %d %d\n"
 171:      param t1
 172:      param t2
 173:      param t3
 174:      param t4
 175:      param t5
 176:      call printf, 6
 177:      t6 = u uint& 65535
 178:      t7 = u uint| 15
 179:      t8 = u uint^ 4294967295
 180:      t9 = uint~ u
 181:      param "%x %x %x %x\n"
 182:      param t6
 183:      param t7
 184:      param t8
 185:      param t9
 186:      call printf, 5
 187:      param u
 188:      param 8
 189:      t10 = call rotl(unsigned int, int), 2
 190:      t11 = u uint<< 4
 191:      t12 = u uint>> 28
 192:      param "%x %x %x\n"
 193:      param t10
 194:      param t11
 195:      param t12
 196:      call printf, 4
 197:      big = 2147483647
 198:      t13 = int- 2147483647
 199:      t14 = t13 int- 1
 200:      small = t14
 201:      wrap = 4294967295
 202:      t15 = wrap uint+ 2
 203:      wrap = t15
 204:      param "%d %d %u %u\n"
 205:      param big
 206:      param small
 207:      param wrap
 208:      param small
 209:      call printf, 5
 210:      t16 = small int>> 31
 211:      t17 = int- 1
 212:      t18 = t17 int>> 1
 213:      t19 = 2147483648 uint>> 31
 214:      t20 = 1 int<< 30
 215:      param "%d %d %d %d\n"
 216:      param t16
 217:      param t18
 218:      param t19
 219:      param t20
 220:      call printf, 5
 221:      uc = 255
 222:      sc = 127
 223:      t21 = int- 32768
 224:      t22 = inttoshort t21
 225:      sh = t22
 226:      us = 65535
 227:      t23 = uchartoint uc
 228:      t24 = t23 int+ 1
 229:      t25 = inttouchar t24
 230:      uc = t25
 231:      t26 = chartoint sc
 232:      t27 = t26 int+ 1
 233:      t28 = inttochar t27
 234:      sc = t28
 235:      t29 = shorttoint sh
 236:      t30 = t29 int- 1
 237:      t31 = inttoshort t30
 238:      sh = t31
 239:      t32 = ushorttoint us
 240:      t33 = t32 int+ 1
 241:      t34 = inttoushort t33
 242:      us = t34
 243:      t35 = uchartoint uc
 244:      t36 = chartoint sc
 245:      t37 = shorttoint sh
 246:      t38 = ushorttoint us
 247:      param "%d %d %d %d\n"
 248:      param t35
 249:      param t36
 250:      param t37
 251:      param t38
 252:      call printf, 5
 253:      t39 = int- 7
 254:      t40 = t39 int/ 2
 255:      t41 = int- 7
 256:      t42 = t41 int% 2
 257:      t43 = int- 2
 258:      t44 = 7 int/ t43
 259:      param "%d %d %d\n"
 260:      param t40
 261:      param t42
 262:      param t44
 263:      call printf, 4
 264:      t46 = int- 1
 265:      if t46 uint< 1 goto L18
 266:      t45 = 0
 267:      goto L19
 268: L18: t45 = 1
 269: L19: t48 = int- 1
 270:      if t48 int< 1 goto L20
 271:      t47 = 0
 272:      goto L21
 273: L20: t47 = 1
 274: L21: t50 = int- 1
 275:      if t50 uint> 100 goto L22
 276:      t49 = 0
 277:      goto L23
 278: L22: t49 = 1
 279: L23: param "%d %d %d\n"
 280:      param t45
 281:      param t47
 282:      param t49
 283:      call printf, 4
 284:      t51 = int- 9
 285:      param t51
 286:      t52 = call sign(int), 1
 287:      param 0
 288:      t53 = call sign(int), 1
 289:      param 4
 290:      t54 = call sign(int), 1
 291:      goto L24
 292:      t55 = 0
 293:      goto L25
 294: L24: t55 = 1
 295: L25: param "%d %d %d %d\n"
 296:      param t52
 297:      param t53
 298:      param t54
 299:      param t55
 300:      call printf, 5
 301:      flags = 0
 302:      t56 = 1 int<< 3
 303:      t57 = flags int| t56
 304:      flags = t57
 305:      t58 = 1 int<< 0
 306:      t59 = flags int| t58
 307:      flags = t59
 308:      t60 = 1 int<< 0
 309:      t61 = int~ t60
 310:      t62 = flags int& t61
 311:      flags = t62
 312:      t63 = flags int^ 24
 313:      flags = t63
 314:      t64 = flags int>> 4
 315:      t65 = t64 int& 1
 316:      param "%d %d\n"
 317:      param flags
 318:      param t65
 319:      call printf, 3
 320:      c = 65
 321:      t66 = chartoint c
 322:      t67 = t66 int| 32
 323:      t68 = inttochar t67
 324:      c = t68
 325:      t69 = chartoint c
 326:      t70 = chartoint c
 327:      t71 = t70 int^ 32
 328:      t72 = 122 int- 97
 329:      param "%c %c %d\n"
 330:      param t69
 331:      param t71
 332:      param t72
 333:      call printf, 4
 334:      param 255
 335:      t73 = call popcount(unsigned int), 1
 336:      return t73


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
popcount           function       int (unsigned int)         -        global                         4     -     2     _Z8popcountj         _Z8popcountj             defined
v                  parameter      unsigned int               param    global > popcount()            4     4     3     v.1                  -                        
n                  variable       int                        local    global > popcount()            4     4     2     n.2                  -                        
reverseBits        function       unsigned int (unsigned int) -        global                         6     -     1     _Z11reverseBitsj     _Z11reverseBitsj         defined
v                  parameter      unsigned int               param    global > reverseBits()         6     4     2     v.3                  -                        
r                  variable       unsigned int               local    global > reverseBits()         7     4     3     r.4                  -                        
i                  variable       int                        local    global > reverseBits() > for   8     4     2     i.5                  -                        
isPowerOfTwo       function       int (unsigned int)         -        global                         12    -     2     _Z12isPowerOfTwoj    _Z12isPowerOfTwoj        defined
v                  parameter      unsigned int               param    global > isPowerOfTwo()        12    4     3     v.6                  -                        
highestBit         function       int (unsigned int)         -        global                         13    -     1     _Z10highestBitj      _Z10highestBitj          defined
v                  parameter      unsigned int               param    global > highestBit()          13    4     2     v.7                  -                        
n                  variable       int                        local    global > highestBit()          13    4     2     n.8                  -                        
rotl               function       unsigned int (unsigned int, int) -        global                         14    -     1     _Z4rotlji            _Z4rotlji                defined
v                  parameter      unsigned int               param    global > rotl()                14    4     2     v.9                  -                        
k                  parameter      int                        param    global > rotl()                14    4     2     k.10                 -                        
sign               function       int (int)                  -        global                         15    -     3     _Z4signi             _Z4signi                 defined
v                  parameter      int                        param    global > sign()                15    4     2     v.11                 -                        
main               function       int (void)                 -        global                         17    -     0     main                 main                     defined
u                  variable       unsigned int               local    global > main()                18    4     9     u.12                 -                        
big                variable       int                        local    global > main()                23    4     1     big.13               -                        
small              variable       int                        local    global > main()                23    4     3     small.14             -                        
wrap               variable       unsigned int               local    global > main()                24    4     3     wrap.15              -                        
uc                 variable       unsigned char              local    global > main()                29    1     2     uc.16                -                        
sc                 variable       char                       local    global > main()                30    1     2     sc.17                -                        
sh                 variable       short                      local    global > main()                31    2     2     sh.18                -                        
us                 variable       unsigned short             local    global > main()                32    2     2     us.19                -                        
flags              variable       int                        local    global > main()                39    4     6     flags.20             -                        
c                  variable       char                       local    global > main()                45    1     3     c.21                 -                        

=== Record Layouts ===
(no records)
