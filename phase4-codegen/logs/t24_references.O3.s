# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t24_references.c
#  Optimization : -O3 (TAC optimizations, registers, peephole)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str1:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str2:
        .byte 37, 46, 49, 102, 32, 37, 46, 49, 102, 32, 37, 100, 32, 37, 46, 49
        .byte 102, 10, 0
str3:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str4:
        .byte 99, 111, 110, 115, 116, 32, 100, 97, 116, 97, 0
str5:
        .byte 37, 99, 32, 37, 99, 10, 0
        .align 3
fc0:  .word 0, 1079582720        # 100.5
        .align 3
fc1:  .word 0, 1081032704        # 250
        .align 3
fc2:  .word 0, 1080623104        # 200
        .align 3
fc3:  .word 0, 1078525952        # 50
        .align 3
fc4:  .word 0, 1072955392        # 1.25
        .align 3
fc5:  .word 0, 1073741824        # 2
        .align 3
fc6:  .word 0, 1071644672        # 0.5

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

# deposit(struct Account &, double)
_Z7depositR7Accountd:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        s.d   $f20, -40($fp)
        s.d   $f22, -48($fp)
        s.d   $f24, -64($fp)
        sw    $s0, -28($fp)
        sw    $s1, -52($fp)
        lw    $s1, 8($fp)
        l.d   $f24, 16($fp)
        # t1 = a ptr+ 8
        addiu $s0, $s1, 8
        # t2 = *t1
        l.d   $f0, 0($s0)
        mov.d $f20, $f0
        # t3 = t2 double+ amount
        add.d $f22, $f20, $f24
        # *t1 = t3
        mov.d $f0, $f22
        s.d   $f0, 0($s0)
        # return
        j     _Z7depositR7Accountd_exit
_Z7depositR7Accountd_exit:
        l.d   $f20, -40($fp)
        l.d   $f22, -48($fp)
        l.d   $f24, -64($fp)
        lw    $s0, -28($fp)
        lw    $s1, -52($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# peek(const struct Account &)
_Z4peekRK7Account:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        s.d   $f20, -32($fp)
        sw    $s0, -20($fp)
        sw    $s1, -36($fp)
        lw    $s1, 8($fp)
        # t1 = a ptr+ 8
        addiu $s0, $s1, 8
        # t2 = *t1
        l.d   $f0, 0($s0)
        mov.d $f20, $f0
        # return t2
        mov.d $f0, $f20
        j     _Z4peekRK7Account_exit
_Z4peekRK7Account_exit:
        l.d   $f20, -32($fp)
        lw    $s0, -20($fp)
        lw    $s1, -36($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# richer(struct Account &, struct Account &)
_Z6richerR7AccountS0_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        s.d   $f20, -48($fp)
        s.d   $f22, -56($fp)
        sw    $s0, -36($fp)
        sw    $s1, -60($fp)
        sw    $s2, -64($fp)
        lw    $s1, 8($fp)
        lw    $s2, 12($fp)
        # t2 = a ptr+ 8
        addiu $s0, $s1, 8
        # t3 = *t2
        l.d   $f0, 0($s0)
        mov.d $f20, $f0
        # t4 = b ptr+ 8
        addiu $s0, $s2, 8
        # t5 = *t4
        l.d   $f0, 0($s0)
        mov.d $f22, $f0
        # if t3 double>= t5 goto 6
        c.le.d $f22, $f20
        bc1t  L2_6
        # goto 8
        j     L2_8
L2_6:
        # t1 = a
        move  $s0, $s1
        # goto 9
        j     L2_9
L2_8:
        # t1 = b
        move  $s0, $s2
L2_9:
        # return t1
        move  $v0, $s0
        j     _Z6richerR7AccountS0__exit
_Z6richerR7AccountS0__exit:
        l.d   $f20, -48($fp)
        l.d   $f22, -56($fp)
        lw    $s0, -36($fp)
        lw    $s1, -60($fp)
        lw    $s2, -64($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# minmax(const int *, int, int &, int &)
_Z6minmaxPKiiRiS1_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -72
        sw    $s0, -44($fp)
        sw    $s1, -72($fp)
        sw    $s2, -64($fp)
        sw    $s3, -68($fp)
        sw    $s4, -48($fp)
        sw    $s5, -52($fp)
        sw    $s6, -56($fp)
        sw    $s7, -60($fp)
        lw    $s2, 16($fp)
        lw    $s3, 20($fp)
        # t1 = *values
        lw    $t8, 8($fp)
        lw    $s0, 0($t8)
        # *hi = t1
        sw    $s0, 0($s3)
        # *lo = t1
        sw    $s0, 0($s2)
        # i = 1
        li    $s1, 1
L3_4:
        # if i int>= n goto 19
        lw    $t1, 12($fp)
        bge   $s1, $t1, L3_19
        # t2 = i int<< 2
        sll   $s4, $s1, 2
        # t3 = values ptr+ t2
        lw    $t0, 8($fp)
        addu  $s0, $t0, $s4
        # t4 = *t3
        lw    $s5, 0($s0)
        # t5 = *lo
        lw    $s6, 0($s2)
        # if t4 int>= t5 goto 12
        bge   $s5, $s6, L3_12
        # t8 = *t3
        lw    $s7, 0($s0)
        # *lo = t8
        sw    $s7, 0($s2)
L3_12:
        # t11 = *t3
        lw    $t0, 0($s0)
        sw    $t0, -32($fp)
        # t12 = *hi
        lw    $t0, 0($s3)
        sw    $t0, -36($fp)
        # if t11 int<= t12 goto 17
        lw    $t0, -32($fp)
        lw    $t1, -36($fp)
        ble   $t0, $t1, L3_17
        # t15 = *t3
        lw    $t0, 0($s0)
        sw    $t0, -40($fp)
        # *hi = t15
        sw    $t0, 0($s3)
L3_17:
        # i = i int+ 1
        addiu $s1, $s1, 1
        # goto 4
        j     L3_4
L3_19:
        # return
        j     _Z6minmaxPKiiRiS1__exit
_Z6minmaxPKiiRiS1__exit:
        lw    $s0, -44($fp)
        lw    $s1, -72($fp)
        lw    $s2, -64($fp)
        lw    $s3, -68($fp)
        lw    $s4, -48($fp)
        lw    $s5, -52($fp)
        lw    $s6, -56($fp)
        lw    $s7, -60($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# advance(int *&, int)
_Z7advanceRPii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        sw    $s0, -16($fp)
        sw    $s1, -20($fp)
        sw    $s2, -24($fp)
        sw    $s3, -28($fp)
        lw    $s3, 8($fp)
        lw    $s2, 12($fp)
        # t1 = *p
        lw    $s0, 0($s3)
        # t2 = steps int<< 2
        sll   $s1, $s2, 2
        # t3 = t1 ptr+ t2
        addu  $s2, $s0, $s1
        # *p = t3
        sw    $s2, 0($s3)
        # return
        j     _Z7advanceRPii_exit
_Z7advanceRPii_exit:
        lw    $s0, -16($fp)
        lw    $s1, -20($fp)
        lw    $s2, -24($fp)
        lw    $s3, -28($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# element(int *, int)
_Z7elementPii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        sw    $s2, -20($fp)
        lw    $s2, 8($fp)
        lw    $s1, 12($fp)
        # t1 = i int<< 2
        sll   $s0, $s1, 2
        # t2 = a ptr+ t1
        addu  $s1, $s2, $s0
        # return t2
        move  $v0, $s1
        j     _Z7elementPii_exit
_Z7elementPii_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        lw    $s2, -20($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# scale(const int &, const double &)
_Z5scaleRKiRKd:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -72
        s.d   $f20, -48($fp)
        s.d   $f22, -56($fp)
        s.d   $f24, -64($fp)
        sw    $s0, -40($fp)
        sw    $s1, -68($fp)
        sw    $s2, -72($fp)
        lw    $s1, 8($fp)
        lw    $s2, 12($fp)
        # t1 = *v
        lw    $s0, 0($s1)
        # t2 = inttodouble t1
        move  $t0, $s0
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        mov.d $f20, $f0
        # t3 = *factor
        l.d   $f0, 0($s2)
        mov.d $f22, $f0
        # t4 = t2 double* t3
        mul.d $f24, $f20, $f22
        # t5 = doubletoint t4
        mov.d $f0, $f24
        trunc.w.d $f0, $f0
        mfc1  $t0, $f0
        move  $s0, $t0
        # return t5
        move  $v0, $s0
        j     _Z5scaleRKiRKd_exit
_Z5scaleRKiRKd_exit:
        l.d   $f20, -48($fp)
        l.d   $f22, -56($fp)
        l.d   $f24, -64($fp)
        lw    $s0, -40($fp)
        lw    $s1, -68($fp)
        lw    $s2, -72($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# rotate(int &, int &, int &)
_Z6rotateRiS_S_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        sw    $s0, -20($fp)
        sw    $s1, -24($fp)
        sw    $s2, -28($fp)
        sw    $s3, -32($fp)
        sw    $s4, -36($fp)
        lw    $s2, 8($fp)
        lw    $s3, 12($fp)
        lw    $s4, 16($fp)
        # t1 = *a
        lw    $s0, 0($s2)
        # t2 = *b
        lw    $s1, 0($s3)
        # *a = t2
        sw    $s1, 0($s2)
        # t3 = *c
        lw    $s1, 0($s4)
        # *b = t3
        sw    $s1, 0($s3)
        # *c = t1
        sw    $s0, 0($s4)
        # return
        j     _Z6rotateRiS_S__exit
_Z6rotateRiS_S__exit:
        lw    $s0, -20($fp)
        lw    $s1, -24($fp)
        lw    $s2, -28($fp)
        lw    $s3, -32($fp)
        lw    $s4, -36($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# main()
main_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -568
        s.d   $f20, -544($fp)
        s.d   $f22, -552($fp)
        s.d   $f24, -568($fp)
        sw    $s0, -520($fp)
        sw    $s1, -528($fp)
        sw    $s2, -524($fp)
        sw    $s3, -532($fp)
        sw    $s4, -536($fp)
        sw    $s5, -556($fp)
        sw    $s6, -560($fp)
        # x = 1
        li    $t0, 1
        sw    $t0, -4($fp)
        # y = 2
        li    $t0, 2
        sw    $t0, -8($fp)
        # z = 3
        li    $t0, 3
        sw    $t0, -12($fp)
        # t1 = &x
        addiu $s0, $fp, -4
        # t2 = *t1
        lw    $s2, 0($s0)
        # t3 = t2 int+ 10
        addiu $s1, $s2, 10
        # *t1 = t3
        sw    $s1, 0($s0)
        # t5 = &y
        addiu $s2, $fp, -8
        # t6 = &z
        addiu $s3, $fp, -12
        # t66 = *t5
        lw    $s4, 0($s2)
        # *t1 = t66
        sw    $s4, 0($s0)
        # t67 = *t6
        lw    $s4, 0($s3)
        # *t5 = t67
        sw    $s4, 0($s2)
        # *t6 = t3
        sw    $s1, 0($s3)
        # t7 = *t1
        lw    $s1, 0($s0)
        # param "%d %d %d %d\n"
        # param x
        # param y
        # param z
        # param t7
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        lw    $t0, -8($fp)
        sw    $t0, 8($sp)
        lw    $t0, -12($fp)
        sw    $t0, 12($sp)
        sw    $s1, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # data[0] = 8
        li    $t0, 8
        sw    $t0, -40($fp)
        # data[4] = -3
        li    $t0, -3
        sw    $t0, -36($fp)
        # data[8] = 15
        li    $t0, 15
        sw    $t0, -32($fp)
        # data[12] = 0
        sw    $zero, -28($fp)
        # data[16] = 7
        li    $t0, 7
        sw    $t0, -24($fp)
        # t9 = &data
        addiu $s1, $fp, -40
        # t10 = &lo
        addiu $s2, $fp, -44
        # t11 = &hi
        addiu $s3, $fp, -48
        # param t9
        # param 5
        # param t10
        # param t11
        # call minmax(const int *, int, int &, int &), 4
        addiu $sp, $sp, -16
        sw    $s1, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        jal   _Z6minmaxPKiiRiS1_
        addiu $sp, $sp, 16
        # t71 = t9 ptr+ 12
        addiu $s2, $s1, 12
        # *t71 = 99
        li    $t0, 99
        sw    $t0, 0($s2)
        # t16 = *t9
        lw    $s2, 0($s1)
        # t17 = t16 int+ 1
        addiu $s3, $s2, 1
        # *t9 = t17
        sw    $s3, 0($s1)
        # p = t9
        move  $t0, $s1
        sw    $t0, -52($fp)
        # t19 = &p
        addiu $s1, $fp, -52
        # t78 = *t19
        lw    $s2, 0($s1)
        # t80 = t78 ptr+ 8
        addiu $s3, $s2, 8
        # *t19 = t80
        sw    $s3, 0($s1)
        # t20 = *p
        lw    $t8, -52($fp)
        lw    $s1, 0($t8)
        # t21 = t20 int+ 1
        addiu $s2, $s1, 1
        # *p = t21
        lw    $t8, -52($fp)
        sw    $s2, 0($t8)
        # t22 = data[12]
        lw    $s1, -28($fp)
        # t23 = data[0]
        lw    $s2, -40($fp)
        # t24 = data[8]
        lw    $s3, -32($fp)
        # param "%d %d %d %d %d\n"
        # param lo
        # param hi
        # param t22
        # param t23
        # param t24
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -44($fp)
        sw    $t0, 4($sp)
        lw    $t0, -48($fp)
        sw    $t0, 8($sp)
        sw    $s1, 12($sp)
        sw    $s2, 16($sp)
        sw    $s3, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # a[0] = 1
        li    $t0, 1
        sw    $t0, -72($fp)
        # a[8] = 100.5
        l.d   $f0, fc0
        s.d   $f0, -64($fp)
        # b[0] = 2
        li    $t0, 2
        sw    $t0, -88($fp)
        # b[8] = 2.5e+02
        l.d   $f0, fc1
        s.d   $f0, -80($fp)
        # t25 = &a
        addiu $s1, $fp, -72
        # t83 = t25 ptr+ 8
        addiu $s3, $s1, 8
        # t84 = *t83
        l.d   $f0, 0($s3)
        mov.d $f22, $f0
        # t85 = t84 double+ 2e+02
        l.d   $f2, fc2
        add.d $f20, $f22, $f2
        # *t83 = t85
        mov.d $f0, $f20
        s.d   $f0, 0($s3)
        # t27 = &b
        addiu $s2, $fp, -88
        # t90 = t27 ptr+ 8
        addiu $s5, $s2, 8
        # t91 = *t90
        l.d   $f0, 0($s5)
        mov.d $f22, $f0
        # if t85 double>= t91 goto 71
        c.le.d $f22, $f20
        bc1t  L8_71
        # goto 73
        j     L8_73
L8_71:
        # t92 = t25
        move  $s6, $s1
        # goto 74
        j     L8_74
L8_73:
        # t92 = t27
        move  $s6, $s2
L8_74:
        # t29 = t92 ptr+ 8
        addiu $s4, $s6, 8
        # t30 = *t29
        l.d   $f0, 0($s4)
        mov.d $f20, $f0
        # t31 = t30 double- 5e+01
        l.d   $f2, fc3
        sub.d $f22, $f20, $f2
        # *t29 = t31
        mov.d $f0, $f22
        s.d   $f0, 0($s4)
        # t96 = *t83
        l.d   $f0, 0($s3)
        mov.d $f20, $f0
        # t98 = *t90
        l.d   $f0, 0($s5)
        mov.d $f22, $f0
        # if t96 double>= t98 goto 82
        c.le.d $f22, $f20
        bc1t  L8_82
        # goto 84
        j     L8_84
L8_82:
        # t99 = t25
        move  $s3, $s1
        # goto 85
        j     L8_85
L8_84:
        # t99 = t27
        move  $s3, $s2
L8_85:
        # t36 = a[8]
        l.d   $f0, -64($fp)
        mov.d $f20, $f0
        # t37 = b[8]
        l.d   $f0, -80($fp)
        mov.d $f22, $f0
        # t38 = *t99
        lw    $s1, 0($s3)
        # t101 = t99 ptr+ 8
        addiu $s2, $s3, 8
        # t102 = *t101
        l.d   $f0, 0($s2)
        mov.d $f24, $f0
        # param "%.1f %.1f %d %.1f\n"
        # param t36
        # param t37
        # param t38
        # param t102
        # call printf, 5
        addiu $sp, $sp, -40
        la    $t0, str2
        sw    $t0, 0($sp)
        mov.d $f0, $f20
        s.d   $f0, 8($sp)
        mov.d $f0, $f22
        s.d   $f0, 16($sp)
        sw    $s1, 24($sp)
        mov.d $f0, $f24
        s.d   $f0, 32($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # limit = 40
        li    $t0, 40
        sw    $t0, -96($fp)
        # rate = 1.25
        l.d   $f0, fc4
        s.d   $f0, -104($fp)
        # t40 = &limit
        addiu $s1, $fp, -96
        # t41 = &rate
        addiu $s2, $fp, -104
        # t105 = *t40
        lw    $s3, 0($s1)
        # t106 = inttodouble t105
        move  $t0, $s3
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        mov.d $f20, $f0
        # t107 = *t41
        l.d   $f0, 0($s2)
        mov.d $f22, $f0
        # t108 = t106 double* t107
        mul.d $f24, $f20, $f22
        # t109 = doubletoint t108
        mov.d $f0, $f24
        trunc.w.d $f0, $f0
        mfc1  $t0, $f0
        move  $s3, $t0
        # t43 = 7
        li    $t0, 7
        sw    $t0, -248($fp)
        # t45 = &t43
        addiu $s1, $fp, -248
        # t46 = 2.0
        l.d   $f0, fc5
        s.d   $f0, -264($fp)
        # t47 = &t46
        addiu $s2, $fp, -264
        # t112 = *t45
        lw    $s4, 0($s1)
        # t113 = inttodouble t112
        move  $t0, $s4
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        mov.d $f20, $f0
        # t114 = *t47
        l.d   $f0, 0($s2)
        mov.d $f22, $f0
        # t115 = t113 double* t114
        mul.d $f24, $f20, $f22
        # t116 = doubletoint t115
        mov.d $f0, $f24
        trunc.w.d $f0, $f0
        mfc1  $t0, $f0
        move  $s4, $t0
        # t49 = 7
        li    $t0, 7
        sw    $t0, -272($fp)
        # t51 = &t49
        addiu $s1, $fp, -272
        # t52 = 0.5
        l.d   $f0, fc6
        s.d   $f0, -288($fp)
        # t53 = &t52
        addiu $s2, $fp, -288
        # t119 = *t51
        lw    $s5, 0($s1)
        # t120 = inttodouble t119
        move  $t0, $s5
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        mov.d $f20, $f0
        # t121 = *t53
        l.d   $f0, 0($s2)
        mov.d $f22, $f0
        # t122 = t120 double* t121
        mul.d $f24, $f20, $f22
        # t123 = doubletoint t122
        mov.d $f0, $f24
        trunc.w.d $f0, $f0
        mfc1  $t0, $f0
        move  $s1, $t0
        # param "%d %d %d\n"
        # param t109
        # param t116
        # param t123
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        sw    $s4, 8($sp)
        sw    $s1, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t55 = *"const data"
        la    $t8, str4
        lb    $s1, 0($t8)
        # t56 = chartoint t55
        move  $t0, $s1
        move  $s2, $t0
        # t57 = "const data" ptr+ 6
        la    $t0, str4
        addiu $s1, $t0, 6
        # t58 = *t57
        lb    $s3, 0($s1)
        # t59 = chartoint t58
        move  $t0, $s3
        move  $s1, $t0
        # param "%c %c\n"
        # param t56
        # param t59
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        sw    $s1, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t60 = *t1
        lw    $s1, 0($s0)
        # t61 = t60 int+ lo
        lw    $t1, -44($fp)
        addu  $s0, $s1, $t1
        # return t61
        move  $v0, $s0
        j     main__exit
main__exit:
        l.d   $f20, -544($fp)
        l.d   $f22, -552($fp)
        l.d   $f24, -568($fp)
        lw    $s0, -520($fp)
        lw    $s1, -528($fp)
        lw    $s2, -524($fp)
        lw    $s3, -532($fp)
        lw    $s4, -536($fp)
        lw    $s5, -556($fp)
        lw    $s6, -560($fp)
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
