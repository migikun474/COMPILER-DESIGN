/* invalid builtins (printf/scanf/memory), references */
int global_value = 1;

int main() {
    int x = 1, y = 2;
    double d = 0;
    const char *ro = "abc";
    int r = global_value;
    scanf("%d", x);               // error: argument 2 of 'scanf' must be a pointer
    scanf("%d %s", &d, ro);       // error: argument 3 of 'scanf' points to read-only storage  // warning: format '%d' expects 'int *', but argument 2 has type 'double *'
    printf(5);                    // error: argument 1 of 'printf' expects 'const char *' but got 'int'
    free(x);                      // error: argument 1 of 'free' expects 'void *' but got 'int'
    int *m = malloc("big");       // error: argument 1 of 'malloc' expects 'int' but got 'char *'
    int *z = calloc(4);           // error: function 'calloc' expects 2 arguments but 1 was provided
    int &ref = 5;                 // error: non-const reference of type 'int &' cannot bind to a temporary of type 'int'
    char &cref = x;               // error: cannot bind to an lvalue of type 'int'
    return r + y;
}
