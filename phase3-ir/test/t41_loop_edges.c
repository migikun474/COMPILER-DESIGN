/* t41 -- loop boundaries: loops that run 0, 1, 2, 3 and 7 times (the
   unrolled copy at -O3 must keep each exit test), do-while running once,
   break and continue in nested loops, a backward goto, a switch inside a
   loop using continue. Expected: g++. */
int count(int n) { int c = 0, i; for (i = 0; i < n; i++) c = c * 2 + 1; return c; }
int main() {
    printf("%d %d %d %d %d\n", count(0), count(1), count(2), count(3), count(7));
    int d = 0;
    do { d++; } while (d < 0);
    int w = 10;
    while (w < 10) w++;
    printf("%d %d\n", d, w);
    int i, j, found = -1, skipped = 0;
    for (i = 0; i < 5 && found < 0; i++)
        for (j = 0; j < 5; j++) {
            if (j == 1) { skipped++; continue; }
            if (i * j == 6) { found = i * 10 + j; break; }
        }
    printf("%d %d %d\n", found, i, skipped);
    int k = 0, total = 0;
again:
    total += k;
    if (++k < 5) goto again;
    printf("%d\n", total);
    int s = 0;
    for (i = 0; i < 8; i++) {
        switch (i % 4) {
            case 0: continue;
            case 1: s += 1; break;
            case 2: s += 10;
            case 3: s += 100; break;
        }
        s += 1000;
    }
    printf("%d\n", s);
    return 0;
}
