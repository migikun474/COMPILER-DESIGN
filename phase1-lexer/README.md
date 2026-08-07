# Phase 1 — Lexical Analyzer

Built with **flex**, compiled as C++.

## Build & run

```bash
make            # generates lex.yy.c and builds ./lexer
./run.sh        # runs ./lexer over every *.c file in test/
./lexer <file>  # run on a single source file
make clean      # remove build artifacts
```

## Output

- Clean input → a two-column `Lexeme  Token` table, one row per token.
- Input with lexical errors → every error found, each on its own line as
  `Line <n>: <description>`, instead of the table.

## Token categories

| Token name          | Examples |
|---|---|
| `keyword`            | `int char float double void struct typedef static if else for while do until switch case default break continue goto return` |
| `identifier`         | `foo`, `_count`, `main` |
| `integer_constant`   | `42`, `0x1F` |
| `float_constant`     | `3.14`, `3.14159f`, `1.5e-3` |
| `char_constant`      | `'a'`, `'\n'` |
| `string_literal`     | `"hello, world\n"` |
| `operator`           | `+ - * / % = == != < > <= >= && \|\| ! & \| ^ ~ << >> ++ -- += -= *= /= %= &= \|= ^= -> . , ? :` |
| `ellipsis`            | `...` (variable-argument function calls) |
| `punctuation`        | `( ) { } [ ] ;` |

Notes:
- `printf`/`scanf`/`malloc`/`free` are ordinary identifiers (as in real C —
  they're library functions, not keywords).
- `&` is reused for both address-of and reference parameters; disambiguated
  later by the parser, not the lexer.
- Comments (`// ...` and `/* ... */`) are skipped, not emitted as tokens.

## Detected lexical errors

- Illegal / unrecognized characters
- Unterminated string literals
- Unterminated char literals
- Unterminated block comments
- Malformed numeric literals (e.g. `12abc`, `3.14x`)

## Test cases (`test/`)

| File | Covers |
|---|---|
| `test1_arithmetic_logical.c` | all arithmetic, relational, logical, bitwise, assignment operators |
| `test2_control_flow.c` | if-else, for, while, do-while, switch-case, goto, break, continue, static, until |
| `test3_arrays_pointers_structs.c` | int/char arrays, multi-dim arrays, pointers, multi-level pointers, structs |
| `test4_functions_advanced.c` | function calls with arguments, varargs (`...`), dynamic memory allocation, argc/argv, typedef, reference |
| `test5_until_loop.c` | until loop, float/hex/char/string constants |
| `test6_lexical_errors.c` | intentionally broken input to exercise every error type above |
