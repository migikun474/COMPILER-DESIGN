#ifndef SCANNER_SUPPORT_H
#define SCANNER_SUPPORT_H

/* State and lookahead the scanner needs beyond the scoped type-name
   table (symbol_table): where a typedef'd name must be read as a fresh
   declarator name, bracket nesting, and three decisions that need more
   than one token of lookahead, made by peeking at the source text. */

/* set by the declaration-specifier rules once a type keyword (`int`,
   `char`, ...) has been seen: a declaration then cannot take *another*
   type, so a typedef'd name right after it -- `int T;`, `char *T;` --
   is being redeclared, and the scanner returns it as IDENTIFIER. Any
   token other than '*', '&', '(' or const clears it. */
extern bool g_afterTypeKeyword;

/* `int a, T;`: while the init-declarators of a declaration are being
   read, a typedef'd name right after a ',' at the declaration's own
   bracket depth is another declarator, so the scanner returns it as
   IDENTIFIER. The parser marks the list (markDeclaratorList, called as
   each init-declarator is reduced -- i.e. on seeing the ',') and ends it
   at the declaration's ';'. */
void markDeclaratorList();
void endDeclaratorList();
bool inDeclaratorListAt(int bracketDepth);
extern int g_bracketDepth; /* ( [ { nesting, maintained by the scanner */

/* Bounded lookahead over the source text (g_sourceLines), used by the
   scanner for decisions LALR(1) cannot make from one token. Lines
   and columns are 1-based; (line, column) is where to start looking.
     parenGroupIsExpression: at `T (...)` with T a type -- true when the
       parenthesized part cannot be a declarator, so `T(...)` must be an
       expression (`Dog(4)`, `Dog()`, `Dog(a).x`, `int(x) + 1`). */
bool parenGroupIsExpression(int line, int column);
/*   abstractDeclaratorGroup: at the inside of a `(` that follows a type
       -- true when the group holds only `*`, `&`, `const`,
       `[n]` and nested parentheses, i.e. `(*)`, `(**)`, `(&)`: a nameless
       declarator (`sizeof(int (*)[3])`), never a functional cast. */
bool abstractDeclaratorGroup(int line, int column);

#endif
