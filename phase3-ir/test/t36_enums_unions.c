/* t36 -- enums (C++ rules) and plain unions (D42): enumerators as
   constants, switch, overloading on an enum, casts into an enum, `?:`;
   unions read through another member (type punning) inside a block,
   across blocks and calls, in arrays, by value, with 8-byte members --
   at every -O level, where the optimizer must not forward a value stored
   through one member to a load through another. Expected output: g++. */
enum Color { Red, Green = 5, Blue, };
typedef enum { Lo, Hi } Level;
union Word { int i; float f; unsigned char b[4]; short h[2]; };
union Wide { double d; long long ll; int half[2]; };
struct Tagged { enum Color kind; union Word v; };
union Word g;
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
union Word flip(union Word w) { w.i = w.i ^ 0x80000000; return w; }
int sumBytes(union Word *p) { return p->b[0] + p->b[1] + p->b[2] + p->b[3]; }

int main() {
    Color c = (Color)6;
    Color d = Color(5);
    Level l = Hi;
    int n = c + 1;
    bool big = c > Green;
    Color e = n > 3 ? Blue : Red;
    enum { Small = 1 << 2, Large = Small * 4 } size = Large;
    struct Tagged t = { Green, { 42 } };
    printf("%s %s %d %d %d %d %d\n", name(c), name(d), n, big, show(c), show(5), show(l));
    printf("%d %d %d %d %d\n", e, size, t.kind, t.v.i, (int)sizeof(table));

    union Word w;
    w.i = 0x40490fdb;
    float f1 = w.f;
    w.f = 2.0f;
    int i1 = w.i;
    w.i = 7;
    int i2 = w.i + w.i;
    w.b[0] = 1;
    int i3 = w.i;
    w.h[1] = 2;
    int i4 = w.i;
    union Word fl = flip(w);
    g.f = -1.5f;
    int gb = g.i;
    printf("%.4f %x %d %x %x %x %x\n", f1, i1, i2, i3, i4, fl.i, gb);

    union Word arr[3];
    int k, s = 0;
    for (k = 0; k < 3; k++) arr[k].i = k * 256 + 1;
    for (k = 0; k < 3; k++) if (arr[k].b[1] > 0) s += arr[k].b[0] + arr[k].b[1];
    union Wide x;
    x.d = 1.0;
    int hi = x.half[1];
    x.ll = 5;
    x.half[0] = 0;
    x.half[1] = 0x40000000;
    printf("%d %d %x %.1f %d %d\n", s, sumBytes(&w), hi, x.d, (int)sizeof(union Wide), (int)sizeof(union Word));
    return 0;
}
