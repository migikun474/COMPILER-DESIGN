#include <algorithm>
#include <map>
#include <set>
#include <string>

#include "opt_internal.h"

namespace tac {

namespace {

using namespace opt;

constexpr int AT_ENTRY = -1;

struct FlowBlock {
    size_t begin = 0, end = 0;
    std::vector<int> predecessors;
};

struct Definition {
    Name name;
    int quad;
};

std::vector<FlowBlock> flowGraph(const Function &fn) {
    std::vector<FlowBlock> blocks;
    std::vector<int> blockOf(fn.quads.size() + 1, -1);
    for (const BasicBlock &b : basicBlocks(fn)) {
        for (size_t i = b.begin; i < b.end; ++i) blockOf[i] = static_cast<int>(blocks.size());
        blocks.push_back({b.begin, b.end, {}});
    }
    for (size_t k = 0; k < blocks.size(); ++k) {
        const Quad &last = fn.quads[blocks[k].end - 1];
        auto addEdgeTo = [&](size_t quad) {
            if (quad < fn.quads.size()) blocks[blockOf[quad]].predecessors.push_back(static_cast<int>(k));
        };
        if (isJump(last)) addEdgeTo(static_cast<size_t>(last.target));
        if (last.op != Op::Goto && last.op != Op::Return) addEdgeTo(blocks[k].end);
    }
    return blocks;
}

Operand assignedName(const Quad &q) {
    switch (q.op) {
        case Op::Store: case Op::IndexStore: case Op::Goto: case Op::IfRel: case Op::Param:
        case Op::Return:
            return Operand();
        default:
            return isName(q.r) ? q.r : Operand();
    }
}

std::vector<Operand> valuesRead(const Quad &q) {
    switch (q.op) {
        case Op::Assign: case Op::Neg: case Op::BitNot: case Op::Conv: case Op::Load: case Op::Param: case Op::Return:
            return {q.a};
        case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod: case Op::BitAnd: case Op::BitOr:
        case Op::BitXor: case Op::Shl: case Op::Shr: case Op::IfRel:
            return {q.a, q.b};
        case Op::IndexLoad: return {q.b};
        case Op::IndexStore: return {q.b, q.r};
        case Op::Store: return {q.a, q.r};
        default: return {};
    }
}

class ReachingDefinitions {
public:
    ReachingDefinitions(const Function &fn) : fn(fn), memory(fn), blocks(flowGraph(fn)) {
        addEntryDefinitions();
        addInstructionDefinitions();
        solve();
    }

    std::vector<std::pair<const sem::Symbol *, int>> readsBeforeAssignment() const {
        std::vector<std::pair<const sem::Symbol *, int>> found;
        std::set<const sem::Symbol *> reported;
        for (size_t k = 0; k < blocks.size(); ++k) {
            std::set<int> reaching = in[k];
            for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) {
                const Quad &q = fn.quads[i];
                for (const Operand &o : valuesRead(q)) {
                    if (o.kind != Operand::Var || reported.count(o.sym) || !reachedByEntry(reaching, nameOf(o))) continue;
                    found.push_back({o.sym, q.line ? q.line : o.sym->line});
                    reported.insert(o.sym);
                }
                applyDefinition(static_cast<int>(i), reaching);
            }
        }
        return found;
    }

private:
    const Function &fn;
    MemoryModel memory;
    std::vector<FlowBlock> blocks;
    std::vector<Definition> definitions;
    std::map<Name, std::vector<int>> definitionsOf;
    std::map<int, int> definitionAt;
    size_t entryDefinitions = 0;
    std::vector<std::set<int>> in;

    void addDefinition(const Name &name, int quad) {
        int d = static_cast<int>(definitions.size());
        definitionsOf[name].push_back(d);
        if (quad != AT_ENTRY) definitionAt[quad] = d;
        definitions.push_back({name, quad});
    }

    bool isTrackedLocal(const sem::SymbolPtr &local) const {
        Operand o;
        o.kind = Operand::Var;
        o.sym = local.get();
        o.type = local->type;
        return local->storage == sem::Storage::Local && !sem::isArray(local->type) && !memory.inMemory(o) && !isBlock(o);
    }

    void addEntryDefinitions() {
        if (!fn.sym) return;
        for (const auto &local : fn.sym->locals) {
            if (!isTrackedLocal(local)) continue;
            Operand o;
            o.kind = Operand::Var;
            o.sym = local.get();
            addDefinition(nameOf(o), AT_ENTRY);
        }
        entryDefinitions = definitions.size();
    }

    void addInstructionDefinitions() {
        for (size_t i = 0; i < fn.quads.size(); ++i) {
            Operand r = assignedName(fn.quads[i]);
            if (isName(r)) addDefinition(nameOf(r), static_cast<int>(i));
        }
    }

    void applyDefinition(int quad, std::set<int> &reaching) const {
        auto at = definitionAt.find(quad);
        if (at == definitionAt.end()) return;
        for (int d : definitionsOf.at(definitions[at->second].name)) reaching.erase(d);
        reaching.insert(at->second);
    }

    std::set<int> outOf(size_t k, const std::set<int> &entering) const {
        std::set<int> reaching = entering;
        for (size_t i = blocks[k].begin; i < blocks[k].end; ++i) applyDefinition(static_cast<int>(i), reaching);
        return reaching;
    }

    void solve() {
        in.assign(blocks.size(), {});
        std::vector<std::set<int>> out(blocks.size());
        for (bool changed = true; changed;) {
            changed = false;
            for (size_t k = 0; k < blocks.size(); ++k) {
                std::set<int> entering;
                if (k == 0)
                    for (size_t d = 0; d < entryDefinitions; ++d) entering.insert(static_cast<int>(d));
                for (int p : blocks[k].predecessors) entering.insert(out[p].begin(), out[p].end());
                std::set<int> leaving = outOf(k, entering);
                if (entering != in[k] || leaving != out[k]) changed = true;
                in[k] = entering;
                out[k] = leaving;
            }
        }
    }

    bool reachedByEntry(const std::set<int> &reaching, const Name &name) const {
        return std::any_of(reaching.begin(), reaching.end(),
                           [&](int d) { return definitions[d].quad == AT_ENTRY && definitions[d].name == name; });
    }
};

}

std::vector<std::pair<int, std::string>> uninitializedReads(Program &program) {
    std::vector<std::pair<int, std::string>> warnings;
    for (auto &f : program.functions) {
        if (f.quads.empty()) continue;
        for (const auto &[variable, line] : ReachingDefinitions(f).readsBeforeAssignment())
            warnings.push_back({line, "variable '" + variable->name + "' may be used uninitialized in function '" + f.signature + "'"});
    }
    std::sort(warnings.begin(), warnings.end());
    return warnings;
}

}
