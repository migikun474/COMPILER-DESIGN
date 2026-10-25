# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t21_numeric.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 37, 46, 51, 102, 32, 37, 46, 51, 102, 32, 37, 46, 51, 102, 32, 37
        .byte 46, 52, 102, 10, 0
str1:
        .byte 37, 46, 53, 102, 32, 37, 46, 52, 102, 32, 37, 46, 50, 102, 10, 0
str2:
        .byte 37, 46, 51, 102, 32, 37, 46, 50, 102, 32, 37, 46, 50, 102, 10, 0
str3:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str4:
        .byte 37, 46, 49, 102, 32, 37, 46, 49, 102, 32, 37, 100, 10, 0
str5:
        .byte 37, 46, 52, 102, 10, 0
str6:
        .byte 37, 46, 52, 102, 32, 37, 46, 50, 102, 10, 0
str7:
        .byte 37, 46, 54, 102, 32, 37, 46, 49, 102, 32, 37, 46, 51, 102, 10, 0
        .align 3
fc0:  .word 0, 0        # 0
        .align 3
fc1:  .word 0, 1073741824        # 2
        .align 3
fc2:  .word 0, 1072693248        # 1
        .align 3
fc3:  .word 0, 1074790400        # 4
        .align 3
fc4:  .word 1077936128        # 3
        .align 3
fc5:  .word 0, 1071644672        # 0.5
        .align 3
fc6:  .word 0, 1074266112        # 3
        .align 3
fc7:  .word 0, 1075576832        # 7
        .align 3
fc8:  .word 0, 1076101120        # 10
        .align 3
fc9:  .word 1065353216        # 1
        .align 3
fc10:  .word 0, 1073217536        # 1.5
        .align 3
fc11:  .word 1069547520        # 1.5
        .align 3
fc12:  .word 1075838976        # 2.5
        .align 3
fc13:  .word 1082130432        # 4
        .align 3
fc14:  .word 0, 1074397184        # 3.25
        .align 3
fc15:  .word 0, 1074003968        # 2.5
        .align 3
fc16:  .word 858993459, 1073951539        # 2.4
        .align 3
fc17:  .word 2576980378, 1069128089        # 0.1
        .align 3
fc18:  .word 2576980378, 1070176665        # 0.2
        .align 3
fc19:  .word 858993459, 1070805811        # 0.3
        .align 3
fc20:  .word 0, 1070596096        # 0.25
        .align 3
fc21:  .word 0, 1072168960        # 0.75
        .align 3
fc22:  .word 1051595899        # 0.34
        .align 3
fc23:  .word 0, 1106247680        # 4.29497e+09
        .align 3
fc24:  .word 1266679808        # 1.67772e+07
        .align 3
fc25:  .word 0        # 0
        .align 3
fc26:  .word 1073741824        # 2
        .align 3
fc27:  .word 3539053052, 1062232653        # 0.001
        .align 3
fc28:  .word 0, 1094914768        # 2.5e+06
        .align 3
fc29:  .word 0, 1079263232        # 81

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

# absolute(double)
_Z8absoluted:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if v double< 0.0 goto 2
        l.d   $f0, 8($fp)
        l.d   $f2, fc0
        c.lt.d $f0, $f2
        bc1t  L0_2
        # goto 5
        j     L0_5
L0_2:
        # t2 = double- v
        l.d   $f0, 8($fp)
        neg.d $f0, $f0
        s.d   $f0, -16($fp)
        # t1 = t2
        l.d   $f0, -16($fp)
        s.d   $f0, -8($fp)
        # goto 6
        j     L0_6
L0_5:
        # t1 = v
        l.d   $f0, 8($fp)
        s.d   $f0, -8($fp)
L0_6:
        # return t1
        l.d   $f0, -8($fp)
        j     _Z8absoluted_exit
_Z8absoluted_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# root(double)
_Z4rootd:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        # t1 = v double/ 2.0
        l.d   $f0, 8($fp)
        l.d   $f2, fc1
        div.d $f0, $f0, $f2
        s.d   $f0, -24($fp)
        # guess = t1
        l.d   $f0, -24($fp)
        s.d   $f0, -8($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -12($fp)
L1_3:
        # if i int< 20 goto 5
        lw    $t0, -12($fp)
        li    $t1, 20
        blt   $t0, $t1, L1_5
        # goto 12
        j     L1_12
L1_5:
        # t2 = v double/ guess
        l.d   $f0, 8($fp)
        l.d   $f2, -8($fp)
        div.d $f0, $f0, $f2
        s.d   $f0, -32($fp)
        # t3 = guess double+ t2
        l.d   $f0, -8($fp)
        l.d   $f2, -32($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -40($fp)
        # t4 = t3 double/ 2.0
        l.d   $f0, -40($fp)
        l.d   $f2, fc1
        div.d $f0, $f0, $f2
        s.d   $f0, -48($fp)
        # guess = t4
        l.d   $f0, -48($fp)
        s.d   $f0, -8($fp)
        # t5 = i int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -52($fp)
        # i = t5
        lw    $t0, -52($fp)
        sw    $t0, -12($fp)
        # goto 3
        j     L1_3
L1_12:
        # return guess
        l.d   $f0, -8($fp)
        j     _Z4rootd_exit
_Z4rootd_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# series(int)
_Z6seriesi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -80
        # sum = 0.0
        l.d   $f0, fc0
        s.d   $f0, -8($fp)
        # sign = 1.0
        l.d   $f0, fc2
        s.d   $f0, -16($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -20($fp)
L2_3:
        # if i int< terms goto 5
        lw    $t0, -20($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L2_5
        # goto 16
        j     L2_16
L2_5:
        # t1 = 2 int* i
        li    $t0, 2
        lw    $t1, -20($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t2 = t1 int+ 1
        lw    $t0, -24($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # t3 = inttodouble t2
        lw    $t0, -28($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -40($fp)
        # t4 = sign double/ t3
        l.d   $f0, -16($fp)
        l.d   $f2, -40($fp)
        div.d $f0, $f0, $f2
        s.d   $f0, -48($fp)
        # t5 = sum double+ t4
        l.d   $f0, -8($fp)
        l.d   $f2, -48($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -56($fp)
        # sum = t5
        l.d   $f0, -56($fp)
        s.d   $f0, -8($fp)
        # t6 = double- sign
        l.d   $f0, -16($fp)
        neg.d $f0, $f0
        s.d   $f0, -64($fp)
        # sign = t6
        l.d   $f0, -64($fp)
        s.d   $f0, -16($fp)
        # t7 = i int+ 1
        lw    $t0, -20($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -68($fp)
        # i = t7
        lw    $t0, -68($fp)
        sw    $t0, -20($fp)
        # goto 3
        j     L2_3
L2_16:
        # t8 = 4.0 double* sum
        l.d   $f0, fc3
        l.d   $f2, -8($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -80($fp)
        # return t8
        l.d   $f0, -80($fp)
        j     _Z6seriesi_exit
_Z6seriesi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# power(double, int)
_Z5powerdi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # r = 1.0
        l.d   $f0, fc2
        s.d   $f0, -8($fp)
L3_1:
        # t1 = n
        lw    $t0, 16($fp)
        sw    $t0, -12($fp)
        # t2 = n int- 1
        lw    $t0, 16($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # n = t2
        lw    $t0, -16($fp)
        sw    $t0, 16($fp)
        # if t1 int> 0 goto 6
        lw    $t0, -12($fp)
        li    $t1, 0
        bgt   $t0, $t1, L3_6
        # goto 9
        j     L3_9
L3_6:
        # t3 = r double* base
        l.d   $f0, -8($fp)
        l.d   $f2, 8($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -24($fp)
        # r = t3
        l.d   $f0, -24($fp)
        s.d   $f0, -8($fp)
        # goto 1
        j     L3_1
L3_9:
        # return r
        l.d   $f0, -8($fp)
        j     _Z5powerdi_exit
_Z5powerdi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# average(float, float, float)
_Z7averagefff:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = a float+ b
        l.s   $f0, 8($fp)
        l.s   $f2, 12($fp)
        add.s $f0, $f0, $f2
        s.s   $f0, -4($fp)
        # t2 = t1 float+ c
        l.s   $f0, -4($fp)
        l.s   $f2, 16($fp)
        add.s $f0, $f0, $f2
        s.s   $f0, -8($fp)
        # t3 = t2 float/ 3.0
        l.s   $f0, -8($fp)
        l.s   $f2, fc4
        div.s $f0, $f0, $f2
        s.s   $f0, -12($fp)
        # return t3
        l.s   $f0, -12($fp)
        j     _Z7averagefff_exit
_Z7averagefff_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# roundToInt(double)
_Z10roundToIntd:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # if v double< 0.0 goto 2
        l.d   $f0, 8($fp)
        l.d   $f2, fc0
        c.lt.d $f0, $f2
        bc1t  L5_2
        # goto 5
        j     L5_5
L5_2:
        # t2 = v double- 0.5
        l.d   $f0, 8($fp)
        l.d   $f2, fc5
        sub.d $f0, $f0, $f2
        s.d   $f0, -16($fp)
        # t1 = t2
        l.d   $f0, -16($fp)
        s.d   $f0, -8($fp)
        # goto 7
        j     L5_7
L5_5:
        # t3 = v double+ 0.5
        l.d   $f0, 8($fp)
        l.d   $f2, fc5
        add.d $f0, $f0, $f2
        s.d   $f0, -24($fp)
        # t1 = t3
        l.d   $f0, -24($fp)
        s.d   $f0, -8($fp)
L5_7:
        # t4 = doubletoint t1
        l.d   $f0, -8($fp)
        trunc.w.d $f0, $f0
        mfc1  $t0, $f0
        sw    $t0, -28($fp)
        # return t4
        lw    $v0, -28($fp)
        j     _Z10roundToIntd_exit
_Z10roundToIntd_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# poly(double)
_Z4polyd:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        # t1 = 2.0 double* x
        l.d   $f0, fc1
        l.d   $f2, 8($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -8($fp)
        # t2 = t1 double- 3.0
        l.d   $f0, -8($fp)
        l.d   $f2, fc6
        sub.d $f0, $f0, $f2
        s.d   $f0, -16($fp)
        # t3 = t2 double* x
        l.d   $f0, -16($fp)
        l.d   $f2, 8($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -24($fp)
        # t4 = t3 double+ 0.5
        l.d   $f0, -24($fp)
        l.d   $f2, fc5
        add.d $f0, $f0, $f2
        s.d   $f0, -32($fp)
        # t5 = t4 double* x
        l.d   $f0, -32($fp)
        l.d   $f2, 8($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -40($fp)
        # t6 = t5 double- 7.0
        l.d   $f0, -40($fp)
        l.d   $f2, fc7
        sub.d $f0, $f0, $f2
        s.d   $f0, -48($fp)
        # return t6
        l.d   $f0, -48($fp)
        j     _Z4polyd_exit
_Z4polyd_exit:
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
        addiu $sp, $sp, -440
        # t1 = 1e+01 double/ 4.0
        l.d   $f0, fc8
        l.d   $f2, fc3
        div.d $f0, $f0, $f2
        s.d   $f0, -104($fp)
        # d = t1
        l.d   $f0, -104($fp)
        s.d   $f0, -8($fp)
        # t2 = 7 int/ 2
        li    $t0, 7
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -108($fp)
        # t3 = inttodouble t2
        lw    $t0, -108($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -120($fp)
        # e = t3
        l.d   $f0, -120($fp)
        s.d   $f0, -16($fp)
        # t4 = 7.0 double/ 2.0
        l.d   $f0, fc7
        l.d   $f2, fc1
        div.d $f0, $f0, $f2
        s.d   $f0, -128($fp)
        # f = t4
        l.d   $f0, -128($fp)
        s.d   $f0, -24($fp)
        # t5 = 1.0 float/ 3.0
        l.s   $f0, fc9
        l.s   $f2, fc4
        div.s $f0, $f0, $f2
        s.s   $f0, -132($fp)
        # g = t5
        l.s   $f0, -132($fp)
        s.s   $f0, -28($fp)
        # t6 = floattodouble g
        l.s   $f0, -28($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -144($fp)
        # param "%.3f %.3f %.3f %.4f\n"
        # param d
        # param e
        # param f
        # param t6
        # call printf, 5
        addiu $sp, $sp, -40
        la    $t0, str0
        sw    $t0, 0($sp)
        l.d   $f0, -8($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -16($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -24($fp)
        s.d   $f0, 24($sp)
        l.d   $f0, -144($fp)
        s.d   $f0, 32($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # param 2.0
        # t7 = call root(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, fc1
        s.d   $f0, 0($sp)
        jal   _Z4rootd
        addiu $sp, $sp, 8
        s.d   $f0, -152($fp)
        # param 1000
        # t8 = call series(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1000
        sw    $t0, 0($sp)
        jal   _Z6seriesi
        addiu $sp, $sp, 8
        s.d   $f0, -160($fp)
        # param 1.5
        # param 6
        # t9 = call power(double, int), 2
        addiu $sp, $sp, -16
        l.d   $f0, fc10
        s.d   $f0, 0($sp)
        li    $t0, 6
        sw    $t0, 8($sp)
        jal   _Z5powerdi
        addiu $sp, $sp, 16
        s.d   $f0, -168($fp)
        # param "%.5f %.4f %.2f\n"
        # param t7
        # param t8
        # param t9
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str1
        sw    $t0, 0($sp)
        l.d   $f0, -152($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -160($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -168($fp)
        s.d   $f0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 1.5
        # param 2.5
        # param 4.0
        # t10 = call average(float, float, float), 3
        addiu $sp, $sp, -16
        l.s   $f0, fc11
        s.s   $f0, 0($sp)
        l.s   $f0, fc12
        s.s   $f0, 4($sp)
        l.s   $f0, fc13
        s.s   $f0, 8($sp)
        jal   _Z7averagefff
        addiu $sp, $sp, 16
        s.s   $f0, -172($fp)
        # t11 = floattodouble t10
        l.s   $f0, -172($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -184($fp)
        # t12 = double- 3.25
        l.d   $f0, fc14
        neg.d $f0, $f0
        s.d   $f0, -192($fp)
        # param t12
        # t13 = call absolute(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, -192($fp)
        s.d   $f0, 0($sp)
        jal   _Z8absoluted
        addiu $sp, $sp, 8
        s.d   $f0, -200($fp)
        # param 2.0
        # t14 = call poly(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, fc1
        s.d   $f0, 0($sp)
        jal   _Z4polyd
        addiu $sp, $sp, 8
        s.d   $f0, -208($fp)
        # param "%.3f %.2f %.2f\n"
        # param t11
        # param t13
        # param t14
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str2
        sw    $t0, 0($sp)
        l.d   $f0, -184($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -200($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -208($fp)
        s.d   $f0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 2.5
        # t15 = call roundToInt(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, fc15
        s.d   $f0, 0($sp)
        jal   _Z10roundToIntd
        addiu $sp, $sp, 8
        sw    $v0, -212($fp)
        # t16 = double- 2.5
        l.d   $f0, fc15
        neg.d $f0, $f0
        s.d   $f0, -224($fp)
        # param t16
        # t17 = call roundToInt(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, -224($fp)
        s.d   $f0, 0($sp)
        jal   _Z10roundToIntd
        addiu $sp, $sp, 8
        sw    $v0, -228($fp)
        # param 2.4
        # t18 = call roundToInt(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, fc16
        s.d   $f0, 0($sp)
        jal   _Z10roundToIntd
        addiu $sp, $sp, 8
        sw    $v0, -232($fp)
        # param "%d %d %d %d\n"
        # param t15
        # param t17
        # param t18
        # param 9
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -212($fp)
        sw    $t0, 4($sp)
        lw    $t0, -228($fp)
        sw    $t0, 8($sp)
        lw    $t0, -232($fp)
        sw    $t0, 12($sp)
        li    $t0, 9
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t20 = 0.1 double+ 0.2
        l.d   $f0, fc17
        l.d   $f2, fc18
        add.d $f0, $f0, $f2
        s.d   $f0, -248($fp)
        # if t20 double== 0.3 goto 60
        l.d   $f0, -248($fp)
        l.d   $f2, fc19
        c.eq.d $f0, $f2
        bc1t  L7_60
        # t19 = 0
        li    $t0, 0
        sw    $t0, -236($fp)
        # goto 61
        j     L7_61
L7_60:
        # t19 = 1
        li    $t0, 1
        sw    $t0, -236($fp)
L7_61:
        # t22 = 0.5 double+ 0.25
        l.d   $f0, fc5
        l.d   $f2, fc20
        add.d $f0, $f0, $f2
        s.d   $f0, -264($fp)
        # if t22 double== 0.75 goto 65
        l.d   $f0, -264($fp)
        l.d   $f2, fc21
        c.eq.d $f0, $f2
        bc1t  L7_65
        # t21 = 0
        li    $t0, 0
        sw    $t0, -252($fp)
        # goto 66
        j     L7_66
L7_65:
        # t21 = 1
        li    $t0, 1
        sw    $t0, -252($fp)
L7_66:
        # if d double> e goto 69
        l.d   $f0, -8($fp)
        l.d   $f2, -16($fp)
        c.lt.d $f2, $f0
        bc1t  L7_69
        # t23 = 0
        li    $t0, 0
        sw    $t0, -268($fp)
        # goto 70
        j     L7_70
L7_69:
        # t23 = 1
        li    $t0, 1
        sw    $t0, -268($fp)
L7_70:
        # if g float< 0.3400000035762787 goto 73
        l.s   $f0, -28($fp)
        l.s   $f2, fc22
        c.lt.s $f0, $f2
        bc1t  L7_73
        # t24 = 0
        li    $t0, 0
        sw    $t0, -272($fp)
        # goto 74
        j     L7_74
L7_73:
        # t24 = 1
        li    $t0, 1
        sw    $t0, -272($fp)
L7_74:
        # param "%d %d %d %d\n"
        # param t19
        # param t21
        # param t23
        # param t24
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -236($fp)
        sw    $t0, 4($sp)
        lw    $t0, -252($fp)
        sw    $t0, 8($sp)
        lw    $t0, -268($fp)
        sw    $t0, 12($sp)
        lw    $t0, -272($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # i = 7
        li    $t0, 7
        sw    $t0, -32($fp)
        # u = 4000000000
        li    $t0, -294967296
        sw    $t0, -36($fp)
        # c = 65
        li    $t0, 65
        sb    $t0, -37($fp)
        # t25 = i int/ 2
        lw    $t0, -32($fp)
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -276($fp)
        # t26 = inttodouble t25
        lw    $t0, -276($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -288($fp)
        # t27 = inttodouble i
        lw    $t0, -32($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -296($fp)
        # t28 = t27 double/ 2.0
        l.d   $f0, -296($fp)
        l.d   $f2, fc1
        div.d $f0, $f0, $f2
        s.d   $f0, -304($fp)
        # t29 = t26 double+ t28
        l.d   $f0, -288($fp)
        l.d   $f2, -304($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -312($fp)
        # t30 = chartodouble c
        lb    $t0, -37($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -320($fp)
        # t31 = t29 double+ t30
        l.d   $f0, -312($fp)
        l.d   $f2, -320($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -328($fp)
        # t32 = uinttodouble u
        lw    $t0, -36($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        bgez  $t0, M7_0
        l.d   $f2, fc23
        add.d $f0, $f0, $f2
M7_0:
        s.d   $f0, -336($fp)
        # t33 = t31 double+ t32
        l.d   $f0, -328($fp)
        l.d   $f2, -336($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -344($fp)
        # mixed = t33
        l.d   $f0, -344($fp)
        s.d   $f0, -48($fp)
        # narrowed = 16777216.0
        l.s   $f0, fc24
        s.s   $f0, -52($fp)
        # t34 = floattodouble narrowed
        l.s   $f0, -52($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -352($fp)
        # param "%.1f %.1f %d\n"
        # param mixed
        # param t34
        # param 0
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str4
        sw    $t0, 0($sp)
        l.d   $f0, -48($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -352($fp)
        s.d   $f0, 16($sp)
        li    $t0, 0
        sw    $t0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # total = 0.0
        l.d   $f0, fc0
        s.d   $f0, -64($fp)
        # step = 0.25
        l.d   $f0, fc20
        s.d   $f0, -72($fp)
L7_102:
        # if step double< 2.0 goto 104
        l.d   $f0, -72($fp)
        l.d   $f2, fc1
        c.lt.d $f0, $f2
        bc1t  L7_104
        # goto 110
        j     L7_110
L7_104:
        # t35 = step double* step
        l.d   $f0, -72($fp)
        l.d   $f2, -72($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -360($fp)
        # t36 = total double+ t35
        l.d   $f0, -64($fp)
        l.d   $f2, -360($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -368($fp)
        # total = t36
        l.d   $f0, -368($fp)
        s.d   $f0, -64($fp)
        # t37 = step double+ 0.25
        l.d   $f0, -72($fp)
        l.d   $f2, fc20
        add.d $f0, $f0, $f2
        s.d   $f0, -376($fp)
        # step = t37
        l.d   $f0, -376($fp)
        s.d   $f0, -72($fp)
        # goto 102
        j     L7_102
L7_110:
        # param "%.4f\n"
        # param total
        # call printf, 2
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        l.d   $f0, -64($fp)
        s.d   $f0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # fsum = 0.0
        l.s   $f0, fc25
        s.s   $f0, -76($fp)
        # k = 1
        li    $t0, 1
        sw    $t0, -80($fp)
L7_115:
        # if k int<= 10 goto 117
        lw    $t0, -80($fp)
        li    $t1, 10
        ble   $t0, $t1, L7_117
        # goto 124
        j     L7_124
L7_117:
        # t38 = inttofloat k
        lw    $t0, -80($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        cvt.s.d $f0, $f0
        s.s   $f0, -380($fp)
        # t39 = 1.0 float/ t38
        l.s   $f0, fc9
        l.s   $f2, -380($fp)
        div.s $f0, $f0, $f2
        s.s   $f0, -384($fp)
        # t40 = fsum float+ t39
        l.s   $f0, -76($fp)
        l.s   $f2, -384($fp)
        add.s $f0, $f0, $f2
        s.s   $f0, -388($fp)
        # fsum = t40
        l.s   $f0, -388($fp)
        s.s   $f0, -76($fp)
        # t41 = k int+ 1
        lw    $t0, -80($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -392($fp)
        # k = t41
        lw    $t0, -392($fp)
        sw    $t0, -80($fp)
        # goto 115
        j     L7_115
L7_124:
        # t42 = floattodouble fsum
        l.s   $f0, -76($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -400($fp)
        # t43 = float- fsum
        l.s   $f0, -76($fp)
        neg.s $f0, $f0
        s.s   $f0, -404($fp)
        # t44 = t43 float* 2.0
        l.s   $f0, -404($fp)
        l.s   $f2, fc26
        mul.s $f0, $f0, $f2
        s.s   $f0, -408($fp)
        # t45 = floattodouble t44
        l.s   $f0, -408($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -416($fp)
        # param "%.4f %.2f\n"
        # param t42
        # param t45
        # call printf, 3
        addiu $sp, $sp, -24
        la    $t0, str6
        sw    $t0, 0($sp)
        l.d   $f0, -400($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -416($fp)
        s.d   $f0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # tiny = 0.001
        l.d   $f0, fc27
        s.d   $f0, -88($fp)
        # huge = 2.5e+06
        l.d   $f0, fc28
        s.d   $f0, -96($fp)
        # t46 = huge double* tiny
        l.d   $f0, -96($fp)
        l.d   $f2, -88($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -424($fp)
        # param "%.6f %.1f %.3f\n"
        # param tiny
        # param huge
        # param t46
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str7
        sw    $t0, 0($sp)
        l.d   $f0, -88($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -96($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -424($fp)
        s.d   $f0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 81.0
        # t47 = call root(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, fc29
        s.d   $f0, 0($sp)
        jal   _Z4rootd
        addiu $sp, $sp, 8
        s.d   $f0, -432($fp)
        # param t47
        # t48 = call roundToInt(double), 1
        addiu $sp, $sp, -8
        l.d   $f0, -432($fp)
        s.d   $f0, 0($sp)
        jal   _Z10roundToIntd
        addiu $sp, $sp, 8
        sw    $v0, -436($fp)
        # return t48
        lw    $v0, -436($fp)
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
