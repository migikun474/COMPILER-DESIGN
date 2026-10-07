/* t01 -- arithmetic, conversions, bitwise, shifts, compound assignment,
   increment/decrement, comma, ternary, sizeof, casts */
#include <stdio.h>

int main() {
    int a = 7, b = 3, c;
    c = a + b * 2 - a / b + a % b;
    printf("%d %d %d %d %d\n", c, a - b, a * b, a / b, a % b);
    c = b * -a + b * -a;                 /* the slides' example */
    printf("%d\n", c);

    double d = 1.5;
    float f = 2.5f;
    d = d + a * 2;                       /* int -> double */
    f = f * b;                           /* int -> float */
    int truncated = d / 2;               /* double -> int */
    printf("%.2f %.2f %d\n", d, f, truncated);

    unsigned int u = 7;
    u = u / 3 + (u << 2) + (u >> 1);
    int neg = -16;
    printf("%u %d %d %d\n", u, neg >> 2, neg / 3, neg % 3);
    printf("%d %d %d %d\n", a & b, a | b, a ^ b, ~a);

    char ch = 'A';
    ch = ch + 2;
    short s = 300;
    s = s * 2;
    long long big = 100000;
    big = big * big + a;
    printf("%c %d %d %lld\n", ch, ch, s, big);

    a += 5; b -= 1; c *= 2; a /= 3; b <<= 3; c %= 7; a |= 8; b &= 12; c ^= 5; d -= 0.5; d *= 2;
    printf("%d %d %d %.1f\n", a, b, c, d);

    int i = 5, j;
    j = i++ + 1;
    printf("%d %d\n", i, j);
    j = ++i * 2;
    printf("%d %d\n", i, j);
    j = i-- - --i;
    i = (j = 3, j + 4);
    printf("%d %d\n", i, j);

    int big2 = a > b ? a : b;
    double mixed = a > 100 ? 1 : 2.5;    /* int and double branches */
    printf("%d %.1f\n", big2, mixed);
    printf("%d %d %d\n", (int) sizeof(int), (int) sizeof(double), (int) sizeof(char));
    printf("%d %.3f %d\n", (int) 3.99, (double) a / 4, (char) 321);
    unsigned char wraps = 250;
    wraps = wraps + 10;
    printf("%d\n", wraps);
    return (a + b) % 256;
}
