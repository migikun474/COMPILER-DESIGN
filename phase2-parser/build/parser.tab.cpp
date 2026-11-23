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
#define YYLAST   2189

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  117
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  86
/* YYNRULES -- Number of rules.  */
#define YYNRULES  344
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  611

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
       0,   140,   140,   144,   152,   153,   154,   155,   156,   160,
     191,   204,   208,   209,   210,   211,   212,   213,   217,   218,
     219,   220,   221,   222,   223,   224,   225,   226,   227,   228,
     242,   249,   250,   254,   258,   254,   274,   274,   288,   294,
     300,   304,   300,   313,   313,   327,   333,   339,   345,   351,
     351,   362,   362,   372,   376,   372,   388,   388,   402,   408,
     417,   418,   425,   426,   430,   435,   443,   444,   448,   449,
     453,   454,   461,   467,   473,   479,   490,   495,   507,   508,
     509,   510,   519,   519,   537,   541,   549,   553,   549,   573,
     574,   575,   579,   580,   584,   585,   589,   590,   594,   595,
     596,   601,   609,   610,   614,   615,   618,   624,   625,   626,
     627,   628,   632,   638,   644,   645,   651,   655,   664,   665,
     666,   667,   671,   675,   682,   694,   703,   707,   714,   721,
     740,   747,   748,   753,   757,   757,   757,   757,   758,   758,
     758,   758,   759,   759,   759,   759,   760,   760,   760,   760,
     761,   761,   761,   761,   762,   762,   762,   763,   763,   763,
     764,   764,   764,   765,   765,   765,   766,   766,   766,   773,
     777,   778,   782,   783,   787,   791,   795,   799,   804,   809,
     817,   817,   882,   883,   884,   885,   886,   887,   888,   889,
     890,   894,   894,   903,   904,   908,   909,   913,   914,   918,
     921,   924,   924,   930,   933,   936,   944,   947,   954,   958,
     962,   965,   969,   978,   982,   983,   987,   988,   989,   990,
     991,  1001,  1002,  1006,  1007,  1013,  1014,  1015,  1016,  1017,
    1018,  1019,  1020,  1021,  1022,  1023,  1027,  1031,  1032,  1033,
    1034,  1035,  1036,  1037,  1038,  1039,  1040,  1041,  1042,  1043,
    1044,  1045,  1046,  1047,  1048,  1049,  1052,  1056,  1057,  1058,
    1059,  1060,  1061,  1062,  1063,  1064,  1065,  1069,  1070,  1077,
    1081,  1088,  1095,  1099,  1100,  1101,  1102,  1103,  1104,  1105,
    1106,  1107,  1108,  1109,  1110,  1111,  1120,  1126,  1132,  1138,
    1144,  1150,  1156,  1162,  1171,  1172,  1173,  1208,  1212,  1220,
    1226,  1230,  1231,  1232,  1233,  1237,  1238,  1239,  1240,  1241,
    1242,  1243,  1244,  1245,  1249,  1250,  1254,  1255,  1259,  1260,
    1264,  1265,  1272,  1281,  1282,  1283,  1284,  1285,  1286,  1287,
    1291,  1298,  1299,  1300,  1301,  1302,  1303,  1304,  1305,  1306,
    1307,  1308,  1315,  1320,  1321
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

#define YYPACT_NINF (-429)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-195)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -429,  1933,  -429,   -30,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,  -429,   -34,   -28,    -6,    -4,  -429,  -429,  -429,
    -429,  -429,  -429,  -429,   -39,  -429,  -429,  1818,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,   -69,   -65,  -429,  -429,   -68,
     -47,  -429,  -429,   -69,   -65,  -429,  -429,   -69,   -65,  -429,
    -429,    -3,  2008,     0,    46,  -429,  -429,   157,  -429,     2,
      22,  -429,   212,   -67,   -20,  -429,  1987,    45,  1987,    60,
    1987,    71,   152,   102,   126,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,   125,   138,
    -429,    16,    56,    46,   144,  -429,   157,  -429,  -429,  -429,
     -20,  1163,   170,   391,   465,  -429,  -429,  -429,   179,  -429,
    -429,   184,  1987,  -429,   -71,  -429,   203,  -429,  -429,   190,
     221,   196,   200,  -429,   218,   205,  -429,   152,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,  -429,  -429,   228,   211,   226,
     237,   272,   275,   276,   278,   279,   280,  -429,   281,   282,
     283,   285,   286,   287,   290,  1620,   291,   292,   293,   295,
    -429,   -26,  -429,  -429,  -429,  -429,  -429,  1687,  1687,  1687,
    1687,  1687,  1687,  1687,  1687,  1553,  1015,  -429,  -429,  2049,
     593,   224,  -429,  -429,   264,   715,  2016,    40,  -429,  -429,
     257,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  1987,  -429,
    -429,  -429,   288,  -429,   194,  -429,  -429,  1987,  1687,   152,
     296,   205,  2016,  1687,  1687,  1687,  1687,  1687,  1687,  1687,
    1687,  1687,  1553,  1553,  1553,  1553,  1553,  1553,  1687,  1553,
    -429,  1553,  1553,  1553,  1687,   348,  1687,  -429,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,   211,   226,   237,   272,   275,
     276,   278,   279,   280,   202,   206,   210,   214,  -429,   290,
    -429,   -26,    75,  -429,   289,   188,  -429,   350,  1687,  -429,
    -429,    73,  -429,  1687,  1687,  1687,  1687,  1687,  1687,  1687,
    1687,  1687,  1687,  1687,  1687,  1687,  1687,  1687,  1687,  1687,
    1687,  1687,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,  -429,  1687,   217,   352,  -429,  -429,   225,  1553,
    1687,  -429,   189,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,   303,   305,   306,   941,   307,   308,  1687,   328,
     309,   310,   363,  1347,  -429,   331,   358,  -429,  -429,  1818,
    -429,  -429,   311,   828,  -429,  -429,  -429,  -429,  1274,  -429,
      35,  1484,   313,   315,  -429,  1687,  -429,  -429,  2016,   715,
     312,   221,  -429,  -429,  1987,   318,  -429,  2049,  -429,  -429,
    -429,   325,   332,   329,   338,   339,   340,   343,   344,   347,
     349,   351,   362,  -429,  -429,   364,   366,  -429,   368,   373,
     374,   375,   376,   377,   378,   381,   383,   384,   385,  -429,
     386,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  1687,
    -429,  1687,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,   164,  -429,   533,   134,  -429,   356,  -429,   379,
     365,  -429,  1089,   -64,   -64,   274,   274,   253,   253,   267,
    2059,   -51,  2091,   617,  1450,   274,   274,    44,    44,  -429,
    -429,  -429,  -429,  -429,   414,  -429,  -429,   438,   388,    92,
    -429,  -429,  1687,  -429,  1687,    17,  1687,  1687,   425,   941,
    -429,  -429,   406,  -429,    36,   941,  -429,  -429,  1420,  1420,
    -429,   191,  -429,  -429,  -429,  1872,  -429,   404,   415,  -429,
    -429,   416,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,  1553,  -429,  -429,  -429,  -429,
    -429,  -429,  1754,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
     417,  -429,   413,   356,   601,  1163,   447,  -429,  -429,  1687,
     479,   480,  -429,  -429,   192,   213,   434,   440,   240,   252,
     941,  -429,  -429,  -429,  -429,  1687,  1687,  -429,  -429,  -429,
    -429,  -429,   435,  -429,  -429,  -429,  -429,   431,  -429,  1163,
    2049,  -429,  -429,   941,   941,  -429,  1687,   941,  -429,  -429,
     436,   439,   442,  -429,  -429,  -429,   521,  -429,   261,  -429,
     435,   941,   941,   941,    28,  -429,  -429,  -429,  -429,  -429,
    -429
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    18,    19,    20,    21,    22,    24,
      25,    26,    27,     0,     0,     0,     0,    12,    14,    13,
      15,    16,    23,    28,    29,     3,     5,    92,    11,    17,
      30,     6,     4,     7,     8,    38,    39,    36,    33,    58,
      59,    56,    53,    45,    46,    43,    40,    47,    48,    51,
      49,     0,     0,   122,    29,   108,   107,     0,    10,     0,
      93,    94,     0,    96,   113,   126,    60,     0,    60,    68,
      60,     0,     0,     0,     0,   155,   156,   153,   154,   149,
     150,   147,   148,   151,   152,   157,   158,   159,   160,   161,
     162,   163,   164,   165,   166,   144,   141,   139,   140,   145,
     146,   134,   135,   136,   137,   138,   143,   142,     0,     0,
     133,     0,     0,     0,     0,     9,     0,   111,   110,   109,
     112,     0,     0,   169,     0,    89,    90,    91,     0,    29,
      78,     0,    61,    76,     0,    81,     0,    79,    34,     0,
       0,     0,     0,    41,    64,    66,    62,     0,    86,   168,
     167,   123,   127,   124,   128,   125,    95,    96,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   328,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     322,     0,   323,   324,   325,   343,   327,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    97,    98,   223,
     256,   257,   304,   294,   326,     0,   172,     0,   170,   131,
       0,    82,    37,    77,    85,   191,    84,    80,    60,    57,
      74,    75,    69,    70,     0,    54,    44,    60,     0,    67,
       0,    66,   172,   314,   314,   314,   314,   314,   314,   314,
     314,   314,   316,   316,   316,   316,   316,   316,   314,     0,
     267,   316,   316,   316,   314,     0,   314,   258,   259,   260,
     262,   263,   261,   264,   265,   273,   274,   275,   276,   277,
     279,   280,   281,   282,     0,     0,     0,     0,   284,   278,
     283,   285,     0,   221,     0,   269,   272,     0,     0,    99,
     104,     0,   102,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   226,   227,   228,   229,   230,   231,   232,   233,
     234,   235,   225,     0,     0,     0,   302,   303,     0,   316,
       0,   344,     0,    18,    19,    20,    21,    22,    24,    25,
      26,    27,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    23,   322,    29,   197,   188,    92,
     195,   182,     0,     0,   183,   184,   187,   185,     0,   186,
       0,   179,     0,   173,   174,     0,   130,   132,   172,     0,
       0,     0,    72,    73,    60,     0,    65,   236,   256,    63,
      52,     0,     0,   315,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   320,   321,     0,   317,   318,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   341,
       0,   286,   287,   292,   293,   288,   289,   290,   291,     0,
     342,     0,   273,   274,   275,   276,   277,   279,   280,   281,
     282,   278,     0,   285,     0,   114,   270,   116,   271,     0,
       0,   100,     0,   248,   249,   246,   247,   242,   243,   238,
     237,     0,   239,   240,   241,   244,   245,   250,   251,   252,
     253,   254,   224,   300,     0,   301,   297,     0,     0,     0,
     189,   190,     0,   213,     0,     0,     0,     0,     0,     0,
     216,   217,     0,   218,     0,     0,   181,   196,     0,     0,
     198,   114,   177,   178,   129,     0,   171,     0,     0,    35,
      71,     0,    42,    50,    87,   331,   332,   333,   334,   335,
     337,   338,   339,   340,   305,     0,   306,   307,   308,   309,
     310,   336,   268,   311,   312,   313,   330,   329,   222,   266,
       0,   118,     0,   115,     0,     0,     0,   101,   103,     0,
       0,     0,   296,   295,     0,     0,     0,     0,     0,     0,
       0,   204,   220,   219,   205,   214,   214,   176,   175,    83,
     192,    55,     0,   319,   117,   119,   120,     0,   105,     0,
     255,   299,   298,     0,     0,   209,     0,     0,   201,   203,
       0,   215,     0,    88,   121,   106,   199,   206,     0,   210,
       0,     0,     0,     0,     0,   202,   212,   211,   200,   208,
     207
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -429,  -429,  -429,     6,    -1,   -19,  -429,   137,  -429,  -429,
    -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,  -429,
     -58,   403,   326,   323,  -429,  -429,   177,  -429,   430,  -429,
    -429,  -429,  -429,  -429,  -429,  -129,  -429,  -429,   448,  -118,
    -429,   111,  -259,   -18,  -358,  -428,   -56,   268,  -429,  -429,
     443,  -197,  -429,    62,   564,  -429,  -309,  -133,  -429,   193,
    -429,  -354,  -429,  -429,  -429,  -429,  -429,     4,  -429,  -171,
    -119,  -429,  -273,  -205,  -132,  -179,  -429,   300,  -429,  -429,
     548,   -24,  -429,    70,  -429,  -429
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    25,   358,   359,    28,    29,    38,    30,    67,
     218,    66,    71,   227,    70,    73,    72,    69,   384,    68,
     131,   145,   146,   230,   141,   222,   223,   132,   133,   134,
     378,   135,    31,   232,   572,   136,    59,    60,    61,   290,
     291,   292,    62,   157,   446,   447,    64,    65,   110,   206,
     393,   372,   373,   374,   137,   122,   360,   361,   379,   362,
     363,   364,   365,   600,   366,   367,   368,   590,   369,   370,
     283,   323,   386,   199,   200,   404,   285,   286,   201,   202,
     394,   405,   406,   407,   203,   204
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      27,   216,   198,   197,   208,   210,   120,    26,    58,    63,
     139,   224,   142,   503,   499,   450,   284,   543,   556,   121,
     -31,    35,    36,   387,   282,    51,   445,    39,    40,   609,
     307,   308,   309,   310,   311,   392,   485,   549,   255,   114,
     214,   -32,   215,   250,   -31,   -31,  -180,   557,   -32,    43,
      44,    47,    48,    74,   497,   257,   258,   259,   260,   261,
     262,   263,   264,   429,   111,    27,   -32,    27,    52,    27,
     414,   151,   130,   543,   130,   488,   130,   198,   282,    37,
     256,    33,    34,   387,   540,    41,   123,   124,   453,   454,
     455,   456,   457,   458,   459,   460,   388,   462,   463,   464,
     465,   466,   467,   468,   469,   470,   471,    45,    52,    49,
     112,   153,   501,   115,   208,   208,   208,   208,   208,   208,
     208,   208,   208,   403,   403,   403,   403,   403,   403,   208,
     461,    27,   403,   403,   403,   208,   116,   208,   130,   610,
     309,   310,   311,   387,   565,   566,   500,   563,   140,   429,
     429,    42,    46,    50,   375,   376,   388,   117,   138,   479,
     380,   388,   388,   388,   388,   388,   388,   388,   388,   385,
     388,   388,   388,   388,   388,   388,   388,   388,   388,   388,
     561,   507,   494,   445,   143,   451,   564,   452,   442,   429,
     430,   432,   433,   434,   435,   436,   437,   438,   439,   440,
     274,   275,   276,   277,   472,   371,   429,   144,   553,    52,
     403,   278,    53,   113,   117,   147,   388,    27,   442,   408,
     409,   410,   411,   412,   130,   118,    27,   415,   416,   417,
     119,   371,   148,   130,   441,   117,   280,   125,   126,   127,
     149,   444,   442,    52,   443,   442,    53,   113,    55,   382,
     383,   589,   224,    56,   150,    55,   506,   421,   422,   155,
      56,   423,   424,    57,    52,   425,   426,    53,   113,   427,
     428,   444,   473,   474,   596,   597,   220,   221,   599,    55,
     476,   477,   118,   205,    56,   211,   324,   119,   325,   326,
     327,   217,   606,   607,   608,   444,   212,    57,   444,   539,
     480,   481,   219,   118,   228,   478,   429,   583,   119,   225,
     538,   554,   226,   555,   121,   558,   559,   233,    57,   229,
     293,   294,   295,   296,   331,   542,   511,   429,   584,   328,
     329,   330,   234,   198,   293,   294,   295,   296,   297,   298,
      58,   293,   294,   235,   580,   305,   306,   307,   308,   309,
     310,   311,    58,   502,   429,   587,   302,   303,   304,   305,
     306,   307,   308,   309,   310,   311,   429,   588,   307,   308,
     309,   310,   311,   377,   498,   429,   604,   371,   236,   152,
     154,   237,   238,    27,   239,   240,   241,   242,   243,   244,
     130,   245,   246,   247,   591,   591,   248,   251,   252,   253,
     539,   254,   381,   419,   431,   449,   403,   475,   390,   482,
     167,   483,   484,   486,   487,   598,   489,   388,   492,   495,
     490,   491,   255,   496,   509,   577,   198,   578,   504,   505,
     512,   168,   169,   170,   171,   172,   173,   513,   175,   593,
     176,   177,   178,   375,   179,   120,   180,   514,   182,   183,
     184,   185,   186,   515,   516,   517,   187,   188,   518,   519,
     198,   595,   520,   544,   521,   545,   522,   605,   158,   159,
     160,   161,   162,   163,   164,   165,   166,   523,   550,   524,
     525,   546,   189,   526,   167,   190,   191,   192,   527,   528,
     529,   530,   531,   532,   193,   194,   533,   195,   534,   535,
     536,   537,   551,   552,   371,   168,   169,   170,   171,   172,
     173,   174,   175,   560,   176,   177,   178,   562,   179,   569,
     180,   181,   182,   183,   184,   185,   186,   570,   571,   575,
     187,   188,   574,   579,   581,   582,   158,   159,   160,   161,
     162,   163,   164,   165,   166,   585,   586,   594,   215,   603,
     231,   601,   167,   429,   391,   389,   189,   602,   510,   190,
     191,   192,   213,   548,   156,    32,   207,   568,   193,   194,
     592,   195,   508,   168,   169,   170,   171,   172,   173,   174,
     175,   209,   176,   177,   178,   448,   179,     0,   180,   181,
     182,   183,   184,   185,   186,   573,     0,     0,   187,   188,
       0,     0,     0,     0,   158,   159,   160,   161,   162,   163,
     164,   165,   166,     0,     0,     0,     0,     0,     0,     0,
     167,     0,     0,     0,   189,     0,     0,   190,   191,   192,
       0,     0,     0,     0,     0,     0,   193,   194,     0,   195,
       0,   168,   169,   170,   171,   172,   173,   174,   175,   541,
     176,   177,   178,     0,   179,     0,   180,   181,   182,   183,
     184,   185,   186,     0,     0,     0,   187,   188,   312,   313,
     314,   315,   316,   317,   318,   319,   320,   321,     0,   322,
       0,     0,     0,     0,   293,   294,   295,   296,   297,   298,
       0,     0,   189,     0,     0,   190,   191,   192,     0,     0,
       0,     0,     0,     0,   193,   194,     0,   195,   304,   305,
     306,   307,   308,   309,   310,   311,   332,   576,   333,   334,
     335,   336,   337,   338,   339,   340,   341,    13,    14,    15,
      16,     0,     0,     0,   167,    17,    18,    19,    20,    21,
       0,     0,   342,     0,   343,   344,   345,   346,   347,   348,
     349,   350,   351,   352,   353,   168,   169,   170,   171,   172,
     173,   354,   175,    23,   176,   177,   178,     0,   179,     0,
     355,   356,   182,   183,   184,   185,   186,     0,     0,     0,
     187,   188,   395,   396,   397,   398,   399,   400,   401,   402,
       0,     0,     0,     0,     0,     0,   413,     0,     0,     0,
       0,     0,   418,     0,   420,     0,   189,     0,     0,   190,
     191,   192,     0,     0,     0,     0,     0,     0,   193,   194,
       0,   195,     0,     0,     0,     0,   357,  -193,   215,   332,
       0,   333,   334,   335,   336,   337,   338,   339,   340,   341,
      13,    14,    15,    16,     0,     0,     0,   167,    17,    18,
      19,    20,    21,     0,     0,   342,     0,   343,   344,   345,
     346,   347,   348,   349,   350,   351,   352,   353,   168,   169,
     170,   171,   172,   173,   354,   175,    23,   176,   177,   178,
       0,   179,     0,   355,   356,   182,   183,   184,   185,   186,
       0,     0,     0,   187,   188,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   189,
       0,     0,   190,   191,   192,     0,     0,     0,     0,     0,
       0,   193,   194,     0,   195,     0,     0,     0,     0,   357,
    -194,   215,   332,     0,   333,   334,   335,   336,   337,   338,
     339,   340,   341,    13,    14,    15,    16,     0,     0,     0,
     167,    17,    18,    19,    20,    21,     0,     0,   342,     0,
     343,   344,   345,   346,   347,   348,   349,   350,   351,   352,
     353,   168,   169,   170,   171,   172,   173,   354,   175,    23,
     176,   177,   178,     0,   179,     0,   355,   356,   182,   183,
     184,   185,   186,     0,     0,     0,   187,   188,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   158,   159,
     160,   161,   162,   163,   164,   165,   166,     0,     0,     0,
       0,     0,   189,     0,   167,   190,   191,   192,     0,     0,
       0,     0,     0,     0,   193,   194,     0,   195,     0,     0,
       0,     0,   357,     0,   215,   168,   169,   170,   171,   172,
     173,   174,   175,     0,   176,   177,   178,     0,   179,     0,
     180,   181,   182,   183,   184,   185,   186,     0,     0,     0,
     187,   188,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   158,   159,   160,   161,   162,   163,   164,   165,
     166,     0,     0,     0,     0,     0,   189,     0,   167,   190,
     191,   192,     0,     0,     0,     0,     0,     0,   193,   194,
     287,   195,   288,     0,     0,     0,     0,   289,   196,   168,
     169,   170,   171,   172,   173,   174,   175,     0,   176,   177,
     178,     0,   179,     0,   180,   181,   182,   183,   184,   185,
     186,     0,     0,     0,   187,   188,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   158,   159,   160,   161,
     162,   163,   164,   165,   166,     0,     0,     0,     0,     0,
     189,     0,   167,   190,   191,   192,     0,     0,     0,     0,
       0,     0,   193,   194,   287,   195,   288,     0,     0,     0,
       0,   547,   196,   168,   169,   170,   171,   172,   173,   174,
     175,     0,   176,   177,   178,     0,   179,     0,   180,   181,
     182,   183,   184,   185,   186,     0,     0,     0,   187,   188,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   189,     0,     0,   190,   191,   192,
       0,     0,     0,     0,     0,     0,   193,   194,     0,   195,
       0,     0,     0,     0,     0,     0,   196,   333,   334,   335,
     336,   337,   338,   339,   340,   341,    13,    14,    15,    16,
       0,     0,     0,   167,    17,    18,    19,    20,    21,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   168,   169,   170,   171,   172,   173,
     354,   175,    23,   176,   177,   178,     0,   179,     0,   180,
     356,   182,   183,   184,   185,   186,     0,     0,     0,   187,
     188,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     158,   159,   160,   161,   162,   163,   164,   165,   166,     0,
       0,     0,     0,     0,     0,   189,   167,     0,   190,   191,
     192,     0,     0,     0,     0,     0,     0,   193,   194,     0,
     195,     0,     0,     0,     0,   357,     0,   168,   169,   170,
     171,   172,   173,   174,   175,     0,   176,   177,   178,     0,
     179,     0,   180,   181,   182,   183,   184,   185,   186,     0,
       0,     0,   187,   188,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   158,   159,   160,   161,   162,   163,   164,
     165,   166,     0,     0,     0,     0,     0,     0,   189,   167,
       0,   190,   191,   192,     0,     0,     0,     0,     0,     0,
     193,   194,     0,   195,     0,     0,     0,     0,   493,     0,
     168,   169,   170,   171,   172,   173,   174,   175,     0,   176,
     177,   178,     0,   179,     0,   180,   181,   182,   183,   184,
     185,   186,     0,     0,     0,   187,   188,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
       0,     0,     0,     0,    17,    18,    19,    20,    21,     0,
       0,   189,     0,     0,   190,   191,   192,   293,   294,   295,
     296,   297,   298,   193,   194,     0,   195,     0,     0,     0,
      22,   357,    23,     0,     0,     0,    52,     0,   442,    53,
      54,     0,   305,   306,   307,   308,   309,   310,   311,     0,
       0,     0,     0,     0,     0,     0,   265,   266,   267,   268,
     269,   270,   271,   272,   273,   274,   275,   276,   277,     0,
       0,     0,   167,     0,     0,    55,   278,     0,     0,     0,
      56,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      57,   444,     0,   168,   169,   170,   171,   172,   173,   279,
     175,   280,   176,   177,   178,     0,   179,     0,   180,   281,
     182,   183,   184,   185,   186,     0,     0,     0,   187,   188,
       0,     0,     0,   158,   159,   160,   161,   162,   163,   164,
     165,   166,     0,     0,     0,     0,     0,     0,     0,   167,
       0,     0,     0,     0,   189,     0,     0,   190,   191,   192,
       0,     0,     0,     0,     0,     0,   193,   194,     0,   195,
     168,   169,   170,   171,   172,   173,   174,   175,     0,   176,
     177,   178,     0,   179,     0,   180,   181,   182,   183,   184,
     185,   186,     0,     0,     0,   187,   188,     0,     0,     0,
     158,   159,   160,   161,   162,   163,   164,   165,   166,     0,
       0,     0,     0,     0,     0,     0,   167,     0,     0,     0,
       0,   189,     0,     0,   190,   191,   192,     0,     0,     0,
       0,     0,     0,   193,   194,     0,   249,   168,   169,   170,
     171,   172,   173,   174,   175,     0,   176,   177,   178,     0,
     179,     0,   180,   181,   182,   183,   184,   185,   186,     0,
       0,     0,   187,   188,     0,     0,     0,   158,   159,   160,
     161,   162,   163,   164,   165,   166,     0,     0,     0,     0,
       0,     0,     0,   167,     0,     0,     0,     0,   189,     0,
       0,   190,   191,   192,     0,     0,     0,     0,     0,     0,
     193,   194,     0,   195,   168,   169,   170,   171,   172,   173,
     174,   175,     0,   176,   177,   178,     0,   179,     0,   180,
     181,   182,   183,   184,   185,   186,     0,     0,     0,   187,
     188,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,     0,     0,     0,     0,    17,    18,
      19,    20,    21,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   193,   194,     0,
     195,     0,     0,     0,    22,     0,    23,     0,     0,     0,
      52,     0,     0,    53,    54,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,     0,     0,
       0,     0,    17,    18,    19,    20,    21,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    55,
       0,     0,     0,     0,    56,     0,     0,     0,    22,     0,
      23,     0,     0,     0,    57,     0,     0,     0,   129,     0,
       0,     0,     0,     2,     3,   567,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,     0,
       0,     0,     0,    17,    18,    19,    20,    21,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    22,
       0,    23,     0,     0,     0,     0,     0,     0,     0,    24,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,   125,   126,   127,     0,    17,    18,    19,
      20,    21,     0,     0,     0,     0,     0,     0,     0,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,     0,    22,     0,    23,    17,    18,    19,    20,
      21,     0,   128,   129,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    22,     0,    23,     0,     0,     0,     0,     0,
       0,     0,   129,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,    87,    88,    89,    90,    91,
      92,    93,    94,     0,    95,     0,     0,    96,    97,    98,
      99,   100,   101,   102,   103,   104,   105,     0,     0,     0,
       0,   106,   107,     0,   108,   109,   293,   294,   295,   296,
     297,   298,   299,   300,     0,     0,   293,   294,   295,   296,
     297,   298,   299,     0,     0,     0,   301,     0,   302,   303,
     304,   305,   306,   307,   308,   309,   310,   311,   302,   303,
     304,   305,   306,   307,   308,   309,   310,   311,   293,   294,
     295,   296,   297,   298,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   303,   304,   305,   306,   307,   308,   309,   310,   311
};

static const yytype_int16 yycheck[] =
{
       1,   134,   121,   121,   123,   124,    62,     1,    27,    27,
      68,   140,    70,   371,   368,   288,   195,   445,     1,    86,
      88,    55,    56,   228,   195,    64,   285,    55,    56,     1,
      94,    95,    96,    97,    98,   232,   345,    88,    64,    57,
     111,    88,   113,   175,   113,   113,   113,    30,   113,    55,
      56,    55,    56,    56,   363,   187,   188,   189,   190,   191,
     192,   193,   194,   114,    64,    66,   113,    68,    52,    70,
     249,    55,    66,   501,    68,   348,    70,   196,   249,   113,
     106,   111,   112,   288,   442,   113,   106,   107,   293,   294,
     295,   296,   297,   298,   299,   300,   228,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   113,    52,   113,
      64,    55,   371,   111,   233,   234,   235,   236,   237,   238,
     239,   240,   241,   242,   243,   244,   245,   246,   247,   248,
     301,   132,   251,   252,   253,   254,   114,   256,   132,   111,
      96,    97,    98,   348,   498,   499,   111,   111,    88,   114,
     114,    14,    15,    16,   114,   115,   288,    23,   113,   330,
     218,   293,   294,   295,   296,   297,   298,   299,   300,   227,
     302,   303,   304,   305,   306,   307,   308,   309,   310,   311,
     489,   378,   353,   442,   113,   112,   495,   114,    54,   114,
     115,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,   323,   206,   114,    55,   116,    52,
     329,    23,    55,    56,    23,   113,   348,   218,    54,   243,
     244,   245,   246,   247,   218,    91,   227,   251,   252,   253,
      96,   232,   106,   227,    46,    23,    48,    16,    17,    18,
     115,   107,    54,    52,    56,    54,    55,    56,    91,    55,
      56,   560,   381,    96,   116,    91,   375,    55,    56,   115,
      96,    55,    56,   106,    52,    55,    56,    55,    56,    55,
      56,   107,    55,    56,   583,   584,    55,    56,   587,    91,
      55,    56,    91,   113,    96,   106,    62,    96,    64,    65,
      66,    88,   601,   602,   603,   107,   112,   106,   107,   431,
     111,   112,   112,    91,    86,   329,   114,   115,    96,   113,
     429,   482,   112,   484,    86,   486,   487,   106,   106,   114,
      67,    68,    69,    70,    60,   444,   384,   114,   115,   105,
     106,   107,   106,   452,    67,    68,    69,    70,    71,    72,
     359,    67,    68,   106,   549,    92,    93,    94,    95,    96,
      97,    98,   371,   371,   114,   115,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    98,   114,   115,    94,    95,
      96,    97,    98,   116,   368,   114,   115,   378,   106,   111,
     112,   106,   106,   384,   106,   106,   106,   106,   106,   106,
     384,   106,   106,   106,   565,   566,   106,   106,   106,   106,
     532,   106,   114,    55,   115,    55,   525,    55,   112,   106,
      19,   106,   106,   106,   106,   586,    88,   549,    55,    88,
     111,   111,    64,   112,   112,   544,   545,   545,   115,   114,
     112,    40,    41,    42,    43,    44,    45,   112,    47,   572,
      49,    50,    51,   114,    53,   501,    55,   115,    57,    58,
      59,    60,    61,   115,   115,   115,    65,    66,   115,   115,
     579,   579,   115,   107,   115,    86,   115,   600,     3,     4,
       5,     6,     7,     8,     9,    10,    11,   115,    64,   115,
     114,   116,    91,   115,    19,    94,    95,    96,   115,   115,
     115,   115,   115,   115,   103,   104,   115,   106,   115,   115,
     115,   115,    64,   115,   505,    40,    41,    42,    43,    44,
      45,    46,    47,    88,    49,    50,    51,   111,    53,   115,
      55,    56,    57,    58,    59,    60,    61,   112,   112,   116,
      65,    66,   115,    86,    55,    55,     3,     4,     5,     6,
       7,     8,     9,    10,    11,   111,   106,   116,   113,    28,
     147,   115,    19,   114,   231,   229,    91,   115,   381,    94,
      95,    96,   132,   452,   116,     1,   123,   505,   103,   104,
     566,   106,   379,    40,    41,    42,    43,    44,    45,    46,
      47,   116,    49,    50,    51,   285,    53,    -1,    55,    56,
      57,    58,    59,    60,    61,   525,    -1,    -1,    65,    66,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      19,    -1,    -1,    -1,    91,    -1,    -1,    94,    95,    96,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,   106,
      -1,    40,    41,    42,    43,    44,    45,    46,    47,   116,
      49,    50,    51,    -1,    53,    -1,    55,    56,    57,    58,
      59,    60,    61,    -1,    -1,    -1,    65,    66,    75,    76,
      77,    78,    79,    80,    81,    82,    83,    84,    -1,    86,
      -1,    -1,    -1,    -1,    67,    68,    69,    70,    71,    72,
      -1,    -1,    91,    -1,    -1,    94,    95,    96,    -1,    -1,
      -1,    -1,    -1,    -1,   103,   104,    -1,   106,    91,    92,
      93,    94,    95,    96,    97,    98,     1,   116,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    -1,    -1,    -1,    19,    20,    21,    22,    23,    24,
      -1,    -1,    27,    -1,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    -1,    53,    -1,
      55,    56,    57,    58,    59,    60,    61,    -1,    -1,    -1,
      65,    66,   234,   235,   236,   237,   238,   239,   240,   241,
      -1,    -1,    -1,    -1,    -1,    -1,   248,    -1,    -1,    -1,
      -1,    -1,   254,    -1,   256,    -1,    91,    -1,    -1,    94,
      95,    96,    -1,    -1,    -1,    -1,    -1,    -1,   103,   104,
      -1,   106,    -1,    -1,    -1,    -1,   111,   112,   113,     1,
      -1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    -1,    -1,    -1,    19,    20,    21,
      22,    23,    24,    -1,    -1,    27,    -1,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    51,
      -1,    53,    -1,    55,    56,    57,    58,    59,    60,    61,
      -1,    -1,    -1,    65,    66,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      -1,    -1,    94,    95,    96,    -1,    -1,    -1,    -1,    -1,
      -1,   103,   104,    -1,   106,    -1,    -1,    -1,    -1,   111,
     112,   113,     1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    -1,    -1,    -1,
      19,    20,    21,    22,    23,    24,    -1,    -1,    27,    -1,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
      39,    40,    41,    42,    43,    44,    45,    46,    47,    48,
      49,    50,    51,    -1,    53,    -1,    55,    56,    57,    58,
      59,    60,    61,    -1,    -1,    -1,    65,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    -1,    91,    -1,    19,    94,    95,    96,    -1,    -1,
      -1,    -1,    -1,    -1,   103,   104,    -1,   106,    -1,    -1,
      -1,    -1,   111,    -1,   113,    40,    41,    42,    43,    44,
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
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,
      91,    -1,    19,    94,    95,    96,    -1,    -1,    -1,    -1,
      -1,    -1,   103,   104,   105,   106,   107,    -1,    -1,    -1,
      -1,   112,   113,    40,    41,    42,    43,    44,    45,    46,
      47,    -1,    49,    50,    51,    -1,    53,    -1,    55,    56,
      57,    58,    59,    60,    61,    -1,    -1,    -1,    65,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    91,    -1,    -1,    94,    95,    96,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,   106,
      -1,    -1,    -1,    -1,    -1,    -1,   113,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      -1,    -1,    -1,    19,    20,    21,    22,    23,    24,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    40,    41,    42,    43,    44,    45,
      46,    47,    48,    49,    50,    51,    -1,    53,    -1,    55,
      56,    57,    58,    59,    60,    61,    -1,    -1,    -1,    65,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    19,    -1,    94,    95,
      96,    -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,
     106,    -1,    -1,    -1,    -1,   111,    -1,    40,    41,    42,
      43,    44,    45,    46,    47,    -1,    49,    50,    51,    -1,
      53,    -1,    55,    56,    57,    58,    59,    60,    61,    -1,
      -1,    -1,    65,    66,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    91,    19,
      -1,    94,    95,    96,    -1,    -1,    -1,    -1,    -1,    -1,
     103,   104,    -1,   106,    -1,    -1,    -1,    -1,   111,    -1,
      40,    41,    42,    43,    44,    45,    46,    47,    -1,    49,
      50,    51,    -1,    53,    -1,    55,    56,    57,    58,    59,
      60,    61,    -1,    -1,    -1,    65,    66,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      -1,    -1,    -1,    -1,    20,    21,    22,    23,    24,    -1,
      -1,    91,    -1,    -1,    94,    95,    96,    67,    68,    69,
      70,    71,    72,   103,   104,    -1,   106,    -1,    -1,    -1,
      46,   111,    48,    -1,    -1,    -1,    52,    -1,    54,    55,
      56,    -1,    92,    93,    94,    95,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    -1,
      -1,    -1,    19,    -1,    -1,    91,    23,    -1,    -1,    -1,
      96,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     106,   107,    -1,    40,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    51,    -1,    53,    -1,    55,    56,
      57,    58,    59,    60,    61,    -1,    -1,    -1,    65,    66,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    19,
      -1,    -1,    -1,    -1,    91,    -1,    -1,    94,    95,    96,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,   106,
      40,    41,    42,    43,    44,    45,    46,    47,    -1,    49,
      50,    51,    -1,    53,    -1,    55,    56,    57,    58,    59,
      60,    61,    -1,    -1,    -1,    65,    66,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    19,    -1,    -1,    -1,
      -1,    91,    -1,    -1,    94,    95,    96,    -1,    -1,    -1,
      -1,    -1,    -1,   103,   104,    -1,   106,    40,    41,    42,
      43,    44,    45,    46,    47,    -1,    49,    50,    51,    -1,
      53,    -1,    55,    56,    57,    58,    59,    60,    61,    -1,
      -1,    -1,    65,    66,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    19,    -1,    -1,    -1,    -1,    91,    -1,
      -1,    94,    95,    96,    -1,    -1,    -1,    -1,    -1,    -1,
     103,   104,    -1,   106,    40,    41,    42,    43,    44,    45,
      46,    47,    -1,    49,    50,    51,    -1,    53,    -1,    55,
      56,    57,    58,    59,    60,    61,    -1,    -1,    -1,    65,
      66,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    -1,    -1,    -1,    -1,    20,    21,
      22,    23,    24,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,   104,    -1,
     106,    -1,    -1,    -1,    46,    -1,    48,    -1,    -1,    -1,
      52,    -1,    -1,    55,    56,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    -1,    -1,
      -1,    -1,    20,    21,    22,    23,    24,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      -1,    -1,    -1,    -1,    96,    -1,    -1,    -1,    46,    -1,
      48,    -1,    -1,    -1,   106,    -1,    -1,    -1,    56,    -1,
      -1,    -1,    -1,     0,     1,    63,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    -1,
      -1,    -1,    -1,    20,    21,    22,    23,    24,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    46,
      -1,    48,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    56,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    18,    -1,    20,    21,    22,
      23,    24,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    -1,    46,    -1,    48,    20,    21,    22,    23,
      24,    -1,    55,    56,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    46,    -1,    48,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    56,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    -1,    86,    -1,    -1,    89,    90,    91,
      92,    93,    94,    95,    96,    97,    98,    -1,    -1,    -1,
      -1,   103,   104,    -1,   106,   107,    67,    68,    69,    70,
      71,    72,    73,    74,    -1,    -1,    67,    68,    69,    70,
      71,    72,    73,    -1,    -1,    -1,    87,    -1,    89,    90,
      91,    92,    93,    94,    95,    96,    97,    98,    89,    90,
      91,    92,    93,    94,    95,    96,    97,    98,    67,    68,
      69,    70,    71,    72,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    93,    94,    95,    96,    97,    98
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   118,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    20,    21,    22,
      23,    24,    46,    48,    56,   119,   120,   121,   122,   123,
     125,   149,   171,   111,   112,    55,    56,   113,   124,    55,
      56,   113,   124,    55,    56,   113,   124,    55,    56,   113,
     124,    64,    52,    55,    56,    91,    96,   106,   122,   153,
     154,   155,   159,   160,   163,   164,   128,   126,   136,   134,
     131,   129,   133,   132,    56,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    86,    89,    90,    91,    92,
      93,    94,    95,    96,    97,    98,   103,   104,   106,   107,
     165,    64,    64,    56,   160,   111,   114,    23,    91,    96,
     163,    86,   172,   106,   107,    16,    17,    18,    55,    56,
     120,   137,   144,   145,   146,   148,   152,   171,   113,   137,
      88,   141,   137,   113,    55,   138,   139,   113,   106,   115,
     116,    55,   164,    55,   164,   115,   155,   160,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    19,    40,    41,
      42,    43,    44,    45,    46,    47,    49,    50,    51,    53,
      55,    56,    57,    58,    59,    60,    61,    65,    66,    91,
      94,    95,    96,   103,   104,   106,   113,   156,   187,   190,
     191,   195,   196,   201,   202,   113,   166,   167,   187,   116,
     187,   106,   112,   145,   111,   113,   174,    88,   127,   112,
      55,    56,   142,   143,   152,   113,   112,   130,    86,   114,
     140,   138,   150,   106,   106,   106,   106,   106,   106,   106,
     106,   106,   106,   106,   106,   106,   106,   106,   106,   106,
     191,   106,   106,   106,   106,    64,   106,   191,   191,   191,
     191,   191,   191,   191,   191,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    23,    46,
      48,    56,   186,   187,   192,   193,   194,   105,   107,   112,
     156,   157,   158,    67,    68,    69,    70,    71,    72,    73,
      74,    87,    89,    90,    91,    92,    93,    94,    95,    96,
      97,    98,    75,    76,    77,    78,    79,    80,    81,    82,
      83,    84,    86,   188,    62,    64,    65,    66,   105,   106,
     107,    60,     1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    27,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    46,    55,    56,   111,   120,   121,
     173,   174,   176,   177,   178,   179,   181,   182,   183,   185,
     186,   121,   168,   169,   170,   114,   115,   116,   147,   175,
     137,   114,    55,    56,   135,   137,   189,   190,   191,   139,
     112,   140,   168,   167,   197,   197,   197,   197,   197,   197,
     197,   197,   197,   187,   192,   198,   199,   200,   198,   198,
     198,   198,   198,   197,   192,   198,   198,   198,   197,    55,
     197,    55,    56,    55,    56,    55,    56,    55,    56,   114,
     115,   115,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    46,    54,    56,   107,   159,   161,   162,   194,    55,
     189,   112,   114,   190,   190,   190,   190,   190,   190,   190,
     190,   186,   190,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   187,    55,    56,    55,    55,    56,   198,   186,
     111,   112,   106,   106,   106,   173,   106,   106,   189,    88,
     111,   111,    55,   111,   186,    88,   112,   173,   120,   178,
     111,   159,   160,   161,   115,   114,   187,   168,   176,   112,
     143,   137,   112,   112,   115,   115,   115,   115,   115,   115,
     115,   115,   115,   115,   115,   114,   115,   115,   115,   115,
     115,   115,   115,   115,   115,   115,   115,   115,   187,   191,
     161,   116,   187,   162,   107,    86,   116,   112,   158,    88,
      64,    64,   115,   116,   186,   186,     1,    30,   186,   186,
      88,   173,   111,   111,   173,   178,   178,    63,   170,   115,
     112,   112,   151,   200,   115,   116,   116,   187,   156,    86,
     190,    55,    55,   115,   115,   111,   106,   115,   115,   173,
     184,   186,   184,   174,   116,   156,   173,   173,   186,   173,
     180,   115,   115,    28,   115,   174,   173,   173,   173,     1,
     111
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   117,   118,   118,   119,   119,   119,   119,   119,   120,
     121,   121,   122,   122,   122,   122,   122,   122,   123,   123,
     123,   123,   123,   123,   123,   123,   123,   123,   123,   123,
     123,   124,   124,   126,   127,   125,   128,   125,   125,   125,
     129,   130,   125,   131,   125,   125,   125,   125,   125,   132,
     125,   133,   125,   134,   135,   125,   136,   125,   125,   125,
     137,   137,   138,   138,   139,   139,   140,   140,   141,   141,
     142,   142,   143,   143,   143,   143,   144,   144,   145,   145,
     145,   145,   147,   146,   148,   148,   150,   151,   149,   152,
     152,   152,   153,   153,   154,   154,   155,   155,   156,   156,
     156,   156,   157,   157,   158,   158,   158,   159,   159,   159,
     159,   159,   160,   160,   161,   161,   161,   162,   162,   162,
     162,   162,   163,   163,   163,   163,   163,   163,   163,   163,
     163,   163,   163,   164,   165,   165,   165,   165,   165,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   165,
     165,   165,   165,   165,   165,   165,   165,   165,   165,   166,
     167,   167,   168,   168,   169,   169,   169,   170,   170,   170,
     172,   171,   173,   173,   173,   173,   173,   173,   173,   173,
     173,   175,   174,   176,   176,   177,   177,   178,   178,   179,
     179,   180,   179,   181,   181,   181,   182,   182,   182,   182,
     182,   182,   182,   183,   184,   184,   185,   185,   185,   185,
     185,   186,   186,   187,   187,   188,   188,   188,   188,   188,
     188,   188,   188,   188,   188,   188,   189,   190,   190,   190,
     190,   190,   190,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   190,   190,   190,   190,   190,   191,   191,   191,
     191,   191,   191,   191,   191,   191,   191,   191,   191,   192,
     192,   193,   193,   194,   194,   194,   194,   194,   194,   194,
     194,   194,   194,   194,   194,   194,   194,   194,   194,   194,
     194,   194,   194,   194,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   196,   196,   196,   196,   196,
     196,   196,   196,   196,   197,   197,   198,   198,   199,   199,
     200,   200,   201,   201,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   202,   202
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     0,     0,     7,     0,     5,     2,     2,
       0,     0,     7,     0,     5,     2,     2,     2,     2,     0,
       7,     0,     6,     0,     0,     8,     0,     5,     2,     2,
       0,     1,     1,     3,     1,     3,     0,     1,     0,     2,
       1,     3,     2,     2,     1,     1,     1,     2,     1,     1,
       2,     1,     0,     5,     2,     2,     0,     0,     9,     1,
       1,     1,     0,     1,     1,     3,     1,     3,     1,     2,
       3,     4,     1,     3,     1,     4,     5,     1,     1,     2,
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
       2,     2,     2,     2,     2,     2,     4,     2,     4,     1,
       2,     2,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     2,     2,     2,     2,
       2,     2,     2,     2,     1,     4,     4,     3,     5,     5,
       3,     3,     2,     2,     1,     4,     4,     4,     4,     4,
       4,     4,     4,     4,     0,     1,     0,     1,     1,     3,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     4,
       4,     4,     4,     4,     4,     4,     4,     4,     4,     4,
       4,     3,     3,     1,     2
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
#line 140 "src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2480 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 144 "src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2490 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 152 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2496 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 153 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2502 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 154 "src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2508 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 155 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2514 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 156 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2520 "build/parser.tab.cpp"
    break;

  case 9: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 160 "src/parser.y"
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
#line 2553 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 191 "src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          yyval.typeSpec.storageClasses += yyvsp[0].typeSpec.storageClasses;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isAuto) yyval.typeSpec.isAuto = true;
          if (yyvsp[0].typeSpec.isFriend) yyval.typeSpec.isFriend = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2571 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 204 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2577 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 208 "src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2583 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: AUTO  */
#line 209 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2589 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: TYPEDEF  */
#line 210 "src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2595 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: CONST  */
#line 211 "src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2601 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: FRIEND  */
#line 212 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isFriend = true; }
#line 2607 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: type_specifier  */
#line 213 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2613 "build/parser.tab.cpp"
    break;

  case 18: /* type_specifier: INT  */
#line 217 "src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2619 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: CHAR  */
#line 218 "src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2625 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: FLOAT  */
#line 219 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2631 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: DOUBLE  */
#line 220 "src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2637 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: VOID  */
#line 221 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2643 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: BOOL  */
#line 222 "src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2649 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: SHORT  */
#line 223 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2655 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: LONG  */
#line 224 "src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2661 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SIGNED  */
#line 225 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2667 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: UNSIGNED  */
#line 226 "src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2673 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: VA_LIST  */
#line 227 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2679 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: TYPE_NAME  */
#line 228 "src/parser.y"
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
#line 2698 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: struct_or_class_specifier  */
#line 242 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2704 "build/parser.tab.cpp"
    break;

  case 31: /* tag_name: IDENTIFIER  */
#line 249 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2710 "build/parser.tab.cpp"
    break;

  case 32: /* tag_name: TYPE_NAME  */
#line 250 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2716 "build/parser.tab.cpp"
    break;

  case 33: /* $@1: %empty  */
#line 254 "src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2726 "build/parser.tab.cpp"
    break;

  case 34: /* $@2: %empty  */
#line 258 "src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2732 "build/parser.tab.cpp"
    break;

  case 35: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 258 "src/parser.y"
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
#line 2750 "build/parser.tab.cpp"
    break;

  case 36: /* @3: %empty  */
#line 274 "src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2762 "build/parser.tab.cpp"
    break;

  case 37: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 280 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2775 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 288 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2786 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 294 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2797 "build/parser.tab.cpp"
    break;

  case 40: /* $@4: %empty  */
#line 300 "src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "UNION");
          enterClass(yyvsp[0].str, "union");
      }
#line 2807 "build/parser.tab.cpp"
    break;

  case 41: /* $@5: %empty  */
#line 304 "src/parser.y"
            { pushScope("union " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2813 "build/parser.tab.cpp"
    break;

  case 42: /* struct_or_class_specifier: UNION tag_name $@4 '{' $@5 member_decl_list_opt '}'  */
#line 304 "src/parser.y"
                                                                                                   {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::UnionDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2827 "build/parser.tab.cpp"
    break;

  case 43: /* @6: %empty  */
#line 313 "src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "union");
          pushScope("union " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2839 "build/parser.tab.cpp"
    break;

  case 44: /* struct_or_class_specifier: UNION '{' @6 member_decl_list_opt '}'  */
#line 319 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::UnionDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2852 "build/parser.tab.cpp"
    break;

  case 45: /* struct_or_class_specifier: UNION IDENTIFIER  */
#line 327 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2863 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: UNION TYPE_NAME  */
#line 333 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2874 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: ENUM IDENTIFIER  */
#line 339 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2885 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: ENUM TYPE_NAME  */
#line 345 "src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2896 "build/parser.tab.cpp"
    break;

  case 49: /* $@7: %empty  */
#line 351 "src/parser.y"
                    {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM");
      }
#line 2905 "build/parser.tab.cpp"
    break;

  case 50: /* struct_or_class_specifier: ENUM tag_name $@7 '{' enumerator_list comma_opt '}'  */
#line 354 "src/parser.y"
                                          {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2918 "build/parser.tab.cpp"
    break;

  case 51: /* @8: %empty  */
#line 362 "src/parser.y"
               {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[-1].idx});
      }
#line 2927 "build/parser.tab.cpp"
    break;

  case 52: /* struct_or_class_specifier: ENUM '{' @8 enumerator_list comma_opt '}'  */
#line 365 "src/parser.y"
                                      {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-3].str;
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-3].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2939 "build/parser.tab.cpp"
    break;

  case 53: /* $@9: %empty  */
#line 372 "src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2949 "build/parser.tab.cpp"
    break;

  case 54: /* $@10: %empty  */
#line 376 "src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2955 "build/parser.tab.cpp"
    break;

  case 55: /* struct_or_class_specifier: CLASS tag_name $@9 inheritance_opt '{' $@10 member_decl_list_opt '}'  */
#line 376 "src/parser.y"
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
#line 2972 "build/parser.tab.cpp"
    break;

  case 56: /* @11: %empty  */
#line 388 "src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2984 "build/parser.tab.cpp"
    break;

  case 57: /* struct_or_class_specifier: CLASS '{' @11 member_decl_list_opt '}'  */
#line 394 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2997 "build/parser.tab.cpp"
    break;

  case 58: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 402 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3008 "build/parser.tab.cpp"
    break;

  case 59: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 408 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 3019 "build/parser.tab.cpp"
    break;

  case 60: /* member_decl_list_opt: %empty  */
#line 417 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3025 "build/parser.tab.cpp"
    break;

  case 61: /* member_decl_list_opt: member_decl_list  */
#line 418 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 3031 "build/parser.tab.cpp"
    break;

  case 62: /* enumerator_list: enumerator  */
#line 425 "src/parser.y"
                 { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3037 "build/parser.tab.cpp"
    break;

  case 63: /* enumerator_list: enumerator_list ',' enumerator  */
#line 426 "src/parser.y"
                                     { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3043 "build/parser.tab.cpp"
    break;

  case 64: /* enumerator: IDENTIFIER  */
#line 430 "src/parser.y"
                 {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[0].str), yyvsp[0].idx);
      }
#line 3053 "build/parser.tab.cpp"
    break;

  case 65: /* enumerator: IDENTIFIER '=' constant_expr  */
#line 435 "src/parser.y"
                                   {
          declareSymbol(yyvsp[-2].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3063 "build/parser.tab.cpp"
    break;

  case 66: /* comma_opt: %empty  */
#line 443 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3069 "build/parser.tab.cpp"
    break;

  case 67: /* comma_opt: ','  */
#line 444 "src/parser.y"
          { yyval = ParserValue(); }
#line 3075 "build/parser.tab.cpp"
    break;

  case 68: /* inheritance_opt: %empty  */
#line 448 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3081 "build/parser.tab.cpp"
    break;

  case 69: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 449 "src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 3087 "build/parser.tab.cpp"
    break;

  case 70: /* inheritance_specifier_list: inheritance_specifier  */
#line 453 "src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 3093 "build/parser.tab.cpp"
    break;

  case 71: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 454 "src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 3102 "build/parser.tab.cpp"
    break;

  case 72: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 461 "src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3113 "build/parser.tab.cpp"
    break;

  case 73: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 467 "src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3124 "build/parser.tab.cpp"
    break;

  case 74: /* inheritance_specifier: IDENTIFIER  */
#line 473 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3135 "build/parser.tab.cpp"
    break;

  case 75: /* inheritance_specifier: TYPE_NAME  */
#line 479 "src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3146 "build/parser.tab.cpp"
    break;

  case 76: /* member_decl_list: member_item  */
#line 490 "src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 3156 "build/parser.tab.cpp"
    break;

  case 77: /* member_decl_list: member_decl_list member_item  */
#line 495 "src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 3170 "build/parser.tab.cpp"
    break;

  case 78: /* member_item: declaration  */
#line 507 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3176 "build/parser.tab.cpp"
    break;

  case 79: /* member_item: function_definition  */
#line 508 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3182 "build/parser.tab.cpp"
    break;

  case 80: /* member_item: access_specifier ':'  */
#line 509 "src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3188 "build/parser.tab.cpp"
    break;

  case 81: /* member_item: constructor_def  */
#line 510 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3194 "build/parser.tab.cpp"
    break;

  case 82: /* $@12: %empty  */
#line 519 "src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3200 "build/parser.tab.cpp"
    break;

  case 83: /* constructor_head: IDENTIFIER '(' $@12 parameter_list_opt ')'  */
#line 519 "src/parser.y"
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
#line 3220 "build/parser.tab.cpp"
    break;

  case 84: /* constructor_def: constructor_head compound_stmt  */
#line 537 "src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3229 "build/parser.tab.cpp"
    break;

  case 85: /* constructor_def: constructor_head ';'  */
#line 541 "src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3238 "build/parser.tab.cpp"
    break;

  case 86: /* $@13: %empty  */
#line 549 "src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3248 "build/parser.tab.cpp"
    break;

  case 87: /* $@14: %empty  */
#line 553 "src/parser.y"
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
#line 3265 "build/parser.tab.cpp"
    break;

  case 88: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@13 parameter_list_opt ')' $@14 compound_stmt  */
#line 564 "src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3275 "build/parser.tab.cpp"
    break;

  case 92: /* init_declarator_list_opt: %empty  */
#line 579 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3281 "build/parser.tab.cpp"
    break;

  case 93: /* init_declarator_list_opt: init_declarator_list  */
#line 580 "src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3287 "build/parser.tab.cpp"
    break;

  case 94: /* init_declarator_list: init_declarator  */
#line 584 "src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3293 "build/parser.tab.cpp"
    break;

  case 95: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 585 "src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3299 "build/parser.tab.cpp"
    break;

  case 96: /* init_declarator: declarator  */
#line 589 "src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3305 "build/parser.tab.cpp"
    break;

  case 97: /* init_declarator: declarator '=' initializer  */
#line 590 "src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3311 "build/parser.tab.cpp"
    break;

  case 98: /* initializer: assignment_expr  */
#line 594 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3317 "build/parser.tab.cpp"
    break;

  case 99: /* initializer: '{' '}'  */
#line 595 "src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3323 "build/parser.tab.cpp"
    break;

  case 100: /* initializer: '{' initializer_list '}'  */
#line 596 "src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3333 "build/parser.tab.cpp"
    break;

  case 101: /* initializer: '{' initializer_list ',' '}'  */
#line 601 "src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3343 "build/parser.tab.cpp"
    break;

  case 102: /* initializer_list: initializer_item  */
#line 609 "src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3349 "build/parser.tab.cpp"
    break;

  case 103: /* initializer_list: initializer_list ',' initializer_item  */
#line 610 "src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3355 "build/parser.tab.cpp"
    break;

  case 104: /* initializer_item: initializer  */
#line 614 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3361 "build/parser.tab.cpp"
    break;

  case 105: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 615 "src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3369 "build/parser.tab.cpp"
    break;

  case 106: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 618 "src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3377 "build/parser.tab.cpp"
    break;

  case 107: /* pointer: '*'  */
#line 624 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3383 "build/parser.tab.cpp"
    break;

  case 108: /* pointer: '&'  */
#line 625 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3389 "build/parser.tab.cpp"
    break;

  case 109: /* pointer: pointer '*'  */
#line 626 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3395 "build/parser.tab.cpp"
    break;

  case 110: /* pointer: pointer '&'  */
#line 627 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3401 "build/parser.tab.cpp"
    break;

  case 111: /* pointer: pointer CONST  */
#line 628 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3407 "build/parser.tab.cpp"
    break;

  case 112: /* declarator: pointer direct_declarator  */
#line 632 "src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3418 "build/parser.tab.cpp"
    break;

  case 113: /* declarator: direct_declarator  */
#line 638 "src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3424 "build/parser.tab.cpp"
    break;

  case 114: /* abstract_declarator: pointer  */
#line 644 "src/parser.y"
              { yyval = yyvsp[0]; }
#line 3430 "build/parser.tab.cpp"
    break;

  case 115: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 645 "src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3441 "build/parser.tab.cpp"
    break;

  case 116: /* abstract_declarator: direct_abstract_declarator  */
#line 651 "src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3447 "build/parser.tab.cpp"
    break;

  case 117: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 655 "src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3461 "build/parser.tab.cpp"
    break;

  case 118: /* direct_abstract_declarator: '[' ']'  */
#line 664 "src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3467 "build/parser.tab.cpp"
    break;

  case 119: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 665 "src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3473 "build/parser.tab.cpp"
    break;

  case 120: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 666 "src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3479 "build/parser.tab.cpp"
    break;

  case 121: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 667 "src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3485 "build/parser.tab.cpp"
    break;

  case 122: /* direct_declarator: IDENTIFIER  */
#line 671 "src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3494 "build/parser.tab.cpp"
    break;

  case 123: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 675 "src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3506 "build/parser.tab.cpp"
    break;

  case 124: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 682 "src/parser.y"
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
#line 3523 "build/parser.tab.cpp"
    break;

  case 125: /* direct_declarator: '(' declarator ')'  */
#line 694 "src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3537 "build/parser.tab.cpp"
    break;

  case 126: /* direct_declarator: operator_function_id  */
#line 703 "src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3546 "build/parser.tab.cpp"
    break;

  case 127: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 707 "src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3558 "build/parser.tab.cpp"
    break;

  case 128: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 714 "src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3570 "build/parser.tab.cpp"
    break;

  case 129: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 721 "src/parser.y"
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
#line 3594 "build/parser.tab.cpp"
    break;

  case 130: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 740 "src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3606 "build/parser.tab.cpp"
    break;

  case 131: /* direct_declarator: direct_declarator '[' ']'  */
#line 747 "src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3612 "build/parser.tab.cpp"
    break;

  case 132: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 748 "src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3618 "build/parser.tab.cpp"
    break;

  case 133: /* operator_function_id: OPERATOR overloadable_operator  */
#line 753 "src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3624 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: '+'  */
#line 757 "src/parser.y"
          { yyval.str = "+"; }
#line 3630 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: '-'  */
#line 757 "src/parser.y"
                                  { yyval.str = "-"; }
#line 3636 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: '*'  */
#line 757 "src/parser.y"
                                                          { yyval.str = "*"; }
#line 3642 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: '/'  */
#line 757 "src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3648 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: '%'  */
#line 758 "src/parser.y"
          { yyval.str = "%"; }
#line 3654 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: '^'  */
#line 758 "src/parser.y"
                                  { yyval.str = "^"; }
#line 3660 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: '&'  */
#line 758 "src/parser.y"
                                                          { yyval.str = "&"; }
#line 3666 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: '|'  */
#line 758 "src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3672 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: '~'  */
#line 759 "src/parser.y"
          { yyval.str = "~"; }
#line 3678 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: '!'  */
#line 759 "src/parser.y"
                                  { yyval.str = "!"; }
#line 3684 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: '='  */
#line 759 "src/parser.y"
                                                          { yyval.str = "="; }
#line 3690 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: '<'  */
#line 759 "src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3696 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: '>'  */
#line 760 "src/parser.y"
          { yyval.str = ">"; }
#line 3702 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: EQ_OP  */
#line 760 "src/parser.y"
                                    { yyval.str = "=="; }
#line 3708 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: NE_OP  */
#line 760 "src/parser.y"
                                                               { yyval.str = "!="; }
#line 3714 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: LE_OP  */
#line 760 "src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3720 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: GE_OP  */
#line 761 "src/parser.y"
            { yyval.str = ">="; }
#line 3726 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: AND_OP  */
#line 761 "src/parser.y"
                                        { yyval.str = "&&"; }
#line 3732 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: OR_OP  */
#line 761 "src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3738 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: SHL  */
#line 761 "src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3744 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: SHR  */
#line 762 "src/parser.y"
          { yyval.str = ">>"; }
#line 3750 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: INC  */
#line 762 "src/parser.y"
                                   { yyval.str = "++"; }
#line 3756 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: DEC  */
#line 762 "src/parser.y"
                                                            { yyval.str = "--"; }
#line 3762 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: PLUS_ASSIGN  */
#line 763 "src/parser.y"
                  { yyval.str = "+="; }
#line 3768 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: MINUS_ASSIGN  */
#line 763 "src/parser.y"
                                                    { yyval.str = "-="; }
#line 3774 "build/parser.tab.cpp"
    break;

  case 159: /* overloadable_operator: MUL_ASSIGN  */
#line 763 "src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3780 "build/parser.tab.cpp"
    break;

  case 160: /* overloadable_operator: DIV_ASSIGN  */
#line 764 "src/parser.y"
                 { yyval.str = "/="; }
#line 3786 "build/parser.tab.cpp"
    break;

  case 161: /* overloadable_operator: MOD_ASSIGN  */
#line 764 "src/parser.y"
                                                 { yyval.str = "%="; }
#line 3792 "build/parser.tab.cpp"
    break;

  case 162: /* overloadable_operator: AND_ASSIGN  */
#line 764 "src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3798 "build/parser.tab.cpp"
    break;

  case 163: /* overloadable_operator: OR_ASSIGN  */
#line 765 "src/parser.y"
                { yyval.str = "|="; }
#line 3804 "build/parser.tab.cpp"
    break;

  case 164: /* overloadable_operator: XOR_ASSIGN  */
#line 765 "src/parser.y"
                                                { yyval.str = "^="; }
#line 3810 "build/parser.tab.cpp"
    break;

  case 165: /* overloadable_operator: SHL_ASSIGN  */
#line 765 "src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3816 "build/parser.tab.cpp"
    break;

  case 166: /* overloadable_operator: SHR_ASSIGN  */
#line 766 "src/parser.y"
                 { yyval.str = ">>="; }
#line 3822 "build/parser.tab.cpp"
    break;

  case 167: /* overloadable_operator: '[' ']'  */
#line 766 "src/parser.y"
                                               { yyval.str = "[]"; }
#line 3828 "build/parser.tab.cpp"
    break;

  case 168: /* overloadable_operator: '(' ')'  */
#line 766 "src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3834 "build/parser.tab.cpp"
    break;

  case 169: /* param_scope: %empty  */
#line 773 "src/parser.y"
                                           { pushScope(); }
#line 3840 "build/parser.tab.cpp"
    break;

  case 170: /* constructor_args: assignment_expr  */
#line 777 "src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3846 "build/parser.tab.cpp"
    break;

  case 171: /* constructor_args: constructor_args ',' assignment_expr  */
#line 778 "src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3852 "build/parser.tab.cpp"
    break;

  case 172: /* parameter_list_opt: %empty  */
#line 782 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3858 "build/parser.tab.cpp"
    break;

  case 173: /* parameter_list_opt: parameter_list  */
#line 783 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3864 "build/parser.tab.cpp"
    break;

  case 174: /* parameter_list: parameter_decl  */
#line 787 "src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3873 "build/parser.tab.cpp"
    break;

  case 175: /* parameter_list: parameter_list ',' parameter_decl  */
#line 791 "src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3882 "build/parser.tab.cpp"
    break;

  case 176: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 795 "src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3888 "build/parser.tab.cpp"
    break;

  case 177: /* parameter_decl: declaration_specifiers declarator  */
#line 799 "src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3898 "build/parser.tab.cpp"
    break;

  case 178: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 804 "src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3908 "build/parser.tab.cpp"
    break;

  case 179: /* parameter_decl: declaration_specifiers  */
#line 809 "src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3918 "build/parser.tab.cpp"
    break;

  case 180: /* $@15: %empty  */
#line 817 "src/parser.y"
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
#line 3960 "build/parser.tab.cpp"
    break;

  case 181: /* function_definition: declaration_specifiers declarator $@15 '{' block_item_list_opt '}'  */
#line 853 "src/parser.y"
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
#line 3991 "build/parser.tab.cpp"
    break;

  case 182: /* statement: compound_stmt  */
#line 882 "src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3997 "build/parser.tab.cpp"
    break;

  case 183: /* statement: expr_stmt  */
#line 883 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 4003 "build/parser.tab.cpp"
    break;

  case 184: /* statement: selection_stmt  */
#line 884 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4009 "build/parser.tab.cpp"
    break;

  case 185: /* statement: iteration_stmt  */
#line 885 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4015 "build/parser.tab.cpp"
    break;

  case 186: /* statement: jump_stmt  */
#line 886 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 4021 "build/parser.tab.cpp"
    break;

  case 187: /* statement: labeled_stmt  */
#line 887 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4027 "build/parser.tab.cpp"
    break;

  case 188: /* statement: declaration  */
#line 888 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4033 "build/parser.tab.cpp"
    break;

  case 189: /* statement: error ';'  */
#line 889 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4039 "build/parser.tab.cpp"
    break;

  case 190: /* statement: error '}'  */
#line 890 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 4045 "build/parser.tab.cpp"
    break;

  case 191: /* $@16: %empty  */
#line 894 "src/parser.y"
          { pushScope(); }
#line 4051 "build/parser.tab.cpp"
    break;

  case 192: /* compound_stmt: '{' $@16 block_item_list_opt '}'  */
#line 894 "src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 4062 "build/parser.tab.cpp"
    break;

  case 193: /* block_item_list_opt: %empty  */
#line 903 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4068 "build/parser.tab.cpp"
    break;

  case 194: /* block_item_list_opt: block_item_list  */
#line 904 "src/parser.y"
                      { yyval = yyvsp[0]; }
#line 4074 "build/parser.tab.cpp"
    break;

  case 195: /* block_item_list: statement  */
#line 908 "src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4080 "build/parser.tab.cpp"
    break;

  case 196: /* block_item_list: block_item_list statement  */
#line 909 "src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 4086 "build/parser.tab.cpp"
    break;

  case 197: /* expr_stmt: ';'  */
#line 913 "src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 4092 "build/parser.tab.cpp"
    break;

  case 198: /* expr_stmt: expr ';'  */
#line 914 "src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 4098 "build/parser.tab.cpp"
    break;

  case 199: /* selection_stmt: IF '(' expr ')' statement  */
#line 918 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4106 "build/parser.tab.cpp"
    break;

  case 200: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 921 "src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 4114 "build/parser.tab.cpp"
    break;

  case 201: /* $@17: %empty  */
#line 924 "src/parser.y"
                          { hintScope("switch"); }
#line 4120 "build/parser.tab.cpp"
    break;

  case 202: /* selection_stmt: SWITCH '(' expr ')' $@17 compound_stmt  */
#line 924 "src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4128 "build/parser.tab.cpp"
    break;

  case 203: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 930 "src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4136 "build/parser.tab.cpp"
    break;

  case 204: /* labeled_stmt: DEFAULT ':' statement  */
#line 933 "src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4144 "build/parser.tab.cpp"
    break;

  case 205: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 936 "src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4154 "build/parser.tab.cpp"
    break;

  case 206: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 944 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4162 "build/parser.tab.cpp"
    break;

  case 207: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 947 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4170 "build/parser.tab.cpp"
    break;

  case 208: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 954 "src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4179 "build/parser.tab.cpp"
    break;

  case 209: /* iteration_stmt: DO statement error ';'  */
#line 958 "src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4188 "build/parser.tab.cpp"
    break;

  case 210: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 962 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4196 "build/parser.tab.cpp"
    break;

  case 211: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 965 "src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4205 "build/parser.tab.cpp"
    break;

  case 212: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 969 "src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4214 "build/parser.tab.cpp"
    break;

  case 213: /* for_open: FOR '('  */
#line 978 "src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4220 "build/parser.tab.cpp"
    break;

  case 214: /* for_incr_opt: %empty  */
#line 982 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4226 "build/parser.tab.cpp"
    break;

  case 215: /* for_incr_opt: expr  */
#line 983 "src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4232 "build/parser.tab.cpp"
    break;

  case 216: /* jump_stmt: BREAK ';'  */
#line 987 "src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4238 "build/parser.tab.cpp"
    break;

  case 217: /* jump_stmt: CONTINUE ';'  */
#line 988 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4244 "build/parser.tab.cpp"
    break;

  case 218: /* jump_stmt: RETURN ';'  */
#line 989 "src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4250 "build/parser.tab.cpp"
    break;

  case 219: /* jump_stmt: RETURN expr ';'  */
#line 990 "src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4256 "build/parser.tab.cpp"
    break;

  case 220: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 991 "src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4268 "build/parser.tab.cpp"
    break;

  case 221: /* expr: assignment_expr  */
#line 1001 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4274 "build/parser.tab.cpp"
    break;

  case 222: /* expr: expr ',' assignment_expr  */
#line 1002 "src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4280 "build/parser.tab.cpp"
    break;

  case 223: /* assignment_expr: binary_expr  */
#line 1006 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4286 "build/parser.tab.cpp"
    break;

  case 224: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 1007 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4294 "build/parser.tab.cpp"
    break;

  case 225: /* assign_op: '='  */
#line 1013 "src/parser.y"
                   { yyval.str = "="; }
#line 4300 "build/parser.tab.cpp"
    break;

  case 226: /* assign_op: PLUS_ASSIGN  */
#line 1014 "src/parser.y"
                   { yyval.str = "+="; }
#line 4306 "build/parser.tab.cpp"
    break;

  case 227: /* assign_op: MINUS_ASSIGN  */
#line 1015 "src/parser.y"
                   { yyval.str = "-="; }
#line 4312 "build/parser.tab.cpp"
    break;

  case 228: /* assign_op: MUL_ASSIGN  */
#line 1016 "src/parser.y"
                   { yyval.str = "*="; }
#line 4318 "build/parser.tab.cpp"
    break;

  case 229: /* assign_op: DIV_ASSIGN  */
#line 1017 "src/parser.y"
                   { yyval.str = "/="; }
#line 4324 "build/parser.tab.cpp"
    break;

  case 230: /* assign_op: MOD_ASSIGN  */
#line 1018 "src/parser.y"
                   { yyval.str = "%="; }
#line 4330 "build/parser.tab.cpp"
    break;

  case 231: /* assign_op: AND_ASSIGN  */
#line 1019 "src/parser.y"
                   { yyval.str = "&="; }
#line 4336 "build/parser.tab.cpp"
    break;

  case 232: /* assign_op: OR_ASSIGN  */
#line 1020 "src/parser.y"
                   { yyval.str = "|="; }
#line 4342 "build/parser.tab.cpp"
    break;

  case 233: /* assign_op: XOR_ASSIGN  */
#line 1021 "src/parser.y"
                   { yyval.str = "^="; }
#line 4348 "build/parser.tab.cpp"
    break;

  case 234: /* assign_op: SHL_ASSIGN  */
#line 1022 "src/parser.y"
                   { yyval.str = "<<="; }
#line 4354 "build/parser.tab.cpp"
    break;

  case 235: /* assign_op: SHR_ASSIGN  */
#line 1023 "src/parser.y"
                   { yyval.str = ">>="; }
#line 4360 "build/parser.tab.cpp"
    break;

  case 236: /* constant_expr: binary_expr  */
#line 1027 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4366 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 1031 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4372 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 1032 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4378 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr '|' binary_expr  */
#line 1033 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4384 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr '^' binary_expr  */
#line 1034 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4390 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr '&' binary_expr  */
#line 1035 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4396 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 1036 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4402 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 1037 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4408 "build/parser.tab.cpp"
    break;

  case 244: /* binary_expr: binary_expr '<' binary_expr  */
#line 1038 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4414 "build/parser.tab.cpp"
    break;

  case 245: /* binary_expr: binary_expr '>' binary_expr  */
#line 1039 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4420 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 1040 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4426 "build/parser.tab.cpp"
    break;

  case 247: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 1041 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4432 "build/parser.tab.cpp"
    break;

  case 248: /* binary_expr: binary_expr SHL binary_expr  */
#line 1042 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4438 "build/parser.tab.cpp"
    break;

  case 249: /* binary_expr: binary_expr SHR binary_expr  */
#line 1043 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4444 "build/parser.tab.cpp"
    break;

  case 250: /* binary_expr: binary_expr '+' binary_expr  */
#line 1044 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4450 "build/parser.tab.cpp"
    break;

  case 251: /* binary_expr: binary_expr '-' binary_expr  */
#line 1045 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4456 "build/parser.tab.cpp"
    break;

  case 252: /* binary_expr: binary_expr '*' binary_expr  */
#line 1046 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4462 "build/parser.tab.cpp"
    break;

  case 253: /* binary_expr: binary_expr '/' binary_expr  */
#line 1047 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4468 "build/parser.tab.cpp"
    break;

  case 254: /* binary_expr: binary_expr '%' binary_expr  */
#line 1048 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4474 "build/parser.tab.cpp"
    break;

  case 255: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 1049 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4482 "build/parser.tab.cpp"
    break;

  case 256: /* binary_expr: unary_expr  */
#line 1052 "src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4488 "build/parser.tab.cpp"
    break;

  case 257: /* unary_expr: postfix_expr  */
#line 1056 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4494 "build/parser.tab.cpp"
    break;

  case 258: /* unary_expr: INC unary_expr  */
#line 1057 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4500 "build/parser.tab.cpp"
    break;

  case 259: /* unary_expr: DEC unary_expr  */
#line 1058 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4506 "build/parser.tab.cpp"
    break;

  case 260: /* unary_expr: '&' unary_expr  */
#line 1059 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4512 "build/parser.tab.cpp"
    break;

  case 261: /* unary_expr: '*' unary_expr  */
#line 1060 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4518 "build/parser.tab.cpp"
    break;

  case 262: /* unary_expr: '+' unary_expr  */
#line 1061 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4524 "build/parser.tab.cpp"
    break;

  case 263: /* unary_expr: '-' unary_expr  */
#line 1062 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4530 "build/parser.tab.cpp"
    break;

  case 264: /* unary_expr: '!' unary_expr  */
#line 1063 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4536 "build/parser.tab.cpp"
    break;

  case 265: /* unary_expr: '~' unary_expr  */
#line 1064 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4542 "build/parser.tab.cpp"
    break;

  case 266: /* unary_expr: '(' type_name ')' unary_expr  */
#line 1065 "src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4551 "build/parser.tab.cpp"
    break;

  case 267: /* unary_expr: SIZEOF unary_expr  */
#line 1069 "src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4557 "build/parser.tab.cpp"
    break;

  case 268: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 1070 "src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4566 "build/parser.tab.cpp"
    break;

  case 269: /* type_name: type_name_specifiers  */
#line 1077 "src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4575 "build/parser.tab.cpp"
    break;

  case 270: /* type_name: type_name_specifiers abstract_declarator  */
#line 1081 "src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4584 "build/parser.tab.cpp"
    break;

  case 271: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1088 "src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4596 "build/parser.tab.cpp"
    break;

  case 272: /* type_name_specifiers: type_name_specifier  */
#line 1095 "src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4602 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifier: INT  */
#line 1099 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4608 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifier: CHAR  */
#line 1100 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4614 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: FLOAT  */
#line 1101 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4620 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: DOUBLE  */
#line 1102 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4626 "build/parser.tab.cpp"
    break;

  case 277: /* type_name_specifier: VOID  */
#line 1103 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4632 "build/parser.tab.cpp"
    break;

  case 278: /* type_name_specifier: BOOL  */
#line 1104 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4638 "build/parser.tab.cpp"
    break;

  case 279: /* type_name_specifier: SHORT  */
#line 1105 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4644 "build/parser.tab.cpp"
    break;

  case 280: /* type_name_specifier: LONG  */
#line 1106 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4650 "build/parser.tab.cpp"
    break;

  case 281: /* type_name_specifier: SIGNED  */
#line 1107 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4656 "build/parser.tab.cpp"
    break;

  case 282: /* type_name_specifier: UNSIGNED  */
#line 1108 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4662 "build/parser.tab.cpp"
    break;

  case 283: /* type_name_specifier: VA_LIST  */
#line 1109 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4668 "build/parser.tab.cpp"
    break;

  case 284: /* type_name_specifier: CONST  */
#line 1110 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4674 "build/parser.tab.cpp"
    break;

  case 285: /* type_name_specifier: TYPE_NAME  */
#line 1111 "src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4688 "build/parser.tab.cpp"
    break;

  case 286: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1120 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4699 "build/parser.tab.cpp"
    break;

  case 287: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1126 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4710 "build/parser.tab.cpp"
    break;

  case 288: /* type_name_specifier: UNION IDENTIFIER  */
#line 1132 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4721 "build/parser.tab.cpp"
    break;

  case 289: /* type_name_specifier: UNION TYPE_NAME  */
#line 1138 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4732 "build/parser.tab.cpp"
    break;

  case 290: /* type_name_specifier: ENUM IDENTIFIER  */
#line 1144 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4743 "build/parser.tab.cpp"
    break;

  case 291: /* type_name_specifier: ENUM TYPE_NAME  */
#line 1150 "src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4754 "build/parser.tab.cpp"
    break;

  case 292: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1156 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4765 "build/parser.tab.cpp"
    break;

  case 293: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1162 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4776 "build/parser.tab.cpp"
    break;

  case 294: /* postfix_expr: primary_expr  */
#line 1171 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4782 "build/parser.tab.cpp"
    break;

  case 295: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1172 "src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4788 "build/parser.tab.cpp"
    break;

  case 296: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1173 "src/parser.y"
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
#line 4828 "build/parser.tab.cpp"
    break;

  case 297: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1208 "src/parser.y"
                                  {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4837 "build/parser.tab.cpp"
    break;

  case 298: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1212 "src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4850 "build/parser.tab.cpp"
    break;

  case 299: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1220 "src/parser.y"
                                                        {
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4861 "build/parser.tab.cpp"
    break;

  case 300: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1226 "src/parser.y"
                                    {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4870 "build/parser.tab.cpp"
    break;

  case 301: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1230 "src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4876 "build/parser.tab.cpp"
    break;

  case 302: /* postfix_expr: postfix_expr INC  */
#line 1231 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4882 "build/parser.tab.cpp"
    break;

  case 303: /* postfix_expr: postfix_expr DEC  */
#line 1232 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4888 "build/parser.tab.cpp"
    break;

  case 304: /* postfix_expr: builtin_call  */
#line 1233 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4894 "build/parser.tab.cpp"
    break;

  case 305: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1237 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4900 "build/parser.tab.cpp"
    break;

  case 306: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1238 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4906 "build/parser.tab.cpp"
    break;

  case 307: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1239 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4912 "build/parser.tab.cpp"
    break;

  case 308: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1240 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4918 "build/parser.tab.cpp"
    break;

  case 309: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1241 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4924 "build/parser.tab.cpp"
    break;

  case 310: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1242 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4930 "build/parser.tab.cpp"
    break;

  case 311: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1243 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4936 "build/parser.tab.cpp"
    break;

  case 312: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1244 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4942 "build/parser.tab.cpp"
    break;

  case 313: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1245 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4948 "build/parser.tab.cpp"
    break;

  case 314: /* constructor_args_opt: %empty  */
#line 1249 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4954 "build/parser.tab.cpp"
    break;

  case 315: /* constructor_args_opt: constructor_args  */
#line 1250 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4960 "build/parser.tab.cpp"
    break;

  case 316: /* argument_list_opt: %empty  */
#line 1254 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4966 "build/parser.tab.cpp"
    break;

  case 317: /* argument_list_opt: argument_list  */
#line 1255 "src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4972 "build/parser.tab.cpp"
    break;

  case 318: /* argument_list: argument  */
#line 1259 "src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4978 "build/parser.tab.cpp"
    break;

  case 319: /* argument_list: argument_list ',' argument  */
#line 1260 "src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4984 "build/parser.tab.cpp"
    break;

  case 320: /* argument: assignment_expr  */
#line 1264 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4990 "build/parser.tab.cpp"
    break;

  case 321: /* argument: type_name  */
#line 1265 "src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4999 "build/parser.tab.cpp"
    break;

  case 322: /* primary_expr: IDENTIFIER  */
#line 1272 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 5013 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: INT_LITERAL  */
#line 1281 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5019 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: FLOAT_LITERAL  */
#line 1282 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5025 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: CHAR_LITERAL  */
#line 1283 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5031 "build/parser.tab.cpp"
    break;

  case 326: /* primary_expr: string_literal  */
#line 1284 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 5037 "build/parser.tab.cpp"
    break;

  case 327: /* primary_expr: BOOL_LITERAL  */
#line 1285 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5043 "build/parser.tab.cpp"
    break;

  case 328: /* primary_expr: THIS  */
#line 1286 "src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 5049 "build/parser.tab.cpp"
    break;

  case 329: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1287 "src/parser.y"
                                             {
          /* `Dog()`: a temporary object (for a scalar type, `int(x)`, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5058 "build/parser.tab.cpp"
    break;

  case 330: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1291 "src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 5068 "build/parser.tab.cpp"
    break;

  case 331: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1298 "src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5074 "build/parser.tab.cpp"
    break;

  case 332: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1299 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5080 "build/parser.tab.cpp"
    break;

  case 333: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1300 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5086 "build/parser.tab.cpp"
    break;

  case 334: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1301 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5092 "build/parser.tab.cpp"
    break;

  case 335: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1302 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5098 "build/parser.tab.cpp"
    break;

  case 336: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1303 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5104 "build/parser.tab.cpp"
    break;

  case 337: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1304 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5110 "build/parser.tab.cpp"
    break;

  case 338: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1305 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5116 "build/parser.tab.cpp"
    break;

  case 339: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1306 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5122 "build/parser.tab.cpp"
    break;

  case 340: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1307 "src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5128 "build/parser.tab.cpp"
    break;

  case 341: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1308 "src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 5140 "build/parser.tab.cpp"
    break;

  case 342: /* primary_expr: '(' expr ')'  */
#line 1315 "src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 5146 "build/parser.tab.cpp"
    break;

  case 343: /* string_literal: STRING_LITERAL  */
#line 1320 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5152 "build/parser.tab.cpp"
    break;

  case 344: /* string_literal: string_literal STRING_LITERAL  */
#line 1321 "src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 5162 "build/parser.tab.cpp"
    break;


#line 5166 "build/parser.tab.cpp"

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

#line 1328 "src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
