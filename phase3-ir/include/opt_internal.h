#ifndef OPT_INTERNAL_H
#define OPT_INTERNAL_H

#include <set>
#include <utility>
#include <vector>

#include "interp.h"
#include "opt.h"

namespace tac::opt {

using Name = std::pair<const sem::Symbol *, int>;

bool isName(const Operand &o);
Name nameOf(const Operand &o);
bool sameName(const Operand &a, const Operand &b);
bool isBlock(const Operand &o);
bool isNumber(const Operand &o);
bool isJump(const Quad &q);
bool isStore(const Quad &q);
bool isIntCls(Cls c);

Val valueOf(const Operand &o);
Operand constant(Val v, const Operand &like);
void becomeCopy(Quad &q, Operand source);

class MemoryModel {
public:
    explicit MemoryModel(const Function &fn);
    bool addressTaken(const Name &name) const;
    bool inMemory(const Operand &o) const;

private:
    std::set<Name> taken;
};

struct BasicBlock {
    size_t begin = 0, end = 0;
};

std::vector<bool> blockLeaders(const Function &fn);
std::vector<BasicBlock> basicBlocks(const Function &fn);

bool simplifyAlgebra(Quad &q);

bool numberBlock(Function &fn, const MemoryModel &memory, BasicBlock block, std::vector<bool> &removed, OptStats &stats);

bool mergeTemporaries(Function &fn, const MemoryModel &memory, std::vector<bool> &removed, OptStats &stats);
bool removeUnusedTemporaries(Function &fn, const MemoryModel &memory, std::vector<bool> &removed, OptStats &stats);
bool cleanJumps(Function &fn, std::vector<bool> &removed, OptStats &stats);
void dropRemoved(Function &fn, const std::vector<bool> &removed);

void inlineCalls(Program &program, OptStats &stats);

}

#endif
