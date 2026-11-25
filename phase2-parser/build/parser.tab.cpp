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
  YYSYMBOL_OPERATOR = 47,                  /* OPERATOR  */
  YYSYMBOL_FCAST = 48,                     /* FCAST  */
  YYSYMBOL_ABSTRACT_LPAREN = 49,           /* ABSTRACT_LPAREN  */
  YYSYMBOL_IDENTIFIER = 50,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 51,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 52,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 53,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 54,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 55,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 56,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 57,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 58,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 59,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 60,                       /* INC  */
  YYSYMBOL_DEC = 61,                       /* DEC  */
  YYSYMBOL_SHL = 62,                       /* SHL  */
  YYSYMBOL_SHR = 63,                       /* SHR  */
  YYSYMBOL_LE_OP = 64,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 65,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 66,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 67,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 68,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 69,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 70,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 71,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 72,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 73,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 74,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 75,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 76,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 77,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 78,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 79,                /* SHR_ASSIGN  */
  YYSYMBOL_PREFER_EXPRESSION = 80,         /* PREFER_EXPRESSION  */
  YYSYMBOL_81_ = 81,                       /* '='  */
  YYSYMBOL_82_ = 82,                       /* '?'  */
  YYSYMBOL_83_ = 83,                       /* ':'  */
  YYSYMBOL_84_ = 84,                       /* '|'  */
  YYSYMBOL_85_ = 85,                       /* '^'  */
  YYSYMBOL_86_ = 86,                       /* '&'  */
  YYSYMBOL_87_ = 87,                       /* '<'  */
  YYSYMBOL_88_ = 88,                       /* '>'  */
  YYSYMBOL_89_ = 89,                       /* '+'  */
  YYSYMBOL_90_ = 90,                       /* '-'  */
  YYSYMBOL_91_ = 91,                       /* '*'  */
  YYSYMBOL_92_ = 92,                       /* '/'  */
  YYSYMBOL_93_ = 93,                       /* '%'  */
  YYSYMBOL_UMINUS = 94,                    /* UMINUS  */
  YYSYMBOL_ADDR = 95,                      /* ADDR  */
  YYSYMBOL_DEREF = 96,                     /* DEREF  */
  YYSYMBOL_CAST = 97,                      /* CAST  */
  YYSYMBOL_98_ = 98,                       /* '!'  */
  YYSYMBOL_99_ = 99,                       /* '~'  */
  YYSYMBOL_100_ = 100,                     /* '.'  */
  YYSYMBOL_101_ = 101,                     /* '('  */
  YYSYMBOL_102_ = 102,                     /* '['  */
  YYSYMBOL_SIZEOF_TYPE = 103,              /* SIZEOF_TYPE  */
  YYSYMBOL_PREFER_DECLARATION = 104,       /* PREFER_DECLARATION  */
  YYSYMBOL_IFX = 105,                      /* IFX  */
  YYSYMBOL_106_ = 106,                     /* ';'  */
  YYSYMBOL_107_ = 107,                     /* '}'  */
  YYSYMBOL_108_ = 108,                     /* '{'  */
  YYSYMBOL_109_ = 109,                     /* ','  */
  YYSYMBOL_110_ = 110,                     /* ')'  */
  YYSYMBOL_111_ = 111,                     /* ']'  */
  YYSYMBOL_YYACCEPT = 112,                 /* $accept  */
  YYSYMBOL_translation_unit = 113,         /* translation_unit  */
  YYSYMBOL_external_decl = 114,            /* external_decl  */
  YYSYMBOL_declaration = 115,              /* declaration  */
  YYSYMBOL_declaration_specifiers = 116,   /* declaration_specifiers  */
  YYSYMBOL_storage_or_type_specifier = 117, /* storage_or_type_specifier  */
  YYSYMBOL_type_specifier = 118,           /* type_specifier  */
  YYSYMBOL_tag_name = 119,                 /* tag_name  */
  YYSYMBOL_struct_or_class_specifier = 120, /* struct_or_class_specifier  */
  YYSYMBOL_121_1 = 121,                    /* $@1  */
  YYSYMBOL_122_2 = 122,                    /* $@2  */
  YYSYMBOL_123_3 = 123,                    /* @3  */
  YYSYMBOL_124_4 = 124,                    /* $@4  */
  YYSYMBOL_125_5 = 125,                    /* @5  */
  YYSYMBOL_126_6 = 126,                    /* $@6  */
  YYSYMBOL_127_7 = 127,                    /* $@7  */
  YYSYMBOL_128_8 = 128,                    /* @8  */
  YYSYMBOL_member_decl_list_opt = 129,     /* member_decl_list_opt  */
  YYSYMBOL_enumerator_list = 130,          /* enumerator_list  */
  YYSYMBOL_enumerator = 131,               /* enumerator  */
  YYSYMBOL_comma_opt = 132,                /* comma_opt  */
  YYSYMBOL_inheritance_opt = 133,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 134, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 135,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 136,         /* member_decl_list  */
  YYSYMBOL_member_item = 137,              /* member_item  */
  YYSYMBOL_constructor_head = 138,         /* constructor_head  */
  YYSYMBOL_139_9 = 139,                    /* $@9  */
  YYSYMBOL_constructor_def = 140,          /* constructor_def  */
  YYSYMBOL_out_of_class_special = 141,     /* out_of_class_special  */
  YYSYMBOL_142_10 = 142,                   /* $@10  */
  YYSYMBOL_143_11 = 143,                   /* $@11  */
  YYSYMBOL_access_specifier = 144,         /* access_specifier  */
  YYSYMBOL_init_declarator_list_opt = 145, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 146,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 147,          /* init_declarator  */
  YYSYMBOL_initializer = 148,              /* initializer  */
  YYSYMBOL_initializer_list = 149,         /* initializer_list  */
  YYSYMBOL_initializer_item = 150,         /* initializer_item  */
  YYSYMBOL_pointer = 151,                  /* pointer  */
  YYSYMBOL_declarator = 152,               /* declarator  */
  YYSYMBOL_abstract_declarator = 153,      /* abstract_declarator  */
  YYSYMBOL_direct_abstract_declarator = 154, /* direct_abstract_declarator  */
  YYSYMBOL_direct_declarator = 155,        /* direct_declarator  */
  YYSYMBOL_operator_function_id = 156,     /* operator_function_id  */
  YYSYMBOL_overloadable_operator = 157,    /* overloadable_operator  */
  YYSYMBOL_param_scope = 158,              /* param_scope  */
  YYSYMBOL_constructor_args = 159,         /* constructor_args  */
  YYSYMBOL_parameter_list_opt = 160,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 161,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 162,           /* parameter_decl  */
  YYSYMBOL_function_definition = 163,      /* function_definition  */
  YYSYMBOL_164_12 = 164,                   /* $@12  */
  YYSYMBOL_statement = 165,                /* statement  */
  YYSYMBOL_compound_stmt = 166,            /* compound_stmt  */
  YYSYMBOL_167_13 = 167,                   /* $@13  */
  YYSYMBOL_block_item_list_opt = 168,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 169,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 170,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 171,           /* selection_stmt  */
  YYSYMBOL_172_14 = 172,                   /* $@14  */
  YYSYMBOL_labeled_stmt = 173,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 174,           /* iteration_stmt  */
  YYSYMBOL_for_open = 175,                 /* for_open  */
  YYSYMBOL_for_incr_opt = 176,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 177,                /* jump_stmt  */
  YYSYMBOL_expr = 178,                     /* expr  */
  YYSYMBOL_assignment_expr = 179,          /* assignment_expr  */
  YYSYMBOL_assign_op = 180,                /* assign_op  */
  YYSYMBOL_constant_expr = 181,            /* constant_expr  */
  YYSYMBOL_binary_expr = 182,              /* binary_expr  */
  YYSYMBOL_unary_expr = 183,               /* unary_expr  */
  YYSYMBOL_type_name = 184,                /* type_name  */
  YYSYMBOL_type_name_specifiers = 185,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 186,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 187,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 188,             /* builtin_call  */
  YYSYMBOL_constructor_args_opt = 189,     /* constructor_args_opt  */
  YYSYMBOL_argument_list_opt = 190,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 191,            /* argument_list  */
  YYSYMBOL_argument = 192,                 /* argument  */
  YYSYMBOL_primary_expr = 193,             /* primary_expr  */
  YYSYMBOL_string_literal = 194            /* string_literal  */
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

#line 359 "build/parser.tab.cpp"

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
#define YYLAST   2079

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  112
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  83
/* YYNRULES -- Number of rules.  */
#define YYNRULES  330
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  581

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   342


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
       2,     2,     2,    98,     2,     2,     2,    93,    86,     2,
     101,   110,    91,    89,   109,    90,   100,    92,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    83,   106,
      87,    81,    88,    82,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   102,     2,   111,    85,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   108,    84,   107,    99,     2,     2,     2,
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
      75,    76,    77,    78,    79,    80,    94,    95,    96,    97,
     103,   104,   105
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   139,   139,   143,   151,   152,   153,   154,   155,   159,
     190,   203,   207,   208,   209,   210,   211,   212,   216,   217,
     218,   219,   220,   221,   222,   223,   224,   225,   226,   240,
     247,   248,   252,   256,   252,   272,   272,   286,   292,   298,
     304,   310,   310,   321,   321,   331,   335,   331,   347,   347,
     361,   367,   376,   377,   384,   385,   389,   394,   402,   403,
     407,   408,   412,   413,   420,   426,   432,   438,   449,   454,
     466,   467,   468,   469,   478,   478,   495,   499,   507,   511,
     507,   531,   532,   533,   537,   538,   542,   543,   547,   548,
     552,   553,   554,   559,   567,   568,   572,   573,   576,   582,
     583,   584,   585,   586,   590,   596,   602,   603,   609,   613,
     622,   623,   624,   625,   629,   633,   640,   652,   661,   665,
     672,   679,   697,   704,   705,   710,   714,   714,   714,   714,
     715,   715,   715,   715,   716,   716,   716,   716,   717,   717,
     717,   717,   718,   718,   718,   718,   719,   719,   719,   720,
     720,   720,   721,   721,   721,   722,   722,   722,   723,   723,
     723,   730,   734,   735,   739,   740,   744,   747,   751,   762,
     767,   772,   780,   780,   845,   846,   847,   848,   849,   850,
     851,   852,   853,   857,   857,   866,   867,   871,   872,   876,
     877,   881,   884,   887,   887,   893,   896,   899,   907,   910,
     917,   921,   925,   928,   932,   941,   945,   946,   950,   951,
     952,   953,   954,   964,   965,   969,   970,   976,   977,   978,
     979,   980,   981,   982,   983,   984,   985,   986,   990,   994,
     995,   996,   997,   998,   999,  1000,  1001,  1002,  1003,  1004,
    1005,  1006,  1007,  1008,  1009,  1010,  1011,  1012,  1015,  1019,
    1020,  1021,  1022,  1023,  1024,  1025,  1026,  1027,  1028,  1032,
    1033,  1040,  1044,  1051,  1058,  1062,  1063,  1064,  1065,  1066,
    1067,  1068,  1069,  1070,  1071,  1072,  1073,  1082,  1088,  1094,
    1100,  1106,  1112,  1121,  1122,  1123,  1158,  1162,  1170,  1176,
    1180,  1181,  1182,  1183,  1187,  1188,  1189,  1190,  1191,  1192,
    1196,  1197,  1201,  1202,  1206,  1207,  1211,  1212,  1219,  1228,
    1229,  1230,  1231,  1232,  1233,  1234,  1238,  1245,  1246,  1247,
    1248,  1249,  1250,  1251,  1252,  1253,  1254,  1255,  1262,  1270,
    1271
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
  "FREE", "CALLOC", "REALLOC", "BOOL", "SIZEOF", "OPERATOR", "FCAST",
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

#define YYPACT_NINF (-392)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-187)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -392,  1862,  -392,   -70,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,   -18,     0,    12,  -392,  -392,  -392,  -392,
    -392,  -392,    41,  -392,  -392,  1723,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,   -60,   -50,  -392,  -392,   -53,   -48,  -392,
    -392,   -60,   -50,  -392,  -392,    27,  1903,    63,    91,  -392,
    -392,    55,  -392,     8,    49,  -392,     2,    -7,    53,  -392,
    1911,    64,  1911,   105,   134,    95,   137,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
     130,    94,  -392,    -8,    -6,    91,   160,  -392,    55,  -392,
    -392,  -392,    53,  1106,   148,  1736,   443,  -392,  -392,  -392,
     180,  -392,  -392,   144,  1911,  -392,    13,  -392,   204,  -392,
    -392,   182,   170,   195,   223,   196,  -392,   134,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,   225,   206,   209,
     210,   211,   212,   213,   214,   217,   218,  -392,   219,   220,
     221,   222,   224,   226,   228,  1538,   229,  -392,   -21,  -392,
    -392,  -392,  -392,  -392,  1601,  1601,  1601,  1601,  1601,  1601,
    1601,  1601,  1475,   966,  -392,  -392,  1944,   171,    16,  -392,
    -392,   271,   680,   739,    52,  -392,  -392,   237,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  1911,  -392,  -392,  -392,   240,
    -392,   143,  -392,  1601,   134,   227,   196,   739,  1601,  1601,
    1601,  1601,  1601,  1601,  1601,  1601,  1601,  1475,  1475,  1475,
    1475,  1475,  1475,  1601,  1475,  -392,  1601,   283,  1601,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,   206,   209,   210,
     211,   212,   213,   214,   217,   218,   146,   150,   157,  -392,
     228,   -21,   101,  -392,   241,   333,  -392,   300,  1601,  -392,
    -392,   -24,  -392,  1601,  1601,  1601,  1601,  1601,  1601,  1601,
    1601,  1601,  1601,  1601,  1601,  1601,  1601,  1601,  1601,  1601,
    1601,  1601,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  1601,   163,   302,  -392,  -392,   172,  1475,
    1601,  -392,   111,  -392,  -392,  -392,  -392,  -392,  -392,  -392,
    -392,  -392,   234,   252,   253,   896,   255,   257,  1601,   276,
     254,   256,   311,  1281,  -392,   281,   309,  -392,  -392,  1723,
    -392,  -392,   262,   788,  -392,  -392,  -392,  -392,  1212,  -392,
       3,  1410,   260,   270,  -392,  1601,  -392,  -392,   739,   680,
     264,   170,  -392,  -392,  1911,  -392,  1944,  -392,  -392,  -392,
     273,   275,   272,   277,   278,   279,   280,   282,   284,   296,
     297,   298,  -392,  -392,   299,   286,  -392,   301,   303,   304,
     305,   306,   308,   312,   315,  -392,   316,  -392,  -392,  -392,
    -392,  -392,  -392,  1601,  -392,  1601,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,   104,  -392,   507,     5,
    -392,   289,  -392,   331,   317,  -392,  1036,   141,   141,   136,
     136,   378,   378,  1380,  1954,    74,  1986,   587,   310,   136,
     136,   167,   167,  -392,  -392,  -392,  -392,  -392,   334,  -392,
    -392,   368,   319,    80,  -392,  -392,  1601,  -392,  1601,    28,
    1601,  1601,   347,   896,  -392,  -392,   325,  -392,     4,   896,
    -392,  -392,  1350,  1350,  -392,    -4,  -392,  -392,  -392,  1835,
    -392,   322,   326,  -392,  -392,   327,  -392,  -392,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,  -392,  1475,  -392,
    -392,  -392,  -392,  -392,  -392,  1664,  -392,  -392,  -392,  -392,
     328,  -392,   345,   289,   571,  1106,   355,  -392,  -392,  1601,
     387,   394,  -392,  -392,   173,   175,   351,   357,   183,   185,
     896,  -392,  -392,  -392,  -392,  1601,  1601,  -392,  -392,  -392,
    -392,  -392,   352,  -392,  -392,  -392,  -392,   348,  -392,  1106,
    1944,  -392,  -392,   896,   896,  -392,  1601,   896,  -392,  -392,
     353,   363,   354,  -392,  -392,  -392,   435,  -392,   188,  -392,
     352,   896,   896,   896,     9,  -392,  -392,  -392,  -392,  -392,
    -392
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    18,    19,    20,    21,    22,    24,
      25,    26,    27,     0,     0,     0,    12,    14,    13,    15,
      16,    23,    28,     3,     5,    84,    11,    17,    29,     6,
       4,     7,     8,    37,    38,    35,    32,    50,    51,    48,
      45,    39,    40,    43,    41,     0,     0,   114,    28,   100,
      99,     0,    10,     0,    85,    86,     0,    88,   105,   118,
      52,     0,    52,    60,     0,     0,     0,   147,   148,   145,
     146,   141,   142,   139,   140,   143,   144,   149,   150,   151,
     152,   153,   154,   155,   156,   157,   158,   136,   133,   131,
     132,   137,   138,   126,   127,   128,   129,   130,   135,   134,
       0,     0,   125,     0,     0,     0,     0,     9,     0,   103,
     102,   101,   104,     0,     0,   161,     0,    81,    82,    83,
       0,    28,    70,     0,    53,    68,     0,    73,     0,    71,
      33,     0,     0,     0,    56,    58,    54,     0,    78,   160,
     159,   115,   119,   116,   120,   117,    87,    88,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   314,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   308,     0,   309,
     310,   311,   329,   313,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    89,    90,   215,   248,   249,   293,
     283,   312,     0,   164,     0,   162,   123,     0,    74,    36,
      69,    77,   183,    76,    72,    52,    49,    66,    67,    61,
      62,     0,    46,     0,    59,     0,    58,   164,   300,   300,
     300,   300,   300,   300,   300,   300,   300,   302,   302,   302,
     302,   302,   302,   300,     0,   259,   300,     0,   300,   250,
     251,   252,   254,   255,   253,   256,   257,   265,   266,   267,
     268,   269,   271,   272,   273,   274,     0,     0,     0,   275,
     270,   276,     0,   213,     0,   261,   264,     0,     0,    91,
      96,     0,    94,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   218,   219,   220,   221,   222,   223,   224,   225,
     226,   227,   217,     0,     0,     0,   291,   292,     0,   302,
       0,   330,     0,    18,    19,    20,    21,    22,    24,    25,
      26,    27,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    23,   308,    28,   189,   180,    84,
     187,   174,     0,     0,   175,   176,   179,   177,     0,   178,
       0,   171,     0,   165,   166,     0,   122,   124,   164,     0,
       0,     0,    64,    65,    52,    57,   228,   248,    55,    44,
       0,     0,   301,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   306,   307,     0,   303,   304,     0,     0,     0,
       0,     0,     0,     0,     0,   327,     0,   277,   278,   281,
     282,   279,   280,     0,   328,     0,   265,   266,   267,   268,
     269,   271,   272,   273,   274,   270,     0,   276,     0,   106,
     262,   108,   263,     0,     0,    92,     0,   240,   241,   238,
     239,   234,   235,   230,   229,     0,   231,   232,   233,   236,
     237,   242,   243,   244,   245,   246,   216,   289,     0,   290,
     286,     0,     0,     0,   181,   182,     0,   205,     0,     0,
       0,     0,     0,     0,   208,   209,     0,   210,     0,     0,
     173,   188,     0,     0,   190,   106,   169,   170,   121,     0,
     163,     0,     0,    34,    63,     0,    42,    79,   317,   318,
     319,   320,   321,   323,   324,   325,   326,   294,     0,   295,
     296,   297,   298,   299,   322,   260,   316,   315,   214,   258,
       0,   110,     0,   107,     0,     0,     0,    93,    95,     0,
       0,     0,   285,   284,     0,     0,     0,     0,     0,     0,
       0,   196,   212,   211,   197,   206,   206,   168,   167,    75,
     184,    47,     0,   305,   109,   111,   112,     0,    97,     0,
     247,   288,   287,     0,     0,   201,     0,     0,   193,   195,
       0,   207,     0,    80,   113,    98,   191,   198,     0,   202,
       0,     0,     0,     0,     0,   194,   204,   203,   192,   200,
     199
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -392,  -392,  -392,    19,    -1,   -23,  -392,   285,  -392,  -392,
    -392,  -392,  -392,  -392,  -392,  -392,  -392,   -56,   336,   261,
     258,  -392,  -392,   115,  -392,   356,  -392,  -392,  -392,  -392,
    -392,  -392,  -124,  -392,  -392,   369,  -110,  -392,    66,  -256,
     -20,  -317,  -391,   -52,   198,  -392,  -392,   364,  -206,  -392,
      11,   480,  -392,  -318,  -125,  -392,   142,  -392,  -325,  -392,
    -392,  -392,  -392,  -392,   -36,  -392,  -170,   -94,  -392,  -242,
     -11,  -109,  -142,  -392,   242,  -392,  -392,   631,  -215,  -392,
       7,  -392,  -392
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    23,   338,   339,    26,    27,    36,    28,    61,
     205,    60,    65,    64,    63,   364,    62,   123,   135,   136,
     215,   133,   209,   210,   124,   125,   126,   358,   127,    29,
     217,   542,   128,    53,    54,    55,   270,   271,   272,    56,
     147,   420,   421,    58,    59,   102,   193,   372,   352,   353,
     354,   129,   114,   340,   341,   359,   342,   343,   344,   345,
     570,   346,   347,   348,   560,   349,   350,   263,   303,   365,
     186,   187,   383,   265,   266,   188,   189,   373,   384,   385,
     386,   190,   191
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      25,   203,    52,   184,   112,    57,   131,   459,   211,   419,
     579,   371,   262,   387,   388,   389,   390,   391,   109,   185,
      24,   195,   197,   473,   109,   471,   424,   109,   513,   526,
     -30,   106,    33,    34,   477,   -31,    31,    32,   237,    46,
     264,    46,   141,    46,   143,   416,    47,   105,   -30,    46,
      37,    38,    47,   105,   416,   -30,   235,   527,   -31,    25,
     -31,    25,    41,    42,   262,   239,   240,   241,   242,   243,
     244,   245,   246,   304,   113,   305,   306,   307,    66,   122,
     238,   122,   110,   425,   513,   426,   462,   111,   110,   185,
      35,   110,   393,   111,   452,   475,   111,    51,   418,   510,
      45,  -172,    46,    51,   367,    47,   105,   418,    39,   474,
     533,   435,   403,   403,   107,   580,   308,   309,   310,   201,
      43,   202,   103,    25,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   382,   382,   382,   382,   382,   382,   195,
     453,    49,   195,   122,   195,   531,    50,   535,   536,   360,
     104,   534,   481,   416,   115,   116,    51,   519,   108,   367,
     419,   355,   356,   468,   367,   367,   367,   367,   367,   367,
     367,   367,   130,   367,   367,   367,   367,   367,   367,   367,
     367,   367,   367,   403,   134,   117,   118,   119,   132,   403,
      49,   523,   351,   362,   363,    50,   397,   398,   273,   274,
     399,   400,   366,   137,    25,   140,   418,   401,   402,   446,
     403,   404,   559,   447,   448,   382,   351,   454,   455,   367,
     207,   208,   450,   451,   122,   287,   288,   289,   290,   291,
     287,   288,   289,   290,   291,   566,   567,   211,   138,   569,
     139,   292,   293,   294,   295,   296,   297,   298,   299,   300,
     301,   199,   302,   576,   577,   578,   192,   366,   289,   290,
     291,   480,   427,   428,   429,   430,   431,   432,   433,   434,
     145,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   198,   403,   553,   403,   554,   524,   204,   525,   206,
     528,   529,   403,   557,   403,   558,   509,   403,   574,    40,
      44,   142,   144,   212,   213,   214,   113,   218,   485,   508,
     219,   220,   221,   222,   223,   224,    52,   366,   225,   226,
     227,   228,   229,   230,   512,   231,   311,   232,    52,   233,
     236,   476,   185,   395,   369,   456,   406,   407,   408,   409,
     410,   411,   412,   413,   414,   256,   257,   258,   357,   361,
     423,   405,   449,   457,   458,   259,   460,   351,   461,   463,
     464,   466,   465,    25,   469,   561,   561,   472,   237,   470,
     478,   483,   273,   274,   275,   276,   277,   278,   415,   479,
     486,   355,   416,   122,   417,   487,   568,   488,   489,   490,
     491,   514,   492,   520,   493,   498,   509,   285,   286,   287,
     288,   289,   290,   291,   382,   548,   494,   495,   496,   497,
     367,   499,   515,   500,   501,   502,   503,   563,   504,    49,
     547,   185,   505,   112,    50,   506,   507,   521,   516,   522,
     530,   532,   539,   540,   541,   418,   549,   551,   544,   565,
     273,   274,   275,   276,   552,   575,   148,   149,   150,   151,
     152,   153,   154,   155,   156,   185,   545,   555,   556,   564,
     202,   157,   573,   571,   572,   285,   286,   287,   288,   289,
     290,   291,   403,   216,   370,   368,   484,   146,   351,   194,
     200,    30,   158,   159,   160,   161,   162,   163,   164,   165,
     538,   166,   518,   167,   168,   169,   170,   171,   172,   173,
     562,   482,     0,   174,   175,   543,     0,   422,   550,     0,
     148,   149,   150,   151,   152,   153,   154,   155,   156,     0,
       0,     0,     0,     0,     0,   157,     0,     0,     0,   176,
       0,     0,   177,   178,   179,     0,     0,     0,     0,     0,
       0,   180,   181,     0,   182,     0,   158,   159,   160,   161,
     162,   163,   164,   165,   196,   166,     0,   167,   168,   169,
     170,   171,   172,   173,     0,     0,     0,   174,   175,     0,
       0,     0,     0,     0,   148,   149,   150,   151,   152,   153,
     154,   155,   156,     0,     0,     0,     0,     0,     0,   157,
       0,     0,     0,   176,     0,     0,   177,   178,   179,     0,
       0,     0,     0,     0,     0,   180,   181,     0,   182,     0,
     158,   159,   160,   161,   162,   163,   164,   165,   511,   166,
       0,   167,   168,   169,   170,   171,   172,   173,     0,     0,
       0,   174,   175,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   273,
     274,   275,   276,   277,   278,     0,     0,   176,     0,     0,
     177,   178,   179,     0,     0,     0,     0,     0,     0,   180,
     181,     0,   182,   284,   285,   286,   287,   288,   289,   290,
     291,   312,   546,   313,   314,   315,   316,   317,   318,   319,
     320,   321,    13,    14,    15,     0,     0,     0,   157,    16,
      17,    18,    19,    20,     0,     0,   322,     0,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   158,
     159,   160,   161,   162,   163,   334,   165,     0,   166,     0,
     335,   336,   169,   170,   171,   172,   173,     0,     0,     0,
     174,   175,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,     0,     0,     0,     0,    16,    17,
      18,    19,    20,     0,     0,     0,   176,     0,     0,   177,
     178,   179,     0,     0,     0,     0,     0,     0,   180,   181,
       0,   182,     0,     0,    21,     0,   337,  -185,   202,   312,
     121,   313,   314,   315,   316,   317,   318,   319,   320,   321,
      13,    14,    15,     0,     0,     0,   157,    16,    17,    18,
      19,    20,     0,     0,   322,     0,   323,   324,   325,   326,
     327,   328,   329,   330,   331,   332,   333,   158,   159,   160,
     161,   162,   163,   334,   165,     0,   166,     0,   335,   336,
     169,   170,   171,   172,   173,     0,     0,     0,   174,   175,
     374,   375,   376,   377,   378,   379,   380,   381,     0,     0,
       0,     0,     0,     0,   392,     0,     0,   394,     0,   396,
       0,     0,     0,     0,   176,     0,     0,   177,   178,   179,
       0,     0,     0,     0,     0,     0,   180,   181,     0,   182,
       0,     0,     0,     0,   337,  -186,   202,   312,     0,   313,
     314,   315,   316,   317,   318,   319,   320,   321,    13,    14,
      15,     0,     0,     0,   157,    16,    17,    18,    19,    20,
       0,     0,   322,     0,   323,   324,   325,   326,   327,   328,
     329,   330,   331,   332,   333,   158,   159,   160,   161,   162,
     163,   334,   165,     0,   166,     0,   335,   336,   169,   170,
     171,   172,   173,     0,     0,     0,   174,   175,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   148,
     149,   150,   151,   152,   153,   154,   155,   156,     0,     0,
       0,     0,   176,     0,   157,   177,   178,   179,     0,     0,
       0,     0,     0,     0,   180,   181,     0,   182,     0,     0,
       0,     0,   337,     0,   202,   158,   159,   160,   161,   162,
     163,   164,   165,     0,   166,     0,   167,   168,   169,   170,
     171,   172,   173,     0,     0,     0,   174,   175,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   148,
     149,   150,   151,   152,   153,   154,   155,   156,     0,     0,
       0,     0,   176,     0,   157,   177,   178,   179,     0,     0,
       0,     0,     0,     0,   180,   181,   267,   182,   268,     0,
       0,     0,     0,   269,   183,   158,   159,   160,   161,   162,
     163,   164,   165,     0,   166,     0,   167,   168,   169,   170,
     171,   172,   173,     0,     0,     0,   174,   175,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   148,
     149,   150,   151,   152,   153,   154,   155,   156,     0,     0,
       0,     0,   176,     0,   157,   177,   178,   179,     0,     0,
       0,     0,     0,     0,   180,   181,   267,   182,   268,     0,
       0,     0,     0,   517,   183,   158,   159,   160,   161,   162,
     163,   164,   165,     0,   166,     0,   167,   168,   169,   170,
     171,   172,   173,     0,     0,     0,   174,   175,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   176,     0,     0,   177,   178,   179,     0,     0,
       0,     0,     0,     0,   180,   181,     0,   182,     0,     0,
       0,     0,     0,     0,   183,   313,   314,   315,   316,   317,
     318,   319,   320,   321,    13,    14,    15,     0,     0,     0,
     157,    16,    17,    18,    19,    20,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   158,   159,   160,   161,   162,   163,   334,   165,     0,
     166,     0,   167,   336,   169,   170,   171,   172,   173,     0,
       0,     0,   174,   175,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   148,   149,   150,   151,   152,   153,
     154,   155,   156,     0,     0,     0,     0,     0,   176,   157,
       0,   177,   178,   179,     0,     0,     0,     0,     0,     0,
     180,   181,     0,   182,     0,     0,     0,     0,   337,     0,
     158,   159,   160,   161,   162,   163,   164,   165,     0,   166,
       0,   167,   168,   169,   170,   171,   172,   173,     0,     0,
       0,   174,   175,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   148,   149,   150,   151,   152,   153,   154,
     155,   156,     0,     0,     0,     0,     0,   176,   157,     0,
     177,   178,   179,     0,     0,     0,     0,     0,     0,   180,
     181,     0,   182,     0,     0,     0,     0,   467,     0,   158,
     159,   160,   161,   162,   163,   164,   165,     0,   166,     0,
     167,   168,   169,   170,   171,   172,   173,     0,     0,     0,
     174,   175,     0,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,     0,     0,     0,     0,    16,
      17,    18,    19,    20,     0,     0,   176,     0,     0,   177,
     178,   179,   273,   274,   275,   276,   277,   278,   180,   181,
       0,   182,     0,     0,     0,    21,   337,    46,     0,   416,
      47,    48,     0,     0,   282,   283,   284,   285,   286,   287,
     288,   289,   290,   291,     0,     0,     0,     0,   247,   248,
     249,   250,   251,   252,   253,   254,   255,   256,   257,   258,
       0,     0,     0,   157,     0,     0,    49,   259,     0,     0,
       0,    50,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    51,   418,     0,   158,   159,   160,   161,   162,   163,
     260,   165,     0,   166,     0,   167,   261,   169,   170,   171,
     172,   173,     0,     0,     0,   174,   175,     0,     0,     0,
       0,   148,   149,   150,   151,   152,   153,   154,   155,   156,
       0,     0,     0,     0,     0,     0,   157,     0,     0,     0,
       0,   176,     0,     0,   177,   178,   179,     0,     0,     0,
       0,     0,     0,   180,   181,     0,   182,   158,   159,   160,
     161,   162,   163,   164,   165,     0,   166,     0,   167,   168,
     169,   170,   171,   172,   173,     0,     0,     0,   174,   175,
       0,     0,     0,     0,   148,   149,   150,   151,   152,   153,
     154,   155,   156,     0,     0,     0,     0,     0,     0,   157,
       0,     0,     0,     0,   176,     0,     0,   177,   178,   179,
       0,     0,     0,     0,     0,     0,   180,   181,     0,   234,
     158,   159,   160,   161,   162,   163,   164,   165,     0,   166,
       0,   167,   168,   169,   170,   171,   172,   173,     0,     0,
       0,   174,   175,     0,     0,     0,     0,   148,   149,   150,
     151,   152,   153,   154,   155,   156,     0,     0,     0,     0,
       0,     0,   157,     0,     0,     0,     0,   176,     0,     0,
     177,   178,   179,     0,     0,     0,     0,     0,     0,   180,
     181,     0,   182,   158,   159,   160,   161,   162,   163,   164,
     165,     0,   166,     0,   167,   168,   169,   170,   171,   172,
     173,     0,     0,     0,   174,   175,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,     0,     0,
       0,     0,    16,    17,    18,    19,    20,     0,     0,     0,
       0,     0,     0,     0,   157,     0,     0,     0,     0,     0,
       0,     0,   180,   181,     0,   182,     0,     0,    21,     0,
      46,     0,     0,    47,    48,   158,   159,   160,   161,   162,
     163,     0,   165,     0,   166,     0,   167,     0,   169,   170,
     171,   172,   173,     0,     0,     0,   174,   175,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    49,
       0,     0,     0,     0,    50,     0,     0,     0,     0,     0,
       0,     0,   176,     0,    51,   177,   178,   179,     0,     0,
       0,     0,     0,     0,   180,   181,     0,   182,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
       0,     0,     0,     0,    16,    17,    18,    19,    20,     0,
       0,     0,     2,     3,     0,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,     0,     0,     0,
      21,    16,    17,    18,    19,    20,   121,     0,     0,     0,
       0,     0,     0,   537,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    21,     0,     0,
       0,     0,     0,    22,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,   117,   118,   119,     0,
      16,    17,    18,    19,    20,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    21,     0,     0,     0,
       0,   120,   121,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,     0,    87,     0,     0,    88,    89,    90,
      91,    92,    93,    94,    95,    96,    97,     0,     0,     0,
       0,    98,    99,     0,   100,   101,   273,   274,   275,   276,
     277,   278,   279,   280,     0,     0,   273,   274,   275,   276,
     277,   278,   279,     0,     0,     0,   281,     0,   282,   283,
     284,   285,   286,   287,   288,   289,   290,   291,   282,   283,
     284,   285,   286,   287,   288,   289,   290,   291,   273,   274,
     275,   276,   277,   278,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   283,   284,   285,   286,   287,   288,   289,   290,   291
};

static const yytype_int16 yycheck[] =
{
       1,   126,    25,   113,    56,    25,    62,   325,   132,   265,
       1,   217,   182,   228,   229,   230,   231,   232,    22,   113,
       1,   115,   116,   348,    22,   343,   268,    22,   419,     1,
      83,    51,    50,    51,   351,    83,   106,   107,    59,    47,
     182,    47,    50,    47,    50,    49,    50,    51,   108,    47,
      50,    51,    50,    51,    49,   108,   165,    29,   108,    60,
     108,    62,    50,    51,   234,   174,   175,   176,   177,   178,
     179,   180,   181,    57,    81,    59,    60,    61,    51,    60,
     101,    62,    86,   107,   475,   109,   328,    91,    86,   183,
     108,    86,   234,    91,   309,   351,    91,   101,   102,   416,
      59,   108,    47,   101,   213,    50,    51,   102,   108,   106,
     106,   281,   109,   109,   106,   106,   100,   101,   102,   106,
     108,   108,    59,   124,   218,   219,   220,   221,   222,   223,
     224,   225,   226,   227,   228,   229,   230,   231,   232,   233,
     310,    86,   236,   124,   238,   463,    91,   472,   473,   205,
      59,   469,   358,    49,   101,   102,   101,    83,   109,   268,
     416,   109,   110,   333,   273,   274,   275,   276,   277,   278,
     279,   280,   108,   282,   283,   284,   285,   286,   287,   288,
     289,   290,   291,   109,    50,    15,    16,    17,    83,   109,
      86,   111,   193,    50,    51,    91,    50,    51,    62,    63,
      50,    51,   213,   108,   205,   111,   102,    50,    51,   303,
     109,   110,   530,    50,    51,   309,   217,   106,   107,   328,
      50,    51,    50,    51,   205,    89,    90,    91,    92,    93,
      89,    90,    91,    92,    93,   553,   554,   361,   101,   557,
     110,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,   107,    81,   571,   572,   573,   108,   268,    91,    92,
      93,   355,   273,   274,   275,   276,   277,   278,   279,   280,
     110,   282,   283,   284,   285,   286,   287,   288,   289,   290,
     291,   101,   109,   110,   109,   110,   456,    83,   458,   107,
     460,   461,   109,   110,   109,   110,   405,   109,   110,    14,
      15,   103,   104,   108,    81,   109,    81,   101,   364,   403,
     101,   101,   101,   101,   101,   101,   339,   328,   101,   101,
     101,   101,   101,   101,   418,   101,    55,   101,   351,   101,
     101,   351,   426,    50,   107,   101,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,   111,   109,
      50,   110,    50,   101,   101,    22,   101,   358,   101,    83,
     106,    50,   106,   364,    83,   535,   536,   348,    59,   107,
     110,   107,    62,    63,    64,    65,    66,    67,    45,   109,
     107,   109,    49,   364,    51,   110,   556,   110,   110,   110,
     110,   102,   110,    59,   110,   109,   505,    87,    88,    89,
      90,    91,    92,    93,   498,   515,   110,   110,   110,   110,
     519,   110,    81,   110,   110,   110,   110,   542,   110,    86,
     514,   515,   110,   475,    91,   110,   110,    59,   111,   110,
      83,   106,   110,   107,   107,   102,    81,    50,   110,   549,
      62,    63,    64,    65,    50,   570,     3,     4,     5,     6,
       7,     8,     9,    10,    11,   549,   111,   106,   101,   111,
     108,    18,    27,   110,   110,    87,    88,    89,    90,    91,
      92,    93,   109,   137,   216,   214,   361,   108,   479,   115,
     124,     1,    39,    40,    41,    42,    43,    44,    45,    46,
     479,    48,   426,    50,    51,    52,    53,    54,    55,    56,
     536,   359,    -1,    60,    61,   498,    -1,   265,   519,    -1,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    -1,    -1,    -1,    86,
      -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,
      -1,    98,    99,    -1,   101,    -1,    39,    40,    41,    42,
      43,    44,    45,    46,   111,    48,    -1,    50,    51,    52,
      53,    54,    55,    56,    -1,    -1,    -1,    60,    61,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    18,
      -1,    -1,    -1,    86,    -1,    -1,    89,    90,    91,    -1,
      -1,    -1,    -1,    -1,    -1,    98,    99,    -1,   101,    -1,
      39,    40,    41,    42,    43,    44,    45,    46,   111,    48,
      -1,    50,    51,    52,    53,    54,    55,    56,    -1,    -1,
      -1,    60,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    62,
      63,    64,    65,    66,    67,    -1,    -1,    86,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,    98,
      99,    -1,   101,    86,    87,    88,    89,    90,    91,    92,
      93,     1,   111,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    -1,    -1,    -1,    18,    19,
      20,    21,    22,    23,    -1,    -1,    26,    -1,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    -1,    48,    -1,
      50,    51,    52,    53,    54,    55,    56,    -1,    -1,    -1,
      60,    61,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    -1,    -1,    -1,    -1,    19,    20,
      21,    22,    23,    -1,    -1,    -1,    86,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    -1,    -1,    -1,    98,    99,
      -1,   101,    -1,    -1,    45,    -1,   106,   107,   108,     1,
      51,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    -1,    -1,    -1,    18,    19,    20,    21,
      22,    23,    -1,    -1,    26,    -1,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    -1,    48,    -1,    50,    51,
      52,    53,    54,    55,    56,    -1,    -1,    -1,    60,    61,
     219,   220,   221,   222,   223,   224,   225,   226,    -1,    -1,
      -1,    -1,    -1,    -1,   233,    -1,    -1,   236,    -1,   238,
      -1,    -1,    -1,    -1,    86,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    -1,    98,    99,    -1,   101,
      -1,    -1,    -1,    -1,   106,   107,   108,     1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    -1,    -1,    -1,    18,    19,    20,    21,    22,    23,
      -1,    -1,    26,    -1,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    45,    46,    -1,    48,    -1,    50,    51,    52,    53,
      54,    55,    56,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    86,    -1,    18,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    -1,    98,    99,    -1,   101,    -1,    -1,
      -1,    -1,   106,    -1,   108,    39,    40,    41,    42,    43,
      44,    45,    46,    -1,    48,    -1,    50,    51,    52,    53,
      54,    55,    56,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    86,    -1,    18,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    -1,    98,    99,   100,   101,   102,    -1,
      -1,    -1,    -1,   107,   108,    39,    40,    41,    42,    43,
      44,    45,    46,    -1,    48,    -1,    50,    51,    52,    53,
      54,    55,    56,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    -1,    -1,
      -1,    -1,    86,    -1,    18,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    -1,    98,    99,   100,   101,   102,    -1,
      -1,    -1,    -1,   107,   108,    39,    40,    41,    42,    43,
      44,    45,    46,    -1,    48,    -1,    50,    51,    52,    53,
      54,    55,    56,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    86,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    -1,    98,    99,    -1,   101,    -1,    -1,
      -1,    -1,    -1,    -1,   108,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    -1,    -1,    -1,
      18,    19,    20,    21,    22,    23,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    39,    40,    41,    42,    43,    44,    45,    46,    -1,
      48,    -1,    50,    51,    52,    53,    54,    55,    56,    -1,
      -1,    -1,    60,    61,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    86,    18,
      -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,
      98,    99,    -1,   101,    -1,    -1,    -1,    -1,   106,    -1,
      39,    40,    41,    42,    43,    44,    45,    46,    -1,    48,
      -1,    50,    51,    52,    53,    54,    55,    56,    -1,    -1,
      -1,    60,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    -1,    -1,    -1,    -1,    -1,    86,    18,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,    98,
      99,    -1,   101,    -1,    -1,    -1,    -1,   106,    -1,    39,
      40,    41,    42,    43,    44,    45,    46,    -1,    48,    -1,
      50,    51,    52,    53,    54,    55,    56,    -1,    -1,    -1,
      60,    61,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    -1,    -1,    -1,    -1,    19,
      20,    21,    22,    23,    -1,    -1,    86,    -1,    -1,    89,
      90,    91,    62,    63,    64,    65,    66,    67,    98,    99,
      -1,   101,    -1,    -1,    -1,    45,   106,    47,    -1,    49,
      50,    51,    -1,    -1,    84,    85,    86,    87,    88,    89,
      90,    91,    92,    93,    -1,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      -1,    -1,    -1,    18,    -1,    -1,    86,    22,    -1,    -1,
      -1,    91,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,   102,    -1,    39,    40,    41,    42,    43,    44,
      45,    46,    -1,    48,    -1,    50,    51,    52,    53,    54,
      55,    56,    -1,    -1,    -1,    60,    61,    -1,    -1,    -1,
      -1,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    -1,    -1,    -1,
      -1,    86,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,
      -1,    -1,    -1,    98,    99,    -1,   101,    39,    40,    41,
      42,    43,    44,    45,    46,    -1,    48,    -1,    50,    51,
      52,    53,    54,    55,    56,    -1,    -1,    -1,    60,    61,
      -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    -1,    -1,    -1,    -1,    -1,    -1,    18,
      -1,    -1,    -1,    -1,    86,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    -1,    98,    99,    -1,   101,
      39,    40,    41,    42,    43,    44,    45,    46,    -1,    48,
      -1,    50,    51,    52,    53,    54,    55,    56,    -1,    -1,
      -1,    60,    61,    -1,    -1,    -1,    -1,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    -1,    -1,    -1,    -1,
      -1,    -1,    18,    -1,    -1,    -1,    -1,    86,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,    98,
      99,    -1,   101,    39,    40,    41,    42,    43,    44,    45,
      46,    -1,    48,    -1,    50,    51,    52,    53,    54,    55,
      56,    -1,    -1,    -1,    60,    61,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    -1,    -1,
      -1,    -1,    19,    20,    21,    22,    23,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    18,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    98,    99,    -1,   101,    -1,    -1,    45,    -1,
      47,    -1,    -1,    50,    51,    39,    40,    41,    42,    43,
      44,    -1,    46,    -1,    48,    -1,    50,    -1,    52,    53,
      54,    55,    56,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,
      -1,    -1,    -1,    -1,    91,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    86,    -1,   101,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    -1,    98,    99,    -1,   101,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      -1,    -1,    -1,    -1,    19,    20,    21,    22,    23,    -1,
      -1,    -1,     0,     1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    -1,    -1,    -1,
      45,    19,    20,    21,    22,    23,    51,    -1,    -1,    -1,
      -1,    -1,    -1,    58,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,
      -1,    -1,    -1,    51,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    -1,
      19,    20,    21,    22,    23,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,    -1,
      -1,    50,    51,    60,    61,    62,    63,    64,    65,    66,
      67,    68,    69,    70,    71,    72,    73,    74,    75,    76,
      77,    78,    79,    -1,    81,    -1,    -1,    84,    85,    86,
      87,    88,    89,    90,    91,    92,    93,    -1,    -1,    -1,
      -1,    98,    99,    -1,   101,   102,    62,    63,    64,    65,
      66,    67,    68,    69,    -1,    -1,    62,    63,    64,    65,
      66,    67,    68,    -1,    -1,    -1,    82,    -1,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    93,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    93,    62,    63,
      64,    65,    66,    67,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    85,    86,    87,    88,    89,    90,    91,    92,    93
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   113,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    19,    20,    21,    22,
      23,    45,    51,   114,   115,   116,   117,   118,   120,   141,
     163,   106,   107,    50,    51,   108,   119,    50,    51,   108,
     119,    50,    51,   108,   119,    59,    47,    50,    51,    86,
      91,   101,   117,   145,   146,   147,   151,   152,   155,   156,
     123,   121,   128,   126,   125,   124,    51,    60,    61,    62,
      63,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,    75,    76,    77,    78,    79,    81,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    93,    98,    99,
     101,   102,   157,    59,    59,    51,   152,   106,   109,    22,
      86,    91,   155,    81,   164,   101,   102,    15,    16,    17,
      50,    51,   115,   129,   136,   137,   138,   140,   144,   163,
     108,   129,    83,   133,    50,   130,   131,   108,   101,   110,
     111,    50,   156,    50,   156,   110,   147,   152,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    18,    39,    40,
      41,    42,    43,    44,    45,    46,    48,    50,    51,    52,
      53,    54,    55,    56,    60,    61,    86,    89,    90,    91,
      98,    99,   101,   108,   148,   179,   182,   183,   187,   188,
     193,   194,   108,   158,   159,   179,   111,   179,   101,   107,
     137,   106,   108,   166,    83,   122,   107,    50,    51,   134,
     135,   144,   108,    81,   109,   132,   130,   142,   101,   101,
     101,   101,   101,   101,   101,   101,   101,   101,   101,   101,
     101,   101,   101,   101,   101,   183,   101,    59,   101,   183,
     183,   183,   183,   183,   183,   183,   183,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    22,
      45,    51,   178,   179,   184,   185,   186,   100,   102,   107,
     148,   149,   150,    62,    63,    64,    65,    66,    67,    68,
      69,    82,    84,    85,    86,    87,    88,    89,    90,    91,
      92,    93,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    81,   180,    57,    59,    60,    61,   100,   101,
     102,    55,     1,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    26,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    45,    50,    51,   106,   115,   116,
     165,   166,   168,   169,   170,   171,   173,   174,   175,   177,
     178,   116,   160,   161,   162,   109,   110,   111,   139,   167,
     129,   109,    50,    51,   127,   181,   182,   183,   131,   107,
     132,   160,   159,   189,   189,   189,   189,   189,   189,   189,
     189,   189,   179,   184,   190,   191,   192,   190,   190,   190,
     190,   190,   189,   184,   189,    50,   189,    50,    51,    50,
      51,    50,    51,   109,   110,   110,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    45,    49,    51,   102,   151,
     153,   154,   186,    50,   181,   107,   109,   182,   182,   182,
     182,   182,   182,   182,   182,   178,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   179,    50,    51,    50,
      50,    51,   190,   178,   106,   107,   101,   101,   101,   165,
     101,   101,   181,    83,   106,   106,    50,   106,   178,    83,
     107,   165,   115,   170,   106,   151,   152,   153,   110,   109,
     179,   160,   168,   107,   135,   129,   107,   110,   110,   110,
     110,   110,   110,   110,   110,   110,   110,   110,   109,   110,
     110,   110,   110,   110,   110,   110,   110,   110,   179,   183,
     153,   111,   179,   154,   102,    81,   111,   107,   150,    83,
      59,    59,   110,   111,   178,   178,     1,    29,   178,   178,
      83,   165,   106,   106,   165,   170,   170,    58,   162,   110,
     107,   107,   143,   192,   110,   111,   111,   179,   148,    81,
     182,    50,    50,   110,   110,   106,   101,   110,   110,   165,
     176,   178,   176,   166,   111,   148,   165,   165,   178,   165,
     172,   110,   110,    27,   110,   166,   165,   165,   165,     1,
     106
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   112,   113,   113,   114,   114,   114,   114,   114,   115,
     116,   116,   117,   117,   117,   117,   117,   117,   118,   118,
     118,   118,   118,   118,   118,   118,   118,   118,   118,   118,
     119,   119,   121,   122,   120,   123,   120,   120,   120,   120,
     120,   124,   120,   125,   120,   126,   127,   120,   128,   120,
     120,   120,   129,   129,   130,   130,   131,   131,   132,   132,
     133,   133,   134,   134,   135,   135,   135,   135,   136,   136,
     137,   137,   137,   137,   139,   138,   140,   140,   142,   143,
     141,   144,   144,   144,   145,   145,   146,   146,   147,   147,
     148,   148,   148,   148,   149,   149,   150,   150,   150,   151,
     151,   151,   151,   151,   152,   152,   153,   153,   153,   154,
     154,   154,   154,   154,   155,   155,   155,   155,   155,   155,
     155,   155,   155,   155,   155,   156,   157,   157,   157,   157,
     157,   157,   157,   157,   157,   157,   157,   157,   157,   157,
     157,   157,   157,   157,   157,   157,   157,   157,   157,   157,
     157,   157,   157,   157,   157,   157,   157,   157,   157,   157,
     157,   158,   159,   159,   160,   160,   161,   161,   161,   162,
     162,   162,   164,   163,   165,   165,   165,   165,   165,   165,
     165,   165,   165,   167,   166,   168,   168,   169,   169,   170,
     170,   171,   171,   172,   171,   173,   173,   173,   174,   174,
     174,   174,   174,   174,   174,   175,   176,   176,   177,   177,
     177,   177,   177,   178,   178,   179,   179,   180,   180,   180,
     180,   180,   180,   180,   180,   180,   180,   180,   181,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   183,
     183,   183,   183,   183,   183,   183,   183,   183,   183,   183,
     183,   184,   184,   185,   185,   186,   186,   186,   186,   186,
     186,   186,   186,   186,   186,   186,   186,   186,   186,   186,
     186,   186,   186,   187,   187,   187,   187,   187,   187,   187,
     187,   187,   187,   187,   188,   188,   188,   188,   188,   188,
     189,   189,   190,   190,   191,   191,   192,   192,   193,   193,
     193,   193,   193,   193,   193,   193,   193,   193,   193,   193,
     193,   193,   193,   193,   193,   193,   193,   193,   193,   194,
     194
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     1,     2,     2,     3,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     0,     0,     7,     0,     5,     2,     2,     2,
       2,     0,     7,     0,     6,     0,     0,     8,     0,     5,
       2,     2,     0,     1,     1,     3,     1,     3,     0,     1,
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
       1,     1,     1,     1,     1,     1,     1,     2,     2,     2,
       2,     2,     2,     1,     4,     4,     3,     5,     5,     3,
       3,     2,     2,     1,     4,     4,     4,     4,     4,     4,
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
#line 2438 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 143 "src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2448 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 151 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2454 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 152 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2460 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: out_of_class_special  */
#line 153 "src/parser.y"
                           { yyval.node = yyvsp[0].node; }
#line 2466 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error ';'  */
#line 154 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2472 "build/parser.tab.cpp"
    break;

  case 8: /* external_decl: error '}'  */
#line 155 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2478 "build/parser.tab.cpp"
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
#line 2511 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 190 "src/parser.y"
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
#line 2529 "build/parser.tab.cpp"
    break;

  case 11: /* declaration_specifiers: storage_or_type_specifier  */
#line 203 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2535 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: STATIC  */
#line 207 "src/parser.y"
               { yyval.typeSpec.isStatic = true; yyval.typeSpec.storageClasses = 1; }
#line 2541 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: AUTO  */
#line 208 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isAuto = true; }
#line 2547 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: TYPEDEF  */
#line 209 "src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; yyval.typeSpec.storageClasses = 1; }
#line 2553 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: CONST  */
#line 210 "src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2559 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: FRIEND  */
#line 211 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isFriend = true; }
#line 2565 "build/parser.tab.cpp"
    break;

  case 17: /* storage_or_type_specifier: type_specifier  */
#line 212 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2571 "build/parser.tab.cpp"
    break;

  case 18: /* type_specifier: INT  */
#line 216 "src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); g_afterTypeKeyword = true; }
#line 2577 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: CHAR  */
#line 217 "src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); g_afterTypeKeyword = true; }
#line 2583 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: FLOAT  */
#line 218 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); g_afterTypeKeyword = true; }
#line 2589 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: DOUBLE  */
#line 219 "src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); g_afterTypeKeyword = true; }
#line 2595 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: VOID  */
#line 220 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); g_afterTypeKeyword = true; }
#line 2601 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: BOOL  */
#line 221 "src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); g_afterTypeKeyword = true; }
#line 2607 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: SHORT  */
#line 222 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); g_afterTypeKeyword = true; }
#line 2613 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: LONG  */
#line 223 "src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); g_afterTypeKeyword = true; }
#line 2619 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: SIGNED  */
#line 224 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); g_afterTypeKeyword = true; }
#line 2625 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: UNSIGNED  */
#line 225 "src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); g_afterTypeKeyword = true; }
#line 2631 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: TYPE_NAME  */
#line 226 "src/parser.y"
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
#line 2650 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: struct_or_class_specifier  */
#line 240 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2656 "build/parser.tab.cpp"
    break;

  case 30: /* tag_name: IDENTIFIER  */
#line 247 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2662 "build/parser.tab.cpp"
    break;

  case 31: /* tag_name: TYPE_NAME  */
#line 248 "src/parser.y"
                 { yyval = yyvsp[0]; }
#line 2668 "build/parser.tab.cpp"
    break;

  case 32: /* $@1: %empty  */
#line 252 "src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str, "struct");
      }
#line 2678 "build/parser.tab.cpp"
    break;

  case 33: /* $@2: %empty  */
#line 256 "src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); markAggregateMemberDepth(); }
#line 2684 "build/parser.tab.cpp"
    break;

  case 34: /* struct_or_class_specifier: STRUCT tag_name $@1 '{' $@2 member_decl_list_opt '}'  */
#line 256 "src/parser.y"
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
#line 2702 "build/parser.tab.cpp"
    break;

  case 35: /* @3: %empty  */
#line 272 "src/parser.y"
                 {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "struct");
          pushScope("struct " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2714 "build/parser.tab.cpp"
    break;

  case 36: /* struct_or_class_specifier: STRUCT '{' @3 member_decl_list_opt '}'  */
#line 278 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::StructDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2727 "build/parser.tab.cpp"
    break;

  case 37: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 286 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2738 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 292 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2749 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: ENUM IDENTIFIER  */
#line 298 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2760 "build/parser.tab.cpp"
    break;

  case 40: /* struct_or_class_specifier: ENUM TYPE_NAME  */
#line 304 "src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2771 "build/parser.tab.cpp"
    break;

  case 41: /* $@4: %empty  */
#line 310 "src/parser.y"
                    {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM");
      }
#line 2780 "build/parser.tab.cpp"
    break;

  case 42: /* struct_or_class_specifier: ENUM tag_name $@4 '{' enumerator_list comma_opt '}'  */
#line 313 "src/parser.y"
                                          {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-5].str;
          addTypeName(yyvsp[-5].str);
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-5].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2793 "build/parser.tab.cpp"
    break;

  case 43: /* @5: %empty  */
#line 321 "src/parser.y"
               {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[-1].idx});
      }
#line 2802 "build/parser.tab.cpp"
    break;

  case 44: /* struct_or_class_specifier: ENUM '{' @5 enumerator_list comma_opt '}'  */
#line 324 "src/parser.y"
                                      {
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[-3].str;
          auto node = atToken(mkNode(ASTKind::EnumDecl, yyvsp[-3].str), yyvsp[-5].idx);
          for (auto &e : yyvsp[-2].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2814 "build/parser.tab.cpp"
    break;

  case 45: /* $@6: %empty  */
#line 331 "src/parser.y"
                     {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str, "class");
      }
#line 2824 "build/parser.tab.cpp"
    break;

  case 46: /* $@7: %empty  */
#line 335 "src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); markAggregateMemberDepth(); }
#line 2830 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: CLASS tag_name $@6 inheritance_opt '{' $@7 member_decl_list_opt '}'  */
#line 335 "src/parser.y"
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
#line 2847 "build/parser.tab.cpp"
    break;

  case 48: /* @8: %empty  */
#line 347 "src/parser.y"
                {
          yyval.str = anonymousTagAt(yyvsp[-1].idx);
          declareSymbol(yyval.str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[-1].idx});
          enterClass(yyval.str, "class");
          pushScope("class " + yyval.str);
          markAggregateMemberDepth();
      }
#line 2859 "build/parser.tab.cpp"
    break;

  case 49: /* struct_or_class_specifier: CLASS '{' @8 member_decl_list_opt '}'  */
#line 353 "src/parser.y"
                                 {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[-2].str;
          auto node = atToken(mkNode(ASTKind::ClassDecl, yyvsp[-2].str), yyvsp[-4].idx);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2872 "build/parser.tab.cpp"
    break;

  case 50: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 361 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2883 "build/parser.tab.cpp"
    break;

  case 51: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 367 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 2894 "build/parser.tab.cpp"
    break;

  case 52: /* member_decl_list_opt: %empty  */
#line 376 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2900 "build/parser.tab.cpp"
    break;

  case 53: /* member_decl_list_opt: member_decl_list  */
#line 377 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2906 "build/parser.tab.cpp"
    break;

  case 54: /* enumerator_list: enumerator  */
#line 384 "src/parser.y"
                 { yyval.nodeList.push_back(yyvsp[0].node); }
#line 2912 "build/parser.tab.cpp"
    break;

  case 55: /* enumerator_list: enumerator_list ',' enumerator  */
#line 385 "src/parser.y"
                                     { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 2918 "build/parser.tab.cpp"
    break;

  case 56: /* enumerator: IDENTIFIER  */
#line 389 "src/parser.y"
                 {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[0].str), yyvsp[0].idx);
      }
#line 2928 "build/parser.tab.cpp"
    break;

  case 57: /* enumerator: IDENTIFIER '=' constant_expr  */
#line 394 "src/parser.y"
                                   {
          declareSymbol(yyvsp[-2].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "ENUM_CONSTANT");
          yyval.node = atToken(mkNode(ASTKind::Enumerator, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 2938 "build/parser.tab.cpp"
    break;

  case 58: /* comma_opt: %empty  */
#line 402 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2944 "build/parser.tab.cpp"
    break;

  case 59: /* comma_opt: ','  */
#line 403 "src/parser.y"
          { yyval = ParserValue(); }
#line 2950 "build/parser.tab.cpp"
    break;

  case 60: /* inheritance_opt: %empty  */
#line 407 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2956 "build/parser.tab.cpp"
    break;

  case 61: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 408 "src/parser.y"
                                     { yyval.str = yyvsp[0].str; yyval.bases = yyvsp[0].bases; }
#line 2962 "build/parser.tab.cpp"
    break;

  case 62: /* inheritance_specifier_list: inheritance_specifier  */
#line 412 "src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2968 "build/parser.tab.cpp"
    break;

  case 63: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 413 "src/parser.y"
                                                           {
          yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str;
          for (auto &b : yyvsp[0].bases) yyval.bases.push_back(b);
      }
#line 2977 "build/parser.tab.cpp"
    break;

  case 64: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 420 "src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2988 "build/parser.tab.cpp"
    break;

  case 65: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 426 "src/parser.y"
                                 {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{yyvsp[-1].str, yyvsp[0].str}};
      }
#line 2999 "build/parser.tab.cpp"
    break;

  case 66: /* inheritance_specifier: IDENTIFIER  */
#line 432 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3010 "build/parser.tab.cpp"
    break;

  case 67: /* inheritance_specifier: TYPE_NAME  */
#line 438 "src/parser.y"
                {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
          yyval.bases = {{"", yyvsp[0].str}};
      }
#line 3021 "build/parser.tab.cpp"
    break;

  case 68: /* member_decl_list: member_item  */
#line 449 "src/parser.y"
                  {
          yyval.str.clear();
          if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node);
          else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") yyval.str = yyvsp[0].str;
      }
#line 3031 "build/parser.tab.cpp"
    break;

  case 69: /* member_decl_list: member_decl_list member_item  */
#line 454 "src/parser.y"
                                   {
          yyval = yyvsp[-1];
          if (yyvsp[0].node) {
              if (!yyval.str.empty()) yyvsp[0].node->access = yyval.str;
              yyval.nodeList.push_back(yyvsp[0].node);
          } else if (yyvsp[0].str == "public" || yyvsp[0].str == "private" || yyvsp[0].str == "protected") {
              yyval.str = yyvsp[0].str;
          }
      }
#line 3045 "build/parser.tab.cpp"
    break;

  case 70: /* member_item: declaration  */
#line 466 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3051 "build/parser.tab.cpp"
    break;

  case 71: /* member_item: function_definition  */
#line 467 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 3057 "build/parser.tab.cpp"
    break;

  case 72: /* member_item: access_specifier ':'  */
#line 468 "src/parser.y"
                           { yyval = ParserValue(); yyval.str = yyvsp[-1].str; }
#line 3063 "build/parser.tab.cpp"
    break;

  case 73: /* member_item: constructor_def  */
#line 469 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3069 "build/parser.tab.cpp"
    break;

  case 74: /* $@9: %empty  */
#line 478 "src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 3075 "build/parser.tab.cpp"
    break;

  case 75: /* constructor_head: IDENTIFIER '(' $@9 parameter_list_opt ')'  */
#line 478 "src/parser.y"
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
      }
#line 3094 "build/parser.tab.cpp"
    break;

  case 76: /* constructor_def: constructor_head compound_stmt  */
#line 495 "src/parser.y"
                                     {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, currentClassName(), yyvsp[0].node);
      }
#line 3103 "build/parser.tab.cpp"
    break;

  case 77: /* constructor_def: constructor_head ';'  */
#line 499 "src/parser.y"
                           {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-1].str, yyvsp[-1].idx, yyvsp[-1].paramList, currentClassName(), nullptr);
      }
#line 3112 "build/parser.tab.cpp"
    break;

  case 78: /* $@10: %empty  */
#line 507 "src/parser.y"
                                        {
          setCategory(yyvsp[-3].idx, categoryForTypeName(lookupTypeSymbol(yyvsp[-3].str)));
          enterClass(yyvsp[-3].str);
          pushScope(yyvsp[-3].str + "::" + yyvsp[-1].str + "()");
      }
#line 3122 "build/parser.tab.cpp"
    break;

  case 79: /* $@11: %empty  */
#line 511 "src/parser.y"
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
#line 3139 "build/parser.tab.cpp"
    break;

  case 80: /* out_of_class_special: TYPE_NAME SCOPE_RES TYPE_NAME '(' $@10 parameter_list_opt ')' $@11 compound_stmt  */
#line 522 "src/parser.y"
                      {
          popScope();
          yyval.node = makeConstructorNode(yyvsp[-6].str, yyvsp[-6].idx, yyvsp[-3].paramList, yyvsp[-8].str, yyvsp[0].node);
          leaveClass();
      }
#line 3149 "build/parser.tab.cpp"
    break;

  case 84: /* init_declarator_list_opt: %empty  */
#line 537 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3155 "build/parser.tab.cpp"
    break;

  case 85: /* init_declarator_list_opt: init_declarator_list  */
#line 538 "src/parser.y"
                           { yyval = yyvsp[0]; }
#line 3161 "build/parser.tab.cpp"
    break;

  case 86: /* init_declarator_list: init_declarator  */
#line 542 "src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3167 "build/parser.tab.cpp"
    break;

  case 87: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 543 "src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); markDeclaratorList(); }
#line 3173 "build/parser.tab.cpp"
    break;

  case 88: /* init_declarator: declarator  */
#line 547 "src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 3179 "build/parser.tab.cpp"
    break;

  case 89: /* init_declarator: declarator '=' initializer  */
#line 548 "src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 3185 "build/parser.tab.cpp"
    break;

  case 90: /* initializer: assignment_expr  */
#line 552 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3191 "build/parser.tab.cpp"
    break;

  case 91: /* initializer: '{' '}'  */
#line 553 "src/parser.y"
              { yyval.node = atToken(mkNode(ASTKind::InitializerList), yyvsp[-1].idx); }
#line 3197 "build/parser.tab.cpp"
    break;

  case 92: /* initializer: '{' initializer_list '}'  */
#line 554 "src/parser.y"
                               {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-2].idx);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3207 "build/parser.tab.cpp"
    break;

  case 93: /* initializer: '{' initializer_list ',' '}'  */
#line 559 "src/parser.y"
                                   {
          auto n = atToken(mkNode(ASTKind::InitializerList), yyvsp[-3].idx);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 3217 "build/parser.tab.cpp"
    break;

  case 94: /* initializer_list: initializer_item  */
#line 567 "src/parser.y"
                       { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3223 "build/parser.tab.cpp"
    break;

  case 95: /* initializer_list: initializer_list ',' initializer_item  */
#line 568 "src/parser.y"
                                            { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3229 "build/parser.tab.cpp"
    break;

  case 96: /* initializer_item: initializer  */
#line 572 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3235 "build/parser.tab.cpp"
    break;

  case 97: /* initializer_item: '.' IDENTIFIER '=' initializer  */
#line 573 "src/parser.y"
                                     {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "." + yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 3243 "build/parser.tab.cpp"
    break;

  case 98: /* initializer_item: '[' constant_expr ']' '=' initializer  */
#line 576 "src/parser.y"
                                            {
          yyval.node = atToken(mkNode(ASTKind::DesignatedInit, "[]", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3251 "build/parser.tab.cpp"
    break;

  case 99: /* pointer: '*'  */
#line 582 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.ptrOps = "*"; }
#line 3257 "build/parser.tab.cpp"
    break;

  case 100: /* pointer: '&'  */
#line 583 "src/parser.y"
                       { yyval.decl.pointerLevel = 1; yyval.decl.isReference = true; yyval.decl.ptrOps = "&"; }
#line 3263 "build/parser.tab.cpp"
    break;

  case 101: /* pointer: pointer '*'  */
#line 584 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "*"; }
#line 3269 "build/parser.tab.cpp"
    break;

  case 102: /* pointer: pointer '&'  */
#line 585 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; yyval.decl.ptrOps += "&"; }
#line 3275 "build/parser.tab.cpp"
    break;

  case 103: /* pointer: pointer CONST  */
#line 586 "src/parser.y"
                       { yyval = yyvsp[-1]; yyval.decl.ptrOps += "c"; }
#line 3281 "build/parser.tab.cpp"
    break;

  case 104: /* declarator: pointer direct_declarator  */
#line 590 "src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3292 "build/parser.tab.cpp"
    break;

  case 105: /* declarator: direct_declarator  */
#line 596 "src/parser.y"
                        { yyval = yyvsp[0]; }
#line 3298 "build/parser.tab.cpp"
    break;

  case 106: /* abstract_declarator: pointer  */
#line 602 "src/parser.y"
              { yyval = yyvsp[0]; }
#line 3304 "build/parser.tab.cpp"
    break;

  case 107: /* abstract_declarator: pointer direct_abstract_declarator  */
#line 603 "src/parser.y"
                                         {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
          if (yyvsp[-1].decl.isReference) yyval.decl.isReference = true;
          yyval.decl.ptrOps = yyvsp[-1].decl.ptrOps + yyvsp[0].decl.ptrOps;
      }
#line 3315 "build/parser.tab.cpp"
    break;

  case 108: /* abstract_declarator: direct_abstract_declarator  */
#line 609 "src/parser.y"
                                 { yyval = yyvsp[0]; }
#line 3321 "build/parser.tab.cpp"
    break;

  case 109: /* direct_abstract_declarator: ABSTRACT_LPAREN abstract_declarator ')'  */
#line 613 "src/parser.y"
                                              {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3335 "build/parser.tab.cpp"
    break;

  case 110: /* direct_abstract_declarator: '[' ']'  */
#line 622 "src/parser.y"
              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(nullptr); }
#line 3341 "build/parser.tab.cpp"
    break;

  case 111: /* direct_abstract_declarator: '[' assignment_expr ']'  */
#line 623 "src/parser.y"
                              { yyval = ParserValue(); yyval.decl.arrayLevel = 1; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3347 "build/parser.tab.cpp"
    break;

  case 112: /* direct_abstract_declarator: direct_abstract_declarator '[' ']'  */
#line 624 "src/parser.y"
                                         { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3353 "build/parser.tab.cpp"
    break;

  case 113: /* direct_abstract_declarator: direct_abstract_declarator '[' assignment_expr ']'  */
#line 625 "src/parser.y"
                                                         { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3359 "build/parser.tab.cpp"
    break;

  case 114: /* direct_declarator: IDENTIFIER  */
#line 629 "src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3368 "build/parser.tab.cpp"
    break;

  case 115: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 633 "src/parser.y"
                                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3380 "build/parser.tab.cpp"
    break;

  case 116: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 640 "src/parser.y"
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
#line 3397 "build/parser.tab.cpp"
    break;

  case 117: /* direct_declarator: '(' declarator ')'  */
#line 652 "src/parser.y"
                         {
          yyval = yyvsp[-1];
          yyval.decl.wasParenGrouped = true;
          yyval.decl.grouped = true;
          yyval.decl.innerPointerLevel = yyvsp[-1].decl.pointerLevel;
          yyval.decl.innerArrayCount = static_cast<int>(yyvsp[-1].decl.arrayDims.size());
          yyval.decl.innerPtrOps = yyvsp[-1].decl.ptrOps;
          yyval.decl.ptrOps.clear();
      }
#line 3411 "build/parser.tab.cpp"
    break;

  case 118: /* direct_declarator: operator_function_id  */
#line 661 "src/parser.y"
                           {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 3420 "build/parser.tab.cpp"
    break;

  case 119: /* direct_declarator: IDENTIFIER SCOPE_RES operator_function_id  */
#line 665 "src/parser.y"
                                                {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3432 "build/parser.tab.cpp"
    break;

  case 120: /* direct_declarator: TYPE_NAME SCOPE_RES operator_function_id  */
#line 672 "src/parser.y"
                                               {
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3444 "build/parser.tab.cpp"
    break;

  case 121: /* direct_declarator: direct_declarator '(' param_scope parameter_list_opt ')'  */
#line 679 "src/parser.y"
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
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
#line 3467 "build/parser.tab.cpp"
    break;

  case 122: /* direct_declarator: direct_declarator '(' constructor_args ')'  */
#line 697 "src/parser.y"
                                                 {
          /* `Dog d(4);`: direct initialization (or a constructor call) */
          yyval = yyvsp[-3];
          auto n = atToken(mkNode(ASTKind::ConstructExpr, yyvsp[-3].decl.name), yyvsp[-2].idx);
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.decl.ctorInit = n;
      }
#line 3479 "build/parser.tab.cpp"
    break;

  case 123: /* direct_declarator: direct_declarator '[' ']'  */
#line 704 "src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(nullptr); }
#line 3485 "build/parser.tab.cpp"
    break;

  case 124: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 705 "src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; yyval.decl.arrayDims.push_back(yyvsp[-1].node); }
#line 3491 "build/parser.tab.cpp"
    break;

  case 125: /* operator_function_id: OPERATOR overloadable_operator  */
#line 710 "src/parser.y"
                                     { yyval = yyvsp[-1]; yyval.str = "operator" + yyvsp[0].str; }
#line 3497 "build/parser.tab.cpp"
    break;

  case 126: /* overloadable_operator: '+'  */
#line 714 "src/parser.y"
          { yyval.str = "+"; }
#line 3503 "build/parser.tab.cpp"
    break;

  case 127: /* overloadable_operator: '-'  */
#line 714 "src/parser.y"
                                  { yyval.str = "-"; }
#line 3509 "build/parser.tab.cpp"
    break;

  case 128: /* overloadable_operator: '*'  */
#line 714 "src/parser.y"
                                                          { yyval.str = "*"; }
#line 3515 "build/parser.tab.cpp"
    break;

  case 129: /* overloadable_operator: '/'  */
#line 714 "src/parser.y"
                                                                                  { yyval.str = "/"; }
#line 3521 "build/parser.tab.cpp"
    break;

  case 130: /* overloadable_operator: '%'  */
#line 715 "src/parser.y"
          { yyval.str = "%"; }
#line 3527 "build/parser.tab.cpp"
    break;

  case 131: /* overloadable_operator: '^'  */
#line 715 "src/parser.y"
                                  { yyval.str = "^"; }
#line 3533 "build/parser.tab.cpp"
    break;

  case 132: /* overloadable_operator: '&'  */
#line 715 "src/parser.y"
                                                          { yyval.str = "&"; }
#line 3539 "build/parser.tab.cpp"
    break;

  case 133: /* overloadable_operator: '|'  */
#line 715 "src/parser.y"
                                                                                  { yyval.str = "|"; }
#line 3545 "build/parser.tab.cpp"
    break;

  case 134: /* overloadable_operator: '~'  */
#line 716 "src/parser.y"
          { yyval.str = "~"; }
#line 3551 "build/parser.tab.cpp"
    break;

  case 135: /* overloadable_operator: '!'  */
#line 716 "src/parser.y"
                                  { yyval.str = "!"; }
#line 3557 "build/parser.tab.cpp"
    break;

  case 136: /* overloadable_operator: '='  */
#line 716 "src/parser.y"
                                                          { yyval.str = "="; }
#line 3563 "build/parser.tab.cpp"
    break;

  case 137: /* overloadable_operator: '<'  */
#line 716 "src/parser.y"
                                                                                  { yyval.str = "<"; }
#line 3569 "build/parser.tab.cpp"
    break;

  case 138: /* overloadable_operator: '>'  */
#line 717 "src/parser.y"
          { yyval.str = ">"; }
#line 3575 "build/parser.tab.cpp"
    break;

  case 139: /* overloadable_operator: EQ_OP  */
#line 717 "src/parser.y"
                                    { yyval.str = "=="; }
#line 3581 "build/parser.tab.cpp"
    break;

  case 140: /* overloadable_operator: NE_OP  */
#line 717 "src/parser.y"
                                                               { yyval.str = "!="; }
#line 3587 "build/parser.tab.cpp"
    break;

  case 141: /* overloadable_operator: LE_OP  */
#line 717 "src/parser.y"
                                                                                          { yyval.str = "<="; }
#line 3593 "build/parser.tab.cpp"
    break;

  case 142: /* overloadable_operator: GE_OP  */
#line 718 "src/parser.y"
            { yyval.str = ">="; }
#line 3599 "build/parser.tab.cpp"
    break;

  case 143: /* overloadable_operator: AND_OP  */
#line 718 "src/parser.y"
                                        { yyval.str = "&&"; }
#line 3605 "build/parser.tab.cpp"
    break;

  case 144: /* overloadable_operator: OR_OP  */
#line 718 "src/parser.y"
                                                                   { yyval.str = "||"; }
#line 3611 "build/parser.tab.cpp"
    break;

  case 145: /* overloadable_operator: SHL  */
#line 718 "src/parser.y"
                                                                                            { yyval.str = "<<"; }
#line 3617 "build/parser.tab.cpp"
    break;

  case 146: /* overloadable_operator: SHR  */
#line 719 "src/parser.y"
          { yyval.str = ">>"; }
#line 3623 "build/parser.tab.cpp"
    break;

  case 147: /* overloadable_operator: INC  */
#line 719 "src/parser.y"
                                   { yyval.str = "++"; }
#line 3629 "build/parser.tab.cpp"
    break;

  case 148: /* overloadable_operator: DEC  */
#line 719 "src/parser.y"
                                                            { yyval.str = "--"; }
#line 3635 "build/parser.tab.cpp"
    break;

  case 149: /* overloadable_operator: PLUS_ASSIGN  */
#line 720 "src/parser.y"
                  { yyval.str = "+="; }
#line 3641 "build/parser.tab.cpp"
    break;

  case 150: /* overloadable_operator: MINUS_ASSIGN  */
#line 720 "src/parser.y"
                                                    { yyval.str = "-="; }
#line 3647 "build/parser.tab.cpp"
    break;

  case 151: /* overloadable_operator: MUL_ASSIGN  */
#line 720 "src/parser.y"
                                                                                    { yyval.str = "*="; }
#line 3653 "build/parser.tab.cpp"
    break;

  case 152: /* overloadable_operator: DIV_ASSIGN  */
#line 721 "src/parser.y"
                 { yyval.str = "/="; }
#line 3659 "build/parser.tab.cpp"
    break;

  case 153: /* overloadable_operator: MOD_ASSIGN  */
#line 721 "src/parser.y"
                                                 { yyval.str = "%="; }
#line 3665 "build/parser.tab.cpp"
    break;

  case 154: /* overloadable_operator: AND_ASSIGN  */
#line 721 "src/parser.y"
                                                                                 { yyval.str = "&="; }
#line 3671 "build/parser.tab.cpp"
    break;

  case 155: /* overloadable_operator: OR_ASSIGN  */
#line 722 "src/parser.y"
                { yyval.str = "|="; }
#line 3677 "build/parser.tab.cpp"
    break;

  case 156: /* overloadable_operator: XOR_ASSIGN  */
#line 722 "src/parser.y"
                                                { yyval.str = "^="; }
#line 3683 "build/parser.tab.cpp"
    break;

  case 157: /* overloadable_operator: SHL_ASSIGN  */
#line 722 "src/parser.y"
                                                                                { yyval.str = "<<="; }
#line 3689 "build/parser.tab.cpp"
    break;

  case 158: /* overloadable_operator: SHR_ASSIGN  */
#line 723 "src/parser.y"
                 { yyval.str = ">>="; }
#line 3695 "build/parser.tab.cpp"
    break;

  case 159: /* overloadable_operator: '[' ']'  */
#line 723 "src/parser.y"
                                               { yyval.str = "[]"; }
#line 3701 "build/parser.tab.cpp"
    break;

  case 160: /* overloadable_operator: '(' ')'  */
#line 723 "src/parser.y"
                                                                            { yyval.str = "()"; }
#line 3707 "build/parser.tab.cpp"
    break;

  case 161: /* param_scope: %empty  */
#line 730 "src/parser.y"
                                           { pushScope(); }
#line 3713 "build/parser.tab.cpp"
    break;

  case 162: /* constructor_args: assignment_expr  */
#line 734 "src/parser.y"
                      { yyval.nodeList.push_back(yyvsp[0].node); }
#line 3719 "build/parser.tab.cpp"
    break;

  case 163: /* constructor_args: constructor_args ',' assignment_expr  */
#line 735 "src/parser.y"
                                           { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 3725 "build/parser.tab.cpp"
    break;

  case 164: /* parameter_list_opt: %empty  */
#line 739 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3731 "build/parser.tab.cpp"
    break;

  case 165: /* parameter_list_opt: parameter_list  */
#line 740 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3737 "build/parser.tab.cpp"
    break;

  case 166: /* parameter_list: parameter_decl  */
#line 744 "src/parser.y"
                     {
          if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3745 "build/parser.tab.cpp"
    break;

  case 167: /* parameter_list: parameter_list ',' parameter_decl  */
#line 747 "src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3754 "build/parser.tab.cpp"
    break;

  case 168: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 751 "src/parser.y"
                                  {
          /* recognized only to be reported: no variable-argument functions (D51) */
          yyval = yyvsp[-2];
          reportDiagnostic(g_tokens[yyvsp[0].idx].line, g_tokens[yyvsp[0].idx].column, "...",
                           "'...' is not supported: this language has no variable-argument functions "
                           "(only printf and scanf take a variable number of arguments)",
                           "Syntax error");
      }
#line 3767 "build/parser.tab.cpp"
    break;

  case 169: /* parameter_decl: declaration_specifiers declarator  */
#line 762 "src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3777 "build/parser.tab.cpp"
    break;

  case 170: /* parameter_decl: declaration_specifiers abstract_declarator  */
#line 767 "src/parser.y"
                                                 {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyval.decl);
      }
#line 3787 "build/parser.tab.cpp"
    break;

  case 171: /* parameter_decl: declaration_specifiers  */
#line 772 "src/parser.y"
                             {
          yyval.decl = DeclInfo();
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl.typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyval.decl);
      }
#line 3797 "build/parser.tab.cpp"
    break;

  case 172: /* $@12: %empty  */
#line 780 "src/parser.y"
                                        {
          bool outOfClass = !yyvsp[0].decl.className.empty();
          if (outOfClass) enterClass(yyvsp[0].decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[0].decl.params) paramTypes.push_back(p.typeStr);
          std::string owner = yyvsp[-1].typeSpec.isFriend ? "" : currentClassName(); /* a friend is not a member */
          std::string mangled = mangle(yyvsp[0].decl.name, paramExprs(yyvsp[0].decl.params), owner);
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
#line 3839 "build/parser.tab.cpp"
    break;

  case 173: /* function_definition: declaration_specifiers declarator $@12 '{' block_item_list_opt '}'  */
#line 816 "src/parser.y"
                                    {
          popScope();
          bool outOfClass = !yyvsp[-4].decl.className.empty();
          /* currentClassName() is still correctly set here for the
             out-of-class case -- it was never left, see above -- so
             no need to re-enter it just to compute the mangled name
             again. */
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[-4].decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[-4].decl.name, paramExprs(yyvsp[-4].decl.params),
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
#line 3870 "build/parser.tab.cpp"
    break;

  case 174: /* statement: compound_stmt  */
#line 845 "src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3876 "build/parser.tab.cpp"
    break;

  case 175: /* statement: expr_stmt  */
#line 846 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3882 "build/parser.tab.cpp"
    break;

  case 176: /* statement: selection_stmt  */
#line 847 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3888 "build/parser.tab.cpp"
    break;

  case 177: /* statement: iteration_stmt  */
#line 848 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3894 "build/parser.tab.cpp"
    break;

  case 178: /* statement: jump_stmt  */
#line 849 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3900 "build/parser.tab.cpp"
    break;

  case 179: /* statement: labeled_stmt  */
#line 850 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3906 "build/parser.tab.cpp"
    break;

  case 180: /* statement: declaration  */
#line 851 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3912 "build/parser.tab.cpp"
    break;

  case 181: /* statement: error ';'  */
#line 852 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3918 "build/parser.tab.cpp"
    break;

  case 182: /* statement: error '}'  */
#line 853 "src/parser.y"
                { yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3924 "build/parser.tab.cpp"
    break;

  case 183: /* $@13: %empty  */
#line 857 "src/parser.y"
          { pushScope(); }
#line 3930 "build/parser.tab.cpp"
    break;

  case 184: /* compound_stmt: '{' $@13 block_item_list_opt '}'  */
#line 857 "src/parser.y"
                                                   {
          popScope();
          auto n = atToken(mkNode(ASTKind::CompoundStmt), yyvsp[-3].idx);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 3941 "build/parser.tab.cpp"
    break;

  case 185: /* block_item_list_opt: %empty  */
#line 866 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3947 "build/parser.tab.cpp"
    break;

  case 186: /* block_item_list_opt: block_item_list  */
#line 867 "src/parser.y"
                      { yyval = yyvsp[0]; }
#line 3953 "build/parser.tab.cpp"
    break;

  case 187: /* block_item_list: statement  */
#line 871 "src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3959 "build/parser.tab.cpp"
    break;

  case 188: /* block_item_list: block_item_list statement  */
#line 872 "src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3965 "build/parser.tab.cpp"
    break;

  case 189: /* expr_stmt: ';'  */
#line 876 "src/parser.y"
          { yyval.node = atToken(mkNode(ASTKind::EmptyStmt), yyvsp[0].idx); }
#line 3971 "build/parser.tab.cpp"
    break;

  case 190: /* expr_stmt: expr ';'  */
#line 877 "src/parser.y"
               { yyval.node = atNode(mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}), yyvsp[-1].node); }
#line 3977 "build/parser.tab.cpp"
    break;

  case 191: /* selection_stmt: IF '(' expr ')' statement  */
#line 881 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 3985 "build/parser.tab.cpp"
    break;

  case 192: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 884 "src/parser.y"
                                               {
          yyval.node = atToken(mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-6].idx);
      }
#line 3993 "build/parser.tab.cpp"
    break;

  case 193: /* $@14: %empty  */
#line 887 "src/parser.y"
                          { hintScope("switch"); }
#line 3999 "build/parser.tab.cpp"
    break;

  case 194: /* selection_stmt: SWITCH '(' expr ')' $@14 compound_stmt  */
#line 887 "src/parser.y"
                                                                 {
          yyval.node = atToken(mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4007 "build/parser.tab.cpp"
    break;

  case 195: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 893 "src/parser.y"
                                       {
          yyval.node = atToken(mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4015 "build/parser.tab.cpp"
    break;

  case 196: /* labeled_stmt: DEFAULT ':' statement  */
#line 896 "src/parser.y"
                            {
          yyval.node = atToken(mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4023 "build/parser.tab.cpp"
    break;

  case 197: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 899 "src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = atToken(mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-2].idx);
      }
#line 4033 "build/parser.tab.cpp"
    break;

  case 198: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 907 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4041 "build/parser.tab.cpp"
    break;

  case 199: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 910 "src/parser.y"
                                          {
          yyval.node = atToken(mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node}), yyvsp[-6].idx);
      }
#line 4049 "build/parser.tab.cpp"
    break;

  case 200: /* iteration_stmt: DO statement WHILE '(' expr ')' error  */
#line 917 "src/parser.y"
                                            {
          /* only the ';' is missing: resume right at the next statement */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4058 "build/parser.tab.cpp"
    break;

  case 201: /* iteration_stmt: DO statement error ';'  */
#line 921 "src/parser.y"
                             {
          /* `while`, '(' or ')' missing / malformed: skip to the ';' */
          yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel());
      }
#line 4067 "build/parser.tab.cpp"
    break;

  case 202: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 925 "src/parser.y"
                                   {
          yyval.node = atToken(mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-4].idx);
      }
#line 4075 "build/parser.tab.cpp"
    break;

  case 203: /* iteration_stmt: for_open expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 928 "src/parser.y"
                                                              {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4084 "build/parser.tab.cpp"
    break;

  case 204: /* iteration_stmt: for_open declaration expr_stmt for_incr_opt ')' statement  */
#line 932 "src/parser.y"
                                                                {
          popScope();
          yyval.node = atToken(mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-5].idx);
      }
#line 4093 "build/parser.tab.cpp"
    break;

  case 205: /* for_open: FOR '('  */
#line 941 "src/parser.y"
              { pushScope("for"); yyval = yyvsp[-1]; }
#line 4099 "build/parser.tab.cpp"
    break;

  case 206: /* for_incr_opt: %empty  */
#line 945 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4105 "build/parser.tab.cpp"
    break;

  case 207: /* for_incr_opt: expr  */
#line 946 "src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 4111 "build/parser.tab.cpp"
    break;

  case 208: /* jump_stmt: BREAK ';'  */
#line 950 "src/parser.y"
                { yyval.node = atToken(mkNode(ASTKind::BreakStmt), yyvsp[-1].idx); }
#line 4117 "build/parser.tab.cpp"
    break;

  case 209: /* jump_stmt: CONTINUE ';'  */
#line 951 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::ContinueStmt), yyvsp[-1].idx); }
#line 4123 "build/parser.tab.cpp"
    break;

  case 210: /* jump_stmt: RETURN ';'  */
#line 952 "src/parser.y"
                 { yyval.node = atToken(mkNode(ASTKind::ReturnStmt), yyvsp[-1].idx); }
#line 4129 "build/parser.tab.cpp"
    break;

  case 211: /* jump_stmt: RETURN expr ';'  */
#line 953 "src/parser.y"
                      { yyval.node = atToken(mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4135 "build/parser.tab.cpp"
    break;

  case 212: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 954 "src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          else queuePendingReference(yyvsp[-1].idx, yyvsp[-1].str, /*isLabel=*/true);
          recordUsage(s);
          yyval.node = atToken(mkNode(ASTKind::GotoStmt, yyvsp[-1].str), yyvsp[-1].idx);
      }
#line 4147 "build/parser.tab.cpp"
    break;

  case 213: /* expr: assignment_expr  */
#line 964 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4153 "build/parser.tab.cpp"
    break;

  case 214: /* expr: expr ',' assignment_expr  */
#line 965 "src/parser.y"
                               { yyval.node = atToken(mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4159 "build/parser.tab.cpp"
    break;

  case 215: /* assignment_expr: binary_expr  */
#line 969 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4165 "build/parser.tab.cpp"
    break;

  case 216: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 970 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx);
      }
#line 4173 "build/parser.tab.cpp"
    break;

  case 217: /* assign_op: '='  */
#line 976 "src/parser.y"
                   { yyval.str = "="; }
#line 4179 "build/parser.tab.cpp"
    break;

  case 218: /* assign_op: PLUS_ASSIGN  */
#line 977 "src/parser.y"
                   { yyval.str = "+="; }
#line 4185 "build/parser.tab.cpp"
    break;

  case 219: /* assign_op: MINUS_ASSIGN  */
#line 978 "src/parser.y"
                   { yyval.str = "-="; }
#line 4191 "build/parser.tab.cpp"
    break;

  case 220: /* assign_op: MUL_ASSIGN  */
#line 979 "src/parser.y"
                   { yyval.str = "*="; }
#line 4197 "build/parser.tab.cpp"
    break;

  case 221: /* assign_op: DIV_ASSIGN  */
#line 980 "src/parser.y"
                   { yyval.str = "/="; }
#line 4203 "build/parser.tab.cpp"
    break;

  case 222: /* assign_op: MOD_ASSIGN  */
#line 981 "src/parser.y"
                   { yyval.str = "%="; }
#line 4209 "build/parser.tab.cpp"
    break;

  case 223: /* assign_op: AND_ASSIGN  */
#line 982 "src/parser.y"
                   { yyval.str = "&="; }
#line 4215 "build/parser.tab.cpp"
    break;

  case 224: /* assign_op: OR_ASSIGN  */
#line 983 "src/parser.y"
                   { yyval.str = "|="; }
#line 4221 "build/parser.tab.cpp"
    break;

  case 225: /* assign_op: XOR_ASSIGN  */
#line 984 "src/parser.y"
                   { yyval.str = "^="; }
#line 4227 "build/parser.tab.cpp"
    break;

  case 226: /* assign_op: SHL_ASSIGN  */
#line 985 "src/parser.y"
                   { yyval.str = "<<="; }
#line 4233 "build/parser.tab.cpp"
    break;

  case 227: /* assign_op: SHR_ASSIGN  */
#line 986 "src/parser.y"
                   { yyval.str = ">>="; }
#line 4239 "build/parser.tab.cpp"
    break;

  case 228: /* constant_expr: binary_expr  */
#line 990 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4245 "build/parser.tab.cpp"
    break;

  case 229: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 994 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4251 "build/parser.tab.cpp"
    break;

  case 230: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 995 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4257 "build/parser.tab.cpp"
    break;

  case 231: /* binary_expr: binary_expr '|' binary_expr  */
#line 996 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4263 "build/parser.tab.cpp"
    break;

  case 232: /* binary_expr: binary_expr '^' binary_expr  */
#line 997 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4269 "build/parser.tab.cpp"
    break;

  case 233: /* binary_expr: binary_expr '&' binary_expr  */
#line 998 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4275 "build/parser.tab.cpp"
    break;

  case 234: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 999 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4281 "build/parser.tab.cpp"
    break;

  case 235: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 1000 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4287 "build/parser.tab.cpp"
    break;

  case 236: /* binary_expr: binary_expr '<' binary_expr  */
#line 1001 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4293 "build/parser.tab.cpp"
    break;

  case 237: /* binary_expr: binary_expr '>' binary_expr  */
#line 1002 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4299 "build/parser.tab.cpp"
    break;

  case 238: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 1003 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4305 "build/parser.tab.cpp"
    break;

  case 239: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 1004 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4311 "build/parser.tab.cpp"
    break;

  case 240: /* binary_expr: binary_expr SHL binary_expr  */
#line 1005 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4317 "build/parser.tab.cpp"
    break;

  case 241: /* binary_expr: binary_expr SHR binary_expr  */
#line 1006 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4323 "build/parser.tab.cpp"
    break;

  case 242: /* binary_expr: binary_expr '+' binary_expr  */
#line 1007 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4329 "build/parser.tab.cpp"
    break;

  case 243: /* binary_expr: binary_expr '-' binary_expr  */
#line 1008 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4335 "build/parser.tab.cpp"
    break;

  case 244: /* binary_expr: binary_expr '*' binary_expr  */
#line 1009 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4341 "build/parser.tab.cpp"
    break;

  case 245: /* binary_expr: binary_expr '/' binary_expr  */
#line 1010 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4347 "build/parser.tab.cpp"
    break;

  case 246: /* binary_expr: binary_expr '%' binary_expr  */
#line 1011 "src/parser.y"
                                     { yyval.node = atToken(mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}), yyvsp[-1].idx); }
#line 4353 "build/parser.tab.cpp"
    break;

  case 247: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 1012 "src/parser.y"
                                           {
          yyval.node = atToken(mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node}), yyvsp[-3].idx);
      }
#line 4361 "build/parser.tab.cpp"
    break;

  case 248: /* binary_expr: unary_expr  */
#line 1015 "src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 4367 "build/parser.tab.cpp"
    break;

  case 249: /* unary_expr: postfix_expr  */
#line 1019 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4373 "build/parser.tab.cpp"
    break;

  case 250: /* unary_expr: INC unary_expr  */
#line 1020 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4379 "build/parser.tab.cpp"
    break;

  case 251: /* unary_expr: DEC unary_expr  */
#line 1021 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4385 "build/parser.tab.cpp"
    break;

  case 252: /* unary_expr: '&' unary_expr  */
#line 1022 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4391 "build/parser.tab.cpp"
    break;

  case 253: /* unary_expr: '*' unary_expr  */
#line 1023 "src/parser.y"
                                 { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4397 "build/parser.tab.cpp"
    break;

  case 254: /* unary_expr: '+' unary_expr  */
#line 1024 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4403 "build/parser.tab.cpp"
    break;

  case 255: /* unary_expr: '-' unary_expr  */
#line 1025 "src/parser.y"
                                  { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4409 "build/parser.tab.cpp"
    break;

  case 256: /* unary_expr: '!' unary_expr  */
#line 1026 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4415 "build/parser.tab.cpp"
    break;

  case 257: /* unary_expr: '~' unary_expr  */
#line 1027 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4421 "build/parser.tab.cpp"
    break;

  case 258: /* unary_expr: '(' type_name ')' unary_expr  */
#line 1028 "src/parser.y"
                                              {
          yyval.node = atToken(mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node}), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-2].typeSpec, yyvsp[-2].decl);
      }
#line 4430 "build/parser.tab.cpp"
    break;

  case 259: /* unary_expr: SIZEOF unary_expr  */
#line 1032 "src/parser.y"
                                   { yyval.node = atToken(mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}), yyvsp[-1].idx); }
#line 4436 "build/parser.tab.cpp"
    break;

  case 260: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 1033 "src/parser.y"
                                                 {
          yyval.node = atToken(mkNode(ASTKind::SizeofExpr, yyvsp[-1].str), yyvsp[-3].idx);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[-1].typeSpec, yyvsp[-1].decl);
      }
#line 4445 "build/parser.tab.cpp"
    break;

  case 261: /* type_name: type_name_specifiers  */
#line 1040 "src/parser.y"
                           {
          yyval.str = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
          yyval.decl = DeclInfo();
      }
#line 4454 "build/parser.tab.cpp"
    break;

  case 262: /* type_name: type_name_specifiers abstract_declarator  */
#line 1044 "src/parser.y"
                                               {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
          yyval.decl = yyvsp[0].decl;
      }
#line 4463 "build/parser.tab.cpp"
    break;

  case 263: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 1051 "src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (!yyvsp[0].typeSpec.tagName.empty()) yyval.typeSpec.tagName = yyvsp[0].typeSpec.tagName;
          if (!yyvsp[0].typeSpec.typedefName.empty()) yyval.typeSpec.typedefName = yyvsp[0].typeSpec.typedefName;
      }
#line 4475 "build/parser.tab.cpp"
    break;

  case 264: /* type_name_specifiers: type_name_specifier  */
#line 1058 "src/parser.y"
                          { yyval = yyvsp[0]; }
#line 4481 "build/parser.tab.cpp"
    break;

  case 265: /* type_name_specifier: INT  */
#line 1062 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("INT"); }
#line 4487 "build/parser.tab.cpp"
    break;

  case 266: /* type_name_specifier: CHAR  */
#line 1063 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("CHAR"); }
#line 4493 "build/parser.tab.cpp"
    break;

  case 267: /* type_name_specifier: FLOAT  */
#line 1064 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 4499 "build/parser.tab.cpp"
    break;

  case 268: /* type_name_specifier: DOUBLE  */
#line 1065 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 4505 "build/parser.tab.cpp"
    break;

  case 269: /* type_name_specifier: VOID  */
#line 1066 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("VOID"); }
#line 4511 "build/parser.tab.cpp"
    break;

  case 270: /* type_name_specifier: BOOL  */
#line 1067 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("BOOL"); }
#line 4517 "build/parser.tab.cpp"
    break;

  case 271: /* type_name_specifier: SHORT  */
#line 1068 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SHORT"); }
#line 4523 "build/parser.tab.cpp"
    break;

  case 272: /* type_name_specifier: LONG  */
#line 1069 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("LONG"); }
#line 4529 "build/parser.tab.cpp"
    break;

  case 273: /* type_name_specifier: SIGNED  */
#line 1070 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 4535 "build/parser.tab.cpp"
    break;

  case 274: /* type_name_specifier: UNSIGNED  */
#line 1071 "src/parser.y"
                                       { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 4541 "build/parser.tab.cpp"
    break;

  case 275: /* type_name_specifier: CONST  */
#line 1072 "src/parser.y"
               { yyval = ParserValue(); yyval.typeSpec.isConst = true; }
#line 4547 "build/parser.tab.cpp"
    break;

  case 276: /* type_name_specifier: TYPE_NAME  */
#line 1073 "src/parser.y"
                                        {
          /* in a cast / sizeof / call argument, `T(` is the expression
             `T(...)`: these positions already accept expressions, and a
             type here could never be followed by '(' anyway */
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
          yyval.typeSpec.typedefName = yyvsp[0].str;
      }
#line 4561 "build/parser.tab.cpp"
    break;

  case 277: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 1082 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4572 "build/parser.tab.cpp"
    break;

  case 278: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 1088 "src/parser.y"
                       {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4583 "build/parser.tab.cpp"
    break;

  case 279: /* type_name_specifier: ENUM IDENTIFIER  */
#line 1094 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4594 "build/parser.tab.cpp"
    break;

  case 280: /* type_name_specifier: ENUM TYPE_NAME  */
#line 1100 "src/parser.y"
                     {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4605 "build/parser.tab.cpp"
    break;

  case 281: /* type_name_specifier: CLASS IDENTIFIER  */
#line 1106 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4616 "build/parser.tab.cpp"
    break;

  case 282: /* type_name_specifier: CLASS TYPE_NAME  */
#line 1112 "src/parser.y"
                      {
          const Symbol *s = lookupTypeSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
          yyval.typeSpec.tagName = yyvsp[0].str;
      }
#line 4627 "build/parser.tab.cpp"
    break;

  case 283: /* postfix_expr: primary_expr  */
#line 1121 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4633 "build/parser.tab.cpp"
    break;

  case 284: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 1122 "src/parser.y"
                                { yyval.node = atToken(mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}), yyvsp[-2].idx); }
#line 4639 "build/parser.tab.cpp"
    break;

  case 285: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 1123 "src/parser.y"
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
#line 4679 "build/parser.tab.cpp"
    break;

  case 286: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 1158 "src/parser.y"
                                  {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4688 "build/parser.tab.cpp"
    break;

  case 287: /* postfix_expr: postfix_expr '.' TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1162 "src/parser.y"
                                                      {
          /* obj.Base::member: the member as class Base declares it, even
             if the object's own class hides it */
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4701 "build/parser.tab.cpp"
    break;

  case 288: /* postfix_expr: postfix_expr ARROW TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1170 "src/parser.y"
                                                        {
          if (const SymbolTableEntry *member = findMember(yyvsp[-2].str, yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-4].node}), yyvsp[0].idx);
          yyval.node->typeExpr = std::make_shared<ASTTypeExpr>();
          yyval.node->typeExpr->className = yyvsp[-2].str;
      }
#line 4712 "build/parser.tab.cpp"
    break;

  case 289: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 1176 "src/parser.y"
                                    {
          if (const SymbolTableEntry *member = findMember(aggregateOf(yyvsp[-2].node), yyvsp[0].str)) setCategory(yyvsp[0].idx, member->typeStr);
          yyval.node = atToken(mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx);
      }
#line 4721 "build/parser.tab.cpp"
    break;

  case 290: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 1180 "src/parser.y"
                                        { yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}), yyvsp[0].idx); }
#line 4727 "build/parser.tab.cpp"
    break;

  case 291: /* postfix_expr: postfix_expr INC  */
#line 1181 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4733 "build/parser.tab.cpp"
    break;

  case 292: /* postfix_expr: postfix_expr DEC  */
#line 1182 "src/parser.y"
                       { yyval.node = atToken(mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}), yyvsp[0].idx); }
#line 4739 "build/parser.tab.cpp"
    break;

  case 293: /* postfix_expr: builtin_call  */
#line 1183 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 4745 "build/parser.tab.cpp"
    break;

  case 294: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 1187 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "printf"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4751 "build/parser.tab.cpp"
    break;

  case 295: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 1188 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "scanf"), yyvsp[-3].idx);   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4757 "build/parser.tab.cpp"
    break;

  case 296: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 1189 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "malloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4763 "build/parser.tab.cpp"
    break;

  case 297: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 1190 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "free"), yyvsp[-3].idx);    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4769 "build/parser.tab.cpp"
    break;

  case 298: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 1191 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "calloc"), yyvsp[-3].idx);  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4775 "build/parser.tab.cpp"
    break;

  case 299: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 1192 "src/parser.y"
                                        { auto n = atToken(mkNode(ASTKind::BuiltinCallExpr, "realloc"), yyvsp[-3].idx); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4781 "build/parser.tab.cpp"
    break;

  case 300: /* constructor_args_opt: %empty  */
#line 1196 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4787 "build/parser.tab.cpp"
    break;

  case 301: /* constructor_args_opt: constructor_args  */
#line 1197 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 4793 "build/parser.tab.cpp"
    break;

  case 302: /* argument_list_opt: %empty  */
#line 1201 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4799 "build/parser.tab.cpp"
    break;

  case 303: /* argument_list_opt: argument_list  */
#line 1202 "src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4805 "build/parser.tab.cpp"
    break;

  case 304: /* argument_list: argument  */
#line 1206 "src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4811 "build/parser.tab.cpp"
    break;

  case 305: /* argument_list: argument_list ',' argument  */
#line 1207 "src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4817 "build/parser.tab.cpp"
    break;

  case 306: /* argument: assignment_expr  */
#line 1211 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4823 "build/parser.tab.cpp"
    break;

  case 307: /* argument: type_name  */
#line 1212 "src/parser.y"
                {
          yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str);
          yyval.node->typeExpr = makeTypeExpr(yyvsp[0].typeSpec, yyvsp[0].decl);
      }
#line 4832 "build/parser.tab.cpp"
    break;

  case 308: /* primary_expr: IDENTIFIER  */
#line 1219 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          else queuePendingReference(yyvsp[0].idx, yyvsp[0].str, /*isLabel=*/false);
          if (!(s && s->kind == SymKind::PROCEDURE && isOverloaded(yyvsp[0].str))) {
              recordUsage(s);
          }
          yyval.node = atToken(mkNode(ASTKind::Identifier, yyvsp[0].str), yyvsp[0].idx);
      }
#line 4846 "build/parser.tab.cpp"
    break;

  case 309: /* primary_expr: INT_LITERAL  */
#line 1228 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::IntLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4852 "build/parser.tab.cpp"
    break;

  case 310: /* primary_expr: FLOAT_LITERAL  */
#line 1229 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::FloatLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4858 "build/parser.tab.cpp"
    break;

  case 311: /* primary_expr: CHAR_LITERAL  */
#line 1230 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::CharLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4864 "build/parser.tab.cpp"
    break;

  case 312: /* primary_expr: string_literal  */
#line 1231 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 4870 "build/parser.tab.cpp"
    break;

  case 313: /* primary_expr: BOOL_LITERAL  */
#line 1232 "src/parser.y"
                   { yyval.node = atToken(mkNode(ASTKind::BoolLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4876 "build/parser.tab.cpp"
    break;

  case 314: /* primary_expr: THIS  */
#line 1233 "src/parser.y"
           { yyval.node = atToken(mkNode(ASTKind::ThisExpr), yyvsp[0].idx); }
#line 4882 "build/parser.tab.cpp"
    break;

  case 315: /* primary_expr: TYPE_NAME '(' constructor_args_opt ')'  */
#line 1234 "src/parser.y"
                                             {
          /* `Dog()`: a temporary object (for a scalar type, `int(x)`, a cast) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4891 "build/parser.tab.cpp"
    break;

  case 316: /* primary_expr: FCAST '(' constructor_args_opt ')'  */
#line 1238 "src/parser.y"
                                         {
          /* `Dog(4)` / `int(x)` where only an expression is possible --
             the scanner already looked past the ')' (see scanner.l) */
          yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList);
      }
#line 4901 "build/parser.tab.cpp"
    break;

  case 317: /* primary_expr: INT '(' constructor_args_opt ')'  */
#line 1245 "src/parser.y"
                                       { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4907 "build/parser.tab.cpp"
    break;

  case 318: /* primary_expr: CHAR '(' constructor_args_opt ')'  */
#line 1246 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4913 "build/parser.tab.cpp"
    break;

  case 319: /* primary_expr: FLOAT '(' constructor_args_opt ')'  */
#line 1247 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4919 "build/parser.tab.cpp"
    break;

  case 320: /* primary_expr: DOUBLE '(' constructor_args_opt ')'  */
#line 1248 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4925 "build/parser.tab.cpp"
    break;

  case 321: /* primary_expr: VOID '(' constructor_args_opt ')'  */
#line 1249 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4931 "build/parser.tab.cpp"
    break;

  case 322: /* primary_expr: BOOL '(' constructor_args_opt ')'  */
#line 1250 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4937 "build/parser.tab.cpp"
    break;

  case 323: /* primary_expr: SHORT '(' constructor_args_opt ')'  */
#line 1251 "src/parser.y"
                                         { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4943 "build/parser.tab.cpp"
    break;

  case 324: /* primary_expr: LONG '(' constructor_args_opt ')'  */
#line 1252 "src/parser.y"
                                        { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4949 "build/parser.tab.cpp"
    break;

  case 325: /* primary_expr: SIGNED '(' constructor_args_opt ')'  */
#line 1253 "src/parser.y"
                                          { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4955 "build/parser.tab.cpp"
    break;

  case 326: /* primary_expr: UNSIGNED '(' constructor_args_opt ')'  */
#line 1254 "src/parser.y"
                                            { yyval.node = makeFunctionalCast(yyvsp[-3].str, yyvsp[-3].idx, yyvsp[-1].nodeList); }
#line 4961 "build/parser.tab.cpp"
    break;

  case 327: /* primary_expr: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 1255 "src/parser.y"
                                     {
          /* `Shape::count` -- the class name is a TYPE_NAME once defined */
          const Symbol *s = lookupTypeSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          auto base = atToken(mkNode(ASTKind::Identifier, yyvsp[-2].str), yyvsp[-2].idx);
          yyval.node = atToken(mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {base}), yyvsp[0].idx);
      }
#line 4973 "build/parser.tab.cpp"
    break;

  case 328: /* primary_expr: '(' expr ')'  */
#line 1262 "src/parser.y"
                   {
          yyval.node = yyvsp[-1].node; /* parentheses build no node, but are remembered: */
          if (yyval.node) yyval.node->parenthesized = true; /* `if ((x = f()))` means the assignment */
      }
#line 4982 "build/parser.tab.cpp"
    break;

  case 329: /* string_literal: STRING_LITERAL  */
#line 1270 "src/parser.y"
                     { yyval.node = atToken(mkNode(ASTKind::StringLiteral, yyvsp[0].str), yyvsp[0].idx); }
#line 4988 "build/parser.tab.cpp"
    break;

  case 330: /* string_literal: string_literal STRING_LITERAL  */
#line 1271 "src/parser.y"
                                    {
          yyval = yyvsp[-1];
          std::string &text = yyval.node->label;
          text = text.substr(0, text.size() - 1) + yyvsp[0].str.substr(1);
      }
#line 4998 "build/parser.tab.cpp"
    break;


#line 5002 "build/parser.tab.cpp"

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

#line 1278 "src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
