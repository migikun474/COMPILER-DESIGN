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

    #include "common.h"

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
    ENUM = 268,                    /* ENUM  */
    UNION = 269,                   /* UNION  */
    CLASS = 270,                   /* CLASS  */
    PUBLIC = 271,                  /* PUBLIC  */
    PRIVATE = 272,                 /* PRIVATE  */
    PROTECTED = 273,               /* PROTECTED  */
    THIS = 274,                    /* THIS  */
    STATIC = 275,                  /* STATIC  */
    TYPEDEF = 276,                 /* TYPEDEF  */
    AUTO = 277,                    /* AUTO  */
    CONST = 278,                   /* CONST  */
    VOLATILE = 279,                /* VOLATILE  */
    IF = 280,                      /* IF  */
    ELSE = 281,                    /* ELSE  */
    FOR = 282,                     /* FOR  */
    WHILE = 283,                   /* WHILE  */
    DO = 284,                      /* DO  */
    UNTIL = 285,                   /* UNTIL  */
    SWITCH = 286,                  /* SWITCH  */
    CASE = 287,                    /* CASE  */
    DEFAULT = 288,                 /* DEFAULT  */
    BREAK = 289,                   /* BREAK  */
    CONTINUE = 290,                /* CONTINUE  */
    GOTO = 291,                    /* GOTO  */
    RETURN = 292,                  /* RETURN  */
    PRINTF = 293,                  /* PRINTF  */
    SCANF = 294,                   /* SCANF  */
    MALLOC = 295,                  /* MALLOC  */
    FREE = 296,                    /* FREE  */
    CALLOC = 297,                  /* CALLOC  */
    REALLOC = 298,                 /* REALLOC  */
    FILE_KW = 299,                 /* FILE_KW  */
    FOPEN = 300,                   /* FOPEN  */
    FCLOSE = 301,                  /* FCLOSE  */
    FREAD = 302,                   /* FREAD  */
    FWRITE = 303,                  /* FWRITE  */
    FPRINTF = 304,                 /* FPRINTF  */
    FSCANF = 305,                  /* FSCANF  */
    FGETS = 306,                   /* FGETS  */
    FPUTS = 307,                   /* FPUTS  */
    FEOF = 308,                    /* FEOF  */
    TRUE_TOK = 309,                /* TRUE_TOK  */
    FALSE_TOK = 310,               /* FALSE_TOK  */
    BOOL = 311,                    /* BOOL  */
    NEW = 312,                     /* NEW  */
    DELETE = 313,                  /* DELETE  */
    SIZEOF = 314,                  /* SIZEOF  */
    IDENTIFIER = 315,              /* IDENTIFIER  */
    TYPE_NAME = 316,               /* TYPE_NAME  */
    INT_LITERAL = 317,             /* INT_LITERAL  */
    FLOAT_LITERAL = 318,           /* FLOAT_LITERAL  */
    CHAR_LITERAL = 319,            /* CHAR_LITERAL  */
    STRING_LITERAL = 320,          /* STRING_LITERAL  */
    ARROW = 321,                   /* ARROW  */
    ELLIPSIS = 322,                /* ELLIPSIS  */
    SCOPE_RES = 323,               /* SCOPE_RES  */
    INC = 324,                     /* INC  */
    DEC = 325,                     /* DEC  */
    SHL = 326,                     /* SHL  */
    SHR = 327,                     /* SHR  */
    LE_OP = 328,                   /* LE_OP  */
    GE_OP = 329,                   /* GE_OP  */
    EQ_OP = 330,                   /* EQ_OP  */
    NE_OP = 331,                   /* NE_OP  */
    AND_OP = 332,                  /* AND_OP  */
    OR_OP = 333,                   /* OR_OP  */
    PLUS_ASSIGN = 334,             /* PLUS_ASSIGN  */
    MINUS_ASSIGN = 335,            /* MINUS_ASSIGN  */
    MUL_ASSIGN = 336,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 337,              /* DIV_ASSIGN  */
    MOD_ASSIGN = 338,              /* MOD_ASSIGN  */
    AND_ASSIGN = 339,              /* AND_ASSIGN  */
    OR_ASSIGN = 340,               /* OR_ASSIGN  */
    XOR_ASSIGN = 341,              /* XOR_ASSIGN  */
    SHL_ASSIGN = 342,              /* SHL_ASSIGN  */
    SHR_ASSIGN = 343,              /* SHR_ASSIGN  */
    UMINUS = 344,                  /* UMINUS  */
    ADDR = 345,                    /* ADDR  */
    DEREF = 346,                   /* DEREF  */
    CAST = 347,                    /* CAST  */
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
