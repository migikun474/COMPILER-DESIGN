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

    /* -O1 and above: registers for the most used names, constants inside
       instructions, a peephole pass (Dragon Book 8.7, 8.8) */
    bool optimize = false;
    std::vector<std::string> code; /* the function being generated, one line per entry */
    bool calls = false;            /* it contains a `jal`: $ra must be saved */
    using Key = std::pair<const sem::Symbol *, int>;
    std::map<Key, std::string> home; /* names that live in $s0-$s7 / $f20-$f30 instead of the frame */
    std::map<Key, Cls> homeClass;    /* the declared class of each of them */

    /* a char, short or bool in a register is kept exactly as a load would give it */
    void normalize(const std::string &reg, Cls c) {
        switch (c) {
            case Cls::Bool: case Cls::UChar: ins("andi  " + reg + ", " + reg + ", 255"); break;
            case Cls::UShort: ins("andi  " + reg + ", " + reg + ", 65535"); break;
            case Cls::Char: ins("sll   " + reg + ", " + reg + ", 24"); ins("sra   " + reg + ", " + reg + ", 24"); break;
            case Cls::Short: ins("sll   " + reg + ", " + reg + ", 16"); ins("sra   " + reg + ", " + reg + ", 16"); break;
            default: break;
        }
    }
    /* a name declared `char` read through an `unsigned char` operand (or the reverse) needs the other extension */
    bool otherReading(const Operand &o) const {
        auto c = homeClass.find(keyOf(o));
        Cls want = classOf(o.type);
        bool narrow = want == Cls::Bool || want == Cls::Char || want == Cls::UChar || want == Cls::Short || want == Cls::UShort;
        return c != homeClass.end() && narrow && c->second != want;
    }

    void ins(const std::string &s) {
        if (s.compare(0, 3, "jal") == 0) calls = true;
        code.push_back("        " + s);
    }
    void lab(const std::string &s) { code.push_back(s + ":"); }

    static Key keyOf(const Operand &o) { return {o.kind == Operand::Var ? o.sym : nullptr, o.kind == Operand::Temp ? o.temp : 0}; }
    const std::string *homeOf(const Operand &o) const {
        if (o.kind != Operand::Var && o.kind != Operand::Temp) return nullptr;
        auto it = home.find(keyOf(o));
        return it == home.end() ? nullptr : &it->second;
    }
    /* the register that holds o's value: its own, $zero, or `scratch` after a load */
    std::string use(const Operand &o, const std::string &scratch) {
        if (const std::string *h = homeOf(o)) {
            if (!otherReading(o)) return *h;
            loadInt(scratch, o);
            return scratch;
        }
        if (optimize && o.kind == Operand::IntConst && static_cast<int32_t>(o.ival) == 0) return "$zero";
        loadInt(scratch, o);
        return scratch;
    }
    /* where to compute r: its own register, or `scratch` to be stored by finish() */
    std::string dest(const Operand &r, const std::string &scratch) const {
        const std::string *h = homeOf(r);
        return h ? *h : scratch;
    }
    /* `have`: the class the value in `reg` is already normalized for, if known */
    void finish(const std::string &reg, const Operand &r, Cls have = Cls::Void) {
        if (!homeOf(r)) storeInt(reg, r);
        else if (homeClass[keyOf(r)] != have) normalize(reg, homeClass[keyOf(r)]);
    }
    std::string floatUse(const Operand &o, const std::string &scratch, Cls c) {
        if (const std::string *h = homeOf(o)) return *h;
        loadFloat(scratch, o, c);
        return scratch;
    }
    void floatFinish(const std::string &reg, const Operand &r) {
        if (!homeOf(r)) storeFloat(reg, r);
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
        if (const std::string *h = homeOf(o)) {
            if (*h != reg) ins("move  " + reg + ", " + *h);
            if (otherReading(o)) normalize(reg, classOf(o.type));
            return;
        }
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
        if (const std::string *h = homeOf(dst)) {
            if (*h != reg) ins("move  " + *h + ", " + reg);
            normalize(*h, homeClass[keyOf(dst)]);
            return;
        }
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
        if (const std::string *h = homeOf(o)) {
            if (*h != reg) ins(std::string(c == Cls::Double ? "mov.d " : "mov.s ") + reg + ", " + *h);
            return;
        }
        std::string op = c == Cls::Double ? "l.d   " : "l.s   ";
        if (o.kind == Operand::FloatConst) ins(op + reg + ", " + constantLabel(o.fval, c == Cls::Double));
        else if (o.kind == Operand::IntConst) ins(op + reg + ", " + constantLabel(static_cast<double>(o.ival), c == Cls::Double));
        else ins(op + reg + ", " + mem(o));
    }

    void storeFloat(const std::string &reg, const Operand &dst) {
        if (const std::string *h = homeOf(dst)) {
            if (*h != reg) ins(std::string(classOf(dst.type) == Cls::Double ? "mov.d " : "mov.s ") + *h + ", " + reg);
            return;
        }
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
            std::string d = dest(dst, "$t0");
            ins(std::string(op) + d + ", " + at);
            finish(d, dst, c);
        }
    }

    /* ---------------- arithmetic ---------------- */

    void binary(const Quad &q) {
        Cls c = q.cls;
        if (isFloatCls(c)) {
            std::string suffix = c == Cls::Double ? ".d" : ".s";
            std::string a = floatUse(q.a, "$f0", c), b = floatUse(q.b, "$f2", c), d = dest(q.r, "$f0");
            const char *op = q.op == Op::Add ? "add" : q.op == Op::Sub ? "sub" : q.op == Op::Mul ? "mul" : "div";
            ins(std::string(op) + suffix + " " + d + ", " + a + ", " + b);
            floatFinish(d, q.r);
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
        bool isSigned = c == Cls::Int;
        std::string d = dest(q.r, "$t0");
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
                finish(d, q.r);
                return;
            }
        }
        std::string a = use(q.a, "$t0"), b = use(q.b, "$t1"), abc = d + ", " + a + ", " + b;
        switch (q.op) {
            case Op::Add: ins("addu  " + abc); break;
            case Op::Sub: ins("subu  " + abc); break;
            case Op::Mul: ins("mul   " + abc); break;
            case Op::Div: case Op::Mod:
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
        finish(d, q.r);
    }

    void unary(const Quad &q) {
        Cls c = q.cls;
        if (isFloatCls(c)) {
            std::string a = floatUse(q.a, "$f0", c), d = dest(q.r, "$f0");
            ins(std::string(c == Cls::Double ? "neg.d " : "neg.s ") + d + ", " + a);
            floatFinish(d, q.r);
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
            std::string a = use(q.a, "$t0"), d = dest(q.r, "$t0");
            ins(q.op == Op::Neg ? "negu  " + d + ", " + a : "nor   " + d + ", " + a + ", $zero");
            finish(d, q.r);
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
        std::string x = use(q.a, "$t0"), y = use(q.b, "$t1");
        bool u = isUnsignedCls(c);
        std::string b = op == "==" ? "beq   " : op == "!=" ? "bne   " : op == "<" ? (u ? "bltu  " : "blt   ") : op == ">" ? (u ? "bgtu  " : "bgt   ")
                        : op == "<=" ? (u ? "bleu  " : "ble   ") : (u ? "bgeu  " : "bge   ");
        ins(b + x + ", " + y + ", " + target);
    }

    /* r = (a relop b) as 0 or 1, without a branch: the four-instruction
       pattern `if a relop b goto +3 ; r = 0 ; goto +2 ; r = 1` in one or two instructions */
    void setCondition(const Quad &q, const Operand &r) {
        std::string a = use(q.a, "$t0"), b = use(q.b, "$t1"), d = dest(r, "$t0");
        std::string slt = isUnsignedCls(q.cls) ? "sltu  " : "slt   ";
        const std::string &op = q.relop;
        if (op == "<") ins(slt + d + ", " + a + ", " + b);
        else if (op == ">") ins(slt + d + ", " + b + ", " + a);
        else if (op == "<=") { ins(slt + d + ", " + b + ", " + a); ins("xori  " + d + ", " + d + ", 1"); }
        else if (op == ">=") { ins(slt + d + ", " + a + ", " + b); ins("xori  " + d + ", " + d + ", 1"); }
        else if (op == "==") { ins("xor   " + d + ", " + a + ", " + b); ins("sltiu " + d + ", " + d + ", 1"); }
        else { ins("xor   " + d + ", " + a + ", " + b); ins("sltu  " + d + ", $zero, " + d); }
        finish(d, r);
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
                    std::string d = dest(q.r, "$f0");
                    loadFloat(d, q.a, rc);
                    floatFinish(d, q.r);
                } else if (isWide(rc)) {
                    loadWide("$t0", "$t1", q.a);
                    storeWide("$t0", "$t1", q.r);
                } else {
                    std::string d = dest(q.r, "$t0");
                    loadInt(d, q.a);
                    finish(d, q.r, classOf(q.a.type));
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
                std::string d = dest(q.r, "$t0");
                address(d, q.a);
                finish(d, q.r);
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

        /* registers for the most used names; a slot to save each register this function uses */
        home.clear();
        homeClass.clear();
        if (optimize) assignRegisters(f, incoming);
        std::map<std::string, int> saved;
        for (const auto &h : home)
            if (!saved.count(h.second)) saved[h.second] = place(h.second[1] == 'f' ? sem::doubleType() : sem::intType());
        auto saveOp = [](const std::string &reg, bool store) { return std::string(reg[1] == 'f' ? (store ? "s.d   " : "l.d   ") : (store ? "sw    " : "lw    ")); };
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
            if (optimize && i + 3 < f.quads.size() && isBooleanValue(f, i, targeted)) {
                setCondition(q, f.quads[i + 1].r);
                i += 3; /* r = 0 ; goto ; r = 1 are done */
                continue;
            }
            quad(q);
        }
        if (targeted[f.quads.size()]) lab(target(static_cast<int>(f.quads.size())));
        std::vector<std::string> body;
        body.swap(code);
        if (optimize) peephole(body);

        text << "\n# " << f.signature << "\n";
        lab(label);
        ins("addiu $sp, $sp, -8");
        if (calls || !optimize) ins("sw    $ra, 4($sp)"); /* a leaf function never changes $ra */
        ins("sw    $fp, 0($sp)");
        ins("move  $fp, $sp");
        if (frameSize) ins("addiu $sp, $sp, -" + std::to_string(frameSize));
        for (const auto &r : saved) ins(saveOp(r.first, true) + r.first + ", " + std::to_string(r.second) + "($fp)");
        for (const sem::Symbol *p : incoming) { /* a parameter that lives in a register is fetched once */
            auto h = home.find(Key(p, 0));
            if (h == home.end()) continue;
            Cls c = homeClass[Key(p, 0)];
            ins(std::string(c == Cls::Double ? "l.d   " : c == Cls::Float ? "l.s   " : "lw    ") + h->second + ", " + std::to_string(varOff[p]) + "($fp)");
        }
        for (const auto &line : code) text << line << "\n";
        for (const auto &line : body) text << line << "\n";
        code.clear();
        lab(label + "_exit");
        for (const auto &r : saved) ins(saveOp(r.first, false) + r.first + ", " + std::to_string(r.second) + "($fp)");
        ins("move  $sp, $fp");
        if (calls || !optimize) ins("lw    $ra, 4($sp)");
        ins("lw    $fp, 0($sp)");
        ins("addiu $sp, $sp, 8");
        ins("jr    $ra");
        for (const auto &line : code) text << line << "\n";
        code.clear();
    }

    /* Dragon Book 8.8 with live intervals: every name gets a use count (a
       use inside a loop counts ten times per level of nesting) and the
       interval of instructions in which it occurs, widened to cover every
       loop it reaches into. In order of count each name takes the first
       register that no name with an overlapping interval already holds:
       $s0-$s7 for integers and pointers, $f20-$f30 for float and double.
       Only scalars whose address is never needed qualify.
       ponytail: long long always stays in the frame (it would need a
       register pair and is rarely in a hot loop). */
    void assignRegisters(const Function &f, const std::vector<const sem::Symbol *> &incoming) {
        int n = static_cast<int>(f.quads.size());
        std::vector<int> depth(n, 0);
        std::vector<std::pair<int, int>> loops;
        for (int j = 0; j < n; ++j) {
            const Quad &q = f.quads[j];
            if ((q.op == Op::Goto || q.op == Op::IfRel) && q.target >= 0 && q.target <= j) { /* a backward jump closes a loop */
                loops.push_back({q.target, j});
                for (int i = q.target; i <= j; ++i) depth[i] = std::min(depth[i] + 1, 3);
            }
        }
        struct Info {
            long long weight = 0;
            int first = 1 << 30, last = -1;
            Cls cls = Cls::Int;
        };
        std::set<Key> never;
        std::map<Key, Info> info;
        auto isNamed = [](const Operand &o) { return o.kind == Operand::Var || o.kind == Operand::Temp; };
        auto note = [&](const Operand &o, long long w, int at) {
            if (!isNamed(o)) return;
            if (o.kind == Operand::Var && !varOff.count(o.sym)) return; /* a global */
            TypePtr t = o.kind == Operand::Temp ? f.temps[o.temp - 1] : o.sym->type;
            Cls c = classOf(t);
            bool scalar = t && !sem::isArray(t) && !t->isVolatile && t->kind != sem::TypeKind::Opaque && c != Cls::Block &&
                          c != Cls::Void && !isWide(c);
            if (!scalar) { never.insert(keyOf(o)); return; }
            Info &x = info[keyOf(o)];
            x.weight += w;
            x.first = std::min(x.first, at);
            x.last = std::max(x.last, at);
            x.cls = c;
        };
        std::vector<int> pending; /* `param`s whose value is read when their call is reached */
        for (int i = 0; i < n; ++i) {
            const Quad &q = f.quads[i];
            long long w = depth[i] == 0 ? 1 : depth[i] == 1 ? 10 : depth[i] == 2 ? 100 : 1000;
            bool memory = q.op == Op::AddrOf || q.op == Op::IndexLoad || q.op == Op::IndexStore || q.op == Op::VaStart ||
                          q.op == Op::VaArg || q.op == Op::VaEnd;
            if (memory && isNamed(q.a)) never.insert(keyOf(q.a)); /* needs an address */
            else note(q.a, w, i);
            if (q.op == Op::VaStart && isNamed(q.b)) never.insert(keyOf(q.b));
            else note(q.b, w, i);
            note(q.r, w, i);
            if (q.op == Op::Param) pending.push_back(i);
            if (q.op == Op::Call) {
                size_t k = std::min(static_cast<size_t>(q.nargs), pending.size());
                for (size_t p = pending.size() - k; p < pending.size(); ++p) note(f.quads[pending[p]].a, 0, i);
                pending.resize(pending.size() - k);
            }
        }
        for (const sem::Symbol *p : incoming) { /* a parameter holds its value from the first instruction */
            auto it = info.find(Key(p, 0));
            if (it != info.end()) it->second.first = 0;
        }
        std::vector<std::pair<long long, Key>> ranked;
        for (auto &e : info) {
            if (never.count(e.first)) continue;
            Info &x = e.second;
            for (bool grown = true; grown;) { /* the value may be needed again on the next trip round a loop */
                grown = false;
                for (const auto &l : loops) {
                    if (x.first > l.second || x.last < l.first || (x.first <= l.first && x.last >= l.second)) continue;
                    x.first = std::min(x.first, l.first);
                    x.last = std::max(x.last, l.second);
                    grown = true;
                }
            }
            ranked.push_back({x.weight, e.first});
        }
        std::stable_sort(ranked.begin(), ranked.end(), [](const std::pair<long long, Key> &x, const std::pair<long long, Key> &y) { return x.first > y.first; });
        static const std::vector<std::string> intRegs = {"$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7"};
        static const std::vector<std::string> floatRegs = {"$f20", "$f22", "$f24", "$f26", "$f28", "$f30"};
        std::map<std::string, std::vector<std::pair<int, int>>> busy;
        for (const auto &r : ranked) {
            const Info &x = info[r.second];
            for (const std::string &reg : isFloatCls(x.cls) ? floatRegs : intRegs) {
                bool free = true;
                for (const auto &b : busy[reg]) free = free && (x.first > b.second || x.last < b.first);
                if (!free) continue;
                home[r.second] = reg;
                homeClass[r.second] = x.cls;
                busy[reg].push_back({x.first, x.last});
                break;
            }
        }
    }

    /* quads i..i+3 are `if a relop b goto i+3 ; r = 0 ; goto i+4 ; r = 1`, entered only at i */
    static bool isBooleanValue(const Function &f, size_t i, const std::vector<int> &targeted) {
        const Quad &test = f.quads[i], &zero = f.quads[i + 1], &skip = f.quads[i + 2], &one = f.quads[i + 3];
        auto isConst = [](const Operand &o, long long v) { return o.kind == Operand::IntConst && o.ival == v; };
        auto same = [](const Operand &x, const Operand &y) { return x.kind == y.kind && x.sym == y.sym && x.temp == y.temp; };
        Cls rc = classOf(zero.r.type);
        return test.op == Op::IfRel && !isFloatCls(test.cls) && !isWide(test.cls) && test.target == static_cast<int>(i) + 3 &&
               zero.op == Op::Assign && isConst(zero.a, 0) && !isFloatCls(rc) && !isWide(rc) && rc != Cls::Block &&
               skip.op == Op::Goto && skip.target == static_cast<int>(i) + 4 &&
               one.op == Op::Assign && isConst(one.a, 1) && same(one.r, zero.r) &&
               targeted[i + 1] == 0 && targeted[i + 2] == 0 && targeted[i + 3] == 1;
    }

    /* Dragon Book 8.7: local patterns in the finished instruction list.
       Comment lines may sit between two instructions; a label may not. */
    static void peephole(std::vector<std::string> &lines) {
        auto isComment = [](const std::string &l) { return l.find_first_not_of(' ') != std::string::npos && l[l.find_first_not_of(' ')] == '#'; };
        auto parse = [](const std::string &l, std::string &op, std::string &a, std::string &b) {
            std::istringstream in(l);
            std::string rest;
            op.clear(); a.clear(); b.clear();
            in >> op;
            std::getline(in, rest);
            size_t comma = rest.find(',');
            auto trim = [](std::string t) {
                size_t x = t.find_first_not_of(' ');
                size_t y = t.find_last_not_of(' ');
                return x == std::string::npos ? std::string() : t.substr(x, y - x + 1);
            };
            a = trim(comma == std::string::npos ? rest : rest.substr(0, comma));
            b = comma == std::string::npos ? std::string() : trim(rest.substr(comma + 1));
        };
        std::vector<std::string> out;
        for (size_t i = 0; i < lines.size(); ++i) {
            std::string op, a, b;
            parse(lines[i], op, a, b);
            if (op == "move" && a == b) continue; /* move $r, $r */
            size_t next = i + 1;
            while (next < lines.size() && isComment(lines[next])) ++next;
            if (next < lines.size()) {
                std::string op2, a2, b2;
                parse(lines[next], op2, a2, b2);
                if (op == "j" && lines[next] == a + ":") continue; /* a jump to the next instruction */
                if (op == "sw" && op2 == "lw" && b == b2) { /* the value just stored is still in its register */
                    lines[next] = a2 == a ? std::string() : "        move  " + a2 + ", " + a;
                }
            }
            if (!lines[i].empty()) out.push_back(lines[i]);
        }
        lines.swap(out);
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

std::string generate(const Program &program, const std::string &runtime, bool optimize) {
    Emitter e(program);
    e.optimize = optimize;
    return e.run(runtime);
}

} // namespace mips
