============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : test/t08_classes.c
   Optimization  : -O1: optimized inside basic blocks
   Result        : Optimized three address code (-O1): 306 -> 274 instruction(s)

   Contents      : optimization summary, globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

----------------------------------------------------------------------------
 OPTIMIZATION SUMMARY (-O1)
----------------------------------------------------------------------------

   instructions                          306 -> 274   (10% fewer)

   constants folded                        0
   algebraic simplifications               0
   common subexpressions                  20
   copies / constants forwarded           22
   temporaries merged away                 4
   dead instructions removed              27
   jumps removed or redirected             3
   unreachable instructions removed        0

----------------------------------------------------------------------------
 GLOBALS: 1 object(s) in static storage
----------------------------------------------------------------------------

   name             type                        width  initial value
   ---------------- -------------------------- ------  -------------
   Dog::made        int                             4  0

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
 FUNCTION Animal::~Animal()        (link name _ZN6AnimalD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0

 Code: 3 instruction(s)

    104     param "~Animal()\n"
    105     call printf, 1
    106     return

============================================================================
 FUNCTION Animal::count()        (link name _ZN6Animal5countEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Animal *                  4       0
   t1               temp    int                             4       4

 Code: 2 instruction(s)

    107     t1 = *this
    108     return t1

============================================================================
 FUNCTION Tag::Tag()        (link name _ZN3TagC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0

 Code: 4 instruction(s)

    109     *this = 7
    110     param "Tag()\n"
    111     call printf, 1
    112     return

============================================================================
 FUNCTION Tag::~Tag()        (link name _ZN3TagD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 0 temporaries, frame 4 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Tag *                     4       0

 Code: 3 instruction(s)

    113     param "~Tag()\n"
    114     call printf, 1
    115     return

============================================================================
 FUNCTION Dog::Dog(int)        (link name _ZN3DogC1Ei)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   a                param   int                             4       4
   t1               temp    class Dog *                     4       8
   t2               temp    class Dog *                     4      12
   t5               temp    int                             4      24
   (2 temporaries no longer used after optimization not shown)

 Code: 13 instruction(s)

    116     param this                          (this)
    117     call Animal::Animal(), 1
    118     t1 = this ptr+ 8
    119     param t1                            (this)
    120     call Tag::Tag(), 1
    121     t2 = this ptr+ 4
    122     *t2 = a
    123     Dog::made = Dog::made int+ 1
    124     t5 = *t2
    125     param "Dog(%d)\n"
    126     param t5
    127     call printf, 2
    128     return

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

    129     param this                          (this)
    130     call Animal::Animal(), 1
    131     t1 = this ptr+ 8
    132     param t1                            (this)
    133     call Tag::Tag(), 1
    134     t2 = this ptr+ 4
    135     *t2 = 0
    136     Dog::made = Dog::made int+ 1
    137     param "Dog()\n"
    138     call printf, 1
    139     return

============================================================================
 FUNCTION Dog::~Dog()        (link name _ZN3DogD1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 3 temporaries, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Dog *                     4       0
   t1               temp    class Dog *                     4       4
   t2               temp    int                             4       8
   t3               temp    class Dog *                     4      12

 Code: 11 instruction(s)

    140     t1 = this ptr+ 4
    141     t2 = *t1
    142     param "~Dog(%d)\n"
    143     param t2
    144     call printf, 2
    145     t3 = this ptr+ 8
    146     param t3                            (this)
    147     call Tag::~Tag(), 1
    148     param this                          (this)
    149     call Animal::~Animal(), 1
    150     return

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

    151     t1 = this ptr+ 4
    152     t2 = *t1
    153     t3 = t2 int* 7
    154     t4 = *this
    155     t5 = t3 int+ t4
    156     t6 = this ptr+ 8
    157     t7 = *t6
    158     t8 = t5 int+ t7
    159     return t8

============================================================================
 FUNCTION Dog::total()        (link name _ZN3Dog5totalEv)
============================================================================

 Code: 1 instruction(s)

    160     return Dog::made

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

    161     t1 = this ptr+ 4
    162     t2 = *t1
    163     t3 = t2 int+ 1
    164     *t1 = t3
    165     return

============================================================================
 FUNCTION Vec::Vec(int, int)        (link name _ZN3VecC1Eii)
============================================================================

 Symbol table: 3 parameter(s)/local(s), 1 temporary, frame 16 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   a                param   int                             4       4
   b                param   int                             4       8
   t1               temp    class Vec *                     4      12

 Code: 4 instruction(s)

    166     *this = a
    167     t1 = this ptr+ 4
    168     *t1 = b
    169     return

============================================================================
 FUNCTION Vec::Vec()        (link name _ZN3VecC1Ev)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 1 temporary, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec *                     4       4

 Code: 4 instruction(s)

    170     *this = 0
    171     t1 = this ptr+ 4
    172     *t1 = 0
    173     return

============================================================================
 FUNCTION Vec::operator+(class Vec)        (link name _ZN3VecplES_)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 9 temporaries, frame 52 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   o                param   class Vec                       8       4
   t1               temp    class Vec                       8      12
   t2               temp    class Vec *                     4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    class Vec *                     4      36
   t7               temp    int                             4      40
   t8               temp    int                             4      44
   t9               temp    int                             4      48

 Code: 13 instruction(s)

    174     t2 = &t1
    175     t3 = *this
    176     t4 = o[0]
    177     t5 = t3 int+ t4
    178     t6 = this ptr+ 4
    179     t7 = *t6
    180     t8 = o[4]
    181     t9 = t7 int+ t8
    182     param t2                            (this)
    183     param t5
    184     param t9
    185     call Vec::Vec(int, int), 3
    186     return t1

============================================================================
 FUNCTION Vec::operator-()        (link name _ZN3VecmiEv)
============================================================================

 Symbol table: 1 parameter(s)/local(s), 7 temporaries, frame 36 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   this             param   class Vec *                     4       0
   t1               temp    class Vec                       8       4
   t2               temp    class Vec *                     4      12
   t3               temp    int                             4      16
   t4               temp    int                             4      20
   t5               temp    class Vec *                     4      24
   t6               temp    int                             4      28
   t7               temp    int                             4      32

 Code: 11 instruction(s)

    187     t2 = &t1
    188     t3 = *this
    189     t4 = int- t3
    190     t5 = this ptr+ 4
    191     t6 = *t5
    192     t7 = int- t6
    193     param t2                            (this)
    194     param t4
    195     param t7
    196     call Vec::Vec(int, int), 3
    197     return t1

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

    198       t2 = *this
    199       t3 = o[0]
    200       if t2 int!= t3 goto L1
    201       t4 = this ptr+ 4
    202       t5 = *t4
    203       t6 = o[4]
    204       if t5 int== t6 goto L2
    205  L1:  t1 = 0
    206       goto L3
    207  L2:  t1 = 1
    208  L3:  return t1

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

    209       if i int!= 0 goto L4
    210       t1 = *this
    211       goto L5
    212  L4:  t3 = this ptr+ 4
    213       t1 = *t3
    214  L5:  return t1

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

    215     t1 = *this
    216     t2 = o[0]
    217     t3 = t1 int+ t2
    218     *this = t3
    219     t4 = this ptr+ 4
    220     t5 = *t4
    221     t6 = o[4]
    222     t7 = t5 int+ t6
    223     *t4 = t7
    224     return this

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

    225     t1 = *this
    226     t2 = t1 int+ 1
    227     *this = t2
    228     return this

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

    229     t1 = *this
    230     t2 = t1 int* k
    231     t3 = this ptr+ 4
    232     t4 = *t3
    233     t5 = t2 int+ t4
    234     return t5

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

    235     t1 = *this
    236     t2 = o[0]
    237     t3 = t1 int* t2
    238     t4 = this ptr+ 4
    239     t5 = *t4
    240     t6 = o[4]
    241     t7 = t5 int* t6
    242     t8 = t3 int+ t7
    243     return t8

============================================================================
 FUNCTION operator*(class Vec, int)        (link name _Zml3Veci)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 6 temporaries, frame 40 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   v                param   class Vec                       8       0
   k                param   int                             4       8
   t1               temp    class Vec                       8      12
   t2               temp    class Vec *                     4      20
   t3               temp    int                             4      24
   t4               temp    int                             4      28
   t5               temp    int                             4      32
   t6               temp    int                             4      36

 Code: 10 instruction(s)

    244     t2 = &t1
    245     t3 = v[0]
    246     t4 = t3 int* k
    247     t5 = v[4]
    248     t6 = t5 int* k
    249     param t2                            (this)
    250     param t4
    251     param t6
    252     call Vec::Vec(int, int), 3
    253     return t1

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 10 parameter(s)/local(s), 29 temporaries, frame 312 bytes

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
   t11              temp    class Dog *                     4     128
   t13              temp    int                             4     136
   t15              temp    class Vec *                     4     144
   t16              temp    class Vec *                     4     148
   t17              temp    class Vec *                     4     152
   t19              temp    class Vec                       8     160
   t22              temp    class Vec                       8     176
   t25              temp    class Vec                       8     192
   t32              temp    int                             4     224
   t33              temp    int                             4     228
   t34              temp    int                             4     232
   t35              temp    int                             4     236
   t36              temp    int                             4     240
   t37              temp    int                             4     244
   t39              temp    int                             4     252
   t41              temp    int                             4     260
   t43              temp    int                             4     268
   t45              temp    int                             4     276
   t47              temp    int                             4     284
   t48              temp    class Vec (*)[2]                4     288
   t49              temp    class Vec (*)[2]                4     292
   t50              temp    int                             4     296
   t52              temp    int                             4     304
   t53              temp    int                             4     308
   (24 temporaries no longer used after optimization not shown)

 Code: 120 instruction(s)

    254     t1 = &rex
    255     param t1                            (this)
    256     param 3
    257     call Dog::Dog(int), 2
    258     param t1                            (this)
    259     call Dog::birthday(), 1
    260     param t1                            (this)
    261     t4 = call Dog::human(), 1
    262     param t1                            (this)
    263     t6 = call Animal::count(), 1
    264     t7 = call Dog::total(), 0
    265     param "%d %d %d\n"
    266     param t4
    267     param t6
    268     param t7
    269     call printf, 4
    270     base = t1
    271     t9 = *t1
    272     param "%d\n"
    273     param t9
    274     call printf, 2
    275     param t1                            (this)
    276     call Dog::~Dog(), 1
    277     param "--\n"
    278     call printf, 1
    279     t11 = &other
    280     param t11                           (this)
    281     param 5
    282     call Dog::Dog(int), 2
    283     param t11                           (this)
    284     t13 = call Dog::human(), 1
    285     param "%d %d\n"
    286     param t13
    287     param Dog::made
    288     call printf, 3
    289     param t11                           (this)
    290     call Dog::~Dog(), 1
    291     param "--\n"
    292     call printf, 1
    293     t15 = &a
    294     param t15                           (this)
    295     param 1
    296     param 2
    297     call Vec::Vec(int, int), 3
    298     t16 = &b
    299     param t16                           (this)
    300     param 3
    301     param 4
    302     call Vec::Vec(int, int), 3
    303     t17 = &c
    304     param t17                           (this)
    305     call Vec::Vec(), 1
    306     param t15                           (this)
    307     param b
    308     t19 = call Vec::operator+(class Vec), 2
    309     c = t19
    310     param t17                           (this)
    311     t22 = call Vec::operator-(), 1
    312     d = t22
    313     param a
    314     param 3
    315     t25 = call operator*(class Vec, int), 2
    316     e = t25
    317     param t15                           (this)
    318     param b
    319     call Vec::operator+=(class Vec), 2
    320     param t15                           (this)
    321     call Vec::operator++(), 1
    322     t32 = c[0]
    323     t33 = c[4]
    324     t34 = d[0]
    325     t35 = e[4]
    326     t36 = a[0]
    327     t37 = a[4]
    328     param "%d %d %d %d %d %d\n"
    329     param t32
    330     param t33
    331     param t34
    332     param t35
    333     param t36
    334     param t37
    335     call printf, 7
    336     param t15                           (this)
    337     param b
    338     t39 = call Vec::operator==(class Vec), 2
    339     param t17                           (this)
    340     param c
    341     t41 = call Vec::operator==(class Vec), 2
    342     param t15                           (this)
    343     param 0
    344     t43 = call Vec::operator[](int), 2
    345     param t15                           (this)
    346     param 2
    347     t45 = call Vec::operator()(int), 2
    348     param t15                           (this)
    349     param b
    350     t47 = call Vec::dot(class Vec), 2
    351     param "%d %d %d %d %d\n"
    352     param t39
    353     param t41
    354     param t43
    355     param t45
    356     param t47
    357     call printf, 6
    358     t48 = &row
    359     param t48                           (this)
    360     call Vec::Vec(), 1
    361     t49 = t48 ptr+ 8
    362     param t49                           (this)
    363     call Vec::Vec(), 1
    364     row[8] = 9
    365     t50 = row[0]
    366     param "%d %d\n"
    367     param t50
    368     param 9
    369     call printf, 3
    370     w = 7
    371     t52 = c[0]
    372     t53 = 7 int+ t52
    373     return t53


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   Animal             class_tag     class Animal               -           5    -    0  size 4
   Tag                class_tag     class Tag                  -          13    -    0  size 4
   Dog                class_tag     class Dog                  -          20    -    0  size 12, public base Animal
   Vec                class_tag     class Vec                  -          35    -    0  size 8
   operator*          function      class Vec (class Vec, int) -          50    -    1  _Zml3Veci; defined
   main               function      int (void)                 -          52    -    0  defined

 scope: global > class Animal
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   legs               field         int                        member      7    4    4  Animal::legs; public, offset 0
   Animal             constructor   void (void)                -           8    -    2  _ZN6AnimalC1Ev; public
   ~Animal            destructor    void (void)                -           9    -    0  _ZN6AnimalD1Ev; public
   count              method        int (void)                 -          10    -    1  _ZN6Animal5countEv; public, defined

 scope: global > class Tag
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   id                 field         int                        member     15    4    2  Tag::id; public, offset 0
   Tag                constructor   void (void)                -          16    -    2  _ZN3TagC1Ev; public
   ~Tag               destructor    void (void)                -          17    -    0  _ZN3TagD1Ev; public

 scope: global > class Dog
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   age                field         int                        member     22    4    7  Dog::age; public, offset 4
   tag                field         class Tag                  member     23    4    1  Dog::tag; public, offset 8
   made               field         int                        static     24    4    4  Dog::made; public, static
   Dog                constructor   void (int)                 -          25    -    2  _ZN3DogC1Ei; public
   Dog                constructor   void (void)                -          26    -    0  _ZN3DogC1Ev; public
   ~Dog               destructor    void (void)                -          27    -    0  _ZN3DogD1Ev; public
   human              method        int (void)                 -          28    -    2  _ZN3Dog5humanEv; public, defined
   birthday           method        void (void)                -          29    -    1  _ZN3Dog8birthdayEv; public, defined
   total              method        int (void)                 -          30    -    1  _ZN3Dog5totalEv; public, static, defined

 scope: global > class Dog > Dog()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      25    4    1  a.1

 scope: global > class Vec
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   x                  field         int                        member     37    4   22  Vec::x; public, offset 0
   y                  field         int                        member     38    4   17  Vec::y; public, offset 4
   Vec                constructor   void (int, int)            -          39    -    5  _ZN3VecC1Eii; public
   Vec                constructor   void (void)                -          40    -    2  _ZN3VecC1Ev; public
   operator+          method        class Vec (class Vec)      -          41    -    1  _ZN3VecplES_; public, defined
   operator-          method        class Vec (void)           -          42    -    1  _ZN3VecmiEv; public, defined
   operator==         method        int (class Vec)            -          43    -    2  _ZN3VeceqES_; public, defined
   operator[]         method        int (int)                  -          44    -    1  _ZN3VecixEi; public, defined
   operator+=         method        class Vec &(class Vec)     -          45    -    1  _ZN3VecpLES_; public, defined
   operator++         method        class Vec &(void)          -          46    -    1  _ZN3VecppEv; public, defined
   operator()         method        int (int)                  -          47    -    1  _ZN3VecclEi; public, defined
   dot                method        int (class Vec)            -          48    -    1  _ZN3Vec3dotES_; public, defined

 scope: global > class Vec > Vec()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  parameter     int                        param      39    4    1  a.2
   b                  parameter     int                        param      39    4    1  b.3

 scope: global > class Vec > operator+()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      41    8    2  o.4

 scope: global > class Vec > operator==()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      43    8    2  o.5

 scope: global > class Vec > operator[]()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  parameter     int                        param      44    4    1  i.6

 scope: global > class Vec > operator+=()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      45    8    2  o.7

 scope: global > class Vec > operator()()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   k                  parameter     int                        param      47    4    1  k.8

 scope: global > class Vec > dot()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   o                  parameter     class Vec                  param      48    8    2  o.9

 scope: global > operator*()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   v                  parameter     class Vec                  param      50    8    2  v.10
   k                  parameter     int                        param      50    4    2  k.11

 scope: global > main() > block
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   rex                variable      class Dog                  local      54   12    4  rex.12
   base               variable      class Animal *             local      57    4    1  base.13
   other              variable      class Dog                  local      62   12    1  other.14

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      class Vec                  local      67    8   10  a.15
   b                  variable      class Vec                  local      67    8    4  b.16
   c                  variable      class Vec                  local      67    8    7  c.17
   d                  variable      class Vec                  local      69    8    1  d.18
   e                  variable      class Vec                  local      70    8    1  e.19
   row                variable      class Vec[2]               local      75   16    3  row.20
   w                  variable      int                        local      78    4    1  w.21

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
