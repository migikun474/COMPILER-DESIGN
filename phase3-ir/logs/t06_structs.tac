============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 109 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION grow(struct Out)        (link name _Z4grow3Out)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   o                param   struct Out                     32       0
   t1               temp    int                             4      32
   t2               temp    int                             4      36

 Code: 5 instruction(s)

    100     t1 = o[0]
    101     t2 = t1 int+ 100
    102     o[0] = t2
    103     o[16] = 9
    104     return o

============================================================================
 FUNCTION area(Pt)        (link name _Z4area2Pt)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   Pt                              8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24

 Code: 7 instruction(s)

    105     t1 = p[0]
    106     t2 = t1 int* 2
    107     p[0] = t2
    108     t3 = p[0]
    109     t4 = p[4]
    110     t5 = t3 int* t4
    111     return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 36 temporaries, frame 396 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   o                local   struct Out                     32       0
   g                local   struct Out                     32      32
   p                local   Pt                              8      64
   os               local   struct Out[2]                  64      72
   op               local   struct Out *                    4     136
   ii               local   int                             4     140
   jj               local   int                             4     144
   ps               local   Pt[2]                          16     148
   h                local   struct Holder                  12     164
   b                local   union Bits                      4     176
   t1               temp    struct Out                     32     184
   t2               temp    int                             4     216
   t3               temp    int                             4     220
   t4               temp    char                            1     224
   t5               temp    int                             4     228
   t6               temp    int                             4     232
   t7               temp    int                             4     236
   t8               temp    int                             4     240
   t9               temp    double                          8     248
   t10              temp    int                             4     256
   t11              temp    int                             4     260
   t12              temp    struct Out *                    4     264
   t13              temp    struct Out *                    4     268
   t14              temp    int                             4     272
   t15              temp    int                             4     276
   t16              temp    int                             4     280
   t17              temp    int                             4     284
   t18              temp    int                             4     288
   t19              temp    struct Out *                    4     292
   t20              temp    struct Out *                    4     296
   t21              temp    int                             4     300
   t22              temp    int                             4     304
   t23              temp    int                             4     308
   t24              temp    int                             4     312
   t25              temp    int                             4     316
   t26              temp    struct Out                     32     320
   t27              temp    int                             4     352
   t28              temp    Pt                              8     356
   t29              temp    int                             4     364
   t30              temp    int                             4     368
   t31              temp    int                             4     372
   t32              temp    int                             4     376
   t33              temp    int                             4     380
   t34              temp    unsigned int                    4     384
   t35              temp    unsigned char                   1     388
   t36              temp    int                             4     392

 Code: 97 instruction(s)

    112     o[0] = 1
    113     o[4] = 107
    114     o[8] = 5
    115     o[12] = 6
    116     o[16] = 7
    117     o[24] = 2.5
    118     param o
    119     t1 = call grow(struct Out), 1
    120     g = t1
    121     t2 = o[0]
    122     t3 = g[0]
    123     t4 = g[4]
    124     t5 = chartoint t4
    125     t6 = g[16]
    126     t7 = o[16]
    127     t8 = t6 int+ t7
    128     t9 = g[24]
    129     param "%d %d %c %d %.1f\n"
    130     param t2
    131     param t3
    132     param t5
    133     param t8
    134     param t9
    135     call printf, 6
    136     p[0] = 3
    137     p[4] = 4
    138     param p
    139     t10 = call area(Pt), 1
    140     t11 = p[0]
    141     param "%d %d\n"
    142     param t10
    143     param t11
    144     call printf, 3
    145     t12 = &os
    146     t13 = t12 ptr+ 32
    147     op = t13
    148     ii = 1
    149     jj = 2
    150     t14 = ii int* 32                    (w = 32)
    151     t15 = t14 int+ 8
    152     t16 = jj int* 4                     (w = 4)
    153     t17 = t15 int+ t16
    154     os[t17] = 31
    155     t18 = ii int* 4                     (w = 4)
    156     t19 = op ptr+ 8
    157     t20 = t19 ptr+ t18
    158     *t20 = 17
    159     t21 = os[48]
    160     t22 = ii int* 32                    (w = 32)
    161     t23 = t22 int+ 8
    162     t24 = t23 int+ 4
    163     t25 = os[t24]
    164     param o
    165     t26 = call grow(struct Out), 1
    166     t27 = t26[0]
    167     param "%d %d %d\n"
    168     param t21
    169     param t25
    170     param t27
    171     call printf, 4
    172     ps[0] = 1
    173     ps[4] = 2
    174     ps[8] = 3
    175     ps[12] = 4
    176     t28 = ps[0]
    177     ps[8] = t28
    178     ps[4] = 50
    179     t29 = ps[12]
    180     t30 = ps[4]
    181     param "%d %d\n"
    182     param t29
    183     param t30
    184     call printf, 3
    185     h[4] = 3
    186     h[8] = 8
    187     h[0] = 1
    188     t31 = h[8]
    189     t32 = h[4]
    190     t33 = t31 int- t32
    191     param "%d %d\n"
    192     param t33
    193     param 12
    194     call printf, 3
    195     param "%d %d\n"
    196     param 8
    197     param 32
    198     call printf, 3
    199     b[0] = 1.0
    200     t34 = b[0]
    201     t35 = b[3]
    202     t36 = uchartoint t35
    203     param "%x %d %d\n"
    204     param t34
    205     param t36
    206     param 4
    207     call printf, 4
    208     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   In                 struct_tag    struct In                  -           6    -    0  size 8
   Out                struct_tag    struct Out                 -           7    -    0  size 32
   (unnamed at 8:9)   struct_tag    struct (unnamed at 8:9)    -           8    -    0  size 8
   Pt                 typedef       Pt                         -           8    -    0  
   Holder             struct_tag    struct Holder              -           9    -    0  size 12
   (unnamed at 9:25)  struct_tag    struct (unnamed at 9:25)   -           9    -    0  size 8
   Bits               union_tag     union Bits                 -          10    -    0  size 4
   grow               function      struct Out (struct Out)    -          11    -    2  _Z4grow3Out; defined
   area               function      int (Pt)                   -          12    -    1  _Z4area2Pt; defined
   main               function      int (void)                 -          13    -    0  defined

 scope: global > struct In
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int                        member      6    4    4  In::a; public, offset 0
   tag                field         char                       member      6    1    1  In::tag; public, offset 4

 scope: global > struct Out
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   in                 field         struct In                  member      7    8    5  Out::in; public, offset 0
   list               field         int[3]                     member      7   12    7  Out::list; public, offset 8
   w                  field         double                     member      7    8    1  Out::w; public, offset 24

 scope: global > struct (unnamed at 8:9)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      8    4    4  (unnamed at 8:9)::x; public, offset 0
   y                  field         int                        member      8    4    4  (unnamed at 8:9)::y; public, offset 4

 scope: global > struct Holder
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member      9    4    1  Holder::id; public, offset 0
   (unnamed)          field         struct (unnamed at 9:25)   member      9    8    0  Holder::(unnamed at 9:25); public, offset 4

 scope: global > struct Holder > struct (unnamed at 9:25)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   lo                 field         int                        member      9    4    0  (unnamed at 9:25)::lo; public, offset 0
   hi                 field         int                        member      9    4    0  (unnamed at 9:25)::hi; public, offset 4

 scope: global > union Bits
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   f                  field         float                      member     10    4    1  Bits::f; public, offset 0
   u                  field         unsigned int               member     10    4    1  Bits::u; public, offset 0
   b                  field         unsigned char[4]           member     10    4    1  Bits::b; public, offset 0

 scope: global > grow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     struct Out                 param      11   32    3  o.1

 scope: global > area()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     Pt                         param      12    8    4  p.2

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  variable      struct Out                 local      14   32    4  o.3
   g                  variable      struct Out                 local      15   32    4  g.4
   p                  variable      Pt                         local      17    8    2  p.5
   os                 variable      struct Out[2]              local      19   64    4  os.6
   op                 variable      struct Out *               local      20    4    1  op.7
   ii                 variable      int                        local      21    4    3  ii.8
   jj                 variable      int                        local      21    4    1  jj.9
   ps                 variable      Pt[2]                      local      25   16    5  ps.10
   h                  variable      struct Holder              local      29   12    5  h.11
   b                  variable      union Bits                 local      33    4    3  b.12

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct In: size 8, align 4
    +0  int a  [public]
    +4  char tag  [public]
struct Out: size 32, align 8
    +0  struct In in  [public]
    +8  int[3] list  [public]
    +24  double w  [public]
struct (unnamed at 8:9): size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
struct Holder: size 12, align 4
    +0  int id  [public]
    +4  struct (unnamed at 9:25)   [public]
    +4  int lo  [public]  (from the unnamed member)
    +8  int hi  [public]  (from the unnamed member)
struct (unnamed at 9:25): size 8, align 4
    +0  int lo  [public]
    +4  int hi  [public]
union Bits: size 4, align 4
    +0  float f  [public]
    +0  unsigned int u  [public]
    +0  unsigned char[4] b  [public]
