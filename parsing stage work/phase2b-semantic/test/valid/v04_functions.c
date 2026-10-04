/* valid: prototypes, definitions, calls, returns, recursion, forward
   calls [test 11, 16] */
int add(int a, int b);            /* declaration ... */
int add(int a, int b) {           /* ... and a matching definition */
    return a + b;
}
int add(int, int);                /* redeclaring a prototype is fine */

int factorial(int n) {            /* direct recursion */
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int is_even(int n);
int is_odd(int n) { return n == 0 ? 0 : is_even(n - 1); }   /* mutual recursion */
int is_even(int n) { return n == 0 ? 1 : is_odd(n - 1); }

void log_value(int v) {
    if (v < 0) return;            /* bare return in a void function */
    printf("%d\n", v);
}

double average(int a, int b) { return (a + b) / 2.0; }
char first(char *s) { return s[0]; }
int sum(int count, ...) { return count; }   /* variadic */

int main() {
    int r = add(1, 2);
    r = add('a', 2);              /* char argument converts to int */
    double avg = average(3, 4);
    log_value(r);
    r = factorial(5) + is_odd(3) + first("abc");
    r = sum(1) + sum(3, 1, 2.0, "x");
    r = later(r);                 /* defined below: file-scope functions may be called before their definition */
    return r + avg;
}

int later(int v) { return v + 1; }
