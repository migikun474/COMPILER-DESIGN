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
#line 1 "../phase2-parser/src/parser.y"

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
    UNION = 269,                   /* UNION  */
    ENUM = 270,                    /* ENUM  */
    PUBLIC = 271,                  /* PUBLIC  */
    PRIVATE = 272,                 /* PRIVATE  */
    PROTECTED = 273,               /* PROTECTED  */
    THIS = 274,                    /* THIS  */
    STATIC = 275,                  /* STATIC  */
    TYPEDEF = 276,                 /* TYPEDEF  */
    AUTO = 277,                    /* AUTO  */
    EXTERN = 278,                  /* EXTERN  */
    CONST = 279,                   /* CONST  */
    FRIEND = 280,                  /* FRIEND  */
    VIRTUAL = 281,                 /* VIRTUAL  */
    EXPLICIT = 282,                /* EXPLICIT  */
    IF = 283,                      /* IF  */
    ELSE = 284,                    /* ELSE  */
    FOR = 285,                     /* FOR  */
    WHILE = 286,                   /* WHILE  */
    DO = 287,                      /* DO  */
    UNTIL = 288,                   /* UNTIL  */
    SWITCH = 289,                  /* SWITCH  */
    CASE = 290,                    /* CASE  */
    DEFAULT = 291,                 /* DEFAULT  */
    BREAK = 292,                   /* BREAK  */
    CONTINUE = 293,                /* CONTINUE  */
    GOTO = 294,                    /* GOTO  */
    RETURN = 295,                  /* RETURN  */
    PRINTF = 296,                  /* PRINTF  */
    SCANF = 297,                   /* SCANF  */
    MALLOC = 298,                  /* MALLOC  */
    FREE = 299,                    /* FREE  */
    CALLOC = 300,                  /* CALLOC  */
    REALLOC = 301,                 /* REALLOC  */
    BOOL = 302,                    /* BOOL  */
    SIZEOF = 303,                  /* SIZEOF  */
    VA_LIST = 304,                 /* VA_LIST  */
    VA_START = 305,                /* VA_START  */
    VA_ARG = 306,                  /* VA_ARG  */
    VA_END = 307,                  /* VA_END  */
    OPERATOR = 308,                /* OPERATOR  */
    FCAST = 309,                   /* FCAST  */
    ABSTRACT_LPAREN = 310,         /* ABSTRACT_LPAREN  */
    IDENTIFIER = 311,              /* IDENTIFIER  */
    TYPE_NAME = 312,               /* TYPE_NAME  */
    INT_LITERAL = 313,             /* INT_LITERAL  */
    FLOAT_LITERAL = 314,           /* FLOAT_LITERAL  */
    CHAR_LITERAL = 315,            /* CHAR_LITERAL  */
    STRING_LITERAL = 316,          /* STRING_LITERAL  */
    BOOL_LITERAL = 317,            /* BOOL_LITERAL  */
    ARROW = 318,                   /* ARROW  */
    ELLIPSIS = 319,                /* ELLIPSIS  */
    SCOPE_RES = 320,               /* SCOPE_RES  */
    INC = 321,                     /* INC  */
    DEC = 322,                     /* DEC  */
    SHL = 323,                     /* SHL  */
    SHR = 324,                     /* SHR  */
    LE_OP = 325,                   /* LE_OP  */
    GE_OP = 326,                   /* GE_OP  */
    EQ_OP = 327,                   /* EQ_OP  */
    NE_OP = 328,                   /* NE_OP  */
    AND_OP = 329,                  /* AND_OP  */
    OR_OP = 330,                   /* OR_OP  */
    PLUS_ASSIGN = 331,             /* PLUS_ASSIGN  */
    MINUS_ASSIGN = 332,            /* MINUS_ASSIGN  */
    MUL_ASSIGN = 333,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 334,              /* DIV_ASSIGN  */
    MOD_ASSIGN = 335,              /* MOD_ASSIGN  */
    AND_ASSIGN = 336,              /* AND_ASSIGN  */
    OR_ASSIGN = 337,               /* OR_ASSIGN  */
    XOR_ASSIGN = 338,              /* XOR_ASSIGN  */
    SHL_ASSIGN = 339,              /* SHL_ASSIGN  */
    SHR_ASSIGN = 340,              /* SHR_ASSIGN  */
    PREFER_EXPRESSION = 341,       /* PREFER_EXPRESSION  */
    UMINUS = 342,                  /* UMINUS  */
    ADDR = 343,                    /* ADDR  */
    DEREF = 344,                   /* DEREF  */
    CAST = 345,                    /* CAST  */
    SIZEOF_TYPE = 346,             /* SIZEOF_TYPE  */
    PREFER_DECLARATION = 347,      /* PREFER_DECLARATION  */
    IFX = 348                      /* IFX  */
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
