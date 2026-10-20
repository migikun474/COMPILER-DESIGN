=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t12_lecture_examples.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 49 -> 36 instruction(s) for 'test/t12_lecture_examples.c'.

optimization summary (-O1)
    instructions                49 -> 36   (26% fewer)
    constants folded            5
    algebraic simplifications   3
    common subexpressions       1
    copies / constants forwarded 12
    temporaries merged away     2
    dead instructions removed   6
    jumps removed or redirected 5
    unreachable instructions    0

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    a              local  int                        4      0
    b              local  int                        4      4
    c              local  int                        4      8
    d              local  int                        4     12
    e              local  int                        4     16
    f              local  int                        4     20
    i              local  int                        4     24
    x              local  int                        4     28
    y              local  int                        4     32
    arr            local  int[10]                   40     36
    m              local  int[3][4]                 48     76
    r              local  double                     8    128
    t1             temp   int                        4    136
    t2             temp   int                        4    140
    t3             temp   int                        4    144
    t4             temp   int                        4    148
    t5             temp   int                        4    152
    t6             temp   int                        4    156
    t7             temp   int                        4    160
    t8             temp   int                        4    164
    t9             temp   double                     8    168
    t10            temp   double                     8    176
    t11            temp   int                        4    184
    t12            temp   int                        4    188
    t13            temp   int                        4    192
    t14            temp   int                        4    196
    t15            temp   int                        4    200
    total width 204
  code
 100:     b = 2
 101:     c = 3
 102:     d = 4
 103:     e = 5
 104:     f = 6
 105:     i = 1
 106:     r = 1.5
 107:     a = -12
 108: L1: if a int>= b goto L2
 109:     a = a int+ 1
 110:     goto L1
 111: L2: if a int>= b goto L3
 112:     x = 1
 113:     goto L4
 114: L3: x = 2
 115: L4: if a int< b goto L5
 116:     t7 = 0
 117:     goto L6
 118: L5: t7 = 1
 119: L6: y = t7
 120:     if a int< b goto L8
 121:     if c int>= d goto L7
 122:     if e int< f goto L8
 123: L7: t8 = 0
 124:     goto L9
 125: L8: t8 = 1
 126: L9: y = t8
 127:     t9 = inttodouble i
 128:     r = r double+ t9
 129:     t11 = i int<< 2                     (w = 4)
 130:     t12 = arr[t11]
 131:     x = t12
 132:     t14 = t11 int+ 2
 133:     t15 = t14 int<< 2                   (w = 4)
 134:     m[t15] = t12
 135:     return t8


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
main               function       int (void)                 -        global                         3     -     0     main                 main                     defined
a                  variable       int                        local    global > main()                4     4     7     a.1                  -                        
b                  variable       int                        local    global > main()                4     4     6     b.2                  -                        
c                  variable       int                        local    global > main()                4     4     3     c.3                  -                        
d                  variable       int                        local    global > main()                4     4     1     d.4                  -                        
e                  variable       int                        local    global > main()                4     4     1     e.5                  -                        
f                  variable       int                        local    global > main()                4     4     1     f.6                  -                        
i                  variable       int                        local    global > main()                4     4     3     i.7                  -                        
x                  variable       int                        local    global > main()                4     4     4     x.8                  -                        
y                  variable       int                        local    global > main()                4     4     3     y.9                  -                        
arr                variable       int[10]                    local    global > main()                5     40    1     arr.10               -                        
m                  variable       int[3][4]                  local    global > main()                6     48    1     m.11                 -                        
r                  variable       double                     local    global > main()                7     8     2     r.12                 -                        

=== Record Layouts ===
(no records)
