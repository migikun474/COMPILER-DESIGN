/* t35 -- loop shapes at -O3: break, continue, a switch inside a while, do-while,
   nested for. This program hung the -O3 global common-subexpression pass
   before its data flow started unknown blocks at top (D41). Expected: g++. */
int main() {
    int n, s = 0, i, k = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++) { if (i == 7) break; if (i % 2) continue; s += i; }
    while (k < n) { switch (k % 3) { case 0: s += 1; break; case 1: s += 2; break; default: s -= 1; } k++; }
    do { s += 10; } while (--n > 0);
    for (i = 0; i < 3; i++) for (k = 0; k < 2; k++) s += i * k;
    printf("%d %d\n", s, i);
    return 0;
}
