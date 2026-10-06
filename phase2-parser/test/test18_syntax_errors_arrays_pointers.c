/* test18 -- syntax errors involving arrays, pointers, multi-level
   pointers and function pointers. One broken construct per function. */

void resync_marker() {}

/* [1] array declarator missing the closing ']' */
void t01_array_decl_missing_close_bracket() {
    int arr[5;
    resync_marker();
}

/* [2] multi-dimensional array missing the second ']' */
void t02_multidim_array_missing_bracket() {
    int m[2][3;
    resync_marker();
}

/* [3] array subscript expression missing the closing ']' */
void t03_array_access_missing_close_bracket() {
    int arr[5];
    arr[2 = 9;
}

/* [4] address-of with a missing operand */
void t04_addressof_missing_operand() {
    int x = 1;
    int *p = &;
}

/* [5] dereference assignment with a missing right-hand side */
void t05_deref_missing_rhs() {
    int x = 1;
    int *p = &x;
    *p = ;
}

/* [6] function-pointer declarator with a missing ')' on the inner
   parenthesized declarator */
void t06_function_pointer_missing_close_paren() {
    int (*fp(int, int);
    resync_marker();
}

/* [7] function-pointer declarator missing the ')' on the parameter
   list itself */
void t07_function_pointer_params_missing_close_paren() {
    int (*fp)(int a, int b;
    resync_marker();
}

/* [8] pointer chain with a stray extra '*' in a place that can't be a
   declarator at all (used as a statement) */
void t08_stray_pointer_star_in_statement() {
    int x = 1;
    * = x;
}

/* [9] cast expression with an incomplete/missing type name */
void t09_cast_missing_type_name() {
    int x = 5;
    int y = (int
    x;
}

/* [10] sizeof with an empty parameter list */
void t10_sizeof_missing_type() {
    int s = sizeof();
}

/* a fully valid function proving the parser recovered after all ten
   broken constructs above */
int main() {
    int arr[3] = {1, 2, 3};
    int *p = &arr[0];
    int **pp = &p;
    return **pp;
}
