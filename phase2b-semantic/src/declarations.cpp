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
       can never be linked -- there is no separate compilation here; the
       same holds for an `extern` object that is never defined */
    for (const auto &s : st.allSymbols()) {
        if (s->kind == SymbolKind::Variable && s->storage == Storage::Global && !s->isDefined && s->evaluatedUses > 0) {
            warning(s->line, s->column, "variable '" + s->name + "' is declared 'extern' and used but never defined",
                    "undefined-variable");
        }
        if (s->kind == SymbolKind::Function && !s->isDefined && s->useCount > 0 &&
            !s->isConstructor && !s->isDestructor) {
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
    /* `struct Dog` may name a class and `class Point` a struct (C++) */
    RecordKind want = kindPart == "CLASS" ? RecordKind::Class : RecordKind::Struct;
    if (sym) return recordType(sym->record);
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
            base = recordType(tag->record);
        } else {
            error(line, col, "unknown type name '" + te.typedefName + "'", "unknown-type");
            base = errorType();
        }
    } else {
        std::map<std::string, int> n;
        for (const auto &p : te.specParts) n[p]++;
        for (const char *tagKw : {"STRUCT", "CLASS"}) {
            if (n.count(tagKw)) {
                if (te.specParts.size() != 1) {
                    error(line, col, "cannot combine a struct/class type with other type specifiers",
                          "invalid-specifiers");
                }
                return qualified(resolveTag(te, tagKw, at), te.isConst, te.isVolatile);
            }
        }
        if (te.specParts.empty()) {
            if (te.isAuto) {
                isAuto = true;
                return nullptr;
            }
            warning(line, col, "type specifier missing, defaults to 'int'", "implicit-int");
            return qualified(intType(), te.isConst, te.isVolatile);
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
                bad = others != 1 + longs || longs > 1;
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
    if (base && isArray(base) && (te.isConst || te.isVolatile)) {
        std::function<TypePtr(const TypePtr &)> elements = [&](const TypePtr &a) -> TypePtr {
            return isArray(a) ? arrayOf(elements(a->elem), a->arraySize) : qualified(a, te.isConst, te.isVolatile);
        };
        return elements(base);
    }
    return qualified(base, te.isConst, te.isVolatile);
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
            if (op == 'c' || op == 'v') {
                t = qualified(t, op == 'c', op == 'v');
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

void SemanticAnalyzer::declaration(const ASTNodePtr &n, DeclCtx ctx) {
    if (!n) return;
    switch (n->kind) {
        case ASTKind::VarDecl: variable(n, ctx); break;
        case ASTKind::FunctionDecl: functionSignature(n, ctx, false); break;
        case ASTKind::FunctionDef: functionDefinition(n, ctx); break;
        case ASTKind::TypedefDecl: typedefDecl(n); break;
        case ASTKind::DeclGroup:
            /* `struct { ... } p;`: the type, then what it declares */
            for (const auto &c : n->children) {
                if (c->kind == ASTKind::StructDecl || c->kind == ASTKind::ClassDecl)
                    recordDefinition(c);
                else
                    declaration(c, ctx);
            }
            break;
        case ASTKind::StructDecl:
        case ASTKind::ClassDecl:
            recordDefinition(n);
            /* `struct { int x; };`: a type nobody can name (gcc says the same) */
            if (isAnonymousTag(tagFromLabel(n->label)))
                warning(n.get(), "unnamed struct that defines no instances", "anonymous");
            break;
        case ASTKind::ConstructorDef:
        case ASTKind::DestructorDef: outOfClassSpecial(n); break; /* `Dog::Dog(...) {}` */
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
                t = qualified(decay(it), te.isConst, te.isVolatile);
            }
        }
    }

    Storage storage = ctx == DeclCtx::Global ? Storage::Global
                      : ctx == DeclCtx::Member ? (te.isStatic ? Storage::Static : Storage::Member)
                                               : (te.isStatic ? Storage::Static : Storage::Local);
    std::string what = ctx == DeclCtx::Member ? "field" : "variable";

    /* storage classes (C11 6.7.1) */
    bool isExtern = te.isExtern && ctx != DeclCtx::Member;
    if (te.storageClasses > 1)
        error(line, col, "multiple storage classes in the declaration of '" + name + "'", "storage-class");
    if (te.isExtern && ctx == DeclCtx::Member)
        error(line, col, "'extern' is not allowed on a member ('" + name + "')", "storage-class");
    if (te.isRegister && ctx == DeclCtx::Global)
        error(line, col, "'register' is not allowed at file scope (variable '" + name + "')", "storage-class");
    if (isExtern && init) {
        if (ctx == DeclCtx::Local) {
            error(line, col, "'" + name + "' has both 'extern' and an initializer (a block-scope 'extern' only refers "
                                          "to an object defined elsewhere)",
                  "storage-class");
            init = nullptr;
        } else {
            warning(line, col, "'" + name + "' initialized and declared 'extern'", "storage-class");
        }
    }
    bool declarationOnly = isExtern && !init; /* `extern int a[];` may stay incomplete */

    /* `int a[] = {1, 2, 3};` / `char s[] = "abc";`: the size comes from the initializer */
    if (isArray(t) && t->arraySize < 0) {
        if (init && init->kind == ASTKind::InitializerList) {
            long long count = 0, pos = 0;
            for (const auto &c : init->children) {
                if (c->kind == ASTKind::DesignatedInit && c->label[0] == '[') pos = std::max(0LL, designatorIndex(c));
                count = std::max(count, ++pos);
            }
            if (count == 0) {
                error(line, col, "zero-size array '" + name + "' (an empty initializer gives the array no elements)",
                      "array-size");
            }
            bool flat = isArray(t->elem) && std::none_of(init->children.begin(), init->children.end(),
                                                         [](const ASTNodePtr &c) { return c->kind == ASTKind::InitializerList; });
            if (flat) {
                long long inner = std::max(1LL, sizeOf(t->elem) / std::max(1LL, sizeOf([&] {
                                                     TypePtr e = t->elem;
                                                     while (isArray(e)) e = e->elem;
                                                     return e;
                                                 }())));
                count = (count + inner - 1) / inner;
            }
            t = qualified(arrayOf(t->elem, std::max(1LL, count)), t->isConst, t->isVolatile);
        } else if (init && init->kind == ASTKind::StringLiteral && t->elem && t->elem->kind == TypeKind::Char) {
            TypePtr lit = expr(init);
            t = arrayOf(t->elem, lit->arraySize);
        } else if (!declarationOnly && (ctx != DeclCtx::Member || !init)) {
            error(line, col, "definition of " + what + " '" + name +
                                 "' with array type needs an explicit size or an initializer",
                  "array-size");
            t = errorType();
        }
    }

    if (isVoid(t)) {
        error(line, col, what + " '" + name + "' has incomplete type 'void'", "incomplete-type");
        t = errorType();
    } else if (!isError(t) && !isComplete(t) && !isReference(t) && !declarationOnly) {
        error(line, col, what + " '" + name + "' has incomplete type " + q(t), "incomplete-type");
        t = errorType();
    }
    if (isReference(t) && !init && ctx != DeclCtx::Member) {
        error(line, col, "declaration of reference variable '" + name + "' requires an initializer", "reference");
    }

    /* external linkage (C11 6.2.2): `extern int x;` and the definition
       `int x = 1;` are one object, so they share one symbol -- whose type
       becomes the composite of the two (`extern int a[]; int a[5];` makes
       a an int[5], Papaspyrou's composite) -- and a block-scope `extern`
       names that file-scope object */
    if ((ctx == DeclCtx::Global || isExtern) && !isError(t)) {
        SymbolPtr prev;
        for (const auto &c : st.scope(0).names[name])
            if (c->kind == SymbolKind::Variable) prev = c;
        std::vector<SymbolPtr> here = ctx == DeclCtx::Local ? st.lookupLocal(name) : std::vector<SymbolPtr>{};
        bool localClash = !here.empty() && here.front() != prev;
        if (!localClash && prev && (!prev->isDefined || declarationOnly)) {
            TypePtr composite;
            if (sameType(prev->type, t, true)) {
                composite = prev->type;
            } else if (isArray(prev->type) && isArray(t) && sameType(prev->type->elem, t->elem, true) &&
                       (prev->type->arraySize < 0 || t->arraySize < 0)) {
                composite = prev->type->arraySize < 0 ? t : prev->type;
            }
            if (!composite) {
                error(line, col, "conflicting types for '" + name + "': " + q(t) + " does not match the previous "
                                     "declaration " + q(prev->type) + " at line " + displayLine(prev->line),
                      "conflicting-types");
                return nullptr;
            }
            prev->type = composite;
            if (!declarationOnly) {
                prev->isDefined = true;
                prev->declNode = n.get();
                prev->line = line;
                prev->column = col;
            }
            if (ctx == DeclCtx::Local && here.empty()) st.current().names[name].push_back(prev);
            n->symbol = prev;
            n->semType = prev->type;
            if (init) {
                prev->hasInitializer = true;
                checkInitializer(prev->type, init, true, "variable '" + name + "'");
            }
            return prev;
        }
        if (!localClash && !prev && ctx == DeclCtx::Local) {
            /* `extern int g;` in a block before any file-scope `g`: declares it there */
            auto g = std::make_shared<Symbol>();
            g->name = name;
            g->kind = SymbolKind::Variable;
            g->type = t;
            g->storage = Storage::Global;
            g->line = line;
            g->column = col;
            g->declNode = n.get();
            st.declareIn(0, g);
            st.current().names[name].push_back(g);
            n->symbol = g;
            n->semType = t;
            return g;
        }
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
    sym->isRegister = te.isRegister;
    sym->isDefined = !declarationOnly; /* `extern int x;` declares; any other object declaration defines */
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

void SemanticAnalyzer::checkInitializer(const TypePtr &target, const ASTNodePtr &init, bool requireConstant,
                                        const std::string &what) {
    if (!init) return;
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
            bool flat = isArray(elem) && std::none_of(items.begin(), items.end(), [](const ASTNodePtr &c) {
                            return c->kind == ASTKind::InitializerList || c->kind == ASTKind::StringLiteral;
                        });
            if (flat) { /* brace elision: `int m[2][2] = {1, 2, 3, 4};` */
                TypePtr leaf = elem;
                long long total = target->arraySize;
                while (isArray(leaf)) {
                    total = total < 0 ? -1 : total * leaf->arraySize;
                    leaf = leaf->elem;
                }
                if (total >= 0 && static_cast<long long>(items.size()) > total) {
                    error(items[total].get(), "excess elements in array initializer (" + what + " holds " +
                                                  std::to_string(total) + " elements)",
                          "initializer");
                }
                for (const auto &c : items) checkInitializer(leaf, c, requireConstant, what);
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
            std::vector<SymbolPtr> fields;
            for (const auto &f : rec->fields) {
                if (f->storage == Storage::Member) fields.push_back(f);
            }
            size_t limit = fields.size();
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
                if (pos >= limit) {
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
    if (RecordInfo *rec = isRecord(target) ? target->record.get() : nullptr) {
        /* `Dog d = 4;`: a constructor taking one argument converts */
        RecordInfo *from = isRecord(decay(it)) ? decay(it)->record.get() : nullptr;
        if (!(from && (from == rec || isDerivedFrom(from, rec))) && !rec->constructors.empty() &&
            anyViable(rec->constructors, {init})) {
            init->converter = construct(rec, {init}, init.get());
            return;
        }
    }
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
    if (r.type && !r.type->isConst && !r.type->isVolatile) {
        if (r.type->kind == TypeKind::Record && r.type->record && isAnonymousTag(r.type->record->tag) &&
            r.type->record->typedefName.empty())
            r.type->record->typedefName = te.name;
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
    c.isConstructorLike = fnSym->isConstructor || fnSym->isDestructor;
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
        blockItems(body); /* the body block shares the parameters' scope, as in C */
        FunctionCtx done = fns.back();
        fns.pop_back();
        if (!isVoid(ft->ret) && !isError(ft->ret) && !done.sawValueReturn && !c.isConstructorLike &&
            !(fnSym->name == "main" && !fnSym->isMethod)) {
            warning(fnSym->line, fnSym->column,
                    "non-void function '" + fnSym->name + "' has no return statement (declared to return " +
                        q(ft->ret) + ")",
                    "missing-return");
        }
    }
    st.exitScope();
    if (cls) st.exitScope();
}

void SemanticAnalyzer::recordDefinition(const ASTNodePtr &n) {
    RecordKind kind = n->kind == ASTKind::ClassDecl ? RecordKind::Class : RecordKind::Struct;
    std::string tag = tagFromLabel(n->label);
    int scopeId = declScopeForTags();
    auto &tags = st.scope(scopeId).tags;
    std::shared_ptr<RecordInfo> rec;
    auto found = tags.find(tag);
    if (found != tags.end()) {
        const SymbolPtr &prev = found->second;
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
        } else if (std::any_of(rec->bases.begin(), rec->bases.end(), [&](const BaseClass &x) { return x.record == b->record; })) {
            error(n.get(), "base class '" + baseName + "' specified more than once", "inheritance");
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
    std::vector<std::pair<ASTNodePtr, SymbolPtr>> bodies;
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
                f->ownerRecord = rec.get();
                f->access = a;
                rec->fields.push_back(f);
                rec->members[te.name] = {f};
                st.declareIn(rec->scopeId, f);
                break;
            }
            case ASTKind::FunctionDecl: {
                SymbolPtr s = functionSignature(m, DeclCtx::Member, false);
                if (s) s->access = a;
                break;
            }
            case ASTKind::FunctionDef: {
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
            case ASTKind::ConstructorDef:
            case ASTKind::DestructorDef: {
                bool ctor = m->kind == ASTKind::ConstructorDef;
                std::string name = tagFromLabel(m->label);
                if (name != tag) {
                    if (ctor) {
                        error(m.get(), "member function '" + name + "' must declare a return type (only constructors, named '" +
                                           tag + "', may omit it)",
                              "missing-return-type");
                    } else {
                        error(m.get(), "destructor name '~" + name + "' does not match the " + recordKindName(kind) +
                                           " name '" + tag + "'",
                              "destructor");
                    }
                    return;
                }
                auto s = std::make_shared<Symbol>();
                s->name = ctor ? tag : "~" + tag;
                s->kind = SymbolKind::Function;
                s->type = functionType(voidType(), ctor && m->typeExpr ? resolveParams(*m->typeExpr, m.get())
                                                                       : std::vector<TypePtr>{},
                                       false);
                s->isMethod = true;
                bool hasBody = !m->children.empty() && m->children.back()->kind == ASTKind::CompoundStmt;
                s->isConstructor = ctor;
                s->isDestructor = !ctor;
                s->isDefined = hasBody; /* else `Dog(int n);`, defined as Dog::Dog(int n) {...} */
                s->ownerRecord = rec.get();
                s->access = a;
                s->line = m->line;
                s->column = m->column;
                s->declNode = m.get();
                s->mangledName = mangle(s->name, s->type->params, s->type->variadic, tag);
                s->uniqueName = s->mangledName;
                if (ctor) {
                    for (const auto &other : rec->constructors) {
                        if (sameParameterLists(other->type, s->type)) {
                            error(m.get(), "constructor '" + describeSignature(s) + "' is already declared at line " +
                                               displayLine(other->line),
                                  "redefinition");
                            return;
                        }
                    }
                    rec->constructors.push_back(s);
                } else {
                    if (rec->destructor) {
                        error(m.get(), "destructor '~" + tag + "' is already declared at line " +
                                           displayLine(rec->destructor->line),
                              "redefinition");
                        return;
                    }
                    rec->destructor = s;
                }
                st.declareHidden(rec->scopeId, s);
                m->symbol = s;
                if (!m->typeExpr) m->typeExpr = std::make_shared<ASTTypeExpr>();
                if (hasBody) bodies.push_back({m, s});
                break;
            }
            case ASTKind::StructDecl:
            case ASTKind::ClassDecl:
                recordDefinition(m);
                if (bare && isAnonymousTag(tagFromLabel(m->label))) anonymousMember(m, a);
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
    layoutRecord(*rec);
    /* a promoted member sits at its holder's offset plus its own */
    for (auto &p : promotions) p.promoted->offset = p.holder->offset + p.inner->offset;
    rec->complete = true;

    /* member function bodies see the complete class (C++ rule) */
    for (auto &[node, sym] : bodies) functionBody(node, sym, rec.get());
}

} // namespace sem
