# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t31_virtual.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g__ZTV6Animal:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV3Dog:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV5Puppy:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV7Swimmer:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV4Seal:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .byte 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV4Seal_8:
        .byte 0, 0, 0, 0, 248, 255, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV5Shape:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV4Rect:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        .align 3
g__ZTV6Square:
        .byte 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
str0:
        .byte 91, 65, 32, 37, 115, 93, 32, 0
str1:
        .byte 91, 126, 65, 32, 37, 115, 93, 32, 0
str2:
        .byte 97, 110, 105, 109, 97, 108, 0
str3:
        .byte 91, 68, 32, 37, 115, 93, 32, 0
str4:
        .byte 91, 126, 68, 32, 37, 115, 93, 32, 0
str5:
        .byte 100, 111, 103, 0
str6:
        .byte 112, 117, 112, 112, 121, 0
str7:
        .byte 115, 101, 97, 108, 0
str8:
        .byte 10, 0
str9:
        .byte 37, 115, 32, 37, 100, 32, 37, 100, 32, 124, 32, 0
str10:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str11:
        .byte 37, 115, 32, 37, 100, 32, 37, 100, 10, 0
str12:
        .byte 37, 115, 32, 37, 100, 10, 0
str13:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 124, 32, 0

        .text
        .globl main
main:
        li    $t0, -8
        and   $sp, $sp, $t0           # frames assume an 8-byte aligned stack
        addiu $sp, $sp, -8
        sw    $a0, 0($sp)             # argc
        sw    $a1, 4($sp)             # argv
        la    $t0, _ZNK6Animal4nameEv
        sw    $t0, g__ZTV6Animal+0
        la    $t0, _ZN6Animal5speedEv
        sw    $t0, g__ZTV6Animal+8
        la    $t0, _ZNK3Dog4nameEv
        sw    $t0, g__ZTV3Dog+0
        la    $t0, _ZN3Dog5speedEv
        sw    $t0, g__ZTV3Dog+8
        la    $t0, _ZNK5Puppy4nameEv
        sw    $t0, g__ZTV5Puppy+0
        la    $t0, _ZN3Dog5speedEv
        sw    $t0, g__ZTV5Puppy+8
        la    $t0, _ZN7Swimmer4swimEv
        sw    $t0, g__ZTV7Swimmer+0
        la    $t0, _ZN7Swimmer4diveEi
        sw    $t0, g__ZTV7Swimmer+8
        la    $t0, _ZNK4Seal4nameEv
        sw    $t0, g__ZTV4Seal+0
        la    $t0, _ZN6Animal5speedEv
        sw    $t0, g__ZTV4Seal+8
        la    $t0, _ZN4Seal4swimEv
        sw    $t0, g__ZTV4Seal+16
        la    $t0, _ZN4Seal4swimEv
        sw    $t0, g__ZTV4Seal_8+0
        la    $t0, _ZN7Swimmer4diveEi
        sw    $t0, g__ZTV4Seal_8+8
        la    $t0, _ZN5Shape5sidesEv
        sw    $t0, g__ZTV5Shape+8
        la    $t0, _ZN4Rect4areaEv
        sw    $t0, g__ZTV4Rect+0
        la    $t0, _ZN4Rect5sidesEv
        sw    $t0, g__ZTV4Rect+8
        la    $t0, _ZN6Square4areaEv
        sw    $t0, g__ZTV6Square+0
        la    $t0, _ZN4Rect5sidesEv
        sw    $t0, g__ZTV6Square+8
        jal   main_
        move  $a0, $v0
        li    $v0, 17                 # exit with main's result
        syscall

# Animal::Animal(int)
_ZN6AnimalC1Ei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        # t1 = &_ZTV6Animal
        la    $t0, g__ZTV6Animal
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # t2 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # *t3 = n
        lw    $t8, -12($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t4 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = t4 ptr+ 4
        lw    $t0, -16($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t7 = *t6
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # t8 = this ptr+ t7
        lw    $t0, 8($fp)
        lw    $t1, -28($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # param t8
        # t9 = call *t5, 1
        addiu $sp, $sp, -8
        lw    $t0, -32($fp)
        sw    $t0, 0($sp)
        lw    $t9, -20($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -36($fp)
        # param "[A %s] "
        # param t9
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -36($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN6AnimalC1Ei_exit
_ZN6AnimalC1Ei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Animal::~Animal()
_ZN6AnimalD1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # t1 = &_ZTV6Animal
        la    $t0, g__ZTV6Animal
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # t2 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = *t2
        lw    $t8, -8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t4 = t2 ptr+ 4
        lw    $t0, -8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = this ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # param t6
        # t7 = call *t3, 1
        addiu $sp, $sp, -8
        lw    $t0, -24($fp)
        sw    $t0, 0($sp)
        lw    $t9, -12($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -28($fp)
        # param "[~A %s] "
        # param t7
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN6AnimalD1Ev_exit
_ZN6AnimalD1Ev_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Animal::name()
_ZNK6Animal4nameEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return "animal"
        la    $v0, str2
        j     _ZNK6Animal4nameEv_exit
_ZNK6Animal4nameEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Animal::speed()
_ZN6Animal5speedEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _ZN6Animal5speedEv_exit
_ZN6Animal5speedEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Animal::describe()
_ZN6Animal8describeEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = t1 ptr+ 8
        lw    $t0, -4($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = *t2
        lw    $t8, -8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t4 = t1 ptr+ 12
        lw    $t0, -4($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = this ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # param t6
        # t7 = call *t3, 1
        addiu $sp, $sp, -8
        lw    $t0, -24($fp)
        sw    $t0, 0($sp)
        lw    $t9, -12($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -28($fp)
        # t8 = t7 int* 10
        lw    $t0, -28($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t9 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # t10 = *t9
        lw    $t8, -36($fp)
        lw    $t0, 0($t8)
        sw    $t0, -40($fp)
        # t11 = t8 int+ t10
        lw    $t0, -32($fp)
        lw    $t1, -40($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -44($fp)
        # return t11
        lw    $v0, -44($fp)
        j     _ZN6Animal8describeEv_exit
_ZN6Animal8describeEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::Dog(int)
_ZN3DogC1Ei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        # param this
        # param 4
        # call Animal::Animal(int), 2
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        jal   _ZN6AnimalC1Ei
        addiu $sp, $sp, 8
        # t1 = &_ZTV3Dog
        la    $t0, g__ZTV3Dog
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # t2 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # *t3 = b
        lw    $t8, -12($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t4 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = t4 ptr+ 4
        lw    $t0, -16($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t7 = *t6
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # t8 = this ptr+ t7
        lw    $t0, 8($fp)
        lw    $t1, -28($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # param t8
        # t9 = call *t5, 1
        addiu $sp, $sp, -8
        lw    $t0, -32($fp)
        sw    $t0, 0($sp)
        lw    $t9, -20($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -36($fp)
        # param "[D %s] "
        # param t9
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -36($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN3DogC1Ei_exit
_ZN3DogC1Ei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::~Dog()
_ZN3DogD1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # t1 = &_ZTV3Dog
        la    $t0, g__ZTV3Dog
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # t2 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = *t2
        lw    $t8, -8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t4 = t2 ptr+ 4
        lw    $t0, -8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = this ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # param t6
        # t7 = call *t3, 1
        addiu $sp, $sp, -8
        lw    $t0, -24($fp)
        sw    $t0, 0($sp)
        lw    $t9, -12($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -28($fp)
        # param "[~D %s] "
        # param t7
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param this
        # call Animal::~Animal(), 1
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        jal   _ZN6AnimalD1Ev
        addiu $sp, $sp, 8
        # return
        j     _ZN3DogD1Ev_exit
_ZN3DogD1Ev_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::name()
_ZNK3Dog4nameEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return "dog"
        la    $v0, str5
        j     _ZNK3Dog4nameEv_exit
_ZNK3Dog4nameEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::speed()
_ZN3Dog5speedEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = 12 int+ t2
        li    $t0, 12
        lw    $t1, -8($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # return t3
        lw    $v0, -12($fp)
        j     _ZN3Dog5speedEv_exit
_ZN3Dog5speedEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Puppy::Puppy()
_ZN5PuppyC1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # param this
        # param 1
        # call Dog::Dog(int), 2
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        li    $t0, 1
        sw    $t0, 4($sp)
        jal   _ZN3DogC1Ei
        addiu $sp, $sp, 8
        # t1 = &_ZTV5Puppy
        la    $t0, g__ZTV5Puppy
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # return
        j     _ZN5PuppyC1Ev_exit
_ZN5PuppyC1Ev_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Puppy::name()
_ZNK5Puppy4nameEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return "puppy"
        la    $v0, str6
        j     _ZNK5Puppy4nameEv_exit
_ZNK5Puppy4nameEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Swimmer::Swimmer()
_ZN7SwimmerC1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = &_ZTV7Swimmer
        la    $t0, g__ZTV7Swimmer
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # t2 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # *t3 = 3
        lw    $t8, -12($fp)
        li    $t0, 3
        sw    $t0, 0($t8)
        # return
        j     _ZN7SwimmerC1Ev_exit
_ZN7SwimmerC1Ev_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Swimmer::swim()
_ZN7Swimmer4swimEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # t1 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _ZN7Swimmer4swimEv_exit
_ZN7Swimmer4swimEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Swimmer::dive(int)
_ZN7Swimmer4diveEi:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # t1 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = t2 int+ m
        lw    $t0, -8($fp)
        lw    $t1, 12($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # return t3
        lw    $v0, -12($fp)
        j     _ZN7Swimmer4diveEi_exit
_ZN7Swimmer4diveEi_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Seal::Seal()
_ZN4SealC1Ev:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # param this
        # param 0
        # call Animal::Animal(int), 2
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        li    $t0, 0
        sw    $t0, 4($sp)
        jal   _ZN6AnimalC1Ei
        addiu $sp, $sp, 8
        # t1 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # param t1
        # call Swimmer::Swimmer(), 1
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        jal   _ZN7SwimmerC1Ev
        addiu $sp, $sp, 8
        # t2 = &_ZTV4Seal
        la    $t0, g__ZTV4Seal
        sw    $t0, -8($fp)
        # *this = t2
        lw    $t8, 8($fp)
        lw    $t0, -8($fp)
        sw    $t0, 0($t8)
        # t3 = &_ZTV4Seal_8
        la    $t0, g__ZTV4Seal_8
        sw    $t0, -12($fp)
        # t4 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # *t4 = t3
        lw    $t8, -16($fp)
        lw    $t0, -12($fp)
        sw    $t0, 0($t8)
        # t5 = this ptr+ 16
        lw    $t0, 8($fp)
        li    $t1, 16
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t6 = this ptr+ 16
        lw    $t0, 8($fp)
        li    $t1, 16
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # *t6 = 7
        lw    $t8, -24($fp)
        li    $t0, 7
        sw    $t0, 0($t8)
        # return
        j     _ZN4SealC1Ev_exit
_ZN4SealC1Ev_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Seal::name()
_ZNK4Seal4nameEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return "seal"
        la    $v0, str7
        j     _ZNK4Seal4nameEv_exit
_ZNK4Seal4nameEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Seal::swim()
_ZN4Seal4swimEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t1 = this ptr+ 16
        lw    $t0, 8($fp)
        li    $t1, 16
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = t2 int* 2
        lw    $t0, -8($fp)
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = this ptr+ 12
        lw    $t0, 8($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = t3 int+ t5
        lw    $t0, -12($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # return t6
        lw    $v0, -24($fp)
        j     _ZN4Seal4swimEv_exit
_ZN4Seal4swimEv_exit:
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

# Shape::twice()
_ZN5Shape5twiceEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # t1 = *this
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = t1 ptr+ 4
        lw    $t0, -4($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = *t3
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = this ptr+ t4
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # param t5
        # t6 = call *t2, 1
        addiu $sp, $sp, -8
        lw    $t0, -20($fp)
        sw    $t0, 0($sp)
        lw    $t9, -8($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -24($fp)
        # t7 = t6 int* 2
        lw    $t0, -24($fp)
        li    $t1, 2
        mul   $t0, $t0, $t1
        sw    $t0, -28($fp)
        # return t7
        lw    $v0, -28($fp)
        j     _ZN5Shape5twiceEv_exit
_ZN5Shape5twiceEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Rect::Rect(int, int)
_ZN4RectC1Eii:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t1 = &_ZTV5Shape
        la    $t0, g__ZTV5Shape
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # t2 = &_ZTV4Rect
        la    $t0, g__ZTV4Rect
        sw    $t0, -8($fp)
        # *this = t2
        lw    $t8, 8($fp)
        lw    $t0, -8($fp)
        sw    $t0, 0($t8)
        # t3 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # *t4 = a
        lw    $t8, -16($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t5 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t6 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # *t6 = b
        lw    $t8, -24($fp)
        lw    $t0, 16($fp)
        sw    $t0, 0($t8)
        # return
        j     _ZN4RectC1Eii_exit
_ZN4RectC1Eii_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Rect::area()
_ZN4Rect4areaEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t1 = this ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = this ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = *t3
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = t2 int* t4
        lw    $t0, -8($fp)
        lw    $t1, -16($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # return t5
        lw    $v0, -20($fp)
        j     _ZN4Rect4areaEv_exit
_ZN4Rect4areaEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Rect::sides()
_ZN4Rect5sidesEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        # return 4
        li    $v0, 4
        j     _ZN4Rect5sidesEv_exit
_ZN4Rect5sidesEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Square::Square(int)
_ZN6SquareC1Ei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # param this
        # param s
        # param s
        # call Rect::Rect(int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        lw    $t0, 12($fp)
        sw    $t0, 4($sp)
        lw    $t0, 12($fp)
        sw    $t0, 8($sp)
        jal   _ZN4RectC1Eii
        addiu $sp, $sp, 16
        # t1 = &_ZTV6Square
        la    $t0, g__ZTV6Square
        sw    $t0, -4($fp)
        # *this = t1
        lw    $t8, 8($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # return
        j     _ZN6SquareC1Ei_exit
_ZN6SquareC1Ei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Square::area()
_ZN6Square4areaEv:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        # param this
        # t1 = call Rect::area(), 1
        addiu $sp, $sp, -8
        lw    $t0, 8($fp)
        sw    $t0, 0($sp)
        jal   _ZN4Rect4areaEv
        addiu $sp, $sp, 8
        sw    $v0, -4($fp)
        # t2 = t1 int+ 1
        lw    $t0, -4($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # return t2
        lw    $v0, -8($fp)
        j     _ZN6Square4areaEv_exit
_ZN6Square4areaEv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# total(class Shape &)
_Z5totalR5Shape:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -56
        # t1 = *s
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = t1 ptr+ 4
        lw    $t0, -4($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = *t3
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # t5 = s ptr+ t4
        lw    $t0, 8($fp)
        lw    $t1, -16($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # param t5
        # t6 = call *t2, 1
        addiu $sp, $sp, -8
        lw    $t0, -20($fp)
        sw    $t0, 0($sp)
        lw    $t9, -8($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -24($fp)
        # t7 = *s
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # t8 = t7 ptr+ 8
        lw    $t0, -28($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # t9 = *t8
        lw    $t8, -32($fp)
        lw    $t0, 0($t8)
        sw    $t0, -36($fp)
        # t10 = t7 ptr+ 12
        lw    $t0, -28($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -40($fp)
        # t11 = *t10
        lw    $t8, -40($fp)
        lw    $t0, 0($t8)
        sw    $t0, -44($fp)
        # t12 = s ptr+ t11
        lw    $t0, 8($fp)
        lw    $t1, -44($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # param t12
        # t13 = call *t9, 1
        addiu $sp, $sp, -8
        lw    $t0, -48($fp)
        sw    $t0, 0($sp)
        lw    $t9, -36($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -52($fp)
        # t14 = t6 int+ t13
        lw    $t0, -24($fp)
        lw    $t1, -52($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -56($fp)
        # return t14
        lw    $v0, -56($fp)
        j     _Z5totalR5Shape_exit
_Z5totalR5Shape_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# race(class Animal *)
_Z4raceP6Animal:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # t1 = *a
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -4($fp)
        # t2 = t1 ptr+ 8
        lw    $t0, -4($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # t3 = *t2
        lw    $t8, -8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t4 = t1 ptr+ 12
        lw    $t0, -4($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # t6 = a ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # param t6
        # t7 = call *t3, 1
        addiu $sp, $sp, -8
        lw    $t0, -24($fp)
        sw    $t0, 0($sp)
        lw    $t9, -12($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -28($fp)
        # return t7
        lw    $v0, -28($fp)
        j     _Z4raceP6Animal_exit
_Z4raceP6Animal_exit:
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
        addiu $sp, $sp, -488
        # t1 = &d
        addiu $t0, $fp, -12
        sw    $t0, -116($fp)
        # param t1
        # param 5
        # call Dog::Dog(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -116($fp)
        sw    $t0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _ZN3DogC1Ei
        addiu $sp, $sp, 8
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t2 = &p
        addiu $t0, $fp, -24
        sw    $t0, -120($fp)
        # param t2
        # call Puppy::Puppy(), 1
        addiu $sp, $sp, -8
        lw    $t0, -120($fp)
        sw    $t0, 0($sp)
        jal   _ZN5PuppyC1Ev
        addiu $sp, $sp, 8
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t3 = &d
        addiu $t0, $fp, -12
        sw    $t0, -124($fp)
        # t4 = &p
        addiu $t0, $fp, -24
        sw    $t0, -128($fp)
        # zoo[0] = t3
        addiu $t8, $fp, -36
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, -124($fp)
        sw    $t0, 0($t8)
        # zoo[4] = t4
        addiu $t8, $fp, -36
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, -128($fp)
        sw    $t0, 0($t8)
        # zoo[8] = 0
        addiu $t8, $fp, -36
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # t5 = &s
        addiu $t0, $fp, -56
        sw    $t0, -132($fp)
        # param t5
        # call Seal::Seal(), 1
        addiu $sp, $sp, -8
        lw    $t0, -132($fp)
        sw    $t0, 0($sp)
        jal   _ZN4SealC1Ev
        addiu $sp, $sp, 8
        # t6 = &s
        addiu $t0, $fp, -56
        sw    $t0, -136($fp)
        # zoo[8] = t6
        addiu $t8, $fp, -36
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, -136($fp)
        sw    $t0, 0($t8)
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # i.13 = 0
        li    $t0, 0
        sw    $t0, -60($fp)
L26_24:
        # if i.13 int< 3 goto 26
        lw    $t0, -60($fp)
        li    $t1, 3
        blt   $t0, $t1, L26_26
        # goto 57
        j     L26_57
L26_26:
        # t7 = i.13 int* 4
        lw    $t0, -60($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -140($fp)
        # t8 = zoo[t7]
        addiu $t8, $fp, -36
        lw    $t9, -140($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -144($fp)
        # t9 = *t8
        lw    $t8, -144($fp)
        lw    $t0, 0($t8)
        sw    $t0, -148($fp)
        # t10 = *t9
        lw    $t8, -148($fp)
        lw    $t0, 0($t8)
        sw    $t0, -152($fp)
        # t11 = t9 ptr+ 4
        lw    $t0, -148($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -156($fp)
        # t12 = *t11
        lw    $t8, -156($fp)
        lw    $t0, 0($t8)
        sw    $t0, -160($fp)
        # t13 = t8 ptr+ t12
        lw    $t0, -144($fp)
        lw    $t1, -160($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -164($fp)
        # param t13
        # t14 = call *t10, 1
        addiu $sp, $sp, -8
        lw    $t0, -164($fp)
        sw    $t0, 0($sp)
        lw    $t9, -152($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -168($fp)
        # t15 = i.13 int* 4
        lw    $t0, -60($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -172($fp)
        # t16 = zoo[t15]
        addiu $t8, $fp, -36
        lw    $t9, -172($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -176($fp)
        # t17 = *t16
        lw    $t8, -176($fp)
        lw    $t0, 0($t8)
        sw    $t0, -180($fp)
        # t18 = t17 ptr+ 8
        lw    $t0, -180($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -184($fp)
        # t19 = *t18
        lw    $t8, -184($fp)
        lw    $t0, 0($t8)
        sw    $t0, -188($fp)
        # t20 = t17 ptr+ 12
        lw    $t0, -180($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -192($fp)
        # t21 = *t20
        lw    $t8, -192($fp)
        lw    $t0, 0($t8)
        sw    $t0, -196($fp)
        # t22 = t16 ptr+ t21
        lw    $t0, -176($fp)
        lw    $t1, -196($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -200($fp)
        # param t22
        # t23 = call *t19, 1
        addiu $sp, $sp, -8
        lw    $t0, -200($fp)
        sw    $t0, 0($sp)
        lw    $t9, -188($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -204($fp)
        # t24 = i.13 int* 4
        lw    $t0, -60($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -208($fp)
        # t25 = zoo[t24]
        addiu $t8, $fp, -36
        lw    $t9, -208($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -212($fp)
        # param t25
        # t26 = call Animal::describe(), 1
        addiu $sp, $sp, -8
        lw    $t0, -212($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Animal8describeEv
        addiu $sp, $sp, 8
        sw    $v0, -216($fp)
        # param "%s %d %d | "
        # param t14
        # param t23
        # param t26
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str9
        sw    $t0, 0($sp)
        lw    $t0, -168($fp)
        sw    $t0, 4($sp)
        lw    $t0, -204($fp)
        sw    $t0, 8($sp)
        lw    $t0, -216($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t27 = i.13 int+ 1
        lw    $t0, -60($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -220($fp)
        # i.13 = t27
        lw    $t0, -220($fp)
        sw    $t0, -60($fp)
        # goto 24
        j     L26_24
L26_57:
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t28 = &s
        addiu $t0, $fp, -56
        sw    $t0, -224($fp)
        # t29 = t28
        lw    $t0, -224($fp)
        sw    $t0, -228($fp)
        # if t28 ptr== 0 goto 63
        lw    $t0, -224($fp)
        li    $t1, 0
        beq   $t0, $t1, L26_63
        # t29 = t28 ptr+ 8
        lw    $t0, -224($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -228($fp)
L26_63:
        # w = t29
        lw    $t0, -228($fp)
        sw    $t0, -64($fp)
        # t30 = *w
        lw    $t8, -64($fp)
        lw    $t0, 0($t8)
        sw    $t0, -232($fp)
        # t31 = *t30
        lw    $t8, -232($fp)
        lw    $t0, 0($t8)
        sw    $t0, -236($fp)
        # t32 = t30 ptr+ 4
        lw    $t0, -232($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -240($fp)
        # t33 = *t32
        lw    $t8, -240($fp)
        lw    $t0, 0($t8)
        sw    $t0, -244($fp)
        # t34 = w ptr+ t33
        lw    $t0, -64($fp)
        lw    $t1, -244($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -248($fp)
        # param t34
        # t35 = call *t31, 1
        addiu $sp, $sp, -8
        lw    $t0, -248($fp)
        sw    $t0, 0($sp)
        lw    $t9, -236($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -252($fp)
        # t36 = *w
        lw    $t8, -64($fp)
        lw    $t0, 0($t8)
        sw    $t0, -256($fp)
        # t37 = t36 ptr+ 8
        lw    $t0, -256($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -260($fp)
        # t38 = *t37
        lw    $t8, -260($fp)
        lw    $t0, 0($t8)
        sw    $t0, -264($fp)
        # t39 = t36 ptr+ 12
        lw    $t0, -256($fp)
        li    $t1, 12
        addu  $t0, $t0, $t1
        sw    $t0, -268($fp)
        # t40 = *t39
        lw    $t8, -268($fp)
        lw    $t0, 0($t8)
        sw    $t0, -272($fp)
        # t41 = w ptr+ t40
        lw    $t0, -64($fp)
        lw    $t1, -272($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -276($fp)
        # param t41
        # param 2
        # t42 = call *t38, 2
        addiu $sp, $sp, -8
        lw    $t0, -276($fp)
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        lw    $t9, -264($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -280($fp)
        # t43 = &s
        addiu $t0, $fp, -56
        sw    $t0, -284($fp)
        # param t43
        # t44 = call race(class Animal *), 1
        addiu $sp, $sp, -8
        lw    $t0, -284($fp)
        sw    $t0, 0($sp)
        jal   _Z4raceP6Animal
        addiu $sp, $sp, 8
        sw    $v0, -288($fp)
        # param "%d %d %d\n"
        # param t35
        # param t42
        # param t44
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str10
        sw    $t0, 0($sp)
        lw    $t0, -252($fp)
        sw    $t0, 4($sp)
        lw    $t0, -280($fp)
        sw    $t0, 8($sp)
        lw    $t0, -288($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t45 = &p
        addiu $t0, $fp, -24
        sw    $t0, -292($fp)
        # ref = t45
        lw    $t0, -292($fp)
        sw    $t0, -68($fp)
        # t46 = *ref
        lw    $t8, -68($fp)
        lw    $t0, 0($t8)
        sw    $t0, -296($fp)
        # t47 = *t46
        lw    $t8, -296($fp)
        lw    $t0, 0($t8)
        sw    $t0, -300($fp)
        # t48 = t46 ptr+ 4
        lw    $t0, -296($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -304($fp)
        # t49 = *t48
        lw    $t8, -304($fp)
        lw    $t0, 0($t8)
        sw    $t0, -308($fp)
        # t50 = ref ptr+ t49
        lw    $t0, -68($fp)
        lw    $t1, -308($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -312($fp)
        # param t50
        # t51 = call *t47, 1
        addiu $sp, $sp, -8
        lw    $t0, -312($fp)
        sw    $t0, 0($sp)
        lw    $t9, -300($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -316($fp)
        # param ref
        # t52 = call Animal::speed(), 1
        addiu $sp, $sp, -8
        lw    $t0, -68($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Animal5speedEv
        addiu $sp, $sp, 8
        sw    $v0, -320($fp)
        # t53 = &d
        addiu $t0, $fp, -12
        sw    $t0, -324($fp)
        # param t53
        # t54 = call Animal::speed(), 1
        addiu $sp, $sp, -8
        lw    $t0, -324($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Animal5speedEv
        addiu $sp, $sp, 8
        sw    $v0, -328($fp)
        # param "%s %d %d\n"
        # param t51
        # param t52
        # param t54
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str11
        sw    $t0, 0($sp)
        lw    $t0, -316($fp)
        sw    $t0, 4($sp)
        lw    $t0, -320($fp)
        sw    $t0, 8($sp)
        lw    $t0, -328($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t55 = d[0]
        addiu $t8, $fp, -12
        li    $t9, 0
        addu  $t8, $t8, $t9
        addiu $a1, $t8, 0
        addiu $a0, $fp, -336
        li    $a2, 8
        jal   __memcpy
        # copy = t55
        addiu $a0, $fp, -76
        addiu $a1, $fp, -336
        li    $a2, 8
        jal   __memcpy
        # t56 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -340($fp)
        # t57 = &_ZTV6Animal
        la    $t0, g__ZTV6Animal
        sw    $t0, -344($fp)
        # *t56 = t57
        lw    $t8, -340($fp)
        lw    $t0, -344($fp)
        sw    $t0, 0($t8)
        # t58 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -348($fp)
        # param t58
        # t59 = call Animal::name(), 1
        addiu $sp, $sp, -8
        lw    $t0, -348($fp)
        sw    $t0, 0($sp)
        jal   _ZNK6Animal4nameEv
        addiu $sp, $sp, 8
        sw    $v0, -352($fp)
        # t60 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -356($fp)
        # param t60
        # t61 = call Animal::speed(), 1
        addiu $sp, $sp, -8
        lw    $t0, -356($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Animal5speedEv
        addiu $sp, $sp, 8
        sw    $v0, -360($fp)
        # param "%s %d\n"
        # param t59
        # param t61
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str12
        sw    $t0, 0($sp)
        lw    $t0, -352($fp)
        sw    $t0, 4($sp)
        lw    $t0, -360($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t62 = p[0]
        addiu $t8, $fp, -24
        li    $t9, 0
        addu  $t8, $t8, $t9
        addiu $a1, $t8, 0
        addiu $a0, $fp, -368
        li    $a2, 8
        jal   __memcpy
        # t63 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -372($fp)
        # t64 = *t63
        lw    $t8, -372($fp)
        lw    $t0, 0($t8)
        sw    $t0, -376($fp)
        # copy = t62
        addiu $a0, $fp, -76
        addiu $a1, $fp, -368
        li    $a2, 8
        jal   __memcpy
        # *t63 = t64
        lw    $t8, -372($fp)
        lw    $t0, -376($fp)
        sw    $t0, 0($t8)
        # t65 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -380($fp)
        # param t65
        # t66 = call Animal::name(), 1
        addiu $sp, $sp, -8
        lw    $t0, -380($fp)
        sw    $t0, 0($sp)
        jal   _ZNK6Animal4nameEv
        addiu $sp, $sp, 8
        sw    $v0, -384($fp)
        # t67 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -388($fp)
        # param t67
        # t68 = call Animal::speed(), 1
        addiu $sp, $sp, -8
        lw    $t0, -388($fp)
        sw    $t0, 0($sp)
        jal   _ZN6Animal5speedEv
        addiu $sp, $sp, 8
        sw    $v0, -392($fp)
        # param "%s %d\n"
        # param t66
        # param t68
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str12
        sw    $t0, 0($sp)
        lw    $t0, -384($fp)
        sw    $t0, 4($sp)
        lw    $t0, -392($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t69 = &r
        addiu $t0, $fp, -88
        sw    $t0, -396($fp)
        # param t69
        # param 2
        # param 3
        # call Rect::Rect(int, int), 3
        addiu $sp, $sp, -16
        lw    $t0, -396($fp)
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        li    $t0, 3
        sw    $t0, 8($sp)
        jal   _ZN4RectC1Eii
        addiu $sp, $sp, 16
        # t70 = &sq
        addiu $t0, $fp, -100
        sw    $t0, -400($fp)
        # param t70
        # param 4
        # call Square::Square(int), 2
        addiu $sp, $sp, -8
        lw    $t0, -400($fp)
        sw    $t0, 0($sp)
        li    $t0, 4
        sw    $t0, 4($sp)
        jal   _ZN6SquareC1Ei
        addiu $sp, $sp, 8
        # t71 = &r
        addiu $t0, $fp, -88
        sw    $t0, -404($fp)
        # t72 = &sq
        addiu $t0, $fp, -100
        sw    $t0, -408($fp)
        # shapes[0] = t71
        addiu $t8, $fp, -108
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, -404($fp)
        sw    $t0, 0($t8)
        # shapes[4] = t72
        addiu $t8, $fp, -108
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, -408($fp)
        sw    $t0, 0($t8)
        # i.20 = 0
        li    $t0, 0
        sw    $t0, -112($fp)
L26_151:
        # if i.20 int< 2 goto 153
        lw    $t0, -112($fp)
        li    $t1, 2
        blt   $t0, $t1, L26_153
        # goto 178
        j     L26_178
L26_153:
        # t73 = i.20 int* 4
        lw    $t0, -112($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -412($fp)
        # t74 = shapes[t73]
        addiu $t8, $fp, -108
        lw    $t9, -412($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -416($fp)
        # t75 = *t74
        lw    $t8, -416($fp)
        lw    $t0, 0($t8)
        sw    $t0, -420($fp)
        # t76 = *t75
        lw    $t8, -420($fp)
        lw    $t0, 0($t8)
        sw    $t0, -424($fp)
        # t77 = t75 ptr+ 4
        lw    $t0, -420($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -428($fp)
        # t78 = *t77
        lw    $t8, -428($fp)
        lw    $t0, 0($t8)
        sw    $t0, -432($fp)
        # t79 = t74 ptr+ t78
        lw    $t0, -416($fp)
        lw    $t1, -432($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -436($fp)
        # param t79
        # t80 = call *t76, 1
        addiu $sp, $sp, -8
        lw    $t0, -436($fp)
        sw    $t0, 0($sp)
        lw    $t9, -424($fp)
        jalr  $t9
        addiu $sp, $sp, 8
        sw    $v0, -440($fp)
        # t81 = i.20 int* 4
        lw    $t0, -112($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -444($fp)
        # t82 = shapes[t81]
        addiu $t8, $fp, -108
        lw    $t9, -444($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -448($fp)
        # param t82
        # t83 = call Shape::twice(), 1
        addiu $sp, $sp, -8
        lw    $t0, -448($fp)
        sw    $t0, 0($sp)
        jal   _ZN5Shape5twiceEv
        addiu $sp, $sp, 8
        sw    $v0, -452($fp)
        # t84 = i.20 int* 4
        lw    $t0, -112($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -456($fp)
        # t85 = shapes[t84]
        addiu $t8, $fp, -108
        lw    $t9, -456($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -460($fp)
        # param t85
        # t86 = call total(class Shape &), 1
        addiu $sp, $sp, -8
        lw    $t0, -460($fp)
        sw    $t0, 0($sp)
        jal   _Z5totalR5Shape
        addiu $sp, $sp, 8
        sw    $v0, -464($fp)
        # param "%d %d %d | "
        # param t80
        # param t83
        # param t86
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str13
        sw    $t0, 0($sp)
        lw    $t0, -440($fp)
        sw    $t0, 4($sp)
        lw    $t0, -452($fp)
        sw    $t0, 8($sp)
        lw    $t0, -464($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t87 = i.20 int+ 1
        lw    $t0, -112($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -468($fp)
        # i.20 = t87
        lw    $t0, -468($fp)
        sw    $t0, -112($fp)
        # goto 151
        j     L26_151
L26_178:
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t88 = &copy
        addiu $t0, $fp, -76
        sw    $t0, -472($fp)
        # param t88
        # call Animal::~Animal(), 1
        addiu $sp, $sp, -8
        lw    $t0, -472($fp)
        sw    $t0, 0($sp)
        jal   _ZN6AnimalD1Ev
        addiu $sp, $sp, 8
        # t89 = &s
        addiu $t0, $fp, -56
        sw    $t0, -476($fp)
        # param t89
        # call Animal::~Animal(), 1
        addiu $sp, $sp, -8
        lw    $t0, -476($fp)
        sw    $t0, 0($sp)
        jal   _ZN6AnimalD1Ev
        addiu $sp, $sp, 8
        # t90 = &p
        addiu $t0, $fp, -24
        sw    $t0, -480($fp)
        # param t90
        # call Dog::~Dog(), 1
        addiu $sp, $sp, -8
        lw    $t0, -480($fp)
        sw    $t0, 0($sp)
        jal   _ZN3DogD1Ev
        addiu $sp, $sp, 8
        # t91 = &d
        addiu $t0, $fp, -12
        sw    $t0, -484($fp)
        # param t91
        # call Dog::~Dog(), 1
        addiu $sp, $sp, -8
        lw    $t0, -484($fp)
        sw    $t0, 0($sp)
        jal   _ZN3DogD1Ev
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
