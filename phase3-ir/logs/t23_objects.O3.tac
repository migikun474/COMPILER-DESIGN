============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t23_objects.c
   Optimization  : -O3: -O2 plus inlining and loop optimizations
   Result        : Optimized three address code (-O3): 356 -> 283 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O3)
----------------------------------------------------------------------------

   instructions                          356 -> 283   (20% fewer)

   constants folded                        3
   algebraic simplifications               2
   common subexpressions                  84
   copies / constants forwarded          224
   temporaries merged away                 5
   dead instructions removed             177
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

 Symbol table: 11 parameter(s)/local(s), 104 temporaries, frame 1156 bytes

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
   t35              temp    class Point *                   4     252
   t37              temp    class Point *                   4     264
   t51              temp    int                             4     320
   t56              temp    int                             4     344
   t57              temp    int                             4     348
   t58              temp    int                             4     352
   t59              temp    int                             4     356
   t62              temp    bool                            1     368
   t63              temp    int                             4     372
   t66              temp    bool                            1     384
   t67              temp    int                             4     388
   t68              temp    class Segment *                 4     392
   t69              temp    class Segment *                 4     396
   t73              temp    int                             4     412
   t74              temp    class Rect *                    4     416
   t80              temp    int                             4     440
   t82              temp    class Rect *                    4     448
   t83              temp    class Rect *                    4     452
   t90              temp    class Rect *                    4     480
   t91              temp    class Rect *                    4     484
   t96              temp    int                             4     504
   t98              temp    int                             4     512
   t99              temp    int                             4     516
   t102             temp    int                             4     528
   t104             temp    int                             4     536
   t105             temp    int                             4     540
   t111             temp    int                             4     564
   t112             temp    int                             4     568
   t114             temp    int                             4     576
   t115             temp    int                             4     580
   t116             temp    int                             4     584
   t118             temp    int                             4     592
   t119             temp    int                             4     596
   t120             temp    int                             4     600
   t126             temp    int                             4     624
   t127             temp    int                             4     628
   t129             temp    int                             4     636
   t130             temp    int                             4     640
   t135             temp    int                             4     660
   t136             temp    int                             4     664
   t142             temp    int                             4     688
   t143             temp    int                             4     692
   t145             temp    class Rect *                    4     700
   t146             temp    class Rect *                    4     704
   t148             temp    class Rect *                    4     712
   t149             temp    class Rect *                    4     716
   t152             temp    int                             4     728
   t154             temp    int                             4     736
   t155             temp    int                             4     740
   t158             temp    int                             4     752
   t160             temp    int                             4     760
   t161             temp    int                             4     764
   t164             temp    class Point                     8     776
   t165             temp    class Point *                   4     784
   t168             temp    class Point                     8     796
   t169             temp    class Point *                   4     804
   t172             temp    int                             4     816
   t173             temp    int                             4     820
   t174             temp    int                             4     824
   t175             temp    class Point *                   4     828
   t176             temp    int                             4     832
   t177             temp    const class Point *             4     836
   t178             temp    int                             4     840
   t179             temp    int                             4     844
   t182             temp    int                             4     856
   t183             temp    int                             4     860
   t184             temp    int                             4     864
   t186             temp    int                             4     872
   t188             temp    int                             4     880
   t189             temp    int                             4     884
   t192             temp    int                             4     896
   t193             temp    int                             4     900
   t194             temp    int                             4     904
   t196             temp    int                             4     912
   t198             temp    int                             4     920
   t199             temp    int                             4     924
   t208             temp    class Point                     8     960
   t209             temp    class Point *                   4     968
   t210             temp    int                             4     972
   t211             temp    int                             4     976
   t212             temp    int                             4     980
   t214             temp    int                             4     988
   t216             temp    int                             4     996
   t217             temp    int                             4    1000
   t219             temp    class Point *                   4    1008
   t221             temp    class Point *                   4    1016
   t227             temp    class Point                     8    1040
   t228             temp    class Point                     8    1048
   t232             temp    class Point                     8    1068
   t233             temp    int                             4    1076
   t234             temp    int                             4    1080
   t235             temp    int                             4    1084
   t236             temp    int                             4    1088
   t237             temp    int                             4    1092
   t239             temp    class Rect *                    4    1100
   t240             temp    class Rect *                    4    1104
   t248             temp    int                             4    1136
   t251             temp    int                             4    1148
   (148 temporaries no longer used after optimization not shown)

 Code: 216 instruction(s)

    167     t1 = &r
    168     param t1                            (this)
    169     call Shape::Shape(), 1
    170     t82 = t1 ptr+ 4
    171     *t82 = 1
    172     t83 = t1 ptr+ 8
    173     *t83 = 1
    174     *t82 = 3
    175     *t83 = 4
    176     t3 = &q
    177     param t3                            (this)
    178     call Shape::Shape(), 1
    179     t90 = t3 ptr+ 4
    180     *t90 = 1
    181     t91 = t3 ptr+ 8
    182     *t91 = 1
    183     param t3                            (this)
    184     param 5
    185     param 5
    186     call Rect::set(int, int), 3
    187     t96 = *t82
    188     t98 = *t83
    189     t99 = t96 int* t98
    190     t102 = *t90
    191     t104 = *t91
    192     t105 = t102 int* t104
    193     t111 = t102 int+ t104
    194     t112 = t111 int<< 1
    195     param "%d %d %d %d\n"
    196     param t99
    197     param t105
    198     param t112
    199     param Shape::live
    200     call printf, 5
    201     param t1                            (this)
    202     t114 = call Rect::area(), 1
    203     t115 = *t1
    204     t116 = t114 int+ t115
    205     param t3                            (this)
    206     t118 = call Shape::area(), 1
    207     param t3                            (this)
    208     t119 = call Shape::name(), 1
    209     t120 = t118 int+ t119
    210     param "%d %d %c %c\n"
    211     param t116
    212     param t120
    213     param 81
    214     param 83
    215     call printf, 5
    216     t126 = *t90
    217     t127 = t126 int+ 1
    218     *t90 = t127
    219     t129 = *t91
    220     t130 = t129 int+ 1
    221     *t91 = t130
    222     *t90 = 10
    223     t135 = *t91
    224     t136 = t135 int* 10
    225     t142 = 10 int+ t135
    226     t143 = t142 int<< 1
    227     param "%d %d\n"
    228     param t136
    229     param t143
    230     call printf, 3
    231     t25 = &pair
    232     param t25                           (this)
    233     call Shape::Shape(), 1
    234     t145 = t25 ptr+ 4
    235     *t145 = 1
    236     t146 = t25 ptr+ 8
    237     *t146 = 1
    238     t26 = t25 ptr+ 12
    239     param t26                           (this)
    240     call Shape::Shape(), 1
    241     t148 = t26 ptr+ 4
    242     *t148 = 1
    243     t149 = t26 ptr+ 8
    244     *t149 = 1
    245     pair[16] = 6
    246     t152 = *t145
    247     t154 = *t146
    248     t155 = t152 int* t154
    249     t158 = *t148
    250     t160 = *t149
    251     t161 = t158 int* t160
    252     t32 = t155 int+ t161
    253     t33 = pair[12]
    254     param "%d %d %d\n"
    255     param t32
    256     param t33
    257     param Shape::live
    258     call printf, 4
    259     param "%d\n"
    260     param Shape::live
    261     call printf, 2
    262     t165 = &t164
    263     param t165                          (this)
    264     call Point::Point(), 1
    265     t164[0] = 3
    266     t164[4] = 4
    267     a = t164
    268     t35 = &a
    269     t169 = &t168
    270     param t169                          (this)
    271     call Point::Point(), 1
    272     t168[0] = 1
    273     t168[4] = 1
    274     b = t168
    275     t37 = &b
    276     t172 = *t35
    277     t173 = *t37
    278     t174 = t172 int+ t173
    279     *t35 = t174
    280     t175 = t35 ptr+ 4
    281     t176 = *t175
    282     t177 = t37 ptr+ 4
    283     t178 = *t177
    284     t179 = t176 int+ t178
    285     *t175 = t179
    286     t182 = *t35
    287     t183 = *t37
    288     t184 = t182 int+ t183
    289     *t35 = t184
    290     t186 = *t175
    291     t188 = *t177
    292     t189 = t186 int+ t188
    293     *t175 = t189
    294     t192 = *t35
    295     t193 = *t37
    296     t194 = t192 int+ t193
    297     *t35 = t194
    298     t196 = *t175
    299     t198 = *t177
    300     t199 = t196 int+ t198
    301     *t175 = t199
    302     t51 = t199 int<< 1
    303     *t35 = t51
    304     t209 = &t208
    305     param t209                          (this)
    306     call Point::Point(), 1
    307     t210 = *t35
    308     t211 = *t37
    309     t212 = t210 int- t211
    310     t208[0] = t212
    311     t214 = *t175
    312     t216 = *t177
    313     t217 = t214 int- t216
    314     t208[4] = t217
    315     c = t208
    316     t56 = a[0]
    317     t57 = a[4]
    318     t58 = c[0]
    319     t59 = c[4]
    320     param t37                           (this)
    321     param t35
    322     t62 = call Point::operator<(const class Point &), 2
    323     t63 = booltoint t62
    324     param t35                           (this)
    325     param t37
    326     t66 = call Point::operator<(const class Point &), 2
    327     t67 = booltoint t66
    328     param "%d %d %d %d %d %d\n"
    329     param t56
    330     param t57
    331     param t58
    332     param t59
    333     param t63
    334     param t67
    335     call printf, 7
    336     t68 = &s
    337     *t68 = 0
    338     t219 = t68 ptr+ 4
    339     *t219 = 0
    340     t69 = t68 ptr+ 8
    341     *t69 = 0
    342     t221 = t69 ptr+ 4
    343     *t221 = 0
    344     param 1
    345     param 2
    346     t227 = call at(int, int), 2
    347     *t68 = t227
    348     param 4
    349     param 6
    350     t228 = call at(int, int), 2
    351     *t69 = t228
    352     param t69                           (this)
    353     param t68
    354     t232 = call Point::operator-(const class Point &), 2
    355     t233 = t232[0]
    356     t234 = t233 int* t233
    357     t235 = t232[4]
    358     t236 = t235 int* t235
    359     t237 = t234 int+ t236
    360     t73 = s[12]
    361     param "%d %d\n"
    362     param t237
    363     param t73
    364     call printf, 3
    365     t74 = &last
    366     param t74                           (this)
    367     call Shape::Shape(), 1
    368     t239 = t74 ptr+ 4
    369     *t239 = 1
    370     t240 = t74 ptr+ 8
    371     *t240 = 1
    372     *t239 = 2
    373     *t240 = 9
    374     t248 = *t239
    375     t251 = t248 int* 9
    376     t80 = *t74
    377     param "%d %d %d\n"
    378     param t251
    379     param 0
    380     param t80
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
