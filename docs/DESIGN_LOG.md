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
it can be tightened if a test ever needs it. (Superseded by D45: both
back ends now reuse freed memory.)

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

## 2026-10-08 — Session 4: MIPS design

SPIM 8.0 is installed (`/usr/bin/spim`); a hand-written program run
with `spim -file` printed correctly and returned its exit code through
the `exit2` system call, so MIPS output can be tested by script.

### D23. `printf` / `scanf`: a run-time routine written in MIPS

**Decided by:** the user.
**Decision:** SPIM has no C library, so `printf` is one MIPS routine
that walks the format string at run time: `%d %u %x %o %c %s %f %%`
with width, precision, the `-` and `0` flags and the `l` / `ll`
lengths. `scanf` is done the same way over the read system calls.
`%e` and `%g` are not supported.
**Alternative rejected:** expanding a literal format into separate
print system calls at compile time — little code, but widths and
precision would be lost and several tests would stop matching gcc.

### D24. `long long`: full support with run-time helpers

**Decided by:** the user.
**Decision:** a `long long` occupies two words; add, subtract,
compare, bitwise operations and conversions are generated inline;
multiply, divide, remainder and shifts call run-time routines.

---

### D25. MIPS calling convention: everything on the stack

**Decided by:** the user, after asking why it was recommended.
**Decision:** all arguments are passed on the stack (first argument at
the lowest address), the result comes back in `$v0` / `$v0:$v1` /
`$f0`, the caller removes the arguments.
**Why:** it maps one-to-one onto `param` / `call`; with every value in
the frame anyway, register arguments would be stored to memory at once;
the o32 convention's special cases (doubles after ints, structs split
across registers, variadic home area, `long long` register pairs) buy
nothing on SPIM, where no foreign code is ever called; and `va_arg`
becomes "read and advance".
**Cost, accepted:** more instructions per call, and it is not the
textbook `$a0`–`$a3` convention. Passing the first integer arguments
in `$a0`–`$a3` can be added with register allocation.

### Progress — MIPS generation working on SPIM (2026-10-08)

- `phase4-codegen/`: `src/mips.cpp` (about 620 lines), the run-time
  library `runtime/runtime.s` (about 800 lines of MIPS: `printf`,
  `scanf`, allocation, 64-bit helpers), driver `mips_generator`.
- `phase4-codegen/run_tests.sh` compiles every test at `-O0`, `-O1`,
  `-O2`, runs it in SPIM and compares with the gcc-verified expected
  output: **16 passed, 0 failed**. 14 of the 15 programs passed on the
  first complete run.
- What had to be fixed after that:
  - `%f` printed `2147483648.0` for larger values and rounded `3.375`
    to `3.37`; the routine now scales to a 64-bit integer and rounds to
    nearest-even, which is what glibc prints.
  - `%zu` was not understood (`z` is now accepted).
  - `%e` is not implemented (as decided in D23), so it was removed from
    test `t10_io`.
  - **A generator bug that the interpreter had hidden:** `1[a]` and
    `"literal"[2]` produced wrong addresses. The interpreter read
    garbage without faulting; SPIM raised an address error. Fixed in
    `indexLValue()`, and both forms are now in `t04_arrays`.
- Wider check: the 45 runnable programs of the semantic and parser
  suites, compiled at `-O0` and `-O2` and run in SPIM — 90 runs, all
  identical to the TAC interpreter.
- New test `t16_runtime` for the run-time library.

### D26. The programs are run in QtSpim

**Decided by:** the user ("shift to qtspim").
**What it changes:** QtSpim 9.1.21 is installed and is what the user
runs and demonstrates with. It is the same simulator as the
command-line `spim` with a window, and it has no batch mode, so:

- the automated tests keep using command-line `spim` (they have to run
  unattended); the generated file is the same for both;
- `scanf` no longer reads file descriptor 0 with the `read` system
  call — QtSpim's console cannot feed that. It now takes input a line
  at a time with `read_string`, which the terminal and the QtSpim
  console both serve; end of input is still detected (`scanf` returns
  -1), checked with a `while (scanf(...) == 1)` loop;
- the run-time library uses only system calls both versions have.

**Not verified by Claude:** an actual run inside the QtSpim window
(it cannot be driven from a script). The steps are in
`phase4-codegen/README.md`; the user's first run there is the check.

Remaining on the roadmap: register allocation and a peephole pass.

### Second audit: are the semantic phase and IR generation finished? (2026-10-09)

**Asked by:** the user ("increase the number of test cases and re-run
the code review so that I can see exactly whether we finished the
semantic phase and the IR generation phase").

**What was done**

- 10 new test programs (`t17`–`t26`: strings, algorithms, scopes, bit
  manipulation, floating point, data structures, class hierarchies,
  references, control flow, declarations), each compared with g++.
- 85 short probe programs for the semantic phase: 40 valid ones to
  look for false errors, 45 invalid ones to look for missed errors.
- A code review of `phase2b-semantic` and `phase3-ir`.

**What the probes say about the semantic phase**

- All 40 genuinely invalid programs were rejected. The 5 "invalid"
  probes that were accepted are programs C itself accepts (division
  by a constant zero, array index out of range, a missing `return` —
  each already gets a warning — plus an uninitialized read and a null
  dereference, which need flow analysis).
- Of the 40 valid programs, 2 were wrongly rejected (both fixed, see
  below); 9 more are rejected because they use features this language
  does not have (templates, namespaces, `virtual`, default arguments,
  member-initializer lists, `const` member functions, pointers to
  members, implicit `int`).

**Findings and what happened to them**

| # | Phase | Finding | Outcome |
|---|---|---|---|
| 1 | IR | a class object passed or returned by value was copied byte by byte; the copy constructor was never called | **fixed** (a returned local and a temporary are not copied, as in g++) |
| 2 | semantic | `Vec v = other;` with a converting constructor overwrote the initializer's symbol; the generated code failed | **fixed** (the constructor is stored separately, `ASTNode::converter`) |
| 3 | semantic | `c ? a : b` was never an lvalue, so `int &r = c ? a : b;` was rejected | **fixed**, with pointer-selecting TAC for it |
| 4 | semantic | `const Row r` (a typedef'd array) lost `const` on its elements | **fixed** |
| 5 | parser | `obj.Base::member()` is a syntax error | **left open** — needs a grammar rule plus lookup changes; a base pointer reaches the same member |
| 6 | IR | unnamed class temporaries are never destroyed | **left open** (needs copy elision to do correctly; D15) |
| 7 | IR | `delete[]` did not call element destructors | **fixed** (the count is stored in front of the block) |
| 8 | IR | static objects were not destroyed when `main` returns | **fixed** |
| 9 | semantic | reading an uninitialized local is not diagnosed | **left open** (no flow analysis in the semantic phase) |
| 10 | IR | two one-line helpers were repeated per file | **fixed** |

**Answer to the question.** For the language as it is defined now, both
phases do what they are meant to do on everything tested: 82 semantic
checks, 27 programs through the TAC interpreter at three optimization
levels and through SPIM at three levels, all equal to g++. What is
knowingly not done is the three open rows above plus the features
listed as unsupported in `docs/FEATURES.md`. "Finished" cannot be
proved by tests — each of the two audits found real defects that the
existing tests had not — so the honest statement is: no known wrong
result remains, and the open items are listed.

Test totals after this session: semantic 82 (25 valid, 21 invalid, 36
parser programs end to end), TAC 27, MIPS on SPIM 27.

---

## 2026-10-10 — Session 5: more TAC optimizations

### D27. `-O3`: TAC-level optimizations before the MIPS-level ones

**Decided by:** the user ("first let's do TAC level optimisations, then
go for MIPS level"), from the list Claude proposed.
**Decision (the level is Claude's choice):** they are a new level,
`-O3`, so that the `-O1` and `-O2` listings stay as they were.

| Optimization | Status |
|---|---|
| inlining of small functions | done: at most 16 instructions, not recursive, not variadic, one level per run |
| tail recursion → jump | done: only when no local's address is taken |
| common subexpressions across blocks | done: available expressions with the holding name |
| loop-invariant code motion | done: natural loops from dominators; never a division |
| store-to-load forwarding | done, inside `-O1`'s block pass |
| strength reduction of induction variables | **not done**: `-O1` already turns `i * 4` into a shift, so replacing it by a running add removes no instruction at this level; it can pay at MIPS level and is noted there |

**Safety conditions worth knowing**
- Inlining copies the callee's parameters, locals and temporaries into
  fresh temporaries of the caller, so a by-value struct stays a copy
  and a side effect in the callee still happens once per call.
- A moved instruction is pure, its operands are not assigned in the
  loop, and its result is assigned nowhere else in the function; so it
  is safe even if the loop body runs zero times. Divisions stay.
- A tail call becomes a jump only if the function takes the address of
  none of its locals (an address passed down would outlive the "call").

### Progress — `-O3` working (2026-10-10)

- `opt.cpp` grew by about 380 lines; flag `-O3` in both drivers.
- Both runners now include `-O3`: `phase3-ir/run_tests.sh` **28
  passed**, `phase4-codegen/run_tests.sh` (SPIM, four levels) **28
  passed**. Executed instructions: `-O2` 8–64% fewer, `-O3` 12–64%
  fewer; the class-heavy tests gain most (t08 8% → 33%, t23 11% → 42%)
  because constructors, getters and operators are inlined.
- New test `t28_o3` with a trap for each optimization.
- `-O3` over the other suites: 46 programs, interpreter and SPIM, no
  difference from unoptimized.

Next: MIPS-level optimizations (register allocation, immediate
operands, peephole).

### D28. Registers by usage count

**Decided by:** the user, from three options (usage counts, linear
scan, graph colouring).
**Decision:** the Dragon book's simple method (8.8): per function, the
names with the highest weighted use count — a use in a loop counts ten
times per nesting level — get `$s0`–`$s7` for the whole function.
**Why:** callee-saved registers survive calls, so nothing changes at a
call site; the method is a few dozen lines and easy to explain.
**Known ceiling:** a name holds its register for the whole function;
short-lived temporaries of an inner loop can take all eight. Linear
scan over live intervals is the upgrade.

### Progress — MIPS-level optimizations working (2026-10-10)

In `phase4-codegen/src/mips.cpp`, switched on by `-O1` and above
(`--stack-only` switches them off for comparison):

- registers by usage count, saved and restored by the function;
- immediate operands (`addiu`, `andi`, `sll` …), `$zero`, constant
  offsets as displacements;
- `slt` for a comparison used as a value;
- leaf functions do not save `$ra`;
- a peephole pass over each function's instruction list.

Result: `phase4-codegen/run_tests.sh` (28 programs × `-O0`…`-O3` in
SPIM) **28 passed** on the first run; 92 further SPIM runs from the
other suites (`-O1` and `-O3`) identical to the TAC interpreter. The
generated functions are 15–30% shorter than the stack-only code at the
same TAC level (table in `phase4-codegen/README.md`).

**Not measured:** instructions *executed* in SPIM — the simulator does
not report a count; the figures are static instruction counts.

### D29. The three limits of the first register allocator

**Asked by:** the user ("work on those limitations … finish it and
merge"). What was done about each:

| Limit | Outcome |
|---|---|
| A name kept its register for the whole function, so inner-loop temporaries could take all eight | **Fixed.** Each name now has a live interval (first to last occurrence, widened over every loop it reaches into, and up to the call for a `param`); names whose intervals do not overlap share a register. Still ordered by use count, so the method stays the one chosen in D28, with intervals added. |
| `float`, `double`, `long long` and narrow integers always stayed in the frame | **Fixed for all but `long long`.** `float`/`double` use `$f20`–`$f30` (saved and restored like `$s0`–`$s7`); `char`/`short`/`bool` use the integer registers and are re-extended after every write. `long long` stays in the frame — a deliberate skip (register pairs, rarely hot). |
| Never run inside the QtSpim window | **Still not verified by Claude.** QtSpim has no batch mode, and an attempt to start it without a window failed (its Qt build only has the `xcb` display plugin). The steps are in `phase4-codegen/README.md`; this needs one run by the user. |

**Result:** `phase4-codegen/run_tests.sh` 29 passed (29 programs ×
`-O0`…`-O3`); new test `t29_registers`. Code size with registers fell
again, for example `t04_arrays` 609 → 470 and `t22_data_structures`
835 → 612 instructions.

**Something the wider check showed.** Two older test programs
(`v19_former_limitations`, `test25_functional_casts_and_lookahead`)
gave a different exit code with registers. They read two variables
that were never assigned (`a` and `m`): in the frame that happens to be
0, in a register it is whatever was there. That is undefined in C, not
a compiler bug; the two programs now initialize the variables. It is
also a reminder that the open item "no warning for an uninitialized
read" matters more once values live in registers.

### Merged (2026-10-10)

On the user's instruction the stacked pull requests #3 (optimizer),
#4 (MIPS), #5 (`-O3`) and #6 (MIPS-level optimizations) were merged
into `main` by merging #6.

### QtSpim run confirmed (2026-10-10)

The last open point of D26 / D29 is closed: the user loaded
`t29_registers` (compiled with `-O3`) in the QtSpim 9.1.21 window and
the Console showed the same output as command-line `spim` and g++.
One practical note from that run: QtSpim's file dialog opens in the
home folder, so write the `.s` file somewhere under it rather than
`/tmp`.

### D30. The four items left open by the second review (2026-10-10)

The user asked for the four open items to be fixed before closing
pull request #7. No new question was put to the user: each item had
one behaviour to match (g++), so the choices below are about how.

| Item | Decision | Why |
|---|---|---|
| `obj.Base::member` was a syntax error | Two grammar rules, `postfix '.' TYPE_NAME '::' IDENTIFIER` and the `->` form (no new conflicts, `%expect 0` holds). The qualifier is stored on the member node; semantic analysis checks it names the object's class or a base and looks the member up there. TAC needed no change. | The existing base-offset code already handles a member that belongs to a base. |
| Unnamed class objects were never destroyed | A list of the objects made while one full expression is translated; destroyed in reverse at the end of the full expression, removed from the list when the object becomes a variable, an element, the function result or the target of a reference. By-value class parameters are copies destroyed after the call. | It is the C++ rule, and the output now equals g++'s destructor for destructor (`t30_temporaries`). |
| ...and `return local;` destroyed the local it had just returned | The local is treated as the result itself only when every `return` of the function names it and it is declared in the outermost block. Otherwise it is copied out and destroyed. | That is exactly when g++ 13 (the reference compiler here) elides the copy; anything else would print different constructor / destructor lines. |
| No warning for reading an uninitialized variable | A warning from liveness on the unoptimized TAC: a tracked local that is live at the function's entry. Printed by `tac_generator` and `mips_generator`. | The semantic phase has no flow graph; the optimizer already had liveness, so this is about 30 lines. It is flow-sensitive (no warning when every path assigns first). |
| `long long` never in registers | A `long long` takes two integer registers when two are free over its interval. Arithmetic reads the pair in place and builds the result in scratch registers. | Smallest change that is always correct when the result is also an operand. |

**Known ceilings, on purpose.** A temporary inside a condition dies
before that test's jump rather than at the end of the whole condition.
The uninitialized warning covers scalars whose address is never taken,
not arrays, objects or anything behind a pointer, and
`semantic_analyzer` alone does not print it.

**Result:** semantic 84 passed (new `v26`, `e22`), TAC 31 passed (new
`t30_temporaries` and the warnings check `diagnostics/uninitialized`),
SPIM 30 passed at `-O0`…`-O3`.

### D31. Feature audit: what the language does not need (2026-10-10)

The user asked for an audit of the feature list ("we do not need some
features like new and delete because I can run on malloc and calloc")
and for anything unnecessary to be removed. Every feature was checked
against the project specification, the number of test programs using it
and what it costs in the compiler. Everything in the specification's
Basic and Advanced lists stays. Three questions were put to the user.

| Question | User's answer | Consequence |
|---|---|---|
| Remove `new` / `delete` / `delete[]`? | **Remove** | Dynamic memory is `malloc` / `calloc` / `realloc` / `free`. A class object on the heap gets no constructor call (`malloc` runs none), so it is set up by an ordinary method; objects with constructors are locals, globals, members and array elements. Gone: the tokens, the `new_type_id` grammar and its precedence level, `NewExpr` / `DeleteExpr`, the semantic checks, and in TAC the element-count header of `new T[n]` with the destructor loop of `delete[]`. |
| Which no-effect keywords go? (`register`, `volatile` + `long double`, `auto`, `extern`) | **`register`, `volatile`, `long double`** | `register` did nothing (the allocator decides by use count, D28). `volatile` only switched optimizations off; the `isVolatile` flag is gone from types, symbols, mangling, the optimizer and the register allocator, and `qualified()` now takes one flag. `long double` was a second spelling of `double` and is now an invalid combination of specifiers. `auto` and `extern` stay. |
| How much of the C++ side stays? | **All of it** | Classes, inheritance, constructors / destructors, function and operator overloading and name mangling are unchanged. |

Kept without a question, because removal would only cost work:
`long long` (the `%f` run-time needs the 64-bit helpers anyway), the
preprocessor (the tests need `#include` / `#define` to compile under
g++ for checking), `const`, casts, `sizeof`, `?:`, the comma operator,
designated initializers, unnamed structs, binary literals.

Like the first batch (D1–D6), the four words are ordinary identifiers
again, so a use is a syntax error (`test29_dropped_features.c`
[12]–[15]). Nineteen test programs that used them were rewritten with
`malloc` or local objects; the seven TAC programs among them print
exactly what they printed before (checked again with g++ / gcc).

**Check of the first batch.** At the user's request the four features
dropped on 2026-10-07 were verified again: no token, grammar rule, type
or check for `enum`, `union`, file I/O, lambdas or function pointers is
left in the sources, and twelve probe programs (definitions, variables,
`fopen` / `fgets`, both lambda forms, function-pointer variables,
parameters, typedefs, members and decay) are all rejected.

**Also corrected:** the feature table in the root `README.md` still
showed TAC and MIPS as "not started" for every feature and listed both
under "Planned". It now shows what is implemented.

**Result:** semantic 84 passed, TAC 31 passed (raw and `-O1`…`-O3`),
SPIM 30 passed at `-O0`…`-O3`.

### D32. The last partial features (2026-10-15)

The user asked for the six remaining partial features of
`docs/FEATURES.md` to be finished and merged. One of them had a real
design choice, which was put to the user; the rest follow g++.

| Feature | Decision | Why |
|---|---|---|
| `virtual` (asked) | **vtable + indirect call** (user's choice over a switch on a class number). One new TAC form, `t = call *t2, n`; the interpreter maps function addresses back to functions, MIPS uses `jalr`, the optimizer treats it like any call (memory barrier, never inlined). Entries are (address, this-adjustment) pairs instead of Itanium thunks. | The standard technique; the pair form handles multiple inheritance without generating thunk functions. |
| Table pointers | At offset 0 of every polymorphic object, shared with the first base when it is polymorphic, else a slot of its own before the bases; stored by constructors after the bases, re-stored at the start of a destructor, by every copy (slicing), and kept by assignment. | Matches C++ behaviour during construction/destruction and for `Base b = derived;` / `b = derived;`. |
| `virtual ~T()` | Accepted; never dispatched. | Without `delete` (D31) an object is always destroyed where its exact class is known. |
| Abstract classes | Variables, members, temporaries, by-value parameters and returns of an abstract type are errors; a pure slot in a table is 0. | C++ rules. |
| Member initializer lists | Bases and members built in declaration order from the list, everything else default-constructed (and must be default-constructible); reference members now work, accessed through their stored address. | C++ rules; reference members needed the extra dereference to be usable at all. |
| `const` member functions | Part of the function type (`f()` and `f() const` overload), mangled `_ZNK...`; on a const object only const members can be called, otherwise the non-const overload wins; inside one, `this` is `const T *`. | C++ rules, g++'s mangling. |
| `friend` | `friend` functions (declared or defined in the class, but file-scope functions) and `friend class X;` may use private and protected members. | C++ rules. |
| `explicit` | Explicit constructors take no part in implicit conversions (copy-initialization, arguments, returns). | C++ rules. |
| Converting constructors for arguments and returns | A new rank, `UserDefined`, between standard conversions and `...`; at most one per argument; the chosen constructor builds a temporary (destroyed after the call, like a by-value parameter). | C++ overload ranking. |
| Slicing | A derived object may initialize, be assigned to, or be passed as its base; only the base part is copied. | Found while testing virtual functions: it was rejected before. |
| Brace elision into struct members | Semantic analysis rewrites a list into fully braced form (`elideBraces()`); the TAC generator lost its own array-only elision path. | One implementation of the C rule instead of two partial ones. |
| Flow checks | In the semantic phase: "control reaches end of non-void function on some path" (warning), "code will never be executed" (warning), a `goto` or `case` jumping into the scope of an initialized variable (error, as g++). Skipped in a function that already has errors. | g++'s behaviour; the warnings are structural (a constant condition is the only one evaluated). |
| Token_Type of member names | `aggregateOf()` follows any postfix expression back to its struct/class tag. | Was limited to a plain identifier before. |
| Lexer columns | `YY_USER_ACTION` tracks the column of every token; diagnostics print `Line N:C`. | The parser's scanner already did. |

**Known ceilings:** no covariant return types, `override` / `final`,
or virtual inheritance; a member inherited from a base keeps
`IDENTIFIER` in the parser's Token_Type table.

**Result:** semantic 87 passed (new `v27`, `e23`, parser `test30`), TAC
34 passed (new `t31_virtual`, `t32_class_features`, `t33_brace_elision`,
expected output from g++ / gcc), SPIM 33 passed at `-O0`…`-O3`.

### D33. `%e` and `%g` in the MIPS `printf` (2026-10-25)

The user asked for the two formats left out in D23. `runtime.s` now has
`%e`, `%E`, `%g` and `%G` with the same flags, width and precision as
`%f`. The `%f` digit generation became a routine of its own
(`__pf_fixed`) that all three use; `%e` normalizes the value to one digit
before the point (repeated division or multiplication by 10, then a check
whether rounding carries it to 10, as in `9.9999996` -> `1.000000e+01`)
and writes `e+XX` (at least two digits) after the mantissa; `%g` takes
the `%e` style when the exponent is below -4 or not below the precision,
otherwise `%f` with precision - 1 - exponent decimals, and removes
trailing zeros and a lone point. Checked against gcc on 140 values
(new test `t34_float_formats`). Same ceiling as `%f`: the scaled value
must stay below about 9·10¹⁸.

### D34. No preprocessor (2026-11-21)

The user asked to remove the preprocessor and chose that any line
starting with `#` is an error (rather than silently skipping it). The
shared `preprocessor` module is deleted. Both scanners report
`preprocessor directive '#include' is not supported` and skip the rest
of the line, so one directive gives one message instead of a cascade of
syntax errors. `printf`, `scanf`, `malloc`, `free` and `va_list` were
always built into the language, so programs lose nothing by dropping
`#include`. The drivers read the source through `openSource()`
(diagnostics module), which keeps the lines for carets and for the
scanner's lookahead; the line-origin map the preprocessor kept is gone,
since every position is now a line of the file as written.

Tests: every `#include` line was removed from the test programs, the
macros in `t26` and parser `test2` were inlined, and the five
preprocessor-only tests were replaced by `e16_no_preprocessor`.

### D35. A smaller C++ subset (2026-11-21)

The user asked to remove most C++ class features and keep the rest
simple. Decisions taken with the user:

| Feature | Now |
|---|---|
| Constructors | Only the default constructor `T()` (one per class, no parameters, no initializer list). `T x(other)` with an object of the same class, `T x = other`, by-value arguments and returns copy the object's bytes: there are no copy constructors |
| Destructors | Removed; `~T()` is a syntax error |
| Temporary object lifetime | Removed with destructors (nothing runs at the end of a full expression) |
| Const member functions | Removed (`int f() const` is a syntax error); a const object can only call static members |
| Nested and local classes | A `class`, or a struct with member functions, a constructor or a base, may not be defined inside a class or a function. Plain C data structs may still nest, as in C |
| Lazily built static locals | A `static` local whose class runs a constructor is an error |
| Inheritance | Single inheritance only: at most one direct base, chains allowed |
| Object slicing | A derived object may not be copied, assigned or passed by value as a base object; pointers and references still convert |
| Virtual functions | Removed with everything that served them: override detection, vtables, vptrs, dynamic dispatch (`call *t`, `jalr`), this-adjustment, abstract classes, `= 0`, virtual destructors and operators |
| `explicit`, converting constructors | Removed |

`virtual` and `explicit` stay reserved words so the scanner can name
them in its error; `~T()`, `int f() const`, `T() : x(1)` and `= 0` are
syntax errors. Friends, access control, static members, operator
overloading, function overloading and references are unchanged.

In the TAC generator this deleted the scope/destructor machinery
(`destroyScopes`, temporaries, `scanLabels`), the vtable code, copy
constructors, slicing and converting-constructor paths. With single
inheritance and no vptr a base always sits at offset 0, so `this` is the
object's address with no adjustment.

Tests: semantic `v10`, `v17`, `v19`, `v21`, `v25`, `v27`, `e09`, `e14`,
`e15`, `e23` rewritten, `e24_removed_keywords` added; parser `test7`,
`test24`, `test25`, `test30` rewritten, `test31_dropped_class_features`
added; TAC `t08`, `t13`, `t23`, `t27` rewritten (expected output from
g++), `t30_temporaries`, `t31_virtual`, `t32_class_features` deleted.

### D36. Loop-invariant code motion removed (2026-11-21)

At the user's request `-O3` no longer hoists invariant computations out
of loops (`hoistInvariants()` deleted). The dominator and natural-loop
analysis (`loops()`) stays, for the loop unrolling planned next.

### D37. Run-time checks and the assignment warning (2026-11-21)

- **Assignment as a condition:** `if (a = b)`, loops and `?:` warn
  `assignment used as the condition`. As in gcc, an extra pair of
  parentheses (`if ((a = b))`) says the assignment is meant: the parser
  marks a parenthesized expression (`ASTNode::parenthesized`, added
  2026-11-24) and the warning skips it.
- **Division by zero:** the MIPS code checks the divisor of every
  integer `/` and `%` (not a nonzero constant), and `__udivmodll` checks
  it for `long long`. On zero it prints the interpreter's message,
  `run-time error: division by zero`, and exits with code 2.
- **Deep recursion:** SPIM's stack grows by doubling and stops 256 KB
  below 0x80000000 (8045 nested 32-byte frames fit, 8046 do not). Every
  function that calls, or whose frame exceeds 4 KB, compares `$sp` with
  `__stack_limit` (16 KB above that floor, set at start-up) and jumps to
  `__stack_overflow`, which prints `run-time error: stack overflow
  (recursion too deep)` and exits with 2. The interpreter recursed in C++
  for every simulated call and crashed near 50,000 calls; it now caps the
  depth at 10,000 with the same message.

### D38. Optimizer additions: algebra, unrolling, dead functions, reaching definitions (2026-11-21)

- **More algebraic rules** (`simplify()`, integers only): `x - x` and
  `x ^ x` are 0, `x & x` and `x & -1` are `x`, `x & 0` is 0, `x | x` is
  `x`, `x | -1` is -1, `x % 1` and `x % -1` are 0. None hold for
  floating point (`x - x` is NaN for infinite `x`).
- **Loop unrolling** (`-O3`, `unrollLoops()`): a small contiguous natural
  loop (header first, at most 24 quads, its single back edge last)
  becomes two copies, each keeping its exit test, so no trip count is
  needed; a pass saves the jump back every other iteration. Loops are
  taken last first so earlier loops keep their indices, and each is
  unrolled once.
- **Dead function elimination** (`-O3`, after inlining): only the
  functions `main` reaches through calls are kept. With no function
  pointers, every use of a function is a `call`.
- **Reaching definitions** (`reachingDefinitions()`): forward, union at
  joins, gen/kill per block, plus an entry pseudo-definition "no value
  yet" for each scalar local. The uninitialized-variable warning now
  uses it instead of liveness: a read reached by the entry definition is
  reported, at the line of that read rather than of the declaration.

### D39. Frame slot reclamation and register arguments (2026-11-21)

- **Frame slots:** the MIPS frame is laid out after register allocation;
  only names kept in memory and still mentioned by some quad get a slot
  (`t01` at `-O2`: 464 bytes -> 8).
- **Register arguments (MIPS o32 style), replacing D25 for user calls:**
  the first 16 bytes of arguments travel in `$a0`-`$a3`. Integer and
  pointer words go straight into their register and are never stored;
  other words there (doubles, `long long`, structs) are stored as before
  and loaded too. The caller always reserves 16 bytes as the callee's home
  area. The callee moves an argument into its home register, or spills it
  to its home slot, so parameter access and `va_arg` are unchanged.
  Calls into the run-time library keep the all-stack convention, so
  `runtime.s` is untouched.

### D40. A combined driver (2026-11-21)

`mips_generator` already compiles phases 2, 2b, 3 and 4 into one
program, so it became the combined driver rather than a new binary: a
stage flag (`--tokens`, `--ast`, `--symbols`, `--tac`, `--run`) stops
after that phase and prints it; with none it writes the MIPS assembly as
before. The per-phase binaries stay for the per-phase test suites.

### D41. Audit of D34-D40 (2026-11-22)

Every item was re-checked with probe programs compared against g++ on
the TAC interpreter and on SPIM at `-O0` ... `-O3` (register arguments
of every kind and position, variadic calls, methods, recursion,
unrolled loops with `break`/`continue`/`switch`, division of every
width, the new algebraic rules, dead functions, the reduced classes),
plus the run-time errors in both back ends. Two changes came out of it:

- **`-O3` hang (older than D34):** `globalCommon()` started a block whose
  predecessors were not yet computed from the empty set instead of
  "everything", so its facts grew later and the iteration never settled
  on some loop shapes. Such a block is now skipped until a predecessor
  is computed; the sets only shrink and the analysis terminates. The
  reproducer is test `t35_loop_shapes`.
- **Register arguments follow the machine-level switch:** `-O0` and
  `--stack-only` keep the all-stack convention of D25 (the direct
  translation); `-O1` and above pass arguments in `$a0`-`$a3` (D39).

### D42. enum and union come back (2026-11-23)

**Decided by:** the user (reverses the enum/union part of D1/D2).
**Choices:** enums follow **C++ rules**; unions are **plain unions**.

- **Lexer/parser:** `enum` and `union` are keywords again. `union` shares
  the struct rules (`UnionDecl`); `enum Tag { A, B = 5, C, }` (trailing
  comma allowed) builds `EnumDecl` / `Enumerator`. The enumerators are
  declared in the parse-time table as they are read, so later values may
  use earlier ones. The grammar still has no conflicts.
- **Representation:** an enum type is a `TypeKind::Int` type that carries
  its `EnumInfo` (`Type::enumInfo`). Every later phase -- TAC, the
  interpreter, the optimizer, MIPS -- sees a plain 4-byte int and needs
  no change; only the semantic rules look at `enumInfo`.
- **Enum rules (C++):** each enum is its own type. enum -> int is an
  integral promotion, enum -> other arithmetic a conversion; int -> enum
  and enum -> another enum only with a cast (`(Color)2`, `Color(2)`).
  `++`/`--` on an enum are errors; `c ? Red : Blue` keeps the enum type;
  overloads can tell an enum from int and enums are mangled by name
  (`_Z4show5Color`, an unnamed enum by its typedef name). Enumerators are
  constants of the enclosing scope with the enum's type: the previous
  value plus one, or an integer constant expression, which must fit
  `int`. No opaque (forward-declared) enums, no `enum class`; an enum
  cannot be defined inside a struct or class.
- **Plain unions:** data members only -- no member functions,
  constructors, friends, static or reference members, and no member
  whose class has a constructor. Every member is at offset 0 and the size
  is the largest member rounded to the largest alignment. A brace
  initializer sets the first member, or the designated one (`{ .f = 1.0f
  }`); more than one value is an error. No anonymous unions (`union {
  ... };` as a member or a statement). `struct U` naming a union (and the
  reverse) is a tag mismatch.
- **Optimizer check:** reading a union through another member than the
  one written (type punning) needed no change: value numbering keys a
  load by its machine class, every store invalidates what is known about
  memory, and a union is a block object, so it is never in a register or
  in global propagation. `t36_enums_unions` checks this at every level
  on the interpreter and on SPIM against g++.

### D43. extern removed (2026-11-23)

**Decided by:** the user. **Done like D31** (`register`, `volatile`):
`extern` is no longer a keyword, so it scans as an identifier and an
`extern` declaration is an ordinary syntax error (`test29` [12]).

Every object declaration is now a definition. The semantic phase loses
the external-linkage merging (one symbol and a composite type for
`extern int a[]; int a[5];`), the block-scope `extern`, the checks for
`extern` with an initializer, and the "declared 'extern' and used but
never defined" warning; a second file-scope definition of a name is the
usual duplicate-declaration error. TAC no longer skips globals that are
declared but not defined, because there are none. (D31 had kept
`extern` when `register` and `volatile` went; this reverses that choice.)

### D44. Virtual functions come back (2026-11-24)

**Decided by:** the user (reverses the virtual-function part of D35).
**Choices:** overriding follows the **C++ rule**; **pure virtual
functions and abstract classes** are included.

- **Syntax:** `virtual` is a keyword of the grammar again (`explicit`
  stays reserved and rejected). `virtual T f(...) = 0;` declares a pure
  virtual function; `= 0` on anything else is a syntax error. `virtual`
  is only allowed on a member function declared inside its class (not on
  a free, static or out-of-class definition).
- **Overriding:** when a class is complete, `virtualFunctions()` copies
  its base's table and lets each of its member functions with the same
  name and parameters as a slot take that slot -- it becomes virtual with
  or without the keyword, and must return the same type. A new virtual
  function gets the next slot. The class is abstract if some slot's final
  overrider is pure.
- **Abstract classes:** no variable, member, array, by-value parameter or
  result, or `T()` of an abstract class; pointers and references are
  fine. A class with virtual functions cannot be brace-initialized.
- **Layout (Claude's choice):** the first polymorphic class of a chain
  adds the vtable pointer right after its base part -- not at offset 0 --
  so the base sub-object stays at offset 0 and derived-to-base conversion
  stays free, as the rest of the compiler assumes since D35; every class
  derived from it uses the same place (`RecordInfo::vptrOffset`). With
  single inheritance a slot is just a function address (4 bytes): no
  this-adjustment is ever needed.
- **TAC:** one global table `_ZTV<class>` per polymorphic class (a pure
  slot holds 0). A constructor -- user-written or implicit -- installs its
  class's table after constructing the base, so a virtual call made while
  a base constructor runs reaches the base's function (C++). A copy that
  creates an object (initialization, by-value parameter, returned value)
  re-installs the declared class's table; an assignment keeps the target's
  table pointer (`*basePtr = other;` leaves a derived object derived).
  A call through a pointer, a reference, `*p` or an implicit `this` loads
  the address from the table and becomes `t = call *a, n`; a call on a
  named object and a qualified call (`p->Base::f()`) stay direct.
  Virtual operators dispatch the same way.
- **Interpreter:** each function gets an address (0x00400000 + 16 k) so a
  table can hold it; `call *t` looks the function up by that address.
- **Optimizer:** dead function removal keeps every function a table names;
  inlining and tail recursion only see direct calls.
- **MIPS:** `jalr` on the address; at `-O1` and above a virtual call uses
  the `$a0`-`$a3` convention of a direct user call (D39), since its target
  is always a user function. The table entries are filled in by the
  start-up code like any other address initializer.
- **Not included:** `override` / `final`, covariant return types, RTTI,
  virtual inheritance; an object obtained from `malloc` runs no
  constructor, so it has no table pointer and must not be used for a
  virtual call.

Tests: `t37_virtual` (interpreter and SPIM at every level, against g++),
`v29_virtual`, `e26_virtual`.

### D45. A free list: freed memory is reused (2026-11-24)

**Decided by:** the user (implement the free list); the shape is Claude's.

- **Blocks:** the word before a block holds its *capacity*, the requested
  size rounded up to 8 (at least 8). A free block's first word links it to
  the next free block; the list head is `__heap_free` in the run-time
  library.
- **`malloc`:** first fit, most recently freed block first, handed out
  whole (no splitting); if nothing fits, a fresh block from `sbrk` as
  before. **`free`:** pushes the block on the list (`free(0)` does
  nothing). **`calloc`:** clears the block's whole capacity, since a
  reused block is not zero. **`realloc`:** keeps the block when its
  capacity is enough, otherwise allocates, copies the old capacity and
  frees the old block.
- **Not done:** splitting a large free block, merging neighbouring free
  blocks, returning memory to the system.
- **Interpreter:** the same algorithm (so the two back ends behave
  alike), and it reports `free` of a pointer `malloc` did not return and
  a double `free` as run-time errors; SPIM cannot check those.

Test: `t38_free_list` (a 50,000-iteration malloc/free loop runs in
constant space; calloc of a reused dirty block is zero; realloc grows and
shrinks keeping the contents), on the interpreter and SPIM at every level
against g++.

### D46. Small focused tests, and exact printf rounding (2026-11-24)

**Decided by:** the user (smaller tests that still catch issues, in
phases 3 and 4).

Ten small programs (under ~40 lines each) were added to the shared
phase 3 / phase 4 suite, each aimed at one area where compilers break:
`t30_int_edges`, `t31_short_circuit`, `t32_calls_registers` (reusing the
numbers left free when D35 removed the old t30–t32), `t40_aliasing`,
`t41_loop_edges`, `t42_statics_globals`, `t43_float_conv`,
`t44_long_long`, `t45_strings_chars`, `t46_classes_small`. They avoid
what legitimately differs from a 64-bit g++ (`long`, pointer sizes,
unspecified argument order) so that any difference is a bug.

They found one: the run-time `printf` scaled a value by 10 once per
decimal, rounding each time, so `%.2f` of 2.675 (stored as 2.67499...)
became 267.5 and printed `2.68`; glibc prints `2.67`. `__pf_fixed` now
computes 10^precision first (exact up to 10^22), multiplies once, and
when the product is exactly a half takes the exact error of that
multiplication (Dekker's two-product with Veltkamp splitting) to decide
which side the true value lies on; only a true half rounds to even.
Checked on 480 values near halves at `%.0f`...`%.6f`, `%e`, `%g`: the old
runtime differed from glibc on 76 lines, the new one on none.

### D47. Virtual functions removed again (2026-11-24)

**Decided by:** the user: remove function overriding, vtables and
everything related to them. This reverses D44 and restores D35's state.

- `virtual` is a reserved word again and the scanner rejects it:
  "'virtual' is not supported: this language has no virtual functions";
  `= 0` is again an ordinary error.
- Gone from every phase: `virtualFunctions()`, abstract classes and
  their checks, the vtable pointer in `layoutRecord`, `_ZTV<class>`
  tables and their installation, `call *t` and dispatch, function
  addresses in the interpreter, vtable roots in dead function removal,
  and `jalr` in the MIPS back end.
- A member function with the same name as a base member function hides
  it and is bound from the declared type (D35).
- Tests: `t37_virtual`, `v29_virtual` and `e26_virtual` are removed;
  `e24` and `test31` reject `virtual` again; `t46_classes_small` tests
  hiding instead of overriding.

### D48. Smaller phase 3/4 tests chosen by coverage (2026-11-24)

**Decided by:** the user: smaller test programs that are still strong
enough to catch problems, in phases 3 and 4.

- The 26 long programs `t01`–`t09` and `t13`–`t29` (1,730 lines) are
  replaced by 15 short ones `t01`–`t09` and `t13`–`t18` (509 lines).
  `t10`–`t12`, `t30`–`t36` and `t38`–`t46` stay. The suite went from
  2,336 to 1,054 lines of test source.
- They were chosen by line coverage (gcov) of `phase3-ir/src` and
  `mips.cpp` over every test at `-O0`...`-O3`, in the interpreter and as
  MIPS: the old suite reached 3,848 lines, the new one 3,879, and every
  line the old suite reached is still reached.
- Writing them found a real bug: `va_start(ap, …)` did not count as a
  definition of `ap` for reaching definitions, so passing a `va_list`
  on gave a false "may be used uninitialized" warning. `assigned()` in
  `opt.cpp` now treats it as one; `diagnostics/uninitialized.c` has the
  case.
- Expected outputs come from g++ (gcc for `t04_arrays`, which uses a C
  designator; `t02_control_flow` with `until(c)` defined as
  `while(!(c))`).

### D49. One optimization level, a modular optimizer, MIPS argument registers always (2026-11-24)

**Decided by:** the user: keep the easiest optimizations (chosen:
textbook basics plus local common subexpressions), bring back function
inlining, make the optimizer modular and readable without comments,
follow the MIPS convention of arguments in `$a0`–`$a3`, and put the
program's output in the TAC logs.

- **Kept (`-O1`, the only level):** value numbering per basic block
  (constant folding, algebraic identities, local common subexpressions,
  copy and constant propagation), temporary merging, dead temporaries,
  jump clean-up, and inlining of functions of at most 16 instructions
  (not recursive, not variadic), with the block passes run before and
  after it.
- **Removed:** `-O2` (global constant/copy propagation, dead
  assignments by liveness) and `-O3` (tail recursion, global common
  subexpressions, loop unrolling, dead function removal); in the MIPS
  back end, register allocation, the peephole pass, the branch-free
  comparison pattern, the second frame layout and `--stack-only`. The
  flags `-O2` and `-O3` are no longer accepted.
- **Kept for the warning:** reaching definitions still drive the
  uninitialized-variable warning (D38), now in `opt_uninitialized.cpp`.
- **Modules:** `opt.cpp` (driver), `opt_common.cpp`,
  `opt_numbering.cpp`, `opt_algebra.cpp`, `opt_cleanup.cpp`,
  `opt_inline.cpp`, `opt_uninitialized.cpp`, with the shared
  declarations in `include/opt_internal.h`. The code has no comments;
  each step is a small function whose name says what it does.
- **Calls (amends D39):** a call to a user function passes the first 16
  bytes of arguments in `$a0`–`$a3` at every level, not only when
  optimizing; the caller always reserves those 16 bytes and the callee
  stores the registers into their slots. Calls into the run-time
  library keep the all-stack convention.
- **Logs:** with `--run`, `logs/<file>.tac` / `.O1.tac` end with a
  PROGRAM OUTPUT section: what the program printed, its exit code and
  the instructions executed.

---

## Open questions

*(none at the moment)*
