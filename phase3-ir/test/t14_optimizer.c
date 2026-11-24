/* t14 -- -O1/-O2 must not reuse what may have changed, and must keep what
   is used: constants that wrap, a branch that never runs, x + y next to
   y + x, values changed through a pointer, a reference, a call and an
   array element, constants that differ per path, a loop-carried value,
   a dead assignment, a call kept although its result is unused, a store
   then a load of the same place. Expected: g++. */
int g = 5;
int calls = 0;
int touch() { calls++; g = g + 1; return g; }
void bump(int &r) { r = r + 100; }
int main() {
    int big = 2147483647, w = big + 0;
    printf("%d %d %d\n", w * 2, (w + 1) / 2, 3 * 4 + 5);
    if (2 > 3) printf("never\n");
    int x = 4, y = 6;
    int s1 = x + y, s2 = y + x, s3 = x * y + 2;
    int *p = &x;
    *p = 10;
    int s4 = x + y;
    int h = g;
    touch();
    int s5 = g + h;
    bump(y);
    printf("%d %d %d %d %d %d\n", s1, s2, s3, s4, s5, x + y);
    int a[3] = {1, 2, 3}, i = 1;
    int e1 = a[i] * 2;
    a[1] = 9;
    printf("%d %d\n", e1, a[i] * 2);
    int z;
    if (calls) z = 1; else z = 2;
    int k = 0, step = 3, acc = 0;
    while (k < 5) { acc += step; k++; }
    int same = x | x, all = x | -1, some = x | 4, cmp = 0;
    if (x <= x) cmp = 1;
    if (x == x) cmp += 2;
    int ignored = touch();
    printf("%d %d %d %d\n", same, all, some, cmp);
    int dead = 7;
    dead = 8;
    touch();
    int m[2];
    m[0] = 42;
    int r = m[0];
    printf("%d %d %d %d %d\n", z, acc, k, dead, r + calls);
    return 0;
}
