/* t07 -- functions: recursion, mutual recursion through a declaration,
   overloading, references (swap, a reference to a pointer, returning a
   reference, const T & bound to another type), arrays passed with their
   length, a static local, tail recursion. Expected: g++. */
int odd(int n);
int even(int n) { return n == 0 ? 1 : odd(n - 1); }
int odd(int n) { return n == 0 ? 0 : even(n - 1); }
int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int pick(int x) { return 1; }
int pick(double x) { return 2; }
int pick(const char *s) { return 3; }
void swap(int &a, int &b) { int t = a; a = b; b = t; }
void advance(int *&p) { p++; }
int &bigger(int &a, int &b) { return a > b ? a : b; }
double half(const double &v) { return v / 2; }
int sumv(int *v, int n) { int s = 0; while (n--) s += *v++; return s; }
int sum(int *v, int n) { return sumv(v, n); }
double avg(double *v, int n) { double t = 0; int i; for (i = 0; i < n; i++) t += v[i]; return t / n; }
int counter() { static int c = 0; return ++c; }
int main() {
    printf("%d %d %d %d\n", even(10), odd(7), fib(15), gcd(84, 36));
    printf("%d %d %d\n", pick(1), pick(1.0), pick("s"));
    int a = 1, b = 2, arr[3] = {7, 8, 9}, *p = arr;
    int &ra = a;
    ra = 30;
    swap(a, b);
    advance(p);
    bigger(a, b) = 40;
    printf("%d %d %d %.1f\n", a, b, *p, half(5));
    int nums[4] = {1, 2, 3, 4};
    double ds[3] = {1.0, 2.0, 4.5};
    printf("%d %.2f\n", sum(nums, 4), avg(ds, 3));
    counter(); counter();
    printf("%d\n", counter());
    return 0;
}
