/* Exercises three related things that a naive declarator grammar can
 * get subtly wrong:
 *   1. genuine multi-level pointers (char **argv), not just single *
 *   2. a function POINTER variable (int (*fp)(int,int)) correctly
 *      classified as a variable, not mistaken for a real function
 *      declaration -- these look structurally identical unless the
 *      grammar tracks *where* the pointer indirection came from
 *   3. a function that legitimately RETURNS a pointer (int *makeInt())
 *      staying correctly classified as a procedure, not accidentally
 *      broken by the fix for (2)
 */

int add(int a, int b) {
    return a + b;
}

int *makeInt() {
    int *p;
    p = new int;
    *p = 42;
    return p;
}

int main(int argc, char **argv) {
    int (*fp)(int, int);
    fp = add;
    int result;
    result = fp(2, 3);

    int *val;
    val = makeInt();

    int x;
    x = argc;

    return 0;
}
