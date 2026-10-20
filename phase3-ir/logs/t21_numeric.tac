=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t21_numeric.c
Optimization : no optimization

Three address code generated: 8 function(s), 213 instruction(s) for 'test/t21_numeric.c'.

function absolute(double)        link name: _Z8absoluted
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    total width 24
  code
 100:     if v double< 0.0 goto L1
 101:     goto L2
 102: L1: t2 = double- v
 103:     t1 = t2
 104:     goto L3
 105: L2: t1 = v
 106: L3: return t1

function root(double)        link name: _Z4rootd
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    guess          local  double                     8      8
    i              local  int                        4     16
    t1             temp   double                     8     24
    t2             temp   double                     8     32
    t3             temp   double                     8     40
    t4             temp   double                     8     48
    t5             temp   int                        4     56
    total width 60
  code
 107:     t1 = v double/ 2.0
 108:     guess = t1
 109:     i = 0
 110: L4: if i int< 20 goto L5
 111:     goto L6
 112: L5: t2 = v double/ guess
 113:     t3 = guess double+ t2
 114:     t4 = t3 double/ 2.0
 115:     guess = t4
 116:     t5 = i int+ 1
 117:     i = t5
 118:     goto L4
 119: L6: return guess

function series(int)        link name: _Z6seriesi
  symbol table (name, kind, type, width, offset)
    terms          param  int                        4      0
    sum            local  double                     8      8
    sign           local  double                     8     16
    i              local  int                        4     24
    t1             temp   int                        4     28
    t2             temp   int                        4     32
    t3             temp   double                     8     40
    t4             temp   double                     8     48
    t5             temp   double                     8     56
    t6             temp   double                     8     64
    t7             temp   int                        4     72
    t8             temp   double                     8     80
    total width 88
  code
 120:     sum = 0.0
 121:     sign = 1.0
 122:     i = 0
 123: L7: if i int< terms goto L8
 124:     goto L9
 125: L8: t1 = 2 int* i
 126:     t2 = t1 int+ 1
 127:     t3 = inttodouble t2
 128:     t4 = sign double/ t3
 129:     t5 = sum double+ t4
 130:     sum = t5
 131:     t6 = double- sign
 132:     sign = t6
 133:     t7 = i int+ 1
 134:     i = t7
 135:     goto L7
 136: L9: t8 = 4.0 double* sum
 137:     return t8

function power(double, int)        link name: _Z5powerdi
  symbol table (name, kind, type, width, offset)
    base           param  double                     8      0
    n              param  int                        4      8
    r              local  double                     8     16
    t1             temp   int                        4     24
    t2             temp   int                        4     28
    t3             temp   double                     8     32
    total width 40
  code
 138:      r = 1.0
 139: L10: t1 = n
 140:      t2 = n int- 1
 141:      n = t2
 142:      if t1 int> 0 goto L11
 143:      goto L12
 144: L11: t3 = r double* base
 145:      r = t3
 146:      goto L10
 147: L12: return r

function average(float, float, float)        link name: _Z7averagefff
  symbol table (name, kind, type, width, offset)
    a              param  float                      4      0
    b              param  float                      4      4
    c              param  float                      4      8
    t1             temp   float                      4     12
    t2             temp   float                      4     16
    t3             temp   float                      4     20
    total width 24
  code
 148:   t1 = a float+ b
 149:   t2 = t1 float+ c
 150:   t3 = t2 float/ 3.0
 151:   return t3

function roundToInt(double)        link name: _Z10roundToIntd
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    t3             temp   double                     8     24
    t4             temp   int                        4     32
    total width 36
  code
 152:      if v double< 0.0 goto L13
 153:      goto L14
 154: L13: t2 = v double- 0.5
 155:      t1 = t2
 156:      goto L15
 157: L14: t3 = v double+ 0.5
 158:      t1 = t3
 159: L15: t4 = doubletoint t1
 160:      return t4

function poly(double)        link name: _Z4polyd
  symbol table (name, kind, type, width, offset)
    x              param  double                     8      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    t3             temp   double                     8     24
    t4             temp   double                     8     32
    t5             temp   double                     8     40
    t6             temp   double                     8     48
    total width 56
  code
 161:   t1 = 2.0 double* x
 162:   t2 = t1 double- 3.0
 163:   t3 = t2 double* x
 164:   t4 = t3 double+ 0.5
 165:   t5 = t4 double* x
 166:   t6 = t5 double- 7.0
 167:   return t6

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    d              local  double                     8      0
    e              local  double                     8      8
    f              local  double                     8     16
    g              local  float                      4     24
    i              local  int                        4     28
    u              local  unsigned int               4     32
    c              local  char                       1     36
    mixed          local  double                     8     40
    narrowed       local  float                      4     48
    total          local  double                     8     56
    step           local  double                     8     64
    fsum           local  float                      4     72
    k              local  int                        4     76
    tiny           local  double                     8     80
    huge           local  double                     8     88
    t1             temp   double                     8     96
    t2             temp   int                        4    104
    t3             temp   double                     8    112
    t4             temp   double                     8    120
    t5             temp   float                      4    128
    t6             temp   double                     8    136
    t7             temp   double                     8    144
    t8             temp   double                     8    152
    t9             temp   double                     8    160
    t10            temp   float                      4    168
    t11            temp   double                     8    176
    t12            temp   double                     8    184
    t13            temp   double                     8    192
    t14            temp   double                     8    200
    t15            temp   int                        4    208
    t16            temp   double                     8    216
    t17            temp   int                        4    224
    t18            temp   int                        4    228
    t19            temp   int                        4    232
    t20            temp   double                     8    240
    t21            temp   int                        4    248
    t22            temp   double                     8    256
    t23            temp   int                        4    264
    t24            temp   int                        4    268
    t25            temp   int                        4    272
    t26            temp   double                     8    280
    t27            temp   double                     8    288
    t28            temp   double                     8    296
    t29            temp   double                     8    304
    t30            temp   double                     8    312
    t31            temp   double                     8    320
    t32            temp   double                     8    328
    t33            temp   double                     8    336
    t34            temp   double                     8    344
    t35            temp   double                     8    352
    t36            temp   double                     8    360
    t37            temp   double                     8    368
    t38            temp   float                      4    376
    t39            temp   float                      4    380
    t40            temp   float                      4    384
    t41            temp   int                        4    388
    t42            temp   double                     8    392
    t43            temp   float                      4    400
    t44            temp   float                      4    404
    t45            temp   double                     8    408
    t46            temp   double                     8    416
    t47            temp   double                     8    424
    t48            temp   int                        4    432
    total width 436
  code
 168:      t1 = 1e+01 double/ 4.0
 169:      d = t1
 170:      t2 = 7 int/ 2
 171:      t3 = inttodouble t2
 172:      e = t3
 173:      t4 = 7.0 double/ 2.0
 174:      f = t4
 175:      t5 = 1.0 float/ 3.0
 176:      g = t5
 177:      t6 = floattodouble g
 178:      param "%.3f %.3f %.3f %.4f\n"
 179:      param d
 180:      param e
 181:      param f
 182:      param t6
 183:      call printf, 5
 184:      param 2.0
 185:      t7 = call root(double), 1
 186:      param 1000
 187:      t8 = call series(int), 1
 188:      param 1.5
 189:      param 6
 190:      t9 = call power(double, int), 2
 191:      param "%.5f %.4f %.2f\n"
 192:      param t7
 193:      param t8
 194:      param t9
 195:      call printf, 4
 196:      param 1.5
 197:      param 2.5
 198:      param 4.0
 199:      t10 = call average(float, float, float), 3
 200:      t11 = floattodouble t10
 201:      t12 = double- 3.25
 202:      param t12
 203:      t13 = call absolute(double), 1
 204:      param 2.0
 205:      t14 = call poly(double), 1
 206:      param "%.3f %.2f %.2f\n"
 207:      param t11
 208:      param t13
 209:      param t14
 210:      call printf, 4
 211:      param 2.5
 212:      t15 = call roundToInt(double), 1
 213:      t16 = double- 2.5
 214:      param t16
 215:      t17 = call roundToInt(double), 1
 216:      param 2.4
 217:      t18 = call roundToInt(double), 1
 218:      param "%d %d %d %d\n"
 219:      param t15
 220:      param t17
 221:      param t18
 222:      param 9
 223:      call printf, 5
 224:      t20 = 0.1 double+ 0.2
 225:      if t20 double== 0.3 goto L16
 226:      t19 = 0
 227:      goto L17
 228: L16: t19 = 1
 229: L17: t22 = 0.5 double+ 0.25
 230:      if t22 double== 0.75 goto L18
 231:      t21 = 0
 232:      goto L19
 233: L18: t21 = 1
 234: L19: if d double> e goto L20
 235:      t23 = 0
 236:      goto L21
 237: L20: t23 = 1
 238: L21: if g float< 0.3400000035762787 goto L22
 239:      t24 = 0
 240:      goto L23
 241: L22: t24 = 1
 242: L23: param "%d %d %d %d\n"
 243:      param t19
 244:      param t21
 245:      param t23
 246:      param t24
 247:      call printf, 5
 248:      i = 7
 249:      u = 4000000000
 250:      c = 65
 251:      t25 = i int/ 2
 252:      t26 = inttodouble t25
 253:      t27 = inttodouble i
 254:      t28 = t27 double/ 2.0
 255:      t29 = t26 double+ t28
 256:      t30 = chartodouble c
 257:      t31 = t29 double+ t30
 258:      t32 = uinttodouble u
 259:      t33 = t31 double+ t32
 260:      mixed = t33
 261:      narrowed = 16777216.0
 262:      t34 = floattodouble narrowed
 263:      param "%.1f %.1f %d\n"
 264:      param mixed
 265:      param t34
 266:      param 0
 267:      call printf, 4
 268:      total = 0.0
 269:      step = 0.25
 270: L24: if step double< 2.0 goto L25
 271:      goto L26
 272: L25: t35 = step double* step
 273:      t36 = total double+ t35
 274:      total = t36
 275:      t37 = step double+ 0.25
 276:      step = t37
 277:      goto L24
 278: L26: param "%.4f\n"
 279:      param total
 280:      call printf, 2
 281:      fsum = 0.0
 282:      k = 1
 283: L27: if k int<= 10 goto L28
 284:      goto L29
 285: L28: t38 = inttofloat k
 286:      t39 = 1.0 float/ t38
 287:      t40 = fsum float+ t39
 288:      fsum = t40
 289:      t41 = k int+ 1
 290:      k = t41
 291:      goto L27
 292: L29: t42 = floattodouble fsum
 293:      t43 = float- fsum
 294:      t44 = t43 float* 2.0
 295:      t45 = floattodouble t44
 296:      param "%.4f %.2f\n"
 297:      param t42
 298:      param t45
 299:      call printf, 3
 300:      tiny = 0.001
 301:      huge = 2.5e+06
 302:      t46 = huge double* tiny
 303:      param "%.6f %.1f %.3f\n"
 304:      param tiny
 305:      param huge
 306:      param t46
 307:      call printf, 4
 308:      param 81.0
 309:      t47 = call root(double), 1
 310:      param t47
 311:      t48 = call roundToInt(double), 1
 312:      return t48


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
absolute           function       double (double)            -        global                         5     -     1     _Z8absoluted         _Z8absoluted             defined
v                  parameter      double                     param    global > absolute()            5     8     3     v.1                  -                        
root               function       double (double)            -        global                         7     -     2     _Z4rootd             _Z4rootd                 defined
v                  parameter      double                     param    global > root()                7     8     2     v.2                  -                        
guess              variable       double                     local    global > root()                8     8     4     guess.3              -                        
i                  variable       int                        local    global > root() > for          9     4     2     i.4                  -                        
series             function       double (int)               -        global                         13    -     1     _Z6seriesi           _Z6seriesi               defined
terms              parameter      int                        param    global > series()              13    4     1     terms.5              -                        
sum                variable       double                     local    global > series()              14    8     2     sum.6                -                        
sign               variable       double                     local    global > series()              14    8     3     sign.7               -                        
i                  variable       int                        local    global > series() > for        15    4     3     i.8                  -                        
power              function       double (double, int)       -        global                         19    -     1     _Z5powerdi           _Z5powerdi               defined
base               parameter      double                     param    global > power()               19    8     1     base.9               -                        
n                  parameter      int                        param    global > power()               19    4     1     n.10                 -                        
r                  variable       double                     local    global > power()               19    8     2     r.11                 -                        
average            function       float (float, float, float) -        global                         20    -     1     _Z7averagefff        _Z7averagefff            defined
a                  parameter      float                      param    global > average()             20    4     1     a.12                 -                        
b                  parameter      float                      param    global > average()             20    4     1     b.13                 -                        
c                  parameter      float                      param    global > average()             20    4     1     c.14                 -                        
roundToInt         function       int (double)               -        global                         21    -     4     _Z10roundToIntd      _Z10roundToIntd          defined
v                  parameter      double                     param    global > roundToInt()          21    8     3     v.15                 -                        
poly               function       double (double)            -        global                         23    -     1     _Z4polyd             _Z4polyd                 defined
x                  parameter      double                     param    global > poly()                23    8     3     x.16                 -                        
main               function       int (void)                 -        global                         25    -     0     main                 main                     defined
d                  variable       double                     local    global > main()                26    8     2     d.17                 -                        
e                  variable       double                     local    global > main()                26    8     2     e.18                 -                        
f                  variable       double                     local    global > main()                26    8     1     f.19                 -                        
g                  variable       float                      local    global > main()                27    4     2     g.20                 -                        
i                  variable       int                        local    global > main()                34    4     2     i.21                 -                        
u                  variable       unsigned int               local    global > main()                35    4     1     u.22                 -                        
c                  variable       char                       local    global > main()                36    1     1     c.23                 -                        
mixed              variable       double                     local    global > main()                37    8     1     mixed.24             -                        
narrowed           variable       float                      local    global > main()                38    4     1     narrowed.25          -                        
total              variable       double                     local    global > main()                41    8     2     total.26             -                        
step               variable       double                     local    global > main() > for          42    8     4     step.27              -                        
fsum               variable       float                      local    global > main()                44    4     3     fsum.28              -                        
k                  variable       int                        local    global > main() > for          45    4     3     k.29                 -                        
tiny               variable       double                     local    global > main()                47    8     2     tiny.30              -                        
huge               variable       double                     local    global > main()                47    8     2     huge.31              -                        

=== Record Layouts ===
(no records)
