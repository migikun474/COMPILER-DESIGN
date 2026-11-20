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
  YYSYMBOL_FRIEND = 23,                    /* FRIEND  */
  YYSYMBOL_VIRTUAL = 24,                   /* VIRTUAL  */
  YYSYMBOL_EXPLICIT = 25,                  /* EXPLICIT  */
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
  YYSYMBOL_out_of_class_special = 140,     /* out_of_class_special  */
  YYSYMBOL_141_8 = 141,                    /* $@8  */
  YYSYMBOL_142_9 = 142,                    /* $@9  */
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
  YYSYMBOL_163_10 = 163,                   /* $@10  */
  YYSYMBOL_statement = 164,                /* statement  */
  YYSYMBOL_compound_stmt = 165,            /* compound_stmt  */
  YYSYMBOL_166_11 = 166,                   /* $@11  */
  YYSYMBOL_block_item_list_opt = 167,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 168,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 169,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 170,           /* selection_stmt  */
  YYSYMBOL_171_12 = 171,                   /* $@12  */
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

#line 358 "build/parser.tab.cpp"

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
#define YYLAST   2141

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  116
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  78
/* YYNRULES -- Number of rules.  */
#define YYNRULES  322
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  573

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
       0,   140,   140,   144,   152,   153,   154,   155,   156,   160,
     191,   205,   209,   210,   211,   212,   213,   214,   215,   219,
     220,   221,   222,   223,   224,   225,   226,   227,   228,   229,
     230,   244,   251,   252,   256,   260,   256,   276,   276,   290,
     296,   302,   306,   302,   318,   318,   332,   338,   347,   348,
     352,   353,   357,   358,   365,   371,   377,   383,   394,   399,
     411,   412,   413,   414,   423,   423,   441,   445,   453,   457,
     453,   477,   478,   479,   483,   484,   488,   489,   493,   494,
     498,   499,   500,   505,   513,   514,   518,   519,   522,   528,
     529,   530,   531,   532,   536,   542,   548,   549,   555,   559,
     568,   569,   570,   571,   575,   579,   586,   598,   607,   611,
     618,   625,   644,   651,   652,   657,   661,   661,   661,   661,
     662,   662,   662,   662,   663,   663,   663,   663,   664,   664,
     664,   664,   665,   665,   665,   665,   666,   666,   666,   667,
     667,   667,   668,   668,   668,   669,   669,   669,   670,   670,
     670,   677,   681,   682,   686,   687,   691,   695,   699,   703,
     708,   713,   721,   721,   786,   787,   788,   789,   790,   791,
     792,   793,   794,   798,   798,   807,   808,   812,   813,   817,
     818,   822,   825,   828,   828,   834,   837,   840,   848,   851,
     858,   862,   866,   869,   873,   882,   886,   887,   891,   892,
     893,   894,   895,   905,   906,   910,   911,   917,   918,   919,
     920,   921,   922,   923,   924,   925,   926,   927,   931,   935,
     936,   937,   938,   939,   940,   941,   942,   943,   944,   945,
     946,   947,   948,   949,   950,   951,   952,   953,   956,   960,
     961,   962,   963,   964,   965,   966,   967,   968,   969,   973,
     974,   981,   985,   992,   999,  1003,  1004,  1005,  1006,  1007,
    1008,  1009,  1010,  1011,  1012,  1013,  1014,  1015,  1024,  1030,
    1036,  1042,  1051,  1052,  1053,  1088,  1092,  1100,  1106,  1110,
    1111,  1112,  1113,  1117,  1118,  1119,  1120,  1121,  1122,  1123,
    1124,  1125,  1129,  1130,  1134,  1135,  1139,  1140,  1144,  1145,
    1152,  1161,  1162,  1163,  1164,  1165,  1166,  1167,  1171,  1178,
    1179,  1180,  1181,  1182,  1183,  1184,  1185,  1186,  1187,  1188,
    1195,  1200,  1201
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
  "AUTO", "EXTERN", "CONST", "FRIEND", "VIRTUAL", "EXPLICIT", "IF", "ELSE",
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
  "constructor_def", "out_of_class_special", "$@8", "$@9",
  "access_specifier", "init_declarator_list_opt", "init_declarator_list",
  "init_declarator", "initializer", "initializer_list", "initializer_item",
  "pointer", "declarator", "abstract_declarator",
  "direct_abstract_declarator", "direct_declarator",
  "operator_function_id", "overloadable_operator", "param_scope",
  "constructor_args", "parameter_list_opt", "parameter_list",
  "parameter_decl", "function_definition", "$@10", "statement",
  "compound_stmt", "$@11", "block_item_list_opt", "block_item_list",
  "expr_stmt", "selection_stmt", "$@12", "labeled_stmt", "iteration_stmt",
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

#define YYPACT_NINF (-394)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-177)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -394,  1886,  -394,   -83,  -394,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,   -31,   -12,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,    -6,  -394,  -394,  1763,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,   -67,   -17,  -394,  -394,    77,    80,
    -394,  -394,    44,  1952,    88,    99,  -394,  -394,    98,  -394,
      55,    84,  -394,   189,   -15,    89,  -394,  1907,    92,  1907,
     128,   112,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,   105,   108,  -394,   -25,    -7,
      99,   111,  -394,    98,  -394,  -394,  -394,    89,  1112,   122,
    1780,   417,  -394,  -394,  -394,   134,  -394,  -394,   130,  1907,
    -394,   -16,  -394,   167,  -394,  -394,   163,    38,   151,  -394,
    -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,   185,   178,
     187,   194,   204,   207,   209,   211,   212,   214,  -394,   215,
     219,   233,   234,   235,   236,   243,  1566,   246,   247,   248,
     249,  -394,   -45,  -394,  -394,  -394,  -394,  -394,  1633,  1633,
    1633,  1633,  1633,  1633,  1633,  1633,  1499,   964,  -394,  -394,
    1993,   369,   217,  -394,  -394,   256,   666,  1960,    86,  -394,
    -394,   240,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  1907,
    -394,  -394,  -394,   245,  -394,   147,  -394,  1960,  1633,  1633,
    1633,  1633,  1633,  1633,  1633,  1633,  1633,  1499,  1499,  1499,
    1499,  1499,  1499,  1633,  1499,  -394,  1499,  1499,  1499,  1633,
     305,  1633,  -394,  -394,  -394,  -394,  -394,  -394,  -394,  -394,
     178,   187,   194,   204,   207,   209,   211,   212,   214,   154,
     158,  -394,   243,  -394,   -45,   119,  -394,   250,   169,  -394,
     306,  1633,  -394,  -394,   -50,  -394,  1633,  1633,  1633,  1633,
    1633,  1633,  1633,  1633,  1633,  1633,  1633,  1633,  1633,  1633,
    1633,  1633,  1633,  1633,  1633,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,  -394,  1633,   191,   307,  -394,
    -394,   197,  1499,  1633,  -394,   137,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,   257,   258,   261,   890,   262,
     263,  1633,   283,   265,   266,   323,  1294,  -394,   291,   317,
    -394,  -394,  1763,  -394,  -394,   276,   778,  -394,  -394,  -394,
    -394,  1222,  -394,   -64,  1430,   274,   277,  -394,  1633,  -394,
    -394,  1960,   666,   278,    38,  -394,  -394,  1907,   280,   279,
     281,   282,   284,   285,   289,   290,   292,   301,   302,  -394,
    -394,   303,   318,  -394,   315,   319,   325,   326,   327,   339,
     341,   350,   356,   364,   365,  -394,   366,  -394,  -394,  -394,
    -394,  1633,  -394,  1633,  -394,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,   -40,  -394,   485,   165,  -394,   299,
    -394,   312,   304,  1993,  -394,  -394,  1038,   193,   193,   210,
     210,   316,   316,  2035,  2003,   -62,  2044,   569,  1396,   210,
     210,    59,    59,  -394,  -394,  -394,  -394,  -394,   328,  -394,
    -394,   367,   370,    70,  -394,  -394,  1633,  -394,  1633,    19,
    1633,  1633,   345,   890,  -394,  -394,   373,  -394,   -51,   890,
    -394,  -394,  1366,  1366,  -394,   115,  -394,  -394,  -394,   324,
    -394,   371,   375,  -394,  -394,   376,  -394,  -394,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,  -394,  -394,  1499,  -394,  -394,
    -394,  -394,  -394,  -394,  1700,  -394,  -394,  -394,  -394,  -394,
    -394,  -394,   383,  -394,   322,   299,   553,  1112,   353,  -394,
    -394,  1633,   444,   445,  -394,  -394,   144,   148,   390,   396,
     152,   159,   890,  -394,  -394,  -394,  -394,  1633,  1633,  -394,
    -394,  -394,  -394,  -394,   391,  -394,  -394,  -394,  -394,   389,
    -394,  1112,  1993,  -394,  -394,   890,   890,  -394,  1633,   890,
    -394,  -394,   392,   395,   399,  -394,  -394,  -394,   478,  -394,
     184,  -394,   391,   890,   890,   890,    16,  -394,  -394,  -394,
    -394,  -394,  -394
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    19,    20,    21,    22,    23,    25,
      26,    27,    28,     0,     0,    12,    15,    14,    13,    16,
      17,    24,    29,    30,     3,     5,    74,    11,    18,    31,
       6,     4,     7,     8,    39,    40,    37,    34,    46,    47,
      44,    41,     0,     0,   104,    30,    90,    89,     0,    10,
       0,    75,    76,     0,    78,    95,   108,    48,     0,    48,
      50,     0,   137,   138,   135,   136,   131,   132,   129,   130,
     133,   134,   139,   140,   141,   142,   143,   144,   145,   146,
     147,   148,   126,   123,   121,   122,   127,   128,   116,   117,
     118,   119,   120,   125,   124,     0,     0,   115,     0,     0,
       0,     0,     9,     0,    93,    92,    91,    94,     0,     0,
     151,     0,    71,    72,    73,     0,    30,    60,     0,    49,
      58,     0,    63,     0,    61,    35,     0,     0,     0,    68,
     150,   149,   105,   109,   106,   110,   107,    77,    78,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   306,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   300,     0,   301,   302,   303,   321,   305,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    79,    80,
     205,   238,   239,   282,   272,   304,     0,   154,     0,   152,
     113,     0,    64,    38,    59,    67,   173,    66,    62,    48,
      45,    56,    57,    51,    52,     0,    42,   154,   292,   292,
     292,   292,   292,   292,   292,   292,   292,   294,   294,   294,
     294,   294,   294,   292,     0,   249,   294,   294,   294,   292,
       0,   292,   240,   241,   242,   244,   245,   243,   246,   247,
     255,   256,   257,   258,   259,   261,   262,   263,   264,     0,
       0,   266,   260,   265,   267,     0,   203,     0,   251,   254,
       0,     0,    81,    86,     0,    84,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   208,   209,   210,   211,   212,
     213,   214,   215,   216,   217,   207,     0,     0,     0,   280,
     281,     0,   294,     0,   322,     0,    19,    20,    21,    22,
      23,    25,    26,    27,    28,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    24,   300,    30,
     179,   170,    74,   177,   164,     0,     0,   165,   166,   169,
     167,     0,   168,     0,   161,     0,   155,   156,     0,   112,
     114,   154,     0,     0,     0,    54,    55,    48,     0,   293,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   298,
     299,     0,   295,   296,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   319,     0,   268,   269,   270,
     271,     0,   320,     0,   255,   256,   257,   258,   259,   261,
     262,   263,   264,   260,     0,   267,     0,    96,   252,    98,
     253,     0,     0,   218,   238,    82,     0,   230,   231,   228,
     229,   224,   225,   220,   219,     0,   221,   222,   223,   226,
     227,   232,   233,   234,   235,   236,   206,   278,     0,   279,
     275,     0,     0,     0,   171,   172,     0,   195,     0,     0,
       0,     0,     0,     0,   198,   199,     0,   200,     0,     0,
     163,   178,     0,     0,   180,    96,   159,   160,   111,     0,
     153,     0,     0,    36,    53,     0,    69,   309,   310,   311,
     312,   313,   315,   316,   317,   318,   283,     0,   284,   285,
     286,   287,   288,   314,   250,   289,   290,   291,   308,   307,
     204,   248,     0,   100,     0,    97,     0,     0,     0,    83,
      85,     0,     0,     0,   274,   273,     0,     0,     0,     0,
       0,     0,     0,   186,   202,   201,   187,   196,   196,   158,
     157,    65,   174,    43,     0,   297,    99,   101,   102,     0,
      87,     0,   237,   277,   276,     0,     0,   191,     0,     0,
     183,   185,     0,   197,     0,    70,   103,    88,   181,   188,
       0,   192,     0,     0,     0,     0,     0,   184,   194,   193,
     182,   190,   189
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -394,  -394,  -394,     8,    -1,   -19,  -394,   495,  -394,  -394,
    -394,  -394,  -394,  -394,  -394,   -49,  -394,  -394,   160,  -394,
     397,  -394,  -394,  -394,  -394,  -394,  -394,  -116,  -394,  -394,
     412,  -105,  -394,   101,  -246,   -18,  -303,  -393,   -47,   203,
    -394,  -394,   408,  -192,  -394,    52,   522,  -394,  -296,  -120,
    -394,   186,  -394,  -302,  -394,  -394,  -394,  -394,  -394,    18,
    -394,  -155,  -106,  -394,   226,  -193,  -137,  -160,  -394,   293,
    -394,  -394,   523,     9,  -394,    49,  -394,  -394
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    24,   331,   332,    27,    28,    37,    29,    58,
     199,    57,    60,   357,    59,   118,   128,   203,   204,   119,
     120,   121,   351,   122,    30,   207,   534,   123,    50,    51,
      52,   263,   264,   265,    53,   138,   408,   409,    55,    56,
      97,   187,   359,   345,   346,   347,   124,   109,   333,   334,
     352,   335,   336,   337,   338,   562,   339,   340,   341,   552,
     342,   343,   256,   296,   412,   180,   181,   370,   258,   259,
     182,   183,   360,   371,   372,   373,   184,   185
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      26,   197,   179,   178,   189,   191,   107,    49,    54,    25,
     126,   205,   407,   404,   505,   358,   257,   571,   230,   225,
     518,   255,   449,    34,    35,   511,    43,    32,    33,   132,
     101,   232,   233,   234,   235,   236,   237,   238,   239,   463,
     461,   467,    38,    39,    43,   -32,   464,   134,   519,   391,
      46,   391,   112,   113,   114,    47,    26,    42,    26,   525,
     231,   415,   391,   416,   380,   117,   406,   117,   413,   255,
     108,   179,   505,   417,   418,   419,   420,   421,   422,   423,
     424,    36,   426,   427,   428,   429,   430,   431,   432,   433,
     434,   435,   201,   202,   195,   -33,   196,  -162,   465,    61,
      40,   502,   189,   189,   189,   189,   189,   189,   189,   189,
     189,   369,   369,   369,   369,   369,   369,   189,    26,   425,
     369,   369,   369,   189,   414,   189,   572,   117,   413,   414,
     414,   414,   414,   414,   414,   414,   414,   104,   414,   414,
     414,   414,   414,   414,   414,   414,   414,   414,   443,    43,
     353,    98,    44,   100,   282,   283,   284,   523,   407,   471,
     527,   528,    99,   526,   -32,   102,    43,   -33,   404,    44,
     100,   458,   394,   395,   396,   397,   398,   399,   400,   401,
     402,   249,   250,   391,   414,   515,   344,   104,    46,   -32,
     436,   251,   -33,    47,   110,   111,   369,   103,    26,   348,
     349,   355,   356,    48,   125,   105,   344,   117,   387,   388,
     106,   104,   389,   390,   403,   127,   253,   129,   404,   130,
      48,   406,   404,   131,   405,   136,   551,   374,   375,   376,
     377,   378,   391,   392,   186,   381,   382,   383,   205,   192,
      43,   193,   470,    44,   100,   437,   438,   444,   445,   558,
     559,   440,   441,   561,   198,   105,   501,   391,   545,    46,
     106,   391,   546,   206,    47,   391,   549,   568,   569,   570,
     108,   406,   391,   550,   200,   406,   266,   267,   297,   105,
     298,   299,   300,   208,   106,   500,   280,   281,   282,   283,
     284,   516,   209,   517,    48,   520,   521,   391,   566,   210,
     504,   133,   135,   280,   281,   282,   283,   284,   475,   211,
     179,   442,   212,    49,   213,   304,   214,   215,   542,   216,
     217,   301,   302,   303,   218,    49,   466,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,   219,   220,
     221,   222,    15,    16,    17,    18,    19,    20,   223,   462,
     344,   226,   227,   228,   229,   350,    26,   501,   354,   385,
     411,   439,   446,   447,   393,   117,   448,   450,   451,    21,
     453,    22,   553,   553,   414,   454,   455,   456,   459,   116,
     230,   369,   266,   267,   268,   269,   529,   460,   468,   473,
     469,   512,   348,   560,   476,   477,   478,   507,   479,   480,
     539,   179,   540,   481,   482,   506,   483,   278,   279,   280,
     281,   282,   283,   284,   555,   484,   485,   486,   107,   508,
     139,   140,   141,   142,   143,   144,   145,   146,   147,   488,
     513,   487,   522,   489,   148,   179,   557,   537,   541,   490,
     491,   492,   567,   285,   286,   287,   288,   289,   290,   291,
     292,   293,   294,   493,   295,   494,   149,   150,   151,   152,
     153,   154,   155,   156,   495,   157,   158,   159,   344,   160,
     496,   161,   162,   163,   164,   165,   166,   167,   497,   498,
     499,   168,   169,   524,   514,   531,   532,   533,   139,   140,
     141,   142,   143,   144,   145,   146,   147,   536,   543,   544,
     547,   548,   148,   196,   556,   565,   563,   170,   391,    41,
     171,   172,   173,   564,   474,   137,   194,   510,   188,   174,
     175,   530,   176,    31,   149,   150,   151,   152,   153,   154,
     155,   156,   190,   157,   158,   159,   535,   160,   472,   161,
     162,   163,   164,   165,   166,   167,   554,   452,     0,   168,
     169,   410,     0,     0,     0,     0,   139,   140,   141,   142,
     143,   144,   145,   146,   147,     0,     0,     0,     0,     0,
     148,     0,     0,     0,     0,   170,     0,     0,   171,   172,
     173,     0,     0,     0,     0,     0,     0,   174,   175,     0,
     176,     0,   149,   150,   151,   152,   153,   154,   155,   156,
     503,   157,   158,   159,     0,   160,     0,   161,   162,   163,
     164,   165,   166,   167,     0,     0,     0,   168,   169,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   266,   267,   268,   269,   270,
     271,     0,     0,   170,     0,     0,   171,   172,   173,     0,
       0,     0,     0,     0,     0,   174,   175,     0,   176,   277,
     278,   279,   280,   281,   282,   283,   284,   305,   538,   306,
     307,   308,   309,   310,   311,   312,   313,   314,    13,    14,
       0,     0,     0,   148,    15,    16,    17,    18,    19,    20,
       0,     0,   315,     0,   316,   317,   318,   319,   320,   321,
     322,   323,   324,   325,   326,   149,   150,   151,   152,   153,
     154,   327,   156,    22,   157,   158,   159,     0,   160,     0,
     328,   329,   163,   164,   165,   166,   167,     0,     0,     0,
     168,   169,   361,   362,   363,   364,   365,   366,   367,   368,
       0,     0,     0,     0,     0,     0,   379,     0,     0,     0,
       0,     0,   384,     0,   386,     0,   170,     0,     0,   171,
     172,   173,     0,     0,     0,     0,     0,     0,   174,   175,
       0,   176,     0,     0,     0,     0,   330,  -175,   196,   305,
       0,   306,   307,   308,   309,   310,   311,   312,   313,   314,
      13,    14,     0,     0,     0,   148,    15,    16,    17,    18,
      19,    20,     0,     0,   315,     0,   316,   317,   318,   319,
     320,   321,   322,   323,   324,   325,   326,   149,   150,   151,
     152,   153,   154,   327,   156,    22,   157,   158,   159,     0,
     160,     0,   328,   329,   163,   164,   165,   166,   167,     0,
       0,     0,   168,   169,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   170,     0,
       0,   171,   172,   173,     0,     0,     0,     0,     0,     0,
     174,   175,     0,   176,     0,     0,     0,     0,   330,  -176,
     196,   305,     0,   306,   307,   308,   309,   310,   311,   312,
     313,   314,    13,    14,     0,     0,     0,   148,    15,    16,
      17,    18,    19,    20,     0,     0,   315,     0,   316,   317,
     318,   319,   320,   321,   322,   323,   324,   325,   326,   149,
     150,   151,   152,   153,   154,   327,   156,    22,   157,   158,
     159,     0,   160,     0,   328,   329,   163,   164,   165,   166,
     167,     0,     0,     0,   168,   169,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   139,   140,   141,
     142,   143,   144,   145,   146,   147,     0,     0,     0,     0,
     170,   148,     0,   171,   172,   173,     0,     0,     0,     0,
       0,     0,   174,   175,     0,   176,     0,     0,     0,     0,
     330,     0,   196,   149,   150,   151,   152,   153,   154,   155,
     156,     0,   157,   158,   159,     0,   160,     0,   161,   162,
     163,   164,   165,   166,   167,     0,     0,     0,   168,   169,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   139,   140,   141,   142,   143,   144,   145,   146,   147,
       0,     0,     0,     0,   170,   148,     0,   171,   172,   173,
       0,     0,     0,     0,     0,     0,   174,   175,   260,   176,
     261,     0,     0,     0,     0,   262,   177,   149,   150,   151,
     152,   153,   154,   155,   156,     0,   157,   158,   159,     0,
     160,     0,   161,   162,   163,   164,   165,   166,   167,     0,
       0,     0,   168,   169,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   139,   140,   141,   142,   143,
     144,   145,   146,   147,     0,     0,     0,     0,   170,   148,
       0,   171,   172,   173,     0,     0,     0,     0,     0,     0,
     174,   175,   260,   176,   261,     0,     0,     0,     0,   509,
     177,   149,   150,   151,   152,   153,   154,   155,   156,     0,
     157,   158,   159,     0,   160,     0,   161,   162,   163,   164,
     165,   166,   167,     0,     0,     0,   168,   169,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   170,     0,     0,   171,   172,   173,     0,     0,
       0,     0,     0,     0,   174,   175,     0,   176,     0,     0,
       0,     0,     0,     0,   177,   306,   307,   308,   309,   310,
     311,   312,   313,   314,    13,    14,     0,     0,     0,   148,
      15,    16,    17,    18,    19,    20,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   149,   150,   151,   152,   153,   154,   327,   156,    22,
     157,   158,   159,     0,   160,     0,   161,   329,   163,   164,
     165,   166,   167,     0,     0,     0,   168,   169,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   139,   140,   141,
     142,   143,   144,   145,   146,   147,     0,     0,     0,     0,
       0,   148,   170,     0,     0,   171,   172,   173,     0,     0,
       0,     0,     0,     0,   174,   175,     0,   176,     0,     0,
       0,     0,   330,   149,   150,   151,   152,   153,   154,   155,
     156,     0,   157,   158,   159,     0,   160,     0,   161,   162,
     163,   164,   165,   166,   167,     0,     0,     0,   168,   169,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   139,
     140,   141,   142,   143,   144,   145,   146,   147,     0,     0,
       0,     0,     0,   148,   170,     0,     0,   171,   172,   173,
       0,     0,     0,     0,     0,     0,   174,   175,     0,   176,
       0,     0,     0,     0,   457,   149,   150,   151,   152,   153,
     154,   155,   156,     0,   157,   158,   159,     0,   160,     0,
     161,   162,   163,   164,   165,   166,   167,     0,     0,     0,
     168,   169,     0,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,     0,     0,     0,     0,    15,    16,
      17,    18,    19,    20,     0,     0,   170,     0,     0,   171,
     172,   173,   266,   267,   268,   269,   270,   271,   174,   175,
       0,   176,     0,     0,     0,    21,   330,    22,     0,     0,
       0,    43,     0,   404,    44,    45,     0,   278,   279,   280,
     281,   282,   283,   284,     0,     0,     0,     0,     0,     0,
       0,     0,   240,   241,   242,   243,   244,   245,   246,   247,
     248,   249,   250,     0,     0,     0,   148,     0,     0,     0,
      46,   251,     0,     0,     0,    47,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    48,   406,     0,   149,   150,
     151,   152,   153,   154,   252,   156,   253,   157,   158,   159,
       0,   160,     0,   161,   254,   163,   164,   165,   166,   167,
       0,     0,     0,   168,   169,     0,     0,     0,     0,   139,
     140,   141,   142,   143,   144,   145,   146,   147,     0,     0,
       0,     0,     0,   148,     0,     0,     0,     0,     0,   170,
       0,     0,   171,   172,   173,     0,     0,     0,     0,     0,
       0,   174,   175,     0,   176,   149,   150,   151,   152,   153,
     154,   155,   156,     0,   157,   158,   159,     0,   160,     0,
     161,   162,   163,   164,   165,   166,   167,     0,     0,     0,
     168,   169,     0,     0,     0,     0,   139,   140,   141,   142,
     143,   144,   145,   146,   147,     0,     0,     0,     0,     0,
     148,     0,     0,     0,     0,     0,   170,     0,     0,   171,
     172,   173,     0,     0,     0,     0,     0,     0,   174,   175,
       0,   224,   149,   150,   151,   152,   153,   154,   155,   156,
       0,   157,   158,   159,     0,   160,     0,   161,   162,   163,
     164,   165,   166,   167,     0,     0,     0,   168,   169,     0,
       0,     0,     0,   139,   140,   141,   142,   143,   144,   145,
     146,   147,     0,     0,     0,     0,     0,   148,     0,     0,
       0,     0,     0,   170,     0,     0,   171,   172,   173,     0,
       0,     0,     0,     0,     0,   174,   175,     0,   176,   149,
     150,   151,   152,   153,   154,   155,   156,     0,   157,   158,
     159,     0,   160,     0,   161,   162,   163,   164,   165,   166,
     167,     0,     0,     0,   168,   169,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,     0,     0,     0,
       0,    15,    16,    17,    18,    19,    20,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   148,     0,     0,
       0,     0,   174,   175,     0,   176,     0,     0,    21,     0,
      22,     0,     0,     0,    43,     0,     0,    44,    45,   149,
     150,   151,   152,   153,   154,     0,   156,     0,   157,   158,
     159,     0,   160,     0,   161,     0,   163,   164,   165,   166,
     167,     0,     0,     0,   168,   169,     0,     0,     0,     0,
       0,     0,     0,    46,     0,     0,     0,     0,    47,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    48,     0,
     170,     0,     0,   171,   172,   173,     0,     0,     0,     0,
       0,     0,   174,   175,     0,   176,     2,     3,     0,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
       0,     0,     0,     0,    15,    16,    17,    18,    19,    20,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,   112,   113,   114,     0,    15,    16,    17,    18,    19,
      20,    21,     0,    22,     0,     0,     0,     0,     0,     0,
       0,    23,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    21,     0,    22,     0,     0,     0,     0,     0,
       0,   115,   116,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,     0,     0,     0,     0,    15,    16,
      17,    18,    19,    20,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    21,     0,    22,     0,     0,
       0,     0,     0,     0,     0,   116,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,     0,    82,     0,     0,
      83,    84,    85,    86,    87,    88,    89,    90,    91,    92,
       0,     0,     0,     0,    93,    94,     0,    95,    96,   266,
     267,   268,   269,   270,   271,   272,   273,     0,     0,   266,
     267,   268,   269,   270,   271,   272,     0,     0,     0,   274,
       0,   275,   276,   277,   278,   279,   280,   281,   282,   283,
     284,   275,   276,   277,   278,   279,   280,   281,   282,   283,
     284,   266,   267,   268,   269,   270,   271,     0,     0,     0,
     266,   267,   268,   269,   270,   271,     0,     0,     0,     0,
       0,     0,     0,   275,   276,   277,   278,   279,   280,   281,
     282,   283,   284,   276,   277,   278,   279,   280,   281,   282,
     283,   284
};

static const yytype_int16 yycheck[] =
{
       1,   121,   108,   108,   110,   111,    53,    26,    26,     1,
      59,   127,   258,    53,   407,   207,   176,     1,    63,   156,
       1,   176,   318,    54,    55,    87,    51,   110,   111,    54,
      48,   168,   169,   170,   171,   172,   173,   174,   175,   341,
     336,   344,    54,    55,    51,   112,   110,    54,    29,   113,
      90,   113,    14,    15,    16,    95,    57,    63,    59,   110,
     105,   111,   113,   113,   224,    57,   106,    59,   261,   224,
      85,   177,   465,   266,   267,   268,   269,   270,   271,   272,
     273,   112,   275,   276,   277,   278,   279,   280,   281,   282,
     283,   284,    54,    55,   110,   112,   112,   112,   344,    55,
     112,   404,   208,   209,   210,   211,   212,   213,   214,   215,
     216,   217,   218,   219,   220,   221,   222,   223,   119,   274,
     226,   227,   228,   229,   261,   231,   110,   119,   321,   266,
     267,   268,   269,   270,   271,   272,   273,    22,   275,   276,
     277,   278,   279,   280,   281,   282,   283,   284,   303,    51,
     199,    63,    54,    55,    95,    96,    97,   453,   404,   351,
     462,   463,    63,   459,    87,   110,    51,    87,    53,    54,
      55,   326,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,   113,   321,   115,   187,    22,    90,   112,
     296,    22,   112,    95,   105,   106,   302,   113,   199,   113,
     114,    54,    55,   105,   112,    90,   207,   199,    54,    55,
      95,    22,    54,    55,    45,    87,    47,   105,    53,   114,
     105,   106,    53,   115,    55,   114,   522,   218,   219,   220,
     221,   222,   113,   114,   112,   226,   227,   228,   354,   105,
      51,   111,   348,    54,    55,    54,    55,   110,   111,   545,
     546,    54,    55,   549,    87,    90,   393,   113,   114,    90,
      95,   113,   114,   112,    95,   113,   114,   563,   564,   565,
      85,   106,   113,   114,   111,   106,    66,    67,    61,    90,
      63,    64,    65,   105,    95,   391,    93,    94,    95,    96,
      97,   446,   105,   448,   105,   450,   451,   113,   114,   105,
     406,    98,    99,    93,    94,    95,    96,    97,   357,   105,
     416,   302,   105,   332,   105,    59,   105,   105,   511,   105,
     105,   104,   105,   106,   105,   344,   344,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,   105,   105,
     105,   105,    18,    19,    20,    21,    22,    23,   105,   341,
     351,   105,   105,   105,   105,   115,   357,   494,   113,    54,
      54,    54,   105,   105,   114,   357,   105,   105,   105,    45,
      87,    47,   527,   528,   511,   110,   110,    54,    87,    55,
      63,   487,    66,    67,    68,    69,    62,   111,   114,   111,
     113,    63,   113,   548,   114,   114,   114,    85,   114,   114,
     506,   507,   507,   114,   114,   106,   114,    91,    92,    93,
      94,    95,    96,    97,   534,   114,   114,   114,   465,   115,
       3,     4,     5,     6,     7,     8,     9,    10,    11,   114,
      63,   113,    87,   114,    17,   541,   541,   115,    85,   114,
     114,   114,   562,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,   114,    85,   114,    39,    40,    41,    42,
      43,    44,    45,    46,   114,    48,    49,    50,   469,    52,
     114,    54,    55,    56,    57,    58,    59,    60,   114,   114,
     114,    64,    65,   110,   114,   114,   111,   111,     3,     4,
       5,     6,     7,     8,     9,    10,    11,   114,    54,    54,
     110,   105,    17,   112,   115,    27,   114,    90,   113,    14,
      93,    94,    95,   114,   354,   103,   119,   416,   110,   102,
     103,   469,   105,     1,    39,    40,    41,    42,    43,    44,
      45,    46,   115,    48,    49,    50,   487,    52,   352,    54,
      55,    56,    57,    58,    59,    60,   528,   321,    -1,    64,
      65,   258,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      17,    -1,    -1,    -1,    -1,    90,    -1,    -1,    93,    94,
      95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,
     105,    -1,    39,    40,    41,    42,    43,    44,    45,    46,
     115,    48,    49,    50,    -1,    52,    -1,    54,    55,    56,
      57,    58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    66,    67,    68,    69,    70,
      71,    -1,    -1,    90,    -1,    -1,    93,    94,    95,    -1,
      -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,    90,
      91,    92,    93,    94,    95,    96,    97,     1,   115,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      -1,    -1,    -1,    17,    18,    19,    20,    21,    22,    23,
      -1,    -1,    26,    -1,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    45,    46,    47,    48,    49,    50,    -1,    52,    -1,
      54,    55,    56,    57,    58,    59,    60,    -1,    -1,    -1,
      64,    65,   209,   210,   211,   212,   213,   214,   215,   216,
      -1,    -1,    -1,    -1,    -1,    -1,   223,    -1,    -1,    -1,
      -1,    -1,   229,    -1,   231,    -1,    90,    -1,    -1,    93,
      94,    95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,
      -1,   105,    -1,    -1,    -1,    -1,   110,   111,   112,     1,
      -1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    -1,    -1,    -1,    17,    18,    19,    20,    21,
      22,    23,    -1,    -1,    26,    -1,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    -1,
      52,    -1,    54,    55,    56,    57,    58,    59,    60,    -1,
      -1,    -1,    64,    65,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    -1,
      -1,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,
     102,   103,    -1,   105,    -1,    -1,    -1,    -1,   110,   111,
     112,     1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    17,    18,    19,
      20,    21,    22,    23,    -1,    -1,    26,    -1,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    -1,    52,    -1,    54,    55,    56,    57,    58,    59,
      60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      90,    17,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,
      -1,    -1,   102,   103,    -1,   105,    -1,    -1,    -1,    -1,
     110,    -1,   112,    39,    40,    41,    42,    43,    44,    45,
      46,    -1,    48,    49,    50,    -1,    52,    -1,    54,    55,
      56,    57,    58,    59,    60,    -1,    -1,    -1,    64,    65,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      -1,    -1,    -1,    -1,    90,    17,    -1,    93,    94,    95,
      -1,    -1,    -1,    -1,    -1,    -1,   102,   103,   104,   105,
     106,    -1,    -1,    -1,    -1,   111,   112,    39,    40,    41,
      42,    43,    44,    45,    46,    -1,    48,    49,    50,    -1,
      52,    -1,    54,    55,    56,    57,    58,    59,    60,    -1,
      -1,    -1,    64,    65,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    -1,    -1,    -1,    -1,    90,    17,
      -1,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,
     102,   103,   104,   105,   106,    -1,    -1,    -1,    -1,   111,
     112,    39,    40,    41,    42,    43,    44,    45,    46,    -1,
      48,    49,    50,    -1,    52,    -1,    54,    55,    56,    57,
      58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    -1,    -1,    93,    94,    95,    -1,    -1,
      -1,    -1,    -1,    -1,   102,   103,    -1,   105,    -1,    -1,
      -1,    -1,    -1,    -1,   112,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    -1,    -1,    -1,    17,
      18,    19,    20,    21,    22,    23,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    39,    40,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    -1,    52,    -1,    54,    55,    56,    57,
      58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    17,    90,    -1,    -1,    93,    94,    95,    -1,    -1,
      -1,    -1,    -1,    -1,   102,   103,    -1,   105,    -1,    -1,
      -1,    -1,   110,    39,    40,    41,    42,    43,    44,    45,
      46,    -1,    48,    49,    50,    -1,    52,    -1,    54,    55,
      56,    57,    58,    59,    60,    -1,    -1,    -1,    64,    65,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    -1,    17,    90,    -1,    -1,    93,    94,    95,
      -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,
      -1,    -1,    -1,    -1,   110,    39,    40,    41,    42,    43,
      44,    45,    46,    -1,    48,    49,    50,    -1,    52,    -1,
      54,    55,    56,    57,    58,    59,    60,    -1,    -1,    -1,
      64,    65,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    -1,    18,    19,
      20,    21,    22,    23,    -1,    -1,    90,    -1,    -1,    93,
      94,    95,    66,    67,    68,    69,    70,    71,   102,   103,
      -1,   105,    -1,    -1,    -1,    45,   110,    47,    -1,    -1,
      -1,    51,    -1,    53,    54,    55,    -1,    91,    92,    93,
      94,    95,    96,    97,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    -1,    -1,    -1,    17,    -1,    -1,    -1,
      90,    22,    -1,    -1,    -1,    95,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   105,   106,    -1,    39,    40,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      -1,    52,    -1,    54,    55,    56,    57,    58,    59,    60,
      -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    -1,    17,    -1,    -1,    -1,    -1,    -1,    90,
      -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,
      -1,   102,   103,    -1,   105,    39,    40,    41,    42,    43,
      44,    45,    46,    -1,    48,    49,    50,    -1,    52,    -1,
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
      60,    -1,    -1,    -1,    64,    65,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    -1,    -1,    -1,
      -1,    18,    19,    20,    21,    22,    23,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,
      -1,    -1,   102,   103,    -1,   105,    -1,    -1,    45,    -1,
      47,    -1,    -1,    -1,    51,    -1,    -1,    54,    55,    39,
      40,    41,    42,    43,    44,    -1,    46,    -1,    48,    49,
      50,    -1,    52,    -1,    54,    -1,    56,    57,    58,    59,
      60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    -1,    -1,    -1,    -1,    95,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   105,    -1,
      90,    -1,    -1,    93,    94,    95,    -1,    -1,    -1,    -1,
      -1,    -1,   102,   103,    -1,   105,     0,     1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      -1,    -1,    -1,    -1,    18,    19,    20,    21,    22,    23,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    -1,    18,    19,    20,    21,    22,
      23,    45,    -1,    47,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    47,    -1,    -1,    -1,    -1,    -1,
      -1,    54,    55,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    -1,    -1,    -1,    -1,    18,    19,
      20,    21,    22,    23,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    45,    -1,    47,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    55,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    -1,    85,    -1,    -1,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      -1,    -1,    -1,    -1,   102,   103,    -1,   105,   106,    66,
      67,    68,    69,    70,    71,    72,    73,    -1,    -1,    66,
      67,    68,    69,    70,    71,    72,    -1,    -1,    -1,    86,
      -1,    88,    89,    90,    91,    92,    93,    94,    95,    96,
      97,    88,    89,    90,    91,    92,    93,    94,    95,    96,
      97,    66,    67,    68,    69,    70,    71,    -1,    -1,    -1,
      66,    67,    68,    69,    70,    71,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    89,    90,    91,    92,    93,    94,    95,
      96,    97
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   117,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    18,    19,    20,    21,    22,
      23,    45,    47,    55,   118,   119,   120,   121,   122,   124,
     140,   162,   110,   111,    54,    55,   112,   123,    54,    55,
     112,   123,    63,    51,    54,    55,    90,    95,   105,   121,
     144,   145,   146,   150,   151,   154,   155,   127,   125,   130,
     128,    55,    64,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    85,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,   102,   103,   105,   106,   156,    63,    63,
      55,   151,   110,   113,    22,    90,    95,   154,    85,   163,
     105,   106,    14,    15,    16,    54,    55,   119,   131,   135,
     136,   137,   139,   143,   162,   112,   131,    87,   132,   105,
     114,   115,    54,   155,    54,   155,   114,   146,   151,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    17,    39,
      40,    41,    42,    43,    44,    45,    46,    48,    49,    50,
      52,    54,    55,    56,    57,    58,    59,    60,    64,    65,
      90,    93,    94,    95,   102,   103,   105,   112,   147,   178,
     181,   182,   186,   187,   192,   193,   112,   157,   158,   178,
     115,   178,   105,   111,   136,   110,   112,   165,    87,   126,
     111,    54,    55,   133,   134,   143,   112,   141,   105,   105,
     105,   105,   105,   105,   105,   105,   105,   105,   105,   105,
     105,   105,   105,   105,   105,   182,   105,   105,   105,   105,
      63,   105,   182,   182,   182,   182,   182,   182,   182,   182,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    22,    45,    47,    55,   177,   178,   183,   184,   185,
     104,   106,   111,   147,   148,   149,    66,    67,    68,    69,
      70,    71,    72,    73,    86,    88,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    83,    85,   179,    61,    63,    64,
      65,   104,   105,   106,    59,     1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    26,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    45,    54,    55,
     110,   119,   120,   164,   165,   167,   168,   169,   170,   172,
     173,   174,   176,   177,   120,   159,   160,   161,   113,   114,
     115,   138,   166,   131,   113,    54,    55,   129,   159,   158,
     188,   188,   188,   188,   188,   188,   188,   188,   188,   178,
     183,   189,   190,   191,   189,   189,   189,   189,   189,   188,
     183,   189,   189,   189,   188,    54,   188,    54,    55,    54,
      55,   113,   114,   114,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    45,    53,    55,   106,   150,   152,   153,
     185,    54,   180,   181,   182,   111,   113,   181,   181,   181,
     181,   181,   181,   181,   181,   177,   181,   181,   181,   181,
     181,   181,   181,   181,   181,   181,   178,    54,    55,    54,
      54,    55,   189,   177,   110,   111,   105,   105,   105,   164,
     105,   105,   180,    87,   110,   110,    54,   110,   177,    87,
     111,   164,   119,   169,   110,   150,   151,   152,   114,   113,
     178,   159,   167,   111,   134,   131,   114,   114,   114,   114,
     114,   114,   114,   114,   114,   114,   114,   113,   114,   114,
     114,   114,   114,   114,   114,   114,   114,   114,   114,   114,
     178,   182,   152,   115,   178,   153,   106,    85,   115,   111,
     149,    87,    63,    63,   114,   115,   177,   177,     1,    29,
     177,   177,    87,   164,   110,   110,   164,   169,   169,    62,
     161,   114,   111,   111,   142,   191,   114,   115,   115,   178,
     147,    85,   181,    54,    54,   114,   114,   110,   105,   114,
     114,   164,   175,   177,   175,   165,   115,   147,   164,   164,
     177,   164,   171,   114,   114,    27,   114,   165,   164,   164,
     164,     1,   110
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   116,   117,   117,   118,   118,   118,   118,   118,   119,
     120,   120,   121,   121,   121,   121,   121,   121,   121,   122,
     122,   122,   122,   122,   122,   122,   122,   122,   122,   122,
     122,   122,   123,   123,   125,   126,   124,   127,   124,   124,
     124,   128,   129,   124,   130,   124,   124,   124,   131,   131,
     132,   132,   133,   133,   134,   134,   134,   134,   135,   135,
     136,   136,   136,   136,   138,   137,   139,   139,   141,   142,
     140,   143,   143,   143,   144,   144,   145,   145,   146,   146,
     147,   147,   147,   147,   148,   148,   149,   149,   149,   150,
     150,   150,   150,   150,   151,   151,   152,   152,   152,   153,
     153,   153,   153,   153,   154,   154,   154,   154,   154,   154,
     154,   154,   154,   154,   154,   155,   156,   156,   156,   156,
     156,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   157,   158,   158,   159,   159,   160,   160,   160,   161,
     161,   161,   163,   162,   164,   164,   164,   164,   164,   164,
     164,   164,   164,   166,   165,   167,   167,   168,   168,   169,
     169,   170,   170,   171,   170,   172,   172,   172,   173,   173,
     173,   173,   173,   173,   173,   174,   175,   175,   176,   176,
     176,   176,   176,   177,   177,   178,   178,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   180,   181,
     181,   181,   181,   181,   181,   181,   181,   181,   181,   181,
     181,   181,   181,   181,   181,   181,   181,   181,   181,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   183,   183,   184,   184,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   186,   186,   186,   186,   186,   186,   186,   186,
     186,   186,   186,   187,   187,   187,   187,   187,   187,   187,
     187,   187,   188,   188,   189,   189,   190,   190,   191,   191,
     192,   192,   192,   192,   192,   192,   192,   192,   192,   192,
     192,   192,   192,   192,   192,   192,   192,   192,   192,   192,
     192,   193,   193
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     0,     0,     7,     0,     5,     2,
       2,     0,     0,     8,     0,     5,     2,     2,     0,     1,
       0,     2,     1,     3,     2,     2,     1,     1,     1,     2,
       1,     1,     2,     1,     0,     5,     2,     2,     0,     0,
       9,     1,     1,     1,     0,     1,     1,     3,     1,     3,
       1,     2,     3,     4,     1,     3,     1,     4,     5,     1,
       1,     2,     2,     2,     2,     1,     1,     2,     1,     3,
       2,     3,     3,     4,     1,     3,     3,     3,     1,     3,
       3,     5,     4,     3,     4,     2,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     2,
       2,     0,     1,     3,     0,     1,     1,     3,     3,     2,
       2,     1,     0,     6,     1,     1,     1,     1,     1,     1,
       1,     2,     2,     0,     4,     0,     1,     1,     2,     1,
       2,     5,     7,     0,     6,     4,     3,     3,     5,     7,
       7,     4,     5,     6,     6,     2,     0,     1,     2,     2,
       2,     3,     3,     1,     3,     1,     3,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     5,     1,     1,
       2,     2,     2,     2,     2,     2,     2,     2,     4,     2,
       4,     1,     2,     2,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     2,     2,
       2,     2,     1,     4,     4,     3,     5,     5,     3,     3,
       2,     2,     1,     4,     4,     4,     4,     4,     4,     4,
       4,     4,     0,     1,     0,     1,     1,     3,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     4,     4,     4,
       4,     4,     4,     4,     4,     4,     4,     4,     4,     3,
       3,     1,     2
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
#line 140 "../phase2-parser/src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2442 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 144 "../phase2-parser/src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2452 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 152 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2458 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 153 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2464 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 154 "../phase2-parser/src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2470 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 155 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2476 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 156 "../phase2-parser/src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2482 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 160 "../phase2-parser/src/parser.y"
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
#line 2515 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 191 "../phase2-parser/src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          if (yyvsp[0].typeSpec.isExtern) yyval.typeSpec.isExtern = true;
          yyval.typeSpec.storageClasses += yyvsp[0].typeSpec.storageClasses;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isAuto) yyval.typeSpec.isAuto = true;
          if (yyvsp[0].typeSpec.isFriend) yyval.typeSpec.isFriend = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2534 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 205 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2540 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 209 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2546 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: EXTERN  */
#line 210 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isExtern = true; yyval.typeSpec.storageClasses = 1; }
#line 2552 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: AUTO  */
#line 211 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2558 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: TYPEDEF  */
#line 212 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2564 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: CONST  */
#line 213 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2570 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: FRIEND  */
#line 214 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isFriend = true; }
#line 2576 "build/parser.tab.cpp"
    break;

  case 18: /* storage_or_type_specifier: type_specifier  */
#line 215 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2582 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: INT  */
#line 219 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2588 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: CHAR  */
#line 220 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2594 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: FLOAT  */
#line 221 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2600 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: DOUBLE  */
#line 222 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2606 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: VOID  */
#line 223 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2612 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: BOOL  */
#line 224 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2618 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: SHORT  */
#line 225 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2624 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: LONG  */
#line 226 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2630 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: SIGNED  */
#line 227 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2636 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: UNSIGNED  */
#line 228 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2642 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: VA_LIST  */
#line 229 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2648 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: TYPE_NAME  */
#line 230 "../phase2-parser/src/parser.y"
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
#line 2667 "build/parser.tab.cpp"
    break;

  case 31: /* type_specifier: struct_or_class_specifier  */
#line 244 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2673 "build/parser.tab.cpp"
    break;

  case 32: /* tag_name: IDENTIFIER  */
#line 251 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2679 "build/parser.tab.cpp"
    break;

  case 33: /* tag_name: TYPE_NAME  */
#line 252 "../phase2-parser/src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2685 "build/parser.tab.cpp"
    break;

  case 34: /* $@1: %empty  */
#line 256 "../phase2-parser/src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2695 "build/parser.tab.cpp"
    break;

  case 35: /* $@2: %empty  */
#line 260 "../phase2-parser/src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2701 "build/parser.tab.cpp"
    break;

  case 36: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 260 "../phase2-parser/src/parser.y"
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
#line 2719 "build/parser.tab.cpp"
    break;

  case 37: /* @3: %empty  */
#line 276 "../phase2-parser/src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2731 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 282 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2744 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 290 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2755 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 296 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2766 "build/parser.tab.cpp"
    break;

  case 41: /* $@4: %empty  */
#line 302 "../phase2-parser/src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2776 "build/parser.tab.cpp"
    break;

  case 42: /* $@5: %empty  */
#line 306 "../phase2-parser/src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2782 "build/parser.tab.cpp"
    break;

  case 43: /* struct_or_class_specifier: CLASS tag_name $@4 inheritance_opt '{' $@5 member_decl_list_opt '}'  */
#line 306 "../phase2-parser/src/parser.y"
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
#line 2799 "build/parser.tab.cpp"
    break;

  case 44: /* @6: %empty  */
#line 318 "../phase2-parser/src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2811 "build/parser.tab.cpp"
    break;

  case 45: /* struct_or_class_specifier: CLASS '{' @6 member_decl_list_opt '}'  */
#line 324 "../phase2-parser/src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2824 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 332 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2835 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 338 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2846 "build/parser.tab.cpp"
    break;

  case 48: /* member_decl_list_opt: %empty  */
#line 347 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 2852 "build/parser.tab.cpp"
    break;

  case 49: /* member_decl_list_opt: member_decl_list  */
#line 348 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2858 "build/parser.tab.cpp"
    break;

  case 50: /* inheritance_opt: %empty  */
#line 352 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 2864 "build/parser.tab.cpp"
    break;

  case 51: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 353 "../phase2-parser/src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 2870 "build/parser.tab.cpp"
    break;

  case 52: /* inheritance_specifier_list: inheritance_specifier  */
#line 357 "../phase2-parser/src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2876 "build/parser.tab.cpp"
    break;

  case 53: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 358 "../phase2-parser/src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 2885 "build/parser.tab.cpp"
    break;

  case 54: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 365 "../phase2-parser/src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2896 "build/parser.tab.cpp"
    break;

  case 55: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 371 "../phase2-parser/src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2907 "build/parser.tab.cpp"
    break;

  case 56: /* inheritance_specifier: IDENTIFIER  */
#line 377 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2918 "build/parser.tab.cpp"
    break;

  case 57: /* inheritance_specifier: TYPE_NAME  */
#line 383 "../phase2-parser/src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 2929 "build/parser.tab.cpp"
    break;

  case 58: /* member_decl_list: member_item  */
#line 394 "../phase2-parser/src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 2939 "build/parser.tab.cpp"
    break;

  case 59: /* member_decl_list: member_decl_list member_item  */
#line 399 "../phase2-parser/src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 2953 "build/parser.tab.cpp"
    break;

  case 60: /* member_item: declaration  */
#line 411 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2959 "build/parser.tab.cpp"
    break;

  case 61: /* member_item: function_definition  */
#line 412 "../phase2-parser/src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2965 "build/parser.tab.cpp"
    break;

  case 62: /* member_item: access_specifier ':'  */
#line 413 "../phase2-parser/src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 2971 "build/parser.tab.cpp"
    break;

  case 63: /* member_item: constructor_def  */
#line 414 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 2977 "build/parser.tab.cpp"
    break;

  case 64: /* $@7: %empty  */
#line 423 "../phase2-parser/src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 2983 "build/parser.tab.cpp"
    break;

  case 65: /* constructor_head: IDENTIFIER '(' $@7 parameter_list_opt ')'  */
#line 423 "../phase2-parser/src/parser.y"
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
#line 3003 "build/parser.tab.cpp"
    break;

  case 66: /* constructor_def: constructor_head compound_stmt  */
#line 441 "../phase2-parser/src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3012 "build/parser.tab.cpp"
    break;

  case 67: /* constructor_def: constructor_head ';'  */
#line 445 "../phase2-parser/src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3021 "build/parser.tab.cpp"
    break;

  case 68: /* $@8: %empty  */
#line 453 "../phase2-parser/src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3031 "build/parser.tab.cpp"
    break;

  case 69: /* $@9: %empty  */
#line 457 "../phase2-parser/src/parser.y"
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
#line 3048 "build/parser.tab.cpp"
    break;

  case 70: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@8 parameter_list_opt ')' $@9 compound_stmt  */
#line 468 "../phase2-parser/src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3058 "build/parser.tab.cpp"
    break;

  case 74: /* init_declarator_list_opt: %empty  */
#line 483 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3064 "build/parser.tab.cpp"
    break;

  case 75: /* init_declarator_list_opt: init_declarator_list  */
#line 484 "../phase2-parser/src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3070 "build/parser.tab.cpp"
    break;

  case 76: /* init_declarator_list: init_declarator  */
#line 488 "../phase2-parser/src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3076 "build/parser.tab.cpp"
    break;

  case 77: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 489 "../phase2-parser/src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3082 "build/parser.tab.cpp"
    break;

  case 78: /* init_declarator: declarator  */
#line 493 "../phase2-parser/src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3088 "build/parser.tab.cpp"
    break;

  case 79: /* init_declarator: declarator '=' initializer  */
#line 494 "../phase2-parser/src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3094 "build/parser.tab.cpp"
    break;

  case 80: /* initializer: assignment_expr  */
#line 498 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3100 "build/parser.tab.cpp"
    break;

  case 81: /* initializer: '{' '}'  */
#line 499 "../phase2-parser/src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3106 "build/parser.tab.cpp"
    break;

  case 82: /* initializer: '{' initializer_list '}'  */
#line 500 "../phase2-parser/src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3116 "build/parser.tab.cpp"
    break;

  case 83: /* initializer: '{' initializer_list ',' '}'  */
#line 505 "../phase2-parser/src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3126 "build/parser.tab.cpp"
    break;

  case 84: /* initializer_list: initializer_item  */
#line 513 "../phase2-parser/src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3132 "build/parser.tab.cpp"
    break;

  case 85: /* initializer_list: initializer_list ',' initializer_item  */
#line 514 "../phase2-parser/src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3138 "build/parser.tab.cpp"
    break;

  case 86: /* initializer_item: initializer  */
#line 518 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3144 "build/parser.tab.cpp"
    break;

  case 87: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 519 "../phase2-parser/src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3152 "build/parser.tab.cpp"
    break;

  case 88: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 522 "../phase2-parser/src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3160 "build/parser.tab.cpp"
    break;

  case 89: /* pointer: '*'  */
#line 528 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3166 "build/parser.tab.cpp"
    break;

  case 90: /* pointer: '&'  */
#line 529 "../phase2-parser/src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3172 "build/parser.tab.cpp"
    break;

  case 91: /* pointer: pointer '*'  */
#line 530 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3178 "build/parser.tab.cpp"
    break;

  case 92: /* pointer: pointer '&'  */
#line 531 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3184 "build/parser.tab.cpp"
    break;

  case 93: /* pointer: pointer CONST  */
#line 532 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3190 "build/parser.tab.cpp"
    break;

  case 94: /* declarator: pointer direct_declarator  */
#line 536 "../phase2-parser/src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3201 "build/parser.tab.cpp"
    break;

  case 95: /* declarator: direct_declarator  */
#line 542 "../phase2-parser/src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3207 "build/parser.tab.cpp"
    break;

  case 96: /* abstract_declarator: pointer  */
#line 548 "../phase2-parser/src/parser.y"
              { yyval = yyvsp[0]; }
#line 3213 "build/parser.tab.cpp"
    break;

  case 97: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 549 "../phase2-parser/src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3224 "build/parser.tab.cpp"
    break;

  case 98: /* abstract_declarator: direct_abstract_declarator  */
#line 555 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3230 "build/parser.tab.cpp"
    break;

  case 99: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 559 "../phase2-parser/src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3244 "build/parser.tab.cpp"
    break;

  case 100: /* direct_abstract_declarator: '[' ']'  */
#line 568 "../phase2-parser/src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3250 "build/parser.tab.cpp"
    break;

  case 101: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 569 "../phase2-parser/src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3256 "build/parser.tab.cpp"
    break;

  case 102: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 570 "../phase2-parser/src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3262 "build/parser.tab.cpp"
    break;

  case 103: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 571 "../phase2-parser/src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3268 "build/parser.tab.cpp"
    break;

  case 104: /* direct_declarator: IDENTIFIER  */
#line 575 "../phase2-parser/src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3277 "build/parser.tab.cpp"
    break;

  case 105: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 579 "../phase2-parser/src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3289 "build/parser.tab.cpp"
    break;

  case 106: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 586 "../phase2-parser/src/parser.y"
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
#line 3306 "build/parser.tab.cpp"
    break;

  case 107: /* direct_declarator: '(' declarator ')'  */
#line 598 "../phase2-parser/src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3320 "build/parser.tab.cpp"
    break;

  case 108: /* direct_declarator: operator_function_id  */
#line 607 "../phase2-parser/src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3329 "build/parser.tab.cpp"
    break;

  case 109: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 611 "../phase2-parser/src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3341 "build/parser.tab.cpp"
    break;

  case 110: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 618 "../phase2-parser/src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3353 "build/parser.tab.cpp"
    break;

  case 111: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 625 "../phase2-parser/src/parser.y"
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
#line 3377 "build/parser.tab.cpp"
    break;

  case 112: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 644 "../phase2-parser/src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3389 "build/parser.tab.cpp"
    break;

  case 113: /* direct_declarator: direct_declarator '[' ']'  */
#line 651 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3395 "build/parser.tab.cpp"
    break;

  case 114: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 652 "../phase2-parser/src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3401 "build/parser.tab.cpp"
    break;

  case 115: /* operator_function_id: OPERATOR overloadable_operator  */
#line 657 "../phase2-parser/src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3407 "build/parser.tab.cpp"
    break;

  case 116: /* overloadable_operator: '+'  */
#line 661 "../phase2-parser/src/parser.y"
          { yyval.str = "+"; }
#line 3413 "build/parser.tab.cpp"
    break;

  case 117: /* overloadable_operator: '-'  */
#line 661 "../phase2-parser/src/parser.y"
                                  { yyval.str = "-"; }
#line 3419 "build/parser.tab.cpp"
    break;

  case 118: /* overloadable_operator: '*'  */
#line 661 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "*"; }
#line 3425 "build/parser.tab.cpp"
    break;

  case 119: /* overloadable_operator: '/'  */
#line 661 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3431 "build/parser.tab.cpp"
    break;

  case 120: /* overloadable_operator: '%'  */
#line 662 "../phase2-parser/src/parser.y"
          { yyval.str = "%"; }
#line 3437 "build/parser.tab.cpp"
    break;

  case 121: /* overloadable_operator: '^'  */
#line 662 "../phase2-parser/src/parser.y"
                                  { yyval.str = "^"; }
#line 3443 "build/parser.tab.cpp"
    break;

  case 122: /* overloadable_operator: '&'  */
#line 662 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "&"; }
#line 3449 "build/parser.tab.cpp"
    break;

  case 123: /* overloadable_operator: '|'  */
#line 662 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3455 "build/parser.tab.cpp"
    break;

  case 124: /* overloadable_operator: '~'  */
#line 663 "../phase2-parser/src/parser.y"
          { yyval.str = "~"; }
#line 3461 "build/parser.tab.cpp"
    break;

  case 125: /* overloadable_operator: '!'  */
#line 663 "../phase2-parser/src/parser.y"
                                  { yyval.str = "!"; }
#line 3467 "build/parser.tab.cpp"
    break;

  case 126: /* overloadable_operator: '='  */
#line 663 "../phase2-parser/src/parser.y"
                                                          { yyval.str = "="; }
#line 3473 "build/parser.tab.cpp"
    break;

  case 127: /* overloadable_operator: '<'  */
#line 663 "../phase2-parser/src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3479 "build/parser.tab.cpp"
    break;

  case 128: /* overloadable_operator: '>'  */
#line 664 "../phase2-parser/src/parser.y"
          { yyval.str = ">"; }
#line 3485 "build/parser.tab.cpp"
    break;

  case 129: /* overloadable_operator: EQ_OP  */
#line 664 "../phase2-parser/src/parser.y"
                                    { yyval.str = "=="; }
#line 3491 "build/parser.tab.cpp"
    break;

  case 130: /* overloadable_operator: NE_OP  */
#line 664 "../phase2-parser/src/parser.y"
                                                               { yyval.str = "!="; }
#line 3497 "build/parser.tab.cpp"
    break;

  case 131: /* overloadable_operator: LE_OP  */
#line 664 "../phase2-parser/src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3503 "build/parser.tab.cpp"
    break;

  case 132: /* overloadable_operator: GE_OP  */
#line 665 "../phase2-parser/src/parser.y"
            { yyval.str = ">="; }
#line 3509 "build/parser.tab.cpp"
    break;

  case 133: /* overloadable_operator: AND_OP  */
#line 665 "../phase2-parser/src/parser.y"
                                        { yyval.str = "&&"; }
#line 3515 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: OR_OP  */
#line 665 "../phase2-parser/src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3521 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: SHL  */
#line 665 "../phase2-parser/src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3527 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: SHR  */
#line 666 "../phase2-parser/src/parser.y"
          { yyval.str = ">>"; }
#line 3533 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: INC  */
#line 666 "../phase2-parser/src/parser.y"
                                   { yyval.str = "++"; }
#line 3539 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: DEC  */
#line 666 "../phase2-parser/src/parser.y"
                                                            { yyval.str = "--"; }
#line 3545 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: PLUS_ASSIGN  */
#line 667 "../phase2-parser/src/parser.y"
                  { yyval.str = "+="; }
#line 3551 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: MINUS_ASSIGN  */
#line 667 "../phase2-parser/src/parser.y"
                                                    { yyval.str = "-="; }
#line 3557 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: MUL_ASSIGN  */
#line 667 "../phase2-parser/src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3563 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: DIV_ASSIGN  */
#line 668 "../phase2-parser/src/parser.y"
                 { yyval.str = "/="; }
#line 3569 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: MOD_ASSIGN  */
#line 668 "../phase2-parser/src/parser.y"
                                                 { yyval.str = "%="; }
#line 3575 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: AND_ASSIGN  */
#line 668 "../phase2-parser/src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3581 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: OR_ASSIGN  */
#line 669 "../phase2-parser/src/parser.y"
                { yyval.str = "|="; }
#line 3587 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: XOR_ASSIGN  */
#line 669 "../phase2-parser/src/parser.y"
                                                { yyval.str = "^="; }
#line 3593 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: SHL_ASSIGN  */
#line 669 "../phase2-parser/src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3599 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: SHR_ASSIGN  */
#line 670 "../phase2-parser/src/parser.y"
                 { yyval.str = ">>="; }
#line 3605 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: '[' ']'  */
#line 670 "../phase2-parser/src/parser.y"
                                               { yyval.str = "[]"; }
#line 3611 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: '(' ')'  */
#line 670 "../phase2-parser/src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3617 "build/parser.tab.cpp"
    break;

  case 151: /* param_scope: %empty  */
#line 677 "../phase2-parser/src/parser.y"
                                           { pushScope(); }
#line 3623 "build/parser.tab.cpp"
    break;

  case 152: /* constructor_args: assignment_expr  */
#line 681 "../phase2-parser/src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3629 "build/parser.tab.cpp"
    break;

  case 153: /* constructor_args: constructor_args ',' assignment_expr  */
#line 682 "../phase2-parser/src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3635 "build/parser.tab.cpp"
    break;

  case 154: /* parameter_list_opt: %empty  */
#line 686 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3641 "build/parser.tab.cpp"
    break;

  case 155: /* parameter_list_opt: parameter_list  */
#line 687 "../phase2-parser/src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3647 "build/parser.tab.cpp"
    break;

  case 156: /* parameter_list: parameter_decl  */
#line 691 "../phase2-parser/src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3656 "build/parser.tab.cpp"
    break;

  case 157: /* parameter_list: parameter_list ',' parameter_decl  */
#line 695 "../phase2-parser/src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3665 "build/parser.tab.cpp"
    break;

  case 158: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 699 "../phase2-parser/src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3671 "build/parser.tab.cpp"
    break;

  case 159: /* parameter_decl: declaration_specifiers declarator  */
#line 703 "../phase2-parser/src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3681 "build/parser.tab.cpp"
    break;

  case 160: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 708 "../phase2-parser/src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3691 "build/parser.tab.cpp"
    break;

  case 161: /* parameter_decl: declaration_specifiers  */
#line 713 "../phase2-parser/src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3701 "build/parser.tab.cpp"
    break;

  case 162: /* $@10: %empty  */
#line 721 "../phase2-parser/src/parser.y"
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
#line 3743 "build/parser.tab.cpp"
    break;

  case 163: /* function_definition: declaration_specifiers declarator $@10 '{' block_item_list_opt '}'  */
#line 757 "../phase2-parser/src/parser.y"
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
#line 3774 "build/parser.tab.cpp"
    break;

  case 164: /* statement: compound_stmt  */
#line 786 "../phase2-parser/src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3780 "build/parser.tab.cpp"
    break;

  case 165: /* statement: expr_stmt  */
#line 787 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3786 "build/parser.tab.cpp"
    break;

  case 166: /* statement: selection_stmt  */
#line 788 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3792 "build/parser.tab.cpp"
    break;

  case 167: /* statement: iteration_stmt  */
#line 789 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3798 "build/parser.tab.cpp"
    break;

  case 168: /* statement: jump_stmt  */
#line 790 "../phase2-parser/src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3804 "build/parser.tab.cpp"
    break;

  case 169: /* statement: labeled_stmt  */
#line 791 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3810 "build/parser.tab.cpp"
    break;

  case 170: /* statement: declaration  */
#line 792 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3816 "build/parser.tab.cpp"
    break;

  case 171: /* statement: error ';'  */
#line 793 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3822 "build/parser.tab.cpp"
    break;

  case 172: /* statement: error '}'  */
#line 794 "../phase2-parser/src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3828 "build/parser.tab.cpp"
    break;

  case 173: /* $@11: %empty  */
#line 798 "../phase2-parser/src/parser.y"
          { pushScope(); }
#line 3834 "build/parser.tab.cpp"
    break;

  case 174: /* compound_stmt: '{' $@11 block_item_list_opt '}'  */
#line 798 "../phase2-parser/src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 3845 "build/parser.tab.cpp"
    break;

  case 175: /* block_item_list_opt: %empty  */
#line 807 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 3851 "build/parser.tab.cpp"
    break;

  case 176: /* block_item_list_opt: block_item_list  */
#line 808 "../phase2-parser/src/parser.y"
                      { yyval = yyvsp[0]; }
#line 3857 "build/parser.tab.cpp"
    break;

  case 177: /* block_item_list: statement  */
#line 812 "../phase2-parser/src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3863 "build/parser.tab.cpp"
    break;

  case 178: /* block_item_list: block_item_list statement  */
#line 813 "../phase2-parser/src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3869 "build/parser.tab.cpp"
    break;

  case 179: /* expr_stmt: ';'  */
#line 817 "../phase2-parser/src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 3875 "build/parser.tab.cpp"
    break;

  case 180: /* expr_stmt: expr ';'  */
#line 818 "../phase2-parser/src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 3881 "build/parser.tab.cpp"
    break;

  case 181: /* selection_stmt: IF '(' expr ')' statement  */
#line 822 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3889 "build/parser.tab.cpp"
    break;

  case 182: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 825 "../phase2-parser/src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 3897 "build/parser.tab.cpp"
    break;

  case 183: /* $@12: %empty  */
#line 828 "../phase2-parser/src/parser.y"
                          { hintScope("switch"); }
#line 3903 "build/parser.tab.cpp"
    break;

  case 184: /* selection_stmt: SWITCH '(' expr ')' $@12 compound_stmt  */
#line 828 "../phase2-parser/src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 3911 "build/parser.tab.cpp"
    break;

  case 185: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 834 "../phase2-parser/src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 3919 "build/parser.tab.cpp"
    break;

  case 186: /* labeled_stmt: DEFAULT ':' statement  */
#line 837 "../phase2-parser/src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3927 "build/parser.tab.cpp"
    break;

  case 187: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 840 "../phase2-parser/src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3937 "build/parser.tab.cpp"
    break;

  case 188: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 848 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3945 "build/parser.tab.cpp"
    break;

  case 189: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 851 "../phase2-parser/src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 3953 "build/parser.tab.cpp"
    break;

  case 190: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 858 "../phase2-parser/src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 3962 "build/parser.tab.cpp"
    break;

  case 191: /* iteration_stmt: DO statement error ';'  */
#line 862 "../phase2-parser/src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 3971 "build/parser.tab.cpp"
    break;

  case 192: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 866 "../phase2-parser/src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3979 "build/parser.tab.cpp"
    break;

  case 193: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 869 "../phase2-parser/src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 3988 "build/parser.tab.cpp"
    break;

  case 194: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 873 "../phase2-parser/src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 3997 "build/parser.tab.cpp"
    break;

  case 195: /* for_open: FOR '('  */
#line 882 "../phase2-parser/src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4003 "build/parser.tab.cpp"
    break;

  case 196: /* for_incr_opt: %empty  */
#line 886 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4009 "build/parser.tab.cpp"
    break;

  case 197: /* for_incr_opt: expr  */
#line 887 "../phase2-parser/src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4015 "build/parser.tab.cpp"
    break;

  case 198: /* jump_stmt: BREAK ';'  */
#line 891 "../phase2-parser/src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4021 "build/parser.tab.cpp"
    break;

  case 199: /* jump_stmt: CONTINUE ';'  */
#line 892 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4027 "build/parser.tab.cpp"
    break;

  case 200: /* jump_stmt: RETURN ';'  */
#line 893 "../phase2-parser/src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4033 "build/parser.tab.cpp"
    break;

  case 201: /* jump_stmt: RETURN expr ';'  */
#line 894 "../phase2-parser/src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4039 "build/parser.tab.cpp"
    break;

  case 202: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 895 "../phase2-parser/src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4051 "build/parser.tab.cpp"
    break;

  case 203: /* expr: assignment_expr  */
#line 905 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4057 "build/parser.tab.cpp"
    break;

  case 204: /* expr: expr ',' assignment_expr  */
#line 906 "../phase2-parser/src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4063 "build/parser.tab.cpp"
    break;

  case 205: /* assignment_expr: binary_expr  */
#line 910 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4069 "build/parser.tab.cpp"
    break;

  case 206: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 911 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4077 "build/parser.tab.cpp"
    break;

  case 207: /* assign_op: '='  */
#line 917 "../phase2-parser/src/parser.y"
                   { yyval.str = "="; }
#line 4083 "build/parser.tab.cpp"
    break;

  case 208: /* assign_op: PLUS_ASSIGN  */
#line 918 "../phase2-parser/src/parser.y"
                   { yyval.str = "+="; }
#line 4089 "build/parser.tab.cpp"
    break;

  case 209: /* assign_op: MINUS_ASSIGN  */
#line 919 "../phase2-parser/src/parser.y"
                   { yyval.str = "-="; }
#line 4095 "build/parser.tab.cpp"
    break;

  case 210: /* assign_op: MUL_ASSIGN  */
#line 920 "../phase2-parser/src/parser.y"
                   { yyval.str = "*="; }
#line 4101 "build/parser.tab.cpp"
    break;

  case 211: /* assign_op: DIV_ASSIGN  */
#line 921 "../phase2-parser/src/parser.y"
                   { yyval.str = "/="; }
#line 4107 "build/parser.tab.cpp"
    break;

  case 212: /* assign_op: MOD_ASSIGN  */
#line 922 "../phase2-parser/src/parser.y"
                   { yyval.str = "%="; }
#line 4113 "build/parser.tab.cpp"
    break;

  case 213: /* assign_op: AND_ASSIGN  */
#line 923 "../phase2-parser/src/parser.y"
                   { yyval.str = "&="; }
#line 4119 "build/parser.tab.cpp"
    break;

  case 214: /* assign_op: OR_ASSIGN  */
#line 924 "../phase2-parser/src/parser.y"
                   { yyval.str = "|="; }
#line 4125 "build/parser.tab.cpp"
    break;

  case 215: /* assign_op: XOR_ASSIGN  */
#line 925 "../phase2-parser/src/parser.y"
                   { yyval.str = "^="; }
#line 4131 "build/parser.tab.cpp"
    break;

  case 216: /* assign_op: SHL_ASSIGN  */
#line 926 "../phase2-parser/src/parser.y"
                   { yyval.str = "<<="; }
#line 4137 "build/parser.tab.cpp"
    break;

  case 217: /* assign_op: SHR_ASSIGN  */
#line 927 "../phase2-parser/src/parser.y"
                   { yyval.str = ">>="; }
#line 4143 "build/parser.tab.cpp"
    break;

  case 218: /* constant_expr: binary_expr  */
#line 931 "../phase2-parser/src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4149 "build/parser.tab.cpp"
    break;

  case 219: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 935 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4155 "build/parser.tab.cpp"
    break;

  case 220: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 936 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4161 "build/parser.tab.cpp"
    break;

  case 221: /* binary_expr: binary_expr '|' binary_expr  */
#line 937 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4167 "build/parser.tab.cpp"
    break;

  case 222: /* binary_expr: binary_expr '^' binary_expr  */
#line 938 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4173 "build/parser.tab.cpp"
    break;

  case 223: /* binary_expr: binary_expr '&' binary_expr  */
#line 939 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4179 "build/parser.tab.cpp"
    break;

  case 224: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 940 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4185 "build/parser.tab.cpp"
    break;

  case 225: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 941 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4191 "build/parser.tab.cpp"
    break;

  case 226: /* binary_expr: binary_expr '<' binary_expr  */
#line 942 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4197 "build/parser.tab.cpp"
    break;

  case 227: /* binary_expr: binary_expr '>' binary_expr  */
#line 943 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4203 "build/parser.tab.cpp"
    break;

  case 228: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 944 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4209 "build/parser.tab.cpp"
    break;

  case 229: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 945 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4215 "build/parser.tab.cpp"
    break;

  case 230: /* binary_expr: binary_expr SHL binary_expr  */
#line 946 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4221 "build/parser.tab.cpp"
    break;

  case 231: /* binary_expr: binary_expr SHR binary_expr  */
#line 947 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4227 "build/parser.tab.cpp"
    break;

  case 232: /* binary_expr: binary_expr '+' binary_expr  */
#line 948 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4233 "build/parser.tab.cpp"
    break;

  case 233: /* binary_expr: binary_expr '-' binary_expr  */
#line 949 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4239 "build/parser.tab.cpp"
    break;

  case 234: /* binary_expr: binary_expr '*' binary_expr  */
#line 950 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4245 "build/parser.tab.cpp"
    break;

  case 235: /* binary_expr: binary_expr '/' binary_expr  */
#line 951 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4251 "build/parser.tab.cpp"
    break;

  case 236: /* binary_expr: binary_expr '%' binary_expr  */
#line 952 "../phase2-parser/src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4257 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 953 "../phase2-parser/src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4265 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: unary_expr  */
#line 956 "../phase2-parser/src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4271 "build/parser.tab.cpp"
    break;

  case 239: /* unary_expr: postfix_expr  */
#line 960 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4277 "build/parser.tab.cpp"
    break;

  case 240: /* unary_expr: INC unary_expr  */
#line 961 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4283 "build/parser.tab.cpp"
    break;

  case 241: /* unary_expr: DEC unary_expr  */
#line 962 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4289 "build/parser.tab.cpp"
    break;

  case 242: /* unary_expr: '&' unary_expr  */
#line 963 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4295 "build/parser.tab.cpp"
    break;

  case 243: /* unary_expr: '*' unary_expr  */
#line 964 "../phase2-parser/src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4301 "build/parser.tab.cpp"
    break;

  case 244: /* unary_expr: '+' unary_expr  */
#line 965 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4307 "build/parser.tab.cpp"
    break;

  case 245: /* unary_expr: '-' unary_expr  */
#line 966 "../phase2-parser/src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4313 "build/parser.tab.cpp"
    break;

  case 246: /* unary_expr: '!' unary_expr  */
#line 967 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4319 "build/parser.tab.cpp"
    break;

  case 247: /* unary_expr: '~' unary_expr  */
#line 968 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4325 "build/parser.tab.cpp"
    break;

  case 248: /* unary_expr: '(' type_name ')' unary_expr  */
#line 969 "../phase2-parser/src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4334 "build/parser.tab.cpp"
    break;

  case 249: /* unary_expr: SIZEOF unary_expr  */
#line 973 "../phase2-parser/src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4340 "build/parser.tab.cpp"
    break;

  case 250: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 974 "../phase2-parser/src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4349 "build/parser.tab.cpp"
    break;

  case 251: /* type_name: type_name_specifiers  */
#line 981 "../phase2-parser/src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4358 "build/parser.tab.cpp"
    break;

  case 252: /* type_name: type_name_specifiers abstract_declarator  */
#line 985 "../phase2-parser/src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4367 "build/parser.tab.cpp"
    break;

  case 253: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 992 "../phase2-parser/src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4379 "build/parser.tab.cpp"
    break;

  case 254: /* type_name_specifiers: type_name_specifier  */
#line 999 "../phase2-parser/src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4385 "build/parser.tab.cpp"
    break;

  case 255: /* type_name_specifier: INT  */
#line 1003 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4391 "build/parser.tab.cpp"
    break;

  case 256: /* type_name_specifier: CHAR  */
#line 1004 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4397 "build/parser.tab.cpp"
    break;

  case 257: /* type_name_specifier: FLOAT  */
#line 1005 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4403 "build/parser.tab.cpp"
    break;

  case 258: /* type_name_specifier: DOUBLE  */
#line 1006 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4409 "build/parser.tab.cpp"
    break;

  case 259: /* type_name_specifier: VOID  */
#line 1007 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4415 "build/parser.tab.cpp"
    break;

  case 260: /* type_name_specifier: BOOL  */
#line 1008 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4421 "build/parser.tab.cpp"
    break;

  case 261: /* type_name_specifier: SHORT  */
#line 1009 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4427 "build/parser.tab.cpp"
    break;

  case 262: /* type_name_specifier: LONG  */
#line 1010 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4433 "build/parser.tab.cpp"
    break;

  case 263: /* type_name_specifier: SIGNED  */
#line 1011 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4439 "build/parser.tab.cpp"
    break;

  case 264: /* type_name_specifier: UNSIGNED  */
#line 1012 "../phase2-parser/src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4445 "build/parser.tab.cpp"
    break;

  case 265: /* type_name_specifier: VA_LIST  */
#line 1013 "../phase2-parser/src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4451 "build/parser.tab.cpp"
    break;

  case 266: /* type_name_specifier: CONST  */
#line 1014 "../phase2-parser/src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4457 "build/parser.tab.cpp"
    break;

  case 267: /* type_name_specifier: TYPE_NAME  */
#line 1015 "../phase2-parser/src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4471 "build/parser.tab.cpp"
    break;

  case 268: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1024 "../phase2-parser/src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4482 "build/parser.tab.cpp"
    break;

  case 269: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1030 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4493 "build/parser.tab.cpp"
    break;

  case 270: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1036 "../phase2-parser/src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4504 "build/parser.tab.cpp"
    break;

  case 271: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1042 "../phase2-parser/src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4515 "build/parser.tab.cpp"
    break;

  case 272: /* postfix_expr: primary_expr  */
#line 1051 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4521 "build/parser.tab.cpp"
    break;

  case 273: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1052 "../phase2-parser/src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4527 "build/parser.tab.cpp"
    break;

  case 274: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1053 "../phase2-parser/src/parser.y"
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
#line 4567 "build/parser.tab.cpp"
    break;

  case 275: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1088 "../phase2-parser/src/parser.y"
                                  {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4576 "build/parser.tab.cpp"
    break;

  case 276: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1092 "../phase2-parser/src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4589 "build/parser.tab.cpp"
    break;

  case 277: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1100 "../phase2-parser/src/parser.y"
                                                        {
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4600 "build/parser.tab.cpp"
    break;

  case 278: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1106 "../phase2-parser/src/parser.y"
                                    {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4609 "build/parser.tab.cpp"
    break;

  case 279: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1110 "../phase2-parser/src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4615 "build/parser.tab.cpp"
    break;

  case 280: /* postfix_expr: postfix_expr INC  */
#line 1111 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4621 "build/parser.tab.cpp"
    break;

  case 281: /* postfix_expr: postfix_expr DEC  */
#line 1112 "../phase2-parser/src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4627 "build/parser.tab.cpp"
    break;

  case 282: /* postfix_expr: builtin_call  */
#line 1113 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4633 "build/parser.tab.cpp"
    break;

  case 283: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1117 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4639 "build/parser.tab.cpp"
    break;

  case 284: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1118 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4645 "build/parser.tab.cpp"
    break;

  case 285: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1119 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4651 "build/parser.tab.cpp"
    break;

  case 286: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1120 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4657 "build/parser.tab.cpp"
    break;

  case 287: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1121 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4663 "build/parser.tab.cpp"
    break;

  case 288: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1122 "../phase2-parser/src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4669 "build/parser.tab.cpp"
    break;

  case 289: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1123 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4675 "build/parser.tab.cpp"
    break;

  case 290: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1124 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4681 "build/parser.tab.cpp"
    break;

  case 291: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1125 "../phase2-parser/src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4687 "build/parser.tab.cpp"
    break;

  case 292: /* constructor_args_opt: %empty  */
#line 1129 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4693 "build/parser.tab.cpp"
    break;

  case 293: /* constructor_args_opt: constructor_args  */
#line 1130 "../phase2-parser/src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4699 "build/parser.tab.cpp"
    break;

  case 294: /* argument_list_opt: %empty  */
#line 1134 "../phase2-parser/src/parser.y"
                  { yyval = ParserValue(); }
#line 4705 "build/parser.tab.cpp"
    break;

  case 295: /* argument_list_opt: argument_list  */
#line 1135 "../phase2-parser/src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4711 "build/parser.tab.cpp"
    break;

  case 296: /* argument_list: argument  */
#line 1139 "../phase2-parser/src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4717 "build/parser.tab.cpp"
    break;

  case 297: /* argument_list: argument_list ',' argument  */
#line 1140 "../phase2-parser/src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4723 "build/parser.tab.cpp"
    break;

  case 298: /* argument: assignment_expr  */
#line 1144 "../phase2-parser/src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4729 "build/parser.tab.cpp"
    break;

  case 299: /* argument: type_name  */
#line 1145 "../phase2-parser/src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4738 "build/parser.tab.cpp"
    break;

  case 300: /* primary_expr: IDENTIFIER  */
#line 1152 "../phase2-parser/src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 4752 "build/parser.tab.cpp"
    break;

  case 301: /* primary_expr: INT_LITERAL  */
#line 1161 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4758 "build/parser.tab.cpp"
    break;

  case 302: /* primary_expr: FLOAT_LITERAL  */
#line 1162 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4764 "build/parser.tab.cpp"
    break;

  case 303: /* primary_expr: CHAR_LITERAL  */
#line 1163 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4770 "build/parser.tab.cpp"
    break;

  case 304: /* primary_expr: string_literal  */
#line 1164 "../phase2-parser/src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4776 "build/parser.tab.cpp"
    break;

  case 305: /* primary_expr: BOOL_LITERAL  */
#line 1165 "../phase2-parser/src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4782 "build/parser.tab.cpp"
    break;

  case 306: /* primary_expr: THIS  */
#line 1166 "../phase2-parser/src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 4788 "build/parser.tab.cpp"
    break;

  case 307: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1167 "../phase2-parser/src/parser.y"
                                             {
          /* `Dog(4)`: a temporary object (for a scalar type, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4797 "build/parser.tab.cpp"
    break;

  case 308: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1171 "../phase2-parser/src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4807 "build/parser.tab.cpp"
    break;

  case 309: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1178 "../phase2-parser/src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4813 "build/parser.tab.cpp"
    break;

  case 310: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1179 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4819 "build/parser.tab.cpp"
    break;

  case 311: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1180 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4825 "build/parser.tab.cpp"
    break;

  case 312: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1181 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4831 "build/parser.tab.cpp"
    break;

  case 313: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1182 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4837 "build/parser.tab.cpp"
    break;

  case 314: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1183 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4843 "build/parser.tab.cpp"
    break;

  case 315: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1184 "../phase2-parser/src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4849 "build/parser.tab.cpp"
    break;

  case 316: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1185 "../phase2-parser/src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4855 "build/parser.tab.cpp"
    break;

  case 317: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1186 "../phase2-parser/src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4861 "build/parser.tab.cpp"
    break;

  case 318: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1187 "../phase2-parser/src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4867 "build/parser.tab.cpp"
    break;

  case 319: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1188 "../phase2-parser/src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 4879 "build/parser.tab.cpp"
    break;

  case 320: /* primary_expr: '(' expr ')'  */
#line 1195 "../phase2-parser/src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 4885 "build/parser.tab.cpp"
    break;

  case 321: /* string_literal: STRING_LITERAL  */
#line 1200 "../phase2-parser/src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4891 "build/parser.tab.cpp"
    break;

  case 322: /* string_literal: string_literal STRING_LITERAL  */
#line 1201 "../phase2-parser/src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 4901 "build/parser.tab.cpp"
    break;


#line 4905 "build/parser.tab.cpp"

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

#line 1208 "../phase2-parser/src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
