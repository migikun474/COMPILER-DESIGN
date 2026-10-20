# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t22_data_structures.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
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

# prepend(struct Node *, int)
_Z7prependP4Nodei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -16
        # param 8
        # t1 = call malloc, 1
        addiu $sp, $sp, -8
        li    $t0, 8
        sw    $t0, 0($sp)
        jal   __malloc
        addiu $sp, $sp, 8
        sw    $v0, -8($fp)
        # n = t1
        lw    $t0, -8($fp)
        sw    $t0, -4($fp)
        # *n = v
        lw    $t8, -4($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t2 = n ptr+ 4
        lw    $t0, -4($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # *t2 = head
        lw    $t8, -12($fp)
        lw    $t0, 8($fp)
        sw    $t0, 0($t8)
        # return n
        lw    $v0, -4($fp)
        j     _Z7prependP4Nodei_exit
_Z7prependP4Nodei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# reverse(struct Node *)
_Z7reverseP4Node:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # prev = 0
        li    $t0, 0
        sw    $t0, -4($fp)
L1_1:
        # if head ptr!= 0 goto 3
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L1_3
        # goto 11
        j     L1_11
L1_3:
        # t1 = head ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = *t1
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # next = t2
        lw    $t0, -16($fp)
        sw    $t0, -8($fp)
        # t3 = head ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # *t3 = prev
        lw    $t8, -20($fp)
        lw    $t0, -4($fp)
        sw    $t0, 0($t8)
        # prev = head
        lw    $t0, 8($fp)
        sw    $t0, -4($fp)
        # head = next
        lw    $t0, -8($fp)
        sw    $t0, 8($fp)
        # goto 1
        j     L1_1
L1_11:
        # return prev
        lw    $v0, -4($fp)
        j     _Z7reverseP4Node_exit
_Z7reverseP4Node_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# removeValue(struct Node **, int)
_Z11removeValuePP4Nodei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
L2_0:
        # t1 = *link
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # if t1 ptr!= 0 goto 3
        lw    $t0, -8($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_3
        # goto 19
        j     L2_19
L2_3:
        # t2 = *link
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # t3 = *t2
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # if t3 int== v goto 7
        lw    $t0, -16($fp)
        lw    $t1, 12($fp)
        beq   $t0, $t1, L2_7
        # goto 15
        j     L2_15
L2_7:
        # t4 = *link
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # dead = t4
        lw    $t0, -20($fp)
        sw    $t0, -4($fp)
        # t5 = dead ptr+ 4
        lw    $t0, -4($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t6 = *t5
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # *link = t6
        lw    $t8, 8($fp)
        lw    $t0, -28($fp)
        sw    $t0, 0($t8)
        # param dead
        # call free, 1
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        jal   __free
        addiu $sp, $sp, 8
        # goto 0
        j     L2_0
L2_15:
        # t7 = *link
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -32($fp)
        # t8 = t7 ptr+ 4
        lw    $t0, -32($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # link = t8
        lw    $t0, -36($fp)
        sw    $t0, 8($fp)
        # goto 0
        j     L2_0
L2_19:
        # return
        j     _Z11removeValuePP4Nodei_exit
_Z11removeValuePP4Nodei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# insert(struct Tree *, int)
_Z6insertP4Treei:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -48
        # if t ptr!= 0 goto 11
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L3_11
        # goto 2
        j     L3_2
L3_2:
        # param 12
        # t1 = call malloc, 1
        addiu $sp, $sp, -8
        li    $t0, 12
        sw    $t0, 0($sp)
        jal   __malloc
        addiu $sp, $sp, 8
        sw    $v0, -4($fp)
        # t = t1
        lw    $t0, -4($fp)
        sw    $t0, 8($fp)
        # *t = key
        lw    $t8, 8($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # t2 = t ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -8($fp)
        # *t2 = 0
        lw    $t8, -8($fp)
        li    $t0, 0
        sw    $t0, 0($t8)
        # t3 = t ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # *t3 = 0
        lw    $t8, -12($fp)
        li    $t0, 0
        sw    $t0, 0($t8)
        # goto 29
        j     L3_29
L3_11:
        # t4 = *t
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # if key int< t4 goto 14
        lw    $t0, 12($fp)
        lw    $t1, -16($fp)
        blt   $t0, $t1, L3_14
        # goto 22
        j     L3_22
L3_14:
        # t5 = t ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t6 = *t5
        lw    $t8, -20($fp)
        lw    $t0, 0($t8)
        sw    $t0, -24($fp)
        # param t6
        # param key
        # t7 = call insert(struct Tree *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -24($fp)
        sw    $t0, 0($sp)
        lw    $t0, 12($fp)
        sw    $t0, 4($sp)
        jal   _Z6insertP4Treei
        addiu $sp, $sp, 8
        sw    $v0, -28($fp)
        # t8 = t ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -32($fp)
        # *t8 = t7
        lw    $t8, -32($fp)
        lw    $t0, -28($fp)
        sw    $t0, 0($t8)
        # goto 29
        j     L3_29
L3_22:
        # t9 = t ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -36($fp)
        # t10 = *t9
        lw    $t8, -36($fp)
        lw    $t0, 0($t8)
        sw    $t0, -40($fp)
        # param t10
        # param key
        # t11 = call insert(struct Tree *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -40($fp)
        sw    $t0, 0($sp)
        lw    $t0, 12($fp)
        sw    $t0, 4($sp)
        jal   _Z6insertP4Treei
        addiu $sp, $sp, 8
        sw    $v0, -44($fp)
        # t12 = t ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -48($fp)
        # *t12 = t11
        lw    $t8, -48($fp)
        lw    $t0, -44($fp)
        sw    $t0, 0($t8)
L3_29:
        # return t
        lw    $v0, 8($fp)
        j     _Z6insertP4Treei_exit
_Z6insertP4Treei_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# inorder(struct Tree *)
_Z7inorderP4Tree:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # if t ptr!= 0 goto 3
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L4_3
        # goto 2
        j     L4_2
L4_2:
        # return
        j     _Z7inorderP4Tree_exit
L4_3:
        # t1 = t ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # param t2
        # call inorder(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -8($fp)
        sw    $t0, 0($sp)
        jal   _Z7inorderP4Tree
        addiu $sp, $sp, 8
        # t3 = *t
        lw    $t8, 8($fp)
        lw    $t0, 0($t8)
        sw    $t0, -12($fp)
        # param "%d "
        # param t3
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -12($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t4 = t ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # t5 = *t4
        lw    $t8, -16($fp)
        lw    $t0, 0($t8)
        sw    $t0, -20($fp)
        # param t5
        # call inorder(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -20($fp)
        sw    $t0, 0($sp)
        jal   _Z7inorderP4Tree
        addiu $sp, $sp, 8
        # return
        j     _Z7inorderP4Tree_exit
_Z7inorderP4Tree_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# height(struct Tree *)
_Z6heightP4Tree:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -40
        # if t ptr!= 0 goto 3
        lw    $t0, 8($fp)
        li    $t1, 0
        bne   $t0, $t1, L5_3
        # goto 2
        j     L5_2
L5_2:
        # return 0
        li    $v0, 0
        j     _Z6heightP4Tree_exit
L5_3:
        # t1 = t ptr+ 4
        lw    $t0, 8($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t2 = *t1
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -16($fp)
        # param t2
        # t3 = call height(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        jal   _Z6heightP4Tree
        addiu $sp, $sp, 8
        sw    $v0, -20($fp)
        # l = t3
        lw    $t0, -20($fp)
        sw    $t0, -4($fp)
        # t4 = t ptr+ 8
        lw    $t0, 8($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t5 = *t4
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # param t5
        # t6 = call height(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -28($fp)
        sw    $t0, 0($sp)
        jal   _Z6heightP4Tree
        addiu $sp, $sp, 8
        sw    $v0, -32($fp)
        # r = t6
        lw    $t0, -32($fp)
        sw    $t0, -8($fp)
        # if l int> r goto 15
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        bgt   $t0, $t1, L5_15
        # goto 17
        j     L5_17
L5_15:
        # t7 = l
        lw    $t0, -4($fp)
        sw    $t0, -36($fp)
        # goto 18
        j     L5_18
L5_17:
        # t7 = r
        lw    $t0, -8($fp)
        sw    $t0, -36($fp)
L5_18:
        # t8 = 1 int+ t7
        li    $t0, 1
        lw    $t1, -36($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -40($fp)
        # return t8
        lw    $v0, -40($fp)
        j     _Z6heightP4Tree_exit
_Z6heightP4Tree_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# push(Stack *, int)
_Z4pushP5Stacki:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -24
        # t1 = s ptr+ 32
        lw    $t0, 8($fp)
        li    $t1, 32
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = t2 int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = s ptr+ 32
        lw    $t0, 8($fp)
        li    $t1, 32
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # *t4 = t3
        lw    $t8, -16($fp)
        lw    $t0, -12($fp)
        sw    $t0, 0($t8)
        # t5 = t2 int* 4
        lw    $t0, -8($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t6 = s ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # *t6 = v
        lw    $t8, -24($fp)
        lw    $t0, 12($fp)
        sw    $t0, 0($t8)
        # return
        j     _Z4pushP5Stacki_exit
_Z4pushP5Stacki_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# pop(Stack *)
_Z3popP5Stack:
        addiu $sp, $sp, -8
        sw    $ra, 4($sp)
        sw    $fp, 0($sp)
        move  $fp, $sp
        addiu $sp, $sp, -32
        # t1 = s ptr+ 32
        lw    $t0, 8($fp)
        li    $t1, 32
        addu  $t0, $t0, $t1
        sw    $t0, -4($fp)
        # t2 = *t1
        lw    $t8, -4($fp)
        lw    $t0, 0($t8)
        sw    $t0, -8($fp)
        # t3 = t2 int- 1
        lw    $t0, -8($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -12($fp)
        # t4 = s ptr+ 32
        lw    $t0, 8($fp)
        li    $t1, 32
        addu  $t0, $t0, $t1
        sw    $t0, -16($fp)
        # *t4 = t3
        lw    $t8, -16($fp)
        lw    $t0, -12($fp)
        sw    $t0, 0($t8)
        # t5 = t3 int* 4
        lw    $t0, -12($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -20($fp)
        # t6 = s ptr+ t5
        lw    $t0, 8($fp)
        lw    $t1, -20($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -24($fp)
        # t7 = *t6
        lw    $t8, -24($fp)
        lw    $t0, 0($t8)
        sw    $t0, -28($fp)
        # return t7
        lw    $v0, -28($fp)
        j     _Z3popP5Stack_exit
_Z3popP5Stack_exit:
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
        # list = 0
        li    $t0, 0
        sw    $t0, -4($fp)
        # i.20 = 1
        li    $t0, 1
        sw    $t0, -8($fp)
L8_2:
        # if i.20 int<= 6 goto 4
        lw    $t0, -8($fp)
        li    $t1, 6
        ble   $t0, $t1, L8_4
        # goto 13
        j     L8_13
L8_4:
        # t1 = i.20 int* i.20
        lw    $t0, -8($fp)
        lw    $t1, -8($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -160($fp)
        # t2 = t1 int% 7
        lw    $t0, -160($fp)
        li    $t1, 7
        div   $t0, $t1
        mfhi  $t0
        sw    $t0, -164($fp)
        # param list
        # param t2
        # t3 = call prepend(struct Node *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        lw    $t0, -164($fp)
        sw    $t0, 4($sp)
        jal   _Z7prependP4Nodei
        addiu $sp, $sp, 8
        sw    $v0, -168($fp)
        # list = t3
        lw    $t0, -168($fp)
        sw    $t0, -4($fp)
        # t4 = i.20 int+ 1
        lw    $t0, -8($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -172($fp)
        # i.20 = t4
        lw    $t0, -172($fp)
        sw    $t0, -8($fp)
        # goto 2
        j     L8_2
L8_13:
        # param list
        # t5 = call reverse(struct Node *), 1
        addiu $sp, $sp, -8
        lw    $t0, -4($fp)
        sw    $t0, 0($sp)
        jal   _Z7reverseP4Node
        addiu $sp, $sp, 8
        sw    $v0, -176($fp)
        # list = t5
        lw    $t0, -176($fp)
        sw    $t0, -4($fp)
        # t6 = &list
        addiu $t0, $fp, -4
        sw    $t0, -180($fp)
        # param t6
        # param 2
        # call removeValue(struct Node **, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -180($fp)
        sw    $t0, 0($sp)
        li    $t0, 2
        sw    $t0, 4($sp)
        jal   _Z11removeValuePP4Nodei
        addiu $sp, $sp, 8
        # p = list
        lw    $t0, -4($fp)
        sw    $t0, -12($fp)
L8_21:
        # if p ptr!= 0 goto 23
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L8_23
        # goto 31
        j     L8_31
L8_23:
        # t7 = *p
        lw    $t8, -12($fp)
        lw    $t0, 0($t8)
        sw    $t0, -184($fp)
        # param "%d "
        # param t7
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -184($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # t8 = p ptr+ 4
        lw    $t0, -12($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -188($fp)
        # t9 = *t8
        lw    $t8, -188($fp)
        lw    $t0, 0($t8)
        sw    $t0, -192($fp)
        # p = t9
        lw    $t0, -192($fp)
        sw    $t0, -12($fp)
        # goto 21
        j     L8_21
L8_31:
        # param "\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str1
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # root = 0
        li    $t0, 0
        sw    $t0, -16($fp)
        # keys[0] = 50
        addiu $t8, $fp, -44
        li    $t9, 0
        addu  $t8, $t8, $t9
        li    $t0, 50
        sw    $t0, 0($t8)
        # keys[4] = 30
        addiu $t8, $fp, -44
        li    $t9, 4
        addu  $t8, $t8, $t9
        li    $t0, 30
        sw    $t0, 0($t8)
        # keys[8] = 70
        addiu $t8, $fp, -44
        li    $t9, 8
        addu  $t8, $t8, $t9
        li    $t0, 70
        sw    $t0, 0($t8)
        # keys[12] = 20
        addiu $t8, $fp, -44
        li    $t9, 12
        addu  $t8, $t8, $t9
        li    $t0, 20
        sw    $t0, 0($t8)
        # keys[16] = 40
        addiu $t8, $fp, -44
        li    $t9, 16
        addu  $t8, $t8, $t9
        li    $t0, 40
        sw    $t0, 0($t8)
        # keys[20] = 60
        addiu $t8, $fp, -44
        li    $t9, 20
        addu  $t8, $t8, $t9
        li    $t0, 60
        sw    $t0, 0($t8)
        # keys[24] = 80
        addiu $t8, $fp, -44
        li    $t9, 24
        addu  $t8, $t8, $t9
        li    $t0, 80
        sw    $t0, 0($t8)
        # i.24 = 0
        li    $t0, 0
        sw    $t0, -48($fp)
L8_42:
        # if i.24 int< 7 goto 44
        lw    $t0, -48($fp)
        li    $t1, 7
        blt   $t0, $t1, L8_44
        # goto 53
        j     L8_53
L8_44:
        # t10 = i.24 int* 4
        lw    $t0, -48($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -196($fp)
        # t11 = keys[t10]
        addiu $t8, $fp, -44
        lw    $t9, -196($fp)
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -200($fp)
        # param root
        # param t11
        # t12 = call insert(struct Tree *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        lw    $t0, -200($fp)
        sw    $t0, 4($sp)
        jal   _Z6insertP4Treei
        addiu $sp, $sp, 8
        sw    $v0, -204($fp)
        # root = t12
        lw    $t0, -204($fp)
        sw    $t0, -16($fp)
        # t13 = i.24 int+ 1
        lw    $t0, -48($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -208($fp)
        # i.24 = t13
        lw    $t0, -208($fp)
        sw    $t0, -48($fp)
        # goto 42
        j     L8_42
L8_53:
        # param root
        # param 10
        # t14 = call insert(struct Tree *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        li    $t0, 10
        sw    $t0, 4($sp)
        jal   _Z6insertP4Treei
        addiu $sp, $sp, 8
        sw    $v0, -212($fp)
        # root = t14
        lw    $t0, -212($fp)
        sw    $t0, -16($fp)
        # param root
        # call inorder(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        jal   _Z7inorderP4Tree
        addiu $sp, $sp, 8
        # param root
        # t15 = call height(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        jal   _Z6heightP4Tree
        addiu $sp, $sp, 8
        sw    $v0, -216($fp)
        # t16 = root ptr+ 4
        lw    $t0, -16($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -220($fp)
        # t17 = *t16
        lw    $t8, -220($fp)
        lw    $t0, 0($t8)
        sw    $t0, -224($fp)
        # t18 = t17 ptr+ 4
        lw    $t0, -224($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -228($fp)
        # t19 = *t18
        lw    $t8, -228($fp)
        lw    $t0, 0($t8)
        sw    $t0, -232($fp)
        # t20 = t19 ptr+ 4
        lw    $t0, -232($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -236($fp)
        # t21 = *t20
        lw    $t8, -236($fp)
        lw    $t0, 0($t8)
        sw    $t0, -240($fp)
        # t22 = *t21
        lw    $t8, -240($fp)
        lw    $t0, 0($t8)
        sw    $t0, -244($fp)
        # t23 = root ptr+ 8
        lw    $t0, -16($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -248($fp)
        # t24 = *t23
        lw    $t8, -248($fp)
        lw    $t0, 0($t8)
        sw    $t0, -252($fp)
        # t25 = t24 ptr+ 4
        lw    $t0, -252($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -256($fp)
        # t26 = *t25
        lw    $t8, -256($fp)
        lw    $t0, 0($t8)
        sw    $t0, -260($fp)
        # t27 = *t26
        lw    $t8, -260($fp)
        lw    $t0, 0($t8)
        sw    $t0, -264($fp)
        # param "\n%d %d %d\n"
        # param t15
        # param t22
        # param t27
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str2
        sw    $t0, 0($sp)
        lw    $t0, -216($fp)
        sw    $t0, 4($sp)
        lw    $t0, -244($fp)
        sw    $t0, 8($sp)
        lw    $t0, -264($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # s[32] = 0
        addiu $t8, $fp, -84
        li    $t9, 32
        addu  $t8, $t8, $t9
        li    $t0, 0
        sw    $t0, 0($t8)
        # i.26 = 0
        li    $t0, 0
        sw    $t0, -88($fp)
L8_80:
        # if i.26 int< 5 goto 82
        lw    $t0, -88($fp)
        li    $t1, 5
        blt   $t0, $t1, L8_82
        # goto 90
        j     L8_90
L8_82:
        # t28 = &s
        addiu $t0, $fp, -84
        sw    $t0, -268($fp)
        # t29 = i.26 int* 3
        lw    $t0, -88($fp)
        li    $t1, 3
        mul   $t0, $t0, $t1
        sw    $t0, -272($fp)
        # param t28
        # param t29
        # call push(Stack *, int), 2
        addiu $sp, $sp, -8
        lw    $t0, -268($fp)
        sw    $t0, 0($sp)
        lw    $t0, -272($fp)
        sw    $t0, 4($sp)
        jal   _Z4pushP5Stacki
        addiu $sp, $sp, 8
        # t30 = i.26 int+ 1
        lw    $t0, -88($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -276($fp)
        # i.26 = t30
        lw    $t0, -276($fp)
        sw    $t0, -88($fp)
        # goto 80
        j     L8_80
L8_90:
        # t31 = &s
        addiu $t0, $fp, -84
        sw    $t0, -280($fp)
        # param t31
        # t32 = call pop(Stack *), 1
        addiu $sp, $sp, -8
        lw    $t0, -280($fp)
        sw    $t0, 0($sp)
        jal   _Z3popP5Stack
        addiu $sp, $sp, 8
        sw    $v0, -284($fp)
        # a = t32
        lw    $t0, -284($fp)
        sw    $t0, -92($fp)
        # t33 = &s
        addiu $t0, $fp, -84
        sw    $t0, -288($fp)
        # param t33
        # t34 = call pop(Stack *), 1
        addiu $sp, $sp, -8
        lw    $t0, -288($fp)
        sw    $t0, 0($sp)
        jal   _Z3popP5Stack
        addiu $sp, $sp, 8
        sw    $v0, -292($fp)
        # b = t34
        lw    $t0, -292($fp)
        sw    $t0, -96($fp)
        # t35 = s[32]
        addiu $t8, $fp, -84
        li    $t9, 32
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -296($fp)
        # param "%d %d %d\n"
        # param a
        # param b
        # param t35
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -92($fp)
        sw    $t0, 4($sp)
        lw    $t0, -96($fp)
        sw    $t0, 8($sp)
        lw    $t0, -296($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # rows = 3
        li    $t0, 3
        sw    $t0, -100($fp)
        # cols = 4
        li    $t0, 4
        sw    $t0, -104($fp)
        # t36 = rows uint* 4
        lw    $t0, -100($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -300($fp)
        # param t36
        # t37 = call malloc, 1
        addiu $sp, $sp, -8
        lw    $t0, -300($fp)
        sw    $t0, 0($sp)
        jal   __malloc
        addiu $sp, $sp, 8
        sw    $v0, -304($fp)
        # table = t37
        lw    $t0, -304($fp)
        sw    $t0, -108($fp)
        # r.32 = 0
        li    $t0, 0
        sw    $t0, -112($fp)
L8_111:
        # if r.32 int< rows goto 113
        lw    $t0, -112($fp)
        lw    $t1, -100($fp)
        blt   $t0, $t1, L8_113
        # goto 136
        j     L8_136
L8_113:
        # t38 = r.32 int* 4
        lw    $t0, -112($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -308($fp)
        # t39 = table ptr+ t38
        lw    $t0, -108($fp)
        lw    $t1, -308($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -312($fp)
        # t40 = cols uint* 4
        lw    $t0, -104($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -316($fp)
        # param t40
        # t41 = call malloc, 1
        addiu $sp, $sp, -8
        lw    $t0, -316($fp)
        sw    $t0, 0($sp)
        jal   __malloc
        addiu $sp, $sp, 8
        sw    $v0, -320($fp)
        # *t39 = t41
        lw    $t8, -312($fp)
        lw    $t0, -320($fp)
        sw    $t0, 0($t8)
        # c = 0
        li    $t0, 0
        sw    $t0, -116($fp)
L8_120:
        # if c int< cols goto 122
        lw    $t0, -116($fp)
        lw    $t1, -104($fp)
        blt   $t0, $t1, L8_122
        # goto 133
        j     L8_133
L8_122:
        # t42 = r.32 int* 4
        lw    $t0, -112($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -324($fp)
        # t43 = table ptr+ t42
        lw    $t0, -108($fp)
        lw    $t1, -324($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -328($fp)
        # t44 = *t43
        lw    $t8, -328($fp)
        lw    $t0, 0($t8)
        sw    $t0, -332($fp)
        # t45 = c int* 4
        lw    $t0, -116($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -336($fp)
        # t46 = t44 ptr+ t45
        lw    $t0, -332($fp)
        lw    $t1, -336($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -340($fp)
        # t47 = r.32 int* 10
        lw    $t0, -112($fp)
        li    $t1, 10
        mul   $t0, $t0, $t1
        sw    $t0, -344($fp)
        # t48 = t47 int+ c
        lw    $t0, -344($fp)
        lw    $t1, -116($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -348($fp)
        # *t46 = t48
        lw    $t8, -340($fp)
        lw    $t0, -348($fp)
        sw    $t0, 0($t8)
        # t49 = c int+ 1
        lw    $t0, -116($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -352($fp)
        # c = t49
        lw    $t0, -352($fp)
        sw    $t0, -116($fp)
        # goto 120
        j     L8_120
L8_133:
        # t50 = r.32 int+ 1
        lw    $t0, -112($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -356($fp)
        # r.32 = t50
        lw    $t0, -356($fp)
        sw    $t0, -112($fp)
        # goto 111
        j     L8_111
L8_136:
        # diagonal = 0
        li    $t0, 0
        sw    $t0, -120($fp)
        # r.35 = 0
        li    $t0, 0
        sw    $t0, -124($fp)
L8_138:
        # if r.35 int< rows goto 140
        lw    $t0, -124($fp)
        lw    $t1, -100($fp)
        blt   $t0, $t1, L8_140
        # goto 151
        j     L8_151
L8_140:
        # t51 = r.35 int* 4
        lw    $t0, -124($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -360($fp)
        # t52 = table ptr+ t51
        lw    $t0, -108($fp)
        lw    $t1, -360($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -364($fp)
        # t53 = *t52
        lw    $t8, -364($fp)
        lw    $t0, 0($t8)
        sw    $t0, -368($fp)
        # t54 = r.35 int* 4
        lw    $t0, -124($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -372($fp)
        # t55 = t53 ptr+ t54
        lw    $t0, -368($fp)
        lw    $t1, -372($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -376($fp)
        # t56 = *t55
        lw    $t8, -376($fp)
        lw    $t0, 0($t8)
        sw    $t0, -380($fp)
        # t57 = diagonal int+ t56
        lw    $t0, -120($fp)
        lw    $t1, -380($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -384($fp)
        # diagonal = t57
        lw    $t0, -384($fp)
        sw    $t0, -120($fp)
        # t58 = r.35 int+ 1
        lw    $t0, -124($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -388($fp)
        # r.35 = t58
        lw    $t0, -388($fp)
        sw    $t0, -124($fp)
        # goto 138
        j     L8_138
L8_151:
        # t59 = rows int- 1
        lw    $t0, -100($fp)
        li    $t1, 1
        subu  $t0, $t0, $t1
        sw    $t0, -392($fp)
        # t60 = t59 int* 4
        lw    $t0, -392($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -396($fp)
        # t61 = table ptr+ t60
        lw    $t0, -108($fp)
        lw    $t1, -396($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -400($fp)
        # t62 = *t61
        lw    $t8, -400($fp)
        lw    $t0, 0($t8)
        sw    $t0, -404($fp)
        # t63 = cols int* 4
        lw    $t0, -104($fp)
        li    $t1, 4
        mul   $t0, $t0, $t1
        sw    $t0, -408($fp)
        # t64 = t62 ptr+ t63
        lw    $t0, -404($fp)
        lw    $t1, -408($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -412($fp)
        # t65 = t64 ptr- 4
        lw    $t0, -412($fp)
        li    $t1, 4
        subu  $t0, $t0, $t1
        sw    $t0, -416($fp)
        # last = t65
        lw    $t0, -416($fp)
        sw    $t0, -128($fp)
        # t66 = *last
        lw    $t8, -128($fp)
        lw    $t0, 0($t8)
        sw    $t0, -420($fp)
        # t67 = table ptr+ 4
        lw    $t0, -108($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -424($fp)
        # t68 = *t67
        lw    $t8, -424($fp)
        lw    $t0, 0($t8)
        sw    $t0, -428($fp)
        # t69 = t68 ptr+ 8
        lw    $t0, -428($fp)
        li    $t1, 8
        addu  $t0, $t0, $t1
        sw    $t0, -432($fp)
        # t70 = *t69
        lw    $t8, -432($fp)
        lw    $t0, 0($t8)
        sw    $t0, -436($fp)
        # param "%d %d %d\n"
        # param diagonal
        # param t66
        # param t70
        # call printf, 4
        addiu $sp, $sp, -16
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, -120($fp)
        sw    $t0, 4($sp)
        lw    $t0, -420($fp)
        sw    $t0, 8($sp)
        lw    $t0, -436($fp)
        sw    $t0, 12($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # v1 = 1
        li    $t0, 1
        sw    $t0, -132($fp)
        # v2 = 2
        li    $t0, 2
        sw    $t0, -136($fp)
        # v3 = 3
        li    $t0, 3
        sw    $t0, -140($fp)
        # t71 = &v3
        addiu $t0, $fp, -140
        sw    $t0, -440($fp)
        # t72 = &v1
        addiu $t0, $fp, -132
        sw    $t0, -444($fp)
        # t73 = &v2
        addiu $t0, $fp, -136
        sw    $t0, -448($fp)
        # ptrs[0] = t71
        addiu $t8, $fp, -152
        li    $t9, 0
        addu  $t8, $t8, $t9
        lw    $t0, -440($fp)
        sw    $t0, 0($t8)
        # ptrs[4] = t72
        addiu $t8, $fp, -152
        li    $t9, 4
        addu  $t8, $t8, $t9
        lw    $t0, -444($fp)
        sw    $t0, 0($t8)
        # ptrs[8] = t73
        addiu $t8, $fp, -152
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, -448($fp)
        sw    $t0, 0($t8)
        # t74 = &ptrs
        addiu $t0, $fp, -152
        sw    $t0, -452($fp)
        # pp = t74
        lw    $t0, -452($fp)
        sw    $t0, -156($fp)
        # t75 = *pp
        lw    $t8, -156($fp)
        lw    $t0, 0($t8)
        sw    $t0, -456($fp)
        # *t75 = 30
        lw    $t8, -456($fp)
        li    $t0, 30
        sw    $t0, 0($t8)
        # t76 = ptrs[8]
        addiu $t8, $fp, -152
        li    $t9, 8
        addu  $t8, $t8, $t9
        lw    $t0, 0($t8)
        sw    $t0, -460($fp)
        # t77 = *t76
        lw    $t8, -460($fp)
        lw    $t0, 0($t8)
        sw    $t0, -464($fp)
        # t78 = t77 int+ 5
        lw    $t0, -464($fp)
        li    $t1, 5
        addu  $t0, $t0, $t1
        sw    $t0, -468($fp)
        # *t76 = t78
        lw    $t8, -460($fp)
        lw    $t0, -468($fp)
        sw    $t0, 0($t8)
        # t79 = pp ptr+ 4
        lw    $t0, -156($fp)
        li    $t1, 4
        addu  $t0, $t0, $t1
        sw    $t0, -472($fp)
        # t80 = *t79
        lw    $t8, -472($fp)
        lw    $t0, 0($t8)
        sw    $t0, -476($fp)
        # t81 = *t80
        lw    $t8, -476($fp)
        lw    $t0, 0($t8)
        sw    $t0, -480($fp)
        # param "%d %d %d %d\n"
        # param v1
        # param v2
        # param v3
        # param t81
        # call printf, 5
        addiu $sp, $sp, -24
        la    $t0, str4
        sw    $t0, 0($sp)
        lw    $t0, -132($fp)
        sw    $t0, 4($sp)
        lw    $t0, -136($fp)
        sw    $t0, 8($sp)
        lw    $t0, -140($fp)
        sw    $t0, 12($sp)
        lw    $t0, -480($fp)
        sw    $t0, 16($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # param root
        # t82 = call height(struct Tree *), 1
        addiu $sp, $sp, -8
        lw    $t0, -16($fp)
        sw    $t0, 0($sp)
        jal   _Z6heightP4Tree
        addiu $sp, $sp, 8
        sw    $v0, -484($fp)
        # return t82
        lw    $v0, -484($fp)
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
