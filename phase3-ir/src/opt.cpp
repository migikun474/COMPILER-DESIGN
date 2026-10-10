/* -O1: local value numbering per basic block, dead temporaries, jump
   clean-up. See opt.h for what each part is. */
#include "opt.h"

#include <algorithm>
#include <cstdint>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

#include "interp.h"

namespace tac {

namespace {

using Name = std::pair<const sem::Symbol *, int>; /* a variable, or (null, n) for the temporary tn */

bool isName(const Operand &o) { return o.kind == Operand::Temp || o.kind == Operand::Var; }
Name nameOf(const Operand &o) { return {o.kind == Operand::Var ? o.sym : nullptr, o.kind == Operand::Temp ? o.temp : 0}; }
bool sameName(const Operand &a, const Operand &b) { return isName(a) && isName(b) && nameOf(a) == nameOf(b); }
bool isBlock(const Operand &o) { return classOf(o.type) == Cls::Block; }
bool isNumber(const Operand &o) { return o.kind == Operand::IntConst || o.kind == Operand::FloatConst; }
bool isJump(const Quad &q) { return q.op == Op::Goto || q.op == Op::IfRel; }

bool isIntCls(Cls c) { return c == Cls::Int || c == Cls::UInt || c == Cls::LLong || c == Cls::ULLong; }

Val valueOf(const Operand &o) {
    Val v;
    v.i = o.ival;
    v.f = o.kind == Operand::FloatConst ? o.fval : static_cast<double>(o.ival);
    return v;
}

/* the constant v written as an operand of the same type as `like` */
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

/* one more temporary in f, with a slot in its symbol table */
Operand addTemp(Function &f, const sem::TypePtr &type) {
    f.temps.push_back(type);
    bool ref = type && sem::isReference(type);
    long long width = ref ? 4 : std::max(0LL, sem::sizeOf(type)), align = ref ? 4 : std::max(1, sem::alignOf(type));
    long long offset = (f.frameWidth + align - 1) / align * align;
    f.frame.push_back({nullptr, "t" + std::to_string(f.temps.size()), "temp", type, width, offset});
    f.frameWidth = (offset + width + 3) / 4 * 4;
    Operand o;
    o.kind = Operand::Temp;
    o.temp = static_cast<int>(f.temps.size());
    o.type = type;
    return o;
}

struct FunctionPass {
    Function &fn;
    OptStats &stats;
    std::set<Name> addressTaken; /* &x was taken somewhere: x can change behind our back */

    FunctionPass(Function &f, OptStats &s) : fn(f), stats(s) {
        for (const auto &q : fn.quads) {
            if (q.op == Op::AddrOf && isName(q.a)) addressTaken.insert(nameOf(q.a));
            if (q.op == Op::VaStart && isName(q.b)) addressTaken.insert(nameOf(q.b));
        }
    }

    /* a name whose value a store through a pointer or a call may change */
    bool inMemory(const Operand &o) const {
        if (!isName(o)) return false;
        if (addressTaken.count(nameOf(o))) return true;
        return o.kind == Operand::Var &&
               (o.sym->storage == sem::Storage::Global || o.sym->storage == sem::Storage::Static);
    }
    static bool isVolatile(const Operand &o) {
        return o.kind == Operand::Var && o.sym->type && o.sym->type->isVolatile;
    }

    std::vector<bool> leaders() const {
        std::vector<bool> lead(fn.quads.size() + 1, false);
        lead[0] = true;
        for (size_t i = 0; i < fn.quads.size(); ++i) {
            const Quad &q = fn.quads[i];
            if (isJump(q) && q.target >= 0) lead[q.target] = true;
            if (isJump(q) || q.op == Op::Return) lead[i + 1] = true;
        }
        return lead;
    }

    /* ---------------- value numbering of one basic block ---------------- */

    struct Node { /* one value: a DAG node */
        bool isConst = false;
        Operand constant;
        std::vector<Operand> names; /* names that held this value when they were assigned */
    };
    std::map<Name, int> current;                       /* name -> the value it holds now */
    std::map<std::tuple<int, int, int, long long, long long, int>, int> exprs;
    std::map<std::pair<int, long long>, int> intConsts;
    std::map<std::pair<int, double>, int> floatConsts;
    std::map<Name, int> nameIds;
    std::vector<Node> nodes;
    int epoch = 0; /* bumped whenever memory may have changed: loads before and after differ */

    int fresh() {
        nodes.emplace_back();
        return static_cast<int>(nodes.size()) - 1;
    }
    int idOf(const Operand &o) { return nameIds.emplace(nameOf(o), static_cast<int>(nameIds.size())).first->second; }

    int number(const Operand &o) {
        if (o.kind == Operand::IntConst || o.kind == Operand::Str) {
            auto key = std::make_pair(o.kind == Operand::Str ? 1 : 0, o.kind == Operand::Str ? o.str : o.ival);
            auto it = intConsts.find(key);
            if (it != intConsts.end()) return it->second;
            int n = fresh();
            nodes[n].isConst = true;
            nodes[n].constant = o;
            return intConsts[key] = n;
        }
        if (o.kind == Operand::FloatConst) {
            auto key = std::make_pair(static_cast<int>(classOf(o.type)), o.fval);
            auto it = floatConsts.find(key);
            if (it != floatConsts.end()) return it->second;
            int n = fresh();
            nodes[n].isConst = true;
            nodes[n].constant = o;
            return floatConsts[key] = n;
        }
        if (!isName(o) || isVolatile(o)) return fresh();
        auto it = current.find(nameOf(o));
        if (it != current.end()) return it->second;
        int n = fresh();
        nodes[n].names.push_back(o);
        return current[nameOf(o)] = n;
    }

    /* an earlier name that still holds value n, if any */
    bool holder(int n, Operand &out) {
        for (const auto &name : nodes[n].names) {
            auto it = current.find(nameOf(name));
            if (it != current.end() && it->second == n) { out = name; return true; }
        }
        return false;
    }

    /* the best way to write operand o: a constant, or the first name that has its value */
    Operand best(const Operand &o) {
        if (!isName(o) || isBlock(o) || isVolatile(o)) return o;
        int n = number(o);
        Operand r = o;
        if (nodes[n].isConst) {
            r = nodes[n].constant.kind == Operand::Str ? nodes[n].constant : constant(valueOf(nodes[n].constant), o);
            r.type = o.type;
        } else {
            Operand h;
            if (holder(n, h) && !sameName(h, o)) {
                r = h;
                r.type = o.type;
            }
        }
        if (!sameName(r, o)) ++stats.copies;
        return r;
    }

    void memoryChanged() {
        ++epoch;
        for (auto it = current.begin(); it != current.end();) {
            Operand probe;
            probe.kind = it->first.first ? Operand::Var : Operand::Temp;
            probe.sym = const_cast<sem::Symbol *>(it->first.first);
            probe.temp = it->first.second;
            if (inMemory(probe)) it = current.erase(it);
            else ++it;
        }
    }

    void define(const Operand &r, int n) {
        if (!isName(r)) return;
        if (inMemory(r)) memoryChanged();
        if (isBlock(r) || isVolatile(r)) { current.erase(nameOf(r)); return; }
        current[nameOf(r)] = n;
        nodes[n].names.push_back(r);
    }

    void becomeCopy(Quad &q, Operand src) { /* by value: src is often q's own operand */
        Operand r = q.r;
        q = Quad();
        q.op = Op::Assign;
        q.r = r;
        q.a = src;
        q.a.type = isName(src) ? r.type : src.type;
        q.cls = classOf(r.type);
        q.line = 0;
    }

    /* x + 0, x * 1, x * 2^k ...; true if q was rewritten */
    bool simplify(Quad &q) {
        bool aNum = isNumber(q.a), bNum = isNumber(q.b);
        bool isFloat = isFloatCls(q.cls);
        auto is = [&](const Operand &o, long long v) {
            return o.kind == Operand::IntConst ? o.ival == v : o.kind == Operand::FloatConst && o.fval == static_cast<double>(v);
        };
        switch (q.op) {
            case Op::Add: case Op::BitOr: case Op::BitXor:
                if (isFloat) return false; /* x + 0.0 is not x for x = -0.0 */
                if (bNum && is(q.b, 0)) { becomeCopy(q, q.a); return true; }
                if (aNum && is(q.a, 0) && q.cls != Cls::Ptr) { becomeCopy(q, q.b); return true; }
                return false;
            case Op::Sub: case Op::Shl: case Op::Shr:
                if (!isFloat && bNum && is(q.b, 0)) { becomeCopy(q, q.a); return true; }
                return false;
            case Op::Div:
                if (bNum && is(q.b, 1)) { becomeCopy(q, q.a); return true; }
                return false;
            case Op::Mul: {
                if (bNum && is(q.b, 1)) { becomeCopy(q, q.a); return true; }
                if (aNum && is(q.a, 1)) { becomeCopy(q, q.b); return true; }
                if (!isIntCls(q.cls)) return false;
                if ((bNum && is(q.b, 0)) || (aNum && is(q.a, 0))) { becomeCopy(q, constant(Val(), q.r)); return true; }
                if (aNum && !bNum) std::swap(q.a, q.b);
                if (q.b.kind == Operand::IntConst && q.b.ival > 1 && (q.b.ival & (q.b.ival - 1)) == 0) {
                    int k = 0; /* x * 2^k  ->  x << k */
                    while ((1LL << k) < q.b.ival) ++k;
                    q.op = Op::Shl;
                    q.b.ival = k;
                    q.b.type = sem::intType();
                    return true;
                }
                return false;
            }
            default:
                return false;
        }
    }

    /* r = <pure expression keyed by `key`>: reuse an earlier result or record this one */
    void expression(Quad &q, std::tuple<int, int, int, long long, long long, int> key) {
        auto it = exprs.find(key);
        Operand h;
        if (it != exprs.end() && (nodes[it->second].isConst || holder(it->second, h))) {
            int n = it->second;
            if (nodes[n].isConst) /* a constant that was stored to this place */
                h = nodes[n].constant.kind == Operand::Str ? nodes[n].constant : constant(valueOf(nodes[n].constant), q.r);
            becomeCopy(q, h);
            ++stats.common;
            define(q.r, n);
            return;
        }
        int n = fresh();
        exprs[key] = n;
        define(q.r, n);
    }

    bool numberBlock(size_t begin, size_t end, std::vector<bool> &dead) {
        current.clear(); exprs.clear(); intConsts.clear(); floatConsts.clear(); nodes.clear();
        int startCount = stats.folded + stats.simplified + stats.common + stats.copies + stats.dead;
        for (size_t i = begin; i < end; ++i) {
            Quad &q = fn.quads[i];
            int cls = static_cast<int>(q.cls), rcls = static_cast<int>(classOf(q.r.type));
            switch (q.op) {
                case Op::Assign:
                    if (isBlock(q.r)) { define(q.r, 0); memoryChanged(); break; }
                    q.a = best(q.a);
                    if (sameName(q.a, q.r)) { dead[i] = true; ++stats.dead; break; } /* x = x */
                    define(q.r, number(q.a));
                    break;
                case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod:
                case Op::BitAnd: case Op::BitOr: case Op::BitXor: case Op::Shl: case Op::Shr:
                case Op::Neg: case Op::BitNot: {
                    bool unary = q.op == Op::Neg || q.op == Op::BitNot;
                    q.a = best(q.a);
                    if (!unary) q.b = best(q.b);
                    if (isNumber(q.a) && (unary || isNumber(q.b))) {
                        try {
                            Val v = evalArithmetic(q, valueOf(q.a), unary ? Val() : valueOf(q.b));
                            becomeCopy(q, constant(v, q.r));
                            ++stats.folded;
                            define(q.r, number(q.a));
                            break;
                        } catch (const std::runtime_error &) { /* division by zero: left for run time */ }
                    }
                    if (!unary && simplify(q)) {
                        ++stats.simplified;
                        if (q.op == Op::Assign) { define(q.r, number(q.a)); break; }
                    }
                    long long na = number(q.a), nb = unary ? -1 : number(q.b);
                    bool commutes = q.op == Op::Add || q.op == Op::Mul || q.op == Op::BitAnd || q.op == Op::BitOr || q.op == Op::BitXor;
                    if (commutes && na > nb) std::swap(na, nb);
                    expression(q, std::make_tuple(static_cast<int>(q.op), cls, rcls, na, nb, -1));
                    break;
                }
                case Op::Conv:
                    q.a = best(q.a);
                    if (isNumber(q.a)) {
                        Val v = evalConvert(q.from, q.cls, valueOf(q.a));
                        becomeCopy(q, constant(v, q.r));
                        ++stats.folded;
                        define(q.r, number(q.a));
                        break;
                    }
                    expression(q, std::make_tuple(static_cast<int>(q.op), cls, static_cast<int>(q.from), number(q.a), -1LL, -1));
                    break;
                case Op::IfRel: {
                    q.a = best(q.a);
                    q.b = best(q.b);
                    int known = -1; /* 1: always jumps, 0: never */
                    if (isNumber(q.a) && isNumber(q.b)) known = evalCompare(q, valueOf(q.a), valueOf(q.b));
                    else if (!isFloatCls(q.cls) && isName(q.a) && isName(q.b) && number(q.a) == number(q.b))
                        known = q.relop == "==" || q.relop == "<=" || q.relop == ">=";
                    if (known == 1) { q.op = Op::Goto; q.a = q.b = Operand(); ++stats.folded; }
                    else if (known == 0) { dead[i] = true; ++stats.folded; }
                    break;
                }
                case Op::AddrOf:
                    expression(q, std::make_tuple(static_cast<int>(q.op), 0, 0, static_cast<long long>(idOf(q.a)), -1LL, -1));
                    break;
                case Op::IndexLoad:
                    q.b = best(q.b);
                    if (isBlock(q.r)) { define(q.r, 0); memoryChanged(); break; }
                    expression(q, std::make_tuple(static_cast<int>(q.op), rcls, 0, static_cast<long long>(idOf(q.a)), static_cast<long long>(number(q.b)), epoch));
                    break;
                case Op::Load:
                    q.a = best(q.a);
                    if (isBlock(q.r)) { define(q.r, 0); memoryChanged(); break; }
                    expression(q, std::make_tuple(static_cast<int>(q.op), rcls, 0, static_cast<long long>(number(q.a)), -1LL, epoch));
                    break;
                case Op::IndexStore: /* afterwards a load of the same place gives the stored value */
                    q.b = best(q.b);
                    if (!isBlock(q.r)) q.r = best(q.r);
                    memoryChanged();
                    if (q.cls != Cls::Block)
                        exprs[std::make_tuple(static_cast<int>(Op::IndexLoad), cls, 0, static_cast<long long>(idOf(q.a)),
                                              static_cast<long long>(number(q.b)), epoch)] = number(q.r);
                    break;
                case Op::Store:
                    q.a = best(q.a);
                    if (!isBlock(q.r)) q.r = best(q.r);
                    memoryChanged();
                    if (q.cls != Cls::Block)
                        exprs[std::make_tuple(static_cast<int>(Op::Load), cls, 0, static_cast<long long>(number(q.a)), -1LL, epoch)] = number(q.r);
                    break;
                case Op::Param: case Op::Return:
                    if (!q.a.isNone() && !isBlock(q.a)) q.a = best(q.a);
                    break;
                case Op::Call: case Op::VaArg: case Op::VaStart:
                    memoryChanged(); /* the callee may write any global or anything whose address escaped */
                    if (q.op != Op::Call && isName(q.a)) current.erase(nameOf(q.a));
                    if (!q.r.isNone()) define(q.r, fresh());
                    break;
                default:
                    break;
            }
        }
        return stats.folded + stats.simplified + stats.common + stats.copies + stats.dead != startCount;
    }

    /* ---------------- whole-function clean-up ---------------- */

    std::map<Name, int> uses() const {
        std::map<Name, int> n;
        auto use = [&](const Operand &o) { if (isName(o)) ++n[nameOf(o)]; };
        for (const auto &q : fn.quads) {
            use(q.a);
            use(q.b);
            if (q.op == Op::Store || q.op == Op::IndexStore) use(q.r); /* the value stored */
        }
        return n;
    }

    /* `t = a + b ; x = t` with t used nowhere else -> `x = a + b` */
    bool coalesce(std::vector<bool> &dead) {
        std::map<Name, int> used = uses(), defs;
        for (const auto &q : fn.quads)
            if (q.op != Op::Store && q.op != Op::IndexStore && isName(q.r)) ++defs[nameOf(q.r)];
        std::vector<bool> lead = leaders();
        bool changed = false;
        for (size_t i = 0; i + 1 < fn.quads.size(); ++i) {
            Quad &q = fn.quads[i], &next = fn.quads[i + 1];
            if (dead[i] || dead[i + 1] || lead[i + 1]) continue;
            if (q.r.kind != Operand::Temp || q.op == Op::Store || q.op == Op::IndexStore || isJump(q)) continue;
            if (next.op != Op::Assign || !sameName(next.a, q.r) || !isName(next.r) || isVolatile(next.r)) continue;
            Name t = nameOf(q.r);
            if (used[t] != 1 || defs[t] != 1 || addressTaken.count(t)) continue;
            if (classOf(next.r.type) != classOf(q.r.type)) continue;
            q.r = next.r;
            dead[i + 1] = true;
            ++stats.coalesced;
            changed = true;
        }
        return changed;
    }

    /* an instruction that only computes a temporary nobody reads */
    bool removeDead(std::vector<bool> &dead) {
        bool changed = false, again = true;
        while (again) {
            again = false;
            std::map<Name, int> used;
            auto use = [&](const Operand &o) { if (isName(o)) ++used[nameOf(o)]; };
            for (size_t i = 0; i < fn.quads.size(); ++i) {
                if (dead[i]) continue;
                const Quad &q = fn.quads[i];
                use(q.a);
                use(q.b);
                if (q.op == Op::Store || q.op == Op::IndexStore) use(q.r);
            }
            for (size_t i = 0; i < fn.quads.size(); ++i) {
                Quad &q = fn.quads[i];
                if (dead[i] || q.r.kind != Operand::Temp || used[nameOf(q.r)] || addressTaken.count(nameOf(q.r))) continue;
                switch (q.op) {
                    case Op::Call:
                        q.r = Operand(); /* the call stays, its unused result goes */
                        break;
                    case Op::Store: case Op::IndexStore: case Op::VaArg:
                        continue;
                    default:
                        dead[i] = true;
                        break;
                }
                ++stats.dead;
                changed = again = true;
            }
        }
        return changed;
    }

    bool cleanJumps(std::vector<bool> &dead) {
        bool changed = false;
        int n = static_cast<int>(fn.quads.size());
        auto live = [&](int i) { while (i < n && dead[i]) ++i; return i; };
        for (int i = 0; i < n; ++i) { /* a jump to a jump goes straight to the final target */
            Quad &q = fn.quads[i];
            if (dead[i] || !isJump(q)) continue;
            int t = live(q.target), hops = 0;
            while (t < n && fn.quads[t].op == Op::Goto && hops++ < n && live(fn.quads[t].target) != t) t = live(fn.quads[t].target);
            if (t != q.target) {
                if (live(q.target) != t) { ++stats.jumps; changed = true; }
                q.target = t;
            }
        }
        std::vector<int> targeted(n + 1, 0);
        for (int i = 0; i < n; ++i)
            if (!dead[i] && isJump(fn.quads[i])) ++targeted[fn.quads[i].target];
        for (int i = 0; i < n; ++i) { /* if c goto L1 ; goto L2 ; L1:   ->   if !c goto L2 */
            Quad &q = fn.quads[i];
            int j = live(i + 1);
            if (dead[i] || q.op != Op::IfRel || isFloatCls(q.cls) || j >= n || fn.quads[j].op != Op::Goto || targeted[j]) continue;
            if (q.target != live(j + 1)) continue;
            static const std::map<std::string, std::string> inverse = {{"==", "!="}, {"!=", "=="}, {"<", ">="},
                                                                       {">=", "<"},  {">", "<="},  {"<=", ">"}};
            q.relop = inverse.at(q.relop);
            q.target = fn.quads[j].target;
            dead[j] = true;
            ++stats.jumps;
            changed = true;
        }
        for (int i = 0; i < n; ++i) { /* a jump to the next instruction */
            const Quad &q = fn.quads[i];
            if (dead[i] || !isJump(q) || live(q.target) != live(i + 1)) continue;
            dead[i] = true;
            ++stats.jumps;
            changed = true;
        }
        std::vector<bool> reached(n + 1, false); /* code no path from the entry reaches */
        std::vector<int> work{live(0)};
        while (!work.empty()) {
            int i = work.back();
            work.pop_back();
            if (i >= n || reached[i]) continue;
            reached[i] = true;
            const Quad &q = fn.quads[i];
            if (isJump(q)) work.push_back(live(q.target));
            if (q.op != Op::Goto && q.op != Op::Return) work.push_back(live(i + 1));
        }
        for (int i = 0; i < n; ++i) {
            if (dead[i] || reached[i]) continue;
            dead[i] = true;
            ++stats.unreachable;
            changed = true;
        }
        return changed;
    }

    void compact(const std::vector<bool> &dead) {
        std::vector<int> moved(fn.quads.size() + 1, 0);
        int kept = 0;
        for (size_t i = 0; i < fn.quads.size(); ++i) {
            moved[i] = kept; /* a removed instruction maps to the next one kept */
            if (!dead[i]) ++kept;
        }
        moved[fn.quads.size()] = kept;
        std::vector<Quad> out;
        for (size_t i = 0; i < fn.quads.size(); ++i) {
            if (dead[i]) continue;
            Quad q = fn.quads[i];
            if (isJump(q) && q.target >= 0) q.target = moved[q.target];
            out.push_back(q);
        }
        fn.quads.swap(out);
    }

    /* ---------------- -O2: data-flow over the flow graph ---------------- */

    struct Block {
        size_t begin = 0, end = 0;
        std::vector<int> succ, pred;
    };

    std::vector<Block> flowGraph() const {
        std::vector<bool> lead = leaders();
        std::vector<Block> blocks;
        std::vector<int> blockOf(fn.quads.size() + 1, -1);
        for (size_t begin = 0; begin < fn.quads.size();) {
            size_t end = begin + 1;
            while (end < fn.quads.size() && !lead[end]) ++end;
            for (size_t i = begin; i < end; ++i) blockOf[i] = static_cast<int>(blocks.size());
            Block b;
            b.begin = begin;
            b.end = end;
            blocks.push_back(b);
            begin = end;
        }
        for (size_t k = 0; k < blocks.size(); ++k) {
            const Quad &last = fn.quads[blocks[k].end - 1];
            auto edge = [&](size_t quad) {
                if (quad >= fn.quads.size()) return;
                blocks[k].succ.push_back(blockOf[quad]);
                blocks[blockOf[quad]].pred.push_back(static_cast<int>(k));
            };
            if (isJump(last)) edge(static_cast<size_t>(last.target));
            if (last.op != Op::Goto && last.op != Op::Return) edge(blocks[k].end);
        }
        return blocks;
    }

    /* the name an instruction assigns, if any */
    static Operand defined(const Quad &q) {
        switch (q.op) {
            case Op::Store: case Op::IndexStore: case Op::Goto: case Op::IfRel: case Op::Param:
            case Op::Return: case Op::VaStart: case Op::VaEnd:
                return Operand();
            default:
                return isName(q.r) ? q.r : Operand();
        }
    }

    /* a scalar local nothing but its own assignments can change */
    bool isPrivate(const Operand &o) const { return isName(o) && !inMemory(o) && !isVolatile(o) && !isBlock(o); }

    /* the operands of q that are read as values (not array bases, not &x) */
    template <class F> static void forEachValueUse(Quad &q, F f) {
        switch (q.op) {
            case Op::Assign: case Op::Neg: case Op::BitNot: case Op::Conv: case Op::Load: case Op::Param: case Op::Return:
                f(q.a);
                break;
            case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod: case Op::BitAnd: case Op::BitOr:
            case Op::BitXor: case Op::Shl: case Op::Shr: case Op::IfRel:
                f(q.a);
                f(q.b);
                break;
            case Op::IndexLoad: f(q.b); break;
            case Op::IndexStore: f(q.b); f(q.r); break;
            case Op::Store: f(q.a); f(q.r); break;
            default: break;
        }
    }

    using Facts = std::map<Name, Operand>; /* name -> the constant or other name it certainly equals */

    static bool sameFact(const Operand &a, const Operand &b) {
        if (a.kind != b.kind) return false;
        if (isName(a)) return sameName(a, b);
        if (classOf(a.type) != classOf(b.type)) return false;
        return a.kind == Operand::FloatConst ? a.fval == b.fval : a.kind == Operand::Str ? a.str == b.str : a.ival == b.ival;
    }

    void transfer(const Quad &q, Facts &facts) const {
        auto kill = [&](const Operand &o) {
            if (!isName(o)) return;
            facts.erase(nameOf(o));
            for (auto it = facts.begin(); it != facts.end();)
                it = sameName(it->second, o) ? facts.erase(it) : std::next(it);
        };
        if (q.op == Op::VaStart || q.op == Op::VaArg) kill(q.a);
        Operand r = defined(q);
        kill(r);
        if (q.op != Op::Assign || !isPrivate(r)) return;
        if (isNumber(q.a) || q.a.kind == Operand::Str) facts[nameOf(r)] = q.a;
        else if (isPrivate(q.a) && !sameName(q.a, r) && classOf(q.a.type) == classOf(r.type)) facts[nameOf(r)] = q.a;
    }

    /* global constant and copy propagation */
    bool propagate() {
        std::vector<Block> blocks = flowGraph();
        std::vector<Facts> in(blocks.size()), out(blocks.size());
        std::vector<bool> done(blocks.size(), false);
        for (bool changed = true; changed;) {
            changed = false;
            for (size_t k = 0; k < blocks.size(); ++k) {
                Facts f;
                bool first = true;
                for (int p : blocks[k].pred) { /* meet: what every (already visited) predecessor agrees on */
                    if (!done[p]) continue;
                    if (first) { f = out[p]; first = false; continue; }
                    for (auto it = f.begin(); it != f.end();) {
                        auto other = out[p].find(it->first);
                        it = other != out[p].end() && sameFact(it->second, other->second) ? std::next(it) : f.erase(it);
                    }
                }
                if (k == 0) f.clear(); /* nothing is known on entry */
                in[k] = f;
                for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) transfer(fn.quads[i], f);
                bool same = done[k] && f.size() == out[k].size();
                if (same)
                    for (const auto &e : f) {
                        auto o = out[k].find(e.first);
                        if (o == out[k].end() || !sameFact(o->second, e.second)) { same = false; break; }
                    }
                if (!same) { out[k] = f; done[k] = true; changed = true; }
            }
        }
        bool rewrote = false;
        for (size_t k = 0; k < blocks.size(); ++k) {
            Facts f = in[k];
            for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) {
                Quad &q = fn.quads[i];
                forEachValueUse(q, [&](Operand &o) {
                    if (!isPrivate(o)) return;
                    auto fact = f.find(nameOf(o));
                    if (fact == f.end()) return;
                    Operand r = fact->second;
                    if (isNumber(r)) r = constant(valueOf(r), o);
                    r.type = o.type;
                    o = r;
                    ++stats.global;
                    rewrote = true;
                });
                transfer(q, f);
            }
        }
        return rewrote;
    }

    /* live-variable analysis; an assignment whose target is not live afterwards is removed */
    static void liveStep(const Quad &q, std::set<Name> &live) { /* live before q, given live after */
        if (q.op == Op::VaStart) { /* va_start(ap, last) assigns ap and reads nothing */
            if (isName(q.a)) live.erase(nameOf(q.a));
            return;
        }
        Operand r = defined(q);
        if (isName(r)) live.erase(nameOf(r));
        if (isName(q.a)) live.insert(nameOf(q.a));
        if (isName(q.b)) live.insert(nameOf(q.b));
        if ((q.op == Op::Store || q.op == Op::IndexStore) && isName(q.r)) live.insert(nameOf(q.r));
    }

    /* live-variable analysis: the names live at the entry of every block */
    std::vector<std::set<Name>> liveness(const std::vector<Block> &blocks) const {
        std::vector<std::set<Name>> liveIn(blocks.size());
        for (bool changed = true; changed;) {
            changed = false;
            for (size_t k = blocks.size(); k-- > 0;) {
                std::set<Name> live;
                for (int s : blocks[k].succ) live.insert(liveIn[s].begin(), liveIn[s].end());
                for (size_t i = blocks[k].end; i-- > blocks[k].begin;) liveStep(fn.quads[i], live);
                if (live != liveIn[k]) { liveIn[k] = live; changed = true; }
            }
        }
        return liveIn;
    }

    /* a scalar local that is live when the function starts is read on
       some path before anything was assigned to it */
    std::vector<const sem::Symbol *> readBeforeAssigned() const {
        std::vector<const sem::Symbol *> found;
        if (fn.quads.empty()) return found;
        std::vector<std::set<Name>> liveIn = liveness(flowGraph()); /* kept: the loop refers into it */
        for (const Name &n : liveIn[0]) {
            if (!n.first || n.first->storage != sem::Storage::Local || sem::isArray(n.first->type)) continue;
            Operand o;
            o.kind = Operand::Var;
            o.sym = const_cast<sem::Symbol *>(n.first);
            o.type = n.first->type;
            if (isPrivate(o)) found.push_back(n.first);
        }
        return found;
    }

    bool removeDeadAssignments() {
        std::vector<Block> blocks = flowGraph();
        auto step = [&](const Quad &q, std::set<Name> &live) { liveStep(q, live); };
        std::vector<std::set<Name>> liveIn = liveness(blocks);
        std::vector<bool> dead(fn.quads.size(), false);
        bool removed = false;
        for (size_t k = 0; k < blocks.size(); ++k) {
            std::set<Name> live;
            for (int s : blocks[k].succ) live.insert(liveIn[s].begin(), liveIn[s].end());
            for (size_t i = blocks[k].end; i-- > blocks[k].begin;) {
                Quad &q = fn.quads[i];
                Operand r = defined(q);
                bool unread = isName(r) && !live.count(nameOf(r)) && !inMemory(r) && !isVolatile(r);
                if (unread && q.op == Op::Call) {
                    q.r = Operand(); /* the call may have effects: only its result is dropped */
                    ++stats.deadAssignments;
                    removed = true;
                } else if (unread && q.op != Op::VaArg) {
                    dead[i] = true;
                    ++stats.deadAssignments;
                    removed = true;
                    continue; /* a removed instruction reads nothing */
                }
                step(q, live);
            }
        }
        if (removed) compact(dead);
        return removed;
    }

    /* ---------------- -O3 ---------------- */

    static bool isPure(Op op) { /* no effect but its result; may be computed early or reused */
        switch (op) {
            case Op::Add: case Op::Sub: case Op::Mul: case Op::BitAnd: case Op::BitOr: case Op::BitXor:
            case Op::Shl: case Op::Shr: case Op::Neg: case Op::BitNot: case Op::Conv: case Op::AddrOf:
                return true;
            default:
                return false;
        }
    }

    static std::string operandKey(const Operand &o) {
        if (isName(o)) return "n" + std::to_string(reinterpret_cast<uintptr_t>(nameOf(o).first)) + ":" + std::to_string(nameOf(o).second);
        if (o.kind == Operand::FloatConst) return "f" + std::to_string(static_cast<int>(classOf(o.type))) + ":" + std::to_string(o.fval);
        if (o.kind == Operand::Str) return "s" + std::to_string(o.str);
        return "c" + std::to_string(static_cast<int>(classOf(o.type))) + ":" + std::to_string(o.ival);
    }

    /* `r = a op b` as something another instruction can reuse: its key, or "" */
    std::string reusable(const Quad &q) const {
        if (!isPure(q.op) && q.op != Op::Div && q.op != Op::Mod) return "";
        Operand r = defined(q);
        if (!isPrivate(r) || sameName(q.a, r) || sameName(q.b, r)) return "";
        if (q.op != Op::AddrOf)
            for (const Operand *o : {&q.a, &q.b})
                if (isName(*o) && !isPrivate(*o)) return "";
        std::string a = operandKey(q.a), b = q.b.isNone() ? "" : operandKey(q.b);
        bool commutes = q.op == Op::Add || q.op == Op::Mul || q.op == Op::BitAnd || q.op == Op::BitOr || q.op == Op::BitXor;
        if (commutes && b < a) std::swap(a, b);
        return std::to_string(static_cast<int>(q.op)) + "|" + std::to_string(static_cast<int>(q.cls)) + "|" +
               std::to_string(static_cast<int>(q.from)) + "|" + std::to_string(static_cast<int>(classOf(q.r.type))) + "|" + a + "|" + b;
    }

    struct Available { /* an expression whose value some name still holds */
        Operand holder;
        std::vector<Name> uses;
    };
    using AvailableSet = std::map<std::string, Available>;

    void transferAvailable(const Quad &q, AvailableSet &set) const {
        auto kill = [&](const Operand &o) {
            if (!isName(o)) return;
            Name n = nameOf(o);
            for (auto it = set.begin(); it != set.end();) {
                bool gone = nameOf(it->second.holder) == n;
                for (const Name &u : it->second.uses) gone = gone || u == n;
                it = gone ? set.erase(it) : std::next(it);
            }
        };
        if (q.op == Op::VaStart || q.op == Op::VaArg) kill(q.a);
        std::string key = reusable(q);
        kill(defined(q));
        if (key.empty()) return;
        Available a;
        a.holder = q.r;
        if (q.op != Op::AddrOf) /* the address of x does not change when x does */
            for (const Operand *o : {&q.a, &q.b})
                if (isName(*o)) a.uses.push_back(nameOf(*o));
        set[key] = a;
    }

    /* common subexpressions across basic blocks: available-expressions analysis */
    bool globalCommon() {
        std::vector<Block> blocks = flowGraph();
        std::vector<AvailableSet> in(blocks.size()), out(blocks.size());
        std::vector<bool> done(blocks.size(), false);
        auto same = [](const AvailableSet &x, const AvailableSet &y) {
            if (x.size() != y.size()) return false;
            for (const auto &e : x) {
                auto o = y.find(e.first);
                if (o == y.end() || !sameName(o->second.holder, e.second.holder)) return false;
            }
            return true;
        };
        for (bool changed = true; changed;) {
            changed = false;
            for (size_t k = 0; k < blocks.size(); ++k) {
                AvailableSet f;
                bool first = true;
                for (int p : blocks[k].pred) {
                    if (!done[p]) continue;
                    if (first) { f = out[p]; first = false; continue; }
                    for (auto it = f.begin(); it != f.end();) {
                        auto o = out[p].find(it->first);
                        it = o != out[p].end() && sameName(o->second.holder, it->second.holder) ? std::next(it) : f.erase(it);
                    }
                }
                if (k == 0) f.clear();
                in[k] = f;
                for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) transferAvailable(fn.quads[i], f);
                if (!done[k] || !same(f, out[k])) { out[k] = f; done[k] = true; changed = true; }
            }
        }
        bool rewrote = false;
        for (size_t k = 0; k < blocks.size(); ++k) {
            AvailableSet f = in[k];
            for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) {
                Quad &q = fn.quads[i];
                std::string key = reusable(q);
                auto hit = key.empty() ? f.end() : f.find(key);
                if (hit != f.end() && !sameName(hit->second.holder, q.r)) {
                    becomeCopy(q, hit->second.holder);
                    ++stats.globalCommon;
                    rewrote = true;
                }
                transferAvailable(q, f);
            }
        }
        return rewrote;
    }

    /* natural loops: a back edge n -> h where h dominates n, with every block that reaches n without passing h */
    struct Loop {
        int header = 0;
        std::set<int> blocks;
    };
    static std::vector<Loop> loops(const std::vector<Block> &b) {
        size_t n = b.size();
        std::vector<std::vector<bool>> dom(n, std::vector<bool>(n, true));
        if (n) { dom[0].assign(n, false); dom[0][0] = true; }
        for (bool changed = true; changed;) {
            changed = false;
            for (size_t k = 1; k < n; ++k) {
                std::vector<bool> d(n, !b[k].pred.empty());
                for (int p : b[k].pred)
                    for (size_t i = 0; i < n; ++i) d[i] = d[i] && dom[p][i];
                d[k] = true;
                if (d != dom[k]) { dom[k] = d; changed = true; }
            }
        }
        std::map<int, Loop> byHeader;
        for (size_t k = 0; k < n; ++k)
            for (int h : b[k].succ) {
                if (!dom[k][h]) continue;
                Loop &l = byHeader[h];
                l.header = h;
                l.blocks.insert(h);
                std::vector<int> work{static_cast<int>(k)};
                while (!work.empty()) {
                    int x = work.back();
                    work.pop_back();
                    if (!l.blocks.insert(x).second) continue;
                    for (int p : b[x].pred) work.push_back(p);
                }
            }
        std::vector<Loop> result;
        for (const auto &e : byHeader) result.push_back(e.second);
        return result;
    }

    /* loop-invariant code motion: a pure instruction whose operands do not
       change in the loop, and whose result is assigned nowhere else, is
       computed once in front of the loop */
    bool hoistInvariants() {
        std::vector<Block> blocks = flowGraph();
        int n = static_cast<int>(fn.quads.size());
        std::map<Name, int> defsAll;
        for (const auto &q : fn.quads) {
            Operand r = defined(q);
            if (isName(r)) ++defsAll[nameOf(r)];
            if ((q.op == Op::VaStart || q.op == Op::VaArg) && isName(q.a)) ++defsAll[nameOf(q.a)];
        }
        for (const Loop &l : loops(blocks)) {
            std::set<int> inLoop;
            for (int k : l.blocks)
                for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) inLoop.insert(static_cast<int>(i));
            int head = static_cast<int>(blocks[l.header].begin);
            /* the code in front of the header must only be reached from outside the loop */
            if (head > 0 && inLoop.count(head - 1) && fn.quads[head - 1].op != Op::Goto && fn.quads[head - 1].op != Op::Return) continue;
            std::map<Name, int> defsIn;
            for (int i : inLoop) {
                const Quad &q = fn.quads[i];
                Operand r = defined(q);
                if (isName(r)) ++defsIn[nameOf(r)];
                if ((q.op == Op::VaStart || q.op == Op::VaArg) && isName(q.a)) ++defsIn[nameOf(q.a)];
            }
            std::vector<Quad> moved;
            std::vector<bool> drop(n, false);
            std::set<Name> hoisted;
            for (int i : inLoop) {
                const Quad &q = fn.quads[i];
                Operand r = defined(q);
                if (!isPure(q.op) || !isPrivate(r) || defsAll[nameOf(r)] != 1) continue;
                bool invariant = true;
                if (q.op != Op::AddrOf)
                    for (const Operand *o : {&q.a, &q.b})
                        if (isName(*o) && !(isPrivate(*o) && (defsIn[nameOf(*o)] == 0 || hoisted.count(nameOf(*o))))) invariant = false;
                if (!invariant) continue;
                moved.push_back(q);
                drop[i] = true;
                hoisted.insert(nameOf(r));
                ++stats.hoisted;
            }
            if (moved.empty()) continue;
            /* rebuild: the moved instructions go in front of the header; jumps
               from inside the loop still go to the header itself */
            std::vector<int> at(n + 1, 0), origin;
            std::vector<Quad> out;
            int front = 0;
            for (int i = 0; i < n; ++i) {
                if (i == head) {
                    front = static_cast<int>(out.size());
                    for (const Quad &m : moved) { out.push_back(m); origin.push_back(-1); }
                }
                at[i] = static_cast<int>(out.size());
                if (!drop[i]) { out.push_back(fn.quads[i]); origin.push_back(i); }
            }
            at[n] = static_cast<int>(out.size());
            for (size_t k = 0; k < out.size(); ++k) {
                if (origin[k] < 0 || !isJump(out[k]) || out[k].target < 0) continue;
                int t = out[k].target;
                out[k].target = t == head && !inLoop.count(origin[k]) ? front : at[t];
            }
            fn.quads.swap(out);
            return true; /* indices changed: the caller starts again */
        }
        return false;
    }

    /* `return f(args);` inside f itself: assign the arguments and jump to the start */
    bool tailRecursion() {
        if (!fn.sym || (fn.sym->name == "main" && !fn.sym->ownerRecord) || !addressTaken.empty()) return false;
        std::vector<sem::Symbol *> params;
        if (fn.thisSym) params.push_back(fn.thisSym);
        for (const auto &p : fn.sym->params) params.push_back(p.get());
        bool changed = false;
        for (size_t i = 0; i + 1 < fn.quads.size(); ++i) {
            const Quad &c = fn.quads[i], &ret = fn.quads[i + 1];
            size_t nargs = static_cast<size_t>(c.nargs);
            if (c.op != Op::Call || c.callee != fn.sym.get() || ret.op != Op::Return || nargs != params.size() || i < nargs) continue;
            if (!(c.r.isNone() ? ret.a.isNone() : sameName(ret.a, c.r))) continue;
            bool ok = fn.sym->type && !fn.sym->type->variadic;
            for (size_t k = 0; k < nargs; ++k) ok = ok && fn.quads[i - nargs + k].op == Op::Param;
            if (!ok) continue;
            std::vector<Quad> body; /* all arguments first: f(b, a) must not overwrite a before reading it */
            std::vector<Operand> saved;
            for (size_t k = 0; k < nargs; ++k) {
                Quad q;
                q.op = Op::Assign;
                q.a = fn.quads[i - nargs + k].a;
                q.r = addTemp(fn, params[k]->type);
                q.cls = classOf(q.r.type);
                saved.push_back(q.r);
                body.push_back(q);
            }
            for (size_t k = 0; k < nargs; ++k) {
                Quad q;
                q.op = Op::Assign;
                q.a = saved[k];
                q.r.kind = Operand::Var;
                q.r.sym = params[k];
                q.r.type = params[k]->type;
                q.cls = classOf(q.r.type);
                body.push_back(q);
            }
            Quad again;
            again.op = Op::Goto;
            again.target = 0;
            body.push_back(again);
            size_t begin = i - nargs, delta = body.size() - (nargs + 1);
            for (auto &q : fn.quads)
                if (isJump(q) && q.target > static_cast<int>(i)) q.target += static_cast<int>(delta);
            fn.quads.erase(fn.quads.begin() + static_cast<long>(begin), fn.quads.begin() + static_cast<long>(i) + 1);
            fn.quads.insert(fn.quads.begin() + static_cast<long>(begin), body.begin(), body.end());
            ++stats.tailCalls;
            changed = true;
            i = begin + body.size() - 1;
        }
        return changed;
    }

    void runLoops() {
        runGlobal();
        if (tailRecursion()) runGlobal();
        for (int round = 0; round < 20; ++round) {
            bool changed = globalCommon();
            changed = hoistInvariants() || changed;
            if (!changed) break;
            runGlobal();
        }
    }

    void runGlobal() {
        for (int round = 0; round < 10; ++round) {
            run();
            bool changed = propagate();
            changed = removeDeadAssignments() || changed;
            if (!changed) break;
        }
        run();
    }

    void run() {
        for (int round = 0; round < 10; ++round) {
            std::vector<bool> dead(fn.quads.size(), false);
            std::vector<bool> lead = leaders();
            bool changed = false;
            for (size_t begin = 0; begin < fn.quads.size();) {
                size_t end = begin + 1;
                while (end < fn.quads.size() && !lead[end]) ++end;
                changed = numberBlock(begin, end, dead) || changed;
                begin = end;
            }
            changed = coalesce(dead) || changed;
            changed = removeDead(dead) || changed;
            changed = cleanJumps(dead) || changed;
            compact(dead);
            if (!changed) break;
        }
    }
};

} // namespace

/* a call to a small function is replaced by the function's body: its
   parameters, locals and temporaries become temporaries of the caller,
   `return v` becomes `result = v; goto <after the body>` */
void inlineCalls(Program &program, OptStats &stats) {
    const std::vector<Function> originals = program.functions; /* bodies are taken from here: one level only */
    std::map<const sem::Symbol *, const Function *> bySymbol;
    for (const auto &f : originals) {
        bool ok = f.quads.size() <= 16 && f.linkName != "main" && f.sym->type && !f.sym->type->variadic;
        for (const auto &q : f.quads)
            ok = ok && q.op != Op::VaStart && q.op != Op::VaArg && !(q.op == Op::Call && q.callee == f.sym.get());
        if (ok) bySymbol[f.sym.get()] = &f;
    }
    for (auto &caller : program.functions) {
        std::vector<Quad> out;
        std::vector<int> at(caller.quads.size() + 1, 0);
        std::vector<bool> own; /* a jump of the caller itself, to be retargeted at the end */
        for (size_t i = 0; i < caller.quads.size(); ++i) {
            const Quad &q = caller.quads[i];
            at[i] = static_cast<int>(out.size());
            auto found = q.op == Op::Call && q.callee && q.callee != caller.sym.get() ? bySymbol.find(q.callee) : bySymbol.end();
            const Function *callee = found == bySymbol.end() ? nullptr : found->second;
            std::vector<const sem::Symbol *> params;
            if (callee) {
                if (callee->thisSym) params.push_back(callee->thisSym);
                for (const auto &p : callee->sym->params) params.push_back(p.get());
            }
            size_t nargs = static_cast<size_t>(q.nargs);
            bool usable = callee && nargs == params.size() && out.size() >= nargs;
            for (size_t k = 0; usable && k < nargs; ++k) usable = out[out.size() - nargs + k].op == Op::Param && own[out.size() - nargs + k];
            if (!usable) {
                out.push_back(q);
                own.push_back(true);
                continue;
            }
            std::map<const sem::Symbol *, Operand> vars;
            std::map<int, Operand> temps;
            auto renamed = [&](Operand o) { /* the callee's names as temporaries of the caller */
                if (o.kind == Operand::Temp) {
                    auto it = temps.find(o.temp);
                    if (it == temps.end()) it = temps.emplace(o.temp, addTemp(caller, callee->temps[o.temp - 1])).first;
                    Operand t = it->second;
                    t.type = o.type;
                    return t;
                }
                if (o.kind == Operand::Var) {
                    bool inFrame = false;
                    for (const auto &e : callee->frame) inFrame = inFrame || e.sym == o.sym;
                    if (!inFrame) return o; /* a global */
                    auto it = vars.find(o.sym);
                    if (it == vars.end()) it = vars.emplace(o.sym, addTemp(caller, o.sym->type)).first;
                    Operand t = it->second;
                    t.type = o.type;
                    return t;
                }
                return o;
            };
            for (size_t k = 0; k < nargs; ++k) { /* param x  ->  parameter = x */
                Quad &p = out[out.size() - nargs + k];
                Operand formal;
                formal.kind = Operand::Var;
                formal.sym = const_cast<sem::Symbol *>(params[k]);
                formal.type = params[k]->type;
                p.op = Op::Assign;
                p.r = renamed(formal);
                p.cls = classOf(p.r.type);
                p.note.clear();
            }
            int start = static_cast<int>(out.size());
            at[i] = start;
            std::vector<size_t> toEnd;
            std::vector<int> bodyAt(callee->quads.size() + 1, 0);
            std::vector<size_t> bodyJumps;
            for (size_t k = 0; k < callee->quads.size(); ++k) {
                Quad b = callee->quads[k];
                bodyAt[k] = static_cast<int>(out.size());
                b.a = renamed(b.a);
                b.b = renamed(b.b);
                b.r = renamed(b.r);
                if (b.op == Op::Return) {
                    if (!b.a.isNone() && !q.r.isNone()) {
                        Quad result;
                        result.op = Op::Assign;
                        result.r = q.r;
                        result.a = b.a;
                        result.cls = classOf(q.r.type);
                        out.push_back(result);
                        own.push_back(false);
                    }
                    if (k + 1 == callee->quads.size()) continue; /* the last one falls out of the body */
                    Quad leave;
                    leave.op = Op::Goto;
                    toEnd.push_back(out.size());
                    out.push_back(leave);
                    own.push_back(false);
                    continue;
                }
                if (b.op == Op::Goto || b.op == Op::IfRel) bodyJumps.push_back(out.size());
                out.push_back(b);
                own.push_back(false);
            }
            bodyAt[callee->quads.size()] = static_cast<int>(out.size());
            for (size_t j : bodyJumps) out[j].target = bodyAt[out[j].target];
            for (size_t j : toEnd) out[j].target = static_cast<int>(out.size());
            ++stats.inlined;
        }
        at[caller.quads.size()] = static_cast<int>(out.size());
        for (size_t k = 0; k < out.size(); ++k)
            if (own[k] && (out[k].op == Op::Goto || out[k].op == Op::IfRel) && out[k].target >= 0) out[k].target = at[out[k].target];
        caller.quads.swap(out);
    }
}

OptStats optimize(Program &program, int level) {
    OptStats stats;
    for (const auto &f : program.functions) stats.before += static_cast<int>(f.quads.size());
    stats.level = level;
    for (auto &f : program.functions) {
        FunctionPass pass(f, stats);
        if (level >= 3) pass.runLoops();
        else if (level == 2) pass.runGlobal();
        else if (level == 1) pass.run();
    }
    if (level >= 3) { /* small functions into their callers, then everything again on the larger bodies */
        inlineCalls(program, stats);
        for (auto &f : program.functions) FunctionPass(f, stats).runLoops();
    }
    int index = 100;
    for (auto &f : program.functions) {
        f.firstIndex = index;
        index += static_cast<int>(f.quads.size());
        stats.after += static_cast<int>(f.quads.size());
    }
    return stats;
}

std::vector<std::pair<int, std::string>> uninitializedReads(Program &program) {
    std::vector<std::pair<int, std::string>> out;
    OptStats unused;
    for (auto &f : program.functions)
        for (const sem::Symbol *v : FunctionPass(f, unused).readBeforeAssigned())
            out.push_back({v->line, "variable '" + v->name + "' may be used uninitialized in function '" + f.signature + "'"});
    std::sort(out.begin(), out.end());
    return out;
}

void printStats(const OptStats &s, std::ostream &out) {
    out << "optimization summary (-O" << s.level << ")\n"
        << "    instructions                " << s.before << " -> " << s.after;
    if (s.before) out << "   (" << (100 * (s.before - s.after) / s.before) << "% fewer)";
    out << "\n"
        << "    constants folded            " << s.folded << "\n"
        << "    algebraic simplifications   " << s.simplified << "\n"
        << "    common subexpressions       " << s.common << "\n"
        << "    copies / constants forwarded " << s.copies << "\n"
        << "    temporaries merged away     " << s.coalesced << "\n"
        << "    dead instructions removed   " << s.dead << "\n"
        << "    jumps removed or redirected " << s.jumps << "\n"
        << "    unreachable instructions    " << s.unreachable << "\n";
    if (s.level >= 2)
        out << "    propagated across blocks    " << s.global << "\n"
            << "    dead assignments removed    " << s.deadAssignments << "\n";
    if (s.level >= 3)
        out << "    calls inlined               " << s.inlined << "\n"
            << "    tail calls turned to jumps  " << s.tailCalls << "\n"
            << "    common across blocks        " << s.globalCommon << "\n"
            << "    moved out of loops          " << s.hoisted << "\n";
    out << "\n";
}

} // namespace tac
