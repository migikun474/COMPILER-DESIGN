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

See `phase1-lexer/README.md` for the full token/keyword reference.

## Features implemented (per project spec)

**Basic:** arithmetic/logical operators, if-else, for, while, do-while,
switch-case, int/char arrays, pointers, structures, printf/scanf,
function calls with arguments, goto/break/continue, static.

**Advanced:** variable-argument function calls, dynamic memory allocation,
command-line input (argc/argv), typedef, reference, until loop,
multi-level pointers, multi-dimensional arrays.
