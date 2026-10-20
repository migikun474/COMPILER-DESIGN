=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t19_scopes.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 98 -> 72 instruction(s) for 'test/t19_scopes.c'.

optimization summary (-O2)
    instructions                98 -> 72   (26% fewer)
    constants folded            2
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 21
    temporaries merged away     7
    dead instructions removed   2
    jumps removed or redirected 2
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    15

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
    total width 72
  code
 131:   param 1
 132:   t1 = call shadow(int), 1
 133:   t2 = call useGlobal(), 0
 134:   param "%d %d %d\n"
 135:   param t1
 136:   param t2
 137:   param x
 138:   call printf, 4
 139:   call changeGlobal(), 0
 140:   call changeGlobal(), 0
 141:   t3 = call useGlobal(), 0
 142:   param "%d %d %d\n"
 143:   param 5
 144:   param t3
 145:   param counter
 146:   call printf, 4
 147:   t4 = call next(), 0
 148:   t5 = call next(), 0
 149:   param "%d %d\n"
 150:   param t4
 151:   param t5
 152:   call printf, 3
 153:   t6 = call twice(), 0
 154:   t7 = call twice(), 0
 155:   t8 = call twice(), 0
 156:   param "%d %d %d\n"
 157:   param t6
 158:   param t7
 159:   param t8
 160:   call printf, 4
 161:   t9 = call loops(), 0
 162:   param "%d\n"
 163:   param t9
 164:   call printf, 2
 165:   param "%d\n"
 166:   param -2
 167:   call printf, 2
 168:   param "%d\n"
 169:   param counter
 170:   call printf, 2
 171:   return 5


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
