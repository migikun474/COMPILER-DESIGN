/* t03 -- boolean expressions: the slides' a < b || c < d && e < f,
   comparisons and ! used as values, booleans stored and summed, && / ||
   in loop conditions, bool variables. Expected: g++. */
int main() {
    int a = 1, b = 2, c = 5, d = 4, e = 6, f = 7;
    int x = a < b || c < d && e < f;
    int y = (a > b || c < d) && e < f;
    printf("%d %d %d %d\n", x, y, !x, !!c);
    int t = (a == 1) + (b != 2) + (c >= 5) + (d <= 3) + (e > f);
    printf("%d %d %d\n", t, a < b == 1, (c > d) * 10);
    bool p = c > d, q = !p;
    printf("%d %d %d %d\n", p, q, p && !q, p || q);
    int i = 0, n = 0;
    while (i < 10 && !(i > 6 || n > 20)) n += i++;
    printf("%d %d\n", i, n);
    if (!(a < b) || c == d) printf("wrong\n"); else printf("right\n");
    if (true && a) printf("t\n");
    while (false) printf("never\n");
    return 0;
}
