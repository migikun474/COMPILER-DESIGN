#ifndef TOKEN_CONVERTER_HPP
#define TOKEN_CONVERTER_HPP

#include "token_type.hpp"

/* Maps a TokenType (from the shared vocabulary in shared/include/
 * token_type.hpp -- the same enum phase1-lexer classifies against) to
 * this phase's own Bison-generated token code (from parser.tab.hpp).
 *
 * This is the one piece of the puzzle that genuinely can't be shared
 * with phase1: the return value is only meaningful in the context of
 * *this* grammar's generated token numbering, which doesn't exist
 * until parser.y is compiled. Single-character operators/punctuation
 * (TokenType::PLUS_OP, TokenType::OPEN_BRACE_OP, ...) map to their own
 * ASCII value, exactly the way Bison expects for a quoted-char token
 * like '+' or '{' in the grammar.
 */
int to_bison_token(TokenType t);

#endif
