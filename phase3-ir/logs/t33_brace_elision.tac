============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t33_brace_elision.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 106 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 3 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   g                struct S                       24  { +0: 1, +4: 2, +8: 3, +12: 4, +16: 5, +20: 97, +21: 98, +22: 0 }
   pts              struct In[3]                   24  { +0: 1, +4: 2, +8: 3, +12: 4, +16: 5 }
   m                int[2][3]                      24  { +0: 1, +4: 2, +8: 3, +12: 4 }

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 34 temporaries, frame 228 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   s                local   struct S                       24       0
   t                local   struct S                       24      24
   first            local   struct In                       8      48
   u                local   struct (unnamed at 11:5)       12      56
   d                local   struct S                       24      68
   t1               temp    int                             4      92
   t2               temp    int                             4      96
   t3               temp    int                             4     100
   t4               temp    int                             4     104
   t5               temp    int                             4     108
   t6               temp    char (*)[4]                     4     112
   t7               temp    char (*)[4]                     4     116
   t8               temp    int                             4     120
   t9               temp    int                             4     124
   t10              temp    int                             4     128
   t11              temp    int                             4     132
   t12              temp    int                             4     136
   t13              temp    char (*)[4]                     4     140
   t14              temp    char (*)[4]                     4     144
   t15              temp    int                             4     148
   t16              temp    int                             4     152
   t17              temp    int                             4     156
   t18              temp    int                             4     160
   t19              temp    int                             4     164
   t20              temp    char (*)[4]                     4     168
   t21              temp    char (*)[4]                     4     172
   t22              temp    unsigned int                    4     176
   t23              temp    int                             4     180
   t24              temp    int                             4     184
   t25              temp    int                             4     188
   t26              temp    unsigned int                    4     192
   t27              temp    int                             4     196
   t28              temp    int                             4     200
   t29              temp    int                             4     204
   t30              temp    int                             4     208
   t31              temp    int                             4     212
   t32              temp    int                             4     216
   t33              temp    char                            1     220
   t34              temp    int                             4     224

 Code: 106 instruction(s)

    100     s[0] = 1
    101     s[4] = 2
    102     s[8] = 3
    103     s[12] = 4
    104     s[16] = 5
    105     s[20] = 120
    106     s[21] = 121
    107     s[22] = 0
    108     s[23] = 0
    109     t[0] = 7
    110     t[4] = 0
    111     t[8] = 8
    112     t[12] = 9
    113     t[16] = 0
    114     t[20] = 122
    115     t[21] = 0
    116     t[22] = 0
    117     t[23] = 0
    118     first[0] = 6
    119     first[4] = 7
    120     u[0] = first
    121     u[8] = 9
    122     d[0] = 1
    123     d[4] = 2
    124     d[8] = 0
    125     d[12] = 3
    126     d[16] = 4
    127     d[20] = 119
    128     d[21] = 0
    129     d[22] = 0
    130     d[23] = 0
    131     t1 = g[0]
    132     t2 = g[4]
    133     t3 = g[8]
    134     t4 = g[12]
    135     t5 = g[16]
    136     t6 = &g
    137     t7 = t6 ptr+ 20
    138     param "%d %d %d %d %d %s\n"
    139     param t1
    140     param t2
    141     param t3
    142     param t4
    143     param t5
    144     param t7
    145     call printf, 7
    146     t8 = s[0]
    147     t9 = s[4]
    148     t10 = s[8]
    149     t11 = s[12]
    150     t12 = s[16]
    151     t13 = &s
    152     t14 = t13 ptr+ 20
    153     param "%d %d %d %d %d %s\n"
    154     param t8
    155     param t9
    156     param t10
    157     param t11
    158     param t12
    159     param t14
    160     call printf, 7
    161     t15 = t[0]
    162     t16 = t[4]
    163     t17 = t[8]
    164     t18 = t[12]
    165     t19 = t[16]
    166     t20 = &t
    167     t21 = t20 ptr+ 20
    168     param "%d %d %d %d %d %s\n"
    169     param t15
    170     param t16
    171     param t17
    172     param t18
    173     param t19
    174     param t21
    175     call printf, 7
    176     t22 = 24 uint/ 8
    177     t23 = pts[12]
    178     t24 = pts[16]
    179     t25 = pts[20]
    180     t26 = 24 uint/ 12
    181     param "%d %d %d %d %d\n"
    182     param t22
    183     param t23
    184     param t24
    185     param t25
    186     param t26
    187     call printf, 6
    188     t27 = u[0]
    189     t28 = u[4]
    190     t29 = u[8]
    191     t30 = m[12]
    192     t31 = m[20]
    193     t32 = d[16]
    194     t33 = d[20]
    195     t34 = chartoint t33
    196     param "%d %d %d %d %d %d %d\n"
    197     param t27
    198     param t28
    199     param t29
    200     param t30
    201     param t31
    202     param t32
    203     param t34
    204     call printf, 8
    205     return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   In                 struct_tag    struct In                  -           2    -    0  size 8
   S                  struct_tag    struct S                   -           3    -    0  size 24
   g                  variable      struct S                   global      4   24    6  
   pts                variable      struct In[3]               global      5   24    5  
   m                  variable      int[2][3]                  global      6   24    4  
   main               function      int (void)                 -           7    -    0  defined

 scope: global > struct In
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member      2    4    5  In::x; public, offset 0
   y                  field         int                        member      2    4    7  In::y; public, offset 4

 scope: global > struct S
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  field         int[2]                     member      3    8    6  S::a; public, offset 0
   b                  field         int                        member      3    4    3  S::b; public, offset 8
   in                 field         struct In                  member      3    8    7  S::in; public, offset 12
   name               field         char[4]                    member      3    4    4  S::name; public, offset 20

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   s                  variable      struct S                   local       8   24    6  s.1
   t                  variable      struct S                   local       9   24    6  t.2
   first              variable      struct In                  local      10    8    2  first.3
   (unnamed at 11:5)  struct_tag    struct (unnamed at 11:5)   -          11    -    0  size 12
   u                  variable      struct (unnamed at 11:5)   local      11   12    3  u.4
   d                  variable      struct S                   local      12   24    2  d.5

 scope: global > main() > struct (unnamed at 11:5)
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   p                  field         struct In                  member     11    8    2  (unnamed at 11:5)::p; public, offset 0
   z                  field         int                        member     11    4    1  (unnamed at 11:5)::z; public, offset 8

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

struct In: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
struct S: size 24, align 4
    +0  int[2] a  [public]
    +8  int b  [public]
    +12  struct In in  [public]
    +20  char[4] name  [public]
struct (unnamed at 11:5): size 12, align 4
    +0  struct In p  [public]
    +8  int z  [public]
