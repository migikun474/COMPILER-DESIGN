/* Unnamed struct / union / enum types and anonymous members (C11, C++).
   Layouts are checked at compile time: a wrong size makes an array
   dimension negative. The `// mangled:` names are g++'s for this file. */

/* anonymous members: their fields are fields of the enclosing struct */
struct Value {
    int kind;
    union {                 /* +4 */
        int i;
        float f;
        char c;
    };
    struct {                /* +8 */
        short lo, hi;
    };
};
int value_size_ok[sizeof(struct Value) == 12 ? 1 : -1];

/* nested: an anonymous struct holding an anonymous union */
struct Packet {
    char tag;
    struct {
        union { int word; char bytes[4]; };
        int crc;
    };
};
int packet_size_ok[sizeof(struct Packet) == 12 ? 1 : -1];

/* a struct inside a struct: members after it still belong to the outer one */
struct Outer {
    struct Inner { int x; } in;
    int after;
};

/* typedef names the unnamed type; the first typedef is its name */
typedef struct { int x, y; } Pt, PtAlias;
typedef enum { LOW, HIGH } Level;
typedef union { int n; float r; } Num;

/* unnamed types with variables, and an unnamed enum of constants */
struct { int hits, misses; } stats;
enum { MAX_ITEMS = 8, MIN_ITEMS = 1 };
enum { OFF, ON } power;
int items[MAX_ITEMS];

/* anonymous union in a class: access applies to its members */
class Register {
public:
    union { int raw; char low; };
    int read() { return raw; }                     // mangled: _ZN8Register4readEv
};

int dist2(Pt a, PtAlias *b) { int dx = a.x - b->x, dy = a.y - b->y; return dx * dx + dy * dy; } // mangled: _Z5dist22PtPS_
Level level_of(int v) { return v > 0 ? HIGH : LOW; }   // mangled: _Z8level_ofi
float as_float(Num n, Level l) { return l == HIGH ? n.r : n.n; } // mangled: _Z8as_float3Num5Level

int main() {                                           // mangled: main
    struct Value v;
    v.kind = 1;
    v.i = 42;
    v.f = 1.5f;
    v.lo = 3;
    v.hi = 4;

    struct Value w = { 2, { 7 }, { 1, 2 } };
    struct Value d = { .kind = 3, .c = 'x', .hi = 9 };

    struct Packet p;
    p.word = 0x01020304;
    p.bytes[0] = 1;
    p.crc = p.word ^ 0xff;

    struct Outer o;
    o.in.x = 1;
    o.after = 2;

    Pt a = { 1, 2 };
    Pt b = { .x = 4, .y = 6 };
    stats.hits = dist2(a, &b);
    power = ON;
    items[MIN_ITEMS] = level_of(stats.hits);

    Register r;
    r.raw = 65;
    Num n;
    n.r = 2.5f;
    return v.i + w.i + d.c + p.crc + o.after + r.read() + r.low + (int)as_float(n, HIGH) + power;
}
