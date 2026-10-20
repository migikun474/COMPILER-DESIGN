# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t28_o3.c
#  Optimization : -O1 (TAC optimizations, registers, peephole)
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
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -8($fp)
        sw    $s1, -12($fp)
        lw    $s1, 8($fp)
        # t1 = v int* v
        mul   $s0, $s1, $s1
        # return t1
        move  $v0, $s0
        j     _Z6squarei_exit
_Z6squarei_exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# clamp(int, int, int)
_Z5clampiii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        sw    $s2, -12($fp)
        lw    $s0, 8($fp)
        lw    $s1, 12($fp)
        lw    $s2, 16($fp)
        # if v int>= lo goto 2
        bge   $s0, $s1, L1_2
        # return lo
        move  $v0, $s1
        j     _Z5clampiii_exit
L1_2:
        # if v int<= hi goto 4
        ble   $s0, $s2, L1_4
        # return hi
        move  $v0, $s2
        j     _Z5clampiii_exit
L1_4:
        # return v
        move  $v0, $s0
        j     _Z5clampiii_exit
_Z5clampiii_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        lw    $s2, -12($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# counted(int)
_Z7countedi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        sw    $s2, -20($fp)
        lw    $s2, 8($fp)
        # t1 = calls int+ 1
        lw    $t0, g_calls
        addiu $s0, $t0, 1
        # calls = t1
        move  $t0, $s0
        sw    $t0, g_calls
        # t2 = v int+ t1
        addu  $s1, $s2, $s0
        # return t2
        move  $v0, $s1
        j     _Z7countedi_exit
_Z7countedi_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        lw    $s2, -20($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# bump(int &, int)
_Z4bumpRii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        sw    $s2, -20($fp)
        sw    $s3, -24($fp)
        lw    $s2, 8($fp)
        lw    $s3, 12($fp)
        # t1 = *r
        lw    $s0, 0($s2)
        # t2 = t1 int+ by
        addu  $s1, $s0, $s3
        # *r = t2
        sw    $s1, 0($s2)
        # return
        j     _Z4bumpRii_exit
_Z4bumpRii_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        lw    $s2, -20($fp)
        lw    $s3, -24($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# total(struct Pair)
_Z5total4Pair:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        sw    $s0, -24($fp)
        sw    $s1, -20($fp)
        sw    $s2, -28($fp)
        # t1 = p[0]
        lw    $s1, 8($fp)
        # t2 = t1 int+ 1
        addiu $s0, $s1, 1
        # p[0] = t2
        sw    $s0, 8($fp)
        # t4 = p[4]
        lw    $s1, 12($fp)
        # t5 = t2 int+ t4
        addu  $s2, $s0, $s1
        # return t5
        move  $v0, $s2
        j     _Z5total4Pair_exit
_Z5total4Pair_exit:
        lw    $s0, -24($fp)
        lw    $s1, -20($fp)
        lw    $s2, -28($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# fact(int)
_Z4facti:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        sw    $s0, -16($fp)
        sw    $s1, -28($fp)
        sw    $s2, -20($fp)
        sw    $s3, -24($fp)
        lw    $s1, 8($fp)
        # if n int> 1 goto 3
        li    $t1, 1
        bgt   $s1, $t1, L5_3
        # t1 = 1
        li    $s0, 1
        # goto 7
        j     L5_7
L5_3:
        # t2 = n int- 1
        addiu $s2, $s1, -1
        # param t2
        # t3 = call fact(int), 1
        addiu $sp, $sp, -8
        sw    $s2, 0($sp)
        jal   _Z4facti
        addiu $sp, $sp, 8
        move  $s3, $v0
        # t1 = n int* t3
        mul   $s0, $s1, $s3
L5_7:
        # return t1
        move  $v0, $s0
        j     _Z4facti_exit
_Z4facti_exit:
        lw    $s0, -16($fp)
        lw    $s1, -28($fp)
        lw    $s2, -20($fp)
        lw    $s3, -24($fp)
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
        addiu $sp, $sp, -24
        sw    $s0, -20($fp)
        sw    $s1, -12($fp)
        sw    $s2, -16($fp)
        lw    $s2, 8($fp)
        lw    $s0, 12($fp)
        # if b int!= 0 goto 2
        bne   $s0, $zero, L6_2
        # return a
        move  $v0, $s2
        j     _Z3gcdii_exit
L6_2:
        # t1 = a int% b
        div   $s2, $s0
        mfhi  $s1
        # param b
        # param t1
        # t2 = call gcd(int, int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        sw    $s1, 4($sp)
        jal   _Z3gcdii
        addiu $sp, $sp, 8
        move  $s2, $v0
        # return t2
        move  $v0, $s2
        j     _Z3gcdii_exit
_Z3gcdii_exit:
        lw    $s0, -20($fp)
        lw    $s1, -12($fp)
        lw    $s2, -16($fp)
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
        addiu $sp, $sp, -32
        sw    $s0, -24($fp)
        sw    $s1, -16($fp)
        sw    $s2, -20($fp)
        sw    $s3, -28($fp)
        lw    $s0, 8($fp)
        lw    $s3, 12($fp)
        # if n int!= 0 goto 2
        bne   $s0, $zero, L7_2
        # return acc
        move  $v0, $s3
        j     _Z5sumToii_exit
L7_2:
        # t1 = n int- 1
        addiu $s1, $s0, -1
        # t2 = acc int+ n
        addu  $s2, $s3, $s0
        # param t1
        # param t2
        # t3 = call sumTo(int, int), 2
        addiu $sp, $sp, -8
        sw    $s1, 0($sp)
        sw    $s2, 4($sp)
        jal   _Z5sumToii
        addiu $sp, $sp, 8
        move  $s0, $v0
        # return t3
        move  $v0, $s0
        j     _Z5sumToii_exit
_Z5sumToii_exit:
        lw    $s0, -24($fp)
        lw    $s1, -16($fp)
        lw    $s2, -20($fp)
        lw    $s3, -28($fp)
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
        addiu $sp, $sp, -16
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        lw    $s1, 8($fp)
        # if n int> 0 goto 2
        bgt   $s1, $zero, L8_2
        # return 0
        li    $v0, 0
        j     _Z9countDowni_exit
L8_2:
        # t1 = n int- 2
        addiu $s0, $s1, -2
        # param t1
        # t2 = call countDown(int), 1
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        jal   _Z9countDowni
        addiu $sp, $sp, 8
        move  $s1, $v0
        # return t2
        move  $v0, $s1
        j     _Z9countDowni_exit
_Z9countDowni_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# invariant(int, int)
_Z9invariantii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        sw    $s0, -60($fp)
        sw    $s1, -56($fp)
        sw    $s2, -36($fp)
        sw    $s3, -32($fp)
        sw    $s4, -40($fp)
        sw    $s5, -44($fp)
        sw    $s6, -52($fp)
        sw    $s7, -48($fp)
        lw    $s7, 8($fp)
        lw    $s6, 12($fp)
        # s = 0
        li    $s1, 0
        # i = 0
        li    $s0, 0
L9_2:
        # if i int>= n goto 13
        bge   $s0, $s7, L9_13
        # t1 = k int* 3
        li    $t1, 3
        mul   $s3, $s6, $t1
        # t2 = t1 int+ 1
        addiu $s2, $s3, 1
        # scale = t2
        move  $t0, $s2
        sw    $t0, -12($fp)
        # t3 = i int* t2
        mul   $s4, $s0, $s2
        # s = s int+ t3
        addu  $s1, $s1, $s4
        # if i int== 2 goto 11
        li    $t1, 2
        beq   $s0, $t1, L9_11
        # t5 = k int* 3
        li    $t1, 3
        mul   $s5, $s6, $t1
        # s = s int+ t5
        addu  $s1, $s1, $s5
L9_11:
        # i = i int+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L9_2
L9_13:
        # return s
        move  $v0, $s1
        j     _Z9invariantii_exit
_Z9invariantii_exit:
        lw    $s0, -60($fp)
        lw    $s1, -56($fp)
        lw    $s2, -36($fp)
        lw    $s3, -32($fp)
        lw    $s4, -40($fp)
        lw    $s5, -44($fp)
        lw    $s6, -52($fp)
        lw    $s7, -48($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# notInvariant(int)
_Z12notInvarianti:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -40($fp)
        sw    $s1, -36($fp)
        sw    $s2, -24($fp)
        sw    $s3, -32($fp)
        sw    $s4, -28($fp)
        sw    $s5, -44($fp)
        lw    $s4, 8($fp)
        # s = 0
        li    $s3, 0
        # k = 1
        li    $s1, 1
        # i = 0
        li    $s0, 0
L10_3:
        # if i int>= n goto 10
        bge   $s0, $s4, L10_10
        # t1 = k int* 3
        li    $t1, 3
        mul   $s2, $s1, $t1
        # v = t1
        move  $s5, $s2
        # s = s int+ t1
        addu  $s3, $s3, $s2
        # k = k int+ i
        addu  $s1, $s1, $s0
        # i = i int+ 1
        addiu $s0, $s0, 1
        # goto 3
        j     L10_3
L10_10:
        # return s
        move  $v0, $s3
        j     _Z12notInvarianti_exit
_Z12notInvarianti_exit:
        lw    $s0, -40($fp)
        lw    $s1, -36($fp)
        lw    $s2, -24($fp)
        lw    $s3, -32($fp)
        lw    $s4, -28($fp)
        lw    $s5, -44($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# zeroTrips(int, int)
_Z9zeroTripsii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -16($fp)
        sw    $s1, -24($fp)
        sw    $s2, -12($fp)
        sw    $s3, -20($fp)
        lw    $s0, 8($fp)
        lw    $s3, 12($fp)
        # s = 7
        li    $s1, 7
L11_1:
        # if n int<= 0 goto 6
        ble   $s0, $zero, L11_6
        # t1 = 100 int/ d
        li    $t0, 100
        div   $t0, $s3
        mflo  $s2
        # s = s int+ t1
        addu  $s1, $s1, $s2
        # n = n int- 1
        addiu $s0, $s0, -1
        # goto 1
        j     L11_1
L11_6:
        # return s
        move  $v0, $s1
        j     _Z9zeroTripsii_exit
_Z9zeroTripsii_exit:
        lw    $s0, -16($fp)
        lw    $s1, -24($fp)
        lw    $s2, -12($fp)
        lw    $s3, -20($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# nested(int, int)
_Z6nestedii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -168
        sw    $s0, -160($fp)
        sw    $s1, -164($fp)
        sw    $s2, -156($fp)
        sw    $s3, -168($fp)
        sw    $s4, -140($fp)
        sw    $s5, -144($fp)
        sw    $s6, -148($fp)
        sw    $s7, -152($fp)
        lw    $s1, 12($fp)
        # s = 0
        li    $s3, 0
        # r.32 = 0
        li    $s2, 0
L12_2:
        # if r.32 int>= rows goto 15
        lw    $t1, 8($fp)
        bge   $s2, $t1, L12_15
        # c.33 = 0
        li    $s0, 0
L12_4:
        # if c.33 int>= cols goto 13
        bge   $s0, $s1, L12_13
        # t1 = r.32 int* 5
        li    $t1, 5
        mul   $s4, $s2, $t1
        # t2 = t1 int+ c.33
        addu  $s5, $s4, $s0
        # t3 = t2 int<< 2
        sll   $s6, $s5, 2
        # t4 = r.32 int* cols
        mul   $s7, $s2, $s1
        # t5 = t4 int+ c.33
        addu  $t0, $s7, $s0
        sw    $t0, -120($fp)
        # grid[t3] = t5
        addiu $t8, $fp, -80
        addu  $t8, $t8, $s6
        lw    $t0, -120($fp)
        sw    $t0, 0($t8)
        # c.33 = c.33 int+ 1
        addiu $s0, $s0, 1
        # goto 4
        j     L12_4
L12_13:
        # r.32 = r.32 int+ 1
        addiu $s2, $s2, 1
        # goto 2
        j     L12_2
L12_15:
        # r.34 = 0
        li    $s7, 0
L12_16:
        # if r.34 int>= rows goto 28
        lw    $t1, 8($fp)
        bge   $s7, $t1, L12_28
        # c.35 = 0
        li    $s0, 0
L12_18:
        # if c.35 int>= cols goto 26
        bge   $s0, $s1, L12_26
        # t8 = r.34 int* 5
        li    $t1, 5
        mul   $s2, $s7, $t1
        # t9 = t8 int+ c.35
        addu  $s4, $s2, $s0
        # t10 = t9 int<< 2
        sll   $s5, $s4, 2
        # t11 = grid[t10]
        addiu $t8, $fp, -80
        addu  $t8, $t8, $s5
        lw    $s6, 0($t8)
        # s = s int+ t11
        addu  $s3, $s3, $s6
        # c.35 = c.35 int+ 1
        addiu $s0, $s0, 1
        # goto 18
        j     L12_18
L12_26:
        # r.34 = r.34 int+ 1
        addiu $s7, $s7, 1
        # goto 16
        j     L12_16
L12_28:
        # return s
        move  $v0, $s3
        j     _Z6nestedii_exit
_Z6nestedii_exit:
        lw    $s0, -160($fp)
        lw    $s1, -164($fp)
        lw    $s2, -156($fp)
        lw    $s3, -168($fp)
        lw    $s4, -140($fp)
        lw    $s5, -144($fp)
        lw    $s6, -148($fp)
        lw    $s7, -152($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# shared(int, int, int)
_Z6sharediii:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        sw    $s0, -52($fp)
        sw    $s1, -56($fp)
        sw    $s2, -44($fp)
        sw    $s3, -60($fp)
        sw    $s4, -48($fp)
        sw    $s5, -64($fp)
        lw    $s0, 8($fp)
        lw    $s1, 12($fp)
        lw    $s3, 16($fp)
        # t1 = x int* y
        mul   $s2, $s0, $s1
        # a = t1 int+ 2
        addiu $s5, $s2, 2
        # if flag int== 0 goto 6
        beq   $s3, $zero, L13_6
        # t3 = x int* y
        mul   $s2, $s0, $s1
        # b = t3 int+ 2
        addiu $s3, $s2, 2
        # goto 10
        j     L13_10
L13_6:
        # t5 = x int+ 1
        addiu $s2, $s0, 1
        # x = t5
        move  $s0, $s2
        # t6 = t5 int* y
        mul   $s4, $s2, $s1
        # b = t6 int+ 2
        addiu $s3, $s4, 2
L13_10:
        # t8 = a int* 1000
        li    $t1, 1000
        mul   $s2, $s5, $t1
        # t9 = t8 int+ b
        addu  $s4, $s2, $s3
        # t10 = x int* y
        mul   $s2, $s0, $s1
        # t11 = t9 int+ t10
        addu  $s0, $s4, $s2
        # return t11
        move  $v0, $s0
        j     _Z6sharediii_exit
_Z6sharediii_exit:
        lw    $s0, -52($fp)
        lw    $s1, -56($fp)
        lw    $s2, -44($fp)
        lw    $s3, -60($fp)
        lw    $s4, -48($fp)
        lw    $s5, -64($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# memory(int)
_Z6memoryi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -96
        sw    $s0, -88($fp)
        sw    $s1, -80($fp)
        sw    $s2, -84($fp)
        sw    $s3, -92($fp)
        sw    $s4, -96($fp)
        lw    $s3, 8($fp)
        # arr[0] = 1
        li    $t0, 1
        sw    $t0, -16($fp)
        # arr[4] = 2
        li    $t0, 2
        sw    $t0, -12($fp)
        # arr[8] = 3
        li    $t0, 3
        sw    $t0, -8($fp)
        # arr[12] = 4
        li    $t0, 4
        sw    $t0, -4($fp)
        # t1 = &arr
        addiu $s1, $fp, -16
        # t2 = t1 ptr+ 4
        addiu $s2, $s1, 4
        # p = t2
        move  $s0, $s2
        # q = t1
        move  $s0, $s1
        # t4 = i int<< 2
        sll   $s0, $s3, 2
        # arr[t4] = 10
        addiu $t8, $fp, -16
        addu  $t8, $t8, $s0
        li    $t0, 10
        sw    $t0, 0($t8)
        # a = 10
        li    $s3, 10
        # *t2 = 20
        li    $t0, 20
        sw    $t0, 0($s2)
        # t8 = arr[t4]
        addiu $t8, $fp, -16
        addu  $t8, $t8, $s0
        lw    $s3, 0($t8)
        # b = t8
        move  $s4, $s3
        # t10 = t1 ptr+ t4
        addu  $s4, $s1, $s0
        # *t10 = 30
        li    $t0, 30
        sw    $t0, 0($s4)
        # t12 = arr[t4]
        addiu $t8, $fp, -16
        addu  $t8, $t8, $s0
        lw    $s1, 0($t8)
        # t13 = *t2
        lw    $s4, 0($s2)
        # t14 = t12 int+ t13
        addu  $s0, $s1, $s4
        # c = t14
        move  $s1, $s0
        # t15 = 10 int+ t8
        li    $t0, 10
        addu  $s1, $t0, $s3
        # t16 = t15 int+ t14
        addu  $s2, $s1, $s0
        # return t16
        move  $v0, $s2
        j     _Z6memoryi_exit
_Z6memoryi_exit:
        lw    $s0, -88($fp)
        lw    $s1, -80($fp)
        lw    $s2, -84($fp)
        lw    $s3, -92($fp)
        lw    $s4, -96($fp)
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
        addiu $sp, $sp, -168
        sw    $s0, -148($fp)
        sw    $s1, -152($fp)
        sw    $s2, -156($fp)
        sw    $s3, -160($fp)
        sw    $s4, -164($fp)
        sw    $s5, -168($fp)
        # x = 5
        li    $t0, 5
        sw    $t0, -4($fp)
        # t1 = &x
        addiu $s0, $fp, -4
        # param 3
        # t2 = call square(int), 1
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        jal   _Z6squarei
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param t1
        # param t2
        # call bump(int &, int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        sw    $s1, 4($sp)
        jal   _Z4bumpRii
        addiu $sp, $sp, 8
        # p[0] = 1
        li    $t0, 1
        sw    $t0, -12($fp)
        # p[4] = 2
        li    $t0, 2
        sw    $t0, -8($fp)
        # param p
        # t3 = call total(struct Pair), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -12
        li    $a2, 8
        jal   __memcpy
        jal   _Z5total4Pair
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param p
        # t4 = call total(struct Pair), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -12
        li    $a2, 8
        jal   __memcpy
        jal   _Z5total4Pair
        addiu $sp, $sp, 8
        move  $s2, $v0
        # t5 = t3 int+ t4
        addu  $s0, $s1, $s2
        # t = t5
        move  $s1, $s0
        # t6 = p[0]
        lw    $s1, -12($fp)
        # param -5
        # param 0
        # param 9
        # t8 = call clamp(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, -5
        sw    $t0, 0($sp)
        sw    $zero, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z5clampiii
        addiu $sp, $sp, 16
        move  $s2, $v0
        # param 50
        # param 0
        # param 9
        # t9 = call clamp(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 50
        sw    $t0, 0($sp)
        sw    $zero, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z5clampiii
        addiu $sp, $sp, 16
        move  $s3, $v0
        # param 4
        # param 0
        # param 9
        # t10 = call clamp(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 4
        sw    $t0, 0($sp)
        sw    $zero, 4($sp)
        li    $t0, 9
        sw    $t0, 8($sp)
        jal   _Z5clampiii
        addiu $sp, $sp, 16
        move  $s4, $v0
        # t11 = t9 int+ t10
        addu  $s5, $s3, $s4
        # param "%d %d %d %d %d\n"
        # param x
        # param t5
        # param t6
        # param t8
        # param t11
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        sw    $s0, 8($sp)
        sw    $s1, 12($sp)
        sw    $s2, 16($sp)
        sw    $s5, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param 1
        # t12 = call counted(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z7countedi
        addiu $sp, $sp, 8
        move  $s0, $v0
        # c1 = t12
        move  $s1, $s0
        # param 1
        # t13 = call counted(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z7countedi
        addiu $sp, $sp, 8
        move  $s1, $v0
        # c2 = t13
        move  $s2, $s1
        # param 1
        # t14 = call counted(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z7countedi
        addiu $sp, $sp, 8
        move  $s2, $v0
        # c3 = t14
        move  $s3, $s2
        # param 6
        # t15 = call fact(int), 1
        addiu $sp, $sp, -8
        li    $t0, 6
        sw    $t0, 0($sp)
        jal   _Z4facti
        addiu $sp, $sp, 8
        move  $s3, $v0
        # param "%d %d %d %d %d\n"
        # param t12
        # param t13
        # param t14
        # param calls
        # param t15
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
        lw    $t0, g_calls
        sw    $t0, 16($sp)
        sw    $s3, 20($sp)
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
        move  $s0, $v0
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
        move  $s1, $v0
        # param 100
        # param 0
        # t18 = call sumTo(int, int), 2
        addiu $sp, $sp, -8
        li    $t0, 100
        sw    $t0, 0($sp)
        sw    $zero, 4($sp)
        jal   _Z5sumToii
        addiu $sp, $sp, 8
        move  $s2, $v0
        # param 9
        # t19 = call countDown(int), 1
        addiu $sp, $sp, -8
        li    $t0, 9
        sw    $t0, 0($sp)
        jal   _Z9countDowni
        addiu $sp, $sp, 8
        move  $s3, $v0
        # param "%d %d %d %d\n"
        # param t16
        # param t17
        # param t18
        # param t19
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
        sw    $s3, 16($sp)
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
        move  $s0, $v0
        # param 0
        # param 9
        # t21 = call invariant(int, int), 2
        addiu $sp, $sp, -8
        sw    $zero, 0($sp)
        li    $t0, 9
        sw    $t0, 4($sp)
        jal   _Z9invariantii
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param 5
        # t22 = call notInvariant(int), 1
        addiu $sp, $sp, -8
        li    $t0, 5
        sw    $t0, 0($sp)
        jal   _Z12notInvarianti
        addiu $sp, $sp, 8
        move  $s2, $v0
        # param 0
        # param 0
        # t23 = call zeroTrips(int, int), 2
        addiu $sp, $sp, -8
        sw    $zero, 0($sp)
        sw    $zero, 4($sp)
        jal   _Z9zeroTripsii
        addiu $sp, $sp, 8
        move  $s3, $v0
        # param "%d %d %d %d\n"
        # param t20
        # param t21
        # param t22
        # param t23
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
        sw    $s3, 16($sp)
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
        move  $s0, $v0
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
        move  $s1, $v0
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
        move  $s2, $v0
        # param "%d %d %d\n"
        # param t24
        # param t25
        # param t26
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
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
        move  $s0, $v0
        # param 3
        # param 4
        # param 0
        # t28 = call shared(int, int, int), 3
        addiu $sp, $sp, -16
        li    $t0, 3
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        sw    $zero, 8($sp)
        jal   _Z6sharediii
        addiu $sp, $sp, 16
        move  $s1, $v0
        # param "%d %d\n"
        # param t27
        # param t28
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 1
        # t29 = call memory(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z6memoryi
        addiu $sp, $sp, 8
        move  $s0, $v0
        # param 2
        # t30 = call memory(int), 1
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        jal   _Z6memoryi
        addiu $sp, $sp, 8
        move  $s1, $v0
        # param "%d %d\n"
        # param t29
        # param t30
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # return calls
        lw    $v0, g_calls
        j     main__exit
main__exit:
        lw    $s0, -148($fp)
        lw    $s1, -152($fp)
        lw    $s2, -156($fp)
        lw    $s3, -160($fp)
        lw    $s4, -164($fp)
        lw    $s5, -168($fp)
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
