#include "types/types.hpp"

#include <algorithm>
#include <functional>

#include "symbol_table/symbol_table.hpp"

namespace sem {

/* ---------------- construction ---------------- */

static TypePtr make(const Type &t) { return std::make_shared<const Type>(t); }

TypePtr basicType(TypeKind k, bool isUnsigned) {
    Type t;
    t.kind = k;
    t.isUnsigned = isUnsigned;
    return make(t);
}

TypePtr errorType() { static TypePtr t = basicType(TypeKind::Error); return t; }
TypePtr voidType() { static TypePtr t = basicType(TypeKind::Void); return t; }
TypePtr boolType() { static TypePtr t = basicType(TypeKind::Bool); return t; }
TypePtr charType() { static TypePtr t = basicType(TypeKind::Char); return t; }
TypePtr intType() { static TypePtr t = basicType(TypeKind::Int); return t; }
TypePtr unsignedIntType() { static TypePtr t = basicType(TypeKind::Int, true); return t; }
TypePtr doubleType() { static TypePtr t = basicType(TypeKind::Double); return t; }

TypePtr pointerTo(const TypePtr &t) {
    Type p;
    p.kind = TypeKind::Pointer;
    p.elem = t;
    return make(p);
}

TypePtr referenceTo(const TypePtr &t) {
    Type p;
    p.kind = TypeKind::Reference;
    p.elem = t;
    return make(p);
}

TypePtr arrayOf(const TypePtr &elem, long long size) {
    Type a;
    a.kind = TypeKind::Array;
    a.elem = elem;
    a.arraySize = size;
    return make(a);
}

TypePtr functionType(const TypePtr &ret, const std::vector<TypePtr> &params, bool variadic) {
    Type f;
    f.kind = TypeKind::Function;
    f.ret = ret;
    f.params = params;
    f.variadic = variadic;
    return make(f);
}

TypePtr recordType(const std::shared_ptr<RecordInfo> &r) {
    Type t;
    t.kind = TypeKind::Record;
    t.record = r;
    return make(t);
}

TypePtr opaqueType(const std::string &name) {
    Type t;
    t.kind = TypeKind::Opaque;
    t.name = name;
    return make(t);
}

TypePtr qualified(const TypePtr &t, bool isConst) {
    if (!t || !isConst || t->isConst) return t;
    Type q = *t;
    q.isConst = true;
    return make(q);
}

TypePtr unqualified(const TypePtr &t) {
    if (!t || !t->isConst) return t;
    Type q = *t;
    q.isConst = false;
    return make(q);
}

/* ---------------- classification ---------------- */

static TypeKind kindOf(const TypePtr &t) { return t ? t->kind : TypeKind::Error; }

bool isError(const TypePtr &t) { return kindOf(t) == TypeKind::Error; }
bool isVoid(const TypePtr &t) { return kindOf(t) == TypeKind::Void; }
bool isBool(const TypePtr &t) { return kindOf(t) == TypeKind::Bool; }
bool isIntegral(const TypePtr &t) {
    switch (kindOf(t)) {
        case TypeKind::Bool: case TypeKind::Char: case TypeKind::Short: case TypeKind::Int:
        case TypeKind::Long: case TypeKind::LongLong:
            return true;
        default:
            return false;
    }
}
bool isFloating(const TypePtr &t) {
    return kindOf(t) == TypeKind::Float || kindOf(t) == TypeKind::Double;
}
bool isArithmetic(const TypePtr &t) { return isIntegral(t) || isFloating(t); }
bool isPointer(const TypePtr &t) { return kindOf(t) == TypeKind::Pointer; }
bool isReference(const TypePtr &t) { return kindOf(t) == TypeKind::Reference; }
bool isArray(const TypePtr &t) { return kindOf(t) == TypeKind::Array; }
bool isFunction(const TypePtr &t) { return kindOf(t) == TypeKind::Function; }
bool isRecord(const TypePtr &t) { return kindOf(t) == TypeKind::Record; }
bool isScalar(const TypePtr &t) { return isArithmetic(t) || isPointer(t); }
bool isVoidPointer(const TypePtr &t) { return isPointer(t) && isVoid(t->elem); }

bool isComplete(const TypePtr &t) {
    switch (kindOf(t)) {
        case TypeKind::Void: case TypeKind::Function:
            return false;
        case TypeKind::Record:
            return t->record && t->record->complete;
        case TypeKind::Array:
            return t->arraySize >= 0 && isComplete(t->elem);
        default:
            return true;
    }
}

/* ---------------- relations ---------------- */

bool sameType(const TypePtr &a, const TypePtr &b, bool exactQualifiers) {
    if (a == b) return true;
    if (!a || !b || a->kind != b->kind) return false;
    if (exactQualifiers && a->isConst != b->isConst) return false;
    switch (a->kind) {
        case TypeKind::Char: case TypeKind::Short: case TypeKind::Int:
        case TypeKind::Long: case TypeKind::LongLong:
            return a->isUnsigned == b->isUnsigned;
        case TypeKind::Pointer: case TypeKind::Reference:
            return sameType(a->elem, b->elem, true);
        case TypeKind::Array:
            return a->arraySize == b->arraySize && sameType(a->elem, b->elem, true);
        case TypeKind::Function:
            if (a->variadic != b->variadic || a->params.size() != b->params.size()) return false;
            if (!sameType(a->ret, b->ret, true)) return false;
            for (size_t i = 0; i < a->params.size(); ++i) {
                if (!sameType(a->params[i], b->params[i], false)) return false;
            }
            return true;
        case TypeKind::Record:
            return a->record == b->record;
        case TypeKind::Opaque:
            return a->name == b->name;
        default:
            return true; /* Void, Bool, Float, Double, Error */
    }
}

bool isDerivedFrom(const RecordInfo *derived, const RecordInfo *base) {
    if (!derived || !base) return false;
    for (const auto &b : derived->bases) {
        if (b.record.get() == base || isDerivedFrom(b.record.get(), base)) return true;
    }
    return false;
}

bool sameParameterLists(const TypePtr &a, const TypePtr &b) {
    if (!a || !b || !isFunction(a) || !isFunction(b)) return false;
    if (a->variadic != b->variadic || a->params.size() != b->params.size()) return false;
    for (size_t i = 0; i < a->params.size(); ++i) {
        if (!sameType(a->params[i], b->params[i])) return false;
    }
    return true;
}

TypePtr decay(const TypePtr &t) {
    if (!t) return errorType();
    switch (t->kind) {
        case TypeKind::Reference: return decay(t->elem);
        case TypeKind::Array: return pointerTo(t->elem);
        case TypeKind::Function: return t; /* not a value: no function pointers */
        default: return unqualified(t);
    }
}

TypePtr integerPromotion(const TypePtr &t) {
    switch (kindOf(t)) {
        case TypeKind::Bool: case TypeKind::Char: case TypeKind::Short:
            return intType();
        default:
            return unqualified(t);
    }
}

static int integerRank(TypeKind k) {
    switch (k) {
        case TypeKind::LongLong: return 3;
        case TypeKind::Long: return 2;
        default: return 1;
    }
}

TypePtr usualArithmetic(const TypePtr &a, const TypePtr &b) {
    if (isError(a) || isError(b)) return errorType();
    if (kindOf(a) == TypeKind::Double || kindOf(b) == TypeKind::Double) return doubleType();
    if (kindOf(a) == TypeKind::Float || kindOf(b) == TypeKind::Float) return basicType(TypeKind::Float);
    TypePtr pa = integerPromotion(a), pb = integerPromotion(b);
    int ra = integerRank(pa->kind), rb = integerRank(pb->kind);
    const TypePtr &hi = ra >= rb ? pa : pb;
    const TypePtr &lo = ra >= rb ? pb : pa;
    bool isUnsigned = hi->isUnsigned || (lo->isUnsigned && sizeOf(lo) == sizeOf(hi));
    return basicType(hi->kind, isUnsigned);
}

Conversion implicitConversion(const TypePtr &fromIn, const TypePtr &toIn, bool fromIsNullConstant) {
    Conversion c;
    if (isError(fromIn) || isError(toIn)) { c.rank = ConvRank::Exact; return c; }
    TypePtr from = unqualified(fromIn);
    TypePtr to = unqualified(isReference(toIn) ? toIn->elem : toIn);

    if (isVoid(to) || isVoid(from)) {
        c.why = isVoid(from) ? "a void expression has no value" : "cannot convert to 'void'";
        return c;
    }
    if (sameType(from, to)) { c.rank = ConvRank::Exact; return c; }

    if (isBool(to)) {
        if (isArithmetic(from) || isPointer(from)) c.rank = ConvRank::Conversion;
        else c.why = "no conversion to 'bool'";
        return c;
    }
    if (isArithmetic(from) && isArithmetic(to)) {
        bool promotion = (to->kind == TypeKind::Int && !to->isUnsigned &&
                          (from->kind == TypeKind::Bool || from->kind == TypeKind::Char ||
                           from->kind == TypeKind::Short)) ||
                         (from->kind == TypeKind::Float && to->kind == TypeKind::Double);
        c.rank = promotion ? ConvRank::Promotion : ConvRank::Conversion;
        return c;
    }
    if (isPointer(to)) {
        if (fromIsNullConstant) { c.rank = ConvRank::Conversion; return c; }
        if (isPointer(from)) {
            const TypePtr &fp = from->elem, &tp = to->elem;
            bool related = sameType(unqualified(fp), unqualified(tp)) ||
                           isVoid(tp) || isVoid(fp) ||
                           (isRecord(fp) && isRecord(tp) &&
                            isDerivedFrom(fp->record.get(), tp->record.get()));
            if (!related) {
                c.why = "incompatible pointer types";
                return c;
            }
            if (fp->isConst && !tp->isConst) {
                c.why = "conversion discards 'const' qualifier";
                return c;
            }
            if (sameType(unqualified(fp), unqualified(tp))) {
                c.rank = fp->isConst != tp->isConst
                             ? ConvRank::Promotion /* qualification added */
                             : ConvRank::Exact;
            } else {
                c.rank = ConvRank::Conversion;
            }
            return c;
        }
        if (isIntegral(from)) c.why = "incompatible integer to pointer conversion";
        else c.why = "no conversion to a pointer type";
        return c;
    }
    if (isArithmetic(to) && isPointer(from)) {
        c.why = "incompatible pointer to integer conversion";
        return c;
    }
    c.why = "no viable conversion";
    return c;
}

std::string checkCast(const TypePtr &fromIn, const TypePtr &to) {
    if (isError(fromIn) || isError(to) || isVoid(to)) return "";
    TypePtr from = unqualified(fromIn);
    if (isArray(to)) return "cannot cast to an array type";
    if (isFunction(to)) return "cannot cast to a function type";
    if (isVoid(from)) return "a void expression cannot be cast to a non-void type";
    if (isRecord(to) || isRecord(from)) {
        if (sameType(from, to)) return "";
        return "cannot cast between a struct/class type and another type";
    }
    if (isArithmetic(from) && isArithmetic(to)) return "";
    if (isPointer(from) && isPointer(to)) return "";
    if (isPointer(from) && isIntegral(to)) return "";
    if (isIntegral(from) && isPointer(to)) return "";
    if (implicitConversion(from, to, false).rank != ConvRank::None) return "";
    if (isPointer(from) || isPointer(to)) return "a pointer can only be cast to/from an integer or another pointer";
    return "invalid cast";
}

/* ---------------- layout (MIPS32) ---------------- */

long long sizeOf(const TypePtr &t) {
    switch (kindOf(t)) {
        case TypeKind::Bool: case TypeKind::Char: return 1;
        case TypeKind::Short: return 2;
        case TypeKind::Int: case TypeKind::Long: case TypeKind::Float:
        case TypeKind::Pointer: case TypeKind::Reference:
            return 4;
        case TypeKind::LongLong: case TypeKind::Double: return 8;
        case TypeKind::Array: {
            long long e = sizeOf(t->elem);
            return (t->arraySize < 0 || e < 0) ? -1 : t->arraySize * e;
        }
        case TypeKind::Record:
            return (t->record && t->record->complete) ? t->record->size : -1;
        case TypeKind::Opaque:
            return 4; /* va_list: a cursor into the argument area */
        default:
            return -1;
    }
}

int alignOf(const TypePtr &t) {
    switch (kindOf(t)) {
        case TypeKind::Array: return alignOf(t->elem);
        case TypeKind::Record: return t->record ? t->record->align : 1;
        default: {
            long long s = sizeOf(t);
            return s > 0 ? static_cast<int>(std::min<long long>(s, 8)) : 1;
        }
    }
}

static long long alignUp(long long v, int a) { return a > 1 ? (v + a - 1) / a * a : v; }

void layoutRecord(RecordInfo &r) {
    long long offset = 0;
    int align = 1;
    for (const auto &b : r.bases) { /* base sub-objects first, in order */
        if (!b.record || !b.record->complete) continue;
        offset = alignUp(offset, b.record->align);
        offset += b.record->size;
        align = std::max(align, b.record->align);
    }
    for (auto &f : r.fields) {
        if (f->storage != Storage::Member) continue; /* static members live elsewhere */
        long long fs = std::max(0LL, sizeOf(f->type));
        int fa = alignOf(f->type);
        align = std::max(align, fa);
        offset = alignUp(offset, fa);
        f->offset = offset;
        offset += fs;
    }
    long long size = offset;
    if (size == 0) size = 1; /* no zero-sized objects (C++ rule) */
    r.size = alignUp(size, align);
    r.align = align;
}

/* ---------------- printing ---------------- */

std::string accessName(Access a) {
    switch (a) {
        case Access::Public: return "public";
        case Access::Protected: return "protected";
        case Access::Private: return "private";
        case Access::NoAccess: return "inaccessible";
    }
    return "?";
}

std::string recordKindName(RecordKind k) {
    switch (k) {
        case RecordKind::Struct: return "struct";
        case RecordKind::Class: return "class";
    }
    return "?";
}

static std::string baseName(const TypePtr &t) {
    std::string u = (t->isUnsigned ? "unsigned " : "");
    switch (t->kind) {
        case TypeKind::Error: return "<error>";
        case TypeKind::Void: return "void";
        case TypeKind::Bool: return "bool";
        case TypeKind::Char: return u + "char";
        case TypeKind::Short: return u + "short";
        case TypeKind::Int: return t->isUnsigned ? "unsigned int" : "int";
        case TypeKind::Long: return u + "long";
        case TypeKind::LongLong: return u + "long long";
        case TypeKind::Float: return "float";
        case TypeKind::Double: return "double";
        case TypeKind::Record:
            return t->record ? recordDisplayName(*t->record) : "struct ?";
        case TypeKind::Opaque: return t->name;
        default: return "?";
    }
}

static std::string quals(const TypePtr &t) {
    std::string q;
    if (t->isConst) q += "const ";
    return q;
}

static std::string paramList(const TypePtr &f) {
    std::string s = "(";
    for (size_t i = 0; i < f->params.size(); ++i) {
        if (i) s += ", ";
        s += typeToString(f->params[i]);
    }
    if (f->variadic) s += f->params.empty() ? "..." : ", ...";
    if (f->params.empty() && !f->variadic) s += "void";
    return s + ")";
}

/* declarator-style printing, inside-out, as C spells types */
static std::string spell(const TypePtr &t, const std::string &inner) {
    if (!t) return "<error>";
    switch (t->kind) {
        case TypeKind::Pointer: case TypeKind::Reference: {
            std::string in = t->kind == TypeKind::Pointer ? "*" : "&";
            if (t->isConst) in += " const";
            if (!inner.empty()) in += (t->isConst ? " " : "") + inner;
            if (isArray(t->elem) || isFunction(t->elem)) in = "(" + in + ")";
            return spell(t->elem, in);
        }
        case TypeKind::Array:
            return spell(t->elem, inner + "[" + (t->arraySize >= 0 ? std::to_string(t->arraySize) : "") + "]");
        case TypeKind::Function:
            return spell(t->ret, inner + paramList(t));
        default: {
            std::string b = quals(t) + baseName(t);
            if (inner.empty()) return b;
            return b + (inner[0] == '[' ? "" : " ") + inner;
        }
    }
}

std::string typeToString(const TypePtr &t) { return spell(t, ""); }

/* ---------------- integer constants in their own type ---------------- */

int integerBits(const TypePtr &t) {
    if (!t) return 0;
    switch (t->kind) {
        case TypeKind::Bool: return 1;
        case TypeKind::Char: return 8;
        case TypeKind::Short: return 16;
        case TypeKind::Int: case TypeKind::Long: case TypeKind::Pointer: return 32;
        case TypeKind::LongLong: return 64;
        default: return 0;
    }
}

bool isUnsignedInteger(const TypePtr &t) {
    return t && (t->isUnsigned || t->kind == TypeKind::Bool || t->kind == TypeKind::Pointer);
}

long long wrapToType(long long v, const TypePtr &t) {
    int bits = integerBits(t);
    if (bits == 0 || bits == 64) return v;
    if (t->kind == TypeKind::Bool) return v != 0;
    unsigned long long mask = (1ULL << bits) - 1, u = static_cast<unsigned long long>(v) & mask;
    if (!isUnsignedInteger(t) && (u >> (bits - 1))) u |= ~mask; /* sign-extend */
    return static_cast<long long>(u);
}

bool fitsInType(long long v, const TypePtr &from, const TypePtr &t) {
    int bits = integerBits(t);
    if (bits == 0) return true;
    bool fromUnsigned64 = integerBits(from) == 64 && isUnsignedInteger(from);
    if (t->kind == TypeKind::Bool) return true;
    if (fromUnsigned64 && v < 0) { /* above LLONG_MAX */
        return bits == 64 && isUnsignedInteger(t);
    }
    if (bits == 64) return isUnsignedInteger(t) ? v >= 0 : true;
    long long lo = isUnsignedInteger(t) ? 0 : -(1LL << (bits - 1));
    long long hi = isUnsignedInteger(t) ? static_cast<long long>((1ULL << bits) - 1) : (1LL << (bits - 1)) - 1;
    return v >= lo && v <= hi;
}

std::string constantToString(long long v, const TypePtr &t) {
    if (integerBits(t) == 64 && isUnsignedInteger(t)) return std::to_string(static_cast<unsigned long long>(v));
    return std::to_string(v);
}

std::string recordDisplayName(const RecordInfo &r) {
    return r.typedefName.empty() ? recordKindName(r.kind) + " " + r.tag : r.typedefName;
}

/* ---------------- member lookup ---------------- */

static Access weaker(Access a, Access b) { return static_cast<int>(a) >= static_cast<int>(b) ? a : b; }

MemberLookup lookupMember(RecordInfo *r, const std::string &name) {
    MemberLookup out;
    if (!r) return out;
    auto it = r->members.find(name);
    if (it != r->members.end() && !it->second.empty()) {
        out.symbols = it->second;
        out.declaringRecord = r;
        out.access = it->second.front()->access;
        return out;
    }
    for (const auto &b : r->bases) {
        MemberLookup sub = lookupMember(b.record.get(), name);
        if (sub.symbols.empty()) continue;
        /* a base's private member is inaccessible in the derived class;
           otherwise the inheritance access caps it (C++ rule) */
        sub.access = sub.access == Access::Private || sub.access == Access::NoAccess
                         ? Access::NoAccess
                         : weaker(sub.access, b.access);
        if (out.symbols.empty()) {
            out = sub;
        } else if (out.declaringRecord != sub.declaringRecord) {
            out.ambiguous = true;
        }
    }
    return out;
}

} // namespace sem
