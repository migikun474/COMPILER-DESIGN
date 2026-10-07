/* Unnamed struct / class bodies, anonymous struct members, and members
   declared after a nested struct (they still belong to the outer one:
   the parser keeps a stack of enclosing aggregates). */
struct Shape {
    int kind;
    struct { int side; struct { int w, h; }; };
    struct Pos { int x, y; } at;
    int color;
};
typedef struct { int r, g, b; } Rgb;
struct { int count; } totals;
class { public: int id; } anonymous_object;

int area(struct Shape *s) { return s->kind == 0 ? s->side * s->side : s->w * s->h; }

int main() {
    struct Shape s;
    Rgb c = { 1, 2, 3 };
    s.kind = 1;
    s.w = 2;
    s.h = 3;
    s.at.x = 0;
    s.color = c.g;
    totals.count = 4;
    anonymous_object.id = c.r;
    return area(&s) + totals.count + anonymous_object.id;
}
