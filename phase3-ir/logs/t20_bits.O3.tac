============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t20_bits.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 237 -> 141 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          237 -> 141   (40% fewer)

   constants folded                       84
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded          135
   temporaries merged away                 8
   dead instructions removed              94
   jumps removed or redirected            18
   unreachable instructions removed       19
   propagated across blocks                4
   dead assignments removed               24
   calls inlined                          10
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   instructions moved out of loops         0

============================================================================
 FUNCTION popcount(unsigned int)        (link name _Z8popcountj)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   unsigned int                    4       0
   n                local   int                             4       4
   t1               temp    unsigned int                    4       8
   t2               temp    unsigned int                    4      12
   (1 temporary no longer used after optimization not shown)

 Code: 8 instruction(s)

    100       n = 0
    101  L1:  if v uint== 0 goto L2
    102       t1 = v uint& 1
    103       t2 = n uint+ t1
    104       n = t2
    105       v = v uint>> 1
    106       goto L1
    107  L2:  return n

============================================================================
 FUNCTION reverseBits(unsigned int)        (link name _Z11reverseBitsj)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   unsigned int                    4       0
   r                local   unsigned int                    4       4
   i                local   int                             4       8
   t1               temp    unsigned int                    4      12
   t2               temp    unsigned int                    4      16
   (3 temporaries no longer used after optimization not shown)

 Code: 10 instruction(s)

    108       r = 0
    109       i = 0
    110  L3:  if i int>= 32 goto L4
    111       t1 = r uint<< 1
    112       t2 = v uint& 1
    113       r = t1 uint| t2
    114       v = v uint>> 1
    115       i = i int+ 1
    116       goto L3
    117  L4:  return r

============================================================================
 FUNCTION isPowerOfTwo(unsigned int)        (link name _Z12isPowerOfTwoj)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   unsigned int                    4       0
   t1               temp    int                             4       4
   t2               temp    unsigned int                    4       8
   t3               temp    unsigned int                    4      12

 Code: 8 instruction(s)

    118       if v uint== 0 goto L5
    119       t2 = v uint- 1
    120       t3 = v uint& t2
    121       if t3 uint== 0 goto L6
    122  L5:  t1 = 0
    123       goto L7
    124  L6:  t1 = 1
    125  L7:  return t1

============================================================================
 FUNCTION highestBit(unsigned int)        (link name _Z10highestBitj)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   unsigned int                    4       0
   n                local   int                             4       4
   (3 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    126       n = -1
    127  L8:  if v uint== 0 goto L9
    128       v = v uint>> 1
    129       n = n int+ 1
    130       goto L8
    131  L9:  return n

============================================================================
 FUNCTION rotl(unsigned int, int)        (link name _Z4rotlji)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   unsigned int                    4       0
   k                param   int                             4       4
   t1               temp    unsigned int                    4       8
   t2               temp    int                             4      12
   t3               temp    unsigned int                    4      16
   t4               temp    unsigned int                    4      20

 Code: 5 instruction(s)

    132     t1 = v uint<< k
    133     t2 = 32 int- k
    134     t3 = v uint>> t2
    135     t4 = t1 uint| t3
    136     return t4

============================================================================
 FUNCTION sign(int)        (link name _Z4signi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   int                             4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12

 Code: 10 instruction(s)

    137        if v int> 0 goto L10
    138        t1 = 0
    139        goto L11
    140  L10:  t1 = 1
    141  L11:  if v int< 0 goto L12
    142        t2 = 0
    143        goto L13
    144  L12:  t2 = 1
    145  L13:  t3 = t1 int- t2
    146        return t3

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 15 temporaries, frame 488 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   u                local   unsigned int                    4       0
   big              local   int                             4       4
   small            local   int                             4       8
   wrap             local   unsigned int                    4      12
   uc               local   unsigned char                   1      16
   sc               local   char                            1      17
   sh               local   short                           2      18
   us               local   unsigned short                  2      20
   flags            local   int                             4      24
   c                local   char                            1      28
   t74              temp    unsigned int                    4     324
   t75              temp    int                             4     328
   t76              temp    unsigned int                    4     332
   t77              temp    unsigned int                    4     336
   t78              temp    unsigned int                    4     340
   t79              temp    unsigned int                    4     344
   t80              temp    int                             4     348
   t81              temp    unsigned int                    4     352
   t82              temp    unsigned int                    4     356
   t91              temp    unsigned int                    4     392
   t92              temp    int                             4     396
   t111             temp    unsigned int                    4     472
   t112             temp    int                             4     476
   t113             temp    unsigned int                    4     480
   t114             temp    unsigned int                    4     484
   (99 temporaries no longer used after optimization not shown)

 Code: 94 instruction(s)

    147        t74 = 4042265140
    148        t75 = 0
    149  L14:  if t74 uint== 0 goto L15
    150        t76 = t74 uint& 1
    151        t77 = t75 uint+ t76
    152        t75 = t77
    153        t74 = t74 uint>> 1
    154        goto L14
    155  L15:  t78 = 4042265140
    156        t79 = 0
    157        t80 = 0
    158  L16:  if t80 int>= 32 goto L17
    159        t81 = t79 uint<< 1
    160        t82 = t78 uint& 1
    161        t79 = t81 uint| t82
    162        t78 = t78 uint>> 1
    163        t80 = t80 int+ 1
    164        goto L16
    165  L17:  t91 = 1000
    166        t92 = -1
    167  L18:  if t91 uint== 0 goto L19
    168        t91 = t91 uint>> 1
    169        t92 = t92 int+ 1
    170        goto L18
    171  L19:  param "%d %x %d %d %d\n"
    172        param t75
    173        param t79
    174        param 1
    175        param 0
    176        param t92
    177        call printf, 6
    178        param "%x %x %x %x\n"
    179        param 4660
    180        param 4042265151
    181        param 252702155
    182        param 252702155
    183        call printf, 5
    184        param "%x %x %x\n"
    185        param 4027725040
    186        param 251732800
    187        param 15
    188        call printf, 4
    189        param "%d %d %u %u\n"
    190        param 2147483647
    191        param -2147483648
    192        param 1
    193        param 2147483648
    194        call printf, 5
    195        param "%d %d %d %d\n"
    196        param -1
    197        param -1
    198        param 1
    199        param 1073741824
    200        call printf, 5
    201        param "%d %d %d %d\n"
    202        param 0
    203        param -128
    204        param 32767
    205        param 0
    206        call printf, 5
    207        param "%d %d %d\n"
    208        param -3
    209        param -1
    210        param -3
    211        call printf, 4
    212        param "%d %d %d\n"
    213        param 0
    214        param 1
    215        param 1
    216        call printf, 4
    217        param "%d %d %d %d\n"
    218        param -1
    219        param 0
    220        param 1
    221        param 1
    222        call printf, 5
    223        param "%d %d\n"
    224        param 16
    225        param 1
    226        call printf, 3
    227        param "%c %c %d\n"
    228        param 97
    229        param 65
    230        param 25
    231        call printf, 4
    232        t111 = 255
    233        t112 = 0
    234  L20:  if t111 uint== 0 goto L21
    235        t113 = t111 uint& 1
    236        t114 = t112 uint+ t113
    237        t112 = t114
    238        t111 = t111 uint>> 1
    239        goto L20
    240  L21:  return t112


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   popcount           function      int (unsigned int)         -           4    -    2  _Z8popcountj; defined
   reverseBits        function      unsigned int (unsigned int) -           6    -    1  _Z11reverseBitsj; defined
   isPowerOfTwo       function      int (unsigned int)         -          12    -    2  _Z12isPowerOfTwoj; defined
   highestBit         function      int (unsigned int)         -          13    -    1  _Z10highestBitj; defined
   rotl               function      unsigned int (unsigned int, int) -          14    -    1  _Z4rotlji; defined
   sign               function      int (int)                  -          15    -    3  _Z4signi; defined
   main               function      int (void)                 -          17    -    0  defined

 scope: global > popcount()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param       4    4    3  v.1
   n                  variable      int                        local       4    4    2  n.2

 scope: global > reverseBits()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param       6    4    2  v.3
   r                  variable      unsigned int               local       7    4    3  r.4

 scope: global > reverseBits() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       8    4    2  i.5

 scope: global > isPowerOfTwo()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param      12    4    3  v.6

 scope: global > highestBit()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param      13    4    2  v.7
   n                  variable      int                        local      13    4    2  n.8

 scope: global > rotl()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param      14    4    2  v.9
   k                  parameter     int                        param      14    4    2  k.10

 scope: global > sign()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      15    4    2  v.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   u                  variable      unsigned int               local      18    4    9  u.12
   big                variable      int                        local      23    4    1  big.13
   small              variable      int                        local      23    4    3  small.14
   wrap               variable      unsigned int               local      24    4    3  wrap.15
   uc                 variable      unsigned char              local      29    1    2  uc.16
   sc                 variable      char                       local      30    1    2  sc.17
   sh                 variable      short                      local      31    2    2  sh.18
   us                 variable      unsigned short             local      32    2    2  us.19
   flags              variable      int                        local      39    4    6  flags.20
   c                  variable      char                       local      45    1    3  c.21

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
