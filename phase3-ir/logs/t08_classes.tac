============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : no optimization
   Result        : Three address code generated: 19 function(s), 261 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Dog::made        int                             4  0

 As three address code (initial values, in place before main runs):

    Dog::made = 0

============================================================================
 FUNCTION Animal::Animal()        (link name _ZN6AnimalC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0

 Code: 4 instruction(s)

    100     *this = 4
    101     param "Animal()\n"
    102     call printf, 1
    103     return

============================================================================
 FUNCTION Animal::count()        (link name _ZN6Animal5countEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    104     t1 = *this
    105     return t1

============================================================================
 FUNCTION Tag::Tag()        (link name _ZN3TagC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0

 Code: 4 instruction(s)

    106     *this = 7
    107     param "Tag()\n"
    108     call printf, 1
    109     return

============================================================================
 FUNCTION Dog::Dog()        (link name _ZN3DogC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    class Dog *                     4       8
   t3               temp    int                             4      12

 Code: 12 instruction(s)

    110     param this                          (this)
    111     call Animal::Animal(), 1
    112     t1 = this ptr+ 8
    113     param t1                            (this)
    114     call Tag::Tag(), 1
    115     t2 = this ptr+ 4
    116     *t2 = 0
    117     t3 = Dog::made int+ 1
    118     Dog::made = t3
    119     param "Dog()\n"
    120     call printf, 1
    121     return

============================================================================
 FUNCTION Dog::human()        (link name _ZN3Dog5humanEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 8 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    int                             4      16
   t5               temp    int                             4      20
   t6               temp    class Dog *                     4      24
   t7               temp    int                             4      28
   t8               temp    int                             4      32

 Code: 9 instruction(s)

    122     t1 = this ptr+ 4
    123     t2 = *t1
    124     t3 = t2 int* 7
    125     t4 = *this
    126     t5 = t3 int+ t4
    127     t6 = this ptr+ 8
    128     t7 = *t6
    129     t8 = t5 int+ t7
    130     return t8

============================================================================
 FUNCTION Dog::total()        (link name _ZN3Dog5totalEv)
============================================================================

 Code: 1 instruction(s)

    131     return Dog::made

============================================================================
 FUNCTION Dog::birthday()        (link name _ZN3Dog8birthdayEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 4 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   t4               temp    class Dog *                     4      16

 Code: 6 instruction(s)

    132     t1 = this ptr+ 4
    133     t2 = *t1
    134     t3 = t2 int+ 1
    135     t4 = this ptr+ 4
    136     *t4 = t3
    137     return

============================================================================
 FUNCTION Vec::Vec()        (link name _ZN3VecC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4

 Code: 4 instruction(s)

    138     *this = 0
    139     t1 = this ptr+ 4
    140     *t1 = 0
    141     return

============================================================================
 FUNCTION Vec::operator+(class Vec)        (link name _ZN3VecplES_)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 8 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   r                local   class Vec                       8      12
   t1               temp    class Vec *                     4      20
   t2               temp    int                             4      24
   t3               temp    int                             4      28
   t4               temp    int                             4      32
   t5               temp    class Vec *                     4      36
   t6               temp    int                             4      40
   t7               temp    int                             4      44
   t8               temp    int                             4      48

 Code: 13 instruction(s)

    142     t1 = &r
    143     param t1                            (this)
    144     call Vec::Vec(), 1
    145     t2 = *this
    146     t3 = o[0]
    147     t4 = t2 int+ t3
    148     r[0] = t4
    149     t5 = this ptr+ 4
    150     t6 = *t5
    151     t7 = o[4]
    152     t8 = t6 int+ t7
    153     r[4] = t8
    154     return r

============================================================================
 FUNCTION Vec::operator-()        (link name _ZN3VecmiEv)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   r                local   class Vec                       8       4
   t1               temp    class Vec *                     4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32

 Code: 11 instruction(s)

    155     t1 = &r
    156     param t1                            (this)
    157     call Vec::Vec(), 1
    158     t2 = *this
    159     t3 = int- t2
    160     r[0] = t3
    161     t4 = this ptr+ 4
    162     t5 = *t4
    163     t6 = int- t5
    164     r[4] = t6
    165     return r

============================================================================
 FUNCTION Vec::operator==(class Vec)        (link name _ZN3VeceqES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32

 Code: 13 instruction(s)

    166       t2 = *this
    167       t3 = o[0]
    168       if t2 int== t3 goto L1
    169       goto L2
    170  L1:  t4 = this ptr+ 4
    171       t5 = *t4
    172       t6 = o[4]
    173       if t5 int== t6 goto L3
    174       goto L2
    175  L2:  t1 = 0
    176       goto L4
    177  L3:  t1 = 1
    178  L4:  return t1

============================================================================
 FUNCTION Vec::operator[](int)        (link name _ZN3VecixEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 4 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   i                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    class Vec *                     4      16
   t4               temp    int                             4      20

 Code: 9 instruction(s)

    179       if i int== 0 goto L5
    180       goto L6
    181  L5:  t2 = *this
    182       t1 = t2
    183       goto L7
    184  L6:  t3 = this ptr+ 4
    185       t4 = *t3
    186       t1 = t4
    187  L7:  return t1

============================================================================
 FUNCTION Vec::operator+=(class Vec)        (link name _ZN3VecpLES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   t7               temp    int                             4      36
   t8               temp    class Vec *                     4      40

 Code: 11 instruction(s)

    188     t1 = *this
    189     t2 = o[0]
    190     t3 = t1 int+ t2
    191     *this = t3
    192     t4 = this ptr+ 4
    193     t5 = *t4
    194     t6 = o[4]
    195     t7 = t5 int+ t6
    196     t8 = this ptr+ 4
    197     *t8 = t7
    198     return this

============================================================================
 FUNCTION Vec::operator++()        (link name _ZN3VecppEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 12 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    int                             4       4
   t2               temp    int                             4       8

 Code: 4 instruction(s)

    199     t1 = *this
    200     t2 = t1 int+ 1
    201     *this = t2
    202     return this

============================================================================
 FUNCTION Vec::operator()(int)        (link name _ZN3VecclEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   k                param   int                             4       4
   t1               temp    int                             4       8
   t2               temp    int                             4      12
   t3               temp    class Vec *                     4      16
   t4               temp    int                             4      20
   t5               temp    int                             4      24

 Code: 6 instruction(s)

    203     t1 = *this
    204     t2 = t1 int* k
    205     t3 = this ptr+ 4
    206     t4 = *t3
    207     t5 = t2 int+ t4
    208     return t5

============================================================================
 FUNCTION Vec::dot(class Vec)        (link name _ZN3Vec3dotES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 8 temporaries, frame 44 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    class Vec *                     4      24
   t5               temp    int                             4      28
   t6               temp    int                             4      32
   t7               temp    int                             4      36
   t8               temp    int                             4      40

 Code: 9 instruction(s)

    209     t1 = *this
    210     t2 = o[0]
    211     t3 = t1 int* t2
    212     t4 = this ptr+ 4
    213     t5 = *t4
    214     t6 = o[4]
    215     t7 = t5 int* t6
    216     t8 = t3 int+ t7
    217     return t8

============================================================================
 FUNCTION make(int, int)        (link name _Z4makeii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                param   int                             4       0
   b                param   int                             4       4
   v                local   class Vec                       8       8
   t1               temp    class Vec *                     4      16

 Code: 6 instruction(s)

    218     t1 = &v
    219     param t1                            (this)
    220     call Vec::Vec(), 1
    221     v[0] = a
    222     v[4] = b
    223     return v

============================================================================
 FUNCTION operator*(class Vec, int)        (link name _Zml3Veci)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 5 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   class Vec                       8       0
   k                param   int                             4       8
   t1               temp    int                             4      12
   t2               temp    int                             4      16
   t3               temp    int                             4      20
   t4               temp    int                             4      24
   t5               temp    class Vec                       8      28

 Code: 8 instruction(s)

    224     t1 = v[0]
    225     t2 = t1 int* k
    226     t3 = v[4]
    227     t4 = t3 int* k
    228     param t2
    229     param t4
    230     t5 = call make(int, int), 2
    231     return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 46 temporaries, frame 292 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   rex              local   class Dog                      12       0
   base             local   class Animal *                  4      12
   other            local   class Dog                      12      16
   a                local   class Vec                       8      28
   b                local   class Vec                       8      36
   c                local   class Vec                       8      44
   d                local   class Vec                       8      52
   e                local   class Vec                       8      60
   row              local   class Vec[2]                   16      68
   w                local   int                             4      84
   t1               temp    class Dog *                     4      88
   t2               temp    class Dog *                     4      92
   t3               temp    class Dog *                     4      96
   t4               temp    int                             4     100
   t5               temp    class Dog *                     4     104
   t6               temp    int                             4     108
   t7               temp    int                             4     112
   t8               temp    class Dog *                     4     116
   t9               temp    int                             4     120
   t10              temp    class Dog *                     4     124
   t11              temp    class Dog *                     4     128
   t12              temp    int                             4     132
   t13              temp    class Vec                       8     136
   t14              temp    class Vec                       8     144
   t15              temp    class Vec *                     4     152
   t16              temp    class Vec *                     4     156
   t17              temp    class Vec                       8     160
   t18              temp    class Vec *                     4     168
   t19              temp    class Vec                       8     172
   t20              temp    class Vec                       8     180
   t21              temp    class Vec *                     4     188
   t22              temp    class Vec &                     4     192
   t23              temp    class Vec *                     4     196
   t24              temp    class Vec &                     4     200
   t25              temp    int                             4     204
   t26              temp    int                             4     208
   t27              temp    int                             4     212
   t28              temp    int                             4     216
   t29              temp    int                             4     220
   t30              temp    int                             4     224
   t31              temp    class Vec *                     4     228
   t32              temp    int                             4     232
   t33              temp    class Vec *                     4     236
   t34              temp    int                             4     240
   t35              temp    class Vec *                     4     244
   t36              temp    int                             4     248
   t37              temp    class Vec *                     4     252
   t38              temp    int                             4     256
   t39              temp    class Vec *                     4     260
   t40              temp    int                             4     264
   t41              temp    class Vec (*)[2]                4     268
   t42              temp    class Vec (*)[2]                4     272
   t43              temp    int                             4     276
   t44              temp    int                             4     280
   t45              temp    int                             4     284
   t46              temp    int                             4     288

 Code: 129 instruction(s)

    232     t1 = &rex
    233     param t1                            (this)
    234     call Dog::Dog(), 1
    235     rex[4] = 3
    236     t2 = &rex
    237     param t2                            (this)
    238     call Dog::birthday(), 1
    239     t3 = &rex
    240     param t3                            (this)
    241     t4 = call Dog::human(), 1
    242     t5 = &rex
    243     param t5                            (this)
    244     t6 = call Animal::count(), 1
    245     t7 = call Dog::total(), 0
    246     param "%d %d %d\n"
    247     param t4
    248     param t6
    249     param t7
    250     call printf, 4
    251     t8 = &rex
    252     base = t8
    253     t9 = *base
    254     param "%d\n"
    255     param t9
    256     call printf, 2
    257     param "--\n"
    258     call printf, 1
    259     t10 = &other
    260     param t10                           (this)
    261     call Dog::Dog(), 1
    262     other[4] = 5
    263     t11 = &other
    264     param t11                           (this)
    265     t12 = call Dog::human(), 1
    266     param "%d %d\n"
    267     param t12
    268     param Dog::made
    269     call printf, 3
    270     param "--\n"
    271     call printf, 1
    272     param 1
    273     param 2
    274     t13 = call make(int, int), 2
    275     a = t13
    276     param 3
    277     param 4
    278     t14 = call make(int, int), 2
    279     b = t14
    280     t15 = &c
    281     param t15                           (this)
    282     call Vec::Vec(), 1
    283     t16 = &a
    284     param t16                           (this)
    285     param b
    286     t17 = call Vec::operator+(class Vec), 2
    287     c = t17
    288     t18 = &c
    289     param t18                           (this)
    290     t19 = call Vec::operator-(), 1
    291     d = t19
    292     param a
    293     param 3
    294     t20 = call operator*(class Vec, int), 2
    295     e = t20
    296     t21 = &a
    297     param t21                           (this)
    298     param b
    299     t22 = call Vec::operator+=(class Vec), 2
    300     t23 = &a
    301     param t23                           (this)
    302     t24 = call Vec::operator++(), 1
    303     t25 = c[0]
    304     t26 = c[4]
    305     t27 = d[0]
    306     t28 = e[4]
    307     t29 = a[0]
    308     t30 = a[4]
    309     param "%d %d %d %d %d %d\n"
    310     param t25
    311     param t26
    312     param t27
    313     param t28
    314     param t29
    315     param t30
    316     call printf, 7
    317     t31 = &a
    318     param t31                           (this)
    319     param b
    320     t32 = call Vec::operator==(class Vec), 2
    321     t33 = &c
    322     param t33                           (this)
    323     param c
    324     t34 = call Vec::operator==(class Vec), 2
    325     t35 = &a
    326     param t35                           (this)
    327     param 0
    328     t36 = call Vec::operator[](int), 2
    329     t37 = &a
    330     param t37                           (this)
    331     param 2
    332     t38 = call Vec::operator()(int), 2
    333     t39 = &a
    334     param t39                           (this)
    335     param b
    336     t40 = call Vec::dot(class Vec), 2
    337     param "%d %d %d %d %d\n"
    338     param t32
    339     param t34
    340     param t36
    341     param t38
    342     param t40
    343     call printf, 6
    344     t41 = &row
    345     param t41                           (this)
    346     call Vec::Vec(), 1
    347     t42 = t41 ptr+ 8
    348     param t42                           (this)
    349     call Vec::Vec(), 1
    350     row[8] = 9
    351     t43 = row[0]
    352     t44 = row[8]
    353     param "%d %d\n"
    354     param t43
    355     param t44
    356     call printf, 3
    357     w = 7
    358     t45 = c[0]
    359     t46 = w int+ t45
    360     return t46


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Animal             class_tag     class Animal               -           5    -    0  size 4
   Tag                class_tag     class Tag                  -          12    -    0  size 4
   Dog                class_tag     class Dog                  -          18    -    0  size 12, public base Animal
   Vec                class_tag     class Vec                  -          31    -    0  size 8
   make               function      class Vec (int, int)       -          45    -    3  _Z4makeii; defined
   operator*          function      class Vec (class Vec, int) -          46    -    1  _Zml3Veci; defined
   main               function      int (void)                 -          48    -    0  defined

 scope: global > class Animal
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   legs               field         int                        member      7    4    4  Animal::legs; public, offset 0
   Animal             constructor   void (void)                -           8    -    0  _ZN6AnimalC1Ev; public
   count              method        int (void)                 -           9    -    1  _ZN6Animal5countEv; public, defined

 scope: global > class Tag
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     14    4    2  Tag::id; public, offset 0
   Tag                constructor   void (void)                -          15    -    0  _ZN3TagC1Ev; public

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   age                field         int                        member     20    4    6  Dog::age; public, offset 4
   tag                field         class Tag                  member     21    4    1  Dog::tag; public, offset 8
   made               field         int                        static     22    4    3  Dog::made; public, static
   Dog                constructor   void (void)                -          23    -    2  _ZN3DogC1Ev; public
   human              method        int (void)                 -          24    -    2  _ZN3Dog5humanEv; public, defined
   birthday           method        void (void)                -          25    -    1  _ZN3Dog8birthdayEv; public, defined
   total              method        int (void)                 -          26    -    1  _ZN3Dog5totalEv; public, static, defined

 scope: global > class Vec
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     33    4   24  Vec::x; public, offset 0
   y                  field         int                        member     34    4   19  Vec::y; public, offset 4
   Vec                constructor   void (void)                -          35    -    5  _ZN3VecC1Ev; public
   operator+          method        class Vec (class Vec)      -          36    -    1  _ZN3VecplES_; public, defined
   operator-          method        class Vec (void)           -          37    -    1  _ZN3VecmiEv; public, defined
   operator==         method        int (class Vec)            -          38    -    2  _ZN3VeceqES_; public, defined
   operator[]         method        int (int)                  -          39    -    1  _ZN3VecixEi; public, defined
   operator+=         method        class Vec &(class Vec)     -          40    -    1  _ZN3VecpLES_; public, defined
   operator++         method        class Vec &(void)          -          41    -    1  _ZN3VecppEv; public, defined
   operator()         method        int (int)                  -          42    -    1  _ZN3VecclEi; public, defined
   dot                method        int (class Vec)            -          43    -    1  _ZN3Vec3dotES_; public, defined

 scope: global > class Vec > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      36    8    2  o.1
   r                  variable      class Vec                  local      36    8    3  r.2

 scope: global > class Vec > operator-()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   r                  variable      class Vec                  local      37    8    3  r.3

 scope: global > class Vec > operator==()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      38    8    2  o.4

 scope: global > class Vec > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      39    4    1  i.5

 scope: global > class Vec > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      40    8    2  o.6

 scope: global > class Vec > operator()()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      42    4    1  k.7

 scope: global > class Vec > dot()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      43    8    2  o.8

 scope: global > make()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      45    4    1  a.9
   b                  parameter     int                        param      45    4    1  b.10
   v                  variable      class Vec                  local      45    8    3  v.11

 scope: global > operator*()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     class Vec                  param      46    8    2  v.12
   k                  parameter     int                        param      46    4    2  k.13

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   rex                variable      class Dog                  local      50   12    5  rex.14
   base               variable      class Animal *             local      54    4    1  base.15
   other              variable      class Dog                  local      59   12    2  other.16

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      class Vec                  local      65    8   10  a.17
   b                  variable      class Vec                  local      65    8    4  b.18
   c                  variable      class Vec                  local      65    8    7  c.19
   d                  variable      class Vec                  local      67    8    1  d.20
   e                  variable      class Vec                  local      68    8    1  e.21
   row                variable      class Vec[2]               local      73   16    3  row.22
   w                  variable      int                        local      76    4    1  w.23

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

class Animal: size 4, align 4
    +0  int legs  [public]
class Tag: size 4, align 4
    +0  int id  [public]
class Dog: size 12, align 4
    (base Animal, public)
    +4  int age  [public]
    +8  class Tag tag  [public]
    static  int made  [public]
class Vec: size 8, align 4
    +0  int x  [public]
    +4  int y  [public]
