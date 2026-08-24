#include "token_converter.hpp"
#include "parser.tab.hpp"

int to_bison_token(TokenType t) {
    switch (t) {
        // ---- literals / values ----
        case TokenType::IDENTIFIER:      return IDENTIFIER;
        case TokenType::INT_LITERAL:     return INT_LITERAL;
        case TokenType::FLOAT_LITERAL:   return FLOAT_LITERAL;
        case TokenType::CHAR_LITERAL:    return CHAR_LITERAL;
        case TokenType::STRING_LITERAL:  return STRING_LITERAL;
        case TokenType::BOOL_LITERAL:    return BOOL_LITERAL;

        // ---- primitive type keywords ----
        case TokenType::INT:      return INT;
        case TokenType::CHAR:     return CHAR;
        case TokenType::FLOAT:    return FLOAT;
        case TokenType::DOUBLE:   return DOUBLE;
        case TokenType::VOID:     return VOID;
        case TokenType::SHORT:    return SHORT;
        case TokenType::LONG:     return LONG;
        case TokenType::SIGNED:   return SIGNED;
        case TokenType::UNSIGNED: return UNSIGNED;
        case TokenType::BOOL:     return BOOL;

        // ---- qualifiers ----
        case TokenType::CONST:    return CONST;
        case TokenType::VOLATILE: return VOLATILE;

        // ---- composite-type keywords ----
        case TokenType::STRUCT: return STRUCT;
        case TokenType::ENUM:   return ENUM;
        case TokenType::UNION:  return UNION;
        case TokenType::CLASS:  return CLASS;

        // ---- access modifiers ----
        case TokenType::PUBLIC:    return PUBLIC;
        case TokenType::PRIVATE:   return PRIVATE;
        case TokenType::PROTECTED: return PROTECTED;

        // ---- object-oriented ----
        case TokenType::THIS:   return THIS;
        case TokenType::NEW:    return NEW;
        case TokenType::DELETE: return DELETE;

        // ---- storage-class keywords ----
        case TokenType::STATIC:  return STATIC;
        case TokenType::TYPEDEF: return TYPEDEF;
        case TokenType::AUTO:    return AUTO;

        // ---- control-flow keywords ----
        case TokenType::IF:       return IF;
        case TokenType::ELSE:     return ELSE;
        case TokenType::FOR:      return FOR;
        case TokenType::WHILE:    return WHILE;
        case TokenType::DO:       return DO;
        case TokenType::UNTIL:    return UNTIL;
        case TokenType::SWITCH:   return SWITCH;
        case TokenType::CASE:     return CASE;
        case TokenType::DEFAULT:  return DEFAULT;
        case TokenType::BREAK:    return BREAK;
        case TokenType::CONTINUE: return CONTINUE;
        case TokenType::GOTO:     return GOTO;
        case TokenType::RETURN:   return RETURN;

        // ---- misc operator-like keyword ----
        case TokenType::SIZEOF: return SIZEOF;

        // ---- I/O keywords ----
        case TokenType::PRINTF: return PRINTF;
        case TokenType::SCANF:  return SCANF;

        // ---- dynamic-memory keywords ----
        case TokenType::MALLOC:  return MALLOC;
        case TokenType::FREE:    return FREE;
        case TokenType::CALLOC:  return CALLOC;
        case TokenType::REALLOC: return REALLOC;

        // ---- file-manipulation keywords ----
        case TokenType::FILE_KEYWORD: return FILE_KW;
        case TokenType::FOPEN:        return FOPEN;
        case TokenType::FCLOSE:       return FCLOSE;
        case TokenType::FREAD:        return FREAD;
        case TokenType::FWRITE:       return FWRITE;
        case TokenType::FPRINTF:      return FPRINTF;
        case TokenType::FSCANF:       return FSCANF;
        case TokenType::FGETS:        return FGETS;
        case TokenType::FPUTS:        return FPUTS;
        case TokenType::FEOF:         return FEOF;

        // ---- multi-character operators ----
        case TokenType::ARROW_OP:            return ARROW;
        case TokenType::ELLIPSIS_OP:         return ELLIPSIS;
        case TokenType::SCOPE_RESOLUTION_OP: return SCOPE_RES;

        case TokenType::PLUS_ASSIGN_OP:      return PLUS_ASSIGN;
        case TokenType::MINUS_ASSIGN_OP:     return MINUS_ASSIGN;
        case TokenType::STAR_ASSIGN_OP:      return MUL_ASSIGN;
        case TokenType::DIVIDE_ASSIGN_OP:    return DIV_ASSIGN;
        case TokenType::MOD_ASSIGN_OP:       return MOD_ASSIGN;
        case TokenType::AMPERSAND_ASSIGN_OP: return AND_ASSIGN;
        case TokenType::PIPE_ASSIGN_OP:      return OR_ASSIGN;
        case TokenType::CARET_ASSIGN_OP:     return XOR_ASSIGN;
        case TokenType::LSHIFT_ASSIGN_OP:    return SHL_ASSIGN;
        case TokenType::RSHIFT_ASSIGN_OP:    return SHR_ASSIGN;

        case TokenType::LOGICAL_AND_OP: return AND_OP;
        case TokenType::LOGICAL_OR_OP:  return OR_OP;
        case TokenType::EQ_OP:          return EQ_OP;
        case TokenType::NE_OP:          return NE_OP;
        case TokenType::LE_OP:          return LE_OP;
        case TokenType::GE_OP:          return GE_OP;

        case TokenType::INCREMENT_OP: return INC;
        case TokenType::DECREMENT_OP: return DEC;

        case TokenType::LSHIFT_OP: return SHL;
        case TokenType::RSHIFT_OP: return SHR;

        // ---- single-character operators/punctuation: Bison treats a
        // quoted-char token like '+' as its own ASCII value, so these
        // just pass the character straight through. ----
        case TokenType::DOT_OP:          return '.';
        case TokenType::QUESTION_OP:     return '?';
        case TokenType::ASSIGN_OP:       return '=';
        case TokenType::LOGICAL_NOT_OP:  return '!';
        case TokenType::LT_OP:           return '<';
        case TokenType::GT_OP:           return '>';
        case TokenType::PLUS_OP:         return '+';
        case TokenType::MINUS_OP:        return '-';
        case TokenType::STAR_OP:         return '*';
        case TokenType::DIVIDE_OP:       return '/';
        case TokenType::MOD_OP:          return '%';
        case TokenType::AMPERSAND_OP:    return '&';
        case TokenType::PIPE_OP:         return '|';
        case TokenType::CARET_OP:        return '^';
        case TokenType::TILDE_OP:        return '~';
        case TokenType::COMMA_OP:        return ',';
        case TokenType::SEMICOLON_OP:    return ';';
        case TokenType::COLON_OP:        return ':';
        case TokenType::OPEN_PAREN_OP:   return '(';
        case TokenType::CLOSE_PAREN_OP:  return ')';
        case TokenType::OPEN_BRACE_OP:   return '{';
        case TokenType::CLOSE_BRACE_OP:  return '}';
        case TokenType::OPEN_BRACKET_OP: return '[';
        case TokenType::CLOSE_BRACKET_OP:return ']';
    }
    return -1; /* unreachable if the switch above is kept exhaustive --
                  -Wswitch (part of -Wall) warns at compile time if a
                  new TokenType is added to the shared enum without a
                  corresponding case here. */
}
