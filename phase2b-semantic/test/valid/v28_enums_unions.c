/* valid: enums and plain unions (D42). An enum is its own type with C++
   rules: it converts to int, an int needs a cast to become an enum, and
   overloads and link names tell enums apart. A union holds one member at
   a time, every member at offset 0. */
enum Color { Red, Green = 5, Blue, };
typedef enum { Lo, Hi } Level;
union Value { int i; float f; unsigned char b[4]; };
struct Tagged { enum Color kind; union Value v; };

int show(int x) { return 1; }                   // mangled: _Z4showi
int show(Color c) { return 2; }                 // mangled: _Z4show5Color
int show(Level l) { return 3; }                 // mangled: _Z4show5Level
int bits(union Value v) { return v.i; }         // mangled: _Z4bits5Value
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
    union Value v = { .f = 1.0f };              /* a designator picks the member */
    union Value w = { 7 };                      /* otherwise the first member */
    struct Tagged t = { Green, { 42 } };
    v.i = v.i + 1;
    return n + show(c) + show(l) + show(5) + bits(w) + t.v.i + table[0] + d + e + size + sizeof(union Value);
}
