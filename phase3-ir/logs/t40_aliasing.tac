============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t40_aliasing.c
   Optimization  : no optimization
   Result        : Three address code generated: 4 function(s), 86 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                int                             4  1

 As three address code (initial values, in place before main runs):

    g = 1

============================================================================
 FUNCTION bump()        (link name _Z4bumpv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    100     t1 = g int+ 10
    101     g = t1
    102     return

============================================================================
 FUNCTION setp(int *, int)        (link name _Z4setpPii)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   int *                           4       0
   v                param   int                             4       4

 Code: 2 instruction(s)

    103     *p = v
    104     return

============================================================================
 FUNCTION swap(int *, int *)        (link name _Z4swapPiS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int *                           4       0
   b                param   int *                           4       4
   t                local   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16

 Code: 6 instruction(s)

    105     t1 = *a
    106     t = t1
    107     t2 = *b
    108     *a = t2
    109     *b = t
    110     return

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 21 temporaries, frame 148 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x                local   int                             4       0
   p                local   int *                           4       4
   y                local   int                             4       8
   z                local   int                             4      12
   q                local   int *                           4      16
   a                local   int[4]                         16      20
   e                local   int *                           4      36
   i                local   int                             4      40
   before           local   int                             4      44
   h                local   int                             4      48
   v                local   int                             4      52
   m                local   int                             4      56
   n                local   int                             4      60
   t1               temp    int *                           4      64
   t2               temp    int                             4      68
   t3               temp    int                             4      72
   t4               temp    int *                           4      76
   t5               temp    int                             4      80
   t6               temp    int                             4      84
   t7               temp    int *                           4      88
   t8               temp    int *                           4      92
   t9               temp    int                             4      96
   t10              temp    int                             4     100
   t11              temp    int                             4     104
   t12              temp    int                             4     108
   t13              temp    int                             4     112
   t14              temp    int                             4     116
   t15              temp    int                             4     120
   t16              temp    int *                           4     124
   t17              temp    int                             4     128
   t18              temp    int *                           4     132
   t19              temp    int *                           4     136
   t20              temp    int *                           4     140
   t21              temp    int *                           4     144

 Code: 75 instruction(s)

    111     x = 5
    112     t1 = &x
    113     p = t1
    114     t2 = x int+ 1
    115     y = t2
    116     *p = 100
    117     t3 = x int+ 1
    118     z = t3
    119     param "%d %d\n"
    120     param y
    121     param z
    122     call printf, 3
    123     t4 = &x
    124     q = t4
    125     *q = 7
    126     t5 = *p
    127     t6 = x int* 2
    128     param "%d %d\n"
    129     param t5
    130     param t6
    131     call printf, 3
    132     a[0] = 1
    133     a[4] = 2
    134     a[8] = 3
    135     a[12] = 4
    136     t7 = &a
    137     t8 = t7 ptr+ 8
    138     e = t8
    139     i = 2
    140     t9 = i int* 4                       (w = 4)
    141     t10 = a[t9]
    142     before = t10
    143     *e = 9
    144     t11 = i int* 4                      (w = 4)
    145     t12 = a[t11]
    146     t13 = a[8]
    147     t14 = *e
    148     t15 = t13 int+ t14
    149     param "%d %d %d\n"
    150     param before
    151     param t12
    152     param t15
    153     call printf, 4
    154     h = g
    155     call bump(), 0
    156     param "%d %d\n"
    157     param h
    158     param g
    159     call printf, 3
    160     v = 3
    161     t16 = &v
    162     param t16
    163     param 4
    164     call setp(int *, int), 2
    165     t17 = v int* v
    166     param "%d\n"
    167     param t17
    168     call printf, 2
    169     m = 1
    170     n = 2
    171     t18 = &m
    172     t19 = &n
    173     param t18
    174     param t19
    175     call swap(int *, int *), 2
    176     t20 = &m
    177     t21 = &m
    178     param t20
    179     param t21
    180     call swap(int *, int *), 2
    181     param "%d %d\n"
    182     param m
    183     param n
    184     call printf, 3
    185     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   g                  variable      int                        global      5    4    4  
   bump               function      void (void)                -           6    -    1  _Z4bumpv; defined
   setp               function      void (int *, int)          -           7    -    1  _Z4setpPii; defined
   swap               function      void (int *, int *)        -           8    -    2  _Z4swapPiS_; defined
   main               function      int (void)                 -           9    -    0  defined

 scope: global > setp()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     int *                      param       7    4    1  p.1
   v                  parameter     int                        param       7    4    1  v.2

 scope: global > swap()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int *                      param       8    4    2  a.3
   b                  parameter     int *                      param       8    4    2  b.4
   t                  variable      int                        local       8    4    1  t.5

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      10    4    5  x.6
   p                  variable      int *                      local      11    4    2  p.7
   y                  variable      int                        local      12    4    1  y.8
   z                  variable      int                        local      14    4    1  z.9
   q                  variable      int *                      local      16    4    1  q.10
   a                  variable      int[4]                     local      19   16    4  a.11
   e                  variable      int *                      local      20    4    2  e.12
   i                  variable      int                        local      21    4    2  i.13
   before             variable      int                        local      21    4    1  before.14
   h                  variable      int                        local      24    4    1  h.15
   v                  variable      int                        local      27    4    3  v.16
   m                  variable      int                        local      30    4    4  m.17
   n                  variable      int                        local      30    4    2  n.18

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
