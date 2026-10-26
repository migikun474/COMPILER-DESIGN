/* t34 -- printf's exponent formats %e %E %g %G next to %f: precision,
   width, flags, rounding into the next power of ten (9.9999996), zero,
   negative values, and where %g switches style. Expected output: gcc. */
#include <stdio.h>
int main() {
    double v[] = {1234.5678, 0.000123456, 1.0, 0.0, -98765.4321, 9.9999996, 123456789.0, 0.5, 100000.0, 1000000.0, 0.0001, 0.00001234, 3.14159265};
    int n = 13;
    for (int i = 0; i < n; i++)
        printf("[%e] [%E] [%.2e] [%.0e] [%g] [%G] [%.3g] [%12.4e] [%-12g] [%012.3e]\n", v[i], v[i], v[i], v[i], v[i], v[i], v[i], v[i], v[i], v[i]);
    float f = 2.5f;
    printf("%e %g %f\n", f, f, f);
    return 0;
}
