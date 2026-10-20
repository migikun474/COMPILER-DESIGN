=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t02_control_flow.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 140 -> 93 instruction(s) for 'test/t02_control_flow.c'.

optimization summary (-O1)
    instructions                140 -> 93   (33% fewer)
    constants folded            3
    algebraic simplifications   1
    common subexpressions       0
    copies / constants forwarded 7
    temporaries merged away     10
    dead instructions removed   2
    jumps removed or redirected 28
    unreachable instructions    15

function classify(int)        link name: _Z8classifyi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    t3             temp   int                        4     12
    t4             temp   int                        4     16
    total width 20
  code
 100:     t1 = n
 101:     goto L5
 102: L1: return 100
 103: L2: n = n int+ 10
 104: L3: n = n int<< 1
 105:     goto L6
 106: L4: n = -1
 107:     goto L6
 108: L5: if t1 int== 0 goto L1
 109:     if t1 int== 1 goto L2
 110:     if t1 int== 2 goto L2
 111:     if t1 int== 3 goto L3
 112:     goto L4
 113: L6: return n

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
 114:      total = 0
 115:      i = 0
 116: L7:  if i int>= 10 goto L9
 117:      if i int== 2 goto L8
 118:      if i int== 8 goto L9
 119:      total = total int+ i
 120: L8:  i = i int+ 1
 121:      goto L7
 122: L9:  param "for: %d %d\n"
 123:      param i
 124:      param total
 125:      call printf, 3
 126:      n = 5
 127:      fact = 1
 128: L10: if n int<= 1 goto L11
 129:      fact = fact int* n
 130:      n = n int- 1
 131:      goto L10
 132: L11: param "while: %d\n"
 133:      param fact
 134:      call printf, 2
 135: L12: t5 = n int+ 3
 136:      n = t5
 137:      if t5 int< 10 goto L12
 138:      param "do: %d\n"
 139:      param n
 140:      call printf, 2
 141: L13: if n int>= 20 goto L14
 142:      n = n int+ 4
 143:      goto L13
 144: L14: param "until: %d\n"
 145:      param n
 146:      call printf, 2
 147:      i = 0
 148: L15: if i int>= 6 goto L16
 149:      param i
 150:      t7 = call classify(int), 1
 151:      param "%d "
 152:      param t7
 153:      call printf, 2
 154:      i = i int+ 1
 155:      goto L15
 156: L16: param "\n"
 157:      call printf, 1
 158:      i = 0
 159: L17: if i int>= 3 goto L20
 160:      j = 0
 161: L18: if j int>= 3 goto L19
 162:      if j int> i goto L19
 163:      param "%d%d "
 164:      param i
 165:      param j
 166:      call printf, 3
 167:      j = j int+ 1
 168:      goto L18
 169: L19: i = i int+ 1
 170:      goto L17
 171: L20: param "\n"
 172:      call printf, 1
 173:      count = 0
 174: L21: t11 = count int+ 1
 175:      count = t11
 176:      if t11 int< 4 goto L21
 177:      if count int== 4 goto L22
 178:      count = 99
 179: L22: param "goto: %d\n"
 180:      param count
 181:      call printf, 2
 182:      x = 3
 183:      param "medium\n"
 184:      call printf, 1
 185: L23: t12 = x int- 1
 186:      x = t12
 187:      if t12 int== 1 goto L23
 188:      if x int> 0 goto L23
 189:      param "x: %d\n"
 190:      param x
 191:      call printf, 2
 192:      return total


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
