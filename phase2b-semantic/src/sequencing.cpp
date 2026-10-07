/* =====================================================================
   SEQUENCE POINTS -- `i = i++` and friends
   ---------------------------------------------------------------------
   Between two sequence points an object may be modified at most once,
   and if it is modified its value may be read only to compute the value
   stored (C11 6.5p2). Papaspyrou's dynamic semantics of C makes this
   precise by giving every operator an evaluation order:

     - the operands of most operators, the two sides of an assignment and
       the function and arguments of a call are *interleaved* (the ⋈ of
       his expression monad): their side effects are unsequenced;
     - `&&`, `||`, `?:` and `,` evaluate their first operand, then reach
       a sequence point (his `seqpt`) before the rest;
     - the end of a full expression is a sequence point.

   This pass is the static counterpart: for each full expression it
   computes, bottom-up, the objects each subexpression writes and reads,
   and reports an object written by one of two interleaved
   subexpressions and read or written by the other -- gcc's
   -Wsequence-point "operation on 'i' may be undefined". Objects are
   named variables and their members (`s.x`); what a pointer or an array
   element designates is not tracked, so the pass never reports a
   conflict that is not there.

   It runs after typing (identifiers already carry their symbols) and
   only warns.
   ===================================================================== */

#include <cstdint>
#include <functional>
#include <map>
#include <set>

#include "semantic.h"

namespace sem {

namespace {

/* an object as an access path: the variable, then member names */
struct Access {
    std::string key;           /* "<symbol address>.x.y" */
    std::string spelling;      /* "s.x" */
};

struct Effects {
    std::map<std::string, const ASTNode *> writes; /* key -> node doing the write */
    /* the writes not yet sequenced before this subexpression's value: an
       enclosing assignment's store may clash only with these (`i = i++`
       is undefined, `i = (i++, i)` and `i = f(i++)` are not) */
    std::map<std::string, const ASTNode *> pending;
    std::map<std::string, std::string> spelling;   /* key -> source spelling */
    std::set<std::string> reads;

    void merge(const Effects &o, bool keepPending = true) {
        for (const auto &[k, at] : o.writes) writes.emplace(k, at);
        if (keepPending)
            for (const auto &[k, at] : o.pending) pending.emplace(k, at);
        for (const auto &[k, s] : o.spelling) spelling.emplace(k, s);
        reads.insert(o.reads.begin(), o.reads.end());
    }
};

/* same object, or one contains the other (`s` and `s.x`) */
bool overlap(const std::string &a, const std::string &b) {
    if (a == b) return true;
    const std::string &shorter = a.size() < b.size() ? a : b, &longer = a.size() < b.size() ? b : a;
    return longer.compare(0, shorter.size(), shorter) == 0 && longer[shorter.size()] == '.';
}

bool isExpressionKind(ASTKind k) {
    switch (k) {
        case ASTKind::BinaryExpr: case ASTKind::UnaryExpr: case ASTKind::PostfixOpExpr: case ASTKind::AssignExpr:
        case ASTKind::TernaryExpr: case ASTKind::CallExpr: case ASTKind::BuiltinCallExpr: case ASTKind::MemberExpr:
        case ASTKind::ArrowExpr: case ASTKind::ScopeExpr: case ASTKind::IndexExpr: case ASTKind::CastExpr:
        case ASTKind::SizeofExpr: case ASTKind::NewExpr: case ASTKind::DeleteExpr:
        case ASTKind::CommaExpr: case ASTKind::ConstructExpr: case ASTKind::InitializerList:
        case ASTKind::DesignatedInit: case ASTKind::IntLiteral: case ASTKind::FloatLiteral: case ASTKind::CharLiteral:
        case ASTKind::StringLiteral: case ASTKind::BoolLiteral: case ASTKind::Identifier: case ASTKind::ThisExpr:
            return true;
        default:
            return false;
    }
}

class Sequencer {
  public:
    explicit Sequencer(std::function<void(const ASTNode *, const std::string &)> report) : report_(std::move(report)) {}

    /* every full expression in the subtree */
    void visit(const ASTNodePtr &n) {
        if (!n) return;
        for (const auto &c : n->children) {
            if (!c) continue;
            if (isExpressionKind(c->kind)) fullExpression(c);
            else visit(c);
        }
    }

  private:
    std::function<void(const ASTNode *, const std::string &)> report_;
    std::set<std::string> reported_; /* one warning per object per full expression */

    void fullExpression(const ASTNodePtr &e) {
        reported_.clear();
        effects(e);
    }

    void conflict(const std::string &key, const Effects &a, const Effects &b, const ASTNode *at) {
        if (!reported_.insert(key).second) return;
        auto s = a.spelling.count(key) ? a.spelling.at(key) : b.spelling.count(key) ? b.spelling.at(key) : key;
        report_(at, "operation on '" + s + "' may be undefined: it is modified and also read or modified "
                    "without an intervening sequence point");
    }

    /* side effects of `parts`, which are interleaved: report every overlap */
    Effects unsequenced(const std::vector<Effects> &parts) {
        for (size_t i = 0; i < parts.size(); ++i) {
            for (size_t j = i + 1; j < parts.size(); ++j) {
                for (const auto &[wk, wat] : parts[j].writes) { /* later write vs earlier access */
                    for (const auto &[k, at] : parts[i].writes)
                        if (overlap(wk, k)) conflict(wk, parts[j], parts[i], wat);
                    for (const auto &k : parts[i].reads)
                        if (overlap(wk, k)) conflict(wk, parts[j], parts[i], wat);
                }
                for (const auto &[wk, wat] : parts[i].writes) /* earlier write vs later read */
                    for (const auto &k : parts[j].reads)
                        if (overlap(wk, k)) conflict(wk, parts[i], parts[j], wat);
            }
        }
        Effects out;
        for (const auto &p : parts) out.merge(p);
        return out;
    }

    /* the object `n` designates, if it is a variable or a member path of one */
    static bool path(const ASTNodePtr &n, Access &a) {
        if (!n) return false;
        if (n->kind == ASTKind::Identifier) {
            const SymbolPtr &s = n->symbol;
            if (!s || (s->kind != SymbolKind::Variable && s->kind != SymbolKind::Parameter)) return false;
            if (s->type && isArray(s->type)) return false; /* an address, not a stored value */
            a.key = std::to_string(reinterpret_cast<std::uintptr_t>(s.get()));
            a.spelling = n->label;
            return true;
        }
        if (n->kind == ASTKind::MemberExpr && !n->children.empty()) {
            if (!path(n->children[0], a)) return false;
            a.key += "." + n->label;
            a.spelling += "." + n->label;
            return true;
        }
        return false;
    }

    Effects read(const Access &a) {
        Effects e;
        e.reads.insert(a.key);
        e.spelling[a.key] = a.spelling;
        return e;
    }

    Effects effects(const ASTNodePtr &n) {
        Effects none;
        if (!n) return none;
        switch (n->kind) {
            case ASTKind::Identifier:
            case ASTKind::MemberExpr: {
                Access a;
                if (path(n, a)) return read(a);
                break; /* `f().x`, `(*p).x`: the operand's effects */
            }
            case ASTKind::SizeofExpr: /* not evaluated */
                return none;
            case ASTKind::BinaryExpr:
                if (n->label == "&&" || n->label == "||") return sequenced(n);
                break;
            case ASTKind::CommaExpr:
            case ASTKind::TernaryExpr: /* condition, then one of two arms */
            case ASTKind::InitializerList: /* C++: left to right */
                return sequenced(n);
            case ASTKind::UnaryExpr:
                if (n->label == "&") {
                    Access a;
                    if (!n->children.empty() && path(n->children[0], a)) return none; /* `&x` does not read x */
                    break;
                }
                if (n->label == "++(pre)" || n->label == "--(pre)") return update(n, n->children[0], n.get());
                break;
            case ASTKind::PostfixOpExpr:
                return update(n, n->children[0], n.get());
            case ASTKind::AssignExpr:
                return assignment(n);
            case ASTKind::CallExpr:
            case ASTKind::BuiltinCallExpr:
            case ASTKind::ConstructExpr:
            case ASTKind::NewExpr: {
                /* function and arguments are interleaved; then a sequence
                   point before the call, so nothing is pending afterwards */
                std::vector<Effects> parts;
                for (const auto &c : n->children) parts.push_back(effects(c));
                Effects out = unsequenced(parts);
                out.pending.clear();
                return out;
            }
            default:
                break;
        }
        std::vector<Effects> parts;
        for (const auto &c : n->children) parts.push_back(effects(c));
        return unsequenced(parts);
    }

    /* `a && b`, `a, b`, `c ? x : y`: a sequence point after the first
       operand, whose writes are then complete; an initializer list is
       sequenced left to right throughout */
    Effects sequenced(const ASTNodePtr &n) {
        Effects out;
        bool list = n->kind == ASTKind::InitializerList;
        for (size_t i = 0; i < n->children.size(); ++i) {
            bool last = i + 1 == n->children.size();
            out.merge(effects(n->children[i]), list ? last : i > 0);
        }
        return out;
    }

    /* `++x`, `x--`: one read-modify-write of x */
    Effects update(const ASTNodePtr &n, const ASTNodePtr &operand, const ASTNode *at) {
        Access a;
        if (!path(operand, a)) return effects(operand);
        (void)n;
        Effects e = read(a);
        e.writes[a.key] = at;
        e.pending[a.key] = at;
        return e;
    }

    /* `x = v`, `x op= v`: the store happens after both sides are computed,
       so v may read x (`i = i + 1`) but not modify it (`i = i++`), and the
       left side's own subexpressions (`a[i] = i++`) are interleaved with v */
    Effects assignment(const ASTNodePtr &n) {
        const ASTNodePtr &lhs = n->children[0], &rhs = n->children[1];
        Effects right = effects(rhs);
        Access a;
        if (!path(lhs, a)) {
            Effects left = effects(lhs); /* `a[i] = ...`, `*p = ...`: only the subexpressions */
            return unsequenced({left, right});
        }
        for (const auto &[k, at] : right.pending) {
            if (overlap(k, a.key)) {
                Effects target;
                target.spelling[a.key] = a.spelling;
                conflict(k, right, target, n.get());
            }
        }
        Effects out = right;
        out.writes[a.key] = n.get();
        out.pending[a.key] = n.get();
        out.spelling[a.key] = a.spelling;
        if (n->label != "=") out.reads.insert(a.key);
        return out;
    }
};

} // namespace

void SemanticAnalyzer::checkSequencing(const ASTNodePtr &root) {
    Sequencer s([this](const ASTNode *at, const std::string &msg) { warning(at, msg, "sequence-point"); });
    s.visit(root);
}

} // namespace sem
