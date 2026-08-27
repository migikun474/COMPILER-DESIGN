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
  YYSYMBOL_FILE_KW = 44,                   /* FILE_KW  */
  YYSYMBOL_FOPEN = 45,                     /* FOPEN  */
  YYSYMBOL_FCLOSE = 46,                    /* FCLOSE  */
  YYSYMBOL_FREAD = 47,                     /* FREAD  */
  YYSYMBOL_FWRITE = 48,                    /* FWRITE  */
  YYSYMBOL_FPRINTF = 49,                   /* FPRINTF  */
  YYSYMBOL_FSCANF = 50,                    /* FSCANF  */
  YYSYMBOL_FGETS = 51,                     /* FGETS  */
  YYSYMBOL_FPUTS = 52,                     /* FPUTS  */
  YYSYMBOL_FEOF = 53,                      /* FEOF  */
  YYSYMBOL_BOOL = 54,                      /* BOOL  */
  YYSYMBOL_NEW = 55,                       /* NEW  */
  YYSYMBOL_DELETE = 56,                    /* DELETE  */
  YYSYMBOL_SIZEOF = 57,                    /* SIZEOF  */
  YYSYMBOL_IDENTIFIER = 58,                /* IDENTIFIER  */
  YYSYMBOL_TYPE_NAME = 59,                 /* TYPE_NAME  */
  YYSYMBOL_INT_LITERAL = 60,               /* INT_LITERAL  */
  YYSYMBOL_FLOAT_LITERAL = 61,             /* FLOAT_LITERAL  */
  YYSYMBOL_CHAR_LITERAL = 62,              /* CHAR_LITERAL  */
  YYSYMBOL_STRING_LITERAL = 63,            /* STRING_LITERAL  */
  YYSYMBOL_BOOL_LITERAL = 64,              /* BOOL_LITERAL  */
  YYSYMBOL_ARROW = 65,                     /* ARROW  */
  YYSYMBOL_ELLIPSIS = 66,                  /* ELLIPSIS  */
  YYSYMBOL_SCOPE_RES = 67,                 /* SCOPE_RES  */
  YYSYMBOL_INC = 68,                       /* INC  */
  YYSYMBOL_DEC = 69,                       /* DEC  */
  YYSYMBOL_SHL = 70,                       /* SHL  */
  YYSYMBOL_SHR = 71,                       /* SHR  */
  YYSYMBOL_LE_OP = 72,                     /* LE_OP  */
  YYSYMBOL_GE_OP = 73,                     /* GE_OP  */
  YYSYMBOL_EQ_OP = 74,                     /* EQ_OP  */
  YYSYMBOL_NE_OP = 75,                     /* NE_OP  */
  YYSYMBOL_AND_OP = 76,                    /* AND_OP  */
  YYSYMBOL_OR_OP = 77,                     /* OR_OP  */
  YYSYMBOL_PLUS_ASSIGN = 78,               /* PLUS_ASSIGN  */
  YYSYMBOL_MINUS_ASSIGN = 79,              /* MINUS_ASSIGN  */
  YYSYMBOL_MUL_ASSIGN = 80,                /* MUL_ASSIGN  */
  YYSYMBOL_DIV_ASSIGN = 81,                /* DIV_ASSIGN  */
  YYSYMBOL_MOD_ASSIGN = 82,                /* MOD_ASSIGN  */
  YYSYMBOL_AND_ASSIGN = 83,                /* AND_ASSIGN  */
  YYSYMBOL_OR_ASSIGN = 84,                 /* OR_ASSIGN  */
  YYSYMBOL_XOR_ASSIGN = 85,                /* XOR_ASSIGN  */
  YYSYMBOL_SHL_ASSIGN = 86,                /* SHL_ASSIGN  */
  YYSYMBOL_SHR_ASSIGN = 87,                /* SHR_ASSIGN  */
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
  YYSYMBOL_struct_or_class_specifier = 124, /* struct_or_class_specifier  */
  YYSYMBOL_125_1 = 125,                    /* $@1  */
  YYSYMBOL_126_2 = 126,                    /* $@2  */
  YYSYMBOL_127_3 = 127,                    /* $@3  */
  YYSYMBOL_128_4 = 128,                    /* $@4  */
  YYSYMBOL_129_5 = 129,                    /* $@5  */
  YYSYMBOL_130_6 = 130,                    /* $@6  */
  YYSYMBOL_131_7 = 131,                    /* $@7  */
  YYSYMBOL_member_decl_list_opt = 132,     /* member_decl_list_opt  */
  YYSYMBOL_inheritance_opt = 133,          /* inheritance_opt  */
  YYSYMBOL_inheritance_specifier_list = 134, /* inheritance_specifier_list  */
  YYSYMBOL_inheritance_specifier = 135,    /* inheritance_specifier  */
  YYSYMBOL_member_decl_list = 136,         /* member_decl_list  */
  YYSYMBOL_member_item = 137,              /* member_item  */
  YYSYMBOL_constructor_def = 138,          /* constructor_def  */
  YYSYMBOL_139_8 = 139,                    /* $@8  */
  YYSYMBOL_140_9 = 140,                    /* $@9  */
  YYSYMBOL_destructor_def = 141,           /* destructor_def  */
  YYSYMBOL_142_10 = 142,                   /* $@10  */
  YYSYMBOL_access_specifier = 143,         /* access_specifier  */
  YYSYMBOL_enumerator_list = 144,          /* enumerator_list  */
  YYSYMBOL_enumerator = 145,               /* enumerator  */
  YYSYMBOL_init_declarator_list_opt = 146, /* init_declarator_list_opt  */
  YYSYMBOL_init_declarator_list = 147,     /* init_declarator_list  */
  YYSYMBOL_init_declarator = 148,          /* init_declarator  */
  YYSYMBOL_initializer = 149,              /* initializer  */
  YYSYMBOL_initializer_list = 150,         /* initializer_list  */
  YYSYMBOL_pointer = 151,                  /* pointer  */
  YYSYMBOL_pointer_opt = 152,              /* pointer_opt  */
  YYSYMBOL_declarator = 153,               /* declarator  */
  YYSYMBOL_direct_declarator = 154,        /* direct_declarator  */
  YYSYMBOL_155_11 = 155,                   /* $@11  */
  YYSYMBOL_parameter_list_opt = 156,       /* parameter_list_opt  */
  YYSYMBOL_parameter_list = 157,           /* parameter_list  */
  YYSYMBOL_parameter_decl = 158,           /* parameter_decl  */
  YYSYMBOL_function_definition = 159,      /* function_definition  */
  YYSYMBOL_160_12 = 160,                   /* $@12  */
  YYSYMBOL_statement = 161,                /* statement  */
  YYSYMBOL_compound_stmt = 162,            /* compound_stmt  */
  YYSYMBOL_163_13 = 163,                   /* $@13  */
  YYSYMBOL_block_item_list_opt = 164,      /* block_item_list_opt  */
  YYSYMBOL_block_item_list = 165,          /* block_item_list  */
  YYSYMBOL_expr_stmt = 166,                /* expr_stmt  */
  YYSYMBOL_selection_stmt = 167,           /* selection_stmt  */
  YYSYMBOL_168_14 = 168,                   /* $@14  */
  YYSYMBOL_labeled_stmt = 169,             /* labeled_stmt  */
  YYSYMBOL_iteration_stmt = 170,           /* iteration_stmt  */
  YYSYMBOL_171_15 = 171,                   /* $@15  */
  YYSYMBOL_for_incr_opt = 172,             /* for_incr_opt  */
  YYSYMBOL_jump_stmt = 173,                /* jump_stmt  */
  YYSYMBOL_expr = 174,                     /* expr  */
  YYSYMBOL_assignment_expr = 175,          /* assignment_expr  */
  YYSYMBOL_assign_op = 176,                /* assign_op  */
  YYSYMBOL_constant_expr = 177,            /* constant_expr  */
  YYSYMBOL_binary_expr = 178,              /* binary_expr  */
  YYSYMBOL_unary_expr = 179,               /* unary_expr  */
  YYSYMBOL_type_name = 180,                /* type_name  */
  YYSYMBOL_type_name_specifiers = 181,     /* type_name_specifiers  */
  YYSYMBOL_type_name_specifier = 182,      /* type_name_specifier  */
  YYSYMBOL_postfix_expr = 183,             /* postfix_expr  */
  YYSYMBOL_builtin_call = 184,             /* builtin_call  */
  YYSYMBOL_argument_list_opt = 185,        /* argument_list_opt  */
  YYSYMBOL_argument_list = 186,            /* argument_list  */
  YYSYMBOL_argument = 187,                 /* argument  */
  YYSYMBOL_primary_expr = 188,             /* primary_expr  */
  YYSYMBOL_lambda_expr = 189,              /* lambda_expr  */
  YYSYMBOL_190_16 = 190,                   /* $@16  */
  YYSYMBOL_191_17 = 191,                   /* $@17  */
  YYSYMBOL_capture_list_opt = 192,         /* capture_list_opt  */
  YYSYMBOL_capture_list = 193,             /* capture_list  */
  YYSYMBOL_capture = 194                   /* capture  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;



/* Unqualified %code blocks.  */
#line 9 "src/parser.y"

    #include <cstdio>
    #include <cstring>
    #include <string>
    extern int yylex();
    extern FILE *yyin;
    extern int yylineno;
    void yyerror(const char *s);

#line 308 "build/parser.tab.cpp"

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
#define YYLAST   1628

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  117
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  78
/* YYNRULES -- Number of rules.  */
#define YYNRULES  274
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  473

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
       2,     2,     2,   105,     2,     2,     2,   100,    93,     2,
     108,   115,    98,    96,   114,    97,   107,    99,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    90,   111,
      94,    88,    95,    89,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   109,     2,   116,    92,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   113,    91,   112,   106,     2,     2,     2,
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
      85,    86,    87,   101,   102,   103,   104,   110
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,    70,    70,    74,    82,    83,    84,    85,    92,   112,
     121,   125,   126,   127,   128,   129,   130,   134,   135,   136,
     137,   138,   139,   140,   141,   142,   143,   144,   145,   150,
     154,   158,   154,   170,   175,   180,   184,   180,   192,   197,
     202,   206,   202,   216,   221,   226,   226,   236,   241,   249,
     250,   254,   255,   259,   260,   264,   269,   274,   279,   287,
     288,   292,   293,   294,   295,   296,   300,   300,   300,   331,
     331,   349,   350,   351,   355,   356,   360,   365,   373,   374,
     378,   379,   383,   384,   388,   389,   394,   402,   403,   410,
     411,   412,   416,   417,   421,   425,   429,   433,   440,   452,
     453,   453,   469,   470,   474,   475,   479,   480,   484,   488,
     492,   501,   501,   553,   554,   555,   556,   557,   558,   559,
     560,   561,   565,   565,   574,   575,   579,   580,   584,   585,
     589,   592,   595,   595,   601,   604,   607,   615,   618,   621,
     624,   627,   627,   634,   635,   639,   640,   641,   642,   643,
     660,   661,   665,   666,   672,   673,   674,   675,   676,   677,
     678,   679,   680,   681,   682,   686,   690,   691,   692,   693,
     694,   695,   696,   697,   698,   699,   700,   701,   702,   703,
     704,   705,   706,   707,   708,   711,   715,   716,   717,   718,
     719,   720,   721,   722,   723,   724,   727,   728,   729,   730,
     734,   740,   744,   753,   754,   755,   756,   757,   758,   759,
     760,   761,   762,   763,   764,   765,   766,   771,   776,   781,
     786,   791,   796,   801,   806,   814,   815,   816,   821,   822,
     823,   824,   825,   826,   830,   831,   832,   833,   834,   835,
     836,   837,   838,   839,   840,   841,   842,   843,   844,   848,
     849,   853,   854,   858,   859,   863,   869,   870,   871,   872,
     873,   874,   875,   876,   880,   880,   880,   899,   900,   904,
     905,   909,   910,   911,   912
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
  "STATIC", "TYPEDEF", "AUTO", "CONST", "VOLATILE", "IF", "ELSE", "FOR",
  "WHILE", "DO", "UNTIL", "SWITCH", "CASE", "DEFAULT", "BREAK", "CONTINUE",
  "GOTO", "RETURN", "PRINTF", "SCANF", "MALLOC", "FREE", "CALLOC",
  "REALLOC", "FILE_KW", "FOPEN", "FCLOSE", "FREAD", "FWRITE", "FPRINTF",
  "FSCANF", "FGETS", "FPUTS", "FEOF", "BOOL", "NEW", "DELETE", "SIZEOF",
  "IDENTIFIER", "TYPE_NAME", "INT_LITERAL", "FLOAT_LITERAL",
  "CHAR_LITERAL", "STRING_LITERAL", "BOOL_LITERAL", "ARROW", "ELLIPSIS",
  "SCOPE_RES", "INC", "DEC", "SHL", "SHR", "LE_OP", "GE_OP", "EQ_OP",
  "NE_OP", "AND_OP", "OR_OP", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN",
  "DIV_ASSIGN", "MOD_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN",
  "SHL_ASSIGN", "SHR_ASSIGN", "'='", "'?'", "':'", "'|'", "'^'", "'&'",
  "'<'", "'>'", "'+'", "'-'", "'*'", "'/'", "'%'", "UMINUS", "ADDR",
  "DEREF", "CAST", "'!'", "'~'", "'.'", "'('", "'['", "IFX", "';'", "'}'",
  "'{'", "','", "')'", "']'", "$accept", "translation_unit",
  "external_decl", "declaration", "declaration_specifiers",
  "storage_or_type_specifier", "type_specifier",
  "struct_or_class_specifier", "$@1", "$@2", "$@3", "$@4", "$@5", "$@6",
  "$@7", "member_decl_list_opt", "inheritance_opt",
  "inheritance_specifier_list", "inheritance_specifier",
  "member_decl_list", "member_item", "constructor_def", "$@8", "$@9",
  "destructor_def", "$@10", "access_specifier", "enumerator_list",
  "enumerator", "init_declarator_list_opt", "init_declarator_list",
  "init_declarator", "initializer", "initializer_list", "pointer",
  "pointer_opt", "declarator", "direct_declarator", "$@11",
  "parameter_list_opt", "parameter_list", "parameter_decl",
  "function_definition", "$@12", "statement", "compound_stmt", "$@13",
  "block_item_list_opt", "block_item_list", "expr_stmt", "selection_stmt",
  "$@14", "labeled_stmt", "iteration_stmt", "$@15", "for_incr_opt",
  "jump_stmt", "expr", "assignment_expr", "assign_op", "constant_expr",
  "binary_expr", "unary_expr", "type_name", "type_name_specifiers",
  "type_name_specifier", "postfix_expr", "builtin_call",
  "argument_list_opt", "argument_list", "argument", "primary_expr",
  "lambda_expr", "$@16", "$@17", "capture_list_opt", "capture_list",
  "capture", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-419)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-126)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -419,  1400,  -419,   -62,  -419,  -419,  -419,  -419,  -419,  -419,
    -419,  -419,  -419,    19,   123,   127,   130,  -419,  -419,  -419,
    -419,  -419,  -419,  -419,  -419,  -419,  -419,   286,  -419,  -419,
    -419,  -419,  -419,  -419,   -93,  -419,   -17,  -419,    10,  -419,
     -43,  -419,    38,    58,  -419,  -419,    76,  -419,    18,    28,
    -419,    82,   -40,    29,    20,    43,    59,    93,   145,   147,
      58,   103,  -419,    76,  -419,    29,   971,   107,  -419,   823,
    -419,   170,  -419,    85,   120,  -419,  -419,  -419,  -419,   150,
    -419,   134,   138,   140,   143,   161,   163,   165,   175,   176,
     177,   178,   194,   195,   196,   197,  1482,  1197,  1269,  -419,
    -419,  -419,  -419,  -419,  -419,  1197,  1197,  1197,  1197,  1197,
    1197,  1197,  1197,   732,    11,   971,  -419,  -419,  1457,   129,
     -46,  -419,  -419,  -419,   430,  1425,  -419,   125,   799,   184,
     -96,  -419,   799,  -419,  -419,  -419,  -419,  -419,   142,  -419,
     133,  -419,   732,   732,   732,   732,   732,   732,   732,   732,
     732,   732,   732,   732,   732,   732,   732,  -419,  -419,  -419,
    -419,  -419,  -419,  -419,  -419,  -419,   136,   164,   168,   172,
    -419,  -419,  -419,  -419,  -419,  -419,   309,  -419,  -419,   732,
    -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,   121,
    -419,   212,  -419,  -419,   253,   213,   217,  -419,  -419,   -48,
    1197,  1197,  1197,  1197,  1197,  1197,  1197,  1197,  1197,  1197,
    1197,  1197,  1197,  1197,  1197,  1197,  1197,  1197,  1197,  -419,
    -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,
    1197,   276,   277,  -419,  -419,   278,   732,  1197,   128,   229,
     230,   233,   656,   234,   235,  1197,   256,   236,   237,   291,
    1047,   260,  -419,  -419,  -419,   286,  -419,  -419,   239,   543,
    -419,  -419,  -419,  -419,  -419,  -101,   286,   240,   242,  -419,
    -419,   246,   299,  -419,   248,   799,  -419,  -419,  -419,   268,
    -419,  1197,  -419,   170,   249,    85,  -419,  -419,   799,  -419,
    -419,   247,   250,  -419,   251,   252,   254,   255,   257,   258,
     259,   262,   263,   265,   266,   267,   280,   288,  -419,  -419,
    -419,  -419,  -419,  -419,  -419,  -419,   273,  -419,  -419,   289,
    1197,  -419,  1197,  -419,   275,    11,  -419,   895,    79,  -419,
      79,   100,   100,   182,   182,   326,  1488,   -39,  1497,   315,
    1528,   100,   100,    47,    47,  -419,  -419,  -419,  -419,  -419,
    -419,  -419,   290,    -8,  -419,  -419,  1197,  1122,  1197,   337,
    1197,  1197,   285,  1457,   656,  -419,  -419,   281,  -419,   -16,
     656,   430,  -419,  -419,  -419,  -419,  -419,  1336,  -419,   283,
    -419,  -419,  -419,  -419,  -419,  -419,  -419,   294,  -419,   732,
    -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,  -419,
    -419,  -419,  -419,  -419,  1197,  -419,  -419,  -419,  -419,  -419,
    -419,  1197,  -419,  -419,   144,  1122,  1425,   146,   319,   148,
     151,   656,  -419,  -419,  -419,  -419,   317,  -419,  -419,  1425,
     331,  -419,  -419,  1425,  1457,   656,  1197,  1122,   656,  1197,
     656,  -419,  -419,  -419,   332,  -419,   333,   367,   341,   316,
    1197,  -419,   153,  -419,   382,  -419,   382,  -419,   656,   656,
     381,   386,  -419,   382,  -419,   382,  -419,  -419,   656,  -419,
    -419,  -419,  -419
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       2,     0,     1,     0,    17,    18,    19,    20,    21,    23,
      24,    25,    26,     0,     0,     0,     0,    11,    13,    12,
      14,    15,    27,    22,    28,     3,     5,    78,    10,    16,
      29,     4,     6,     7,    33,    34,    47,    48,    38,    39,
      43,    44,    96,    28,    90,    89,     0,     9,     0,    79,
      80,     0,    82,    95,     0,     0,     0,    51,     0,     0,
       0,     0,     8,     0,    91,    94,     0,     0,   100,     0,
      31,     0,    36,     0,     0,    97,    98,    99,    81,    82,
     261,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   255,
     256,   257,   258,   259,   260,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   267,     0,    83,    84,   152,   185,
     186,   233,   225,   263,     0,   104,   102,     0,    49,    76,
       0,    74,    49,    71,    72,    73,    57,    58,    52,    53,
       0,    41,   249,   249,   249,   249,   249,   249,   249,   249,
     249,   249,   249,   249,   249,   249,   249,   203,   204,   205,
     206,   207,   209,   210,   211,   212,     0,     0,     0,     0,
     214,   215,   213,   208,   216,   198,    92,   202,   199,     0,
     196,   187,   188,   189,   191,   192,   190,   193,   194,     0,
     150,     0,   271,   274,   273,     0,   268,   269,    87,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   155,
     156,   157,   158,   159,   160,   161,   162,   163,   164,   154,
       0,     0,     0,   231,   232,     0,   249,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   255,   128,   122,   119,    78,   126,   113,     0,     0,
     114,   115,   118,   116,   117,     0,   110,     0,   105,   106,
     103,     0,     0,    61,     0,    50,    59,    64,    65,     0,
      62,     0,    46,     0,     0,     0,    55,    56,    49,   253,
     254,     0,   250,   251,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   217,   218,
     223,   224,   219,   220,   221,   222,    93,   200,   201,     0,
       0,   262,     0,   272,     0,     0,    85,     0,   177,   185,
     178,   175,   176,   171,   172,   167,   166,     0,   168,   169,
     170,   173,   174,   179,   180,   181,   182,   183,   153,   229,
     230,   228,     0,     0,   120,   121,     0,   141,     0,     0,
       0,     0,     0,   165,     0,   145,   146,     0,   147,     0,
       0,     0,   112,   127,   129,   109,   101,     0,    66,     0,
      32,    60,    63,    77,    75,    37,    54,     0,   234,     0,
     235,   236,   237,   238,   239,   240,   241,   242,   243,   244,
     245,   246,   247,   248,   197,   151,   195,   264,   270,    86,
      88,     0,   227,   226,     0,     0,     0,     0,     0,     0,
       0,     0,   135,   149,   148,   136,     0,   108,   107,   104,
       0,    42,   252,   104,   184,     0,   143,     0,     0,     0,
       0,   132,   134,   123,     0,    69,     0,   130,     0,   144,
     143,   137,     0,   139,     0,    67,     0,   265,     0,     0,
       0,     0,   133,     0,    70,     0,   131,   140,     0,   138,
      68,   266,   142
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -419,  -419,  -419,     0,    -1,   -23,  -419,  -419,  -419,  -419,
    -419,  -419,  -419,  -419,  -419,  -120,  -419,  -419,   215,  -419,
     226,  -419,  -419,  -419,  -419,  -419,   -66,  -419,   219,  -419,
    -419,   440,  -106,  -419,   328,  -419,   -22,   454,  -419,  -418,
    -419,   131,   505,  -419,  -234,  -389,  -419,   139,  -419,  -343,
    -419,  -419,  -419,  -419,  -419,    57,  -419,  -111,   -63,  -419,
     228,  -174,   -52,   -79,  -419,   335,  -419,  -419,   -34,  -419,
     124,  -419,  -419,  -419,  -419,  -419,  -419,   187
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,    25,   254,   255,    28,    29,    30,    54,   128,
      56,   132,    57,   288,    55,   274,    74,   138,   139,   275,
     276,   277,   429,   463,   278,   456,   279,   130,   131,    48,
      49,    50,   116,   199,    51,   317,    79,    53,   125,   267,
     268,   269,   280,    67,   256,   257,   371,   258,   259,   260,
     261,   454,   262,   263,   416,   448,   264,   265,   190,   230,
     362,   118,   119,   290,   176,   177,   120,   121,   291,   292,
     293,   122,   123,   433,   465,   195,   196,   197
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      27,    26,   189,   117,    47,    52,   127,   140,   359,   198,
     374,   444,   284,   320,   415,   446,   282,   175,   283,   231,
     -30,   232,   233,   234,    61,   373,   328,   330,   331,   332,
     333,   334,   335,   336,   191,   338,   339,   340,   341,   342,
     343,   344,   345,   346,   347,   178,   180,   -40,    66,    32,
      33,   411,   117,   181,   182,   183,   184,   185,   186,   187,
     188,   235,   236,   237,   326,   462,   327,   464,   189,   192,
     -40,   363,   436,  -111,   470,   320,   471,    34,    35,   289,
     289,   289,   289,   289,   289,   289,   289,   289,   289,   289,
     289,   289,   289,   289,   450,   424,   -45,   337,   320,   193,
     319,   133,   134,   135,   194,    58,   320,   363,   413,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   -35,   266,    59,   353,    27,   273,    62,
     422,    27,   273,    70,    42,    60,   425,    68,    69,   369,
      42,    60,    63,   136,   137,   216,   217,   218,   329,   329,
     329,   329,   329,   329,   329,   329,    71,   329,   329,   329,
     329,   329,   329,   329,   329,   329,   329,   348,   387,    44,
     200,   201,    72,   289,    45,   214,   215,   216,   217,   218,
      64,    36,    37,    73,    46,    38,    39,   442,    40,    41,
      46,   286,   287,   329,   308,   309,   214,   215,   216,   217,
     218,   447,   352,    75,   451,    76,   453,   219,   220,   221,
     222,   223,   224,   225,   226,   227,   228,   229,    77,   140,
     124,   410,   310,   311,   466,   467,   312,   313,   129,   329,
     314,   315,    47,   141,   472,   320,   321,   434,    66,   354,
     355,   270,   142,    47,   375,   414,   143,   417,   144,   419,
     420,   145,   200,   201,   202,   203,   285,   405,   320,   435,
     320,   438,   320,   440,   117,   320,   441,   320,   461,   146,
     406,   147,   281,   148,    27,   273,   212,   213,   214,   215,
     216,   217,   218,   149,   150,   151,   152,    27,   273,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,   153,   154,   155,   156,    17,    18,    19,    20,
      21,   323,   157,   158,   159,   160,   161,   162,   163,   164,
     165,   166,   167,   168,   169,   449,   289,   322,   452,   324,
      22,   325,   170,   171,   349,   350,   351,   356,   357,   449,
      23,   358,   360,   361,    42,    43,   364,   365,   366,   367,
     370,   372,   406,   172,   378,   376,   377,   379,   382,   329,
     380,   385,   388,   173,   389,   418,   390,   391,   174,   392,
     393,    64,   394,   395,   396,   421,   266,   397,   398,    44,
     399,   400,   401,   407,    45,   200,   201,   202,   203,   204,
     205,   430,   423,   458,    46,   402,   200,   201,   202,   203,
     204,   205,    44,   403,   404,   412,   431,    45,   211,   212,
     213,   214,   215,   216,   217,   218,   437,   209,   210,   211,
     212,   213,   214,   215,   216,   217,   218,   439,   266,   443,
     320,   238,   266,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,   445,   455,   457,    80,
      17,    18,    19,    20,    21,   239,   459,   240,   241,   242,
     243,   244,   245,   246,   247,   248,   249,   250,    81,    82,
      83,    84,    85,    86,    22,    87,    88,    89,    90,    91,
      92,    93,    94,    95,    23,    96,    97,    98,   251,    24,
     100,   101,   102,   103,   104,   253,   468,   469,   105,   106,
     386,   381,   384,    78,   316,    65,    31,   460,   428,   383,
     426,   318,   408,   432,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   107,     0,     0,   108,   109,   110,     0,
       0,     0,     0,     0,     0,   111,   112,     0,   113,   114,
       0,   252,  -124,   253,   238,     0,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,     0,
       0,     0,    80,    17,    18,    19,    20,    21,   239,     0,
     240,   241,   242,   243,   244,   245,   246,   247,   248,   249,
     250,    81,    82,    83,    84,    85,    86,    22,    87,    88,
      89,    90,    91,    92,    93,    94,    95,    23,    96,    97,
      98,   251,    24,   100,   101,   102,   103,   104,     0,     0,
       0,   105,   106,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   107,     0,     0,   108,
     109,   110,     0,     0,     0,     0,     0,     0,   111,   112,
       0,   113,   114,     0,   252,  -125,   253,   238,     0,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,     0,     0,     0,    80,    17,    18,    19,    20,
      21,   239,     0,   240,   241,   242,   243,   244,   245,   246,
     247,   248,   249,   250,    81,    82,    83,    84,    85,    86,
      22,    87,    88,    89,    90,    91,    92,    93,    94,    95,
      23,    96,    97,    98,   251,    24,   100,   101,   102,   103,
     104,     0,     0,     0,   105,   106,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   157,   158,   159,   160,   161,
     162,   163,   164,   165,   166,   167,   168,   169,     0,   107,
       0,    80,   108,   109,   110,   170,   171,     0,     0,     0,
       0,   111,   112,     0,   113,   114,     0,   252,     0,   253,
      81,    82,    83,    84,    85,    86,   172,    87,    88,    89,
      90,    91,    92,    93,    94,    95,   173,    96,    97,    98,
      99,   174,   100,   101,   102,   103,   104,     0,     0,     0,
     105,   106,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,   133,   134,   135,     0,    17,
      18,    19,    20,    21,     0,   107,     0,     0,   108,   109,
     110,     0,     0,     0,     0,     0,     0,   111,   112,     0,
     113,   114,    80,    22,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    23,     0,     0,     0,   271,    24,     0,
       0,    81,    82,    83,    84,    85,    86,     0,    87,    88,
      89,    90,    91,    92,    93,    94,    95,     0,    96,    97,
      98,    99,     0,   100,   101,   102,   103,   104,     0,     0,
       0,   105,   106,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   272,     0,     0,     0,     0,
       0,     0,     0,     0,    80,     0,   107,     0,     0,   108,
     109,   110,     0,     0,     0,     0,     0,     0,   111,   112,
       0,   113,   114,    81,    82,    83,    84,    85,    86,   126,
      87,    88,    89,    90,    91,    92,    93,    94,    95,     0,
      96,    97,    98,    99,     0,   100,   101,   102,   103,   104,
       0,     0,     0,   105,   106,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   107,     0,
      80,   108,   109,   110,     0,     0,     0,     0,     0,     0,
     111,   112,     0,   113,   114,     0,     0,   409,   115,    81,
      82,    83,    84,    85,    86,     0,    87,    88,    89,    90,
      91,    92,    93,    94,    95,     0,    96,    97,    98,    99,
       0,   100,   101,   102,   103,   104,     0,     0,     0,   105,
     106,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   107,     0,    80,   108,   109,   110,
       0,     0,     0,     0,     0,     0,   111,   112,     0,   113,
     114,     0,     0,     0,   115,    81,    82,    83,    84,    85,
      86,     0,    87,    88,    89,    90,    91,    92,    93,    94,
      95,     0,    96,    97,    98,    99,     0,   100,   101,   102,
     103,   104,     0,     0,     0,   105,   106,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     107,    80,     0,   108,   109,   110,     0,     0,     0,     0,
       0,     0,   111,   112,     0,   113,   114,     0,   368,     0,
      81,    82,    83,    84,    85,    86,     0,    87,    88,    89,
      90,    91,    92,    93,    94,    95,     0,    96,    97,    98,
      99,     0,   100,   101,   102,   103,   104,     0,     0,     0,
     105,   106,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   107,    80,     0,   108,   109,
     110,     0,     0,     0,     0,     0,     0,   111,   112,     0,
     113,   114,     0,   252,     0,    81,    82,    83,    84,    85,
      86,     0,    87,    88,    89,    90,    91,    92,    93,    94,
      95,     0,    96,    97,    98,    99,     0,   100,   101,   102,
     103,   104,     0,     0,     0,   105,   106,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    80,     0,
     107,     0,     0,   108,   109,   110,     0,     0,     0,     0,
       0,     0,   111,   112,     0,   113,   114,    81,    82,    83,
      84,    85,    86,     0,    87,    88,    89,    90,    91,    92,
      93,    94,    95,     0,    96,    97,    98,    99,     0,   100,
     101,   102,   103,   104,     0,     0,     0,   105,   106,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,     0,     0,     0,     0,    17,    18,    19,    20,
      21,     0,   107,     0,     0,   108,   109,   110,     0,     0,
       0,     0,     0,     0,   111,   112,     0,   179,   114,     0,
      22,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      23,     0,     0,     0,     0,    24,     0,     0,     0,     0,
       2,     3,   427,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,     0,     0,     0,     0,
      17,    18,    19,    20,    21,     0,     0,     0,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,     0,     0,     0,    22,    17,    18,    19,    20,    21,
       0,     0,     0,     0,    23,     0,     0,     0,     0,    24,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    22,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    23,
       0,     0,     0,     0,    24,   157,   158,   159,   160,   161,
     162,   163,   164,   165,   166,   167,   168,   169,     0,     0,
       0,     0,     0,     0,     0,   170,   171,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   172,   200,   201,   202,
     203,   204,   205,   206,   207,     0,   173,     0,     0,     0,
       0,   174,     0,     0,     0,     0,   208,     0,   209,   210,
     211,   212,   213,   214,   215,   216,   217,   218,   200,   201,
     202,   203,   204,   205,   206,     0,     0,   200,   201,   202,
     203,   204,   205,     0,     0,     0,     0,     0,     0,   209,
     210,   211,   212,   213,   214,   215,   216,   217,   218,   210,
     211,   212,   213,   214,   215,   216,   217,   218,   200,   201,
     202,   203,   204,   205,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   212,   213,   214,   215,   216,   217,   218
};

static const yytype_int16 yycheck[] =
{
       1,     1,   113,    66,    27,    27,    69,    73,   242,   115,
     111,   429,   132,   114,   357,   433,   112,    96,   114,    65,
     113,    67,    68,    69,    46,   259,   200,   201,   202,   203,
     204,   205,   206,   207,   113,   209,   210,   211,   212,   213,
     214,   215,   216,   217,   218,    97,    98,    90,    88,   111,
     112,    90,   115,   105,   106,   107,   108,   109,   110,   111,
     112,   107,   108,   109,   112,   454,   114,   456,   179,    58,
     113,   245,   415,   113,   463,   114,   465,    58,    59,   142,
     143,   144,   145,   146,   147,   148,   149,   150,   151,   152,
     153,   154,   155,   156,   437,   111,   113,   208,   114,    88,
     179,    16,    17,    18,    93,    67,   114,   281,   116,   143,
     144,   145,   146,   147,   148,   149,   150,   151,   152,   153,
     154,   155,   156,   113,   125,    67,   237,   128,   128,   111,
     364,   132,   132,   113,    58,    59,   370,   108,   109,   250,
      58,    59,   114,    58,    59,    98,    99,   100,   200,   201,
     202,   203,   204,   205,   206,   207,   113,   209,   210,   211,
     212,   213,   214,   215,   216,   217,   218,   230,   288,    93,
      70,    71,   113,   236,    98,    96,    97,    98,    99,   100,
      98,    58,    59,    90,   108,    58,    59,   421,    58,    59,
     108,    58,    59,   245,    58,    59,    96,    97,    98,    99,
     100,   435,   236,    58,   438,    58,   440,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    87,    88,   115,   285,
     113,   327,    58,    59,   458,   459,    58,    59,    58,   281,
      58,    59,   255,   113,   468,   114,   115,   411,    88,   111,
     112,   116,   108,   266,   266,   356,   108,   358,   108,   360,
     361,   108,    70,    71,    72,    73,   114,   320,   114,   115,
     114,   115,   114,   115,   327,   114,   115,   114,   115,   108,
     322,   108,    88,   108,   275,   275,    94,    95,    96,    97,
      98,    99,   100,   108,   108,   108,   108,   288,   288,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,   108,   108,   108,   108,    20,    21,    22,    23,
      24,    58,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,   436,   389,   115,   439,   116,
      44,   114,    23,    24,    58,    58,    58,   108,   108,   450,
      54,   108,   108,   108,    58,    59,    90,   111,   111,    58,
      90,   112,   404,    44,   108,   115,   114,    58,    90,   411,
     112,   112,   115,    54,   114,    28,   115,   115,    59,   115,
     115,    98,   115,   115,   115,    90,   377,   115,   115,    93,
     115,   115,   115,   108,    98,    70,    71,    72,    73,    74,
      75,   108,   111,    26,   108,   115,    70,    71,    72,    73,
      74,    75,    93,   115,   115,   115,   112,    98,    93,    94,
      95,    96,    97,    98,    99,   100,   416,    91,    92,    93,
      94,    95,    96,    97,    98,    99,   100,   108,   429,   112,
     114,     1,   433,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,   115,   115,   115,    19,
      20,    21,    22,    23,    24,    25,   115,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,    52,    53,    54,    55,    56,    57,    58,    59,
      60,    61,    62,    63,    64,   113,   115,   111,    68,    69,
     285,   275,   283,    63,   176,    51,     1,   450,   377,   281,
     371,   176,   325,   389,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    93,    -1,    -1,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,   105,   106,    -1,   108,   109,
      -1,   111,   112,   113,     1,    -1,     3,     4,     5,     6,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    -1,
      -1,    -1,    19,    20,    21,    22,    23,    24,    25,    -1,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,    48,    49,    50,    51,    52,    53,    54,    55,    56,
      57,    58,    59,    60,    61,    62,    63,    64,    -1,    -1,
      -1,    68,    69,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    93,    -1,    -1,    96,
      97,    98,    -1,    -1,    -1,    -1,    -1,    -1,   105,   106,
      -1,   108,   109,    -1,   111,   112,   113,     1,    -1,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    -1,    -1,    -1,    19,    20,    21,    22,    23,
      24,    25,    -1,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    45,    46,    47,    48,    49,    50,    51,    52,    53,
      54,    55,    56,    57,    58,    59,    60,    61,    62,    63,
      64,    -1,    -1,    -1,    68,    69,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    -1,    93,
      -1,    19,    96,    97,    98,    23,    24,    -1,    -1,    -1,
      -1,   105,   106,    -1,   108,   109,    -1,   111,    -1,   113,
      38,    39,    40,    41,    42,    43,    44,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    57,
      58,    59,    60,    61,    62,    63,    64,    -1,    -1,    -1,
      68,    69,     3,     4,     5,     6,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    18,    -1,    20,
      21,    22,    23,    24,    -1,    93,    -1,    -1,    96,    97,
      98,    -1,    -1,    -1,    -1,    -1,    -1,   105,   106,    -1,
     108,   109,    19,    44,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    54,    -1,    -1,    -1,    58,    59,    -1,
      -1,    38,    39,    40,    41,    42,    43,    -1,    45,    46,
      47,    48,    49,    50,    51,    52,    53,    -1,    55,    56,
      57,    58,    -1,    60,    61,    62,    63,    64,    -1,    -1,
      -1,    68,    69,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   106,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    19,    -1,    93,    -1,    -1,    96,
      97,    98,    -1,    -1,    -1,    -1,    -1,    -1,   105,   106,
      -1,   108,   109,    38,    39,    40,    41,    42,    43,   116,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    -1,
      55,    56,    57,    58,    -1,    60,    61,    62,    63,    64,
      -1,    -1,    -1,    68,    69,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    93,    -1,
      19,    96,    97,    98,    -1,    -1,    -1,    -1,    -1,    -1,
     105,   106,    -1,   108,   109,    -1,    -1,   112,   113,    38,
      39,    40,    41,    42,    43,    -1,    45,    46,    47,    48,
      49,    50,    51,    52,    53,    -1,    55,    56,    57,    58,
      -1,    60,    61,    62,    63,    64,    -1,    -1,    -1,    68,
      69,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    93,    -1,    19,    96,    97,    98,
      -1,    -1,    -1,    -1,    -1,    -1,   105,   106,    -1,   108,
     109,    -1,    -1,    -1,   113,    38,    39,    40,    41,    42,
      43,    -1,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    -1,    55,    56,    57,    58,    -1,    60,    61,    62,
      63,    64,    -1,    -1,    -1,    68,    69,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      93,    19,    -1,    96,    97,    98,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,    -1,   108,   109,    -1,   111,    -1,
      38,    39,    40,    41,    42,    43,    -1,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    -1,    55,    56,    57,
      58,    -1,    60,    61,    62,    63,    64,    -1,    -1,    -1,
      68,    69,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    93,    19,    -1,    96,    97,
      98,    -1,    -1,    -1,    -1,    -1,    -1,   105,   106,    -1,
     108,   109,    -1,   111,    -1,    38,    39,    40,    41,    42,
      43,    -1,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    -1,    55,    56,    57,    58,    -1,    60,    61,    62,
      63,    64,    -1,    -1,    -1,    68,    69,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    19,    -1,
      93,    -1,    -1,    96,    97,    98,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,    -1,   108,   109,    38,    39,    40,
      41,    42,    43,    -1,    45,    46,    47,    48,    49,    50,
      51,    52,    53,    -1,    55,    56,    57,    58,    -1,    60,
      61,    62,    63,    64,    -1,    -1,    -1,    68,    69,     3,
       4,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    -1,    -1,    -1,    -1,    20,    21,    22,    23,
      24,    -1,    93,    -1,    -1,    96,    97,    98,    -1,    -1,
      -1,    -1,    -1,    -1,   105,   106,    -1,   108,   109,    -1,
      44,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      54,    -1,    -1,    -1,    -1,    59,    -1,    -1,    -1,    -1,
       0,     1,    66,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    -1,    -1,    -1,    -1,
      20,    21,    22,    23,    24,    -1,    -1,    -1,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    -1,    -1,    -1,    44,    20,    21,    22,    23,    24,
      -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,    59,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    44,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,    59,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    23,    24,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    44,    70,    71,    72,
      73,    74,    75,    76,    77,    -1,    54,    -1,    -1,    -1,
      -1,    59,    -1,    -1,    -1,    -1,    89,    -1,    91,    92,
      93,    94,    95,    96,    97,    98,    99,   100,    70,    71,
      72,    73,    74,    75,    76,    -1,    -1,    70,    71,    72,
      73,    74,    75,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    94,    95,    96,    97,    98,    99,   100,    92,
      93,    94,    95,    96,    97,    98,    99,   100,    70,    71,
      72,    73,    74,    75,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    94,    95,    96,    97,    98,    99,   100
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   118,     0,     1,     3,     4,     5,     6,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    20,    21,    22,
      23,    24,    44,    54,    59,   119,   120,   121,   122,   123,
     124,   159,   111,   112,    58,    59,    58,    59,    58,    59,
      58,    59,    58,    59,    93,    98,   108,   122,   146,   147,
     148,   151,   153,   154,   125,   131,   127,   129,    67,    67,
      59,   153,   111,   114,    98,   154,    88,   160,   108,   109,
     113,   113,   113,    90,   133,    58,    58,   115,   148,   153,
      19,    38,    39,    40,    41,    42,    43,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    55,    56,    57,    58,
      60,    61,    62,    63,    64,    68,    69,    93,    96,    97,
      98,   105,   106,   108,   109,   113,   149,   175,   178,   179,
     183,   184,   188,   189,   113,   155,   116,   175,   126,    58,
     144,   145,   128,    16,    17,    18,    58,    59,   134,   135,
     143,   113,   108,   108,   108,   108,   108,   108,   108,   108,
     108,   108,   108,   108,   108,   108,   108,     3,     4,     5,
       6,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      23,    24,    44,    54,    59,   180,   181,   182,   179,   108,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   174,
     175,   180,    58,    88,    93,   192,   193,   194,   149,   150,
      70,    71,    72,    73,    74,    75,    76,    77,    89,    91,
      92,    93,    94,    95,    96,    97,    98,    99,   100,    78,
      79,    80,    81,    82,    83,    84,    85,    86,    87,    88,
     176,    65,    67,    68,    69,   107,   108,   109,     1,    25,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    58,   111,   113,   120,   121,   161,   162,   164,   165,
     166,   167,   169,   170,   173,   174,   121,   156,   157,   158,
     116,    58,   106,   120,   132,   136,   137,   138,   141,   143,
     159,    88,   112,   114,   132,   114,    58,    59,   130,   175,
     180,   185,   186,   187,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,    58,    59,
      58,    59,    58,    59,    58,    59,   151,   152,   182,   180,
     114,   115,   115,    58,   116,   114,   112,   114,   178,   179,
     178,   178,   178,   178,   178,   178,   178,   174,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   175,    58,
      58,    58,   185,   174,   111,   112,   108,   108,   108,   161,
     108,   108,   177,   178,    90,   111,   111,    58,   111,   174,
      90,   163,   112,   161,   111,   153,   115,   114,   108,    58,
     112,   137,    90,   177,   145,   112,   135,   132,   115,   114,
     115,   115,   115,   115,   115,   115,   115,   115,   115,   115,
     115,   115,   115,   115,   115,   175,   179,   108,   194,   112,
     149,    90,   115,   116,   174,   166,   171,   174,    28,   174,
     174,    90,   161,   111,   111,   161,   164,    66,   158,   139,
     108,   112,   187,   190,   178,   115,   166,   120,   115,   108,
     115,   115,   161,   112,   156,   115,   156,   161,   172,   174,
     166,   161,   174,   161,   168,   115,   142,   115,    26,   115,
     172,   115,   162,   140,   162,   191,   161,   161,   115,   111,
     162,   162,   161
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   117,   118,   118,   119,   119,   119,   119,   120,   121,
     121,   122,   122,   122,   122,   122,   122,   123,   123,   123,
     123,   123,   123,   123,   123,   123,   123,   123,   123,   123,
     125,   126,   124,   124,   124,   127,   128,   124,   124,   124,
     129,   130,   124,   124,   124,   131,   124,   124,   124,   132,
     132,   133,   133,   134,   134,   135,   135,   135,   135,   136,
     136,   137,   137,   137,   137,   137,   139,   140,   138,   142,
     141,   143,   143,   143,   144,   144,   145,   145,   146,   146,
     147,   147,   148,   148,   149,   149,   149,   150,   150,   151,
     151,   151,   152,   152,   153,   153,   154,   154,   154,   154,
     155,   154,   154,   154,   156,   156,   157,   157,   157,   158,
     158,   160,   159,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   163,   162,   164,   164,   165,   165,   166,   166,
     167,   167,   168,   167,   169,   169,   169,   170,   170,   170,
     170,   171,   170,   172,   172,   173,   173,   173,   173,   173,
     174,   174,   175,   175,   176,   176,   176,   176,   176,   176,
     176,   176,   176,   176,   176,   177,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   179,
     180,   181,   181,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   183,   183,   183,   183,   183,
     183,   183,   183,   183,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   185,
     185,   186,   186,   187,   187,   188,   188,   188,   188,   188,
     188,   188,   188,   188,   190,   191,   189,   192,   192,   193,
     193,   194,   194,   194,   194
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     2,     1,     1,     2,     2,     3,     2,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       0,     0,     7,     2,     2,     0,     0,     7,     2,     2,
       0,     0,     8,     2,     2,     0,     6,     2,     2,     0,
       1,     0,     2,     1,     3,     2,     2,     1,     1,     1,
       2,     1,     1,     2,     1,     1,     0,     0,     7,     0,
       6,     1,     1,     1,     1,     3,     1,     3,     0,     1,
       1,     3,     1,     3,     1,     3,     4,     1,     3,     1,
       1,     2,     0,     1,     2,     1,     1,     3,     3,     3,
       0,     5,     3,     4,     0,     1,     1,     3,     3,     2,
       1,     0,     6,     1,     1,     1,     1,     1,     1,     1,
       2,     2,     0,     4,     0,     1,     1,     2,     1,     2,
       5,     7,     0,     6,     4,     3,     3,     5,     7,     5,
       7,     0,     8,     0,     1,     2,     2,     2,     3,     3,
       1,     3,     1,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     5,     1,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     4,     2,     4,     2,     2,
       2,     2,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     1,     4,     4,     3,     3,
       3,     2,     2,     1,     4,     4,     4,     4,     4,     4,
       4,     4,     4,     4,     4,     4,     4,     4,     4,     0,
       1,     1,     3,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     3,     1,     0,     0,     9,     0,     1,     1,
       3,     1,     2,     1,     1
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
#line 70 "src/parser.y"
                  {
          yyval.node = mkNode(ASTKind::Program, "translation_unit");
          g_astRoot = yyval.node;
      }
#line 2242 "build/parser.tab.cpp"
    break;

  case 3: /* translation_unit: translation_unit external_decl  */
#line 74 "src/parser.y"
                                     {
          yyval = yyvsp[-1];
          addChild(yyval.node, yyvsp[0].node);
          g_astRoot = yyval.node;
      }
#line 2252 "build/parser.tab.cpp"
    break;

  case 4: /* external_decl: function_definition  */
#line 82 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2258 "build/parser.tab.cpp"
    break;

  case 5: /* external_decl: declaration  */
#line 83 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2264 "build/parser.tab.cpp"
    break;

  case 6: /* external_decl: error ';'  */
#line 84 "src/parser.y"
                 { yyerrok; yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2270 "build/parser.tab.cpp"
    break;

  case 7: /* external_decl: error '}'  */
#line 85 "src/parser.y"
                 { yyerrok; yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 2276 "build/parser.tab.cpp"
    break;

  case 8: /* declaration: declaration_specifiers init_declarator_list_opt ';'  */
#line 92 "src/parser.y"
                                                          {
          std::vector<ASTNodePtr> declNodes;
          for (auto &d : yyvsp[-1].paramList) {
              auto n = registerDeclarator(d, yyvsp[-2].typeSpec);
              if (n) declNodes.push_back(n);
          }
          if (declNodes.empty()) {
              yyval.node = yyvsp[-2].node; /* bare struct/class/enum/union declaration */
          } else if (declNodes.size() == 1 && !yyvsp[-2].node) {
              yyval.node = declNodes[0];
          } else {
              auto grp = mkNode(ASTKind::DeclGroup);
              if (yyvsp[-2].node) addChild(grp, yyvsp[-2].node);
              for (auto &n : declNodes) addChild(grp, n);
              yyval.node = grp;
          }
      }
#line 2298 "build/parser.tab.cpp"
    break;

  case 9: /* declaration_specifiers: declaration_specifiers storage_or_type_specifier  */
#line 112 "src/parser.y"
                                                       {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
          if (yyvsp[0].typeSpec.isStatic) yyval.typeSpec.isStatic = true;
          if (yyvsp[0].typeSpec.isTypedefStorage) yyval.typeSpec.isTypedefStorage = true;
          if (yyvsp[0].typeSpec.isConst) yyval.typeSpec.isConst = true;
          if (yyvsp[0].typeSpec.isVolatile) yyval.typeSpec.isVolatile = true;
          if (yyvsp[0].node) yyval.node = yyvsp[0].node;
      }
#line 2312 "build/parser.tab.cpp"
    break;

  case 10: /* declaration_specifiers: storage_or_type_specifier  */
#line 121 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2318 "build/parser.tab.cpp"
    break;

  case 11: /* storage_or_type_specifier: STATIC  */
#line 125 "src/parser.y"
               { yyval.typeSpec.isStatic = true; }
#line 2324 "build/parser.tab.cpp"
    break;

  case 12: /* storage_or_type_specifier: AUTO  */
#line 126 "src/parser.y"
               { yyval = ParserValue(); }
#line 2330 "build/parser.tab.cpp"
    break;

  case 13: /* storage_or_type_specifier: TYPEDEF  */
#line 127 "src/parser.y"
               { yyval.typeSpec.isTypedefStorage = true; }
#line 2336 "build/parser.tab.cpp"
    break;

  case 14: /* storage_or_type_specifier: CONST  */
#line 128 "src/parser.y"
               { yyval.typeSpec.isConst = true; }
#line 2342 "build/parser.tab.cpp"
    break;

  case 15: /* storage_or_type_specifier: VOLATILE  */
#line 129 "src/parser.y"
               { yyval.typeSpec.isVolatile = true; }
#line 2348 "build/parser.tab.cpp"
    break;

  case 16: /* storage_or_type_specifier: type_specifier  */
#line 130 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 2354 "build/parser.tab.cpp"
    break;

  case 17: /* type_specifier: INT  */
#line 134 "src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); }
#line 2360 "build/parser.tab.cpp"
    break;

  case 18: /* type_specifier: CHAR  */
#line 135 "src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); }
#line 2366 "build/parser.tab.cpp"
    break;

  case 19: /* type_specifier: FLOAT  */
#line 136 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 2372 "build/parser.tab.cpp"
    break;

  case 20: /* type_specifier: DOUBLE  */
#line 137 "src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 2378 "build/parser.tab.cpp"
    break;

  case 21: /* type_specifier: VOID  */
#line 138 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); }
#line 2384 "build/parser.tab.cpp"
    break;

  case 22: /* type_specifier: BOOL  */
#line 139 "src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); }
#line 2390 "build/parser.tab.cpp"
    break;

  case 23: /* type_specifier: SHORT  */
#line 140 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); }
#line 2396 "build/parser.tab.cpp"
    break;

  case 24: /* type_specifier: LONG  */
#line 141 "src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); }
#line 2402 "build/parser.tab.cpp"
    break;

  case 25: /* type_specifier: SIGNED  */
#line 142 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 2408 "build/parser.tab.cpp"
    break;

  case 26: /* type_specifier: UNSIGNED  */
#line 143 "src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 2414 "build/parser.tab.cpp"
    break;

  case 27: /* type_specifier: FILE_KW  */
#line 144 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FILE"); }
#line 2420 "build/parser.tab.cpp"
    break;

  case 28: /* type_specifier: TYPE_NAME  */
#line 145 "src/parser.y"
                {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
      }
#line 2430 "build/parser.tab.cpp"
    break;

  case 29: /* type_specifier: struct_or_class_specifier  */
#line 150 "src/parser.y"
                                { yyval = yyvsp[0]; }
#line 2436 "build/parser.tab.cpp"
    break;

  case 30: /* $@1: %empty  */
#line 154 "src/parser.y"
                        {
          declareSymbol(yyvsp[0].str, SymKind::STRUCT_TAG, "STRUCT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "STRUCT");
          enterClass(yyvsp[0].str);
      }
#line 2446 "build/parser.tab.cpp"
    break;

  case 31: /* $@2: %empty  */
#line 158 "src/parser.y"
            { pushScope("struct " + yyvsp[-2].str); }
#line 2452 "build/parser.tab.cpp"
    break;

  case 32: /* struct_or_class_specifier: STRUCT IDENTIFIER $@1 '{' $@2 member_decl_list_opt '}'  */
#line 158 "src/parser.y"
                                                                        {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("STRUCT");
          g_typedefNames.insert(yyvsp[-5].str); /* usable as a type from here on, but
                                             NOT inside its own body -- lets
                                             constructors/destructors keep
                                             matching the class's own name as
                                             a plain IDENTIFIER */
          auto node = mkNode(ASTKind::StructDecl, yyvsp[-5].str);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2469 "build/parser.tab.cpp"
    break;

  case 33: /* struct_or_class_specifier: STRUCT IDENTIFIER  */
#line 170 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
      }
#line 2479 "build/parser.tab.cpp"
    break;

  case 34: /* struct_or_class_specifier: STRUCT TYPE_NAME  */
#line 175 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
      }
#line 2489 "build/parser.tab.cpp"
    break;

  case 35: /* $@3: %empty  */
#line 180 "src/parser.y"
                       {
          declareSymbol(yyvsp[0].str, SymKind::UNION_TAG, "UNION", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "UNION");
          enterClass(yyvsp[0].str);
      }
#line 2499 "build/parser.tab.cpp"
    break;

  case 36: /* $@4: %empty  */
#line 184 "src/parser.y"
            { pushScope("union " + yyvsp[-2].str); }
#line 2505 "build/parser.tab.cpp"
    break;

  case 37: /* struct_or_class_specifier: UNION IDENTIFIER $@3 '{' $@4 member_decl_list_opt '}'  */
#line 184 "src/parser.y"
                                                                       {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("UNION");
          g_typedefNames.insert(yyvsp[-5].str);
          auto node = mkNode(ASTKind::UnionDecl, yyvsp[-5].str);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2518 "build/parser.tab.cpp"
    break;

  case 38: /* struct_or_class_specifier: UNION IDENTIFIER  */
#line 192 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
      }
#line 2528 "build/parser.tab.cpp"
    break;

  case 39: /* struct_or_class_specifier: UNION TYPE_NAME  */
#line 197 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
      }
#line 2538 "build/parser.tab.cpp"
    break;

  case 40: /* $@5: %empty  */
#line 202 "src/parser.y"
                       {
          declareSymbol(yyvsp[0].str, SymKind::CLASS_TAG, "CLASS", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "CLASS");
          enterClass(yyvsp[0].str);
      }
#line 2548 "build/parser.tab.cpp"
    break;

  case 41: /* $@6: %empty  */
#line 206 "src/parser.y"
                            { pushScope("class " + yyvsp[-3].str); }
#line 2554 "build/parser.tab.cpp"
    break;

  case 42: /* struct_or_class_specifier: CLASS IDENTIFIER $@5 inheritance_opt '{' $@6 member_decl_list_opt '}'  */
#line 206 "src/parser.y"
                                                                                       {
          popScope(); leaveClass();
          yyval.typeSpec.parts.push_back("CLASS");
          g_typedefNames.insert(yyvsp[-6].str);
          std::string label = yyvsp[-6].str;
          if (!yyvsp[-4].str.empty()) label += " : " + yyvsp[-4].str;
          auto node = mkNode(ASTKind::ClassDecl, label);
          for (auto &m : yyvsp[-1].nodeList) addChild(node, m);
          yyval.node = node;
      }
#line 2569 "build/parser.tab.cpp"
    break;

  case 43: /* struct_or_class_specifier: CLASS IDENTIFIER  */
#line 216 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
      }
#line 2579 "build/parser.tab.cpp"
    break;

  case 44: /* struct_or_class_specifier: CLASS TYPE_NAME  */
#line 221 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
      }
#line 2589 "build/parser.tab.cpp"
    break;

  case 45: /* $@7: %empty  */
#line 226 "src/parser.y"
                      {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_TAG, "ENUM", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM");
      }
#line 2598 "build/parser.tab.cpp"
    break;

  case 46: /* struct_or_class_specifier: ENUM IDENTIFIER $@7 '{' enumerator_list '}'  */
#line 229 "src/parser.y"
                                {
          yyval.typeSpec.parts.push_back("ENUM");
          g_typedefNames.insert(yyvsp[-4].str);
          auto node = mkNode(ASTKind::EnumDecl, yyvsp[-4].str);
          for (auto &e : yyvsp[-1].nodeList) addChild(node, e);
          yyval.node = node;
      }
#line 2610 "build/parser.tab.cpp"
    break;

  case 47: /* struct_or_class_specifier: ENUM IDENTIFIER  */
#line 236 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
      }
#line 2620 "build/parser.tab.cpp"
    break;

  case 48: /* struct_or_class_specifier: ENUM TYPE_NAME  */
#line 241 "src/parser.y"
                     {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
      }
#line 2630 "build/parser.tab.cpp"
    break;

  case 49: /* member_decl_list_opt: %empty  */
#line 249 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2636 "build/parser.tab.cpp"
    break;

  case 50: /* member_decl_list_opt: member_decl_list  */
#line 250 "src/parser.y"
                       { yyval = yyvsp[0]; }
#line 2642 "build/parser.tab.cpp"
    break;

  case 51: /* inheritance_opt: %empty  */
#line 254 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2648 "build/parser.tab.cpp"
    break;

  case 52: /* inheritance_opt: ':' inheritance_specifier_list  */
#line 255 "src/parser.y"
                                     { yyval.str = yyvsp[0].str; }
#line 2654 "build/parser.tab.cpp"
    break;

  case 53: /* inheritance_specifier_list: inheritance_specifier  */
#line 259 "src/parser.y"
                            { yyval.str = yyvsp[0].str; }
#line 2660 "build/parser.tab.cpp"
    break;

  case 54: /* inheritance_specifier_list: inheritance_specifier_list ',' inheritance_specifier  */
#line 260 "src/parser.y"
                                                           { yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str; }
#line 2666 "build/parser.tab.cpp"
    break;

  case 55: /* inheritance_specifier: access_specifier IDENTIFIER  */
#line 264 "src/parser.y"
                                  {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
      }
#line 2676 "build/parser.tab.cpp"
    break;

  case 56: /* inheritance_specifier: access_specifier TYPE_NAME  */
#line 269 "src/parser.y"
                                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
      }
#line 2686 "build/parser.tab.cpp"
    break;

  case 57: /* inheritance_specifier: IDENTIFIER  */
#line 274 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.str = yyvsp[0].str;
      }
#line 2696 "build/parser.tab.cpp"
    break;

  case 58: /* inheritance_specifier: TYPE_NAME  */
#line 279 "src/parser.y"
                {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.str = yyvsp[0].str;
      }
#line 2706 "build/parser.tab.cpp"
    break;

  case 59: /* member_decl_list: member_item  */
#line 287 "src/parser.y"
                  { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 2712 "build/parser.tab.cpp"
    break;

  case 60: /* member_decl_list: member_decl_list member_item  */
#line 288 "src/parser.y"
                                   { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 2718 "build/parser.tab.cpp"
    break;

  case 61: /* member_item: declaration  */
#line 292 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 2724 "build/parser.tab.cpp"
    break;

  case 62: /* member_item: function_definition  */
#line 293 "src/parser.y"
                          { yyval.node = yyvsp[0].node; }
#line 2730 "build/parser.tab.cpp"
    break;

  case 63: /* member_item: access_specifier ':'  */
#line 294 "src/parser.y"
                           { yyval = ParserValue(); }
#line 2736 "build/parser.tab.cpp"
    break;

  case 64: /* member_item: constructor_def  */
#line 295 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 2742 "build/parser.tab.cpp"
    break;

  case 65: /* member_item: destructor_def  */
#line 296 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 2748 "build/parser.tab.cpp"
    break;

  case 66: /* $@8: %empty  */
#line 300 "src/parser.y"
                     { pushScope(currentClassName() + "::" + yyvsp[-1].str + "()"); }
#line 2754 "build/parser.tab.cpp"
    break;

  case 67: /* $@9: %empty  */
#line 300 "src/parser.y"
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
#line 2770 "build/parser.tab.cpp"
    break;

  case 68: /* constructor_def: IDENTIFIER '(' $@8 parameter_list_opt ')' $@9 compound_stmt  */
#line 310 "src/parser.y"
                      {
          popScope();
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[-3].paramList) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[-6].str, paramTypes, currentClassName());
          SymbolDeclInfo extra;
          extra.tokenIdx = yyvsp[-6].idx;
          extra.returnType = "VOID";
          extra.paramTypes = paramTypes;
          extra.mangledName = mangled;
          declareSymbol(yyvsp[-6].str, SymKind::PROCEDURE, "CONSTRUCTOR", extra);
          auto node = mkNode(ASTKind::ConstructorDef, yyvsp[-6].str + " : " + mangled);
          for (auto &p : yyvsp[-3].paramList) {
              if (!p.name.empty()) addChild(node, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
          }
          addChild(node, yyvsp[0].node);
          yyval.node = node;
      }
#line 2793 "build/parser.tab.cpp"
    break;

  case 69: /* $@10: %empty  */
#line 331 "src/parser.y"
                             {
          setCategory(yyvsp[-2].idx, "DESTRUCTOR");
          pushScope(currentClassName() + "::~" + yyvsp[-2].str + "()");
      }
#line 2802 "build/parser.tab.cpp"
    break;

  case 70: /* destructor_def: '~' IDENTIFIER '(' ')' $@10 compound_stmt  */
#line 334 "src/parser.y"
                      {
          popScope();
          std::string mangled = mangle("~" + yyvsp[-4].str, {}, currentClassName());
          SymbolDeclInfo extra;
          extra.tokenIdx = yyvsp[-4].idx;
          extra.returnType = "VOID";
          extra.mangledName = mangled;
          declareSymbol("~" + yyvsp[-4].str, SymKind::PROCEDURE, "DESTRUCTOR", extra);
          auto node = mkNode(ASTKind::DestructorDef, yyvsp[-4].str + " : " + mangled);
          addChild(node, yyvsp[0].node);
          yyval.node = node;
      }
#line 2819 "build/parser.tab.cpp"
    break;

  case 74: /* enumerator_list: enumerator  */
#line 355 "src/parser.y"
                 { yyval.nodeList.push_back(yyvsp[0].node); }
#line 2825 "build/parser.tab.cpp"
    break;

  case 75: /* enumerator_list: enumerator_list ',' enumerator  */
#line 356 "src/parser.y"
                                     { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 2831 "build/parser.tab.cpp"
    break;

  case 76: /* enumerator: IDENTIFIER  */
#line 360 "src/parser.y"
                 {
          declareSymbol(yyvsp[0].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[0].idx});
          setCategory(yyvsp[0].idx, "ENUM_CONSTANT");
          yyval.node = mkNode(ASTKind::Enumerator, yyvsp[0].str);
      }
#line 2841 "build/parser.tab.cpp"
    break;

  case 77: /* enumerator: IDENTIFIER '=' constant_expr  */
#line 365 "src/parser.y"
                                   {
          declareSymbol(yyvsp[-2].str, SymKind::ENUM_CONST, "ENUM_CONSTANT", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "ENUM_CONSTANT");
          yyval.node = mkNode(ASTKind::Enumerator, yyvsp[-2].str, {yyvsp[0].node});
      }
#line 2851 "build/parser.tab.cpp"
    break;

  case 78: /* init_declarator_list_opt: %empty  */
#line 373 "src/parser.y"
                  { yyval = ParserValue(); }
#line 2857 "build/parser.tab.cpp"
    break;

  case 79: /* init_declarator_list_opt: init_declarator_list  */
#line 374 "src/parser.y"
                           { yyval = yyvsp[0]; }
#line 2863 "build/parser.tab.cpp"
    break;

  case 80: /* init_declarator_list: init_declarator  */
#line 378 "src/parser.y"
                      { yyval.paramList.push_back(yyvsp[0].decl); }
#line 2869 "build/parser.tab.cpp"
    break;

  case 81: /* init_declarator_list: init_declarator_list ',' init_declarator  */
#line 379 "src/parser.y"
                                               { yyval = yyvsp[-2]; yyval.paramList.push_back(yyvsp[0].decl); }
#line 2875 "build/parser.tab.cpp"
    break;

  case 82: /* init_declarator: declarator  */
#line 383 "src/parser.y"
                 { yyval.decl = yyvsp[0].decl; }
#line 2881 "build/parser.tab.cpp"
    break;

  case 83: /* init_declarator: declarator '=' initializer  */
#line 384 "src/parser.y"
                                 { yyval.decl = yyvsp[-2].decl; yyval.decl.initExpr = yyvsp[0].node; }
#line 2887 "build/parser.tab.cpp"
    break;

  case 84: /* initializer: assignment_expr  */
#line 388 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 2893 "build/parser.tab.cpp"
    break;

  case 85: /* initializer: '{' initializer_list '}'  */
#line 389 "src/parser.y"
                               {
          auto n = mkNode(ASTKind::InitializerList);
          for (auto &c : yyvsp[-1].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 2903 "build/parser.tab.cpp"
    break;

  case 86: /* initializer: '{' initializer_list ',' '}'  */
#line 394 "src/parser.y"
                                   {
          auto n = mkNode(ASTKind::InitializerList);
          for (auto &c : yyvsp[-2].nodeList) addChild(n, c);
          yyval.node = n;
      }
#line 2913 "build/parser.tab.cpp"
    break;

  case 87: /* initializer_list: initializer  */
#line 402 "src/parser.y"
                  { yyval.nodeList.push_back(yyvsp[0].node); }
#line 2919 "build/parser.tab.cpp"
    break;

  case 88: /* initializer_list: initializer_list ',' initializer  */
#line 403 "src/parser.y"
                                       { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 2925 "build/parser.tab.cpp"
    break;

  case 89: /* pointer: '*'  */
#line 410 "src/parser.y"
                  { yyval.decl.pointerLevel = 1; }
#line 2931 "build/parser.tab.cpp"
    break;

  case 90: /* pointer: '&'  */
#line 411 "src/parser.y"
                  { yyval.decl.pointerLevel = 1; }
#line 2937 "build/parser.tab.cpp"
    break;

  case 91: /* pointer: pointer '*'  */
#line 412 "src/parser.y"
                  { yyval = yyvsp[-1]; yyval.decl.pointerLevel++; }
#line 2943 "build/parser.tab.cpp"
    break;

  case 92: /* pointer_opt: %empty  */
#line 416 "src/parser.y"
                  { yyval.decl.pointerLevel = 0; }
#line 2949 "build/parser.tab.cpp"
    break;

  case 93: /* pointer_opt: pointer  */
#line 417 "src/parser.y"
                  { yyval = yyvsp[0]; }
#line 2955 "build/parser.tab.cpp"
    break;

  case 94: /* declarator: pointer direct_declarator  */
#line 421 "src/parser.y"
                                {
          yyval = yyvsp[0];
          yyval.decl.pointerLevel += yyvsp[-1].decl.pointerLevel;
      }
#line 2964 "build/parser.tab.cpp"
    break;

  case 95: /* declarator: direct_declarator  */
#line 425 "src/parser.y"
                        { yyval = yyvsp[0]; }
#line 2970 "build/parser.tab.cpp"
    break;

  case 96: /* direct_declarator: IDENTIFIER  */
#line 429 "src/parser.y"
                 {
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
      }
#line 2979 "build/parser.tab.cpp"
    break;

  case 97: /* direct_declarator: IDENTIFIER SCOPE_RES IDENTIFIER  */
#line 433 "src/parser.y"
                                      {
          const Symbol *s = lookupSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, s ? s->typeStr : "CLASS");
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 2991 "build/parser.tab.cpp"
    break;

  case 98: /* direct_declarator: TYPE_NAME SCOPE_RES IDENTIFIER  */
#line 440 "src/parser.y"
                                     {
          /* the common case in practice: an out-of-class method
             definition (Dog::bark(...) {...}) is almost always
             written AFTER the class's closing '}', by which point
             its name is already TYPE_NAME, not IDENTIFIER (see the
             typedef lexer-hack note above) */
          const Symbol *s = lookupSymbol(yyvsp[-2].str);
          setCategory(yyvsp[-2].idx, categoryForTypeName(s));
          yyval.decl.name = yyvsp[0].str;
          yyval.decl.nameIdx = yyvsp[0].idx;
          yyval.decl.className = yyvsp[-2].str;
      }
#line 3008 "build/parser.tab.cpp"
    break;

  case 99: /* direct_declarator: '(' declarator ')'  */
#line 452 "src/parser.y"
                         { yyval = yyvsp[-1]; yyval.decl.wasParenGrouped = true; }
#line 3014 "build/parser.tab.cpp"
    break;

  case 100: /* $@11: %empty  */
#line 453 "src/parser.y"
                            { pushScope(); }
#line 3020 "build/parser.tab.cpp"
    break;

  case 101: /* direct_declarator: direct_declarator '(' $@11 parameter_list_opt ')'  */
#line 453 "src/parser.y"
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
          popScope(); /* only used to keep param names out of the
                         enclosing scope while scanning the list; the
                         real function-body scope is pushed again by
                         function_definition, which re-declares them */
      }
#line 3041 "build/parser.tab.cpp"
    break;

  case 102: /* direct_declarator: direct_declarator '[' ']'  */
#line 469 "src/parser.y"
                                { yyval = yyvsp[-2]; yyval.decl.arrayLevel++; }
#line 3047 "build/parser.tab.cpp"
    break;

  case 103: /* direct_declarator: direct_declarator '[' assignment_expr ']'  */
#line 470 "src/parser.y"
                                                { yyval = yyvsp[-3]; yyval.decl.arrayLevel++; }
#line 3053 "build/parser.tab.cpp"
    break;

  case 104: /* parameter_list_opt: %empty  */
#line 474 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3059 "build/parser.tab.cpp"
    break;

  case 105: /* parameter_list_opt: parameter_list  */
#line 475 "src/parser.y"
                     { yyval = yyvsp[0]; }
#line 3065 "build/parser.tab.cpp"
    break;

  case 106: /* parameter_list: parameter_decl  */
#line 479 "src/parser.y"
                     { if (yyvsp[0].decl.nameIdx >= 0 || !yyvsp[0].decl.typeStr.empty()) yyval.paramList.push_back(yyvsp[0].decl); }
#line 3071 "build/parser.tab.cpp"
    break;

  case 107: /* parameter_list: parameter_list ',' parameter_decl  */
#line 480 "src/parser.y"
                                        {
          yyval = yyvsp[-2];
          yyval.paramList.push_back(yyvsp[0].decl);
      }
#line 3080 "build/parser.tab.cpp"
    break;

  case 108: /* parameter_list: parameter_list ',' ELLIPSIS  */
#line 484 "src/parser.y"
                                  { yyval = yyvsp[-2]; }
#line 3086 "build/parser.tab.cpp"
    break;

  case 109: /* parameter_decl: declaration_specifiers declarator  */
#line 488 "src/parser.y"
                                        {
          yyval.decl = yyvsp[0].decl;
          yyval.decl.typeStr = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, yyvsp[0].decl.arrayLevel);
      }
#line 3095 "build/parser.tab.cpp"
    break;

  case 110: /* parameter_decl: declaration_specifiers  */
#line 492 "src/parser.y"
                             {
          yyval.decl.typeStr = computeTypeStr(yyvsp[0].typeSpec, 0, 0);
      }
#line 3103 "build/parser.tab.cpp"
    break;

  case 111: /* $@12: %empty  */
#line 501 "src/parser.y"
                                        {
          bool outOfClass = !yyvsp[0].decl.className.empty();
          if (outOfClass) enterClass(yyvsp[0].decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[0].decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[0].decl.name, paramTypes, currentClassName());
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
          if (outOfClass) leaveClass();
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
#line 3138 "build/parser.tab.cpp"
    break;

  case 112: /* function_definition: declaration_specifiers declarator $@12 '{' block_item_list_opt '}'  */
#line 530 "src/parser.y"
                                    {
          popScope();
          bool outOfClass = !yyvsp[-4].decl.className.empty();
          if (outOfClass) enterClass(yyvsp[-4].decl.className);
          std::vector<std::string> paramTypes;
          for (auto &p : yyvsp[-4].decl.params) paramTypes.push_back(p.typeStr);
          std::string mangled = mangle(yyvsp[-4].decl.name, paramTypes, currentClassName());
          if (outOfClass) leaveClass();
          auto node = mkNode(ASTKind::FunctionDef, yyvsp[-4].decl.name + " : " + mangled);
          for (auto &p : yyvsp[-4].decl.params) {
              if (!p.name.empty()) addChild(node, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
          }
          auto body = mkNode(ASTKind::CompoundStmt);
          for (auto &s : yyvsp[-1].nodeList) addChild(body, s);
          addChild(node, body);
          yyval.node = node;
      }
#line 3160 "build/parser.tab.cpp"
    break;

  case 113: /* statement: compound_stmt  */
#line 553 "src/parser.y"
                    { yyval.node = yyvsp[0].node; }
#line 3166 "build/parser.tab.cpp"
    break;

  case 114: /* statement: expr_stmt  */
#line 554 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3172 "build/parser.tab.cpp"
    break;

  case 115: /* statement: selection_stmt  */
#line 555 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3178 "build/parser.tab.cpp"
    break;

  case 116: /* statement: iteration_stmt  */
#line 556 "src/parser.y"
                     { yyval.node = yyvsp[0].node; }
#line 3184 "build/parser.tab.cpp"
    break;

  case 117: /* statement: jump_stmt  */
#line 557 "src/parser.y"
                { yyval.node = yyvsp[0].node; }
#line 3190 "build/parser.tab.cpp"
    break;

  case 118: /* statement: labeled_stmt  */
#line 558 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3196 "build/parser.tab.cpp"
    break;

  case 119: /* statement: declaration  */
#line 559 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3202 "build/parser.tab.cpp"
    break;

  case 120: /* statement: error ';'  */
#line 560 "src/parser.y"
                { yyerrok; yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3208 "build/parser.tab.cpp"
    break;

  case 121: /* statement: error '}'  */
#line 561 "src/parser.y"
                { yyerrok; yyval.node = mkNode(ASTKind::ErrorNode, lastErrorLabel()); }
#line 3214 "build/parser.tab.cpp"
    break;

  case 122: /* $@13: %empty  */
#line 565 "src/parser.y"
          { pushScope(); }
#line 3220 "build/parser.tab.cpp"
    break;

  case 123: /* compound_stmt: '{' $@13 block_item_list_opt '}'  */
#line 565 "src/parser.y"
                                                   {
          popScope();
          auto n = mkNode(ASTKind::CompoundStmt);
          for (auto &s : yyvsp[-1].nodeList) addChild(n, s);
          yyval.node = n;
      }
#line 3231 "build/parser.tab.cpp"
    break;

  case 124: /* block_item_list_opt: %empty  */
#line 574 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3237 "build/parser.tab.cpp"
    break;

  case 125: /* block_item_list_opt: block_item_list  */
#line 575 "src/parser.y"
                      { yyval = yyvsp[0]; }
#line 3243 "build/parser.tab.cpp"
    break;

  case 126: /* block_item_list: statement  */
#line 579 "src/parser.y"
                { if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3249 "build/parser.tab.cpp"
    break;

  case 127: /* block_item_list: block_item_list statement  */
#line 580 "src/parser.y"
                                { yyval = yyvsp[-1]; if (yyvsp[0].node) yyval.nodeList.push_back(yyvsp[0].node); }
#line 3255 "build/parser.tab.cpp"
    break;

  case 128: /* expr_stmt: ';'  */
#line 584 "src/parser.y"
          { yyval.node = mkNode(ASTKind::EmptyStmt); }
#line 3261 "build/parser.tab.cpp"
    break;

  case 129: /* expr_stmt: expr ';'  */
#line 585 "src/parser.y"
               { yyval.node = mkNode(ASTKind::ExprStmt, "", {yyvsp[-1].node}); }
#line 3267 "build/parser.tab.cpp"
    break;

  case 130: /* selection_stmt: IF '(' expr ')' statement  */
#line 589 "src/parser.y"
                                          {
          yyval.node = mkNode(ASTKind::IfStmt, "", {yyvsp[-2].node, yyvsp[0].node});
      }
#line 3275 "build/parser.tab.cpp"
    break;

  case 131: /* selection_stmt: IF '(' expr ')' statement ELSE statement  */
#line 592 "src/parser.y"
                                               {
          yyval.node = mkNode(ASTKind::IfStmt, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node});
      }
#line 3283 "build/parser.tab.cpp"
    break;

  case 132: /* $@14: %empty  */
#line 595 "src/parser.y"
                          { hintScope("switch"); }
#line 3289 "build/parser.tab.cpp"
    break;

  case 133: /* selection_stmt: SWITCH '(' expr ')' $@14 compound_stmt  */
#line 595 "src/parser.y"
                                                                 {
          yyval.node = mkNode(ASTKind::SwitchStmt, "", {yyvsp[-3].node, yyvsp[0].node});
      }
#line 3297 "build/parser.tab.cpp"
    break;

  case 134: /* labeled_stmt: CASE constant_expr ':' statement  */
#line 601 "src/parser.y"
                                       {
          yyval.node = mkNode(ASTKind::CaseStmt, "", {yyvsp[-2].node, yyvsp[0].node});
      }
#line 3305 "build/parser.tab.cpp"
    break;

  case 135: /* labeled_stmt: DEFAULT ':' statement  */
#line 604 "src/parser.y"
                            {
          yyval.node = mkNode(ASTKind::DefaultStmt, "", {yyvsp[0].node});
      }
#line 3313 "build/parser.tab.cpp"
    break;

  case 136: /* labeled_stmt: IDENTIFIER ':' statement  */
#line 607 "src/parser.y"
                               {
          declareSymbol(yyvsp[-2].str, SymKind::LABEL, "LABEL", SymbolDeclInfo{yyvsp[-2].idx});
          setCategory(yyvsp[-2].idx, "LABEL");
          yyval.node = mkNode(ASTKind::LabeledStmt, yyvsp[-2].str, {yyvsp[0].node});
      }
#line 3323 "build/parser.tab.cpp"
    break;

  case 137: /* iteration_stmt: WHILE '(' expr ')' statement  */
#line 615 "src/parser.y"
                                   {
          yyval.node = mkNode(ASTKind::WhileStmt, "", {yyvsp[-2].node, yyvsp[0].node});
      }
#line 3331 "build/parser.tab.cpp"
    break;

  case 138: /* iteration_stmt: DO statement WHILE '(' expr ')' ';'  */
#line 618 "src/parser.y"
                                          {
          yyval.node = mkNode(ASTKind::DoWhileStmt, "", {yyvsp[-5].node, yyvsp[-2].node});
      }
#line 3339 "build/parser.tab.cpp"
    break;

  case 139: /* iteration_stmt: UNTIL '(' expr ')' statement  */
#line 621 "src/parser.y"
                                   {
          yyval.node = mkNode(ASTKind::UntilStmt, "", {yyvsp[-2].node, yyvsp[0].node});
      }
#line 3347 "build/parser.tab.cpp"
    break;

  case 140: /* iteration_stmt: FOR '(' expr_stmt expr_stmt for_incr_opt ')' statement  */
#line 624 "src/parser.y"
                                                             {
          yyval.node = mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node});
      }
#line 3355 "build/parser.tab.cpp"
    break;

  case 141: /* $@15: %empty  */
#line 627 "src/parser.y"
              { hintScope("for"); pushScope(); }
#line 3361 "build/parser.tab.cpp"
    break;

  case 142: /* iteration_stmt: FOR '(' $@15 declaration expr_stmt for_incr_opt ')' statement  */
#line 627 "src/parser.y"
                                                                                                  {
          popScope();
          yyval.node = mkNode(ASTKind::ForStmt, "", {yyvsp[-4].node, yyvsp[-3].node, yyvsp[-2].node, yyvsp[0].node});
      }
#line 3370 "build/parser.tab.cpp"
    break;

  case 143: /* for_incr_opt: %empty  */
#line 634 "src/parser.y"
                  { yyval = ParserValue(); }
#line 3376 "build/parser.tab.cpp"
    break;

  case 144: /* for_incr_opt: expr  */
#line 635 "src/parser.y"
           { yyval.node = yyvsp[0].node; }
#line 3382 "build/parser.tab.cpp"
    break;

  case 145: /* jump_stmt: BREAK ';'  */
#line 639 "src/parser.y"
                { yyval.node = mkNode(ASTKind::BreakStmt); }
#line 3388 "build/parser.tab.cpp"
    break;

  case 146: /* jump_stmt: CONTINUE ';'  */
#line 640 "src/parser.y"
                   { yyval.node = mkNode(ASTKind::ContinueStmt); }
#line 3394 "build/parser.tab.cpp"
    break;

  case 147: /* jump_stmt: RETURN ';'  */
#line 641 "src/parser.y"
                 { yyval.node = mkNode(ASTKind::ReturnStmt); }
#line 3400 "build/parser.tab.cpp"
    break;

  case 148: /* jump_stmt: RETURN expr ';'  */
#line 642 "src/parser.y"
                      { yyval.node = mkNode(ASTKind::ReturnStmt, "", {yyvsp[-1].node}); }
#line 3406 "build/parser.tab.cpp"
    break;

  case 149: /* jump_stmt: GOTO IDENTIFIER ';'  */
#line 643 "src/parser.y"
                          {
          const Symbol *s = lookupSymbol(yyvsp[-1].str);
          if (s) setCategory(yyvsp[-1].idx, "LABEL");
          recordUsage(s);
          yyval.node = mkNode(ASTKind::GotoStmt, yyvsp[-1].str);
      }
#line 3417 "build/parser.tab.cpp"
    break;

  case 150: /* expr: assignment_expr  */
#line 660 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 3423 "build/parser.tab.cpp"
    break;

  case 151: /* expr: expr ',' assignment_expr  */
#line 661 "src/parser.y"
                               { yyval.node = mkNode(ASTKind::CommaExpr, "", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3429 "build/parser.tab.cpp"
    break;

  case 152: /* assignment_expr: binary_expr  */
#line 665 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3435 "build/parser.tab.cpp"
    break;

  case 153: /* assignment_expr: unary_expr assign_op assignment_expr  */
#line 666 "src/parser.y"
                                           {
          yyval.node = mkNode(ASTKind::AssignExpr, yyvsp[-1].str, {yyvsp[-2].node, yyvsp[0].node});
      }
#line 3443 "build/parser.tab.cpp"
    break;

  case 154: /* assign_op: '='  */
#line 672 "src/parser.y"
                   { yyval.str = "="; }
#line 3449 "build/parser.tab.cpp"
    break;

  case 155: /* assign_op: PLUS_ASSIGN  */
#line 673 "src/parser.y"
                   { yyval.str = "+="; }
#line 3455 "build/parser.tab.cpp"
    break;

  case 156: /* assign_op: MINUS_ASSIGN  */
#line 674 "src/parser.y"
                   { yyval.str = "-="; }
#line 3461 "build/parser.tab.cpp"
    break;

  case 157: /* assign_op: MUL_ASSIGN  */
#line 675 "src/parser.y"
                   { yyval.str = "*="; }
#line 3467 "build/parser.tab.cpp"
    break;

  case 158: /* assign_op: DIV_ASSIGN  */
#line 676 "src/parser.y"
                   { yyval.str = "/="; }
#line 3473 "build/parser.tab.cpp"
    break;

  case 159: /* assign_op: MOD_ASSIGN  */
#line 677 "src/parser.y"
                   { yyval.str = "%="; }
#line 3479 "build/parser.tab.cpp"
    break;

  case 160: /* assign_op: AND_ASSIGN  */
#line 678 "src/parser.y"
                   { yyval.str = "&="; }
#line 3485 "build/parser.tab.cpp"
    break;

  case 161: /* assign_op: OR_ASSIGN  */
#line 679 "src/parser.y"
                   { yyval.str = "|="; }
#line 3491 "build/parser.tab.cpp"
    break;

  case 162: /* assign_op: XOR_ASSIGN  */
#line 680 "src/parser.y"
                   { yyval.str = "^="; }
#line 3497 "build/parser.tab.cpp"
    break;

  case 163: /* assign_op: SHL_ASSIGN  */
#line 681 "src/parser.y"
                   { yyval.str = "<<="; }
#line 3503 "build/parser.tab.cpp"
    break;

  case 164: /* assign_op: SHR_ASSIGN  */
#line 682 "src/parser.y"
                   { yyval.str = ">>="; }
#line 3509 "build/parser.tab.cpp"
    break;

  case 165: /* constant_expr: binary_expr  */
#line 686 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 3515 "build/parser.tab.cpp"
    break;

  case 166: /* binary_expr: binary_expr OR_OP binary_expr  */
#line 690 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "||", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3521 "build/parser.tab.cpp"
    break;

  case 167: /* binary_expr: binary_expr AND_OP binary_expr  */
#line 691 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "&&", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3527 "build/parser.tab.cpp"
    break;

  case 168: /* binary_expr: binary_expr '|' binary_expr  */
#line 692 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "|", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3533 "build/parser.tab.cpp"
    break;

  case 169: /* binary_expr: binary_expr '^' binary_expr  */
#line 693 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "^", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3539 "build/parser.tab.cpp"
    break;

  case 170: /* binary_expr: binary_expr '&' binary_expr  */
#line 694 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "&", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3545 "build/parser.tab.cpp"
    break;

  case 171: /* binary_expr: binary_expr EQ_OP binary_expr  */
#line 695 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "==", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3551 "build/parser.tab.cpp"
    break;

  case 172: /* binary_expr: binary_expr NE_OP binary_expr  */
#line 696 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "!=", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3557 "build/parser.tab.cpp"
    break;

  case 173: /* binary_expr: binary_expr '<' binary_expr  */
#line 697 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "<", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3563 "build/parser.tab.cpp"
    break;

  case 174: /* binary_expr: binary_expr '>' binary_expr  */
#line 698 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, ">", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3569 "build/parser.tab.cpp"
    break;

  case 175: /* binary_expr: binary_expr LE_OP binary_expr  */
#line 699 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "<=", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3575 "build/parser.tab.cpp"
    break;

  case 176: /* binary_expr: binary_expr GE_OP binary_expr  */
#line 700 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, ">=", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3581 "build/parser.tab.cpp"
    break;

  case 177: /* binary_expr: binary_expr SHL binary_expr  */
#line 701 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "<<", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3587 "build/parser.tab.cpp"
    break;

  case 178: /* binary_expr: binary_expr SHR binary_expr  */
#line 702 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, ">>", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3593 "build/parser.tab.cpp"
    break;

  case 179: /* binary_expr: binary_expr '+' binary_expr  */
#line 703 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "+", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3599 "build/parser.tab.cpp"
    break;

  case 180: /* binary_expr: binary_expr '-' binary_expr  */
#line 704 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "-", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3605 "build/parser.tab.cpp"
    break;

  case 181: /* binary_expr: binary_expr '*' binary_expr  */
#line 705 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "*", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3611 "build/parser.tab.cpp"
    break;

  case 182: /* binary_expr: binary_expr '/' binary_expr  */
#line 706 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "/", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3617 "build/parser.tab.cpp"
    break;

  case 183: /* binary_expr: binary_expr '%' binary_expr  */
#line 707 "src/parser.y"
                                     { yyval.node = mkNode(ASTKind::BinaryExpr, "%", {yyvsp[-2].node, yyvsp[0].node}); }
#line 3623 "build/parser.tab.cpp"
    break;

  case 184: /* binary_expr: binary_expr '?' expr ':' binary_expr  */
#line 708 "src/parser.y"
                                           {
          yyval.node = mkNode(ASTKind::TernaryExpr, "", {yyvsp[-4].node, yyvsp[-2].node, yyvsp[0].node});
      }
#line 3631 "build/parser.tab.cpp"
    break;

  case 185: /* binary_expr: unary_expr  */
#line 711 "src/parser.y"
                 { yyval.node = yyvsp[0].node; }
#line 3637 "build/parser.tab.cpp"
    break;

  case 186: /* unary_expr: postfix_expr  */
#line 715 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3643 "build/parser.tab.cpp"
    break;

  case 187: /* unary_expr: INC unary_expr  */
#line 716 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::UnaryExpr, "++(pre)", {yyvsp[0].node}); }
#line 3649 "build/parser.tab.cpp"
    break;

  case 188: /* unary_expr: DEC unary_expr  */
#line 717 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::UnaryExpr, "--(pre)", {yyvsp[0].node}); }
#line 3655 "build/parser.tab.cpp"
    break;

  case 189: /* unary_expr: '&' unary_expr  */
#line 718 "src/parser.y"
                                 { yyval.node = mkNode(ASTKind::UnaryExpr, "&", {yyvsp[0].node}); }
#line 3661 "build/parser.tab.cpp"
    break;

  case 190: /* unary_expr: '*' unary_expr  */
#line 719 "src/parser.y"
                                 { yyval.node = mkNode(ASTKind::UnaryExpr, "*", {yyvsp[0].node}); }
#line 3667 "build/parser.tab.cpp"
    break;

  case 191: /* unary_expr: '+' unary_expr  */
#line 720 "src/parser.y"
                                  { yyval.node = mkNode(ASTKind::UnaryExpr, "+", {yyvsp[0].node}); }
#line 3673 "build/parser.tab.cpp"
    break;

  case 192: /* unary_expr: '-' unary_expr  */
#line 721 "src/parser.y"
                                  { yyval.node = mkNode(ASTKind::UnaryExpr, "-", {yyvsp[0].node}); }
#line 3679 "build/parser.tab.cpp"
    break;

  case 193: /* unary_expr: '!' unary_expr  */
#line 722 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::UnaryExpr, "!", {yyvsp[0].node}); }
#line 3685 "build/parser.tab.cpp"
    break;

  case 194: /* unary_expr: '~' unary_expr  */
#line 723 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::UnaryExpr, "~", {yyvsp[0].node}); }
#line 3691 "build/parser.tab.cpp"
    break;

  case 195: /* unary_expr: '(' type_name ')' unary_expr  */
#line 724 "src/parser.y"
                                              {
          yyval.node = mkNode(ASTKind::CastExpr, yyvsp[-2].str, {yyvsp[0].node});
      }
#line 3699 "build/parser.tab.cpp"
    break;

  case 196: /* unary_expr: SIZEOF unary_expr  */
#line 727 "src/parser.y"
                                   { yyval.node = mkNode(ASTKind::SizeofExpr, "", {yyvsp[0].node}); }
#line 3705 "build/parser.tab.cpp"
    break;

  case 197: /* unary_expr: SIZEOF '(' type_name ')'  */
#line 728 "src/parser.y"
                               { yyval.node = mkNode(ASTKind::SizeofExpr, yyvsp[-1].str); }
#line 3711 "build/parser.tab.cpp"
    break;

  case 198: /* unary_expr: NEW type_name  */
#line 729 "src/parser.y"
                    { yyval.node = mkNode(ASTKind::NewExpr, yyvsp[0].str); }
#line 3717 "build/parser.tab.cpp"
    break;

  case 199: /* unary_expr: DELETE unary_expr  */
#line 730 "src/parser.y"
                        { yyval.node = mkNode(ASTKind::DeleteExpr, "", {yyvsp[0].node}); }
#line 3723 "build/parser.tab.cpp"
    break;

  case 200: /* type_name: type_name_specifiers pointer_opt  */
#line 734 "src/parser.y"
                                       {
          yyval.str = computeTypeStr(yyvsp[-1].typeSpec, yyvsp[0].decl.pointerLevel, 0);
      }
#line 3731 "build/parser.tab.cpp"
    break;

  case 201: /* type_name_specifiers: type_name_specifiers type_name_specifier  */
#line 740 "src/parser.y"
                                               {
          yyval = yyvsp[-1];
          for (auto &p : yyvsp[0].typeSpec.parts) yyval.typeSpec.parts.push_back(p);
      }
#line 3740 "build/parser.tab.cpp"
    break;

  case 202: /* type_name_specifiers: type_name_specifier  */
#line 744 "src/parser.y"
                          { yyval = yyvsp[0]; }
#line 3746 "build/parser.tab.cpp"
    break;

  case 203: /* type_name_specifier: INT  */
#line 753 "src/parser.y"
               { yyval.typeSpec.parts.push_back("INT"); }
#line 3752 "build/parser.tab.cpp"
    break;

  case 204: /* type_name_specifier: CHAR  */
#line 754 "src/parser.y"
               { yyval.typeSpec.parts.push_back("CHAR"); }
#line 3758 "build/parser.tab.cpp"
    break;

  case 205: /* type_name_specifier: FLOAT  */
#line 755 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FLOAT"); }
#line 3764 "build/parser.tab.cpp"
    break;

  case 206: /* type_name_specifier: DOUBLE  */
#line 756 "src/parser.y"
               { yyval.typeSpec.parts.push_back("DOUBLE"); }
#line 3770 "build/parser.tab.cpp"
    break;

  case 207: /* type_name_specifier: VOID  */
#line 757 "src/parser.y"
               { yyval.typeSpec.parts.push_back("VOID"); }
#line 3776 "build/parser.tab.cpp"
    break;

  case 208: /* type_name_specifier: BOOL  */
#line 758 "src/parser.y"
               { yyval.typeSpec.parts.push_back("BOOL"); }
#line 3782 "build/parser.tab.cpp"
    break;

  case 209: /* type_name_specifier: SHORT  */
#line 759 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SHORT"); }
#line 3788 "build/parser.tab.cpp"
    break;

  case 210: /* type_name_specifier: LONG  */
#line 760 "src/parser.y"
               { yyval.typeSpec.parts.push_back("LONG"); }
#line 3794 "build/parser.tab.cpp"
    break;

  case 211: /* type_name_specifier: SIGNED  */
#line 761 "src/parser.y"
               { yyval.typeSpec.parts.push_back("SIGNED"); }
#line 3800 "build/parser.tab.cpp"
    break;

  case 212: /* type_name_specifier: UNSIGNED  */
#line 762 "src/parser.y"
               { yyval.typeSpec.parts.push_back("UNSIGNED"); }
#line 3806 "build/parser.tab.cpp"
    break;

  case 213: /* type_name_specifier: FILE_KW  */
#line 763 "src/parser.y"
               { yyval.typeSpec.parts.push_back("FILE"); }
#line 3812 "build/parser.tab.cpp"
    break;

  case 214: /* type_name_specifier: CONST  */
#line 764 "src/parser.y"
               { yyval = ParserValue(); }
#line 3818 "build/parser.tab.cpp"
    break;

  case 215: /* type_name_specifier: VOLATILE  */
#line 765 "src/parser.y"
               { yyval = ParserValue(); }
#line 3824 "build/parser.tab.cpp"
    break;

  case 216: /* type_name_specifier: TYPE_NAME  */
#line 766 "src/parser.y"
                {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back(s ? s->typeStr : "INT");
      }
#line 3834 "build/parser.tab.cpp"
    break;

  case 217: /* type_name_specifier: STRUCT IDENTIFIER  */
#line 771 "src/parser.y"
                        {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "STRUCT");
          yyval.typeSpec.parts.push_back("STRUCT");
      }
#line 3844 "build/parser.tab.cpp"
    break;

  case 218: /* type_name_specifier: STRUCT TYPE_NAME  */
#line 776 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("STRUCT");
      }
#line 3854 "build/parser.tab.cpp"
    break;

  case 219: /* type_name_specifier: UNION IDENTIFIER  */
#line 781 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "UNION");
          yyval.typeSpec.parts.push_back("UNION");
      }
#line 3864 "build/parser.tab.cpp"
    break;

  case 220: /* type_name_specifier: UNION TYPE_NAME  */
#line 786 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("UNION");
      }
#line 3874 "build/parser.tab.cpp"
    break;

  case 221: /* type_name_specifier: CLASS IDENTIFIER  */
#line 791 "src/parser.y"
                       {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "CLASS");
          yyval.typeSpec.parts.push_back("CLASS");
      }
#line 3884 "build/parser.tab.cpp"
    break;

  case 222: /* type_name_specifier: CLASS TYPE_NAME  */
#line 796 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("CLASS");
      }
#line 3894 "build/parser.tab.cpp"
    break;

  case 223: /* type_name_specifier: ENUM IDENTIFIER  */
#line 801 "src/parser.y"
                      {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, s ? s->typeStr : "ENUM");
          yyval.typeSpec.parts.push_back("ENUM");
      }
#line 3904 "build/parser.tab.cpp"
    break;

  case 224: /* type_name_specifier: ENUM TYPE_NAME  */
#line 806 "src/parser.y"
                     {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          setCategory(yyvsp[0].idx, categoryForTypeName(s));
          yyval.typeSpec.parts.push_back("ENUM");
      }
#line 3914 "build/parser.tab.cpp"
    break;

  case 225: /* postfix_expr: primary_expr  */
#line 814 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3920 "build/parser.tab.cpp"
    break;

  case 226: /* postfix_expr: postfix_expr '[' expr ']'  */
#line 815 "src/parser.y"
                                { yyval.node = mkNode(ASTKind::IndexExpr, "", {yyvsp[-3].node, yyvsp[-1].node}); }
#line 3926 "build/parser.tab.cpp"
    break;

  case 227: /* postfix_expr: postfix_expr '(' argument_list_opt ')'  */
#line 816 "src/parser.y"
                                             {
          auto n = mkNode(ASTKind::CallExpr, "", {yyvsp[-3].node});
          for (auto &a : yyvsp[-1].nodeList) addChild(n, a);
          yyval.node = n;
      }
#line 3936 "build/parser.tab.cpp"
    break;

  case 228: /* postfix_expr: postfix_expr '.' IDENTIFIER  */
#line 821 "src/parser.y"
                                  { yyval.node = mkNode(ASTKind::MemberExpr, yyvsp[0].str, {yyvsp[-2].node}); }
#line 3942 "build/parser.tab.cpp"
    break;

  case 229: /* postfix_expr: postfix_expr ARROW IDENTIFIER  */
#line 822 "src/parser.y"
                                    { yyval.node = mkNode(ASTKind::ArrowExpr, yyvsp[0].str, {yyvsp[-2].node}); }
#line 3948 "build/parser.tab.cpp"
    break;

  case 230: /* postfix_expr: postfix_expr SCOPE_RES IDENTIFIER  */
#line 823 "src/parser.y"
                                        { yyval.node = mkNode(ASTKind::ScopeExpr, yyvsp[0].str, {yyvsp[-2].node}); }
#line 3954 "build/parser.tab.cpp"
    break;

  case 231: /* postfix_expr: postfix_expr INC  */
#line 824 "src/parser.y"
                       { yyval.node = mkNode(ASTKind::PostfixOpExpr, "++", {yyvsp[-1].node}); }
#line 3960 "build/parser.tab.cpp"
    break;

  case 232: /* postfix_expr: postfix_expr DEC  */
#line 825 "src/parser.y"
                       { yyval.node = mkNode(ASTKind::PostfixOpExpr, "--", {yyvsp[-1].node}); }
#line 3966 "build/parser.tab.cpp"
    break;

  case 233: /* postfix_expr: builtin_call  */
#line 826 "src/parser.y"
                   { yyval.node = yyvsp[0].node; }
#line 3972 "build/parser.tab.cpp"
    break;

  case 234: /* builtin_call: PRINTF '(' argument_list_opt ')'  */
#line 830 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "printf");  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 3978 "build/parser.tab.cpp"
    break;

  case 235: /* builtin_call: SCANF '(' argument_list_opt ')'  */
#line 831 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "scanf");   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 3984 "build/parser.tab.cpp"
    break;

  case 236: /* builtin_call: MALLOC '(' argument_list_opt ')'  */
#line 832 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "malloc");  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 3990 "build/parser.tab.cpp"
    break;

  case 237: /* builtin_call: FREE '(' argument_list_opt ')'  */
#line 833 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "free");    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 3996 "build/parser.tab.cpp"
    break;

  case 238: /* builtin_call: CALLOC '(' argument_list_opt ')'  */
#line 834 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "calloc");  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4002 "build/parser.tab.cpp"
    break;

  case 239: /* builtin_call: REALLOC '(' argument_list_opt ')'  */
#line 835 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "realloc"); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4008 "build/parser.tab.cpp"
    break;

  case 240: /* builtin_call: FOPEN '(' argument_list_opt ')'  */
#line 836 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fopen");   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4014 "build/parser.tab.cpp"
    break;

  case 241: /* builtin_call: FCLOSE '(' argument_list_opt ')'  */
#line 837 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fclose");  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4020 "build/parser.tab.cpp"
    break;

  case 242: /* builtin_call: FREAD '(' argument_list_opt ')'  */
#line 838 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fread");   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4026 "build/parser.tab.cpp"
    break;

  case 243: /* builtin_call: FWRITE '(' argument_list_opt ')'  */
#line 839 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fwrite");  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4032 "build/parser.tab.cpp"
    break;

  case 244: /* builtin_call: FPRINTF '(' argument_list_opt ')'  */
#line 840 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fprintf"); for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4038 "build/parser.tab.cpp"
    break;

  case 245: /* builtin_call: FSCANF '(' argument_list_opt ')'  */
#line 841 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fscanf");  for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4044 "build/parser.tab.cpp"
    break;

  case 246: /* builtin_call: FGETS '(' argument_list_opt ')'  */
#line 842 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fgets");   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4050 "build/parser.tab.cpp"
    break;

  case 247: /* builtin_call: FPUTS '(' argument_list_opt ')'  */
#line 843 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "fputs");   for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4056 "build/parser.tab.cpp"
    break;

  case 248: /* builtin_call: FEOF '(' argument_list_opt ')'  */
#line 844 "src/parser.y"
                                        { auto n = mkNode(ASTKind::BuiltinCallExpr, "feof");    for (auto &a : yyvsp[-1].nodeList) addChild(n, a); yyval.node = n; }
#line 4062 "build/parser.tab.cpp"
    break;

  case 249: /* argument_list_opt: %empty  */
#line 848 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4068 "build/parser.tab.cpp"
    break;

  case 250: /* argument_list_opt: argument_list  */
#line 849 "src/parser.y"
                    { yyval = yyvsp[0]; }
#line 4074 "build/parser.tab.cpp"
    break;

  case 251: /* argument_list: argument  */
#line 853 "src/parser.y"
               { yyval.nodeList.push_back(yyvsp[0].node); }
#line 4080 "build/parser.tab.cpp"
    break;

  case 252: /* argument_list: argument_list ',' argument  */
#line 854 "src/parser.y"
                                 { yyval = yyvsp[-2]; yyval.nodeList.push_back(yyvsp[0].node); }
#line 4086 "build/parser.tab.cpp"
    break;

  case 253: /* argument: assignment_expr  */
#line 858 "src/parser.y"
                      { yyval.node = yyvsp[0].node; }
#line 4092 "build/parser.tab.cpp"
    break;

  case 254: /* argument: type_name  */
#line 859 "src/parser.y"
                { yyval.node = mkNode(ASTKind::TypeNameNode, yyvsp[0].str); }
#line 4098 "build/parser.tab.cpp"
    break;

  case 255: /* primary_expr: IDENTIFIER  */
#line 863 "src/parser.y"
                 {
          const Symbol *s = lookupSymbol(yyvsp[0].str);
          if (s) setCategory(yyvsp[0].idx, s->typeStr);
          recordUsage(s);
          yyval.node = mkNode(ASTKind::Identifier, yyvsp[0].str);
      }
#line 4109 "build/parser.tab.cpp"
    break;

  case 256: /* primary_expr: INT_LITERAL  */
#line 869 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::IntLiteral, yyvsp[0].str); }
#line 4115 "build/parser.tab.cpp"
    break;

  case 257: /* primary_expr: FLOAT_LITERAL  */
#line 870 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::FloatLiteral, yyvsp[0].str); }
#line 4121 "build/parser.tab.cpp"
    break;

  case 258: /* primary_expr: CHAR_LITERAL  */
#line 871 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::CharLiteral, yyvsp[0].str); }
#line 4127 "build/parser.tab.cpp"
    break;

  case 259: /* primary_expr: STRING_LITERAL  */
#line 872 "src/parser.y"
                     { yyval.node = mkNode(ASTKind::StringLiteral, yyvsp[0].str); }
#line 4133 "build/parser.tab.cpp"
    break;

  case 260: /* primary_expr: BOOL_LITERAL  */
#line 873 "src/parser.y"
                   { yyval.node = mkNode(ASTKind::BoolLiteral, yyvsp[0].str); }
#line 4139 "build/parser.tab.cpp"
    break;

  case 261: /* primary_expr: THIS  */
#line 874 "src/parser.y"
           { yyval.node = mkNode(ASTKind::ThisExpr); }
#line 4145 "build/parser.tab.cpp"
    break;

  case 262: /* primary_expr: '(' expr ')'  */
#line 875 "src/parser.y"
                   { yyval.node = yyvsp[-1].node; }
#line 4151 "build/parser.tab.cpp"
    break;

  case 263: /* primary_expr: lambda_expr  */
#line 876 "src/parser.y"
                  { yyval.node = yyvsp[0].node; }
#line 4157 "build/parser.tab.cpp"
    break;

  case 264: /* $@16: %empty  */
#line 880 "src/parser.y"
                                   { pushScope("lambda"); }
#line 4163 "build/parser.tab.cpp"
    break;

  case 265: /* $@17: %empty  */
#line 880 "src/parser.y"
                                                                                   {
          for (auto &p : yyvsp[-1].paramList) {
              if (p.nameIdx >= 0) {
                  declareSymbol(p.name, SymKind::PARAMETER, p.typeStr, SymbolDeclInfo{p.nameIdx});
                  setCategory(p.nameIdx, p.typeStr);
              }
          }
      }
#line 4176 "build/parser.tab.cpp"
    break;

  case 266: /* lambda_expr: '[' capture_list_opt ']' '(' $@16 parameter_list_opt ')' $@17 compound_stmt  */
#line 887 "src/parser.y"
                      {
          popScope();
          auto n = mkNode(ASTKind::LambdaExpr, yyvsp[-7].str);
          for (auto &p : yyvsp[-3].paramList) {
              if (!p.name.empty()) addChild(n, mkNode(ASTKind::ParamDecl, p.name + " : " + p.typeStr));
          }
          addChild(n, yyvsp[0].node);
          yyval.node = n;
      }
#line 4190 "build/parser.tab.cpp"
    break;

  case 267: /* capture_list_opt: %empty  */
#line 899 "src/parser.y"
                  { yyval = ParserValue(); }
#line 4196 "build/parser.tab.cpp"
    break;

  case 268: /* capture_list_opt: capture_list  */
#line 900 "src/parser.y"
                   { yyval = yyvsp[0]; }
#line 4202 "build/parser.tab.cpp"
    break;

  case 269: /* capture_list: capture  */
#line 904 "src/parser.y"
              { yyval.str = yyvsp[0].str; }
#line 4208 "build/parser.tab.cpp"
    break;

  case 270: /* capture_list: capture_list ',' capture  */
#line 905 "src/parser.y"
                               { yyval.str = yyvsp[-2].str + ", " + yyvsp[0].str; }
#line 4214 "build/parser.tab.cpp"
    break;

  case 271: /* capture: IDENTIFIER  */
#line 909 "src/parser.y"
                 { yyval.str = yyvsp[0].str; }
#line 4220 "build/parser.tab.cpp"
    break;

  case 272: /* capture: '&' IDENTIFIER  */
#line 910 "src/parser.y"
                     { yyval.str = "&" + yyvsp[0].str; }
#line 4226 "build/parser.tab.cpp"
    break;

  case 273: /* capture: '&'  */
#line 911 "src/parser.y"
          { yyval.str = "&"; }
#line 4232 "build/parser.tab.cpp"
    break;

  case 274: /* capture: '='  */
#line 912 "src/parser.y"
          { yyval.str = "="; }
#line 4238 "build/parser.tab.cpp"
    break;


#line 4242 "build/parser.tab.cpp"

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

#line 915 "src/parser.y"


void yyerror(const char *s) {
    reportDiagnostic(g_currentLine, g_currentColumn, g_lastText, s, "Syntax error");
}
