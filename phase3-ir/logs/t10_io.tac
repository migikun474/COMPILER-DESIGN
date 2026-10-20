=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t10_io.c
Optimization : no optimization

Three address code generated: 1 function(s), 68 instruction(s) for 'test/t10_io.c'.

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
 112: L1: if i int< n goto L2
 113:     goto L3
 114: L2: t5 = &v
 115:     param "%d"
 116:     param t5
 117:     call scanf, 2
 118:     t6 = total int+ v
 119:     total = t6
 120:     t7 = i int+ 1
 121:     i = t7
 122:     goto L1
 123: L3: t8 = &name
 124:     t9 = chartoint grade
 125:     t10 = inttodouble total
 126:     t11 = t10 double* scale
 127:     param "%s %c %d %.2f\n"
 128:     param t8
 129:     param t9
 130:     param total
 131:     param t11
 132:     call printf, 5
 133:     param "[%5d] [%-5d] [%05d] [%x] [%o] [%c] [%%]\n"
 134:     param 42
 135:     param 42
 136:     param 42
 137:     param 255
 138:     param 8
 139:     param 122
 140:     call printf, 7
 141:     param "[%8.3f] [%-8.1f] [%10s] [%-6s] [%.3s]\n"
 142:     param 3.14159
 143:     param 2.5
 144:     param "right"
 145:     param "left"
 146:     param "truncated"
 147:     call printf, 6
 148:     t12 = int- 5
 149:     param "%u %lld %d\n"
 150:     param 3000000000
 151:     param 9000000000
 152:     param t12
 153:     call printf, 4
 154:     f = 1.25
 155:     c = 113
 156:     t13 = int- 3
 157:     t14 = inttoshort t13
 158:     s = t14
 159:     t15 = floattodouble f
 160:     t16 = chartoint c
 161:     t17 = shorttoint s
 162:     param "%.2f %c %d\n"
 163:     param t15
 164:     param t16
 165:     param t17
 166:     call printf, 4
 167:     return total


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
