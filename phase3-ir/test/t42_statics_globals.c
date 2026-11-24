/* t42 -- storage: a static local kept between calls (also in recursion),
   global arrays and structs partly initialized (the rest is zero), string
   literals in globals, a global changed through a pointer. Expected: g++. */
struct Point { int x, y; };
int table[6] = {5, 6};
struct Point origin = {3};
struct Point pts[3] = {{1, 2}, {3}};
const char *names[3] = {"zero", "one"};
int total;
int next() { static int n = 100; return n++; }
int depth(int k) { static int calls; calls++; return k == 0 ? calls : depth(k - 1); }
int main() {
    int n1 = next(), n2 = next(), n3 = next();   /* one per statement: argument order is unspecified */
    printf("%d %d %d\n", n1, n2, n3);
    printf("%d\n", depth(4));
    printf("%d %d %d %d\n", table[0], table[1], table[2], table[5]);
    printf("%d %d %d %d %d\n", origin.x, origin.y, pts[1].x, pts[1].y, pts[2].x);
    printf("%s %s %d\n", names[0], names[1], names[2] == 0);
    int *p = &total;
    *p = 42;
    total += table[0];
    printf("%d\n", total);
    return 0;
}
