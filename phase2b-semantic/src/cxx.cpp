/* The C++-style parts of the language: constructors and object
   construction, operator overloading, `new`, and va_start/va_arg/va_end. */
#include <algorithm>

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

SymbolPtr SemanticAnalyzer::construct(RecordInfo *rec, const std::vector<ASTNodePtr> &args, const ASTNode *at) {
    if (!rec) return nullptr;
    if (!rec->complete) {
        error(at, "cannot construct an object of incomplete type '" + recordName(rec) + "'", "incomplete-type");
        return nullptr;
    }
    for (const auto &a : args) {
        if (isError(a->semType)) return nullptr;
    }
    RecordInfo *argRec = args.size() == 1 ? recordOf(args[0]->semType) : nullptr;
    bool copyLike = argRec && (argRec == rec || isDerivedFrom(argRec, rec)); /* the implicit copy constructor */
    if (rec->constructors.empty()) {
        if (args.empty() || copyLike) return nullptr; /* implicit default / copy constructor */
        error(at, "no matching constructor for initialization of '" + recordName(rec) + "' with " +
                      std::to_string(args.size()) + " argument" + (args.size() == 1 ? "" : "s") +
                      " (it declares no constructors, so only default and copy construction are possible)",
              "constructor");
        return nullptr;
    }
    if (copyLike && !anyViable(rec->constructors, args)) return nullptr;
    if (args.empty() && !anyViable(rec->constructors, args)) {
        std::string declared;
        for (const auto &c : rec->constructors) declared += (declared.empty() ? "" : ", ") + describeSignature(c);
        error(at, "'" + recordName(rec) + "' has no default constructor (declared: " + declared +
                      "); pass constructor arguments, e.g. '" + rec->tag + " x(...)'",
              "constructor");
        return nullptr;
    }
    SymbolPtr chosen = resolveOverload(rec->tag + "::" + rec->tag, rec->constructors, args, at);
    if (chosen) {
        MemberLookup ml;
        ml.symbols = {chosen};
        ml.declaringRecord = rec;
        ml.access = chosen->access;
        checkAccess(ml, rec, rec->tag + "::" + describeSignature(chosen), at);
        chosen->useCount++;
    }
    return chosen;
}

/* `Dog d;` / `Dog pack[3];` / `new Dog`: a class with constructors must
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

TypePtr SemanticAnalyzer::newExpr(const ASTNodePtr &n) {
    if (!n->typeExpr) return errorType();
    ASTTypeExpr te = *n->typeExpr;
    bool arrayNew = !te.arrayDims.empty() && !te.grouped;
    if (arrayNew) { /* `new T[n]`: the first size is evaluated at run time */
        ASTNodePtr first = te.arrayDims.front();
        te.arrayDims.erase(te.arrayDims.begin());
        TypePtr st0 = value(first);
        if (!isError(st0) && !isIntegral(st0)) {
            error(first.get(), "array size in 'new' must have an integer type, not " + q(st0), "array-size");
        } else if (first->hasConstValue && first->constValue < 0) {
            error(first.get(), "array size in 'new' is negative ('" + std::to_string(first->constValue) + "')",
                  "array-size");
        }
    }
    TypePtr target = resolveType(te, n.get(), false).type;
    if (!target) target = errorType();
    ASTNodePtr init;
    for (const auto &c : n->children) {
        if (c->kind == ASTKind::ConstructExpr) init = c;
    }
    if (isError(target)) {
        if (init) for (const auto &a : init->children) expr(a);
        return errorType();
    }
    if (!isComplete(target)) {
        error(n.get(), "'new' cannot allocate an object of incomplete type " + q(target), "incomplete-type");
        return errorType();
    }
    if (init) {
        if (arrayNew && !init->children.empty()) {
            error(init.get(), "'new T[n]' cannot pass constructor arguments to the elements", "initializer");
        }
        constructorInit(target, init, "the object allocated by 'new'");
    } else {
        defaultConstruct(target, n.get());
    }
    return pointerTo(target);
}

/* `Dog::Dog(...) { }` / `Dog::~Dog() { }` after the class */
void SemanticAnalyzer::outOfClassSpecial(const ASTNodePtr &n) {
    bool ctor = n->kind == ASTKind::ConstructorDef;
    const std::string cls = n->typeExpr ? n->typeExpr->className : "";
    std::string name = tagFromLabel(n->label);
    SymbolPtr tag = st.lookupTag(cls);
    if (!tag || !tag->record) {
        error(n.get(), "use of undeclared class '" + cls + "'", "unknown-type");
        return;
    }
    RecordInfo *rec = tag->record.get();
    if (name != rec->tag) {
        error(n.get(), std::string(ctor ? "constructor" : "destructor") + " name '" + (ctor ? "" : "~") + name +
                           "' does not match the class name '" + rec->tag + "'",
              ctor ? "constructor" : "destructor");
        return;
    }
    SymbolPtr sym;
    if (ctor) {
        TypePtr ft = functionType(voidType(), resolveParams(*n->typeExpr, n.get()), n->typeExpr->isVariadic);
        for (const auto &c : rec->constructors) {
            if (sameParameterLists(c->type, ft)) sym = c;
        }
        if (!sym) {
            std::string sig = rec->tag + "::" + rec->tag + "(";
            for (size_t i = 0; i < ft->params.size(); ++i) sig += (i ? ", " : "") + typeToString(ft->params[i]);
            error(n.get(), "out-of-line definition of constructor '" + sig + ")' does not match any constructor declared in '" +
                               recordName(rec) + "'",
                  "no-matching-declaration");
            return;
        }
    } else {
        sym = rec->destructor;
        if (!sym) {
            error(n.get(), "out-of-line definition of '" + rec->tag + "::~" + rec->tag + "', but '" + recordName(rec) +
                               "' declares no destructor",
                  "no-matching-declaration");
            return;
        }
    }
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
    if (s->type->variadic) return bad("cannot be variadic");
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

/* ---------------- va_start / va_arg / va_end ---------------- */

TypePtr SemanticAnalyzer::varargBuiltin(const ASTNodePtr &n) {
    const std::string &name = n->label;
    const auto &args = n->children;
    size_t want = name == "va_end" ? 1 : 2;
    for (size_t i = 0; i < args.size(); ++i) {
        if (!(name == "va_arg" && i == 1 && args[i]->kind == ASTKind::TypeNameNode)) expr(args[i]);
    }
    if (args.size() != want) {
        error(n.get(), "'" + name + "' expects " + std::to_string(want) + " argument" + (want == 1 ? "" : "s") + " but " +
                           std::to_string(args.size()) + (args.size() == 1 ? " was" : " were") + " provided",
              "argument-count");
        return name == "va_arg" ? errorType() : voidType();
    }
    const ASTNodePtr &ap = args[0];
    TypePtr apt = stripRef(ap->semType);
    if (!isError(apt) && !(apt->kind == TypeKind::Opaque && apt->name == "va_list")) {
        error(ap.get(), "argument 1 of '" + name + "' must be a 'va_list' variable, not " + q(ap->semType), "varargs");
    } else if (!isError(apt) && !ap->isLValue) {
        error(ap.get(), "argument 1 of '" + name + "' must be a 'va_list' variable (an lvalue)", "varargs");
    }
    if (name == "va_start") {
        FunctionCtx *f = fn();
        Symbol *fsym = f ? f->fn : nullptr;
        if (!fsym || !fsym->type->variadic) {
            error(n.get(), "'va_start' used in " + std::string(fsym ? "function '" + fsym->name + "', which has fixed arguments"
                                                                    : "a context that is not a variadic function"),
                  "varargs");
        } else if (fsym->params.empty()) {
            error(n.get(), "'va_start' needs a named parameter before the '...'", "varargs");
        } else {
            const SymbolPtr &last = fsym->params.back();
            if (!(args[1]->kind == ASTKind::Identifier && args[1]->symbol == last)) {
                warning(args[1].get(), "second argument of 'va_start' is not the last named parameter ('" + last->name + "')",
                        "varargs");
            }
        }
        return voidType();
    }
    if (name == "va_end") return voidType();
    /* va_arg(ap, T) */
    const ASTNodePtr &tn = args[1];
    if (tn->kind != ASTKind::TypeNameNode || !tn->typeExpr) {
        error(tn.get(), "second argument of 'va_arg' must be a type", "varargs");
        return errorType();
    }
    TypePtr t = resolveType(*tn->typeExpr, tn.get(), false).type;
    tn->semType = t;
    if (!t || isError(t)) return errorType();
    if (!isComplete(t) || isArray(t) || isFunction(t)) {
        error(tn.get(), "'va_arg' cannot fetch a value of type " + q(t), "varargs");
        return errorType();
    }
    TypePtr promoted = integerPromotion(t);
    if (t->kind == TypeKind::Float) promoted = doubleType();
    if (!sameType(promoted, t)) {
        warning(tn.get(), q(t) + " is promoted to " + q(promoted) + " when passed through '...', so 'va_arg' must ask for " +
                              q(promoted),
                "varargs");
    }
    return unqualified(t);
}

} // namespace sem
