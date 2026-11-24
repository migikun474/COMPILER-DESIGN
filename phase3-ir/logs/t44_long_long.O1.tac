============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t44_long_long.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 88 -> 49 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           88 -> 49   (44% fewer)

   calls inlined                           2
   constants folded                       26
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           68
   temporaries merged away                 0
   dead instructions removed              34
   jumps removed or redirected             3
   unreachable instructions removed        6

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

 Symbol table: 10 parameter(s)/local(s), 0 temporaries, frame 344 bytes

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
   (34 temporaries no longer used after optimization not shown)

 Code: 46 instruction(s)

    103     a = 4294967295
    104     b = 1
    105     param "%lld %lld\n"
    106     param 4294967296
    107     param -4294967296
    108     call printf, 3
    109     m = 123457159370360
    110     param "%lld %lld %lld\n"
    111     param 123457159370360
    112     param -123457159370
    113     param 360
    114     call printf, 4
    115     x = 1
    116     param "%lld %lld %lld\n"
    117     param 2147483648
    118     param 4294967296
    119     param 4611686018427387904
    120     call printf, 4
    121     neg = -1000000000000
    122     param "%lld %lld\n"
    123     param -62500000000
    124     param -142857142857
    125     call printf, 3
    126     big = 18446744073709551615
    127     param "%llu %llu\n"
    128     param 18446744073709551615
    129     param 6148914691236517205
    130     call printf, 3
    131     param "%d %d %d\n"
    132     param 1
    133     param 1
    134     param 1
    135     call printf, 4
    136     dd = 1.2345715937036e+14
    137     back = 41152386456786
    138     param "%.0f %lld\n"
    139     param 1.2345715937036e+14
    140     param 41152386456786
    141     call printf, 3
    142     keep = 9000000000
    143     r = 10
    144     param "%lld %lld\n"
    145     param 9000000000
    146     param 9000000010
    147     call printf, 3
    148     return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

4294967296 -4294967296
123457159370360 -123457159370 360
2147483648 4294967296 4611686018427387904
-62500000000 -142857142857
18446744073709551615 6148914691236517205
1 1 1
123457159370360 41152386456786
9000000000 9000000010

   exit code 0, 46 instructions executed
