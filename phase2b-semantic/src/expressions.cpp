/* Expression type checking: every rule synthesizes the node's type
   (semType), whether it designates an object (isLValue) and, for integer
   constant expressions, its value (constValue) -- needed for case labels,
   array sizes, enumerators and static initializers. */
#include <algorithm>
#include <cctype>
#include <climits>
#include <cstring>
#include <functional>

#include "diagnostics/diagnostics.hpp"
#include "semantic.h"

namespace sem {

static std::string q(const TypePtr &t) { return "'" + typeToString(t) + "'"; }

static void setConst(const ASTNodePtr &n, long long v) {
    n->hasConstValue = true;
    n->constValue = v;
}

/* ---------------- literals ---------------- */

static bool parseIntLiteral(const std::string &text, unsigned long long &v, bool &isUnsigned, int &longs,
                            bool &decimal) {
    size_t i = 0;
    int base = 10;
    if (text.size() > 1 && text[0] == '0' && (text[1] == 'x' || text[1] == 'X')) base = 16, i = 2;
    else if (text.size() > 1 && text[0] == '0' && (text[1] == 'b' || text[1] == 'B')) base = 2, i = 2;
    else if (text.size() > 1 && text[0] == '0' && std::isdigit(static_cast<unsigned char>(text[1]))) base = 8, i = 1;
    decimal = base == 10;
    v = 0;
    bool overflow = false;
    for (; i < text.size(); ++i) {
        char ch = text[i];
        int d;
        if (std::isdigit(static_cast<unsigned char>(ch))) d = ch - '0';
        else if (base == 16 && std::isxdigit(static_cast<unsigned char>(ch))) d = std::tolower(ch) - 'a' + 10;
        else break;
        if (d >= base) break;
        if (v > (ULLONG_MAX - d) / base) overflow = true;
        v = v * base + d;
    }
    isUnsigned = false;
    longs = 0;
    for (; i < text.size(); ++i) {
        char ch = static_cast<char>(std::tolower(text[i]));
        if (ch == 'u') isUnsigned = true;
        else if (ch == 'l') ++longs;
    }
    return !overflow;
}

/* decodes the escapes of a char/string literal body (quotes stripped) */
static std::vector<int> decodeEscapes(const std::string &body) {
    std::vector<int> out;
    for (size_t i = 0; i < body.size(); ++i) {
        if (body[i] != '\\' || i + 1 >= body.size()) {
            out.push_back(static_cast<unsigned char>(body[i]));
            continue;
        }
        char e = body[++i];
        switch (e) {
            case 'n': out.push_back('\n'); break;
            case 't': out.push_back('\t'); break;
            case 'r': out.push_back('\r'); break;
            case 'a': out.push_back('\a'); break;
            case 'b': out.push_back('\b'); break;
            case 'f': out.push_back('\f'); break;
            case 'v': out.push_back('\v'); break;
            case 'x': {
                int v = 0;
                while (i + 1 < body.size() && std::isxdigit(static_cast<unsigned char>(body[i + 1]))) {
                    char h = static_cast<char>(std::tolower(body[++i]));
                    v = v * 16 + (std::isdigit(static_cast<unsigned char>(h)) ? h - '0' : h - 'a' + 10);
                }
                out.push_back(v & 0xff);
                break;
            }
            default:
                if (e >= '0' && e <= '7') {
                    int v = e - '0';
                    for (int k = 0; k < 2 && i + 1 < body.size() && body[i + 1] >= '0' && body[i + 1] <= '7'; ++k)
                        v = v * 8 + (body[++i] - '0');
                    out.push_back(v & 0xff);
                } else {
                    out.push_back(static_cast<unsigned char>(e)); /* \\ \' \" \? */
                }
        }
    }
    return out;
}

static std::string stripQuotes(const std::string &s) {
    return s.size() >= 2 ? s.substr(1, s.size() - 2) : std::string();
}

/* ---------------- helpers ---------------- */

TypePtr SemanticAnalyzer::value(const ASTNodePtr &n) { return decay(expr(n)); }

bool SemanticAnalyzer::isNullPointerConstant(const ASTNodePtr &n) {
    if (!n) return false;
    if (n->hasConstValue && n->constValue == 0 && isIntegral(n->semType)) return true;
    if (n->kind == ASTKind::CastExpr && isVoidPointer(n->semType)) return isNullPointerConstant(n->children[0]);
    return false;
}

static std::string fill(std::string tmpl, const TypePtr &from, const TypePtr &to) {
    auto put = [&](const std::string &key, const std::string &val) {
        for (size_t p; (p = tmpl.find(key)) != std::string::npos;) tmpl.replace(p, key.size(), val);
    };
    put("%F", typeToString(from));
    put("%T", typeToString(to));
    return tmpl;
}

bool SemanticAnalyzer::convertible(const TypePtr &target, const ASTNodePtr &e, const std::string &message) {
    TypePtr from = decay(e->semType);
    if (isError(from) || isError(target)) return true;
    if (isRecord(target) || isRecord(from)) {
        if (sameType(unqualified(target), from)) return true;
        error(e.get(), fill(message, from, target), "type-mismatch");
        return false;
    }
    Conversion c = implicitConversion(from, target, isNullPointerConstant(e));
    if (c.rank != ConvRank::None) {
        checkConstantConversion(target, e);
        return true;
    }
    error(e.get(), fill(message, from, target) + (c.why.empty() ? "" : " (" + c.why + ")"), "type-mismatch");
    return false;
}

/* an integer constant that changes value when converted: `char c = 300;`
   (gcc's -Woverflow). Converting a negative constant to an unsigned type
   of the same width (`unsigned u = -1;`) is a deliberate idiom and is not
   reported, as in gcc. */
void SemanticAnalyzer::checkConstantConversion(const TypePtr &targetIn, const ASTNodePtr &e) {
    TypePtr from = e->semType ? unqualified(decay(e->semType)) : nullptr;
    TypePtr target = unqualified(targetIn);
    if (!e->hasConstValue || !from || !isIntegral(from) || !isIntegral(target) || target->kind == TypeKind::Bool ||
        target->kind == TypeKind::Enum)
        return;
    long long v = wrapToType(e->constValue, from);
    if (fitsInType(v, from, target)) return;
    bool uns = isUnsignedInteger(target);
    if (uns) {
        auto signedTarget = basicType(target->kind, false);
        if (fitsInType(v, from, signedTarget)) return; /* -1 -> 0xFF...: intended */
    }
    long long r = wrapToType(v, target);
    warning(e.get(), std::string(uns ? "unsigned conversion" : "overflow in conversion") + " from " + q(from) + " to " +
                         q(target) + " changes value from '" + constantToString(v, from) + "' to '" +
                         constantToString(r, target) + "'",
            "overflow");
}

/* A record is a modifiable lvalue only if all its members are (C11
   6.3.2.1; Papaspyrou's isModifiable for struct/union types): the first
   const-qualified data member reached through fields, arrays, nested
   records and base classes, as "id" or "inner.id"; "" if there is none. */
static std::string constMemberPath(const RecordInfo *r, int depth = 0) {
    if (!r || depth > 32) return "";
    for (const auto &b : r->bases) {
        std::string p = constMemberPath(b.record.get(), depth + 1);
        if (!p.empty()) return p;
    }
    for (const auto &f : r->fields) {
        if (f->storage != Storage::Member || !f->type) continue;
        TypePtr t = f->type;
        while (t && t->kind == TypeKind::Array) {
            if (t->isConst) break;
            t = t->elem;
        }
        if (!t) continue;
        std::string name = f->name.empty() ? std::string("(unnamed member)") : f->name;
        if (t->isConst) return name;
        if (t->kind == TypeKind::Record) {
            std::string p = constMemberPath(t->record.get(), depth + 1);
            if (!p.empty()) return f->name.empty() ? p : name + "." + p;
        }
    }
    return "";
}

bool SemanticAnalyzer::checkModifiable(const ASTNodePtr &n, const std::string &what) {
    const TypePtr &t = n->semType;
    if (isError(t)) return false;
    if (!n->isLValue) {
        error(n.get(), "lvalue required as " + what + " (this expression is not assignable)", "lvalue");
        return false;
    }
    if (isArray(t)) {
        error(n.get(), "array type " + q(t) + " is not assignable", "lvalue");
        return false;
    }
    if (isFunction(t)) {
        error(n.get(), "a function is not assignable", "lvalue");
        return false;
    }
    if (byCopyCaptureUses.count(n.get())) {
        error(n.get(), "cannot modify '" + n->label + "': it is captured by copy in a non-mutable lambda", "const");
        return false;
    }
    if (t->isConst) {
        if (n->kind == ASTKind::Identifier) {
            error(n.get(), "cannot assign to variable '" + n->label + "' with const-qualified type " + q(t), "const");
        } else {
            error(n.get(), "cannot assign to a read-only location of type " + q(t), "const");
        }
        return false;
    }
    if (t->kind == TypeKind::Record) {
        std::string member = constMemberPath(t->record.get());
        if (!member.empty()) {
            error(n.get(), "cannot assign to " +
                               (n->kind == ASTKind::Identifier ? "variable '" + n->label + "'" : std::string("an object")) +
                               " of type " + q(t) + ": its member '" + member + "' is const-qualified",
                  "const");
            return false;
        }
    }
    return true;
}

void SemanticAnalyzer::checkAccess(const MemberLookup &ml, RecordInfo *naming, const std::string &name,
                                   const ASTNode *at) {
    if (!ml.declaringRecord || ml.symbols.empty()) return;
    RecordInfo *ctx = currentClass();
    if (ctx == ml.declaringRecord) return;
    bool ok = false;
    switch (ml.access) {
        case Access::Public: ok = true; break;
        case Access::Private: ok = ctx && ctx == naming; break;
        /* C++: from a member of `ctx`, only through `ctx` or a class derived from it */
        case Access::Protected: ok = ctx && (ctx == naming || isDerivedFrom(naming, ctx)); break;
        case Access::NoAccess: ok = false; break;
    }
    if (ok) return;
    const RecordInfo *d = ml.declaringRecord;
    std::string owner = recordDisplayName(*d);
    Access declared = ml.symbols.front()->access;
    std::string from = ctx ? " from " + recordKindName(ctx->kind) + " '" + ctx->tag + "'" : " outside the class";
    if (declared == Access::Private || declared == Access::Protected) {
        error(at, "'" + name + "' is a " + accessName(declared) + " member of '" + owner + "' and is not accessible" + from,
              "access");
    } else {
        error(at, "'" + name + "' (a public member of '" + owner + "') is not accessible" + from +
                      " because of non-public inheritance",
              "access");
    }
}

/* ---------------- dispatcher ---------------- */

TypePtr SemanticAnalyzer::expr(const ASTNodePtr &n) {
    if (!n) return errorType();
    n->isLValue = false;
    n->hasConstValue = false;
    TypePtr t;
    switch (n->kind) {
        case ASTKind::IntLiteral: {
            unsigned long long v;
            bool isUnsigned, decimal;
            int longs;
            if (!parseIntLiteral(n->label, v, isUnsigned, longs, decimal)) {
                warning(n.get(), "integer literal '" + n->label + "' is too large and was truncated", "literal");
            }
            TypeKind k = longs >= 2 ? TypeKind::LongLong : longs == 1 ? TypeKind::Long : TypeKind::Int;
            if (k != TypeKind::LongLong) {
                if (!isUnsigned && v > static_cast<unsigned long long>(INT_MAX)) {
                    if (!decimal && v <= UINT_MAX) isUnsigned = true;
                    else k = TypeKind::LongLong;
                } else if (isUnsigned && v > UINT_MAX) {
                    k = TypeKind::LongLong;
                }
            }
            t = basicType(k, isUnsigned);
            setConst(n, static_cast<long long>(v));
            break;
        }
        case ASTKind::FloatLiteral: {
            char last = n->label.empty() ? ' ' : n->label.back();
            t = (last == 'f' || last == 'F') ? basicType(TypeKind::Float) : doubleType();
            break;
        }
        case ASTKind::CharLiteral: {
            std::vector<int> cs = decodeEscapes(stripQuotes(n->label));
            if (cs.empty()) {
                error(n.get(), "empty character constant", "literal");
                t = errorType();
                break;
            }
            if (cs.size() == 1) {
                t = charType();
                setConst(n, static_cast<signed char>(cs[0]));
            } else {
                warning(n.get(), "multi-character character constant " + n->label + " has type 'int'", "multichar");
                long long v = 0;
                for (int c : cs) v = (v << 8) | (c & 0xff);
                t = intType();
                setConst(n, static_cast<int>(v));
            }
            break;
        }
        case ASTKind::StringLiteral:
            t = arrayOf(charType(), static_cast<long long>(decodeEscapes(stripQuotes(n->label)).size()) + 1);
            n->isLValue = true;
            break;
        case ASTKind::BoolLiteral:
            t = boolType();
            setConst(n, n->label == "true" ? 1 : 0);
            break;
        case ASTKind::Identifier: t = identifier(n); break;
        case ASTKind::ThisExpr: {
            RecordInfo *cls = currentClass();
            FunctionCtx *f = fn();
            if (!cls || (f && f->isStaticMethod)) {
                error(n.get(), cls ? "'this' cannot be used in a static member function"
                                   : "invalid use of 'this' outside of a non-static member function",
                      "this");
                t = errorType();
            } else {
                if (f && f->isLambda && !isLambdaThisCaptured(f)) {
                    error(n.get(), "'this' is not captured by this lambda (capture it with [this], [=] or [&])",
                          "capture");
                }
                t = pointerTo(recordType(cls->shared_from_this()));
            }
            break;
        }
        case ASTKind::BinaryExpr: t = binary(n); break;
        case ASTKind::UnaryExpr: t = unary(n); break;
        case ASTKind::PostfixOpExpr: {
            TypePtr ot = expr(n->children[0]);
            if (isRecord(isReference(ot) ? ot->elem : ot)) { /* `obj++` calls operator++(int) */
                auto dummy = std::make_shared<ASTNode>();
                dummy->kind = ASTKind::IntLiteral;
                dummy->label = "0";
                dummy->semType = intType();
                dummy->hasConstValue = true;
                if (!overloadedOperator(n, n->label, {n->children[0], dummy}, t)) {
                    error(n.get(), "cannot " + std::string(n->label == "++" ? "increment" : "decrement") +
                                       " a value of type " + q(ot) + " (no 'operator" + n->label + "(int)' is declared)",
                          "invalid-operands");
                    t = errorType();
                }
                break;
            }
            std::string what = n->label == "++" ? "increment operand" : "decrement operand";
            TypePtr vt = decay(ot);
            if (!isError(vt) && !(isArithmetic(vt) || (isPointer(vt) && isComplete(vt->elem)))) {
                error(n.get(), "cannot " + std::string(n->label == "++" ? "increment" : "decrement") +
                                   " a value of type " + q(ot),
                      "invalid-operands");
                t = errorType();
                break;
            }
            checkModifiable(n->children[0], what);
            t = vt;
            break;
        }
        case ASTKind::AssignExpr: t = assignment(n); break;
        case ASTKind::TernaryExpr: t = ternary(n); break;
        case ASTKind::CommaExpr:
            value(n->children[0]);
            t = value(n->children[1]);
            break;
        case ASTKind::CallExpr: t = call(n); break;
        case ASTKind::BuiltinCallExpr: t = builtinCall(n); break;
        case ASTKind::MemberExpr: t = member(n, false, false); break;
        case ASTKind::ArrowExpr: t = member(n, true, false); break;
        case ASTKind::ScopeExpr: t = scopeMember(n); break;
        case ASTKind::IndexExpr: t = index(n); break;
        case ASTKind::CastExpr: t = cast(n); break;
        case ASTKind::SizeofExpr: t = sizeofExpr(n); break;
        case ASTKind::NewExpr: t = newExpr(n); break;
        case ASTKind::ConstructExpr: t = constructExpr(n); break;
        case ASTKind::DeleteExpr: {
            TypePtr vt = value(n->children[0]);
            if (!isError(vt) && (!isPointer(vt) || isFunction(vt->elem))) {
                error(n.get(), "cannot " + std::string(n->label == "[]" ? "delete[]" : "delete") +
                                   " an expression of type " + q(vt) + " (a pointer is required)",
                      "delete");
            }
            t = voidType();
            break;
        }
        case ASTKind::LambdaExpr: t = lambda(n); break;
        case ASTKind::TypeNameNode:
            error(n.get(), "unexpected type name '" + n->label + "' where an expression was expected", "type-as-value");
            t = errorType();
            break;
        case ASTKind::InitializerList:
            error(n.get(), "a brace-enclosed initializer list is not an expression", "initializer");
            for (const auto &c : n->children) expr(c);
            t = errorType();
            break;
        default:
            t = errorType();
            break;
    }
    n->semType = t ? t : errorType();
    return n->semType;
}

/* ---------------- identifiers ---------------- */

TypePtr SemanticAnalyzer::identifier(const ASTNodePtr &n) {
    const std::string &name = n->label;
    Lookup l = st.lookup(name);
    if (l.symbols.empty() && hoistFunction(name)) l = st.lookup(name);
    if (l.symbols.empty()) {
        auto later = topVariableLines.find(name);
        if (later != topVariableLines.end() && later->second > n->line) {
            error(n.get(), "undeclared identifier '" + name + "' (it is declared later, at line " +
                               std::to_string(later->second) + "; variables must be declared before use)",
                  "undeclared");
        } else {
            error(n.get(), "undeclared identifier '" + name + "'", "undeclared");
        }
        return errorType();
    }
    SymbolPtr sym = l.symbols.front();
    n->symbol = sym;
    switch (sym->kind) {
        case SymbolKind::Typedef:
        case SymbolKind::Tag:
        case SymbolKind::Label:
            error(n.get(), "unexpected type name '" + name + "' where an expression was expected", "type-as-value");
            return errorType();
        case SymbolKind::EnumConstant:
            sym->useCount++;
            setConst(n, sym->constValue);
            return intType();
        case SymbolKind::Function: {
            if (l.symbols.size() > 1) {
                error(n.get(), "reference to overloaded function '" + name +
                                   "' is ambiguous here (call it, so its arguments select an overload)",
                      "ambiguous-overload");
                return errorType();
            }
            if (l.viaRecord && sym->isMethod && !sym->isStatic) {
                error(n.get(), "reference to non-static member function '" + name + "' must be called", "member-access");
                return errorType();
            }
            sym->useCount++;
            return sym->type;
        }
        default:
            break;
    }

    /* objects */
    FunctionCtx *f = fn();
    if (l.viaRecord) {
        if (f && f->isStaticMethod && sym->storage == Storage::Member) {
            error(n.get(), "invalid use of non-static member '" + name + "' in a static member function", "this");
            return errorType();
        }
        if (f && f->isLambda && !isLambdaThisCaptured(f) && sym->storage == Storage::Member) {
            error(n.get(), "member '" + name + "' needs 'this', which this lambda does not capture ([this], [=] or [&])",
                  "capture");
        }
        checkAccess(l.member, currentClass(), name, n.get());
    }
    bool byCopy = false;
    if (l.crossedLambda && (sym->storage == Storage::Local || sym->storage == Storage::Param)) {
        for (auto &ctx : fns) {
            if (!ctx.isLambda || ctx.lambdaScope != l.lambdaScopeId) continue;
            auto cap = ctx.captures.find(name);
            if (cap == ctx.captures.end() && !ctx.defaultCapture) {
                error(n.get(), "variable '" + name +
                                   "' cannot be used in the lambda: it is not captured and the lambda has no capture-default",
                      "capture");
            } else {
                byCopy = (cap != ctx.captures.end() ? !cap->second.byRef : ctx.defaultCapture == '=') && !ctx.isMutable;
            }
        }
    }
    sym->useCount++;
    if (!unevaluated) sym->evaluatedUses++;
    TypePtr t = sym->type;
    if (isReference(t)) t = t->elem;
    if (byCopy) {
        byCopyCaptureUses.insert(n.get());
        t = qualified(t, true, false);
    }
    n->isLValue = true;
    if (sym->isConstant) setConst(n, sym->constValue);
    return t;
}

/* ---------------- operators ---------------- */

/* Folds an integer constant expression in its own type (Papaspyrou's
   V[op] over val[tau]: operands are first converted as the typing rule
   says -- usual arithmetic conversions, or only the left operand's
   integer promotion for a shift -- then the operation is done exactly and
   the result wrapped to the result type). Signed overflow and bad shift
   counts are reported, like gcc's -Woverflow / -Wshift-count-*. */
void SemanticAnalyzer::foldBinary(const ASTNodePtr &n, const std::string &op) {
    const ASTNodePtr &a = n->children[0], &b = n->children[1];
    TypePtr rt = n->semType ? n->semType : intType();
    if (!a->hasConstValue || !b->hasConstValue || !isIntegral(rt)) return;
    TypePtr at = a->semType ? unqualified(decay(a->semType)) : intType();
    TypePtr bt = b->semType ? unqualified(decay(b->semType)) : intType();
    if (!isIntegral(at) || !isIntegral(bt)) return;
    long long x = a->constValue, y = b->constValue;

    if (op == "&&" || op == "||") {
        setConst(n, op == "&&" ? (x != 0 && y != 0) : (x != 0 || y != 0));
        return;
    }
    if (op == "==" || op == "!=" || op == "<" || op == ">" || op == "<=" || op == ">=") {
        TypePtr ct = usualArithmetic(at, bt); /* `-1 < 0u` compares as unsigned */
        long long X = wrapToType(x, ct), Y = wrapToType(y, ct);
        bool u64 = integerBits(ct) == 64 && isUnsignedInteger(ct);
        auto ux = static_cast<unsigned long long>(X), uy = static_cast<unsigned long long>(Y);
        bool r = op == "==" ? X == Y
                 : op == "!=" ? X != Y
                 : op == "<"  ? (u64 ? ux < uy : X < Y)
                 : op == ">"  ? (u64 ? ux > uy : X > Y)
                 : op == "<=" ? (u64 ? ux <= uy : X <= Y)
                              : (u64 ? ux >= uy : X >= Y);
        setConst(n, r);
        return;
    }
    int bits = integerBits(rt);
    bool uns = isUnsignedInteger(rt);
    if (op == "<<" || op == ">>") {
        long long count = wrapToType(y, integerPromotion(bt));
        std::string dir = op == "<<" ? "left" : "right";
        if (count < 0) {
            warning(b.get(), dir + " shift count is negative", "shift-count");
            return;
        }
        if (count >= bits) {
            warning(b.get(), dir + " shift count >= width of type " + q(rt) + " (" + std::to_string(bits) + " bits)",
                    "shift-count");
            return;
        }
        long long X = wrapToType(x, rt);
        unsigned long long mask = bits == 64 ? ~0ULL : (1ULL << bits) - 1;
        long long r;
        if (op == "<<") r = static_cast<long long>((static_cast<unsigned long long>(X) << count) & mask);
        else if (uns) r = static_cast<long long>((static_cast<unsigned long long>(X) & mask) >> count);
        else r = X >> count; /* arithmetic shift of a sign-extended value */
        setConst(n, wrapToType(r, rt));
        return;
    }
    /* + - * / % & | ^ in the common type */
    long long X = wrapToType(x, rt), Y = wrapToType(y, rt);
    if ((op == "/" || op == "%") && Y == 0) return; /* reported by the caller */
    if (uns) {
        unsigned long long ux = static_cast<unsigned long long>(X), uy = static_cast<unsigned long long>(Y), ur;
        if (bits < 64) {
            unsigned long long mask = (1ULL << bits) - 1;
            ux &= mask, uy &= mask;
        }
        if (op == "+") ur = ux + uy;
        else if (op == "-") ur = ux - uy;
        else if (op == "*") ur = ux * uy;
        else if (op == "/") ur = ux / uy;
        else if (op == "%") ur = ux % uy;
        else if (op == "&") ur = ux & uy;
        else if (op == "|") ur = ux | uy;
        else if (op == "^") ur = ux ^ uy;
        else return;
        setConst(n, wrapToType(static_cast<long long>(ur), rt)); /* unsigned arithmetic wraps: no overflow */
        return;
    }
    __int128 X1 = X, Y1 = Y, r;
    if (op == "+") r = X1 + Y1;
    else if (op == "-") r = X1 - Y1;
    else if (op == "*") r = X1 * Y1;
    else if (op == "/") r = X1 / Y1;
    else if (op == "%") r = X1 % Y1;
    else if (op == "&") r = X1 & Y1;
    else if (op == "|") r = X1 | Y1;
    else if (op == "^") r = X1 ^ Y1;
    else return;
    __int128 lo = -(static_cast<__int128>(1) << (bits - 1)), hi = (static_cast<__int128>(1) << (bits - 1)) - 1;
    long long wrapped = wrapToType(static_cast<long long>(static_cast<unsigned long long>(r)), rt);
    if (r < lo || r > hi) {
        warning(n.get(), "integer overflow in expression of type " + q(rt) + " results in '" +
                             constantToString(wrapped, rt) + "'",
                "overflow");
    }
    setConst(n, wrapped);
}

TypePtr SemanticAnalyzer::binary(const ASTNodePtr &n) {
    const std::string &op = n->label;
    const ASTNodePtr &L = n->children[0], &R = n->children[1];
    TypePtr lt = value(L), rt = value(R);
    TypePtr overloaded;
    if (overloadedOperator(n, op, {L, R}, overloaded)) return overloaded;
    if (isError(lt) || isError(rt)) return errorType();
    bool classOperand = isRecord(lt) || isRecord(rt);
    auto bad = [&](const std::string &why) {
        error(n.get(), "invalid operands to binary '" + op + "' (" + q(lt) + " and " + q(rt) + ")" +
                           (classOperand ? ": no 'operator" + op + "' is declared for these operands"
                                         : why.empty() ? "" : ": " + why),
              "invalid-operands");
        return errorType();
    };
    auto pointeeUsable = [&](const TypePtr &p) {
        const TypePtr &e = p->elem;
        if (isVoid(e)) return error(n.get(), "arithmetic on a pointer to void (" + q(p) + ")", "invalid-operands"), false;
        if (isFunction(e)) return error(n.get(), "arithmetic on a pointer to a function (" + q(p) + ")", "invalid-operands"), false;
        if (!isComplete(e)) return error(n.get(), "arithmetic on a pointer to incomplete type " + q(e), "invalid-operands"), false;
        return true;
    };
    auto compatiblePointers = [&](const TypePtr &a, const TypePtr &b) {
        return sameType(unqualified(a->elem), unqualified(b->elem)) || isVoid(a->elem) || isVoid(b->elem) ||
               (isRecord(a->elem) && isRecord(b->elem) &&
                (isDerivedFrom(a->elem->record.get(), b->elem->record.get()) ||
                 isDerivedFrom(b->elem->record.get(), a->elem->record.get())));
    };
    TypePtr t;
    if (op == "&&" || op == "||") {
        if (!isScalar(lt) || !isScalar(rt)) return bad("operands must be scalar (arithmetic or pointer)");
        t = intType();
    } else if (op == "+" || op == "-") {
        if (isArithmetic(lt) && isArithmetic(rt)) {
            t = usualArithmetic(lt, rt);
        } else if (op == "+" && isPointer(lt) && isIntegral(rt)) {
            t = pointeeUsable(lt) ? lt : errorType();
        } else if (op == "+" && isIntegral(lt) && isPointer(rt)) {
            t = pointeeUsable(rt) ? rt : errorType();
        } else if (op == "-" && isPointer(lt) && isIntegral(rt)) {
            t = pointeeUsable(lt) ? lt : errorType();
        } else if (op == "-" && isPointer(lt) && isPointer(rt)) {
            if (!sameType(unqualified(lt->elem), unqualified(rt->elem)))
                return bad("pointers to different types cannot be subtracted");
            t = pointeeUsable(lt) ? intType() : errorType();
        } else {
            return bad(isPointer(lt) && isPointer(rt) ? "two pointers cannot be added" : "");
        }
    } else if (op == "*" || op == "/") {
        if (!isArithmetic(lt) || !isArithmetic(rt)) return bad("both operands must be arithmetic");
        t = usualArithmetic(lt, rt);
    } else if (op == "%") {
        if (!isIntegral(lt) || !isIntegral(rt)) return bad("both operands of '%' must be integers");
        t = usualArithmetic(lt, rt);
    } else if (op == "<<" || op == ">>") {
        if (!isIntegral(lt) || !isIntegral(rt)) return bad("both operands of a shift must be integers");
        t = integerPromotion(lt);
    } else if (op == "&" || op == "|" || op == "^") {
        if (!isIntegral(lt) || !isIntegral(rt)) return bad("both operands of a bitwise operator must be integers");
        t = usualArithmetic(lt, rt);
    } else { /* relational / equality */
        bool equality = op == "==" || op == "!=";
        if (isArithmetic(lt) && isArithmetic(rt)) {
            t = intType();
        } else if (isPointer(lt) && isPointer(rt)) {
            if (!compatiblePointers(lt, rt)) {
                error(n.get(), "comparison of distinct pointer types (" + q(lt) + " and " + q(rt) + ")", "invalid-operands");
                return errorType();
            }
            t = intType();
        } else if ((isPointer(lt) && isNullPointerConstant(R)) || (isPointer(rt) && isNullPointerConstant(L))) {
            t = intType();
        } else if ((isPointer(lt) && isIntegral(rt)) || (isIntegral(lt) && isPointer(rt))) {
            error(n.get(), "comparison between pointer and integer (" + q(lt) + " and " + q(rt) + ")", "invalid-operands");
            return errorType();
        } else {
            return bad(equality ? "these types cannot be compared for equality" : "these types cannot be ordered");
        }
    }
    if ((op == "/" || op == "%") && R->hasConstValue && R->constValue == 0 && isIntegral(rt)) {
        warning(R.get(), "division by zero is undefined", "division-by-zero");
    }
    n->semType = t;
    foldBinary(n, op);
    return t;
}

TypePtr SemanticAnalyzer::unary(const ASTNodePtr &n) {
    const std::string &op = n->label;
    const ASTNodePtr &c = n->children[0];
    if (op == "++(pre)" || op == "--(pre)") {
        TypePtr ot = expr(c);
        TypePtr overloaded;
        if (overloadedOperator(n, op.substr(0, 2), {c}, overloaded)) return overloaded;
        TypePtr vt = decay(ot);
        if (isError(vt)) return errorType();
        if (!(isArithmetic(vt) || (isPointer(vt) && isComplete(vt->elem)))) {
            error(n.get(), "cannot " + std::string(op[0] == '+' ? "increment" : "decrement") + " a value of type " + q(ot),
                  "invalid-operands");
            return errorType();
        }
        checkModifiable(c, op[0] == '+' ? "increment operand" : "decrement operand");
        return vt;
    }
    if (op == "&") {
        TypePtr ot = expr(c);
        TypePtr overloaded;
        if (overloadedOperator(n, "&", {c}, overloaded)) return overloaded;
        if (isError(ot)) return errorType();
        if (isFunction(ot)) return pointerTo(ot);
        if (!c->isLValue) {
            error(n.get(), "cannot take the address of an rvalue of type " + q(ot), "address-of");
            return errorType();
        }
        if (c->kind == ASTKind::Identifier && c->symbol && c->symbol->isRegister) {
            error(n.get(), "address of register variable '" + c->label + "' requested", "address-of");
            return errorType();
        }
        return pointerTo(ot);
    }
    if (op == "*") {
        TypePtr vt = value(c);
        TypePtr overloaded;
        if (overloadedOperator(n, "*", {c}, overloaded)) return overloaded;
        if (isError(vt)) return errorType();
        if (!isPointer(vt)) {
            error(n.get(), "indirection requires a pointer operand (" + q(vt) + " is not a pointer)", "dereference");
            return errorType();
        }
        if (isVoid(vt->elem)) {
            error(n.get(), "cannot dereference a " + q(vt) + " pointer (cast it to a typed pointer first)", "dereference");
            return errorType();
        }
        if (!isFunction(vt->elem) && !isComplete(vt->elem) && !isArray(vt->elem)) {
            error(n.get(), "cannot dereference a pointer to incomplete type " + q(vt->elem), "dereference");
            return errorType();
        }
        n->isLValue = !isFunction(vt->elem);
        return vt->elem;
    }
    TypePtr vt = value(c);
    TypePtr overloaded;
    if (overloadedOperator(n, op, {c}, overloaded)) return overloaded;
    if (isError(vt)) return errorType();
    TypePtr t;
    if (op == "+" || op == "-") {
        if (!isArithmetic(vt)) {
            error(n.get(), "invalid argument type " + q(vt) + " to unary '" + op + "' (an arithmetic type is required)",
                  "invalid-operands");
            return errorType();
        }
        t = integerPromotion(vt);
        if (c->hasConstValue && isIntegral(t)) {
            long long v = wrapToType(c->constValue, t);
            if (op == "-") {
                long long r = wrapToType(static_cast<long long>(0ULL - static_cast<unsigned long long>(v)), t);
                if (!isUnsignedInteger(t) && v != 0 && r == v) /* -INT_MIN */
                    warning(n.get(), "integer overflow in expression of type " + q(t) + " results in '" +
                                         constantToString(r, t) + "'",
                            "overflow");
                v = r;
            }
            setConst(n, v);
        }
    } else if (op == "~") {
        if (!isIntegral(vt)) {
            error(n.get(), "invalid argument type " + q(vt) + " to unary '~' (an integer type is required)",
                  "invalid-operands");
            return errorType();
        }
        t = integerPromotion(vt);
        if (c->hasConstValue) setConst(n, wrapToType(~c->constValue, integerPromotion(vt))); /* ~0u is 4294967295 */
    } else { /* ! */
        if (!isScalar(vt)) {
            error(n.get(), "invalid argument type " + q(vt) + " to unary '!' (a scalar type is required)",
                  "invalid-operands");
            return errorType();
        }
        t = intType();
        if (c->hasConstValue) setConst(n, !c->constValue);
    }
    return t;
}

TypePtr SemanticAnalyzer::assignment(const ASTNodePtr &n) {
    const std::string &op = n->label;
    const ASTNodePtr &L = n->children[0], &R = n->children[1];
    TypePtr lt = expr(L);
    TypePtr rt = value(R);
    if (isRecord(isReference(lt) ? lt->elem : lt)) { /* `a = b` / `a += b` on objects */
        TypePtr overloaded;
        if (overloadedOperator(n, op, {L, R}, overloaded)) return overloaded;
        if (op != "=") {
            if (!isError(rt)) {
                error(n.get(), "invalid operands to compound assignment '" + op + "' (" + q(lt) + " and " + q(rt) +
                                   "): no 'operator" + op + "' is declared",
                      "invalid-operands");
            }
            return errorType();
        }
        /* plain `=` without operator=: memberwise copy, checked below */
    }
    bool modifiable = checkModifiable(L, "left operand of assignment");
    if (isError(lt) || isError(rt)) return isError(lt) ? errorType() : unqualified(lt);
    TypePtr target = unqualified(lt);
    if (op == "=") {
        if (modifiable) convertible(target, R, "type mismatch: cannot assign '%F' to '%T'");
        return target;
    }
    std::string base = op.substr(0, op.size() - 1);
    bool ok;
    if ((base == "+" || base == "-") && isPointer(target)) {
        ok = isIntegral(rt) && isComplete(target->elem);
    } else if (base == "+" || base == "-" || base == "*" || base == "/") {
        ok = isArithmetic(target) && isArithmetic(rt);
    } else {
        ok = isIntegral(target) && isIntegral(rt);
    }
    if (!ok) {
        error(n.get(), "invalid operands to compound assignment '" + op + "' (" + q(target) + " and " + q(rt) + ")",
              "invalid-operands");
    }
    if ((base == "/" || base == "%") && R->hasConstValue && R->constValue == 0 && isIntegral(rt)) {
        warning(R.get(), "division by zero is undefined", "division-by-zero");
    }
    return target;
}

TypePtr SemanticAnalyzer::ternary(const ASTNodePtr &n) {
    const ASTNodePtr &C = n->children[0], &A = n->children[1], &B = n->children[2];
    condition(C, "?:");
    TypePtr a = value(A), b = value(B);
    if (isError(a) || isError(b)) return errorType();
    TypePtr t;
    if (isArithmetic(a) && isArithmetic(b)) t = usualArithmetic(a, b);
    else if (isVoid(a) && isVoid(b)) t = voidType();
    else if (isRecord(a) && sameType(a, b)) t = a;
    else if (isPointer(a) && isPointer(b)) {
        if (sameType(unqualified(a->elem), unqualified(b->elem))) t = qualified(a, false, false);
        else if (isVoid(a->elem)) t = a;
        else if (isVoid(b->elem)) t = b;
        else if (isRecord(a->elem) && isRecord(b->elem) && isDerivedFrom(a->elem->record.get(), b->elem->record.get())) t = b;
        else if (isRecord(a->elem) && isRecord(b->elem) && isDerivedFrom(b->elem->record.get(), a->elem->record.get())) t = a;
    } else if (isPointer(a) && isNullPointerConstant(B)) t = a;
    else if (isPointer(b) && isNullPointerConstant(A)) t = b;
    else if (isClosure(a) && sameType(a, b)) t = a;
    if (!t) {
        error(n.get(), "incompatible operand types in conditional expression (" + q(a) + " and " + q(b) + ")",
              "type-mismatch");
        return errorType();
    }
    if (C->hasConstValue) {
        const ASTNodePtr &chosen = C->constValue ? A : B;
        if (chosen->hasConstValue && isIntegral(t)) setConst(n, wrapToType(chosen->constValue, t));
    }
    return t;
}

TypePtr SemanticAnalyzer::index(const ASTNodePtr &n) {
    const ASTNodePtr &A = n->children[0], &I = n->children[1];
    TypePtr raw = expr(A);
    TypePtr at = decay(raw);
    TypePtr it = value(I);
    TypePtr overloaded;
    if (overloadedOperator(n, "[]", {A, I}, overloaded)) return overloaded;
    if (isError(at) || isError(it)) return errorType();
    TypePtr ptr, idx;
    const ASTNode *idxNode = I.get();
    if (isPointer(at)) ptr = at, idx = it;
    else if (isPointer(it)) ptr = it, idx = at, idxNode = A.get();
    else {
        error(n.get(), "subscripted value is not an array or pointer (it has type " + q(raw) + ")", "subscript");
        return errorType();
    }
    if (!isIntegral(idx)) {
        error(idxNode, "array subscript is not an integer (it has type " + q(idx) + ")", "subscript");
        return errorType();
    }
    if (isVoid(ptr->elem) || isFunction(ptr->elem) || !isComplete(ptr->elem)) {
        error(n.get(), "subscript of a pointer to " + std::string(isVoid(ptr->elem) ? "void" : isFunction(ptr->elem) ? "a function" : "an incomplete type") +
                           " (" + q(ptr) + ")",
              "subscript");
        return errorType();
    }
    if (isArray(raw) && raw->arraySize >= 0 && I->hasConstValue) {
        long long v = I->constValue;
        if (v < 0) {
            warning(I.get(), "array index " + std::to_string(v) + " is before the beginning of the array", "array-bounds");
        } else if (v >= raw->arraySize) {
            warning(I.get(), "array index " + std::to_string(v) + " is past the end of the array (which has " +
                                 std::to_string(raw->arraySize) + " elements)",
                    "array-bounds");
        }
    }
    n->isLValue = true;
    return ptr->elem;
}

TypePtr SemanticAnalyzer::cast(const ASTNodePtr &n) {
    TypePtr target = n->typeExpr ? resolveType(*n->typeExpr, n.get(), false).type : errorType();
    if (!target) target = errorType();
    const ASTNodePtr &c = n->children[0];
    TypePtr from = value(c);
    if (isError(target) || isError(from)) return target;
    std::string why = checkCast(from, target);
    if (!why.empty()) {
        error(n.get(), "invalid cast from " + q(from) + " to " + q(target) + ": " + why, "invalid-cast");
        return errorType();
    }
    if (c->hasConstValue && isIntegral(target)) {
        setConst(n, wrapToType(c->constValue, unqualified(target))); /* (unsigned char)300 is 44 */
    }
    return unqualified(target);
}

TypePtr SemanticAnalyzer::sizeofExpr(const ASTNodePtr &n) {
    TypePtr t;
    if (n->children.empty()) {
        t = n->typeExpr ? resolveType(*n->typeExpr, n.get(), false).type : errorType();
        if (!t) t = errorType();
    } else {
        ++unevaluated;
        t = expr(n->children[0]); /* not evaluated, only typed; arrays do not decay here */
        --unevaluated;
    }
    if (isError(t)) return unsignedIntType();
    if (isReference(t)) t = t->elem;
    if (isFunction(t)) {
        error(n.get(), "invalid application of 'sizeof' to a function type", "sizeof");
    } else if (!isComplete(t)) {
        error(n.get(), "invalid application of 'sizeof' to an incomplete type " + q(t), "sizeof");
    } else {
        setConst(n, sizeOf(t));
    }
    return unsignedIntType();
}

/* ---------------- members ---------------- */

/* evaluates the object of `obj.m` / `p->m` and finds its record */
static RecordInfo *recordOfBase(const TypePtr &bt, bool arrow, bool &constObject) {
    constObject = false;
    TypePtr t = bt;
    if (arrow) {
        t = decay(bt);
        if (!isPointer(t)) return nullptr;
        t = t->elem;
    } else if (isReference(t)) {
        t = t->elem;
    }
    if (!isRecord(t)) return nullptr;
    constObject = t->isConst;
    return t->record.get();
}

TypePtr SemanticAnalyzer::member(const ASTNodePtr &n, bool arrow, bool calleePosition) {
    const ASTNodePtr &base = n->children[0];
    const std::string &name = n->label;
    TypePtr bt = expr(base);
    if (isError(bt)) return errorType();
    bool constObject;
    RecordInfo *rec = recordOfBase(bt, arrow, constObject);
    if (!rec) {
        TypePtr vt = decay(bt);
        if (arrow && isRecord(bt)) {
            error(n.get(), "member reference type " + q(bt) + " is not a pointer; did you mean to use '.'?", "member-access");
        } else if (!arrow && isPointer(vt) && isRecord(vt->elem)) {
            error(n.get(), "member reference type " + q(bt) + " is a pointer; did you mean to use '->'?", "member-access");
        } else {
            error(n.get(), "member reference base type " + q(bt) + " is not a " +
                               std::string(arrow ? "pointer to a struct, union or class" : "struct, union or class"),
                  "member-access");
        }
        return errorType();
    }
    if (!rec->complete) {
        error(n.get(), "member access into incomplete type '" + recordDisplayName(*rec) + "'",
              "incomplete-type");
        return errorType();
    }
    MemberLookup ml = lookupMember(rec, name);
    if (ml.symbols.empty()) {
        error(n.get(), "unknown member '" + name + "': no member named '" + name + "' in '" +
                           recordDisplayName(*rec) + "'",
              "unknown-member");
        return errorType();
    }
    if (ml.ambiguous) {
        error(n.get(), "member '" + name + "' is found in more than one base class of '" + rec->tag + "'",
              "ambiguous-member");
        return errorType();
    }
    checkAccess(ml, rec, name, n.get());
    SymbolPtr sym = ml.symbols.front();
    n->symbol = sym;
    if (sym->kind == SymbolKind::Function) { /* counted once the call picks an overload */
        if (!calleePosition) {
            error(n.get(), "reference to member function '" + name + "' must be called", "member-access");
            return errorType();
        }
        return sym->type;
    }
    sym->useCount++;
    TypePtr t = sym->type;
    if (isReference(t)) t = t->elem;
    if (constObject && sym->storage == Storage::Member) t = qualified(t, true, false);
    n->isLValue = arrow || base->isLValue || sym->storage == Storage::Static;
    return t;
}

TypePtr SemanticAnalyzer::scopeMember(const ASTNodePtr &n) {
    const ASTNodePtr &base = n->children[0];
    if (base->kind != ASTKind::Identifier) {
        error(n.get(), "the left side of '::' must name a class", "scope");
        return errorType();
    }
    SymbolPtr tag = st.lookupTag(base->label);
    if (!tag || !tag->record) {
        error(base.get(), "'" + base->label + "' is not a class, struct or union", "scope");
        return errorType();
    }
    RecordInfo *rec = tag->record.get();
    MemberLookup ml = lookupMember(rec, n->label);
    if (ml.symbols.empty()) {
        error(n.get(), "no member named '" + n->label + "' in '" + recordDisplayName(*rec) + "'",
              "unknown-member");
        return errorType();
    }
    checkAccess(ml, rec, n->label, n.get());
    SymbolPtr sym = ml.symbols.front();
    n->symbol = sym;
    sym->useCount++;
    RecordInfo *cls = currentClass();
    bool viaThis = cls && (cls == rec || isDerivedFrom(cls, rec)) && !(fn() && fn()->isStaticMethod);
    if (sym->kind == SymbolKind::Function) {
        error(n.get(), "reference to member function '" + n->label + "' must be called", "member-access");
        return errorType();
    }
    if (sym->storage == Storage::Member && !viaThis) {
        error(n.get(), "invalid use of non-static data member '" + rec->tag + "::" + n->label + "' without an object",
              "member-access");
        return errorType();
    }
    n->isLValue = true;
    return sym->type;
}

/* ---------------- calls ---------------- */

TypePtr SemanticAnalyzer::callResult(const TypePtr &fnType) {
    if (!fnType || !isFunction(fnType)) return errorType();
    return fnType->ret;
}

Conversion SemanticAnalyzer::argumentConversion(const TypePtr &param, const ASTNodePtr &arg) {
    TypePtr at = arg->semType;
    Conversion c;
    if (isError(at) || isError(param)) {
        c.rank = ConvRank::Exact;
        return c;
    }
    if (isReference(param)) {
        const TypePtr &T = param->elem;
        bool binds = arg->isLValue && (T->isConst || !at->isConst) &&
                     (sameType(unqualified(T), unqualified(at)) ||
                      (isRecord(T) && isRecord(at) && isDerivedFrom(at->record.get(), T->record.get())));
        if (binds) {
            c.rank = sameType(unqualified(T), unqualified(at)) ? ConvRank::Exact : ConvRank::Conversion;
            return c;
        }
        if (T->isConst) return implicitConversion(decay(at), T, isNullPointerConstant(arg));
        c.why = std::string("a non-const reference needs an lvalue of exactly type ") + q(T);
        return c;
    }
    TypePtr from = decay(at);
    if (isRecord(param) || isRecord(from)) {
        if (sameType(unqualified(param), from)) c.rank = ConvRank::Exact;
        else c.why = "no conversion between these types";
        return c;
    }
    return implicitConversion(from, param, isNullPointerConstant(arg));
}

TypePtr SemanticAnalyzer::checkCallArgs(const TypePtr &ft, const std::string &name, const std::vector<ASTNodePtr> &args,
                                        const ASTNode *at) {
    if (!ft || !isFunction(ft)) return errorType();
    size_t np = ft->params.size(), na = args.size();
    if (na < np || (na > np && !ft->variadic)) {
        error(at, "function '" + name + "' expects " + std::string(ft->variadic ? "at least " : "") + std::to_string(np) +
                      " argument" + (np == 1 ? "" : "s") + " but " + std::to_string(na) +
                      (na == 1 ? " was" : " were") + " provided",
              "argument-count");
    }
    for (size_t i = 0; i < na; ++i) {
        const ASTNodePtr &a = args[i];
        if (i < np) {
            Conversion c = argumentConversion(ft->params[i], a);
            if (c.rank == ConvRank::None) {
                error(a.get(), "type mismatch: argument " + std::to_string(i + 1) + " of '" + name + "' expects " +
                                   q(ft->params[i]) + " but got " + q(decay(a->semType)) +
                                   (c.why.empty() ? "" : " (" + c.why + ")"),
                      "argument-type");
            }
        } else if (isVoid(a->semType)) {
            error(a.get(), "argument " + std::to_string(i + 1) + " of '" + name + "' has type 'void'", "argument-type");
        }
    }
    return ft->ret;
}

SymbolPtr SemanticAnalyzer::resolveOverload(const std::string &name, const std::vector<SymbolPtr> &candidates,
                                            const std::vector<ASTNodePtr> &args, const ASTNode *at) {
    std::vector<SymbolPtr> fns;
    for (const auto &c : candidates) {
        if (c->kind == SymbolKind::Function) fns.push_back(c);
    }
    if (fns.empty()) return nullptr;
    if (fns.size() == 1) {
        checkCallArgs(fns[0]->type, name, args, at);
        return fns[0];
    }
    for (const auto &a : args) {
        if (isError(a->semType)) return nullptr; /* already reported; don't guess */
    }
    struct Viable {
        SymbolPtr s;
        std::vector<ConvRank> ranks;
    };
    std::vector<Viable> viable;
    for (const auto &f : fns) {
        const TypePtr &ft = f->type;
        if (args.size() < ft->params.size() || (args.size() > ft->params.size() && !ft->variadic)) continue;
        Viable v{f, {}};
        bool ok = true;
        for (size_t i = 0; i < args.size() && ok; ++i) {
            ConvRank r = i < ft->params.size() ? argumentConversion(ft->params[i], args[i]).rank : ConvRank::Ellipsis;
            ok = r != ConvRank::None;
            v.ranks.push_back(r);
        }
        if (ok) viable.push_back(v);
    }
    std::string argList;
    for (size_t i = 0; i < args.size(); ++i) argList += (i ? ", " : "") + typeToString(decay(args[i]->semType));
    std::string candidatesText;
    for (const auto &f : fns) candidatesText += (candidatesText.empty() ? "" : ", ") + describeSignature(f);
    if (viable.empty()) {
        error(at, "no matching function for call to '" + name + "(" + argList + ")'; candidates are: " + candidatesText,
              "no-matching-overload");
        return nullptr;
    }
    auto better = [](const Viable &a, const Viable &b) { /* a strictly better than b */
        bool strictly = false;
        for (size_t i = 0; i < a.ranks.size(); ++i) {
            if (a.ranks[i] > b.ranks[i]) return false;
            if (a.ranks[i] < b.ranks[i]) strictly = true;
        }
        return strictly;
    };
    for (const auto &v : viable) {
        bool best = std::all_of(viable.begin(), viable.end(),
                                [&](const Viable &w) { return w.s == v.s || better(v, w); });
        if (best) return v.s;
    }
    error(at, "call to overloaded function '" + name + "(" + argList + ")' is ambiguous; candidates are: " + candidatesText,
          "ambiguous-call");
    return nullptr;
}

TypePtr SemanticAnalyzer::call(const ASTNodePtr &n) {
    const ASTNodePtr &callee = n->children[0];
    std::vector<ASTNodePtr> args(n->children.begin() + 1, n->children.end());
    for (const auto &a : args) expr(a);

    auto finish = [&](const SymbolPtr &chosen, const std::string &name) -> TypePtr {
        if (!chosen) return errorType();
        callee->symbol = chosen;
        callee->semType = chosen->type;
        n->symbol = chosen;
        chosen->useCount++;
        TypePtr r = callResult(chosen->type);
        if (isReference(r)) {
            n->isLValue = true;
            r = r->elem;
        }
        (void)name;
        return r;
    };

    if (callee->kind == ASTKind::Identifier) {
        const std::string &name = callee->label;
        Lookup l = st.lookup(name);
        if (l.symbols.empty() && hoistFunction(name)) l = st.lookup(name);
        if (l.symbols.empty()) {
            SymbolPtr tag = st.lookupTag(name);
            if (tag && tag->record) { /* `Node(v)` inside class Node's own body */
                n->kind = ASTKind::ConstructExpr; /* it is one; TAC sees it as such */
                n->label = name;
                n->children.erase(n->children.begin());
                n->symbol = construct(tag->record.get(), args, callee.get());
                return recordType(tag->record);
            }
            error(callee.get(), "call to undeclared function '" + name + "'", "undeclared");
            return errorType();
        }
        if (l.symbols.front()->kind == SymbolKind::Function) {
            SymbolPtr chosen = resolveOverload(name, l.symbols, args, callee.get());
            if (chosen && l.viaRecord) {
                checkAccess(l.member, currentClass(), name, callee.get());
                FunctionCtx *f = fn();
                if (!chosen->isStatic && f && f->isStaticMethod) {
                    error(callee.get(), "call to non-static member function '" + name +
                                            "' from a static member function (there is no object)",
                          "this");
                } else if (!chosen->isStatic && f && f->isLambda && !f->defaultCapture) {
                    error(callee.get(), "calling member function '" + name +
                                            "' needs 'this', which a lambda with no capture-default does not capture",
                          "capture");
                }
            }
            return finish(chosen, name);
        }
    }

    TypePtr t;
    if (callee->kind == ASTKind::MemberExpr || callee->kind == ASTKind::ArrowExpr) {
        bool arrow = callee->kind == ASTKind::ArrowExpr;
        t = member(callee, arrow, /*calleePosition=*/true);
        if (isError(t)) return errorType();
        if (callee->symbol && callee->symbol->kind == SymbolKind::Function) {
            bool constObject;
            RecordInfo *rec = recordOfBase(callee->children[0]->semType, arrow, constObject);
            MemberLookup ml = lookupMember(rec, callee->label);
            return finish(resolveOverload(callee->label, ml.symbols, args, callee.get()), callee->label);
        }
        /* a field holding a function pointer or a lambda: called below */
    } else if (callee->kind == ASTKind::ScopeExpr && callee->children[0]->kind == ASTKind::Identifier &&
               st.lookupTag(callee->children[0]->label) && st.lookupTag(callee->children[0]->label)->record &&
               [&] {
                   MemberLookup ml = lookupMember(st.lookupTag(callee->children[0]->label)->record.get(), callee->label);
                   return !ml.symbols.empty() && ml.symbols.front()->kind == SymbolKind::Function;
               }()) {
        RecordInfo *rec = st.lookupTag(callee->children[0]->label)->record.get();
        MemberLookup ml = lookupMember(rec, callee->label);
        checkAccess(ml, rec, callee->label, callee.get());
        SymbolPtr chosen = resolveOverload(callee->label, ml.symbols, args, callee.get());
        RecordInfo *cls = currentClass();
        bool viaThis = cls && (cls == rec || isDerivedFrom(cls, rec)) && !(fn() && fn()->isStaticMethod);
        if (chosen && !chosen->isStatic && !viaThis) {
            error(callee.get(), "call to non-static member function '" + rec->tag + "::" + callee->label +
                                    "' without an object",
                  "member-access");
        }
        return finish(chosen, callee->label);
    } else {
        t = expr(callee);
    }

    /* calling through a value: function pointer, lambda, `(*fp)(...)` */
    callee->semType = t;
    if (isError(t)) return errorType();
    TypePtr vt = decay(t);
    std::string name = callee->kind == ASTKind::Identifier ? callee->label
                       : (callee->kind == ASTKind::MemberExpr || callee->kind == ASTKind::ArrowExpr) ? callee->label
                                                                                                    : "the callee";
    if (isRecord(vt)) { /* a function object: operator() */
        std::vector<ASTNodePtr> operands{callee};
        operands.insert(operands.end(), args.begin(), args.end());
        TypePtr overloaded;
        if (overloadedOperator(n, "()", operands, overloaded)) return overloaded;
    }
    if (isFunctionPointer(vt)) return checkCallArgs(vt->elem, name, args, n.get());
    if (isClosure(vt)) return checkCallArgs(functionType(vt->ret, vt->params, false), name, args, n.get());
    error(callee.get(), "called object of type " + q(t) + " is not a function, function pointer or lambda", "not-callable");
    return errorType();
}

/* ---------------- printf / scanf / memory / file builtins ---------------- */

namespace {
struct Builtin {
    TypePtr ret;
    std::vector<TypePtr> params;
    bool variadic = false;
    int formatIndex = -1;  /* printf-family / scanf-family format argument */
    bool scanf = false;    /* trailing arguments must be pointers */
};

const Builtin *builtinFor(const std::string &name) {
    static std::map<std::string, Builtin> table = [] {
        TypePtr cstr = pointerTo(qualified(charType(), true, false));
        TypePtr str = pointerTo(charType());
        TypePtr vp = pointerTo(voidType());
        TypePtr cvp = pointerTo(qualified(voidType(), true, false));
        TypePtr file = pointerTo(opaqueType("FILE"));
        TypePtr i = intType();
        std::map<std::string, Builtin> m;
        m["printf"] = {i, {cstr}, true, 0, false};
        m["scanf"] = {i, {cstr}, true, 0, true};
        m["malloc"] = {vp, {i}, false, -1, false};
        m["calloc"] = {vp, {i, i}, false, -1, false};
        m["realloc"] = {vp, {vp, i}, false, -1, false};
        m["free"] = {voidType(), {vp}, false, -1, false};
        m["fopen"] = {file, {cstr, cstr}, false, -1, false};
        m["fclose"] = {i, {file}, false, -1, false};
        m["fread"] = {i, {vp, i, i, file}, false, -1, false};
        m["fwrite"] = {i, {cvp, i, i, file}, false, -1, false};
        m["fprintf"] = {i, {file, cstr}, true, 1, false};
        m["fscanf"] = {i, {file, cstr}, true, 1, true};
        m["fgets"] = {str, {str, i, file}, false, -1, false};
        m["fputs"] = {i, {cstr, file}, false, -1, false};
        m["feof"] = {i, {file}, false, -1, false};
        return m;
    }();
    auto it = table.find(name);
    return it == table.end() ? nullptr : &it->second;
}
} // namespace

TypePtr SemanticAnalyzer::builtinCall(const ASTNodePtr &n) {
    if (n->label.compare(0, 3, "va_") == 0) return varargBuiltin(n);
    std::vector<ASTNodePtr> args(n->children.begin(), n->children.end());
    for (const auto &a : args) expr(a);
    const Builtin *b = builtinFor(n->label);
    if (!b) return errorType();
    TypePtr ft = functionType(b->ret, b->params, b->variadic);
    checkCallArgs(ft, n->label, args, n.get());
    if (b->scanf) {
        for (size_t i = b->params.size(); i < args.size(); ++i) {
            TypePtr t = decay(args[i]->semType);
            if (isError(t)) continue;
            if (!isPointer(t) || isFunction(t->elem)) {
                error(args[i].get(), "argument " + std::to_string(i + 1) + " of '" + n->label +
                                         "' must be a pointer to the object to store into, not " + q(t) +
                                         " (did you forget '&'?)",
                      "scanf-argument");
            } else if (t->elem->isConst) {
                error(args[i].get(), "argument " + std::to_string(i + 1) + " of '" + n->label +
                                         "' points to read-only storage " + q(t),
                      "scanf-argument");
            }
        }
    }
    if (b->formatIndex >= 0) checkFormat(n->label, args, static_cast<size_t>(b->formatIndex), b->scanf, n.get());
    return b->ret;
}

/* Light printf/scanf format checking (warnings, like gcc -Wformat): the
   number of conversions must match the number of arguments, and printf
   conversions must receive a compatible kind of value. Only literal
   format strings are inspected. */
/* printf / scanf format checking (gcc's -Wformat). A printf argument
   in the `...` part arrives after the default argument promotions
   (Papaspyrou's argPromote: char/short/bool -> int, float -> double), so
   `%d` takes any of those and `%f` a float; the length modifier then
   fixes the width (`%ld` long, `%lld` long long, `%zu` size_t). A scanf
   argument is a pointer to exactly the converted type: `%f` a float *,
   `%lf` a double *, `%d` an int *. Signedness differences (`%u` with an
   int) are not reported, as in gcc without -Wformat-signedness. */
namespace {
struct FormatConv {
    char c;
    std::string len; /* "", "hh", "h", "l", "ll", "L", "z", "j", "t" */
};
/* the integer kind a length modifier names (MIPS32: size_t is unsigned int) */
TypeKind lengthKind(const std::string &len, bool promoted) {
    if (len == "l") return TypeKind::Long;
    if (len == "ll" || len == "j" || len == "q") return TypeKind::LongLong;
    if (len == "z" || len == "t") return TypeKind::Int;
    if (!promoted && len == "h") return TypeKind::Short;
    if (!promoted && len == "hh") return TypeKind::Char;
    return TypeKind::Int; /* printf: hh / h values arrive promoted to int */
}
std::string kindName(TypeKind k) {
    switch (k) {
        case TypeKind::Char: return "char";
        case TypeKind::Short: return "short";
        case TypeKind::Long: return "long";
        case TypeKind::LongLong: return "long long";
        default: return "int";
    }
}
} // namespace

void SemanticAnalyzer::checkFormat(const std::string &fnName, const std::vector<ASTNodePtr> &args, size_t fmtIndex,
                                   bool isScanf, const ASTNode *at) {
    if (args.size() <= fmtIndex || args[fmtIndex]->kind != ASTKind::StringLiteral) return;
    std::vector<int> f = decodeEscapes(stripQuotes(args[fmtIndex]->label));
    std::vector<FormatConv> convs; /* one entry per consumed argument; '*' = int width */
    for (size_t i = 0; i < f.size(); ++i) {
        if (f[i] != '%') continue;
        if (++i >= f.size()) break;
        if (f[i] == '%') continue;
        bool suppressed = false;
        if (isScanf && f[i] == '*') suppressed = true, ++i;
        while (i < f.size() && std::strchr("-+ #0", f[i])) ++i;
        if (i < f.size() && f[i] == '*' && !isScanf) convs.push_back({'*', ""}), ++i;
        while (i < f.size() && std::isdigit(f[i])) ++i;
        if (i < f.size() && f[i] == '.') {
            ++i;
            if (i < f.size() && f[i] == '*' && !isScanf) convs.push_back({'*', ""}), ++i;
            while (i < f.size() && std::isdigit(f[i])) ++i;
        }
        std::string len;
        while (i < f.size() && std::strchr("hlLqjzt", f[i])) len += static_cast<char>(f[i++]);
        if (i >= f.size()) break;
        char c = static_cast<char>(f[i]);
        if (!std::strchr("diouxXeEfFgGaAcspn[", c)) {
            warning(args[fmtIndex].get(), std::string("invalid conversion specifier '%") + c + "' in format string",
                    "format");
            continue;
        }
        if (c == '[') { /* scanf scanset */
            while (i < f.size() && f[i] != ']') ++i;
        }
        if (!suppressed) convs.push_back({c, len});
    }
    size_t provided = args.size() - fmtIndex - 1;
    if (convs.size() != provided) {
        warning(at, "format string of '" + fnName + "' expects " + std::to_string(convs.size()) + " argument" +
                        (convs.size() == 1 ? "" : "s") + " after the format, but " + std::to_string(provided) +
                        (provided == 1 ? " was" : " were") + " provided",
                "format");
        return;
    }
    for (size_t k = 0; k < convs.size(); ++k) {
        const ASTNodePtr &a = args[fmtIndex + 1 + k];
        TypePtr t = decay(a->semType);
        if (isError(t)) continue;
        const FormatConv &cv = convs[k];
        char c = cv.c;
        std::string spec = std::string("%") + (c == '*' ? "*" : cv.len + c);
        std::string argNo = std::to_string(fmtIndex + 2 + k);
        auto complain = [&](const std::string &want) {
            warning(a.get(), "format '" + spec + "' expects " + want + ", but argument " + argNo + " has type " + q(t),
                    "format");
        };
        if (isScanf) { /* pointer-ness is already enforced as an error; check what it points to */
            if (!isPointer(t) || c == 'p') continue;
            TypePtr e = unqualified(t->elem);
            if (std::strchr("diouxXn", c)) {
                TypeKind want = lengthKind(cv.len, false);
                TypePtr norm = e->kind == TypeKind::Enum ? intType() : e;
                if (!isIntegral(norm) || norm->kind != want || norm->kind == TypeKind::Bool)
                    complain("'" + kindName(want) + " *'");
            } else if (std::strchr("eEfFgGaA", c)) {
                bool wantDouble = cv.len == "l" || cv.len == "L";
                if (e->kind != (wantDouble ? TypeKind::Double : TypeKind::Float))
                    complain(wantDouble ? "'double *'" : "'float *' (use '%l" + std::string(1, c) + "' for a double)");
            } else if (c == 's' || c == 'c' || c == '[') {
                if (e->kind != TypeKind::Char) complain("'char *'");
            }
            continue;
        }
        TypePtr p = isIntegral(t) ? integerPromotion(t) : t->kind == TypeKind::Float ? doubleType() : t; /* argPromote */
        if (c == '*' || std::strchr("dioxXuc", c)) {
            if (!isIntegral(t)) {
                complain("an integer");
                continue;
            }
            if (c == '*' || c == 'c') continue;
            TypeKind want = lengthKind(cv.len, true);
            TypeKind have = p->kind == TypeKind::Enum ? TypeKind::Int : p->kind;
            if (have != want) complain("'" + kindName(want) + "'");
        } else if (std::strchr("eEfFgGaA", c)) {
            if (!isFloating(t)) complain("a floating-point value ('double')");
        } else if (c == 's') {
            if (!(isPointer(t) && t->elem->kind == TypeKind::Char)) complain("a string (char *)");
        } else if (!isPointer(t)) { /* p, n */
            complain("a pointer");
        }
    }
}

/* ---------------- lambdas ---------------- */

TypePtr SemanticAnalyzer::lambda(const ASTNodePtr &n) {
    FunctionCtx ctx;
    ctx.isLambda = true;
    ctx.name = "lambda";
    ctx.cls = nullptr;

    /* capture list, as the parser spelled it: "x, &y" / "&" / "=" */
    std::string caps = n->label;
    std::vector<std::string> items;
    for (size_t start = 0; start < caps.size();) {
        size_t comma = caps.find(',', start);
        std::string item = caps.substr(start, comma == std::string::npos ? std::string::npos : comma - start);
        item.erase(0, item.find_first_not_of(' '));
        item.erase(item.find_last_not_of(' ') + 1);
        if (!item.empty()) items.push_back(item);
        if (comma == std::string::npos) break;
        start = comma + 1;
    }
    for (const auto &item : items) {
        if (item == "&" || item == "=") {
            if (ctx.defaultCapture) error(n.get(), "a lambda can have only one capture-default", "capture");
            ctx.defaultCapture = item[0];
            continue;
        }
        if (item == "this") {
            RecordInfo *cls = currentClass();
            FunctionCtx *outer = fn();
            if (!cls || (outer && outer->isStaticMethod)) {
                error(n.get(), "'this' cannot be captured outside a non-static member function", "capture");
            } else if (ctx.capturesThis) {
                error(n.get(), "'this' can appear only once in a capture list", "capture");
            }
            ctx.capturesThis = true;
            continue;
        }
        bool byRef = item[0] == '&';
        std::string name = byRef ? item.substr(1) : item;
        if (ctx.captures.count(name)) {
            error(n.get(), "'" + name + "' can appear only once in a capture list", "capture");
            continue;
        }
        Lookup l = st.lookup(name);
        if (l.symbols.empty()) {
            error(n.get(), "undeclared identifier '" + name + "' in the capture list", "undeclared");
            continue;
        }
        const SymbolPtr &s = l.symbols.front();
        if (s->kind != SymbolKind::Variable && s->kind != SymbolKind::Parameter) {
            error(n.get(), "'" + name + "' in the capture list does not name a variable", "capture");
            continue;
        }
        if (l.viaRecord || (s->storage != Storage::Local && s->storage != Storage::Param)) {
            error(n.get(), "'" + name + "' cannot be captured because it does not have automatic storage duration",
                  "capture");
            continue;
        }
        s->useCount++;
        ctx.captures[name] = LambdaCapture{byRef};
    }

    int sid = st.enterScope(ScopeKind::Lambda, "lambda");
    ctx.lambdaScope = sid;
    if (n->typeExpr) {
        ctx.isMutable = n->typeExpr->isMutable;
        if (n->typeExpr->hasExplicitReturn) { /* `-> T`: returns are checked against T */
            ASTTypeExpr retExpr = *n->typeExpr;
            retExpr.isFunction = false;
            retExpr.params.clear();
            retExpr.isVariadic = false;
            ctx.explicitReturn = true;
            ctx.ret = resolveType(retExpr, n.get(), false).type;
            if (!ctx.ret) ctx.ret = errorType();
            ctx.name = "lambda";
        }
    }
    std::vector<TypePtr> params =
        n->typeExpr ? resolveParams(*n->typeExpr, n.get()) : std::vector<TypePtr>{};
    std::vector<ASTNodePtr> paramNodes;
    for (const auto &c : n->children) {
        if (c->kind == ASTKind::ParamDecl) paramNodes.push_back(c);
    }
    size_t named = 0;
    for (size_t i = 0; i < params.size(); ++i) {
        ASTTypeExprPtr pte = n->typeExpr && i < n->typeExpr->params.size() ? n->typeExpr->params[i] : nullptr;
        SymbolPtr ps = makeParamSymbol(pte, params[i], n.get());
        if (ps->name.empty()) continue;
        if (!st.lookupLocal(ps->name).empty()) {
            error(ps->line, ps->column, "redefinition of parameter '" + ps->name + "'", "redeclaration");
            continue;
        }
        st.declare(ps);
        if (named < paramNodes.size()) {
            paramNodes[named]->symbol = ps;
            paramNodes[named]->semType = ps->type;
            ++named;
        }
    }
    ASTNodePtr body = n->children.empty() ? nullptr : n->children.back();
    if (body && body->kind == ASTKind::CompoundStmt) {
        collectLabels(body, ctx);
        fns.push_back(ctx);
        blockItems(body);
        ctx = fns.back();
        fns.pop_back();
    }
    st.exitScope();
    TypePtr ret = ctx.explicitReturn ? ctx.ret : ctx.deducedRet ? ctx.deducedRet : voidType();
    bool hasCaptures = !ctx.captures.empty() || ctx.defaultCapture || ctx.capturesThis;
    return closureType(ret, params, hasCaptures,
                       "lambda at line " + displayLine(n->line) + ":" + std::to_string(n->column));
}

} // namespace sem
