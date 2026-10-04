/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output, and Bison version.  */
#define YYBISON 30802

/* Bison version string.  */
#define YYBISON_VERSION "3.8.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1





# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

#include "parser.tab.hpp"
/* Symbol kind.  */
enum yysymbol_kind_t
{
  YYSYMBOL_YYEMPTY = -2,
  YYSYMBOL_YYEOF = 0,                      /* "end of file"  */
  YYSYMBOL_YYerror = 1,                    /* error  */
  YYSYMBOL_YYUNDEF = 2,                    /* "invalid token"  */
  YYSYMBOL_INT = 3,                        /* INT  */
  YYSYMBOL_CHAR = 4,                       /* CHAR  */
  YYSYMBOL_FLOAT = 5,                      /* FLOAT  */
  YYSYMBOL_DOUBLE = 6,                     /* DOUBLE  */
  YYSYMBOL_VOID = 7,                       /* VOID  */
  YYSYMBOL_SHORT = 8,                      /* SHORT  */
  YYSYMBOL_LONG = 9,                       /* LONG  */
  YYSYMBOL_SIGNED = 10,                    /* SIGNED  */
  YYSYMBOL_UNSIGNED = 11,                  /* UNSIGNED  */
  YYSYMBOL_STRUCT = 12,                    /* STRUCT  */
  YYSYMBOL_ENUM = 13,                      /* ENUM  */
  YYSYMBOL_UNION = 14,                     /* UNION  */
  YYSYMBOL_CLASS = 15,                     /* CLASS  */
  YYSYMBOL_PUBLIC = 16,                    /* PUBLIC  */
  YYSYMBOL_PRIVATE = 17,                   /* PRIVATE  */
  YYSYMBOL_PROTECTED = 18,                 /* PROTECTED  */
  YYSYMBOL_THIS = 19,                      /* THIS  */
  YYSYMBOL_STATIC = 20,                    /* STATIC  */
  YYSYMBOL_TYPEDEF = 21,                   /* TYPEDEF  */
  YYSYMBOL_AUTO = 22,                      /* AUTO  */
  YYSYMBOL_EXTERN = 23,                    /* EXTERN  */
  YYSYMBOL_REGISTER = 24,                  /* REGISTER  */
  YYSYMBOL_CONST = 25,                     /* CONST  */
  YYSYMBOL_VOLATILE = 26,                  /* VOLATILE  */
  YYSYMBOL_IF = 27,                        /* IF  */
  YYSYMBOL_ELSE = 28,                      /* ELSE  */
  YYSYMBOL_FOR = 29,                       /* FOR  */
  YYSYMBOL_WHILE = 30,                     /* WHILE  */
  YYSYMBOL_DO = 31,                        /* DO  */
  YYSYMBOL_UNTIL = 32,                     /* UNTIL  */
  YYSYMBOL_SWITCH = 33,                    /* SWITCH  */
  YYSYMBOL_CASE = 34,                      /* CASE  */
  YYSYMBOL_DEFAULT = 35,                   /* DEFAULT  */
  YYSYMBOL_BREAK = 36,                     /* BREAK  */
  YYSYMBOL_CONTINUE = 37,                  /* CONTINUE  */
  YYSYMBOL_GOTO = 38,                      /* GOTO  */
  YYSYMBOL_RETURN = 39,                    /* RETURN  */
  YYSYMBOL_PRINTF = 40,                    /* PRINTF  */
  YYSYMBOL_SCANF = 41,                     /* SCANF  */
  YYSYMBOL_MALLOC = 42,                    /* MALLOC  */
  YYSYMBOL_FREE = 43,                      /* FREE  */
  YYSYMBOL_CALLOC = 44,                    /* CALLOC  */
  YYSYMBOL_REALLOC = 45,                   /* REALLOC  */
  YYSYMBOL_FILE_KW = 46,                   /* FILE_KW  */
  YYSYMBOL_FOPEN = 47,                     /* FOPEN  */
  YYSYMBOL_FCLOSE = 48,                    /* FCLOSE  */
  YYSYMBOL_FREAD = 49,                     /* FREAD  */
  YYSYMBOL_FWRITE = 50,                    /* FWRITE  */
  YYSYMBOL_FPRINTF = 51,                   /* FPRINTF  */
  YYSYMBOL_FSCANF = 52,                    /* FSCANF  */
  YYSYMBOL_FGETS = 53,                     /* FGETS  */
  YYSYMBOL_FPUTS = 54,                     /* FPUTS  */
  YYSYMBOL_FEOF = 55,                      /* FEOF  */
  YYSYMBOL_BOOL = 56,                      /* BOOL  */
  YYSYMBOL_NEW = 57,                       /* NEW  */
  YYSYMBOL_DELETE = 58,                    /* DELETE  */
  YYSYMBOL_SIZEOF = 59,                    /* SIZEOF  */
  YYSYMBOL_VA_LIST = 60,                   /* VA_LIST  */
  YYSYMBOL_VA_START = 61,                  /* VA_START  */
  YYSYMBOL_VA_ARG = 62,                    /* VA_ARG  */
  YYSYMBOL_VA_END = 63,                    /* VA_END  */
  YYSYMBOL_MUTABLE = 64,                   /* MUTABLE  */
  YYSYMBOL_OPERATOR = 65,                  /* OPERATOR  */
  YYSYMBOL_DELETE_ARRAY = 66,              /* DELETE_ARRAY  */
  YYSYMBOL_FCAST = 67,                     /* FCAST  */
  YYSYMBOL_DESIG_LBRACKET = 68,            /* DESIG_LBRACKET  */
  YYSYMBOL_ABSTRACT_LPAREN = 69,           /* ABSTRACT_LPAREN  */
  YYSYMBOL_IDENTIFIER = 70,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 71,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 72,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 73,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 74,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 75,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 76,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 77,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 78,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 79,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 80,                       /* INC  */
  YYSYMBOL_DEC = 81,                       /* DEC  */
  YYSYMBOL_SHL = 82,                       /* SHL  */
  YYSYMBOL_SHR = 83,                       /* SHR  */
  YYSYMBOL_LE_OP = 84,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 85,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 86,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 87,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 88,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 89,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 90,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 91,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 92,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 93,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 94,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 95,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 96,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 97,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 98,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 99,                /* SHR_ASSIGN  */
  YYSYMBOL_PREFER_EXPRESSION = 100,        /* PREFER_EXPRESSION  */
  YYSYMBOL_NEW_TYPE_END = 101,             /* NEW_TYPE_END  */
  YYSYMBOL_102_ = 102,                     /* '='  */
  YYSYMBOL_103_ = 103,                     /* '?'  */
  YYSYMBOL_104_ = 104,                     /* ':'  */
  YYSYMBOL_105_ = 105,                     /* '|'  */
  YYSYMBOL_106_ = 106,                     /* '^'  */
  YYSYMBOL_107_ = 107,                     /* '&'  */
  YYSYMBOL_108_ = 108,                     /* '<'  */
  YYSYMBOL_109_ = 109,                     /* '>'  */
  YYSYMBOL_110_ = 110,                     /* '+'  */
  YYSYMBOL_111_ = 111,                     /* '-'  */
  YYSYMBOL_112_ = 112,                     /* '*'  */
  YYSYMBOL_113_ = 113,                     /* '/'  */
  YYSYMBOL_114_ = 114,                     /* '%'  */
  YYSYMBOL_UMINUS = 115,                   /* UMINUS  */
  YYSYMBOL_ADDR = 116,                     /* ADDR  */
  YYSYMBOL_DEREF = 117,                    /* DEREF  */
  YYSYMBOL_CAST = 118,                     /* CAST  */
  YYSYMBOL_119_ = 119,                     /* '!'  */
  YYSYMBOL_120_ = 120,                     /* '~'  */
  YYSYMBOL_121_ = 121,                     /* '.'  */
  YYSYMBOL_122_ = 122,                     /* '('  */
  YYSYMBOL_123_ = 123,                     /* '['  */
  YYSYMBOL_SIZEOF_TYPE = 124,              /* SIZEOF_TYPE  */
  YYSYMBOL_PREFER_DECLARATION = 125,       /* PREFER_DECLARATION  */
  YYSYMBOL_IFX = 126,                      /* IFX  */
  YYSYMBOL_127_ = 127,                     /* ';'  */
  YYSYMBOL_128_ = 128,                     /* '}'  */
  YYSYMBOL_129_ = 129,                     /* '{'  */
  YYSYMBOL_130_ = 130,                     /* ','  */
  YYSYMBOL_131_ = 131,                     /* ')'  */
  YYSYMBOL_132_ = 132,                     /* ']'  */
  YYSYMBOL_YYACCEPT = 133,                 /* $accept  */
  YYSYMBOL_translation_unit = 134,         /* translation_unit  */
  YYSYMBOL_external_decl = 135,            /* external_decl  */
  YYSYMBOL_declaration = 136,              /* declaration  */
  YYSYMBOL_declaration_specifiers = 137,   /* declaration_specifiers  */
  YYSYMBOL_storage_or_type_specifier = 138, /* storage_or_type_specifier  */
  YYSYMBOL_type_specifier = 139,           /* type_specifier  */
  YYSYMBOL_tag_name = 140,                 /* tag_name  */
  YYSYMBOL_struct_or_class_specifier = 141, /* struct_or_class_specifier  */
  YYSYMBOL_142_1 = 142,                    /* $@1  */
  YYSYMBOL_143_2 = 143,                    /* $@2  */
  YYSYMBOL_144_3 = 144,                    /* @3  */
  YYSYMBOL_145_4 = 145,                    /* $@4  */
  YYSYMBOL_146_5 = 146,                    /* $@5  */
  YYSYMBOL_147_6 = 147,                    /* @6  */
  YYSYMBOL_148_7 = 148,                    /* $@7  */
  YYSYMBOL_149_8 = 149,                    /* $@8  */
  YYSYMBOL_150_9 = 150,                    /* @9  */
  YYSYMBOL_151_10 = 151,                   /* $@10  */
  YYSYMBOL_152_11 = 152,                   /* @11  */
  YYSYMBOL_member_decl_list_opt = 153,     /* member_decl_list_opt  */
  YYSYMBOL_inheritance_opt = 154,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 155, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 156,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 157,         /* member_decl_list  */
  YYSYMBOL_member_item = 158,              /* member_item  */
  YYSYMBOL_constructor_head = 159,         /* constructor_head  */
  YYSYMBOL_160_12 = 160,                   /* $@12  */
  YYSYMBOL_constructor_def = 161,          /* constructor_def  */
  YYSYMBOL_destructor_head = 162,          /* destructor_head  */
  YYSYMBOL_destructor_def = 163,           /* destructor_def  */
  YYSYMBOL_out_of_class_special = 164,     /* out_of_class_special  */
  YYSYMBOL_165_13 = 165,                   /* $@13  */
  YYSYMBOL_166_14 = 166,                   /* $@14  */
  YYSYMBOL_167_15 = 167,                   /* $@15  */
  YYSYMBOL_access_specifier = 168,         /* access_specifier  */
  YYSYMBOL_enumerator_list = 169,          /* enumerator_list  */
  YYSYMBOL_enumerator = 170,               /* enumerator  */
  YYSYMBOL_init_declarator_list_opt = 171, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 172,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 173,          /* init_declarator  */
  YYSYMBOL_initializer = 174,              /* initializer  */
  YYSYMBOL_initializer_list = 175,         /* initializer_list  */
  YYSYMBOL_initializer_item = 176,         /* initializer_item  */
  YYSYMBOL_pointer = 177,                  /* pointer  */
  YYSYMBOL_declarator = 178,               /* declarator  */
  YYSYMBOL_abstract_declarator = 179,      /* abstract_declarator  */
  YYSYMBOL_direct_abstract_declarator = 180, /* direct_abstract_declarator  */
  YYSYMBOL_direct_declarator = 181,        /* direct_declarator  */
  YYSYMBOL_operator_function_id = 182,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 183,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 184,              /* param_scope  */
  YYSYMBOL_constructor_args = 185,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 186,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 187,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 188,           /* parameter_decl  */
  YYSYMBOL_function_definition = 189,      /* function_definition  */
  YYSYMBOL_190_16 = 190,                   /* $@16  */
  YYSYMBOL_statement = 191,                /* statement  */
  YYSYMBOL_compound_stmt = 192,            /* compound_stmt  */
  YYSYMBOL_193_17 = 193,                   /* $@17  */
  YYSYMBOL_block_item_list_opt = 194,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 195,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 196,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 197,           /* selection_stmt  */
  YYSYMBOL_198_18 = 198,                   /* $@18  */
  YYSYMBOL_labeled_stmt = 199,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 200,           /* iteration_stmt  */
  YYSYMBOL_for_open = 201,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 202,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 203,                /* jump_stmt  */
  YYSYMBOL_expr = 204,                     /* expr  */
  YYSYMBOL_assignment_expr = 205,          /* assignment_expr  */
  YYSYMBOL_assign_op = 206,                /* assign_op  */
  YYSYMBOL_constant_expr = 207,            /* constant_expr  */
  YYSYMBOL_binary_expr = 208,              /* binary_expr  */
  YYSYMBOL_unary_expr = 209,               /* unary_expr  */
  YYSYMBOL_type_name = 210,                /* type_name  */
  YYSYMBOL_new_type_id = 211,              /* new_type_id  */
  YYSYMBOL_new_pointer = 212,              /* new_pointer  */
  YYSYMBOL_new_array_dims = 213,           /* new_array_dims  */
  YYSYMBOL_type_name_specifiers = 214,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 215,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 216,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 217,             /* builtin_call  */
  YYSYMBOL_constructor_args_opt = 218,     /* constructor_args_opt  */
  YYSYMBOL_argument_list_opt = 219,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 220,            /* argument_list  */
  YYSYMBOL_argument = 221,                 /* argument  */
  YYSYMBOL_primary_expr = 222,             /* primary_expr  */
  YYSYMBOL_string_literal = 223,           /* string_literal  */
  YYSYMBOL_lambda_expr = 224,              /* lambda_expr  */
  YYSYMBOL_225_19 = 225,                   /* $@19  */
  YYSYMBOL_226_20 = 226,                   /* $@20  */
  YYSYMBOL_227_21 = 227,                   /* $@21  */
  YYSYMBOL_lambda_specifiers = 228,        /* lambda_specifiers  */
  YYSYMBOL_capture_list_opt = 229,         /* capture_list_opt  */
  YYSYMBOL_capture_list = 230,             /* capture_list  */
  YYSYMBOL_capture = 231                   /* capture  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;



/* Unqualified %code blocks.  */
#line 13 "../phase2-parser/src/parser.y"

    #include <cstdio>
    #include <cctype>
    #include <cstring>
    #include <string>

    #include "declarators.h"
    #include "diagnostics/diagnostics.hpp"
    #include "scanner_support.h"
    #include "symbol_table/symbol_table.hpp"
    #include "token/token_log.hpp"
    #include "token/token_type.hpp"
    extern int yylex();
    extern FILE *yyin;
    extern int yylineno;
    void yyerror(const char *s);

    /* `T(args)` as an expression: ConstructExpr whose typeExpr names T
       (a type keyword, a typedef, or a class/struct used as a type) */
    static ASTNodePtr makeFunctionalCast(const std::string &name, int idx, const std::vector<ASTNodePtr> &args) {
        auto n = atToken(mkNode(ASTKind::ConstructExpr, name), idx);
        TypeSpec ts;
        auto kw = reserved_word(name);
        if (kw.has_value()) {
            std::string part = name;
            for (auto &ch : part) ch = static_cast<char>(toupper(static_cast<unsigned char>(ch)));
            ts.parts.push_back(part);
        } else {
            const Symbol *s = lookupTypeSymbol(name);
            setCategory(idx, categoryForTypeName(s));
            ts.parts.push_back(s ? s->typeStr : "INT");
            ts.typedefName = name;
        }
        n->typeExpr = makeTypeExpr(ts, DeclInfo());
        for (auto &a : args) addChild(n, a);
        return n;
    }

    /* LambdaExpr: label = capture list, children = named ParamDecls then
       the body; typeExpr = the function shape, with the explicit `-> T`
       return type in its specifiers when one was written */
    static ASTNodePtr makeLambdaNode(int bracketIdx, const std::string &captures,
                                     const std::vector<DeclInfo> &params, bool variadic,
                                     const ParserValue &specs, const ASTNodePtr &body) {
        auto n = atToken(mkNode(ASTKind::LambdaExpr, captures), bracketIdx);
        bool explicitReturn = specs.idx == 1;
        DeclInfo fn = explicitReturn ? specs.decl : DeclInfo();
        fn.isFunction = true;
        fn.isVariadic = variadic;
        fn.params = params;
        n->typeExpr = makeTypeExpr(explicitReturn ? specs.typeSpec : TypeSpec(), fn);
        n->typeExpr->isMutable = specs.str == "mutable";
        n->typeExpr->hasExplicitReturn = explicitReturn;
        for (auto &p : params) {
            if (!p.name.empty()) {
                auto pn = atToken(mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr), p.nameIdx);
                pn->typeExpr = p.typeExpr;
                addChild(n, pn);
            }
        }
        addChild(n, body);
        return n;
    }

#line 400 "build/parser.tab.cpp"

#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

/* Work around bug in HP-UX 11.23, which defines these macros
   incorrectly for preprocessor constants.  This workaround can likely
   be removed in 2023, as HPE has promised support for HP-UX 11.23
   (aka HP-UX 11i v2) only through the end of 2022; see Table 2 of
   <https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf>.  */
#ifdef __hpux
# undef UINT_LEAST8_MAX
# undef UINT_LEAST16_MAX
# define UINT_LEAST8_MAX 255
# define UINT_LEAST16_MAX 65535
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))


/* Stored state numbers (used for stacks). */
typedef yytype_int16 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif


#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YY_USE(E) ((void) (E))
#else
# define YY_USE(E) /* empty */
#endif

/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
#if defined __GNUC__ && ! defined __ICC && 406 <= __GNUC__ * 100 + __GNUC_MINOR__
# if __GNUC__ * 100 + __GNUC_MINOR__ < 407
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")
# else
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# endif
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if 1

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* 1 */

#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL \
             && defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
  YYLTYPE yyls_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE) \
             + YYSIZEOF (YYLTYPE)) \
      + 2 * YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  2
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   2724

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  133
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  99
/* YYNRULES -- Number of rules.  */
#define YYNRULES  393
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  711

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   363


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK                     \
   ? YY_CAST (yysymbol_kind_t, yytranslate[YYX])        \
   : YYSYMBOL_YYUNDEF)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   119,     2,     2,     2,   114,   107,     2,
     122,   131,   112,   110,   130,   111,   121,   113,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   104,   127,
     108,   102,   109,   103,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   123,     2,   132,   106,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   129,   105,   128,   120,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   115,   116,   117,
     118,   124,   125,   126
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   152,   152,   156,   164,   165,   166,   167,   168,   172,
     206,   221,   225,   226,   227,   228,   229,   230,   231,   232,
     236,   237,   238,   239,   240,   241,   242,   243,   244,   245,
     246,   247,   248,   264,   271,   272,   276,   280,   276,   296,
     296,   310,   316,   322,   326,   322,   335,   335,   349,   355,
     361,   365,   361,   377,   377,   391,   397,   403,   403,   414,
     414,   424,   430,   439,   440,   444,   445,   449,   450,   457,
     463,   469,   475,   486,   491,   503,   504,   505,   506,   507,
     514,   514,   531,   535,   542,   550,   554,   562,   566,   562,
     581,   581,   594,   595,   596,   600,   601,   605,   610,   618,
     619,   623,   624,   628,   629,   633,   634,   635,   640,   648,
     649,   653,   654,   657,   664,   665,   666,   667,   668,   669,
     673,   679,   685,   686,   692,   696,   705,   706,   707,   708,
     709,   721,   725,   732,   744,   753,   757,   764,   771,   788,
     795,   796,   801,   805,   805,   805,   805,   806,   806,   806,
     806,   807,   807,   807,   807,   808,   808,   808,   808,   809,
     809,   809,   809,   810,   810,   810,   811,   811,   811,   812,
     812,   812,   813,   813,   813,   814,   814,   814,   821,   825,
     826,   830,   831,   835,   839,   843,   847,   852,   857,   865,
     865,   927,   928,   929,   930,   931,   932,   933,   934,   935,
     939,   939,   948,   949,   953,   954,   958,   959,   963,   966,
     969,   969,   975,   978,   981,   989,   992,   999,  1003,  1007,
    1010,  1014,  1023,  1027,  1028,  1032,  1033,  1034,  1035,  1036,
    1046,  1047,  1051,  1052,  1058,  1059,  1060,  1061,  1062,  1063,
    1064,  1065,  1066,  1067,  1068,  1072,  1076,  1077,  1078,  1079,
    1080,  1081,  1082,  1083,  1084,  1085,  1086,  1087,  1088,  1089,
    1090,  1091,  1092,  1093,  1094,  1097,  1101,  1102,  1103,  1104,
    1105,  1106,  1107,  1108,  1109,  1110,  1114,  1115,  1119,  1123,
    1131,  1132,  1136,  1140,  1149,  1153,  1157,  1161,  1170,  1171,
    1176,  1177,  1181,  1189,  1193,  1194,  1195,  1196,  1197,  1198,
    1199,  1200,  1201,  1202,  1203,  1204,  1205,  1206,  1207,  1216,
    1222,  1228,  1234,  1240,  1246,  1252,  1258,  1267,  1268,  1269,
    1304,  1314,  1324,  1325,  1326,  1327,  1331,  1332,  1333,  1334,
    1335,  1336,  1337,  1338,  1339,  1340,  1341,  1342,  1343,  1344,
    1345,  1346,  1347,  1348,  1352,  1353,  1357,  1358,  1362,  1363,
    1367,  1368,  1375,  1384,  1385,  1386,  1387,  1388,  1389,  1390,
    1394,  1401,  1402,  1403,  1404,  1405,  1406,  1407,  1408,  1409,
    1410,  1411,  1418,  1419,  1424,  1425,  1433,  1433,  1433,  1444,
    1444,  1454,  1455,  1456,  1457,  1461,  1462,  1466,  1467,  1471,
    1477,  1483,  1484,  1485
};
#endif

/** Accessing symbol of state STATE.  */
#define YY_ACCESSING_SYMBOL(State) YY_CAST (yysymbol_kind_t, yystos[State])

#if 1
/* The user-facing name of the symbol whose (internal) number is
   YYSYMBOL.  No bounds checking.  */
static const char *yysymbol_name (yysymbol_kind_t yysymbol) YY_ATTRIBUTE_UNUSED;

/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "\"end of file\"", "error", "\"invalid token\"", "INT", "CHAR", "FLOAT",
  "DOUBLE", "VOID", "SHORT", "LONG", "SIGNED", "UNSIGNED", "STRUCT",
  "ENUM", "UNION", "CLASS", "PUBLIC", "PRIVATE", "PROTECTED", "THIS",
  "STATIC", "TYPEDEF", "AUTO", "EXTERN", "REGISTER", "CONST", "VOLATILE",
  "IF", "ELSE", "FOR", "WHILE", "DO", "UNTIL", "SWITCH", "CASE", "DEFAULT",
  "BREAK", "CONTINUE", "GOTO", "RETURN", "PRINTF", "SCANF", "MALLOC",
  "FREE", "CALLOC", "REALLOC", "FILE_KW", "FOPEN", "FCLOSE", "FREAD",
  "FWRITE", "FPRINTF", "FSCANF", "FGETS", "FPUTS", "FEOF", "BOOL", "NEW",
  "DELETE", "SIZEOF", "VA_LIST", "VA_START", "VA_ARG", "VA_END", "MUTABLE",
  "OPERATOR", "DELETE_ARRAY", "FCAST", "DESIG_LBRACKET", "ABSTRACT_LPAREN",
  "IDENTIFIER", "TYPE_NAME", "INT_LITERAL", "FLOAT_LITERAL",
  "CHAR_LITERAL", "STRING_LITERAL", "BOOL_LITERAL", "ARROW", "ELLIPSIS",
  "SCOPE_RES", "INC", "DEC", "SHL", "SHR", "LE_OP", "GE_OP", "EQ_OP",
  "NE_OP", "AND_OP", "OR_OP", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN",
  "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN",
  "SHL_ASSIGN", "SHR_ASSIGN", "PREFER_EXPRESSION", "NEW_TYPE_END", "'='",
  "'?'", "':'", "'|'", "'^'", "'&'", "'<'", "'>'", "'+'", "'-'", "'*'",
  "'/'", "'%'", "UMINUS", "ADDR", "DEREF", "CAST", "'!'", "'~'", "'.'",
  "'('", "'['", "SIZEOF_TYPE", "PREFER_DECLARATION", "IFX", "';'", "'}'",
  "'{'", "','", "')'", "']'", "$accept", "translation_unit",
  "external_decl", "declaration", "declaration_specifiers",
  "storage_or_type_specifier", "type_specifier", "tag_name",
  "struct_or_class_specifier", "$@1", "$@2", "@3", "$@4", "$@5", "@6",
  "$@7", "$@8", "@9", "$@10", "@11", "member_decl_list_opt",
  "inheritance_opt", "inheritance_specifier_list", "inheritance_specifier",
  "member_decl_list", "member_item", "constructor_head", "$@12",
  "constructor_def", "destructor_head", "destructor_def",
  "out_of_class_special", "$@13", "$@14", "$@15", "access_specifier",
  "enumerator_list", "enumerator", "init_declarator_list_opt",
  "init_declarator_list", "init_declarator", "initializer",
  "initializer_list", "initializer_item", "pointer", "declarator",
  "abstract_declarator", "direct_abstract_declarator", "direct_declarator",
  "operator_function_id", "overloadable_operator", "param_scope",
  "constructor_args", "parameter_list_opt", "parameter_list",
  "parameter_decl", "function_definition", "$@16", "statement",
  "compound_stmt", "$@17", "block_item_list_opt", "block_item_list",
  "expr_stmt", "selection_stmt", "$@18", "labeled_stmt", "iteration_stmt",
  "for_open", "for_incr_opt", "jump_stmt", "expr", "assignment_expr",
  "assign_op", "constant_expr", "binary_expr", "unary_expr", "type_name",
  "new_type_id", "new_pointer", "new_array_dims", "type_name_specifiers",
  "type_name_specifier", "postfix_expr", "builtin_call",
  "constructor_args_opt", "argument_list_opt", "argument_list", "argument",
  "primary_expr", "string_literal", "lambda_expr", "$@19", "$@20", "$@21",
  "lambda_specifiers", "capture_list_opt", "capture_list", "capture", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-468)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-204)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -468,   553,  -468,    74,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,   -29,   -24,    -7,    -4,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,   -61,  -468,  -468,
    2318,  -468,  -468,  -468,  -468,  -468,  -468,  -468,   -95,   -33,
    -468,  -468,   -95,   -33,  -468,  -468,   -95,   -33,  -468,  -468,
     -28,   -22,  -468,  -468,   -50,  2559,    30,    38,  -468,  -468,
      14,  -468,    60,     8,  -468,   171,   -58,    93,  -468,  2387,
      78,   162,   122,  2387,   138,  2387,   170,   160,   214,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,   168,   215,  -468,    46,   116,    38,   217,  -468,
      14,  -468,  -468,  -468,  -468,    93,  1455,   220,  2419,   625,
    -468,  -468,  -468,   228,  -468,   282,  -468,   226,  2387,  -468,
     -35,  -468,    79,  -468,   254,  -468,  -468,   257,   109,  -468,
     162,   232,  -468,   234,   159,   253,  -468,   261,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,   283,   264,   265,   268,
     269,   270,   271,   272,   273,   274,  -468,   275,   278,   279,
     280,   281,   284,   285,   286,   287,   290,   291,   292,   295,
     298,   299,   313,   419,  1933,  2017,   314,   316,   317,  1933,
     318,  -468,   -14,  -468,  -468,  -468,  -468,  -468,  1933,  1933,
    1933,  1933,  1933,  1933,  1933,  1933,  1849,    13,  1275,  -468,
    -468,  2601,   236,   154,  -468,  -468,   329,  -468,   927,  2567,
      96,  -468,  -468,   309,  -468,   321,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  2387,  1933,  -468,   162,   110,  -468,
    2387,  -468,  -468,  -468,   319,  -468,   190,  -468,  2567,   315,
    1933,  1933,  1933,  1933,  1933,  1933,  1933,  1933,  1933,  1849,
    1849,  1849,  1849,  1849,  1849,  1849,  1849,  1849,  1849,  1849,
    1849,  1849,  1849,  1849,  1933,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,   193,   195,   199,   201,  -468,  -468,
    -468,  -468,  -468,  -468,   325,   525,  -468,  -468,  1849,  -468,
    1849,  1849,  1849,  -468,  1933,   335,  1933,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,   264,   265,   268,   269,   270,
     271,   272,   273,   274,   313,   -14,   161,  -468,   322,  2249,
    -468,  -468,  -468,   378,   323,   324,  -468,  1933,   386,  -468,
    -468,   117,  -468,  1933,  1933,  1933,  1933,  1933,  1933,  1933,
    1933,  1933,  1933,  1933,  1933,  1933,  1933,  1933,  1933,  1933,
    1933,  1933,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  1933,   388,   389,  -468,  -468,   390,  1849,
    1933,  -468,   167,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,   339,   340,   341,  1185,   342,   344,  1933,   363,
     345,   346,   398,  1671,  -468,   365,   392,  -468,  -468,  2318,
    -468,  -468,   348,  1056,  -468,  -468,  -468,  -468,  1582,  -468,
     -17,  2180,   343,   351,  -468,  1933,  -468,  -468,  2567,   347,
     927,   354,  -468,  2601,  -468,  -468,  -468,   355,   159,  -468,
    -468,  2387,   353,  -468,   356,   360,   361,   371,   372,   375,
     377,   379,   380,   381,  -468,  -468,   382,   357,  -468,   383,
     384,   410,   412,   414,   416,   417,   418,   424,   441,   449,
     451,   452,   453,   456,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  1933,  -468,  1933,    -9,   362,  -468,   457,   464,
     466,   467,   469,  -468,   470,  1933,  -468,  1933,    11,   711,
      12,  -468,   174,  -468,   422,    13,   471,   500,  -468,  1365,
     100,   100,   176,   176,  2159,  2159,  2523,   413,    69,  2610,
     507,   813,   176,   176,    16,    16,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,   473,   114,  -468,  -468,  1933,  -468,  1933,
      18,  1933,  1933,   501,  1185,  -468,  -468,   367,  -468,    73,
    1185,  -468,  -468,  1760,  1760,  -468,    62,  -468,  -468,  -468,
    2540,  -468,   475,  -468,   479,  -468,  -468,  -468,   480,  -468,
     481,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  1849,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,   492,   118,  -468,
     362,  1933,  2101,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
     494,  -468,   495,   174,  -468,   797,  -468,   481,  -468,   509,
    1455,  -468,  -468,  1933,  -468,  -468,   173,   206,   485,   504,
     209,   211,  1185,  -468,  -468,  -468,  -468,  1933,  1933,  -468,
    -468,  -468,  -468,  -468,   481,  -468,  -468,  -468,  -468,   124,
    -468,  -468,  2567,  -468,   506,  2567,  -468,  1455,  -468,  2601,
    1185,  1185,  -468,  1933,  1185,  -468,  -468,   508,   510,   511,
    -468,  -468,   514,  -468,   515,  -468,   613,  -468,   213,  -468,
     481,  1185,  1185,  -468,     9,  1185,    39,  -468,  -468,  -468,
     570,   419,  -468,  -468,  -468,  -468,   419,  -468,   481,  -468,
    -468
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    20,    21,    22,    23,    24,    26,
      27,    28,    29,     0,     0,     0,     0,    12,    16,    15,
      13,    14,    17,    18,    30,    25,    31,    32,     3,     5,
      99,    11,    19,    33,     6,     4,     7,     8,    41,    42,
      39,    36,    61,    62,    59,    57,    48,    49,    46,    43,
      55,    56,    53,    50,     0,     0,   131,    32,   115,   114,
       0,    10,     0,   100,   101,     0,   103,   121,   135,    63,
       0,     0,     0,    63,     0,    63,    65,     0,     0,   164,
     165,   162,   163,   158,   159,   156,   157,   160,   161,   166,
     167,   168,   169,   170,   171,   172,   173,   174,   175,   153,
     150,   148,   149,   154,   155,   143,   144,   145,   146,   147,
     152,   151,     0,     0,   142,     0,     0,     0,     0,     9,
       0,   118,   119,   117,   116,   120,     0,     0,   178,     0,
      92,    93,    94,     0,    32,     0,    75,     0,    64,    73,
       0,    78,     0,    79,     0,    76,    37,    97,     0,    95,
       0,     0,    44,     0,     0,     0,    87,     0,   177,   176,
     132,   136,   133,   137,   134,   102,   103,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   358,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   352,     0,   353,   354,   355,   374,   357,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   385,     0,   104,
     105,   232,   265,   266,   325,   317,   356,   373,     0,   181,
       0,   179,   140,     0,    80,     0,    40,    74,    83,   200,
      82,    86,    85,    77,    63,     0,    60,     0,     0,    47,
      63,    54,    71,    72,    66,    67,     0,    51,   181,     0,
     344,   344,   344,   344,   344,   344,   344,   344,   344,   346,
     346,   346,   346,   346,   346,   346,   346,   346,   346,   346,
     346,   346,   346,   346,   344,   294,   295,   296,   297,   298,
     300,   301,   302,   303,     0,     0,     0,     0,   306,   307,
     304,   299,   305,   308,   278,   284,   293,   280,     0,   276,
     346,   346,   346,   281,   344,     0,   344,   267,   268,   269,
     271,   272,   270,   273,   274,   294,   295,   296,   297,   298,
     300,   301,   302,   303,   299,   308,     0,   230,     0,   282,
     393,   389,   392,   391,     0,   386,   387,     0,     0,   106,
     111,     0,   109,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   235,   236,   237,   238,   239,   240,   241,   242,
     243,   244,   234,     0,     0,     0,   323,   324,     0,   346,
       0,   375,     0,    20,    21,    22,    23,    24,    26,    27,
      28,    29,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    25,   352,    32,   206,   197,    99,
     204,   191,     0,     0,   192,   193,   196,   194,     0,   195,
       0,   188,     0,   182,   183,     0,   139,   141,   181,     0,
       0,     0,    98,   245,   265,    96,    58,     0,     0,    69,
      70,    63,     0,    90,   345,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   350,   351,     0,   347,   348,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   309,   310,   315,   316,   311,   312,
     313,   314,   344,   288,     0,   285,   286,   292,     0,     0,
       0,     0,     0,   371,     0,     0,   372,     0,     0,     0,
     122,   283,   124,   390,   379,     0,     0,     0,   107,     0,
     257,   258,   255,   256,   251,   252,   247,   246,     0,   248,
     249,   250,   253,   254,   259,   260,   261,   262,   263,   233,
     321,   322,   320,     0,     0,   198,   199,     0,   222,     0,
       0,     0,     0,     0,     0,   225,   226,     0,   227,     0,
       0,   190,   205,     0,     0,   207,   122,   186,   187,   138,
       0,   180,     0,    84,     0,    38,    45,    68,     0,    88,
       0,   361,   362,   363,   364,   365,   367,   368,   369,   370,
     326,     0,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   366,     0,     0,   289,
     287,     0,   277,   341,   342,   343,   360,   359,   231,   275,
       0,   126,     0,   123,   178,     0,   376,     0,   388,     0,
       0,   108,   110,     0,   319,   318,     0,     0,     0,     0,
       0,     0,     0,   213,   229,   228,   214,   223,   223,   185,
     184,    81,   201,    52,     0,    91,   349,   279,   290,     0,
     125,   127,   181,   128,     0,   181,   380,     0,   112,   264,
       0,     0,   218,     0,     0,   210,   212,     0,   224,     0,
      89,   291,     0,   129,     0,   113,   208,   215,     0,   219,
       0,     0,     0,   130,   381,     0,     0,   211,   221,   220,
     382,     0,   377,   209,   217,   216,     0,   383,     0,   384,
     378
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -468,  -468,  -468,    29,    -1,   -20,  -468,   164,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
     -62,  -468,  -468,   202,  -468,   513,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -123,   499,   405,  -468,  -468,
     533,  -125,  -468,   135,  -325,   -21,  -415,  -467,   -59,   230,
    -468,    31,   528,  -246,  -468,    87,   657,  -468,  -390,  -138,
    -468,   219,  -468,  -392,  -468,  -468,  -468,  -468,  -468,    15,
    -468,  -196,  -121,  -468,  -330,   -47,    10,  -213,  -468,  -468,
     165,   478,  -270,  -468,  -468,  -239,  -221,  -468,    71,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,   175
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    28,   418,   419,    31,    32,    41,    33,    70,
     244,    69,    74,   250,    73,    76,   451,    75,    72,    71,
     137,   155,   254,   255,   138,   139,   140,   438,   141,   142,
     143,    34,   258,   654,   580,   144,   148,   149,    62,    63,
      64,   350,   351,   352,    65,   166,   511,   512,    67,    68,
     114,   229,   454,   432,   433,   434,   145,   127,   420,   421,
     440,   422,   423,   424,   425,   690,   426,   427,   428,   677,
     429,   430,   337,   383,   442,   221,   222,   465,   304,   495,
     496,   339,   306,   223,   224,   455,   466,   467,   468,   225,
     226,   227,   665,   708,   627,   702,   344,   345,   346
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      30,   219,   240,   338,   242,   220,   125,   231,   233,    66,
      61,   151,   452,   153,   510,   550,   568,   516,    54,   638,
     336,    77,   456,   457,   458,   459,   460,   461,   462,   463,
      29,   256,   340,   562,   -34,   497,   564,   121,   122,   118,
     704,    38,    39,   623,   126,   483,    42,    43,   639,   469,
     470,   471,   472,   473,   474,   475,   476,   477,   478,   479,
     480,   481,   482,    46,    47,   315,    50,    51,    30,   497,
      78,  -189,    30,   700,    30,   502,   -34,   504,   553,    55,
     508,   508,   -35,   341,    56,   117,   701,   121,   122,   499,
     500,   501,   238,   620,   239,   498,   -35,   220,   136,   623,
      40,   -34,   136,   609,   136,    44,   566,   -35,   316,   115,
     565,    55,   336,   505,   494,   342,   160,   116,    58,   123,
     343,    58,    48,    59,   124,    52,    59,    55,   369,   370,
     371,   508,    56,   117,   509,   509,    60,    30,   120,   231,
     231,   231,   231,   231,   231,   231,   231,   231,   464,   464,
     464,   464,   464,   464,   464,   464,   464,   464,   464,   464,
     464,   464,   464,   231,   643,   528,   705,   136,   543,   123,
     646,   647,   648,   633,   124,   130,   131,   132,    45,    49,
      53,    55,   441,   510,    60,   509,   162,   119,   447,   464,
     464,   464,   572,   231,   544,   231,   121,   122,   443,   505,
     645,    36,    37,   505,   307,   309,   241,   146,   239,   313,
     367,   368,   369,   370,   371,   128,   129,   559,   317,   318,
     319,   320,   321,   322,   323,   324,   435,   436,   431,   252,
     253,   384,   147,   385,   386,   387,    55,   246,   446,   247,
     247,    56,   117,    30,   505,   518,   635,   519,   505,    30,
     658,   150,   676,   607,   505,   444,   681,   431,   353,   354,
     449,   450,   539,   484,   485,   486,   487,   152,   464,   488,
     489,   490,   491,   136,   154,   388,   389,   390,   123,   136,
     686,   687,   156,   124,   689,   157,   367,   368,   369,   370,
     371,   505,   506,    60,   545,   546,   624,   625,   608,   158,
     443,   698,   699,   505,   670,   703,   520,   521,   522,   523,
     524,   525,   526,   527,   571,   529,   530,   531,   532,   533,
     534,   535,   536,   537,   538,   256,   372,   373,   374,   375,
     376,   377,   378,   379,   380,   381,   505,   671,   382,   505,
     674,   505,   675,   505,   696,   161,   163,   159,   164,   228,
     234,   636,   235,   637,   236,   640,   641,   444,   243,   245,
     249,   443,   251,   444,   444,   444,   444,   444,   444,   444,
     444,   231,   444,   444,   444,   444,   444,   444,   444,   444,
     444,   444,   257,   259,   618,   126,   260,   261,   622,   578,
     262,   263,   264,   265,   266,   267,   268,   269,   220,    61,
     270,   271,   272,   273,   391,   503,   274,   275,   276,   277,
     567,    61,   278,   279,   280,   659,   682,   281,   444,   684,
     282,   283,   285,   286,   287,   288,   289,   290,   291,   292,
     293,   294,   295,   296,   297,   284,   310,   431,   311,   312,
     314,   437,   655,   439,   298,   299,   453,   492,   513,   448,
      30,   678,   678,   507,   515,   514,   517,   563,   540,   541,
     542,   547,   548,   549,   551,   300,   552,   554,   557,   560,
     464,   315,   555,   556,   569,   301,   561,   688,   573,   302,
     136,   570,   575,   576,   579,   611,   435,   591,   707,   666,
     303,   581,   582,   709,   644,   353,   354,   355,   356,   357,
     358,   359,   583,   584,   664,   668,   585,   125,   586,   220,
     587,   588,   589,   590,   592,   593,   680,   619,   362,   363,
     364,   365,   366,   367,   368,   369,   370,   371,   285,   286,
     287,   288,   289,   290,   291,   292,   293,   294,   295,   296,
     297,   594,   685,   595,   626,   596,   220,   597,   598,   599,
     298,   299,   697,     2,     3,   600,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,   431,
     710,   300,   601,    17,    18,    19,    20,    21,    22,    23,
     602,   301,   603,   604,   605,   302,   669,   606,   612,   353,
     354,   355,   356,   357,   358,   613,   303,   614,   615,    24,
     616,   617,   630,   629,   634,   642,   651,   652,   653,    25,
     239,   667,   672,    26,   364,   365,   366,   367,   368,   369,
     370,   371,   619,   657,    27,   660,   673,   661,   167,   168,
     169,   170,   171,   172,   173,   174,   175,   493,   683,   691,
     505,   695,   692,   444,   176,   693,   694,   706,   494,   248,
     577,   237,   445,   165,   632,   662,   230,   650,    35,   574,
     610,   431,   656,   679,   431,   177,   178,   179,   180,   181,
     182,   305,   183,   184,   185,   186,   187,   188,   189,   190,
     191,   192,   193,   194,   195,     0,   196,   197,   198,     0,
     628,   199,   200,     0,     0,   201,   202,   203,   204,   205,
     206,   207,     0,     0,     0,   208,   209,     0,     0,     0,
       0,     0,     0,     0,   167,   168,   169,   170,   171,   172,
     173,   174,   175,     0,     0,     0,     0,     0,     0,     0,
     176,     0,   210,     0,     0,   211,   212,   213,     0,     0,
       0,     0,     0,     0,   214,   215,     0,   216,   217,     0,
       0,   177,   178,   179,   180,   181,   182,   232,   183,   184,
     185,   186,   187,   188,   189,   190,   191,   192,   193,   194,
     195,     0,   196,   197,   198,     0,     0,   199,   200,     0,
       0,   201,   202,   203,   204,   205,   206,   207,     0,     0,
       0,   208,   209,     0,     0,     0,     0,     0,     0,     0,
     167,   168,   169,   170,   171,   172,   173,   174,   175,     0,
       0,     0,     0,     0,     0,     0,   176,     0,   210,     0,
       0,   211,   212,   213,     0,     0,     0,     0,     0,     0,
     214,   215,     0,   216,   217,     0,     0,   177,   178,   179,
     180,   181,   182,   621,   183,   184,   185,   186,   187,   188,
     189,   190,   191,   192,   193,   194,   195,     0,   196,   197,
     198,     0,     0,   199,   200,     0,     0,   201,   202,   203,
     204,   205,   206,   207,     0,     0,     0,   208,   209,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   353,   354,   355,   356,   357,
     358,     0,     0,     0,   210,     0,     0,   211,   212,   213,
       0,     0,     0,     0,     0,     0,   214,   215,     0,   216,
     217,   365,   366,   367,   368,   369,   370,   371,   392,   663,
     393,   394,   395,   396,   397,   398,   399,   400,   401,    13,
      14,    15,    16,     0,     0,     0,   176,    17,    18,    19,
      20,    21,    22,    23,   402,     0,   403,   404,   405,   406,
     407,   408,   409,   410,   411,   412,   413,   177,   178,   179,
     180,   181,   182,    24,   183,   184,   185,   186,   187,   188,
     189,   190,   191,   414,   193,   194,   195,    26,   196,   197,
     198,     0,     0,   199,   200,     0,     0,   415,   416,   203,
     204,   205,   206,   207,     0,     0,     0,   208,   209,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   210,     0,     0,   211,   212,   213,
       0,     0,     0,     0,     0,     0,   214,   215,     0,   216,
     217,     0,     0,     0,   417,  -202,   239,   392,     0,   393,
     394,   395,   396,   397,   398,   399,   400,   401,    13,    14,
      15,    16,     0,     0,     0,   176,    17,    18,    19,    20,
      21,    22,    23,   402,     0,   403,   404,   405,   406,   407,
     408,   409,   410,   411,   412,   413,   177,   178,   179,   180,
     181,   182,    24,   183,   184,   185,   186,   187,   188,   189,
     190,   191,   414,   193,   194,   195,    26,   196,   197,   198,
       0,     0,   199,   200,     0,     0,   415,   416,   203,   204,
     205,   206,   207,     0,     0,     0,   208,   209,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   210,     0,     0,   211,   212,   213,     0,
       0,     0,     0,     0,     0,   214,   215,     0,   216,   217,
       0,     0,     0,   417,  -203,   239,   392,     0,   393,   394,
     395,   396,   397,   398,   399,   400,   401,    13,    14,    15,
      16,     0,     0,     0,   176,    17,    18,    19,    20,    21,
      22,    23,   402,     0,   403,   404,   405,   406,   407,   408,
     409,   410,   411,   412,   413,   177,   178,   179,   180,   181,
     182,    24,   183,   184,   185,   186,   187,   188,   189,   190,
     191,   414,   193,   194,   195,    26,   196,   197,   198,     0,
       0,   199,   200,     0,     0,   415,   416,   203,   204,   205,
     206,   207,     0,     0,     0,   208,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   167,   168,
     169,   170,   171,   172,   173,   174,   175,     0,     0,     0,
       0,     0,   210,     0,   176,   211,   212,   213,     0,     0,
       0,     0,     0,     0,   214,   215,     0,   216,   217,     0,
       0,     0,   417,     0,   239,   177,   178,   179,   180,   181,
     182,     0,   183,   184,   185,   186,   187,   188,   189,   190,
     191,   192,   193,   194,   195,     0,   196,   197,   198,     0,
       0,   199,   200,   347,     0,   201,   202,   203,   204,   205,
     206,   207,     0,     0,     0,   208,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   167,   168,
     169,   170,   171,   172,   173,   174,   175,     0,     0,     0,
       0,     0,   210,     0,   176,   211,   212,   213,     0,     0,
       0,     0,     0,     0,   214,   215,   348,   216,   217,     0,
       0,     0,     0,   349,   218,   177,   178,   179,   180,   181,
     182,     0,   183,   184,   185,   186,   187,   188,   189,   190,
     191,   192,   193,   194,   195,     0,   196,   197,   198,     0,
       0,   199,   200,   347,     0,   201,   202,   203,   204,   205,
     206,   207,     0,     0,     0,   208,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   167,   168,
     169,   170,   171,   172,   173,   174,   175,     0,     0,     0,
       0,     0,   210,     0,   176,   211,   212,   213,     0,     0,
       0,     0,     0,     0,   214,   215,   348,   216,   217,     0,
       0,     0,     0,   631,   218,   177,   178,   179,   180,   181,
     182,     0,   183,   184,   185,   186,   187,   188,   189,   190,
     191,   192,   193,   194,   195,     0,   196,   197,   198,     0,
       0,   199,   200,     0,     0,   201,   202,   203,   204,   205,
     206,   207,     0,     0,     0,   208,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   210,     0,     0,   211,   212,   213,     0,     0,
       0,     0,     0,     0,   214,   215,     0,   216,   217,     0,
       0,     0,     0,     0,   218,   393,   394,   395,   396,   397,
     398,   399,   400,   401,    13,    14,    15,    16,     0,     0,
       0,   176,    17,    18,    19,    20,    21,    22,    23,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   177,   178,   179,   180,   181,   182,    24,   183,
     184,   185,   186,   187,   188,   189,   190,   191,   414,   193,
     194,   195,    26,   196,   197,   198,     0,     0,   199,   200,
       0,     0,   201,   416,   203,   204,   205,   206,   207,     0,
       0,     0,   208,   209,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   167,   168,   169,   170,   171,   172,
     173,   174,   175,     0,     0,     0,     0,     0,     0,   210,
     176,     0,   211,   212,   213,     0,     0,     0,     0,     0,
       0,   214,   215,     0,   216,   217,     0,     0,     0,   417,
       0,   177,   178,   179,   180,   181,   182,     0,   183,   184,
     185,   186,   187,   188,   189,   190,   191,   192,   193,   194,
     195,     0,   196,   197,   198,     0,     0,   199,   200,     0,
       0,   201,   202,   203,   204,   205,   206,   207,     0,     0,
       0,   208,   209,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   167,   168,   169,   170,   171,   172,   173,
     174,   175,     0,     0,     0,     0,     0,     0,   210,   176,
       0,   211,   212,   213,     0,     0,     0,     0,     0,     0,
     214,   215,     0,   216,   217,     0,     0,     0,   558,     0,
     177,   178,   179,   180,   181,   182,     0,   183,   184,   185,
     186,   187,   188,   189,   190,   191,   192,   193,   194,   195,
       0,   196,   197,   198,     0,     0,   199,   200,     0,     0,
     201,   202,   203,   204,   205,   206,   207,     0,     0,     0,
     208,   209,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   325,   326,   327,   328,   329,   330,   331,   332,
     333,   294,   295,   296,   297,     0,     0,   210,   176,     0,
     211,   212,   213,     0,   298,   299,     0,     0,     0,   214,
     215,     0,   216,   217,     0,     0,     0,   417,     0,   177,
     178,   179,   180,   181,   182,   300,   183,   184,   185,   186,
     187,   188,   189,   190,   191,   334,   193,   194,   195,   302,
     196,   197,   198,     0,     0,   199,   200,     0,     0,   201,
     335,   203,   204,   205,   206,   207,     0,     0,     0,   208,
     209,     0,     0,     0,     0,     0,   167,   168,   169,   170,
     171,   172,   173,   174,   175,     0,     0,     0,     0,     0,
       0,     0,   176,     0,     0,     0,   210,     0,     0,   211,
     212,   213,     0,     0,     0,     0,     0,     0,   214,   215,
       0,   216,   217,   177,   178,   179,   180,   181,   182,     0,
     183,   184,   185,   186,   187,   188,   189,   190,   191,   192,
     193,   194,   195,     0,   196,   197,   198,     0,     0,   199,
     200,     0,     0,   201,   202,   203,   204,   205,   206,   207,
       0,     0,     0,   208,   209,     0,     0,     0,     0,     0,
     167,   168,   169,   170,   171,   172,   173,   174,   175,     0,
       0,     0,     0,     0,     0,     0,   176,     0,     0,     0,
     210,     0,     0,   211,   212,   213,     0,     0,     0,     0,
       0,     0,   214,   215,     0,   216,   217,   177,   178,   179,
     180,   181,   182,     0,   183,   184,   185,   186,   187,   188,
     189,   190,   191,   192,   193,   194,   195,     0,   196,   197,
     198,     0,     0,   199,   200,     0,     0,   201,   202,   203,
     204,   205,   206,   207,     0,     0,     0,   208,   209,     0,
       0,     0,     0,     0,   167,   168,   169,   170,   171,   172,
     173,   174,   175,     0,     0,     0,     0,     0,     0,     0,
     176,     0,     0,     0,   210,     0,     0,   211,   212,   213,
       0,     0,     0,     0,     0,     0,   214,   215,     0,   308,
     217,   177,   178,   179,   180,   181,   182,     0,   183,   184,
     185,   186,   187,   188,   189,   190,   191,   192,   193,   194,
     195,     0,   196,   197,   198,     0,     0,   199,   200,     0,
       0,   201,   202,   203,   204,   205,   206,   207,     0,     0,
       0,   208,   209,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,     0,     0,     0,     0,
      17,    18,    19,    20,    21,    22,    23,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     214,   215,     0,   216,   217,     0,    24,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    25,     0,     0,     0,
      26,   353,   354,   355,   356,    55,     0,     0,     0,   508,
      56,    57,   285,   286,   287,   288,   289,   290,   291,   292,
     293,   294,   295,   296,   297,     0,     0,   365,   366,   367,
     368,   369,   370,   371,   298,   299,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    58,     0,     0,
       0,     0,    59,     0,     0,   300,     0,     0,     0,     0,
       0,     0,    60,   509,     0,   301,     0,     0,     0,   302,
       0,     0,     0,     0,     0,     0,     0,     0,   508,     0,
     303,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,     0,     0,     0,     0,    17,    18,
      19,    20,    21,    22,    23,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    58,     0,     0,     0,
       0,    59,     0,     0,    24,     0,     0,     0,     0,     0,
       0,     0,   509,     0,    25,     0,     0,     0,    26,     0,
       0,     0,     0,    55,     0,     0,     0,     0,    56,    57,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,   130,   131,   132,     0,    17,    18,    19,
      20,    21,    22,    23,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    58,     0,     0,     0,     0,
      59,     0,     0,    24,     0,     0,     0,     0,   176,     0,
      60,     0,     0,    25,     0,     0,     0,    26,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   133,   134,   177,
     178,   179,   180,   181,   182,     0,   183,   184,   185,   186,
     187,   188,   189,   190,   191,     0,   193,   194,   195,     0,
     196,   197,   198,     0,     0,   199,   200,     0,     0,   201,
       0,   203,   204,   205,   206,   207,     0,     0,     0,   208,
     209,     0,     0,     0,     0,     0,     0,   135,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   210,     0,     0,   211,
     212,   213,     0,     0,     0,     0,     0,     0,   214,   215,
       0,   216,   217,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,     0,     0,     0,     0,
      17,    18,    19,    20,    21,    22,    23,     0,     0,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,     0,     0,     0,    24,    17,    18,    19,
      20,    21,    22,    23,     0,     0,    25,     0,     0,     0,
      26,     0,     0,     0,     0,   353,   354,   355,   356,   357,
     358,   134,     0,    24,     0,     0,     0,     0,   649,     0,
       0,     0,     0,    25,     0,     0,     0,    26,   362,   363,
     364,   365,   366,   367,   368,   369,   370,   371,   134,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    89,
      90,    91,    92,    93,    94,    95,    96,    97,    98,     0,
       0,    99,     0,     0,   100,   101,   102,   103,   104,   105,
     106,   107,   108,   109,     0,     0,     0,     0,   110,   111,
       0,   112,   113,   353,   354,   355,   356,   357,   358,   359,
     360,     0,   353,   354,   355,   356,   357,   358,     0,     0,
       0,     0,     0,     0,   361,     0,   362,   363,   364,   365,
     366,   367,   368,   369,   370,   371,   363,   364,   365,   366,
     367,   368,   369,   370,   371
};

static const yytype_int16 yycheck[] =
{
       1,   126,   140,   216,   142,   126,    65,   128,   129,    30,
      30,    73,   258,    75,   339,   405,   431,   347,    79,     1,
     216,    71,   261,   262,   263,   264,   265,   266,   267,   268,
       1,   154,    19,   423,   129,   305,   428,    25,    26,    60,
       1,    70,    71,   510,   102,   284,    70,    71,    30,   270,
     271,   272,   273,   274,   275,   276,   277,   278,   279,   280,
     281,   282,   283,    70,    71,    79,    70,    71,    69,   339,
     120,   129,    73,    64,    75,   314,   104,   316,   408,    65,
      69,    69,   104,    70,    70,    71,    77,    25,    26,   310,
     311,   312,   127,   508,   129,   308,   129,   218,    69,   566,
     129,   129,    73,   112,    75,   129,   431,   129,   122,    79,
     127,    65,   308,   130,   123,   102,    70,    79,   107,   107,
     107,   107,   129,   112,   112,   129,   112,    65,   112,   113,
     114,    69,    70,    71,   123,   123,   122,   138,   130,   260,
     261,   262,   263,   264,   265,   266,   267,   268,   269,   270,
     271,   272,   273,   274,   275,   276,   277,   278,   279,   280,
     281,   282,   283,   284,   554,   361,   127,   138,   389,   107,
     560,   563,   564,   104,   112,    16,    17,    18,    14,    15,
      16,    65,   244,   508,   122,   123,    70,   127,   250,   310,
     311,   312,   438,   314,   390,   316,    25,    26,   245,   130,
     127,   127,   128,   130,   194,   195,   127,   129,   129,   199,
     110,   111,   112,   113,   114,   122,   123,   413,   208,   209,
     210,   211,   212,   213,   214,   215,   130,   131,   229,    70,
      71,    77,    70,    79,    80,    81,    65,   128,   128,   130,
     130,    70,    71,   244,   130,   128,   132,   130,   130,   250,
     132,   129,   642,   492,   130,   245,   132,   258,    82,    83,
      70,    71,   383,    70,    71,    70,    71,   129,   389,    70,
      71,    70,    71,   244,   104,   121,   122,   123,   107,   250,
     670,   671,   122,   112,   674,    71,   110,   111,   112,   113,
     114,   130,   131,   122,   127,   128,   122,   123,   494,   131,
     347,   691,   692,   130,   131,   695,   353,   354,   355,   356,
     357,   358,   359,   360,   435,   362,   363,   364,   365,   366,
     367,   368,   369,   370,   371,   448,    90,    91,    92,    93,
      94,    95,    96,    97,    98,    99,   130,   131,   102,   130,
     131,   130,   131,   130,   131,   115,   116,   132,   131,   129,
     122,   547,    70,   549,   128,   551,   552,   347,   104,   102,
     128,   408,   128,   353,   354,   355,   356,   357,   358,   359,
     360,   492,   362,   363,   364,   365,   366,   367,   368,   369,
     370,   371,   129,   122,   505,   102,   122,   122,   509,   451,
     122,   122,   122,   122,   122,   122,   122,   122,   519,   419,
     122,   122,   122,   122,    75,    70,   122,   122,   122,   122,
     431,   431,   122,   122,   122,   611,   662,   122,   408,   665,
     122,   122,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,   122,   122,   438,   122,   122,
     122,   132,   580,   122,    25,    26,   131,   122,    70,   130,
     451,   647,   648,   131,   130,   132,    70,   428,    70,    70,
      70,   122,   122,   122,   122,    46,   122,   104,    70,   104,
     591,    79,   127,   127,   131,    56,   128,   673,   131,    60,
     451,   130,   128,   128,   131,   123,   130,   130,   701,   627,
      71,   131,   131,   706,   127,    82,    83,    84,    85,    86,
      87,    88,   131,   131,   625,   630,   131,   566,   131,   630,
     131,   131,   131,   131,   131,   131,   654,   507,   105,   106,
     107,   108,   109,   110,   111,   112,   113,   114,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,   131,   667,   131,   122,   131,   667,   131,   131,   131,
      25,    26,   690,     0,     1,   131,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,   570,
     708,    46,   131,    20,    21,    22,    23,    24,    25,    26,
     131,    56,   131,   131,   131,    60,   633,   131,   131,    82,
      83,    84,    85,    86,    87,   131,    71,   131,   131,    46,
     131,   131,   102,   132,   131,   104,   131,   128,   128,    56,
     129,   102,   127,    60,   107,   108,   109,   110,   111,   112,
     113,   114,   612,   131,    71,   131,   122,   132,     3,     4,
       5,     6,     7,     8,     9,    10,    11,   112,   132,   131,
     130,    28,   131,   633,    19,   131,   131,    77,   123,   150,
     448,   138,   247,   120,   519,   624,   128,   570,     1,   440,
     495,   662,   591,   648,   665,    40,    41,    42,    43,    44,
      45,   193,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    -1,    61,    62,    63,    -1,
     515,    66,    67,    -1,    -1,    70,    71,    72,    73,    74,
      75,    76,    -1,    -1,    -1,    80,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      19,    -1,   107,    -1,    -1,   110,   111,   112,    -1,    -1,
      -1,    -1,    -1,    -1,   119,   120,    -1,   122,   123,    -1,
      -1,    40,    41,    42,    43,    44,    45,   132,    47,    48,
      49,    50,    51,    52,    53,    54,    55,    56,    57,    58,
      59,    -1,    61,    62,    63,    -1,    -1,    66,    67,    -1,
      -1,    70,    71,    72,    73,    74,    75,    76,    -1,    -1,
      -1,    80,    81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    19,    -1,   107,    -1,
      -1,   110,   111,   112,    -1,    -1,    -1,    -1,    -1,    -1,
     119,   120,    -1,   122,   123,    -1,    -1,    40,    41,    42,
      43,    44,    45,   132,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    57,    58,    59,    -1,    61,    62,
      63,    -1,    -1,    66,    67,    -1,    -1,    70,    71,    72,
      73,    74,    75,    76,    -1,    -1,    -1,    80,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    82,    83,    84,    85,    86,
      87,    -1,    -1,    -1,   107,    -1,    -1,   110,   111,   112,
      -1,    -1,    -1,    -1,    -1,    -1,   119,   120,    -1,   122,
     123,   108,   109,   110,   111,   112,   113,   114,     1,   132,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    -1,    -1,    -1,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    -1,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    57,    58,    59,    60,    61,    62,
      63,    -1,    -1,    66,    67,    -1,    -1,    70,    71,    72,
      73,    74,    75,    76,    -1,    -1,    -1,    80,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   107,    -1,    -1,   110,   111,   112,
      -1,    -1,    -1,    -1,    -1,    -1,   119,   120,    -1,   122,
     123,    -1,    -1,    -1,   127,   128,   129,     1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    -1,    -1,    -1,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    -1,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    45,    46,    47,    48,    49,    50,    51,    52,    53,
      54,    55,    56,    57,    58,    59,    60,    61,    62,    63,
      -1,    -1,    66,    67,    -1,    -1,    70,    71,    72,    73,
      74,    75,    76,    -1,    -1,    -1,    80,    81,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   107,    -1,    -1,   110,   111,   112,    -1,
      -1,    -1,    -1,    -1,    -1,   119,   120,    -1,   122,   123,
      -1,    -1,    -1,   127,   128,   129,     1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    -1,    -1,    -1,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    -1,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    -1,
      -1,    66,    67,    -1,    -1,    70,    71,    72,    73,    74,
      75,    76,    -1,    -1,    -1,    80,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    -1,   107,    -1,    19,   110,   111,   112,    -1,    -1,
      -1,    -1,    -1,    -1,   119,   120,    -1,   122,   123,    -1,
      -1,    -1,   127,    -1,   129,    40,    41,    42,    43,    44,
      45,    -1,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    -1,    61,    62,    63,    -1,
      -1,    66,    67,    68,    -1,    70,    71,    72,    73,    74,
      75,    76,    -1,    -1,    -1,    80,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    -1,   107,    -1,    19,   110,   111,   112,    -1,    -1,
      -1,    -1,    -1,    -1,   119,   120,   121,   122,   123,    -1,
      -1,    -1,    -1,   128,   129,    40,    41,    42,    43,    44,
      45,    -1,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    -1,    61,    62,    63,    -1,
      -1,    66,    67,    68,    -1,    70,    71,    72,    73,    74,
      75,    76,    -1,    -1,    -1,    80,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    -1,   107,    -1,    19,   110,   111,   112,    -1,    -1,
      -1,    -1,    -1,    -1,   119,   120,   121,   122,   123,    -1,
      -1,    -1,    -1,   128,   129,    40,    41,    42,    43,    44,
      45,    -1,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    -1,    61,    62,    63,    -1,
      -1,    66,    67,    -1,    -1,    70,    71,    72,    73,    74,
      75,    76,    -1,    -1,    -1,    80,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   107,    -1,    -1,   110,   111,   112,    -1,    -1,
      -1,    -1,    -1,    -1,   119,   120,    -1,   122,   123,    -1,
      -1,    -1,    -1,    -1,   129,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    -1,    -1,
      -1,    19,    20,    21,    22,    23,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    40,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    57,
      58,    59,    60,    61,    62,    63,    -1,    -1,    66,    67,
      -1,    -1,    70,    71,    72,    73,    74,    75,    76,    -1,
      -1,    -1,    80,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,   107,
      19,    -1,   110,   111,   112,    -1,    -1,    -1,    -1,    -1,
      -1,   119,   120,    -1,   122,   123,    -1,    -1,    -1,   127,
      -1,    40,    41,    42,    43,    44,    45,    -1,    47,    48,
      49,    50,    51,    52,    53,    54,    55,    56,    57,    58,
      59,    -1,    61,    62,    63,    -1,    -1,    66,    67,    -1,
      -1,    70,    71,    72,    73,    74,    75,    76,    -1,    -1,
      -1,    80,    81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    -1,   107,    19,
      -1,   110,   111,   112,    -1,    -1,    -1,    -1,    -1,    -1,
     119,   120,    -1,   122,   123,    -1,    -1,    -1,   127,    -1,
      40,    41,    42,    43,    44,    45,    -1,    47,    48,    49,
      50,    51,    52,    53,    54,    55,    56,    57,    58,    59,
      -1,    61,    62,    63,    -1,    -1,    66,    67,    -1,    -1,
      70,    71,    72,    73,    74,    75,    76,    -1,    -1,    -1,
      80,    81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    -1,    -1,   107,    19,    -1,
     110,   111,   112,    -1,    25,    26,    -1,    -1,    -1,   119,
     120,    -1,   122,   123,    -1,    -1,    -1,   127,    -1,    40,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      51,    52,    53,    54,    55,    56,    57,    58,    59,    60,
      61,    62,    63,    -1,    -1,    66,    67,    -1,    -1,    70,
      71,    72,    73,    74,    75,    76,    -1,    -1,    -1,    80,
      81,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    19,    -1,    -1,    -1,   107,    -1,    -1,   110,
     111,   112,    -1,    -1,    -1,    -1,    -1,    -1,   119,   120,
      -1,   122,   123,    40,    41,    42,    43,    44,    45,    -1,
      47,    48,    49,    50,    51,    52,    53,    54,    55,    56,
      57,    58,    59,    -1,    61,    62,    63,    -1,    -1,    66,
      67,    -1,    -1,    70,    71,    72,    73,    74,    75,    76,
      -1,    -1,    -1,    80,    81,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    19,    -1,    -1,    -1,
     107,    -1,    -1,   110,   111,   112,    -1,    -1,    -1,    -1,
      -1,    -1,   119,   120,    -1,   122,   123,    40,    41,    42,
      43,    44,    45,    -1,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    57,    58,    59,    -1,    61,    62,
      63,    -1,    -1,    66,    67,    -1,    -1,    70,    71,    72,
      73,    74,    75,    76,    -1,    -1,    -1,    80,    81,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      19,    -1,    -1,    -1,   107,    -1,    -1,   110,   111,   112,
      -1,    -1,    -1,    -1,    -1,    -1,   119,   120,    -1,   122,
     123,    40,    41,    42,    43,    44,    45,    -1,    47,    48,
      49,    50,    51,    52,    53,    54,    55,    56,    57,    58,
      59,    -1,    61,    62,    63,    -1,    -1,    66,    67,    -1,
      -1,    70,    71,    72,    73,    74,    75,    76,    -1,    -1,
      -1,    80,    81,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    -1,    -1,    -1,    -1,
      20,    21,    22,    23,    24,    25,    26,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     119,   120,    -1,   122,   123,    -1,    46,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    56,    -1,    -1,    -1,
      60,    82,    83,    84,    85,    65,    -1,    -1,    -1,    69,
      70,    71,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    -1,    -1,   108,   109,   110,
     111,   112,   113,   114,    25,    26,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   107,    -1,    -1,
      -1,    -1,   112,    -1,    -1,    46,    -1,    -1,    -1,    -1,
      -1,    -1,   122,   123,    -1,    56,    -1,    -1,    -1,    60,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    69,    -1,
      71,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    -1,    -1,    -1,    -1,    20,    21,
      22,    23,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   107,    -1,    -1,    -1,
      -1,   112,    -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   123,    -1,    56,    -1,    -1,    -1,    60,    -1,
      -1,    -1,    -1,    65,    -1,    -1,    -1,    -1,    70,    71,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    18,    -1,    20,    21,    22,
      23,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   107,    -1,    -1,    -1,    -1,
     112,    -1,    -1,    46,    -1,    -1,    -1,    -1,    19,    -1,
     122,    -1,    -1,    56,    -1,    -1,    -1,    60,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    70,    71,    40,
      41,    42,    43,    44,    45,    -1,    47,    48,    49,    50,
      51,    52,    53,    54,    55,    -1,    57,    58,    59,    -1,
      61,    62,    63,    -1,    -1,    66,    67,    -1,    -1,    70,
      -1,    72,    73,    74,    75,    76,    -1,    -1,    -1,    80,
      81,    -1,    -1,    -1,    -1,    -1,    -1,   120,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   107,    -1,    -1,   110,
     111,   112,    -1,    -1,    -1,    -1,    -1,    -1,   119,   120,
      -1,   122,   123,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    -1,    -1,    -1,    -1,
      20,    21,    22,    23,    24,    25,    26,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    -1,    -1,    -1,    46,    20,    21,    22,
      23,    24,    25,    26,    -1,    -1,    56,    -1,    -1,    -1,
      60,    -1,    -1,    -1,    -1,    82,    83,    84,    85,    86,
      87,    71,    -1,    46,    -1,    -1,    -1,    -1,    78,    -1,
      -1,    -1,    -1,    56,    -1,    -1,    -1,    60,   105,   106,
     107,   108,   109,   110,   111,   112,   113,   114,    71,    80,
      81,    82,    83,    84,    85,    86,    87,    88,    89,    90,
      91,    92,    93,    94,    95,    96,    97,    98,    99,    -1,
      -1,   102,    -1,    -1,   105,   106,   107,   108,   109,   110,
     111,   112,   113,   114,    -1,    -1,    -1,    -1,   119,   120,
      -1,   122,   123,    82,    83,    84,    85,    86,    87,    88,
      89,    -1,    82,    83,    84,    85,    86,    87,    -1,    -1,
      -1,    -1,    -1,    -1,   103,    -1,   105,   106,   107,   108,
     109,   110,   111,   112,   113,   114,   106,   107,   108,   109,
     110,   111,   112,   113,   114
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   134,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    20,    21,    22,
      23,    24,    25,    26,    46,    56,    60,    71,   135,   136,
     137,   138,   139,   141,   164,   189,   127,   128,    70,    71,
     129,   140,    70,    71,   129,   140,    70,    71,   129,   140,
      70,    71,   129,   140,    79,    65,    70,    71,   107,   112,
     122,   138,   171,   172,   173,   177,   178,   181,   182,   144,
     142,   152,   151,   147,   145,   150,   148,    71,   120,    80,
      81,    82,    83,    84,    85,    86,    87,    88,    89,    90,
      91,    92,    93,    94,    95,    96,    97,    98,    99,   102,
     105,   106,   107,   108,   109,   110,   111,   112,   113,   114,
     119,   120,   122,   123,   183,    79,    79,    71,   178,   127,
     130,    25,    26,   107,   112,   181,   102,   190,   122,   123,
      16,    17,    18,    70,    71,   120,   136,   153,   157,   158,
     159,   161,   162,   163,   168,   189,   129,    70,   169,   170,
     129,   153,   129,   153,   104,   154,   122,    71,   131,   132,
      70,   182,    70,   182,   131,   173,   178,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    19,    40,    41,    42,
      43,    44,    45,    47,    48,    49,    50,    51,    52,    53,
      54,    55,    56,    57,    58,    59,    61,    62,    63,    66,
      67,    70,    71,    72,    73,    74,    75,    76,    80,    81,
     107,   110,   111,   112,   119,   120,   122,   123,   129,   174,
     205,   208,   209,   216,   217,   222,   223,   224,   129,   184,
     185,   205,   132,   205,   122,    70,   128,   158,   127,   129,
     192,   127,   192,   104,   143,   102,   128,   130,   169,   128,
     146,   128,    70,    71,   155,   156,   168,   129,   165,   122,
     122,   122,   122,   122,   122,   122,   122,   122,   122,   122,
     122,   122,   122,   122,   122,   122,   122,   122,   122,   122,
     122,   122,   122,   122,   122,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    25,    26,
      46,    56,    60,    71,   211,   214,   215,   209,   122,   209,
     122,   122,   122,   209,   122,    79,   122,   209,   209,   209,
     209,   209,   209,   209,   209,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    56,    71,   204,   205,   210,   214,
      19,    70,   102,   107,   229,   230,   231,    68,   121,   128,
     174,   175,   176,    82,    83,    84,    85,    86,    87,    88,
      89,   103,   105,   106,   107,   108,   109,   110,   111,   112,
     113,   114,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   102,   206,    77,    79,    80,    81,   121,   122,
     123,    75,     1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    27,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    56,    70,    71,   127,   136,   137,
     191,   192,   194,   195,   196,   197,   199,   200,   201,   203,
     204,   137,   186,   187,   188,   130,   131,   132,   160,   122,
     193,   153,   207,   208,   209,   170,   128,   153,   130,    70,
      71,   149,   186,   131,   185,   218,   218,   218,   218,   218,
     218,   218,   218,   218,   205,   210,   219,   220,   221,   219,
     219,   219,   219,   219,   219,   219,   219,   219,   219,   219,
     219,   219,   219,   218,    70,    71,    70,    71,    70,    71,
      70,    71,   122,   112,   123,   212,   213,   215,   210,   219,
     219,   219,   218,    70,   218,   130,   131,   131,    69,   123,
     177,   179,   180,    70,   132,   130,   207,    70,   128,   130,
     208,   208,   208,   208,   208,   208,   208,   208,   204,   208,
     208,   208,   208,   208,   208,   208,   208,   208,   208,   205,
      70,    70,    70,   219,   204,   127,   128,   122,   122,   122,
     191,   122,   122,   207,   104,   127,   127,    70,   127,   204,
     104,   128,   191,   136,   196,   127,   177,   178,   179,   131,
     130,   205,   186,   131,   194,   128,   128,   156,   153,   131,
     167,   131,   131,   131,   131,   131,   131,   131,   131,   131,
     131,   130,   131,   131,   131,   131,   131,   131,   131,   131,
     131,   131,   131,   131,   131,   131,   131,   218,   204,   112,
     213,   123,   131,   131,   131,   131,   131,   131,   205,   209,
     179,   132,   205,   180,   122,   123,   122,   227,   231,   132,
     102,   128,   176,   104,   131,   132,   204,   204,     1,    30,
     204,   204,   104,   191,   127,   127,   191,   196,   196,    78,
     188,   131,   128,   128,   166,   192,   221,   131,   132,   204,
     131,   132,   184,   132,   205,   225,   192,   102,   174,   208,
     131,   131,   127,   122,   131,   131,   191,   202,   204,   202,
     192,   132,   186,   132,   186,   174,   191,   191,   204,   191,
     198,   131,   131,   131,   131,    28,   131,   192,   191,   191,
      64,    77,   228,   191,     1,   127,    77,   210,   226,   210,
     192
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   133,   134,   134,   135,   135,   135,   135,   135,   136,
     137,   137,   138,   138,   138,   138,   138,   138,   138,   138,
     139,   139,   139,   139,   139,   139,   139,   139,   139,   139,
     139,   139,   139,   139,   140,   140,   142,   143,   141,   144,
     141,   141,   141,   145,   146,   141,   147,   141,   141,   141,
     148,   149,   141,   150,   141,   141,   141,   151,   141,   152,
     141,   141,   141,   153,   153,   154,   154,   155,   155,   156,
     156,   156,   156,   157,   157,   158,   158,   158,   158,   158,
     160,   159,   161,   161,   162,   163,   163,   165,   166,   164,
     167,   164,   168,   168,   168,   169,   169,   170,   170,   171,
     171,   172,   172,   173,   173,   174,   174,   174,   174,   175,
     175,   176,   176,   176,   177,   177,   177,   177,   177,   177,
     178,   178,   179,   179,   179,   180,   180,   180,   180,   180,
     180,   181,   181,   181,   181,   181,   181,   181,   181,   181,
     181,   181,   182,   183,   183,   183,   183,   183,   183,   183,
     183,   183,   183,   183,   183,   183,   183,   183,   183,   183,
     183,   183,   183,   183,   183,   183,   183,   183,   183,   183,
     183,   183,   183,   183,   183,   183,   183,   183,   184,   185,
     185,   186,   186,   187,   187,   187,   188,   188,   188,   190,
     189,   191,   191,   191,   191,   191,   191,   191,   191,   191,
     193,   192,   194,   194,   195,   195,   196,   196,   197,   197,
     198,   197,   199,   199,   199,   200,   200,   200,   200,   200,
     200,   200,   201,   202,   202,   203,   203,   203,   203,   203,
     204,   204,   205,   205,   206,   206,   206,   206,   206,   206,
     206,   206,   206,   206,   206,   207,   208,   208,   208,   208,
     208,   208,   208,   208,   208,   208,   208,   208,   208,   208,
     208,   208,   208,   208,   208,   208,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   210,   210,   211,   211,   211,   211,   212,   212,
     213,   213,   214,   214,   215,   215,   215,   215,   215,   215,
     215,   215,   215,   215,   215,   215,   215,   215,   215,   215,
     215,   215,   215,   215,   215,   215,   215,   216,   216,   216,
     216,   216,   216,   216,   216,   216,   217,   217,   217,   217,
     217,   217,   217,   217,   217,   217,   217,   217,   217,   217,
     217,   217,   217,   217,   218,   218,   219,   219,   220,   220,
     221,   221,   222,   222,   222,   222,   222,   222,   222,   222,
     222,   222,   222,   222,   222,   222,   222,   222,   222,   222,
     222,   222,   222,   222,   223,   223,   225,   226,   224,   227,
     224,   228,   228,   228,   228,   229,   229,   230,   230,   231,
     231,   231,   231,   231
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     0,     0,     7,     0,
       5,     2,     2,     0,     0,     7,     0,     5,     2,     2,
       0,     0,     8,     0,     5,     2,     2,     0,     6,     0,
       5,     2,     2,     0,     1,     0,     2,     1,     3,     2,
       2,     1,     1,     1,     2,     1,     1,     2,     1,     1,
       0,     5,     2,     2,     4,     2,     2,     0,     0,     9,
       0,     8,     1,     1,     1,     1,     3,     1,     3,     0,
       1,     1,     3,     1,     3,     1,     2,     3,     4,     1,
       3,     1,     4,     5,     1,     1,     2,     2,     2,     2,
       2,     1,     1,     2,     1,     3,     2,     3,     3,     4,
       5,     1,     3,     3,     3,     1,     3,     3,     5,     4,
       3,     4,     2,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     2,     2,     0,     1,
       3,     0,     1,     1,     3,     3,     2,     2,     1,     0,
       6,     1,     1,     1,     1,     1,     1,     1,     2,     2,
       0,     4,     0,     1,     1,     2,     1,     2,     5,     7,
       0,     6,     4,     3,     3,     5,     7,     7,     4,     5,
       6,     6,     2,     0,     1,     2,     2,     2,     3,     3,
       1,     3,     1,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     5,     1,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     4,     2,     4,     2,     5,
       2,     2,     1,     2,     1,     2,     2,     3,     1,     2,
       3,     4,     2,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     2,
       2,     2,     2,     2,     2,     2,     2,     1,     4,     4,
       3,     3,     3,     2,     2,     1,     4,     4,     4,     4,
       4,     4,     4,     4,     4,     4,     4,     4,     4,     4,
       4,     4,     4,     4,     0,     1,     0,     1,     1,     3,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     4,
       4,     4,     4,     4,     4,     4,     4,     4,     4,     4,
       4,     3,     3,     1,     1,     2,     0,     0,    10,     0,
       5,     0,     1,     2,     3,     0,     1,     1,     3,     1,
       2,     1,     1,     1
};


enum { YYENOMEM = -2 };

#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab
#define YYNOMEM         goto yyexhaustedlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Backward compatibility with an undocumented macro.
   Use YYerror or YYUNDEF. */
#define YYERRCODE YYUNDEF

/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)                                \
    do                                                                  \
      if (N)                                                            \
        {                                                               \
          (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;        \
          (Current).first_column = YYRHSLOC (Rhs, 1).first_column;      \
          (Current).last_line    = YYRHSLOC (Rhs, N).last_line;         \
          (Current).last_column  = YYRHSLOC (Rhs, N).last_column;       \
        }                                                               \
      else                                                              \
        {                                                               \
          (Current).first_line   = (Current).last_line   =              \
            YYRHSLOC (Rhs, 0).last_line;                                \
          (Current).first_column = (Current).last_column =              \
            YYRHSLOC (Rhs, 0).last_column;                              \
        }                                                               \
    while (0)
#endif

#define YYRHSLOC(Rhs, K) ((Rhs)[K])


/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)


/* YYLOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

# ifndef YYLOCATION_PRINT

#  if defined YY_LOCATION_PRINT

   /* Temporary convenience wrapper in case some people defined the
      undocumented and private YY_LOCATION_PRINT macros.  */
#   define YYLOCATION_PRINT(File, Loc)  YY_LOCATION_PRINT(File, *(Loc))

#  elif defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL

/* Print *YYLOCP on YYO.  Private, do not rely on its existence. */

YY_ATTRIBUTE_UNUSED
static int
yy_location_print_ (FILE *yyo, YYLTYPE const * const yylocp)
{
  int res = 0;
  int end_col = 0 != yylocp->last_column ? yylocp->last_column - 1 : 0;
  if (0 <= yylocp->first_line)
    {
      res += YYFPRINTF (yyo, "%d", yylocp->first_line);
      if (0 <= yylocp->first_column)
        res += YYFPRINTF (yyo, ".%d", yylocp->first_column);
    }
  if (0 <= yylocp->last_line)
    {
      if (yylocp->first_line < yylocp->last_line)
        {
          res += YYFPRINTF (yyo, "-%d", yylocp->last_line);
          if (0 <= end_col)
            res += YYFPRINTF (yyo, ".%d", end_col);
        }
      else if (0 <= end_col && yylocp->first_column < end_col)
        res += YYFPRINTF (yyo, "-%d", end_col);
    }
  return res;
}

#   define YYLOCATION_PRINT  yy_location_print_

    /* Temporary convenience wrapper in case some people defined the
       undocumented and private YY_LOCATION_PRINT macros.  */
#   define YY_LOCATION_PRINT(File, Loc)  YYLOCATION_PRINT(File, &(Loc))

#  else

#   define YYLOCATION_PRINT(File, Loc) ((void) 0)
    /* Temporary convenience wrapper in case some people defined the
       undocumented and private YY_LOCATION_PRINT macros.  */
#   define YY_LOCATION_PRINT  YYLOCATION_PRINT

#  endif
# endif /* !defined YYLOCATION_PRINT */


# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Kind, Value, Location); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo,
                       yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep, YYLTYPE const * const yylocationp)
{
  FILE *yyoutput = yyo;
  YY_USE (yyoutput);
  YY_USE (yylocationp);
  if (!yyvaluep)
    return;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo,
                 yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep, YYLTYPE const * const yylocationp)
{
  YYFPRINTF (yyo, "%s %s (",
             yykind < YYNTOKENS ? "token" : "nterm", yysymbol_name (yykind));

  YYLOCATION_PRINT (yyo, yylocationp);
  YYFPRINTF (yyo, ": ");
  yy_symbol_value_print (yyo, yykind, yyvaluep, yylocationp);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp, YYLTYPE *yylsp,
                 int yyrule)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       YY_ACCESSING_SYMBOL (+yyssp[yyi + 1 - yynrhs]),
                       &yyvsp[(yyi + 1) - (yynrhs)],
                       &(yylsp[(yyi + 1) - (yynrhs)]));
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, yylsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args) ((void) 0)
# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


/* Context of a parse error.  */
typedef struct
{
  yy_state_t *yyssp;
  yysymbol_kind_t yytoken;
  YYLTYPE *yylloc;
} yypcontext_t;

/* Put in YYARG at most YYARGN of the expected tokens given the
   current YYCTX, and return the number of tokens stored in YYARG.  If
   YYARG is null, return the number of expected tokens (guaranteed to
   be less than YYNTOKENS).  Return YYENOMEM on memory exhaustion.
   Return 0 if there are more than YYARGN expected tokens, yet fill
   YYARG up to YYARGN. */
static int
yypcontext_expected_tokens (const yypcontext_t *yyctx,
                            yysymbol_kind_t yyarg[], int yyargn)
{
  /* Actual size of YYARG. */
  int yycount = 0;
  int yyn = yypact[+*yyctx->yyssp];
  if (!yypact_value_is_default (yyn))
    {
      /* Start YYX at -YYN if negative to avoid negative indexes in
         YYCHECK.  In other words, skip the first -YYN actions for
         this state because they are default actions.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;
      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yyx;
      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
        if (yycheck[yyx + yyn] == yyx && yyx != YYSYMBOL_YYerror
            && !yytable_value_is_error (yytable[yyx + yyn]))
          {
            if (!yyarg)
              ++yycount;
            else if (yycount == yyargn)
              return 0;
            else
              yyarg[yycount++] = YY_CAST (yysymbol_kind_t, yyx);
          }
    }
  if (yyarg && yycount == 0 && 0 < yyargn)
    yyarg[0] = YYSYMBOL_YYEMPTY;
  return yycount;
}




#ifndef yystrlen
# if defined __GLIBC__ && defined _STRING_H
#  define yystrlen(S) (YY_CAST (YYPTRDIFF_T, strlen (S)))
# else
/* Return the length of YYSTR.  */
static YYPTRDIFF_T
yystrlen (const char *yystr)
{
  YYPTRDIFF_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
# endif
#endif

#ifndef yystpcpy
# if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#  define yystpcpy stpcpy
# else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
# endif
#endif

#ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYPTRDIFF_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYPTRDIFF_T yyn = 0;
      char const *yyp = yystr;
      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            else
              goto append;

          append:
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (yyres)
    return yystpcpy (yyres, yystr) - yyres;
  else
    return yystrlen (yystr);
}
#endif


static int
yy_syntax_error_arguments (const yypcontext_t *yyctx,
                           yysymbol_kind_t yyarg[], int yyargn)
{
  /* Actual size of YYARG. */
  int yycount = 0;
  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yyctx->yytoken != YYSYMBOL_YYEMPTY)
    {
      int yyn;
      if (yyarg)
        yyarg[yycount] = yyctx->yytoken;
      ++yycount;
      yyn = yypcontext_expected_tokens (yyctx,
                                        yyarg ? yyarg + 1 : yyarg, yyargn - 1);
      if (yyn == YYENOMEM)
        return YYENOMEM;
      else
        yycount += yyn;
    }
  return yycount;
}

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return -1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return YYENOMEM if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYPTRDIFF_T *yymsg_alloc, char **yymsg,
                const yypcontext_t *yyctx)
{
  enum { YYARGS_MAX = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat: reported tokens (one for the "unexpected",
     one per "expected"). */
  yysymbol_kind_t yyarg[YYARGS_MAX];
  /* Cumulated lengths of YYARG.  */
  YYPTRDIFF_T yysize = 0;

  /* Actual size of YYARG. */
  int yycount = yy_syntax_error_arguments (yyctx, yyarg, YYARGS_MAX);
  if (yycount == YYENOMEM)
    return YYENOMEM;

  switch (yycount)
    {
#define YYCASE_(N, S)                       \
      case N:                               \
        yyformat = S;                       \
        break
    default: /* Avoid compiler warnings. */
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
#undef YYCASE_
    }

  /* Compute error message size.  Don't count the "%s"s, but reserve
     room for the terminator.  */
  yysize = yystrlen (yyformat) - 2 * yycount + 1;
  {
    int yyi;
    for (yyi = 0; yyi < yycount; ++yyi)
      {
        YYPTRDIFF_T yysize1
          = yysize + yytnamerr (YY_NULLPTR, yytname[yyarg[yyi]]);
        if (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM)
          yysize = yysize1;
        else
          return YYENOMEM;
      }
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return -1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yytname[yyarg[yyi++]]);
          yyformat += 2;
        }
      else
        {
          ++yyp;
          ++yyformat;
        }
  }
  return 0;
}


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg,
            yysymbol_kind_t yykind, YYSTYPE *yyvaluep, YYLTYPE *yylocationp)
{
  YY_USE (yyvaluep);
  YY_USE (yylocationp);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yykind, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/* Lookahead token kind.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Location data for the lookahead symbol.  */
YYLTYPE yylloc
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
  = { 1, 1, 1, 1 }
# endif
;
/* Number of syntax errors so far.  */
int yynerrs;




/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    yy_state_fast_t yystate = 0;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus = 0;

    /* Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* Their size.  */
    YYPTRDIFF_T yystacksize = YYINITDEPTH;

    /* The state stack: array, bottom, top.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss = yyssa;
    yy_state_t *yyssp = yyss;

    /* The semantic value stack: array, bottom, top.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs = yyvsa;
    YYSTYPE *yyvsp = yyvs;

    /* The location stack: array, bottom, top.  */
    YYLTYPE yylsa[YYINITDEPTH];
    YYLTYPE *yyls = yylsa;
    YYLTYPE *yylsp = yyls;

  int yyn;
  /* The return value of yyparse.  */
  int yyresult;
  /* Lookahead symbol kind.  */
  yysymbol_kind_t yytoken = YYSYMBOL_YYEMPTY;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;
  YYLTYPE yyloc;

  /* The locations where the error started and ended.  */
  YYLTYPE yyerror_range[3];

  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYPTRDIFF_T yymsg_alloc = sizeof yymsgbuf;

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N), yylsp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yychar = YYEMPTY; /* Cause a token to be read.  */

  yylsp[0] = yylloc;
  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END
  YY_STACK_PRINT (yyss, yyssp);

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    YYNOMEM;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;
        YYLTYPE *yyls1 = yyls;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yyls1, yysize * YYSIZEOF (*yylsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
        yyls = yyls1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        YYNOMEM;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          YYNOMEM;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
        YYSTACK_RELOCATE (yyls_alloc, yyls);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;
      yylsp = yyls + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */


  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either empty, or end-of-input, or a valid lookahead.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token\n"));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = YYEOF;
      yytoken = YYSYMBOL_YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else if (yychar == YYerror)
    {
      /* The scanner already issued an error message, process directly
         to error recovery.  But do not keep the error token as
         lookahead, it is too special and may lead us to an endless
         loop in error recovery. */
      yychar = YYUNDEF;
      yytoken = YYSYMBOL_YYerror;
      yyerror_range[1] = yylloc;
      goto yyerrlab1;
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END
  *++yylsp = yylloc;

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];

  /* Default location. */
  YYLLOC_DEFAULT (yyloc, (yylsp - yylen), yylen);
  yyerror_range[1] = yyloc;
  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
  case 2: /* translation_unit: %empty  */
#line 152 "../phase2-parser/src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2675 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 156 "../phase2-parser/src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2685 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 164 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2691 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 165 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2697 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 166 "../phase2-parser/src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2703 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 167 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2709 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 168 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2715 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 172 "../phase2-parser/src/parser.y"
                                                          {
          endDeclaratorList();
          std::vector<ASTNodePtr> declNodes;
          for (auto &d : yyvsp[-1].paramList) {
              auto n = registerDeclarator(d, yyvsp[-2].typeSpec);
              if (n) declNodes.push_back(n);
          }
          if (declNodes.empty()) {
              yyval.node = yyvsp[-2].node; /* bare struct/class/enum/union declaration */
              /* `union { int i; float f; };` inside a struct: its members
                 are the enclosing struct's (an anonymous member) */
              if (isAnonymousTag(yyvsp[-2].typeSpec.tagName) && yyvsp[-2].node) {
                  if (atAggregateMemberLevel()) {
                      addAnonymousMember(currentClassName(), yyvsp[-2].typeSpec.tagName);
                  } else if (yyvsp[-2].node->kind == ASTKind::UnionDecl) {
                      /* `union { int a; char b; };` in a function (or `static`
                         at file scope): a and b are names in this scope */
                      promoteAnonymousMembers(yyvsp[-2].typeSpec.tagName);
                  }
                  /* `static union {...};`: phase 2b needs the storage class */
                  yyvsp[-2].node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, DeclInfo());
              }
          } else if (declNodes.size() == 1 && !yyvsp[-2].node) {
              yyval.node = declNodes[0];
          } else {
              auto grp = mkNode(ASTKind::DeclGroup);
              if (yyvsp[-2].node) addChild(grp, yyvsp[-2].node);
              for (auto &n : declNodes) addChild(grp, n);
              yyval.node = grp;
          }
      }
#line 2751 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 206 "../phase2-parser/src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          if (yyvsp[0].typeSpec.isExtern) yyval.typeSpec.isExtern = true;
          if (yyvsp[0].typeSpec.isRegister) yyval.typeSpec.isRegister = true;
          yyval.typeSpec.storageClasses += yyvsp[0].typeSpec.storageClasses;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isVolatile) yyval.typeSpec.isVolatile = true;
          if (yyvsp[0].typeSpec.isAuto) yyval.typeSpec.isAuto = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2771 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 221 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2777 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 225 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2783 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: EXTERN  */
#line 226 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isExtern = true; yyval.typeSpec.storageClasses = 1; }
#line 2789 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: REGISTER  */
#line 227 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isRegister = true; yyval.typeSpec.storageClasses = 1; }
#line 2795 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: AUTO  */
#line 228 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2801 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: TYPEDEF  */
#line 229 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2807 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: CONST  */
#line 230 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2813 "build/parser.tab.cpp"
    break;

  case 18: /* storage_or_type_specifier: VOLATILE  */
#line 231 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isVolatile = true; }
#line 2819 "build/parser.tab.cpp"
    break;

  case 19: /* storage_or_type_specifier: type_specifier  */
#line 232 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2825 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: INT  */
#line 236 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2831 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: CHAR  */
#line 237 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2837 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: FLOAT  */
#line 238 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2843 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: DOUBLE  */
#line 239 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2849 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: VOID  */
#line 240 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2855 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: BOOL  */
#line 241 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2861 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SHORT  */
#line 242 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2867 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: LONG  */
#line 243 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2873 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: SIGNED  */
#line 244 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2879 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: UNSIGNED  */
#line 245 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2885 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: FILE_KW  */
#line 246 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FILE"); g_afterTypeKeyword = true; }
#line 2891 "build/parser.tab.cpp"
    break;

  case 31: /* type_specifier: VA_LIST  */
#line 247 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2897 "build/parser.tab.cpp"
    break;

  case 32: /* type_specifier: TYPE_NAME  */
#line 248 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
          if (s && (s->kind == SymKind::STRUCT_TAG || s->kind == SymKind::UNION_TAG ||
                    s->kind == SymKind::CLASS_TAG)) {
              yyval.typeSpec.tagName = yyvsp[0].str; /* "Dog d;" -- Dog referenced directly,
                                                without repeating class/struct */
          } else if (s && s->kind == SymKind::TYPEDEF_NAME && s->typeExpr && s->typeExpr->pointerLevel == 0 &&
                     s->typeExpr->arrayDims.empty() && !s->typeExpr->isFunction &&
                     !s->typeExpr->isFunctionPointer) {
              yyval.typeSpec.tagName = s->typeExpr->tagName; /* `Pt p;` with `typedef struct {...} Pt;`:
                                                              p.x resolves through the struct */
          }
      }
#line 2918 "build/parser.tab.cpp"
    break;

  case 33: /* type_specifier: struct_or_class_specifier  */
#line 264 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2924 "build/parser.tab.cpp"
    break;

  case 34: /* tag_name: IDENTIFIER  */
#line 271 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2930 "build/parser.tab.cpp"
    break;

  case 35: /* tag_name: TYPE_NAME  */
#line 272 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2936 "build/parser.tab.cpp"
    break;

  case 36: /* $@1: %empty  */
#line 276 "../phase2-parser/src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2946 "build/parser.tab.cpp"
    break;

  case 37: /* $@2: %empty  */
#line 280 "../phase2-parser/src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2952 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 280 "../phase2-parser/src/parser.y"
                                                                                                    {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str); /* usable as a type from here on, but
                                             NOT inside its own body -- lets
                                             constructors/destructors keep
                                             matching the class's own name as
                                             a plain IDENTIFIER */
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2970 "build/parser.tab.cpp"
    break;

  case 39: /* @3: %empty  */
#line 296 "../phase2-parser/src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2982 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 302 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2995 "build/parser.tab.cpp"
    break;

  case 41: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 310 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3006 "build/parser.tab.cpp"
    break;

  case 42: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 316 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3017 "build/parser.tab.cpp"
    break;

  case 43: /* $@4: %empty  */
#line 322 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "UNION");
          enterClass(yyvsp[0].str, "union");
      }
#line 3027 "build/parser.tab.cpp"
    break;

  case 44: /* $@5: %empty  */
#line 326 "../phase2-parser/src/parser.y"
            { pushScope("union " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 3033 "build/parser.tab.cpp"
    break;

  case 45: /* struct_or_class_specifier: UNION tag_name $@4 '{' $@5 member_decl_list_opt '}'  */
#line 326 "../phase2-parser/src/parser.y"
                                                                                                   {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::UnionDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 3047 "build/parser.tab.cpp"
    break;

  case 46: /* @6: %empty  */
#line 335 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "union");
          pushScope("union " + yyval.str);
          markAggregateMemberDepth();
      }
#line 3059 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: UNION '{' @6 member_decl_list_opt '}'  */
#line 341 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::UnionDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 3072 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: UNION IDENTIFIER  */
#line 349 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3083 "build/parser.tab.cpp"
    break;

  case 49: /* struct_or_class_specifier: UNION TYPE_NAME  */
#line 355 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3094 "build/parser.tab.cpp"
    break;

  case 50: /* $@7: %empty  */
#line 361 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 3104 "build/parser.tab.cpp"
    break;

  case 51: /* $@8: %empty  */
#line 365 "../phase2-parser/src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 3110 "build/parser.tab.cpp"
    break;

  case 52: /* struct_or_class_specifier: CLASS tag_name $@7 inheritance_opt '{' $@8 member_decl_list_opt '}'  */
#line 365 "../phase2-parser/src/parser.y"
                                                                                                                   {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-6].str;
          addTypeName(yyvsp[-6].str);
          std::string label = yyvsp[-6].str;
          if (!yyvsp[-4].str.empty()) label += " : " + yyvsp[-4].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, label), yyvsp[-6].idx);
          node->bases = yyvsp[-4].bases;
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 3127 "build/parser.tab.cpp"
    break;

  case 53: /* @9: %empty  */
#line 377 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 3139 "build/parser.tab.cpp"
    break;

  case 54: /* struct_or_class_specifier: CLASS '{' @9 member_decl_list_opt '}'  */
#line 383 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 3152 "build/parser.tab.cpp"
    break;

  case 55: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 391 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3163 "build/parser.tab.cpp"
    break;

  case 56: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 397 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3174 "build/parser.tab.cpp"
    break;

  case 57: /* $@10: %empty  */
#line 403 "../phase2-parser/src/parser.y"
                    {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM");
      }
#line 3183 "build/parser.tab.cpp"
    break;

  case 58: /* struct_or_class_specifier: ENUM tag_name $@10 '{' enumerator_list '}'  */
#line 406 "../phase2-parser/src/parser.y"
                                {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-4].str;
          addTypeName(yyvsp[-4].str);
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-4].str), yyvsp[-4].idx);
          for (auto &e : yyvsp[-1].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 3196 "build/parser.tab.cpp"
    break;

  case 59: /* @11: %empty  */
#line 414 "../phase2-parser/src/parser.y"
               {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[-1].idx});
      }
#line 3205 "build/parser.tab.cpp"
    break;

  case 60: /* struct_or_class_specifier: ENUM '{' @11 enumerator_list '}'  */
#line 417 "../phase2-parser/src/parser.y"
                            {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &e : yyvsp[-1].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 3217 "build/parser.tab.cpp"
    break;

  case 61: /* struct_or_class_specifier: ENUM IDENTIFIER  */
#line 424 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3228 "build/parser.tab.cpp"
    break;

  case 62: /* struct_or_class_specifier: ENUM TYPE_NAME  */
#line 430 "../phase2-parser/src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3239 "build/parser.tab.cpp"
    break;

  case 63: /* member_decl_list_opt: %empty  */
#line 439 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3245 "build/parser.tab.cpp"
    break;

  case 64: /* member_decl_list_opt: member_decl_list  */
#line 440 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 3251 "build/parser.tab.cpp"
    break;

  case 65: /* inheritance_opt: %empty  */
#line 444 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3257 "build/parser.tab.cpp"
    break;

  case 66: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 445 "../phase2-parser/src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 3263 "build/parser.tab.cpp"
    break;

  case 67: /* inheritance_specifier_list: inheritance_specifier  */
#line 449 "../phase2-parser/src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 3269 "build/parser.tab.cpp"
    break;

  case 68: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 450 "../phase2-parser/src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 3278 "build/parser.tab.cpp"
    break;

  case 69: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 457 "../phase2-parser/src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3289 "build/parser.tab.cpp"
    break;

  case 70: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 463 "../phase2-parser/src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3300 "build/parser.tab.cpp"
    break;

  case 71: /* inheritance_specifier: IDENTIFIER  */
#line 469 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3311 "build/parser.tab.cpp"
    break;

  case 72: /* inheritance_specifier: TYPE_NAME  */
#line 475 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3322 "build/parser.tab.cpp"
    break;

  case 73: /* member_decl_list: member_item  */
#line 486 "../phase2-parser/src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 3332 "build/parser.tab.cpp"
    break;

  case 74: /* member_decl_list: member_decl_list member_item  */
#line 491 "../phase2-parser/src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 3346 "build/parser.tab.cpp"
    break;

  case 75: /* member_item: declaration  */
#line 503 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3352 "build/parser.tab.cpp"
    break;

  case 76: /* member_item: function_definition  */
#line 504 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3358 "build/parser.tab.cpp"
    break;

  case 77: /* member_item: access_specifier ':'  */
#line 505 "../phase2-parser/src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3364 "build/parser.tab.cpp"
    break;

  case 78: /* member_item: constructor_def  */
#line 506 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3370 "build/parser.tab.cpp"
    break;

  case 79: /* member_item: destructor_def  */
#line 507 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3376 "build/parser.tab.cpp"
    break;

  case 80: /* $@12: %empty  */
#line 514 "../phase2-parser/src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3382 "build/parser.tab.cpp"
    break;

  case 81: /* constructor_head: IDENTIFIER '(' $@12 parameter_list_opt ')'  */
#line 514 "../phase2-parser/src/parser.y"
                                                                                                      {
          setCategory(yyvsp[-4].idx, "CONSTRUCTOR");
          for (auto &p : yyvsp[-1].paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
          yyval = yyvsp[-4];
          yyval.paramList = yyvsp[-1].paramList;
          yyval.decl.isVariadic = yyvsp[-1].decl.isVariadic;
      }
#line 3401 "build/parser.tab.cpp"
    break;

  case 82: /* constructor_def: constructor_head compound_stmt  */
#line 531 "../phase2-parser/src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3410 "build/parser.tab.cpp"
    break;

  case 83: /* constructor_def: constructor_head ';'  */
#line 535 "../phase2-parser/src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3419 "build/parser.tab.cpp"
    break;

  case 84: /* destructor_head: '~' IDENTIFIER '(' ')'  */
#line 542 "../phase2-parser/src/parser.y"
                             {
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          pushScope(currentClassName() + "::~" + yyvsp[-2].str + "()");
          yyval = yyvsp[-2];
      }
#line 3429 "build/parser.tab.cpp"
    break;

  case 85: /* destructor_def: destructor_head compound_stmt  */
#line 550 "../phase2-parser/src/parser.y"
                                    {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), yyvsp[0].node);
      }
#line 3438 "build/parser.tab.cpp"
    break;

  case 86: /* destructor_def: destructor_head ';'  */
#line 554 "../phase2-parser/src/parser.y"
                          {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), nullptr);
      }
#line 3447 "build/parser.tab.cpp"
    break;

  case 87: /* $@13: %empty  */
#line 562 "../phase2-parser/src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3457 "build/parser.tab.cpp"
    break;

  case 88: /* $@14: %empty  */
#line 566 "../phase2-parser/src/parser.y"
                               {
          setCategory(yyvsp[-4].idx, "CONSTRUCTOR");
          for (auto &p : yyvsp[-1].paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      }
#line 3473 "build/parser.tab.cpp"
    break;

  case 89: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@13 parameter_list_opt ')' $@14 compound_stmt  */
#line 576 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3483 "build/parser.tab.cpp"
    break;

  case 90: /* $@15: %empty  */
#line 581 "../phase2-parser/src/parser.y"
                                                {
          setCategory(yyvsp[-5].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-5].str)));
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          enterClass(yyvsp[-5].str);
          pushScope(yyvsp[-5].str + "::~" + yyvsp[-2].str + "()");
      }
#line 3494 "build/parser.tab.cpp"
    break;

  case 91: /* out_of_class_special: TYPE_NAME SCOPE_RES '~' TYPE_NAME '(' ')' $@15 compound_stmt  */
#line 586 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-4].str, yyvsp[-4].idx, yyvsp[-7].str, yyvsp[0].node);
          leaveClass();
      }
#line 3504 "build/parser.tab.cpp"
    break;

  case 95: /* enumerator_list: enumerator  */
#line 600 "../phase2-parser/src/parser.y"
                 { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3510 "build/parser.tab.cpp"
    break;

  case 96: /* enumerator_list: enumerator_list ',' enumerator  */
#line 601 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3516 "build/parser.tab.cpp"
    break;

  case 97: /* enumerator: IDENTIFIER  */
#line 605 "../phase2-parser/src/parser.y"
                 {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[0].str), yyvsp[0].idx);
      }
#line 3526 "build/parser.tab.cpp"
    break;

  case 98: /* enumerator: IDENTIFIER '=' constant_expr  */
#line 610 "../phase2-parser/src/parser.y"
                                   {
          declareSymbol(yyvsp[-2].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3536 "build/parser.tab.cpp"
    break;

  case 99: /* init_declarator_list_opt: %empty  */
#line 618 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3542 "build/parser.tab.cpp"
    break;

  case 100: /* init_declarator_list_opt: init_declarator_list  */
#line 619 "../phase2-parser/src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3548 "build/parser.tab.cpp"
    break;

  case 101: /* init_declarator_list: init_declarator  */
#line 623 "../phase2-parser/src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3554 "build/parser.tab.cpp"
    break;

  case 102: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 624 "../phase2-parser/src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3560 "build/parser.tab.cpp"
    break;

  case 103: /* init_declarator: declarator  */
#line 628 "../phase2-parser/src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3566 "build/parser.tab.cpp"
    break;

  case 104: /* init_declarator: declarator '=' initializer  */
#line 629 "../phase2-parser/src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3572 "build/parser.tab.cpp"
    break;

  case 105: /* initializer: assignment_expr  */
#line 633 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3578 "build/parser.tab.cpp"
    break;

  case 106: /* initializer: '{' '}'  */
#line 634 "../phase2-parser/src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3584 "build/parser.tab.cpp"
    break;

  case 107: /* initializer: '{' initializer_list '}'  */
#line 635 "../phase2-parser/src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3594 "build/parser.tab.cpp"
    break;

  case 108: /* initializer: '{' initializer_list ',' '}'  */
#line 640 "../phase2-parser/src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3604 "build/parser.tab.cpp"
    break;

  case 109: /* initializer_list: initializer_item  */
#line 648 "../phase2-parser/src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3610 "build/parser.tab.cpp"
    break;

  case 110: /* initializer_list: initializer_list ',' initializer_item  */
#line 649 "../phase2-parser/src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3616 "build/parser.tab.cpp"
    break;

  case 111: /* initializer_item: initializer  */
#line 653 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3622 "build/parser.tab.cpp"
    break;

  case 112: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 654 "../phase2-parser/src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3630 "build/parser.tab.cpp"
    break;

  case 113: /* initializer_item: DESIG_LBRACKET constant_expr ']' '=' initializer  */
#line 657 "../phase2-parser/src/parser.y"
                                                       {
          /* the scanner saw `] =` ahead, so this '[' cannot open a lambda */
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3639 "build/parser.tab.cpp"
    break;

  case 114: /* pointer: '*'  */
#line 664 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3645 "build/parser.tab.cpp"
    break;

  case 115: /* pointer: '&'  */
#line 665 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3651 "build/parser.tab.cpp"
    break;

  case 116: /* pointer: pointer '*'  */
#line 666 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3657 "build/parser.tab.cpp"
    break;

  case 117: /* pointer: pointer '&'  */
#line 667 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3663 "build/parser.tab.cpp"
    break;

  case 118: /* pointer: pointer CONST  */
#line 668 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3669 "build/parser.tab.cpp"
    break;

  case 119: /* pointer: pointer VOLATILE  */
#line 669 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "v"; }
#line 3675 "build/parser.tab.cpp"
    break;

  case 120: /* declarator: pointer direct_declarator  */
#line 673 "../phase2-parser/src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3686 "build/parser.tab.cpp"
    break;

  case 121: /* declarator: direct_declarator  */
#line 679 "../phase2-parser/src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3692 "build/parser.tab.cpp"
    break;

  case 122: /* abstract_declarator: pointer  */
#line 685 "../phase2-parser/src/parser.y"
              { yyval = yyvsp[0]; }
#line 3698 "build/parser.tab.cpp"
    break;

  case 123: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 686 "../phase2-parser/src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3709 "build/parser.tab.cpp"
    break;

  case 124: /* abstract_declarator: direct_abstract_declarator  */
#line 692 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3715 "build/parser.tab.cpp"
    break;

  case 125: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 696 "../phase2-parser/src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3729 "build/parser.tab.cpp"
    break;

  case 126: /* direct_abstract_declarator: '[' ']'  */
#line 705 "../phase2-parser/src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3735 "build/parser.tab.cpp"
    break;

  case 127: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 706 "../phase2-parser/src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3741 "build/parser.tab.cpp"
    break;

  case 128: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 707 "../phase2-parser/src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3747 "build/parser.tab.cpp"
    break;

  case 129: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 708 "../phase2-parser/src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3753 "build/parser.tab.cpp"
    break;

  case 130: /* direct_abstract_declarator: direct_abstract_declarator '(' param_scope parameter_list_opt ')'  */
#line 709 "../phase2-parser/src/parser.y"
                                                                        {
          yyval = yyvsp[-4];
          if (yyvsp[-4].decl.wasParenGrouped && yyvsp[-4].decl.pointerLevel > 0) yyval.decl.isFunctionPointer = true;
          else yyval.decl.isFunction = true;
          yyval.decl.wasParenGrouped = false;
          yyval.decl.params = yyvsp[-1].paramList;
          yyval.decl.isVariadic = yyvsp[-1].decl.isVariadic;
          popScope();
      }
#line 3767 "build/parser.tab.cpp"
    break;

  case 131: /* direct_declarator: IDENTIFIER  */
#line 721 "../phase2-parser/src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3776 "build/parser.tab.cpp"
    break;

  case 132: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 725 "../phase2-parser/src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3788 "build/parser.tab.cpp"
    break;

  case 133: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 732 "../phase2-parser/src/parser.y"
                                     {
          /* the common case in practice: an out-of-class method
             definition (Dog::bark(...) {...}) is almost always
             written AFTER the class's closing '}', by which point
             its name is already TYPE_NAME, not IDENTIFIER (see the
             typedef lexer-hack note above) */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3805 "build/parser.tab.cpp"
    break;

  case 134: /* direct_declarator: '(' declarator ')'  */
#line 744 "../phase2-parser/src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3819 "build/parser.tab.cpp"
    break;

  case 135: /* direct_declarator: operator_function_id  */
#line 753 "../phase2-parser/src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3828 "build/parser.tab.cpp"
    break;

  case 136: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 757 "../phase2-parser/src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3840 "build/parser.tab.cpp"
    break;

  case 137: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 764 "../phase2-parser/src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3852 "build/parser.tab.cpp"
    break;

  case 138: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 771 "../phase2-parser/src/parser.y"
                                                               {
          yyval = yyvsp[-4];
          if (yyvsp[-4].decl.wasParenGrouped && yyvsp[-4].decl.pointerLevel > 0) {
              /* `int (*fp)(int, int)` -- fp is a VARIABLE of function-
                 pointer type, not a function declaration. */
              yyval.decl.isFunctionPointer = true;
          } else {
              yyval.decl.isFunction = true;
          }
          yyval.decl.wasParenGrouped = false; /* consumed */
          yyval.decl.params = yyvsp[-1].paramList;
          yyval.decl.isVariadic = yyvsp[-1].decl.isVariadic;
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
#line 3874 "build/parser.tab.cpp"
    break;

  case 139: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 788 "../phase2-parser/src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3886 "build/parser.tab.cpp"
    break;

  case 140: /* direct_declarator: direct_declarator '[' ']'  */
#line 795 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3892 "build/parser.tab.cpp"
    break;

  case 141: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 796 "../phase2-parser/src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3898 "build/parser.tab.cpp"
    break;

  case 142: /* operator_function_id: OPERATOR overloadable_operator  */
#line 801 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3904 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: '+'  */
#line 805 "../phase2-parser/src/parser.y"
          { yyval.str = "+"; }
#line 3910 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: '-'  */
#line 805 "../phase2-parser/src/parser.y"
                                  { yyval.str = "-"; }
#line 3916 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: '*'  */
#line 805 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "*"; }
#line 3922 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: '/'  */
#line 805 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3928 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: '%'  */
#line 806 "../phase2-parser/src/parser.y"
          { yyval.str = "%"; }
#line 3934 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: '^'  */
#line 806 "../phase2-parser/src/parser.y"
                                  { yyval.str = "^"; }
#line 3940 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: '&'  */
#line 806 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "&"; }
#line 3946 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: '|'  */
#line 806 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3952 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: '~'  */
#line 807 "../phase2-parser/src/parser.y"
          { yyval.str = "~"; }
#line 3958 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: '!'  */
#line 807 "../phase2-parser/src/parser.y"
                                  { yyval.str = "!"; }
#line 3964 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: '='  */
#line 807 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "="; }
#line 3970 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: '<'  */
#line 807 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3976 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: '>'  */
#line 808 "../phase2-parser/src/parser.y"
          { yyval.str = ">"; }
#line 3982 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: EQ_OP  */
#line 808 "../phase2-parser/src/parser.y"
                                    { yyval.str = "=="; }
#line 3988 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: NE_OP  */
#line 808 "../phase2-parser/src/parser.y"
                                                               { yyval.str = "!="; }
#line 3994 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: LE_OP  */
#line 808 "../phase2-parser/src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 4000 "build/parser.tab.cpp"
    break;

  case 159: /* overloadable_operator: GE_OP  */
#line 809 "../phase2-parser/src/parser.y"
            { yyval.str = ">="; }
#line 4006 "build/parser.tab.cpp"
    break;

  case 160: /* overloadable_operator: AND_OP  */
#line 809 "../phase2-parser/src/parser.y"
                                        { yyval.str = "&&"; }
#line 4012 "build/parser.tab.cpp"
    break;

  case 161: /* overloadable_operator: OR_OP  */
#line 809 "../phase2-parser/src/parser.y"
                                                                   { yyval.str = "||"; }
#line 4018 "build/parser.tab.cpp"
    break;

  case 162: /* overloadable_operator: SHL  */
#line 809 "../phase2-parser/src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 4024 "build/parser.tab.cpp"
    break;

  case 163: /* overloadable_operator: SHR  */
#line 810 "../phase2-parser/src/parser.y"
          { yyval.str = ">>"; }
#line 4030 "build/parser.tab.cpp"
    break;

  case 164: /* overloadable_operator: INC  */
#line 810 "../phase2-parser/src/parser.y"
                                   { yyval.str = "++"; }
#line 4036 "build/parser.tab.cpp"
    break;

  case 165: /* overloadable_operator: DEC  */
#line 810 "../phase2-parser/src/parser.y"
                                                            { yyval.str = "--"; }
#line 4042 "build/parser.tab.cpp"
    break;

  case 166: /* overloadable_operator: PLUS_ASSIGN  */
#line 811 "../phase2-parser/src/parser.y"
                  { yyval.str = "+="; }
#line 4048 "build/parser.tab.cpp"
    break;

  case 167: /* overloadable_operator: MINUS_ASSIGN  */
#line 811 "../phase2-parser/src/parser.y"
                                                    { yyval.str = "-="; }
#line 4054 "build/parser.tab.cpp"
    break;

  case 168: /* overloadable_operator: MUL_ASSIGN  */
#line 811 "../phase2-parser/src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 4060 "build/parser.tab.cpp"
    break;

  case 169: /* overloadable_operator: DIV_ASSIGN  */
#line 812 "../phase2-parser/src/parser.y"
                 { yyval.str = "/="; }
#line 4066 "build/parser.tab.cpp"
    break;

  case 170: /* overloadable_operator: MOD_ASSIGN  */
#line 812 "../phase2-parser/src/parser.y"
                                                 { yyval.str = "%="; }
#line 4072 "build/parser.tab.cpp"
    break;

  case 171: /* overloadable_operator: AND_ASSIGN  */
#line 812 "../phase2-parser/src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 4078 "build/parser.tab.cpp"
    break;

  case 172: /* overloadable_operator: OR_ASSIGN  */
#line 813 "../phase2-parser/src/parser.y"
                { yyval.str = "|="; }
#line 4084 "build/parser.tab.cpp"
    break;

  case 173: /* overloadable_operator: XOR_ASSIGN  */
#line 813 "../phase2-parser/src/parser.y"
                                                { yyval.str = "^="; }
#line 4090 "build/parser.tab.cpp"
    break;

  case 174: /* overloadable_operator: SHL_ASSIGN  */
#line 813 "../phase2-parser/src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 4096 "build/parser.tab.cpp"
    break;

  case 175: /* overloadable_operator: SHR_ASSIGN  */
#line 814 "../phase2-parser/src/parser.y"
                 { yyval.str = ">>="; }
#line 4102 "build/parser.tab.cpp"
    break;

  case 176: /* overloadable_operator: '[' ']'  */
#line 814 "../phase2-parser/src/parser.y"
                                               { yyval.str = "[]"; }
#line 4108 "build/parser.tab.cpp"
    break;

  case 177: /* overloadable_operator: '(' ')'  */
#line 814 "../phase2-parser/src/parser.y"
                                                                            { yyval.str = "()"; }
#line 4114 "build/parser.tab.cpp"
    break;

  case 178: /* param_scope: %empty  */
#line 821 "../phase2-parser/src/parser.y"
                                           { pushScope(); }
#line 4120 "build/parser.tab.cpp"
    break;

  case 179: /* constructor_args: assignment_expr  */
#line 825 "../phase2-parser/src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4126 "build/parser.tab.cpp"
    break;

  case 180: /* constructor_args: constructor_args ',' assignment_expr  */
#line 826 "../phase2-parser/src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4132 "build/parser.tab.cpp"
    break;

  case 181: /* parameter_list_opt: %empty  */
#line 830 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4138 "build/parser.tab.cpp"
    break;

  case 182: /* parameter_list_opt: parameter_list  */
#line 831 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 4144 "build/parser.tab.cpp"
    break;

  case 183: /* parameter_list: parameter_decl  */
#line 835 "../phase2-parser/src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 4153 "build/parser.tab.cpp"
    break;

  case 184: /* parameter_list: parameter_list ',' parameter_decl  */
#line 839 "../phase2-parser/src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 4162 "build/parser.tab.cpp"
    break;

  case 185: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 843 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 4168 "build/parser.tab.cpp"
    break;

  case 186: /* parameter_decl: declaration_specifiers declarator  */
#line 847 "../phase2-parser/src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 4178 "build/parser.tab.cpp"
    break;

  case 187: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 852 "../phase2-parser/src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 4188 "build/parser.tab.cpp"
    break;

  case 188: /* parameter_decl: declaration_specifiers  */
#line 857 "../phase2-parser/src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 4198 "build/parser.tab.cpp"
    break;

  case 189: /* $@16: %empty  */
#line 865 "../phase2-parser/src/parser.y"
                                        {
          bool outOfClass = !yyvsp[0].decl.className.empty();
          if (outOfClass) enterClass(yyvsp[0].decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[0].decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[0].decl.name, paramExprs(yyvsp[0].decl.params), yyvsp[0].decl.isVariadic, currentClassName());
          std::string returnType = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          SymbolDeclInfo extra;
          extra.tokenIdx = yyvsp[0].decl.nameIdx;
          extra.isStatic = yyvsp[-1].typeSpec.isStatic;
          extra.isConst = yyvsp[-1].typeSpec.isConst;
          extra.isVolatile = yyvsp[-1].typeSpec.isVolatile;
          extra.pointerLevel = yyvsp[0].decl.pointerLevel;
          extra.arrayLevel = yyvsp[0].decl.arrayLevel;
          extra.returnType = returnType;
          extra.paramTypes = paramTypes;
          extra.mangledName = mangled;
          declareSymbol(yyvsp[0].decl.name, SymKind::PROCEDURE, "PROCEDURE", extra);
          setCategory(yyvsp[0].decl.nameIdx, "PROCEDURE");
          /* deliberately NOT calling leaveClass() here for the
             out-of-class case (Dog::bark() {...}) -- class context
             needs to stay active through the whole body, so `this`
             used inside it is correctly recognized as valid. Left at
             the very end, in the final action, once the body is
             fully parsed. */
          pushScope(yyvsp[0].decl.name + "()");
          for (auto &p : yyvsp[0].decl.params) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      }
#line 4238 "build/parser.tab.cpp"
    break;

  case 190: /* function_definition: declaration_specifiers declarator $@16 '{' block_item_list_opt '}'  */
#line 899 "../phase2-parser/src/parser.y"
                                    {
          popScope();
          bool outOfClass = !yyvsp[-4].decl.className.empty();
          /* currentClassName() is still correctly set here for the
             out-of-class case -- it was never left, see above -- so
             no need to re-enter it just to compute the mangled name
             again. */
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[-4].decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[-4].decl.name, paramExprs(yyvsp[-4].decl.params), yyvsp[-4].decl.isVariadic, currentClassName());
          if (outOfClass) leaveClass();
          auto node = atToken(mkNode(ASTKind::FunctionDef, yyvsp[-4].decl.name + " : " + mangled), yyvsp[-4].decl.nameIdx);
          node->typeExpr = makeTypeExpr(yyvsp[-5].typeSpec, yyvsp[-4].decl);
          for (auto &p : yyvsp[-4].decl.params) {
              if (!p.name.empty()) {
                  auto pn = atToken(mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr), p.nameIdx);
                  pn->typeExpr = p.typeExpr;
                  addChild(node, pn);
              }
          }
          auto body = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-2].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(body, s);
          addChild(node, body);
          yyval.node = node;
      }
#line 4268 "build/parser.tab.cpp"
    break;

  case 191: /* statement: compound_stmt  */
#line 927 "../phase2-parser/src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 4274 "build/parser.tab.cpp"
    break;

  case 192: /* statement: expr_stmt  */
#line 928 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 4280 "build/parser.tab.cpp"
    break;

  case 193: /* statement: selection_stmt  */
#line 929 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4286 "build/parser.tab.cpp"
    break;

  case 194: /* statement: iteration_stmt  */
#line 930 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4292 "build/parser.tab.cpp"
    break;

  case 195: /* statement: jump_stmt  */
#line 931 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 4298 "build/parser.tab.cpp"
    break;

  case 196: /* statement: labeled_stmt  */
#line 932 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4304 "build/parser.tab.cpp"
    break;

  case 197: /* statement: declaration  */
#line 933 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4310 "build/parser.tab.cpp"
    break;

  case 198: /* statement: error ';'  */
#line 934 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4316 "build/parser.tab.cpp"
    break;

  case 199: /* statement: error '}'  */
#line 935 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4322 "build/parser.tab.cpp"
    break;

  case 200: /* $@17: %empty  */
#line 939 "../phase2-parser/src/parser.y"
          { pushScope(); }
#line 4328 "build/parser.tab.cpp"
    break;

  case 201: /* compound_stmt: '{' $@17 block_item_list_opt '}'  */
#line 939 "../phase2-parser/src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 4339 "build/parser.tab.cpp"
    break;

  case 202: /* block_item_list_opt: %empty  */
#line 948 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4345 "build/parser.tab.cpp"
    break;

  case 203: /* block_item_list_opt: block_item_list  */
#line 949 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[0]; }
#line 4351 "build/parser.tab.cpp"
    break;

  case 204: /* block_item_list: statement  */
#line 953 "../phase2-parser/src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4357 "build/parser.tab.cpp"
    break;

  case 205: /* block_item_list: block_item_list statement  */
#line 954 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4363 "build/parser.tab.cpp"
    break;

  case 206: /* expr_stmt: ';'  */
#line 958 "../phase2-parser/src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 4369 "build/parser.tab.cpp"
    break;

  case 207: /* expr_stmt: expr ';'  */
#line 959 "../phase2-parser/src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 4375 "build/parser.tab.cpp"
    break;

  case 208: /* selection_stmt: IF '(' expr ')' statement  */
#line 963 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4383 "build/parser.tab.cpp"
    break;

  case 209: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 966 "../phase2-parser/src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 4391 "build/parser.tab.cpp"
    break;

  case 210: /* $@18: %empty  */
#line 969 "../phase2-parser/src/parser.y"
                          { hintScope("switch"); }
#line 4397 "build/parser.tab.cpp"
    break;

  case 211: /* selection_stmt: SWITCH '(' expr ')' $@18 compound_stmt  */
#line 969 "../phase2-parser/src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4405 "build/parser.tab.cpp"
    break;

  case 212: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 975 "../phase2-parser/src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4413 "build/parser.tab.cpp"
    break;

  case 213: /* labeled_stmt: DEFAULT ':' statement  */
#line 978 "../phase2-parser/src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4421 "build/parser.tab.cpp"
    break;

  case 214: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 981 "../phase2-parser/src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4431 "build/parser.tab.cpp"
    break;

  case 215: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 989 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4439 "build/parser.tab.cpp"
    break;

  case 216: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 992 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4447 "build/parser.tab.cpp"
    break;

  case 217: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 999 "../phase2-parser/src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4456 "build/parser.tab.cpp"
    break;

  case 218: /* iteration_stmt: DO statement error ';'  */
#line 1003 "../phase2-parser/src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4465 "build/parser.tab.cpp"
    break;

  case 219: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 1007 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4473 "build/parser.tab.cpp"
    break;

  case 220: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 1010 "../phase2-parser/src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4482 "build/parser.tab.cpp"
    break;

  case 221: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 1014 "../phase2-parser/src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4491 "build/parser.tab.cpp"
    break;

  case 222: /* for_open: FOR '('  */
#line 1023 "../phase2-parser/src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4497 "build/parser.tab.cpp"
    break;

  case 223: /* for_incr_opt: %empty  */
#line 1027 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4503 "build/parser.tab.cpp"
    break;

  case 224: /* for_incr_opt: expr  */
#line 1028 "../phase2-parser/src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4509 "build/parser.tab.cpp"
    break;

  case 225: /* jump_stmt: BREAK ';'  */
#line 1032 "../phase2-parser/src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4515 "build/parser.tab.cpp"
    break;

  case 226: /* jump_stmt: CONTINUE ';'  */
#line 1033 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4521 "build/parser.tab.cpp"
    break;

  case 227: /* jump_stmt: RETURN ';'  */
#line 1034 "../phase2-parser/src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4527 "build/parser.tab.cpp"
    break;

  case 228: /* jump_stmt: RETURN expr ';'  */
#line 1035 "../phase2-parser/src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4533 "build/parser.tab.cpp"
    break;

  case 229: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 1036 "../phase2-parser/src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4545 "build/parser.tab.cpp"
    break;

  case 230: /* expr: assignment_expr  */
#line 1046 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4551 "build/parser.tab.cpp"
    break;

  case 231: /* expr: expr ',' assignment_expr  */
#line 1047 "../phase2-parser/src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4557 "build/parser.tab.cpp"
    break;

  case 232: /* assignment_expr: binary_expr  */
#line 1051 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4563 "build/parser.tab.cpp"
    break;

  case 233: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 1052 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4571 "build/parser.tab.cpp"
    break;

  case 234: /* assign_op: '='  */
#line 1058 "../phase2-parser/src/parser.y"
                   { yyval.str = "="; }
#line 4577 "build/parser.tab.cpp"
    break;

  case 235: /* assign_op: PLUS_ASSIGN  */
#line 1059 "../phase2-parser/src/parser.y"
                   { yyval.str = "+="; }
#line 4583 "build/parser.tab.cpp"
    break;

  case 236: /* assign_op: MINUS_ASSIGN  */
#line 1060 "../phase2-parser/src/parser.y"
                   { yyval.str = "-="; }
#line 4589 "build/parser.tab.cpp"
    break;

  case 237: /* assign_op: MUL_ASSIGN  */
#line 1061 "../phase2-parser/src/parser.y"
                   { yyval.str = "*="; }
#line 4595 "build/parser.tab.cpp"
    break;

  case 238: /* assign_op: DIV_ASSIGN  */
#line 1062 "../phase2-parser/src/parser.y"
                   { yyval.str = "/="; }
#line 4601 "build/parser.tab.cpp"
    break;

  case 239: /* assign_op: MOD_ASSIGN  */
#line 1063 "../phase2-parser/src/parser.y"
                   { yyval.str = "%="; }
#line 4607 "build/parser.tab.cpp"
    break;

  case 240: /* assign_op: AND_ASSIGN  */
#line 1064 "../phase2-parser/src/parser.y"
                   { yyval.str = "&="; }
#line 4613 "build/parser.tab.cpp"
    break;

  case 241: /* assign_op: OR_ASSIGN  */
#line 1065 "../phase2-parser/src/parser.y"
                   { yyval.str = "|="; }
#line 4619 "build/parser.tab.cpp"
    break;

  case 242: /* assign_op: XOR_ASSIGN  */
#line 1066 "../phase2-parser/src/parser.y"
                   { yyval.str = "^="; }
#line 4625 "build/parser.tab.cpp"
    break;

  case 243: /* assign_op: SHL_ASSIGN  */
#line 1067 "../phase2-parser/src/parser.y"
                   { yyval.str = "<<="; }
#line 4631 "build/parser.tab.cpp"
    break;

  case 244: /* assign_op: SHR_ASSIGN  */
#line 1068 "../phase2-parser/src/parser.y"
                   { yyval.str = ">>="; }
#line 4637 "build/parser.tab.cpp"
    break;

  case 245: /* constant_expr: binary_expr  */
#line 1072 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4643 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 1076 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4649 "build/parser.tab.cpp"
    break;

  case 247: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 1077 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4655 "build/parser.tab.cpp"
    break;

  case 248: /* binary_expr: binary_expr '|' binary_expr  */
#line 1078 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4661 "build/parser.tab.cpp"
    break;

  case 249: /* binary_expr: binary_expr '^' binary_expr  */
#line 1079 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4667 "build/parser.tab.cpp"
    break;

  case 250: /* binary_expr: binary_expr '&' binary_expr  */
#line 1080 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4673 "build/parser.tab.cpp"
    break;

  case 251: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 1081 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4679 "build/parser.tab.cpp"
    break;

  case 252: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 1082 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4685 "build/parser.tab.cpp"
    break;

  case 253: /* binary_expr: binary_expr '<' binary_expr  */
#line 1083 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4691 "build/parser.tab.cpp"
    break;

  case 254: /* binary_expr: binary_expr '>' binary_expr  */
#line 1084 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4697 "build/parser.tab.cpp"
    break;

  case 255: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 1085 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4703 "build/parser.tab.cpp"
    break;

  case 256: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 1086 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4709 "build/parser.tab.cpp"
    break;

  case 257: /* binary_expr: binary_expr SHL binary_expr  */
#line 1087 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4715 "build/parser.tab.cpp"
    break;

  case 258: /* binary_expr: binary_expr SHR binary_expr  */
#line 1088 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4721 "build/parser.tab.cpp"
    break;

  case 259: /* binary_expr: binary_expr '+' binary_expr  */
#line 1089 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4727 "build/parser.tab.cpp"
    break;

  case 260: /* binary_expr: binary_expr '-' binary_expr  */
#line 1090 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4733 "build/parser.tab.cpp"
    break;

  case 261: /* binary_expr: binary_expr '*' binary_expr  */
#line 1091 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4739 "build/parser.tab.cpp"
    break;

  case 262: /* binary_expr: binary_expr '/' binary_expr  */
#line 1092 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4745 "build/parser.tab.cpp"
    break;

  case 263: /* binary_expr: binary_expr '%' binary_expr  */
#line 1093 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4751 "build/parser.tab.cpp"
    break;

  case 264: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 1094 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4759 "build/parser.tab.cpp"
    break;

  case 265: /* binary_expr: unary_expr  */
#line 1097 "../phase2-parser/src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4765 "build/parser.tab.cpp"
    break;

  case 266: /* unary_expr: postfix_expr  */
#line 1101 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4771 "build/parser.tab.cpp"
    break;

  case 267: /* unary_expr: INC unary_expr  */
#line 1102 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4777 "build/parser.tab.cpp"
    break;

  case 268: /* unary_expr: DEC unary_expr  */
#line 1103 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4783 "build/parser.tab.cpp"
    break;

  case 269: /* unary_expr: '&' unary_expr  */
#line 1104 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4789 "build/parser.tab.cpp"
    break;

  case 270: /* unary_expr: '*' unary_expr  */
#line 1105 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4795 "build/parser.tab.cpp"
    break;

  case 271: /* unary_expr: '+' unary_expr  */
#line 1106 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4801 "build/parser.tab.cpp"
    break;

  case 272: /* unary_expr: '-' unary_expr  */
#line 1107 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4807 "build/parser.tab.cpp"
    break;

  case 273: /* unary_expr: '!' unary_expr  */
#line 1108 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4813 "build/parser.tab.cpp"
    break;

  case 274: /* unary_expr: '~' unary_expr  */
#line 1109 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4819 "build/parser.tab.cpp"
    break;

  case 275: /* unary_expr: '(' type_name ')' unary_expr  */
#line 1110 "../phase2-parser/src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4828 "build/parser.tab.cpp"
    break;

  case 276: /* unary_expr: SIZEOF unary_expr  */
#line 1114 "../phase2-parser/src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4834 "build/parser.tab.cpp"
    break;

  case 277: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 1115 "../phase2-parser/src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4843 "build/parser.tab.cpp"
    break;

  case 278: /* unary_expr: NEW new_type_id  */
#line 1119 "../phase2-parser/src/parser.y"
                      {
          yyval.node = atToken(mkNode(ASTKind::NewExpr, yyvsp[0].str), yyvsp[-1].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4852 "build/parser.tab.cpp"
    break;

  case 279: /* unary_expr: NEW new_type_id '(' constructor_args_opt ')'  */
#line 1123 "../phase2-parser/src/parser.y"
                                                   {
          yyval.node = atToken(mkNode(ASTKind::NewExpr, yyvsp[-3].str), yyvsp[-4].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-3].typeSpec, yyvsp[-3].decl);
          auto c = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].str), yyvsp[-2].idx);
          c->typeExpr = yyval.node->typeExpr;
          for (auto &a : yyvsp[-1].nodeList) addChild(c, a);
          addChild(yyval.node, c);
      }
#line 4865 "build/parser.tab.cpp"
    break;

  case 280: /* unary_expr: DELETE unary_expr  */
#line 1131 "../phase2-parser/src/parser.y"
                        { yyval.node = atToken(mkNode(ASTKind::DeleteExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4871 "build/parser.tab.cpp"
    break;

  case 281: /* unary_expr: DELETE_ARRAY unary_expr  */
#line 1132 "../phase2-parser/src/parser.y"
                              { yyval.node = atToken(mkNode(ASTKind::DeleteExpr, "[]", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4877 "build/parser.tab.cpp"
    break;

  case 282: /* type_name: type_name_specifiers  */
#line 1136 "../phase2-parser/src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4886 "build/parser.tab.cpp"
    break;

  case 283: /* type_name: type_name_specifiers abstract_declarator  */
#line 1140 "../phase2-parser/src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4895 "build/parser.tab.cpp"
    break;

  case 284: /* new_type_id: type_name_specifiers  */
#line 1149 "../phase2-parser/src/parser.y"
                                              {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4904 "build/parser.tab.cpp"
    break;

  case 285: /* new_type_id: type_name_specifiers new_pointer  */
#line 1153 "../phase2-parser/src/parser.y"
                                                          {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, 0);
          yyval.decl = yyvsp[0].decl;
      }
#line 4913 "build/parser.tab.cpp"
    break;

  case 286: /* new_type_id: type_name_specifiers new_array_dims  */
#line 1157 "../phase2-parser/src/parser.y"
                                          {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, 0, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4922 "build/parser.tab.cpp"
    break;

  case 287: /* new_type_id: type_name_specifiers new_pointer new_array_dims  */
#line 1161 "../phase2-parser/src/parser.y"
                                                      {
          yyval.str = computeTypeStr(yyvsp[-2].typeSpec, yyvsp[-1].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
          yyval.decl.pointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps;
      }
#line 4933 "build/parser.tab.cpp"
    break;

  case 288: /* new_pointer: '*'  */
#line 1170 "../phase2-parser/src/parser.y"
                      { yyval.decl = DeclInfo(); yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 4939 "build/parser.tab.cpp"
    break;

  case 289: /* new_pointer: new_pointer '*'  */
#line 1171 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 4945 "build/parser.tab.cpp"
    break;

  case 290: /* new_array_dims: '[' expr ']'  */
#line 1176 "../phase2-parser/src/parser.y"
                   { yyval.decl = DeclInfo(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 4951 "build/parser.tab.cpp"
    break;

  case 291: /* new_array_dims: new_array_dims '[' expr ']'  */
#line 1177 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 4957 "build/parser.tab.cpp"
    break;

  case 292: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1181 "../phase2-parser/src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isVolatile) yyval.typeSpec.isVolatile = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4970 "build/parser.tab.cpp"
    break;

  case 293: /* type_name_specifiers: type_name_specifier  */
#line 1189 "../phase2-parser/src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4976 "build/parser.tab.cpp"
    break;

  case 294: /* type_name_specifier: INT  */
#line 1193 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4982 "build/parser.tab.cpp"
    break;

  case 295: /* type_name_specifier: CHAR  */
#line 1194 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4988 "build/parser.tab.cpp"
    break;

  case 296: /* type_name_specifier: FLOAT  */
#line 1195 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4994 "build/parser.tab.cpp"
    break;

  case 297: /* type_name_specifier: DOUBLE  */
#line 1196 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 5000 "build/parser.tab.cpp"
    break;

  case 298: /* type_name_specifier: VOID  */
#line 1197 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 5006 "build/parser.tab.cpp"
    break;

  case 299: /* type_name_specifier: BOOL  */
#line 1198 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 5012 "build/parser.tab.cpp"
    break;

  case 300: /* type_name_specifier: SHORT  */
#line 1199 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 5018 "build/parser.tab.cpp"
    break;

  case 301: /* type_name_specifier: LONG  */
#line 1200 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 5024 "build/parser.tab.cpp"
    break;

  case 302: /* type_name_specifier: SIGNED  */
#line 1201 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 5030 "build/parser.tab.cpp"
    break;

  case 303: /* type_name_specifier: UNSIGNED  */
#line 1202 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 5036 "build/parser.tab.cpp"
    break;

  case 304: /* type_name_specifier: FILE_KW  */
#line 1203 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FILE"); }
#line 5042 "build/parser.tab.cpp"
    break;

  case 305: /* type_name_specifier: VA_LIST  */
#line 1204 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 5048 "build/parser.tab.cpp"
    break;

  case 306: /* type_name_specifier: CONST  */
#line 1205 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 5054 "build/parser.tab.cpp"
    break;

  case 307: /* type_name_specifier: VOLATILE  */
#line 1206 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isVolatile = true; }
#line 5060 "build/parser.tab.cpp"
    break;

  case 308: /* type_name_specifier: TYPE_NAME  */
#line 1207 "../phase2-parser/src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 5074 "build/parser.tab.cpp"
    break;

  case 309: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1216 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5085 "build/parser.tab.cpp"
    break;

  case 310: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1222 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5096 "build/parser.tab.cpp"
    break;

  case 311: /* type_name_specifier: UNION IDENTIFIER  */
#line 1228 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5107 "build/parser.tab.cpp"
    break;

  case 312: /* type_name_specifier: UNION TYPE_NAME  */
#line 1234 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5118 "build/parser.tab.cpp"
    break;

  case 313: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1240 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5129 "build/parser.tab.cpp"
    break;

  case 314: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1246 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5140 "build/parser.tab.cpp"
    break;

  case 315: /* type_name_specifier: ENUM IDENTIFIER  */
#line 1252 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5151 "build/parser.tab.cpp"
    break;

  case 316: /* type_name_specifier: ENUM TYPE_NAME  */
#line 1258 "../phase2-parser/src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 5162 "build/parser.tab.cpp"
    break;

  case 317: /* postfix_expr: primary_expr  */
#line 1267 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 5168 "build/parser.tab.cpp"
    break;

  case 318: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1268 "../phase2-parser/src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 5174 "build/parser.tab.cpp"
    break;

  case 319: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1269 "../phase2-parser/src/parser.y"
                                             {
          auto n = atNode(mkNode(ASTKind::CallExpr, "", {yyvsp[-3].node}), yyvsp[-3].node);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);

          if (yyvsp[-3].node && yyvsp[-3].node->kind == ASTKind::Identifier) {
              const std::string &calleeName = yyvsp[-3].node->label;
              if (isOverloaded(calleeName)) {
                  std::vector<std::string> argTypes;
                  bool allKnown = true;
                  for (auto &a : yyvsp[-1].nodeList) {
                      std::string t = inferExprType(a);
                      if (t.empty()) { allKnown = false; break; }
                      argTypes.push_back(t);
                  }
                  const Symbol *matched = allKnown ? lookupOverload(calleeName, argTypes) : nullptr;
                  if (matched) {
                      recordUsage(matched);
                      n->label = matched->mangledName; /* which overload this
                                                            call actually
                                                            resolved to */
                  } else {
                      /* couldn't confidently type every argument, or none
                         matched exactly -- fall back rather than guess */
                      recordUsage(lookupSymbol(calleeName));
                  }
              }
              /* not overloaded: primary_expr's IDENTIFIER handling
                 already called recordUsage() for this exact occurrence
                 (it only defers/skips that when the name IS
                 overloaded) -- calling it again here would double-count
                 every non-overloaded call, which is the common case. */
          }

          yyval.node = n;
      }
#line 5214 "build/parser.tab.cpp"
    break;

  case 320: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1304 "../phase2-parser/src/parser.y"
                                  {
          if (yyvsp[-2].node && yyvsp[-2].node->kind == ASTKind::Identifier) {
              const Symbol *base = lookupSymbol(yyvsp[-2].node->label);
              if (base && !base->aggregateTagName.empty()) {
                  const SymbolTableEntry *member = findMember(base->aggregateTagName, yyvsp[0].str);
                  if (member) setCategory(yyvsp[0].idx, member->typeStr);
              }
          }
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 5229 "build/parser.tab.cpp"
    break;

  case 321: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1314 "../phase2-parser/src/parser.y"
                                    {
          if (yyvsp[-2].node && yyvsp[-2].node->kind == ASTKind::Identifier) {
              const Symbol *base = lookupSymbol(yyvsp[-2].node->label);
              if (base && !base->aggregateTagName.empty()) {
                  const SymbolTableEntry *member = findMember(base->aggregateTagName, yyvsp[0].str);
                  if (member) setCategory(yyvsp[0].idx, member->typeStr);
              }
          }
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 5244 "build/parser.tab.cpp"
    break;

  case 322: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1324 "../phase2-parser/src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 5250 "build/parser.tab.cpp"
    break;

  case 323: /* postfix_expr: postfix_expr INC  */
#line 1325 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 5256 "build/parser.tab.cpp"
    break;

  case 324: /* postfix_expr: postfix_expr DEC  */
#line 1326 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 5262 "build/parser.tab.cpp"
    break;

  case 325: /* postfix_expr: builtin_call  */
#line 1327 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 5268 "build/parser.tab.cpp"
    break;

  case 326: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1331 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5274 "build/parser.tab.cpp"
    break;

  case 327: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1332 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5280 "build/parser.tab.cpp"
    break;

  case 328: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1333 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5286 "build/parser.tab.cpp"
    break;

  case 329: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1334 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5292 "build/parser.tab.cpp"
    break;

  case 330: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1335 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5298 "build/parser.tab.cpp"
    break;

  case 331: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1336 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5304 "build/parser.tab.cpp"
    break;

  case 332: /* builtin_call: FOPEN '(' argument_list_opt ')'  */
#line 1337 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fopen"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5310 "build/parser.tab.cpp"
    break;

  case 333: /* builtin_call: FCLOSE '(' argument_list_opt ')'  */
#line 1338 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fclose"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5316 "build/parser.tab.cpp"
    break;

  case 334: /* builtin_call: FREAD '(' argument_list_opt ')'  */
#line 1339 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fread"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5322 "build/parser.tab.cpp"
    break;

  case 335: /* builtin_call: FWRITE '(' argument_list_opt ')'  */
#line 1340 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fwrite"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5328 "build/parser.tab.cpp"
    break;

  case 336: /* builtin_call: FPRINTF '(' argument_list_opt ')'  */
#line 1341 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fprintf"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5334 "build/parser.tab.cpp"
    break;

  case 337: /* builtin_call: FSCANF '(' argument_list_opt ')'  */
#line 1342 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fscanf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5340 "build/parser.tab.cpp"
    break;

  case 338: /* builtin_call: FGETS '(' argument_list_opt ')'  */
#line 1343 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fgets"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5346 "build/parser.tab.cpp"
    break;

  case 339: /* builtin_call: FPUTS '(' argument_list_opt ')'  */
#line 1344 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "fputs"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5352 "build/parser.tab.cpp"
    break;

  case 340: /* builtin_call: FEOF '(' argument_list_opt ')'  */
#line 1345 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "feof"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5358 "build/parser.tab.cpp"
    break;

  case 341: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1346 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5364 "build/parser.tab.cpp"
    break;

  case 342: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1347 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5370 "build/parser.tab.cpp"
    break;

  case 343: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1348 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 5376 "build/parser.tab.cpp"
    break;

  case 344: /* constructor_args_opt: %empty  */
#line 1352 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 5382 "build/parser.tab.cpp"
    break;

  case 345: /* constructor_args_opt: constructor_args  */
#line 1353 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 5388 "build/parser.tab.cpp"
    break;

  case 346: /* argument_list_opt: %empty  */
#line 1357 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 5394 "build/parser.tab.cpp"
    break;

  case 347: /* argument_list_opt: argument_list  */
#line 1358 "../phase2-parser/src/parser.y"
                    { yyval = yyvsp[0]; }
#line 5400 "build/parser.tab.cpp"
    break;

  case 348: /* argument_list: argument  */
#line 1362 "../phase2-parser/src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 5406 "build/parser.tab.cpp"
    break;

  case 349: /* argument_list: argument_list ',' argument  */
#line 1363 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 5412 "build/parser.tab.cpp"
    break;

  case 350: /* argument: assignment_expr  */
#line 1367 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 5418 "build/parser.tab.cpp"
    break;

  case 351: /* argument: type_name  */
#line 1368 "../phase2-parser/src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 5427 "build/parser.tab.cpp"
    break;

  case 352: /* primary_expr: IDENTIFIER  */
#line 1375 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 5441 "build/parser.tab.cpp"
    break;

  case 353: /* primary_expr: INT_LITERAL  */
#line 1384 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5447 "build/parser.tab.cpp"
    break;

  case 354: /* primary_expr: FLOAT_LITERAL  */
#line 1385 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5453 "build/parser.tab.cpp"
    break;

  case 355: /* primary_expr: CHAR_LITERAL  */
#line 1386 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5459 "build/parser.tab.cpp"
    break;

  case 356: /* primary_expr: string_literal  */
#line 1387 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 5465 "build/parser.tab.cpp"
    break;

  case 357: /* primary_expr: BOOL_LITERAL  */
#line 1388 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5471 "build/parser.tab.cpp"
    break;

  case 358: /* primary_expr: THIS  */
#line 1389 "../phase2-parser/src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 5477 "build/parser.tab.cpp"
    break;

  case 359: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1390 "../phase2-parser/src/parser.y"
                                             {
          /* `Dog(4)`: a temporary object (for a scalar type, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5486 "build/parser.tab.cpp"
    break;

  case 360: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1394 "../phase2-parser/src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5496 "build/parser.tab.cpp"
    break;

  case 361: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1401 "../phase2-parser/src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5502 "build/parser.tab.cpp"
    break;

  case 362: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1402 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5508 "build/parser.tab.cpp"
    break;

  case 363: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1403 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5514 "build/parser.tab.cpp"
    break;

  case 364: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1404 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5520 "build/parser.tab.cpp"
    break;

  case 365: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1405 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5526 "build/parser.tab.cpp"
    break;

  case 366: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1406 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5532 "build/parser.tab.cpp"
    break;

  case 367: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1407 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5538 "build/parser.tab.cpp"
    break;

  case 368: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1408 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5544 "build/parser.tab.cpp"
    break;

  case 369: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1409 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5550 "build/parser.tab.cpp"
    break;

  case 370: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1410 "../phase2-parser/src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5556 "build/parser.tab.cpp"
    break;

  case 371: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1411 "../phase2-parser/src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 5568 "build/parser.tab.cpp"
    break;

  case 372: /* primary_expr: '(' expr ')'  */
#line 1418 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 5574 "build/parser.tab.cpp"
    break;

  case 373: /* primary_expr: lambda_expr  */
#line 1419 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 5580 "build/parser.tab.cpp"
    break;

  case 374: /* string_literal: STRING_LITERAL  */
#line 1424 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5586 "build/parser.tab.cpp"
    break;

  case 375: /* string_literal: string_literal STRING_LITERAL  */
#line 1425 "../phase2-parser/src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 5596 "build/parser.tab.cpp"
    break;

  case 376: /* $@19: %empty  */
#line 1433 "../phase2-parser/src/parser.y"
                                   { pushScope("lambda"); }
#line 5602 "build/parser.tab.cpp"
    break;

  case 377: /* $@20: %empty  */
#line 1433 "../phase2-parser/src/parser.y"
                                                                                                     {
          for (auto &p : yyvsp[-2].paramList) {
              if (p.nameIdx >= 0) {
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, SymbolDeclInfo{p.nameIdx});
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      }
#line 5615 "build/parser.tab.cpp"
    break;

  case 378: /* lambda_expr: '[' capture_list_opt ']' '(' $@19 parameter_list_opt ')' lambda_specifiers $@20 compound_stmt  */
#line 1440 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeLambdaNode(yyvsp[-9].idx, yyvsp[-8].str, yyvsp[-4].paramList, yyvsp[-4].decl.isVariadic, yyvsp[-2], yyvsp[0].node);
      }
#line 5624 "build/parser.tab.cpp"
    break;

  case 379: /* $@21: %empty  */
#line 1444 "../phase2-parser/src/parser.y"
                               { pushScope("lambda"); }
#line 5630 "build/parser.tab.cpp"
    break;

  case 380: /* lambda_expr: '[' capture_list_opt ']' $@21 compound_stmt  */
#line 1444 "../phase2-parser/src/parser.y"
                                                                      {
          /* `[x] { ... }`: no parameter list */
          popScope();
          yyval.node = makeLambdaNode(yyvsp[-4].idx, yyvsp[-3].str, {}, false, ParserValue(), yyvsp[0].node);
      }
#line 5640 "build/parser.tab.cpp"
    break;

  case 381: /* lambda_specifiers: %empty  */
#line 1454 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 5646 "build/parser.tab.cpp"
    break;

  case 382: /* lambda_specifiers: MUTABLE  */
#line 1455 "../phase2-parser/src/parser.y"
              { yyval = ParserValue(); yyval.str = "mutable"; }
#line 5652 "build/parser.tab.cpp"
    break;

  case 383: /* lambda_specifiers: ARROW type_name  */
#line 1456 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[0]; yyval.str = ""; yyval.idx = 1; }
#line 5658 "build/parser.tab.cpp"
    break;

  case 384: /* lambda_specifiers: MUTABLE ARROW type_name  */
#line 1457 "../phase2-parser/src/parser.y"
                              { yyval = yyvsp[0]; yyval.str = "mutable"; yyval.idx = 1; }
#line 5664 "build/parser.tab.cpp"
    break;

  case 385: /* capture_list_opt: %empty  */
#line 1461 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 5670 "build/parser.tab.cpp"
    break;

  case 386: /* capture_list_opt: capture_list  */
#line 1462 "../phase2-parser/src/parser.y"
                   { yyval = yyvsp[0]; }
#line 5676 "build/parser.tab.cpp"
    break;

  case 387: /* capture_list: capture  */
#line 1466 "../phase2-parser/src/parser.y"
              { yyval.str = yyvsp[0].str; }
#line 5682 "build/parser.tab.cpp"
    break;

  case 388: /* capture_list: capture_list ',' capture  */
#line 1467 "../phase2-parser/src/parser.y"
                               { yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str; }
#line 5688 "build/parser.tab.cpp"
    break;

  case 389: /* capture: IDENTIFIER  */
#line 1471 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          recordUsage(s);
          yyval.str = yyvsp[0].str;
      }
#line 5699 "build/parser.tab.cpp"
    break;

  case 390: /* capture: '&' IDENTIFIER  */
#line 1477 "../phase2-parser/src/parser.y"
                     {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          recordUsage(s);
          yyval.str = "&" + yyvsp[0].str;
      }
#line 5710 "build/parser.tab.cpp"
    break;

  case 391: /* capture: '&'  */
#line 1483 "../phase2-parser/src/parser.y"
          { yyval.str = "&"; }
#line 5716 "build/parser.tab.cpp"
    break;

  case 392: /* capture: '='  */
#line 1484 "../phase2-parser/src/parser.y"
          { yyval.str = "="; }
#line 5722 "build/parser.tab.cpp"
    break;

  case 393: /* capture: THIS  */
#line 1485 "../phase2-parser/src/parser.y"
           { yyval.str = "this"; }
#line 5728 "build/parser.tab.cpp"
    break;


#line 5732 "build/parser.tab.cpp"

      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", YY_CAST (yysymbol_kind_t, yyr1[yyn]), &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;

  *++yyvsp = yyval;
  *++yylsp = yyloc;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYSYMBOL_YYEMPTY : YYTRANSLATE (yychar);
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
      {
        yypcontext_t yyctx
          = {yyssp, yytoken, &yylloc};
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = yysyntax_error (&yymsg_alloc, &yymsg, &yyctx);
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == -1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = YY_CAST (char *,
                             YYSTACK_ALLOC (YY_CAST (YYSIZE_T, yymsg_alloc)));
            if (yymsg)
              {
                yysyntax_error_status
                  = yysyntax_error (&yymsg_alloc, &yymsg, &yyctx);
                yymsgp = yymsg;
              }
            else
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = YYENOMEM;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == YYENOMEM)
          YYNOMEM;
      }
    }

  yyerror_range[1] = yylloc;
  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval, &yylloc);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;
  ++yynerrs;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  /* Pop stack until we find a state that shifts the error token.  */
  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYSYMBOL_YYerror;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYSYMBOL_YYerror)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;

      yyerror_range[1] = *yylsp;
      yydestruct ("Error: popping",
                  YY_ACCESSING_SYMBOL (yystate), yyvsp, yylsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  yyerror_range[2] = yylloc;
  ++yylsp;
  YYLLOC_DEFAULT (*yylsp, yyerror_range, 2);

  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", YY_ACCESSING_SYMBOL (yyn), yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturnlab;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturnlab;


/*-----------------------------------------------------------.
| yyexhaustedlab -- YYNOMEM (memory exhaustion) comes here.  |
`-----------------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  goto yyreturnlab;


/*----------------------------------------------------------.
| yyreturnlab -- parsing is finished, clean up and return.  |
`----------------------------------------------------------*/
yyreturnlab:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval, &yylloc);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  YY_ACCESSING_SYMBOL (+*yyssp), yyvsp, yylsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
  return yyresult;
}

#line 1488 "../phase2-parser/src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
