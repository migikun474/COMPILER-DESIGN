# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t18_algorithms.c
#  Optimization : no optimization (every value in the stack frame)
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
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -112
        # i = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L0_1:
        # t1 = n int- 1
        lw    $t0, 12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # if i int< t1 goto 4
        lw    $t0, -4($fp)
        lw    $t1, -16($fp)
        blt   $t0, $t1, L0_4
        # goto 39
        j     L0_39
L0_4:
        # j = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L0_5:
        # t2 = n int- 1
        lw    $t0, 12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t3 = t2 int- i
        lw    $t0, -20($fp)
        lw    $t1, -4($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # if j int< t3 goto 9
        lw    $t0, -8($fp)
        lw    $t1, -24($fp)
        blt   $t0, $t1, L0_9
        # goto 36
        j     L0_36
L0_9:
        # t4 = j int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -28($fp)
        # t5 = a ptr+ t4
        lw    $t0, 8($fp)
        lw    $t1, -28($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t6 = *t5
        lw    $t8, -32($fp)
        lw    $t0, 0($t8)
        sw    $t0, -36($fp)
        # t7 = j int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -40($fp)
        # t8 = t7 int* 4
        lw    $t0, -40($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t9 = a ptr+ t8
        lw    $t0, 8($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # t10 = *t9
        lw    $t8, -48($fp)
        lw    $t0, 0($t8)
        sw    $t0, -52($fp)
        # if t6 int> t10 goto 18
        lw    $t0, -36($fp)
        lw    $t1, -52($fp)
        bgt   $t0, $t1, L0_18
        # goto 33
        j     L0_33
L0_18:
        # t11 = j int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -56($fp)
        # t12 = a ptr+ t11
        lw    $t0, 8($fp)
        lw    $t1, -56($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # t13 = *t12
        lw    $t8, -60($fp)
        lw    $t0, 0($t8)
        sw    $t0, -64($fp)
        # t = t13
        lw    $t0, -64($fp)
        sw    $t0, -12($fp)
        # t14 = j int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -68($fp)
        # t15 = a ptr+ t14
        lw    $t0, 8($fp)
        lw    $t1, -68($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -72($fp)
        # t16 = j int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # t17 = t16 int* 4
        lw    $t0, -76($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -80($fp)
        # t18 = a ptr+ t17
        lw    $t0, 8($fp)
        lw    $t1, -80($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -84($fp)
        # t19 = *t18
        lw    $t8, -84($fp)
        lw    $t0, 0($t8)
        sw    $t0, -88($fp)
        # *t15 = t19
        lw    $t8, -72($fp)
        lw    $t0, -88($fp)
        sw    $t0, 0($t8)
        # t20 = j int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -92($fp)
        # t21 = t20 int* 4
        lw    $t0, -92($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -96($fp)
        # t22 = a ptr+ t21
        lw    $t0, 8($fp)
        lw    $t1, -96($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -100($fp)
        # *t22 = t
        lw    $t8, -100($fp)
        lw    $t0, -12($fp)
        sw    $t0, 0($t8)
L0_33:
        # t23 = j int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -104($fp)
        # j = t23
        lw    $t0, -104($fp)
        sw    $t0, -8($fp)
        # goto 5
        j     L0_5
L0_36:
        # t24 = i int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -108($fp)
        # i = t24
        lw    $t0, -108($fp)
        sw    $t0, -4($fp)
        # goto 1
        j     L0_1
L0_39:
        # return
        j     _Z6bubblePii_exit
_Z6bubblePii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# quick(int *, int, int)
_Z5quickPiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -120
        # if lo int>= hi goto 2
        lw    $t0, 12($fp)
        lw    $t1, 16($fp)
        bge   $t0, $t1, L1_2
        # goto 3
        j     L1_3
L1_2:
        # return
        j     _Z5quickPiii_exit
L1_3:
        # t1 = lo int+ hi
        lw    $t0, 12($fp)
        lw    $t1, 16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t2 = t1 int/ 2
        lw    $t0, -20($fp)
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -24($fp)
        # t3 = t2 int* 4
        lw    $t0, -24($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -28($fp)
        # t4 = a ptr+ t3
        lw    $t0, 8($fp)
        lw    $t1, -28($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t5 = *t4
        lw    $t8, -32($fp)
        lw    $t0, 0($t8)
        sw    $t0, -36($fp)
        # pivot = t5
        lw    $t0, -36($fp)
        sw    $t0, -4($fp)
        # i = lo
        lw    $t0, 12($fp)
        sw    $t0, -8($fp)
        # j = hi
        lw    $t0, 16($fp)
        sw    $t0, -12($fp)
L1_11:
        # if i int<= j goto 13
        lw    $t0, -8($fp)
        lw    $t1, -12($fp)
        ble   $t0, $t1, L1_13
        # goto 49
        j     L1_49
L1_13:
        # t6 = i int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -40($fp)
        # t7 = a ptr+ t6
        lw    $t0, 8($fp)
        lw    $t1, -40($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t8 = *t7
        lw    $t8, -44($fp)
        lw    $t0, 0($t8)
        sw    $t0, -48($fp)
        # if t8 int< pivot goto 18
        lw    $t0, -48($fp)
        lw    $t1, -4($fp)
        blt   $t0, $t1, L1_18
        # goto 21
        j     L1_21
L1_18:
        # t9 = i int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -52($fp)
        # i = t9
        lw    $t0, -52($fp)
        sw    $t0, -8($fp)
        # goto 13
        j     L1_13
L1_21:
        # t10 = j int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -56($fp)
        # t11 = a ptr+ t10
        lw    $t0, 8($fp)
        lw    $t1, -56($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # t12 = *t11
        lw    $t8, -60($fp)
        lw    $t0, 0($t8)
        sw    $t0, -64($fp)
        # if t12 int> pivot goto 26
        lw    $t0, -64($fp)
        lw    $t1, -4($fp)
        bgt   $t0, $t1, L1_26
        # goto 29
        j     L1_29
L1_26:
        # t13 = j int- 1
        lw    $t0, -12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -68($fp)
        # j = t13
        lw    $t0, -68($fp)
        sw    $t0, -12($fp)
        # goto 21
        j     L1_21
L1_29:
        # if i int<= j goto 31
        lw    $t0, -8($fp)
        lw    $t1, -12($fp)
        ble   $t0, $t1, L1_31
        # goto 11
        j     L1_11
L1_31:
        # t14 = i int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -72($fp)
        # t15 = a ptr+ t14
        lw    $t0, 8($fp)
        lw    $t1, -72($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # t16 = *t15
        lw    $t8, -76($fp)
        lw    $t0, 0($t8)
        sw    $t0, -80($fp)
        # t = t16
        lw    $t0, -80($fp)
        sw    $t0, -16($fp)
        # t17 = i int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -84($fp)
        # t18 = a ptr+ t17
        lw    $t0, 8($fp)
        lw    $t1, -84($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -88($fp)
        # t19 = j int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -92($fp)
        # t20 = a ptr+ t19
        lw    $t0, 8($fp)
        lw    $t1, -92($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -96($fp)
        # t21 = *t20
        lw    $t8, -96($fp)
        lw    $t0, 0($t8)
        sw    $t0, -100($fp)
        # *t18 = t21
        lw    $t8, -88($fp)
        lw    $t0, -100($fp)
        sw    $t0, 0($t8)
        # t22 = j int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -104($fp)
        # t23 = a ptr+ t22
        lw    $t0, 8($fp)
        lw    $t1, -104($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -108($fp)
        # *t23 = t
        lw    $t8, -108($fp)
        lw    $t0, -16($fp)
        sw    $t0, 0($t8)
        # t24 = i int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -112($fp)
        # i = t24
        lw    $t0, -112($fp)
        sw    $t0, -8($fp)
        # t25 = j int- 1
        lw    $t0, -12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -116($fp)
        # j = t25
        lw    $t0, -116($fp)
        sw    $t0, -12($fp)
        # goto 11
        j     L1_11
L1_49:
        # param a
        # param lo
        # param j
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        lw    $t0, 12($fp)
        sw    $t0, 4($sp)
        lw    $t0, -12($fp)
        sw    $t0, 8($sp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # param a
        # param i
        # param hi
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        lw    $t0, -8($fp)
        sw    $t0, 4($sp)
        lw    $t0, 16($fp)
        sw    $t0, 8($sp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # return
        j     _Z5quickPiii_exit
_Z5quickPiii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# search(int *, int, int)
_Z6searchPiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        # lo = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # t1 = n int- 1
        lw    $t0, 12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # hi = t1
        lw    $t0, -16($fp)
        sw    $t0, -8($fp)
L2_3:
        # if lo int<= hi goto 5
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        ble   $t0, $t1, L2_5
        # goto 26
        j     L2_26
L2_5:
        # t2 = hi int- lo
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t3 = t2 int/ 2
        lw    $t0, -20($fp)
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -24($fp)
        # t4 = lo int+ t3
        lw    $t0, -4($fp)
        lw    $t1, -24($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # mid = t4
        lw    $t0, -28($fp)
        sw    $t0, -12($fp)
        # t5 = mid int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t6 = a ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -32($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # t7 = *t6
        lw    $t8, -36($fp)
        lw    $t0, 0($t8)
        sw    $t0, -40($fp)
        # if t7 int== key goto 14
        lw    $t0, -40($fp)
        lw    $t1, 16($fp)
        beq   $t0, $t1, L2_14
        # goto 15
        j     L2_15
L2_14:
        # return mid
        lw    $v0, -12($fp)
        j     _Z6searchPiii_exit
L2_15:
        # t8 = mid int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t9 = a ptr+ t8
        lw    $t0, 8($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # t10 = *t9
        lw    $t8, -48($fp)
        lw    $t0, 0($t8)
        sw    $t0, -52($fp)
        # if t10 int< key goto 20
        lw    $t0, -52($fp)
        lw    $t1, 16($fp)
        blt   $t0, $t1, L2_20
        # goto 23
        j     L2_23
L2_20:
        # t11 = mid int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -56($fp)
        # lo = t11
        lw    $t0, -56($fp)
        sw    $t0, -4($fp)
        # goto 3
        j     L2_3
L2_23:
        # t12 = mid int- 1
        lw    $t0, -12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -60($fp)
        # hi = t12
        lw    $t0, -60($fp)
        sw    $t0, -8($fp)
        # goto 3
        j     L2_3
L2_26:
        # t13 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -64($fp)
        # return t13
        lw    $v0, -64($fp)
        j     _Z6searchPiii_exit
_Z6searchPiii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# hanoi(int, int, int, int)
_Z5hanoiiiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if n int== 0 goto 2
        lw    $t0, 8($fp)
        li    $t1, 0
        beq   $t0, $t1, L3_2
        # goto 3
        j     L3_3
L3_2:
        # return
        j     _Z5hanoiiiii_exit
L3_3:
        # t1 = n int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # param t1
        # param from
        # param via
        # param to
        # call hanoi(int, int, int, int), 4
        addiu $sp, $sp, -16
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        lw    $t0, 12($fp)
        sw    $t0, 4($sp)
        lw    $t0, 20($fp)
        sw    $t0, 8($sp)
        lw    $t0, 16($fp)
        sw    $t0, 12($sp)
        jal   _Z5hanoiiiii
        addiu $sp, $sp, 16
        # t2 = moves int+ 1
        lw    $t0, g_moves
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # moves = t2
        lw    $t0, -8($fp)
        sw    $t0, g_moves
        # t3 = n int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # param t3
        # param via
        # param to
        # param from
        # call hanoi(int, int, int, int), 4
        addiu $sp, $sp, -16
        lw    $t0, -12($fp)
        sw    $t0, 0($sp)
        lw    $t0, 20($fp)
        sw    $t0, 4($sp)
        lw    $t0, 16($fp)
        sw    $t0, 8($sp)
        lw    $t0, 12($fp)
        sw    $t0, 12($sp)
        jal   _Z5hanoiiiii
        addiu $sp, $sp, 16
        # return
        j     _Z5hanoiiiii_exit
_Z5hanoiiiii_exit:
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
        addiu $sp, $sp, -32
        # if m int== 0 goto 2
        lw    $t0, 8($fp)
        li    $t1, 0
        beq   $t0, $t1, L4_2
        # goto 4
        j     L4_4
L4_2:
        # t1 = n int+ 1
        lw    $t0, 12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # return t1
        lw    $v0, -4($fp)
        j     _Z9ackermannii_exit
L4_4:
        # if n int== 0 goto 6
        lw    $t0, 12($fp)
        li    $t1, 0
        beq   $t0, $t1, L4_6
        # goto 11
        j     L4_11
L4_6:
        # t2 = m int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # param t2
        # param 1
        # t3 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        sw    $v0, -12($fp)
        # return t3
        lw    $v0, -12($fp)
        j     _Z9ackermannii_exit
L4_11:
        # t4 = m int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = n int- 1
        lw    $t0, 12($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # param m
        # param t5
        # t6 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        lw    $t0, -20($fp)
        sw    $t0, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        sw    $v0, -24($fp)
        # param t4
        # param t6
        # t7 = call ackermann(int, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        lw    $t0, -24($fp)
        sw    $t0, 4($sp)
        jal   _Z9ackermannii
        addiu $sp, $sp, 8
        sw    $v0, -28($fp)
        # return t7
        lw    $v0, -28($fp)
        j     _Z9ackermannii_exit
_Z9ackermannii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# multiply(int (*)[3], int (*)[2], int (*)[2])
_Z8multiplyPA3_iPA2_iS2_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -112
        # i = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L5_1:
        # if i int< 2 goto 3
        lw    $t0, -4($fp)
        li    $t1, 2
        blt   $t0, $t1, L5_3
        # goto 41
        j     L5_41
L5_3:
        # j = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L5_4:
        # if j int< 2 goto 6
        lw    $t0, -8($fp)
        li    $t1, 2
        blt   $t0, $t1, L5_6
        # goto 38
        j     L5_38
L5_6:
        # t1 = i int* 8
        lw    $t0, -4($fp)
        li    $t1, 8
        mul   $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t2 = c ptr+ t1
        lw    $t0, 16($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t3 = j int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t4 = t2 ptr+ t3
        lw    $t0, -20($fp)
        lw    $t1, -24($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # *t4 = 0
        lw    $t8, -28($fp)
        li    $t0, 0
        sw    $t0, 0($t8)
        # k = 0
        li    $t0, 0
        sw    $t0, -12($fp)
L5_12:
        # if k int< 3 goto 14
        lw    $t0, -12($fp)
        li    $t1, 3
        blt   $t0, $t1, L5_14
        # goto 35
        j     L5_35
L5_14:
        # t5 = i int* 8
        lw    $t0, -4($fp)
        li    $t1, 8
        mul   $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t6 = c ptr+ t5
        lw    $t0, 16($fp)
        lw    $t1, -32($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # t7 = j int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -40($fp)
        # t8 = t6 ptr+ t7
        lw    $t0, -36($fp)
        lw    $t1, -40($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t9 = *t8
        lw    $t8, -44($fp)
        lw    $t0, 0($t8)
        sw    $t0, -48($fp)
        # t10 = i int* 12
        lw    $t0, -4($fp)
        li    $t1, 12
        mul   $t0, $t0, $t1
        sw    $t0, -52($fp)
        # t11 = a ptr+ t10
        lw    $t0, 8($fp)
        lw    $t1, -52($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -56($fp)
        # t12 = k int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -60($fp)
        # t13 = t11 ptr+ t12
        lw    $t0, -56($fp)
        lw    $t1, -60($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -64($fp)
        # t14 = *t13
        lw    $t8, -64($fp)
        lw    $t0, 0($t8)
        sw    $t0, -68($fp)
        # t15 = k int* 8
        lw    $t0, -12($fp)
        li    $t1, 8
        mul   $t0, $t0, $t1
        sw    $t0, -72($fp)
        # t16 = b ptr+ t15
        lw    $t0, 12($fp)
        lw    $t1, -72($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # t17 = j int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -80($fp)
        # t18 = t16 ptr+ t17
        lw    $t0, -76($fp)
        lw    $t1, -80($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -84($fp)
        # t19 = *t18
        lw    $t8, -84($fp)
        lw    $t0, 0($t8)
        sw    $t0, -88($fp)
        # t20 = t14 int* t19
        lw    $t0, -68($fp)
        lw    $t1, -88($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -92($fp)
        # t21 = t9 int+ t20
        lw    $t0, -48($fp)
        lw    $t1, -92($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -96($fp)
        # *t8 = t21
        lw    $t8, -44($fp)
        lw    $t0, -96($fp)
        sw    $t0, 0($t8)
        # t22 = k int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -100($fp)
        # k = t22
        lw    $t0, -100($fp)
        sw    $t0, -12($fp)
        # goto 12
        j     L5_12
L5_35:
        # t23 = j int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -104($fp)
        # j = t23
        lw    $t0, -104($fp)
        sw    $t0, -8($fp)
        # goto 4
        j     L5_4
L5_38:
        # t24 = i int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -108($fp)
        # i = t24
        lw    $t0, -108($fp)
        sw    $t0, -4($fp)
        # goto 1
        j     L5_1
L5_41:
        # return
        j     _Z8multiplyPA3_iPA2_iS2__exit
_Z8multiplyPA3_iPA2_iS2__exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# primes(int)
_Z6primesi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -144
        # count = 0
        li    $t0, 0
        sw    $t0, -108($fp)
        # i.34 = 0
        li    $t0, 0
        sw    $t0, -112($fp)
L6_2:
        # if i.34 int<= limit goto 4
        lw    $t0, -112($fp)
        lw    $t1, 8($fp)
        ble   $t0, $t1, L6_4
        # goto 8
        j     L6_8
L6_4:
        # composite[i.34] = 0
        addiu $t8, $fp, -101
        lw    $t9, -112($fp)
        addu  $t8, $t8, $t9
        li    $t0, 0
        sb    $t0, 0($t8)
        # t1 = i.34 int+ 1
        lw    $t0, -112($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -124($fp)
        # i.34 = t1
        lw    $t0, -124($fp)
        sw    $t0, -112($fp)
        # goto 2
        j     L6_2
L6_8:
        # i.35 = 2
        li    $t0, 2
        sw    $t0, -116($fp)
L6_9:
        # if i.35 int<= limit goto 11
        lw    $t0, -116($fp)
        lw    $t1, 8($fp)
        ble   $t0, $t1, L6_11
        # goto 28
        j     L6_28
L6_11:
        # t2 = composite[i.35]
        addiu $t8, $fp, -101
        lw    $t9, -116($fp)
        addu  $t8, $t8, $t9
        lb    $t0, 0($t8)
        sb    $t0, -125($fp)
        # if t2 char!= 0 goto 14
        lb    $t0, -125($fp)
        li    $t1, 0
        bne   $t0, $t1, L6_14
        # goto 15
        j     L6_15
L6_14:
        # goto 25
        j     L6_25
L6_15:
        # t3 = count int+ 1
        lw    $t0, -108($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -132($fp)
        # count = t3
        lw    $t0, -132($fp)
        sw    $t0, -108($fp)
        # t4 = i.35 int* i.35
        lw    $t0, -116($fp)
        lw    $t1, -116($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -136($fp)
        # j = t4
        lw    $t0, -136($fp)
        sw    $t0, -120($fp)
L6_19:
        # if j int<= limit goto 21
        lw    $t0, -120($fp)
        lw    $t1, 8($fp)
        ble   $t0, $t1, L6_21
        # goto 25
        j     L6_25
L6_21:
        # composite[j] = 1
        addiu $t8, $fp, -101
        lw    $t9, -120($fp)
        addu  $t8, $t8, $t9
        li    $t0, 1
        sb    $t0, 0($t8)
        # t5 = j int+ i.35
        lw    $t0, -120($fp)
        lw    $t1, -116($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -140($fp)
        # j = t5
        lw    $t0, -140($fp)
        sw    $t0, -120($fp)
        # goto 19
        j     L6_19
L6_25:
        # t6 = i.35 int+ 1
        lw    $t0, -116($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -144($fp)
        # i.35 = t6
        lw    $t0, -144($fp)
        sw    $t0, -116($fp)
        # goto 9
        j     L6_9
L6_28:
        # return count
        lw    $v0, -108($fp)
        j     _Z6primesi_exit
_Z6primesi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# power(int, int)
_Z5powerii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # result = 1
        li    $t0, 1
        sw    $t0, -4($fp)
L7_1:
        # if exp int> 0 goto 3
        lw    $t0, 12($fp)
        li    $t1, 0
        bgt   $t0, $t1, L7_3
        # goto 13
        j     L7_13
L7_3:
        # t1 = exp int& 1
        lw    $t0, 12($fp)
        li    $t1, 1
        and   $t0, $t0, $t1
        sw    $t0, -8($fp)
        # if t1 int!= 0 goto 6
        lw    $t0, -8($fp)
        li    $t1, 0
        bne   $t0, $t1, L7_6
        # goto 8
        j     L7_8
L7_6:
        # t2 = result int* base
        lw    $t0, -4($fp)
        lw    $t1, 8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # result = t2
        lw    $t0, -12($fp)
        sw    $t0, -4($fp)
L7_8:
        # t3 = base int* base
        lw    $t0, 8($fp)
        lw    $t1, 8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -16($fp)
        # base = t3
        lw    $t0, -16($fp)
        sw    $t0, 8($fp)
        # t4 = exp int>> 1
        lw    $t0, 12($fp)
        li    $t1, 1
        srav  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # exp = t4
        lw    $t0, -20($fp)
        sw    $t0, 12($fp)
        # goto 1
        j     L7_1
L7_13:
        # return result
        lw    $v0, -4($fp)
        j     _Z5powerii_exit
_Z5powerii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# collatz(int)
_Z7collatzi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # steps = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L8_1:
        # if n int!= 1 goto 3
        lw    $t0, 8($fp)
        li    $t1, 1
        bne   $t0, $t1, L8_3
        # goto 16
        j     L8_16
L8_3:
        # t2 = n int% 2
        lw    $t0, 8($fp)
        li    $t1, 2
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -12($fp)
        # if t2 int!= 0 goto 6
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L8_6
        # goto 10
        j     L8_10
L8_6:
        # t3 = 3 int* n
        li    $t0, 3
        lw    $t1, 8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t4 = t3 int+ 1
        lw    $t0, -16($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t1 = t4
        lw    $t0, -20($fp)
        sw    $t0, -8($fp)
        # goto 12
        j     L8_12
L8_10:
        # t5 = n int/ 2
        lw    $t0, 8($fp)
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -24($fp)
        # t1 = t5
        lw    $t0, -24($fp)
        sw    $t0, -8($fp)
L8_12:
        # n = t1
        lw    $t0, -8($fp)
        sw    $t0, 8($fp)
        # t6 = steps int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # steps = t6
        lw    $t0, -28($fp)
        sw    $t0, -4($fp)
        # goto 1
        j     L8_1
L8_16:
        # return steps
        lw    $v0, -4($fp)
        j     _Z7collatzi_exit
_Z7collatzi_exit:
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
        # a[0] = 42
        addiu $t8, $fp, -32
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 42
        sw    $t0, 0($t8)
        # a[4] = 7
        addiu $t8, $fp, -32
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 7
        sw    $t0, 0($t8)
        # a[8] = 19
        addiu $t8, $fp, -32
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 19
        sw    $t0, 0($t8)
        # a[12] = 3
        addiu $t8, $fp, -32
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # a[16] = 25
        addiu $t8, $fp, -32
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 25
        sw    $t0, 0($t8)
        # a[20] = 7
        addiu $t8, $fp, -32
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 7
        sw    $t0, 0($t8)
        # a[24] = 88
        addiu $t8, $fp, -32
        li    $t9, 24
        addu  $t8, $t8, $t9
        li    $t0, 88
        sw    $t0, 0($t8)
        # a[28] = 1
        addiu $t8, $fp, -32
        li    $t9, 28
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # t1 = int- 2
        li    $t0, 2
        negu  $t0, $t0
        sw    $t0, -140($fp)
        # t2 = int- 7
        li    $t0, 7
        negu  $t0, $t0
        sw    $t0, -144($fp)
        # b[0] = 5
        addiu $t8, $fp, -64
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 5
        sw    $t0, 0($t8)
        # b[4] = t1
        addiu $t8, $fp, -64
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, -140($fp)
        sw    $t0, 0($t8)
        # b[8] = 9
        addiu $t8, $fp, -64
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 9
        sw    $t0, 0($t8)
        # b[12] = 0
        addiu $t8, $fp, -64
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # b[16] = 9
        addiu $t8, $fp, -64
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 9
        sw    $t0, 0($t8)
        # b[20] = 14
        addiu $t8, $fp, -64
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 14
        sw    $t0, 0($t8)
        # b[24] = t2
        addiu $t8, $fp, -64
        li    $t9, 24
        addu  $t8, $t8, $t9
        lw    $t0, -144($fp)
        sw    $t0, 0($t8)
        # b[28] = 3
        addiu $t8, $fp, -64
        li    $t9, 28
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # t3 = &a
        addiu $t0, $fp, -32
        sw    $t0, -148($fp)
        # param t3
        # param 8
        # call bubble(int *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -148($fp)
        sw    $t0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        jal   _Z6bubblePii
        addiu $sp, $sp, 8
        # t4 = &b
        addiu $t0, $fp, -64
        sw    $t0, -152($fp)
        # param t4
        # param 0
        # param 7
        # call quick(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -152($fp)
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        li    $t0, 7
        sw    $t0, 8($sp)
        jal   _Z5quickPiii
        addiu $sp, $sp, 16
        # i.44 = 0
        li    $t0, 0
        sw    $t0, -68($fp)
L9_28:
        # if i.44 int< 8 goto 30
        lw    $t0, -68($fp)
        li    $t1, 8
        blt   $t0, $t1, L9_30
        # goto 38
        j     L9_38
L9_30:
        # t5 = i.44 int* 4
        lw    $t0, -68($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -156($fp)
        # t6 = a[t5]
        addiu $t8, $fp, -32
        lw    $t9, -156($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -160($fp)
        # param "%d "
        # param t6
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -160($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t7 = i.44 int+ 1
        lw    $t0, -68($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -164($fp)
        # i.44 = t7
        lw    $t0, -164($fp)
        sw    $t0, -68($fp)
        # goto 28
        j     L9_28
L9_38:
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i.45 = 0
        li    $t0, 0
        sw    $t0, -72($fp)
L9_41:
        # if i.45 int< 8 goto 43
        lw    $t0, -72($fp)
        li    $t1, 8
        blt   $t0, $t1, L9_43
        # goto 51
        j     L9_51
L9_43:
        # t8 = i.45 int* 4
        lw    $t0, -72($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -168($fp)
        # t9 = b[t8]
        addiu $t8, $fp, -64
        lw    $t9, -168($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -172($fp)
        # param "%d "
        # param t9
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -172($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t10 = i.45 int+ 1
        lw    $t0, -72($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -176($fp)
        # i.45 = t10
        lw    $t0, -176($fp)
        sw    $t0, -72($fp)
        # goto 41
        j     L9_41
L9_51:
        # t11 = &a
        addiu $t0, $fp, -32
        sw    $t0, -180($fp)
        # param t11
        # param 8
        # param 25
        # t12 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -180($fp)
        sw    $t0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, 25
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        sw    $v0, -184($fp)
        # t13 = &a
        addiu $t0, $fp, -32
        sw    $t0, -188($fp)
        # param t13
        # param 8
        # param 26
        # t14 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -188($fp)
        sw    $t0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, 26
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        sw    $v0, -192($fp)
        # t15 = &b
        addiu $t0, $fp, -64
        sw    $t0, -196($fp)
        # t16 = int- 7
        li    $t0, 7
        negu  $t0, $t0
        sw    $t0, -200($fp)
        # param t15
        # param 8
        # param t16
        # t17 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -196($fp)
        sw    $t0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        lw    $t0, -200($fp)
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        sw    $v0, -204($fp)
        # param "\n%d %d %d\n"
        # param t12
        # param t14
        # param t17
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -184($fp)
        sw    $t0, 4($sp)
        lw    $t0, -192($fp)
        sw    $t0, 8($sp)
        lw    $t0, -204($fp)
        sw    $t0, 12($sp)
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
        sw    $v0, -208($fp)
        # param 27
        # t19 = call collatz(int), 1
        addiu $sp, $sp, -8
        li    $t0, 27
        sw    $t0, 0($sp)
        jal   _Z7collatzi
        addiu $sp, $sp, 8
        sw    $v0, -212($fp)
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
        lw    $t0, -208($fp)
        sw    $t0, 8($sp)
        lw    $t0, -212($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # x[0] = 1
        addiu $t8, $fp, -96
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # x[4] = 2
        addiu $t8, $fp, -96
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # x[8] = 3
        addiu $t8, $fp, -96
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # x[12] = 4
        addiu $t8, $fp, -96
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 4
        sw    $t0, 0($t8)
        # x[16] = 5
        addiu $t8, $fp, -96
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 5
        sw    $t0, 0($t8)
        # x[20] = 6
        addiu $t8, $fp, -96
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 6
        sw    $t0, 0($t8)
        # y[0] = 7
        addiu $t8, $fp, -120
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 7
        sw    $t0, 0($t8)
        # y[4] = 8
        addiu $t8, $fp, -120
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 8
        sw    $t0, 0($t8)
        # y[8] = 9
        addiu $t8, $fp, -120
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 9
        sw    $t0, 0($t8)
        # y[12] = 10
        addiu $t8, $fp, -120
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 10
        sw    $t0, 0($t8)
        # y[16] = 11
        addiu $t8, $fp, -120
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 11
        sw    $t0, 0($t8)
        # y[20] = 12
        addiu $t8, $fp, -120
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 12
        sw    $t0, 0($t8)
        # t20 = &x
        addiu $t0, $fp, -96
        sw    $t0, -216($fp)
        # t21 = &y
        addiu $t0, $fp, -120
        sw    $t0, -220($fp)
        # t22 = &z
        addiu $t0, $fp, -136
        sw    $t0, -224($fp)
        # param t20
        # param t21
        # param t22
        # call multiply(int (*)[3], int (*)[2], int (*)[2]), 3
        addiu $sp, $sp, -16
        lw    $t0, -216($fp)
        sw    $t0, 0($sp)
        lw    $t0, -220($fp)
        sw    $t0, 4($sp)
        lw    $t0, -224($fp)
        sw    $t0, 8($sp)
        jal   _Z8multiplyPA3_iPA2_iS2_
        addiu $sp, $sp, 16
        # t23 = z[0]
        addiu $t8, $fp, -136
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -228($fp)
        # t24 = z[4]
        addiu $t8, $fp, -136
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -232($fp)
        # t25 = z[8]
        addiu $t8, $fp, -136
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -236($fp)
        # t26 = z[12]
        addiu $t8, $fp, -136
        li    $t9, 12
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -240($fp)
        # param "%d %d %d %d\n"
        # param t23
        # param t24
        # param t25
        # param t26
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -228($fp)
        sw    $t0, 4($sp)
        lw    $t0, -232($fp)
        sw    $t0, 8($sp)
        lw    $t0, -236($fp)
        sw    $t0, 12($sp)
        lw    $t0, -240($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 100
        # t27 = call primes(int), 1
        addiu $sp, $sp, -8
        li    $t0, 100
        sw    $t0, 0($sp)
        jal   _Z6primesi
        addiu $sp, $sp, 8
        sw    $v0, -244($fp)
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
        sw    $v0, -248($fp)
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
        sw    $v0, -252($fp)
        # param "%d %d %d\n"
        # param t27
        # param t28
        # param t29
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -244($fp)
        sw    $t0, 4($sp)
        lw    $t0, -248($fp)
        sw    $t0, 8($sp)
        lw    $t0, -252($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t30 = &a
        addiu $t0, $fp, -32
        sw    $t0, -256($fp)
        # param t30
        # param 8
        # param 88
        # t31 = call search(int *, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -256($fp)
        sw    $t0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        li    $t0, 88
        sw    $t0, 8($sp)
        jal   _Z6searchPiii
        addiu $sp, $sp, 16
        sw    $v0, -260($fp)
        # return t31
        lw    $v0, -260($fp)
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
