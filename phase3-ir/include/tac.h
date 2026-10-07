#ifndef TAC_H
#define TAC_H

/* =====================================================================
   THREE ADDRESS CODE
   ---------------------------------------------------------------------
   The intermediate representation, in the form of the course slides
   (Lectures 25-27) and Dragon Book chapter 6:

     - an instruction is a quadruple (op, arg1, arg2, result) with named
       temporaries (`E.place = newtmp()`), kept in a numbered array per
       function;
     - a jump's target is an index into that array, filled in by
       backpatching; when the code is printed every target instruction
       also gets a label (L1, L2, ...);
     - arithmetic carries the type it works on (`int+`, `double*`) and
       every conversion is its own instruction (`inttodouble`).

   Instruction forms (x, y, z are names, temporaries or constants):

     x = y op z          x = op y            x = y
     x = <a>to<b> y      conversion
     goto L              if x relop y goto L
     x = y[z]            y[z] = x            z is a byte offset from y
     x = &y              x = *y              *x = y
     param x             call f, n           x = call f, n
     return              return x
     va_start x, y       x = va_arg y        va_end x
   ===================================================================== */

#include <memory>
#include <ostream>
#include <string>
#include <vector>

#include "symbol_table/symbol_table.hpp"
#include "types/types.hpp"

namespace tac {

/* The machine class of a value: what decides which MIPS instruction an
   operator becomes. Bool/Char/Short only exist in memory; arithmetic
   happens in Int and above (C's integer promotions). */
enum class Cls { Void, Bool, Char, UChar, Short, UShort, Int, UInt, LLong, ULLong, Float, Double, Ptr, Block };

Cls classOf(const sem::TypePtr &t);
const char *clsName(Cls c);
bool isFloatCls(Cls c);
bool isIntegerCls(Cls c);

struct Operand {
    enum Kind { None, IntConst, FloatConst, Temp, Var, Str } kind = None;
    long long ival = 0;         /* IntConst */
    double fval = 0;            /* FloatConst */
    int temp = 0;               /* Temp: 1, 2, ... (t1, t2, ...) */
    sem::Symbol *sym = nullptr; /* Var */
    int str = -1;               /* Str: index into Program::strings */
    sem::TypePtr type;

    bool isNone() const { return kind == None; }
    bool isConst() const { return kind == IntConst || kind == FloatConst; }
};

enum class Op {
    Assign,                                               /* r = a */
    Add, Sub, Mul, Div, Mod, BitAnd, BitOr, BitXor, Shl, Shr, /* r = a op b */
    Neg, BitNot,                                          /* r = op a */
    Conv,                                                 /* r = <from>to<cls> a */
    Goto,                                                 /* goto target */
    IfRel,                                                /* if a relop b goto target */
    IndexLoad,                                            /* r = a[b] */
    IndexStore,                                           /* a[b] = r */
    AddrOf,                                               /* r = &a */
    Load,                                                 /* r = *a */
    Store,                                                /* *a = r */
    Param,                                                /* param a */
    Call,                                                 /* [r =] call callee, nargs */
    Return,                                               /* return [a] */
    VaStart,                                              /* va_start a, b */
    VaArg,                                                /* r = va_arg a */
    VaEnd                                                 /* va_end a */
};

struct Quad {
    Op op = Op::Assign;
    Operand a, b, r;
    Cls cls = Cls::Void;      /* the type the operator works on */
    Cls from = Cls::Void;     /* Conv: source class */
    std::string relop;        /* IfRel: == != < > <= >= */
    int target = -1;          /* Goto / IfRel: index in the function, -1 until backpatched */
    sem::Symbol *callee = nullptr; /* Call: a user function ... */
    std::string calleeName;        /* ... or a built-in (printf, malloc, ...) */
    int nargs = 0;
    std::string note;         /* shown beside the instruction: "(this)", "(n2 = 4)" */
    int line = 0;             /* source line */
};

/* one row of a procedure's symbol table (Lecture 25: enter(table, name,
   type, offset); addwidth(table, width)) */
struct FrameEntry {
    sem::Symbol *sym = nullptr; /* null for a temporary */
    std::string name;
    std::string kind;         /* param / local / temp */
    sem::TypePtr type;
    long long width = 0;
    long long offset = 0;
};

struct Function {
    sem::SymbolPtr sym;
    std::string signature;    /* add(int, int) */
    std::string linkName;     /* _Z3addii */
    std::vector<Quad> quads;
    std::vector<sem::TypePtr> temps;       /* type of t1, t2, ... */
    std::vector<sem::SymbolPtr> owned;     /* synthetic symbols (`this`) */
    sem::Symbol *thisSym = nullptr;
    std::vector<FrameEntry> frame;
    long long frameWidth = 0;
    int firstIndex = 100;     /* number of quads[0] in the listing */
};

struct GlobalInit {
    long long offset = 0;
    Cls cls = Cls::Int;
    std::string value;        /* as printed: "5", "1.5", "&g", "\"text\"" */
    enum Kind { Integer, Floating, Address, String } kind = Integer;
    long long i = 0;          /* Integer */
    double f = 0;             /* Floating */
    sem::Symbol *target = nullptr; /* Address: &target */
    int str = -1;             /* String: index into Program::strings */
};

struct Global {
    sem::SymbolPtr sym;
    std::vector<GlobalInit> init; /* empty: zero-initialized (.bss) */
};

struct Program {
    std::vector<Function> functions;
    std::vector<Global> globals;           /* file-scope objects, static locals, static members */
    std::vector<std::string> strings;      /* string literals, as written in the source */
    std::vector<std::string> unsupported;  /* constructs the generator had to give up on */
};

/* a floating constant as the listing prints it: shortest text that reads back equal */
std::string floatText(double v);

/* a callee's source-level signature: `add(int, int)`, `Dog::bark(int)` */
std::string signatureOf(const sem::Symbol &fn);

void printProgram(const Program &p, std::ostream &out);
void printFunction(const Program &p, const Function &f, std::ostream &out);
/* one instruction without its number/label column: "t1 = a int+ b" */
std::string quadText(const Program &p, const Function &f, const Quad &q,
                     const std::vector<std::string> &labelOfIndex);

} // namespace tac

#endif
