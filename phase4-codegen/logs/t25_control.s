# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t25_control.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 65, 0
str1:
        .byte 66, 0
str2:
        .byte 67, 0
str3:
        .byte 70, 0
str4:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str5:
        .byte 49, 50, 51, 52, 0
str6:
        .byte 49, 50, 46, 53, 0
str7:
        .byte 120, 95, 57, 0
str8:
        .byte 57, 120, 0
str9:
        .byte 0
str10:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str11:
        .byte 37, 115, 32, 37, 115, 32, 37, 115, 32, 37, 115, 10, 0
str12:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str13:
        .byte 37, 100, 32, 37, 100, 10, 0
str14:
        .byte 37, 100, 32, 0
str15:
        .byte 10, 37, 100, 10, 0

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

# classify(const char *)
_Z8classifyPKc:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        # state = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L0_1:
        # t1 = *s
        lw    $t8, 8($fp)
        lb    $t0, 0($t8)
        sb    $t0, -17($fp)
        # if t1 char!= 0 goto 4
        lb    $t0, -17($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_4
        # goto 68
        j     L0_68
L0_4:
        # t2 = *s
        lw    $t8, 8($fp)
        lb    $t0, 0($t8)
        sb    $t0, -18($fp)
        # c = t2
        lb    $t0, -18($fp)
        sb    $t0, -5($fp)
        # t4 = chartoint c
        lb    $t0, -5($fp)
        sw    $t0, -28($fp)
        # if t4 int>= 48 goto 9
        lw    $t0, -28($fp)
        li    $t1, 48
        bge   $t0, $t1, L0_9
        # goto 12
        j     L0_12
L0_9:
        # t5 = chartoint c
        lb    $t0, -5($fp)
        sw    $t0, -32($fp)
        # if t5 int<= 57 goto 14
        lw    $t0, -32($fp)
        li    $t1, 57
        ble   $t0, $t1, L0_14
        # goto 12
        j     L0_12
L0_12:
        # t3 = 0
        li    $t0, 0
        sw    $t0, -24($fp)
        # goto 15
        j     L0_15
L0_14:
        # t3 = 1
        li    $t0, 1
        sw    $t0, -24($fp)
L0_15:
        # digit = t3
        lw    $t0, -24($fp)
        sw    $t0, -12($fp)
        # t7 = chartoint c
        lb    $t0, -5($fp)
        sw    $t0, -40($fp)
        # if t7 int>= 97 goto 19
        lw    $t0, -40($fp)
        li    $t1, 97
        bge   $t0, $t1, L0_19
        # goto 22
        j     L0_22
L0_19:
        # t8 = chartoint c
        lb    $t0, -5($fp)
        sw    $t0, -44($fp)
        # if t8 int<= 122 goto 27
        lw    $t0, -44($fp)
        li    $t1, 122
        ble   $t0, $t1, L0_27
        # goto 22
        j     L0_22
L0_22:
        # t9 = chartoint c
        lb    $t0, -5($fp)
        sw    $t0, -48($fp)
        # if t9 int== 95 goto 27
        lw    $t0, -48($fp)
        li    $t1, 95
        beq   $t0, $t1, L0_27
        # goto 25
        j     L0_25
L0_25:
        # t6 = 0
        li    $t0, 0
        sw    $t0, -36($fp)
        # goto 28
        j     L0_28
L0_27:
        # t6 = 1
        li    $t0, 1
        sw    $t0, -36($fp)
L0_28:
        # letter = t6
        lw    $t0, -36($fp)
        sw    $t0, -16($fp)
        # t10 = state
        lw    $t0, -4($fp)
        sw    $t0, -52($fp)
        # goto 61
        j     L0_61
L0_31:
        # if digit int!= 0 goto 33
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_33
        # goto 35
        j     L0_35
L0_33:
        # state = 1
        li    $t0, 1
        sw    $t0, -4($fp)
        # goto 40
        j     L0_40
L0_35:
        # if letter int!= 0 goto 37
        lw    $t0, -16($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_37
        # goto 39
        j     L0_39
L0_37:
        # state = 3
        li    $t0, 3
        sw    $t0, -4($fp)
        # goto 40
        j     L0_40
L0_39:
        # return 0
        li    $v0, 0
        j     _Z8classifyPKc_exit
L0_40:
        # goto 65
        j     L0_65
L0_41:
        # t11 = chartoint c
        lb    $t0, -5($fp)
        sw    $t0, -56($fp)
        # if t11 int== 46 goto 44
        lw    $t0, -56($fp)
        li    $t1, 46
        beq   $t0, $t1, L0_44
        # goto 46
        j     L0_46
L0_44:
        # state = 2
        li    $t0, 2
        sw    $t0, -4($fp)
        # goto 49
        j     L0_49
L0_46:
        # if digit int!= 0 goto 49
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_49
        # goto 48
        j     L0_48
L0_48:
        # return 0
        li    $v0, 0
        j     _Z8classifyPKc_exit
L0_49:
        # goto 65
        j     L0_65
L0_50:
        # if digit int!= 0 goto 53
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_53
        # goto 52
        j     L0_52
L0_52:
        # return 0
        li    $v0, 0
        j     _Z8classifyPKc_exit
L0_53:
        # goto 65
        j     L0_65
L0_54:
        # if digit int!= 0 goto 59
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_59
        # goto 56
        j     L0_56
L0_56:
        # if letter int!= 0 goto 59
        lw    $t0, -16($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_59
        # goto 58
        j     L0_58
L0_58:
        # return 0
        li    $v0, 0
        j     _Z8classifyPKc_exit
L0_59:
        # goto 65
        j     L0_65
        # goto 65
        j     L0_65
L0_61:
        # if t10 int== 0 goto 31
        lw    $t0, -52($fp)
        li    $t1, 0
        beq   $t0, $t1, L0_31
        # if t10 int== 1 goto 41
        lw    $t0, -52($fp)
        li    $t1, 1
        beq   $t0, $t1, L0_41
        # if t10 int== 2 goto 50
        lw    $t0, -52($fp)
        li    $t1, 2
        beq   $t0, $t1, L0_50
        # if t10 int== 3 goto 54
        lw    $t0, -52($fp)
        li    $t1, 3
        beq   $t0, $t1, L0_54
L0_65:
        # t12 = s ptr+ 1
        lw    $t0, 8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # s = t12
        lw    $t0, -60($fp)
        sw    $t0, 8($fp)
        # goto 1
        j     L0_1
L0_68:
        # return state
        lw    $v0, -4($fp)
        j     _Z8classifyPKc_exit
_Z8classifyPKc_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# daysIn(int, int)
_Z6daysInii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t1 = month
        lw    $t0, 8($fp)
        sw    $t0, -4($fp)
        # goto 18
        j     L1_18
L1_2:
        # return 30
        li    $v0, 30
        j     _Z6daysInii_exit
L1_3:
        # t3 = year int% 4
        lw    $t0, 12($fp)
        li    $t1, 4
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -12($fp)
        # if t3 int== 0 goto 6
        lw    $t0, -12($fp)
        li    $t1, 0
        beq   $t0, $t1, L1_6
        # goto 9
        j     L1_9
L1_6:
        # t4 = year int% 100
        lw    $t0, 12($fp)
        li    $t1, 100
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -16($fp)
        # if t4 int!= 0 goto 12
        lw    $t0, -16($fp)
        li    $t1, 0
        bne   $t0, $t1, L1_12
        # goto 9
        j     L1_9
L1_9:
        # t5 = year int% 400
        lw    $t0, 12($fp)
        li    $t1, 400
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -20($fp)
        # if t5 int== 0 goto 12
        lw    $t0, -20($fp)
        li    $t1, 0
        beq   $t0, $t1, L1_12
        # goto 14
        j     L1_14
L1_12:
        # t2 = 29
        li    $t0, 29
        sw    $t0, -8($fp)
        # goto 15
        j     L1_15
L1_14:
        # t2 = 28
        li    $t0, 28
        sw    $t0, -8($fp)
L1_15:
        # return t2
        lw    $v0, -8($fp)
        j     _Z6daysInii_exit
L1_16:
        # return 31
        li    $v0, 31
        j     _Z6daysInii_exit
        # goto 24
        j     L1_24
L1_18:
        # if t1 int== 4 goto 2
        lw    $t0, -4($fp)
        li    $t1, 4
        beq   $t0, $t1, L1_2
        # if t1 int== 6 goto 2
        lw    $t0, -4($fp)
        li    $t1, 6
        beq   $t0, $t1, L1_2
        # if t1 int== 9 goto 2
        lw    $t0, -4($fp)
        li    $t1, 9
        beq   $t0, $t1, L1_2
        # if t1 int== 11 goto 2
        lw    $t0, -4($fp)
        li    $t1, 11
        beq   $t0, $t1, L1_2
        # if t1 int== 2 goto 3
        lw    $t0, -4($fp)
        li    $t1, 2
        beq   $t0, $t1, L1_3
        # goto 16
        j     L1_16
L1_24:
        # return
        j     _Z6daysInii_exit
_Z6daysInii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# grade(int)
_Z5gradei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if score int>= 90 goto 2
        lw    $t0, 8($fp)
        li    $t1, 90
        bge   $t0, $t1, L2_2
        # goto 4
        j     L2_4
L2_2:
        # t1 = "A"
        la    $t0, str0
        sw    $t0, -4($fp)
        # goto 15
        j     L2_15
L2_4:
        # if score int>= 75 goto 6
        lw    $t0, 8($fp)
        li    $t1, 75
        bge   $t0, $t1, L2_6
        # goto 8
        j     L2_8
L2_6:
        # t2 = "B"
        la    $t0, str1
        sw    $t0, -8($fp)
        # goto 14
        j     L2_14
L2_8:
        # if score int>= 60 goto 10
        lw    $t0, 8($fp)
        li    $t1, 60
        bge   $t0, $t1, L2_10
        # goto 12
        j     L2_12
L2_10:
        # t3 = "C"
        la    $t0, str2
        sw    $t0, -12($fp)
        # goto 13
        j     L2_13
L2_12:
        # t3 = "F"
        la    $t0, str3
        sw    $t0, -12($fp)
L2_13:
        # t2 = t3
        lw    $t0, -12($fp)
        sw    $t0, -8($fp)
L2_14:
        # t1 = t2
        lw    $t0, -8($fp)
        sw    $t0, -4($fp)
L2_15:
        # return t1
        lw    $v0, -4($fp)
        j     _Z5gradei_exit
_Z5gradei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# firstPair(int)
_Z9firstPairi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # i = 1
        li    $t0, 1
        sw    $t0, -4($fp)
L3_1:
        # if i int< 10 goto 3
        lw    $t0, -4($fp)
        li    $t1, 10
        blt   $t0, $t1, L3_3
        # goto 16
        j     L3_16
L3_3:
        # j = i
        lw    $t0, -4($fp)
        sw    $t0, -8($fp)
L3_4:
        # if j int< 10 goto 6
        lw    $t0, -8($fp)
        li    $t1, 10
        blt   $t0, $t1, L3_6
        # goto 13
        j     L3_13
L3_6:
        # t1 = i int* j
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # if t1 int== target goto 9
        lw    $t0, -12($fp)
        lw    $t1, 8($fp)
        beq   $t0, $t1, L3_9
        # goto 10
        j     L3_10
L3_9:
        # goto 18
        j     L3_18
L3_10:
        # t2 = j int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # j = t2
        lw    $t0, -16($fp)
        sw    $t0, -8($fp)
        # goto 4
        j     L3_4
L3_13:
        # t3 = i int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # i = t3
        lw    $t0, -20($fp)
        sw    $t0, -4($fp)
        # goto 1
        j     L3_1
L3_16:
        # t4 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -24($fp)
        # return t4
        lw    $v0, -24($fp)
        j     _Z9firstPairi_exit
L3_18:
        # t5 = i int* 10
        lw    $t0, -4($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -28($fp)
        # t6 = t5 int+ j
        lw    $t0, -28($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # return t6
        lw    $v0, -32($fp)
        j     _Z9firstPairi_exit
_Z9firstPairi_exit:
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
        addiu $sp, $sp, -216
        # param "1234"
        # t1 = call classify(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   _Z8classifyPKc
        addiu $sp, $sp, 8
        sw    $v0, -56($fp)
        # param "12.5"
        # t2 = call classify(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        jal   _Z8classifyPKc
        addiu $sp, $sp, 8
        sw    $v0, -60($fp)
        # param "x_9"
        # t3 = call classify(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str7
        sw    $t0, 0($sp)
        jal   _Z8classifyPKc
        addiu $sp, $sp, 8
        sw    $v0, -64($fp)
        # param "9x"
        # t4 = call classify(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   _Z8classifyPKc
        addiu $sp, $sp, 8
        sw    $v0, -68($fp)
        # param ""
        # t5 = call classify(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str9
        sw    $t0, 0($sp)
        jal   _Z8classifyPKc
        addiu $sp, $sp, 8
        sw    $v0, -72($fp)
        # param "%d %d %d %d %d\n"
        # param t1
        # param t2
        # param t3
        # param t4
        # param t5
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -56($fp)
        sw    $t0, 4($sp)
        lw    $t0, -60($fp)
        sw    $t0, 8($sp)
        lw    $t0, -64($fp)
        sw    $t0, 12($sp)
        lw    $t0, -68($fp)
        sw    $t0, 16($sp)
        lw    $t0, -72($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 2
        # param 2024
        # t6 = call daysIn(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        li    $t0, 2024
        sw    $t0, 4($sp)
        jal   _Z6daysInii
        addiu $sp, $sp, 8
        sw    $v0, -76($fp)
        # param 2
        # param 1900
        # t7 = call daysIn(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        li    $t0, 1900
        sw    $t0, 4($sp)
        jal   _Z6daysInii
        addiu $sp, $sp, 8
        sw    $v0, -80($fp)
        # param 2
        # param 2000
        # t8 = call daysIn(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        li    $t0, 2000
        sw    $t0, 4($sp)
        jal   _Z6daysInii
        addiu $sp, $sp, 8
        sw    $v0, -84($fp)
        # param 11
        # param 2023
        # t9 = call daysIn(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 11
        sw    $t0, 0($sp)
        li    $t0, 2023
        sw    $t0, 4($sp)
        jal   _Z6daysInii
        addiu $sp, $sp, 8
        sw    $v0, -88($fp)
        # param "%d %d %d %d\n"
        # param t6
        # param t7
        # param t8
        # param t9
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str10
        sw    $t0, 0($sp)
        lw    $t0, -76($fp)
        sw    $t0, 4($sp)
        lw    $t0, -80($fp)
        sw    $t0, 8($sp)
        lw    $t0, -84($fp)
        sw    $t0, 12($sp)
        lw    $t0, -88($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 95
        # t10 = call grade(int), 1
        addiu $sp, $sp, -8
        li    $t0, 95
        sw    $t0, 0($sp)
        jal   _Z5gradei
        addiu $sp, $sp, 8
        sw    $v0, -92($fp)
        # param 80
        # t11 = call grade(int), 1
        addiu $sp, $sp, -8
        li    $t0, 80
        sw    $t0, 0($sp)
        jal   _Z5gradei
        addiu $sp, $sp, 8
        sw    $v0, -96($fp)
        # param 60
        # t12 = call grade(int), 1
        addiu $sp, $sp, -8
        li    $t0, 60
        sw    $t0, 0($sp)
        jal   _Z5gradei
        addiu $sp, $sp, 8
        sw    $v0, -100($fp)
        # param 10
        # t13 = call grade(int), 1
        addiu $sp, $sp, -8
        li    $t0, 10
        sw    $t0, 0($sp)
        jal   _Z5gradei
        addiu $sp, $sp, 8
        sw    $v0, -104($fp)
        # param "%s %s %s %s\n"
        # param t10
        # param t11
        # param t12
        # param t13
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str11
        sw    $t0, 0($sp)
        lw    $t0, -92($fp)
        sw    $t0, 4($sp)
        lw    $t0, -96($fp)
        sw    $t0, 8($sp)
        lw    $t0, -100($fp)
        sw    $t0, 12($sp)
        lw    $t0, -104($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 24
        # t14 = call firstPair(int), 1
        addiu $sp, $sp, -8
        li    $t0, 24
        sw    $t0, 0($sp)
        jal   _Z9firstPairi
        addiu $sp, $sp, 8
        sw    $v0, -108($fp)
        # param 49
        # t15 = call firstPair(int), 1
        addiu $sp, $sp, -8
        li    $t0, 49
        sw    $t0, 0($sp)
        jal   _Z9firstPairi
        addiu $sp, $sp, 8
        sw    $v0, -112($fp)
        # param 97
        # t16 = call firstPair(int), 1
        addiu $sp, $sp, -8
        li    $t0, 97
        sw    $t0, 0($sp)
        jal   _Z9firstPairi
        addiu $sp, $sp, 8
        sw    $v0, -116($fp)
        # param "%d %d %d\n"
        # param t14
        # param t15
        # param t16
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str12
        sw    $t0, 0($sp)
        lw    $t0, -108($fp)
        sw    $t0, 4($sp)
        lw    $t0, -112($fp)
        sw    $t0, 8($sp)
        lw    $t0, -116($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # triangle = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # skipped = 0
        li    $t0, 0
        sw    $t0, -8($fp)
        # i = 1
        li    $t0, 1
        sw    $t0, -12($fp)
L4_63:
        # if i int<= 6 goto 65
        lw    $t0, -12($fp)
        li    $t1, 6
        ble   $t0, $t1, L4_65
        # goto 90
        j     L4_90
L4_65:
        # if i int== 4 goto 67
        lw    $t0, -12($fp)
        li    $t1, 4
        beq   $t0, $t1, L4_67
        # goto 70
        j     L4_70
L4_67:
        # t17 = skipped int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -120($fp)
        # skipped = t17
        lw    $t0, -120($fp)
        sw    $t0, -8($fp)
        # goto 87
        j     L4_87
L4_70:
        # j = 1
        li    $t0, 1
        sw    $t0, -16($fp)
L4_71:
        # if j int<= 6 goto 73
        lw    $t0, -16($fp)
        li    $t1, 6
        ble   $t0, $t1, L4_73
        # goto 87
        j     L4_87
L4_73:
        # if j int> i goto 75
        lw    $t0, -16($fp)
        lw    $t1, -12($fp)
        bgt   $t0, $t1, L4_75
        # goto 76
        j     L4_76
L4_75:
        # goto 87
        j     L4_87
L4_76:
        # t18 = i int+ j
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -124($fp)
        # t19 = t18 int% 2
        lw    $t0, -124($fp)
        li    $t1, 2
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -128($fp)
        # if t19 int!= 0 goto 80
        lw    $t0, -128($fp)
        li    $t1, 0
        bne   $t0, $t1, L4_80
        # goto 81
        j     L4_81
L4_80:
        # goto 84
        j     L4_84
L4_81:
        # t20 = i int* j
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -132($fp)
        # t21 = triangle int+ t20
        lw    $t0, -4($fp)
        lw    $t1, -132($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -136($fp)
        # triangle = t21
        lw    $t0, -136($fp)
        sw    $t0, -4($fp)
L4_84:
        # t22 = j int+ 1
        lw    $t0, -16($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -140($fp)
        # j = t22
        lw    $t0, -140($fp)
        sw    $t0, -16($fp)
        # goto 71
        j     L4_71
L4_87:
        # t23 = i int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -144($fp)
        # i = t23
        lw    $t0, -144($fp)
        sw    $t0, -12($fp)
        # goto 63
        j     L4_63
L4_90:
        # param "%d %d\n"
        # param triangle
        # param skipped
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str13
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        lw    $t0, -8($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # n = 0
        li    $t0, 0
        sw    $t0, -20($fp)
        # digits = 0
        li    $t0, 0
        sw    $t0, -24($fp)
        # value = 90210
        li    $t0, 90210
        sw    $t0, -28($fp)
L4_97:
        # t24 = digits int+ 1
        lw    $t0, -24($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -148($fp)
        # digits = t24
        lw    $t0, -148($fp)
        sw    $t0, -24($fp)
        # t25 = value int/ 10
        lw    $t0, -28($fp)
        li    $t1, 10
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -152($fp)
        # value = t25
        lw    $t0, -152($fp)
        sw    $t0, -28($fp)
        # if value int!= 0 goto 97
        lw    $t0, -28($fp)
        li    $t1, 0
        bne   $t0, $t1, L4_97
        # goto 103
        j     L4_103
L4_103:
        # t26 = n int* n
        lw    $t0, -20($fp)
        lw    $t1, -20($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -156($fp)
        # if t26 int> 200 goto 109
        lw    $t0, -156($fp)
        li    $t1, 200
        bgt   $t0, $t1, L4_109
        # goto 106
        j     L4_106
L4_106:
        # t27 = n int+ 1
        lw    $t0, -20($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -160($fp)
        # n = t27
        lw    $t0, -160($fp)
        sw    $t0, -20($fp)
        # goto 103
        j     L4_103
L4_109:
        # a = 0
        li    $t0, 0
        sw    $t0, -32($fp)
        # b = 10
        li    $t0, 10
        sw    $t0, -36($fp)
L4_111:
        # if a int< b goto 113
        lw    $t0, -32($fp)
        lw    $t1, -36($fp)
        blt   $t0, $t1, L4_113
        # goto 118
        j     L4_118
L4_113:
        # t28 = a int+ 1
        lw    $t0, -32($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -164($fp)
        # a = t28
        lw    $t0, -164($fp)
        sw    $t0, -32($fp)
        # t29 = b int- 1
        lw    $t0, -36($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -168($fp)
        # b = t29
        lw    $t0, -168($fp)
        sw    $t0, -36($fp)
        # goto 111
        j     L4_111
L4_118:
        # t30 = a int+ 1
        lw    $t0, -32($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -172($fp)
        # a = t30
        lw    $t0, -172($fp)
        sw    $t0, -32($fp)
        # t31 = b int+ 2
        lw    $t0, -36($fp)
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -176($fp)
        # b = t31
        lw    $t0, -176($fp)
        sw    $t0, -36($fp)
        # t32 = a int+ b
        lw    $t0, -32($fp)
        lw    $t1, -36($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -180($fp)
        # c = t32
        lw    $t0, -180($fp)
        sw    $t0, -40($fp)
        # param "%d %d %d %d %d\n"
        # param digits
        # param n
        # param a
        # param b
        # param c
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -24($fp)
        sw    $t0, 4($sp)
        lw    $t0, -20($fp)
        sw    $t0, 8($sp)
        lw    $t0, -32($fp)
        sw    $t0, 12($sp)
        lw    $t0, -36($fp)
        sw    $t0, 16($sp)
        lw    $t0, -40($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # steps = 0
        li    $t0, 0
        sw    $t0, -44($fp)
        # k = 27
        li    $t0, 27
        sw    $t0, -48($fp)
L4_133:
        # goto 134
        j     L4_134
L4_134:
        # if k int== 1 goto 136
        lw    $t0, -48($fp)
        li    $t1, 1
        beq   $t0, $t1, L4_136
        # goto 137
        j     L4_137
L4_136:
        # goto 153
        j     L4_153
L4_137:
        # t34 = k int% 2
        lw    $t0, -48($fp)
        li    $t1, 2
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -188($fp)
        # if t34 int!= 0 goto 140
        lw    $t0, -188($fp)
        li    $t1, 0
        bne   $t0, $t1, L4_140
        # goto 144
        j     L4_144
L4_140:
        # t35 = 3 int* k
        li    $t0, 3
        lw    $t1, -48($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -192($fp)
        # t36 = t35 int+ 1
        lw    $t0, -192($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -196($fp)
        # t33 = t36
        lw    $t0, -196($fp)
        sw    $t0, -184($fp)
        # goto 146
        j     L4_146
L4_144:
        # t37 = k int/ 2
        lw    $t0, -48($fp)
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -200($fp)
        # t33 = t37
        lw    $t0, -200($fp)
        sw    $t0, -184($fp)
L4_146:
        # k = t33
        lw    $t0, -184($fp)
        sw    $t0, -48($fp)
        # t38 = steps int+ 1
        lw    $t0, -44($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -204($fp)
        # steps = t38
        lw    $t0, -204($fp)
        sw    $t0, -44($fp)
        # if t38 int> 200 goto 151
        lw    $t0, -204($fp)
        li    $t1, 200
        bgt   $t0, $t1, L4_151
        # goto 133
        j     L4_133
L4_151:
        # goto 153
        j     L4_153
        # goto 133
        j     L4_133
L4_153:
        # countdown = 3
        li    $t0, 3
        sw    $t0, -52($fp)
L4_154:
        # t39 = countdown
        lw    $t0, -52($fp)
        sw    $t0, -208($fp)
        # t40 = countdown int- 1
        lw    $t0, -52($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -212($fp)
        # countdown = t40
        lw    $t0, -212($fp)
        sw    $t0, -52($fp)
        # if t39 int> 0 goto 159
        lw    $t0, -208($fp)
        li    $t1, 0
        bgt   $t0, $t1, L4_159
        # goto 163
        j     L4_163
L4_159:
        # param "%d "
        # param countdown
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str14
        sw    $t0, 0($sp)
        lw    $t0, -52($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # goto 154
        j     L4_154
L4_163:
        # param "\n%d\n"
        # param steps
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str15
        sw    $t0, 0($sp)
        lw    $t0, -44($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return digits
        lw    $v0, -24($fp)
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
