/* t16 -- the MIPS register allocator: values across calls and recursion,
   more live values than registers, arguments computed before a call,
   char / unsigned char / short wrapping in registers, many doubles at once,
   a loop made of goto. Expected: g++. */
int depth(int n) { int a = n, b = n * 2, c = n * 3; if (n == 0) return 0; return depth(n - 1) + a + b + c; }
int three(int a, int b, int c) { return a * 100 + b * 10 + c; }
int twice(int &x) { x = x * 2; return x; }
int main() {
    int v1 = 1, v2 = 2, v3 = 3, v4 = 4, v5 = 5, v6 = 6, v7 = 7, v8 = 8, v9 = 9, v10 = 10;
    int s = depth(5);
    s += v1 * v2 + v3 * v4 + v5 * v6 + v7 * v8 + v9 * v10;
    printf("%d %d %d\n", s, v1 + v10, v5 * v6);
    int x = 3;
    int tw = twice(x);                   /* its own statement: argument order is unspecified */
    int r = three(x, tw, x + 1);
    printf("%d\n", r);
    char c = 120; unsigned char uc = 250; short sh = 32760;
    int i;
    for (i = 0; i < 10; i++) { c++; uc++; sh++; }
    printf("%d %d %d %u\n", c, uc, sh, (unsigned)(unsigned short)sh);
    double d1 = 1.5, d2 = 2.5, d3 = 3.5, d4 = 4.5, d5 = 5.5, d6 = 6.5, d7 = 7.5;
    double dt = d1 * d2 + d3 * d4 + d5 * d6 + d7;
    printf("%.2f %.2f\n", dt, d1 + d7);
    int n = 0, t = 0;
loop:
    t += n * v2;
    if (++n < 5) goto loop;
    printf("%d %d\n", t, v9);
    return 0;
}
