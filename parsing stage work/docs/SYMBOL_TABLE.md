# The Symbol Tables

This compiler has **two** symbol tables, both in one shared module:
[`shared/symbol_table/symbol_table.hpp`](../shared/symbol_table/symbol_table.hpp)
and `.cpp`. They have different jobs, lifetimes and data structures:

| | Part 1 — parse-time table | Part 2 — semantic table |
|---|---|---|
| Namespace | global (`::Symbol`, `declareSymbol`, …) | `sem::` (`sem::Symbol`, `sem::SymbolTable`) |
| Built by | the Bison grammar actions in [`phase2-parser/src/parser.y`](../phase2-parser/src/parser.y) and [`declarators.cpp`](../phase2-parser/src/declarators.cpp), *while* parsing | `sem::SemanticAnalyzer` in [`phase2b-semantic/src/`](../phase2b-semantic/src), walking the finished AST |
| Purpose | classify identifiers for the Token/Token_Type table (`a → INT`, `f → PROCEDURE`), drive the typedef "lexer hack", resolve overloads by argument shape, mangle names | type checking and every semantic check; the table handed to the future IR phase |
| Types | strings (`"INT_POINTER"`, `"PROCEDURE"`) | structural `sem::Type` graphs ([`shared/types/types.hpp`](../shared/types/types.hpp)) |
| Scopes | a **stack** of hash maps; a scope is destroyed when it closes | a **persistent tree** of scopes; closing a scope only pops it off the active stack |
| Printed by | `printSymbolTable()` — the parser's `=== Symbol Table ===` | `sem::printSemanticSymbolTable()` — the semantic phase's `=== Semantic Symbol Table ===` |

The parser's table exists because the parser must already know, token by
token, whether a name is a type (`T * x;` is a declaration if `T` is a
typedef, a multiplication otherwise). The semantic table exists because
type checking needs real types and scopes that survive the pass.

![Symbol table architecture](diagrams/symbol-table-architecture.svg)

*(Diagram source: [`diagrams/symbol-table-architecture.html`](diagrams/symbol-table-architecture.html).)*

---

## Part 1 — the parse-time table

### Data structures

All of these are file-static in `symbol_table.cpp`:

| Variable | Type | Role |
|---|---|---|
| `g_scopes` | `std::vector<std::unordered_map<std::string, std::vector<Symbol>>>` | the scope **stack**; index 0 is the global scope. A name maps to a vector so overloads of one function can coexist. |
| `g_scopeLabels` | `std::vector<std::string>` | parallel to `g_scopes`: what each scope is (`"main()"`, `"if"`, `"struct P"`, `"block"`) — joined into scope paths like `global > main() > if` |
| `g_typeNameScopes` | `std::vector<std::unordered_map<std::string, bool>>` | parallel to `g_scopes`: is this name a **type** here? (the lexer hack) |
| `g_symbolTable` (exported) | `std::vector<SymbolTableEntry>` | flat, append-only record of every declaration ever made, kept only for the final report (scopes are destroyed, so nothing else would survive) |
| `g_pendingReferences` | `std::vector<PendingReference>` | uses of names not yet declared (a `goto` to a later label, a call to a function defined further down), resolved after the parse |
| `g_classStack` + `g_currentClassName`, `g_currentAggregateKind`, `g_aggregateMemberDepth` | stack of `ClassContext` | which struct/union/class body we are in; nests (`struct A { struct B {…} b; int y; }` — `y` is still `A`'s member) |
| `g_anonymousTagNames`, `g_anonymousMembers` | `unordered_map` | unnamed aggregates: the typedef that names one; which unnamed members a tag can see through |

One live entry (`::Symbol`, in a scope's map):

| Field | Meaning |
|---|---|
| `kind` | `SymKind`: `VARIABLE, PROCEDURE, PARAMETER, STRUCT_TAG, UNION_TAG, ENUM_TAG, CLASS_TAG, TYPEDEF_NAME, ENUM_CONST, LABEL` |
| `typeStr` | the Token_Type text (`"INT"`, `"CHAR_POINTER"`, `"PROCEDURE"`, `"STRUCT"`) |
| `mangledName` | Itanium link name, callables only |
| `aggregateTagName` | for a variable of struct/union/class type: its tag, so `p.x` can find `x` |
| `flatIndex` | index of the matching `SymbolTableEntry` in `g_symbolTable` |
| `typeExpr` | for a `TYPEDEF_NAME`: the aliased declaration (used by mangling and member lookup) |

One report entry (`SymbolTableEntry` in `g_symbolTable`): `name`,
`qualifiedName` (`"Dog::bark"`), `kind`, `typeStr`, `mangledName`,
`scopeDepth`, `scopePath`, `ownerAggregateKind` (`"struct"`/`"union"`/
`"class"`/`""`), `declLine`, `isStatic`, `isConst`, `isVolatile`,
`pointerLevel`, `arrayLevel`, `returnType`, `paramTypes`, `useCount`.

### Operations

| Operation | Function | Algorithm | Called from |
|---|---|---|---|
| open scope | `pushScope(label)` | push an empty map onto `g_scopes` and `g_typeNameScopes`, push the label (or a pending `hintScope()` label, or `"block"`) | grammar mid-rule actions: `compound_stmt`, `function_definition` (`name()`), `for_open` (`"for"`), struct/union/class bodies, constructors/destructors, lambdas, `param_scope` |
| close scope | `popScope()` | pop all three stacks — the scope's symbols are **gone** (only `g_symbolTable` remembers them) | end of the same rules |
| insert | `declareSymbol(name, kind, typeStr, extra)` | build a `SymbolTableEntry` (qualified name from the class stack, scope path, declaration line from the token log) and append it to `g_symbolTable`; push a `Symbol` onto `g_scopes.back()[name]` | `registerDeclarator()` in `declarators.cpp` for every declarator; tag rules; enumerators; labels; parameters |
| lookup | `lookupSymbol(name)` | walk `g_scopes` from innermost to outermost; first scope containing the name wins; return its **last** pushed symbol | identifier classification in `primary_expr`, member access, `recordUsage()` |
| type lookup | `lookupTypeSymbol(name)` | same walk, but only `TYPEDEF_NAME` and tag kinds | the `TYPE_NAME` specifier rule |
| overloads | `isOverloaded(name)`, `lookupOverload(name, argTypes)` | in the innermost scope that has the name, compare each `PROCEDURE`'s `paramTypes` with `inferExprType()` of the arguments; fall back to the last declared | call expressions: the `CallExpr` label becomes the chosen mangled name |
| use count | `recordUsage(name / Symbol*)` | `++g_symbolTable[flatIndex].useCount` | every identifier use |
| forward refs | `queuePendingReference()`, `resolvePendingReferences()` | remember the token; after parsing, match against `g_symbolTable` (labels within the same function, otherwise global declarations) and fix the token's category | undeclared-at-use identifiers and `goto` targets |
| members | `findMember(tag, member)` | linear search of `g_symbolTable` for `qualifiedName == tag::member`, then through unnamed members (`g_anonymousMembers`) | `p.x` / `p->x` classification |
| type names (lexer hack) | `addTypeName`, `hideTypeName`, `isTypeName` | `isTypeName` walks `g_typeNameScopes` innermost-first; `hideTypeName` records `false` in the current scope so `int T;` hides an outer `typedef … T` | the scanner ([`scanner.l`](../phase2-parser/src/scanner.l)) decides `TYPE_NAME` vs `IDENTIFIER` with `isTypeName()` |

**No semantic errors are produced by Part 1.** A duplicate or undeclared
name here only affects the printed Token_Type; the errors come from Part 2.

---

## Part 2 — the semantic table (`sem::SymbolTable`)

### Data structures

```cpp
class SymbolTable {
    std::vector<Scope>     scopes_;  // every scope ever created; never shrinks
    std::vector<int>       stack_;   // ids of the scopes active right now, innermost last
    std::vector<SymbolPtr> all_;     // every symbol in declaration order (the printed table)
    int nextUnique_;                 // counter for "name.N" unique names
};
```

A **`Scope`** (`struct Scope`):

| Field | Meaning |
|---|---|
| `id`, `parent`, `depth` | position in the tree (`parent` = the scope active when it was entered) |
| `kind` | `ScopeKind::Global`, `Function`, `Block`, `Record`, `Lambda` |
| `label` | `"global"`, `"main()"`, `"block"`, `"for"`, `"if"`, `"struct P"`, `"lambda"` — joined by `pathOf()` into `global > main() > block` |
| `names` | `unordered_map<string, vector<SymbolPtr>>` — **ordinary identifiers**; a vector because overloaded functions share a name |
| `tags` | `unordered_map<string, SymbolPtr>` — **struct/union/class/enum tags**, a separate name space as in C |
| `ordered` | every symbol declared here, in order (tags included) |
| `record` | for a `Record` scope, its `RecordInfo` |
| `function` | for a `Function`/`Lambda` scope, the owning function symbol |

A **`sem::Symbol`** (every field that exists):

| Field | Meaning |
|---|---|
| `name` | as written |
| `uniqueName` | program-wide unique name for IR: globals keep their name, functions their mangled name, locals and parameters get `name.N` (`x.4`, `x.5`), fields `Tag::name` |
| `kind` | `SymbolKind::Variable, Parameter, Function, Field, Typedef, EnumConstant, Label, Tag` |
| `type` | `sem::TypePtr` — the structural type |
| `storage` | `Storage::None, Global, Static, Local, Param, Member` |
| `scopeId`, `scopePath`, `line`, `column` | where it was declared |
| `isConstant`, `constValue` | enum constants and `const` objects with a known integer value |
| `hasInitializer`, `useCount`, `evaluatedUses` | bookkeeping (`evaluatedUses` excludes uses inside `sizeof`) |
| `isDefined` | functions: body seen; objects: defined, not just declared `extern` |
| `isRegister`, `isStatic` | storage-class keywords |
| `isMethod`, `isConstructor`, `isDestructor`, `mangledName` | callables |
| `params`, `locals`, `bodyScopeId` | functions: parameter symbols in order (unnamed ones too), every local, the body scope |
| `ownerRecord`, `access`, `offset` | members: owning `RecordInfo`, `public`/`protected`/`private`, byte offset (MIPS32 layout) |
| `anonymousUnion` | a variable that is a member of a block-scope anonymous union: the hidden union object it lives in |
| `record`, `enumInfo` | tags: the `RecordInfo` / `EnumInfo` |
| `declNode` | the declaring AST node |

### Operations

| Purpose | Function | Algorithm | Used by |
|---|---|---|---|
| create the global scope | `SymbolTable()` | scope 0, `kind = Global`, label `"global"`, pushed on `stack_` | `main.cpp` constructs one table per run |
| enter a scope | `enterScope(kind, label, record, function)` | append a new `Scope` with `parent = stack_.back()`, push its id | `functionBody()` (Function), `statement()` for `CompoundStmt` and `ForStmt` (Block), `subStatement()` for `if`/`while`/… bodies (Block), `recordDefinition()` (Record), `lambda()` (Lambda) |
| leave a scope | `exitScope()` | pop `stack_` — the scope and its symbols **stay** in `scopes_` | the same functions |
| re-activate | `reenterScope(id)` | push an existing scope id | out-of-class member bodies (`void Dog::bark() {…}`) re-enter the class's Record scope so members resolve |
| insert (visible) | `declare(s)` / `declareIn(id, s)` | `assignNames()` (scope id, path, `uniqueName`), then `names[s->name].push_back(s)`, `ordered`, `all_` | every variable, parameter, function, typedef, enumerator |
| insert (hidden) | `declareHidden(id, s)` | recorded in `ordered`/`all_` but **not** in `names` — lookup cannot find it | labels, unnamed parameters, constructors, hidden anonymous-union objects |
| insert a tag | `declareTag` / `declareTagIn(id, s)` | `tags[s->name] = s` | struct/union/class/enum definitions and first mentions (`struct Node *next;`) |
| current-scope lookup | `lookupLocal(name)`, `lookupTagLocal(name)` | only `scopes_[stack_.back()]` | **duplicate detection** in `variable()`, `functionSignature()`, `typedefDecl()`, `enumDefinition()` |
| full lookup | `lookup(name)` → `Lookup` | walk `stack_` innermost → outermost (algorithm below) | `identifier()`, call resolution, lambda captures |
| tag lookup | `lookupTag(name)` | walk `stack_` innermost → outermost over `tags` | `resolveTag()` |
| file scope only | `saveAndResetToGlobal()` / `restoreStack()` | temporarily make only scope 0 active | `hoistFunction()`: declaring a function that is called before its definition |

### Scopes as built for a function

```
scope 0  Global  "global"
│   global          variable   int
│   add             function   int (int, int)
│   main            function   int (void)
│
├── scope 1  Function  "add()"       ← parameters AND the body's top-level declarations
│       a           parameter  int       (the body block shares this scope, as in C,
│       b           parameter  int        so `int a;` in the body is a redeclaration)
│       result      variable   int
│
└── scope 2  Function  "main()"
    │   x           variable   int    (x.4)
    └── scope 3  Block  "block"
            x       variable   int    (x.5, shadows x.4)
```

- **Entering** a scope never copies anything: the new scope is empty and
  points to its parent.
- **Shadowing** is simply that `lookup()` stops at the first scope that has
  the name: the inner `x` (`x.5`) hides the outer `x` (`x.4`).
- **Duplicate detection** uses `lookupLocal()`, which looks at the current
  scope only, so shadowing across scopes is allowed and redeclaration in
  the same scope is an error (`duplicate declaration of 'x' in the same
  scope (previous declaration at line N)`).
- **Lifetime**: every scope and symbol survives the pass; the IR phase can
  walk `scopes()` and `allSymbols()`, and every AST use already points at
  its symbol (`ASTNode::symbol`).

![Scope tree](diagrams/symbol-table-scopes.svg)

### The lookup algorithm

`SymbolTable::lookup(name)`:

```
for scope in stack_, innermost first:
    if scope.kind == Record:                    # inside a member function body
        ml = lookupMember(scope.record, name)   # fields + methods, then base classes
        if found: return {symbols, viaRecord = true}   # an implicit this->name
        continue
    if name in scope.names (non-empty):
        return {scope.names[name], scopeId}     # all overloads of a function name
    if scope.kind == Lambda:
        crossedLambda = true                    # remember: the name is outside the lambda
return {}                                       # not visible
```

`Lookup.crossedLambda` lets `identifier()` check captures: a local found
*outside* the innermost lambda must be in its capture list (or there must
be a capture-default).

![Symbol lookup flow](diagrams/symbol-lookup.svg)

#### Example: `x = y + z;`

`SemanticAnalyzer::expr()` dispatches the `AssignExpr` to
`assignment()`, which types both sides; each `Identifier` goes to
`identifier()`:

1. `st.lookup("x")` walks the active stack. Found → `n->symbol` is set
   to that symbol and `useCount` is incremented. Not found →
   `hoistFunction("x")` is tried (a top-level function declared later);
   otherwise the error `undeclared identifier 'x'` (or `… it is declared
   later, at line N; variables must be declared before use`).
2. The symbol's kind decides the result: a variable/parameter gives its
   `type` and marks the node an lvalue; an enum constant gives `int` with
   a constant value; a typedef or tag is the error `unexpected type name
   'x' where an expression was expected`.
3. `y` and `z` are looked up the same way; `binary()` applies the usual
   arithmetic conversions (`usualArithmetic()`) to get the type of `y + z`.
4. `assignment()` calls `checkModifiable(x)` (lvalue, not an array, not
   `const`, no `const` member) and `convertible(type(x), y + z)`
   (`implicitConversion()` from the types module); failure is
   `type mismatch: cannot assign 'T1' to 'T2'`.

---

## Symbols and types

A symbol's `type` is a `sem::Type` node from
[`shared/types/types.hpp`](../shared/types/types.hpp). Types are
**structural graphs**, not strings:

```cpp
struct Type {
    TypeKind kind;               // Error, Void, Bool, Char, Short, Int, Long, LongLong,
                                 // Float, Double, Enum, Pointer, Reference, Array,
                                 // Function, Record, Opaque, Closure
    bool isConst, isVolatile, isUnsigned;
    TypePtr elem;                // Pointer / Reference target, Array element
    long long arraySize;         // Array: element count, -1 for []
    TypePtr ret; std::vector<TypePtr> params; bool variadic;   // Function / Closure
    std::shared_ptr<RecordInfo> record;  std::shared_ptr<EnumInfo> enumInfo;
    std::string name;            // Opaque ("FILE", "va_list"), Closure
};
```

| Source | Representation | Size (MIPS32) |
|---|---|---|
| `int`, `char`, `short`, `long`, `long long`, `float`, `double`, `bool` | basic kinds; `unsigned` is a flag | 4, 1, 2, 4, 8, 4, 8, 1 |
| `void` | `Void` (only behind a pointer or as a return type) | — |
| `int *`, `int **`, `int ***` | `Pointer → Pointer → Pointer → Int`: depth is the length of the chain, never a counter | 4 |
| `const int *p` / `int *const p` | `Pointer(const Int)` / `const Pointer(Int)`: a qualifier sits on the level it qualifies | 4 |
| `int a[3][4]` | `Array(3, Array(4, Int))` | 48 |
| `int (*pa)[3]` | `Pointer(Array(3, Int))` (declarators are read inside-out by `resolveType()`) | 4 |
| `int f(int, char *)` | `Function(ret = Int, params = [Int, Pointer(Char)])` | — |
| `int (*fp)(int)` | `Pointer(Function(Int, [Int]))` | 4 |
| `int &r` | `Reference(Int)` | 4 |
| `struct P`, `union U`, `class C` | `Record` → a shared `RecordInfo` (fields, members, bases, layout) | from `layoutRecord()` |
| `enum E` | `Enum` → `EnumInfo` (enumerators and values) | 4 |
| `FILE`, `va_list` | `Opaque` | `va_list` 4 |
| a lambda | `Closure` (its own type) | — |

Type equality is structural for these constructors and **by name** for
records and enums: two `struct P` types are the same type exactly when
they share one `RecordInfo` (`sameType()`).

```
Identifier → lookup() → sem::Symbol → symbol.type → expression type
           → implicitConversion() / usualArithmetic() / checkCast() → OK or semantic error
```

---

## Function symbols

`functionSignature()` ([`declarations.cpp`](../phase2b-semantic/src/declarations.cpp)) registers a function:

1. `resolveType()` builds the `Function` type (parameters adjusted:
   arrays and functions decay to pointers, `f(void)` has no parameters).
2. Candidates with the same name in the scope (or class) are compared:
   - same parameter list and same return type → it is a redeclaration
     of the same symbol;
   - same parameters but a different return type → error `conflicting
     types for 'f'`;
   - different parameters → a new **overload**, pushed onto the same
     `names["f"]` vector.
3. The symbol gets its `mangledName` (Itanium C++ ABI, `mangle()` in
   the symbol-table module; `main` stays `main`) and that becomes its
   `uniqueName`.

`functionDefinition()` checks for a second body (`redefinition of
function`), sets `isDefined`, and calls `functionBody()`:

1. Re-enters the class's Record scope for a member function.
2. `enterScope(Function, "f()")`; sets `bodyScopeId`.
3. Builds the parameter symbols with `makeParamSymbol()`: named ones go
   in with `declare()` (`a.1`, `b.2`), unnamed ones with `declareHidden()`;
   all are appended to `fnSym->params`.
4. `collectLabels()` pre-declares every label of the body (labels have
   function scope, so `goto` may jump forward).
5. Pushes a `FunctionCtx` (return type, loop and switch nesting, labels)
   and analyses the body's statements in the **same** scope as the
   parameters.
6. A non-`void` function with no `return` at all gets the warning
   `non-void function 'f' has no return statement`.

**Recursion** works because the symbol is declared (step 2 above) before
its body is analysed. **Calls to functions defined later** work because
`prescan()` records every top-level function and `hoistFunction()`
declares it on first use. **Argument checking**: `call()` picks the
overload with `resolveOverload()` (exact, promotion, conversion,
ellipsis ranks; ambiguity is an error), then `checkCallArgs()` checks
the count and converts every argument as if by assignment.

![Function semantic analysis](diagrams/function-analysis.svg)

---

## Arrays

There is no separate "dimensions" field: an array is an `Array` type
node with `elem` and `arraySize`, nested for each dimension.
`resolveType()` evaluates every dimension with `arrayDimension()`, which
requires an integer constant expression greater than zero (no VLAs),
and only the first dimension may be omitted (`int a[]` takes its size
from the initializer: `int a[] = {1,2,3}` is `int[3]`).

`a[i]` is checked by `SemanticAnalyzer::index()`:

1. Both operands are typed; `a` decays to a pointer (`decay()`).
2. One operand must be a pointer and the other an integer (`i[a]` is
   accepted too, as in C); otherwise `subscripted value is not an array
   or pointer` / `array subscript is not an integer`.
3. The element must be complete (no `void *` subscripts).
4. With a constant index into an array of known size, an out-of-range
   index is the warning `array index N is past the end of the array`.
5. The result is an lvalue of the element type.

---

## Pointers

`int ***` is `Pointer(Pointer(Pointer(Int)))`, built by `resolveType()`
from the declarator's pointer operators (`ASTTypeExpr::ptrOps`, e.g.
`"*c*"` for `int *const *`).

- `&e` (`unary()`): `e` must be an lvalue (`cannot take the address of an
  rvalue`), not a `register` variable; the result is `pointerTo(type(e))`.
- `*p` (`unary()`): `p` must be a pointer (`indirection requires a
  pointer operand`), not `void *`, not a pointer to an incomplete type;
  the result is an lvalue of `p->elem`.
- Pointer arithmetic in `binary()`: pointer ± integer, pointer − pointer
  of the same type (result `int`), never pointer + pointer, nothing on
  `void *` or function pointers.
- Assignment: `implicitConversion()` allows adding qualifiers
  (`int *` → `const int *`), rejects dropping them (`conversion discards
  'const' qualifier`), allows `void *` both ways and null pointer
  constants.

---

## Structures, unions and classes

`recordDefinition()` creates (or completes) a `RecordInfo` and a `Tag`
symbol in the tag name space:

```cpp
struct RecordInfo {
    RecordKind kind;                 // Struct, Union, Class
    std::string tag, typedefName;    // typedefName: for an unnamed type, its first typedef
    bool complete;
    std::vector<SymbolPtr> fields;   // data members in declaration order
    std::map<std::string, std::vector<SymbolPtr>> members;  // name -> field or method overloads
    std::vector<SymbolPtr> constructors;  SymbolPtr destructor;
    std::vector<BaseClass> bases;    // record + inheritance access
    std::vector<SymbolPtr> promoted; // fields of unnamed members, usable directly
    long long size; int align; int scopeId;
};
```

- Members are declared in the record's own `Record` scope and in
  `members`; a duplicate is `duplicate member 'x' in struct 'P'`.
- After the body, `layoutRecord()` assigns MIPS32 offsets (bases first,
  each field aligned, unions all at 0, size rounded to the alignment).
- Member bodies are analysed after the class is complete, so every
  member is visible to every method (C++ rule).
- `p.x` / `p->x` (`member()`) use `lookupMember(record, "x")`, which
  searches the record, then its base classes (ambiguity across two bases
  is an error); `checkAccess()` enforces `private`/`protected`.
- An unnamed member (`struct S { union { int i; float f; }; };`) becomes
  an unnamed field whose fields are copied into `promoted` and `members`
  with offsets relative to `S`.

---

## Worked example (real output)

Source ([`examples/add.c`](examples/add.c), verified with the current build):

```c
int global;

int add(int a, int b) {
    int result;
    result = a + b;
    return result;
}

int main() {
    int x = 2;
    {
        int x = 3;          /* shadows the outer x */
        global = add(x, 4);
    }
    return global + x;
}
```

`phase2-parser/syntax_analyzer add.c` — Part 1 (columns abridged):

```
Name      Kind       Line  Scope                     Type       Uses  Signature       Mangled Name
global    variable   1     global                    INT        2
add       procedure  3     global                    PROCEDURE  1     INT (INT, INT)  _Z3addii
a         parameter  3     global > add()            INT        1
b         parameter  3     global > add()            INT        1
result    variable   4     global > add()            INT        2
main      procedure  9     global                    PROCEDURE  0     INT ()          main
x         variable   10    global > main()           INT        1
x         variable   12    global > main() > block   INT        1
```

`phase2b-semantic/semantic_analyzer add.c` — Part 2 (columns abridged):

```
Name    Kind       Type            Storage  Scope                    Line  Size  Uses  Unique Name  Notes
global  variable   int             global   global                   1     4     2     global
add     function   int (int, int)  -        global                   3     -     1     _Z3addii     defined
a       parameter  int             param    global > add()           3     4     1     a.1
b       parameter  int             param    global > add()           3     4     1     b.2
result  variable   int             local    global > add()           4     4     2     result.3
main    function   int (void)      -        global                   9     -     0     main         defined
x       variable   int             local    global > main()          10    4     1     x.4
x       variable   int             local    global > main() > block  12    4     1     x.5
```

and in the annotated AST, every use points at the right one:
`global = add(x, 4)` uses `x.5`, `return global + x` uses `x.4`.

---

## Extending the table

- **A new symbol attribute**: add the field to `sem::Symbol` in
  `symbol_table.hpp`, set it where the symbol is built
  (`variable()`, `functionSignature()`, `recordDefinition()` …), and if it
  should be visible, print it in `notes()` in `symbol_table.cpp`.
- **A new scope kind**: add it to `ScopeKind` and decide in `lookup()`
  whether the walk treats it specially (as it does `Record` and `Lambda`).
- **A new name space** (e.g. namespaces): add a map to `Scope` beside
  `names` and `tags`, with `declare…`/`lookup…` functions mirroring the
  tag ones.
- **For IR generation**: `allSymbols()` is the complete list; `storage`
  says where an object lives, `uniqueName` is a collision-free IR name,
  `offset` places members, `Function` symbols list `params` and `locals`.
