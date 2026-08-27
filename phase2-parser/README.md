# Phase 2 — Syntax Analyzer

A Bison/Flex syntax analyzer for the custom C-like language, built on top
of Phase 1's token/keyword design. It consumes source code directly
(scanning + parsing in one pass, feeding tokens to the parser on demand)
and produces either:

- a **Token / Token_Type** table, where every identifier's `Token_Type`
  is its *resolved role* (`INT`, `INT_POINTER`, `PROCEDURE`, `STRUCT`,
  `TYPEDEF`, `LABEL`, `ENUM_CONSTANT`, ...) rather than a blanket
  `identifier`, or
- a list of **every syntax error found**, if the program doesn't parse.

```bash
cd phase2-parser
make                 # builds ./syntax_analyzer
./run.sh             # runs ./syntax_analyzer over every file in test/
./syntax_analyzer test/test1_variables_vs_procedures.c
```

## Why "smarter" than a plain token dump

The original brief asked for a Lexeme/Token table. That's fine for
*keywords and operators*, but it's not useful for identifiers: printing
`a -> identifier` for every name in the program throws away exactly the
information a syntax analyzer is supposed to recover. Given

```c
int a(int b, int c) { return b + c; }   // a is a function
int main() {
    int a;                              // a *different* a — a variable
    a = 5;
}
```

the two `a`s are the same *lexeme* but play completely different
grammatical roles, and the table should say so. That's what this phase
does: `a` in the first line prints as `PROCEDURE`, `a` inside `main`
prints as `INT`.

## Approach

**1. One-pass scan-and-parse.** Flex (`src/scanner.l`) doesn't
pre-tokenize the file into a vector the way Phase 1 does; Bison
(`src/parser.y`) calls `yylex()` on demand, driving an LALR(1)
shift-reduce parse of the whole translation unit.

**2. A token log, patched after the fact.** Every token the scanner
matches is appended, in order, to a global vector of `{lexeme,
category}` (`g_tokens` in `include/common.h`). Identifiers start with a
generic placeholder category. Each token carries the *index* of its
own slot in that vector inside the parser's semantic value
(`ParserValue::idx`). As the grammar reduces a declaration, a function
header, a struct tag, a label, etc., the corresponding semantic action
looks up (or inserts) the identifier in the **symbol table** and calls
`setCategory(idx, resolvedType)` to overwrite that specific slot. At
the end, if there were no errors, the log is printed as the final
table — in original token order, but with every identifier now
carrying its resolved role instead of the word "identifier".

**3. A scoped symbol table.** `include/common.h` / `src/common.cpp`
keep a stack of scopes (`vector<unordered_map<string, Symbol>>`). A
new scope is pushed on every `{`, on entry to a function body (before
its parameters are inserted, so they're visible for the whole body),
and on a `for (int i = ...; ...)` init-declaration; it's popped on the
matching `}`. Symbols carry a `SymKind` (`VARIABLE`, `PROCEDURE`,
`PARAMETER`, `STRUCT_TAG`, `CLASS_TAG`, `ENUM_TAG`, `UNION_TAG`,
`TYPEDEF_NAME`, `ENUM_CONST`, `LABEL`) and the pre-computed string to
print for it. Lookup walks the scope stack from innermost to outermost,
so shadowing works the same way it does in C.

**4. Declarator → type-string resolution.** `declaration_specifiers`
accumulates the base type (`INT`, `UNSIGNED_LONG`, `STRUCT`, ...) into
a small `TypeSpec` struct; `declarator` accumulates pointer depth
(`*`/`&`) and array depth (`[...]`) into a `DeclInfo` struct.
`registerDeclarator()` combines the two into the final classification
string, e.g. `int **p` → `INT_POINTER`, `char name[20]` →
`CHAR_ARRAY`. If the declarator turns out to have a parameter list
(`name(...)`), it's registered as `PROCEDURE` instead, and if the
declaration was prefixed with `typedef`, the name is registered as
`TYPEDEF` and remembered so the *scanner* can recognize later uses of
it as a type name (see next point).

**5. The typedef "lexer hack".** `MyInt x;` is genuinely ambiguous to
an LALR(1) C-style grammar unless the scanner and parser cooperate:
when the parser finishes a `typedef` declaration it adds the new name
to a global `unordered_set<string> g_typedefNames`; the scanner checks
every identifier it matches against that set and returns a distinct
`TYPE_NAME` token (instead of `IDENTIFIER`) for known typedef names.
That one-token difference is what lets the grammar treat `MyInt` as a
type-specifier without any backtracking or ambiguity — this is the
same technique real C compilers built with yacc/bison use.

**6. Custom keywords are parsed as builtin calls, not identifier
calls.** Per Phase 1's design, `printf`, `scanf`, `malloc`, `free`,
`calloc`, `realloc`, and the whole `fopen`/`fclose`/`fread`/`fwrite`/
`fprintf`/`fscanf`/`fgets`/`fputs`/`feof` family are *reserved
keywords* in this language (real C treats them as ordinary library
identifiers). The grammar has a dedicated `builtin_call` production
for each of them so they parse as calls without needing a symbol-table
entry.

**7. Multiple syntax errors, not just the first.** `%define
parse.error verbose` gives descriptive messages ("unexpected X,
expecting Y"). Panic-mode recovery rules (`statement: error ';'` and
`external_decl: error ';' | error '}'`, each followed by `yyerrok;`)
let the parser discard tokens up to the next statement/declaration
boundary and keep going instead of aborting on the first mistake, so a
file with several unrelated mistakes gets several diagnostics in one
run (see `test5_syntax_errors.c`). Every diagnostic (line, the text
near the error, and the message) is collected in `g_diagnostics` and
also written to `logs/<file>.log`. On success, the log file contains
the same three sections stdout does -- Token/Token_Type table,
Abstract Syntax Tree, Symbol Table -- via shared print functions in
`main.cpp` so the two outputs can't drift apart from each other.

## AST and symbol table (no semantic checks)

On top of the classified token table, this phase now also builds a
real **abstract syntax tree** and a **symbol table with name
mangling** -- while deliberately staying out of semantic-analysis
territory (no type checking, no redefinition errors, no "undeclared
identifier" errors). Per the standard compiler-phase breakdown, syntax
analysis's job is tokens in, (parse tree / AST + syntax errors) out --
semantic checking and an *annotated* AST are the next phase's job, not
this one's.

```
$ ./syntax_analyzer test/test1_variables_vs_procedures.c
...
=== Abstract Syntax Tree ===
Program "translation_unit"
|-- FunctionDef "a : _Z1aii"
|   |-- ParamDecl "b : INT"
|   |-- ParamDecl "c : INT"
|   `-- CompoundStmt
|       `-- ReturnStmt
|           `-- BinaryExpr "+"
|               |-- Identifier "b"
|               `-- Identifier "c"
...

=== Symbol Table ===
Name                 Kind           Line   Scope                        Type             Qualifiers               Uses      Signature              Mangled Name
----                 ----           ----   -----                        ----             ----------               ----      ---------              ------------
a                    procedure      9      global                       PROCEDURE                                 0         INT (INT, INT)         _Z1aii
b                    parameter      9      global > a()                 INT                                       1
c                    parameter      9      global > a()                 INT                                       1
main                 procedure      13     global                       PROCEDURE                                 0         INT ()                 _Z4mainv
a                    variable       14     global > main()              INT                                       2
result               variable       16     global > main()              INT                                       0
```

**AST.** One generic node shape (`ASTKind kind; std::string label;
vector<ASTNodePtr> children;` in `include/ast.h`) is enough to
represent the whole tree without a class hierarchy per construct --
this is a syntax tree for display/verification, not a typed IR a
later phase compiles against. Every grammar rule that has structural
meaning (declarations, statements, expressions) builds and returns
its own node via a new `node` field on `ParserValue`; container rules
(`block_item_list`, `argument_list`, `member_decl_list`, ...)
accumulate into a `nodeList` field the same way `paramList` already
worked for declarators. `printAST()` renders it with ASCII branch
connectors (`|--`, `` `-- ``), one node per line.

Two things worth flagging about how it's built:
- **Redundant parens are dropped.** `'(' expr ')'` just returns the
  inner expression's node rather than wrapping it, so `(a + b)` and
  `a + b` produce the identical subtree -- parenthesization is a
  parsing aid, not something worth a tree node.
- **Omitted optional parts are simply absent, not shown as an
  explicit "none".** An `if` with no `else`, or a `for`-loop with no
  increment expression, prints with fewer children rather than an
  empty placeholder node. `mkNode()`'s children list silently skips
  any `nullptr` passed to it, which is what makes this automatic
  without every call site having to check first.

**Symbol table.** `pushScope()`/`popScope()` (used during parsing for
correct, shadow-respecting name lookup) discard each scope once it's
popped, so there'd be nothing left to print at the end. A second,
append-only `g_symbolTable` (`include/common.h`) records every
`declareSymbol()` call permanently, independent of scope lifetime,
purely for this final report -- it plays no role in parsing itself.
Class members are recorded with a qualified `ClassName::member` name
using a single-slot "current class" tracked via `enterClass()`/
`leaveClass()`, entered right after a class/struct/union tag is
declared and left once its closing `}` is reached.

Concretely, that's **two different structs** carrying different
subsets of the same information, on purpose:
```cpp
struct Symbol {                          // lives inside g_scopes, for lookup
    SymKind kind;
    std::string typeStr;
    std::string mangledName;
    int flatIndex = -1;                  // this symbol's slot in g_symbolTable
};

struct SymbolTableEntry {                // lives in g_symbolTable, for reporting
    std::string name, qualifiedName, typeStr, mangledName, scopePath, ...;
    int declLine; bool isStatic, isConst, isVolatile; int useCount; ...
};
```
`Symbol` stays deliberately lean -- it's only ever consulted mid-parse
to classify a token or resolve a type, so it carries just enough to do
that. `SymbolTableEntry` carries everything else (declaration line,
qualifiers, usage count, ...), since it only exists for the final
report and there's no cost to it being bigger. `flatIndex` is the
bridge between them: an **index**, not a pointer, specifically because
`g_symbolTable` is a `std::vector` that can reallocate as it grows --
storing a raw pointer into it anywhere would be a live dangling-pointer
bug waiting for the vector to resize. An index stays valid across any
number of reallocations, so `recordUsage()` can cheaply bump a usage
count in the flat table (`g_symbolTable[s->flatIndex].useCount++`)
from a `Symbol*` obtained during parsing, without either struct
needing to know more about the other than it has to.

Beyond name/kind/type, each entry also carries what a real compiler's
symbol table typically accumulates before code generation, all still
purely structural (nothing here validates or flags anything):

- **Declaration line.** `TokenRecord` now stamps every token with the
  line it was scanned on; a declarator's `nameIdx` is looked back up
  through `g_tokens` for an accurate line even when the declaring
  action doesn't fire until several tokens later (e.g. after a long
  initializer expression has already advanced the scanner).
- **Scope, as a readable owner path rather than a bare number.**
  Every `pushScope()` call now takes a label describing what the scope
  actually *is* -- `"main()"`, `"class Dog"`, `"Dog::Dog()"`,
  `"switch"`, `"for"` -- and `currentScopePath()` joins every
  currently-open scope's label in nesting order
  (`"global > main() > for"`), captured once per symbol at declaration
  time into `SymbolTableEntry::scopePath`. Function bodies,
  constructors/destructors, struct/union/class bodies, lambdas, and a
  `for`-loop's own init-scope all get a specific label taken straight
  from context already available at that point in the grammar (the
  declarator's name, the enclosing class, etc.) -- no renumbering
  needed, since the label is just one more line inside an action block
  that already existed.

  `if`/`while`/`do`/`until` bodies are the one place this stops short
  and falls back to a generic `"block"` label instead of `"if"`/
  `"while"`/etc, and that's a deliberate, tested decision, not an
  oversight: those all route their body through the same generic
  `statement` nonterminal that also handles the dangling-else case,
  and inserting a mid-rule action there to hint the label turned out
  to badly break the `%prec IFX`/`ELSE` precedence mechanism the
  dangling-else fix depends on -- conflict count jumped from the usual
  7 to 78, and the rule became unreachable. Reverted immediately, and
  left alone rather than risk reintroducing exactly the class of
  silent grammar bug the pointer-recursion issue earlier in this
  project already was. `switch`, structurally unrelated to that
  precedence machinery, got the same treatment and *is* safe (tested:
  conflict count stayed at 7), so its body correctly shows `"switch"`.
- **Storage class and qualifiers** (`static`, `const`, `volatile`) --
  previously parsed and silently discarded; `TypeSpec` now actually
  carries `isConst`/`isVolatile` alongside the `isStatic` it already
  had, and they ride along into the symbol table entry.
- **Pointer/array depth as plain numbers**, not just baked into the
  `INT_POINTER`/`INT_ARRAY`-style type string.
- **A real return type and readable parameter list for functions**,
  shown as `Signature` (e.g. `INT (INT, INT)`) -- separate from the
  generic `PROCEDURE`/`CONSTRUCTOR`/`DESTRUCTOR` kind label and
  distinct from (but consistent with) the encoded mangled name.
- **A usage count.** `recordUsage()` bumps a counter on every *use* of
  a name (an identifier in an expression, a `goto`'s target label) as
  distinct from every *declaration* of one. It has two overloads --
  `recordUsage(const Symbol *s)`, used when the caller has already
  called `lookupSymbol()` itself moments earlier (true at both call
  sites), and a `recordUsage(const std::string &name)` convenience
  wrapper that just calls `lookupSymbol()` and forwards. The
  `Symbol*` overload exists specifically because the original
  string-only version was silently walking the scope chain and
  re-hashing the same name a second time on every single identifier
  occurrence in a program, right after the caller had *already* done
  that exact walk to classify the token -- a real, measurable
  inefficiency (see "A real inefficiency, found and fixed" below), not
  just a style choice. This is the one piece of bookkeeping actually
  worth calling out for what it enables: it's the raw ingredient an
  "unused variable" warning would need, but computing that warning is
  a judgment call about control flow and intent that belongs to
  semantic analysis -- here it's just an honest count of textual
  references, not a claim about whether any of them are reachable or
  meaningful.

**Name mangling.** `mangle()` in `common.cpp` produces an
Itanium-ABI-*inspired* (not spec-compliant) mangled name for every
function, constructor, and destructor: `_Z<len><name><param-codes|v>`,
nested with `N<len><Class>...E` for class members, e.g.
`add(int,int)` &rarr; `_Z3addii`, `Dog::bark()` &rarr; `_ZN3Dog4barkEv`.
It's driven entirely off the same classification strings already
computed for the Token_Type column (`INT`, `INT_POINTER`, `CLASS`,
...) mapped to single-letter codes -- good enough to demonstrate
overload-distinguishing mangling without requiring a real type system
underneath it, which is out of scope for a syntax-only pass.
Out-of-class method definitions (`ClassName::method(...) {...}`) mangle
identically to their in-class prototype: `direct_declarator`'s
`IDENTIFIER SCOPE_RES IDENTIFIER` / `TYPE_NAME SCOPE_RES IDENTIFIER`
forms (the latter needed because by the time `Dog::bark(...)` is
written, `Dog` has almost always already become a `TYPE_NAME`, not a
plain `IDENTIFIER`) now carry the class name through in
`DeclInfo::className`, and `function_definition` temporarily enters
that class context (`enterClass()`/`leaveClass()`) just long enough to
compute the mangled name and register the symbol -- see
`test8_out_of_class_methods.c`.

**A bug worth documenting because it's easy to reintroduce:** Bison's
plain-struct (non-variant) C skeleton reuses a single semantic-value
slot (`yyval`) across every reduction without resetting it first. Any
grammar action that doesn't explicitly touch a field it isn't using
(most commonly a blank `{ }` no-op action on an epsilon/empty
alternative) can silently inherit **stale data left over from a
previous, unrelated reduction** -- this showed up as a phantom `"{"`
leaking into a class's inheritance label the first time this AST work
was tested, traced back to `inheritance_opt: /* empty */ { }` not
resetting anything. The fix applied throughout: every action that
intentionally produces "nothing" writes `$$ = ParserValue();`
explicitly rather than leaving the action block empty.

## Grammar coverage

All of the "basic" feature list is implemented: arithmetic/logical/
bitwise/relational/shift operators with full C precedence, if-else,
for (including a C99-style declaration in the init-clause), while,
do-while, switch/case/default, int/char arrays (incl. multi-dimensional,
via repeated `[...]`), pointers (incl. multi-level), structs, printf/
scanf as builtin calls, function calls with arguments, goto/break/
continue, and static.

Most of the "advanced" list is also implemented: variable-argument
calls (`...`), malloc/free/calloc/realloc as builtins, typedef (with
the lexer-hack support above), reference declarators (`&`), the
`until` loop, multi-level pointers, and multi-dimensional arrays.
Command-line input needs no special grammar (`main(int argc, char
**argv)` is just an ordinary function declarator).

Beyond the original spec, this also parses (mirroring the "Features
added beyond the original spec" section of the top-level README):
`enum`/`union`/`class` with access modifiers and inline methods,
`this`, `::` scope resolution in expressions, boolean literals, the
`FILE` type and its function family, and C++-style lambdas
(`[capture](params) { body }`).

On top of that, a further C++-flavored layer was added: `bool`,
`const`/`volatile` qualifiers, `sizeof x` / `sizeof(type)` as real
operators (not just piggy-backed on a generic call), `new`/`delete`,
single-base class inheritance (`class Derived : public Base { ... }`),
and constructors/destructors as class members (`Shape(int x) {...}`,
`~Shape() {...}`). Getting there required two follow-on fixes worth
calling out because they're the kind of thing that only shows up once
you actually try a real program through the grammar:

- **Class/struct/union/enum tag names are now usable directly as a
  type**, the way C++ (unlike C) allows -- `Dog d;` works without
  repeating `class Dog d;`. This piggy-backs on the same typedef
  lexer-hack described above: once a tag's closing `}` is reached, its
  name is added to the same "treat as `TYPE_NAME`" set typedef names
  use, and `categoryForTypeName()` decides whether to print `TYPEDEF`
  or the tag's own category (`CLASS`/`STRUCT`/`UNION`/`ENUM`) for that
  usage.
- **The tag name is deliberately *not* registered as a type until
  after its own closing `}`**, specifically so a constructor/
  destructor inside the class's own body (`Dog(int n) {...}` inside
  `class Dog {...}`) still sees `Dog` as a plain `IDENTIFIER` at that
  point rather than colliding with the parenthesized-declarator/
  function-declaration grammar. Without that delay, `Dog(int n)` inside
  its own body is genuinely ambiguous with "a variable of type `Dog`
  declared via a parenthesized declarator."
- A `type_name` used for casts/`sizeof`/`new` is intentionally
  **restricted to referencing an existing tag**, never declaring a new
  one with a body -- otherwise `(SomeType) x` could theoretically try
  to swallow an entire `{ ... }` class body and collide with statement
  parsing.

**Deliberately not implemented:** constructor-call direct-initialization
(`Dog d(4);`) and functional-style construction as an expression
(`x = Dog(4);`). Real C++ resolves the declaration-vs-expression
ambiguity here via the notorious "most vexing parse" rule (prefer the
declaration interpretation), which needs real disambiguation work well
beyond a syntax-only pass; `Dog d;` followed by ordinary field/method
access is supported instead. Operator overloading declarators (`T
operator+(...)`) and designated initializers (`.field = val`) were
also left out as further optional additions, not because they're hard
to add but to keep this pass focused on syntax rather than growing
into a full semantic analyzer.

## A real inefficiency, found and fixed

`recordUsage(const std::string &name)` used to call `lookupSymbol(name)`
internally -- but its only two call sites (`primary_expr`'s
`IDENTIFIER` handling, and `GOTO`'s label resolution) had *already*
called `lookupSymbol()` themselves a line earlier, to classify the
token. That meant every single identifier occurrence in a program was
walking the scope chain and re-hashing the same name **twice**, back
to back, for no reason. Fixed by adding a `recordUsage(const Symbol
*s)` overload that reuses the already-found result, and updating both
call sites to pass it instead of re-deriving it from the name string.
Verified behavior-preserving (identical usage counts before/after) and
re-ran the full test suite before and after to confirm no regression.

`lookupSymbol()`'s own `O(scope depth)` walk-the-stack-of-maps design
was considered and deliberately left alone -- real high-throughput
compilers use a single global map with a per-name binding stack
instead (`O(1)` lookup regardless of nesting depth), but that's a
genuine architecture change for a performance gain that wouldn't be
measurable at this project's realistic file sizes and nesting depths;
not worth the risk without a profiler actually showing it matters.

## Programmer-friendly diagnostics and a resilient AST

Three additions on top of the base error-reporting mechanism, aimed
specifically at making failures easier to actually read and act on.

**GCC/Clang-style diagnostics**, with an exact source snippet and
caret instead of just a line number:
```
test.c:3:5: syntax error: syntax error, unexpected RETURN, expecting ';'
 3 |     return 0;
   |     ^
```
Column tracking is added via Flex's `YY_USER_ACTION` hook, which fires
automatically before every matched token, so it didn't need touching
every single rule in `scanner.l` by hand. `main.cpp` reads the whole
source file into `g_sourceLines` up front purely to print this
snippet. Color (bold location, red "syntax error"/"lexical error",
bold message) is applied only when `isatty(fileno(stderr))` is true —
piped output and the on-disk log file both stay plain text, so nothing
saved to a file ends up full of escape-code noise.

**Clang-style fix-it hints.** When Bison's verbose error message names
*exactly one* unambiguous literal token it was expecting (e.g.
`"expecting ';'"`), an extra line suggests the fix, in green:
```
test.c:3:5: syntax error: syntax error, unexpected RETURN, expecting ';'
 3 |     return 0;
   |     ^
   | note: insert ';' here
```
`singleExpectedLiteral()` deliberately does **not** guess when Bison's
message lists more than one option (`"expecting ',' or ')'"`) or names
an abstract, non-literal token (`"expecting IDENTIFIER"`, which has no
single canonical piece of text to suggest) — a wrong suggestion is
worse than no suggestion, so those cases just get the plain caret with
no fix-it line, rather than the tool bluffing.

**A resilient AST — `ErrorNode`.** Previously, a statement or
declaration that failed to parse just left a silent hole in the tree:
panic-mode recovery (`error ';'`/`error '}'`) discarded it and moved
on, with no visible trace once parsing continued. Now the recovery
actions insert an explicit `ErrorNode` exactly where the broken
construct would have been, labeled with what actually went wrong
(`ErrorNode "line 3: near 'return'"`) via a small `lastErrorLabel()`
helper that reads back the diagnostic `yyerror()` just recorded. This
borrows the "always produce a complete tree" philosophy real IDE-grade
tooling (Roslyn's red-green trees, rust-analyzer's `rowan`) uses,
without needing a different parsing algorithm or a rewrite — it's a
small, contained change on top of the same Bison/LALR grammar.

Since the AST used to only ever get printed on a *successful* parse,
adding `ErrorNode` alone wouldn't have been visible to anyone —
`main.cpp` and the log file now also print a `--- Partial AST
(best-effort) ---` section on the failure path, so a file with several
scattered mistakes shows exactly which constructs broke and where they
sit relative to the parts that parsed fine:
```
Program "translation_unit"
|-- FunctionDef "main : _Z4mainv"
|   `-- CompoundStmt
|       |-- ErrorNode "line 9: near 'a'"
|       `-- ErrorNode "line 11: near '{'"
|-- ErrorNode "line 15: near ';'"
...
```

## Known limitations (by design, for a course-scope parser)

- **Single pass, so forward references print as `IDENTIFIER`.** A
  `goto` to a label declared later in the same function, or a call to
  a function defined further down the file, is syntactically fine and
  parses correctly, but its Token_Type falls back to the generic
  `IDENTIFIER`/label default because the symbol doesn't exist in the
  table *yet* when that token is scanned. A full two-pass or
  forward-declaration-aware design would resolve this; out of scope
  here since the deliverable is the *syntax* phase, not semantic
  analysis.
- **Struct/class member names after `.`/`->` aren't resolved** (no
  per-type member namespace is tracked), so `p.x` shows `x` as
  `IDENTIFIER` even though `p`'s type is known. Again, a semantic
  concern more than a syntactic one.
- **Lambda captures aren't resolved** to their enclosing-scope type;
  they're accepted syntactically but not looked up.
- **Cascading errors after severe recovery.** Panic-mode recovery can
  occasionally produce one or two extra "ghost" diagnostics after a
  serious error (e.g. an unbalanced brace) before it resynchronizes.
  This is a well-known characteristic of single-token panic-mode error
  recovery in LALR parsers, not a bug in the specific grammar rules.

## Files

```
phase2-parser/
├── include/
│   ├── common.h       symbol table, token log, diagnostics, parser value type, mangling
│   └── ast.h          AST node kind/shape, node constructors, tree printer
├── src/
│   ├── common.cpp      their implementations
│   ├── ast.cpp          AST implementation
│   ├── scanner.l          flex scanner (token classification + typedef hack)
│   ├── parser.y           bison grammar (declarations, statements, expressions, AST)
│   └── main.cpp           driver: parses a file, prints the table/AST/symbols or the errors
├── test/                  8 test cases (7 valid, 1 deliberately broken)
├── makefile
└── run.sh
```
