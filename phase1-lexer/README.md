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
| `type_keyword`       | `int char float double void short long signed unsigned` |
| `struct_keyword`     | `struct` |
| `storage_keyword`    | `static typedef` |
| `control_keyword`    | `if else for while do until switch case default break continue goto return` |
| `io_keyword`         | `printf scanf` |
| `memory_keyword`     | `malloc free calloc realloc` |
| `identifier`         | `foo`, `_count`, `main` |
| `integer_constant`   | `42`, `0x1F` |
| `float_constant`     | `3.14`, `3.14159f`, `1.5e-3` |
| `char_constant`      | `'a'`, `'\n'` |
| `string_literal`     | `"hello, world\n"` |
| `operator`           | `+ - * / % = == != < > <= >= && \|\| ! & \| ^ ~ << >> ++ -- += -= *= /= %= &= \|= ^= -> . , ? :` |
| `ellipsis`            | `...` (variable-argument function calls) |
| `punctuation`        | `( ) { } [ ] ;` |

Notes:
- **This language intentionally diverges from real C** on which words are
  reserved: `printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc` are
  keywords here, not ordinary library-function identifiers as in real C.
  That means (unlike real C) they can never be used as a variable or
  function name in this language.
- `until` is also a reserved keyword; real C has no until loop.
- Keywords are split into six specific categories (above) instead of one
  flat `keyword` token, so the parser/symbol-table phase can act on a
  token's role directly instead of re-classifying every keyword string
  again.
- `long long` lexes as **two** consecutive `long` (`type_keyword`) tokens,
  same as real C — there's no single combined token for it, since a
  lexer can't tell "two keywords in a row" apart from "one compound
  keyword" without introducing an artificial special case. The parser
  is expected to recognize the `long long` sequence as one type.
- `&` is reused for both address-of and reference parameters; disambiguated
  later by the parser, not the lexer.
- Comments (`// ...` and `/* ... */`) are skipped, not emitted as tokens.
- `sizeof` is currently an ordinary `identifier`, same as in the original
  build — it isn't in the project's required feature list, so it hasn't
  been made a keyword. Flag it if you want it reserved too.

## Detected lexical errors

- Illegal / unrecognized characters
- Unterminated string literals
- Unterminated char literals
- Unterminated block comments
- Malformed numeric literals (e.g. `12abc`, `3.14x`)
- Invalid escape sequences in strings/chars (e.g. `\q`, `\xz`, `\89` —
  digits 8/9 aren't valid octal digits). Valid escapes: `\n \t \r \\ \'
  \" \a \b \f \v \?`, octal `\ddd` (1–3 digits, 0–7), and hex `\xH+`
  (one or more hex digits).
- Empty character literals (`''`) — this language requires exactly one
  character (or one escape) inside `'...'`, unlike real C which permits
  multi-character constants as an implementation-defined extension; here
  `'AB'` is a lexical error, not just a compiler warning.
- Char literals with more than one character (`'AB'`) — see above.

## Test cases (`test/`)

| File | Covers |
|---|---|
| `test1_arithmetic_logical.c` | all arithmetic, relational, logical, bitwise, assignment operators |
| `test2_control_flow.c` | if-else, for, while, do-while, switch-case, goto, break, continue, static, until |
| `test3_arrays_pointers_structs.c` | int/char arrays, multi-dim arrays, pointers, multi-level pointers, structs |
| `test4_functions_advanced.c` | function calls with arguments, varargs (`...`), dynamic memory allocation, argc/argv, typedef, reference |
| `test5_until_loop.c` | until loop, float/hex/char/string constants |
| `test6_lexical_errors.c` | intentionally broken input to exercise every error type above (10 errors: bad numeric literal, unterminated char, unterminated string, illegal char, malformed float, multi-char literal, invalid escape, bad hex escape, bad octal escape, unterminated comment) |
| `test7_type_modifiers_and_custom_keywords.c` | `short`/`long`/`long long`/`signed`/`unsigned` type modifiers, and this language's custom `io_keyword`/`memory_keyword` reserved words (`printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`) |
