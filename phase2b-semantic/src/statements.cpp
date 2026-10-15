/* Statements: blocks, conditions, loops, switch/case, jumps, return. */
#include "semantic.h"

#include <algorithm>
#include <functional>

#include "diagnostics/diagnostics.hpp"

namespace sem {

static std::string q(const TypePtr &t) { return "'" + typeToString(t) + "'"; }

/* =====================================================================
   statements
   ===================================================================== */

void SemanticAnalyzer::collectLabels(const ASTNodePtr &n, FunctionCtx &ctx) {
    if (!n) return;
    if (n->kind == ASTKind::LabeledStmt) {
        auto it = ctx.labels.find(n->label);
        if (it != ctx.labels.end()) {
            error(n.get(), "redefinition of label '" + n->label + "' (previous definition at line " +
                               displayLine(it->second->line) + ")",
                  "label");
        } else {
            ctx.labels[n->label] = n.get();
        }
    }
    for (const auto &c : n->children) collectLabels(c, ctx);
}

void SemanticAnalyzer::blockItems(const ASTNodePtr &block) {
    for (const auto &s : block->children) statement(s);
}

void SemanticAnalyzer::subStatement(const ASTNodePtr &n, const std::string &scopeLabel) {
    if (!n) return;
    st.enterScope(ScopeKind::Block, scopeLabel);
    if (n->kind == ASTKind::CompoundStmt) blockItems(n);
    else statement(n);
    st.exitScope();
}

void SemanticAnalyzer::condition(const ASTNodePtr &n, const std::string &construct) {
    if (!n) return;
    TypePtr t = value(n);
    if (!isError(t) && !isScalar(t)) {
        error(n.get(), "condition of '" + construct + "' must have a scalar (arithmetic or pointer) type, not " + q(t),
              "invalid-condition");
    }
}

void SemanticAnalyzer::statement(const ASTNodePtr &n) {
    if (!n) return;
    FunctionCtx *f = fn();
    const auto &c = n->children;
    auto child = [&](size_t i) -> ASTNodePtr { return i < c.size() ? c[i] : nullptr; };
    auto loopBody = [&](const ASTNodePtr &body, const std::string &label) {
        f->breakables.push_back('L');
        f->loopDepth++;
        subStatement(body, label);
        f->loopDepth--;
        f->breakables.pop_back();
    };

    switch (n->kind) {
        case ASTKind::CompoundStmt:
            st.enterScope(ScopeKind::Block, "block");
            blockItems(n);
            st.exitScope();
            break;
        case ASTKind::ExprStmt:
            if (child(0)) expr(child(0));
            break;
        case ASTKind::EmptyStmt:
            break;
        case ASTKind::IfStmt:
            condition(child(0), "if");
            subStatement(child(1), "if");
            if (child(2)) subStatement(child(2), "else");
            break;
        case ASTKind::WhileStmt:
            condition(child(0), "while");
            loopBody(child(1), "while");
            break;
        case ASTKind::UntilStmt:
            condition(child(0), "until");
            loopBody(child(1), "until");
            break;
        case ASTKind::DoWhileStmt:
            loopBody(child(0), "do");
            condition(child(1), "do-while");
            break;
        case ASTKind::ForStmt: {
            /* children: init, cond, [incr,] body -- an absent increment
               leaves no child at all */
            st.enterScope(ScopeKind::Block, "for");
            ASTNodePtr init = child(0), cond = child(1);
            ASTNodePtr incr = c.size() == 4 ? c[2] : nullptr;
            ASTNodePtr body = c.empty() ? nullptr : c.back();
            if (init) {
                if (init->kind == ASTKind::ExprStmt || init->kind == ASTKind::EmptyStmt) statement(init);
                else declaration(init, DeclCtx::Local);
            }
            if (cond && cond->kind == ASTKind::ExprStmt) condition(cond->children[0], "for");
            if (incr) expr(incr);
            loopBody(body, "for body");
            st.exitScope();
            break;
        }
        case ASTKind::SwitchStmt: {
            TypePtr t = value(child(0));
            SwitchCtx s;
            if (!isError(t) && !isIntegral(t)) {
                error(child(0).get(), "switch quantity must have an integer type, not " + q(t), "invalid-switch");
                s.subject = errorType();
            } else {
                s.subject = integerPromotion(t);
            }
            f->switches.push_back(s);
            f->breakables.push_back('S');
            subStatement(child(1), "switch");
            f->breakables.pop_back();
            f->switches.pop_back();
            break;
        }
        case ASTKind::CaseStmt: {
            TypePtr t = value(child(0));
            if (f->switches.empty()) {
                error(n.get(), "'case' label not within a switch statement", "misplaced-case");
            } else if (!isError(t)) {
                SwitchCtx &s = f->switches.back();
                if (!isIntegral(t) || !child(0)->hasConstValue) {
                    error(child(0).get(), "case label does not reduce to an integer constant", "non-constant-case");
                } else {
                    long long v = child(0)->constValue;
                    auto prev = s.caseLines.find(v);
                    if (prev != s.caseLines.end()) {
                        error(child(0).get(), "duplicate case value '" + std::to_string(v) +
                                                  "' (previously used at line " + displayLine(prev->second) + ")",
                              "duplicate-case");
                    } else {
                        s.caseLines[v] = n->line;
                    }
                }
            }
            statement(child(1));
            break;
        }
        case ASTKind::DefaultStmt:
            if (f->switches.empty()) {
                error(n.get(), "'default' label not within a switch statement", "misplaced-default");
            } else if (f->switches.back().defaultLine) {
                error(n.get(), "multiple default labels in one switch (previous default at line " +
                                   displayLine(f->switches.back().defaultLine) + ")",
                      "duplicate-default");
            } else {
                f->switches.back().defaultLine = n->line;
            }
            statement(child(0));
            break;
        case ASTKind::LabeledStmt:
            statement(child(0));
            break;
        case ASTKind::BreakStmt:
            if (f->breakables.empty()) error(n.get(), "'break' statement not within a loop or switch", "misplaced-break");
            break;
        case ASTKind::ContinueStmt:
            if (f->loopDepth == 0) error(n.get(), "'continue' statement not within a loop", "misplaced-continue");
            break;
        case ASTKind::ReturnStmt:
            returnStatement(n);
            break;
        case ASTKind::GotoStmt: {
            auto it = f->labels.find(n->label);
            if (it == f->labels.end()) {
                error(n.get(), "use of undeclared label '" + n->label + "' (labels are local to their function)", "label");
            } else {
                n->symbol = it->second->symbol;
                if (n->symbol) n->symbol->useCount++;
            }
            break;
        }
        case ASTKind::VarDecl: case ASTKind::DeclGroup: case ASTKind::FunctionDecl: case ASTKind::TypedefDecl:
        case ASTKind::StructDecl: case ASTKind::ClassDecl:
            declaration(n, DeclCtx::Local);
            break;
        default:
            break;
    }
}

void SemanticAnalyzer::returnStatement(const ASTNodePtr &n) {
    FunctionCtx *f = fn();
    ASTNodePtr e = n->children.empty() ? nullptr : n->children[0];
    if (f->isConstructorLike) {
        if (e) {
            expr(e);
            error(e.get(), std::string(f->fn && f->fn->isDestructor ? "destructor" : "constructor") + " '" + f->name +
                               "' cannot return a value",
                  "return-type");
        }
        return;
    }
    if (isVoid(f->ret)) {
        if (e) {
            TypePtr t = value(e);
            if (!isError(t) && !isVoid(t)) {
                error(e.get(), "void function '" + f->name + "' should not return a value (returning " + q(t) + ")",
                      "return-type");
            }
        }
        return;
    }
    f->sawValueReturn = true; /* even a faulty `return;` -- it gets its own error */
    if (!e) {
        if (!isError(f->ret)) {
            error(n.get(), "non-void function '" + f->name + "' should return a value of type " + q(f->ret),
                  "return-type");
        }
        return;
    }
    if (isReference(f->ret)) {
        checkInitializer(f->ret, e, false, "the return value of '" + f->name + "'");
        return;
    }
    expr(e);
    if (isRecord(f->ret) && !isRecord(decay(e->semType)) && userConvertible(unqualified(f->ret), e)) { /* `return 4;` from a Dog function */
        e->converter = construct(f->ret->record.get(), {e}, e.get(), true);
        return;
    }
    convertible(f->ret, e, "type mismatch: cannot return '%F' from function '" + f->name +
                               "' whose return type is '%T'");
}

/* =====================================================================
   flow checks, run once a function body has been analysed
   ===================================================================== */

static bool constantTrue(const ASTNodePtr &cond) {
    if (!cond) return true; /* `for (;;)` */
    const ASTNodePtr &e = cond->kind == ASTKind::ExprStmt ? (cond->children.empty() ? nullptr : cond->children[0]) : cond;
    return !e || (e->hasConstValue && e->constValue != 0);
}

static bool startsWithLabel(const ASTNodePtr &s) {
    return s && (s->kind == ASTKind::LabeledStmt || s->kind == ASTKind::CaseStmt || s->kind == ASTKind::DefaultStmt);
}

/* a `break` (or `continue`) under `n` that belongs to `n`'s loop / switch */
static bool jumpsOut(const ASTNodePtr &n, ASTKind kind) {
    if (!n) return false;
    if (n->kind == kind) return true;
    switch (n->kind) {
        case ASTKind::WhileStmt: case ASTKind::UntilStmt: case ASTKind::DoWhileStmt: case ASTKind::ForStmt:
            return false; /* its own break / continue */
        case ASTKind::SwitchStmt:
            if (kind == ASTKind::BreakStmt) return false;
            break;
        default:
            break;
    }
    for (const auto &c : n->children)
        if (jumpsOut(c, kind)) return true;
    return false;
}

/* can control fall out of the end of `s`? (a loop on a constant-true
   condition ends only through `break`; a label is reachable by a jump) */
bool SemanticAnalyzer::completes(const ASTNodePtr &s) {
    if (!s) return true;
    const auto &c = s->children;
    auto child = [&](size_t i) -> ASTNodePtr { return i < c.size() ? c[i] : nullptr; };
    switch (s->kind) {
        case ASTKind::CompoundStmt: {
            bool reach = true, told = false;
            for (const auto &item : c) {
                if (startsWithLabel(item)) reach = true;
                if (!reach) {
                    if (!told && item->kind != ASTKind::EmptyStmt) warning(item.get(), "code will never be executed", "unreachable-code");
                    told = true;
                    continue;
                }
                reach = completes(item);
            }
            return reach;
        }
        case ASTKind::IfStmt:
            return completes(child(1)) || !child(2) || completes(child(2));
        case ASTKind::WhileStmt: {
            bool body = completes(child(1));
            (void)body;
            return !constantTrue(child(0)) || jumpsOut(child(1), ASTKind::BreakStmt);
        }
        case ASTKind::UntilStmt: { /* until (0) never ends by itself */
            completes(child(1));
            bool never = child(0) && child(0)->hasConstValue && child(0)->constValue == 0;
            return !never || jumpsOut(child(1), ASTKind::BreakStmt);
        }
        case ASTKind::ForStmt: {
            ASTNodePtr body = c.empty() ? nullptr : c.back();
            completes(body);
            return !constantTrue(child(1)) || jumpsOut(body, ASTKind::BreakStmt);
        }
        case ASTKind::DoWhileStmt: {
            bool body = completes(child(0)) || jumpsOut(child(0), ASTKind::ContinueStmt);
            return (body && !constantTrue(child(1))) || jumpsOut(child(0), ASTKind::BreakStmt);
        }
        case ASTKind::SwitchStmt: {
            bool hasDefault = false;
            std::function<void(const ASTNodePtr &)> find = [&](const ASTNodePtr &n) {
                if (!n || n->kind == ASTKind::SwitchStmt) return;
                if (n->kind == ASTKind::DefaultStmt) hasDefault = true;
                for (const auto &k : n->children) find(k);
            };
            if (child(1)) for (const auto &k : child(1)->children) find(k);
            bool body = completes(child(1));
            return !hasDefault || body || jumpsOut(child(1), ASTKind::BreakStmt);
        }
        case ASTKind::LabeledStmt: return completes(child(0));
        case ASTKind::CaseStmt: return completes(child(1));
        case ASTKind::DefaultStmt: return completes(child(0));
        case ASTKind::ReturnStmt: case ASTKind::GotoStmt: case ASTKind::BreakStmt: case ASTKind::ContinueStmt:
            return false;
        default:
            return true;
    }
}

/* C++ forbids a jump into the scope of a variable past its
   initialization: `goto L; int x = 1; L:` and a `case` label after an
   initialized declaration in the same switch block. `inScope` holds the
   initialized locals visible at the current point. */
void SemanticAnalyzer::jumpScopes(const ASTNodePtr &n, std::vector<const Symbol *> &inScope, JumpWalk &w) {
    if (!n) return;
    auto initialized = [](const ASTNodePtr &d) -> const Symbol * {
        const Symbol *s = d->kind == ASTKind::VarDecl ? d->symbol.get() : nullptr;
        if (!s || s->storage != Storage::Local || !s->type) return nullptr;
        TypePtr t = s->type;
        while (isArray(t)) t = t->elem;
        bool constructed = isRecord(t) && t->record && !t->record->constructors.empty();
        return !d->children.empty() || constructed ? s : nullptr;
    };
    switch (n->kind) {
        case ASTKind::StructDecl: case ASTKind::ClassDecl: case ASTKind::FunctionDef:
            return; /* a local class's member functions are checked on their own */
        case ASTKind::LabeledStmt:
            w.labels[n->symbol.get()] = inScope;
            break;
        case ASTKind::GotoStmt:
            w.gotos.push_back({n.get(), inScope});
            return;
        case ASTKind::SwitchStmt:
            w.switches.push_back(inScope.size());
            for (const auto &c : n->children) jumpScopes(c, inScope, w);
            w.switches.pop_back();
            return;
        case ASTKind::CaseStmt: case ASTKind::DefaultStmt:
            if (!w.switches.empty() && inScope.size() > w.switches.back()) {
                const Symbol *v = inScope.back();
                error(n.get(), "jump to case label crosses the initialization of '" + v->name + "' (line " +
                                   displayLine(v->line) + "); put the case's declarations in a block",
                      "jump-over-init");
            }
            break;
        case ASTKind::VarDecl:
            for (const auto &c : n->children) jumpScopes(c, inScope, w);
            if (const Symbol *s = initialized(n)) inScope.push_back(s);
            return;
        case ASTKind::DeclGroup:
            for (const auto &c : n->children) jumpScopes(c, inScope, w); /* each one in order */
            return;
        default:
            break;
    }
    bool block = n->kind == ASTKind::CompoundStmt || n->kind == ASTKind::ForStmt;
    size_t depth = inScope.size();
    for (const auto &c : n->children) jumpScopes(c, inScope, w);
    if (block) inScope.resize(depth);
}

void SemanticAnalyzer::flowChecks(const ASTNodePtr &body, const Symbol *fnSym, bool valueReturned) {
    bool falls = completes(body);
    if (falls && valueReturned) {
        warning(body->children.empty() ? body.get() : body->children.back().get(),
                "control reaches end of non-void function '" + fnSym->name + "' on some path", "return-type");
    }
    JumpWalk w;
    std::vector<const Symbol *> inScope;
    jumpScopes(body, inScope, w);
    for (const auto &g : w.gotos) {
        auto at = w.labels.find(g.first->symbol.get());
        if (at == w.labels.end()) continue;
        for (const Symbol *v : at->second) {
            if (std::find(g.second.begin(), g.second.end(), v) != g.second.end()) continue;
            error(g.first, "jump to label '" + g.first->label + "' crosses the initialization of '" + v->name +
                               "' (line " + displayLine(v->line) + ")",
                  "jump-over-init");
            break;
        }
    }
}

} // namespace sem
