# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t26_declarations.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g_primes:
        .byte 2, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 7, 0, 0, 0
        .align 3
g_matrix:
        .byte 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0
        .byte 5, 0, 0, 0, 6, 0, 0, 0
        .align 3
g_letters:
        .byte 111, 107, 0
        .align 3
g_stock:
        .byte 115, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 64
        .byte 3, 0, 0, 0, 0, 0, 0, 0
        .align 3
g_table:
        .byte 0, 0, 0, 0, 0, 0, 248, 63, 0, 0, 0, 0, 0, 0, 0, 0
        .byte 0, 0, 0, 0, 0, 0, 35, 64
        .align 3
g_kept_17:
        .byte 3, 0, 0, 0
str0:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str1:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str2:
        .byte 37, 100, 32, 37, 46, 49, 102, 32, 37, 99, 32, 37, 46, 49, 102, 10
        .byte 0
str3:
        .byte 37, 99, 32, 37, 100, 32, 37, 99, 32, 37, 100, 32, 37, 46, 49, 102
        .byte 32, 37, 99, 32, 37, 100, 10, 0
str4:
        .byte 37, 115, 32, 37, 46, 49, 102, 32, 37, 46, 49, 102, 32, 37, 46, 49
        .byte 102, 32, 37, 100, 10, 0
str5:
        .byte 111, 110, 101, 0
str6:
        .byte 116, 119, 111, 0
str7:
        .byte 116, 104, 114, 101, 101, 0
str8:
        .byte 37, 100, 32, 37, 115, 32, 37, 99, 32, 37, 115, 32, 37, 100, 10, 0
        .align 3
fc0:  .word 0, 1073217536        # 1.5
        .align 3
fc1:  .word 0, 1074003968        # 2.5
        .align 3
fc2:  .word 0, 0        # 0
        .align 3
fc3:  .word 0, 1073741824        # 2
        .align 3
fc4:  .word 0, 1074528256        # 3.5

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

# sum(const int *)
_Z3sumPKi:
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
        # if i int< 4 goto 4
        lw    $t0, -8($fp)
        li    $t1, 4
        blt   $t0, $t1, L0_4
        # goto 12
        j     L0_12
L0_4:
        # t1 = i int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = r ptr+ t1
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
        j     _Z3sumPKi_exit
_Z3sumPKi_exit:
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
        addiu $sp, $sp, -584
        # t1 = 2 int* 2
        li    $t0, 2
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -272($fp)
        # if 3 int> 9 goto 3
        li    $t0, 3
        li    $t1, 9
        bgt   $t0, $t1, L1_3
        # goto 5
        j     L1_5
L1_3:
        # t2 = 3
        li    $t0, 3
        sw    $t0, -276($fp)
        # goto 6
        j     L1_6
L1_5:
        # t2 = 9
        li    $t0, 9
        sw    $t0, -276($fp)
L1_6:
        # r[0] = t1
        addiu $t8, $fp, -16
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, -272($fp)
        sw    $t0, 0($t8)
        # r[4] = t2
        addiu $t8, $fp, -16
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, -276($fp)
        sw    $t0, 0($t8)
        # r[8] = 2
        addiu $t8, $fp, -16
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # r[12] = 4
        addiu $t8, $fp, -16
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 4
        sw    $t0, 0($t8)
        # t3 = &r
        addiu $t0, $fp, -16
        sw    $t0, -280($fp)
        # param t3
        # t4 = call sum(const int *), 1
        addiu $sp, $sp, -8
        lw    $t0, -280($fp)
        sw    $t0, 0($sp)
        jal   _Z3sumPKi
        addiu $sp, $sp, 8
        sw    $v0, -284($fp)
        # t5 = &primes
        la    $t0, g_primes
        sw    $t0, -288($fp)
        # param t5
        # t6 = call sum(const int *), 1
        addiu $sp, $sp, -8
        lw    $t0, -288($fp)
        sw    $t0, 0($sp)
        jal   _Z3sumPKi
        addiu $sp, $sp, 8
        sw    $v0, -292($fp)
        # t7 = t4 int+ t6
        lw    $t0, -284($fp)
        lw    $t1, -292($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -296($fp)
        # n = t7
        lw    $t0, -296($fp)
        sw    $t0, -20($fp)
        # t8 = 1 int+ 2
        li    $t0, 1
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -300($fp)
        # t9 = 1 int+ 2
        li    $t0, 1
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -304($fp)
        # t10 = t8 int* t9
        lw    $t0, -300($fp)
        lw    $t1, -304($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -308($fp)
        # if n int> 100 goto 23
        lw    $t0, -20($fp)
        li    $t1, 100
        bgt   $t0, $t1, L1_23
        # goto 25
        j     L1_25
L1_23:
        # t11 = n
        lw    $t0, -20($fp)
        sw    $t0, -312($fp)
        # goto 26
        j     L1_26
L1_25:
        # t11 = 100
        li    $t0, 100
        sw    $t0, -312($fp)
L1_26:
        # param "%d %d %d\n"
        # param n
        # param t10
        # param t11
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -20($fp)
        sw    $t0, 4($sp)
        lw    $t0, -308($fp)
        sw    $t0, 8($sp)
        lw    $t0, -312($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param "%d %d %d %d\n"
        # param 24
        # param 80
        # param 32
        # param 16
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str1
        sw    $t0, 0($sp)
        li    $t0, 24
        sw    $t0, 4($sp)
        li    $t0, 80
        sw    $t0, 8($sp)
        li    $t0, 32
        sw    $t0, 12($sp)
        li    $t0, 16
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t12 = 24 uint/ 12
        li    $t0, 24
        li    $t1, 12
        divu  $t0, $t1
        mflo  $t0
        sw    $t0, -316($fp)
        # param "%d %d %d\n"
        # param 24
        # param t12
        # param 3
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 24
        sw    $t0, 4($sp)
        lw    $t0, -316($fp)
        sw    $t0, 8($sp)
        li    $t0, 3
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # box[0] = 97
        addiu $t8, $fp, -104
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 97
        sb    $t0, 0($t8)
        # box[8] = 1.5
        addiu $t8, $fp, -104
        li    $t9, 8
        addu  $t8, $t8, $t9
        l.d   $f0, fc0
        s.d   $f0, 0($t8)
        # box[16] = 2
        addiu $t8, $fp, -104
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 2
        sh    $t0, 0($t8)
        # box[24] = 98
        addiu $t8, $fp, -104
        li    $t9, 24
        addu  $t8, $t8, $t9
        li    $t0, 98
        sb    $t0, 0($t8)
        # box[32] = 2.5
        addiu $t8, $fp, -104
        li    $t9, 32
        addu  $t8, $t8, $t9
        l.d   $f0, fc1
        s.d   $f0, 0($t8)
        # box[40] = 4
        addiu $t8, $fp, -104
        li    $t9, 40
        addu  $t8, $t8, $t9
        li    $t0, 4
        sh    $t0, 0($t8)
        # box[48] = 99
        addiu $t8, $fp, -104
        li    $t9, 48
        addu  $t8, $t8, $t9
        li    $t0, 99
        sb    $t0, 0($t8)
        # box[56] = 0.0
        addiu $t8, $fp, -104
        li    $t9, 56
        addu  $t8, $t8, $t9
        l.d   $f0, fc2
        s.d   $f0, 0($t8)
        # box[64] = 8
        addiu $t8, $fp, -104
        li    $t9, 64
        addu  $t8, $t8, $t9
        li    $t0, 8
        sh    $t0, 0($t8)
        # box[72] = 0
        addiu $t8, $fp, -104
        li    $t9, 72
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # t13 = box[16]
        addiu $t8, $fp, -104
        li    $t9, 16
        addu  $t8, $t8, $t9
        lh    $t0, 0($t8)
        sh    $t0, -318($fp)
        # t14 = shorttoint t13
        lh    $t0, -318($fp)
        sw    $t0, -324($fp)
        # t15 = box[40]
        addiu $t8, $fp, -104
        li    $t9, 40
        addu  $t8, $t8, $t9
        lh    $t0, 0($t8)
        sh    $t0, -326($fp)
        # t16 = shorttoint t15
        lh    $t0, -326($fp)
        sw    $t0, -332($fp)
        # t17 = t14 int+ t16
        lw    $t0, -324($fp)
        lw    $t1, -332($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -336($fp)
        # t18 = box[64]
        addiu $t8, $fp, -104
        li    $t9, 64
        addu  $t8, $t8, $t9
        lh    $t0, 0($t8)
        sh    $t0, -338($fp)
        # t19 = shorttoint t18
        lh    $t0, -338($fp)
        sw    $t0, -344($fp)
        # t20 = t17 int+ t19
        lw    $t0, -336($fp)
        lw    $t1, -344($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -348($fp)
        # box[72] = t20
        addiu $t8, $fp, -104
        li    $t9, 72
        addu  $t8, $t8, $t9
        lw    $t0, -348($fp)
        sw    $t0, 0($t8)
        # t21 = &box
        addiu $t0, $fp, -104
        sw    $t0, -352($fp)
        # t22 = t21 ptr+ 48
        lw    $t0, -352($fp)
        li    $t1, 48
        addu  $t0, $t0, $t1
        sw    $t0, -356($fp)
        # it = t22
        lw    $t0, -356($fp)
        sw    $t0, -108($fp)
        # t23 = box[32]
        addiu $t8, $fp, -104
        li    $t9, 32
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -368($fp)
        # t24 = t23 double* 2.0
        l.d   $f0, -368($fp)
        l.d   $f2, fc3
        mul.d $f0, $f0, $f2
        s.d   $f0, -376($fp)
        # t25 = it ptr+ 8
        lw    $t0, -108($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -380($fp)
        # *t25 = t24
        lw    $t8, -380($fp)
        l.d   $f0, -376($fp)
        s.d   $f0, 0($t8)
        # t26 = box[72]
        addiu $t8, $fp, -104
        li    $t9, 72
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -384($fp)
        # t27 = it ptr+ 8
        lw    $t0, -108($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -388($fp)
        # t28 = *t27
        lw    $t8, -388($fp)
        l.d   $f0, 0($t8)
        s.d   $f0, -400($fp)
        # t29 = box[48]
        addiu $t8, $fp, -104
        li    $t9, 48
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -401($fp)
        # t30 = chartoint t29
        lb    $t0, -401($fp)
        sw    $t0, -408($fp)
        # t31 = stock[8]
        la    $t8, g_stock
        li    $t9, 8
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -416($fp)
        # t32 = stock[16]
        la    $t8, g_stock
        li    $t9, 16
        addu  $t8, $t8, $t9
        lh    $t0, 0($t8)
        sh    $t0, -418($fp)
        # t33 = shorttodouble t32
        lh    $t0, -418($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -432($fp)
        # t34 = t31 double* t33
        l.d   $f0, -416($fp)
        l.d   $f2, -432($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -440($fp)
        # param "%d %.1f %c %.1f\n"
        # param t26
        # param t28
        # param t30
        # param t34
        # call printf, 5
        addiu $sp, $sp, -32
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -384($fp)
        sw    $t0, 4($sp)
        l.d   $f0, -400($fp)
        s.d   $f0, 8($sp)
        lw    $t0, -408($fp)
        sw    $t0, 16($sp)
        l.d   $f0, -440($fp)
        s.d   $f0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # m[0] = 120
        addiu $t8, $fp, -144
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 120
        sb    $t0, 0($t8)
        # m[4] = 1
        addiu $t8, $fp, -144
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # m[8] = 121
        addiu $t8, $fp, -144
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 121
        sb    $t0, 0($t8)
        # m[10] = 2
        addiu $t8, $fp, -144
        li    $t9, 10
        addu  $t8, $t8, $t9
        li    $t0, 2
        sh    $t0, 0($t8)
        # m[16] = 3.5
        addiu $t8, $fp, -144
        li    $t9, 16
        addu  $t8, $t8, $t9
        l.d   $f0, fc4
        s.d   $f0, 0($t8)
        # m[24] = 122
        addiu $t8, $fp, -144
        li    $t9, 24
        addu  $t8, $t8, $t9
        li    $t0, 122
        sb    $t0, 0($t8)
        # copy = m
        addiu $a0, $fp, -176
        addiu $a1, $fp, -144
        li    $a2, 32
        jal   __memcpy
        # t35 = &copy
        addiu $t0, $fp, -176
        sw    $t0, -444($fp)
        # copy[4] = 100
        addiu $t8, $fp, -176
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 100
        sw    $t0, 0($t8)
        # t36 = m[0]
        addiu $t8, $fp, -144
        li    $t9, 0
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -445($fp)
        # t37 = chartoint t36
        lb    $t0, -445($fp)
        sw    $t0, -452($fp)
        # t38 = m[4]
        addiu $t8, $fp, -144
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -456($fp)
        # t39 = m[8]
        addiu $t8, $fp, -144
        li    $t9, 8
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -457($fp)
        # t40 = chartoint t39
        lb    $t0, -457($fp)
        sw    $t0, -464($fp)
        # t41 = m[10]
        addiu $t8, $fp, -144
        li    $t9, 10
        addu  $t8, $t8, $t9
        lh    $t0, 0($t8)
        sh    $t0, -466($fp)
        # t42 = shorttoint t41
        lh    $t0, -466($fp)
        sw    $t0, -472($fp)
        # t43 = m[16]
        addiu $t8, $fp, -144
        li    $t9, 16
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -480($fp)
        # t44 = m[24]
        addiu $t8, $fp, -144
        li    $t9, 24
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -481($fp)
        # t45 = chartoint t44
        lb    $t0, -481($fp)
        sw    $t0, -488($fp)
        # t46 = copy[4]
        addiu $t8, $fp, -176
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -492($fp)
        # param "%c %d %c %d %.1f %c %d\n"
        # param t37
        # param t38
        # param t40
        # param t42
        # param t43
        # param t45
        # param t46
        # call printf, 8
        addiu $sp, $sp, -40
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -452($fp)
        sw    $t0, 4($sp)
        lw    $t0, -456($fp)
        sw    $t0, 8($sp)
        lw    $t0, -464($fp)
        sw    $t0, 12($sp)
        lw    $t0, -472($fp)
        sw    $t0, 16($sp)
        l.d   $f0, -480($fp)
        s.d   $f0, 24($sp)
        lw    $t0, -488($fp)
        sw    $t0, 32($sp)
        lw    $t0, -492($fp)
        sw    $t0, 36($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # t47 = &letters
        la    $t0, g_letters
        sw    $t0, -496($fp)
        # t48 = table[0]
        la    $t8, g_table
        li    $t9, 0
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -504($fp)
        # t49 = table[8]
        la    $t8, g_table
        li    $t9, 8
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -512($fp)
        # t50 = table[16]
        la    $t8, g_table
        li    $t9, 16
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -520($fp)
        # t51 = matrix[20]
        la    $t8, g_matrix
        li    $t9, 20
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -524($fp)
        # t52 = matrix[0]
        la    $t8, g_matrix
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -528($fp)
        # t53 = t51 int- t52
        lw    $t0, -524($fp)
        lw    $t1, -528($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -532($fp)
        # param "%s %.1f %.1f %.1f %d\n"
        # param t47
        # param t48
        # param t49
        # param t50
        # param t53
        # call printf, 6
        addiu $sp, $sp, -40
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -496($fp)
        sw    $t0, 4($sp)
        l.d   $f0, -504($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -512($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -520($fp)
        s.d   $f0, 24($sp)
        lw    $t0, -532($fp)
        sw    $t0, 32($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # grid[0] = 1
        addiu $t8, $fp, -224
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # grid[4] = 0
        addiu $t8, $fp, -224
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[8] = 0
        addiu $t8, $fp, -224
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[12] = 0
        addiu $t8, $fp, -224
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[16] = 0
        addiu $t8, $fp, -224
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[20] = 2
        addiu $t8, $fp, -224
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # grid[24] = 0
        addiu $t8, $fp, -224
        li    $t9, 24
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[28] = 0
        addiu $t8, $fp, -224
        li    $t9, 28
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[32] = 0
        addiu $t8, $fp, -224
        li    $t9, 32
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[36] = 0
        addiu $t8, $fp, -224
        li    $t9, 36
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # grid[40] = 3
        addiu $t8, $fp, -224
        li    $t9, 40
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # grid[44] = 0
        addiu $t8, $fp, -224
        li    $t9, 44
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # trace = 0
        li    $t0, 0
        sw    $t0, -228($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -232($fp)
L1_141:
        # if i int< 3 goto 143
        lw    $t0, -232($fp)
        li    $t1, 3
        blt   $t0, $t1, L1_143
        # goto 152
        j     L1_152
L1_143:
        # t54 = i int* 4
        lw    $t0, -232($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -536($fp)
        # t55 = t54 int+ i
        lw    $t0, -536($fp)
        lw    $t1, -232($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -540($fp)
        # t56 = t55 int* 4
        lw    $t0, -540($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -544($fp)
        # t57 = grid[t56]
        addiu $t8, $fp, -224
        lw    $t9, -544($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -548($fp)
        # t58 = trace int+ t57
        lw    $t0, -228($fp)
        lw    $t1, -548($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -552($fp)
        # trace = t58
        lw    $t0, -552($fp)
        sw    $t0, -228($fp)
        # t59 = i int+ 1
        lw    $t0, -232($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -556($fp)
        # i = t59
        lw    $t0, -556($fp)
        sw    $t0, -232($fp)
        # goto 141
        j     L1_141
L1_152:
        # words[0] = "one"
        addiu $t8, $fp, -244
        li    $t9, 0
        addu  $t8, $t8, $t9
        la    $t0, str5
        sw    $t0, 0($t8)
        # words[4] = "two"
        addiu $t8, $fp, -244
        li    $t9, 4
        addu  $t8, $t8, $t9
        la    $t0, str6
        sw    $t0, 0($t8)
        # words[8] = "three"
        addiu $t8, $fp, -244
        li    $t9, 8
        addu  $t8, $t8, $t9
        la    $t0, str7
        sw    $t0, 0($t8)
        # rows[0] = 97
        addiu $t8, $fp, -256
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 97
        sb    $t0, 0($t8)
        # rows[1] = 98
        addiu $t8, $fp, -256
        li    $t9, 1
        addu  $t8, $t8, $t9
        li    $t0, 98
        sb    $t0, 0($t8)
        # rows[2] = 0
        addiu $t8, $fp, -256
        li    $t9, 2
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # rows[3] = 0
        addiu $t8, $fp, -256
        li    $t9, 3
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # rows[4] = 0
        addiu $t8, $fp, -256
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # rows[5] = 0
        addiu $t8, $fp, -256
        li    $t9, 5
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # rows[6] = 99
        addiu $t8, $fp, -256
        li    $t9, 6
        addu  $t8, $t8, $t9
        li    $t0, 99
        sb    $t0, 0($t8)
        # rows[7] = 100
        addiu $t8, $fp, -256
        li    $t9, 7
        addu  $t8, $t8, $t9
        li    $t0, 100
        sb    $t0, 0($t8)
        # rows[8] = 101
        addiu $t8, $fp, -256
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 101
        sb    $t0, 0($t8)
        # rows[9] = 0
        addiu $t8, $fp, -256
        li    $t9, 9
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # rows[10] = 0
        addiu $t8, $fp, -256
        li    $t9, 10
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # rows[11] = 0
        addiu $t8, $fp, -256
        li    $t9, 11
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # t60 = words[8]
        addiu $t8, $fp, -244
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -560($fp)
        # t61 = rows[8]
        addiu $t8, $fp, -256
        li    $t9, 8
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -561($fp)
        # t62 = chartoint t61
        lb    $t0, -561($fp)
        sw    $t0, -568($fp)
        # t63 = &rows
        addiu $t0, $fp, -256
        sw    $t0, -572($fp)
        # t64 = 12 uint/ 4
        li    $t0, 12
        li    $t1, 4
        divu  $t0, $t1
        mflo  $t0
        sw    $t0, -576($fp)
        # param "%d %s %c %s %d\n"
        # param trace
        # param t60
        # param t62
        # param t63
        # param t64
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str8
        sw    $t0, 0($sp)
        lw    $t0, -228($fp)
        sw    $t0, 4($sp)
        lw    $t0, -560($fp)
        sw    $t0, 8($sp)
        lw    $t0, -568($fp)
        sw    $t0, 12($sp)
        lw    $t0, -572($fp)
        sw    $t0, 16($sp)
        lw    $t0, -576($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # sensor = 5
        li    $t0, 5
        sw    $t0, -260($fp)
        # t65 = sensor int* 2
        lw    $t0, -260($fp)
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -580($fp)
        # fast = t65
        lw    $t0, -580($fp)
        sw    $t0, -264($fp)
        # t66 = fast int+ kept.17
        lw    $t0, -264($fp)
        lw    $t1, g_kept_17
        addu  $t0, $t0, $t1
        sw    $t0, -584($fp)
        # deduced = t66
        lw    $t0, -584($fp)
        sw    $t0, -268($fp)
        # return deduced
        lw    $v0, -268($fp)
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
