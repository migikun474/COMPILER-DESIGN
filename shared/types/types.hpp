#ifndef SHARED_TYPES_HPP
#define SHARED_TYPES_HPP

/* =====================================================================
   STRUCTURAL TYPE SYSTEM
   ---------------------------------------------------------------------
   A type is a small immutable graph of type constructors over basic
   types (Dragon Book 6.3.1): pointer(t), reference(t), array(n, t),
   function(params -> ret), plus named record types. Pointer
   depth is therefore structural -- `int **` is Pointer(Pointer(Int)) --
   never a counter. Qualifiers (const/volatile) live on the level they
   qualify, so `const int *p` is Pointer(const Int): *p is read-only, p
   is not.

   Equivalence is structural for the constructors and *by name* for
   records (C's rule): two struct types are the same type iff they share
   the same RecordInfo, which is what the tag in scope resolves to.

   A Function type only ever describes a declared function: the language
   has no function pointers, so Pointer(Function) is never built and a
   function name is not a value.

   Sizes follow the MIPS32 (ILP32) target, so later phases can lay out
   frames and records straight from these numbers.
   ===================================================================== */

#include <map>
#include <memory>
#include <string>
#include <vector>

namespace sem {

struct Type;
using TypePtr = std::shared_ptr<const Type>;
struct Symbol;
using SymbolPtr = std::shared_ptr<Symbol>;
struct RecordInfo;

enum class TypeKind {
    Error,     /* result of an expression that already produced an error;
                  accepted silently everywhere to avoid cascades */
    Void, Bool, Char, Short, Int, Long, LongLong, Float, Double,
    Pointer, Reference, Array, Function,
    Record,    /* struct / class */
    Opaque     /* va_list */
};

/* NoAccess = "not accessible at all from here", e.g. a base class's
   private member seen through a derived class */
enum class Access { Public, Protected, Private, NoAccess };
enum class RecordKind { Struct, Class };

struct Type {
    TypeKind kind = TypeKind::Error;
    bool isConst = false;
    bool isVolatile = false;
    bool isUnsigned = false;     /* integer kinds only */

    TypePtr elem;                /* Pointer/Reference: target; Array: element */
    long long arraySize = -1;    /* Array: element count, -1 for `[]` */

    TypePtr ret;                 /* Function */
    std::vector<TypePtr> params;
    bool variadic = false;

    std::shared_ptr<RecordInfo> record; /* Record */
    std::string name;            /* Opaque: "va_list" */
};

struct BaseClass {
    std::shared_ptr<RecordInfo> record;
    Access access = Access::Public;
};

struct RecordInfo : std::enable_shared_from_this<RecordInfo> {
    RecordKind kind = RecordKind::Struct;
    std::string tag;             /* "(unnamed at L:C)" for an unnamed type, see ast.hpp */
    std::string typedefName;     /* unnamed type: the first typedef naming it
                                    (`typedef struct {...} Pt;`), used in messages
                                    and as its link name, as in C++ */
    bool complete = false;       /* closing '}' seen */
    int declLine = 0;

    std::vector<SymbolPtr> fields;                         /* data members, declaration order */
    std::map<std::string, std::vector<SymbolPtr>> members; /* name -> field, or method overloads */
    std::vector<SymbolPtr> constructors;
    SymbolPtr destructor;
    std::vector<BaseClass> bases;

    /* members of unnamed members (`struct S { struct { int i; float f; }; }`),
       usable as s.i: one entry per promoted name, a copy of the inner
       field with its offset from the start of *this* record. They are in
       `members` too (so lookup finds them) but not in `fields`. */
    std::vector<SymbolPtr> promoted;

    long long size = 0;          /* MIPS32 layout, valid once complete */
    int align = 1;
    int scopeId = -1;            /* scope holding the members (see SymbolTable) */
};

/* ---------------- construction ---------------- */
TypePtr errorType();
TypePtr voidType();
TypePtr boolType();
TypePtr charType();
TypePtr intType();
TypePtr unsignedIntType();
TypePtr doubleType();
TypePtr basicType(TypeKind k, bool isUnsigned = false);
TypePtr pointerTo(const TypePtr &t);
TypePtr referenceTo(const TypePtr &t);
TypePtr arrayOf(const TypePtr &elem, long long size);
TypePtr functionType(const TypePtr &ret, const std::vector<TypePtr> &params, bool variadic);
TypePtr recordType(const std::shared_ptr<RecordInfo> &r);
TypePtr opaqueType(const std::string &name);
TypePtr qualified(const TypePtr &t, bool isConst, bool isVolatile); /* adds to existing */
TypePtr unqualified(const TypePtr &t);

/* ---------------- classification ---------------- */
bool isError(const TypePtr &t);
bool isVoid(const TypePtr &t);
bool isBool(const TypePtr &t);
bool isIntegral(const TypePtr &t);   /* bool, char, short, int, long, long long */
bool isFloating(const TypePtr &t);
bool isArithmetic(const TypePtr &t);
bool isPointer(const TypePtr &t);
bool isReference(const TypePtr &t);
bool isArray(const TypePtr &t);
bool isFunction(const TypePtr &t);
bool isRecord(const TypePtr &t);
bool isScalar(const TypePtr &t);     /* arithmetic or pointer: usable as a condition */
bool isVoidPointer(const TypePtr &t);
/* has a known size: not void, not an incomplete record, not `[]`, not
   a function */
bool isComplete(const TypePtr &t);

/* ---------------- relations ---------------- */
/* structural equality; records by identity. Top-level qualifiers
   are ignored unless `exactQualifiers` (nested levels always compare
   qualifiers, so `const int *` != `int *`). */
bool sameType(const TypePtr &a, const TypePtr &b, bool exactQualifiers = false);
bool isDerivedFrom(const RecordInfo *derived, const RecordInfo *base);
/* same parameter types and `...` (what makes two declarations the same function) */
bool sameParameterLists(const TypePtr &a, const TypePtr &b);

/* the value a use of an expression of type t produces: arrays decay to
   a pointer to their first element, references to what they refer to;
   top-level qualifiers drop. A function type is returned unchanged (a
   function is not a value; the caller reports that). */
TypePtr decay(const TypePtr &t);
TypePtr integerPromotion(const TypePtr &t);
/* "usual arithmetic conversions": the common type both operands of an
   arithmetic operator are converted to (the max() of Dragon Fig 6.27) */
TypePtr usualArithmetic(const TypePtr &a, const TypePtr &b);

/* ---------------- integer constants in their own type ----------------
   A constant expression has a value *of its type* (Papaspyrou's val[tau]):
   `-1 < 0u` compares 4294967295u with 0u, `~0u` is 4294967295 and
   `2147483647 + 1` overflows int. Values are kept in a long long holding
   the type's bit pattern sign- or zero-extended (MIPS32 widths: char 8,
   short 16, int/long/pointer 32, long long 64), so a 64-bit unsigned
   value above LLONG_MAX is stored as its two's-complement pattern. */
int integerBits(const TypePtr &t);           /* 0 for a non-integer type */
bool isUnsignedInteger(const TypePtr &t);    /* unsigned kinds, bool, pointers */
long long wrapToType(long long v, const TypePtr &t);
/* is the mathematical value v representable in t? (v itself read as a
   value of `from`, so an unsigned 64-bit pattern is not negative) */
bool fitsInType(long long v, const TypePtr &from, const TypePtr &t);
std::string constantToString(long long v, const TypePtr &t);

/* How well a value of type `from` converts implicitly to `to`
   (assignment, initialization, argument passing, return). Ranks follow
   C++ overload resolution so the same function also orders overloads. */
enum class ConvRank { Exact = 0, Promotion = 1, Conversion = 2, Ellipsis = 3, None = 4 };
struct Conversion {
    ConvRank rank = ConvRank::None;
    std::string why; /* explanation when rank == None */
};
/* `from` must already be decayed. `fromIsNullConstant` marks an integer
   constant expression equal to 0, the only integer that converts to a
   pointer. */
Conversion implicitConversion(const TypePtr &from, const TypePtr &to, bool fromIsNullConstant);

/* explicit cast legality; returns "" if allowed, else the reason */
std::string checkCast(const TypePtr &from, const TypePtr &to);

/* ---------------- layout (MIPS32) ---------------- */
long long sizeOf(const TypePtr &t); /* -1 when incomplete */
int alignOf(const TypePtr &t);
void layoutRecord(RecordInfo &r);   /* assigns field offsets, size, align */

/* ---------------- printing ---------------- */
/* C spelling: "int", "char *", "int [10]", "struct Point", "int (int, int)" */
std::string typeToString(const TypePtr &t);
/* "struct Point", or for an unnamed type its typedef name ("Pt") or
   "struct (unnamed at 3:9)" */
std::string recordDisplayName(const RecordInfo &r);
std::string accessName(Access a);
std::string recordKindName(RecordKind k);

/* ---------------- member lookup ---------------- */
struct MemberLookup {
    std::vector<SymbolPtr> symbols;   /* the field, or all method overloads */
    RecordInfo *declaringRecord = nullptr;
    Access access = Access::Public;   /* effective access as a member of the
                                         record the lookup started from */
    bool ambiguous = false;           /* found in two unrelated bases */
};
/* finds `name` in `r` or, if absent there, in its bases (derived first) */
MemberLookup lookupMember(RecordInfo *r, const std::string &name);

} // namespace sem

#endif
