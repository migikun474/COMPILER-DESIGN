# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t04_arrays.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g_squares:  .space 20
        .align 3
g_table:
        .byte 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0
        .byte 5, 0, 0, 0, 6, 0, 0, 0
str0:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str1:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str2:
        .byte 37, 100, 32, 37, 100, 10, 0
str3:
        .byte 119, 105, 100, 101, 32, 119, 111, 114, 108, 100, 0
str4:
        .byte 37, 115, 32, 37, 115, 32, 37, 115, 32, 37, 100, 32, 37, 100, 10, 0
str5:
        .byte 37, 46, 50, 102, 10, 0
str6:
        .byte 37, 100, 32, 37, 99, 32, 37, 99, 10, 0
str7:
        .byte 108, 105, 116, 101, 114, 97, 108, 0
        .align 3
fc0:  .word 0, 1073217536        # 1.5
        .align 3
fc1:  .word 0, 1074003968        # 2.5
        .align 3
fc2:  .word 0, 0        # 0
        .align 3
fc3:  .word 0, 1073741824        # 2

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

# total(int *, int)
_Z5totalPii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # s = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L0_2:
        # if i int< n goto 4
        lw    $t0, -8($fp)
        lw    $t1, 12($fp)
        blt   $t0, $t1, L0_4
        # goto 12
        j     L0_12
L0_4:
        # t1 = i int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = a ptr+ t1
        lw    $t0, 8($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t3 = *t2
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t4 = s int+ t3
        lw    $t0, -4($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # s = t4
        lw    $t0, -24($fp)
        sw    $t0, -4($fp)
        # t5 = i int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # i = t5
        lw    $t0, -28($fp)
        sw    $t0, -8($fp)
        # goto 2
        j     L0_2
L0_12:
        # return s
        lw    $v0, -4($fp)
        j     _Z5totalPii_exit
_Z5totalPii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# trace(int (*)[3], int)
_Z5tracePA3_ii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        # s = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L1_2:
        # if i int< n goto 4
        lw    $t0, -8($fp)
        lw    $t1, 12($fp)
        blt   $t0, $t1, L1_4
        # goto 14
        j     L1_14
L1_4:
        # t1 = i int* 12
        lw    $t0, -8($fp)
        li    $t1, 12
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = m ptr+ t1
        lw    $t0, 8($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t3 = i int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t4 = t2 ptr+ t3
        lw    $t0, -16($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t5 = *t4
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # t6 = s int+ t5
        lw    $t0, -4($fp)
        lw    $t1, -28($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # s = t6
        lw    $t0, -32($fp)
        sw    $t0, -4($fp)
        # t7 = i int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # i = t7
        lw    $t0, -36($fp)
        sw    $t0, -8($fp)
        # goto 2
        j     L1_2
L1_14:
        # return s
        lw    $v0, -4($fp)
        j     _Z5tracePA3_ii_exit
_Z5tracePA3_ii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# length(char *)
_Z6lengthPc:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # n = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L2_1:
        # t1 = s ptr+ n
        lw    $t0, 8($fp)
        lw    $t1, -4($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t2 = *t1
        lw    $t8, -8($fp)
        lb    $t0, 0($t8)
        sb    $t0, -9($fp)
        # if t2 char!= 0 goto 5
        lb    $t0, -9($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_5
        # goto 8
        j     L2_8
L2_5:
        # t3 = n int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # n = t3
        lw    $t0, -16($fp)
        sw    $t0, -4($fp)
        # goto 1
        j     L2_1
L2_8:
        # return n
        lw    $v0, -4($fp)
        j     _Z6lengthPc_exit
_Z6lengthPc_exit:
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
        addiu $sp, $sp, -600
        # a[0] = 1
        addiu $t8, $fp, -20
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # a[4] = 2
        addiu $t8, $fp, -20
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # a[8] = 3
        addiu $t8, $fp, -20
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # a[12] = 0
        addiu $t8, $fp, -20
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # a[16] = 0
        addiu $t8, $fp, -20
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # i = 0
        li    $t0, 0
        sw    $t0, -156($fp)
L3_6:
        # if i int< 5 goto 8
        lw    $t0, -156($fp)
        li    $t1, 5
        blt   $t0, $t1, L3_8
        # goto 14
        j     L3_14
L3_8:
        # t1 = i int* 4
        lw    $t0, -156($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -268($fp)
        # t2 = i int* i
        lw    $t0, -156($fp)
        lw    $t1, -156($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -272($fp)
        # squares[t1] = t2
        la    $t8, g_squares
        lw    $t9, -268($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -272($fp)
        sw    $t0, 0($t8)
        # t3 = i int+ 1
        lw    $t0, -156($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -276($fp)
        # i = t3
        lw    $t0, -276($fp)
        sw    $t0, -156($fp)
        # goto 6
        j     L3_6
L3_14:
        # i = 0
        li    $t0, 0
        sw    $t0, -156($fp)
L3_15:
        # if i int< 3 goto 17
        lw    $t0, -156($fp)
        li    $t1, 3
        blt   $t0, $t1, L3_17
        # goto 32
        j     L3_32
L3_17:
        # j = 0
        li    $t0, 0
        sw    $t0, -160($fp)
L3_18:
        # if j int< 3 goto 20
        lw    $t0, -160($fp)
        li    $t1, 3
        blt   $t0, $t1, L3_20
        # goto 29
        j     L3_29
L3_20:
        # t4 = i int* 3
        lw    $t0, -156($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -280($fp)
        # t5 = t4 int+ j
        lw    $t0, -280($fp)
        lw    $t1, -160($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -284($fp)
        # t6 = t5 int* 4
        lw    $t0, -284($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -288($fp)
        # t7 = i int* 3
        lw    $t0, -156($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -292($fp)
        # t8 = t7 int+ j
        lw    $t0, -292($fp)
        lw    $t1, -160($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -296($fp)
        # m[t6] = t8
        addiu $t8, $fp, -56
        lw    $t9, -288($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -296($fp)
        sw    $t0, 0($t8)
        # t9 = j int+ 1
        lw    $t0, -160($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -300($fp)
        # j = t9
        lw    $t0, -300($fp)
        sw    $t0, -160($fp)
        # goto 18
        j     L3_18
L3_29:
        # t10 = i int+ 1
        lw    $t0, -156($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -304($fp)
        # i = t10
        lw    $t0, -304($fp)
        sw    $t0, -156($fp)
        # goto 15
        j     L3_15
L3_32:
        # i = 0
        li    $t0, 0
        sw    $t0, -156($fp)
L3_33:
        # if i int< 2 goto 35
        lw    $t0, -156($fp)
        li    $t1, 2
        blt   $t0, $t1, L3_35
        # goto 60
        j     L3_60
L3_35:
        # j = 0
        li    $t0, 0
        sw    $t0, -160($fp)
L3_36:
        # if j int< 3 goto 38
        lw    $t0, -160($fp)
        li    $t1, 3
        blt   $t0, $t1, L3_38
        # goto 57
        j     L3_57
L3_38:
        # k = 0
        li    $t0, 0
        sw    $t0, -164($fp)
L3_39:
        # if k int< 4 goto 41
        lw    $t0, -164($fp)
        li    $t1, 4
        blt   $t0, $t1, L3_41
        # goto 54
        j     L3_54
L3_41:
        # t11 = i int* 3
        lw    $t0, -156($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -308($fp)
        # t12 = t11 int+ j
        lw    $t0, -308($fp)
        lw    $t1, -160($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -312($fp)
        # t13 = t12 int* 4
        lw    $t0, -312($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -316($fp)
        # t14 = t13 int+ k
        lw    $t0, -316($fp)
        lw    $t1, -164($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -320($fp)
        # t15 = t14 int* 4
        lw    $t0, -320($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -324($fp)
        # t16 = i int* 100
        lw    $t0, -156($fp)
        li    $t1, 100
        mul   $t0, $t0, $t1
        sw    $t0, -328($fp)
        # t17 = j int* 10
        lw    $t0, -160($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -332($fp)
        # t18 = t16 int+ t17
        lw    $t0, -328($fp)
        lw    $t1, -332($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -336($fp)
        # t19 = t18 int+ k
        lw    $t0, -336($fp)
        lw    $t1, -164($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -340($fp)
        # cube[t15] = t19
        addiu $t8, $fp, -152
        lw    $t9, -324($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -340($fp)
        sw    $t0, 0($t8)
        # t20 = k int+ 1
        lw    $t0, -164($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -344($fp)
        # k = t20
        lw    $t0, -344($fp)
        sw    $t0, -164($fp)
        # goto 39
        j     L3_39
L3_54:
        # t21 = j int+ 1
        lw    $t0, -160($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -348($fp)
        # j = t21
        lw    $t0, -348($fp)
        sw    $t0, -160($fp)
        # goto 36
        j     L3_36
L3_57:
        # t22 = i int+ 1
        lw    $t0, -156($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -352($fp)
        # i = t22
        lw    $t0, -352($fp)
        sw    $t0, -156($fp)
        # goto 33
        j     L3_33
L3_60:
        # t23 = a[0]
        addiu $t8, $fp, -20
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -356($fp)
        # t24 = a[8]
        addiu $t8, $fp, -20
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -360($fp)
        # t25 = a[12]
        addiu $t8, $fp, -20
        li    $t9, 12
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -364($fp)
        # t26 = a[16]
        addiu $t8, $fp, -20
        li    $t9, 16
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -368($fp)
        # t27 = &a
        addiu $t0, $fp, -20
        sw    $t0, -372($fp)
        # param t27
        # param 5
        # t28 = call total(int *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -372($fp)
        sw    $t0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _Z5totalPii
        addiu $sp, $sp, 8
        sw    $v0, -376($fp)
        # param "%d %d %d %d %d\n"
        # param t23
        # param t24
        # param t25
        # param t26
        # param t28
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -356($fp)
        sw    $t0, 4($sp)
        lw    $t0, -360($fp)
        sw    $t0, 8($sp)
        lw    $t0, -364($fp)
        sw    $t0, 12($sp)
        lw    $t0, -368($fp)
        sw    $t0, 16($sp)
        lw    $t0, -376($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t29 = squares[16]
        la    $t8, g_squares
        li    $t9, 16
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -380($fp)
        # t30 = &squares
        la    $t0, g_squares
        sw    $t0, -384($fp)
        # param t30
        # param 5
        # t31 = call total(int *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -384($fp)
        sw    $t0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _Z5totalPii
        addiu $sp, $sp, 8
        sw    $v0, -388($fp)
        # t32 = &m
        addiu $t0, $fp, -56
        sw    $t0, -392($fp)
        # param t32
        # param 3
        # t33 = call trace(int (*)[3], int), 2
        addiu $sp, $sp, -8
        lw    $t0, -392($fp)
        sw    $t0, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        jal   _Z5tracePA3_ii
        addiu $sp, $sp, 8
        sw    $v0, -396($fp)
        # param "%d %d %d\n"
        # param t29
        # param t31
        # param t33
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -380($fp)
        sw    $t0, 4($sp)
        lw    $t0, -388($fp)
        sw    $t0, 8($sp)
        lw    $t0, -396($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t34 = cube[92]
        addiu $t8, $fp, -152
        li    $t9, 92
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -400($fp)
        # t35 = cube[24]
        addiu $t8, $fp, -152
        li    $t9, 24
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -404($fp)
        # t36 = m[28]
        addiu $t8, $fp, -56
        li    $t9, 28
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -408($fp)
        # param "%d %d %d\n"
        # param t34
        # param t35
        # param t36
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -400($fp)
        sw    $t0, 4($sp)
        lw    $t0, -404($fp)
        sw    $t0, 8($sp)
        lw    $t0, -408($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t37 = table[20]
        la    $t8, g_table
        li    $t9, 20
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -412($fp)
        # t38 = table[4]
        la    $t8, g_table
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -416($fp)
        # t39 = table[12]
        la    $t8, g_table
        li    $t9, 12
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -420($fp)
        # t40 = t38 int+ t39
        lw    $t0, -416($fp)
        lw    $t1, -420($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -424($fp)
        # param "%d %d\n"
        # param t37
        # param t40
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -412($fp)
        sw    $t0, 4($sp)
        lw    $t0, -424($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # flat[0] = 1
        addiu $t8, $fp, -180
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # flat[4] = 2
        addiu $t8, $fp, -180
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # flat[8] = 3
        addiu $t8, $fp, -180
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # flat[12] = 4
        addiu $t8, $fp, -180
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 4
        sw    $t0, 0($t8)
        # sparse[0] = 0
        addiu $t8, $fp, -204
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # sparse[4] = 7
        addiu $t8, $fp, -204
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 7
        sw    $t0, 0($t8)
        # sparse[8] = 0
        addiu $t8, $fp, -204
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # sparse[12] = 0
        addiu $t8, $fp, -204
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # sparse[16] = 9
        addiu $t8, $fp, -204
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 9
        sw    $t0, 0($t8)
        # sparse[20] = 0
        addiu $t8, $fp, -204
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # sized[0] = 5
        addiu $t8, $fp, -220
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 5
        sw    $t0, 0($t8)
        # sized[4] = 6
        addiu $t8, $fp, -220
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 6
        sw    $t0, 0($t8)
        # sized[8] = 7
        addiu $t8, $fp, -220
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 7
        sw    $t0, 0($t8)
        # sized[12] = 8
        addiu $t8, $fp, -220
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 8
        sw    $t0, 0($t8)
        # t41 = flat[8]
        addiu $t8, $fp, -180
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -428($fp)
        # t42 = sparse[4]
        addiu $t8, $fp, -204
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -432($fp)
        # t43 = sparse[16]
        addiu $t8, $fp, -204
        li    $t9, 16
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -436($fp)
        # t44 = sparse[20]
        addiu $t8, $fp, -204
        li    $t9, 20
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -440($fp)
        # t45 = 16 uint/ 4
        li    $t0, 16
        li    $t1, 4
        divu  $t0, $t1
        mflo  $t0
        sw    $t0, -444($fp)
        # param "%d %d %d %d %d\n"
        # param t41
        # param t42
        # param t43
        # param t44
        # param t45
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -428($fp)
        sw    $t0, 4($sp)
        lw    $t0, -432($fp)
        sw    $t0, 8($sp)
        lw    $t0, -436($fp)
        sw    $t0, 12($sp)
        lw    $t0, -440($fp)
        sw    $t0, 16($sp)
        lw    $t0, -444($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # word[0] = 104
        addiu $t8, $fp, -226
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 104
        sb    $t0, 0($t8)
        # word[1] = 101
        addiu $t8, $fp, -226
        li    $t9, 1
        addu  $t8, $t8, $t9
        li    $t0, 101
        sb    $t0, 0($t8)
        # word[2] = 108
        addiu $t8, $fp, -226
        li    $t9, 2
        addu  $t8, $t8, $t9
        li    $t0, 108
        sb    $t0, 0($t8)
        # word[3] = 108
        addiu $t8, $fp, -226
        li    $t9, 3
        addu  $t8, $t8, $t9
        li    $t0, 108
        sb    $t0, 0($t8)
        # word[4] = 111
        addiu $t8, $fp, -226
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 111
        sb    $t0, 0($t8)
        # word[5] = 0
        addiu $t8, $fp, -226
        li    $t9, 5
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # buf[0] = 97
        addiu $t8, $fp, -234
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 97
        sb    $t0, 0($t8)
        # buf[1] = 98
        addiu $t8, $fp, -234
        li    $t9, 1
        addu  $t8, $t8, $t9
        li    $t0, 98
        sb    $t0, 0($t8)
        # buf[2] = 0
        addiu $t8, $fp, -234
        li    $t9, 2
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # buf[3] = 0
        addiu $t8, $fp, -234
        li    $t9, 3
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # buf[4] = 0
        addiu $t8, $fp, -234
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # buf[5] = 0
        addiu $t8, $fp, -234
        li    $t9, 5
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # buf[6] = 0
        addiu $t8, $fp, -234
        li    $t9, 6
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # buf[7] = 0
        addiu $t8, $fp, -234
        li    $t9, 7
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # lit = "wide world"
        la    $t0, str3
        sw    $t0, -240($fp)
        # word[0] = 106
        addiu $t8, $fp, -226
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 106
        sb    $t0, 0($t8)
        # buf[2] = 99
        addiu $t8, $fp, -234
        li    $t9, 2
        addu  $t8, $t8, $t9
        li    $t0, 99
        sb    $t0, 0($t8)
        # t46 = &word
        addiu $t0, $fp, -226
        sw    $t0, -448($fp)
        # t47 = &buf
        addiu $t0, $fp, -234
        sw    $t0, -452($fp)
        # t48 = &word
        addiu $t0, $fp, -226
        sw    $t0, -456($fp)
        # param t48
        # t49 = call length(char *), 1
        addiu $sp, $sp, -8
        lw    $t0, -456($fp)
        sw    $t0, 0($sp)
        jal   _Z6lengthPc
        addiu $sp, $sp, 8
        sw    $v0, -460($fp)
        # param lit
        # t50 = call length(char *), 1
        addiu $sp, $sp, -8
        lw    $t0, -240($fp)
        sw    $t0, 0($sp)
        jal   _Z6lengthPc
        addiu $sp, $sp, 8
        sw    $v0, -464($fp)
        # param "%s %s %s %d %d\n"
        # param t46
        # param t47
        # param lit
        # param t49
        # param t50
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -448($fp)
        sw    $t0, 4($sp)
        lw    $t0, -452($fp)
        sw    $t0, 8($sp)
        lw    $t0, -240($fp)
        sw    $t0, 12($sp)
        lw    $t0, -460($fp)
        sw    $t0, 16($sp)
        lw    $t0, -464($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # avg[0] = 1.5
        addiu $t8, $fp, -264
        li    $t9, 0
        addu  $t8, $t8, $t9
        l.d   $f0, fc0
        s.d   $f0, 0($t8)
        # avg[8] = 2.5
        addiu $t8, $fp, -264
        li    $t9, 8
        addu  $t8, $t8, $t9
        l.d   $f0, fc1
        s.d   $f0, 0($t8)
        # avg[16] = 0.0
        addiu $t8, $fp, -264
        li    $t9, 16
        addu  $t8, $t8, $t9
        l.d   $f0, fc2
        s.d   $f0, 0($t8)
        # t51 = avg[0]
        addiu $t8, $fp, -264
        li    $t9, 0
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -472($fp)
        # t52 = avg[8]
        addiu $t8, $fp, -264
        li    $t9, 8
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -480($fp)
        # t53 = t51 double+ t52
        l.d   $f0, -472($fp)
        l.d   $f2, -480($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -488($fp)
        # t54 = t53 double/ 2.0
        l.d   $f0, -488($fp)
        l.d   $f2, fc3
        div.d $f0, $f0, $f2
        s.d   $f0, -496($fp)
        # avg[16] = t54
        addiu $t8, $fp, -264
        li    $t9, 16
        addu  $t8, $t8, $t9
        l.d   $f0, -496($fp)
        s.d   $f0, 0($t8)
        # t55 = avg[16]
        addiu $t8, $fp, -264
        li    $t9, 16
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -504($fp)
        # param "%.2f\n"
        # param t55
        # call printf, 2
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        l.d   $f0, -504($fp)
        s.d   $f0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # i = 2
        li    $t0, 2
        sw    $t0, -156($fp)
        # t56 = i int* 4
        lw    $t0, -156($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -508($fp)
        # t57 = i int- 1
        lw    $t0, -156($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -512($fp)
        # t58 = t57 int* 4
        lw    $t0, -512($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -516($fp)
        # t59 = a[t58]
        addiu $t8, $fp, -20
        lw    $t9, -516($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -520($fp)
        # t60 = i int+ 1
        lw    $t0, -156($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -524($fp)
        # t61 = t60 int* 4
        lw    $t0, -524($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -528($fp)
        # t62 = a[t61]
        addiu $t8, $fp, -20
        lw    $t9, -528($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -532($fp)
        # t63 = t59 int+ t62
        lw    $t0, -520($fp)
        lw    $t1, -532($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -536($fp)
        # a[t56] = t63
        addiu $t8, $fp, -20
        lw    $t9, -508($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -536($fp)
        sw    $t0, 0($t8)
        # t64 = a[0]
        addiu $t8, $fp, -20
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -540($fp)
        # t65 = t64 int* 4
        lw    $t0, -540($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -544($fp)
        # t66 = a[t65]
        addiu $t8, $fp, -20
        lw    $t9, -544($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -548($fp)
        # t67 = t66 int+ 10
        lw    $t0, -548($fp)
        li    $t1, 10
        addu  $t0, $t0, $t1
        sw    $t0, -552($fp)
        # a[t65] = t67
        addiu $t8, $fp, -20
        lw    $t9, -544($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -552($fp)
        sw    $t0, 0($t8)
        # t68 = a[8]
        addiu $t8, $fp, -20
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -556($fp)
        # t69 = a[4]
        addiu $t8, $fp, -20
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -560($fp)
        # param "%d %d\n"
        # param t68
        # param t69
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -556($fp)
        sw    $t0, 4($sp)
        lw    $t0, -560($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t70 = &a
        addiu $t0, $fp, -20
        sw    $t0, -564($fp)
        # t71 = t70 ptr+ 4
        lw    $t0, -564($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -568($fp)
        # t72 = *t71
        lw    $t8, -568($fp)
        lw    $t0, 0($t8)
        sw    $t0, -572($fp)
        # t73 = "literal" ptr+ 2
        la    $t0, str7
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -576($fp)
        # t74 = *t73
        lw    $t8, -576($fp)
        lb    $t0, 0($t8)
        sb    $t0, -577($fp)
        # t75 = chartoint t74
        lb    $t0, -577($fp)
        sw    $t0, -584($fp)
        # t76 = &word
        addiu $t0, $fp, -226
        sw    $t0, -588($fp)
        # t77 = *t76
        lw    $t8, -588($fp)
        lb    $t0, 0($t8)
        sb    $t0, -589($fp)
        # t78 = chartoint t77
        lb    $t0, -589($fp)
        sw    $t0, -596($fp)
        # param "%d %c %c\n"
        # param t72
        # param t75
        # param t78
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -572($fp)
        sw    $t0, 4($sp)
        lw    $t0, -584($fp)
        sw    $t0, 8($sp)
        lw    $t0, -596($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t79 = m[16]
        addiu $t8, $fp, -56
        li    $t9, 16
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -600($fp)
        # return t79
        lw    $v0, -600($fp)
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
# %d %i %u %x %X %o %c %s %f %%, with '-' and '0' flags, width, precision
# (strings and %f), '*', and the lengths l / ll / h.
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
        addiu $s1, $s1, 7
        li    $t5, -8
        and   $s1, $s1, $t5
        l.d   $f12, 0($s1)
        addiu $s1, $s1, 8
        bgez  $s5, __pf_fsign
        li    $s5, 6
__pf_fsign:
        li    $t2, 0
        l.d   $f14, __c_zero
        c.lt.d $f12, $f14
        bc1f  __pf_fscale
        li    $t2, 45
        neg.d $f12, $f12
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
        la    $s6, __pf_buf+95
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
        move  $t0, $s6
        la    $t1, __pf_buf+95
        subu  $t1, $t1, $s6
        jal   __pf_out
        j     __pf_loop

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
