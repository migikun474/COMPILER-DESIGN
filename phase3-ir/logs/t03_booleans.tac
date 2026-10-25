============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t03_booleans.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 234 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   calls            int                             4  0

 As three address code (initial values, in place before main runs):

    calls = 0

============================================================================
 FUNCTION yes()        (link name _Z3yesv)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    100     t1 = calls int+ 1
    101     calls = t1
    102     return 1

============================================================================
 FUNCTION no()        (link name _Z2nov)
============================================================================

 Symbol table: 0 parameter(s)/local(s), 1 temporary, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   t1               temp    int                             4       0

 Code: 3 instruction(s)

    103     t1 = calls int+ 1
    104     calls = t1
    105     return 0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 15 parameter(s)/local(s), 37 temporaries, frame 208 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   d                local   int                             4      12
   e                local   int                             4      16
   f                local   int                             4      20
   r                local   int                             4      24
   x                local   int                             4      28
   z                local   double                          8      32
   ch               local   char                            1      40
   p                local   int *                           4      44
   flag             local   bool                            1      48
   both             local   bool                            1      49
   big              local   unsigned int                    4      52
   minus            local   int                             4      56
   t1               temp    int                             4      60
   t2               temp    int                             4      64
   t3               temp    int                             4      68
   t4               temp    int                             4      72
   t5               temp    int                             4      76
   t6               temp    int                             4      80
   t7               temp    int                             4      84
   t8               temp    int                             4      88
   t9               temp    int                             4      92
   t10              temp    int                             4      96
   t11              temp    int                             4     100
   t12              temp    int                             4     104
   t13              temp    int                             4     108
   t14              temp    int                             4     112
   t15              temp    int                             4     116
   t16              temp    int                             4     120
   t17              temp    int                             4     124
   t18              temp    int                             4     128
   t19              temp    int                             4     132
   t20              temp    int                             4     136
   t21              temp    int                             4     140
   t22              temp    int                             4     144
   t23              temp    int                             4     148
   t24              temp    int                             4     152
   t25              temp    int                             4     156
   t26              temp    int                             4     160
   t27              temp    int                             4     164
   t28              temp    int                             4     168
   t29              temp    bool                            1     172
   t30              temp    int                             4     176
   t31              temp    bool                            1     180
   t32              temp    int                             4     184
   t33              temp    int                             4     188
   t34              temp    int                             4     192
   t35              temp    int                             4     196
   t36              temp    int                             4     200
   t37              temp    int                             4     204

 Code: 228 instruction(s)

    106        a = 1
    107        b = 2
    108        c = 3
    109        d = 4
    110        e = 5
    111        f = 6
    112        if a int< b goto L4
    113        goto L1
    114  L1:   if c int< d goto L2
    115        goto L3
    116  L2:   if e int< f goto L4
    117        goto L3
    118  L3:   t1 = 0
    119        goto L5
    120  L4:   t1 = 1
    121  L5:   r = t1
    122        param "%d\n"
    123        param r
    124        call printf, 2
    125        if a int> b goto L6
    126        t2 = 0
    127        goto L7
    128  L6:   t2 = 1
    129  L7:   r = t2
    130        if a int< b goto L8
    131        t3 = 0
    132        goto L9
    133  L8:   t3 = 1
    134  L9:   if a int== 1 goto L10
    135        t4 = 0
    136        goto L11
    137  L10:  t4 = 1
    138  L11:  if a int!= 1 goto L12
    139        t5 = 0
    140        goto L13
    141  L12:  t5 = 1
    142  L13:  if b int>= 2 goto L14
    143        t6 = 0
    144        goto L15
    145  L14:  t6 = 1
    146  L15:  if b int<= 1 goto L16
    147        t7 = 0
    148        goto L17
    149  L16:  t7 = 1
    150  L17:  param "%d %d %d %d %d %d\n"
    151        param r
    152        param t3
    153        param t4
    154        param t5
    155        param t6
    156        param t7
    157        call printf, 7
    158        calls = 0
    159        t8 = call no(), 0
    160        if t8 int!= 0 goto L18
    161        goto L20
    162  L18:  t9 = call yes(), 0
    163        if t9 int!= 0 goto L19
    164        goto L20
    165  L19:  param "no\n"
    166        call printf, 1
    167  L20:  param "calls after &&: %d\n"
    168        param calls
    169        call printf, 2
    170        calls = 0
    171        t10 = call yes(), 0
    172        if t10 int!= 0 goto L22
    173        goto L21
    174  L21:  t11 = call no(), 0
    175        if t11 int!= 0 goto L22
    176        goto L23
    177  L22:  param "or taken\n"
    178        call printf, 1
    179  L23:  param "calls after ||: %d\n"
    180        param calls
    181        call printf, 2
    182        calls = 0
    183        t13 = call no(), 0
    184        if t13 int!= 0 goto L25
    185        goto L24
    186  L24:  t14 = call yes(), 0
    187        if t14 int!= 0 goto L25
    188        goto L26
    189  L25:  t15 = call no(), 0
    190        if t15 int!= 0 goto L26
    191        goto L27
    192  L26:  t12 = 0
    193        goto L28
    194  L27:  t12 = 1
    195  L28:  r = t12
    196        param "%d %d\n"
    197        param r
    198        param calls
    199        call printf, 3
    200        x = 0
    201        z = 0.5
    202        ch = 0
    203        p = 0
    204        if x int!= 0 goto L29
    205        goto L30
    206  L29:  t16 = 0
    207        goto L31
    208  L30:  t16 = 1
    209  L31:  if z double!= 0.0 goto L32
    210        goto L33
    211  L32:  t17 = 0
    212        goto L34
    213  L33:  t17 = 1
    214  L34:  if ch char!= 0 goto L35
    215        goto L36
    216  L35:  t18 = 0
    217        goto L37
    218  L36:  t18 = 1
    219  L37:  if p ptr!= 0 goto L38
    220        goto L39
    221  L38:  t19 = 0
    222        goto L40
    223  L39:  t19 = 1
    224  L40:  if c int!= 0 goto L42
    225        goto L41
    226  L41:  t20 = 0
    227        goto L43
    228  L42:  t20 = 1
    229  L43:  param "%d %d %d %d %d\n"
    230        param t16
    231        param t17
    232        param t18
    233        param t19
    234        param t20
    235        call printf, 6
    236        if z double!= 0.0 goto L44
    237        goto L45
    238  L44:  param "double is true\n"
    239        call printf, 1
    240  L45:  if p ptr!= 0 goto L47
    241        goto L46
    242  L46:  param "null pointer is false\n"
    243        call printf, 1
    244  L47:  if a int< b goto L48
    245        t21 = 0
    246        goto L49
    247  L48:  t21 = 1
    248  L49:  if b int< c goto L50
    249        t22 = 0
    250        goto L51
    251  L50:  t22 = 1
    252  L51:  t23 = t21 int+ t22
    253        if c int< a goto L52
    254        t24 = 0
    255        goto L53
    256  L52:  t24 = 1
    257  L53:  t25 = t23 int+ t24
    258        r = t25
    259        param "%d\n"
    260        param r
    261        call printf, 2
    262        if a int!= 0 goto L54
    263        goto L55
    264  L54:  if b int!= 0 goto L56
    265        goto L55
    266  L55:  t26 = 0
    267        goto L57
    268  L56:  t26 = 1
    269  L57:  r = t26
    270        if x int!= 0 goto L60
    271        goto L58
    272  L58:  if ch char!= 0 goto L60
    273        goto L59
    274  L59:  t27 = 0
    275        goto L61
    276  L60:  t27 = 1
    277  L61:  param "%d %d\n"
    278        param r
    279        param t27
    280        call printf, 3
    281        if c int> a goto L62
    282        t28 = 0
    283        goto L63
    284  L62:  t28 = 1
    285  L63:  if t28 int!= 0 goto L64
    286        t29 = 0
    287        goto L65
    288  L64:  t29 = 1
    289  L65:  flag = t29
    290        if flag bool!= 0 goto L66
    291        goto L67
    292  L66:  if d int!= 0 goto L68
    293        goto L67
    294  L67:  t30 = 0
    295        goto L69
    296  L68:  t30 = 1
    297  L69:  if t30 int!= 0 goto L70
    298        t31 = 0
    299        goto L71
    300  L70:  t31 = 1
    301  L71:  both = t31
    302        t32 = booltoint flag
    303        t33 = booltoint both
    304        param "%d %d\n"
    305        param t32
    306        param t33
    307        call printf, 3
    308  L72:  if x int< 3 goto L73
    309        goto L75
    310  L73:  if x int== 2 goto L75
    311        goto L74
    312  L74:  t34 = x int+ 1
    313        x = t34
    314        goto L72
    315  L75:  param "%d\n"
    316        param x
    317        call printf, 2
    318        big = 4000000000
    319        t35 = int- 1
    320        minus = t35
    321        if big uint> 5 goto L76
    322        t36 = 0
    323        goto L77
    324  L76:  t36 = 1
    325  L77:  if minus int< 0 goto L78
    326        t37 = 0
    327        goto L79
    328  L78:  t37 = 1
    329  L79:  param "%d %d\n"
    330        param t36
    331        param t37
    332        call printf, 3
    333        return r


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   calls              variable      int                        global      4    4    8  
   yes                function      int (void)                 -           5    -    3  _Z3yesv; defined
   no                 function      int (void)                 -           6    -    4  _Z2nov; defined
   main               function      int (void)                 -           8    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local       9    4    9  a.1
   b                  variable      int                        local       9    4    8  b.2
   c                  variable      int                        local       9    4    5  c.3
   d                  variable      int                        local       9    4    2  d.4
   e                  variable      int                        local       9    4    1  e.5
   f                  variable      int                        local       9    4    1  f.6
   r                  variable      int                        local      10    4   10  r.7
   x                  variable      int                        local      25    4    6  x.8
   z                  variable      double                     local      26    8    2  z.9
   ch                 variable      char                       local      27    1    2  ch.10
   p                  variable      int *                      local      28    4    2  p.11
   flag               variable      bool                       local      36    1    2  flag.12
   both               variable      bool                       local      37    1    1  both.13
   big                variable      unsigned int               local      41    4    1  big.14
   minus              variable      int                        local      42    4    1  minus.15

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
