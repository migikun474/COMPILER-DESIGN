/* The C++-style parts of the language: constructors and object
   construction and operator overloading. */
#include <algorithm>
#include <functional>
#include <set>

#include "diagnostics/diagnostics.hpp"
#include "semantic.h"

namespace sem {

static std::string q(const TypePtr &t) { return "'" + typeToString(t) + "'"; }

static std::string tagFromLabel(const std::string &label) {
    size_t p = label.find(" : ");
    return p == std::string::npos ? label : label.substr(0, p);
}

static TypePtr stripRef(const TypePtr &t) { return isReference(t) ? t->elem : t; }

static RecordInfo *recordOf(const TypePtr &t) {
    TypePtr s = stripRef(t);
    return isRecord(s) ? s->record.get() : nullptr;
}

static std::string recordName(const RecordInfo *r) { return recordDisplayName(*r); }

bool SemanticAnalyzer::anyViable(const std::vector<SymbolPtr> &candidates, const std::vector<ASTNodePtr> &args) {
    for (const auto &c : candidates) {
        if (c->kind != SymbolKind::Function || !isFunction(c->type)) continue;
        const TypePtr &ft = c->type;
        if (args.size() < ft->params.size() || (args.size() > ft->params.size() && !ft->variadic)) continue;
        bool ok = true;
        for (size_t i = 0; i < ft->params.size() && ok; ++i) {
            ok = argumentConversion(ft->params[i], args[i]).rank != ConvRank::None;
        }
        if (ok) return true;
    }
    return false;
}

/* ---------------- constructors ---------------- */

/* the only constructor is the default one, `T()` (D35). `T x(other)` with an
   object of the same class is a plain copy of its bytes (there are no copy
   constructors); any other argument is an error. Returns the constructor
   to call, or null when there is none to call. */
SymbolPtr SemanticAnalyzer::construct(RecordInfo *rec, const std::vector<ASTNodePtr> &args, const ASTNode *at) {
    if (!rec) return nullptr;
    if (!rec->complete) {
        error(at, "cannot construct an object of incomplete type '" + recordName(rec) + "'", "incomplete-type");
        return nullptr;
    }
    for (const auto &a : args) {
        if (isError(a->semType)) return nullptr;
    }
    if (args.size() == 1 && recordOf(args[0]->semType) == rec) return nullptr; /* a copy */
    if (!args.empty()) {
        error(at, "'" + recordName(rec) + "' cannot be constructed from " + std::to_string(args.size()) + " argument" +
                      (args.size() == 1 ? "" : "s") + ": only default construction is supported ('" + rec->tag + " x;')",
              "constructor");
        return nullptr;
    }
    if (rec->constructors.empty()) return nullptr;
    SymbolPtr chosen = rec->constructors.front();
    MemberLookup ml;
    ml.symbols = {chosen};
    ml.declaringRecord = rec;
    ml.access = chosen->access;
    checkAccess(ml, rec, rec->tag + "::" + rec->tag + "()", at);
    chosen->useCount++;
    return chosen;
}

/* `Dog d;` / `Dog pack[3];`: a class with constructors must
   have one callable without arguments */
void SemanticAnalyzer::defaultConstruct(const TypePtr &t, const ASTNode *at) {
    TypePtr e = t;
    while (isArray(e)) e = e->elem;
    if (RecordInfo *rec = isRecord(e) ? e->record.get() : nullptr) {
        if (rec->complete && !rec->constructors.empty()) construct(rec, {}, at);
    }
}

/* `T x(args);` */
void SemanticAnalyzer::constructorInit(const TypePtr &target, const ASTNodePtr &init, const std::string &what) {
    const auto &args = init->children;
    for (const auto &a : args) expr(a);
    init->semType = target;
    if (isError(target)) return;
    if (RecordInfo *rec = isRecord(target) ? target->record.get() : nullptr) {
        init->symbol = construct(rec, args, init.get());
        return;
    }
    if (isArray(target)) {
        error(init.get(), "array " + what + " cannot be initialized with a parenthesized argument list", "initializer");
        return;
    }
    if (args.size() != 1) {
        error(init.get(), "a scalar " + what + " is initialized with exactly one value, not " + std::to_string(args.size()),
              "initializer");
        return;
    }
    if (isReference(target)) {
        checkInitializer(target, args[0], false, what);
        return;
    }
    convertible(target, args[0], "type mismatch: cannot initialize " + what + " of type '%T' with a value of type '%F'");
}

/* `T(args)`: a temporary object, or for a non-class type a functional cast */
TypePtr SemanticAnalyzer::constructExpr(const ASTNodePtr &n) {
    TypePtr t = n->typeExpr ? resolveType(*n->typeExpr, n.get(), false).type : errorType();
    if (!t) t = errorType();
    const auto &args = n->children;
    for (const auto &a : args) expr(a);
    if (isError(t)) return errorType();
    if (RecordInfo *rec = isRecord(t) ? t->record.get() : nullptr) {
        n->symbol = construct(rec, args, n.get());
        return t;
    }
    if (args.empty()) {
        if (isVoid(t)) return t;
        if (isIntegral(t)) n->hasConstValue = true, n->constValue = 0; /* `int()` is 0 */
        return unqualified(t);
    }
    if (args.size() > 1) {
        error(n.get(), "functional cast to " + q(t) + " takes exactly one argument, not " + std::to_string(args.size()),
              "invalid-cast");
        return errorType();
    }
    TypePtr from = decay(args[0]->semType);
    if (isError(from)) return errorType();
    std::string why = checkCast(from, t);
    if (!why.empty()) {
        error(n.get(), "invalid functional cast from " + q(from) + " to " + q(t) + ": " + why, "invalid-cast");
        return errorType();
    }
    if (args[0]->hasConstValue && isIntegral(t)) n->hasConstValue = true, n->constValue = args[0]->constValue;
    return unqualified(t);
}

/* `Dog::Dog() { }` after the class */
void SemanticAnalyzer::outOfClassSpecial(const ASTNodePtr &n) {
    const std::string cls = n->typeExpr ? n->typeExpr->className : "";
    std::string name = tagFromLabel(n->label);
    SymbolPtr tag = st.lookupTag(cls);
    if (!tag || !tag->record) {
        error(n.get(), "use of undeclared class '" + cls + "'", "unknown-type");
        return;
    }
    RecordInfo *rec = tag->record.get();
    if (name != rec->tag) {
        error(n.get(), "constructor name '" + name + "' does not match the class name '" + rec->tag + "'", "constructor");
        return;
    }
    if (!resolveParams(*n->typeExpr, n.get()).empty()) {
        error(n.get(), "constructor '" + rec->tag + "' cannot take parameters: only default constructors '" + rec->tag +
                           "()' are supported",
              "constructor");
        return;
    }
    if (rec->constructors.empty()) {
        error(n.get(), "out-of-line definition of constructor '" + rec->tag + "::" + rec->tag + "()' but '" + recordName(rec) +
                           "' declares no constructor",
              "no-matching-declaration");
        return;
    }
    SymbolPtr sym = rec->constructors.front();
    if (sym->isDefined) {
        error(n.get(), "redefinition of '" + rec->tag + "::" + sym->name + "' (previously defined at line " +
                           displayLine(sym->declNode ? sym->declNode->line : sym->line) + ")",
              "redefinition");
        return;
    }
    sym->isDefined = true;
    sym->declNode = n.get();
    n->symbol = sym;
    functionBody(n, sym, rec);
}

/* `obj.f()` on a const object may only call `f() const`; on any other
   object a non-const `f` is preferred to `f() const` with the same parameters */
std::vector<SymbolPtr> SemanticAnalyzer::objectCandidates(const std::vector<SymbolPtr> &all, bool constObject,
                                                          const ASTNode *at, const std::string &name) {
    if (!constObject) return all;
    /* there are no const member functions (D35): a const object can only use static ones */
    std::vector<SymbolPtr> out;
    for (const auto &c : all)
        if (c->kind != SymbolKind::Function || c->isStatic) out.push_back(c);
    if (out.empty() && !all.empty())
        error(at, "member function '" + name + "' cannot be called on a const object (there are no const member functions)",
              "const-object");
    return out;
}

/* ---------------- operator overloading ---------------- */

void SemanticAnalyzer::checkOperatorDeclaration(const SymbolPtr &s, const ASTNode *at) {
    const std::string op = s->name.substr(8);
    static const std::set<std::string> binaryOnly = {"/", "%", "^", "|", "=", "<", ">", "==", "!=", "<=", ">=",
                                                     "&&", "||", "<<", ">>", "+=", "-=", "*=", "/=", "%=", "&=",
                                                     "|=", "^=", "<<=", ">>=", "[]"};
    static const std::set<std::string> unaryOnly = {"~", "!"};
    static const std::set<std::string> either = {"+", "-", "*", "&"};
    static const std::set<std::string> memberOnly = {"=", "[]", "()"};
    bool member = s->isMethod;
    size_t p = s->type->params.size();
    size_t operands = p + (member ? 1 : 0);
    std::string where = member ? "a member" : "a non-member";
    auto bad = [&](const std::string &why) { error(at, "overloaded '" + s->name + "' " + why, "operator-overload"); };
    if (!member && memberOnly.count(op)) return bad("must be a non-static member function");
    if (op == "()") return;
    if (binaryOnly.count(op) && operands != 2) return bad("must be a binary operator (it has " + std::to_string(operands) + " operand" + (operands == 1 ? "" : "s") + ")");
    if (unaryOnly.count(op) && operands != 1) return bad("must be a unary operator (it has " + std::to_string(operands) + " operands)");
    if (either.count(op) && operands != 1 && operands != 2) return bad("must be a unary or binary operator (it has " + std::to_string(operands) + " operands)");
    if ((op == "++" || op == "--")) {
        if (operands == 2) {
            const TypePtr &last = s->type->params.back();
            if (!(last->kind == TypeKind::Int && !last->isUnsigned)) return bad("(postfix) must take 'int' as its extra parameter");
        } else if (operands != 1) {
            return bad("must take one operand (prefix) or one plus 'int' (postfix)");
        }
    }
    if (!member) {
        bool classParam = std::any_of(s->type->params.begin(), s->type->params.end(), [](const TypePtr &t) {
            TypePtr u = stripRef(t);
            return isRecord(u);
        });
        if (!classParam) return bad("must have at least one parameter of class type");
    }
}

bool SemanticAnalyzer::overloadedOperator(const ASTNodePtr &n, const std::string &op,
                                          const std::vector<ASTNodePtr> &operands, TypePtr &result) {
    bool anyRecord = false;
    for (const auto &o : operands) {
        if (recordOf(o->semType)) anyRecord = true;
    }
    if (!anyRecord) return false;
    for (const auto &o : operands) {
        if (isError(o->semType)) {
            result = errorType();
            return true;
        }
    }
    const std::string name = "operator" + op;
    RecordInfo *lrec = recordOf(operands[0]->semType);
    std::vector<ASTNodePtr> memberArgs(operands.begin() + 1, operands.end());
    std::vector<SymbolPtr> members, frees;
    MemberLookup ml;
    if (lrec && lrec->complete) {
        ml = lookupMember(lrec, name);
        for (const auto &s : ml.symbols) {
            if (s->kind == SymbolKind::Function) members.push_back(s);
        }
    }
    auto g = st.scope(0).names.find(name); /* operators are file-scope functions */
    if (g != st.scope(0).names.end()) {
        for (const auto &s : g->second) {
            if (s->kind == SymbolKind::Function && !s->isMethod) frees.push_back(s);
        }
    }
    if (members.empty() && frees.empty()) return false;
    SymbolPtr chosen;
    bool viaMember;
    if (!members.empty() && (anyViable(members, memberArgs) || frees.empty() || !anyViable(frees, operands))) {
        chosen = resolveOverload(name, members, memberArgs, n.get());
        viaMember = true;
    } else {
        chosen = resolveOverload(name, frees, operands, n.get());
        viaMember = false;
    }
    if (!chosen) {
        result = errorType();
        return true;
    }
    if (viaMember) checkAccess(ml, lrec, name, n.get());
    n->symbol = chosen;
    chosen->useCount++;
    TypePtr r = callResult(chosen->type);
    if (isReference(r)) {
        n->isLValue = true;
        r = r->elem;
    }
    result = r;
    return true;
}

} // namespace sem
