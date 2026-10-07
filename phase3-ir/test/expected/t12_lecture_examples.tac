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
 100:      b = 2
 101:      c = 3
 102:      d = 4
 103:      e = 5
 104:      f = 6
 105:      i = 1
 106:      r = 1.5
 107:      t1 = int- c
 108:      t2 = b int* t1
 109:      t3 = int- c
 110:      t4 = b int* t3
 111:      t5 = t2 int+ t4
 112:      a = t5
 113: L1:  if a int< b goto L2
 114:      goto L3
 115: L2:  t6 = a int+ 1
 116:      a = t6
 117:      goto L1
 118: L3:  if a int< b goto L4
 119:      goto L5
 120: L4:  x = 1
 121:      goto L6
 122: L5:  x = 2
 123: L6:  if a int< b goto L7
 124:      t7 = 0
 125:      goto L8
 126: L7:  t7 = 1
 127: L8:  y = t7
 128:      if a int< b goto L12
 129:      goto L9
 130: L9:  if c int< d goto L10
 131:      goto L11
 132: L10: if e int< f goto L12
 133:      goto L11
 134: L11: t8 = 0
 135:      goto L13
 136: L12: t8 = 1
 137: L13: y = t8
 138:      t9 = inttodouble i
 139:      t10 = r double+ t9
 140:      r = t10
 141:      t11 = i int* 4                      (w = 4)
 142:      t12 = arr[t11]
 143:      x = t12
 144:      t13 = i int* 4                      (n2 = 4)
 145:      t14 = t13 int+ 2
 146:      t15 = t14 int* 4                    (w = 4)
 147:      m[t15] = x
 148:      return y

