/* t14 -- code the optimizer must improve without changing its meaning:
   constants, common subexpressions and copies, next to the cases where
   reusing a value would be wrong (pointers, globals, calls) */
#include <stdio.h>

int g = 1;
int bump() { g = g + 10; return g; }
void set(int *p, int v) { *p = v; }
void twice(int &r) { r = r * 2; }

int fold() {
    int a = 3 + 4 * 2, b = (a << 1) - 6, c = b / 4 % 3;       /* all constants */
    double d = 1.5 * 2 + a;
    unsigned u = 4000000000u + 500000000u;                    /* wraps */
    char ch = 'a' + 300;                                      /* wraps */
    if (0) a = 99;                                            /* never runs */
    if (1) b = b + 1;
    while (0) c = 99;
    return a + b + c + (int) d + (int) (u % 1000) + ch;
}

int common(int x, int y) {
    int a = x * y + 3, b = x * y + 3;                         /* the same expression twice */
    int c = (x + y) * (x + y), d = y + x;                     /* x + y and y + x */
    int e = x * 8 + y * 1 + 0 + x / 1 - 0;                    /* shifts and identities */
    x = x + 1;
    int f = x * y + 3;                                        /* not the same: x changed */
    return a + b + c + d + e + f;
}

int aliasing() {
    int x = 5, y = 7;
    int *p = &x;
    int a = x + y;
    *p = 20;                                                  /* x changed through p */
    int b = x + y;
    set(&y, 1);                                               /* y changed by a call */
    int c = x + y;
    int &r = x;
    r = r + 1;                                                /* x changed through r */
    int d = x + y;
    twice(x);
    int arr[3] = {1, 2, 3};
    int i = 1;
    int e = arr[i] + arr[i];
    arr[i] = 9;                                               /* the element changed */
    int f = arr[i] + arr[1];
    int *q = arr;
    q[2] = 4;
    return a + b * 2 + c * 3 + d * 5 + e + f + x + arr[2];
}

int globals() {
    int a = g + 1;
    int b = g + 1;                                            /* same value: nothing between */
    bump();                                                   /* g changed by the call */
    int c = g + 1;
    g = 2;
    int d = g + 1;
    int v = 3;
    int e = v + v;
    return a + b + c + d + e + bump();
}

int flow(int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        int k = n * 2;                                        /* the same every time round */
        if (i % 2 == 0) s += k; else s -= 1;
        if (s > 1000) return -1;
    }
    switch (n) {
        case 3: s += 1;
        case 4: s += 2; break;
        default: s = 0;
    }
    return s;
    s = 12345;                                                /* unreachable */
    return s;
}

int divide(int a, int b) { return b == 0 ? 0 : a / b; }       /* 1 / 0 must not be folded away */

int main() {
    printf("%d\n", fold());
    printf("%d\n", common(3, 4));
    printf("%d\n", aliasing());
    int total = globals();
    printf("%d %d\n", total, g);
    printf("%d %d %d\n", flow(3), flow(4), flow(5));
    int zero = 0;
    printf("%d %d\n", divide(1, zero), divide(9, 3));
    double x = 0.0, y = -x;
    printf("%.1f %.1f\n", y + 0.0, x * 1.0);                  /* no float identities applied wrongly */
    return 0;
}
