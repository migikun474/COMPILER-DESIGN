/* Statements: blocks, conditions, loops, switch/case, jumps, return. */
#include "semantic.h"

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
    convertible(f->ret, e, "type mismatch: cannot return '%F' from function '" + f->name +
                               "' whose return type is '%T'");
}

} // namespace sem
