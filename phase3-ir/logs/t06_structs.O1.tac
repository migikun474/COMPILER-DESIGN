============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 109 -> 110 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          109 -> 110   (0% fewer)

   calls inlined                           3
   constants folded                        8
   algebraic simplifications               1
   common subexpressions                   2
   copies / constants forwarded           16
   temporaries merged away                 1
   dead instructions removed              11
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

 Symbol table: 10 parameter(s)/local(s), 36 temporaries, frame 504 bytes

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
   t37              temp    struct Out                     32     400
   t38              temp    int                             4     432
   t39              temp    int                             4     436
   t40              temp    Pt                              8     440
   t41              temp    int                             4     448
   t42              temp    int                             4     452
   t43              temp    int                             4     456
   t44              temp    int                             4     460
   t45              temp    struct Out                     32     464
   t46              temp    int                             4     496
   t47              temp    int                             4     500
   (11 temporaries no longer used after optimization not shown)

 Code: 99 instruction(s)

    111     o[0] = 1
    112     o[4] = 107
    113     o[8] = 5
    114     o[12] = 6
    115     o[16] = 7
    116     o[24] = 2.5
    117     t37 = o
    118     t38 = t37[0]
    119     t39 = t38 int+ 100
    120     t37[0] = t39
    121     t37[16] = 9
    122     g = t37
    123     t2 = o[0]
    124     t3 = g[0]
    125     t4 = g[4]
    126     t5 = chartoint t4
    127     t6 = g[16]
    128     t7 = o[16]
    129     t8 = t6 int+ t7
    130     t9 = g[24]
    131     param "%d %d %c %d %.1f\n"
    132     param t2
    133     param t3
    134     param t5
    135     param t8
    136     param t9
    137     call printf, 6
    138     p[0] = 3
    139     p[4] = 4
    140     t40 = p
    141     t41 = t40[0]
    142     t42 = t41 int<< 1
    143     t40[0] = t42
    144     t43 = t40[4]
    145     t44 = t42 int* t43
    146     t11 = p[0]
    147     param "%d %d\n"
    148     param t44
    149     param t11
    150     call printf, 3
    151     t12 = &os
    152     t13 = t12 ptr+ 32
    153     op = t13
    154     ii = 1
    155     jj = 2
    156     os[48] = 31
    157     t19 = t13 ptr+ 8
    158     t20 = t19 ptr+ 4
    159     *t20 = 17
    160     t21 = os[48]
    161     t25 = os[44]
    162     t45 = o
    163     t46 = t45[0]
    164     t47 = t46 int+ 100
    165     t45[0] = t47
    166     t45[16] = 9
    167     t26 = t45
    168     t27 = t26[0]
    169     param "%d %d %d\n"
    170     param t21
    171     param t25
    172     param t27
    173     call printf, 4
    174     ps[0] = 1
    175     ps[4] = 2
    176     ps[8] = 3
    177     ps[12] = 4
    178     t28 = ps[0]
    179     ps[8] = t28
    180     ps[4] = 50
    181     t29 = ps[12]
    182     param "%d %d\n"
    183     param t29
    184     param 50
    185     call printf, 3
    186     h[4] = 3
    187     h[8] = 8
    188     h[0] = 1
    189     t31 = h[8]
    190     t32 = h[4]
    191     t33 = t31 int- t32
    192     param "%d %d\n"
    193     param t33
    194     param 12
    195     call printf, 3
    196     param "%d %d\n"
    197     param 8
    198     param 32
    199     call printf, 3
    200     b[0] = 1.0
    201     t34 = b[0]
    202     t35 = b[3]
    203     t36 = uchartoint t35
    204     param "%x %d %d\n"
    205     param t34
    206     param t36
    207     param 4
    208     call printf, 4
    209     return 0


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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

1 101 k 16 2.5
24 3
31 17 101
2 50
5 12
8 32
3f800000 63 4

   exit code 0, 99 instructions executed
