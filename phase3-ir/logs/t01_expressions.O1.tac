=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t01_expressions.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 199 -> 112 instruction(s) for 'test/t01_expressions.c'.

optimization summary (-O1)
    instructions                199 -> 112   (43% fewer)
    constants folded            77
    algebraic simplifications   0
    common subexpressions       0
    copies / constants forwarded 172
    temporaries merged away     0
    dead instructions removed   79
    jumps removed or redirected 4
    unreachable instructions    4

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
 100:   a = 7
 101:   b = 3
 102:   c = 12
 103:   param "%d %d %d %d %d\n"
 104:   param 12
 105:   param 4
 106:   param 21
 107:   param 2
 108:   param 1
 109:   call printf, 6
 110:   c = -42
 111:   param "%d\n"
 112:   param -42
 113:   call printf, 2
 114:   d = 1.5
 115:   f = 2.5
 116:   d = 15.5
 117:   f = 7.5
 118:   truncated = 7
 119:   param "%.2f %.2f %d\n"
 120:   param 15.5
 121:   param 7.5
 122:   param 7
 123:   call printf, 4
 124:   u = 7
 125:   u = 33
 126:   neg = -16
 127:   param "%u %d %d %d\n"
 128:   param 33
 129:   param -4
 130:   param -5
 131:   param -1
 132:   call printf, 5
 133:   param "%d %d %d %d\n"
 134:   param 3
 135:   param 7
 136:   param 4
 137:   param -8
 138:   call printf, 5
 139:   ch = 65
 140:   ch = 67
 141:   s = 300
 142:   s = 600
 143:   big = 100000
 144:   big = 10000000007
 145:   param "%c %d %d %lld\n"
 146:   param 67
 147:   param 67
 148:   param 600
 149:   param 10000000007
 150:   call printf, 5
 151:   a = 12
 152:   b = 2
 153:   c = -84
 154:   a = 4
 155:   b = 16
 156:   c = 0
 157:   a = 12
 158:   b = 0
 159:   c = 5
 160:   d = 15.0
 161:   d = 3e+01
 162:   param "%d %d %d %.1f\n"
 163:   param 12
 164:   param 0
 165:   param 5
 166:   param 3e+01
 167:   call printf, 5
 168:   i = 5
 169:   i = 6
 170:   j = 6
 171:   param "%d %d\n"
 172:   param 6
 173:   param 6
 174:   call printf, 3
 175:   i = 7
 176:   j = 14
 177:   param "%d %d\n"
 178:   param 7
 179:   param 14
 180:   call printf, 3
 181:   i = 6
 182:   i = 5
 183:   j = 2
 184:   j = 3
 185:   i = 7
 186:   param "%d %d\n"
 187:   param 7
 188:   param 3
 189:   call printf, 3
 190:   big2 = 12
 191:   mixed = 2.5
 192:   param "%d %.1f\n"
 193:   param 12
 194:   param 2.5
 195:   call printf, 3
 196:   param "%d %d %d\n"
 197:   param 4
 198:   param 8
 199:   param 1
 200:   call printf, 4
 201:   param "%d %.3f %d\n"
 202:   param 3
 203:   param 3.0
 204:   param 65
 205:   call printf, 4
 206:   wraps = 250
 207:   wraps = 4
 208:   param "%d\n"
 209:   param 4
 210:   call printf, 2
 211:   return 12


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
