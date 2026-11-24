# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t17_algorithms.c
#  Optimization : -O2 (TAC optimizations, registers, peephole)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37
        .byte 100, 10, 0
str1:
        .byte 37, 100, 32, 37, 100, 10, 0
str2:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str3:
        .byte 37, 100, 32, 37, 115, 32, 37, 100, 10, 0

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

# bubble(int *, int)
_Z6bubblePii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -80
        sw    $s0, -76($fp)
        sw    $s1, -72($fp)
        sw    $s2, -64($fp)
        sw    $s3, -68($fp)
        sw    $s4, -48($fp)
        sw    $s5, -52($fp)
        sw    $s6, -56($fp)
        sw    $s7, -60($fp)
        move  $s1, $a0
        sw    $a1, 12($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L0_1:
        # if i int>= n goto 27
        lw    $t0, -4($fp)
        lw    $t1, 12($fp)
        bge   $t0, $t1, L0_27
        # j = 0
        li    $s0, 0
L0_3:
        # t1 = j int+ 1
        addiu $s4, $s0, 1
        # t2 = n int- i
        lw    $t0, 12($fp)
        lw    $t1, -4($fp)
        subu  $s5, $t0, $t1
        # if t1 int>= t2 goto 25
        bge   $s4, $s5, L0_25
        # t3 = j int<< 2
        sll   $s6, $s0, 2
        # t4 = a ptr+ t3
        addu  $s7, $s1, $s6
        # t5 = *t4
        lw    $t0, 0($s7)
        sw    $t0, -8($fp)
        # t6 = j int+ 1
        addiu $t0, $s0, 1
        sw    $t0, -12($fp)
        # t7 = t6 int<< 2
        sll   $t0, $t0, 2
        sw    $t0, -16($fp)
        # t8 = a ptr+ t7
        move  $t1, $t0
        addu  $t0, $s1, $t1
        sw    $t0, -20($fp)
        # t9 = *t8
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -24($fp)
        # if t5 int<= t9 goto 23
        lw    $t0, -8($fp)
        lw    $t1, -24($fp)
        ble   $t0, $t1, L0_23
        # t10 = j int<< 2
        sll   $t0, $s0, 2
        sw    $t0, -28($fp)
        # t11 = a ptr+ t10
        move  $t1, $t0
        addu  $s2, $s1, $t1
        # t12 = *t11
        lw    $t0, 0($s2)
        sw    $t0, -32($fp)
        # t15 = j int+ 1
        addiu $t0, $s0, 1
        sw    $t0, -36($fp)
        # t16 = t15 int<< 2
        sll   $t0, $t0, 2
        sw    $t0, -40($fp)
        # t17 = a ptr+ t16
        move  $t1, $t0
        addu  $s3, $s1, $t1
        # t18 = *t17
        lw    $t0, 0($s3)
        sw    $t0, -44($fp)
        # *t11 = t18
        sw    $t0, 0($s2)
        # *t17 = t12
        lw    $t0, -32($fp)
        sw    $t0, 0($s3)
L0_23:
        # j = j int+ 1
        addiu $s0, $s0, 1
        # goto 3
        j     L0_3
L0_25:
        # i = i int+ 1
        lw    $t0, -4($fp)
        addiu $t0, $t0, 1
        sw    $t0, -4($fp)
        # goto 1
        j     L0_1
L0_27:
        # return
        j     _Z6bubblePii_exit
_Z6bubblePii_exit:
        lw    $s0, -76($fp)
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

# quick(int *, int, int)
_Z5quickPiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        lw    $t8, __stack_limit
        sltu  $t8, $sp, $t8
        beqz  $t8, M1_0
        j     __stack_overflow
M1_0:
        sw    $s0, -36($fp)
        sw    $s1, -40($fp)
        sw    $s2, -64($fp)
        sw    $s3, -60($fp)
        sw    $s4, -44($fp)
        sw    $s5, -48($fp)
        sw    $s6, -52($fp)
        sw    $s7, -56($fp)
        move  $s2, $a0
        sw    $a1, 12($fp)
        sw    $a2, 16($fp)
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
        # p = *t4
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
        # if t8 int>= p goto 16
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
        sw    $t0, -4($fp)
        # t12 = *t11
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # if t12 int<= p goto 22
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
        sw    $t0, -12($fp)
        # t15 = a ptr+ t14
        move  $t1, $t0
        addu  $t0, $s2, $t1
        sw    $t0, -16($fp)
        # t16 = *t15
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t19 = j int<< 2
        sll   $t0, $s1, 2
        sw    $t0, -24($fp)
        # t20 = a ptr+ t19
        move  $t1, $t0
        addu  $t0, $s2, $t1
        sw    $t0, -28($fp)
        # t21 = *t20
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -32($fp)
        # *t15 = t21
        lw    $t8, -16($fp)
        lw    $t0, -32($fp)
        sw    $t0, 0($t8)
        # *t20 = t16
        lw    $t8, -28($fp)
        lw    $t0, -20($fp)
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
        move  $a0, $s2
        lw    $a1, 12($fp)
        move  $a2, $s1
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # param a
        # param i
        # param hi
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        move  $a0, $s2
        move  $a1, $s0
        lw    $a2, 16($fp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # return
        j     _Z5quickPiii_exit
_Z5quickPiii_exit:
        lw    $s0, -36($fp)
        lw    $s1, -40($fp)
        lw    $s2, -64($fp)
        lw    $s3, -60($fp)
        lw    $s4, -44($fp)
        lw    $s5, -48($fp)
        lw    $s6, -52($fp)
        lw    $s7, -56($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# find(int *, int, int)
_Z4findPiii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        sw    $s0, -16($fp)
        sw    $s1, -36($fp)
        sw    $s2, -40($fp)
        sw    $s3, -12($fp)
        sw    $s4, -20($fp)
        sw    $s5, -24($fp)
        sw    $s6, -28($fp)
        sw    $s7, -32($fp)
        sw    $a0, 8($fp)
        move  $s0, $a1
        sw    $a2, 16($fp)
        # lo = 0
        li    $s1, 0
        # hi = n int- 1
        addiu $s2, $s0, -1
L2_2:
        # if lo int> hi goto 18
        bgt   $s1, $s2, L2_18
        # t2 = lo int+ hi
        addu  $s3, $s1, $s2
        # t3 = t2 int/ 2
        li    $t1, 2
        div   $s3, $t1
        mflo  $s0
        # t4 = t3 int<< 2
        sll   $s4, $s0, 2
        # t5 = a ptr+ t4
        lw    $t0, 8($fp)
        addu  $s5, $t0, $s4
        # t6 = *t5
        lw    $s6, 0($s5)
        # if t6 int!= k goto 10
        lw    $t1, 16($fp)
        bne   $s6, $t1, L2_10
        # return t3
        move  $v0, $s0
        j     _Z4findPiii_exit
L2_10:
        # t7 = t3 int<< 2
        sll   $s7, $s0, 2
        # t8 = a ptr+ t7
        lw    $t0, 8($fp)
        addu  $t0, $t0, $s7
        sw    $t0, -4($fp)
        # t9 = *t8
        move  $t8, $t0
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # if t9 int>= k goto 16
        lw    $t1, 16($fp)
        bge   $t0, $t1, L2_16
        # lo = t3 int+ 1
        addiu $s1, $s0, 1
        # goto 2
        j     L2_2
L2_16:
        # hi = t3 int- 1
        addiu $s2, $s0, -1
        # goto 2
        j     L2_2
L2_18:
        # return -1
        li    $v0, -1
        j     _Z4findPiii_exit
_Z4findPiii_exit:
        lw    $s0, -16($fp)
        lw    $s1, -36($fp)
        lw    $s2, -40($fp)
        lw    $s3, -12($fp)
        lw    $s4, -20($fp)
        lw    $s5, -24($fp)
        lw    $s6, -28($fp)
        lw    $s7, -32($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# hanoi(int)
_Z5hanoii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        lw    $t8, __stack_limit
        sltu  $t8, $sp, $t8
        beqz  $t8, M3_0
        j     __stack_overflow
M3_0:
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        sw    $s2, -12($fp)
        move  $s2, $a0
        # if n int!= 0 goto 3
        bne   $s2, $zero, L3_3
        # t1 = 0
        li    $s0, 0
        # goto 8
        j     L3_8
L3_3:
        # t2 = n int- 1
        addiu $s1, $s2, -1
        # param t2
        # t3 = call hanoi(int), 1
        addiu $sp, $sp, -16
        move  $a0, $s1
        jal   _Z5hanoii
        addiu $sp, $sp, 16
        move  $s2, $v0
        # t4 = t3 int<< 1
        sll   $s1, $s2, 1
        # t1 = t4 int+ 1
        addiu $s0, $s1, 1
L3_8:
        # return t1
        move  $v0, $s0
        j     _Z5hanoii_exit
_Z5hanoii_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        lw    $s2, -12($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# ack(int, int)
_Z3ackii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        lw    $t8, __stack_limit
        sltu  $t8, $sp, $t8
        beqz  $t8, M4_0
        j     __stack_overflow
M4_0:
        sw    $s0, -24($fp)
        sw    $s1, -4($fp)
        sw    $s2, -8($fp)
        sw    $s3, -20($fp)
        sw    $s4, -12($fp)
        sw    $s5, -16($fp)
        move  $s0, $a0
        move  $s3, $a1
        # if m int!= 0 goto 3
        bne   $s0, $zero, L4_3
        # t1 = n int+ 1
        addiu $s1, $s3, 1
        # goto 18
        j     L4_18
L4_3:
        # if n int!= 0 goto 9
        bne   $s3, $zero, L4_9
        # t4 = m int- 1
        addiu $s4, $s0, -1
        # param t4
        # param 1
        # t3 = call ack(int, int), 2
        addiu $sp, $sp, -16
        move  $a0, $s4
        li    $a1, 1
        jal   _Z3ackii
        addiu $sp, $sp, 16
        move  $s2, $v0
        # goto 17
        j     L4_17
L4_9:
        # t6 = m int- 1
        addiu $s4, $s0, -1
        # t7 = n int- 1
        addiu $s5, $s3, -1
        # param m
        # param t7
        # t8 = call ack(int, int), 2
        addiu $sp, $sp, -16
        move  $a0, $s0
        move  $a1, $s5
        jal   _Z3ackii
        addiu $sp, $sp, 16
        move  $s3, $v0
        # param t6
        # param t8
        # t3 = call ack(int, int), 2
        addiu $sp, $sp, -16
        move  $a0, $s4
        move  $a1, $s3
        jal   _Z3ackii
        addiu $sp, $sp, 16
        move  $s2, $v0
L4_17:
        # t1 = t3
        move  $s1, $s2
L4_18:
        # return t1
        move  $v0, $s1
        j     _Z3ackii_exit
_Z3ackii_exit:
        lw    $s0, -24($fp)
        lw    $s1, -4($fp)
        lw    $s2, -8($fp)
        lw    $s3, -20($fp)
        lw    $s4, -12($fp)
        lw    $s5, -16($fp)
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
        addiu $sp, $sp, -264
        lw    $t8, __stack_limit
        sltu  $t8, $sp, $t8
        beqz  $t8, M5_0
        j     __stack_overflow
M5_0:
        sw    $s0, -232($fp)
        sw    $s1, -236($fp)
        sw    $s2, -240($fp)
        sw    $s3, -244($fp)
        sw    $s4, -248($fp)
        sw    $s5, -252($fp)
        sw    $s6, -256($fp)
        sw    $s7, -260($fp)
        # a[0] = 5
        li    $t0, 5
        sw    $t0, -32($fp)
        # a[4] = 2
        li    $t0, 2
        sw    $t0, -28($fp)
        # a[8] = 9
        li    $t0, 9
        sw    $t0, -24($fp)
        # a[12] = 1
        li    $t0, 1
        sw    $t0, -20($fp)
        # a[16] = 7
        li    $t0, 7
        sw    $t0, -16($fp)
        # a[20] = 3
        li    $t0, 3
        sw    $t0, -12($fp)
        # a[24] = 8
        li    $t0, 8
        sw    $t0, -8($fp)
        # a[28] = 6
        li    $t0, 6
        sw    $t0, -4($fp)
        # b[0] = 4
        li    $t0, 4
        sw    $t0, -64($fp)
        # b[4] = 0
        sw    $zero, -60($fp)
        # b[8] = 3
        li    $t0, 3
        sw    $t0, -56($fp)
        # b[12] = 9
        li    $t0, 9
        sw    $t0, -52($fp)
        # b[16] = 1
        li    $t0, 1
        sw    $t0, -48($fp)
        # b[20] = 8
        li    $t0, 8
        sw    $t0, -44($fp)
        # b[24] = 2
        li    $t0, 2
        sw    $t0, -40($fp)
        # b[28] = 7
        li    $t0, 7
        sw    $t0, -36($fp)
        # t1 = &a
        addiu $s0, $fp, -32
        # param t1
        # param 8
        # call bubble(int *, int), 2
        addiu $sp, $sp, -16
        move  $a0, $s0
        li    $a1, 8
        jal   _Z6bubblePii
        addiu $sp, $sp, 16
        # t2 = &b
        addiu $s1, $fp, -64
        # param t2
        # param 0
        # param 7
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        move  $a0, $s1
        move  $a1, $zero
        li    $a2, 7
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # t3 = a[0]
        lw    $s1, -32($fp)
        # t4 = a[28]
        lw    $s2, -4($fp)
        # t5 = b[0]
        lw    $s3, -64($fp)
        # t6 = b[28]
        lw    $s4, -36($fp)
        # param t1
        # param 8
        # param 7
        # t8 = call find(int *, int, int), 3
        addiu $sp, $sp, -16
        move  $a0, $s0
        li    $a1, 8
        li    $a2, 7
        jal   _Z4findPiii
        addiu $sp, $sp, 16
        move  $s5, $v0
        # param t1
        # param 8
        # param 4
        # t10 = call find(int *, int, int), 3
        addiu $sp, $sp, -16
        move  $a0, $s0
        li    $a1, 8
        li    $a2, 4
        jal   _Z4findPiii
        addiu $sp, $sp, 16
        move  $s6, $v0
        # param "%d %d %d %d %d %d\n"
        # param t3
        # param t4
        # param t5
        # param t6
        # param t8
        # param t10
        # call printf, 7
        addiu $sp, $sp, -32
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        sw    $s4, 16($sp)
        sw    $s5, 20($sp)
        sw    $s6, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 10
        # t11 = call hanoi(int), 1
        addiu $sp, $sp, -16
        li    $a0, 10
        jal   _Z5hanoii
        addiu $sp, $sp, 16
        move  $s0, $v0
        # param 2
        # param 3
        # t12 = call ack(int, int), 2
        addiu $sp, $sp, -16
        li    $a0, 2
        li    $a1, 3
        jal   _Z3ackii
        addiu $sp, $sp, 16
        move  $s1, $v0
        # param "%d %d\n"
        # param t11
        # param t12
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # m1[0] = 1
        li    $t0, 1
        sw    $t0, -84($fp)
        # m1[4] = 2
        li    $t0, 2
        sw    $t0, -80($fp)
        # m1[8] = 3
        li    $t0, 3
        sw    $t0, -76($fp)
        # m1[12] = 4
        li    $t0, 4
        sw    $t0, -72($fp)
        # m2[0] = 5
        li    $t0, 5
        sw    $t0, -100($fp)
        # m2[4] = 6
        li    $t0, 6
        sw    $t0, -96($fp)
        # m2[8] = 7
        li    $t0, 7
        sw    $t0, -92($fp)
        # m2[12] = 8
        li    $t0, 8
        sw    $t0, -88($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -68($fp)
L5_63:
        # if i int>= 2 goto 92
        lw    $t0, -68($fp)
        li    $t1, 2
        bge   $t0, $t1, L5_92
        # j = 0
        li    $s3, 0
L5_65:
        # if j int>= 2 goto 90
        li    $t1, 2
        bge   $s3, $t1, L5_90
        # t13 = i int<< 1
        lw    $t0, -68($fp)
        sll   $t0, $t0, 1
        sw    $t0, -192($fp)
        # t14 = t13 int+ j
        addu  $t0, $t0, $s3
        sw    $t0, -196($fp)
        # t15 = t14 int<< 2
        sll   $t0, $t0, 2
        sw    $t0, -200($fp)
        # p[t15] = 0
        addiu $t8, $fp, -116
        lw    $t9, -200($fp)
        addu  $t8, $t8, $t9
        sw    $zero, 0($t8)
        # k = 0
        li    $s0, 0
L5_71:
        # if k int>= 2 goto 88
        li    $t1, 2
        bge   $s0, $t1, L5_88
        # t16 = i int<< 1
        lw    $t0, -68($fp)
        sll   $s1, $t0, 1
        # t17 = t16 int+ j
        addu  $s4, $s1, $s3
        # t18 = t17 int<< 2
        sll   $s2, $s4, 2
        # t19 = p[t18]
        addiu $t8, $fp, -116
        addu  $t8, $t8, $s2
        lw    $s5, 0($t8)
        # t21 = t16 int+ k
        addu  $s6, $s1, $s0
        # t22 = t21 int<< 2
        sll   $s7, $s6, 2
        # t23 = m1[t22]
        addiu $t8, $fp, -84
        addu  $t8, $t8, $s7
        lw    $t0, 0($t8)
        sw    $t0, -204($fp)
        # t24 = k int<< 1
        sll   $t0, $s0, 1
        sw    $t0, -208($fp)
        # t25 = t24 int+ j
        addu  $t0, $t0, $s3
        sw    $t0, -212($fp)
        # t26 = t25 int<< 2
        sll   $t0, $t0, 2
        sw    $t0, -216($fp)
        # t27 = m2[t26]
        addiu $t8, $fp, -100
        lw    $t9, -216($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -220($fp)
        # t28 = t23 int* t27
        lw    $t0, -204($fp)
        lw    $t1, -220($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -224($fp)
        # t29 = t19 int+ t28
        move  $t1, $t0
        addu  $t0, $s5, $t1
        sw    $t0, -228($fp)
        # p[t18] = t29
        addiu $t8, $fp, -116
        addu  $t8, $t8, $s2
        lw    $t0, -228($fp)
        sw    $t0, 0($t8)
        # k = k int+ 1
        addiu $s0, $s0, 1
        # goto 71
        j     L5_71
L5_88:
        # j = j int+ 1
        addiu $s3, $s3, 1
        # goto 65
        j     L5_65
L5_90:
        # i = i int+ 1
        lw    $t0, -68($fp)
        addiu $t0, $t0, 1
        sw    $t0, -68($fp)
        # goto 63
        j     L5_63
L5_92:
        # t33 = p[0]
        lw    $s1, -116($fp)
        # t34 = p[4]
        lw    $s2, -112($fp)
        # t35 = p[8]
        lw    $s4, -108($fp)
        # t36 = p[12]
        lw    $s5, -104($fp)
        # param "%d %d %d %d\n"
        # param t33
        # param t34
        # param t35
        # param t36
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        sw    $s2, 8($sp)
        sw    $s4, 12($sp)
        sw    $s5, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # primes = 0
        li    $s4, 0
        # i = 0
        li    $t0, 0
        sw    $t0, -68($fp)
L5_104:
        # if i int>= 50 goto 108
        lw    $t0, -68($fp)
        li    $t1, 50
        bge   $t0, $t1, L5_108
        # sieve[i] = 1
        addiu $t8, $fp, -166
        lw    $t9, -68($fp)
        addu  $t8, $t8, $t9
        li    $t0, 1
        sb    $t0, 0($t8)
        # i = i int+ 1
        lw    $t0, -68($fp)
        addiu $t0, $t0, 1
        sw    $t0, -68($fp)
        # goto 104
        j     L5_104
L5_108:
        # i = 2
        li    $t0, 2
        sw    $t0, -68($fp)
L5_109:
        # if i int>= 50 goto 120
        lw    $t0, -68($fp)
        li    $t1, 50
        bge   $t0, $t1, L5_120
        # t38 = sieve[i]
        addiu $t8, $fp, -166
        lw    $t9, -68($fp)
        addu  $t8, $t8, $t9
        lb    $s1, 0($t8)
        # if t38 char== 0 goto 118
        beq   $s1, $zero, L5_118
        # primes = primes int+ 1
        addiu $s4, $s4, 1
        # j = i int* i
        lw    $t0, -68($fp)
        lw    $t1, -68($fp)
        mul   $s3, $t0, $t1
L5_114:
        # if j int>= 50 goto 118
        li    $t1, 50
        bge   $s3, $t1, L5_118
        # sieve[j] = 0
        addiu $t8, $fp, -166
        addu  $t8, $t8, $s3
        sb    $zero, 0($t8)
        # j = j int+ i
        lw    $t1, -68($fp)
        addu  $s3, $s3, $t1
        # goto 114
        j     L5_114
L5_118:
        # i = i int+ 1
        lw    $t0, -68($fp)
        addiu $t0, $t0, 1
        sw    $t0, -68($fp)
        # goto 109
        j     L5_109
L5_120:
        # text[0] = 99
        li    $t0, 99
        sb    $t0, -178($fp)
        # text[1] = 111
        li    $t0, 111
        sb    $t0, -177($fp)
        # text[2] = 109
        li    $t0, 109
        sb    $t0, -176($fp)
        # text[3] = 112
        li    $t0, 112
        sb    $t0, -175($fp)
        # text[4] = 105
        li    $t0, 105
        sb    $t0, -174($fp)
        # text[5] = 108
        li    $t0, 108
        sb    $t0, -173($fp)
        # text[6] = 101
        li    $t0, 101
        sb    $t0, -172($fp)
        # text[7] = 114
        li    $t0, 114
        sb    $t0, -171($fp)
        # text[8] = 0
        sb    $zero, -170($fp)
        # text[9] = 0
        sb    $zero, -169($fp)
        # text[10] = 0
        sb    $zero, -168($fp)
        # text[11] = 0
        sb    $zero, -167($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -68($fp)
        # j = 7
        li    $s3, 7
L5_134:
        # if i int>= j goto 142
        lw    $t0, -68($fp)
        bge   $t0, $s3, L5_142
        # t43 = text[i]
        addiu $t8, $fp, -178
        lw    $t9, -68($fp)
        addu  $t8, $t8, $t9
        lb    $s1, 0($t8)
        # t44 = text[j]
        addiu $t8, $fp, -178
        addu  $t8, $t8, $s3
        lb    $s2, 0($t8)
        # text[i] = t44
        addiu $t8, $fp, -178
        lw    $t9, -68($fp)
        addu  $t8, $t8, $t9
        sb    $s2, 0($t8)
        # text[j] = t43
        addiu $t8, $fp, -178
        addu  $t8, $t8, $s3
        sb    $s1, 0($t8)
        # i = i int+ 1
        lw    $t0, -68($fp)
        addiu $t0, $t0, 1
        sw    $t0, -68($fp)
        # j = j int- 1
        addiu $s3, $s3, -1
        # goto 134
        j     L5_134
L5_142:
        # n = 9081
        li    $s1, 9081
        # v = 0
        li    $s2, 0
        # k = 0
        li    $s0, 0
L5_145:
        # if n int== 0 goto 154
        beq   $s1, $zero, L5_154
        # t47 = k
        move  $s3, $s0
        # k = k int+ 1
        addiu $s0, $s0, 1
        # t49 = n int% 10
        li    $t1, 10
        div   $s1, $t1
        mfhi  $s5
        # t50 = 48 int+ t49
        li    $t0, 48
        addu  $s6, $t0, $s5
        # t51 = inttochar t50
        move  $t0, $s6
        move  $s7, $t0
        sll   $s7, $s7, 24
        sra   $s7, $s7, 24
        # num[t47] = t51
        addiu $t8, $fp, -186
        addu  $t8, $t8, $s3
        sb    $s7, 0($t8)
        # n = n int/ 10
        li    $t1, 10
        div   $s1, $t1
        mflo  $s1
        # goto 145
        j     L5_145
L5_154:
        # i = k int- 1
        addiu $t0, $s0, -1
        sw    $t0, -68($fp)
L5_155:
        # if i int< 0 goto 163
        lw    $t0, -68($fp)
        blt   $t0, $zero, L5_163
        # t54 = v int* 10
        li    $t1, 10
        mul   $s0, $s2, $t1
        # t55 = num[i]
        addiu $t8, $fp, -186
        lw    $t9, -68($fp)
        addu  $t8, $t8, $t9
        lb    $s1, 0($t8)
        # t56 = chartoint t55
        move  $t0, $s1
        move  $s3, $t0
        # t57 = t56 int- 48
        addiu $s5, $s3, -48
        # v = t54 int+ t57
        addu  $s2, $s0, $s5
        # i = i int- 1
        lw    $t0, -68($fp)
        addiu $t0, $t0, -1
        sw    $t0, -68($fp)
        # goto 155
        j     L5_155
L5_163:
        # t60 = &text
        addiu $s0, $fp, -178
        # param "%d %s %d\n"
        # param primes
        # param t60
        # param v
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s4, 4($sp)
        sw    $s0, 8($sp)
        sw    $s2, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # return 0
        li    $v0, 0
        j     main__exit
main__exit:
        lw    $s0, -232($fp)
        lw    $s1, -236($fp)
        lw    $s2, -240($fp)
        lw    $s3, -244($fp)
        lw    $s4, -248($fp)
        lw    $s5, -252($fp)
        lw    $s6, -256($fp)
        lw    $s7, -260($fp)
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
