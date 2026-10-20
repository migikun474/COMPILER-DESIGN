# =========================================================================
#  MIPS ASSEMBLY  --  run with: spim -file <this file>
# =========================================================================
#  Source file  : ../phase3-ir/test/t03_booleans.c
#  Optimization : no optimization (every value in the stack frame)
# =========================================================================

# generated for SPIM: `spim -file <this file> [arguments]`

        .data
        .align 3
g_calls:
        .byte 0, 0, 0, 0
str0:
        .byte 37, 100, 10, 0
str1:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37
        .byte 100, 10, 0
str2:
        .byte 110, 111, 10, 0
str3:
        .byte 99, 97, 108, 108, 115, 32, 97, 102, 116, 101, 114, 32, 38, 38, 58, 32
        .byte 37, 100, 10, 0
str4:
        .byte 111, 114, 32, 116, 97, 107, 101, 110, 10, 0
str5:
        .byte 99, 97, 108, 108, 115, 32, 97, 102, 116, 101, 114, 32, 124, 124, 58, 32
        .byte 37, 100, 10, 0
str6:
        .byte 37, 100, 32, 37, 100, 10, 0
str7:
        .byte 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 32, 37, 100, 10, 0
str8:
        .byte 100, 111, 117, 98, 108, 101, 32, 105, 115, 32, 116, 114, 117, 101, 10, 0
str9:
        .byte 110, 117, 108, 108, 32, 112, 111, 105, 110, 116, 101, 114, 32, 105, 115, 32
        .byte 102, 97, 108, 115, 101, 10, 0
        .align 3
fc0:  .word 0, 1071644672        # 0.5
        .align 3
fc1:  .word 0, 0        # 0

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

# yes()
_Z3yesv:
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
        # return 1
        li    $v0, 1
        j     _Z3yesv_exit
_Z3yesv_exit:
        move  $sp, $fp
        lw    $ra, 4($sp)
        lw    $fp, 0($sp)
        addiu $sp, $sp, 8
        jr    $ra

# no()
_Z2nov:
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
        # return 0
        li    $v0, 0
        j     _Z2nov_exit
_Z2nov_exit:
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
        addiu $sp, $sp, -208
        # a = 1
        li    $t0, 1
        sw    $t0, -4($fp)
        # b = 2
        li    $t0, 2
        sw    $t0, -8($fp)
        # c = 3
        li    $t0, 3
        sw    $t0, -12($fp)
        # d = 4
        li    $t0, 4
        sw    $t0, -16($fp)
        # e = 5
        li    $t0, 5
        sw    $t0, -20($fp)
        # f = 6
        li    $t0, 6
        sw    $t0, -24($fp)
        # if a int< b goto 14
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        blt   $t0, $t1, L2_14
        # goto 8
        j     L2_8
L2_8:
        # if c int< d goto 10
        lw    $t0, -12($fp)
        lw    $t1, -16($fp)
        blt   $t0, $t1, L2_10
        # goto 12
        j     L2_12
L2_10:
        # if e int< f goto 14
        lw    $t0, -20($fp)
        lw    $t1, -24($fp)
        blt   $t0, $t1, L2_14
        # goto 12
        j     L2_12
L2_12:
        # t1 = 0
        li    $t0, 0
        sw    $t0, -64($fp)
        # goto 15
        j     L2_15
L2_14:
        # t1 = 1
        li    $t0, 1
        sw    $t0, -64($fp)
L2_15:
        # r = t1
        lw    $t0, -64($fp)
        sw    $t0, -28($fp)
        # param "%d\n"
        # param r
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if a int> b goto 22
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        bgt   $t0, $t1, L2_22
        # t2 = 0
        li    $t0, 0
        sw    $t0, -68($fp)
        # goto 23
        j     L2_23
L2_22:
        # t2 = 1
        li    $t0, 1
        sw    $t0, -68($fp)
L2_23:
        # r = t2
        lw    $t0, -68($fp)
        sw    $t0, -28($fp)
        # if a int< b goto 27
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        blt   $t0, $t1, L2_27
        # t3 = 0
        li    $t0, 0
        sw    $t0, -72($fp)
        # goto 28
        j     L2_28
L2_27:
        # t3 = 1
        li    $t0, 1
        sw    $t0, -72($fp)
L2_28:
        # if a int== 1 goto 31
        lw    $t0, -4($fp)
        li    $t1, 1
        beq   $t0, $t1, L2_31
        # t4 = 0
        li    $t0, 0
        sw    $t0, -76($fp)
        # goto 32
        j     L2_32
L2_31:
        # t4 = 1
        li    $t0, 1
        sw    $t0, -76($fp)
L2_32:
        # if a int!= 1 goto 35
        lw    $t0, -4($fp)
        li    $t1, 1
        bne   $t0, $t1, L2_35
        # t5 = 0
        li    $t0, 0
        sw    $t0, -80($fp)
        # goto 36
        j     L2_36
L2_35:
        # t5 = 1
        li    $t0, 1
        sw    $t0, -80($fp)
L2_36:
        # if b int>= 2 goto 39
        lw    $t0, -8($fp)
        li    $t1, 2
        bge   $t0, $t1, L2_39
        # t6 = 0
        li    $t0, 0
        sw    $t0, -84($fp)
        # goto 40
        j     L2_40
L2_39:
        # t6 = 1
        li    $t0, 1
        sw    $t0, -84($fp)
L2_40:
        # if b int<= 1 goto 43
        lw    $t0, -8($fp)
        li    $t1, 1
        ble   $t0, $t1, L2_43
        # t7 = 0
        li    $t0, 0
        sw    $t0, -88($fp)
        # goto 44
        j     L2_44
L2_43:
        # t7 = 1
        li    $t0, 1
        sw    $t0, -88($fp)
L2_44:
        # param "%d %d %d %d %d %d\n"
        # param r
        # param t3
        # param t4
        # param t5
        # param t6
        # param t7
        # call printf, 7
        addiu $sp, $sp, -32
        la    $t0, str1
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        lw    $t0, -72($fp)
        sw    $t0, 8($sp)
        lw    $t0, -76($fp)
        sw    $t0, 12($sp)
        lw    $t0, -80($fp)
        sw    $t0, 16($sp)
        lw    $t0, -84($fp)
        sw    $t0, 20($sp)
        lw    $t0, -88($fp)
        sw    $t0, 24($sp)
        jal   __printf
        addiu $sp, $sp, 32
        # calls = 0
        li    $t0, 0
        sw    $t0, g_calls
        # t8 = call no(), 0
        jal   _Z2nov
        sw    $v0, -92($fp)
        # if t8 int!= 0 goto 56
        lw    $t0, -92($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_56
        # goto 61
        j     L2_61
L2_56:
        # t9 = call yes(), 0
        jal   _Z3yesv
        sw    $v0, -96($fp)
        # if t9 int!= 0 goto 59
        lw    $t0, -96($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_59
        # goto 61
        j     L2_61
L2_59:
        # param "no\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str2
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
L2_61:
        # param "calls after &&: %d\n"
        # param calls
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str3
        sw    $t0, 0($sp)
        lw    $t0, g_calls
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # calls = 0
        li    $t0, 0
        sw    $t0, g_calls
        # t10 = call yes(), 0
        jal   _Z3yesv
        sw    $v0, -100($fp)
        # if t10 int!= 0 goto 71
        lw    $t0, -100($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_71
        # goto 68
        j     L2_68
L2_68:
        # t11 = call no(), 0
        jal   _Z2nov
        sw    $v0, -104($fp)
        # if t11 int!= 0 goto 71
        lw    $t0, -104($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_71
        # goto 73
        j     L2_73
L2_71:
        # param "or taken\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str4
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
L2_73:
        # param "calls after ||: %d\n"
        # param calls
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str5
        sw    $t0, 0($sp)
        lw    $t0, g_calls
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # calls = 0
        li    $t0, 0
        sw    $t0, g_calls
        # t13 = call no(), 0
        jal   _Z2nov
        sw    $v0, -112($fp)
        # if t13 int!= 0 goto 83
        lw    $t0, -112($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_83
        # goto 80
        j     L2_80
L2_80:
        # t14 = call yes(), 0
        jal   _Z3yesv
        sw    $v0, -116($fp)
        # if t14 int!= 0 goto 83
        lw    $t0, -116($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_83
        # goto 86
        j     L2_86
L2_83:
        # t15 = call no(), 0
        jal   _Z2nov
        sw    $v0, -120($fp)
        # if t15 int!= 0 goto 86
        lw    $t0, -120($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_86
        # goto 88
        j     L2_88
L2_86:
        # t12 = 0
        li    $t0, 0
        sw    $t0, -108($fp)
        # goto 89
        j     L2_89
L2_88:
        # t12 = 1
        li    $t0, 1
        sw    $t0, -108($fp)
L2_89:
        # r = t12
        lw    $t0, -108($fp)
        sw    $t0, -28($fp)
        # param "%d %d\n"
        # param r
        # param calls
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        lw    $t0, g_calls
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # x = 0
        li    $t0, 0
        sw    $t0, -32($fp)
        # z = 0.5
        l.d   $f0, fc0
        s.d   $f0, -40($fp)
        # ch = 0
        li    $t0, 0
        sb    $t0, -41($fp)
        # p = 0
        li    $t0, 0
        sw    $t0, -48($fp)
        # if x int!= 0 goto 100
        lw    $t0, -32($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_100
        # goto 102
        j     L2_102
L2_100:
        # t16 = 0
        li    $t0, 0
        sw    $t0, -124($fp)
        # goto 103
        j     L2_103
L2_102:
        # t16 = 1
        li    $t0, 1
        sw    $t0, -124($fp)
L2_103:
        # if z double!= 0.0 goto 105
        l.d   $f0, -40($fp)
        l.d   $f2, fc1
        c.eq.d $f0, $f2
        bc1f  L2_105
        # goto 107
        j     L2_107
L2_105:
        # t17 = 0
        li    $t0, 0
        sw    $t0, -128($fp)
        # goto 108
        j     L2_108
L2_107:
        # t17 = 1
        li    $t0, 1
        sw    $t0, -128($fp)
L2_108:
        # if ch char!= 0 goto 110
        lb    $t0, -41($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_110
        # goto 112
        j     L2_112
L2_110:
        # t18 = 0
        li    $t0, 0
        sw    $t0, -132($fp)
        # goto 113
        j     L2_113
L2_112:
        # t18 = 1
        li    $t0, 1
        sw    $t0, -132($fp)
L2_113:
        # if p ptr!= 0 goto 115
        lw    $t0, -48($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_115
        # goto 117
        j     L2_117
L2_115:
        # t19 = 0
        li    $t0, 0
        sw    $t0, -136($fp)
        # goto 118
        j     L2_118
L2_117:
        # t19 = 1
        li    $t0, 1
        sw    $t0, -136($fp)
L2_118:
        # if c int!= 0 goto 122
        lw    $t0, -12($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_122
        # goto 120
        j     L2_120
L2_120:
        # t20 = 0
        li    $t0, 0
        sw    $t0, -140($fp)
        # goto 123
        j     L2_123
L2_122:
        # t20 = 1
        li    $t0, 1
        sw    $t0, -140($fp)
L2_123:
        # param "%d %d %d %d %d\n"
        # param t16
        # param t17
        # param t18
        # param t19
        # param t20
        # call printf, 6
        addiu $sp, $sp, -24
        la    $t0, str7
        sw    $t0, 0($sp)
        lw    $t0, -124($fp)
        sw    $t0, 4($sp)
        lw    $t0, -128($fp)
        sw    $t0, 8($sp)
        lw    $t0, -132($fp)
        sw    $t0, 12($sp)
        lw    $t0, -136($fp)
        sw    $t0, 16($sp)
        lw    $t0, -140($fp)
        sw    $t0, 20($sp)
        jal   __printf
        addiu $sp, $sp, 24
        # if z double!= 0.0 goto 132
        l.d   $f0, -40($fp)
        l.d   $f2, fc1
        c.eq.d $f0, $f2
        bc1f  L2_132
        # goto 134
        j     L2_134
L2_132:
        # param "double is true\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str8
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
L2_134:
        # if p ptr!= 0 goto 138
        lw    $t0, -48($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_138
        # goto 136
        j     L2_136
L2_136:
        # param "null pointer is false\n"
        # call printf, 1
        addiu $sp, $sp, -8
        la    $t0, str9
        sw    $t0, 0($sp)
        jal   __printf
        addiu $sp, $sp, 8
L2_138:
        # if a int< b goto 141
        lw    $t0, -4($fp)
        lw    $t1, -8($fp)
        blt   $t0, $t1, L2_141
        # t21 = 0
        li    $t0, 0
        sw    $t0, -144($fp)
        # goto 142
        j     L2_142
L2_141:
        # t21 = 1
        li    $t0, 1
        sw    $t0, -144($fp)
L2_142:
        # if b int< c goto 145
        lw    $t0, -8($fp)
        lw    $t1, -12($fp)
        blt   $t0, $t1, L2_145
        # t22 = 0
        li    $t0, 0
        sw    $t0, -148($fp)
        # goto 146
        j     L2_146
L2_145:
        # t22 = 1
        li    $t0, 1
        sw    $t0, -148($fp)
L2_146:
        # t23 = t21 int+ t22
        lw    $t0, -144($fp)
        lw    $t1, -148($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -152($fp)
        # if c int< a goto 150
        lw    $t0, -12($fp)
        lw    $t1, -4($fp)
        blt   $t0, $t1, L2_150
        # t24 = 0
        li    $t0, 0
        sw    $t0, -156($fp)
        # goto 151
        j     L2_151
L2_150:
        # t24 = 1
        li    $t0, 1
        sw    $t0, -156($fp)
L2_151:
        # t25 = t23 int+ t24
        lw    $t0, -152($fp)
        lw    $t1, -156($fp)
        addu  $t0, $t0, $t1
        sw    $t0, -160($fp)
        # r = t25
        lw    $t0, -160($fp)
        sw    $t0, -28($fp)
        # param "%d\n"
        # param r
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # if a int!= 0 goto 158
        lw    $t0, -4($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_158
        # goto 160
        j     L2_160
L2_158:
        # if b int!= 0 goto 162
        lw    $t0, -8($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_162
        # goto 160
        j     L2_160
L2_160:
        # t26 = 0
        li    $t0, 0
        sw    $t0, -164($fp)
        # goto 163
        j     L2_163
L2_162:
        # t26 = 1
        li    $t0, 1
        sw    $t0, -164($fp)
L2_163:
        # r = t26
        lw    $t0, -164($fp)
        sw    $t0, -28($fp)
        # if x int!= 0 goto 170
        lw    $t0, -32($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_170
        # goto 166
        j     L2_166
L2_166:
        # if ch char!= 0 goto 170
        lb    $t0, -41($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_170
        # goto 168
        j     L2_168
L2_168:
        # t27 = 0
        li    $t0, 0
        sw    $t0, -168($fp)
        # goto 171
        j     L2_171
L2_170:
        # t27 = 1
        li    $t0, 1
        sw    $t0, -168($fp)
L2_171:
        # param "%d %d\n"
        # param r
        # param t27
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -28($fp)
        sw    $t0, 4($sp)
        lw    $t0, -168($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # if c int> a goto 178
        lw    $t0, -12($fp)
        lw    $t1, -4($fp)
        bgt   $t0, $t1, L2_178
        # t28 = 0
        li    $t0, 0
        sw    $t0, -172($fp)
        # goto 179
        j     L2_179
L2_178:
        # t28 = 1
        li    $t0, 1
        sw    $t0, -172($fp)
L2_179:
        # if t28 int!= 0 goto 182
        lw    $t0, -172($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_182
        # t29 = 0
        li    $t0, 0
        sb    $t0, -173($fp)
        # goto 183
        j     L2_183
L2_182:
        # t29 = 1
        li    $t0, 1
        sb    $t0, -173($fp)
L2_183:
        # flag = t29
        lbu   $t0, -173($fp)
        sb    $t0, -49($fp)
        # if flag bool!= 0 goto 186
        lbu   $t0, -49($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_186
        # goto 188
        j     L2_188
L2_186:
        # if d int!= 0 goto 190
        lw    $t0, -16($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_190
        # goto 188
        j     L2_188
L2_188:
        # t30 = 0
        li    $t0, 0
        sw    $t0, -180($fp)
        # goto 191
        j     L2_191
L2_190:
        # t30 = 1
        li    $t0, 1
        sw    $t0, -180($fp)
L2_191:
        # if t30 int!= 0 goto 194
        lw    $t0, -180($fp)
        li    $t1, 0
        bne   $t0, $t1, L2_194
        # t31 = 0
        li    $t0, 0
        sb    $t0, -181($fp)
        # goto 195
        j     L2_195
L2_194:
        # t31 = 1
        li    $t0, 1
        sb    $t0, -181($fp)
L2_195:
        # both = t31
        lbu   $t0, -181($fp)
        sb    $t0, -50($fp)
        # t32 = booltoint flag
        lbu   $t0, -49($fp)
        sw    $t0, -188($fp)
        # t33 = booltoint both
        lbu   $t0, -50($fp)
        sw    $t0, -192($fp)
        # param "%d %d\n"
        # param t32
        # param t33
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -188($fp)
        sw    $t0, 4($sp)
        lw    $t0, -192($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
L2_202:
        # if x int< 3 goto 204
        lw    $t0, -32($fp)
        li    $t1, 3
        blt   $t0, $t1, L2_204
        # goto 209
        j     L2_209
L2_204:
        # if x int== 2 goto 209
        lw    $t0, -32($fp)
        li    $t1, 2
        beq   $t0, $t1, L2_209
        # goto 206
        j     L2_206
L2_206:
        # t34 = x int+ 1
        lw    $t0, -32($fp)
        li    $t1, 1
        addu  $t0, $t0, $t1
        sw    $t0, -196($fp)
        # x = t34
        lw    $t0, -196($fp)
        sw    $t0, -32($fp)
        # goto 202
        j     L2_202
L2_209:
        # param "%d\n"
        # param x
        # call printf, 2
        addiu $sp, $sp, -8
        la    $t0, str0
        sw    $t0, 0($sp)
        lw    $t0, -32($fp)
        sw    $t0, 4($sp)
        jal   __printf
        addiu $sp, $sp, 8
        # big = 4000000000
        li    $t0, -294967296
        sw    $t0, -56($fp)
        # t35 = int- 1
        li    $t0, 1
        negu  $t0, $t0
        sw    $t0, -200($fp)
        # minus = t35
        lw    $t0, -200($fp)
        sw    $t0, -60($fp)
        # if big uint> 5 goto 218
        lw    $t0, -56($fp)
        li    $t1, 5
        bgtu  $t0, $t1, L2_218
        # t36 = 0
        li    $t0, 0
        sw    $t0, -204($fp)
        # goto 219
        j     L2_219
L2_218:
        # t36 = 1
        li    $t0, 1
        sw    $t0, -204($fp)
L2_219:
        # if minus int< 0 goto 222
        lw    $t0, -60($fp)
        li    $t1, 0
        blt   $t0, $t1, L2_222
        # t37 = 0
        li    $t0, 0
        sw    $t0, -208($fp)
        # goto 223
        j     L2_223
L2_222:
        # t37 = 1
        li    $t0, 1
        sw    $t0, -208($fp)
L2_223:
        # param "%d %d\n"
        # param t36
        # param t37
        # call printf, 3
        addiu $sp, $sp, -16
        la    $t0, str6
        sw    $t0, 0($sp)
        lw    $t0, -204($fp)
        sw    $t0, 4($sp)
        lw    $t0, -208($fp)
        sw    $t0, 8($sp)
        jal   __printf
        addiu $sp, $sp, 16
        # return r
        lw    $v0, -28($fp)
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
