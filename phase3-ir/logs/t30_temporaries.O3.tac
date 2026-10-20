============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t30_temporaries.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 522 -> 544 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          522 -> 544   (-4% fewer)

   constants folded                        3
   algebraic simplifications               0
   common subexpressions                  55
   copies / constants forwarded          218
   temporaries merged away                11
   dead instructions removed             193
   jumps removed or redirected             6
   unreachable instructions removed        0
   propagated across blocks                2
   dead assignments removed               14
   calls inlined                          85
   tail calls turned into jumps            0
   common subexpressions across blocks      6
   instructions moved out of loops         3

============================================================================
 FUNCTION Tag::Tag(int)        (link name _ZN3TagC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   n                param   int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    100     *this = n
    101     param "+%d "
    102     param n
    103     call printf, 2
    104     return

============================================================================
 FUNCTION Tag::~Tag()        (link name _ZN3TagD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    105     t1 = *this
    106     param "-%d "
    107     param t1
    108     call printf, 2
    109     return

============================================================================
 FUNCTION Tag::value()        (link name _ZN3Tag5valueEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 3 instruction(s)

    110     t1 = *this
    111     t2 = t1 int* 10
    112     return t2

============================================================================
 FUNCTION Tag::operator+(const class Tag &)        (link name _ZN3TagplERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0
   o                param   const class Tag &               4       4
   t1               temp    class Tag                       4       8
   t2               temp    class Tag *                     4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    113     t2 = &t1
    114     t3 = *this
    115     t4 = *o
    116     t5 = t3 int+ t4
    117     *t2 = t5
    118     param "+%d "
    119     param t5
    120     call printf, 2
    121     return t1

============================================================================
 FUNCTION Copy::Copy(int)        (link name _ZN4CopyC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Copy *                    4       0
   n                param   int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    122     *this = n
    123     param "+c%d "
    124     param n
    125     call printf, 2
    126     return

============================================================================
 FUNCTION Copy::Copy(const class Copy &)        (link name _ZN4CopyC1ERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Copy *                    4       0
   o                param   const class Copy &              4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    127     t1 = *o
    128     t2 = t1 int+ 100
    129     *this = t2
    130     param "copy%d "
    131     param t2
    132     call printf, 2
    133     return

============================================================================
 FUNCTION Copy::~Copy()        (link name _ZN4CopyD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Copy *                    4       0
   t1               temp    int                             4       4

 Code: 5 instruction(s)

    134     t1 = *this
    135     param "-c%d "
    136     param t1
    137     call printf, 2
    138     return

============================================================================
 FUNCTION make(int)        (link name _Z4makei)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    class Tag                       4       4
   t2               temp    class Tag *                     4       8
   (2 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    139     t2 = &t1
    140     *t2 = n
    141     param "+%d "
    142     param n
    143     call printf, 2
    144     return t1

============================================================================
 FUNCTION named(int)        (link name _Z5namedi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t                local   class Tag                       4       4
   t1               temp    class Tag *                     4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    145     t1 = &t
    146     *t1 = n
    147     param "+%d "
    148     param n
    149     call printf, 2
    150     t2 = t[0]
    151     t3 = t2 int+ 1
    152     t[0] = t3
    153     return t

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 8 temporaries, frame 92 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   which            param   int                             4       0
   a                local   class Tag                       4       4
   b                local   class Tag                       4       8
   t1               temp    class Tag *                     4      12
   t2               temp    class Tag *                     4      16
   t3               temp    class Tag                       4      20
   t6               temp    class Tag                       4      32
   t14              temp    int                             4      64
   t16              temp    int                             4      72
   t18              temp    int                             4      80
   t20              temp    int                             4      88
   (12 temporaries no longer used after optimization not shown)

 Code: 31 instruction(s)

    154       t1 = &a
    155       *t1 = 40
    156       param "+%d "
    157       param 40
    158       call printf, 2
    159       t2 = &b
    160       *t2 = 41
    161       param "+%d "
    162       param 41
    163       call printf, 2
    164       if which int== 0 goto L1
    165       t3 = a
    166       t14 = *t2
    167       param "-%d "
    168       param t14
    169       call printf, 2
    170       t16 = *t1
    171       param "-%d "
    172       param t16
    173       call printf, 2
    174       return t3
    175  L1:  t6 = b
    176       t18 = *t2
    177       param "-%d "
    178       param t18
    179       call printf, 2
    180       t20 = *t1
    181       param "-%d "
    182       param t20
    183       call printf, 2
    184       return t6

============================================================================
 FUNCTION byValue(class Tag)        (link name _Z7byValue3Tag)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   class Tag                       4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    185     t1 = t[0]
    186     return t1

============================================================================
 FUNCTION byRef(const class Tag &)        (link name _Z5byRefRK3Tag)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t                param   const class Tag &               4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    187     t1 = *t
    188     return t1

============================================================================
 FUNCTION copied(class Copy)        (link name _Z6copied4Copy)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Copy                      4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    189     t1 = c[0]
    190     return t1

============================================================================
 FUNCTION makeCopy(int)        (link name _Z8makeCopyi)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   t1               temp    class Copy                      4       4
   t2               temp    class Copy *                    4       8
   (2 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    191     t2 = &t1
    192     *t2 = n
    193     param "+c%d "
    194     param n
    195     call printf, 2
    196     return t1

============================================================================
 FUNCTION sameCopy(class Copy)        (link name _Z8sameCopy4Copy)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 32 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   c                param   class Copy                      4       0
   t1               temp    class Copy                      4       4
   t2               temp    class Copy *                    4       8
   t3               temp    class Copy *                    4      12
   t6               temp    int                             4      24
   t7               temp    int                             4      28
   (2 temporaries no longer used after optimization not shown)

 Code: 9 instruction(s)

    197     t2 = &t1
    198     t3 = &c
    199     t6 = *t3
    200     t7 = t6 int+ 100
    201     *t2 = t7
    202     param "copy%d "
    203     param t7
    204     call printf, 2
    205     return t1

============================================================================
 FUNCTION Shape::sides()        (link name _ZN5Shape5sidesEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    206     return 0

============================================================================
 FUNCTION Shape::kind()        (link name _ZN5Shape4kindEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    207     return 1

============================================================================
 FUNCTION Square::sides()        (link name _ZN6Square5sidesEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    208     return 4

============================================================================
 FUNCTION Square::kind()        (link name _ZN6Square4kindEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Square *                  4       0

 Code: 1 instruction(s)

    209     return 2

============================================================================
 FUNCTION mix(long long, long long, int)        (link name _Z3mixxxi)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 9 temporaries, frame 136 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   long long                       8       0
   b                param   long long                       8       8
   n                param   int                             4      16
   sum              local   long long                       8      24
   i                local   int                             4      32
   t1               temp    long long                       8      40
   t2               temp    long long                       8      48
   t3               temp    long long                       8      56
   t4               temp    long long                       8      64
   t5               temp    long long                       8      72
   t7               temp    long long                       8      88
   t8               temp    long long                       8      96
   t11              temp    long long                       8     120
   t12              temp    long long                       8     128
   (3 temporaries no longer used after optimization not shown)

 Code: 18 instruction(s)

    210       sum = 0
    211       i = 0
    212  L2:  if i int>= n goto L3
    213       t1 = inttollong i
    214       t2 = a llong* t1
    215       t3 = sum llong+ t2
    216       t4 = b llong^ sum
    217       t5 = t3 llong- t4
    218       sum = t5
    219       a = a llong+ 4294967296
    220       t7 = llong- b
    221       t8 = t5 llong& 65535
    222       b = t7 llong+ t8
    223       i = i int+ 1
    224       goto L2
    225  L3:  t11 = sum llong+ a
    226       t12 = t11 llong- b
    227       return t12

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 13 parameter(s)/local(s), 150 temporaries, frame 1392 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                local   int                             4       0
   kept             local   class Tag                       4       4
   sum              local   class Tag                       4       8
   i                local   int                             4      12
   n                local   class Tag                       4      16
   r                local   const class Tag &               4      20
   c                local   class Copy                      4      24
   d                local   class Copy                      4      28
   e                local   class Copy                      4      32
   q                local   class Square                    1      36
   p                local   class Shape *                   4      40
   m                local   long long                       8      48
   inner            local   class Tag                       4      56
   t1               temp    class Tag                       4      60
   t2               temp    class Tag *                     4      64
   t4               temp    class Tag                       4      72
   t5               temp    class Tag *                     4      76
   t7               temp    class Tag                       4      84
   t8               temp    class Tag *                     4      88
   t11              temp    class Tag                       4     100
   t12              temp    class Tag *                     4     104
   t15              temp    int                             4     116
   t20              temp    class Tag *                     4     136
   t22              temp    class Tag                       4     144
   t23              temp    class Tag *                     4     148
   t27              temp    class Tag *                     4     164
   t29              temp    int                             4     172
   t32              temp    class Tag                       4     184
   t33              temp    class Tag *                     4     188
   t36              temp    class Tag                       4     200
   t37              temp    class Tag *                     4     204
   t38              temp    int                             4     208
   t41              temp    class Tag                       4     220
   t42              temp    class Tag *                     4     224
   t45              temp    class Tag                       4     236
   t46              temp    class Tag *                     4     240
   t49              temp    class Tag                       4     252
   t50              temp    class Tag *                     4     256
   t54              temp    class Tag                       4     272
   t55              temp    class Tag *                     4     276
   t59              temp    int                             4     292
   t60              temp    class Tag                       4     296
   t61              temp    class Tag *                     4     300
   t62              temp    int                             4     304
   t64              temp    class Tag                       4     312
   t65              temp    class Tag *                     4     316
   t70              temp    int                             4     336
   t71              temp    class Tag                       4     340
   t72              temp    class Tag *                     4     344
   t75              temp    class Tag                       4     356
   t76              temp    class Tag *                     4     360
   t81              temp    class Tag *                     4     380
   t82              temp    int                             4     384
   t83              temp    class Tag                       4     388
   t84              temp    class Tag *                     4     392
   t85              temp    int                             4     396
   t87              temp    class Tag                       4     404
   t88              temp    class Tag *                     4     408
   t89              temp    int                             4     412
   t90              temp    int                             4     416
   t92              temp    class Tag                       4     424
   t93              temp    class Tag *                     4     428
   t95              temp    int                             4     436
   t96              temp    class Tag                       4     440
   t97              temp    class Tag *                     4     444
   t99              temp    int                             4     452
   t100             temp    class Copy *                    4     456
   t101             temp    class Copy                      4     460
   t102             temp    class Copy *                    4     464
   t106             temp    class Copy                      4     480
   t107             temp    class Copy *                    4     484
   t112             temp    class Copy *                    4     504
   t113             temp    int                             4     508
   t114             temp    class Copy                      4     512
   t115             temp    class Copy *                    4     516
   t119             temp    class Copy *                    4     532
   t121             temp    int                             4     540
   t133             temp    long long                       8     592
   t137             temp    long long                       8     624
   t138             temp    class Tag *                     4     632
   t141             temp    class Tag                       4     644
   t142             temp    class Tag *                     4     648
   t145             temp    int                             4     660
   t158             temp    int                             4     712
   t160             temp    class Tag                       4     720
   t161             temp    class Tag *                     4     724
   t163             temp    int                             4     732
   t167             temp    int                             4     748
   t168             temp    int                             4     752
   t170             temp    class Tag                       4     760
   t171             temp    class Tag *                     4     764
   t173             temp    int                             4     772
   t174             temp    int                             4     776
   t178             temp    int                             4     792
   t180             temp    class Tag                       4     800
   t181             temp    class Tag *                     4     804
   t186             temp    class Tag                       4     824
   t187             temp    class Tag *                     4     828
   t188             temp    int                             4     832
   t189             temp    int                             4     836
   t190             temp    int                             4     840
   t192             temp    int                             4     848
   t195             temp    class Tag                       4     860
   t196             temp    class Tag *                     4     864
   t197             temp    int                             4     868
   t198             temp    int                             4     872
   t199             temp    int                             4     876
   t202             temp    class Tag                       4     888
   t203             temp    class Tag *                     4     892
   t204             temp    int                             4     896
   t205             temp    int                             4     900
   t206             temp    int                             4     904
   t208             temp    int                             4     912
   t210             temp    int                             4     920
   t213             temp    class Tag                       4     932
   t214             temp    int                             4     936
   t216             temp    int                             4     944
   t217             temp    class Tag                       4     948
   t218             temp    int                             4     952
   t220             temp    int                             4     960
   t224             temp    int                             4     976
   t230             temp    int                             4    1000
   t234             temp    class Tag                       4    1016
   t235             temp    class Tag *                     4    1020
   t237             temp    int                             4    1028
   t241             temp    int                             4    1044
   t247             temp    int                             4    1068
   t251             temp    int                             4    1084
   t253             temp    class Tag                       4    1092
   t254             temp    class Tag *                     4    1096
   t255             temp    int                             4    1100
   t256             temp    int                             4    1104
   t258             temp    int                             4    1112
   t260             temp    int                             4    1120
   t266             temp    int                             4    1144
   t271             temp    int                             4    1164
   t272             temp    int                             4    1168
   t273             temp    class Copy                      4    1172
   t274             temp    int                             4    1176
   t276             temp    int                             4    1184
   t279             temp    class Copy                      4    1196
   t280             temp    int                             4    1200
   t282             temp    int                             4    1208
   t284             temp    class Copy                      4    1216
   t285             temp    class Copy *                    4    1220
   t288             temp    int                             4    1232
   t289             temp    int                             4    1236
   t290             temp    class Copy                      4    1240
   t291             temp    class Copy                      4    1244
   t292             temp    class Copy *                    4    1248
   t293             temp    class Copy *                    4    1252
   t295             temp    int                             4    1260
   t305             temp    int                             4    1300
   t309             temp    int                             4    1316
   t311             temp    int                             4    1324
   t313             temp    int                             4    1332
   t315             temp    int                             4    1340
   t317             temp    int                             4    1348
   t319             temp    int                             4    1356
   t321             temp    int                             4    1364
   t323             temp    int                             4    1372
   t325             temp    int                             4    1380
   t327             temp    int                             4    1388
   (177 temporaries no longer used after optimization not shown)

 Code: 416 instruction(s)

    228       t2 = &t1
    229       *t2 = 1
    230       param "+%d "
    231       param 1
    232       call printf, 2
    233       t158 = *t2
    234       param "-%d "
    235       param t158
    236       call printf, 2
    237       param "| "
    238       call printf, 1
    239       t161 = &t160
    240       param t161                          (this)
    241       param 2
    242       call Tag::Tag(int), 2
    243       t4 = t160
    244       t5 = &t4
    245       t163 = *t5
    246       param "-%d "
    247       param t163
    248       call printf, 2
    249       param "| "
    250       call printf, 1
    251       t8 = &t7
    252       *t8 = 3
    253       param "+%d "
    254       param 3
    255       call printf, 2
    256       t167 = *t8
    257       t168 = t167 int* 10
    258       t171 = &t170
    259       param t171                          (this)
    260       param 4
    261       call Tag::Tag(int), 2
    262       t11 = t170
    263       t12 = &t11
    264       t173 = *t12
    265       t174 = t173 int* 10
    266       t15 = t168 int+ t174
    267       param "-%d "
    268       param t173
    269       call printf, 2
    270       t178 = *t8
    271       param "-%d "
    272       param t178
    273       call printf, 2
    274       param "%d | "
    275       param t15
    276       call printf, 2
    277       t181 = &t180
    278       param t181                          (this)
    279       param 5
    280       call Tag::Tag(int), 2
    281       kept = t180
    282       t20 = &kept
    283       param "| "
    284       call printf, 1
    285       t23 = &t22
    286       *t23 = 6
    287       param "+%d "
    288       param 6
    289       call printf, 2
    290       t187 = &t186
    291       t188 = *t20
    292       t189 = *t23
    293       t190 = t188 int+ t189
    294       param t187                          (this)
    295       param t190
    296       call Tag::Tag(int), 2
    297       sum = t186
    298       t27 = &sum
    299       t192 = *t23
    300       param "-%d "
    301       param t192
    302       call printf, 2
    303       t29 = sum[0]
    304       param "%d | "
    305       param t29
    306       call printf, 2
    307       t196 = &t195
    308       t197 = *t20
    309       t198 = *t27
    310       t199 = t197 int+ t198
    311       param t196                          (this)
    312       param t199
    313       call Tag::Tag(int), 2
    314       t32 = t195
    315       t33 = &t32
    316       t203 = &t202
    317       t204 = *t33
    318       t205 = *t20
    319       t206 = t204 int+ t205
    320       param t203                          (this)
    321       param t206
    322       call Tag::Tag(int), 2
    323       t36 = t202
    324       t37 = &t36
    325       t38 = t36[0]
    326       t208 = *t37
    327       param "-%d "
    328       param t208
    329       call printf, 2
    330       t210 = *t33
    331       param "-%d "
    332       param t210
    333       call printf, 2
    334       param "%d | "
    335       param t38
    336       call printf, 2
    337       t42 = &t41
    338       *t42 = 10
    339       param "+%d "
    340       param 10
    341       call printf, 2
    342       t213 = t41
    343       t214 = t213[0]
    344       t216 = *t42
    345       param "-%d "
    346       param t216
    347       call printf, 2
    348       param "%d | "
    349       param t214
    350       call printf, 2
    351       t45 = kept
    352       t46 = &t45
    353       t217 = t45
    354       t218 = t217[0]
    355       t220 = *t46
    356       param "-%d "
    357       param t220
    358       call printf, 2
    359       param "%d | "
    360       param t218
    361       call printf, 2
    362       t50 = &t49
    363       *t50 = 11
    364       param "+%d "
    365       param 11
    366       call printf, 2
    367       t224 = *t50
    368       param "-%d "
    369       param t224
    370       call printf, 2
    371       param "%d | "
    372       param t224
    373       call printf, 2
    374       t55 = &t54
    375       *t55 = 12
    376       param "+%d "
    377       param 12
    378       call printf, 2
    379       t230 = *t55
    380       param "-%d "
    381       param t230
    382       call printf, 2
    383       if t230 int<= 5 goto L4
    384       param "if "
    385       call printf, 1
    386  L4:  param "| "
    387       call printf, 1
    388       i = 0
    389       t61 = &t60
    390       t65 = &t64
    391       t235 = &t234
    392  L5:  if i int>= 2 goto L6
    393       t59 = 13 int+ i
    394       param t235                          (this)
    395       param t59
    396       call Tag::Tag(int), 2
    397       t60 = t234
    398       t62 = t60[0]
    399       t237 = *t61
    400       param "-%d "
    401       param t237
    402       call printf, 2
    403       if t62 int<= 0 goto L6
    404       param "body "
    405       call printf, 1
    406       *t65 = 20
    407       param "+%d "
    408       param 20
    409       call printf, 2
    410       t241 = *t65
    411       i = i int+ t241
    412       param "-%d "
    413       param t241
    414       call printf, 2
    415       goto L5
    416  L6:  param "| "
    417       call printf, 1
    418       if t224 int<= 0 goto L7
    419       t72 = &t71
    420       *t72 = 21
    421       param "+%d "
    422       param 21
    423       call printf, 2
    424       t70 = t71[0]
    425       t247 = *t72
    426       param "-%d "
    427       param t247
    428       call printf, 2
    429       goto L8
    430  L7:  t76 = &t75
    431       *t76 = 22
    432       param "+%d "
    433       param 22
    434       call printf, 2
    435       t70 = t75[0]
    436       t251 = *t76
    437       param "-%d "
    438       param t251
    439       call printf, 2
    440  L8:  param "%d | "
    441       param t70
    442       call printf, 2
    443       t254 = &t253
    444       param t254                          (this)
    445       param 30
    446       call Tag::Tag(int), 2
    447       t255 = t253[0]
    448       t256 = t255 int+ 1
    449       t253[0] = t256
    450       n = t253
    451       t81 = &n
    452       t82 = n[0]
    453       param "%d | "
    454       param t82
    455       call printf, 2
    456       param 1
    457       t83 = call pick(int), 1
    458       t84 = &t83
    459       t85 = t83[0]
    460       t258 = *t84
    461       param "-%d "
    462       param t258
    463       call printf, 2
    464       param 0
    465       t87 = call pick(int), 1
    466       t88 = &t87
    467       t89 = t87[0]
    468       t90 = t85 int+ t89
    469       t260 = *t88
    470       param "-%d "
    471       param t260
    472       call printf, 2
    473       param "%d | "
    474       param t90
    475       call printf, 2
    476       t93 = &t92
    477       *t93 = 50
    478       param "+%d "
    479       param 50
    480       call printf, 2
    481       t95 = *t93
    482       param "%d | "
    483       param t95
    484       call printf, 2
    485       t97 = &t96
    486       *t97 = 60
    487       param "+%d "
    488       param 60
    489       call printf, 2
    490       kept = t96
    491       t266 = *t97
    492       param "-%d "
    493       param t266
    494       call printf, 2
    495       t99 = kept[0]
    496       param "%d\n"
    497       param t99
    498       call printf, 2
    499       t100 = &c
    500       *t100 = 1
    501       param "+c%d "
    502       param 1
    503       call printf, 2
    504       param "| "
    505       call printf, 1
    506       t102 = &t101
    507       t271 = *t100
    508       t272 = t271 int+ 100
    509       *t102 = t272
    510       param "copy%d "
    511       param t272
    512       call printf, 2
    513       t273 = t101
    514       t274 = t273[0]
    515       t276 = *t102
    516       param "-c%d "
    517       param t276
    518       call printf, 2
    519       param "%d | "
    520       param t274
    521       call printf, 2
    522       t107 = &t106
    523       *t107 = 2
    524       param "+c%d "
    525       param 2
    526       call printf, 2
    527       t279 = t106
    528       t280 = t279[0]
    529       t282 = *t107
    530       param "-c%d "
    531       param t282
    532       call printf, 2
    533       param "%d | "
    534       param t280
    535       call printf, 2
    536       t285 = &t284
    537       param t285                          (this)
    538       param 3
    539       call Copy::Copy(int), 2
    540       d = t284
    541       t112 = &d
    542       t113 = d[0]
    543       param "%d | "
    544       param t113
    545       call printf, 2
    546       t115 = &t114
    547       t288 = *t100
    548       t289 = t288 int+ 100
    549       *t115 = t289
    550       param "copy%d "
    551       param t289
    552       call printf, 2
    553       t290 = t114
    554       t292 = &t291
    555       t293 = &t290
    556       param t292                          (this)
    557       param t293
    558       call Copy::Copy(const class Copy &), 2
    559       e = t291
    560       t119 = &e
    561       t295 = *t115
    562       param "-c%d "
    563       param t295
    564       call printf, 2
    565       t121 = e[0]
    566       param "%d\n"
    567       param t121
    568       call printf, 2
    569       param "%d %d %d %d %d %d\n"
    570       param 4
    571       param 0
    572       param 0
    573       param 0
    574       param 2
    575       param 1
    576       call printf, 7
    577       param 3
    578       param 5
    579       param 20
    580       t133 = call mix(long long, long long, int), 3
    581       param -7
    582       param 1099511627776
    583       param 9
    584       t137 = call mix(long long, long long, int), 3
    585       param "%lld %lld\n"
    586       param t133
    587       param t137
    588       call printf, 3
    589       t138 = &inner
    590       *t138 = 70
    591       param "+%d "
    592       param 70
    593       call printf, 2
    594       t305 = *t138
    595       t142 = &t141
    596       *t142 = 71
    597       param "+%d "
    598       param 71
    599       call printf, 2
    600       t309 = *t142
    601       t145 = t305 int+ t309
    602       param "%d "
    603       param t145
    604       call printf, 2
    605       t311 = *t142
    606       param "-%d "
    607       param t311
    608       call printf, 2
    609       t313 = *t138
    610       param "-%d "
    611       param t313
    612       call printf, 2
    613       param "end\n"
    614       call printf, 1
    615       t315 = *t119
    616       param "-c%d "
    617       param t315
    618       call printf, 2
    619       t317 = *t112
    620       param "-c%d "
    621       param t317
    622       call printf, 2
    623       t319 = *t100
    624       param "-c%d "
    625       param t319
    626       call printf, 2
    627       t321 = *t93
    628       param "-%d "
    629       param t321
    630       call printf, 2
    631       t323 = *t81
    632       param "-%d "
    633       param t323
    634       call printf, 2
    635       t325 = *t27
    636       param "-%d "
    637       param t325
    638       call printf, 2
    639       t327 = *t20
    640       param "-%d "
    641       param t327
    642       call printf, 2
    643       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Tag                class_tag     class Tag                  -           7    -    0  size 4
   Copy               class_tag     class Copy                 -          16    -    0  size 4
   make               function      class Tag (int)            -          24    -    4  _Z4makei; defined
   named              function      class Tag (int)            -          25    -    1  _Z5namedi; defined
   pick               function      class Tag (int)            -          30    -    2  _Z4picki; defined
   byValue            function      int (class Tag)            -          36    -    2  _Z7byValue3Tag; defined
   byRef              function      int (const class Tag &)    -          37    -    5  _Z5byRefRK3Tag; defined
   copied             function      int (class Copy)           -          38    -    2  _Z6copied4Copy; defined
   makeCopy           function      class Copy (int)           -          39    -    1  _Z8makeCopyi; defined
   sameCopy           function      class Copy (class Copy)    -          40    -    1  _Z8sameCopy4Copy; defined
   Shape              class_tag     class Shape                -          42    -    0  size 1
   Square             class_tag     class Square               -          47    -    0  size 1, public base Shape
   mix                function      long long (long long, long long, int) -          53    -    2  _Z3mixxxi; defined
   main               function      int (void)                 -          63    -    0  defined

 scope: global > class Tag
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      9    4   20  Tag::id; public, offset 0
   Tag                constructor   void (int)                 -          10    -   18  _ZN3TagC1Ei; public
   ~Tag               destructor    void (void)                -          11    -    0  _ZN3TagD1Ev; public
   value              method        int (void)                 -          12    -    2  _ZN3Tag5valueEv; public, defined
   operator+          method        class Tag (const class Tag &) -          13    -    3  _ZN3TagplERKS_; public, defined

 scope: global > class Tag > Tag()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      10    4    1  n.1

 scope: global > class Tag > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Tag &          param      13    4    1  o.2

 scope: global > class Copy
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     18    4    9  Copy::id; public, offset 0
   Copy               constructor   void (int)                 -          19    -    3  _ZN4CopyC1Ei; public
   Copy               constructor   void (const class Copy &)  -          20    -    0  _ZN4CopyC1ERKS_; public
   ~Copy              destructor    void (void)                -          21    -    0  _ZN4CopyD1Ev; public

 scope: global > class Copy > Copy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      19    4    1  n.3
   o                  parameter     const class Copy &         param      20    4    1  o.4

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      24    4    1  n.5

 scope: global > named()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      25    4    1  n.6
   t                  variable      class Tag                  local      26    4    3  t.7

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   which              parameter     int                        param      30    4    1  which.8
   a                  variable      class Tag                  local      31    4    1  a.9
   b                  variable      class Tag                  local      32    4    1  b.10

 scope: global > byValue()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     class Tag                  param      36    4    1  t.11

 scope: global > byRef()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   t                  parameter     const class Tag &          param      37    4    1  t.12

 scope: global > copied()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Copy                 param      38    4    1  c.13

 scope: global > makeCopy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param      39    4    1  n.14

 scope: global > sameCopy()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   c                  parameter     class Copy                 param      40    4    1  c.15

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   sides              method        int (void)                 -          44    -    3  _ZN5Shape5sidesEv; public, defined
   kind               method        int (void)                 -          45    -    1  _ZN5Shape4kindEv; public, defined

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   sides              method        int (void)                 -          49    -    1  _ZN6Square5sidesEv; public, defined
   kind               method        int (void)                 -          50    -    1  _ZN6Square4kindEv; public, defined

 scope: global > mix()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     long long                  param      53    8    4  a.16
   b                  parameter     long long                  param      53    8    4  b.17
   n                  parameter     int                        param      53    4    1  n.18
   sum                variable      long long                  local      54    8    5  sum.19

 scope: global > mix() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      55    4    3  i.20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  variable      int                        local      68    4   20  v.21
   kept               variable      class Tag                  local      70    4    6  kept.22
   sum                variable      class Tag                  local      72    4    2  sum.23
   n                  variable      class Tag                  local      88    4    1  n.25
   r                  variable      const class Tag &          local      93    4    1  r.26
   c                  variable      class Copy                 local      98    4    2  c.27
   d                  variable      class Copy                 local     104    4    1  d.28
   e                  variable      class Copy                 local     106    4    1  e.29
   q                  variable      class Square               local     109    1    5  q.30
   p                  variable      class Shape *              local     110    4    2  p.31
   m                  variable      long long                  local     113    8    1  m.32

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      84    4    4  i.24

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   inner              variable      class Tag                  local     116    4    1  inner.33

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Tag: size 4, align 4
    +0  int id  [public]
class Copy: size 4, align 4
    +0  int id  [public]
class Shape: size 1, align 1
class Square: size 1, align 1
    (base Shape, public)
