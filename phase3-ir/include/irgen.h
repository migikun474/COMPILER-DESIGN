#ifndef IRGEN_H
#define IRGEN_H

/* =====================================================================
   TAC GENERATOR
   ---------------------------------------------------------------------
   One walk over the AST that semantic analysis has annotated. The
   slides' attributes are what the functions below compute:

     E.place          the Operand an expression function returns
     E.code           instructions appended to the function's quad array
     E.true/E.false   the two backpatch lists cond() fills
     S.next           the backpatch list a statement function returns

   and the slides' helpers have the same names: newTemp() (newtmp),
   emit(), makelist(), merge(), backpatch().
   ===================================================================== */

#include <map>
#include <set>
#include <string>
#include <vector>

#include "ast/ast.hpp"
#include "symbol_table/symbol_table.hpp"
#include "tac.h"
#include "types/types.hpp"

namespace tac {

using List = std::vector<int>; /* a backpatch list: indices of jumps with no target yet */

class Generator {
  public:
    explicit Generator(sem::SymbolTable &table) : st(table) {}
    Program generate(const ASTNodePtr &root);

  private:
    /* where an lvalue lives */
    struct LValue {
        enum Kind { Direct, Indexed, Deref } kind = Direct;
        Operand base;       /* Direct / Indexed: the object; Deref: a pointer value */
        Operand off;        /* Indexed: byte offset (constant or computed) */
        long long disp = 0; /* Deref: constant displacement added to the pointer */
        sem::TypePtr type;
    };

    /* a block's local objects that have a destructor, in construction order */
    struct Scope {
        const ASTNode *node = nullptr;
        std::vector<LValue> objects;
    };
    struct LabelInfo {
        int pos = -1;
        size_t objectsBefore = 0; /* objects of its block already constructed at the label */
    };

    struct Breakable {
        bool isSwitch = false;
        size_t scopeDepth = 0; /* scopes open when the loop / switch started */
        List breaks, continues;
        std::vector<std::pair<long long, int>> cases; /* value -> instruction index */
        int defaultPos = -1;
    };

    sem::SymbolTable &st;
    Program prog;
    Function *fn = nullptr;
    int curLine = 0;
    std::vector<Breakable> breakables;
    std::map<const sem::Symbol *, LabelInfo> labels;
    std::map<const sem::Symbol *, std::vector<const ASTNode *>> labelScopes; /* the blocks around each label */
    std::vector<Scope> scopes;
    std::vector<Operand> temporaries;           /* unnamed class objects of the current full expression */
    const sem::Symbol *resultObject = nullptr;  /* the local every `return` names: it is the result itself */
    std::vector<std::pair<sem::Symbol *, const ASTNode *>> dynamicGlobals; /* class objects built at program start */
    std::vector<std::pair<const sem::Symbol *, int>> pendingGotos;
    List returnJumps;                 /* destructor bodies: `return` runs the epilogue first */
    bool inDestructor = false;
    std::vector<ASTNodePtr> localRecords; /* classes declared inside a function body */
    std::map<std::string, int> stringIds;
    std::set<const sem::Symbol *> generated;

    /* ---- slides' helpers ---- */
    int nextQuad() const { return static_cast<int>(fn->quads.size()); }
    int emit(Quad q);
    Operand newTemp(const sem::TypePtr &t);
    static List makelist(int i) { return List{i}; }
    static List merge(List a, const List &b) { a.insert(a.end(), b.begin(), b.end()); return a; }
    void backpatch(const List &l, int target);

    /* ---- small emitters ---- */
    int emitGoto(int target = -1);
    Operand emitBinary(Op op, const Operand &a, const Operand &b, const sem::TypePtr &type, const std::string &note = "");
    void emitAssign(const Operand &dst, const Operand &src);
    Operand icon(long long v, const sem::TypePtr &t = nullptr);
    Operand fcon(double v, const sem::TypePtr &t);
    Operand var(sem::Symbol *s);
    Operand strOperand(const ASTNodePtr &n);
    Operand thisOperand();

    /* ---- functions and declarations ---- */
    void collect(const ASTNodePtr &n);
    void function(const ASTNodePtr &n);
    void buildFrame();
    void globals();
    void globalInit(Global &g, const sem::TypePtr &type, const ASTNodePtr &init, long long base);
    void localDecl(const ASTNodePtr &n);
    void localVariable(const ASTNodePtr &n);
    void initObject(const LValue &obj, const ASTNodePtr &init);
    void scanLabels(const ASTNodePtr &n, std::vector<const ASTNode *> &chain);
    void destroyObject(const LValue &obj);
    void destroyScopes(size_t downTo);
    bool hasObjects(size_t downTo) const;
    struct InitItem {
        long long offset;
        sem::TypePtr type;
        ASTNodePtr value;
        int ch = -1; /* >= 0: one character of a string literal instead of `value` */
    };
    void initItems(const sem::TypePtr &type, const ASTNodePtr &init, long long base, std::vector<InitItem> &out);
    void initAggregate(const LValue &obj, const ASTNodePtr &init);
    void scalarLeaves(const sem::TypePtr &type, long long base, std::vector<std::pair<long long, sem::TypePtr>> &out);

    /* ---- objects ---- */
    bool needsConstruction(const sem::TypePtr &t);
    void defaultConstruct(const Operand &addr, const sem::TypePtr &t);
    void constructSubobjects(const Operand &addr, sem::RecordInfo *rec);
    void constructInto(const Operand &addr, sem::RecordInfo *rec, sem::Symbol *ctor,
                       const std::vector<ASTNodePtr> &args);
    void destroy(const Operand &addr, sem::RecordInfo *rec);
    void destroySubobjects(const Operand &addr, sem::RecordInfo *rec);

    /* ---- statements: each returns its S.next list ---- */
    List stmt(const ASTNodePtr &n);
    List block(const ASTNodePtr &n);
    Breakable *innermostLoop();

    /* ---- expressions ---- */
    Operand rvalue(const ASTNodePtr &n, bool discard = false);
    LValue lvalue(const ASTNodePtr &n);
    LValue lvalueOrTemp(const ASTNodePtr &n);
    LValue indexLValue(const ASTNodePtr &n);
    void cond(const ASTNodePtr &n, List &trueList, List &falseList);
    int relJump(const ASTNodePtr &n);
    Operand boolValue(const ASTNodePtr &n);
    Operand binary(const ASTNodePtr &n);
    Operand unary(const ASTNodePtr &n, bool discard);
    Operand assignment(const ASTNodePtr &n, bool discard);
    Operand incDec(const ASTNodePtr &operand, bool increment, bool prefix, bool discard);
    Operand ternary(const ASTNodePtr &n, bool discard);
    Operand construct(const ASTNodePtr &n);
    Operand builtin(const ASTNodePtr &n, bool discard);
    Operand callExpr(const ASTNodePtr &n, bool discard);
    Operand overloaded(const ASTNodePtr &n);
    Operand call(sem::Symbol *callee, const Operand &thisArg, const std::vector<ASTNodePtr> &args,
                 const std::vector<Operand> &extraArgs, bool wantResult);
    bool isOverloaded(const ASTNodePtr &n) const;
    bool isLValueKind(const ASTNodePtr &n) const;

    Operand load(const LValue &lv);
    void store(const LValue &lv, const Operand &v);
    Operand address(const LValue &lv);
    LValue addOffset(LValue lv, const Operand &off, const sem::TypePtr &type);
    LValue member(LValue lv, long long offset, const sem::TypePtr &type);
    Operand pointerAdd(const Operand &p, const Operand &byteOffset, bool subtract = false);
    Operand scaled(const Operand &index, long long width, const std::string &note = "");
    Operand convert(const Operand &v, const sem::TypePtr &to);
    Operand argumentFor(const sem::TypePtr &param, const ASTNodePtr &arg);
    Operand promoteVariadic(const Operand &v);
    Operand referenceTo(const ASTNodePtr &n, const sem::TypePtr &elem);
    Operand copyOf(const ASTNodePtr &n, const sem::TypePtr &type, bool returned);
    void destroyStatics();
    Operand temporary(const Operand &t);
    void keep(const Operand &t);
    void destroyTemporaries(size_t from = 0);
    bool isExisting(const ASTNodePtr &n) const;
    bool inMain() const { return fn && fn->sym && fn->sym->name == "main" && !fn->sym->ownerRecord; }
    sem::RecordInfo *currentClass() const;
};

/* offset of the `base` sub-object inside a `derived` object; false if
   `base` is not a base class of `derived` */
bool baseOffset(const sem::RecordInfo *derived, const sem::RecordInfo *base, long long &offset);
inline sem::TypePtr strip(const sem::TypePtr &t) { return sem::isReference(t) ? t->elem : t; }
inline long long alignUp(long long v, long long a) { return a > 1 ? (v + a - 1) / a * a : v; }

/* a class with a destructor, or with a base or member that has one */
bool needsDestruction(const sem::TypePtr &t);

} // namespace tac

#endif
