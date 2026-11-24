/* t43 -- floating point: double and float to int truncate toward zero
   (also negative), int to double and back, float precision, rounding in
   printf, comparisons between int and double, unsigned to double.
   Expected: g++. */
int main() {
    double d = -3.99, e = 3.99;
    float f = 2.5f;
    printf("%d %d %d %d\n", (int)d, (int)e, (int)-0.5, (int)f);
    int i = 7;
    double h = i / 2, q = i / 2.0;
    printf("%.1f %.1f %.3f\n", h, q, 1.0 / 3);
    float third = 1.0f / 3.0f;
    printf("%.6f %.2f %.0f %.0f\n", third, 2.675, 0.5, 1.5);
    printf("%d %d %d\n", i < 7.5, i == 7.0, 3 > 2.9999);
    unsigned u = 4000000000u;
    double ud = u;
    printf("%.0f %u\n", ud, (unsigned)(ud / 2));
    double big = 1e9;
    int back = (int)(big * 2 / 3);
    printf("%d %.2e %g\n", back, 12345.678, 0.0001);
    return 0;
}
