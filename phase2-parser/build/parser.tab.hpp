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
    ENUM = 269,                    /* ENUM  */
    PUBLIC = 270,                  /* PUBLIC  */
    PRIVATE = 271,                 /* PRIVATE  */
    PROTECTED = 272,               /* PROTECTED  */
    THIS = 273,                    /* THIS  */
    STATIC = 274,                  /* STATIC  */
    TYPEDEF = 275,                 /* TYPEDEF  */
    AUTO = 276,                    /* AUTO  */
    CONST = 277,                   /* CONST  */
    FRIEND = 278,                  /* FRIEND  */
    VIRTUAL = 279,                 /* VIRTUAL  */
    EXPLICIT = 280,                /* EXPLICIT  */
    IF = 281,                      /* IF  */
    ELSE = 282,                    /* ELSE  */
    FOR = 283,                     /* FOR  */
    WHILE = 284,                   /* WHILE  */
    DO = 285,                      /* DO  */
    UNTIL = 286,                   /* UNTIL  */
    SWITCH = 287,                  /* SWITCH  */
    CASE = 288,                    /* CASE  */
    DEFAULT = 289,                 /* DEFAULT  */
    BREAK = 290,                   /* BREAK  */
    CONTINUE = 291,                /* CONTINUE  */
    GOTO = 292,                    /* GOTO  */
    RETURN = 293,                  /* RETURN  */
    PRINTF = 294,                  /* PRINTF  */
    SCANF = 295,                   /* SCANF  */
    MALLOC = 296,                  /* MALLOC  */
    FREE = 297,                    /* FREE  */
    CALLOC = 298,                  /* CALLOC  */
    REALLOC = 299,                 /* REALLOC  */
    BOOL = 300,                    /* BOOL  */
    SIZEOF = 301,                  /* SIZEOF  */
    OPERATOR = 302,                /* OPERATOR  */
    FCAST = 303,                   /* FCAST  */
    ABSTRACT_LPAREN = 304,         /* ABSTRACT_LPAREN  */
    IDENTIFIER = 305,              /* IDENTIFIER  */
    TYPE_NAME = 306,               /* TYPE_NAME  */
    INT_LITERAL = 307,             /* INT_LITERAL  */
    FLOAT_LITERAL = 308,           /* FLOAT_LITERAL  */
    CHAR_LITERAL = 309,            /* CHAR_LITERAL  */
    STRING_LITERAL = 310,          /* STRING_LITERAL  */
    BOOL_LITERAL = 311,            /* BOOL_LITERAL  */
    ARROW = 312,                   /* ARROW  */
    ELLIPSIS = 313,                /* ELLIPSIS  */
    SCOPE_RES = 314,               /* SCOPE_RES  */
    INC = 315,                     /* INC  */
    DEC = 316,                     /* DEC  */
    SHL = 317,                     /* SHL  */
    SHR = 318,                     /* SHR  */
    LE_OP = 319,                   /* LE_OP  */
    GE_OP = 320,                   /* GE_OP  */
    EQ_OP = 321,                   /* EQ_OP  */
    NE_OP = 322,                   /* NE_OP  */
    AND_OP = 323,                  /* AND_OP  */
    OR_OP = 324,                   /* OR_OP  */
    PLUS_ASSIGN = 325,             /* PLUS_ASSIGN  */
    MINUS_ASSIGN = 326,            /* MINUS_ASSIGN  */
    MUL_ASSIGN = 327,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 328,              /* DIV_ASSIGN  */
    MOD_ASSIGN = 329,              /* MOD_ASSIGN  */
    AND_ASSIGN = 330,              /* AND_ASSIGN  */
    OR_ASSIGN = 331,               /* OR_ASSIGN  */
    XOR_ASSIGN = 332,              /* XOR_ASSIGN  */
    SHL_ASSIGN = 333,              /* SHL_ASSIGN  */
    SHR_ASSIGN = 334,              /* SHR_ASSIGN  */
    PREFER_EXPRESSION = 335,       /* PREFER_EXPRESSION  */
    UMINUS = 336,                  /* UMINUS  */
    ADDR = 337,                    /* ADDR  */
    DEREF = 338,                   /* DEREF  */
    CAST = 339,                    /* CAST  */
    SIZEOF_TYPE = 340,             /* SIZEOF_TYPE  */
    PREFER_DECLARATION = 341,      /* PREFER_DECLARATION  */
    IFX = 342                      /* IFX  */
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
