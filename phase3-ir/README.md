# Phase 3 — Intermediate Representation (Three Address Code)

> **Status: not started.** This folder contains only this README. There
> is no TAC data structure, no generator, no interpreter and no build
> file anywhere in the repository; the compiler stops after semantic
> analysis.

## What exists today that this phase will use

The semantic phase ([`../phase2b-semantic`](../phase2b-semantic/README.md))
already produces everything a TAC generator needs to read; none of it is
consumed yet:

| Available | Where |
|---|---|
| The annotated AST: each expression's type (`semType`), lvalue-ness, folded constant, resolved symbol | `ASTNode` fields, set by `sem::SemanticAnalyzer` |
| A persistent symbol table with a collision-free `uniqueName` per symbol (`x.4`, `_Z3addii`), storage class, and each function's `params` and `locals` | `sem::SymbolTable` — [`../docs/SYMBOL_TABLE.md`](../docs/SYMBOL_TABLE.md) |
| MIPS32 sizes, alignments and record field offsets | `sizeOf()`, `alignOf()`, `layoutRecord()` in `../shared/types` |
| Conversion rules to insert explicit conversions | `usualArithmetic()`, `integerPromotion()`, `implicitConversion()`, `decay()` |
| Constant arithmetic with the target's widths | `wrapToType()`, `fitsInType()` |

See ["What the IR phase gets"](../phase2b-semantic/README.md#what-the-ir-phase-gets).

## Planned work (not implemented)

The agreed order for the back end:

1. **TAC generation** — lower the annotated AST into quadruples
   (`t1 = a + b`, `if t1 goto L`, `param x`, `call f, n`, indexed and
   pointer loads/stores); explicit conversions; short-circuit `&&`/`||`;
   `switch`; calls, constructors and destructors at scope exit.
2. **A TAC interpreter**, used as the correctness check for generated
   and optimized code.
3. **Local optimizations** on basic blocks: constant folding, algebraic
   simplification, copy propagation, common-subexpression elimination,
   dead-code removal.
4. Later: global data-flow and loop optimizations.

Open design questions: closure conversion for lambdas, how `this` is
passed to methods, `long long` on a 32-bit target.
