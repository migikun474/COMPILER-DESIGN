============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t20_bits.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 237 -> 113 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          237 -> 113   (52% fewer)

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
   loops unrolled                          7
   unreachable functions removed           6

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

 Code: 113 instruction(s)

    100       t74 = 4042265140
    101       t75 = 0
    102  L1:  if t74 uint== 0 goto L2
    103       t76 = t74 uint& 1
    104       t77 = t75 uint+ t76
    105       t75 = t77
    106       t74 = t74 uint>> 1
    107       if t74 uint== 0 goto L2
    108       t76 = t74 uint& 1
    109       t77 = t75 uint+ t76
    110       t75 = t77
    111       t74 = t74 uint>> 1
    112       goto L1
    113  L2:  t78 = 4042265140
    114       t79 = 0
    115       t80 = 0
    116  L3:  if t80 int>= 32 goto L4
    117       t81 = t79 uint<< 1
    118       t82 = t78 uint& 1
    119       t79 = t81 uint| t82
    120       t78 = t78 uint>> 1
    121       t80 = t80 int+ 1
    122       if t80 int>= 32 goto L4
    123       t81 = t79 uint<< 1
    124       t82 = t78 uint& 1
    125       t79 = t81 uint| t82
    126       t78 = t78 uint>> 1
    127       t80 = t80 int+ 1
    128       goto L3
    129  L4:  t91 = 1000
    130       t92 = -1
    131  L5:  if t91 uint== 0 goto L6
    132       t91 = t91 uint>> 1
    133       t92 = t92 int+ 1
    134       if t91 uint== 0 goto L6
    135       t91 = t91 uint>> 1
    136       t92 = t92 int+ 1
    137       goto L5
    138  L6:  param "%d %x %d %d %d\n"
    139       param t75
    140       param t79
    141       param 1
    142       param 0
    143       param t92
    144       call printf, 6
    145       param "%x %x %x %x\n"
    146       param 4660
    147       param 4042265151
    148       param 252702155
    149       param 252702155
    150       call printf, 5
    151       param "%x %x %x\n"
    152       param 4027725040
    153       param 251732800
    154       param 15
    155       call printf, 4
    156       param "%d %d %u %u\n"
    157       param 2147483647
    158       param -2147483648
    159       param 1
    160       param 2147483648
    161       call printf, 5
    162       param "%d %d %d %d\n"
    163       param -1
    164       param -1
    165       param 1
    166       param 1073741824
    167       call printf, 5
    168       param "%d %d %d %d\n"
    169       param 0
    170       param -128
    171       param 32767
    172       param 0
    173       call printf, 5
    174       param "%d %d %d\n"
    175       param -3
    176       param -1
    177       param -3
    178       call printf, 4
    179       param "%d %d %d\n"
    180       param 0
    181       param 1
    182       param 1
    183       call printf, 4
    184       param "%d %d %d %d\n"
    185       param -1
    186       param 0
    187       param 1
    188       param 1
    189       call printf, 5
    190       param "%d %d\n"
    191       param 16
    192       param 1
    193       call printf, 3
    194       param "%c %c %d\n"
    195       param 97
    196       param 65
    197       param 25
    198       call printf, 4
    199       t111 = 255
    200       t112 = 0
    201  L7:  if t111 uint== 0 goto L8
    202       t113 = t111 uint& 1
    203       t114 = t112 uint+ t113
    204       t112 = t114
    205       t111 = t111 uint>> 1
    206       if t111 uint== 0 goto L8
    207       t113 = t111 uint& 1
    208       t114 = t112 uint+ t113
    209       t112 = t114
    210       t111 = t111 uint>> 1
    211       goto L7
    212  L8:  return t112


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   popcount           function      int (unsigned int)         -           3    -    2  _Z8popcountj; defined
   reverseBits        function      unsigned int (unsigned int) -           5    -    1  _Z11reverseBitsj; defined
   isPowerOfTwo       function      int (unsigned int)         -          11    -    2  _Z12isPowerOfTwoj; defined
   highestBit         function      int (unsigned int)         -          12    -    1  _Z10highestBitj; defined
   rotl               function      unsigned int (unsigned int, int) -          13    -    1  _Z4rotlji; defined
   sign               function      int (int)                  -          14    -    3  _Z4signi; defined
   main               function      int (void)                 -          16    -    0  defined

 scope: global > popcount()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param       3    4    3  v.1
   n                  variable      int                        local       3    4    2  n.2

 scope: global > reverseBits()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param       5    4    2  v.3
   r                  variable      unsigned int               local       6    4    3  r.4

 scope: global > reverseBits() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       7    4    2  i.5

 scope: global > isPowerOfTwo()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param      11    4    3  v.6

 scope: global > highestBit()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param      12    4    2  v.7
   n                  variable      int                        local      12    4    2  n.8

 scope: global > rotl()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     unsigned int               param      13    4    2  v.9
   k                  parameter     int                        param      13    4    2  k.10

 scope: global > sign()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     int                        param      14    4    2  v.11

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   u                  variable      unsigned int               local      17    4    9  u.12
   big                variable      int                        local      22    4    1  big.13
   small              variable      int                        local      22    4    3  small.14
   wrap               variable      unsigned int               local      23    4    3  wrap.15
   uc                 variable      unsigned char              local      28    1    2  uc.16
   sc                 variable      char                       local      29    1    2  sc.17
   sh                 variable      short                      local      30    2    2  sh.18
   us                 variable      unsigned short             local      31    2    2  us.19
   flags              variable      int                        local      38    4    6  flags.20
   c                  variable      char                       local      44    1    3  c.21

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
