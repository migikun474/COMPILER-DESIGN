# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t20_bits.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 37, 100, 32, 37, 120, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str1:
        .byte 37, 120, 32, 37, 120, 32, 37, 120, 32, 37, 120, 10, 0
str2:
        .byte 37, 120, 32, 37, 120, 32, 37, 120, 10, 0
str3:
        .byte 37, 100, 32, 37, 100, 32, 37, 117, 32, 37, 117, 10, 0
str4:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str5:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str6:
        .byte 37, 100, 32, 37, 100, 10, 0
str7:
        .byte 37, 99, 32, 37, 99, 32, 37, 100, 10, 0

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

# popcount(unsigned int)
_Z8popcountj:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # n = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L0_1:
        # if v uint!= 0 goto 3
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L0_3
        # goto 9
        j     L0_9
L0_3:
        # t1 = v uint& 1
        lw    $t0, 8($fp)
        li    $t1, 1
        and   $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t2 = n uint+ t1
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # n = t2
        lw    $t0, -12($fp)
        sw    $t0, -4($fp)
        # t3 = v uint>> 1
        lw    $t0, 8($fp)
        li    $t1, 1
        srlv  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # v = t3
        lw    $t0, -16($fp)
        sw    $t0, 8($fp)
        # goto 1
        j     L0_1
L0_9:
        # return n
        lw    $v0, -4($fp)
        j     _Z8popcountj_exit
_Z8popcountj_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# reverseBits(unsigned int)
_Z11reverseBitsj:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # r = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -8($fp)
L1_2:
        # if i int< 32 goto 4
        lw    $t0, -8($fp)
        li    $t1, 32
        blt   $t0, $t1, L1_4
        # goto 13
        j     L1_13
L1_4:
        # t1 = r uint<< 1
        lw    $t0, -4($fp)
        li    $t1, 1
        sllv  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = v uint& 1
        lw    $t0, 8($fp)
        li    $t1, 1
        and   $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t3 = t1 uint| t2
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        or    $t0, $t0, $t1
        sw    $t0, -20($fp)
        # r = t3
        lw    $t0, -20($fp)
        sw    $t0, -4($fp)
        # t4 = v uint>> 1
        lw    $t0, 8($fp)
        li    $t1, 1
        srlv  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # v = t4
        lw    $t0, -24($fp)
        sw    $t0, 8($fp)
        # t5 = i int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -28($fp)
        # i = t5
        lw    $t0, -28($fp)
        sw    $t0, -8($fp)
        # goto 2
        j     L1_2
L1_13:
        # return r
        lw    $v0, -4($fp)
        j     _Z11reverseBitsj_exit
_Z11reverseBitsj_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# isPowerOfTwo(unsigned int)
_Z12isPowerOfTwoj:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if v uint!= 0 goto 2
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_2
        # goto 6
        j     L2_6
L2_2:
        # t2 = v uint- 1
        lw    $t0, 8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = v uint& t2
        lw    $t0, 8($fp)
        lw    $t1, -8($fp)
        and   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # if t3 uint== 0 goto 8
        lw    $t0, -12($fp)
        li    $t1, 0
        beq   $t0, $t1, L2_8
        # goto 6
        j     L2_6
L2_6:
        # t1 = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # goto 9
        j     L2_9
L2_8:
        # t1 = 1
        li    $t0, 1
        sw    $t0, -4($fp)
L2_9:
        # return t1
        lw    $v0, -4($fp)
        j     _Z12isPowerOfTwoj_exit
_Z12isPowerOfTwoj_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# highestBit(unsigned int)
_Z10highestBitj:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -8($fp)
        # n = t1
        lw    $t0, -8($fp)
        sw    $t0, -4($fp)
L3_2:
        # if v uint!= 0 goto 4
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L3_4
        # goto 9
        j     L3_9
L3_4:
        # t2 = v uint>> 1
        lw    $t0, 8($fp)
        li    $t1, 1
        srlv  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # v = t2
        lw    $t0, -12($fp)
        sw    $t0, 8($fp)
        # t3 = n int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # n = t3
        lw    $t0, -16($fp)
        sw    $t0, -4($fp)
        # goto 2
        j     L3_2
L3_9:
        # return n
        lw    $v0, -4($fp)
        j     _Z10highestBitj_exit
_Z10highestBitj_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# rotl(unsigned int, int)
_Z4rotlji:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = v uint<< k
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        sllv  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = 32 int- k
        li    $t0, 32
        lw    $t1, 12($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = v uint>> t2
        lw    $t0, 8($fp)
        lw    $t1, -8($fp)
        srlv  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = t1 uint| t3
        lw    $t0, -4($fp)
        lw    $t1, -12($fp)
        or    $t0, $t0, $t1
        sw    $t0, -16($fp)
        # return t4
        lw    $v0, -16($fp)
        j     _Z4rotlji_exit
_Z4rotlji_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# sign(int)
_Z4signi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # if v int> 0 goto 3
        lw    $t0, 8($fp)
        li    $t1, 0
        bgt   $t0, $t1, L5_3
        # t1 = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # goto 4
        j     L5_4
L5_3:
        # t1 = 1
        li    $t0, 1
        sw    $t0, -4($fp)
L5_4:
        # if v int< 0 goto 7
        lw    $t0, 8($fp)
        li    $t1, 0
        blt   $t0, $t1, L5_7
        # t2 = 0
        li    $t0, 0
        sw    $t0, -8($fp)
        # goto 8
        j     L5_8
L5_7:
        # t2 = 1
        li    $t0, 1
        sw    $t0, -8($fp)
L5_8:
        # t3 = t1 int- t2
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        subu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # return t3
        lw    $v0, -12($fp)
        j     _Z4signi_exit
_Z4signi_exit:
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
        addiu $sp, $sp, -328
        # u = 4042265140
        li    $t0, -252702156
        sw    $t0, -4($fp)
        # param u
        # t1 = call popcount(unsigned int), 1
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        jal   _Z8popcountj
        addiu $sp, $sp, 8
        sw    $v0, -36($fp)
        # param u
        # t2 = call reverseBits(unsigned int), 1
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        jal   _Z11reverseBitsj
        addiu $sp, $sp, 8
        sw    $v0, -40($fp)
        # param 64
        # t3 = call isPowerOfTwo(unsigned int), 1
        addiu $sp, $sp, -8
        li    $t0, 64
        sw    $t0, 0($sp)
        jal   _Z12isPowerOfTwoj
        addiu $sp, $sp, 8
        sw    $v0, -44($fp)
        # param 65
        # t4 = call isPowerOfTwo(unsigned int), 1
        addiu $sp, $sp, -8
        li    $t0, 65
        sw    $t0, 0($sp)
        jal   _Z12isPowerOfTwoj
        addiu $sp, $sp, 8
        sw    $v0, -48($fp)
        # param 1000
        # t5 = call highestBit(unsigned int), 1
        addiu $sp, $sp, -8
        li    $t0, 1000
        sw    $t0, 0($sp)
        jal   _Z10highestBitj
        addiu $sp, $sp, 8
        sw    $v0, -52($fp)
        # param "%d %x %d %d %d\n"
        # param t1
        # param t2
        # param t3
        # param t4
        # param t5
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -36($fp)
        sw    $t0, 4($sp)
        lw    $t0, -40($fp)
        sw    $t0, 8($sp)
        lw    $t0, -44($fp)
        sw    $t0, 12($sp)
        lw    $t0, -48($fp)
        sw    $t0, 16($sp)
        lw    $t0, -52($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t6 = u uint& 65535
        lw    $t0, -4($fp)
        li    $t1, 65535
        and   $t0, $t0, $t1
        sw    $t0, -56($fp)
        # t7 = u uint| 15
        lw    $t0, -4($fp)
        li    $t1, 15
        or    $t0, $t0, $t1
        sw    $t0, -60($fp)
        # t8 = u uint^ 4294967295
        lw    $t0, -4($fp)
        li    $t1, -1
        xor   $t0, $t0, $t1
        sw    $t0, -64($fp)
        # t9 = uint~ u
        lw    $t0, -4($fp)
        nor   $t0, $t0, $zero
        sw    $t0, -68($fp)
        # param "%x %x %x %x\n"
        # param t6
        # param t7
        # param t8
        # param t9
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -56($fp)
        sw    $t0, 4($sp)
        lw    $t0, -60($fp)
        sw    $t0, 8($sp)
        lw    $t0, -64($fp)
        sw    $t0, 12($sp)
        lw    $t0, -68($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param u
        # param 8
        # t10 = call rotl(unsigned int, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        li    $t0, 8
        sw    $t0, 4($sp)
        jal   _Z4rotlji
        addiu $sp, $sp, 8
        sw    $v0, -72($fp)
        # t11 = u uint<< 4
        lw    $t0, -4($fp)
        li    $t1, 4
        sllv  $t0, $t0, $t1
        sw    $t0, -76($fp)
        # t12 = u uint>> 28
        lw    $t0, -4($fp)
        li    $t1, 28
        srlv  $t0, $t0, $t1
        sw    $t0, -80($fp)
        # param "%x %x %x\n"
        # param t10
        # param t11
        # param t12
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -72($fp)
        sw    $t0, 4($sp)
        lw    $t0, -76($fp)
        sw    $t0, 8($sp)
        lw    $t0, -80($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # big = 2147483647
        li    $t0, 2147483647
        sw    $t0, -8($fp)
        # t13 = int- 2147483647
        li    $t0, 2147483647
        negu  $t0, $t0
        sw    $t0, -84($fp)
        # t14 = t13 int- 1
        lw    $t0, -84($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -88($fp)
        # small = t14
        lw    $t0, -88($fp)
        sw    $t0, -12($fp)
        # wrap = 4294967295
        li    $t0, -1
        sw    $t0, -16($fp)
        # t15 = wrap uint+ 2
        lw    $t0, -16($fp)
        li    $t1, 2
        addu  $t0, $t0, $t1
        sw    $t0, -92($fp)
        # wrap = t15
        lw    $t0, -92($fp)
        sw    $t0, -16($fp)
        # param "%d %d %u %u\n"
        # param big
        # param small
        # param wrap
        # param small
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -8($fp)
        sw    $t0, 4($sp)
        lw    $t0, -12($fp)
        sw    $t0, 8($sp)
        lw    $t0, -16($fp)
        sw    $t0, 12($sp)
        lw    $t0, -12($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t16 = small int>> 31
        lw    $t0, -12($fp)
        li    $t1, 31
        srav  $t0, $t0, $t1
        sw    $t0, -96($fp)
        # t17 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -100($fp)
        # t18 = t17 int>> 1
        lw    $t0, -100($fp)
        li    $t1, 1
        srav  $t0, $t0, $t1
        sw    $t0, -104($fp)
        # t19 = 2147483648 uint>> 31
        li    $t0, -2147483648
        li    $t1, 31
        srlv  $t0, $t0, $t1
        sw    $t0, -108($fp)
        # t20 = 1 int<< 30
        li    $t0, 1
        li    $t1, 30
        sllv  $t0, $t0, $t1
        sw    $t0, -112($fp)
        # param "%d %d %d %d\n"
        # param t16
        # param t18
        # param t19
        # param t20
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -96($fp)
        sw    $t0, 4($sp)
        lw    $t0, -104($fp)
        sw    $t0, 8($sp)
        lw    $t0, -108($fp)
        sw    $t0, 12($sp)
        lw    $t0, -112($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # uc = 255
        li    $t0, 255
        sb    $t0, -17($fp)
        # sc = 127
        li    $t0, 127
        sb    $t0, -18($fp)
        # t21 = int- 32768
        li    $t0, 32768
        negu  $t0, $t0
        sw    $t0, -116($fp)
        # t22 = inttoshort t21
        lw    $t0, -116($fp)
        sh    $t0, -118($fp)
        # sh = t22
        lh    $t0, -118($fp)
        sh    $t0, -20($fp)
        # us = 65535
        li    $t0, 65535
        sh    $t0, -22($fp)
        # t23 = uchartoint uc
        lbu   $t0, -17($fp)
        sw    $t0, -124($fp)
        # t24 = t23 int+ 1
        lw    $t0, -124($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -128($fp)
        # t25 = inttouchar t24
        lw    $t0, -128($fp)
        sb    $t0, -129($fp)
        # uc = t25
        lbu   $t0, -129($fp)
        sb    $t0, -17($fp)
        # t26 = chartoint sc
        lb    $t0, -18($fp)
        sw    $t0, -136($fp)
        # t27 = t26 int+ 1
        lw    $t0, -136($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -140($fp)
        # t28 = inttochar t27
        lw    $t0, -140($fp)
        sb    $t0, -141($fp)
        # sc = t28
        lb    $t0, -141($fp)
        sb    $t0, -18($fp)
        # t29 = shorttoint sh
        lh    $t0, -20($fp)
        sw    $t0, -148($fp)
        # t30 = t29 int- 1
        lw    $t0, -148($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -152($fp)
        # t31 = inttoshort t30
        lw    $t0, -152($fp)
        sh    $t0, -154($fp)
        # sh = t31
        lh    $t0, -154($fp)
        sh    $t0, -20($fp)
        # t32 = ushorttoint us
        lhu   $t0, -22($fp)
        sw    $t0, -160($fp)
        # t33 = t32 int+ 1
        lw    $t0, -160($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -164($fp)
        # t34 = inttoushort t33
        lw    $t0, -164($fp)
        sh    $t0, -166($fp)
        # us = t34
        lhu   $t0, -166($fp)
        sh    $t0, -22($fp)
        # t35 = uchartoint uc
        lbu   $t0, -17($fp)
        sw    $t0, -172($fp)
        # t36 = chartoint sc
        lb    $t0, -18($fp)
        sw    $t0, -176($fp)
        # t37 = shorttoint sh
        lh    $t0, -20($fp)
        sw    $t0, -180($fp)
        # t38 = ushorttoint us
        lhu   $t0, -22($fp)
        sw    $t0, -184($fp)
        # param "%d %d %d %d\n"
        # param t35
        # param t36
        # param t37
        # param t38
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -172($fp)
        sw    $t0, 4($sp)
        lw    $t0, -176($fp)
        sw    $t0, 8($sp)
        lw    $t0, -180($fp)
        sw    $t0, 12($sp)
        lw    $t0, -184($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t39 = int- 7
        li    $t0, 7
        negu  $t0, $t0
        sw    $t0, -188($fp)
        # t40 = t39 int/ 2
        lw    $t0, -188($fp)
        li    $t1, 2
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -192($fp)
        # t41 = int- 7
        li    $t0, 7
        negu  $t0, $t0
        sw    $t0, -196($fp)
        # t42 = t41 int% 2
        lw    $t0, -196($fp)
        li    $t1, 2
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -200($fp)
        # t43 = int- 2
        li    $t0, 2
        negu  $t0, $t0
        sw    $t0, -204($fp)
        # t44 = 7 int/ t43
        li    $t0, 7
        lw    $t1, -204($fp)
        div   $t0, $t1
        mflo  $t0
        sw    $t0, -208($fp)
        # param "%d %d %d\n"
        # param t40
        # param t42
        # param t44
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        lw    $t0, -192($fp)
        sw    $t0, 4($sp)
        lw    $t0, -200($fp)
        sw    $t0, 8($sp)
        lw    $t0, -208($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t46 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -216($fp)
        # if t46 uint< 1 goto 109
        lw    $t0, -216($fp)
        li    $t1, 1
        bltu  $t0, $t1, L6_109
        # t45 = 0
        li    $t0, 0
        sw    $t0, -212($fp)
        # goto 110
        j     L6_110
L6_109:
        # t45 = 1
        li    $t0, 1
        sw    $t0, -212($fp)
L6_110:
        # t48 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -224($fp)
        # if t48 int< 1 goto 114
        lw    $t0, -224($fp)
        li    $t1, 1
        blt   $t0, $t1, L6_114
        # t47 = 0
        li    $t0, 0
        sw    $t0, -220($fp)
        # goto 115
        j     L6_115
L6_114:
        # t47 = 1
        li    $t0, 1
        sw    $t0, -220($fp)
L6_115:
        # t50 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -232($fp)
        # if t50 uint> 100 goto 119
        lw    $t0, -232($fp)
        li    $t1, 100
        bgtu  $t0, $t1, L6_119
        # t49 = 0
        li    $t0, 0
        sw    $t0, -228($fp)
        # goto 120
        j     L6_120
L6_119:
        # t49 = 1
        li    $t0, 1
        sw    $t0, -228($fp)
L6_120:
        # param "%d %d %d\n"
        # param t45
        # param t47
        # param t49
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str5
        sw    $t0, 0($sp)
        lw    $t0, -212($fp)
        sw    $t0, 4($sp)
        lw    $t0, -220($fp)
        sw    $t0, 8($sp)
        lw    $t0, -228($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t51 = int- 9
        li    $t0, 9
        negu  $t0, $t0
        sw    $t0, -236($fp)
        # param t51
        # t52 = call sign(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -236($fp)
        sw    $t0, 0($sp)
        jal   _Z4signi
        addiu $sp, $sp, 8
        sw    $v0, -240($fp)
        # param 0
        # t53 = call sign(int), 1
        addiu $sp, $sp, -8
        li    $t0, 0
        sw    $t0, 0($sp)
        jal   _Z4signi
        addiu $sp, $sp, 8
        sw    $v0, -244($fp)
        # param 4
        # t54 = call sign(int), 1
        addiu $sp, $sp, -8
        li    $t0, 4
        sw    $t0, 0($sp)
        jal   _Z4signi
        addiu $sp, $sp, 8
        sw    $v0, -248($fp)
        # goto 135
        j     L6_135
        # t55 = 0
        li    $t0, 0
        sw    $t0, -252($fp)
        # goto 136
        j     L6_136
L6_135:
        # t55 = 1
        li    $t0, 1
        sw    $t0, -252($fp)
L6_136:
        # param "%d %d %d %d\n"
        # param t52
        # param t53
        # param t54
        # param t55
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -240($fp)
        sw    $t0, 4($sp)
        lw    $t0, -244($fp)
        sw    $t0, 8($sp)
        lw    $t0, -248($fp)
        sw    $t0, 12($sp)
        lw    $t0, -252($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # flags = 0
        li    $t0, 0
        sw    $t0, -28($fp)
        # t56 = 1 int<< 3
        li    $t0, 1
        li    $t1, 3
        sllv  $t0, $t0, $t1
        sw    $t0, -256($fp)
        # t57 = flags int| t56
        lw    $t0, -28($fp)
        lw    $t1, -256($fp)
        or    $t0, $t0, $t1
        sw    $t0, -260($fp)
        # flags = t57
        lw    $t0, -260($fp)
        sw    $t0, -28($fp)
        # t58 = 1 int<< 0
        li    $t0, 1
        li    $t1, 0
        sllv  $t0, $t0, $t1
        sw    $t0, -264($fp)
        # t59 = flags int| t58
        lw    $t0, -28($fp)
        lw    $t1, -264($fp)
        or    $t0, $t0, $t1
        sw    $t0, -268($fp)
        # flags = t59
        lw    $t0, -268($fp)
        sw    $t0, -28($fp)
        # t60 = 1 int<< 0
        li    $t0, 1
        li    $t1, 0
        sllv  $t0, $t0, $t1
        sw    $t0, -272($fp)
        # t61 = int~ t60
        lw    $t0, -272($fp)
        nor   $t0, $t0, $zero
        sw    $t0, -276($fp)
        # t62 = flags int& t61
        lw    $t0, -28($fp)
        lw    $t1, -276($fp)
        and   $t0, $t0, $t1
        sw    $t0, -280($fp)
        # flags = t62
        lw    $t0, -280($fp)
        sw    $t0, -28($fp)
        # t63 = flags int^ 24
        lw    $t0, -28($fp)
        li    $t1, 24
        xor   $t0, $t0, $t1
        sw    $t0, -284($fp)
        # flags = t63
        lw    $t0, -284($fp)
        sw    $t0, -28($fp)
        # t64 = flags int>> 4
        lw    $t0, -28($fp)
        li    $t1, 4
        srav  $t0, $t0, $t1
        sw    $t0, -288($fp)
        # t65 = t64 int& 1
        lw    $t0, -288($fp)
        li    $t1, 1
        and   $t0, $t0, $t1
        sw    $t0, -292($fp)
        # param "%d %d\n"
        # param flags
        # param t65
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        lw    $t0, -292($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # c = 65
        li    $t0, 65
        sb    $t0, -29($fp)
        # t66 = chartoint c
        lb    $t0, -29($fp)
        sw    $t0, -296($fp)
        # t67 = t66 int| 32
        lw    $t0, -296($fp)
        li    $t1, 32
        or    $t0, $t0, $t1
        sw    $t0, -300($fp)
        # t68 = inttochar t67
        lw    $t0, -300($fp)
        sb    $t0, -301($fp)
        # c = t68
        lb    $t0, -301($fp)
        sb    $t0, -29($fp)
        # t69 = chartoint c
        lb    $t0, -29($fp)
        sw    $t0, -308($fp)
        # t70 = chartoint c
        lb    $t0, -29($fp)
        sw    $t0, -312($fp)
        # t71 = t70 int^ 32
        lw    $t0, -312($fp)
        li    $t1, 32
        xor   $t0, $t0, $t1
        sw    $t0, -316($fp)
        # t72 = 122 int- 97
        li    $t0, 122
        li    $t1, 97
        subu  $t0, $t0, $t1
        sw    $t0, -320($fp)
        # param "%c %c %d\n"
        # param t69
        # param t71
        # param t72
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str7
        sw    $t0, 0($sp)
        lw    $t0, -308($fp)
        sw    $t0, 4($sp)
        lw    $t0, -316($fp)
        sw    $t0, 8($sp)
        lw    $t0, -320($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # param 255
        # t73 = call popcount(unsigned int), 1
        addiu $sp, $sp, -8
        li    $t0, 255
        sw    $t0, 0($sp)
        jal   _Z8popcountj
        addiu $sp, $sp, 8
        sw    $v0, -324($fp)
        # return t73
        lw    $v0, -324($fp)
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
