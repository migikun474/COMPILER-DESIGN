/* invalid pointer operations [test 21] */
struct S { int v; };
int f(int a) { return a; }

int main() {
    int x = 1, *p = &x, **pp = &p;
    char *cp = 0;
    void *vp = p;
    double d = 2.0;
    x = *x;                       // error: indirection requires a pointer operand ('int' is not a pointer)
    x = ***pp;                    // error: indirection requires a pointer operand
    x = *vp;                      // error: cannot dereference a 'void *' pointer
    p = &5;                       // error: cannot take the address of an rvalue of type 'int'
    p = &(x + 1);                 // error: cannot take the address of an rvalue
    p = cp;                       // error: incompatible pointer types
    pp = p;                       // error: cannot assign 'int *' to 'int **'
    p = &pp;                      // error: cannot assign 'int ***' to 'int *'
    vp = vp + 1;                  // error: arithmetic on a pointer to void
    x = p < cp;                   // error: comparison of distinct pointer types
    p = d;                        // error: cannot assign 'double' to 'int *'
    x = cp - p;                   // error: pointers to different types cannot be subtracted
    int (*pa)[3] = &x;            // error: incompatible pointer types
    x = f(*pp);                   // error: argument 1 of 'f' expects 'int' but got 'int *'
    return x;
}
