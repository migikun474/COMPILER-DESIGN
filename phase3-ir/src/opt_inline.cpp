#include <algorithm>
#include <map>

#include "opt_internal.h"

namespace tac::opt {

namespace {

constexpr size_t MAX_INLINED_QUADS = 16;

Operand newTemporary(Function &f, const sem::TypePtr &type) {
    f.temps.push_back(type);
    bool reference = type && sem::isReference(type);
    long long width = reference ? 4 : std::max(0LL, sem::sizeOf(type));
    long long align = reference ? 4 : std::max(1, sem::alignOf(type));
    long long offset = (f.frameWidth + align - 1) / align * align;
    f.frame.push_back({nullptr, "t" + std::to_string(f.temps.size()), "temp", type, width, offset});
    f.frameWidth = (offset + width + 3) / 4 * 4;
    Operand o;
    o.kind = Operand::Temp;
    o.temp = static_cast<int>(f.temps.size());
    o.type = type;
    return o;
}

bool callsItself(const Function &f) {
    return std::any_of(f.quads.begin(), f.quads.end(), [&](const Quad &q) { return q.op == Op::Call && q.callee == f.sym.get(); });
}

bool usesVarargs(const Function &f) {
    if (f.sym->type && f.sym->type->variadic) return true;
    return std::any_of(f.quads.begin(), f.quads.end(), [](const Quad &q) { return q.op == Op::VaStart || q.op == Op::VaArg; });
}

bool isInlinable(const Function &f) {
    return f.quads.size() <= MAX_INLINED_QUADS && f.linkName != "main" && f.sym->type && !usesVarargs(f) && !callsItself(f);
}

std::vector<const sem::Symbol *> formalParameters(const Function &f) {
    std::vector<const sem::Symbol *> formals;
    if (f.thisSym) formals.push_back(f.thisSym);
    for (const auto &p : f.sym->params) formals.push_back(p.get());
    return formals;
}

bool isInFrame(const Function &f, const sem::Symbol *sym) {
    return std::any_of(f.frame.begin(), f.frame.end(), [&](const auto &entry) { return entry.sym == sym; });
}

Quad assignment(const Operand &target, const Operand &source) {
    Quad q;
    q.op = Op::Assign;
    q.r = target;
    q.a = source;
    q.cls = classOf(target.type);
    return q;
}

class CallerRewriter {
public:
    CallerRewriter(Function &caller, const std::map<const sem::Symbol *, const Function *> &inlinable, OptStats &stats)
        : caller(caller), inlinable(inlinable), stats(stats) {}

    void run() {
        std::vector<int> newIndex(caller.quads.size() + 1, 0);
        for (size_t i = 0; i < caller.quads.size(); ++i) {
            newIndex[i] = static_cast<int>(out.size());
            const Quad &q = caller.quads[i];
            const Function *callee = inlinableCallee(q);
            if (callee && argumentsAreReady(q, *callee)) {
                newIndex[i] = expandCall(q, *callee);
                ++stats.inlined;
            } else {
                emit(q, true);
            }
        }
        newIndex[caller.quads.size()] = static_cast<int>(out.size());
        retargetCallerJumps(newIndex);
        caller.quads.swap(out);
    }

private:
    Function &caller;
    const std::map<const sem::Symbol *, const Function *> &inlinable;
    OptStats &stats;
    std::vector<Quad> out;
    std::vector<bool> fromCaller;

    void emit(const Quad &q, bool ownJump) {
        out.push_back(q);
        fromCaller.push_back(ownJump);
    }

    const Function *inlinableCallee(const Quad &q) const {
        if (q.op != Op::Call || !q.callee || q.callee == caller.sym.get()) return nullptr;
        auto found = inlinable.find(q.callee);
        return found == inlinable.end() ? nullptr : found->second;
    }

    bool argumentsAreReady(const Quad &call, const Function &callee) const {
        size_t count = static_cast<size_t>(call.nargs);
        if (count != formalParameters(callee).size() || out.size() < count) return false;
        for (size_t k = out.size() - count; k < out.size(); ++k)
            if (out[k].op != Op::Param || !fromCaller[k]) return false;
        return true;
    }

    int expandCall(const Quad &call, const Function &callee) {
        std::map<const sem::Symbol *, Operand> variables;
        std::map<int, Operand> temporaries;
        auto renamed = [&](Operand o) {
            if (o.kind == Operand::Temp) {
                auto it = temporaries.find(o.temp);
                if (it == temporaries.end()) it = temporaries.emplace(o.temp, newTemporary(caller, callee.temps[o.temp - 1])).first;
                Operand t = it->second;
                t.type = o.type;
                return t;
            }
            if (o.kind == Operand::Var && isInFrame(callee, o.sym)) {
                auto it = variables.find(o.sym);
                if (it == variables.end()) it = variables.emplace(o.sym, newTemporary(caller, o.sym->type)).first;
                Operand t = it->second;
                t.type = o.type;
                return t;
            }
            return o;
        };
        bindArguments(callee, renamed);
        int start = static_cast<int>(out.size());
        copyBody(call, callee, renamed);
        return start;
    }

    template <class Rename> void bindArguments(const Function &callee, Rename &renamed) {
        std::vector<const sem::Symbol *> formals = formalParameters(callee);
        size_t first = out.size() - formals.size();
        for (size_t k = 0; k < formals.size(); ++k) {
            Operand formal;
            formal.kind = Operand::Var;
            formal.sym = const_cast<sem::Symbol *>(formals[k]);
            formal.type = formals[k]->type;
            Quad &param = out[first + k];
            param.op = Op::Assign;
            param.r = renamed(formal);
            param.cls = classOf(param.r.type);
            param.note.clear();
        }
    }

    template <class Rename> void copyBody(const Quad &call, const Function &callee, Rename &renamed) {
        std::vector<int> bodyIndex(callee.quads.size() + 1, 0);
        std::vector<size_t> bodyJumps, exits;
        for (size_t k = 0; k < callee.quads.size(); ++k) {
            Quad q = callee.quads[k];
            bodyIndex[k] = static_cast<int>(out.size());
            q.a = renamed(q.a);
            q.b = renamed(q.b);
            q.r = renamed(q.r);
            if (q.op != Op::Return) {
                if (isJump(q)) bodyJumps.push_back(out.size());
                emit(q, false);
                continue;
            }
            if (!q.a.isNone() && !call.r.isNone()) emit(assignment(call.r, q.a), false);
            bool isLast = k + 1 == callee.quads.size();
            if (isLast) continue;
            Quad leave;
            leave.op = Op::Goto;
            exits.push_back(out.size());
            emit(leave, false);
        }
        bodyIndex[callee.quads.size()] = static_cast<int>(out.size());
        for (size_t j : bodyJumps) out[j].target = bodyIndex[out[j].target];
        for (size_t j : exits) out[j].target = static_cast<int>(out.size());
    }

    void retargetCallerJumps(const std::vector<int> &newIndex) {
        for (size_t k = 0; k < out.size(); ++k)
            if (fromCaller[k] && isJump(out[k]) && out[k].target >= 0) out[k].target = newIndex[out[k].target];
    }
};

}

void inlineCalls(Program &program, OptStats &stats) {
    const std::vector<Function> originals = program.functions;
    std::map<const sem::Symbol *, const Function *> inlinable;
    for (const auto &f : originals)
        if (isInlinable(f)) inlinable[f.sym.get()] = &f;
    for (auto &caller : program.functions) CallerRewriter(caller, inlinable, stats).run();
}

}
