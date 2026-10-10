/* a variable read on some path before anything was stored in it */
#include <stdio.h>
#include <stdarg.h>

int pick(int which) {
    int x;
    if (which) x = 1;
    return x; /* not assigned when which == 0 */
}

int total(int n, ...) { /* no warning: va_start gives ap its value */
    va_list ap;
    va_start(ap, n);
    int sum = 0;
    for (int i = 0; i < n; i++) sum = sum + va_arg(ap, int);
    va_end(ap);
    return sum;
}

int main() {
    int a;
    int b = a + 1;
    int c;
    c = 5;       /* assigned before it is read */
    int table[4]; /* arrays and objects are not tracked */
    long long wide;
    printf("%d %d %d %d\n", b, c, table[0], pick(1) + total(2, 3, 4));
    return (int) wide;
}
