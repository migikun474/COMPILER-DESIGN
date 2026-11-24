/* t36 -- enums with C++ rules: enumerators as constants (auto-numbered
   and set), a typedef'd unnamed enum, an enum in a struct and as an
   array size, switch, overloading on an enum, casts into an enum,
   functional casts, `?:` keeping the enum type, an anonymous enum used
   for constants. Expected output: g++. */
enum Color { Red, Green = 5, Blue, };
typedef enum { Lo, Hi } Level;
struct Tagged { enum Color kind; int value; };
int table[Blue + 1];

int show(int x) { return 1; }
int show(Color c) { return 2; }
int show(Level l) { return 3; }
const char *name(Color c) {
    switch (c) {
        case Red: return "red";
        case Green: return "green";
        default: return "blue";
    }
}
Color next(Color c) { return c == Blue ? Red : c == Red ? Green : Blue; }

int main() {
    Color c = (Color)6;
    Color d = Color(5);
    Level l = Hi;
    int n = c + 1;
    bool big = c > Green;
    Color e = n > 3 ? Blue : Red;
    enum { Small = 1 << 2, Large = Small * 4 } size = Large;
    struct Tagged t = { Green, 42 };
    printf("%s %s %d %d %d %d %d\n", name(c), name(d), n, big, show(c), show(5), show(l));
    printf("%d %d %d %d %d\n", e, size, t.kind, t.value, (int)sizeof(table));
    int steps = 0;
    Color walk = Red;
    do { walk = next(walk); steps++; } while (walk != Red);
    printf("%d %s %d\n", steps, name(next(Green)), Red + Green + Blue);
    return 0;
}
