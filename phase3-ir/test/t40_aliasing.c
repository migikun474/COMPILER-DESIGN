/* t40 -- the optimizer must not reuse a value that may have changed:
   a store through a pointer to a local, two pointers to one variable,
   array elements reached two ways, a global changed by a call, a value
   read again after a call that wrote through its address. Expected: g++. */
int g = 1;
void bump() { g = g + 10; }
void setp(int *p, int v) { *p = v; }
void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }
int main() {
    int x = 5;
    int *p = &x;
    int y = x + 1;
    *p = 100;
    int z = x + 1;
    printf("%d %d\n", y, z);
    int *q = &x;
    *q = 7;
    printf("%d %d\n", *p, x * 2);
    int a[4] = {1, 2, 3, 4};
    int *e = &a[2];
    int i = 2, before = a[i];
    *e = 9;
    printf("%d %d %d\n", before, a[i], a[2] + e[0]);
    int h = g;
    bump();
    printf("%d %d\n", h, g);
    int v = 3;
    setp(&v, 4);
    printf("%d\n", v * v);
    int m = 1, n = 2;
    swap(&m, &n);
    swap(&m, &m);
    printf("%d %d\n", m, n);
    return 0;
}
