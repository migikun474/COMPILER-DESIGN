# Phase 4 — MIPS Code Generation

> Status: **implemented and tested** on the SPIM simulator. All 29 test
> programs give the output and exit code that gcc/g++ give, compiled
> without optimization and with `-O1`, `-O2` and `-O3`
> (`./run_tests.sh`: 29 passed).

Design decisions and their reasons: [`../docs/DESIGN_LOG.md`](../docs/DESIGN_LOG.md)
(D18 SPIM, D23 `printf`, D24 `long long`, D25 calling convention).

## Usage

```bash
make
```

```bash
./mips_generator -O3 file.c > file.s
```

```bash
spim -file file.s arg1 arg2
```

`-O1` / `-O2` / `-O3` run the TAC optimizer first and turn on the
machine-level optimizations below; without them the code is a direct
translation. `--stack-only` keeps the direct translation even when
optimizing, to compare the two. SPIM prints a five-line banner before the
program's output; the program's `return` value from `main` becomes
SPIM's exit code.

### Running in QtSpim

The same `.s` file is meant for QtSpim (the windowed SPIM, 9.1):

1. *File → Reinitialize and Load File*, choose `file.s`.
2. Program arguments, if any: *Simulator → Run Parameters*.
3. *Simulator → Run/Continue* (F5). `printf` output appears in the
   Console window; `scanf` waits there for a line of input.

Use the default settings (*Simulator → Settings*): Accept Pseudo
Instructions **on**, Load Exception Handler **on**, Bare Machine
**off**, Enable Delayed Branches **off**.

Checked on 2026-10-10 with QtSpim 9.1.21: `t29_registers` compiled at
`-O3` prints the same five lines in the QtSpim Console as in the
terminal.

QtSpim has no batch mode, so the automated tests run the command-line
`spim`, which is the same simulator without the window. The run-time
library only uses system calls both have (`print_char`, `read_string`,
`sbrk`, `exit2`).

## How TAC becomes MIPS

Each TAC instruction is translated on its own into a short fixed
sequence: load the operands from memory into scratch registers, do the
operation, store the result. The TAC instruction is written above its
code as a comment:

```
        # t2 = b int* t1
        lw    $t0, -8($fp)
        lw    $t1, -140($fp)
        mul   $t0, $t0, $t1
        sw    $t0, -144($fp)
```

Without optimization no value is kept in a register between two TAC
instructions. With `-O1` and above the most used names live in
registers (next section).

| TAC | MIPS |
|---|---|
| `int+` `uint+` `ptr+` | `addu`; `-` `subu`; `*` `mul`; `/` `%` → `div`/`divu` + `mflo`/`mfhi` |
| `int<<` `>>` | `sllv`, `srav` (signed) / `srlv` (unsigned) |
| `float`/`double` operators | `add.s`/`add.d` … on `$f0`, `$f2` |
| `llong` operators | two words: add/subtract with carry, multiply from `multu`, the rest in the run-time library |
| conversions | `mtc1` + `cvt.d.w`, `trunc.w.d` + `mfc1`, `cvt.s.d`/`cvt.d.s`; unsigned values adjusted by 2^32 / 2^31 |
| `if a relop b goto L` | `beq`/`blt`/`bltu` …; floating point `c.lt.d` + `bc1t` |
| `x = a[i]`, `*p = x` | address in `$t8`, then `lw`/`lb`/`l.d` … or a byte copy for structs |
| `param` / `call` | arguments stored into a freshly reserved stack area, `jal`, area released |

## Machine-level optimizations (`-O1` and above)

| Optimization | What it does |
|---|---|
| registers by usage count and live interval (Dragon Book 8.8) | in each function the uses of every name are counted, a use inside a loop counting ten times per level of nesting, and the interval of instructions in which the name occurs is recorded (widened over every loop it reaches into). In order of count each name takes the first register that no overlapping name holds, so names that are never alive together share one: `$s0`–`$s7` for integers, pointers, `char`, `short` and `bool`; `$f20`–`$f30` for `float` and `double`. Only scalars whose address is never taken qualify. The function saves and restores the registers it uses, so they survive calls. A parameter that got a register is loaded once on entry. |
| immediate operands | a small constant goes into the instruction: `addiu`, `andi`, `ori`, `xori`, `sll`, `sra`, `srl`; `$zero` for 0; a constant array or field offset becomes the displacement (`lw $s0, -12($fp)`) |
| comparison as a value | the TAC pattern `if a < b goto +3 ; t = 0 ; goto +2 ; t = 1` becomes `slt` (plus `xori`/`sltiu` for the other relations) |
| leaf functions | a function that calls nothing does not save `$ra` |
| peephole (Dragon Book 8.7) | a load right after a store to the same place reuses the register; a jump to the next line and `move $r, $r` are removed |

```
        # t4 = j int<< 2            (j in $s0, t4 in $s3)
        sll   $s3, $s0, 2
        # j = j int+ 1
        addiu $s0, $s0, 1
```

Instructions in the generated functions (not the run-time library):

| Program | `-O0` | `-O3 --stack-only` | `-O3` |
|---|---|---|---|
| `t04_arrays` | 856 | 864 | 470 |
| `t17_strings` | 1022 | 1215 | 807 |
| `t18_algorithms` | 1247 | 1081 | 766 |
| `t20_bits` | 679 | 424 | 328 |
| `t21_numeric` | 655 | 528 | 425 |
| `t22_data_structures` | 991 | 975 | 612 |
| `t25_control` | 731 | 698 | 485 |

A `char`, `short` or `bool` in a register is re-extended after every
write, so it always holds what a load from memory would give.
`long long` always stays in the frame: it would need a pair of
registers and is rarely in a hot loop.

A variable that is read before it is ever assigned has an arbitrary
value in C. In the frame that value happens to be 0 on SPIM; in a
register it is whatever the register held.

## Frame and calling convention (decision D25: stack only)

```
        arguments ...           8($fp), 12($fp), ...    stored by the caller
        saved $ra               4($fp)
        saved $fp               0($fp)      <- $fp
        locals and temporaries  -4($fp), -8($fp), ...
                                            <- $sp
```

- Every argument is on the stack, the first at the lowest address;
  `double` and `long long` arguments are 8-byte aligned. `this` is the
  first argument of a member function.
- The result is in `$v0` (`$v0`/`$v1` for `long long`, `$f0` for
  `float`/`double`). A struct is returned as its address in `$v0` and
  copied by the caller at once.
- The caller removes the arguments. `$sp` is always 8-byte aligned.
- Variable arguments need nothing special: `va_start` is the address
  after the last named argument, `va_arg` reads and advances.
- Only temporaries that the (optimized) code still uses get a frame
  slot.

`main` in the assembly file is a small start-up stub: it aligns the
stack, stores `argc`/`argv` as arguments, stores the addresses that
initialize pointer globals, calls the program's `main` (`main_`) and
exits with its result.

## Run-time library

[`runtime/runtime.s`](runtime/runtime.s) is appended to every output,
because SPIM has no C library:

| Routine | What it does |
|---|---|
| `__printf` | `%d %i %u %x %X %o %c %s %f %%` with `-` and `0` flags, width, precision, `*`, lengths `l` `ll` `h` `z`. `%f` rounds to nearest, ties to even, like glibc. |
| `__scanf` | `%d %i %u %c %s %f` (`l` for `double`, a width for `%s`); input is taken a line at a time with the `read_string` system call, so it works in a terminal and in QtSpim's console |
| `__malloc` `__calloc` `__realloc` `__free` | over the `sbrk` system call; a block's size is stored before it; memory is not reused |
| `__memcpy` | struct copies |
| `__divll` `__modll` `__udivll` `__umodll` | 64-bit division by shift and subtract |
| `__shlll` `__shrll` `__sarll`, `__dtoll` | 64-bit shifts; `double` → `long long` |

## Source layout

| File | Contents |
|---|---|
| [`include/mips.h`](include/mips.h), [`src/mips.cpp`](src/mips.cpp) | the code generator |
| [`src/main.cpp`](src/main.cpp) | driver: phases 2, 2b and 3 compiled in unchanged, then MIPS |
| [`runtime/runtime.s`](runtime/runtime.s) | the run-time library |
| [`run_tests.sh`](run_tests.sh) | compiles and runs every test in SPIM at three optimization levels |

## Tests

```bash
./run_tests.sh
```

Uses the programs and expected outputs of
[`../phase3-ir/test`](../phase3-ir/test) (the outputs are gcc/g++'s).
`t16_runtime` is aimed at this phase: 64-bit arithmetic, conversions,
`printf` formats, structs and doubles through calls, variable
arguments, the allocation routines. Besides the suite, the 45 runnable
programs of the semantic and parser suites were compiled at `-O0` and
`-O2` and run in SPIM: all 90 runs match the TAC interpreter.

## Limitations

- `long long` values always stay in the frame (no register pairs).
- `printf` has no `%e` / `%g`; `%f` needs a value below about 9·10¹⁸
  after scaling by the precision. `scanf` has no `%x`.
- `double` → `long long` needs a result below 2⁶³/2 in magnitude.
- `free` does not reuse memory.
- The limits of the TAC generator apply unchanged (see
  [`../phase3-ir/README.md`](../phase3-ir/README.md#limitations)).
