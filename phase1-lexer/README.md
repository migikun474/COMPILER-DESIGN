# Phase 1 — Lexical Analyzer

Built with **flex**, compiled as C++.

## Build & run

```bash
make            # generates lex.yy.c and builds ./lexer
./run.sh        # runs ./lexer over every *.c file in test/
./lexer <file>  # run on a single source file
make clean      # remove build artifacts
```

## General

* All tokens produced by the lexer carry a **token category** as a plain
  string (e.g. `identifier`, `type_keyword`, `operator`) rather than an
  enum from a separate `token_type.hpp`-style file. The category *is*
  the type — there's no extra `to_string` conversion step needed.
* The lexer uses **flex**, compiled as C++. Rules are defined in
  `src/lexer.l`.
* For finding the line number, the `yylineno` feature is used.
* **Column number is not tracked** — only line numbers are recorded on
  tokens and errors. (A reference lexer we compared against tracks both
  line and column via a `YY_USER_ACTION` macro; ours only does line
  number for now.)

## Comments

* Comments are skipped — never emitted as tokens.
* Single-line comments start with `//` and run to end of line.
* Multi-line comments start with `/*` and end with `*/`, and can span
  multiple lines via an exclusive flex start-condition (`COMMENTSTATE`).
* An unterminated `/*` that runs to end-of-file is reported as a lexical
  error (`Unterminated block comment`) instead of silently swallowing
  the rest of the file.

## Strings

* Strings are enclosed in double quotes `"` and may contain escape
  sequences.
* The lexer enters an exclusive `STRSTATE` start-condition on `"` and
  accumulates characters until the closing `"`.
* An unescaped newline before the closing quote is a lexical error
  (`Unterminated string literal`) — strings cannot span multiple lines.
  Running off the end of the file inside a string is also an error.

## Escaped Characters

* Escape sequences are recognized and **validated** inside both string
  and character literals, using the same rules for both.
* Valid escapes: `\n \t \r \\ \' \" \a \b \f \v \?` (simple escapes),
  octal `\ddd` (1–3 digits, each `0`–`7`), and hex `\xH+` (one or more
  hex digits, unbounded — unlike some implementations that cap it at 2
  digits for a single byte).
* Anything else after a `\` — e.g. `\q`, `\xz` (`x` with no valid hex
  digit following), `\8`/`\9` (not valid octal digits) — is a lexical
  error (`Invalid escape sequence`), and the literal containing it is
  excluded from the printed token table.

## Int Literals

* Supported bases:
   * Decimal: `123`
   * Octal: `017` — validated: a leading-zero literal containing digit
     `8` or `9` (e.g. `089`) is a lexical error
     (`Invalid octal literal`), matching real C's octal-constant
     grammar.
   * Hexadecimal: `0x1F` / `0X1F`
* **Not supported: binary literals** (`0b1101`). A reference lexer we
  compared against has these; ours doesn't yet — flag it if you want
  this added.
* Integer suffixes are supported and combinable: `u`/`U` (unsigned),
  `l`/`L` (long), `ll`/`LL` (long long), in either order —
  `45U`, `45L`, `45UL`, `45LU`, `45LL`, `45ULL`, `45LLU` all lex as one
  `integer_constant`. Mixed-case `long long` (`45lL`) is **not** valid
  (real C requires `ll` or `LL` consistently, never `lL`/`Ll`) — see the
  note on malformed literals below for what happens to it now.
* Char literals are enclosed in single quotes `'` and may contain a
  single character or a single escape sequence — same escape rules as
  strings. **This language requires exactly one character inside
  `'...'`**: `''` is a lexical error (`Empty character literal`) and
  `'AB'` is a lexical error (`Too many characters in character
  literal`). This is stricter than real C, which permits multi-character
  constants as an implementation-defined extension (a warning, not an
  error, in gcc/clang) — a deliberate design choice for this language.

## Float Literals

* Supported formats:
   * Standard decimal notation: `123.456`
   * Scientific notation: `1.23e4` / `1.23E4`, `1.23e-4` / `1.23E-4`
   * Optional trailing `f`/`F` suffix: `3.14f`

> **Note**
> Float literals do **not** support patterns like `.123` or `123.`
> (a digit required on *both* sides of the `.`) — this is a known,
> unfixed gap, not a deliberate design choice. `.5` currently lexes as
> `.` (operator) then `5` (integer_constant); `5.` lexes as `5`
> (integer_constant) then `.` (operator). Flag it if you want this
> fixed.
> Also not supported: an `l`/`L` (long double) suffix on floats — only
> `f`/`F` is recognized.

## Reserved Keywords and Identifiers

* There's no separate `reserved_words` map checked at runtime — each
  keyword category is its own flex rule, matched directly against
  literal alternations (e.g. `"int"|"char"|"float"|...`) as part of the
  generated scanner itself. A word either matches one of these literal
  alternations (and becomes that keyword's category) or falls through
  to the generic identifier pattern `{LETTER}({LETTER}|{DIGIT})*`.
* Keywords are split into **nine categories** instead of one flat
  `keyword` token, so a later symbol-table/parser phase can act on a
  token's role directly:

  | Category | Keywords |
  |---|---|
  | `type_keyword` | `int char float double void short long signed unsigned` |
  | `struct_keyword` | `struct` |
  | `enum_keyword` | `enum` |
  | `union_keyword` | `union` |
  | `storage_keyword` | `static typedef` |
  | `control_keyword` | `if else for while do until switch case default break continue goto return` |
  | `io_keyword` | `printf scanf` |
  | `memory_keyword` | `malloc free calloc realloc` |
  | `file_keyword` | `FILE fopen fclose fread fwrite fprintf fscanf fgets fputs feof` |

* **This language intentionally diverges from real C**: `printf`,
  `scanf`, `malloc`, `free`, `calloc`, `realloc`, `FILE`, `fopen`,
  `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`, `fputs`,
  `feof` are reserved keywords here, not ordinary library-function
  identifiers as in real C — they can never be used as a variable or
  function name in this language. `until` is also reserved; real C has
  no until loop.
* **Not supported: boolean literals** (`true`/`false`). A reference
  lexer we compared against recognizes these as a `BOOL_LITERAL` token;
  ours has no boolean keyword at all currently.
* `sizeof` is currently an ordinary `identifier`, not a keyword.
* To add a new reserved keyword in this codebase: add it to the
  relevant category's literal alternation in `src/lexer.l` — that's the
  only file that needs changing (no separate enum/map files to keep in
  sync).

## Operators

* Operators are matched via **explicit flex rules**, one pattern per
  operator (or a `|`-separated group for same-length ones), ordered
  longest-first (`<<=` before `<<` before `<`, etc.) so flex's built-in
  maximal-munch resolves ambiguity automatically — no manual
  character-by-character lookahead (`yyinput`/`unput`) is needed the
  way a runtime operator-table approach would require.
* Full set: `+ - * / % = == != < > <= >= && || ! & | ^ ~ << >> ++ -- +=
  -= *= /= %= &= |= ^= -> . , ? :`, plus `...` as its own `ellipsis`
  token (variable-argument functions).
* Adding a new operator: add one flex rule line to `src/lexer.l`, placed
  above any shorter operator it could be confused with.

## Error Handling

* Anything not matched by any rule above is an `Illegal character`
  error via a catch-all `.` rule at the very end of the ruleset.
* Errors are collected into a `diagnostics` vector via a `reportError()`
  function (line, offending lexeme, message) — **all** errors in the
  file are collected in one pass, not just the first one, per this
  project's spec ("report all the lexical errors in your input
  program").
* If any errors were found: the table is **not** printed. Instead every
  error is printed to stderr (`Line <n>: <message> (near '<lexeme>')`),
  and a full report is written to `logs/<source-file-stem>.log`.
* If the file is completely clean: the two-column `Lexeme` / `Token`
  table is printed instead.

> **Note — deliberate design choice**
> A digit followed directly by letters (e.g. `12abc`, `3.14x`) is
> **not** flagged as a lexical error here, even though real C/C++
> actually do diagnose this at the lexical level (gcc's `invalid
> suffix "abc" on integer constant`). This lexer only recognizes valid
> token shapes and does no such pre-validation: `12abc` lexes as two
> separate valid tokens — `integer_constant "12"` then `identifier
> "abc"` — and a future parser is expected to reject the resulting
> nonsensical token sequence as a syntax error instead. The same
> applies to `3.14x` and to the invalid-suffix case `45lL` mentioned
> above (→ `integer_constant "45l"` + `identifier "L"`).
> The narrower `089`-style invalid-octal-digit check is a *separate*
> rule and is unaffected by this — it still errors.

## Conclusion

* The current lexer prints a two-column table of every token's
  **lexeme** (raw source text) and **category** — it does not decode
  escape sequences or numeric literals into actual runtime values (e.g.
  `\x41` is stored as the 4-character source string `\x41`, not decoded
  to the byte `0x41`). A reference lexer we compared against does
  decode into real semantic values via Bison's `yylval`; that's a
  meaningful gap for whenever this lexer gets wired into Phase 2's
  parser, not just a cosmetic difference.
* The lexer batch-tokenizes the entire input file in one call and
  prints everything at the end, rather than returning one token per
  call on demand the way a parser-driven lexer (`getNextToken()` style)
  would. This is the right shape for Phase 1's own deliverable (a
  printed table / error report) but will need refactoring before
  Phase 2's parser can drive it directly.
* Extensible in the areas this phase cares about: new keywords, new
  operators, and new error categories are all single, localized changes
  in `src/lexer.l` (see the relevant sections above for exactly where).

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
