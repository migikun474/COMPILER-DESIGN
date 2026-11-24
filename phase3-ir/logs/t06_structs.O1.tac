============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 109 -> 98 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          109 -> 98   (10% fewer)

   constants folded                        8
   algebraic simplifications               1
   common subexpressions                   2
   copies / constants forwarded           15
   temporaries merged away                 1
   dead instructions removed              10
   jumps removed or redirected             0
   unreachable instructions removed        0

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

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   p                param   Pt                              8       0
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t4               temp    int                             4      20
   t5               temp    int                             4      24
   (1 temporary no longer used after optimization not shown)

 Code: 6 instruction(s)

    105     t1 = p[0]
    106     t2 = t1 int<< 1
    107     p[0] = t2
    108     t4 = p[4]
    109     t5 = t2 int* t4
    110     return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 26 temporaries, frame 396 bytes

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
   t19              temp    struct Out *                    4     292
   t20              temp    struct Out *                    4     296
   t21              temp    int                             4     300
   t25              temp    int                             4     316
   t26              temp    struct Out                     32     320
   t27              temp    int                             4     352
   t28              temp    Pt                              8     356
   t29              temp    int                             4     364
   t31              temp    int                             4     372
   t32              temp    int                             4     376
   t33              temp    int                             4     380
   t34              temp    unsigned int                    4     384
   t35              temp    unsigned char                   1     388
   t36              temp    int                             4     392
   (10 temporaries no longer used after optimization not shown)

 Code: 87 instruction(s)

    111     o[0] = 1
    112     o[4] = 107
    113     o[8] = 5
    114     o[12] = 6
    115     o[16] = 7
    116     o[24] = 2.5
    117     param o
    118     g = call grow(struct Out), 1
    119     t2 = o[0]
    120     t3 = g[0]
    121     t4 = g[4]
    122     t5 = chartoint t4
    123     t6 = g[16]
    124     t7 = o[16]
    125     t8 = t6 int+ t7
    126     t9 = g[24]
    127     param "%d %d %c %d %.1f\n"
    128     param t2
    129     param t3
    130     param t5
    131     param t8
    132     param t9
    133     call printf, 6
    134     p[0] = 3
    135     p[4] = 4
    136     param p
    137     t10 = call area(Pt), 1
    138     t11 = p[0]
    139     param "%d %d\n"
    140     param t10
    141     param t11
    142     call printf, 3
    143     t12 = &os
    144     t13 = t12 ptr+ 32
    145     op = t13
    146     ii = 1
    147     jj = 2
    148     os[48] = 31
    149     t19 = t13 ptr+ 8
    150     t20 = t19 ptr+ 4
    151     *t20 = 17
    152     t21 = os[48]
    153     t25 = os[44]
    154     param o
    155     t26 = call grow(struct Out), 1
    156     t27 = t26[0]
    157     param "%d %d %d\n"
    158     param t21
    159     param t25
    160     param t27
    161     call printf, 4
    162     ps[0] = 1
    163     ps[4] = 2
    164     ps[8] = 3
    165     ps[12] = 4
    166     t28 = ps[0]
    167     ps[8] = t28
    168     ps[4] = 50
    169     t29 = ps[12]
    170     param "%d %d\n"
    171     param t29
    172     param 50
    173     call printf, 3
    174     h[4] = 3
    175     h[8] = 8
    176     h[0] = 1
    177     t31 = h[8]
    178     t32 = h[4]
    179     t33 = t31 int- t32
    180     param "%d %d\n"
    181     param t33
    182     param 12
    183     call printf, 3
    184     param "%d %d\n"
    185     param 8
    186     param 32
    187     call printf, 3
    188     b[0] = 1.0
    189     t34 = b[0]
    190     t35 = b[3]
    191     t36 = uchartoint t35
    192     param "%x %d %d\n"
    193     param t34
    194     param t36
    195     param 4
    196     call printf, 4
    197     return 0


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
