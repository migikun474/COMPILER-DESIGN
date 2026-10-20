============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t20_bits.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 237 -> 150 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          237 -> 150   (36% fewer)

   constants folded                       63
   algebraic simplifications               0
   common subexpressions                   0
   copies / constants forwarded           96
   temporaries merged away                 6
   dead instructions removed              64
   jumps removed or redirected            10
   unreachable instructions removed        8

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

 Symbol table: 10 parameter(s)/local(s), 10 temporaries, frame 324 bytes

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
   t1               temp    int                             4      32
   t2               temp    unsigned int                    4      36
   t3               temp    int                             4      40
   t4               temp    int                             4      44
   t5               temp    int                             4      48
   t10              temp    unsigned int                    4      68
   t52              temp    int                             4     236
   t53              temp    int                             4     240
   t54              temp    int                             4     244
   t73              temp    int                             4     320
   (63 temporaries no longer used after optimization not shown)

 Code: 103 instruction(s)

    147     u = 4042265140
    148     param 4042265140
    149     t1 = call popcount(unsigned int), 1
    150     param 4042265140
    151     t2 = call reverseBits(unsigned int), 1
    152     param 64
    153     t3 = call isPowerOfTwo(unsigned int), 1
    154     param 65
    155     t4 = call isPowerOfTwo(unsigned int), 1
    156     param 1000
    157     t5 = call highestBit(unsigned int), 1
    158     param "%d %x %d %d %d\n"
    159     param t1
    160     param t2
    161     param t3
    162     param t4
    163     param t5
    164     call printf, 6
    165     param "%x %x %x %x\n"
    166     param 4660
    167     param 4042265151
    168     param 252702155
    169     param 252702155
    170     call printf, 5
    171     param 4042265140
    172     param 8
    173     t10 = call rotl(unsigned int, int), 2
    174     param "%x %x %x\n"
    175     param t10
    176     param 251732800
    177     param 15
    178     call printf, 4
    179     big = 2147483647
    180     small = -2147483648
    181     wrap = 4294967295
    182     wrap = 1
    183     param "%d %d %u %u\n"
    184     param 2147483647
    185     param -2147483648
    186     param 1
    187     param 2147483648
    188     call printf, 5
    189     param "%d %d %d %d\n"
    190     param -1
    191     param -1
    192     param 1
    193     param 1073741824
    194     call printf, 5
    195     uc = 255
    196     sc = 127
    197     sh = -32768
    198     us = 65535
    199     uc = 0
    200     sc = -128
    201     sh = 32767
    202     us = 0
    203     param "%d %d %d %d\n"
    204     param 0
    205     param -128
    206     param 32767
    207     param 0
    208     call printf, 5
    209     param "%d %d %d\n"
    210     param -3
    211     param -1
    212     param -3
    213     call printf, 4
    214     param "%d %d %d\n"
    215     param 0
    216     param 1
    217     param 1
    218     call printf, 4
    219     param -9
    220     t52 = call sign(int), 1
    221     param 0
    222     t53 = call sign(int), 1
    223     param 4
    224     t54 = call sign(int), 1
    225     param "%d %d %d %d\n"
    226     param t52
    227     param t53
    228     param t54
    229     param 1
    230     call printf, 5
    231     flags = 0
    232     flags = 8
    233     flags = 9
    234     flags = 8
    235     flags = 16
    236     param "%d %d\n"
    237     param 16
    238     param 1
    239     call printf, 3
    240     c = 65
    241     c = 97
    242     param "%c %c %d\n"
    243     param 97
    244     param 65
    245     param 25
    246     call printf, 4
    247     param 255
    248     t73 = call popcount(unsigned int), 1
    249     return t73


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
