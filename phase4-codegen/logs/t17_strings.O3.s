# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t17_strings.c
#  Optimization : -O3 (TAC optimizations, registers, peephole)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 100, 101, 108, 116, 97, 0
str1:
        .byte 97, 108, 112, 104, 97, 0
str2:
        .byte 99, 104, 97, 114, 108, 105, 101, 0
str3:
        .byte 99, 111, 109, 112, 105, 108, 101, 114, 0
str4:
        .byte 37, 115, 32, 37, 100, 10, 0
str5:
        .byte 37, 115, 32, 37, 100, 32, 37, 100, 10, 0
str6:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str7:
        .byte 97, 98, 99, 0
str8:
        .byte 97, 98, 100, 0
str9:
        .byte 98, 0
str10:
        .byte 37, 115, 32, 37, 99, 10, 0
str11:
        .byte 55, 55, 120, 0
str12:
        .byte 108, 101, 118, 101, 108, 0
str13:
        .byte 108, 101, 118, 101, 114, 0
str14:
        .byte 32, 32, 116, 104, 101, 32, 113, 117, 105, 99, 107, 32, 32, 98, 114, 111
        .byte 119, 110, 32, 102, 111, 120, 32, 0

        .text
        .globl main
main:
        li    $t0, -8
        and   $sp, $sp, $t0           # frames assume an 8-byte aligned stack
        li    $t1, 0x7ffc4000
        sw    $t1, __stack_limit      # deeper than this is a stack overflow
        addiu $sp, $sp, -8
        sw    $a0, 0($sp)             # argc
        sw    $a1, 4($sp)             # argv
        jal   main_
        move  $a0, $v0
        li    $v0, 17                 # exit with main's result
        syscall

# length(const char *)
_Z6lengthPKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -20($fp)
        sw    $s1, -4($fp)
        sw    $s2, -8($fp)
        sw    $s3, -12($fp)
        sw    $s4, -16($fp)
        move  $s4, $a0
        # n = 0
        li    $s0, 0
L0_1:
        # t1 = s ptr+ n
        addu  $s1, $s4, $s0
        # t2 = *t1
        lb    $s2, 0($s1)
        # t3 = chartoint t2
        move  $t0, $s2
        move  $s3, $t0
        # if t3 int== 0 goto 12
        beq   $s3, $zero, L0_12
        # n = n int+ 1
        addiu $s0, $s0, 1
        # t1 = s ptr+ n
        addu  $s1, $s4, $s0
        # t2 = *t1
        lb    $s2, 0($s1)
        # t3 = chartoint t2
        move  $t0, $s2
        move  $s3, $t0
        # if t3 int== 0 goto 12
        beq   $s3, $zero, L0_12
        # n = n int+ 1
        addiu $s0, $s0, 1
        # goto 1
        j     L0_1
L0_12:
        # return n
        move  $v0, $s0
        j     _Z6lengthPKc_exit
_Z6lengthPKc_exit:
        lw    $s0, -20($fp)
        lw    $s1, -4($fp)
        lw    $s2, -8($fp)
        lw    $s3, -12($fp)
        lw    $s4, -16($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# toNumber(const char *)
_Z8toNumberPKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -40($fp)
        sw    $s1, -44($fp)
        sw    $s2, -16($fp)
        sw    $s3, -20($fp)
        sw    $s4, -24($fp)
        sw    $s5, -28($fp)
        sw    $s6, -32($fp)
        sw    $s7, -36($fp)
        move  $s0, $a0
        # sign = 1
        li    $t0, 1
        sw    $t0, -4($fp)
        # v = 0
        li    $s1, 0
        # t1 = *s
        lb    $s2, 0($s0)
        # t2 = chartoint t1
        move  $t0, $s2
        move  $s3, $t0
        # if t2 int!= 45 goto 7
        li    $t1, 45
        bne   $s3, $t1, L1_7
        # sign = -1
        li    $t0, -1
        sw    $t0, -4($fp)
        # s = s ptr+ 1
        addiu $s0, $s0, 1
L1_7:
        # t5 = *s
        lb    $s2, 0($s0)
        # t6 = chartoint t5
        move  $t0, $s2
        move  $s3, $t0
        # if t6 int< 48 goto 32
        li    $t1, 48
        blt   $s3, $t1, L1_32
        # t7 = *s
        lb    $s4, 0($s0)
        # t8 = chartoint t7
        move  $t0, $s4
        move  $s5, $t0
        # if t8 int> 57 goto 32
        li    $t1, 57
        bgt   $s5, $t1, L1_32
        # t9 = v int* 10
        li    $t1, 10
        mul   $s6, $s1, $t1
        # t10 = *s
        lb    $s7, 0($s0)
        # t11 = chartoint t10
        move  $t0, $s7
        sw    $t0, -8($fp)
        # t12 = t11 int- 48
        addiu $t0, $t0, -48
        sw    $t0, -12($fp)
        # v = t9 int+ t12
        move  $t1, $t0
        addu  $s1, $s6, $t1
        # s = s ptr+ 1
        addiu $s0, $s0, 1
        # t5 = *s
        lb    $s2, 0($s0)
        # t6 = chartoint t5
        move  $t0, $s2
        move  $s3, $t0
        # if t6 int< 48 goto 32
        li    $t1, 48
        blt   $s3, $t1, L1_32
        # t7 = *s
        lb    $s4, 0($s0)
        # t8 = chartoint t7
        move  $t0, $s4
        move  $s5, $t0
        # if t8 int> 57 goto 32
        li    $t1, 57
        bgt   $s5, $t1, L1_32
        # t9 = v int* 10
        li    $t1, 10
        mul   $s6, $s1, $t1
        # t10 = *s
        lb    $s7, 0($s0)
        # t11 = chartoint t10
        move  $t0, $s7
        sw    $t0, -8($fp)
        # t12 = t11 int- 48
        addiu $t0, $t0, -48
        sw    $t0, -12($fp)
        # v = t9 int+ t12
        move  $t1, $t0
        addu  $s1, $s6, $t1
        # s = s ptr+ 1
        addiu $s0, $s0, 1
        # goto 7
        j     L1_7
L1_32:
        # t15 = sign int* v
        lw    $t0, -4($fp)
        mul   $s0, $t0, $s1
        # return t15
        move  $v0, $s0
        j     _Z8toNumberPKc_exit
_Z8toNumberPKc_exit:
        lw    $s0, -40($fp)
        lw    $s1, -44($fp)
        lw    $s2, -16($fp)
        lw    $s3, -20($fp)
        lw    $s4, -24($fp)
        lw    $s5, -28($fp)
        lw    $s6, -32($fp)
        lw    $s7, -36($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# toText(int, char *)
_Z6toTextiPc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -48($fp)
        sw    $s1, -40($fp)
        sw    $s2, -44($fp)
        sw    $s3, -36($fp)
        sw    $s4, -20($fp)
        sw    $s5, -24($fp)
        sw    $s6, -28($fp)
        sw    $s7, -32($fp)
        move  $s1, $a0
        move  $s2, $a1
        # n = 0
        li    $s0, 0
        # if v int< 0 goto 4
        slt   $t0, $s1, $zero
        sw    $t0, -16($fp)
L2_5:
        # if t1 int== 0 goto 7
        lw    $t0, -16($fp)
        beq   $t0, $zero, L2_7
        # v = int- v
        negu  $s1, $s1
L2_7:
        # t3 = n
        move  $s4, $s0
        # n = n int+ 1
        addiu $s0, $s0, 1
        # t5 = v int% 10
        li    $t1, 10
        div   $s1, $t1
        mfhi  $s5
        # t6 = 48 int+ t5
        li    $t0, 48
        addu  $s6, $t0, $s5
        # t7 = inttochar t6
        move  $t0, $s6
        move  $s7, $t0
        sll   $s7, $s7, 24
        sra   $s7, $s7, 24
        # tmp[t3] = t7
        addiu $t8, $fp, -12
        addu  $t8, $t8, $s4
        sb    $s7, 0($t8)
        # t8 = v int/ 10
        li    $t1, 10
        div   $s1, $t1
        mflo  $s3
        # v = t8
        move  $s1, $s3
        # if t8 int> 0 goto 7
        bgt   $s3, $zero, L2_7
        # if t1 int== 0 goto 20
        lw    $t0, -16($fp)
        beq   $t0, $zero, L2_20
        # t9 = n
        move  $s1, $s0
        # n = n int+ 1
        addiu $s0, $s0, 1
        # tmp[t9] = 45
        addiu $t8, $fp, -12
        addu  $t8, $t8, $s1
        li    $t0, 45
        sb    $t0, 0($t8)
L2_20:
        # if n int<= 0 goto 35
        ble   $s0, $zero, L2_35
        # t11 = out
        move  $s3, $s2
        # out = out ptr+ 1
        addiu $s2, $s2, 1
        # t13 = n int- 1
        addiu $s1, $s0, -1
        # n = t13
        move  $s0, $s1
        # t14 = tmp[t13]
        addiu $t8, $fp, -12
        addu  $t8, $t8, $s1
        lb    $s4, 0($t8)
        # *t11 = t14
        sb    $s4, 0($s3)
        # if t13 int<= 0 goto 35
        ble   $s1, $zero, L2_35
        # t11 = out
        move  $s3, $s2
        # out = out ptr+ 1
        addiu $s2, $s2, 1
        # t13 = n int- 1
        addiu $s1, $s0, -1
        # n = t13
        move  $s0, $s1
        # t14 = tmp[t13]
        addiu $t8, $fp, -12
        addu  $t8, $t8, $s1
        lb    $s4, 0($t8)
        # *t11 = t14
        sb    $s4, 0($s3)
        # goto 20
        j     L2_20
L2_35:
        # *out = 0
        sb    $zero, 0($s2)
        # return
        j     _Z6toTextiPc_exit
_Z6toTextiPc_exit:
        lw    $s0, -48($fp)
        lw    $s1, -40($fp)
        lw    $s2, -44($fp)
        lw    $s3, -36($fp)
        lw    $s4, -20($fp)
        lw    $s5, -24($fp)
        lw    $s6, -28($fp)
        lw    $s7, -32($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# isPalindrome(const char *)
_Z12isPalindromePKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -16($fp)
        sw    $s1, -44($fp)
        sw    $s2, -36($fp)
        sw    $s3, -20($fp)
        sw    $s4, -24($fp)
        sw    $s5, -40($fp)
        sw    $s6, -28($fp)
        sw    $s7, -32($fp)
        move  $s5, $a0
        # i = 0
        li    $s1, 0
        # t14 = 0
        li    $s0, 0
L3_2:
        # t15 = s ptr+ t14
        addu  $s2, $s5, $s0
        # t16 = *t15
        lb    $s3, 0($s2)
        # t17 = chartoint t16
        move  $t0, $s3
        move  $s4, $t0
        # if t17 int== 0 goto 13
        beq   $s4, $zero, L3_13
        # t14 = t14 int+ 1
        addiu $s0, $s0, 1
        # t15 = s ptr+ t14
        addu  $s2, $s5, $s0
        # t16 = *t15
        lb    $s3, 0($s2)
        # t17 = chartoint t16
        move  $t0, $s3
        move  $s4, $t0
        # if t17 int== 0 goto 13
        beq   $s4, $zero, L3_13
        # t14 = t14 int+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L3_2
L3_13:
        # j = t14 int- 1
        addiu $s2, $s0, -1
L3_14:
        # if i int>= j goto 27
        bge   $s1, $s2, L3_27
        # t3 = i
        move  $s0, $s1
        # i = i int+ 1
        addiu $s1, $s1, 1
        # t5 = s ptr+ t3
        addu  $s3, $s5, $s0
        # t6 = *t5
        lb    $s4, 0($s3)
        # t7 = chartoint t6
        move  $t0, $s4
        move  $s6, $t0
        # t8 = j
        move  $s7, $s2
        # j = j int- 1
        addiu $s2, $s2, -1
        # t10 = s ptr+ t8
        addu  $t0, $s5, $s7
        sw    $t0, -4($fp)
        # t11 = *t10
        move  $t8, $t0
        lb    $t0, 0($t8)
        sb    $t0, -5($fp)
        # t12 = chartoint t11
        lb    $t0, -5($fp)
        sw    $t0, -12($fp)
        # if t7 int== t12 goto 14
        move  $t1, $t0
        beq   $s6, $t1, L3_14
        # return 0
        li    $v0, 0
        j     _Z12isPalindromePKc_exit
L3_27:
        # return 1
        li    $v0, 1
        j     _Z12isPalindromePKc_exit
_Z12isPalindromePKc_exit:
        lw    $s0, -16($fp)
        lw    $s1, -44($fp)
        lw    $s2, -36($fp)
        lw    $s3, -20($fp)
        lw    $s4, -24($fp)
        lw    $s5, -40($fp)
        lw    $s6, -28($fp)
        lw    $s7, -32($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# countWords(const char *)
_Z10countWordsPKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        sw    $s0, -24($fp)
        sw    $s1, -32($fp)
        sw    $s2, -28($fp)
        sw    $s3, -4($fp)
        sw    $s4, -8($fp)
        sw    $s5, -12($fp)
        sw    $s6, -16($fp)
        sw    $s7, -20($fp)
        move  $s0, $a0
        # words = 0
        li    $s2, 0
        # inside = 0
        li    $s1, 0
L4_2:
        # t1 = *s
        lb    $s3, 0($s0)
        # if t1 char== 0 goto 31
        beq   $s3, $zero, L4_31
        # t2 = *s
        lb    $s4, 0($s0)
        # t3 = chartoint t2
        move  $t0, $s4
        move  $s5, $t0
        # if t3 int== 32 goto 10
        li    $t1, 32
        beq   $s5, $t1, L4_10
        # t4 = *s
        lb    $s6, 0($s0)
        # t5 = chartoint t4
        move  $t0, $s6
        move  $s7, $t0
        # if t5 int!= 9 goto 12
        li    $t1, 9
        bne   $s7, $t1, L4_12
L4_10:
        # inside = 0
        li    $s1, 0
        # goto 15
        j     L4_15
L4_12:
        # if inside int!= 0 goto 15
        bne   $s1, $zero, L4_15
        # inside = 1
        li    $s1, 1
        # words = words int+ 1
        addiu $s2, $s2, 1
L4_15:
        # s = s ptr+ 1
        addiu $s0, $s0, 1
        # t1 = *s
        lb    $s3, 0($s0)
        # if t1 char== 0 goto 31
        beq   $s3, $zero, L4_31
        # t2 = *s
        lb    $s4, 0($s0)
        # t3 = chartoint t2
        move  $t0, $s4
        move  $s5, $t0
        # if t3 int== 32 goto 24
        li    $t1, 32
        beq   $s5, $t1, L4_24
        # t4 = *s
        lb    $s6, 0($s0)
        # t5 = chartoint t4
        move  $t0, $s6
        move  $s7, $t0
        # if t5 int!= 9 goto 26
        li    $t1, 9
        bne   $s7, $t1, L4_26
L4_24:
        # inside = 0
        li    $s1, 0
        # goto 29
        j     L4_29
L4_26:
        # if inside int!= 0 goto 29
        bne   $s1, $zero, L4_29
        # inside = 1
        li    $s1, 1
        # words = words int+ 1
        addiu $s2, $s2, 1
L4_29:
        # s = s ptr+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L4_2
L4_31:
        # return words
        move  $v0, $s2
        j     _Z10countWordsPKc_exit
_Z10countWordsPKc_exit:
        lw    $s0, -24($fp)
        lw    $s1, -32($fp)
        lw    $s2, -28($fp)
        lw    $s3, -4($fp)
        lw    $s4, -8($fp)
        lw    $s5, -12($fp)
        lw    $s6, -16($fp)
        lw    $s7, -20($fp)
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
        addiu $sp, $sp, -152
        lw    $t8, __stack_limit
        sltu  $t8, $sp, $t8
        beqz  $t8, M5_0
        j     __stack_overflow
M5_0:
        sw    $s0, -124($fp)
        sw    $s1, -136($fp)
        sw    $s2, -140($fp)
        sw    $s3, -144($fp)
        sw    $s4, -148($fp)
        sw    $s5, -152($fp)
        sw    $s6, -128($fp)
        sw    $s7, -132($fp)
        # names[0] = "delta"
        la    $t0, str0
        sw    $t0, -60($fp)
        # names[4] = "alpha"
        la    $t0, str1
        sw    $t0, -56($fp)
        # names[8] = "charlie"
        la    $t0, str2
        sw    $t0, -52($fp)
        # t1 = &buf
        addiu $s0, $fp, -32
        # t55 = t1
        move  $s1, $s0
        # t56 = "compiler"
        la    $s2, str3
L5_6:
        # t57 = t55
        move  $s4, $s1
        # t55 = t55 ptr+ 1
        addiu $s1, $s1, 1
        # t58 = t56
        move  $s5, $s2
        # t56 = t56 ptr+ 1
        addiu $s2, $s2, 1
        # t59 = *t58
        lb    $s3, 0($s5)
        # *t57 = t59
        sb    $s3, 0($s4)
        # t60 = chartoint t59
        move  $t0, $s3
        move  $s6, $t0
        # if t60 int!= 0 goto 6
        bne   $s6, $zero, L5_6
        # t62 = 0
        li    $s1, 0
L5_15:
        # t63 = t1 ptr+ t62
        addu  $s2, $s0, $s1
        # t64 = *t63
        lb    $s3, 0($s2)
        # t65 = chartoint t64
        move  $t0, $s3
        move  $s4, $t0
        # if t65 int== 0 goto 26
        beq   $s4, $zero, L5_26
        # t62 = t62 int+ 1
        addiu $s1, $s1, 1
        # t63 = t1 ptr+ t62
        addu  $s2, $s0, $s1
        # t64 = *t63
        lb    $s3, 0($s2)
        # t65 = chartoint t64
        move  $t0, $s3
        move  $s4, $t0
        # if t65 int== 0 goto 26
        beq   $s4, $zero, L5_26
        # t62 = t62 int+ 1
        addiu $s1, $s1, 1
        # goto 15
        j     L5_15
L5_26:
        # param "%s %d\n"
        # param t1
        # param t62
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t67 = 0
        li    $s1, 0
        # param t1
        # t68 = call length(const char *), 1
        addiu $sp, $sp, -16
        move  $a0, $s0
        jal   _Z6lengthPKc
        addiu $sp, $sp, 16
        move  $s3, $v0
        # t69 = t68 int- 1
        addiu $s2, $s3, -1
L5_34:
        # if t67 int>= t69 goto 53
        bge   $s1, $s2, L5_53
        # t70 = t1 ptr+ t67
        addu  $s3, $s0, $s1
        # t71 = *t70
        lb    $s5, 0($s3)
        # t72 = t1 ptr+ t69
        addu  $s4, $s0, $s2
        # t73 = *t72
        lb    $s6, 0($s4)
        # *t70 = t73
        sb    $s6, 0($s3)
        # *t72 = t71
        sb    $s5, 0($s4)
        # t67 = t67 int+ 1
        addiu $s1, $s1, 1
        # t69 = t69 int- 1
        addiu $s2, $s2, -1
        # if t67 int>= t69 goto 53
        bge   $s1, $s2, L5_53
        # t70 = t1 ptr+ t67
        addu  $s3, $s0, $s1
        # t71 = *t70
        lb    $s5, 0($s3)
        # t72 = t1 ptr+ t69
        addu  $s4, $s0, $s2
        # t73 = *t72
        lb    $s6, 0($s4)
        # *t70 = t73
        sb    $s6, 0($s3)
        # *t72 = t71
        sb    $s5, 0($s4)
        # t67 = t67 int+ 1
        addiu $s1, $s1, 1
        # t69 = t69 int- 1
        addiu $s2, $s2, -1
        # goto 34
        j     L5_34
L5_53:
        # t76 = 0
        li    $s1, 0
L5_54:
        # t77 = t1 ptr+ t76
        addu  $s2, $s0, $s1
        # t78 = *t77
        lb    $s3, 0($s2)
        # if t78 char== 0 goto 64
        beq   $s3, $zero, L5_64
        # t79 = *t77
        lb    $s4, 0($s2)
        # t80 = chartoint t79
        move  $t0, $s4
        move  $s5, $t0
        # if t80 int!= 112 goto 62
        li    $t1, 112
        bne   $s5, $t1, L5_62
        # t8 = t76
        move  $s6, $s1
        # goto 65
        j     L5_65
L5_62:
        # t76 = t76 int+ 1
        addiu $s1, $s1, 1
        # goto 54
        j     L5_54
L5_64:
        # t8 = -1
        li    $s6, -1
L5_65:
        # t84 = 0
        li    $s1, 0
L5_66:
        # t85 = t1 ptr+ t84
        addu  $s2, $s0, $s1
        # t86 = *t85
        lb    $s3, 0($s2)
        # if t86 char== 0 goto 76
        beq   $s3, $zero, L5_76
        # t87 = *t85
        lb    $s4, 0($s2)
        # t88 = chartoint t87
        move  $t0, $s4
        move  $s5, $t0
        # if t88 int!= 122 goto 74
        li    $t1, 122
        bne   $s5, $t1, L5_74
        # t10 = t84
        move  $s7, $s1
        # goto 77
        j     L5_77
L5_74:
        # t84 = t84 int+ 1
        addiu $s1, $s1, 1
        # goto 66
        j     L5_66
L5_76:
        # t10 = -1
        li    $s7, -1
L5_77:
        # param "%s %d %d\n"
        # param t1
        # param t8
        # param t10
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s6, 8($sp)
        sw    $s7, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t90 = "abc"
        la    $s0, str7
        # t91 = "abd"
        la    $s1, str8
L5_84:
        # t92 = *t90
        lb    $s2, 0($s0)
        # if t92 char== 0 goto 103
        beq   $s2, $zero, L5_103
        # t93 = *t90
        lb    $s3, 0($s0)
        # t94 = chartoint t93
        move  $t0, $s3
        move  $s4, $t0
        # t95 = *t91
        lb    $s5, 0($s1)
        # t96 = chartoint t95
        move  $t0, $s5
        move  $s6, $t0
        # if t94 int!= t96 goto 103
        bne   $s4, $s6, L5_103
        # t90 = t90 ptr+ 1
        addiu $s0, $s0, 1
        # t91 = t91 ptr+ 1
        addiu $s1, $s1, 1
        # t92 = *t90
        lb    $s2, 0($s0)
        # if t92 char== 0 goto 103
        beq   $s2, $zero, L5_103
        # t93 = *t90
        lb    $s3, 0($s0)
        # t94 = chartoint t93
        move  $t0, $s3
        move  $s4, $t0
        # t95 = *t91
        lb    $s5, 0($s1)
        # t96 = chartoint t95
        move  $t0, $s5
        move  $s6, $t0
        # if t94 int!= t96 goto 103
        bne   $s4, $s6, L5_103
        # t90 = t90 ptr+ 1
        addiu $s0, $s0, 1
        # t91 = t91 ptr+ 1
        addiu $s1, $s1, 1
        # goto 84
        j     L5_84
L5_103:
        # t97 = *t90
        lb    $s2, 0($s0)
        # t98 = chartoint t97
        move  $t0, $s2
        move  $s0, $t0
        # t99 = *t91
        lb    $s2, 0($s1)
        # t100 = chartoint t99
        move  $t0, $s2
        move  $s1, $t0
        # t101 = t98 int- t100
        subu  $s2, $s0, $s1
        # if t101 int< 0 goto 111
        slt   $s7, $s2, $zero
L5_112:
        # t102 = "abc"
        la    $s0, str7
        # t103 = "abc"
        la    $s1, str7
L5_114:
        # t104 = *t102
        lb    $s2, 0($s0)
        # if t104 char== 0 goto 133
        beq   $s2, $zero, L5_133
        # t105 = *t102
        lb    $s3, 0($s0)
        # t106 = chartoint t105
        move  $t0, $s3
        move  $s4, $t0
        # t107 = *t103
        lb    $s5, 0($s1)
        # t108 = chartoint t107
        move  $t0, $s5
        move  $s6, $t0
        # if t106 int!= t108 goto 133
        bne   $s4, $s6, L5_133
        # t102 = t102 ptr+ 1
        addiu $s0, $s0, 1
        # t103 = t103 ptr+ 1
        addiu $s1, $s1, 1
        # t104 = *t102
        lb    $s2, 0($s0)
        # if t104 char== 0 goto 133
        beq   $s2, $zero, L5_133
        # t105 = *t102
        lb    $s3, 0($s0)
        # t106 = chartoint t105
        move  $t0, $s3
        move  $s4, $t0
        # t107 = *t103
        lb    $s5, 0($s1)
        # t108 = chartoint t107
        move  $t0, $s5
        move  $s6, $t0
        # if t106 int!= t108 goto 133
        bne   $s4, $s6, L5_133
        # t102 = t102 ptr+ 1
        addiu $s0, $s0, 1
        # t103 = t103 ptr+ 1
        addiu $s1, $s1, 1
        # goto 114
        j     L5_114
L5_133:
        # t109 = *t102
        lb    $s2, 0($s0)
        # t110 = chartoint t109
        move  $t0, $s2
        move  $s0, $t0
        # t111 = *t103
        lb    $s2, 0($s1)
        # t112 = chartoint t111
        move  $t0, $s2
        move  $s1, $t0
        # t13 = t110 int- t112
        subu  $t0, $s0, $s1
        sw    $t0, -76($fp)
        # t114 = "b"
        la    $s0, str9
        # t115 = "abc"
        la    $s1, str7
L5_140:
        # t116 = *t114
        lb    $s2, 0($s0)
        # if t116 char== 0 goto 159
        beq   $s2, $zero, L5_159
        # t117 = *t114
        lb    $s3, 0($s0)
        # t118 = chartoint t117
        move  $t0, $s3
        move  $s4, $t0
        # t119 = *t115
        lb    $s5, 0($s1)
        # t120 = chartoint t119
        move  $t0, $s5
        move  $s6, $t0
        # if t118 int!= t120 goto 159
        bne   $s4, $s6, L5_159
        # t114 = t114 ptr+ 1
        addiu $s0, $s0, 1
        # t115 = t115 ptr+ 1
        addiu $s1, $s1, 1
        # t116 = *t114
        lb    $s2, 0($s0)
        # if t116 char== 0 goto 159
        beq   $s2, $zero, L5_159
        # t117 = *t114
        lb    $s3, 0($s0)
        # t118 = chartoint t117
        move  $t0, $s3
        move  $s4, $t0
        # t119 = *t115
        lb    $s5, 0($s1)
        # t120 = chartoint t119
        move  $t0, $s5
        move  $s6, $t0
        # if t118 int!= t120 goto 159
        bne   $s4, $s6, L5_159
        # t114 = t114 ptr+ 1
        addiu $s0, $s0, 1
        # t115 = t115 ptr+ 1
        addiu $s1, $s1, 1
        # goto 140
        j     L5_140
L5_159:
        # t121 = *t114
        lb    $s2, 0($s0)
        # t122 = chartoint t121
        move  $t0, $s2
        move  $s0, $t0
        # t123 = *t115
        lb    $s2, 0($s1)
        # t124 = chartoint t123
        move  $t0, $s2
        move  $s1, $t0
        # t125 = t122 int- t124
        subu  $s2, $s0, $s1
        # if t125 int> 0 goto 167
        slt   $s0, $zero, $s2
L5_168:
        # param "%d %d %d\n"
        # param t11
        # param t13
        # param t14
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s7, 4($sp)
        lw    $t0, -76($fp)
        sw    $t0, 8($sp)
        sw    $s0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # smallest = 0
        li    $t0, 0
        sw    $t0, -64($fp)
        # i.32 = 1
        li    $s7, 1
L5_175:
        # if i.32 int>= 3 goto 210
        li    $t1, 3
        bge   $s7, $t1, L5_210
        # t16 = i.32 int<< 2
        sll   $t0, $s7, 2
        sw    $t0, -80($fp)
        # t17 = names[t16]
        addiu $t8, $fp, -60
        lw    $t9, -80($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -84($fp)
        # t18 = smallest int<< 2
        lw    $t0, -64($fp)
        sll   $t0, $t0, 2
        sw    $t0, -88($fp)
        # t19 = names[t18]
        addiu $t8, $fp, -60
        lw    $t9, -88($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -92($fp)
        # t126 = t17
        lw    $s0, -84($fp)
        # t127 = t19
        lw    $s1, -92($fp)
L5_182:
        # t128 = *t126
        lb    $s2, 0($s0)
        # if t128 char== 0 goto 201
        beq   $s2, $zero, L5_201
        # t129 = *t126
        lb    $s3, 0($s0)
        # t130 = chartoint t129
        move  $t0, $s3
        move  $s4, $t0
        # t131 = *t127
        lb    $s5, 0($s1)
        # t132 = chartoint t131
        move  $t0, $s5
        move  $s6, $t0
        # if t130 int!= t132 goto 201
        bne   $s4, $s6, L5_201
        # t126 = t126 ptr+ 1
        addiu $s0, $s0, 1
        # t127 = t127 ptr+ 1
        addiu $s1, $s1, 1
        # t128 = *t126
        lb    $s2, 0($s0)
        # if t128 char== 0 goto 201
        beq   $s2, $zero, L5_201
        # t129 = *t126
        lb    $s3, 0($s0)
        # t130 = chartoint t129
        move  $t0, $s3
        move  $s4, $t0
        # t131 = *t127
        lb    $s5, 0($s1)
        # t132 = chartoint t131
        move  $t0, $s5
        move  $s6, $t0
        # if t130 int!= t132 goto 201
        bne   $s4, $s6, L5_201
        # t126 = t126 ptr+ 1
        addiu $s0, $s0, 1
        # t127 = t127 ptr+ 1
        addiu $s1, $s1, 1
        # goto 182
        j     L5_182
L5_201:
        # t133 = *t126
        lb    $t0, 0($s0)
        sb    $t0, -102($fp)
        # t134 = chartoint t133
        lb    $t0, -102($fp)
        sw    $t0, -108($fp)
        # t135 = *t127
        lb    $t0, 0($s1)
        sb    $t0, -109($fp)
        # t136 = chartoint t135
        lb    $t0, -109($fp)
        sw    $t0, -116($fp)
        # t137 = t134 int- t136
        lw    $t0, -108($fp)
        lw    $t1, -116($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -120($fp)
        # if t137 int>= 0 goto 208
        bge   $t0, $zero, L5_208
        # smallest = i.32
        move  $t0, $s7
        sw    $t0, -64($fp)
L5_208:
        # i.32 = i.32 int+ 1
        addiu $s7, $s7, 1
        # goto 175
        j     L5_175
L5_210:
        # t22 = smallest int<< 2
        lw    $t0, -64($fp)
        sll   $s0, $t0, 2
        # t23 = names[t22]
        addiu $t8, $fp, -60
        addu  $t8, $t8, $s0
        lw    $s1, 0($t8)
        # t24 = names[8]
        lw    $s0, -52($fp)
        # t25 = t24 ptr+ 3
        addiu $s2, $s0, 3
        # t26 = *t25
        lb    $s0, 0($s2)
        # t27 = chartoint t26
        move  $t0, $s0
        move  $s2, $t0
        # param "%s %c\n"
        # param t23
        # param t27
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str10
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t29 = &num
        addiu $s0, $fp, -48
        # param -40213
        # param t29
        # call toText(int, char *), 2
        addiu $sp, $sp, -16
        li    $a0, -40213
        move  $a1, $s0
        jal   _Z6toTextiPc
        addiu $sp, $sp, 16
        # param t29
        # t32 = call toNumber(const char *), 1
        addiu $sp, $sp, -16
        move  $a0, $s0
        jal   _Z8toNumberPKc
        addiu $sp, $sp, 16
        move  $s1, $v0
        # t33 = t32 int+ 1
        addiu $s2, $s1, 1
        # param "77x"
        # t34 = call toNumber(const char *), 1
        addiu $sp, $sp, -16
        la    $a0, str11
        jal   _Z8toNumberPKc
        addiu $sp, $sp, 16
        move  $s1, $v0
        # param "%s %d %d\n"
        # param t29
        # param t33
        # param t34
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s2, 8($sp)
        sw    $s1, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param "level"
        # t35 = call isPalindrome(const char *), 1
        addiu $sp, $sp, -16
        la    $a0, str12
        jal   _Z12isPalindromePKc
        addiu $sp, $sp, 16
        move  $s0, $v0
        # param "lever"
        # t36 = call isPalindrome(const char *), 1
        addiu $sp, $sp, -16
        la    $a0, str13
        jal   _Z12isPalindromePKc
        addiu $sp, $sp, 16
        move  $s1, $v0
        # param "  the quick  brown fox "
        # t37 = call countWords(const char *), 1
        addiu $sp, $sp, -16
        la    $a0, str14
        jal   _Z10countWordsPKc
        addiu $sp, $sp, 16
        move  $s2, $v0
        # param "%d %d %d\n"
        # param t35
        # param t36
        # param t37
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # upper[0] = 109
        li    $t0, 109
        sb    $t0, -72($fp)
        # upper[1] = 105
        li    $t0, 105
        sb    $t0, -71($fp)
        # upper[2] = 120
        li    $t0, 120
        sb    $t0, -70($fp)
        # upper[3] = 101
        li    $t0, 101
        sb    $t0, -69($fp)
        # upper[4] = 100
        li    $t0, 100
        sb    $t0, -68($fp)
        # upper[5] = 0
        sb    $zero, -67($fp)
        # upper[6] = 0
        sb    $zero, -66($fp)
        # upper[7] = 0
        sb    $zero, -65($fp)
        # i.34 = 0
        li    $s0, 0
L5_254:
        # t38 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s1, 0($t8)
        # if t38 char== 0 goto 285
        beq   $s1, $zero, L5_285
        # t39 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s2, 0($t8)
        # t40 = chartoint t39
        move  $t0, $s2
        move  $s3, $t0
        # if t40 int< 97 goto 268
        li    $t1, 97
        blt   $s3, $t1, L5_268
        # t41 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s4, 0($t8)
        # t42 = chartoint t41
        move  $t0, $s4
        move  $s5, $t0
        # if t42 int> 122 goto 268
        li    $t1, 122
        bgt   $s5, $t1, L5_268
        # t43 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s6, 0($t8)
        # t44 = chartoint t43
        move  $t0, $s6
        move  $s7, $t0
        # t45 = t44 int- 97
        addiu $t0, $s7, -97
        sw    $t0, -96($fp)
        # t46 = t45 int+ 65
        addiu $t0, $t0, 65
        sw    $t0, -100($fp)
        # t47 = inttochar t46
        sb    $t0, -101($fp)
        # upper[i.34] = t47
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $t0, -101($fp)
        sb    $t0, 0($t8)
L5_268:
        # i.34 = i.34 int+ 1
        addiu $s0, $s0, 1
        # t38 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s1, 0($t8)
        # if t38 char== 0 goto 285
        beq   $s1, $zero, L5_285
        # t39 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s2, 0($t8)
        # t40 = chartoint t39
        move  $t0, $s2
        move  $s3, $t0
        # if t40 int< 97 goto 283
        li    $t1, 97
        blt   $s3, $t1, L5_283
        # t41 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s4, 0($t8)
        # t42 = chartoint t41
        move  $t0, $s4
        move  $s5, $t0
        # if t42 int> 122 goto 283
        li    $t1, 122
        bgt   $s5, $t1, L5_283
        # t43 = upper[i.34]
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $s6, 0($t8)
        # t44 = chartoint t43
        move  $t0, $s6
        move  $s7, $t0
        # t45 = t44 int- 97
        addiu $t0, $s7, -97
        sw    $t0, -96($fp)
        # t46 = t45 int+ 65
        addiu $t0, $t0, 65
        sw    $t0, -100($fp)
        # t47 = inttochar t46
        sb    $t0, -101($fp)
        # upper[i.34] = t47
        addiu $t8, $fp, -72
        addu  $t8, $t8, $s0
        lb    $t0, -101($fp)
        sb    $t0, 0($t8)
L5_283:
        # i.34 = i.34 int+ 1
        addiu $s0, $s0, 1
        # goto 254
        j     L5_254
L5_285:
        # t49 = &upper
        addiu $s0, $fp, -72
        # param "%s %d\n"
        # param t49
        # param 8
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        li    $t0, 8
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t138 = names[4]
        lw    $s4, -56($fp)
        # t139 = 0
        li    $s0, 0
L5_292:
        # t140 = t138 ptr+ t139
        addu  $s1, $s4, $s0
        # t141 = *t140
        lb    $s2, 0($s1)
        # t142 = chartoint t141
        move  $t0, $s2
        move  $s3, $t0
        # if t142 int== 0 goto 303
        beq   $s3, $zero, L5_303
        # t139 = t139 int+ 1
        addiu $s0, $s0, 1
        # t140 = t138 ptr+ t139
        addu  $s1, $s4, $s0
        # t141 = *t140
        lb    $s2, 0($s1)
        # t142 = chartoint t141
        move  $t0, $s2
        move  $s3, $t0
        # if t142 int== 0 goto 303
        beq   $s3, $zero, L5_303
        # t139 = t139 int+ 1
        addiu $s0, $s0, 1
        # goto 292
        j     L5_292
L5_303:
        # t52 = buf[0]
        lb    $s1, -32($fp)
        # t53 = chartoint t52
        move  $t0, $s1
        move  $s2, $t0
        # t54 = t139 int+ t53
        addu  $s1, $s0, $s2
        # return t54
        move  $v0, $s1
        j     main__exit
main__exit:
        lw    $s0, -124($fp)
        lw    $s1, -136($fp)
        lw    $s2, -140($fp)
        lw    $s3, -144($fp)
        lw    $s4, -148($fp)
        lw    $s5, -152($fp)
        lw    $s6, -128($fp)
        lw    $s7, -132($fp)
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
#   __div_by_zero             jumped to by integer division with a zero divisor
#   __stack_overflow          jumped to by a prologue whose $sp passed __stack_limit
#                             (both print the interpreter's message and exit with 2)
#
# The generated code keeps nothing in registers across a call, so these
# routines use the temporaries freely; they preserve $sp, $fp and $s0-$s7.
# =====================================================================

        .data
__pf_buf:    .space 96
__pf_digits: .asciiz "0123456789abcdef"
__pf_nil:    .asciiz "(nil)"              # %p of a null pointer, as glibc prints it
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
__c_split:   .double 134217729.0         # 2^27 + 1, Veltkamp's splitting constant
__pf_mend:   .word 0                    # %g: where the digits end (the exponent, if any, follows)
__stack_limit: .word 0                  # lowest $sp a frame may reach; set by the start-up code
__heap_free: .word 0                    # the free list: freed blocks, most recent first (D45)
__m_divzero: .asciiz "\nrun-time error: division by zero\n"
__m_stack:   .asciiz "\nrun-time error: stack overflow (recursion too deep)\n"

        .text

# ------------------------------------------------------- run-time errors
__div_by_zero:
        la    $a0, __m_divzero
        j     __rt_error
__stack_overflow:
        la    $a0, __m_stack
__rt_error:                             # print the message in $a0, exit with code 2
        li    $v0, 4
        syscall
        li    $a0, 2
        li    $v0, 17
        syscall

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
__malloc_n:                             # size in $t0 -> block in $v0 (uses $t1, $t4-$t7, $a0)
        addiu $t1, $t0, 7               # capacity: the size rounded up to 8, at least 8
        li    $t4, -8
        and   $t1, $t1, $t4
        bnez  $t1, __malloc_fit
        li    $t1, 8
__malloc_fit:                           # first fit in the free list, most recently freed first
        la    $t5, __heap_free          # $t5: the word that points at the block looked at
__malloc_scan:
        lw    $t6, 0($t5)
        beqz  $t6, __malloc_new
        lw    $t7, -8($t6)              # its capacity
        sltu  $t7, $t7, $t1
        bnez  $t7, __malloc_next
        lw    $t7, 0($t6)               # big enough: unlink it and hand it out whole
        sw    $t7, 0($t5)
        move  $v0, $t6
        jr    $ra
__malloc_next:
        move  $t5, $t6                  # a free block's first word links to the next one
        j     __malloc_scan
__malloc_new:                           # none fits: a fresh block from sbrk, 8-byte aligned,
        addiu $a0, $t1, 15              # with its capacity in the 8 bytes before it
        and   $a0, $a0, $t4
        li    $v0, 9                    # sbrk
        syscall
        addiu $v0, $v0, 7
        and   $v0, $v0, $t4
        sw    $t1, 0($v0)
        addiu $v0, $v0, 8
        jr    $ra

__calloc:                               # calloc(count, size): a block, cleared
        lw    $t0, 0($sp)
        lw    $t1, 4($sp)
        mul   $t0, $t0, $t1
        move  $t9, $ra
        jal   __malloc_n
        lw    $t1, -8($v0)              # the whole capacity: a reused block is not zero
        move  $t2, $v0
__calloc_zero:
        sw    $zero, 0($t2)
        addiu $t2, $t2, 4
        addiu $t1, $t1, -4
        bnez  $t1, __calloc_zero
        jr    $t9

__realloc:                              # realloc(pointer, size)
        lw    $t2, 0($sp)
        lw    $t0, 4($sp)
        move  $t9, $ra
        beqz  $t2, __realloc_new        # realloc(0, n) is malloc(n)
        lw    $t3, -8($t2)              # the old block's capacity
        sltu  $t4, $t3, $t0
        bnez  $t4, __realloc_new
        move  $v0, $t2                  # it still fits: the same block
        jr    $t9
__realloc_new:
        jal   __malloc_n                # keeps $t2, $t3, $t9
        beqz  $t2, __realloc_done
        move  $t5, $v0
        move  $a0, $v0                  # copy the old capacity (the new block is bigger)
        move  $a1, $t2
        move  $a2, $t3
        jal   __memcpy
        lw    $t1, __heap_free          # then free the old block
        sw    $t1, 0($t2)
        sw    $t2, __heap_free
        move  $v0, $t5
__realloc_done:
        jr    $t9

__free:                                 # free(pointer): onto the free list, for malloc to reuse
        lw    $t0, 0($sp)
        beqz  $t0, __free_done          # free(0) does nothing
        lw    $t1, __heap_free
        sw    $t1, 0($t0)
        sw    $t0, __heap_free
__free_done:
        jr    $ra

# ------------------------------------------------------- 64-bit arithmetic
__udivmodll:                            # unsigned: quotient $v1:$v0, remainder $t9:$t8
        or    $t6, $a2, $a3             # a zero divisor is a run-time error
        beqz  $t6, __div_by_zero
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
# %d %i %u %x %X %o %c %s %p %f %e %E %g %G %%, with '-' and '0' flags,
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
        li    $t1, 112
        beq   $t0, $t1, __pf_p
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

__pf_p:                                 # %p: 0x and the address in hex, (nil) for 0 (as glibc)
        lw    $t0, 0($s1)
        addiu $s1, $s1, 4
        li    $t2, 0
        bnez  $t0, __pf_phex
        la    $t0, __pf_nil
        li    $t1, 5
        jal   __pf_out
        j     __pf_loop
__pf_phex:                              # hex digits, last one first, then "0x" in front
        la    $s5, __pf_buf+95
        li    $s6, 0
__pf_ploop:
        andi  $t5, $t0, 15
        la    $t8, __pf_digits
        addu  $t8, $t8, $t5
        lbu   $t5, 0($t8)
        addiu $s5, $s5, -1
        sb    $t5, 0($s5)
        addiu $s6, $s6, 1
        srl   $t0, $t0, 4
        bnez  $t0, __pf_ploop
        li    $t5, 120
        sb    $t5, -1($s5)
        li    $t5, 48
        sb    $t5, -2($s5)
        addiu $s5, $s5, -2
        addiu $s6, $s6, 2
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
        l.d   $f16, __c_ten             # 10^precision first (exact up to 10^22) ...
        l.d   $f18, __c_one
        move  $t5, $s5
__pf_fscale1:
        blez  $t5, __pf_fscale2
        mul.d $f18, $f18, $f16
        addiu $t5, $t5, -1
        j     __pf_fscale1
__pf_fscale2:                           # ... then one multiplication, with its exact rounding error
        l.d   $f0, __c_split            # in $f0 (Dekker's two-product, Veltkamp splitting): when
        mul.d $f4, $f0, $f12            # the product lands exactly on a half, the error says which
        sub.d $f6, $f4, $f12            # side of it the true value is (2.675 is 2.67499999...)
        sub.d $f4, $f4, $f6             # $f4 = high half of the value
        sub.d $f6, $f12, $f4            # $f6 = low half
        mul.d $f8, $f0, $f18
        sub.d $f10, $f8, $f18
        sub.d $f8, $f8, $f10            # $f8 = high half of 10^precision
        sub.d $f10, $f18, $f8           # $f10 = low half
        mul.d $f12, $f12, $f18          # the rounded product
        mul.d $f0, $f4, $f8
        sub.d $f0, $f0, $f12
        mul.d $f18, $f4, $f10
        add.d $f0, $f0, $f18
        mul.d $f18, $f6, $f8
        add.d $f0, $f0, $f18
        mul.d $f18, $f6, $f10
        add.d $f0, $f0, $f18            # $f0 = exact product - rounded product
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
        l.d   $f16, __c_zero            # exactly half as computed: the true value decides
        c.lt.d $f0, $f16
        bc1t  __pf_fdigits              # it was just below the half: down
        c.lt.d $f16, $f0
        bc1t  __pf_fup                  # just above: up
        andi  $t5, $v0, 1               # a true half: round to the even neighbour
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
