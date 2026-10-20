# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t30_temporaries.c
#  Optimization : no optimization (every value in the stack frame)
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
        # *this = n
        lw    $t8, 8($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # param "+%d "
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN3TagC1Ei_exit
_ZN3TagC1Ei_exit:
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
        addiu $sp, $sp, -8
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # param "-%d "
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN3TagD1Ev_exit
_ZN3TagD1Ev_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Tag::value()
_ZN3Tag5valueEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = t1 int* 10
        lw    $t0, -4($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _ZN3Tag5valueEv_exit
_ZN3Tag5valueEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Tag::operator+(const class Tag &)
_ZN3TagplERKS_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t2 = &t1
        addiu $t0, $fp, -4
        sw    $t0, -8($fp)
        # t3 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t4 = *o
        lw    $t8, 12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = t3 int+ t4
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # param t2
        # param t5
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        lw    $t0, -20($fp)
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _ZN3TagplERKS__exit
_ZN3TagplERKS__exit:
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
        # *this = n
        lw    $t8, 8($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # param "+c%d "
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN4CopyC1Ei_exit
_ZN4CopyC1Ei_exit:
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
        addiu $sp, $sp, -16
        # t1 = *o
        lw    $t8, 12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = t1 int+ 100
        lw    $t0, -4($fp)
        li    $t1, 100
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # *this = t2
        lw    $t8, 8($fp)
        lw    $t0, -8($fp)
        sw    $t0, 0($t8)
        # t3 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # param "copy%d "
        # param t3
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -12($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN4CopyC1ERKS__exit
_ZN4CopyC1ERKS__exit:
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
        addiu $sp, $sp, -8
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # param "-c%d "
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN4CopyD1Ev_exit
_ZN4CopyD1Ev_exit:
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
        addiu $sp, $sp, -8
        # t2 = &t1
        addiu $t0, $fp, -4
        sw    $t0, -8($fp)
        # param t2
        # param n
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        lw    $t0, 8($fp)
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z4makei_exit
_Z4makei_exit:
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
        addiu $sp, $sp, -16
        # t1 = &t
        addiu $t0, $fp, -4
        sw    $t0, -8($fp)
        # param t1
        # param n
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        lw    $t0, 8($fp)
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t2 = t[0]
        addiu $t8, $fp, -4
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t3 = t2 int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t[0] = t3
        addiu $t8, $fp, -4
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, -16($fp)
        sw    $t0, 0($t8)
        # return t
        addiu $v0, $fp, -4
        j     _Z5namedi_exit
_Z5namedi_exit:
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
        addiu $sp, $sp, -40
        # t1 = &a
        addiu $t0, $fp, -4
        sw    $t0, -12($fp)
        # param t1
        # param 40
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -12($fp)
        sw    $t0, 0($sp)
        li    $t0, 40
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t2 = &b
        addiu $t0, $fp, -8
        sw    $t0, -16($fp)
        # param t2
        # param 41
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        li    $t0, 41
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # if which int!= 0 goto 10
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L9_10
        # goto 18
        j     L9_18
L9_10:
        # t3 = a
        addiu $a0, $fp, -20
        addiu $a1, $fp, -4
        li    $a2, 4
        jal   __memcpy
        # t4 = &b
        addiu $t0, $fp, -8
        sw    $t0, -24($fp)
        # param t4
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -24($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t5 = &a
        addiu $t0, $fp, -4
        sw    $t0, -28($fp)
        # param t5
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -28($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # return t3
        addiu $v0, $fp, -20
        j     _Z4picki_exit
L9_18:
        # t6 = b
        addiu $a0, $fp, -32
        addiu $a1, $fp, -8
        li    $a2, 4
        jal   __memcpy
        # t7 = &b
        addiu $t0, $fp, -8
        sw    $t0, -36($fp)
        # param t7
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -36($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t8 = &a
        addiu $t0, $fp, -4
        sw    $t0, -40($fp)
        # param t8
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -40($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # return t6
        addiu $v0, $fp, -32
        j     _Z4picki_exit
_Z4picki_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# byValue(class Tag)
_Z7byValue3Tag:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = t[0]
        addiu $t8, $fp, 8
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # return t1
        lw    $v0, -4($fp)
        j     _Z7byValue3Tag_exit
_Z7byValue3Tag_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# byRef(const class Tag &)
_Z5byRefRK3Tag:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = *t
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # return t1
        lw    $v0, -4($fp)
        j     _Z5byRefRK3Tag_exit
_Z5byRefRK3Tag_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# copied(class Copy)
_Z6copied4Copy:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = c[0]
        addiu $t8, $fp, 8
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # return t1
        lw    $v0, -4($fp)
        j     _Z6copied4Copy_exit
_Z6copied4Copy_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# makeCopy(int)
_Z8makeCopyi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t2 = &t1
        addiu $t0, $fp, -4
        sw    $t0, -8($fp)
        # param t2
        # param n
        # call Copy::Copy(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        lw    $t0, 8($fp)
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1Ei
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z8makeCopyi_exit
_Z8makeCopyi_exit:
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
        addiu $sp, $sp, -16
        # t2 = &t1
        addiu $t0, $fp, -4
        sw    $t0, -8($fp)
        # t3 = &c
        addiu $t0, $fp, 8
        sw    $t0, -12($fp)
        # param t2
        # param t3
        # call Copy::Copy(const class Copy &), 2
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        lw    $t0, -12($fp)
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1ERKS_
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z8sameCopy4Copy_exit
_Z8sameCopy4Copy_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Shape::sides()
_ZN5Shape5sidesEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 0
        li    $v0, 0
        j     _ZN5Shape5sidesEv_exit
_ZN5Shape5sidesEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Shape::kind()
_ZN5Shape4kindEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 1
        li    $v0, 1
        j     _ZN5Shape4kindEv_exit
_ZN5Shape4kindEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Square::sides()
_ZN6Square5sidesEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 4
        li    $v0, 4
        j     _ZN6Square5sidesEv_exit
_ZN6Square5sidesEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Square::kind()
_ZN6Square4kindEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 2
        li    $v0, 2
        j     _ZN6Square4kindEv_exit
_ZN6Square4kindEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# mix(long long, long long, int)
_Z3mixxxi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -112
        # sum = 0
        li    $t0, 0
        li    $t1, 0
        sw    $t0, -8($fp)
        sw    $t1, -4($fp)
        # i = 0
        li    $t0, 0
        sw    $t0, -12($fp)
L19_2:
        # if i int< n goto 4
        lw    $t0, -12($fp)
        lw    $t1, 24($fp)
        blt   $t0, $t1, L19_4
        # goto 19
        j     L19_19
L19_4:
        # t1 = inttollong i
        lw    $t0, -12($fp)
        sra   $t1, $t0, 31
        sw    $t0, -24($fp)
        sw    $t1, -20($fp)
        # t2 = a llong* t1
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        lw    $t2, -24($fp)
        lw    $t3, -20($fp)
        multu $t0, $t2
        mflo  $t4
        mfhi  $t5
        mul   $t6, $t0, $t3
        addu  $t5, $t5, $t6
        mul   $t6, $t1, $t2
        addu  $t6, $t5, $t6
        sw    $t4, -32($fp)
        sw    $t6, -28($fp)
        # t3 = sum llong+ t2
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        lw    $t2, -32($fp)
        lw    $t3, -28($fp)
        addu  $t4, $t0, $t2
        sltu  $t5, $t4, $t0
        addu  $t6, $t1, $t3
        addu  $t6, $t6, $t5
        sw    $t4, -40($fp)
        sw    $t6, -36($fp)
        # t4 = b llong^ sum
        lw    $t0, 16($fp)
        lw    $t1, 20($fp)
        lw    $t2, -8($fp)
        lw    $t3, -4($fp)
        xor   $t4, $t0, $t2
        xor   $t6, $t1, $t3
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
        lw    $t0, -56($fp)
        lw    $t1, -52($fp)
        sw    $t0, -8($fp)
        sw    $t1, -4($fp)
        # t6 = a llong+ 4294967296
        lw    $t0, 8($fp)
        lw    $t1, 12($fp)
        li    $t2, 0
        li    $t3, 1
        addu  $t4, $t0, $t2
        sltu  $t5, $t4, $t0
        addu  $t6, $t1, $t3
        addu  $t6, $t6, $t5
        sw    $t4, -64($fp)
        sw    $t6, -60($fp)
        # a = t6
        lw    $t0, -64($fp)
        lw    $t1, -60($fp)
        sw    $t0, 8($fp)
        sw    $t1, 12($fp)
        # t7 = llong- b
        lw    $t0, 16($fp)
        lw    $t1, 20($fp)
        sltu  $t5, $zero, $t0
        negu  $t4, $t0
        negu  $t6, $t1
        subu  $t6, $t6, $t5
        sw    $t4, -72($fp)
        sw    $t6, -68($fp)
        # t8 = sum llong& 65535
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        li    $t2, 65535
        li    $t3, 0
        and   $t4, $t0, $t2
        and   $t6, $t1, $t3
        sw    $t4, -80($fp)
        sw    $t6, -76($fp)
        # t9 = t7 llong+ t8
        lw    $t0, -72($fp)
        lw    $t1, -68($fp)
        lw    $t2, -80($fp)
        lw    $t3, -76($fp)
        addu  $t4, $t0, $t2
        sltu  $t5, $t4, $t0
        addu  $t6, $t1, $t3
        addu  $t6, $t6, $t5
        sw    $t4, -88($fp)
        sw    $t6, -84($fp)
        # b = t9
        lw    $t0, -88($fp)
        lw    $t1, -84($fp)
        sw    $t0, 16($fp)
        sw    $t1, 20($fp)
        # t10 = i int+ 1
        lw    $t0, -12($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -92($fp)
        # i = t10
        lw    $t0, -92($fp)
        sw    $t0, -12($fp)
        # goto 2
        j     L19_2
L19_19:
        # t11 = sum llong+ a
        lw    $t0, -8($fp)
        lw    $t1, -4($fp)
        lw    $t2, 8($fp)
        lw    $t3, 12($fp)
        addu  $t4, $t0, $t2
        sltu  $t5, $t4, $t0
        addu  $t6, $t1, $t3
        addu  $t6, $t6, $t5
        sw    $t4, -104($fp)
        sw    $t6, -100($fp)
        # t12 = t11 llong- b
        lw    $t0, -104($fp)
        lw    $t1, -100($fp)
        lw    $t2, 16($fp)
        lw    $t3, 20($fp)
        sltu  $t5, $t0, $t2
        subu  $t4, $t0, $t2
        subu  $t6, $t1, $t3
        subu  $t6, $t6, $t5
        sw    $t4, -112($fp)
        sw    $t6, -108($fp)
        # return t12
        lw    $v0, -112($fp)
        lw    $v1, -108($fp)
        j     _Z3mixxxi_exit
_Z3mixxxi_exit:
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
        addiu $sp, $sp, -704
        # t2 = &t1
        addiu $t0, $fp, -64
        sw    $t0, -68($fp)
        # param t2
        # param 1
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -68($fp)
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t3 = &t1
        addiu $t0, $fp, -64
        sw    $t0, -72($fp)
        # param t3
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -72($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param 2
        # t4 = call make(int), 1
        addiu $sp, $sp, -8
        li    $t0, 2
        sw    $t0, 0($sp)
        jal   _Z4makei
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -76
        li    $a2, 4
        jal   __memcpy
        # t5 = &t4
        addiu $t0, $fp, -76
        sw    $t0, -80($fp)
        # t6 = &t4
        addiu $t0, $fp, -76
        sw    $t0, -84($fp)
        # param t6
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -84($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t8 = &t7
        addiu $t0, $fp, -88
        sw    $t0, -92($fp)
        # param t8
        # param 3
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -92($fp)
        sw    $t0, 0($sp)
        li    $t0, 3
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t9 = &t7
        addiu $t0, $fp, -88
        sw    $t0, -96($fp)
        # param t9
        # t10 = call Tag::value(), 1
        addiu $sp, $sp, -8
        lw    $t0, -96($fp)
        sw    $t0, 0($sp)
        jal   _ZN3Tag5valueEv
        addiu $sp, $sp, 8
        sw    $v0, -100($fp)
        # param 4
        # t11 = call make(int), 1
        addiu $sp, $sp, -8
        li    $t0, 4
        sw    $t0, 0($sp)
        jal   _Z4makei
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -104
        li    $a2, 4
        jal   __memcpy
        # t12 = &t11
        addiu $t0, $fp, -104
        sw    $t0, -108($fp)
        # t13 = &t11
        addiu $t0, $fp, -104
        sw    $t0, -112($fp)
        # param t13
        # t14 = call Tag::value(), 1
        addiu $sp, $sp, -8
        lw    $t0, -112($fp)
        sw    $t0, 0($sp)
        jal   _ZN3Tag5valueEv
        addiu $sp, $sp, 8
        sw    $v0, -116($fp)
        # t15 = t10 int+ t14
        lw    $t0, -100($fp)
        lw    $t1, -116($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -120($fp)
        # v = t15
        lw    $t0, -120($fp)
        sw    $t0, -4($fp)
        # t16 = &t11
        addiu $t0, $fp, -104
        sw    $t0, -124($fp)
        # param t16
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -124($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t17 = &t7
        addiu $t0, $fp, -88
        sw    $t0, -128($fp)
        # param t17
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -128($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param 5
        # t18 = call make(int), 1
        addiu $sp, $sp, -8
        li    $t0, 5
        sw    $t0, 0($sp)
        jal   _Z4makei
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -132
        li    $a2, 4
        jal   __memcpy
        # t19 = &t18
        addiu $t0, $fp, -132
        sw    $t0, -136($fp)
        # kept = t18
        addiu $a0, $fp, -8
        addiu $a1, $fp, -132
        li    $a2, 4
        jal   __memcpy
        # t20 = &kept
        addiu $t0, $fp, -8
        sw    $t0, -140($fp)
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t21 = &kept
        addiu $t0, $fp, -8
        sw    $t0, -144($fp)
        # t23 = &t22
        addiu $t0, $fp, -148
        sw    $t0, -152($fp)
        # param t23
        # param 6
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -152($fp)
        sw    $t0, 0($sp)
        li    $t0, 6
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t24 = &t22
        addiu $t0, $fp, -148
        sw    $t0, -156($fp)
        # param t21
        # param t24
        # t25 = call Tag::operator+(const class Tag &), 2
        addiu $sp, $sp, -8
        lw    $t0, -144($fp)
        sw    $t0, 0($sp)
        lw    $t0, -156($fp)
        sw    $t0, 4($sp)
        jal   _ZN3TagplERKS_
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -160
        li    $a2, 4
        jal   __memcpy
        # t26 = &t25
        addiu $t0, $fp, -160
        sw    $t0, -164($fp)
        # sum = t25
        addiu $a0, $fp, -12
        addiu $a1, $fp, -160
        li    $a2, 4
        jal   __memcpy
        # t27 = &sum
        addiu $t0, $fp, -12
        sw    $t0, -168($fp)
        # t28 = &t22
        addiu $t0, $fp, -148
        sw    $t0, -172($fp)
        # param t28
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -172($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t29 = sum[0]
        addiu $t8, $fp, -12
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -176($fp)
        # param "%d | "
        # param t29
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -176($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t30 = &kept
        addiu $t0, $fp, -8
        sw    $t0, -180($fp)
        # t31 = &sum
        addiu $t0, $fp, -12
        sw    $t0, -184($fp)
        # param t30
        # param t31
        # t32 = call Tag::operator+(const class Tag &), 2
        addiu $sp, $sp, -8
        lw    $t0, -180($fp)
        sw    $t0, 0($sp)
        lw    $t0, -184($fp)
        sw    $t0, 4($sp)
        jal   _ZN3TagplERKS_
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -188
        li    $a2, 4
        jal   __memcpy
        # t33 = &t32
        addiu $t0, $fp, -188
        sw    $t0, -192($fp)
        # t34 = &t32
        addiu $t0, $fp, -188
        sw    $t0, -196($fp)
        # t35 = &kept
        addiu $t0, $fp, -8
        sw    $t0, -200($fp)
        # param t34
        # param t35
        # t36 = call Tag::operator+(const class Tag &), 2
        addiu $sp, $sp, -8
        lw    $t0, -196($fp)
        sw    $t0, 0($sp)
        lw    $t0, -200($fp)
        sw    $t0, 4($sp)
        jal   _ZN3TagplERKS_
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -204
        li    $a2, 4
        jal   __memcpy
        # t37 = &t36
        addiu $t0, $fp, -204
        sw    $t0, -208($fp)
        # t38 = t36[0]
        addiu $t8, $fp, -204
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -212($fp)
        # v = t38
        lw    $t0, -212($fp)
        sw    $t0, -4($fp)
        # t39 = &t36
        addiu $t0, $fp, -204
        sw    $t0, -216($fp)
        # param t39
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -216($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t40 = &t32
        addiu $t0, $fp, -188
        sw    $t0, -220($fp)
        # param t40
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -220($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t42 = &t41
        addiu $t0, $fp, -224
        sw    $t0, -228($fp)
        # param t42
        # param 10
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -228($fp)
        sw    $t0, 0($sp)
        li    $t0, 10
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # param t41
        # t43 = call byValue(class Tag), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -224
        li    $a2, 4
        jal   __memcpy
        jal   _Z7byValue3Tag
        addiu $sp, $sp, 8
        sw    $v0, -232($fp)
        # v = t43
        lw    $t0, -232($fp)
        sw    $t0, -4($fp)
        # t44 = &t41
        addiu $t0, $fp, -224
        sw    $t0, -236($fp)
        # param t44
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -236($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t45 = kept
        addiu $a0, $fp, -240
        addiu $a1, $fp, -8
        li    $a2, 4
        jal   __memcpy
        # t46 = &t45
        addiu $t0, $fp, -240
        sw    $t0, -244($fp)
        # param t45
        # t47 = call byValue(class Tag), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -240
        li    $a2, 4
        jal   __memcpy
        jal   _Z7byValue3Tag
        addiu $sp, $sp, 8
        sw    $v0, -248($fp)
        # v = t47
        lw    $t0, -248($fp)
        sw    $t0, -4($fp)
        # t48 = &t45
        addiu $t0, $fp, -240
        sw    $t0, -252($fp)
        # param t48
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -252($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t50 = &t49
        addiu $t0, $fp, -256
        sw    $t0, -260($fp)
        # param t50
        # param 11
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -260($fp)
        sw    $t0, 0($sp)
        li    $t0, 11
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t51 = &t49
        addiu $t0, $fp, -256
        sw    $t0, -264($fp)
        # param t51
        # t52 = call byRef(const class Tag &), 1
        addiu $sp, $sp, -8
        lw    $t0, -264($fp)
        sw    $t0, 0($sp)
        jal   _Z5byRefRK3Tag
        addiu $sp, $sp, 8
        sw    $v0, -268($fp)
        # v = t52
        lw    $t0, -268($fp)
        sw    $t0, -4($fp)
        # t53 = &t49
        addiu $t0, $fp, -256
        sw    $t0, -272($fp)
        # param t53
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -272($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t55 = &t54
        addiu $t0, $fp, -276
        sw    $t0, -280($fp)
        # param t55
        # param 12
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -280($fp)
        sw    $t0, 0($sp)
        li    $t0, 12
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t56 = &t54
        addiu $t0, $fp, -276
        sw    $t0, -284($fp)
        # param t56
        # t57 = call byRef(const class Tag &), 1
        addiu $sp, $sp, -8
        lw    $t0, -284($fp)
        sw    $t0, 0($sp)
        jal   _Z5byRefRK3Tag
        addiu $sp, $sp, 8
        sw    $v0, -288($fp)
        # t58 = &t54
        addiu $t0, $fp, -276
        sw    $t0, -292($fp)
        # param t58
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -292($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # if t57 int> 5 goto 140
        lw    $t0, -288($fp)
        li    $t1, 5
        bgt   $t0, $t1, L20_140
        # goto 142
        j     L20_142
L20_140:
        # param "if "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str7
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
L20_142:
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i = 0
        li    $t0, 0
        sw    $t0, -16($fp)
L20_145:
        # if i int< 2 goto 147
        lw    $t0, -16($fp)
        li    $t1, 2
        blt   $t0, $t1, L20_147
        # goto 172
        j     L20_172
L20_147:
        # t59 = 13 int+ i
        li    $t0, 13
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -296($fp)
        # param t59
        # t60 = call make(int), 1
        addiu $sp, $sp, -8
        lw    $t0, -296($fp)
        sw    $t0, 0($sp)
        jal   _Z4makei
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -300
        li    $a2, 4
        jal   __memcpy
        # t61 = &t60
        addiu $t0, $fp, -300
        sw    $t0, -304($fp)
        # t62 = t60[0]
        addiu $t8, $fp, -300
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -308($fp)
        # t63 = &t60
        addiu $t0, $fp, -300
        sw    $t0, -312($fp)
        # param t63
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -312($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # if t62 int> 0 goto 157
        lw    $t0, -308($fp)
        li    $t1, 0
        bgt   $t0, $t1, L20_157
        # goto 172
        j     L20_172
L20_157:
        # param "body "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t65 = &t64
        addiu $t0, $fp, -316
        sw    $t0, -320($fp)
        # param t65
        # param 20
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -320($fp)
        sw    $t0, 0($sp)
        li    $t0, 20
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t66 = &t64
        addiu $t0, $fp, -316
        sw    $t0, -324($fp)
        # param t66
        # t67 = call byRef(const class Tag &), 1
        addiu $sp, $sp, -8
        lw    $t0, -324($fp)
        sw    $t0, 0($sp)
        jal   _Z5byRefRK3Tag
        addiu $sp, $sp, 8
        sw    $v0, -328($fp)
        # t68 = i int+ t67
        lw    $t0, -16($fp)
        lw    $t1, -328($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -332($fp)
        # i = t68
        lw    $t0, -332($fp)
        sw    $t0, -16($fp)
        # t69 = &t64
        addiu $t0, $fp, -316
        sw    $t0, -336($fp)
        # param t69
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -336($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # goto 145
        j     L20_145
L20_172:
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if v int> 0 goto 176
        lw    $t0, -4($fp)
        li    $t1, 0
        bgt   $t0, $t1, L20_176
        # goto 186
        j     L20_186
L20_176:
        # t72 = &t71
        addiu $t0, $fp, -344
        sw    $t0, -348($fp)
        # param t72
        # param 21
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -348($fp)
        sw    $t0, 0($sp)
        li    $t0, 21
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t73 = t71[0]
        addiu $t8, $fp, -344
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -352($fp)
        # t70 = t73
        lw    $t0, -352($fp)
        sw    $t0, -340($fp)
        # t74 = &t71
        addiu $t0, $fp, -344
        sw    $t0, -356($fp)
        # param t74
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -356($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # goto 195
        j     L20_195
L20_186:
        # t76 = &t75
        addiu $t0, $fp, -360
        sw    $t0, -364($fp)
        # param t76
        # param 22
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -364($fp)
        sw    $t0, 0($sp)
        li    $t0, 22
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t77 = t75[0]
        addiu $t8, $fp, -360
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -368($fp)
        # t70 = t77
        lw    $t0, -368($fp)
        sw    $t0, -340($fp)
        # t78 = &t75
        addiu $t0, $fp, -360
        sw    $t0, -372($fp)
        # param t78
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -372($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
L20_195:
        # v = t70
        lw    $t0, -340($fp)
        sw    $t0, -4($fp)
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param 30
        # t79 = call named(int), 1
        addiu $sp, $sp, -8
        li    $t0, 30
        sw    $t0, 0($sp)
        jal   _Z5namedi
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -376
        li    $a2, 4
        jal   __memcpy
        # t80 = &t79
        addiu $t0, $fp, -376
        sw    $t0, -380($fp)
        # n = t79
        addiu $a0, $fp, -20
        addiu $a1, $fp, -376
        li    $a2, 4
        jal   __memcpy
        # t81 = &n
        addiu $t0, $fp, -20
        sw    $t0, -384($fp)
        # t82 = n[0]
        addiu $t8, $fp, -20
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -388($fp)
        # param "%d | "
        # param t82
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -388($fp)
        sw    $t0, 4($sp)
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
        addiu $a0, $fp, -392
        li    $a2, 4
        jal   __memcpy
        # t84 = &t83
        addiu $t0, $fp, -392
        sw    $t0, -396($fp)
        # t85 = t83[0]
        addiu $t8, $fp, -392
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -400($fp)
        # v = t85
        lw    $t0, -400($fp)
        sw    $t0, -4($fp)
        # t86 = &t83
        addiu $t0, $fp, -392
        sw    $t0, -404($fp)
        # param t86
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -404($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param 0
        # t87 = call pick(int), 1
        addiu $sp, $sp, -8
        li    $t0, 0
        sw    $t0, 0($sp)
        jal   _Z4picki
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -408
        li    $a2, 4
        jal   __memcpy
        # t88 = &t87
        addiu $t0, $fp, -408
        sw    $t0, -412($fp)
        # t89 = t87[0]
        addiu $t8, $fp, -408
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -416($fp)
        # t90 = v int+ t89
        lw    $t0, -4($fp)
        lw    $t1, -416($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -420($fp)
        # v = t90
        lw    $t0, -420($fp)
        sw    $t0, -4($fp)
        # t91 = &t87
        addiu $t0, $fp, -408
        sw    $t0, -424($fp)
        # param t91
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -424($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t93 = &t92
        addiu $t0, $fp, -428
        sw    $t0, -432($fp)
        # param t93
        # param 50
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -432($fp)
        sw    $t0, 0($sp)
        li    $t0, 50
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t94 = &t92
        addiu $t0, $fp, -428
        sw    $t0, -436($fp)
        # r = t94
        lw    $t0, -436($fp)
        sw    $t0, -24($fp)
        # t95 = *r
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -440($fp)
        # param "%d | "
        # param t95
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -440($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t97 = &t96
        addiu $t0, $fp, -444
        sw    $t0, -448($fp)
        # param t97
        # param 60
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -448($fp)
        sw    $t0, 0($sp)
        li    $t0, 60
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # kept = t96
        addiu $a0, $fp, -8
        addiu $a1, $fp, -444
        li    $a2, 4
        jal   __memcpy
        # t98 = &t96
        addiu $t0, $fp, -444
        sw    $t0, -452($fp)
        # param t98
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -452($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t99 = kept[0]
        addiu $t8, $fp, -8
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -456($fp)
        # param "%d\n"
        # param t99
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str9
        sw    $t0, 0($sp)
        lw    $t0, -456($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t100 = &c
        addiu $t0, $fp, -28
        sw    $t0, -460($fp)
        # param t100
        # param 1
        # call Copy::Copy(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -460($fp)
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1Ei
        addiu $sp, $sp, 8
        # param "| "
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t102 = &t101
        addiu $t0, $fp, -464
        sw    $t0, -468($fp)
        # t103 = &c
        addiu $t0, $fp, -28
        sw    $t0, -472($fp)
        # param t102
        # param t103
        # call Copy::Copy(const class Copy &), 2
        addiu $sp, $sp, -8
        lw    $t0, -468($fp)
        sw    $t0, 0($sp)
        lw    $t0, -472($fp)
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1ERKS_
        addiu $sp, $sp, 8
        # param t101
        # t104 = call copied(class Copy), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -464
        li    $a2, 4
        jal   __memcpy
        jal   _Z6copied4Copy
        addiu $sp, $sp, 8
        sw    $v0, -476($fp)
        # v = t104
        lw    $t0, -476($fp)
        sw    $t0, -4($fp)
        # t105 = &t101
        addiu $t0, $fp, -464
        sw    $t0, -480($fp)
        # param t105
        # call Copy::~Copy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -480($fp)
        sw    $t0, 0($sp)
        jal   _ZN4CopyD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t107 = &t106
        addiu $t0, $fp, -484
        sw    $t0, -488($fp)
        # param t107
        # param 2
        # call Copy::Copy(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -488($fp)
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1Ei
        addiu $sp, $sp, 8
        # param t106
        # t108 = call copied(class Copy), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -484
        li    $a2, 4
        jal   __memcpy
        jal   _Z6copied4Copy
        addiu $sp, $sp, 8
        sw    $v0, -492($fp)
        # v = t108
        lw    $t0, -492($fp)
        sw    $t0, -4($fp)
        # t109 = &t106
        addiu $t0, $fp, -484
        sw    $t0, -496($fp)
        # param t109
        # call Copy::~Copy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -496($fp)
        sw    $t0, 0($sp)
        jal   _ZN4CopyD1Ev
        addiu $sp, $sp, 8
        # param "%d | "
        # param v
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -4($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param 3
        # t110 = call makeCopy(int), 1
        addiu $sp, $sp, -8
        li    $t0, 3
        sw    $t0, 0($sp)
        jal   _Z8makeCopyi
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -500
        li    $a2, 4
        jal   __memcpy
        # t111 = &t110
        addiu $t0, $fp, -500
        sw    $t0, -504($fp)
        # d = t110
        addiu $a0, $fp, -32
        addiu $a1, $fp, -500
        li    $a2, 4
        jal   __memcpy
        # t112 = &d
        addiu $t0, $fp, -32
        sw    $t0, -508($fp)
        # t113 = d[0]
        addiu $t8, $fp, -32
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -512($fp)
        # param "%d | "
        # param t113
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -512($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t115 = &t114
        addiu $t0, $fp, -516
        sw    $t0, -520($fp)
        # t116 = &c
        addiu $t0, $fp, -28
        sw    $t0, -524($fp)
        # param t115
        # param t116
        # call Copy::Copy(const class Copy &), 2
        addiu $sp, $sp, -8
        lw    $t0, -520($fp)
        sw    $t0, 0($sp)
        lw    $t0, -524($fp)
        sw    $t0, 4($sp)
        jal   _ZN4CopyC1ERKS_
        addiu $sp, $sp, 8
        # param t114
        # t117 = call sameCopy(class Copy), 1
        addiu $sp, $sp, -8
        addiu $a0, $sp, 0
        addiu $a1, $fp, -516
        li    $a2, 4
        jal   __memcpy
        jal   _Z8sameCopy4Copy
        addiu $sp, $sp, 8
        move  $a1, $v0
        addiu $a0, $fp, -528
        li    $a2, 4
        jal   __memcpy
        # t118 = &t117
        addiu $t0, $fp, -528
        sw    $t0, -532($fp)
        # e = t117
        addiu $a0, $fp, -36
        addiu $a1, $fp, -528
        li    $a2, 4
        jal   __memcpy
        # t119 = &e
        addiu $t0, $fp, -36
        sw    $t0, -536($fp)
        # t120 = &t114
        addiu $t0, $fp, -516
        sw    $t0, -540($fp)
        # param t120
        # call Copy::~Copy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -540($fp)
        sw    $t0, 0($sp)
        jal   _ZN4CopyD1Ev
        addiu $sp, $sp, 8
        # t121 = e[0]
        addiu $t8, $fp, -36
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -544($fp)
        # param "%d\n"
        # param t121
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str9
        sw    $t0, 0($sp)
        lw    $t0, -544($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t122 = &q
        addiu $t0, $fp, -37
        sw    $t0, -548($fp)
        # p = t122
        lw    $t0, -548($fp)
        sw    $t0, -44($fp)
        # t123 = &q
        addiu $t0, $fp, -37
        sw    $t0, -552($fp)
        # param t123
        # t124 = call Square::sides(), 1
        addiu $sp, $sp, -8
        lw    $t0, -552($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Square5sidesEv
        addiu $sp, $sp, 8
        sw    $v0, -556($fp)
        # t125 = &q
        addiu $t0, $fp, -37
        sw    $t0, -560($fp)
        # param t125
        # t126 = call Shape::sides(), 1
        addiu $sp, $sp, -8
        lw    $t0, -560($fp)
        sw    $t0, 0($sp)
        jal   _ZN5Shape5sidesEv
        addiu $sp, $sp, 8
        sw    $v0, -564($fp)
        # param p
        # t127 = call Shape::sides(), 1
        addiu $sp, $sp, -8
        lw    $t0, -44($fp)
        sw    $t0, 0($sp)
        jal   _ZN5Shape5sidesEv
        addiu $sp, $sp, 8
        sw    $v0, -568($fp)
        # param p
        # t128 = call Shape::sides(), 1
        addiu $sp, $sp, -8
        lw    $t0, -44($fp)
        sw    $t0, 0($sp)
        jal   _ZN5Shape5sidesEv
        addiu $sp, $sp, 8
        sw    $v0, -572($fp)
        # t129 = &q
        addiu $t0, $fp, -37
        sw    $t0, -576($fp)
        # param t129
        # t130 = call Square::kind(), 1
        addiu $sp, $sp, -8
        lw    $t0, -576($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Square4kindEv
        addiu $sp, $sp, 8
        sw    $v0, -580($fp)
        # t131 = &q
        addiu $t0, $fp, -37
        sw    $t0, -584($fp)
        # param t131
        # t132 = call Shape::kind(), 1
        addiu $sp, $sp, -8
        lw    $t0, -584($fp)
        sw    $t0, 0($sp)
        jal   _ZN5Shape4kindEv
        addiu $sp, $sp, 8
        sw    $v0, -588($fp)
        # param "%d %d %d %d %d %d\n"
        # param t124
        # param t126
        # param t127
        # param t128
        # param t130
        # param t132
        # call printf, 7
        addiu $sp, $sp, -32
        la    $t0, str10
        sw    $t0, 0($sp)
        lw    $t0, -556($fp)
        sw    $t0, 4($sp)
        lw    $t0, -564($fp)
        sw    $t0, 8($sp)
        lw    $t0, -568($fp)
        sw    $t0, 12($sp)
        lw    $t0, -572($fp)
        sw    $t0, 16($sp)
        lw    $t0, -580($fp)
        sw    $t0, 20($sp)
        lw    $t0, -588($fp)
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
        sw    $v0, -600($fp)
        sw    $v1, -596($fp)
        # m = t133
        lw    $t0, -600($fp)
        lw    $t1, -596($fp)
        sw    $t0, -56($fp)
        sw    $t1, -52($fp)
        # t134 = int- 7
        li    $t0, 7
        negu  $t0, $t0
        sw    $t0, -604($fp)
        # t135 = inttollong t134
        lw    $t0, -604($fp)
        sra   $t1, $t0, 31
        sw    $t0, -616($fp)
        sw    $t1, -612($fp)
        # t136 = 1 llong<< 40
        li    $a0, 1
        li    $a1, 0
        li    $a2, 40
        jal   __shlll
        sw    $v0, -624($fp)
        sw    $v1, -620($fp)
        # param t135
        # param t136
        # param 9
        # t137 = call mix(long long, long long, int), 3
        addiu $sp, $sp, -24
        lw    $t0, -616($fp)
        lw    $t1, -612($fp)
        sw    $t0, 0($sp)
        sw    $t1, 4($sp)
        lw    $t0, -624($fp)
        lw    $t1, -620($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        li    $t0, 9
        sw    $t0, 16($sp)
        jal   _Z3mixxxi
        addiu $sp, $sp, 24
        sw    $v0, -632($fp)
        sw    $v1, -628($fp)
        # param "%lld %lld\n"
        # param m
        # param t137
        # call printf, 3
        addiu $sp, $sp, -24
        la    $t0, str11
        sw    $t0, 0($sp)
        lw    $t0, -56($fp)
        lw    $t1, -52($fp)
        sw    $t0, 8($sp)
        sw    $t1, 12($sp)
        lw    $t0, -632($fp)
        lw    $t1, -628($fp)
        sw    $t0, 16($sp)
        sw    $t1, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # t138 = &inner
        addiu $t0, $fp, -60
        sw    $t0, -636($fp)
        # param t138
        # param 70
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -636($fp)
        sw    $t0, 0($sp)
        li    $t0, 70
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t139 = &inner
        addiu $t0, $fp, -60
        sw    $t0, -640($fp)
        # param t139
        # t140 = call byRef(const class Tag &), 1
        addiu $sp, $sp, -8
        lw    $t0, -640($fp)
        sw    $t0, 0($sp)
        jal   _Z5byRefRK3Tag
        addiu $sp, $sp, 8
        sw    $v0, -644($fp)
        # t142 = &t141
        addiu $t0, $fp, -648
        sw    $t0, -652($fp)
        # param t142
        # param 71
        # call Tag::Tag(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -652($fp)
        sw    $t0, 0($sp)
        li    $t0, 71
        sw    $t0, 4($sp)
        jal   _ZN3TagC1Ei
        addiu $sp, $sp, 8
        # t143 = &t141
        addiu $t0, $fp, -648
        sw    $t0, -656($fp)
        # param t143
        # t144 = call byRef(const class Tag &), 1
        addiu $sp, $sp, -8
        lw    $t0, -656($fp)
        sw    $t0, 0($sp)
        jal   _Z5byRefRK3Tag
        addiu $sp, $sp, 8
        sw    $v0, -660($fp)
        # t145 = t140 int+ t144
        lw    $t0, -644($fp)
        lw    $t1, -660($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -664($fp)
        # param "%d "
        # param t145
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str12
        sw    $t0, 0($sp)
        lw    $t0, -664($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t146 = &t141
        addiu $t0, $fp, -648
        sw    $t0, -668($fp)
        # param t146
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -668($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t147 = &inner
        addiu $t0, $fp, -60
        sw    $t0, -672($fp)
        # param t147
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -672($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # param "end\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str13
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t148 = &e
        addiu $t0, $fp, -36
        sw    $t0, -676($fp)
        # param t148
        # call Copy::~Copy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -676($fp)
        sw    $t0, 0($sp)
        jal   _ZN4CopyD1Ev
        addiu $sp, $sp, 8
        # t149 = &d
        addiu $t0, $fp, -32
        sw    $t0, -680($fp)
        # param t149
        # call Copy::~Copy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -680($fp)
        sw    $t0, 0($sp)
        jal   _ZN4CopyD1Ev
        addiu $sp, $sp, 8
        # t150 = &c
        addiu $t0, $fp, -28
        sw    $t0, -684($fp)
        # param t150
        # call Copy::~Copy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -684($fp)
        sw    $t0, 0($sp)
        jal   _ZN4CopyD1Ev
        addiu $sp, $sp, 8
        # t151 = &t92
        addiu $t0, $fp, -428
        sw    $t0, -688($fp)
        # param t151
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -688($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t152 = &n
        addiu $t0, $fp, -20
        sw    $t0, -692($fp)
        # param t152
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -692($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t153 = &sum
        addiu $t0, $fp, -12
        sw    $t0, -696($fp)
        # param t153
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -696($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # t154 = &kept
        addiu $t0, $fp, -8
        sw    $t0, -700($fp)
        # param t154
        # call Tag::~Tag(), 1
        addiu $sp, $sp, -8
        lw    $t0, -700($fp)
        sw    $t0, 0($sp)
        jal   _ZN3TagD1Ev
        addiu $sp, $sp, 8
        # return 0
        li    $v0, 0
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
