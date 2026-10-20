=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t19_scopes.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 98 -> 92 instruction(s) for 'test/t19_scopes.c'.

optimization summary (-O3)
    instructions                98 -> 92   (6% fewer)
    constants folded            6
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 39
    temporaries merged away     7
    dead instructions removed   16
    jumps removed or redirected 2
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    15
    calls inlined               11
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

globals (name, type, width, initial value)
    x              int                        4  100
    counter        int                        4  0
    hidden         int                        4  7
    n.1            int                        4  10
    calls.2        int                        4  0

function next()        link name: _Z4nextv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 100:   t1 = n.1 int+ 5
 101:   n.1 = t1
 102:   return t1

function twice()        link name: _Z5twicev
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    t2             temp   int                        4      4
    total width 8
  code
 103:   t1 = calls.2 int+ 1
 104:   calls.2 = t1
 105:   t2 = t1 int<< 1
 106:   return t2

function shadow(int)        link name: _Z6shadowi
  symbol table (name, kind, type, width, offset)
    x.3            param  int                        4      0
    r              local  int                        4      4
    x.5            local  int                        4      8
    x.6            local  int                        4     12
    t1             temp   int                        4     16
    t2             temp   int                        4     20
    t3             temp   int                        4     24
    t4             temp   int                        4     28
    total width 32
  code
 107:   t1 = x.3 int+ 3
 108:   t2 = t1 int+ 4
 109:   t3 = t2 int+ 3
 110:   t4 = t3 int+ x.3
 111:   return t4

function useGlobal()        link name: _Z9useGlobalv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 112:   t1 = x int+ hidden
 113:   return t1

function changeGlobal()        link name: _Z12changeGlobalv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    t2             temp   int                        4      4
    total width 8
  code
 114:   x = x int+ 1
 115:   counter = counter int+ 1
 116:   return

function loops()        link name: _Z5loopsv
  symbol table (name, kind, type, width, offset)
    total          local  int                        4      0
    i.8            local  int                        4      4
    i2             local  int                        4      8
    i.10           local  int                        4     12
    i.11           local  int                        4     16
    t1             temp   int                        4     20
    t2             temp   int                        4     24
    t3             temp   int                        4     28
    t4             temp   int                        4     32
    t5             temp   int                        4     36
    t6             temp   int                        4     40
    total width 44
  code
 117:     total = 0
 118:     i.8 = 0
 119: L1: if i.8 int>= 3 goto L4
 120:     i2 = i.8 int* i.8
 121:     i.10 = 10
 122: L2: if i.10 int>= 12 goto L3
 123:     total = total int+ i.10
 124:     i.10 = i.10 int+ 1
 125:     goto L2
 126: L3: total = total int+ i2
 127:     i.8 = i.8 int+ 1
 128:     goto L1
 129: L4: t6 = total int+ 50
 130:     return t6

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    x.12           local  int                        4      0
    n1             local  int                        4      4
    n2             local  int                        4      8
    a              local  int                        4     12
    b              local  int                        4     16
    c              local  int                        4     20
    counter.18     local  int                        4     24
    t1             temp   int                        4     28
    t2             temp   int                        4     32
    t3             temp   int                        4     36
    t4             temp   int                        4     40
    t5             temp   int                        4     44
    t6             temp   int                        4     48
    t7             temp   int                        4     52
    t8             temp   int                        4     56
    t9             temp   int                        4     60
    t10            temp   int                        4     64
    t11            temp   int                        4     68
    t12            temp   int                        4     72
    t13            temp   int                        4     76
    t14            temp   int                        4     80
    t15            temp   int                        4     84
    t16            temp   int                        4     88
    t17            temp   int                        4     92
    t18            temp   int                        4     96
    t19            temp   int                        4    100
    t20            temp   int                        4    104
    t21            temp   int                        4    108
    t22            temp   int                        4    112
    t23            temp   int                        4    116
    t24            temp   int                        4    120
    t25            temp   int                        4    124
    t26            temp   int                        4    128
    t27            temp   int                        4    132
    t28            temp   int                        4    136
    t29            temp   int                        4    140
    t30            temp   int                        4    144
    t31            temp   int                        4    148
    total width 152
  code
 131:     t17 = x int+ hidden
 132:     param "%d %d %d\n"
 133:     param 12
 134:     param t17
 135:     param x
 136:     call printf, 4
 137:     x = x int+ 1
 138:     counter = counter int+ 1
 139:     x = x int+ 1
 140:     counter = counter int+ 1
 141:     t18 = x int+ hidden
 142:     param "%d %d %d\n"
 143:     param 5
 144:     param t18
 145:     param counter
 146:     call printf, 4
 147:     t19 = n.1 int+ 5
 148:     n.1 = t19
 149:     t20 = t19 int+ 5
 150:     n.1 = t20
 151:     param "%d %d\n"
 152:     param t19
 153:     param t20
 154:     call printf, 3
 155:     t21 = calls.2 int+ 1
 156:     calls.2 = t21
 157:     t22 = t21 int<< 1
 158:     t23 = t21 int+ 1
 159:     calls.2 = t23
 160:     t24 = t23 int<< 1
 161:     t25 = t23 int+ 1
 162:     calls.2 = t25
 163:     t26 = t25 int<< 1
 164:     param "%d %d %d\n"
 165:     param t22
 166:     param t24
 167:     param t26
 168:     call printf, 4
 169:     t27 = 0
 170:     t28 = 0
 171: L5: if t28 int>= 3 goto L8
 172:     t29 = t28 int* t28
 173:     t30 = 10
 174: L6: if t30 int>= 12 goto L7
 175:     t27 = t27 int+ t30
 176:     t30 = t30 int+ 1
 177:     goto L6
 178: L7: t27 = t27 int+ t29
 179:     t28 = t28 int+ 1
 180:     goto L5
 181: L8: t31 = t27 int+ 50
 182:     param "%d\n"
 183:     param t31
 184:     call printf, 2
 185:     param "%d\n"
 186:     param -2
 187:     call printf, 2
 188:     param "%d\n"
 189:     param counter
 190:     call printf, 2
 191:     return 5


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
x                  variable       int                        global   global                         5     4     4     x                    -                        
counter            variable       int                        global   global                         6     4     3     counter              -                        
hidden             variable       int                        global   global                         7     4     1     hidden               -                        static
next               function       int (void)                 -        global                         9     -     2     _Z4nextv             _Z4nextv                 defined
n                  variable       int                        static   global > next()                9     4     2     n.1                  -                        static
twice              function       int (void)                 -        global                         10    -     3     _Z5twicev            _Z5twicev                defined
calls              variable       int                        static   global > twice()               10    4     2     calls.2              -                        static
shadow             function       int (int)                  -        global                         12    -     1     _Z6shadowi           _Z6shadowi               defined
x                  parameter      int                        param    global > shadow()              12    4     2     x.3                  -                        
r                  variable       int                        local    global > shadow()              13    4     4     r.4                  -                        
x                  variable       int                        local    global > shadow() > block      15    4     2     x.5                  -                        
x                  variable       int                        local    global > shadow() > block > block 18    4     1     x.6                  -                        
useGlobal          function       int (void)                 -        global                         26    -     2     _Z9useGlobalv        _Z9useGlobalv            defined
changeGlobal       function       void (void)                -        global                         28    -     2     _Z12changeGlobalv    _Z12changeGlobalv        defined
loops              function       int (void)                 -        global                         30    -     1     _Z5loopsv            _Z5loopsv                defined
total              variable       int                        local    global > loops()               31    4     3     total.7              -                        
i                  variable       int                        local    global > loops() > for         32    4     4     i.8                  -                        
i2                 variable       int                        local    global > loops() > for > for body 33    4     1     i2.9                 -                        
i                  variable       int                        local    global > loops() > for > for body > for 34    4     3     i.10                 -                        
i                  variable       int                        local    global > loops()               37    4     1     i.11                 -                        
main               function       int (void)                 -        global                         41    -     0     main                 main                     defined
x                  variable       int                        local    global > main()                45    4     2     x.12                 -                        
n1                 variable       int                        local    global > main()                47    4     1     n1.13                -                        
n2                 variable       int                        local    global > main()                47    4     1     n2.14                -                        
a                  variable       int                        local    global > main()                49    4     1     a.15                 -                        
b                  variable       int                        local    global > main()                49    4     1     b.16                 -                        
c                  variable       int                        local    global > main()                49    4     1     c.17                 -                        
counter            variable       int                        local    global > main() > block        53    4     2     counter.18           -                        

=== Record Layouts ===
(no records)
