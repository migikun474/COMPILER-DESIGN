/* t15 -- -O3: inlining (side effects kept, several returns, a reference
   parameter, a by-value struct the caller keeps), a recursive function
   that must not be inlined, a tail call with swapped arguments, a division
   in a loop that may run zero times, values reused across branches only
   where safe. Expected: g++. */
struct P { int a, b; };
int calls = 0;
int sq(int v) { return v * v; }
int clamp(int v, int lo, int hi) { if (v < lo) return lo; if (v > hi) return hi; return v; }
int counted(int v) { calls++; return v + calls; }
void inc(int &r) { r++; }
int sumP(struct P p) { p.a = 0; return p.b; }
int fact(int n) { return n <= 1 ? 1 : n * fact(n - 1); }
int down(int a, int b) { if (a <= 0) return b; return down(b - 1, a - 1); }
int divide(int n, int d) { int s = 0; while (n > 0) { s += 100 / d; n--; } return s; }
int main() {
    int r = counted(1) + counted(1);
    int v = 3;
    inc(v);
    struct P p = {5, 6};
    printf("%d %d %d %d %d\n", sq(7), clamp(-4, 0, 9), clamp(50, 0, 9), r, calls);
    printf("%d %d %d %d\n", v, sumP(p), p.a, fact(6));
    printf("%d %d %d\n", down(7, 3), divide(0, 0), divide(3, 4));
    int x = v * 3, t;
    if (x > 10) t = v * 3 + 1; else t = v * 3 - 1;
    v = 100;
    printf("%d %d\n", t, v * 3);
    return 0;
}
