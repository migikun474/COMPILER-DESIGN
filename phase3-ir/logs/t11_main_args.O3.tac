=========================================
         THREE ADDRESS CODE
=========================================

Source File  : test/t11_main_args.c
Optimization : -O3: -O2 plus inlining and loop optimizations

Optimized three address code (-O3): 31 -> 23 instruction(s) for 'test/t11_main_args.c'.

optimization summary (-O3)
    instructions                31 -> 23   (25% fewer)
    constants folded            0
    algebraic simplifications   2
    common subexpressions       0
    copies / constants forwarded 2
    temporaries merged away     4
    dead instructions removed   2
    jumps removed or redirected 2
    unreachable instructions    0
    propagated across blocks    0
    dead assignments removed    0
    calls inlined               0
    tail calls turned to jumps  0
    common across blocks        2
    moved out of loops          0

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
 111: L3: t9 = *t2
 112:     param "%d: %s\n"
 113:     param i
 114:     param t9
 115:     call printf, 3
 116:     i = i int+ 1
 117:     goto L1
 118: L4: param "%d %d\n"
 119:     param argc
 120:     param letters
 121:     call printf, 3
 122:     return argc


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
