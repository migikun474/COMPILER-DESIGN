/* valid: enums (D42). An enum is its own type with C++ rules: it
   converts to int, an int needs a cast to become an enum, and overloads
   and link names tell enums apart. */
enum Color { Red, Green = 5, Blue, };
typedef enum { Lo, Hi } Level;
struct Tagged { enum Color kind; int value; };

int show(int x) { return 1; }                   // mangled: _Z4showi
int show(Color c) { return 2; }                 // mangled: _Z4show5Color
int show(Level l) { return 3; }                 // mangled: _Z4show5Level
const char *name(enum Color c) {                // mangled: _Z4name5Color
    switch (c) {
        case Red: return "red";
        case Green: return "green";
        default: return "blue";
    }
}
int table[Blue + 1];                            /* an enumerator is a constant expression */

int main() {
    Color c = (Color)6;                         /* int -> enum: only with a cast */
    Color d = Color(5);
    enum Color e = c > Green ? Blue : Red;      /* `?:` keeps the enum type */
    Level l = Hi;
    int n = c + 1;                              /* enum -> int: implicit */
    enum { Small = 1 << 2, Large = Small * 4 } size = Large;
    struct Tagged t = { Green, 42 };
    return n + show(c) + show(l) + show(5) + t.kind + t.value + table[0] + d + e + size;
}
