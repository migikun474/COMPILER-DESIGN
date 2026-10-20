=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t11_main_args.c
Optimization : -O1: optimized inside basic blocks

Optimized three address code (-O1): 31 -> 25 instruction(s) for 'test/t11_main_args.c'.

optimization summary (-O1)
    instructions                31 -> 25   (19% fewer)
    constants folded            0
    algebraic simplifications   2
    common subexpressions       0
    copies / constants forwarded 0
    temporaries merged away     4
    dead instructions removed   0
    jumps removed or redirected 2
    unreachable instructions    0

function main(int, char **)        link name: main
  symbol table (name, kind, type, width, offset)
    argc           param  int                        4      0
    argv           param  char **                    4      4
    letters        local  int                        4      8
    i              local  int                        4     12
    s              local  char *                     4     16
    t1             temp   int                        4     20
    t2             temp   char **                    4     24
    t3             temp   char *                     4     28
    t4             temp   char                       1     32
    t5             temp   int                        4     36
    t6             temp   char *                     4     40
    t7             temp   int                        4     44
    t8             temp   char **                    4     48
    t9             temp   char *                     4     52
    t10            temp   int                        4     56
    total width 60
  code
 100:     letters = 0
 101:     i = 1
 102: L1: if i int>= argc goto L4
 103:     t1 = i int<< 2
 104:     t2 = argv ptr+ t1
 105:     s = *t2
 106: L2: t4 = *s
 107:     if t4 char== 0 goto L3
 108:     letters = letters int+ 1
 109:     s = s ptr+ 1
 110:     goto L2
 111: L3: t7 = i int<< 2
 112:     t8 = argv ptr+ t7
 113:     t9 = *t8
 114:     param "%d: %s\n"
 115:     param i
 116:     param t9
 117:     call printf, 3
 118:     i = i int+ 1
 119:     goto L1
 120: L4: param "%d %d\n"
 121:     param argc
 122:     param letters
 123:     call printf, 3
 124:     return argc


=== Semantic Symbol Table ===
Name               Kind           Type                       Storage  Scope                          Line  Size  Uses  Unique Name          Mangled Name             Notes
----               ----           ----                       -------  -----                          ----  ----  ----  -----------          ------------             -----
main               function       int (int, char **)         -        global                         4     -     0     main                 main                     defined
argc               parameter      int                        param    global > main()                4     4     3     argc.1               -                        
argv               parameter      char **                    param    global > main()                4     4     2     argv.2               -                        
letters            variable       int                        local    global > main()                5     4     2     letters.3            -                        
i                  variable       int                        local    global > main() > for          6     4     5     i.4                  -                        
s                  variable       char *                     local    global > main() > for > for body 7     4     2     s.5                  -                        

=== Record Layouts ===
(no records)
