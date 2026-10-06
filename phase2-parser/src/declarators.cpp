#include "declarators.h"

#include "diagnostics/diagnostics.hpp"
#include "symbol_table/symbol_table.hpp"
#include "token/token_log.hpp"

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
   
    for (int i = 0; i < pointerLevel; ++i) base += "_POINTER";
    /* likewise one "_ARRAY" per dimension, so int[3] and int[2][2] are
       distinguishable. */
    for (int i = 0; i < arrayLevel; ++i) base += "_ARRAY";
    return base;
}

ASTTypeExprPtr makeTypeExpr(const TypeSpec &ts, const DeclInfo &d) {
    auto t = std::make_shared<ASTTypeExpr>();
    t->specParts = ts.parts;
    t->tagName = ts.tagName;
    t->typedefName = ts.typedefName;
    t->isStatic = ts.isStatic;
    t->isExtern = ts.isExtern;
    t->isRegister = ts.isRegister;
    t->storageClasses = ts.storageClasses;
    t->isConst = ts.isConst;
    t->isVolatile = ts.isVolatile;
    t->isAuto = ts.isAuto;
    t->isTypedef = ts.isTypedefStorage;
    t->pointerLevel = d.pointerLevel;
    t->isReference = d.isReference;
    t->arrayDims = d.arrayDims;
    t->grouped = d.grouped;
    t->innerPointerLevel = d.innerPointerLevel;
    t->innerArrayCount = d.innerArrayCount;
    t->ptrOps = d.ptrOps;
    t->innerPtrOps = d.innerPtrOps;
    t->isFunction = d.isFunction;
    t->isFunctionPointer = d.isFunctionPointer;
    t->isVariadic = d.isVariadic;
    for (const auto &p : d.params) {
        t->params.push_back(p.typeExpr ? p.typeExpr : std::make_shared<ASTTypeExpr>());
    }
    t->className = d.className;
    t->name = d.name;
    if (d.nameIdx >= 0 && d.nameIdx < static_cast<int>(g_tokens.size())) {
        t->nameLine = g_tokens[d.nameIdx].line;
        t->nameColumn = g_tokens[d.nameIdx].column;
    }
    return t;
}

ASTNodePtr atToken(const ASTNodePtr &n, int tokIdx) {
    if (n && tokIdx >= 0 && tokIdx < static_cast<int>(g_tokens.size())) {
        n->line = g_tokens[tokIdx].line;
        n->column = g_tokens[tokIdx].column;
    }
    return n;
}

ASTNodePtr atNode(const ASTNodePtr &n, const ASTNodePtr &from) {
    if (n && from) {
        n->line = from->line;
        n->column = from->column;
    }
    return n;
}

std::string anonymousTagAt(int tokIdx) {
    if (tokIdx >= 0 && tokIdx < static_cast<int>(g_tokens.size()))
        return anonymousTag(g_tokens[tokIdx].line, g_tokens[tokIdx].column);
    return anonymousTag(g_currentLine, g_currentColumn);
}

std::vector<ASTTypeExprPtr> paramExprs(const std::vector<DeclInfo> &params) {
    std::vector<ASTTypeExprPtr> out;
    for (const auto &p : params) out.push_back(p.typeExpr);
    return out;
}

ASTNodePtr registerDeclarator(DeclInfo &d, TypeSpec &ts) {
    if (d.nameIdx < 0) return nullptr; /* abstract declarator, nothing to register */

    if (ts.isTypedefStorage) {
        std::string typeStr = computeTypeStr(ts, d.pointerLevel, d.arrayLevel);
        /* `typedef struct { ... } Pt;` names the unnamed type Pt */
        if (isAnonymousTag(ts.tagName) && d.pointerLevel == 0 && d.arrayLevel == 0 && !d.isFunction &&
            !d.isFunctionPointer)
            nameAnonymousTag(ts.tagName, d.name);
        SymbolDeclInfo extra;
        extra.tokenIdx = d.nameIdx;
        extra.pointerLevel = d.pointerLevel;
        extra.arrayLevel = d.arrayLevel;
        extra.typeExpr = makeTypeExpr(ts, d);
        declareSymbol(d.name, SymKind::TYPEDEF_NAME, typeStr, extra);
        addTypeName(d.name);
        setCategory(d.nameIdx, "TYPEDEF");
        auto node = atToken(mkNode(ASTKind::TypedefDecl, d.name + " = " + typeStr), d.nameIdx);
        node->typeExpr = extra.typeExpr;
        return node;
    } else if (d.isFunctionPointer) {
    
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
        auto node = atToken(mkNode(ASTKind::VarDecl, d.name + " : " + typeStr), d.nameIdx);
        node->typeExpr = makeTypeExpr(ts, d);
        if (d.initExpr) addChild(node, d.initExpr);
        return node;
    } else if (d.isFunction) {
        std::vector<std::string> paramTypes;
        for (auto &p : d.params) paramTypes.push_back(p.typeStr);
        std::string mangled = mangle(d.name, paramExprs(d.params), d.isVariadic, currentClassName());
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

        auto node = atToken(mkNode(ASTKind::FunctionDecl, d.name + " : " + mangled), d.nameIdx);
        node->typeExpr = makeTypeExpr(ts, d);
        for (auto &p : d.params) {
            if (!p.name.empty()) {
                auto pn = atToken(mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr), p.nameIdx);
                pn->typeExpr = p.typeExpr;
                addChild(node, pn);
            }
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
        extra.aggregateTagName = ts.tagName; /* enables p.x / p->x resolution below */
        declareSymbol(d.name, SymKind::VARIABLE, typeStr, extra);
        setCategory(d.nameIdx, typeStr);
        hideTypeName(d.name);
        auto node = atToken(mkNode(ASTKind::VarDecl, d.name + " : " + typeStr), d.nameIdx);
        node->typeExpr = makeTypeExpr(ts, d);
        if (d.initExpr) addChild(node, d.initExpr);
        else if (d.ctorInit) {
            d.ctorInit->label = typeStr;
            addChild(node, d.ctorInit);
        }
        return node;
    }
}

ASTNodePtr makeConstructorNode(const std::string &name, int nameIdx, const std::vector<DeclInfo> &params,
                               bool variadic, const std::string &className, const ASTNodePtr &body) {
    std::vector<std::string> paramTypes;
    for (auto &p : params) paramTypes.push_back(p.typeStr);
    std::string mangled = mangle(name, paramExprs(params), variadic, className);
    SymbolDeclInfo extra;
    extra.tokenIdx = nameIdx;
    extra.returnType = "VOID";
    extra.paramTypes = paramTypes;
    extra.mangledName = mangled;
    declareSymbol(name, SymKind::PROCEDURE, "CONSTRUCTOR", extra);
    auto node = atToken(mkNode(ASTKind::ConstructorDef, name + " : " + mangled), nameIdx);
    DeclInfo ctor;
    ctor.name = name;
    ctor.nameIdx = nameIdx;
    ctor.isFunction = true;
    ctor.isVariadic = variadic;
    ctor.params = params;
    ctor.className = className;
    node->typeExpr = makeTypeExpr(TypeSpec(), ctor);
    for (auto &p : params) {
        if (!p.name.empty()) {
            auto pn = atToken(mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr), p.nameIdx);
            pn->typeExpr = p.typeExpr;
            addChild(node, pn);
        }
    }
    if (body) addChild(node, body);
    return node;
}

ASTNodePtr makeDestructorNode(const std::string &name, int nameIdx, const std::string &className,
                              const ASTNodePtr &body) {
    std::string mangled = mangle("~" + name, std::vector<ASTTypeExprPtr>{}, false, className);
    SymbolDeclInfo extra;
    extra.tokenIdx = nameIdx;
    extra.returnType = "VOID";
    extra.mangledName = mangled;
    declareSymbol("~" + name, SymKind::PROCEDURE, "DESTRUCTOR", extra);
    auto node = atToken(mkNode(ASTKind::DestructorDef, name + " : " + mangled), nameIdx);
    DeclInfo dtor;
    dtor.name = name;
    dtor.nameIdx = nameIdx;
    dtor.isFunction = true;
    dtor.className = className;
    node->typeExpr = makeTypeExpr(TypeSpec(), dtor);
    if (body) addChild(node, body);
    return node;
}
