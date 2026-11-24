#include <cstdio>

#include "opt_internal.h"

namespace tac {

namespace {

using namespace opt;

constexpr int MAX_ROUNDS = 10;
constexpr int FIRST_QUAD_INDEX = 100;

bool optimizeOnce(Function &fn, const MemoryModel &memory, OptStats &stats) {
    std::vector<bool> removed(fn.quads.size(), false);
    bool changed = false;
    for (const BasicBlock &block : basicBlocks(fn)) changed = numberBlock(fn, memory, block, removed, stats) || changed;
    changed = mergeTemporaries(fn, memory, removed, stats) || changed;
    changed = removeUnusedTemporaries(fn, memory, removed, stats) || changed;
    changed = cleanJumps(fn, removed, stats) || changed;
    dropRemoved(fn, removed);
    return changed;
}

void optimizeEachFunction(Program &program, OptStats &stats) {
    for (auto &fn : program.functions) {
        MemoryModel memory(fn);
        for (int round = 0; round < MAX_ROUNDS && optimizeOnce(fn, memory, stats); ++round) {
        }
    }
}

int instructionCount(const Program &program) {
    int count = 0;
    for (const auto &fn : program.functions) count += static_cast<int>(fn.quads.size());
    return count;
}

void renumberQuads(Program &program) {
    int index = FIRST_QUAD_INDEX;
    for (auto &fn : program.functions) {
        fn.firstIndex = index;
        index += static_cast<int>(fn.quads.size());
    }
}

}

OptStats optimize(Program &program) {
    OptStats stats;
    stats.before = instructionCount(program);
    optimizeEachFunction(program, stats);
    inlineCalls(program, stats);
    optimizeEachFunction(program, stats);
    renumberQuads(program);
    stats.after = instructionCount(program);
    return stats;
}

void printStats(const OptStats &s, std::ostream &out) {
    std::string rule(76, '-');
    out << rule << "\n OPTIMIZATION SUMMARY (-O1)\n" << rule << "\n\n";
    auto row = [&](const char *what, long long n) {
        char line[128];
        snprintf(line, sizeof line, "   %-34s %6lld\n", what, n);
        out << line;
    };
    char line[128];
    snprintf(line, sizeof line, "   %-34s %6lld -> %lld", "instructions", static_cast<long long>(s.before),
             static_cast<long long>(s.after));
    out << line;
    if (s.before) out << "   (" << (100 * (s.before - s.after) / s.before) << "% fewer)";
    out << "\n\n";
    row("calls inlined", s.inlined);
    row("constants folded", s.folded);
    row("algebraic simplifications", s.simplified);
    row("common subexpressions", s.common);
    row("copies / constants forwarded", s.copies);
    row("temporaries merged away", s.coalesced);
    row("dead instructions removed", s.dead);
    row("jumps removed or redirected", s.jumps);
    row("unreachable instructions removed", s.unreachable);
    out << "\n";
}

}
