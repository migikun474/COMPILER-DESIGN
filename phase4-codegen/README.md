# Phase 4 — MIPS Code Generation

> Status: **implemented and tested** on the SPIM simulator. All 16 test
> programs give the output and exit code that gcc/g++ give, compiled
> without optimization, with `-O1` and with `-O2`
> (`./run_tests.sh`: 16 passed).

Design decisions and their reasons: [`../docs/DESIGN_LOG.md`](../docs/DESIGN_LOG.md)
(D18 SPIM, D23 `printf`, D24 `long long`, D25 calling convention).

## Usage

```bash
make
```

```bash
./mips_generator -O2 file.c > file.s
```

```bash
spim -file file.s arg1 arg2
```

`-O1` / `-O2` run the TAC optimizer first; without them the code is a
direct translation. SPIM prints a five-line banner before the
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

No value is kept in a register between two TAC instructions: there is
no register allocation yet (the next step of the roadmap).

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

- No register allocation: every operand is loaded from and stored to
  the frame.
- `printf` has no `%e` / `%g`; `%f` needs a value below about 9·10¹⁸
  after scaling by the precision. `scanf` has no `%x`.
- `double` → `long long` needs a result below 2⁶³/2 in magnitude.
- `free` does not reuse memory.
- The limits of the TAC generator apply unchanged (see
  [`../phase3-ir/README.md`](../phase3-ir/README.md#limitations)).
