============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 352 -> 283 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          352 -> 283   (19% fewer)

   constants folded                        3
   algebraic simplifications               2
   common subexpressions                  82
   copies / constants forwarded          222
   temporaries merged away                 5
   dead instructions removed             173
   jumps removed or redirected             3
   unreachable instructions removed        3
   propagated across blocks                0
   dead assignments removed                3
   calls inlined                          44
   tail calls turned into jumps            0
   common subexpressions across blocks      0
   loops unrolled                          0
   unreachable functions removed          11

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Shape::live      int                             4  0

 As three address code (initial values, in place before main runs):

    Shape::live = 0

============================================================================
 FUNCTION Shape::Shape()        (link name _ZN5ShapeC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0
   t1               temp    int                             4       4
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    100     t1 = Shape::live int+ 1
    101     Shape::live = t1
    102     *this = t1
    103     param "Shape %d\n"
    104     param t1
    105     call printf, 2
    106     return

============================================================================
 FUNCTION Shape::area()        (link name _ZN5Shape4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    107     return 0

============================================================================
 FUNCTION Shape::name()        (link name _ZN5Shape4nameEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Shape *                   4       0

 Code: 1 instruction(s)

    108     return 83

============================================================================
 FUNCTION Rect::set(int, int)        (link name _ZN4Rect3setEii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Rect *                    4      12
   t2               temp    class Rect *                    4      16

 Code: 5 instruction(s)

    109     t1 = this ptr+ 4
    110     *t1 = a
    111     t2 = this ptr+ 8
    112     *t2 = b
    113     return

============================================================================
 FUNCTION Rect::area()        (link name _ZN4Rect4areaEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Rect *                    4       0
   t1               temp    class Rect *                    4       4
   t2               temp    int                             4       8
   t3               temp    class Rect *                    4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20

 Code: 6 instruction(s)

    114     t1 = this ptr+ 4
    115     t2 = *t1
    116     t3 = this ptr+ 8
    117     t4 = *t3
    118     t5 = t2 int* t4
    119     return t5

============================================================================
 FUNCTION Point::Point()        (link name _ZN5PointC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   t1               temp    class Point *                   4       4

 Code: 4 instruction(s)

    120     *this = 0
    121     t1 = this ptr+ 4
    122     *t1 = 0
    123     return

============================================================================
 FUNCTION Point::operator-(const class Point &)        (link name _ZN5PointmiERKS_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 10 temporaries, frame 60 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   r                local   class Point                     8       8
   t1               temp    class Point *                   4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    class Point *                   4      32
   t6               temp    int                             4      36
   t7               temp    const class Point *             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48
   t11              temp    class Point *                   4      56
   (1 temporary no longer used after optimization not shown)

 Code: 15 instruction(s)

    124     t1 = &r
    125     *t1 = 0
    126     t11 = t1 ptr+ 4
    127     *t11 = 0
    128     t2 = *this
    129     t3 = *o
    130     t4 = t2 int- t3
    131     r[0] = t4
    132     t5 = this ptr+ 4
    133     t6 = *t5
    134     t7 = o ptr+ 4
    135     t8 = *t7
    136     t9 = t6 int- t8
    137     r[4] = t9
    138     return r

============================================================================
 FUNCTION Point::operator<(const class Point &)        (link name _ZN5PointltERKS_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 14 temporaries, frame 88 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Point *                   4       0
   o                param   const class Point &             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t4               temp    int                             4      20
   t5               temp    class Point *                   4      24
   t6               temp    int                             4      28
   t9               temp    int                             4      40
   t10              temp    int                             4      44
   t11              temp    int                             4      48
   t13              temp    int                             4      56
   t14              temp    const class Point *             4      60
   t15              temp    int                             4      64
   t18              temp    int                             4      76
   t19              temp    int                             4      80
   t20              temp    bool                            1      84
   (6 temporaries no longer used after optimization not shown)

 Code: 21 instruction(s)

    139       t2 = *this
    140       t4 = t2 int* t2
    141       t5 = this ptr+ 4
    142       t6 = *t5
    143       t9 = t6 int* t6
    144       t10 = t4 int+ t9
    145       t11 = *o
    146       t13 = t11 int* t11
    147       t14 = o ptr+ 4
    148       t15 = *t14
    149       t18 = t15 int* t15
    150       t19 = t13 int+ t18
    151       if t10 int< t19 goto L1
    152       t1 = 0
    153       goto L2
    154  L1:  t1 = 1
    155  L2:  if t1 int!= 0 goto L3
    156       t20 = 0
    157       goto L4
    158  L3:  t20 = 1
    159  L4:  return t20

============================================================================
 FUNCTION at(int, int)        (link name _Z2atii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   p                local   class Point                     8       8
   t1               temp    class Point *                   4      16
   t3               temp    class Point *                   4      24
   (1 temporary no longer used after optimization not shown)

 Code: 7 instruction(s)

    160     t1 = &p
    161     *t1 = 0
    162     t3 = t1 ptr+ 4
    163     *t3 = 0
    164     p[0] = a
    165     p[4] = b
    166     return p

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 104 temporaries, frame 1144 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   r                local   class Rect                     12       0
   q                local   class Square                   12      12
   asShape          local   class Shape *                   4      24
   alias            local   class Rect &                    4      28
   pair             local   class Rect[2]                  24      32
   a                local   class Point                     8      56
   b                local   class Point                     8      64
   c                local   class Point                     8      72
   s                local   class Segment                  16      80
   last             local   class Rect                     12      96
   base             local   class Shape *                   4     108
   t1               temp    class Rect *                    4     112
   t3               temp    class Square *                  4     120
   t25              temp    class Rect (*)[2]               4     208
   t26              temp    class Rect (*)[2]               4     212
   t32              temp    int                             4     236
   t33              temp    int                             4     240
   t36              temp    class Point *                   4     260
   t37              temp    class Point *                   4     264
   t49              temp    int                             4     312
   t53              temp    int                             4     332
   t54              temp    int                             4     336
   t55              temp    int                             4     340
   t56              temp    int                             4     344
   t59              temp    bool                            1     356
   t60              temp    int                             4     360
   t63              temp    bool                            1     372
   t64              temp    int                             4     376
   t65              temp    class Segment *                 4     380
   t66              temp    class Segment *                 4     384
   t70              temp    int                             4     400
   t71              temp    class Rect *                    4     404
   t77              temp    int                             4     428
   t79              temp    class Rect *                    4     436
   t80              temp    class Rect *                    4     440
   t87              temp    class Rect *                    4     468
   t88              temp    class Rect *                    4     472
   t93              temp    int                             4     492
   t95              temp    int                             4     500
   t96              temp    int                             4     504
   t99              temp    int                             4     516
   t101             temp    int                             4     524
   t102             temp    int                             4     528
   t108             temp    int                             4     552
   t109             temp    int                             4     556
   t111             temp    int                             4     564
   t112             temp    int                             4     568
   t113             temp    int                             4     572
   t115             temp    int                             4     580
   t116             temp    int                             4     584
   t117             temp    int                             4     588
   t123             temp    int                             4     612
   t124             temp    int                             4     616
   t126             temp    int                             4     624
   t127             temp    int                             4     628
   t132             temp    int                             4     648
   t133             temp    int                             4     652
   t139             temp    int                             4     676
   t140             temp    int                             4     680
   t142             temp    class Rect *                    4     688
   t143             temp    class Rect *                    4     692
   t145             temp    class Rect *                    4     700
   t146             temp    class Rect *                    4     704
   t149             temp    int                             4     716
   t151             temp    int                             4     724
   t152             temp    int                             4     728
   t155             temp    int                             4     740
   t157             temp    int                             4     748
   t158             temp    int                             4     752
   t161             temp    class Point                     8     764
   t162             temp    class Point *                   4     772
   t165             temp    class Point                     8     784
   t166             temp    class Point *                   4     792
   t169             temp    int                             4     804
   t170             temp    int                             4     808
   t171             temp    int                             4     812
   t172             temp    class Point *                   4     816
   t173             temp    int                             4     820
   t174             temp    const class Point *             4     824
   t175             temp    int                             4     828
   t176             temp    int                             4     832
   t179             temp    int                             4     844
   t180             temp    int                             4     848
   t181             temp    int                             4     852
   t183             temp    int                             4     860
   t185             temp    int                             4     868
   t186             temp    int                             4     872
   t189             temp    int                             4     884
   t190             temp    int                             4     888
   t191             temp    int                             4     892
   t193             temp    int                             4     900
   t195             temp    int                             4     908
   t196             temp    int                             4     912
   t205             temp    class Point                     8     948
   t206             temp    class Point *                   4     956
   t207             temp    int                             4     960
   t208             temp    int                             4     964
   t209             temp    int                             4     968
   t211             temp    int                             4     976
   t213             temp    int                             4     984
   t214             temp    int                             4     988
   t216             temp    class Point *                   4     996
   t218             temp    class Point *                   4    1004
   t224             temp    class Point                     8    1028
   t225             temp    class Point                     8    1036
   t229             temp    class Point                     8    1056
   t230             temp    int                             4    1064
   t231             temp    int                             4    1068
   t232             temp    int                             4    1072
   t233             temp    int                             4    1076
   t234             temp    int                             4    1080
   t236             temp    class Rect *                    4    1088
   t237             temp    class Rect *                    4    1092
   t245             temp    int                             4    1124
   t248             temp    int                             4    1136
   (145 temporaries no longer used after optimization not shown)

 Code: 216 instruction(s)

    167     t1 = &r
    168     param t1                            (this)
    169     call Shape::Shape(), 1
    170     t79 = t1 ptr+ 4
    171     *t79 = 1
    172     t80 = t1 ptr+ 8
    173     *t80 = 1
    174     *t79 = 3
    175     *t80 = 4
    176     t3 = &q
    177     param t3                            (this)
    178     call Shape::Shape(), 1
    179     t87 = t3 ptr+ 4
    180     *t87 = 1
    181     t88 = t3 ptr+ 8
    182     *t88 = 1
    183     param t3                            (this)
    184     param 5
    185     param 5
    186     call Rect::set(int, int), 3
    187     t93 = *t79
    188     t95 = *t80
    189     t96 = t93 int* t95
    190     t99 = *t87
    191     t101 = *t88
    192     t102 = t99 int* t101
    193     t108 = t99 int+ t101
    194     t109 = t108 int<< 1
    195     param "%d %d %d %d\n"
    196     param t96
    197     param t102
    198     param t109
    199     param Shape::live
    200     call printf, 5
    201     param t1                            (this)
    202     t111 = call Rect::area(), 1
    203     t112 = *t1
    204     t113 = t111 int+ t112
    205     param t3                            (this)
    206     t115 = call Shape::area(), 1
    207     param t3                            (this)
    208     t116 = call Shape::name(), 1
    209     t117 = t115 int+ t116
    210     param "%d %d %c %c\n"
    211     param t113
    212     param t117
    213     param 81
    214     param 83
    215     call printf, 5
    216     t123 = *t87
    217     t124 = t123 int+ 1
    218     *t87 = t124
    219     t126 = *t88
    220     t127 = t126 int+ 1
    221     *t88 = t127
    222     *t87 = 10
    223     t132 = *t88
    224     t133 = t132 int* 10
    225     t139 = 10 int+ t132
    226     t140 = t139 int<< 1
    227     param "%d %d\n"
    228     param t133
    229     param t140
    230     call printf, 3
    231     t25 = &pair
    232     param t25                           (this)
    233     call Shape::Shape(), 1
    234     t142 = t25 ptr+ 4
    235     *t142 = 1
    236     t143 = t25 ptr+ 8
    237     *t143 = 1
    238     t26 = t25 ptr+ 12
    239     param t26                           (this)
    240     call Shape::Shape(), 1
    241     t145 = t26 ptr+ 4
    242     *t145 = 1
    243     t146 = t26 ptr+ 8
    244     *t146 = 1
    245     pair[16] = 6
    246     t149 = *t142
    247     t151 = *t143
    248     t152 = t149 int* t151
    249     t155 = *t145
    250     t157 = *t146
    251     t158 = t155 int* t157
    252     t32 = t152 int+ t158
    253     t33 = pair[12]
    254     param "%d %d %d\n"
    255     param t32
    256     param t33
    257     param Shape::live
    258     call printf, 4
    259     param "%d\n"
    260     param Shape::live
    261     call printf, 2
    262     t162 = &t161
    263     param t162                          (this)
    264     call Point::Point(), 1
    265     t161[0] = 3
    266     t161[4] = 4
    267     a = t161
    268     t166 = &t165
    269     param t166                          (this)
    270     call Point::Point(), 1
    271     t165[0] = 1
    272     t165[4] = 1
    273     b = t165
    274     t36 = &a
    275     t37 = &b
    276     t169 = *t36
    277     t170 = *t37
    278     t171 = t169 int+ t170
    279     *t36 = t171
    280     t172 = t36 ptr+ 4
    281     t173 = *t172
    282     t174 = t37 ptr+ 4
    283     t175 = *t174
    284     t176 = t173 int+ t175
    285     *t172 = t176
    286     t179 = *t36
    287     t180 = *t37
    288     t181 = t179 int+ t180
    289     *t36 = t181
    290     t183 = *t172
    291     t185 = *t174
    292     t186 = t183 int+ t185
    293     *t172 = t186
    294     t189 = *t36
    295     t190 = *t37
    296     t191 = t189 int+ t190
    297     *t36 = t191
    298     t193 = *t172
    299     t195 = *t174
    300     t196 = t193 int+ t195
    301     *t172 = t196
    302     t49 = t196 int<< 1
    303     *t36 = t49
    304     t206 = &t205
    305     param t206                          (this)
    306     call Point::Point(), 1
    307     t207 = *t36
    308     t208 = *t37
    309     t209 = t207 int- t208
    310     t205[0] = t209
    311     t211 = *t172
    312     t213 = *t174
    313     t214 = t211 int- t213
    314     t205[4] = t214
    315     c = t205
    316     t53 = a[0]
    317     t54 = a[4]
    318     t55 = c[0]
    319     t56 = c[4]
    320     param t37                           (this)
    321     param t36
    322     t59 = call Point::operator<(const class Point &), 2
    323     t60 = booltoint t59
    324     param t36                           (this)
    325     param t37
    326     t63 = call Point::operator<(const class Point &), 2
    327     t64 = booltoint t63
    328     param "%d %d %d %d %d %d\n"
    329     param t53
    330     param t54
    331     param t55
    332     param t56
    333     param t60
    334     param t64
    335     call printf, 7
    336     t65 = &s
    337     *t65 = 0
    338     t216 = t65 ptr+ 4
    339     *t216 = 0
    340     t66 = t65 ptr+ 8
    341     *t66 = 0
    342     t218 = t66 ptr+ 4
    343     *t218 = 0
    344     param 1
    345     param 2
    346     t224 = call at(int, int), 2
    347     *t65 = t224
    348     param 4
    349     param 6
    350     t225 = call at(int, int), 2
    351     *t66 = t225
    352     param t66                           (this)
    353     param t65
    354     t229 = call Point::operator-(const class Point &), 2
    355     t230 = t229[0]
    356     t231 = t230 int* t230
    357     t232 = t229[4]
    358     t233 = t232 int* t232
    359     t234 = t231 int+ t233
    360     t70 = s[12]
    361     param "%d %d\n"
    362     param t234
    363     param t70
    364     call printf, 3
    365     t71 = &last
    366     param t71                           (this)
    367     call Shape::Shape(), 1
    368     t236 = t71 ptr+ 4
    369     *t236 = 1
    370     t237 = t71 ptr+ 8
    371     *t237 = 1
    372     *t236 = 2
    373     *t237 = 9
    374     t245 = *t236
    375     t248 = t245 int* 9
    376     t77 = *t71
    377     param "%d %d %d\n"
    378     param t248
    379     param 0
    380     param t77
    381     call printf, 4
    382     return Shape::live


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Shape              class_tag     class Shape                -           5    -    0  size 4
   Rect               class_tag     class Rect                 -          15    -    0  size 12, public base Shape
   Square             class_tag     class Square               -          24    -    0  size 12, public base Rect
   Point              class_tag     class Point                -          30    -    0  size 8
   at                 function      class Point (int, int)     -          39    -    4  _Z2atii; defined
   Segment            class_tag     class Segment              -          41    -    0  size 16
   total              function      int (class Rect &)         -          48    -    1  _Z5totalR4Rect; defined
   through            function      int (class Shape *)        -          49    -    1  _Z7throughP5Shape; defined
   grow               function      void (class Rect *, int)   -          50    -    1  _Z4growP4Recti; defined
   main               function      int (void)                 -          52    -    0  defined

 scope: global > class Shape
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      7    4    5  Shape::id; public, offset 0
   live               field         int                        static      8    4    5  Shape::live; public, static
   Shape              constructor   void (void)                -           9    -    0  _ZN5ShapeC1Ev; public
   area               method        int (void)                 -          10    -    2  _ZN5Shape4areaEv; public, defined
   name               method        int (void)                 -          11    -    2  _ZN5Shape4nameEv; public, defined

 scope: global > class Rect
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   w                  field         int                        member     17    4    7  Rect::w; public, offset 4
   h                  field         int                        member     17    4    5  Rect::h; public, offset 8
   Rect               constructor   void (void)                -          18    -    3  _ZN4RectC1Ev; public
   set                method        void (int, int)            -          19    -    3  _ZN4Rect3setEii; public, defined
   area               method        int (void)                 -          20    -    7  _ZN4Rect4areaEv; public, defined
   perimeter          method        int (void)                 -          21    -    2  _ZN4Rect9perimeterEv; public, defined

 scope: global > class Rect > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      19    4    1  a.1
   b                  parameter     int                        param      19    4    1  b.2

 scope: global > class Square
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   side               method        void (int)                 -          26    -    1  _ZN6Square4sideEi; public, defined
   name               method        int (void)                 -          27    -    1  _ZN6Square4nameEv; public, defined

 scope: global > class Square > side()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     int                        param      26    4    2  s.3

 scope: global > class Point
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     32    4   16  Point::x; public, offset 0
   y                  field         int                        member     32    4   17  Point::y; public, offset 4
   Point              constructor   void (void)                -          33    -    2  _ZN5PointC1Ev; public
   operator+=         method        class Point &(const class Point &) -          34    -    3  _ZN5PointpLERKS_; public, defined
   operator-          method        class Point (const class Point &) -          35    -    2  _ZN5PointmiERKS_; public, defined
   operator<          method        bool (const class Point &) -          36    -    2  _ZN5PointltERKS_; public, defined
   operator[]         method        int &(int)                 -          37    -    2  _ZN5PointixEi; public, defined

 scope: global > class Point > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      34    4    2  o.4

 scope: global > class Point > operator-()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      35    4    2  o.5
   r                  variable      class Point                local      35    8    3  r.6

 scope: global > class Point > operator<()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     const class Point &        param      36    4    4  o.7

 scope: global > class Point > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      37    4    1  i.8

 scope: global > at()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      39    4    1  a.9
   b                  parameter     int                        param      39    4    1  b.10
   p                  variable      class Point                local      39    8    3  p.11

 scope: global > class Segment
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   from               field         class Point                member     43    8    2  Segment::from; public, offset 0
   to                 field         class Point                member     43    8    3  Segment::to; public, offset 8
   set                method        void (int, int, int, int)  -          44    -    1  _ZN7Segment3setEiiii; public, defined
   length2            method        int (void)                 -          45    -    1  _ZN7Segment7length2Ev; public, defined

 scope: global > class Segment > set()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      44    4    1  a.12
   b                  parameter     int                        param      44    4    1  b.13
   c                  parameter     int                        param      44    4    1  c.14
   d                  parameter     int                        param      44    4    1  d.15

 scope: global > class Segment > length2()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      class Point                local      45    8    4  d.16

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect &               param      48    4    2  r.17

 scope: global > through()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  parameter     class Shape *              param      49    4    2  s.18

 scope: global > grow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  parameter     class Rect *               param      50    4    2  r.19
   by                 parameter     int                        param      50    4    2  by.20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Rect                 local      53   12    3  r.21
   q                  variable      class Square               local      55   12    9  q.22
   asShape            variable      class Shape *              local      58    4    1  asShape.23
   alias              variable      class Rect &               local      61    4    2  alias.24
   a                  variable      class Point                local      71    8    9  a.26
   b                  variable      class Point                local      71    8    6  b.27
   c                  variable      class Point                local      75    8    2  c.28
   s                  variable      class Segment              local      77   16    3  s.29

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pair               variable      class Rect[2]              local      65   24    4  pair.25
   last               variable      class Rect                 local      82   12    3  last.30
   base               variable      class Shape *              local      84    4    2  base.31

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Shape: size 4, align 4
    +0  int id  [public]
    static  int live  [public]
class Rect: size 12, align 4
    (base Shape, public)
    +4  int w  [public]
    +8  int h  [public]
class Square: size 12, align 4
    (base Rect, public)
class Point: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
class Segment: size 16, align 4
    +0  class Point from  [public]
    +8  class Point to  [public]
