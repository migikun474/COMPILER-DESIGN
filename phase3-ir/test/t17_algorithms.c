/* t17 -- small programs end to end: bubble sort, quicksort, binary search,
   Towers of Hanoi, Ackermann, a matrix product, the sieve of Eratosthenes,
   reversing a string and turning numbers into text and back. Expected: g++. */
void bubble(int *a, int n) { int i, j; for (i = 0; i < n; i++) for (j = 0; j + 1 < n - i; j++) if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; } }
void quick(int *a, int lo, int hi) {
    if (lo >= hi) return;
    int p = a[(lo + hi) / 2], i = lo, j = hi;
    while (i <= j) { while (a[i] < p) i++; while (a[j] > p) j--; if (i <= j) { int t = a[i]; a[i] = a[j]; a[j] = t; i++; j--; } }
    quick(a, lo, j); quick(a, i, hi);
}
int find(int *a, int n, int k) { int lo = 0, hi = n - 1; while (lo <= hi) { int m = (lo + hi) / 2; if (a[m] == k) return m; if (a[m] < k) lo = m + 1; else hi = m - 1; } return -1; }
int hanoi(int n) { return n == 0 ? 0 : 2 * hanoi(n - 1) + 1; }
int ack(int m, int n) { return m == 0 ? n + 1 : n == 0 ? ack(m - 1, 1) : ack(m - 1, ack(m, n - 1)); }
int main() {
    int a[8] = {5, 2, 9, 1, 7, 3, 8, 6}, b[8] = {4, 0, 3, 9, 1, 8, 2, 7}, i, j, k;
    bubble(a, 8); quick(b, 0, 7);
    printf("%d %d %d %d %d %d\n", a[0], a[7], b[0], b[7], find(a, 8, 7), find(a, 8, 4));
    printf("%d %d\n", hanoi(10), ack(2, 3));
    int m1[2][2] = {{1, 2}, {3, 4}}, m2[2][2] = {{5, 6}, {7, 8}}, p[2][2];
    for (i = 0; i < 2; i++) for (j = 0; j < 2; j++) { p[i][j] = 0; for (k = 0; k < 2; k++) p[i][j] += m1[i][k] * m2[k][j]; }
    printf("%d %d %d %d\n", p[0][0], p[0][1], p[1][0], p[1][1]);
    char sieve[50]; int primes = 0;
    for (i = 0; i < 50; i++) sieve[i] = 1;
    for (i = 2; i < 50; i++) if (sieve[i]) { primes++; for (j = i * i; j < 50; j += i) sieve[j] = 0; }
    char text[12] = "compiler", t;
    for (i = 0, j = 7; i < j; i++, j--) { t = text[i]; text[i] = text[j]; text[j] = t; }
    int n = 9081, v = 0; char num[8]; k = 0;
    while (n) { num[k++] = (char)('0' + n % 10); n /= 10; }
    for (i = k - 1; i >= 0; i--) v = v * 10 + (num[i] - '0');
    printf("%d %s %d\n", primes, text, v);
    return 0;
}
