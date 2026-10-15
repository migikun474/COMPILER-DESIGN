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
  YYSYMBOL_PUBLIC = 14,                    /* PUBLIC  */
  YYSYMBOL_PRIVATE = 15,                   /* PRIVATE  */
  YYSYMBOL_PROTECTED = 16,                 /* PROTECTED  */
  YYSYMBOL_THIS = 17,                      /* THIS  */
  YYSYMBOL_STATIC = 18,                    /* STATIC  */
  YYSYMBOL_TYPEDEF = 19,                   /* TYPEDEF  */
  YYSYMBOL_AUTO = 20,                      /* AUTO  */
  YYSYMBOL_EXTERN = 21,                    /* EXTERN  */
  YYSYMBOL_CONST = 22,                     /* CONST  */
  YYSYMBOL_VIRTUAL = 23,                   /* VIRTUAL  */
  YYSYMBOL_EXPLICIT = 24,                  /* EXPLICIT  */
  YYSYMBOL_FRIEND = 25,                    /* FRIEND  */
  YYSYMBOL_IF = 26,                        /* IF  */
  YYSYMBOL_ELSE = 27,                      /* ELSE  */
  YYSYMBOL_FOR = 28,                       /* FOR  */
  YYSYMBOL_WHILE = 29,                     /* WHILE  */
  YYSYMBOL_DO = 30,                        /* DO  */
  YYSYMBOL_UNTIL = 31,                     /* UNTIL  */
  YYSYMBOL_SWITCH = 32,                    /* SWITCH  */
  YYSYMBOL_CASE = 33,                      /* CASE  */
  YYSYMBOL_DEFAULT = 34,                   /* DEFAULT  */
  YYSYMBOL_BREAK = 35,                     /* BREAK  */
  YYSYMBOL_CONTINUE = 36,                  /* CONTINUE  */
  YYSYMBOL_GOTO = 37,                      /* GOTO  */
  YYSYMBOL_RETURN = 38,                    /* RETURN  */
  YYSYMBOL_PRINTF = 39,                    /* PRINTF  */
  YYSYMBOL_SCANF = 40,                     /* SCANF  */
  YYSYMBOL_MALLOC = 41,                    /* MALLOC  */
  YYSYMBOL_FREE = 42,                      /* FREE  */
  YYSYMBOL_CALLOC = 43,                    /* CALLOC  */
  YYSYMBOL_REALLOC = 44,                   /* REALLOC  */
  YYSYMBOL_BOOL = 45,                      /* BOOL  */
  YYSYMBOL_SIZEOF = 46,                    /* SIZEOF  */
  YYSYMBOL_VA_LIST = 47,                   /* VA_LIST  */
  YYSYMBOL_VA_START = 48,                  /* VA_START  */
  YYSYMBOL_VA_ARG = 49,                    /* VA_ARG  */
  YYSYMBOL_VA_END = 50,                    /* VA_END  */
  YYSYMBOL_OPERATOR = 51,                  /* OPERATOR  */
  YYSYMBOL_FCAST = 52,                     /* FCAST  */
  YYSYMBOL_ABSTRACT_LPAREN = 53,           /* ABSTRACT_LPAREN  */
  YYSYMBOL_IDENTIFIER = 54,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 55,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 56,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 57,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 58,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 59,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 60,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 61,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 62,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 63,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 64,                       /* INC  */
  YYSYMBOL_DEC = 65,                       /* DEC  */
  YYSYMBOL_SHL = 66,                       /* SHL  */
  YYSYMBOL_SHR = 67,                       /* SHR  */
  YYSYMBOL_LE_OP = 68,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 69,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 70,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 71,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 72,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 73,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 74,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 75,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 76,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 77,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 78,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 79,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 80,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 81,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 82,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 83,                /* SHR_ASSIGN  */
  YYSYMBOL_PREFER_EXPRESSION = 84,         /* PREFER_EXPRESSION  */
  YYSYMBOL_85_ = 85,                       /* '='  */
  YYSYMBOL_86_ = 86,                       /* '?'  */
  YYSYMBOL_87_ = 87,                       /* ':'  */
  YYSYMBOL_88_ = 88,                       /* '|'  */
  YYSYMBOL_89_ = 89,                       /* '^'  */
  YYSYMBOL_90_ = 90,                       /* '&'  */
  YYSYMBOL_91_ = 91,                       /* '<'  */
  YYSYMBOL_92_ = 92,                       /* '>'  */
  YYSYMBOL_93_ = 93,                       /* '+'  */
  YYSYMBOL_94_ = 94,                       /* '-'  */
  YYSYMBOL_95_ = 95,                       /* '*'  */
  YYSYMBOL_96_ = 96,                       /* '/'  */
  YYSYMBOL_97_ = 97,                       /* '%'  */
  YYSYMBOL_UMINUS = 98,                    /* UMINUS  */
  YYSYMBOL_ADDR = 99,                      /* ADDR  */
  YYSYMBOL_DEREF = 100,                    /* DEREF  */
  YYSYMBOL_CAST = 101,                     /* CAST  */
  YYSYMBOL_102_ = 102,                     /* '!'  */
  YYSYMBOL_103_ = 103,                     /* '~'  */
  YYSYMBOL_104_ = 104,                     /* '.'  */
  YYSYMBOL_105_ = 105,                     /* '('  */
  YYSYMBOL_106_ = 106,                     /* '['  */
  YYSYMBOL_SIZEOF_TYPE = 107,              /* SIZEOF_TYPE  */
  YYSYMBOL_PREFER_DECLARATION = 108,       /* PREFER_DECLARATION  */
  YYSYMBOL_IFX = 109,                      /* IFX  */
  YYSYMBOL_110_ = 110,                     /* ';'  */
  YYSYMBOL_111_ = 111,                     /* '}'  */
  YYSYMBOL_112_ = 112,                     /* '{'  */
  YYSYMBOL_113_ = 113,                     /* ','  */
  YYSYMBOL_114_ = 114,                     /* ')'  */
  YYSYMBOL_115_ = 115,                     /* ']'  */
  YYSYMBOL_YYACCEPT = 116,                 /* $accept  */
  YYSYMBOL_translation_unit = 117,         /* translation_unit  */
  YYSYMBOL_external_decl = 118,            /* external_decl  */
  YYSYMBOL_declaration = 119,              /* declaration  */
  YYSYMBOL_declaration_specifiers = 120,   /* declaration_specifiers  */
  YYSYMBOL_storage_or_type_specifier = 121, /* storage_or_type_specifier  */
  YYSYMBOL_type_specifier = 122,           /* type_specifier  */
  YYSYMBOL_tag_name = 123,                 /* tag_name  */
  YYSYMBOL_struct_or_class_specifier = 124, /* struct_or_class_specifier  */
  YYSYMBOL_125_1 = 125,                    /* $@1  */
  YYSYMBOL_126_2 = 126,                    /* $@2  */
  YYSYMBOL_127_3 = 127,                    /* @3  */
  YYSYMBOL_128_4 = 128,                    /* $@4  */
  YYSYMBOL_129_5 = 129,                    /* $@5  */
  YYSYMBOL_130_6 = 130,                    /* @6  */
  YYSYMBOL_member_decl_list_opt = 131,     /* member_decl_list_opt  */
  YYSYMBOL_inheritance_opt = 132,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 133, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 134,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 135,         /* member_decl_list  */
  YYSYMBOL_member_item = 136,              /* member_item  */
  YYSYMBOL_constructor_head = 137,         /* constructor_head  */
  YYSYMBOL_138_7 = 138,                    /* $@7  */
  YYSYMBOL_constructor_def = 139,          /* constructor_def  */
  YYSYMBOL_destructor_head = 140,          /* destructor_head  */
  YYSYMBOL_destructor_def = 141,           /* destructor_def  */
  YYSYMBOL_out_of_class_special = 142,     /* out_of_class_special  */
  YYSYMBOL_143_8 = 143,                    /* $@8  */
  YYSYMBOL_144_9 = 144,                    /* $@9  */
  YYSYMBOL_145_10 = 145,                   /* $@10  */
  YYSYMBOL_mem_init_opt = 146,             /* mem_init_opt  */
  YYSYMBOL_mem_initializer_list = 147,     /* mem_initializer_list  */
  YYSYMBOL_mem_initializer = 148,          /* mem_initializer  */
  YYSYMBOL_access_specifier = 149,         /* access_specifier  */
  YYSYMBOL_init_declarator_list_opt = 150, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 151,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 152,          /* init_declarator  */
  YYSYMBOL_initializer = 153,              /* initializer  */
  YYSYMBOL_initializer_list = 154,         /* initializer_list  */
  YYSYMBOL_initializer_item = 155,         /* initializer_item  */
  YYSYMBOL_pointer = 156,                  /* pointer  */
  YYSYMBOL_declarator = 157,               /* declarator  */
  YYSYMBOL_abstract_declarator = 158,      /* abstract_declarator  */
  YYSYMBOL_direct_abstract_declarator = 159, /* direct_abstract_declarator  */
  YYSYMBOL_direct_declarator = 160,        /* direct_declarator  */
  YYSYMBOL_method_cv_opt = 161,            /* method_cv_opt  */
  YYSYMBOL_operator_function_id = 162,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 163,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 164,              /* param_scope  */
  YYSYMBOL_constructor_args = 165,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 166,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 167,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 168,           /* parameter_decl  */
  YYSYMBOL_function_definition = 169,      /* function_definition  */
  YYSYMBOL_170_11 = 170,                   /* $@11  */
  YYSYMBOL_statement = 171,                /* statement  */
  YYSYMBOL_compound_stmt = 172,            /* compound_stmt  */
  YYSYMBOL_173_12 = 173,                   /* $@12  */
  YYSYMBOL_block_item_list_opt = 174,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 175,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 176,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 177,           /* selection_stmt  */
  YYSYMBOL_178_13 = 178,                   /* $@13  */
  YYSYMBOL_labeled_stmt = 179,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 180,           /* iteration_stmt  */
  YYSYMBOL_for_open = 181,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 182,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 183,                /* jump_stmt  */
  YYSYMBOL_expr = 184,                     /* expr  */
  YYSYMBOL_assignment_expr = 185,          /* assignment_expr  */
  YYSYMBOL_assign_op = 186,                /* assign_op  */
  YYSYMBOL_constant_expr = 187,            /* constant_expr  */
  YYSYMBOL_binary_expr = 188,              /* binary_expr  */
  YYSYMBOL_unary_expr = 189,               /* unary_expr  */
  YYSYMBOL_type_name = 190,                /* type_name  */
  YYSYMBOL_type_name_specifiers = 191,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 192,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 193,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 194,             /* builtin_call  */
  YYSYMBOL_constructor_args_opt = 195,     /* constructor_args_opt  */
  YYSYMBOL_argument_list_opt = 196,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 197,            /* argument_list  */
  YYSYMBOL_argument = 198,                 /* argument  */
  YYSYMBOL_primary_expr = 199,             /* primary_expr  */
  YYSYMBOL_string_literal = 200            /* string_literal  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;



/* Unqualified %code blocks.  */
#line 13 "src/parser.y"

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

#line 365 "build/parser.tab.cpp"

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
#define YYLAST   2197

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  116
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  85
/* YYNRULES -- Number of rules.  */
#define YYNRULES  340
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  613

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   346


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
       2,     2,     2,   102,     2,     2,     2,    97,    90,     2,
     105,   114,    95,    93,   113,    94,   104,    96,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    87,   110,
      91,    85,    92,    86,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   106,     2,   115,    89,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   112,    88,   111,   103,     2,     2,     2,
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
      98,    99,   100,   101,   107,   108,   109
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   139,   139,   143,   151,   152,   153,   154,   155,   159,
     190,   205,   209,   210,   211,   212,   213,   214,   215,   216,
     220,   221,   222,   223,   224,   225,   226,   227,   228,   229,
     230,   231,   245,   252,   253,   257,   261,   257,   277,   277,
     291,   297,   303,   307,   303,   319,   319,   333,   339,   348,
     349,   353,   354,   358,   359,   366,   372,   378,   384,   395,
     400,   412,   413,   414,   415,   416,   420,   421,   431,   431,
     449,   454,   461,   469,   473,   481,   485,   481,   501,   501,
     517,   518,   522,   523,   527,   531,   535,   542,   543,   544,
     548,   549,   553,   554,   558,   559,   563,   564,   565,   570,
     578,   579,   583,   584,   587,   593,   594,   595,   596,   597,
     601,   607,   613,   614,   620,   624,   633,   634,   635,   636,
     640,   644,   651,   663,   672,   676,   683,   690,   710,   717,
     718,   723,   724,   729,   733,   733,   733,   733,   734,   734,
     734,   734,   735,   735,   735,   735,   736,   736,   736,   736,
     737,   737,   737,   737,   738,   738,   738,   739,   739,   739,
     740,   740,   740,   741,   741,   741,   742,   742,   742,   749,
     753,   754,   758,   759,   763,   767,   771,   775,   780,   785,
     793,   793,   858,   859,   860,   861,   862,   863,   864,   865,
     866,   870,   870,   879,   880,   884,   885,   889,   890,   894,
     897,   900,   900,   906,   909,   912,   920,   923,   930,   934,
     938,   941,   945,   954,   958,   959,   963,   964,   965,   966,
     967,   977,   978,   982,   983,   989,   990,   991,   992,   993,
     994,   995,   996,   997,   998,   999,  1003,  1007,  1008,  1009,
    1010,  1011,  1012,  1013,  1014,  1015,  1016,  1017,  1018,  1019,
    1020,  1021,  1022,  1023,  1024,  1025,  1028,  1032,  1033,  1034,
    1035,  1036,  1037,  1038,  1039,  1040,  1041,  1045,  1046,  1053,
    1057,  1064,  1071,  1075,  1076,  1077,  1078,  1079,  1080,  1081,
    1082,  1083,  1084,  1085,  1086,  1087,  1096,  1102,  1108,  1114,
    1123,  1124,  1125,  1160,  1164,  1172,  1178,  1182,  1183,  1184,
    1185,  1189,  1190,  1191,  1192,  1193,  1194,  1195,  1196,  1197,
    1201,  1202,  1206,  1207,  1211,  1212,  1216,  1217,  1224,  1233,
    1234,  1235,  1236,  1237,  1238,  1239,  1243,  1250,  1251,  1252,
    1253,  1254,  1255,  1256,  1257,  1258,  1259,  1260,  1267,  1272,
    1273
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
  "CLASS", "PUBLIC", "PRIVATE", "PROTECTED", "THIS", "STATIC", "TYPEDEF",
  "AUTO", "EXTERN", "CONST", "VIRTUAL", "EXPLICIT", "FRIEND", "IF", "ELSE",
  "FOR", "WHILE", "DO", "UNTIL", "SWITCH", "CASE", "DEFAULT", "BREAK",
  "CONTINUE", "GOTO", "RETURN", "PRINTF", "SCANF", "MALLOC", "FREE",
  "CALLOC", "REALLOC", "BOOL", "SIZEOF", "VA_LIST", "VA_START", "VA_ARG",
  "VA_END", "OPERATOR", "FCAST", "ABSTRACT_LPAREN", "IDENTIFIER",
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
  "$@5", "@6", "member_decl_list_opt", "inheritance_opt",
  "inheritance_specifier_list", "inheritance_specifier",
  "member_decl_list", "member_item", "constructor_head", "$@7",
  "constructor_def", "destructor_head", "destructor_def",
  "out_of_class_special", "$@8", "$@9", "$@10", "mem_init_opt",
  "mem_initializer_list", "mem_initializer", "access_specifier",
  "init_declarator_list_opt", "init_declarator_list", "init_declarator",
  "initializer", "initializer_list", "initializer_item", "pointer",
  "declarator", "abstract_declarator", "direct_abstract_declarator",
  "direct_declarator", "method_cv_opt", "operator_function_id",
  "overloadable_operator", "param_scope", "constructor_args",
  "parameter_list_opt", "parameter_list", "parameter_decl",
  "function_definition", "$@11", "statement", "compound_stmt", "$@12",
  "block_item_list_opt", "block_item_list", "expr_stmt", "selection_stmt",
  "$@13", "labeled_stmt", "iteration_stmt", "for_open", "for_incr_opt",
  "jump_stmt", "expr", "assignment_expr", "assign_op", "constant_expr",
  "binary_expr", "unary_expr", "type_name", "type_name_specifiers",
  "type_name_specifier", "postfix_expr", "builtin_call",
  "constructor_args_opt", "argument_list_opt", "argument_list", "argument",
  "primary_expr", "string_literal", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-392)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-195)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -392,  1994,  -392,   -10,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,     7,    37,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,   -44,  -392,  -392,  1790,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,   -39,   -32,  -392,  -392,    -9,
       9,  -392,  -392,    -5,  2017,    31,    44,  -392,  -392,     0,
    -392,   -52,     2,  -392,    63,   -29,   -17,  -392,  1843,    48,
    1843,    35,    87,   141,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,    86,    90,  -392,
      55,   103,    44,   113,  -392,     0,  -392,  -392,  -392,   -17,
    1139,   131,  1860,   444,  -392,  -392,  -392,   155,   224,   177,
    -392,   233,  -392,   180,  1843,  -392,   104,  -392,   176,  -392,
     202,  -392,  -392,   185,   187,   188,  -392,   212,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,   245,   235,   247,   259,
     265,   266,   269,   270,   271,   277,  -392,   278,   279,   280,
     281,   297,   299,   301,  1593,   305,   307,   308,   309,  -392,
      11,  -392,  -392,  -392,  -392,  -392,  1660,  1660,  1660,  1660,
    1660,  1660,  1660,  1660,  1526,   991,  -392,  -392,  2058,   572,
     134,  -392,  -392,   318,   693,  2025,   139,  -392,  -392,   300,
    -392,  -392,  -392,   311,  -392,  -392,   174,  -392,   310,  -392,
    -392,  -392,  -392,  1843,  -392,  -392,  -392,   304,  -392,   162,
    -392,  2025,   306,  1660,  1660,  1660,  1660,  1660,  1660,  1660,
    1660,  1660,  1526,  1526,  1526,  1526,  1526,  1526,  1660,  1526,
    -392,  1526,  1526,  1526,  1660,   365,  1660,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,   235,   247,   259,   265,   266,
     269,   270,   271,   277,   248,   251,  -392,   301,  -392,    11,
     199,  -392,   312,   350,  -392,   367,  1660,  -392,  -392,   181,
    -392,  1660,  1660,  1660,  1660,  1660,  1660,  1660,  1660,  1660,
    1660,  1660,  1660,  1660,  1660,  1660,  1660,  1660,  1660,  1660,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  1660,   260,   369,  -392,  -392,   272,  1526,  1660,  -392,
     218,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
     319,   320,   322,   917,   325,   326,  1660,   345,   323,   324,
     382,  1321,  -392,   352,   378,  -392,  -392,  1790,  -392,  -392,
     331,   805,  -392,  -392,  -392,  -392,  1249,  -392,   105,  1457,
     329,   333,  -392,  1660,  -392,  -392,  2025,   330,   353,   354,
     355,   344,  -392,  -392,   693,   351,   187,  -392,  -392,  1843,
     349,  -392,   356,   357,   358,   359,   360,   362,   363,   364,
     366,   368,  -392,  -392,   381,   384,  -392,   391,   392,   393,
     396,   397,   398,   399,   400,   410,   411,   412,  -392,   413,
    -392,  -392,  -392,  -392,  1660,  -392,  1660,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,    98,  -392,   512,
      71,  -392,   361,  -392,   379,   415,  2058,  -392,  -392,  1065,
     167,   167,   214,   214,   595,   595,  2068,   178,   -11,  2100,
     252,   140,   214,   214,   126,   126,  -392,  -392,  -392,  -392,
    -392,   402,  -392,  -392,   403,   414,   186,  -392,  -392,  1660,
    -392,  1660,    52,  1660,  1660,   394,   917,  -392,  -392,   421,
    -392,   144,   917,  -392,  -392,  1393,  1393,  -392,    57,  -392,
    -392,   510,  1963,  -392,   419,  -392,  1526,  1526,  1526,   174,
     424,  -392,  -392,   425,  -392,   310,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  1526,  -392,  -392,  -392,
    -392,  -392,  -392,  1727,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,   426,  -392,   427,   361,   580,  1139,   456,  -392,  -392,
    1660,   489,   490,  -392,  -392,   219,   221,   435,   443,   225,
     237,   917,  -392,  -392,  -392,  -392,  1660,  1660,  -392,  -392,
    -392,  -392,  -392,   436,   449,   451,  -392,  -392,  -392,   486,
    -392,  -392,  -392,  -392,  -392,   459,  -392,  1139,  2058,  -392,
    -392,   917,   917,  -392,  1660,   917,  -392,  -392,   461,   465,
     466,  -392,  -392,  -392,   310,  -392,  -392,   552,  -392,   253,
    -392,   310,   917,   917,  -392,   917,    10,  -392,  -392,  -392,
    -392,  -392,  -392
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    20,    21,    22,    23,    24,    26,
      27,    28,    29,     0,     0,    12,    15,    14,    13,    16,
      17,    18,    25,    30,    31,     3,     5,    90,    11,    19,
      32,     6,     4,     7,     8,    40,    41,    38,    35,    47,
      48,    45,    42,     0,     0,   120,    31,   106,   105,     0,
      10,     0,    91,    92,     0,    94,   111,   124,    49,     0,
      49,    51,     0,     0,   155,   156,   153,   154,   149,   150,
     147,   148,   151,   152,   157,   158,   159,   160,   161,   162,
     163,   164,   165,   166,   144,   141,   139,   140,   145,   146,
     134,   135,   136,   137,   138,   143,   142,     0,     0,   133,
       0,     0,     0,     0,     9,     0,   109,   108,   107,   110,
       0,     0,   169,     0,    87,    88,    89,    17,     0,     0,
      31,     0,    61,     0,    50,    59,    80,    64,     0,    66,
       0,    62,    36,     0,     0,     0,    75,     0,   168,   167,
     121,   125,   122,   126,   123,    93,    94,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   324,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   318,
       0,   319,   320,   321,   339,   323,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    95,    96,   223,   256,
     257,   300,   290,   322,     0,   172,     0,   170,   129,     0,
      67,    65,    68,     0,    39,    60,     0,    71,     0,    74,
     191,    73,    63,    49,    46,    57,    58,    52,    53,     0,
      43,   172,     0,   310,   310,   310,   310,   310,   310,   310,
     310,   310,   312,   312,   312,   312,   312,   312,   310,     0,
     267,   312,   312,   312,   310,     0,   310,   258,   259,   260,
     262,   263,   261,   264,   265,   273,   274,   275,   276,   277,
     279,   280,   281,   282,     0,     0,   284,   278,   283,   285,
       0,   221,     0,   269,   272,     0,     0,    97,   102,     0,
     100,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     226,   227,   228,   229,   230,   231,   232,   233,   234,   235,
     225,     0,     0,     0,   298,   299,     0,   312,     0,   340,
       0,    20,    21,    22,    23,    24,    26,    27,    28,    29,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    25,   318,    31,   197,   188,    90,   195,   182,
       0,     0,   183,   184,   187,   185,     0,   186,     0,   179,
       0,   173,   174,     0,   128,   130,   172,     0,     0,     0,
       0,    81,    82,    70,     0,     0,     0,    55,    56,    49,
       0,    78,   311,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   316,   317,     0,   313,   314,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   337,     0,
     286,   287,   288,   289,     0,   338,     0,   273,   274,   275,
     276,   277,   279,   280,   281,   282,   278,     0,   285,     0,
     112,   270,   114,   271,     0,     0,   236,   256,    98,     0,
     248,   249,   246,   247,   242,   243,   238,   237,     0,   239,
     240,   241,   244,   245,   250,   251,   252,   253,   254,   224,
     296,     0,   297,   293,     0,     0,     0,   189,   190,     0,
     213,     0,     0,     0,     0,     0,     0,   216,   217,     0,
     218,     0,     0,   181,   196,     0,     0,   198,   112,   177,
     178,   131,     0,   171,     0,    72,   312,   312,   312,     0,
       0,    37,    54,     0,    76,     0,   327,   328,   329,   330,
     331,   333,   334,   335,   336,   301,     0,   302,   303,   304,
     305,   306,   332,   268,   307,   308,   309,   326,   325,   222,
     266,     0,   116,     0,   113,     0,     0,     0,    99,   101,
       0,     0,     0,   292,   291,     0,     0,     0,     0,     0,
       0,     0,   204,   220,   219,   205,   214,   214,   132,   127,
     176,   175,    69,     0,     0,     0,    83,   192,    44,    80,
      79,   315,   115,   117,   118,     0,   103,     0,   255,   295,
     294,     0,     0,   209,     0,     0,   201,   203,     0,   215,
       0,    86,    84,    85,     0,   119,   104,   199,   206,     0,
     210,     0,     0,     0,    77,     0,     0,   202,   212,   211,
     200,   208,   207
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -392,  -392,  -392,    17,    -1,   -23,  -392,   567,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,   -54,  -392,  -392,   206,  -392,
     468,  -392,  -392,   475,  -392,   477,  -392,  -392,  -392,  -392,
      26,  -392,    97,  -125,  -392,  -392,   493,  -107,  -392,   160,
    -260,   -22,  -343,  -391,   -53,  -392,   268,  -392,  -392,   488,
    -211,  -392,   109,   602,  -392,  -326,  -126,  -392,   230,  -392,
    -296,  -392,  -392,  -392,  -392,  -392,    51,  -392,  -176,   -98,
    -392,   273,  -250,  -112,  -167,  -392,   337,  -392,  -392,   163,
    -213,  -392,    95,  -392,  -392
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    25,   346,   347,    28,    29,    38,    30,    59,
     213,    58,    61,   379,    60,   123,   135,   217,   218,   124,
     125,   126,   366,   127,   128,   129,    31,   221,   569,   505,
     208,   371,   372,   130,    51,    52,    53,   278,   279,   280,
      54,   146,   431,   432,    56,   559,    57,    99,   195,   382,
     360,   361,   362,   131,   111,   348,   349,   374,   350,   351,
     352,   353,   601,   354,   355,   356,   588,   357,   358,   271,
     311,   435,   188,   189,   393,   273,   274,   190,   191,   383,
     394,   395,   396,   192,   193
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      27,   109,   211,   186,    50,    55,   133,   472,   270,   219,
     380,   611,   187,   430,   197,   199,   490,   272,    26,    43,
     397,   398,   399,   400,   401,   484,   436,   103,   404,   405,
     406,   440,   441,   442,   443,   444,   445,   446,   447,   534,
     449,   450,   451,   452,   453,   454,   455,   456,   457,   458,
      62,    44,   240,   547,    45,   102,   110,    27,   104,    27,
     486,    35,    36,   270,   247,   248,   249,   250,   251,   252,
     253,   254,   403,   -33,   245,   122,   540,   122,   -33,   106,
     -34,   548,   373,  -180,   531,   106,   436,   187,   112,   113,
      47,    39,    40,   106,   100,    48,   -34,   534,    63,   488,
      33,    34,   414,   -33,   465,    49,    44,   101,    44,   140,
     427,    45,   102,   448,    44,   105,   246,    45,   102,    37,
     612,   -34,   134,    27,   427,   197,   197,   197,   197,   197,
     197,   197,   197,   197,   392,   392,   392,   392,   392,   392,
     197,   122,   466,   392,   392,   392,   197,   107,   197,    41,
     552,   427,   108,   107,    44,   494,   555,   142,   108,   375,
     132,   107,    49,   429,   437,   481,   108,   430,    49,   437,
     437,   437,   437,   437,   437,   437,   437,   429,   437,   437,
     437,   437,   437,   437,   437,   437,   437,   437,    47,   556,
     557,   206,   136,    48,   359,   312,   137,   313,   314,   315,
     138,   114,   115,   116,   429,   139,   281,   282,   283,   284,
     285,   286,    27,   459,   207,   487,   377,   378,   414,   392,
     359,   297,   298,   299,   437,   587,   368,   144,   369,   370,
     122,   293,   294,   295,   296,   297,   298,   299,   316,   317,
     318,   215,   216,   194,   281,   282,   283,   284,   285,   286,
     287,   219,   363,   364,   554,   597,   598,   414,   121,   600,
     295,   296,   297,   298,   299,   493,   290,   291,   292,   293,
     294,   295,   296,   297,   298,   299,   608,   609,   119,   610,
     281,   282,   202,   563,   564,   565,   209,   203,   210,   212,
     578,   204,   438,   545,   439,   546,   214,   549,   550,   414,
     220,   544,   410,   411,   530,   412,   413,   295,   296,   297,
     298,   299,   414,   415,   460,   461,   529,   222,   281,   282,
     283,   284,   285,   286,    50,   503,   463,   464,   467,   468,
     110,   533,   414,   581,   414,   582,    50,   489,   414,   585,
     223,   187,   292,   293,   294,   295,   296,   297,   298,   299,
     414,   586,   224,   417,   418,   419,   420,   421,   422,   423,
     424,   425,   264,   265,   225,   359,   414,   606,   141,   143,
     226,   227,   266,   485,   228,   229,   230,   319,    27,   570,
     589,   589,   231,   232,   233,   234,   235,   384,   385,   386,
     387,   388,   389,   390,   391,   426,   122,   268,   392,   392,
     392,   402,   236,   427,   237,   428,   238,   407,   599,   409,
     241,   530,   242,   243,   244,   365,   367,   376,   392,   408,
     381,   434,   210,   462,   469,   470,   416,   471,   437,   576,
     473,   474,   476,   477,   478,   109,   479,   575,   187,   482,
      47,   245,   483,   491,   495,    48,   492,   147,   148,   149,
     150,   151,   152,   153,   154,   155,   429,   499,   496,   497,
     498,   156,   501,   504,   536,   541,   542,   535,   604,   363,
     596,   506,   507,   508,   509,   607,   510,   511,   512,   187,
     513,   551,   514,   157,   158,   159,   160,   161,   162,   163,
     164,   359,   165,   166,   167,   515,   168,   516,   169,   170,
     171,   172,   173,   174,   175,   517,   518,   519,   176,   177,
     520,   521,   522,   523,   524,   147,   148,   149,   150,   151,
     152,   153,   154,   155,   525,   526,   527,   528,   543,   156,
     537,   553,   558,   562,   178,   567,   568,   179,   180,   181,
     572,   577,   573,   579,   580,   583,   182,   183,   584,   184,
     591,   157,   158,   159,   160,   161,   162,   163,   164,   198,
     165,   166,   167,   592,   168,   593,   169,   170,   171,   172,
     173,   174,   175,   206,   595,   602,   176,   177,   414,   605,
     603,    42,   502,   147,   148,   149,   150,   151,   152,   153,
     154,   155,   205,   201,   200,   594,   566,   156,   145,   539,
     196,   561,   178,    32,   500,   179,   180,   181,   590,   475,
     433,   571,     0,     0,   182,   183,     0,   184,     0,   157,
     158,   159,   160,   161,   162,   163,   164,   532,   165,   166,
     167,     0,   168,     0,   169,   170,   171,   172,   173,   174,
     175,     0,     0,     0,   176,   177,   300,   301,   302,   303,
     304,   305,   306,   307,   308,   309,     0,   310,     0,     0,
       0,   281,   282,   283,   284,     0,     0,     0,     0,     0,
     178,     0,     0,   179,   180,   181,     0,     0,     0,     0,
       0,     0,   182,   183,     0,   184,   293,   294,   295,   296,
     297,   298,   299,     0,   320,   574,   321,   322,   323,   324,
     325,   326,   327,   328,   329,    13,    14,     0,     0,     0,
     156,    15,    16,    17,    18,    19,    20,     0,    21,   330,
       0,   331,   332,   333,   334,   335,   336,   337,   338,   339,
     340,   341,   157,   158,   159,   160,   161,   162,   342,   164,
      23,   165,   166,   167,     0,   168,     0,   343,   344,   171,
     172,   173,   174,   175,     0,     0,     0,   176,   177,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   178,     0,     0,   179,   180,   181,     0,
       0,     0,     0,     0,     0,   182,   183,     0,   184,     0,
       0,     0,     0,   345,  -193,   210,   320,     0,   321,   322,
     323,   324,   325,   326,   327,   328,   329,    13,    14,     0,
       0,     0,   156,    15,    16,    17,    18,    19,    20,     0,
      21,   330,     0,   331,   332,   333,   334,   335,   336,   337,
     338,   339,   340,   341,   157,   158,   159,   160,   161,   162,
     342,   164,    23,   165,   166,   167,     0,   168,     0,   343,
     344,   171,   172,   173,   174,   175,     0,     0,     0,   176,
     177,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   178,     0,     0,   179,   180,
     181,     0,     0,     0,     0,     0,     0,   182,   183,     0,
     184,     0,     0,     0,     0,   345,  -194,   210,   320,     0,
     321,   322,   323,   324,   325,   326,   327,   328,   329,    13,
      14,     0,     0,     0,   156,    15,    16,    17,    18,    19,
      20,     0,    21,   330,     0,   331,   332,   333,   334,   335,
     336,   337,   338,   339,   340,   341,   157,   158,   159,   160,
     161,   162,   342,   164,    23,   165,   166,   167,     0,   168,
       0,   343,   344,   171,   172,   173,   174,   175,     0,     0,
       0,   176,   177,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   147,   148,   149,   150,   151,   152,
     153,   154,   155,     0,     0,     0,     0,   178,   156,     0,
     179,   180,   181,     0,     0,     0,     0,     0,     0,   182,
     183,     0,   184,     0,     0,     0,     0,   345,     0,   210,
     157,   158,   159,   160,   161,   162,   163,   164,     0,   165,
     166,   167,     0,   168,     0,   169,   170,   171,   172,   173,
     174,   175,     0,     0,     0,   176,   177,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   147,   148,
     149,   150,   151,   152,   153,   154,   155,     0,     0,     0,
       0,   178,   156,     0,   179,   180,   181,     0,     0,     0,
       0,     0,     0,   182,   183,   275,   184,   276,     0,     0,
       0,     0,   277,   185,   157,   158,   159,   160,   161,   162,
     163,   164,     0,   165,   166,   167,     0,   168,     0,   169,
     170,   171,   172,   173,   174,   175,     0,     0,     0,   176,
     177,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   147,   148,   149,   150,   151,   152,   153,   154,
     155,     0,     0,     0,     0,   178,   156,     0,   179,   180,
     181,     0,     0,     0,     0,     0,     0,   182,   183,   275,
     184,   276,     0,     0,     0,     0,   538,   185,   157,   158,
     159,   160,   161,   162,   163,   164,     0,   165,   166,   167,
       0,   168,     0,   169,   170,   171,   172,   173,   174,   175,
       0,     0,     0,   176,   177,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   178,
       0,     0,   179,   180,   181,     0,     0,     0,     0,     0,
       0,   182,   183,     0,   184,     0,     0,     0,     0,     0,
       0,   185,   321,   322,   323,   324,   325,   326,   327,   328,
     329,    13,    14,     0,     0,     0,   156,    15,    16,    17,
      18,    19,    20,     0,    21,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   157,   158,
     159,   160,   161,   162,   342,   164,    23,   165,   166,   167,
       0,   168,     0,   169,   344,   171,   172,   173,   174,   175,
       0,     0,     0,   176,   177,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   147,   148,   149,   150,   151,   152,
     153,   154,   155,     0,     0,     0,     0,     0,   156,   178,
       0,     0,   179,   180,   181,     0,     0,     0,     0,     0,
       0,   182,   183,     0,   184,     0,     0,     0,     0,   345,
     157,   158,   159,   160,   161,   162,   163,   164,     0,   165,
     166,   167,     0,   168,     0,   169,   170,   171,   172,   173,
     174,   175,     0,     0,     0,   176,   177,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   147,   148,   149,   150,
     151,   152,   153,   154,   155,     0,     0,     0,     0,     0,
     156,   178,     0,     0,   179,   180,   181,     0,     0,     0,
       0,     0,     0,   182,   183,     0,   184,     0,     0,     0,
       0,   480,   157,   158,   159,   160,   161,   162,   163,   164,
       0,   165,   166,   167,     0,   168,     0,   169,   170,   171,
     172,   173,   174,   175,     0,     0,     0,   176,   177,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,     0,     0,     0,     0,    15,    16,    17,    18,    19,
      20,     0,    21,   178,     0,     0,   179,   180,   181,     0,
       0,     0,     0,     0,     0,   182,   183,     0,   184,     0,
       0,     0,    22,   345,    23,     0,     0,     0,    44,     0,
     427,    45,    46,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   255,
     256,   257,   258,   259,   260,   261,   262,   263,   264,   265,
       0,     0,     0,   156,     0,     0,     0,    47,   266,     0,
       0,     0,    48,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    49,   429,     0,   157,   158,   159,   160,   161,
     162,   267,   164,   268,   165,   166,   167,     0,   168,     0,
     169,   269,   171,   172,   173,   174,   175,     0,     0,     0,
     176,   177,     0,     0,     0,     0,   147,   148,   149,   150,
     151,   152,   153,   154,   155,     0,     0,     0,     0,     0,
     156,     0,     0,     0,     0,     0,   178,     0,     0,   179,
     180,   181,     0,     0,     0,     0,     0,     0,   182,   183,
       0,   184,   157,   158,   159,   160,   161,   162,   163,   164,
       0,   165,   166,   167,     0,   168,     0,   169,   170,   171,
     172,   173,   174,   175,     0,     0,     0,   176,   177,     0,
       0,     0,     0,   147,   148,   149,   150,   151,   152,   153,
     154,   155,     0,     0,     0,     0,     0,   156,     0,     0,
       0,     0,     0,   178,     0,     0,   179,   180,   181,     0,
       0,     0,     0,     0,     0,   182,   183,     0,   239,   157,
     158,   159,   160,   161,   162,   163,   164,     0,   165,   166,
     167,     0,   168,     0,   169,   170,   171,   172,   173,   174,
     175,     0,     0,     0,   176,   177,     0,     0,     0,     0,
     147,   148,   149,   150,   151,   152,   153,   154,   155,     0,
       0,     0,     0,     0,   156,     0,     0,     0,     0,     0,
     178,     0,     0,   179,   180,   181,     0,     0,     0,     0,
       0,     0,   182,   183,     0,   184,   157,   158,   159,   160,
     161,   162,   163,   164,     0,   165,   166,   167,     0,   168,
       0,   169,   170,   171,   172,   173,   174,   175,     0,     0,
       0,   176,   177,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,     0,     0,     0,     0,    15,    16,
      17,    18,    19,    20,     0,    21,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   182,
     183,     0,   184,     0,     0,    22,     0,    23,     0,     0,
       0,    44,     0,     0,    45,    46,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,   114,   115,   116,
       0,    15,    16,    17,    18,    19,   117,   118,    21,     0,
       0,     0,     0,     0,     0,     0,     0,   156,     0,     0,
      47,     0,     0,     0,     0,    48,     0,     0,    22,     0,
      23,     0,     0,     0,     0,    49,     0,   119,   120,   157,
     158,   159,   160,   161,   162,     0,   164,     0,   165,   166,
     167,     0,   168,     0,   169,     0,   171,   172,   173,   174,
     175,     0,     0,     0,   176,   177,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   121,     0,     0,     0,
     178,     0,     0,   179,   180,   181,     0,     0,     0,     0,
       0,     0,   182,   183,     0,   184,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,     0,     0,     0,
       0,    15,    16,    17,    18,    19,    20,     0,    21,     0,
       0,     0,     0,     0,     2,     3,     0,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    22,     0,
      23,     0,    15,    16,    17,    18,    19,    20,   120,    21,
       0,     0,     0,     0,     0,   560,     0,     0,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    22,
       0,    23,     0,    15,    16,    17,    18,    19,    20,    24,
      21,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      22,     0,    23,     0,     0,     0,     0,     0,     0,     0,
     120,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,    75,    76,    77,    78,    79,    80,    81,    82,
      83,     0,    84,     0,     0,    85,    86,    87,    88,    89,
      90,    91,    92,    93,    94,     0,     0,     0,     0,    95,
      96,     0,    97,    98,   281,   282,   283,   284,   285,   286,
     287,   288,     0,     0,   281,   282,   283,   284,   285,   286,
       0,     0,     0,     0,   289,     0,   290,   291,   292,   293,
     294,   295,   296,   297,   298,   299,   290,   291,   292,   293,
     294,   295,   296,   297,   298,   299,   281,   282,   283,   284,
     285,   286,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   291,
     292,   293,   294,   295,   296,   297,   298,   299
};

static const yytype_int16 yycheck[] =
{
       1,    54,   128,   110,    27,    27,    60,   333,   184,   134,
     221,     1,   110,   273,   112,   113,   359,   184,     1,    63,
     233,   234,   235,   236,   237,   351,   276,    49,   241,   242,
     243,   281,   282,   283,   284,   285,   286,   287,   288,   430,
     290,   291,   292,   293,   294,   295,   296,   297,   298,   299,
      55,    51,   164,     1,    54,    55,    85,    58,   110,    60,
     356,    54,    55,   239,   176,   177,   178,   179,   180,   181,
     182,   183,   239,   112,    63,    58,    87,    60,    87,    22,
     112,    29,   208,   112,   427,    22,   336,   185,   105,   106,
      90,    54,    55,    22,    63,    95,    87,   488,   103,   359,
     110,   111,   113,   112,   317,   105,    51,    63,    51,    54,
      53,    54,    55,   289,    51,   113,   105,    54,    55,   112,
     110,   112,    87,   124,    53,   223,   224,   225,   226,   227,
     228,   229,   230,   231,   232,   233,   234,   235,   236,   237,
     238,   124,   318,   241,   242,   243,   244,    90,   246,   112,
     476,    53,    95,    90,    51,   366,   482,    54,    95,   213,
     112,    90,   105,   106,   276,   341,    95,   427,   105,   281,
     282,   283,   284,   285,   286,   287,   288,   106,   290,   291,
     292,   293,   294,   295,   296,   297,   298,   299,    90,   485,
     486,    87,   105,    95,   195,    61,    55,    63,    64,    65,
     114,    14,    15,    16,   106,   115,    66,    67,    68,    69,
      70,    71,   213,   311,   110,   110,    54,    55,   113,   317,
     221,    95,    96,    97,   336,   551,    52,   114,    54,    55,
     213,    91,    92,    93,    94,    95,    96,    97,   104,   105,
     106,    54,    55,   112,    66,    67,    68,    69,    70,    71,
      72,   376,   113,   114,   110,   581,   582,   113,   103,   585,
      93,    94,    95,    96,    97,   363,    88,    89,    90,    91,
      92,    93,    94,    95,    96,    97,   602,   603,    54,   605,
      66,    67,   105,   496,   497,   498,   110,    54,   112,    87,
     540,   111,   111,   469,   113,   471,   111,   473,   474,   113,
     112,   115,    54,    55,   416,    54,    55,    93,    94,    95,
      96,    97,   113,   114,    54,    55,   414,   105,    66,    67,
      68,    69,    70,    71,   347,   379,    54,    55,   110,   111,
      85,   429,   113,   114,   113,   114,   359,   359,   113,   114,
     105,   439,    90,    91,    92,    93,    94,    95,    96,    97,
     113,   114,   105,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,   105,   366,   113,   114,   100,   101,
     105,   105,    22,   356,   105,   105,   105,    59,   379,   505,
     556,   557,   105,   105,   105,   105,   105,   224,   225,   226,
     227,   228,   229,   230,   231,    45,   379,    47,   496,   497,
     498,   238,   105,    53,   105,    55,   105,   244,   584,   246,
     105,   523,   105,   105,   105,   115,   105,   113,   516,    54,
     114,    54,   112,    54,   105,   105,   114,   105,   540,   536,
     105,   105,    87,   110,   110,   488,    54,   535,   536,    87,
      90,    63,   111,   114,   114,    95,   113,     3,     4,     5,
       6,     7,     8,     9,    10,    11,   106,   113,   105,   105,
     105,    17,   111,   114,    85,    63,    63,   106,   594,   113,
     577,   114,   114,   114,   114,   601,   114,   114,   114,   577,
     114,    87,   114,    39,    40,    41,    42,    43,    44,    45,
      46,   492,    48,    49,    50,   114,    52,   113,    54,    55,
      56,    57,    58,    59,    60,   114,   114,   114,    64,    65,
     114,   114,   114,   114,   114,     3,     4,     5,     6,     7,
       8,     9,    10,    11,   114,   114,   114,   114,   114,    17,
     115,   110,    22,   114,    90,   111,   111,    93,    94,    95,
     114,    85,   115,    54,    54,   110,   102,   103,   105,   105,
     114,    39,    40,    41,    42,    43,    44,    45,    46,   115,
      48,    49,    50,   114,    52,   114,    54,    55,    56,    57,
      58,    59,    60,    87,   115,   114,    64,    65,   113,    27,
     114,    14,   376,     3,     4,     5,     6,     7,     8,     9,
      10,    11,   124,   118,   117,   569,   499,    17,   105,   439,
     112,   492,    90,     1,   374,    93,    94,    95,   557,   336,
     273,   516,    -1,    -1,   102,   103,    -1,   105,    -1,    39,
      40,    41,    42,    43,    44,    45,    46,   115,    48,    49,
      50,    -1,    52,    -1,    54,    55,    56,    57,    58,    59,
      60,    -1,    -1,    -1,    64,    65,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    -1,    85,    -1,    -1,
      -1,    66,    67,    68,    69,    -1,    -1,    -1,    -1,    -1,
      90,    -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,
      -1,    -1,   102,   103,    -1,   105,    91,    92,    93,    94,
      95,    96,    97,    -1,     1,   115,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    -1,    -1,    -1,
      17,    18,    19,    20,    21,    22,    23,    -1,    25,    26,
      -1,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    -1,    52,    -1,    54,    55,    56,
      57,    58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    -1,    -1,    93,    94,    95,    -1,
      -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,    -1,
      -1,    -1,    -1,   110,   111,   112,     1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    -1,
      -1,    -1,    17,    18,    19,    20,    21,    22,    23,    -1,
      25,    26,    -1,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    -1,    52,    -1,    54,
      55,    56,    57,    58,    59,    60,    -1,    -1,    -1,    64,
      65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    -1,    -1,    93,    94,
      95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,
     105,    -1,    -1,    -1,    -1,   110,   111,   112,     1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    -1,    -1,    -1,    17,    18,    19,    20,    21,    22,
      23,    -1,    25,    26,    -1,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    -1,    52,
      -1,    54,    55,    56,    57,    58,    59,    60,    -1,    -1,
      -1,    64,    65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    90,    17,    -1,
      93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,   102,
     103,    -1,   105,    -1,    -1,    -1,    -1,   110,    -1,   112,
      39,    40,    41,    42,    43,    44,    45,    46,    -1,    48,
      49,    50,    -1,    52,    -1,    54,    55,    56,    57,    58,
      59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    90,    17,    -1,    93,    94,    95,    -1,    -1,    -1,
      -1,    -1,    -1,   102,   103,   104,   105,   106,    -1,    -1,
      -1,    -1,   111,   112,    39,    40,    41,    42,    43,    44,
      45,    46,    -1,    48,    49,    50,    -1,    52,    -1,    54,
      55,    56,    57,    58,    59,    60,    -1,    -1,    -1,    64,
      65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    -1,    -1,    -1,    -1,    90,    17,    -1,    93,    94,
      95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,   104,
     105,   106,    -1,    -1,    -1,    -1,   111,   112,    39,    40,
      41,    42,    43,    44,    45,    46,    -1,    48,    49,    50,
      -1,    52,    -1,    54,    55,    56,    57,    58,    59,    60,
      -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,
      -1,   102,   103,    -1,   105,    -1,    -1,    -1,    -1,    -1,
      -1,   112,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    -1,    -1,    -1,    17,    18,    19,    20,
      21,    22,    23,    -1,    25,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    39,    40,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      -1,    52,    -1,    54,    55,    56,    57,    58,    59,    60,
      -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    17,    90,
      -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,
      -1,   102,   103,    -1,   105,    -1,    -1,    -1,    -1,   110,
      39,    40,    41,    42,    43,    44,    45,    46,    -1,    48,
      49,    50,    -1,    52,    -1,    54,    55,    56,    57,    58,
      59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      17,    90,    -1,    -1,    93,    94,    95,    -1,    -1,    -1,
      -1,    -1,    -1,   102,   103,    -1,   105,    -1,    -1,    -1,
      -1,   110,    39,    40,    41,    42,    43,    44,    45,    46,
      -1,    48,    49,    50,    -1,    52,    -1,    54,    55,    56,
      57,    58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    -1,    -1,    -1,    -1,    18,    19,    20,    21,    22,
      23,    -1,    25,    90,    -1,    -1,    93,    94,    95,    -1,
      -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,    -1,
      -1,    -1,    45,   110,    47,    -1,    -1,    -1,    51,    -1,
      53,    54,    55,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      -1,    -1,    -1,    17,    -1,    -1,    -1,    90,    22,    -1,
      -1,    -1,    95,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,    -1,    39,    40,    41,    42,    43,
      44,    45,    46,    47,    48,    49,    50,    -1,    52,    -1,
      54,    55,    56,    57,    58,    59,    60,    -1,    -1,    -1,
      64,    65,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      17,    -1,    -1,    -1,    -1,    -1,    90,    -1,    -1,    93,
      94,    95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,
      -1,   105,    39,    40,    41,    42,    43,    44,    45,    46,
      -1,    48,    49,    50,    -1,    52,    -1,    54,    55,    56,
      57,    58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,
      -1,    -1,    -1,    90,    -1,    -1,    93,    94,    95,    -1,
      -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,    39,
      40,    41,    42,    43,    44,    45,    46,    -1,    48,    49,
      50,    -1,    52,    -1,    54,    55,    56,    57,    58,    59,
      60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    17,    -1,    -1,    -1,    -1,    -1,
      90,    -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,
      -1,    -1,   102,   103,    -1,   105,    39,    40,    41,    42,
      43,    44,    45,    46,    -1,    48,    49,    50,    -1,    52,
      -1,    54,    55,    56,    57,    58,    59,    60,    -1,    -1,
      -1,    64,    65,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    -1,    18,    19,
      20,    21,    22,    23,    -1,    25,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   102,
     103,    -1,   105,    -1,    -1,    45,    -1,    47,    -1,    -1,
      -1,    51,    -1,    -1,    54,    55,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      -1,    18,    19,    20,    21,    22,    23,    24,    25,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,
      90,    -1,    -1,    -1,    -1,    95,    -1,    -1,    45,    -1,
      47,    -1,    -1,    -1,    -1,   105,    -1,    54,    55,    39,
      40,    41,    42,    43,    44,    -1,    46,    -1,    48,    49,
      50,    -1,    52,    -1,    54,    -1,    56,    57,    58,    59,
      60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      90,    -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,
      -1,    -1,   102,   103,    -1,   105,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    -1,    -1,    -1,
      -1,    18,    19,    20,    21,    22,    23,    -1,    25,    -1,
      -1,    -1,    -1,    -1,     0,     1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    45,    -1,
      47,    -1,    18,    19,    20,    21,    22,    23,    55,    25,
      -1,    -1,    -1,    -1,    -1,    62,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    45,
      -1,    47,    -1,    18,    19,    20,    21,    22,    23,    55,
      25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      45,    -1,    47,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      55,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,    75,    76,    77,    78,    79,    80,    81,    82,
      83,    -1,    85,    -1,    -1,    88,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    -1,    -1,    -1,    -1,   102,
     103,    -1,   105,   106,    66,    67,    68,    69,    70,    71,
      72,    73,    -1,    -1,    66,    67,    68,    69,    70,    71,
      -1,    -1,    -1,    -1,    86,    -1,    88,    89,    90,    91,
      92,    93,    94,    95,    96,    97,    88,    89,    90,    91,
      92,    93,    94,    95,    96,    97,    66,    67,    68,    69,
      70,    71,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    92,    93,    94,    95,    96,    97
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   117,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    18,    19,    20,    21,    22,
      23,    25,    45,    47,    55,   118,   119,   120,   121,   122,
     124,   142,   169,   110,   111,    54,    55,   112,   123,    54,
      55,   112,   123,    63,    51,    54,    55,    90,    95,   105,
     121,   150,   151,   152,   156,   157,   160,   162,   127,   125,
     130,   128,    55,   103,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    85,    88,    89,    90,    91,    92,
      93,    94,    95,    96,    97,   102,   103,   105,   106,   163,
      63,    63,    55,   157,   110,   113,    22,    90,    95,   160,
      85,   170,   105,   106,    14,    15,    16,    23,    24,    54,
      55,   103,   119,   131,   135,   136,   137,   139,   140,   141,
     149,   169,   112,   131,    87,   132,   105,    55,   114,   115,
      54,   162,    54,   162,   114,   152,   157,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    17,    39,    40,    41,
      42,    43,    44,    45,    46,    48,    49,    50,    52,    54,
      55,    56,    57,    58,    59,    60,    64,    65,    90,    93,
      94,    95,   102,   103,   105,   112,   153,   185,   188,   189,
     193,   194,   199,   200,   112,   164,   165,   185,   115,   185,
     141,   139,   105,    54,   111,   136,    87,   110,   146,   110,
     112,   172,    87,   126,   111,    54,    55,   133,   134,   149,
     112,   143,   105,   105,   105,   105,   105,   105,   105,   105,
     105,   105,   105,   105,   105,   105,   105,   105,   105,   105,
     189,   105,   105,   105,   105,    63,   105,   189,   189,   189,
     189,   189,   189,   189,   189,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    22,    45,    47,    55,
     184,   185,   190,   191,   192,   104,   106,   111,   153,   154,
     155,    66,    67,    68,    69,    70,    71,    72,    73,    86,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      74,    75,    76,    77,    78,    79,    80,    81,    82,    83,
      85,   186,    61,    63,    64,    65,   104,   105,   106,    59,
       1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      26,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    45,    54,    55,   110,   119,   120,   171,   172,
     174,   175,   176,   177,   179,   180,   181,   183,   184,   120,
     166,   167,   168,   113,   114,   115,   138,   105,    52,    54,
      55,   147,   148,   172,   173,   131,   113,    54,    55,   129,
     166,   114,   165,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   185,   190,   196,   197,   198,   196,   196,   196,
     196,   196,   195,   190,   196,   196,   196,   195,    54,   195,
      54,    55,    54,    55,   113,   114,   114,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    45,    53,    55,   106,
     156,   158,   159,   192,    54,   187,   188,   189,   111,   113,
     188,   188,   188,   188,   188,   188,   188,   188,   184,   188,
     188,   188,   188,   188,   188,   188,   188,   188,   188,   185,
      54,    55,    54,    54,    55,   196,   184,   110,   111,   105,
     105,   105,   171,   105,   105,   187,    87,   110,   110,    54,
     110,   184,    87,   111,   171,   119,   176,   110,   156,   157,
     158,   114,   113,   185,   166,   114,   105,   105,   105,   113,
     174,   111,   134,   131,   114,   145,   114,   114,   114,   114,
     114,   114,   114,   114,   114,   114,   113,   114,   114,   114,
     114,   114,   114,   114,   114,   114,   114,   114,   114,   185,
     189,   158,   115,   185,   159,   106,    85,   115,   111,   155,
      87,    63,    63,   114,   115,   184,   184,     1,    29,   184,
     184,    87,   171,   110,   110,   171,   176,   176,    22,   161,
      62,   168,   114,   196,   196,   196,   148,   111,   111,   144,
     172,   198,   114,   115,   115,   185,   153,    85,   188,    54,
      54,   114,   114,   110,   105,   114,   114,   171,   182,   184,
     182,   114,   114,   114,   146,   115,   153,   171,   171,   184,
     171,   178,   114,   114,   172,    27,   114,   172,   171,   171,
     171,     1,   110
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   116,   117,   117,   118,   118,   118,   118,   118,   119,
     120,   120,   121,   121,   121,   121,   121,   121,   121,   121,
     122,   122,   122,   122,   122,   122,   122,   122,   122,   122,
     122,   122,   122,   123,   123,   125,   126,   124,   127,   124,
     124,   124,   128,   129,   124,   130,   124,   124,   124,   131,
     131,   132,   132,   133,   133,   134,   134,   134,   134,   135,
     135,   136,   136,   136,   136,   136,   136,   136,   138,   137,
     139,   139,   140,   141,   141,   143,   144,   142,   145,   142,
     146,   146,   147,   147,   148,   148,   148,   149,   149,   149,
     150,   150,   151,   151,   152,   152,   153,   153,   153,   153,
     154,   154,   155,   155,   155,   156,   156,   156,   156,   156,
     157,   157,   158,   158,   158,   159,   159,   159,   159,   159,
     160,   160,   160,   160,   160,   160,   160,   160,   160,   160,
     160,   161,   161,   162,   163,   163,   163,   163,   163,   163,
     163,   163,   163,   163,   163,   163,   163,   163,   163,   163,
     163,   163,   163,   163,   163,   163,   163,   163,   163,   163,
     163,   163,   163,   163,   163,   163,   163,   163,   163,   164,
     165,   165,   166,   166,   167,   167,   167,   168,   168,   168,
     170,   169,   171,   171,   171,   171,   171,   171,   171,   171,
     171,   173,   172,   174,   174,   175,   175,   176,   176,   177,
     177,   178,   177,   179,   179,   179,   180,   180,   180,   180,
     180,   180,   180,   181,   182,   182,   183,   183,   183,   183,
     183,   184,   184,   185,   185,   186,   186,   186,   186,   186,
     186,   186,   186,   186,   186,   186,   187,   188,   188,   188,
     188,   188,   188,   188,   188,   188,   188,   188,   188,   188,
     188,   188,   188,   188,   188,   188,   188,   189,   189,   189,
     189,   189,   189,   189,   189,   189,   189,   189,   189,   190,
     190,   191,   191,   192,   192,   192,   192,   192,   192,   192,
     192,   192,   192,   192,   192,   192,   192,   192,   192,   192,
     193,   193,   193,   193,   193,   193,   193,   193,   193,   193,
     193,   194,   194,   194,   194,   194,   194,   194,   194,   194,
     195,   195,   196,   196,   197,   197,   198,   198,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   200,
     200
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     0,     0,     7,     0,     5,
       2,     2,     0,     0,     8,     0,     5,     2,     2,     0,
       1,     0,     2,     1,     3,     2,     2,     1,     1,     1,
       2,     1,     1,     2,     1,     2,     1,     2,     0,     5,
       3,     2,     4,     2,     2,     0,     0,    10,     0,     8,
       0,     2,     1,     3,     4,     4,     4,     1,     1,     1,
       0,     1,     1,     3,     1,     3,     1,     2,     3,     4,
       1,     3,     1,     4,     5,     1,     1,     2,     2,     2,
       2,     1,     1,     2,     1,     3,     2,     3,     3,     4,
       1,     3,     3,     3,     1,     3,     3,     6,     4,     3,
       4,     0,     1,     2,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     2,     2,     0,
       1,     3,     0,     1,     1,     3,     3,     2,     2,     1,
       0,     6,     1,     1,     1,     1,     1,     1,     1,     2,
       2,     0,     4,     0,     1,     1,     2,     1,     2,     5,
       7,     0,     6,     4,     3,     3,     5,     7,     7,     4,
       5,     6,     6,     2,     0,     1,     2,     2,     2,     3,
       3,     1,     3,     1,     3,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     5,     1,     1,     2,     2,
       2,     2,     2,     2,     2,     2,     4,     2,     4,     1,
       2,     2,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     2,     2,     2,     2,
       1,     4,     4,     3,     5,     5,     3,     3,     2,     2,
       1,     4,     4,     4,     4,     4,     4,     4,     4,     4,
       0,     1,     0,     1,     1,     3,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     4,     4,     4,     4,     4,
       4,     4,     4,     4,     4,     4,     4,     3,     3,     1,
       2
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
#line 139 "src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2481 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 143 "src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2491 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 151 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2497 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 152 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2503 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 153 "src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2509 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 154 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2515 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 155 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2521 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 159 "src/parser.y"
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
#line 2554 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 190 "src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          if (yyvsp[0].typeSpec.isExtern) yyval.typeSpec.isExtern = true;
          yyval.typeSpec.storageClasses += yyvsp[0].typeSpec.storageClasses;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isAuto) yyval.typeSpec.isAuto = true;
          if (yyvsp[0].typeSpec.isVirtual) yyval.typeSpec.isVirtual = true;
          if (yyvsp[0].typeSpec.isFriend) yyval.typeSpec.isFriend = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2574 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 205 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2580 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 209 "src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2586 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: EXTERN  */
#line 210 "src/parser.y"
               { yyval.typeSpec.isExtern = true; yyval.typeSpec.storageClasses = 1; }
#line 2592 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: AUTO  */
#line 211 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2598 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: TYPEDEF  */
#line 212 "src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2604 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: CONST  */
#line 213 "src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2610 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: VIRTUAL  */
#line 214 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isVirtual = true; }
#line 2616 "build/parser.tab.cpp"
    break;

  case 18: /* storage_or_type_specifier: FRIEND  */
#line 215 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isFriend = true; }
#line 2622 "build/parser.tab.cpp"
    break;

  case 19: /* storage_or_type_specifier: type_specifier  */
#line 216 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2628 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: INT  */
#line 220 "src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2634 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: CHAR  */
#line 221 "src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2640 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: FLOAT  */
#line 222 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2646 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: DOUBLE  */
#line 223 "src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2652 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: VOID  */
#line 224 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2658 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: BOOL  */
#line 225 "src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2664 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SHORT  */
#line 226 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2670 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: LONG  */
#line 227 "src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2676 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: SIGNED  */
#line 228 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2682 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: UNSIGNED  */
#line 229 "src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2688 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: VA_LIST  */
#line 230 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2694 "build/parser.tab.cpp"
    break;

  case 31: /* type_specifier: TYPE_NAME  */
#line 231 "src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
          if (s && (s->kind == SymKind::STRUCT_TAG || s->kind == SymKind::CLASS_TAG)) {
              yyval.typeSpec.tagName = yyvsp[0].str; /* "Dog d;" -- Dog referenced directly,
                                                without repeating class/struct */
          } else if (s && s->kind == SymKind::TYPEDEF_NAME && s->typeExpr && s->typeExpr->pointerLevel == 0 &&
                     s->typeExpr->arrayDims.empty() && !s->typeExpr->isFunction) {
              yyval.typeSpec.tagName = s->typeExpr->tagName; /* `Pt p;` with `typedef struct {...} Pt;`:
                                                              p.x resolves through the struct */
          }
      }
#line 2713 "build/parser.tab.cpp"
    break;

  case 32: /* type_specifier: struct_or_class_specifier  */
#line 245 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2719 "build/parser.tab.cpp"
    break;

  case 33: /* tag_name: IDENTIFIER  */
#line 252 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2725 "build/parser.tab.cpp"
    break;

  case 34: /* tag_name: TYPE_NAME  */
#line 253 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2731 "build/parser.tab.cpp"
    break;

  case 35: /* $@1: %empty  */
#line 257 "src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2741 "build/parser.tab.cpp"
    break;

  case 36: /* $@2: %empty  */
#line 261 "src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2747 "build/parser.tab.cpp"
    break;

  case 37: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 261 "src/parser.y"
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
#line 2765 "build/parser.tab.cpp"
    break;

  case 38: /* @3: %empty  */
#line 277 "src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2777 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 283 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2790 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 291 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2801 "build/parser.tab.cpp"
    break;

  case 41: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 297 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2812 "build/parser.tab.cpp"
    break;

  case 42: /* $@4: %empty  */
#line 303 "src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2822 "build/parser.tab.cpp"
    break;

  case 43: /* $@5: %empty  */
#line 307 "src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2828 "build/parser.tab.cpp"
    break;

  case 44: /* struct_or_class_specifier: CLASS tag_name $@4 inheritance_opt '{' $@5 member_decl_list_opt '}'  */
#line 307 "src/parser.y"
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
#line 2845 "build/parser.tab.cpp"
    break;

  case 45: /* @6: %empty  */
#line 319 "src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2857 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: CLASS '{' @6 member_decl_list_opt '}'  */
#line 325 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2870 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 333 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2881 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 339 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2892 "build/parser.tab.cpp"
    break;

  case 49: /* member_decl_list_opt: %empty  */
#line 348 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2898 "build/parser.tab.cpp"
    break;

  case 50: /* member_decl_list_opt: member_decl_list  */
#line 349 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2904 "build/parser.tab.cpp"
    break;

  case 51: /* inheritance_opt: %empty  */
#line 353 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2910 "build/parser.tab.cpp"
    break;

  case 52: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 354 "src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 2916 "build/parser.tab.cpp"
    break;

  case 53: /* inheritance_specifier_list: inheritance_specifier  */
#line 358 "src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2922 "build/parser.tab.cpp"
    break;

  case 54: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 359 "src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 2931 "build/parser.tab.cpp"
    break;

  case 55: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 366 "src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2942 "build/parser.tab.cpp"
    break;

  case 56: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 372 "src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2953 "build/parser.tab.cpp"
    break;

  case 57: /* inheritance_specifier: IDENTIFIER  */
#line 378 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2964 "build/parser.tab.cpp"
    break;

  case 58: /* inheritance_specifier: TYPE_NAME  */
#line 384 "src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2975 "build/parser.tab.cpp"
    break;

  case 59: /* member_decl_list: member_item  */
#line 395 "src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 2985 "build/parser.tab.cpp"
    break;

  case 60: /* member_decl_list: member_decl_list member_item  */
#line 400 "src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 2999 "build/parser.tab.cpp"
    break;

  case 61: /* member_item: declaration  */
#line 412 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3005 "build/parser.tab.cpp"
    break;

  case 62: /* member_item: function_definition  */
#line 413 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3011 "build/parser.tab.cpp"
    break;

  case 63: /* member_item: access_specifier ':'  */
#line 414 "src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3017 "build/parser.tab.cpp"
    break;

  case 64: /* member_item: constructor_def  */
#line 415 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3023 "build/parser.tab.cpp"
    break;

  case 65: /* member_item: EXPLICIT constructor_def  */
#line 416 "src/parser.y"
                               {
          yyval.node = yyvsp[0].node;
          if (yyval.node && yyval.node->typeExpr) yyval.node->typeExpr->isExplicit = true;
      }
#line 3032 "build/parser.tab.cpp"
    break;

  case 66: /* member_item: destructor_def  */
#line 420 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3038 "build/parser.tab.cpp"
    break;

  case 67: /* member_item: VIRTUAL destructor_def  */
#line 421 "src/parser.y"
                             {
          yyval.node = yyvsp[0].node;
          if (yyval.node && yyval.node->typeExpr) yyval.node->typeExpr->isVirtual = true;
      }
#line 3047 "build/parser.tab.cpp"
    break;

  case 68: /* $@7: %empty  */
#line 431 "src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3053 "build/parser.tab.cpp"
    break;

  case 69: /* constructor_head: IDENTIFIER '(' $@7 parameter_list_opt ')'  */
#line 431 "src/parser.y"
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
#line 3073 "build/parser.tab.cpp"
    break;

  case 70: /* constructor_def: constructor_head mem_init_opt compound_stmt  */
#line 449 "src/parser.y"
                                                  {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-2].str, yyvsp[-2].idx, yyvsp[-2].paramList, yyvsp[-2].decl.isVariadic, currentClassName(), yyvsp[0].node,
                                        yyvsp[-1].nodeList);
      }
#line 3083 "build/parser.tab.cpp"
    break;

  case 71: /* constructor_def: constructor_head ';'  */
#line 454 "src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3092 "build/parser.tab.cpp"
    break;

  case 72: /* destructor_head: '~' IDENTIFIER '(' ')'  */
#line 461 "src/parser.y"
                             {
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          pushScope(currentClassName() + "::~" + yyvsp[-2].str + "()");
          yyval = yyvsp[-2];
      }
#line 3102 "build/parser.tab.cpp"
    break;

  case 73: /* destructor_def: destructor_head compound_stmt  */
#line 469 "src/parser.y"
                                    {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), yyvsp[0].node);
      }
#line 3111 "build/parser.tab.cpp"
    break;

  case 74: /* destructor_def: destructor_head ';'  */
#line 473 "src/parser.y"
                          {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), nullptr);
      }
#line 3120 "build/parser.tab.cpp"
    break;

  case 75: /* $@8: %empty  */
#line 481 "src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3130 "build/parser.tab.cpp"
    break;

  case 76: /* $@9: %empty  */
#line 485 "src/parser.y"
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
#line 3147 "build/parser.tab.cpp"
    break;

  case 77: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@8 parameter_list_opt ')' $@9 mem_init_opt compound_stmt  */
#line 496 "src/parser.y"
                                   {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-7].str, yyvsp[-7].idx, yyvsp[-4].paramList, yyvsp[-4].decl.isVariadic, yyvsp[-9].str, yyvsp[0].node, yyvsp[-1].nodeList);
          leaveClass();
      }
#line 3157 "build/parser.tab.cpp"
    break;

  case 78: /* $@10: %empty  */
#line 501 "src/parser.y"
                                                {
          setCategory(yyvsp[-5].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-5].str)));
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          enterClass(yyvsp[-5].str);
          pushScope(yyvsp[-5].str + "::~" + yyvsp[-2].str + "()");
      }
#line 3168 "build/parser.tab.cpp"
    break;

  case 79: /* out_of_class_special: TYPE_NAME SCOPE_RES '~' TYPE_NAME '(' ')' $@10 compound_stmt  */
#line 506 "src/parser.y"
                      {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-4].str, yyvsp[-4].idx, yyvsp[-7].str, yyvsp[0].node);
          leaveClass();
      }
#line 3178 "build/parser.tab.cpp"
    break;

  case 80: /* mem_init_opt: %empty  */
#line 517 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3184 "build/parser.tab.cpp"
    break;

  case 81: /* mem_init_opt: ':' mem_initializer_list  */
#line 518 "src/parser.y"
                               { yyval = yyvsp[0]; }
#line 3190 "build/parser.tab.cpp"
    break;

  case 82: /* mem_initializer_list: mem_initializer  */
#line 522 "src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3196 "build/parser.tab.cpp"
    break;

  case 83: /* mem_initializer_list: mem_initializer_list ',' mem_initializer  */
#line 523 "src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3202 "build/parser.tab.cpp"
    break;

  case 84: /* mem_initializer: IDENTIFIER '(' argument_list_opt ')'  */
#line 527 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::MemInit, yyvsp[-3].str), yyvsp[-3].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(yyval.node, a);
      }
#line 3211 "build/parser.tab.cpp"
    break;

  case 85: /* mem_initializer: TYPE_NAME '(' argument_list_opt ')'  */
#line 531 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::MemInit, yyvsp[-3].str), yyvsp[-3].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(yyval.node, a);
      }
#line 3220 "build/parser.tab.cpp"
    break;

  case 86: /* mem_initializer: FCAST '(' argument_list_opt ')'  */
#line 535 "src/parser.y"
                                      {
          yyval.node = atToken(mkNode(ASTKind::MemInit, yyvsp[-3].str), yyvsp[-3].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(yyval.node, a);
      }
#line 3229 "build/parser.tab.cpp"
    break;

  case 90: /* init_declarator_list_opt: %empty  */
#line 548 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3235 "build/parser.tab.cpp"
    break;

  case 91: /* init_declarator_list_opt: init_declarator_list  */
#line 549 "src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3241 "build/parser.tab.cpp"
    break;

  case 92: /* init_declarator_list: init_declarator  */
#line 553 "src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3247 "build/parser.tab.cpp"
    break;

  case 93: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 554 "src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3253 "build/parser.tab.cpp"
    break;

  case 94: /* init_declarator: declarator  */
#line 558 "src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3259 "build/parser.tab.cpp"
    break;

  case 95: /* init_declarator: declarator '=' initializer  */
#line 559 "src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3265 "build/parser.tab.cpp"
    break;

  case 96: /* initializer: assignment_expr  */
#line 563 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3271 "build/parser.tab.cpp"
    break;

  case 97: /* initializer: '{' '}'  */
#line 564 "src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3277 "build/parser.tab.cpp"
    break;

  case 98: /* initializer: '{' initializer_list '}'  */
#line 565 "src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3287 "build/parser.tab.cpp"
    break;

  case 99: /* initializer: '{' initializer_list ',' '}'  */
#line 570 "src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3297 "build/parser.tab.cpp"
    break;

  case 100: /* initializer_list: initializer_item  */
#line 578 "src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3303 "build/parser.tab.cpp"
    break;

  case 101: /* initializer_list: initializer_list ',' initializer_item  */
#line 579 "src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3309 "build/parser.tab.cpp"
    break;

  case 102: /* initializer_item: initializer  */
#line 583 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3315 "build/parser.tab.cpp"
    break;

  case 103: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 584 "src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3323 "build/parser.tab.cpp"
    break;

  case 104: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 587 "src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3331 "build/parser.tab.cpp"
    break;

  case 105: /* pointer: '*'  */
#line 593 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3337 "build/parser.tab.cpp"
    break;

  case 106: /* pointer: '&'  */
#line 594 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3343 "build/parser.tab.cpp"
    break;

  case 107: /* pointer: pointer '*'  */
#line 595 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3349 "build/parser.tab.cpp"
    break;

  case 108: /* pointer: pointer '&'  */
#line 596 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3355 "build/parser.tab.cpp"
    break;

  case 109: /* pointer: pointer CONST  */
#line 597 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3361 "build/parser.tab.cpp"
    break;

  case 110: /* declarator: pointer direct_declarator  */
#line 601 "src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3372 "build/parser.tab.cpp"
    break;

  case 111: /* declarator: direct_declarator  */
#line 607 "src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3378 "build/parser.tab.cpp"
    break;

  case 112: /* abstract_declarator: pointer  */
#line 613 "src/parser.y"
              { yyval = yyvsp[0]; }
#line 3384 "build/parser.tab.cpp"
    break;

  case 113: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 614 "src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3395 "build/parser.tab.cpp"
    break;

  case 114: /* abstract_declarator: direct_abstract_declarator  */
#line 620 "src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3401 "build/parser.tab.cpp"
    break;

  case 115: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 624 "src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3415 "build/parser.tab.cpp"
    break;

  case 116: /* direct_abstract_declarator: '[' ']'  */
#line 633 "src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3421 "build/parser.tab.cpp"
    break;

  case 117: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 634 "src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3427 "build/parser.tab.cpp"
    break;

  case 118: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 635 "src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3433 "build/parser.tab.cpp"
    break;

  case 119: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 636 "src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3439 "build/parser.tab.cpp"
    break;

  case 120: /* direct_declarator: IDENTIFIER  */
#line 640 "src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3448 "build/parser.tab.cpp"
    break;

  case 121: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 644 "src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3460 "build/parser.tab.cpp"
    break;

  case 122: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 651 "src/parser.y"
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
#line 3477 "build/parser.tab.cpp"
    break;

  case 123: /* direct_declarator: '(' declarator ')'  */
#line 663 "src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3491 "build/parser.tab.cpp"
    break;

  case 124: /* direct_declarator: operator_function_id  */
#line 672 "src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3500 "build/parser.tab.cpp"
    break;

  case 125: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 676 "src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3512 "build/parser.tab.cpp"
    break;

  case 126: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 683 "src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3524 "build/parser.tab.cpp"
    break;

  case 127: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')' method_cv_opt  */
#line 690 "src/parser.y"
                                                                             {
          yyval = yyvsp[-5];
          yyval.decl.isConstMethod = yyvsp[0].decl.isConstMethod;
          if (yyvsp[-5].decl.wasParenGrouped && yyvsp[-5].decl.pointerLevel > 0) {
              /* `int (*fp)(int)` would declare a pointer to a function;
                 the language has no function pointers, so a parameter
                 list cannot follow a parenthesized pointer declarator */
              popScope();
              yyerror("syntax error, unexpected '(' after a parenthesized pointer declarator");
              YYERROR;
          }
          yyval.decl.isFunction = true;
          yyval.decl.wasParenGrouped = false; /* consumed */
          yyval.decl.params = yyvsp[-2].paramList;
          yyval.decl.isVariadic = yyvsp[-2].decl.isVariadic;
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
#line 3549 "build/parser.tab.cpp"
    break;

  case 128: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 710 "src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3561 "build/parser.tab.cpp"
    break;

  case 129: /* direct_declarator: direct_declarator '[' ']'  */
#line 717 "src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3567 "build/parser.tab.cpp"
    break;

  case 130: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 718 "src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3573 "build/parser.tab.cpp"
    break;

  case 131: /* method_cv_opt: %empty  */
#line 723 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3579 "build/parser.tab.cpp"
    break;

  case 132: /* method_cv_opt: CONST  */
#line 724 "src/parser.y"
            { yyval = ParserValue(); yyval.decl.isConstMethod = true; }
#line 3585 "build/parser.tab.cpp"
    break;

  case 133: /* operator_function_id: OPERATOR overloadable_operator  */
#line 729 "src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3591 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: '+'  */
#line 733 "src/parser.y"
          { yyval.str = "+"; }
#line 3597 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: '-'  */
#line 733 "src/parser.y"
                                  { yyval.str = "-"; }
#line 3603 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: '*'  */
#line 733 "src/parser.y"
                                                          { yyval.str = "*"; }
#line 3609 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: '/'  */
#line 733 "src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3615 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: '%'  */
#line 734 "src/parser.y"
          { yyval.str = "%"; }
#line 3621 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: '^'  */
#line 734 "src/parser.y"
                                  { yyval.str = "^"; }
#line 3627 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: '&'  */
#line 734 "src/parser.y"
                                                          { yyval.str = "&"; }
#line 3633 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: '|'  */
#line 734 "src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3639 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: '~'  */
#line 735 "src/parser.y"
          { yyval.str = "~"; }
#line 3645 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: '!'  */
#line 735 "src/parser.y"
                                  { yyval.str = "!"; }
#line 3651 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: '='  */
#line 735 "src/parser.y"
                                                          { yyval.str = "="; }
#line 3657 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: '<'  */
#line 735 "src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3663 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: '>'  */
#line 736 "src/parser.y"
          { yyval.str = ">"; }
#line 3669 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: EQ_OP  */
#line 736 "src/parser.y"
                                    { yyval.str = "=="; }
#line 3675 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: NE_OP  */
#line 736 "src/parser.y"
                                                               { yyval.str = "!="; }
#line 3681 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: LE_OP  */
#line 736 "src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3687 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: GE_OP  */
#line 737 "src/parser.y"
            { yyval.str = ">="; }
#line 3693 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: AND_OP  */
#line 737 "src/parser.y"
                                        { yyval.str = "&&"; }
#line 3699 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: OR_OP  */
#line 737 "src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3705 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: SHL  */
#line 737 "src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3711 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: SHR  */
#line 738 "src/parser.y"
          { yyval.str = ">>"; }
#line 3717 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: INC  */
#line 738 "src/parser.y"
                                   { yyval.str = "++"; }
#line 3723 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: DEC  */
#line 738 "src/parser.y"
                                                            { yyval.str = "--"; }
#line 3729 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: PLUS_ASSIGN  */
#line 739 "src/parser.y"
                  { yyval.str = "+="; }
#line 3735 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: MINUS_ASSIGN  */
#line 739 "src/parser.y"
                                                    { yyval.str = "-="; }
#line 3741 "build/parser.tab.cpp"
    break;

  case 159: /* overloadable_operator: MUL_ASSIGN  */
#line 739 "src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3747 "build/parser.tab.cpp"
    break;

  case 160: /* overloadable_operator: DIV_ASSIGN  */
#line 740 "src/parser.y"
                 { yyval.str = "/="; }
#line 3753 "build/parser.tab.cpp"
    break;

  case 161: /* overloadable_operator: MOD_ASSIGN  */
#line 740 "src/parser.y"
                                                 { yyval.str = "%="; }
#line 3759 "build/parser.tab.cpp"
    break;

  case 162: /* overloadable_operator: AND_ASSIGN  */
#line 740 "src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3765 "build/parser.tab.cpp"
    break;

  case 163: /* overloadable_operator: OR_ASSIGN  */
#line 741 "src/parser.y"
                { yyval.str = "|="; }
#line 3771 "build/parser.tab.cpp"
    break;

  case 164: /* overloadable_operator: XOR_ASSIGN  */
#line 741 "src/parser.y"
                                                { yyval.str = "^="; }
#line 3777 "build/parser.tab.cpp"
    break;

  case 165: /* overloadable_operator: SHL_ASSIGN  */
#line 741 "src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3783 "build/parser.tab.cpp"
    break;

  case 166: /* overloadable_operator: SHR_ASSIGN  */
#line 742 "src/parser.y"
                 { yyval.str = ">>="; }
#line 3789 "build/parser.tab.cpp"
    break;

  case 167: /* overloadable_operator: '[' ']'  */
#line 742 "src/parser.y"
                                               { yyval.str = "[]"; }
#line 3795 "build/parser.tab.cpp"
    break;

  case 168: /* overloadable_operator: '(' ')'  */
#line 742 "src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3801 "build/parser.tab.cpp"
    break;

  case 169: /* param_scope: %empty  */
#line 749 "src/parser.y"
                                           { pushScope(); }
#line 3807 "build/parser.tab.cpp"
    break;

  case 170: /* constructor_args: assignment_expr  */
#line 753 "src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3813 "build/parser.tab.cpp"
    break;

  case 171: /* constructor_args: constructor_args ',' assignment_expr  */
#line 754 "src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3819 "build/parser.tab.cpp"
    break;

  case 172: /* parameter_list_opt: %empty  */
#line 758 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3825 "build/parser.tab.cpp"
    break;

  case 173: /* parameter_list_opt: parameter_list  */
#line 759 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3831 "build/parser.tab.cpp"
    break;

  case 174: /* parameter_list: parameter_decl  */
#line 763 "src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3840 "build/parser.tab.cpp"
    break;

  case 175: /* parameter_list: parameter_list ',' parameter_decl  */
#line 767 "src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3849 "build/parser.tab.cpp"
    break;

  case 176: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 771 "src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3855 "build/parser.tab.cpp"
    break;

  case 177: /* parameter_decl: declaration_specifiers declarator  */
#line 775 "src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3865 "build/parser.tab.cpp"
    break;

  case 178: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 780 "src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3875 "build/parser.tab.cpp"
    break;

  case 179: /* parameter_decl: declaration_specifiers  */
#line 785 "src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3885 "build/parser.tab.cpp"
    break;

  case 180: /* $@11: %empty  */
#line 793 "src/parser.y"
                                        {
          bool outOfClass = !yyvsp[0].decl.className.empty();
          if (outOfClass) enterClass(yyvsp[0].decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[0].decl.params) paramTypes.push_back(p.typeStr);
          std::string owner = yyvsp[-1].typeSpec.isFriend ? "" : currentClassName(); /* a friend is not a member */
          std::string mangled = mangle(yyvsp[0].decl.name, paramExprs(yyvsp[0].decl.params), yyvsp[0].decl.isVariadic, owner, yyvsp[0].decl.isConstMethod);
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
#line 3927 "build/parser.tab.cpp"
    break;

  case 181: /* function_definition: declaration_specifiers declarator $@11 '{' block_item_list_opt '}'  */
#line 829 "src/parser.y"
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
                                       yyvsp[-5].typeSpec.isFriend ? "" : currentClassName(), yyvsp[-4].decl.isConstMethod);
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
#line 3958 "build/parser.tab.cpp"
    break;

  case 182: /* statement: compound_stmt  */
#line 858 "src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3964 "build/parser.tab.cpp"
    break;

  case 183: /* statement: expr_stmt  */
#line 859 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3970 "build/parser.tab.cpp"
    break;

  case 184: /* statement: selection_stmt  */
#line 860 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3976 "build/parser.tab.cpp"
    break;

  case 185: /* statement: iteration_stmt  */
#line 861 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3982 "build/parser.tab.cpp"
    break;

  case 186: /* statement: jump_stmt  */
#line 862 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3988 "build/parser.tab.cpp"
    break;

  case 187: /* statement: labeled_stmt  */
#line 863 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3994 "build/parser.tab.cpp"
    break;

  case 188: /* statement: declaration  */
#line 864 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4000 "build/parser.tab.cpp"
    break;

  case 189: /* statement: error ';'  */
#line 865 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4006 "build/parser.tab.cpp"
    break;

  case 190: /* statement: error '}'  */
#line 866 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4012 "build/parser.tab.cpp"
    break;

  case 191: /* $@12: %empty  */
#line 870 "src/parser.y"
          { pushScope(); }
#line 4018 "build/parser.tab.cpp"
    break;

  case 192: /* compound_stmt: '{' $@12 block_item_list_opt '}'  */
#line 870 "src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 4029 "build/parser.tab.cpp"
    break;

  case 193: /* block_item_list_opt: %empty  */
#line 879 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4035 "build/parser.tab.cpp"
    break;

  case 194: /* block_item_list_opt: block_item_list  */
#line 880 "src/parser.y"
                      { yyval = yyvsp[0]; }
#line 4041 "build/parser.tab.cpp"
    break;

  case 195: /* block_item_list: statement  */
#line 884 "src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4047 "build/parser.tab.cpp"
    break;

  case 196: /* block_item_list: block_item_list statement  */
#line 885 "src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4053 "build/parser.tab.cpp"
    break;

  case 197: /* expr_stmt: ';'  */
#line 889 "src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 4059 "build/parser.tab.cpp"
    break;

  case 198: /* expr_stmt: expr ';'  */
#line 890 "src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 4065 "build/parser.tab.cpp"
    break;

  case 199: /* selection_stmt: IF '(' expr ')' statement  */
#line 894 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4073 "build/parser.tab.cpp"
    break;

  case 200: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 897 "src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 4081 "build/parser.tab.cpp"
    break;

  case 201: /* $@13: %empty  */
#line 900 "src/parser.y"
                          { hintScope("switch"); }
#line 4087 "build/parser.tab.cpp"
    break;

  case 202: /* selection_stmt: SWITCH '(' expr ')' $@13 compound_stmt  */
#line 900 "src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4095 "build/parser.tab.cpp"
    break;

  case 203: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 906 "src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4103 "build/parser.tab.cpp"
    break;

  case 204: /* labeled_stmt: DEFAULT ':' statement  */
#line 909 "src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4111 "build/parser.tab.cpp"
    break;

  case 205: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 912 "src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4121 "build/parser.tab.cpp"
    break;

  case 206: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 920 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4129 "build/parser.tab.cpp"
    break;

  case 207: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 923 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4137 "build/parser.tab.cpp"
    break;

  case 208: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 930 "src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4146 "build/parser.tab.cpp"
    break;

  case 209: /* iteration_stmt: DO statement error ';'  */
#line 934 "src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4155 "build/parser.tab.cpp"
    break;

  case 210: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 938 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4163 "build/parser.tab.cpp"
    break;

  case 211: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 941 "src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4172 "build/parser.tab.cpp"
    break;

  case 212: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 945 "src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4181 "build/parser.tab.cpp"
    break;

  case 213: /* for_open: FOR '('  */
#line 954 "src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4187 "build/parser.tab.cpp"
    break;

  case 214: /* for_incr_opt: %empty  */
#line 958 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4193 "build/parser.tab.cpp"
    break;

  case 215: /* for_incr_opt: expr  */
#line 959 "src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4199 "build/parser.tab.cpp"
    break;

  case 216: /* jump_stmt: BREAK ';'  */
#line 963 "src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4205 "build/parser.tab.cpp"
    break;

  case 217: /* jump_stmt: CONTINUE ';'  */
#line 964 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4211 "build/parser.tab.cpp"
    break;

  case 218: /* jump_stmt: RETURN ';'  */
#line 965 "src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4217 "build/parser.tab.cpp"
    break;

  case 219: /* jump_stmt: RETURN expr ';'  */
#line 966 "src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4223 "build/parser.tab.cpp"
    break;

  case 220: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 967 "src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4235 "build/parser.tab.cpp"
    break;

  case 221: /* expr: assignment_expr  */
#line 977 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4241 "build/parser.tab.cpp"
    break;

  case 222: /* expr: expr ',' assignment_expr  */
#line 978 "src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4247 "build/parser.tab.cpp"
    break;

  case 223: /* assignment_expr: binary_expr  */
#line 982 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4253 "build/parser.tab.cpp"
    break;

  case 224: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 983 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4261 "build/parser.tab.cpp"
    break;

  case 225: /* assign_op: '='  */
#line 989 "src/parser.y"
                   { yyval.str = "="; }
#line 4267 "build/parser.tab.cpp"
    break;

  case 226: /* assign_op: PLUS_ASSIGN  */
#line 990 "src/parser.y"
                   { yyval.str = "+="; }
#line 4273 "build/parser.tab.cpp"
    break;

  case 227: /* assign_op: MINUS_ASSIGN  */
#line 991 "src/parser.y"
                   { yyval.str = "-="; }
#line 4279 "build/parser.tab.cpp"
    break;

  case 228: /* assign_op: MUL_ASSIGN  */
#line 992 "src/parser.y"
                   { yyval.str = "*="; }
#line 4285 "build/parser.tab.cpp"
    break;

  case 229: /* assign_op: DIV_ASSIGN  */
#line 993 "src/parser.y"
                   { yyval.str = "/="; }
#line 4291 "build/parser.tab.cpp"
    break;

  case 230: /* assign_op: MOD_ASSIGN  */
#line 994 "src/parser.y"
                   { yyval.str = "%="; }
#line 4297 "build/parser.tab.cpp"
    break;

  case 231: /* assign_op: AND_ASSIGN  */
#line 995 "src/parser.y"
                   { yyval.str = "&="; }
#line 4303 "build/parser.tab.cpp"
    break;

  case 232: /* assign_op: OR_ASSIGN  */
#line 996 "src/parser.y"
                   { yyval.str = "|="; }
#line 4309 "build/parser.tab.cpp"
    break;

  case 233: /* assign_op: XOR_ASSIGN  */
#line 997 "src/parser.y"
                   { yyval.str = "^="; }
#line 4315 "build/parser.tab.cpp"
    break;

  case 234: /* assign_op: SHL_ASSIGN  */
#line 998 "src/parser.y"
                   { yyval.str = "<<="; }
#line 4321 "build/parser.tab.cpp"
    break;

  case 235: /* assign_op: SHR_ASSIGN  */
#line 999 "src/parser.y"
                   { yyval.str = ">>="; }
#line 4327 "build/parser.tab.cpp"
    break;

  case 236: /* constant_expr: binary_expr  */
#line 1003 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4333 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 1007 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4339 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 1008 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4345 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr '|' binary_expr  */
#line 1009 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4351 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr '^' binary_expr  */
#line 1010 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4357 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr '&' binary_expr  */
#line 1011 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4363 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 1012 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4369 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 1013 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4375 "build/parser.tab.cpp"
    break;

  case 244: /* binary_expr: binary_expr '<' binary_expr  */
#line 1014 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4381 "build/parser.tab.cpp"
    break;

  case 245: /* binary_expr: binary_expr '>' binary_expr  */
#line 1015 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4387 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 1016 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4393 "build/parser.tab.cpp"
    break;

  case 247: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 1017 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4399 "build/parser.tab.cpp"
    break;

  case 248: /* binary_expr: binary_expr SHL binary_expr  */
#line 1018 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4405 "build/parser.tab.cpp"
    break;

  case 249: /* binary_expr: binary_expr SHR binary_expr  */
#line 1019 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4411 "build/parser.tab.cpp"
    break;

  case 250: /* binary_expr: binary_expr '+' binary_expr  */
#line 1020 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4417 "build/parser.tab.cpp"
    break;

  case 251: /* binary_expr: binary_expr '-' binary_expr  */
#line 1021 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4423 "build/parser.tab.cpp"
    break;

  case 252: /* binary_expr: binary_expr '*' binary_expr  */
#line 1022 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4429 "build/parser.tab.cpp"
    break;

  case 253: /* binary_expr: binary_expr '/' binary_expr  */
#line 1023 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4435 "build/parser.tab.cpp"
    break;

  case 254: /* binary_expr: binary_expr '%' binary_expr  */
#line 1024 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4441 "build/parser.tab.cpp"
    break;

  case 255: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 1025 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4449 "build/parser.tab.cpp"
    break;

  case 256: /* binary_expr: unary_expr  */
#line 1028 "src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4455 "build/parser.tab.cpp"
    break;

  case 257: /* unary_expr: postfix_expr  */
#line 1032 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4461 "build/parser.tab.cpp"
    break;

  case 258: /* unary_expr: INC unary_expr  */
#line 1033 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4467 "build/parser.tab.cpp"
    break;

  case 259: /* unary_expr: DEC unary_expr  */
#line 1034 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4473 "build/parser.tab.cpp"
    break;

  case 260: /* unary_expr: '&' unary_expr  */
#line 1035 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4479 "build/parser.tab.cpp"
    break;

  case 261: /* unary_expr: '*' unary_expr  */
#line 1036 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4485 "build/parser.tab.cpp"
    break;

  case 262: /* unary_expr: '+' unary_expr  */
#line 1037 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4491 "build/parser.tab.cpp"
    break;

  case 263: /* unary_expr: '-' unary_expr  */
#line 1038 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4497 "build/parser.tab.cpp"
    break;

  case 264: /* unary_expr: '!' unary_expr  */
#line 1039 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4503 "build/parser.tab.cpp"
    break;

  case 265: /* unary_expr: '~' unary_expr  */
#line 1040 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4509 "build/parser.tab.cpp"
    break;

  case 266: /* unary_expr: '(' type_name ')' unary_expr  */
#line 1041 "src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4518 "build/parser.tab.cpp"
    break;

  case 267: /* unary_expr: SIZEOF unary_expr  */
#line 1045 "src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4524 "build/parser.tab.cpp"
    break;

  case 268: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 1046 "src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4533 "build/parser.tab.cpp"
    break;

  case 269: /* type_name: type_name_specifiers  */
#line 1053 "src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4542 "build/parser.tab.cpp"
    break;

  case 270: /* type_name: type_name_specifiers abstract_declarator  */
#line 1057 "src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4551 "build/parser.tab.cpp"
    break;

  case 271: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1064 "src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4563 "build/parser.tab.cpp"
    break;

  case 272: /* type_name_specifiers: type_name_specifier  */
#line 1071 "src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4569 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifier: INT  */
#line 1075 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4575 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifier: CHAR  */
#line 1076 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4581 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: FLOAT  */
#line 1077 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4587 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: DOUBLE  */
#line 1078 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4593 "build/parser.tab.cpp"
    break;

  case 277: /* type_name_specifier: VOID  */
#line 1079 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4599 "build/parser.tab.cpp"
    break;

  case 278: /* type_name_specifier: BOOL  */
#line 1080 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4605 "build/parser.tab.cpp"
    break;

  case 279: /* type_name_specifier: SHORT  */
#line 1081 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4611 "build/parser.tab.cpp"
    break;

  case 280: /* type_name_specifier: LONG  */
#line 1082 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4617 "build/parser.tab.cpp"
    break;

  case 281: /* type_name_specifier: SIGNED  */
#line 1083 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4623 "build/parser.tab.cpp"
    break;

  case 282: /* type_name_specifier: UNSIGNED  */
#line 1084 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4629 "build/parser.tab.cpp"
    break;

  case 283: /* type_name_specifier: VA_LIST  */
#line 1085 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4635 "build/parser.tab.cpp"
    break;

  case 284: /* type_name_specifier: CONST  */
#line 1086 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4641 "build/parser.tab.cpp"
    break;

  case 285: /* type_name_specifier: TYPE_NAME  */
#line 1087 "src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4655 "build/parser.tab.cpp"
    break;

  case 286: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1096 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4666 "build/parser.tab.cpp"
    break;

  case 287: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1102 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4677 "build/parser.tab.cpp"
    break;

  case 288: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1108 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4688 "build/parser.tab.cpp"
    break;

  case 289: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1114 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4699 "build/parser.tab.cpp"
    break;

  case 290: /* postfix_expr: primary_expr  */
#line 1123 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4705 "build/parser.tab.cpp"
    break;

  case 291: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1124 "src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4711 "build/parser.tab.cpp"
    break;

  case 292: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1125 "src/parser.y"
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
#line 4751 "build/parser.tab.cpp"
    break;

  case 293: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1160 "src/parser.y"
                                  {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4760 "build/parser.tab.cpp"
    break;

  case 294: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1164 "src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4773 "build/parser.tab.cpp"
    break;

  case 295: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1172 "src/parser.y"
                                                        {
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4784 "build/parser.tab.cpp"
    break;

  case 296: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1178 "src/parser.y"
                                    {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4793 "build/parser.tab.cpp"
    break;

  case 297: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1182 "src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4799 "build/parser.tab.cpp"
    break;

  case 298: /* postfix_expr: postfix_expr INC  */
#line 1183 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4805 "build/parser.tab.cpp"
    break;

  case 299: /* postfix_expr: postfix_expr DEC  */
#line 1184 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4811 "build/parser.tab.cpp"
    break;

  case 300: /* postfix_expr: builtin_call  */
#line 1185 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4817 "build/parser.tab.cpp"
    break;

  case 301: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1189 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4823 "build/parser.tab.cpp"
    break;

  case 302: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1190 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4829 "build/parser.tab.cpp"
    break;

  case 303: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1191 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4835 "build/parser.tab.cpp"
    break;

  case 304: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1192 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4841 "build/parser.tab.cpp"
    break;

  case 305: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1193 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4847 "build/parser.tab.cpp"
    break;

  case 306: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1194 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4853 "build/parser.tab.cpp"
    break;

  case 307: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1195 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4859 "build/parser.tab.cpp"
    break;

  case 308: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1196 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4865 "build/parser.tab.cpp"
    break;

  case 309: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1197 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4871 "build/parser.tab.cpp"
    break;

  case 310: /* constructor_args_opt: %empty  */
#line 1201 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4877 "build/parser.tab.cpp"
    break;

  case 311: /* constructor_args_opt: constructor_args  */
#line 1202 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4883 "build/parser.tab.cpp"
    break;

  case 312: /* argument_list_opt: %empty  */
#line 1206 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4889 "build/parser.tab.cpp"
    break;

  case 313: /* argument_list_opt: argument_list  */
#line 1207 "src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4895 "build/parser.tab.cpp"
    break;

  case 314: /* argument_list: argument  */
#line 1211 "src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4901 "build/parser.tab.cpp"
    break;

  case 315: /* argument_list: argument_list ',' argument  */
#line 1212 "src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4907 "build/parser.tab.cpp"
    break;

  case 316: /* argument: assignment_expr  */
#line 1216 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4913 "build/parser.tab.cpp"
    break;

  case 317: /* argument: type_name  */
#line 1217 "src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4922 "build/parser.tab.cpp"
    break;

  case 318: /* primary_expr: IDENTIFIER  */
#line 1224 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 4936 "build/parser.tab.cpp"
    break;

  case 319: /* primary_expr: INT_LITERAL  */
#line 1233 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4942 "build/parser.tab.cpp"
    break;

  case 320: /* primary_expr: FLOAT_LITERAL  */
#line 1234 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4948 "build/parser.tab.cpp"
    break;

  case 321: /* primary_expr: CHAR_LITERAL  */
#line 1235 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4954 "build/parser.tab.cpp"
    break;

  case 322: /* primary_expr: string_literal  */
#line 1236 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4960 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: BOOL_LITERAL  */
#line 1237 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4966 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: THIS  */
#line 1238 "src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 4972 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1239 "src/parser.y"
                                             {
          /* `Dog(4)`: a temporary object (for a scalar type, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4981 "build/parser.tab.cpp"
    break;

  case 326: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1243 "src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4991 "build/parser.tab.cpp"
    break;

  case 327: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1250 "src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4997 "build/parser.tab.cpp"
    break;

  case 328: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1251 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5003 "build/parser.tab.cpp"
    break;

  case 329: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1252 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5009 "build/parser.tab.cpp"
    break;

  case 330: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1253 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5015 "build/parser.tab.cpp"
    break;

  case 331: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1254 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5021 "build/parser.tab.cpp"
    break;

  case 332: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1255 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5027 "build/parser.tab.cpp"
    break;

  case 333: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1256 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5033 "build/parser.tab.cpp"
    break;

  case 334: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1257 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5039 "build/parser.tab.cpp"
    break;

  case 335: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1258 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5045 "build/parser.tab.cpp"
    break;

  case 336: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1259 "src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5051 "build/parser.tab.cpp"
    break;

  case 337: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1260 "src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 5063 "build/parser.tab.cpp"
    break;

  case 338: /* primary_expr: '(' expr ')'  */
#line 1267 "src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 5069 "build/parser.tab.cpp"
    break;

  case 339: /* string_literal: STRING_LITERAL  */
#line 1272 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5075 "build/parser.tab.cpp"
    break;

  case 340: /* string_literal: string_literal STRING_LITERAL  */
#line 1273 "src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 5085 "build/parser.tab.cpp"
    break;


#line 5089 "build/parser.tab.cpp"

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

#line 1280 "src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
