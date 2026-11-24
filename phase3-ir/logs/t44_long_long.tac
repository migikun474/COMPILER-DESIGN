============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t44_long_long.c
   Optimization  : no optimization
   Result        : Three address code generated: 2 function(s), 88 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION mulAdd(long long, long long, long long)        (link name _Z6mulAddxxx)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 2 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   long long                       8       0
   b                param   long long                       8       8
   c                param   long long                       8      16
   t1               temp    long long                       8      24
   t2               temp    long long                       8      32

 Code: 3 instruction(s)

    100     t1 = a llong* b
    101     t2 = t1 llong+ c
    102     return t2

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 24 temporaries, frame 264 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   long long                       8       0
   b                local   long long                       8       8
   m                local   long long                       8      16
   x                local   long long                       8      24
   neg              local   long long                       8      32
   big              local   unsigned long long              8      40
   dd               local   double                          8      48
   back             local   long long                       8      56
   keep             local   long long                       8      64
   r                local   long long                       8      72
   t1               temp    long long                       8      80
   t2               temp    long long                       8      88
   t3               temp    long long                       8      96
   t4               temp    long long                       8     104
   t5               temp    long long                       8     112
   t6               temp    long long                       8     120
   t7               temp    long long                       8     128
   t8               temp    long long                       8     136
   t9               temp    long long                       8     144
   t10              temp    long long                       8     152
   t11              temp    long long                       8     160
   t12              temp    long long                       8     168
   t13              temp    long long                       8     176
   t14              temp    long long                       8     184
   t15              temp    unsigned long long              8     192
   t16              temp    int                             4     200
   t17              temp    int                             4     204
   t18              temp    int                             4     208
   t19              temp    long long                       8     216
   t20              temp    double                          8     224
   t21              temp    double                          8     232
   t22              temp    long long                       8     240
   t23              temp    long long                       8     248
   t24              temp    long long                       8     256

 Code: 85 instruction(s)

    103       a = 4294967295
    104       b = 1
    105       t1 = a llong+ b
    106       t2 = a llong+ b
    107       t3 = llong- t2
    108       param "%lld %lld\n"
    109       param t1
    110       param t3
    111       call printf, 3
    112       t4 = llong- 7
    113       param 123456789
    114       param 1000003
    115       param t4
    116       t5 = call mulAdd(long long, long long, long long), 3
    117       m = t5
    118       t6 = llong- 1000
    119       t7 = m llong/ t6
    120       t8 = m llong% 1000
    121       param "%lld %lld %lld\n"
    122       param m
    123       param t7
    124       param t8
    125       call printf, 4
    126       x = 1
    127       t9 = x llong<< 31
    128       t10 = x llong<< 32
    129       t11 = x llong<< 62
    130       param "%lld %lld %lld\n"
    131       param t9
    132       param t10
    133       param t11
    134       call printf, 4
    135       t12 = llong- 1000000000000
    136       neg = t12
    137       t13 = neg llong>> 4
    138       t14 = neg llong/ 7
    139       param "%lld %lld\n"
    140       param t13
    141       param t14
    142       call printf, 3
    143       big = 18446744073709551615
    144       t15 = big ullong/ 3
    145       param "%llu %llu\n"
    146       param big
    147       param t15
    148       call printf, 3
    149       if a llong> b goto L1
    150       t16 = 0
    151       goto L2
    152  L1:  t16 = 1
    153  L2:  if neg llong< a goto L3
    154       t17 = 0
    155       goto L4
    156  L3:  t17 = 1
    157  L4:  t19 = a llong+ 1
    158       if t19 llong== 4294967296 goto L5
    159       t18 = 0
    160       goto L6
    161  L5:  t18 = 1
    162  L6:  param "%d %d %d\n"
    163       param t16
    164       param t17
    165       param t18
    166       call printf, 4
    167       t20 = llongtodouble m
    168       dd = t20
    169       t21 = dd double/ 3.0
    170       t22 = doubletollong t21
    171       back = t22
    172       param "%.0f %lld\n"
    173       param dd
    174       param back
    175       call printf, 3
    176       keep = 9000000000
    177       param 2
    178       param 3
    179       param 4
    180       t23 = call mulAdd(long long, long long, long long), 3
    181       r = t23
    182       t24 = r llong+ keep
    183       param "%lld %lld\n"
    184       param keep
    185       param t24
    186       call printf, 3
    187       return 0


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   mulAdd             function      long long (long long, long long, long long) -           5    -    2  _Z6mulAddxxx; defined
   main               function      int (void)                 -           6    -    0  defined

 scope: global > mulAdd()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     long long                  param       5    8    1  a.1
   b                  parameter     long long                  param       5    8    1  b.2
   c                  parameter     long long                  param       5    8    1  c.3

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      long long                  local       7    8    5  a.4
   b                  variable      long long                  local       7    8    3  b.5
   m                  variable      long long                  local       9    8    4  m.6
   x                  variable      long long                  local      11    8    3  x.7
   neg                variable      long long                  local      13    8    3  neg.8
   big                variable      unsigned long long         local      15    8    2  big.9
   dd                 variable      double                     local      18    8    2  dd.10
   back               variable      long long                  local      19    8    1  back.11
   keep               variable      long long                  local      21    8    2  keep.12
   r                  variable      long long                  local      22    8    1  r.13

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
