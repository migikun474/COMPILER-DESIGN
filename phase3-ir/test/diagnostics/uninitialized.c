/* a variable read on some path before anything was stored in it */

int pick(int which) {
    int x;
    if (which) x = 1;
    return x; /* not assigned when which == 0 */
}

int main() {
    int a;
    int b = a + 1;
    int c;
    c = 5;       /* assigned before it is read */
    int table[4]; /* arrays and objects are not tracked */
    long long wide;
    printf("%d %d %d %d\n", b, c, table[0], pick(1));
    return (int) wide;
}
