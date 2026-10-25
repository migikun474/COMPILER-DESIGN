# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t29_registers.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 37, 100, 32, 37, 100, 10, 0
str1:
        .byte 114, 101, 103, 105, 115, 116, 101, 114, 32, 97, 108, 108, 111, 99, 97, 116
        .byte 105, 111, 110, 0
str2:
        .byte 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122, 122
        .byte 122, 122, 122, 122, 0
str3:
        .byte 37, 46, 52, 102, 32, 37, 46, 52, 102, 32, 37, 46, 52, 102, 10, 0
str4:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
        .align 3
fc0:  .word 0, 1073741824        # 2
        .align 3
fc1:  .word 0, 1073217536        # 1.5
        .align 3
fc2:  .word 0, 1074003968        # 2.5
        .align 3
fc3:  .word 0, 1070596096        # 0.25
        .align 3
fc4:  .word 0, 1074790400        # 4
        .align 3
fc5:  .word 0, 1069547520        # 0.125
        .align 3
fc6:  .word 0, 1075838976        # 8
        .align 3
fc7:  .word 0, 1076920320        # 16.5
        .align 3
fc8:  .word 0, 0        # 0
        .align 3
fc9:  .word 1056964608        # 0.5
        .align 3
fc10:  .word 1069547520        # 1.5
        .align 3
fc11:  .word 0, 1083129856        # 1000

        .text
        .globl main
main:
        li    $t0, -8
        and   $sp, $sp, $t0           # frames assume an 8-byte aligned stack
        addiu $sp, $sp, -8
        sw    $a0, 0($sp)             # argc
        sw    $a1, 4($sp)             # argv
        jal   main_
        move  $a0, $v0
        li    $v0, 17                 # exit with main's result
        syscall

# depth(int)
_Z5depthi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        # t1 = n int* 2
        lw    $t0, 8($fp)
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # a = t1
        lw    $t0, -20($fp)
        sw    $t0, -4($fp)
        # t2 = n int+ 7
        lw    $t0, 8($fp)
        li    $t1, 7
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # b = t2
        lw    $t0, -24($fp)
        sw    $t0, -8($fp)
        # t3 = a int- b
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # c = t3
        lw    $t0, -28($fp)
        sw    $t0, -12($fp)
        # if n int== 0 goto 8
        lw    $t0, 8($fp)
        li    $t1, 0
        beq   $t0, $t1, L0_8
        # goto 9
        j     L0_9
L0_8:
        # return 1
        li    $v0, 1
        j     _Z5depthi_exit
L0_9:
        # t4 = n int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # param t4
        # t5 = call depth(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -32($fp)
        sw    $t0, 0($sp)
        jal   _Z5depthi
        addiu $sp, $sp, 8
        sw    $v0, -36($fp)
        # below = t5
        lw    $t0, -36($fp)
        sw    $t0, -16($fp)
        # t6 = a int+ b
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -40($fp)
        # t7 = t6 int+ c
        lw    $t0, -40($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t8 = t7 int+ below
        lw    $t0, -44($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # return t8
        lw    $v0, -48($fp)
        j     _Z5depthi_exit
_Z5depthi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# many(int)
_Z4manyi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -208
        # t1 = x int+ 1
        lw    $t0, 8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # a = t1
        lw    $t0, -60($fp)
        sw    $t0, -4($fp)
        # t2 = x int+ 2
        lw    $t0, 8($fp)
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -64($fp)
        # b = t2
        lw    $t0, -64($fp)
        sw    $t0, -8($fp)
        # t3 = x int+ 3
        lw    $t0, 8($fp)
        li    $t1, 3
        addu  $t0, $t0, $t1
        sw    $t0, -68($fp)
        # c = t3
        lw    $t0, -68($fp)
        sw    $t0, -12($fp)
        # t4 = x int+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -72($fp)
        # d = t4
        lw    $t0, -72($fp)
        sw    $t0, -16($fp)
        # t5 = x int+ 5
        lw    $t0, 8($fp)
        li    $t1, 5
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # e = t5
        lw    $t0, -76($fp)
        sw    $t0, -20($fp)
        # t6 = x int+ 6
        lw    $t0, 8($fp)
        li    $t1, 6
        addu  $t0, $t0, $t1
        sw    $t0, -80($fp)
        # f = t6
        lw    $t0, -80($fp)
        sw    $t0, -24($fp)
        # t7 = x int+ 7
        lw    $t0, 8($fp)
        li    $t1, 7
        addu  $t0, $t0, $t1
        sw    $t0, -84($fp)
        # g = t7
        lw    $t0, -84($fp)
        sw    $t0, -28($fp)
        # t8 = x int+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -88($fp)
        # h = t8
        lw    $t0, -88($fp)
        sw    $t0, -32($fp)
        # t9 = x int+ 9
        lw    $t0, 8($fp)
        li    $t1, 9
        addu  $t0, $t0, $t1
        sw    $t0, -92($fp)
        # i = t9
        lw    $t0, -92($fp)
        sw    $t0, -36($fp)
        # t10 = x int+ 10
        lw    $t0, 8($fp)
        li    $t1, 10
        addu  $t0, $t0, $t1
        sw    $t0, -96($fp)
        # j = t10
        lw    $t0, -96($fp)
        sw    $t0, -40($fp)
        # t11 = x int+ 11
        lw    $t0, 8($fp)
        li    $t1, 11
        addu  $t0, $t0, $t1
        sw    $t0, -100($fp)
        # k = t11
        lw    $t0, -100($fp)
        sw    $t0, -44($fp)
        # t12 = x int+ 12
        lw    $t0, 8($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -104($fp)
        # l = t12
        lw    $t0, -104($fp)
        sw    $t0, -48($fp)
        # s = 0
        li    $t0, 0
        sw    $t0, -52($fp)
        # t = 0
        li    $t0, 0
        sw    $t0, -56($fp)
L1_26:
        # if t int< 3 goto 28
        lw    $t0, -56($fp)
        li    $t1, 3
        blt   $t0, $t1, L1_28
        # goto 45
        j     L1_45
L1_28:
        # t13 = a int* b
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -108($fp)
        # t14 = c int* d
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -112($fp)
        # t15 = t13 int+ t14
        lw    $t0, -108($fp)
        lw    $t1, -112($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -116($fp)
        # t16 = e int* f
        lw    $t0, -20($fp)
        lw    $t1, -24($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -120($fp)
        # t17 = t15 int+ t16
        lw    $t0, -116($fp)
        lw    $t1, -120($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -124($fp)
        # t18 = g int* h
        lw    $t0, -28($fp)
        lw    $t1, -32($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -128($fp)
        # t19 = t17 int+ t18
        lw    $t0, -124($fp)
        lw    $t1, -128($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -132($fp)
        # t20 = i int* j
        lw    $t0, -36($fp)
        lw    $t1, -40($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -136($fp)
        # t21 = t19 int+ t20
        lw    $t0, -132($fp)
        lw    $t1, -136($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -140($fp)
        # t22 = k int* l
        lw    $t0, -44($fp)
        lw    $t1, -48($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -144($fp)
        # t23 = t21 int+ t22
        lw    $t0, -140($fp)
        lw    $t1, -144($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -148($fp)
        # t24 = t23 int+ t
        lw    $t0, -148($fp)
        lw    $t1, -56($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -152($fp)
        # t25 = s int+ t24
        lw    $t0, -52($fp)
        lw    $t1, -152($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -156($fp)
        # s = t25
        lw    $t0, -156($fp)
        sw    $t0, -52($fp)
        # t26 = t int+ 1
        lw    $t0, -56($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -160($fp)
        # t = t26
        lw    $t0, -160($fp)
        sw    $t0, -56($fp)
        # goto 26
        j     L1_26
L1_45:
        # t27 = s int+ a
        lw    $t0, -52($fp)
        lw    $t1, -4($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -164($fp)
        # t28 = t27 int+ b
        lw    $t0, -164($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -168($fp)
        # t29 = t28 int+ c
        lw    $t0, -168($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -172($fp)
        # t30 = t29 int+ d
        lw    $t0, -172($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -176($fp)
        # t31 = t30 int+ e
        lw    $t0, -176($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -180($fp)
        # t32 = t31 int+ f
        lw    $t0, -180($fp)
        lw    $t1, -24($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -184($fp)
        # t33 = t32 int+ g
        lw    $t0, -184($fp)
        lw    $t1, -28($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -188($fp)
        # t34 = t33 int+ h
        lw    $t0, -188($fp)
        lw    $t1, -32($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -192($fp)
        # t35 = t34 int+ i
        lw    $t0, -192($fp)
        lw    $t1, -36($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -196($fp)
        # t36 = t35 int+ j
        lw    $t0, -196($fp)
        lw    $t1, -40($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -200($fp)
        # t37 = t36 int+ k
        lw    $t0, -200($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -204($fp)
        # t38 = t37 int+ l
        lw    $t0, -204($fp)
        lw    $t1, -48($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -208($fp)
        # return t38
        lw    $v0, -208($fp)
        j     _Z4manyi_exit
_Z4manyi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# three(int, int, int)
_Z5threeiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = p int* 100
        lw    $t0, 8($fp)
        li    $t1, 100
        mul   $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = q int* 10
        lw    $t0, 12($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = t1 int+ t2
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = t3 int+ r
        lw    $t0, -12($fp)
        lw    $t1, 16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # return t4
        lw    $v0, -16($fp)
        j     _Z5threeiii_exit
_Z5threeiii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# twice(int)
_Z5twicei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = v int* 2
        lw    $t0, 8($fp)
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -4($fp)
        # return t1
        lw    $v0, -4($fp)
        j     _Z5twicei_exit
_Z5twicei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# arguments(int, int, int)
_Z9argumentsiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        # t1 = a int+ 1
        lw    $t0, 8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # x = t1
        lw    $t0, -16($fp)
        sw    $t0, -4($fp)
        # param b
        # t2 = call twice(int), 1
        addiu $sp, $sp, -8
        lw    $t0, 12($fp)
        sw    $t0, 0($sp)
        jal   _Z5twicei
        addiu $sp, $sp, 8
        sw    $v0, -20($fp)
        # t3 = c int- 1
        lw    $t0, 16($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # param x
        # param t2
        # param t3
        # t4 = call three(int, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        lw    $t0, -20($fp)
        sw    $t0, 4($sp)
        lw    $t0, -24($fp)
        sw    $t0, 8($sp)
        jal   _Z5threeiii
        addiu $sp, $sp, 16
        sw    $v0, -28($fp)
        # y = t4
        lw    $t0, -28($fp)
        sw    $t0, -8($fp)
        # param a
        # t5 = call twice(int), 1
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        jal   _Z5twicei
        addiu $sp, $sp, 8
        sw    $v0, -32($fp)
        # param b
        # t6 = call twice(int), 1
        addiu $sp, $sp, -8
        lw    $t0, 12($fp)
        sw    $t0, 0($sp)
        jal   _Z5twicei
        addiu $sp, $sp, 8
        sw    $v0, -36($fp)
        # param t6
        # t7 = call twice(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -36($fp)
        sw    $t0, 0($sp)
        jal   _Z5twicei
        addiu $sp, $sp, 8
        sw    $v0, -40($fp)
        # param c
        # t8 = call twice(int), 1
        addiu $sp, $sp, -8
        lw    $t0, 16($fp)
        sw    $t0, 0($sp)
        jal   _Z5twicei
        addiu $sp, $sp, 8
        sw    $v0, -44($fp)
        # t9 = t8 int+ x
        lw    $t0, -44($fp)
        lw    $t1, -4($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # param t5
        # param t7
        # param t9
        # t10 = call three(int, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -32($fp)
        sw    $t0, 0($sp)
        lw    $t0, -40($fp)
        sw    $t0, 4($sp)
        lw    $t0, -48($fp)
        sw    $t0, 8($sp)
        jal   _Z5threeiii
        addiu $sp, $sp, 16
        sw    $v0, -52($fp)
        # z = t10
        lw    $t0, -52($fp)
        sw    $t0, -12($fp)
        # t11 = y int+ z
        lw    $t0, -8($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -56($fp)
        # return t11
        lw    $v0, -56($fp)
        j     _Z9argumentsiii_exit
_Z9argumentsiii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# characters(const char *)
_Z10charactersPKc:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -184
        # c = 0
        li    $t0, 0
        sb    $t0, -1($fp)
        # u = 0
        li    $t0, 0
        sb    $t0, -2($fp)
        # h = 0
        li    $t0, 0
        sh    $t0, -4($fp)
        # any = 0
        li    $t0, 0
        sb    $t0, -5($fp)
        # signs = 0
        li    $t0, 0
        sw    $t0, -12($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -16($fp)
L5_6:
        # t1 = s ptr+ i
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t2 = *t1
        lw    $t8, -24($fp)
        lb    $t0, 0($t8)
        sb    $t0, -25($fp)
        # if t2 char!= 0 goto 10
        lb    $t0, -25($fp)
        li    $t1, 0
        bne   $t0, $t1, L5_10
        # goto 55
        j     L5_55
L5_10:
        # t3 = chartoint c
        lb    $t0, -1($fp)
        sw    $t0, -32($fp)
        # t4 = s ptr+ i
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # t5 = *t4
        lw    $t8, -36($fp)
        lb    $t0, 0($t8)
        sb    $t0, -37($fp)
        # t6 = chartoint t5
        lb    $t0, -37($fp)
        sw    $t0, -44($fp)
        # t7 = t3 int+ t6
        lw    $t0, -32($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # t8 = inttochar t7
        lw    $t0, -48($fp)
        sb    $t0, -49($fp)
        # c = t8
        lb    $t0, -49($fp)
        sb    $t0, -1($fp)
        # t9 = uchartoint u
        lbu   $t0, -2($fp)
        sw    $t0, -56($fp)
        # t10 = s ptr+ i
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # t11 = *t10
        lw    $t8, -60($fp)
        lb    $t0, 0($t8)
        sb    $t0, -61($fp)
        # t12 = chartoint t11
        lb    $t0, -61($fp)
        sw    $t0, -68($fp)
        # t13 = t9 int+ t12
        lw    $t0, -56($fp)
        lw    $t1, -68($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -72($fp)
        # t14 = inttouchar t13
        lw    $t0, -72($fp)
        sb    $t0, -73($fp)
        # u = t14
        lbu   $t0, -73($fp)
        sb    $t0, -2($fp)
        # t15 = shorttoint h
        lh    $t0, -4($fp)
        sw    $t0, -80($fp)
        # t16 = t15 int* 31
        lw    $t0, -80($fp)
        li    $t1, 31
        mul   $t0, $t0, $t1
        sw    $t0, -84($fp)
        # t17 = s ptr+ i
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -88($fp)
        # t18 = *t17
        lw    $t8, -88($fp)
        lb    $t0, 0($t8)
        sb    $t0, -89($fp)
        # t19 = chartoint t18
        lb    $t0, -89($fp)
        sw    $t0, -96($fp)
        # t20 = t16 int+ t19
        lw    $t0, -84($fp)
        lw    $t1, -96($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -100($fp)
        # t21 = inttoshort t20
        lw    $t0, -100($fp)
        sh    $t0, -102($fp)
        # h = t21
        lh    $t0, -102($fp)
        sh    $t0, -4($fp)
        # t22 = chartoint c
        lb    $t0, -1($fp)
        sw    $t0, -108($fp)
        # if t22 int< 0 goto 35
        lw    $t0, -108($fp)
        li    $t1, 0
        blt   $t0, $t1, L5_35
        # goto 37
        j     L5_37
L5_35:
        # t23 = signs int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -112($fp)
        # signs = t23
        lw    $t0, -112($fp)
        sw    $t0, -12($fp)
L5_37:
        # if any bool!= 0 goto 46
        lbu   $t0, -5($fp)
        li    $t1, 0
        bne   $t0, $t1, L5_46
        # goto 39
        j     L5_39
L5_39:
        # t25 = s ptr+ i
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -120($fp)
        # t26 = *t25
        lw    $t8, -120($fp)
        lb    $t0, 0($t8)
        sb    $t0, -121($fp)
        # t27 = chartoint t26
        lb    $t0, -121($fp)
        sw    $t0, -128($fp)
        # if t27 int== 122 goto 46
        lw    $t0, -128($fp)
        li    $t1, 122
        beq   $t0, $t1, L5_46
        # goto 44
        j     L5_44
L5_44:
        # t24 = 0
        li    $t0, 0
        sw    $t0, -116($fp)
        # goto 47
        j     L5_47
L5_46:
        # t24 = 1
        li    $t0, 1
        sw    $t0, -116($fp)
L5_47:
        # if t24 int!= 0 goto 50
        lw    $t0, -116($fp)
        li    $t1, 0
        bne   $t0, $t1, L5_50
        # t28 = 0
        li    $t0, 0
        sb    $t0, -129($fp)
        # goto 51
        j     L5_51
L5_50:
        # t28 = 1
        li    $t0, 1
        sb    $t0, -129($fp)
L5_51:
        # any = t28
        lbu   $t0, -129($fp)
        sb    $t0, -5($fp)
        # t29 = i int+ 1
        lw    $t0, -16($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -136($fp)
        # i = t29
        lw    $t0, -136($fp)
        sw    $t0, -16($fp)
        # goto 6
        j     L5_6
L5_55:
        # same = c
        lbu   $t0, -1($fp)
        sb    $t0, -17($fp)
        # t30 = chartoint c
        lb    $t0, -1($fp)
        sw    $t0, -140($fp)
        # t31 = uchartoint u
        lbu   $t0, -2($fp)
        sw    $t0, -144($fp)
        # t32 = t31 int* 2
        lw    $t0, -144($fp)
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -148($fp)
        # t33 = t30 int+ t32
        lw    $t0, -140($fp)
        lw    $t1, -148($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -152($fp)
        # t34 = shorttoint h
        lh    $t0, -4($fp)
        sw    $t0, -156($fp)
        # t35 = t33 int+ t34
        lw    $t0, -152($fp)
        lw    $t1, -156($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -160($fp)
        # t36 = signs int* 1000
        lw    $t0, -12($fp)
        li    $t1, 1000
        mul   $t0, $t0, $t1
        sw    $t0, -164($fp)
        # t37 = t35 int+ t36
        lw    $t0, -160($fp)
        lw    $t1, -164($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -168($fp)
        # t38 = booltoint any
        lbu   $t0, -5($fp)
        sw    $t0, -172($fp)
        # t39 = t37 int+ t38
        lw    $t0, -168($fp)
        lw    $t1, -172($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -176($fp)
        # t40 = uchartoint same
        lbu   $t0, -17($fp)
        sw    $t0, -180($fp)
        # t41 = t39 int+ t40
        lw    $t0, -176($fp)
        lw    $t1, -180($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -184($fp)
        # return t41
        lw    $v0, -184($fp)
        j     _Z10charactersPKc_exit
_Z10charactersPKc_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# half(double)
_Z4halfd:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = v double/ 2.0
        l.d   $f0, 8($fp)
        l.d   $f2, fc0
        div.d $f0, $f0, $f2
        s.d   $f0, -8($fp)
        # return t1
        l.d   $f0, -8($fp)
        j     _Z4halfd_exit
_Z4halfd_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# numbers(int)
_Z7numbersi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -192
        # a = 1.5
        l.d   $f0, fc1
        s.d   $f0, -8($fp)
        # b = 2.5
        l.d   $f0, fc2
        s.d   $f0, -16($fp)
        # c = 0.25
        l.d   $f0, fc3
        s.d   $f0, -24($fp)
        # d = 4.0
        l.d   $f0, fc4
        s.d   $f0, -32($fp)
        # e = 0.125
        l.d   $f0, fc5
        s.d   $f0, -40($fp)
        # f = 8.0
        l.d   $f0, fc6
        s.d   $f0, -48($fp)
        # g = 16.5
        l.d   $f0, fc7
        s.d   $f0, -56($fp)
        # total = 0.0
        l.d   $f0, fc8
        s.d   $f0, -64($fp)
        # small = 0.5
        l.s   $f0, fc9
        s.s   $f0, -68($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -72($fp)
L7_10:
        # if i int< n goto 12
        lw    $t0, -72($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L7_12
        # goto 33
        j     L7_33
L7_12:
        # t1 = a double* b
        l.d   $f0, -8($fp)
        l.d   $f2, -16($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -80($fp)
        # t2 = c double* d
        l.d   $f0, -24($fp)
        l.d   $f2, -32($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -88($fp)
        # t3 = t1 double+ t2
        l.d   $f0, -80($fp)
        l.d   $f2, -88($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -96($fp)
        # t4 = e double* f
        l.d   $f0, -40($fp)
        l.d   $f2, -48($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -104($fp)
        # t5 = t3 double+ t4
        l.d   $f0, -96($fp)
        l.d   $f2, -104($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -112($fp)
        # t6 = t5 double+ g
        l.d   $f0, -112($fp)
        l.d   $f2, -56($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -120($fp)
        # t7 = total double+ t6
        l.d   $f0, -64($fp)
        l.d   $f2, -120($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -128($fp)
        # total = t7
        l.d   $f0, -128($fp)
        s.d   $f0, -64($fp)
        # param total
        # t8 = call half(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, -64($fp)
        s.d   $f0, 0($sp)
        jal   _Z4halfd
        addiu $sp, $sp, 8
        s.d   $f0, -136($fp)
        # t9 = floattodouble small
        l.s   $f0, -68($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -144($fp)
        # t10 = t8 double+ t9
        l.d   $f0, -136($fp)
        l.d   $f2, -144($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -152($fp)
        # total = t10
        l.d   $f0, -152($fp)
        s.d   $f0, -64($fp)
        # t11 = small float* 1.5
        l.s   $f0, -68($fp)
        l.s   $f2, fc10
        mul.s $f0, $f0, $f2
        s.s   $f0, -156($fp)
        # small = t11
        l.s   $f0, -156($fp)
        s.s   $f0, -68($fp)
        # if total double> 1e+03 goto 29
        l.d   $f0, -64($fp)
        l.d   $f2, fc11
        c.lt.d $f2, $f0
        bc1t  L7_29
        # goto 30
        j     L7_30
L7_29:
        # goto 33
        j     L7_33
L7_30:
        # t12 = i int+ 1
        lw    $t0, -72($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -160($fp)
        # i = t12
        lw    $t0, -160($fp)
        sw    $t0, -72($fp)
        # goto 10
        j     L7_10
L7_33:
        # t13 = total double+ a
        l.d   $f0, -64($fp)
        l.d   $f2, -8($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -168($fp)
        # t14 = t13 double+ g
        l.d   $f0, -168($fp)
        l.d   $f2, -56($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -176($fp)
        # t15 = floattodouble small
        l.s   $f0, -68($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -184($fp)
        # t16 = t14 double+ t15
        l.d   $f0, -176($fp)
        l.d   $f2, -184($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -192($fp)
        # return t16
        l.d   $f0, -192($fp)
        j     _Z7numbersi_exit
_Z7numbersi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# jumps(int)
_Z5jumpsi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        # i = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # s = 0
        li    $t0, 0
        sw    $t0, -8($fp)
        # t1 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -16($fp)
        # last = t1
        lw    $t0, -16($fp)
        sw    $t0, -12($fp)
L8_4:
        # if i int>= n goto 6
        lw    $t0, -4($fp)
        lw    $t1, 8($fp)
        bge   $t0, $t1, L8_6
        # goto 7
        j     L8_7
L8_6:
        # goto 14
        j     L8_14
L8_7:
        # t2 = i int* i
        lw    $t0, -4($fp)
        lw    $t1, -4($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t3 = s int+ t2
        lw    $t0, -8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # s = t3
        lw    $t0, -24($fp)
        sw    $t0, -8($fp)
        # last = i
        lw    $t0, -4($fp)
        sw    $t0, -12($fp)
        # t4 = i int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # i = t4
        lw    $t0, -28($fp)
        sw    $t0, -4($fp)
        # goto 4
        j     L8_4
L8_14:
        # t5 = s int* 10
        lw    $t0, -8($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t6 = t5 int+ last
        lw    $t0, -32($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # return t6
        lw    $v0, -36($fp)
        j     _Z5jumpsi_exit
_Z5jumpsi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# mixed(int)
_Z5mixedi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        # t1 = n int* 3
        lw    $t0, 8($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -24($fp)
        # before = t1
        lw    $t0, -24($fp)
        sw    $t0, -4($fp)
        # sum = 0
        li    $t0, 0
        sw    $t0, -8($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -12($fp)
L9_4:
        # if i int< n goto 6
        lw    $t0, -12($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L9_6
        # goto 23
        j     L9_23
L9_6:
        # t2 = i int* before
        lw    $t0, -12($fp)
        lw    $t1, -4($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -28($fp)
        # inside = t2
        lw    $t0, -28($fp)
        sw    $t0, -16($fp)
        # t3 = inside int% 7
        lw    $t0, -16($fp)
        li    $t1, 7
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -32($fp)
        # t4 = sum int+ t3
        lw    $t0, -8($fp)
        lw    $t1, -32($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # sum = t4
        lw    $t0, -36($fp)
        sw    $t0, -8($fp)
        # if sum int> 50 goto 13
        lw    $t0, -8($fp)
        li    $t1, 50
        bgt   $t0, $t1, L9_13
        # goto 16
        j     L9_16
L9_13:
        # t5 = sum int- before
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -40($fp)
        # sum = t5
        lw    $t0, -40($fp)
        sw    $t0, -8($fp)
        # goto 20
        j     L9_20
L9_16:
        # param i
        # t6 = call twice(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -12($fp)
        sw    $t0, 0($sp)
        jal   _Z5twicei
        addiu $sp, $sp, 8
        sw    $v0, -44($fp)
        # t7 = sum int+ t6
        lw    $t0, -8($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # sum = t7
        lw    $t0, -48($fp)
        sw    $t0, -8($fp)
L9_20:
        # t8 = i int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -52($fp)
        # i = t8
        lw    $t0, -52($fp)
        sw    $t0, -12($fp)
        # goto 4
        j     L9_4
L9_23:
        # t9 = sum int+ before
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -56($fp)
        # after = t9
        lw    $t0, -56($fp)
        sw    $t0, -20($fp)
        # return after
        lw    $v0, -20($fp)
        j     _Z5mixedi_exit
_Z5mixedi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# main()
main_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -72
        # param 5
        # t1 = call depth(int), 1
        addiu $sp, $sp, -8
        li    $t0, 5
        sw    $t0, 0($sp)
        jal   _Z5depthi
        addiu $sp, $sp, 8
        sw    $v0, -4($fp)
        # param 3
        # t2 = call many(int), 1
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        jal   _Z4manyi
        addiu $sp, $sp, 8
        sw    $v0, -8($fp)
        # param "%d %d\n"
        # param t1
        # param t2
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        lw    $t0, -8($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 1
        # param 2
        # param 3
        # t3 = call arguments(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 1
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        li    $t0, 3
        sw    $t0, 8($sp)
        jal   _Z9argumentsiii
        addiu $sp, $sp, 16
        sw    $v0, -12($fp)
        # param 4
        # param 0
        # param 9
        # t4 = call arguments(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 4
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z9argumentsiii
        addiu $sp, $sp, 16
        sw    $v0, -16($fp)
        # param "%d %d\n"
        # param t3
        # param t4
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -12($fp)
        sw    $t0, 4($sp)
        lw    $t0, -16($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param "register allocation"
        # t5 = call characters(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        jal   _Z10charactersPKc
        addiu $sp, $sp, 8
        sw    $v0, -20($fp)
        # param "zzzzzzzzzzzzzzzzzzzz"
        # t6 = call characters(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        jal   _Z10charactersPKc
        addiu $sp, $sp, 8
        sw    $v0, -24($fp)
        # param "%d %d\n"
        # param t5
        # param t6
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -20($fp)
        sw    $t0, 4($sp)
        lw    $t0, -24($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 0
        # t7 = call numbers(int), 1
        addiu $sp, $sp, -8
        li    $t0, 0
        sw    $t0, 0($sp)
        jal   _Z7numbersi
        addiu $sp, $sp, 8
        s.d   $f0, -32($fp)
        # param 3
        # t8 = call numbers(int), 1
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        jal   _Z7numbersi
        addiu $sp, $sp, 8
        s.d   $f0, -40($fp)
        # param 40
        # t9 = call numbers(int), 1
        addiu $sp, $sp, -8
        li    $t0, 40
        sw    $t0, 0($sp)
        jal   _Z7numbersi
        addiu $sp, $sp, 8
        s.d   $f0, -48($fp)
        # param "%.4f %.4f %.4f\n"
        # param t7
        # param t8
        # param t9
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str3
        sw    $t0, 0($sp)
        l.d   $f0, -32($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -40($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -48($fp)
        s.d   $f0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 0
        # t10 = call jumps(int), 1
        addiu $sp, $sp, -8
        li    $t0, 0
        sw    $t0, 0($sp)
        jal   _Z5jumpsi
        addiu $sp, $sp, 8
        sw    $v0, -52($fp)
        # param 5
        # t11 = call jumps(int), 1
        addiu $sp, $sp, -8
        li    $t0, 5
        sw    $t0, 0($sp)
        jal   _Z5jumpsi
        addiu $sp, $sp, 8
        sw    $v0, -56($fp)
        # param 9
        # t12 = call mixed(int), 1
        addiu $sp, $sp, -8
        li    $t0, 9
        sw    $t0, 0($sp)
        jal   _Z5mixedi
        addiu $sp, $sp, 8
        sw    $v0, -60($fp)
        # param "%d %d %d\n"
        # param t10
        # param t11
        # param t12
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -52($fp)
        sw    $t0, 4($sp)
        lw    $t0, -56($fp)
        sw    $t0, 8($sp)
        lw    $t0, -60($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 3
        # t13 = call jumps(int), 1
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        jal   _Z5jumpsi
        addiu $sp, $sp, 8
        sw    $v0, -64($fp)
        # t14 = t13 int% 100
        lw    $t0, -64($fp)
        li    $t1, 100
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -68($fp)
        # return t14
        lw    $v0, -68($fp)
        j     main__exit
main__exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# =====================================================================
# Run-time library for the generated code (SPIM has no C library).
#
#   __printf __scanf          arguments on the stack, like any function:
#   __malloc __calloc         0($sp) is the first argument; result in $v0
#   __realloc __free
#   __memcpy                  $a0 = to, $a1 = from, $a2 = bytes (registers only)
#   __divll __modll           64-bit helpers: a in $a1:$a0, b in $a3:$a2,
#   __udivll __umodll         result in $v1:$v0
#   __shlll __shrll __sarll   a in $a1:$a0, count in $a2
#   __dtoll                   double in $f12 -> $v1:$v0
#
# The generated code keeps nothing in registers across a call, so these
# routines use the temporaries freely; they preserve $sp, $fp and $s0-$s7.
# =====================================================================

        .data
__pf_buf:    .space 96
__pf_digits: .asciiz "0123456789abcdef"
        .align 2
__sc_peek:   .word -2                   # a character read ahead; -2 = none, -1 = end of input
__sc_pos:    .word __sc_line            # the next unread character of the current input line
__sc_line:   .space 132
        .align 3
__c_2p32:    .double 4294967296.0
__c_2p31:    .double 2147483648.0
__c_ten:     .double 10.0
__c_half:    .double 0.5
__c_zero:    .double 0.0
__c_one:     .double 1.0
__pf_mend:   .word 0                    # %g: where the digits end (the exponent, if any, follows)

        .text

# ---------------------------------------------------------------- memory
__memcpy:
        beqz  $a2, __memcpy_done
__memcpy_loop:
        lbu   $t8, 0($a1)
        sb    $t8, 0($a0)
        addiu $a0, $a0, 1
        addiu $a1, $a1, 1
        addiu $a2, $a2, -1
        bnez  $a2, __memcpy_loop
__memcpy_done:
        jr    $ra

__malloc:                               # malloc(size)
        lw    $t0, 0($sp)
__malloc_n:                             # size in $t0; the block is 8-byte aligned,
        addiu $a0, $t0, 23              # with its size in the 8 bytes before it
        li    $t1, -8
        and   $a0, $a0, $t1
        li    $v0, 9                    # sbrk
        syscall
        addiu $v0, $v0, 7
        and   $v0, $v0, $t1
        sw    $t0, 0($v0)
        addiu $v0, $v0, 8
        jr    $ra

__calloc:                               # calloc(count, size): fresh memory is already zero
        lw    $t0, 0($sp)
        lw    $t1, 4($sp)
        mul   $t0, $t0, $t1
        j     __malloc_n

__realloc:                              # realloc(pointer, size): a new block and a copy
        lw    $t2, 0($sp)
        lw    $t0, 4($sp)
        move  $t9, $ra
        jal   __malloc_n
        beqz  $t2, __realloc_done
        lw    $t3, -8($t2)              # the old size
        sltu  $t4, $t0, $t3
        beqz  $t4, __realloc_copy
        move  $t3, $t0
__realloc_copy:
        move  $t5, $v0
        move  $a0, $v0
        move  $a1, $t2
        move  $a2, $t3
        jal   __memcpy
        move  $v0, $t5
__realloc_done:
        jr    $t9

__free:                                 # memory is not reused
        jr    $ra

# ------------------------------------------------------- 64-bit arithmetic
__udivmodll:                            # unsigned: quotient $v1:$v0, remainder $t9:$t8
        li    $v0, 0
        li    $v1, 0
        li    $t8, 0
        li    $t9, 0
        li    $t7, 64
__udm_loop:
        srl   $t6, $t8, 31              # remainder = remainder * 2 + next bit of a
        sll   $t9, $t9, 1
        or    $t9, $t9, $t6
        sll   $t8, $t8, 1
        srl   $t6, $a1, 31
        or    $t8, $t8, $t6
        srl   $t6, $a0, 31
        sll   $a1, $a1, 1
        or    $a1, $a1, $t6
        sll   $a0, $a0, 1
        srl   $t6, $v0, 31              # quotient = quotient * 2
        sll   $v1, $v1, 1
        or    $v1, $v1, $t6
        sll   $v0, $v0, 1
        bltu  $t9, $a3, __udm_next      # if remainder >= b: subtract, quotient bit = 1
        bne   $t9, $a3, __udm_sub
        bltu  $t8, $a2, __udm_next
__udm_sub:
        sltu  $t6, $t8, $a2
        subu  $t8, $t8, $a2
        subu  $t9, $t9, $a3
        subu  $t9, $t9, $t6
        ori   $v0, $v0, 1
__udm_next:
        addiu $t7, $t7, -1
        bnez  $t7, __udm_loop
        jr    $ra

__udivll:
        j     __udivmodll

__umodll:
        move  $t5, $ra
        jal   __udivmodll
        move  $v0, $t8
        move  $v1, $t9
        jr    $t5

__divll:                                # signed: divide the magnitudes, then fix the sign
        move  $t5, $ra
        xor   $t4, $a1, $a3             # negative if the signs differ
        bgez  $a1, __divll_b
        sltu  $t6, $zero, $a0
        negu  $a0, $a0
        negu  $a1, $a1
        subu  $a1, $a1, $t6
__divll_b:
        bgez  $a3, __divll_go
        sltu  $t6, $zero, $a2
        negu  $a2, $a2
        negu  $a3, $a3
        subu  $a3, $a3, $t6
__divll_go:
        jal   __udivmodll
        bgez  $t4, __divll_done
        sltu  $t6, $zero, $v0
        negu  $v0, $v0
        negu  $v1, $v1
        subu  $v1, $v1, $t6
__divll_done:
        jr    $t5

__modll:                                # the remainder has the sign of a
        move  $t5, $ra
        move  $t4, $a1
        bgez  $a1, __modll_b
        sltu  $t6, $zero, $a0
        negu  $a0, $a0
        negu  $a1, $a1
        subu  $a1, $a1, $t6
__modll_b:
        bgez  $a3, __modll_go
        sltu  $t6, $zero, $a2
        negu  $a2, $a2
        negu  $a3, $a3
        subu  $a3, $a3, $t6
__modll_go:
        jal   __udivmodll
        move  $v0, $t8
        move  $v1, $t9
        bgez  $t4, __modll_done
        sltu  $t6, $zero, $v0
        negu  $v0, $v0
        negu  $v1, $v1
        subu  $v1, $v1, $t6
__modll_done:
        jr    $t5

__shlll:
        andi  $a2, $a2, 63
        move  $v0, $a0
        move  $v1, $a1
        beqz  $a2, __shift_done
        slti  $t6, $a2, 32
        beqz  $t6, __shlll_big
        li    $t7, 32
        subu  $t7, $t7, $a2
        sllv  $v1, $a1, $a2
        srlv  $t6, $a0, $t7
        or    $v1, $v1, $t6
        sllv  $v0, $a0, $a2
        jr    $ra
__shlll_big:
        addiu $t7, $a2, -32
        sllv  $v1, $a0, $t7
        li    $v0, 0
__shift_done:
        jr    $ra

__shrll:                                # logical
        andi  $a2, $a2, 63
        move  $v0, $a0
        move  $v1, $a1
        beqz  $a2, __shift_done
        slti  $t6, $a2, 32
        beqz  $t6, __shrll_big
        li    $t7, 32
        subu  $t7, $t7, $a2
        srlv  $v0, $a0, $a2
        sllv  $t6, $a1, $t7
        or    $v0, $v0, $t6
        srlv  $v1, $a1, $a2
        jr    $ra
__shrll_big:
        addiu $t7, $a2, -32
        srlv  $v0, $a1, $t7
        li    $v1, 0
        jr    $ra

__sarll:                                # arithmetic
        andi  $a2, $a2, 63
        move  $v0, $a0
        move  $v1, $a1
        beqz  $a2, __shift_done
        slti  $t6, $a2, 32
        beqz  $t6, __sarll_big
        li    $t7, 32
        subu  $t7, $t7, $a2
        srlv  $v0, $a0, $a2
        sllv  $t6, $a1, $t7
        or    $v0, $v0, $t6
        srav  $v1, $a1, $a2
        jr    $ra
__sarll_big:
        addiu $t7, $a2, -32
        srav  $v0, $a1, $t7
        sra   $v1, $a1, 31
        jr    $ra

__dtoll:                                # double -> long long, toward zero
        l.d   $f14, __c_zero
        li    $t4, 0
        c.lt.d $f12, $f14
        bc1f  __dtoll_abs
        li    $t4, 1
        neg.d $f12, $f12
__dtoll_abs:
        l.d   $f14, __c_2p32
        div.d $f16, $f12, $f14          # the high word (assumed below 2^31)
        trunc.w.d $f18, $f16
        mfc1  $v1, $f18
        cvt.d.w $f18, $f18
        mul.d $f18, $f18, $f14
        sub.d $f16, $f12, $f18          # the low word, 0 .. 2^32
        l.d   $f14, __c_2p31
        c.lt.d $f16, $f14
        bc1t  __dtoll_small
        sub.d $f16, $f16, $f14
        trunc.w.d $f18, $f16
        mfc1  $v0, $f18
        lui   $t6, 0x8000
        addu  $v0, $v0, $t6
        j     __dtoll_sign
__dtoll_small:
        trunc.w.d $f18, $f16
        mfc1  $v0, $f18
__dtoll_sign:
        beqz  $t4, __dtoll_done
        sltu  $t6, $zero, $v0
        negu  $v0, $v0
        negu  $v1, $v1
        subu  $v1, $v1, $t6
__dtoll_done:
        jr    $ra

# ---------------------------------------------------------------- printf
# %d %i %u %x %X %o %c %s %f %e %E %g %G %%, with '-' and '0' flags,
# width, precision (strings and the floating formats), '*', and the
# lengths l / ll / h.
#   $s0 format   $s1 next argument   $s2 left-justify   $s3 pad character
#   $s4 width    $s5 precision       $s6 number of 'l'  $s7 characters written
__printf:
        addiu $sp, $sp, -40
        sw    $ra, 36($sp)
        sw    $s0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        sw    $s4, 16($sp)
        sw    $s5, 20($sp)
        sw    $s6, 24($sp)
        sw    $s7, 28($sp)
        lw    $s0, 40($sp)
        addiu $s1, $sp, 44
        li    $s7, 0
__pf_loop:
        lbu   $a0, 0($s0)
        beqz  $a0, __pf_done
        addiu $s0, $s0, 1
        li    $t0, 37                   # '%'
        beq   $a0, $t0, __pf_spec
__pf_char:
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
        j     __pf_loop
__pf_spec:
        li    $s2, 0
        li    $s3, 32
        li    $s4, 0
        li    $s5, -1
        li    $s6, 0
__pf_flags:
        lbu   $t0, 0($s0)
        li    $t1, 45                   # '-'
        bne   $t0, $t1, __pf_flag0
        li    $s2, 1
        j     __pf_flagnext
__pf_flag0:
        li    $t1, 48                   # '0'
        bne   $t0, $t1, __pf_flagx
        li    $s3, 48
        j     __pf_flagnext
__pf_flagx:
        li    $t1, 43                   # '+', ' ', '#' are accepted and ignored
        beq   $t0, $t1, __pf_flagnext
        li    $t1, 32
        beq   $t0, $t1, __pf_flagnext
        li    $t1, 35
        bne   $t0, $t1, __pf_width
__pf_flagnext:
        addiu $s0, $s0, 1
        j     __pf_flags
__pf_width:
        lbu   $t0, 0($s0)
        li    $t1, 42                   # '*'
        bne   $t0, $t1, __pf_wdigit
        lw    $s4, 0($s1)
        addiu $s1, $s1, 4
        addiu $s0, $s0, 1
        bgez  $s4, __pf_prec
        li    $s2, 1
        negu  $s4, $s4
        j     __pf_prec
__pf_wdigit:
        lbu   $t0, 0($s0)
        addiu $t1, $t0, -48
        sltiu $t2, $t1, 10
        beqz  $t2, __pf_prec
        li    $t3, 10
        mul   $s4, $s4, $t3
        addu  $s4, $s4, $t1
        addiu $s0, $s0, 1
        j     __pf_wdigit
__pf_prec:
        lbu   $t0, 0($s0)
        li    $t1, 46                   # '.'
        bne   $t0, $t1, __pf_len
        addiu $s0, $s0, 1
        li    $s5, 0
        lbu   $t0, 0($s0)
        li    $t1, 42
        bne   $t0, $t1, __pf_pdigit
        lw    $s5, 0($s1)
        addiu $s1, $s1, 4
        addiu $s0, $s0, 1
        j     __pf_len
__pf_pdigit:
        lbu   $t0, 0($s0)
        addiu $t1, $t0, -48
        sltiu $t2, $t1, 10
        beqz  $t2, __pf_len
        li    $t3, 10
        mul   $s5, $s5, $t3
        addu  $s5, $s5, $t1
        addiu $s0, $s0, 1
        j     __pf_pdigit
__pf_len:
        lbu   $t0, 0($s0)
        li    $t1, 108                  # 'l'
        bne   $t0, $t1, __pf_lenh
        addiu $s6, $s6, 1
        addiu $s0, $s0, 1
        j     __pf_len
__pf_lenh:
        li    $t1, 104                  # 'h' and 'z' change nothing: the argument is one word
        beq   $t0, $t1, __pf_lenskip
        li    $t1, 122
        bne   $t0, $t1, __pf_conv
__pf_lenskip:
        addiu $s0, $s0, 1
        j     __pf_len
__pf_conv:
        lbu   $t0, 0($s0)
        beqz  $t0, __pf_done
        addiu $s0, $s0, 1
        li    $t3, 10                   # base
        li    $t4, 0                    # upper-case digits?
        li    $t1, 100
        beq   $t0, $t1, __pf_d
        li    $t1, 105
        beq   $t0, $t1, __pf_d
        li    $t1, 117
        beq   $t0, $t1, __pf_u
        li    $t1, 99
        beq   $t0, $t1, __pf_c
        li    $t1, 115
        beq   $t0, $t1, __pf_s
        li    $t1, 102
        beq   $t0, $t1, __pf_f
        li    $t9, 101                  # the exponent letter: 'e' ...
        li    $t1, 101
        beq   $t0, $t1, __pf_e
        li    $t1, 103
        beq   $t0, $t1, __pf_g
        li    $t9, 69                   # ... or 'E' for %E and %G
        li    $t1, 69
        beq   $t0, $t1, __pf_e
        li    $t1, 71
        beq   $t0, $t1, __pf_g
        li    $t3, 16
        li    $t1, 120
        beq   $t0, $t1, __pf_u
        li    $t4, 1
        li    $t1, 88
        beq   $t0, $t1, __pf_u
        li    $t4, 0
        li    $t3, 8
        li    $t1, 111
        beq   $t0, $t1, __pf_u
        move  $a0, $t0                  # "%%" and anything unknown: the character itself
        j     __pf_char

__pf_d:                                 # signed: magnitude in $t1:$t0, sign character in $t2
        slti  $t5, $s6, 2
        bnez  $t5, __pf_d32
        addiu $s1, $s1, 7
        li    $t5, -8
        and   $s1, $s1, $t5
        lw    $t0, 0($s1)
        lw    $t1, 4($s1)
        addiu $s1, $s1, 8
        j     __pf_dsign
__pf_d32:
        lw    $t0, 0($s1)
        addiu $s1, $s1, 4
        sra   $t1, $t0, 31
__pf_dsign:
        li    $t2, 0
        bgez  $t1, __pf_num
        li    $t2, 45
        sltu  $t5, $zero, $t0
        negu  $t0, $t0
        negu  $t1, $t1
        subu  $t1, $t1, $t5
        j     __pf_num
__pf_u:                                 # unsigned, base in $t3
        li    $t2, 0
        slti  $t5, $s6, 2
        bnez  $t5, __pf_u32
        addiu $s1, $s1, 7
        li    $t5, -8
        and   $s1, $s1, $t5
        lw    $t0, 0($s1)
        lw    $t1, 4($s1)
        addiu $s1, $s1, 8
        j     __pf_num
__pf_u32:
        lw    $t0, 0($s1)
        addiu $s1, $s1, 4
        li    $t1, 0
__pf_num:                               # digits into the buffer, last one first
        la    $s5, __pf_buf+95
        li    $s6, 0
        or    $t5, $t0, $t1
        bnez  $t5, __pf_nloop
        li    $t5, 0
        j     __pf_ndigit
__pf_nloop:
        or    $t5, $t0, $t1
        beqz  $t5, __pf_nout
        bnez  $t1, __pf_n64
        divu  $t0, $t3
        mflo  $t0
        mfhi  $t5
        j     __pf_ndigit
__pf_n64:
        move  $a0, $t0
        move  $a1, $t1
        move  $a2, $t3
        li    $a3, 0
        jal   __udivmodll
        move  $t0, $v0
        move  $t1, $v1
        move  $t5, $t8
__pf_ndigit:
        la    $t8, __pf_digits
        addu  $t8, $t8, $t5
        lbu   $t5, 0($t8)
        beqz  $t4, __pf_nstore
        slti  $t8, $t5, 97
        bnez  $t8, __pf_nstore
        addiu $t5, $t5, -32
__pf_nstore:
        addiu $s5, $s5, -1
        sb    $t5, 0($s5)
        addiu $s6, $s6, 1
        j     __pf_nloop
__pf_nout:
        move  $t0, $s5
        move  $t1, $s6
        jal   __pf_out
        j     __pf_loop

__pf_c:
        lw    $t5, 0($s1)
        addiu $s1, $s1, 4
        la    $t0, __pf_buf
        sb    $t5, 0($t0)
        li    $t1, 1
        li    $t2, 0
        li    $s3, 32
        jal   __pf_out
        j     __pf_loop

__pf_s:
        lw    $t0, 0($s1)
        addiu $s1, $s1, 4
        move  $t3, $t0
        li    $t1, 0
__pf_slen:                              # the length, at most the precision
        lbu   $t5, 0($t3)
        beqz  $t5, __pf_sgo
        bltz  $s5, __pf_sinc
        bge   $t1, $s5, __pf_sgo
__pf_sinc:
        addiu $t1, $t1, 1
        addiu $t3, $t3, 1
        j     __pf_slen
__pf_sgo:
        li    $t2, 0
        li    $s3, 32
        jal   __pf_out
        j     __pf_loop

__pf_f:                                 # fixed notation
        jal   __pf_getd
        bgez  $s5, __pf_f1
        li    $s5, 6
__pf_f1:
        la    $s6, __pf_buf+95
        jal   __pf_fixed
        move  $t0, $s6
        la    $t1, __pf_buf+95
        subu  $t1, $t1, $s6
        jal   __pf_out
        j     __pf_loop

__pf_e:                                 # d.dddddde+XX, $s5 digits after the point
        jal   __pf_getd
        bgez  $s5, __pf_e1
        li    $s5, 6
__pf_e1:
        move  $t3, $s5
        jal   __pf_norm                 # $f12 in [1, 10), exponent in $t7
        jal   __pf_expo                 # "e+03" at the end of the buffer, $s6 = its start
        jal   __pf_fixed                # the mantissa's digits right before it
        move  $t0, $s6
        la    $t1, __pf_buf+95
        subu  $t1, $t1, $s6
        jal   __pf_out
        j     __pf_loop

__pf_g:                                 # $s5 significant digits: %e style if the exponent
        jal   __pf_getd                 # is below -4 or not below $s5, else %f style;
        bgez  $s5, __pf_g1              # no trailing zeros either way
        li    $s5, 6
__pf_g1:
        bnez  $s5, __pf_g2
        li    $s5, 1
__pf_g2:
        mov.d $f2, $f12                 # the value, kept for the %f style
        addiu $t3, $s5, -1
        jal   __pf_norm                 # the exponent %e would print, in $t7
        li    $t5, -4
        blt   $t7, $t5, __pf_gexp
        bge   $t7, $s5, __pf_gexp
        subu  $s5, $s5, $t7             # %f style with P - 1 - X decimals
        addiu $s5, $s5, -1
        mov.d $f12, $f2
        la    $s6, __pf_buf+95
        sw    $s6, __pf_mend
        jal   __pf_fixed
        j     __pf_gstrip
__pf_gexp:
        addiu $s5, $s5, -1              # %e style with P - 1 decimals; $f12 is the mantissa
        jal   __pf_expo
        sw    $s6, __pf_mend
        jal   __pf_fixed
__pf_gstrip:                            # trailing zeros go, and then a lone point
        lw    $t5, __pf_mend
        beqz  $s5, __pf_gmove           # no decimals: nothing to strip
__pf_gzero:
        lbu   $t6, -1($t5)
        li    $t8, 48
        bne   $t6, $t8, __pf_gdot
        addiu $t5, $t5, -1
        j     __pf_gzero
__pf_gdot:
        li    $t8, 46
        bne   $t6, $t8, __pf_gmove
        addiu $t5, $t5, -1
__pf_gmove:                             # the exponent, if any, moves up behind the digits
        lw    $t6, __pf_mend
        la    $t8, __pf_buf+95
__pf_gcopy:
        beq   $t6, $t8, __pf_gout
        lbu   $a0, 0($t6)
        sb    $a0, 0($t5)
        addiu $t6, $t6, 1
        addiu $t5, $t5, 1
        j     __pf_gcopy
__pf_gout:
        move  $t0, $s6
        subu  $t1, $t5, $s6
        jal   __pf_out
        j     __pf_loop

__pf_getd:                              # the next argument, a double, into $f12 made
        addiu $s1, $s1, 7               # non-negative; its sign character in $t2
        li    $t5, -8
        and   $s1, $s1, $t5
        l.d   $f12, 0($s1)
        addiu $s1, $s1, 8
        li    $t2, 0
        l.d   $f14, __c_zero
        c.lt.d $f12, $f14
        bc1f  __pf_getd_done
        li    $t2, 45
        neg.d $f12, $f12
__pf_getd_done:
        jr    $ra

__pf_norm:                              # $f12 (>= 0) = m * 10^$t7 with 1 <= m < 10, m in $f12,
        li    $t7, 0                    # after rounding m to $t3 decimals (9.9999996 -> 1.0, X + 1)
        l.d   $f4, __c_zero
        c.eq.d $f12, $f4
        bc1t  __pf_norm_done            # 0 is 0.000000e+00
        l.d   $f6, __c_ten
        l.d   $f8, __c_one
__pf_norm_down:
        c.lt.d $f12, $f6
        bc1t  __pf_norm_up
        div.d $f12, $f12, $f6
        addiu $t7, $t7, 1
        j     __pf_norm_down
__pf_norm_up:
        c.lt.d $f12, $f8
        bc1f  __pf_norm_round
        mul.d $f12, $f12, $f6
        addiu $t7, $t7, -1
        j     __pf_norm_up
__pf_norm_round:                        # would rounding make it 10? then 1.0 and one more in the exponent
        l.d   $f4, __c_half
        move  $t5, $t3
__pf_norm_half:
        blez  $t5, __pf_norm_cmp
        div.d $f4, $f4, $f6
        addiu $t5, $t5, -1
        j     __pf_norm_half
__pf_norm_cmp:
        sub.d $f4, $f6, $f4
        c.lt.d $f12, $f4
        bc1t  __pf_norm_done
        div.d $f12, $f12, $f6
        addiu $t7, $t7, 1
__pf_norm_done:
        jr    $ra

__pf_expo:                              # "e+XX" ($t9 the letter, $t7 the exponent, at least two
        la    $s6, __pf_buf+95          # digits) at the end of the buffer; $s6 = its start
        move  $t5, $t7
        li    $t6, 43                   # '+'
        bgez  $t5, __pf_expo_digits
        li    $t6, 45                   # '-'
        negu  $t5, $t5
__pf_expo_digits:
        li    $t8, 0
        li    $a1, 10
__pf_expo_digit:
        divu  $t5, $a1
        mflo  $t5
        mfhi  $a0
        addiu $a0, $a0, 48
        addiu $s6, $s6, -1
        sb    $a0, 0($s6)
        addiu $t8, $t8, 1
        bnez  $t5, __pf_expo_digit
        slti  $a0, $t8, 2
        bnez  $a0, __pf_expo_digit
        addiu $s6, $s6, -1
        sb    $t6, 0($s6)
        addiu $s6, $s6, -1
        sb    $t9, 0($s6)
        jr    $ra

__pf_fixed:                             # the digits of $f12 (>= 0) with $s5 decimals, written to
        addiu $sp, $sp, -8              # end at $s6; returns their start in $s6. Keeps $t2.
        sw    $ra, 0($sp)
__pf_fscale:                            # N = the value * 10^precision, rounded to nearest (ties to even)
        l.d   $f18, __c_ten
        move  $t5, $s5
__pf_fscale1:
        blez  $t5, __pf_fscale2
        mul.d $f12, $f12, $f18
        addiu $t5, $t5, -1
        j     __pf_fscale1
__pf_fscale2:
        jal   __dtoll                   # $v1:$v0 = N truncated ($f12 is not negative, so it is kept)
        mtc1  $v1, $f14                 # back to double, to see what was cut off
        cvt.d.w $f14, $f14
        l.d   $f16, __c_2p32
        mul.d $f14, $f14, $f16
        mtc1  $v0, $f18
        cvt.d.w $f18, $f18
        bgez  $v0, __pf_fback
        add.d $f18, $f18, $f16
__pf_fback:
        add.d $f14, $f14, $f18
        sub.d $f12, $f12, $f14          # the fraction that was cut off
        l.d   $f16, __c_half
        c.lt.d $f16, $f12
        bc1t  __pf_fup
        c.eq.d $f16, $f12
        bc1f  __pf_fdigits
        andi  $t5, $v0, 1               # exactly half: round to the even neighbour
        beqz  $t5, __pf_fdigits
__pf_fup:
        addiu $v0, $v0, 1
        sltiu $t5, $v0, 1
        addu  $v1, $v1, $t5
__pf_fdigits:                           # digits of N, last first, with the point after `precision` of them
        move  $t0, $v0
        move  $t1, $v1
        li    $t3, 10
        li    $t4, 0                    # digits written
__pf_fdigit:
        bnez  $t1, __pf_fdiv64
        divu  $t0, $t3
        mflo  $t0
        mfhi  $t5
        j     __pf_fstore
__pf_fdiv64:
        move  $a0, $t0
        move  $a1, $t1
        move  $a2, $t3
        li    $a3, 0
        jal   __udivmodll
        move  $t0, $v0
        move  $t1, $v1
        move  $t5, $t8
__pf_fstore:
        addiu $t5, $t5, 48
        addiu $s6, $s6, -1
        sb    $t5, 0($s6)
        addiu $t4, $t4, 1
        bne   $t4, $s5, __pf_fmore
        li    $t5, 46                   # the decimal point
        addiu $s6, $s6, -1
        sb    $t5, 0($s6)
__pf_fmore:
        or    $t5, $t0, $t1
        bnez  $t5, __pf_fdigit
        ble   $t4, $s5, __pf_fdigit     # at least one digit before the point
        lw    $ra, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

__pf_out:                               # $t0 text, $t1 length, $t2 sign character or 0
        move  $t3, $t1
        beqz  $t2, __pf_opad
        addiu $t3, $t3, 1
__pf_opad:
        subu  $t4, $s4, $t3             # padding needed
        bnez  $s2, __pf_osign           # left-justified: pad afterwards
        li    $t5, 48
        beq   $s3, $t5, __pf_ozero
__pf_ospace:
        blez  $t4, __pf_osign
        li    $a0, 32
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
        addiu $t4, $t4, -1
        j     __pf_ospace
__pf_ozero:                             # sign, then zeros
        beqz  $t2, __pf_ozeros
        move  $a0, $t2
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
        li    $t2, 0
__pf_ozeros:
        blez  $t4, __pf_otext
        li    $a0, 48
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
        addiu $t4, $t4, -1
        j     __pf_ozeros
__pf_osign:
        beqz  $t2, __pf_otext
        move  $a0, $t2
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
__pf_otext:
        blez  $t1, __pf_otail
        lbu   $a0, 0($t0)
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
        addiu $t0, $t0, 1
        addiu $t1, $t1, -1
        j     __pf_otext
__pf_otail:
        beqz  $s2, __pf_oret
__pf_otail1:
        blez  $t4, __pf_oret
        li    $a0, 32
        li    $v0, 11
        syscall
        addiu $s7, $s7, 1
        addiu $t4, $t4, -1
        j     __pf_otail1
__pf_oret:
        jr    $ra

__pf_done:
        move  $v0, $s7
        lw    $s0, 0($sp)
        lw    $s1, 4($sp)
        lw    $s2, 8($sp)
        lw    $s3, 12($sp)
        lw    $s4, 16($sp)
        lw    $s5, 20($sp)
        lw    $s6, 24($sp)
        lw    $s7, 28($sp)
        lw    $ra, 36($sp)
        addiu $sp, $sp, 40
        jr    $ra

# ----------------------------------------------------------------- scanf
# %d %i %u %c %s %f (with l for double), a width for %s, h / hh / l / ll.
# Input is taken a line at a time with the read_string system call.
__sc_getc:                              # the next input character in $v0, -1 at the end
        lw    $v0, __sc_peek
        li    $t8, -2
        beq   $v0, $t8, __sc_read
        li    $t9, -1
        beq   $v0, $t9, __sc_ret        # the end of input stays the end
        sw    $t8, __sc_peek
__sc_ret:
        jr    $ra
__sc_read:                              # from the current line; a new line comes from the console
        lw    $t8, __sc_pos             # (read_string, so it works in the SPIM terminal and in QtSpim's console)
        lbu   $v0, 0($t8)
        bnez  $v0, __sc_take
        la    $t8, __sc_line
        sb    $zero, 0($t8)
        move  $a0, $t8
        li    $a1, 130
        li    $v0, 8                    # read_string
        syscall
        la    $t8, __sc_line
        lbu   $v0, 0($t8)
        beqz  $v0, __sc_eof             # nothing was read: the input has ended
__sc_take:
        addiu $t8, $t8, 1
        sw    $t8, __sc_pos
        jr    $ra
__sc_eof:
        li    $v0, -1
        sw    $v0, __sc_peek
        jr    $ra

__sc_skip:                              # skip white space; the next character stays unread
        move  $t7, $ra
__sc_skip1:
        jal   __sc_getc
        li    $t8, 32
        beq   $v0, $t8, __sc_skip1
        li    $t8, 10
        beq   $v0, $t8, __sc_skip1
        li    $t8, 9
        beq   $v0, $t8, __sc_skip1
        li    $t8, 13
        beq   $v0, $t8, __sc_skip1
        sw    $v0, __sc_peek
        jr    $t7

__scanf:
        addiu $sp, $sp, -40
        sw    $ra, 36($sp)
        sw    $s0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        sw    $s4, 16($sp)
        sw    $s5, 20($sp)
        sw    $s6, 24($sp)
        sw    $s7, 28($sp)
        lw    $s0, 40($sp)
        addiu $s1, $sp, 44
        li    $s7, 0                    # conversions stored
__sf_loop:
        lbu   $t0, 0($s0)
        beqz  $t0, __sf_done
        addiu $s0, $s0, 1
        li    $t1, 32
        beq   $t0, $t1, __sf_space
        li    $t1, 10
        beq   $t0, $t1, __sf_space
        li    $t1, 9
        beq   $t0, $t1, __sf_space
        li    $t1, 37
        beq   $t0, $t1, __sf_spec
        move  $s2, $t0                  # any other character must be the next input character
        jal   __sc_getc
        beq   $v0, $s2, __sf_loop
        sw    $v0, __sc_peek
        j     __sf_done
__sf_space:
        jal   __sc_skip
        j     __sf_loop
__sf_spec:
        li    $s4, 0                    # width
        li    $s5, 0                    # number of 'h'
        li    $s6, 0                    # number of 'l'
__sf_width:
        lbu   $t0, 0($s0)
        addiu $t1, $t0, -48
        sltiu $t2, $t1, 10
        beqz  $t2, __sf_len
        li    $t3, 10
        mul   $s4, $s4, $t3
        addu  $s4, $s4, $t1
        addiu $s0, $s0, 1
        j     __sf_width
__sf_len:
        lbu   $t0, 0($s0)
        li    $t1, 108
        bne   $t0, $t1, __sf_lenh
        addiu $s6, $s6, 1
        addiu $s0, $s0, 1
        j     __sf_len
__sf_lenh:
        li    $t1, 104
        bne   $t0, $t1, __sf_conv
        addiu $s5, $s5, 1
        addiu $s0, $s0, 1
        j     __sf_len
__sf_conv:
        lbu   $t0, 0($s0)
        beqz  $t0, __sf_done
        addiu $s0, $s0, 1
        li    $t1, 99
        beq   $t0, $t1, __sf_c
        li    $t1, 115
        beq   $t0, $t1, __sf_s
        li    $t1, 100
        beq   $t0, $t1, __sf_d
        li    $t1, 105
        beq   $t0, $t1, __sf_d
        li    $t1, 117
        beq   $t0, $t1, __sf_d
        li    $t1, 102
        beq   $t0, $t1, __sf_f
        li    $t1, 101
        beq   $t0, $t1, __sf_f
        li    $t1, 103
        beq   $t0, $t1, __sf_f
        j     __sf_done

__sf_d:                                 # an optional sign and decimal digits
        jal   __sc_skip
        jal   __sc_getc
        li    $s2, 0
        li    $t1, 45
        bne   $v0, $t1, __sf_dplus
        li    $s2, 1
        jal   __sc_getc
        j     __sf_dfirst
__sf_dplus:
        li    $t1, 43
        bne   $v0, $t1, __sf_dfirst
        jal   __sc_getc
__sf_dfirst:
        addiu $t1, $v0, -48
        sltiu $t2, $t1, 10
        bnez  $t2, __sf_dstart
        sw    $v0, __sc_peek
        j     __sf_done
__sf_dstart:
        li    $t4, 0
__sf_ddigit:
        li    $t3, 10
        mul   $t4, $t4, $t3
        addu  $t4, $t4, $t1
        jal   __sc_getc
        addiu $t1, $v0, -48
        sltiu $t2, $t1, 10
        bnez  $t2, __sf_ddigit
        sw    $v0, __sc_peek
        beqz  $s2, __sf_dstore
        negu  $t4, $t4
__sf_dstore:
        lw    $t5, 0($s1)
        addiu $s1, $s1, 4
        li    $t1, 2
        beq   $s6, $t1, __sf_dll
        beq   $s5, $t1, __sf_dhh
        bnez  $s5, __sf_dh
        sw    $t4, 0($t5)
        j     __sf_stored
__sf_dh:
        sh    $t4, 0($t5)
        j     __sf_stored
__sf_dhh:
        sb    $t4, 0($t5)
        j     __sf_stored
__sf_dll:
        sw    $t4, 0($t5)
        sra   $t4, $t4, 31
        sw    $t4, 4($t5)
__sf_stored:
        addiu $s7, $s7, 1
        j     __sf_loop

__sf_c:                                 # one character, white space included
        jal   __sc_getc
        bltz  $v0, __sf_done
        lw    $t5, 0($s1)
        addiu $s1, $s1, 4
        sb    $v0, 0($t5)
        j     __sf_stored

__sf_s:                                 # a word, at most `width` characters
        jal   __sc_skip
        jal   __sc_getc
        bltz  $v0, __sf_done
        lw    $t5, 0($s1)
        addiu $s1, $s1, 4
        li    $t4, 0
__sf_schar:
        sb    $v0, 0($t5)
        addiu $t5, $t5, 1
        addiu $t4, $t4, 1
        beqz  $s4, __sf_snext
        bge   $t4, $s4, __sf_send
__sf_snext:
        jal   __sc_getc
        bltz  $v0, __sf_sstop
        li    $t1, 32
        beq   $v0, $t1, __sf_sstop
        li    $t1, 10
        beq   $v0, $t1, __sf_sstop
        li    $t1, 9
        beq   $v0, $t1, __sf_sstop
        li    $t1, 13
        beq   $v0, $t1, __sf_sstop
        j     __sf_schar
__sf_sstop:
        sw    $v0, __sc_peek
__sf_send:
        sb    $zero, 0($t5)
        j     __sf_stored

__sf_f:                                 # [sign] digits [. digits] [e [sign] digits]
        jal   __sc_skip
        jal   __sc_getc
        li    $s2, 0
        li    $t1, 45
        bne   $v0, $t1, __sf_fplus
        li    $s2, 1
        jal   __sc_getc
        j     __sf_fstart
__sf_fplus:
        li    $t1, 43
        bne   $v0, $t1, __sf_fstart
        jal   __sc_getc
__sf_fstart:
        l.d   $f4, __c_zero             # the value, as an integer of all digits read
        l.d   $f8, __c_ten
        li    $t6, 0                    # digits seen
        li    $t7, 0                    # digits after the point
        li    $t5, 0                    # past the point?
__sf_fdigit:
        addiu $t1, $v0, -48
        sltiu $t2, $t1, 10
        beqz  $t2, __sf_fpoint
        mul.d $f4, $f4, $f8
        mtc1  $t1, $f6
        cvt.d.w $f6, $f6
        add.d $f4, $f4, $f6
        addiu $t6, $t6, 1
        addu  $t7, $t7, $t5
        jal   __sc_getc
        j     __sf_fdigit
__sf_fpoint:
        li    $t1, 46
        bne   $v0, $t1, __sf_fexp
        bnez  $t5, __sf_fexp
        li    $t5, 1
        jal   __sc_getc
        j     __sf_fdigit
__sf_fexp:
        bnez  $t6, __sf_fexp1
        sw    $v0, __sc_peek            # no digits at all
        j     __sf_done
__sf_fexp1:
        li    $t4, 0                    # exponent
        li    $t3, 0                    # exponent negative?
        li    $t1, 101
        beq   $v0, $t1, __sf_fexp2
        li    $t1, 69
        bne   $v0, $t1, __sf_fscale
__sf_fexp2:
        jal   __sc_getc
        li    $t1, 45
        bne   $v0, $t1, __sf_fexp3
        li    $t3, 1
        jal   __sc_getc
        j     __sf_fexp4
__sf_fexp3:
        li    $t1, 43
        bne   $v0, $t1, __sf_fexp4
        jal   __sc_getc
__sf_fexp4:
        addiu $t1, $v0, -48
        sltiu $t2, $t1, 10
        beqz  $t2, __sf_fexp5
        li    $t0, 10
        mul   $t4, $t4, $t0
        addu  $t4, $t4, $t1
        jal   __sc_getc
        j     __sf_fexp4
__sf_fexp5:
        beqz  $t3, __sf_fscale
        negu  $t4, $t4
__sf_fscale:
        sw    $v0, __sc_peek
        subu  $t4, $t4, $t7             # power of ten still to apply
__sf_fup:
        blez  $t4, __sf_fdown
        mul.d $f4, $f4, $f8
        addiu $t4, $t4, -1
        j     __sf_fup
__sf_fdown:
        bgez  $t4, __sf_fsign
        div.d $f4, $f4, $f8
        addiu $t4, $t4, 1
        j     __sf_fdown
__sf_fsign:
        beqz  $s2, __sf_fstore
        neg.d $f4, $f4
__sf_fstore:
        lw    $t5, 0($s1)
        addiu $s1, $s1, 4
        bnez  $s6, __sf_fdouble
        cvt.s.d $f4, $f4
        s.s   $f4, 0($t5)
        j     __sf_stored
__sf_fdouble:
        s.d   $f4, 0($t5)
        j     __sf_stored

__sf_done:
        move  $v0, $s7
        bnez  $s7, __sf_ret
        lw    $t0, __sc_peek            # nothing stored and the input is exhausted: EOF
        li    $t1, -1
        bne   $t0, $t1, __sf_ret
        li    $v0, -1
__sf_ret:
        lw    $s0, 0($sp)
        lw    $s1, 4($sp)
        lw    $s2, 8($sp)
        lw    $s3, 12($sp)
        lw    $s4, 16($sp)
        lw    $s5, 20($sp)
        lw    $s6, 24($sp)
        lw    $s7, 28($sp)
        lw    $ra, 36($sp)
        addiu $sp, $sp, 40
        jr    $ra
