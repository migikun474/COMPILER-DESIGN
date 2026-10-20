============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t19_scopes.c
   Optimization  : no optimization
   Result        : Three address code generated: 7 function(s), 98 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 5 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   x                int                             4  100
   counter          int                             4  0
   hidden           int                             4  7
   n.1              int                             4  10
   calls.2          int                             4  0

============================================================================
 FUNCTION next()        (link name _Z4nextv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    100     t1 = n.1 int+ 5
    101     n.1 = t1
    102     return n.1

============================================================================
 FUNCTION twice()        (link name _Z5twicev)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 2 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0
   t2               temp    int                             4       4

 Code: 4 instruction(s)

    103     t1 = calls.2 int+ 1
    104     calls.2 = t1
    105     t2 = calls.2 int* 2
    106     return t2

============================================================================
 FUNCTION shadow(int)        (link name _Z6shadowi)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 4 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x.3              param   int                             4       0
   r                local   int                             4       4
   x.5              local   int                             4       8
   x.6              local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28

 Code: 11 instruction(s)

    107     r = x.3
    108     x.5 = 3
    109     t1 = r int+ x.5
    110     r = t1
    111     x.6 = 4
    112     t2 = r int+ x.6
    113     r = t2
    114     t3 = r int+ x.5
    115     r = t3
    116     t4 = r int+ x.3
    117     return t4

============================================================================
 FUNCTION useGlobal()        (link name _Z9useGlobalv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 2 instruction(s)

    118     t1 = x int+ hidden
    119     return t1

============================================================================
 FUNCTION changeGlobal()        (link name _Z12changeGlobalv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 2 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0
   t2               temp    int                             4       4

 Code: 5 instruction(s)

    120     t1 = x int+ 1
    121     x = t1
    122     t2 = counter int+ 1
    123     counter = t2
    124     return

============================================================================
 FUNCTION loops()        (link name _Z5loopsv)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 6 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   total            local   int                             4       0
   i.8              local   int                             4       4
   i2               local   int                             4       8
   i.10             local   int                             4      12
   i.11             local   int                             4      16
   t1               temp    int                             4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    int                             4      36
   t6               temp    int                             4      40

 Code: 22 instruction(s)

    125       total = 0
    126       i.8 = 0
    127  L1:  if i.8 int< 3 goto L2
    128       goto L6
    129  L2:  t1 = i.8 int* i.8
    130       i2 = t1
    131       i.10 = 10
    132  L3:  if i.10 int< 12 goto L4
    133       goto L5
    134  L4:  t2 = total int+ i.10
    135       total = t2
    136       t3 = i.10 int+ 1
    137       i.10 = t3
    138       goto L3
    139  L5:  t4 = total int+ i2
    140       total = t4
    141       t5 = i.8 int+ 1
    142       i.8 = t5
    143       goto L1
    144  L6:  i.11 = 50
    145       t6 = total int+ i.11
    146       return t6

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 7 parameter(s)/local(s), 11 temporaries, frame 72 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   x.12             local   int                             4       0
   n1               local   int                             4       4
   n2               local   int                             4       8
   a                local   int                             4      12
   b                local   int                             4      16
   c                local   int                             4      20
   counter.18       local   int                             4      24
   t1               temp    int                             4      28
   t2               temp    int                             4      32
   t3               temp    int                             4      36
   t4               temp    int                             4      40
   t5               temp    int                             4      44
   t6               temp    int                             4      48
   t7               temp    int                             4      52
   t8               temp    int                             4      56
   t9               temp    int                             4      60
   t10              temp    int                             4      64
   t11              temp    int                             4      68

 Code: 51 instruction(s)

    147     param 1
    148     t1 = call shadow(int), 1
    149     t2 = call useGlobal(), 0
    150     param "%d %d %d\n"
    151     param t1
    152     param t2
    153     param x
    154     call printf, 4
    155     call changeGlobal(), 0
    156     call changeGlobal(), 0
    157     x.12 = 5
    158     t3 = call useGlobal(), 0
    159     param "%d %d %d\n"
    160     param x.12
    161     param t3
    162     param counter
    163     call printf, 4
    164     t4 = call next(), 0
    165     n1 = t4
    166     t5 = call next(), 0
    167     n2 = t5
    168     param "%d %d\n"
    169     param n1
    170     param n2
    171     call printf, 3
    172     t6 = call twice(), 0
    173     a = t6
    174     t7 = call twice(), 0
    175     b = t7
    176     t8 = call twice(), 0
    177     c = t8
    178     param "%d %d %d\n"
    179     param a
    180     param b
    181     param c
    182     call printf, 4
    183     t9 = call loops(), 0
    184     param "%d\n"
    185     param t9
    186     call printf, 2
    187     t10 = int- 1
    188     counter.18 = t10
    189     t11 = counter.18 int- 1
    190     counter.18 = t11
    191     param "%d\n"
    192     param counter.18
    193     call printf, 2
    194     param "%d\n"
    195     param counter
    196     call printf, 2
    197     return x.12


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        global      5    4    4  
   counter            variable      int                        global      6    4    3  
   hidden             variable      int                        global      7    4    1  static
   next               function      int (void)                 -           9    -    2  _Z4nextv; defined
   twice              function      int (void)                 -          10    -    3  _Z5twicev; defined
   shadow             function      int (int)                  -          12    -    1  _Z6shadowi; defined
   useGlobal          function      int (void)                 -          26    -    2  _Z9useGlobalv; defined
   changeGlobal       function      void (void)                -          28    -    2  _Z12changeGlobalv; defined
   loops              function      int (void)                 -          30    -    1  _Z5loopsv; defined
   main               function      int (void)                 -          41    -    0  defined

 scope: global > next()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  variable      int                        static      9    4    2  n.1; static

 scope: global > twice()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        static     10    4    2  calls.2; static

 scope: global > shadow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  parameter     int                        param      12    4    2  x.3
   r                  variable      int                        local      13    4    4  r.4

 scope: global > shadow() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      15    4    2  x.5

 scope: global > shadow() > block > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      18    4    1  x.6

 scope: global > loops()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   total              variable      int                        local      31    4    3  total.7
   i                  variable      int                        local      37    4    1  i.11

 scope: global > loops() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      32    4    4  i.8

 scope: global > loops() > for > for body
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i2                 variable      int                        local      33    4    1  i2.9

 scope: global > loops() > for > for body > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      34    4    3  i.10

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  variable      int                        local      45    4    2  x.12
   n1                 variable      int                        local      47    4    1  n1.13
   n2                 variable      int                        local      47    4    1  n2.14
   a                  variable      int                        local      49    4    1  a.15
   b                  variable      int                        local      49    4    1  b.16
   c                  variable      int                        local      49    4    1  c.17

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   counter            variable      int                        local      53    4    2  counter.18

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
