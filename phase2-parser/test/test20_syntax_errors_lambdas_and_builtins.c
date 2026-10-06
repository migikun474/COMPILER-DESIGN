/* test20 -- syntax errors in lambdas, ternary/casts/goto, and the
   built-in I/O / memory calls (printf, scanf, malloc, ...). One
   broken construct per function, each followed by a resync anchor
   where it matters. */

void resync_marker() {}

/* [1] [boundary -- now VALID] lambda without a parameter list: once a
   syntax error, but as in real C++ the '(' ')' may now be omitted, so
   this file reports 9 errors, not 10 */
void t01_lambda_missing_param_parens() {
    int x = 1;
    int (*f)() = [x] { return x; };
}

/* [2] lambda with a capture list missing its comma */
void t02_lambda_capture_missing_comma() {
    int x = 1;
    int y = 2;
    auto f = [x y](int a) { return a + x + y; };
}

/* [3] ternary expression missing the ':' branch */
void t03_ternary_missing_colon() {
    int a = 1;
    int b = (a > 0) ? 1 ;
}

/* [4] goto with no target label at all */
void t04_goto_missing_label() {
    goto ;
}

/* [5] printf call missing its closing ')' */
void t05_printf_missing_close_paren() {
    printf("hello, %d", 5;
}

/* [6] scanf call with a stray leading comma in the argument list */
void t06_scanf_stray_comma() {
    int x;
    scanf(, &x);
}

/* [7] malloc call missing its argument entirely, with a dangling
   comma left behind */
void t07_malloc_dangling_comma() {
    int *p = malloc(,);
}

/* [8] fprintf missing its closing ')' */
void t08_fprintf_missing_close_paren() {
    fprintf(stdout_placeholder, "x = %d", 3;
}

/* [9] sizeof used with unbalanced parens around the type */
void t09_sizeof_unbalanced_parens() {
    int s = sizeof(int;
}

/* [10] new-expression used where it can't produce a valid statement
   (missing the type entirely) */
void t10_new_missing_type() {
    int *p = new;
}

/* a fully valid function proving the parser recovered after all ten
   broken constructs above -- exercises the same features correctly */
int main() {
    int x = 10, y = 20;
    auto adder = [x, &y](int a) { return a + x + y; };
    int cond = (x > y) ? x : y;

    printf("cond=%d\n", cond);
    scanf("%d", &x);

    int *p = (int *)malloc(sizeof(int) * 4);
    free(p);

    goto done;
done:
    return 0;
}
