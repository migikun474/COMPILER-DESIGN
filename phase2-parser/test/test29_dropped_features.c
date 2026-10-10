/* test29 -- the four features dropped before the back end was built:
   enum and union, file manipulation, lambdas, function pointers. Their
   keywords are no longer reserved and their grammar rules are gone, so
   each construct below is an ordinary syntax error. One per top-level
   declaration or function, each followed by a resync anchor (17 errors
   for 15 constructs: [2] and [4] are each reported twice, at the start
   of the construct and again inside its body).

   (File I/O leaves no syntax behind: `FILE *f = fopen("a", "r");` now
   reads as the expression `FILE * f = fopen(...)` over undeclared names,
   which semantic analysis reports -- see
   phase2b-semantic/test/invalid/e19_dropped_features.c.) */

void resync_marker() {}

/* [1] an enum definition */
enum T01_Color { RED, GREEN, BLUE };
int resync_after_1;

/* [2] a union definition */
union T02_Number { int i; float f; };
int resync_after_2;

/* [3] a variable of an enum type */
void t03_enum_variable() {
    enum T01_Color c;
    resync_marker();
}

/* [4] an unnamed union object */
void t04_unnamed_union() {
    union { int word; char bytes[4]; } u;
    resync_marker();
}

/* [5] a lambda with a capture list */
void t05_lambda() {
    int x = 1;
    auto add = [x](int a) { return a + x; };
    resync_marker();
}

/* [6] a lambda with a capture-default */
void t06_lambda_capture_default() {
    int x = 1;
    auto get = [&]() { return x; };
    resync_marker();
}

/* [7] a function-pointer variable */
void t07_function_pointer_variable() {
    int (*fp)(int, int);
    resync_marker();
}

/* [8] a function-pointer parameter */
int t08_function_pointer_parameter(int (*op)(int), int v) { return v; }

/* [9] a typedef of a function-pointer type */
typedef int (*T09_BinOp)(int, int);

/* [10] a cast to a function-pointer type */
void t10_function_pointer_cast() {
    int x = 0;
    x = (int (*)(int)) x;
    resync_marker();
}

/* [11] an array of function pointers */
void t11_function_pointer_array() {
    int (*table[2])(int, int);
    resync_marker();
}

/* The second batch (dropped after the back end was complete): `new`,
   `delete`, `register` and `volatile` are ordinary identifiers too, so
   each of [12]-[15] is one more syntax error. Dynamic memory is
   malloc / calloc / realloc / free. */

/* [12] a new-expression */
void t12_new() {
    int *p = new int;
    resync_marker();
}

/* [13] a delete-expression */
void t13_delete() {
    int *p = 0;
    delete p;
    resync_marker();
}

/* [14] the register storage class */
void t14_register() {
    register int fast = 1;
    resync_marker();
}

/* [15] the volatile qualifier */
void t15_volatile() {
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
