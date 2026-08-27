# Phase 1 — Lexical Analyzer

Built with **flex**, compiled as C++.

## Build & run

```bash
make            # generates lex.yy.c and builds ./lexer
./run.sh        # runs ./lexer over every *.c file in test/
./lexer <file>  # run on a single source file
make clean      # remove build artifacts
```

## Deviations from Real C (and Why)

Every place this language's lexer behaves differently from a real C
compiler, gathered in one place with the reasoning behind each, instead
of scattered across the sections below where they're easy to miss.

| Deviation | What real C does instead | Why this language does it differently |
|---|---|---|
| `printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`, `FILE`, `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`, `fputs`, `feof` are **reserved keywords** | These are ordinary `<stdio.h>`/`<stdlib.h>` library functions — just identifiers, usable as variable names (`int malloc = 5;` is legal C) | This is a custom language, not a strict C clone. Reserving the core I/O and memory-management vocabulary as keywords means the parser/symbol-table phase never has to special-case "well-known library names" — it can treat them as structural tokens from the start, the same way `if`/`while` are. Trade-off, accepted deliberately: these names can never be reused as variables here, unlike real C. |
| `until` is a **reserved keyword** | No such keyword exists | Directly requested by this project's own spec (an intentional extra loop construct), not a deviation from *this* project's requirements — only from real C. |
| `true`/`false` are **reserved literals** | No boolean keywords exist in C89–C17 (that's C++, or C23's `<stdbool.h>`) | Adopted for more ergonomic boolean literal support. Note there's still no `bool` *type* keyword — only the two literals exist so far. |
| Char literals must contain **exactly one character** — `''` and `'AB'` are lexical errors | C permits multi-character constants (`'AB'`) as a legal, if unusual, implementation-defined extension — gcc/clang only warn, never error | Multi-character constants are a genuinely obscure C feature whose numeric value is implementation-defined and rarely intentional — treating them as an error catches likely mistakes instead of silently accepting ambiguous input. |
| `class`, `public`, `private`, `protected`, `this`, `::` are **reserved** | None of these exist in C at all | Added to support this language's object-oriented features (classes, access control, scope resolution) — a deliberate extension toward C++-style OOP on top of the C-like base. |
| C++-style lambda syntax `[capture](params) { body }` is supported, using **existing tokens only** | C has no lambda syntax at all | Chosen (among several possible syntaxes) specifically because it needed **zero new lexer tokens** — every piece already existed (`[`/`]` from arrays, `->` from pointer access, etc.), verified by testing every capture form. The one real consequence: `auto` had to become a keyword too, since it's the only way to hold a lambda's value here. |
| A digit followed directly by letters (`12abc`, `0x` with no hex digits, `45lL`) is **not a lexical error** — it lexes as two separate valid tokens instead | Real C/C++ lock this into a single "preprocessing number" token via maximal munch *before* any validity check happens, so `12abc` can never split apart — it's diagnosed immediately as one malformed token (gcc: `invalid suffix "abc" on integer constant`) | **Explicit, considered reversal** of this lexer's original behavior (which *did* match real C here), made after comparing against a reference lexer that takes this approach. The lexer now only recognizes valid token shapes and does no such pre-validation; a future parser is expected to reject the resulting nonsensical token sequence instead. Trade-off, accepted deliberately: Phase 1 alone gives no diagnostic for this case — the error only becomes visible once Phase 2's parser exists, and the eventual message (a generic syntax error) will be less specific than the lexical diagnostic this project used to give. |
| Digit-range checks *within* a stated base (`089`, `0b1102`, and the zero-digit boundary case `0x`/`0b` with nothing valid after) **are still lexical errors** | Also flagged by real compilers, though via the same preprocessing-number mechanism as the row above | Deliberately **not** covered by the reversal above — validating a digit against its own declared base (is `8` a legal octal digit? did `0x` get *any* hex digit at all?) is a narrower, self-contained check, not the "digit + arbitrary trailing garbage" pattern that row is about. The key distinction from `12abc`: `12` is already a complete, valid, self-sufficient number on its own — splitting there just defers "what comes after"; `0x` alone was never a complete number to begin with, there's no valid prefix to split off. `0x1g`/`0b1x` (a valid digit *then* invalid trailing letters) still split-and-defer as `0x1`+`g` — only the genuinely digit-less case (`0x`, `0b`, or `0x`/`0b` followed straight by non-hex/non-binary letters like `0xzz`) is caught eagerly. |

## General

* Every token carries a **`TokenType`** — a C++ `enum class` (in
  `../shared/include/token_type.hpp`) with one distinct value per keyword and per
  operator/punctuation mark (e.g. `TokenType::IF`, `TokenType::ARROW_OP`,
  `TokenType::OPEN_PAREN_OP`), not a shared category string. This
  replaced an earlier design that used ~9 broad category strings
  (`type_keyword`, `control_keyword`, ...); the switch was made
  specifically to prepare for a parser phase, which generally wants one
  terminal symbol per keyword rather than a shared bucket.
* `to_string(TokenType)` (in `../shared/src/token_type.cpp`) converts a `TokenType`
  back to its printable name (e.g. `TokenType::ARROW_OP` → `"arrow_op"`)
  for the table printed at the end.
* Identifiers and keywords share **one** flex rule. The matched text is
  looked up via `reserved_word()` (a `keyword_map`, string → `TokenType`,
  in `../shared/src/token_type.cpp`); if found, that keyword's specific
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
   * Hexadecimal: `0x1F` / `0X1F` — validated: `0x`/`0X` with no hex
     digit at all after it (e.g. bare `0x`, or `0xzz`) is a lexical
     error (`Invalid hex literal`). `0x1g` (a valid hex digit *then*
     an invalid trailing letter) is unaffected by this — it still
     splits into `0x1` + `g` per the malformed-literal design decision
     below, since `0x1` is already a complete valid number.
   * Binary: `0b1101` / `0B1101` — validated: a `0b`/`0B` literal
     containing a digit `2`–`9` (e.g. `0b1102`) is a lexical error
     (`Invalid binary literal`), and so is `0b`/`0B` with no binary
     digit at all after it (bare `0b`, or `0bxy`), same reasoning as
     the hex case above.
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

* Keywords are stored in `keyword_map` (`../shared/src/token_type.cpp`) — a
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
  `../shared/src/token_type.cpp` (and its `TokenType` enum value in
  `../shared/include/token_type.hpp`, and its printable name in `token_to_string_map`) —
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
  `../shared/src/token_type.cpp`) at match time.
* Full set: `+ - * / % = == != < > <= >= && || ! & | ^ ~ << >> ++ -- +=
  -= *= /= %= &= |= ^= -> . , ? : ::`, plus `...` (`ELLIPSIS_OP`, for
  variable-argument functions) and `::` (`SCOPE_RESOLUTION_OP`, for
  `ClassName::member`).
* Adding a new operator: add its `TokenType` to `../shared/include/token_type.hpp`, an
  entry to `operator_map`/`token_to_string_map` in `../shared/src/token_type.cpp`,
  and — only if it's multi-character — one flex rule in `src/lexer.l`
  (single-character operators need no `lexer.l` change at all, since
  they already fall through to the table-lookup rule). This same
  table is shared with phase2-parser, so the change is picked up by
  both phases automatically — see `../README.md` and
  `../phase2-parser/README.md` for why the *tables* are shared but
  each phase keeps its own scanner.

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
  and a full report is written to a log file — see
  [Logging](#logging) below for the exact format.
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

## Logging

* Every run of `./lexer <file>` writes a log file to
  `logs/<file-stem>.log` (the `logs/` directory is created automatically
  if it doesn't exist) — **on every run, not just runs with errors.**
* On a **clean** run: the log just says `No lexical errors found.` —
  and nothing is printed to the console about this happening. It's
  silent; you'd only know it's there if you looked in `logs/`.
* On a run **with errors**: each error gets a numbered entry (line,
  offending lexeme, message), followed by a total count at the bottom.
  The console additionally prints `Lexical errors found.` and
  `Report written to <path>` so it's obvious there's something to check
  — unlike the clean-run case.
* Example log content for a broken file:
  ```
  =========================================
          LEXICAL ERROR REPORT
  =========================================

  Source File : test/test6_lexical_errors.c

  [1]
  Line    : 2
  Lexeme  : 'a;
  Message : Unterminated character literal

  [2]
  Line    : 3
  Lexeme  : "oops;
  Message : Unterminated string literal

  ...

  -----------------------------------------
  Total Errors : 12
  ```
* The log filename is derived from the **input file's stem**, not its
  content (e.g. `test6_lexical_errors.c` → `test6_lexical_errors.log`)
  — running the lexer twice on the same source file overwrites the
  previous log for that file.
* Implemented in `src/logger.h`/`src/logger.cpp` (`writeLexerLog()`),
  called unconditionally near the top of `main()` in `src/lexer.l`,
  before the clean/error branch is even decided.
* `logs/` is `.gitignore`'d — it's regenerated build output, not
  tracked in the repo.

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

## Resources

- **[Lex & Yacc Tutorial](https://www.epaperpress.com/lexandyacc/download/LexAndYacc.pdf)**
  by Tom Niemann (epaperpress.com) — the classic short introduction to
  building a compiler with lex/yacc (flex/bison are their modern GNU
  clones, what this project actually uses). Directly useful for this
  phase: the *Lex* section (theory of regular expressions → finite
  state automata, the `%{ }%%%%` file structure, `yytext`/`yyleng`,
  start conditions for string scanning) covers exactly the mechanics
  `src/lexer.l` is built on. The *Yacc* section, the worked calculator
  example (interpreter + stack-machine compiler + syntax-tree dump),
  and *More Yacc* (recursion, if-else ambiguity, `%prec`, error
  recovery) are the natural next read once `phase2-parser/` starts —
  same author, same running example, builds directly on the lex half.

## Test cases (`test/`)

| File | Covers |
|---|---|
| `test1_arithmetic_logical.c` | all arithmetic, relational, logical, bitwise, assignment operators |
| `test2_control_flow.c` | if-else, for, while, do-while, switch-case, goto, break, continue, static, until |
| `test3_arrays_pointers_structs.c` | int/char arrays, multi-dim arrays, pointers, multi-level pointers, structs, enums, unions |
| `test4_functions_advanced.c` | function calls with arguments, varargs (`...`), dynamic memory allocation, argc/argv, typedef, reference |
| `test5_until_loop.c` | until loop, float/hex/char/string constants |
| `test6_lexical_errors.c` | intentionally broken input to exercise every error type above (12 errors: unterminated char, unterminated string, illegal char, multi-char literal, invalid escape, bad hex escape, bad octal escape, invalid octal literal, invalid binary literal, bare `0x`, bare `0b`, unterminated comment) |
| `test7_type_modifiers_and_custom_keywords.c` | `short`/`long`/`long long`/`signed`/`unsigned` type modifiers, hex/octal/binary literals, integer suffixes (`U`/`L`/`LL` combinations), leading/trailing-dot floats (`.5`/`5.`), boolean literals (`true`/`false`), and this language's custom I/O and memory-allocation reserved words (`printf`, `scanf`, `malloc`, `free`, `calloc`, `realloc`) |
| `test8_file_manipulation.c` | this language's custom file-manipulation reserved words (`FILE`, `fopen`, `fclose`, `fread`, `fwrite`, `fprintf`, `fscanf`, `fgets`, `fputs`, `feof`) |
| `test9_classes_and_objects.c` | object-oriented keywords/operators: `class`, access modifiers (`public`/`private`/`protected`), `this`, scope resolution (`::`), and a lambda capturing `this` |
| `test10_lambda_functions.c` | C++-style lambda expressions: empty/`&`/`=`/mixed capture lists, trailing return type (`-> int`), `auto` |

## Resources

- **[Lex & Yacc Tutorial](https://epaperpress.com/lexandyacc/) by Tom
  Niemann** ([direct PDF](https://epaperpress.com/lexandyacc/download/LexAndYacc.pdf)) —
  a compact, practical introduction to building a lexer and parser
  together with lex/flex and yacc/bison. Covers exactly the pattern this
  project follows: a `%{ }%`/definitions/rules/subroutines-structured
  `.l` file, exclusive start conditions for strings (its "More Lex →
  Strings" section is close to how this lexer's `STRSTATE`/`CHRSTATE`
  work), and — relevant for whenever Phase 2 starts — how `yylex()`
  hands tokens to a bison-generated parser one at a time via `yylval`.
- **[The flex manual](https://westes.github.io/flex/manual/)** (official,
  [source on GitHub](https://github.com/westes/flex)) — the authoritative
  reference for flex's pattern syntax, start conditions, and the
  `%option` directives used in `src/lexer.l` (`noyywrap`, `yylineno`,
  `nounput`, `noinput`).
- **[The Bison manual](https://www.gnu.org/software/bison/manual/html_node/index.html)**
  (official) — for whenever `phase2-parser/` starts consuming this
  lexer's token stream.
- **Compilers: Principles, Techniques, and Tools** (Aho, Sethi, Ullman —
  "the Dragon Book") — the source of the classic
  lexer/parser/symbol-table interaction diagram (`getNextToken()`) this
  project has referenced when discussing what changes before Phase 2
  can drive this lexer directly.
