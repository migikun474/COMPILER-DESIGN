/* invalid lambdas, builtins (printf/scanf/memory/files), enums, references */
int global_value = 1;
enum Mode { OFF, ON = global_value };   // error: value of enumerator 'ON' is not an integer constant expression
enum Color { RED, GREEN };
int RED = 3;                      // error: redefinition of 'RED'

int main() {
    int x = 1, y = 2;
    double d = 0;
    char buf[8];
    const char *ro = "abc";
    auto noCap = []() { return x; };              // error: variable 'x' cannot be used in the lambda: it is not captured
    auto byCopy = [x]() { x = 5; return x; };      // error: captured by copy in a non-mutable lambda
    auto glob = [global_value]() { return 0; };   // error: 'global_value' cannot be captured because it does not have automatic storage duration
    auto twice = [x, x]() { return 0; };          // error: 'x' can appear only once in a capture list
    auto mixed = [](int a) { if (a) return 1; return "one"; };   // error: must match the previous return type 'int'
    int r = noCap(1);             // error: function 'noCap' expects 0 arguments but 1 was provided
    scanf("%d", x);               // error: argument 2 of 'scanf' must be a pointer
    scanf("%d %s", &d, ro);       // error: argument 3 of 'scanf' points to read-only storage  // warning: format '%d' expects 'int *', but argument 2 has type 'double *'
    printf(5);                    // error: argument 1 of 'printf' expects 'const char *' but got 'int'
    free(x);                      // error: argument 1 of 'free' expects 'void *' but got 'int'
    int *m = malloc("big");       // error: argument 1 of 'malloc' expects 'int' but got 'char *'
    fclose(buf);                  // error: argument 1 of 'fclose' expects 'FILE *' but got 'char *'
    FILE *f = fopen("a.txt");     // error: function 'fopen' expects 2 arguments but 1 was provided
    int &ref = 5;                 // error: non-const reference of type 'int &' cannot bind to a temporary of type 'int'
    char &cref = x;               // error: cannot bind to an lvalue of type 'int'
    enum Color c = GREEN;
    c = 1;                        /* C: an enum accepts an int */
    return r + y + c;
}
