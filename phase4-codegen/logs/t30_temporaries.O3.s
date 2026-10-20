# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t30_temporaries.c
#  Optimization : -O3 (TAC optimizations, registers, peephole)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
str0:
        .byte 43, 37, 100, 32, 0
str1:
        .byte 45, 37, 100, 32, 0
str2:
        .byte 43, 99, 37, 100, 32, 0
str3:
        .byte 99, 111, 112, 121, 37, 100, 32, 0
str4:
        .byte 45, 99, 37, 100, 32, 0
str5:
        .byte 124, 32, 0
str6:
        .byte 37, 100, 32, 124, 32, 0
str7:
        .byte 105, 102, 32, 0
str8:
        .byte 98, 111, 100, 121, 32, 0
str9:
        .byte 37, 100, 10, 0
str10:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37
        .byte 100, 10, 0
str11:
        .byte 37, 108, 108, 100, 32, 37, 108, 108, 100, 10, 0
str12:
        .byte 37, 100, 32, 0
str13:
        .byte 101, 110, 100, 10, 0

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

# Tag::Tag(int)
_ZN3TagC1Ei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        lw    $s1, 8($fp)
        lw    $s0, 12($fp)
        # *this = n
        sw    $s0, 0($s1)
        # param "+%d "
        # param n
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN3TagC1Ei_exit
_ZN3TagC1Ei_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Tag::~Tag()
_ZN3TagD1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -8($fp)
        sw    $s1, -12($fp)
        lw    $s1, 8($fp)
        # t1 = *this
        lw    $s0, 0($s1)
        # param "-%d "
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN3TagD1Ev_exit
_ZN3TagD1Ev_exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Tag::value()
_ZN3Tag5valueEv:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        lw    $s1, 8($fp)
        # t1 = *this
        lw    $s0, 0($s1)
        # t2 = t1 int* 10
        li    $t1, 10
        mul   $s1, $s0, $t1
        # return t2
        move  $v0, $s1
        j     _ZN3Tag5valueEv_exit
_ZN3Tag5valueEv_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Tag::operator+(const class Tag &)
_ZN3TagplERKS_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        sw    $s0, -36($fp)
        sw    $s1, -24($fp)
        sw    $s2, -28($fp)
        sw    $s3, -32($fp)
        lw    $s3, 8($fp)
        lw    $s0, 12($fp)
        # t2 = &t1
        addiu $s1, $fp, -4
        # t3 = *this
        lw    $s2, 0($s3)
        # t4 = *o
        lw    $s3, 0($s0)
        # t5 = t3 int+ t4
        addu  $s0, $s2, $s3
        # *t2 = t5
        sw    $s0, 0($s1)
        # param "+%d "
        # param t5
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _ZN3TagplERKS__exit
_ZN3TagplERKS__exit:
        lw    $s0, -36($fp)
        lw    $s1, -24($fp)
        lw    $s2, -28($fp)
        lw    $s3, -32($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Copy::Copy(int)
_ZN4CopyC1Ei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        lw    $s1, 8($fp)
        lw    $s0, 12($fp)
        # *this = n
        sw    $s0, 0($s1)
        # param "+c%d "
        # param n
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN4CopyC1Ei_exit
_ZN4CopyC1Ei_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Copy::Copy(const class Copy &)
_ZN4CopyC1ERKS_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -16($fp)
        sw    $s1, -12($fp)
        sw    $s2, -20($fp)
        lw    $s2, 8($fp)
        lw    $s0, 12($fp)
        # t1 = *o
        lw    $s1, 0($s0)
        # t2 = t1 int+ 100
        addiu $s0, $s1, 100
        # *this = t2
        sw    $s0, 0($s2)
        # param "copy%d "
        # param t2
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN4CopyC1ERKS__exit
_ZN4CopyC1ERKS__exit:
        lw    $s0, -16($fp)
        lw    $s1, -12($fp)
        lw    $s2, -20($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Copy::~Copy()
_ZN4CopyD1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -8($fp)
        sw    $s1, -12($fp)
        lw    $s1, 8($fp)
        # t1 = *this
        lw    $s0, 0($s1)
        # param "-c%d "
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN4CopyD1Ev_exit
_ZN4CopyD1Ev_exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# make(int)
_Z4makei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        lw    $s1, 8($fp)
        # t2 = &t1
        addiu $s0, $fp, -4
        # *t2 = n
        sw    $s1, 0($s0)
        # param "+%d "
        # param n
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z4makei_exit
_Z4makei_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# named(int)
_Z5namedi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -20($fp)
        sw    $s1, -24($fp)
        lw    $s1, 8($fp)
        # t1 = &t
        addiu $s0, $fp, -4
        # *t1 = n
        sw    $s1, 0($s0)
        # param "+%d "
        # param n
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t2 = t[0]
        lw    $s0, -4($fp)
        # t3 = t2 int+ 1
        addiu $s1, $s0, 1
        # t[0] = t3
        sw    $s1, -4($fp)
        # return t
        addiu $v0, $fp, -4
        j     _Z5namedi_exit
_Z5namedi_exit:
        lw    $s0, -20($fp)
        lw    $s1, -24($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# pick(int)
_Z4picki:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        sw    $s0, -44($fp)
        sw    $s1, -48($fp)
        sw    $s2, -52($fp)
        lw    $s2, 8($fp)
        # t1 = &a
        addiu $s0, $fp, -4
        # *t1 = 40
        li    $t0, 40
        sw    $t0, 0($s0)
        # param "+%d "
        # param 40
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 40
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t2 = &b
        addiu $s1, $fp, -8
        # *t2 = 41
        li    $t0, 41
        sw    $t0, 0($s1)
        # param "+%d "
        # param 41
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 41
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if which int== 0 goto 21
        beq   $s2, $zero, L9_21
        # t3 = a
        addiu $a0, $fp, -20
        addiu $a1, $fp, -4
        li    $a2, 4
        jal   __memcpy
        # t14 = *t2
        lw    $s2, 0($s1)
        # param "-%d "
        # param t14
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t16 = *t1
        lw    $s2, 0($s0)
        # param "-%d "
        # param t16
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t3
        addiu $v0, $fp, -20
        j     _Z4picki_exit
L9_21:
        # t6 = b
        addiu $a0, $fp, -24
        addiu $a1, $fp, -8
        li    $a2, 4
        jal   __memcpy
        # t18 = *t2
        lw    $s2, 0($s1)
        # param "-%d "
        # param t18
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t20 = *t1
        lw    $s1, 0($s0)
        # param "-%d "
        # param t20
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t6
        addiu $v0, $fp, -24
        j     _Z4picki_exit
_Z4picki_exit:
        lw    $s0, -44($fp)
        lw    $s1, -48($fp)
        lw    $s2, -52($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# byValue(class Tag)
_Z7byValue3Tag:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -8($fp)
        # t1 = t[0]
        lw    $s0, 8($fp)
        # return t1
        move  $v0, $s0
        j     _Z7byValue3Tag_exit
_Z7byValue3Tag_exit:
        lw    $s0, -8($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# byRef(const class Tag &)
_Z5byRefRK3Tag:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -8($fp)
        sw    $s1, -12($fp)
        lw    $s1, 8($fp)
        # t1 = *t
        lw    $s0, 0($s1)
        # return t1
        move  $v0, $s0
        j     _Z5byRefRK3Tag_exit
_Z5byRefRK3Tag_exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# copied(class Copy)
_Z6copied4Copy:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -8($fp)
        # t1 = c[0]
        lw    $s0, 8($fp)
        # return t1
        move  $v0, $s0
        j     _Z6copied4Copy_exit
_Z6copied4Copy_exit:
        lw    $s0, -8($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# makeCopy(int)
_Z8makeCopyi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        lw    $s1, 8($fp)
        # t2 = &t1
        addiu $s0, $fp, -4
        # *t2 = n
        sw    $s1, 0($s0)
        # param "+c%d "
        # param n
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z8makeCopyi_exit
_Z8makeCopyi_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# sameCopy(class Copy)
_Z8sameCopy4Copy:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        sw    $s0, -28($fp)
        sw    $s1, -24($fp)
        sw    $s2, -32($fp)
        # t2 = &t1
        addiu $s1, $fp, -4
        # t3 = &c
        addiu $s0, $fp, 8
        # t6 = *t3
        lw    $s2, 0($s0)
        # t7 = t6 int+ 100
        addiu $s0, $s2, 100
        # *t2 = t7
        sw    $s0, 0($s1)
        # param "copy%d "
        # param t7
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z8sameCopy4Copy_exit
_Z8sameCopy4Copy_exit:
        lw    $s0, -28($fp)
        lw    $s1, -24($fp)
        lw    $s2, -32($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Shape::sides()
_ZN5Shape5sidesEv:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 0
        li    $v0, 0
        j     _ZN5Shape5sidesEv_exit
_ZN5Shape5sidesEv_exit:
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Shape::kind()
_ZN5Shape4kindEv:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 1
        li    $v0, 1
        j     _ZN5Shape4kindEv_exit
_ZN5Shape4kindEv_exit:
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Square::sides()
_ZN6Square5sidesEv:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 4
        li    $v0, 4
        j     _ZN6Square5sidesEv_exit
_ZN6Square5sidesEv_exit:
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Square::kind()
_ZN6Square4kindEv:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 2
        li    $v0, 2
        j     _ZN6Square4kindEv_exit
_ZN6Square4kindEv_exit:
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# mix(long long, long long, int)
_Z3mixxxi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -120
        sw    $s0, -92($fp)
        sw    $s1, -96($fp)
        sw    $s2, -112($fp)
        sw    $s3, -100($fp)
        sw    $s4, -116($fp)
        sw    $s5, -104($fp)
        sw    $s6, -120($fp)
        sw    $s7, -108($fp)
        lw    $s3, 8($fp)
        lw    $s4, 12($fp)
        lw    $s5, 16($fp)
        lw    $s6, 20($fp)
        lw    $s7, 24($fp)
        # sum = 0
        li    $s1, 0
        li    $s2, 0
        # i = 0
        li    $s0, 0
L19_2:
        # if i int>= n goto 15
        bge   $s0, $s7, L19_15
        # t1 = inttollong i
        move  $t0, $s0
        sra   $t1, $t0, 31
        sw    $t0, -24($fp)
        sw    $t1, -20($fp)
        # t2 = a llong* t1
        lw    $t2, -24($fp)
        lw    $t3, -20($fp)
        multu $s3, $t2
        mflo  $t4
        mfhi  $t5
        mul   $t6, $s3, $t3
        addu  $t5, $t5, $t6
        mul   $t6, $s4, $t2
        addu  $t6, $t5, $t6
        sw    $t4, -32($fp)
        sw    $t6, -28($fp)
        # t3 = sum llong+ t2
        lw    $t2, -32($fp)
        lw    $t3, -28($fp)
        addu  $t4, $s1, $t2
        sltu  $t5, $t4, $s1
        addu  $t6, $s2, $t3
        addu  $t6, $t6, $t5
        sw    $t4, -40($fp)
        sw    $t6, -36($fp)
        # t4 = b llong^ sum
        xor   $t4, $s5, $s1
        xor   $t6, $s6, $s2
        sw    $t4, -48($fp)
        sw    $t6, -44($fp)
        # t5 = t3 llong- t4
        lw    $t0, -40($fp)
        lw    $t1, -36($fp)
        lw    $t2, -48($fp)
        lw    $t3, -44($fp)
        sltu  $t5, $t0, $t2
        subu  $t4, $t0, $t2
        subu  $t6, $t1, $t3
        subu  $t6, $t6, $t5
        sw    $t4, -56($fp)
        sw    $t6, -52($fp)
        # sum = t5
        lw    $s1, -56($fp)
        lw    $s2, -52($fp)
        # a = a llong+ 4294967296
        li    $t2, 0
        li    $t3, 1
        addu  $t4, $s3, $t2
        sltu  $t5, $t4, $s3
        addu  $t6, $s4, $t3
        addu  $t6, $t6, $t5
        move  $s3, $t4
        move  $s4, $t6
        # t7 = llong- b
        sltu  $t5, $zero, $s5
        negu  $t4, $s5
        negu  $t6, $s6
        subu  $t6, $t6, $t5
        sw    $t4, -64($fp)
        sw    $t6, -60($fp)
        # t8 = t5 llong& 65535
        lw    $t0, -56($fp)
        lw    $t1, -52($fp)
        li    $t2, 65535
        li    $t3, 0
        and   $t4, $t0, $t2
        and   $t6, $t1, $t3
        sw    $t4, -72($fp)
        sw    $t6, -68($fp)
        # b = t7 llong+ t8
        lw    $t0, -64($fp)
        lw    $t1, -60($fp)
        lw    $t2, -72($fp)
        lw    $t3, -68($fp)
        addu  $t4, $t0, $t2
        sltu  $t5, $t4, $t0
        addu  $t6, $t1, $t3
        addu  $t6, $t6, $t5
        move  $s5, $t4
        move  $s6, $t6
        # i = i int+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L19_2
L19_15:
        # t11 = sum llong+ a
        addu  $t4, $s1, $s3
        sltu  $t5, $t4, $s1
        addu  $t6, $s2, $s4
        addu  $t6, $t6, $t5
        move  $s0, $t4
        move  $s7, $t6
        # t12 = t11 llong- b
        sltu  $t5, $s0, $s5
        subu  $t4, $s0, $s5
        subu  $t6, $s7, $s6
        subu  $t6, $t6, $t5
        move  $s1, $t4
        move  $s2, $t6
        # return t12
        move  $v0, $s1
        move  $v1, $s2
        j     _Z3mixxxi_exit
_Z3mixxxi_exit:
        lw    $s0, -92($fp)
        lw    $s1, -96($fp)
        lw    $s2, -112($fp)
        lw    $s3, -100($fp)
        lw    $s4, -116($fp)
        lw    $s5, -104($fp)
        lw    $s6, -120($fp)
        lw    $s7, -108($fp)
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
        addiu $sp, $sp, -704
        sw    $s0, -676($fp)
        sw    $s1, -684($fp)
        sw    $s2, -680($fp)
        sw    $s3, -688($fp)
        sw    $s4, -696($fp)
        sw    $s5, -700($fp)
        sw    $s6, -692($fp)
        sw    $s7, -704($fp)
        # t2 = &t1
        addiu $s0, $fp, -64
        # *t2 = 1
        li    $t0, 1
        sw    $t0, 0($s0)
        # param "+%d "
        # param 1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t158 = *t2
        lw    $s1, 0($s0)
        # param "-%d "
        # param t158
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t161 = &t160
        addiu $s0, $fp, -360
        # param t161
        # param 2
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t4 = t160
        addiu $a0, $fp, -72
        addiu $a1, $fp, -360
        li    $a2, 4
        jal   __memcpy
        # t5 = &t4
        addiu $s0, $fp, -72
        # t163 = *t5
        lw    $s1, 0($s0)
        # param "-%d "
        # param t163
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t8 = &t7
        addiu $s0, $fp, -80
        # *t8 = 3
        li    $t0, 3
        sw    $t0, 0($s0)
        # param "+%d "
        # param 3
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t167 = *t8
        lw    $s1, 0($s0)
        # t168 = t167 int* 10
        li    $t1, 10
        mul   $s3, $s1, $t1
        # t171 = &t170
        addiu $s1, $fp, -380
        # param t171
        # param 4
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s1, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t11 = t170
        addiu $a0, $fp, -88
        addiu $a1, $fp, -380
        li    $a2, 4
        jal   __memcpy
        # t12 = &t11
        addiu $s2, $fp, -88
        # t173 = *t12
        lw    $s1, 0($s2)
        # t174 = t173 int* 10
        li    $t1, 10
        mul   $s4, $s1, $t1
        # t15 = t168 int+ t174
        addu  $s2, $s3, $s4
        # param "-%d "
        # param t173
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t178 = *t8
        lw    $s1, 0($s0)
        # param "-%d "
        # param t178
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t15
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t181 = &t180
        addiu $s0, $fp, -400
        # param t181
        # param 5
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # kept = t180
        addiu $a0, $fp, -8
        addiu $a1, $fp, -400
        li    $a2, 4
        jal   __memcpy
        # t20 = &kept
        addiu $t0, $fp, -8
        sw    $t0, -100($fp)
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t23 = &t22
        addiu $s0, $fp, -104
        # *t23 = 6
        li    $t0, 6
        sw    $t0, 0($s0)
        # param "+%d "
        # param 6
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 6
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t187 = &t186
        addiu $s1, $fp, -408
        # t188 = *t20
        lw    $t8, -100($fp)
        lw    $s2, 0($t8)
        # t189 = *t23
        lw    $s3, 0($s0)
        # t190 = t188 int+ t189
        addu  $s4, $s2, $s3
        # param t187
        # param t190
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s1, 0($sp)
        sw    $s4, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # sum = t186
        addiu $a0, $fp, -12
        addiu $a1, $fp, -408
        li    $a2, 4
        jal   __memcpy
        # t27 = &sum
        addiu $t0, $fp, -12
        sw    $t0, -112($fp)
        # t192 = *t23
        lw    $s1, 0($s0)
        # param "-%d "
        # param t192
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t29 = sum[0]
        lw    $s0, -12($fp)
        # param "%d | "
        # param t29
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t196 = &t195
        addiu $s0, $fp, -432
        # t197 = *t20
        lw    $t8, -100($fp)
        lw    $s1, 0($t8)
        # t198 = *t27
        lw    $t8, -112($fp)
        lw    $s2, 0($t8)
        # t199 = t197 int+ t198
        addu  $s3, $s1, $s2
        # param t196
        # param t199
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        sw    $s3, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t32 = t195
        addiu $a0, $fp, -120
        addiu $a1, $fp, -432
        li    $a2, 4
        jal   __memcpy
        # t33 = &t32
        addiu $s0, $fp, -120
        # t203 = &t202
        addiu $s1, $fp, -452
        # t204 = *t33
        lw    $s2, 0($s0)
        # t205 = *t20
        lw    $t8, -100($fp)
        lw    $s3, 0($t8)
        # t206 = t204 int+ t205
        addu  $s4, $s2, $s3
        # param t203
        # param t206
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s1, 0($sp)
        sw    $s4, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t36 = t202
        addiu $a0, $fp, -128
        addiu $a1, $fp, -452
        li    $a2, 4
        jal   __memcpy
        # t37 = &t36
        addiu $s1, $fp, -128
        # t38 = t36[0]
        lw    $s2, -128($fp)
        # t208 = *t37
        lw    $s3, 0($s1)
        # param "-%d "
        # param t208
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t210 = *t33
        lw    $s1, 0($s0)
        # param "-%d "
        # param t210
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t38
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t42 = &t41
        addiu $s0, $fp, -140
        # *t42 = 10
        li    $t0, 10
        sw    $t0, 0($s0)
        # param "+%d "
        # param 10
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 10
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t213 = t41
        addiu $a0, $fp, -480
        addiu $a1, $fp, -140
        li    $a2, 4
        jal   __memcpy
        # t214 = t213[0]
        lw    $s1, -480($fp)
        # t216 = *t42
        lw    $s2, 0($s0)
        # param "-%d "
        # param t216
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t214
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t45 = kept
        addiu $a0, $fp, -148
        addiu $a1, $fp, -8
        li    $a2, 4
        jal   __memcpy
        # t46 = &t45
        addiu $s0, $fp, -148
        # t217 = t45
        addiu $a0, $fp, -492
        addiu $a1, $fp, -148
        li    $a2, 4
        jal   __memcpy
        # t218 = t217[0]
        lw    $s1, -492($fp)
        # t220 = *t46
        lw    $s2, 0($s0)
        # param "-%d "
        # param t220
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t218
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t50 = &t49
        addiu $s0, $fp, -156
        # *t50 = 11
        li    $t0, 11
        sw    $t0, 0($s0)
        # param "+%d "
        # param 11
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 11
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t224 = *t50
        lw    $t0, 0($s0)
        sw    $t0, -504($fp)
        # param "-%d "
        # param t224
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -504($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t224
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -504($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t55 = &t54
        addiu $s0, $fp, -164
        # *t55 = 12
        li    $t0, 12
        sw    $t0, 0($s0)
        # param "+%d "
        # param 12
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 12
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t230 = *t55
        lw    $s1, 0($s0)
        # param "-%d "
        # param t230
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if t230 int<= 5 goto 158
        li    $t1, 5
        ble   $s1, $t1, L20_158
        # param "if "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str7
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
L20_158:
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i = 0
        li    $s0, 0
        # t61 = &t60
        addiu $s6, $fp, -176
        # t65 = &t64
        addiu $s2, $fp, -188
        # t235 = &t234
        addiu $s7, $fp, -512
L20_164:
        # if i int>= 2 goto 188
        li    $t1, 2
        bge   $s0, $t1, L20_188
        # t59 = 13 int+ i
        li    $t0, 13
        addu  $s3, $t0, $s0
        # param t235
        # param t59
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s7, 0($sp)
        sw    $s3, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t60 = t234
        addiu $a0, $fp, -176
        addiu $a1, $fp, -512
        li    $a2, 4
        jal   __memcpy
        # t62 = t60[0]
        lw    $s4, -176($fp)
        # t237 = *t61
        lw    $s5, 0($s6)
        # param "-%d "
        # param t237
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s5, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if t62 int<= 0 goto 188
        ble   $s4, $zero, L20_188
        # param "body "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # *t65 = 20
        li    $t0, 20
        sw    $t0, 0($s2)
        # param "+%d "
        # param 20
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 20
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t241 = *t65
        lw    $s1, 0($s2)
        # i = i int+ t241
        addu  $s0, $s0, $s1
        # param "-%d "
        # param t241
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # goto 164
        j     L20_164
L20_188:
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if t224 int<= 0 goto 202
        lw    $t0, -504($fp)
        ble   $t0, $zero, L20_202
        # t72 = &t71
        addiu $s1, $fp, -200
        # *t72 = 21
        li    $t0, 21
        sw    $t0, 0($s1)
        # param "+%d "
        # param 21
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 21
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t70 = t71[0]
        lw    $s0, -200($fp)
        # t247 = *t72
        lw    $s2, 0($s1)
        # param "-%d "
        # param t247
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # goto 212
        j     L20_212
L20_202:
        # t76 = &t75
        addiu $s1, $fp, -208
        # *t76 = 22
        li    $t0, 22
        sw    $t0, 0($s1)
        # param "+%d "
        # param 22
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 22
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t70 = t75[0]
        lw    $s0, -208($fp)
        # t251 = *t76
        lw    $s2, 0($s1)
        # param "-%d "
        # param t251
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
L20_212:
        # param "%d | "
        # param t70
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t254 = &t253
        addiu $s0, $fp, -536
        # param t254
        # param 30
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        li    $t0, 30
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t255 = t253[0]
        lw    $s0, -536($fp)
        # t256 = t255 int+ 1
        addiu $s1, $s0, 1
        # t253[0] = t256
        sw    $s1, -536($fp)
        # n = t253
        addiu $a0, $fp, -20
        addiu $a1, $fp, -536
        li    $a2, 4
        jal   __memcpy
        # t81 = &n
        addiu $s4, $fp, -20
        # t82 = n[0]
        lw    $s0, -20($fp)
        # param "%d | "
        # param t82
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param 1
        # t83 = call pick(int), 1
        addiu $sp, $sp, -8
        li    $t0, 1
        sw    $t0, 0($sp)
        jal   _Z4picki
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -224
        li    $a2, 4
        jal   __memcpy
        # t84 = &t83
        addiu $s0, $fp, -224
        # t85 = t83[0]
        lw    $s1, -224($fp)
        # t258 = *t84
        lw    $s2, 0($s0)
        # param "-%d "
        # param t258
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param 0
        # t87 = call pick(int), 1
        addiu $sp, $sp, -8
        sw    $zero, 0($sp)
        jal   _Z4picki
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -236
        li    $a2, 4
        jal   __memcpy
        # t88 = &t87
        addiu $s0, $fp, -236
        # t89 = t87[0]
        lw    $s2, -236($fp)
        # t90 = t85 int+ t89
        addu  $s3, $s1, $s2
        # t260 = *t88
        lw    $s1, 0($s0)
        # param "-%d "
        # param t260
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t90
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t93 = &t92
        addiu $s1, $fp, -252
        # *t93 = 50
        li    $t0, 50
        sw    $t0, 0($s1)
        # param "+%d "
        # param 50
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 50
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t95 = *t93
        lw    $s0, 0($s1)
        # param "%d | "
        # param t95
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t97 = &t96
        addiu $s0, $fp, -264
        # *t97 = 60
        li    $t0, 60
        sw    $t0, 0($s0)
        # param "+%d "
        # param 60
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 60
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # kept = t96
        addiu $a0, $fp, -8
        addiu $a1, $fp, -264
        li    $a2, 4
        jal   __memcpy
        # t266 = *t97
        lw    $s2, 0($s0)
        # param "-%d "
        # param t266
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t99 = kept[0]
        lw    $s0, -8($fp)
        # param "%d\n"
        # param t99
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str9
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t100 = &c
        addiu $s0, $fp, -28
        # *t100 = 1
        li    $t0, 1
        sw    $t0, 0($s0)
        # param "+c%d "
        # param 1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t102 = &t101
        addiu $s2, $fp, -280
        # t271 = *t100
        lw    $s5, 0($s0)
        # t272 = t271 int+ 100
        addiu $s3, $s5, 100
        # *t102 = t272
        sw    $s3, 0($s2)
        # param "copy%d "
        # param t272
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t273 = t101
        addiu $a0, $fp, -572
        addiu $a1, $fp, -280
        li    $a2, 4
        jal   __memcpy
        # t274 = t273[0]
        lw    $s3, -572($fp)
        # t276 = *t102
        lw    $s5, 0($s2)
        # param "-c%d "
        # param t276
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s5, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t274
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t107 = &t106
        addiu $s2, $fp, -288
        # *t107 = 2
        li    $t0, 2
        sw    $t0, 0($s2)
        # param "+c%d "
        # param 2
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t279 = t106
        addiu $a0, $fp, -584
        addiu $a1, $fp, -288
        li    $a2, 4
        jal   __memcpy
        # t280 = t279[0]
        lw    $s3, -584($fp)
        # t282 = *t107
        lw    $s5, 0($s2)
        # param "-c%d "
        # param t282
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s5, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d | "
        # param t280
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t285 = &t284
        addiu $s2, $fp, -596
        # param t285
        # param 3
        # call Copy::Copy(int), 2
        addiu $sp, $sp, -8
        sw    $s2, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1Ei
        addiu $sp, $sp, 8
        # d = t284
        addiu $a0, $fp, -32
        addiu $a1, $fp, -596
        li    $a2, 4
        jal   __memcpy
        # t112 = &d
        addiu $s5, $fp, -32
        # t113 = d[0]
        lw    $s2, -32($fp)
        # param "%d | "
        # param t113
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t115 = &t114
        addiu $s2, $fp, -304
        # t288 = *t100
        lw    $s6, 0($s0)
        # t289 = t288 int+ 100
        addiu $s3, $s6, 100
        # *t115 = t289
        sw    $s3, 0($s2)
        # param "copy%d "
        # param t289
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t290 = t114
        addiu $a0, $fp, -612
        addiu $a1, $fp, -304
        li    $a2, 4
        jal   __memcpy
        # t292 = &t291
        addiu $s3, $fp, -616
        # t293 = &t290
        addiu $s6, $fp, -612
        # param t292
        # param t293
        # call Copy::Copy(const class Copy &), 2
        addiu $sp, $sp, -8
        sw    $s3, 0($sp)
        sw    $s6, 4($sp)
        jal   _ZN4CopyC1ERKS_
        addiu $sp, $sp, 8
        # e = t291
        addiu $a0, $fp, -36
        addiu $a1, $fp, -616
        li    $a2, 4
        jal   __memcpy
        # t119 = &e
        addiu $s6, $fp, -36
        # t295 = *t115
        lw    $s3, 0($s2)
        # param "-c%d "
        # param t295
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t121 = e[0]
        lw    $s2, -36($fp)
        # param "%d\n"
        # param t121
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str9
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "%d %d %d %d %d %d\n"
        # param 4
        # param 0
        # param 0
        # param 0
        # param 2
        # param 1
        # call printf, 7
        addiu $sp, $sp, -32
        la    $t0, str10
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        sw    $zero, 8($sp)
        sw    $zero, 12($sp)
        sw    $zero, 16($sp)
        li    $t0, 2
        sw    $t0, 20($sp)
        li    $t0, 1
        sw    $t0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # param 3
        # param 5
        # param 20
        # t133 = call mix(long long, long long, int), 3
        addiu $sp, $sp, -24
        li    $t0, 3
        li    $t1, 0
        sw    $t0, 0($sp)
        sw    $t1, 4($sp)
        li    $t0, 5
        li    $t1, 0
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        li    $t0, 20
        sw    $t0, 16($sp)
        jal   _Z3mixxxi
        addiu $sp, $sp, 24
        move  $s2, $v0
        move  $s3, $v1
        # param -7
        # param 1099511627776
        # param 9
        # t137 = call mix(long long, long long, int), 3
        addiu $sp, $sp, -24
        li    $t0, -7
        li    $t1, -1
        sw    $t0, 0($sp)
        sw    $t1, 4($sp)
        li    $t0, 0
        li    $t1, 256
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        li    $t0, 9
        sw    $t0, 16($sp)
        jal   _Z3mixxxi
        addiu $sp, $sp, 24
        sw    $v0, -336($fp)
        sw    $v1, -332($fp)
        # param "%lld %lld\n"
        # param t133
        # param t137
        # call printf, 3
        addiu $sp, $sp, -24
        la    $t0, str11
        sw    $t0, 0($sp)
        sw    $s2, 8($sp)
        sw    $s3, 12($sp)
        lw    $t0, -336($fp)
        lw    $t1, -332($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t138 = &inner
        addiu $s2, $fp, -60
        # *t138 = 70
        li    $t0, 70
        sw    $t0, 0($s2)
        # param "+%d "
        # param 70
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 70
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t305 = *t138
        lw    $t0, 0($s2)
        sw    $t0, -632($fp)
        # t142 = &t141
        addiu $s3, $fp, -344
        # *t142 = 71
        li    $t0, 71
        sw    $t0, 0($s3)
        # param "+%d "
        # param 71
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        li    $t0, 71
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t309 = *t142
        lw    $t0, 0($s3)
        sw    $t0, -636($fp)
        # t145 = t305 int+ t309
        lw    $t0, -632($fp)
        lw    $t1, -636($fp)
        addu  $s7, $t0, $t1
        # param "%d "
        # param t145
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str12
        sw    $t0, 0($sp)
        sw    $s7, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t311 = *t142
        lw    $s7, 0($s3)
        # param "-%d "
        # param t311
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s7, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t313 = *t138
        lw    $s3, 0($s2)
        # param "-%d "
        # param t313
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s3, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "end\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str13
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t315 = *t119
        lw    $s2, 0($s6)
        # param "-c%d "
        # param t315
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t317 = *t112
        lw    $s2, 0($s5)
        # param "-c%d "
        # param t317
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t319 = *t100
        lw    $s2, 0($s0)
        # param "-c%d "
        # param t319
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s2, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t321 = *t93
        lw    $s0, 0($s1)
        # param "-%d "
        # param t321
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t323 = *t81
        lw    $s0, 0($s4)
        # param "-%d "
        # param t323
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t325 = *t27
        lw    $t8, -112($fp)
        lw    $s0, 0($t8)
        # param "-%d "
        # param t325
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t327 = *t20
        lw    $t8, -100($fp)
        lw    $s0, 0($t8)
        # param "-%d "
        # param t327
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return 0
        li    $v0, 0
        j     main__exit
main__exit:
        lw    $s0, -676($fp)
        lw    $s1, -684($fp)
        lw    $s2, -680($fp)
        lw    $s3, -688($fp)
        lw    $s4, -696($fp)
        lw    $s5, -700($fp)
        lw    $s6, -692($fp)
        lw    $s7, -704($fp)
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
