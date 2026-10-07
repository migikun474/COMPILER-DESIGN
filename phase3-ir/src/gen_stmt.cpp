/* TAC for statements, declarations and whole functions. A statement
   function returns S.next: the jumps that must go to whatever follows. */
#include <algorithm>
#include <cstdlib>

#include "irgen.h"

namespace tac {

using sem::RecordInfo;
using sem::TypePtr;

static TypePtr strip(const TypePtr &t) { return sem::isReference(t) ? t->elem : t; }

static long long alignUp(long long v, long long a) { return a > 1 ? (v + a - 1) / a * a : v; }

/* ---------------- statements ---------------- */

Generator::Breakable *Generator::innermostLoop() {
    for (auto it = breakables.rbegin(); it != breakables.rend(); ++it)
        if (!it->isSwitch) return &*it;
    return nullptr;
}

/* ---------------- destructors at scope exit ---------------- */

void Generator::destroyObject(const LValue &obj) {
    TypePtr t = obj.type;
    long long count = 1;
    while (sem::isArray(t)) {
        count *= std::max(0LL, t->arraySize);
        t = t->elem;
    }
    if (!sem::isRecord(t)) return;
    long long w = std::max(1LL, sem::sizeOf(t));
    for (long long i = count; i-- > 0;) { /* elements of an array in reverse */
        LValue e = count == 1 && !sem::isArray(obj.type) ? obj : addOffset(obj, icon(i * w), t);
        e.type = t;
        destroy(address(e), t->record.get());
    }
}

bool Generator::hasObjects(size_t downTo) const {
    for (size_t i = downTo; i < scopes.size(); ++i)
        if (!scopes[i].objects.empty()) return true;
    return false;
}

/* leaving every scope from the innermost down to index `downTo`: their
   objects are destroyed in reverse order of construction */
void Generator::destroyScopes(size_t downTo) {
    for (size_t i = scopes.size(); i-- > downTo;) {
        std::vector<LValue> objects = scopes[i].objects;
        for (auto o = objects.rbegin(); o != objects.rend(); ++o) destroyObject(*o);
    }
}

/* which blocks enclose each label: a `goto` out of a block must destroy
   that block's objects, and the label may come later in the function */
void Generator::scanLabels(const ASTNodePtr &n, std::vector<const ASTNode *> &chain) {
    if (!n) return;
    switch (n->kind) {
        case ASTKind::StructDecl: case ASTKind::ClassDecl: case ASTKind::FunctionDef:
            return; /* a local class's functions have their own labels */
        case ASTKind::LabeledStmt:
            labelScopes[n->symbol.get()] = chain;
            break;
        default:
            break;
    }
    bool opens = n->kind == ASTKind::CompoundStmt || n->kind == ASTKind::ForStmt;
    if (opens) chain.push_back(n.get());
    for (const auto &c : n->children) scanLabels(c, chain);
    if (opens) chain.pop_back();
}

List Generator::block(const ASTNodePtr &n) {
    scopes.push_back({n.get(), {}});
    List next;
    for (const auto &s : n->children) {
        backpatch(next, nextQuad()); /* S1.next = the first instruction of S2 */
        next = stmt(s);
    }
    if (!scopes.back().objects.empty()) {
        /* falling out of the block runs its destructors; skipped when the
           block cannot end by falling out (it ends in a jump nothing passes) */
        bool reachable = !next.empty() || fn->quads.empty() ||
                         (fn->quads.back().op != Op::Return && fn->quads.back().op != Op::Goto);
        for (const auto &l : labels)
            if (l.second.pos == nextQuad()) reachable = true;
        for (const auto &q : fn->quads)
            if ((q.op == Op::Goto || q.op == Op::IfRel) && q.target == nextQuad()) reachable = true;
        if (reachable) {
            backpatch(next, nextQuad());
            next.clear();
            destroyScopes(scopes.size() - 1);
        }
    }
    scopes.pop_back();
    return next;
}

List Generator::stmt(const ASTNodePtr &n) {
    if (!n) return {};
    if (n->line) curLine = n->line;
    auto child = [&](size_t i) -> ASTNodePtr { return i < n->children.size() ? n->children[i] : nullptr; };
    switch (n->kind) {
        case ASTKind::CompoundStmt:
            return block(n);
        case ASTKind::ExprStmt:
            rvalue(child(0), true);
            return {};
        case ASTKind::EmptyStmt:
            return {};
        case ASTKind::VarDecl: case ASTKind::DeclGroup: case ASTKind::StructDecl: case ASTKind::ClassDecl:
        case ASTKind::FunctionDecl: case ASTKind::TypedefDecl:
            localDecl(n);
            return {};

        case ASTKind::IfStmt: {
            /* E.code ; E.true: S1 ; goto S.next ; E.false: S2 */
            List trueList, falseList;
            cond(child(0), trueList, falseList);
            backpatch(trueList, nextQuad());
            List next = stmt(child(1));
            if (!child(2)) return merge(next, falseList);
            next.push_back(emitGoto());
            backpatch(falseList, nextQuad());
            return merge(next, stmt(child(2)));
        }
        case ASTKind::WhileStmt:
        case ASTKind::UntilStmt: {
            /* S.begin: E.code ; E.true: S1 ; goto S.begin      (until: the lists swap) */
            int begin = nextQuad();
            List trueList, falseList;
            if (n->kind == ASTKind::WhileStmt) cond(child(0), trueList, falseList);
            else cond(child(0), falseList, trueList);
            backpatch(trueList, nextQuad());
            breakables.push_back(Breakable());
            breakables.back().scopeDepth = scopes.size();
            List bodyNext = stmt(child(1));
            Breakable loop = breakables.back();
            breakables.pop_back();
            backpatch(merge(bodyNext, loop.continues), begin);
            emitGoto(begin);
            return merge(falseList, loop.breaks);
        }
        case ASTKind::DoWhileStmt: {
            int begin = nextQuad();
            breakables.push_back(Breakable());
            breakables.back().scopeDepth = scopes.size();
            List bodyNext = stmt(child(0));
            Breakable loop = breakables.back();
            breakables.pop_back();
            backpatch(merge(bodyNext, loop.continues), nextQuad());
            List trueList, falseList;
            cond(child(1), trueList, falseList);
            backpatch(trueList, begin);
            return merge(falseList, loop.breaks);
        }
        case ASTKind::ForStmt: {
            /* children: init, condition, [step,] body */
            bool hasStep = n->children.size() == 4;
            ASTNodePtr init = child(0), test = child(1), step = hasStep ? child(2) : nullptr;
            ASTNodePtr body = child(hasStep ? 3 : 2);
            scopes.push_back({n.get(), {}}); /* `for (Dog d; ...)`: d lives as long as the loop */
            backpatch(stmt(init), nextQuad());
            int begin = nextQuad();
            List trueList, falseList;
            if (test && test->kind == ASTKind::ExprStmt && !test->children.empty()) {
                cond(test->children[0], trueList, falseList);
                backpatch(trueList, nextQuad());
            }
            breakables.push_back(Breakable());
            breakables.back().scopeDepth = scopes.size();
            List bodyNext = stmt(body);
            Breakable loop = breakables.back();
            breakables.pop_back();
            backpatch(merge(bodyNext, loop.continues), nextQuad()); /* `continue` runs the step */
            if (step) rvalue(step, true);
            emitGoto(begin);
            List exits = merge(falseList, loop.breaks);
            if (!scopes.back().objects.empty()) {
                backpatch(exits, nextQuad());
                exits.clear();
                destroyScopes(scopes.size() - 1);
            }
            scopes.pop_back();
            return exits;
        }
        case ASTKind::SwitchStmt: {
            /* t = E ; goto test ; body ; goto next ; test: if t == v1 goto L1 ... goto default */
            Operand subject = rvalue(child(0));
            TypePtr T = sem::integerPromotion(subject.type ? strip(subject.type) : sem::intType());
            Operand t = newTemp(T);
            emitAssign(t, convert(subject, T));
            int toTests = emitGoto();
            Breakable sw;
            sw.isSwitch = true;
            sw.scopeDepth = scopes.size();
            breakables.push_back(sw);
            List bodyNext = stmt(child(1));
            sw = breakables.back();
            breakables.pop_back();
            bodyNext.push_back(emitGoto());
            backpatch(makelist(toTests), nextQuad());
            for (const auto &c : sw.cases) {
                Quad q;
                q.op = Op::IfRel;
                q.a = t;
                q.b = icon(c.first, T);
                q.relop = "==";
                q.cls = classOf(T);
                q.target = c.second;
                emit(q);
            }
            if (sw.defaultPos >= 0) emitGoto(sw.defaultPos);
            return merge(bodyNext, sw.breaks);
        }
        case ASTKind::CaseStmt: {
            for (auto it = breakables.rbegin(); it != breakables.rend(); ++it) {
                if (!it->isSwitch) continue;
                it->cases.push_back({child(0) ? child(0)->constValue : 0, nextQuad()});
                break;
            }
            return stmt(child(1));
        }
        case ASTKind::DefaultStmt: {
            for (auto it = breakables.rbegin(); it != breakables.rend(); ++it) {
                if (!it->isSwitch) continue;
                it->defaultPos = nextQuad();
                break;
            }
            return stmt(child(0));
        }
        case ASTKind::BreakStmt:
            if (!breakables.empty()) {
                destroyScopes(breakables.back().scopeDepth); /* the blocks being left */
                breakables.back().breaks.push_back(emitGoto());
            }
            return {};
        case ASTKind::ContinueStmt:
            if (Breakable *loop = innermostLoop()) {
                destroyScopes(loop->scopeDepth);
                loop->continues.push_back(emitGoto());
            }
            return {};
        case ASTKind::ReturnStmt: {
            if (inDestructor) { /* the epilogue destroys the members first */
                destroyScopes(0);
                returnJumps.push_back(emitGoto());
                return {};
            }
            Quad q;
            q.op = Op::Return;
            TypePtr ret = fn->sym && fn->sym->type ? fn->sym->type->ret : nullptr;
            bool noValue = !ret || sem::isVoid(ret) || fn->sym->isConstructor;
            if (child(0)) {
                if (noValue) rvalue(child(0), true);
                else if (sem::isReference(ret)) q.a = referenceTo(child(0), ret->elem);
                else if (sem::isRecord(ret)) q.a = rvalue(child(0));
                else q.a = convert(rvalue(child(0)), ret);
            }
            if (hasObjects(0)) {
                /* the value is computed first, then the locals are destroyed */
                if (q.a.kind == Operand::Var) {
                    Operand saved = newTemp(q.a.type);
                    emitAssign(saved, q.a);
                    q.a = saved;
                }
                destroyScopes(0);
            }
            emit(q);
            return {};
        }
        case ASTKind::GotoStmt: {
            const sem::Symbol *label = n->symbol.get();
            /* blocks the jump leaves: those not around the label too */
            const std::vector<const ASTNode *> &around = labelScopes[label];
            size_t common = 0;
            while (common < scopes.size() && common < around.size() && scopes[common].node == around[common]) ++common;
            destroyScopes(common);
            auto known = labels.find(label);
            if (known != labels.end() && common > 0 && common == around.size()) {
                /* a jump backwards in the same block passes the declarations
                   made after the label again: those objects are destroyed */
                std::vector<LValue> objects = scopes[common - 1].objects;
                for (size_t i = objects.size(); i-- > known->second.objectsBefore;) destroyObject(objects[i]);
            }
            int j = emitGoto(known != labels.end() ? known->second.pos : -1);
            if (known == labels.end()) pendingGotos.push_back({label, j});
            return {};
        }
        case ASTKind::LabeledStmt: {
            const sem::Symbol *label = n->symbol.get();
            labels[label] = {nextQuad(), scopes.empty() ? 0 : scopes.back().objects.size()};
            for (auto &g : pendingGotos)
                if (g.first == label) fn->quads[g.second].target = nextQuad();
            return stmt(child(0));
        }
        default:
            return {};
    }
}

/* ---------------- local declarations ---------------- */

void Generator::localDecl(const ASTNodePtr &n) {
    switch (n->kind) {
        case ASTKind::VarDecl:
            localVariable(n);
            break;
        case ASTKind::DeclGroup:
            for (const auto &c : n->children) localDecl(c);
            break;
        case ASTKind::StructDecl: case ASTKind::ClassDecl:
            localRecords.push_back(n); /* its member functions are generated after this one */
            break;
        default:
            break;
    }
}

void Generator::localVariable(const ASTNodePtr &n) {
    sem::Symbol *s = n->symbol.get();
    if (!s || s->kind != sem::SymbolKind::Variable) return;
    if (s->storage != sem::Storage::Local) return; /* static / extern: data, not code (see globals()) */
    if (n->line) curLine = n->line;
    ASTNodePtr init = n->children.empty() ? nullptr : n->children[0];
    TypePtr T = s->type;
    LValue obj;
    obj.kind = LValue::Direct;
    obj.base = var(s);
    obj.type = T;

    if (sem::isReference(T)) { /* int &r = x;   r holds the address of x */
        if (!init) return;
        ASTNodePtr target = init;
        if (init->kind == ASTKind::ConstructExpr && !init->typeExpr && init->children.size() == 1) target = init->children[0];
        Operand dst = var(s);
        dst.type = sem::pointerTo(T->elem);
        emitAssign(dst, referenceTo(target, T->elem));
        return;
    }
    if (sem::isRecord(T) || sem::isArray(T)) {
        initObject(obj, init);
        if (!scopes.empty() && needsDestruction(T)) scopes.back().objects.push_back(obj); /* destroyed at scope exit */
        return;
    }
    if (!init) return;
    ASTNodePtr value = init;
    if (init->kind == ASTKind::InitializerList || (init->kind == ASTKind::ConstructExpr && !init->typeExpr)) {
        if (init->children.empty()) { /* int x = {};   int x(); */
            emitAssign(obj.base, isFloatCls(classOf(T)) ? fcon(0, T) : icon(0, T));
            return;
        }
        value = init->children[0];
    }
    Operand dst = obj.base;
    emitAssign(dst, convert(rvalue(value), T));
}

/* a struct, class object or array being created: constructor call,
   brace list, or a copy of another object */
void Generator::initObject(const LValue &obj, const ASTNodePtr &init) {
    const TypePtr &T = obj.type;
    if (sem::isArray(T)) {
        if (init) initAggregate(obj, init);
        else if (needsConstruction(T)) defaultConstruct(address(obj), T);
        return;
    }
    RecordInfo *rec = T->record.get();
    if (!init) {
        if (needsConstruction(T)) defaultConstruct(address(obj), T);
    } else if (init->kind == ASTKind::InitializerList) {
        initAggregate(obj, init);
    } else if (init->kind == ASTKind::ConstructExpr && sem::isRecord(strip(init->semType)) &&
               strip(init->semType)->record.get() == rec) { /* Dog d(4);  Dog d = Dog(4); */
        constructInto(address(obj), rec, init->symbol.get(), init->children);
    } else if (init->symbol && init->symbol->isConstructor && !sem::isRecord(strip(init->semType))) {
        /* Dog d = 4;  a converting constructor */
        Operand a = address(obj);
        sem::Symbol *ctor = init->symbol.get();
        Operand v = convert(rvalue(init), ctor->type->params.empty() ? init->semType : ctor->type->params[0]);
        call(ctor, a, {}, {v}, false);
    } else {
        store(obj, rvalue(init));
    }
}

/* every scalar an aggregate is made of, in address order */
void Generator::scalarLeaves(const TypePtr &type, long long base, std::vector<std::pair<long long, TypePtr>> &out) {
    if (sem::isArray(type)) {
        long long w = std::max(1LL, sem::sizeOf(type->elem));
        for (long long i = 0; i < type->arraySize; ++i) scalarLeaves(type->elem, base + i * w, out);
    } else if (sem::isRecord(type)) {
        for (const auto &f : type->record->fields)
            if (f->storage == sem::Storage::Member) scalarLeaves(f->type, base + f->offset, out);
    } else {
        out.push_back({base, type});
    }
}

/* which value initializes which offset: the same walk semantic analysis
   did to check the list (positions, designators, brace elision) */
void Generator::initItems(const TypePtr &type, const ASTNodePtr &init, long long base, std::vector<InitItem> &out) {
    if (!init) return;
    if (sem::isArray(type) && init->kind == ASTKind::StringLiteral) { /* char s[] = "hi"; */
        std::string text = init->label.size() >= 2 ? init->label.substr(1, init->label.size() - 2) : "";
        std::vector<int> chars;
        for (size_t i = 0; i < text.size(); ++i) {
            char c = text[i];
            if (c == '\\' && i + 1 < text.size()) {
                char e = text[++i];
                c = e == 'n' ? '\n' : e == 't' ? '\t' : e == '0' ? '\0' : e == 'r' ? '\r' : e;
            }
            chars.push_back(static_cast<unsigned char>(c));
        }
        chars.push_back(0);
        for (size_t i = 0; i < chars.size() && (type->arraySize < 0 || static_cast<long long>(i) < type->arraySize); ++i)
            out.push_back({base + static_cast<long long>(i), type->elem, nullptr, chars[i]});
        return;
    }
    if (init->kind != ASTKind::InitializerList) {
        out.push_back({base, type, init, -1});
        return;
    }
    const auto &items = init->children;
    if (sem::isArray(type)) {
        TypePtr elem = type->elem;
        long long w = std::max(1LL, sem::sizeOf(elem));
        bool designated = std::any_of(items.begin(), items.end(),
                                      [](const ASTNodePtr &c) { return c->kind == ASTKind::DesignatedInit; });
        bool flat = !designated && sem::isArray(elem) &&
                    std::none_of(items.begin(), items.end(), [](const ASTNodePtr &c) {
                        return c->kind == ASTKind::InitializerList || c->kind == ASTKind::StringLiteral;
                    });
        if (flat) { /* int m[2][2] = {1, 2, 3, 4}; */
            TypePtr leaf = elem;
            while (sem::isArray(leaf)) leaf = leaf->elem;
            long long lw = std::max(1LL, sem::sizeOf(leaf));
            for (size_t i = 0; i < items.size(); ++i) initItems(leaf, items[i], base + static_cast<long long>(i) * lw, out);
            return;
        }
        long long pos = 0;
        for (const auto &c : items) {
            ASTNodePtr value = c;
            if (c->kind == ASTKind::DesignatedInit && c->children.size() == 2) {
                pos = c->children[0]->constValue;
                value = c->children[1];
            }
            initItems(elem, value, base + pos * w, out);
            ++pos;
        }
        return;
    }
    if (sem::isRecord(type)) {
        RecordInfo *rec = type->record.get();
        std::vector<sem::SymbolPtr> fields;
        for (const auto &f : rec->fields)
            if (f->storage == sem::Storage::Member) fields.push_back(f);
        size_t pos = 0;
        for (const auto &c : items) {
            ASTNodePtr value = c;
            if (c->kind == ASTKind::DesignatedInit && !c->children.empty()) {
                std::string name = c->label.substr(1);
                auto it = std::find_if(fields.begin(), fields.end(),
                                       [&](const sem::SymbolPtr &f) { return f->name == name; });
                if (it == fields.end()) { /* a member of an unnamed member */
                    if (c->symbol) initItems(c->symbol->type, c->children[0], base + c->symbol->offset, out);
                    for (size_t k = 0; k < fields.size(); ++k) {
                        if (fields[k]->name.empty() && fields[k]->type && fields[k]->type->record &&
                            !sem::lookupMember(fields[k]->type->record.get(), name).symbols.empty()) {
                            pos = k;
                            break;
                        }
                    }
                    ++pos;
                    continue;
                }
                pos = static_cast<size_t>(it - fields.begin());
                value = c->children[0];
            }
            if (pos < fields.size()) initItems(fields[pos]->type, value, base + fields[pos]->offset, out);
            ++pos;
        }
        return;
    }
    if (!items.empty()) initItems(type, items[0], base, out); /* int x = {5}; */
}

/* `T a = { ... };` for a local: one store per initialized element, and
   0 for every element the list leaves out (C's rule) */
void Generator::initAggregate(const LValue &obj, const ASTNodePtr &init) {
    std::vector<InitItem> items;
    initItems(obj.type, init, 0, items);
    std::vector<std::pair<long long, TypePtr>> leaves;
    scalarLeaves(obj.type, 0, leaves);
    auto storeAt = [&](long long offset, const TypePtr &type, const Operand &v) {
        store(addOffset(obj, icon(offset), type), v);
    };
    /* the values are computed in source order; the stores then go out
       in address order, with 0 for what the list leaves out */
    struct Store {
        long long offset;
        TypePtr type;
        Operand value;
    };
    std::vector<Store> stores;
    for (const auto &item : items) {
        Operand v = item.ch >= 0 ? icon(item.ch, item.type)
                    : sem::isRecord(item.type) ? rvalue(item.value)
                                               : convert(rvalue(item.value), item.type);
        auto same = std::find_if(stores.begin(), stores.end(), [&](const Store &s) { return s.offset == item.offset; });
        if (same != stores.end()) *same = {item.offset, item.type, v}; /* a later initializer of the same element wins */
        else stores.push_back({item.offset, item.type, v});
    }
    for (const auto &leaf : leaves) {
        bool covered = false;
        for (const auto &s : stores) {
            long long size = std::max(1LL, sem::sizeOf(s.type));
            if (leaf.first >= s.offset && leaf.first < s.offset + size) covered = true;
        }
        if (covered) continue;
        Cls c = classOf(leaf.second);
        stores.push_back({leaf.first, leaf.second, isFloatCls(c) ? fcon(0, leaf.second) : icon(0, leaf.second)});
    }
    std::stable_sort(stores.begin(), stores.end(), [](const Store &x, const Store &y) { return x.offset < y.offset; });
    for (const auto &s : stores) storeAt(s.offset, s.type, s.value);
}

/* ---------------- globals (static data) ---------------- */

namespace {

struct Constant {
    bool ok = false, isFloat = false;
    long long i = 0;
    double f = 0;
    std::string symbolic; /* "&x", a string literal */
    sem::Symbol *target = nullptr;
    ASTNodePtr text;
    double asDouble() const { return isFloat ? f : static_cast<double>(i); }
};

Constant evaluate(const ASTNodePtr &n) {
    Constant c;
    if (!n) return c;
    if (n->hasConstValue && n->semType && sem::isIntegral(n->semType)) {
        c.ok = true;
        c.i = n->constValue;
        return c;
    }
    switch (n->kind) {
        case ASTKind::FloatLiteral:
            c.ok = c.isFloat = true;
            c.f = std::strtod(n->label.c_str(), nullptr);
            return c;
        case ASTKind::StringLiteral:
            c.ok = true;
            c.symbolic = n->label;
            c.text = n;
            return c;
        case ASTKind::Identifier:
            if (n->symbol && sem::isArray(n->symbol->type)) {
                c.ok = true;
                c.symbolic = "&" + n->symbol->uniqueName;
                c.target = n->symbol.get();
            }
            return c;
        case ASTKind::UnaryExpr: {
            if (n->label == "&" && n->children[0]->kind == ASTKind::Identifier && n->children[0]->symbol) {
                c.ok = true;
                c.symbolic = "&" + n->children[0]->symbol->uniqueName;
                c.target = n->children[0]->symbol.get();
                return c;
            }
            Constant v = evaluate(n->children[0]);
            if (!v.ok || !v.symbolic.empty()) return c;
            c = v;
            if (n->label == "-") { c.i = -c.i; c.f = -c.f; }
            return c;
        }
        case ASTKind::CastExpr: case ASTKind::ConstructExpr: {
            if (n->children.size() != 1) return c;
            Constant v = evaluate(n->children[0]);
            if (!v.ok || !v.symbolic.empty()) return v;
            c.ok = true;
            c.isFloat = n->semType && sem::isFloating(n->semType);
            if (c.isFloat) c.f = v.asDouble();
            else c.i = v.isFloat ? static_cast<long long>(v.f) : v.i;
            return c;
        }
        case ASTKind::TernaryExpr: {
            Constant test = evaluate(n->children[0]);
            if (!test.ok || !test.symbolic.empty()) return c;
            return evaluate(n->children[test.asDouble() != 0 ? 1 : 2]);
        }
        case ASTKind::BinaryExpr: {
            Constant a = evaluate(n->children[0]), b = evaluate(n->children[1]);
            if (!a.ok || !b.ok || !a.symbolic.empty() || !b.symbolic.empty()) return c;
            double x = a.asDouble(), y = b.asDouble();
            const std::string &op = n->label;
            c.ok = true;
            c.isFloat = n->semType && sem::isFloating(n->semType);
            double r = 0;
            if (op == "+") r = x + y;
            else if (op == "-") r = x - y;
            else if (op == "*") r = x * y;
            else if (op == "/" && y != 0) r = x / y;
            else if (op == "<") r = x < y;
            else if (op == ">") r = x > y;
            else if (op == "<=") r = x <= y;
            else if (op == ">=") r = x >= y;
            else if (op == "==") r = x == y;
            else if (op == "!=") r = x != y;
            else c.ok = false;
            c.f = r;
            c.i = static_cast<long long>(r);
            return c;
        }
        default:
            return c;
    }
}

} // namespace

void Generator::globalInit(Global &g, const TypePtr &type, const ASTNodePtr &init, long long base) {
    std::vector<InitItem> items;
    initItems(type, init, base, items);
    for (const auto &item : items) {
        GlobalInit gi;
        gi.offset = item.offset;
        gi.cls = classOf(item.type);
        if (item.ch >= 0) {
            gi.i = item.ch;
            gi.value = std::to_string(item.ch);
        } else {
            Constant c = evaluate(item.value);
            if (!c.ok) {
                gi.value = "?";
                prog.unsupported.push_back("initializer of '" + g.sym->uniqueName +
                                           "' is a constant expression this generator cannot evaluate");
            } else if (c.text) {
                gi.kind = GlobalInit::String;
                gi.str = strOperand(c.text).str;
                gi.value = c.symbolic;
            } else if (c.target) {
                gi.kind = GlobalInit::Address;
                gi.target = c.target;
                gi.value = c.symbolic;
            } else if (isFloatCls(gi.cls)) {
                gi.kind = GlobalInit::Floating;
                gi.f = gi.cls == Cls::Float ? static_cast<float>(c.asDouble()) : c.asDouble();
                gi.value = floatText(gi.f);
            } else {
                gi.i = c.isFloat ? static_cast<long long>(c.f) : c.i;
                if (sem::isIntegral(item.type)) gi.i = sem::wrapToType(gi.i, item.type);
                gi.value = sem::isIntegral(item.type) ? sem::constantToString(gi.i, item.type) : std::to_string(gi.i);
            }
        }
        g.init.push_back(gi);
    }
}

/* every object with static storage: file-scope variables, static locals
   and static data members. Their initializers are constants, so they
   become data, not code. */
void Generator::globals() {
    for (const auto &s : st.allSymbols()) {
        bool object = s->kind == sem::SymbolKind::Variable || s->kind == sem::SymbolKind::Field;
        bool isStaticData = s->storage == sem::Storage::Global || s->storage == sem::Storage::Static;
        if (!object || !isStaticData || !s->type) continue;
        if (s->kind == sem::SymbolKind::Variable && s->storage == sem::Storage::Global && !s->isDefined) continue; /* extern */
        Global g;
        g.sym = s;
        const ASTNode *decl = s->declNode;
        ASTNodePtr init = decl && decl->kind == ASTKind::VarDecl && !decl->children.empty() ? decl->children[0] : nullptr;
        bool listOrNone = !init || init->kind == ASTKind::InitializerList || init->kind == ASTKind::StringLiteral;
        if ((sem::isRecord(s->type) || sem::isArray(s->type)) && (needsConstruction(s->type) || !listOrNone)) {
            dynamicGlobals.push_back({s.get(), decl}); /* a constructor has to run: done when main starts */
        } else if (init) {
            if (init->kind == ASTKind::ConstructExpr && !init->typeExpr && init->children.size() == 1) init = init->children[0];
            globalInit(g, s->type, init, 0);
        }
        prog.globals.push_back(g);
    }
}

/* ---------------- functions ---------------- */

/* Lecture 25: enter(table, name, type, offset) for every name of the
   procedure, addwidth(table, total) at its end */
void Generator::buildFrame() {
    long long offset = 0;
    auto enter = [&](sem::Symbol *sym, const std::string &name, const std::string &kind, const TypePtr &type) {
        TypePtr t = type;
        long long width = sem::isReference(t) ? 4 : std::max(0LL, sem::sizeOf(t));
        long long align = sem::isReference(t) ? 4 : sem::alignOf(t);
        offset = alignUp(offset, align);
        fn->frame.push_back({sym, name, kind, t, width, offset});
        offset += width;
    };
    if (fn->thisSym) enter(fn->thisSym, "this", "param", fn->thisSym->type);
    if (fn->sym) {
        for (const auto &p : fn->sym->params) enter(p.get(), p->name.empty() ? "(unnamed)" : p->uniqueName, "param", p->type);
        for (const auto &l : fn->sym->locals)
            if (l->storage == sem::Storage::Local) enter(l.get(), l->uniqueName, "local", l->type);
    }
    for (size_t i = 0; i < fn->temps.size(); ++i) enter(nullptr, "t" + std::to_string(i + 1), "temp", fn->temps[i]);
    fn->frameWidth = alignUp(offset, 4);
}

void Generator::function(const ASTNodePtr &n) {
    sem::SymbolPtr sym = n->symbol;
    if (!sym || sym->kind != sem::SymbolKind::Function || n->children.empty()) return;
    ASTNodePtr body = n->children.back();
    if (body->kind != ASTKind::CompoundStmt) return; /* a declaration only */
    if (!generated.insert(sym.get()).second) return;

    prog.functions.emplace_back();
    fn = &prog.functions.back();
    fn->sym = sym;
    fn->signature = signatureOf(*sym);
    fn->linkName = sym->mangledName.empty() ? sym->name : sym->mangledName;
    breakables.clear();
    labels.clear();
    labelScopes.clear();
    scopes.clear();
    pendingGotos.clear();
    returnJumps.clear();
    inDestructor = sym->isDestructor;
    curLine = n->line;

    RecordInfo *cls = sym->ownerRecord;
    if (cls && !sym->isStatic) { /* the hidden first parameter */
        auto self = std::make_shared<sem::Symbol>();
        self->name = self->uniqueName = "this";
        self->kind = sem::SymbolKind::Parameter;
        self->storage = sem::Storage::Param;
        self->type = sem::pointerTo(sem::recordType(cls->shared_from_this()));
        fn->owned.push_back(self);
        fn->thisSym = self.get();
    }
    if (sym->isConstructor && cls) constructSubobjects(thisOperand(), cls); /* bases and members first */
    if (sym->name == "main" && !cls) {
        /* objects with static storage whose constructor must run */
        for (const auto &g : dynamicGlobals) {
            LValue obj;
            obj.kind = LValue::Direct;
            obj.base = var(g.first);
            obj.type = g.first->type;
            initObject(obj, g.second && !g.second->children.empty() ? g.second->children[0] : nullptr);
        }
    }
    std::vector<const ASTNode *> chain;
    scanLabels(body, chain);

    List next = block(body);
    backpatch(merge(next, returnJumps), nextQuad());
    if (sym->isDestructor && cls) destroySubobjects(thisOperand(), cls);

    bool endsInJump = !fn->quads.empty() &&
                      (fn->quads.back().op == Op::Return || fn->quads.back().op == Op::Goto);
    bool endIsTarget = false;
    for (const auto &q : fn->quads)
        if ((q.op == Op::Goto || q.op == Op::IfRel) && q.target == nextQuad()) endIsTarget = true;
    if (!endsInJump || endIsTarget) {
        Quad q;
        q.op = Op::Return;
        if (sym->name == "main" && !cls) q.a = icon(0); /* falling off the end of main returns 0 */
        emit(q);
    }
    buildFrame();
    fn = nullptr;
}

/* every function body in the tree: top level, class members, classes
   declared inside classes */
void Generator::collect(const ASTNodePtr &n) {
    if (!n) return;
    switch (n->kind) {
        case ASTKind::FunctionDef: case ASTKind::ConstructorDef: case ASTKind::DestructorDef:
            function(n);
            break;
        case ASTKind::StructDecl: case ASTKind::ClassDecl: case ASTKind::DeclGroup: case ASTKind::Program:
            for (const auto &c : n->children) collect(c);
            break;
        default:
            break;
    }
}

Program Generator::generate(const ASTNodePtr &root) {
    prog = Program();
    globals();
    collect(root);
    while (!localRecords.empty()) { /* classes declared inside function bodies */
        ASTNodePtr rec = localRecords.back();
        localRecords.pop_back();
        collect(rec);
    }
    int index = 100; /* the slides number instructions from 100 */
    for (auto &f : prog.functions) {
        f.firstIndex = index;
        index += static_cast<int>(f.quads.size());
    }
    return prog;
}

} // namespace tac
