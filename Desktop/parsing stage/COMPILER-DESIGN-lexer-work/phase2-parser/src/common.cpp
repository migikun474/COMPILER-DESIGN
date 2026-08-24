#include "common.h"

#include <algorithm>
#include <cctype>

std::vector<TokenRecord> g_tokens;
std::vector<Diagnostic> g_diagnostics;
std::unordered_set<std::string> g_typedefNames;
std::vector<SymbolTableEntry> g_symbolTable;
ASTNodePtr g_astRoot;

int g_currentLine = 1;
std::string g_lastText;

static std::vector<std::unordered_map<std::string, Symbol>> g_scopes;
static std::string g_currentClassName;

int addTokenRecord(const std::string &lexeme, const std::string &category) {
    g_tokens.push_back({lexeme, category, g_currentLine});
    return static_cast<int>(g_tokens.size()) - 1;
}

void setCategory(int idx, const std::string &category) {
    if (idx >= 0 && idx < static_cast<int>(g_tokens.size())) {
        g_tokens[idx].category = category;
    }
}

void reportDiagnostic(int line, const std::string &near_text,
                       const std::string &message, const std::string &kind) {
    g_diagnostics.push_back({line, near_text, message, kind});
}

bool hasErrors() { return !g_diagnostics.empty(); }

void pushScope() { g_scopes.emplace_back(); }

void popScope() {
    if (!g_scopes.empty()) g_scopes.pop_back();
}

void enterClass(const std::string &className) { g_currentClassName = className; }
void leaveClass() { g_currentClassName.clear(); }
std::string currentClassName() { return g_currentClassName; }

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
    g_scopes.back()[name] = Symbol{kind, typeStr, extra.mangledName, flatIndex};
}

const Symbol *lookupSymbol(const std::string &name) {
    for (auto it = g_scopes.rbegin(); it != g_scopes.rend(); ++it) {
        auto found = it->find(name);
        if (found != it->end()) return &found->second;
    }
    return nullptr;
}

void recordUsage(const std::string &name) {
    const Symbol *s = lookupSymbol(name);
    if (s && s->flatIndex >= 0 && s->flatIndex < static_cast<int>(g_symbolTable.size())) {
        g_symbolTable[s->flatIndex].useCount++;
    }
}

std::string computeTypeStr(const TypeSpec &ts, int pointerLevel, int arrayLevel) {
    std::string base;
    if (ts.parts.empty()) {
        base = "INT"; /* implicit-int, mirrors classic C default */
    } else {
        for (size_t i = 0; i < ts.parts.size(); ++i) {
            if (i) base += "_";
            base += ts.parts[i];
        }
    }
    /* one "_POINTER" per level, so char* and char** are distinguishable
       (CHAR_POINTER vs CHAR_POINTER_POINTER) rather than collapsing to
       the same classification regardless of depth. */
    for (int i = 0; i < pointerLevel; ++i) base += "_POINTER";
    /* likewise one "_ARRAY" per dimension, so int[3] and int[2][2] are
       distinguishable. */
    for (int i = 0; i < arrayLevel; ++i) base += "_ARRAY";
    return base;
}

std::string categoryForTypeName(const Symbol *s) {
    if (!s) return "TYPEDEF";
    switch (s->kind) {
        case SymKind::TYPEDEF_NAME: return "TYPEDEF";
        default: return s->typeStr; /* CLASS / STRUCT / UNION / ENUM tags */
    }
}

std::string symKindName(SymKind k) {
    switch (k) {
        case SymKind::VARIABLE: return "variable";
        case SymKind::PROCEDURE: return "procedure";
        case SymKind::PARAMETER: return "parameter";
        case SymKind::STRUCT_TAG: return "struct_tag";
        case SymKind::UNION_TAG: return "union_tag";
        case SymKind::ENUM_TAG: return "enum_tag";
        case SymKind::CLASS_TAG: return "class_tag";
        case SymKind::TYPEDEF_NAME: return "typedef";
        case SymKind::ENUM_CONST: return "enum_constant";
        case SymKind::LABEL: return "label";
    }
    return "?";
}

/* ---------------------------------------------------------------------
   Name mangling (Itanium-inspired, not spec-compliant -- see common.h)
   --------------------------------------------------------------------- */
static std::string mangleOneType(const std::string &t) {
    std::string base = t;
    int ptr = 0, arr = 0;
    while (true) {
        if (base.size() > 8 && base.compare(base.size() - 8, 8, "_POINTER") == 0) {
            ptr++; base.resize(base.size() - 8); continue;
        }
        if (base.size() > 6 && base.compare(base.size() - 6, 6, "_ARRAY") == 0) {
            arr++; base.resize(base.size() - 6); continue;
        }
        break;
    }

    std::string code;
    if (base == "INT") code = "i";
    else if (base == "CHAR") code = "c";
    else if (base == "FLOAT") code = "f";
    else if (base == "DOUBLE") code = "d";
    else if (base == "BOOL") code = "b";
    else if (base == "VOID") code = "v";
    else if (base == "SHORT") code = "s";
    else if (base == "LONG") code = "l";
    else if (base == "STRUCT") code = "3Str";
    else if (base == "CLASS") code = "3Cls";
    else if (base == "UNION") code = "3Uni";
    else if (base == "ENUM") code = "3Enu";
    else code = std::to_string(base.size()) + base; /* fallback: length-prefixed raw name */

    for (int i = 0; i < arr; ++i) code = "A" + code;
    for (int i = 0; i < ptr; ++i) code = "P" + code;
    return code;
}

std::string mangle(const std::string &name, const std::vector<std::string> &paramTypes,
                    const std::string &className) {
    std::string out = "_Z";
    if (!className.empty()) {
        out += "N" + std::to_string(className.size()) + className;
        out += std::to_string(name.size()) + name;
        out += "E";
    } else {
        out += std::to_string(name.size()) + name;
    }
    if (paramTypes.empty()) {
        out += "v";
    } else {
        for (auto &t : paramTypes) out += mangleOneType(t);
    }
    return out;
}

ASTNodePtr registerDeclarator(DeclInfo &d, TypeSpec &ts) {
    if (d.nameIdx < 0) return nullptr; /* abstract declarator, nothing to register */

    if (ts.isTypedefStorage) {
        std::string typeStr = computeTypeStr(ts, d.pointerLevel, d.arrayLevel);
        SymbolDeclInfo extra;
        extra.tokenIdx = d.nameIdx;
        extra.pointerLevel = d.pointerLevel;
        extra.arrayLevel = d.arrayLevel;
        declareSymbol(d.name, SymKind::TYPEDEF_NAME, typeStr, extra);
        g_typedefNames.insert(d.name);
        setCategory(d.nameIdx, "TYPEDEF");
        return mkNode(ASTKind::TypedefDecl, d.name + " = " + typeStr);
    } else if (d.isFunctionPointer) {
        /* `int (*fp)(int, int);` -- fp is a VARIABLE whose type is
           "pointer to function returning X taking (...)", not a
           function declaration. d.pointerLevel counts the star(s)
           inside the parens, e.g. 1 for `(*fp)`, 2 for `(**fpp)`. */
        std::vector<std::string> paramTypes;
        for (auto &p : d.params) paramTypes.push_back(p.typeStr);
        std::string returnType = computeTypeStr(ts, d.pointerLevel - 1, 0);
        std::string typeStr = returnType + "_FUNCTION_POINTER";

        SymbolDeclInfo extra;
        extra.tokenIdx = d.nameIdx;
        extra.isStatic = ts.isStatic;
        extra.isConst = ts.isConst;
        extra.isVolatile = ts.isVolatile;
        extra.pointerLevel = d.pointerLevel;
        extra.returnType = returnType;
        extra.paramTypes = paramTypes;
        declareSymbol(d.name, SymKind::VARIABLE, typeStr, extra);
        setCategory(d.nameIdx, typeStr);
        return mkNode(ASTKind::VarDecl, d.name + " : " + typeStr);
    } else if (d.isFunction) {
        std::vector<std::string> paramTypes;
        for (auto &p : d.params) paramTypes.push_back(p.typeStr);
        std::string mangled = mangle(d.name, paramTypes, currentClassName());
        std::string returnType = computeTypeStr(ts, d.pointerLevel, d.arrayLevel);

        SymbolDeclInfo extra;
        extra.tokenIdx = d.nameIdx;
        extra.isStatic = ts.isStatic;
        extra.isConst = ts.isConst;
        extra.isVolatile = ts.isVolatile;
        extra.pointerLevel = d.pointerLevel;
        extra.arrayLevel = d.arrayLevel;
        extra.returnType = returnType;
        extra.paramTypes = paramTypes;
        extra.mangledName = mangled;
        declareSymbol(d.name, SymKind::PROCEDURE, "PROCEDURE", extra);
        setCategory(d.nameIdx, "PROCEDURE");

        auto node = mkNode(ASTKind::FunctionDecl, d.name + " : " + mangled);
        for (auto &p : d.params) {
            if (!p.name.empty()) addChild(node, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
        }
        return node;
    } else {
        std::string typeStr = computeTypeStr(ts, d.pointerLevel, d.arrayLevel);
        SymbolDeclInfo extra;
        extra.tokenIdx = d.nameIdx;
        extra.isStatic = ts.isStatic;
        extra.isConst = ts.isConst;
        extra.isVolatile = ts.isVolatile;
        extra.pointerLevel = d.pointerLevel;
        extra.arrayLevel = d.arrayLevel;
        declareSymbol(d.name, SymKind::VARIABLE, typeStr, extra);
        setCategory(d.nameIdx, typeStr);
        auto node = mkNode(ASTKind::VarDecl, d.name + " : " + typeStr);
        if (d.initExpr) addChild(node, d.initExpr);
        return node;
    }
}
