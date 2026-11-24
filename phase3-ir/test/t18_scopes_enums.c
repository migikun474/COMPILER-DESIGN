/* t18 -- names and types: a parameter hiding a global, a block hiding a
   parameter (the global read again through a function), loop variables,
   a local hiding a global from its declaration on, statics in two
   functions, typedefs, a conditional constant initializer, enums with C++
   rules (values, switch, overloading on an enum, a cast into an enum).
   Expected: g++. */
enum Color { Red, Green = 5, Blue, };
typedef enum { Lo, Hi } Level;
typedef int Number;
typedef Number Row[3];
int x = 1;
double rate = 2.5 * 2;
float part = 1.25f;
double chosen = sizeof(int) > 2 ? 2.5 : 1.5;              /* a conditional constant initializer */
int show(int v) { return 1; }
int show(Color c) { return 2; }
int globalX() { return x; }
int hide(int x) { int r = x; { int x = 50; r += x; } return r + globalX(); }
int countA() { static int n; return ++n; }
int countB() { static int n = 10; return ++n; }
const char *name(Color c) { switch (c) { case Red: return "red"; case Green: return "green"; default: return "blue"; } }
int main() {
    printf("%d %d %.2f %.2f %.1f\n", hide(3), x, rate, part, chosen);
    int total = 0, i;
    for (i = 0; i < 3; i++) { int i = 7; total += i; }
    printf("%d %d\n", total, i);
    int before = x;
    int x = 40;
    printf("%d %d\n", before, x);
    countA(); countB(); countA();
    printf("%d %d\n", countA(), countB());
    Row r = {1, 2, 3};
    Number n = r[0] + r[2];
    Color c = (Color)6;
    Level l = Hi;
    printf("%d %s %s %d %d %d %d\n", n, name(c), name(Green), Blue, show(c), show(3), l);
    return 0;
}
