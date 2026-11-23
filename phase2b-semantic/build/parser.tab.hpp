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
    CONST = 278,                   /* CONST  */
    FRIEND = 279,                  /* FRIEND  */
    VIRTUAL = 280,                 /* VIRTUAL  */
    EXPLICIT = 281,                /* EXPLICIT  */
    IF = 282,                      /* IF  */
    ELSE = 283,                    /* ELSE  */
    FOR = 284,                     /* FOR  */
    WHILE = 285,                   /* WHILE  */
    DO = 286,                      /* DO  */
    UNTIL = 287,                   /* UNTIL  */
    SWITCH = 288,                  /* SWITCH  */
    CASE = 289,                    /* CASE  */
    DEFAULT = 290,                 /* DEFAULT  */
    BREAK = 291,                   /* BREAK  */
    CONTINUE = 292,                /* CONTINUE  */
    GOTO = 293,                    /* GOTO  */
    RETURN = 294,                  /* RETURN  */
    PRINTF = 295,                  /* PRINTF  */
    SCANF = 296,                   /* SCANF  */
    MALLOC = 297,                  /* MALLOC  */
    FREE = 298,                    /* FREE  */
    CALLOC = 299,                  /* CALLOC  */
    REALLOC = 300,                 /* REALLOC  */
    BOOL = 301,                    /* BOOL  */
    SIZEOF = 302,                  /* SIZEOF  */
    VA_LIST = 303,                 /* VA_LIST  */
    VA_START = 304,                /* VA_START  */
    VA_ARG = 305,                  /* VA_ARG  */
    VA_END = 306,                  /* VA_END  */
    OPERATOR = 307,                /* OPERATOR  */
    FCAST = 308,                   /* FCAST  */
    ABSTRACT_LPAREN = 309,         /* ABSTRACT_LPAREN  */
    IDENTIFIER = 310,              /* IDENTIFIER  */
    TYPE_NAME = 311,               /* TYPE_NAME  */
    INT_LITERAL = 312,             /* INT_LITERAL  */
    FLOAT_LITERAL = 313,           /* FLOAT_LITERAL  */
    CHAR_LITERAL = 314,            /* CHAR_LITERAL  */
    STRING_LITERAL = 315,          /* STRING_LITERAL  */
    BOOL_LITERAL = 316,            /* BOOL_LITERAL  */
    ARROW = 317,                   /* ARROW  */
    ELLIPSIS = 318,                /* ELLIPSIS  */
    SCOPE_RES = 319,               /* SCOPE_RES  */
    INC = 320,                     /* INC  */
    DEC = 321,                     /* DEC  */
    SHL = 322,                     /* SHL  */
    SHR = 323,                     /* SHR  */
    LE_OP = 324,                   /* LE_OP  */
    GE_OP = 325,                   /* GE_OP  */
    EQ_OP = 326,                   /* EQ_OP  */
    NE_OP = 327,                   /* NE_OP  */
    AND_OP = 328,                  /* AND_OP  */
    OR_OP = 329,                   /* OR_OP  */
    PLUS_ASSIGN = 330,             /* PLUS_ASSIGN  */
    MINUS_ASSIGN = 331,            /* MINUS_ASSIGN  */
    MUL_ASSIGN = 332,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 333,              /* DIV_ASSIGN  */
    MOD_ASSIGN = 334,              /* MOD_ASSIGN  */
    AND_ASSIGN = 335,              /* AND_ASSIGN  */
    OR_ASSIGN = 336,               /* OR_ASSIGN  */
    XOR_ASSIGN = 337,              /* XOR_ASSIGN  */
    SHL_ASSIGN = 338,              /* SHL_ASSIGN  */
    SHR_ASSIGN = 339,              /* SHR_ASSIGN  */
    PREFER_EXPRESSION = 340,       /* PREFER_EXPRESSION  */
    UMINUS = 341,                  /* UMINUS  */
    ADDR = 342,                    /* ADDR  */
    DEREF = 343,                   /* DEREF  */
    CAST = 344,                    /* CAST  */
    SIZEOF_TYPE = 345,             /* SIZEOF_TYPE  */
    PREFER_DECLARATION = 346,      /* PREFER_DECLARATION  */
    IFX = 347                      /* IFX  */
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
