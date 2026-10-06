/* test17 -- syntax errors in function definitions: missing return
   type, malformed parameter lists, misuse of variadic '...', and
   mismatched braces spanning a function boundary. One function per
   case, each verified independently. */

void resync_marker() {}

/* [1] no return type at all -- function_definition requires
   declaration_specifiers before the declarator */
missing_return_type() {
    return;
}

/* [2] trailing comma in the parameter list with nothing after it */
int t02_trailing_comma_param(int a, ) {
    return a;
}

/* [3] a parameter with no type at all */
int t03_untyped_param(a, int b) {
    return a + b;
}

/* [4] '...' with no ordinary parameter before it -- the grammar only
   allows ELLIPSIS after a real parameter_list, not on its own */
int t04_ellipsis_with_no_params(...) {
    return 0;
}

/* [5] missing ')' on the parameter list */
int t05_missing_close_paren(int a, int b {
    return a + b;
}

/* [6] missing closing '}' on the function body -- this one is
   deliberately last: the parser has to recover from a genuinely
   unclosed brace right before end of file, one of the hardest cases
   for panic-mode recovery (there is no following token at all to
   resync on). */
int t06_unterminated_body(int a) {
    int b = a + 1;
    return b;
