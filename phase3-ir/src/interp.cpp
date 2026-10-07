/* The TAC interpreter: a small machine with byte-addressed memory. */
#include "interp.h"

#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <map>
#include <stdexcept>

namespace tac {

namespace {

using sem::TypePtr;

const uint32_t DATA_BASE = 0x1000;    /* below it: the null page */
const uint32_t STACK_BASE = 0x100000; /* frames grow upwards from here */
const uint32_t HEAP_BASE = 0x1000000;
const uint32_t MEMORY_LIMIT = 0x8000000;
const long long STEP_LIMIT = 500000000LL;

struct Arg { /* a `param` waiting for its call */
    Cls cls = Cls::Int;
    Val v;
    std::vector<uint8_t> bytes; /* a struct passed by value */
};

struct Layout { /* where a function's names are in its frame */
    std::map<const sem::Symbol *, uint32_t> vars;
    std::vector<uint32_t> temps;
    uint32_t width = 0;
};

struct Frame {
    const Function *fn = nullptr;
    const Layout *layout = nullptr;
    uint32_t base = 0;
    std::vector<Arg> varargs;
};

struct Fault : std::runtime_error {
    using std::runtime_error::runtime_error;
};

uint32_t alignUp(uint32_t v, uint32_t a) { return (v + a - 1) / a * a; }

class Machine {
  public:
    Machine(const Program &p, const std::string &in) : prog(p), input(in) {}

    RunResult run(const std::vector<std::string> &args) {
        RunResult result;
        try {
            load();
            const Function *entry = nullptr;
            for (const auto &f : prog.functions)
                if (f.linkName == "main") entry = &f;
            if (!entry) throw Fault("the program has no 'main' function");
            std::vector<Arg> argv;
            if (entry->sym && entry->sym->params.size() == 2) {
                std::vector<uint32_t> ptrs;
                for (const auto &a : args) ptrs.push_back(addString(a));
                uint32_t table = allocData(4 * (static_cast<uint32_t>(ptrs.size()) + 1), 4);
                for (size_t i = 0; i < ptrs.size(); ++i) write(table + 4 * static_cast<uint32_t>(i), Cls::Ptr, {ptrs[i], 0});
                Arg argc, av;
                argc.v.i = static_cast<long long>(args.size());
                av.cls = Cls::Ptr;
                av.v.i = table;
                argv = {argc, av};
            }
            Arg ret = call(*entry, argv);
            result.exitCode = static_cast<int>(static_cast<int32_t>(ret.v.i));
        } catch (const Fault &f) {
            result.error = f.what();
            result.exitCode = 1;
        }
        result.executed = executed;
        result.output = output;
        return result;
    }

    /* (everything below is file-local; the eval* functions at the end use the statics) */
    const Program &prog;
    std::string input;
    size_t inputPos = 0;
    std::vector<uint8_t> mem;
    std::map<const sem::Symbol *, uint32_t> globals;
    std::vector<uint32_t> strings;
    std::map<const sem::Symbol *, const Function *> functions;
    std::map<const Function *, Layout> layouts;
    uint32_t dataTop = DATA_BASE, heapTop = HEAP_BASE, stackTop = STACK_BASE;
    std::map<uint32_t, uint32_t> blocks; /* heap block -> size */
    long long executed = 0;
    std::string output;

    /* ---------------- memory ---------------- */

    void need(uint32_t addr, uint32_t size) {
        if (addr < DATA_BASE) throw Fault("invalid memory access at address " + std::to_string(addr) + " (null pointer?)");
        if (addr > MEMORY_LIMIT || size > MEMORY_LIMIT || addr + size > MEMORY_LIMIT) throw Fault("invalid memory access (address out of range)");
        if (addr + size > mem.size()) mem.resize(alignUp(addr + size, 4096), 0);
    }

    static uint32_t width(Cls c) {
        switch (c) {
            case Cls::Bool: case Cls::Char: case Cls::UChar: return 1;
            case Cls::Short: case Cls::UShort: return 2;
            case Cls::LLong: case Cls::ULLong: case Cls::Double: return 8;
            default: return 4;
        }
    }

    Val read(uint32_t addr, Cls c) {
        need(addr, width(c));
        Val v;
        const uint8_t *p = &mem[addr];
        switch (c) {
            case Cls::Bool: case Cls::UChar: v.i = *p; break;
            case Cls::Char: v.i = static_cast<int8_t>(*p); break;
            case Cls::Short: { int16_t x; memcpy(&x, p, 2); v.i = x; break; }
            case Cls::UShort: { uint16_t x; memcpy(&x, p, 2); v.i = x; break; }
            case Cls::Int: { int32_t x; memcpy(&x, p, 4); v.i = x; break; }
            case Cls::UInt: case Cls::Ptr: { uint32_t x; memcpy(&x, p, 4); v.i = x; break; }
            case Cls::LLong: case Cls::ULLong: { int64_t x; memcpy(&x, p, 8); v.i = x; break; }
            case Cls::Float: { float x; memcpy(&x, p, 4); v.f = x; break; }
            case Cls::Double: { double x; memcpy(&x, p, 8); v.f = x; break; }
            default: break;
        }
        return v;
    }

    void write(uint32_t addr, Cls c, Val v) {
        need(addr, width(c));
        uint8_t *p = &mem[addr];
        switch (c) {
            case Cls::Bool: case Cls::Char: case Cls::UChar: *p = static_cast<uint8_t>(v.i); break;
            case Cls::Short: case Cls::UShort: { uint16_t x = static_cast<uint16_t>(v.i); memcpy(p, &x, 2); break; }
            case Cls::Int: case Cls::UInt: case Cls::Ptr: { uint32_t x = static_cast<uint32_t>(v.i); memcpy(p, &x, 4); break; }
            case Cls::LLong: case Cls::ULLong: { int64_t x = v.i; memcpy(p, &x, 8); break; }
            case Cls::Float: { float x = static_cast<float>(v.f); memcpy(p, &x, 4); break; }
            case Cls::Double: { double x = v.f; memcpy(p, &x, 8); break; }
            default: break;
        }
    }

    void copy(uint32_t dst, uint32_t src, uint32_t size) {
        if (!size) return;
        need(dst, size);
        need(src, size);
        memmove(&mem[dst], &mem[src], size);
    }

    uint32_t allocData(uint32_t size, uint32_t align) {
        dataTop = alignUp(dataTop, std::max<uint32_t>(1, align));
        uint32_t at = dataTop;
        dataTop += std::max<uint32_t>(1, size);
        if (dataTop > STACK_BASE) throw Fault("static data does not fit in memory");
        need(at, std::max<uint32_t>(1, size));
        return at;
    }

    uint32_t addString(const std::string &bytes) {
        uint32_t at = allocData(static_cast<uint32_t>(bytes.size()) + 1, 1);
        memcpy(&mem[at], bytes.data(), bytes.size());
        mem[at + bytes.size()] = 0;
        return at;
    }

    std::string cstring(uint32_t addr) {
        std::string s;
        for (;; ++addr) {
            need(addr, 1);
            if (!mem[addr]) break;
            s += static_cast<char>(mem[addr]);
        }
        return s;
    }

    /* a literal as written in the source ("a\n") -> its bytes */
    static std::string decode(const std::string &literal) {
        std::string s;
        size_t i = 0;
        while (i < literal.size()) { /* adjacent literals are concatenated */
            if (literal[i] != '"') { ++i; continue; }
            for (++i; i < literal.size() && literal[i] != '"'; ++i) {
                char c = literal[i];
                if (c == '\\' && i + 1 < literal.size()) {
                    char e = literal[++i];
                    switch (e) {
                        case 'n': c = '\n'; break;
                        case 't': c = '\t'; break;
                        case 'r': c = '\r'; break;
                        case '0': c = '\0'; break;
                        case 'a': c = '\a'; break;
                        case 'b': c = '\b'; break;
                        default: c = e; break;
                    }
                }
                s += c;
            }
            ++i;
        }
        return s;
    }

    void load() {
        mem.assign(DATA_BASE, 0);
        for (const auto &s : prog.strings) strings.push_back(addString(decode(s)));
        for (const auto &g : prog.globals) {
            long long size = std::max(1LL, sem::sizeOf(g.sym->type));
            globals[g.sym.get()] = allocData(static_cast<uint32_t>(size), static_cast<uint32_t>(sem::alignOf(g.sym->type)));
        }
        for (const auto &g : prog.globals) {
            uint32_t base = globals[g.sym.get()];
            for (const auto &init : g.init) {
                Val v;
                switch (init.kind) {
                    case GlobalInit::Integer: v.i = init.i; break;
                    case GlobalInit::Floating: v.f = init.f; break;
                    case GlobalInit::Address: v.i = globals.count(init.target) ? globals[init.target] : 0; break;
                    case GlobalInit::String: v.i = init.str >= 0 ? strings[init.str] : 0; break;
                }
                write(base + static_cast<uint32_t>(init.offset), init.cls == Cls::Block ? Cls::Int : init.cls, v);
            }
        }
        for (const auto &f : prog.functions) {
            functions[f.sym.get()] = &f;
            Layout &l = layouts[&f];
            l.width = static_cast<uint32_t>(f.frameWidth);
            for (const auto &e : f.frame) {
                if (e.sym) l.vars[e.sym] = static_cast<uint32_t>(e.offset);
                else l.temps.push_back(static_cast<uint32_t>(e.offset));
            }
        }
    }

    /* ---------------- operands ---------------- */

    uint32_t addressOf(const Operand &o, const Frame &fr) {
        switch (o.kind) {
            case Operand::Temp:
                if (o.temp < 1 || o.temp > static_cast<int>(fr.layout->temps.size())) throw Fault("unknown temporary");
                return fr.base + fr.layout->temps[o.temp - 1];
            case Operand::Var: {
                auto local = fr.layout->vars.find(o.sym);
                if (local != fr.layout->vars.end()) return fr.base + local->second;
                auto global = globals.find(o.sym);
                if (global != globals.end()) return global->second;
                throw Fault("no storage for '" + o.sym->name + "'");
            }
            case Operand::Str:
                return strings[o.str];
            default:
                throw Fault("a constant has no address");
        }
    }

    Val value(const Operand &o, const Frame &fr) {
        Val v;
        switch (o.kind) {
            case Operand::IntConst: v.i = o.ival; v.f = static_cast<double>(o.ival); return v;
            case Operand::FloatConst: v.f = o.fval; return v;
            case Operand::Str: v.i = strings[o.str]; return v;
            case Operand::None: return v;
            default: return read(addressOf(o, fr), classOf(o.type));
        }
    }

    static uint32_t sizeOfType(const TypePtr &t) { return static_cast<uint32_t>(std::max(0LL, sem::sizeOf(t))); }

    /* r = v, for any class of r (a struct is copied byte by byte) */
    void assign(const Operand &r, const Operand &src, const Frame &fr) {
        if (r.isNone()) return;
        Cls c = classOf(r.type);
        if (c == Cls::Block) copy(addressOf(r, fr), addressOf(src, fr), sizeOfType(r.type));
        else write(addressOf(r, fr), c, value(src, fr));
    }

    /* ---------------- arithmetic ---------------- */

    static Val wrap(Cls c, Val v) {
        switch (c) {
            case Cls::Bool: v.i = v.i != 0; break;
            case Cls::Char: v.i = static_cast<int8_t>(v.i); break;
            case Cls::UChar: v.i = static_cast<uint8_t>(v.i); break;
            case Cls::Short: v.i = static_cast<int16_t>(v.i); break;
            case Cls::UShort: v.i = static_cast<uint16_t>(v.i); break;
            case Cls::Int: v.i = static_cast<int32_t>(v.i); break;
            case Cls::UInt: case Cls::Ptr: v.i = static_cast<uint32_t>(v.i); break;
            case Cls::Float: v.f = static_cast<float>(v.f); break;
            default: break;
        }
        return v;
    }

    static Val arithmetic(const Quad &q, Val a, Val b) {
        Val r;
        Cls c = q.cls;
        if (isFloatCls(c)) {
            switch (q.op) {
                case Op::Add: r.f = a.f + b.f; break;
                case Op::Sub: r.f = a.f - b.f; break;
                case Op::Mul: r.f = a.f * b.f; break;
                case Op::Div: r.f = a.f / b.f; break;
                case Op::Neg: r.f = -a.f; break;
                default: throw Fault("operator not defined on floating-point values");
            }
            return wrap(c, r);
        }
        bool isUnsigned = c == Cls::UInt || c == Cls::Ptr || c == Cls::ULLong;
        bool wide = c == Cls::LLong || c == Cls::ULLong;
        uint64_t x = static_cast<uint64_t>(a.i), y = static_cast<uint64_t>(b.i);
        if (!wide && isUnsigned) { x = static_cast<uint32_t>(x); y = static_cast<uint32_t>(y); }
        int bits = wide ? 64 : 32;
        switch (q.op) {
            case Op::Add: r.i = static_cast<long long>(x + y); break;
            case Op::Sub: r.i = static_cast<long long>(x - y); break;
            case Op::Mul: r.i = static_cast<long long>(x * y); break;
            case Op::Div: case Op::Mod: {
                if (y == 0 || (!isUnsigned && b.i == 0)) throw Fault("division by zero");
                if (isUnsigned) r.i = static_cast<long long>(q.op == Op::Div ? x / y : x % y);
                else if (b.i == -1) r.i = q.op == Op::Div ? static_cast<long long>(0 - x) : 0;
                else r.i = q.op == Op::Div ? a.i / b.i : a.i % b.i;
                break;
            }
            case Op::BitAnd: r.i = static_cast<long long>(x & y); break;
            case Op::BitOr: r.i = static_cast<long long>(x | y); break;
            case Op::BitXor: r.i = static_cast<long long>(x ^ y); break;
            case Op::Shl: r.i = static_cast<long long>(x << (y & (bits - 1))); break;
            case Op::Shr:
                if (isUnsigned) r.i = static_cast<long long>(x >> (y & (bits - 1)));
                else r.i = a.i >> (y & (bits - 1));
                break;
            case Op::Neg: r.i = static_cast<long long>(0 - x); break;
            case Op::BitNot: r.i = static_cast<long long>(~x); break;
            default: break;
        }
        return wrap(c, r);
    }

    static Val converted(Cls from, Cls to, Val v) {
        Val r;
        if (isFloatCls(to)) {
            if (isFloatCls(from)) r.f = v.f;
            else if (from == Cls::ULLong) r.f = static_cast<double>(static_cast<uint64_t>(v.i));
            else r.f = static_cast<double>(v.i);
        } else if (isFloatCls(from)) {
            if (to == Cls::ULLong) r.i = static_cast<long long>(static_cast<uint64_t>(v.f));
            else r.i = static_cast<long long>(v.f);
        } else {
            r.i = v.i;
        }
        return wrap(to, r);
    }

    static bool compare(const Quad &q, Val a, Val b) {
        int order;
        if (isFloatCls(q.cls)) {
            if (std::isnan(a.f) || std::isnan(b.f)) return q.relop == "!=";
            order = a.f < b.f ? -1 : a.f > b.f ? 1 : 0;
        } else if (q.cls == Cls::UInt || q.cls == Cls::Ptr || q.cls == Cls::ULLong || q.cls == Cls::Bool ||
                   q.cls == Cls::UChar || q.cls == Cls::UShort) {
            uint64_t x = static_cast<uint64_t>(a.i), y = static_cast<uint64_t>(b.i);
            if (q.cls != Cls::ULLong) { x = static_cast<uint32_t>(x); y = static_cast<uint32_t>(y); }
            order = x < y ? -1 : x > y ? 1 : 0;
        } else {
            order = a.i < b.i ? -1 : a.i > b.i ? 1 : 0;
        }
        if (q.relop == "==") return order == 0;
        if (q.relop == "!=") return order != 0;
        if (q.relop == "<") return order < 0;
        if (q.relop == ">") return order > 0;
        if (q.relop == "<=") return order <= 0;
        return order >= 0;
    }

    /* ---------------- built-in functions ---------------- */

    uint32_t heapAlloc(uint32_t size) {
        heapTop = alignUp(heapTop, 8);
        uint32_t at = heapTop;
        heapTop += std::max<uint32_t>(size, 1);
        need(at, std::max<uint32_t>(size, 1));
        memset(&mem[at], 0, std::max<uint32_t>(size, 1));
        blocks[at] = size;
        return at;
    }

    std::string format(const std::vector<Arg> &args) {
        std::string fmt = cstring(static_cast<uint32_t>(args[0].v.i)), out;
        size_t next = 1;
        auto take = [&]() -> Arg { return next < args.size() ? args[next++] : Arg(); };
        for (size_t i = 0; i < fmt.size(); ++i) {
            if (fmt[i] != '%') { out += fmt[i]; continue; }
            std::string spec = "%";
            ++i;
            while (i < fmt.size() && strchr("-+ #0", fmt[i])) spec += fmt[i++];
            auto number = [&]() {
                if (i < fmt.size() && fmt[i] == '*') { spec += std::to_string(static_cast<int>(take().v.i)); ++i; }
                else while (i < fmt.size() && isdigit(static_cast<unsigned char>(fmt[i]))) spec += fmt[i++];
            };
            number();
            if (i < fmt.size() && fmt[i] == '.') { spec += fmt[i++]; number(); }
            std::string length;
            while (i < fmt.size() && strchr("hlLzjt", fmt[i])) length += fmt[i++];
            if (i >= fmt.size()) break;
            char conv = fmt[i];
            char buf[512];
            switch (conv) {
                case '%': out += '%'; continue;
                case 'd': case 'i': {
                    long long v = take().v.i;
                    if (length != "ll") v = static_cast<int32_t>(v);
                    snprintf(buf, sizeof buf, (spec + "lld").c_str(), v);
                    break;
                }
                case 'u': case 'x': case 'X': case 'o': {
                    unsigned long long v = static_cast<unsigned long long>(take().v.i);
                    if (length != "ll") v = static_cast<uint32_t>(v);
                    snprintf(buf, sizeof buf, (spec + "ll" + conv).c_str(), v);
                    break;
                }
                case 'c': snprintf(buf, sizeof buf, (spec + "c").c_str(), static_cast<int>(take().v.i)); break;
                case 'f': case 'F': case 'e': case 'E': case 'g': case 'G': {
                    Arg a = take();
                    snprintf(buf, sizeof buf, (spec + conv).c_str(), isFloatCls(a.cls) ? a.v.f : static_cast<double>(a.v.i));
                    break;
                }
                case 's': {
                    std::string s = cstring(static_cast<uint32_t>(take().v.i));
                    std::vector<char> big(s.size() + 512);
                    snprintf(big.data(), big.size(), (spec + "s").c_str(), s.c_str());
                    out += big.data();
                    continue;
                }
                case 'p': snprintf(buf, sizeof buf, "0x%x", static_cast<uint32_t>(take().v.i)); break;
                default: buf[0] = conv; buf[1] = 0; break;
            }
            out += buf;
        }
        return out;
    }

    void skipSpace() {
        while (inputPos < input.size() && isspace(static_cast<unsigned char>(input[inputPos]))) ++inputPos;
    }

    long long scan(const std::vector<Arg> &args) {
        std::string fmt = cstring(static_cast<uint32_t>(args[0].v.i));
        size_t next = 1;
        long long assigned = 0;
        for (size_t i = 0; i < fmt.size(); ++i) {
            if (isspace(static_cast<unsigned char>(fmt[i]))) { skipSpace(); continue; }
            if (fmt[i] != '%') {
                if (inputPos < input.size() && input[inputPos] == fmt[i]) { ++inputPos; continue; }
                return assigned;
            }
            ++i;
            int maxWidth = 0;
            while (i < fmt.size() && isdigit(static_cast<unsigned char>(fmt[i]))) maxWidth = maxWidth * 10 + (fmt[i++] - '0');
            std::string length;
            while (i < fmt.size() && strchr("hlL", fmt[i])) length += fmt[i++];
            if (i >= fmt.size() || next >= args.size()) return assigned;
            char conv = fmt[i];
            uint32_t dst = static_cast<uint32_t>(args[next++].v.i);
            if (conv == 'c') {
                if (inputPos >= input.size()) return assigned ? assigned : -1;
                write(dst, Cls::Char, {input[inputPos++], 0});
                ++assigned;
                continue;
            }
            skipSpace();
            if (inputPos >= input.size()) return assigned ? assigned : -1;
            const char *start = input.c_str() + inputPos;
            char *end = nullptr;
            if (conv == 's') {
                size_t n = 0;
                while (inputPos < input.size() && !isspace(static_cast<unsigned char>(input[inputPos])) &&
                       (maxWidth == 0 || static_cast<int>(n) < maxWidth)) {
                    write(dst + static_cast<uint32_t>(n++), Cls::Char, {input[inputPos++], 0});
                }
                write(dst + static_cast<uint32_t>(n), Cls::Char, {0, 0});
            } else if (conv == 'f' || conv == 'e' || conv == 'g') {
                double v = strtod(start, &end);
                if (end == start) return assigned;
                inputPos += static_cast<size_t>(end - start);
                write(dst, length.empty() ? Cls::Float : Cls::Double, {0, v});
            } else {
                long long v = strtoll(start, &end, conv == 'x' ? 16 : conv == 'o' ? 8 : 10);
                if (end == start) return assigned;
                inputPos += static_cast<size_t>(end - start);
                Cls c = length == "ll" ? Cls::LLong : length == "h" ? Cls::Short : length == "hh" ? Cls::Char : Cls::Int;
                write(dst, c, {v, 0});
            }
            ++assigned;
        }
        return assigned;
    }

    Val builtinCall(const std::string &name, const std::vector<Arg> &args) {
        Val r;
        auto arg = [&](size_t i) -> long long { return i < args.size() ? args[i].v.i : 0; };
        if (name == "printf") {
            if (args.empty()) return r;
            std::string text = format(args);
            output += text;
            r.i = static_cast<long long>(text.size());
        } else if (name == "scanf") {
            r.i = args.empty() ? 0 : scan(args);
        } else if (name == "malloc") {
            r.i = heapAlloc(static_cast<uint32_t>(arg(0)));
        } else if (name == "calloc") {
            r.i = heapAlloc(static_cast<uint32_t>(arg(0) * arg(1)));
        } else if (name == "realloc") {
            uint32_t old = static_cast<uint32_t>(arg(0)), size = static_cast<uint32_t>(arg(1));
            uint32_t fresh = heapAlloc(size);
            auto known = blocks.find(old);
            if (old && known != blocks.end()) copy(fresh, old, std::min(size, known->second));
            r.i = fresh;
        } else if (name == "free") {
            /* memory is not reused: a freed block stays readable, as on a real heap */
        } else {
            throw Fault("call to unknown built-in function '" + name + "'");
        }
        return r;
    }

    /* ---------------- execution ---------------- */

    Arg call(const Function &f, const std::vector<Arg> &args) {
        Frame fr;
        fr.fn = &f;
        fr.layout = &layouts[&f];
        stackTop = alignUp(stackTop, 8);
        fr.base = stackTop;
        if (fr.base + fr.layout->width + 16 > HEAP_BASE) throw Fault("stack overflow (recursion too deep)");
        stackTop += fr.layout->width + 8;
        need(fr.base, fr.layout->width + 8);
        memset(&mem[fr.base], 0, fr.layout->width + 8);

        /* bind `this`, then the declared parameters; the rest are `...` */
        std::vector<const sem::Symbol *> params;
        if (f.thisSym) params.push_back(f.thisSym);
        if (f.sym)
            for (const auto &p : f.sym->params) params.push_back(p.get());
        for (size_t i = 0; i < args.size(); ++i) {
            if (i >= params.size()) { fr.varargs.push_back(args[i]); continue; }
            auto slot = fr.layout->vars.find(params[i]);
            if (slot == fr.layout->vars.end()) continue;
            uint32_t at = fr.base + slot->second;
            Cls c = classOf(params[i]->type);
            if (c == Cls::Block) {
                need(at, static_cast<uint32_t>(args[i].bytes.size()));
                if (!args[i].bytes.empty()) memcpy(&mem[at], args[i].bytes.data(), args[i].bytes.size());
            } else {
                write(at, c, args[i].v);
            }
        }

        Arg result;
        std::vector<Arg> pending;
        size_t pc = 0;
        while (pc < f.quads.size()) {
            const Quad &q = f.quads[pc];
            if (++executed > STEP_LIMIT) throw Fault("instruction limit reached (infinite loop?)");
            size_t nextPc = pc + 1;
            switch (q.op) {
                case Op::Assign:
                    assign(q.r, q.a, fr);
                    break;
                case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod:
                case Op::BitAnd: case Op::BitOr: case Op::BitXor: case Op::Shl: case Op::Shr:
                    write(addressOf(q.r, fr), classOf(q.r.type), arithmetic(q, value(q.a, fr), value(q.b, fr)));
                    break;
                case Op::Neg: case Op::BitNot:
                    write(addressOf(q.r, fr), classOf(q.r.type), arithmetic(q, value(q.a, fr), Val()));
                    break;
                case Op::Conv:
                    write(addressOf(q.r, fr), q.cls, converted(q.from, q.cls, value(q.a, fr)));
                    break;
                case Op::Goto:
                    nextPc = static_cast<size_t>(q.target);
                    break;
                case Op::IfRel:
                    if (compare(q, value(q.a, fr), value(q.b, fr))) nextPc = static_cast<size_t>(q.target);
                    break;
                case Op::IndexLoad: {
                    uint32_t at = addressOf(q.a, fr) + static_cast<uint32_t>(value(q.b, fr).i);
                    Cls c = classOf(q.r.type);
                    if (c == Cls::Block) copy(addressOf(q.r, fr), at, sizeOfType(q.r.type));
                    else write(addressOf(q.r, fr), c, read(at, c));
                    break;
                }
                case Op::IndexStore: {
                    uint32_t at = addressOf(q.a, fr) + static_cast<uint32_t>(value(q.b, fr).i);
                    if (q.cls == Cls::Block) copy(at, addressOf(q.r, fr), sizeOfType(q.r.type));
                    else write(at, q.cls, value(q.r, fr));
                    break;
                }
                case Op::AddrOf:
                    write(addressOf(q.r, fr), Cls::Ptr, {addressOf(q.a, fr), 0});
                    break;
                case Op::Load: {
                    uint32_t at = static_cast<uint32_t>(value(q.a, fr).i);
                    Cls c = classOf(q.r.type);
                    if (c == Cls::Block) copy(addressOf(q.r, fr), at, sizeOfType(q.r.type));
                    else write(addressOf(q.r, fr), c, read(at, c));
                    break;
                }
                case Op::Store: {
                    uint32_t at = static_cast<uint32_t>(value(q.a, fr).i);
                    if (q.cls == Cls::Block) copy(at, addressOf(q.r, fr), sizeOfType(q.r.type));
                    else write(at, q.cls, value(q.r, fr));
                    break;
                }
                case Op::Param: {
                    Arg a;
                    a.cls = classOf(q.a.type);
                    if (a.cls == Cls::Block) {
                        uint32_t at = addressOf(q.a, fr), size = sizeOfType(q.a.type);
                        need(at, size);
                        a.bytes.assign(mem.begin() + at, mem.begin() + at + size);
                    } else {
                        a.v = value(q.a, fr);
                    }
                    pending.push_back(a);
                    break;
                }
                case Op::Call: {
                    size_t n = std::min(static_cast<size_t>(q.nargs), pending.size());
                    std::vector<Arg> callArgs(pending.end() - static_cast<long>(n), pending.end());
                    pending.resize(pending.size() - n);
                    if (q.callee) {
                        auto target = functions.find(q.callee);
                        if (target == functions.end())
                            throw Fault("call to '" + signatureOf(*q.callee) + "', which has no definition");
                        uint32_t savedStack = stackTop;
                        Arg ret = call(*target->second, callArgs);
                        stackTop = savedStack;
                        if (!q.r.isNone()) {
                            Cls c = classOf(q.r.type);
                            if (c == Cls::Block) {
                                uint32_t at = addressOf(q.r, fr);
                                need(at, static_cast<uint32_t>(ret.bytes.size()));
                                if (!ret.bytes.empty()) memcpy(&mem[at], ret.bytes.data(), ret.bytes.size());
                            } else {
                                write(addressOf(q.r, fr), c, ret.v);
                            }
                        }
                    } else {
                        Val v = builtinCall(q.calleeName, callArgs);
                        if (!q.r.isNone()) write(addressOf(q.r, fr), classOf(q.r.type), v);
                    }
                    break;
                }
                case Op::Return:
                    if (!q.a.isNone()) {
                        result.cls = classOf(q.a.type);
                        if (result.cls == Cls::Block) {
                            uint32_t at = addressOf(q.a, fr), size = sizeOfType(q.a.type);
                            need(at, size);
                            result.bytes.assign(mem.begin() + at, mem.begin() + at + size);
                        } else {
                            result.v = value(q.a, fr);
                        }
                    }
                    return result;
                case Op::VaStart: {
                    /* the extra arguments in 8-byte slots (double or 64-bit integer);
                       `ap` is a pointer into them, so it can be passed on */
                    uint32_t area = heapAlloc(8 * static_cast<uint32_t>(fr.varargs.size()) + 8);
                    for (size_t i = 0; i < fr.varargs.size(); ++i)
                        write(area + 8 * static_cast<uint32_t>(i), isFloatCls(fr.varargs[i].cls) ? Cls::Double : Cls::LLong,
                              fr.varargs[i].v);
                    write(addressOf(q.a, fr), Cls::Ptr, {area, 0});
                    break;
                }
                case Op::VaArg: {
                    uint32_t cursor = addressOf(q.a, fr);
                    uint32_t slot = static_cast<uint32_t>(read(cursor, Cls::Ptr).i);
                    Val v = read(slot, isFloatCls(q.cls) ? Cls::Double : Cls::LLong);
                    write(cursor, Cls::Ptr, {slot + 8, 0});
                    write(addressOf(q.r, fr), classOf(q.r.type), v);
                    break;
                }
                case Op::VaEnd:
                    break;
            }
            pc = nextPc;
        }
        return result;
    }
};

} // namespace

Val evalWrap(Cls c, Val v) { return Machine::wrap(c, v); }
Val evalArithmetic(const Quad &q, Val a, Val b) { return Machine::arithmetic(q, a, b); }
Val evalConvert(Cls from, Cls to, Val v) { return Machine::converted(from, to, v); }
bool evalCompare(const Quad &q, Val a, Val b) { return Machine::compare(q, a, b); }

RunResult run(const Program &program, const std::vector<std::string> &args, const std::string &input) {
    Machine m(program, input);
    return m.run(args);
}

} // namespace tac
