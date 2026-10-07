/* Three address code: classification helpers and the listing printer. */
#include "tac.h"

#include <cstdio>
#include <map>
#include <set>
#include <sstream>

namespace tac {

using sem::TypeKind;
using sem::TypePtr;

Cls classOf(const TypePtr &t) {
    if (!t) return Cls::Void;
    switch (t->kind) {
        case TypeKind::Bool: return Cls::Bool;
        case TypeKind::Char: return t->isUnsigned ? Cls::UChar : Cls::Char;
        case TypeKind::Short: return t->isUnsigned ? Cls::UShort : Cls::Short;
        case TypeKind::Int: case TypeKind::Long: return t->isUnsigned ? Cls::UInt : Cls::Int;
        case TypeKind::LongLong: return t->isUnsigned ? Cls::ULLong : Cls::LLong;
        case TypeKind::Float: return Cls::Float;
        case TypeKind::Double: return Cls::Double;
        case TypeKind::Pointer: case TypeKind::Reference: case TypeKind::Array: case TypeKind::Opaque:
            return Cls::Ptr; /* an array used as a value is the address of its first element */
        case TypeKind::Record: return Cls::Block;
        default: return Cls::Void;
    }
}

const char *clsName(Cls c) {
    switch (c) {
        case Cls::Void: return "void";
        case Cls::Bool: return "bool";
        case Cls::Char: return "char";
        case Cls::UChar: return "uchar";
        case Cls::Short: return "short";
        case Cls::UShort: return "ushort";
        case Cls::Int: return "int";
        case Cls::UInt: return "uint";
        case Cls::LLong: return "llong";
        case Cls::ULLong: return "ullong";
        case Cls::Float: return "float";
        case Cls::Double: return "double";
        case Cls::Ptr: return "ptr";
        case Cls::Block: return "block";
    }
    return "?";
}

bool isFloatCls(Cls c) { return c == Cls::Float || c == Cls::Double; }
bool isIntegerCls(Cls c) { return c != Cls::Void && c != Cls::Block && !isFloatCls(c); }

std::string signatureOf(const sem::Symbol &fn) {
    std::string s = (fn.ownerRecord ? fn.ownerRecord->tag + "::" : std::string()) + fn.name + "(";
    if (fn.type && sem::isFunction(fn.type)) {
        for (size_t i = 0; i < fn.type->params.size(); ++i) {
            if (i) s += ", ";
            s += sem::typeToString(fn.type->params[i]);
        }
        if (fn.type->variadic) s += fn.type->params.empty() ? "..." : ", ...";
    }
    return s + ")";
}

std::string floatText(double v) {
    char buf[64];
    snprintf(buf, sizeof buf, "%.17g", v);
    std::string s = buf;
    /* the shortest spelling that reads back as the same double */
    for (int prec = 1; prec < 17; ++prec) {
        char shortBuf[64];
        snprintf(shortBuf, sizeof shortBuf, "%.*g", prec, v);
        if (std::stod(shortBuf) == v) { s = shortBuf; break; }
    }
    if (s.find_first_of(".einf") == std::string::npos) s += ".0";
    return s;
}

namespace {

const char *opSymbol(Op op) {
    switch (op) {
        case Op::Add: return "+";
        case Op::Sub: return "-";
        case Op::Mul: return "*";
        case Op::Div: return "/";
        case Op::Mod: return "%";
        case Op::BitAnd: return "&";
        case Op::BitOr: return "|";
        case Op::BitXor: return "^";
        case Op::Shl: return "<<";
        case Op::Shr: return ">>";
        case Op::Neg: return "-";
        case Op::BitNot: return "~";
        default: return "?";
    }
}


/* Locals print under their own name when that is unambiguous in the
   function and under the symbol table's unique name (x.7) when two
   live in different blocks or one hides a global. */
struct Names {
    std::map<const sem::Symbol *, std::string> shown;

    Names(const Program &p, const Function &f) {
        std::set<std::string> globals;
        for (const auto &g : p.globals) globals.insert(g.sym->name);
        std::map<std::string, int> count;
        auto add = [&](const sem::SymbolPtr &s) { if (s && !s->name.empty()) count[s->name]++; };
        if (f.sym) {
            for (const auto &s : f.sym->params) add(s);
            for (const auto &s : f.sym->locals) add(s);
        }
        auto decide = [&](const sem::SymbolPtr &s) {
            if (!s) return;
            bool plain = !s->name.empty() && count[s->name] == 1 && !globals.count(s->name) &&
                         s->storage != sem::Storage::Static;
            shown[s.get()] = plain ? s->name : s->uniqueName;
        };
        if (f.sym) {
            for (const auto &s : f.sym->params) decide(s);
            for (const auto &s : f.sym->locals) decide(s);
        }
    }

    std::string of(const sem::Symbol *s) const {
        auto it = shown.find(s);
        if (it != shown.end()) return it->second;
        return s->uniqueName.empty() ? s->name : s->uniqueName;
    }
};

std::string operandText(const Program &p, const Names &names, const Operand &o) {
    switch (o.kind) {
        case Operand::None: return "_";
        case Operand::IntConst:
            return sem::constantToString(o.ival, o.type);
        case Operand::FloatConst: return floatText(o.fval);
        case Operand::Temp: return "t" + std::to_string(o.temp);
        case Operand::Var: return names.of(o.sym);
        case Operand::Str: return o.str >= 0 && o.str < static_cast<int>(p.strings.size()) ? p.strings[o.str] : "\"?\"";
    }
    return "?";
}

std::string quadTextWith(const Program &p, const Names &names, const Quad &q,
                         const std::vector<std::string> &labelOfIndex) {
    auto T = [&](const Operand &o) { return operandText(p, names, o); };
    auto target = [&]() -> std::string {
        if (q.target < 0) return "?";
        if (q.target < static_cast<int>(labelOfIndex.size()) && !labelOfIndex[q.target].empty())
            return labelOfIndex[q.target];
        return std::to_string(q.target);
    };
    std::string s;
    switch (q.op) {
        case Op::Assign: s = T(q.r) + " = " + T(q.a); break;
        case Op::Add: case Op::Sub: case Op::Mul: case Op::Div: case Op::Mod:
        case Op::BitAnd: case Op::BitOr: case Op::BitXor: case Op::Shl: case Op::Shr:
            s = T(q.r) + " = " + T(q.a) + " " + clsName(q.cls) + opSymbol(q.op) + " " + T(q.b);
            break;
        case Op::Neg: case Op::BitNot:
            s = T(q.r) + " = " + clsName(q.cls) + opSymbol(q.op) + " " + T(q.a);
            break;
        case Op::Conv:
            s = T(q.r) + " = " + clsName(q.from) + "to" + clsName(q.cls) + " " + T(q.a);
            break;
        case Op::Goto: s = "goto " + target(); break;
        case Op::IfRel:
            s = "if " + T(q.a) + " " + clsName(q.cls) + q.relop + " " + T(q.b) + " goto " + target();
            break;
        case Op::IndexLoad: s = T(q.r) + " = " + T(q.a) + "[" + T(q.b) + "]"; break;
        case Op::IndexStore: s = T(q.a) + "[" + T(q.b) + "] = " + T(q.r); break;
        case Op::AddrOf: s = T(q.r) + " = &" + T(q.a); break;
        case Op::Load: s = T(q.r) + " = *" + T(q.a); break;
        case Op::Store: s = "*" + T(q.a) + " = " + T(q.r); break;
        case Op::Param: s = "param " + T(q.a); break;
        case Op::Call: {
            std::string callee = q.callee ? signatureOf(*q.callee) : q.calleeName;
            s = (q.r.isNone() ? std::string() : T(q.r) + " = ") + "call " + callee + ", " + std::to_string(q.nargs);
            break;
        }
        case Op::Return: s = q.a.isNone() ? "return" : "return " + T(q.a); break;
        case Op::VaStart: s = "va_start " + T(q.a) + ", " + T(q.b); break;
        case Op::VaArg: s = T(q.r) + " = va_arg " + T(q.a) + ", " + clsName(q.cls); break;
        case Op::VaEnd: s = "va_end " + T(q.a); break;
    }
    return s;
}

/* every instruction that some jump targets gets a label; numbering is
   program-wide so the labels can be used as they are in assembly */
std::vector<std::string> assignLabels(const Function &f, int &nextLabel) {
    std::vector<bool> isTarget(f.quads.size() + 1, false);
    for (const auto &q : f.quads) {
        if ((q.op == Op::Goto || q.op == Op::IfRel) && q.target >= 0 && q.target <= static_cast<int>(f.quads.size()))
            isTarget[q.target] = true;
    }
    std::vector<std::string> labels(f.quads.size() + 1);
    for (size_t i = 0; i < isTarget.size(); ++i) {
        if (isTarget[i]) labels[i] = "L" + std::to_string(nextLabel++);
    }
    return labels;
}

void printFunctionWith(const Program &p, const Function &f, std::ostream &out, int &nextLabel) {
    Names names(p, f);
    std::vector<std::string> labels = assignLabels(f, nextLabel);

    out << "function " << f.signature;
    if (f.linkName != f.signature) out << "        link name: " << f.linkName;
    out << "\n";
    if (!f.frame.empty()) {
        out << "  symbol table (name, kind, type, width, offset)\n";
        for (const auto &e : f.frame) {
            char line[256];
            std::string name = e.sym && !e.sym->name.empty() ? names.of(e.sym) : e.name;
            snprintf(line, sizeof line, "    %-14s %-6s %-22s %5lld %6lld\n", name.c_str(), e.kind.c_str(),
                     sem::typeToString(e.type).c_str(), e.width, e.offset);
            out << line;
        }
        out << "    total width " << f.frameWidth << "\n";
    }
    out << "  code\n";
    size_t labelWidth = 0;
    for (const auto &l : labels) labelWidth = std::max(labelWidth, l.size());
    for (size_t i = 0; i < f.quads.size(); ++i) {
        const Quad &q = f.quads[i];
        std::string text = quadTextWith(p, names, q, labels);
        std::string label = labels[i].empty() ? std::string() : labels[i] + ":";
        char head[64];
        snprintf(head, sizeof head, "%4d: %-*s ", f.firstIndex + static_cast<int>(i),
                 static_cast<int>(labelWidth + 1), label.c_str());
        out << head << text;
        if (!q.note.empty()) {
            if (text.size() < 34) out << std::string(34 - text.size(), ' ');
            out << "  " << q.note;
        }
        out << "\n";
    }
    out << "\n";
}

} // namespace

std::string quadText(const Program &p, const Function &f, const Quad &q,
                     const std::vector<std::string> &labelOfIndex) {
    Names names(p, f);
    return quadTextWith(p, names, q, labelOfIndex);
}

void printFunction(const Program &p, const Function &f, std::ostream &out) {
    int nextLabel = 1;
    printFunctionWith(p, f, out, nextLabel);
}

void printProgram(const Program &p, std::ostream &out) {
    if (!p.globals.empty()) {
        out << "globals (name, type, width, initial value)\n";
        for (const auto &g : p.globals) {
            char line[256];
            snprintf(line, sizeof line, "    %-14s %-22s %5lld  ", g.sym->uniqueName.c_str(),
                     sem::typeToString(g.sym->type).c_str(), sem::sizeOf(g.sym->type));
            out << line;
            if (g.init.empty()) {
                out << "0";
            } else if (g.init.size() == 1 && g.init[0].offset == 0 && !sem::isArray(g.sym->type) &&
                       !sem::isRecord(g.sym->type)) {
                out << g.init[0].value;
            } else {
                out << "{";
                for (size_t i = 0; i < g.init.size(); ++i)
                    out << (i ? ", " : " ") << "+" << g.init[i].offset << ": " << g.init[i].value;
                out << " }";
            }
            out << "\n";
        }
        out << "\n";
    }
    int nextLabel = 1;
    for (const auto &f : p.functions) printFunctionWith(p, f, out, nextLabel);
}

} // namespace tac
