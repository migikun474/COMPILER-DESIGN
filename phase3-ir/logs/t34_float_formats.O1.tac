============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t34_float_formats.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 63 -> 39 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                           63 -> 39   (38% fewer)

   calls inlined                           0
   constants folded                        4
   algebraic simplifications              10
   common subexpressions                  18
   copies / constants forwarded           25
   temporaries merged away                 1
   dead instructions removed              22
   jumps removed or redirected             1
   unreachable instructions removed        0

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 2 temporaries, frame 320 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                local   double[13]                    104       0
   n                local   int                             4     104
   i                local   int                             4     108
   f                local   float                           4     112
   t2               temp    int                             4     128
   t3               temp    double                          8     136
   (23 temporaries no longer used after optimization not shown)

 Code: 39 instruction(s)

    100       v[0] = 1234.5678
    101       v[8] = 0.000123456
    102       v[16] = 1.0
    103       v[24] = 0.0
    104       v[32] = -98765.4321
    105       v[40] = 9.9999996
    106       v[48] = 123456789.0
    107       v[56] = 0.5
    108       v[64] = 1e+05
    109       v[72] = 1e+06
    110       v[80] = 0.0001
    111       v[88] = 1.234e-05
    112       v[96] = 3.14159265
    113       n = 13
    114       i = 0
    115  L1:  if i int>= n goto L2
    116       t2 = i int<< 3                      (w = 8)
    117       t3 = v[t2]
    118       param "[%e] [%E] [%.2e] [%.0e] [%g] [%G] [%.3g] [%12.4e] [%-12g] [%012.3e]\n"
    119       param t3
    120       param t3
    121       param t3
    122       param t3
    123       param t3
    124       param t3
    125       param t3
    126       param t3
    127       param t3
    128       param t3
    129       call printf, 11
    130       i = i int+ 1
    131       goto L1
    132  L2:  f = 2.5
    133       param "%e %g %f\n"
    134       param 2.5
    135       param 2.5
    136       param 2.5
    137       call printf, 4
    138       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   main               function      int (void)                 -           4    -    0  defined

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  variable      double[13]                 local       5  104   10  v.1
   n                  variable      int                        local       6    4    1  n.2
   f                  variable      float                      local       9    4    3  f.4

 scope: global > main() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local       7    4   12  i.3

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)

----------------------------------------------------------------------------
 PROGRAM OUTPUT (the TAC run by the interpreter)
----------------------------------------------------------------------------

[1.234568e+03] [1.234568E+03] [1.23e+03] [1e+03] [1234.57] [1234.57] [1.23e+03] [  1.2346e+03] [1234.57     ] [0001.235e+03]
[1.234560e-04] [1.234560E-04] [1.23e-04] [1e-04] [0.000123456] [0.000123456] [0.000123] [  1.2346e-04] [0.000123456 ] [0001.235e-04]
[1.000000e+00] [1.000000E+00] [1.00e+00] [1e+00] [1] [1] [1] [  1.0000e+00] [1           ] [0001.000e+00]
[0.000000e+00] [0.000000E+00] [0.00e+00] [0e+00] [0] [0] [0] [  0.0000e+00] [0           ] [0000.000e+00]
[-9.876543e+04] [-9.876543E+04] [-9.88e+04] [-1e+05] [-98765.4] [-98765.4] [-9.88e+04] [ -9.8765e+04] [-98765.4    ] [-009.877e+04]
[1.000000e+01] [1.000000E+01] [1.00e+01] [1e+01] [10] [10] [10] [  1.0000e+01] [10          ] [0001.000e+01]
[1.234568e+08] [1.234568E+08] [1.23e+08] [1e+08] [1.23457e+08] [1.23457E+08] [1.23e+08] [  1.2346e+08] [1.23457e+08 ] [0001.235e+08]
[5.000000e-01] [5.000000E-01] [5.00e-01] [5e-01] [0.5] [0.5] [0.5] [  5.0000e-01] [0.5         ] [0005.000e-01]
[1.000000e+05] [1.000000E+05] [1.00e+05] [1e+05] [100000] [100000] [1e+05] [  1.0000e+05] [100000      ] [0001.000e+05]
[1.000000e+06] [1.000000E+06] [1.00e+06] [1e+06] [1e+06] [1E+06] [1e+06] [  1.0000e+06] [1e+06       ] [0001.000e+06]
[1.000000e-04] [1.000000E-04] [1.00e-04] [1e-04] [0.0001] [0.0001] [0.0001] [  1.0000e-04] [0.0001      ] [0001.000e-04]
[1.234000e-05] [1.234000E-05] [1.23e-05] [1e-05] [1.234e-05] [1.234E-05] [1.23e-05] [  1.2340e-05] [1.234e-05   ] [0001.234e-05]
[3.141593e+00] [3.141593E+00] [3.14e+00] [3e+00] [3.14159] [3.14159] [3.14] [  3.1416e+00] [3.14159     ] [0003.142e+00]
2.500000e+00 2.5 2.500000

   exit code 0, 244 instructions executed
