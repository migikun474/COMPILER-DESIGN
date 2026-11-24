/* t06 -- structs: nesting, copies (the original stays the
   same), by-value parameters and results, an array of structs, a struct
   with an array member, anonymous struct members, a typedef'd unnamed
   struct, layout with padding.
   Expected: g++. */
struct In { int a; char tag; };
struct Out { struct In in; int list[3]; double w; };
typedef struct { int x, y; } Pt;
struct Holder { int id; struct { int lo, hi; }; };
struct Out grow(struct Out o) { o.in.a += 100; o.list[2] = 9; return o; }
int area(Pt p) { p.x = p.x * 2; return p.x * p.y; }
int main() {
    struct Out o = {{1, 'k'}, {5, 6, 7}, 2.5};
    struct Out g = grow(o);
    printf("%d %d %c %d %.1f\n", o.in.a, g.in.a, g.in.tag, g.list[2] + o.list[2], g.w);
    Pt p = {3, 4};
    printf("%d %d\n", area(p), p.x);
    struct Out os[2];
    struct Out *op = &os[1];
    int ii = 1, jj = 2;
    os[ii].list[jj] = 31;
    op->list[ii] = 17;
    printf("%d %d %d\n", os[1].list[2], os[ii].list[1], grow(o).in.a);
    Pt ps[2] = {{1, 2}, {3, 4}};
    ps[1] = ps[0];
    ps[0].y = 50;
    printf("%d %d\n", ps[1].y, ps[0].y);
    struct Holder h;
    h.lo = 3; h.hi = 8; h.id = 1;
    printf("%d %d\n", h.hi - h.lo, (int)sizeof(struct Holder));
    printf("%d %d\n", (int)sizeof(struct In), (int)sizeof(struct Out));
    return 0;
}
