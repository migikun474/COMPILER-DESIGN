============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t31_short_circuit.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 136 -> 78 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          136 -> 78   (42% fewer)

   calls inlined                          13
   constants folded                       23
   algebraic simplifications               4
   common subexpressions                   1
   copies / constants forwarded           81
   temporaries merged away                 6
   dead instructions removed              40
   jumps removed or redirected            17
   unreachable instructions removed       18

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

============================================================================
 FUNCTION t(int)        (link name _Z1ti)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 3 instruction(s)

    100     t1 = calls int* 10
    101     calls = t1 int+ v
    102     return v

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 12 parameter(s)/local(s), 11 temporaries, frame 304 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r1               local   int                             4       0
   r2               local   int                             4       4
   r3               local   int                             4       8
   r4               local   int                             4      12
   r5               local   int                             4      16
   a                local   int                             4      20
   b                local   int                             4      24
   c                local   int                             4      28
   arr              local   int[5]                         20      32
   i                local   int                             4      52
   n                local   int                             4      56
   k                local   int                             4      60
   t23              temp    int                             4     152
   t24              temp    int                             4     156
   t27              temp    int                             4     168
   t28              temp    int                             4     172
   t29              temp    int                             4     176
   t30              temp    int                             4     180
   t32              temp    int                             4     188
   t34              temp    int                             4     196
   t40              temp    int                             4     220
   t46              temp    int                             4     244
   t48              temp    int                             4     252
   (49 temporaries no longer used after optimization not shown)

 Code: 75 instruction(s)

    103       calls = calls int* 10
    104       r1 = 0
    105       t40 = calls int* 10
    106       calls = t40 int+ 2
    107       r2 = 1
    108       calls = calls int* 10
    109       t46 = calls int* 10
    110       calls = t46 int+ 4
    111       t48 = calls int* 10
    112       calls = t48 int+ 5
    113       r3 = 1
    114       param "%d %d %d %d\n"
    115       param 0
    116       param 1
    117       param 1
    118       param calls
    119       call printf, 5
    120       calls = 0
    121       calls = 1
    122       calls = 17
    123       r4 = 7
    124       calls = 170
    125       calls = 1709
    126       r5 = 9
    127       param "%d %d %d\n"
    128       param 7
    129       param 9
    130       param 1709
    131       call printf, 4
    132       c = 4
    133       b = 4
    134       a = 4
    135       c = 8
    136       b = -4
    137       a = 0
    138       param "%d %d %d\n"
    139       param 0
    140       param -4
    141       param 8
    142       call printf, 4
    143       arr[0] = 10
    144       arr[4] = 20
    145       arr[8] = 30
    146       arr[12] = 40
    147       arr[16] = 50
    148       i = 1
    149       i = 2
    150       t23 = arr[4]
    151       t24 = t23 int+ 5
    152       arr[4] = t24
    153       i = 3
    154       t27 = arr[12]
    155       t28 = t27 int<< 1
    156       arr[12] = t28
    157       t29 = arr[4]
    158       t30 = arr[8]
    159       param "%d %d %d %d\n"
    160       param t29
    161       param t30
    162       param t28
    163       param 3
    164       call printf, 5
    165       n = 0
    166       k = 0
    167  L1:  t32 = n
    168       n = n int+ 1
    169       if t32 int>= 5 goto L2
    170       t34 = k int+ n
    171       k = t34
    172       if t34 int< 9 goto L1
    173  L2:  param "%d %d\n"
    174       param n
    175       param k
    176       call printf, 3
    177       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      5    4    5  
   t                  function      int (int)                  -           6    -   13  _Z1ti; defined
   main               function      int (void)                 -           7    -    0  defined

 scope: global > t()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param       6    4    2  v.1

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r1                 variable      int                        local       8    4    1  r1.2
   r2                 variable      int                        local       9    4    1  r2.3
   r3                 variable      int                        local      10    4    1  r3.4
   r4                 variable      int                        local      13    4    1  r4.5
   r5                 variable      int                        local      14    4    1  r5.6
   a                  variable      int                        local      16    4    3  a.7
   b                  variable      int                        local      16    4    3  b.8
   c                  variable      int                        local      16    4    3  c.9
   arr                variable      int[5]                     local      20   20    5  arr.10
   i                  variable      int                        local      21    4    3  i.11
   n                  variable      int                        local      25    4    3  n.12
   k                  variable      int                        local      25    4    2  k.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

0 1 1 2045
7 9 1709
0 -4 8
25 30 80 3
4 10

   exit code 0, 93 instructions executed
