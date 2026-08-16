# Compiler Project

A compiler for a C-like source language, built in phases.

| | |
|---|---|
| Source language   | C-like language |
| Intermediate rep. | Three Address Code |
| Target language   | MIPS |
| Implementation    | C++ |

## Layout

```
compiler-project/
├── phase1-lexer/     Lexical analyzer     -- done
├── phase2-parser/    Syntax analyzer / parser           -- not started
├── phase3-ir/        Three Address Code generation      -- not started
├── phase4-codegen/   MIPS code generation                -- not started
└── docs/             Project spec and design notes
```

Each phase directory is self-contained: `src/` (source), `test/` (test
cases), `makefile` (build recipe), and `run.sh` (runs the built executable
over every test case). Build a phase with `make` inside its directory, then
`./run.sh` to run all tests, or `./run.sh /path/to/other/executable` to run
a specific binary.

## Phase 1 — Lexical Analyzer

Tokenizes the source language into lexemes using flex. On clean input it
prints a Lexeme/Token table; on invalid input it reports every lexical
error found (line number + description) instead.

```bash
cd phase1-lexer
make            # builds ./lexer
./run.sh        # runs ./lexer over every file in test/
./lexer test/test1_arithmetic_logical.c   # run on a single file
```

See [`phase1-lexer/README.md`](phase1-lexer/README.md) for the full
token/keyword reference and [`docs/project_description.md`](docs/project_description.md)
for the full feature/design-decision history.

## Features implemented (per project spec)

**Basic:** arithmetic/logical operators, if-else, for, while, do-while,
switch-case, int/char arrays, pointers, structures, printf/scanf,
function calls with arguments, goto/break/continue, static.

**Advanced:** variable-argument function calls, dynamic memory allocation,
command-line input (argc/argv), typedef, reference, until loop,
multi-level pointers, multi-dimensional arrays.

## Features added beyond the original spec

Requested and implemented after the initial spec — see
[`docs/project_description.md`](docs/project_description.md#features-added-beyond-the-original-spec)
for the full writeup of each:

- **enum, union** — composite-type keywords, same treatment as `struct`
- **Boolean literals** — `true`/`false` (no `bool` type keyword yet)
- **File manipulation** — `FILE`, `fopen`, `fclose`, `fread`, `fwrite`,
  `fprintf`, `fscanf`, `fgets`, `fputs`, `feof`, all reserved as keywords
- **Object-oriented features** — `class`, access modifiers
  (`public`/`private`/`protected`), `this`, scope resolution (`::`)
- **Lambda functions** — C++-style `[capture](params) { body }` syntax
- **Numeric literal completeness** — binary literals (`0b1101`), octal
  literals with digit validation, combinable integer suffixes
  (`u`/`l`/`ll`), leading/trailing-dot floats (`.5`, `5.`)

This language also deliberately diverges from real C in several places
(custom reserved keywords, stricter char literals, and more) — see
[Deviations from Real C (and Why)](phase1-lexer/README.md#deviations-from-real-c-and-why)
for the full list with justifications.
