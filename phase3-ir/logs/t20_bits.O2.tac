=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t20_bits.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 237 -> 130 instruction(s) for 'test/t20_bits.c'.

optimization summary (-O2)
    instructions                237 -> 130   (45% fewer)
    constants folded            63
    algebraic simplifications   0
    common subexpressions       0
    copies / constants forwarded 96
    temporaries merged away     6
    dead instructions removed   64
    jumps removed or redirected 10
    unreachable instructions    8
    propagated across blocks    0
    dead assignments removed    20

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
 101: L1: if v uint== 0 goto L2
 102:     t1 = v uint& 1
 103:     t2 = n uint+ t1
 104:     n = t2
 105:     v = v uint>> 1
 106:     goto L1
 107: L2: return n

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
 108:     r = 0
 109:     i = 0
 110: L3: if i int>= 32 goto L4
 111:     t1 = r uint<< 1
 112:     t2 = v uint& 1
 113:     r = t1 uint| t2
 114:     v = v uint>> 1
 115:     i = i int+ 1
 116:     goto L3
 117: L4: return r

function isPowerOfTwo(unsigned int)        link name: _Z12isPowerOfTwoj
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    t1             temp   int                        4      4
    t2             temp   unsigned int               4      8
    t3             temp   unsigned int               4     12
    total width 16
  code
 118:     if v uint== 0 goto L5
 119:     t2 = v uint- 1
 120:     t3 = v uint& t2
 121:     if t3 uint== 0 goto L6
 122: L5: t1 = 0
 123:     goto L7
 124: L6: t1 = 1
 125: L7: return t1

function highestBit(unsigned int)        link name: _Z10highestBitj
  symbol table (name, kind, type, width, offset)
    v              param  unsigned int               4      0
    n              local  int                        4      4
    t1             temp   int                        4      8
    t2             temp   unsigned int               4     12
    t3             temp   int                        4     16
    total width 20
  code
 126:     n = -1
 127: L8: if v uint== 0 goto L9
 128:     v = v uint>> 1
 129:     n = n int+ 1
 130:     goto L8
 131: L9: return n

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
 132:   t1 = v uint<< k
 133:   t2 = 32 int- k
 134:   t3 = v uint>> t2
 135:   t4 = t1 uint| t3
 136:   return t4

function sign(int)        link name: _Z4signi
  symbol table (name, kind, type, width, offset)
    v              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    total width 16
  code
 137:      if v int> 0 goto L10
 138:      t1 = 0
 139:      goto L11
 140: L10: t1 = 1
 141: L11: if v int< 0 goto L12
 142:      t2 = 0
 143:      goto L13
 144: L12: t2 = 1
 145: L13: t3 = t1 int- t2
 146:      return t3

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
 147:   param 4042265140
 148:   t1 = call popcount(unsigned int), 1
 149:   param 4042265140
 150:   t2 = call reverseBits(unsigned int), 1
 151:   param 64
 152:   t3 = call isPowerOfTwo(unsigned int), 1
 153:   param 65
 154:   t4 = call isPowerOfTwo(unsigned int), 1
 155:   param 1000
 156:   t5 = call highestBit(unsigned int), 1
 157:   param "%d %x %d %d %d\n"
 158:   param t1
 159:   param t2
 160:   param t3
 161:   param t4
 162:   param t5
 163:   call printf, 6
 164:   param "%x %x %x %x\n"
 165:   param 4660
 166:   param 4042265151
 167:   param 252702155
 168:   param 252702155
 169:   call printf, 5
 170:   param 4042265140
 171:   param 8
 172:   t10 = call rotl(unsigned int, int), 2
 173:   param "%x %x %x\n"
 174:   param t10
 175:   param 251732800
 176:   param 15
 177:   call printf, 4
 178:   param "%d %d %u %u\n"
 179:   param 2147483647
 180:   param -2147483648
 181:   param 1
 182:   param 2147483648
 183:   call printf, 5
 184:   param "%d %d %d %d\n"
 185:   param -1
 186:   param -1
 187:   param 1
 188:   param 1073741824
 189:   call printf, 5
 190:   param "%d %d %d %d\n"
 191:   param 0
 192:   param -128
 193:   param 32767
 194:   param 0
 195:   call printf, 5
 196:   param "%d %d %d\n"
 197:   param -3
 198:   param -1
 199:   param -3
 200:   call printf, 4
 201:   param "%d %d %d\n"
 202:   param 0
 203:   param 1
 204:   param 1
 205:   call printf, 4
 206:   param -9
 207:   t52 = call sign(int), 1
 208:   param 0
 209:   t53 = call sign(int), 1
 210:   param 4
 211:   t54 = call sign(int), 1
 212:   param "%d %d %d %d\n"
 213:   param t52
 214:   param t53
 215:   param t54
 216:   param 1
 217:   call printf, 5
 218:   param "%d %d\n"
 219:   param 16
 220:   param 1
 221:   call printf, 3
 222:   param "%c %c %d\n"
 223:   param 97
 224:   param 65
 225:   param 25
 226:   call printf, 4
 227:   param 255
 228:   t73 = call popcount(unsigned int), 1
 229:   return t73


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
