#include "opt_internal.h"

namespace tac::opt {

namespace {

bool equals(const Operand &o, long long v) {
    return o.kind == Operand::IntConst ? o.ival == v : o.kind == Operand::FloatConst && o.fval == static_cast<double>(v);
}

bool isPowerOfTwoAboveOne(const Operand &o) {
    return o.kind == Operand::IntConst && o.ival > 1 && (o.ival & (o.ival - 1)) == 0;
}

int log2Of(long long powerOfTwo) {
    int k = 0;
    while ((1LL << k) < powerOfTwo) ++k;
    return k;
}

Val zeroValue() { return Val(); }

Val allOnesValue() {
    Val v;
    v.i = -1;
    return v;
}

bool simplifyIntegerOnlyIdentity(Quad &q) {
    bool sameOperands = sameName(q.a, q.b);
    bool constantRight = isNumber(q.b);
    switch (q.op) {
        case Op::Sub: case Op::BitXor:
            if (sameOperands) { becomeCopy(q, constant(zeroValue(), q.r)); return true; }
            return false;
        case Op::BitAnd:
            if (sameOperands || (constantRight && equals(q.b, -1))) { becomeCopy(q, q.a); return true; }
            if (constantRight && equals(q.b, 0)) { becomeCopy(q, constant(zeroValue(), q.r)); return true; }
            return false;
        case Op::BitOr:
            if (sameOperands) { becomeCopy(q, q.a); return true; }
            if (constantRight && equals(q.b, -1)) { becomeCopy(q, constant(allOnesValue(), q.r)); return true; }
            return false;
        case Op::Mod:
            if (constantRight && (equals(q.b, 1) || equals(q.b, -1))) { becomeCopy(q, constant(zeroValue(), q.r)); return true; }
            return false;
        default:
            return false;
    }
}

bool simplifyAdditiveIdentity(Quad &q) {
    bool negativeZeroMatters = isFloatCls(q.cls);
    if (negativeZeroMatters) return false;
    if (isNumber(q.b) && equals(q.b, 0)) { becomeCopy(q, q.a); return true; }
    if (isNumber(q.a) && equals(q.a, 0) && q.cls != Cls::Ptr) { becomeCopy(q, q.b); return true; }
    return false;
}

bool simplifyRightZero(Quad &q) {
    if (!isFloatCls(q.cls) && isNumber(q.b) && equals(q.b, 0)) { becomeCopy(q, q.a); return true; }
    return false;
}

bool simplifyDivision(Quad &q) {
    if (isNumber(q.b) && equals(q.b, 1)) { becomeCopy(q, q.a); return true; }
    return false;
}

bool simplifyMultiplication(Quad &q) {
    bool constantLeft = isNumber(q.a), constantRight = isNumber(q.b);
    if (constantRight && equals(q.b, 1)) { becomeCopy(q, q.a); return true; }
    if (constantLeft && equals(q.a, 1)) { becomeCopy(q, q.b); return true; }
    if (!isIntCls(q.cls)) return false;
    if ((constantRight && equals(q.b, 0)) || (constantLeft && equals(q.a, 0))) {
        becomeCopy(q, constant(zeroValue(), q.r));
        return true;
    }
    if (constantLeft && !constantRight) std::swap(q.a, q.b);
    if (!isPowerOfTwoAboveOne(q.b)) return false;
    q.op = Op::Shl;
    q.b.ival = log2Of(q.b.ival);
    q.b.type = sem::intType();
    return true;
}

}

bool simplifyAlgebra(Quad &q) {
    if (isIntCls(q.cls) && simplifyIntegerOnlyIdentity(q)) return true;
    switch (q.op) {
        case Op::Add: case Op::BitOr: case Op::BitXor: return simplifyAdditiveIdentity(q);
        case Op::Sub: case Op::Shl: case Op::Shr: return simplifyRightZero(q);
        case Op::Div: return simplifyDivision(q);
        case Op::Mul: return simplifyMultiplication(q);
        default: return false;
    }
}

}
