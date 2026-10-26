============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t34_float_formats.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 63 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 25 temporaries, frame 320 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                local   double[13]                    104       0
   n                local   int                             4     104
   i                local   int                             4     108
   f                local   float                           4     112
   t1               temp    double                          8     120
   t2               temp    int                             4     128
   t3               temp    double                          8     136
   t4               temp    int                             4     144
   t5               temp    double                          8     152
   t6               temp    int                             4     160
   t7               temp    double                          8     168
   t8               temp    int                             4     176
   t9               temp    double                          8     184
   t10              temp    int                             4     192
   t11              temp    double                          8     200
   t12              temp    int                             4     208
   t13              temp    double                          8     216
   t14              temp    int                             4     224
   t15              temp    double                          8     232
   t16              temp    int                             4     240
   t17              temp    double                          8     248
   t18              temp    int                             4     256
   t19              temp    double                          8     264
   t20              temp    int                             4     272
   t21              temp    double                          8     280
   t22              temp    int                             4     288
   t23              temp    double                          8     296
   t24              temp    double                          8     304
   t25              temp    double                          8     312

 Code: 63 instruction(s)

    100       t1 = double- 98765.4321
    101       v[0] = 1234.5678
    102       v[8] = 0.000123456
    103       v[16] = 1.0
    104       v[24] = 0.0
    105       v[32] = t1
    106       v[40] = 9.9999996
    107       v[48] = 123456789.0
    108       v[56] = 0.5
    109       v[64] = 1e+05
    110       v[72] = 1e+06
    111       v[80] = 0.0001
    112       v[88] = 1.234e-05
    113       v[96] = 3.14159265
    114       n = 13
    115       i = 0
    116  L1:  if i int< n goto L2
    117       goto L3
    118  L2:  t2 = i int* 8                       (w = 8)
    119       t3 = v[t2]
    120       t4 = i int* 8                       (w = 8)
    121       t5 = v[t4]
    122       t6 = i int* 8                       (w = 8)
    123       t7 = v[t6]
    124       t8 = i int* 8                       (w = 8)
    125       t9 = v[t8]
    126       t10 = i int* 8                      (w = 8)
    127       t11 = v[t10]
    128       t12 = i int* 8                      (w = 8)
    129       t13 = v[t12]
    130       t14 = i int* 8                      (w = 8)
    131       t15 = v[t14]
    132       t16 = i int* 8                      (w = 8)
    133       t17 = v[t16]
    134       t18 = i int* 8                      (w = 8)
    135       t19 = v[t18]
    136       t20 = i int* 8                      (w = 8)
    137       t21 = v[t20]
    138       param "[%e] [%E] [%.2e] [%.0e] [%g] [%G] [%.3g] [%12.4e] [%-12g] [%012.3e]\n"
    139       param t3
    140       param t5
    141       param t7
    142       param t9
    143       param t11
    144       param t13
    145       param t15
    146       param t17
    147       param t19
    148       param t21
    149       call printf, 11
    150       t22 = i int+ 1
    151       i = t22
    152       goto L1
    153  L3:  f = 2.5
    154       t23 = floattodouble f
    155       t24 = floattodouble f
    156       t25 = floattodouble f
    157       param "%e %g %f\n"
    158       param t23
    159       param t24
    160       param t25
    161       call printf, 4
    162       return 0


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
   v                  variable      double[13]                 local       6  104   10  v.1
   n                  variable      int                        local       7    4    1  n.2
   f                  variable      float                      local      10    4    3  f.4

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       8    4   12  i.3

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
