/* TAC -> MIPS for SPIM. See mips.h for the frame layout and the
   calling convention. */
#include "mips.h"

#include <algorithm>
#include <cstdint>
#include <cstring>
#include <map>
#include <set>
#include <sstream>
#include <vector>

#include "interp.h"

namespace mips {

using namespace tac;
using sem::TypePtr;

namespace {

int roundUp(int v, int a) { return (v + a - 1) / a * a; }
bool isWide(Cls c) { return c == Cls::LLong || c == Cls::ULLong; }
bool isUnsignedCls(Cls c) { return c != Cls::Char && c != Cls::Short && c != Cls::Int && c != Cls::LLong; }

int sizeOfType(const TypePtr &t) {
    if (t && sem::isReference(t)) return 4;
    long long s = sem::sizeOf(t);
    return s > 0 ? static_cast<int>(s) : 4;
}

/* an argument's place in the argument area: (size, alignment) */
std::pair<int, int> slot(const TypePtr &t) {
    Cls c = classOf(t);
    if (c == Cls::Double || isWide(c)) return {8, 8};
    if (c == Cls::Block) return {roundUp(sizeOfType(t), 4), sem::alignOf(t) > 4 ? 8 : 4};
    return {4, 4};
}

struct Emitter {
    const Program &prog;
    std::ostringstream text, data;
    std::map<const sem::Symbol *, std::string> globalLabel;
    std::map<const sem::Symbol *, std::string> functionLabel;
    std::map<std::pair<int, unsigned long long>, std::string> pool; /* floating constants */

    /* the function being generated */
    const Function *fn = nullptr;
    std::string label;                          /* its assembly name */
    std::map<const sem::Symbol *, int> varOff;  /* $fp-relative */
    std::map<int, int> tempOff;
    int frameSize = 0, varargStart = 0, fnIndex = 0, localLabels = 0;
    std::vector<const Quad *> params;           /* `param`s waiting for their call */

    explicit Emitter(const Program &p) : prog(p) {}

    void ins(const std::string &s) { text << "        " << s << "\n"; }
    void lab(const std::string &s) { text << s << ":\n"; }
    std::string fresh() { return "M" + std::to_string(fnIndex) + "_" + std::to_string(localLabels++); }

    /* ---------------- where an operand is ---------------- */

    bool isLocal(const Operand &o) const { return o.kind == Operand::Temp || (o.kind == Operand::Var && varOff.count(o.sym)); }

    std::string mem(const Operand &o, int delta = 0) {
        if (o.kind == Operand::Temp) return std::to_string(tempOff[o.temp] + delta) + "($fp)";
        if (o.kind == Operand::Var) {
            auto local = varOff.find(o.sym);
            if (local != varOff.end()) return std::to_string(local->second + delta) + "($fp)";
            return globalLabel[o.sym] + (delta ? "+" + std::to_string(delta) : "");
        }
        return "0($zero)";
    }

    void address(const std::string &reg, const Operand &o) {
        if (o.kind == Operand::Str) ins("la    " + reg + ", str" + std::to_string(o.str));
        else if (isLocal(o)) ins("addiu " + reg + ", $fp, " + std::to_string(o.kind == Operand::Temp ? tempOff[o.temp] : varOff[o.sym]));
        else ins("la    " + reg + ", " + globalLabel[o.sym]);
    }

    /* ---------------- loads and stores ---------------- */

    /* an integer or pointer of at most 32 bits, extended to the register */
    void loadInt(const std::string &reg, const Operand &o) {
        if (o.kind == Operand::IntConst) { ins("li    " + reg + ", " + std::to_string(static_cast<int32_t>(o.ival))); return; }
        if (o.kind == Operand::Str) { address(reg, o); return; }
        switch (classOf(o.type)) {
            case Cls::Bool: case Cls::UChar: ins("lbu   " + reg + ", " + mem(o)); break;
            case Cls::Char: ins("lb    " + reg + ", " + mem(o)); break;
            case Cls::Short: ins("lh    " + reg + ", " + mem(o)); break;
            case Cls::UShort: ins("lhu   " + reg + ", " + mem(o)); break;
            default: ins("lw    " + reg + ", " + mem(o)); break;
        }
    }

    void storeInt(const std::string &reg, const Operand &dst) {
        switch (classOf(dst.type)) {
            case Cls::Bool: case Cls::Char: case Cls::UChar: ins("sb    " + reg + ", " + mem(dst)); break;
            case Cls::Short: case Cls::UShort: ins("sh    " + reg + ", " + mem(dst)); break;
            default: ins("sw    " + reg + ", " + mem(dst)); break;
        }
    }

    void loadWide(const std::string &lo, const std::string &hi, const Operand &o) {
        if (o.kind == Operand::IntConst) {
            ins("li    " + lo + ", " + std::to_string(static_cast<int32_t>(o.ival)));
            ins("li    " + hi + ", " + std::to_string(static_cast<int32_t>(o.ival >> 32)));
            return;
        }
        ins("lw    " + lo + ", " + mem(o));
        ins("lw    " + hi + ", " + mem(o, 4));
    }

    void storeWide(const std::string &lo, const std::string &hi, const Operand &dst) {
        ins("sw    " + lo + ", " + mem(dst));
        ins("sw    " + hi + ", " + mem(dst, 4));
    }

    /* floating constants live in the data segment as their exact bits */
    std::string constantLabel(double v, bool isDouble) {
        unsigned long long bits = 0;
        if (isDouble) memcpy(&bits, &v, 8);
        else { float f = static_cast<float>(v); uint32_t b; memcpy(&b, &f, 4); bits = b; }
        auto key = std::make_pair(isDouble ? 1 : 0, bits);
        auto it = pool.find(key);
        if (it != pool.end()) return it->second;
        std::string name = "fc" + std::to_string(pool.size());
        pool[key] = name;
        std::ostringstream line;
        line << "        .align 3\n" << name << ":  .word " << static_cast<uint32_t>(bits);
        if (isDouble) line << ", " << static_cast<uint32_t>(bits >> 32);
        line << "        # " << v << "\n";
        data << line.str();
        return name;
    }

    void loadFloat(const std::string &reg, const Operand &o, Cls c) {
        std::string op = c == Cls::Double ? "l.d   " : "l.s   ";
        if (o.kind == Operand::FloatConst) ins(op + reg + ", " + constantLabel(o.fval, c == Cls::Double));
        else if (o.kind == Operand::IntConst) ins(op + reg + ", " + constantLabel(static_cast<double>(o.ival), c == Cls::Double));
        else ins(op + reg + ", " + mem(o));
    }

    void storeFloat(const std::string &reg, const Operand &dst) {
        ins(std::string(classOf(dst.type) == Cls::Double ? "s.d   " : "s.s   ") + reg + ", " + mem(dst));
    }

    /* copy `size` bytes; both addresses are already in $a0 (to) and $a1 (from) */
    void copyBytes(int size) {
        ins("li    $a2, " + std::to_string(size));
        ins("jal   __memcpy");
    }

    /* the value of `o` (any class) stored at offset(base register) */
    void storeValueAt(const Operand &o, Cls c, const std::string &at) {
        if (c == Cls::Block) {
            ins("addiu $a0, " + at.substr(at.find('(') + 1, at.find(')') - at.find('(') - 1) + ", " + at.substr(0, at.find('(')));
            address("$a1", o);
            copyBytes(sizeOfType(o.type));
        } else if (isFloatCls(c)) {
            loadFloat("$f0", o, c);
            ins(std::string(c == Cls::Double ? "s.d   " : "s.s   ") + "$f0, " + at);
        } else if (isWide(c)) {
            loadWide("$t0", "$t1", o);
            std::string base = at.substr(at.find('('));
            int off = std::stoi(at.substr(0, at.find('(')));
            ins("sw    $t0, " + std::to_string(off) + base);
            ins("sw    $t1, " + std::to_string(off + 4) + base);
        } else {
            loadInt("$t0", o);
            ins(std::string(c == Cls::Bool || c == Cls::Char || c == Cls::UChar ? "sb    " : c == Cls::Short || c == Cls::UShort ? "sh    " : "sw    ") + "$t0, " + at);
        }
    }

    /* the value at offset(base register) loaded and stored into `dst` */
    void loadValueFrom(const std::string &at, const Operand &dst) {
        Cls c = classOf(dst.type);
        std::string base = at.substr(at.find('('));
        int off = std::stoi(at.substr(0, at.find('(')));
        if (c == Cls::Block) {
            ins("addiu $a1, " + base.substr(1, base.size() - 2) + ", " + std::to_string(off));
            address("$a0", dst);
            copyBytes(sizeOfType(dst.type));
        } else if (isFloatCls(c)) {
            ins(std::string(c == Cls::Double ? "l.d   " : "l.s   ") + "$f0, " + at);
            storeFloat("$f0", dst);
        } else if (isWide(c)) {
            ins("lw    $t1, " + std::to_string(off + 4) + base);
            ins("lw    $t0, " + at);
            storeWide("$t0", "$t1", dst);
        } else {
            const char *op = c == Cls::Bool || c == Cls::UChar ? "lbu   " : c == Cls::Char ? "lb    " : c == Cls::Short ? "lh    "
                             : c == Cls::UShort ? "lhu   " : "lw    ";
            ins(std::string(op) + "$t0, " + at);
            storeInt("$t0", dst);
        }
    }

    /* ---------------- arithmetic ---------------- */

    void binary(const Quad &q) {
        Cls c = q.cls;
        if (isFloatCls(c)) {
            std::string suffix = c == Cls::Double ? ".d" : ".s";
            loadFloat("$f0", q.a, c);
            loadFloat("$f2", q.b, c);
            const char *op = q.op == Op::Add ? "add" : q.op == Op::Sub ? "sub" : q.op == Op::Mul ? "mul" : "div";
            ins(std::string(op) + suffix + " $f0, $f0, $f2");
            storeFloat("$f0", q.r);
            return;
        }
        if (isWide(c)) {
            bool isUnsigned = c == Cls::ULLong;
            if (q.op == Op::Shl || q.op == Op::Shr) {
                loadWide("$a0", "$a1", q.a);
                loadInt("$a2", q.b);
                ins(std::string("jal   ") + (q.op == Op::Shl ? "__shlll" : isUnsigned ? "__shrll" : "__sarll"));
                storeWide("$v0", "$v1", q.r);
                return;
            }
            if (q.op == Op::Div || q.op == Op::Mod) {
                loadWide("$a0", "$a1", q.a);
                loadWide("$a2", "$a3", q.b);
                ins(std::string("jal   ") + (q.op == Op::Div ? (isUnsigned ? "__udivll" : "__divll") : (isUnsigned ? "__umodll" : "__modll")));
                storeWide("$v0", "$v1", q.r);
                return;
            }
            loadWide("$t0", "$t1", q.a);
            loadWide("$t2", "$t3", q.b);
            switch (q.op) {
                case Op::Add:
                    ins("addu  $t4, $t0, $t2");
                    ins("sltu  $t5, $t4, $t0"); /* carry out of the low word */
                    ins("addu  $t1, $t1, $t3");
                    ins("addu  $t1, $t1, $t5");
                    break;
                case Op::Sub:
                    ins("sltu  $t5, $t0, $t2"); /* borrow */
                    ins("subu  $t4, $t0, $t2");
                    ins("subu  $t1, $t1, $t3");
                    ins("subu  $t1, $t1, $t5");
                    break;
                case Op::Mul:
                    ins("multu $t0, $t2");
                    ins("mflo  $t4");
                    ins("mfhi  $t5");
                    ins("mul   $t6, $t0, $t3");
                    ins("addu  $t5, $t5, $t6");
                    ins("mul   $t6, $t1, $t2");
                    ins("addu  $t1, $t5, $t6");
                    break;
                default: {
                    const char *op = q.op == Op::BitAnd ? "and   " : q.op == Op::BitOr ? "or    " : "xor   ";
                    ins(std::string(op) + "$t4, $t0, $t2");
                    ins(std::string(op) + "$t1, $t1, $t3");
                    break;
                }
            }
            storeWide("$t4", "$t1", q.r);
            return;
        }
        loadInt("$t0", q.a);
        loadInt("$t1", q.b);
        bool isSigned = c == Cls::Int;
        switch (q.op) {
            case Op::Add: ins("addu  $t0, $t0, $t1"); break;
            case Op::Sub: ins("subu  $t0, $t0, $t1"); break;
            case Op::Mul: ins("mul   $t0, $t0, $t1"); break;
            case Op::Div: case Op::Mod:
                ins(std::string(isSigned ? "div   " : "divu  ") + "$t0, $t1");
                ins(q.op == Op::Div ? "mflo  $t0" : "mfhi  $t0");
                break;
            case Op::BitAnd: ins("and   $t0, $t0, $t1"); break;
            case Op::BitOr: ins("or    $t0, $t0, $t1"); break;
            case Op::BitXor: ins("xor   $t0, $t0, $t1"); break;
            case Op::Shl: ins("sllv  $t0, $t0, $t1"); break;
            case Op::Shr: ins(std::string(isSigned ? "srav  " : "srlv  ") + "$t0, $t0, $t1"); break;
            default: break;
        }
        storeInt("$t0", q.r);
    }

    void unary(const Quad &q) {
        Cls c = q.cls;
        if (isFloatCls(c)) {
            loadFloat("$f0", q.a, c);
            ins(std::string(c == Cls::Double ? "neg.d " : "neg.s ") + "$f0, $f0");
            storeFloat("$f0", q.r);
        } else if (isWide(c)) {
            loadWide("$t0", "$t1", q.a);
            if (q.op == Op::Neg) {
                ins("sltu  $t5, $zero, $t0");
                ins("negu  $t0, $t0");
                ins("negu  $t1, $t1");
                ins("subu  $t1, $t1, $t5");
            } else {
                ins("nor   $t0, $t0, $zero");
                ins("nor   $t1, $t1, $zero");
            }
            storeWide("$t0", "$t1", q.r);
        } else {
            loadInt("$t0", q.a);
            ins(q.op == Op::Neg ? "negu  $t0, $t0" : "nor   $t0, $t0, $zero");
            storeInt("$t0", q.r);
        }
    }

    /* an unsigned 32-bit value in `reg`, already converted as if signed into $f0: add 2^32 when it was "negative" */
    void fixUnsigned(const std::string &reg) {
        std::string done = fresh();
        ins("bgez  " + reg + ", " + done);
        ins("l.d   $f2, " + constantLabel(4294967296.0, true));
        ins("add.d $f0, $f0, $f2");
        lab(done);
    }

    void convert(const Quad &q) {
        Cls from = q.from, to = q.cls;
        if (isFloatCls(from)) {
            loadFloat("$f0", q.a, from);
            if (from == Cls::Float) ins("cvt.d.s $f0, $f0"); /* work in double */
            if (to == Cls::Double) { ins("s.d   $f0, " + mem(q.r)); return; }
            if (to == Cls::Float) { ins("cvt.s.d $f0, $f0"); ins("s.s   $f0, " + mem(q.r)); return; }
            if (isWide(to)) {
                ins("mov.d $f12, $f0");
                ins("jal   __dtoll");
                storeWide("$v0", "$v1", q.r);
                return;
            }
            if (isUnsignedCls(to) && to != Cls::Bool) { /* values from 2^31 up do not fit trunc.w */
                std::string small = fresh(), done = fresh();
                ins("l.d   $f2, " + constantLabel(2147483648.0, true));
                ins("c.lt.d $f0, $f2");
                ins("bc1t  " + small);
                ins("sub.d $f0, $f0, $f2");
                ins("trunc.w.d $f0, $f0");
                ins("mfc1  $t0, $f0");
                ins("lui   $t1, 0x8000");
                ins("addu  $t0, $t0, $t1");
                ins("j     " + done);
                lab(small);
                ins("trunc.w.d $f0, $f0");
                ins("mfc1  $t0, $f0");
                lab(done);
            } else {
                ins("trunc.w.d $f0, $f0"); /* C truncates toward zero */
                ins("mfc1  $t0, $f0");
            }
            storeInt("$t0", q.r);
            return;
        }
        if (isWide(from)) {
            loadWide("$t0", "$t1", q.a);
            if (isWide(to)) { storeWide("$t0", "$t1", q.r); return; }
            if (!isFloatCls(to)) { storeInt("$t0", q.r); return; }
            ins("mtc1  $t1, $f0"); /* high word * 2^32 + low word (unsigned) */
            ins("cvt.d.w $f0, $f0");
            if (from == Cls::ULLong) fixUnsigned("$t1");
            ins("l.d   $f4, " + constantLabel(4294967296.0, true));
            ins("mul.d $f6, $f0, $f4");
            ins("mtc1  $t0, $f0");
            ins("cvt.d.w $f0, $f0");
            fixUnsigned("$t0");
            ins("add.d $f0, $f0, $f6");
        } else {
            loadInt("$t0", q.a);
            if (isWide(to)) {
                if (isUnsignedCls(from)) ins("li    $t1, 0");
                else ins("sra   $t1, $t0, 31");
                storeWide("$t0", "$t1", q.r);
                return;
            }
            if (!isFloatCls(to)) { storeInt("$t0", q.r); return; }
            ins("mtc1  $t0, $f0");
            ins("cvt.d.w $f0, $f0");
            if (from == Cls::UInt || from == Cls::Ptr) fixUnsigned("$t0");
        }
        if (to == Cls::Float) ins("cvt.s.d $f0, $f0");
        storeFloat("$f0", q.r);
    }

    void branch(const Quad &q, const std::string &target) {
        Cls c = q.cls;
        const std::string &op = q.relop;
        if (isFloatCls(c)) {
            std::string suffix = c == Cls::Double ? ".d" : ".s";
            loadFloat("$f0", q.a, c);
            loadFloat("$f2", q.b, c);
            bool swap = op == ">" || op == ">=";
            std::string test = op == "==" || op == "!=" ? "c.eq" : op == "<" || op == ">" ? "c.lt" : "c.le";
            ins(test + suffix + (swap ? " $f2, $f0" : " $f0, $f2"));
            ins(std::string(op == "!=" ? "bc1f  " : "bc1t  ") + target);
            return;
        }
        if (isWide(c)) {
            loadWide("$t0", "$t1", q.a);
            loadWide("$t2", "$t3", q.b);
            if (op == "==" || op == "!=") {
                ins("xor   $t4, $t0, $t2");
                ins("xor   $t5, $t1, $t3");
                ins("or    $t4, $t4, $t5");
                ins(std::string(op == "==" ? "beqz  " : "bnez  ") + "$t4, " + target);
                return;
            }
            /* high words decide unless they are equal; then the low words, unsigned */
            bool swap = op == ">" || op == ">=";
            std::string aLo = swap ? "$t2" : "$t0", aHi = swap ? "$t3" : "$t1", bLo = swap ? "$t0" : "$t2", bHi = swap ? "$t1" : "$t3";
            std::string skip = fresh();
            ins(std::string(c == Cls::ULLong ? "bltu  " : "blt   ") + aHi + ", " + bHi + ", " + target);
            ins("bne   " + aHi + ", " + bHi + ", " + skip);
            ins(std::string(op == "<" || op == ">" ? "bltu  " : "bleu  ") + aLo + ", " + bLo + ", " + target);
            lab(skip);
            return;
        }
        loadInt("$t0", q.a);
        loadInt("$t1", q.b);
        bool u = isUnsignedCls(c);
        std::string b = op == "==" ? "beq   " : op == "!=" ? "bne   " : op == "<" ? (u ? "bltu  " : "blt   ") : op == ">" ? (u ? "bgtu  " : "bgt   ")
                        : op == "<=" ? (u ? "bleu  " : "ble   ") : (u ? "bgeu  " : "bge   ");
        ins(b + "$t0, $t1, " + target);
    }

    /* ---------------- calls ---------------- */

    void call(const Quad &q) {
        size_t n = std::min(static_cast<size_t>(q.nargs), params.size());
        std::vector<const Quad *> args(params.end() - static_cast<long>(n), params.end());
        params.resize(params.size() - n);
        std::vector<int> offsets;
        int size = 0;
        for (const Quad *p : args) {
            auto s = slot(p->a.type);
            size = roundUp(size, s.second);
            offsets.push_back(size);
            size += s.first;
        }
        size = roundUp(size, 8);
        if (size) ins("addiu $sp, $sp, -" + std::to_string(size));
        for (size_t i = 0; i < args.size(); ++i) {
            Cls c = classOf(args[i]->a.type);
            bool narrow = c == Cls::Bool || c == Cls::Char || c == Cls::UChar || c == Cls::Short || c == Cls::UShort;
            storeValueAt(args[i]->a, narrow ? Cls::Int : c, std::to_string(offsets[i]) + "($sp)"); /* a full word per small argument */
        }
        ins("jal   " + (q.callee ? functionLabel.count(q.callee) ? functionLabel[q.callee] : "__undefined" : "__" + q.calleeName));
        if (size) ins("addiu $sp, $sp, " + std::to_string(size));
        if (q.r.isNone()) return;
        Cls c = classOf(q.r.type);
        if (c == Cls::Block) {
            ins("move  $a1, $v0"); /* the callee's object: copied before anything can overwrite it */
            address("$a0", q.r);
            copyBytes(sizeOfType(q.r.type));
        } else if (isFloatCls(c)) {
            storeFloat("$f0", q.r);
        } else if (isWide(c)) {
            storeWide("$v0", "$v1", q.r);
        } else {
            storeInt("$v0", q.r);
        }
    }

    /* ---------------- one instruction ---------------- */

    void quad(const Quad &q) {
        Cls rc = classOf(q.r.type);
        switch (q.op) {
            case Op::Assign:
                if (rc == Cls::Block) {
                    address("$a0", q.r);
                    address("$a1", q.a);
                    copyBytes(sizeOfType(q.r.type));
                } else if (isFloatCls(rc)) {
                    loadFloat("$f0", q.a, rc);
                    storeFloat("$f0", q.r);
                } else if (isWide(rc)) {
                    loadWide("$t0", "$t1", q.a);
                    storeWide("$t0", "$t1", q.r);
                } else {
                    loadInt("$t0", q.a);
                    storeInt("$t0", q.r);
                }
                break;
            case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod:
            case Op::BitAnd: case Op::BitOr: case Op::BitXor: case Op::Shl: case Op::Shr:
                binary(q);
                break;
            case Op::Neg: case Op::BitNot:
                unary(q);
                break;
            case Op::Conv:
                convert(q);
                break;
            case Op::Goto:
                ins("j     " + target(q.target));
                break;
            case Op::IfRel:
                branch(q, target(q.target));
                break;
            case Op::IndexLoad:
                address("$t8", q.a);
                loadInt("$t9", q.b);
                ins("addu  $t8, $t8, $t9");
                loadValueFrom("0($t8)", q.r);
                break;
            case Op::IndexStore:
                address("$t8", q.a);
                loadInt("$t9", q.b);
                ins("addu  $t8, $t8, $t9");
                storeValueAt(q.r, q.cls, "0($t8)");
                break;
            case Op::AddrOf:
                address("$t0", q.a);
                ins("sw    $t0, " + mem(q.r));
                break;
            case Op::Load:
                loadInt("$t8", q.a);
                loadValueFrom("0($t8)", q.r);
                break;
            case Op::Store:
                loadInt("$t8", q.a);
                storeValueAt(q.r, q.cls, "0($t8)");
                break;
            case Op::Param:
                params.push_back(&q);
                break;
            case Op::Call:
                call(q);
                break;
            case Op::Return:
                if (!q.a.isNone()) {
                    Cls c = classOf(q.a.type);
                    if (c == Cls::Block) address("$v0", q.a);
                    else if (isFloatCls(c)) loadFloat("$f0", q.a, c);
                    else if (isWide(c)) loadWide("$v0", "$v1", q.a);
                    else loadInt("$v0", q.a);
                }
                ins("j     " + label + "_exit");
                break;
            case Op::VaStart: /* the first argument after the named ones */
                ins("addiu $t0, $fp, " + std::to_string(8 + varargStart));
                ins("sw    $t0, " + mem(q.a));
                break;
            case Op::VaArg: {
                auto s = slot(q.r.type);
                ins("lw    $t8, " + mem(q.a));
                if (s.second == 8) {
                    ins("addiu $t8, $t8, 7");
                    ins("li    $t9, -8");
                    ins("and   $t8, $t8, $t9");
                }
                ins("addiu $t9, $t8, " + std::to_string(s.first));
                ins("sw    $t9, " + mem(q.a));
                loadValueFrom("0($t8)", q.r);
                break;
            }
            case Op::VaEnd:
                break;
        }
    }

    std::string target(int index) { return "L" + std::to_string(fnIndex) + "_" + std::to_string(index); }

    /* ---------------- one function ---------------- */

    void function(const Function &f, int index) {
        fn = &f;
        fnIndex = index;
        localLabels = 0;
        label = functionLabel[f.sym.get()];
        varOff.clear();
        tempOff.clear();
        params.clear();

        /* arguments: above the saved $fp / $ra, in the order they were pushed */
        int at = 0;
        std::vector<const sem::Symbol *> incoming;
        if (f.thisSym) incoming.push_back(f.thisSym);
        for (const auto &p : f.sym->params) incoming.push_back(p.get());
        for (const sem::Symbol *p : incoming) {
            auto s = slot(p->type);
            at = roundUp(at, s.second);
            varOff[p] = 8 + at;
            at += s.first;
        }
        varargStart = at;

        /* locals, and the temporaries the code still uses, below $fp */
        int depth = 0;
        auto place = [&](const TypePtr &t) {
            int size = sizeOfType(t), align = sem::isReference(t) ? 4 : std::max(1, sem::alignOf(t));
            depth = roundUp(depth + size, std::min(align, 8));
            return -depth;
        };
        for (const auto &l : f.sym->locals)
            if (l->storage == sem::Storage::Local) varOff[l.get()] = place(l->type);
        std::set<int> used;
        for (const auto &q : f.quads)
            for (const Operand *o : {&q.a, &q.b, &q.r})
                if (o->kind == Operand::Temp) used.insert(o->temp);
        for (int t : used) tempOff[t] = place(f.temps[t - 1]);
        frameSize = roundUp(depth, 8);

        std::vector<bool> isTarget(f.quads.size() + 1, false);
        for (const auto &q : f.quads)
            if ((q.op == Op::Goto || q.op == Op::IfRel) && q.target >= 0) isTarget[q.target] = true;

        text << "\n# " << f.signature << "\n";
        lab(label);
        ins("addiu $sp, $sp, -8");
        ins("sw    $ra, 4($sp)");
        ins("sw    $fp, 0($sp)");
        ins("move  $fp, $sp");
        if (frameSize) ins("addiu $sp, $sp, -" + std::to_string(frameSize));
        for (size_t i = 0; i < f.quads.size(); ++i) {
            if (isTarget[i]) lab(target(static_cast<int>(i)));
            text << "        # " << quadText(prog, f, f.quads[i], {}) << "\n";
            quad(f.quads[i]);
        }
        if (isTarget[f.quads.size()]) lab(target(static_cast<int>(f.quads.size())));
        lab(label + "_exit");
        ins("move  $sp, $fp");
        ins("lw    $ra, 4($sp)");
        ins("lw    $fp, 0($sp)");
        ins("addiu $sp, $sp, 8");
        ins("jr    $ra");
    }

    /* ---------------- static data ---------------- */

    static std::string clean(const std::string &name) {
        std::string s;
        for (char c : name) s += isalnum(static_cast<unsigned char>(c)) ? c : '_';
        return s;
    }

    void globals(std::ostringstream &startup) {
        std::set<std::string> taken;
        for (const auto &g : prog.globals) {
            std::string name = "g_" + clean(g.sym->uniqueName);
            while (!taken.insert(name).second) name += "_";
            globalLabel[g.sym.get()] = name;
        }
        for (const auto &g : prog.globals) {
            int size = sizeOfType(g.sym->type);
            std::vector<uint8_t> bytes(static_cast<size_t>(size), 0);
            bool any = false;
            for (const auto &init : g.init) {
                size_t at = static_cast<size_t>(init.offset);
                if (init.kind == GlobalInit::Address || init.kind == GlobalInit::String) {
                    /* an address is only known to the assembler: stored when the program starts */
                    startup << "        la    $t0, " << (init.kind == GlobalInit::String ? "str" + std::to_string(init.str) : globalLabel[init.target])
                            << "\n        sw    $t0, " << globalLabel[g.sym.get()] << "+" << init.offset << "\n";
                    continue;
                }
                any = true;
                if (init.cls == Cls::Double) { double d = init.f; memcpy(&bytes[at], &d, 8); }
                else if (init.cls == Cls::Float) { float fl = static_cast<float>(init.f); memcpy(&bytes[at], &fl, 4); }
                else {
                    int width = isWide(init.cls) ? 8 : init.cls == Cls::Short || init.cls == Cls::UShort ? 2
                                : init.cls == Cls::Bool || init.cls == Cls::Char || init.cls == Cls::UChar ? 1 : 4;
                    long long v = init.i;
                    if (at + static_cast<size_t>(width) <= bytes.size()) memcpy(&bytes[at], &v, static_cast<size_t>(width));
                }
            }
            data << "        .align 3\n" << globalLabel[g.sym.get()] << ":";
            if (!any) {
                data << "  .space " << size << "\n";
                continue;
            }
            for (size_t i = 0; i < bytes.size(); ++i)
                data << (i % 16 == 0 ? "\n        .byte " : ", ") << static_cast<int>(bytes[i]);
            data << "\n";
        }
        for (size_t i = 0; i < prog.strings.size(); ++i) {
            std::string bytes = decodeLiteral(prog.strings[i]);
            data << "str" << i << ":";
            for (size_t k = 0; k <= bytes.size(); ++k)
                data << (k % 16 == 0 ? "\n        .byte " : ", ") << (k < bytes.size() ? static_cast<int>(static_cast<unsigned char>(bytes[k])) : 0);
            data << "\n";
        }
    }

    std::string run(const std::string &runtime) {
        for (const auto &f : prog.functions)
            functionLabel[f.sym.get()] = f.linkName == "main" ? "main_" : f.linkName; /* `main` itself is the start-up code below */
        std::ostringstream startup;
        globals(startup);
        for (size_t i = 0; i < prog.functions.size(); ++i) function(prog.functions[i], static_cast<int>(i));

        std::ostringstream out;
        out << "# generated for SPIM: `spim -file <this file> [arguments]`\n\n        .data\n" << data.str()
            << "\n        .text\n        .globl main\n"
            << "main:\n"
            << "        li    $t0, -8\n        and   $sp, $sp, $t0           # frames assume an 8-byte aligned stack\n"
            << "        addiu $sp, $sp, -8\n        sw    $a0, 0($sp)             # argc\n        sw    $a1, 4($sp)             # argv\n"
            << startup.str()
            << "        jal   main_\n        move  $a0, $v0\n        li    $v0, 17                 # exit with main's result\n        syscall\n"
            << text.str() << "\n" << runtime;
        return out.str();
    }
};

} // namespace

std::string generate(const Program &program, const std::string &runtime) {
    Emitter e(program);
    return e.run(runtime);
}

} // namespace mips
