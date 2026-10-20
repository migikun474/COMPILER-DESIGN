=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t15_global_opt.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 138 -> 139 instruction(s) for 'test/t15_global_opt.c'.

optimization summary (-O3)
    instructions                138 -> 139   (0% fewer)
    constants folded            16
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 41
    temporaries merged away     12
    dead instructions removed   25
    jumps removed or redirected 10
    unreachable instructions    7
    propagated across blocks    11
    dead assignments removed    20
    calls inlined               10
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

globals (name, type, width, initial value)
    g              int                        4  0

function touch()        link name: _Z5touchv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 100:   t1 = g int+ 1
 101:   g = t1
 102:   return t1

function branches(int)        link name: _Z8branchesi
  symbol table (name, kind, type, width, offset)
    c              param  int                        4      0
    x              local  int                        4      4
    y              local  int                        4      8
    z              local  int                        4     12
    unused         local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    total width 40
  code
 103:     if c int== 0 goto L1
 104:     y = 6
 105:     goto L2
 106: L1: y = 7
 107: L2: z = 1
 108:     if c int== 0 goto L3
 109:     z = 2
 110: L3: t4 = 5 int+ y
 111:     t5 = t4 int+ z
 112:     return t5

function loop(int)        link name: _Z4loopi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    step           local  int                        4      4
    sum            local  int                        4      8
    last           local  int                        4     12
    i.10           local  int                        4     16
    scratch        local  int                        4     20
    i.12           local  int                        4     24
    t1             temp   int                        4     28
    t2             temp   int                        4     32
    t3             temp   int                        4     36
    t4             temp   int                        4     40
    t5             temp   int                        4     44
    total width 48
  code
 113:     sum = 0
 114:     last = 0
 115:     i.10 = 0
 116: L4: if i.10 int>= n goto L5
 117:     sum = sum int+ 3
 118:     last = i.10
 119:     i.10 = i.10 int+ 1
 120:     goto L4
 121: L5: t4 = sum int+ last
 122:     t5 = t4 int+ 100
 123:     return t5

function rewritten(int)        link name: _Z9rewritteni
  symbol table (name, kind, type, width, offset)
    a              param  int                        4      0
    b              local  int                        4      4
    c              local  int                        4      8
    d              local  int                        4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    t5             temp   int                        4     32
    t6             temp   int                        4     36
    t7             temp   int                        4     40
    total width 44
  code
 124:     b = a
 125:     if a int<= 3 goto L6
 126:     a = 0
 127: L6: t1 = b int+ a
 128:     t6 = g int+ 1
 129:     g = t6
 130:     t7 = t6 int+ 1
 131:     g = t7
 132:     t4 = t1 int+ 8
 133:     t5 = t4 int+ t7
 134:     return t5

function viaPointer()        link name: _Z10viaPointerv
  symbol table (name, kind, type, width, offset)
    x              local  int                        4      0
    y              local  int                        4      4
    p              local  int *                      4      8
    s              local  struct (unnamed at 44:5)     8     12
    t1             temp   int *                      4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    total width 40
  code
 135:   x = 1
 136:   t1 = &x
 137:   x = 10
 138:   t2 = *t1
 139:   t3 = t2 int+ 1
 140:   s[0] = 3
 141:   s[4] = 4
 142:   t4 = s[0]
 143:   t5 = t3 int+ t4
 144:   return t5

function jumps(int)        link name: _Z5jumpsi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    k              local  int                        4      4
    t              local  int                        4      8
    t1             temp   int                        4     12
    t2             temp   int                        4     16
    t3             temp   int                        4     20
    t4             temp   int                        4     24
    t5             temp   int                        4     28
    total width 32
  code
 145:      k = 0
 146:      t = 9
 147: L7:  t1 = k int+ 1
 148:      k = t1
 149:      if t1 int< n goto L7
 150:      goto L11
 151: L8:  t = 1
 152:      goto L12
 153: L9:  t = 2
 154: L10: t = t int+ 10
 155:      goto L12
 156: L11: if n int== 1 goto L8
 157:      if n int== 2 goto L9
 158:      if n int== 3 goto L10
 159: L12: t4 = t1 int* 100
 160:      t5 = t4 int+ t
 161:      return t5

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    r1             local  int                        4      0
    r9             local  int                        4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    t6             temp   int                        4     28
    t7             temp   int                        4     32
    t8             temp   int                        4     36
    t9             temp   int                        4     40
    t10            temp   int                        4     44
    t11            temp   int                        4     48
    t12            temp   int                        4     52
    t13            temp   int                        4     56
    t14            temp   int                        4     60
    t15            temp   int                        4     64
    t16            temp   int                        4     68
    t17            temp   int                        4     72
    t18            temp   int                        4     76
    t19            temp   int                        4     80
    t20            temp   int                        4     84
    t21            temp   int                        4     88
    t22            temp   int                        4     92
    t23            temp   int                        4     96
    t24            temp   int                        4    100
    t25            temp   int                        4    104
    t26            temp   int                        4    108
    t27            temp   int                        4    112
    t28            temp   int                        4    116
    t29            temp   int                        4    120
    t30            temp   int                        4    124
    t31            temp   int                        4    128
    t32            temp   int                        4    132
    t33            temp   int                        4    136
    t34            temp   int                        4    140
    t35            temp   int                        4    144
    t36            temp   int                        4    148
    t37            temp   int                        4    152
    t38            temp   int                        4    156
    t39            temp   int                        4    160
    t40            temp   int                        4    164
    t41            temp   int                        4    168
    t42            temp   int                        4    172
    t43            temp   int                        4    176
    t44            temp   int                        4    180
    t45            temp   int                        4    184
    t46            temp   int                        4    188
    t47            temp   int                        4    192
    t48            temp   int                        4    196
    t49            temp   int                        4    200
    t50            temp   int                        4    204
    t51            temp   int                        4    208
    t52            temp   int                        4    212
    t53            temp   int                        4    216
    t54            temp   int *                      4    220
    t55            temp   int                        4    224
    t56            temp   int                        4    228
    t57            temp   struct (unnamed at 44:5)     8    232
    t58            temp   int                        4    240
    t59            temp   int                        4    244
    total width 248
  code
 162:      param "%d %d\n"
 163:      param 13
 164:      param 13
 165:      call printf, 3
 166:      t24 = 0
 167:      t25 = 0
 168:      t26 = 0
 169: L13: if t26 int>= 0 goto L14
 170:      t24 = t24 int+ 3
 171:      t25 = t26
 172:      t26 = t26 int+ 1
 173:      goto L13
 174: L14: t27 = t24 int+ t25
 175:      t3 = t27 int+ 100
 176:      t30 = 0
 177:      t31 = 0
 178:      t32 = 0
 179: L15: if t32 int>= 1 goto L16
 180:      t30 = t30 int+ 3
 181:      t31 = t32
 182:      t32 = t32 int+ 1
 183:      goto L15
 184: L16: t33 = t30 int+ t31
 185:      t4 = t33 int+ 100
 186:      t36 = 0
 187:      t37 = 0
 188:      t38 = 0
 189: L17: if t38 int>= 4 goto L18
 190:      t36 = t36 int+ 3
 191:      t37 = t38
 192:      t38 = t38 int+ 1
 193:      goto L17
 194: L18: t39 = t36 int+ t37
 195:      t40 = t39 int+ 100
 196:      param "%d %d %d\n"
 197:      param t3
 198:      param t4
 199:      param t40
 200:      call printf, 4
 201:      call touch(), 0
 202:      t44 = call touch(), 0
 203:      t6 = 10 int+ t44
 204:      call touch(), 0
 205:      t50 = call touch(), 0
 206:      t52 = 17 int+ t50
 207:      param "%d %d %d\n"
 208:      param t6
 209:      param t52
 210:      param g
 211:      call printf, 4
 212:      t53 = 1
 213:      t54 = &t53
 214:      t53 = 10
 215:      t55 = *t54
 216:      t56 = t55 int+ 1
 217:      t57[0] = 3
 218:      t57[4] = 4
 219:      t58 = t57[0]
 220:      t59 = t56 int+ t58
 221:      param "%d\n"
 222:      param t59
 223:      call printf, 2
 224:      param 1
 225:      t9 = call jumps(int), 1
 226:      param 2
 227:      t10 = call jumps(int), 1
 228:      param 3
 229:      t11 = call jumps(int), 1
 230:      param 5
 231:      t12 = call jumps(int), 1
 232:      param "%d %d %d %d\n"
 233:      param t9
 234:      param t10
 235:      param t11
 236:      param t12
 237:      call printf, 5
 238:      return g


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
g                  variable       int                        global   global                         5     4     4     g                    -                        
touch              function       int (void)                 -        global                         6     -     2     _Z5touchv            _Z5touchv                defined
branches           function       int (int)                  -        global                         8     -     2     _Z8branchesi         _Z8branchesi             defined
c                  parameter      int                        param    global > branches()            8     4     2     c.1                  -                        
x                  variable       int                        local    global > branches()            9     4     3     x.2                  -                        
y                  variable       int                        local    global > branches()            9     4     4     y.3                  -                        
z                  variable       int                        local    global > branches()            11    4     2     z.4                  -                        
unused             variable       int                        local    global > branches()            13    4     0     unused.5             -                        
loop               function       int (int)                  -        global                         17    -     3     _Z4loopi             _Z4loopi                 defined
n                  parameter      int                        param    global > loop()                17    4     1     n.6                  -                        
step               variable       int                        local    global > loop()                18    4     1     step.7               -                        
sum                variable       int                        local    global > loop()                18    4     3     sum.8                -                        
last               variable       int                        local    global > loop()                18    4     2     last.9               -                        
i                  variable       int                        local    global > loop() > for          19    4     3     i.10                 -                        
scratch            variable       int                        local    global > loop() > for > for body 22    4     0     scratch.11           -                        
i                  variable       int                        local    global > loop()                24    4     1     i.12                 -                        
rewritten          function       int (int)                  -        global                         28    -     2     _Z9rewritteni        _Z9rewritteni            defined
a                  parameter      int                        param    global > rewritten()           28    4     7     a.13                 -                        
b                  variable       int                        local    global > rewritten()           29    4     1     b.14                 -                        
c                  variable       int                        local    global > rewritten()           31    4     1     c.15                 -                        
d                  variable       int                        local    global > rewritten()           33    4     2     d.16                 -                        
viaPointer         function       int (void)                 -        global                         38    -     1     _Z10viaPointerv      _Z10viaPointerv          defined
x                  variable       int                        local    global > viaPointer()          39    4     2     x.17                 -                        
y                  variable       int                        local    global > viaPointer()          39    4     3     y.18                 -                        
p                  variable       int *                      local    global > viaPointer()          40    4     1     p.19                 -                        
(unnamed at 44:5)  struct_tag     struct (unnamed at 44:5)   -        global > viaPointer()          44    -     0     (unnamed at 44:5)    -                        size 8
(unnamed at 44:5)::a field          int                        member   global > viaPointer() > struct (unnamed at 44:5) 44    4     2     (unnamed at 44:5)::a -                        public, offset 0
(unnamed at 44:5)::b field          int                        member   global > viaPointer() > struct (unnamed at 44:5) 44    4     1     (unnamed at 44:5)::b -                        public, offset 4
s                  variable       struct (unnamed at 44:5)   local    global > viaPointer()          44    8     3     s.20                 -                        
jumps              function       int (int)                  -        global                         49    -     4     _Z5jumpsi            _Z5jumpsi                defined
n                  parameter      int                        param    global > jumps()               49    4     2     n.21                 -                        
again              label          -                          -        global > jumps()               51    -     1     _Z5jumpsi.again      -                        
k                  variable       int                        local    global > jumps()               50    4     3     k.22                 -                        
t                  variable       int                        local    global > jumps()               50    4     5     t.23                 -                        
main               function       int (void)                 -        global                         62    -     0     main                 main                     defined
r1                 variable       int                        local    global > main()                65    4     1     r1.24                -                        
r9                 variable       int                        local    global > main()                65    4     1     r9.25                -                        

=== Record Layouts ===
struct (unnamed at 44:5): size 8, align 4
    +0  int a  [public]
    +4  int b  [public]
