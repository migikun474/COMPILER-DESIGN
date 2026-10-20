=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t12_lecture_examples.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 49 -> 7 instruction(s) for 'test/t12_lecture_examples.c'.

optimization summary (-O3)
    instructions                49 -> 7   (85% fewer)
    constants folded            10
    algebraic simplifications   3
    common subexpressions       1
    copies / constants forwarded 17
    temporaries merged away     2
    dead instructions removed   12
    jumps removed or redirected 11
    unreachable instructions    2
    propagated across blocks    11
    dead assignments removed    14
    calls inlined               0
    tail calls turned to jumps  0
    common across blocks        0
    moved out of loops          0

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
 100:     a = -12
 101: L1: if a int>= 2 goto L2
 102:     a = a int+ 1
 103:     goto L1
 104: L2: t12 = arr[4]
 105:     m[24] = t12
 106:     return 1


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
