============================================================================
 THREE ADDRESS CODE
============================================================================

   Source file   : phase3-ir/test/diagnostics/uninitialized.c
   Optimization  : no optimization
   Result        : Three address code generated: 3 function(s), 36 instruction(s)

   Contents      : globals, one section per function
                   (its symbol table, then its code), the semantic symbol table,
                   record layouts

============================================================================
 FUNCTION pick(int)        (link name _Z4picki)
============================================================================

 Symbol table: 2 parameter(s)/local(s), 0 temporaries, frame 8 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   which            param   int                             4       0
   x                local   int                             4       4

 Code: 4 instruction(s)

    100       if which int!= 0 goto L1
    101       goto L2
    102  L1:  x = 1
    103  L2:  return x

============================================================================
 FUNCTION total(int, ...)        (link name _Z5totaliz)
============================================================================

 Symbol table: 4 parameter(s)/local(s), 3 temporaries, frame 28 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   n                param   int                             4       0
   ap               local   va_list                         4       4
   sum              local   int                             4       8
   i                local   int                             4      12
   t1               temp    int                             4      16
   t2               temp    int                             4      20
   t3               temp    int                             4      24

 Code: 13 instruction(s)

    104       va_start ap, n
    105       sum = 0
    106       i = 0
    107  L3:  if i int< n goto L4
    108       goto L5
    109  L4:  t1 = va_arg ap, int
    110       t2 = sum int+ t1
    111       sum = t2
    112       t3 = i int+ 1
    113       i = t3
    114       goto L3
    115  L5:  va_end ap
    116       return sum

============================================================================
 FUNCTION main()        (link name main)
============================================================================

 Symbol table: 5 parameter(s)/local(s), 6 temporaries, frame 64 bytes

   name             kind    type                        width  offset
   ---------------- ------- -------------------------- ------ -------
   a                local   int                             4       0
   b                local   int                             4       4
   c                local   int                             4       8
   table            local   int[4]                         16      12
   wide             local   long long                       8      32
   t1               temp    int                             4      40
   t2               temp    int                             4      44
   t3               temp    int                             4      48
   t4               temp    int                             4      52
   t5               temp    int                             4      56
   t6               temp    int                             4      60

 Code: 19 instruction(s)

    117     t1 = a int+ 1
    118     b = t1
    119     c = 5
    120     t2 = table[0]
    121     param 1
    122     t3 = call pick(int), 1
    123     param 2
    124     param 3
    125     param 4
    126     t4 = call total(int, ...), 3
    127     t5 = t3 int+ t4
    128     param "%d %d %d %d\n"
    129     param b
    130     param c
    131     param t2
    132     param t5
    133     call printf, 5
    134     t6 = llongtoint wide
    135     return t6


----------------------------------------------------------------------------
 SEMANTIC SYMBOL TABLE (every scope and symbol of the program)
----------------------------------------------------------------------------

 scope: global
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   pick               function      int (int)                  -           3    -    1  _Z4picki; defined
   total              function      int (int, ...)             -           9    -    1  _Z5totaliz; defined
   main               function      int (void)                 -          18    -    0  defined

 scope: global > pick()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   which              parameter     int                        param       3    4    1  which.1
   x                  variable      int                        local       4    4    2  x.2

 scope: global > total()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   n                  parameter     int                        param       9    4    2  n.3
   ap                 variable      va_list                    local      10    4    3  ap.4
   sum                variable      int                        local      12    4    3  sum.5

 scope: global > total() > for
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   i                  variable      int                        local      13    4    2  i.6

 scope: global > main()
   name               kind          type                       storage  line size uses  TAC name / notes
   ------------------ ------------- -------------------------- ------- ----- ---- ----  ----------------
   a                  variable      int                        local      19    4    1  a.7
   b                  variable      int                        local      20    4    1  b.8
   c                  variable      int                        local      21    4    2  c.9
   table              variable      int[4]                     local      23   16    1  table.10
   wide               variable      long long                  local      24    8    1  wide.11

----------------------------------------------------------------------------
 RECORD LAYOUTS (MIPS32 sizes and offsets)
----------------------------------------------------------------------------

(no records)
