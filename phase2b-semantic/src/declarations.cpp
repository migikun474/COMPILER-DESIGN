/* Diagnostics, the entry point, type resolution and declarations.
   Statements are in statements.cpp, expressions in expressions.cpp, the
   C++-specific rules in cxx.cpp. */
#include "semantic.h"

#include <algorithm>
#include <functional>

#include "diagnostics/diagnostics.hpp"

namespace sem {

/* =====================================================================
   diagnostics
   ===================================================================== */

void SemanticAnalyzer::error(int line, int column, const std::string &msg, const std::string &category) {
    std::string key = std::to_string(line) + ":" + std::to_string(column) + ":" + msg;
    if (!reported.insert(key).second) return;
    ++errors;
    reportDiagnostic(line, column, "", msg + " [" + category + "]", "Semantic error");
}

void SemanticAnalyzer::error(const ASTNode *at, const std::string &msg, const std::string &category) {
    error(at ? at->line : 0, at ? at->column : 0, msg, category);
}

void SemanticAnalyzer::warning(int line, int column, const std::string &msg, const std::string &category) {
    std::string key = "w" + std::to_string(line) + ":" + std::to_string(column) + ":" + msg;
    if (!reported.insert(key).second) return;
    ++warnings;
    reportDiagnostic(line, column, "", msg + " [" + category + "]", "Semantic warning");
}

void SemanticAnalyzer::warning(const ASTNode *at, const std::string &msg, const std::string &category) {
    warning(at ? at->line : 0, at ? at->column : 0, msg, category);
}

static std::string q(const TypePtr &t) { return "'" + typeToString(t) + "'"; }

/* where a declaration's own name sits, falling back to the node */
static int lineOf(const ASTTypeExpr &te, const ASTNode *n) { return te.nameLine ? te.nameLine : (n ? n->line : 0); }
static int colOf(const ASTTypeExpr &te, const ASTNode *n) { return te.nameLine ? te.nameColumn : (n ? n->column : 0); }

static std::string tagFromLabel(const std::string &label) {
    size_t p = label.find(" : ");
    return p == std::string::npos ? label : label.substr(0, p);
}

static std::string symbolWhat(const SymbolPtr &s) {
    switch (s->kind) {
        case SymbolKind::Function: return "a function";
        case SymbolKind::Typedef: return "a typedef";
        case SymbolKind::Parameter: return "a parameter";
        case SymbolKind::EnumConstant: return "an enumerator";
        default: return "a variable";
    }
}

RecordInfo *SemanticAnalyzer::currentClass() {
    return fns.empty() ? nullptr : fns.back().cls;
}

int SemanticAnalyzer::declScopeForTags() {
    const auto &stack = st.activeStack();
    for (auto it = stack.rbegin(); it != stack.rend(); ++it) {
        if (st.scope(*it).kind != ScopeKind::Record) return *it;
    }
    return 0;
}

std::string describeSignature(const SymbolPtr &f) {
    std::string s = f->name + "(";
    if (f->type && isFunction(f->type)) {
        for (size_t i = 0; i < f->type->params.size(); ++i) {
            if (i) s += ", ";
            s += typeToString(f->type->params[i]);
        }
        if (f->type->variadic) s += f->type->params.empty() ? "..." : ", ...";
    }
    return s + ")";
}

/* =====================================================================
   entry point
   ===================================================================== */

void SemanticAnalyzer::analyze(const ASTNodePtr &root) {
    if (!root) return;
    prescan(root);
    for (const auto &item : root->children) declaration(item, DeclCtx::Global);
    checkSequencing(root); /* needs the symbols typing attached */

    /* a function that is called but has no body anywhere in the program
       can never be linked -- there is no separate compilation here */
    for (const auto &s : st.allSymbols()) {
        if (s->kind == SymbolKind::Function && !s->isDefined && s->useCount > 0 &&
            !s->isConstructor && !s->isPure) { /* a pure virtual function is only called through the table */
            warning(s->line, s->column, "function '" + s->name + "' is used but never defined",
                    "undefined-function");
        }
    }
}

void SemanticAnalyzer::prescan(const ASTNodePtr &root) {
    std::function<void(const ASTNodePtr &)> visit = [&](const ASTNodePtr &n) {
        if (!n) return;
        if (n->kind == ASTKind::DeclGroup) {
            for (const auto &c : n->children) visit(c);
        } else if ((n->kind == ASTKind::FunctionDecl || n->kind == ASTKind::FunctionDef) && n->typeExpr &&
                   n->typeExpr->className.empty()) {
            topFunctions[n->typeExpr->name].push_back(n);
        } else if (n->kind == ASTKind::VarDecl && n->typeExpr) {
            topVariableLines.emplace(n->typeExpr->name, lineOf(*n->typeExpr, n.get()));
        }
    };
    for (const auto &c : root->children) visit(c);
}

/* A file-scope function used before its declaration: declare every
   file-scope declaration of that name now, in file scope. Returns true
   if the name is such a function. */
bool SemanticAnalyzer::hoistFunction(const std::string &name) {
    auto it = topFunctions.find(name);
    if (it == topFunctions.end()) return false;
    bool any = false;
    for (const auto &n : it->second) any = any || !signatureDone.count(n.get());
    if (!any) return false;
    std::vector<int> saved = st.saveAndResetToGlobal();
    std::vector<FunctionCtx> savedFns;
    savedFns.swap(fns);
    for (const auto &n : it->second) functionSignature(n, DeclCtx::Global, n->kind == ASTKind::FunctionDef);
    fns.swap(savedFns);
    st.restoreStack(saved);
    return true;
}

/* =====================================================================
   types
   ===================================================================== */

TypePtr SemanticAnalyzer::resolveTag(const ASTTypeExpr &te, const std::string &kindPart, const ASTNode *at) {
    const std::string &tag = te.tagName.empty() ? te.typedefName : te.tagName;
    int line = lineOf(te, at), col = colOf(te, at);
    SymbolPtr sym = st.lookupTag(tag);
    if (kindPart == "ENUM") { /* C++: no forward-declared (opaque) enums in this language */
        if (sym && sym->enumInfo) return enumType(sym->enumInfo);
        if (sym) error(line, col, "'" + tag + "' is not an enum (it is a " + recordKindName(sym->record->kind) + ")",
                       "tag-mismatch");
        else error(line, col, "use of undeclared enum 'enum " + tag + "'", "unknown-type");
        return errorType();
    }
    /* `struct Dog` may name a class and `class Point` a struct (C++), but a
       union is a different kind of tag */
    RecordKind want = kindPart == "UNION" ? RecordKind::Union
                      : kindPart == "CLASS" ? RecordKind::Class
                                            : RecordKind::Struct;
    if (sym) {
        if (!sym->record) {
            error(line, col, "use of '" + tag + "' with tag type '" + recordKindName(want) +
                                 "' that does not match its declaration as an enum",
                  "tag-mismatch");
            return errorType();
        }
        if ((want == RecordKind::Union) != (sym->record->kind == RecordKind::Union)) {
            error(line, col, "use of '" + tag + "' with tag type '" + recordKindName(want) +
                                 "' that does not match its declaration as '" + recordKindName(sym->record->kind) + "'",
                  "tag-mismatch");
        }
        return recordType(sym->record);
    }
    /* first mention, e.g. `struct Node *next;`: declares an incomplete type */
    auto rec = std::make_shared<RecordInfo>();
    rec->kind = want;
    rec->tag = tag;
    rec->declLine = line;
    auto ts = std::make_shared<Symbol>();
    ts->name = tag;
    ts->kind = SymbolKind::Tag;
    ts->record = rec;
    ts->line = line;
    ts->column = col;
    st.declareTagIn(declScopeForTags(), ts);
    return recordType(rec);
}

TypePtr SemanticAnalyzer::resolveSpecifiers(const ASTTypeExpr &te, const ASTNode *at, bool &isAuto) {
    isAuto = false;
    int line = lineOf(te, at), col = colOf(te, at);
    TypePtr base;
    if (!te.typedefName.empty()) {
        if (te.specParts.size() != 1) {
            error(line, col, "cannot combine type name '" + te.typedefName + "' with other type specifiers",
                  "invalid-specifiers");
        }
        Lookup l = st.lookup(te.typedefName);
        SymbolPtr td;
        for (const auto &s : l.symbols) {
            if (s->kind == SymbolKind::Typedef) td = s;
        }
        if (td) {
            base = td->type;
        } else if (SymbolPtr tag = st.lookupTag(te.typedefName)) {
            base = tag->enumInfo ? enumType(tag->enumInfo) : recordType(tag->record); /* `Color c;` (C++) */
        } else {
            error(line, col, "unknown type name '" + te.typedefName + "'", "unknown-type");
            base = errorType();
        }
    } else {
        std::map<std::string, int> n;
        for (const auto &p : te.specParts) n[p]++;
        for (const char *tagKw : {"STRUCT", "CLASS", "UNION", "ENUM"}) {
            if (n.count(tagKw)) {
                if (te.specParts.size() != 1) {
                    error(line, col, "cannot combine a struct/union/class/enum type with other type specifiers",
                          "invalid-specifiers");
                }
                return qualified(resolveTag(te, tagKw, at), te.isConst);
            }
        }
        if (te.specParts.empty()) {
            if (te.isAuto) {
                isAuto = true;
                return nullptr;
            }
            warning(line, col, "type specifier missing, defaults to 'int'", "implicit-int");
            return qualified(intType(), te.isConst);
        }
        auto c = [&](const char *k) { return n.count(k) ? n[k] : 0; };
        int ints = c("INT"), chars = c("CHAR"), shorts = c("SHORT"), longs = c("LONG"), sig = c("SIGNED"),
            uns = c("UNSIGNED"), flts = c("FLOAT"), dbls = c("DOUBLE"), voids = c("VOID"), bools = c("BOOL"),
            valists = c("VA_LIST");
        std::string spelled;
        for (const auto &p : te.specParts) {
            std::string lower = p;
            std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
            spelled += (spelled.empty() ? "" : " ") + lower;
        }
        bool bad = ints > 1 || chars > 1 || shorts > 1 || longs > 2 || sig > 1 || uns > 1 || flts > 1 ||
                   dbls > 1 || voids > 1 || bools > 1 || valists > 1 || (sig && uns);
        int others = static_cast<int>(te.specParts.size());
        if (!bad) {
            if (voids || bools || flts || valists) {
                bad = others != 1;
                base = voids ? voidType() : bools ? boolType()
                     : valists ? opaqueType("va_list") : basicType(TypeKind::Float);
            } else if (dbls) {
                bad = others != 1; /* `long double` is not a type of this language */
                base = doubleType();
            } else if (chars) {
                bad = ints || shorts || longs;
                base = basicType(TypeKind::Char, uns > 0);
            } else if (shorts) {
                bad = longs > 0;
                base = basicType(TypeKind::Short, uns > 0);
            } else if (longs) {
                base = basicType(longs == 2 ? TypeKind::LongLong : TypeKind::Long, uns > 0);
            } else {
                base = basicType(TypeKind::Int, uns > 0);
            }
        }
        if (bad) {
            error(line, col, "invalid combination of type specifiers '" + spelled + "'", "invalid-specifiers");
            base = errorType();
        }
    }
    /* `const Row r` with `typedef int Row[4]`: the elements are const */
    if (base && isArray(base) && te.isConst) {
        std::function<TypePtr(const TypePtr &)> elements = [&](const TypePtr &a) -> TypePtr {
            return isArray(a) ? arrayOf(elements(a->elem), a->arraySize) : qualified(a, te.isConst);
        };
        return elements(base);
    }
    return qualified(base, te.isConst);
}

long long SemanticAnalyzer::arrayDimension(const ASTNodePtr &dim, const ASTNode *at) {
    TypePtr t = value(dim);
    if (isError(t)) return 1;
    if (!isIntegral(t) || !dim->hasConstValue) {
        error(dim.get() ? dim.get() : at,
              "array size must be an integer constant expression (variable-length arrays are not supported)",
              "array-size");
        return 1;
    }
    if (dim->constValue <= 0) {
        error(dim.get(), "array size must be greater than zero ('" + std::to_string(dim->constValue) + "' given)",
              "array-size");
        return 1;
    }
    return dim->constValue;
}

std::vector<TypePtr> SemanticAnalyzer::resolveParams(const ASTTypeExpr &te, const ASTNode *at) {
    std::vector<TypePtr> out;
    /* `f(void)` means no parameters */
    if (te.params.size() == 1) {
        const ASTTypeExpr &p = *te.params[0];
        if (p.specParts.size() == 1 && p.specParts[0] == "VOID" && p.typedefName.empty() && p.pointerLevel == 0 &&
            p.arrayDims.empty() && !p.isFunction && p.name.empty()) {
            return out;
        }
    }
    for (const auto &p : te.params) {
        Resolved r = resolveType(*p, at, true);
        int line = p->nameLine ? p->nameLine : lineOf(te, at);
        int col = p->nameLine ? p->nameColumn : colOf(te, at);
        if (r.isAuto) {
            error(line, col, "'auto' is not allowed in a function parameter", "auto");
            r.type = errorType();
        } else if (isVoid(r.type)) {
            error(line, col, "parameter" + (p->name.empty() ? std::string() : " '" + p->name + "'") +
                                 " cannot have type 'void'",
                  "invalid-parameter");
            r.type = errorType();
        } else if (isFunction(r.type)) {
            /* C would adjust it to a pointer to the function; there are none */
            error(line, col, "parameter" + (p->name.empty() ? std::string() : " '" + p->name + "'") +
                                 " cannot have a function type (function pointers are not supported)",
                  "invalid-parameter");
            r.type = errorType();
        }
        out.push_back(r.type);
    }
    return out;
}

SemanticAnalyzer::Resolved SemanticAnalyzer::resolveType(const ASTTypeExpr &te, const ASTNode *at, bool isParam) {
    Resolved r;
    int line = lineOf(te, at), col = colOf(te, at);
    std::string who = te.name.empty() ? std::string("type") : "'" + te.name + "'";
    bool isAuto = false;
    TypePtr base = resolveSpecifiers(te, at, isAuto);
    if (isAuto) {
        if (te.pointerLevel || !te.arrayDims.empty() || te.isFunction) {
            error(line, col, "'auto' can only deduce the type of a plain variable", "auto");
            r.type = errorType();
            return r;
        }
        r.isAuto = true;
        return r;
    }
    if (!base) base = errorType();

    /* C declarators read inside-out: base type, then the pointers written
       before any `( ... )` group, then the suffix after the group (a
       parameter list or array dimensions), then what is inside the
       group. `int (*pa)[3]` is therefore pointer-to-array, `int *pa[3]`
       array-of-pointers. */
    /* pointer operators in source order ('*', '&', and 'c'/'v' qualifying
       the pointer before them); older snapshots only carry counts */
    std::string outerOps = te.ptrOps, innerOps = te.innerPtrOps;
    if (outerOps.empty() && innerOps.empty() && te.pointerLevel > 0) {
        outerOps = te.isReference ? "&" + std::string(te.pointerLevel - 1, '*') : std::string(te.pointerLevel, '*');
    }
    size_t innerDims = te.grouped ? std::min<size_t>(te.innerArrayCount, te.arrayDims.size()) : 0;

    auto wrapPointers = [&](TypePtr t, const std::string &ops) {
        for (char op : ops) {
            if (isError(t)) return t;
            if (op == 'c') {
                t = qualified(t, true);
            } else if (isFunction(t)) {
                /* only reachable through a typedef of a function type */
                error(line, col, who + " declared as a " + std::string(op == '&' ? "reference" : "pointer") +
                                     " to a function (function pointers are not supported)",
                      "invalid-declarator");
                return errorType();
            } else if (isReference(t)) {
                error(line, col, who + " declared as a " + std::string(op == '&' ? "reference" : "pointer") +
                                     " to a reference",
                      "invalid-declarator");
                return errorType();
            } else if (op == '&') {
                if (isVoid(t)) {
                    error(line, col, "cannot form a reference to 'void'", "invalid-declarator");
                    return errorType();
                }
                t = referenceTo(t);
            } else {
                t = pointerTo(t);
            }
        }
        return t;
    };
    auto wrapArrays = [&](TypePtr t, size_t from, size_t to) {
        for (size_t i = to; i-- > from && !isError(t);) {
            const ASTNodePtr &d = te.arrayDims[i];
            long long size = d ? arrayDimension(d, at) : -1;
            if (size < 0 && i > 0) {
                error(line, col, "only the first dimension of array " + who + " may be left unspecified",
                      "array-size");
                return errorType();
            }
            if (isReference(t)) {
                error(line, col, who + " declared as an array of references", "invalid-declarator");
                return errorType();
            }
            if (isVoid(t) || isFunction(t) || (!isError(t) && !isComplete(t) && !isArray(t))) {
                error(line, col, "array " + who + " has incomplete element type " + q(t), "incomplete-type");
                return errorType();
            }
            t = arrayOf(t, size);
        }
        return t;
    };

    TypePtr t = wrapPointers(base, outerOps);
    if (te.isFunction) {
        if (innerDims < te.arrayDims.size()) {
            error(line, col, "function " + who + " cannot return an array type", "invalid-declarator");
            t = errorType();
        }
        t = functionType(t, resolveParams(te, at), te.isVariadic);
    } else {
        t = wrapArrays(t, innerDims, te.arrayDims.size());
    }
    if (te.grouped) {
        t = wrapPointers(t, innerOps);
        t = wrapArrays(t, 0, innerDims);
    }
    if (isParam && isArray(t)) t = pointerTo(t->elem); /* `int a[]` / `char *argv[]` adjust to pointers */
    r.type = t;
    return r;
}

/* =====================================================================
   declarations
   ===================================================================== */

/* an object of type `t` runs a constructor: its class, a base or a member (or an array element's) has one */
static bool hasConstructor(const TypePtr &tIn) {
    TypePtr t = tIn;
    while (t && isArray(t)) t = t->elem;
    RecordInfo *rec = t && isRecord(t) ? t->record.get() : nullptr;
    if (!rec || !rec->complete) return false;
    if (!rec->constructors.empty() || rec->polymorphic) return true; /* a vptr to set up */
    for (const auto &b : rec->bases)
        if (b.record && hasConstructor(recordType(b.record))) return true;
    for (const auto &f : rec->fields)
        if (f->storage == Storage::Member && hasConstructor(f->type)) return true;
    return false;
}

/* a C++ class rather than a plain C struct: declared `class`, or with a
   base, member functions or a constructor (D35 forbids defining these
   inside a function or another class; data-only structs are still C) */
static bool isCxxClass(const ASTNodePtr &n) {
    if (n->kind == ASTKind::ClassDecl || !n->bases.empty()) return true;
    for (const auto &m : n->children) {
        if (m->kind == ASTKind::FunctionDef || m->kind == ASTKind::FunctionDecl || m->kind == ASTKind::ConstructorDef ||
            m->kind == ASTKind::FriendDecl)
            return true;
        if (m->kind == ASTKind::DeclGroup)
            for (const auto &c : m->children)
                if (c->kind == ASTKind::FunctionDecl || c->kind == ASTKind::FunctionDef) return true;
    }
    return false;
}

/* a class defined inside a function body (D35: no local classes) */
static bool definesLocalRecord(const ASTNodePtr &n) {
    if (n->kind == ASTKind::StructDecl || n->kind == ASTKind::ClassDecl) return isCxxClass(n);
    if (n->kind == ASTKind::DeclGroup)
        for (const auto &c : n->children)
            if ((c->kind == ASTKind::StructDecl || c->kind == ASTKind::ClassDecl) && isCxxClass(c)) return true;
    return false;
}

void SemanticAnalyzer::declaration(const ASTNodePtr &n, DeclCtx ctx) {
    if (!n) return;
    if (ctx == DeclCtx::Local && definesLocalRecord(n)) {
        error(n.get(), "a class cannot be defined inside a function (no local classes): define it at file scope", "local-class");
        return;
    }
    switch (n->kind) {
        case ASTKind::VarDecl: variable(n, ctx); break;
        case ASTKind::FunctionDecl: functionSignature(n, ctx, false); break;
        case ASTKind::FunctionDef: functionDefinition(n, ctx); break;
        case ASTKind::TypedefDecl: typedefDecl(n); break;
        case ASTKind::DeclGroup:
            /* `struct { ... } p;`: the type, then what it declares */
            for (const auto &c : n->children) {
                if (c->kind == ASTKind::StructDecl || c->kind == ASTKind::ClassDecl || c->kind == ASTKind::UnionDecl)
                    recordDefinition(c);
                else if (c->kind == ASTKind::EnumDecl)
                    enumDefinition(c);
                else
                    declaration(c, ctx);
            }
            break;
        case ASTKind::StructDecl:
        case ASTKind::ClassDecl:
        case ASTKind::UnionDecl:
            recordDefinition(n);
            /* `struct { int x; };`: a type nobody can name (gcc says the same) */
            if (isAnonymousTag(tagFromLabel(n->label))) {
                if (n->kind == ASTKind::UnionDecl)
                    error(n.get(), "anonymous unions are not supported: name the union or declare a variable of it",
                          "anonymous-union");
                else
                    warning(n.get(), "unnamed struct that defines no instances", "anonymous");
            }
            break;
        case ASTKind::EnumDecl: enumDefinition(n); break; /* `enum { A, B };` declares A and B */
        case ASTKind::ConstructorDef: outOfClassSpecial(n); break; /* `Dog::Dog() {}` */
        default: break; /* ErrorNode: only reachable with syntax errors, which skip this phase */
    }
}

SymbolPtr SemanticAnalyzer::variable(const ASTNodePtr &n, DeclCtx ctx) {
    if (!n->typeExpr) return nullptr;
    const ASTTypeExpr &te = *n->typeExpr;
    int line = lineOf(te, n.get()), col = colOf(te, n.get());
    const std::string &name = te.name;
    ASTNodePtr init = n->children.empty() ? nullptr : n->children[0];

    Resolved r = resolveType(te, n.get(), false);
    TypePtr t = r.type;
    /* `int Dog::count = 5;`: the definition of a static data member, not a
       new file-scope variable */
    if (ctx == DeclCtx::Global && !te.className.empty()) {
        SymbolPtr tag = st.lookupTag(te.className);
        MemberLookup ml = tag && tag->record ? lookupMember(tag->record.get(), name) : MemberLookup();
        SymbolPtr member = ml.symbols.empty() ? nullptr : ml.symbols.front();
        if (!member || member->kind != SymbolKind::Field || member->storage != Storage::Static) {
            error(line, col, "'" + te.className + "::" + name + "' is not a static data member of '" + te.className + "'",
                  "member-access");
            if (init) expr(init);
            return nullptr;
        }
        if (t && !isError(t) && !sameType(t, member->type)) {
            error(line, col, "definition of '" + te.className + "::" + name + "' with type " + q(t) +
                                 " does not match its declaration as " + q(member->type),
                  "conflicting-types");
        }
        if (init) {
            checkInitializer(member->type, init, true, "static member '" + te.className + "::" + name + "'");
            member->hasInitializer = true;
        }
        member->isDefined = true;
        member->declNode = n.get();
        n->symbol = member;
        n->semType = member->type;
        return member;
    }
    if (r.isAuto) {
        if (!init) {
            error(line, col, "declaration of '" + name + "' with deduced type 'auto' requires an initializer", "auto");
            t = errorType();
        } else if (init->kind == ASTKind::InitializerList) {
            error(init.get(), "cannot deduce 'auto' from a brace-enclosed initializer list", "auto");
            t = errorType();
        } else {
            TypePtr it = expr(init);
            if (isVoid(it)) {
                error(init.get(), "variable '" + name + "' cannot be deduced from an expression of type 'void'", "auto");
                t = errorType();
            } else {
                t = qualified(decay(it), te.isConst);
            }
        }
    }

    Storage storage = ctx == DeclCtx::Global ? Storage::Global
                      : ctx == DeclCtx::Member ? (te.isStatic ? Storage::Static : Storage::Member)
                                               : (te.isStatic ? Storage::Static : Storage::Local);
    std::string what = ctx == DeclCtx::Member ? "field" : "variable";

    /* storage classes (C11 6.7.1) */
    if (te.storageClasses > 1)
        error(line, col, "multiple storage classes in the declaration of '" + name + "'", "storage-class");

    /* `int a[] = {1, 2, 3};` / `char s[] = "abc";`: the size comes from the initializer */
    if (isArray(t) && t->arraySize < 0) {
        if (init && init->kind == ASTKind::InitializerList) {
            elideBraces(t, init); /* `int m[][2] = {1, 2, 3, 4}` has 2 rows */
            long long count = 0, pos = 0;
            for (const auto &c : init->children) {
                if (c->kind == ASTKind::DesignatedInit && c->label[0] == '[') pos = std::max(0LL, designatorIndex(c));
                count = std::max(count, ++pos);
            }
            if (count == 0) {
                error(line, col, "zero-size array '" + name + "' (an empty initializer gives the array no elements)",
                      "array-size");
            }
            t = qualified(arrayOf(t->elem, std::max(1LL, count)), t->isConst);
        } else if (init && init->kind == ASTKind::StringLiteral && t->elem && t->elem->kind == TypeKind::Char) {
            TypePtr lit = expr(init);
            t = arrayOf(t->elem, lit->arraySize);
        } else if (ctx != DeclCtx::Member || !init) {
            error(line, col, "definition of " + what + " '" + name +
                                 "' with array type needs an explicit size or an initializer",
                  "array-size");
            t = errorType();
        }
    }

    if (isVoid(t)) {
        error(line, col, what + " '" + name + "' has incomplete type 'void'", "incomplete-type");
        t = errorType();
    } else if (!isError(t) && !isComplete(t) && !isReference(t)) {
        error(line, col, what + " '" + name + "' has incomplete type " + q(t), "incomplete-type");
        t = errorType();
    }
    checkNotAbstract(t, line, col, what + " '" + name + "'");
    if (isReference(t) && !init && ctx != DeclCtx::Member) {
        error(line, col, "declaration of reference variable '" + name + "' requires an initializer", "reference");
    }

    if (ctx != DeclCtx::Member) {
        std::vector<SymbolPtr> existing = st.lookupLocal(name);
        if (!existing.empty()) {
            const SymbolPtr &prev = existing.front();
            if (prev->kind == SymbolKind::Variable || prev->kind == SymbolKind::Parameter) {
                error(line, col, std::string(prev->kind == SymbolKind::Parameter ? "redefinition of parameter '"
                                                                                  : "duplicate declaration of '") +
                                     name + "' in the same scope (previous declaration at line " +
                                     displayLine(prev->line) + ")",
                      "redeclaration");
            } else {
                error(line, col, "redefinition of '" + name + "' as a different kind of symbol (previously declared as " +
                                     symbolWhat(prev) + " at line " + displayLine(prev->line) + ")",
                      "redeclaration");
            }
            if (init && !r.isAuto) checkInitializer(t, init, false, "variable '" + name + "'");
            return nullptr;
        }
    }

    auto sym = std::make_shared<Symbol>();
    sym->name = name;
    sym->kind = SymbolKind::Variable;
    sym->type = t;
    sym->storage = storage;
    sym->line = line;
    sym->column = col;
    sym->isStatic = te.isStatic;
    sym->isDefined = true; /* every object declaration defines it (there is no `extern`) */
    sym->declNode = n.get();
    if (ctx == DeclCtx::Member) {
        sym->kind = SymbolKind::Field;
    } else {
        st.declare(sym);
        if (FunctionCtx *f = fn()) {
            if (f->fn) f->fn->locals.push_back(sym);
        }
    }
    n->symbol = sym;
    n->semType = t;

    if (ctx == DeclCtx::Local && storage == Storage::Static && hasConstructor(t)) {
        /* D35: no lazily constructed static locals (C++ builds them on first use) */
        error(line, col, "static local '" + name + "' of type " + q(t) +
                             " is not supported: its class has a constructor (make it a global or a non-static local)",
              "static-object");
        return sym;
    }
    if (!init && ctx != DeclCtx::Member && !isError(t)) defaultConstruct(t, n.get());
    if (init) {
        sym->hasInitializer = true;
        bool requireConstant = (storage == Storage::Global || storage == Storage::Static) && ctx != DeclCtx::Member;
        if (r.isAuto) {
            if (requireConstant && !isError(t) && !isConstantInitializer(init)) {
                error(init.get(), "initializer element is not a compile-time constant (required for " +
                                      std::string(storage == Storage::Global ? "global" : "static") + " '" + name + "')",
                      "non-constant-initializer");
            }
        } else {
            checkInitializer(t, init, requireConstant, what + " '" + name + "'");
        }
        if (t && t->isConst && isIntegral(t) && init->hasConstValue) {
            sym->isConstant = true;
            sym->constValue = init->constValue;
        }
    }
    return sym;
}

long long SemanticAnalyzer::designatorIndex(const ASTNodePtr &d) {
    const ASTNodePtr &e = d->children[0];
    if (!e->semType) {
        TypePtr t = value(e);
        if (isError(t)) return -1;
        if (!isIntegral(t) || !e->hasConstValue) {
            error(e.get(), "array designator index must be an integer constant expression", "initializer");
            e->semType = errorType();
            return -1;
        }
        if (e->constValue < 0) {
            error(e.get(), "array designator index " + std::to_string(e->constValue) + " is negative", "initializer");
            e->semType = errorType();
            return -1;
        }
    }
    return isError(e->semType) ? -1 : e->constValue;
}

bool SemanticAnalyzer::isConstantInitializer(const ASTNodePtr &n) {
    if (!n) return false;
    if (n->hasConstValue) return true;
    switch (n->kind) {
        case ASTKind::IntLiteral: case ASTKind::FloatLiteral: case ASTKind::CharLiteral:
        case ASTKind::StringLiteral: case ASTKind::BoolLiteral: case ASTKind::SizeofExpr:
            return true;
        case ASTKind::Identifier:
            /* a file-scope/static array designates a link-time address */
            return n->symbol && (n->symbol->storage == Storage::Global || n->symbol->storage == Storage::Static) &&
                   isArray(n->symbol->type);
        case ASTKind::UnaryExpr:
            if (n->label == "&") {
                const ASTNodePtr &c = n->children[0];
                return c->kind == ASTKind::Identifier && c->symbol &&
                       (c->symbol->storage == Storage::Global || c->symbol->storage == Storage::Static);
            }
            if (n->label == "+" || n->label == "-" || n->label == "!" || n->label == "~")
                return isConstantInitializer(n->children[0]);
            return false;
        case ASTKind::BinaryExpr: case ASTKind::TernaryExpr: case ASTKind::CastExpr:
            for (const auto &c : n->children) {
                if (!isConstantInitializer(c)) return false;
            }
            return true;
        case ASTKind::InitializerList: case ASTKind::DesignatedInit:
            for (const auto &c : n->children) {
                if (!isConstantInitializer(c)) return false;
            }
            return true;
        case ASTKind::ConstructExpr:
            if (isRecord(n->semType)) return false;
            for (const auto &c : n->children) {
                if (!isConstantInitializer(c)) return false;
            }
            return true;
        default:
            return false;
    }
}

/* ---- brace elision (C11 6.7.9p20) ----
   An aggregate member whose initializer does not start with `{` takes
   as many of the following values as it has elements:
   `struct { int a[2]; int b; } s = {1, 2, 3};` means `{{1, 2}, 3}`.
   The list is rewritten into that fully braced form, so checking and
   code generation only ever see braced aggregates.
   ponytail: the value after a designator must be braced when it names
   an aggregate (`{.a = 1, 2}` is not elided); gcc accepts that too. */
static bool isAggregate(const TypePtr &t) {
    return t && (isArray(t) || (isRecord(t) && t->record && t->record->constructors.empty()));
}

static std::vector<SymbolPtr> memberFields(const TypePtr &t) {
    std::vector<SymbolPtr> out;
    for (const auto &f : t->record->fields)
        if (f->storage == Storage::Member) out.push_back(f);
    return out;
}

/* the initializer for one subobject of type `sub`, starting at items[i] */
ASTNodePtr SemanticAnalyzer::takeElided(const TypePtr &sub, const std::vector<ASTNodePtr> &items, size_t &i) {
    const ASTNodePtr c = items[i];
    if (c->kind == ASTKind::InitializerList) {
        elideBraces(sub, c);
        ++i;
        return c;
    }
    bool whole = !isAggregate(sub) ||
                 (c->kind == ASTKind::StringLiteral && isArray(sub) && sub->elem && sub->elem->kind == TypeKind::Char);
    if (!whole && isRecord(sub) && c->kind != ASTKind::DesignatedInit) { /* `{other, 1}`: a struct value */
        TypePtr ct = decay(expr(c));
        whole = isRecord(ct) && ct->record == sub->record;
    }
    if (whole) {
        ++i;
        return c;
    }
    ASTNodePtr group = mkNode(ASTKind::InitializerList);
    group->line = c->line;
    group->column = c->column;
    std::vector<SymbolPtr> fields = isRecord(sub) ? memberFields(sub) : std::vector<SymbolPtr>();
    size_t count = isArray(sub) ? (sub->arraySize < 0 ? items.size() : static_cast<size_t>(sub->arraySize))
                   : sub->record->kind == RecordKind::Union ? std::min<size_t>(1, fields.size()) /* a union takes one value */
                                                            : fields.size();
    for (size_t k = 0; k < count && i < items.size() && items[i]->kind != ASTKind::DesignatedInit; ++k)
        group->children.push_back(takeElided(isArray(sub) ? sub->elem : fields[k]->type, items, i));
    if (group->children.empty()) { /* nothing to fill (an empty struct): the value stays where it was */
        ++i;
        return c;
    }
    return group;
}

void SemanticAnalyzer::elideBraces(const TypePtr &target, const ASTNodePtr &list) {
    if (!isAggregate(target) || !list || list->kind != ASTKind::InitializerList) return;
    std::vector<ASTNodePtr> items = list->children, out;
    std::vector<SymbolPtr> fields = isRecord(target) ? memberFields(target) : std::vector<SymbolPtr>();
    size_t i = 0, pos = 0;
    while (i < items.size()) {
        const ASTNodePtr &c = items[i];
        if (c->kind == ASTKind::DesignatedInit) { /* only re-positions; its value is braced or a scalar */
            TypePtr sub;
            if (isArray(target) && c->label[0] == '[') {
                sub = target->elem;
            } else if (isRecord(target) && c->label[0] == '.') {
                for (size_t k = 0; k < fields.size(); ++k)
                    if (fields[k]->name == c->label.substr(1)) sub = fields[k]->type, pos = k;
            }
            if (sub && !c->children.empty()) elideBraces(sub, c->children.back());
            out.push_back(c);
            ++i;
            ++pos;
            continue;
        }
        TypePtr sub = isArray(target) ? target->elem : pos < fields.size() ? fields[pos]->type : nullptr;
        out.push_back(sub ? takeElided(sub, items, i) : items[i++]); /* past the end: an excess element, reported later */
        ++pos;
    }
    list->children = out;
}

void SemanticAnalyzer::checkInitializer(const TypePtr &target, const ASTNodePtr &init, bool requireConstant,
                                        const std::string &what) {
    if (!init) return;
    elideBraces(target, init);
    if (init->kind == ASTKind::ConstructExpr && !init->typeExpr) { /* `T x(args)` */
        constructorInit(target, init, what);
        if (requireConstant && !isRecord(target) && !isError(target) && !isConstantInitializer(init)) {
            error(init.get(), "initializer element is not a compile-time constant (" + what + " has static storage)",
                  "non-constant-initializer");
        }
        return;
    }
    if (init->kind == ASTKind::InitializerList) {
        init->semType = target;
        const auto &items = init->children;
        auto designatorMisuse = [&](const ASTNodePtr &d, const std::string &kind) {
            error(d.get(), "designator '" + d->label + "' cannot be used to initialize " + kind + " " + what, "initializer");
            for (const auto &c : d->children) {
                if (c->kind == ASTKind::InitializerList) checkInitializer(errorType(), c, false, what);
                else expr(c);
            }
        };
        if (isError(target)) {
            for (const auto &c : items) {
                if (c->kind == ASTKind::InitializerList) checkInitializer(errorType(), c, false, what);
                else expr(c);
            }
            return;
        }
        if (isArray(target)) {
            TypePtr elem = target->elem;
            bool designated = std::any_of(items.begin(), items.end(), [](const ASTNodePtr &c) {
                return c->kind == ASTKind::DesignatedInit;
            });
            if (designated) { /* `{[2] = 5, 6}`: positions continue after each designator */
                long long pos = 0;
                for (const auto &c : items) {
                    ASTNodePtr value = c;
                    if (c->kind == ASTKind::DesignatedInit) {
                        if (c->label[0] != '[') {
                            designatorMisuse(c, "the array");
                            continue;
                        }
                        long long index = designatorIndex(c);
                        value = c->children[1];
                        if (index < 0) {
                            checkInitializer(errorType(), value, false, what);
                            continue;
                        }
                        pos = index;
                        c->semType = elem;
                    }
                    if (target->arraySize >= 0 && pos >= target->arraySize) {
                        error(c.get(), "array index " + std::to_string(pos) + " in initializer exceeds the bounds of " +
                                           what + " (" + std::to_string(target->arraySize) + " elements)",
                              "initializer");
                    }
                    checkInitializer(elem, value, requireConstant, what);
                    ++pos;
                }
                return;
            }
            if (target->arraySize >= 0 && static_cast<long long>(items.size()) > target->arraySize) {
                error(items[target->arraySize].get(), "excess elements in array initializer (" + what + " has " +
                                                          std::to_string(target->arraySize) + " elements)",
                      "initializer");
            }
            for (const auto &c : items) checkInitializer(elem, c, requireConstant, what);
            return;
        }
        if (isRecord(target)) {
            RecordInfo *rec = target->record.get();
            if (rec->polymorphic) {
                error(init.get(), "an object of " + q(target) + " cannot be initialized with a brace list (its class has "
                                  "virtual functions)",
                      "initializer");
                return;
            }
            std::vector<SymbolPtr> fields;
            for (const auto &f : rec->fields) {
                if (f->storage == Storage::Member) fields.push_back(f);
            }
            size_t limit = fields.size();
            if (rec->kind == RecordKind::Union) { /* one member: the first, or the designated one */
                limit = std::min<size_t>(1, fields.size());
                if (items.size() > 1) {
                    error(items[1].get(), "excess elements in union initializer for " + q(target) +
                                              " (a union holds one member at a time)",
                          "initializer");
                    for (size_t k = 1; k < items.size(); ++k) checkInitializer(errorType(), items[k], false, what);
                }
            }
            /* positional, or `.field = v` (later positional values continue after it) */
            size_t pos = 0;
            for (const auto &c : items) {
                ASTNodePtr value = c;
                if (c->kind == ASTKind::DesignatedInit) {
                    if (c->label[0] != '.') {
                        designatorMisuse(c, "the " + recordKindName(rec->kind));
                        continue;
                    }
                    std::string fieldName = c->label.substr(1);
                    auto it = std::find_if(fields.begin(), fields.end(),
                                           [&](const SymbolPtr &f) { return f->name == fieldName; });
                    /* `.i = 1` where i is in an unnamed member: initializes that member */
                    auto promoted = std::find_if(rec->promoted.begin(), rec->promoted.end(),
                                                 [&](const SymbolPtr &f) { return f->name == fieldName; });
                    if (it == fields.end() && promoted != rec->promoted.end()) {
                        for (size_t k = 0; k < fields.size(); ++k) {
                            if (fields[k]->name.empty() && fields[k]->type && fields[k]->type->record &&
                                lookupMember(fields[k]->type->record.get(), fieldName).symbols.size()) {
                                pos = k;
                                break;
                            }
                        }
                        c->symbol = *promoted;
                        c->semType = (*promoted)->type;
                        checkInitializer((*promoted)->type, c->children[0], requireConstant, what);
                        ++pos;
                        continue;
                    }
                    if (it == fields.end()) {
                        error(c.get(), "unknown member '" + fieldName + "': no member named '" + fieldName + "' in " +
                                           q(target),
                              "unknown-member");
                        checkInitializer(errorType(), c->children[0], false, what);
                        continue;
                    }
                    pos = static_cast<size_t>(it - fields.begin());
                    c->symbol = *it;
                    c->semType = (*it)->type;
                    value = c->children[0];
                }
                if (rec->kind == RecordKind::Union && c != items.front()) break; /* reported above */
                if (pos >= limit && !(rec->kind == RecordKind::Union && c->kind == ASTKind::DesignatedInit)) {
                    error(c.get(), "excess elements in " + recordKindName(rec->kind) + " initializer for " + q(target),
                          "initializer");
                    checkInitializer(errorType(), value, false, what);
                } else {
                    checkInitializer(fields[pos]->type, value, requireConstant, what);
                }
                ++pos;
            }
            return;
        }
        if (isReference(target)) {
            error(init.get(), "a reference cannot be initialized with a brace-enclosed list", "initializer");
            return;
        }
        if (items.empty()) return; /* `int x = {};` value-initializes (C23 / C++) */
        if (items[0]->kind == ASTKind::DesignatedInit) {
            designatorMisuse(items[0], "the scalar");
            return;
        }
        if (items.size() > 1) error(items[1].get(), "excess elements in scalar initializer", "initializer");
        checkInitializer(target, items[0], requireConstant, what);
        return;
    }

    if (isArray(target)) {
        TypePtr it = expr(init);
        if (init->kind == ASTKind::StringLiteral && target->elem && target->elem->kind == TypeKind::Char) {
            long long chars = it->arraySize - 1; /* without the terminating NUL, as C allows */
            if (target->arraySize >= 0 && chars > target->arraySize) {
                error(init.get(), "initializer-string for char array is too long (" + std::to_string(chars) +
                                      " characters for " + q(target) + ")",
                      "initializer");
            }
            return;
        }
        if (!isError(it)) {
            error(init.get(), "array " + what + " must be initialized with a brace-enclosed list" +
                                  std::string(target->elem && target->elem->kind == TypeKind::Char ? " or a string literal" : ""),
                  "initializer");
        }
        return;
    }

    if (isReference(target)) {
        TypePtr it = expr(init);
        if (isError(it) || isError(target)) return;
        const TypePtr &T = target->elem;
        bool binds = init->isLValue && (T->isConst || !it->isConst) &&
                     (sameType(unqualified(T), unqualified(it)) ||
                      (isRecord(T) && isRecord(it) && isDerivedFrom(it->record.get(), T->record.get())));
        if (binds) return;
        if (T->isConst) {
            convertible(T, init, "type mismatch: cannot bind a reference of type '%T' to a value of type '%F'");
            return;
        }
        error(init.get(), "non-const reference of type " + q(target) + " cannot bind to " +
                              (init->isLValue ? "an lvalue of type " + q(it) : "a temporary of type " + q(it)),
              "reference");
        return;
    }

    TypePtr it = expr(init);
    if (isError(it) || isError(target)) return;
    if (convertible(target, init, "type mismatch: cannot initialize " + what + " of type '%T' with a value of type '%F'") &&
        requireConstant && !isConstantInitializer(init)) {
        error(init.get(), "initializer element is not a compile-time constant (" + what + " has static storage)",
              "non-constant-initializer");
    }
}

void SemanticAnalyzer::typedefDecl(const ASTNodePtr &n) {
    if (!n->typeExpr) return;
    const ASTTypeExpr &te = *n->typeExpr;
    int line = lineOf(te, n.get()), col = colOf(te, n.get());
    Resolved r = resolveType(te, n.get(), false);
    if (r.isAuto) {
        error(line, col, "'auto' is not allowed in a typedef", "auto");
        r.type = errorType();
    }
    int scopeId = declScopeForTags();
    auto &names = st.scope(scopeId).names;
    auto it = names.find(te.name);
    if (it != names.end() && !it->second.empty()) {
        const SymbolPtr &prev = it->second.front();
        if (prev->kind != SymbolKind::Typedef) {
            error(line, col, "redefinition of '" + te.name + "' as a different kind of symbol (previously declared as " +
                                 symbolWhat(prev) + " at line " + displayLine(prev->line) + ")",
                  "redeclaration");
        } else if (!sameType(prev->type, r.type, true)) {
            error(line, col, "typedef redefinition with different types (" + q(r.type) + " vs " + q(prev->type) + ")",
                  "redeclaration");
        } else {
            n->symbol = prev;
        }
        return;
    }
    /* `typedef struct { ... } Pt;`: the unnamed type is called Pt from now
       on, in messages and in mangled names (the first typedef wins) */
    if (r.type && !r.type->isConst) {
        if (r.type->kind == TypeKind::Record && r.type->record && isAnonymousTag(r.type->record->tag) &&
            r.type->record->typedefName.empty())
            r.type->record->typedefName = te.name;
        if (isEnum(r.type) && isAnonymousTag(r.type->enumInfo->tag) && r.type->enumInfo->typedefName.empty())
            r.type->enumInfo->typedefName = te.name;
    }
    auto sym = std::make_shared<Symbol>();
    sym->name = te.name;
    sym->kind = SymbolKind::Typedef;
    sym->type = r.type;
    sym->line = line;
    sym->column = col;
    sym->declNode = n.get();
    st.declareIn(scopeId, sym);
    n->symbol = sym;
    n->semType = r.type;
}

SymbolPtr SemanticAnalyzer::functionSignature(const ASTNodePtr &n, DeclCtx ctx, bool isDefinition) {
    if (!n->typeExpr) return nullptr;
    if (signatureDone.count(n.get())) return n->symbol;
    signatureDone.insert(n.get());
    const ASTTypeExpr &te = *n->typeExpr;
    int line = lineOf(te, n.get()), col = colOf(te, n.get());
    const std::string &name = te.name;

    Resolved r = resolveType(te, n.get(), false);
    if (r.isAuto) {
        error(line, col, "'auto' return types are not supported", "auto");
        return nullptr;
    }
    TypePtr ft = r.type;
    if (!isFunction(ft)) return nullptr;
    for (size_t i = 0; i < ft->params.size(); ++i)
        checkNotAbstract(ft->params[i], line, col, "parameter " + std::to_string(i + 1) + " of '" + name + "'");
    checkNotAbstract(ft->ret, line, col, "the return type of '" + name + "'");
    if (isDefinition && ctx != DeclCtx::Member && !isVoid(ft->ret) && !isError(ft->ret) && !isComplete(ft->ret) &&
        !isReference(ft->ret)) {
        error(line, col, "function '" + name + "' has incomplete return type " + q(ft->ret), "incomplete-type");
    }

    RecordInfo *rec = ctx == DeclCtx::Member ? st.current().record : nullptr;
    std::vector<SymbolPtr> candidates;
    if (rec) {
        auto it = rec->members.find(name);
        if (it != rec->members.end()) candidates = it->second;
    } else if (ctx == DeclCtx::Local) {
        /* a block-scope prototype names the file-scope function */
        if (topFunctions.count(name)) hoistFunction(name);
        auto &globals = st.scope(0).names;
        auto g = globals.find(name);
        if (g != globals.end()) {
            for (const auto &c : g->second) {
                if (c->kind == SymbolKind::Function && sameParameterLists(c->type, ft) && sameType(c->type->ret, ft->ret, true)) {
                    st.current().names[name].push_back(c);
                    n->symbol = c;
                    return c;
                }
            }
        }
        candidates = st.lookupLocal(name);
    } else {
        candidates = st.lookupLocal(name);
    }

    for (const auto &c : candidates) {
        if (c->kind != SymbolKind::Function) {
            error(line, col, "redefinition of '" + name + "' as a different kind of symbol (previously declared as " +
                                 symbolWhat(c) + " at line " + displayLine(c->line) + ")",
                  rec ? "duplicate-member" : "redeclaration");
            return nullptr;
        }
        if (sameParameterLists(c->type, ft)) {
            if (!sameType(c->type->ret, ft->ret, true)) {
                error(line, col, "conflicting types for '" + name + "': " + q(ft) +
                                     " does not match the previous declaration " + q(c->type) + " at line " +
                                     displayLine(c->line) + " (functions cannot be overloaded on return type alone)",
                      "conflicting-types");
                return nullptr;
            }
            n->symbol = c;
            return c;
        }
    }
    if (name == "main" && ctx == DeclCtx::Global && !candidates.empty()) {
        error(line, col, "'main' cannot be overloaded (previous declaration at line " +
                             displayLine(candidates.front()->line) + ")",
              "main");
        return nullptr;
    }

    auto sym = std::make_shared<Symbol>();
    sym->name = name;
    sym->kind = SymbolKind::Function;
    sym->type = ft;
    sym->line = line;
    sym->column = col;
    sym->isStatic = te.isStatic;
    sym->declNode = n.get();
    /* the link name, from the resolved signature (Itanium C++ ABI) */
    sym->mangledName = (name == "main" && ctx == DeclCtx::Global) ? "main"
                                                                  : mangle(name, ft->params, ft->variadic, rec ? rec->tag : "");
    sym->uniqueName = sym->mangledName;
    /* distinct signatures always mangle differently; this only guards
       the TAC namespace against a declaration that already failed */
    for (int k = 2; std::any_of(st.allSymbols().begin(), st.allSymbols().end(), [&](const SymbolPtr &o) {
             return o->kind == SymbolKind::Function && o->uniqueName == sym->uniqueName;
         });
         ++k) {
        sym->uniqueName = (sym->mangledName.empty() ? name : sym->mangledName) + "_" + std::to_string(k);
    }
    if (te.isVirtual) { /* D44 */
        if (!rec || te.isFriend)
            error(line, col, "'virtual' can only be used on a member function, inside its class", "virtual");
        else if (te.isStatic)
            error(line, col, "static member function '" + name + "' cannot be virtual", "virtual");
        else
            sym->isVirtual = true;
    }
    sym->isPure = te.isPure && sym->isVirtual;
    if (rec) {
        sym->isMethod = true;
        sym->ownerRecord = rec;
        rec->members[name].push_back(sym);
        st.declareIn(rec->scopeId, sym);
    } else {
        st.declare(sym);
    }
    if (name == "main" && ctx == DeclCtx::Global) checkMainSignature(sym, n.get());
    if (name.compare(0, 8, "operator") == 0) checkOperatorDeclaration(sym, n.get());
    n->symbol = sym;
    n->semType = ft;
    return sym;
}

void SemanticAnalyzer::checkMainSignature(const SymbolPtr &s, const ASTNode *at) {
    const TypePtr &ft = s->type;
    if (!isError(ft->ret) && !(ft->ret->kind == TypeKind::Int && !ft->ret->isUnsigned)) {
        error(s->line, s->column, "'main' must return 'int' (declared to return " + q(ft->ret) + ")", "main");
    }
    bool ok = ft->params.empty() && !ft->variadic;
    if (ft->params.size() == 2 && !ft->variadic) {
        TypePtr argvType = pointerTo(pointerTo(charType()));
        ok = ft->params[0]->kind == TypeKind::Int && !ft->params[0]->isUnsigned &&
             sameType(ft->params[1], argvType);
    }
    if (!ok) {
        error(s->line, s->column, "invalid parameter list for 'main': expected '()' or '(int argc, char **argv)'",
              "main");
    }
    (void)at;
}

SymbolPtr SemanticAnalyzer::makeParamSymbol(const ASTTypeExprPtr &pte, const TypePtr &t, const ASTNode *at) {
    auto ps = std::make_shared<Symbol>();
    ps->name = pte ? pte->name : "";
    ps->kind = SymbolKind::Parameter;
    ps->storage = Storage::Param;
    ps->type = t;
    ps->line = (pte && pte->nameLine) ? pte->nameLine : (at ? at->line : 0);
    ps->column = (pte && pte->nameLine) ? pte->nameColumn : (at ? at->column : 0);
    return ps;
}

void SemanticAnalyzer::functionDefinition(const ASTNodePtr &n, DeclCtx ctx) {
    if (!n->typeExpr) return;
    if (ctx == DeclCtx::Global && !n->typeExpr->className.empty()) {
        outOfClassDefinition(n);
        return;
    }
    SymbolPtr sym = functionSignature(n, ctx, true);
    if (!sym) return;
    if (sym->isDefined) {
        error(lineOf(*n->typeExpr, n.get()), colOf(*n->typeExpr, n.get()),
              "redefinition of function '" + describeSignature(sym) + "' (previously defined at line " +
                  displayLine(sym->declNode ? sym->declNode->line : sym->line) + ")",
              "redefinition");
        return;
    }
    sym->isDefined = true;
    sym->declNode = n.get();
    functionBody(n, sym, nullptr);
}

void SemanticAnalyzer::outOfClassDefinition(const ASTNodePtr &n) {
    const ASTTypeExpr &te = *n->typeExpr;
    int line = lineOf(te, n.get()), col = colOf(te, n.get());
    SymbolPtr tag = st.lookupTag(te.className);
    if (!tag || !tag->record) {
        error(line, col, "use of undeclared class '" + te.className + "' in the definition of '" + te.className +
                             "::" + te.name + "'",
              "unknown-type");
        return;
    }
    RecordInfo *rec = tag->record.get();
    Resolved r = resolveType(te, n.get(), false);
    if (!isFunction(r.type)) return;
    if (te.isVirtual)
        error(line, col, "'virtual' is only allowed on the declaration inside the class, not on '" + te.className + "::" +
                             te.name + "'",
              "virtual");
    SymbolPtr match;
    auto it = rec->members.find(te.name);
    if (it != rec->members.end()) {
        for (const auto &c : it->second) {
            if (c->kind == SymbolKind::Function && sameParameterLists(c->type, r.type) &&
                sameType(c->type->ret, r.type->ret, true)) {
                match = c;
            }
        }
    }
    if (!match) {
        error(line, col, "out-of-line definition of '" + te.className + "::" + te.name + "' with type " + q(r.type) +
                             " does not match any declaration in " + recordKindName(rec->kind) + " '" + rec->tag + "'",
              "no-matching-declaration");
        return;
    }
    if (match->isDefined) {
        error(line, col, "redefinition of '" + te.className + "::" + describeSignature(match) +
                             "' (previously defined at line " + displayLine(match->declNode ? match->declNode->line : match->line) + ")",
              "redefinition");
        return;
    }
    match->isDefined = true;
    match->declNode = n.get();
    n->symbol = match;
    n->semType = match->type;
    functionBody(n, match, rec);
}

void SemanticAnalyzer::functionBody(const ASTNodePtr &n, const SymbolPtr &fnSym, RecordInfo *cls) {
    if (cls) st.reenterScope(cls->scopeId);
    std::string label = fnSym->name + "()";
    int sid = st.enterScope(ScopeKind::Function, label, nullptr, fnSym.get());
    fnSym->bodyScopeId = sid;

    const TypePtr &ft = fnSym->type;
    if (!isVoid(ft->ret) && !isError(ft->ret) && !isComplete(ft->ret) && !isReference(ft->ret)) {
        error(fnSym->line, fnSym->column, "function '" + fnSym->name + "' has incomplete return type " + q(ft->ret),
              "incomplete-type");
    }
    std::vector<ASTNodePtr> paramNodes;
    for (const auto &c : n->children) {
        if (c->kind == ASTKind::ParamDecl) paramNodes.push_back(c);
    }
    size_t named = 0;
    fnSym->params.clear();
    for (size_t i = 0; i < ft->params.size(); ++i) {
        ASTTypeExprPtr pte = i < n->typeExpr->params.size() ? n->typeExpr->params[i] : nullptr;
        SymbolPtr ps = makeParamSymbol(pte, ft->params[i], n.get());
        if (!isError(ps->type) && !isComplete(ps->type) && !isReference(ps->type)) {
            error(ps->line, ps->column, "parameter '" + ps->name + "' has incomplete type " + q(ps->type),
                  "incomplete-type");
        }
        if (!ps->name.empty()) {
            if (!st.lookupLocal(ps->name).empty()) {
                error(ps->line, ps->column, "redefinition of parameter '" + ps->name + "'", "redeclaration");
                st.declareHidden(sid, ps);
            } else {
                st.declare(ps);
            }
            if (named < paramNodes.size()) {
                paramNodes[named]->symbol = ps;
                paramNodes[named]->semType = ps->type;
                ++named;
            }
        } else {
            ps->uniqueName = "param" + std::to_string(i) + "." + fnSym->uniqueName;
            st.declareHidden(sid, ps);
        }
        fnSym->params.push_back(ps);
    }

    FunctionCtx c;
    c.fn = fnSym.get();
    c.name = fnSym->name;
    c.ret = ft->ret;
    c.cls = cls;
    c.isStaticMethod = cls && fnSym->isStatic;
    c.isConstructorLike = fnSym->isConstructor;
    ASTNodePtr body = n->children.empty() ? nullptr : n->children.back();
    if (body && body->kind == ASTKind::CompoundStmt) {
        collectLabels(body, c);
        for (auto &[name, node] : c.labels) {
            auto ls = std::make_shared<Symbol>();
            ls->name = name;
            ls->kind = SymbolKind::Label;
            ls->line = node->line;
            ls->column = node->column;
            ls->uniqueName = fnSym->uniqueName + "." + name;
            ls->declNode = node;
            st.declareHidden(sid, ls);
            const_cast<ASTNode *>(node)->symbol = ls;
        }
        fns.push_back(c);
        int errorsBefore = errors;
        blockItems(body); /* the body block shares the parameters' scope, as in C */
        FunctionCtx done = fns.back();
        fns.pop_back();
        bool needsValue = !isVoid(ft->ret) && !isError(ft->ret) && !c.isConstructorLike &&
                          !(fnSym->name == "main" && !fnSym->isMethod);
        if (errors == errorsBefore) flowChecks(body, fnSym.get(), needsValue && done.sawValueReturn); /* not on broken code */
        if (needsValue && !done.sawValueReturn) {
            warning(fnSym->line, fnSym->column,
                    "non-void function '" + fnSym->name + "' has no return statement (declared to return " +
                        q(ft->ret) + ")",
                    "missing-return");
        }
    }
    st.exitScope();
    if (cls) st.exitScope();
}

/* enum Color { Red, Green = 5, Blue };  (D42, C++ rules) -- the
   enumerators are constants of the enclosing scope with the enum's type;
   a value is the previous one plus one (the first is 0) or an integer
   constant expression, and must fit the underlying int */
void SemanticAnalyzer::enumDefinition(const ASTNodePtr &n) {
    const std::string &tag = n->label;
    int scopeId = declScopeForTags();
    auto &tags = st.scope(scopeId).tags;
    std::shared_ptr<EnumInfo> info;
    auto found = tags.find(tag);
    if (found != tags.end()) {
        const SymbolPtr &prev = found->second;
        if (!prev->enumInfo) {
            error(n.get(), "'" + tag + "' redeclared as a different kind of tag (previously a " +
                               recordKindName(prev->record->kind) + " at line " + displayLine(prev->line) + ")",
                  "redefinition");
            return;
        }
        error(n.get(), "redefinition of 'enum " + tag + "' (previous definition at line " + displayLine(prev->line) + ")",
              "redefinition");
        return;
    }
    info = std::make_shared<EnumInfo>();
    info->tag = tag;
    info->declLine = n->line;
    auto ts = std::make_shared<Symbol>();
    ts->name = tag;
    ts->kind = SymbolKind::Tag;
    ts->enumInfo = info;
    ts->line = n->line;
    ts->column = n->column;
    ts->declNode = n.get();
    st.declareTagIn(scopeId, ts);
    n->symbol = ts;
    TypePtr t = enumType(info);
    n->semType = t;
    long long next = 0;
    for (const auto &e : n->children) {
        long long v = next;
        if (!e->children.empty()) {
            TypePtr vt = value(e->children[0]);
            if (!isError(vt)) {
                if (isIntegral(vt) && e->children[0]->hasConstValue) {
                    v = e->children[0]->constValue;
                } else {
                    error(e->children[0].get(),
                          "value of enumerator '" + e->label + "' is not an integer constant expression", "enum");
                }
            }
        }
        if (!fitsInType(v, basicType(TypeKind::LongLong), intType())) {
            error(e.get(), "value " + std::to_string(v) + " of enumerator '" + e->label +
                               "' does not fit the enum's underlying type 'int'",
                  "enum");
            v = wrapToType(v, intType());
        }
        auto &names = st.scope(scopeId).names;
        auto prev = names.find(e->label);
        if (prev != names.end() && !prev->second.empty()) {
            error(e.get(), "redefinition of '" + e->label + "' (previously declared as " + symbolWhat(prev->second.front()) +
                               " at line " + displayLine(prev->second.front()->line) + ")",
                  "redeclaration");
        } else {
            auto s = std::make_shared<Symbol>();
            s->name = e->label;
            s->uniqueName = e->label;
            s->kind = SymbolKind::EnumConstant;
            s->type = t;
            s->isConstant = true;
            s->constValue = v;
            s->line = e->line;
            s->column = e->column;
            s->declNode = e.get();
            st.declareIn(scopeId, s);
            e->symbol = s;
        }
        e->semType = t;
        e->hasConstValue = true;
        e->constValue = v;
        info->enumerators.push_back({e->label, v});
        next = v + 1;
    }
    info->complete = true;
}

void SemanticAnalyzer::recordDefinition(const ASTNodePtr &n) {
    RecordKind kind = n->kind == ASTKind::ClassDecl   ? RecordKind::Class
                      : n->kind == ASTKind::UnionDecl ? RecordKind::Union
                                                      : RecordKind::Struct;
    std::string tag = tagFromLabel(n->label);
    int scopeId = declScopeForTags();
    auto &tags = st.scope(scopeId).tags;
    std::shared_ptr<RecordInfo> rec;
    auto found = tags.find(tag);
    if (found != tags.end()) {
        const SymbolPtr &prev = found->second;
        if (!prev->record) {
            error(n.get(), "'" + tag + "' redeclared as a different kind of tag (previously an enum at line " +
                               displayLine(prev->line) + ")",
                  "redefinition");
            return;
        }
        if ((kind == RecordKind::Union) != (prev->record->kind == RecordKind::Union)) {
            error(n.get(), "'" + tag + "' redeclared as a different kind of tag (previously a " +
                               recordKindName(prev->record->kind) + " at line " + displayLine(prev->line) + ")",
                  "redefinition");
            return;
        }
        if (prev->record->complete) {
            error(n.get(), "redefinition of '" + recordKindName(prev->record->kind) + " " + tag +
                               "' (previous definition at line " + displayLine(prev->record->declLine) + ")",
                  "redefinition");
            return;
        }
        rec = prev->record;
        n->symbol = prev;
    } else {
        rec = std::make_shared<RecordInfo>();
        rec->tag = tag;
        auto ts = std::make_shared<Symbol>();
        ts->name = tag;
        ts->kind = SymbolKind::Tag;
        ts->record = rec;
        ts->line = n->line;
        ts->column = n->column;
        ts->declNode = n.get();
        st.declareTagIn(scopeId, ts);
        n->symbol = ts;
    }
    rec->kind = kind;
    rec->declLine = n->line;
    n->semType = recordType(rec);

    for (const auto &[accessText, baseName] : n->bases) {
        SymbolPtr b = st.lookupTag(baseName);
        if (!b || !b->record) {
            error(n.get(), "base class '" + baseName + "' is not a declared class or struct", "inheritance");
        } else if (b->record == rec) {
            error(n.get(), "'" + tag + "' cannot inherit from itself", "inheritance");
        } else if (!b->record->complete) {
            error(n.get(), "base class '" + recordKindName(b->record->kind) + " " + baseName + "' has incomplete type",
                  "inheritance");
        } else if (!rec->bases.empty()) {
            /* single inheritance only (D35): one direct base; chains B : A, C : B are fine */
            error(n.get(), "'" + tag + "' cannot have a second base class '" + baseName +
                               "': only single inheritance is supported", "inheritance");
        } else {
            Access a = accessText == "public"      ? Access::Public
                       : accessText == "protected" ? Access::Protected
                       : accessText == "private"   ? Access::Private
                       : (kind == RecordKind::Class ? Access::Private : Access::Public);
            rec->bases.push_back({b->record, a});
        }
    }

    rec->scopeId = st.enterScope(ScopeKind::Record, recordKindName(kind) + " " + tag, rec.get());
    Access defaultAccess = kind == RecordKind::Class ? Access::Private : Access::Public;
    std::vector<std::pair<ASTNodePtr, SymbolPtr>> bodies, friendBodies;
    /* promoted member -> (the unnamed member holding it, the inner field) */
    struct Promotion {
        SymbolPtr promoted, holder, inner;
    };
    std::vector<Promotion> promotions;

    /* `struct { int i; float f; };` as a member (C11): an unnamed field
       of that type, whose own fields are usable as fields of this record */
    auto anonymousMember = [&](const ASTNodePtr &m, Access a) {
        RecordInfo *inner = m->semType && m->semType->record ? m->semType->record.get() : nullptr;
        if (!inner) return;
        auto holder = std::make_shared<Symbol>();
        holder->kind = SymbolKind::Field;
        holder->type = m->semType;
        holder->storage = Storage::Member;
        holder->ownerRecord = rec.get();
        holder->access = a;
        holder->line = m->line;
        holder->column = m->column;
        holder->declNode = m.get();
        rec->fields.push_back(holder);
        st.declareHidden(rec->scopeId, holder); /* listed, but has no name to look up */
        holder->uniqueName = tag + "::" + inner->tag;
        std::vector<SymbolPtr> innerFields;
        for (const auto &f : inner->fields) {
            if (f->storage == Storage::Member && !f->name.empty()) innerFields.push_back(f);
        }
        for (const auto &f : inner->promoted) innerFields.push_back(f); /* nested unnamed members */
        for (const auto &f : innerFields) {
            auto existing = rec->members.find(f->name);
            if (existing != rec->members.end()) {
                error(f->line, f->column, "duplicate member '" + f->name + "' in " + recordKindName(kind) + " '" + tag +
                                              "' (previous declaration at line " +
                                              displayLine(existing->second.front()->line) + ")",
                      "duplicate-member");
                continue;
            }
            auto p = std::make_shared<Symbol>(*f);
            p->ownerRecord = rec.get();
            p->access = a;
            rec->members[f->name] = {p};
            rec->promoted.push_back(p);
            promotions.push_back({p, holder, f});
        }
    };

    std::function<void(const ASTNodePtr &, Access, bool)> memberItem = [&](const ASTNodePtr &m, Access a, bool bare) {
        if (!m) return;
        if (!m->access.empty()) {
            a = m->access == "public" ? Access::Public : m->access == "protected" ? Access::Protected : Access::Private;
        }
        if (kind == RecordKind::Union &&
            (m->kind == ASTKind::FunctionDecl || m->kind == ASTKind::FunctionDef || m->kind == ASTKind::ConstructorDef ||
             m->kind == ASTKind::FriendDecl)) {
            /* plain unions (D42): data members only */
            error(m.get(), "union '" + tag + "' cannot have member functions, constructors or friends: unions hold data only",
                  "union");
            return;
        }
        switch (m->kind) {
            case ASTKind::DeclGroup:
                for (const auto &c : m->children) memberItem(c, a, false);
                break;
            case ASTKind::VarDecl: {
                const ASTTypeExpr &te = *m->typeExpr;
                int line = lineOf(te, m.get()), col = colOf(te, m.get());
                auto existing = rec->members.find(te.name);
                if (existing != rec->members.end()) {
                    error(line, col, "duplicate member '" + te.name + "' in " + recordKindName(kind) + " '" + tag +
                                         "' (previous declaration at line " + displayLine(existing->second.front()->line) + ")",
                          "duplicate-member");
                    return;
                }
                if (te.isAuto && te.specParts.empty()) {
                    error(line, col, "'auto' is not allowed in a member declaration", "auto");
                    return;
                }
                SymbolPtr f = variable(m, DeclCtx::Member);
                if (!f) return;
                if (kind == RecordKind::Union) {
                    std::string why = f->storage == Storage::Static ? "cannot be static"
                                      : isReference(f->type)       ? "cannot be a reference"
                                      : hasConstructor(f->type)    ? "has a class type with a constructor"
                                                                   : "";
                    if (!why.empty()) {
                        error(line, col, "member '" + te.name + "' of union '" + tag + "' " + why, "union");
                        return;
                    }
                }
                f->ownerRecord = rec.get();
                f->access = a;
                rec->fields.push_back(f);
                rec->members[te.name] = {f};
                st.declareIn(rec->scopeId, f);
                break;
            }
            case ASTKind::FriendDecl: /* `friend class Cat;` */
                rec->friendClasses.insert(m->label);
                break;
            case ASTKind::FunctionDecl: {
                if (m->typeExpr && m->typeExpr->isFriend) {
                    friendFunction(m, rec.get(), false, friendBodies);
                    break;
                }
                SymbolPtr s = functionSignature(m, DeclCtx::Member, false);
                if (s) s->access = a;
                break;
            }
            case ASTKind::FunctionDef: {
                if (m->typeExpr && m->typeExpr->isFriend) {
                    friendFunction(m, rec.get(), true, friendBodies);
                    break;
                }
                SymbolPtr s = functionSignature(m, DeclCtx::Member, true);
                if (!s) break;
                s->access = a;
                if (s->isDefined) {
                    error(lineOf(*m->typeExpr, m.get()), colOf(*m->typeExpr, m.get()),
                          "redefinition of member function '" + describeSignature(s) + "'", "redefinition");
                    break;
                }
                s->isDefined = true;
                s->declNode = m.get();
                bodies.push_back({m, s});
                break;
            }
            case ASTKind::ConstructorDef: {
                std::string name = tagFromLabel(m->label);
                if (name != tag) {
                    error(m.get(), "member function '" + name + "' must declare a return type (only constructors, named '" +
                                       tag + "', may omit it)",
                          "missing-return-type");
                    return;
                }
                auto s = std::make_shared<Symbol>();
                s->name = tag;
                s->kind = SymbolKind::Function;
                std::vector<TypePtr> params = m->typeExpr ? resolveParams(*m->typeExpr, m.get()) : std::vector<TypePtr>{};
                if (!params.empty() || (m->typeExpr && m->typeExpr->isVariadic)) {
                    /* only the default constructor exists in this language (D35) */
                    error(m.get(), "constructor '" + tag + "' cannot take parameters: only default constructors '" + tag +
                                       "()' are supported",
                          "constructor");
                    return;
                }
                s->type = functionType(voidType(), {}, false);
                s->isMethod = true;
                bool hasBody = !m->children.empty() && m->children.back()->kind == ASTKind::CompoundStmt;
                s->isConstructor = true;
                s->isDefined = hasBody; /* else `Dog();`, defined later as Dog::Dog() {...} */
                s->ownerRecord = rec.get();
                s->access = a;
                s->line = m->line;
                s->column = m->column;
                s->declNode = m.get();
                s->mangledName = mangle(s->name, s->type->params, s->type->variadic, tag);
                s->uniqueName = s->mangledName;
                if (!rec->constructors.empty()) {
                    error(m.get(), "constructor '" + describeSignature(s) + "' is already declared at line " +
                                       displayLine(rec->constructors.front()->line),
                          "redefinition");
                    return;
                }
                rec->constructors.push_back(s);
                st.declareHidden(rec->scopeId, s);
                m->symbol = s;
                if (!m->typeExpr) m->typeExpr = std::make_shared<ASTTypeExpr>();
                if (hasBody) bodies.push_back({m, s});
                break;
            }
            case ASTKind::StructDecl:
            case ASTKind::ClassDecl:
            case ASTKind::UnionDecl:
                if (isCxxClass(m) || (kind == RecordKind::Class && !isAnonymousTag(tagFromLabel(m->label)))) {
                    /* a class inside a class (D35); C's nested data structs and unnamed members stay */
                    error(m.get(), "nested " + std::string(m->kind == ASTKind::ClassDecl ? "class" : m->kind == ASTKind::UnionDecl ? "union" : "struct") + " '" +
                                       tagFromLabel(m->label) + "' is not supported: define it outside '" + tag + "'",
                          "nested-class");
                    break;
                }
                if (bare && m->kind == ASTKind::UnionDecl && isAnonymousTag(tagFromLabel(m->label))) {
                    /* plain unions only (D42): `union { int i; float f; };` as a member */
                    error(m.get(), "anonymous unions are not supported: give the union member a name", "anonymous-union");
                    break;
                }
                recordDefinition(m);
                if (bare) anonymousMember(m, a);
                break;
            case ASTKind::EnumDecl:
                error(m.get(), "an enum cannot be defined inside '" + tag + "': define it at file scope or in a function",
                      "nested-enum");
                enumDefinition(m); /* still defined (in the enclosing scope), so its uses report nothing more */
                break;
            case ASTKind::TypedefDecl:
                typedefDecl(m);
                break;
            default:
                break;
        }
    };
    for (const auto &m : n->children) memberItem(m, defaultAccess, true);
    st.exitScope();
    virtualFunctions(rec.get(), n);
    layoutRecord(*rec);
    /* a promoted member sits at its holder's offset plus its own */
    for (auto &p : promotions) p.promoted->offset = p.holder->offset + p.inner->offset;
    rec->complete = true;

    /* member function bodies see the complete class (C++ rule) */
    for (auto &[node, sym] : bodies) functionBody(node, sym, rec.get());
    for (auto &[node, sym] : friendBodies) functionBody(node, sym, nullptr); /* not members: no `this` */
}

/* ---------------- virtual functions (D44) ---------------- */

/* same name and parameters: one overrides the other */
static bool sameSlot(const Symbol *a, const Symbol *b) {
    return a->name == b->name && sameParameterLists(a->type, b->type);
}

/* once a class's members are known (before its layout): which member
   functions are virtual, the slots of its table and the function each
   slot calls, and whether the class is abstract. A function that matches
   a virtual function of the base overrides it, with or without the
   keyword (C++); a new virtual function gets the next slot. */
void SemanticAnalyzer::virtualFunctions(RecordInfo *rec, const ASTNodePtr &n) {
    std::vector<Symbol *> methods; /* declaration order */
    std::function<void(const ASTNodePtr &)> walk = [&](const ASTNodePtr &m) {
        if (!m) return;
        if (m->kind == ASTKind::DeclGroup) {
            for (const auto &c : m->children) walk(c);
            return;
        }
        if ((m->kind == ASTKind::FunctionDecl || m->kind == ASTKind::FunctionDef) && m->symbol &&
            m->symbol->ownerRecord == rec && std::find(methods.begin(), methods.end(), m->symbol.get()) == methods.end())
            methods.push_back(m->symbol.get());
    };
    for (const auto &m : n->children) walk(m);
    RecordInfo *base = !rec->bases.empty() ? rec->bases[0].record.get() : nullptr;
    bool inherited = base && base->polymorphic;
    if (inherited) rec->vtable = base->vtable;
    for (Symbol *m : methods) {
        if (m->isStatic) continue;
        for (size_t k = 0; k < rec->vtable.size(); ++k) {
            if (!sameSlot(rec->vtable[k], m)) continue;
            if (!sameType(m->type->ret, rec->vtable[k]->type->ret, true))
                error(m->line, m->column, "'" + rec->tag + "::" + m->name + "' overrides a virtual function but its return " +
                                              "type differs (" + q(m->type->ret) + " vs " + q(rec->vtable[k]->type->ret) + ")",
                      "virtual");
            m->isVirtual = true; /* overriding makes it virtual, with or without the keyword */
            m->vtableIndex = static_cast<int>(k);
            rec->vtable[k] = m;
            break;
        }
        if (m->isVirtual && m->vtableIndex < 0) {
            m->vtableIndex = static_cast<int>(rec->vtable.size());
            rec->vtable.push_back(m);
        }
    }
    rec->polymorphic = !rec->vtable.empty();
    rec->ownVptr = rec->polymorphic && !inherited;
    rec->abstract = std::any_of(rec->vtable.begin(), rec->vtable.end(), [](const Symbol *f) { return f->isPure; });
}

bool SemanticAnalyzer::isAbstractType(const TypePtr &t) const {
    TypePtr e = t;
    while (e && isArray(e)) e = e->elem;
    return e && isRecord(e) && e->record && e->record->abstract;
}

/* no object of an abstract class: only pointers and references to one */
void SemanticAnalyzer::checkNotAbstract(const TypePtr &t, int line, int col, const std::string &what) {
    if (!isAbstractType(t)) return;
    TypePtr e = t;
    while (isArray(e)) e = e->elem;
    std::string pure;
    for (const Symbol *f : e->record->vtable)
        if (f->isPure) {
            pure = f->name + "(";
            for (size_t i = 0; i < f->type->params.size(); ++i)
                pure += (i ? ", " : "") + typeToString(f->type->params[i]);
            pure += ")";
            break;
        }
    error(line, col, what + " has abstract type " + q(e) + " (pure virtual function '" + pure + "' is not overridden)",
          "abstract");
}

/* `friend int peek(const Shape &);` inside a class: an ordinary function
   at file scope that may use the class's private and protected members */
void SemanticAnalyzer::friendFunction(const ASTNodePtr &m, RecordInfo *rec, bool isDefinition,
                                      std::vector<std::pair<ASTNodePtr, SymbolPtr>> &bodies) {
    st.reenterScope(0);
    SymbolPtr s = functionSignature(m, DeclCtx::Global, isDefinition);
    st.exitScope();
    if (!s) return;
    rec->friendFunctions.insert(s.get());
    if (!isDefinition) return;
    if (s->isDefined) {
        error(m.get(), "redefinition of '" + describeSignature(s) + "'", "redefinition");
        return;
    }
    s->isDefined = true;
    s->declNode = m.get();
    bodies.push_back({m, s});
}

} // namespace sem
