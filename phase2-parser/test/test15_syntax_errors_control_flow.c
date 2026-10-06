/* test15 -- syntax errors across if/else, while, until, for (both
   header forms) and switch/case. Each broken construct gets its own
   function so recovery from one never has to reach across into the
   next.

   NOTE on scope: do-while's error recovery has a separate, more
   serious problem -- ANY malformed do-while (missing 'while', missing
   parens, missing the trailing ';') makes the whole parser give up
   entirely (yyparse() returns nonzero) and lose the rest of the file,
   not just that one statement. That's real and reproducible, but it
   doesn't compose with anything else in a shared file since nothing
   after it would ever be analyzed -- see
   test16_syntax_errors_do_while_recovery_gap.c (since FIXED: a broken
   do-while now recovers locally; test16 is the regression test).

   NOTE on scope, second: this grammar performs no semantic checks and
   no extra syntax-shape checks beyond what its productions accept --
   `break`/`continue`/`case`/`default` are matched purely structurally
   (BREAK ';' , CONTINUE ';' , CASE constant_expr ':' statement,
   DEFAULT ':' statement), with no check anywhere for whether an
   enclosing loop or switch actually exists. So `break;` outside any
   loop, `continue;` outside any loop, and `case`/`default` outside any
   switch are all VALID by this grammar's own rules -- not errors.
   Cases [9]-[12] below are marked [boundary] to document that
   precisely, rather than leaving it untested. */

void resync_marker() {}

/* [1] if with missing ')' before the body */
void t01_if_missing_close_paren() {
    int a = 1;
    if (a > 0 {
        a = a + 1;
    }
}

/* [2] if with missing '(' around the condition */
void t02_if_missing_open_paren() {
    int a = 1;
    if a > 0) {
        a = a + 1;
    }
}

/* [3] while missing ')' */
void t03_while_missing_close_paren() {
    int a = 1;
    while (a > 0 {
        a = a - 1;
    }
}

/* [4] until missing ')' */
void t04_until_missing_close_paren() {
    int a = 1;
    until (a > 100 {
        a = a + 1;
    }
}

/* [5] for-header (three-clause form) missing the first ';' */
void t05_for_missing_first_semicolon() {
    int a;
    for (a = 0 a < 10; a++) {
        resync_marker();
    }
}

/* [6] for-header (declaring form) missing the middle ';' */
void t06_for_decl_missing_second_semicolon() {
    for (int i = 0 i < 10; i++) {
        resync_marker();
    }
}

/* [7] switch missing ')' around the controlling expression */
void t07_switch_missing_close_paren() {
    int a = 1;
    switch (a {
        case 1: break;
    }
}

/* [8] case label missing its ':' */
void t08_case_missing_colon() {
    int a = 1;
    switch (a) {
        case 1 a = 2; break;
    }
}

/* [boundary] break used outside any loop or switch -- accepted, see
   the file header note */
void t09_break_outside_loop_is_accepted() {
    int a = 1;
    if (a > 0) {
        break;
    }
}

/* [boundary] continue used outside any loop -- accepted */
void t10_continue_outside_loop_is_accepted() {
    {
        continue;
    }
}

/* [boundary] case label with no enclosing switch -- accepted */
void t11_case_outside_switch_is_accepted() {
    int a = 1;
    case 5: a = a + 1;
}

/* [boundary] default label with no enclosing switch -- accepted */
void t12_default_outside_switch_is_accepted() {
    int a = 1;
    default: a = a - 1;
}

/* a fully valid function at the very end -- proves the parser is back
   on its feet after all eight broken constructs above */
int main() {
    int total = 0;
    for (int i = 0; i < 10; i++) {
        total += i;
    }
    return total;
}
