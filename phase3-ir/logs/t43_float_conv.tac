============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t43_float_conv.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 76 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 11 parameter(s)/local(s), 24 temporaries, frame 244 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   d                local   double                          8       0
   e                local   double                          8       8
   f                local   float                           4      16
   i                local   int                             4      20
   h                local   double                          8      24
   q                local   double                          8      32
   third            local   float                           4      40
   u                local   unsigned int                    4      44
   ud               local   double                          8      48
   big              local   double                          8      56
   back             local   int                             4      64
   t1               temp    double                          8      72
   t2               temp    int                             4      80
   t3               temp    int                             4      84
   t4               temp    double                          8      88
   t5               temp    int                             4      96
   t6               temp    int                             4     100
   t7               temp    int                             4     104
   t8               temp    double                          8     112
   t9               temp    double                          8     120
   t10              temp    double                          8     128
   t11              temp    double                          8     136
   t12              temp    float                           4     144
   t13              temp    double                          8     152
   t14              temp    int                             4     160
   t15              temp    double                          8     168
   t16              temp    int                             4     176
   t17              temp    double                          8     184
   t18              temp    int                             4     192
   t19              temp    double                          8     200
   t20              temp    double                          8     208
   t21              temp    unsigned int                    4     216
   t22              temp    double                          8     224
   t23              temp    double                          8     232
   t24              temp    int                             4     240

 Code: 76 instruction(s)

    100       t1 = double- 3.99
    101       d = t1
    102       e = 3.99
    103       f = 2.5
    104       t2 = doubletoint d
    105       t3 = doubletoint e
    106       t4 = double- 0.5
    107       t5 = doubletoint t4
    108       t6 = floattoint f
    109       param "%d %d %d %d\n"
    110       param t2
    111       param t3
    112       param t5
    113       param t6
    114       call printf, 5
    115       i = 7
    116       t7 = i int/ 2
    117       t8 = inttodouble t7
    118       h = t8
    119       t9 = inttodouble i
    120       t10 = t9 double/ 2.0
    121       q = t10
    122       t11 = 1.0 double/ 3.0
    123       param "%.1f %.1f %.3f\n"
    124       param h
    125       param q
    126       param t11
    127       call printf, 4
    128       t12 = 1.0 float/ 3.0
    129       third = t12
    130       t13 = floattodouble third
    131       param "%.6f %.2f %.0f %.0f\n"
    132       param t13
    133       param 2.675
    134       param 0.5
    135       param 1.5
    136       call printf, 5
    137       t15 = inttodouble i
    138       if t15 double< 7.5 goto L1
    139       t14 = 0
    140       goto L2
    141  L1:  t14 = 1
    142  L2:  t17 = inttodouble i
    143       if t17 double== 7.0 goto L3
    144       t16 = 0
    145       goto L4
    146  L3:  t16 = 1
    147  L4:  if 3.0 double> 2.9999 goto L5
    148       t18 = 0
    149       goto L6
    150  L5:  t18 = 1
    151  L6:  param "%d %d %d\n"
    152       param t14
    153       param t16
    154       param t18
    155       call printf, 4
    156       u = 4000000000
    157       t19 = uinttodouble u
    158       ud = t19
    159       t20 = ud double/ 2.0
    160       t21 = doubletouint t20
    161       param "%.0f %u\n"
    162       param ud
    163       param t21
    164       call printf, 3
    165       big = 1e+09
    166       t22 = big double* 2.0
    167       t23 = t22 double/ 3.0
    168       t24 = doubletoint t23
    169       back = t24
    170       param "%d %.2e %g\n"
    171       param back
    172       param 12345.678
    173       param 0.0001
    174       call printf, 4
    175       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           5    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   d                  variable      double                     local       6    8    1  d.1
   e                  variable      double                     local       6    8    1  e.2
   f                  variable      float                      local       7    4    1  f.3
   i                  variable      int                        local       9    4    4  i.4
   h                  variable      double                     local      10    8    1  h.5
   q                  variable      double                     local      10    8    1  q.6
   third              variable      float                      local      12    4    1  third.7
   u                  variable      unsigned int               local      15    4    1  u.8
   ud                 variable      double                     local      16    8    2  ud.9
   big                variable      double                     local      18    8    1  big.10
   back               variable      int                        local      19    4    1  back.11

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
