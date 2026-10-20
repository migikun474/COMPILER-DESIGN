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
        addiu $sp, $sp, -40
        sw    $s0, -36($fp)
        sw    $s1, -20($fp)
        sw    $s2, -24($fp)
        sw    $s3, -28($fp)
        sw    $s4, -32($fp)
        lw    $s4, 8($fp)
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
        # if t3 int== 0 goto 7
        beq   $s3, $zero, L0_7
        # n = n int+ 1
        addiu $s0, $s0, 1
        # goto 1
        j     L0_1
L0_7:
        # return n
        move  $v0, $s0
        j     _Z6lengthPKc_exit
_Z6lengthPKc_exit:
        lw    $s0, -36($fp)
        lw    $s1, -20($fp)
        lw    $s2, -24($fp)
        lw    $s3, -28($fp)
        lw    $s4, -32($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# copy(char *, const char *)
_Z4copyPcPKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        sw    $s0, -28($fp)
        sw    $s1, -36($fp)
        sw    $s2, -40($fp)
        sw    $s3, -20($fp)
        sw    $s4, -24($fp)
        sw    $s5, -32($fp)
        lw    $s1, 8($fp)
        lw    $s2, 12($fp)
L1_0:
        # t1 = to
        move  $s3, $s1
        # to = to ptr+ 1
        addiu $s1, $s1, 1
        # t3 = from
        move  $s4, $s2
        # from = from ptr+ 1
        addiu $s2, $s2, 1
        # t5 = *t3
        lb    $s0, 0($s4)
        # *t1 = t5
        sb    $s0, 0($s3)
        # t6 = chartoint t5
        move  $t0, $s0
        move  $s5, $t0
        # if t6 int!= 0 goto 0
        bne   $s5, $zero, L1_0
        # return
        j     _Z4copyPcPKc_exit
_Z4copyPcPKc_exit:
        lw    $s0, -28($fp)
        lw    $s1, -36($fp)
        lw    $s2, -40($fp)
        lw    $s3, -20($fp)
        lw    $s4, -24($fp)
        lw    $s5, -32($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# compare(const char *, const char *)
_Z7comparePKcS0_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        sw    $s0, -60($fp)
        sw    $s1, -64($fp)
        sw    $s2, -40($fp)
        sw    $s3, -44($fp)
        sw    $s4, -48($fp)
        sw    $s5, -52($fp)
        sw    $s6, -56($fp)
        lw    $s0, 8($fp)
        lw    $s1, 12($fp)
L2_0:
        # t1 = *a
        lb    $s2, 0($s0)
        # if t1 char== 0 goto 10
        beq   $s2, $zero, L2_10
        # t2 = *a
        lb    $s3, 0($s0)
        # t3 = chartoint t2
        move  $t0, $s3
        move  $s4, $t0
        # t4 = *b
        lb    $s5, 0($s1)
        # t5 = chartoint t4
        move  $t0, $s5
        move  $s6, $t0
        # if t3 int!= t5 goto 10
        bne   $s4, $s6, L2_10
        # a = a ptr+ 1
        addiu $s0, $s0, 1
        # b = b ptr+ 1
        addiu $s1, $s1, 1
        # goto 0
        j     L2_0
L2_10:
        # t8 = *a
        lb    $s2, 0($s0)
        # t9 = chartoint t8
        move  $t0, $s2
        move  $s0, $t0
        # t10 = *b
        lb    $s2, 0($s1)
        # t11 = chartoint t10
        move  $t0, $s2
        move  $s1, $t0
        # t12 = t9 int- t11
        subu  $s2, $s0, $s1
        # return t12
        move  $v0, $s2
        j     _Z7comparePKcS0__exit
_Z7comparePKcS0__exit:
        lw    $s0, -60($fp)
        lw    $s1, -64($fp)
        lw    $s2, -40($fp)
        lw    $s3, -44($fp)
        lw    $s4, -48($fp)
        lw    $s5, -52($fp)
        lw    $s6, -56($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# reverse(char *)
_Z7reversePc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -72
        sw    $s0, -72($fp)
        sw    $s1, -64($fp)
        sw    $s2, -48($fp)
        sw    $s3, -56($fp)
        sw    $s4, -68($fp)
        sw    $s5, -52($fp)
        sw    $s6, -60($fp)
        lw    $s4, 8($fp)
        # i = 0
        li    $s0, 0
        # t12 = 0
        li    $s2, 0
L3_2:
        # t13 = s ptr+ t12
        addu  $s1, $s4, $s2
        # t14 = *t13
        lb    $s3, 0($s1)
        # t15 = chartoint t14
        move  $t0, $s3
        move  $s5, $t0
        # if t15 int== 0 goto 8
        beq   $s5, $zero, L3_8
        # t12 = t12 int+ 1
        addiu $s2, $s2, 1
        # goto 2
        j     L3_2
L3_8:
        # j = t12 int- 1
        addiu $s1, $s2, -1
L3_9:
        # if i int>= j goto 19
        bge   $s0, $s1, L3_19
        # t3 = s ptr+ i
        addu  $s2, $s4, $s0
        # t4 = *t3
        lb    $s5, 0($s2)
        # t6 = s ptr+ j
        addu  $s3, $s4, $s1
        # t7 = *t6
        lb    $s6, 0($s3)
        # *t3 = t7
        sb    $s6, 0($s2)
        # *t6 = t4
        sb    $s5, 0($s3)
        # i = i int+ 1
        addiu $s0, $s0, 1
        # j = j int- 1
        addiu $s1, $s1, -1
        # goto 9
        j     L3_9
L3_19:
        # return
        j     _Z7reversePc_exit
_Z7reversePc_exit:
        lw    $s0, -72($fp)
        lw    $s1, -64($fp)
        lw    $s2, -48($fp)
        lw    $s3, -56($fp)
        lw    $s4, -68($fp)
        lw    $s5, -52($fp)
        lw    $s6, -60($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# find(const char *, char)
_Z4findPKcc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -48($fp)
        sw    $s1, -24($fp)
        sw    $s2, -28($fp)
        sw    $s3, -32($fp)
        sw    $s4, -36($fp)
        sw    $s5, -40($fp)
        sw    $s6, -44($fp)
        lw    $s6, 8($fp)
        lw    $s1, 12($fp)
        # i = 0
        li    $s0, 0
        # t6 = chartoint c
        move  $t0, $s1
        move  $s5, $t0
L4_2:
        # t1 = text ptr+ i
        addu  $s1, $s6, $s0
        # t2 = *t1
        lb    $s2, 0($s1)
        # if t2 char== 0 goto 11
        beq   $s2, $zero, L4_11
        # t4 = *t1
        lb    $s3, 0($s1)
        # t5 = chartoint t4
        move  $t0, $s3
        move  $s4, $t0
        # if t5 int!= t6 goto 9
        bne   $s4, $s5, L4_9
        # return i
        move  $v0, $s0
        j     _Z4findPKcc_exit
L4_9:
        # i = i int+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L4_2
L4_11:
        # return -1
        li    $v0, -1
        j     _Z4findPKcc_exit
_Z4findPKcc_exit:
        lw    $s0, -48($fp)
        lw    $s1, -24($fp)
        lw    $s2, -28($fp)
        lw    $s3, -32($fp)
        lw    $s4, -36($fp)
        lw    $s5, -40($fp)
        lw    $s6, -44($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# toNumber(const char *)
_Z8toNumberPKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -88
        sw    $s0, -80($fp)
        sw    $s1, -84($fp)
        sw    $s2, -56($fp)
        sw    $s3, -60($fp)
        sw    $s4, -64($fp)
        sw    $s5, -68($fp)
        sw    $s6, -72($fp)
        sw    $s7, -76($fp)
        lw    $s0, 8($fp)
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
        bne   $s3, $t1, L5_7
        # sign = -1
        li    $t0, -1
        sw    $t0, -4($fp)
        # s = s ptr+ 1
        addiu $s0, $s0, 1
L5_7:
        # t5 = *s
        lb    $s2, 0($s0)
        # t6 = chartoint t5
        move  $t0, $s2
        move  $s3, $t0
        # if t6 int< 48 goto 20
        li    $t1, 48
        blt   $s3, $t1, L5_20
        # t7 = *s
        lb    $s4, 0($s0)
        # t8 = chartoint t7
        move  $t0, $s4
        move  $s5, $t0
        # if t8 int> 57 goto 20
        li    $t1, 57
        bgt   $s5, $t1, L5_20
        # t9 = v int* 10
        li    $t1, 10
        mul   $s6, $s1, $t1
        # t10 = *s
        lb    $s7, 0($s0)
        # t11 = chartoint t10
        move  $t0, $s7
        sw    $t0, -44($fp)
        # t12 = t11 int- 48
        addiu $t0, $t0, -48
        sw    $t0, -48($fp)
        # v = t9 int+ t12
        move  $t1, $t0
        addu  $s1, $s6, $t1
        # s = s ptr+ 1
        addiu $s0, $s0, 1
        # goto 7
        j     L5_7
L5_20:
        # t15 = sign int* v
        lw    $t0, -4($fp)
        mul   $s0, $t0, $s1
        # return t15
        move  $v0, $s0
        j     _Z8toNumberPKc_exit
_Z8toNumberPKc_exit:
        lw    $s0, -80($fp)
        lw    $s1, -84($fp)
        lw    $s2, -56($fp)
        lw    $s3, -60($fp)
        lw    $s4, -64($fp)
        lw    $s5, -68($fp)
        lw    $s6, -72($fp)
        lw    $s7, -76($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# toText(int, char *)
_Z6toTextiPc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -96
        sw    $s0, -92($fp)
        sw    $s1, -84($fp)
        sw    $s2, -88($fp)
        sw    $s3, -80($fp)
        sw    $s4, -64($fp)
        sw    $s5, -68($fp)
        sw    $s6, -72($fp)
        sw    $s7, -76($fp)
        lw    $s1, 8($fp)
        lw    $s2, 12($fp)
        # n = 0
        li    $s0, 0
        # if v int< 0 goto 4
        slt   $t0, $s1, $zero
        sw    $t0, -24($fp)
L6_5:
        # if t1 int== 0 goto 7
        lw    $t0, -24($fp)
        beq   $t0, $zero, L6_7
        # v = int- v
        negu  $s1, $s1
L6_7:
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
        bgt   $s3, $zero, L6_7
        # if t1 int== 0 goto 20
        lw    $t0, -24($fp)
        beq   $t0, $zero, L6_20
        # t9 = n
        move  $s1, $s0
        # n = n int+ 1
        addiu $s0, $s0, 1
        # tmp[t9] = 45
        addiu $t8, $fp, -12
        addu  $t8, $t8, $s1
        li    $t0, 45
        sb    $t0, 0($t8)
L6_20:
        # if n int<= 0 goto 28
        ble   $s0, $zero, L6_28
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
        j     L6_20
L6_28:
        # *out = 0
        sb    $zero, 0($s2)
        # return
        j     _Z6toTextiPc_exit
_Z6toTextiPc_exit:
        lw    $s0, -92($fp)
        lw    $s1, -84($fp)
        lw    $s2, -88($fp)
        lw    $s3, -80($fp)
        lw    $s4, -64($fp)
        lw    $s5, -68($fp)
        lw    $s6, -72($fp)
        lw    $s7, -76($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# isPalindrome(const char *)
_Z12isPalindromePKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -88
        sw    $s0, -88($fp)
        sw    $s1, -80($fp)
        sw    $s2, -60($fp)
        sw    $s3, -84($fp)
        sw    $s4, -64($fp)
        sw    $s5, -68($fp)
        sw    $s6, -72($fp)
        sw    $s7, -76($fp)
        lw    $s3, 8($fp)
        # i = 0
        li    $s0, 0
        # t14 = 0
        li    $s2, 0
L7_2:
        # t15 = s ptr+ t14
        addu  $s1, $s3, $s2
        # t16 = *t15
        lb    $s4, 0($s1)
        # t17 = chartoint t16
        move  $t0, $s4
        move  $s5, $t0
        # if t17 int== 0 goto 8
        beq   $s5, $zero, L7_8
        # t14 = t14 int+ 1
        addiu $s2, $s2, 1
        # goto 2
        j     L7_2
L7_8:
        # j = t14 int- 1
        addiu $s1, $s2, -1
L7_9:
        # if i int>= j goto 22
        bge   $s0, $s1, L7_22
        # t3 = i
        move  $s2, $s0
        # i = i int+ 1
        addiu $s0, $s0, 1
        # t5 = s ptr+ t3
        addu  $s4, $s3, $s2
        # t6 = *t5
        lb    $s5, 0($s4)
        # t7 = chartoint t6
        move  $t0, $s5
        move  $s6, $t0
        # t8 = j
        move  $s7, $s1
        # j = j int- 1
        addiu $s1, $s1, -1
        # t10 = s ptr+ t8
        addu  $t0, $s3, $s7
        sw    $t0, -32($fp)
        # t11 = *t10
        move  $t8, $t0
        lb    $t0, 0($t8)
        sb    $t0, -33($fp)
        # t12 = chartoint t11
        lb    $t0, -33($fp)
        sw    $t0, -40($fp)
        # if t7 int== t12 goto 9
        move  $t1, $t0
        beq   $s6, $t1, L7_9
        # return 0
        li    $v0, 0
        j     _Z12isPalindromePKc_exit
L7_22:
        # return 1
        li    $v0, 1
        j     _Z12isPalindromePKc_exit
_Z12isPalindromePKc_exit:
        lw    $s0, -88($fp)
        lw    $s1, -80($fp)
        lw    $s2, -60($fp)
        lw    $s3, -84($fp)
        lw    $s4, -64($fp)
        lw    $s5, -68($fp)
        lw    $s6, -72($fp)
        lw    $s7, -76($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# countWords(const char *)
_Z10countWordsPKc:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        sw    $s0, -48($fp)
        sw    $s1, -56($fp)
        sw    $s2, -52($fp)
        sw    $s3, -28($fp)
        sw    $s4, -32($fp)
        sw    $s5, -36($fp)
        sw    $s6, -40($fp)
        sw    $s7, -44($fp)
        lw    $s0, 8($fp)
        # words = 0
        li    $s2, 0
        # inside = 0
        li    $s1, 0
L8_2:
        # t1 = *s
        lb    $s3, 0($s0)
        # if t1 char== 0 goto 17
        beq   $s3, $zero, L8_17
        # t2 = *s
        lb    $s4, 0($s0)
        # t3 = chartoint t2
        move  $t0, $s4
        move  $s5, $t0
        # if t3 int== 32 goto 10
        li    $t1, 32
        beq   $s5, $t1, L8_10
        # t4 = *s
        lb    $s6, 0($s0)
        # t5 = chartoint t4
        move  $t0, $s6
        move  $s7, $t0
        # if t5 int!= 9 goto 12
        li    $t1, 9
        bne   $s7, $t1, L8_12
L8_10:
        # inside = 0
        li    $s1, 0
        # goto 15
        j     L8_15
L8_12:
        # if inside int!= 0 goto 15
        bne   $s1, $zero, L8_15
        # inside = 1
        li    $s1, 1
        # words = words int+ 1
        addiu $s2, $s2, 1
L8_15:
        # s = s ptr+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L8_2
L8_17:
        # return words
        move  $v0, $s2
        j     _Z10countWordsPKc_exit
_Z10countWordsPKc_exit:
        lw    $s0, -48($fp)
        lw    $s1, -56($fp)
        lw    $s2, -52($fp)
        lw    $s3, -28($fp)
        lw    $s4, -32($fp)
        lw    $s5, -36($fp)
        lw    $s6, -40($fp)
        lw    $s7, -44($fp)
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
        addiu $sp, $sp, -552
        sw    $s0, -520($fp)
        sw    $s1, -532($fp)
        sw    $s2, -536($fp)
        sw    $s3, -540($fp)
        sw    $s4, -544($fp)
        sw    $s5, -548($fp)
        sw    $s6, -524($fp)
        sw    $s7, -528($fp)
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
L9_6:
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
        bne   $s6, $zero, L9_6
        # t62 = 0
        li    $s1, 0
L9_15:
        # t63 = t1 ptr+ t62
        addu  $s2, $s0, $s1
        # t64 = *t63
        lb    $s3, 0($s2)
        # t65 = chartoint t64
        move  $t0, $s3
        move  $s4, $t0
        # if t65 int== 0 goto 21
        beq   $s4, $zero, L9_21
        # t62 = t62 int+ 1
        addiu $s1, $s1, 1
        # goto 15
        j     L9_15
L9_21:
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
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        jal   _Z6lengthPKc
        addiu $sp, $sp, 8
        move  $s3, $v0
        # t69 = t68 int- 1
        addiu $s2, $s3, -1
L9_29:
        # if t67 int>= t69 goto 39
        bge   $s1, $s2, L9_39
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
        # goto 29
        j     L9_29
L9_39:
        # t76 = 0
        li    $s1, 0
L9_40:
        # t78 = t1 ptr+ t76
        addu  $s2, $s0, $s1
        # t79 = *t78
        lb    $s3, 0($s2)
        # if t79 char== 0 goto 50
        beq   $s3, $zero, L9_50
        # t80 = *t78
        lb    $s4, 0($s2)
        # t81 = chartoint t80
        move  $t0, $s4
        move  $s5, $t0
        # if t81 int!= 112 goto 48
        li    $t1, 112
        bne   $s5, $t1, L9_48
        # t8 = t76
        move  $s6, $s1
        # goto 51
        j     L9_51
L9_48:
        # t76 = t76 int+ 1
        addiu $s1, $s1, 1
        # goto 40
        j     L9_40
L9_50:
        # t8 = -1
        li    $s6, -1
L9_51:
        # t84 = 0
        li    $s1, 0
L9_52:
        # t86 = t1 ptr+ t84
        addu  $s2, $s0, $s1
        # t87 = *t86
        lb    $s3, 0($s2)
        # if t87 char== 0 goto 62
        beq   $s3, $zero, L9_62
        # t88 = *t86
        lb    $s4, 0($s2)
        # t89 = chartoint t88
        move  $t0, $s4
        move  $s5, $t0
        # if t89 int!= 122 goto 60
        li    $t1, 122
        bne   $s5, $t1, L9_60
        # t10 = t84
        move  $s7, $s1
        # goto 63
        j     L9_63
L9_60:
        # t84 = t84 int+ 1
        addiu $s1, $s1, 1
        # goto 52
        j     L9_52
L9_62:
        # t10 = -1
        li    $s7, -1
L9_63:
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
L9_70:
        # t92 = *t90
        lb    $s2, 0($s0)
        # if t92 char== 0 goto 80
        beq   $s2, $zero, L9_80
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
        # if t94 int!= t96 goto 80
        bne   $s4, $s6, L9_80
        # t90 = t90 ptr+ 1
        addiu $s0, $s0, 1
        # t91 = t91 ptr+ 1
        addiu $s1, $s1, 1
        # goto 70
        j     L9_70
L9_80:
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
        # if t101 int< 0 goto 88
        slt   $s7, $s2, $zero
L9_89:
        # t102 = "abc"
        la    $s0, str7
        # t103 = "abc"
        la    $s1, str7
L9_91:
        # t104 = *t102
        lb    $s2, 0($s0)
        # if t104 char== 0 goto 101
        beq   $s2, $zero, L9_101
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
        # if t106 int!= t108 goto 101
        bne   $s4, $s6, L9_101
        # t102 = t102 ptr+ 1
        addiu $s0, $s0, 1
        # t103 = t103 ptr+ 1
        addiu $s1, $s1, 1
        # goto 91
        j     L9_91
L9_101:
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
        sw    $t0, -100($fp)
        # t114 = "b"
        la    $s0, str9
        # t115 = "abc"
        la    $s1, str7
L9_108:
        # t116 = *t114
        lb    $s2, 0($s0)
        # if t116 char== 0 goto 118
        beq   $s2, $zero, L9_118
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
        # if t118 int!= t120 goto 118
        bne   $s4, $s6, L9_118
        # t114 = t114 ptr+ 1
        addiu $s0, $s0, 1
        # t115 = t115 ptr+ 1
        addiu $s1, $s1, 1
        # goto 108
        j     L9_108
L9_118:
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
        # if t125 int> 0 goto 126
        slt   $s0, $zero, $s2
L9_127:
        # param "%d %d %d\n"
        # param t11
        # param t13
        # param t14
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s7, 4($sp)
        lw    $t0, -100($fp)
        sw    $t0, 8($sp)
        sw    $s0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # smallest = 0
        li    $t0, 0
        sw    $t0, -64($fp)
        # i.32 = 1
        li    $s7, 1
L9_134:
        # if i.32 int>= 3 goto 160
        li    $t1, 3
        bge   $s7, $t1, L9_160
        # t16 = i.32 int<< 2
        sll   $t0, $s7, 2
        sw    $t0, -108($fp)
        # t17 = names[t16]
        addiu $t8, $fp, -60
        lw    $t9, -108($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -112($fp)
        # t18 = smallest int<< 2
        lw    $t0, -64($fp)
        sll   $t0, $t0, 2
        sw    $t0, -116($fp)
        # t19 = names[t18]
        addiu $t8, $fp, -60
        lw    $t9, -116($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -120($fp)
        # t126 = t17
        lw    $s0, -112($fp)
        # t127 = t19
        lw    $s1, -120($fp)
L9_141:
        # t128 = *t126
        lb    $s2, 0($s0)
        # if t128 char== 0 goto 151
        beq   $s2, $zero, L9_151
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
        # if t130 int!= t132 goto 151
        bne   $s4, $s6, L9_151
        # t126 = t126 ptr+ 1
        addiu $s0, $s0, 1
        # t127 = t127 ptr+ 1
        addiu $s1, $s1, 1
        # goto 141
        j     L9_141
L9_151:
        # t133 = *t126
        lb    $t0, 0($s0)
        sb    $t0, -477($fp)
        # t134 = chartoint t133
        lb    $t0, -477($fp)
        sw    $t0, -484($fp)
        # t135 = *t127
        lb    $t0, 0($s1)
        sb    $t0, -485($fp)
        # t136 = chartoint t135
        lb    $t0, -485($fp)
        sw    $t0, -492($fp)
        # t137 = t134 int- t136
        lw    $t0, -484($fp)
        lw    $t1, -492($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -496($fp)
        # if t137 int>= 0 goto 158
        bge   $t0, $zero, L9_158
        # smallest = i.32
        move  $t0, $s7
        sw    $t0, -64($fp)
L9_158:
        # i.32 = i.32 int+ 1
        addiu $s7, $s7, 1
        # goto 134
        j     L9_134
L9_160:
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
        addiu $sp, $sp, -8
        li    $t0, -40213
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   _Z6toTextiPc
        addiu $sp, $sp, 8
        # param t29
        # t32 = call toNumber(const char *), 1
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        jal   _Z8toNumberPKc
        addiu $sp, $sp, 8
        move  $s1, $v0
        # t33 = t32 int+ 1
        addiu $s2, $s1, 1
        # param "77x"
        # t34 = call toNumber(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str11
        sw    $t0, 0($sp)
        jal   _Z8toNumberPKc
        addiu $sp, $sp, 8
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
        addiu $sp, $sp, -8
        la    $t0, str12
        sw    $t0, 0($sp)
        jal   _Z12isPalindromePKc
        addiu $sp, $sp, 8
        move  $s0, $v0
        # param "lever"
        # t36 = call isPalindrome(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str13
        sw    $t0, 0($sp)
        jal   _Z12isPalindromePKc
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param "  the quick  brown fox "
        # t37 = call countWords(const char *), 1
        addiu $sp, $sp, -8
        la    $t0, str14
        sw    $t0, 0($sp)
        jal   _Z10countWordsPKc
        addiu $sp, $sp, 8
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
        sb    $t0, -76($fp)
        # upper[1] = 105
        li    $t0, 105
        sb    $t0, -75($fp)
        # upper[2] = 120
        li    $t0, 120
        sb    $t0, -74($fp)
        # upper[3] = 101
        li    $t0, 101
        sb    $t0, -73($fp)
        # upper[4] = 100
        li    $t0, 100
        sb    $t0, -72($fp)
        # upper[5] = 0
        sb    $zero, -71($fp)
        # upper[6] = 0
        sb    $zero, -70($fp)
        # upper[7] = 0
        sb    $zero, -69($fp)
        # i.34 = 0
        li    $s0, 0
L9_204:
        # t38 = upper[i.34]
        addiu $t8, $fp, -76
        addu  $t8, $t8, $s0
        lb    $s1, 0($t8)
        # if t38 char== 0 goto 220
        beq   $s1, $zero, L9_220
        # t39 = upper[i.34]
        addiu $t8, $fp, -76
        addu  $t8, $t8, $s0
        lb    $s2, 0($t8)
        # t40 = chartoint t39
        move  $t0, $s2
        move  $s3, $t0
        # if t40 int< 97 goto 218
        li    $t1, 97
        blt   $s3, $t1, L9_218
        # t41 = upper[i.34]
        addiu $t8, $fp, -76
        addu  $t8, $t8, $s0
        lb    $s4, 0($t8)
        # t42 = chartoint t41
        move  $t0, $s4
        move  $s5, $t0
        # if t42 int> 122 goto 218
        li    $t1, 122
        bgt   $s5, $t1, L9_218
        # t43 = upper[i.34]
        addiu $t8, $fp, -76
        addu  $t8, $t8, $s0
        lb    $s6, 0($t8)
        # t44 = chartoint t43
        move  $t0, $s6
        move  $s7, $t0
        # t45 = t44 int- 97
        addiu $t0, $s7, -97
        sw    $t0, -200($fp)
        # t46 = t45 int+ 65
        addiu $t0, $t0, 65
        sw    $t0, -204($fp)
        # t47 = inttochar t46
        sb    $t0, -205($fp)
        # upper[i.34] = t47
        addiu $t8, $fp, -76
        addu  $t8, $t8, $s0
        lb    $t0, -205($fp)
        sb    $t0, 0($t8)
L9_218:
        # i.34 = i.34 int+ 1
        addiu $s0, $s0, 1
        # goto 204
        j     L9_204
L9_220:
        # t49 = &upper
        addiu $s0, $fp, -76
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
L9_227:
        # t140 = t138 ptr+ t139
        addu  $s1, $s4, $s0
        # t141 = *t140
        lb    $s2, 0($s1)
        # t142 = chartoint t141
        move  $t0, $s2
        move  $s3, $t0
        # if t142 int== 0 goto 233
        beq   $s3, $zero, L9_233
        # t139 = t139 int+ 1
        addiu $s0, $s0, 1
        # goto 227
        j     L9_227
L9_233:
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
        lw    $s0, -520($fp)
        lw    $s1, -532($fp)
        lw    $s2, -536($fp)
        lw    $s3, -540($fp)
        lw    $s4, -544($fp)
        lw    $s5, -548($fp)
        lw    $s6, -524($fp)
        lw    $s7, -528($fp)
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
