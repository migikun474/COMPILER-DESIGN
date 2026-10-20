=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t10_io.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 68 -> 55 instruction(s) for 'test/t10_io.c'.

optimization summary (-O3)
    instructions                68 -> 55   (19% fewer)
    constants folded            6
    algebraic simplifications   0
    common subexpressions       0
    copies / constants forwarded 10
    temporaries merged away     2
    dead instructions removed   7
    jumps removed or redirected 1
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    3
    calls inlined               0
    tail calls turned to jumps  0
    common across blocks        1
    moved out of loops          1

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    n              local  int                        4      0
    total          local  int                        4      4
    scale          local  double                     8      8
    name           local  char[16]                  16     16
    grade          local  char                       1     32
    i              local  int                        4     36
    v              local  int                        4     40
    f              local  float                      4     44
    c              local  char                       1     48
    s              local  short                      2     50
    t1             temp   int *                      4     52
    t2             temp   double *                   4     56
    t3             temp   char (*)[16]               4     60
    t4             temp   char *                     4     64
    t5             temp   int *                      4     68
    t6             temp   int                        4     72
    t7             temp   int                        4     76
    t8             temp   char (*)[16]               4     80
    t9             temp   int                        4     84
    t10            temp   double                     8     88
    t11            temp   double                     8     96
    t12            temp   int                        4    104
    t13            temp   int                        4    108
    t14            temp   short                      2    112
    t15            temp   double                     8    120
    t16            temp   int                        4    128
    t17            temp   int                        4    132
    total width 136
  code
 100:     total = 0
 101:     t1 = &n
 102:     t2 = &scale
 103:     t3 = &name
 104:     t4 = &grade
 105:     param "%d %lf %15s %c"
 106:     param t1
 107:     param t2
 108:     param t3
 109:     param t4
 110:     call scanf, 5
 111:     i = 0
 112:     t5 = &v
 113: L1: if i int>= n goto L2
 114:     param "%d"
 115:     param t5
 116:     call scanf, 2
 117:     total = total int+ v
 118:     i = i int+ 1
 119:     goto L1
 120: L2: t9 = chartoint grade
 121:     t10 = inttodouble total
 122:     t11 = t10 double* scale
 123:     param "%s %c %d %.2f\n"
 124:     param t3
 125:     param t9
 126:     param total
 127:     param t11
 128:     call printf, 5
 129:     param "[%5d] [%-5d] [%05d] [%x] [%o] [%c] [%%]\n"
 130:     param 42
 131:     param 42
 132:     param 42
 133:     param 255
 134:     param 8
 135:     param 122
 136:     call printf, 7
 137:     param "[%8.3f] [%-8.1f] [%10s] [%-6s] [%.3s]\n"
 138:     param 3.14159
 139:     param 2.5
 140:     param "right"
 141:     param "left"
 142:     param "truncated"
 143:     call printf, 6
 144:     param "%u %lld %d\n"
 145:     param 3000000000
 146:     param 9000000000
 147:     param -5
 148:     call printf, 4
 149:     param "%.2f %c %d\n"
 150:     param 1.25
 151:     param 113
 152:     param -3
 153:     call printf, 4
 154:     return total


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
main               function       int (void)                 -        global                         4     -     0     main                 main                     defined
n                  variable       int                        local    global > main()                5     4     2     n.1                  -                        
total              variable       int                        local    global > main()                5     4     4     total.2              -                        
scale              variable       double                     local    global > main()                6     8     2     scale.3              -                        
name               variable       char[16]                   local    global > main()                7     16    2     name.4               -                        
grade              variable       char                       local    global > main()                8     1     2     grade.5              -                        
i                  variable       int                        local    global > main() > for          10    4     2     i.6                  -                        
v                  variable       int                        local    global > main() > for > for body 11    4     2     v.7                  -                        
f                  variable       float                      local    global > main()                19    4     1     f.8                  -                        
c                  variable       char                       local    global > main()                20    1     1     c.9                  -                        
s                  variable       short                      local    global > main()                21    2     1     s.10                 -                        

=== Record Layouts ===
(no records)
