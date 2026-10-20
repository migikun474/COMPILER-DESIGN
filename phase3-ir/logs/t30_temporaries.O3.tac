=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t30_temporaries.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 522 -> 544 instruction(s) for 'test/t30_temporaries.c'.

optimization summary (-O3)
    instructions                522 -> 544   (-4% fewer)
    constants folded            3
    algebraic simplifications   0
    common subexpressions       55
    copies / constants forwarded 218
    temporaries merged away     11
    dead instructions removed   193
    jumps removed or redirected 6
    unreachable instructions    0
    propagated across blocks    2
    dead assignments removed    14
    calls inlined               85
    tail calls turned to jumps  0
    common across blocks        6
    moved out of loops          3

function Tag::Tag(int)        link name: _ZN3TagC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 100:   *this = n
 101:   param "+%d "
 102:   param n
 103:   call printf, 2
 104:   return

function Tag::~Tag()        link name: _ZN3TagD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    t1             temp   int                        4      4
    total width 8
  code
 105:   t1 = *this
 106:   param "-%d "
 107:   param t1
 108:   call printf, 2
 109:   return

function Tag::value()        link name: _ZN3Tag5valueEv
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    t1             temp   int                        4      4
    t2             temp   int                        4      8
    total width 12
  code
 110:   t1 = *this
 111:   t2 = t1 int* 10
 112:   return t2

function Tag::operator+(const class Tag &)        link name: _ZN3TagplERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Tag *                4      0
    o              param  const class Tag &          4      4
    t1             temp   class Tag                  4      8
    t2             temp   class Tag *                4     12
    t3             temp   int                        4     16
    t4             temp   int                        4     20
    t5             temp   int                        4     24
    t6             temp   class Tag *                4     28
    t7             temp   int                        4     32
    total width 36
  code
 113:   t2 = &t1
 114:   t3 = *this
 115:   t4 = *o
 116:   t5 = t3 int+ t4
 117:   *t2 = t5
 118:   param "+%d "
 119:   param t5
 120:   call printf, 2
 121:   return t1

function Copy::Copy(int)        link name: _ZN4CopyC1Ei
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    n              param  int                        4      4
    t1             temp   int                        4      8
    total width 12
  code
 122:   *this = n
 123:   param "+c%d "
 124:   param n
 125:   call printf, 2
 126:   return

function Copy::Copy(const class Copy &)        link name: _ZN4CopyC1ERKS_
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    o              param  const class Copy &         4      4
    t1             temp   int                        4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    total width 20
  code
 127:   t1 = *o
 128:   t2 = t1 int+ 100
 129:   *this = t2
 130:   param "copy%d "
 131:   param t2
 132:   call printf, 2
 133:   return

function Copy::~Copy()        link name: _ZN4CopyD1Ev
  symbol table (name, kind, type, width, offset)
    this           param  class Copy *               4      0
    t1             temp   int                        4      4
    total width 8
  code
 134:   t1 = *this
 135:   param "-c%d "
 136:   param t1
 137:   call printf, 2
 138:   return

function make(int)        link name: _Z4makei
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   class Tag                  4      4
    t2             temp   class Tag *                4      8
    t3             temp   class Tag *                4     12
    t4             temp   int                        4     16
    total width 20
  code
 139:   t2 = &t1
 140:   *t2 = n
 141:   param "+%d "
 142:   param n
 143:   call printf, 2
 144:   return t1

function named(int)        link name: _Z5namedi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t              local  class Tag                  4      4
    t1             temp   class Tag *                4      8
    t2             temp   int                        4     12
    t3             temp   int                        4     16
    t4             temp   class Tag *                4     20
    t5             temp   int                        4     24
    total width 28
  code
 145:   t1 = &t
 146:   *t1 = n
 147:   param "+%d "
 148:   param n
 149:   call printf, 2
 150:   t2 = t[0]
 151:   t3 = t2 int+ 1
 152:   t[0] = t3
 153:   return t

function pick(int)        link name: _Z4picki
  symbol table (name, kind, type, width, offset)
    which          param  int                        4      0
    a              local  class Tag                  4      4
    b              local  class Tag                  4      8
    t1             temp   class Tag *                4     12
    t2             temp   class Tag *                4     16
    t3             temp   class Tag                  4     20
    t4             temp   class Tag *                4     24
    t5             temp   class Tag *                4     28
    t6             temp   class Tag                  4     32
    t7             temp   class Tag *                4     36
    t8             temp   class Tag *                4     40
    t9             temp   class Tag *                4     44
    t10            temp   int                        4     48
    t11            temp   class Tag *                4     52
    t12            temp   int                        4     56
    t13            temp   class Tag *                4     60
    t14            temp   int                        4     64
    t15            temp   class Tag *                4     68
    t16            temp   int                        4     72
    t17            temp   class Tag *                4     76
    t18            temp   int                        4     80
    t19            temp   class Tag *                4     84
    t20            temp   int                        4     88
    total width 92
  code
 154:     t1 = &a
 155:     *t1 = 40
 156:     param "+%d "
 157:     param 40
 158:     call printf, 2
 159:     t2 = &b
 160:     *t2 = 41
 161:     param "+%d "
 162:     param 41
 163:     call printf, 2
 164:     if which int== 0 goto L1
 165:     t3 = a
 166:     t14 = *t2
 167:     param "-%d "
 168:     param t14
 169:     call printf, 2
 170:     t16 = *t1
 171:     param "-%d "
 172:     param t16
 173:     call printf, 2
 174:     return t3
 175: L1: t6 = b
 176:     t18 = *t2
 177:     param "-%d "
 178:     param t18
 179:     call printf, 2
 180:     t20 = *t1
 181:     param "-%d "
 182:     param t20
 183:     call printf, 2
 184:     return t6

function byValue(class Tag)        link name: _Z7byValue3Tag
  symbol table (name, kind, type, width, offset)
    t              param  class Tag                  4      0
    t1             temp   int                        4      4
    total width 8
  code
 185:   t1 = t[0]
 186:   return t1

function byRef(const class Tag &)        link name: _Z5byRefRK3Tag
  symbol table (name, kind, type, width, offset)
    t              param  const class Tag &          4      0
    t1             temp   int                        4      4
    total width 8
  code
 187:   t1 = *t
 188:   return t1

function copied(class Copy)        link name: _Z6copied4Copy
  symbol table (name, kind, type, width, offset)
    c              param  class Copy                 4      0
    t1             temp   int                        4      4
    total width 8
  code
 189:   t1 = c[0]
 190:   return t1

function makeCopy(int)        link name: _Z8makeCopyi
  symbol table (name, kind, type, width, offset)
    n              param  int                        4      0
    t1             temp   class Copy                 4      4
    t2             temp   class Copy *               4      8
    t3             temp   class Copy *               4     12
    t4             temp   int                        4     16
    total width 20
  code
 191:   t2 = &t1
 192:   *t2 = n
 193:   param "+c%d "
 194:   param n
 195:   call printf, 2
 196:   return t1

function sameCopy(class Copy)        link name: _Z8sameCopy4Copy
  symbol table (name, kind, type, width, offset)
    c              param  class Copy                 4      0
    t1             temp   class Copy                 4      4
    t2             temp   class Copy *               4      8
    t3             temp   class Copy *               4     12
    t4             temp   class Copy *               4     16
    t5             temp   const class Copy &         4     20
    t6             temp   int                        4     24
    t7             temp   int                        4     28
    total width 32
  code
 197:   t2 = &t1
 198:   t3 = &c
 199:   t6 = *t3
 200:   t7 = t6 int+ 100
 201:   *t2 = t7
 202:   param "copy%d "
 203:   param t7
 204:   call printf, 2
 205:   return t1

function Shape::sides()        link name: _ZN5Shape5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 206:   return 0

function Shape::kind()        link name: _ZN5Shape4kindEv
  symbol table (name, kind, type, width, offset)
    this           param  class Shape *              4      0
    total width 4
  code
 207:   return 1

function Square::sides()        link name: _ZN6Square5sidesEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 208:   return 4

function Square::kind()        link name: _ZN6Square4kindEv
  symbol table (name, kind, type, width, offset)
    this           param  class Square *             4      0
    total width 4
  code
 209:   return 2

function mix(long long, long long, int)        link name: _Z3mixxxi
  symbol table (name, kind, type, width, offset)
    a              param  long long                  8      0
    b              param  long long                  8      8
    n              param  int                        4     16
    sum            local  long long                  8     24
    i              local  int                        4     32
    t1             temp   long long                  8     40
    t2             temp   long long                  8     48
    t3             temp   long long                  8     56
    t4             temp   long long                  8     64
    t5             temp   long long                  8     72
    t6             temp   long long                  8     80
    t7             temp   long long                  8     88
    t8             temp   long long                  8     96
    t9             temp   long long                  8    104
    t10            temp   int                        4    112
    t11            temp   long long                  8    120
    t12            temp   long long                  8    128
    total width 136
  code
 210:     sum = 0
 211:     i = 0
 212: L2: if i int>= n goto L3
 213:     t1 = inttollong i
 214:     t2 = a llong* t1
 215:     t3 = sum llong+ t2
 216:     t4 = b llong^ sum
 217:     t5 = t3 llong- t4
 218:     sum = t5
 219:     a = a llong+ 4294967296
 220:     t7 = llong- b
 221:     t8 = t5 llong& 65535
 222:     b = t7 llong+ t8
 223:     i = i int+ 1
 224:     goto L2
 225: L3: t11 = sum llong+ a
 226:     t12 = t11 llong- b
 227:     return t12

function main()        link name: main
  symbol table (name, kind, type, width, offset)
    v              local  int                        4      0
    kept           local  class Tag                  4      4
    sum            local  class Tag                  4      8
    i              local  int                        4     12
    n              local  class Tag                  4     16
    r              local  const class Tag &          4     20
    c              local  class Copy                 4     24
    d              local  class Copy                 4     28
    e              local  class Copy                 4     32
    q              local  class Square               1     36
    p              local  class Shape *              4     40
    m              local  long long                  8     48
    inner          local  class Tag                  4     56
    t1             temp   class Tag                  4     60
    t2             temp   class Tag *                4     64
    t3             temp   class Tag *                4     68
    t4             temp   class Tag                  4     72
    t5             temp   class Tag *                4     76
    t6             temp   class Tag *                4     80
    t7             temp   class Tag                  4     84
    t8             temp   class Tag *                4     88
    t9             temp   class Tag *                4     92
    t10            temp   int                        4     96
    t11            temp   class Tag                  4    100
    t12            temp   class Tag *                4    104
    t13            temp   class Tag *                4    108
    t14            temp   int                        4    112
    t15            temp   int                        4    116
    t16            temp   class Tag *                4    120
    t17            temp   class Tag *                4    124
    t18            temp   class Tag                  4    128
    t19            temp   class Tag *                4    132
    t20            temp   class Tag *                4    136
    t21            temp   class Tag *                4    140
    t22            temp   class Tag                  4    144
    t23            temp   class Tag *                4    148
    t24            temp   class Tag *                4    152
    t25            temp   class Tag                  4    156
    t26            temp   class Tag *                4    160
    t27            temp   class Tag *                4    164
    t28            temp   class Tag *                4    168
    t29            temp   int                        4    172
    t30            temp   class Tag *                4    176
    t31            temp   class Tag *                4    180
    t32            temp   class Tag                  4    184
    t33            temp   class Tag *                4    188
    t34            temp   class Tag *                4    192
    t35            temp   class Tag *                4    196
    t36            temp   class Tag                  4    200
    t37            temp   class Tag *                4    204
    t38            temp   int                        4    208
    t39            temp   class Tag *                4    212
    t40            temp   class Tag *                4    216
    t41            temp   class Tag                  4    220
    t42            temp   class Tag *                4    224
    t43            temp   int                        4    228
    t44            temp   class Tag *                4    232
    t45            temp   class Tag                  4    236
    t46            temp   class Tag *                4    240
    t47            temp   int                        4    244
    t48            temp   class Tag *                4    248
    t49            temp   class Tag                  4    252
    t50            temp   class Tag *                4    256
    t51            temp   class Tag *                4    260
    t52            temp   int                        4    264
    t53            temp   class Tag *                4    268
    t54            temp   class Tag                  4    272
    t55            temp   class Tag *                4    276
    t56            temp   class Tag *                4    280
    t57            temp   int                        4    284
    t58            temp   class Tag *                4    288
    t59            temp   int                        4    292
    t60            temp   class Tag                  4    296
    t61            temp   class Tag *                4    300
    t62            temp   int                        4    304
    t63            temp   class Tag *                4    308
    t64            temp   class Tag                  4    312
    t65            temp   class Tag *                4    316
    t66            temp   class Tag *                4    320
    t67            temp   int                        4    324
    t68            temp   int                        4    328
    t69            temp   class Tag *                4    332
    t70            temp   int                        4    336
    t71            temp   class Tag                  4    340
    t72            temp   class Tag *                4    344
    t73            temp   int                        4    348
    t74            temp   class Tag *                4    352
    t75            temp   class Tag                  4    356
    t76            temp   class Tag *                4    360
    t77            temp   int                        4    364
    t78            temp   class Tag *                4    368
    t79            temp   class Tag                  4    372
    t80            temp   class Tag *                4    376
    t81            temp   class Tag *                4    380
    t82            temp   int                        4    384
    t83            temp   class Tag                  4    388
    t84            temp   class Tag *                4    392
    t85            temp   int                        4    396
    t86            temp   class Tag *                4    400
    t87            temp   class Tag                  4    404
    t88            temp   class Tag *                4    408
    t89            temp   int                        4    412
    t90            temp   int                        4    416
    t91            temp   class Tag *                4    420
    t92            temp   class Tag                  4    424
    t93            temp   class Tag *                4    428
    t94            temp   class Tag *                4    432
    t95            temp   int                        4    436
    t96            temp   class Tag                  4    440
    t97            temp   class Tag *                4    444
    t98            temp   class Tag *                4    448
    t99            temp   int                        4    452
    t100           temp   class Copy *               4    456
    t101           temp   class Copy                 4    460
    t102           temp   class Copy *               4    464
    t103           temp   class Copy *               4    468
    t104           temp   int                        4    472
    t105           temp   class Copy *               4    476
    t106           temp   class Copy                 4    480
    t107           temp   class Copy *               4    484
    t108           temp   int                        4    488
    t109           temp   class Copy *               4    492
    t110           temp   class Copy                 4    496
    t111           temp   class Copy *               4    500
    t112           temp   class Copy *               4    504
    t113           temp   int                        4    508
    t114           temp   class Copy                 4    512
    t115           temp   class Copy *               4    516
    t116           temp   class Copy *               4    520
    t117           temp   class Copy                 4    524
    t118           temp   class Copy *               4    528
    t119           temp   class Copy *               4    532
    t120           temp   class Copy *               4    536
    t121           temp   int                        4    540
    t122           temp   class Square *             4    544
    t123           temp   class Square *             4    548
    t124           temp   int                        4    552
    t125           temp   class Square *             4    556
    t126           temp   int                        4    560
    t127           temp   int                        4    564
    t128           temp   int                        4    568
    t129           temp   class Square *             4    572
    t130           temp   int                        4    576
    t131           temp   class Square *             4    580
    t132           temp   int                        4    584
    t133           temp   long long                  8    592
    t134           temp   int                        4    600
    t135           temp   long long                  8    608
    t136           temp   long long                  8    616
    t137           temp   long long                  8    624
    t138           temp   class Tag *                4    632
    t139           temp   class Tag *                4    636
    t140           temp   int                        4    640
    t141           temp   class Tag                  4    644
    t142           temp   class Tag *                4    648
    t143           temp   class Tag *                4    652
    t144           temp   int                        4    656
    t145           temp   int                        4    660
    t146           temp   class Tag *                4    664
    t147           temp   class Tag *                4    668
    t148           temp   class Copy *               4    672
    t149           temp   class Copy *               4    676
    t150           temp   class Copy *               4    680
    t151           temp   class Tag *                4    684
    t152           temp   class Tag *                4    688
    t153           temp   class Tag *                4    692
    t154           temp   class Tag *                4    696
    t155           temp   class Tag *                4    700
    t156           temp   int                        4    704
    t157           temp   class Tag *                4    708
    t158           temp   int                        4    712
    t159           temp   int                        4    716
    t160           temp   class Tag                  4    720
    t161           temp   class Tag *                4    724
    t162           temp   class Tag *                4    728
    t163           temp   int                        4    732
    t164           temp   class Tag *                4    736
    t165           temp   int                        4    740
    t166           temp   class Tag *                4    744
    t167           temp   int                        4    748
    t168           temp   int                        4    752
    t169           temp   int                        4    756
    t170           temp   class Tag                  4    760
    t171           temp   class Tag *                4    764
    t172           temp   class Tag *                4    768
    t173           temp   int                        4    772
    t174           temp   int                        4    776
    t175           temp   class Tag *                4    780
    t176           temp   int                        4    784
    t177           temp   class Tag *                4    788
    t178           temp   int                        4    792
    t179           temp   int                        4    796
    t180           temp   class Tag                  4    800
    t181           temp   class Tag *                4    804
    t182           temp   class Tag *                4    808
    t183           temp   int                        4    812
    t184           temp   class Tag *                4    816
    t185           temp   const class Tag &          4    820
    t186           temp   class Tag                  4    824
    t187           temp   class Tag *                4    828
    t188           temp   int                        4    832
    t189           temp   int                        4    836
    t190           temp   int                        4    840
    t191           temp   class Tag *                4    844
    t192           temp   int                        4    848
    t193           temp   class Tag *                4    852
    t194           temp   const class Tag &          4    856
    t195           temp   class Tag                  4    860
    t196           temp   class Tag *                4    864
    t197           temp   int                        4    868
    t198           temp   int                        4    872
    t199           temp   int                        4    876
    t200           temp   class Tag *                4    880
    t201           temp   const class Tag &          4    884
    t202           temp   class Tag                  4    888
    t203           temp   class Tag *                4    892
    t204           temp   int                        4    896
    t205           temp   int                        4    900
    t206           temp   int                        4    904
    t207           temp   class Tag *                4    908
    t208           temp   int                        4    912
    t209           temp   class Tag *                4    916
    t210           temp   int                        4    920
    t211           temp   class Tag *                4    924
    t212           temp   int                        4    928
    t213           temp   class Tag                  4    932
    t214           temp   int                        4    936
    t215           temp   class Tag *                4    940
    t216           temp   int                        4    944
    t217           temp   class Tag                  4    948
    t218           temp   int                        4    952
    t219           temp   class Tag *                4    956
    t220           temp   int                        4    960
    t221           temp   class Tag *                4    964
    t222           temp   int                        4    968
    t223           temp   const class Tag &          4    972
    t224           temp   int                        4    976
    t225           temp   class Tag *                4    980
    t226           temp   int                        4    984
    t227           temp   class Tag *                4    988
    t228           temp   int                        4    992
    t229           temp   const class Tag &          4    996
    t230           temp   int                        4   1000
    t231           temp   class Tag *                4   1004
    t232           temp   int                        4   1008
    t233           temp   int                        4   1012
    t234           temp   class Tag                  4   1016
    t235           temp   class Tag *                4   1020
    t236           temp   class Tag *                4   1024
    t237           temp   int                        4   1028
    t238           temp   class Tag *                4   1032
    t239           temp   int                        4   1036
    t240           temp   const class Tag &          4   1040
    t241           temp   int                        4   1044
    t242           temp   class Tag *                4   1048
    t243           temp   int                        4   1052
    t244           temp   class Tag *                4   1056
    t245           temp   int                        4   1060
    t246           temp   class Tag *                4   1064
    t247           temp   int                        4   1068
    t248           temp   class Tag *                4   1072
    t249           temp   int                        4   1076
    t250           temp   class Tag *                4   1080
    t251           temp   int                        4   1084
    t252           temp   int                        4   1088
    t253           temp   class Tag                  4   1092
    t254           temp   class Tag *                4   1096
    t255           temp   int                        4   1100
    t256           temp   int                        4   1104
    t257           temp   class Tag *                4   1108
    t258           temp   int                        4   1112
    t259           temp   class Tag *                4   1116
    t260           temp   int                        4   1120
    t261           temp   class Tag *                4   1124
    t262           temp   int                        4   1128
    t263           temp   class Tag *                4   1132
    t264           temp   int                        4   1136
    t265           temp   class Tag *                4   1140
    t266           temp   int                        4   1144
    t267           temp   class Copy *               4   1148
    t268           temp   int                        4   1152
    t269           temp   class Copy *               4   1156
    t270           temp   const class Copy &         4   1160
    t271           temp   int                        4   1164
    t272           temp   int                        4   1168
    t273           temp   class Copy                 4   1172
    t274           temp   int                        4   1176
    t275           temp   class Copy *               4   1180
    t276           temp   int                        4   1184
    t277           temp   class Copy *               4   1188
    t278           temp   int                        4   1192
    t279           temp   class Copy                 4   1196
    t280           temp   int                        4   1200
    t281           temp   class Copy *               4   1204
    t282           temp   int                        4   1208
    t283           temp   int                        4   1212
    t284           temp   class Copy                 4   1216
    t285           temp   class Copy *               4   1220
    t286           temp   class Copy *               4   1224
    t287           temp   const class Copy &         4   1228
    t288           temp   int                        4   1232
    t289           temp   int                        4   1236
    t290           temp   class Copy                 4   1240
    t291           temp   class Copy                 4   1244
    t292           temp   class Copy *               4   1248
    t293           temp   class Copy *               4   1252
    t294           temp   class Copy *               4   1256
    t295           temp   int                        4   1260
    t296           temp   class Square *             4   1264
    t297           temp   class Shape *              4   1268
    t298           temp   class Shape *              4   1272
    t299           temp   class Shape *              4   1276
    t300           temp   class Square *             4   1280
    t301           temp   class Shape *              4   1284
    t302           temp   class Tag *                4   1288
    t303           temp   int                        4   1292
    t304           temp   const class Tag &          4   1296
    t305           temp   int                        4   1300
    t306           temp   class Tag *                4   1304
    t307           temp   int                        4   1308
    t308           temp   const class Tag &          4   1312
    t309           temp   int                        4   1316
    t310           temp   class Tag *                4   1320
    t311           temp   int                        4   1324
    t312           temp   class Tag *                4   1328
    t313           temp   int                        4   1332
    t314           temp   class Copy *               4   1336
    t315           temp   int                        4   1340
    t316           temp   class Copy *               4   1344
    t317           temp   int                        4   1348
    t318           temp   class Copy *               4   1352
    t319           temp   int                        4   1356
    t320           temp   class Tag *                4   1360
    t321           temp   int                        4   1364
    t322           temp   class Tag *                4   1368
    t323           temp   int                        4   1372
    t324           temp   class Tag *                4   1376
    t325           temp   int                        4   1380
    t326           temp   class Tag *                4   1384
    t327           temp   int                        4   1388
    total width 1392
  code
 228:     t2 = &t1
 229:     *t2 = 1
 230:     param "+%d "
 231:     param 1
 232:     call printf, 2
 233:     t158 = *t2
 234:     param "-%d "
 235:     param t158
 236:     call printf, 2
 237:     param "| "
 238:     call printf, 1
 239:     t161 = &t160
 240:     param t161                          (this)
 241:     param 2
 242:     call Tag::Tag(int), 2
 243:     t4 = t160
 244:     t5 = &t4
 245:     t163 = *t5
 246:     param "-%d "
 247:     param t163
 248:     call printf, 2
 249:     param "| "
 250:     call printf, 1
 251:     t8 = &t7
 252:     *t8 = 3
 253:     param "+%d "
 254:     param 3
 255:     call printf, 2
 256:     t167 = *t8
 257:     t168 = t167 int* 10
 258:     t171 = &t170
 259:     param t171                          (this)
 260:     param 4
 261:     call Tag::Tag(int), 2
 262:     t11 = t170
 263:     t12 = &t11
 264:     t173 = *t12
 265:     t174 = t173 int* 10
 266:     t15 = t168 int+ t174
 267:     param "-%d "
 268:     param t173
 269:     call printf, 2
 270:     t178 = *t8
 271:     param "-%d "
 272:     param t178
 273:     call printf, 2
 274:     param "%d | "
 275:     param t15
 276:     call printf, 2
 277:     t181 = &t180
 278:     param t181                          (this)
 279:     param 5
 280:     call Tag::Tag(int), 2
 281:     kept = t180
 282:     t20 = &kept
 283:     param "| "
 284:     call printf, 1
 285:     t23 = &t22
 286:     *t23 = 6
 287:     param "+%d "
 288:     param 6
 289:     call printf, 2
 290:     t187 = &t186
 291:     t188 = *t20
 292:     t189 = *t23
 293:     t190 = t188 int+ t189
 294:     param t187                          (this)
 295:     param t190
 296:     call Tag::Tag(int), 2
 297:     sum = t186
 298:     t27 = &sum
 299:     t192 = *t23
 300:     param "-%d "
 301:     param t192
 302:     call printf, 2
 303:     t29 = sum[0]
 304:     param "%d | "
 305:     param t29
 306:     call printf, 2
 307:     t196 = &t195
 308:     t197 = *t20
 309:     t198 = *t27
 310:     t199 = t197 int+ t198
 311:     param t196                          (this)
 312:     param t199
 313:     call Tag::Tag(int), 2
 314:     t32 = t195
 315:     t33 = &t32
 316:     t203 = &t202
 317:     t204 = *t33
 318:     t205 = *t20
 319:     t206 = t204 int+ t205
 320:     param t203                          (this)
 321:     param t206
 322:     call Tag::Tag(int), 2
 323:     t36 = t202
 324:     t37 = &t36
 325:     t38 = t36[0]
 326:     t208 = *t37
 327:     param "-%d "
 328:     param t208
 329:     call printf, 2
 330:     t210 = *t33
 331:     param "-%d "
 332:     param t210
 333:     call printf, 2
 334:     param "%d | "
 335:     param t38
 336:     call printf, 2
 337:     t42 = &t41
 338:     *t42 = 10
 339:     param "+%d "
 340:     param 10
 341:     call printf, 2
 342:     t213 = t41
 343:     t214 = t213[0]
 344:     t216 = *t42
 345:     param "-%d "
 346:     param t216
 347:     call printf, 2
 348:     param "%d | "
 349:     param t214
 350:     call printf, 2
 351:     t45 = kept
 352:     t46 = &t45
 353:     t217 = t45
 354:     t218 = t217[0]
 355:     t220 = *t46
 356:     param "-%d "
 357:     param t220
 358:     call printf, 2
 359:     param "%d | "
 360:     param t218
 361:     call printf, 2
 362:     t50 = &t49
 363:     *t50 = 11
 364:     param "+%d "
 365:     param 11
 366:     call printf, 2
 367:     t224 = *t50
 368:     param "-%d "
 369:     param t224
 370:     call printf, 2
 371:     param "%d | "
 372:     param t224
 373:     call printf, 2
 374:     t55 = &t54
 375:     *t55 = 12
 376:     param "+%d "
 377:     param 12
 378:     call printf, 2
 379:     t230 = *t55
 380:     param "-%d "
 381:     param t230
 382:     call printf, 2
 383:     if t230 int<= 5 goto L4
 384:     param "if "
 385:     call printf, 1
 386: L4: param "| "
 387:     call printf, 1
 388:     i = 0
 389:     t61 = &t60
 390:     t65 = &t64
 391:     t235 = &t234
 392: L5: if i int>= 2 goto L6
 393:     t59 = 13 int+ i
 394:     param t235                          (this)
 395:     param t59
 396:     call Tag::Tag(int), 2
 397:     t60 = t234
 398:     t62 = t60[0]
 399:     t237 = *t61
 400:     param "-%d "
 401:     param t237
 402:     call printf, 2
 403:     if t62 int<= 0 goto L6
 404:     param "body "
 405:     call printf, 1
 406:     *t65 = 20
 407:     param "+%d "
 408:     param 20
 409:     call printf, 2
 410:     t241 = *t65
 411:     i = i int+ t241
 412:     param "-%d "
 413:     param t241
 414:     call printf, 2
 415:     goto L5
 416: L6: param "| "
 417:     call printf, 1
 418:     if t224 int<= 0 goto L7
 419:     t72 = &t71
 420:     *t72 = 21
 421:     param "+%d "
 422:     param 21
 423:     call printf, 2
 424:     t70 = t71[0]
 425:     t247 = *t72
 426:     param "-%d "
 427:     param t247
 428:     call printf, 2
 429:     goto L8
 430: L7: t76 = &t75
 431:     *t76 = 22
 432:     param "+%d "
 433:     param 22
 434:     call printf, 2
 435:     t70 = t75[0]
 436:     t251 = *t76
 437:     param "-%d "
 438:     param t251
 439:     call printf, 2
 440: L8: param "%d | "
 441:     param t70
 442:     call printf, 2
 443:     t254 = &t253
 444:     param t254                          (this)
 445:     param 30
 446:     call Tag::Tag(int), 2
 447:     t255 = t253[0]
 448:     t256 = t255 int+ 1
 449:     t253[0] = t256
 450:     n = t253
 451:     t81 = &n
 452:     t82 = n[0]
 453:     param "%d | "
 454:     param t82
 455:     call printf, 2
 456:     param 1
 457:     t83 = call pick(int), 1
 458:     t84 = &t83
 459:     t85 = t83[0]
 460:     t258 = *t84
 461:     param "-%d "
 462:     param t258
 463:     call printf, 2
 464:     param 0
 465:     t87 = call pick(int), 1
 466:     t88 = &t87
 467:     t89 = t87[0]
 468:     t90 = t85 int+ t89
 469:     t260 = *t88
 470:     param "-%d "
 471:     param t260
 472:     call printf, 2
 473:     param "%d | "
 474:     param t90
 475:     call printf, 2
 476:     t93 = &t92
 477:     *t93 = 50
 478:     param "+%d "
 479:     param 50
 480:     call printf, 2
 481:     t95 = *t93
 482:     param "%d | "
 483:     param t95
 484:     call printf, 2
 485:     t97 = &t96
 486:     *t97 = 60
 487:     param "+%d "
 488:     param 60
 489:     call printf, 2
 490:     kept = t96
 491:     t266 = *t97
 492:     param "-%d "
 493:     param t266
 494:     call printf, 2
 495:     t99 = kept[0]
 496:     param "%d\n"
 497:     param t99
 498:     call printf, 2
 499:     t100 = &c
 500:     *t100 = 1
 501:     param "+c%d "
 502:     param 1
 503:     call printf, 2
 504:     param "| "
 505:     call printf, 1
 506:     t102 = &t101
 507:     t271 = *t100
 508:     t272 = t271 int+ 100
 509:     *t102 = t272
 510:     param "copy%d "
 511:     param t272
 512:     call printf, 2
 513:     t273 = t101
 514:     t274 = t273[0]
 515:     t276 = *t102
 516:     param "-c%d "
 517:     param t276
 518:     call printf, 2
 519:     param "%d | "
 520:     param t274
 521:     call printf, 2
 522:     t107 = &t106
 523:     *t107 = 2
 524:     param "+c%d "
 525:     param 2
 526:     call printf, 2
 527:     t279 = t106
 528:     t280 = t279[0]
 529:     t282 = *t107
 530:     param "-c%d "
 531:     param t282
 532:     call printf, 2
 533:     param "%d | "
 534:     param t280
 535:     call printf, 2
 536:     t285 = &t284
 537:     param t285                          (this)
 538:     param 3
 539:     call Copy::Copy(int), 2
 540:     d = t284
 541:     t112 = &d
 542:     t113 = d[0]
 543:     param "%d | "
 544:     param t113
 545:     call printf, 2
 546:     t115 = &t114
 547:     t288 = *t100
 548:     t289 = t288 int+ 100
 549:     *t115 = t289
 550:     param "copy%d "
 551:     param t289
 552:     call printf, 2
 553:     t290 = t114
 554:     t292 = &t291
 555:     t293 = &t290
 556:     param t292                          (this)
 557:     param t293
 558:     call Copy::Copy(const class Copy &), 2
 559:     e = t291
 560:     t119 = &e
 561:     t295 = *t115
 562:     param "-c%d "
 563:     param t295
 564:     call printf, 2
 565:     t121 = e[0]
 566:     param "%d\n"
 567:     param t121
 568:     call printf, 2
 569:     param "%d %d %d %d %d %d\n"
 570:     param 4
 571:     param 0
 572:     param 0
 573:     param 0
 574:     param 2
 575:     param 1
 576:     call printf, 7
 577:     param 3
 578:     param 5
 579:     param 20
 580:     t133 = call mix(long long, long long, int), 3
 581:     param -7
 582:     param 1099511627776
 583:     param 9
 584:     t137 = call mix(long long, long long, int), 3
 585:     param "%lld %lld\n"
 586:     param t133
 587:     param t137
 588:     call printf, 3
 589:     t138 = &inner
 590:     *t138 = 70
 591:     param "+%d "
 592:     param 70
 593:     call printf, 2
 594:     t305 = *t138
 595:     t142 = &t141
 596:     *t142 = 71
 597:     param "+%d "
 598:     param 71
 599:     call printf, 2
 600:     t309 = *t142
 601:     t145 = t305 int+ t309
 602:     param "%d "
 603:     param t145
 604:     call printf, 2
 605:     t311 = *t142
 606:     param "-%d "
 607:     param t311
 608:     call printf, 2
 609:     t313 = *t138
 610:     param "-%d "
 611:     param t313
 612:     call printf, 2
 613:     param "end\n"
 614:     call printf, 1
 615:     t315 = *t119
 616:     param "-c%d "
 617:     param t315
 618:     call printf, 2
 619:     t317 = *t112
 620:     param "-c%d "
 621:     param t317
 622:     call printf, 2
 623:     t319 = *t100
 624:     param "-c%d "
 625:     param t319
 626:     call printf, 2
 627:     t321 = *t93
 628:     param "-%d "
 629:     param t321
 630:     call printf, 2
 631:     t323 = *t81
 632:     param "-%d "
 633:     param t323
 634:     call printf, 2
 635:     t325 = *t27
 636:     param "-%d "
 637:     param t325
 638:     call printf, 2
 639:     t327 = *t20
 640:     param "-%d "
 641:     param t327
 642:     call printf, 2
 643:     return 0


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
Tag                class_tag      class Tag                  -        global                         7     -     0     Tag                  -                        size 4
Tag::id            field          int                        member   global > class Tag             9     4     20    Tag::id              -                        public, offset 0
Tag::Tag           constructor    void (int)                 -        global > class Tag             10    -     18    _ZN3TagC1Ei          _ZN3TagC1Ei              public
Tag::~Tag          destructor     void (void)                -        global > class Tag             11    -     0     _ZN3TagD1Ev          _ZN3TagD1Ev              public
Tag::value         method         int (void)                 -        global > class Tag             12    -     2     _ZN3Tag5valueEv      _ZN3Tag5valueEv          public, defined
Tag::operator+     method         class Tag (const class Tag &) -        global > class Tag             13    -     3     _ZN3TagplERKS_       _ZN3TagplERKS_           public, defined
n                  parameter      int                        param    global > class Tag > Tag()     10    4     1     n.1                  -                        
o                  parameter      const class Tag &          param    global > class Tag > operator+() 13    4     1     o.2                  -                        
Copy               class_tag      class Copy                 -        global                         16    -     0     Copy                 -                        size 4
Copy::id           field          int                        member   global > class Copy            18    4     9     Copy::id             -                        public, offset 0
Copy::Copy         constructor    void (int)                 -        global > class Copy            19    -     3     _ZN4CopyC1Ei         _ZN4CopyC1Ei             public
Copy::Copy         constructor    void (const class Copy &)  -        global > class Copy            20    -     0     _ZN4CopyC1ERKS_      _ZN4CopyC1ERKS_          public
Copy::~Copy        destructor     void (void)                -        global > class Copy            21    -     0     _ZN4CopyD1Ev         _ZN4CopyD1Ev             public
n                  parameter      int                        param    global > class Copy > Copy()   19    4     1     n.3                  -                        
o                  parameter      const class Copy &         param    global > class Copy > Copy()   20    4     1     o.4                  -                        
make               function       class Tag (int)            -        global                         24    -     4     _Z4makei             _Z4makei                 defined
n                  parameter      int                        param    global > make()                24    4     1     n.5                  -                        
named              function       class Tag (int)            -        global                         25    -     1     _Z5namedi            _Z5namedi                defined
n                  parameter      int                        param    global > named()               25    4     1     n.6                  -                        
t                  variable       class Tag                  local    global > named()               26    4     3     t.7                  -                        
pick               function       class Tag (int)            -        global                         30    -     2     _Z4picki             _Z4picki                 defined
which              parameter      int                        param    global > pick()                30    4     1     which.8              -                        
a                  variable       class Tag                  local    global > pick()                31    4     1     a.9                  -                        
b                  variable       class Tag                  local    global > pick()                32    4     1     b.10                 -                        
byValue            function       int (class Tag)            -        global                         36    -     2     _Z7byValue3Tag       _Z7byValue3Tag           defined
t                  parameter      class Tag                  param    global > byValue()             36    4     1     t.11                 -                        
byRef              function       int (const class Tag &)    -        global                         37    -     5     _Z5byRefRK3Tag       _Z5byRefRK3Tag           defined
t                  parameter      const class Tag &          param    global > byRef()               37    4     1     t.12                 -                        
copied             function       int (class Copy)           -        global                         38    -     2     _Z6copied4Copy       _Z6copied4Copy           defined
c                  parameter      class Copy                 param    global > copied()              38    4     1     c.13                 -                        
makeCopy           function       class Copy (int)           -        global                         39    -     1     _Z8makeCopyi         _Z8makeCopyi             defined
n                  parameter      int                        param    global > makeCopy()            39    4     1     n.14                 -                        
sameCopy           function       class Copy (class Copy)    -        global                         40    -     1     _Z8sameCopy4Copy     _Z8sameCopy4Copy         defined
c                  parameter      class Copy                 param    global > sameCopy()            40    4     1     c.15                 -                        
Shape              class_tag      class Shape                -        global                         42    -     0     Shape                -                        size 1
Shape::sides       method         int (void)                 -        global > class Shape           44    -     3     _ZN5Shape5sidesEv    _ZN5Shape5sidesEv        public, defined
Shape::kind        method         int (void)                 -        global > class Shape           45    -     1     _ZN5Shape4kindEv     _ZN5Shape4kindEv         public, defined
Square             class_tag      class Square               -        global                         47    -     0     Square               -                        size 1, public base Shape
Square::sides      method         int (void)                 -        global > class Square          49    -     1     _ZN6Square5sidesEv   _ZN6Square5sidesEv       public, defined
Square::kind       method         int (void)                 -        global > class Square          50    -     1     _ZN6Square4kindEv    _ZN6Square4kindEv        public, defined
mix                function       long long (long long, long long, int) -        global                         53    -     2     _Z3mixxxi            _Z3mixxxi                defined
a                  parameter      long long                  param    global > mix()                 53    8     4     a.16                 -                        
b                  parameter      long long                  param    global > mix()                 53    8     4     b.17                 -                        
n                  parameter      int                        param    global > mix()                 53    4     1     n.18                 -                        
sum                variable       long long                  local    global > mix()                 54    8     5     sum.19               -                        
i                  variable       int                        local    global > mix() > for           55    4     3     i.20                 -                        
main               function       int (void)                 -        global                         63    -     0     main                 main                     defined
v                  variable       int                        local    global > main()                68    4     20    v.21                 -                        
kept               variable       class Tag                  local    global > main()                70    4     6     kept.22              -                        
sum                variable       class Tag                  local    global > main()                72    4     2     sum.23               -                        
i                  variable       int                        local    global > main() > for          84    4     4     i.24                 -                        
n                  variable       class Tag                  local    global > main()                88    4     1     n.25                 -                        
r                  variable       const class Tag &          local    global > main()                93    4     1     r.26                 -                        
c                  variable       class Copy                 local    global > main()                98    4     2     c.27                 -                        
d                  variable       class Copy                 local    global > main()                104   4     1     d.28                 -                        
e                  variable       class Copy                 local    global > main()                106   4     1     e.29                 -                        
q                  variable       class Square               local    global > main()                109   1     5     q.30                 -                        
p                  variable       class Shape *              local    global > main()                110   4     2     p.31                 -                        
m                  variable       long long                  local    global > main()                113   8     1     m.32                 -                        
inner              variable       class Tag                  local    global > main() > block        116   4     1     inner.33             -                        

=== Record Layouts ===
class Tag: size 4, align 4
    +0  int id  [public]
class Copy: size 4, align 4
    +0  int id  [public]
class Shape: size 1, align 1
class Square: size 1, align 1
    (base Shape, public)
