=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t03_booleans.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 234 -> 70 instruction(s) for 'test/t03_booleans.c'.

optimization summary (-O3)
    instructions                234 -> 70   (70% fewer)
    constants folded            45
    algebraic simplifications   0
    common subexpressions       0
    copies / constants forwarded 57
    temporaries merged away     3
    dead instructions removed   28
    jumps removed or redirected 52
    unreachable instructions    53
    propagated across blocks    30
    dead assignments removed    26
    calls inlined               7
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

globals (name, type, width, initial value)
    calls          int                        4  0

function yes()        link name: _Z3yesv
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 100:   calls = calls int+ 1
 101:   return 1

function no()        link name: _Z2nov
  symbol table (name, kind, type, width, offset)
    t1             temp   int                        4      0
    total width 4
  code
 102:   calls = calls int+ 1
 103:   return 0

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    a              local  int                        4      0
    b              local  int                        4      4
    c              local  int                        4      8
    d              local  int                        4     12
    e              local  int                        4     16
    f              local  int                        4     20
    r              local  int                        4     24
    x              local  int                        4     28
    z              local  double                     8     32
    ch             local  char                       1     40
    p              local  int *                      4     44
    flag           local  bool                       1     48
    both           local  bool                       1     49
    big            local  unsigned int               4     52
    minus          local  int                        4     56
    t1             temp   int                        4     60
    t2             temp   int                        4     64
    t3             temp   int                        4     68
    t4             temp   int                        4     72
    t5             temp   int                        4     76
    t6             temp   int                        4     80
    t7             temp   int                        4     84
    t8             temp   int                        4     88
    t9             temp   int                        4     92
    t10            temp   int                        4     96
    t11            temp   int                        4    100
    t12            temp   int                        4    104
    t13            temp   int                        4    108
    t14            temp   int                        4    112
    t15            temp   int                        4    116
    t16            temp   int                        4    120
    t17            temp   int                        4    124
    t18            temp   int                        4    128
    t19            temp   int                        4    132
    t20            temp   int                        4    136
    t21            temp   int                        4    140
    t22            temp   int                        4    144
    t23            temp   int                        4    148
    t24            temp   int                        4    152
    t25            temp   int                        4    156
    t26            temp   int                        4    160
    t27            temp   int                        4    164
    t28            temp   int                        4    168
    t29            temp   bool                       1    172
    t30            temp   int                        4    176
    t31            temp   bool                       1    180
    t32            temp   int                        4    184
    t33            temp   int                        4    188
    t34            temp   int                        4    192
    t35            temp   int                        4    196
    t36            temp   int                        4    200
    t37            temp   int                        4    204
    total width 208
  code
 104:     param "%d\n"
 105:     param 1
 106:     call printf, 2
 107:     param "%d %d %d %d %d %d\n"
 108:     param 0
 109:     param 1
 110:     param 1
 111:     param 0
 112:     param 1
 113:     param 0
 114:     call printf, 7
 115:     calls = 0
 116:     calls = 1
 117:     param "calls after &&: %d\n"
 118:     param 1
 119:     call printf, 2
 120:     calls = 0
 121:     calls = 1
 122:     param "or taken\n"
 123:     call printf, 1
 124:     param "calls after ||: %d\n"
 125:     param calls
 126:     call printf, 2
 127:     calls = 0
 128:     calls = 1
 129:     calls = 2
 130:     calls = 3
 131:     param "%d %d\n"
 132:     param 1
 133:     param 3
 134:     call printf, 3
 135:     x = 0
 136:     param "%d %d %d %d %d\n"
 137:     param 1
 138:     param 0
 139:     param 1
 140:     param 1
 141:     param 1
 142:     call printf, 6
 143:     param "double is true\n"
 144:     call printf, 1
 145:     param "null pointer is false\n"
 146:     call printf, 1
 147:     param "%d\n"
 148:     param 2
 149:     call printf, 2
 150:     param "%d %d\n"
 151:     param 1
 152:     param 0
 153:     call printf, 3
 154:     param "%d %d\n"
 155:     param 1
 156:     param 1
 157:     call printf, 3
 158: L1: if x int>= 3 goto L2
 159:     if x int== 2 goto L2
 160:     x = x int+ 1
 161:     goto L1
 162: L2: param "%d\n"
 163:     param x
 164:     call printf, 2
 165:     param "%d %d\n"
 166:     param 1
 167:     param 1
 168:     call printf, 3
 169:     return 1


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
calls              variable       int                        global   global                         4     4     8     calls                -                        
yes                function       int (void)                 -        global                         5     -     3     _Z3yesv              _Z3yesv                  defined
no                 function       int (void)                 -        global                         6     -     4     _Z2nov               _Z2nov                   defined
main               function       int (void)                 -        global                         8     -     0     main                 main                     defined
a                  variable       int                        local    global > main()                9     4     9     a.1                  -                        
b                  variable       int                        local    global > main()                9     4     8     b.2                  -                        
c                  variable       int                        local    global > main()                9     4     5     c.3                  -                        
d                  variable       int                        local    global > main()                9     4     2     d.4                  -                        
e                  variable       int                        local    global > main()                9     4     1     e.5                  -                        
f                  variable       int                        local    global > main()                9     4     1     f.6                  -                        
r                  variable       int                        local    global > main()                10    4     10    r.7                  -                        
x                  variable       int                        local    global > main()                25    4     6     x.8                  -                        
z                  variable       double                     local    global > main()                26    8     2     z.9                  -                        
ch                 variable       char                       local    global > main()                27    1     2     ch.10                -                        
p                  variable       int *                      local    global > main()                28    4     2     p.11                 -                        
flag               variable       bool                       local    global > main()                36    1     2     flag.12              -                        
both               variable       bool                       local    global > main()                37    1     1     both.13              -                        
big                variable       unsigned int               local    global > main()                41    4     1     big.14               -                        
minus              variable       int                        local    global > main()                42    4     1     minus.15             -                        

=== Record Layouts ===
(no records)
