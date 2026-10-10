/* TAC for expressions: E.place is the Operand each function returns,
   E.code is what it emits on the way. */
#include <cstdlib>

#include "irgen.h"

namespace tac {

using sem::RecordInfo;
using sem::TypeKind;
using sem::TypePtr;

static RecordInfo *recordOf(const TypePtr &tIn) {
    TypePtr t = strip(tIn);
    return t && sem::isRecord(t) ? t->record.get() : nullptr;
}

bool baseOffset(const RecordInfo *derived, const RecordInfo *base, long long &offset) {
    if (!derived || !base) return false;
    if (derived == base) { offset = 0; return true; }
    long long at = 0; /* base sub-objects come first, in order (layoutRecord) */
    for (const auto &b : derived->bases) {
        if (!b.record || !b.record->complete) continue;
        at = alignUp(at, b.record->align);
        long long inner = 0;
        if (baseOffset(b.record.get(), base, inner)) { offset = at + inner; return true; }
        at += b.record->size;
    }
    return false;
}

static int widthOf(Cls c) {
    switch (c) {
        case Cls::Bool: case Cls::Char: case Cls::UChar: return 1;
        case Cls::Short: case Cls::UShort: return 2;
        case Cls::Int: case Cls::UInt: case Cls::Ptr: case Cls::Float: return 4;
        case Cls::LLong: case Cls::ULLong: case Cls::Double: return 8;
        default: return 0;
    }
}

static bool isRelational(const std::string &op) {
    return op == "==" || op == "!=" || op == "<" || op == ">" || op == "<=" || op == ">=";
}

static bool binaryOp(const std::string &op, Op &out) {
    if (op == "+") out = Op::Add;
    else if (op == "-") out = Op::Sub;
    else if (op == "*") out = Op::Mul;
    else if (op == "/") out = Op::Div;
    else if (op == "%") out = Op::Mod;
    else if (op == "&") out = Op::BitAnd;
    else if (op == "|") out = Op::BitOr;
    else if (op == "^") out = Op::BitXor;
    else if (op == "<<") out = Op::Shl;
    else if (op == ">>") out = Op::Shr;
    else return false;
    return true;
}

/* ---------------- the slides' helpers ---------------- */

int Generator::emit(Quad q) {
    q.line = curLine;
    fn->quads.push_back(q);
    return static_cast<int>(fn->quads.size()) - 1;
}

Operand Generator::newTemp(const TypePtr &t) {
    TypePtr type = sem::unqualified(t);
    fn->temps.push_back(type);
    Operand o;
    o.kind = Operand::Temp;
    o.temp = static_cast<int>(fn->temps.size());
    o.type = type;
    return o;
}

void Generator::backpatch(const List &l, int target) {
    for (int i : l) fn->quads[i].target = target;
}

int Generator::emitGoto(int target) {
    Quad q;
    q.op = Op::Goto;
    q.target = target;
    return emit(q);
}

Operand Generator::emitBinary(Op op, const Operand &a, const Operand &b, const TypePtr &type, const std::string &note) {
    Quad q;
    q.op = op;
    q.a = a;
    q.b = b;
    q.r = newTemp(type);
    q.cls = classOf(type);
    q.note = note;
    emit(q);
    return q.r;
}

void Generator::emitAssign(const Operand &dst, const Operand &src) {
    Quad q;
    q.op = Op::Assign;
    q.r = dst;
    q.a = src;
    q.cls = classOf(dst.type);
    emit(q);
}

Operand Generator::icon(long long v, const TypePtr &t) {
    Operand o;
    o.kind = Operand::IntConst;
    o.type = t ? sem::unqualified(t) : sem::intType();
    o.ival = sem::isIntegral(o.type) ? sem::wrapToType(v, o.type) : v;
    return o;
}

Operand Generator::fcon(double v, const TypePtr &t) {
    Operand o;
    o.kind = Operand::FloatConst;
    o.type = sem::unqualified(t);
    o.fval = classOf(o.type) == Cls::Float ? static_cast<float>(v) : v;
    return o;
}

Operand Generator::var(sem::Symbol *s) {
    Operand o;
    o.kind = Operand::Var;
    o.sym = s;
    o.type = s->type;
    return o;
}

Operand Generator::strOperand(const ASTNodePtr &n) {
    auto it = stringIds.find(n->label);
    if (it == stringIds.end()) {
        it = stringIds.emplace(n->label, static_cast<int>(prog.strings.size())).first;
        prog.strings.push_back(n->label);
    }
    Operand o;
    o.kind = Operand::Str;
    o.str = it->second;
    o.type = sem::pointerTo(sem::charType());
    return o;
}

Operand Generator::thisOperand() {
    if (fn->thisSym) return var(fn->thisSym);
    return icon(0, sem::pointerTo(sem::voidType()));
}

RecordInfo *Generator::currentClass() const {
    return fn && fn->sym ? fn->sym->ownerRecord : nullptr;
}

/* ---------------- conversions (Lecture 26: inttoreal) ---------------- */

Operand Generator::convert(const Operand &vIn, const TypePtr &toIn) {
    if (!toIn || vIn.isNone()) return vIn;
    TypePtr to = sem::unqualified(strip(toIn));
    Operand v = vIn;
    TypePtr from = v.type ? strip(v.type) : sem::intType();
    if (sem::isArray(from)) from = sem::pointerTo(from->elem);
    Cls f = classOf(from), t = classOf(to);
    if (t == Cls::Void || f == Cls::Void) return v;
    if (t == Cls::Block || f == Cls::Block) { v.type = to; return v; }

    /* Derived * -> Base *: the base sub-object may not be at offset 0 */
    if (sem::isPointer(from) && sem::isPointer(to) && sem::isRecord(from->elem) && sem::isRecord(to->elem) &&
        from->elem->record != to->elem->record) {
        long long off = 0;
        if (baseOffset(from->elem->record.get(), to->elem->record.get(), off) && off != 0) {
            Operand r = newTemp(to); /* r = p; if p != null, r = p + offset */
            emitAssign(r, v);
            Quad isNull;
            isNull.op = Op::IfRel;
            isNull.a = v;
            isNull.b = icon(0, from);
            isNull.relop = "==";
            isNull.cls = Cls::Ptr;
            int skip = emit(isNull);
            Quad add;
            add.op = Op::Add;
            add.a = v;
            add.b = icon(off);
            add.r = r;
            add.cls = Cls::Ptr;
            emit(add);
            backpatch(makelist(skip), nextQuad());
            return r;
        }
        v.type = to;
        return v;
    }
    if (v.kind == Operand::IntConst) { /* a constant is simply written in the new type */
        long long val = v.ival;
        if (isFloatCls(t)) {
            bool big = sem::integerBits(from) == 64 && sem::isUnsignedInteger(from);
            return fcon(big ? static_cast<double>(static_cast<unsigned long long>(val)) : static_cast<double>(val), to);
        }
        if (t == Cls::Bool) return icon(val != 0, to);
        Operand c = icon(val, to);
        if (!sem::isIntegral(to)) c.ival = val; /* a pointer constant */
        return c;
    }
    if (v.kind == Operand::FloatConst) {
        if (isFloatCls(t)) return fcon(v.fval, to);
        if (t == Cls::Bool) return icon(v.fval != 0, to);
        return icon(static_cast<long long>(v.fval), to);
    }
    if (f == t) { v.type = to; return v; }
    if (t == Cls::Bool) { /* any scalar -> 0 / 1 */
        Operand r = newTemp(to);
        Quad q;
        q.op = Op::IfRel;
        q.a = v;
        q.b = isFloatCls(f) ? fcon(0, from) : icon(0, from);
        q.relop = "!=";
        q.cls = f;
        int test = emit(q);
        emitAssign(r, icon(0, to));
        int skip = emitGoto();
        backpatch(makelist(test), nextQuad());
        emitAssign(r, icon(1, to));
        backpatch(makelist(skip), nextQuad());
        return r;
    }
    /* same bits, different reading: int <-> unsigned <-> pointer */
    if (isIntegerCls(f) && isIntegerCls(t) && widthOf(f) == widthOf(t)) { v.type = to; return v; }
    Quad q;
    q.op = Op::Conv;
    q.a = v;
    q.r = newTemp(to);
    q.cls = t;
    q.from = f;
    emit(q);
    return q.r;
}

Operand Generator::promoteVariadic(const Operand &v) {
    switch (classOf(v.type)) { /* C's default argument promotions */
        case Cls::Float: return convert(v, sem::doubleType());
        case Cls::Bool: case Cls::Char: case Cls::UChar: case Cls::Short: case Cls::UShort:
            return convert(v, sem::intType());
        default: return v;
    }
}

/* ---------------- addresses (Lecture 26: base + i * w) ---------------- */

Operand Generator::pointerAdd(const Operand &p, const Operand &byteOffset, bool subtract) {
    if (byteOffset.kind == Operand::IntConst && byteOffset.ival == 0) return p;
    Quad q;
    q.op = subtract ? Op::Sub : Op::Add;
    q.a = p;
    q.b = byteOffset;
    q.r = newTemp(p.type);
    q.cls = Cls::Ptr;
    emit(q);
    return q.r;
}

Operand Generator::scaled(const Operand &index, long long width, const std::string &note) {
    Operand i = convert(index, sem::intType());
    if (i.kind == Operand::IntConst) return icon(i.ival * width);
    if (width == 1) return i;
    return emitBinary(Op::Mul, i, icon(width), sem::intType(), note);
}

Generator::LValue Generator::addOffset(LValue lv, const Operand &off, const TypePtr &type) {
    lv.type = type;
    switch (lv.kind) {
        case LValue::Direct:
            lv.kind = LValue::Indexed;
            lv.off = off;
            break;
        case LValue::Indexed:
            if (lv.off.kind == Operand::IntConst && off.kind == Operand::IntConst) lv.off = icon(lv.off.ival + off.ival);
            else if (off.kind == Operand::IntConst && off.ival == 0) break;
            else if (lv.off.kind == Operand::IntConst && lv.off.ival == 0) lv.off = off;
            else lv.off = emitBinary(Op::Add, lv.off, off, sem::intType());
            break;
        case LValue::Deref:
            if (off.kind == Operand::IntConst) {
                lv.disp += off.ival;
            } else {
                Operand p = lv.disp ? pointerAdd(lv.base, icon(lv.disp)) : lv.base;
                lv.disp = 0;
                lv.base = pointerAdd(p, off);
            }
            break;
    }
    return lv;
}

Generator::LValue Generator::member(LValue lv, long long offset, const TypePtr &type) {
    return addOffset(lv, icon(offset), type);
}

Operand Generator::address(const LValue &lv) {
    TypePtr pt = sem::pointerTo(lv.type);
    switch (lv.kind) {
        case LValue::Direct: {
            Quad q;
            q.op = Op::AddrOf;
            q.a = lv.base;
            q.r = newTemp(pt);
            emit(q);
            return q.r;
        }
        case LValue::Indexed: {
            Quad q;
            q.op = Op::AddrOf;
            q.a = lv.base;
            q.r = newTemp(pt);
            emit(q);
            return pointerAdd(q.r, lv.off);
        }
        case LValue::Deref: {
            Operand p = pointerAdd(lv.base, icon(lv.disp));
            p.type = pt;
            return p;
        }
    }
    return {};
}

Operand Generator::load(const LValue &lv) {
    if (sem::isArray(lv.type)) { /* an array used as a value is the address of its first element */
        Operand p = address(lv);
        p.type = sem::pointerTo(lv.type->elem);
        return p;
    }
    switch (lv.kind) {
        case LValue::Direct: {
            Operand o = lv.base;
            o.type = lv.type;
            return o;
        }
        case LValue::Indexed: {
            Quad q;
            q.op = Op::IndexLoad;
            q.a = lv.base;
            q.b = lv.off;
            q.r = newTemp(lv.type);
            q.cls = classOf(lv.type);
            emit(q);
            return q.r;
        }
        case LValue::Deref: {
            Quad q;
            q.op = Op::Load;
            q.a = pointerAdd(lv.base, icon(lv.disp));
            q.r = newTemp(lv.type);
            q.cls = classOf(lv.type);
            emit(q);
            return q.r;
        }
    }
    return {};
}

void Generator::store(const LValue &lv, const Operand &v) {
    switch (lv.kind) {
        case LValue::Direct: {
            Operand dst = lv.base;
            dst.type = lv.type;
            emitAssign(dst, v);
            break;
        }
        case LValue::Indexed: {
            Quad q;
            q.op = Op::IndexStore;
            q.a = lv.base;
            q.b = lv.off;
            q.r = v;
            q.cls = classOf(lv.type);
            emit(q);
            break;
        }
        case LValue::Deref: {
            Quad q;
            q.op = Op::Store;
            q.a = pointerAdd(lv.base, icon(lv.disp));
            q.r = v;
            q.cls = classOf(lv.type);
            emit(q);
            break;
        }
    }
}

/* ---------------- lvalues ---------------- */

bool Generator::isOverloaded(const ASTNodePtr &n) const {
    switch (n->kind) {
        case ASTKind::BinaryExpr: case ASTKind::UnaryExpr: case ASTKind::PostfixOpExpr:
        case ASTKind::AssignExpr: case ASTKind::IndexExpr:
            return n->symbol && n->symbol->kind == sem::SymbolKind::Function && !n->symbol->isConstructor;
        default:
            return false;
    }
}

bool Generator::isLValueKind(const ASTNodePtr &n) const {
    switch (n->kind) {
        case ASTKind::Identifier: case ASTKind::MemberExpr: case ASTKind::ArrowExpr: case ASTKind::ScopeExpr:
            return true;
        case ASTKind::IndexExpr:
            return !isOverloaded(n);
        case ASTKind::UnaryExpr:
            return n->label == "*" && !isOverloaded(n);
        case ASTKind::TernaryExpr:
            return n->isLValue; /* c ? a : b with two lvalues names one of them */
        default:
            return false;
    }
}

Generator::LValue Generator::lvalue(const ASTNodePtr &n) {
    LValue lv;
    lv.type = strip(n->semType);
    switch (n->kind) {
        case ASTKind::Identifier:
        case ASTKind::ScopeExpr: {
            sem::Symbol *s = n->symbol.get();
            if (!s) break;
            if (s->kind == sem::SymbolKind::Field && s->storage == sem::Storage::Member) {
                long long off = 0; /* an implicit this->field */
                baseOffset(currentClass(), s->ownerRecord, off);
                lv.kind = LValue::Deref;
                lv.base = thisOperand();
                lv.disp = off + s->offset;
                return lv;
            }
            if (sem::isReference(s->type)) { /* a reference holds the address of what it names */
                lv.kind = LValue::Deref;
                lv.base = var(s);
                lv.base.type = sem::pointerTo(s->type->elem);
                return lv;
            }
            lv.kind = LValue::Direct;
            lv.base = var(s);
            return lv;
        }
        case ASTKind::MemberExpr: {
            sem::Symbol *s = n->symbol.get();
            if (s && s->storage == sem::Storage::Static) {
                lv.kind = LValue::Direct;
                lv.base = var(s);
                return lv;
            }
            LValue base = lvalueOrTemp(n->children[0]);
            long long off = 0;
            if (s) baseOffset(recordOf(base.type), s->ownerRecord, off);
            return member(base, off + (s ? s->offset : 0), lv.type);
        }
        case ASTKind::ArrowExpr: {
            sem::Symbol *s = n->symbol.get();
            if (s && s->storage == sem::Storage::Static) {
                lv.kind = LValue::Direct;
                lv.base = var(s);
                return lv;
            }
            Operand p = rvalue(n->children[0]);
            long long off = 0;
            if (s && p.type && sem::isPointer(p.type)) baseOffset(recordOf(p.type->elem), s->ownerRecord, off);
            lv.kind = LValue::Deref;
            lv.base = p;
            lv.disp = off + (s ? s->offset : 0);
            return lv;
        }
        case ASTKind::IndexExpr:
            if (!isOverloaded(n)) return indexLValue(n);
            break;
        case ASTKind::UnaryExpr:
            if (n->label == "*" && !isOverloaded(n)) {
                lv.kind = LValue::Deref;
                lv.base = rvalue(n->children[0]);
                return lv;
            }
            break;
        case ASTKind::TernaryExpr:
            if (n->isLValue) { /* p = c ? &a : &b, and the lvalue is *p */
                Operand p = newTemp(sem::pointerTo(lv.type));
                List trueList, falseList;
                cond(n->children[0], trueList, falseList);
                backpatch(trueList, nextQuad());
                emitAssign(p, address(lvalue(n->children[1])));
                int skip = emitGoto();
                backpatch(falseList, nextQuad());
                emitAssign(p, address(lvalue(n->children[2])));
                backpatch(makelist(skip), nextQuad());
                lv.kind = LValue::Deref;
                lv.base = p;
                return lv;
            }
            break;
        default:
            break;
    }
    return lvalueOrTemp(n);
}

/* an object to take a member or the address of: the lvalue itself, what
   a reference-returning call refers to, or a temporary holding the value */
Generator::LValue Generator::lvalueOrTemp(const ASTNodePtr &n) {
    if (isLValueKind(n)) return lvalue(n);
    LValue lv;
    lv.type = strip(n->semType);
    Operand v;
    if (n->kind == ASTKind::CallExpr) v = callExpr(n, false);
    else if (isOverloaded(n)) v = overloaded(n);
    else v = rvalue(n);
    if (v.type && sem::isReference(v.type)) {
        lv.kind = LValue::Deref;
        lv.base = v;
        lv.base.type = sem::pointerTo(v.type->elem);
        return lv;
    }
    if (v.kind != Operand::Temp && v.kind != Operand::Var) {
        Operand t = newTemp(lv.type);
        emitAssign(t, v);
        v = t;
    }
    lv.kind = LValue::Direct;
    lv.base = v;
    return lv;
}

/* A[i1][i2]...: the slides' row-major formula, ((i1 * n2) + i2) * w */
Generator::LValue Generator::indexLValue(const ASTNodePtr &n) {
    std::vector<ASTNodePtr> indices;
    ASTNodePtr node = n;
    while (node->kind == ASTKind::IndexExpr && !isOverloaded(node) && sem::isArray(strip(node->children[0]->semType)) &&
           node->children[0]->kind != ASTKind::StringLiteral) { /* "abc"[i] goes through the literal's address */
        indices.insert(indices.begin(), node->children[1]);
        node = node->children[0];
    }
    if (indices.empty()) { /* p[i] through a pointer: *(p + i * w) */
        ASTNodePtr base = n->children[0], index = n->children[1];
        TypePtr bt = sem::decay(base->semType);
        if (!sem::isPointer(bt)) std::swap(base, index); /* i[p] means p[i] */
        Operand p = rvalue(base);
        TypePtr elem = strip(n->semType);
        Operand off = scaled(rvalue(index), std::max(1LL, sem::sizeOf(elem)));
        LValue lv;
        lv.kind = LValue::Deref;
        lv.type = elem;
        if (off.kind == Operand::IntConst) {
            lv.base = p;
            lv.disp = off.ival;
        } else {
            lv.base = pointerAdd(p, off);
        }
        return lv;
    }
    LValue base = lvalueOrTemp(node);
    TypePtr t = strip(node->semType)->elem;
    Operand acc = convert(rvalue(indices[0]), sem::intType());
    for (size_t k = 1; k < indices.size(); ++k) {
        long long nk = t->arraySize;
        std::string dim = "(n" + std::to_string(k + 1) + " = " + std::to_string(nk) + ")";
        if (acc.kind == Operand::IntConst) acc = icon(acc.ival * nk);
        else acc = emitBinary(Op::Mul, acc, icon(nk), sem::intType(), dim);
        Operand ik = convert(rvalue(indices[k]), sem::intType());
        if (acc.kind == Operand::IntConst && ik.kind == Operand::IntConst) acc = icon(acc.ival + ik.ival);
        else if (acc.kind == Operand::IntConst && acc.ival == 0) acc = ik;
        else if (!(ik.kind == Operand::IntConst && ik.ival == 0)) acc = emitBinary(Op::Add, acc, ik, sem::intType());
        t = t->elem;
    }
    long long w = std::max(1LL, sem::sizeOf(t));
    Operand off = scaled(acc, w, "(w = " + std::to_string(w) + ")");
    return addOffset(base, off, t);
}

/* ---------------- values ---------------- */

Operand Generator::rvalue(const ASTNodePtr &n, bool discard) {
    if (!n) return {};
    if (n->line) curLine = n->line;
    if (isOverloaded(n)) {
        Operand r = overloaded(n);
        if (r.type && sem::isReference(r.type)) {
            LValue lv;
            lv.kind = LValue::Deref;
            lv.base = r;
            lv.base.type = sem::pointerTo(r.type->elem);
            lv.type = r.type->elem;
            return discard ? Operand() : load(lv);
        }
        return r;
    }
    switch (n->kind) {
        case ASTKind::IntLiteral: case ASTKind::CharLiteral: case ASTKind::BoolLiteral: case ASTKind::SizeofExpr:
            return icon(n->constValue, n->semType);
        case ASTKind::FloatLiteral:
            return fcon(std::strtod(n->label.c_str(), nullptr), n->semType);
        case ASTKind::StringLiteral:
            return strOperand(n);
        case ASTKind::Identifier: case ASTKind::MemberExpr: case ASTKind::ArrowExpr: case ASTKind::IndexExpr:
        case ASTKind::ScopeExpr: {
            if (discard && n->kind == ASTKind::Identifier) return {};
            return load(lvalue(n));
        }
        case ASTKind::ThisExpr: return thisOperand();
        case ASTKind::BinaryExpr: return binary(n);
        case ASTKind::UnaryExpr: return unary(n, discard);
        case ASTKind::PostfixOpExpr: return incDec(n->children[0], n->label == "++", false, discard);
        case ASTKind::AssignExpr: return assignment(n, discard);
        case ASTKind::TernaryExpr: return ternary(n, discard);
        case ASTKind::CommaExpr:
            rvalue(n->children[0], true);
            return rvalue(n->children[1], discard);
        case ASTKind::CallExpr: {
            Operand r = callExpr(n, discard);
            if (r.type && sem::isReference(r.type)) {
                LValue lv;
                lv.kind = LValue::Deref;
                lv.base = r;
                lv.base.type = sem::pointerTo(r.type->elem);
                lv.type = r.type->elem;
                return discard ? Operand() : load(lv);
            }
            return r;
        }
        case ASTKind::BuiltinCallExpr: return builtin(n, discard);
        case ASTKind::CastExpr: {
            Operand v = rvalue(n->children[0], sem::isVoid(n->semType));
            if (sem::isVoid(n->semType)) return {};
            return convert(v, n->semType);
        }
        case ASTKind::ConstructExpr: return construct(n);
        case ASTKind::NewExpr: return newExpr(n);
        case ASTKind::DeleteExpr:
            deleteExpr(n);
            return {};
        default:
            return {};
    }
}

Operand Generator::binary(const ASTNodePtr &n) {
    const std::string &op = n->label;
    if (op == "&&" || op == "||" || isRelational(op)) return boolValue(n);
    const ASTNodePtr &L = n->children[0], &R = n->children[1];
    TypePtr lt = sem::decay(L->semType), rt = sem::decay(R->semType), T = n->semType;
    Op o = Op::Add;
    if (!binaryOp(op, o)) return {};

    if ((op == "+" || op == "-") && (sem::isPointer(lt) || sem::isPointer(rt))) {
        Operand a = rvalue(L), b = rvalue(R);
        if (sem::isPointer(lt) && sem::isPointer(rt)) { /* p - q: bytes apart / element size */
            Quad q;
            q.op = Op::Sub;
            q.a = a;
            q.b = b;
            q.r = newTemp(sem::intType());
            q.cls = Cls::Ptr;
            emit(q);
            long long w = std::max(1LL, sem::sizeOf(lt->elem));
            return w > 1 ? emitBinary(Op::Div, q.r, icon(w), sem::intType()) : q.r;
        }
        bool ptrLeft = sem::isPointer(lt);
        const Operand &p = ptrLeft ? a : b, &i = ptrLeft ? b : a;
        long long w = std::max(1LL, sem::sizeOf((ptrLeft ? lt : rt)->elem));
        return pointerAdd(p, scaled(i, w), op == "-");
    }
    Operand a = convert(rvalue(L), T);
    Operand b = convert(rvalue(R), (o == Op::Shl || o == Op::Shr) ? sem::intType() : T);
    return emitBinary(o, a, b, T);
}

Operand Generator::unary(const ASTNodePtr &n, bool discard) {
    const std::string &op = n->label;
    const ASTNodePtr &c = n->children[0];
    if (op == "++(pre)" || op == "--(pre)") return incDec(c, op[0] == '+', true, discard);
    if (op == "!") return boolValue(n);
    if (op == "&") {
        Operand a = address(lvalueOrTemp(c));
        a.type = n->semType;
        return a;
    }
    if (op == "*") return load(lvalue(n));
    Operand v = convert(rvalue(c), n->semType);
    if (op == "+") return v;
    Quad q;
    q.op = op == "-" ? Op::Neg : Op::BitNot;
    q.a = v;
    q.r = newTemp(n->semType);
    q.cls = classOf(n->semType);
    emit(q);
    return q.r;
}

Operand Generator::incDec(const ASTNodePtr &operand, bool increment, bool prefix, bool discard) {
    LValue lv = lvalue(operand);
    TypePtr T = sem::unqualified(lv.type);
    Operand cur = load(lv);
    Operand old = cur;
    if (!prefix && !discard && cur.kind == Operand::Var) { /* the value before the update */
        old = newTemp(T);
        emitAssign(old, cur);
    }
    Operand updated;
    if (sem::isPointer(T)) {
        updated = pointerAdd(cur, icon(std::max(1LL, sem::sizeOf(T->elem))), !increment);
    } else {
        TypePtr P = sem::isIntegral(T) ? sem::integerPromotion(T) : T;
        Operand one = sem::isFloating(P) ? fcon(1.0, P) : icon(1, P);
        updated = convert(emitBinary(increment ? Op::Add : Op::Sub, convert(cur, P), one, P), T);
    }
    store(lv, updated);
    return prefix ? updated : old;
}

Operand Generator::assignment(const ASTNodePtr &n, bool discard) {
    (void)discard;
    const std::string &op = n->label;
    const ASTNodePtr &L = n->children[0], &R = n->children[1];
    LValue lv = lvalue(L);
    if (op == "=") {
        Operand v = sem::isRecord(lv.type) ? rvalue(R) : convert(rvalue(R), lv.type);
        store(lv, v);
        return v;
    }
    TypePtr lt = sem::unqualified(lv.type), rt = sem::decay(R->semType);
    std::string bop = op.substr(0, op.size() - 1);
    Op o = Op::Add;
    if (!binaryOp(bop, o)) return {};
    Operand cur = load(lv);
    Operand result;
    if (sem::isPointer(lt)) {
        result = pointerAdd(cur, scaled(rvalue(R), std::max(1LL, sem::sizeOf(lt->elem))), bop == "-");
    } else if (o == Op::Shl || o == Op::Shr) {
        TypePtr P = sem::integerPromotion(lt);
        Operand a = convert(cur, P);
        result = emitBinary(o, a, convert(rvalue(R), sem::intType()), P);
    } else {
        TypePtr C = sem::usualArithmetic(lt, rt);
        Operand a = convert(cur, C);
        result = emitBinary(o, a, convert(rvalue(R), C), C);
    }
    Operand v = convert(result, lt);
    store(lv, v);
    return v;
}

Operand Generator::ternary(const ASTNodePtr &n, bool discard) {
    const ASTNodePtr &C = n->children[0], &A = n->children[1], &B = n->children[2];
    TypePtr T = n->semType;
    bool isVoid = sem::isVoid(T) || discard;
    Operand t = isVoid ? Operand() : newTemp(T);
    List trueList, falseList;
    cond(C, trueList, falseList);
    backpatch(trueList, nextQuad());
    /* a class object picked by value is a temporary of its own; whatever
       else a branch creates dies inside that branch, the only place it exists */
    bool object = !isVoid && sem::isRecord(T) && !n->isLValue;
    auto branch = [&](const ASTNodePtr &e) {
        size_t mark = temporaries.size();
        Operand v = object ? copyOf(e, T, false) : rvalue(e, isVoid);
        if (!isVoid) emitAssign(t, sem::isRecord(T) ? v : convert(v, T));
        keep(v);
        destroyTemporaries(mark);
    };
    branch(A);
    int skip = emitGoto();
    backpatch(falseList, nextQuad());
    branch(B);
    backpatch(makelist(skip), nextQuad());
    return object ? temporary(t) : t;
}

/* ---------------- boolean expressions (Lecture 27) ---------------- */

/* `if a relop b goto _`: returns the index of the jump to backpatch */
int Generator::relJump(const ASTNodePtr &n) {
    const ASTNodePtr &L = n->children[0], &R = n->children[1];
    TypePtr lt = sem::decay(L->semType), rt = sem::decay(R->semType);
    TypePtr C = (sem::isArithmetic(lt) && sem::isArithmetic(rt)) ? sem::usualArithmetic(lt, rt)
                : sem::isPointer(lt) ? lt : rt;
    /* ponytail: a test's temporaries die before its jump, not at the end
       of the whole condition; `a(T(1)) && b(T(2))` destroys T(1) before T(2) is made */
    size_t mark = temporaries.size();
    Quad q;
    q.op = Op::IfRel;
    q.a = convert(rvalue(L), C);
    q.b = convert(rvalue(R), C);
    q.relop = n->label;
    q.cls = classOf(C);
    destroyTemporaries(mark);
    return emit(q);
}

/* control-flow translation: E.true and E.false are backpatch lists */
void Generator::cond(const ASTNodePtr &n, List &trueList, List &falseList) {
    if (n->line) curLine = n->line;
    if (!isOverloaded(n)) {
        if (n->kind == ASTKind::BinaryExpr && n->label == "&&") { /* E1.true = start of E2 */
            List leftTrue;
            cond(n->children[0], leftTrue, falseList);
            backpatch(leftTrue, nextQuad());
            cond(n->children[1], trueList, falseList);
            return;
        }
        if (n->kind == ASTKind::BinaryExpr && n->label == "||") { /* E1.false = start of E2 */
            List leftFalse;
            cond(n->children[0], trueList, leftFalse);
            backpatch(leftFalse, nextQuad());
            cond(n->children[1], trueList, falseList);
            return;
        }
        if (n->kind == ASTKind::UnaryExpr && n->label == "!") { /* swap the lists */
            cond(n->children[0], falseList, trueList);
            return;
        }
        if (n->kind == ASTKind::BinaryExpr && isRelational(n->label)) {
            trueList.push_back(relJump(n));
            falseList.push_back(emitGoto());
            return;
        }
    }
    if (n->kind == ASTKind::BoolLiteral || n->kind == ASTKind::IntLiteral || n->kind == ASTKind::CharLiteral) {
        (n->constValue ? trueList : falseList).push_back(emitGoto()); /* E -> true: goto E.true */
        return;
    }
    size_t mark = temporaries.size();
    Operand v = rvalue(n);
    TypePtr vt = v.type ? strip(v.type) : sem::intType();
    Quad q;
    q.op = Op::IfRel;
    q.a = v;
    q.b = isFloatCls(classOf(vt)) ? fcon(0, vt) : icon(0, vt);
    q.relop = "!=";
    q.cls = classOf(vt);
    destroyTemporaries(mark);
    trueList.push_back(emit(q));
    falseList.push_back(emitGoto());
}

/* a boolean used as a value: the slides' pattern
       if a relop b goto +3 ; t = 0 ; goto +2 ; t = 1                */
Operand Generator::boolValue(const ASTNodePtr &n) {
    Operand t = newTemp(sem::intType());
    List trueList, falseList;
    if (n->kind == ASTKind::BinaryExpr && isRelational(n->label) && !isOverloaded(n)) trueList.push_back(relJump(n));
    else cond(n, trueList, falseList);
    backpatch(falseList, nextQuad());
    emitAssign(t, icon(0));
    int skip = emitGoto();
    backpatch(trueList, nextQuad());
    emitAssign(t, icon(1));
    backpatch(makelist(skip), nextQuad());
    return t;
}

/* ---------------- calls (param / call) ---------------- */

Operand Generator::referenceTo(const ASTNodePtr &n, const TypePtr &elem) {
    bool refCall = (n->kind == ASTKind::CallExpr || isOverloaded(n)) && n->isLValue;
    TypePtr have = strip(n->semType);
    /* `const double &r = anInt;` cannot name the int: it gets a converted temporary */
    bool sameObject = sem::isRecord(have) || sem::sameType(sem::unqualified(have), sem::unqualified(elem));
    if (sameObject && (isLValueKind(n) || refCall || sem::isRecord(have))) {
        Operand a = address(lvalueOrTemp(n));
        return convert(a, sem::pointerTo(elem));
    }
    Operand t = newTemp(elem); /* a temporary the reference can name */
    emitAssign(t, convert(rvalue(n), elem));
    LValue lv;
    lv.kind = LValue::Direct;
    lv.base = t;
    lv.type = elem;
    return address(lv);
}

/* `rec`'s copy constructor rec(const rec &), if the class declares one */
static sem::Symbol *copyConstructor(RecordInfo *rec) {
    if (!rec) return nullptr;
    for (const auto &c : rec->constructors) {
        if (!c->type || c->type->params.size() != 1) continue;
        const TypePtr &p = c->type->params[0];
        if (sem::isReference(p) && sem::isRecord(p->elem) && p->elem->record.get() == rec) return c.get();
    }
    return nullptr;
}

/* an object that already exists (an lvalue), not one the expression creates */
bool Generator::isExisting(const ASTNodePtr &n) const {
    return isLValueKind(n) || ((n->kind == ASTKind::CallExpr || isOverloaded(n)) && n->isLValue);
}

/* ---------------- unnamed class objects ---------------- */

/* `t` is an object the expression created: it is destroyed at the end of
   the full expression unless something keeps it */
Operand Generator::temporary(const Operand &t) {
    if (t.kind == Operand::Temp && t.type && sem::isRecord(t.type) && needsDestruction(t.type)) temporaries.push_back(t);
    return t;
}

/* `t` became a variable, an element or the function's result: no destructor here */
void Generator::keep(const Operand &t) {
    for (size_t i = temporaries.size(); t.kind == Operand::Temp && i-- > 0;)
        if (temporaries[i].temp == t.temp) temporaries.erase(temporaries.begin() + i);
}

/* the end of a full expression: the last one made is destroyed first */
void Generator::destroyTemporaries(size_t from) {
    while (temporaries.size() > from) {
        LValue obj;
        obj.kind = LValue::Direct;
        obj.base = temporaries.back();
        obj.type = obj.base.type;
        temporaries.pop_back();
        destroyObject(obj);
    }
}

/* a class object passed or returned by value. An existing object is
   copied: by the copy constructor when the class has one, else as a
   block. A parameter's copy is destroyed after the call. An object the
   expression creates is used as it is, and so is the local that is the
   function's result (what C++ compilers do: copy elision). */
Operand Generator::copyOf(const ASTNodePtr &n, const TypePtr &type, bool returned) {
    sem::Symbol *ctor = copyConstructor(recordOf(type));
    bool result = returned && n->kind == ASTKind::Identifier && n->symbol.get() == resultObject;
    if (!isExisting(n) || result || (!ctor && (returned || !needsDestruction(type)))) return rvalue(n);
    Operand copy = newTemp(type);
    if (ctor) {
        LValue lv;
        lv.kind = LValue::Direct;
        lv.base = copy;
        lv.type = sem::unqualified(strip(type));
        Operand to = address(lv);
        call(ctor, to, {n}, {}, false);
    } else {
        emitAssign(copy, rvalue(n));
    }
    return returned ? copy : temporary(copy);
}

Operand Generator::argumentFor(const TypePtr &param, const ASTNodePtr &arg) {
    if (sem::isReference(param)) return referenceTo(arg, param->elem);
    if (sem::isRecord(param)) return copyOf(arg, param, false);
    return convert(rvalue(arg), param);
}

Operand Generator::call(sem::Symbol *callee, const Operand &thisArg, const std::vector<ASTNodePtr> &args,
                        const std::vector<Operand> &extraArgs, bool wantResult) {
    TypePtr ft = callee->type;
    std::vector<Operand> values; /* all arguments first: an argument may itself contain a call */
    for (size_t i = 0; i < args.size(); ++i) {
        if (ft && i < ft->params.size()) values.push_back(argumentFor(ft->params[i], args[i]));
        else values.push_back(promoteVariadic(rvalue(args[i])));
    }
    for (const auto &e : extraArgs) values.push_back(e);
    if (!thisArg.isNone()) {
        Quad p;
        p.op = Op::Param;
        p.a = thisArg;
        p.note = "(this)";
        emit(p);
    }
    for (const auto &v : values) {
        Quad p;
        p.op = Op::Param;
        p.a = v;
        emit(p);
    }
    Quad q;
    q.op = Op::Call;
    q.callee = callee;
    q.nargs = static_cast<int>(values.size()) + (thisArg.isNone() ? 0 : 1);
    TypePtr ret = ft ? ft->ret : nullptr;
    /* an object result is received even when it is not used: it must be destroyed */
    bool wanted = wantResult || (ret && needsDestruction(ret));
    if (wanted && ret && !sem::isVoid(ret) && !callee->isConstructor && !callee->isDestructor) q.r = newTemp(ret);
    if (!q.r.isNone()) q.r.type = ret; /* keeps `T &`: the caller dereferences */
    emit(q);
    return temporary(q.r);
}

/* the address a member function receives as `this`, adjusted to the
   class that declares it (a base sub-object may not start at offset 0) */
static long long thisAdjust(const RecordInfo *object, const sem::Symbol *method) {
    long long off = 0;
    if (object && method->ownerRecord) baseOffset(object, method->ownerRecord, off);
    return off;
}

Operand Generator::callExpr(const ASTNodePtr &n, bool discard) {
    sem::Symbol *f = n->symbol.get();
    if (!f || f->kind != sem::SymbolKind::Function) return {};
    const ASTNodePtr &callee = n->children[0];
    std::vector<ASTNodePtr> args(n->children.begin() + 1, n->children.end());
    Operand thisArg;
    if (f->ownerRecord && !f->isStatic) {
        if (callee->kind == ASTKind::MemberExpr) {
            LValue obj = lvalueOrTemp(callee->children[0]);
            thisArg = pointerAdd(address(obj), icon(thisAdjust(recordOf(obj.type), f)));
        } else if (callee->kind == ASTKind::ArrowExpr) {
            Operand p = rvalue(callee->children[0]);
            const RecordInfo *rec = p.type && sem::isPointer(p.type) ? recordOf(p.type->elem) : nullptr;
            thisArg = pointerAdd(p, icon(thisAdjust(rec, f)));
        } else if (callee->semType && sem::isFunction(callee->semType)) { /* an implicit this->f() */
            thisArg = pointerAdd(thisOperand(), icon(thisAdjust(currentClass(), f)));
        } else { /* a function object: obj(args) is obj.operator()(args) */
            LValue obj = lvalueOrTemp(callee);
            thisArg = pointerAdd(address(obj), icon(thisAdjust(recordOf(obj.type), f)));
        }
        thisArg.type = sem::pointerTo(sem::recordType(f->ownerRecord->shared_from_this()));
    }
    return call(f, thisArg, args, {}, !discard);
}

/* a + b, -a, a[i], a = b, a++ on a class: a call to operator<op> */
Operand Generator::overloaded(const ASTNodePtr &n) {
    sem::Symbol *f = n->symbol.get();
    std::vector<ASTNodePtr> operands(n->children.begin(), n->children.end());
    std::vector<Operand> extra;
    if (n->kind == ASTKind::PostfixOpExpr) extra.push_back(icon(0)); /* the dummy int of operator++(int) */
    Operand thisArg;
    if (f->ownerRecord && !f->isStatic) {
        LValue obj = lvalueOrTemp(operands[0]);
        thisArg = pointerAdd(address(obj), icon(thisAdjust(recordOf(obj.type), f)));
        thisArg.type = sem::pointerTo(sem::recordType(f->ownerRecord->shared_from_this()));
        operands.erase(operands.begin());
    }
    return call(f, thisArg, operands, extra, true);
}

Operand Generator::builtin(const ASTNodePtr &n, bool discard) {
    const std::string &name = n->label;
    const auto &args = n->children;
    if (name == "va_start" || name == "va_end") {
        Quad q;
        q.op = name == "va_start" ? Op::VaStart : Op::VaEnd;
        q.a = lvalue(args[0]).base;
        if (name == "va_start" && args.size() > 1) q.b = lvalue(args[1]).base;
        emit(q);
        return {};
    }
    if (name == "va_arg") {
        Quad q;
        q.op = Op::VaArg;
        q.a = lvalue(args[0]).base;
        q.r = newTemp(n->semType);
        q.cls = classOf(n->semType);
        emit(q);
        return q.r;
    }
    TypePtr i = sem::intType(), vp = sem::pointerTo(sem::voidType()), cstr = sem::pointerTo(sem::charType());
    std::vector<TypePtr> fixed;
    if (name == "printf" || name == "scanf") fixed = {cstr};
    else if (name == "malloc") fixed = {i};
    else if (name == "calloc") fixed = {i, i};
    else if (name == "realloc") fixed = {vp, i};
    else if (name == "free") fixed = {vp};
    std::vector<Operand> values;
    for (size_t k = 0; k < args.size(); ++k) {
        Operand v = rvalue(args[k]);
        values.push_back(k < fixed.size() ? convert(v, fixed[k]) : promoteVariadic(v));
    }
    for (const auto &v : values) {
        Quad p;
        p.op = Op::Param;
        p.a = v;
        emit(p);
    }
    Quad q;
    q.op = Op::Call;
    q.calleeName = name;
    q.nargs = static_cast<int>(values.size());
    if (!discard && n->semType && !sem::isVoid(n->semType)) q.r = newTemp(n->semType);
    emit(q);
    return q.r;
}

/* ---------------- objects ---------------- */

bool needsDestruction(const TypePtr &tIn) {
    TypePtr t = tIn;
    while (t && sem::isArray(t)) t = t->elem;
    RecordInfo *rec = t && sem::isRecord(t) ? t->record.get() : nullptr;
    if (!rec || !rec->complete) return false;
    if (rec->destructor) return true;
    for (const auto &b : rec->bases)
        if (b.record && needsDestruction(sem::recordType(b.record))) return true;
    for (const auto &f : rec->fields)
        if (f->storage == sem::Storage::Member && needsDestruction(f->type)) return true;
    return false;
}

bool Generator::needsConstruction(const TypePtr &tIn) {
    TypePtr t = tIn;
    while (t && sem::isArray(t)) t = t->elem;
    RecordInfo *rec = t && sem::isRecord(t) ? t->record.get() : nullptr;
    if (!rec || !rec->complete) return false;
    if (!rec->constructors.empty()) return true;
    for (const auto &b : rec->bases)
        if (b.record && needsConstruction(sem::recordType(b.record))) return true;
    for (const auto &f : rec->fields)
        if (f->storage == sem::Storage::Member && needsConstruction(f->type)) return true;
    return false;
}

/* base sub-objects, then members, in declaration order (C++ order) */
void Generator::constructSubobjects(const Operand &addr, RecordInfo *rec) {
    for (const auto &b : rec->bases) {
        if (!b.record || !needsConstruction(sem::recordType(b.record))) continue;
        long long off = 0;
        baseOffset(rec, b.record.get(), off);
        Operand p = pointerAdd(addr, icon(off));
        p.type = sem::pointerTo(sem::recordType(b.record));
        defaultConstruct(p, sem::recordType(b.record));
    }
    for (const auto &f : rec->fields) {
        if (f->storage != sem::Storage::Member || !needsConstruction(f->type)) continue;
        Operand p = pointerAdd(addr, icon(f->offset));
        p.type = sem::pointerTo(f->type);
        defaultConstruct(p, f->type);
    }
}

void Generator::defaultConstruct(const Operand &addr, const TypePtr &t) {
    if (!needsConstruction(t)) return;
    if (sem::isArray(t)) {
        long long w = std::max(1LL, sem::sizeOf(t->elem));
        for (long long i = 0; i < t->arraySize; ++i) {
            Operand p = pointerAdd(addr, icon(i * w));
            p.type = sem::pointerTo(t->elem);
            defaultConstruct(p, t->elem);
        }
        return;
    }
    RecordInfo *rec = t->record.get();
    for (const auto &c : rec->constructors) {
        if (c->type && c->type->params.empty()) {
            call(c.get(), addr, {}, {}, false);
            return;
        }
    }
    if (rec->constructors.empty()) constructSubobjects(addr, rec); /* the implicit default constructor */
}

void Generator::constructInto(const Operand &addr, RecordInfo *rec, sem::Symbol *ctor,
                              const std::vector<ASTNodePtr> &args) {
    /* T x(f()), T(f()): the object f made becomes this one, no copy */
    bool same = args.size() == 1 && !isExisting(args[0]) && recordOf(args[0]->semType) == rec;
    if (ctor && !(same && ctor == copyConstructor(rec))) {
        call(ctor, addr, args, {}, false);
        return;
    }
    if (args.size() == 1) { /* the implicit copy constructor: a memberwise copy */
        Quad q;
        q.op = Op::Store;
        q.a = addr;
        RecordInfo *from = recordOf(args[0]->semType);
        if (from && from != rec) { /* from a derived object: only its base sub-object */
            long long off = 0;
            baseOffset(from, rec, off);
            q.r = load(member(lvalueOrTemp(args[0]), off, sem::recordType(rec->shared_from_this())));
        } else {
            q.r = rvalue(args[0]);
            keep(q.r);
        }
        q.cls = Cls::Block;
        emit(q);
        return;
    }
    defaultConstruct(addr, sem::recordType(rec->shared_from_this()));
}

/* members in reverse order, then base sub-objects (C++ order) */
void Generator::destroySubobjects(const Operand &addr, RecordInfo *rec) {
    for (auto f = rec->fields.rbegin(); f != rec->fields.rend(); ++f) {
        if ((*f)->storage != sem::Storage::Member || !needsDestruction((*f)->type)) continue;
        TypePtr t = (*f)->type;
        long long count = 1;
        while (sem::isArray(t)) {
            count *= std::max(0LL, t->arraySize);
            t = t->elem;
        }
        long long w = std::max(1LL, sem::sizeOf(t));
        for (long long i = count; i-- > 0;) {
            Operand p = pointerAdd(addr, icon((*f)->offset + i * w));
            p.type = sem::pointerTo(t);
            destroy(p, t->record.get());
        }
    }
    for (auto b = rec->bases.rbegin(); b != rec->bases.rend(); ++b) {
        if (!b->record || !needsDestruction(sem::recordType(b->record))) continue;
        long long off = 0;
        baseOffset(rec, b->record.get(), off);
        Operand p = pointerAdd(addr, icon(off));
        p.type = sem::pointerTo(sem::recordType(b->record));
        destroy(p, b->record.get());
    }
}

void Generator::destroy(const Operand &addr, RecordInfo *rec) {
    if (!rec || !needsDestruction(sem::recordType(rec->shared_from_this()))) return;
    if (rec->destructor) call(rec->destructor.get(), addr, {}, {}, false); /* it destroys its own sub-objects */
    else destroySubobjects(addr, rec);
}

/* T(args): a temporary object, or for a non-class type a conversion */
Operand Generator::construct(const ASTNodePtr &n) {
    TypePtr T = n->semType;
    if (RecordInfo *rec = recordOf(T)) {
        Operand obj = newTemp(T);
        LValue lv;
        lv.kind = LValue::Direct;
        lv.base = obj;
        lv.type = T;
        constructInto(address(lv), rec, n->symbol.get(), n->children);
        return temporary(obj);
    }
    if (n->children.empty()) return isFloatCls(classOf(T)) ? fcon(0, T) : icon(0, T);
    return convert(rvalue(n->children[0]), T);
}

Operand Generator::newExpr(const ASTNodePtr &n) {
    TypePtr pt = n->semType;
    if (!pt || !sem::isPointer(pt)) return {};
    TypePtr target = pt->elem;
    ASTNodePtr init;
    for (const auto &c : n->children)
        if (c->kind == ASTKind::ConstructExpr) init = c;
    bool arrayNew = n->typeExpr && !n->typeExpr->arrayDims.empty() && !n->typeExpr->grouped;
    long long w = std::max(1LL, sem::sizeOf(target));
    Operand count, size = icon(w);
    bool counted = arrayNew && needsDestruction(target); /* delete[] must know how many to destroy */
    if (arrayNew) {
        count = convert(rvalue(n->typeExpr->arrayDims.front()), sem::intType());
        size = scaled(count, w);
        if (counted) size = size.kind == Operand::IntConst ? icon(size.ival + 8) : emitBinary(Op::Add, size, icon(8), sem::intType());
    }
    Quad p;
    p.op = Op::Param;
    p.a = size;
    emit(p);
    Quad q;
    q.op = Op::Call;
    q.calleeName = "malloc";
    q.nargs = 1;
    q.r = newTemp(pt);
    emit(q);
    Operand obj = q.r;
    if (counted) { /* [count][elements ...]: the pointer handed out is to the elements */
        Quad keep;
        keep.op = Op::Store;
        keep.a = obj;
        keep.r = count;
        keep.cls = Cls::Int;
        emit(keep);
        obj = pointerAdd(obj, icon(8));
    }

    RecordInfo *rec = recordOf(target);
    if (!arrayNew) {
        if (rec) {
            constructInto(obj, rec, init ? init->symbol.get() : nullptr,
                          init ? init->children : std::vector<ASTNodePtr>());
        } else if (init && init->children.size() == 1) { /* new int(5) */
            Quad s;
            s.op = Op::Store;
            s.a = obj;
            s.r = convert(rvalue(init->children[0]), target);
            s.cls = classOf(target);
            emit(s);
        }
        return obj;
    }
    if (needsConstruction(target)) { /* new T[n]: default-construct each element */
        Operand i = newTemp(sem::intType());
        emitAssign(i, icon(0));
        int test = nextQuad();
        Quad done;
        done.op = Op::IfRel;
        done.a = i;
        done.b = count;
        done.relop = ">=";
        done.cls = Cls::Int;
        int exit = emit(done);
        Operand elem = pointerAdd(obj, scaled(i, w));
        elem.type = pt;
        defaultConstruct(elem, target);
        Quad inc;
        inc.op = Op::Add;
        inc.a = i;
        inc.b = icon(1);
        inc.r = i;
        inc.cls = Cls::Int;
        emit(inc);
        emitGoto(test);
        backpatch(makelist(exit), nextQuad());
    }
    return obj;
}

void Generator::deleteExpr(const ASTNodePtr &n) {
    Operand p = rvalue(n->children[0]);
    bool arrayDelete = n->label == "[]";
    if (arrayDelete && p.type && sem::isPointer(p.type) && needsDestruction(p.type->elem)) {
        /* the count is in front of the block (see newExpr): destroy the
           elements last to first, then free the whole block */
        TypePtr elem = p.type->elem;
        long long w = std::max(1LL, sem::sizeOf(elem));
        Quad isNull;
        isNull.op = Op::IfRel;
        isNull.a = p;
        isNull.b = icon(0, p.type);
        isNull.relop = "==";
        isNull.cls = Cls::Ptr;
        int skip = emit(isNull);
        Operand block = pointerAdd(p, icon(8), true);
        Operand i = newTemp(sem::intType());
        Quad load;
        load.op = Op::Load;
        load.a = block;
        load.r = i;
        load.cls = Cls::Int;
        emit(load);
        int test = nextQuad();
        Quad done;
        done.op = Op::IfRel;
        done.a = i;
        done.b = icon(0);
        done.relop = "<=";
        done.cls = Cls::Int;
        int exit = emit(done);
        Quad dec;
        dec.op = Op::Sub;
        dec.a = i;
        dec.b = icon(1);
        dec.r = i;
        dec.cls = Cls::Int;
        emit(dec);
        Operand e = pointerAdd(p, scaled(i, w));
        e.type = p.type;
        destroy(e, recordOf(elem));
        emitGoto(test);
        backpatch(makelist(exit), nextQuad());
        Quad a;
        a.op = Op::Param;
        a.a = block;
        emit(a);
        Quad q;
        q.op = Op::Call;
        q.calleeName = "free";
        q.nargs = 1;
        emit(q);
        backpatch(makelist(skip), nextQuad());
        return;
    }
    RecordInfo *rec = !arrayDelete && p.type && sem::isPointer(p.type) ? recordOf(p.type->elem) : nullptr;
    if (rec && needsDestruction(sem::recordType(rec->shared_from_this()))) {
        Quad isNull; /* `delete` of a null pointer does nothing */
        isNull.op = Op::IfRel;
        isNull.a = p;
        isNull.b = icon(0, p.type);
        isNull.relop = "==";
        isNull.cls = Cls::Ptr;
        int skip = emit(isNull);
        destroy(p, rec);
        Quad a;
        a.op = Op::Param;
        a.a = p;
        emit(a);
        Quad q;
        q.op = Op::Call;
        q.calleeName = "free";
        q.nargs = 1;
        emit(q);
        backpatch(makelist(skip), nextQuad());
        return;
    }
    Quad a;
    a.op = Op::Param;
    a.a = p;
    emit(a);
    Quad q;
    q.op = Op::Call;
    q.calleeName = "free";
    q.nargs = 1;
    emit(q);
}

} // namespace tac
