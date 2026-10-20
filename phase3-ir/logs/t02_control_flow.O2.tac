=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t02_control_flow.c
Optimization : -O2: -O1 plus data flow across blocks

Optimized three address code (-O2): 140 -> 92 instruction(s) for 'test/t02_control_flow.c'.

optimization summary (-O2)
    instructions                140 -> 92   (34% fewer)
    constants folded            3
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 7
    temporaries merged away     10
    dead instructions removed   2
    jumps removed or redirected 28
    unreachable instructions    15
    propagated across blocks    8
    dead assignments removed    1

function classify(int)        link name: _Z8classifyi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 100:     goto L5
 101: L1: return 100
 102: L2: n = n int+ 10
 103: L3: n = n int<< 1
 104:     goto L6
 105: L4: n = -1
 106:     goto L6
 107: L5: if n int== 0 goto L1
 108:     if n int== 1 goto L2
 109:     if n int== 2 goto L2
 110:     if n int== 3 goto L3
 111:     goto L4
 112: L6: return n

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    i              local  int                        4      0
    total          local  int                        4      4
    n              local  int                        4      8
    fact           local  int                        4     12
    j              local  int                        4     16
    count          local  int                        4     20
    x              local  int                        4     24
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
    total width 80
  code
 113:      total = 0
 114:      i = 0
 115: L7:  if i int>= 10 goto L9
 116:      if i int== 2 goto L8
 117:      if i int== 8 goto L9
 118:      total = total int+ i
 119: L8:  i = i int+ 1
 120:      goto L7
 121: L9:  param "for: %d %d\n"
 122:      param i
 123:      param total
 124:      call printf, 3
 125:      n = 5
 126:      fact = 1
 127: L10: if n int<= 1 goto L11
 128:      fact = fact int* n
 129:      n = n int- 1
 130:      goto L10
 131: L11: param "while: %d\n"
 132:      param fact
 133:      call printf, 2
 134: L12: t5 = n int+ 3
 135:      n = t5
 136:      if t5 int< 10 goto L12
 137:      param "do: %d\n"
 138:      param t5
 139:      call printf, 2
 140: L13: if n int>= 20 goto L14
 141:      n = n int+ 4
 142:      goto L13
 143: L14: param "until: %d\n"
 144:      param n
 145:      call printf, 2
 146:      i = 0
 147: L15: if i int>= 6 goto L16
 148:      param i
 149:      t7 = call classify(int), 1
 150:      param "%d "
 151:      param t7
 152:      call printf, 2
 153:      i = i int+ 1
 154:      goto L15
 155: L16: param "\n"
 156:      call printf, 1
 157:      i = 0
 158: L17: if i int>= 3 goto L20
 159:      j = 0
 160: L18: if j int>= 3 goto L19
 161:      if j int> i goto L19
 162:      param "%d%d "
 163:      param i
 164:      param j
 165:      call printf, 3
 166:      j = j int+ 1
 167:      goto L18
 168: L19: i = i int+ 1
 169:      goto L17
 170: L20: param "\n"
 171:      call printf, 1
 172:      count = 0
 173: L21: t11 = count int+ 1
 174:      count = t11
 175:      if t11 int< 4 goto L21
 176:      if t11 int== 4 goto L22
 177:      count = 99
 178: L22: param "goto: %d\n"
 179:      param count
 180:      call printf, 2
 181:      x = 3
 182:      param "medium\n"
 183:      call printf, 1
 184: L23: t12 = x int- 1
 185:      x = t12
 186:      if t12 int== 1 goto L23
 187:      if t12 int> 0 goto L23
 188:      param "x: %d\n"
 189:      param t12
 190:      call printf, 2
 191:      return total


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
classify           function       int (int)                  -        global                         7     -     1     _Z8classifyi         _Z8classifyi             defined
n                  parameter      int                        param    global > classify()            7     4     7     n.1                  -                        
main               function       int (void)                 -        global                         18    -     0     main                 main                     defined
again              label          -                          -        global > main()                49    -     1     main.again           -                        
done               label          -                          -        global > main()                54    -     1     main.done            -                        
i                  variable       int                        local    global > main()                19    4     16    i.2                  -                        
total              variable       int                        local    global > main()                19    4     3     total.3              -                        
n                  variable       int                        local    global > main()                27    4     11    n.4                  -                        
fact               variable       int                        local    global > main()                27    4     3     fact.5               -                        
j                  variable       int                        local    global > main() > for > for body > for 41    4     4     j.6                  -                        
count              variable       int                        local    global > main()                48    4     5     count.7              -                        
x                  variable       int                        local    global > main()                57    4     6     x.8                  -                        

=== Record Layouts ===
(no records)
