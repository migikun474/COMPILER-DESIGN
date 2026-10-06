# Feature Audit

Every status below was established from the source and by running the
current build — not from the specification or older READMEs. Each
feature was compiled through all three executables
(`phase1-lexer/lexer`, `phase2-parser/syntax_analyzer`,
`phase2b-semantic/semantic_analyzer`); the "Tests" column names test
files that exercise it.

**Legend**

| Mark | Meaning |
|---|---|
| ✓ | implemented in that phase and verified |
| ◐ | implemented with documented gaps (see the notes / [Partial features](#d-partial-features)) |
| ✗ | rejected (not implemented) |
| — | not started (TAC and MIPS phases do not exist yet) |

The IR/TAC and MIPS columns are **— for every feature**: no back-end
code exists (`phase3-ir/` and `phase4-codegen/` contain only a README).
So "front end complete" is the strongest status any feature can have
today.

Test names: `L:` phase1-lexer/test, `P:` phase2-parser/test,
`S:` phase2b-semantic/test (valid `v..`, invalid `e..`).

![Feature implementation map](diagrams/feature-map.svg)

## Feature matrix

### Basic features (project specification)

| Feature | Lexer | Parser | AST | Semantic | IR | MIPS | Tests | Status |
|---|---|---|---|---|---|---|---|---|
| Arithmetic operators `+ - * / %` | ✓ | ✓ | ✓ | ✓ | — | — | L:test1, P:operators, S:v02 e02 | front end complete |
| Logical `&& \|\| !` (short-circuit typing) | ✓ | ✓ | ✓ | ✓ | — | — | L:test1, P:operators, S:v02 | front end complete |
| Relational / equality `< > <= >= == !=` | ✓ | ✓ | ✓ | ✓ | — | — | L:test1, S:v02 e02 e06 | front end complete |
| Bitwise `& \| ^ ~ << >>` | ✓ | ✓ | ✓ | ✓ | — | — | L:test1, S:v02 e02 | front end complete |
| Assignment and compound assignment | ✓ | ✓ | ✓ | ✓ | — | — | S:v02 e02 e20 | front end complete |
| Unary `+ - ++ --` (pre/post) | ✓ | ✓ | ✓ | ✓ | — | — | P:operators, S:v02 | front end complete |
| Address-of `&`, dereference `*` | ✓ | ✓ | ✓ | ✓ | — | — | S:v06 e06 | front end complete |
| if / if-else / nested if | ✓ | ✓ | ✓ | ✓ | — | — | L:test2, P:if_else, S:v08 e08 | front end complete |
| for loop | ✓ | ✓ | ✓ | ✓ | — | — | P:loops, S:v08 | front end complete |
| while loop | ✓ | ✓ | ✓ | ✓ | — | — | P:loops, S:v08 | front end complete |
| do-while loop | ✓ | ✓ | ✓ | ✓ | — | — | P:loops test16, S:v08 | front end complete |
| switch / case / default (fall-through, multiple labels) | ✓ | ✓ | ✓ | ✓ | — | — | L:test2, P:test4, S:v08 e08 | front end complete |
| break / continue / goto / labels | ✓ | ✓ | ✓ | ◐ | — | — | L:test2, P:test10, S:v08 e08 | front end complete; jumps over initializations are not checked |
| int, char, void (+ short, long, long long, float, double, bool, signed/unsigned) | ✓ | ✓ | ✓ | ✓ | — | — | L:test7, S:v01 | front end complete (`long double` is treated as `double`) |
| Integer and char arrays | ✓ | ✓ | ✓ | ✓ | — | — | P:array, S:v05 e05 | front end complete |
| Pointers | ✓ | ✓ | ✓ | ✓ | — | — | P:pointers, S:v06 e06 | front end complete |
| Structures (nested) | ✓ | ✓ | ✓ | ◐ | — | — | P:test2 test11, S:v07 e07 | front end complete; no brace elision into struct members |
| printf / scanf | ✓ | ✓ | ✓ | ✓ | — | — | P:printf_scanf, S:v09 e10 v24 e20 | front end complete (reserved words; format strings checked) |
| Function declaration / definition / call / arguments / return | ✓ | ✓ | ✓ | ✓ | — | — | P:funcCall test1, S:v04 e04 | front end complete |
| static keyword | ✓ | ✓ | ✓ | ✓ | — | — | L:test2, P:test28, S:v01 | front end complete |

### Advanced features (project specification)

| Feature | Lexer | Parser | AST | Semantic | IR | MIPS | Tests | Status |
|---|---|---|---|---|---|---|---|---|
| Variable-argument functions (`...`, `va_list`, `va_start`, `va_arg`, `va_end`) | ✓ | ✓ | ✓ | ✓ | — | — | L:test4, S:v04 v18 e15 | front end complete |
| Dynamic memory (`malloc` `calloc` `realloc` `free`, `new` `delete` `delete[]`) | ✓ | ✓ | ✓ | ✓ | — | — | L:test4, P:test6, S:v09 e10 | front end complete |
| Command-line input (`int main(int argc, char **argv)`) | ✓ | ✓ | ✓ | ✓ | — | — | S:v12 v13 e11 e12 | front end complete (`main` signature checked) |
| typedef | ✓ | ✓ | ✓ | ✓ | — | — | L:test4, S:v01 v07 | front end complete |
| References (`int &r`, `int *&r`) | ✓ | ✓ | ✓ | ✓ | — | — | S:v11 v18 e14 | front end complete |
| until loop | ✓ | ✓ | ✓ | ✓ | — | — | L:test5, P:test15, S:v08 e08 | front end complete |
| Multi-level pointers | ✓ | ✓ | ✓ | ✓ | — | — | L:test3, S:v06 | front end complete |
| Multi-dimensional arrays | ✓ | ✓ | ✓ | ✓ | — | — | L:test3, S:v05 e05 | front end complete |

### Additional features (not in the specification)

| Feature | Lexer | Parser | AST | Semantic | IR | MIPS | Tests | Status |
|---|---|---|---|---|---|---|---|---|
| Classes, objects, `this`, methods, static members | ✓ | ◐ | ✓ | ◐ | — | — | P:test7 test8 test13, S:v10 e09 | partial: no constructor initializer lists, `virtual`, `const` methods, `friend`, `explicit` |
| Inheritance (single, multiple), inheritance access | ✓ | ✓ | ✓ | ✓ | — | — | S:v10 e09 e14 | front end complete |
| Access modifiers `public` / `protected` / `private` | ✓ | ✓ | ✓ | ✓ | — | — | S:v10 e09 e14 | front end complete |
| Constructors / destructors (in-class, out-of-class, `new T(args)`) | ✓ | ◐ | ✓ | ✓ | — | — | P:test24, S:v17 e15 | partial: no member-initializer lists |
| Operator overloading (member and free) | ✓ | ✓ | ✓ | ✓ | — | — | P:test24, S:v17 e15 | front end complete |
| Function overloading (C++ ranking, ambiguity) | ✓ | ✓ | ✓ | ◐ | — | — | P:test12, S:v11 v16 e04 | front end complete; converting constructors only in initialization |
| Lambdas (`[x, &y]`, `[=]`, `[&]`, `[this]`, `mutable`, `-> T`) | ✓ | ✓ | ✓ | ◐ | — | — | L:test10, S:v11 v18 e10 | front end complete; capture rules checked against the innermost lambda only |
| Function pointers (arrays of, as parameters, typedef'd) | ✓ | ✓ | ✓ | ✓ | — | — | P:funcPtr test9, S:v06 v15 | front end complete |
| enum | ✓ | ✓ | ✓ | ✓ | — | — | L:test3, S:v08 e10 | front end complete (values folded; C rules: `int` converts to an enum) |
| union | ✓ | ✓ | ✓ | ✓ | — | — | L:test3, S:v07 e07 | front end complete |
| File manipulation (`FILE`, `fopen` `fclose` `fread` `fwrite` `fprintf` `fscanf` `fgets` `fputs` `feof`) | ✓ | ✓ | ✓ | ✓ | — | — | L:test8, P:test6 test22, S:v09 e10 | front end complete (reserved words with built-in signatures) |
| Preprocessor (`#define` object/function-like, `#` `##` `__VA_ARGS__`, `#undef`, `#if/#ifdef/#ifndef/#elif/#else/#endif`, `#include "…"`, `#error`, `#pragma once`) | ✓ | ✓ | — | ✓ | — | — | L:test11, P:test26, S:v20 e16 e17 | front end complete; `#include <…>` system headers are accepted and ignored |
| `const`, `volatile`, `auto` (type deduction) | ✓ | ✓ | ✓ | ✓ | — | — | S:v01 v18 | front end complete |
| `extern`, `register` | ✓ | ✓ | ✓ | ✓ | — | — | P:test28, S:v24 e20 | front end complete (linkage, composite types) |
| Casts: C-style `(T)e`, functional `T(e)`, `int(x)` | ✓ | ✓ | ✓ | ✓ | — | — | P:test25, S:v19 | front end complete |
| `sizeof` (expression and type) | ✓ | ✓ | ✓ | ✓ | — | — | S:v02 v22 v24 | front end complete |
| Ternary `?:`, comma operator | ✓ | ✓ | ✓ | ✓ | — | — | S:v02 | front end complete |
| Initializer lists, designated `.x = 1`, `[2] = 7`, empty `{}` | ✓ | ✓ | ✓ | ◐ | — | — | P:test24, S:v05 v18 | front end complete; brace elision for arrays only |
| Unnamed struct/union/enum, anonymous members, anonymous unions | ✓ | ✓ | ✓ | ✓ | — | — | P:test27, S:v22 v23 e18 e19 | front end complete |
| Numeric literals: hex, octal, binary, suffixes `U L LL`, floats `.5` `5.` `1e3f` | ✓ | ✓ | ✓ | ✓ | — | — | L:test5 test7 | front end complete |
| String/char literals, escapes, adjacent string concatenation | ✓ | ✓ | ✓ | ✓ | — | — | L:test6, P:array | front end complete |
| `bool`, `true`, `false` | ✓ | ✓ | ✓ | ✓ | — | — | L:test7, S:v01 | front end complete |
| Itanium C++ name mangling | — | ✓ | — | ✓ | — | — | S:v21 | front end complete (checked against g++) |

### Compiler capabilities (not language features)

| Capability | Where | Tests |
|---|---|---|
| Preprocessing with a line map (errors reported at the original file and line, including headers) | `shared/preprocessor`, `shared/diagnostics` | P:test26, S:v20 e16 e17 |
| Multiple-error reporting: lexer collects all errors; parser recovers at `;` / `}` (Bison `error` productions); semantic analysis reports every error once (de-duplicated) | `lexer.l`, `parser.y`, `SemanticAnalyzer::error()` | L:test6, P:test14–test23 |
| GCC/Clang-style diagnostics: `file:line:col: kind: message`, source line, caret | `printDiagnostic()` in `shared/diagnostics` | all invalid tests |
| Partial AST on syntax errors (`ErrorNode`) | `parser.y` | P:test5, test14–test23 |
| Token / Token_Type table with context classification (`a → INT`, `f → PROCEDURE`) | `parser.y` + parse-time symbol table | all P tests |
| AST construction during parsing, printed as a tree | `shared/ast` | all P tests |
| Annotated AST: every expression's type, lvalue-ness, folded constant, resolved symbol | `phase2b-semantic/src/report.cpp` | all S valid tests |
| Two symbol tables (parse-time, semantic) with scope paths, unique names, use counts | `shared/symbol_table` | see [SYMBOL_TABLE.md](SYMBOL_TABLE.md) |
| MIPS32 record layouts (size, alignment, field offsets) | `layoutRecord()` in `shared/types` | S:v07 v22 v24 |
| Constant folding in the expression's own type, with overflow / shift / conversion warnings | `foldBinary()`, `wrapToType()` | S:v24 e20 |
| Sequence-point check (`i = i++`) | `phase2b-semantic/src/sequencing.cpp` | S:v02 v24 e20 |
| Forward references: calls to functions defined later, `goto` to later labels | `prescan()`, `hoistFunction()`, `collectLabels()`; parser `resolvePendingReferences()` | P:test10, S:v04 |
| Self-checking semantic test runner (expected diagnostics written inline) | `phase2b-semantic/run_tests.sh` | 81 test programs |

## Feature catalog

### A. Basic features — implemented (front end)

All of the specification's basic features: all arithmetic and logical
operators, if-else, for, while, do-while, switch/case, integer and char
arrays, pointers, structures, printf and scanf, function calls with
arguments, goto/break/continue, `static`.

### B. Advanced features — implemented (front end)

All of the specification's advanced features: variable-argument
functions, dynamic memory allocation, command-line input, typedef,
references, the `until` loop, multi-level pointers, multi-dimensional
arrays.

### C. Additional features discovered in the code

Classes/objects/`this`, single and multiple inheritance, access
modifiers, constructors/destructors, operator overloading, function
overloading, lambdas, function pointers, enums, unions, file
manipulation, a C preprocessor, `const`/`volatile`/`auto`,
`extern`/`register`, C-style and functional casts, `sizeof`, ternary
and comma operators, designated and empty initializers, unnamed
aggregates and anonymous unions, hex/octal/binary literals with
suffixes, `bool`, Itanium name mangling — plus the analysis capabilities
listed above (sequence-point warnings, typed constant folding, record
layouts, gcc-style printf/scanf format checking).

### D. Partial features

| Feature | What is missing | Component |
|---|---|---|
| Classes | constructor member-initializer lists (`Dog() : Animal(4) {}` is a syntax error), `virtual` / polymorphism, `const` member functions, `friend`, `explicit` | grammar (`parser.y`) |
| Struct initialization | brace elision into struct members: `struct { int a[2]; int b; } s = {1, 2, 3};` is rejected (and the message calls `s` an "array variable") | `checkInitializer()` |
| Control-flow checks | no flow analysis: "missing return" only when a non-`void` function has no `return` at all; no unreachable-code or uninitialized-use diagnostics; a `goto`/`case` jumping over an initialization is not reported | `statements.cpp` |
| Lambdas | capture rules are checked against the innermost lambda only | `identifier()` |
| Overloading | converting constructors are applied in initialization (`Dog d = 4;`) but not to arguments or returns | `argumentConversion()` |
| Parser member classification | the Token_Type table resolves `p.x` / `p->x` only when the base is a plain identifier (`arr[0].x` stays `IDENTIFIER`); semantic analysis types every form correctly | `parser.y` |
| Phase-1 lexer positions | line numbers only, no columns (the parser's scanner does report columns) | `lexer.l` |
| `long double` | accepted, but treated as `double` | `resolveSpecifiers()` |

### E. Parser-only features

None of the language features is parser-only: every construct the
grammar accepts is also checked by the semantic analyzer. (The
parse-time symbol table's classifications are cosmetic by design; the
semantic phase redoes all name resolution.)

### F. Planned (not implemented)

| Item | State |
|---|---|
| Three Address Code generation (phase 3) | not started — [`phase3-ir/README.md`](../phase3-ir/README.md) |
| TAC optimizations | not started |
| MIPS code generation (phase 4) | not started — [`phase4-codegen/README.md`](../phase4-codegen/README.md) |
| MIPS optimizations, register allocation | not started |

### G. Unsupported (no implementation; rejected as syntax errors)

Bit-fields, default arguments, templates, namespaces, `using` aliases,
exceptions (`try`/`catch`/`throw`), `inline`, `virtual`, `friend`,
`explicit`, `const` member functions, compound literals
(`(struct P){1, 2}`), nested function definitions, `wchar_t` and wide
literals (`L'a'`, `L"..."`).
