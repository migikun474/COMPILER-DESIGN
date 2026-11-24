# Phase 3 — Intermediate Representation (Three Address Code)

> Status: **implemented and tested** — a TAC generator, a TAC
> interpreter and the optimizer (`-O1`). 34 test programs are
> generated, executed raw and at `-O1`, and compared with gcc/g++
> (`./run_tests.sh`: 35 passed, the 34 programs and one warnings check).

The format follows the course slides (Lectures 25–27) and Dragon Book
chapter 6. Every choice between two valid forms was put to the user;
the decisions and their reasons are in
[`../docs/DESIGN_LOG.md`](../docs/DESIGN_LOG.md) (D8–D17).

## Usage

```bash
make
```

```bash
./tac_generator file.c
```

Prints the TAC and writes it to `logs/file.tac`. Lexical, syntax or
semantic errors are reported exactly as in the earlier phases and no
code is generated.

```bash
./tac_generator --run file.c arg1 arg2
```

Prints the TAC, then executes it with the interpreter (`-q` after
`--run` prints only what the program itself prints). The program's
`scanf` reads standard input; its exit code becomes the exit code of
`tac_generator`; the number of executed instructions goes to stderr.

```bash
./tac_generator -O1 --run file.c
```

Optimizes first (see [Optimization](#optimization--o1)). With `--run`
the program is executed both ways; a difference in output or exit code
is reported as `OPTIMIZER BUG`, otherwise the line on stderr shows the
instructions executed with and without optimization.

## What the output looks like

```c
int main() {
    int a, b = 2, c = 3, x, y, i = 1, arr[10];
    a = b * -c + b * -c;
    while (a < b) a = a + 1;
    y = a < b;
    x = arr[i];
    return y;
}
```

```
function main()        link name: main
  symbol table (name, kind, type, width, offset)
    a              local  int                        4      0
    ...
    t1             temp   int                        4     64
    ...
    total width 100
  code
 100:     b = 2
 101:     c = 3
 102:     i = 1
 103:     t1 = int- c
 104:     t2 = b int* t1
 105:     t3 = int- c
 106:     t4 = b int* t3
 107:     t5 = t2 int+ t4
 108:     a = t5
 109: L1: if a int< b goto L2
 110:     goto L3
 111: L2: t6 = a int+ 1
 112:     a = t6
 113:     goto L1
 114: L3: if a int< b goto L4
 115:     t7 = 0
 116:     goto L5
 117: L4: t7 = 1
 118: L5: y = t7
 119:     t8 = i int* 4                       (w = 4)
 120:     t9 = arr[t8]
 121:     x = t9
 122:     return y
```

The full listing for the slides' examples is
[`test/expected/t12_lecture_examples.tac`](test/expected/t12_lecture_examples.tac).

## Instruction set

Quadruples `(op, arg1, arg2, result)` in one numbered array per
function (numbering runs through the program from 100).

| Form | Meaning |
|---|---|
| `x = y` | copy (a struct is copied whole) |
| `x = y <type><op> z` | `+ - * / % & \| ^ << >>` on `int`, `uint`, `llong`, `ullong`, `float`, `double`, `ptr` |
| `x = <type>- y`, `x = <type>~ y` | unary minus, bitwise not |
| `x = <from>to<to> y` | conversion: `inttodouble`, `chartoint`, `doubletoint`, … |
| `goto L` | jump |
| `if x <type><relop> y goto L` | conditional jump, `== != < > <= >=` |
| `x = y[z]`, `y[z] = x` | load / store at byte offset `z` from the object `y` |
| `x = &y`, `x = *y`, `*x = y` | address, load and store through a pointer |
| `param x`, `call f, n`, `x = call f, n` | arguments left to right, then the call |
| `return`, `return x` | |
| `va_start ap, last`, `x = va_arg ap, type`, `va_end ap` | variable arguments |

Every instruction that is a jump target gets a label (`L1`, `L2` …,
unique in the program); the instruction number stays visible.

## How the slides map to the code

| Slides | Here |
|---|---|
| `E.place`, `E.code` | the `Operand` returned by `rvalue()` / the quads it appends |
| `newtmp()`, `emit()` / `gen()` | `newTemp()`, `emit()` |
| `E.true`, `E.false`, `S.next` | backpatch lists: the two filled by `cond()`, the one returned by `stmt()` |
| `makelist`, `merge`, `backpatch` | the same names in `Generator` |
| `mktable`, `enter`, `addwidth` (Lecture 25) | `buildFrame()`: each function's table of names with type, width, offset |
| `base + i × w`, `((i1 × n2) + i2) × w` (Lecture 26) | `indexLValue()` |
| `int +`, `real +`, `inttoreal` (Lecture 26) | the type on every operator, `convert()` |
| relop as a value: `if … goto +3; t = 0; goto +2; t = 1` (Lecture 27) | `boolValue()` |
| short-circuit `or` / `and` / `not` (Lecture 27) | `cond()` |

## Source layout

| File | Contents |
|---|---|
| [`include/tac.h`](include/tac.h), [`src/tac.cpp`](src/tac.cpp) | `Operand`, `Quad`, `Function`, `Program`; the listing printer |
| [`include/irgen.h`](include/irgen.h) | the `Generator` class |
| [`src/gen_expr.cpp`](src/gen_expr.cpp) | expressions: conversions, lvalues and addresses, operators, boolean expressions, calls, constructors |
| [`src/gen_stmt.cpp`](src/gen_stmt.cpp) | statements, local and static initializers, functions, frame tables |
| [`include/interp.h`](include/interp.h), [`src/interp.cpp`](src/interp.cpp) | the TAC interpreter |
| [`include/opt.h`](include/opt.h), [`src/opt.cpp`](src/opt.cpp) | the optimizer driver (`-O1`); the passes are in `src/opt_*.cpp` (below) |
| [`src/main.cpp`](src/main.cpp) | driver: phases 2 and 2b (compiled in unchanged), then generation and `--run` |

The generator walks the AST that semantic analysis annotated: it reads
each node's `semType`, `symbol` and constant value and never re-derives
a type or an overload.

## How language features are lowered

| Feature | TAC |
|---|---|
| `if`, `while`, `for`, `do`, `until`, `?:`, `&&`, `\|\|`, `!` | jumping code with backpatching |
| `switch` | subject in a temporary, body, then a chain of `if t == v goto Lcase` and a `goto` to the default |
| `break`, `continue`, `goto` | `goto` |
| arrays, `struct` / `union` fields | `x = a[offset]`, offset from the slides' formula or the field's layout offset (always 0 in a union) |
| enums | an enum value is an `int`; an enumerator is an integer constant operand (it has no storage) |
| pointers, `p->f`, `p[i]` | `ptr+` and `*` |
| references | hold an address: `r = &x`, a use is `*r` |
| member functions | `this` is a hidden first parameter; fields are `this ptr+ offset` |
| inheritance | single inheritance: the base is at offset 0, so `this` and converted pointers are unchanged |
| constructors | default constructors only (D35): a call with the object's address; the base and the members are built first, in declaration order, then the body runs. There are no destructors |
| operator overloading | a call to `operator<op>` |
| `printf`, `scanf`, `malloc`, `calloc`, `realloc`, `free` | `call` to the built-in by name |
| variable arguments | `va_start` / `va_arg` / `va_end` instructions; extra arguments promoted as in C |
| globals, `static` locals | data in the `globals` table; class objects among them are constructed when `main` starts |

## The interpreter

`src/interp.cpp` executes a `tac::Program` with the MIPS32 data model:
byte-addressed memory, 4-byte `int` and pointers, each function's
frame laid out by its symbol table. It implements the built-ins
(`printf` formats, `scanf`, the allocation functions), reports run-time
errors (null or out-of-range access, division by zero, recursion deeper
than 10,000 calls (`stack overflow (recursion too deep)`), a 500-million
instruction limit) and counts executed instructions — the number the
optimizer will later be measured by.

## Optimization (`-O1`)

There is one optimization level (D49). Each function is cut into basic
blocks (a block starts at the first instruction, at every jump target
and after every jump or return) and each block is optimized by **value
numbering**: every value computed in the block gets a number, and two
instructions that get the same number compute the same value. A value
number is a node of the block's DAG (Dragon Book 8.5; the hash-table
construction is 6.1.2), so this is the DAG method without building and
re-linearizing a graph. Small functions are then inlined and the block
passes run again on the larger bodies.

| Optimization | Example |
|---|---|
| constant folding | `t1 = 3 int+ 4` → `t1 = 7`; `if 1 int== 1 goto L` → `goto L`; folded with the interpreter's own arithmetic, so wrap-around and conversions are exact |
| algebraic simplification | `x + 0`, `x * 1`, `x / 1`, `x & x`, `x \| x`, `x & -1` → `x`; `x * 0`, `x - x`, `x ^ x`, `x & 0`, `x % 1` → `0`; `x \| -1` → `-1`; `x * 8` → `x << 3` (the identities are for integers only; `x + 0.0` is left alone because of `-0.0`) |
| common subexpressions | the second `x * y + 3`, `&d`, `a[i]` or `*p` in a block reuses the first result; after `a[i] = x`, a load of `a[i]` is `x` |
| copy and constant propagation | after `t = a`, uses of `t` become `a`; after `b = 2`, uses of `b` in the block become `2` |
| temporary merging | `t1 = a + b ; x = t1` → `x = a + b` |
| dead temporaries | an instruction whose result no instruction reads is removed (a call stays, only its unused result goes) |
| jump clean-up | jump to the next instruction; jump to a jump; `if c goto L1 ; goto L2 ; L1:` → `if !c goto L2`; code no path reaches |
| function inlining | a call to a function of at most 16 instructions, not recursive and not variadic, is replaced by its body; parameters, locals and temporaries become temporaries of the caller | `square(3)` → `9` after folding |

What keeps it correct: a value read from memory is only reused while
nothing can have changed it. Any store through a pointer, any array or
field store, any call, and any assignment to a global or to a variable
whose address was taken invalidates what is known about memory.

The optimizer is split by job, one file each:

| File | Job |
|---|---|
| [`src/opt.cpp`](src/opt.cpp) | the driver: block passes until nothing changes, inlining, block passes again; the summary |
| [`src/opt_common.cpp`](src/opt_common.cpp) | operands and names, basic blocks, which names memory writes can change |
| [`src/opt_numbering.cpp`](src/opt_numbering.cpp) | value numbering of one block: folding, propagation, common subexpressions |
| [`src/opt_algebra.cpp`](src/opt_algebra.cpp) | the algebraic identities |
| [`src/opt_cleanup.cpp`](src/opt_cleanup.cpp) | temporary merging, dead temporaries, jump clean-up |
| [`src/opt_inline.cpp`](src/opt_inline.cpp) | function inlining |
| [`src/opt_uninitialized.cpp`](src/opt_uninitialized.cpp) | reaching definitions for the uninitialized-variable warning (not an optimization) |

On the test programs `-O1` executes 1% to 50% fewer instructions; the
runner prints the figure per test.

## Tests

```bash
./run_tests.sh
```

Each `test/tNN_*.c` is generated and executed raw and with `-O1`;
every time what it prints and its exit code must equal
`test/expected/<name>.out`. The programs are also
valid C or C++, and every expected file was checked to be identical to
the output of the same source compiled with gcc/g++.
`t12_lecture_examples` additionally compares the TAC listing itself.

| Test | Covers |
|---|---|
| `t01_expressions` | arithmetic, conversions, unsigned, bitwise, compound assignment, `++`/`--`, comma, `?:`, C-style and functional casts, `sizeof`, scalar brace and paren initialization, wrap-around of every width |
| `t02_control_flow` | `if`/`else` chains, `while`, `do`-`while`, `for` with a declaration, `until`, `switch` with fall-through and `default` in the middle, `break`, `continue`, `goto` out of two loops, a state machine |
| `t03_booleans` | the slides' `a < b \|\| c < d && e < f`, comparisons and `!` as values, booleans stored and summed, `&&`/`\|\|` in loop conditions, `bool` |
| `t04_arrays` | 1-D to 3-D arrays, partial and designated initializers, zeroed static data, `i[a]`, array parameters (1-D and 2-D), strings, `sizeof` of an array (plain C: expected output from gcc) |
| `t05_pointers` | two and three levels, arithmetic and differences, `void *`, pointer to an array, array of pointers, writing through a pointer to a pointer |
| `t06_structs` | nesting, copies, by-value parameters and results, arrays of structs, array members, anonymous members, padding, a union read through another member |
| `t07_functions` | recursion, mutual recursion, overloading, references (to a pointer, returned, `const T &` to another type), varargs with a `va_list` passed on, `static` locals, tail recursion |
| `t08_classes` | construction order (base, members, body), a static member, operators, arrays of objects, objects inside objects, a hidden base function called through `Base::`, `this`, a friend, a global object built before `main`, block copies |
| `t09_memory` | `malloc`/`calloc`/`realloc`/`free`, a freed block reused, a linked list built, reversed and freed, rows from `malloc`, a long malloc/free loop |
| `t10_io` | `printf` formats, `scanf` (input in `t10_io.in`) |
| `t11_main_args` | `argc` / `argv` (arguments in `t11_main_args.args`) |
| `t12_lecture_examples` | the slides' examples, with the expected listing |
| `t13_runtime` | aimed at the MIPS run-time library: 64-bit `printf`, `long long` ↔ `double`, flags, widths, precision, `%e %g %x %o %c %%`, structs and doubles through calls, varargs with doubles, `long long` and strings |
| `t14_optimizer` | `-O1` must not reuse what may have changed (through a pointer, a reference, a call, an array element) and must keep what is used: wrapping constants, per-path constants, a loop-carried value, dead assignments, calls whose result is unused |
| `t15_o3` | inlining (side effects, several returns, a reference, a by-value struct), a recursive function not inlined, a tail call with swapped arguments, a division in a loop that may run zero times |
| `t16_registers` | for the MIPS back end: values across calls and recursion, many live values at once, arguments computed before a call, `char`/`short` wrapping in registers, many doubles at once, a loop made of `goto` |
| `t17_algorithms` | bubble sort, quicksort, binary search, Hanoi, Ackermann, matrix product, sieve, string reversal, number ↔ text |
| `t18_scopes_enums` | shadowing (parameters, blocks, loop variables, a local hiding a global from its declaration on), `static` locals, `typedef`, a conditional constant initializer, enums with C++ rules |
| `t30_int_edges` | small: `/` and `%` with negative operands, shifts of signed and unsigned values, unsigned wrap-around, `char`/`short` sign and zero extension, signed vs unsigned comparison, `INT_MAX`/`INT_MIN` |
| `t31_short_circuit` | small: `&&`/`\|\|` skipping their right operand, `?:` evaluating one branch, comma, chained and compound assignment, `i++` in an index, side effects in a loop condition |
| `t32_calls_registers` | small: more arguments than `$a0`–`$a3`, mixed `char`/`double`/`long long` arguments, calls as arguments, values kept across calls, a struct by value and returned, recursion with live values |
| `t33_brace_elision` | `struct { int a[2]; int b; } s = {1, 2, 3}` and friends, for globals (static data) and locals |
| `t34_float_formats` | `printf` `%e` `%E` `%g` `%G` next to `%f`: precision, width, flags, rounding into the next power of ten, zero, negatives, where `%g` changes style |
| `t35_loop_shapes` | `break`, `continue`, a `switch` inside a `while`, `do`-`while`, nested `for` (the program that hung global common subexpressions before D41; input in `t35_loop_shapes.in`) |
| `t36_enums_unions` | enums (switch, overloading, casts into an enum, `?:`) and unions read through another member than the one written, in a block, across blocks and calls, in arrays and by value, with 8-byte members (D42) |
| `t38_free_list` | the heap reuses freed memory (D45): the same block back after `free`, a 50,000-iteration malloc/free loop in constant space, a list freed and rebuilt, `calloc` of a reused dirty block, `realloc` growing and shrinking, `free(0)` |
| `t39_printf_pointers` | `printf("%p")`: `0x` and lowercase hex, `(nil)` for a null pointer, width and `-` over the whole text, pointer arithmetic shown through `%p`; the pointers are made from fixed numbers so g++, the interpreter and SPIM print the same |
| `t40_aliasing` | small: the optimizer must not reuse a value changed through a pointer, through a second pointer, through another array index, by a call to a global or through an address passed to a call |
| `t41_loop_edges` | small: loops running 0, 1, 2, 3 and 7 times (the unrolled copy keeps each exit test), do-while once, `break`/`continue` in nested loops, a backward `goto`, `continue` from a `switch` |
| `t42_statics_globals` | small: static locals across calls and in recursion, partly initialized global arrays and structs, string literals in globals |
| `t43_float_conv` | small: double/float → int truncation toward zero, int ↔ double, float precision, `printf` rounding (`%.2f` of 2.675 is `2.67`), int/double comparison, unsigned → double |
| `t44_long_long` | small: carries between the halves, multiply/divide/remainder with negatives, shifts across 32, comparisons, conversion to and from double, values across calls |
| `t45_strings_chars` | small: walking, copying and comparing strings with pointers, escapes, character arithmetic, digits ↔ number, `%5s` `%-5s` `%.2s` |
| `t46_classes_small` | small: constructor order down a chain, a static member counting objects, functions a derived class hides (bound from the declared type), an operator returning a reference, an array of objects |
| `diagnostics/uninitialized` | not run: the warnings it must produce are in `uninitialized.err` |

## Warnings from this phase

`tac_generator` and `mips_generator` print one warning for each local
variable that some path reads before anything was stored in it:

```
u.c:6: warning: variable 'x' may be used uninitialized in function 'pick(int)' [uninitialized]
```

It comes from reaching definitions (D38, Dragon Book 9.2.4): every
local starts with a pseudo-definition at the function's entry, and a
read that this entry definition reaches is reported, at the line of the
read. It is computed on the unoptimized code at every `-O` level. Only
scalars whose address is never taken are tracked: arrays, objects,
globals and anything reached through a pointer are not.

## Syntax-directed translation (Lectures 25–27)

A walk-through with flowcharts of every construct is in
[`../docs/TRANSLATION.md`](../docs/TRANSLATION.md).

The translation is the slides' syntax-directed translation scheme. The
semantic rules are run during a walk over the annotated syntax tree
rather than inside the parser's actions (decision D10 in
`docs/DESIGN_LOG.md`: the types, overloads and offsets the rules need
only exist after semantic analysis). The attributes and helpers keep
their names:

| Slides | Here |
|---|---|
| `E.place` | the `Operand` an expression function returns |
| `E.code` | the instructions it `emit()`s, in order |
| `newtemp()`, `gen()` / `emit()` | `newTemp()`, `emit()` |
| `makelist`, `merge`, `backpatch` | `makelist()`, `merge()`, `backpatch()` |
| `nextquad`, marker `M -> e { M.quad = nextquad }` | `nextQuad()`, called where `M` would be reduced |
| `N -> e { N.nextlist = makelist(nextquad); gen('goto _') }` | `emitGoto()` with its index kept in a list |
| `B.truelist`, `B.falselist`, `S.nextlist` | the lists `cond()` fills and `stmt()` returns |

Each production, and where its semantic rules are:

| Production (slides) | Function |
|---|---|
| `E -> E1 op E2` | `binary()` in `src/gen_expr.cpp` |
| `E -> - E1`, `E -> ( E1 )`, `& E1`, `* E1` | `unary()` |
| `S -> id = E`, `S -> L = E` | `assignment()` |
| `L -> id [ E ]`, `L -> L1 [ E ]` (row-major, `((i1*n2)+i2)*w`) | `indexLValue()` |
| `B -> E1 relop E2` | `relJump()` (called by `cond()`) |
| `B -> B1 \|\| M B2`, `B -> B1 && M B2`, `B -> ! B1`, `B -> true / false` | `cond()` |
| boolean as a value (`if a < b goto +3 ; t = 0 ; goto +2 ; t = 1`) | `boolValue()` |
| `E -> B ? E1 : E2` | `ternary()` |
| `S -> call id ( Elist )`, `Elist -> Elist , E` | `call()` |
| `S -> { L }`, `L -> L1 M S` | `block()` in `src/gen_stmt.cpp` |
| `S -> if ( B ) M S1`, `if ... else`, `while`, `do-while`, `for`, `switch`, `break`, `continue`, `return`, `goto` | the cases of `stmt()` |

The rule each function implements is written in the comment above it,
in the slides' notation.

Because jump targets are filled in by backpatching, the TAC of a
function comes out in a single walk, with no second pass to fix the
jumps. The compiler as a whole is not single-pass: parsing, semantic
analysis and this walk are separate passes.

## Quadruples

Each TAC instruction is stored as a quadruple (the slides' "quad"), a
record with four fields: `op`, `arg1`, `arg2`, `result` -- `struct Quad`
in `include/tac.h` (`op`, `a`, `b`, `r`, plus the jump target and the
callee). The instructions of a function are an array of quads, numbered
from 100 as in the slides; a jump's target is the index of a quad, which
is what `backpatch()` writes.

| TAC | op | arg1 | arg2 | result |
|---|---|---|---|---|
| `t1 = a int+ b` | `int+` | `a` | `b` | `t1` |
| `t2 = minus c` | `minus` | `c` | | `t2` |
| `x = t1` | `=` | `t1` | | `x` |
| `if a < b goto 104` | `if <` | `a` | `b` | `104` |
| `param t2` | `param` | `t2` | | |
| `t3 = call f, 2` | `call` | `f` | `2` | `t3` |

## Logs

Every run writes the listing to `logs/` in the current directory:
`logs/<file>.tac` without optimization and `logs/<file>.O1.tac` with
`-O1`. Each log is in sections:
a header (source, optimization level, instruction count), the
optimization summary (with `-O1`), the globals, one section per
function (its symbol table -- name, kind, type, width, offset -- then its
numbered code with labels), the semantic symbol table grouped by scope,
and the record layouts; with `--run`, a last section holds what the
program printed, its exit code and the instructions executed. Temporaries the optimized code no longer uses
are left out of a function's table (a line says how many).
`./run_tests.sh` keeps both logs of every test program in
`phase3-ir/logs/`.

## Limitations

- Without an `-O` flag the output is deliberately unoptimized (decision D16).
- After optimization the symbol table still lists temporaries that are no
  longer used (the MIPS back end gives them no frame slot, D39).
- A static initializer the generator cannot evaluate at compile time
  is reported as a code generation error (no code is produced).

## Next

Phase 4 turns this TAC into MIPS: [`../phase4-codegen/README.md`](../phase4-codegen/README.md).
