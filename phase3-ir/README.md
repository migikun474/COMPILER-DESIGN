# Phase 3 — Intermediate Representation (Three Address Code)

> Status: **implemented and tested** — a TAC generator, a TAC
> interpreter and the optimizer (`-O1`, `-O2`, `-O3`). 34 test programs are
> generated, executed raw and at every level, and compared with gcc/g++
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
./tac_generator -O2 --run file.c
```

Optimizes first (`-O1`, `-O2` or `-O3`, see [Optimization](#optimization--o1--o2--o3)). With `--run`
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
| [`include/opt.h`](include/opt.h), [`src/opt.cpp`](src/opt.cpp) | the optimizer (`-O1`, `-O2`, `-O3`) |
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
| constructors | default constructors only (D35): a call with the object's address; the base is built first, then (for a class with virtual functions) the table pointer is set, then the members, then the body. There are no destructors |
| virtual functions (D44) | one table `_ZTV<class>` per polymorphic class (a global of function addresses); a call through a pointer, a reference or `this` is `t1 = *p` (the table pointer, at the class's `vptrOffset`), `t2 = t1[4k]`, `param p (this)`, `t3 = call *t2, n`; `obj.f()` and `p->Base::f()` stay direct calls. A copy that creates an object re-installs its declared class's table; an assignment keeps the target's |
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

## Optimization (`-O1`, `-O2`, `-O3`)

[`src/opt.cpp`](src/opt.cpp). Each function is cut into basic blocks
(a block starts at the first instruction, at every jump target and
after every jump or return) and each block is optimized by **value
numbering**: every value computed in the block gets a number, and two
instructions that get the same number compute the same value. A value
number is a node of the block's DAG (Dragon Book 8.5; the hash-table
construction is 6.1.2), so this is the DAG method without building and
re-linearizing a graph.

| Optimization | Example |
|---|---|
| constant folding | `t1 = 3 int+ 4` → `t1 = 7`; `if 1 int== 1 goto L` → `goto L`; folded with the interpreter's own arithmetic, so wrap-around and conversions are exact |
| algebraic simplification | `x + 0`, `x * 1`, `x / 1`, `x & x`, `x \| x`, `x & -1` → `x`; `x * 0`, `x - x`, `x ^ x`, `x & 0`, `x % 1` → `0`; `x \| -1` → `-1`; `x * 8` → `x << 3` (the identities are for integers only; `x + 0.0` is left alone because of `-0.0`) |
| common subexpressions | the second `x * y + 3`, `&d`, `a[i]` or `*p` reuses the first result |
| copy and constant propagation | after `t = a`, uses of `t` become `a`; after `b = 2`, uses of `b` in the block become `2` |
| temporary merging | `t1 = a + b ; x = t1` → `x = a + b` |
| dead temporaries | an instruction whose result no instruction reads is removed (a call stays, only its unused result goes) |
| jump clean-up | jump to the next instruction; jump to a jump; `if c goto L1 ; goto L2 ; L1:` → `if !c goto L2`; code no path reaches |

What keeps it correct: a value read from memory is only reused while
nothing can have changed it. Any store through a pointer, any array or
field store, any call, and any assignment to a global or to a variable
whose address was taken invalidates what is known about memory
(`memoryChanged()`).

**`-O2`** adds two optimizations across basic blocks. Both are
data-flow analyses over the function's flow graph (Dragon Book 9.2)
and both only reason about scalar locals whose address is never taken:

| Optimization | Analysis | Example |
|---|---|---|
| global constant and copy propagation | forward; a fact (`x = 5`, `b = a`) holds at a block's entry only if it holds at the end of every predecessor | `x = 5; if (c) y = x + 1; else y = x + 2;` → `y = 6` / `y = 7` |
| dead assignment elimination | backward live-variable analysis | `a = 7; a = 8;` drops the first; a variable never read again loses its assignments (a call stays, its result is dropped) |

After each, `-O1` runs again on the result, until nothing changes.

**`-O3`** adds (decision D27):

| Optimization | How | Example |
|---|---|---|
| inlining | a call to a function of at most 16 instructions, not recursive and not variadic, is replaced by its body; parameters, locals and temporaries become temporaries of the caller; one level per run | `square(3)` → `9` after folding; getters and small operators disappear |
| tail recursion | `return f(args);` inside `f` becomes "assign the arguments, jump to the start" | `gcd(b, a % b)` becomes a loop |
| common subexpressions across blocks | available-expressions analysis: an expression is reused when the same name still holds it on every path | `x * y + 2` before an `if` and again inside it |
| loop unrolling by two | natural loops from dominators; a small loop (header first, one back edge, at most 24 instructions) gets a second copy of its test and body, so the jump back is taken every other iteration | `H: test; body; goto H` → `H: test; body; H2: test; body; goto H` |
| dead function removal | after inlining, a function no call reaches from `main` is dropped | a helper inlined everywhere disappears |
| store-to-load forwarding (part of `-O1`'s block pass) | after `a[i] = x` or `*p = x`, a load of the same place in the block is `x` until memory may have changed | `arr[i] = 10; a = arr[i];` → `a = 10` |

Loop-invariant code motion was removed (D36); the dominator and
natural-loop analysis it used now serves unrolling. Strength reduction
of induction variables is not done: `-O1` already turns `i * 4` into a
shift, so it would not remove any instruction.

On the test programs `-O1` executes 1% to 50% fewer instructions,
`-O2` 1% to 64% and `-O3` 1% to 64%; the runner prints the figures per
test.

## Tests

```bash
./run_tests.sh
```

Each `test/tNN_*.c` is generated and executed raw, with `-O1`, `-O2`
and `-O3`; every time what it prints and its exit code must equal
`test/expected/<name>.out`. The programs are also
valid C or C++, and every expected file was checked to be identical to
the output of the same source compiled with gcc/g++.
`t12_lecture_examples` additionally compares the TAC listing itself.

| Test | Covers |
|---|---|
| `t01_expressions` | arithmetic, conversions, unsigned, `long long`, bitwise, compound assignment, `++`/`--`, comma, `?:`, casts |
| `t02_control_flow` | `if`, loops, `until`, `switch` with fall-through, `break`, `continue`, `goto` |
| `t03_booleans` | short circuit with side effects, comparisons as values, `!` |
| `t04_arrays` | 1-D to 3-D arrays, initializers, designators, strings, array parameters |
| `t05_pointers` | multi-level pointers, pointer arithmetic, `void *`, pointer to array |
| `t06_structs` | nesting, copies, by-value parameters and results, anonymous members |
| `t07_functions` | recursion, overloading, references, varargs, `static` locals, forward calls |
| `t08_classes` | default constructor order (base, members, body), single inheritance, static members, operators, arrays of objects |
| `t09_memory` | `malloc` family, a linked list |
| `t10_io` | `printf` formats, `scanf` (input in `t10_io.in`) |
| `t11_main_args` | `argc` / `argv` (arguments in `t11_main_args.args`) |
| `t12_lecture_examples` | the slides' examples, with the expected listing |
| `t13_review_cases` | cases the code review found wrong: `const T &` to another type, static member initializers, an inheritance chain, null base pointers, `va_list` passed on |
| `t14_optimizer` | constants, common subexpressions and copies next to the cases where reuse would be wrong: pointers, references, globals changed by calls |
| `t15_global_opt` | `-O2`: constants and copies across branches and loops, dead assignments, values that differ per path or are read through a pointer |
| `t16_runtime` | 64-bit arithmetic, int/float conversions, `printf` formats, structs and doubles through calls (aimed at the MIPS run-time library) |
| `t17_strings` | strings by hand: length, copy, compare, reverse, number ↔ text |
| `t18_algorithms` | bubble sort, quicksort, binary search, Hanoi, Ackermann, matrix product, sieve |
| `t19_scopes` | shadowing, nested blocks, `static` locals, globals |
| `t20_bits` | bit tricks, shifts, wrap-around of every integer width, signed/unsigned comparison |
| `t21_numeric` | `float` and `double`: Newton's method, series, rounding, mixed conversions |
| `t22_data_structures` | linked list, binary tree, stack, table of rows from `malloc`, pointers to pointers |
| `t23_objects` | three-level inheritance, objects inside objects, arrays of objects, operators returning references |
| `t24_references` | reference parameters and results, references to structs and pointers, `const` references |
| `t25_control` | state machine in a `switch`, nested loops, `goto` out of loops, `?:` chains, comma |
| `t26_declarations` | `typedef`, `sizeof`, struct layout, nested and designated initializers |
| `t27_object_semantics` | object rules of the reduced subset (D35): objects passed and returned by value are block copies, `?:` as an lvalue, arrays of objects built by the default constructor, a global object built before `main`, friends |
| `t28_o3` | `-O3`: inlining (side effects, references, by-value structs, several returns), tail calls with swapped arguments, loops (unrolled, or run zero times), a division that must stay, values reused or not across branches and stores |
| `t29_registers` | for the MIPS register allocator: values across calls and recursion, more live values than registers, arguments computed before a call, `char`/`short`/`bool` and `float`/`double` in registers, loops made of `goto` |
| `t33_brace_elision` | `struct { int a[2]; int b; } s = {1, 2, 3}` and friends, for globals (static data) and locals |
| `t34_float_formats` | `printf` `%e` `%E` `%g` `%G` next to `%f`: precision, width, flags, rounding into the next power of ten, zero, negatives, where `%g` changes style |
| `t35_loop_shapes` | `break`, `continue`, a `switch` inside a `while`, `do`-`while`, nested `for` at `-O3` (the program that hung global common subexpressions before D41; input in `t35_loop_shapes.in`) |
| `t36_enums_unions` | enums (switch, overloading, casts into an enum, `?:`) and unions read through another member than the one written, in a block, across blocks and calls, in arrays and by value, with 8-byte members (D42) |
| `t37_virtual` | virtual functions (D44): overriding at three levels with and without the keyword, an abstract base used through pointers, calls through pointers, references and `this`, qualified calls, a virtual call inside a base constructor, copies and assignments keeping each object's class, by-value parameters and results, a virtual operator, overloaded virtuals, arguments wider than `$a0`–`$a3`, a global object |
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
`logs/<file>.tac` without optimization and `logs/<file>.O1.tac`,
`.O2.tac`, `.O3.tac` with `-O1`, `-O2`, `-O3`. Each log is in sections:
a header (source, optimization level, instruction count), the
optimization summary (with `-O<n>`), the globals, one section per
function (its symbol table -- name, kind, type, width, offset -- then its
numbered code with labels), the semantic symbol table grouped by scope,
and the record layouts. Temporaries the optimized code no longer uses
are left out of a function's table (a line says how many).
`./run_tests.sh` keeps all four logs of every test program in
`phase3-ir/logs/`.

## Limitations

- Without an `-O` flag the output is deliberately unoptimized (decision D16).
- After optimization the symbol table still lists temporaries that are no
  longer used (the MIPS back end gives them no frame slot, D39).
- The interpreter's `free` does not reuse memory.
- A static initializer the generator cannot evaluate at compile time
  is reported as a code generation error (no code is produced).

## Next

Phase 4 turns this TAC into MIPS: [`../phase4-codegen/README.md`](../phase4-codegen/README.md).
