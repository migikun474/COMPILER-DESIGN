# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t27_object_semantics.c
#  Optimization : -O3 (TAC optimizations, registers, peephole)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g_keeper:  .space 4
        .align 3
g_primes:
        .byte 2, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 7, 0, 0, 0
str0:
        .byte 99, 111, 112, 121, 32, 111, 102, 32, 37, 100, 10, 0
str1:
        .byte 126, 68, 111, 103, 32, 37, 100, 10, 0
str2:
        .byte 37, 100, 10, 0
str3:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str4:
        .byte 37, 100, 32, 37, 100, 10, 0
str5:
        .byte 37, 100, 32, 37, 100, 32, 37, 46, 49, 102, 32, 37, 46, 49, 102, 10
        .byte 0
str6:
        .byte 101, 110, 100, 32, 111, 102, 32, 109, 97, 105, 110, 10, 0
        .align 3
fc0:  .word 0, 1076166656        # 10.5
        .align 3
fc1:  .word 0, 1079558144        # 99
        .align 3
fc2:  .word 0, 1075970048        # 9

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

# Counted::Counted(int)
_ZN7CountedC1Ei:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        lw    $s1, 8($fp)
        lw    $s0, 12($fp)
        # *this = x
        sw    $s0, 0($s1)
        # return
        j     _ZN7CountedC1Ei_exit
_ZN7CountedC1Ei_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Counted::Counted(const class Counted &)
_ZN7CountedC1ERKS_:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        sw    $s0, -16($fp)
        sw    $s1, -20($fp)
        sw    $s2, -24($fp)
        sw    $s3, -28($fp)
        lw    $s3, 8($fp)
        lw    $s2, 12($fp)
        # t1 = *o
        lw    $s0, 0($s2)
        # t2 = t1 int+ 100
        addiu $s1, $s0, 100
        # *this = t2
        sw    $s1, 0($s3)
        # t3 = *o
        lw    $s0, 0($s2)
        # param "copy of %d\n"
        # param t3
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN7CountedC1ERKS__exit
_ZN7CountedC1ERKS__exit:
        lw    $s0, -16($fp)
        lw    $s1, -20($fp)
        lw    $s2, -24($fp)
        lw    $s3, -28($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# take(class Counted)
_Z4take7Counted:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -8($fp)
        # t1 = c[0]
        lw    $s0, 8($fp)
        # return t1
        move  $v0, $s0
        j     _Z4take7Counted_exit
_Z4take7Counted_exit:
        lw    $s0, -8($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# give(class Counted &)
_Z4giveR7Counted:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        sw    $s0, -24($fp)
        sw    $s1, -28($fp)
        sw    $s2, -32($fp)
        sw    $s3, -36($fp)
        lw    $s3, 8($fp)
        # t2 = &t1
        addiu $s0, $fp, -4
        # t5 = *c
        lw    $s1, 0($s3)
        # t6 = t5 int+ 100
        addiu $s2, $s1, 100
        # *t2 = t6
        sw    $s2, 0($s0)
        # t7 = *c
        lw    $s0, 0($s3)
        # param "copy of %d\n"
        # param t7
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return t1
        addiu $v0, $fp, -4
        j     _Z4giveR7Counted_exit
_Z4giveR7Counted_exit:
        lw    $s0, -24($fp)
        lw    $s1, -28($fp)
        lw    $s2, -32($fp)
        lw    $s3, -36($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# fresh(int)
_Z5freshi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        lw    $s1, 8($fp)
        # t1 = &local
        addiu $s0, $fp, -4
        # *t1 = x
        sw    $s1, 0($s0)
        # return local
        addiu $v0, $fp, -4
        j     _Z5freshi_exit
_Z5freshi_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Other::Other()
_ZN5OtherC1Ev:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        lw    $s0, 8($fp)
        # *this = 7
        li    $t0, 7
        sw    $t0, 0($s0)
        # return
        j     _ZN5OtherC1Ev_exit
_ZN5OtherC1Ev_exit:
        lw    $s0, -4($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Vec::Vec(class Other)
_ZN3VecC1E5Other:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        sw    $s0, -12($fp)
        sw    $s1, -16($fp)
        sw    $s2, -20($fp)
        lw    $s2, 8($fp)
        # t1 = o[0]
        lw    $s0, 12($fp)
        # t2 = t1 int<< 1
        sll   $s1, $s0, 1
        # *this = t2
        sw    $s1, 0($s2)
        # return
        j     _ZN3VecC1E5Other_exit
_ZN3VecC1E5Other_exit:
        lw    $s0, -12($fp)
        lw    $s1, -16($fp)
        lw    $s2, -20($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Vec::Vec(int)
_ZN3VecC1Ei:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        lw    $s1, 8($fp)
        lw    $s0, 12($fp)
        # *this = k
        sw    $s0, 0($s1)
        # return
        j     _ZN3VecC1Ei_exit
_ZN3VecC1Ei_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::Dog()
_ZN3DogC1Ev:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        lw    $s0, 8($fp)
        # *this = 0
        sw    $zero, 0($s0)
        # return
        j     _ZN3DogC1Ev_exit
_ZN3DogC1Ev_exit:
        lw    $s0, -4($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::Dog(int)
_ZN3DogC1Ei:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -8
        sw    $s0, -4($fp)
        sw    $s1, -8($fp)
        lw    $s1, 8($fp)
        lw    $s0, 12($fp)
        # *this = n
        sw    $s0, 0($s1)
        # return
        j     _ZN3DogC1Ei_exit
_ZN3DogC1Ei_exit:
        lw    $s0, -4($fp)
        lw    $s1, -8($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# Dog::~Dog()
_ZN3DogD1Ev:
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
        # param "~Dog %d\n"
        # param t1
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # return
        j     _ZN3DogD1Ev_exit
_ZN3DogD1Ev_exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# sum(const int *)
_Z3sumPKi:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        sw    $s0, -40($fp)
        sw    $s1, -36($fp)
        sw    $s2, -24($fp)
        sw    $s3, -28($fp)
        sw    $s4, -32($fp)
        sw    $s5, -44($fp)
        lw    $s5, 8($fp)
        # s = 0
        li    $s1, 0
        # i = 0
        li    $s0, 0
L11_2:
        # if i int>= 4 goto 9
        li    $t1, 4
        bge   $s0, $t1, L11_9
        # t1 = i int<< 2
        sll   $s2, $s0, 2
        # t2 = r ptr+ t1
        addu  $s3, $s5, $s2
        # t3 = *t2
        lw    $s4, 0($s3)
        # s = s int+ t3
        addu  $s1, $s1, $s4
        # i = i int+ 1
        addiu $s0, $s0, 1
        # goto 2
        j     L11_2
L11_9:
        # return s
        move  $v0, $s1
        j     _Z3sumPKi_exit
_Z3sumPKi_exit:
        lw    $s0, -40($fp)
        lw    $s1, -36($fp)
        lw    $s2, -24($fp)
        lw    $s3, -28($fp)
        lw    $s4, -32($fp)
        lw    $s5, -44($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# richer(struct Account &, struct Account &)
_Z6richerR7AccountS0_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -64
        s.d   $f20, -48($fp)
        s.d   $f22, -56($fp)
        sw    $s0, -36($fp)
        sw    $s1, -60($fp)
        sw    $s2, -64($fp)
        lw    $s1, 8($fp)
        lw    $s2, 12($fp)
        # t2 = a ptr+ 8
        addiu $s0, $s1, 8
        # t3 = *t2
        l.d   $f0, 0($s0)
        mov.d $f20, $f0
        # t4 = b ptr+ 8
        addiu $s0, $s2, 8
        # t5 = *t4
        l.d   $f0, 0($s0)
        mov.d $f22, $f0
        # if t3 double>= t5 goto 6
        c.le.d $f22, $f20
        bc1t  L12_6
        # goto 8
        j     L12_8
L12_6:
        # t1 = a
        move  $s0, $s1
        # goto 9
        j     L12_9
L12_8:
        # t1 = b
        move  $s0, $s2
L12_9:
        # return t1
        move  $v0, $s0
        j     _Z6richerR7AccountS0__exit
_Z6richerR7AccountS0__exit:
        l.d   $f20, -48($fp)
        l.d   $f22, -56($fp)
        lw    $s0, -36($fp)
        lw    $s1, -60($fp)
        lw    $s2, -64($fp)
        move  $sp, $fp
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# pick(int, int &, int &)
_Z4pickiRiS_:
        addiu $sp, $sp, -8
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        sw    $s0, -8($fp)
        sw    $s1, -12($fp)
        sw    $s2, -16($fp)
        lw    $s0, 8($fp)
        lw    $s1, 12($fp)
        lw    $s2, 16($fp)
        # if which int== 0 goto 3
        beq   $s0, $zero, L13_3
        # t1 = a
        move  $s0, $s1
        # goto 4
        j     L13_4
L13_3:
        # t1 = b
        move  $s0, $s2
L13_4:
        # return t1
        move  $v0, $s0
        j     _Z4pickiRiS__exit
_Z4pickiRiS__exit:
        lw    $s0, -8($fp)
        lw    $s1, -12($fp)
        lw    $s2, -16($fp)
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
        addiu $sp, $sp, -384
        s.d   $f20, -360($fp)
        s.d   $f22, -368($fp)
        sw    $s0, -340($fp)
        sw    $s1, -344($fp)
        sw    $s2, -348($fp)
        sw    $s3, -372($fp)
        sw    $s4, -376($fp)
        sw    $s5, -380($fp)
        sw    $s6, -336($fp)
        # t1 = &keeper
        la    $s6, g_keeper
        # *t1 = 9
        li    $t0, 9
        sw    $t0, 0($s6)
        # t2 = &a
        addiu $s0, $fp, -4
        # *t2 = 1
        li    $t0, 1
        sw    $t0, 0($s0)
        # t4 = &t3
        addiu $s1, $fp, -100
        # *t4 = 101
        li    $t0, 101
        sw    $t0, 0($s1)
        # t64 = *t2
        lw    $s1, 0($s0)
        # param "copy of %d\n"
        # param t64
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t65 = t3
        addiu $a0, $fp, -228
        addiu $a1, $fp, -100
        li    $a2, 4
        jal   __memcpy
        # t66 = t65[0]
        lw    $s1, -228($fp)
        # param "%d\n"
        # param t66
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t69 = &t68
        addiu $s1, $fp, -236
        # param t69
        # param t2
        # call Counted::Counted(const class Counted &), 2
        addiu $sp, $sp, -8
        sw    $s1, 0($sp)
        sw    $s0, 4($sp)
        jal   _ZN7CountedC1ERKS_
        addiu $sp, $sp, 8
        # b = t68
        addiu $a0, $fp, -8
        addiu $a1, $fp, -236
        li    $a2, 4
        jal   __memcpy
        # t72 = &t71
        addiu $s0, $fp, -244
        # param t72
        # param 5
        # call Counted::Counted(int), 2
        addiu $sp, $sp, -8
        sw    $s0, 0($sp)
        li    $t0, 5
        sw    $t0, 4($sp)
        jal   _ZN7CountedC1Ei
        addiu $sp, $sp, 8
        # c = t71
        addiu $a0, $fp, -12
        addiu $a1, $fp, -244
        li    $a2, 4
        jal   __memcpy
        # t14 = a[0]
        lw    $s0, -4($fp)
        # t15 = b[0]
        lw    $s1, -8($fp)
        # t16 = c[0]
        lw    $s2, -12($fp)
        # param "%d %d %d\n"
        # param t14
        # param t15
        # param t16
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        sw    $s2, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # t17 = &o
        addiu $s0, $fp, -16
        # *t17 = 7
        li    $t0, 7
        sw    $t0, 0($s0)
        # t18 = &f
        addiu $s0, $fp, -20
        # t75 = o
        addiu $a0, $fp, -252
        addiu $a1, $fp, -16
        li    $a2, 4
        jal   __memcpy
        # t76 = t75[0]
        lw    $s1, -252($fp)
        # t77 = t76 int<< 1
        sll   $s2, $s1, 1
        # *t18 = t77
        sw    $s2, 0($s0)
        # t19 = &g
        addiu $s0, $fp, -24
        # *t19 = 5
        li    $t0, 5
        sw    $t0, 0($s0)
        # t20 = f[0]
        lw    $s0, -20($fp)
        # t21 = g[0]
        lw    $s1, -24($fp)
        # param "%d %d\n"
        # param t20
        # param t21
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str4
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        sw    $s1, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # x = 1
        li    $t0, 1
        sw    $t0, -28($fp)
        # y = 2
        li    $t0, 2
        sw    $t0, -32($fp)
        # if x int<= 2 goto 53
        lw    $t0, -28($fp)
        li    $t1, 2
        ble   $t0, $t1, L14_53
        # t22 = &x
        addiu $s0, $fp, -28
        # goto 54
        j     L14_54
L14_53:
        # t22 = &y
        addiu $s0, $fp, -32
L14_54:
        # *t22 = 20
        li    $t0, 20
        sw    $t0, 0($s0)
        # if x int>= y goto 58
        lw    $t0, -28($fp)
        lw    $t1, -32($fp)
        bge   $t0, $t1, L14_58
        # t25 = &x
        addiu $s0, $fp, -28
        # goto 59
        j     L14_59
L14_58:
        # t25 = &y
        addiu $s0, $fp, -32
L14_59:
        # *t25 = 10
        li    $t0, 10
        sw    $t0, 0($s0)
        # t28 = &x
        addiu $s0, $fp, -28
        # t31 = *t28
        lw    $s1, 0($s0)
        # t32 = t31 int+ 5
        addiu $s2, $s1, 5
        # *t28 = t32
        sw    $s2, 0($s0)
        # p[0] = 1
        li    $t0, 1
        sw    $t0, -56($fp)
        # p[8] = 10.5
        l.d   $f0, fc0
        s.d   $f0, -48($fp)
        # q[0] = 2
        li    $t0, 2
        sw    $t0, -72($fp)
        # q[8] = 99.0
        l.d   $f0, fc1
        s.d   $f0, -64($fp)
        # t33 = &p
        addiu $s0, $fp, -56
        # t34 = &q
        addiu $s1, $fp, -72
        # t86 = t33 ptr+ 8
        addiu $s2, $s0, 8
        # t87 = *t86
        l.d   $f0, 0($s2)
        mov.d $f20, $f0
        # t88 = t34 ptr+ 8
        addiu $s2, $s1, 8
        # t89 = *t88
        l.d   $f0, 0($s2)
        mov.d $f22, $f0
        # if t87 double>= t89 goto 76
        c.le.d $f22, $f20
        bc1t  L14_76
        # goto 78
        j     L14_78
L14_76:
        # t90 = t33
        move  $s2, $s0
        # goto 79
        j     L14_79
L14_78:
        # t90 = t34
        move  $s2, $s1
L14_79:
        # t36 = t90 ptr+ 8
        addiu $s0, $s2, 8
        # t37 = *t36
        l.d   $f0, 0($s0)
        mov.d $f20, $f0
        # t38 = t37 double- 9.0
        l.d   $f2, fc2
        sub.d $f22, $f20, $f2
        # *t36 = t38
        mov.d $f0, $f22
        s.d   $f0, 0($s0)
        # t40 = p[8]
        l.d   $f0, -48($fp)
        mov.d $f20, $f0
        # t41 = q[8]
        l.d   $f0, -64($fp)
        mov.d $f22, $f0
        # param "%d %d %.1f %.1f\n"
        # param x
        # param y
        # param t40
        # param t41
        # call printf, 5
        addiu $sp, $sp, -32
        la    $t0, str5
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        lw    $t0, -32($fp)
        sw    $t0, 8($sp)
        mov.d $f0, $f20
        s.d   $f0, 16($sp)
        mov.d $f0, $f22
        s.d   $f0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # t91 = &primes
        la    $s5, g_primes
        # t92 = 0
        li    $s1, 0
        # t93 = 0
        li    $s0, 0
L14_94:
        # if t93 int>= 4 goto 101
        li    $t1, 4
        bge   $s0, $t1, L14_101
        # t94 = t93 int<< 2
        sll   $s2, $s0, 2
        # t95 = t91 ptr+ t94
        addu  $s3, $s5, $s2
        # t96 = *t95
        lw    $s4, 0($s3)
        # t92 = t92 int+ t96
        addu  $s1, $s1, $s4
        # t93 = t93 int+ 1
        addiu $s0, $s0, 1
        # goto 94
        j     L14_94
L14_101:
        # param "%d\n"
        # param t92
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        sw    $s1, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t44 = &pack
        addiu $s3, $fp, -84
        # *t44 = 0
        sw    $zero, 0($s3)
        # t45 = t44 ptr+ 4
        addiu $s4, $s3, 4
        # *t45 = 0
        sw    $zero, 0($s4)
        # t46 = t44 ptr+ 8
        addiu $s5, $s3, 8
        # *t46 = 0
        sw    $zero, 0($s5)
        # i = 0
        li    $s0, 0
L14_111:
        # if i int>= 3 goto 117
        li    $t1, 3
        bge   $s0, $t1, L14_117
        # t47 = i int<< 2
        sll   $s2, $s0, 2
        # t48 = i int+ 1
        addiu $s1, $s0, 1
        # pack[t47] = t48
        addiu $t8, $fp, -84
        addu  $t8, $t8, $s2
        sw    $s1, 0($t8)
        # i = t48
        move  $s0, $s1
        # goto 111
        j     L14_111
L14_117:
        # t101 = *t46
        lw    $s0, 0($s5)
        # param "~Dog %d\n"
        # param t101
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t103 = *t45
        lw    $s0, 0($s4)
        # param "~Dog %d\n"
        # param t103
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t105 = *t44
        lw    $s0, 0($s3)
        # param "~Dog %d\n"
        # param t105
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        sw    $s0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # param "end of main\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str6
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t107 = *t1
        lw    $s0, 0($s6)
        # param "~Dog %d\n"
        # param t107
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
        l.d   $f20, -360($fp)
        l.d   $f22, -368($fp)
        lw    $s0, -340($fp)
        lw    $s1, -344($fp)
        lw    $s2, -348($fp)
        lw    $s3, -372($fp)
        lw    $s4, -376($fp)
        lw    $s5, -380($fp)
        lw    $s6, -336($fp)
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
