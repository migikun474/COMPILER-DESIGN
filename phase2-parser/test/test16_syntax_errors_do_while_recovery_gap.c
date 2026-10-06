/* test16 -- FIXED; kept as the regression test. A malformed do-while
   now produces exactly one error and parsing continues (here: the
   missing ';' is reported at `return a;`, which is kept in the AST).
   The actual root cause turned out to differ from the sketch below:
   recovery popped back to the state right after `do` and accepted
   `error` there as the loop *body*, then waited for a `while` that
   never came. The fix is two local error alternatives on the do-while
   production (see parser.y and the phase 2 README, "Finding 2").

   Original description:

   a real, reproducible gap in this grammar's panic-mode
   recovery: ANY malformed do-while statement -- a missing 'while'
   keyword, a missing '(' / ')', or (most surprisingly) just the
   ordinary missing trailing ';' that every other statement recovers
   from just fine -- causes yyparse() itself to give up entirely,
   not just the one broken statement. Once that happens, nothing else
   in the file gets parsed: no more diagnostics, no more AST nodes,
   even for code far away and completely unrelated to the do-while.

   Root cause sketch: `iteration_stmt: DO statement WHILE '(' expr ')'
   ';'` is the only loop form whose tail after the body is a long,
   rigid, fixed token sequence with no shorter alternative the grammar
   can fall back to. When one of those tail tokens is missing/wrong,
   Bison's `error` recovery has to pop the parse stack much further
   back than it does for e.g. a missing ')' in an `if` condition --
   apparently far enough that it can no longer find a state, before
   EOF, where either `statement: error ';'` or `statement: error '}'`
   is able to shift. The result is exactly what a "the parser
   quietly gave up" driver bug looks like: yyparse() returns nonzero,
   and the original driver never checked that return value, so the
   rest of the file just silently vanished from the report with
   nothing to explain why.

   This build now checks yyparse()'s return value (see main.cpp) and
   emits a "fatal error: parser could not recover..." diagnostic when
   this happens, so at least the failure is visible instead of a
   silent truncation -- but the underlying recovery gap in the
   do-while production itself is still open. A real fix belongs in
   the grammar (e.g. adding a narrower `error` alternative inside the
   do-while production itself, right after the body statement, so a
   broken tail can be recovered locally instead of unwinding all the
   way out to `statement`).

   Because of that "loses the rest of the file" property, this file
   deliberately contains ONLY the one broken construct -- anything
   placed after it here would never be reached, which would make this
   test misleading about what actually ran. */

int this_function_never_gets_analyzed_because_of_the_bug_above() {
    int a = 1;

    do {
        a = a + 1;
    } while (a < 10)   /* <-- missing ';' */

    return a;
}
