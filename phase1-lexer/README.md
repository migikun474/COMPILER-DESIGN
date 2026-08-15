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

* Every token carries a **`TokenType`** — a C++ `enum class` (in
  `include/token_type.hpp`) with one distinct value per keyword and per
  operator/punctuation mark (e.g. `TokenType::IF`, `TokenType::ARROW_OP`,
  `TokenType::OPEN_PAREN_OP`), not a shared category string. This
  replaced an earlier design that used ~9 broad category strings
  (`type_keyword`, `control_keyword`, ...); the switch was made
  specifically to prepare for a parser phase, which generally wants one
  terminal symbol per keyword rather than a shared bucket.
* `to_string(TokenType)` (in `src/token_type.cpp`) converts a `TokenType`
  back to its printable name (e.g. `TokenType::ARROW_OP` → `"arrow_op"`)
  for the table printed at the end.
* Identifiers and keywords share **one** flex rule. The matched text is
  looked up via `reserved_word()` (a `keyword_map`, string → `TokenType`,
  in `src/token_type.cpp`); if found, that keyword's specific
  `TokenType` is used, otherwise it's a plain `IDENTIFIER`. This means
  the flex rules no longer encode keywords directly — adding a keyword
  is a one-line change to `keyword_map`, not a new flex pattern.
* Single-character operators/punctuation similarly share one flex rule
  and resolve their specific `TokenType` via `operator_token()` (an
  `operator_map`) — multi-character operators keep individual flex
  patterns (flex's own longest-match already disambiguates `<<=` vs
  `<<` vs `<` declaratively, so no manual lookahead is needed there).
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
   * Binary: `0b1101` / `0B1101` — validated: a `0b`/`0B` literal
     containing a digit `2`–`9` (e.g. `0b1102`) is a lexical error
     (`Invalid binary literal`).
* Integer suffixes are supported and combinable: `u`/`U` (unsigned),
  `l`/`L` (long), `ll`/`LL` (long long), in either order —
  `45U`, `45L`, `45UL`, `45LU`, `45LL`, `45ULL`, `45LLU` all lex as one
  `int_literal`. Mixed-case `long long` (`45lL`) is **not** valid
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
   * Leading or trailing dot: `.5`, `5.` (a digit is required on at
     least one side of the `.`, but not both — a lone `.` with no digit
     either side stays the `.` operator, unaffected)
   * Scientific notation: `1.23e4` / `1.23E4`, `1.23e-4` / `1.23E-4`
   * Optional trailing `f`/`F` suffix: `3.14f`

> **Note**
> Not supported: an `l`/`L` (long double) suffix on floats — only
> `f`/`F` is recognized.

## Reserved Keywords and Identifiers

* Keywords are stored in `keyword_map` (`src/token_type.cpp`) — a
  `std::unordered_map<std::string, TokenType>`. A word either matches an
  entry in this map (and becomes that specific keyword's `TokenType`) or
  falls through to the generic identifier pattern
  `{LETTER}({LETTER}|{DIGIT})*`.
* Every keyword gets its **own** `TokenType` — `IF`, `WHILE`, `INT`,
  `CLASS`, `PUBLIC`, and so on are all distinct values, not grouped
  under a shared category the way an earlier version of this lexer did:

  | Group | Keywords |
  |---|---|
  | primitive types | `int char float double void short long signed unsigned` |
  | composite types | `struct enum union class` |
  | access modifiers | `public private protected` |
  | object-oriented | `this` |
  | storage class | `static typedef auto` |
  | control flow | `if else for while do until switch case default break continue goto return` |
  | I/O (custom) | `printf scanf` |
  | dynamic memory (custom) | `malloc free calloc realloc` |
  | file manipulation (custom) | `FILE fopen fclose fread fwrite fprintf fscanf fgets fputs feof` |

* **This language intentionally diverges from real C** in several
  places:
   * `printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`, `FILE`,
     `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`,
     `fputs`, `feof` are reserved keywords here, not ordinary
     library-function identifiers as in real C.
   * `until` is reserved; real C has no until loop.
   * `true`/`false` are reserved (that's C++ or C23's `<stdbool.h>`, not
     C). Categorized as `BOOL_LITERAL`, not a keyword `TokenType`, since
     (like `INT_LITERAL`/`STRING_LITERAL`) they denote a value rather
     than a structural role — but they're still looked up via
     `keyword_map` like any other reserved word.
   * `class`, `public`, `private`, `protected`, `this` are reserved for
     this language's object-oriented features; real C has none of them.
* **Not supported: boolean *type*.** There is no `bool` type keyword to
  declare a variable of that type — you can currently only assign
  `true`/`false` to an `int`. Flag it if you want a `bool` type added.
* **Lambda functions need no new tokens at all.** This language uses
  C++-style lambda syntax — `[capture](params) { body }`, optionally
  with a trailing `-> returnType` — and every piece of that already
  decomposes into existing tokens: `[`/`]` (already used for arrays),
  `(`/`)`, `{`/`}`, `->` (already used for pointer member access), plus
  ordinary operators/identifiers inside the capture list (`&`, `=`,
  `,`, and even `this` for capturing the enclosing object). Verified by
  running every capture form (empty, `&`, `=`, mixed named captures,
  explicit return type, capturing `this`) through the lexer — nothing
  needed to change in `lexer.l`. The one real gap this exposed: `auto`
  wasn't a keyword, which matters specifically for lambdas since
  `auto f = [](...){...};` is the only sensible way to hold a lambda's
  value in this language — fixed alongside this (`AUTO` is now a
  storage-class-style keyword, see above).
* **Not supported yet: `new`/`delete`/operator overloading.** Only
  `class`/access-modifiers/`this`/scope-resolution were built — real
  C++-style object construction/destruction keywords weren't requested,
  flagging in case they're wanted too.
* **Not supported yet: typedef-name tracking.** Real C-style grammars
  need the lexer to remember that a name was `typedef`'d so it can be
  classified as a type (not a plain identifier) on later use — this
  lexer doesn't track that yet; every identifier, `typedef`'d or not, is
  just `IDENTIFIER`.
* `sizeof` is currently an ordinary `identifier`, not a keyword.
* To add a new reserved keyword: add one line to `keyword_map` in
  `src/token_type.cpp` (and its `TokenType` enum value in
  `token_type.hpp`, and its printable name in `token_to_string_map`) —
  `src/lexer.l` itself needs no changes.

## Operators

* Every operator/punctuation mark gets its own `TokenType` too (e.g.
  `PLUS_OP`, `ARROW_OP`, `OPEN_PAREN_OP`, `SEMICOLON_OP`) — punctuation
  isn't a separate category from "operators" here, it's just more
  entries in the same scheme (matching a reference lexer's convention of
  suffixing everything, including parens/braces/semicolons, with `_OP`).
* Multi-character operators (`<<=`, `->`, `::`, `...`, etc.) each keep
  their own flex pattern, ordered longest-first for readability — flex's
  built-in longest-match resolves ambiguity (`<<=` beats `<<` beats `<`
  whenever the longer form is actually present) regardless of rule
  order, so this is about clarity, not correctness. Each rule assigns
  its specific `TokenType` directly.
* Single-character operators/punctuation share one flex rule; since many
  different characters match that one pattern, the specific `TokenType`
  is resolved via `operator_token()` (`operator_map` in
  `src/token_type.cpp`) at match time.
* Full set: `+ - * / % = == != < > <= >= && || ! & | ^ ~ << >> ++ -- +=
  -= *= /= %= &= |= ^= -> . , ? : ::`, plus `...` (`ELLIPSIS_OP`, for
  variable-argument functions) and `::` (`SCOPE_RESOLUTION_OP`, for
  `ClassName::member`).
* Adding a new operator: add its `TokenType` to `token_type.hpp`, an
  entry to `operator_map`/`token_to_string_map` in `token_type.cpp`,
  and — only if it's multi-character — one flex rule in `src/lexer.l`
  (single-character operators need no `lexer.l` change at all, since
  they already fall through to the table-lookup rule).

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
> separate valid tokens — `int_literal "12"` then `identifier
> "abc"` — and a future parser is expected to reject the resulting
> nonsensical token sequence as a syntax error instead. The same
> applies to `3.14x` and to the invalid-suffix case `45lL` mentioned
> above (→ `int_literal "45l"` + `identifier "L"`).
> The narrower `089`-style invalid-octal-digit check is a *separate*
> rule and is unaffected by this — it still errors.

## Conclusion

* The current lexer prints a two-column table of every token's
  **lexeme** (raw source text) and **`TokenType`** (converted to a
  printable name via `to_string()`) — it does not decode escape
  sequences or numeric literals into actual runtime values (e.g.
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
* Extensible in the areas this phase cares about: new keywords are a
  one-line addition to `keyword_map`, new operators are a `TokenType` +
  map entries (+ a flex rule if multi-character), and new error
  categories are a localized change in `src/lexer.l` (see the relevant
  sections above for exactly where).

## Test cases (`test/`)

| File | Covers |
|---|---|
| `test1_arithmetic_logical.c` | all arithmetic, relational, logical, bitwise, assignment operators |
| `test2_control_flow.c` | if-else, for, while, do-while, switch-case, goto, break, continue, static, until |
| `test3_arrays_pointers_structs.c` | int/char arrays, multi-dim arrays, pointers, multi-level pointers, structs, enums, unions |
| `test4_functions_advanced.c` | function calls with arguments, varargs (`...`), dynamic memory allocation, argc/argv, typedef, reference |
| `test5_until_loop.c` | until loop, float/hex/char/string constants |
| `test6_lexical_errors.c` | intentionally broken input to exercise every error type above (10 errors: unterminated char, unterminated string, illegal char, multi-char literal, invalid escape, bad hex escape, bad octal escape, invalid octal literal, invalid binary literal, unterminated comment) |
| `test7_type_modifiers_and_custom_keywords.c` | `short`/`long`/`long long`/`signed`/`unsigned` type modifiers, hex/octal/binary literals, integer suffixes (`U`/`L`/`LL` combinations), leading/trailing-dot floats (`.5`/`5.`), boolean literals (`true`/`false`), and this language's custom I/O and memory-allocation reserved words (`printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`) |
| `test8_file_manipulation.c` | this language's custom file-manipulation reserved words (`FILE`, `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`, `fputs`, `feof`) |
| `test9_classes_and_objects.c` | object-oriented keywords/operators: `class`, access modifiers (`public`/`private`/`protected`), `this`, scope resolution (`::`), and a lambda capturing `this` |
| `test10_lambda_functions.c` | C++-style lambda expressions: empty/`&`/`=`/mixed capture lists, trailing return type (`-> int`), `auto` |
