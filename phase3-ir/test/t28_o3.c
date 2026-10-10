/* t28 -- -O3: inlining, tail recursion, expressions shared across
   blocks, code moved out of loops, stored values reused -- next to the
   cases where each of them would be wrong */
#include <stdio.h>

int calls = 0;
int square(int v) { return v * v; }                    /* inlined */
int clamp(int v, int lo, int hi) { if (v < lo) return lo; if (v > hi) return hi; return v; }   /* several returns */
int counted(int v) { calls++; return v + calls; }      /* a side effect that must happen every time */
void bump(int &r, int by) { r += by; }                 /* a reference parameter */
struct Pair { int a; int b; };
int total(struct Pair p) { p.a += 1; return p.a + p.b; }   /* a by-value struct: the caller's copy is unchanged */
int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }   /* recursive: not inlined, not a tail call */

int gcd(int a, int b) { if (b == 0) return a; return gcd(b, a % b); }            /* tail call, arguments swapped */
int sumTo(int n, int acc) { if (n == 0) return acc; return sumTo(n - 1, acc + n); }
int countDown(int n) { if (n <= 0) return 0; return countDown(n - 2); }

int invariant(int n, int k) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        int scale = k * 3 + 1;                         /* the same on every round */
        s += i * scale;
        if (i == 2) continue;
        s += k * 3;                                    /* k * 3 again */
    }
    return s;
}

int notInvariant(int n) {
    int s = 0, k = 1;
    for (int i = 0; i < n; i++) {
        int v = k * 3;                                 /* k changes below: must stay in the loop */
        s += v;
        k = k + i;
    }
    return s;
}

int zeroTrips(int n, int d) {
    int s = 7;
    while (n > 0) { s += 100 / d; n--; }               /* a division is never moved: d may be 0 when n is 0 */
    return s;
}

int nested(int rows, int cols) {
    int grid[4][5], s = 0;
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) grid[r][c] = r * cols + c;     /* r * cols does not change in the inner loop */
    for (int r = 0; r < rows; r++)
        for (int c = 0; c < cols; c++) s += grid[r][c];
    return s;
}

int shared(int x, int y, int flag) {
    int a = x * y + 2, b;
    if (flag) b = x * y + 2;                           /* available from above */
    else { x = x + 1; b = x * y + 2; }                 /* x changed: computed again */
    return a * 1000 + b + x * y;                       /* x * y differs per path here */
}

int memory(int i) {
    int arr[4] = {1, 2, 3, 4};
    int *p = &arr[1], *q = arr;
    arr[i] = 10;
    int a = arr[i];                                    /* the value just stored */
    *p = 20;                                           /* may be the same element */
    int b = arr[i];
    q[i] = 30;
    int c = arr[i] + *p;
    return a + b + c;
}

int main() {
    int x = 5;
    bump(x, square(3));
    struct Pair p = {1, 2};
    int t = total(p) + total(p);
    printf("%d %d %d %d %d\n", x, t, p.a, clamp(-5, 0, 9), clamp(50, 0, 9) + clamp(4, 0, 9));
    int c1 = counted(1), c2 = counted(1), c3 = counted(1);
    printf("%d %d %d %d %d\n", c1, c2, c3, calls, fact(6));
    printf("%d %d %d %d\n", gcd(1071, 462), gcd(17, 5), sumTo(100, 0), countDown(9));
    printf("%d %d %d %d\n", invariant(5, 2), invariant(0, 9), notInvariant(5), zeroTrips(0, 0));
    printf("%d %d %d\n", zeroTrips(3, 4), nested(4, 5), nested(2, 3));
    printf("%d %d\n", shared(3, 4, 1), shared(3, 4, 0));
    printf("%d %d\n", memory(1), memory(2));
    return calls;
}
