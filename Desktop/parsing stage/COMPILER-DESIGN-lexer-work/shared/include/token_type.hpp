#ifndef TOKEN_TYPE_HPP
#define TOKEN_TYPE_HPP

#include <optional>
#include <string>

/* This enum, and the tables below it, are the single source of truth
 * for "what are this language's keywords and operators" -- used by
 * BOTH phase1-lexer (which classifies a whole file up front into a
 * Lexeme/Token table) and phase2-parser (whose scanner classifies
 * tokens on demand, on Bison's request, and additionally maps each
 * TokenType to Bison's own generated token codes via
 * phase2-parser/include/token_converter.hpp).
 *
 * Previously these tables were duplicated by hand in
 * phase2-parser/src/scanner.l, which meant the two phases' notion of
 * "what counts as a keyword" or "what to call the '{' operator" could
 * silently drift apart -- and did, at least once. Sharing this file
 * makes that class of bug structurally impossible: there is exactly
 * one keyword_map, one operator_map, one to_string(), and both phases
 * link against the same compiled object.
 */
enum class TokenType {
    // ---- literals / values (not "keywords" -- these denote a value,
    // not a structural role) ----
    IDENTIFIER,
    INT_LITERAL,
    FLOAT_LITERAL,
    CHAR_LITERAL,
    STRING_LITERAL,
    BOOL_LITERAL,

    // ---- primitive type keywords ----
    INT,
    CHAR,
    FLOAT,
    DOUBLE,
    VOID,
    SHORT,
    LONG,
    SIGNED,
    UNSIGNED,
    BOOL,

    // ---- type qualifiers ----
    CONST,
    VOLATILE,

    // ---- composite-type keywords (introduce a user-defined type) ----
    STRUCT,
    ENUM,
    UNION,
    CLASS,

    // ---- access modifiers ----
    PUBLIC,
    PRIVATE,
    PROTECTED,

    // ---- object-oriented ----
    THIS,
    NEW,
    DELETE,

    // ---- storage-class keywords ----
    STATIC,
    TYPEDEF,
    AUTO,

    // ---- control-flow keywords ----
    IF,
    ELSE,
    FOR,
    WHILE,
    DO,
    UNTIL,
    SWITCH,
    CASE,
    DEFAULT,
    BREAK,
    CONTINUE,
    GOTO,
    RETURN,

    // ---- misc operator-like keyword ----
    SIZEOF,

    // ---- I/O keywords (custom to this language -- real C treats these
    // as ordinary <stdio.h> library identifiers, not reserved words) ----
    PRINTF,
    SCANF,

    // ---- dynamic-memory keywords (custom to this language) ----
    MALLOC,
    FREE,
    CALLOC,
    REALLOC,

    // ---- file-manipulation keywords (custom to this language) ----
    FILE_KEYWORD,
    FOPEN,
    FCLOSE,
    FREAD,
    FWRITE,
    FPRINTF,
    FSCANF,
    FGETS,
    FPUTS,
    FEOF,

    // ---- operators ----
    ARROW_OP,
    DOT_OP,
    QUESTION_OP,
    ELLIPSIS_OP,
    SCOPE_RESOLUTION_OP,

    ASSIGN_OP,
    PLUS_ASSIGN_OP,
    MINUS_ASSIGN_OP,
    STAR_ASSIGN_OP,
    DIVIDE_ASSIGN_OP,
    MOD_ASSIGN_OP,
    AMPERSAND_ASSIGN_OP,
    PIPE_ASSIGN_OP,
    CARET_ASSIGN_OP,
    LSHIFT_ASSIGN_OP,
    RSHIFT_ASSIGN_OP,

    LOGICAL_AND_OP,
    LOGICAL_OR_OP,
    LOGICAL_NOT_OP,
    EQ_OP,
    NE_OP,
    LT_OP,
    GT_OP,
    LE_OP,
    GE_OP,

    INCREMENT_OP,
    DECREMENT_OP,

    PLUS_OP,
    MINUS_OP,
    STAR_OP,
    DIVIDE_OP,
    MOD_OP,

    AMPERSAND_OP,
    PIPE_OP,
    CARET_OP,
    TILDE_OP,
    LSHIFT_OP,
    RSHIFT_OP,

    COMMA_OP,
    SEMICOLON_OP,
    COLON_OP,

    OPEN_PAREN_OP,
    CLOSE_PAREN_OP,
    OPEN_BRACE_OP,
    CLOSE_BRACE_OP,
    OPEN_BRACKET_OP,
    CLOSE_BRACKET_OP
};

std::string to_string(TokenType type);
std::optional<TokenType> reserved_word(const std::string &str);
std::optional<TokenType> operator_token(const std::string &str);

#endif
