/* t21 -- floating point: float and double arithmetic, conversions,
   comparisons, simple numerical methods */
#include <stdio.h>

double absolute(double v) { return v < 0 ? -v : v; }

double root(double v) {                       /* Newton's method */
    double guess = v / 2;
    for (int i = 0; i < 20; i++) guess = (guess + v / guess) / 2;
    return guess;
}

double series(int terms) {                    /* 4 * (1 - 1/3 + 1/5 - ...) */
    double sum = 0, sign = 1;
    for (int i = 0; i < terms; i++) { sum += sign / (2 * i + 1); sign = -sign; }
    return 4 * sum;
}

double power(double base, int n) { double r = 1; while (n-- > 0) r *= base; return r; }
float average(float a, float b, float c) { return (a + b + c) / 3; }
int roundToInt(double v) { return (int) (v < 0 ? v - 0.5 : v + 0.5); }

double poly(double x) { return ((2 * x - 3) * x + 0.5) * x - 7; }

int main() {
    double d = 10.0 / 4, e = 7 / 2, f = 7 / 2.0;
    float g = 1.0f / 3;
    printf("%.3f %.3f %.3f %.4f\n", d, e, f, g);
    printf("%.5f %.4f %.2f\n", root(2.0), series(1000), power(1.5, 6));
    printf("%.3f %.2f %.2f\n", average(1.5f, 2.5f, 4.0f), absolute(-3.25), poly(2.0));
    printf("%d %d %d %d\n", roundToInt(2.5), roundToInt(-2.5), roundToInt(2.4), (int) 9.99);
    printf("%d %d %d %d\n", 0.1 + 0.2 == 0.3, 0.5 + 0.25 == 0.75, d > e, g < 0.34f);

    int i = 7;
    unsigned int u = 4000000000u;
    char c = 'A';
    double mixed = i / 2 + i / 2.0 + c + u;
    float narrowed = 16777217;                /* not representable in float */
    printf("%.1f %.1f %d\n", mixed, narrowed, (int) (float) 0.999999f);

    double total = 0;
    for (double step = 0.25; step < 2.0; step += 0.25) total += step * step;
    printf("%.4f\n", total);
    float fsum = 0;
    for (int k = 1; k <= 10; k++) fsum += 1.0f / k;
    printf("%.4f %.2f\n", fsum, -fsum * 2);
    double tiny = 1e-3, huge = 2.5e6;
    printf("%.6f %.1f %.3f\n", tiny, huge, huge * tiny);
    return roundToInt(root(81.0));
}
