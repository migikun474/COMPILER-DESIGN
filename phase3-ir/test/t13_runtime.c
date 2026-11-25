/* t13 -- what the MIPS run-time library must get right: 64-bit printf,
   long long <-> double, printf flags, widths, precision, %e %g %x %o %c
   %%, structs and doubles passed and returned through calls, a double, a
   long long and a string as arguments, Newton's method. Expected: g++. */
struct Big { double d; int n[3]; char tag; long long w; };
struct Big make(int k) { struct Big b; b.d = k * 1.5; b.n[2] = k; b.tag = 'A' + k; b.w = 10000000000LL * k; return b; }
double weigh(struct Big b, double f, char c, int i) { return b.d * f + c + i; }
double mix(int n, double d, long long w, char *s) { return d + (double)w + s[0] + n; }
int main() {
    long long big = 123456789012345LL;
    long long other = 987654321098LL;
    printf("%lld %lld %llu %lld %lld\n", big, -big / 7, (unsigned long long)big * 3, big - other, ~other);
    printf("%.1f %lld %d\n", (double)big, (long long)3.99e10, (int)-2.7);
    printf("[%6.2f] [%-8.3f] [%08.2f] [%.0f] [%d]\n", 3.14159, -2.5, 7.125, 0.5, 2);
    printf("[%5d] [%-5d] [%05d] [%x] [%X] [%o] [%c] [%%]\n", -42, 42, -42, 255, 255, 8, 'z');
    printf("%e %E %g %g %.3g\n", 12345.678, 0.000123, 100000.0, 1e-5, 2.0 / 3);
    struct Big s = make(2);
    printf("%.1f %d %c %lld %.1f\n", s.d, s.n[2], s.tag, s.w, weigh(s, 2.0, 'a', 5));
    printf("%.2f\n", mix(1, 2.5, 3LL, "Z"));
    double x = 2, r = 1;
    int i;
    for (i = 0; i < 20; i++) r = (r + x / r) / 2;
    printf("%.10f\n", r);
    return 0;
}
