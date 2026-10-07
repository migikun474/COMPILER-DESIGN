/* t15 -- -O2: constants, copies and dead assignments across basic
   blocks, next to the cases where a value is not the same on every path */
#include <stdio.h>

int g = 0;
int touch() { g++; return g; }

int branches(int c) {
    int x = 5, y;
    if (c) y = x + 1; else y = x + 2;         /* x is 5 on both paths */
    int z = 1;
    if (c) z = 2;                             /* z is 1 or 2 afterwards: not a constant */
    int unused = y * 100;                     /* never read */
    return x + y + z;
}

int loop(int n) {
    int step = 3, sum = 0, last = 0;
    for (int i = 0; i < n; i++) {
        sum += step;                          /* step is 3 on every path into the loop */
        last = i;                             /* read after the loop: must stay */
        int scratch = sum * 2;                /* dead in every iteration */
    }
    int i = 100;                              /* another i, not the loop's */
    return sum + last + i;
}

int rewritten(int a) {
    int b = a;                                /* b is a copy of a ... */
    if (a > 3) a = 0;                         /* ... until a changes on one path */
    int c = b + a;
    a = 7; a = 8;                             /* the first assignment is dead */
    int d = touch();                          /* the call must happen even if d were unused */
    d = touch();
    return c + a + d;
}

int viaPointer() {
    int x = 1, y = 2;
    int *p = &x;
    x = 10;                                   /* not dead: read through p */
    y = 20;                                   /* dead: overwritten before any read */
    y = *p + 1;
    struct { int a; int b; } s;
    s.a = 3; s.b = 4;                         /* s.b is never read */
    return y + s.a;
}

int jumps(int n) {
    int k = 0, t = 9;
again:
    k++;
    if (k < n) goto again;                    /* k changes round the loop */
    switch (n) {
        case 1: t = 1; break;
        case 2: t = 2;
        case 3: t = t + 10; break;            /* t is 2 or 9 here */
    }
    return k * 100 + t;
}

int main() {
    printf("%d %d\n", branches(0), branches(1));
    printf("%d %d %d\n", loop(0), loop(1), loop(4));
    int r1 = rewritten(1), r9 = rewritten(9);   /* separate statements: argument order is unspecified in C */
    printf("%d %d %d\n", r1, r9, g);
    printf("%d\n", viaPointer());
    printf("%d %d %d %d\n", jumps(1), jumps(2), jumps(3), jumps(5));
    return g;
}
