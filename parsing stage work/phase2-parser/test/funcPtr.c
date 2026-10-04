int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }
int apply(int (*f)(int, int), int x, int y) { return f(x, y); }
int main() {
 int r1 = apply(add, 2, 3);
 int r2 = apply(mul, 2, 3);
 printf("%d\n",r1 + r2); // 5 + 6 = 11
}
