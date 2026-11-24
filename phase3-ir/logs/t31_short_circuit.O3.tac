============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t31_short_circuit.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 136 -> 61 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          136 -> 61   (55% fewer)

   constants folded                       23
   algebraic simplifications               4
   common subexpressions                   1
   copies / constants forwarded           76
   temporaries merged away                 6
   dead instructions removed              40
   jumps removed or redirected            17
   unreachable instructions removed       18
   propagated across blocks                2
   dead assignments removed               14
   calls inlined                          13
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           1

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

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

 Code: 61 instruction(s)

    100       calls = calls int* 10
    101       t40 = calls int* 10
    102       calls = t40 int+ 2
    103       calls = calls int* 10
    104       t46 = calls int* 10
    105       calls = t46 int+ 4
    106       t48 = calls int* 10
    107       calls = t48 int+ 5
    108       param "%d %d %d %d\n"
    109       param 0
    110       param 1
    111       param 1
    112       param calls
    113       call printf, 5
    114       calls = 0
    115       calls = 1
    116       calls = 17
    117       calls = 170
    118       calls = 1709
    119       param "%d %d %d\n"
    120       param 7
    121       param 9
    122       param 1709
    123       call printf, 4
    124       param "%d %d %d\n"
    125       param 0
    126       param -4
    127       param 8
    128       call printf, 4
    129       arr[0] = 10
    130       arr[4] = 20
    131       arr[8] = 30
    132       arr[12] = 40
    133       arr[16] = 50
    134       t23 = arr[4]
    135       t24 = t23 int+ 5
    136       arr[4] = t24
    137       t27 = arr[12]
    138       t28 = t27 int<< 1
    139       arr[12] = t28
    140       t29 = arr[4]
    141       t30 = arr[8]
    142       param "%d %d %d %d\n"
    143       param t29
    144       param t30
    145       param t28
    146       param 3
    147       call printf, 5
    148       n = 0
    149       k = 0
    150  L1:  t32 = n
    151       n = n int+ 1
    152       if t32 int>= 5 goto L2
    153       t34 = k int+ n
    154       k = t34
    155       if t34 int< 9 goto L1
    156  L2:  param "%d %d\n"
    157       param n
    158       param k
    159       call printf, 3
    160       return 0


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
