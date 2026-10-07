# Design Log

A running record of the decisions taken while building the back end:
what was decided, who decided it, why, and what was done as a result.
Newest entries are at the bottom. Open questions are listed at the end.

Reference material for this work:

- Course lectures 25–27 (Compiler Design CSC-305): symbol tables with
  offsets, three-address code for expressions (`E.place`, `E.code`,
  `newtmp()`, `gen`), flow of control, array addressing, type conversion,
  boolean expressions (numerical and short-circuit), backpatching.
- Aho, Lam, Sethi, Ullman — *Compilers: Principles, Techniques, and Tools*
  (the "Dragon Book"), chapter 6.
- N. Papaspyrou — *A Formal Semantics for the C Programming Language*
  (evaluation order, sequence points, conversions).

---

## 2026-10-07 — Session 1: scope reduction before TAC

### D1. Four advanced features are dropped

**Decided by:** the user.
**Decision:** remove these features from the language before the back
end is built:

1. `enum` and `union`
2. file manipulation (`FILE`, `fopen`, `fclose`, `fread`, `fwrite`,
   `fprintf`, `fscanf`, `fgets`, `fputs`, `feof`)
3. lambda functions
4. function pointers

**Why:** each of them needs its own machinery in TAC and MIPS (closure
conversion for lambdas, indirect calls for function pointers, a
run-time file layer, overlapping storage for unions); dropping them
keeps the back end focused on the features the project is graded on.

### D2. Dropped features are removed completely

**Decided by:** the user (option "Remove completely").
**Decision:** the keywords stop being reserved (`enum`, `union`, `FILE`,
`fopen` …, `mutable` become ordinary identifiers), the grammar rules,
AST node kinds, type kinds and semantic checks are deleted. A program
that uses a dropped construct gets an ordinary syntax error.
**Alternative rejected:** keeping the words reserved with a dedicated
"not supported" message (friendlier, but leaves stubs in every phase).

### D3. Affected tests are edited, not deleted

**Decided by:** the user.
**Decision:** about 40 of the 92 test programs use a dropped feature
beside features that stay. Only the dropped parts are cut out; a test
is deleted only when nothing else is left in it. One new invalid test
shows that each dropped construct is now rejected.

### D4. `auto` stays

**Decided by:** the user.
**Decision:** `auto x = 3;` (type deduction from the initializer) is
kept. It costs nothing later: semantic analysis replaces `auto` by the
real type before TAC sees the declaration.

### D5. Branch

**Decided by:** the user.
**Decision:** work happens on a new branch `tac`, created from `main`
after pull request #1 (the semantic phase) was merged. Feature removal
and TAC generation are separate commits. Nothing is pushed until asked.

### D6. How function pointers are rejected

**Decided by:** Claude (implementation detail of D1/D2 — say so if you
want it done differently).
**Decision:** a function is never a value; its name can only be called.

| Construct | Rejected by | Message |
|---|---|---|
| `int (*fp)(int);`, `int (*table[2])(int);`, `typedef int (*Op)(int);`, a parameter `int (*op)(int)` | parser (`direct_declarator` action) | `syntax error, unexpected '(' after a parenthesized pointer declarator` |
| a cast `(int (*)(int)) x`, `sizeof(int (*)(int))` | parser (the abstract-declarator rule is gone) | `syntax error, unexpected '('` |
| `x = f;`, `&f`, `*f`, `g(f)`, `if (f)`, `sizeof(f)` | semantic (`identifier()`) | `reference to function 'f' must be called (a function is not a value: function pointers are not supported)` |
| a parameter of function type, `int apply(int op(int))` | semantic (`resolveParams()`) | `parameter 'op' cannot have a function type` |
| `typedef int Fn(int); Fn *p;` | semantic (`resolveType()`) | `'p' declared as a pointer to a function` |

**Why this shape:** in C a function name "decays" to a pointer whenever
it is used as a value. Without function pointers there is nothing for it
to decay to, so the one place a bare function name can still appear —
the callee of a call — is resolved by `call()` directly, and every
other appearance reaches `identifier()` and is an error. `int (*pa)[3]`
(pointer to an array) is unaffected.
**Consequence for the back end:** every call in TAC has a callee known
at compile time (`call _Z3addii, 2`); there is no indirect call.

### D7. Consequences of "remove completely" found while implementing

Recorded so nothing here is a surprise later:

1. **File I/O leaves no syntax behind.** `FILE *f = fopen("a", "r");`
   is now the *expression* `FILE * f = fopen(...)` over plain
   identifiers, so it is not a syntax error; semantic analysis reports
   `undeclared identifier 'FILE'`, `'f'` and `call to undeclared
   function 'fopen'`. (The other three features do give syntax errors.)
2. **Anonymous unions went with `union`** — both the member form and
   the block-scope form (`union { int a; char b; };` in a function, with
   its hidden `__anon_union.N` object). **Unnamed structs and anonymous
   struct members stay** (`struct S { struct { int lo, hi; }; };`,
   `typedef struct { int x; } Pt;`).
3. **The former keywords are ordinary identifiers**: `int enum = 1;`,
   `struct FILE { int fd; };`, `int fopen(int mode)` are legal
   (`phase2b-semantic/test/valid/v23_former_keywords.c`).
4. **One scanner hack disappeared.** `[` used to need lookahead to tell
   a designator (`{[2] = 7}`) from a lambda (`[x](int a) {...}`). With
   no lambdas, `[` is an ordinary token and the `DESIG_LBRACKET` token
   and `bracketIsDesignator()` are gone.
5. **Tag checks simplified.** With only `struct` and `class` left there
   is no "declared as union, used as struct" mismatch and no "previously
   an enum" case.

### Progress — feature removal finished (2026-10-07)

What was changed, front to back:

| Component | Change |
|---|---|
| `shared/token` | 13 token kinds removed (116 → 103): `ENUM`, `UNION`, `FILE`, the nine file functions, `MUTABLE` |
| `phase2-parser` (`parser.y`, `scanner.l`) | `enum`/`union` rules, enumerator lists, nine file built-ins, lambda rules (captures, `mutable`, `-> T`), the function-type abstract declarator; grammar 1492 → 1267 lines, still **0 conflicts** (`%expect 0`) |
| `shared/ast` | 4 node kinds removed (60 → 56): `EnumDecl`, `Enumerator`, `UnionDecl`, `LambdaExpr` |
| `shared/types` | `TypeKind::Enum`, `TypeKind::Closure`, `EnumInfo`, `RecordKind::Union`, the `FILE` opaque type, union layout, closure → function-pointer conversion |
| `shared/symbol_table` | `UNION_TAG`/`ENUM_TAG`/`ENUM_CONST`, `SymbolKind::EnumConstant`, `ScopeKind::Lambda`, lambda-crossing in `lookup()`, anonymous-union promotion, `FILE`/closure mangling |
| `phase2b-semantic` | `enumDefinition()`, `lambda()` and all capture checking, anonymous-union objects, nine file built-in signatures, calls through values; the rules of D6 added |

In total 22 source files, about 1100 lines removed and 200 added.

Tests (decision D3):

| Suite | Before | After | Notes |
|---|---|---|---|
| Lexer | 11 | 9 | deleted `test8_file_manipulation`, `test10_lambda_functions` (nothing else in them); edited 2 |
| Parser | 37 | 36 | deleted `funcPtr`, `test22_syntax_errors_file_io`; edited 7 (3 renamed); added `test29_dropped_features` |
| Semantic, valid | 24 | 24 | edited 11 (2 renamed); `v23_anonymous_unions` replaced by `v23_former_keywords` |
| Semantic, invalid | 20 | 20 | edited 8 (1 renamed); `e19_anonymous_unions` replaced by `e19_dropped_features` |

The two new "rejected" tests are `phase2-parser/test/test29_dropped_features.c`
(11 dropped constructs, each a syntax error, followed by a valid `main`
that proves the parser recovered) and
`phase2b-semantic/test/invalid/e19_dropped_features.c` (the semantic
rules of D6).

Verification: clean rebuild of `shared`, `phase1-lexer`,
`phase2-parser`, `phase2b-semantic` with no compiler warnings and no
grammar conflicts; `phase2b-semantic/run_tests.sh` → **passed: 80
failed: 0** (44 semantic programs + the 36 parser programs end to end).
All `logs/` were regenerated. Documentation updated: `README.md`,
`docs/FEATURES.md`, `docs/SYMBOL_TABLE.md`, the phase READMEs,
`GRAMMAR_DESIGN.md` §3c/§4, three diagrams (feature map, symbol lookup,
repository layout); the archived `DEVELOPMENT_NOTES.md` files got a
note instead of a rewrite.

Committed on branch `tac` as `c73fc59` ("Drop enum, union, file
manipulation, lambdas and function pointers") on the user's go-ahead;
not pushed.

---

## 2026-10-07 — Session 2: TAC design

The course slides (Lectures 25–27) are the reference format. Where the
slides show one way, that way is used; where they show two, the user
chooses.

### D8. Instructions are quadruples

**Decided by:** the user ("how was it mentioned in the slides, do it
that way").
**What the slides do:** every rule creates a named temporary and emits a
statement that names its result — `E.place = newtmp()`,
`emit(E.place = E1.place + E2.place)` — and the statements live in a
numbered array ("labels are indices into this array", `goto state+3`).
An instruction with an operator, up to two operands and an explicit
result name, stored in an indexed array, is the **quadruple** form
`(op, arg1, arg2, result)`. Triples (results referred to by instruction
number, no temporaries) do not appear in the slides.
**Decision:** quadruples in one numbered array per function.

### D9. Boolean expressions: jumping code, and the slides' 0/1 pattern for values

**Decided by:** the user.
**Decision:**
- a condition (`if`, `while`, `for`, `do`-`while`, `until`, `?:`, the
  operands of `&&` `||` `!`) is translated by **flow of control**
  (Lecture 27, "short circuit evaluation"): `if a < b goto E.true`,
  `goto E.false`; `&&` and `||` generate no instruction of their own;
- when a boolean is needed **as a value** (`y = a < b;`, `f(a && b)`),
  it is materialised with the slides' relop pattern:

  ```
  110: if a < b goto 113
  111: t1 = 0
  112: goto 114
  113: t1 = 1
  114: y = t1
  ```

**Alternatives rejected:** a single `t1 = a < b` instruction for values
(shorter, maps to MIPS `slt`, but not in the slides); numerical
evaluation of every condition (`if t == 0 goto`, Lecture 26) — C
requires short-circuit for `&&`/`||` anyway.
**Note for later:** the optimizer may turn the 4-instruction pattern
into `slt` at MIPS level; the TAC stays in the lecture format.

### D10. TAC is generated by a walk over the annotated AST

**Decided by:** Claude (forced by the existing architecture — say so if
you disagree).
**Decision:** phase 3 is a separate pass over the AST that semantic
analysis has annotated; the slides' attributes become values computed
during that walk (`E.place` = the operand an expression function
returns, `E.code` = instructions appended to the function's quad array,
`E.true`/`E.false`/`S.next` = backpatch lists).
**Why not in the Bison actions (the slides' one-pass presentation):**
TAC needs each expression's type, the overload a call resolves to,
implicit conversions and record offsets. Those are computed by
`phase2b-semantic` *after* parsing (functions may be called before they
are declared, class members are visible in every method), so they do
not exist yet while the parser is reducing.

### D11. Jump targets: backpatching, printed with labels and numbers

**Decided by:** the user, after asking for the pros and cons.
**Decision:** jumps are generated with `makelist` / `merge` /
`backpatch` (Lecture 27); a target is an instruction index. When the
code is printed, every instruction that is the target of a jump also
gets a label (`L1`, `L2` …) and the instruction number stays visible:

```
100:      if a < b goto L1
101:      t1 = 0
102:      goto L2
103: L1:  t1 = 1
104: L2:  x = t1
```

**Why (the points that decided it):** the two options generate code
identically; with numbers only, every jump target has to be renumbered
whenever the optimizer deletes or moves an instruction and the
before/after listings stop lining up; MIPS needs labels anyway, and a
labelled instruction is exactly where a basic block starts.

### D12. Typed operators and explicit conversions, with exact types

**Decided by:** the user ("the first choice, but think about which one
is best for MIPS code generation").
**Decision:** every arithmetic and comparison instruction carries the
type it operates on, printed in the slides' notation (`int +` →
`int+`), and every conversion is its own instruction named
`<from>to<to>` (the slides' `inttoreal`):

```
100: t1 = i int* 2
101: t2 = inttodouble t1
102: t3 = d double+ t2
104: t4 = u uint/ 3
```

The slides have two classes, `int` and `real`. This language needs
seven machine classes: `int`, `uint` (32-bit), `llong`, `ullong`
(64-bit), `float`, `double`, and `ptr`. `char`, `short` and `bool` only
exist in memory: they are widened when loaded (`chartoint`) and narrowed
when stored (`inttochar`), as C's integer promotions say. `long` is
32 bits on MIPS32, so it is the class `int`.

**Why this is also the best choice for MIPS** (the user's question):
the MIPS instruction to emit is decided by exactly this information, so
with the type on the instruction the code generator is a table lookup
and needs no type inference of its own:

| TAC | MIPS |
|---|---|
| `int+` / `uint+` / `ptr+` | `addu` |
| `float+` / `double+` | `add.s` / `add.d` (coprocessor 1 registers) |
| `int/` vs `uint/` | `div` vs `divu` |
| `int<` vs `uint<` / `ptr<` | `slt` vs `sltu` |
| `int>>` vs `uint>>` | `sra` vs `srl` |
| `llong+` | two-word add with carry (`addu`, `sltu`, `addu`) |
| `inttodouble` | `mtc1` + `cvt.d.w` |
| `chartoint` / `uchartoint` | `lb` / `lbu` on load, or `sll`+`sra` / `andi` |

With the "two classes" listing the same facts would have to be stored
anyway and just not shown; with "plain operators + type table" the code
generator would have to look every operand up. Carrying the exact type
costs nothing and also lets the optimizer fold constants with the right
width and signedness (`wrapToType()`).

### D13. Arrays: the slides' offset formula with indexed instructions

**Decided by:** the user.
**Decision:** an element's byte offset is computed with the slides'
formula (`i × w`, and `((i1 × n2) + i2) × w` for row-major 2-D arrays;
`low` is always 0 in C) and used in the indexed instructions
`x = a[t]` and `a[t] = x`:

```
x = a[i];            m[i][j] = x;        (int m[3][4])

100: t1 = i int* 4   103: t3 = i int* 4      (n2 = 4)
101: t2 = a[t1]      104: t4 = t3 int+ j
102: x = t2          105: t5 = t4 int* 4     (w = 4)
                     106: m[t5] = x
```

Following from it (Claude's reading of the same rule — say so if you
want otherwise): the indexed form is used whenever the base is a named
object with storage, so a struct field is the same instruction with a
constant offset (`p.y` → `t1 = p[4]`); through a pointer the address is
computed and dereferenced (`q->y` → `t1 = q ptr+ 4`, `t2 = *t1`).
**Alternative rejected:** explicit addresses only (`t2 = &a`,
`t3 = t2 ptr+ t1`, `t4 = *t3`) — uniform, but longer, and it hides which
array is accessed, which the optimizer wants to know.

### D14. Calls: `param` / `call` / `return`, readable callee names

**Decided by:** the user (who also offered more reference material if
needed — may be taken up for the MIPS calling convention).
**Decision:** the slides do not cover calls; the Dragon book's
instructions are used: one `param` per argument, left to right, then
`call f, n` (or `t = call f, n`), and `return` / `return x`. A member
function receives the object's address as a hidden first argument
(`this`). The listing shows the callee's source-level signature; its
mangled link name is stored in the instruction and printed once in the
function's header:

```
100: t1 = y int* 2
101: param x
102: param t1
103: t2 = call add(int, int), 2
104: r = t2
105: t3 = &d
106: param t3            (this)
107: param 3
108: call Dog::bark(int), 2
```

Since function pointers were dropped (D6), every `call` names its
callee; there is no indirect call.

### D15. Destructors run automatically at scope exit

**Decided by:** the user ("Automatic at scope exit").
**Decision:** a local object of a class with a destructor (or with a
base or member that has one) is destroyed when its block is left, in
reverse order of construction, whichever way the block is left:

| Leaving by | What is emitted |
|---|---|
| falling out of the block's end | the destructor calls, as the block's last instructions |
| `return` | the return value is computed (and copied to a temporary if it is a local), then every open block's objects are destroyed, then `return` |
| `break` / `continue` | the objects of the blocks inside the loop or switch are destroyed before the jump |
| `goto` | the objects of the blocks the jump leaves; a jump backwards in the same block also destroys the objects declared after the label (they are constructed again when control passes their declaration) |

`for (Dog d; ...)` keeps `d` alive for the whole loop. Inside a
constructor the base and member constructors run first; a destructor
ends by destroying members and bases in reverse order. Class objects
with static storage (globals, `static` locals) are constructed when
`main` starts.

**Known limits (Claude's, flagged):** unnamed temporaries
(`Dog(4).bark();`, the result of `a + b`) and by-value class parameters
are not destroyed — doing that correctly needs copy elision; static
objects are not destroyed at program exit; `delete[]` frees the array
without calling element destructors (the element count is not stored).

### D16. The generator's output is kept raw

**Decided by:** the user.
**Decision:** the generator emits exactly what the slides' rules give,
including a `goto` to the next instruction and unfolded constant
arithmetic (`t1 = 8 uint+ 4`). Removing those is the `-O1` optimizer's
job, which then has honest before/after numbers.
Two things are *not* arithmetic folding and are done while generating:
a constant converted to another type is written in that type (`d > 0`
compares with `0.0`, no `inttodouble 0`), and a constant array index is
multiplied out (`arr[1]` is `arr[4]`).

### D17. Smaller choices made while writing the generator

**Decided by:** Claude — each is the conventional reading of the
slides or of C; say so if you want any of them changed.

- **One quad array per function**, numbered through the whole program
  from 100 (the slides' starting number); temporaries restart at `t1`
  in each function; labels `L1, L2 …` are unique program-wide.
- **Procedure symbol table (Lecture 25).** Every function is printed
  with its table: parameters, locals and temporaries with `type`,
  `width` and `offset`, and the total width — `enter(table, name, type,
  offset)` / `addwidth`. Offsets follow the MIPS32 sizes and alignment
  already used for record layouts.
- **Names.** A local prints under its own name when that is unambiguous
  in the function, otherwise under the symbol table's unique name
  (`x.7`), so two `i`s in different blocks cannot be confused.
- **`while`** is the Lecture 27 form: `S.begin: E.code ; E.true: S1 ;
  goto S.begin`. `until (c)` is the same with the true and false lists
  swapped. `for` runs its step where `continue` lands.
- **`switch`** evaluates the subject once into a temporary, jumps over
  the body to a test sequence (`if t == v goto Lcase` …, then `goto`
  the default), as in the Dragon book; `break` goes to the end.
- **Aggregate initializers** of locals become one store per element in
  address order, with `0` for elements the list leaves out (C's rule).
  Objects with static storage and constant initializers are data and
  appear in the `globals` table, not in code.
- **References** hold an address: `int &r = x` is `r = &x`, a use of
  `r` is `*r`, a reference argument passes `&x`.
- **Member access through `this`** is `this ptr+ offset` and `*`; a
  base class sub-object's offset is added when a derived object is used
  as its base (calls to inherited methods, `Base *p = &derived`).
- **Variable arguments** use three instructions of their own
  (`va_start ap, n`, `t = va_arg ap, int`, `va_end ap`); extra
  arguments get C's default promotions (`float` → `double`, `char` →
  `int`).
- **`new` / `delete`** are `malloc` / `free` plus the constructor or
  destructor call.

### Progress — TAC generator and interpreter working (2026-10-07)

What exists in `phase3-ir/` now:

| Piece | File | Size |
|---|---|---|
| IR data structures and the listing printer | `include/tac.h`, `src/tac.cpp` | ~400 lines |
| Generator: expressions | `src/gen_expr.cpp` | ~900 lines |
| Generator: statements, declarations, functions | `src/gen_stmt.cpp` | ~650 lines |
| TAC interpreter | `src/interp.cpp` | ~560 lines |
| Driver (`tac_generator`, `--run`, `-q`) | `src/main.cpp` | ~120 lines |

How it was checked, in the order it happened:

1. The slides' own examples (`a = b * -c + b * -c`, `while a < b`,
   `a < b or c < d and e < f`, `inttoreal`, array addressing) were
   generated and read against the slides; the listing is kept as
   `test/expected/t12_lecture_examples.tac`.
2. The generator was run over all 24 valid semantic test programs and
   the 24 valid parser programs: no crash, no jump left unpatched.
3. The interpreter was written (roadmap step 1: "TAC plus an
   interpreter as the correctness oracle"). It uses the MIPS32 data
   model, so a wrong offset or width shows up as a wrong result.
4. Twelve test programs were written to be valid C/C++ as well, so
   **gcc/g++ is the reference**: each was compiled with g++ (two with
   gcc in C mode, because g++ rejects their designated initializers),
   and the output and exit code of the native binary and of the
   interpreted TAC are identical for all twelve. Those outputs are
   stored in `test/expected/` and `./run_tests.sh` compares against
   them (**passed: 12 failed: 0**), so the suite does not need gcc.

One interpreter decision (Claude's): `free` does not reuse memory. It
makes use-after-free silently "work", but keeps the interpreter small;
it can be tightened if a test ever needs it.

Documentation updated: `phase3-ir/README.md` (rewritten), root
`README.md`, `docs/FEATURES.md` (the IR column is filled in),
`phase4-codegen/README.md`, the feature-map diagram.


Next on the agreed roadmap: basic blocks and the control-flow graph,
then the local optimizations behind `-O1` (constant folding, algebraic
simplification, copy propagation, common-subexpression elimination,
dead and unreachable code, jumps to the next instruction).

### Audit before the commit (2026-10-07)

**Asked by:** the user ("run the audit … to make sure of your honest
work"). Done as a code review of everything on the branch, with probe
programs run against g++ to look for wrong results rather than only
reading the code. It found ten things; all are fixed.

| # | What was wrong | Found by | Fix |
|---|---|---|---|
| 1 | `const double &` given an `int` variable read the int's bytes as a double | probe vs g++ (0.00 instead of 2.50) | a converted temporary when the types differ |
| 2 | `int Cnt::made = 5;` created a second, unrelated global; the static member stayed 0 | probe vs g++ | **semantic phase**: the out-of-class definition now defines the member |
| 3 | a block ending in a discarded `c ? f() : 0;` skipped its destructors | reading `block()`, then a probe | the block end counts as reachable when any jump targets it |
| 4 | a `va_list` passed to another function could not be read there | probe vs g++ | the interpreter lays the extra arguments out in memory; `ap` is a pointer |
| 5 | `delete` of a null pointer called the destructor | probe vs g++ | a null test around destructor and `free` |
| 6 | `A a(derivedObject)` copied the whole derived object into the base | reading the code | only the base sub-object is copied |
| 7 | a null `Derived *` became non-null when converted to a non-first base | reading the code | null test before adding the offset |
| 8 | a static initializer the generator could not evaluate silently became 0 | reading the code | `?:` and comparisons are evaluated; anything else is a code generation error |
| 9 | the feature matrix said "done" for things no phase 3 test covered | comparing docs with tests | `t13_review_cases` covers 1–8 and multiple inheritance |
| 10 | `floatText()` existed twice | reading the code | one definition (two one-line helpers are still repeated per file) |

After the fixes: `phase3-ir/run_tests.sh` **13 passed**,
`phase2b-semantic/run_tests.sh` **80 passed**, every phase builds
without warnings. Honest remaining limits are the ones listed under
D15 and in `phase3-ir/README.md`.

### Merged (2026-10-07)

Both commits of branch `tac` were pushed and merged into `main` through
pull request #2 (merge commit `1136ed4`), on the user's instruction.

### D18. MIPS target: the SPIM simulator

**Decided by:** Claude, at the user's request ("confirm which simulator
we will use and why") — the user can still overrule it.
**Decision:** generated MIPS runs on **SPIM**; the assembly is kept to
the system calls and directives that MARS also accepts, so it can be
shown in MARS/QtSpim as well.

| | SPIM | MARS | MIPS Linux (cross gcc + qemu) |
|---|---|---|---|
| Install here | `sudo apt install spim` (in Ubuntu's repository) | needs Java (not installed) and a manually downloaded jar | two toolchain packages |
| Run from a script | `spim -file prog.s` | `java -jar Mars.jar nc prog.asm` | `qemu-mipsel ./prog` |
| printf / scanf / malloc | system calls + a small run-time written in MIPS | the same | the C library, for free |
| What must be exactly right | our own conventions | our own conventions | the full o32 ABI (varargs, struct passing, double alignment), or libc calls crash |
| Fits a course demo | the textbook simulator (Patterson & Hennessy) | also common | not a simulator |

**Why SPIM:** it installs with one command, runs from the command
line (so `run_tests.sh` can compare its output with the TAC
interpreter's automatically), has no delayed branches by default, and
is the simulator the standard textbook uses. **Cost:** there is no C
library, so `printf` formatting (`%5.2f`, `%lld`), `scanf` and
`malloc`/`realloc` are a run-time library we write in MIPS on top of
the print/read/`sbrk` system calls.
**Needed from the user:** `sudo apt install spim` (Claude cannot run
`sudo`).

---

## 2026-10-08 — Session 3: optimization

### D19. Order of the remaining work: `-O1`, `-O2`, then MIPS

**Decided by:** the user. Claude had recommended MIPS before `-O2`
(the required deliverable before the open-ended part); the user chose
to finish all optimizer work first. Both orders are technically fine:
optimizations work on TAC and are verified by the interpreter.

### D20. Common subexpressions by value numbering

**Decided by:** the user, conditionally: "choose the DAG if it is
computationally easier".
**Decision:** value numbering — because the honest answer to the
condition is that the explicit DAG is *not* the easier one. Building
the graph is easy, but the block then has to be regenerated from it
(choosing an order, choosing which of several names keeps a value);
value numbering does the same analysis in one pass over the block with
a hash table and rewrites instructions in place. The two are the same
idea: a value number **is** a DAG node, and the Dragon book itself
builds DAGs this way (section 6.1.2, "the value-number method").
**What is given up:** there is no DAG picture to print. If the course
slides, when they arrive, require showing the DAG, a printer over the
value-number table can be added.

### D21. What `-O1` contains, and how it is known to be right

**Decided by:** Claude (the list is the roadmap's; slides not available
yet, the Dragon book chapters 8.4–8.5 are followed).

- per basic block: constant folding, algebraic simplification, copy
  and constant propagation, common subexpressions (including repeated
  `&x`, `a[i]`, `*p`);
- per function: merging `t = e ; x = t`, removing dead temporaries,
  jump clean-up, unreachable code.

**Constant folding uses the interpreter's own arithmetic functions**
(`evalArithmetic`, `evalConvert`, `evalCompare`), so a folded result is
by construction what executing the instruction would have produced —
there is one definition of `int` wrap-around, not two.
**Safety rule:** anything read from memory is forgotten at a store
through a pointer, an array/field store, a call, or an assignment to a
global or address-taken variable; `volatile` is never remembered;
floating-point identities that are not exact are not applied.

**How you can see it:** `./tac_generator -O1 file.c` prints a summary
(instructions before → after, a count per optimization) and the
optimized listing; with `--run` it executes the program both ways,
refuses to continue if they differ, and prints the instructions
executed by each.

### Progress — `-O1` working (2026-10-08)

- `phase3-ir/src/opt.cpp` (about 480 lines), `-O1` flag in the driver.
- `./run_tests.sh` now runs every program raw **and** with `-O1`
  against the same expected output: **14 passed, 0 failed**; executed
  instructions drop by 6% to 42% per test.
- A new test, `t14_optimizer`, is built around the traps: values
  changed through pointers, references, calls and globals, `volatile`,
  `-0.0`, a division that must not be folded.
- That test caught a real bug in the first version: a simplified
  instruction lost its operand (`t15 = _`) because the rewrite reset
  the instruction before copying the operand out of it. Fixed.
- `-O1` was also run over the other suites' programs: 45 programs run
  to completion with identical output and exit code before and after.
- Not addressed at `-O1`, by design: assignments to named variables
  that are never read again stay (removing them needs liveness across
  blocks — `-O2`).

### D22. What `-O2` contains

**Decided by:** the user, choosing from four candidates.
**In:** dead assignment elimination (live-variable analysis) and global
constant and copy propagation.
**Out:** global common subexpressions and loop optimizations
(invariant code motion, induction-variable strength reduction). They
can be added later as further passes over the same flow graph.

**How they are done (Claude):** one flow graph per function (blocks
from the same leader rule as `-O1`, edges from jumps and fall-through);
propagation is a forward analysis whose meet keeps only the facts all
predecessors agree on, with nothing known at the entry; liveness is the
usual backward analysis, nothing live at the exit. Both restrict
themselves to scalar locals whose address is never taken, so pointers,
globals and calls cannot invalidate a fact. After each pass `-O1` runs
again; the whole thing repeats until nothing changes.

### Progress — `-O2` working (2026-10-08)

- `opt.cpp` grew by about 200 lines; flag `-O2`.
- `./run_tests.sh` runs every program raw, with `-O1` and with `-O2`:
  **15 passed, 0 failed**. Executed instructions: `-O1` 6–42% fewer,
  `-O2` 7–64% fewer.
- New test `t15_global_opt`: facts that hold on every path versus
  values that differ per path, loop-carried variables, a variable read
  only through a pointer, a call whose result is unused.
- `-O2` over the other suites: 45 programs run to completion with
  identical output and exit code.
- Twice a new test "failed" because the **test** was wrong, not the
  compiler: `printf("%d %d", f(), g)` where `f` changes `g` — C leaves
  the order of argument evaluation unspecified, and g++ and this
  compiler legitimately differ. Both tests were rewritten to use
  separate statements.

---

## Open questions

*(none at the moment — say so if your course requires MARS or QtSpim instead of SPIM)*
