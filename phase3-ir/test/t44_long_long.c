/* t44 -- 64-bit integers on a 32-bit machine: carries between the two
   halves, multiply, divide and remainder with negatives, shifts across 32,
   comparisons, conversion to and from double, values kept across calls.
   Expected: g++. */
long long mulAdd(long long a, long long b, long long c) { return a * b + c; }
int main() {
    long long a = 4294967295LL, b = 1;
    printf("%lld %lld\n", a + b, -(a + b));
    long long m = mulAdd(123456789LL, 1000003LL, -7LL);
    printf("%lld %lld %lld\n", m, m / -1000LL, m % 1000LL);
    long long x = 1;
    printf("%lld %lld %lld\n", x << 31, x << 32, x << 62);
    long long neg = -1000000000000LL;
    printf("%lld %lld\n", neg >> 4, neg / 7);
    unsigned long long big = 18446744073709551615ULL;
    printf("%llu %llu\n", big, big / 3);
    printf("%d %d %d\n", a > b, neg < a, (a + 1) == 4294967296LL);
    double dd = (double)m;
    long long back = (long long)(dd / 3);
    printf("%.0f %lld\n", dd, back);
    long long keep = 9000000000LL;
    long long r = mulAdd(2, 3, 4);
    printf("%lld %lld\n", keep, r + keep);
    return 0;
}
