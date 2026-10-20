# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t28_o3.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g_calls:
        .byte 0, 0, 0, 0
str0:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str1:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str2:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str3:
        .byte 37, 100, 32, 37, 100, 10, 0

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

# square(int)
_Z6squarei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = v int* v
        lw    $t0, 8($fp)
        lw    $t1, 8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -4($fp)
        # return t1
        lw    $v0, -4($fp)
        j     _Z6squarei_exit
_Z6squarei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# clamp(int, int, int)
_Z5clampiii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # if v int< lo goto 2
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        blt   $t0, $t1, L1_2
        # goto 3
        j     L1_3
L1_2:
        # return lo
        lw    $v0, 12($fp)
        j     _Z5clampiii_exit
L1_3:
        # if v int> hi goto 5
        lw    $t0, 8($fp)
        lw    $t1, 16($fp)
        bgt   $t0, $t1, L1_5
        # goto 6
        j     L1_6
L1_5:
        # return hi
        lw    $v0, 16($fp)
        j     _Z5clampiii_exit
L1_6:
        # return v
        lw    $v0, 8($fp)
        j     _Z5clampiii_exit
_Z5clampiii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# counted(int)
_Z7countedi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = calls int+ 1
        lw    $t0, g_calls
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # calls = t1
        lw    $t0, -4($fp)
        sw    $t0, g_calls
        # t2 = v int+ calls
        lw    $t0, 8($fp)
        lw    $t1, g_calls
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _Z7countedi_exit
_Z7countedi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# bump(int &, int)
_Z4bumpRii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = *r
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = t1 int+ by
        lw    $t0, -4($fp)
        lw    $t1, 12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # *r = t2
        lw    $t8, 8($fp)
        lw    $t0, -8($fp)
        sw    $t0, 0($t8)
        # return
        j     _Z4bumpRii_exit
_Z4bumpRii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# total(struct Pair)
_Z5total4Pair:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t1 = p[0]
        addiu $t8, $fp, 8
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = t1 int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # p[0] = t2
        addiu $t8, $fp, 8
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, -8($fp)
        sw    $t0, 0($t8)
        # t3 = p[0]
        addiu $t8, $fp, 8
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t4 = p[4]
        addiu $t8, $fp, 8
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = t3 int+ t4
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # return t5
        lw    $v0, -20($fp)
        j     _Z5total4Pair_exit
_Z5total4Pair_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# fact(int)
_Z4facti:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if n int<= 1 goto 2
        lw    $t0, 8($fp)
        li    $t1, 1
        ble   $t0, $t1, L5_2
        # goto 4
        j     L5_4
L5_2:
        # t1 = 1
        li    $t0, 1
        sw    $t0, -4($fp)
        # goto 9
        j     L5_9
L5_4:
        # t2 = n int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # param t2
        # t3 = call fact(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        jal   _Z4facti
        addiu $sp, $sp, 8
        sw    $v0, -12($fp)
        # t4 = n int* t3
        lw    $t0, 8($fp)
        lw    $t1, -12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t1 = t4
        lw    $t0, -16($fp)
        sw    $t0, -4($fp)
L5_9:
        # return t1
        lw    $v0, -4($fp)
        j     _Z4facti_exit
_Z4facti_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# gcd(int, int)
_Z3gcdii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # if b int== 0 goto 2
        lw    $t0, 12($fp)
        li    $t1, 0
        beq   $t0, $t1, L6_2
        # goto 3
        j     L6_3
L6_2:
        # return a
        lw    $v0, 8($fp)
        j     _Z3gcdii_exit
L6_3:
        # t1 = a int% b
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -4($fp)
        # param b
        # param t1
        # t2 = call gcd(int, int), 2
        addiu $sp, $sp, -8
        lw    $t0, 12($fp)
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   _Z3gcdii
        addiu $sp, $sp, 8
        sw    $v0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _Z3gcdii_exit
_Z3gcdii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# sumTo(int, int)
_Z5sumToii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if n int== 0 goto 2
        lw    $t0, 8($fp)
        li    $t1, 0
        beq   $t0, $t1, L7_2
        # goto 3
        j     L7_3
L7_2:
        # return acc
        lw    $v0, 12($fp)
        j     _Z5sumToii_exit
L7_3:
        # t1 = n int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = acc int+ n
        lw    $t0, 12($fp)
        lw    $t1, 8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # param t1
        # param t2
        # t3 = call sumTo(int, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        lw    $t0, -8($fp)
        sw    $t0, 4($sp)
        jal   _Z5sumToii
        addiu $sp, $sp, 8
        sw    $v0, -12($fp)
        # return t3
        lw    $v0, -12($fp)
        j     _Z5sumToii_exit
_Z5sumToii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# countDown(int)
_Z9countDowni:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # if n int<= 0 goto 2
        lw    $t0, 8($fp)
        li    $t1, 0
        ble   $t0, $t1, L8_2
        # goto 3
        j     L8_3
L8_2:
        # return 0
        li    $v0, 0
        j     _Z9countDowni_exit
L8_3:
        # t1 = n int- 2
        lw    $t0, 8($fp)
        li    $t1, 2
        subu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # param t1
        # t2 = call countDown(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        jal   _Z9countDowni
        addiu $sp, $sp, 8
        sw    $v0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _Z9countDowni_exit
_Z9countDowni_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# invariant(int, int)
_Z9invariantii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        # s = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L9_2:
        # if i int< n goto 4
        lw    $t0, -8($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L9_4
        # goto 19
        j     L9_19
L9_4:
        # t1 = k int* 3
        lw    $t0, 12($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t2 = t1 int+ 1
        lw    $t0, -16($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # scale = t2
        lw    $t0, -20($fp)
        sw    $t0, -12($fp)
        # t3 = i int* scale
        lw    $t0, -8($fp)
        lw    $t1, -12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t4 = s int+ t3
        lw    $t0, -4($fp)
        lw    $t1, -24($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # s = t4
        lw    $t0, -28($fp)
        sw    $t0, -4($fp)
        # if i int== 2 goto 12
        lw    $t0, -8($fp)
        li    $t1, 2
        beq   $t0, $t1, L9_12
        # goto 13
        j     L9_13
L9_12:
        # goto 16
        j     L9_16
L9_13:
        # t5 = k int* 3
        lw    $t0, 12($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t6 = s int+ t5
        lw    $t0, -4($fp)
        lw    $t1, -32($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # s = t6
        lw    $t0, -36($fp)
        sw    $t0, -4($fp)
L9_16:
        # t7 = i int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -40($fp)
        # i = t7
        lw    $t0, -40($fp)
        sw    $t0, -8($fp)
        # goto 2
        j     L9_2
L9_19:
        # return s
        lw    $v0, -4($fp)
        j     _Z9invariantii_exit
_Z9invariantii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# notInvariant(int)
_Z12notInvarianti:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # s = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # k = 1
        li    $t0, 1
        sw    $t0, -8($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -12($fp)
L10_3:
        # if i int< n goto 5
        lw    $t0, -12($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L10_5
        # goto 14
        j     L10_14
L10_5:
        # t1 = k int* 3
        lw    $t0, -8($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # v = t1
        lw    $t0, -20($fp)
        sw    $t0, -16($fp)
        # t2 = s int+ v
        lw    $t0, -4($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # s = t2
        lw    $t0, -24($fp)
        sw    $t0, -4($fp)
        # t3 = k int+ i
        lw    $t0, -8($fp)
        lw    $t1, -12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # k = t3
        lw    $t0, -28($fp)
        sw    $t0, -8($fp)
        # t4 = i int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # i = t4
        lw    $t0, -32($fp)
        sw    $t0, -12($fp)
        # goto 3
        j     L10_3
L10_14:
        # return s
        lw    $v0, -4($fp)
        j     _Z12notInvarianti_exit
_Z12notInvarianti_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# zeroTrips(int, int)
_Z9zeroTripsii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # s = 7
        li    $t0, 7
        sw    $t0, -4($fp)
L11_1:
        # if n int> 0 goto 3
        lw    $t0, 8($fp)
        li    $t1, 0
        bgt   $t0, $t1, L11_3
        # goto 9
        j     L11_9
L11_3:
        # t1 = 100 int/ d
        li    $t0, 100
        lw    $t1, 12($fp)
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -8($fp)
        # t2 = s int+ t1
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # s = t2
        lw    $t0, -12($fp)
        sw    $t0, -4($fp)
        # t3 = n int- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # n = t3
        lw    $t0, -16($fp)
        sw    $t0, 8($fp)
        # goto 1
        j     L11_1
L11_9:
        # return s
        lw    $v0, -4($fp)
        j     _Z9zeroTripsii_exit
_Z9zeroTripsii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# nested(int, int)
_Z6nestedii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -160
        # s = 0
        li    $t0, 0
        sw    $t0, -84($fp)
        # r.32 = 0
        li    $t0, 0
        sw    $t0, -88($fp)
L12_2:
        # if r.32 int< rows goto 4
        lw    $t0, -88($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L12_4
        # goto 19
        j     L12_19
L12_4:
        # c.33 = 0
        li    $t0, 0
        sw    $t0, -92($fp)
L12_5:
        # if c.33 int< cols goto 7
        lw    $t0, -92($fp)
        lw    $t1, 12($fp)
        blt   $t0, $t1, L12_7
        # goto 16
        j     L12_16
L12_7:
        # t1 = r.32 int* 5
        lw    $t0, -88($fp)
        li    $t1, 5
        mul   $t0, $t0, $t1
        sw    $t0, -104($fp)
        # t2 = t1 int+ c.33
        lw    $t0, -104($fp)
        lw    $t1, -92($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -108($fp)
        # t3 = t2 int* 4
        lw    $t0, -108($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -112($fp)
        # t4 = r.32 int* cols
        lw    $t0, -88($fp)
        lw    $t1, 12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -116($fp)
        # t5 = t4 int+ c.33
        lw    $t0, -116($fp)
        lw    $t1, -92($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -120($fp)
        # grid[t3] = t5
        addiu $t8, $fp, -80
        lw    $t9, -112($fp)
        addu  $t8, $t8, $t9
        lw    $t0, -120($fp)
        sw    $t0, 0($t8)
        # t6 = c.33 int+ 1
        lw    $t0, -92($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -124($fp)
        # c.33 = t6
        lw    $t0, -124($fp)
        sw    $t0, -92($fp)
        # goto 5
        j     L12_5
L12_16:
        # t7 = r.32 int+ 1
        lw    $t0, -88($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -128($fp)
        # r.32 = t7
        lw    $t0, -128($fp)
        sw    $t0, -88($fp)
        # goto 2
        j     L12_2
L12_19:
        # r.34 = 0
        li    $t0, 0
        sw    $t0, -96($fp)
L12_20:
        # if r.34 int< rows goto 22
        lw    $t0, -96($fp)
        lw    $t1, 8($fp)
        blt   $t0, $t1, L12_22
        # goto 37
        j     L12_37
L12_22:
        # c.35 = 0
        li    $t0, 0
        sw    $t0, -100($fp)
L12_23:
        # if c.35 int< cols goto 25
        lw    $t0, -100($fp)
        lw    $t1, 12($fp)
        blt   $t0, $t1, L12_25
        # goto 34
        j     L12_34
L12_25:
        # t8 = r.34 int* 5
        lw    $t0, -96($fp)
        li    $t1, 5
        mul   $t0, $t0, $t1
        sw    $t0, -132($fp)
        # t9 = t8 int+ c.35
        lw    $t0, -132($fp)
        lw    $t1, -100($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -136($fp)
        # t10 = t9 int* 4
        lw    $t0, -136($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -140($fp)
        # t11 = grid[t10]
        addiu $t8, $fp, -80
        lw    $t9, -140($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -144($fp)
        # t12 = s int+ t11
        lw    $t0, -84($fp)
        lw    $t1, -144($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -148($fp)
        # s = t12
        lw    $t0, -148($fp)
        sw    $t0, -84($fp)
        # t13 = c.35 int+ 1
        lw    $t0, -100($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -152($fp)
        # c.35 = t13
        lw    $t0, -152($fp)
        sw    $t0, -100($fp)
        # goto 23
        j     L12_23
L12_34:
        # t14 = r.34 int+ 1
        lw    $t0, -96($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -156($fp)
        # r.34 = t14
        lw    $t0, -156($fp)
        sw    $t0, -96($fp)
        # goto 20
        j     L12_20
L12_37:
        # return s
        lw    $v0, -84($fp)
        j     _Z6nestedii_exit
_Z6nestedii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# shared(int, int, int)
_Z6sharediii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        # t1 = x int* y
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = t1 int+ 2
        lw    $t0, -12($fp)
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # a = t2
        lw    $t0, -16($fp)
        sw    $t0, -4($fp)
        # if flag int!= 0 goto 5
        lw    $t0, 16($fp)
        li    $t1, 0
        bne   $t0, $t1, L13_5
        # goto 9
        j     L13_9
L13_5:
        # t3 = x int* y
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t4 = t3 int+ 2
        lw    $t0, -20($fp)
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # b = t4
        lw    $t0, -24($fp)
        sw    $t0, -8($fp)
        # goto 14
        j     L13_14
L13_9:
        # t5 = x int+ 1
        lw    $t0, 8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # x = t5
        lw    $t0, -28($fp)
        sw    $t0, 8($fp)
        # t6 = x int* y
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t7 = t6 int+ 2
        lw    $t0, -32($fp)
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # b = t7
        lw    $t0, -36($fp)
        sw    $t0, -8($fp)
L13_14:
        # t8 = a int* 1000
        lw    $t0, -4($fp)
        li    $t1, 1000
        mul   $t0, $t0, $t1
        sw    $t0, -40($fp)
        # t9 = t8 int+ b
        lw    $t0, -40($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # t10 = x int* y
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -48($fp)
        # t11 = t9 int+ t10
        lw    $t0, -44($fp)
        lw    $t1, -48($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -52($fp)
        # return t11
        lw    $v0, -52($fp)
        j     _Z6sharediii_exit
_Z6sharediii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# memory(int)
_Z6memoryi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -104
        # arr[0] = 1
        addiu $t8, $fp, -16
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # arr[4] = 2
        addiu $t8, $fp, -16
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # arr[8] = 3
        addiu $t8, $fp, -16
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 3
        sw    $t0, 0($t8)
        # arr[12] = 4
        addiu $t8, $fp, -16
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 4
        sw    $t0, 0($t8)
        # t1 = &arr
        addiu $t0, $fp, -16
        sw    $t0, -40($fp)
        # t2 = t1 ptr+ 4
        lw    $t0, -40($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # p = t2
        lw    $t0, -44($fp)
        sw    $t0, -20($fp)
        # t3 = &arr
        addiu $t0, $fp, -16
        sw    $t0, -48($fp)
        # q = t3
        lw    $t0, -48($fp)
        sw    $t0, -24($fp)
        # t4 = i int* 4
        lw    $t0, 8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -52($fp)
        # arr[t4] = 10
        addiu $t8, $fp, -16
        lw    $t9, -52($fp)
        addu  $t8, $t8, $t9
        li    $t0, 10
        sw    $t0, 0($t8)
        # t5 = i int* 4
        lw    $t0, 8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -56($fp)
        # t6 = arr[t5]
        addiu $t8, $fp, -16
        lw    $t9, -56($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -60($fp)
        # a = t6
        lw    $t0, -60($fp)
        sw    $t0, -28($fp)
        # *p = 20
        lw    $t8, -20($fp)
        li    $t0, 20
        sw    $t0, 0($t8)
        # t7 = i int* 4
        lw    $t0, 8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -64($fp)
        # t8 = arr[t7]
        addiu $t8, $fp, -16
        lw    $t9, -64($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -68($fp)
        # b = t8
        lw    $t0, -68($fp)
        sw    $t0, -32($fp)
        # t9 = i int* 4
        lw    $t0, 8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -72($fp)
        # t10 = q ptr+ t9
        lw    $t0, -24($fp)
        lw    $t1, -72($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # *t10 = 30
        lw    $t8, -76($fp)
        li    $t0, 30
        sw    $t0, 0($t8)
        # t11 = i int* 4
        lw    $t0, 8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -80($fp)
        # t12 = arr[t11]
        addiu $t8, $fp, -16
        lw    $t9, -80($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -84($fp)
        # t13 = *p
        lw    $t8, -20($fp)
        lw    $t0, 0($t8)
        sw    $t0, -88($fp)
        # t14 = t12 int+ t13
        lw    $t0, -84($fp)
        lw    $t1, -88($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -92($fp)
        # c = t14
        lw    $t0, -92($fp)
        sw    $t0, -36($fp)
        # t15 = a int+ b
        lw    $t0, -28($fp)
        lw    $t1, -32($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -96($fp)
        # t16 = t15 int+ c
        lw    $t0, -96($fp)
        lw    $t1, -36($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -100($fp)
        # return t16
        lw    $v0, -100($fp)
        j     _Z6memoryi_exit
_Z6memoryi_exit:
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
        addiu $sp, $sp, -152
        # x = 5
        li    $t0, 5
        sw    $t0, -4($fp)
        # t1 = &x
        addiu $t0, $fp, -4
        sw    $t0, -32($fp)
        # param 3
        # t2 = call square(int), 1
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        jal   _Z6squarei
        addiu $sp, $sp, 8
        sw    $v0, -36($fp)
        # param t1
        # param t2
        # call bump(int &, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -32($fp)
        sw    $t0, 0($sp)
        lw    $t0, -36($fp)
        sw    $t0, 4($sp)
        jal   _Z4bumpRii
        addiu $sp, $sp, 8
        # p[0] = 1
        addiu $t8, $fp, -12
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 1
        sw    $t0, 0($t8)
        # p[4] = 2
        addiu $t8, $fp, -12
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 2
        sw    $t0, 0($t8)
        # param p
        # t3 = call total(struct Pair), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -12
        li    $a2, 8
        jal   __memcpy
        jal   _Z5total4Pair
        addiu $sp, $sp, 8
        sw    $v0, -40($fp)
        # param p
        # t4 = call total(struct Pair), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -12
        li    $a2, 8
        jal   __memcpy
        jal   _Z5total4Pair
        addiu $sp, $sp, 8
        sw    $v0, -44($fp)
        # t5 = t3 int+ t4
        lw    $t0, -40($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # t = t5
        lw    $t0, -48($fp)
        sw    $t0, -16($fp)
        # t6 = p[0]
        addiu $t8, $fp, -12
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -52($fp)
        # t7 = int- 5
        li    $t0, 5
        negu  $t0, $t0
        sw    $t0, -56($fp)
        # param t7
        # param 0
        # param 9
        # t8 = call clamp(int, int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -56($fp)
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z5clampiii
        addiu $sp, $sp, 16
        sw    $v0, -60($fp)
        # param 50
        # param 0
        # param 9
        # t9 = call clamp(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 50
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z5clampiii
        addiu $sp, $sp, 16
        sw    $v0, -64($fp)
        # param 4
        # param 0
        # param 9
        # t10 = call clamp(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 4
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z5clampiii
        addiu $sp, $sp, 16
        sw    $v0, -68($fp)
        # t11 = t9 int+ t10
        lw    $t0, -64($fp)
        lw    $t1, -68($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -72($fp)
        # param "%d %d %d %d %d\n"
        # param x
        # param t
        # param t6
        # param t8
        # param t11
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        lw    $t0, -16($fp)
        sw    $t0, 8($sp)
        lw    $t0, -52($fp)
        sw    $t0, 12($sp)
        lw    $t0, -60($fp)
        sw    $t0, 16($sp)
        lw    $t0, -72($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 1
        # t12 = call counted(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z7countedi
        addiu $sp, $sp, 8
        sw    $v0, -76($fp)
        # c1 = t12
        lw    $t0, -76($fp)
        sw    $t0, -20($fp)
        # param 1
        # t13 = call counted(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z7countedi
        addiu $sp, $sp, 8
        sw    $v0, -80($fp)
        # c2 = t13
        lw    $t0, -80($fp)
        sw    $t0, -24($fp)
        # param 1
        # t14 = call counted(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z7countedi
        addiu $sp, $sp, 8
        sw    $v0, -84($fp)
        # c3 = t14
        lw    $t0, -84($fp)
        sw    $t0, -28($fp)
        # param 6
        # t15 = call fact(int), 1
        addiu $sp, $sp, -8
        li    $t0, 6
        sw    $t0, 0($sp)
        jal   _Z4facti
        addiu $sp, $sp, 8
        sw    $v0, -88($fp)
        # param "%d %d %d %d %d\n"
        # param c1
        # param c2
        # param c3
        # param calls
        # param t15
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -20($fp)
        sw    $t0, 4($sp)
        lw    $t0, -24($fp)
        sw    $t0, 8($sp)
        lw    $t0, -28($fp)
        sw    $t0, 12($sp)
        lw    $t0, g_calls
        sw    $t0, 16($sp)
        lw    $t0, -88($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 1071
        # param 462
        # t16 = call gcd(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 1071
        sw    $t0, 0($sp)
        li    $t0, 462
        sw    $t0, 4($sp)
        jal   _Z3gcdii
        addiu $sp, $sp, 8
        sw    $v0, -92($fp)
        # param 17
        # param 5
        # t17 = call gcd(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 17
        sw    $t0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _Z3gcdii
        addiu $sp, $sp, 8
        sw    $v0, -96($fp)
        # param 100
        # param 0
        # t18 = call sumTo(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 100
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        jal   _Z5sumToii
        addiu $sp, $sp, 8
        sw    $v0, -100($fp)
        # param 9
        # t19 = call countDown(int), 1
        addiu $sp, $sp, -8
        li    $t0, 9
        sw    $t0, 0($sp)
        jal   _Z9countDowni
        addiu $sp, $sp, 8
        sw    $v0, -104($fp)
        # param "%d %d %d %d\n"
        # param t16
        # param t17
        # param t18
        # param t19
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str1
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
        # param 5
        # param 2
        # t20 = call invariant(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 5
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        jal   _Z9invariantii
        addiu $sp, $sp, 8
        sw    $v0, -108($fp)
        # param 0
        # param 9
        # t21 = call invariant(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 0
        sw    $t0, 0($sp)
        li    $t0, 9
        sw    $t0, 4($sp)
        jal   _Z9invariantii
        addiu $sp, $sp, 8
        sw    $v0, -112($fp)
        # param 5
        # t22 = call notInvariant(int), 1
        addiu $sp, $sp, -8
        li    $t0, 5
        sw    $t0, 0($sp)
        jal   _Z12notInvarianti
        addiu $sp, $sp, 8
        sw    $v0, -116($fp)
        # param 0
        # param 0
        # t23 = call zeroTrips(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 0
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        jal   _Z9zeroTripsii
        addiu $sp, $sp, 8
        sw    $v0, -120($fp)
        # param "%d %d %d %d\n"
        # param t20
        # param t21
        # param t22
        # param t23
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -108($fp)
        sw    $t0, 4($sp)
        lw    $t0, -112($fp)
        sw    $t0, 8($sp)
        lw    $t0, -116($fp)
        sw    $t0, 12($sp)
        lw    $t0, -120($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 3
        # param 4
        # t24 = call zeroTrips(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        jal   _Z9zeroTripsii
        addiu $sp, $sp, 8
        sw    $v0, -124($fp)
        # param 4
        # param 5
        # t25 = call nested(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 4
        sw    $t0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _Z6nestedii
        addiu $sp, $sp, 8
        sw    $v0, -128($fp)
        # param 2
        # param 3
        # t26 = call nested(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        jal   _Z6nestedii
        addiu $sp, $sp, 8
        sw    $v0, -132($fp)
        # param "%d %d %d\n"
        # param t24
        # param t25
        # param t26
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -124($fp)
        sw    $t0, 4($sp)
        lw    $t0, -128($fp)
        sw    $t0, 8($sp)
        lw    $t0, -132($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 3
        # param 4
        # param 1
        # t27 = call shared(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 3
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        li    $t0, 1
        sw    $t0, 8($sp)
        jal   _Z6sharediii
        addiu $sp, $sp, 16
        sw    $v0, -136($fp)
        # param 3
        # param 4
        # param 0
        # t28 = call shared(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 3
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        li    $t0, 0
        sw    $t0, 8($sp)
        jal   _Z6sharediii
        addiu $sp, $sp, 16
        sw    $v0, -140($fp)
        # param "%d %d\n"
        # param t27
        # param t28
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -136($fp)
        sw    $t0, 4($sp)
        lw    $t0, -140($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 1
        # t29 = call memory(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z6memoryi
        addiu $sp, $sp, 8
        sw    $v0, -144($fp)
        # param 2
        # t30 = call memory(int), 1
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        jal   _Z6memoryi
        addiu $sp, $sp, 8
        sw    $v0, -148($fp)
        # param "%d %d\n"
        # param t29
        # param t30
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -144($fp)
        sw    $t0, 4($sp)
        lw    $t0, -148($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # return calls
        lw    $v0, g_calls
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
