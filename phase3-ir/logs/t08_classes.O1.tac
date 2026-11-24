============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 265 -> 234 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          265 -> 234   (11% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                  17
   copies / constants forwarded           19
   temporaries merged away                 8
   dead instructions removed              22
   jumps removed or redirected             3
   unreachable instructions removed        0

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

 Symbol table: 1 parameter(s)/local(s), 2 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    class Dog *                     4       8
   (1 temporary no longer used after optimization not shown)

 Code: 11 instruction(s)

    110     param this                          (this)
    111     call Animal::Animal(), 1
    112     t1 = this ptr+ 8
    113     param t1                            (this)
    114     call Tag::Tag(), 1
    115     t2 = this ptr+ 4
    116     *t2 = 0
    117     Dog::made = Dog::made int+ 1
    118     param "Dog()\n"
    119     call printf, 1
    120     return

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

    121     t1 = this ptr+ 4
    122     t2 = *t1
    123     t3 = t2 int* 7
    124     t4 = *this
    125     t5 = t3 int+ t4
    126     t6 = this ptr+ 8
    127     t7 = *t6
    128     t8 = t5 int+ t7
    129     return t8

============================================================================
 FUNCTION Dog::total()        (link name _ZN3Dog5totalEv)
============================================================================

 Code: 1 instruction(s)

    130     return Dog::made

============================================================================
 FUNCTION Dog::birthday()        (link name _ZN3Dog8birthdayEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 20 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    int                             4      12
   (1 temporary no longer used after optimization not shown)

 Code: 5 instruction(s)

    131     t1 = this ptr+ 4
    132     t2 = *t1
    133     t3 = t2 int+ 1
    134     *t1 = t3
    135     return

============================================================================
 FUNCTION Vec::Vec()        (link name _ZN3VecC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4

 Code: 4 instruction(s)

    136     *this = 0
    137     t1 = this ptr+ 4
    138     *t1 = 0
    139     return

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

    140     t1 = &r
    141     param t1                            (this)
    142     call Vec::Vec(), 1
    143     t2 = *this
    144     t3 = o[0]
    145     t4 = t2 int+ t3
    146     r[0] = t4
    147     t5 = this ptr+ 4
    148     t6 = *t5
    149     t7 = o[4]
    150     t8 = t6 int+ t7
    151     r[4] = t8
    152     return r

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

    153     t1 = &r
    154     param t1                            (this)
    155     call Vec::Vec(), 1
    156     t2 = *this
    157     t3 = int- t2
    158     r[0] = t3
    159     t4 = this ptr+ 4
    160     t5 = *t4
    161     t6 = int- t5
    162     r[4] = t6
    163     return r

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

 Code: 11 instruction(s)

    164       t2 = *this
    165       t3 = o[0]
    166       if t2 int!= t3 goto L1
    167       t4 = this ptr+ 4
    168       t5 = *t4
    169       t6 = o[4]
    170       if t5 int== t6 goto L2
    171  L1:  t1 = 0
    172       goto L3
    173  L2:  t1 = 1
    174  L3:  return t1

============================================================================
 FUNCTION Vec::operator[](int)        (link name _ZN3VecixEi)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 2 temporaries, frame 24 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   i                param   int                             4       4
   t1               temp    int                             4       8
   t3               temp    class Vec *                     4      16
   (2 temporaries no longer used after optimization not shown)

 Code: 6 instruction(s)

    175       if i int!= 0 goto L4
    176       t1 = *this
    177       goto L5
    178  L4:  t3 = this ptr+ 4
    179       t1 = *t3
    180  L5:  return t1

============================================================================
 FUNCTION Vec::operator+=(class Vec)        (link name _ZN3VecpLES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 7 temporaries, frame 44 bytes

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
   (1 temporary no longer used after optimization not shown)

 Code: 10 instruction(s)

    181     t1 = *this
    182     t2 = o[0]
    183     t3 = t1 int+ t2
    184     *this = t3
    185     t4 = this ptr+ 4
    186     t5 = *t4
    187     t6 = o[4]
    188     t7 = t5 int+ t6
    189     *t4 = t7
    190     return this

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

    191     t1 = *this
    192     t2 = t1 int+ 1
    193     *this = t2
    194     return this

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

    195     t1 = *this
    196     t2 = t1 int* k
    197     t3 = this ptr+ 4
    198     t4 = *t3
    199     t5 = t2 int+ t4
    200     return t5

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

    201     t1 = *this
    202     t2 = o[0]
    203     t3 = t1 int* t2
    204     t4 = this ptr+ 4
    205     t5 = *t4
    206     t6 = o[4]
    207     t7 = t5 int* t6
    208     t8 = t3 int+ t7
    209     return t8

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

    210     t1 = &v
    211     param t1                            (this)
    212     call Vec::Vec(), 1
    213     v[0] = a
    214     v[4] = b
    215     return v

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

    216     t1 = v[0]
    217     t2 = t1 int* k
    218     t3 = v[4]
    219     t4 = t3 int* k
    220     param t2
    221     param t4
    222     t5 = call make(int, int), 2
    223     return t5

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 25 temporaries, frame 308 bytes

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
   t4               temp    int                             4     100
   t6               temp    int                             4     108
   t7               temp    int                             4     112
   t9               temp    int                             4     120
   t10              temp    class Dog *                     4     124
   t12              temp    int                             4     132
   t14              temp    class Vec *                     4     144
   t17              temp    class Vec *                     4     160
   t29              temp    int                             4     220
   t30              temp    int                             4     224
   t31              temp    int                             4     228
   t32              temp    int                             4     232
   t33              temp    int                             4     236
   t34              temp    int                             4     240
   t36              temp    int                             4     248
   t38              temp    int                             4     256
   t40              temp    int                             4     264
   t42              temp    int                             4     272
   t44              temp    int                             4     280
   t45              temp    class Vec (*)[2]                4     284
   t46              temp    class Vec (*)[2]                4     288
   t47              temp    int                             4     292
   t49              temp    int                             4     300
   t50              temp    int                             4     304
   (25 temporaries no longer used after optimization not shown)

 Code: 110 instruction(s)

    224     t1 = &rex
    225     param t1                            (this)
    226     call Dog::Dog(), 1
    227     rex[4] = 3
    228     param t1                            (this)
    229     call Dog::birthday(), 1
    230     param t1                            (this)
    231     t4 = call Dog::human(), 1
    232     param t1                            (this)
    233     t6 = call Animal::count(), 1
    234     t7 = call Dog::total(), 0
    235     param "%d %d %d\n"
    236     param t4
    237     param t6
    238     param t7
    239     call printf, 4
    240     base = t1
    241     t9 = *t1
    242     param "%d\n"
    243     param t9
    244     call printf, 2
    245     param "--\n"
    246     call printf, 1
    247     t10 = &other
    248     param t10                           (this)
    249     call Dog::Dog(), 1
    250     other[4] = 5
    251     param t10                           (this)
    252     t12 = call Dog::human(), 1
    253     param "%d %d\n"
    254     param t12
    255     param Dog::made
    256     call printf, 3
    257     param "--\n"
    258     call printf, 1
    259     param 1
    260     param 2
    261     a = call make(int, int), 2
    262     t14 = &a
    263     param 3
    264     param 4
    265     b = call make(int, int), 2
    266     t17 = &c
    267     param t17                           (this)
    268     call Vec::Vec(), 1
    269     param t14                           (this)
    270     param b
    271     c = call Vec::operator+(class Vec), 2
    272     param t17                           (this)
    273     d = call Vec::operator-(), 1
    274     param a
    275     param 3
    276     e = call operator*(class Vec, int), 2
    277     param t14                           (this)
    278     param b
    279     call Vec::operator+=(class Vec), 2
    280     param t14                           (this)
    281     call Vec::operator++(), 1
    282     t29 = c[0]
    283     t30 = c[4]
    284     t31 = d[0]
    285     t32 = e[4]
    286     t33 = a[0]
    287     t34 = a[4]
    288     param "%d %d %d %d %d %d\n"
    289     param t29
    290     param t30
    291     param t31
    292     param t32
    293     param t33
    294     param t34
    295     call printf, 7
    296     param t14                           (this)
    297     param b
    298     t36 = call Vec::operator==(class Vec), 2
    299     param t17                           (this)
    300     param c
    301     t38 = call Vec::operator==(class Vec), 2
    302     param t14                           (this)
    303     param 0
    304     t40 = call Vec::operator[](int), 2
    305     param t14                           (this)
    306     param 2
    307     t42 = call Vec::operator()(int), 2
    308     param t14                           (this)
    309     param b
    310     t44 = call Vec::dot(class Vec), 2
    311     param "%d %d %d %d %d\n"
    312     param t36
    313     param t38
    314     param t40
    315     param t42
    316     param t44
    317     call printf, 6
    318     t45 = &row
    319     param t45                           (this)
    320     call Vec::Vec(), 1
    321     t46 = t45 ptr+ 8
    322     param t46                           (this)
    323     call Vec::Vec(), 1
    324     row[8] = 9
    325     t47 = row[0]
    326     param "%d %d\n"
    327     param t47
    328     param 9
    329     call printf, 3
    330     w = 7
    331     t49 = c[0]
    332     t50 = 7 int+ t49
    333     return t50


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
