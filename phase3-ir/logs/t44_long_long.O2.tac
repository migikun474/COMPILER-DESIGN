============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t44_long_long.c
   Optimization  : -O2: -O1 plus data flow across blocks
   Result        : Optimized three address code (-O2): 88 -> 53 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O2)
----------------------------------------------------------------------------

   instructions                           88 -> 53   (39% fewer)

   constants folded                       16
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           42
   temporaries merged away                 0
   dead instructions removed              16
   jumps removed or redirected             3
   unreachable instructions removed        6
   propagated across blocks                0
   dead assignments removed               10

============================================================================
 FUNCTION mulAdd(long long, long long, long long)        (link name _Z6mulAddxxx)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   long long                       8       0
   b                param   long long                       8       8
   c                param   long long                       8      16
   t1               temp    long long                       8      24
   t2               temp    long long                       8      32

 Code: 3 instruction(s)

    100     t1 = a llong* b
    101     t2 = t1 llong+ c
    102     return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 8 temporaries, frame 264 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   long long                       8       0
   b                local   long long                       8       8
   m                local   long long                       8      16
   x                local   long long                       8      24
   neg              local   long long                       8      32
   big              local   unsigned long long              8      40
   dd               local   double                          8      48
   back             local   long long                       8      56
   keep             local   long long                       8      64
   r                local   long long                       8      72
   t5               temp    long long                       8     112
   t7               temp    long long                       8     128
   t8               temp    long long                       8     136
   t20              temp    double                          8     224
   t21              temp    double                          8     232
   t22              temp    long long                       8     240
   t23              temp    long long                       8     248
   t24              temp    long long                       8     256
   (16 temporaries no longer used after optimization not shown)

 Code: 50 instruction(s)

    103     param "%lld %lld\n"
    104     param 4294967296
    105     param -4294967296
    106     call printf, 3
    107     param 123456789
    108     param 1000003
    109     param -7
    110     t5 = call mulAdd(long long, long long, long long), 3
    111     t7 = t5 llong/ -1000
    112     t8 = t5 llong% 1000
    113     param "%lld %lld %lld\n"
    114     param t5
    115     param t7
    116     param t8
    117     call printf, 4
    118     param "%lld %lld %lld\n"
    119     param 2147483648
    120     param 4294967296
    121     param 4611686018427387904
    122     call printf, 4
    123     param "%lld %lld\n"
    124     param -62500000000
    125     param -142857142857
    126     call printf, 3
    127     param "%llu %llu\n"
    128     param 18446744073709551615
    129     param 6148914691236517205
    130     call printf, 3
    131     param "%d %d %d\n"
    132     param 1
    133     param 1
    134     param 1
    135     call printf, 4
    136     t20 = llongtodouble t5
    137     t21 = t20 double/ 3.0
    138     t22 = doubletollong t21
    139     param "%.0f %lld\n"
    140     param t20
    141     param t22
    142     call printf, 3
    143     param 2
    144     param 3
    145     param 4
    146     t23 = call mulAdd(long long, long long, long long), 3
    147     t24 = t23 llong+ 9000000000
    148     param "%lld %lld\n"
    149     param 9000000000
    150     param t24
    151     call printf, 3
    152     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   mulAdd             function      long long (long long, long long, long long) -           5    -    2  _Z6mulAddxxx; defined
   main               function      int (void)                 -           6    -    0  defined

 scope: global > mulAdd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     long long                  param       5    8    1  a.1
   b                  parameter     long long                  param       5    8    1  b.2
   c                  parameter     long long                  param       5    8    1  c.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      long long                  local       7    8    5  a.4
   b                  variable      long long                  local       7    8    3  b.5
   m                  variable      long long                  local       9    8    4  m.6
   x                  variable      long long                  local      11    8    3  x.7
   neg                variable      long long                  local      13    8    3  neg.8
   big                variable      unsigned long long         local      15    8    2  big.9
   dd                 variable      double                     local      18    8    2  dd.10
   back               variable      long long                  local      19    8    1  back.11
   keep               variable      long long                  local      21    8    2  keep.12
   r                  variable      long long                  local      22    8    1  r.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
