# Diagrams

Each diagram exists as a standalone page (`.html`, open in a browser)
and as an image (`.svg`, embedded in the READMEs). They were generated
with the diagram-design skill in its default style and describe the
implementation as audited on 2026-10-06.

| Diagram | Type | Shows | Used in |
|---|---|---|---|
| [compiler-architecture](compiler-architecture.svg) | architecture | the pipeline: implemented front-end phases, the shared library, and the two planned back-end phases | [`README.md`](../../README.md) |
| [repository-layout](repository-layout.svg) | tree | the project folders and what each contains | [`README.md`](../../README.md) |
| [lexer-dataflow](lexer-dataflow.svg) | architecture | source → preprocessor → `yylex()` → tokens or diagnostics | [`phase1-lexer/README.md`](../../phase1-lexer/README.md) |
| [parser-architecture](parser-architecture.svg) | sequence | how `yyparse()`, `yylex()`, the parse-time symbol table and the AST interact for each token | [`phase2-parser/README.md`](../../phase2-parser/README.md) |
| [semantic-architecture](semantic-architecture.svg) | architecture | the analyzer with the symbol table, type system, diagnostics and annotated AST | [`phase2b-semantic/README.md`](../../phase2b-semantic/README.md) |
| [symbol-table-architecture](symbol-table-architecture.svg) | nested | the scope tree built for `docs/examples/add.c` | [`SYMBOL_TABLE.md`](../SYMBOL_TABLE.md) |
| [symbol-lookup](symbol-lookup.svg) | flowchart | `SymbolTable::lookup()` | [`SYMBOL_TABLE.md`](../SYMBOL_TABLE.md) |
| [type-checking](type-checking.svg) | swimlane | which component does what when `x = y + z` is checked | [`phase2b-semantic/README.md`](../../phase2b-semantic/README.md) |
| [function-analysis](function-analysis.svg) | flowchart | `functionSignature()` → `functionBody()` | [`phase2b-semantic/README.md`](../../phase2b-semantic/README.md), [`SYMBOL_TABLE.md`](../SYMBOL_TABLE.md) |
| [feature-map](feature-map.svg) | heatmap | share of features complete per phase, from the matrix in `FEATURES.md` | [`FEATURES.md`](../FEATURES.md) |
