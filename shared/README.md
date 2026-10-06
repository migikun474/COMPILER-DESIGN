# shared — the compiler's common library

Everything more than one phase needs lives here, one folder per
section of the compiler, built once into `build/libshared.a` by
`make` (each phase's makefile does this automatically). Each phase
keeps only its own logic and links the library. Phases 3 (TAC) and 4
(MIPS) do not exist yet; they are meant to link it too.

```
shared/
├── token/          token_type.hpp/.cpp   keyword / operator vocabulary (TokenType, keyword_map, operator_map, to_string)
│                   token_log.hpp/.cpp    the token log (TokenRecord, g_tokens, setCategory) + Token / Token_Type table printer
├── diagnostics/    diagnostics.hpp/.cpp  one diagnostics list for every phase, source lines, current scanner
│                                         position, GCC/Clang-style printer (file:line:col, source line, caret),
│                                         and the line map back to the file/line the user wrote
├── preprocessor/   preprocessor.hpp/.cpp #define (object- and function-like, #, ##, __VA_ARGS__), #undef,
│                                         #if/#ifdef/#ifndef/#elif/#else/#endif, #include, #error, #pragma once;
│                                         runs before lexing, one output line per input line
├── ast/            ast.hpp/.cpp          AST nodes, ASTTypeExpr, semantic annotation slots, tree printer, g_astRoot
├── types/          types.hpp/.cpp        structural type system: constructors, equivalence, conversions, casts,
│                                         MIPS32 sizes/layout, member lookup through base classes
├── symbol_table/   symbol_table.hpp/.cpp every symbol table: the parse-time scoped table + type-name table
│                                         (lexer hack) + pending references + overload lookup + mangling,
│                                         the semantic SymbolTable, and the printers for both
└── Makefile        -> build/libshared.a
```

## Using it from a phase

```make
SHARED    = ../shared
CFLAGS   += -I$(SHARED)
LIBSHARED = $(SHARED)/build/libshared.a

$(LIBSHARED):
	$(MAKE) -C $(SHARED)          # every phase's makefile rebuilds it when needed

$(TARGET): ... $(LIBSHARED)
	$(CC) $(CFLAGS) -o $@ <phase sources> $(LIBSHARED)
```

Headers are always included by module, so it is obvious where a name
comes from:

```cpp
#include "diagnostics/diagnostics.hpp"
#include "symbol_table/symbol_table.hpp"
```

## Who uses what

| Module | phase1-lexer | phase2-parser | phase2b-semantic |
|---|---|---|---|
| token | ✓ (vocabulary) | ✓ | ✓ (via the parser) |
| diagnostics | ✓ | ✓ | ✓ |
| preprocessor | ✓ | ✓ | ✓ |
| ast | | ✓ (builds it) | ✓ (annotates it) |
| types | | ✓ (mangling builds types from declarations) | ✓ |
| symbol_table | | ✓ (part 1) | ✓ (part 2, and part 1 via the parser) |

Dependencies inside the library: `token_log`, `ast` and `preprocessor`
use `diagnostics` (the current source position, the line map); `symbol_table` uses
`token`, `diagnostics`, `ast` and `types`; `types` and `symbol_table`
refer to each other (a record's members are symbols, a symbol has a
type), which is why they live in the same library.

## What stays in the phases

| Phase | Its own code |
|---|---|
| phase1-lexer | `lexer.l` (standalone flex scanner), its token list and log writer |
| phase2-parser | `scanner.l`, `parser.y`, `parser_value.h` (Bison's value type), `declarators` (declaration → AST + symbols), `scanner_support` (lookahead decisions), `token_converter` (TokenType → Bison codes) |
| phase2b-semantic | the analyzer: `declarations`, `statements`, `expressions`, `cxx` (constructors, operators, varargs), `sequencing` (sequence points), `report` (annotated AST) |

## Main entry points

| Module | Functions and types |
|---|---|
| token | `enum class TokenType`, `reserved_word()`, `operator_token()`, `to_string()`; `g_tokens`, `addTokenRecord()`, `setCategory()`, `printTokenTable()` |
| diagnostics | `struct Diagnostic`, `g_diagnostics`, `reportDiagnostic()`, `hasErrors()`, `errorDiagnostics()`, `warningDiagnostics()`, `printDiagnostic()`, `displayLine()`, `g_lineOrigins` |
| preprocessor | `preprocessFile()`, `openPreprocessed()` |
| ast | `ASTKind`, `ASTNode`, `ASTTypeExpr`, `mkNode()`, `addChild()`, `printAST()`, `g_astRoot`, `anonymousTag()` |
| types | `sem::Type`, `TypeKind`, `RecordInfo`, `EnumInfo`; `pointerTo()`, `arrayOf()`, `functionType()` …; `sameType()`, `implicitConversion()`, `checkCast()`, `usualArithmetic()`, `integerPromotion()`, `decay()`, `sizeOf()`, `alignOf()`, `layoutRecord()`, `lookupMember()`, `typeToString()`, `wrapToType()` |
| symbol_table | part 1: `pushScope()`, `popScope()`, `declareSymbol()`, `lookupSymbol()`, `isTypeName()`, `mangle()`, `printSymbolTable()`; part 2: `sem::Symbol`, `sem::Scope`, `sem::SymbolTable`, `printSemanticSymbolTable()`, `printRecordLayouts()` |

The symbol tables are documented in detail in
[`../docs/SYMBOL_TABLE.md`](../docs/SYMBOL_TABLE.md).
