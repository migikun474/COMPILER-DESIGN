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
| `enum_keyword`        | `enum` |
| `union_keyword`       | `union` |
| `storage_keyword`    | `static typedef` |
| `control_keyword`    | `if else for while do until switch case default break continue goto return` |
| `io_keyword`         | `printf scanf` |
| `memory_keyword`     | `malloc free calloc realloc` |
| `file_keyword`       | `FILE fopen fclose fread fwrite fprintf fscanf fgets fputs feof` |
| `identifier`         | `foo`, `_count`, `main` |
| `integer_constant`   | `42`, `0x1F` (hex), `017` (octal), `45U`, `45UL`, `45LL`, `45ULL` (integer suffixes: unsigned/long/long-long, any valid order/case) |
| `float_constant`     | `3.14`, `3.14159f`, `1.5e-3` |
| `char_constant`      | `'a'`, `'\n'` |
| `string_literal`     | `"hello, world\n"` |
| `operator`           | `+ - * / % = == != < > <= >= && \|\| ! & \| ^ ~ << >> ++ -- += -= *= /= %= &= \|= ^= -> . , ? :` |
| `ellipsis`            | `...` (variable-argument function calls) |
| `punctuation`        | `( ) { } [ ] ;` |

Notes:
- **This language intentionally diverges from real C** on which words are
  reserved: `printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`,
  `FILE`, `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`,
  `fgets`, `fputs`, `feof` are keywords here, not ordinary library
  identifiers as in real C. That means (unlike real C) they can never be
  used as a variable or function name in this language.
- `until` is also a reserved keyword; real C has no until loop.
- Keywords are split into nine specific categories (above) instead of one
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
- **Design decision: a digit followed directly by letters is NOT a
  lexical error here.** `12abc` lexes as two separate valid tokens —
  `integer_constant "12"` then `identifier "abc"` — with no error
  raised. Real C/C++ actually treat this as a single invalid
  "preprocessing number" token and diagnose it right there (that's what
  gcc's `invalid suffix "abc" on integer constant` error is), which
  is arguably the more standard-compliant behavior. This project
  deliberately diverges from that: the lexer only recognizes valid
  token shapes and does no numeric-literal-specific pre-validation
  beyond that; a malformed sequence like `12abc` is left to produce a
  nonsensical token stream that the (future) parser will reject as a
  syntax error, instead of the lexer catching it. The same applies to
  `3.14x` (→ `float_constant "3.14"` + `identifier "x"`) and `45lL`
  (→ `integer_constant "45l"` + `identifier "L"`, since the mixed-case
  suffix stops early instead of being flagged). Note this means Phase 1
  alone will print a "clean" table for these inputs — the error only
  surfaces once Phase 2's parser exists.

## Detected lexical errors

- Illegal / unrecognized characters
- Unterminated string literals
- Unterminated char literals
- Unterminated block comments
- Invalid octal literals — a leading-zero literal containing digit `8`
  or `9` (e.g. `089`), matching real C's octal-constant grammar. Note:
  this one is still caught here even though `12abc`-style malformed
  literals are not (see design decision above) — it's a separate,
  narrower rule that specifically validates octal digit range, not a
  general "digits followed by garbage" catch-all.
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
| `test3_arrays_pointers_structs.c` | int/char arrays, multi-dim arrays, pointers, multi-level pointers, structs, enums, unions |
| `test4_functions_advanced.c` | function calls with arguments, varargs (`...`), dynamic memory allocation, argc/argv, typedef, reference |
| `test5_until_loop.c` | until loop, float/hex/char/string constants |
| `test6_lexical_errors.c` | intentionally broken input to exercise every error type above (9 errors: unterminated char, unterminated string, illegal char, multi-char literal, invalid escape, bad hex escape, bad octal escape, invalid octal literal, unterminated comment) |
| `test7_type_modifiers_and_custom_keywords.c` | `short`/`long`/`long long`/`signed`/`unsigned` type modifiers, hex/octal literals, integer suffixes (`U`/`L`/`LL` combinations), and this language's custom `io_keyword`/`memory_keyword` reserved words (`printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`) |
| `test8_file_manipulation.c` | this language's custom `file_keyword` reserved words (`FILE`, `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`, `fputs`, `feof`) |
