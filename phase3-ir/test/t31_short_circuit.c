/* t31 -- side effects and evaluation order: && and || skip their right
   operand, ?: evaluates one branch, the comma operator, chained and
   compound assignment, i++ inside an index, side effects inside loop
   conditions. Expected: g++. */
int calls = 0;
int t(int v) { calls = calls * 10 + v; return v; }
int main() {
    int r1 = t(0) && t(1);
    int r2 = t(2) || t(3);
    int r3 = (t(0) || t(4)) && (t(5) || t(6));
    printf("%d %d %d %d\n", r1, r2, r3, calls);
    calls = 0;
    int r4 = t(1) ? t(7) : t(8);
    int r5 = (t(0), t(9));
    printf("%d %d %d\n", r4, r5, calls);
    int a, b, c;
    a = b = c = 4;
    a += b -= c *= 2;
    printf("%d %d %d\n", a, b, c);
    int arr[5] = {10, 20, 30, 40, 50};
    int i = 1;
    arr[i++] += 5;
    arr[++i] *= 2;
    printf("%d %d %d %d\n", arr[1], arr[2], arr[3], i);
    int n = 0, k = 0;
    while (n++ < 5 && (k += n) < 9) { }
    printf("%d %d\n", n, k);
    return 0;
}
