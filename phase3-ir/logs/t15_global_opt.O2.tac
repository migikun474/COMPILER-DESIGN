=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t15_global_opt.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 138 -> 107 instruction(s) for 'test/t15_global_opt.c'.

optimization summary (-O2)
    instructions                138 -> 107   (22% fewer)
    constants folded            2
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 11
    temporaries merged away     8
    dead instructions removed   0
    jumps removed or redirected 6
    unreachable instructions    2
    propagated across blocks    8
    dead assignments removed    17

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
    total width 36
  code
 124:     b = a
 125:     if a int<= 3 goto L6
 126:     a = 0
 127: L6: t1 = b int+ a
 128:     call touch(), 0
 129:     t3 = call touch(), 0
 130:     t4 = t1 int+ 8
 131:     t5 = t4 int+ t3
 132:     return t5

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
 133:   x = 1
 134:   t1 = &x
 135:   x = 10
 136:   t2 = *t1
 137:   t3 = t2 int+ 1
 138:   s[0] = 3
 139:   s[4] = 4
 140:   t4 = s[0]
 141:   t5 = t3 int+ t4
 142:   return t5

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
 143:      k = 0
 144:      t = 9
 145: L7:  t1 = k int+ 1
 146:      k = t1
 147:      if t1 int< n goto L7
 148:      goto L11
 149: L8:  t = 1
 150:      goto L12
 151: L9:  t = 2
 152: L10: t = t int+ 10
 153:      goto L12
 154: L11: if n int== 1 goto L8
 155:      if n int== 2 goto L9
 156:      if n int== 3 goto L10
 157: L12: t4 = t1 int* 100
 158:      t5 = t4 int+ t
 159:      return t5

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
    total width 56
  code
 160:   param 0
 161:   t1 = call branches(int), 1
 162:   param 1
 163:   t2 = call branches(int), 1
 164:   param "%d %d\n"
 165:   param t1
 166:   param t2
 167:   call printf, 3
 168:   param 0
 169:   t3 = call loop(int), 1
 170:   param 1
 171:   t4 = call loop(int), 1
 172:   param 4
 173:   t5 = call loop(int), 1
 174:   param "%d %d %d\n"
 175:   param t3
 176:   param t4
 177:   param t5
 178:   call printf, 4
 179:   param 1
 180:   t6 = call rewritten(int), 1
 181:   param 9
 182:   t7 = call rewritten(int), 1
 183:   param "%d %d %d\n"
 184:   param t6
 185:   param t7
 186:   param g
 187:   call printf, 4
 188:   t8 = call viaPointer(), 0
 189:   param "%d\n"
 190:   param t8
 191:   call printf, 2
 192:   param 1
 193:   t9 = call jumps(int), 1
 194:   param 2
 195:   t10 = call jumps(int), 1
 196:   param 3
 197:   t11 = call jumps(int), 1
 198:   param 5
 199:   t12 = call jumps(int), 1
 200:   param "%d %d %d %d\n"
 201:   param t9
 202:   param t10
 203:   param t11
 204:   param t12
 205:   call printf, 5
 206:   return g


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
