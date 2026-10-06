> **Historical development notes — not maintained.**
> This was the phase README until the documentation audit of 2026-10-04.
> It records how the phase was built and the reasoning behind decisions;
> some statements (counts, limitations, plans) are outdated. The current,
> verified documentation is [`../README.md`](../README.md).

# Phase 2b — Semantic Analyzer

Type checking, scope resolution and every other "is this program
meaningful?" rule, run on the abstract syntax tree that
[phase 2](../../phase2-parser/README.md) builds. Phase 2 deliberately checks
nothing but the grammar; this phase is where its README says "semantic
checking and an *annotated* AST" belong. The output is that annotated
AST plus a persistent, typed symbol table — the input TAC generation
(phase 3) will consume.

```
source ─► scanner.l ─► parser.y ─► AST ─► semantic analysis ─► annotated AST + symbol table ─► (TAC)
          └───────────────────── phase 2 ────────────────────┘ └────────── this phase ─────────┘
```

| | |
|---|---|
| Build | `make` → `./semantic_analyzer` |
| Run one file | `./semantic_analyzer file.c` (`-q`: verdict and diagnostics only) |
| Run all tests, checked | `./run_tests.sh` (or `make test`) |
| Run all tests, raw output | `./run.sh` |
| Exit status | 0 = no semantic errors (warnings allowed), 1 = syntax or semantic errors |
| Log | `logs/<file>.log`, same report as the terminal |

On success it prints the annotated AST (every node with its type,
lvalue-ness, folded constant and resolved symbol), the semantic symbol
table, and the MIPS32 layout of every struct/union/class. On failure it
prints GCC/Clang-style diagnostics, through the exact printer phase 2
uses:

```
test/invalid/e03_scopes.c:11:5: semantic error: undeclared identifier 'inner' [undeclared]
 11 |     inner = 2;
    |     ^
```

Every message ends in a `[category]` tag (`undeclared`, `type-mismatch`,
`argument-count`, `access`, `duplicate-case`, …). If the file has
lexical/syntax errors, those are reported exactly as phase 2 reports
them and semantic analysis is not run — typing a partial tree only
produces cascades of bogus errors.

## How it fits the existing compiler

Building this phase changed nothing observable in phase 2: all 32 of
its tests produced byte-identical stdout, stderr and logs, with exactly
the baseline 7 shift/reduce conflicts. A later round then *extended* the
grammar so the C++-style features could actually be used (constructor
calls, `Class::member`, operator overloading, `va_arg`, designated
initializers, ...; see phase 2's README, "C++ and C99 syntax additions");
that round fixed the `do`-`while` recovery gap and a `sizeof(T) * x`
misparse in the original grammar, went from 7 conflicts to 0, and changed
a handful of parser test outputs, each intentionally. This phase has its own
`makefile`, which regenerates the parser from phase 2's *sources* into
its own `build/`, compiles phase 2's parser-specific sources
(`declarators`, `scanner_support`, `token_converter`) and links the shared
library ([`../shared`](../../shared/README.md)), where the AST, the types,
both symbol tables and the diagnostics live.

### What had to change in phase 2, and why

The AST phase 2 produced was enough to print, not enough to type-check.
Declared types only survived as flattened strings (`INT_POINTER_ARRAY`):
struct tags, array sizes, `...`, unnamed parameters, function return
types, typedef identity, `const` in casts, access specifiers and
inheritance access were all thrown away. Reconstructing them from label
strings is impossible (the information is gone) and re-parsing would mean
a second grammar. So the smallest extension that carries the facts was
made instead — every change is additive and none is printed:

| Change | Where | Why |
|---|---|---|
| `ASTTypeExpr` attached to every declaration, parameter, cast, `sizeof(type)`, `new`, lambda | `shared/ast`, `declarators.cpp` (`makeTypeExpr`), `parser.y` actions | the declared type exactly as written: specifiers, tag/typedef name, qualifiers, pointer/array/function shape, array-size expressions, `(...)` grouping, `...` |
| `line`/`column` of each node set from its own token (`atToken`) | `parser.y`, `TokenRecord::column` | `mkNode` stamped the *lookahead* token's line, so diagnostics pointed past the construct |
| `ASTNode::access`, `ASTNode::bases` | `parser.y` member/inheritance rules | `public:`/`protected:`/`private:` and `class D : private B` were parsed and dropped |
| semantic annotation slots (`semType`, `symbol`, `isLValue`, `constValue`) | `shared/ast` | filled by this phase; forward-declared, so phase 2 does not depend on it |
| function-pointer `VarDecl` keeps its initializer | `declarators.cpp` | `int (*fp)(int) = add;` silently lost `add` from the AST (a real bug; no phase-2 test covered it) |
| diagnostic/table printers moved out of `main.cpp` | now `shared/diagnostics`, `shared/token`, `shared/symbol_table` | so every driver prints diagnostics identically |

In that first step only grammar *actions* changed, never productions,
so the conflict count could not move. The later syntax additions are
listed in phase 2's README.

## Design

### Alternatives considered

| Decision | Chosen | Rejected, and why |
|---|---|---|
| Where checking happens | a separate pass over the finished AST | **inside the Bison actions**, as the reference compiler (`cielc`) does. Phase 2 is explicitly grammar-only and stays independently testable; a tree walk can also see things a single bottom-up pass cannot (whole class bodies before method bodies, labels before the `goto`s that use them, functions defined later in the file). |
| Input representation | phase 2's AST + a syntactic `ASTTypeExpr` | **re-deriving types from `typeStr` labels** (information already lost), or **a new AST** (duplicates the tree, breaks phase 2's output). |
| Type representation | immutable structural type graph | **`typeStr` + pointer/array counters**, as phase 2 uses. Cannot express `int (*)[3]` vs `int *[3]`, `const int *` vs `int *`, or function signatures, and every rule becomes string surgery. |
| Symbol table | persistent tree of scopes | **a stack that discards popped scopes** (phase 2's). TAC/MIPS generation needs every local, its scope and storage after the pass. |

The theory follows the Dragon Book: type expressions built from basic
types with constructors `pointer`, `array(n, t)`, `function`, `record`
(§6.3.1); structural equivalence for constructors and name equivalence
for records (§6.3.2); widths and field offsets (§6.3.4–6.3.6);
synthesized expression types with widening via usual arithmetic
conversions (§6.5.2, the `max()`/`widen()` of Fig. 6.27); overload
resolution by argument types (§6.5.3); chained symbol tables with the
most-closely-nested rule (§2.7). From `cielc` came the idea of the
context stacks (function / loop / switch / lambda), case-value sets per
switch, lvalue tracking per expression node, and access checks along
inheritance paths.

### Files

The type system and the symbol table are in the shared library
([`../shared/types`](../../shared/README.md), `../shared/symbol_table`), so
other phases can use them; this folder holds only the analyzer.

```
phase2b-semantic/
├── include/
│   ├── semantic.h      SemanticAnalyzer (the pass) and its contexts
│   └── report.h        annotated-AST printer
├── src/
│   ├── declarations.cpp diagnostics, entry point, type resolution, declarations, classes, functions
│   ├── statements.cpp   blocks, conditions, loops, switch/case, jumps, return
│   ├── expressions.cpp  expression typing, calls & overloads, builtins, lambdas
│   ├── cxx.cpp          constructors, operator overloading, new, va_start/va_arg/va_end
│   ├── sequencing.cpp   sequence-point check (`i = i++`), a pass after typing
│   ├── report.cpp       annotated AST
│   └── main.cpp         driver: parse -> analyze -> report
├── test/valid/          programs that must be accepted
├── test/invalid/        programs that must be rejected, with expected diagnostics inline
├── run_tests.sh         self-checking test runner
├── run.sh               raw runner, same convention as the other phases
└── makefile
```

### Type system (`shared/types/types.hpp`)

`Type` is an immutable node: a kind (`Void`, `Bool`, `Char`, `Short`,
`Int`, `Long`, `LongLong`, `Float`, `Double`, `Enum`, `Pointer`,
`Reference`, `Array`, `Function`, `Record`, `Opaque` for `FILE` and `va_list`,
`Closure` for lambdas, and `Error`), `const`/`volatile` on the level they
qualify, and children (`elem`, `ret`, `params`). Pointer depth is
structural: `int **` is `Pointer(Pointer(Int))`. Records and enums point
at a shared `RecordInfo`/`EnumInfo`, so equality is by identity (C's name
equivalence); everything else is structural.

Declarators are applied inside-out exactly as C reads them, using the
`(...)` grouping the parser now records — so `int (*pa)[3]` is a pointer
to an array, `int *pa[3]` an array of pointers, `int (*fps[2])(int)` an
array of function pointers, `int *(*f)(int)` a pointer to a function
returning `int *`.

`implicitConversion(from, to)` is the single source of truth for
assignment, initialization, argument passing and `return`. It also
returns a C++-style rank (exact / promotion / conversion / none) so the
same rules drive overload resolution. `decay()` performs array→pointer,
function→function-pointer and reference→referent conversion;
`usualArithmetic()` computes the common type of an arithmetic operator.
`sizeOf`/`alignOf`/`layoutRecord` use the MIPS32 ILP32 model (`char` 1,
`short` 2, `int`/`long`/pointers 4, `long long`/`double` 8; base class
sub-objects first; union members all at offset 0).

### Symbol table and scopes (`shared/symbol_table/symbol_table.hpp`, part 2)

A tree of `Scope`s (`Global`, `Function`, `Block`, `Record`, `Lambda`),
never destroyed. The *active stack* is what is visible "here", so the
analysis never confuses "exists somewhere" with "visible at this point".
Each scope has two namespaces (ordinary identifiers, which allow
function overloads, and struct/union/class/enum tags).

A `Symbol` records its kind, structural type, storage class (`global`,
`static`, `local`, `param`, `member`), scope and scope path, source
position, use count and a program-wide `uniqueName` (globals keep their
name, functions their mangled name — `main` stays `main` — locals and
parameters get `name.N`). Every callable also gets its `mangledName`,
computed here from the resolved signature under the Itanium C++ ABI
(typedefs resolved, struct/class/enum by tag, ABI substitutions; the
same names g++ emits), shown in the table's *Mangled Name* column. Function symbols also list their parameters
(unnamed ones included), their locals and their body scope; members
carry their owner record, access and byte offset.

While a member function body is analysed, the class's `Record` scope is
on the stack, so a bare `legs` resolves to `this->legs` — through base
classes too, with C++ name hiding (a member of the derived class hides
an inherited one of the same name).

Function bodies share one scope with their parameters (so `int f(int a)
{ int a; }` is a redeclaration, as in C); every `{}` block, `for`
header, and the body of `if`/`while`/`for`/`until`/`switch` gets its
own scope.

### Analysis order (language decisions)

- Objects, typedefs and tags are **declare-before-use**, as in C.
- File-scope **functions may be called before their declaration**. Phase 2
  already resolves exactly these forward references (see its test10 and
  test23), so this phase keeps that language rule: the first use of an
  undeclared name that is a file-scope function declares it from its
  later declaration. A *variable* used before its declaration is an
  error, with a hint pointing at where it is declared.
- Inside a class every member is visible to every method body (bodies
  are checked after the class is complete, as in C++).
- Labels have function scope (collected before the body is walked), so
  forward `goto` works; each lambda has its own labels.
- `int x; int x;` is an error even at file scope (no C tentative
  definitions — the language has no `extern`).
- `auto x = expr;` deduces `x`'s type from the initializer.

### Error handling

Errors and warnings go through phase 2's `reportDiagnostic()` /
`g_diagnostics` with kind `Semantic error` / `Semantic warning`, and are
printed by the shared `printDiagnostic()` (source line + caret). An
expression that already failed is given the `Error` type, which every
rule accepts silently, so one mistake produces one message; identical
messages at the same position are reported once. Warnings never change
the exit status.

## Rule catalog

**Declarations** — duplicate declaration in the same scope; redefinition
as a different kind of symbol; `void` / incomplete-type objects
(`struct Missing m;`, `FILE f;`); arrays without size or initializer;
array size not a positive integer constant (no VLAs); only the first
dimension may be omitted; arrays of `void`/functions/references; invalid
specifier combinations (`int char`, `signed unsigned`); missing type
specifier (warning, defaults to `int`); `auto` without initializer;
reference without initializer; file-scope and `static` initializers must
be compile-time constants; initializer lists (excess elements, nested
lists, brace elision for arrays, struct/union member order, string
literals into `char` arrays, size inference for `int a[] = {...}` /
`char s[] = "..."`); typedef redefinition with a different type; enum
values must be integer constants.

**Expressions** — undeclared identifiers; type names used as values;
operand rules for every operator (`%`, shifts and bitwise need integers;
`*`/`/` need arithmetic; `+`/`-` allow pointer ± integer and pointer −
pointer of the same type; relational/equality allow compatible pointers
and pointer vs. null constant, reject pointer vs. integer and distinct
pointer types; logical operators and conditions need scalars); pointer
arithmetic on `void *`/function/incomplete pointees; usual arithmetic
conversions and integer promotions for the result type; assignment
compatibility with an explanation (`incompatible integer to pointer
conversion`, `discards 'const' qualifier`, …); modifiable-lvalue rules
for `=`, compound assignment, `++`/`--` (rvalues, arrays, functions,
`const` objects, read-only locations, by-copy lambda captures); `&` needs
an lvalue (or a function); `*` needs a non-`void` pointer; subscripts
need a pointer/array and an integer (constant out-of-bounds index:
warning); member access (`.` vs `->` with "did you mean" hints, unknown
member, member of a non-struct, ambiguous member in multiple
inheritance); casts (no struct casts, no casts from `void`, pointers only
to/from integers and pointers); conditional-operator operand
compatibility; `sizeof` on functions/incomplete types; `new` of
incomplete types; `delete` of non-pointers; constant folding of integer
constant expressions (used by case labels, array sizes, enumerators,
initializers); division by a constant zero (warning).

**Functions** — conflicting types between declarations (including
"overloaded only on return type"); redefinition; duplicate parameter
names; `void` parameters; incomplete parameter/return types in
definitions; argument count (`function 'foo' expects 2 arguments but 3
were provided`, "at least" for variadic) and per-argument conversion;
reference parameters need lvalues of exactly the referenced type unless
`const`; calling a non-function; overload resolution with C++ ranking
(exact > promotion > conversion > ellipsis), "no matching function" and
"ambiguous call" errors listing the candidates; `return` value vs. `void`
function, missing value in a non-`void` function, returned type
compatibility, reference returns need lvalues; warning when a non-`void`
function has no `return` at all; warning when a called function is never
defined; `main` must return `int` and take `()` or `(int, char **)`.

**Control flow** — `break` outside a loop/switch; `continue` outside a
loop (a switch alone is not enough); `case`/`default` outside a switch;
case labels must be integer constant expressions; duplicate case values
(after folding: `'a'` and `97`, `ONE` and `1` collide); multiple
`default`s; switch on a non-integer; conditions of
`if`/`while`/`do`/`for`/`until`/`?:` must be scalar; `goto` to an
undeclared label; duplicate labels; contexts reset inside lambdas
(`break` inside a lambda inside a loop is an error).

**Constructors and objects** — `Dog d(args)`, `Dog(args)`, `new
Dog(args)`, `Dog d = 5` (converting constructor) and `Dog d;` all pick
a constructor by overload resolution, with the implicit default and copy
constructors when the class declares none; a class that declares
constructors but none callable without arguments cannot be
default-constructed (`Dog d;`, `new Dog`, `Dog pack[3]`, `new Dog[n]`);
private constructors are access-checked; in-class prototypes
(`Dog(int);`) must be matched by an out-of-class `Dog::Dog(int) {...}`,
destructors likewise; a scalar initialized with `int x(a, b)` gets
exactly one value.

**Operator overloading** — declarations: arity per operator (binary-only,
unary-only, either, `++`/`--` with the `int` postfix marker), `=` `[]`
`()` must be members, non-member operators need a class or enum
parameter. Uses: `a + b`, `-a`, `!a`, `++a`, `a++`, `a = b`, `a += b`,
`a[i]`, `a(...)`, `*a`, `&a` on class operands resolve `operator<op>` as a
member (left operand is the object) or a file-scope function, with normal
overload resolution; otherwise "no 'operator*' is declared for these
operands". Plain `=` without `operator=` is a memberwise copy of the same
class; `&` without `operator&` takes the address.

**Variable arguments** — `va_start(ap, last)` only in a variadic
function (and only a lambda-free one), `ap` must be a `va_list` lvalue,
`last` should be the last named parameter (warning, as gcc);
`va_arg(ap, T)` needs a type, yields `T`, and warns when `T` is promoted
through `...` (`char`, `short`, `bool`, `float`); `va_end(ap)`.

**Initializers (additions)** — `.field = v` must name a field (positional
values continue after it; any union member may be designated), `[N] = v`
must be inside the array (which sizes `int a[] = {[4] = 1}` to 5), the
designator kind must match the target, `{}` value-initializes anything
except an unsized array (zero-size array error).

**Structures, classes, unions, enums** — unnamed types (`struct {...} p;`,
`typedef struct {...} Pt;`, which is then called `Pt` in messages and
mangled names, as in C++); anonymous members (`struct S { union { int
i; float f; }; };`): the union is an unnamed field and its members are
*promoted* -- `s.i` works, at the union's offset plus its own, so
`RecordInfo::promoted` gives TAC ready-made offsets, and `.i = 1`
designates them; a promoted name clashing with another member is a
duplicate member. **Anonymous unions outside a record** (C++): `union {
int a; char b; };` in a function -- or `static` at file scope, which
C++ requires -- creates one hidden union object (`__anon_union.N`), and
`a`, `b` become variables of that scope with no storage of their own
(`Symbol::anonymousUnion` points at the object, `offset` is their place
in it); they clash with other names in the scope like any declaration.
An anonymous union may only have public non-static data members, and an
anonymous struct inside one needs a named enclosing record (g++'s
rules). An unnamed *struct* outside a record that declares nothing
earns gcc's "unnamed struct/union that defines no instances".
Then duplicate members; members of
incomplete type (including the struct itself; pointers to it are fine);
base class undeclared/incomplete/union/itself/listed twice; access
control for `public`/`protected`/`private` members including inheritance
access (`private` base members are inaccessible in derived classes,
non-public inheritance hides public members from outsiders, `protected`
only through the accessing class); `this` outside a non-static member
function or inside a static one; non-static members used in static
member functions; constructor and destructor names must match the class;
constructors/destructors cannot return values; out-of-class definitions
must match a declaration in the class; methods must be called;
derived-to-base pointer conversion (not the reverse); tag kind
mismatches (`struct U` when `U` is a union).

**Lambdas** — capture list entries must be automatic variables, appear
once, and at most one capture-default; using an uncaptured local without
a capture-default; members/`this` need `[this]` or a capture-default,
and `[this]` only inside a non-static member function; assigning a
by-copy capture unless the lambda is `mutable`; the return type is
deduced from `return` statements, which must agree, or fixed by `-> T`
and checked like a function's; calls are checked against the lambda's
parameters; a capture-less lambda converts to a matching function
pointer.

**Builtins** — `printf`, `scanf`, `malloc`, `calloc`, `realloc`, `free`,
`fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`,
`fputs`, `feof` are reserved words in this language, so they are checked
against built-in signatures (`FILE *` where a stream is expected, etc.).
`scanf`/`fscanf` arguments after the format must be pointers to writable
storage (`did you forget '&'?`). For literal format strings, a
`gcc -Wformat`-style warning checks the argument count and that printf
conversions get the right kind of value.

## Rules taken from a formal semantics of C

Papaspyrou's *A Formal Semantics for the C Programming Language* (PhD
thesis, NTUA 1998) gives ANSI C a complete denotational semantics: a
static semantics (types, environments, compatible/composite types),
typing rules for every phrase (Part III) and a dynamic semantics whose
central result is the unspecified evaluation order between sequence
points (Part IV). The analyzer already matched most of it -- the type
classes, environments with separate tag/ordinary name spaces, integer
promotions and usual arithmetic conversions (`unsigned + long` is
`unsigned long` on ILP32), the type of every integer constant (`3000000000`
is `long long`, `0xFFFFFFFF` `unsigned int`), qualifier inclusion in
pointer assignment, null pointer constants, the typing of each operator.
Checking every rule against it, with gcc and g++ as the reference for
the diagnostics, found these gaps, now closed:

| Thesis rule | Before | Now |
|---|---|---|
| `isModifiable` (4.6.1): a struct/union is assignable only if all its members are | `k1 = k2` accepted for `struct { const int id; }` | error naming the member, also through nested records and base classes (`its member 'k.id' is const-qualified`) |
| constants have values *of their type* (`val[τ]`, `arithConv`, 4.6.2, E4-E8) | folding in plain 64-bit: `-1 < 0u` was true, `~0u` was -1, `2147483647 + 1` positive | operands converted as the typing rule says (usual conversions; only the left operand's promotion for a shift), result wrapped to the type (`shared/types`: `wrapToType`, `fitsInType`); gcc's warnings: integer overflow, shift count negative / >= width, `char c = 300` changes value to 44 |
| evaluation order (11.8, 12.6: operands interleaved, `seqpt` after the first operand of `&&` `\|\|` `?:` `,`, before a call) | nothing | `sequencing.cpp`: per full expression, the variables (and member paths `s.x`) each subexpression writes and reads; a write interleaved with another access is gcc's "operation on 'i' may be undefined" -- same lines as gcc on the test set, no warning on `i = (i++, i)`, `i = f(i++)`, `j = i && i++`, `sizeof(i++)` |
| declarations with linkage (ch. 5, 13), composite types (4.6.3) | `extern` was a syntax error | `extern` / `register`: an `extern` declaration and the definition are one symbol whose type is the composite (`extern int a[]; int a[5];` makes `a` an `int[5]`); a block-scope `extern` names the file-scope object; conflicting types, `extern` with an initializer in a block, several storage classes, file-scope `register`, `&` of a `register` variable, an `extern` object used but defined nowhere |
| default argument promotions (`argPromote`, R4) in printf/scanf | length modifiers ignored, `%f` took an `int`, scanf pointees unchecked | `%ld` / `%lld` / `%hhd` / `%zu` widths, `%f` needs a floating value, scanf `%f` needs a `float *` (`%lf` a `double *`), `%d` an `int *` -- the warnings gcc's -Wformat gives |

Where C and C++ differ the analyzer keeps its documented choice (a
`void *` converts to any object pointer and `1 - 1` is a null pointer
constant, as in C and in the thesis; `'a'` is a `char` and `const int N`
is a constant, as in C++).

## Feature matrix

✓ = supported, — = phase not started yet.

| Feature | Lexer | Parser | AST | Semantic | TAC | MIPS | Notes |
|---|---|---|---|---|---|---|---|
| Arithmetic / logical / relational / bitwise operators | ✓ | ✓ | ✓ | ✓ | — | — | |
| Assignment, compound assignment, `++`/`--` | ✓ | ✓ | ✓ | ✓ | — | — | lvalue / const rules |
| if-else, for, while, do-while | ✓ | ✓ | ✓ | ✓ | — | — | |
| until | ✓ | ✓ | ✓ | ✓ | — | — | |
| switch / case / default | ✓ | ✓ | ✓ | ✓ | — | — | constant + duplicate labels |
| break / continue / goto | ✓ | ✓ | ✓ | ✓ | — | — | |
| int and char arrays, multidimensional arrays | ✓ | ✓ | ✓ | ✓ | — | — | |
| Pointers, multi-level pointers | ✓ | ✓ | ✓ | ✓ | — | — | structural depth |
| Structures | ✓ | ✓ | ✓ | ✓ | — | — | layouts + offsets |
| Unions | ✓ | ✓ | ✓ | ✓ | — | — | |
| Enums | ✓ | ✓ | ✓ | ✓ | — | — | values folded |
| typedef | ✓ | ✓ | ✓ | ✓ | — | — | incl. typedef'd structs and function pointers |
| printf / scanf | ✓ | ✓ | ✓ | ✓ | — | — | |
| Function calls, arguments, recursion | ✓ | ✓ | ✓ | ✓ | — | — | incl. forward calls |
| static | ✓ | ✓ | ✓ | ✓ | — | — | storage + constant initializers |
| extern, register | ✓ | ✓ | ✓ | ✓ | — | — | linkage, composite types, block-scope `extern`; `v24`, `e20` |
| Sequence points | — | — | — | ✓ | — | — | `i = i++` etc., gcc's -Wsequence-point |
| Typed constant folding | — | — | — | ✓ | — | — | values wrapped to their type; overflow / shift / conversion warnings |
| Variable-argument functions | ✓ | ✓ | ✓ | ✓ | — | — | `...`, `va_list`, `va_start`/`va_arg`/`va_end` |
| Dynamic memory (`malloc`/`calloc`/`realloc`/`free`/`new`/`delete`) | ✓ | ✓ | ✓ | ✓ | — | — | incl. `new T(args)`, `new T[n]`, `delete[]` |
| Command-line input | ✓ | ✓ | ✓ | ✓ | — | — | `main` signature |
| References | ✓ | ✓ | ✓ | ✓ | — | — | binding rules, `int *&r` |
| Function pointers | ✓ | ✓ | ✓ | ✓ | — | — | |
| Function overloading | ✓ | ✓ | ✓ | ✓ | — | — | C++ ranking, ambiguity |
| Classes, objects, `this` | ✓ | ✓ | ✓ | ✓ | — | — | `Class::member`, the class name as a type in its own body |
| Inheritance (single, multiple) | ✓ | ✓ | ✓ | ✓ | — | — | |
| Access modifiers | ✓ | ✓ | ✓ | ✓ | — | — | |
| Constructors / destructors | ✓ | ✓ | ✓ | ✓ | — | — | calls, overloads, prototypes + out-of-class definitions |
| Operator overloading | ✓ | ✓ | ✓ | ✓ | — | — | member and non-member |
| Lambdas | ✓ | ✓ | ✓ | ✓ | — | — | captures, `mutable`, `-> T`, `[this]` |
| Designated / empty initializers | ✓ | ✓ | ✓ | ✓ | — | — | `.f =`, `[N] =`, `{}` |
| Unnamed struct/union/enum, anonymous members | ✓ | ✓ | ✓ | ✓ | — | — | `v22`, `e18`; offsets checked against gcc |
| Anonymous unions in functions / `static` at file scope | ✓ | ✓ | ✓ | ✓ | — | — | `v23`, `e19`; same errors and lines as g++ |
| `#define`, `#include`, `#if` (preprocessor) | ✓ (shared preprocessor) | ✓ | ✓ | ✓ | — | — | errors in macro expansions reported at the line as written |
| File manipulation | ✓ | ✓ | ✓ | ✓ | — | — | builtin signatures |
| `bool`, `const`, `volatile`, `auto` | ✓ | ✓ | ✓ | ✓ | — | — | incl. `int *const p` |

## Tests

`./run_tests.sh` runs three groups and fails on anything unexpected:

1. **`test/valid/`** (24 programs) must be accepted. Covers
   declarations, expressions, scopes and shadowing, functions and
   recursion, arrays, pointers, structures/unions, control flow,
   builtins, classes, lambdas and overloading, `main(argc, argv)` in both
   spellings, parenthesized declarators, subtle name resolution,
   constructors and operator overloading, the newer declarator /
   initializer / lambda / varargs syntax, the four former grammar
   limitations, macros and `#include` (`v20`), name mangling (`v21`),
   unnamed aggregates and anonymous members (`v22`), anonymous unions
   in functions and at file scope (`v23`), the rules taken from the
   formal semantics -- typed constants checked with array dimensions,
   linkage, sequence points, promotions (`v24`),
   and a file of programs that are legal but earn warnings. A
   declaration may announce its link name:

   ```c
   int over(double a) { return 0; }    // mangled: _Z4overd
   ```

   and the runner then requires exactly the announced names in both the
   semantic and the parser's symbol table. `v21`'s 42 names were taken
   from g++ (`g++ -c` + `nm`) for the same file.
2. **`test/invalid/`** (20 programs) must be rejected. Every expected
   diagnostic is written on the line where it must appear:

   ```c
   x = add(1, 2, 3);   // error: function 'add' expects 2 arguments but 3 were provided
   ```

   The runner requires each annotated message (as a substring) on that
   line, *and* that no unannotated diagnostic appears — so spurious
   errors fail a test just like missing ones. `// error:` / `// warning:`
   annotations also match preprocessor diagnostics (`e16`: `#error`, bad
   `#include`, unterminated `#if`; `e17`: type errors inside macro
   expansions, reported at the line that uses the macro).
3. **End to end**: all 37 programs of phase 2's test suite. The
   syntactically broken ones must stop before semantic analysis; the
   valid ones must pass, except two that g++ also rejects:
   `operators.c`, whose `c = a+++++b;` lexes as `(a++)++ + b` ("lvalue
   required as increment operand"), and `test7_cpp_features.c`, whose
   `Dog d;` default-constructs a class whose only constructor is
   `Dog(int)` (written before constructors could be called at all).
   Phase 2 only checks that they parse.

The 35 scenarios the phase was specified against map onto these files
(e.g. duplicate declaration and undeclared variable: `e01`; incompatible
assignment and invalid operands: `e02`; invalid scope access: `e03`;
argument count/types, return types and declaration/definition mismatch:
`e04`; break/continue/case/duplicate case/goto: `e08`; shadowing and
nested scopes: `v03`; recursion: `v04`), plus regressions for the bugs
found while trying to break the analyzer (`v15`, `v16`, `e13`, `e14`),
and the constructor / operator / varargs / initializer additions (`v17`,
`v18`, `e15`). In total the files pin down 185+ expected errors and
warnings, each on its exact line.

## Known limitations

These come from the grammar (phase 2):

- `T(...)` follows C++'s "if it can be a declaration, it is one" only
  as far as the scanner's bounded lookahead sees (to the matching `)`
  and one token after it): `Dog(x);` is a declaration, `Dog(x).bark();`
  an expression. A declaration-shaped group that only later turns out to
  be an expression (`Dog(x)[0] = 1;`) is read as a declaration.
- `int;` and `struct S;` produce no AST node, so "declaration does not
  declare anything" cannot be reported; forward struct declarations
  happen implicitly at first use (`struct S *p;`) instead.
- An out-of-class constructor of an undeclared class (`Other::Other()`)
  is a syntax error rather than "undeclared class", like any unknown
  type name.
- No `const` member functions, `explicit`, `virtual`, templates or
  namespaces.

Simplifications in this phase (documented choices, not bugs):

- No flow analysis: "missing return" is only reported when a non-`void`
  function contains no `return` at all; no uninitialized-use or
  unreachable-code diagnostics; jumping over an initialization with
  `goto`/`case` is not checked.
- Lambda capture rules are checked against the innermost lambda only.
- A class declared inside a function body can see that function's
  locals (C++ forbids it).
- Brace elision is supported for arrays, not for struct members
  (`struct { int a[2]; } s = {1, 2};` is rejected).
- Enums follow C (an `int` converts to an enum implicitly).
- Converting constructors apply in initialization (`Dog d = 4;`), not
  when passing arguments or returning (`f(4)` for `f(Dog)` is rejected).
- `sizeof` yields `unsigned int`. A constant's value is kept in its
  type's bit pattern (`wrapToType`); `long double` is `double`.
- The sequence-point check tracks named variables and their members;
  what a pointer or an array element designates (`a[i] = a[j]++`) is not
  tracked, and function bodies are not looked into (`i = f()` where `f`
  modifies `i` is not reported) -- as in gcc.

## What TAC generation gets from this phase

After `SemanticAnalyzer::analyze()`:

- **Every expression node** has `semType` (the type *before*
  array/function decay — call `sem::decay()` for the value type),
  `isLValue` (whether it designates storage, i.e. needs an address), and
  `hasConstValue`/`constValue` for integer constant expressions, already
  in the expression's type (`~0u` is 4294967295, `(char)200` is -56).
- **Identifier, member, call and declaration nodes** have `symbol`. For a
  call it is the overload actually chosen; a bare identifier whose symbol
  is a `Field` with `Storage::Member` is an implicit `this->field`; a call
  whose symbol is a non-static method reached through a bare identifier
  is an implicit `this->method(...)`. `goto` and labelled statements point
  at a `Label` symbol whose `uniqueName` is unique per function.
- **Symbols** carry everything storage allocation needs: `storage`
  (`global`/`static` → `.data`/`.bss`; `local`/`param` → the frame;
  `member` → `offset` into the record; a global with `isDefined` false is
  only declared `extern` here -- an external symbol, no storage; a variable with `anonymousUnion`
  set is a member of that hidden union object at `offset` -- address it
  through the object), `uniqueName` (a collision-free
  TAC name), and for functions `params` (unnamed ones included), `locals`
  (every local, including those of nested blocks) and `mangledName`.
- **Sizes and layouts**: `sem::sizeOf`, `sem::alignOf`, and each
  `RecordInfo`'s field offsets, size and alignment (MIPS32), base classes
  laid out first.
- **Conversions**: where an operand's value type differs from what its
  context needs, TAC inserts the conversion. The rules are public:
  `usualArithmetic`, `integerPromotion`, `decay`, `implicitConversion`;
  assignment/argument/return targets are the declared types already on
  the symbols.
- **C++ constructs** are explicit in the tree: `ConstructExpr` nodes
  (`Dog d(4)`, `Dog(4)`, `new Dog(4)`, and `Node(v)` inside class `Node`,
  which the analyzer rewrites from a call into a `ConstructExpr`) carry the
  chosen constructor in `symbol` (null = implicit default/copy); an
  operator expression on objects carries the chosen `operator<op>`
  function in `symbol`, so TAC emits a call instead of the primitive
  operation; `NewExpr` with array dimensions is `new T[n]` (first size is
  a run-time value); `DeleteExpr` labelled `[]` is `delete[]`; `va_*`
  builtins type-check `ap` as `va_list` (a 4-byte cursor) and `va_arg`'s
  second child is the `TypeName` node whose `semType` is the fetched type.
- Still to be decided by phase 3: closure conversion for lambdas (the
  capture list is on the `LambdaExpr` label; captured symbols are the
  enclosing function's locals), how `this` is passed to methods, and
  whether `long long` (8 bytes) is supported on MIPS32.
