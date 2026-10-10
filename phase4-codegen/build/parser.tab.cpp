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
  YYSYMBOL_IF = 23,                        /* IF  */
  YYSYMBOL_ELSE = 24,                      /* ELSE  */
  YYSYMBOL_FOR = 25,                       /* FOR  */
  YYSYMBOL_WHILE = 26,                     /* WHILE  */
  YYSYMBOL_DO = 27,                        /* DO  */
  YYSYMBOL_UNTIL = 28,                     /* UNTIL  */
  YYSYMBOL_SWITCH = 29,                    /* SWITCH  */
  YYSYMBOL_CASE = 30,                      /* CASE  */
  YYSYMBOL_DEFAULT = 31,                   /* DEFAULT  */
  YYSYMBOL_BREAK = 32,                     /* BREAK  */
  YYSYMBOL_CONTINUE = 33,                  /* CONTINUE  */
  YYSYMBOL_GOTO = 34,                      /* GOTO  */
  YYSYMBOL_RETURN = 35,                    /* RETURN  */
  YYSYMBOL_PRINTF = 36,                    /* PRINTF  */
  YYSYMBOL_SCANF = 37,                     /* SCANF  */
  YYSYMBOL_MALLOC = 38,                    /* MALLOC  */
  YYSYMBOL_FREE = 39,                      /* FREE  */
  YYSYMBOL_CALLOC = 40,                    /* CALLOC  */
  YYSYMBOL_REALLOC = 41,                   /* REALLOC  */
  YYSYMBOL_BOOL = 42,                      /* BOOL  */
  YYSYMBOL_SIZEOF = 43,                    /* SIZEOF  */
  YYSYMBOL_VA_LIST = 44,                   /* VA_LIST  */
  YYSYMBOL_VA_START = 45,                  /* VA_START  */
  YYSYMBOL_VA_ARG = 46,                    /* VA_ARG  */
  YYSYMBOL_VA_END = 47,                    /* VA_END  */
  YYSYMBOL_OPERATOR = 48,                  /* OPERATOR  */
  YYSYMBOL_FCAST = 49,                     /* FCAST  */
  YYSYMBOL_ABSTRACT_LPAREN = 50,           /* ABSTRACT_LPAREN  */
  YYSYMBOL_IDENTIFIER = 51,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 52,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 53,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 54,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 55,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 56,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 57,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 58,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 59,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 60,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 61,                       /* INC  */
  YYSYMBOL_DEC = 62,                       /* DEC  */
  YYSYMBOL_SHL = 63,                       /* SHL  */
  YYSYMBOL_SHR = 64,                       /* SHR  */
  YYSYMBOL_LE_OP = 65,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 66,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 67,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 68,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 69,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 70,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 71,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 72,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 73,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 74,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 75,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 76,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 77,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 78,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 79,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 80,                /* SHR_ASSIGN  */
  YYSYMBOL_PREFER_EXPRESSION = 81,         /* PREFER_EXPRESSION  */
  YYSYMBOL_82_ = 82,                       /* '='  */
  YYSYMBOL_83_ = 83,                       /* '?'  */
  YYSYMBOL_84_ = 84,                       /* ':'  */
  YYSYMBOL_85_ = 85,                       /* '|'  */
  YYSYMBOL_86_ = 86,                       /* '^'  */
  YYSYMBOL_87_ = 87,                       /* '&'  */
  YYSYMBOL_88_ = 88,                       /* '<'  */
  YYSYMBOL_89_ = 89,                       /* '>'  */
  YYSYMBOL_90_ = 90,                       /* '+'  */
  YYSYMBOL_91_ = 91,                       /* '-'  */
  YYSYMBOL_92_ = 92,                       /* '*'  */
  YYSYMBOL_93_ = 93,                       /* '/'  */
  YYSYMBOL_94_ = 94,                       /* '%'  */
  YYSYMBOL_UMINUS = 95,                    /* UMINUS  */
  YYSYMBOL_ADDR = 96,                      /* ADDR  */
  YYSYMBOL_DEREF = 97,                     /* DEREF  */
  YYSYMBOL_CAST = 98,                      /* CAST  */
  YYSYMBOL_99_ = 99,                       /* '!'  */
  YYSYMBOL_100_ = 100,                     /* '~'  */
  YYSYMBOL_101_ = 101,                     /* '.'  */
  YYSYMBOL_102_ = 102,                     /* '('  */
  YYSYMBOL_103_ = 103,                     /* '['  */
  YYSYMBOL_SIZEOF_TYPE = 104,              /* SIZEOF_TYPE  */
  YYSYMBOL_PREFER_DECLARATION = 105,       /* PREFER_DECLARATION  */
  YYSYMBOL_IFX = 106,                      /* IFX  */
  YYSYMBOL_107_ = 107,                     /* ';'  */
  YYSYMBOL_108_ = 108,                     /* '}'  */
  YYSYMBOL_109_ = 109,                     /* '{'  */
  YYSYMBOL_110_ = 110,                     /* ','  */
  YYSYMBOL_111_ = 111,                     /* ')'  */
  YYSYMBOL_112_ = 112,                     /* ']'  */
  YYSYMBOL_YYACCEPT = 113,                 /* $accept  */
  YYSYMBOL_translation_unit = 114,         /* translation_unit  */
  YYSYMBOL_external_decl = 115,            /* external_decl  */
  YYSYMBOL_declaration = 116,              /* declaration  */
  YYSYMBOL_declaration_specifiers = 117,   /* declaration_specifiers  */
  YYSYMBOL_storage_or_type_specifier = 118, /* storage_or_type_specifier  */
  YYSYMBOL_type_specifier = 119,           /* type_specifier  */
  YYSYMBOL_tag_name = 120,                 /* tag_name  */
  YYSYMBOL_struct_or_class_specifier = 121, /* struct_or_class_specifier  */
  YYSYMBOL_122_1 = 122,                    /* $@1  */
  YYSYMBOL_123_2 = 123,                    /* $@2  */
  YYSYMBOL_124_3 = 124,                    /* @3  */
  YYSYMBOL_125_4 = 125,                    /* $@4  */
  YYSYMBOL_126_5 = 126,                    /* $@5  */
  YYSYMBOL_127_6 = 127,                    /* @6  */
  YYSYMBOL_member_decl_list_opt = 128,     /* member_decl_list_opt  */
  YYSYMBOL_inheritance_opt = 129,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 130, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 131,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 132,         /* member_decl_list  */
  YYSYMBOL_member_item = 133,              /* member_item  */
  YYSYMBOL_constructor_head = 134,         /* constructor_head  */
  YYSYMBOL_135_7 = 135,                    /* $@7  */
  YYSYMBOL_constructor_def = 136,          /* constructor_def  */
  YYSYMBOL_destructor_head = 137,          /* destructor_head  */
  YYSYMBOL_destructor_def = 138,           /* destructor_def  */
  YYSYMBOL_out_of_class_special = 139,     /* out_of_class_special  */
  YYSYMBOL_140_8 = 140,                    /* $@8  */
  YYSYMBOL_141_9 = 141,                    /* $@9  */
  YYSYMBOL_142_10 = 142,                   /* $@10  */
  YYSYMBOL_access_specifier = 143,         /* access_specifier  */
  YYSYMBOL_init_declarator_list_opt = 144, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 145,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 146,          /* init_declarator  */
  YYSYMBOL_initializer = 147,              /* initializer  */
  YYSYMBOL_initializer_list = 148,         /* initializer_list  */
  YYSYMBOL_initializer_item = 149,         /* initializer_item  */
  YYSYMBOL_pointer = 150,                  /* pointer  */
  YYSYMBOL_declarator = 151,               /* declarator  */
  YYSYMBOL_abstract_declarator = 152,      /* abstract_declarator  */
  YYSYMBOL_direct_abstract_declarator = 153, /* direct_abstract_declarator  */
  YYSYMBOL_direct_declarator = 154,        /* direct_declarator  */
  YYSYMBOL_operator_function_id = 155,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 156,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 157,              /* param_scope  */
  YYSYMBOL_constructor_args = 158,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 159,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 160,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 161,           /* parameter_decl  */
  YYSYMBOL_function_definition = 162,      /* function_definition  */
  YYSYMBOL_163_11 = 163,                   /* $@11  */
  YYSYMBOL_statement = 164,                /* statement  */
  YYSYMBOL_compound_stmt = 165,            /* compound_stmt  */
  YYSYMBOL_166_12 = 166,                   /* $@12  */
  YYSYMBOL_block_item_list_opt = 167,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 168,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 169,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 170,           /* selection_stmt  */
  YYSYMBOL_171_13 = 171,                   /* $@13  */
  YYSYMBOL_labeled_stmt = 172,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 173,           /* iteration_stmt  */
  YYSYMBOL_for_open = 174,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 175,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 176,                /* jump_stmt  */
  YYSYMBOL_expr = 177,                     /* expr  */
  YYSYMBOL_assignment_expr = 178,          /* assignment_expr  */
  YYSYMBOL_assign_op = 179,                /* assign_op  */
  YYSYMBOL_constant_expr = 180,            /* constant_expr  */
  YYSYMBOL_binary_expr = 181,              /* binary_expr  */
  YYSYMBOL_unary_expr = 182,               /* unary_expr  */
  YYSYMBOL_type_name = 183,                /* type_name  */
  YYSYMBOL_type_name_specifiers = 184,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 185,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 186,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 187,             /* builtin_call  */
  YYSYMBOL_constructor_args_opt = 188,     /* constructor_args_opt  */
  YYSYMBOL_argument_list_opt = 189,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 190,            /* argument_list  */
  YYSYMBOL_argument = 191,                 /* argument  */
  YYSYMBOL_primary_expr = 192,             /* primary_expr  */
  YYSYMBOL_string_literal = 193            /* string_literal  */
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


#line 337 "build/parser.tab.cpp"

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
#define YYLAST   2230

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  113
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  81
/* YYNRULES -- Number of rules.  */
#define YYNRULES  327
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  586

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   343


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
       2,     2,     2,    99,     2,     2,     2,    94,    87,     2,
     102,   111,    92,    90,   110,    91,   101,    93,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    84,   107,
      88,    82,    89,    83,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   103,     2,   112,    86,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   109,    85,   108,   100,     2,     2,     2,
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
      75,    76,    77,    78,    79,    80,    81,    95,    96,    97,
      98,   104,   105,   106
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   118,   118,   122,   130,   131,   132,   133,   134,   138,
     166,   179,   183,   184,   185,   186,   187,   188,   192,   193,
     194,   195,   196,   197,   198,   199,   200,   201,   202,   203,
     217,   224,   225,   229,   233,   229,   249,   249,   263,   269,
     275,   279,   275,   291,   291,   305,   311,   320,   321,   325,
     326,   330,   331,   338,   344,   350,   356,   367,   372,   384,
     385,   386,   387,   388,   395,   395,   412,   416,   423,   431,
     435,   443,   447,   443,   462,   462,   475,   476,   477,   481,
     482,   486,   487,   491,   492,   496,   497,   498,   503,   511,
     512,   516,   517,   520,   526,   527,   528,   529,   530,   534,
     540,   546,   547,   553,   557,   566,   567,   568,   569,   573,
     577,   584,   596,   605,   609,   616,   623,   642,   649,   650,
     655,   659,   659,   659,   659,   660,   660,   660,   660,   661,
     661,   661,   661,   662,   662,   662,   662,   663,   663,   663,
     663,   664,   664,   664,   665,   665,   665,   666,   666,   666,
     667,   667,   667,   668,   668,   668,   675,   679,   680,   684,
     685,   689,   693,   697,   701,   706,   711,   719,   719,   780,
     781,   782,   783,   784,   785,   786,   787,   788,   792,   792,
     801,   802,   806,   807,   811,   812,   816,   819,   822,   822,
     828,   831,   834,   842,   845,   852,   856,   860,   863,   867,
     876,   880,   881,   885,   886,   887,   888,   889,   899,   900,
     904,   905,   911,   912,   913,   914,   915,   916,   917,   918,
     919,   920,   921,   925,   929,   930,   931,   932,   933,   934,
     935,   936,   937,   938,   939,   940,   941,   942,   943,   944,
     945,   946,   947,   950,   954,   955,   956,   957,   958,   959,
     960,   961,   962,   963,   967,   968,   975,   979,   986,   993,
     997,   998,   999,  1000,  1001,  1002,  1003,  1004,  1005,  1006,
    1007,  1008,  1009,  1018,  1024,  1030,  1036,  1045,  1046,  1047,
    1082,  1092,  1099,  1104,  1114,  1115,  1116,  1117,  1121,  1122,
    1123,  1124,  1125,  1126,  1127,  1128,  1129,  1133,  1134,  1138,
    1139,  1143,  1144,  1148,  1149,  1156,  1165,  1166,  1167,  1168,
    1169,  1170,  1171,  1175,  1182,  1183,  1184,  1185,  1186,  1187,
    1188,  1189,  1190,  1191,  1192,  1199,  1204,  1205
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
  "AUTO", "EXTERN", "CONST", "IF", "ELSE", "FOR", "WHILE", "DO", "UNTIL",
  "SWITCH", "CASE", "DEFAULT", "BREAK", "CONTINUE", "GOTO", "RETURN",
  "PRINTF", "SCANF", "MALLOC", "FREE", "CALLOC", "REALLOC", "BOOL",
  "SIZEOF", "VA_LIST", "VA_START", "VA_ARG", "VA_END", "OPERATOR", "FCAST",
  "ABSTRACT_LPAREN", "IDENTIFIER", "TYPE_NAME", "INT_LITERAL",
  "FLOAT_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", "BOOL_LITERAL",
  "ARROW", "ELLIPSIS", "SCOPE_RES", "INC", "DEC", "SHL", "SHR", "LE_OP",
  "GE_OP", "EQ_OP", "NE_OP", "AND_OP", "OR_OP", "PLUS_ASSIGN",
  "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN",
  "OR_ASSIGN", "XOR_ASSIGN", "SHL_ASSIGN", "SHR_ASSIGN",
  "PREFER_EXPRESSION", "'='", "'?'", "':'", "'|'", "'^'", "'&'", "'<'",
  "'>'", "'+'", "'-'", "'*'", "'/'", "'%'", "UMINUS", "ADDR", "DEREF",
  "CAST", "'!'", "'~'", "'.'", "'('", "'['", "SIZEOF_TYPE",
  "PREFER_DECLARATION", "IFX", "';'", "'}'", "'{'", "','", "')'", "']'",
  "$accept", "translation_unit", "external_decl", "declaration",
  "declaration_specifiers", "storage_or_type_specifier", "type_specifier",
  "tag_name", "struct_or_class_specifier", "$@1", "$@2", "@3", "$@4",
  "$@5", "@6", "member_decl_list_opt", "inheritance_opt",
  "inheritance_specifier_list", "inheritance_specifier",
  "member_decl_list", "member_item", "constructor_head", "$@7",
  "constructor_def", "destructor_head", "destructor_def",
  "out_of_class_special", "$@8", "$@9", "$@10", "access_specifier",
  "init_declarator_list_opt", "init_declarator_list", "init_declarator",
  "initializer", "initializer_list", "initializer_item", "pointer",
  "declarator", "abstract_declarator", "direct_abstract_declarator",
  "direct_declarator", "operator_function_id", "overloadable_operator",
  "param_scope", "constructor_args", "parameter_list_opt",
  "parameter_list", "parameter_decl", "function_definition", "$@11",
  "statement", "compound_stmt", "$@12", "block_item_list_opt",
  "block_item_list", "expr_stmt", "selection_stmt", "$@13", "labeled_stmt",
  "iteration_stmt", "for_open", "for_incr_opt", "jump_stmt", "expr",
  "assignment_expr", "assign_op", "constant_expr", "binary_expr",
  "unary_expr", "type_name", "type_name_specifiers", "type_name_specifier",
  "postfix_expr", "builtin_call", "constructor_args_opt",
  "argument_list_opt", "argument_list", "argument", "primary_expr",
  "string_literal", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-396)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-182)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -396,  2027,  -396,    -5,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,   -32,    -4,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,   -35,  -396,  -396,  1855,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,   -73,   -13,  -396,  -396,   -12,     0,  -396,
    -396,   -26,  2046,    57,    96,  -396,  -396,   151,  -396,    93,
      99,  -396,   188,   -28,     4,  -396,  1907,   111,  1907,   138,
     122,   185,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,  -396,  -396,   131,   140,  -396,     5,    53,
      96,   143,  -396,   151,  -396,  -396,  -396,     4,  1213,   147,
    1924,   428,  -396,  -396,  -396,   159,  -396,   214,  -396,   165,
    1907,  -396,   -49,  -396,    41,  -396,   192,  -396,  -396,   173,
      35,   177,  -396,   186,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,   226,   194,   208,   217,   220,   221,   224,   225,
     227,   229,  -396,   232,   244,   245,   246,   247,   253,   254,
    1660,   255,   257,   258,   259,  -396,   -43,  -396,  -396,  -396,
    -396,  -396,  1727,  1727,  1727,  1727,  1727,  1727,  1727,  1727,
    1593,   999,  -396,  -396,  2087,   556,   197,  -396,  -396,   262,
     674,  2054,    49,  -396,  -396,   212,  -396,   260,  -396,  -396,
    -396,  -396,  -396,  -396,  -396,  -396,  1907,  -396,  -396,  -396,
     263,  -396,   160,  -396,  2054,   252,  1727,  1727,  1727,  1727,
    1727,  1727,  1727,  1727,  1727,  1593,  1593,  1593,  1593,  1593,
    1593,  1727,  1593,  -396,  1593,  1593,  1593,  1727,   277,  1727,
    -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,   194,   208,
     217,   220,   221,   224,   225,   227,   229,   164,   199,  -396,
     254,  -396,   -43,   152,  -396,   261,   222,  -396,   313,  1727,
    -396,  -396,    43,  -396,  1727,  1727,  1727,  1727,  1727,  1727,
    1727,  1727,  1727,  1727,  1727,  1727,  1727,  1727,  1727,  1727,
    1727,  1727,  1727,  -396,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,  -396,  1727,   216,   317,  -396,  -396,   219,
    1593,  1727,  -396,   171,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,   267,   273,   275,   892,   276,   283,  1727,
     302,   280,   281,   338,  1392,  -396,   306,   333,  -396,  -396,
    1855,  -396,  -396,   286,   783,  -396,  -396,  -396,  -396,  1320,
    -396,     8,  1525,   284,   287,  -396,  1727,  -396,  -396,  2054,
     285,   674,   291,    35,  -396,  -396,  1907,   289,  -396,   292,
     290,   300,   301,   303,   305,   307,   308,   309,   310,  -396,
    -396,   315,   314,  -396,   318,   319,   329,   330,   331,   335,
     336,   339,   340,   341,   342,  -396,   344,  -396,  -396,  -396,
    -396,  1727,  -396,  1727,  -396,  -396,  -396,  -396,  -396,  -396,
    -396,  -396,  -396,  -396,   104,  -396,   496,   114,  -396,   325,
    -396,   361,   337,  2087,  -396,  -396,  1106,    95,    95,   155,
     155,   316,   316,  1494,  2097,   -22,  2129,   580,  2136,   155,
     155,   100,   100,  -396,  -396,  -396,  -396,  -396,   357,  -396,
    -396,   384,   345,    85,  -396,  -396,  1727,  -396,  1727,    88,
    1727,  1727,   373,   892,  -396,  -396,   352,  -396,    39,   892,
    -396,  -396,  1464,  1464,  -396,    60,  -396,  -396,  -396,   332,
    -396,   349,  -396,   353,  -396,  -396,   354,  -396,   363,  -396,
    -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  1593,
    -396,  -396,  -396,  -396,  -396,  -396,  1794,  -396,  -396,  -396,
    -396,  -396,  -396,  -396,   365,  -396,   351,   325,   564,  1213,
     404,  -396,  -396,  1727,   436,   437,  -396,  -396,   172,   174,
     385,   389,   191,   193,   892,  -396,  -396,  -396,  -396,  1727,
    1727,  -396,  -396,  -396,  -396,  -396,   363,  -396,  -396,  -396,
    -396,  -396,   381,  -396,  1213,  2087,  -396,  -396,   892,   892,
    -396,  1727,   892,  -396,  -396,   383,   386,   387,  -396,  -396,
    -396,   471,  -396,   196,  -396,   363,   892,   892,   892,     9,
    -396,  -396,  -396,  -396,  -396,  -396
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    18,    19,    20,    21,    22,    24,
      25,    26,    27,     0,     0,    12,    15,    14,    13,    16,
      23,    28,    29,     3,     5,    79,    11,    17,    30,     6,
       4,     7,     8,    38,    39,    36,    33,    45,    46,    43,
      40,     0,     0,   109,    29,    95,    94,     0,    10,     0,
      80,    81,     0,    83,   100,   113,    47,     0,    47,    49,
       0,     0,   142,   143,   140,   141,   136,   137,   134,   135,
     138,   139,   144,   145,   146,   147,   148,   149,   150,   151,
     152,   153,   131,   128,   126,   127,   132,   133,   121,   122,
     123,   124,   125,   130,   129,     0,     0,   120,     0,     0,
       0,     0,     9,     0,    98,    97,    96,    99,     0,     0,
     156,     0,    76,    77,    78,     0,    29,     0,    59,     0,
      48,    57,     0,    62,     0,    63,     0,    60,    34,     0,
       0,     0,    71,     0,   155,   154,   110,   114,   111,   115,
     112,    82,    83,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   311,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   305,     0,   306,   307,   308,
     326,   310,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    84,    85,   210,   243,   244,   287,   277,   309,
       0,   159,     0,   157,   118,     0,    64,     0,    37,    58,
      67,   178,    66,    70,    69,    61,    47,    44,    55,    56,
      50,    51,     0,    41,   159,     0,   297,   297,   297,   297,
     297,   297,   297,   297,   297,   299,   299,   299,   299,   299,
     299,   297,     0,   254,   299,   299,   299,   297,     0,   297,
     245,   246,   247,   249,   250,   248,   251,   252,   260,   261,
     262,   263,   264,   266,   267,   268,   269,     0,     0,   271,
     265,   270,   272,     0,   208,     0,   256,   259,     0,     0,
      86,    91,     0,    89,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   213,   214,   215,   216,   217,   218,   219,
     220,   221,   222,   212,     0,     0,     0,   285,   286,     0,
     299,     0,   327,     0,    18,    19,    20,    21,    22,    24,
      25,    26,    27,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    23,   305,    29,   184,   175,
      79,   182,   169,     0,     0,   170,   171,   174,   172,     0,
     173,     0,   166,     0,   160,   161,     0,   117,   119,   159,
       0,     0,     0,     0,    53,    54,    47,     0,    74,   298,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   303,
     304,     0,   300,   301,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   324,     0,   273,   274,   275,
     276,     0,   325,     0,   260,   261,   262,   263,   264,   266,
     267,   268,   269,   265,     0,   272,     0,   101,   257,   103,
     258,     0,     0,   223,   243,    87,     0,   235,   236,   233,
     234,   229,   230,   225,   224,     0,   226,   227,   228,   231,
     232,   237,   238,   239,   240,   241,   211,   283,     0,   284,
     280,     0,     0,     0,   176,   177,     0,   200,     0,     0,
       0,     0,     0,     0,   203,   204,     0,   205,     0,     0,
     168,   183,     0,     0,   185,   101,   164,   165,   116,     0,
     158,     0,    68,     0,    35,    52,     0,    72,     0,   314,
     315,   316,   317,   318,   320,   321,   322,   323,   288,     0,
     289,   290,   291,   292,   293,   319,   255,   294,   295,   296,
     313,   312,   209,   253,     0,   105,     0,   102,     0,     0,
       0,    88,    90,     0,     0,     0,   279,   278,     0,     0,
       0,     0,     0,     0,     0,   191,   207,   206,   192,   201,
     201,   163,   162,    65,   179,    42,     0,    75,   302,   104,
     106,   107,     0,    92,     0,   242,   282,   281,     0,     0,
     196,     0,     0,   188,   190,     0,   202,     0,    73,   108,
      93,   186,   193,     0,   197,     0,     0,     0,     0,     0,
     189,   199,   198,   187,   195,   194
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -396,  -396,  -396,    17,    -1,   -19,  -396,   483,  -396,  -396,
    -396,  -396,  -396,  -396,  -396,   -51,  -396,  -396,   145,  -396,
     390,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,  -396,
    -122,  -396,  -396,   406,  -106,  -396,    86,  -257,   -20,  -336,
    -395,   -48,   218,  -396,  -396,   401,  -201,  -396,    37,   513,
    -396,  -265,  -121,  -396,   156,  -396,  -328,  -396,  -396,  -396,
    -396,  -396,   -18,  -396,  -169,   -96,  -396,   195,  -246,  -108,
    -156,  -396,   265,  -396,  -396,   520,  -136,  -396,    22,  -396,
    -396
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    23,   339,   340,    26,    27,    36,    28,    57,
     206,    56,    59,   366,    58,   119,   131,   210,   211,   120,
     121,   122,   359,   123,   124,   125,    29,   214,   546,   488,
     126,    49,    50,    51,   271,   272,   273,    52,   142,   418,
     419,    54,    55,    97,   191,   369,   353,   354,   355,   127,
     109,   341,   342,   361,   343,   344,   345,   346,   575,   347,
     348,   349,   565,   350,   351,   264,   304,   422,   184,   185,
     380,   266,   267,   186,   187,   370,   381,   382,   383,   188,
     189
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      25,   202,   182,   204,   107,    53,    48,   129,   212,   417,
     584,   263,   183,   367,   193,   195,   477,   238,    24,    33,
      34,   473,   517,   423,   265,    41,    60,   101,   427,   428,
     429,   430,   431,   432,   433,   434,   -31,   436,   437,   438,
     439,   440,   441,   442,   443,   444,   445,    37,    38,   112,
     113,   114,   233,    42,   108,    25,   136,    25,   200,   239,
     201,   459,   523,   263,   240,   241,   242,   243,   244,   245,
     246,   247,   -31,   118,    61,   118,   390,    35,   514,   471,
     517,  -167,   104,   423,   -32,   183,   208,   209,   401,   530,
     384,   385,   386,   387,   388,   475,   -32,   -31,   391,   392,
     393,    42,    31,    32,   138,    39,   110,   111,    42,   -32,
     414,    43,   100,   435,   531,   474,   585,    98,   401,    25,
     193,   193,   193,   193,   193,   193,   193,   193,   193,   379,
     379,   379,   379,   379,   379,   193,   104,   118,   379,   379,
     379,   193,   453,   193,   539,   540,   537,   105,   203,   401,
     201,   425,   106,   426,   414,   362,    99,   417,   481,   356,
     357,   424,    47,   416,   414,   468,   424,   424,   424,   424,
     424,   424,   424,   424,   452,   424,   424,   424,   424,   424,
     424,   424,   424,   424,   424,   288,   289,   290,   291,   292,
     352,    45,   290,   291,   292,   401,    46,   527,   535,    42,
     102,   105,    43,   100,   538,    25,   106,   416,   446,   103,
     104,   364,   365,   352,   379,   397,   398,   416,   274,   275,
     128,   424,   130,   118,   132,   404,   405,   406,   407,   408,
     409,   410,   411,   412,   257,   258,    42,   133,    45,    43,
     100,   212,   134,    46,   259,   288,   289,   290,   291,   292,
     399,   400,   135,    47,   140,   305,   190,   306,   307,   308,
     480,   196,   401,   402,   413,   197,   261,   447,   448,   564,
     450,   451,   414,   198,   415,   105,   205,   555,   454,   455,
     106,   207,   401,   558,   401,   559,   213,   528,   215,   529,
      47,   532,   533,   571,   572,   513,   216,   574,   309,   310,
     311,   401,   562,   401,   563,   512,   401,   579,   108,    45,
     217,   581,   582,   583,    46,   486,   137,   139,   312,   218,
     516,    48,   219,   220,   358,   416,   221,   222,   395,   223,
     183,   224,   476,    48,   225,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,   226,   227,   228,   229,
      15,    16,    17,    18,    19,   230,   231,   234,   352,   235,
     236,   237,   360,   368,   421,    25,   472,   547,   449,   456,
     566,   566,   403,   363,    20,   457,    21,   458,   460,   274,
     275,   276,   277,   118,   116,   461,   463,   464,   465,   466,
     469,   541,   573,   238,   470,   478,   482,   479,   513,   484,
     487,   489,   356,   379,   286,   287,   288,   289,   290,   291,
     292,   490,   491,   553,   492,   424,   493,   524,   494,   495,
     496,   497,   552,   183,   499,   568,   498,   107,   518,   500,
     501,   143,   144,   145,   146,   147,   148,   149,   150,   151,
     502,   503,   504,   519,   525,   152,   505,   506,   570,   520,
     507,   508,   509,   510,   580,   511,   526,   534,   183,   536,
     543,   544,   545,   550,   153,   154,   155,   156,   157,   158,
     159,   160,   201,   161,   162,   163,   549,   164,   352,   165,
     166,   167,   168,   169,   170,   171,   554,   556,   557,   172,
     173,   561,   560,   569,   576,   578,   401,    40,   577,   143,
     144,   145,   146,   147,   148,   149,   150,   151,   485,   141,
     199,   192,   522,   152,    30,   174,   542,   483,   175,   176,
     177,   548,   567,     0,   462,     0,     0,   178,   179,     0,
     180,   420,   153,   154,   155,   156,   157,   158,   159,   160,
     194,   161,   162,   163,     0,   164,     0,   165,   166,   167,
     168,   169,   170,   171,     0,     0,     0,   172,   173,     0,
       0,     0,     0,     0,     0,     0,     0,   143,   144,   145,
     146,   147,   148,   149,   150,   151,     0,     0,     0,     0,
       0,   152,     0,   174,     0,     0,   175,   176,   177,     0,
       0,     0,     0,     0,     0,   178,   179,     0,   180,     0,
     153,   154,   155,   156,   157,   158,   159,   160,   515,   161,
     162,   163,     0,   164,     0,   165,   166,   167,   168,   169,
     170,   171,     0,     0,     0,   172,   173,   293,   294,   295,
     296,   297,   298,   299,   300,   301,   302,     0,   303,     0,
       0,     0,     0,   274,   275,   276,   277,   278,   279,     0,
       0,   174,     0,     0,   175,   176,   177,     0,     0,     0,
       0,     0,     0,   178,   179,     0,   180,   285,   286,   287,
     288,   289,   290,   291,   292,   313,   551,   314,   315,   316,
     317,   318,   319,   320,   321,   322,    13,    14,     0,     0,
       0,   152,    15,    16,    17,    18,    19,   323,     0,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     153,   154,   155,   156,   157,   158,   335,   160,    21,   161,
     162,   163,     0,   164,     0,   336,   337,   167,   168,   169,
     170,   171,     0,     0,     0,   172,   173,   371,   372,   373,
     374,   375,   376,   377,   378,     0,     0,     0,     0,     0,
       0,   389,     0,     0,     0,     0,     0,   394,     0,   396,
       0,   174,     0,     0,   175,   176,   177,     0,     0,     0,
       0,     0,     0,   178,   179,     0,   180,     0,     0,     0,
       0,   338,  -180,   201,   313,     0,   314,   315,   316,   317,
     318,   319,   320,   321,   322,    13,    14,     0,     0,     0,
     152,    15,    16,    17,    18,    19,   323,     0,   324,   325,
     326,   327,   328,   329,   330,   331,   332,   333,   334,   153,
     154,   155,   156,   157,   158,   335,   160,    21,   161,   162,
     163,     0,   164,     0,   336,   337,   167,   168,   169,   170,
     171,     0,     0,     0,   172,   173,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     174,     0,     0,   175,   176,   177,     0,     0,     0,     0,
       0,     0,   178,   179,     0,   180,     0,     0,     0,     0,
     338,  -181,   201,   313,     0,   314,   315,   316,   317,   318,
     319,   320,   321,   322,    13,    14,     0,     0,     0,   152,
      15,    16,    17,    18,    19,   323,     0,   324,   325,   326,
     327,   328,   329,   330,   331,   332,   333,   334,   153,   154,
     155,   156,   157,   158,   335,   160,    21,   161,   162,   163,
       0,   164,     0,   336,   337,   167,   168,   169,   170,   171,
       0,     0,     0,   172,   173,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   174,
       0,     0,   175,   176,   177,     0,     0,     0,     0,     0,
       0,   178,   179,     0,   180,     0,     0,     0,     0,   338,
       0,   201,   143,   144,   145,   146,   147,   148,   149,   150,
     151,     0,     0,     0,     0,     0,   152,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   153,   154,   155,   156,   157,
     158,   159,   160,     0,   161,   162,   163,     0,   164,     0,
     165,   166,   167,   168,   169,   170,   171,     0,     0,     0,
     172,   173,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   174,     0,     0,   175,
     176,   177,     0,     0,     0,     0,     0,     0,   178,   179,
     268,   180,   269,     0,     0,     0,     0,   270,   181,   143,
     144,   145,   146,   147,   148,   149,   150,   151,     0,     0,
       0,     0,     0,   152,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   153,   154,   155,   156,   157,   158,   159,   160,
       0,   161,   162,   163,     0,   164,     0,   165,   166,   167,
     168,   169,   170,   171,     0,     0,     0,   172,   173,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   174,     0,     0,   175,   176,   177,     0,
       0,     0,     0,     0,     0,   178,   179,   268,   180,   269,
       0,     0,     0,     0,   521,   181,   143,   144,   145,   146,
     147,   148,   149,   150,   151,     0,     0,     0,     0,     0,
     152,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   153,
     154,   155,   156,   157,   158,   159,   160,     0,   161,   162,
     163,     0,   164,     0,   165,   166,   167,   168,   169,   170,
     171,     0,     0,     0,   172,   173,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     174,     0,     0,   175,   176,   177,     0,     0,     0,     0,
       0,     0,   178,   179,     0,   180,     0,     0,     0,     0,
       0,     0,   181,   314,   315,   316,   317,   318,   319,   320,
     321,   322,    13,    14,     0,     0,     0,   152,    15,    16,
      17,    18,    19,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   153,   154,   155,   156,
     157,   158,   335,   160,    21,   161,   162,   163,     0,   164,
       0,   165,   337,   167,   168,   169,   170,   171,     0,     0,
       0,   172,   173,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   143,   144,   145,   146,   147,
     148,   149,   150,   151,     0,     0,     0,   174,     0,   152,
     175,   176,   177,     0,     0,     0,     0,     0,     0,   178,
     179,     0,   180,     0,     0,     0,     0,   338,   153,   154,
     155,   156,   157,   158,   159,   160,     0,   161,   162,   163,
       0,   164,     0,   165,   166,   167,   168,   169,   170,   171,
       0,     0,     0,   172,   173,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   143,   144,   145,
     146,   147,   148,   149,   150,   151,     0,     0,     0,   174,
       0,   152,   175,   176,   177,     0,     0,     0,     0,     0,
       0,   178,   179,     0,   180,     0,     0,     0,     0,   467,
     153,   154,   155,   156,   157,   158,   159,   160,     0,   161,
     162,   163,     0,   164,     0,   165,   166,   167,   168,   169,
     170,   171,     0,     0,     0,   172,   173,     0,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,     0,
       0,     0,     0,    15,    16,    17,    18,    19,     0,     0,
       0,   174,     0,     0,   175,   176,   177,   274,   275,   276,
     277,   278,   279,   178,   179,     0,   180,    20,     0,    21,
       0,   338,     0,    42,     0,   414,    43,    44,     0,   283,
     284,   285,   286,   287,   288,   289,   290,   291,   292,     0,
       0,     0,     0,     0,     0,     0,   248,   249,   250,   251,
     252,   253,   254,   255,   256,   257,   258,     0,     0,     0,
     152,     0,    45,     0,     0,   259,     0,    46,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    47,   416,   153,
     154,   155,   156,   157,   158,   260,   160,   261,   161,   162,
     163,     0,   164,     0,   165,   262,   167,   168,   169,   170,
     171,     0,     0,     0,   172,   173,     0,     0,     0,     0,
       0,     0,     0,   143,   144,   145,   146,   147,   148,   149,
     150,   151,     0,     0,     0,     0,     0,   152,     0,     0,
     174,     0,     0,   175,   176,   177,     0,     0,     0,     0,
       0,     0,   178,   179,     0,   180,   153,   154,   155,   156,
     157,   158,   159,   160,     0,   161,   162,   163,     0,   164,
       0,   165,   166,   167,   168,   169,   170,   171,     0,     0,
       0,   172,   173,     0,     0,     0,     0,     0,     0,     0,
     143,   144,   145,   146,   147,   148,   149,   150,   151,     0,
       0,     0,     0,     0,   152,     0,     0,   174,     0,     0,
     175,   176,   177,     0,     0,     0,     0,     0,     0,   178,
     179,     0,   232,   153,   154,   155,   156,   157,   158,   159,
     160,     0,   161,   162,   163,     0,   164,     0,   165,   166,
     167,   168,   169,   170,   171,     0,     0,     0,   172,   173,
       0,     0,     0,     0,     0,     0,     0,   143,   144,   145,
     146,   147,   148,   149,   150,   151,     0,     0,     0,     0,
       0,   152,     0,     0,   174,     0,     0,   175,   176,   177,
       0,     0,     0,     0,     0,     0,   178,   179,     0,   180,
     153,   154,   155,   156,   157,   158,   159,   160,     0,   161,
     162,   163,     0,   164,     0,   165,   166,   167,   168,   169,
     170,   171,     0,     0,     0,   172,   173,     0,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,     0,
       0,     0,     0,    15,    16,    17,    18,    19,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   178,   179,     0,   180,    20,     0,    21,
       0,     0,     0,    42,     0,     0,    43,    44,     0,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,   112,   113,   114,     0,    15,    16,    17,    18,    19,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   152,    45,     0,     0,     0,     0,    46,     0,    20,
       0,    21,     0,     0,     0,     0,     0,    47,   115,   116,
     153,   154,   155,   156,   157,   158,     0,   160,     0,   161,
     162,   163,     0,   164,     0,   165,     0,   167,   168,   169,
     170,   171,     0,     0,     0,   172,   173,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   117,     0,     0,
       0,   174,     0,     0,   175,   176,   177,     0,     0,     0,
       0,     0,     0,   178,   179,     0,   180,     2,     3,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,     0,     0,     0,     0,    15,    16,    17,    18,    19,
       0,     0,     0,     0,     0,     0,     0,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,     0,    20,
       0,    21,    15,    16,    17,    18,    19,     0,     0,    22,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    20,     0,    21,     0,
       0,     0,     0,     0,     0,     0,   116,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,     0,    82,     0,
       0,    83,    84,    85,    86,    87,    88,    89,    90,    91,
      92,     0,     0,     0,     0,    93,    94,     0,    95,    96,
     274,   275,   276,   277,   278,   279,   280,   281,     0,     0,
     274,   275,   276,   277,   278,   279,   280,     0,     0,     0,
     282,     0,   283,   284,   285,   286,   287,   288,   289,   290,
     291,   292,   283,   284,   285,   286,   287,   288,   289,   290,
     291,   292,   274,   275,   276,   277,   278,   279,     0,   274,
     275,   276,   277,   278,   279,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   284,   285,   286,   287,   288,
     289,   290,   291,   292,   286,   287,   288,   289,   290,   291,
     292
};

static const yytype_int16 yycheck[] =
{
       1,   122,   108,   124,    52,    25,    25,    58,   130,   266,
       1,   180,   108,   214,   110,   111,   352,    60,     1,    51,
      52,   349,   417,   269,   180,    60,    52,    47,   274,   275,
     276,   277,   278,   279,   280,   281,   109,   283,   284,   285,
     286,   287,   288,   289,   290,   291,   292,    51,    52,    14,
      15,    16,   160,    48,    82,    56,    51,    58,   107,   102,
     109,   326,    84,   232,   172,   173,   174,   175,   176,   177,
     178,   179,    84,    56,   100,    58,   232,   109,   414,   344,
     475,   109,    22,   329,    84,   181,    51,    52,   110,     1,
     226,   227,   228,   229,   230,   352,   109,   109,   234,   235,
     236,    48,   107,   108,    51,   109,   102,   103,    48,   109,
      50,    51,    52,   282,    26,   107,   107,    60,   110,   120,
     216,   217,   218,   219,   220,   221,   222,   223,   224,   225,
     226,   227,   228,   229,   230,   231,    22,   120,   234,   235,
     236,   237,   311,   239,   472,   473,   107,    87,   107,   110,
     109,   108,    92,   110,    50,   206,    60,   414,   359,   110,
     111,   269,   102,   103,    50,   334,   274,   275,   276,   277,
     278,   279,   280,   281,   310,   283,   284,   285,   286,   287,
     288,   289,   290,   291,   292,    90,    91,    92,    93,    94,
     191,    87,    92,    93,    94,   110,    92,   112,   463,    48,
     107,    87,    51,    52,   469,   206,    92,   103,   304,   110,
      22,    51,    52,   214,   310,    51,    52,   103,    63,    64,
     109,   329,    84,   206,   102,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    48,    52,    87,    51,
      52,   363,   111,    92,    22,    90,    91,    92,    93,    94,
      51,    52,   112,   102,   111,    58,   109,    60,    61,    62,
     356,   102,   110,   111,    42,    51,    44,    51,    52,   534,
      51,    52,    50,   108,    52,    87,    84,   523,   107,   108,
      92,   108,   110,   111,   110,   111,   109,   456,   102,   458,
     102,   460,   461,   558,   559,   403,   102,   562,   101,   102,
     103,   110,   111,   110,   111,   401,   110,   111,    82,    87,
     102,   576,   577,   578,    92,   366,    98,    99,    56,   102,
     416,   340,   102,   102,   112,   103,   102,   102,    51,   102,
     426,   102,   352,   352,   102,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,   102,   102,   102,   102,
      18,    19,    20,    21,    22,   102,   102,   102,   359,   102,
     102,   102,   102,   111,    51,   366,   349,   488,    51,   102,
     539,   540,   111,   110,    42,   102,    44,   102,   102,    63,
      64,    65,    66,   366,    52,   102,    84,   107,   107,    51,
      84,    59,   561,    60,   108,   111,   111,   110,   506,   108,
     111,   111,   110,   499,    88,    89,    90,    91,    92,    93,
      94,   111,   111,   519,   111,   523,   111,    60,   111,   111,
     111,   111,   518,   519,   110,   546,   111,   475,   103,   111,
     111,     3,     4,     5,     6,     7,     8,     9,    10,    11,
     111,   111,   111,    82,    60,    17,   111,   111,   554,   112,
     111,   111,   111,   111,   575,   111,   111,    84,   554,   107,
     111,   108,   108,   112,    36,    37,    38,    39,    40,    41,
      42,    43,   109,    45,    46,    47,   111,    49,   479,    51,
      52,    53,    54,    55,    56,    57,    82,    51,    51,    61,
      62,   102,   107,   112,   111,    24,   110,    14,   111,     3,
       4,     5,     6,     7,     8,     9,    10,    11,   363,   103,
     120,   110,   426,    17,     1,    87,   479,   361,    90,    91,
      92,   499,   540,    -1,   329,    -1,    -1,    99,   100,    -1,
     102,   266,    36,    37,    38,    39,    40,    41,    42,    43,
     112,    45,    46,    47,    -1,    49,    -1,    51,    52,    53,
      54,    55,    56,    57,    -1,    -1,    -1,    61,    62,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    17,    -1,    87,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    99,   100,    -1,   102,    -1,
      36,    37,    38,    39,    40,    41,    42,    43,   112,    45,
      46,    47,    -1,    49,    -1,    51,    52,    53,    54,    55,
      56,    57,    -1,    -1,    -1,    61,    62,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    -1,    82,    -1,
      -1,    -1,    -1,    63,    64,    65,    66,    67,    68,    -1,
      -1,    87,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    99,   100,    -1,   102,    87,    88,    89,
      90,    91,    92,    93,    94,     1,   112,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    -1,    -1,
      -1,    17,    18,    19,    20,    21,    22,    23,    -1,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    -1,    49,    -1,    51,    52,    53,    54,    55,
      56,    57,    -1,    -1,    -1,    61,    62,   217,   218,   219,
     220,   221,   222,   223,   224,    -1,    -1,    -1,    -1,    -1,
      -1,   231,    -1,    -1,    -1,    -1,    -1,   237,    -1,   239,
      -1,    87,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    99,   100,    -1,   102,    -1,    -1,    -1,
      -1,   107,   108,   109,     1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    -1,    -1,    -1,
      17,    18,    19,    20,    21,    22,    23,    -1,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,    -1,    49,    -1,    51,    52,    53,    54,    55,    56,
      57,    -1,    -1,    -1,    61,    62,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      87,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,   100,    -1,   102,    -1,    -1,    -1,    -1,
     107,   108,   109,     1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    -1,    -1,    -1,    17,
      18,    19,    20,    21,    22,    23,    -1,    25,    26,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    42,    43,    44,    45,    46,    47,
      -1,    49,    -1,    51,    52,    53,    54,    55,    56,    57,
      -1,    -1,    -1,    61,    62,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    99,   100,    -1,   102,    -1,    -1,    -1,    -1,   107,
      -1,   109,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    36,    37,    38,    39,    40,
      41,    42,    43,    -1,    45,    46,    47,    -1,    49,    -1,
      51,    52,    53,    54,    55,    56,    57,    -1,    -1,    -1,
      61,    62,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    87,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,   100,
     101,   102,   103,    -1,    -1,    -1,    -1,   108,   109,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    -1,    17,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    36,    37,    38,    39,    40,    41,    42,    43,
      -1,    45,    46,    47,    -1,    49,    -1,    51,    52,    53,
      54,    55,    56,    57,    -1,    -1,    -1,    61,    62,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    87,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    99,   100,   101,   102,   103,
      -1,    -1,    -1,    -1,   108,   109,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      17,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    36,
      37,    38,    39,    40,    41,    42,    43,    -1,    45,    46,
      47,    -1,    49,    -1,    51,    52,    53,    54,    55,    56,
      57,    -1,    -1,    -1,    61,    62,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      87,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,   100,    -1,   102,    -1,    -1,    -1,    -1,
      -1,    -1,   109,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    17,    18,    19,
      20,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    -1,    49,
      -1,    51,    52,    53,    54,    55,    56,    57,    -1,    -1,
      -1,    61,    62,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    -1,    -1,    -1,    87,    -1,    17,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
     100,    -1,   102,    -1,    -1,    -1,    -1,   107,    36,    37,
      38,    39,    40,    41,    42,    43,    -1,    45,    46,    47,
      -1,    49,    -1,    51,    52,    53,    54,    55,    56,    57,
      -1,    -1,    -1,    61,    62,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    87,
      -1,    17,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    99,   100,    -1,   102,    -1,    -1,    -1,    -1,   107,
      36,    37,    38,    39,    40,    41,    42,    43,    -1,    45,
      46,    47,    -1,    49,    -1,    51,    52,    53,    54,    55,
      56,    57,    -1,    -1,    -1,    61,    62,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    -1,
      -1,    -1,    -1,    18,    19,    20,    21,    22,    -1,    -1,
      -1,    87,    -1,    -1,    90,    91,    92,    63,    64,    65,
      66,    67,    68,    99,   100,    -1,   102,    42,    -1,    44,
      -1,   107,    -1,    48,    -1,    50,    51,    52,    -1,    85,
      86,    87,    88,    89,    90,    91,    92,    93,    94,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    -1,    -1,    -1,
      17,    -1,    87,    -1,    -1,    22,    -1,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,    -1,    49,    -1,    51,    52,    53,    54,    55,    56,
      57,    -1,    -1,    -1,    61,    62,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,
      87,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,   100,    -1,   102,    36,    37,    38,    39,
      40,    41,    42,    43,    -1,    45,    46,    47,    -1,    49,
      -1,    51,    52,    53,    54,    55,    56,    57,    -1,    -1,
      -1,    61,    62,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    17,    -1,    -1,    87,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
     100,    -1,   102,    36,    37,    38,    39,    40,    41,    42,
      43,    -1,    45,    46,    47,    -1,    49,    -1,    51,    52,
      53,    54,    55,    56,    57,    -1,    -1,    -1,    61,    62,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    17,    -1,    -1,    87,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    99,   100,    -1,   102,
      36,    37,    38,    39,    40,    41,    42,    43,    -1,    45,
      46,    47,    -1,    49,    -1,    51,    52,    53,    54,    55,
      56,    57,    -1,    -1,    -1,    61,    62,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    -1,
      -1,    -1,    -1,    18,    19,    20,    21,    22,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    99,   100,    -1,   102,    42,    -1,    44,
      -1,    -1,    -1,    48,    -1,    -1,    51,    52,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    -1,    18,    19,    20,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    17,    87,    -1,    -1,    -1,    -1,    92,    -1,    42,
      -1,    44,    -1,    -1,    -1,    -1,    -1,   102,    51,    52,
      36,    37,    38,    39,    40,    41,    -1,    43,    -1,    45,
      46,    47,    -1,    49,    -1,    51,    -1,    53,    54,    55,
      56,    57,    -1,    -1,    -1,    61,    62,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   100,    -1,    -1,
      -1,    87,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    99,   100,    -1,   102,     0,     1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    -1,    -1,    -1,    -1,    18,    19,    20,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    -1,    42,
      -1,    44,    18,    19,    20,    21,    22,    -1,    -1,    52,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    42,    -1,    44,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    52,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    -1,    82,    -1,
      -1,    85,    86,    87,    88,    89,    90,    91,    92,    93,
      94,    -1,    -1,    -1,    -1,    99,   100,    -1,   102,   103,
      63,    64,    65,    66,    67,    68,    69,    70,    -1,    -1,
      63,    64,    65,    66,    67,    68,    69,    -1,    -1,    -1,
      83,    -1,    85,    86,    87,    88,    89,    90,    91,    92,
      93,    94,    85,    86,    87,    88,    89,    90,    91,    92,
      93,    94,    63,    64,    65,    66,    67,    68,    -1,    63,
      64,    65,    66,    67,    68,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    86,    87,    88,    89,    90,
      91,    92,    93,    94,    88,    89,    90,    91,    92,    93,
      94
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   114,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    18,    19,    20,    21,    22,
      42,    44,    52,   115,   116,   117,   118,   119,   121,   139,
     162,   107,   108,    51,    52,   109,   120,    51,    52,   109,
     120,    60,    48,    51,    52,    87,    92,   102,   118,   144,
     145,   146,   150,   151,   154,   155,   124,   122,   127,   125,
      52,   100,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    82,    85,    86,    87,    88,    89,    90,    91,
      92,    93,    94,    99,   100,   102,   103,   156,    60,    60,
      52,   151,   107,   110,    22,    87,    92,   154,    82,   163,
     102,   103,    14,    15,    16,    51,    52,   100,   116,   128,
     132,   133,   134,   136,   137,   138,   143,   162,   109,   128,
      84,   129,   102,    52,   111,   112,    51,   155,    51,   155,
     111,   146,   151,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    17,    36,    37,    38,    39,    40,    41,    42,
      43,    45,    46,    47,    49,    51,    52,    53,    54,    55,
      56,    57,    61,    62,    87,    90,    91,    92,    99,   100,
     102,   109,   147,   178,   181,   182,   186,   187,   192,   193,
     109,   157,   158,   178,   112,   178,   102,    51,   108,   133,
     107,   109,   165,   107,   165,    84,   123,   108,    51,    52,
     130,   131,   143,   109,   140,   102,   102,   102,   102,   102,
     102,   102,   102,   102,   102,   102,   102,   102,   102,   102,
     102,   102,   102,   182,   102,   102,   102,   102,    60,   102,
     182,   182,   182,   182,   182,   182,   182,   182,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    22,
      42,    44,    52,   177,   178,   183,   184,   185,   101,   103,
     108,   147,   148,   149,    63,    64,    65,    66,    67,    68,
      69,    70,    83,    85,    86,    87,    88,    89,    90,    91,
      92,    93,    94,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    82,   179,    58,    60,    61,    62,   101,
     102,   103,    56,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    23,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    42,    51,    52,   107,   116,
     117,   164,   165,   167,   168,   169,   170,   172,   173,   174,
     176,   177,   117,   159,   160,   161,   110,   111,   112,   135,
     102,   166,   128,   110,    51,    52,   126,   159,   111,   158,
     188,   188,   188,   188,   188,   188,   188,   188,   188,   178,
     183,   189,   190,   191,   189,   189,   189,   189,   189,   188,
     183,   189,   189,   189,   188,    51,   188,    51,    52,    51,
      52,   110,   111,   111,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    42,    50,    52,   103,   150,   152,   153,
     185,    51,   180,   181,   182,   108,   110,   181,   181,   181,
     181,   181,   181,   181,   181,   177,   181,   181,   181,   181,
     181,   181,   181,   181,   181,   181,   178,    51,    52,    51,
      51,    52,   189,   177,   107,   108,   102,   102,   102,   164,
     102,   102,   180,    84,   107,   107,    51,   107,   177,    84,
     108,   164,   116,   169,   107,   150,   151,   152,   111,   110,
     178,   159,   111,   167,   108,   131,   128,   111,   142,   111,
     111,   111,   111,   111,   111,   111,   111,   111,   111,   110,
     111,   111,   111,   111,   111,   111,   111,   111,   111,   111,
     111,   111,   178,   182,   152,   112,   178,   153,   103,    82,
     112,   108,   149,    84,    60,    60,   111,   112,   177,   177,
       1,    26,   177,   177,    84,   164,   107,   107,   164,   169,
     169,    59,   161,   111,   108,   108,   141,   165,   191,   111,
     112,   112,   178,   147,    82,   181,    51,    51,   111,   111,
     107,   102,   111,   111,   164,   175,   177,   175,   165,   112,
     147,   164,   164,   177,   164,   171,   111,   111,    24,   111,
     165,   164,   164,   164,     1,   107
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   113,   114,   114,   115,   115,   115,   115,   115,   116,
     117,   117,   118,   118,   118,   118,   118,   118,   119,   119,
     119,   119,   119,   119,   119,   119,   119,   119,   119,   119,
     119,   120,   120,   122,   123,   121,   124,   121,   121,   121,
     125,   126,   121,   127,   121,   121,   121,   128,   128,   129,
     129,   130,   130,   131,   131,   131,   131,   132,   132,   133,
     133,   133,   133,   133,   135,   134,   136,   136,   137,   138,
     138,   140,   141,   139,   142,   139,   143,   143,   143,   144,
     144,   145,   145,   146,   146,   147,   147,   147,   147,   148,
     148,   149,   149,   149,   150,   150,   150,   150,   150,   151,
     151,   152,   152,   152,   153,   153,   153,   153,   153,   154,
     154,   154,   154,   154,   154,   154,   154,   154,   154,   154,
     155,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   156,   156,   156,   156,   156,   157,   158,   158,   159,
     159,   160,   160,   160,   161,   161,   161,   163,   162,   164,
     164,   164,   164,   164,   164,   164,   164,   164,   166,   165,
     167,   167,   168,   168,   169,   169,   170,   170,   171,   170,
     172,   172,   172,   173,   173,   173,   173,   173,   173,   173,
     174,   175,   175,   176,   176,   176,   176,   176,   177,   177,
     178,   178,   179,   179,   179,   179,   179,   179,   179,   179,
     179,   179,   179,   180,   181,   181,   181,   181,   181,   181,
     181,   181,   181,   181,   181,   181,   181,   181,   181,   181,
     181,   181,   181,   181,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   183,   183,   184,   184,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   186,   186,   186,
     186,   186,   186,   186,   186,   186,   186,   186,   187,   187,
     187,   187,   187,   187,   187,   187,   187,   188,   188,   189,
     189,   190,   190,   191,   191,   192,   192,   192,   192,   192,
     192,   192,   192,   192,   192,   192,   192,   192,   192,   192,
     192,   192,   192,   192,   192,   192,   193,   193
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     0,     0,     7,     0,     5,     2,     2,
       0,     0,     8,     0,     5,     2,     2,     0,     1,     0,
       2,     1,     3,     2,     2,     1,     1,     1,     2,     1,
       1,     2,     1,     1,     0,     5,     2,     2,     4,     2,
       2,     0,     0,     9,     0,     8,     1,     1,     1,     0,
       1,     1,     3,     1,     3,     1,     2,     3,     4,     1,
       3,     1,     4,     5,     1,     1,     2,     2,     2,     2,
       1,     1,     2,     1,     3,     2,     3,     3,     4,     1,
       3,     3,     3,     1,     3,     3,     5,     4,     3,     4,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     2,     2,     0,     1,     3,     0,
       1,     1,     3,     3,     2,     2,     1,     0,     6,     1,
       1,     1,     1,     1,     1,     1,     2,     2,     0,     4,
       0,     1,     1,     2,     1,     2,     5,     7,     0,     6,
       4,     3,     3,     5,     7,     7,     4,     5,     6,     6,
       2,     0,     1,     2,     2,     2,     3,     3,     1,     3,
       1,     3,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     5,     1,     1,     2,     2,     2,     2,     2,
       2,     2,     2,     4,     2,     4,     1,     2,     2,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     2,     2,     2,     2,     1,     4,     4,
       3,     5,     5,     3,     3,     2,     2,     1,     4,     4,
       4,     4,     4,     4,     4,     4,     4,     0,     1,     0,
       1,     1,     3,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     4,     4,     4,     4,     4,     4,     4,     4,
       4,     4,     4,     4,     3,     3,     1,     2
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
#line 118 "../phase2-parser/src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2445 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 122 "../phase2-parser/src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2455 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 130 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2461 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 131 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2467 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 132 "../phase2-parser/src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2473 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 133 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2479 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 134 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2485 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 138 "../phase2-parser/src/parser.y"
                                                          {
          endDeclaratorList();
          std::vector<ASTNodePtr> declNodes;
          for (auto &d : yyvsp[-1].paramList) {
              auto n = registerDeclarator(d, yyvsp[-2].typeSpec);
              if (n) declNodes.push_back(n);
          }
          if (declNodes.empty()) {
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
#line 2515 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 166 "../phase2-parser/src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          if (yyvsp[0].typeSpec.isExtern) yyval.typeSpec.isExtern = true;
          yyval.typeSpec.storageClasses += yyvsp[0].typeSpec.storageClasses;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isAuto) yyval.typeSpec.isAuto = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2533 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 179 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2539 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 183 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2545 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: EXTERN  */
#line 184 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isExtern = true; yyval.typeSpec.storageClasses = 1; }
#line 2551 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: AUTO  */
#line 185 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2557 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: TYPEDEF  */
#line 186 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2563 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: CONST  */
#line 187 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2569 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: type_specifier  */
#line 188 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2575 "build/parser.tab.cpp"
    break;

  case 18: /* type_specifier: INT  */
#line 192 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2581 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: CHAR  */
#line 193 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2587 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: FLOAT  */
#line 194 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2593 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: DOUBLE  */
#line 195 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2599 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: VOID  */
#line 196 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2605 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: BOOL  */
#line 197 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2611 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: SHORT  */
#line 198 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2617 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: LONG  */
#line 199 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2623 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SIGNED  */
#line 200 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2629 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: UNSIGNED  */
#line 201 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2635 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: VA_LIST  */
#line 202 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2641 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: TYPE_NAME  */
#line 203 "../phase2-parser/src/parser.y"
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
#line 2660 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: struct_or_class_specifier  */
#line 217 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2666 "build/parser.tab.cpp"
    break;

  case 31: /* tag_name: IDENTIFIER  */
#line 224 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2672 "build/parser.tab.cpp"
    break;

  case 32: /* tag_name: TYPE_NAME  */
#line 225 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2678 "build/parser.tab.cpp"
    break;

  case 33: /* $@1: %empty  */
#line 229 "../phase2-parser/src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2688 "build/parser.tab.cpp"
    break;

  case 34: /* $@2: %empty  */
#line 233 "../phase2-parser/src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2694 "build/parser.tab.cpp"
    break;

  case 35: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 233 "../phase2-parser/src/parser.y"
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
#line 2712 "build/parser.tab.cpp"
    break;

  case 36: /* @3: %empty  */
#line 249 "../phase2-parser/src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2724 "build/parser.tab.cpp"
    break;

  case 37: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 255 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2737 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 263 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2748 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 269 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2759 "build/parser.tab.cpp"
    break;

  case 40: /* $@4: %empty  */
#line 275 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2769 "build/parser.tab.cpp"
    break;

  case 41: /* $@5: %empty  */
#line 279 "../phase2-parser/src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2775 "build/parser.tab.cpp"
    break;

  case 42: /* struct_or_class_specifier: CLASS tag_name $@4 inheritance_opt '{' $@5 member_decl_list_opt '}'  */
#line 279 "../phase2-parser/src/parser.y"
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
#line 2792 "build/parser.tab.cpp"
    break;

  case 43: /* @6: %empty  */
#line 291 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2804 "build/parser.tab.cpp"
    break;

  case 44: /* struct_or_class_specifier: CLASS '{' @6 member_decl_list_opt '}'  */
#line 297 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2817 "build/parser.tab.cpp"
    break;

  case 45: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 305 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2828 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 311 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2839 "build/parser.tab.cpp"
    break;

  case 47: /* member_decl_list_opt: %empty  */
#line 320 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 2845 "build/parser.tab.cpp"
    break;

  case 48: /* member_decl_list_opt: member_decl_list  */
#line 321 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2851 "build/parser.tab.cpp"
    break;

  case 49: /* inheritance_opt: %empty  */
#line 325 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 2857 "build/parser.tab.cpp"
    break;

  case 50: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 326 "../phase2-parser/src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 2863 "build/parser.tab.cpp"
    break;

  case 51: /* inheritance_specifier_list: inheritance_specifier  */
#line 330 "../phase2-parser/src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2869 "build/parser.tab.cpp"
    break;

  case 52: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 331 "../phase2-parser/src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 2878 "build/parser.tab.cpp"
    break;

  case 53: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 338 "../phase2-parser/src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2889 "build/parser.tab.cpp"
    break;

  case 54: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 344 "../phase2-parser/src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2900 "build/parser.tab.cpp"
    break;

  case 55: /* inheritance_specifier: IDENTIFIER  */
#line 350 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2911 "build/parser.tab.cpp"
    break;

  case 56: /* inheritance_specifier: TYPE_NAME  */
#line 356 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2922 "build/parser.tab.cpp"
    break;

  case 57: /* member_decl_list: member_item  */
#line 367 "../phase2-parser/src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 2932 "build/parser.tab.cpp"
    break;

  case 58: /* member_decl_list: member_decl_list member_item  */
#line 372 "../phase2-parser/src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 2946 "build/parser.tab.cpp"
    break;

  case 59: /* member_item: declaration  */
#line 384 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2952 "build/parser.tab.cpp"
    break;

  case 60: /* member_item: function_definition  */
#line 385 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2958 "build/parser.tab.cpp"
    break;

  case 61: /* member_item: access_specifier ':'  */
#line 386 "../phase2-parser/src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 2964 "build/parser.tab.cpp"
    break;

  case 62: /* member_item: constructor_def  */
#line 387 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 2970 "build/parser.tab.cpp"
    break;

  case 63: /* member_item: destructor_def  */
#line 388 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 2976 "build/parser.tab.cpp"
    break;

  case 64: /* $@7: %empty  */
#line 395 "../phase2-parser/src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 2982 "build/parser.tab.cpp"
    break;

  case 65: /* constructor_head: IDENTIFIER '(' $@7 parameter_list_opt ')'  */
#line 395 "../phase2-parser/src/parser.y"
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
#line 3001 "build/parser.tab.cpp"
    break;

  case 66: /* constructor_def: constructor_head compound_stmt  */
#line 412 "../phase2-parser/src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3010 "build/parser.tab.cpp"
    break;

  case 67: /* constructor_def: constructor_head ';'  */
#line 416 "../phase2-parser/src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3019 "build/parser.tab.cpp"
    break;

  case 68: /* destructor_head: '~' IDENTIFIER '(' ')'  */
#line 423 "../phase2-parser/src/parser.y"
                             {
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          pushScope(currentClassName() + "::~" + yyvsp[-2].str + "()");
          yyval = yyvsp[-2];
      }
#line 3029 "build/parser.tab.cpp"
    break;

  case 69: /* destructor_def: destructor_head compound_stmt  */
#line 431 "../phase2-parser/src/parser.y"
                                    {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), yyvsp[0].node);
      }
#line 3038 "build/parser.tab.cpp"
    break;

  case 70: /* destructor_def: destructor_head ';'  */
#line 435 "../phase2-parser/src/parser.y"
                          {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), nullptr);
      }
#line 3047 "build/parser.tab.cpp"
    break;

  case 71: /* $@8: %empty  */
#line 443 "../phase2-parser/src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3057 "build/parser.tab.cpp"
    break;

  case 72: /* $@9: %empty  */
#line 447 "../phase2-parser/src/parser.y"
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
#line 3073 "build/parser.tab.cpp"
    break;

  case 73: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@8 parameter_list_opt ')' $@9 compound_stmt  */
#line 457 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3083 "build/parser.tab.cpp"
    break;

  case 74: /* $@10: %empty  */
#line 462 "../phase2-parser/src/parser.y"
                                                {
          setCategory(yyvsp[-5].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-5].str)));
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          enterClass(yyvsp[-5].str);
          pushScope(yyvsp[-5].str + "::~" + yyvsp[-2].str + "()");
      }
#line 3094 "build/parser.tab.cpp"
    break;

  case 75: /* out_of_class_special: TYPE_NAME SCOPE_RES '~' TYPE_NAME '(' ')' $@10 compound_stmt  */
#line 467 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-4].str, yyvsp[-4].idx, yyvsp[-7].str, yyvsp[0].node);
          leaveClass();
      }
#line 3104 "build/parser.tab.cpp"
    break;

  case 79: /* init_declarator_list_opt: %empty  */
#line 481 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3110 "build/parser.tab.cpp"
    break;

  case 80: /* init_declarator_list_opt: init_declarator_list  */
#line 482 "../phase2-parser/src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3116 "build/parser.tab.cpp"
    break;

  case 81: /* init_declarator_list: init_declarator  */
#line 486 "../phase2-parser/src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3122 "build/parser.tab.cpp"
    break;

  case 82: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 487 "../phase2-parser/src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3128 "build/parser.tab.cpp"
    break;

  case 83: /* init_declarator: declarator  */
#line 491 "../phase2-parser/src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3134 "build/parser.tab.cpp"
    break;

  case 84: /* init_declarator: declarator '=' initializer  */
#line 492 "../phase2-parser/src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3140 "build/parser.tab.cpp"
    break;

  case 85: /* initializer: assignment_expr  */
#line 496 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3146 "build/parser.tab.cpp"
    break;

  case 86: /* initializer: '{' '}'  */
#line 497 "../phase2-parser/src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3152 "build/parser.tab.cpp"
    break;

  case 87: /* initializer: '{' initializer_list '}'  */
#line 498 "../phase2-parser/src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3162 "build/parser.tab.cpp"
    break;

  case 88: /* initializer: '{' initializer_list ',' '}'  */
#line 503 "../phase2-parser/src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3172 "build/parser.tab.cpp"
    break;

  case 89: /* initializer_list: initializer_item  */
#line 511 "../phase2-parser/src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3178 "build/parser.tab.cpp"
    break;

  case 90: /* initializer_list: initializer_list ',' initializer_item  */
#line 512 "../phase2-parser/src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3184 "build/parser.tab.cpp"
    break;

  case 91: /* initializer_item: initializer  */
#line 516 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3190 "build/parser.tab.cpp"
    break;

  case 92: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 517 "../phase2-parser/src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3198 "build/parser.tab.cpp"
    break;

  case 93: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 520 "../phase2-parser/src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3206 "build/parser.tab.cpp"
    break;

  case 94: /* pointer: '*'  */
#line 526 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3212 "build/parser.tab.cpp"
    break;

  case 95: /* pointer: '&'  */
#line 527 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3218 "build/parser.tab.cpp"
    break;

  case 96: /* pointer: pointer '*'  */
#line 528 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3224 "build/parser.tab.cpp"
    break;

  case 97: /* pointer: pointer '&'  */
#line 529 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3230 "build/parser.tab.cpp"
    break;

  case 98: /* pointer: pointer CONST  */
#line 530 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3236 "build/parser.tab.cpp"
    break;

  case 99: /* declarator: pointer direct_declarator  */
#line 534 "../phase2-parser/src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3247 "build/parser.tab.cpp"
    break;

  case 100: /* declarator: direct_declarator  */
#line 540 "../phase2-parser/src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3253 "build/parser.tab.cpp"
    break;

  case 101: /* abstract_declarator: pointer  */
#line 546 "../phase2-parser/src/parser.y"
              { yyval = yyvsp[0]; }
#line 3259 "build/parser.tab.cpp"
    break;

  case 102: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 547 "../phase2-parser/src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3270 "build/parser.tab.cpp"
    break;

  case 103: /* abstract_declarator: direct_abstract_declarator  */
#line 553 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3276 "build/parser.tab.cpp"
    break;

  case 104: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 557 "../phase2-parser/src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3290 "build/parser.tab.cpp"
    break;

  case 105: /* direct_abstract_declarator: '[' ']'  */
#line 566 "../phase2-parser/src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3296 "build/parser.tab.cpp"
    break;

  case 106: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 567 "../phase2-parser/src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3302 "build/parser.tab.cpp"
    break;

  case 107: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 568 "../phase2-parser/src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3308 "build/parser.tab.cpp"
    break;

  case 108: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 569 "../phase2-parser/src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3314 "build/parser.tab.cpp"
    break;

  case 109: /* direct_declarator: IDENTIFIER  */
#line 573 "../phase2-parser/src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3323 "build/parser.tab.cpp"
    break;

  case 110: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 577 "../phase2-parser/src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3335 "build/parser.tab.cpp"
    break;

  case 111: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 584 "../phase2-parser/src/parser.y"
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
#line 3352 "build/parser.tab.cpp"
    break;

  case 112: /* direct_declarator: '(' declarator ')'  */
#line 596 "../phase2-parser/src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3366 "build/parser.tab.cpp"
    break;

  case 113: /* direct_declarator: operator_function_id  */
#line 605 "../phase2-parser/src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3375 "build/parser.tab.cpp"
    break;

  case 114: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 609 "../phase2-parser/src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3387 "build/parser.tab.cpp"
    break;

  case 115: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 616 "../phase2-parser/src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3399 "build/parser.tab.cpp"
    break;

  case 116: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 623 "../phase2-parser/src/parser.y"
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
#line 3423 "build/parser.tab.cpp"
    break;

  case 117: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 642 "../phase2-parser/src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3435 "build/parser.tab.cpp"
    break;

  case 118: /* direct_declarator: direct_declarator '[' ']'  */
#line 649 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3441 "build/parser.tab.cpp"
    break;

  case 119: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 650 "../phase2-parser/src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3447 "build/parser.tab.cpp"
    break;

  case 120: /* operator_function_id: OPERATOR overloadable_operator  */
#line 655 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3453 "build/parser.tab.cpp"
    break;

  case 121: /* overloadable_operator: '+'  */
#line 659 "../phase2-parser/src/parser.y"
          { yyval.str = "+"; }
#line 3459 "build/parser.tab.cpp"
    break;

  case 122: /* overloadable_operator: '-'  */
#line 659 "../phase2-parser/src/parser.y"
                                  { yyval.str = "-"; }
#line 3465 "build/parser.tab.cpp"
    break;

  case 123: /* overloadable_operator: '*'  */
#line 659 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "*"; }
#line 3471 "build/parser.tab.cpp"
    break;

  case 124: /* overloadable_operator: '/'  */
#line 659 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3477 "build/parser.tab.cpp"
    break;

  case 125: /* overloadable_operator: '%'  */
#line 660 "../phase2-parser/src/parser.y"
          { yyval.str = "%"; }
#line 3483 "build/parser.tab.cpp"
    break;

  case 126: /* overloadable_operator: '^'  */
#line 660 "../phase2-parser/src/parser.y"
                                  { yyval.str = "^"; }
#line 3489 "build/parser.tab.cpp"
    break;

  case 127: /* overloadable_operator: '&'  */
#line 660 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "&"; }
#line 3495 "build/parser.tab.cpp"
    break;

  case 128: /* overloadable_operator: '|'  */
#line 660 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3501 "build/parser.tab.cpp"
    break;

  case 129: /* overloadable_operator: '~'  */
#line 661 "../phase2-parser/src/parser.y"
          { yyval.str = "~"; }
#line 3507 "build/parser.tab.cpp"
    break;

  case 130: /* overloadable_operator: '!'  */
#line 661 "../phase2-parser/src/parser.y"
                                  { yyval.str = "!"; }
#line 3513 "build/parser.tab.cpp"
    break;

  case 131: /* overloadable_operator: '='  */
#line 661 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "="; }
#line 3519 "build/parser.tab.cpp"
    break;

  case 132: /* overloadable_operator: '<'  */
#line 661 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3525 "build/parser.tab.cpp"
    break;

  case 133: /* overloadable_operator: '>'  */
#line 662 "../phase2-parser/src/parser.y"
          { yyval.str = ">"; }
#line 3531 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: EQ_OP  */
#line 662 "../phase2-parser/src/parser.y"
                                    { yyval.str = "=="; }
#line 3537 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: NE_OP  */
#line 662 "../phase2-parser/src/parser.y"
                                                               { yyval.str = "!="; }
#line 3543 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: LE_OP  */
#line 662 "../phase2-parser/src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3549 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: GE_OP  */
#line 663 "../phase2-parser/src/parser.y"
            { yyval.str = ">="; }
#line 3555 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: AND_OP  */
#line 663 "../phase2-parser/src/parser.y"
                                        { yyval.str = "&&"; }
#line 3561 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: OR_OP  */
#line 663 "../phase2-parser/src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3567 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: SHL  */
#line 663 "../phase2-parser/src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3573 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: SHR  */
#line 664 "../phase2-parser/src/parser.y"
          { yyval.str = ">>"; }
#line 3579 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: INC  */
#line 664 "../phase2-parser/src/parser.y"
                                   { yyval.str = "++"; }
#line 3585 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: DEC  */
#line 664 "../phase2-parser/src/parser.y"
                                                            { yyval.str = "--"; }
#line 3591 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: PLUS_ASSIGN  */
#line 665 "../phase2-parser/src/parser.y"
                  { yyval.str = "+="; }
#line 3597 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: MINUS_ASSIGN  */
#line 665 "../phase2-parser/src/parser.y"
                                                    { yyval.str = "-="; }
#line 3603 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: MUL_ASSIGN  */
#line 665 "../phase2-parser/src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3609 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: DIV_ASSIGN  */
#line 666 "../phase2-parser/src/parser.y"
                 { yyval.str = "/="; }
#line 3615 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: MOD_ASSIGN  */
#line 666 "../phase2-parser/src/parser.y"
                                                 { yyval.str = "%="; }
#line 3621 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: AND_ASSIGN  */
#line 666 "../phase2-parser/src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3627 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: OR_ASSIGN  */
#line 667 "../phase2-parser/src/parser.y"
                { yyval.str = "|="; }
#line 3633 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: XOR_ASSIGN  */
#line 667 "../phase2-parser/src/parser.y"
                                                { yyval.str = "^="; }
#line 3639 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: SHL_ASSIGN  */
#line 667 "../phase2-parser/src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3645 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: SHR_ASSIGN  */
#line 668 "../phase2-parser/src/parser.y"
                 { yyval.str = ">>="; }
#line 3651 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: '[' ']'  */
#line 668 "../phase2-parser/src/parser.y"
                                               { yyval.str = "[]"; }
#line 3657 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: '(' ')'  */
#line 668 "../phase2-parser/src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3663 "build/parser.tab.cpp"
    break;

  case 156: /* param_scope: %empty  */
#line 675 "../phase2-parser/src/parser.y"
                                           { pushScope(); }
#line 3669 "build/parser.tab.cpp"
    break;

  case 157: /* constructor_args: assignment_expr  */
#line 679 "../phase2-parser/src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3675 "build/parser.tab.cpp"
    break;

  case 158: /* constructor_args: constructor_args ',' assignment_expr  */
#line 680 "../phase2-parser/src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3681 "build/parser.tab.cpp"
    break;

  case 159: /* parameter_list_opt: %empty  */
#line 684 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3687 "build/parser.tab.cpp"
    break;

  case 160: /* parameter_list_opt: parameter_list  */
#line 685 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3693 "build/parser.tab.cpp"
    break;

  case 161: /* parameter_list: parameter_decl  */
#line 689 "../phase2-parser/src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3702 "build/parser.tab.cpp"
    break;

  case 162: /* parameter_list: parameter_list ',' parameter_decl  */
#line 693 "../phase2-parser/src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3711 "build/parser.tab.cpp"
    break;

  case 163: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 697 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3717 "build/parser.tab.cpp"
    break;

  case 164: /* parameter_decl: declaration_specifiers declarator  */
#line 701 "../phase2-parser/src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3727 "build/parser.tab.cpp"
    break;

  case 165: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 706 "../phase2-parser/src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3737 "build/parser.tab.cpp"
    break;

  case 166: /* parameter_decl: declaration_specifiers  */
#line 711 "../phase2-parser/src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3747 "build/parser.tab.cpp"
    break;

  case 167: /* $@11: %empty  */
#line 719 "../phase2-parser/src/parser.y"
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
#line 3786 "build/parser.tab.cpp"
    break;

  case 168: /* function_definition: declaration_specifiers declarator $@11 '{' block_item_list_opt '}'  */
#line 752 "../phase2-parser/src/parser.y"
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
#line 3816 "build/parser.tab.cpp"
    break;

  case 169: /* statement: compound_stmt  */
#line 780 "../phase2-parser/src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3822 "build/parser.tab.cpp"
    break;

  case 170: /* statement: expr_stmt  */
#line 781 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3828 "build/parser.tab.cpp"
    break;

  case 171: /* statement: selection_stmt  */
#line 782 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3834 "build/parser.tab.cpp"
    break;

  case 172: /* statement: iteration_stmt  */
#line 783 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3840 "build/parser.tab.cpp"
    break;

  case 173: /* statement: jump_stmt  */
#line 784 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3846 "build/parser.tab.cpp"
    break;

  case 174: /* statement: labeled_stmt  */
#line 785 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3852 "build/parser.tab.cpp"
    break;

  case 175: /* statement: declaration  */
#line 786 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3858 "build/parser.tab.cpp"
    break;

  case 176: /* statement: error ';'  */
#line 787 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3864 "build/parser.tab.cpp"
    break;

  case 177: /* statement: error '}'  */
#line 788 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3870 "build/parser.tab.cpp"
    break;

  case 178: /* $@12: %empty  */
#line 792 "../phase2-parser/src/parser.y"
          { pushScope(); }
#line 3876 "build/parser.tab.cpp"
    break;

  case 179: /* compound_stmt: '{' $@12 block_item_list_opt '}'  */
#line 792 "../phase2-parser/src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 3887 "build/parser.tab.cpp"
    break;

  case 180: /* block_item_list_opt: %empty  */
#line 801 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3893 "build/parser.tab.cpp"
    break;

  case 181: /* block_item_list_opt: block_item_list  */
#line 802 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[0]; }
#line 3899 "build/parser.tab.cpp"
    break;

  case 182: /* block_item_list: statement  */
#line 806 "../phase2-parser/src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3905 "build/parser.tab.cpp"
    break;

  case 183: /* block_item_list: block_item_list statement  */
#line 807 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3911 "build/parser.tab.cpp"
    break;

  case 184: /* expr_stmt: ';'  */
#line 811 "../phase2-parser/src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 3917 "build/parser.tab.cpp"
    break;

  case 185: /* expr_stmt: expr ';'  */
#line 812 "../phase2-parser/src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 3923 "build/parser.tab.cpp"
    break;

  case 186: /* selection_stmt: IF '(' expr ')' statement  */
#line 816 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3931 "build/parser.tab.cpp"
    break;

  case 187: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 819 "../phase2-parser/src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 3939 "build/parser.tab.cpp"
    break;

  case 188: /* $@13: %empty  */
#line 822 "../phase2-parser/src/parser.y"
                          { hintScope("switch"); }
#line 3945 "build/parser.tab.cpp"
    break;

  case 189: /* selection_stmt: SWITCH '(' expr ')' $@13 compound_stmt  */
#line 822 "../phase2-parser/src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 3953 "build/parser.tab.cpp"
    break;

  case 190: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 828 "../phase2-parser/src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 3961 "build/parser.tab.cpp"
    break;

  case 191: /* labeled_stmt: DEFAULT ':' statement  */
#line 831 "../phase2-parser/src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3969 "build/parser.tab.cpp"
    break;

  case 192: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 834 "../phase2-parser/src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3979 "build/parser.tab.cpp"
    break;

  case 193: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 842 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3987 "build/parser.tab.cpp"
    break;

  case 194: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 845 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 3995 "build/parser.tab.cpp"
    break;

  case 195: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 852 "../phase2-parser/src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4004 "build/parser.tab.cpp"
    break;

  case 196: /* iteration_stmt: DO statement error ';'  */
#line 856 "../phase2-parser/src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4013 "build/parser.tab.cpp"
    break;

  case 197: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 860 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4021 "build/parser.tab.cpp"
    break;

  case 198: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 863 "../phase2-parser/src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4030 "build/parser.tab.cpp"
    break;

  case 199: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 867 "../phase2-parser/src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4039 "build/parser.tab.cpp"
    break;

  case 200: /* for_open: FOR '('  */
#line 876 "../phase2-parser/src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4045 "build/parser.tab.cpp"
    break;

  case 201: /* for_incr_opt: %empty  */
#line 880 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4051 "build/parser.tab.cpp"
    break;

  case 202: /* for_incr_opt: expr  */
#line 881 "../phase2-parser/src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4057 "build/parser.tab.cpp"
    break;

  case 203: /* jump_stmt: BREAK ';'  */
#line 885 "../phase2-parser/src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4063 "build/parser.tab.cpp"
    break;

  case 204: /* jump_stmt: CONTINUE ';'  */
#line 886 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4069 "build/parser.tab.cpp"
    break;

  case 205: /* jump_stmt: RETURN ';'  */
#line 887 "../phase2-parser/src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4075 "build/parser.tab.cpp"
    break;

  case 206: /* jump_stmt: RETURN expr ';'  */
#line 888 "../phase2-parser/src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4081 "build/parser.tab.cpp"
    break;

  case 207: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 889 "../phase2-parser/src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4093 "build/parser.tab.cpp"
    break;

  case 208: /* expr: assignment_expr  */
#line 899 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4099 "build/parser.tab.cpp"
    break;

  case 209: /* expr: expr ',' assignment_expr  */
#line 900 "../phase2-parser/src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4105 "build/parser.tab.cpp"
    break;

  case 210: /* assignment_expr: binary_expr  */
#line 904 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4111 "build/parser.tab.cpp"
    break;

  case 211: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 905 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4119 "build/parser.tab.cpp"
    break;

  case 212: /* assign_op: '='  */
#line 911 "../phase2-parser/src/parser.y"
                   { yyval.str = "="; }
#line 4125 "build/parser.tab.cpp"
    break;

  case 213: /* assign_op: PLUS_ASSIGN  */
#line 912 "../phase2-parser/src/parser.y"
                   { yyval.str = "+="; }
#line 4131 "build/parser.tab.cpp"
    break;

  case 214: /* assign_op: MINUS_ASSIGN  */
#line 913 "../phase2-parser/src/parser.y"
                   { yyval.str = "-="; }
#line 4137 "build/parser.tab.cpp"
    break;

  case 215: /* assign_op: MUL_ASSIGN  */
#line 914 "../phase2-parser/src/parser.y"
                   { yyval.str = "*="; }
#line 4143 "build/parser.tab.cpp"
    break;

  case 216: /* assign_op: DIV_ASSIGN  */
#line 915 "../phase2-parser/src/parser.y"
                   { yyval.str = "/="; }
#line 4149 "build/parser.tab.cpp"
    break;

  case 217: /* assign_op: MOD_ASSIGN  */
#line 916 "../phase2-parser/src/parser.y"
                   { yyval.str = "%="; }
#line 4155 "build/parser.tab.cpp"
    break;

  case 218: /* assign_op: AND_ASSIGN  */
#line 917 "../phase2-parser/src/parser.y"
                   { yyval.str = "&="; }
#line 4161 "build/parser.tab.cpp"
    break;

  case 219: /* assign_op: OR_ASSIGN  */
#line 918 "../phase2-parser/src/parser.y"
                   { yyval.str = "|="; }
#line 4167 "build/parser.tab.cpp"
    break;

  case 220: /* assign_op: XOR_ASSIGN  */
#line 919 "../phase2-parser/src/parser.y"
                   { yyval.str = "^="; }
#line 4173 "build/parser.tab.cpp"
    break;

  case 221: /* assign_op: SHL_ASSIGN  */
#line 920 "../phase2-parser/src/parser.y"
                   { yyval.str = "<<="; }
#line 4179 "build/parser.tab.cpp"
    break;

  case 222: /* assign_op: SHR_ASSIGN  */
#line 921 "../phase2-parser/src/parser.y"
                   { yyval.str = ">>="; }
#line 4185 "build/parser.tab.cpp"
    break;

  case 223: /* constant_expr: binary_expr  */
#line 925 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4191 "build/parser.tab.cpp"
    break;

  case 224: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 929 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4197 "build/parser.tab.cpp"
    break;

  case 225: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 930 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4203 "build/parser.tab.cpp"
    break;

  case 226: /* binary_expr: binary_expr '|' binary_expr  */
#line 931 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4209 "build/parser.tab.cpp"
    break;

  case 227: /* binary_expr: binary_expr '^' binary_expr  */
#line 932 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4215 "build/parser.tab.cpp"
    break;

  case 228: /* binary_expr: binary_expr '&' binary_expr  */
#line 933 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4221 "build/parser.tab.cpp"
    break;

  case 229: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 934 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4227 "build/parser.tab.cpp"
    break;

  case 230: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 935 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4233 "build/parser.tab.cpp"
    break;

  case 231: /* binary_expr: binary_expr '<' binary_expr  */
#line 936 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4239 "build/parser.tab.cpp"
    break;

  case 232: /* binary_expr: binary_expr '>' binary_expr  */
#line 937 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4245 "build/parser.tab.cpp"
    break;

  case 233: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 938 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4251 "build/parser.tab.cpp"
    break;

  case 234: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 939 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4257 "build/parser.tab.cpp"
    break;

  case 235: /* binary_expr: binary_expr SHL binary_expr  */
#line 940 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4263 "build/parser.tab.cpp"
    break;

  case 236: /* binary_expr: binary_expr SHR binary_expr  */
#line 941 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4269 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr '+' binary_expr  */
#line 942 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4275 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr '-' binary_expr  */
#line 943 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4281 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr '*' binary_expr  */
#line 944 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4287 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr '/' binary_expr  */
#line 945 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4293 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr '%' binary_expr  */
#line 946 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4299 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 947 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4307 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: unary_expr  */
#line 950 "../phase2-parser/src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4313 "build/parser.tab.cpp"
    break;

  case 244: /* unary_expr: postfix_expr  */
#line 954 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4319 "build/parser.tab.cpp"
    break;

  case 245: /* unary_expr: INC unary_expr  */
#line 955 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4325 "build/parser.tab.cpp"
    break;

  case 246: /* unary_expr: DEC unary_expr  */
#line 956 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4331 "build/parser.tab.cpp"
    break;

  case 247: /* unary_expr: '&' unary_expr  */
#line 957 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4337 "build/parser.tab.cpp"
    break;

  case 248: /* unary_expr: '*' unary_expr  */
#line 958 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4343 "build/parser.tab.cpp"
    break;

  case 249: /* unary_expr: '+' unary_expr  */
#line 959 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4349 "build/parser.tab.cpp"
    break;

  case 250: /* unary_expr: '-' unary_expr  */
#line 960 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4355 "build/parser.tab.cpp"
    break;

  case 251: /* unary_expr: '!' unary_expr  */
#line 961 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4361 "build/parser.tab.cpp"
    break;

  case 252: /* unary_expr: '~' unary_expr  */
#line 962 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4367 "build/parser.tab.cpp"
    break;

  case 253: /* unary_expr: '(' type_name ')' unary_expr  */
#line 963 "../phase2-parser/src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4376 "build/parser.tab.cpp"
    break;

  case 254: /* unary_expr: SIZEOF unary_expr  */
#line 967 "../phase2-parser/src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4382 "build/parser.tab.cpp"
    break;

  case 255: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 968 "../phase2-parser/src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4391 "build/parser.tab.cpp"
    break;

  case 256: /* type_name: type_name_specifiers  */
#line 975 "../phase2-parser/src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4400 "build/parser.tab.cpp"
    break;

  case 257: /* type_name: type_name_specifiers abstract_declarator  */
#line 979 "../phase2-parser/src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4409 "build/parser.tab.cpp"
    break;

  case 258: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 986 "../phase2-parser/src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4421 "build/parser.tab.cpp"
    break;

  case 259: /* type_name_specifiers: type_name_specifier  */
#line 993 "../phase2-parser/src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4427 "build/parser.tab.cpp"
    break;

  case 260: /* type_name_specifier: INT  */
#line 997 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4433 "build/parser.tab.cpp"
    break;

  case 261: /* type_name_specifier: CHAR  */
#line 998 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4439 "build/parser.tab.cpp"
    break;

  case 262: /* type_name_specifier: FLOAT  */
#line 999 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4445 "build/parser.tab.cpp"
    break;

  case 263: /* type_name_specifier: DOUBLE  */
#line 1000 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4451 "build/parser.tab.cpp"
    break;

  case 264: /* type_name_specifier: VOID  */
#line 1001 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4457 "build/parser.tab.cpp"
    break;

  case 265: /* type_name_specifier: BOOL  */
#line 1002 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4463 "build/parser.tab.cpp"
    break;

  case 266: /* type_name_specifier: SHORT  */
#line 1003 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4469 "build/parser.tab.cpp"
    break;

  case 267: /* type_name_specifier: LONG  */
#line 1004 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4475 "build/parser.tab.cpp"
    break;

  case 268: /* type_name_specifier: SIGNED  */
#line 1005 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4481 "build/parser.tab.cpp"
    break;

  case 269: /* type_name_specifier: UNSIGNED  */
#line 1006 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4487 "build/parser.tab.cpp"
    break;

  case 270: /* type_name_specifier: VA_LIST  */
#line 1007 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4493 "build/parser.tab.cpp"
    break;

  case 271: /* type_name_specifier: CONST  */
#line 1008 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4499 "build/parser.tab.cpp"
    break;

  case 272: /* type_name_specifier: TYPE_NAME  */
#line 1009 "../phase2-parser/src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4513 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1018 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4524 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1024 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4535 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1030 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4546 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1036 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4557 "build/parser.tab.cpp"
    break;

  case 277: /* postfix_expr: primary_expr  */
#line 1045 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4563 "build/parser.tab.cpp"
    break;

  case 278: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1046 "../phase2-parser/src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4569 "build/parser.tab.cpp"
    break;

  case 279: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1047 "../phase2-parser/src/parser.y"
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
#line 4609 "build/parser.tab.cpp"
    break;

  case 280: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1082 "../phase2-parser/src/parser.y"
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
#line 4624 "build/parser.tab.cpp"
    break;

  case 281: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1092 "../phase2-parser/src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4636 "build/parser.tab.cpp"
    break;

  case 282: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1099 "../phase2-parser/src/parser.y"
                                                        {
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4646 "build/parser.tab.cpp"
    break;

  case 283: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1104 "../phase2-parser/src/parser.y"
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
#line 4661 "build/parser.tab.cpp"
    break;

  case 284: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1114 "../phase2-parser/src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4667 "build/parser.tab.cpp"
    break;

  case 285: /* postfix_expr: postfix_expr INC  */
#line 1115 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4673 "build/parser.tab.cpp"
    break;

  case 286: /* postfix_expr: postfix_expr DEC  */
#line 1116 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4679 "build/parser.tab.cpp"
    break;

  case 287: /* postfix_expr: builtin_call  */
#line 1117 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4685 "build/parser.tab.cpp"
    break;

  case 288: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1121 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4691 "build/parser.tab.cpp"
    break;

  case 289: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1122 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4697 "build/parser.tab.cpp"
    break;

  case 290: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1123 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4703 "build/parser.tab.cpp"
    break;

  case 291: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1124 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4709 "build/parser.tab.cpp"
    break;

  case 292: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1125 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4715 "build/parser.tab.cpp"
    break;

  case 293: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1126 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4721 "build/parser.tab.cpp"
    break;

  case 294: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1127 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4727 "build/parser.tab.cpp"
    break;

  case 295: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1128 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4733 "build/parser.tab.cpp"
    break;

  case 296: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1129 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4739 "build/parser.tab.cpp"
    break;

  case 297: /* constructor_args_opt: %empty  */
#line 1133 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4745 "build/parser.tab.cpp"
    break;

  case 298: /* constructor_args_opt: constructor_args  */
#line 1134 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4751 "build/parser.tab.cpp"
    break;

  case 299: /* argument_list_opt: %empty  */
#line 1138 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4757 "build/parser.tab.cpp"
    break;

  case 300: /* argument_list_opt: argument_list  */
#line 1139 "../phase2-parser/src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4763 "build/parser.tab.cpp"
    break;

  case 301: /* argument_list: argument  */
#line 1143 "../phase2-parser/src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4769 "build/parser.tab.cpp"
    break;

  case 302: /* argument_list: argument_list ',' argument  */
#line 1144 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4775 "build/parser.tab.cpp"
    break;

  case 303: /* argument: assignment_expr  */
#line 1148 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4781 "build/parser.tab.cpp"
    break;

  case 304: /* argument: type_name  */
#line 1149 "../phase2-parser/src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4790 "build/parser.tab.cpp"
    break;

  case 305: /* primary_expr: IDENTIFIER  */
#line 1156 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 4804 "build/parser.tab.cpp"
    break;

  case 306: /* primary_expr: INT_LITERAL  */
#line 1165 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4810 "build/parser.tab.cpp"
    break;

  case 307: /* primary_expr: FLOAT_LITERAL  */
#line 1166 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4816 "build/parser.tab.cpp"
    break;

  case 308: /* primary_expr: CHAR_LITERAL  */
#line 1167 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4822 "build/parser.tab.cpp"
    break;

  case 309: /* primary_expr: string_literal  */
#line 1168 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4828 "build/parser.tab.cpp"
    break;

  case 310: /* primary_expr: BOOL_LITERAL  */
#line 1169 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4834 "build/parser.tab.cpp"
    break;

  case 311: /* primary_expr: THIS  */
#line 1170 "../phase2-parser/src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 4840 "build/parser.tab.cpp"
    break;

  case 312: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1171 "../phase2-parser/src/parser.y"
                                             {
          /* `Dog(4)`: a temporary object (for a scalar type, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4849 "build/parser.tab.cpp"
    break;

  case 313: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1175 "../phase2-parser/src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4859 "build/parser.tab.cpp"
    break;

  case 314: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1182 "../phase2-parser/src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4865 "build/parser.tab.cpp"
    break;

  case 315: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1183 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4871 "build/parser.tab.cpp"
    break;

  case 316: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1184 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4877 "build/parser.tab.cpp"
    break;

  case 317: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1185 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4883 "build/parser.tab.cpp"
    break;

  case 318: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1186 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4889 "build/parser.tab.cpp"
    break;

  case 319: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1187 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4895 "build/parser.tab.cpp"
    break;

  case 320: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1188 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4901 "build/parser.tab.cpp"
    break;

  case 321: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1189 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4907 "build/parser.tab.cpp"
    break;

  case 322: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1190 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4913 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1191 "../phase2-parser/src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4919 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1192 "../phase2-parser/src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 4931 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: '(' expr ')'  */
#line 1199 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 4937 "build/parser.tab.cpp"
    break;

  case 326: /* string_literal: STRING_LITERAL  */
#line 1204 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4943 "build/parser.tab.cpp"
    break;

  case 327: /* string_literal: string_literal STRING_LITERAL  */
#line 1205 "../phase2-parser/src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 4953 "build/parser.tab.cpp"
    break;


#line 4957 "build/parser.tab.cpp"

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

#line 1212 "../phase2-parser/src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
