/* t03 -- boolean expressions: short circuit, comparisons as values, ! */
#include <stdio.h>

int calls = 0;
int yes() { calls++; return 1; }
int no() { calls++; return 0; }

int main() {
    int a = 1, b = 2, c = 3, d = 4, e = 5, f = 6;
    int r = a < b || c < d && e < f;     /* the slides' example */
    printf("%d\n", r);
    r = a > b;
    printf("%d %d %d %d %d %d\n", r, a < b, a == 1, a != 1, b >= 2, b <= 1);

    calls = 0;
    if (no() && yes()) printf("no\n");
    printf("calls after &&: %d\n", calls);
    calls = 0;
    if (yes() || no()) printf("or taken\n");
    printf("calls after ||: %d\n", calls);
    calls = 0;
    r = (no() || yes()) && !no();
    printf("%d %d\n", r, calls);

    int x = 0;
    double z = 0.5;
    char ch = 0;
    int *p = 0;
    printf("%d %d %d %d %d\n", !x, !z, !ch, !p, !!c);
    if (z) printf("double is true\n");
    if (!p) printf("null pointer is false\n");
    r = (a < b) + (b < c) + (c < a);
    printf("%d\n", r);
    r = a && b;
    printf("%d %d\n", r, x || ch);
    bool flag = c > a;
    bool both = flag && d;
    printf("%d %d\n", flag, both);
    while (x < 3 && !(x == 2)) x++;
    printf("%d\n", x);
    unsigned int big = 4000000000u;
    int minus = -1;
    printf("%d %d\n", big > 5u, minus < 0);
    return r;
}
