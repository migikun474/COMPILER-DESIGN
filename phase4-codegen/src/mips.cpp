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

/* SPIM's stack segment ends at 0x80000000 and grows downwards by
   doubling; by default it stops at 256 KB (the next doubling would pass
   the 512 KB limit of `spim -lstack`), and its top already holds argv and
   the environment. A frame may reach down to 16 KB above that end, which
   leaves room for the run-time library and the error message, so deep
   recursion stops with "stack overflow" instead of SPIM's own failure
   (measured: 8045 nested 32-byte frames fit, 8046 do not) */
const char *const STACK_FLOOR = "0x7ffc4000";
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
    int frameSize = 0, argumentBytes = 0, fnIndex = 0, localLabels = 0;
    std::vector<const Quad *> params;           /* `param`s waiting for their call */

    explicit Emitter(const Program &p) : prog(p) {}

    /* -O1: constants inside instructions, leaf functions skip saving $ra */
    bool optimize = false;
    std::vector<std::string> code; /* the function being generated, one line per entry */
    bool calls = false;            /* it contains a `jal`: $ra must be saved */

    void ins(const std::string &s) {
        if (s.compare(0, 3, "jal") == 0) calls = true;
        code.push_back("        " + s);
    }
    void lab(const std::string &s) { code.push_back(s + ":"); }

    std::string use(const Operand &o, const std::string &scratch) {
        if (optimize && o.kind == Operand::IntConst && static_cast<int32_t>(o.ival) == 0) return "$zero";
        loadInt(scratch, o);
        return scratch;
    }
    std::string floatUse(const Operand &o, const std::string &scratch, Cls c) {
        loadFloat(scratch, o, c);
        return scratch;
    }
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

    /* the registers that hold a long long (low, high) after a load */
    std::pair<std::string, std::string> wideUse(const Operand &o, const std::string &lo, const std::string &hi) {
        loadWide(lo, hi, o);
        return {lo, hi};
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
            auto v = wideUse(o, "$t0", "$t1");
            std::string base = at.substr(at.find('('));
            int off = std::stoi(at.substr(0, at.find('(')));
            ins("sw    " + v.first + ", " + std::to_string(off) + base);
            ins("sw    " + v.second + ", " + std::to_string(off + 4) + base);
        } else {
            std::string r = use(o, "$t0");
            ins(std::string(c == Cls::Bool || c == Cls::Char || c == Cls::UChar ? "sb    " : c == Cls::Short || c == Cls::UShort ? "sh    " : "sw    ") + r + ", " + at);
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
            std::string d = "$t0";
            ins(std::string(op) + d + ", " + at);
            storeInt(d, dst);
        }
    }

    /* ---------------- arithmetic ---------------- */

    void binary(const Quad &q) {
        Cls c = q.cls;
        if (isFloatCls(c)) {
            std::string suffix = c == Cls::Double ? ".d" : ".s";
            std::string a = floatUse(q.a, "$f0", c), b = floatUse(q.b, "$f2", c), d = "$f0";
            const char *op = q.op == Op::Add ? "add" : q.op == Op::Sub ? "sub" : q.op == Op::Mul ? "mul" : "div";
            ins(std::string(op) + suffix + " " + d + ", " + a + ", " + b);
            storeFloat(d, q.r);
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
            /* the operands are read where they are; the result is built in
               $t4:$t6 because it may be one of the operands (x = x + y) */
            auto a = wideUse(q.a, "$t0", "$t1"), b = wideUse(q.b, "$t2", "$t3");
            const std::string &aLo = a.first, &aHi = a.second, &bLo = b.first, &bHi = b.second;
            switch (q.op) {
                case Op::Add:
                    ins("addu  $t4, " + aLo + ", " + bLo);
                    ins("sltu  $t5, $t4, " + aLo); /* carry out of the low word */
                    ins("addu  $t6, " + aHi + ", " + bHi);
                    ins("addu  $t6, $t6, $t5");
                    break;
                case Op::Sub:
                    ins("sltu  $t5, " + aLo + ", " + bLo); /* borrow */
                    ins("subu  $t4, " + aLo + ", " + bLo);
                    ins("subu  $t6, " + aHi + ", " + bHi);
                    ins("subu  $t6, $t6, $t5");
                    break;
                case Op::Mul:
                    ins("multu " + aLo + ", " + bLo);
                    ins("mflo  $t4");
                    ins("mfhi  $t5");
                    ins("mul   $t6, " + aLo + ", " + bHi);
                    ins("addu  $t5, $t5, $t6");
                    ins("mul   $t6, " + aHi + ", " + bLo);
                    ins("addu  $t6, $t5, $t6");
                    break;
                default: {
                    const char *op = q.op == Op::BitAnd ? "and   " : q.op == Op::BitOr ? "or    " : "xor   ";
                    ins(std::string(op) + "$t4, " + aLo + ", " + bLo);
                    ins(std::string(op) + "$t6, " + aHi + ", " + bHi);
                    break;
                }
            }
            storeWide("$t4", "$t6", q.r);
            return;
        }
        bool isSigned = c == Cls::Int;
        std::string d = "$t0";
        if (optimize && q.b.kind == Operand::IntConst) { /* a small constant goes into the instruction itself */
            long long v = static_cast<int32_t>(q.b.ival);
            std::string op;
            if (q.op == Op::Add && v >= -32768 && v <= 32767) op = "addiu ";
            else if (q.op == Op::Sub && v >= -32767 && v <= 32768) { op = "addiu "; v = -v; }
            else if (q.op == Op::BitAnd && v >= 0 && v <= 65535) op = "andi  ";
            else if (q.op == Op::BitOr && v >= 0 && v <= 65535) op = "ori   ";
            else if (q.op == Op::BitXor && v >= 0 && v <= 65535) op = "xori  ";
            else if (q.op == Op::Shl && v >= 0 && v <= 31) op = "sll   ";
            else if (q.op == Op::Shr && v >= 0 && v <= 31) op = isSigned ? "sra   " : "srl   ";
            if (!op.empty()) {
                std::string a = use(q.a, "$t0");
                ins(op + d + ", " + a + ", " + std::to_string(v));
                storeInt(d, q.r);
                return;
            }
        }
        std::string a = use(q.a, "$t0"), b = use(q.b, "$t1"), abc = d + ", " + a + ", " + b;
        switch (q.op) {
            case Op::Add: ins("addu  " + abc); break;
            case Op::Sub: ins("subu  " + abc); break;
            case Op::Mul: ins("mul   " + abc); break;
            case Op::Div: case Op::Mod:
                if (!(q.b.kind == Operand::IntConst && static_cast<int32_t>(q.b.ival) != 0)) {
                    /* the hardware does not trap: a zero divisor is reported like the interpreter does */
                    std::string ok = fresh();
                    ins("bnez  " + b + ", " + ok);
                    ins("jal   __div_by_zero");
                    lab(ok);
                }
                ins(std::string(isSigned ? "div   " : "divu  ") + a + ", " + b);
                ins(std::string(q.op == Op::Div ? "mflo  " : "mfhi  ") + d);
                break;
            case Op::BitAnd: ins("and   " + abc); break;
            case Op::BitOr: ins("or    " + abc); break;
            case Op::BitXor: ins("xor   " + abc); break;
            case Op::Shl: ins("sllv  " + abc); break;
            case Op::Shr: ins(std::string(isSigned ? "srav  " : "srlv  ") + abc); break;
            default: break;
        }
        storeInt(d, q.r);
    }

    void unary(const Quad &q) {
        Cls c = q.cls;
        if (isFloatCls(c)) {
            std::string a = floatUse(q.a, "$f0", c), d = "$f0";
            ins(std::string(c == Cls::Double ? "neg.d " : "neg.s ") + d + ", " + a);
            storeFloat(d, q.r);
        } else if (isWide(c)) {
            auto a = wideUse(q.a, "$t0", "$t1");
            if (q.op == Op::Neg) {
                ins("sltu  $t5, $zero, " + a.first);
                ins("negu  $t4, " + a.first);
                ins("negu  $t6, " + a.second);
                ins("subu  $t6, $t6, $t5");
            } else {
                ins("nor   $t4, " + a.first + ", $zero");
                ins("nor   $t6, " + a.second + ", $zero");
            }
            storeWide("$t4", "$t6", q.r);
        } else {
            std::string a = use(q.a, "$t0"), d = "$t0";
            ins(q.op == Op::Neg ? "negu  " + d + ", " + a : "nor   " + d + ", " + a + ", $zero");
            storeInt(d, q.r);
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
            if (to == Cls::Double) { storeFloat("$f0", q.r); return; }
            if (to == Cls::Float) { ins("cvt.s.d $f0, $f0"); storeFloat("$f0", q.r); return; }
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
            std::string x = floatUse(q.a, "$f0", c), y = floatUse(q.b, "$f2", c);
            bool swap = op == ">" || op == ">=";
            std::string test = op == "==" || op == "!=" ? "c.eq" : op == "<" || op == ">" ? "c.lt" : "c.le";
            ins(test + suffix + " " + (swap ? y + ", " + x : x + ", " + y));
            ins(std::string(op == "!=" ? "bc1f  " : "bc1t  ") + target);
            return;
        }
        if (isWide(c)) {
            auto wa = wideUse(q.a, "$t0", "$t1"), wb = wideUse(q.b, "$t2", "$t3");
            if (op == "==" || op == "!=") {
                ins("xor   $t4, " + wa.first + ", " + wb.first);
                ins("xor   $t5, " + wa.second + ", " + wb.second);
                ins("or    $t4, $t4, $t5");
                ins(std::string(op == "==" ? "beqz  " : "bnez  ") + "$t4, " + target);
                return;
            }
            /* high words decide unless they are equal; then the low words, unsigned */
            bool swap = op == ">" || op == ">=";
            if (swap) std::swap(wa, wb);
            const std::string &aLo = wa.first, &aHi = wa.second, &bLo = wb.first, &bHi = wb.second;
            std::string skip = fresh();
            ins(std::string(c == Cls::ULLong ? "bltu  " : "blt   ") + aHi + ", " + bHi + ", " + target);
            ins("bne   " + aHi + ", " + bHi + ", " + skip);
            ins(std::string(op == "<" || op == ">" ? "bltu  " : "bleu  ") + aLo + ", " + bLo + ", " + target);
            lab(skip);
            return;
        }
        std::string x = use(q.a, "$t0"), y = use(q.b, "$t1");
        bool u = isUnsignedCls(c);
        std::string b = op == "==" ? "beq   " : op == "!=" ? "bne   " : op == "<" ? (u ? "bltu  " : "blt   ") : op == ">" ? (u ? "bgtu  " : "bgt   ")
                        : op == "<=" ? (u ? "bleu  " : "ble   ") : (u ? "bgeu  " : "bge   ");
        ins(b + x + ", " + y + ", " + target);
    }

    /* the place a[offset], as displacement(register) */
    std::string element(const Quad &q) {
        if (optimize && q.b.kind == Operand::IntConst) {
            int off = static_cast<int32_t>(q.b.ival);
            if (isLocal(q.a)) return std::to_string((q.a.kind == Operand::Temp ? tempOff[q.a.temp] : varOff[q.a.sym]) + off) + "($fp)";
            address("$t8", q.a);
            return std::to_string(off) + "($t8)";
        }
        address("$t8", q.a);
        std::string i = use(q.b, "$t9");
        ins("addu  $t8, $t8, " + i);
        return "0($t8)";
    }

    /* ---------------- calls ---------------- */

    static constexpr int ARGUMENT_REGISTER_BYTES = 16;

    static bool isNarrow(Cls c) { return c == Cls::Bool || c == Cls::Char || c == Cls::UChar || c == Cls::Short || c == Cls::UShort; }
    static bool isWordInteger(Cls c) { return isNarrow(c) || c == Cls::Int || c == Cls::UInt || c == Cls::Ptr; }
    static std::string argumentRegister(int word) { return "$a" + std::to_string(word); }

    void loadArgumentRegisters(const std::vector<const Quad *> &args, const std::vector<int> &offsets,
                               const std::vector<int> &sizes, const std::vector<bool> &inRegister) {
        for (int word = 0; word < ARGUMENT_REGISTER_BYTES / 4; ++word)
            for (size_t i = 0; i < args.size(); ++i)
                if (!inRegister[i] && offsets[i] <= 4 * word && 4 * word < offsets[i] + sizes[i])
                    ins("lw    " + argumentRegister(word) + ", " + std::to_string(4 * word) + "($sp)");
        for (size_t i = 0; i < args.size(); ++i) {
            if (!inRegister[i]) continue;
            std::string target = argumentRegister(offsets[i] / 4), value = use(args[i]->a, target);
            if (value != target) ins("move  " + target + ", " + value);
        }
    }

    void saveArgumentRegisters() {
        int words = std::min(ARGUMENT_REGISTER_BYTES / 4, (argumentBytes + 3) / 4);
        for (int word = 0; word < words; ++word)
            ins("sw    " + argumentRegister(word) + ", " + std::to_string(8 + 4 * word) + "($fp)");
    }

    void call(const Quad &q) {
        size_t n = std::min(static_cast<size_t>(q.nargs), params.size());
        std::vector<const Quad *> args(params.end() - static_cast<long>(n), params.end());
        params.resize(params.size() - n);
        std::vector<int> offsets, sizes;
        int size = 0;
        for (const Quad *p : args) {
            auto s = slot(p->a.type);
            size = roundUp(size, s.second);
            offsets.push_back(size);
            sizes.push_back(s.first);
            size += s.first;
        }
        bool userFunction = q.callee != nullptr;
        size = roundUp(size, 8);
        if (userFunction) size = std::max(size, ARGUMENT_REGISTER_BYTES);
        if (size) ins("addiu $sp, $sp, -" + std::to_string(size));
        std::vector<bool> inRegister(args.size(), false);
        for (size_t i = 0; i < args.size(); ++i) {
            Cls c = classOf(args[i]->a.type);
            inRegister[i] = userFunction && offsets[i] < ARGUMENT_REGISTER_BYTES && isWordInteger(c);
            if (!inRegister[i]) storeValueAt(args[i]->a, isNarrow(c) ? Cls::Int : c, std::to_string(offsets[i]) + "($sp)");
        }
        if (userFunction) loadArgumentRegisters(args, offsets, sizes, inRegister);
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
                    std::string d = "$f0";
                    loadFloat(d, q.a, rc);
                    storeFloat(d, q.r);
                } else if (isWide(rc)) {
                    auto a = wideUse(q.a, "$t0", "$t1");
                    storeWide(a.first, a.second, q.r);
                } else {
                    std::string d = "$t0";
                    loadInt(d, q.a);
                    storeInt(d, q.r);
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
                loadValueFrom(element(q), q.r);
                break;
            case Op::IndexStore:
                storeValueAt(q.r, q.cls, element(q));
                break;
            case Op::AddrOf: {
                std::string d = "$t0";
                address(d, q.a);
                storeInt(d, q.r);
                break;
            }
            case Op::Load:
                loadValueFrom("0(" + use(q.a, "$t8") + ")", q.r);
                break;
            case Op::Store:
                storeValueAt(q.r, q.cls, "0(" + use(q.a, "$t8") + ")");
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
        argumentBytes = at;

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

        std::vector<int> targeted(f.quads.size() + 1, 0);
        for (const auto &q : f.quads)
            if ((q.op == Op::Goto || q.op == Op::IfRel) && q.target >= 0) ++targeted[q.target];

        code.clear();
        calls = false;
        for (size_t i = 0; i < f.quads.size(); ++i) {
            if (targeted[i]) lab(target(static_cast<int>(i)));
            const Quad &q = f.quads[i];
            code.push_back("        # " + quadText(prog, f, q, {}));
            quad(q);
        }
        if (targeted[f.quads.size()]) lab(target(static_cast<int>(f.quads.size())));
        std::vector<std::string> body;
        body.swap(code);

        text << "\n# " << f.signature << "\n";
        lab(label);
        ins("addiu $sp, $sp, -8");
        if (calls || !optimize) ins("sw    $ra, 4($sp)"); /* a leaf function never changes $ra */
        ins("sw    $fp, 0($sp)");
        ins("move  $fp, $sp");
        if (frameSize) ins("addiu $sp, $sp, -" + std::to_string(frameSize));
        if (calls || frameSize > 4096) { /* only a function that calls can recurse; a big frame can overflow alone */
            std::string ok = fresh();
            ins("lw    $t8, __stack_limit");
            ins("sltu  $t8, $sp, $t8");
            ins("beqz  $t8, " + ok);
            ins("j     __stack_overflow");
            lab(ok);
        }
        saveArgumentRegisters();
        for (const auto &line : code) text << line << "\n";
        for (const auto &line : body) text << line << "\n";
        code.clear();
        lab(label + "_exit");
        ins("move  $sp, $fp");
        if (calls || !optimize) ins("lw    $ra, 4($sp)");
        ins("lw    $fp, 0($sp)");
        ins("addiu $sp, $sp, 8");
        ins("jr    $ra");
        for (const auto &line : code) text << line << "\n";
        code.clear();
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
                    std::string to = init.kind == GlobalInit::String ? "str" + std::to_string(init.str)
                                     : globalLabel.count(init.target) ? globalLabel[init.target] : functionLabel[init.target];
                    startup << "        la    $t0, " << to
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
            << "        li    $t1, " << STACK_FLOOR << "\n"
            << "        sw    $t1, __stack_limit      # deeper than this is a stack overflow\n"
            << "        addiu $sp, $sp, -8\n        sw    $a0, 0($sp)             # argc\n        sw    $a1, 4($sp)             # argv\n"
            << startup.str()
            << "        jal   main_\n        move  $a0, $v0\n        li    $v0, 17                 # exit with main's result\n        syscall\n"
            << text.str() << "\n" << runtime;
        return out.str();
    }
};

} // namespace

std::string generate(const Program &program, const std::string &runtime, bool optimize) {
    Emitter e(program);
    e.optimize = optimize;
    return e.run(runtime);
}

} // namespace mips
