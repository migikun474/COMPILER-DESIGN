/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

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

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_BUILD_PARSER_TAB_HPP_INCLUDED
# define YY_YY_BUILD_PARSER_TAB_HPP_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif
/* "%code requires" blocks.  */
#line 1 "src/parser.y"

    #include "parser_value.h"

#line 53 "build/parser.tab.hpp"

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    INT = 258,                     /* INT  */
    CHAR = 259,                    /* CHAR  */
    FLOAT = 260,                   /* FLOAT  */
    DOUBLE = 261,                  /* DOUBLE  */
    VOID = 262,                    /* VOID  */
    SHORT = 263,                   /* SHORT  */
    LONG = 264,                    /* LONG  */
    SIGNED = 265,                  /* SIGNED  */
    UNSIGNED = 266,                /* UNSIGNED  */
    STRUCT = 267,                  /* STRUCT  */
    CLASS = 268,                   /* CLASS  */
    PUBLIC = 269,                  /* PUBLIC  */
    PRIVATE = 270,                 /* PRIVATE  */
    PROTECTED = 271,               /* PROTECTED  */
    THIS = 272,                    /* THIS  */
    STATIC = 273,                  /* STATIC  */
    TYPEDEF = 274,                 /* TYPEDEF  */
    AUTO = 275,                    /* AUTO  */
    EXTERN = 276,                  /* EXTERN  */
    CONST = 277,                   /* CONST  */
    IF = 278,                      /* IF  */
    ELSE = 279,                    /* ELSE  */
    FOR = 280,                     /* FOR  */
    WHILE = 281,                   /* WHILE  */
    DO = 282,                      /* DO  */
    UNTIL = 283,                   /* UNTIL  */
    SWITCH = 284,                  /* SWITCH  */
    CASE = 285,                    /* CASE  */
    DEFAULT = 286,                 /* DEFAULT  */
    BREAK = 287,                   /* BREAK  */
    CONTINUE = 288,                /* CONTINUE  */
    GOTO = 289,                    /* GOTO  */
    RETURN = 290,                  /* RETURN  */
    PRINTF = 291,                  /* PRINTF  */
    SCANF = 292,                   /* SCANF  */
    MALLOC = 293,                  /* MALLOC  */
    FREE = 294,                    /* FREE  */
    CALLOC = 295,                  /* CALLOC  */
    REALLOC = 296,                 /* REALLOC  */
    BOOL = 297,                    /* BOOL  */
    SIZEOF = 298,                  /* SIZEOF  */
    VA_LIST = 299,                 /* VA_LIST  */
    VA_START = 300,                /* VA_START  */
    VA_ARG = 301,                  /* VA_ARG  */
    VA_END = 302,                  /* VA_END  */
    OPERATOR = 303,                /* OPERATOR  */
    FCAST = 304,                   /* FCAST  */
    ABSTRACT_LPAREN = 305,         /* ABSTRACT_LPAREN  */
    IDENTIFIER = 306,              /* IDENTIFIER  */
    TYPE_NAME = 307,               /* TYPE_NAME  */
    INT_LITERAL = 308,             /* INT_LITERAL  */
    FLOAT_LITERAL = 309,           /* FLOAT_LITERAL  */
    CHAR_LITERAL = 310,            /* CHAR_LITERAL  */
    STRING_LITERAL = 311,          /* STRING_LITERAL  */
    BOOL_LITERAL = 312,            /* BOOL_LITERAL  */
    ARROW = 313,                   /* ARROW  */
    ELLIPSIS = 314,                /* ELLIPSIS  */
    SCOPE_RES = 315,               /* SCOPE_RES  */
    INC = 316,                     /* INC  */
    DEC = 317,                     /* DEC  */
    SHL = 318,                     /* SHL  */
    SHR = 319,                     /* SHR  */
    LE_OP = 320,                   /* LE_OP  */
    GE_OP = 321,                   /* GE_OP  */
    EQ_OP = 322,                   /* EQ_OP  */
    NE_OP = 323,                   /* NE_OP  */
    AND_OP = 324,                  /* AND_OP  */
    OR_OP = 325,                   /* OR_OP  */
    PLUS_ASSIGN = 326,             /* PLUS_ASSIGN  */
    MINUS_ASSIGN = 327,            /* MINUS_ASSIGN  */
    MUL_ASSIGN = 328,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 329,              /* DIV_ASSIGN  */
    MOD_ASSIGN = 330,              /* MOD_ASSIGN  */
    AND_ASSIGN = 331,              /* AND_ASSIGN  */
    OR_ASSIGN = 332,               /* OR_ASSIGN  */
    XOR_ASSIGN = 333,              /* XOR_ASSIGN  */
    SHL_ASSIGN = 334,              /* SHL_ASSIGN  */
    SHR_ASSIGN = 335,              /* SHR_ASSIGN  */
    PREFER_EXPRESSION = 336,       /* PREFER_EXPRESSION  */
    UMINUS = 337,                  /* UMINUS  */
    ADDR = 338,                    /* ADDR  */
    DEREF = 339,                   /* DEREF  */
    CAST = 340,                    /* CAST  */
    SIZEOF_TYPE = 341,             /* SIZEOF_TYPE  */
    PREFER_DECLARATION = 342,      /* PREFER_DECLARATION  */
    IFX = 343                      /* IFX  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef ParserValue YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE YYLTYPE;
struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif


extern YYSTYPE yylval;
extern YYLTYPE yylloc;

int yyparse (void);


#endif /* !YY_YY_BUILD_PARSER_TAB_HPP_INCLUDED  */
