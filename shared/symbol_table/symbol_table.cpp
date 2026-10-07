#include "symbol_table/symbol_table.hpp"

#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstdio>

#include "diagnostics/diagnostics.hpp"
#include "token/token_log.hpp"

/* =====================================================================
   PART 1 -- PARSE-TIME SYMBOL TABLE
   ===================================================================== */

std::vector<SymbolTableEntry> g_symbolTable;

static std::vector<std::unordered_map<std::string, std::vector<Symbol>>> g_scopes;
static std::vector<std::string> g_scopeLabels; /* parallel to g_scopes */
static std::vector<std::unordered_map<std::string, bool>> g_typeNameScopes; /* parallel to g_scopes:
                                                       name -> "is a type here" */
static std::string g_pendingScopeLabel;
static std::string g_currentClassName;
static std::string g_currentAggregateKind;
static int g_aggregateMemberDepth = -1;
/* the enclosing aggregates' contexts, restored by leaveClass() */
struct ClassContext {
    std::string name, kind;
    int memberDepth;
};
static std::vector<ClassContext> g_classStack;
/* unnamed tag -> the first typedef that names it */
static std::unordered_map<std::string, std::string> g_anonymousTagNames;
/* tag -> the unnamed members (by tag) whose fields it can use directly */
static std::unordered_map<std::string, std::vector<std::string>> g_anonymousMembers;

void addTypeName(const std::string &name) {
    if (g_typeNameScopes.empty()) g_typeNameScopes.emplace_back();
    g_typeNameScopes.back()[name] = true;
}

void hideTypeName(const std::string &name) {
    if (g_typeNameScopes.empty()) return;
    for (const auto &scope : g_typeNameScopes) {
        if (scope.count(name)) { /* only matters if it is a type somewhere */
            g_typeNameScopes.back()[name] = false;
            return;
        }
    }
}

bool isTypeName(const std::string &name) {
    for (auto it = g_typeNameScopes.rbegin(); it != g_typeNameScopes.rend(); ++it) {
        auto found = it->find(name);
        if (found != it->end()) return found->second;
    }
    return false;
}

void pushScope(const std::string &label) {
    g_scopes.emplace_back();
    g_typeNameScopes.emplace_back();
    std::string useLabel = label;
    if (useLabel.empty()) {
        if (!g_pendingScopeLabel.empty()) {
            useLabel = g_pendingScopeLabel;
            g_pendingScopeLabel.clear();
        } else {
            useLabel = "block";
        }
    }
    g_scopeLabels.push_back(useLabel);
}

void popScope() {
    if (!g_scopes.empty()) g_scopes.pop_back();
    if (!g_typeNameScopes.empty()) g_typeNameScopes.pop_back();
    if (!g_scopeLabels.empty()) g_scopeLabels.pop_back();
}

void hintScope(const std::string &label) { g_pendingScopeLabel = label; }

std::string currentScopePath() {
    std::string path;
    for (size_t i = 0; i < g_scopeLabels.size(); ++i) {
        if (i) path += " > ";
        path += g_scopeLabels[i];
    }
    return path;
}

static std::string functionPrefixOf(const std::string &path) {
    size_t pos = path.find("()");
    if (pos == std::string::npos) return path;
    return path.substr(0, pos + 2);
}

struct PendingReference {
    int tokenIdx;
    std::string name;
    std::string enclosingFunctionPrefix;
    bool isLabel;
};
static std::vector<PendingReference> g_pendingReferences;

void queuePendingReference(int tokenIdx, const std::string &name, bool isLabel) {
    g_pendingReferences.push_back({tokenIdx, name, functionPrefixOf(currentScopePath()), isLabel});
}

void resolvePendingReferences() {
    for (const auto &ref : g_pendingReferences) {
        for (const auto &e : g_symbolTable) {
            if (e.name != ref.name) continue;
            if (ref.isLabel) {
                if (e.kind != SymKind::LABEL) continue;
                if (functionPrefixOf(e.scopePath) != ref.enclosingFunctionPrefix) continue;
                setCategory(ref.tokenIdx, "LABEL");
            } else {
                if (e.scopePath != "global") continue; /* only global declarations are
                                                            legitimately forward-referenceable */
                setCategory(ref.tokenIdx, e.typeStr);
            }
            break;
        }
    }
}

const SymbolTableEntry *findMember(const std::string &tagName, const std::string &memberName) {
    if (tagName.empty()) return nullptr;
    std::string wanted = tagName + "::" + memberName;
    for (const auto &e : g_symbolTable) {
        if (e.qualifiedName == wanted) return &e;
    }
    /* `s.i` where `i` belongs to an unnamed struct inside s */
    auto anon = g_anonymousMembers.find(tagName);
    if (anon != g_anonymousMembers.end()) {
        for (const auto &inner : anon->second) {
            if (const SymbolTableEntry *e = findMember(inner, memberName)) return e;
        }
    }
    return nullptr;
}

void enterClass(const std::string &className, const std::string &kind) {
    g_classStack.push_back({g_currentClassName, g_currentAggregateKind, g_aggregateMemberDepth});
    g_currentClassName = className;
    g_currentAggregateKind = kind;
    g_aggregateMemberDepth = -1;
}
void leaveClass() {
    if (g_classStack.empty()) {
        g_currentClassName.clear();
        g_currentAggregateKind.clear();
        g_aggregateMemberDepth = -1;
        return;
    }
    g_currentClassName = g_classStack.back().name;
    g_currentAggregateKind = g_classStack.back().kind;
    g_aggregateMemberDepth = g_classStack.back().memberDepth;
    g_classStack.pop_back();
}
bool atAggregateMemberLevel() {
    return g_aggregateMemberDepth >= 0 && static_cast<int>(g_scopes.size()) == g_aggregateMemberDepth;
}
void nameAnonymousTag(const std::string &tag, const std::string &typedefName) {
    g_anonymousTagNames.emplace(tag, typedefName); /* the first one wins */
}
std::string anonymousTagName(const std::string &tag) {
    auto it = g_anonymousTagNames.find(tag);
    return it == g_anonymousTagNames.end() ? "" : it->second;
}
void addAnonymousMember(const std::string &outerTag, const std::string &anonTag) {
    g_anonymousMembers[outerTag].push_back(anonTag);
}
std::string currentClassName() { return g_currentClassName; }
std::string currentAggregateKind() { return g_currentAggregateKind; }
void markAggregateMemberDepth() { g_aggregateMemberDepth = static_cast<int>(g_scopes.size()); }

void declareSymbol(const std::string &name, SymKind kind, const std::string &typeStr,
                    const SymbolDeclInfo &extra) {
    if (g_scopes.empty()) g_scopes.emplace_back(); /* safety net: global scope */

    SymbolTableEntry e;
    e.name = name;
    e.qualifiedName = g_currentClassName.empty() ? name : (g_currentClassName + "::" + name);
    e.kind = kind;
    e.typeStr = typeStr;
    e.mangledName = extra.mangledName;
    e.scopeDepth = static_cast<int>(g_scopes.size());
    e.scopePath = currentScopePath();
    e.ownerAggregateKind = (static_cast<int>(g_scopes.size()) == g_aggregateMemberDepth)
                                ? currentAggregateKind()
                                : "";
    e.declLine = (extra.tokenIdx >= 0 && extra.tokenIdx < static_cast<int>(g_tokens.size()))
                     ? g_tokens[extra.tokenIdx].line
                     : g_currentLine;
    e.isStatic = extra.isStatic;
    e.isConst = extra.isConst;
    e.isVolatile = extra.isVolatile;
    e.pointerLevel = extra.pointerLevel;
    e.arrayLevel = extra.arrayLevel;
    e.returnType = extra.returnType;
    e.paramTypes = extra.paramTypes;
    e.useCount = 0;
    g_symbolTable.push_back(std::move(e));

    int flatIndex = static_cast<int>(g_symbolTable.size()) - 1;
    g_scopes.back()[name].push_back(Symbol{kind, typeStr, extra.mangledName, extra.aggregateTagName, flatIndex, extra.typeExpr});
}

const Symbol *lookupSymbol(const std::string &name) {
    for (auto it = g_scopes.rbegin(); it != g_scopes.rend(); ++it) {
        auto found = it->find(name);
        if (found != it->end() && !found->second.empty()) return &found->second.back();
    }
    return nullptr;
}

const Symbol *lookupTypeSymbol(const std::string &name) {
    for (auto it = g_scopes.rbegin(); it != g_scopes.rend(); ++it) {
        auto found = it->find(name);
        if (found == it->end()) continue;
        for (auto s = found->second.rbegin(); s != found->second.rend(); ++s) {
            switch (s->kind) {
                case SymKind::TYPEDEF_NAME: case SymKind::STRUCT_TAG: case SymKind::CLASS_TAG:
                    return &*s;
                default:
                    break;
            }
        }
    }
    return nullptr;
}

bool isOverloaded(const std::string &name) {
    for (auto it = g_scopes.rbegin(); it != g_scopes.rend(); ++it) {
        auto found = it->find(name);
        if (found == it->end()) continue;
        int count = 0;
        for (const auto &sym : found->second) {
            if (sym.kind == SymKind::PROCEDURE) ++count;
        }
        return count > 1; /* shadowing: only the innermost scope where this
                              name exists at all is what matters */
    }
    return false;
}

std::string inferExprType(const ASTNodePtr &node) {
    if (!node) return "";
    switch (node->kind) {
        case ASTKind::IntLiteral: return "INT";
        case ASTKind::FloatLiteral: return "FLOAT";
        case ASTKind::CharLiteral: return "CHAR";
        case ASTKind::StringLiteral: return "CHAR_POINTER";
        case ASTKind::BoolLiteral: return "BOOL";
        case ASTKind::Identifier: {
            const Symbol *s = lookupSymbol(node->label);
            return s ? s->typeStr : "";
        }
        default: return ""; 
    }
}

const Symbol *lookupOverload(const std::string &name, const std::vector<std::string> &argTypes) {
    for (auto it = g_scopes.rbegin(); it != g_scopes.rend(); ++it) {
        auto found = it->find(name);
        if (found == it->end() || found->second.empty()) continue;

        for (const auto &sym : found->second) {
            if (sym.kind != SymKind::PROCEDURE) continue;
            if (sym.flatIndex < 0 || sym.flatIndex >= static_cast<int>(g_symbolTable.size())) continue;
            const auto &entry = g_symbolTable[sym.flatIndex];
            if (entry.paramTypes.size() != argTypes.size()) continue;
            bool match = true;
            for (size_t i = 0; i < argTypes.size(); ++i) {
                if (entry.paramTypes[i] != argTypes[i]) { match = false; break; }
            }
            if (match) return &sym;
        }
        return &found->second.back(); 
    }
    return nullptr;
}

void recordUsage(const std::string &name) {
    recordUsage(lookupSymbol(name));
}

void recordUsage(const Symbol *s) {
    if (s && s->flatIndex >= 0 && s->flatIndex < static_cast<int>(g_symbolTable.size())) {
        g_symbolTable[s->flatIndex].useCount++;
    }
}

std::string categoryForTypeName(const Symbol *s) {
    if (!s) return "TYPEDEF";
    switch (s->kind) {
        case SymKind::TYPEDEF_NAME: return "TYPEDEF";
        default: return s->typeStr; /* CLASS / STRUCT tags */
    }
}

std::string symKindName(SymKind k) {
    switch (k) {
        case SymKind::VARIABLE: return "variable";
        case SymKind::PROCEDURE: return "procedure";
        case SymKind::PARAMETER: return "parameter";
        case SymKind::STRUCT_TAG: return "struct_tag";
        case SymKind::CLASS_TAG: return "class_tag";
        case SymKind::TYPEDEF_NAME: return "typedef";
        case SymKind::LABEL: return "label";
    }
    return "?";
}
/* ---- Itanium C++ ABI mangling (see the header) ---- */
namespace {

using sem::TypeKind;
using sem::TypePtr;

/* <len><name>, or for `operator+` etc. the Itanium two-letter code */
std::string sourceName(const std::string &name) {
    static const std::unordered_map<std::string, std::string> ops = {
        {"+", "pl"}, {"-", "mi"}, {"*", "ml"}, {"/", "dv"}, {"%", "rm"}, {"^", "eo"}, {"&", "an"},
        {"|", "or"}, {"~", "co"}, {"!", "nt"}, {"=", "aS"}, {"<", "lt"}, {">", "gt"}, {"==", "eq"},
        {"!=", "ne"}, {"<=", "le"}, {">=", "ge"}, {"&&", "aa"}, {"||", "oo"}, {"<<", "ls"}, {">>", "rs"},
        {"++", "pp"}, {"--", "mm"}, {"+=", "pL"}, {"-=", "mI"}, {"*=", "mL"}, {"/=", "dV"}, {"%=", "rM"},
        {"&=", "aN"}, {"|=", "oR"}, {"^=", "eO"}, {"<<=", "lS"}, {">>=", "rS"}, {"[]", "ix"}, {"()", "cl"},
        {"->", "pt"}, {",", "cm"}};
    if (name.compare(0, 8, "operator") == 0) {
        auto it = ops.find(name.substr(8));
        if (it != ops.end()) return it->second;
    }
    return std::to_string(name.size()) + name;
}

/* builtin types: never substitution candidates */
std::string builtinCode(const sem::Type &t) {
    switch (t.kind) {
        case TypeKind::Void: return "v";
        case TypeKind::Bool: return "b";
        case TypeKind::Char: return t.isUnsigned ? "h" : "c";
        case TypeKind::Short: return t.isUnsigned ? "t" : "s";
        case TypeKind::Int: return t.isUnsigned ? "j" : "i";
        case TypeKind::Long: return t.isUnsigned ? "m" : "l";
        case TypeKind::LongLong: return t.isUnsigned ? "y" : "x";
        case TypeKind::Float: return "f";
        case TypeKind::Double: return "d";
        default: return "";
    }
}

class Mangler {
  public:
    /* the enclosing class of a member: the first substitution candidate */
    std::string nestedPrefix(const std::string &cls) {
        std::string e = sourceName(cls);
        subs_.push_back(e);
        return e;
    }

    /* a type, using substitutions for components seen before */
    std::string type(const TypePtr &tIn) {
        TypePtr t = normalize(tIn);
        std::string plain = canonical(t);
        if (!(t->isConst || t->isVolatile) && !builtinCode(*t).empty()) return plain;
        for (size_t i = 0; i < subs_.size(); ++i) {
            if (subs_[i] == plain) return seqId(i);
        }
        std::string out;
        if (t->isConst || t->isVolatile) {
            out = cvCode(*t) + type(sem::unqualified(t));
        } else {
            switch (t->kind) {
                case TypeKind::Pointer: out = "P" + type(t->elem); break;
                case TypeKind::Reference: out = "R" + type(t->elem); break;
                case TypeKind::Array: out = arrayCode(*t) + type(t->elem); break;
                case TypeKind::Function: {
                    out = "F" + type(t->ret);
                    out += paramList(t->params, t->variadic);
                    out += "E";
                    break;
                }
                default: out = plain; break; /* record, va_list */
            }
        }
        subs_.push_back(plain);
        return out;
    }

    std::string paramList(const std::vector<TypePtr> &params, bool variadic) {
        if (params.empty() && !variadic) return "v";
        std::string out;
        for (const auto &p : params) out += type(p ? sem::unqualified(p) : sem::errorType()); /* top-level cv is not part of the signature */
        if (variadic) out += "z";
        return out;
    }

  private:
    std::vector<std::string> subs_; /* expansions, in order of first appearance */

    static std::string seqId(size_t i) {
        if (i == 0) return "S_";
        size_t n = i - 1;
        std::string digits;
        do {
            int d = static_cast<int>(n % 36);
            digits.insert(digits.begin(), static_cast<char>(d < 10 ? '0' + d : 'A' + d - 10));
            n /= 36;
        } while (n);
        return "S" + digits + "_";
    }
    static std::string cvCode(const sem::Type &t) { return std::string(t.isVolatile ? "V" : "") + (t.isConst ? "K" : ""); }
    static std::string arrayCode(const sem::Type &t) {
        return "A" + (t.arraySize >= 0 ? std::to_string(t.arraySize) : std::string()) + "_";
    }
    static std::string typeName(const std::string &tag, const std::string &typedefName) {
        if (!isAnonymousTag(tag)) return sourceName(tag);
        return typedefName.empty() ? "Ut_" : sourceName(typedefName);
    }
    /* va_list is `void *` on MIPS o32 */
    static TypePtr normalize(const TypePtr &t) {
        if (!t) return sem::errorType();
        if (t->kind == TypeKind::Opaque && t->name == "va_list")
            return sem::qualified(sem::pointerTo(sem::voidType()), t->isConst, t->isVolatile);
        return t;
    }
    /* the full encoding without substitutions: the identity of a component */
    static std::string canonical(const TypePtr &tIn) {
        TypePtr t = normalize(tIn);
        if (t->isConst || t->isVolatile) return cvCode(*t) + canonical(sem::unqualified(t));
        std::string b = builtinCode(*t);
        if (!b.empty()) return b;
        switch (t->kind) {
            case TypeKind::Pointer: return "P" + canonical(t->elem);
            case TypeKind::Reference: return "R" + canonical(t->elem);
            case TypeKind::Array: return arrayCode(*t) + canonical(t->elem);
            case TypeKind::Function: {
                std::string out = "F" + canonical(t->ret);
                if (t->params.empty() && !t->variadic) out += "v";
                for (const auto &p : t->params) out += canonical(sem::unqualified(p));
                if (t->variadic) out += "z";
                return out + "E";
            }
            /* an unnamed type is known by its first typedef name (C++
               [dcl.typedef]/9); one with none has no linkage: Ut_ */
            case TypeKind::Record: return t->record ? typeName(t->record->tag, t->record->typedefName) : "Ut_";
            case TypeKind::Opaque: return sourceName(t->name);
            default: return "u5error"; /* a vendor-extended type: only after an error */
        }
    }
};

} // namespace

std::string mangle(const std::string &name, const std::vector<sem::TypePtr> &params, bool variadic,
                   const std::string &className) {
    if (name == "main" && className.empty()) return "main";
    Mangler m;
    std::string out = "_Z";
    if (!className.empty()) {
        out += "N" + m.nestedPrefix(className);
        if (name == className) out += "C1";
        else if (name == "~" + className) out += "D1";
        else out += sourceName(name);
        out += "E";
    } else {
        out += sourceName(name);
    }
    return out + m.paramList(params, variadic);
}

std::string mangle(const std::string &name, const std::vector<ASTTypeExprPtr> &params, bool variadic,
                   const std::string &className) {
    std::vector<sem::TypePtr> types;
    /* `f(void)` has no parameters */
    bool voidList = params.size() == 1 && params[0] && params[0]->specParts.size() == 1 &&
                    params[0]->specParts[0] == "VOID" && params[0]->typedefName.empty() &&
                    params[0]->pointerLevel == 0 && params[0]->arrayDims.empty() &&
                    !params[0]->isFunction;
    if (!voidList) {
        for (const auto &p : params) types.push_back(p ? parseTimeType(*p, true) : sem::errorType());
    }
    return mangle(name, types, variadic, className);
}

/* mirrors the semantic phase's resolveType()/resolveSpecifiers() minus
   the checks; tags become stub records (mangling only needs the name) */
static sem::TypePtr parseTimeSpecifiers(const ASTTypeExpr &te, int depth) {
    using namespace sem;
    TypePtr base;
    if (!te.typedefName.empty()) {
        const ::Symbol *s = lookupTypeSymbol(te.typedefName);
        if (s && s->kind == SymKind::TYPEDEF_NAME && s->typeExpr && depth < 64) {
            /* the alias's own declarator applies too: typedef int *IntPtr */
            ASTTypeExpr alias = *s->typeExpr;
            alias.isStatic = alias.isTypedef = false;
            base = parseTimeType(alias, false);
        } else {
            auto r = std::make_shared<RecordInfo>();
            r->tag = te.typedefName;
            base = recordType(r);
        }
        return qualified(base, te.isConst, te.isVolatile);
    }
    std::map<std::string, int> n;
    for (const auto &p : te.specParts) n[p]++;
    auto c = [&](const char *k) { return n.count(k) ? n[k] : 0; };
    if (c("STRUCT") || c("CLASS")) {
        auto r = std::make_shared<RecordInfo>();
        r->tag = te.tagName;
        r->typedefName = anonymousTagName(te.tagName);
        base = recordType(r);
    } else if (c("VOID")) base = voidType();
    else if (c("BOOL")) base = boolType();
    else if (c("VA_LIST")) base = opaqueType("va_list");
    else if (c("FLOAT")) base = basicType(TypeKind::Float);
    else if (c("DOUBLE")) base = doubleType();
    else if (c("CHAR")) base = basicType(TypeKind::Char, c("UNSIGNED") > 0);
    else if (c("SHORT")) base = basicType(TypeKind::Short, c("UNSIGNED") > 0);
    else if (c("LONG")) base = basicType(c("LONG") == 2 ? TypeKind::LongLong : TypeKind::Long, c("UNSIGNED") > 0);
    else base = basicType(TypeKind::Int, c("UNSIGNED") > 0);
    return qualified(base, te.isConst, te.isVolatile);
}

static int parseTimeTypedefDepth = 0;

sem::TypePtr parseTimeType(const ASTTypeExpr &te, bool isParam) {
    using namespace sem;
    ++parseTimeTypedefDepth;
    TypePtr base = parseTimeSpecifiers(te, parseTimeTypedefDepth);
    --parseTimeTypedefDepth;

    std::string outerOps = te.ptrOps, innerOps = te.innerPtrOps;
    if (outerOps.empty() && innerOps.empty() && te.pointerLevel > 0) {
        outerOps = te.isReference ? "&" + std::string(te.pointerLevel - 1, '*') : std::string(te.pointerLevel, '*');
    }
    size_t innerDims = te.grouped ? std::min<size_t>(te.innerArrayCount, te.arrayDims.size()) : 0;
    auto wrapPointers = [](TypePtr t, const std::string &ops) {
        for (char op : ops) {
            if (op == 'c' || op == 'v') t = qualified(t, op == 'c', op == 'v');
            else t = op == '&' ? referenceTo(t) : pointerTo(t);
        }
        return t;
    };
    auto wrapArrays = [&](TypePtr t, size_t from, size_t to) {
        for (size_t i = to; i-- > from;) {
            const ASTNodePtr &d = te.arrayDims[i];
            long long size = -1;
            if (d && d->kind == ASTKind::IntLiteral) size = std::strtoll(d->label.c_str(), nullptr, 0);
            t = arrayOf(t, size);
        }
        return t;
    };
    std::vector<TypePtr> params;
    bool voidList = te.params.size() == 1 && te.params[0]->specParts.size() == 1 &&
                    te.params[0]->specParts[0] == "VOID" && te.params[0]->typedefName.empty() &&
                    te.params[0]->pointerLevel == 0 && te.params[0]->arrayDims.empty();
    if (!voidList) {
        for (const auto &p : te.params) params.push_back(parseTimeType(*p, true));
    }
    TypePtr t = wrapPointers(base, outerOps);
    if (te.isFunction) t = functionType(t, params, te.isVariadic);
    else t = wrapArrays(t, innerDims, te.arrayDims.size());
    if (te.grouped) {
        t = wrapPointers(t, innerOps);
        t = wrapArrays(t, 0, innerDims);
    }
    if (isParam && isArray(t)) t = pointerTo(t->elem);
    return t;
}

static std::string qualifiersFor(const SymbolTableEntry &e) {
    std::string q;
    if (e.isStatic) q += "static ";
    if (e.isConst) q += "const ";
    if (e.isVolatile) q += "volatile ";
    if (e.pointerLevel > 0) q += std::string(e.pointerLevel, '*') + " ";
    if (e.arrayLevel > 0) q += "[]" + std::string(e.arrayLevel > 1 ? std::to_string(e.arrayLevel) : "") + " ";
    if (!q.empty()) q.pop_back(); /* trailing space */
    return q;
}

static std::string signatureFor(const SymbolTableEntry &e) {
    if (e.kind != SymKind::PROCEDURE && e.returnType.empty()) return "";
    std::string sig = e.returnType.empty() ? "?" : e.returnType;
    sig += " (";
    for (size_t i = 0; i < e.paramTypes.size(); ++i) {
        if (i) sig += ", ";
        sig += e.paramTypes[i];
    }
    sig += ")";
    return sig;
}

static std::string kindLabelFor(const SymbolTableEntry &e) {
    std::string base = symKindName(e.kind);
    if (e.ownerAggregateKind.empty()) return base;
    if (e.kind == SymKind::VARIABLE) return e.ownerAggregateKind + "_member";
    if (e.kind == SymKind::PROCEDURE) return e.ownerAggregateKind + "_method";
    return base;
}

void printSymbolTable(std::ostream &out) {
    out << "\n=== Symbol Table ===\n";
    char header[256];
    snprintf(header, sizeof(header), "%-20s %-14s %-6s %-28s %-16s %-24s %-9s %-22s %s\n",
             "Name", "Kind", "Line", "Scope", "Type", "Qualifiers", "Uses", "Signature", "Mangled Name");
    out << header;
    snprintf(header, sizeof(header), "%-20s %-14s %-6s %-28s %-16s %-24s %-9s %-22s %s\n",
             "----", "----", "----", "-----", "----", "----------", "----", "---------", "------------");
    out << header;
    for (const auto &e : g_symbolTable) {
        char line[512];
        snprintf(line, sizeof(line), "%-20s %-14s %-6s %-28s %-16s %-24s %-9d %-22s %s\n",
                 e.qualifiedName.c_str(), kindLabelFor(e).c_str(), displayLine(e.declLine).c_str(),
                 e.scopePath.c_str(), e.typeStr.c_str(), qualifiersFor(e).c_str(),
                 e.useCount, signatureFor(e).c_str(), e.mangledName.c_str());
        out << line;
    }
}

/* =====================================================================
   PART 2 -- SEMANTIC SYMBOL TABLE
   ===================================================================== */

namespace sem {

SymbolTable::SymbolTable() {
    Scope g;
    g.id = 0;
    g.kind = ScopeKind::Global;
    g.label = "global";
    scopes_.push_back(g);
    stack_.push_back(0);
}

int SymbolTable::enterScope(ScopeKind kind, const std::string &label, RecordInfo *record,
                            Symbol *function) {
    Scope s;
    s.id = static_cast<int>(scopes_.size());
    s.parent = stack_.back();
    s.depth = static_cast<int>(stack_.size());
    s.kind = kind;
    s.label = label;
    s.record = record;
    s.function = function;
    scopes_.push_back(s);
    stack_.push_back(s.id);
    return s.id;
}

void SymbolTable::exitScope() {
    if (stack_.size() > 1) stack_.pop_back();
}

void SymbolTable::reenterScope(int id) {
    if (id >= 0 && id < static_cast<int>(scopes_.size())) stack_.push_back(id);
}

Scope &SymbolTable::current() { return scopes_[stack_.back()]; }
Scope &SymbolTable::scope(int id) { return scopes_[id]; }

std::string SymbolTable::pathOf(int scopeId) const {
    std::vector<std::string> parts;
    for (int id = scopeId; id >= 0; id = scopes_[id].parent) parts.push_back(scopes_[id].label);
    std::string path;
    for (auto it = parts.rbegin(); it != parts.rend(); ++it) {
        if (!path.empty()) path += " > ";
        path += *it;
    }
    return path;
}

void SymbolTable::assignNames(int scopeId, const SymbolPtr &s) {
    s->scopeId = scopeId;
    s->scopePath = pathOf(scopeId);
    if (!s->uniqueName.empty()) return;
    bool fileLevel = scopes_[scopeId].kind == ScopeKind::Global;
    switch (s->kind) {
        case SymbolKind::Variable:
        case SymbolKind::Parameter:
            s->uniqueName = fileLevel ? s->name : s->name + "." + std::to_string(++nextUnique_);
            break;
        case SymbolKind::Field:
            s->uniqueName = (s->ownerRecord ? s->ownerRecord->tag + "::" : "") + s->name;
            break;
        case SymbolKind::Function:
            s->uniqueName = s->mangledName.empty() ? s->name : s->mangledName;
            break;
        default:
            s->uniqueName = s->name;
            break;
    }
}

void SymbolTable::declare(const SymbolPtr &s) { declareIn(stack_.back(), s); }

void SymbolTable::declareIn(int scopeId, const SymbolPtr &s) {
    assignNames(scopeId, s);
    scopes_[scopeId].names[s->name].push_back(s);
    scopes_[scopeId].ordered.push_back(s);
    all_.push_back(s);
}

void SymbolTable::declareHidden(int scopeId, const SymbolPtr &s) {
    assignNames(scopeId, s);
    scopes_[scopeId].ordered.push_back(s);
    all_.push_back(s);
}

void SymbolTable::declareTag(const SymbolPtr &s) { declareTagIn(stack_.back(), s); }

void SymbolTable::declareTagIn(int scopeId, const SymbolPtr &s) {
    assignNames(scopeId, s);
    scopes_[scopeId].tags[s->name] = s;
    scopes_[scopeId].ordered.push_back(s);
    all_.push_back(s);
}

std::vector<SymbolPtr> SymbolTable::lookupLocal(const std::string &name) const {
    const Scope &s = scopes_[stack_.back()];
    auto it = s.names.find(name);
    return it == s.names.end() ? std::vector<SymbolPtr>{} : it->second;
}

SymbolPtr SymbolTable::lookupTagLocal(const std::string &name) const {
    const Scope &s = scopes_[stack_.back()];
    auto it = s.tags.find(name);
    return it == s.tags.end() ? nullptr : it->second;
}

Lookup SymbolTable::lookup(const std::string &name) const {
    Lookup out;
    for (auto it = stack_.rbegin(); it != stack_.rend(); ++it) {
        const Scope &s = scopes_[*it];
        if (s.kind == ScopeKind::Record) {
            MemberLookup ml = lookupMember(s.record, name);
            if (!ml.symbols.empty()) {
                out.symbols = ml.symbols;
                out.scopeId = s.id;
                out.viaRecord = true;
                out.member = ml;
                return out;
            }
            continue;
        }
        auto f = s.names.find(name);
        if (f != s.names.end() && !f->second.empty()) {
            out.symbols = f->second;
            out.scopeId = s.id;
            return out;
        }
    }
    return out;
}

SymbolPtr SymbolTable::lookupTag(const std::string &name) const {
    for (auto it = stack_.rbegin(); it != stack_.rend(); ++it) {
        const Scope &s = scopes_[*it];
        auto f = s.tags.find(name);
        if (f != s.tags.end()) return f->second;
    }
    return nullptr;
}

std::vector<int> SymbolTable::saveAndResetToGlobal() {
    std::vector<int> saved = stack_;
    stack_.assign(1, 0);
    return saved;
}

void SymbolTable::restoreStack(const std::vector<int> &saved) { stack_ = saved; }

std::string symbolKindName(SymbolKind k) {
    switch (k) {
        case SymbolKind::Variable: return "variable";
        case SymbolKind::Parameter: return "parameter";
        case SymbolKind::Function: return "function";
        case SymbolKind::Field: return "field";
        case SymbolKind::Typedef: return "typedef";
        case SymbolKind::Label: return "label";
        case SymbolKind::Tag: return "tag";
    }
    return "?";
}

std::string storageName(Storage s) {
    switch (s) {
        case Storage::None: return "-";
        case Storage::Global: return "global";
        case Storage::Static: return "static";
        case Storage::Local: return "local";
        case Storage::Param: return "param";
        case Storage::Member: return "member";
    }
    return "?";
}

/* ---------------- printers ---------------- */

static std::string kindLabel(const Symbol &s) {
    if (s.kind == SymbolKind::Tag) {
        return s.record ? recordKindName(s.record->kind) + "_tag" : "tag";
    }
    if (s.kind == SymbolKind::Function) {
        if (s.isConstructor) return "constructor";
        if (s.isDestructor) return "destructor";
        if (s.isMethod) return "method";
    }
    return symbolKindName(s.kind);
}

static std::string typeLabel(const Symbol &s) {
    if (s.kind == SymbolKind::Tag) {
        if (s.record) return recordKindName(s.record->kind) + " " + s.name + (s.record->complete ? "" : " (incomplete)");
    }
    if (s.kind == SymbolKind::Label) return "-";
    return s.type ? typeToString(s.type) : "-";
}

static std::string notes(const Symbol &s) {
    std::string n;
    auto add = [&](const std::string &x) { n += (n.empty() ? "" : ", ") + x; };
    if (s.ownerRecord) add(accessName(s.access));
    if (s.isStatic) add("static");
    if (s.kind == SymbolKind::Function && !s.isConstructor && !s.isDestructor) add(s.isDefined ? "defined" : "declared only");
    if (s.isConstant) add("value " + std::to_string(s.constValue));
    if (s.kind == SymbolKind::Variable && s.storage == Storage::Global && !s.isDefined) add("extern, not defined here");
    if (s.isRegister) add("register");
    if (s.offset >= 0) add("offset " + std::to_string(s.offset));
    if (s.kind == SymbolKind::Tag && s.record && s.record->complete) {
        add("size " + std::to_string(s.record->size));
        for (const auto &b : s.record->bases) add(accessName(b.access) + " base " + b.record->tag);
    }
    return n;
}

void printSemanticSymbolTable(const SymbolTable &st, std::ostream &out) {
    char line[1024];
    /* Unique Name: what TAC calls the symbol; Mangled Name: a function's
       link name (Itanium C++ ABI), "-" for everything else */
    snprintf(line, sizeof(line), "%-18s %-14s %-26s %-8s %-30s %-5s %-5s %-5s %-20s %-24s %s\n", "Name", "Kind",
             "Type", "Storage", "Scope", "Line", "Size", "Uses", "Unique Name", "Mangled Name", "Notes");
    out << line;
    snprintf(line, sizeof(line), "%-18s %-14s %-26s %-8s %-30s %-5s %-5s %-5s %-20s %-24s %s\n", "----", "----",
             "----", "-------", "-----", "----", "----", "----", "-----------", "------------", "-----");
    out << line;
    for (const auto &sp : st.allSymbols()) {
        const Symbol &s = *sp;
        long long size = (s.kind == SymbolKind::Variable || s.kind == SymbolKind::Parameter || s.kind == SymbolKind::Field)
                             ? sizeOf(s.type)
                             : -1;
        std::string name = s.name.empty() ? "(unnamed)" : (s.ownerRecord ? s.ownerRecord->tag + "::" + s.name : s.name);
        snprintf(line, sizeof(line), "%-18s %-14s %-26s %-8s %-30s %-5s %-5s %-5d %-20s %-24s %s\n", name.c_str(),
                 kindLabel(s).c_str(), typeLabel(s).c_str(), storageName(s.storage).c_str(), s.scopePath.c_str(),
                 displayLine(s.line).c_str(), size >= 0 ? std::to_string(size).c_str() : "-", s.useCount,
                 s.uniqueName.c_str(), s.mangledName.empty() ? "-" : s.mangledName.c_str(), notes(s).c_str());
        out << line;
    }
}

void printRecordLayouts(const SymbolTable &st, std::ostream &out) {
    bool any = false;
    for (const auto &sp : st.allSymbols()) {
        if (sp->kind != SymbolKind::Tag || !sp->record || !sp->record->complete) continue;
        const RecordInfo &r = *sp->record;
        any = true;
        out << recordKindName(r.kind) << " " << r.tag << ": size " << r.size << ", align " << r.align << "\n";
        for (const auto &b : r.bases) out << "    (base " << b.record->tag << ", " << accessName(b.access) << ")\n";
        for (const auto &f : r.fields) {
            out << "    " << (f->storage == Storage::Member ? "+" + std::to_string(f->offset) : std::string("static"))
                << "  " << typeToString(f->type) << " " << f->name << "  [" << accessName(f->access) << "]\n";
        }
        for (const auto &p : r.promoted) { /* fields of unnamed members, usable directly */
            out << "    +" << p->offset << "  " << typeToString(p->type) << " " << p->name << "  ["
                << accessName(p->access) << "]  (from the unnamed member)\n";
        }
    }
    if (!any) out << "(no records)\n";
}

} // namespace sem
