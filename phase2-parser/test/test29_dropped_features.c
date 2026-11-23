/* test29 -- the features dropped before the back end was built: file
   manipulation, lambdas, function pointers (enum and union were dropped
   too, and came back with D42), and new/delete/register/volatile, dropped
   later. Their keywords are no longer reserved and their grammar rules
   are gone, so each construct below is an ordinary syntax error. One per
   top-level declaration or function, each followed by a resync anchor
   (11 errors for 11 constructs).

   (File I/O leaves no syntax behind: `FILE *f = fopen("a", "r");` now
   reads as the expression `FILE * f = fopen(...)` over undeclared names,
   which semantic analysis reports -- see
   phase2b-semantic/test/invalid/e19_dropped_features.c.) */

void resync_marker() {}

/* [1] a lambda with a capture list */
void t01_lambda() {
    int x = 1;
    auto add = [x](int a) { return a + x; };
    resync_marker();
}

/* [2] a lambda with a capture-default */
void t02_lambda_capture_default() {
    int x = 1;
    auto get = [&]() { return x; };
    resync_marker();
}

/* [3] a function-pointer variable */
void t03_function_pointer_variable() {
    int (*fp)(int, int);
    resync_marker();
}

/* [4] a function-pointer parameter */
int t04_function_pointer_parameter(int (*op)(int), int v) { return v; }

/* [5] a typedef of a function-pointer type */
typedef int (*T05_BinOp)(int, int);

/* [6] a cast to a function-pointer type */
void t06_function_pointer_cast() {
    int x = 0;
    x = (int (*)(int)) x;
    resync_marker();
}

/* [7] an array of function pointers */
void t07_function_pointer_array() {
    int (*table[2])(int, int);
    resync_marker();
}

/* The second batch (dropped after the back end was complete): `new`,
   `delete`, `register` and `volatile` are ordinary identifiers too, so
   each of [8]-[11] is one more syntax error. Dynamic memory is
   malloc / calloc / realloc / free. */

/* [8] a new-expression */
void t08_new() {
    int *p = new int;
    resync_marker();
}

/* [9] a delete-expression */
void t09_delete() {
    int *p = 0;
    delete p;
    resync_marker();
}

/* [10] the register storage class */
void t10_register() {
    register int fast = 1;
    resync_marker();
}

/* [11] the volatile qualifier */
void t11_volatile() {
    volatile int sensor = 1;
    resync_marker();
}

/* a fully valid function proving the parser recovered after every
   dropped construct above -- the features that stay still work */
int twice(int v) { return v * 2; }
int main() {
    int nums[3] = {1, 2, 3};
    int (*row)[3] = &nums;        /* a parenthesized declarator that is not a function pointer */
    auto total = twice((*row)[0]) + nums[2];
    return total;
}
