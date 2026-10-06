# Design Log

A running record of the decisions taken while building the back end:
what was decided, who decided it, why, and what was done as a result.
Newest entries are at the bottom. Open questions are listed at the end.

Reference material for this work:

- Course lectures 25–27 (Compiler Design CSC-305): symbol tables with
  offsets, three-address code for expressions (`E.place`, `E.code`,
  `newtmp()`, `gen`), flow of control, array addressing, type conversion,
  boolean expressions (numerical and short-circuit), backpatching.
- Aho, Lam, Sethi, Ullman — *Compilers: Principles, Techniques, and Tools*
  (the "Dragon Book"), chapter 6.
- N. Papaspyrou — *A Formal Semantics for the C Programming Language*
  (evaluation order, sequence points, conversions).

---

## 2026-10-07 — Session 1: scope reduction before TAC

### D1. Four advanced features are dropped

**Decided by:** the user.
**Decision:** remove these features from the language before the back
end is built:

1. `enum` and `union`
2. file manipulation (`FILE`, `fopen`, `fclose`, `fread`, `fwrite`,
   `fprintf`, `fscanf`, `fgets`, `fputs`, `feof`)
3. lambda functions
4. function pointers

**Why:** each of them needs its own machinery in TAC and MIPS (closure
conversion for lambdas, indirect calls for function pointers, a
run-time file layer, overlapping storage for unions); dropping them
keeps the back end focused on the features the project is graded on.

### D2. Dropped features are removed completely

**Decided by:** the user (option "Remove completely").
**Decision:** the keywords stop being reserved (`enum`, `union`, `FILE`,
`fopen` …, `mutable` become ordinary identifiers), the grammar rules,
AST node kinds, type kinds and semantic checks are deleted. A program
that uses a dropped construct gets an ordinary syntax error.
**Alternative rejected:** keeping the words reserved with a dedicated
"not supported" message (friendlier, but leaves stubs in every phase).

### D3. Affected tests are edited, not deleted

**Decided by:** the user.
**Decision:** about 40 of the 92 test programs use a dropped feature
beside features that stay. Only the dropped parts are cut out; a test
is deleted only when nothing else is left in it. One new invalid test
shows that each dropped construct is now rejected.

### D4. `auto` stays

**Decided by:** the user.
**Decision:** `auto x = 3;` (type deduction from the initializer) is
kept. It costs nothing later: semantic analysis replaces `auto` by the
real type before TAC sees the declaration.

### D5. Branch

**Decided by:** the user.
**Decision:** work happens on a new branch `tac`, created from `main`
after pull request #1 (the semantic phase) was merged. Feature removal
and TAC generation are separate commits. Nothing is pushed until asked.

### D6. How function pointers are rejected

**Decided by:** Claude (implementation detail of D1/D2 — say so if you
want it done differently).
**Decision:** a function is never a value; its name can only be called.

| Construct | Rejected by | Message |
|---|---|---|
| `int (*fp)(int);`, `int (*table[2])(int);`, `typedef int (*Op)(int);`, a parameter `int (*op)(int)` | parser (`direct_declarator` action) | `syntax error, unexpected '(' after a parenthesized pointer declarator` |
| a cast `(int (*)(int)) x`, `sizeof(int (*)(int))` | parser (the abstract-declarator rule is gone) | `syntax error, unexpected '('` |
| `x = f;`, `&f`, `*f`, `g(f)`, `if (f)`, `sizeof(f)` | semantic (`identifier()`) | `reference to function 'f' must be called (a function is not a value: function pointers are not supported)` |
| a parameter of function type, `int apply(int op(int))` | semantic (`resolveParams()`) | `parameter 'op' cannot have a function type` |
| `typedef int Fn(int); Fn *p;` | semantic (`resolveType()`) | `'p' declared as a pointer to a function` |

**Why this shape:** in C a function name "decays" to a pointer whenever
it is used as a value. Without function pointers there is nothing for it
to decay to, so the one place a bare function name can still appear —
the callee of a call — is resolved by `call()` directly, and every
other appearance reaches `identifier()` and is an error. `int (*pa)[3]`
(pointer to an array) is unaffected.
**Consequence for the back end:** every call in TAC has a callee known
at compile time (`call _Z3addii, 2`); there is no indirect call.

### D7. Consequences of "remove completely" found while implementing

Recorded so nothing here is a surprise later:

1. **File I/O leaves no syntax behind.** `FILE *f = fopen("a", "r");`
   is now the *expression* `FILE * f = fopen(...)` over plain
   identifiers, so it is not a syntax error; semantic analysis reports
   `undeclared identifier 'FILE'`, `'f'` and `call to undeclared
   function 'fopen'`. (The other three features do give syntax errors.)
2. **Anonymous unions went with `union`** — both the member form and
   the block-scope form (`union { int a; char b; };` in a function, with
   its hidden `__anon_union.N` object). **Unnamed structs and anonymous
   struct members stay** (`struct S { struct { int lo, hi; }; };`,
   `typedef struct { int x; } Pt;`).
3. **The former keywords are ordinary identifiers**: `int enum = 1;`,
   `struct FILE { int fd; };`, `int fopen(int mode)` are legal
   (`phase2b-semantic/test/valid/v23_former_keywords.c`).
4. **One scanner hack disappeared.** `[` used to need lookahead to tell
   a designator (`{[2] = 7}`) from a lambda (`[x](int a) {...}`). With
   no lambdas, `[` is an ordinary token and the `DESIG_LBRACKET` token
   and `bracketIsDesignator()` are gone.
5. **Tag checks simplified.** With only `struct` and `class` left there
   is no "declared as union, used as struct" mismatch and no "previously
   an enum" case.

### Progress — feature removal finished (2026-10-07)

What was changed, front to back:

| Component | Change |
|---|---|
| `shared/token` | 13 token kinds removed (116 → 103): `ENUM`, `UNION`, `FILE`, the nine file functions, `MUTABLE` |
| `phase2-parser` (`parser.y`, `scanner.l`) | `enum`/`union` rules, enumerator lists, nine file built-ins, lambda rules (captures, `mutable`, `-> T`), the function-type abstract declarator; grammar 1492 → 1267 lines, still **0 conflicts** (`%expect 0`) |
| `shared/ast` | 4 node kinds removed (60 → 56): `EnumDecl`, `Enumerator`, `UnionDecl`, `LambdaExpr` |
| `shared/types` | `TypeKind::Enum`, `TypeKind::Closure`, `EnumInfo`, `RecordKind::Union`, the `FILE` opaque type, union layout, closure → function-pointer conversion |
| `shared/symbol_table` | `UNION_TAG`/`ENUM_TAG`/`ENUM_CONST`, `SymbolKind::EnumConstant`, `ScopeKind::Lambda`, lambda-crossing in `lookup()`, anonymous-union promotion, `FILE`/closure mangling |
| `phase2b-semantic` | `enumDefinition()`, `lambda()` and all capture checking, anonymous-union objects, nine file built-in signatures, calls through values; the rules of D6 added |

In total 22 source files, about 1100 lines removed and 200 added.

Tests (decision D3):

| Suite | Before | After | Notes |
|---|---|---|---|
| Lexer | 11 | 9 | deleted `test8_file_manipulation`, `test10_lambda_functions` (nothing else in them); edited 2 |
| Parser | 37 | 36 | deleted `funcPtr`, `test22_syntax_errors_file_io`; edited 7 (3 renamed); added `test29_dropped_features` |
| Semantic, valid | 24 | 24 | edited 11 (2 renamed); `v23_anonymous_unions` replaced by `v23_former_keywords` |
| Semantic, invalid | 20 | 20 | edited 8 (1 renamed); `e19_anonymous_unions` replaced by `e19_dropped_features` |

The two new "rejected" tests are `phase2-parser/test/test29_dropped_features.c`
(11 dropped constructs, each a syntax error, followed by a valid `main`
that proves the parser recovered) and
`phase2b-semantic/test/invalid/e19_dropped_features.c` (the semantic
rules of D6).

Verification: clean rebuild of `shared`, `phase1-lexer`,
`phase2-parser`, `phase2b-semantic` with no compiler warnings and no
grammar conflicts; `phase2b-semantic/run_tests.sh` → **passed: 80
failed: 0** (44 semantic programs + the 36 parser programs end to end).
All `logs/` were regenerated. Documentation updated: `README.md`,
`docs/FEATURES.md`, `docs/SYMBOL_TABLE.md`, the phase READMEs,
`GRAMMAR_DESIGN.md` §3c/§4, three diagrams (feature map, symbol lookup,
repository layout); the archived `DEVELOPMENT_NOTES.md` files got a
note instead of a rewrite.

Not committed yet (waiting for the user's word, D5).

---

## Open questions

*(none recorded yet — the TAC design questions start in session 2)*
