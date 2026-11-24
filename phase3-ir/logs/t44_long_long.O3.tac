============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t44_long_long.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 88 -> 36 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                           88 -> 36   (59% fewer)

   constants folded                       26
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           64
   temporaries merged away                 0
   dead instructions removed              34
   jumps removed or redirected             3
   unreachable instructions removed        6
   propagated across blocks                0
   dead assignments removed               10
   calls inlined                           2
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed           1

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

 Code: 36 instruction(s)

    100     param "%lld %lld\n"
    101     param 4294967296
    102     param -4294967296
    103     call printf, 3
    104     param "%lld %lld %lld\n"
    105     param 123457159370360
    106     param -123457159370
    107     param 360
    108     call printf, 4
    109     param "%lld %lld %lld\n"
    110     param 2147483648
    111     param 4294967296
    112     param 4611686018427387904
    113     call printf, 4
    114     param "%lld %lld\n"
    115     param -62500000000
    116     param -142857142857
    117     call printf, 3
    118     param "%llu %llu\n"
    119     param 18446744073709551615
    120     param 6148914691236517205
    121     call printf, 3
    122     param "%d %d %d\n"
    123     param 1
    124     param 1
    125     param 1
    126     call printf, 4
    127     param "%.0f %lld\n"
    128     param 1.2345715937036e+14
    129     param 41152386456786
    130     call printf, 3
    131     param "%lld %lld\n"
    132     param 9000000000
    133     param 9000000010
    134     call printf, 3
    135     return 0


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
