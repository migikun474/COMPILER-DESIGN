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
  YYSYMBOL_CLASS = 13,                     /* CLASS  */
  YYSYMBOL_UNION = 14,                     /* UNION  */
  YYSYMBOL_ENUM = 15,                      /* ENUM  */
  YYSYMBOL_PUBLIC = 16,                    /* PUBLIC  */
  YYSYMBOL_PRIVATE = 17,                   /* PRIVATE  */
  YYSYMBOL_PROTECTED = 18,                 /* PROTECTED  */
  YYSYMBOL_THIS = 19,                      /* THIS  */
  YYSYMBOL_STATIC = 20,                    /* STATIC  */
  YYSYMBOL_TYPEDEF = 21,                   /* TYPEDEF  */
  YYSYMBOL_AUTO = 22,                      /* AUTO  */
  YYSYMBOL_CONST = 23,                     /* CONST  */
  YYSYMBOL_FRIEND = 24,                    /* FRIEND  */
  YYSYMBOL_VIRTUAL = 25,                   /* VIRTUAL  */
  YYSYMBOL_EXPLICIT = 26,                  /* EXPLICIT  */
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
  YYSYMBOL_BOOL = 46,                      /* BOOL  */
  YYSYMBOL_SIZEOF = 47,                    /* SIZEOF  */
  YYSYMBOL_VA_LIST = 48,                   /* VA_LIST  */
  YYSYMBOL_VA_START = 49,                  /* VA_START  */
  YYSYMBOL_VA_ARG = 50,                    /* VA_ARG  */
  YYSYMBOL_VA_END = 51,                    /* VA_END  */
  YYSYMBOL_OPERATOR = 52,                  /* OPERATOR  */
  YYSYMBOL_FCAST = 53,                     /* FCAST  */
  YYSYMBOL_ABSTRACT_LPAREN = 54,           /* ABSTRACT_LPAREN  */
  YYSYMBOL_IDENTIFIER = 55,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 56,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 57,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 58,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 59,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 60,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 61,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 62,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 63,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 64,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 65,                       /* INC  */
  YYSYMBOL_DEC = 66,                       /* DEC  */
  YYSYMBOL_SHL = 67,                       /* SHL  */
  YYSYMBOL_SHR = 68,                       /* SHR  */
  YYSYMBOL_LE_OP = 69,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 70,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 71,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 72,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 73,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 74,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 75,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 76,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 77,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 78,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 79,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 80,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 81,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 82,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 83,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 84,                /* SHR_ASSIGN  */
  YYSYMBOL_PREFER_EXPRESSION = 85,         /* PREFER_EXPRESSION  */
  YYSYMBOL_86_ = 86,                       /* '='  */
  YYSYMBOL_87_ = 87,                       /* '?'  */
  YYSYMBOL_88_ = 88,                       /* ':'  */
  YYSYMBOL_89_ = 89,                       /* '|'  */
  YYSYMBOL_90_ = 90,                       /* '^'  */
  YYSYMBOL_91_ = 91,                       /* '&'  */
  YYSYMBOL_92_ = 92,                       /* '<'  */
  YYSYMBOL_93_ = 93,                       /* '>'  */
  YYSYMBOL_94_ = 94,                       /* '+'  */
  YYSYMBOL_95_ = 95,                       /* '-'  */
  YYSYMBOL_96_ = 96,                       /* '*'  */
  YYSYMBOL_97_ = 97,                       /* '/'  */
  YYSYMBOL_98_ = 98,                       /* '%'  */
  YYSYMBOL_UMINUS = 99,                    /* UMINUS  */
  YYSYMBOL_ADDR = 100,                     /* ADDR  */
  YYSYMBOL_DEREF = 101,                    /* DEREF  */
  YYSYMBOL_CAST = 102,                     /* CAST  */
  YYSYMBOL_103_ = 103,                     /* '!'  */
  YYSYMBOL_104_ = 104,                     /* '~'  */
  YYSYMBOL_105_ = 105,                     /* '.'  */
  YYSYMBOL_106_ = 106,                     /* '('  */
  YYSYMBOL_107_ = 107,                     /* '['  */
  YYSYMBOL_SIZEOF_TYPE = 108,              /* SIZEOF_TYPE  */
  YYSYMBOL_PREFER_DECLARATION = 109,       /* PREFER_DECLARATION  */
  YYSYMBOL_IFX = 110,                      /* IFX  */
  YYSYMBOL_111_ = 111,                     /* ';'  */
  YYSYMBOL_112_ = 112,                     /* '}'  */
  YYSYMBOL_113_ = 113,                     /* '{'  */
  YYSYMBOL_114_ = 114,                     /* ','  */
  YYSYMBOL_115_ = 115,                     /* ')'  */
  YYSYMBOL_116_ = 116,                     /* ']'  */
  YYSYMBOL_YYACCEPT = 117,                 /* $accept  */
  YYSYMBOL_translation_unit = 118,         /* translation_unit  */
  YYSYMBOL_external_decl = 119,            /* external_decl  */
  YYSYMBOL_declaration = 120,              /* declaration  */
  YYSYMBOL_declaration_specifiers = 121,   /* declaration_specifiers  */
  YYSYMBOL_storage_or_type_specifier = 122, /* storage_or_type_specifier  */
  YYSYMBOL_type_specifier = 123,           /* type_specifier  */
  YYSYMBOL_tag_name = 124,                 /* tag_name  */
  YYSYMBOL_struct_or_class_specifier = 125, /* struct_or_class_specifier  */
  YYSYMBOL_126_1 = 126,                    /* $@1  */
  YYSYMBOL_127_2 = 127,                    /* $@2  */
  YYSYMBOL_128_3 = 128,                    /* @3  */
  YYSYMBOL_129_4 = 129,                    /* $@4  */
  YYSYMBOL_130_5 = 130,                    /* $@5  */
  YYSYMBOL_131_6 = 131,                    /* @6  */
  YYSYMBOL_132_7 = 132,                    /* $@7  */
  YYSYMBOL_133_8 = 133,                    /* @8  */
  YYSYMBOL_134_9 = 134,                    /* $@9  */
  YYSYMBOL_135_10 = 135,                   /* $@10  */
  YYSYMBOL_136_11 = 136,                   /* @11  */
  YYSYMBOL_member_decl_list_opt = 137,     /* member_decl_list_opt  */
  YYSYMBOL_enumerator_list = 138,          /* enumerator_list  */
  YYSYMBOL_enumerator = 139,               /* enumerator  */
  YYSYMBOL_comma_opt = 140,                /* comma_opt  */
  YYSYMBOL_inheritance_opt = 141,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 142, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 143,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 144,         /* member_decl_list  */
  YYSYMBOL_member_item = 145,              /* member_item  */
  YYSYMBOL_constructor_head = 146,         /* constructor_head  */
  YYSYMBOL_147_12 = 147,                   /* $@12  */
  YYSYMBOL_constructor_def = 148,          /* constructor_def  */
  YYSYMBOL_out_of_class_special = 149,     /* out_of_class_special  */
  YYSYMBOL_150_13 = 150,                   /* $@13  */
  YYSYMBOL_151_14 = 151,                   /* $@14  */
  YYSYMBOL_access_specifier = 152,         /* access_specifier  */
  YYSYMBOL_init_declarator_list_opt = 153, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 154,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 155,          /* init_declarator  */
  YYSYMBOL_initializer = 156,              /* initializer  */
  YYSYMBOL_initializer_list = 157,         /* initializer_list  */
  YYSYMBOL_initializer_item = 158,         /* initializer_item  */
  YYSYMBOL_pointer = 159,                  /* pointer  */
  YYSYMBOL_declarator = 160,               /* declarator  */
  YYSYMBOL_abstract_declarator = 161,      /* abstract_declarator  */
  YYSYMBOL_direct_abstract_declarator = 162, /* direct_abstract_declarator  */
  YYSYMBOL_direct_declarator = 163,        /* direct_declarator  */
  YYSYMBOL_operator_function_id = 164,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 165,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 166,              /* param_scope  */
  YYSYMBOL_constructor_args = 167,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 168,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 169,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 170,           /* parameter_decl  */
  YYSYMBOL_function_definition = 171,      /* function_definition  */
  YYSYMBOL_172_15 = 172,                   /* $@15  */
  YYSYMBOL_statement = 173,                /* statement  */
  YYSYMBOL_compound_stmt = 174,            /* compound_stmt  */
  YYSYMBOL_175_16 = 175,                   /* $@16  */
  YYSYMBOL_block_item_list_opt = 176,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 177,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 178,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 179,           /* selection_stmt  */
  YYSYMBOL_180_17 = 180,                   /* $@17  */
  YYSYMBOL_labeled_stmt = 181,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 182,           /* iteration_stmt  */
  YYSYMBOL_for_open = 183,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 184,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 185,                /* jump_stmt  */
  YYSYMBOL_expr = 186,                     /* expr  */
  YYSYMBOL_assignment_expr = 187,          /* assignment_expr  */
  YYSYMBOL_assign_op = 188,                /* assign_op  */
  YYSYMBOL_constant_expr = 189,            /* constant_expr  */
  YYSYMBOL_binary_expr = 190,              /* binary_expr  */
  YYSYMBOL_unary_expr = 191,               /* unary_expr  */
  YYSYMBOL_type_name = 192,                /* type_name  */
  YYSYMBOL_type_name_specifiers = 193,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 194,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 195,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 196,             /* builtin_call  */
  YYSYMBOL_constructor_args_opt = 197,     /* constructor_args_opt  */
  YYSYMBOL_argument_list_opt = 198,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 199,            /* argument_list  */
  YYSYMBOL_argument = 200,                 /* argument  */
  YYSYMBOL_primary_expr = 201,             /* primary_expr  */
  YYSYMBOL_string_literal = 202            /* string_literal  */
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

    /* the struct/class tag of what a postfix expression denotes, so the
       Token_Type column can classify a member name after it: `p.x`,
       `arr[0].x`, `a.b.c`, `f().x`, `(*p).x`, `this->x` ("" if unknown) */
    static std::string aggregateOf(const ASTNodePtr &n) {
        if (!n) return "";
        switch (n->kind) {
            case ASTKind::Identifier: {
                const Symbol *s = lookupSymbol(n->label);
                return s ? s->aggregateTagName : "";
            }
            case ASTKind::ThisExpr: return currentClassName();
            case ASTKind::MemberExpr: case ASTKind::ArrowExpr: {
                const SymbolTableEntry *m = findMember(n->typeExpr ? n->typeExpr->className : aggregateOf(n->children[0]), n->label);
                return m ? m->aggregateTagName : "";
            }
            case ASTKind::IndexExpr: return aggregateOf(n->children[0]);
            case ASTKind::UnaryExpr: return n->label == "*" ? aggregateOf(n->children[0]) : "";
            case ASTKind::CallExpr: return n->children.empty() ? "" : aggregateOf(n->children[0]);
            default: return "";
        }
    }

#line 367 "build/parser.tab.cpp"

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
#define YYLAST   2216

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  117
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  86
/* YYNRULES -- Number of rules.  */
#define YYNRULES  345
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  612

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   347


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK                     \
   ? YY_CAST (yysymbol_kind_t, yytranslate[YYX])        \
   : YYSYMBOL_YYUNDEF)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_int8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   103,     2,     2,     2,    98,    91,     2,
     106,   115,    96,    94,   114,    95,   105,    97,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    88,   111,
      92,    86,    93,    87,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   107,     2,   116,    90,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   113,    89,   112,   104,     2,     2,     2,
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
      85,    99,   100,   101,   102,   108,   109,   110
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   141,   141,   145,   153,   154,   155,   156,   157,   161,
     192,   206,   210,   211,   212,   213,   214,   215,   216,   220,
     221,   222,   223,   224,   225,   226,   227,   228,   229,   230,
     231,   245,   252,   253,   257,   261,   257,   277,   277,   291,
     297,   303,   307,   303,   316,   316,   330,   336,   342,   348,
     354,   354,   365,   365,   375,   379,   375,   391,   391,   405,
     411,   420,   421,   428,   429,   433,   438,   446,   447,   451,
     452,   456,   457,   464,   470,   476,   482,   493,   498,   510,
     511,   512,   513,   522,   522,   540,   544,   552,   556,   552,
     576,   577,   578,   582,   583,   587,   588,   592,   593,   597,
     598,   599,   604,   612,   613,   617,   618,   621,   627,   628,
     629,   630,   631,   635,   641,   647,   648,   654,   658,   667,
     668,   669,   670,   674,   678,   685,   697,   706,   710,   717,
     724,   743,   750,   751,   756,   760,   760,   760,   760,   761,
     761,   761,   761,   762,   762,   762,   762,   763,   763,   763,
     763,   764,   764,   764,   764,   765,   765,   765,   766,   766,
     766,   767,   767,   767,   768,   768,   768,   769,   769,   769,
     776,   780,   781,   785,   786,   790,   794,   798,   802,   807,
     812,   820,   820,   885,   886,   887,   888,   889,   890,   891,
     892,   893,   897,   897,   906,   907,   911,   912,   916,   917,
     921,   924,   927,   927,   933,   936,   939,   947,   950,   957,
     961,   965,   968,   972,   981,   985,   986,   990,   991,   992,
     993,   994,  1004,  1005,  1009,  1010,  1016,  1017,  1018,  1019,
    1020,  1021,  1022,  1023,  1024,  1025,  1026,  1030,  1034,  1035,
    1036,  1037,  1038,  1039,  1040,  1041,  1042,  1043,  1044,  1045,
    1046,  1047,  1048,  1049,  1050,  1051,  1052,  1055,  1059,  1060,
    1061,  1062,  1063,  1064,  1065,  1066,  1067,  1068,  1072,  1073,
    1080,  1084,  1091,  1098,  1102,  1103,  1104,  1105,  1106,  1107,
    1108,  1109,  1110,  1111,  1112,  1113,  1114,  1123,  1129,  1135,
    1141,  1147,  1153,  1159,  1165,  1174,  1175,  1176,  1211,  1215,
    1223,  1229,  1233,  1234,  1235,  1236,  1240,  1241,  1242,  1243,
    1244,  1245,  1246,  1247,  1248,  1252,  1253,  1257,  1258,  1262,
    1263,  1267,  1268,  1275,  1284,  1285,  1286,  1287,  1288,  1289,
    1290,  1294,  1301,  1302,  1303,  1304,  1305,  1306,  1307,  1308,
    1309,  1310,  1311,  1318,  1323,  1324
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
  "CLASS", "UNION", "ENUM", "PUBLIC", "PRIVATE", "PROTECTED", "THIS",
  "STATIC", "TYPEDEF", "AUTO", "CONST", "FRIEND", "VIRTUAL", "EXPLICIT",
  "IF", "ELSE", "FOR", "WHILE", "DO", "UNTIL", "SWITCH", "CASE", "DEFAULT",
  "BREAK", "CONTINUE", "GOTO", "RETURN", "PRINTF", "SCANF", "MALLOC",
  "FREE", "CALLOC", "REALLOC", "BOOL", "SIZEOF", "VA_LIST", "VA_START",
  "VA_ARG", "VA_END", "OPERATOR", "FCAST", "ABSTRACT_LPAREN", "IDENTIFIER",
  "TYPE_NAME", "INT_LITERAL", "FLOAT_LITERAL", "CHAR_LITERAL",
  "STRING_LITERAL", "BOOL_LITERAL", "ARROW", "ELLIPSIS", "SCOPE_RES",
  "INC", "DEC", "SHL", "SHR", "LE_OP", "GE_OP", "EQ_OP", "NE_OP", "AND_OP",
  "OR_OP", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN",
  "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "SHL_ASSIGN",
  "SHR_ASSIGN", "PREFER_EXPRESSION", "'='", "'?'", "':'", "'|'", "'^'",
  "'&'", "'<'", "'>'", "'+'", "'-'", "'*'", "'/'", "'%'", "UMINUS", "ADDR",
  "DEREF", "CAST", "'!'", "'~'", "'.'", "'('", "'['", "SIZEOF_TYPE",
  "PREFER_DECLARATION", "IFX", "';'", "'}'", "'{'", "','", "')'", "']'",
  "$accept", "translation_unit", "external_decl", "declaration",
  "declaration_specifiers", "storage_or_type_specifier", "type_specifier",
  "tag_name", "struct_or_class_specifier", "$@1", "$@2", "@3", "$@4",
  "$@5", "@6", "$@7", "@8", "$@9", "$@10", "@11", "member_decl_list_opt",
  "enumerator_list", "enumerator", "comma_opt", "inheritance_opt",
  "inheritance_specifier_list", "inheritance_specifier",
  "member_decl_list", "member_item", "constructor_head", "$@12",
  "constructor_def", "out_of_class_special", "$@13", "$@14",
  "access_specifier", "init_declarator_list_opt", "init_declarator_list",
  "init_declarator", "initializer", "initializer_list", "initializer_item",
  "pointer", "declarator", "abstract_declarator",
  "direct_abstract_declarator", "direct_declarator",
  "operator_function_id", "overloadable_operator", "param_scope",
  "constructor_args", "parameter_list_opt", "parameter_list",
  "parameter_decl", "function_definition", "$@15", "statement",
  "compound_stmt", "$@16", "block_item_list_opt", "block_item_list",
  "expr_stmt", "selection_stmt", "$@17", "labeled_stmt", "iteration_stmt",
  "for_open", "for_incr_opt", "jump_stmt", "expr", "assignment_expr",
  "assign_op", "constant_expr", "binary_expr", "unary_expr", "type_name",
  "type_name_specifiers", "type_name_specifier", "postfix_expr",
  "builtin_call", "constructor_args_opt", "argument_list_opt",
  "argument_list", "argument", "primary_expr", "string_literal", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-432)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-196)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -432,  1944,  -432,   -58,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,   -37,   -27,    -6,    -4,  -432,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,   -38,  -432,  -432,  1794,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,   -72,   -44,  -432,  -432,
     -48,   -46,  -432,  -432,   -72,   -44,  -432,  -432,   -72,   -44,
    -432,  -432,    -9,  2019,    23,    50,  -432,  -432,   204,  -432,
      -3,    40,  -432,   187,   -69,   -26,  -432,  1998,    56,  1998,
     100,  1998,   104,   153,   118,   108,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,   120,
     117,  -432,    30,    94,    50,   126,  -432,   204,  -432,  -432,
    -432,   -26,  1139,   145,  1811,   441,  -432,  -432,  -432,   170,
    -432,  -432,   169,  1998,  -432,   -80,  -432,   191,  -432,  -432,
     180,    95,   193,   219,  -432,   215,   218,  -432,   153,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,   247,   229,
     230,   235,   236,   237,   239,   241,   242,   243,  -432,   245,
     248,   250,   261,   262,   263,   264,  1596,   266,   267,   268,
     270,  -432,   -43,  -432,  -432,  -432,  -432,  -432,  1663,  1663,
    1663,  1663,  1663,  1663,  1663,  1663,  1529,   991,  -432,  -432,
    2060,   354,   232,  -432,  -432,   305,   691,  2027,    33,  -432,
    -432,   265,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  1998,
    -432,  -432,  -432,   269,  -432,   103,  -432,  -432,  1998,  1663,
     153,   273,   218,  2027,  1663,  1663,  1663,  1663,  1663,  1663,
    1663,  1663,  1663,  1529,  1529,  1529,  1529,  1529,  1529,  1663,
    1529,  -432,  1529,  1529,  1529,  1663,   325,  1663,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,   229,   230,   235,   236,
     237,   239,   241,   242,   243,   142,   167,   189,   197,  -432,
     264,  -432,   -43,   140,  -432,   271,   259,  -432,   327,  1663,
    -432,  -432,   101,  -432,  1663,  1663,  1663,  1663,  1663,  1663,
    1663,  1663,  1663,  1663,  1663,  1663,  1663,  1663,  1663,  1663,
    1663,  1663,  1663,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,  -432,  1663,   231,   332,  -432,  -432,   234,
    1529,  1663,  -432,   207,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,   282,   283,   284,   917,   286,   287,  1663,
     306,   288,   290,   342,  1323,  -432,   310,   338,  -432,  -432,
    1794,  -432,  -432,   291,   804,  -432,  -432,  -432,  -432,  1250,
    -432,    41,  1460,   289,   292,  -432,  1663,  -432,  -432,  2027,
     691,   293,    95,  -432,  -432,  1998,   296,  -432,  2060,  -432,
    -432,  -432,   297,   295,   298,   299,   300,   303,   304,   307,
     308,   309,   328,   339,  -432,  -432,   340,   311,  -432,   341,
     343,   344,   348,   349,   350,   351,   353,   355,   356,   357,
    -432,   358,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
    1663,  -432,  1663,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,   133,  -432,   509,   184,  -432,   313,  -432,
     335,   326,  -432,  1065,   -60,   -60,   152,   152,  2118,  2118,
    2102,  2070,   -66,  2111,   593,  1426,   152,   152,    44,    44,
    -432,  -432,  -432,  -432,  -432,   347,  -432,  -432,   389,   359,
     114,  -432,  -432,  1663,  -432,  1663,    15,  1663,  1663,   369,
     917,  -432,  -432,   302,  -432,    98,   917,  -432,  -432,  1396,
    1396,  -432,   130,  -432,  -432,  -432,  1915,  -432,   360,   364,
    -432,  -432,   365,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,  1529,  -432,  -432,  -432,
    -432,  -432,  -432,  1730,  -432,  -432,  -432,  -432,  -432,  -432,
    -432,   363,  -432,   373,   313,   577,  1139,   383,  -432,  -432,
    1663,   424,   425,  -432,  -432,   194,   206,   382,   397,   208,
     210,   917,  -432,  -432,  -432,  -432,  1663,  1663,  -432,  -432,
    -432,  -432,  -432,   391,  -432,  -432,  -432,  -432,   379,  -432,
    1139,  2060,  -432,  -432,   917,   917,  -432,  1663,   917,  -432,
    -432,   393,   395,   396,  -432,  -432,  -432,   482,  -432,   213,
    -432,   391,   917,   917,   917,    26,  -432,  -432,  -432,  -432,
    -432,  -432
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    19,    20,    21,    22,    23,    25,
      26,    27,    28,     0,     0,     0,     0,    12,    14,    13,
      15,    16,    17,    24,    29,    30,     3,     5,    93,    11,
      18,    31,     6,     4,     7,     8,    39,    40,    37,    34,
      59,    60,    57,    54,    46,    47,    44,    41,    48,    49,
      52,    50,     0,     0,   123,    30,   109,   108,     0,    10,
       0,    94,    95,     0,    97,   114,   127,    61,     0,    61,
      69,    61,     0,     0,     0,     0,   156,   157,   154,   155,
     150,   151,   148,   149,   152,   153,   158,   159,   160,   161,
     162,   163,   164,   165,   166,   167,   145,   142,   140,   141,
     146,   147,   135,   136,   137,   138,   139,   144,   143,     0,
       0,   134,     0,     0,     0,     0,     9,     0,   112,   111,
     110,   113,     0,     0,   170,     0,    90,    91,    92,     0,
      30,    79,     0,    62,    77,     0,    82,     0,    80,    35,
       0,     0,     0,     0,    42,    65,    67,    63,     0,    87,
     169,   168,   124,   128,   125,   129,   126,    96,    97,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   329,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   323,     0,   324,   325,   326,   344,   328,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    98,    99,
     224,   257,   258,   305,   295,   327,     0,   173,     0,   171,
     132,     0,    83,    38,    78,    86,   192,    85,    81,    61,
      58,    75,    76,    70,    71,     0,    55,    45,    61,     0,
      68,     0,    67,   173,   315,   315,   315,   315,   315,   315,
     315,   315,   315,   317,   317,   317,   317,   317,   317,   315,
       0,   268,   317,   317,   317,   315,     0,   315,   259,   260,
     261,   263,   264,   262,   265,   266,   274,   275,   276,   277,
     278,   280,   281,   282,   283,     0,     0,     0,     0,   285,
     279,   284,   286,     0,   222,     0,   270,   273,     0,     0,
     100,   105,     0,   103,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   227,   228,   229,   230,   231,   232,   233,
     234,   235,   236,   226,     0,     0,     0,   303,   304,     0,
     317,     0,   345,     0,    19,    20,    21,    22,    23,    25,
      26,    27,    28,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    24,   323,    30,   198,   189,
      93,   196,   183,     0,     0,   184,   185,   188,   186,     0,
     187,     0,   180,     0,   174,   175,     0,   131,   133,   173,
       0,     0,     0,    73,    74,    61,     0,    66,   237,   257,
      64,    53,     0,     0,   316,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   321,   322,     0,   318,   319,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     342,     0,   287,   288,   293,   294,   289,   290,   291,   292,
       0,   343,     0,   274,   275,   276,   277,   278,   280,   281,
     282,   283,   279,     0,   286,     0,   115,   271,   117,   272,
       0,     0,   101,     0,   249,   250,   247,   248,   243,   244,
     239,   238,     0,   240,   241,   242,   245,   246,   251,   252,
     253,   254,   255,   225,   301,     0,   302,   298,     0,     0,
       0,   190,   191,     0,   214,     0,     0,     0,     0,     0,
       0,   217,   218,     0,   219,     0,     0,   182,   197,     0,
       0,   199,   115,   178,   179,   130,     0,   172,     0,     0,
      36,    72,     0,    43,    51,    88,   332,   333,   334,   335,
     336,   338,   339,   340,   341,   306,     0,   307,   308,   309,
     310,   311,   337,   269,   312,   313,   314,   331,   330,   223,
     267,     0,   119,     0,   116,     0,     0,     0,   102,   104,
       0,     0,     0,   297,   296,     0,     0,     0,     0,     0,
       0,     0,   205,   221,   220,   206,   215,   215,   177,   176,
      84,   193,    56,     0,   320,   118,   120,   121,     0,   106,
       0,   256,   300,   299,     0,     0,   210,     0,     0,   202,
     204,     0,   216,     0,    89,   122,   107,   200,   207,     0,
     211,     0,     0,     0,     0,     0,   203,   213,   212,   201,
     209,   208
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -432,  -432,  -432,     6,    -1,   -20,  -432,   188,  -432,  -432,
    -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,  -432,
     -39,   374,   294,   301,  -432,  -432,   139,  -432,   390,  -432,
    -432,  -432,  -432,  -432,  -432,  -131,  -432,  -432,   408,  -118,
    -432,    73,  -262,   -19,  -359,  -431,   -61,   217,  -432,  -432,
     403,  -222,  -432,    24,   528,  -432,  -300,  -134,  -432,   151,
    -432,  -355,  -432,  -432,  -432,  -432,  -432,   -33,  -432,  -171,
    -119,  -432,  -277,  -206,  -133,  -176,  -432,   252,  -432,  -432,
     122,   -53,  -432,    13,  -432,  -432
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    26,   359,   360,    29,    30,    39,    31,    68,
     219,    67,    72,   228,    71,    74,    73,    70,   385,    69,
     132,   146,   147,   231,   142,   223,   224,   133,   134,   135,
     379,   136,    32,   233,   573,   137,    60,    61,    62,   291,
     292,   293,    63,   158,   447,   448,    65,    66,   111,   207,
     394,   373,   374,   375,   138,   123,   361,   362,   380,   363,
     364,   365,   366,   601,   367,   368,   369,   591,   370,   371,
     284,   324,   387,   200,   201,   405,   286,   287,   202,   203,
     395,   406,   407,   408,   204,   205
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      28,   217,   121,   199,   198,   209,   211,    27,    59,    64,
     225,   393,   451,   504,   500,   544,   557,   122,    36,    37,
     285,   256,   550,   388,   446,   283,    52,   610,    40,    41,
     140,   215,   143,   216,   308,   309,   310,   311,   312,   115,
     -32,   -32,   -33,   251,  -181,   558,   486,    75,   430,    44,
      45,    48,    49,    34,    35,   258,   259,   260,   261,   262,
     263,   264,   265,   257,   498,   -32,    28,   -33,    28,   -33,
      28,   544,   489,   131,   415,   131,    38,   131,   199,   283,
     124,   125,    53,   388,   541,   152,    42,   112,   454,   455,
     456,   457,   458,   459,   460,   461,   389,   463,   464,   465,
     466,   467,   468,   469,   470,   471,   472,    46,   116,    50,
     502,   126,   127,   128,   113,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   404,   404,   404,   404,   404,   404,
     209,   462,    28,   404,   404,   404,   209,   611,   209,   131,
     310,   311,   312,   388,   566,   567,    53,   376,   377,   154,
     221,   222,   501,   118,   117,   430,   389,   508,   383,   384,
     480,   389,   389,   389,   389,   389,   389,   389,   389,   139,
     389,   389,   389,   389,   389,   389,   389,   389,   389,   389,
     381,   446,    53,   495,   443,    54,   114,   443,   141,   386,
     562,   409,   410,   411,   412,   413,   565,   422,   423,   416,
     417,   418,    43,    47,    51,   473,   372,   118,   145,   564,
     118,   404,   430,   452,   149,   453,   389,   144,    28,   294,
     295,   119,   424,   425,    56,   131,   120,    28,   430,    57,
     554,   148,   372,   151,   131,   150,    58,   445,   443,    53,
     445,   156,    54,   114,   426,   427,   308,   309,   310,   311,
     312,   225,   428,   429,   430,   431,    53,   507,   206,    54,
     114,   590,   433,   434,   435,   436,   437,   438,   439,   440,
     441,   275,   276,   277,   278,   119,   212,   479,   119,   218,
     120,   213,   279,   120,   597,   598,   474,   475,   600,   477,
     478,   445,   220,    58,   325,    56,   326,   327,   328,   540,
      57,   229,   607,   608,   609,   442,   226,   281,   430,   584,
      58,   539,   555,   443,   556,   444,   559,   560,   481,   482,
     430,   585,   430,   588,   430,   589,   543,   430,   605,   153,
     155,   227,   230,   122,   199,   234,   235,   329,   330,   331,
      59,   236,   237,   238,   581,   239,   512,   240,   241,   242,
      56,   243,    59,   503,   244,    57,   245,   396,   397,   398,
     399,   400,   401,   402,   403,   332,   445,   246,   247,   248,
     249,   414,   252,   253,   254,   499,   255,   419,   372,   421,
     420,   378,   450,   382,    28,   391,   432,   476,   483,   484,
     485,   131,   487,   488,   490,   592,   592,   493,   496,   491,
     540,   492,   256,   497,   505,   510,   506,   404,   513,   514,
     515,   551,   376,   563,   516,   517,   599,   389,   518,   519,
     545,   546,   520,   521,   522,   526,   578,   199,   579,   313,
     314,   315,   316,   317,   318,   319,   320,   321,   322,   594,
     323,   121,   547,   523,   159,   160,   161,   162,   163,   164,
     165,   166,   167,   552,   524,   525,   527,   561,   528,   529,
     168,   199,   596,   530,   531,   532,   533,   606,   534,   580,
     535,   536,   537,   538,   553,   570,   571,   572,   575,   582,
     583,   169,   170,   171,   172,   173,   174,   175,   176,   576,
     177,   178,   179,   586,   180,   595,   181,   182,   183,   184,
     185,   186,   187,   587,   216,   372,   188,   189,   602,   430,
     604,   603,   159,   160,   161,   162,   163,   164,   165,   166,
     167,   511,   232,   214,   390,   157,   549,   208,   168,    33,
     569,   509,   190,   392,   593,   191,   192,   193,   449,   574,
       0,     0,     0,     0,   194,   195,     0,   196,     0,   169,
     170,   171,   172,   173,   174,   175,   176,   210,   177,   178,
     179,     0,   180,     0,   181,   182,   183,   184,   185,   186,
     187,     0,     0,     0,   188,   189,     0,     0,     0,     0,
     159,   160,   161,   162,   163,   164,   165,   166,   167,     0,
       0,     0,     0,     0,     0,     0,   168,     0,     0,     0,
     190,     0,     0,   191,   192,   193,     0,     0,     0,     0,
       0,     0,   194,   195,     0,   196,     0,   169,   170,   171,
     172,   173,   174,   175,   176,   542,   177,   178,   179,     0,
     180,     0,   181,   182,   183,   184,   185,   186,   187,     0,
       0,     0,   188,   189,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     294,   295,   296,   297,   298,   299,     0,     0,   190,     0,
       0,   191,   192,   193,     0,     0,     0,     0,     0,     0,
     194,   195,     0,   196,   305,   306,   307,   308,   309,   310,
     311,   312,   333,   577,   334,   335,   336,   337,   338,   339,
     340,   341,   342,    13,    14,    15,    16,     0,     0,     0,
     168,    17,    18,    19,    20,    21,    22,     0,   343,     0,
     344,   345,   346,   347,   348,   349,   350,   351,   352,   353,
     354,   169,   170,   171,   172,   173,   174,   355,   176,    24,
     177,   178,   179,     0,   180,     0,   356,   357,   183,   184,
     185,   186,   187,     0,     0,     0,   188,   189,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   190,     0,     0,   191,   192,   193,     0,     0,
       0,     0,     0,     0,   194,   195,     0,   196,     0,     0,
       0,     0,   358,  -194,   216,   333,     0,   334,   335,   336,
     337,   338,   339,   340,   341,   342,    13,    14,    15,    16,
       0,     0,     0,   168,    17,    18,    19,    20,    21,    22,
       0,   343,     0,   344,   345,   346,   347,   348,   349,   350,
     351,   352,   353,   354,   169,   170,   171,   172,   173,   174,
     355,   176,    24,   177,   178,   179,     0,   180,     0,   356,
     357,   183,   184,   185,   186,   187,     0,     0,     0,   188,
     189,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   190,     0,     0,   191,   192,
     193,     0,     0,     0,     0,     0,     0,   194,   195,     0,
     196,     0,     0,     0,     0,   358,  -195,   216,   333,     0,
     334,   335,   336,   337,   338,   339,   340,   341,   342,    13,
      14,    15,    16,     0,     0,     0,   168,    17,    18,    19,
      20,    21,    22,     0,   343,     0,   344,   345,   346,   347,
     348,   349,   350,   351,   352,   353,   354,   169,   170,   171,
     172,   173,   174,   355,   176,    24,   177,   178,   179,     0,
     180,     0,   356,   357,   183,   184,   185,   186,   187,     0,
       0,     0,   188,   189,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   159,   160,   161,   162,   163,   164,
     165,   166,   167,     0,     0,     0,     0,     0,   190,     0,
     168,   191,   192,   193,     0,     0,     0,     0,     0,     0,
     194,   195,     0,   196,     0,     0,     0,     0,   358,     0,
     216,   169,   170,   171,   172,   173,   174,   175,   176,     0,
     177,   178,   179,     0,   180,     0,   181,   182,   183,   184,
     185,   186,   187,     0,     0,     0,   188,   189,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   159,   160,
     161,   162,   163,   164,   165,   166,   167,     0,     0,     0,
       0,     0,   190,     0,   168,   191,   192,   193,     0,     0,
       0,     0,     0,     0,   194,   195,   288,   196,   289,     0,
       0,     0,     0,   290,   197,   169,   170,   171,   172,   173,
     174,   175,   176,     0,   177,   178,   179,     0,   180,     0,
     181,   182,   183,   184,   185,   186,   187,     0,     0,     0,
     188,   189,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   159,   160,   161,   162,   163,   164,   165,   166,
     167,     0,     0,     0,     0,     0,   190,     0,   168,   191,
     192,   193,     0,     0,     0,     0,     0,     0,   194,   195,
     288,   196,   289,     0,     0,     0,     0,   548,   197,   169,
     170,   171,   172,   173,   174,   175,   176,     0,   177,   178,
     179,     0,   180,     0,   181,   182,   183,   184,   185,   186,
     187,     0,     0,     0,   188,   189,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     190,     0,     0,   191,   192,   193,     0,     0,     0,     0,
       0,     0,   194,   195,     0,   196,     0,     0,     0,     0,
       0,     0,   197,   334,   335,   336,   337,   338,   339,   340,
     341,   342,    13,    14,    15,    16,     0,     0,     0,   168,
      17,    18,    19,    20,    21,    22,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     169,   170,   171,   172,   173,   174,   355,   176,    24,   177,
     178,   179,     0,   180,     0,   181,   357,   183,   184,   185,
     186,   187,     0,     0,     0,   188,   189,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   159,   160,   161,   162,
     163,   164,   165,   166,   167,     0,     0,     0,     0,     0,
       0,   190,   168,     0,   191,   192,   193,     0,     0,     0,
       0,     0,     0,   194,   195,     0,   196,     0,     0,     0,
       0,   358,     0,   169,   170,   171,   172,   173,   174,   175,
     176,     0,   177,   178,   179,     0,   180,     0,   181,   182,
     183,   184,   185,   186,   187,     0,     0,     0,   188,   189,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   159,
     160,   161,   162,   163,   164,   165,   166,   167,     0,     0,
       0,     0,     0,     0,   190,   168,     0,   191,   192,   193,
       0,     0,     0,     0,     0,     0,   194,   195,     0,   196,
       0,     0,     0,     0,   494,     0,   169,   170,   171,   172,
     173,   174,   175,   176,     0,   177,   178,   179,     0,   180,
       0,   181,   182,   183,   184,   185,   186,   187,     0,     0,
       0,   188,   189,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,     0,     0,     0,     0,
      17,    18,    19,    20,    21,    22,     0,   190,     0,     0,
     191,   192,   193,   294,   295,   296,   297,   298,   299,   194,
     195,     0,   196,     0,     0,     0,    23,   358,    24,     0,
       0,     0,    53,     0,   443,    54,    55,     0,   306,   307,
     308,   309,   310,   311,   312,     0,     0,     0,     0,     0,
       0,     0,   266,   267,   268,   269,   270,   271,   272,   273,
     274,   275,   276,   277,   278,     0,     0,     0,   168,     0,
       0,    56,   279,     0,     0,     0,    57,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    58,   445,     0,   169,
     170,   171,   172,   173,   174,   280,   176,   281,   177,   178,
     179,     0,   180,     0,   181,   282,   183,   184,   185,   186,
     187,     0,     0,     0,   188,   189,     0,     0,     0,   159,
     160,   161,   162,   163,   164,   165,   166,   167,     0,     0,
       0,     0,     0,     0,     0,   168,     0,     0,     0,     0,
     190,     0,     0,   191,   192,   193,     0,     0,     0,     0,
       0,     0,   194,   195,     0,   196,   169,   170,   171,   172,
     173,   174,   175,   176,     0,   177,   178,   179,     0,   180,
       0,   181,   182,   183,   184,   185,   186,   187,     0,     0,
       0,   188,   189,     0,     0,     0,   159,   160,   161,   162,
     163,   164,   165,   166,   167,     0,     0,     0,     0,     0,
       0,     0,   168,     0,     0,     0,     0,   190,     0,     0,
     191,   192,   193,     0,     0,     0,     0,     0,     0,   194,
     195,     0,   250,   169,   170,   171,   172,   173,   174,   175,
     176,     0,   177,   178,   179,     0,   180,     0,   181,   182,
     183,   184,   185,   186,   187,     0,     0,     0,   188,   189,
       0,     0,     0,   159,   160,   161,   162,   163,   164,   165,
     166,   167,     0,     0,     0,     0,     0,     0,     0,   168,
       0,     0,     0,     0,   190,     0,     0,   191,   192,   193,
       0,     0,     0,     0,     0,     0,   194,   195,     0,   196,
     169,   170,   171,   172,   173,   174,   175,   176,     0,   177,
     178,   179,     0,   180,     0,   181,   182,   183,   184,   185,
     186,   187,     0,     0,     0,   188,   189,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
       0,     0,     0,     0,    17,    18,    19,    20,    21,    22,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     168,     0,     0,   194,   195,     0,   196,     0,     0,     0,
      23,     0,    24,     0,     0,     0,    53,     0,     0,    54,
      55,   169,   170,   171,   172,   173,   174,     0,   176,     0,
     177,   178,   179,     0,   180,     0,   181,     0,   183,   184,
     185,   186,   187,     0,     0,     0,   188,   189,     0,     0,
       0,     0,     0,     0,     0,    56,     0,     0,     0,     0,
      57,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      58,     0,   190,     0,     0,   191,   192,   193,     0,     0,
       0,     0,     0,     0,   194,   195,     0,   196,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,     0,     0,     0,     0,    17,    18,    19,    20,    21,
      22,     0,     0,     0,     2,     3,     0,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
       0,    23,     0,    24,    17,    18,    19,    20,    21,    22,
       0,   130,     0,     0,     0,     0,     0,     0,   568,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      23,     0,    24,     0,     0,     0,     0,     0,     0,     0,
      25,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,   126,   127,   128,     0,    17,    18,
      19,    20,    21,    22,     0,     0,     0,     0,     0,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,     0,    23,     0,    24,    17,    18,    19,
      20,    21,    22,   129,   130,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    23,     0,    24,     0,     0,     0,     0,
       0,     0,     0,   130,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,    87,    88,    89,    90,    91,
      92,    93,    94,    95,     0,    96,     0,     0,    97,    98,
      99,   100,   101,   102,   103,   104,   105,   106,     0,     0,
       0,     0,   107,   108,     0,   109,   110,   294,   295,   296,
     297,   298,   299,   300,   301,     0,     0,   294,   295,   296,
     297,   298,   299,   300,     0,     0,     0,   302,     0,   303,
     304,   305,   306,   307,   308,   309,   310,   311,   312,   303,
     304,   305,   306,   307,   308,   309,   310,   311,   312,   294,
     295,   296,   297,   298,   299,     0,     0,     0,   294,   295,
     296,   297,   298,   299,     0,   294,   295,   296,   297,     0,
       0,   303,   304,   305,   306,   307,   308,   309,   310,   311,
     312,   304,   305,   306,   307,   308,   309,   310,   311,   312,
     306,   307,   308,   309,   310,   311,   312
};

static const yytype_int16 yycheck[] =
{
       1,   135,    63,   122,   122,   124,   125,     1,    28,    28,
     141,   233,   289,   372,   369,   446,     1,    86,    55,    56,
     196,    64,    88,   229,   286,   196,    64,     1,    55,    56,
      69,   111,    71,   113,    94,    95,    96,    97,    98,    58,
      88,   113,    88,   176,   113,    30,   346,    56,   114,    55,
      56,    55,    56,   111,   112,   188,   189,   190,   191,   192,
     193,   194,   195,   106,   364,   113,    67,   113,    69,   113,
      71,   502,   349,    67,   250,    69,   113,    71,   197,   250,
     106,   107,    52,   289,   443,    55,   113,    64,   294,   295,
     296,   297,   298,   299,   300,   301,   229,   303,   304,   305,
     306,   307,   308,   309,   310,   311,   312,   113,   111,   113,
     372,    16,    17,    18,    64,   234,   235,   236,   237,   238,
     239,   240,   241,   242,   243,   244,   245,   246,   247,   248,
     249,   302,   133,   252,   253,   254,   255,   111,   257,   133,
      96,    97,    98,   349,   499,   500,    52,   114,   115,    55,
      55,    56,   111,    23,   114,   114,   289,   379,    55,    56,
     331,   294,   295,   296,   297,   298,   299,   300,   301,   113,
     303,   304,   305,   306,   307,   308,   309,   310,   311,   312,
     219,   443,    52,   354,    54,    55,    56,    54,    88,   228,
     490,   244,   245,   246,   247,   248,   496,    55,    56,   252,
     253,   254,    14,    15,    16,   324,   207,    23,    55,   111,
      23,   330,   114,   112,   106,   114,   349,   113,   219,    67,
      68,    91,    55,    56,    91,   219,    96,   228,   114,    96,
     116,   113,   233,   116,   228,   115,   106,   107,    54,    52,
     107,   115,    55,    56,    55,    56,    94,    95,    96,    97,
      98,   382,    55,    56,   114,   115,    52,   376,   113,    55,
      56,   561,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    91,   106,   330,    91,    88,
      96,   112,    23,    96,   584,   585,    55,    56,   588,    55,
      56,   107,   112,   106,    62,    91,    64,    65,    66,   432,
      96,    86,   602,   603,   604,    46,   113,    48,   114,   115,
     106,   430,   483,    54,   485,    56,   487,   488,   111,   112,
     114,   115,   114,   115,   114,   115,   445,   114,   115,   112,
     113,   112,   114,    86,   453,   106,   106,   105,   106,   107,
     360,   106,   106,   106,   550,   106,   385,   106,   106,   106,
      91,   106,   372,   372,   106,    96,   106,   235,   236,   237,
     238,   239,   240,   241,   242,    60,   107,   106,   106,   106,
     106,   249,   106,   106,   106,   369,   106,   255,   379,   257,
      55,   116,    55,   114,   385,   112,   115,    55,   106,   106,
     106,   385,   106,   106,    88,   566,   567,    55,    88,   111,
     533,   111,    64,   112,   115,   112,   114,   526,   112,   112,
     115,    64,   114,   111,   115,   115,   587,   550,   115,   115,
     107,    86,   115,   115,   115,   114,   545,   546,   546,    75,
      76,    77,    78,    79,    80,    81,    82,    83,    84,   573,
      86,   502,   116,   115,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    64,   115,   115,   115,    88,   115,   115,
      19,   580,   580,   115,   115,   115,   115,   601,   115,    86,
     115,   115,   115,   115,   115,   115,   112,   112,   115,    55,
      55,    40,    41,    42,    43,    44,    45,    46,    47,   116,
      49,    50,    51,   111,    53,   116,    55,    56,    57,    58,
      59,    60,    61,   106,   113,   506,    65,    66,   115,   114,
      28,   115,     3,     4,     5,     6,     7,     8,     9,    10,
      11,   382,   148,   133,   230,   117,   453,   124,    19,     1,
     506,   380,    91,   232,   567,    94,    95,    96,   286,   526,
      -1,    -1,    -1,    -1,   103,   104,    -1,   106,    -1,    40,
      41,    42,    43,    44,    45,    46,    47,   116,    49,    50,
      51,    -1,    53,    -1,    55,    56,    57,    58,    59,    60,
      61,    -1,    -1,    -1,    65,    66,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    19,    -1,    -1,    -1,
      91,    -1,    -1,    94,    95,    96,    -1,    -1,    -1,    -1,
      -1,    -1,   103,   104,    -1,   106,    -1,    40,    41,    42,
      43,    44,    45,    46,    47,   116,    49,    50,    51,    -1,
      53,    -1,    55,    56,    57,    58,    59,    60,    61,    -1,
      -1,    -1,    65,    66,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      67,    68,    69,    70,    71,    72,    -1,    -1,    91,    -1,
      -1,    94,    95,    96,    -1,    -1,    -1,    -1,    -1,    -1,
     103,   104,    -1,   106,    91,    92,    93,    94,    95,    96,
      97,    98,     1,   116,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    -1,    -1,    -1,
      19,    20,    21,    22,    23,    24,    25,    -1,    27,    -1,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
      39,    40,    41,    42,    43,    44,    45,    46,    47,    48,
      49,    50,    51,    -1,    53,    -1,    55,    56,    57,    58,
      59,    60,    61,    -1,    -1,    -1,    65,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    -1,    -1,    94,    95,    96,    -1,    -1,
      -1,    -1,    -1,    -1,   103,   104,    -1,   106,    -1,    -1,
      -1,    -1,   111,   112,   113,     1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      -1,    -1,    -1,    19,    20,    21,    22,    23,    24,    25,
      -1,    27,    -1,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    48,    49,    50,    51,    -1,    53,    -1,    55,
      56,    57,    58,    59,    60,    61,    -1,    -1,    -1,    65,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    -1,    -1,    94,    95,
      96,    -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,
     106,    -1,    -1,    -1,    -1,   111,   112,   113,     1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    -1,    -1,    -1,    19,    20,    21,    22,
      23,    24,    25,    -1,    27,    -1,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    -1,
      53,    -1,    55,    56,    57,    58,    59,    60,    61,    -1,
      -1,    -1,    65,    66,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    91,    -1,
      19,    94,    95,    96,    -1,    -1,    -1,    -1,    -1,    -1,
     103,   104,    -1,   106,    -1,    -1,    -1,    -1,   111,    -1,
     113,    40,    41,    42,    43,    44,    45,    46,    47,    -1,
      49,    50,    51,    -1,    53,    -1,    55,    56,    57,    58,
      59,    60,    61,    -1,    -1,    -1,    65,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    -1,    91,    -1,    19,    94,    95,    96,    -1,    -1,
      -1,    -1,    -1,    -1,   103,   104,   105,   106,   107,    -1,
      -1,    -1,    -1,   112,   113,    40,    41,    42,    43,    44,
      45,    46,    47,    -1,    49,    50,    51,    -1,    53,    -1,
      55,    56,    57,    58,    59,    60,    61,    -1,    -1,    -1,
      65,    66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    -1,    -1,    -1,    -1,    -1,    91,    -1,    19,    94,
      95,    96,    -1,    -1,    -1,    -1,    -1,    -1,   103,   104,
     105,   106,   107,    -1,    -1,    -1,    -1,   112,   113,    40,
      41,    42,    43,    44,    45,    46,    47,    -1,    49,    50,
      51,    -1,    53,    -1,    55,    56,    57,    58,    59,    60,
      61,    -1,    -1,    -1,    65,    66,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    -1,    -1,    94,    95,    96,    -1,    -1,    -1,    -1,
      -1,    -1,   103,   104,    -1,   106,    -1,    -1,    -1,    -1,
      -1,    -1,   113,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    -1,    -1,    -1,    19,
      20,    21,    22,    23,    24,    25,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    -1,    53,    -1,    55,    56,    57,    58,    59,
      60,    61,    -1,    -1,    -1,    65,    66,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    19,    -1,    94,    95,    96,    -1,    -1,    -1,
      -1,    -1,    -1,   103,   104,    -1,   106,    -1,    -1,    -1,
      -1,   111,    -1,    40,    41,    42,    43,    44,    45,    46,
      47,    -1,    49,    50,    51,    -1,    53,    -1,    55,    56,
      57,    58,    59,    60,    61,    -1,    -1,    -1,    65,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    91,    19,    -1,    94,    95,    96,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,   106,
      -1,    -1,    -1,    -1,   111,    -1,    40,    41,    42,    43,
      44,    45,    46,    47,    -1,    49,    50,    51,    -1,    53,
      -1,    55,    56,    57,    58,    59,    60,    61,    -1,    -1,
      -1,    65,    66,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    -1,    -1,    -1,    -1,
      20,    21,    22,    23,    24,    25,    -1,    91,    -1,    -1,
      94,    95,    96,    67,    68,    69,    70,    71,    72,   103,
     104,    -1,   106,    -1,    -1,    -1,    46,   111,    48,    -1,
      -1,    -1,    52,    -1,    54,    55,    56,    -1,    92,    93,
      94,    95,    96,    97,    98,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    -1,    -1,    -1,    19,    -1,
      -1,    91,    23,    -1,    -1,    -1,    96,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   106,   107,    -1,    40,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      51,    -1,    53,    -1,    55,    56,    57,    58,    59,    60,
      61,    -1,    -1,    -1,    65,    66,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    19,    -1,    -1,    -1,    -1,
      91,    -1,    -1,    94,    95,    96,    -1,    -1,    -1,    -1,
      -1,    -1,   103,   104,    -1,   106,    40,    41,    42,    43,
      44,    45,    46,    47,    -1,    49,    50,    51,    -1,    53,
      -1,    55,    56,    57,    58,    59,    60,    61,    -1,    -1,
      -1,    65,    66,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    19,    -1,    -1,    -1,    -1,    91,    -1,    -1,
      94,    95,    96,    -1,    -1,    -1,    -1,    -1,    -1,   103,
     104,    -1,   106,    40,    41,    42,    43,    44,    45,    46,
      47,    -1,    49,    50,    51,    -1,    53,    -1,    55,    56,
      57,    58,    59,    60,    61,    -1,    -1,    -1,    65,    66,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    19,
      -1,    -1,    -1,    -1,    91,    -1,    -1,    94,    95,    96,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,   106,
      40,    41,    42,    43,    44,    45,    46,    47,    -1,    49,
      50,    51,    -1,    53,    -1,    55,    56,    57,    58,    59,
      60,    61,    -1,    -1,    -1,    65,    66,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      -1,    -1,    -1,    -1,    20,    21,    22,    23,    24,    25,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      19,    -1,    -1,   103,   104,    -1,   106,    -1,    -1,    -1,
      46,    -1,    48,    -1,    -1,    -1,    52,    -1,    -1,    55,
      56,    40,    41,    42,    43,    44,    45,    -1,    47,    -1,
      49,    50,    51,    -1,    53,    -1,    55,    -1,    57,    58,
      59,    60,    61,    -1,    -1,    -1,    65,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    -1,    -1,    -1,    -1,
      96,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     106,    -1,    91,    -1,    -1,    94,    95,    96,    -1,    -1,
      -1,    -1,    -1,    -1,   103,   104,    -1,   106,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    -1,    -1,    -1,    -1,    20,    21,    22,    23,    24,
      25,    -1,    -1,    -1,     0,     1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      -1,    46,    -1,    48,    20,    21,    22,    23,    24,    25,
      -1,    56,    -1,    -1,    -1,    -1,    -1,    -1,    63,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      46,    -1,    48,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      56,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    -1,    20,    21,
      22,    23,    24,    25,    -1,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    -1,    46,    -1,    48,    20,    21,    22,
      23,    24,    25,    55,    56,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    46,    -1,    48,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    56,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    -1,    86,    -1,    -1,    89,    90,
      91,    92,    93,    94,    95,    96,    97,    98,    -1,    -1,
      -1,    -1,   103,   104,    -1,   106,   107,    67,    68,    69,
      70,    71,    72,    73,    74,    -1,    -1,    67,    68,    69,
      70,    71,    72,    73,    -1,    -1,    -1,    87,    -1,    89,
      90,    91,    92,    93,    94,    95,    96,    97,    98,    89,
      90,    91,    92,    93,    94,    95,    96,    97,    98,    67,
      68,    69,    70,    71,    72,    -1,    -1,    -1,    67,    68,
      69,    70,    71,    72,    -1,    67,    68,    69,    70,    -1,
      -1,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    90,    91,    92,    93,    94,    95,    96,    97,    98,
      92,    93,    94,    95,    96,    97,    98
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   118,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    20,    21,    22,
      23,    24,    25,    46,    48,    56,   119,   120,   121,   122,
     123,   125,   149,   171,   111,   112,    55,    56,   113,   124,
      55,    56,   113,   124,    55,    56,   113,   124,    55,    56,
     113,   124,    64,    52,    55,    56,    91,    96,   106,   122,
     153,   154,   155,   159,   160,   163,   164,   128,   126,   136,
     134,   131,   129,   133,   132,    56,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    83,    84,    86,    89,    90,    91,
      92,    93,    94,    95,    96,    97,    98,   103,   104,   106,
     107,   165,    64,    64,    56,   160,   111,   114,    23,    91,
      96,   163,    86,   172,   106,   107,    16,    17,    18,    55,
      56,   120,   137,   144,   145,   146,   148,   152,   171,   113,
     137,    88,   141,   137,   113,    55,   138,   139,   113,   106,
     115,   116,    55,   164,    55,   164,   115,   155,   160,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    19,    40,
      41,    42,    43,    44,    45,    46,    47,    49,    50,    51,
      53,    55,    56,    57,    58,    59,    60,    61,    65,    66,
      91,    94,    95,    96,   103,   104,   106,   113,   156,   187,
     190,   191,   195,   196,   201,   202,   113,   166,   167,   187,
     116,   187,   106,   112,   145,   111,   113,   174,    88,   127,
     112,    55,    56,   142,   143,   152,   113,   112,   130,    86,
     114,   140,   138,   150,   106,   106,   106,   106,   106,   106,
     106,   106,   106,   106,   106,   106,   106,   106,   106,   106,
     106,   191,   106,   106,   106,   106,    64,   106,   191,   191,
     191,   191,   191,   191,   191,   191,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    23,
      46,    48,    56,   186,   187,   192,   193,   194,   105,   107,
     112,   156,   157,   158,    67,    68,    69,    70,    71,    72,
      73,    74,    87,    89,    90,    91,    92,    93,    94,    95,
      96,    97,    98,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    86,   188,    62,    64,    65,    66,   105,
     106,   107,    60,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    27,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    46,    55,    56,   111,   120,
     121,   173,   174,   176,   177,   178,   179,   181,   182,   183,
     185,   186,   121,   168,   169,   170,   114,   115,   116,   147,
     175,   137,   114,    55,    56,   135,   137,   189,   190,   191,
     139,   112,   140,   168,   167,   197,   197,   197,   197,   197,
     197,   197,   197,   197,   187,   192,   198,   199,   200,   198,
     198,   198,   198,   198,   197,   192,   198,   198,   198,   197,
      55,   197,    55,    56,    55,    56,    55,    56,    55,    56,
     114,   115,   115,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    46,    54,    56,   107,   159,   161,   162,   194,
      55,   189,   112,   114,   190,   190,   190,   190,   190,   190,
     190,   190,   186,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   190,   187,    55,    56,    55,    55,    56,   198,
     186,   111,   112,   106,   106,   106,   173,   106,   106,   189,
      88,   111,   111,    55,   111,   186,    88,   112,   173,   120,
     178,   111,   159,   160,   161,   115,   114,   187,   168,   176,
     112,   143,   137,   112,   112,   115,   115,   115,   115,   115,
     115,   115,   115,   115,   115,   115,   114,   115,   115,   115,
     115,   115,   115,   115,   115,   115,   115,   115,   115,   187,
     191,   161,   116,   187,   162,   107,    86,   116,   112,   158,
      88,    64,    64,   115,   116,   186,   186,     1,    30,   186,
     186,    88,   173,   111,   111,   173,   178,   178,    63,   170,
     115,   112,   112,   151,   200,   115,   116,   116,   187,   156,
      86,   190,    55,    55,   115,   115,   111,   106,   115,   115,
     173,   184,   186,   184,   174,   116,   156,   173,   173,   186,
     173,   180,   115,   115,    28,   115,   174,   173,   173,   173,
       1,   111
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   117,   118,   118,   119,   119,   119,   119,   119,   120,
     121,   121,   122,   122,   122,   122,   122,   122,   122,   123,
     123,   123,   123,   123,   123,   123,   123,   123,   123,   123,
     123,   123,   124,   124,   126,   127,   125,   128,   125,   125,
     125,   129,   130,   125,   131,   125,   125,   125,   125,   125,
     132,   125,   133,   125,   134,   135,   125,   136,   125,   125,
     125,   137,   137,   138,   138,   139,   139,   140,   140,   141,
     141,   142,   142,   143,   143,   143,   143,   144,   144,   145,
     145,   145,   145,   147,   146,   148,   148,   150,   151,   149,
     152,   152,   152,   153,   153,   154,   154,   155,   155,   156,
     156,   156,   156,   157,   157,   158,   158,   158,   159,   159,
     159,   159,   159,   160,   160,   161,   161,   161,   162,   162,
     162,   162,   162,   163,   163,   163,   163,   163,   163,   163,
     163,   163,   163,   163,   164,   165,   165,   165,   165,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   165,
     166,   167,   167,   168,   168,   169,   169,   169,   170,   170,
     170,   172,   171,   173,   173,   173,   173,   173,   173,   173,
     173,   173,   175,   174,   176,   176,   177,   177,   178,   178,
     179,   179,   180,   179,   181,   181,   181,   182,   182,   182,
     182,   182,   182,   182,   183,   184,   184,   185,   185,   185,
     185,   185,   186,   186,   187,   187,   188,   188,   188,   188,
     188,   188,   188,   188,   188,   188,   188,   189,   190,   190,
     190,   190,   190,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   190,   190,   190,   190,   190,   190,   191,   191,
     191,   191,   191,   191,   191,   191,   191,   191,   191,   191,
     192,   192,   193,   193,   194,   194,   194,   194,   194,   194,
     194,   194,   194,   194,   194,   194,   194,   194,   194,   194,
     194,   194,   194,   194,   194,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   196,   196,   196,   196,
     196,   196,   196,   196,   196,   197,   197,   198,   198,   199,
     199,   200,   200,   201,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   202,   202
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     0,     0,     7,     0,     5,     2,
       2,     0,     0,     7,     0,     5,     2,     2,     2,     2,
       0,     7,     0,     6,     0,     0,     8,     0,     5,     2,
       2,     0,     1,     1,     3,     1,     3,     0,     1,     0,
       2,     1,     3,     2,     2,     1,     1,     1,     2,     1,
       1,     2,     1,     0,     5,     2,     2,     0,     0,     9,
       1,     1,     1,     0,     1,     1,     3,     1,     3,     1,
       2,     3,     4,     1,     3,     1,     4,     5,     1,     1,
       2,     2,     2,     2,     1,     1,     2,     1,     3,     2,
       3,     3,     4,     1,     3,     3,     3,     1,     3,     3,
       5,     4,     3,     4,     2,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     2,     2,
       0,     1,     3,     0,     1,     1,     3,     3,     2,     2,
       1,     0,     6,     1,     1,     1,     1,     1,     1,     1,
       2,     2,     0,     4,     0,     1,     1,     2,     1,     2,
       5,     7,     0,     6,     4,     3,     3,     5,     7,     7,
       4,     5,     6,     6,     2,     0,     1,     2,     2,     2,
       3,     3,     1,     3,     1,     3,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     5,     1,     1,     2,
       2,     2,     2,     2,     2,     2,     2,     4,     2,     4,
       1,     2,     2,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     1,     4,     4,     3,     5,
       5,     3,     3,     2,     2,     1,     4,     4,     4,     4,
       4,     4,     4,     4,     4,     0,     1,     0,     1,     1,
       3,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       4,     4,     4,     4,     4,     4,     4,     4,     4,     4,
       4,     4,     3,     3,     1,     2
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
#line 141 "../phase2-parser/src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2486 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 145 "../phase2-parser/src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2496 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 153 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2502 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 154 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2508 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 155 "../phase2-parser/src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2514 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 156 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2520 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 157 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2526 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 161 "../phase2-parser/src/parser.y"
                                                          {
          endDeclaratorList();
          std::vector<ASTNodePtr> declNodes;
          for (auto &d : yyvsp[-1].paramList) {
              auto n = registerDeclarator(d, yyvsp[-2].typeSpec);
              if (n) declNodes.push_back(n);
          }
          if (declNodes.empty() && yyvsp[-2].typeSpec.isFriend) { /* `friend class Cat;` */
              std::string who = !yyvsp[-2].typeSpec.tagName.empty() ? yyvsp[-2].typeSpec.tagName : yyvsp[-2].typeSpec.typedefName;
              yyval.node = atToken(mkNode(ASTKind::FriendDecl, who), yyvsp[-2].idx);
          } else if (declNodes.empty()) {
              yyval.node = yyvsp[-2].node; /* bare struct/class declaration */
              /* `struct { int i; float f; };` inside a struct: its members
                 are the enclosing struct's (an anonymous member) */
              if (isAnonymousTag(yyvsp[-2].typeSpec.tagName) && yyvsp[-2].node) {
                  if (atAggregateMemberLevel())
                      addAnonymousMember(currentClassName(), yyvsp[-2].typeSpec.tagName);
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
#line 2559 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 192 "../phase2-parser/src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          yyval.typeSpec.storageClasses += yyvsp[0].typeSpec.storageClasses;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isAuto) yyval.typeSpec.isAuto = true;
          if (yyvsp[0].typeSpec.isFriend) yyval.typeSpec.isFriend = true;
          if (yyvsp[0].typeSpec.isVirtual) yyval.typeSpec.isVirtual = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2578 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 206 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2584 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 210 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2590 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: AUTO  */
#line 211 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2596 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: TYPEDEF  */
#line 212 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2602 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: CONST  */
#line 213 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2608 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: FRIEND  */
#line 214 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isFriend = true; }
#line 2614 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: VIRTUAL  */
#line 215 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isVirtual = true; }
#line 2620 "build/parser.tab.cpp"
    break;

  case 18: /* storage_or_type_specifier: type_specifier  */
#line 216 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2626 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: INT  */
#line 220 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2632 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: CHAR  */
#line 221 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2638 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: FLOAT  */
#line 222 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2644 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: DOUBLE  */
#line 223 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2650 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: VOID  */
#line 224 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2656 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: BOOL  */
#line 225 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2662 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: SHORT  */
#line 226 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2668 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: LONG  */
#line 227 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2674 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: SIGNED  */
#line 228 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2680 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: UNSIGNED  */
#line 229 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2686 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: VA_LIST  */
#line 230 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2692 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: TYPE_NAME  */
#line 231 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
          if (s && (s->kind == SymKind::STRUCT_TAG || s->kind == SymKind::CLASS_TAG || s->kind == SymKind::UNION_TAG)) {
              yyval.typeSpec.tagName = yyvsp[0].str; /* "Dog d;" -- Dog referenced directly,
                                                without repeating class/struct */
          } else if (s && s->kind == SymKind::TYPEDEF_NAME && s->typeExpr && s->typeExpr->pointerLevel == 0 &&
                     s->typeExpr->arrayDims.empty() && !s->typeExpr->isFunction) {
              yyval.typeSpec.tagName = s->typeExpr->tagName; /* `Pt p;` with `typedef struct {...} Pt;`:
                                                              p.x resolves through the struct */
          }
      }
#line 2711 "build/parser.tab.cpp"
    break;

  case 31: /* type_specifier: struct_or_class_specifier  */
#line 245 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2717 "build/parser.tab.cpp"
    break;

  case 32: /* tag_name: IDENTIFIER  */
#line 252 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2723 "build/parser.tab.cpp"
    break;

  case 33: /* tag_name: TYPE_NAME  */
#line 253 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2729 "build/parser.tab.cpp"
    break;

  case 34: /* $@1: %empty  */
#line 257 "../phase2-parser/src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2739 "build/parser.tab.cpp"
    break;

  case 35: /* $@2: %empty  */
#line 261 "../phase2-parser/src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2745 "build/parser.tab.cpp"
    break;

  case 36: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 261 "../phase2-parser/src/parser.y"
                                                                                                    {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str); /* usable as a type from here on, but
                                             NOT inside its own body -- lets
                                             constructors keep
                                             matching the class's own name as
                                             a plain IDENTIFIER */
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2763 "build/parser.tab.cpp"
    break;

  case 37: /* @3: %empty  */
#line 277 "../phase2-parser/src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2775 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 283 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2788 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 291 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2799 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 297 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2810 "build/parser.tab.cpp"
    break;

  case 41: /* $@4: %empty  */
#line 303 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "UNION");
          enterClass(yyvsp[0].str, "union");
      }
#line 2820 "build/parser.tab.cpp"
    break;

  case 42: /* $@5: %empty  */
#line 307 "../phase2-parser/src/parser.y"
            { pushScope("union " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2826 "build/parser.tab.cpp"
    break;

  case 43: /* struct_or_class_specifier: UNION tag_name $@4 '{' $@5 member_decl_list_opt '}'  */
#line 307 "../phase2-parser/src/parser.y"
                                                                                                   {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::UnionDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2840 "build/parser.tab.cpp"
    break;

  case 44: /* @6: %empty  */
#line 316 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "union");
          pushScope("union " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2852 "build/parser.tab.cpp"
    break;

  case 45: /* struct_or_class_specifier: UNION '{' @6 member_decl_list_opt '}'  */
#line 322 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::UnionDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2865 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: UNION IDENTIFIER  */
#line 330 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2876 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: UNION TYPE_NAME  */
#line 336 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2887 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: ENUM IDENTIFIER  */
#line 342 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2898 "build/parser.tab.cpp"
    break;

  case 49: /* struct_or_class_specifier: ENUM TYPE_NAME  */
#line 348 "../phase2-parser/src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2909 "build/parser.tab.cpp"
    break;

  case 50: /* $@7: %empty  */
#line 354 "../phase2-parser/src/parser.y"
                    {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM");
      }
#line 2918 "build/parser.tab.cpp"
    break;

  case 51: /* struct_or_class_specifier: ENUM tag_name $@7 '{' enumerator_list comma_opt '}'  */
#line 357 "../phase2-parser/src/parser.y"
                                          {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2931 "build/parser.tab.cpp"
    break;

  case 52: /* @8: %empty  */
#line 365 "../phase2-parser/src/parser.y"
               {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[-1].idx});
      }
#line 2940 "build/parser.tab.cpp"
    break;

  case 53: /* struct_or_class_specifier: ENUM '{' @8 enumerator_list comma_opt '}'  */
#line 368 "../phase2-parser/src/parser.y"
                                      {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-3].str;
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-3].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2952 "build/parser.tab.cpp"
    break;

  case 54: /* $@9: %empty  */
#line 375 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2962 "build/parser.tab.cpp"
    break;

  case 55: /* $@10: %empty  */
#line 379 "../phase2-parser/src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2968 "build/parser.tab.cpp"
    break;

  case 56: /* struct_or_class_specifier: CLASS tag_name $@9 inheritance_opt '{' $@10 member_decl_list_opt '}'  */
#line 379 "../phase2-parser/src/parser.y"
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
#line 2985 "build/parser.tab.cpp"
    break;

  case 57: /* @11: %empty  */
#line 391 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2997 "build/parser.tab.cpp"
    break;

  case 58: /* struct_or_class_specifier: CLASS '{' @11 member_decl_list_opt '}'  */
#line 397 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 3010 "build/parser.tab.cpp"
    break;

  case 59: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 405 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3021 "build/parser.tab.cpp"
    break;

  case 60: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 411 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3032 "build/parser.tab.cpp"
    break;

  case 61: /* member_decl_list_opt: %empty  */
#line 420 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3038 "build/parser.tab.cpp"
    break;

  case 62: /* member_decl_list_opt: member_decl_list  */
#line 421 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 3044 "build/parser.tab.cpp"
    break;

  case 63: /* enumerator_list: enumerator  */
#line 428 "../phase2-parser/src/parser.y"
                 { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3050 "build/parser.tab.cpp"
    break;

  case 64: /* enumerator_list: enumerator_list ',' enumerator  */
#line 429 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3056 "build/parser.tab.cpp"
    break;

  case 65: /* enumerator: IDENTIFIER  */
#line 433 "../phase2-parser/src/parser.y"
                 {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[0].str), yyvsp[0].idx);
      }
#line 3066 "build/parser.tab.cpp"
    break;

  case 66: /* enumerator: IDENTIFIER '=' constant_expr  */
#line 438 "../phase2-parser/src/parser.y"
                                   {
          declareSymbol(yyvsp[-2].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3076 "build/parser.tab.cpp"
    break;

  case 67: /* comma_opt: %empty  */
#line 446 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3082 "build/parser.tab.cpp"
    break;

  case 68: /* comma_opt: ','  */
#line 447 "../phase2-parser/src/parser.y"
          { yyval = ParserValue(); }
#line 3088 "build/parser.tab.cpp"
    break;

  case 69: /* inheritance_opt: %empty  */
#line 451 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3094 "build/parser.tab.cpp"
    break;

  case 70: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 452 "../phase2-parser/src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 3100 "build/parser.tab.cpp"
    break;

  case 71: /* inheritance_specifier_list: inheritance_specifier  */
#line 456 "../phase2-parser/src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 3106 "build/parser.tab.cpp"
    break;

  case 72: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 457 "../phase2-parser/src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 3115 "build/parser.tab.cpp"
    break;

  case 73: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 464 "../phase2-parser/src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3126 "build/parser.tab.cpp"
    break;

  case 74: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 470 "../phase2-parser/src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3137 "build/parser.tab.cpp"
    break;

  case 75: /* inheritance_specifier: IDENTIFIER  */
#line 476 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3148 "build/parser.tab.cpp"
    break;

  case 76: /* inheritance_specifier: TYPE_NAME  */
#line 482 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3159 "build/parser.tab.cpp"
    break;

  case 77: /* member_decl_list: member_item  */
#line 493 "../phase2-parser/src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 3169 "build/parser.tab.cpp"
    break;

  case 78: /* member_decl_list: member_decl_list member_item  */
#line 498 "../phase2-parser/src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 3183 "build/parser.tab.cpp"
    break;

  case 79: /* member_item: declaration  */
#line 510 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3189 "build/parser.tab.cpp"
    break;

  case 80: /* member_item: function_definition  */
#line 511 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3195 "build/parser.tab.cpp"
    break;

  case 81: /* member_item: access_specifier ':'  */
#line 512 "../phase2-parser/src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3201 "build/parser.tab.cpp"
    break;

  case 82: /* member_item: constructor_def  */
#line 513 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3207 "build/parser.tab.cpp"
    break;

  case 83: /* $@12: %empty  */
#line 522 "../phase2-parser/src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3213 "build/parser.tab.cpp"
    break;

  case 84: /* constructor_head: IDENTIFIER '(' $@12 parameter_list_opt ')'  */
#line 522 "../phase2-parser/src/parser.y"
                                                                                                      {
          setCategory(yyvsp[-4].idx, "CONSTRUCTOR");
          for (auto &p : yyvsp[-1].paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  pex.aggregateTagName = p.typeExpr ? p.typeExpr->tagName : ""; /* p->x */
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
          yyval = yyvsp[-4];
          yyval.paramList = yyvsp[-1].paramList;
          yyval.decl.isVariadic = yyvsp[-1].decl.isVariadic;
      }
#line 3233 "build/parser.tab.cpp"
    break;

  case 85: /* constructor_def: constructor_head compound_stmt  */
#line 540 "../phase2-parser/src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3242 "build/parser.tab.cpp"
    break;

  case 86: /* constructor_def: constructor_head ';'  */
#line 544 "../phase2-parser/src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3251 "build/parser.tab.cpp"
    break;

  case 87: /* $@13: %empty  */
#line 552 "../phase2-parser/src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3261 "build/parser.tab.cpp"
    break;

  case 88: /* $@14: %empty  */
#line 556 "../phase2-parser/src/parser.y"
                               {
          setCategory(yyvsp[-4].idx, "CONSTRUCTOR");
          for (auto &p : yyvsp[-1].paramList) {
              if (p.nameIdx >= 0) {
                  SymbolDeclInfo pex;
                  pex.tokenIdx = p.nameIdx;
                  pex.aggregateTagName = p.typeExpr ? p.typeExpr->tagName : ""; /* p->x */
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      }
#line 3278 "build/parser.tab.cpp"
    break;

  case 89: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@13 parameter_list_opt ')' $@14 compound_stmt  */
#line 567 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3288 "build/parser.tab.cpp"
    break;

  case 93: /* init_declarator_list_opt: %empty  */
#line 582 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3294 "build/parser.tab.cpp"
    break;

  case 94: /* init_declarator_list_opt: init_declarator_list  */
#line 583 "../phase2-parser/src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3300 "build/parser.tab.cpp"
    break;

  case 95: /* init_declarator_list: init_declarator  */
#line 587 "../phase2-parser/src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3306 "build/parser.tab.cpp"
    break;

  case 96: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 588 "../phase2-parser/src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3312 "build/parser.tab.cpp"
    break;

  case 97: /* init_declarator: declarator  */
#line 592 "../phase2-parser/src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3318 "build/parser.tab.cpp"
    break;

  case 98: /* init_declarator: declarator '=' initializer  */
#line 593 "../phase2-parser/src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3324 "build/parser.tab.cpp"
    break;

  case 99: /* initializer: assignment_expr  */
#line 597 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3330 "build/parser.tab.cpp"
    break;

  case 100: /* initializer: '{' '}'  */
#line 598 "../phase2-parser/src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3336 "build/parser.tab.cpp"
    break;

  case 101: /* initializer: '{' initializer_list '}'  */
#line 599 "../phase2-parser/src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3346 "build/parser.tab.cpp"
    break;

  case 102: /* initializer: '{' initializer_list ',' '}'  */
#line 604 "../phase2-parser/src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3356 "build/parser.tab.cpp"
    break;

  case 103: /* initializer_list: initializer_item  */
#line 612 "../phase2-parser/src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3362 "build/parser.tab.cpp"
    break;

  case 104: /* initializer_list: initializer_list ',' initializer_item  */
#line 613 "../phase2-parser/src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3368 "build/parser.tab.cpp"
    break;

  case 105: /* initializer_item: initializer  */
#line 617 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3374 "build/parser.tab.cpp"
    break;

  case 106: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 618 "../phase2-parser/src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3382 "build/parser.tab.cpp"
    break;

  case 107: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 621 "../phase2-parser/src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3390 "build/parser.tab.cpp"
    break;

  case 108: /* pointer: '*'  */
#line 627 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3396 "build/parser.tab.cpp"
    break;

  case 109: /* pointer: '&'  */
#line 628 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3402 "build/parser.tab.cpp"
    break;

  case 110: /* pointer: pointer '*'  */
#line 629 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3408 "build/parser.tab.cpp"
    break;

  case 111: /* pointer: pointer '&'  */
#line 630 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3414 "build/parser.tab.cpp"
    break;

  case 112: /* pointer: pointer CONST  */
#line 631 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3420 "build/parser.tab.cpp"
    break;

  case 113: /* declarator: pointer direct_declarator  */
#line 635 "../phase2-parser/src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3431 "build/parser.tab.cpp"
    break;

  case 114: /* declarator: direct_declarator  */
#line 641 "../phase2-parser/src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3437 "build/parser.tab.cpp"
    break;

  case 115: /* abstract_declarator: pointer  */
#line 647 "../phase2-parser/src/parser.y"
              { yyval = yyvsp[0]; }
#line 3443 "build/parser.tab.cpp"
    break;

  case 116: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 648 "../phase2-parser/src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3454 "build/parser.tab.cpp"
    break;

  case 117: /* abstract_declarator: direct_abstract_declarator  */
#line 654 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3460 "build/parser.tab.cpp"
    break;

  case 118: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 658 "../phase2-parser/src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3474 "build/parser.tab.cpp"
    break;

  case 119: /* direct_abstract_declarator: '[' ']'  */
#line 667 "../phase2-parser/src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3480 "build/parser.tab.cpp"
    break;

  case 120: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 668 "../phase2-parser/src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3486 "build/parser.tab.cpp"
    break;

  case 121: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 669 "../phase2-parser/src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3492 "build/parser.tab.cpp"
    break;

  case 122: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 670 "../phase2-parser/src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3498 "build/parser.tab.cpp"
    break;

  case 123: /* direct_declarator: IDENTIFIER  */
#line 674 "../phase2-parser/src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3507 "build/parser.tab.cpp"
    break;

  case 124: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 678 "../phase2-parser/src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3519 "build/parser.tab.cpp"
    break;

  case 125: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 685 "../phase2-parser/src/parser.y"
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
#line 3536 "build/parser.tab.cpp"
    break;

  case 126: /* direct_declarator: '(' declarator ')'  */
#line 697 "../phase2-parser/src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3550 "build/parser.tab.cpp"
    break;

  case 127: /* direct_declarator: operator_function_id  */
#line 706 "../phase2-parser/src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3559 "build/parser.tab.cpp"
    break;

  case 128: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 710 "../phase2-parser/src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3571 "build/parser.tab.cpp"
    break;

  case 129: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 717 "../phase2-parser/src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3583 "build/parser.tab.cpp"
    break;

  case 130: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 724 "../phase2-parser/src/parser.y"
                                                               {
          yyval = yyvsp[-4];
          if (yyvsp[-4].decl.wasParenGrouped && yyvsp[-4].decl.pointerLevel > 0) {
              /* `int (*fp)(int)` would declare a pointer to a function;
                 the language has no function pointers, so a parameter
                 list cannot follow a parenthesized pointer declarator */
              popScope();
              yyerror("syntax error, unexpected '(' after a parenthesized pointer declarator");
              YYERROR;
          }
          yyval.decl.isFunction = true;
          yyval.decl.wasParenGrouped = false; /* consumed */
          yyval.decl.params = yyvsp[-1].paramList;
          yyval.decl.isVariadic = yyvsp[-1].decl.isVariadic;
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
#line 3607 "build/parser.tab.cpp"
    break;

  case 131: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 743 "../phase2-parser/src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3619 "build/parser.tab.cpp"
    break;

  case 132: /* direct_declarator: direct_declarator '[' ']'  */
#line 750 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3625 "build/parser.tab.cpp"
    break;

  case 133: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 751 "../phase2-parser/src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3631 "build/parser.tab.cpp"
    break;

  case 134: /* operator_function_id: OPERATOR overloadable_operator  */
#line 756 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3637 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: '+'  */
#line 760 "../phase2-parser/src/parser.y"
          { yyval.str = "+"; }
#line 3643 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: '-'  */
#line 760 "../phase2-parser/src/parser.y"
                                  { yyval.str = "-"; }
#line 3649 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: '*'  */
#line 760 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "*"; }
#line 3655 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: '/'  */
#line 760 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3661 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: '%'  */
#line 761 "../phase2-parser/src/parser.y"
          { yyval.str = "%"; }
#line 3667 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: '^'  */
#line 761 "../phase2-parser/src/parser.y"
                                  { yyval.str = "^"; }
#line 3673 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: '&'  */
#line 761 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "&"; }
#line 3679 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: '|'  */
#line 761 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3685 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: '~'  */
#line 762 "../phase2-parser/src/parser.y"
          { yyval.str = "~"; }
#line 3691 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: '!'  */
#line 762 "../phase2-parser/src/parser.y"
                                  { yyval.str = "!"; }
#line 3697 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: '='  */
#line 762 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "="; }
#line 3703 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: '<'  */
#line 762 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3709 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: '>'  */
#line 763 "../phase2-parser/src/parser.y"
          { yyval.str = ">"; }
#line 3715 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: EQ_OP  */
#line 763 "../phase2-parser/src/parser.y"
                                    { yyval.str = "=="; }
#line 3721 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: NE_OP  */
#line 763 "../phase2-parser/src/parser.y"
                                                               { yyval.str = "!="; }
#line 3727 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: LE_OP  */
#line 763 "../phase2-parser/src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3733 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: GE_OP  */
#line 764 "../phase2-parser/src/parser.y"
            { yyval.str = ">="; }
#line 3739 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: AND_OP  */
#line 764 "../phase2-parser/src/parser.y"
                                        { yyval.str = "&&"; }
#line 3745 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: OR_OP  */
#line 764 "../phase2-parser/src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3751 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: SHL  */
#line 764 "../phase2-parser/src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3757 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: SHR  */
#line 765 "../phase2-parser/src/parser.y"
          { yyval.str = ">>"; }
#line 3763 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: INC  */
#line 765 "../phase2-parser/src/parser.y"
                                   { yyval.str = "++"; }
#line 3769 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: DEC  */
#line 765 "../phase2-parser/src/parser.y"
                                                            { yyval.str = "--"; }
#line 3775 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: PLUS_ASSIGN  */
#line 766 "../phase2-parser/src/parser.y"
                  { yyval.str = "+="; }
#line 3781 "build/parser.tab.cpp"
    break;

  case 159: /* overloadable_operator: MINUS_ASSIGN  */
#line 766 "../phase2-parser/src/parser.y"
                                                    { yyval.str = "-="; }
#line 3787 "build/parser.tab.cpp"
    break;

  case 160: /* overloadable_operator: MUL_ASSIGN  */
#line 766 "../phase2-parser/src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3793 "build/parser.tab.cpp"
    break;

  case 161: /* overloadable_operator: DIV_ASSIGN  */
#line 767 "../phase2-parser/src/parser.y"
                 { yyval.str = "/="; }
#line 3799 "build/parser.tab.cpp"
    break;

  case 162: /* overloadable_operator: MOD_ASSIGN  */
#line 767 "../phase2-parser/src/parser.y"
                                                 { yyval.str = "%="; }
#line 3805 "build/parser.tab.cpp"
    break;

  case 163: /* overloadable_operator: AND_ASSIGN  */
#line 767 "../phase2-parser/src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3811 "build/parser.tab.cpp"
    break;

  case 164: /* overloadable_operator: OR_ASSIGN  */
#line 768 "../phase2-parser/src/parser.y"
                { yyval.str = "|="; }
#line 3817 "build/parser.tab.cpp"
    break;

  case 165: /* overloadable_operator: XOR_ASSIGN  */
#line 768 "../phase2-parser/src/parser.y"
                                                { yyval.str = "^="; }
#line 3823 "build/parser.tab.cpp"
    break;

  case 166: /* overloadable_operator: SHL_ASSIGN  */
#line 768 "../phase2-parser/src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3829 "build/parser.tab.cpp"
    break;

  case 167: /* overloadable_operator: SHR_ASSIGN  */
#line 769 "../phase2-parser/src/parser.y"
                 { yyval.str = ">>="; }
#line 3835 "build/parser.tab.cpp"
    break;

  case 168: /* overloadable_operator: '[' ']'  */
#line 769 "../phase2-parser/src/parser.y"
                                               { yyval.str = "[]"; }
#line 3841 "build/parser.tab.cpp"
    break;

  case 169: /* overloadable_operator: '(' ')'  */
#line 769 "../phase2-parser/src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3847 "build/parser.tab.cpp"
    break;

  case 170: /* param_scope: %empty  */
#line 776 "../phase2-parser/src/parser.y"
                                           { pushScope(); }
#line 3853 "build/parser.tab.cpp"
    break;

  case 171: /* constructor_args: assignment_expr  */
#line 780 "../phase2-parser/src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3859 "build/parser.tab.cpp"
    break;

  case 172: /* constructor_args: constructor_args ',' assignment_expr  */
#line 781 "../phase2-parser/src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3865 "build/parser.tab.cpp"
    break;

  case 173: /* parameter_list_opt: %empty  */
#line 785 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3871 "build/parser.tab.cpp"
    break;

  case 174: /* parameter_list_opt: parameter_list  */
#line 786 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3877 "build/parser.tab.cpp"
    break;

  case 175: /* parameter_list: parameter_decl  */
#line 790 "../phase2-parser/src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3886 "build/parser.tab.cpp"
    break;

  case 176: /* parameter_list: parameter_list ',' parameter_decl  */
#line 794 "../phase2-parser/src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3895 "build/parser.tab.cpp"
    break;

  case 177: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 798 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3901 "build/parser.tab.cpp"
    break;

  case 178: /* parameter_decl: declaration_specifiers declarator  */
#line 802 "../phase2-parser/src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3911 "build/parser.tab.cpp"
    break;

  case 179: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 807 "../phase2-parser/src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3921 "build/parser.tab.cpp"
    break;

  case 180: /* parameter_decl: declaration_specifiers  */
#line 812 "../phase2-parser/src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3931 "build/parser.tab.cpp"
    break;

  case 181: /* $@15: %empty  */
#line 820 "../phase2-parser/src/parser.y"
                                        {
          bool outOfClass = !yyvsp[0].decl.className.empty();
          if (outOfClass) enterClass(yyvsp[0].decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[0].decl.params) paramTypes.push_back(p.typeStr);
          std::string owner = yyvsp[-1].typeSpec.isFriend ? "" : currentClassName(); /* a friend is not a member */
          std::string mangled = mangle(yyvsp[0].decl.name, paramExprs(yyvsp[0].decl.params), yyvsp[0].decl.isVariadic, owner);
          std::string returnType = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          SymbolDeclInfo extra;
          extra.tokenIdx = yyvsp[0].decl.nameIdx;
          extra.isStatic = yyvsp[-1].typeSpec.isStatic;
          extra.isConst = yyvsp[-1].typeSpec.isConst;
          extra.pointerLevel = yyvsp[0].decl.pointerLevel;
          extra.arrayLevel = yyvsp[0].decl.arrayLevel;
          extra.returnType = returnType;
          extra.paramTypes = paramTypes;
          extra.mangledName = mangled;
          extra.aggregateTagName = yyvsp[-1].typeSpec.tagName; /* f().x */
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
                  pex.aggregateTagName = p.typeExpr ? p.typeExpr->tagName : ""; /* p->x */
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, pex);
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      }
#line 3973 "build/parser.tab.cpp"
    break;

  case 182: /* function_definition: declaration_specifiers declarator $@15 '{' block_item_list_opt '}'  */
#line 856 "../phase2-parser/src/parser.y"
                                    {
          popScope();
          bool outOfClass = !yyvsp[-4].decl.className.empty();
          /* currentClassName() is still correctly set here for the
             out-of-class case -- it was never left, see above -- so
             no need to re-enter it just to compute the mangled name
             again. */
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[-4].decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[-4].decl.name, paramExprs(yyvsp[-4].decl.params), yyvsp[-4].decl.isVariadic,
                                       yyvsp[-5].typeSpec.isFriend ? "" : currentClassName());
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
#line 4004 "build/parser.tab.cpp"
    break;

  case 183: /* statement: compound_stmt  */
#line 885 "../phase2-parser/src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 4010 "build/parser.tab.cpp"
    break;

  case 184: /* statement: expr_stmt  */
#line 886 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 4016 "build/parser.tab.cpp"
    break;

  case 185: /* statement: selection_stmt  */
#line 887 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4022 "build/parser.tab.cpp"
    break;

  case 186: /* statement: iteration_stmt  */
#line 888 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4028 "build/parser.tab.cpp"
    break;

  case 187: /* statement: jump_stmt  */
#line 889 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 4034 "build/parser.tab.cpp"
    break;

  case 188: /* statement: labeled_stmt  */
#line 890 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4040 "build/parser.tab.cpp"
    break;

  case 189: /* statement: declaration  */
#line 891 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4046 "build/parser.tab.cpp"
    break;

  case 190: /* statement: error ';'  */
#line 892 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4052 "build/parser.tab.cpp"
    break;

  case 191: /* statement: error '}'  */
#line 893 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4058 "build/parser.tab.cpp"
    break;

  case 192: /* $@16: %empty  */
#line 897 "../phase2-parser/src/parser.y"
          { pushScope(); }
#line 4064 "build/parser.tab.cpp"
    break;

  case 193: /* compound_stmt: '{' $@16 block_item_list_opt '}'  */
#line 897 "../phase2-parser/src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 4075 "build/parser.tab.cpp"
    break;

  case 194: /* block_item_list_opt: %empty  */
#line 906 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4081 "build/parser.tab.cpp"
    break;

  case 195: /* block_item_list_opt: block_item_list  */
#line 907 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[0]; }
#line 4087 "build/parser.tab.cpp"
    break;

  case 196: /* block_item_list: statement  */
#line 911 "../phase2-parser/src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4093 "build/parser.tab.cpp"
    break;

  case 197: /* block_item_list: block_item_list statement  */
#line 912 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4099 "build/parser.tab.cpp"
    break;

  case 198: /* expr_stmt: ';'  */
#line 916 "../phase2-parser/src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 4105 "build/parser.tab.cpp"
    break;

  case 199: /* expr_stmt: expr ';'  */
#line 917 "../phase2-parser/src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 4111 "build/parser.tab.cpp"
    break;

  case 200: /* selection_stmt: IF '(' expr ')' statement  */
#line 921 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4119 "build/parser.tab.cpp"
    break;

  case 201: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 924 "../phase2-parser/src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 4127 "build/parser.tab.cpp"
    break;

  case 202: /* $@17: %empty  */
#line 927 "../phase2-parser/src/parser.y"
                          { hintScope("switch"); }
#line 4133 "build/parser.tab.cpp"
    break;

  case 203: /* selection_stmt: SWITCH '(' expr ')' $@17 compound_stmt  */
#line 927 "../phase2-parser/src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4141 "build/parser.tab.cpp"
    break;

  case 204: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 933 "../phase2-parser/src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4149 "build/parser.tab.cpp"
    break;

  case 205: /* labeled_stmt: DEFAULT ':' statement  */
#line 936 "../phase2-parser/src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4157 "build/parser.tab.cpp"
    break;

  case 206: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 939 "../phase2-parser/src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4167 "build/parser.tab.cpp"
    break;

  case 207: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 947 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4175 "build/parser.tab.cpp"
    break;

  case 208: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 950 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4183 "build/parser.tab.cpp"
    break;

  case 209: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 957 "../phase2-parser/src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4192 "build/parser.tab.cpp"
    break;

  case 210: /* iteration_stmt: DO statement error ';'  */
#line 961 "../phase2-parser/src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4201 "build/parser.tab.cpp"
    break;

  case 211: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 965 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4209 "build/parser.tab.cpp"
    break;

  case 212: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 968 "../phase2-parser/src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4218 "build/parser.tab.cpp"
    break;

  case 213: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 972 "../phase2-parser/src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4227 "build/parser.tab.cpp"
    break;

  case 214: /* for_open: FOR '('  */
#line 981 "../phase2-parser/src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4233 "build/parser.tab.cpp"
    break;

  case 215: /* for_incr_opt: %empty  */
#line 985 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4239 "build/parser.tab.cpp"
    break;

  case 216: /* for_incr_opt: expr  */
#line 986 "../phase2-parser/src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4245 "build/parser.tab.cpp"
    break;

  case 217: /* jump_stmt: BREAK ';'  */
#line 990 "../phase2-parser/src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4251 "build/parser.tab.cpp"
    break;

  case 218: /* jump_stmt: CONTINUE ';'  */
#line 991 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4257 "build/parser.tab.cpp"
    break;

  case 219: /* jump_stmt: RETURN ';'  */
#line 992 "../phase2-parser/src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4263 "build/parser.tab.cpp"
    break;

  case 220: /* jump_stmt: RETURN expr ';'  */
#line 993 "../phase2-parser/src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4269 "build/parser.tab.cpp"
    break;

  case 221: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 994 "../phase2-parser/src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4281 "build/parser.tab.cpp"
    break;

  case 222: /* expr: assignment_expr  */
#line 1004 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4287 "build/parser.tab.cpp"
    break;

  case 223: /* expr: expr ',' assignment_expr  */
#line 1005 "../phase2-parser/src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4293 "build/parser.tab.cpp"
    break;

  case 224: /* assignment_expr: binary_expr  */
#line 1009 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4299 "build/parser.tab.cpp"
    break;

  case 225: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 1010 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4307 "build/parser.tab.cpp"
    break;

  case 226: /* assign_op: '='  */
#line 1016 "../phase2-parser/src/parser.y"
                   { yyval.str = "="; }
#line 4313 "build/parser.tab.cpp"
    break;

  case 227: /* assign_op: PLUS_ASSIGN  */
#line 1017 "../phase2-parser/src/parser.y"
                   { yyval.str = "+="; }
#line 4319 "build/parser.tab.cpp"
    break;

  case 228: /* assign_op: MINUS_ASSIGN  */
#line 1018 "../phase2-parser/src/parser.y"
                   { yyval.str = "-="; }
#line 4325 "build/parser.tab.cpp"
    break;

  case 229: /* assign_op: MUL_ASSIGN  */
#line 1019 "../phase2-parser/src/parser.y"
                   { yyval.str = "*="; }
#line 4331 "build/parser.tab.cpp"
    break;

  case 230: /* assign_op: DIV_ASSIGN  */
#line 1020 "../phase2-parser/src/parser.y"
                   { yyval.str = "/="; }
#line 4337 "build/parser.tab.cpp"
    break;

  case 231: /* assign_op: MOD_ASSIGN  */
#line 1021 "../phase2-parser/src/parser.y"
                   { yyval.str = "%="; }
#line 4343 "build/parser.tab.cpp"
    break;

  case 232: /* assign_op: AND_ASSIGN  */
#line 1022 "../phase2-parser/src/parser.y"
                   { yyval.str = "&="; }
#line 4349 "build/parser.tab.cpp"
    break;

  case 233: /* assign_op: OR_ASSIGN  */
#line 1023 "../phase2-parser/src/parser.y"
                   { yyval.str = "|="; }
#line 4355 "build/parser.tab.cpp"
    break;

  case 234: /* assign_op: XOR_ASSIGN  */
#line 1024 "../phase2-parser/src/parser.y"
                   { yyval.str = "^="; }
#line 4361 "build/parser.tab.cpp"
    break;

  case 235: /* assign_op: SHL_ASSIGN  */
#line 1025 "../phase2-parser/src/parser.y"
                   { yyval.str = "<<="; }
#line 4367 "build/parser.tab.cpp"
    break;

  case 236: /* assign_op: SHR_ASSIGN  */
#line 1026 "../phase2-parser/src/parser.y"
                   { yyval.str = ">>="; }
#line 4373 "build/parser.tab.cpp"
    break;

  case 237: /* constant_expr: binary_expr  */
#line 1030 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4379 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 1034 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4385 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 1035 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4391 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr '|' binary_expr  */
#line 1036 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4397 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr '^' binary_expr  */
#line 1037 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4403 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr '&' binary_expr  */
#line 1038 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4409 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 1039 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4415 "build/parser.tab.cpp"
    break;

  case 244: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 1040 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4421 "build/parser.tab.cpp"
    break;

  case 245: /* binary_expr: binary_expr '<' binary_expr  */
#line 1041 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4427 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: binary_expr '>' binary_expr  */
#line 1042 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4433 "build/parser.tab.cpp"
    break;

  case 247: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 1043 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4439 "build/parser.tab.cpp"
    break;

  case 248: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 1044 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4445 "build/parser.tab.cpp"
    break;

  case 249: /* binary_expr: binary_expr SHL binary_expr  */
#line 1045 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4451 "build/parser.tab.cpp"
    break;

  case 250: /* binary_expr: binary_expr SHR binary_expr  */
#line 1046 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4457 "build/parser.tab.cpp"
    break;

  case 251: /* binary_expr: binary_expr '+' binary_expr  */
#line 1047 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4463 "build/parser.tab.cpp"
    break;

  case 252: /* binary_expr: binary_expr '-' binary_expr  */
#line 1048 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4469 "build/parser.tab.cpp"
    break;

  case 253: /* binary_expr: binary_expr '*' binary_expr  */
#line 1049 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4475 "build/parser.tab.cpp"
    break;

  case 254: /* binary_expr: binary_expr '/' binary_expr  */
#line 1050 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4481 "build/parser.tab.cpp"
    break;

  case 255: /* binary_expr: binary_expr '%' binary_expr  */
#line 1051 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4487 "build/parser.tab.cpp"
    break;

  case 256: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 1052 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4495 "build/parser.tab.cpp"
    break;

  case 257: /* binary_expr: unary_expr  */
#line 1055 "../phase2-parser/src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4501 "build/parser.tab.cpp"
    break;

  case 258: /* unary_expr: postfix_expr  */
#line 1059 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4507 "build/parser.tab.cpp"
    break;

  case 259: /* unary_expr: INC unary_expr  */
#line 1060 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4513 "build/parser.tab.cpp"
    break;

  case 260: /* unary_expr: DEC unary_expr  */
#line 1061 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4519 "build/parser.tab.cpp"
    break;

  case 261: /* unary_expr: '&' unary_expr  */
#line 1062 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4525 "build/parser.tab.cpp"
    break;

  case 262: /* unary_expr: '*' unary_expr  */
#line 1063 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4531 "build/parser.tab.cpp"
    break;

  case 263: /* unary_expr: '+' unary_expr  */
#line 1064 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4537 "build/parser.tab.cpp"
    break;

  case 264: /* unary_expr: '-' unary_expr  */
#line 1065 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4543 "build/parser.tab.cpp"
    break;

  case 265: /* unary_expr: '!' unary_expr  */
#line 1066 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4549 "build/parser.tab.cpp"
    break;

  case 266: /* unary_expr: '~' unary_expr  */
#line 1067 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4555 "build/parser.tab.cpp"
    break;

  case 267: /* unary_expr: '(' type_name ')' unary_expr  */
#line 1068 "../phase2-parser/src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4564 "build/parser.tab.cpp"
    break;

  case 268: /* unary_expr: SIZEOF unary_expr  */
#line 1072 "../phase2-parser/src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4570 "build/parser.tab.cpp"
    break;

  case 269: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 1073 "../phase2-parser/src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4579 "build/parser.tab.cpp"
    break;

  case 270: /* type_name: type_name_specifiers  */
#line 1080 "../phase2-parser/src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4588 "build/parser.tab.cpp"
    break;

  case 271: /* type_name: type_name_specifiers abstract_declarator  */
#line 1084 "../phase2-parser/src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4597 "build/parser.tab.cpp"
    break;

  case 272: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1091 "../phase2-parser/src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4609 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifiers: type_name_specifier  */
#line 1098 "../phase2-parser/src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4615 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifier: INT  */
#line 1102 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4621 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: CHAR  */
#line 1103 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4627 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: FLOAT  */
#line 1104 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4633 "build/parser.tab.cpp"
    break;

  case 277: /* type_name_specifier: DOUBLE  */
#line 1105 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4639 "build/parser.tab.cpp"
    break;

  case 278: /* type_name_specifier: VOID  */
#line 1106 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4645 "build/parser.tab.cpp"
    break;

  case 279: /* type_name_specifier: BOOL  */
#line 1107 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4651 "build/parser.tab.cpp"
    break;

  case 280: /* type_name_specifier: SHORT  */
#line 1108 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4657 "build/parser.tab.cpp"
    break;

  case 281: /* type_name_specifier: LONG  */
#line 1109 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4663 "build/parser.tab.cpp"
    break;

  case 282: /* type_name_specifier: SIGNED  */
#line 1110 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4669 "build/parser.tab.cpp"
    break;

  case 283: /* type_name_specifier: UNSIGNED  */
#line 1111 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4675 "build/parser.tab.cpp"
    break;

  case 284: /* type_name_specifier: VA_LIST  */
#line 1112 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4681 "build/parser.tab.cpp"
    break;

  case 285: /* type_name_specifier: CONST  */
#line 1113 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4687 "build/parser.tab.cpp"
    break;

  case 286: /* type_name_specifier: TYPE_NAME  */
#line 1114 "../phase2-parser/src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4701 "build/parser.tab.cpp"
    break;

  case 287: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1123 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4712 "build/parser.tab.cpp"
    break;

  case 288: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1129 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4723 "build/parser.tab.cpp"
    break;

  case 289: /* type_name_specifier: UNION IDENTIFIER  */
#line 1135 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4734 "build/parser.tab.cpp"
    break;

  case 290: /* type_name_specifier: UNION TYPE_NAME  */
#line 1141 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4745 "build/parser.tab.cpp"
    break;

  case 291: /* type_name_specifier: ENUM IDENTIFIER  */
#line 1147 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4756 "build/parser.tab.cpp"
    break;

  case 292: /* type_name_specifier: ENUM TYPE_NAME  */
#line 1153 "../phase2-parser/src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4767 "build/parser.tab.cpp"
    break;

  case 293: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1159 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4778 "build/parser.tab.cpp"
    break;

  case 294: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1165 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4789 "build/parser.tab.cpp"
    break;

  case 295: /* postfix_expr: primary_expr  */
#line 1174 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4795 "build/parser.tab.cpp"
    break;

  case 296: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1175 "../phase2-parser/src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4801 "build/parser.tab.cpp"
    break;

  case 297: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1176 "../phase2-parser/src/parser.y"
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
#line 4841 "build/parser.tab.cpp"
    break;

  case 298: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1211 "../phase2-parser/src/parser.y"
                                  {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4850 "build/parser.tab.cpp"
    break;

  case 299: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1215 "../phase2-parser/src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4863 "build/parser.tab.cpp"
    break;

  case 300: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1223 "../phase2-parser/src/parser.y"
                                                        {
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4874 "build/parser.tab.cpp"
    break;

  case 301: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1229 "../phase2-parser/src/parser.y"
                                    {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4883 "build/parser.tab.cpp"
    break;

  case 302: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1233 "../phase2-parser/src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4889 "build/parser.tab.cpp"
    break;

  case 303: /* postfix_expr: postfix_expr INC  */
#line 1234 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4895 "build/parser.tab.cpp"
    break;

  case 304: /* postfix_expr: postfix_expr DEC  */
#line 1235 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4901 "build/parser.tab.cpp"
    break;

  case 305: /* postfix_expr: builtin_call  */
#line 1236 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4907 "build/parser.tab.cpp"
    break;

  case 306: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1240 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4913 "build/parser.tab.cpp"
    break;

  case 307: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1241 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4919 "build/parser.tab.cpp"
    break;

  case 308: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1242 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4925 "build/parser.tab.cpp"
    break;

  case 309: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1243 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4931 "build/parser.tab.cpp"
    break;

  case 310: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1244 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4937 "build/parser.tab.cpp"
    break;

  case 311: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1245 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4943 "build/parser.tab.cpp"
    break;

  case 312: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1246 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4949 "build/parser.tab.cpp"
    break;

  case 313: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1247 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4955 "build/parser.tab.cpp"
    break;

  case 314: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1248 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4961 "build/parser.tab.cpp"
    break;

  case 315: /* constructor_args_opt: %empty  */
#line 1252 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4967 "build/parser.tab.cpp"
    break;

  case 316: /* constructor_args_opt: constructor_args  */
#line 1253 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4973 "build/parser.tab.cpp"
    break;

  case 317: /* argument_list_opt: %empty  */
#line 1257 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4979 "build/parser.tab.cpp"
    break;

  case 318: /* argument_list_opt: argument_list  */
#line 1258 "../phase2-parser/src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4985 "build/parser.tab.cpp"
    break;

  case 319: /* argument_list: argument  */
#line 1262 "../phase2-parser/src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4991 "build/parser.tab.cpp"
    break;

  case 320: /* argument_list: argument_list ',' argument  */
#line 1263 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4997 "build/parser.tab.cpp"
    break;

  case 321: /* argument: assignment_expr  */
#line 1267 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 5003 "build/parser.tab.cpp"
    break;

  case 322: /* argument: type_name  */
#line 1268 "../phase2-parser/src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 5012 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: IDENTIFIER  */
#line 1275 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 5026 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: INT_LITERAL  */
#line 1284 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5032 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: FLOAT_LITERAL  */
#line 1285 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5038 "build/parser.tab.cpp"
    break;

  case 326: /* primary_expr: CHAR_LITERAL  */
#line 1286 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5044 "build/parser.tab.cpp"
    break;

  case 327: /* primary_expr: string_literal  */
#line 1287 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 5050 "build/parser.tab.cpp"
    break;

  case 328: /* primary_expr: BOOL_LITERAL  */
#line 1288 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5056 "build/parser.tab.cpp"
    break;

  case 329: /* primary_expr: THIS  */
#line 1289 "../phase2-parser/src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 5062 "build/parser.tab.cpp"
    break;

  case 330: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1290 "../phase2-parser/src/parser.y"
                                             {
          /* `Dog()`: a temporary object (for a scalar type, `int(x)`, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5071 "build/parser.tab.cpp"
    break;

  case 331: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1294 "../phase2-parser/src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5081 "build/parser.tab.cpp"
    break;

  case 332: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1301 "../phase2-parser/src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5087 "build/parser.tab.cpp"
    break;

  case 333: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1302 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5093 "build/parser.tab.cpp"
    break;

  case 334: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1303 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5099 "build/parser.tab.cpp"
    break;

  case 335: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1304 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5105 "build/parser.tab.cpp"
    break;

  case 336: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1305 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5111 "build/parser.tab.cpp"
    break;

  case 337: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1306 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5117 "build/parser.tab.cpp"
    break;

  case 338: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1307 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5123 "build/parser.tab.cpp"
    break;

  case 339: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1308 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5129 "build/parser.tab.cpp"
    break;

  case 340: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1309 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5135 "build/parser.tab.cpp"
    break;

  case 341: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1310 "../phase2-parser/src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5141 "build/parser.tab.cpp"
    break;

  case 342: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1311 "../phase2-parser/src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 5153 "build/parser.tab.cpp"
    break;

  case 343: /* primary_expr: '(' expr ')'  */
#line 1318 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 5159 "build/parser.tab.cpp"
    break;

  case 344: /* string_literal: STRING_LITERAL  */
#line 1323 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5165 "build/parser.tab.cpp"
    break;

  case 345: /* string_literal: string_literal STRING_LITERAL  */
#line 1324 "../phase2-parser/src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 5175 "build/parser.tab.cpp"
    break;


#line 5179 "build/parser.tab.cpp"

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

#line 1331 "../phase2-parser/src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
