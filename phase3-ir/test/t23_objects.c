/* t23 -- classes used together: an inheritance chain, objects holding
   objects, arrays of objects, objects through pointers and references,
   operators returning references */

class Shape {
public:
    int id;
    static int live;
    Shape() { id = ++live; printf("Shape %d\n", id); }
    int area() { return 0; }
    int name() { return 'S'; }
};
int Shape::live = 0;

class Rect : public Shape {
public:
    int w, h;
    Rect() { w = 1; h = 1; }
    void set(int a, int b) { w = a; h = b; }
    int area() { return w * h; }               /* hides Shape::area */
    int perimeter() { return 2 * (w + h); }
};

class Square : public Rect {
public:
    void side(int s) { set(s, s); }            /* a base class method through `this` */
    int name() { return 'Q'; }
};

class Point {
public:
    int x, y;
    Point() { x = 0; y = 0; }
    Point &operator+=(const Point &o) { x += o.x; y += o.y; return *this; }
    Point operator-(const Point &o) { Point r; r.x = x - o.x; r.y = y - o.y; return r; }
    bool operator<(const Point &o) { return x * x + y * y < o.x * o.x + o.y * o.y; }
    int &operator[](int i) { return i == 0 ? x : y; }
};
Point at(int a, int b) { Point p; p.x = a; p.y = b; return p; }

class Segment {
public:
    Point from, to;                            /* objects inside an object */
    void set(int a, int b, int c, int d) { from = at(a, b); to = at(c, d); }
    int length2() { Point d = to - from; return d.x * d.x + d.y * d.y; }
};

int total(Rect &r) { return r.area() + r.id; }
int through(Shape *s) { return s->area() + s->name(); }      /* no virtual: Shape's own functions */
void grow(Rect *r, int by) { r->w += by; r->h += by; }

int main() {
    Rect r;
    r.set(3, 4);
    Square q;
    q.side(5);
    printf("%d %d %d %d\n", r.area(), q.area(), q.perimeter(), Shape::live);
    Shape *asShape = &q;                       /* the hidden Shape::name is reached through a Shape * */
    printf("%d %d %c %c\n", total(r), through(&q), q.name(), asShape->name());
    grow(&q, 1);
    Rect &alias = q;
    alias.w = 10;
    printf("%d %d\n", q.area(), alias.perimeter());
    {
        Rect pair[2];
        pair[1].w = 6;
        printf("%d %d %d\n", pair[0].area() + pair[1].area(), pair[1].id, Shape::live);
    }
    printf("%d\n", Shape::live);

    Point a = at(3, 4), b = at(1, 1);
    a += b;
    (a += b) += b;
    a[0] = a[1] * 2;
    Point c = a - b;
    printf("%d %d %d %d %d %d\n", a.x, a.y, c.x, c.y, b < a, a < b);
    Segment s;
    s.set(1, 2, 4, 6);
    printf("%d %d\n", s.length2(), s.to.y);

    {
        Rect last;
        last.set(2, 9);
        Shape *base = &last;
        printf("%d %d %d\n", last.area(), base->area(), base->id);
    }
    return Shape::live;
}
