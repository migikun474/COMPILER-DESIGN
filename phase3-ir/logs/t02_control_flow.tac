=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t02_control_flow.c
Optimization : no optimization

Three address code generated: 2 function(s), 140 instruction(s) for 'test/t02_control_flow.c'.

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
 103: L2: t2 = n int+ 10
 104:     n = t2
 105: L3: t3 = n int* 2
 106:     n = t3
 107:     goto L6
 108: L4: t4 = int- 1
 109:     n = t4
 110:     goto L6
 111: L5: if t1 int== 0 goto L1
 112:     if t1 int== 1 goto L2
 113:     if t1 int== 2 goto L2
 114:     if t1 int== 3 goto L3
 115:     goto L4
 116: L6: return n

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
 117:      total = 0
 118:      i = 0
 119: L7:  if i int< 10 goto L8
 120:      goto L14
 121: L8:  if i int== 2 goto L9
 122:      goto L10
 123: L9:  goto L13
 124: L10: if i int== 8 goto L11
 125:      goto L12
 126: L11: goto L14
 127: L12: t1 = total int+ i
 128:      total = t1
 129: L13: t2 = i int+ 1
 130:      i = t2
 131:      goto L7
 132: L14: param "for: %d %d\n"
 133:      param i
 134:      param total
 135:      call printf, 3
 136:      n = 5
 137:      fact = 1
 138: L15: if n int> 1 goto L16
 139:      goto L17
 140: L16: t3 = fact int* n
 141:      fact = t3
 142:      t4 = n int- 1
 143:      n = t4
 144:      goto L15
 145: L17: param "while: %d\n"
 146:      param fact
 147:      call printf, 2
 148: L18: t5 = n int+ 3
 149:      n = t5
 150:      if n int< 10 goto L18
 151:      goto L19
 152: L19: param "do: %d\n"
 153:      param n
 154:      call printf, 2
 155: L20: if n int>= 20 goto L22
 156:      goto L21
 157: L21: t6 = n int+ 4
 158:      n = t6
 159:      goto L20
 160: L22: param "until: %d\n"
 161:      param n
 162:      call printf, 2
 163:      i = 0
 164: L23: if i int< 6 goto L24
 165:      goto L25
 166: L24: param i
 167:      t7 = call classify(int), 1
 168:      param "%d "
 169:      param t7
 170:      call printf, 2
 171:      t8 = i int+ 1
 172:      i = t8
 173:      goto L23
 174: L25: param "\n"
 175:      call printf, 1
 176:      i = 0
 177: L26: if i int< 3 goto L27
 178:      goto L33
 179: L27: j = 0
 180: L28: if j int< 3 goto L29
 181:      goto L32
 182: L29: if j int> i goto L30
 183:      goto L31
 184: L30: goto L32
 185: L31: param "%d%d "
 186:      param i
 187:      param j
 188:      call printf, 3
 189:      t9 = j int+ 1
 190:      j = t9
 191:      goto L28
 192: L32: t10 = i int+ 1
 193:      i = t10
 194:      goto L26
 195: L33: param "\n"
 196:      call printf, 1
 197:      count = 0
 198: L34: t11 = count int+ 1
 199:      count = t11
 200:      if count int< 4 goto L35
 201:      goto L36
 202: L35: goto L34
 203: L36: if count int== 4 goto L37
 204:      goto L38
 205: L37: goto L39
 206: L38: count = 99
 207: L39: param "goto: %d\n"
 208:      param count
 209:      call printf, 2
 210:      x = 3
 211:      if x int> 5 goto L40
 212:      goto L41
 213: L40: param "big\n"
 214:      call printf, 1
 215:      goto L44
 216: L41: if x int> 2 goto L42
 217:      goto L43
 218: L42: param "medium\n"
 219:      call printf, 1
 220:      goto L44
 221: L43: param "small\n"
 222:      call printf, 1
 223: L44: t12 = x int- 1
 224:      x = t12
 225:      t13 = x
 226:      goto L47
 227: L45: goto L50
 228: L46: goto L48
 229:      goto L48
 230: L47: if t13 int== 1 goto L45
 231:      goto L46
 232: L48: if x int<= 0 goto L49
 233:      goto L50
 234: L49: goto L51
 235: L50: goto L44
 236: L51: param "x: %d\n"
 237:      param x
 238:      call printf, 2
 239:      return total


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
