# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t18_algorithms.c
#  Optimization : -O2 (TAC optimizations, registers, peephole)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g_moves:
        .byte 0, 0, 0, 0
str0:
        .byte 37, 100, 32, 0
str1:
        .byte 10, 0
str2:
        .byte 10, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str3:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str4:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0

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

# bubble(int *, int)
_Z6bubblePii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -112
        sw    $s0, -108($fp)
        sw    $s1, -112($fp)
        sw    $s2, -100($fp)
        sw    $s3, -104($fp)
        sw    $s4, -84($fp)
        sw    $s5, -88($fp)
        sw    $s6, -92($fp)
        sw    $s7, -96($fp)
        lw    $s1, 8($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L0_1:
        # t1 = n int- 1
        lw    $t0, 12($fp)
        addiu $t0, $t0, -1
        sw    $t0, -16($fp)
        # if i int>= t1 goto 28
        lw    $t0, -4($fp)
        lw    $t1, -16($fp)
        bge   $t0, $t1, L0_28
        # j = 0
        li    $s0, 0
L0_4:
        # t2 = n int- 1
        lw    $t0, 12($fp)
        addiu $s4, $t0, -1
        # t3 = t2 int- i
        lw    $t1, -4($fp)
        subu  $s5, $s4, $t1
        # if j int>= t3 goto 26
        bge   $s0, $s5, L0_26
        # t4 = j int<< 2
        sll   $s6, $s0, 2
        # t5 = a ptr+ t4
        addu  $s7, $s1, $s6
        # t6 = *t5
        lw    $t0, 0($s7)
        sw    $t0, -36($fp)
        # t7 = j int+ 1
        addiu $t0, $s0, 1
        sw    $t0, -40($fp)
        # t8 = t7 int<< 2
        sll   $t0, $t0, 2
        sw    $t0, -44($fp)
        # t9 = a ptr+ t8
        move  $t1, $t0
        addu  $t0, $s1, $t1
        sw    $t0, -48($fp)
        # t10 = *t9
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -52($fp)
        # if t6 int<= t10 goto 24
        lw    $t0, -36($fp)
        lw    $t1, -52($fp)
        ble   $t0, $t1, L0_24
        # t11 = j int<< 2
        sll   $t0, $s0, 2
        sw    $t0, -56($fp)
        # t12 = a ptr+ t11
        move  $t1, $t0
        addu  $s2, $s1, $t1
        # t13 = *t12
        lw    $t0, 0($s2)
        sw    $t0, -64($fp)
        # t16 = j int+ 1
        addiu $t0, $s0, 1
        sw    $t0, -68($fp)
        # t17 = t16 int<< 2
        sll   $t0, $t0, 2
        sw    $t0, -72($fp)
        # t18 = a ptr+ t17
        move  $t1, $t0
        addu  $s3, $s1, $t1
        # t19 = *t18
        lw    $t0, 0($s3)
        sw    $t0, -80($fp)
        # *t12 = t19
        sw    $t0, 0($s2)
        # *t18 = t13
        lw    $t0, -64($fp)
        sw    $t0, 0($s3)
L0_24:
        # j = j int+ 1
        addiu $s0, $s0, 1
        # goto 4
        j     L0_4
L0_26:
        # i = i int+ 1
        lw    $t0, -4($fp)
        addiu $t0, $t0, 1
        sw    $t0, -4($fp)
        # goto 1
        j     L0_1
L0_28:
        # return
        j     _Z6bubblePii_exit
_Z6bubblePii_exit:
        lw    $s0, -108($fp)
        lw    $s1, -112($fp)
        lw    $s2, -100($fp)
        lw    $s3, -104($fp)
        lw    $s4, -84($fp)
        lw    $s5, -88($fp)
        lw    $s6, -92($fp)
        lw    $s7, -96($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# quick(int *, int, int)
_Z5quickPiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -112
        sw    $s0, -84($fp)
        sw    $s1, -88($fp)
        sw    $s2, -112($fp)
        sw    $s3, -108($fp)
        sw    $s4, -92($fp)
        sw    $s5, -96($fp)
        sw    $s6, -100($fp)
        sw    $s7, -104($fp)
        lw    $s2, 8($fp)
        # if lo int< hi goto 2
        lw    $t0, 12($fp)
        lw    $t1, 16($fp)
        blt   $t0, $t1, L1_2
        # return
        j     _Z5quickPiii_exit
L1_2:
        # t1 = lo int+ hi
        lw    $t0, 12($fp)
        lw    $t1, 16($fp)
        addu  $s0, $t0, $t1
        # t2 = t1 int/ 2
        li    $t1, 2
        div   $s0, $t1
        mflo  $s1
        # t3 = t2 int<< 2
        sll   $s0, $s1, 2
        # t4 = a ptr+ t3
        addu  $s1, $s2, $s0
        # pivot = *t4
        lw    $s3, 0($s1)
        # i = lo
        lw    $s0, 12($fp)
        # j = hi
        lw    $s1, 16($fp)
L1_9:
        # if i int> j goto 34
        bgt   $s0, $s1, L1_34
L1_10:
        # t6 = i int<< 2
        sll   $s4, $s0, 2
        # t7 = a ptr+ t6
        addu  $s5, $s2, $s4
        # t8 = *t7
        lw    $s6, 0($s5)
        # if t8 int>= pivot goto 16
        bge   $s6, $s3, L1_16
        # i = i int+ 1
        addiu $s0, $s0, 1
        # goto 10
        j     L1_10
L1_16:
        # t10 = j int<< 2
        sll   $s7, $s1, 2
        # t11 = a ptr+ t10
        addu  $t0, $s2, $s7
        sw    $t0, -52($fp)
        # t12 = *t11
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -56($fp)
        # if t12 int<= pivot goto 22
        ble   $t0, $s3, L1_22
        # j = j int- 1
        addiu $s1, $s1, -1
        # goto 16
        j     L1_16
L1_22:
        # if i int> j goto 9
        bgt   $s0, $s1, L1_9
        # t14 = i int<< 2
        sll   $t0, $s0, 2
        sw    $t0, -60($fp)
        # t15 = a ptr+ t14
        move  $t1, $t0
        addu  $t0, $s2, $t1
        sw    $t0, -64($fp)
        # t16 = *t15
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -68($fp)
        # t19 = j int<< 2
        sll   $t0, $s1, 2
        sw    $t0, -72($fp)
        # t20 = a ptr+ t19
        move  $t1, $t0
        addu  $t0, $s2, $t1
        sw    $t0, -76($fp)
        # t21 = *t20
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -80($fp)
        # *t15 = t21
        lw    $t8, -64($fp)
        lw    $t0, -80($fp)
        sw    $t0, 0($t8)
        # *t20 = t16
        lw    $t8, -76($fp)
        lw    $t0, -68($fp)
        sw    $t0, 0($t8)
        # i = i int+ 1
        addiu $s0, $s0, 1
        # j = j int- 1
        addiu $s1, $s1, -1
        # goto 9
        j     L1_9
L1_34:
        # param a
        # param lo
        # param j
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s2, 0($sp)
        lw    $t0, 12($fp)
        sw    $t0, 4($sp)
        sw    $s1, 8($sp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # param a
        # param i
        # param hi
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s2, 0($sp)
        sw    $s0, 4($sp)
        lw    $t0, 16($fp)
        sw    $t0, 8($sp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # return
        j     _Z5quickPiii_exit
_Z5quickPiii_exit:
        lw    $s0, -84($fp)
        lw    $s1, -88($fp)
        lw    $s2, -112($fp)
        lw    $s3, -108($fp)
        lw    $s4, -92($fp)
        lw    $s5, -96($fp)
        lw    $s6, -100($fp)
        lw    $s7, -104($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# search(int *, int, int)
_Z6searchPiii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -80
        sw    $s0, -60($fp)
        sw    $s1, -76($fp)
        sw    $s2, -80($fp)
        sw    $s3, -52($fp)
        sw    $s4, -56($fp)
        sw    $s5, -64($fp)
        sw    $s6, -68($fp)
        sw    $s7, -72($fp)
        lw    $s0, 12($fp)
        # lo = 0
        li    $s1, 0
        # hi = n int- 1
        addiu $s2, $s0, -1
L2_2:
        # if lo int> hi goto 19
        bgt   $s1, $s2, L2_19
        # t2 = hi int- lo
        subu  $s3, $s2, $s1
        # t3 = t2 int/ 2
        li    $t1, 2
        div   $s3, $t1
        mflo  $s4
        # t4 = lo int+ t3
        addu  $s0, $s1, $s4
        # t5 = t4 int<< 2
        sll   $s5, $s0, 2
        # t6 = a ptr+ t5
        lw    $t0, 8($fp)
        addu  $s6, $t0, $s5
        # t7 = *t6
        lw    $s7, 0($s6)
        # if t7 int!= key goto 11
        lw    $t1, 16($fp)
        bne   $s7, $t1, L2_11
        # return t4
        move  $v0, $s0
        j     _Z6searchPiii_exit
L2_11:
        # t8 = t4 int<< 2
        sll   $t0, $s0, 2
        sw    $t0, -40($fp)
        # t9 = a ptr+ t8
        lw    $t0, 8($fp)
        lw    $t1, -40($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t10 = *t9
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -48($fp)
        # if t10 int>= key goto 17
        lw    $t1, 16($fp)
        bge   $t0, $t1, L2_17
        # lo = t4 int+ 1
        addiu $s1, $s0, 1
        # goto 2
        j     L2_2
L2_17:
        # hi = t4 int- 1
        addiu $s2, $s0, -1
        # goto 2
        j     L2_2
L2_19:
        # return -1
        li    $v0, -1
        j     _Z6searchPiii_exit
_Z6searchPiii_exit:
        lw    $s0, -60($fp)
        lw    $s1, -76($fp)
        lw    $s2, -80($fp)
        lw    $s3, -52($fp)
        lw    $s4, -56($fp)
        lw    $s5, -64($fp)
        lw    $s6, -68($fp)
        lw    $s7, -72($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# hanoi(int, int, int, int)
_Z5hanoiiiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -8($fp)
        sw    $s1, -12($fp)
        sw    $s2, -16($fp)
        sw    $s3, -20($fp)
        sw    $s4, -24($fp)
        lw    $s1, 8($fp)
        lw    $s2, 12($fp)
        lw    $s3, 16($fp)
        lw    $s4, 20($fp)
        # if n int!= 0 goto 2
        bne   $s1, $zero, L3_2
        # return
        j     _Z5hanoiiiii_exit
L3_2:
        # t1 = n int- 1
        addiu $s0, $s1, -1
        # param t1
        # param from
        # param via
        # param to
        # call hanoi(int, int, int, int), 4
        addiu $sp, $sp, -16
        sw    $s0, 0($sp)
        sw    $s2, 4($sp)
        sw    $s4, 8($sp)
        sw    $s3, 12($sp)
        jal   _Z5hanoiiiii
        addiu $sp, $sp, 16
        # moves = moves int+ 1
        lw    $t0, g_moves
        addiu $t0, $t0, 1
        sw    $t0, g_moves
        # param t1
        # param via
        # param to
        # param from
        # call hanoi(int, int, int, int), 4
        addiu $sp, $sp, -16
        sw    $s0, 0($sp)
        sw    $s4, 4($sp)
        sw    $s3, 8($sp)
        sw    $s2, 12($sp)
        jal   _Z5hanoiiiii
        addiu $sp, $sp, 16
        # return
        j     _Z5hanoiiiii_exit
_Z5hanoiiiii_exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        lw    $s2, -16($fp)
        lw    $s3, -20($fp)
        lw    $s4, -24($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# ackermann(int, int)
_Z9ackermannii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -44($fp)
        sw    $s1, -40($fp)
        sw    $s2, -32($fp)
        sw    $s3, -36($fp)
        lw    $s0, 8($fp)
        lw    $s1, 12($fp)
        # if m int!= 0 goto 3
        bne   $s0, $zero, L4_3
        # t1 = n int+ 1
        addiu $s2, $s1, 1
        # return t1
        move  $v0, $s2
        j     _Z9ackermannii_exit
L4_3:
        # if n int!= 0 goto 9
        bne   $s1, $zero, L4_9
        # t2 = m int- 1
        addiu $s2, $s0, -1
        # param t2
        # param 1
        # t3 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        sw    $s2, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        move  $s3, $v0
        # return t3
        move  $v0, $s3
        j     _Z9ackermannii_exit
L4_9:
        # t4 = m int- 1
        addiu $s2, $s0, -1
        # t5 = n int- 1
        addiu $s3, $s1, -1
        # param m
        # param t5
        # t6 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        sw    $s3, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param t4
        # param t6
        # t7 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        sw    $s2, 0($sp)
        sw    $s1, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        move  $s0, $v0
        # return t7
        move  $v0, $s0
        j     _Z9ackermannii_exit
_Z9ackermannii_exit:
        lw    $s0, -44($fp)
        lw    $s1, -40($fp)
        lw    $s2, -32($fp)
        lw    $s3, -36($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# multiply(int (*)[3], int (*)[2], int (*)[2])
_Z8multiplyPA3_iPA2_iS2_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -128
        sw    $s0, -124($fp)
        sw    $s1, -104($fp)
        sw    $s2, -108($fp)
        sw    $s3, -120($fp)
        sw    $s4, -96($fp)
        sw    $s5, -100($fp)
        sw    $s6, -112($fp)
        sw    $s7, -116($fp)
        # i = 0
        li    $s3, 0
L5_1:
        # if i int>= 2 goto 34
        li    $t1, 2
        bge   $s3, $t1, L5_34
        # j = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L5_3:
        # if j int>= 2 goto 32
        lw    $t0, -8($fp)
        li    $t1, 2
        bge   $t0, $t1, L5_32
        # t1 = i int<< 3
        sll   $t0, $s3, 3
        sw    $t0, -16($fp)
        # t2 = c ptr+ t1
        lw    $t0, 16($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t3 = j int<< 2
        lw    $t0, -8($fp)
        sll   $t0, $t0, 2
        sw    $t0, -24($fp)
        # t4 = t2 ptr+ t3
        lw    $t0, -20($fp)
        lw    $t1, -24($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # *t4 = 0
        move  $t8, $t0
        sw    $zero, 0($t8)
        # k = 0
        li    $s0, 0
L5_10:
        # if k int>= 3 goto 30
        li    $t1, 3
        bge   $s0, $t1, L5_30
        # t5 = i int<< 3
        sll   $s4, $s3, 3
        # t6 = c ptr+ t5
        lw    $t0, 16($fp)
        addu  $s5, $t0, $s4
        # t7 = j int<< 2
        lw    $t0, -8($fp)
        sll   $s1, $t0, 2
        # t8 = t6 ptr+ t7
        addu  $s2, $s5, $s1
        # t9 = *t8
        lw    $s6, 0($s2)
        # t10 = i int* 12
        li    $t1, 12
        mul   $s7, $s3, $t1
        # t11 = a ptr+ t10
        lw    $t0, 8($fp)
        addu  $t0, $t0, $s7
        sw    $t0, -56($fp)
        # t12 = k int<< 2
        sll   $t0, $s0, 2
        sw    $t0, -60($fp)
        # t13 = t11 ptr+ t12
        lw    $t0, -56($fp)
        lw    $t1, -60($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -64($fp)
        # t14 = *t13
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -68($fp)
        # t15 = k int<< 3
        sll   $t0, $s0, 3
        sw    $t0, -72($fp)
        # t16 = b ptr+ t15
        lw    $t0, 12($fp)
        lw    $t1, -72($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # t18 = t16 ptr+ t7
        addu  $t0, $t0, $s1
        sw    $t0, -80($fp)
        # t19 = *t18
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -84($fp)
        # t20 = t14 int* t19
        lw    $t0, -68($fp)
        lw    $t1, -84($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -88($fp)
        # t21 = t9 int+ t20
        move  $t1, $t0
        addu  $t0, $s6, $t1
        sw    $t0, -92($fp)
        # *t8 = t21
        sw    $t0, 0($s2)
        # k = k int+ 1
        addiu $s0, $s0, 1
        # goto 10
        j     L5_10
L5_30:
        # j = j int+ 1
        lw    $t0, -8($fp)
        addiu $t0, $t0, 1
        sw    $t0, -8($fp)
        # goto 3
        j     L5_3
L5_32:
        # i = i int+ 1
        addiu $s3, $s3, 1
        # goto 1
        j     L5_1
L5_34:
        # return
        j     _Z8multiplyPA3_iPA2_iS2__exit
_Z8multiplyPA3_iPA2_iS2__exit:
        lw    $s0, -124($fp)
        lw    $s1, -104($fp)
        lw    $s2, -108($fp)
        lw    $s3, -120($fp)
        lw    $s4, -96($fp)
        lw    $s5, -100($fp)
        lw    $s6, -112($fp)
        lw    $s7, -116($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# primes(int)
_Z6primesi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -144
        sw    $s0, -136($fp)
        sw    $s1, -132($fp)
        sw    $s2, -140($fp)
        sw    $s3, -144($fp)
        sw    $s4, -128($fp)
        lw    $s2, 8($fp)
        # count = 0
        li    $s3, 0
        # i.34 = 0
        li    $s0, 0
L6_2:
        # if i.34 int> limit goto 6
        bgt   $s0, $s2, L6_6
        # composite[i.34] = 0
        addiu $t8, $fp, -101
        addu  $t8, $t8, $s0
        sb    $zero, 0($t8)
        # i.34 = i.34 int+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L6_2
L6_6:
        # i.35 = 2
        li    $s1, 2
L6_7:
        # if i.35 int> limit goto 18
        bgt   $s1, $s2, L6_18
        # t2 = composite[i.35]
        addiu $t8, $fp, -101
        addu  $t8, $t8, $s1
        lb    $s4, 0($t8)
        # if t2 char!= 0 goto 16
        bne   $s4, $zero, L6_16
        # count = count int+ 1
        addiu $s3, $s3, 1
        # j = i.35 int* i.35
        mul   $s0, $s1, $s1
L6_12:
        # if j int> limit goto 16
        bgt   $s0, $s2, L6_16
        # composite[j] = 1
        addiu $t8, $fp, -101
        addu  $t8, $t8, $s0
        li    $t0, 1
        sb    $t0, 0($t8)
        # j = j int+ i.35
        addu  $s0, $s0, $s1
        # goto 12
        j     L6_12
L6_16:
        # i.35 = i.35 int+ 1
        addiu $s1, $s1, 1
        # goto 7
        j     L6_7
L6_18:
        # return count
        move  $v0, $s3
        j     _Z6primesi_exit
_Z6primesi_exit:
        lw    $s0, -136($fp)
        lw    $s1, -132($fp)
        lw    $s2, -140($fp)
        lw    $s3, -144($fp)
        lw    $s4, -128($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# power(int, int)
_Z5powerii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -16($fp)
        sw    $s1, -20($fp)
        sw    $s2, -24($fp)
        sw    $s3, -12($fp)
        lw    $s0, 8($fp)
        lw    $s1, 12($fp)
        # result = 1
        li    $s2, 1
L7_1:
        # if exp int<= 0 goto 8
        ble   $s1, $zero, L7_8
        # t1 = exp int& 1
        andi  $s3, $s1, 1
        # if t1 int== 0 goto 5
        beq   $s3, $zero, L7_5
        # result = result int* base
        mul   $s2, $s2, $s0
L7_5:
        # base = base int* base
        mul   $s0, $s0, $s0
        # exp = exp int>> 1
        sra   $s1, $s1, 1
        # goto 1
        j     L7_1
L7_8:
        # return result
        move  $v0, $s2
        j     _Z5powerii_exit
_Z5powerii_exit:
        lw    $s0, -16($fp)
        lw    $s1, -20($fp)
        lw    $s2, -24($fp)
        lw    $s3, -12($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# collatz(int)
_Z7collatzi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        sw    $s0, -32($fp)
        sw    $s1, -20($fp)
        sw    $s2, -36($fp)
        sw    $s3, -24($fp)
        sw    $s4, -28($fp)
        lw    $s0, 8($fp)
        # steps = 0
        li    $s2, 0
L8_1:
        # if n int== 1 goto 11
        li    $t1, 1
        beq   $s0, $t1, L8_11
        # t2 = n int% 2
        li    $t1, 2
        div   $s0, $t1
        mfhi  $s3
        # if t2 int== 0 goto 7
        beq   $s3, $zero, L8_7
        # t3 = n int* 3
        li    $t1, 3
        mul   $s4, $s0, $t1
        # t1 = t3 int+ 1
        addiu $s1, $s4, 1
        # goto 8
        j     L8_8
L8_7:
        # t1 = n int/ 2
        li    $t1, 2
        div   $s0, $t1
        mflo  $s1
L8_8:
        # n = t1
        move  $s0, $s1
        # steps = steps int+ 1
        addiu $s2, $s2, 1
        # goto 1
        j     L8_1
L8_11:
        # return steps
        move  $v0, $s2
        j     _Z7collatzi_exit
_Z7collatzi_exit:
        lw    $s0, -32($fp)
        lw    $s1, -20($fp)
        lw    $s2, -36($fp)
        lw    $s3, -24($fp)
        lw    $s4, -28($fp)
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
        addiu $sp, $sp, -256
        sw    $s0, -236($fp)
        sw    $s1, -240($fp)
        sw    $s2, -244($fp)
        sw    $s3, -248($fp)
        sw    $s4, -252($fp)
        # a[0] = 42
        li    $t0, 42
        sw    $t0, -32($fp)
        # a[4] = 7
        li    $t0, 7
        sw    $t0, -28($fp)
        # a[8] = 19
        li    $t0, 19
        sw    $t0, -24($fp)
        # a[12] = 3
        li    $t0, 3
        sw    $t0, -20($fp)
        # a[16] = 25
        li    $t0, 25
        sw    $t0, -16($fp)
        # a[20] = 7
        li    $t0, 7
        sw    $t0, -12($fp)
        # a[24] = 88
        li    $t0, 88
        sw    $t0, -8($fp)
        # a[28] = 1
        li    $t0, 1
        sw    $t0, -4($fp)
        # b[0] = 5
        li    $t0, 5
        sw    $t0, -64($fp)
        # b[4] = -2
        li    $t0, -2
        sw    $t0, -60($fp)
        # b[8] = 9
        li    $t0, 9
        sw    $t0, -56($fp)
        # b[12] = 0
        sw    $zero, -52($fp)
        # b[16] = 9
        li    $t0, 9
        sw    $t0, -48($fp)
        # b[20] = 14
        li    $t0, 14
        sw    $t0, -44($fp)
        # b[24] = -7
        li    $t0, -7
        sw    $t0, -40($fp)
        # b[28] = 3
        li    $t0, 3
        sw    $t0, -36($fp)
        # t3 = &a
        addiu $s0, $fp, -32
        # param t3
        # param 8
        # call bubble(int *, int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        jal   _Z6bubblePii
        addiu $sp, $sp, 8
        # t4 = &b
        addiu $s0, $fp, -64
        # param t4
        # param 0
        # param 7
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s0, 0($sp)
        sw    $zero, 4($sp)
        li    $t0, 7
        sw    $t0, 8($sp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # i.44 = 0
        li    $s0, 0
L9_26:
        # if i.44 int>= 8 goto 34
        li    $t1, 8
        bge   $s0, $t1, L9_34
        # t5 = i.44 int<< 2
        sll   $s1, $s0, 2
        # t6 = a[t5]
        addiu $t8, $fp, -32
        addu  $t8, $t8, $s1
        lw    $s2, 0($t8)
        # param "%d "
        # param t6
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i.44 = i.44 int+ 1
        addiu $s0, $s0, 1
        # goto 26
        j     L9_26
L9_34:
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i.45 = 0
        li    $s0, 0
L9_37:
        # if i.45 int>= 8 goto 45
        li    $t1, 8
        bge   $s0, $t1, L9_45
        # t8 = i.45 int<< 2
        sll   $s1, $s0, 2
        # t9 = b[t8]
        addiu $t8, $fp, -64
        addu  $t8, $t8, $s1
        lw    $s2, 0($t8)
        # param "%d "
        # param t9
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i.45 = i.45 int+ 1
        addiu $s0, $s0, 1
        # goto 37
        j     L9_37
L9_45:
        # t11 = &a
        addiu $s0, $fp, -32
        # param t11
        # param 8
        # param 25
        # t12 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, 25
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        move  $s1, $v0
        # param t11
        # param 8
        # param 26
        # t14 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, 26
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        move  $s2, $v0
        # t15 = &b
        addiu $s3, $fp, -64
        # param t15
        # param 8
        # param -7
        # t17 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s3, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, -7
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        move  $s4, $v0
        # param "\n%d %d %d\n"
        # param t12
        # param t14
        # param t17
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s4, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 6
        # param 1
        # param 3
        # param 2
        # call hanoi(int, int, int, int), 4
        addiu $sp, $sp, -16
        li    $t0, 6
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        li    $t0, 3
        sw    $t0, 8($sp)
        li    $t0, 2
        sw    $t0, 12($sp)
        jal   _Z5hanoiiiii
        addiu $sp, $sp, 16
        # param 2
        # param 3
        # t18 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param 27
        # t19 = call collatz(int), 1
        addiu $sp, $sp, -8
        li    $t0, 27
        sw    $t0, 0($sp)
        jal   _Z7collatzi
        addiu $sp, $sp, 8
        move  $s2, $v0
        # param "%d %d %d\n"
        # param moves
        # param t18
        # param t19
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, g_moves
        sw    $t0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # x[0] = 1
        li    $t0, 1
        sw    $t0, -96($fp)
        # x[4] = 2
        li    $t0, 2
        sw    $t0, -92($fp)
        # x[8] = 3
        li    $t0, 3
        sw    $t0, -88($fp)
        # x[12] = 4
        li    $t0, 4
        sw    $t0, -84($fp)
        # x[16] = 5
        li    $t0, 5
        sw    $t0, -80($fp)
        # x[20] = 6
        li    $t0, 6
        sw    $t0, -76($fp)
        # y[0] = 7
        li    $t0, 7
        sw    $t0, -120($fp)
        # y[4] = 8
        li    $t0, 8
        sw    $t0, -116($fp)
        # y[8] = 9
        li    $t0, 9
        sw    $t0, -112($fp)
        # y[12] = 10
        li    $t0, 10
        sw    $t0, -108($fp)
        # y[16] = 11
        li    $t0, 11
        sw    $t0, -104($fp)
        # y[20] = 12
        li    $t0, 12
        sw    $t0, -100($fp)
        # t20 = &x
        addiu $s1, $fp, -96
        # t21 = &y
        addiu $s2, $fp, -120
        # t22 = &z
        addiu $s3, $fp, -136
        # param t20
        # param t21
        # param t22
        # call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
        addiu $sp, $sp, -16
        sw    $s1, 0($sp)
        sw    $s2, 4($sp)
        sw    $s3, 8($sp)
        jal   _Z8multiplyPA3_iPA2_iS2_
        addiu $sp, $sp, 16
        # t23 = z[0]
        lw    $s1, -136($fp)
        # t24 = z[4]
        lw    $s2, -132($fp)
        # t25 = z[8]
        lw    $s3, -128($fp)
        # t26 = z[12]
        lw    $s4, -124($fp)
        # param "%d %d %d %d\n"
        # param t23
        # param t24
        # param t25
        # param t26
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        sw    $s4, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 100
        # t27 = call primes(int), 1
        addiu $sp, $sp, -8
        li    $t0, 100
        sw    $t0, 0($sp)
        jal   _Z6primesi
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param 3
        # param 13
        # t28 = call power(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        li    $t0, 13
        sw    $t0, 4($sp)
        jal   _Z5powerii
        addiu $sp, $sp, 8
        move  $s2, $v0
        # param 2
        # param 10
        # t29 = call power(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        li    $t0, 10
        sw    $t0, 4($sp)
        jal   _Z5powerii
        addiu $sp, $sp, 8
        move  $s3, $v0
        # param "%d %d %d\n"
        # param t27
        # param t28
        # param t29
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param t11
        # param 8
        # param 88
        # t31 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        sw    $s0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, 88
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        move  $s1, $v0
        # return t31
        move  $v0, $s1
        j     main__exit
main__exit:
        lw    $s0, -236($fp)
        lw    $s1, -240($fp)
        lw    $s2, -244($fp)
        lw    $s3, -248($fp)
        lw    $s4, -252($fp)
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
