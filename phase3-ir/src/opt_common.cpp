#include <algorithm>

#include "opt_internal.h"

namespace tac::opt {

bool isName(const Operand &o) { return o.kind == Operand::Temp || o.kind == Operand::Var; }

Name nameOf(const Operand &o) {
    return {o.kind == Operand::Var ? o.sym : nullptr, o.kind == Operand::Temp ? o.temp : 0};
}

bool sameName(const Operand &a, const Operand &b) { return isName(a) && isName(b) && nameOf(a) == nameOf(b); }
bool isBlock(const Operand &o) { return classOf(o.type) == Cls::Block; }
bool isNumber(const Operand &o) { return o.kind == Operand::IntConst || o.kind == Operand::FloatConst; }
bool isJump(const Quad &q) { return q.op == Op::Goto || q.op == Op::IfRel; }
bool isStore(const Quad &q) { return q.op == Op::Store || q.op == Op::IndexStore; }
bool isIntCls(Cls c) { return c == Cls::Int || c == Cls::UInt || c == Cls::LLong || c == Cls::ULLong; }

Val valueOf(const Operand &o) {
    Val v;
    v.i = o.ival;
    v.f = o.kind == Operand::FloatConst ? o.fval : static_cast<double>(o.ival);
    return v;
}

Operand constant(Val v, const Operand &like) {
    Operand o;
    o.type = like.type;
    Cls c = classOf(like.type);
    v = evalWrap(c, v);
    if (isFloatCls(c)) {
        o.kind = Operand::FloatConst;
        o.fval = v.f;
    } else {
        o.kind = Operand::IntConst;
        o.ival = v.i;
    }
    return o;
}

void becomeCopy(Quad &q, Operand source) {
    Operand result = q.r;
    q = Quad();
    q.op = Op::Assign;
    q.r = result;
    q.a = source;
    q.a.type = isName(source) ? result.type : source.type;
    q.cls = classOf(result.type);
    q.line = 0;
}

MemoryModel::MemoryModel(const Function &fn) {
    for (const auto &q : fn.quads) {
        if (q.op == Op::AddrOf && isName(q.a)) taken.insert(nameOf(q.a));
    }
}

bool MemoryModel::addressTaken(const Name &name) const { return taken.count(name) > 0; }

bool MemoryModel::inMemory(const Operand &o) const {
    if (!isName(o)) return false;
    if (addressTaken(nameOf(o))) return true;
    return o.kind == Operand::Var && (o.sym->storage == sem::Storage::Global || o.sym->storage == sem::Storage::Static);
}

std::vector<bool> blockLeaders(const Function &fn) {
    std::vector<bool> leader(fn.quads.size() + 1, false);
    leader[0] = true;
    for (size_t i = 0; i < fn.quads.size(); ++i) {
        const Quad &q = fn.quads[i];
        if (isJump(q) && q.target >= 0) leader[q.target] = true;
        if (isJump(q) || q.op == Op::Return) leader[i + 1] = true;
    }
    return leader;
}

std::vector<BasicBlock> basicBlocks(const Function &fn) {
    std::vector<bool> leader = blockLeaders(fn);
    std::vector<BasicBlock> blocks;
    for (size_t begin = 0; begin < fn.quads.size();) {
        size_t end = begin + 1;
        while (end < fn.quads.size() && !leader[end]) ++end;
        blocks.push_back({begin, end});
        begin = end;
    }
    return blocks;
}

}
