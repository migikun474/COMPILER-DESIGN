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
    EXTERN = 278,                  /* EXTERN  */
    REGISTER = 279,                /* REGISTER  */
    CONST = 280,                   /* CONST  */
    VOLATILE = 281,                /* VOLATILE  */
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
    FILE_KW = 301,                 /* FILE_KW  */
    FOPEN = 302,                   /* FOPEN  */
    FCLOSE = 303,                  /* FCLOSE  */
    FREAD = 304,                   /* FREAD  */
    FWRITE = 305,                  /* FWRITE  */
    FPRINTF = 306,                 /* FPRINTF  */
    FSCANF = 307,                  /* FSCANF  */
    FGETS = 308,                   /* FGETS  */
    FPUTS = 309,                   /* FPUTS  */
    FEOF = 310,                    /* FEOF  */
    BOOL = 311,                    /* BOOL  */
    NEW = 312,                     /* NEW  */
    DELETE = 313,                  /* DELETE  */
    SIZEOF = 314,                  /* SIZEOF  */
    VA_LIST = 315,                 /* VA_LIST  */
    VA_START = 316,                /* VA_START  */
    VA_ARG = 317,                  /* VA_ARG  */
    VA_END = 318,                  /* VA_END  */
    MUTABLE = 319,                 /* MUTABLE  */
    OPERATOR = 320,                /* OPERATOR  */
    DELETE_ARRAY = 321,            /* DELETE_ARRAY  */
    FCAST = 322,                   /* FCAST  */
    DESIG_LBRACKET = 323,          /* DESIG_LBRACKET  */
    ABSTRACT_LPAREN = 324,         /* ABSTRACT_LPAREN  */
    IDENTIFIER = 325,              /* IDENTIFIER  */
    TYPE_NAME = 326,               /* TYPE_NAME  */
    INT_LITERAL = 327,             /* INT_LITERAL  */
    FLOAT_LITERAL = 328,           /* FLOAT_LITERAL  */
    CHAR_LITERAL = 329,            /* CHAR_LITERAL  */
    STRING_LITERAL = 330,          /* STRING_LITERAL  */
    BOOL_LITERAL = 331,            /* BOOL_LITERAL  */
    ARROW = 332,                   /* ARROW  */
    ELLIPSIS = 333,                /* ELLIPSIS  */
    SCOPE_RES = 334,               /* SCOPE_RES  */
    INC = 335,                     /* INC  */
    DEC = 336,                     /* DEC  */
    SHL = 337,                     /* SHL  */
    SHR = 338,                     /* SHR  */
    LE_OP = 339,                   /* LE_OP  */
    GE_OP = 340,                   /* GE_OP  */
    EQ_OP = 341,                   /* EQ_OP  */
    NE_OP = 342,                   /* NE_OP  */
    AND_OP = 343,                  /* AND_OP  */
    OR_OP = 344,                   /* OR_OP  */
    PLUS_ASSIGN = 345,             /* PLUS_ASSIGN  */
    MINUS_ASSIGN = 346,            /* MINUS_ASSIGN  */
    MUL_ASSIGN = 347,              /* MUL_ASSIGN  */
    DIV_ASSIGN = 348,              /* DIV_ASSIGN  */
    MOD_ASSIGN = 349,              /* MOD_ASSIGN  */
    AND_ASSIGN = 350,              /* AND_ASSIGN  */
    OR_ASSIGN = 351,               /* OR_ASSIGN  */
    XOR_ASSIGN = 352,              /* XOR_ASSIGN  */
    SHL_ASSIGN = 353,              /* SHL_ASSIGN  */
    SHR_ASSIGN = 354,              /* SHR_ASSIGN  */
    PREFER_EXPRESSION = 355,       /* PREFER_EXPRESSION  */
    NEW_TYPE_END = 356,            /* NEW_TYPE_END  */
    UMINUS = 357,                  /* UMINUS  */
    ADDR = 358,                    /* ADDR  */
    DEREF = 359,                   /* DEREF  */
    CAST = 360,                    /* CAST  */
    SIZEOF_TYPE = 361,             /* SIZEOF_TYPE  */
    PREFER_DECLARATION = 362,      /* PREFER_DECLARATION  */
    IFX = 363                      /* IFX  */
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
