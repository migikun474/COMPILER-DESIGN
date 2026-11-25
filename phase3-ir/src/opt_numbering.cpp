#include <map>
#include <stdexcept>
#include <tuple>

#include "opt_internal.h"

namespace tac::opt {

namespace {

using ExpressionKey = std::tuple<int, int, int, long long, long long, int>;

constexpr long long NO_OPERAND = -1;
constexpr int ANY_MEMORY = -1;

struct Value {
    bool isConstant = false;
    Operand constant;
    std::vector<Operand> holders;
};

bool commutes(Op op) {
    return op == Op::Add || op == Op::Mul || op == Op::BitAnd || op == Op::BitOr || op == Op::BitXor;
}

bool isUnary(Op op) { return op == Op::Neg || op == Op::BitNot; }

int progress(const OptStats &s) { return s.folded + s.simplified + s.common + s.copies + s.dead; }

class BlockNumbering {
public:
    BlockNumbering(Function &fn, const MemoryModel &memory, std::vector<bool> &removed, OptStats &stats)
        : fn(fn), memory(memory), removed(removed), stats(stats) {}

    void run(BasicBlock block) {
        for (size_t i = block.begin; i < block.end; ++i) numberQuad(fn.quads[i], i);
    }

private:
    Function &fn;
    const MemoryModel &memory;
    std::vector<bool> &removed;
    OptStats &stats;

    std::vector<Value> values;
    std::map<Name, int> valueHeldBy;
    std::map<ExpressionKey, int> expressions;
    std::map<std::pair<int, long long>, int> intConstants;
    std::map<std::pair<int, double>, int> floatConstants;
    std::map<Name, int> nameIds;
    int memoryVersion = 0;

    int newValue() {
        values.emplace_back();
        return static_cast<int>(values.size()) - 1;
    }

    int constantValue(const Operand &o, int &slot) {
        if (slot >= 0) return slot;
        int v = newValue();
        values[v].isConstant = true;
        values[v].constant = o;
        return slot = v;
    }

    int valueOfOperand(const Operand &o) {
        if (o.kind == Operand::IntConst || o.kind == Operand::Str) {
            bool isString = o.kind == Operand::Str;
            auto key = std::make_pair(isString ? 1 : 0, isString ? o.str : o.ival);
            auto found = intConstants.emplace(key, -1).first;
            return constantValue(o, found->second);
        }
        if (o.kind == Operand::FloatConst) {
            auto key = std::make_pair(static_cast<int>(classOf(o.type)), o.fval);
            auto found = floatConstants.emplace(key, -1).first;
            return constantValue(o, found->second);
        }
        if (!isName(o)) return newValue();
        auto held = valueHeldBy.find(nameOf(o));
        if (held != valueHeldBy.end()) return held->second;
        int v = newValue();
        values[v].holders.push_back(o);
        return valueHeldBy[nameOf(o)] = v;
    }

    int idOf(const Operand &o) { return nameIds.emplace(nameOf(o), static_cast<int>(nameIds.size())).first->second; }

    bool currentHolder(int v, Operand &holder) const {
        for (const auto &name : values[v].holders) {
            auto held = valueHeldBy.find(nameOf(name));
            if (held != valueHeldBy.end() && held->second == v) {
                holder = name;
                return true;
            }
        }
        return false;
    }

    Operand constantOf(int v, const Operand &like) const {
        const Operand &c = values[v].constant;
        return c.kind == Operand::Str ? c : constant(valueOf(c), like);
    }

    Operand cheapestForm(const Operand &o) {
        if (!isName(o) || isBlock(o)) return o;
        int v = valueOfOperand(o);
        Operand replacement = o;
        Operand holder;
        if (values[v].isConstant) replacement = constantOf(v, o);
        else if (currentHolder(v, holder) && !sameName(holder, o)) replacement = holder;
        replacement.type = o.type;
        if (!sameName(replacement, o)) ++stats.copies;
        return replacement;
    }

    void forgetMemory() {
        ++memoryVersion;
        for (auto it = valueHeldBy.begin(); it != valueHeldBy.end();) {
            Operand name;
            name.kind = it->first.first ? Operand::Var : Operand::Temp;
            name.sym = const_cast<sem::Symbol *>(it->first.first);
            name.temp = it->first.second;
            it = memory.inMemory(name) ? valueHeldBy.erase(it) : std::next(it);
        }
    }

    void assignValue(const Operand &target, int v) {
        if (!isName(target)) return;
        if (memory.inMemory(target)) forgetMemory();
        if (isBlock(target)) {
            valueHeldBy.erase(nameOf(target));
            return;
        }
        valueHeldBy[nameOf(target)] = v;
        values[v].holders.push_back(target);
    }

    void reuseOrRecord(Quad &q, const ExpressionKey &key) {
        auto known = expressions.find(key);
        Operand holder;
        if (known != expressions.end() && (values[known->second].isConstant || currentHolder(known->second, holder))) {
            int v = known->second;
            if (values[v].isConstant) holder = constantOf(v, q.r);
            becomeCopy(q, holder);
            ++stats.common;
            assignValue(q.r, v);
            return;
        }
        int v = newValue();
        expressions[key] = v;
        assignValue(q.r, v);
    }

    void foldTo(Quad &q, Val result) {
        becomeCopy(q, constant(result, q.r));
        ++stats.folded;
        assignValue(q.r, valueOfOperand(q.a));
    }

    void copyBlock(Quad &q) {
        valueHeldBy.erase(nameOf(q.r));
        forgetMemory();
    }

    void numberAssign(Quad &q, size_t i) {
        if (isBlock(q.r)) { copyBlock(q); return; }
        q.a = cheapestForm(q.a);
        if (sameName(q.a, q.r)) {
            removed[i] = true;
            ++stats.dead;
            return;
        }
        assignValue(q.r, valueOfOperand(q.a));
    }

    void numberArithmetic(Quad &q) {
        bool unary = isUnary(q.op);
        q.a = cheapestForm(q.a);
        if (!unary) q.b = cheapestForm(q.b);
        if (isNumber(q.a) && (unary || isNumber(q.b))) {
            try {
                foldTo(q, evalArithmetic(q, valueOf(q.a), unary ? Val() : valueOf(q.b)));
                return;
            } catch (const std::runtime_error &) {
            }
        }
        if (!unary && simplifyAlgebra(q)) {
            ++stats.simplified;
            if (q.op == Op::Assign) {
                assignValue(q.r, valueOfOperand(q.a));
                return;
            }
        }
        long long left = valueOfOperand(q.a), right = unary ? NO_OPERAND : valueOfOperand(q.b);
        if (commutes(q.op) && left > right) std::swap(left, right);
        reuseOrRecord(q, {static_cast<int>(q.op), static_cast<int>(q.cls), static_cast<int>(classOf(q.r.type)), left, right, ANY_MEMORY});
    }

    void numberConversion(Quad &q) {
        q.a = cheapestForm(q.a);
        if (isNumber(q.a)) {
            foldTo(q, evalConvert(q.from, q.cls, valueOf(q.a)));
            return;
        }
        reuseOrRecord(q, {static_cast<int>(q.op), static_cast<int>(q.cls), static_cast<int>(q.from), valueOfOperand(q.a), NO_OPERAND, ANY_MEMORY});
    }

    int branchOutcome(const Quad &q) {
        if (isNumber(q.a) && isNumber(q.b)) return evalCompare(q, valueOf(q.a), valueOf(q.b));
        bool sameValue = !isFloatCls(q.cls) && isName(q.a) && isName(q.b) && valueOfOperand(q.a) == valueOfOperand(q.b);
        if (sameValue) return q.relop == "==" || q.relop == "<=" || q.relop == ">=";
        return -1;
    }

    void numberBranch(Quad &q, size_t i) {
        q.a = cheapestForm(q.a);
        q.b = cheapestForm(q.b);
        int outcome = branchOutcome(q);
        if (outcome == 1) {
            q.op = Op::Goto;
            q.a = q.b = Operand();
            ++stats.folded;
        } else if (outcome == 0) {
            removed[i] = true;
            ++stats.folded;
        }
    }

    ExpressionKey indexedLoadKey(const Quad &q, int cls) {
        return {static_cast<int>(Op::IndexLoad), cls, 0, idOf(q.a), valueOfOperand(q.b), memoryVersion};
    }

    ExpressionKey loadKey(const Operand &address, int cls) {
        return {static_cast<int>(Op::Load), cls, 0, valueOfOperand(address), NO_OPERAND, memoryVersion};
    }

    void numberIndexLoad(Quad &q) {
        q.b = cheapestForm(q.b);
        if (isBlock(q.r)) { copyBlock(q); return; }
        reuseOrRecord(q, indexedLoadKey(q, static_cast<int>(classOf(q.r.type))));
    }

    void numberLoad(Quad &q) {
        q.a = cheapestForm(q.a);
        if (isBlock(q.r)) { copyBlock(q); return; }
        reuseOrRecord(q, loadKey(q.a, static_cast<int>(classOf(q.r.type))));
    }

    void numberIndexStore(Quad &q) {
        q.b = cheapestForm(q.b);
        if (!isBlock(q.r)) q.r = cheapestForm(q.r);
        forgetMemory();
        if (q.cls != Cls::Block) expressions[indexedLoadKey(q, static_cast<int>(q.cls))] = valueOfOperand(q.r);
    }

    void numberStore(Quad &q) {
        q.a = cheapestForm(q.a);
        if (!isBlock(q.r)) q.r = cheapestForm(q.r);
        forgetMemory();
        if (q.cls != Cls::Block) expressions[loadKey(q.a, static_cast<int>(q.cls))] = valueOfOperand(q.r);
    }

    void numberCall(Quad &q) {
        forgetMemory();
        if (!q.r.isNone()) assignValue(q.r, newValue());
    }

    void numberQuad(Quad &q, size_t i) {
        switch (q.op) {
            case Op::Assign: numberAssign(q, i); break;
            case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod:
            case Op::BitAnd: case Op::BitOr: case Op::BitXor: case Op::Shl: case Op::Shr:
            case Op::Neg: case Op::BitNot: numberArithmetic(q); break;
            case Op::Conv: numberConversion(q); break;
            case Op::IfRel: numberBranch(q, i); break;
            case Op::AddrOf: reuseOrRecord(q, {static_cast<int>(q.op), 0, 0, idOf(q.a), NO_OPERAND, ANY_MEMORY}); break;
            case Op::IndexLoad: numberIndexLoad(q); break;
            case Op::Load: numberLoad(q); break;
            case Op::IndexStore: numberIndexStore(q); break;
            case Op::Store: numberStore(q); break;
            case Op::Param: case Op::Return:
                if (!q.a.isNone() && !isBlock(q.a)) q.a = cheapestForm(q.a);
                break;
            case Op::Call: numberCall(q); break;
            default: break;
        }
    }
};

}

bool numberBlock(Function &fn, const MemoryModel &memory, BasicBlock block, std::vector<bool> &removed, OptStats &stats) {
    int before = progress(stats);
    BlockNumbering(fn, memory, removed, stats).run(block);
    return progress(stats) != before;
}

}
