/* t29 -- what register allocation must not break: values that live
   across calls and recursion, more live values than registers,
   arguments computed before a call, char / short / bool and float /
   double kept in registers, loops built from goto */
#include <stdio.h>

int depth(int n) {                               /* every level has its own a, b, c in the same registers */
    int a = n * 2, b = n + 7, c = a - b;
    if (n == 0) return 1;
    int below = depth(n - 1);
    return a + b + c + below;
}

int many(int x) {                                /* more than eight values alive at once */
    int a = x + 1, b = x + 2, c = x + 3, d = x + 4, e = x + 5, f = x + 6;
    int g = x + 7, h = x + 8, i = x + 9, j = x + 10, k = x + 11, l = x + 12;
    int s = 0;
    for (int t = 0; t < 3; t++) s += a * b + c * d + e * f + g * h + i * j + k * l + t;
    return s + a + b + c + d + e + f + g + h + i + j + k + l;
}

int three(int p, int q, int r) { return p * 100 + q * 10 + r; }
int twice(int v) { return v * 2; }
int arguments(int a, int b, int c) {
    int x = a + 1;
    int y = three(x, twice(b), c - 1);           /* x is read when three is called, after twice ran */
    int z = three(twice(a), twice(twice(b)), twice(c) + x);
    return y + z;
}

int characters(const char *s) {
    char c = 0;
    unsigned char u = 0;
    short h = 0;
    bool any = false;
    int signs = 0;
    for (int i = 0; s[i]; i++) {
        c = c + s[i];                            /* wraps as a signed char */
        u = u + s[i];                            /* wraps as an unsigned char */
        h = h * 31 + s[i];                       /* wraps as a short */
        if (c < 0) signs++;
        any = any || s[i] == 'z';
    }
    unsigned char same = c;                      /* the same bits, read unsigned */
    return c + u * 2 + h + signs * 1000 + any + same;
}

double half(double v) { return v / 2; }
double numbers(int n) {
    double a = 1.5, b = 2.5, c = 0.25, d = 4.0, e = 0.125, f = 8.0, g = 16.5, total = 0;
    float small = 0.5f;
    for (int i = 0; i < n; i++) {
        total += a * b + c * d + e * f + g;      /* seven doubles in use: more than there are registers */
        total = half(total) + small;             /* a call in the middle */
        small = small * 1.5f;
        if (total > 1000) break;
    }
    return total + a + g + small;
}

int jumps(int n) {                               /* a loop made of goto: the values must survive the jump back */
    int i = 0, s = 0, last = -1;
top:
    if (i >= n) goto done;
    s += i * i;
    last = i;
    i++;
    goto top;
done:
    return s * 10 + last;
}

int mixed(int n) {
    int before = n * 3, sum = 0;
    for (int i = 0; i < n; i++) {
        int inside = i * before;
        sum += inside % 7;
        if (sum > 50) { sum -= before; continue; }
        sum += twice(i);
    }
    int after = sum + before;
    return after;
}

int main() {
    printf("%d %d\n", depth(5), many(3));
    printf("%d %d\n", arguments(1, 2, 3), arguments(4, 0, 9));
    printf("%d %d\n", characters("register allocation"), characters("zzzzzzzzzzzzzzzzzzzz"));
    printf("%.4f %.4f %.4f\n", numbers(0), numbers(3), numbers(40));
    printf("%d %d %d\n", jumps(0), jumps(5), mixed(9));
    return jumps(3) % 100;
}
