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
  YYSYMBOL_REGISTER = 22,                  /* REGISTER  */
  YYSYMBOL_CONST = 23,                     /* CONST  */
  YYSYMBOL_VOLATILE = 24,                  /* VOLATILE  */
  YYSYMBOL_IF = 25,                        /* IF  */
  YYSYMBOL_ELSE = 26,                      /* ELSE  */
  YYSYMBOL_FOR = 27,                       /* FOR  */
  YYSYMBOL_WHILE = 28,                     /* WHILE  */
  YYSYMBOL_DO = 29,                        /* DO  */
  YYSYMBOL_UNTIL = 30,                     /* UNTIL  */
  YYSYMBOL_SWITCH = 31,                    /* SWITCH  */
  YYSYMBOL_CASE = 32,                      /* CASE  */
  YYSYMBOL_DEFAULT = 33,                   /* DEFAULT  */
  YYSYMBOL_BREAK = 34,                     /* BREAK  */
  YYSYMBOL_CONTINUE = 35,                  /* CONTINUE  */
  YYSYMBOL_GOTO = 36,                      /* GOTO  */
  YYSYMBOL_RETURN = 37,                    /* RETURN  */
  YYSYMBOL_PRINTF = 38,                    /* PRINTF  */
  YYSYMBOL_SCANF = 39,                     /* SCANF  */
  YYSYMBOL_MALLOC = 40,                    /* MALLOC  */
  YYSYMBOL_FREE = 41,                      /* FREE  */
  YYSYMBOL_CALLOC = 42,                    /* CALLOC  */
  YYSYMBOL_REALLOC = 43,                   /* REALLOC  */
  YYSYMBOL_BOOL = 44,                      /* BOOL  */
  YYSYMBOL_NEW = 45,                       /* NEW  */
  YYSYMBOL_DELETE = 46,                    /* DELETE  */
  YYSYMBOL_SIZEOF = 47,                    /* SIZEOF  */
  YYSYMBOL_VA_LIST = 48,                   /* VA_LIST  */
  YYSYMBOL_VA_START = 49,                  /* VA_START  */
  YYSYMBOL_VA_ARG = 50,                    /* VA_ARG  */
  YYSYMBOL_VA_END = 51,                    /* VA_END  */
  YYSYMBOL_OPERATOR = 52,                  /* OPERATOR  */
  YYSYMBOL_DELETE_ARRAY = 53,              /* DELETE_ARRAY  */
  YYSYMBOL_FCAST = 54,                     /* FCAST  */
  YYSYMBOL_ABSTRACT_LPAREN = 55,           /* ABSTRACT_LPAREN  */
  YYSYMBOL_IDENTIFIER = 56,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 57,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 58,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 59,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 60,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 61,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 62,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 63,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 64,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 65,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 66,                       /* INC  */
  YYSYMBOL_DEC = 67,                       /* DEC  */
  YYSYMBOL_SHL = 68,                       /* SHL  */
  YYSYMBOL_SHR = 69,                       /* SHR  */
  YYSYMBOL_LE_OP = 70,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 71,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 72,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 73,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 74,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 75,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 76,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 77,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 78,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 79,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 80,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 81,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 82,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 83,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 84,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 85,                /* SHR_ASSIGN  */
  YYSYMBOL_PREFER_EXPRESSION = 86,         /* PREFER_EXPRESSION  */
  YYSYMBOL_NEW_TYPE_END = 87,              /* NEW_TYPE_END  */
  YYSYMBOL_88_ = 88,                       /* '='  */
  YYSYMBOL_89_ = 89,                       /* '?'  */
  YYSYMBOL_90_ = 90,                       /* ':'  */
  YYSYMBOL_91_ = 91,                       /* '|'  */
  YYSYMBOL_92_ = 92,                       /* '^'  */
  YYSYMBOL_93_ = 93,                       /* '&'  */
  YYSYMBOL_94_ = 94,                       /* '<'  */
  YYSYMBOL_95_ = 95,                       /* '>'  */
  YYSYMBOL_96_ = 96,                       /* '+'  */
  YYSYMBOL_97_ = 97,                       /* '-'  */
  YYSYMBOL_98_ = 98,                       /* '*'  */
  YYSYMBOL_99_ = 99,                       /* '/'  */
  YYSYMBOL_100_ = 100,                     /* '%'  */
  YYSYMBOL_UMINUS = 101,                   /* UMINUS  */
  YYSYMBOL_ADDR = 102,                     /* ADDR  */
  YYSYMBOL_DEREF = 103,                    /* DEREF  */
  YYSYMBOL_CAST = 104,                     /* CAST  */
  YYSYMBOL_105_ = 105,                     /* '!'  */
  YYSYMBOL_106_ = 106,                     /* '~'  */
  YYSYMBOL_107_ = 107,                     /* '.'  */
  YYSYMBOL_108_ = 108,                     /* '('  */
  YYSYMBOL_109_ = 109,                     /* '['  */
  YYSYMBOL_SIZEOF_TYPE = 110,              /* SIZEOF_TYPE  */
  YYSYMBOL_PREFER_DECLARATION = 111,       /* PREFER_DECLARATION  */
  YYSYMBOL_IFX = 112,                      /* IFX  */
  YYSYMBOL_113_ = 113,                     /* ';'  */
  YYSYMBOL_114_ = 114,                     /* '}'  */
  YYSYMBOL_115_ = 115,                     /* '{'  */
  YYSYMBOL_116_ = 116,                     /* ','  */
  YYSYMBOL_117_ = 117,                     /* ')'  */
  YYSYMBOL_118_ = 118,                     /* ']'  */
  YYSYMBOL_YYACCEPT = 119,                 /* $accept  */
  YYSYMBOL_translation_unit = 120,         /* translation_unit  */
  YYSYMBOL_external_decl = 121,            /* external_decl  */
  YYSYMBOL_declaration = 122,              /* declaration  */
  YYSYMBOL_declaration_specifiers = 123,   /* declaration_specifiers  */
  YYSYMBOL_storage_or_type_specifier = 124, /* storage_or_type_specifier  */
  YYSYMBOL_type_specifier = 125,           /* type_specifier  */
  YYSYMBOL_tag_name = 126,                 /* tag_name  */
  YYSYMBOL_struct_or_class_specifier = 127, /* struct_or_class_specifier  */
  YYSYMBOL_128_1 = 128,                    /* $@1  */
  YYSYMBOL_129_2 = 129,                    /* $@2  */
  YYSYMBOL_130_3 = 130,                    /* @3  */
  YYSYMBOL_131_4 = 131,                    /* $@4  */
  YYSYMBOL_132_5 = 132,                    /* $@5  */
  YYSYMBOL_133_6 = 133,                    /* @6  */
  YYSYMBOL_member_decl_list_opt = 134,     /* member_decl_list_opt  */
  YYSYMBOL_inheritance_opt = 135,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 136, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 137,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 138,         /* member_decl_list  */
  YYSYMBOL_member_item = 139,              /* member_item  */
  YYSYMBOL_constructor_head = 140,         /* constructor_head  */
  YYSYMBOL_141_7 = 141,                    /* $@7  */
  YYSYMBOL_constructor_def = 142,          /* constructor_def  */
  YYSYMBOL_destructor_head = 143,          /* destructor_head  */
  YYSYMBOL_destructor_def = 144,           /* destructor_def  */
  YYSYMBOL_out_of_class_special = 145,     /* out_of_class_special  */
  YYSYMBOL_146_8 = 146,                    /* $@8  */
  YYSYMBOL_147_9 = 147,                    /* $@9  */
  YYSYMBOL_148_10 = 148,                   /* $@10  */
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
  YYSYMBOL_operator_function_id = 161,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 162,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 163,              /* param_scope  */
  YYSYMBOL_constructor_args = 164,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 165,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 166,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 167,           /* parameter_decl  */
  YYSYMBOL_function_definition = 168,      /* function_definition  */
  YYSYMBOL_169_11 = 169,                   /* $@11  */
  YYSYMBOL_statement = 170,                /* statement  */
  YYSYMBOL_compound_stmt = 171,            /* compound_stmt  */
  YYSYMBOL_172_12 = 172,                   /* $@12  */
  YYSYMBOL_block_item_list_opt = 173,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 174,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 175,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 176,           /* selection_stmt  */
  YYSYMBOL_177_13 = 177,                   /* $@13  */
  YYSYMBOL_labeled_stmt = 178,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 179,           /* iteration_stmt  */
  YYSYMBOL_for_open = 180,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 181,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 182,                /* jump_stmt  */
  YYSYMBOL_expr = 183,                     /* expr  */
  YYSYMBOL_assignment_expr = 184,          /* assignment_expr  */
  YYSYMBOL_assign_op = 185,                /* assign_op  */
  YYSYMBOL_constant_expr = 186,            /* constant_expr  */
  YYSYMBOL_binary_expr = 187,              /* binary_expr  */
  YYSYMBOL_unary_expr = 188,               /* unary_expr  */
  YYSYMBOL_type_name = 189,                /* type_name  */
  YYSYMBOL_new_type_id = 190,              /* new_type_id  */
  YYSYMBOL_new_pointer = 191,              /* new_pointer  */
  YYSYMBOL_new_array_dims = 192,           /* new_array_dims  */
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


#line 346 "build/parser.tab.cpp"

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
#define YYLAST   2439

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  119
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  84
/* YYNRULES -- Number of rules.  */
#define YYNRULES  341
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  605

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   349


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
       2,     2,     2,   105,     2,     2,     2,   100,    93,     2,
     108,   117,    98,    96,   116,    97,   107,    99,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    90,   113,
      94,    88,    95,    89,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   109,     2,   118,    92,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   115,    91,   114,   106,     2,     2,     2,
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
      85,    86,    87,   101,   102,   103,   104,   110,   111,   112
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   125,   125,   129,   137,   138,   139,   140,   141,   145,
     173,   188,   192,   193,   194,   195,   196,   197,   198,   199,
     203,   204,   205,   206,   207,   208,   209,   210,   211,   212,
     213,   214,   228,   235,   236,   240,   244,   240,   260,   260,
     274,   280,   286,   290,   286,   302,   302,   316,   322,   331,
     332,   336,   337,   341,   342,   349,   355,   361,   367,   378,
     383,   395,   396,   397,   398,   399,   406,   406,   423,   427,
     434,   442,   446,   454,   458,   454,   473,   473,   486,   487,
     488,   492,   493,   497,   498,   502,   503,   507,   508,   509,
     514,   522,   523,   527,   528,   531,   537,   538,   539,   540,
     541,   542,   546,   552,   558,   559,   565,   569,   578,   579,
     580,   581,   585,   589,   596,   608,   617,   621,   628,   635,
     654,   661,   662,   667,   671,   671,   671,   671,   672,   672,
     672,   672,   673,   673,   673,   673,   674,   674,   674,   674,
     675,   675,   675,   675,   676,   676,   676,   677,   677,   677,
     678,   678,   678,   679,   679,   679,   680,   680,   680,   687,
     691,   692,   696,   697,   701,   705,   709,   713,   718,   723,
     731,   731,   793,   794,   795,   796,   797,   798,   799,   800,
     801,   805,   805,   814,   815,   819,   820,   824,   825,   829,
     832,   835,   835,   841,   844,   847,   855,   858,   865,   869,
     873,   876,   880,   889,   893,   894,   898,   899,   900,   901,
     902,   912,   913,   917,   918,   924,   925,   926,   927,   928,
     929,   930,   931,   932,   933,   934,   938,   942,   943,   944,
     945,   946,   947,   948,   949,   950,   951,   952,   953,   954,
     955,   956,   957,   958,   959,   960,   963,   967,   968,   969,
     970,   971,   972,   973,   974,   975,   976,   980,   981,   985,
     989,   997,   998,  1002,  1006,  1015,  1019,  1023,  1027,  1036,
    1037,  1042,  1043,  1047,  1055,  1059,  1060,  1061,  1062,  1063,
    1064,  1065,  1066,  1067,  1068,  1069,  1070,  1071,  1072,  1081,
    1087,  1093,  1099,  1108,  1109,  1110,  1145,  1155,  1165,  1166,
    1167,  1168,  1172,  1173,  1174,  1175,  1176,  1177,  1178,  1179,
    1180,  1184,  1185,  1189,  1190,  1194,  1195,  1199,  1200,  1207,
    1216,  1217,  1218,  1219,  1220,  1221,  1222,  1226,  1233,  1234,
    1235,  1236,  1237,  1238,  1239,  1240,  1241,  1242,  1243,  1250,
    1255,  1256
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
  "AUTO", "EXTERN", "REGISTER", "CONST", "VOLATILE", "IF", "ELSE", "FOR",
  "WHILE", "DO", "UNTIL", "SWITCH", "CASE", "DEFAULT", "BREAK", "CONTINUE",
  "GOTO", "RETURN", "PRINTF", "SCANF", "MALLOC", "FREE", "CALLOC",
  "REALLOC", "BOOL", "NEW", "DELETE", "SIZEOF", "VA_LIST", "VA_START",
  "VA_ARG", "VA_END", "OPERATOR", "DELETE_ARRAY", "FCAST",
  "ABSTRACT_LPAREN", "IDENTIFIER", "TYPE_NAME", "INT_LITERAL",
  "FLOAT_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", "BOOL_LITERAL",
  "ARROW", "ELLIPSIS", "SCOPE_RES", "INC", "DEC", "SHL", "SHR", "LE_OP",
  "GE_OP", "EQ_OP", "NE_OP", "AND_OP", "OR_OP", "PLUS_ASSIGN",
  "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN",
  "OR_ASSIGN", "XOR_ASSIGN", "SHL_ASSIGN", "SHR_ASSIGN",
  "PREFER_EXPRESSION", "NEW_TYPE_END", "'='", "'?'", "':'", "'|'", "'^'",
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
  "unary_expr", "type_name", "new_type_id", "new_pointer",
  "new_array_dims", "type_name_specifiers", "type_name_specifier",
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

#define YYPACT_NINF (-406)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-185)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -406,  2185,  -406,   -42,  -406,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,    -4,    -2,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,   -14,  -406,  -406,   302,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,   -92,   -87,  -406,  -406,    63,
      76,  -406,  -406,   -37,  2254,    47,    50,  -406,  -406,   158,
    -406,    31,    44,  -406,   325,   -18,    -3,  -406,  1997,    40,
    1997,   118,   109,   166,  -406,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,  -406,  -406,   119,   134,  -406,
     -34,    39,    50,   138,  -406,   158,  -406,  -406,  -406,  -406,
      -3,  1314,   112,  2017,   502,  -406,  -406,  -406,   149,  -406,
     209,  -406,   153,  1997,  -406,    46,  -406,    94,  -406,   186,
    -406,  -406,   164,   217,   165,  -406,   174,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,   199,   180,   189,   210,   219,
     223,   227,   239,   248,   254,  -406,   255,   256,   257,   266,
     271,   275,   276,  2262,  1790,  1861,   277,   278,   280,  1790,
     282,  -406,   -15,  -406,  -406,  -406,  -406,  -406,  1790,  1790,
    1790,  1790,  1790,  1790,  1790,  1790,  1719,  1158,  -406,  -406,
    2296,   376,   233,  -406,  -406,   234,   850,  2240,    77,  -406,
    -406,   273,  -406,   284,  -406,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  1997,  -406,  -406,  -406,   281,  -406,   156,  -406,
    2240,   279,  1790,  1790,  1790,  1790,  1790,  1790,  1790,  1790,
    1790,  1719,  1719,  1719,  1719,  1719,  1719,  1790,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,  -406,  -406,   204,   207,  -406,
    -406,  -406,  -406,  -406,   285,   177,  -406,  -406,  1719,  -406,
    1719,  1719,  1719,  -406,  1790,   338,  1790,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,   180,   189,   210,   219,   223,
     227,   239,   248,   254,   276,   -15,   155,  -406,   286,   235,
     343,  1790,  -406,  -406,    60,  -406,  1790,  1790,  1790,  1790,
    1790,  1790,  1790,  1790,  1790,  1790,  1790,  1790,  1790,  1790,
    1790,  1790,  1790,  1790,  1790,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,  -406,  1790,   345,   346,  -406,
    -406,   348,  1719,  1790,  -406,   171,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,   297,   299,   300,  1080,   301,
     303,  1790,   322,   304,   311,   357,  1504,  -406,   324,   350,
    -406,  -406,   302,  -406,  -406,   312,   965,  -406,  -406,  -406,
    -406,  1427,  -406,    55,  1647,   308,   314,  -406,  1790,  -406,
    -406,  2240,   310,   850,   317,   217,  -406,  -406,  1997,   315,
    -406,   318,   319,   320,   321,   326,   327,   349,   352,   354,
     355,  -406,  -406,   356,   347,  -406,   358,   359,   361,   363,
     364,   365,  -406,  -406,  -406,  -406,  1790,  -406,  1790,    -9,
     353,  -406,   366,   386,   387,   397,   398,  -406,   399,  1790,
    -406,  1790,     5,   618,     1,  -406,   408,   340,   400,  2296,
    -406,  -406,  1236,   106,   106,    49,    49,   351,   351,   545,
    2306,    61,  2339,   750,  1612,    49,    49,    99,    99,  -406,
    -406,  -406,  -406,  -406,  -406,  -406,   403,   100,  -406,  -406,
    1790,  -406,  1790,    73,  1790,  1790,   377,  1080,  -406,  -406,
     409,  -406,    79,  1080,  -406,  -406,  1581,  1581,  -406,    64,
    -406,  -406,  -406,  2123,  -406,   404,  -406,   360,  -406,  -406,
     410,  -406,   411,  -406,  -406,  -406,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,  1719,  -406,  -406,  -406,  -406,  -406,  -406,
     406,   104,  -406,   353,  1790,  1932,  -406,  -406,  -406,  -406,
    -406,  -406,  -406,   412,  -406,   407,   408,   734,  1314,   380,
    -406,  -406,  1790,  -406,  -406,   185,   187,   414,   420,   200,
     213,  1080,  -406,  -406,  -406,  -406,  1790,  1790,  -406,  -406,
    -406,  -406,  -406,   411,  -406,  -406,  -406,  -406,   110,  -406,
    -406,  -406,   413,  -406,  1314,  2296,  1080,  1080,  -406,  1790,
    1080,  -406,  -406,   415,   417,   418,  -406,  -406,  -406,  -406,
     504,  -406,   221,  -406,   411,  1080,  1080,  1080,    11,  -406,
    -406,  -406,  -406,  -406,  -406
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    20,    21,    22,    23,    24,    26,
      27,    28,    29,     0,     0,    12,    16,    15,    13,    14,
      17,    18,    25,    30,    31,     3,     5,    81,    11,    19,
      32,     6,     4,     7,     8,    40,    41,    38,    35,    47,
      48,    45,    42,     0,     0,   112,    31,    97,    96,     0,
      10,     0,    82,    83,     0,    85,   103,   116,    49,     0,
      49,    51,     0,     0,   145,   146,   143,   144,   139,   140,
     137,   138,   141,   142,   147,   148,   149,   150,   151,   152,
     153,   154,   155,   156,   134,   131,   129,   130,   135,   136,
     124,   125,   126,   127,   128,   133,   132,     0,     0,   123,
       0,     0,     0,     0,     9,     0,   100,   101,    99,    98,
     102,     0,     0,   159,     0,    78,    79,    80,     0,    31,
       0,    61,     0,    50,    59,     0,    64,     0,    65,     0,
      62,    36,     0,     0,     0,    73,     0,   158,   157,   113,
     117,   114,   118,   115,    84,    85,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   325,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   319,     0,   320,   321,   322,   340,   324,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    86,    87,
     213,   246,   247,   301,   293,   323,     0,   162,     0,   160,
     121,     0,    66,     0,    39,    60,    69,   181,    68,    72,
      71,    63,    49,    46,    57,    58,    52,    53,     0,    43,
     162,     0,   311,   311,   311,   311,   311,   311,   311,   311,
     311,   313,   313,   313,   313,   313,   313,   311,   275,   276,
     277,   278,   279,   281,   282,   283,   284,     0,     0,   286,
     287,   280,   285,   288,   259,   265,   274,   261,     0,   257,
     313,   313,   313,   262,   311,     0,   311,   248,   249,   250,
     252,   253,   251,   254,   255,   275,   276,   277,   278,   279,
     281,   282,   283,   284,   280,   288,     0,   211,     0,   263,
       0,     0,    88,    93,     0,    91,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   216,   217,   218,   219,   220,
     221,   222,   223,   224,   225,   215,     0,     0,     0,   299,
     300,     0,   313,     0,   341,     0,    20,    21,    22,    23,
      24,    26,    27,    28,    29,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    25,   319,    31,
     187,   178,    81,   185,   172,     0,     0,   173,   174,   177,
     175,     0,   176,     0,   169,     0,   163,   164,     0,   120,
     122,   162,     0,     0,     0,     0,    55,    56,    49,     0,
      76,   312,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   317,   318,     0,   314,   315,     0,     0,     0,     0,
       0,     0,   289,   290,   291,   292,   311,   269,     0,   266,
     267,   273,     0,     0,     0,     0,     0,   338,     0,     0,
     339,     0,     0,     0,   104,   264,   106,     0,     0,   226,
     246,    89,     0,   238,   239,   236,   237,   232,   233,   228,
     227,     0,   229,   230,   231,   234,   235,   240,   241,   242,
     243,   244,   214,   297,   298,   296,     0,     0,   179,   180,
       0,   203,     0,     0,     0,     0,     0,     0,   206,   207,
       0,   208,     0,     0,   171,   186,     0,     0,   188,   104,
     167,   168,   119,     0,   161,     0,    70,     0,    37,    54,
       0,    74,     0,   328,   329,   330,   331,   332,   334,   335,
     336,   337,   302,     0,   303,   304,   305,   306,   307,   333,
       0,     0,   270,   268,     0,   258,   308,   309,   310,   327,
     326,   212,   256,     0,   108,     0,   105,     0,     0,     0,
      90,    92,     0,   295,   294,     0,     0,     0,     0,     0,
       0,     0,   194,   210,   209,   195,   204,   204,   166,   165,
      67,   182,    44,     0,    77,   316,   260,   271,     0,   107,
     109,   110,     0,    94,     0,   245,     0,     0,   199,     0,
       0,   191,   193,     0,   205,     0,    75,   272,   111,    95,
     189,   196,     0,   200,     0,     0,     0,     0,     0,   192,
     202,   201,   190,   198,   197
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -406,  -406,  -406,    18,    -1,   -23,  -406,   421,  -406,  -406,
    -406,  -406,  -406,  -406,  -406,   -54,  -406,  -406,   151,  -406,
     427,  -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,  -406,
    -123,  -406,  -406,   429,  -109,  -406,    95,  -278,   -19,  -359,
    -405,   -47,   260,  -406,  -406,   425,  -211,  -406,    72,   553,
    -406,  -327,  -124,  -406,   183,  -406,  -344,  -406,  -406,  -406,
    -406,  -406,     0,  -406,  -181,   -97,  -406,   216,  -265,   188,
    -173,  -406,  -406,   152,   416,  -197,  -406,  -406,  -162,  -153,
    -406,    57,  -406,  -406
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    25,   361,   362,    28,    29,    38,    30,    59,
     212,    58,    61,   388,    60,   122,   134,   216,   217,   123,
     124,   125,   381,   126,   127,   128,    31,   220,   563,   502,
     129,    51,    52,    53,   293,   294,   295,    54,   145,   435,
     436,    56,    57,    99,   197,   391,   375,   376,   377,   130,
     112,   363,   364,   383,   365,   366,   367,   368,   594,   369,
     370,   371,   583,   372,   373,   287,   326,   438,   190,   191,
     402,   254,   419,   420,   289,   256,   192,   193,   392,   403,
     404,   405,   194,   195
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      27,   208,   188,   210,    50,   286,   132,   110,    55,   389,
     218,   434,   603,   288,   189,   491,   199,   201,    44,    26,
      62,   473,   139,   -33,   106,   107,   439,   487,   -34,   536,
     103,   443,   444,   445,   446,   447,   448,   449,   450,   485,
     452,   453,   454,   455,   456,   457,   458,   459,   460,   461,
     265,    43,    35,    36,    39,    40,   432,    27,   421,    27,
     432,   393,   394,   395,   396,   397,   398,   399,   400,    63,
     111,    33,    34,   533,   547,   411,   121,   286,   121,   406,
     407,   408,   409,   410,   536,   422,   439,   106,   107,   522,
     189,    44,   421,   266,   108,   141,   489,  -170,    47,   109,
     418,   548,   426,    48,   428,   113,   114,   423,   424,   425,
     433,    37,   100,    41,   433,   101,    44,   296,   297,   432,
      45,   102,    27,   451,   604,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   401,   401,   401,   401,   401,   401,
     199,   121,   556,   557,   104,   310,   311,   312,   313,   314,
     552,   542,   467,   -33,   434,   131,   555,   108,   384,   206,
     105,   207,   109,   401,   401,   401,   -34,   199,   488,   199,
     495,   429,    49,   433,   441,   482,   442,   429,   -33,   466,
     238,   239,   240,   241,   242,   243,   244,   245,   246,   247,
     248,   -34,   554,   378,   379,   429,   374,   312,   313,   314,
     249,   250,   310,   311,   312,   313,   314,   209,   133,   207,
      44,    27,   386,   387,    45,   102,   429,   135,   544,   374,
     429,   251,   567,   136,   582,   252,   429,   196,   587,   462,
     121,   115,   116,   117,   253,   401,   137,   521,   238,   239,
     240,   241,   242,   243,   244,   245,   246,   247,   248,   590,
     591,    47,   138,   593,   520,   143,    48,   202,   249,   250,
     412,   413,   218,   414,   415,   203,    49,   204,   600,   601,
     602,   429,   430,   214,   215,   417,   211,   575,   213,   251,
     219,   494,   221,   252,   468,   469,   418,   111,   222,   545,
     432,   546,   253,   549,   550,   334,   327,   223,   328,   329,
     330,   429,   576,   429,   577,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,   429,   580,   224,   199,
      15,    16,    17,    18,    19,    20,    21,   225,    47,   429,
     581,   226,   531,    48,   500,   227,   535,   429,   598,    50,
     331,   332,   333,   568,   433,   189,    22,   228,   106,   107,
      23,    50,   257,   259,    44,   490,   229,   263,    45,    46,
     140,   142,   230,   231,   232,   233,   267,   268,   269,   270,
     271,   272,   273,   274,   234,   584,   584,    44,   564,   235,
     374,    45,   102,   236,   237,   260,   261,    27,   262,   486,
     264,   380,   382,   416,   427,    47,   390,   385,   592,   437,
      48,   463,   464,   431,   465,   470,   121,   471,   472,   474,
      49,   475,   477,   480,   483,   265,   401,   478,   108,   296,
     297,   298,   299,   109,   479,   492,   484,   496,   538,   573,
     493,   498,   501,    49,   378,    42,   503,   504,   505,   586,
     572,   189,   110,   506,   507,   308,   309,   310,   311,   312,
     313,   314,   315,   316,   317,   318,   319,   320,   321,   322,
     323,   324,   524,   513,   325,   589,   508,   551,   574,   509,
     599,   510,   511,   512,   561,   514,   515,   189,   516,   440,
     517,   518,   519,   525,   440,   440,   440,   440,   440,   440,
     440,   440,   374,   440,   440,   440,   440,   440,   440,   440,
     440,   440,   440,   526,   527,   146,   147,   148,   149,   150,
     151,   152,   153,   154,   528,   529,   530,   537,   539,   155,
     543,   560,   553,   566,   562,   570,   207,   578,   579,   569,
     597,   588,   595,   429,   144,   596,   499,   541,   198,   440,
     156,   157,   158,   159,   160,   161,   162,   163,   164,   165,
     205,   166,   167,   168,    32,   169,   170,   585,   171,   172,
     173,   174,   175,   176,   177,   559,   497,   476,   178,   179,
     565,   523,     0,     0,     0,     0,     0,     0,     0,   255,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   180,     0,     0,   181,   182,
     183,     0,     0,     0,     0,     0,     0,   184,   185,     0,
     186,     0,     0,   296,   297,   298,   299,   300,   301,   532,
     200,   146,   147,   148,   149,   150,   151,   152,   153,   154,
       0,     0,     0,     0,     0,   155,   305,   306,   307,   308,
     309,   310,   311,   312,   313,   314,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   156,   157,   158,   159,
     160,   161,   162,   163,   164,   165,     0,   166,   167,   168,
       0,   169,   170,     0,   171,   172,   173,   174,   175,   176,
     177,     0,     0,     0,   178,   179,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   180,     0,   532,   181,   182,   183,     0,     0,     0,
       0,     0,     0,   184,   185,     0,   186,     0,     0,     0,
     440,     0,     0,     0,     0,     0,   534,   146,   147,   148,
     149,   150,   151,   152,   153,   154,     0,     0,     0,     0,
       0,   155,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   156,   157,   158,   159,   160,   161,   162,   163,
     164,   165,     0,   166,   167,   168,     0,   169,   170,     0,
     171,   172,   173,   174,   175,   176,   177,     0,     0,     0,
     178,   179,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   296,   297,
     298,   299,   300,   301,     0,     0,     0,   180,     0,     0,
     181,   182,   183,     0,     0,     0,     0,     0,     0,   184,
     185,     0,   186,   307,   308,   309,   310,   311,   312,   313,
     314,   335,   571,   336,   337,   338,   339,   340,   341,   342,
     343,   344,    13,    14,     0,     0,     0,   155,    15,    16,
      17,    18,    19,    20,    21,   345,     0,   346,   347,   348,
     349,   350,   351,   352,   353,   354,   355,   356,   156,   157,
     158,   159,   160,   161,   357,   163,   164,   165,    23,   166,
     167,   168,     0,   169,   170,     0,   358,   359,   173,   174,
     175,   176,   177,     0,     0,     0,   178,   179,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   180,     0,     0,   181,   182,   183,     0,
       0,     0,     0,     0,     0,   184,   185,     0,   186,     0,
       0,     0,     0,   360,  -183,   207,   335,     0,   336,   337,
     338,   339,   340,   341,   342,   343,   344,    13,    14,     0,
       0,     0,   155,    15,    16,    17,    18,    19,    20,    21,
     345,     0,   346,   347,   348,   349,   350,   351,   352,   353,
     354,   355,   356,   156,   157,   158,   159,   160,   161,   357,
     163,   164,   165,    23,   166,   167,   168,     0,   169,   170,
       0,   358,   359,   173,   174,   175,   176,   177,     0,     0,
       0,   178,   179,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   180,     0,
       0,   181,   182,   183,     0,     0,     0,     0,     0,     0,
     184,   185,     0,   186,     0,     0,     0,     0,   360,  -184,
     207,   335,     0,   336,   337,   338,   339,   340,   341,   342,
     343,   344,    13,    14,     0,     0,     0,   155,    15,    16,
      17,    18,    19,    20,    21,   345,     0,   346,   347,   348,
     349,   350,   351,   352,   353,   354,   355,   356,   156,   157,
     158,   159,   160,   161,   357,   163,   164,   165,    23,   166,
     167,   168,     0,   169,   170,     0,   358,   359,   173,   174,
     175,   176,   177,     0,     0,     0,   178,   179,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   146,   147,   148,   149,   150,   151,   152,   153,   154,
       0,     0,     0,   180,     0,   155,   181,   182,   183,     0,
       0,     0,     0,     0,     0,   184,   185,     0,   186,     0,
       0,     0,     0,   360,     0,   207,   156,   157,   158,   159,
     160,   161,   162,   163,   164,   165,     0,   166,   167,   168,
       0,   169,   170,     0,   171,   172,   173,   174,   175,   176,
     177,     0,     0,     0,   178,   179,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   146,
     147,   148,   149,   150,   151,   152,   153,   154,     0,     0,
       0,   180,     0,   155,   181,   182,   183,     0,     0,     0,
       0,     0,     0,   184,   185,   290,   186,   291,     0,     0,
       0,     0,   292,   187,   156,   157,   158,   159,   160,   161,
     162,   163,   164,   165,     0,   166,   167,   168,     0,   169,
     170,     0,   171,   172,   173,   174,   175,   176,   177,     0,
       0,     0,   178,   179,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   146,   147,   148,
     149,   150,   151,   152,   153,   154,     0,     0,     0,   180,
       0,   155,   181,   182,   183,     0,     0,     0,     0,     0,
       0,   184,   185,   290,   186,   291,     0,     0,     0,     0,
     540,   187,   156,   157,   158,   159,   160,   161,   162,   163,
     164,   165,     0,   166,   167,   168,     0,   169,   170,     0,
     171,   172,   173,   174,   175,   176,   177,     0,     0,     0,
     178,   179,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   180,     0,     0,
     181,   182,   183,     0,     0,     0,     0,     0,     0,   184,
     185,     0,   186,     0,     0,     0,     0,     0,     0,   187,
     336,   337,   338,   339,   340,   341,   342,   343,   344,    13,
      14,     0,     0,     0,   155,    15,    16,    17,    18,    19,
      20,    21,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   156,   157,   158,   159,   160,
     161,   357,   163,   164,   165,    23,   166,   167,   168,     0,
     169,   170,     0,   171,   359,   173,   174,   175,   176,   177,
       0,     0,     0,   178,   179,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   146,   147,   148,
     149,   150,   151,   152,   153,   154,     0,     0,     0,     0,
     180,   155,     0,   181,   182,   183,     0,     0,     0,     0,
       0,     0,   184,   185,     0,   186,     0,     0,     0,     0,
     360,     0,   156,   157,   158,   159,   160,   161,   162,   163,
     164,   165,     0,   166,   167,   168,     0,   169,   170,     0,
     171,   172,   173,   174,   175,   176,   177,     0,     0,     0,
     178,   179,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   146,   147,   148,   149,   150,   151,
     152,   153,   154,     0,     0,     0,     0,   180,   155,     0,
     181,   182,   183,     0,     0,     0,     0,     0,     0,   184,
     185,     0,   186,     0,     0,     0,     0,   481,     0,   156,
     157,   158,   159,   160,   161,   162,   163,   164,   165,     0,
     166,   167,   168,     0,   169,   170,     0,   171,   172,   173,
     174,   175,   176,   177,     0,     0,     0,   178,   179,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,     0,     0,     0,     0,    15,    16,    17,    18,    19,
      20,    21,     0,     0,   180,     0,     0,   181,   182,   183,
     296,   297,   298,   299,   300,   301,   184,   185,     0,   186,
       0,    22,     0,     0,   360,    23,     0,     0,     0,    44,
       0,     0,   432,    45,    46,     0,   308,   309,   310,   311,
     312,   313,   314,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   275,   276,   277,   278,   279,   280,   281,   282,
     283,   247,   248,     0,     0,     0,   155,     0,     0,     0,
      47,     0,   249,   250,     0,    48,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    49,   433,   156,   157,   158,
     159,   160,   161,   284,   163,   164,   165,   252,   166,   167,
     168,     0,   169,   170,     0,   171,   285,   173,   174,   175,
     176,   177,     0,     0,     0,   178,   179,     0,     0,     0,
       0,     0,     0,   146,   147,   148,   149,   150,   151,   152,
     153,   154,     0,     0,     0,     0,     0,   155,     0,     0,
       0,     0,   180,     0,     0,   181,   182,   183,     0,     0,
       0,     0,     0,     0,   184,   185,     0,   186,   156,   157,
     158,   159,   160,   161,   162,   163,   164,   165,     0,   166,
     167,   168,     0,   169,   170,     0,   171,   172,   173,   174,
     175,   176,   177,     0,     0,     0,   178,   179,     0,     0,
       0,     0,     0,     0,   146,   147,   148,   149,   150,   151,
     152,   153,   154,     0,     0,     0,     0,     0,   155,     0,
       0,     0,     0,   180,     0,     0,   181,   182,   183,     0,
       0,     0,     0,     0,     0,   184,   185,     0,   186,   156,
     157,   158,   159,   160,   161,   162,   163,   164,   165,     0,
     166,   167,   168,     0,   169,   170,     0,   171,   172,   173,
     174,   175,   176,   177,     0,     0,     0,   178,   179,     0,
       0,     0,     0,     0,     0,   146,   147,   148,   149,   150,
     151,   152,   153,   154,     0,     0,     0,     0,     0,   155,
       0,     0,     0,     0,   180,     0,     0,   181,   182,   183,
       0,     0,     0,     0,     0,     0,   184,   185,     0,   258,
     156,   157,   158,   159,   160,   161,   162,   163,   164,   165,
       0,   166,   167,   168,     0,   169,   170,     0,   171,   172,
     173,   174,   175,   176,   177,     0,     0,     0,   178,   179,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,   115,   116,   117,     0,    15,    16,    17,    18,    19,
      20,    21,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   155,     0,     0,   184,   185,     0,
     186,    22,     0,     0,     0,    23,     0,     0,     0,     0,
       0,     0,     0,   118,   119,   156,   157,   158,   159,   160,
     161,     0,   163,   164,   165,     0,   166,   167,   168,     0,
     169,   170,     0,   171,     0,   173,   174,   175,   176,   177,
       0,     0,     0,   178,   179,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   120,     0,     0,     0,     0,     0,     0,
     180,     0,     0,   181,   182,   183,     0,     0,     0,     0,
       0,     0,   184,   185,     0,   186,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,     0,     0,     0,
       0,    15,    16,    17,    18,    19,    20,    21,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    22,     0,     0,
       0,    23,     0,     0,     0,     0,     0,     0,     0,     0,
     119,     0,     0,     0,     0,     2,     3,   558,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,     0,
       0,     0,     0,    15,    16,    17,    18,    19,    20,    21,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    22,
       0,     0,     0,    23,     0,     0,     0,     0,     0,     0,
       0,     0,    24,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,     0,     0,     0,     0,    15,    16,
      17,    18,    19,    20,    21,   238,   239,   240,   241,   242,
     243,   244,   245,   246,   247,   248,     0,     0,     0,     0,
       0,     0,     0,     0,    22,   249,   250,     0,    23,     0,
       0,     0,     0,     0,     0,     0,     0,   119,     0,     0,
       0,     0,     0,     0,     0,     0,   251,     0,     0,     0,
     252,     0,     0,     0,     0,     0,     0,     0,     0,   253,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    82,    83,
       0,     0,    84,     0,     0,    85,    86,    87,    88,    89,
      90,    91,    92,    93,    94,     0,     0,     0,     0,    95,
      96,     0,    97,    98,   296,   297,   298,   299,   300,   301,
     302,   303,     0,     0,   296,   297,   298,   299,   300,   301,
     302,     0,     0,     0,     0,   304,     0,   305,   306,   307,
     308,   309,   310,   311,   312,   313,   314,   305,   306,   307,
     308,   309,   310,   311,   312,   313,   314,   296,   297,   298,
     299,   300,   301,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   306,   307,   308,   309,   310,   311,   312,   313,   314
};

static const yytype_int16 yycheck[] =
{
       1,   125,   111,   127,    27,   186,    60,    54,    27,   220,
     133,   289,     1,   186,   111,   374,   113,   114,    52,     1,
      57,   348,    56,   115,    23,    24,   291,   371,   115,   434,
      49,   296,   297,   298,   299,   300,   301,   302,   303,   366,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
      65,    65,    56,    57,    56,    57,    55,    58,   255,    60,
      55,   223,   224,   225,   226,   227,   228,   229,   230,   106,
      88,   113,   114,   432,     1,   237,    58,   258,    60,   232,
     233,   234,   235,   236,   489,   258,   351,    23,    24,    98,
     187,    52,   289,   108,    93,    56,   374,   115,    93,    98,
     109,    28,   264,    98,   266,   108,   109,   260,   261,   262,
     109,   115,    65,   115,   109,    65,    52,    68,    69,    55,
      56,    57,   123,   304,   113,   222,   223,   224,   225,   226,
     227,   228,   229,   230,   231,   232,   233,   234,   235,   236,
     237,   123,   486,   487,   113,    96,    97,    98,    99,   100,
     477,    90,   333,    90,   432,   115,   483,    93,   212,   113,
     116,   115,    98,   260,   261,   262,    90,   264,   113,   266,
     381,   116,   108,   109,   114,   356,   116,   116,   115,   332,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,   115,   113,   116,   117,   116,   197,    98,    99,   100,
      23,    24,    96,    97,    98,    99,   100,   113,    90,   115,
      52,   212,    56,    57,    56,    57,   116,   108,   118,   220,
     116,    44,   118,    57,   551,    48,   116,   115,   118,   326,
     212,    14,    15,    16,    57,   332,   117,   418,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,   576,
     577,    93,   118,   580,   416,   117,    98,   108,    23,    24,
      56,    57,   385,    56,    57,    56,   108,   114,   595,   596,
     597,   116,   117,    56,    57,    98,    90,   542,   114,    44,
     115,   378,   108,    48,   113,   114,   109,    88,   108,   470,
      55,   472,    57,   474,   475,    61,    63,   108,    65,    66,
      67,   116,   117,   116,   117,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,   116,   117,   108,   416,
      18,    19,    20,    21,    22,    23,    24,   108,    93,   116,
     117,   108,   429,    98,   388,   108,   433,   116,   117,   362,
     107,   108,   109,   524,   109,   442,    44,   108,    23,    24,
      48,   374,   164,   165,    52,   374,   108,   169,    56,    57,
     100,   101,   108,   108,   108,   108,   178,   179,   180,   181,
     182,   183,   184,   185,   108,   556,   557,    52,   502,   108,
     381,    56,    57,   108,   108,   108,   108,   388,   108,   371,
     108,   118,   108,   108,    56,    93,   117,   116,   579,    56,
      98,    56,    56,   117,    56,   108,   388,   108,   108,   108,
     108,   108,    90,    56,    90,    65,   513,   113,    93,    68,
      69,    70,    71,    98,   113,   117,   114,   117,    88,   538,
     116,   114,   117,   108,   116,    14,   117,   117,   117,   563,
     537,   538,   489,   117,   117,    94,    95,    96,    97,    98,
      99,   100,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,   109,   116,    88,   574,   117,    90,    88,   117,
     594,   117,   117,   117,   114,   117,   117,   574,   117,   291,
     117,   117,   117,   117,   296,   297,   298,   299,   300,   301,
     302,   303,   493,   305,   306,   307,   308,   309,   310,   311,
     312,   313,   314,   117,   117,     3,     4,     5,     6,     7,
       8,     9,    10,    11,   117,   117,   117,   109,   118,    17,
     117,   117,   113,   117,   114,   118,   115,   113,   108,   117,
      26,   118,   117,   116,   105,   117,   385,   442,   113,   351,
      38,    39,    40,    41,    42,    43,    44,    45,    46,    47,
     123,    49,    50,    51,     1,    53,    54,   557,    56,    57,
      58,    59,    60,    61,    62,   493,   383,   351,    66,    67,
     513,   419,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   163,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    93,    -1,    -1,    96,    97,
      98,    -1,    -1,    -1,    -1,    -1,    -1,   105,   106,    -1,
     108,    -1,    -1,    68,    69,    70,    71,    72,    73,   431,
     118,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      -1,    -1,    -1,    -1,    -1,    17,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    -1,    49,    50,    51,
      -1,    53,    54,    -1,    56,    57,    58,    59,    60,    61,
      62,    -1,    -1,    -1,    66,    67,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    93,    -1,   525,    96,    97,    98,    -1,    -1,    -1,
      -1,    -1,    -1,   105,   106,    -1,   108,    -1,    -1,    -1,
     542,    -1,    -1,    -1,    -1,    -1,   118,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    17,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    -1,    49,    50,    51,    -1,    53,    54,    -1,
      56,    57,    58,    59,    60,    61,    62,    -1,    -1,    -1,
      66,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    68,    69,
      70,    71,    72,    73,    -1,    -1,    -1,    93,    -1,    -1,
      96,    97,    98,    -1,    -1,    -1,    -1,    -1,    -1,   105,
     106,    -1,   108,    93,    94,    95,    96,    97,    98,    99,
     100,     1,   118,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    -1,    53,    54,    -1,    56,    57,    58,    59,
      60,    61,    62,    -1,    -1,    -1,    66,    67,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    93,    -1,    -1,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,   105,   106,    -1,   108,    -1,
      -1,    -1,    -1,   113,   114,   115,     1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    -1,
      -1,    -1,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    -1,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    -1,    53,    54,
      -1,    56,    57,    58,    59,    60,    61,    62,    -1,    -1,
      -1,    66,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    93,    -1,
      -1,    96,    97,    98,    -1,    -1,    -1,    -1,    -1,    -1,
     105,   106,    -1,   108,    -1,    -1,    -1,    -1,   113,   114,
     115,     1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    -1,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    -1,    53,    54,    -1,    56,    57,    58,    59,
      60,    61,    62,    -1,    -1,    -1,    66,    67,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      -1,    -1,    -1,    93,    -1,    17,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,   105,   106,    -1,   108,    -1,
      -1,    -1,    -1,   113,    -1,   115,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    -1,    49,    50,    51,
      -1,    53,    54,    -1,    56,    57,    58,    59,    60,    61,
      62,    -1,    -1,    -1,    66,    67,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    93,    -1,    17,    96,    97,    98,    -1,    -1,    -1,
      -1,    -1,    -1,   105,   106,   107,   108,   109,    -1,    -1,
      -1,    -1,   114,   115,    38,    39,    40,    41,    42,    43,
      44,    45,    46,    47,    -1,    49,    50,    51,    -1,    53,
      54,    -1,    56,    57,    58,    59,    60,    61,    62,    -1,
      -1,    -1,    66,    67,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    93,
      -1,    17,    96,    97,    98,    -1,    -1,    -1,    -1,    -1,
      -1,   105,   106,   107,   108,   109,    -1,    -1,    -1,    -1,
     114,   115,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    -1,    49,    50,    51,    -1,    53,    54,    -1,
      56,    57,    58,    59,    60,    61,    62,    -1,    -1,    -1,
      66,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    93,    -1,    -1,
      96,    97,    98,    -1,    -1,    -1,    -1,    -1,    -1,   105,
     106,    -1,   108,    -1,    -1,    -1,    -1,    -1,    -1,   115,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    -1,    -1,    -1,    17,    18,    19,    20,    21,    22,
      23,    24,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    -1,
      53,    54,    -1,    56,    57,    58,    59,    60,    61,    62,
      -1,    -1,    -1,    66,    67,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      93,    17,    -1,    96,    97,    98,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,    -1,   108,    -1,    -1,    -1,    -1,
     113,    -1,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,    -1,    49,    50,    51,    -1,    53,    54,    -1,
      56,    57,    58,    59,    60,    61,    62,    -1,    -1,    -1,
      66,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    93,    17,    -1,
      96,    97,    98,    -1,    -1,    -1,    -1,    -1,    -1,   105,
     106,    -1,   108,    -1,    -1,    -1,    -1,   113,    -1,    38,
      39,    40,    41,    42,    43,    44,    45,    46,    47,    -1,
      49,    50,    51,    -1,    53,    54,    -1,    56,    57,    58,
      59,    60,    61,    62,    -1,    -1,    -1,    66,    67,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    -1,    -1,    -1,    -1,    18,    19,    20,    21,    22,
      23,    24,    -1,    -1,    93,    -1,    -1,    96,    97,    98,
      68,    69,    70,    71,    72,    73,   105,   106,    -1,   108,
      -1,    44,    -1,    -1,   113,    48,    -1,    -1,    -1,    52,
      -1,    -1,    55,    56,    57,    -1,    94,    95,    96,    97,
      98,    99,   100,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    -1,    -1,    -1,    17,    -1,    -1,    -1,
      93,    -1,    23,    24,    -1,    98,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   108,   109,    38,    39,    40,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      51,    -1,    53,    54,    -1,    56,    57,    58,    59,    60,
      61,    62,    -1,    -1,    -1,    66,    67,    -1,    -1,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,
      -1,    -1,    93,    -1,    -1,    96,    97,    98,    -1,    -1,
      -1,    -1,    -1,    -1,   105,   106,    -1,   108,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    -1,    49,
      50,    51,    -1,    53,    54,    -1,    56,    57,    58,    59,
      60,    61,    62,    -1,    -1,    -1,    66,    67,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    17,    -1,
      -1,    -1,    -1,    93,    -1,    -1,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,   105,   106,    -1,   108,    38,
      39,    40,    41,    42,    43,    44,    45,    46,    47,    -1,
      49,    50,    51,    -1,    53,    54,    -1,    56,    57,    58,
      59,    60,    61,    62,    -1,    -1,    -1,    66,    67,    -1,
      -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,    17,
      -1,    -1,    -1,    -1,    93,    -1,    -1,    96,    97,    98,
      -1,    -1,    -1,    -1,    -1,    -1,   105,   106,    -1,   108,
      38,    39,    40,    41,    42,    43,    44,    45,    46,    47,
      -1,    49,    50,    51,    -1,    53,    54,    -1,    56,    57,
      58,    59,    60,    61,    62,    -1,    -1,    -1,    66,    67,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    -1,    18,    19,    20,    21,    22,
      23,    24,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    17,    -1,    -1,   105,   106,    -1,
     108,    44,    -1,    -1,    -1,    48,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    56,    57,    38,    39,    40,    41,    42,
      43,    -1,    45,    46,    47,    -1,    49,    50,    51,    -1,
      53,    54,    -1,    56,    -1,    58,    59,    60,    61,    62,
      -1,    -1,    -1,    66,    67,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   106,    -1,    -1,    -1,    -1,    -1,    -1,
      93,    -1,    -1,    96,    97,    98,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,    -1,   108,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    -1,    -1,    -1,
      -1,    18,    19,    20,    21,    22,    23,    24,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    44,    -1,    -1,
      -1,    48,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      57,    -1,    -1,    -1,    -1,     0,     1,    64,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    -1,
      -1,    -1,    -1,    18,    19,    20,    21,    22,    23,    24,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    44,
      -1,    -1,    -1,    48,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    57,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    -1,    18,    19,
      20,    21,    22,    23,    24,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    44,    23,    24,    -1,    48,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    57,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    44,    -1,    -1,    -1,
      48,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    57,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      -1,    -1,    88,    -1,    -1,    91,    92,    93,    94,    95,
      96,    97,    98,    99,   100,    -1,    -1,    -1,    -1,   105,
     106,    -1,   108,   109,    68,    69,    70,    71,    72,    73,
      74,    75,    -1,    -1,    68,    69,    70,    71,    72,    73,
      74,    -1,    -1,    -1,    -1,    89,    -1,    91,    92,    93,
      94,    95,    96,    97,    98,    99,   100,    91,    92,    93,
      94,    95,    96,    97,    98,    99,   100,    68,    69,    70,
      71,    72,    73,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    92,    93,    94,    95,    96,    97,    98,    99,   100
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   120,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    18,    19,    20,    21,    22,
      23,    24,    44,    48,    57,   121,   122,   123,   124,   125,
     127,   145,   168,   113,   114,    56,    57,   115,   126,    56,
      57,   115,   126,    65,    52,    56,    57,    93,    98,   108,
     124,   150,   151,   152,   156,   157,   160,   161,   130,   128,
     133,   131,    57,   106,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    88,    91,    92,    93,    94,    95,
      96,    97,    98,    99,   100,   105,   106,   108,   109,   162,
      65,    65,    57,   157,   113,   116,    23,    24,    93,    98,
     160,    88,   169,   108,   109,    14,    15,    16,    56,    57,
     106,   122,   134,   138,   139,   140,   142,   143,   144,   149,
     168,   115,   134,    90,   135,   108,    57,   117,   118,    56,
     161,    56,   161,   117,   152,   157,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    17,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    49,    50,    51,    53,
      54,    56,    57,    58,    59,    60,    61,    62,    66,    67,
      93,    96,    97,    98,   105,   106,   108,   115,   153,   184,
     187,   188,   195,   196,   201,   202,   115,   163,   164,   184,
     118,   184,   108,    56,   114,   139,   113,   115,   171,   113,
     171,    90,   129,   114,    56,    57,   136,   137,   149,   115,
     146,   108,   108,   108,   108,   108,   108,   108,   108,   108,
     108,   108,   108,   108,   108,   108,   108,   108,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    23,
      24,    44,    48,    57,   190,   193,   194,   188,   108,   188,
     108,   108,   108,   188,   108,    65,   108,   188,   188,   188,
     188,   188,   188,   188,   188,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    44,    57,   183,   184,   189,   193,
     107,   109,   114,   153,   154,   155,    68,    69,    70,    71,
      72,    73,    74,    75,    89,    91,    92,    93,    94,    95,
      96,    97,    98,    99,   100,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    88,   185,    63,    65,    66,
      67,   107,   108,   109,    61,     1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    25,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    44,    56,    57,
     113,   122,   123,   170,   171,   173,   174,   175,   176,   178,
     179,   180,   182,   183,   123,   165,   166,   167,   116,   117,
     118,   141,   108,   172,   134,   116,    56,    57,   132,   165,
     117,   164,   197,   197,   197,   197,   197,   197,   197,   197,
     197,   184,   189,   198,   199,   200,   198,   198,   198,   198,
     198,   197,    56,    57,    56,    57,   108,    98,   109,   191,
     192,   194,   189,   198,   198,   198,   197,    56,   197,   116,
     117,   117,    55,   109,   156,   158,   159,    56,   186,   187,
     188,   114,   116,   187,   187,   187,   187,   187,   187,   187,
     187,   183,   187,   187,   187,   187,   187,   187,   187,   187,
     187,   187,   184,    56,    56,    56,   198,   183,   113,   114,
     108,   108,   108,   170,   108,   108,   186,    90,   113,   113,
      56,   113,   183,    90,   114,   170,   122,   175,   113,   156,
     157,   158,   117,   116,   184,   165,   117,   173,   114,   137,
     134,   117,   148,   117,   117,   117,   117,   117,   117,   117,
     117,   117,   117,   116,   117,   117,   117,   117,   117,   117,
     197,   183,    98,   192,   109,   117,   117,   117,   117,   117,
     117,   184,   188,   158,   118,   184,   159,   109,    88,   118,
     114,   155,    90,   117,   118,   183,   183,     1,    28,   183,
     183,    90,   170,   113,   113,   170,   175,   175,    64,   167,
     117,   114,   114,   147,   171,   200,   117,   118,   183,   117,
     118,   118,   184,   153,    88,   187,   117,   117,   113,   108,
     117,   117,   170,   181,   183,   181,   171,   118,   118,   153,
     170,   170,   183,   170,   177,   117,   117,    26,   117,   171,
     170,   170,   170,     1,   113
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   119,   120,   120,   121,   121,   121,   121,   121,   122,
     123,   123,   124,   124,   124,   124,   124,   124,   124,   124,
     125,   125,   125,   125,   125,   125,   125,   125,   125,   125,
     125,   125,   125,   126,   126,   128,   129,   127,   130,   127,
     127,   127,   131,   132,   127,   133,   127,   127,   127,   134,
     134,   135,   135,   136,   136,   137,   137,   137,   137,   138,
     138,   139,   139,   139,   139,   139,   141,   140,   142,   142,
     143,   144,   144,   146,   147,   145,   148,   145,   149,   149,
     149,   150,   150,   151,   151,   152,   152,   153,   153,   153,
     153,   154,   154,   155,   155,   155,   156,   156,   156,   156,
     156,   156,   157,   157,   158,   158,   158,   159,   159,   159,
     159,   159,   160,   160,   160,   160,   160,   160,   160,   160,
     160,   160,   160,   161,   162,   162,   162,   162,   162,   162,
     162,   162,   162,   162,   162,   162,   162,   162,   162,   162,
     162,   162,   162,   162,   162,   162,   162,   162,   162,   162,
     162,   162,   162,   162,   162,   162,   162,   162,   162,   163,
     164,   164,   165,   165,   166,   166,   166,   167,   167,   167,
     169,   168,   170,   170,   170,   170,   170,   170,   170,   170,
     170,   172,   171,   173,   173,   174,   174,   175,   175,   176,
     176,   177,   176,   178,   178,   178,   179,   179,   179,   179,
     179,   179,   179,   180,   181,   181,   182,   182,   182,   182,
     182,   183,   183,   184,   184,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   186,   187,   187,   187,
     187,   187,   187,   187,   187,   187,   187,   187,   187,   187,
     187,   187,   187,   187,   187,   187,   187,   188,   188,   188,
     188,   188,   188,   188,   188,   188,   188,   188,   188,   188,
     188,   188,   188,   189,   189,   190,   190,   190,   190,   191,
     191,   192,   192,   193,   193,   194,   194,   194,   194,   194,
     194,   194,   194,   194,   194,   194,   194,   194,   194,   194,
     194,   194,   194,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   196,   196,   196,   196,   196,   196,   196,   196,
     196,   197,   197,   198,   198,   199,   199,   200,   200,   201,
     201,   201,   201,   201,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   201,   201,   201,   201,   201,   201,
     202,   202
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
       2,     1,     1,     2,     1,     1,     0,     5,     2,     2,
       4,     2,     2,     0,     0,     9,     0,     8,     1,     1,
       1,     0,     1,     1,     3,     1,     3,     1,     2,     3,
       4,     1,     3,     1,     4,     5,     1,     1,     2,     2,
       2,     2,     2,     1,     1,     2,     1,     3,     2,     3,
       3,     4,     1,     3,     3,     3,     1,     3,     3,     5,
       4,     3,     4,     2,     1,     1,     1,     1,     1,     1,
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
       2,     2,     2,     2,     2,     2,     4,     2,     4,     2,
       5,     2,     2,     1,     2,     1,     2,     2,     3,     1,
       2,     3,     4,     2,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     2,
       2,     2,     2,     1,     4,     4,     3,     3,     3,     2,
       2,     1,     4,     4,     4,     4,     4,     4,     4,     4,
       4,     0,     1,     0,     1,     1,     3,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     4,     4,     4,     4,
       4,     4,     4,     4,     4,     4,     4,     4,     3,     3,
       1,     2
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
#line 125 "../phase2-parser/src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2508 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 129 "../phase2-parser/src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2518 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 137 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2524 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 138 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2530 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 139 "../phase2-parser/src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2536 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 140 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2542 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 141 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2548 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 145 "../phase2-parser/src/parser.y"
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
#line 2578 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 173 "../phase2-parser/src/parser.y"
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
#line 2598 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 188 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2604 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 192 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2610 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: EXTERN  */
#line 193 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isExtern = true; yyval.typeSpec.storageClasses = 1; }
#line 2616 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: REGISTER  */
#line 194 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isRegister = true; yyval.typeSpec.storageClasses = 1; }
#line 2622 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: AUTO  */
#line 195 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2628 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: TYPEDEF  */
#line 196 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2634 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: CONST  */
#line 197 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2640 "build/parser.tab.cpp"
    break;

  case 18: /* storage_or_type_specifier: VOLATILE  */
#line 198 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isVolatile = true; }
#line 2646 "build/parser.tab.cpp"
    break;

  case 19: /* storage_or_type_specifier: type_specifier  */
#line 199 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2652 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: INT  */
#line 203 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2658 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: CHAR  */
#line 204 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2664 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: FLOAT  */
#line 205 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2670 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: DOUBLE  */
#line 206 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2676 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: VOID  */
#line 207 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2682 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: BOOL  */
#line 208 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2688 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SHORT  */
#line 209 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2694 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: LONG  */
#line 210 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2700 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: SIGNED  */
#line 211 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2706 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: UNSIGNED  */
#line 212 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2712 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: VA_LIST  */
#line 213 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2718 "build/parser.tab.cpp"
    break;

  case 31: /* type_specifier: TYPE_NAME  */
#line 214 "../phase2-parser/src/parser.y"
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
#line 2737 "build/parser.tab.cpp"
    break;

  case 32: /* type_specifier: struct_or_class_specifier  */
#line 228 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2743 "build/parser.tab.cpp"
    break;

  case 33: /* tag_name: IDENTIFIER  */
#line 235 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2749 "build/parser.tab.cpp"
    break;

  case 34: /* tag_name: TYPE_NAME  */
#line 236 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2755 "build/parser.tab.cpp"
    break;

  case 35: /* $@1: %empty  */
#line 240 "../phase2-parser/src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2765 "build/parser.tab.cpp"
    break;

  case 36: /* $@2: %empty  */
#line 244 "../phase2-parser/src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2771 "build/parser.tab.cpp"
    break;

  case 37: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 244 "../phase2-parser/src/parser.y"
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
#line 2789 "build/parser.tab.cpp"
    break;

  case 38: /* @3: %empty  */
#line 260 "../phase2-parser/src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2801 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 266 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2814 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 274 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2825 "build/parser.tab.cpp"
    break;

  case 41: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 280 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2836 "build/parser.tab.cpp"
    break;

  case 42: /* $@4: %empty  */
#line 286 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2846 "build/parser.tab.cpp"
    break;

  case 43: /* $@5: %empty  */
#line 290 "../phase2-parser/src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2852 "build/parser.tab.cpp"
    break;

  case 44: /* struct_or_class_specifier: CLASS tag_name $@4 inheritance_opt '{' $@5 member_decl_list_opt '}'  */
#line 290 "../phase2-parser/src/parser.y"
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
#line 2869 "build/parser.tab.cpp"
    break;

  case 45: /* @6: %empty  */
#line 302 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2881 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: CLASS '{' @6 member_decl_list_opt '}'  */
#line 308 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2894 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 316 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2905 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 322 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2916 "build/parser.tab.cpp"
    break;

  case 49: /* member_decl_list_opt: %empty  */
#line 331 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 2922 "build/parser.tab.cpp"
    break;

  case 50: /* member_decl_list_opt: member_decl_list  */
#line 332 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2928 "build/parser.tab.cpp"
    break;

  case 51: /* inheritance_opt: %empty  */
#line 336 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 2934 "build/parser.tab.cpp"
    break;

  case 52: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 337 "../phase2-parser/src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 2940 "build/parser.tab.cpp"
    break;

  case 53: /* inheritance_specifier_list: inheritance_specifier  */
#line 341 "../phase2-parser/src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2946 "build/parser.tab.cpp"
    break;

  case 54: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 342 "../phase2-parser/src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 2955 "build/parser.tab.cpp"
    break;

  case 55: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 349 "../phase2-parser/src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2966 "build/parser.tab.cpp"
    break;

  case 56: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 355 "../phase2-parser/src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2977 "build/parser.tab.cpp"
    break;

  case 57: /* inheritance_specifier: IDENTIFIER  */
#line 361 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2988 "build/parser.tab.cpp"
    break;

  case 58: /* inheritance_specifier: TYPE_NAME  */
#line 367 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2999 "build/parser.tab.cpp"
    break;

  case 59: /* member_decl_list: member_item  */
#line 378 "../phase2-parser/src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 3009 "build/parser.tab.cpp"
    break;

  case 60: /* member_decl_list: member_decl_list member_item  */
#line 383 "../phase2-parser/src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 3023 "build/parser.tab.cpp"
    break;

  case 61: /* member_item: declaration  */
#line 395 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3029 "build/parser.tab.cpp"
    break;

  case 62: /* member_item: function_definition  */
#line 396 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3035 "build/parser.tab.cpp"
    break;

  case 63: /* member_item: access_specifier ':'  */
#line 397 "../phase2-parser/src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3041 "build/parser.tab.cpp"
    break;

  case 64: /* member_item: constructor_def  */
#line 398 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3047 "build/parser.tab.cpp"
    break;

  case 65: /* member_item: destructor_def  */
#line 399 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3053 "build/parser.tab.cpp"
    break;

  case 66: /* $@7: %empty  */
#line 406 "../phase2-parser/src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3059 "build/parser.tab.cpp"
    break;

  case 67: /* constructor_head: IDENTIFIER '(' $@7 parameter_list_opt ')'  */
#line 406 "../phase2-parser/src/parser.y"
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
#line 3078 "build/parser.tab.cpp"
    break;

  case 68: /* constructor_def: constructor_head compound_stmt  */
#line 423 "../phase2-parser/src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3087 "build/parser.tab.cpp"
    break;

  case 69: /* constructor_def: constructor_head ';'  */
#line 427 "../phase2-parser/src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3096 "build/parser.tab.cpp"
    break;

  case 70: /* destructor_head: '~' IDENTIFIER '(' ')'  */
#line 434 "../phase2-parser/src/parser.y"
                             {
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          pushScope(currentClassName() + "::~" + yyvsp[-2].str + "()");
          yyval = yyvsp[-2];
      }
#line 3106 "build/parser.tab.cpp"
    break;

  case 71: /* destructor_def: destructor_head compound_stmt  */
#line 442 "../phase2-parser/src/parser.y"
                                    {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), yyvsp[0].node);
      }
#line 3115 "build/parser.tab.cpp"
    break;

  case 72: /* destructor_def: destructor_head ';'  */
#line 446 "../phase2-parser/src/parser.y"
                          {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-1].str, yyvsp[-1].idx, currentClassName(), nullptr);
      }
#line 3124 "build/parser.tab.cpp"
    break;

  case 73: /* $@8: %empty  */
#line 454 "../phase2-parser/src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3134 "build/parser.tab.cpp"
    break;

  case 74: /* $@9: %empty  */
#line 458 "../phase2-parser/src/parser.y"
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
#line 3150 "build/parser.tab.cpp"
    break;

  case 75: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@8 parameter_list_opt ')' $@9 compound_stmt  */
#line 468 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3160 "build/parser.tab.cpp"
    break;

  case 76: /* $@10: %empty  */
#line 473 "../phase2-parser/src/parser.y"
                                                {
          setCategory(yyvsp[-5].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-5].str)));
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          enterClass(yyvsp[-5].str);
          pushScope(yyvsp[-5].str + "::~" + yyvsp[-2].str + "()");
      }
#line 3171 "build/parser.tab.cpp"
    break;

  case 77: /* out_of_class_special: TYPE_NAME SCOPE_RES '~' TYPE_NAME '(' ')' $@10 compound_stmt  */
#line 478 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeDestructorNode(yyvsp[-4].str, yyvsp[-4].idx, yyvsp[-7].str, yyvsp[0].node);
          leaveClass();
      }
#line 3181 "build/parser.tab.cpp"
    break;

  case 81: /* init_declarator_list_opt: %empty  */
#line 492 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3187 "build/parser.tab.cpp"
    break;

  case 82: /* init_declarator_list_opt: init_declarator_list  */
#line 493 "../phase2-parser/src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3193 "build/parser.tab.cpp"
    break;

  case 83: /* init_declarator_list: init_declarator  */
#line 497 "../phase2-parser/src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3199 "build/parser.tab.cpp"
    break;

  case 84: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 498 "../phase2-parser/src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3205 "build/parser.tab.cpp"
    break;

  case 85: /* init_declarator: declarator  */
#line 502 "../phase2-parser/src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3211 "build/parser.tab.cpp"
    break;

  case 86: /* init_declarator: declarator '=' initializer  */
#line 503 "../phase2-parser/src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3217 "build/parser.tab.cpp"
    break;

  case 87: /* initializer: assignment_expr  */
#line 507 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3223 "build/parser.tab.cpp"
    break;

  case 88: /* initializer: '{' '}'  */
#line 508 "../phase2-parser/src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3229 "build/parser.tab.cpp"
    break;

  case 89: /* initializer: '{' initializer_list '}'  */
#line 509 "../phase2-parser/src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3239 "build/parser.tab.cpp"
    break;

  case 90: /* initializer: '{' initializer_list ',' '}'  */
#line 514 "../phase2-parser/src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3249 "build/parser.tab.cpp"
    break;

  case 91: /* initializer_list: initializer_item  */
#line 522 "../phase2-parser/src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3255 "build/parser.tab.cpp"
    break;

  case 92: /* initializer_list: initializer_list ',' initializer_item  */
#line 523 "../phase2-parser/src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3261 "build/parser.tab.cpp"
    break;

  case 93: /* initializer_item: initializer  */
#line 527 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3267 "build/parser.tab.cpp"
    break;

  case 94: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 528 "../phase2-parser/src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3275 "build/parser.tab.cpp"
    break;

  case 95: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 531 "../phase2-parser/src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3283 "build/parser.tab.cpp"
    break;

  case 96: /* pointer: '*'  */
#line 537 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3289 "build/parser.tab.cpp"
    break;

  case 97: /* pointer: '&'  */
#line 538 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3295 "build/parser.tab.cpp"
    break;

  case 98: /* pointer: pointer '*'  */
#line 539 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3301 "build/parser.tab.cpp"
    break;

  case 99: /* pointer: pointer '&'  */
#line 540 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3307 "build/parser.tab.cpp"
    break;

  case 100: /* pointer: pointer CONST  */
#line 541 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3313 "build/parser.tab.cpp"
    break;

  case 101: /* pointer: pointer VOLATILE  */
#line 542 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "v"; }
#line 3319 "build/parser.tab.cpp"
    break;

  case 102: /* declarator: pointer direct_declarator  */
#line 546 "../phase2-parser/src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3330 "build/parser.tab.cpp"
    break;

  case 103: /* declarator: direct_declarator  */
#line 552 "../phase2-parser/src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3336 "build/parser.tab.cpp"
    break;

  case 104: /* abstract_declarator: pointer  */
#line 558 "../phase2-parser/src/parser.y"
              { yyval = yyvsp[0]; }
#line 3342 "build/parser.tab.cpp"
    break;

  case 105: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 559 "../phase2-parser/src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3353 "build/parser.tab.cpp"
    break;

  case 106: /* abstract_declarator: direct_abstract_declarator  */
#line 565 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3359 "build/parser.tab.cpp"
    break;

  case 107: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 569 "../phase2-parser/src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3373 "build/parser.tab.cpp"
    break;

  case 108: /* direct_abstract_declarator: '[' ']'  */
#line 578 "../phase2-parser/src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3379 "build/parser.tab.cpp"
    break;

  case 109: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 579 "../phase2-parser/src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3385 "build/parser.tab.cpp"
    break;

  case 110: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 580 "../phase2-parser/src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3391 "build/parser.tab.cpp"
    break;

  case 111: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 581 "../phase2-parser/src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3397 "build/parser.tab.cpp"
    break;

  case 112: /* direct_declarator: IDENTIFIER  */
#line 585 "../phase2-parser/src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3406 "build/parser.tab.cpp"
    break;

  case 113: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 589 "../phase2-parser/src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3418 "build/parser.tab.cpp"
    break;

  case 114: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 596 "../phase2-parser/src/parser.y"
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
#line 3435 "build/parser.tab.cpp"
    break;

  case 115: /* direct_declarator: '(' declarator ')'  */
#line 608 "../phase2-parser/src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3449 "build/parser.tab.cpp"
    break;

  case 116: /* direct_declarator: operator_function_id  */
#line 617 "../phase2-parser/src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3458 "build/parser.tab.cpp"
    break;

  case 117: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 621 "../phase2-parser/src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3470 "build/parser.tab.cpp"
    break;

  case 118: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 628 "../phase2-parser/src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3482 "build/parser.tab.cpp"
    break;

  case 119: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 635 "../phase2-parser/src/parser.y"
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
#line 3506 "build/parser.tab.cpp"
    break;

  case 120: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 654 "../phase2-parser/src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3518 "build/parser.tab.cpp"
    break;

  case 121: /* direct_declarator: direct_declarator '[' ']'  */
#line 661 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3524 "build/parser.tab.cpp"
    break;

  case 122: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 662 "../phase2-parser/src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3530 "build/parser.tab.cpp"
    break;

  case 123: /* operator_function_id: OPERATOR overloadable_operator  */
#line 667 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3536 "build/parser.tab.cpp"
    break;

  case 124: /* overloadable_operator: '+'  */
#line 671 "../phase2-parser/src/parser.y"
          { yyval.str = "+"; }
#line 3542 "build/parser.tab.cpp"
    break;

  case 125: /* overloadable_operator: '-'  */
#line 671 "../phase2-parser/src/parser.y"
                                  { yyval.str = "-"; }
#line 3548 "build/parser.tab.cpp"
    break;

  case 126: /* overloadable_operator: '*'  */
#line 671 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "*"; }
#line 3554 "build/parser.tab.cpp"
    break;

  case 127: /* overloadable_operator: '/'  */
#line 671 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3560 "build/parser.tab.cpp"
    break;

  case 128: /* overloadable_operator: '%'  */
#line 672 "../phase2-parser/src/parser.y"
          { yyval.str = "%"; }
#line 3566 "build/parser.tab.cpp"
    break;

  case 129: /* overloadable_operator: '^'  */
#line 672 "../phase2-parser/src/parser.y"
                                  { yyval.str = "^"; }
#line 3572 "build/parser.tab.cpp"
    break;

  case 130: /* overloadable_operator: '&'  */
#line 672 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "&"; }
#line 3578 "build/parser.tab.cpp"
    break;

  case 131: /* overloadable_operator: '|'  */
#line 672 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3584 "build/parser.tab.cpp"
    break;

  case 132: /* overloadable_operator: '~'  */
#line 673 "../phase2-parser/src/parser.y"
          { yyval.str = "~"; }
#line 3590 "build/parser.tab.cpp"
    break;

  case 133: /* overloadable_operator: '!'  */
#line 673 "../phase2-parser/src/parser.y"
                                  { yyval.str = "!"; }
#line 3596 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: '='  */
#line 673 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "="; }
#line 3602 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: '<'  */
#line 673 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3608 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: '>'  */
#line 674 "../phase2-parser/src/parser.y"
          { yyval.str = ">"; }
#line 3614 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: EQ_OP  */
#line 674 "../phase2-parser/src/parser.y"
                                    { yyval.str = "=="; }
#line 3620 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: NE_OP  */
#line 674 "../phase2-parser/src/parser.y"
                                                               { yyval.str = "!="; }
#line 3626 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: LE_OP  */
#line 674 "../phase2-parser/src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3632 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: GE_OP  */
#line 675 "../phase2-parser/src/parser.y"
            { yyval.str = ">="; }
#line 3638 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: AND_OP  */
#line 675 "../phase2-parser/src/parser.y"
                                        { yyval.str = "&&"; }
#line 3644 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: OR_OP  */
#line 675 "../phase2-parser/src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3650 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: SHL  */
#line 675 "../phase2-parser/src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3656 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: SHR  */
#line 676 "../phase2-parser/src/parser.y"
          { yyval.str = ">>"; }
#line 3662 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: INC  */
#line 676 "../phase2-parser/src/parser.y"
                                   { yyval.str = "++"; }
#line 3668 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: DEC  */
#line 676 "../phase2-parser/src/parser.y"
                                                            { yyval.str = "--"; }
#line 3674 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: PLUS_ASSIGN  */
#line 677 "../phase2-parser/src/parser.y"
                  { yyval.str = "+="; }
#line 3680 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: MINUS_ASSIGN  */
#line 677 "../phase2-parser/src/parser.y"
                                                    { yyval.str = "-="; }
#line 3686 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: MUL_ASSIGN  */
#line 677 "../phase2-parser/src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3692 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: DIV_ASSIGN  */
#line 678 "../phase2-parser/src/parser.y"
                 { yyval.str = "/="; }
#line 3698 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: MOD_ASSIGN  */
#line 678 "../phase2-parser/src/parser.y"
                                                 { yyval.str = "%="; }
#line 3704 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: AND_ASSIGN  */
#line 678 "../phase2-parser/src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3710 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: OR_ASSIGN  */
#line 679 "../phase2-parser/src/parser.y"
                { yyval.str = "|="; }
#line 3716 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: XOR_ASSIGN  */
#line 679 "../phase2-parser/src/parser.y"
                                                { yyval.str = "^="; }
#line 3722 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: SHL_ASSIGN  */
#line 679 "../phase2-parser/src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3728 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: SHR_ASSIGN  */
#line 680 "../phase2-parser/src/parser.y"
                 { yyval.str = ">>="; }
#line 3734 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: '[' ']'  */
#line 680 "../phase2-parser/src/parser.y"
                                               { yyval.str = "[]"; }
#line 3740 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: '(' ')'  */
#line 680 "../phase2-parser/src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3746 "build/parser.tab.cpp"
    break;

  case 159: /* param_scope: %empty  */
#line 687 "../phase2-parser/src/parser.y"
                                           { pushScope(); }
#line 3752 "build/parser.tab.cpp"
    break;

  case 160: /* constructor_args: assignment_expr  */
#line 691 "../phase2-parser/src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3758 "build/parser.tab.cpp"
    break;

  case 161: /* constructor_args: constructor_args ',' assignment_expr  */
#line 692 "../phase2-parser/src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3764 "build/parser.tab.cpp"
    break;

  case 162: /* parameter_list_opt: %empty  */
#line 696 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3770 "build/parser.tab.cpp"
    break;

  case 163: /* parameter_list_opt: parameter_list  */
#line 697 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3776 "build/parser.tab.cpp"
    break;

  case 164: /* parameter_list: parameter_decl  */
#line 701 "../phase2-parser/src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3785 "build/parser.tab.cpp"
    break;

  case 165: /* parameter_list: parameter_list ',' parameter_decl  */
#line 705 "../phase2-parser/src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3794 "build/parser.tab.cpp"
    break;

  case 166: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 709 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3800 "build/parser.tab.cpp"
    break;

  case 167: /* parameter_decl: declaration_specifiers declarator  */
#line 713 "../phase2-parser/src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3810 "build/parser.tab.cpp"
    break;

  case 168: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 718 "../phase2-parser/src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3820 "build/parser.tab.cpp"
    break;

  case 169: /* parameter_decl: declaration_specifiers  */
#line 723 "../phase2-parser/src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3830 "build/parser.tab.cpp"
    break;

  case 170: /* $@11: %empty  */
#line 731 "../phase2-parser/src/parser.y"
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
#line 3870 "build/parser.tab.cpp"
    break;

  case 171: /* function_definition: declaration_specifiers declarator $@11 '{' block_item_list_opt '}'  */
#line 765 "../phase2-parser/src/parser.y"
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
#line 3900 "build/parser.tab.cpp"
    break;

  case 172: /* statement: compound_stmt  */
#line 793 "../phase2-parser/src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3906 "build/parser.tab.cpp"
    break;

  case 173: /* statement: expr_stmt  */
#line 794 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3912 "build/parser.tab.cpp"
    break;

  case 174: /* statement: selection_stmt  */
#line 795 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3918 "build/parser.tab.cpp"
    break;

  case 175: /* statement: iteration_stmt  */
#line 796 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3924 "build/parser.tab.cpp"
    break;

  case 176: /* statement: jump_stmt  */
#line 797 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3930 "build/parser.tab.cpp"
    break;

  case 177: /* statement: labeled_stmt  */
#line 798 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3936 "build/parser.tab.cpp"
    break;

  case 178: /* statement: declaration  */
#line 799 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3942 "build/parser.tab.cpp"
    break;

  case 179: /* statement: error ';'  */
#line 800 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3948 "build/parser.tab.cpp"
    break;

  case 180: /* statement: error '}'  */
#line 801 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3954 "build/parser.tab.cpp"
    break;

  case 181: /* $@12: %empty  */
#line 805 "../phase2-parser/src/parser.y"
          { pushScope(); }
#line 3960 "build/parser.tab.cpp"
    break;

  case 182: /* compound_stmt: '{' $@12 block_item_list_opt '}'  */
#line 805 "../phase2-parser/src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 3971 "build/parser.tab.cpp"
    break;

  case 183: /* block_item_list_opt: %empty  */
#line 814 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3977 "build/parser.tab.cpp"
    break;

  case 184: /* block_item_list_opt: block_item_list  */
#line 815 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[0]; }
#line 3983 "build/parser.tab.cpp"
    break;

  case 185: /* block_item_list: statement  */
#line 819 "../phase2-parser/src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3989 "build/parser.tab.cpp"
    break;

  case 186: /* block_item_list: block_item_list statement  */
#line 820 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3995 "build/parser.tab.cpp"
    break;

  case 187: /* expr_stmt: ';'  */
#line 824 "../phase2-parser/src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 4001 "build/parser.tab.cpp"
    break;

  case 188: /* expr_stmt: expr ';'  */
#line 825 "../phase2-parser/src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 4007 "build/parser.tab.cpp"
    break;

  case 189: /* selection_stmt: IF '(' expr ')' statement  */
#line 829 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4015 "build/parser.tab.cpp"
    break;

  case 190: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 832 "../phase2-parser/src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 4023 "build/parser.tab.cpp"
    break;

  case 191: /* $@13: %empty  */
#line 835 "../phase2-parser/src/parser.y"
                          { hintScope("switch"); }
#line 4029 "build/parser.tab.cpp"
    break;

  case 192: /* selection_stmt: SWITCH '(' expr ')' $@13 compound_stmt  */
#line 835 "../phase2-parser/src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4037 "build/parser.tab.cpp"
    break;

  case 193: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 841 "../phase2-parser/src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4045 "build/parser.tab.cpp"
    break;

  case 194: /* labeled_stmt: DEFAULT ':' statement  */
#line 844 "../phase2-parser/src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4053 "build/parser.tab.cpp"
    break;

  case 195: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 847 "../phase2-parser/src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4063 "build/parser.tab.cpp"
    break;

  case 196: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 855 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4071 "build/parser.tab.cpp"
    break;

  case 197: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 858 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4079 "build/parser.tab.cpp"
    break;

  case 198: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 865 "../phase2-parser/src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4088 "build/parser.tab.cpp"
    break;

  case 199: /* iteration_stmt: DO statement error ';'  */
#line 869 "../phase2-parser/src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4097 "build/parser.tab.cpp"
    break;

  case 200: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 873 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4105 "build/parser.tab.cpp"
    break;

  case 201: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 876 "../phase2-parser/src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4114 "build/parser.tab.cpp"
    break;

  case 202: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 880 "../phase2-parser/src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4123 "build/parser.tab.cpp"
    break;

  case 203: /* for_open: FOR '('  */
#line 889 "../phase2-parser/src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4129 "build/parser.tab.cpp"
    break;

  case 204: /* for_incr_opt: %empty  */
#line 893 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4135 "build/parser.tab.cpp"
    break;

  case 205: /* for_incr_opt: expr  */
#line 894 "../phase2-parser/src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4141 "build/parser.tab.cpp"
    break;

  case 206: /* jump_stmt: BREAK ';'  */
#line 898 "../phase2-parser/src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4147 "build/parser.tab.cpp"
    break;

  case 207: /* jump_stmt: CONTINUE ';'  */
#line 899 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4153 "build/parser.tab.cpp"
    break;

  case 208: /* jump_stmt: RETURN ';'  */
#line 900 "../phase2-parser/src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4159 "build/parser.tab.cpp"
    break;

  case 209: /* jump_stmt: RETURN expr ';'  */
#line 901 "../phase2-parser/src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4165 "build/parser.tab.cpp"
    break;

  case 210: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 902 "../phase2-parser/src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4177 "build/parser.tab.cpp"
    break;

  case 211: /* expr: assignment_expr  */
#line 912 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4183 "build/parser.tab.cpp"
    break;

  case 212: /* expr: expr ',' assignment_expr  */
#line 913 "../phase2-parser/src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4189 "build/parser.tab.cpp"
    break;

  case 213: /* assignment_expr: binary_expr  */
#line 917 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4195 "build/parser.tab.cpp"
    break;

  case 214: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 918 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4203 "build/parser.tab.cpp"
    break;

  case 215: /* assign_op: '='  */
#line 924 "../phase2-parser/src/parser.y"
                   { yyval.str = "="; }
#line 4209 "build/parser.tab.cpp"
    break;

  case 216: /* assign_op: PLUS_ASSIGN  */
#line 925 "../phase2-parser/src/parser.y"
                   { yyval.str = "+="; }
#line 4215 "build/parser.tab.cpp"
    break;

  case 217: /* assign_op: MINUS_ASSIGN  */
#line 926 "../phase2-parser/src/parser.y"
                   { yyval.str = "-="; }
#line 4221 "build/parser.tab.cpp"
    break;

  case 218: /* assign_op: MUL_ASSIGN  */
#line 927 "../phase2-parser/src/parser.y"
                   { yyval.str = "*="; }
#line 4227 "build/parser.tab.cpp"
    break;

  case 219: /* assign_op: DIV_ASSIGN  */
#line 928 "../phase2-parser/src/parser.y"
                   { yyval.str = "/="; }
#line 4233 "build/parser.tab.cpp"
    break;

  case 220: /* assign_op: MOD_ASSIGN  */
#line 929 "../phase2-parser/src/parser.y"
                   { yyval.str = "%="; }
#line 4239 "build/parser.tab.cpp"
    break;

  case 221: /* assign_op: AND_ASSIGN  */
#line 930 "../phase2-parser/src/parser.y"
                   { yyval.str = "&="; }
#line 4245 "build/parser.tab.cpp"
    break;

  case 222: /* assign_op: OR_ASSIGN  */
#line 931 "../phase2-parser/src/parser.y"
                   { yyval.str = "|="; }
#line 4251 "build/parser.tab.cpp"
    break;

  case 223: /* assign_op: XOR_ASSIGN  */
#line 932 "../phase2-parser/src/parser.y"
                   { yyval.str = "^="; }
#line 4257 "build/parser.tab.cpp"
    break;

  case 224: /* assign_op: SHL_ASSIGN  */
#line 933 "../phase2-parser/src/parser.y"
                   { yyval.str = "<<="; }
#line 4263 "build/parser.tab.cpp"
    break;

  case 225: /* assign_op: SHR_ASSIGN  */
#line 934 "../phase2-parser/src/parser.y"
                   { yyval.str = ">>="; }
#line 4269 "build/parser.tab.cpp"
    break;

  case 226: /* constant_expr: binary_expr  */
#line 938 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4275 "build/parser.tab.cpp"
    break;

  case 227: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 942 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4281 "build/parser.tab.cpp"
    break;

  case 228: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 943 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4287 "build/parser.tab.cpp"
    break;

  case 229: /* binary_expr: binary_expr '|' binary_expr  */
#line 944 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4293 "build/parser.tab.cpp"
    break;

  case 230: /* binary_expr: binary_expr '^' binary_expr  */
#line 945 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4299 "build/parser.tab.cpp"
    break;

  case 231: /* binary_expr: binary_expr '&' binary_expr  */
#line 946 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4305 "build/parser.tab.cpp"
    break;

  case 232: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 947 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4311 "build/parser.tab.cpp"
    break;

  case 233: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 948 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4317 "build/parser.tab.cpp"
    break;

  case 234: /* binary_expr: binary_expr '<' binary_expr  */
#line 949 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4323 "build/parser.tab.cpp"
    break;

  case 235: /* binary_expr: binary_expr '>' binary_expr  */
#line 950 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4329 "build/parser.tab.cpp"
    break;

  case 236: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 951 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4335 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 952 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4341 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr SHL binary_expr  */
#line 953 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4347 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr SHR binary_expr  */
#line 954 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4353 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr '+' binary_expr  */
#line 955 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4359 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr '-' binary_expr  */
#line 956 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4365 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr '*' binary_expr  */
#line 957 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4371 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: binary_expr '/' binary_expr  */
#line 958 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4377 "build/parser.tab.cpp"
    break;

  case 244: /* binary_expr: binary_expr '%' binary_expr  */
#line 959 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4383 "build/parser.tab.cpp"
    break;

  case 245: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 960 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4391 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: unary_expr  */
#line 963 "../phase2-parser/src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4397 "build/parser.tab.cpp"
    break;

  case 247: /* unary_expr: postfix_expr  */
#line 967 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4403 "build/parser.tab.cpp"
    break;

  case 248: /* unary_expr: INC unary_expr  */
#line 968 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4409 "build/parser.tab.cpp"
    break;

  case 249: /* unary_expr: DEC unary_expr  */
#line 969 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4415 "build/parser.tab.cpp"
    break;

  case 250: /* unary_expr: '&' unary_expr  */
#line 970 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4421 "build/parser.tab.cpp"
    break;

  case 251: /* unary_expr: '*' unary_expr  */
#line 971 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4427 "build/parser.tab.cpp"
    break;

  case 252: /* unary_expr: '+' unary_expr  */
#line 972 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4433 "build/parser.tab.cpp"
    break;

  case 253: /* unary_expr: '-' unary_expr  */
#line 973 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4439 "build/parser.tab.cpp"
    break;

  case 254: /* unary_expr: '!' unary_expr  */
#line 974 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4445 "build/parser.tab.cpp"
    break;

  case 255: /* unary_expr: '~' unary_expr  */
#line 975 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4451 "build/parser.tab.cpp"
    break;

  case 256: /* unary_expr: '(' type_name ')' unary_expr  */
#line 976 "../phase2-parser/src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4460 "build/parser.tab.cpp"
    break;

  case 257: /* unary_expr: SIZEOF unary_expr  */
#line 980 "../phase2-parser/src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4466 "build/parser.tab.cpp"
    break;

  case 258: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 981 "../phase2-parser/src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4475 "build/parser.tab.cpp"
    break;

  case 259: /* unary_expr: NEW new_type_id  */
#line 985 "../phase2-parser/src/parser.y"
                      {
          yyval.node = atToken(mkNode(ASTKind::NewExpr, yyvsp[0].str), yyvsp[-1].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4484 "build/parser.tab.cpp"
    break;

  case 260: /* unary_expr: NEW new_type_id '(' constructor_args_opt ')'  */
#line 989 "../phase2-parser/src/parser.y"
                                                   {
          yyval.node = atToken(mkNode(ASTKind::NewExpr, yyvsp[-3].str), yyvsp[-4].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-3].typeSpec, yyvsp[-3].decl);
          auto c = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].str), yyvsp[-2].idx);
          c->typeExpr = yyval.node->typeExpr;
          for (auto &a : yyvsp[-1].nodeList) addChild(c, a);
          addChild(yyval.node, c);
      }
#line 4497 "build/parser.tab.cpp"
    break;

  case 261: /* unary_expr: DELETE unary_expr  */
#line 997 "../phase2-parser/src/parser.y"
                        { yyval.node = atToken(mkNode(ASTKind::DeleteExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4503 "build/parser.tab.cpp"
    break;

  case 262: /* unary_expr: DELETE_ARRAY unary_expr  */
#line 998 "../phase2-parser/src/parser.y"
                              { yyval.node = atToken(mkNode(ASTKind::DeleteExpr, "[]", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4509 "build/parser.tab.cpp"
    break;

  case 263: /* type_name: type_name_specifiers  */
#line 1002 "../phase2-parser/src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4518 "build/parser.tab.cpp"
    break;

  case 264: /* type_name: type_name_specifiers abstract_declarator  */
#line 1006 "../phase2-parser/src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4527 "build/parser.tab.cpp"
    break;

  case 265: /* new_type_id: type_name_specifiers  */
#line 1015 "../phase2-parser/src/parser.y"
                                              {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4536 "build/parser.tab.cpp"
    break;

  case 266: /* new_type_id: type_name_specifiers new_pointer  */
#line 1019 "../phase2-parser/src/parser.y"
                                                          {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, 0);
          yyval.decl = yyvsp[0].decl;
      }
#line 4545 "build/parser.tab.cpp"
    break;

  case 267: /* new_type_id: type_name_specifiers new_array_dims  */
#line 1023 "../phase2-parser/src/parser.y"
                                          {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, 0, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4554 "build/parser.tab.cpp"
    break;

  case 268: /* new_type_id: type_name_specifiers new_pointer new_array_dims  */
#line 1027 "../phase2-parser/src/parser.y"
                                                      {
          yyval.str = computeTypeStr(yyvsp[-2].typeSpec, yyvsp[-1].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
          yyval.decl.pointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps;
      }
#line 4565 "build/parser.tab.cpp"
    break;

  case 269: /* new_pointer: '*'  */
#line 1036 "../phase2-parser/src/parser.y"
                      { yyval.decl = DeclInfo(); yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 4571 "build/parser.tab.cpp"
    break;

  case 270: /* new_pointer: new_pointer '*'  */
#line 1037 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 4577 "build/parser.tab.cpp"
    break;

  case 271: /* new_array_dims: '[' expr ']'  */
#line 1042 "../phase2-parser/src/parser.y"
                   { yyval.decl = DeclInfo(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 4583 "build/parser.tab.cpp"
    break;

  case 272: /* new_array_dims: new_array_dims '[' expr ']'  */
#line 1043 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 4589 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1047 "../phase2-parser/src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isVolatile) yyval.typeSpec.isVolatile = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4602 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifiers: type_name_specifier  */
#line 1055 "../phase2-parser/src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4608 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: INT  */
#line 1059 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4614 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: CHAR  */
#line 1060 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4620 "build/parser.tab.cpp"
    break;

  case 277: /* type_name_specifier: FLOAT  */
#line 1061 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4626 "build/parser.tab.cpp"
    break;

  case 278: /* type_name_specifier: DOUBLE  */
#line 1062 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4632 "build/parser.tab.cpp"
    break;

  case 279: /* type_name_specifier: VOID  */
#line 1063 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4638 "build/parser.tab.cpp"
    break;

  case 280: /* type_name_specifier: BOOL  */
#line 1064 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4644 "build/parser.tab.cpp"
    break;

  case 281: /* type_name_specifier: SHORT  */
#line 1065 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4650 "build/parser.tab.cpp"
    break;

  case 282: /* type_name_specifier: LONG  */
#line 1066 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4656 "build/parser.tab.cpp"
    break;

  case 283: /* type_name_specifier: SIGNED  */
#line 1067 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4662 "build/parser.tab.cpp"
    break;

  case 284: /* type_name_specifier: UNSIGNED  */
#line 1068 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4668 "build/parser.tab.cpp"
    break;

  case 285: /* type_name_specifier: VA_LIST  */
#line 1069 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4674 "build/parser.tab.cpp"
    break;

  case 286: /* type_name_specifier: CONST  */
#line 1070 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4680 "build/parser.tab.cpp"
    break;

  case 287: /* type_name_specifier: VOLATILE  */
#line 1071 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isVolatile = true; }
#line 4686 "build/parser.tab.cpp"
    break;

  case 288: /* type_name_specifier: TYPE_NAME  */
#line 1072 "../phase2-parser/src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4700 "build/parser.tab.cpp"
    break;

  case 289: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1081 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4711 "build/parser.tab.cpp"
    break;

  case 290: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1087 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4722 "build/parser.tab.cpp"
    break;

  case 291: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1093 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4733 "build/parser.tab.cpp"
    break;

  case 292: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1099 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4744 "build/parser.tab.cpp"
    break;

  case 293: /* postfix_expr: primary_expr  */
#line 1108 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4750 "build/parser.tab.cpp"
    break;

  case 294: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1109 "../phase2-parser/src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4756 "build/parser.tab.cpp"
    break;

  case 295: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1110 "../phase2-parser/src/parser.y"
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
#line 4796 "build/parser.tab.cpp"
    break;

  case 296: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1145 "../phase2-parser/src/parser.y"
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
#line 4811 "build/parser.tab.cpp"
    break;

  case 297: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1155 "../phase2-parser/src/parser.y"
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
#line 4826 "build/parser.tab.cpp"
    break;

  case 298: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1165 "../phase2-parser/src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4832 "build/parser.tab.cpp"
    break;

  case 299: /* postfix_expr: postfix_expr INC  */
#line 1166 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4838 "build/parser.tab.cpp"
    break;

  case 300: /* postfix_expr: postfix_expr DEC  */
#line 1167 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4844 "build/parser.tab.cpp"
    break;

  case 301: /* postfix_expr: builtin_call  */
#line 1168 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4850 "build/parser.tab.cpp"
    break;

  case 302: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1172 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4856 "build/parser.tab.cpp"
    break;

  case 303: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1173 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4862 "build/parser.tab.cpp"
    break;

  case 304: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1174 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4868 "build/parser.tab.cpp"
    break;

  case 305: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1175 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4874 "build/parser.tab.cpp"
    break;

  case 306: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1176 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4880 "build/parser.tab.cpp"
    break;

  case 307: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1177 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4886 "build/parser.tab.cpp"
    break;

  case 308: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1178 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4892 "build/parser.tab.cpp"
    break;

  case 309: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1179 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4898 "build/parser.tab.cpp"
    break;

  case 310: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1180 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4904 "build/parser.tab.cpp"
    break;

  case 311: /* constructor_args_opt: %empty  */
#line 1184 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4910 "build/parser.tab.cpp"
    break;

  case 312: /* constructor_args_opt: constructor_args  */
#line 1185 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4916 "build/parser.tab.cpp"
    break;

  case 313: /* argument_list_opt: %empty  */
#line 1189 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4922 "build/parser.tab.cpp"
    break;

  case 314: /* argument_list_opt: argument_list  */
#line 1190 "../phase2-parser/src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4928 "build/parser.tab.cpp"
    break;

  case 315: /* argument_list: argument  */
#line 1194 "../phase2-parser/src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4934 "build/parser.tab.cpp"
    break;

  case 316: /* argument_list: argument_list ',' argument  */
#line 1195 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4940 "build/parser.tab.cpp"
    break;

  case 317: /* argument: assignment_expr  */
#line 1199 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4946 "build/parser.tab.cpp"
    break;

  case 318: /* argument: type_name  */
#line 1200 "../phase2-parser/src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4955 "build/parser.tab.cpp"
    break;

  case 319: /* primary_expr: IDENTIFIER  */
#line 1207 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 4969 "build/parser.tab.cpp"
    break;

  case 320: /* primary_expr: INT_LITERAL  */
#line 1216 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4975 "build/parser.tab.cpp"
    break;

  case 321: /* primary_expr: FLOAT_LITERAL  */
#line 1217 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4981 "build/parser.tab.cpp"
    break;

  case 322: /* primary_expr: CHAR_LITERAL  */
#line 1218 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4987 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: string_literal  */
#line 1219 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4993 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: BOOL_LITERAL  */
#line 1220 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4999 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: THIS  */
#line 1221 "../phase2-parser/src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 5005 "build/parser.tab.cpp"
    break;

  case 326: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1222 "../phase2-parser/src/parser.y"
                                             {
          /* `Dog(4)`: a temporary object (for a scalar type, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5014 "build/parser.tab.cpp"
    break;

  case 327: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1226 "../phase2-parser/src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5024 "build/parser.tab.cpp"
    break;

  case 328: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1233 "../phase2-parser/src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5030 "build/parser.tab.cpp"
    break;

  case 329: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1234 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5036 "build/parser.tab.cpp"
    break;

  case 330: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1235 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5042 "build/parser.tab.cpp"
    break;

  case 331: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1236 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5048 "build/parser.tab.cpp"
    break;

  case 332: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1237 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5054 "build/parser.tab.cpp"
    break;

  case 333: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1238 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5060 "build/parser.tab.cpp"
    break;

  case 334: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1239 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5066 "build/parser.tab.cpp"
    break;

  case 335: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1240 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5072 "build/parser.tab.cpp"
    break;

  case 336: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1241 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5078 "build/parser.tab.cpp"
    break;

  case 337: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1242 "../phase2-parser/src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5084 "build/parser.tab.cpp"
    break;

  case 338: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1243 "../phase2-parser/src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 5096 "build/parser.tab.cpp"
    break;

  case 339: /* primary_expr: '(' expr ')'  */
#line 1250 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 5102 "build/parser.tab.cpp"
    break;

  case 340: /* string_literal: STRING_LITERAL  */
#line 1255 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5108 "build/parser.tab.cpp"
    break;

  case 341: /* string_literal: string_literal STRING_LITERAL  */
#line 1256 "../phase2-parser/src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 5118 "build/parser.tab.cpp"
    break;


#line 5122 "build/parser.tab.cpp"

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

#line 1263 "../phase2-parser/src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
