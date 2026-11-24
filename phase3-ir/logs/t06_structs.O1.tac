============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t06_structs.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 100 -> 101 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          100 -> 101   (-1% fewer)

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

 Symbol table: 9 parameter(s)/local(s), 33 temporaries, frame 480 bytes

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
   t2               temp    int                             4     208
   t3               temp    int                             4     212
   t4               temp    char                            1     216
   t5               temp    int                             4     220
   t6               temp    int                             4     224
   t7               temp    int                             4     228
   t8               temp    int                             4     232
   t9               temp    double                          8     240
   t11              temp    int                             4     252
   t12              temp    struct Out *                    4     256
   t13              temp    struct Out *                    4     260
   t19              temp    struct Out *                    4     284
   t20              temp    struct Out *                    4     288
   t21              temp    int                             4     292
   t25              temp    int                             4     308
   t26              temp    struct Out                     32     312
   t27              temp    int                             4     344
   t28              temp    Pt                              8     348
   t29              temp    int                             4     356
   t31              temp    int                             4     364
   t32              temp    int                             4     368
   t33              temp    int                             4     372
   t34              temp    struct Out                     32     376
   t35              temp    int                             4     408
   t36              temp    int                             4     412
   t37              temp    Pt                              8     416
   t38              temp    int                             4     424
   t39              temp    int                             4     428
   t40              temp    int                             4     432
   t41              temp    int                             4     436
   t42              temp    struct Out                     32     440
   t43              temp    int                             4     472
   t44              temp    int                             4     476
   (11 temporaries no longer used after optimization not shown)

 Code: 90 instruction(s)

    111     o[0] = 1
    112     o[4] = 107
    113     o[8] = 5
    114     o[12] = 6
    115     o[16] = 7
    116     o[24] = 2.5
    117     t34 = o
    118     t35 = t34[0]
    119     t36 = t35 int+ 100
    120     t34[0] = t36
    121     t34[16] = 9
    122     g = t34
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
    140     t37 = p
    141     t38 = t37[0]
    142     t39 = t38 int<< 1
    143     t37[0] = t39
    144     t40 = t37[4]
    145     t41 = t39 int* t40
    146     t11 = p[0]
    147     param "%d %d\n"
    148     param t41
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
    162     t42 = o
    163     t43 = t42[0]
    164     t44 = t43 int+ 100
    165     t42[0] = t44
    166     t42[16] = 9
    167     t26 = t42
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
    200     return 0


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
   grow               function      struct Out (struct Out)    -          10    -    2  _Z4grow3Out; defined
   area               function      int (Pt)                   -          11    -    1  _Z4area2Pt; defined
   main               function      int (void)                 -          12    -    0  defined

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

 scope: global > grow()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     struct Out                 param      10   32    3  o.1

 scope: global > area()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  parameter     Pt                         param      11    8    4  p.2

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  variable      struct Out                 local      13   32    4  o.3
   g                  variable      struct Out                 local      14   32    4  g.4
   p                  variable      Pt                         local      16    8    2  p.5
   os                 variable      struct Out[2]              local      18   64    4  os.6
   op                 variable      struct Out *               local      19    4    1  op.7
   ii                 variable      int                        local      20    4    3  ii.8
   jj                 variable      int                        local      20    4    1  jj.9
   ps                 variable      Pt[2]                      local      24   16    5  ps.10
   h                  variable      struct Holder              local      28   12    5  h.11

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

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

1 101 k 16 2.5
24 3
31 17 101
2 50
5 12
8 32

   exit code 0, 90 instructions executed
