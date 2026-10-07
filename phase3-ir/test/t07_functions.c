/* t07 -- functions: recursion, overloading, references, varargs,
   static locals, globals, forward calls */
#include <stdio.h>
#include <stdarg.h>

int later(int n);                        /* defined after its first call */

int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
int fib(int n) { if (n < 2) return n; return fib(n - 1) + fib(n - 2); }
int gcd(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

int pick(int a) { return 1; }
int pick(double a) { return 2; }
int pick(char *s) { return 3; }
int pick(int a, int b) { return 4; }

void bump(int &r) { r = r + 1; }
void exchange(int &a, int &b) { int t = a; a = b; b = t; }
int &largest(int &a, int &b) { if (a > b) return a; return b; }
double half(const double &v) { return v / 2; }

int sum(int n, ...) {
    va_list ap;
    va_start(ap, n);
    int s = 0;
    for (int i = 0; i < n; i++) s += va_arg(ap, int);
    va_end(ap);
    return s;
}

double mix(int n, ...) {
    va_list ap;
    va_start(ap, n);
    double s = va_arg(ap, double) + va_arg(ap, int);
    va_end(ap);
    return s;
}

int counter() {
    static int calls = 0;
    calls++;
    return calls;
}

int global = 10;
double ratio = 2.5;
void scale(int k) { global = global * k; }

int main() {
    printf("%d %d %d %d\n", fact(6), fib(10), gcd(84, 36), later(4));
    char text[4] = "abc";
    printf("%d %d %d %d %d\n", pick(1), pick(2.5), pick(text), pick(1, 2), pick('c'));

    int x = 5, y = 9;
    bump(x);
    exchange(x, y);
    int &alias = x;
    alias = alias + 100;
    largest(x, y) = 0;
    printf("%d %d %.2f\n", x, y, half(5));

    printf("%d %d %.1f\n", sum(3, 10, 20, 30), sum(0), mix(2, 1.5, 4));
    counter(); counter();
    printf("%d\n", counter());
    scale(3);
    printf("%d %.1f\n", global, ratio * global);
    return later(1);
}

int later(int n) { return n * 11; }
