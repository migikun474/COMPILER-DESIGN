/* t16 -- what the MIPS run-time library has to get right: 64-bit
   arithmetic, conversions between integers and floating point, printf
   formats, structs and doubles passed and returned on the stack */
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

struct Big { double d; int n[5]; char tag; long long w; };

struct Big make(int k) {
    struct Big b;
    b.d = k * 1.5;
    for (int i = 0; i < 5; i++) b.n[i] = k + i;
    b.tag = 'A' + k;
    b.w = 10000000000LL * k;
    return b;
}

double weigh(struct Big b, double scale, char c, long long extra) {
    return b.d * scale + b.n[4] + c + (double) (b.w / 1000000000LL) + extra;
}

double average(int count, ...) {
    va_list ap;
    va_start(ap, count);
    double total = 0;
    for (int i = 0; i < count; i++) total += va_arg(ap, double);
    long long tail = va_arg(ap, long long);
    char *label = va_arg(ap, char *);
    va_end(ap);
    printf("%s %lld\n", label, tail);
    return total / count;
}

long long power(long long base, int n) { return n == 0 ? 1 : base * power(base, n - 1); }

int main() {
    long long a = 123456789012345LL, b = -987654321LL;
    unsigned long long u = 18000000000000000000ULL;
    printf("%lld %lld %lld\n", a + b, a - b, a * 3);
    printf("%lld %lld %lld %lld\n", a / 1000, a % 1000, a / b, a % b);
    printf("%lld %lld\n", b / 7, b % 7);
    printf("%llu %llu %llu\n", u / 10, u % 1000, u >> 3);
    printf("%lld %lld %lld %lld\n", a << 5, a >> 7, b >> 4, (long long) 1 << 40);
    printf("%d %d %d %d\n", a > b, b < 0, a == a, u > (unsigned long long) a);
    printf("%lld %llx\n", power(3, 30), u);
    printf("%lld %lld\n", -a, ~a);

    int i = -7;
    unsigned int big = 3000000000u;
    double d = i, e = big, f = a;
    float fl = (float) big;
    printf("%.1f %.1f %.1f %.1f\n", d, e, f, fl);
    printf("%d %u %lld %d\n", (int) 3.99, (unsigned int) 3000000000.5, (long long) 12345678901.7, (int) -2.5);
    printf("%lld %d %d\n", (long long) -5000000000.0, (char) 200, (short) 70000);
    float x = 1.5f, y = 2.25f;
    printf("%.2f %.2f %.2f %.2f %d\n", x + y, x * y, x / y, -x, x < y);

    printf("[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%f]\n", 3.14159, -2.5, 7.125, 2.5, 0.1);
    printf("[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%5s] [%-5s] [%c] [%%]\n", -42, 42, -42, 255, 255, 8, "ab", "cd", 'z');
    printf("[%*d] [%.*f] [%3s]\n", 6, 12, 2, 1.23456, "long string");

    struct Big s = make(2);
    struct Big t = s;
    t.n[4] = 100;
    printf("%.1f %d %d %c %lld\n", s.d, s.n[4], t.n[4], s.tag, s.w);
    printf("%.1f\n", weigh(s, 2.0, 'a', 5));
    printf("%.2f\n", average(3, 1.0, 2.5, 4.0, 77LL, "tail"));

    int *p = (int *) malloc(3 * sizeof(int));
    p[0] = 1; p[1] = 2; p[2] = 3;
    p = (int *) realloc(p, 6 * sizeof(int));
    int *z = (int *) calloc(4, sizeof(int));
    printf("%d %d %d %d\n", p[0] + p[1] + p[2], z[0], z[3], p != z);
    return (int) (a % 100);
}
