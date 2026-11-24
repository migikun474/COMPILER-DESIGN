============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t30_int_edges.c
   Optimization  : no optimization
   Result        : Three address code generated: 1 function(s), 99 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 38 temporaries, frame 184 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   big              local   int                             4       8
   small            local   int                             4      12
   u                local   unsigned int                    4      16
   c                local   char                            1      20
   uc               local   unsigned char                   1      21
   s                local   short                           2      22
   us               local   unsigned short                  2      24
   x                local   int                             4      28
   t1               temp    int                             4      32
   t2               temp    int                             4      36
   t3               temp    int                             4      40
   t4               temp    int                             4      44
   t5               temp    int                             4      48
   t6               temp    int                             4      52
   t7               temp    int                             4      56
   t8               temp    int                             4      60
   t9               temp    int                             4      64
   t10              temp    int                             4      68
   t11              temp    int                             4      72
   t12              temp    int                             4      76
   t13              temp    int                             4      80
   t14              temp    int                             4      84
   t15              temp    int                             4      88
   t16              temp    int                             4      92
   t17              temp    int                             4      96
   t18              temp    int                             4     100
   t19              temp    unsigned int                    4     104
   t20              temp    unsigned int                    4     108
   t21              temp    unsigned int                    4     112
   t22              temp    unsigned int                    4     116
   t23              temp    unsigned int                    4     120
   t24              temp    int                             4     124
   t25              temp    int                             4     128
   t26              temp    int                             4     132
   t27              temp    int                             4     136
   t28              temp    int                             4     140
   t29              temp    int                             4     144
   t30              temp    int                             4     148
   t31              temp    int                             4     152
   t32              temp    unsigned int                    4     156
   t33              temp    int                             4     160
   t34              temp    int                             4     164
   t35              temp    int                             4     168
   t36              temp    int                             4     172
   t37              temp    int                             4     176
   t38              temp    int                             4     180

 Code: 99 instruction(s)

    100       t1 = int- 7
    101       a = t1
    102       b = 2
    103       big = 2147483647
    104       t2 = int- 2147483647
    105       t3 = t2 int- 1
    106       small = t3
    107       t4 = a int/ b
    108       t5 = a int% b
    109       t6 = int- 2
    110       t7 = 7 int/ t6
    111       t8 = int- 2
    112       t9 = 7 int% t8
    113       param "%d %d %d %d\n"
    114       param t4
    115       param t5
    116       param t7
    117       param t9
    118       call printf, 5
    119       t10 = int- a
    120       t11 = int- b
    121       t12 = t10 int/ t11
    122       t13 = int- 8
    123       t14 = t13 int/ 3
    124       t15 = int- 8
    125       t16 = t15 int% 3
    126       param "%d %d %d\n"
    127       param t12
    128       param t14
    129       param t16
    130       call printf, 4
    131       t17 = a int>> 1
    132       t18 = a int<< 2
    133       t19 = a uint>> 28
    134       t20 = 1 uint<< 31
    135       param "%d %d %u %u\n"
    136       param t17
    137       param t18
    138       param t19
    139       param t20
    140       call printf, 5
    141       u = 0
    142       t21 = u uint- 1
    143       u = t21
    144       t22 = u uint+ 2
    145       t23 = u uint/ 2
    146       param "%u %u %d\n"
    147       param u
    148       param t22
    149       param t23
    150       call printf, 4
    151       c = -56
    152       uc = 200
    153       s = -25536
    154       us = 4464
    155       t24 = chartoint c
    156       t25 = uchartoint uc
    157       t26 = shorttoint s
    158       t27 = ushorttoint us
    159       param "%d %d %d %d\n"
    160       param t24
    161       param t25
    162       param t26
    163       param t27
    164       call printf, 5
    165       t29 = int- 1
    166       if t29 uint< 0 goto L1
    167       t28 = 0
    168       goto L2
    169  L1:  t28 = 1
    170  L2:  t31 = int- 1
    171       if t31 uint> 5 goto L3
    172       t30 = 0
    173       goto L4
    174  L3:  t30 = 1
    175  L4:  param "%d %d\n"
    176       param t28
    177       param t30
    178       call printf, 3
    179       t32 = big uint+ 1
    180       param "%d %d %u\n"
    181       param big
    182       param small
    183       param t32
    184       call printf, 4
    185       x = 1000
    186       t33 = x int* x
    187       t34 = t33 int* 3
    188       x = t34
    189       t35 = x int/ 7
    190       t36 = t35 int% 13
    191       t37 = x int& 255
    192       t38 = t37 int^ 85
    193       param "%d %d %d\n"
    194       param x
    195       param t36
    196       param t38
    197       call printf, 4
    198       return 0


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
   a                  variable      int                        local       6    4    6  a.1
   b                  variable      int                        local       6    4    3  b.2
   big                variable      int                        local       6    4    2  big.3
   small              variable      int                        local       6    4    1  small.4
   u                  variable      unsigned int               local      10    4    5  u.5
   c                  variable      char                       local      13    1    1  c.6
   uc                 variable      unsigned char              local      14    1    1  uc.7
   s                  variable      short                      local      15    2    1  s.8
   us                 variable      unsigned short             local      16    2    1  us.9
   x                  variable      int                        local      20    4    6  x.10

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
