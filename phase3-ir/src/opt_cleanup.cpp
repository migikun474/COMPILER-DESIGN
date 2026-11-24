#include <map>
#include <string>

#include "opt_internal.h"

namespace tac::opt {

namespace {

std::map<Name, int> countReads(const Function &fn, const std::vector<bool> &removed) {
    std::map<Name, int> reads;
    auto read = [&](const Operand &o) { if (isName(o)) ++reads[nameOf(o)]; };
    for (size_t i = 0; i < fn.quads.size(); ++i) {
        if (removed[i]) continue;
        const Quad &q = fn.quads[i];
        read(q.a);
        read(q.b);
        if (isStore(q)) read(q.r);
    }
    return reads;
}

std::map<Name, int> countWrites(const Function &fn) {
    std::map<Name, int> writes;
    for (const auto &q : fn.quads)
        if (!isStore(q) && isName(q.r)) ++writes[nameOf(q.r)];
    return writes;
}

bool isTemporaryCopiedOnward(const Quad &q, const Quad &next) {
    if (q.r.kind != Operand::Temp || isStore(q) || isJump(q)) return false;
    if (next.op != Op::Assign || !sameName(next.a, q.r) || !isName(next.r)) return false;
    return classOf(next.r.type) == classOf(q.r.type);
}

bool removeIfUnread(Quad &q, size_t i, std::vector<bool> &removed) {
    switch (q.op) {
        case Op::Store: case Op::IndexStore: case Op::VaArg:
            return false;
        case Op::Call:
            q.r = Operand();
            return true;
        default:
            removed[i] = true;
            return true;
    }
}

const std::map<std::string, std::string> &invertedRelation() {
    static const std::map<std::string, std::string> inverse = {
        {"==", "!="}, {"!=", "=="}, {"<", ">="}, {">=", "<"}, {">", "<="}, {"<=", ">"}};
    return inverse;
}

class JumpCleaner {
public:
    JumpCleaner(Function &fn, std::vector<bool> &removed, OptStats &stats)
        : fn(fn), removed(removed), stats(stats), size(static_cast<int>(fn.quads.size())) {}

    bool run() {
        bool changed = threadJumpChains();
        changed = invertBranchesOverJumps() || changed;
        changed = dropJumpsToNext() || changed;
        changed = dropUnreachable() || changed;
        return changed;
    }

private:
    Function &fn;
    std::vector<bool> &removed;
    OptStats &stats;
    int size;

    int nextKept(int i) const {
        while (i < size && removed[i]) ++i;
        return i;
    }

    bool isKeptJump(int i) const { return !removed[i] && isJump(fn.quads[i]); }

    int finalTarget(int target) const {
        int t = nextKept(target);
        for (int hops = 0; t < size && fn.quads[t].op == Op::Goto && hops < size; ++hops) {
            int next = nextKept(fn.quads[t].target);
            if (next == t) break;
            t = next;
        }
        return t;
    }

    bool threadJumpChains() {
        bool changed = false;
        for (int i = 0; i < size; ++i) {
            if (!isKeptJump(i)) continue;
            Quad &q = fn.quads[i];
            int t = finalTarget(q.target);
            if (t == q.target) continue;
            if (nextKept(q.target) != t) {
                ++stats.jumps;
                changed = true;
            }
            q.target = t;
        }
        return changed;
    }

    std::vector<int> jumpsInto() const {
        std::vector<int> count(size + 1, 0);
        for (int i = 0; i < size; ++i)
            if (isKeptJump(i)) ++count[fn.quads[i].target];
        return count;
    }

    bool invertBranchesOverJumps() {
        bool changed = false;
        std::vector<int> targeted = jumpsInto();
        for (int i = 0; i < size; ++i) {
            Quad &branch = fn.quads[i];
            int j = nextKept(i + 1);
            if (removed[i] || branch.op != Op::IfRel || isFloatCls(branch.cls)) continue;
            if (j >= size || fn.quads[j].op != Op::Goto || targeted[j] || branch.target != nextKept(j + 1)) continue;
            branch.relop = invertedRelation().at(branch.relop);
            branch.target = fn.quads[j].target;
            removed[j] = true;
            ++stats.jumps;
            changed = true;
        }
        return changed;
    }

    bool dropJumpsToNext() {
        bool changed = false;
        for (int i = 0; i < size; ++i) {
            if (!isKeptJump(i) || nextKept(fn.quads[i].target) != nextKept(i + 1)) continue;
            removed[i] = true;
            ++stats.jumps;
            changed = true;
        }
        return changed;
    }

    std::vector<bool> reachableFromEntry() const {
        std::vector<bool> reached(size + 1, false);
        std::vector<int> work{nextKept(0)};
        while (!work.empty()) {
            int i = work.back();
            work.pop_back();
            if (i >= size || reached[i]) continue;
            reached[i] = true;
            const Quad &q = fn.quads[i];
            if (isJump(q)) work.push_back(nextKept(q.target));
            if (q.op != Op::Goto && q.op != Op::Return) work.push_back(nextKept(i + 1));
        }
        return reached;
    }

    bool dropUnreachable() {
        bool changed = false;
        std::vector<bool> reached = reachableFromEntry();
        for (int i = 0; i < size; ++i) {
            if (removed[i] || reached[i]) continue;
            removed[i] = true;
            ++stats.unreachable;
            changed = true;
        }
        return changed;
    }
};

}

bool mergeTemporaries(Function &fn, const MemoryModel &memory, std::vector<bool> &removed, OptStats &stats) {
    std::vector<bool> noneRemoved(fn.quads.size(), false);
    std::map<Name, int> reads = countReads(fn, noneRemoved), writes = countWrites(fn);
    std::vector<bool> leader = blockLeaders(fn);
    bool changed = false;
    for (size_t i = 0; i + 1 < fn.quads.size(); ++i) {
        Quad &q = fn.quads[i], &next = fn.quads[i + 1];
        if (removed[i] || removed[i + 1] || leader[i + 1] || !isTemporaryCopiedOnward(q, next)) continue;
        Name temp = nameOf(q.r);
        if (reads[temp] != 1 || writes[temp] != 1 || memory.addressTaken(temp)) continue;
        q.r = next.r;
        removed[i + 1] = true;
        ++stats.coalesced;
        changed = true;
    }
    return changed;
}

bool removeUnusedTemporaries(Function &fn, const MemoryModel &memory, std::vector<bool> &removed, OptStats &stats) {
    bool changed = false;
    for (bool again = true; again;) {
        again = false;
        std::map<Name, int> reads = countReads(fn, removed);
        for (size_t i = 0; i < fn.quads.size(); ++i) {
            Quad &q = fn.quads[i];
            if (removed[i] || q.r.kind != Operand::Temp || reads[nameOf(q.r)] || memory.addressTaken(nameOf(q.r))) continue;
            if (!removeIfUnread(q, i, removed)) continue;
            ++stats.dead;
            changed = again = true;
        }
    }
    return changed;
}

bool cleanJumps(Function &fn, std::vector<bool> &removed, OptStats &stats) { return JumpCleaner(fn, removed, stats).run(); }

void dropRemoved(Function &fn, const std::vector<bool> &removed) {
    std::vector<int> newIndex(fn.quads.size() + 1, 0);
    int kept = 0;
    for (size_t i = 0; i < fn.quads.size(); ++i) {
        newIndex[i] = kept;
        if (!removed[i]) ++kept;
    }
    newIndex[fn.quads.size()] = kept;
    std::vector<Quad> remaining;
    for (size_t i = 0; i < fn.quads.size(); ++i) {
        if (removed[i]) continue;
        Quad q = fn.quads[i];
        if (isJump(q) && q.target >= 0) q.target = newIndex[q.target];
        remaining.push_back(q);
    }
    fn.quads.swap(remaining);
}

}
