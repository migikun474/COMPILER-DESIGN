# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t16_runtime.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 37, 115, 32, 37, 108, 108, 100, 10, 0
str1:
        .byte 37, 108, 108, 100, 32, 37, 108, 108, 100, 32, 37, 108, 108, 100, 10, 0
str2:
        .byte 37, 108, 108, 100, 32, 37, 108, 108, 100, 32, 37, 108, 108, 100, 32, 37
        .byte 108, 108, 100, 10, 0
str3:
        .byte 37, 108, 108, 100, 32, 37, 108, 108, 100, 10, 0
str4:
        .byte 37, 108, 108, 117, 32, 37, 108, 108, 117, 32, 37, 108, 108, 117, 10, 0
str5:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str6:
        .byte 37, 108, 108, 100, 32, 37, 108, 108, 120, 10, 0
str7:
        .byte 37, 46, 49, 102, 32, 37, 46, 49, 102, 32, 37, 46, 49, 102, 32, 37
        .byte 46, 49, 102, 10, 0
str8:
        .byte 37, 100, 32, 37, 117, 32, 37, 108, 108, 100, 32, 37, 100, 10, 0
str9:
        .byte 37, 108, 108, 100, 32, 37, 100, 32, 37, 100, 10, 0
str10:
        .byte 37, 46, 50, 102, 32, 37, 46, 50, 102, 32, 37, 46, 50, 102, 32, 37
        .byte 46, 50, 102, 32, 37, 100, 10, 0
str11:
        .byte 91, 37, 54, 46, 50, 102, 93, 32, 91, 37, 45, 56, 46, 51, 102, 93
        .byte 32, 91, 37, 48, 56, 46, 50, 102, 93, 32, 91, 37, 46, 48, 102, 93
        .byte 32, 91, 37, 102, 93, 10, 0
str12:
        .byte 91, 37, 53, 100, 93, 32, 91, 37, 45, 53, 100, 93, 32, 91, 37, 48
        .byte 53, 100, 93, 32, 91, 37, 120, 93, 32, 91, 37, 88, 93, 32, 91, 37
        .byte 111, 93, 32, 91, 37, 53, 115, 93, 32, 91, 37, 45, 53, 115, 93, 32
        .byte 91, 37, 99, 93, 32, 91, 37, 37, 93, 10, 0
str13:
        .byte 97, 98, 0
str14:
        .byte 99, 100, 0
str15:
        .byte 91, 37, 42, 100, 93, 32, 91, 37, 46, 42, 102, 93, 32, 91, 37, 51
        .byte 115, 93, 10, 0
str16:
        .byte 108, 111, 110, 103, 32, 115, 116, 114, 105, 110, 103, 0
str17:
        .byte 37, 46, 49, 102, 32, 37, 100, 32, 37, 100, 32, 37, 99, 32, 37, 108
        .byte 108, 100, 10, 0
str18:
        .byte 37, 46, 49, 102, 10, 0
str19:
        .byte 37, 46, 50, 102, 10, 0
str20:
        .byte 116, 97, 105, 108, 0
        .align 3
fc0:  .word 0, 1073217536        # 1.5
        .align 3
fc1:  .word 0, 1106247680        # 4.29497e+09
        .align 3
fc2:  .word 0, 0        # 0
        .align 3
fc3:  .word 0, 1074003968        # 2.5
        .align 3
fc4:  .word 536870912, 1106419807        # 5e+09
        .align 3
fc5:  .word 1069547520        # 1.5
        .align 3
fc6:  .word 1074790400        # 2.25
        .align 3
fc7:  .word 4028335726, 1074340345        # 3.14159
        .align 3
fc8:  .word 0, 1075609600        # 7.125
        .align 3
fc9:  .word 2576980378, 1069128089        # 0.1
        .align 3
fc10:  .word 4237242936, 1072939201        # 1.23456
        .align 3
fc11:  .word 0, 1073741824        # 2
        .align 3
fc12:  .word 0, 1072693248        # 1
        .align 3
fc13:  .word 0, 1074790400        # 4

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

# make(int)
_Z4makei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -104
        # t1 = inttodouble k
        lw    $t0, 8($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -56($fp)
        # t2 = t1 double* 1.5
        l.d   $f0, -56($fp)
        l.d   $f2, fc0
        mul.d $f0, $f0, $f2
        s.d   $f0, -64($fp)
        # b[0] = t2
        addiu $t8, $fp, -40
        li    $t9, 0
        addu  $t8, $t8, $t9
        l.d   $f0, -64($fp)
        s.d   $f0, 0($t8)
        # i = 0
        li    $t0, 0
        sw    $t0, -44($fp)
L0_4:
        # if i int< 5 goto 6
        lw    $t0, -44($fp)
        li    $t1, 5
        blt   $t0, $t1, L0_6
        # goto 13
        j     L0_13
L0_6:
        # t3 = i int* 4
        lw    $t0, -44($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -68($fp)
        # t4 = 8 int+ t3
        li    $t0, 8
        lw    $t1, -68($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -72($fp)
        # t5 = k int+ i
        lw    $t0, 8($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # b[t4] = t5
        addiu $t8, $fp, -40
        lw    $t9, -72($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -76($fp)
        sw    $t0, 0($t8)
        # t6 = i int+ 1
        lw    $t0, -44($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -80($fp)
        # i = t6
        lw    $t0, -80($fp)
        sw    $t0, -44($fp)
        # goto 4
        j     L0_4
L0_13:
        # t7 = 65 int+ k
        li    $t0, 65
        lw    $t1, 8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -84($fp)
        # t8 = inttochar t7
        lw    $t0, -84($fp)
        sb    $t0, -85($fp)
        # b[28] = t8
        addiu $t8, $fp, -40
        li    $t9, 28
        addu  $t8, $t8, $t9
        lb    $t0, -85($fp)
        sb    $t0, 0($t8)
        # t9 = inttollong k
        lw    $t0, 8($fp)
        sra   $t1, $t0, 31
        sw    $t0, -96($fp)
        sw    $t1, -92($fp)
        # t10 = 10000000000 llong* t9
        li    $t0, 1410065408
        li    $t1, 2
        lw    $t2, -96($fp)
        lw    $t3, -92($fp)
        multu $t0, $t2
        mflo  $t4
        mfhi  $t5
        mul   $t6, $t0, $t3
        addu  $t5, $t5, $t6
        mul   $t6, $t1, $t2
        addu  $t6, $t5, $t6
        sw    $t4, -104($fp)
        sw    $t6, -100($fp)
        # b[32] = t10
        addiu $t8, $fp, -40
        li    $t9, 32
        addu  $t8, $t8, $t9
        lw    $t0, -104($fp)
        lw    $t1, -100($fp)
        sw    $t0, 0($t8)
        sw    $t1, 4($t8)
        # return b
        addiu $v0, $fp, -40
        j     _Z4makei_exit
_Z4makei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# weigh(struct Big, double, char, long long)
_Z5weigh3Bigdcx:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -104
        # t1 = b[0]
        addiu $t8, $fp, 8
        li    $t9, 0
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -8($fp)
        # t2 = t1 double* scale
        l.d   $f0, -8($fp)
        l.d   $f2, 48($fp)
        mul.d $f0, $f0, $f2
        s.d   $f0, -16($fp)
        # t3 = b[24]
        addiu $t8, $fp, 8
        li    $t9, 24
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t4 = inttodouble t3
        lw    $t0, -20($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -32($fp)
        # t5 = t2 double+ t4
        l.d   $f0, -16($fp)
        l.d   $f2, -32($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -40($fp)
        # t6 = chartodouble c
        lb    $t0, 56($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -48($fp)
        # t7 = t5 double+ t6
        l.d   $f0, -40($fp)
        l.d   $f2, -48($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -56($fp)
        # t8 = b[32]
        addiu $t8, $fp, 8
        li    $t9, 32
        addu  $t8, $t8, $t9
        lw    $t1, 4($t8)
        lw    $t0, 0($t8)
        sw    $t0, -64($fp)
        sw    $t1, -60($fp)
        # t9 = t8 llong/ 1000000000
        lw    $a0, -64($fp)
        lw    $a1, -60($fp)
        li    $a2, 1000000000
        li    $a3, 0
        jal   __divll
        sw    $v0, -72($fp)
        sw    $v1, -68($fp)
        # t10 = llongtodouble t9
        lw    $t0, -72($fp)
        lw    $t1, -68($fp)
        mtc1  $t1, $f0
        cvt.d.w $f0, $f0
        l.d   $f4, fc1
        mul.d $f6, $f0, $f4
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        bgez  $t0, M1_0
        l.d   $f2, fc1
        add.d $f0, $f0, $f2
M1_0:
        add.d $f0, $f0, $f6
        s.d   $f0, -80($fp)
        # t11 = t7 double+ t10
        l.d   $f0, -56($fp)
        l.d   $f2, -80($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -88($fp)
        # t12 = llongtodouble extra
        lw    $t0, 64($fp)
        lw    $t1, 68($fp)
        mtc1  $t1, $f0
        cvt.d.w $f0, $f0
        l.d   $f4, fc1
        mul.d $f6, $f0, $f4
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        bgez  $t0, M1_1
        l.d   $f2, fc1
        add.d $f0, $f0, $f2
M1_1:
        add.d $f0, $f0, $f6
        s.d   $f0, -96($fp)
        # t13 = t11 double+ t12
        l.d   $f0, -88($fp)
        l.d   $f2, -96($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -104($fp)
        # return t13
        l.d   $f0, -104($fp)
        j     _Z5weigh3Bigdcx_exit
_Z5weigh3Bigdcx_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# average(int, ...)
_Z7averageiz:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -96
        # va_start ap, count
        addiu $t0, $fp, 12
        sw    $t0, -4($fp)
        # total = 0.0
        l.d   $f0, fc2
        s.d   $f0, -16($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -20($fp)
L2_3:
        # if i int< count goto 5
        lw    $t0, -20($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L2_5
        # goto 11
        j     L2_11
L2_5:
        # t1 = va_arg ap, double
        lw    $t8, -4($fp)
        addiu $t8, $t8, 7
        li    $t9, -8
        and   $t8, $t8, $t9
        addiu $t9, $t8, 8
        sw    $t9, -4($fp)
        l.d   $f0, 0($t8)
        s.d   $f0, -48($fp)
        # t2 = total double+ t1
        l.d   $f0, -16($fp)
        l.d   $f2, -48($fp)
        add.d $f0, $f0, $f2
        s.d   $f0, -56($fp)
        # total = t2
        l.d   $f0, -56($fp)
        s.d   $f0, -16($fp)
        # t3 = i int+ 1
        lw    $t0, -20($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # i = t3
        lw    $t0, -60($fp)
        sw    $t0, -20($fp)
        # goto 3
        j     L2_3
L2_11:
        # t4 = va_arg ap, llong
        lw    $t8, -4($fp)
        addiu $t8, $t8, 7
        li    $t9, -8
        and   $t8, $t8, $t9
        addiu $t9, $t8, 8
        sw    $t9, -4($fp)
        lw    $t1, 4($t8)
        lw    $t0, 0($t8)
        sw    $t0, -72($fp)
        sw    $t1, -68($fp)
        # tail = t4
        lw    $t0, -72($fp)
        lw    $t1, -68($fp)
        sw    $t0, -32($fp)
        sw    $t1, -28($fp)
        # t5 = va_arg ap, ptr
        lw    $t8, -4($fp)
        addiu $t9, $t8, 4
        sw    $t9, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -76($fp)
        # label = t5
        lw    $t0, -76($fp)
        sw    $t0, -36($fp)
        # va_end ap
        # param "%s %lld\n"
        # param label
        # param tail
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -36($fp)
        sw    $t0, 4($sp)
        lw    $t0, -32($fp)
        lw    $t1, -28($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t6 = inttodouble count
        lw    $t0, 8($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -88($fp)
        # t7 = total double/ t6
        l.d   $f0, -16($fp)
        l.d   $f2, -88($fp)
        div.d $f0, $f0, $f2
        s.d   $f0, -96($fp)
        # return t7
        l.d   $f0, -96($fp)
        j     _Z7averageiz_exit
_Z7averageiz_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# power(long long, int)
_Z5powerxi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # if n int== 0 goto 2
        lw    $t0, 16($fp)
        li    $t1, 0
        beq   $t0, $t1, L3_2
        # goto 4
        j     L3_4
L3_2:
        # t1 = 1
        li    $t0, 1
        li    $t1, 0
        sw    $t0, -8($fp)
        sw    $t1, -4($fp)
        # goto 10
        j     L3_10
L3_4:
        # t2 = n int- 1
        lw    $t0, 16($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # param base
        # param t2
        # t3 = call power(long long, int), 2
        addiu $sp, $sp, -16
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        sw    $t0, 0($sp)
        sw    $t1, 4($sp)
        lw    $t0, -12($fp)
        sw    $t0, 8($sp)
        jal   _Z5powerxi
        addiu $sp, $sp, 16
        sw    $v0, -24($fp)
        sw    $v1, -20($fp)
        # t4 = base llong* t3
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        lw    $t2, -24($fp)
        lw    $t3, -20($fp)
        multu $t0, $t2
        mflo  $t4
        mfhi  $t5
        mul   $t6, $t0, $t3
        addu  $t5, $t5, $t6
        mul   $t6, $t1, $t2
        addu  $t6, $t5, $t6
        sw    $t4, -32($fp)
        sw    $t6, -28($fp)
        # t1 = t4
        lw    $t0, -32($fp)
        lw    $t1, -28($fp)
        sw    $t0, -8($fp)
        sw    $t1, -4($fp)
L3_10:
        # return t1
        lw    $v0, -8($fp)
        lw    $v1, -4($fp)
        j     _Z5powerxi_exit
_Z5powerxi_exit:
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
        addiu $sp, $sp, -696
        # a = 123456789012345
        li    $t0, -2045911175
        li    $t1, 28744
        sw    $t0, -8($fp)
        sw    $t1, -4($fp)
        # t1 = llong- 987654321
        li    $t0, 987654321
        li    $t1, 0
        sltu  $t5, $zero, $t0
        negu  $t4, $t0
        negu  $t6, $t1
        subu  $t6, $t6, $t5
        sw    $t4, -168($fp)
        sw    $t6, -164($fp)
        # b = t1
        lw    $t0, -168($fp)
        lw    $t1, -164($fp)
        sw    $t0, -16($fp)
        sw    $t1, -12($fp)
        # u = 18000000000000000000
        li    $t0, -989331456
        li    $t1, -104015711
        sw    $t0, -24($fp)
        sw    $t1, -20($fp)
        # t2 = a llong+ b
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        lw    $t2, -16($fp)
        lw    $t3, -12($fp)
        addu  $t4, $t0, $t2
        sltu  $t5, $t4, $t0
        addu  $t6, $t1, $t3
        addu  $t6, $t6, $t5
        sw    $t4, -176($fp)
        sw    $t6, -172($fp)
        # t3 = a llong- b
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        lw    $t2, -16($fp)
        lw    $t3, -12($fp)
        sltu  $t5, $t0, $t2
        subu  $t4, $t0, $t2
        subu  $t6, $t1, $t3
        subu  $t6, $t6, $t5
        sw    $t4, -184($fp)
        sw    $t6, -180($fp)
        # t4 = a llong* 3
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        li    $t2, 3
        li    $t3, 0
        multu $t0, $t2
        mflo  $t4
        mfhi  $t5
        mul   $t6, $t0, $t3
        addu  $t5, $t5, $t6
        mul   $t6, $t1, $t2
        addu  $t6, $t5, $t6
        sw    $t4, -192($fp)
        sw    $t6, -188($fp)
        # param "%lld %lld %lld\n"
        # param t2
        # param t3
        # param t4
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -176($fp)
        lw    $t1, -172($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -184($fp)
        lw    $t1, -180($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        lw    $t0, -192($fp)
        lw    $t1, -188($fp)
        sw    $t0, 24($sp)
        sw    $t1, 28($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # t5 = a llong/ 1000
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        li    $a2, 1000
        li    $a3, 0
        jal   __divll
        sw    $v0, -200($fp)
        sw    $v1, -196($fp)
        # t6 = a llong% 1000
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        li    $a2, 1000
        li    $a3, 0
        jal   __modll
        sw    $v0, -208($fp)
        sw    $v1, -204($fp)
        # t7 = a llong/ b
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        lw    $a2, -16($fp)
        lw    $a3, -12($fp)
        jal   __divll
        sw    $v0, -216($fp)
        sw    $v1, -212($fp)
        # t8 = a llong% b
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        lw    $a2, -16($fp)
        lw    $a3, -12($fp)
        jal   __modll
        sw    $v0, -224($fp)
        sw    $v1, -220($fp)
        # param "%lld %lld %lld %lld\n"
        # param t5
        # param t6
        # param t7
        # param t8
        # call printf, 5
        addiu $sp, $sp, -40
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -200($fp)
        lw    $t1, -196($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -208($fp)
        lw    $t1, -204($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        lw    $t0, -216($fp)
        lw    $t1, -212($fp)
        sw    $t0, 24($sp)
        sw    $t1, 28($sp)
        lw    $t0, -224($fp)
        lw    $t1, -220($fp)
        sw    $t0, 32($sp)
        sw    $t1, 36($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # t9 = b llong/ 7
        lw    $a0, -16($fp)
        lw    $a1, -12($fp)
        li    $a2, 7
        li    $a3, 0
        jal   __divll
        sw    $v0, -232($fp)
        sw    $v1, -228($fp)
        # t10 = b llong% 7
        lw    $a0, -16($fp)
        lw    $a1, -12($fp)
        li    $a2, 7
        li    $a3, 0
        jal   __modll
        sw    $v0, -240($fp)
        sw    $v1, -236($fp)
        # param "%lld %lld\n"
        # param t9
        # param t10
        # call printf, 3
        addiu $sp, $sp, -24
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -232($fp)
        lw    $t1, -228($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -240($fp)
        lw    $t1, -236($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t11 = u ullong/ 10
        lw    $a0, -24($fp)
        lw    $a1, -20($fp)
        li    $a2, 10
        li    $a3, 0
        jal   __udivll
        sw    $v0, -248($fp)
        sw    $v1, -244($fp)
        # t12 = u ullong% 1000
        lw    $a0, -24($fp)
        lw    $a1, -20($fp)
        li    $a2, 1000
        li    $a3, 0
        jal   __umodll
        sw    $v0, -256($fp)
        sw    $v1, -252($fp)
        # t13 = u ullong>> 3
        lw    $a0, -24($fp)
        lw    $a1, -20($fp)
        li    $a2, 3
        jal   __shrll
        sw    $v0, -264($fp)
        sw    $v1, -260($fp)
        # param "%llu %llu %llu\n"
        # param t11
        # param t12
        # param t13
        # call printf, 4
        addiu $sp, $sp, -32
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -248($fp)
        lw    $t1, -244($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -256($fp)
        lw    $t1, -252($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        lw    $t0, -264($fp)
        lw    $t1, -260($fp)
        sw    $t0, 24($sp)
        sw    $t1, 28($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # t14 = a llong<< 5
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        li    $a2, 5
        jal   __shlll
        sw    $v0, -272($fp)
        sw    $v1, -268($fp)
        # t15 = a llong>> 7
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        li    $a2, 7
        jal   __sarll
        sw    $v0, -280($fp)
        sw    $v1, -276($fp)
        # t16 = b llong>> 4
        lw    $a0, -16($fp)
        lw    $a1, -12($fp)
        li    $a2, 4
        jal   __sarll
        sw    $v0, -288($fp)
        sw    $v1, -284($fp)
        # t17 = 1 llong<< 40
        li    $a0, 1
        li    $a1, 0
        li    $a2, 40
        jal   __shlll
        sw    $v0, -296($fp)
        sw    $v1, -292($fp)
        # param "%lld %lld %lld %lld\n"
        # param t14
        # param t15
        # param t16
        # param t17
        # call printf, 5
        addiu $sp, $sp, -40
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -272($fp)
        lw    $t1, -268($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -280($fp)
        lw    $t1, -276($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        lw    $t0, -288($fp)
        lw    $t1, -284($fp)
        sw    $t0, 24($sp)
        sw    $t1, 28($sp)
        lw    $t0, -296($fp)
        lw    $t1, -292($fp)
        sw    $t0, 32($sp)
        sw    $t1, 36($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # if a llong> b goto 49
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        lw    $t2, -16($fp)
        lw    $t3, -12($fp)
        blt   $t3, $t1, L4_49
        bne   $t3, $t1, M4_0
        bltu  $t2, $t0, L4_49
M4_0:
        # t18 = 0
        li    $t0, 0
        sw    $t0, -300($fp)
        # goto 50
        j     L4_50
L4_49:
        # t18 = 1
        li    $t0, 1
        sw    $t0, -300($fp)
L4_50:
        # if b llong< 0 goto 53
        lw    $t0, -16($fp)
        lw    $t1, -12($fp)
        li    $t2, 0
        li    $t3, 0
        blt   $t1, $t3, L4_53
        bne   $t1, $t3, M4_1
        bltu  $t0, $t2, L4_53
M4_1:
        # t19 = 0
        li    $t0, 0
        sw    $t0, -304($fp)
        # goto 54
        j     L4_54
L4_53:
        # t19 = 1
        li    $t0, 1
        sw    $t0, -304($fp)
L4_54:
        # if a llong== a goto 57
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        lw    $t2, -8($fp)
        lw    $t3, -4($fp)
        xor   $t4, $t0, $t2
        xor   $t5, $t1, $t3
        or    $t4, $t4, $t5
        beqz  $t4, L4_57
        # t20 = 0
        li    $t0, 0
        sw    $t0, -308($fp)
        # goto 58
        j     L4_58
L4_57:
        # t20 = 1
        li    $t0, 1
        sw    $t0, -308($fp)
L4_58:
        # if u ullong> a goto 61
        lw    $t0, -24($fp)
        lw    $t1, -20($fp)
        lw    $t2, -8($fp)
        lw    $t3, -4($fp)
        bltu  $t3, $t1, L4_61
        bne   $t3, $t1, M4_2
        bltu  $t2, $t0, L4_61
M4_2:
        # t21 = 0
        li    $t0, 0
        sw    $t0, -312($fp)
        # goto 62
        j     L4_62
L4_61:
        # t21 = 1
        li    $t0, 1
        sw    $t0, -312($fp)
L4_62:
        # param "%d %d %d %d\n"
        # param t18
        # param t19
        # param t20
        # param t21
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str5
        sw    $t0, 0($sp)
        lw    $t0, -300($fp)
        sw    $t0, 4($sp)
        lw    $t0, -304($fp)
        sw    $t0, 8($sp)
        lw    $t0, -308($fp)
        sw    $t0, 12($sp)
        lw    $t0, -312($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 3
        # param 30
        # t22 = call power(long long, int), 2
        addiu $sp, $sp, -16
        li    $t0, 3
        li    $t1, 0
        sw    $t0, 0($sp)
        sw    $t1, 4($sp)
        li    $t0, 30
        sw    $t0, 8($sp)
        jal   _Z5powerxi
        addiu $sp, $sp, 16
        sw    $v0, -320($fp)
        sw    $v1, -316($fp)
        # param "%lld %llx\n"
        # param t22
        # param u
        # call printf, 3
        addiu $sp, $sp, -24
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -320($fp)
        lw    $t1, -316($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -24($fp)
        lw    $t1, -20($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t23 = llong- a
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        sltu  $t5, $zero, $t0
        negu  $t4, $t0
        negu  $t6, $t1
        subu  $t6, $t6, $t5
        sw    $t4, -328($fp)
        sw    $t6, -324($fp)
        # t24 = llong~ a
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        nor   $t4, $t0, $zero
        nor   $t6, $t1, $zero
        sw    $t4, -336($fp)
        sw    $t6, -332($fp)
        # param "%lld %lld\n"
        # param t23
        # param t24
        # call printf, 3
        addiu $sp, $sp, -24
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -328($fp)
        lw    $t1, -324($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -336($fp)
        lw    $t1, -332($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t25 = int- 7
        li    $t0, 7
        negu  $t0, $t0
        sw    $t0, -340($fp)
        # i = t25
        lw    $t0, -340($fp)
        sw    $t0, -28($fp)
        # big = 3000000000
        li    $t0, -1294967296
        sw    $t0, -32($fp)
        # t26 = inttodouble i
        lw    $t0, -28($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        s.d   $f0, -352($fp)
        # d = t26
        l.d   $f0, -352($fp)
        s.d   $f0, -40($fp)
        # t27 = uinttodouble big
        lw    $t0, -32($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        bgez  $t0, M4_3
        l.d   $f2, fc1
        add.d $f0, $f0, $f2
M4_3:
        s.d   $f0, -360($fp)
        # e = t27
        l.d   $f0, -360($fp)
        s.d   $f0, -48($fp)
        # t28 = llongtodouble a
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        mtc1  $t1, $f0
        cvt.d.w $f0, $f0
        l.d   $f4, fc1
        mul.d $f6, $f0, $f4
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        bgez  $t0, M4_4
        l.d   $f2, fc1
        add.d $f0, $f0, $f2
M4_4:
        add.d $f0, $f0, $f6
        s.d   $f0, -368($fp)
        # f = t28
        l.d   $f0, -368($fp)
        s.d   $f0, -56($fp)
        # t29 = uinttofloat big
        lw    $t0, -32($fp)
        mtc1  $t0, $f0
        cvt.d.w $f0, $f0
        bgez  $t0, M4_5
        l.d   $f2, fc1
        add.d $f0, $f0, $f2
M4_5:
        cvt.s.d $f0, $f0
        s.s   $f0, -372($fp)
        # fl = t29
        l.s   $f0, -372($fp)
        s.s   $f0, -60($fp)
        # t30 = floattodouble fl
        l.s   $f0, -60($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -384($fp)
        # param "%.1f %.1f %.1f %.1f\n"
        # param d
        # param e
        # param f
        # param t30
        # call printf, 5
        addiu $sp, $sp, -40
        la    $t0, str7
        sw    $t0, 0($sp)
        l.d   $f0, -40($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -48($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -56($fp)
        s.d   $f0, 24($sp)
        l.d   $f0, -384($fp)
        s.d   $f0, 32($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # t31 = double- 2.5
        l.d   $f0, fc3
        neg.d $f0, $f0
        s.d   $f0, -392($fp)
        # t32 = doubletoint t31
        l.d   $f0, -392($fp)
        trunc.w.d $f0, $f0
        mfc1  $t0, $f0
        sw    $t0, -396($fp)
        # param "%d %u %lld %d\n"
        # param 3
        # param 3000000000
        # param 12345678901
        # param t32
        # call printf, 5
        addiu $sp, $sp, -32
        la    $t0, str8
        sw    $t0, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        li    $t0, -1294967296
        sw    $t0, 8($sp)
        li    $t0, -539222987
        li    $t1, 2
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        lw    $t0, -396($fp)
        sw    $t0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # t33 = double- 5e+09
        l.d   $f0, fc4
        neg.d $f0, $f0
        s.d   $f0, -408($fp)
        # t34 = doubletollong t33
        l.d   $f0, -408($fp)
        mov.d $f12, $f0
        jal   __dtoll
        sw    $v0, -416($fp)
        sw    $v1, -412($fp)
        # param "%lld %d %d\n"
        # param t34
        # param -56
        # param 4464
        # call printf, 4
        addiu $sp, $sp, -24
        la    $t0, str9
        sw    $t0, 0($sp)
        lw    $t0, -416($fp)
        lw    $t1, -412($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        li    $t0, -56
        sw    $t0, 16($sp)
        li    $t0, 4464
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # x = 1.5
        l.s   $f0, fc5
        s.s   $f0, -64($fp)
        # y = 2.25
        l.s   $f0, fc6
        s.s   $f0, -68($fp)
        # t35 = x float+ y
        l.s   $f0, -64($fp)
        l.s   $f2, -68($fp)
        add.s $f0, $f0, $f2
        s.s   $f0, -420($fp)
        # t36 = floattodouble t35
        l.s   $f0, -420($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -432($fp)
        # t37 = x float* y
        l.s   $f0, -64($fp)
        l.s   $f2, -68($fp)
        mul.s $f0, $f0, $f2
        s.s   $f0, -436($fp)
        # t38 = floattodouble t37
        l.s   $f0, -436($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -448($fp)
        # t39 = x float/ y
        l.s   $f0, -64($fp)
        l.s   $f2, -68($fp)
        div.s $f0, $f0, $f2
        s.s   $f0, -452($fp)
        # t40 = floattodouble t39
        l.s   $f0, -452($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -464($fp)
        # t41 = float- x
        l.s   $f0, -64($fp)
        neg.s $f0, $f0
        s.s   $f0, -468($fp)
        # t42 = floattodouble t41
        l.s   $f0, -468($fp)
        cvt.d.s $f0, $f0
        s.d   $f0, -480($fp)
        # if x float< y goto 127
        l.s   $f0, -64($fp)
        l.s   $f2, -68($fp)
        c.lt.s $f0, $f2
        bc1t  L4_127
        # t43 = 0
        li    $t0, 0
        sw    $t0, -484($fp)
        # goto 128
        j     L4_128
L4_127:
        # t43 = 1
        li    $t0, 1
        sw    $t0, -484($fp)
L4_128:
        # param "%.2f %.2f %.2f %.2f %d\n"
        # param t36
        # param t38
        # param t40
        # param t42
        # param t43
        # call printf, 6
        addiu $sp, $sp, -48
        la    $t0, str10
        sw    $t0, 0($sp)
        l.d   $f0, -432($fp)
        s.d   $f0, 8($sp)
        l.d   $f0, -448($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, -464($fp)
        s.d   $f0, 24($sp)
        l.d   $f0, -480($fp)
        s.d   $f0, 32($sp)
        lw    $t0, -484($fp)
        sw    $t0, 40($sp)
        jal   __printf
        addiu $sp, $sp, 48
        # t44 = double- 2.5
        l.d   $f0, fc3
        neg.d $f0, $f0
        s.d   $f0, -496($fp)
        # param "[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n"
        # param 3.14159
        # param t44
        # param 7.125
        # param 2.5
        # param 0.1
        # call printf, 6
        addiu $sp, $sp, -48
        la    $t0, str11
        sw    $t0, 0($sp)
        l.d   $f0, fc7
        s.d   $f0, 8($sp)
        l.d   $f0, -496($fp)
        s.d   $f0, 16($sp)
        l.d   $f0, fc8
        s.d   $f0, 24($sp)
        l.d   $f0, fc3
        s.d   $f0, 32($sp)
        l.d   $f0, fc9
        s.d   $f0, 40($sp)
        jal   __printf
        addiu $sp, $sp, 48
        # t45 = int- 42
        li    $t0, 42
        negu  $t0, $t0
        sw    $t0, -500($fp)
        # t46 = int- 42
        li    $t0, 42
        negu  $t0, $t0
        sw    $t0, -504($fp)
        # param "[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n"
        # param t45
        # param 42
        # param t46
        # param 255
        # param 255
        # param 8
        # param "ab"
        # param "cd"
        # param 122
        # call printf, 10
        addiu $sp, $sp, -40
        la    $t0, str12
        sw    $t0, 0($sp)
        lw    $t0, -500($fp)
        sw    $t0, 4($sp)
        li    $t0, 42
        sw    $t0, 8($sp)
        lw    $t0, -504($fp)
        sw    $t0, 12($sp)
        li    $t0, 255
        sw    $t0, 16($sp)
        li    $t0, 255
        sw    $t0, 20($sp)
        li    $t0, 8
        sw    $t0, 24($sp)
        la    $t0, str13
        sw    $t0, 28($sp)
        la    $t0, str14
        sw    $t0, 32($sp)
        li    $t0, 122
        sw    $t0, 36($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # param "[%*d] [%.*f] [%3s]\n"
        # param 6
        # param 12
        # param 2
        # param 1.23456
        # param "long string"
        # call printf, 6
        addiu $sp, $sp, -32
        la    $t0, str15
        sw    $t0, 0($sp)
        li    $t0, 6
        sw    $t0, 4($sp)
        li    $t0, 12
        sw    $t0, 8($sp)
        li    $t0, 2
        sw    $t0, 12($sp)
        l.d   $f0, fc10
        s.d   $f0, 16($sp)
        la    $t0, str16
        sw    $t0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 2
        # t47 = call make(int), 1
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        jal   _Z4makei
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -544
        li    $a2, 40
        jal   __memcpy
        # t48 = &t47
        addiu $t0, $fp, -544
        sw    $t0, -548($fp)
        # s = t47
        addiu $a0, $fp, -112
        addiu $a1, $fp, -544
        li    $a2, 40
        jal   __memcpy
        # t49 = &s
        addiu $t0, $fp, -112
        sw    $t0, -552($fp)
        # t = s
        addiu $a0, $fp, -152
        addiu $a1, $fp, -112
        li    $a2, 40
        jal   __memcpy
        # t50 = &t
        addiu $t0, $fp, -152
        sw    $t0, -556($fp)
        # t[24] = 100
        addiu $t8, $fp, -152
        li    $t9, 24
        addu  $t8, $t8, $t9
        li    $t0, 100
        sw    $t0, 0($t8)
        # t51 = s[0]
        addiu $t8, $fp, -112
        li    $t9, 0
        addu  $t8, $t8, $t9
        l.d   $f0, 0($t8)
        s.d   $f0, -568($fp)
        # t52 = s[24]
        addiu $t8, $fp, -112
        li    $t9, 24
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -572($fp)
        # t53 = t[24]
        addiu $t8, $fp, -152
        li    $t9, 24
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -576($fp)
        # t54 = s[28]
        addiu $t8, $fp, -112
        li    $t9, 28
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -577($fp)
        # t55 = chartoint t54
        lb    $t0, -577($fp)
        sw    $t0, -584($fp)
        # t56 = s[32]
        addiu $t8, $fp, -112
        li    $t9, 32
        addu  $t8, $t8, $t9
        lw    $t1, 4($t8)
        lw    $t0, 0($t8)
        sw    $t0, -592($fp)
        sw    $t1, -588($fp)
        # param "%.1f %d %d %c %lld\n"
        # param t51
        # param t52
        # param t53
        # param t55
        # param t56
        # call printf, 6
        addiu $sp, $sp, -40
        la    $t0, str17
        sw    $t0, 0($sp)
        l.d   $f0, -568($fp)
        s.d   $f0, 8($sp)
        lw    $t0, -572($fp)
        sw    $t0, 16($sp)
        lw    $t0, -576($fp)
        sw    $t0, 20($sp)
        lw    $t0, -584($fp)
        sw    $t0, 24($sp)
        lw    $t0, -592($fp)
        lw    $t1, -588($fp)
        sw    $t0, 32($sp)
        sw    $t1, 36($sp)
        jal   __printf
        addiu $sp, $sp, 40
        # param s
        # param 2.0
        # param 97
        # param 5
        # t57 = call weigh(struct Big, double, char, long long), 4
        addiu $sp, $sp, -64
        addiu $a0, $sp, 0
        addiu $a1, $fp, -112
        li    $a2, 40
        jal   __memcpy
        l.d   $f0, fc11
        s.d   $f0, 40($sp)
        li    $t0, 97
        sw    $t0, 48($sp)
        li    $t0, 5
        li    $t1, 0
        sw    $t0, 56($sp)
        sw    $t1, 60($sp)
        jal   _Z5weigh3Bigdcx
        addiu $sp, $sp, 64
        s.d   $f0, -600($fp)
        # param "%.1f\n"
        # param t57
        # call printf, 2
        addiu $sp, $sp, -16
        la    $t0, str18
        sw    $t0, 0($sp)
        l.d   $f0, -600($fp)
        s.d   $f0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 3
        # param 1.0
        # param 2.5
        # param 4.0
        # param 77
        # param "tail"
        # t58 = call average(int, ...), 6
        addiu $sp, $sp, -48
        li    $t0, 3
        sw    $t0, 0($sp)
        l.d   $f0, fc12
        s.d   $f0, 8($sp)
        l.d   $f0, fc3
        s.d   $f0, 16($sp)
        l.d   $f0, fc13
        s.d   $f0, 24($sp)
        li    $t0, 77
        li    $t1, 0
        sw    $t0, 32($sp)
        sw    $t1, 36($sp)
        la    $t0, str20
        sw    $t0, 40($sp)
        jal   _Z7averageiz
        addiu $sp, $sp, 48
        s.d   $f0, -608($fp)
        # param "%.2f\n"
        # param t58
        # call printf, 2
        addiu $sp, $sp, -16
        la    $t0, str19
        sw    $t0, 0($sp)
        l.d   $f0, -608($fp)
        s.d   $f0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t59 = 3 uint* 4
        li    $t0, 3
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -612($fp)
        # param t59
        # t60 = call malloc, 1
        addiu $sp, $sp, -8
        lw    $t0, -612($fp)
        sw    $t0, 0($sp)
        jal   __malloc
        addiu $sp, $sp, 8
        sw    $v0, -616($fp)
        # p = t60
        lw    $t0, -616($fp)
        sw    $t0, -156($fp)
        # *p = 1
        lw    $t8, -156($fp)
        li    $t0, 1
        sw    $t0, 0($t8)
        # t61 = p ptr+ 4
        lw    $t0, -156($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -620($fp)
        # *t61 = 2
        lw    $t8, -620($fp)
        li    $t0, 2
        sw    $t0, 0($t8)
        # t62 = p ptr+ 8
        lw    $t0, -156($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -624($fp)
        # *t62 = 3
        lw    $t8, -624($fp)
        li    $t0, 3
        sw    $t0, 0($t8)
        # t63 = 6 uint* 4
        li    $t0, 6
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -628($fp)
        # param p
        # param t63
        # t64 = call realloc, 2
        addiu $sp, $sp, -8
        lw    $t0, -156($fp)
        sw    $t0, 0($sp)
        lw    $t0, -628($fp)
        sw    $t0, 4($sp)
        jal   __realloc
        addiu $sp, $sp, 8
        sw    $v0, -632($fp)
        # p = t64
        lw    $t0, -632($fp)
        sw    $t0, -156($fp)
        # param 4
        # param 4
        # t65 = call calloc, 2
        addiu $sp, $sp, -8
        li    $t0, 4
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        jal   __calloc
        addiu $sp, $sp, 8
        sw    $v0, -636($fp)
        # z = t65
        lw    $t0, -636($fp)
        sw    $t0, -160($fp)
        # t66 = *p
        lw    $t8, -156($fp)
        lw    $t0, 0($t8)
        sw    $t0, -640($fp)
        # t67 = p ptr+ 4
        lw    $t0, -156($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -644($fp)
        # t68 = *t67
        lw    $t8, -644($fp)
        lw    $t0, 0($t8)
        sw    $t0, -648($fp)
        # t69 = t66 int+ t68
        lw    $t0, -640($fp)
        lw    $t1, -648($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -652($fp)
        # t70 = p ptr+ 8
        lw    $t0, -156($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -656($fp)
        # t71 = *t70
        lw    $t8, -656($fp)
        lw    $t0, 0($t8)
        sw    $t0, -660($fp)
        # t72 = t69 int+ t71
        lw    $t0, -652($fp)
        lw    $t1, -660($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -664($fp)
        # t73 = *z
        lw    $t8, -160($fp)
        lw    $t0, 0($t8)
        sw    $t0, -668($fp)
        # t74 = z ptr+ 12
        lw    $t0, -160($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -672($fp)
        # t75 = *t74
        lw    $t8, -672($fp)
        lw    $t0, 0($t8)
        sw    $t0, -676($fp)
        # if p ptr!= z goto 233
        lw    $t0, -156($fp)
        lw    $t1, -160($fp)
        bne   $t0, $t1, L4_233
        # t76 = 0
        li    $t0, 0
        sw    $t0, -680($fp)
        # goto 234
        j     L4_234
L4_233:
        # t76 = 1
        li    $t0, 1
        sw    $t0, -680($fp)
L4_234:
        # param "%d %d %d %d\n"
        # param t72
        # param t73
        # param t75
        # param t76
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str5
        sw    $t0, 0($sp)
        lw    $t0, -664($fp)
        sw    $t0, 4($sp)
        lw    $t0, -668($fp)
        sw    $t0, 8($sp)
        lw    $t0, -676($fp)
        sw    $t0, 12($sp)
        lw    $t0, -680($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t77 = a llong% 100
        lw    $a0, -8($fp)
        lw    $a1, -4($fp)
        li    $a2, 100
        li    $a3, 0
        jal   __modll
        sw    $v0, -688($fp)
        sw    $v1, -684($fp)
        # t78 = llongtoint t77
        lw    $t0, -688($fp)
        lw    $t1, -684($fp)
        sw    $t0, -692($fp)
        # return t78
        lw    $v0, -692($fp)
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
