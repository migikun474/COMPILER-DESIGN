=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t21_numeric.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 213 -> 146 instruction(s) for 'test/t21_numeric.c'.

optimization summary (-O2)
    instructions                213 -> 146   (31% fewer)
    constants folded            25
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 42
    temporaries merged away     15
    dead instructions removed   25
    jumps removed or redirected 8
    unreachable instructions    7
    propagated across blocks    0
    dead assignments removed    11

function absolute(double)        link name: _Z8absoluted
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    total width 24
  code
 100:     if v double< 0.0 goto L1
 101:     goto L2
 102: L1: t1 = double- v
 103:     goto L3
 104: L2: t1 = v
 105: L3: return t1

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
 106:     guess = v double/ 2.0
 107:     i = 0
 108: L4: if i int>= 20 goto L5
 109:     t2 = v double/ guess
 110:     t3 = guess double+ t2
 111:     guess = t3 double/ 2.0
 112:     i = i int+ 1
 113:     goto L4
 114: L5: return guess

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
 115:     sum = 0.0
 116:     sign = 1.0
 117:     i = 0
 118: L6: if i int>= terms goto L7
 119:     t1 = i int<< 1
 120:     t2 = t1 int+ 1
 121:     t3 = inttodouble t2
 122:     t4 = sign double/ t3
 123:     sum = sum double+ t4
 124:     sign = double- sign
 125:     i = i int+ 1
 126:     goto L6
 127: L7: t8 = 4.0 double* sum
 128:     return t8

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
 129:     r = 1.0
 130: L8: t1 = n
 131:     n = n int- 1
 132:     if t1 int<= 0 goto L9
 133:     r = r double* base
 134:     goto L8
 135: L9: return r

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
 136:   t1 = a float+ b
 137:   t2 = t1 float+ c
 138:   t3 = t2 float/ 3.0
 139:   return t3

function roundToInt(double)        link name: _Z10roundToIntd
  symbol table (name, kind, type, width, offset)
    v              param  double                     8      0
    t1             temp   double                     8      8
    t2             temp   double                     8     16
    t3             temp   double                     8     24
    t4             temp   int                        4     32
    total width 36
  code
 140:      if v double< 0.0 goto L10
 141:      goto L11
 142: L10: t1 = v double- 0.5
 143:      goto L12
 144: L11: t1 = v double+ 0.5
 145: L12: t4 = doubletoint t1
 146:      return t4

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
 147:   t1 = 2.0 double* x
 148:   t2 = t1 double- 3.0
 149:   t3 = t2 double* x
 150:   t4 = t3 double+ 0.5
 151:   t5 = t4 double* x
 152:   t6 = t5 double- 7.0
 153:   return t6

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
 154:      param "%.3f %.3f %.3f %.4f\n"
 155:      param 2.5
 156:      param 3.0
 157:      param 3.5
 158:      param 0.3333333432674408
 159:      call printf, 5
 160:      param 2.0
 161:      t7 = call root(double), 1
 162:      param 1000
 163:      t8 = call series(int), 1
 164:      param 1.5
 165:      param 6
 166:      t9 = call power(double, int), 2
 167:      param "%.5f %.4f %.2f\n"
 168:      param t7
 169:      param t8
 170:      param t9
 171:      call printf, 4
 172:      param 1.5
 173:      param 2.5
 174:      param 4.0
 175:      t10 = call average(float, float, float), 3
 176:      t11 = floattodouble t10
 177:      param -3.25
 178:      t13 = call absolute(double), 1
 179:      param 2.0
 180:      t14 = call poly(double), 1
 181:      param "%.3f %.2f %.2f\n"
 182:      param t11
 183:      param t13
 184:      param t14
 185:      call printf, 4
 186:      param 2.5
 187:      t15 = call roundToInt(double), 1
 188:      param -2.5
 189:      t17 = call roundToInt(double), 1
 190:      param 2.4
 191:      t18 = call roundToInt(double), 1
 192:      param "%d %d %d %d\n"
 193:      param t15
 194:      param t17
 195:      param t18
 196:      param 9
 197:      call printf, 5
 198:      param "%d %d %d %d\n"
 199:      param 0
 200:      param 1
 201:      param 0
 202:      param 1
 203:      call printf, 5
 204:      param "%.1f %.1f %d\n"
 205:      param 4000000071.5
 206:      param 16777216.0
 207:      param 0
 208:      call printf, 4
 209:      total = 0.0
 210:      step = 0.25
 211: L13: if step double< 2.0 goto L14
 212:      goto L15
 213: L14: t35 = step double* step
 214:      total = total double+ t35
 215:      step = step double+ 0.25
 216:      goto L13
 217: L15: param "%.4f\n"
 218:      param total
 219:      call printf, 2
 220:      fsum = 0.0
 221:      k = 1
 222: L16: if k int> 10 goto L17
 223:      t38 = inttofloat k
 224:      t39 = 1.0 float/ t38
 225:      fsum = fsum float+ t39
 226:      k = k int+ 1
 227:      goto L16
 228: L17: t42 = floattodouble fsum
 229:      t43 = float- fsum
 230:      t44 = t43 float* 2.0
 231:      t45 = floattodouble t44
 232:      param "%.4f %.2f\n"
 233:      param t42
 234:      param t45
 235:      call printf, 3
 236:      param "%.6f %.1f %.3f\n"
 237:      param 0.001
 238:      param 2.5e+06
 239:      param 2.5e+03
 240:      call printf, 4
 241:      param 81.0
 242:      t47 = call root(double), 1
 243:      param t47
 244:      t48 = call roundToInt(double), 1
 245:      return t48


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
