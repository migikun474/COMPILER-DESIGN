# Project Description (source spec)

Transcribed from the project's Google Form submission.

- **Source Language:** C-like language
- **Intermediate Representation:** 3 Address Code
- **Target Language:** MIPS
- **Implementation Language:** C++

## Basic features to be implemented

- All arithmetic and logical operators
- if-else
- for loop
- while loop
- do-while loop
- switch cases
- arrays (integer and char)
- pointers
- structures
- printf and scanf
- function call with arguments
- goto, break and continue
- static keyword

## Advanced features to be implemented

- Function call with variable arguments
- Dynamic memory allocation
- Command line input
- typedef
- Reference
- until loop
- Multi-level pointers
- Multi-dimensional arrays

## Phase 1 requirements — Lexical Analyzer

Write a lexical analyzer that tokenizes the source language into lexemes
(lex/flex for C/C++, PLY for Python).

**Expected output:**
- Valid program → a two-column table of `Lexeme` and `Token`.
- Program with a lexical error → report all lexical errors found.

**Expected deliverables:**
- `src/` — the lex/flex/python source for the tokenizer
- `test/` — minimum 5 test cases covering all implemented features
- `makefile` — recipe to compile the lex/flex file into an executable
- `run.sh` — script that takes the executable and runs it over every test
  case in `test/`
