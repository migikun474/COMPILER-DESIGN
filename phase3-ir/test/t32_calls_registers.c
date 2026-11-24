/* t32 -- calls: more arguments than $a0-$a3 hold, mixed int / char /
   double / long long arguments, arguments that are themselves calls,
   values that must survive calls, a struct passed and returned by value,
   recursion with several live values. Expected: g++. */
struct Pair { int x; double y; };
int many(int a, int b, int c, int d, int e, int f) { return a - b + c * d - e + f; }
double mixed(char c, double d, int i, long long w) { return c + d * i + (double)w; }
struct Pair make(int x, double y) { struct Pair p; p.x = x; p.y = y; return p; }
struct Pair twice(struct Pair p) { p.x = p.x * 2; p.y = p.y * 2; return p; }
int sq(int v) { return v * v; }
int walk(int n, int acc) {
    int before = acc + n;
    if (n == 0) return acc;
    int r = walk(n - 1, acc + sq(n));
    return r + before - acc - n;
}
int main() {
    printf("%d\n", many(1, 2, 3, 4, 5, 6));
    printf("%.2f\n", mixed('A', 1.5, 4, 10000000000LL));
    printf("%d\n", many(sq(1), sq(2), sq(3), sq(4), sq(5), sq(6)));
    int keep1 = 11, keep2 = 22, keep3 = 33, keep4 = 44, keep5 = 55;
    int s = sq(keep1) + sq(keep2);
    printf("%d %d %d %d %d %d\n", s, keep1, keep2, keep3, keep4, keep5);
    struct Pair p = twice(make(3, 1.25));
    printf("%d %.2f\n", p.x, p.y);
    printf("%d\n", walk(10, 0));
    return 0;
}
