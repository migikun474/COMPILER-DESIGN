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
  YYSYMBOL_ENUM = 14,                      /* ENUM  */
  YYSYMBOL_PUBLIC = 15,                    /* PUBLIC  */
  YYSYMBOL_PRIVATE = 16,                   /* PRIVATE  */
  YYSYMBOL_PROTECTED = 17,                 /* PROTECTED  */
  YYSYMBOL_THIS = 18,                      /* THIS  */
  YYSYMBOL_STATIC = 19,                    /* STATIC  */
  YYSYMBOL_TYPEDEF = 20,                   /* TYPEDEF  */
  YYSYMBOL_AUTO = 21,                      /* AUTO  */
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
  YYSYMBOL_129_5 = 129,                    /* @5  */
  YYSYMBOL_130_6 = 130,                    /* $@6  */
  YYSYMBOL_131_7 = 131,                    /* $@7  */
  YYSYMBOL_132_8 = 132,                    /* @8  */
  YYSYMBOL_member_decl_list_opt = 133,     /* member_decl_list_opt  */
  YYSYMBOL_enumerator_list = 134,          /* enumerator_list  */
  YYSYMBOL_enumerator = 135,               /* enumerator  */
  YYSYMBOL_comma_opt = 136,                /* comma_opt  */
  YYSYMBOL_inheritance_opt = 137,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 138, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 139,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 140,         /* member_decl_list  */
  YYSYMBOL_member_item = 141,              /* member_item  */
  YYSYMBOL_constructor_head = 142,         /* constructor_head  */
  YYSYMBOL_143_9 = 143,                    /* $@9  */
  YYSYMBOL_constructor_def = 144,          /* constructor_def  */
  YYSYMBOL_out_of_class_special = 145,     /* out_of_class_special  */
  YYSYMBOL_146_10 = 146,                   /* $@10  */
  YYSYMBOL_147_11 = 147,                   /* $@11  */
  YYSYMBOL_access_specifier = 148,         /* access_specifier  */
  YYSYMBOL_init_declarator_list_opt = 149, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 150,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 151,          /* init_declarator  */
  YYSYMBOL_initializer = 152,              /* initializer  */
  YYSYMBOL_initializer_list = 153,         /* initializer_list  */
  YYSYMBOL_initializer_item = 154,         /* initializer_item  */
  YYSYMBOL_pointer = 155,                  /* pointer  */
  YYSYMBOL_declarator = 156,               /* declarator  */
  YYSYMBOL_abstract_declarator = 157,      /* abstract_declarator  */
  YYSYMBOL_direct_abstract_declarator = 158, /* direct_abstract_declarator  */
  YYSYMBOL_direct_declarator = 159,        /* direct_declarator  */
  YYSYMBOL_operator_function_id = 160,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 161,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 162,              /* param_scope  */
  YYSYMBOL_constructor_args = 163,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 164,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 165,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 166,           /* parameter_decl  */
  YYSYMBOL_function_definition = 167,      /* function_definition  */
  YYSYMBOL_168_12 = 168,                   /* $@12  */
  YYSYMBOL_statement = 169,                /* statement  */
  YYSYMBOL_compound_stmt = 170,            /* compound_stmt  */
  YYSYMBOL_171_13 = 171,                   /* $@13  */
  YYSYMBOL_block_item_list_opt = 172,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 173,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 174,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 175,           /* selection_stmt  */
  YYSYMBOL_176_14 = 176,                   /* $@14  */
  YYSYMBOL_labeled_stmt = 177,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 178,           /* iteration_stmt  */
  YYSYMBOL_for_open = 179,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 180,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 181,                /* jump_stmt  */
  YYSYMBOL_expr = 182,                     /* expr  */
  YYSYMBOL_assignment_expr = 183,          /* assignment_expr  */
  YYSYMBOL_assign_op = 184,                /* assign_op  */
  YYSYMBOL_constant_expr = 185,            /* constant_expr  */
  YYSYMBOL_binary_expr = 186,              /* binary_expr  */
  YYSYMBOL_unary_expr = 187,               /* unary_expr  */
  YYSYMBOL_type_name = 188,                /* type_name  */
  YYSYMBOL_type_name_specifiers = 189,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 190,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 191,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 192,             /* builtin_call  */
  YYSYMBOL_constructor_args_opt = 193,     /* constructor_args_opt  */
  YYSYMBOL_argument_list_opt = 194,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 195,            /* argument_list  */
  YYSYMBOL_argument = 196,                 /* argument  */
  YYSYMBOL_primary_expr = 197,             /* primary_expr  */
  YYSYMBOL_string_literal = 198            /* string_literal  */
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

#line 363 "build/parser.tab.cpp"

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
#define YYLAST   2139

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  116
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  83
/* YYNRULES -- Number of rules.  */
#define YYNRULES  335
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  595

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
     191,   204,   208,   209,   210,   211,   212,   213,   217,   218,
     219,   220,   221,   222,   223,   224,   225,   226,   227,   228,
     242,   249,   250,   254,   258,   254,   274,   274,   288,   294,
     300,   306,   312,   312,   323,   323,   333,   337,   333,   349,
     349,   363,   369,   378,   379,   386,   387,   391,   396,   404,
     405,   409,   410,   414,   415,   422,   428,   434,   440,   451,
     456,   468,   469,   470,   471,   480,   480,   498,   502,   510,
     514,   510,   534,   535,   536,   540,   541,   545,   546,   550,
     551,   555,   556,   557,   562,   570,   571,   575,   576,   579,
     585,   586,   587,   588,   589,   593,   599,   605,   606,   612,
     616,   625,   626,   627,   628,   632,   636,   643,   655,   664,
     668,   675,   682,   701,   708,   709,   714,   718,   718,   718,
     718,   719,   719,   719,   719,   720,   720,   720,   720,   721,
     721,   721,   721,   722,   722,   722,   722,   723,   723,   723,
     724,   724,   724,   725,   725,   725,   726,   726,   726,   727,
     727,   727,   734,   738,   739,   743,   744,   748,   752,   756,
     760,   765,   770,   778,   778,   843,   844,   845,   846,   847,
     848,   849,   850,   851,   855,   855,   864,   865,   869,   870,
     874,   875,   879,   882,   885,   885,   891,   894,   897,   905,
     908,   915,   919,   923,   926,   930,   939,   943,   944,   948,
     949,   950,   951,   952,   962,   963,   967,   968,   974,   975,
     976,   977,   978,   979,   980,   981,   982,   983,   984,   988,
     992,   993,   994,   995,   996,   997,   998,   999,  1000,  1001,
    1002,  1003,  1004,  1005,  1006,  1007,  1008,  1009,  1010,  1013,
    1017,  1018,  1019,  1020,  1021,  1022,  1023,  1024,  1025,  1026,
    1030,  1031,  1038,  1042,  1049,  1056,  1060,  1061,  1062,  1063,
    1064,  1065,  1066,  1067,  1068,  1069,  1070,  1071,  1072,  1081,
    1087,  1093,  1099,  1105,  1111,  1120,  1121,  1122,  1157,  1161,
    1169,  1175,  1179,  1180,  1181,  1182,  1186,  1187,  1188,  1189,
    1190,  1191,  1192,  1193,  1194,  1198,  1199,  1203,  1204,  1208,
    1209,  1213,  1214,  1221,  1230,  1231,  1232,  1233,  1234,  1235,
    1236,  1240,  1247,  1248,  1249,  1250,  1251,  1252,  1253,  1254,
    1255,  1256,  1257,  1264,  1272,  1273
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
  "CLASS", "ENUM", "PUBLIC", "PRIVATE", "PROTECTED", "THIS", "STATIC",
  "TYPEDEF", "AUTO", "CONST", "FRIEND", "VIRTUAL", "EXPLICIT", "IF",
  "ELSE", "FOR", "WHILE", "DO", "UNTIL", "SWITCH", "CASE", "DEFAULT",
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
  "tag_name", "struct_or_class_specifier", "$@1", "$@2", "@3", "$@4", "@5",
  "$@6", "$@7", "@8", "member_decl_list_opt", "enumerator_list",
  "enumerator", "comma_opt", "inheritance_opt",
  "inheritance_specifier_list", "inheritance_specifier",
  "member_decl_list", "member_item", "constructor_head", "$@9",
  "constructor_def", "out_of_class_special", "$@10", "$@11",
  "access_specifier", "init_declarator_list_opt", "init_declarator_list",
  "init_declarator", "initializer", "initializer_list", "initializer_item",
  "pointer", "declarator", "abstract_declarator",
  "direct_abstract_declarator", "direct_declarator",
  "operator_function_id", "overloadable_operator", "param_scope",
  "constructor_args", "parameter_list_opt", "parameter_list",
  "parameter_decl", "function_definition", "$@12", "statement",
  "compound_stmt", "$@13", "block_item_list_opt", "block_item_list",
  "expr_stmt", "selection_stmt", "$@14", "labeled_stmt", "iteration_stmt",
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

#define YYPACT_NINF (-415)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-188)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -415,  1877,  -415,    80,  -415,  -415,  -415,  -415,  -415,  -415,
    -415,  -415,  -415,   -32,   -18,    -4,  -415,  -415,  -415,  -415,
    -415,  -415,  -415,   -36,  -415,  -415,  1728,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,   -74,   -53,  -415,  -415,   -38,   -29,
    -415,  -415,   -74,   -53,  -415,  -415,    23,  1943,    26,    33,
    -415,  -415,   159,  -415,   -10,    -7,  -415,   138,   -28,    95,
    -415,  1930,    30,  1930,    32,    97,    41,    56,  -415,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,
    -415,    44,    50,  -415,    51,    53,    33,    93,  -415,   159,
    -415,  -415,  -415,    95,  1131,    82,  1745,   436,  -415,  -415,
    -415,   104,  -415,  -415,   108,  1930,  -415,   -68,  -415,   140,
    -415,  -415,   126,    38,   136,   191,   149,  -415,    97,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,   204,   185,
     186,   188,   190,   195,   196,   198,   199,   200,  -415,   211,
     212,   214,   215,   217,   225,   226,  1598,   227,   229,   230,
     233,  -415,   -44,  -415,  -415,  -415,  -415,  -415,  1665,  1665,
    1665,  1665,  1665,  1665,  1665,  1665,  1525,   983,  -415,  -415,
    1984,   308,   134,  -415,  -415,   280,   685,  1951,    89,  -415,
    -415,   235,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  1930,
    -415,  -415,  -415,   241,  -415,   151,  -415,  1665,    97,   245,
     149,  1951,  1665,  1665,  1665,  1665,  1665,  1665,  1665,  1665,
    1665,  1525,  1525,  1525,  1525,  1525,  1525,  1665,  1525,  -415,
    1525,  1525,  1525,  1665,   286,  1665,  -415,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,   185,   186,   188,   190,   195,   196,
     198,   199,   200,   157,   162,   169,  -415,   226,  -415,   -44,
     112,  -415,   250,  1505,  -415,   312,  1665,  -415,  -415,   -34,
    -415,  1665,  1665,  1665,  1665,  1665,  1665,  1665,  1665,  1665,
    1665,  1665,  1665,  1665,  1665,  1665,  1665,  1665,  1665,  1665,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,
    -415,  1665,   175,   315,  -415,  -415,   177,  1525,  1665,  -415,
     125,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,
     265,   267,   268,   909,   271,   272,  1665,   291,   269,   270,
     338,  1314,  -415,   307,   333,  -415,  -415,  1728,  -415,  -415,
     292,   797,  -415,  -415,  -415,  -415,  1241,  -415,     5,  1451,
     290,   294,  -415,  1665,  -415,  -415,  1951,   685,   298,    38,
    -415,  -415,  1930,  -415,  1984,  -415,  -415,  -415,   299,   297,
     301,   302,   304,   306,   317,   321,   322,   323,   324,   334,
    -415,  -415,   335,   309,  -415,   336,   339,   341,   342,   343,
     345,   346,   347,   348,   349,   350,  -415,   351,  -415,  -415,
    -415,  -415,  -415,  -415,  1665,  -415,  1665,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,    69,  -415,   504,
      -5,  -415,   360,  -415,   327,   300,  -415,  1057,    16,    16,
     232,   232,   332,   332,  2026,  1994,   -14,  2035,   588,  2042,
     232,   232,    91,    91,  -415,  -415,  -415,  -415,  -415,   358,
    -415,  -415,   389,   354,    10,  -415,  -415,  1665,  -415,  1665,
      27,  1665,  1665,   382,   909,  -415,  -415,   361,  -415,     7,
     909,  -415,  -415,  1387,  1387,  -415,    -8,  -415,  -415,  -415,
    1848,  -415,   356,   362,  -415,  -415,   363,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  -415,  1525,
    -415,  -415,  -415,  -415,  -415,  -415,   303,  -415,  -415,  -415,
    -415,  -415,  -415,  -415,   369,  -415,   357,   360,   572,  1131,
     402,  -415,  -415,  1665,   443,   444,  -415,  -415,   133,   137,
     392,   394,   139,   142,   909,  -415,  -415,  -415,  -415,  1665,
    1665,  -415,  -415,  -415,  -415,  -415,   391,  -415,  -415,  -415,
    -415,   390,  -415,  1131,  1984,  -415,  -415,   909,   909,  -415,
    1665,   909,  -415,  -415,   403,   393,   404,  -415,  -415,  -415,
     477,  -415,   144,  -415,   391,   909,   909,   909,    11,  -415,
    -415,  -415,  -415,  -415,  -415
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    18,    19,    20,    21,    22,    24,
      25,    26,    27,     0,     0,     0,    12,    14,    13,    15,
      16,    23,    28,    29,     3,     5,    85,    11,    17,    30,
       6,     4,     7,     8,    38,    39,    36,    33,    51,    52,
      49,    46,    40,    41,    44,    42,     0,     0,   115,    29,
     101,   100,     0,    10,     0,    86,    87,     0,    89,   106,
     119,    53,     0,    53,    61,     0,     0,     0,   148,   149,
     146,   147,   142,   143,   140,   141,   144,   145,   150,   151,
     152,   153,   154,   155,   156,   157,   158,   159,   137,   134,
     132,   133,   138,   139,   127,   128,   129,   130,   131,   136,
     135,     0,     0,   126,     0,     0,     0,     0,     9,     0,
     104,   103,   102,   105,     0,     0,   162,     0,    82,    83,
      84,     0,    29,    71,     0,    54,    69,     0,    74,     0,
      72,    34,     0,     0,     0,    57,    59,    55,     0,    79,
     161,   160,   116,   120,   117,   121,   118,    88,    89,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   319,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   313,     0,   314,   315,   316,   334,   318,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    90,    91,
     216,   249,   250,   295,   285,   317,     0,   165,     0,   163,
     124,     0,    75,    37,    70,    78,   184,    77,    73,    53,
      50,    67,    68,    62,    63,     0,    47,     0,    60,     0,
      59,   165,   305,   305,   305,   305,   305,   305,   305,   305,
     305,   307,   307,   307,   307,   307,   307,   305,     0,   260,
     307,   307,   307,   305,     0,   305,   251,   252,   253,   255,
     256,   254,   257,   258,   266,   267,   268,   269,   270,   272,
     273,   274,   275,     0,     0,     0,   277,   271,   276,   278,
       0,   214,     0,   262,   265,     0,     0,    92,    97,     0,
      95,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     219,   220,   221,   222,   223,   224,   225,   226,   227,   228,
     218,     0,     0,     0,   293,   294,     0,   307,     0,   335,
       0,    18,    19,    20,    21,    22,    24,    25,    26,    27,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    23,   313,    29,   190,   181,    85,   188,   175,
       0,     0,   176,   177,   180,   178,     0,   179,     0,   172,
       0,   166,   167,     0,   123,   125,   165,     0,     0,     0,
      65,    66,    53,    58,   229,   249,    56,    45,     0,     0,
     306,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     311,   312,     0,   308,   309,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   332,     0,   279,   280,
     283,   284,   281,   282,     0,   333,     0,   266,   267,   268,
     269,   270,   272,   273,   274,   275,   271,     0,   278,     0,
     107,   263,   109,   264,     0,     0,    93,     0,   241,   242,
     239,   240,   235,   236,   231,   230,     0,   232,   233,   234,
     237,   238,   243,   244,   245,   246,   247,   217,   291,     0,
     292,   288,     0,     0,     0,   182,   183,     0,   206,     0,
       0,     0,     0,     0,     0,   209,   210,     0,   211,     0,
       0,   174,   189,     0,     0,   191,   107,   170,   171,   122,
       0,   164,     0,     0,    35,    64,     0,    43,    80,   322,
     323,   324,   325,   326,   328,   329,   330,   331,   296,     0,
     297,   298,   299,   300,   301,   327,   261,   302,   303,   304,
     321,   320,   215,   259,     0,   111,     0,   108,     0,     0,
       0,    94,    96,     0,     0,     0,   287,   286,     0,     0,
       0,     0,     0,     0,     0,   197,   213,   212,   198,   207,
     207,   169,   168,    76,   185,    48,     0,   310,   110,   112,
     113,     0,    98,     0,   248,   290,   289,     0,     0,   202,
       0,     0,   194,   196,     0,   208,     0,    81,   114,    99,
     192,   199,     0,   203,     0,     0,     0,     0,     0,   195,
     205,   204,   193,   201,   200
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -415,  -415,  -415,    25,    -1,   -23,  -415,   251,  -415,  -415,
    -415,  -415,  -415,  -415,  -415,  -415,  -415,   -57,   378,   305,
     313,  -415,  -415,   150,  -415,   396,  -415,  -415,  -415,  -415,
    -415,  -415,  -125,  -415,  -415,   415,  -112,  -415,    88,  -264,
     -22,  -346,  -414,   -52,   183,  -415,  -415,   411,  -211,  -415,
      42,   527,  -415,  -326,  -126,  -415,   167,  -415,  -327,  -415,
    -415,  -415,  -415,  -415,   -15,  -415,  -175,   -96,  -415,  -261,
     -13,  -114,  -162,  -415,   263,  -415,  -415,   528,  -201,  -415,
      28,  -415,  -415
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    24,   346,   347,    27,    28,    37,    29,    62,
     209,    61,    66,    65,    64,   372,    63,   124,   136,   137,
     219,   134,   213,   214,   125,   126,   127,   366,   128,    30,
     221,   556,   129,    54,    55,    56,   278,   279,   280,    57,
     148,   431,   432,    59,    60,   103,   197,   380,   360,   361,
     362,   130,   115,   348,   349,   367,   350,   351,   352,   353,
     584,   354,   355,   356,   574,   357,   358,   271,   311,   373,
     190,   191,   391,   273,   274,   192,   193,   381,   392,   393,
     394,   194,   195
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      26,   207,   188,    53,    58,   113,   132,   470,   215,   430,
     379,   270,   593,   488,   110,   435,   527,   110,   189,   244,
     199,   201,    34,    35,   272,   482,    25,    46,   540,   484,
     107,   395,   396,   397,   398,   399,    38,    39,   -31,   402,
     403,   404,   205,    47,   206,   427,    48,   106,   427,   -31,
      42,    43,   239,   118,   119,   120,   541,   114,   -32,   -32,
      26,   245,    26,   270,   246,   247,   248,   249,   250,   251,
     252,   253,   527,   533,   -31,   473,   401,   436,    67,   437,
      36,   524,   111,   -32,  -173,   111,   123,   112,   123,   104,
     112,   189,   211,   212,    40,   486,   105,    52,   429,   414,
     108,   429,    47,   375,    47,   142,   109,   144,    44,   295,
     296,   297,   298,   299,   446,   485,   463,   547,   414,   133,
     414,   594,   427,   414,    26,   537,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   390,   390,   390,   390,   390,
     390,   199,   131,   464,   390,   390,   390,   199,   545,   199,
     123,   135,   368,   138,   548,   492,   549,   550,   140,    50,
     110,   139,   375,   430,    51,   141,   479,   375,   375,   375,
     375,   375,   375,   375,   375,   429,   375,   375,   375,   375,
     375,   375,   375,   375,   375,   375,   297,   298,   299,    47,
      32,    33,    48,   106,   196,   312,   359,   313,   314,   315,
     116,   117,   363,   364,   374,   370,   371,   146,    26,   202,
      47,   408,   409,    48,   106,   457,   410,   411,   573,   203,
     359,   390,   375,   412,   413,   414,   415,   208,   111,   458,
     459,   461,   462,   112,   123,   465,   466,   210,   316,   317,
     318,   580,   581,    52,   215,   583,   414,   567,   216,    50,
     414,   568,   414,   571,    51,   414,   572,   414,   588,   590,
     591,   592,   218,   374,    52,    41,    45,   491,   438,   439,
     440,   441,   442,   443,   444,   445,   217,   447,   448,   449,
     450,   451,   452,   453,   454,   455,   456,   143,   145,   114,
     222,   223,   538,   224,   539,   225,   542,   543,   281,   282,
     226,   227,   523,   228,   229,   230,   149,   150,   151,   152,
     153,   154,   155,   156,   157,   496,   231,   232,   522,   233,
     234,   158,   235,   374,    53,   295,   296,   297,   298,   299,
     236,   237,   240,   526,   241,   242,    53,   487,   243,   319,
     406,   189,   159,   160,   161,   162,   163,   164,   165,   166,
     365,   167,   168,   169,   369,   170,   377,   171,   172,   173,
     174,   175,   176,   177,   416,   359,   434,   178,   179,   460,
     467,    26,   468,   469,   575,   575,   471,   472,   474,   475,
     476,   483,   300,   301,   302,   303,   304,   305,   306,   307,
     308,   309,   477,   310,   480,   582,   244,   123,   281,   282,
     283,   284,   523,   481,   489,   184,   185,   490,   186,   494,
     497,   498,   529,   390,   363,   530,   499,   562,   500,   375,
     501,   534,   509,   293,   294,   295,   296,   297,   298,   299,
     577,   502,   561,   189,   113,   503,   504,   505,   506,   149,
     150,   151,   152,   153,   154,   155,   156,   157,   507,   508,
     510,   579,   535,   511,   158,   512,   513,   514,   589,   515,
     516,   517,   518,   519,   520,   521,   528,   189,   536,   544,
     553,   546,   559,   554,   555,   159,   160,   161,   162,   163,
     164,   165,   166,   558,   167,   168,   169,   563,   170,   359,
     171,   172,   173,   174,   175,   176,   177,   565,   566,   570,
     178,   179,   569,   206,   587,   578,   414,   149,   150,   151,
     152,   153,   154,   155,   156,   157,   220,   585,   586,   495,
     564,   204,   158,   376,   147,   532,   180,   198,    31,   181,
     182,   183,   552,   378,   493,   576,   433,   557,   184,   185,
       0,   186,     0,   159,   160,   161,   162,   163,   164,   165,
     166,   200,   167,   168,   169,     0,   170,     0,   171,   172,
     173,   174,   175,   176,   177,     0,     0,     0,   178,   179,
       0,     0,     0,     0,     0,   149,   150,   151,   152,   153,
     154,   155,   156,   157,     0,     0,     0,     0,     0,     0,
     158,     0,     0,     0,   180,     0,     0,   181,   182,   183,
       0,     0,     0,     0,     0,     0,   184,   185,     0,   186,
       0,   159,   160,   161,   162,   163,   164,   165,   166,   525,
     167,   168,   169,     0,   170,     0,   171,   172,   173,   174,
     175,   176,   177,     0,     0,     0,   178,   179,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   281,   282,   283,   284,   285,   286,
       0,     0,   180,     0,     0,   181,   182,   183,     0,     0,
       0,     0,     0,     0,   184,   185,     0,   186,   292,   293,
     294,   295,   296,   297,   298,   299,   320,   560,   321,   322,
     323,   324,   325,   326,   327,   328,   329,    13,    14,    15,
       0,     0,     0,   158,    16,    17,    18,    19,    20,     0,
       0,   330,     0,   331,   332,   333,   334,   335,   336,   337,
     338,   339,   340,   341,   159,   160,   161,   162,   163,   164,
     342,   166,    22,   167,   168,   169,     0,   170,     0,   343,
     344,   173,   174,   175,   176,   177,     0,     0,     0,   178,
     179,   382,   383,   384,   385,   386,   387,   388,   389,     0,
       0,     0,     0,     0,     0,   400,     0,     0,     0,     0,
       0,   405,     0,   407,     0,   180,     0,     0,   181,   182,
     183,     0,     0,     0,     0,     0,     0,   184,   185,     0,
     186,     0,     0,     0,     0,   345,  -186,   206,   320,     0,
     321,   322,   323,   324,   325,   326,   327,   328,   329,    13,
      14,    15,     0,     0,     0,   158,    16,    17,    18,    19,
      20,     0,     0,   330,     0,   331,   332,   333,   334,   335,
     336,   337,   338,   339,   340,   341,   159,   160,   161,   162,
     163,   164,   342,   166,    22,   167,   168,   169,     0,   170,
       0,   343,   344,   173,   174,   175,   176,   177,     0,     0,
       0,   178,   179,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   180,     0,     0,
     181,   182,   183,     0,     0,     0,     0,     0,     0,   184,
     185,     0,   186,     0,     0,     0,     0,   345,  -187,   206,
     320,     0,   321,   322,   323,   324,   325,   326,   327,   328,
     329,    13,    14,    15,     0,     0,     0,   158,    16,    17,
      18,    19,    20,     0,     0,   330,     0,   331,   332,   333,
     334,   335,   336,   337,   338,   339,   340,   341,   159,   160,
     161,   162,   163,   164,   342,   166,    22,   167,   168,   169,
       0,   170,     0,   343,   344,   173,   174,   175,   176,   177,
       0,     0,     0,   178,   179,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   149,   150,   151,   152,
     153,   154,   155,   156,   157,     0,     0,     0,     0,   180,
       0,   158,   181,   182,   183,     0,     0,     0,     0,     0,
       0,   184,   185,     0,   186,     0,     0,     0,     0,   345,
       0,   206,   159,   160,   161,   162,   163,   164,   165,   166,
       0,   167,   168,   169,     0,   170,     0,   171,   172,   173,
     174,   175,   176,   177,     0,     0,     0,   178,   179,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     149,   150,   151,   152,   153,   154,   155,   156,   157,     0,
       0,     0,     0,   180,     0,   158,   181,   182,   183,     0,
       0,     0,     0,     0,     0,   184,   185,   275,   186,   276,
       0,     0,     0,     0,   277,   187,   159,   160,   161,   162,
     163,   164,   165,   166,     0,   167,   168,   169,     0,   170,
       0,   171,   172,   173,   174,   175,   176,   177,     0,     0,
       0,   178,   179,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   149,   150,   151,   152,   153,   154,
     155,   156,   157,     0,     0,     0,     0,   180,     0,   158,
     181,   182,   183,     0,     0,     0,     0,     0,     0,   184,
     185,   275,   186,   276,     0,     0,     0,     0,   531,   187,
     159,   160,   161,   162,   163,   164,   165,   166,     0,   167,
     168,   169,     0,   170,     0,   171,   172,   173,   174,   175,
     176,   177,     0,     0,     0,   178,   179,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   180,     0,     0,   181,   182,   183,     0,     0,     0,
       0,     0,     0,   184,   185,     0,   186,     0,     0,     0,
       0,     0,     0,   187,   321,   322,   323,   324,   325,   326,
     327,   328,   329,    13,    14,    15,     0,     0,     0,   158,
      16,    17,    18,    19,    20,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     159,   160,   161,   162,   163,   164,   342,   166,    22,   167,
     168,   169,     0,   170,     0,   171,   344,   173,   174,   175,
     176,   177,     0,     0,     0,   178,   179,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   149,   150,   151,
     152,   153,   154,   155,   156,   157,     0,     0,     0,     0,
       0,   180,   158,     0,   181,   182,   183,     0,     0,     0,
       0,     0,     0,   184,   185,     0,   186,     0,     0,     0,
       0,   345,     0,   159,   160,   161,   162,   163,   164,   165,
     166,     0,   167,   168,   169,     0,   170,     0,   171,   172,
     173,   174,   175,   176,   177,     0,     0,     0,   178,   179,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     149,   150,   151,   152,   153,   154,   155,   156,   157,     0,
       0,     0,     0,     0,   180,   158,     0,   181,   182,   183,
       0,     0,     0,     0,     0,     0,   184,   185,     0,   186,
       0,     0,     0,     0,   478,     0,   159,   160,   161,   162,
     163,   164,   165,   166,     0,   167,   168,   169,     0,   170,
       0,   171,   172,   173,   174,   175,   176,   177,     0,     0,
       0,   178,   179,     0,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,     0,     0,     0,     0,
      16,    17,    18,    19,    20,     0,     0,   180,     0,     0,
     181,   182,   183,     0,     0,     0,     0,     0,     0,   184,
     185,     0,   186,     0,     0,     0,    21,   345,    22,     0,
       0,     0,    47,     0,   427,    48,    49,     0,   417,   418,
     419,   420,   421,   422,   423,   424,   425,   263,   264,   265,
       0,     0,     0,     0,     0,     0,     0,   266,   254,   255,
     256,   257,   258,   259,   260,   261,   262,   263,   264,   265,
       0,    50,     0,   158,     0,     0,    51,   266,     0,     0,
     426,     0,   268,     0,     0,     0,    52,   429,   427,     0,
     428,     0,     0,     0,   159,   160,   161,   162,   163,   164,
     267,   166,   268,   167,   168,   169,     0,   170,     0,   171,
     269,   173,   174,   175,   176,   177,     0,     0,     0,   178,
     179,     0,     0,     0,     0,    50,     0,     0,     0,     0,
      51,   149,   150,   151,   152,   153,   154,   155,   156,   157,
       0,   429,     0,     0,     0,   180,   158,     0,   181,   182,
     183,     0,     0,     0,     0,     0,     0,   184,   185,     0,
     186,     0,     0,     0,     0,     0,     0,   159,   160,   161,
     162,   163,   164,   165,   166,     0,   167,   168,   169,     0,
     170,     0,   171,   172,   173,   174,   175,   176,   177,     0,
       0,     0,   178,   179,     0,     0,     0,     0,   149,   150,
     151,   152,   153,   154,   155,   156,   157,     0,     0,     0,
       0,     0,     0,   158,     0,     0,     0,     0,   180,     0,
       0,   181,   182,   183,     0,     0,     0,     0,     0,     0,
     184,   185,     0,   238,   159,   160,   161,   162,   163,   164,
     165,   166,     0,   167,   168,   169,     0,   170,     0,   171,
     172,   173,   174,   175,   176,   177,     0,     0,     0,   178,
     179,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,     0,     0,     0,     0,    16,    17,    18,
      19,    20,     0,     0,     0,   180,     0,     0,   181,   182,
     183,     0,     0,   158,     0,     0,     0,   184,   185,     0,
     186,     0,     0,    21,     0,    22,     0,     0,     0,    47,
       0,     0,    48,    49,   159,   160,   161,   162,   163,   164,
       0,   166,     0,   167,   168,   169,     0,   170,     0,   171,
       0,   173,   174,   175,   176,   177,     0,     0,     0,   178,
     179,     0,     0,     0,     0,     0,     0,     0,    50,     0,
       0,     0,     0,    51,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    52,     0,   180,     0,     0,   181,   182,
     183,     0,     0,     0,     0,     0,     0,   184,   185,     0,
     186,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,     0,     0,     0,     0,    16,    17,    18,
      19,    20,     0,     0,     0,     0,     0,     2,     3,     0,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,     0,    21,     0,    22,    16,    17,    18,    19,
      20,     0,     0,   122,     0,     0,     0,     0,     0,     0,
     551,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    21,     0,    22,     0,     0,     0,     0,     0,
       0,     0,    23,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,   118,   119,   120,     0,    16,
      17,    18,    19,    20,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,     0,     0,     0,     0,
      16,    17,    18,    19,    20,    21,     0,    22,     0,     0,
       0,     0,     0,     0,   121,   122,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    21,     0,    22,     0,
       0,     0,     0,     0,     0,     0,   122,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    87,     0,    88,     0,
       0,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,     0,     0,     0,     0,    99,   100,     0,   101,   102,
     281,   282,   283,   284,   285,   286,   287,   288,     0,     0,
     281,   282,   283,   284,   285,   286,   287,     0,     0,     0,
     289,     0,   290,   291,   292,   293,   294,   295,   296,   297,
     298,   299,   290,   291,   292,   293,   294,   295,   296,   297,
     298,   299,   281,   282,   283,   284,   285,   286,     0,     0,
       0,   281,   282,   283,   284,   285,   286,     0,   281,   282,
     283,   284,   285,   286,   290,   291,   292,   293,   294,   295,
     296,   297,   298,   299,   291,   292,   293,   294,   295,   296,
     297,   298,   299,   293,   294,   295,   296,   297,   298,   299
};

static const yytype_int16 yycheck[] =
{
       1,   127,   114,    26,    26,    57,    63,   333,   133,   273,
     221,   186,     1,   359,    22,   276,   430,    22,   114,    63,
     116,   117,    54,    55,   186,   351,     1,    63,     1,   356,
      52,   232,   233,   234,   235,   236,    54,    55,   112,   240,
     241,   242,   110,    51,   112,    53,    54,    55,    53,    87,
      54,    55,   166,    15,    16,    17,    29,    85,    87,   112,
      61,   105,    63,   238,   178,   179,   180,   181,   182,   183,
     184,   185,   486,    87,   112,   336,   238,   111,    55,   113,
     112,   427,    90,   112,   112,    90,    61,    95,    63,    63,
      95,   187,    54,    55,   112,   359,    63,   105,   106,   113,
     110,   106,    51,   217,    51,    54,   113,    54,   112,    93,
      94,    95,    96,    97,   289,   110,   317,   110,   113,    87,
     113,   110,    53,   113,   125,   115,   222,   223,   224,   225,
     226,   227,   228,   229,   230,   231,   232,   233,   234,   235,
     236,   237,   112,   318,   240,   241,   242,   243,   474,   245,
     125,    54,   209,   112,   480,   366,   483,   484,   114,    90,
      22,   105,   276,   427,    95,   115,   341,   281,   282,   283,
     284,   285,   286,   287,   288,   106,   290,   291,   292,   293,
     294,   295,   296,   297,   298,   299,    95,    96,    97,    51,
     110,   111,    54,    55,   112,    61,   197,    63,    64,    65,
     105,   106,   113,   114,   217,    54,    55,   114,   209,   105,
      51,    54,    55,    54,    55,   311,    54,    55,   544,   111,
     221,   317,   336,    54,    55,   113,   114,    87,    90,    54,
      55,    54,    55,    95,   209,   110,   111,   111,   104,   105,
     106,   567,   568,   105,   369,   571,   113,   114,   112,    90,
     113,   114,   113,   114,    95,   113,   114,   113,   114,   585,
     586,   587,   113,   276,   105,    14,    15,   363,   281,   282,
     283,   284,   285,   286,   287,   288,    85,   290,   291,   292,
     293,   294,   295,   296,   297,   298,   299,   104,   105,    85,
     105,   105,   467,   105,   469,   105,   471,   472,    66,    67,
     105,   105,   416,   105,   105,   105,     3,     4,     5,     6,
       7,     8,     9,    10,    11,   372,   105,   105,   414,   105,
     105,    18,   105,   336,   347,    93,    94,    95,    96,    97,
     105,   105,   105,   429,   105,   105,   359,   359,   105,    59,
      54,   437,    39,    40,    41,    42,    43,    44,    45,    46,
     115,    48,    49,    50,   113,    52,   111,    54,    55,    56,
      57,    58,    59,    60,   114,   366,    54,    64,    65,    54,
     105,   372,   105,   105,   549,   550,   105,   105,    87,   110,
     110,   356,    74,    75,    76,    77,    78,    79,    80,    81,
      82,    83,    54,    85,    87,   570,    63,   372,    66,    67,
      68,    69,   516,   111,   114,   102,   103,   113,   105,   111,
     111,   114,    85,   509,   113,   115,   114,   529,   114,   533,
     114,    63,   113,    91,    92,    93,    94,    95,    96,    97,
     556,   114,   528,   529,   486,   114,   114,   114,   114,     3,
       4,     5,     6,     7,     8,     9,    10,    11,   114,   114,
     114,   563,    63,   114,    18,   114,   114,   114,   584,   114,
     114,   114,   114,   114,   114,   114,   106,   563,   114,    87,
     114,   110,   115,   111,   111,    39,    40,    41,    42,    43,
      44,    45,    46,   114,    48,    49,    50,    85,    52,   490,
      54,    55,    56,    57,    58,    59,    60,    54,    54,   105,
      64,    65,   110,   112,    27,   115,   113,     3,     4,     5,
       6,     7,     8,     9,    10,    11,   138,   114,   114,   369,
     533,   125,    18,   218,   109,   437,    90,   116,     1,    93,
      94,    95,   490,   220,   367,   550,   273,   509,   102,   103,
      -1,   105,    -1,    39,    40,    41,    42,    43,    44,    45,
      46,   115,    48,    49,    50,    -1,    52,    -1,    54,    55,
      56,    57,    58,    59,    60,    -1,    -1,    -1,    64,    65,
      -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,
      18,    -1,    -1,    -1,    90,    -1,    -1,    93,    94,    95,
      -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,
      -1,    39,    40,    41,    42,    43,    44,    45,    46,   115,
      48,    49,    50,    -1,    52,    -1,    54,    55,    56,    57,
      58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    67,    68,    69,    70,    71,
      -1,    -1,    90,    -1,    -1,    93,    94,    95,    -1,    -1,
      -1,    -1,    -1,    -1,   102,   103,    -1,   105,    90,    91,
      92,    93,    94,    95,    96,    97,     1,   115,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      -1,    -1,    -1,    18,    19,    20,    21,    22,    23,    -1,
      -1,    26,    -1,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    -1,    52,    -1,    54,
      55,    56,    57,    58,    59,    60,    -1,    -1,    -1,    64,
      65,   223,   224,   225,   226,   227,   228,   229,   230,    -1,
      -1,    -1,    -1,    -1,    -1,   237,    -1,    -1,    -1,    -1,
      -1,   243,    -1,   245,    -1,    90,    -1,    -1,    93,    94,
      95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,
     105,    -1,    -1,    -1,    -1,   110,   111,   112,     1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    -1,    -1,    -1,    18,    19,    20,    21,    22,
      23,    -1,    -1,    26,    -1,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    -1,    52,
      -1,    54,    55,    56,    57,    58,    59,    60,    -1,    -1,
      -1,    64,    65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    -1,    -1,
      93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,   102,
     103,    -1,   105,    -1,    -1,    -1,    -1,   110,   111,   112,
       1,    -1,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    -1,    -1,    -1,    18,    19,    20,
      21,    22,    23,    -1,    -1,    26,    -1,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,    40,
      41,    42,    43,    44,    45,    46,    47,    48,    49,    50,
      -1,    52,    -1,    54,    55,    56,    57,    58,    59,    60,
      -1,    -1,    -1,    64,    65,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,    90,
      -1,    18,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,
      -1,   102,   103,    -1,   105,    -1,    -1,    -1,    -1,   110,
      -1,   112,    39,    40,    41,    42,    43,    44,    45,    46,
      -1,    48,    49,    50,    -1,    52,    -1,    54,    55,    56,
      57,    58,    59,    60,    -1,    -1,    -1,    64,    65,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    90,    -1,    18,    93,    94,    95,    -1,
      -1,    -1,    -1,    -1,    -1,   102,   103,   104,   105,   106,
      -1,    -1,    -1,    -1,   111,   112,    39,    40,    41,    42,
      43,    44,    45,    46,    -1,    48,    49,    50,    -1,    52,
      -1,    54,    55,    56,    57,    58,    59,    60,    -1,    -1,
      -1,    64,    65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    90,    -1,    18,
      93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,   102,
     103,   104,   105,   106,    -1,    -1,    -1,    -1,   111,   112,
      39,    40,    41,    42,    43,    44,    45,    46,    -1,    48,
      49,    50,    -1,    52,    -1,    54,    55,    56,    57,    58,
      59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    -1,    -1,    93,    94,    95,    -1,    -1,    -1,
      -1,    -1,    -1,   102,   103,    -1,   105,    -1,    -1,    -1,
      -1,    -1,    -1,   112,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    -1,    -1,    -1,    18,
      19,    20,    21,    22,    23,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      39,    40,    41,    42,    43,    44,    45,    46,    47,    48,
      49,    50,    -1,    52,    -1,    54,    55,    56,    57,    58,
      59,    60,    -1,    -1,    -1,    64,    65,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    90,    18,    -1,    93,    94,    95,    -1,    -1,    -1,
      -1,    -1,    -1,   102,   103,    -1,   105,    -1,    -1,    -1,
      -1,   110,    -1,    39,    40,    41,    42,    43,    44,    45,
      46,    -1,    48,    49,    50,    -1,    52,    -1,    54,    55,
      56,    57,    58,    59,    60,    -1,    -1,    -1,    64,    65,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    90,    18,    -1,    93,    94,    95,
      -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,
      -1,    -1,    -1,    -1,   110,    -1,    39,    40,    41,    42,
      43,    44,    45,    46,    -1,    48,    49,    50,    -1,    52,
      -1,    54,    55,    56,    57,    58,    59,    60,    -1,    -1,
      -1,    64,    65,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    -1,    -1,    -1,    -1,
      19,    20,    21,    22,    23,    -1,    -1,    90,    -1,    -1,
      93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,   102,
     103,    -1,   105,    -1,    -1,    -1,    45,   110,    47,    -1,
      -1,    -1,    51,    -1,    53,    54,    55,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    22,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      -1,    90,    -1,    18,    -1,    -1,    95,    22,    -1,    -1,
      45,    -1,    47,    -1,    -1,    -1,   105,   106,    53,    -1,
      55,    -1,    -1,    -1,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    -1,    52,    -1,    54,
      55,    56,    57,    58,    59,    60,    -1,    -1,    -1,    64,
      65,    -1,    -1,    -1,    -1,    90,    -1,    -1,    -1,    -1,
      95,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      -1,   106,    -1,    -1,    -1,    90,    18,    -1,    93,    94,
      95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,
     105,    -1,    -1,    -1,    -1,    -1,    -1,    39,    40,    41,
      42,    43,    44,    45,    46,    -1,    48,    49,    50,    -1,
      52,    -1,    54,    55,    56,    57,    58,    59,    60,    -1,
      -1,    -1,    64,    65,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    -1,    -1,    -1,
      -1,    -1,    -1,    18,    -1,    -1,    -1,    -1,    90,    -1,
      -1,    93,    94,    95,    -1,    -1,    -1,    -1,    -1,    -1,
     102,   103,    -1,   105,    39,    40,    41,    42,    43,    44,
      45,    46,    -1,    48,    49,    50,    -1,    52,    -1,    54,
      55,    56,    57,    58,    59,    60,    -1,    -1,    -1,    64,
      65,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    -1,    -1,    -1,    -1,    19,    20,    21,
      22,    23,    -1,    -1,    -1,    90,    -1,    -1,    93,    94,
      95,    -1,    -1,    18,    -1,    -1,    -1,   102,   103,    -1,
     105,    -1,    -1,    45,    -1,    47,    -1,    -1,    -1,    51,
      -1,    -1,    54,    55,    39,    40,    41,    42,    43,    44,
      -1,    46,    -1,    48,    49,    50,    -1,    52,    -1,    54,
      -1,    56,    57,    58,    59,    60,    -1,    -1,    -1,    64,
      65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    -1,
      -1,    -1,    -1,    95,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   105,    -1,    90,    -1,    -1,    93,    94,
      95,    -1,    -1,    -1,    -1,    -1,    -1,   102,   103,    -1,
     105,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    -1,    -1,    -1,    -1,    19,    20,    21,
      22,    23,    -1,    -1,    -1,    -1,    -1,     0,     1,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    -1,    45,    -1,    47,    19,    20,    21,    22,
      23,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,    -1,
      62,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    47,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    55,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    19,
      20,    21,    22,    23,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    -1,    -1,    -1,    -1,
      19,    20,    21,    22,    23,    45,    -1,    47,    -1,    -1,
      -1,    -1,    -1,    -1,    54,    55,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    47,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    55,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,    75,    76,
      77,    78,    79,    80,    81,    82,    83,    -1,    85,    -1,
      -1,    88,    89,    90,    91,    92,    93,    94,    95,    96,
      97,    -1,    -1,    -1,    -1,   102,   103,    -1,   105,   106,
      66,    67,    68,    69,    70,    71,    72,    73,    -1,    -1,
      66,    67,    68,    69,    70,    71,    72,    -1,    -1,    -1,
      86,    -1,    88,    89,    90,    91,    92,    93,    94,    95,
      96,    97,    88,    89,    90,    91,    92,    93,    94,    95,
      96,    97,    66,    67,    68,    69,    70,    71,    -1,    -1,
      -1,    66,    67,    68,    69,    70,    71,    -1,    66,    67,
      68,    69,    70,    71,    88,    89,    90,    91,    92,    93,
      94,    95,    96,    97,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    91,    92,    93,    94,    95,    96,    97
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   117,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    19,    20,    21,    22,
      23,    45,    47,    55,   118,   119,   120,   121,   122,   124,
     145,   167,   110,   111,    54,    55,   112,   123,    54,    55,
     112,   123,    54,    55,   112,   123,    63,    51,    54,    55,
      90,    95,   105,   121,   149,   150,   151,   155,   156,   159,
     160,   127,   125,   132,   130,   129,   128,    55,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,    82,    83,    85,    88,
      89,    90,    91,    92,    93,    94,    95,    96,    97,   102,
     103,   105,   106,   161,    63,    63,    55,   156,   110,   113,
      22,    90,    95,   159,    85,   168,   105,   106,    15,    16,
      17,    54,    55,   119,   133,   140,   141,   142,   144,   148,
     167,   112,   133,    87,   137,    54,   134,   135,   112,   105,
     114,   115,    54,   160,    54,   160,   114,   151,   156,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    18,    39,
      40,    41,    42,    43,    44,    45,    46,    48,    49,    50,
      52,    54,    55,    56,    57,    58,    59,    60,    64,    65,
      90,    93,    94,    95,   102,   103,   105,   112,   152,   183,
     186,   187,   191,   192,   197,   198,   112,   162,   163,   183,
     115,   183,   105,   111,   141,   110,   112,   170,    87,   126,
     111,    54,    55,   138,   139,   148,   112,    85,   113,   136,
     134,   146,   105,   105,   105,   105,   105,   105,   105,   105,
     105,   105,   105,   105,   105,   105,   105,   105,   105,   187,
     105,   105,   105,   105,    63,   105,   187,   187,   187,   187,
     187,   187,   187,   187,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    22,    45,    47,    55,
     182,   183,   188,   189,   190,   104,   106,   111,   152,   153,
     154,    66,    67,    68,    69,    70,    71,    72,    73,    86,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      74,    75,    76,    77,    78,    79,    80,    81,    82,    83,
      85,   184,    61,    63,    64,    65,   104,   105,   106,    59,
       1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      26,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    45,    54,    55,   110,   119,   120,   169,   170,
     172,   173,   174,   175,   177,   178,   179,   181,   182,   120,
     164,   165,   166,   113,   114,   115,   143,   171,   133,   113,
      54,    55,   131,   185,   186,   187,   135,   111,   136,   164,
     163,   193,   193,   193,   193,   193,   193,   193,   193,   193,
     183,   188,   194,   195,   196,   194,   194,   194,   194,   194,
     193,   188,   194,   194,   194,   193,    54,   193,    54,    55,
      54,    55,    54,    55,   113,   114,   114,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    45,    53,    55,   106,
     155,   157,   158,   190,    54,   185,   111,   113,   186,   186,
     186,   186,   186,   186,   186,   186,   182,   186,   186,   186,
     186,   186,   186,   186,   186,   186,   186,   183,    54,    55,
      54,    54,    55,   194,   182,   110,   111,   105,   105,   105,
     169,   105,   105,   185,    87,   110,   110,    54,   110,   182,
      87,   111,   169,   119,   174,   110,   155,   156,   157,   114,
     113,   183,   164,   172,   111,   139,   133,   111,   114,   114,
     114,   114,   114,   114,   114,   114,   114,   114,   114,   113,
     114,   114,   114,   114,   114,   114,   114,   114,   114,   114,
     114,   114,   183,   187,   157,   115,   183,   158,   106,    85,
     115,   111,   154,    87,    63,    63,   114,   115,   182,   182,
       1,    29,   182,   182,    87,   169,   110,   110,   169,   174,
     174,    62,   166,   114,   111,   111,   147,   196,   114,   115,
     115,   183,   152,    85,   186,    54,    54,   114,   114,   110,
     105,   114,   114,   169,   180,   182,   180,   170,   115,   152,
     169,   169,   182,   169,   176,   114,   114,    27,   114,   170,
     169,   169,   169,     1,   110
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   116,   117,   117,   118,   118,   118,   118,   118,   119,
     120,   120,   121,   121,   121,   121,   121,   121,   122,   122,
     122,   122,   122,   122,   122,   122,   122,   122,   122,   122,
     122,   123,   123,   125,   126,   124,   127,   124,   124,   124,
     124,   124,   128,   124,   129,   124,   130,   131,   124,   132,
     124,   124,   124,   133,   133,   134,   134,   135,   135,   136,
     136,   137,   137,   138,   138,   139,   139,   139,   139,   140,
     140,   141,   141,   141,   141,   143,   142,   144,   144,   146,
     147,   145,   148,   148,   148,   149,   149,   150,   150,   151,
     151,   152,   152,   152,   152,   153,   153,   154,   154,   154,
     155,   155,   155,   155,   155,   156,   156,   157,   157,   157,
     158,   158,   158,   158,   158,   159,   159,   159,   159,   159,
     159,   159,   159,   159,   159,   159,   160,   161,   161,   161,
     161,   161,   161,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   161,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   161,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   162,   163,   163,   164,   164,   165,   165,   165,
     166,   166,   166,   168,   167,   169,   169,   169,   169,   169,
     169,   169,   169,   169,   171,   170,   172,   172,   173,   173,
     174,   174,   175,   175,   176,   175,   177,   177,   177,   178,
     178,   178,   178,   178,   178,   178,   179,   180,   180,   181,
     181,   181,   181,   181,   182,   182,   183,   183,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   185,
     186,   186,   186,   186,   186,   186,   186,   186,   186,   186,
     186,   186,   186,   186,   186,   186,   186,   186,   186,   186,
     187,   187,   187,   187,   187,   187,   187,   187,   187,   187,
     187,   187,   188,   188,   189,   189,   190,   190,   190,   190,
     190,   190,   190,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   190,   190,   190,   191,   191,   191,   191,   191,
     191,   191,   191,   191,   191,   191,   192,   192,   192,   192,
     192,   192,   192,   192,   192,   193,   193,   194,   194,   195,
     195,   196,   196,   197,   197,   197,   197,   197,   197,   197,
     197,   197,   197,   197,   197,   197,   197,   197,   197,   197,
     197,   197,   197,   197,   198,   198
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     0,     0,     7,     0,     5,     2,     2,
       2,     2,     0,     7,     0,     6,     0,     0,     8,     0,
       5,     2,     2,     0,     1,     1,     3,     1,     3,     0,
       1,     0,     2,     1,     3,     2,     2,     1,     1,     1,
       2,     1,     1,     2,     1,     0,     5,     2,     2,     0,
       0,     9,     1,     1,     1,     0,     1,     1,     3,     1,
       3,     1,     2,     3,     4,     1,     3,     1,     4,     5,
       1,     1,     2,     2,     2,     2,     1,     1,     2,     1,
       3,     2,     3,     3,     4,     1,     3,     3,     3,     1,
       3,     3,     5,     4,     3,     4,     2,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       2,     2,     0,     1,     3,     0,     1,     1,     3,     3,
       2,     2,     1,     0,     6,     1,     1,     1,     1,     1,
       1,     1,     2,     2,     0,     4,     0,     1,     1,     2,
       1,     2,     5,     7,     0,     6,     4,     3,     3,     5,
       7,     7,     4,     5,     6,     6,     2,     0,     1,     2,
       2,     2,     3,     3,     1,     3,     1,     3,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     5,     1,
       1,     2,     2,     2,     2,     2,     2,     2,     2,     4,
       2,     4,     1,     2,     2,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     2,
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
#line 140 "src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2457 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 144 "src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2467 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 152 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2473 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 153 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2479 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 154 "src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2485 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 155 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2491 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 156 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2497 "build/parser.tab.cpp"
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
#line 2530 "build/parser.tab.cpp"
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
#line 2548 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 204 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2554 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 208 "src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2560 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: AUTO  */
#line 209 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2566 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: TYPEDEF  */
#line 210 "src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2572 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: CONST  */
#line 211 "src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2578 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: FRIEND  */
#line 212 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isFriend = true; }
#line 2584 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: type_specifier  */
#line 213 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2590 "build/parser.tab.cpp"
    break;

  case 18: /* type_specifier: INT  */
#line 217 "src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2596 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: CHAR  */
#line 218 "src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2602 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: FLOAT  */
#line 219 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2608 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: DOUBLE  */
#line 220 "src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2614 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: VOID  */
#line 221 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2620 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: BOOL  */
#line 222 "src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2626 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: SHORT  */
#line 223 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2632 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: LONG  */
#line 224 "src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2638 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SIGNED  */
#line 225 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2644 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: UNSIGNED  */
#line 226 "src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2650 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: VA_LIST  */
#line 227 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); g_afterTypeKeyword = true; }
#line 2656 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: TYPE_NAME  */
#line 228 "src/parser.y"
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
#line 2675 "build/parser.tab.cpp"
    break;

  case 30: /* type_specifier: struct_or_class_specifier  */
#line 242 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2681 "build/parser.tab.cpp"
    break;

  case 31: /* tag_name: IDENTIFIER  */
#line 249 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2687 "build/parser.tab.cpp"
    break;

  case 32: /* tag_name: TYPE_NAME  */
#line 250 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2693 "build/parser.tab.cpp"
    break;

  case 33: /* $@1: %empty  */
#line 254 "src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2703 "build/parser.tab.cpp"
    break;

  case 34: /* $@2: %empty  */
#line 258 "src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2709 "build/parser.tab.cpp"
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
#line 2727 "build/parser.tab.cpp"
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
#line 2739 "build/parser.tab.cpp"
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
#line 2752 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 288 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2763 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 294 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2774 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: ENUM IDENTIFIER  */
#line 300 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2785 "build/parser.tab.cpp"
    break;

  case 41: /* struct_or_class_specifier: ENUM TYPE_NAME  */
#line 306 "src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2796 "build/parser.tab.cpp"
    break;

  case 42: /* $@4: %empty  */
#line 312 "src/parser.y"
                    {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM");
      }
#line 2805 "build/parser.tab.cpp"
    break;

  case 43: /* struct_or_class_specifier: ENUM tag_name $@4 '{' enumerator_list comma_opt '}'  */
#line 315 "src/parser.y"
                                          {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2818 "build/parser.tab.cpp"
    break;

  case 44: /* @5: %empty  */
#line 323 "src/parser.y"
               {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[-1].idx});
      }
#line 2827 "build/parser.tab.cpp"
    break;

  case 45: /* struct_or_class_specifier: ENUM '{' @5 enumerator_list comma_opt '}'  */
#line 326 "src/parser.y"
                                      {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-3].str;
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-3].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2839 "build/parser.tab.cpp"
    break;

  case 46: /* $@6: %empty  */
#line 333 "src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2849 "build/parser.tab.cpp"
    break;

  case 47: /* $@7: %empty  */
#line 337 "src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2855 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: CLASS tag_name $@6 inheritance_opt '{' $@7 member_decl_list_opt '}'  */
#line 337 "src/parser.y"
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
#line 2872 "build/parser.tab.cpp"
    break;

  case 49: /* @8: %empty  */
#line 349 "src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2884 "build/parser.tab.cpp"
    break;

  case 50: /* struct_or_class_specifier: CLASS '{' @8 member_decl_list_opt '}'  */
#line 355 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2897 "build/parser.tab.cpp"
    break;

  case 51: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 363 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2908 "build/parser.tab.cpp"
    break;

  case 52: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 369 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2919 "build/parser.tab.cpp"
    break;

  case 53: /* member_decl_list_opt: %empty  */
#line 378 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2925 "build/parser.tab.cpp"
    break;

  case 54: /* member_decl_list_opt: member_decl_list  */
#line 379 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2931 "build/parser.tab.cpp"
    break;

  case 55: /* enumerator_list: enumerator  */
#line 386 "src/parser.y"
                 { yyval.nodeList.push_back(yyvsp[0].node); }
#line 2937 "build/parser.tab.cpp"
    break;

  case 56: /* enumerator_list: enumerator_list ',' enumerator  */
#line 387 "src/parser.y"
                                     { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 2943 "build/parser.tab.cpp"
    break;

  case 57: /* enumerator: IDENTIFIER  */
#line 391 "src/parser.y"
                 {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[0].str), yyvsp[0].idx);
      }
#line 2953 "build/parser.tab.cpp"
    break;

  case 58: /* enumerator: IDENTIFIER '=' constant_expr  */
#line 396 "src/parser.y"
                                   {
          declareSymbol(yyvsp[-2].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 2963 "build/parser.tab.cpp"
    break;

  case 59: /* comma_opt: %empty  */
#line 404 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2969 "build/parser.tab.cpp"
    break;

  case 60: /* comma_opt: ','  */
#line 405 "src/parser.y"
          { yyval = ParserValue(); }
#line 2975 "build/parser.tab.cpp"
    break;

  case 61: /* inheritance_opt: %empty  */
#line 409 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2981 "build/parser.tab.cpp"
    break;

  case 62: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 410 "src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 2987 "build/parser.tab.cpp"
    break;

  case 63: /* inheritance_specifier_list: inheritance_specifier  */
#line 414 "src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2993 "build/parser.tab.cpp"
    break;

  case 64: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 415 "src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 3002 "build/parser.tab.cpp"
    break;

  case 65: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 422 "src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3013 "build/parser.tab.cpp"
    break;

  case 66: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 428 "src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 3024 "build/parser.tab.cpp"
    break;

  case 67: /* inheritance_specifier: IDENTIFIER  */
#line 434 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3035 "build/parser.tab.cpp"
    break;

  case 68: /* inheritance_specifier: TYPE_NAME  */
#line 440 "src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3046 "build/parser.tab.cpp"
    break;

  case 69: /* member_decl_list: member_item  */
#line 451 "src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 3056 "build/parser.tab.cpp"
    break;

  case 70: /* member_decl_list: member_decl_list member_item  */
#line 456 "src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 3070 "build/parser.tab.cpp"
    break;

  case 71: /* member_item: declaration  */
#line 468 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3076 "build/parser.tab.cpp"
    break;

  case 72: /* member_item: function_definition  */
#line 469 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3082 "build/parser.tab.cpp"
    break;

  case 73: /* member_item: access_specifier ':'  */
#line 470 "src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3088 "build/parser.tab.cpp"
    break;

  case 74: /* member_item: constructor_def  */
#line 471 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3094 "build/parser.tab.cpp"
    break;

  case 75: /* $@9: %empty  */
#line 480 "src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3100 "build/parser.tab.cpp"
    break;

  case 76: /* constructor_head: IDENTIFIER '(' $@9 parameter_list_opt ')'  */
#line 480 "src/parser.y"
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
#line 3120 "build/parser.tab.cpp"
    break;

  case 77: /* constructor_def: constructor_head compound_stmt  */
#line 498 "src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), yyvsp[0].node);
      }
#line 3129 "build/parser.tab.cpp"
    break;

  case 78: /* constructor_def: constructor_head ';'  */
#line 502 "src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, yyvsp[-1].decl.isVariadic, currentClassName(), nullptr);
      }
#line 3138 "build/parser.tab.cpp"
    break;

  case 79: /* $@10: %empty  */
#line 510 "src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3148 "build/parser.tab.cpp"
    break;

  case 80: /* $@11: %empty  */
#line 514 "src/parser.y"
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
#line 3165 "build/parser.tab.cpp"
    break;

  case 81: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@10 parameter_list_opt ')' $@11 compound_stmt  */
#line 525 "src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-3].decl.isVariadic, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3175 "build/parser.tab.cpp"
    break;

  case 85: /* init_declarator_list_opt: %empty  */
#line 540 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3181 "build/parser.tab.cpp"
    break;

  case 86: /* init_declarator_list_opt: init_declarator_list  */
#line 541 "src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3187 "build/parser.tab.cpp"
    break;

  case 87: /* init_declarator_list: init_declarator  */
#line 545 "src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3193 "build/parser.tab.cpp"
    break;

  case 88: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 546 "src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3199 "build/parser.tab.cpp"
    break;

  case 89: /* init_declarator: declarator  */
#line 550 "src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3205 "build/parser.tab.cpp"
    break;

  case 90: /* init_declarator: declarator '=' initializer  */
#line 551 "src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3211 "build/parser.tab.cpp"
    break;

  case 91: /* initializer: assignment_expr  */
#line 555 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3217 "build/parser.tab.cpp"
    break;

  case 92: /* initializer: '{' '}'  */
#line 556 "src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3223 "build/parser.tab.cpp"
    break;

  case 93: /* initializer: '{' initializer_list '}'  */
#line 557 "src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3233 "build/parser.tab.cpp"
    break;

  case 94: /* initializer: '{' initializer_list ',' '}'  */
#line 562 "src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3243 "build/parser.tab.cpp"
    break;

  case 95: /* initializer_list: initializer_item  */
#line 570 "src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3249 "build/parser.tab.cpp"
    break;

  case 96: /* initializer_list: initializer_list ',' initializer_item  */
#line 571 "src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3255 "build/parser.tab.cpp"
    break;

  case 97: /* initializer_item: initializer  */
#line 575 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3261 "build/parser.tab.cpp"
    break;

  case 98: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 576 "src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3269 "build/parser.tab.cpp"
    break;

  case 99: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 579 "src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3277 "build/parser.tab.cpp"
    break;

  case 100: /* pointer: '*'  */
#line 585 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3283 "build/parser.tab.cpp"
    break;

  case 101: /* pointer: '&'  */
#line 586 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3289 "build/parser.tab.cpp"
    break;

  case 102: /* pointer: pointer '*'  */
#line 587 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3295 "build/parser.tab.cpp"
    break;

  case 103: /* pointer: pointer '&'  */
#line 588 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3301 "build/parser.tab.cpp"
    break;

  case 104: /* pointer: pointer CONST  */
#line 589 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3307 "build/parser.tab.cpp"
    break;

  case 105: /* declarator: pointer direct_declarator  */
#line 593 "src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3318 "build/parser.tab.cpp"
    break;

  case 106: /* declarator: direct_declarator  */
#line 599 "src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3324 "build/parser.tab.cpp"
    break;

  case 107: /* abstract_declarator: pointer  */
#line 605 "src/parser.y"
              { yyval = yyvsp[0]; }
#line 3330 "build/parser.tab.cpp"
    break;

  case 108: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 606 "src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3341 "build/parser.tab.cpp"
    break;

  case 109: /* abstract_declarator: direct_abstract_declarator  */
#line 612 "src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3347 "build/parser.tab.cpp"
    break;

  case 110: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 616 "src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3361 "build/parser.tab.cpp"
    break;

  case 111: /* direct_abstract_declarator: '[' ']'  */
#line 625 "src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3367 "build/parser.tab.cpp"
    break;

  case 112: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 626 "src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3373 "build/parser.tab.cpp"
    break;

  case 113: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 627 "src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3379 "build/parser.tab.cpp"
    break;

  case 114: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 628 "src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3385 "build/parser.tab.cpp"
    break;

  case 115: /* direct_declarator: IDENTIFIER  */
#line 632 "src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3394 "build/parser.tab.cpp"
    break;

  case 116: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 636 "src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3406 "build/parser.tab.cpp"
    break;

  case 117: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 643 "src/parser.y"
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
#line 3423 "build/parser.tab.cpp"
    break;

  case 118: /* direct_declarator: '(' declarator ')'  */
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
#line 3437 "build/parser.tab.cpp"
    break;

  case 119: /* direct_declarator: operator_function_id  */
#line 664 "src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3446 "build/parser.tab.cpp"
    break;

  case 120: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 668 "src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3458 "build/parser.tab.cpp"
    break;

  case 121: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 675 "src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3470 "build/parser.tab.cpp"
    break;

  case 122: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 682 "src/parser.y"
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
#line 3494 "build/parser.tab.cpp"
    break;

  case 123: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 701 "src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3506 "build/parser.tab.cpp"
    break;

  case 124: /* direct_declarator: direct_declarator '[' ']'  */
#line 708 "src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3512 "build/parser.tab.cpp"
    break;

  case 125: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 709 "src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3518 "build/parser.tab.cpp"
    break;

  case 126: /* operator_function_id: OPERATOR overloadable_operator  */
#line 714 "src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3524 "build/parser.tab.cpp"
    break;

  case 127: /* overloadable_operator: '+'  */
#line 718 "src/parser.y"
          { yyval.str = "+"; }
#line 3530 "build/parser.tab.cpp"
    break;

  case 128: /* overloadable_operator: '-'  */
#line 718 "src/parser.y"
                                  { yyval.str = "-"; }
#line 3536 "build/parser.tab.cpp"
    break;

  case 129: /* overloadable_operator: '*'  */
#line 718 "src/parser.y"
                                                          { yyval.str = "*"; }
#line 3542 "build/parser.tab.cpp"
    break;

  case 130: /* overloadable_operator: '/'  */
#line 718 "src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3548 "build/parser.tab.cpp"
    break;

  case 131: /* overloadable_operator: '%'  */
#line 719 "src/parser.y"
          { yyval.str = "%"; }
#line 3554 "build/parser.tab.cpp"
    break;

  case 132: /* overloadable_operator: '^'  */
#line 719 "src/parser.y"
                                  { yyval.str = "^"; }
#line 3560 "build/parser.tab.cpp"
    break;

  case 133: /* overloadable_operator: '&'  */
#line 719 "src/parser.y"
                                                          { yyval.str = "&"; }
#line 3566 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: '|'  */
#line 719 "src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3572 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: '~'  */
#line 720 "src/parser.y"
          { yyval.str = "~"; }
#line 3578 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: '!'  */
#line 720 "src/parser.y"
                                  { yyval.str = "!"; }
#line 3584 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: '='  */
#line 720 "src/parser.y"
                                                          { yyval.str = "="; }
#line 3590 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: '<'  */
#line 720 "src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3596 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: '>'  */
#line 721 "src/parser.y"
          { yyval.str = ">"; }
#line 3602 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: EQ_OP  */
#line 721 "src/parser.y"
                                    { yyval.str = "=="; }
#line 3608 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: NE_OP  */
#line 721 "src/parser.y"
                                                               { yyval.str = "!="; }
#line 3614 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: LE_OP  */
#line 721 "src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3620 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: GE_OP  */
#line 722 "src/parser.y"
            { yyval.str = ">="; }
#line 3626 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: AND_OP  */
#line 722 "src/parser.y"
                                        { yyval.str = "&&"; }
#line 3632 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: OR_OP  */
#line 722 "src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3638 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: SHL  */
#line 722 "src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3644 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: SHR  */
#line 723 "src/parser.y"
          { yyval.str = ">>"; }
#line 3650 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: INC  */
#line 723 "src/parser.y"
                                   { yyval.str = "++"; }
#line 3656 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: DEC  */
#line 723 "src/parser.y"
                                                            { yyval.str = "--"; }
#line 3662 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: PLUS_ASSIGN  */
#line 724 "src/parser.y"
                  { yyval.str = "+="; }
#line 3668 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: MINUS_ASSIGN  */
#line 724 "src/parser.y"
                                                    { yyval.str = "-="; }
#line 3674 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: MUL_ASSIGN  */
#line 724 "src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3680 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: DIV_ASSIGN  */
#line 725 "src/parser.y"
                 { yyval.str = "/="; }
#line 3686 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: MOD_ASSIGN  */
#line 725 "src/parser.y"
                                                 { yyval.str = "%="; }
#line 3692 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: AND_ASSIGN  */
#line 725 "src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3698 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: OR_ASSIGN  */
#line 726 "src/parser.y"
                { yyval.str = "|="; }
#line 3704 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: XOR_ASSIGN  */
#line 726 "src/parser.y"
                                                { yyval.str = "^="; }
#line 3710 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: SHL_ASSIGN  */
#line 726 "src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3716 "build/parser.tab.cpp"
    break;

  case 159: /* overloadable_operator: SHR_ASSIGN  */
#line 727 "src/parser.y"
                 { yyval.str = ">>="; }
#line 3722 "build/parser.tab.cpp"
    break;

  case 160: /* overloadable_operator: '[' ']'  */
#line 727 "src/parser.y"
                                               { yyval.str = "[]"; }
#line 3728 "build/parser.tab.cpp"
    break;

  case 161: /* overloadable_operator: '(' ')'  */
#line 727 "src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3734 "build/parser.tab.cpp"
    break;

  case 162: /* param_scope: %empty  */
#line 734 "src/parser.y"
                                           { pushScope(); }
#line 3740 "build/parser.tab.cpp"
    break;

  case 163: /* constructor_args: assignment_expr  */
#line 738 "src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3746 "build/parser.tab.cpp"
    break;

  case 164: /* constructor_args: constructor_args ',' assignment_expr  */
#line 739 "src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3752 "build/parser.tab.cpp"
    break;

  case 165: /* parameter_list_opt: %empty  */
#line 743 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3758 "build/parser.tab.cpp"
    break;

  case 166: /* parameter_list_opt: parameter_list  */
#line 744 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3764 "build/parser.tab.cpp"
    break;

  case 167: /* parameter_list: parameter_decl  */
#line 748 "src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
          yyval.decl.isVariadic = false; /* $$ started as a copy of this param's own decl */
      }
#line 3773 "build/parser.tab.cpp"
    break;

  case 168: /* parameter_list: parameter_list ',' parameter_decl  */
#line 752 "src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3782 "build/parser.tab.cpp"
    break;

  case 169: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 756 "src/parser.y"
                                  { yyval = yyvsp[-2]; yyval.decl.isVariadic = true; }
#line 3788 "build/parser.tab.cpp"
    break;

  case 170: /* parameter_decl: declaration_specifiers declarator  */
#line 760 "src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3798 "build/parser.tab.cpp"
    break;

  case 171: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 765 "src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3808 "build/parser.tab.cpp"
    break;

  case 172: /* parameter_decl: declaration_specifiers  */
#line 770 "src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3818 "build/parser.tab.cpp"
    break;

  case 173: /* $@12: %empty  */
#line 778 "src/parser.y"
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
#line 3860 "build/parser.tab.cpp"
    break;

  case 174: /* function_definition: declaration_specifiers declarator $@12 '{' block_item_list_opt '}'  */
#line 814 "src/parser.y"
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
#line 3891 "build/parser.tab.cpp"
    break;

  case 175: /* statement: compound_stmt  */
#line 843 "src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3897 "build/parser.tab.cpp"
    break;

  case 176: /* statement: expr_stmt  */
#line 844 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3903 "build/parser.tab.cpp"
    break;

  case 177: /* statement: selection_stmt  */
#line 845 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3909 "build/parser.tab.cpp"
    break;

  case 178: /* statement: iteration_stmt  */
#line 846 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3915 "build/parser.tab.cpp"
    break;

  case 179: /* statement: jump_stmt  */
#line 847 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3921 "build/parser.tab.cpp"
    break;

  case 180: /* statement: labeled_stmt  */
#line 848 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3927 "build/parser.tab.cpp"
    break;

  case 181: /* statement: declaration  */
#line 849 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3933 "build/parser.tab.cpp"
    break;

  case 182: /* statement: error ';'  */
#line 850 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3939 "build/parser.tab.cpp"
    break;

  case 183: /* statement: error '}'  */
#line 851 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3945 "build/parser.tab.cpp"
    break;

  case 184: /* $@13: %empty  */
#line 855 "src/parser.y"
          { pushScope(); }
#line 3951 "build/parser.tab.cpp"
    break;

  case 185: /* compound_stmt: '{' $@13 block_item_list_opt '}'  */
#line 855 "src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 3962 "build/parser.tab.cpp"
    break;

  case 186: /* block_item_list_opt: %empty  */
#line 864 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3968 "build/parser.tab.cpp"
    break;

  case 187: /* block_item_list_opt: block_item_list  */
#line 865 "src/parser.y"
                      { yyval = yyvsp[0]; }
#line 3974 "build/parser.tab.cpp"
    break;

  case 188: /* block_item_list: statement  */
#line 869 "src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3980 "build/parser.tab.cpp"
    break;

  case 189: /* block_item_list: block_item_list statement  */
#line 870 "src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3986 "build/parser.tab.cpp"
    break;

  case 190: /* expr_stmt: ';'  */
#line 874 "src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 3992 "build/parser.tab.cpp"
    break;

  case 191: /* expr_stmt: expr ';'  */
#line 875 "src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 3998 "build/parser.tab.cpp"
    break;

  case 192: /* selection_stmt: IF '(' expr ')' statement  */
#line 879 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4006 "build/parser.tab.cpp"
    break;

  case 193: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 882 "src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 4014 "build/parser.tab.cpp"
    break;

  case 194: /* $@14: %empty  */
#line 885 "src/parser.y"
                          { hintScope("switch"); }
#line 4020 "build/parser.tab.cpp"
    break;

  case 195: /* selection_stmt: SWITCH '(' expr ')' $@14 compound_stmt  */
#line 885 "src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4028 "build/parser.tab.cpp"
    break;

  case 196: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 891 "src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4036 "build/parser.tab.cpp"
    break;

  case 197: /* labeled_stmt: DEFAULT ':' statement  */
#line 894 "src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4044 "build/parser.tab.cpp"
    break;

  case 198: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 897 "src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4054 "build/parser.tab.cpp"
    break;

  case 199: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 905 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4062 "build/parser.tab.cpp"
    break;

  case 200: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 908 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4070 "build/parser.tab.cpp"
    break;

  case 201: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 915 "src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4079 "build/parser.tab.cpp"
    break;

  case 202: /* iteration_stmt: DO statement error ';'  */
#line 919 "src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4088 "build/parser.tab.cpp"
    break;

  case 203: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 923 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4096 "build/parser.tab.cpp"
    break;

  case 204: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 926 "src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4105 "build/parser.tab.cpp"
    break;

  case 205: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 930 "src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4114 "build/parser.tab.cpp"
    break;

  case 206: /* for_open: FOR '('  */
#line 939 "src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4120 "build/parser.tab.cpp"
    break;

  case 207: /* for_incr_opt: %empty  */
#line 943 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4126 "build/parser.tab.cpp"
    break;

  case 208: /* for_incr_opt: expr  */
#line 944 "src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4132 "build/parser.tab.cpp"
    break;

  case 209: /* jump_stmt: BREAK ';'  */
#line 948 "src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4138 "build/parser.tab.cpp"
    break;

  case 210: /* jump_stmt: CONTINUE ';'  */
#line 949 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4144 "build/parser.tab.cpp"
    break;

  case 211: /* jump_stmt: RETURN ';'  */
#line 950 "src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4150 "build/parser.tab.cpp"
    break;

  case 212: /* jump_stmt: RETURN expr ';'  */
#line 951 "src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4156 "build/parser.tab.cpp"
    break;

  case 213: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 952 "src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4168 "build/parser.tab.cpp"
    break;

  case 214: /* expr: assignment_expr  */
#line 962 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4174 "build/parser.tab.cpp"
    break;

  case 215: /* expr: expr ',' assignment_expr  */
#line 963 "src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4180 "build/parser.tab.cpp"
    break;

  case 216: /* assignment_expr: binary_expr  */
#line 967 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4186 "build/parser.tab.cpp"
    break;

  case 217: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 968 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4194 "build/parser.tab.cpp"
    break;

  case 218: /* assign_op: '='  */
#line 974 "src/parser.y"
                   { yyval.str = "="; }
#line 4200 "build/parser.tab.cpp"
    break;

  case 219: /* assign_op: PLUS_ASSIGN  */
#line 975 "src/parser.y"
                   { yyval.str = "+="; }
#line 4206 "build/parser.tab.cpp"
    break;

  case 220: /* assign_op: MINUS_ASSIGN  */
#line 976 "src/parser.y"
                   { yyval.str = "-="; }
#line 4212 "build/parser.tab.cpp"
    break;

  case 221: /* assign_op: MUL_ASSIGN  */
#line 977 "src/parser.y"
                   { yyval.str = "*="; }
#line 4218 "build/parser.tab.cpp"
    break;

  case 222: /* assign_op: DIV_ASSIGN  */
#line 978 "src/parser.y"
                   { yyval.str = "/="; }
#line 4224 "build/parser.tab.cpp"
    break;

  case 223: /* assign_op: MOD_ASSIGN  */
#line 979 "src/parser.y"
                   { yyval.str = "%="; }
#line 4230 "build/parser.tab.cpp"
    break;

  case 224: /* assign_op: AND_ASSIGN  */
#line 980 "src/parser.y"
                   { yyval.str = "&="; }
#line 4236 "build/parser.tab.cpp"
    break;

  case 225: /* assign_op: OR_ASSIGN  */
#line 981 "src/parser.y"
                   { yyval.str = "|="; }
#line 4242 "build/parser.tab.cpp"
    break;

  case 226: /* assign_op: XOR_ASSIGN  */
#line 982 "src/parser.y"
                   { yyval.str = "^="; }
#line 4248 "build/parser.tab.cpp"
    break;

  case 227: /* assign_op: SHL_ASSIGN  */
#line 983 "src/parser.y"
                   { yyval.str = "<<="; }
#line 4254 "build/parser.tab.cpp"
    break;

  case 228: /* assign_op: SHR_ASSIGN  */
#line 984 "src/parser.y"
                   { yyval.str = ">>="; }
#line 4260 "build/parser.tab.cpp"
    break;

  case 229: /* constant_expr: binary_expr  */
#line 988 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4266 "build/parser.tab.cpp"
    break;

  case 230: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 992 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4272 "build/parser.tab.cpp"
    break;

  case 231: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 993 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4278 "build/parser.tab.cpp"
    break;

  case 232: /* binary_expr: binary_expr '|' binary_expr  */
#line 994 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4284 "build/parser.tab.cpp"
    break;

  case 233: /* binary_expr: binary_expr '^' binary_expr  */
#line 995 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4290 "build/parser.tab.cpp"
    break;

  case 234: /* binary_expr: binary_expr '&' binary_expr  */
#line 996 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4296 "build/parser.tab.cpp"
    break;

  case 235: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 997 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4302 "build/parser.tab.cpp"
    break;

  case 236: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 998 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4308 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr '<' binary_expr  */
#line 999 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4314 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr '>' binary_expr  */
#line 1000 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4320 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 1001 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4326 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 1002 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4332 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr SHL binary_expr  */
#line 1003 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4338 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr SHR binary_expr  */
#line 1004 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4344 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: binary_expr '+' binary_expr  */
#line 1005 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4350 "build/parser.tab.cpp"
    break;

  case 244: /* binary_expr: binary_expr '-' binary_expr  */
#line 1006 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4356 "build/parser.tab.cpp"
    break;

  case 245: /* binary_expr: binary_expr '*' binary_expr  */
#line 1007 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4362 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: binary_expr '/' binary_expr  */
#line 1008 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4368 "build/parser.tab.cpp"
    break;

  case 247: /* binary_expr: binary_expr '%' binary_expr  */
#line 1009 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4374 "build/parser.tab.cpp"
    break;

  case 248: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 1010 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4382 "build/parser.tab.cpp"
    break;

  case 249: /* binary_expr: unary_expr  */
#line 1013 "src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4388 "build/parser.tab.cpp"
    break;

  case 250: /* unary_expr: postfix_expr  */
#line 1017 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4394 "build/parser.tab.cpp"
    break;

  case 251: /* unary_expr: INC unary_expr  */
#line 1018 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4400 "build/parser.tab.cpp"
    break;

  case 252: /* unary_expr: DEC unary_expr  */
#line 1019 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4406 "build/parser.tab.cpp"
    break;

  case 253: /* unary_expr: '&' unary_expr  */
#line 1020 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4412 "build/parser.tab.cpp"
    break;

  case 254: /* unary_expr: '*' unary_expr  */
#line 1021 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4418 "build/parser.tab.cpp"
    break;

  case 255: /* unary_expr: '+' unary_expr  */
#line 1022 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4424 "build/parser.tab.cpp"
    break;

  case 256: /* unary_expr: '-' unary_expr  */
#line 1023 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4430 "build/parser.tab.cpp"
    break;

  case 257: /* unary_expr: '!' unary_expr  */
#line 1024 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4436 "build/parser.tab.cpp"
    break;

  case 258: /* unary_expr: '~' unary_expr  */
#line 1025 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4442 "build/parser.tab.cpp"
    break;

  case 259: /* unary_expr: '(' type_name ')' unary_expr  */
#line 1026 "src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4451 "build/parser.tab.cpp"
    break;

  case 260: /* unary_expr: SIZEOF unary_expr  */
#line 1030 "src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4457 "build/parser.tab.cpp"
    break;

  case 261: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 1031 "src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4466 "build/parser.tab.cpp"
    break;

  case 262: /* type_name: type_name_specifiers  */
#line 1038 "src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4475 "build/parser.tab.cpp"
    break;

  case 263: /* type_name: type_name_specifiers abstract_declarator  */
#line 1042 "src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4484 "build/parser.tab.cpp"
    break;

  case 264: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1049 "src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4496 "build/parser.tab.cpp"
    break;

  case 265: /* type_name_specifiers: type_name_specifier  */
#line 1056 "src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4502 "build/parser.tab.cpp"
    break;

  case 266: /* type_name_specifier: INT  */
#line 1060 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4508 "build/parser.tab.cpp"
    break;

  case 267: /* type_name_specifier: CHAR  */
#line 1061 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4514 "build/parser.tab.cpp"
    break;

  case 268: /* type_name_specifier: FLOAT  */
#line 1062 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4520 "build/parser.tab.cpp"
    break;

  case 269: /* type_name_specifier: DOUBLE  */
#line 1063 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4526 "build/parser.tab.cpp"
    break;

  case 270: /* type_name_specifier: VOID  */
#line 1064 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4532 "build/parser.tab.cpp"
    break;

  case 271: /* type_name_specifier: BOOL  */
#line 1065 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4538 "build/parser.tab.cpp"
    break;

  case 272: /* type_name_specifier: SHORT  */
#line 1066 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4544 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifier: LONG  */
#line 1067 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4550 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifier: SIGNED  */
#line 1068 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4556 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: UNSIGNED  */
#line 1069 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4562 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: VA_LIST  */
#line 1070 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VA_LIST"); }
#line 4568 "build/parser.tab.cpp"
    break;

  case 277: /* type_name_specifier: CONST  */
#line 1071 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4574 "build/parser.tab.cpp"
    break;

  case 278: /* type_name_specifier: TYPE_NAME  */
#line 1072 "src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4588 "build/parser.tab.cpp"
    break;

  case 279: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1081 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4599 "build/parser.tab.cpp"
    break;

  case 280: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1087 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4610 "build/parser.tab.cpp"
    break;

  case 281: /* type_name_specifier: ENUM IDENTIFIER  */
#line 1093 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4621 "build/parser.tab.cpp"
    break;

  case 282: /* type_name_specifier: ENUM TYPE_NAME  */
#line 1099 "src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4632 "build/parser.tab.cpp"
    break;

  case 283: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1105 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4643 "build/parser.tab.cpp"
    break;

  case 284: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1111 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4654 "build/parser.tab.cpp"
    break;

  case 285: /* postfix_expr: primary_expr  */
#line 1120 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4660 "build/parser.tab.cpp"
    break;

  case 286: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1121 "src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4666 "build/parser.tab.cpp"
    break;

  case 287: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1122 "src/parser.y"
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
#line 4706 "build/parser.tab.cpp"
    break;

  case 288: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1157 "src/parser.y"
                                  {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4715 "build/parser.tab.cpp"
    break;

  case 289: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1161 "src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4728 "build/parser.tab.cpp"
    break;

  case 290: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1169 "src/parser.y"
                                                        {
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4739 "build/parser.tab.cpp"
    break;

  case 291: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1175 "src/parser.y"
                                    {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4748 "build/parser.tab.cpp"
    break;

  case 292: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1179 "src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4754 "build/parser.tab.cpp"
    break;

  case 293: /* postfix_expr: postfix_expr INC  */
#line 1180 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4760 "build/parser.tab.cpp"
    break;

  case 294: /* postfix_expr: postfix_expr DEC  */
#line 1181 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4766 "build/parser.tab.cpp"
    break;

  case 295: /* postfix_expr: builtin_call  */
#line 1182 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4772 "build/parser.tab.cpp"
    break;

  case 296: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1186 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4778 "build/parser.tab.cpp"
    break;

  case 297: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1187 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4784 "build/parser.tab.cpp"
    break;

  case 298: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1188 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4790 "build/parser.tab.cpp"
    break;

  case 299: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1189 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4796 "build/parser.tab.cpp"
    break;

  case 300: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1190 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4802 "build/parser.tab.cpp"
    break;

  case 301: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1191 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4808 "build/parser.tab.cpp"
    break;

  case 302: /* builtin_call: VA_START '(' argument_list_opt ')'  */
#line 1192 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_start"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4814 "build/parser.tab.cpp"
    break;

  case 303: /* builtin_call: VA_ARG '(' argument_list_opt ')'  */
#line 1193 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_arg"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4820 "build/parser.tab.cpp"
    break;

  case 304: /* builtin_call: VA_END '(' argument_list_opt ')'  */
#line 1194 "src/parser.y"
                                         { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "va_end"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4826 "build/parser.tab.cpp"
    break;

  case 305: /* constructor_args_opt: %empty  */
#line 1198 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4832 "build/parser.tab.cpp"
    break;

  case 306: /* constructor_args_opt: constructor_args  */
#line 1199 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4838 "build/parser.tab.cpp"
    break;

  case 307: /* argument_list_opt: %empty  */
#line 1203 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4844 "build/parser.tab.cpp"
    break;

  case 308: /* argument_list_opt: argument_list  */
#line 1204 "src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4850 "build/parser.tab.cpp"
    break;

  case 309: /* argument_list: argument  */
#line 1208 "src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4856 "build/parser.tab.cpp"
    break;

  case 310: /* argument_list: argument_list ',' argument  */
#line 1209 "src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4862 "build/parser.tab.cpp"
    break;

  case 311: /* argument: assignment_expr  */
#line 1213 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4868 "build/parser.tab.cpp"
    break;

  case 312: /* argument: type_name  */
#line 1214 "src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4877 "build/parser.tab.cpp"
    break;

  case 313: /* primary_expr: IDENTIFIER  */
#line 1221 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 4891 "build/parser.tab.cpp"
    break;

  case 314: /* primary_expr: INT_LITERAL  */
#line 1230 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4897 "build/parser.tab.cpp"
    break;

  case 315: /* primary_expr: FLOAT_LITERAL  */
#line 1231 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4903 "build/parser.tab.cpp"
    break;

  case 316: /* primary_expr: CHAR_LITERAL  */
#line 1232 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4909 "build/parser.tab.cpp"
    break;

  case 317: /* primary_expr: string_literal  */
#line 1233 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4915 "build/parser.tab.cpp"
    break;

  case 318: /* primary_expr: BOOL_LITERAL  */
#line 1234 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4921 "build/parser.tab.cpp"
    break;

  case 319: /* primary_expr: THIS  */
#line 1235 "src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 4927 "build/parser.tab.cpp"
    break;

  case 320: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1236 "src/parser.y"
                                             {
          /* `Dog()`: a temporary object (for a scalar type, `int(x)`, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4936 "build/parser.tab.cpp"
    break;

  case 321: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1240 "src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4946 "build/parser.tab.cpp"
    break;

  case 322: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1247 "src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4952 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1248 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4958 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1249 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4964 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1250 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4970 "build/parser.tab.cpp"
    break;

  case 326: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1251 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4976 "build/parser.tab.cpp"
    break;

  case 327: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1252 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4982 "build/parser.tab.cpp"
    break;

  case 328: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1253 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4988 "build/parser.tab.cpp"
    break;

  case 329: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1254 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4994 "build/parser.tab.cpp"
    break;

  case 330: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1255 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5000 "build/parser.tab.cpp"
    break;

  case 331: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1256 "src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 5006 "build/parser.tab.cpp"
    break;

  case 332: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1257 "src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 5018 "build/parser.tab.cpp"
    break;

  case 333: /* primary_expr: '(' expr ')'  */
#line 1264 "src/parser.y"
                   {
          yyval.node = yyvsp[-1].node; /* parentheses build no node, but are remembered: */
          if (yyval.node) yyval.node->parenthesized = true; /* `if ((x = f()))` means the assignment */
      }
#line 5027 "build/parser.tab.cpp"
    break;

  case 334: /* string_literal: STRING_LITERAL  */
#line 1272 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 5033 "build/parser.tab.cpp"
    break;

  case 335: /* string_literal: string_literal STRING_LITERAL  */
#line 1273 "src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 5043 "build/parser.tab.cpp"
    break;


#line 5047 "build/parser.tab.cpp"

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
