#include "token_type.hpp"

#include <unordered_map>

static const std::unordered_map<std::string, TokenType> keyword_map = {
    // primitive types
    {"int", TokenType::INT},
    {"char", TokenType::CHAR},
    {"float", TokenType::FLOAT},
    {"double", TokenType::DOUBLE},
    {"void", TokenType::VOID},
    {"short", TokenType::SHORT},
    {"long", TokenType::LONG},
    {"signed", TokenType::SIGNED},
    {"unsigned", TokenType::UNSIGNED},

    // composite types
    {"struct", TokenType::STRUCT},
    {"enum", TokenType::ENUM},
    {"union", TokenType::UNION},
    {"class", TokenType::CLASS},

    // access modifiers
    {"public", TokenType::PUBLIC},
    {"private", TokenType::PRIVATE},
    {"protected", TokenType::PROTECTED},

    // object-oriented
    {"this", TokenType::THIS},

    // storage class
    {"static", TokenType::STATIC},
    {"typedef", TokenType::TYPEDEF},
    {"auto", TokenType::AUTO},

    // control flow
    {"if", TokenType::IF},
    {"else", TokenType::ELSE},
    {"for", TokenType::FOR},
    {"while", TokenType::WHILE},
    {"do", TokenType::DO},
    {"until", TokenType::UNTIL},
    {"switch", TokenType::SWITCH},
    {"case", TokenType::CASE},
    {"default", TokenType::DEFAULT},
    {"break", TokenType::BREAK},
    {"continue", TokenType::CONTINUE},
    {"goto", TokenType::GOTO},
    {"return", TokenType::RETURN},

    // I/O (custom reserved words -- see token_type.hpp)
    {"printf", TokenType::PRINTF},
    {"scanf", TokenType::SCANF},

    // dynamic memory (custom reserved words)
    {"malloc", TokenType::MALLOC},
    {"free", TokenType::FREE},
    {"calloc", TokenType::CALLOC},
    {"realloc", TokenType::REALLOC},

    // file manipulation (custom reserved words)
    {"FILE", TokenType::FILE_KEYWORD},
    {"fopen", TokenType::FOPEN},
    {"fclose", TokenType::FCLOSE},
    {"fread", TokenType::FREAD},
    {"fwrite", TokenType::FWRITE},
    {"fprintf", TokenType::FPRINTF},
    {"fscanf", TokenType::FSCANF},
    {"fgets", TokenType::FGETS},
    {"fputs", TokenType::FPUTS},
    {"feof", TokenType::FEOF},

    // boolean literals -- returned via keyword_map like the reference
    // does, even though they're categorized as a LITERAL, not a
    // "keyword", once looked up (see TokenType::BOOL_LITERAL)
    {"true", TokenType::BOOL_LITERAL},
    {"false", TokenType::BOOL_LITERAL},
};

static const std::unordered_map<std::string, TokenType> operator_map = {
    {"->", TokenType::ARROW_OP},
    {".", TokenType::DOT_OP},
    {"?", TokenType::QUESTION_OP},
    {"...", TokenType::ELLIPSIS_OP},
    {"::", TokenType::SCOPE_RESOLUTION_OP},

    {"=", TokenType::ASSIGN_OP},
    {"+=", TokenType::PLUS_ASSIGN_OP},
    {"-=", TokenType::MINUS_ASSIGN_OP},
    {"*=", TokenType::STAR_ASSIGN_OP},
    {"/=", TokenType::DIVIDE_ASSIGN_OP},
    {"%=", TokenType::MOD_ASSIGN_OP},
    {"&=", TokenType::AMPERSAND_ASSIGN_OP},
    {"|=", TokenType::PIPE_ASSIGN_OP},
    {"^=", TokenType::CARET_ASSIGN_OP},
    {"<<=", TokenType::LSHIFT_ASSIGN_OP},
    {">>=", TokenType::RSHIFT_ASSIGN_OP},

    {"&&", TokenType::LOGICAL_AND_OP},
    {"||", TokenType::LOGICAL_OR_OP},
    {"!", TokenType::LOGICAL_NOT_OP},
    {"==", TokenType::EQ_OP},
    {"!=", TokenType::NE_OP},

    {"<", TokenType::LT_OP},
    {">", TokenType::GT_OP},
    {"<=", TokenType::LE_OP},
    {">=", TokenType::GE_OP},

    {"++", TokenType::INCREMENT_OP},
    {"--", TokenType::DECREMENT_OP},

    {"+", TokenType::PLUS_OP},
    {"-", TokenType::MINUS_OP},
    {"*", TokenType::STAR_OP},
    {"/", TokenType::DIVIDE_OP},
    {"%", TokenType::MOD_OP},

    {"&", TokenType::AMPERSAND_OP},
    {"|", TokenType::PIPE_OP},
    {"^", TokenType::CARET_OP},
    {"~", TokenType::TILDE_OP},
    {"<<", TokenType::LSHIFT_OP},
    {">>", TokenType::RSHIFT_OP},

    {",", TokenType::COMMA_OP},
    {";", TokenType::SEMICOLON_OP},
    {":", TokenType::COLON_OP},

    {"(", TokenType::OPEN_PAREN_OP},
    {")", TokenType::CLOSE_PAREN_OP},
    {"{", TokenType::OPEN_BRACE_OP},
    {"}", TokenType::CLOSE_BRACE_OP},
    {"[", TokenType::OPEN_BRACKET_OP},
    {"]", TokenType::CLOSE_BRACKET_OP},
};

static const std::unordered_map<TokenType, std::string> token_to_string_map = {
    {TokenType::IDENTIFIER, "identifier"},
    {TokenType::INT_LITERAL, "int_literal"},
    {TokenType::FLOAT_LITERAL, "float_literal"},
    {TokenType::CHAR_LITERAL, "char_literal"},
    {TokenType::STRING_LITERAL, "string_literal"},
    {TokenType::BOOL_LITERAL, "bool_literal"},

    {TokenType::INT, "int"},
    {TokenType::CHAR, "char"},
    {TokenType::FLOAT, "float"},
    {TokenType::DOUBLE, "double"},
    {TokenType::VOID, "void"},
    {TokenType::SHORT, "short"},
    {TokenType::LONG, "long"},
    {TokenType::SIGNED, "signed"},
    {TokenType::UNSIGNED, "unsigned"},

    {TokenType::STRUCT, "struct"},
    {TokenType::ENUM, "enum"},
    {TokenType::UNION, "union"},
    {TokenType::CLASS, "class"},

    {TokenType::PUBLIC, "public"},
    {TokenType::PRIVATE, "private"},
    {TokenType::PROTECTED, "protected"},

    {TokenType::THIS, "this"},

    {TokenType::STATIC, "static"},
    {TokenType::TYPEDEF, "typedef"},
    {TokenType::AUTO, "auto"},

    {TokenType::IF, "if"},
    {TokenType::ELSE, "else"},
    {TokenType::FOR, "for"},
    {TokenType::WHILE, "while"},
    {TokenType::DO, "do"},
    {TokenType::UNTIL, "until"},
    {TokenType::SWITCH, "switch"},
    {TokenType::CASE, "case"},
    {TokenType::DEFAULT, "default"},
    {TokenType::BREAK, "break"},
    {TokenType::CONTINUE, "continue"},
    {TokenType::GOTO, "goto"},
    {TokenType::RETURN, "return"},

    {TokenType::PRINTF, "printf"},
    {TokenType::SCANF, "scanf"},

    {TokenType::MALLOC, "malloc"},
    {TokenType::FREE, "free"},
    {TokenType::CALLOC, "calloc"},
    {TokenType::REALLOC, "realloc"},

    {TokenType::FILE_KEYWORD, "file"},
    {TokenType::FOPEN, "fopen"},
    {TokenType::FCLOSE, "fclose"},
    {TokenType::FREAD, "fread"},
    {TokenType::FWRITE, "fwrite"},
    {TokenType::FPRINTF, "fprintf"},
    {TokenType::FSCANF, "fscanf"},
    {TokenType::FGETS, "fgets"},
    {TokenType::FPUTS, "fputs"},
    {TokenType::FEOF, "feof"},

    {TokenType::ARROW_OP, "arrow_op"},
    {TokenType::DOT_OP, "dot_op"},
    {TokenType::QUESTION_OP, "question_op"},
    {TokenType::ELLIPSIS_OP, "ellipsis_op"},
    {TokenType::SCOPE_RESOLUTION_OP, "scope_resolution_op"},

    {TokenType::ASSIGN_OP, "assign_op"},
    {TokenType::PLUS_ASSIGN_OP, "plus_assign_op"},
    {TokenType::MINUS_ASSIGN_OP, "minus_assign_op"},
    {TokenType::STAR_ASSIGN_OP, "star_assign_op"},
    {TokenType::DIVIDE_ASSIGN_OP, "divide_assign_op"},
    {TokenType::MOD_ASSIGN_OP, "mod_assign_op"},
    {TokenType::AMPERSAND_ASSIGN_OP, "ampersand_assign_op"},
    {TokenType::PIPE_ASSIGN_OP, "pipe_assign_op"},
    {TokenType::CARET_ASSIGN_OP, "caret_assign_op"},
    {TokenType::LSHIFT_ASSIGN_OP, "lshift_assign_op"},
    {TokenType::RSHIFT_ASSIGN_OP, "rshift_assign_op"},

    {TokenType::LOGICAL_AND_OP, "logical_and_op"},
    {TokenType::LOGICAL_OR_OP, "logical_or_op"},
    {TokenType::LOGICAL_NOT_OP, "logical_not_op"},
    {TokenType::EQ_OP, "eq_op"},
    {TokenType::NE_OP, "ne_op"},
    {TokenType::LT_OP, "lt_op"},
    {TokenType::GT_OP, "gt_op"},
    {TokenType::LE_OP, "le_op"},
    {TokenType::GE_OP, "ge_op"},

    {TokenType::INCREMENT_OP, "increment_op"},
    {TokenType::DECREMENT_OP, "decrement_op"},

    {TokenType::PLUS_OP, "plus_op"},
    {TokenType::MINUS_OP, "minus_op"},
    {TokenType::STAR_OP, "star_op"},
    {TokenType::DIVIDE_OP, "divide_op"},
    {TokenType::MOD_OP, "mod_op"},

    {TokenType::AMPERSAND_OP, "ampersand_op"},
    {TokenType::PIPE_OP, "pipe_op"},
    {TokenType::CARET_OP, "caret_op"},
    {TokenType::TILDE_OP, "tilde_op"},
    {TokenType::LSHIFT_OP, "lshift_op"},
    {TokenType::RSHIFT_OP, "rshift_op"},

    {TokenType::COMMA_OP, "comma_op"},
    {TokenType::SEMICOLON_OP, "semicolon_op"},
    {TokenType::COLON_OP, "colon_op"},

    {TokenType::OPEN_PAREN_OP, "open_paren_op"},
    {TokenType::CLOSE_PAREN_OP, "close_paren_op"},
    {TokenType::OPEN_BRACE_OP, "open_brace_op"},
    {TokenType::CLOSE_BRACE_OP, "close_brace_op"},
    {TokenType::OPEN_BRACKET_OP, "open_bracket_op"},
    {TokenType::CLOSE_BRACKET_OP, "close_bracket_op"},
};

std::string to_string(TokenType type) {
    auto it = token_to_string_map.find(type);
    if (it != token_to_string_map.end()) {
        return it->second;
    }
    return "UNKNOWN";
}

std::optional<TokenType> reserved_word(const std::string &str) {
    auto it = keyword_map.find(str);
    if (it != keyword_map.end()) {
        return it->second;
    }
    return std::nullopt;
}

std::optional<TokenType> operator_token(const std::string &str) {
    auto it = operator_map.find(str);
    if (it != operator_map.end()) {
        return it->second;
    }
    return std::nullopt;
}
