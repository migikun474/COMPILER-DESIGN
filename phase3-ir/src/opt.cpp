/* -O1: local value numbering per basic block, dead temporaries, jump
   clean-up. See opt.h for what each part is. */
#include "opt.h"

#include <map>
#include <set>
#include <stdexcept>
#include <tuple>

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
        if (it != exprs.end() && holder(it->second, h)) {
            int n = it->second;
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
                case Op::IndexStore:
                    q.b = best(q.b);
                    if (!isBlock(q.r)) q.r = best(q.r);
                    memoryChanged();
                    break;
                case Op::Store:
                    q.a = best(q.a);
                    if (!isBlock(q.r)) q.r = best(q.r);
                    memoryChanged();
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

OptStats optimize(Program &program, int level) {
    OptStats stats;
    for (const auto &f : program.functions) stats.before += static_cast<int>(f.quads.size());
    if (level >= 1) {
        for (auto &f : program.functions) FunctionPass(f, stats).run();
    }
    int index = 100;
    for (auto &f : program.functions) {
        f.firstIndex = index;
        index += static_cast<int>(f.quads.size());
        stats.after += static_cast<int>(f.quads.size());
    }
    return stats;
}

void printStats(const OptStats &s, std::ostream &out) {
    out << "optimization summary (-O1)\n"
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
        << "    unreachable instructions    " << s.unreachable << "\n\n";
}

} // namespace tac
