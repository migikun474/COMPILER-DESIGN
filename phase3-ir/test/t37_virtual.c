/* t37 -- virtual functions (D44): overriding at several levels (with and
   without the keyword), pure virtual functions and an abstract base used
   through pointers, calls through pointers, references and `this`,
   qualified calls, a virtual call made while a base constructor runs, copies
   and assignments that keep each object's own class, by-value parameters
   and results, a virtual operator, overloaded virtual functions, arguments
   wider than the 16 bytes of $a0-$a3, global and implicitly constructed
   objects -- at every -O level. Expected output: g++. */
class Shape {
public:
    int id;
    Shape() { id = 1; printf("Shape() sees %d\n", tag()); }
    virtual int tag() { return 10; }
    virtual int area() = 0;
    virtual int scale(int k, int m, double f, int n) { return k + m + (int)f + n; }
    virtual int pick(int x) { return x; }
    virtual int pick(double x) { return (int)(x * 2); }
    int describe() { return tag() * 1000 + area(); }
    int plain() { return 1; }
};
class Rect : public Shape {
public:
    int w, h;
    Rect() { w = 2; h = 3; }
    int tag() { return 20; }
    int area() { return w * h; }
    virtual int perimeter() { return 2 * (w + h); }
    int plain() { return 2; }
};
class Square : public Rect {
public:
    Square() { w = 4; h = 4; }
    virtual int tag() { return 30; }
    int perimeter() { return 4 * w; }
    int scale(int k, int m, double f, int n) { return 100 + Rect::scale(k, m, f, n); }
    int pick(double x) { return -1; }
};
class Counter {
public:
    int n;
    virtual int step() { n = n + 1; return n; }
    virtual Counter &operator+=(int k) { n = n + k; return *this; }
};
class Fast : public Counter {
public:
    int step() { n = n + 10; return n; }
    Counter &operator+=(int k) { n = n + 100 * k; return *this; }
};
Square g;

int area2(Shape &s) { return s.area() * 2; }
int perim(Rect r) { return r.perimeter(); }       /* a by-value Rect is exactly a Rect */
Rect copyOf(Rect &r) { return r; }
int sum(Shape **all, int n) { int s = 0, i; for (i = 0; i < n; i++) s += all[i]->area(); return s; }
int depth(Rect *p, int n) { return n == 0 ? p->perimeter() : depth(p, n - 1) + 1; }

int main() {
    Rect r;
    Square q;
    Shape *shapes[3];
    shapes[0] = &r; shapes[1] = &q; shapes[2] = &g;
    printf("%d %d %d\n", shapes[0]->area(), shapes[1]->area(), sum(shapes, 3));
    printf("%d %d %d\n", r.describe(), q.describe(), area2(q));
    Rect *rp = &q;
    printf("%d %d %d %d\n", rp->perimeter(), rp->Rect::perimeter(), rp->plain(), rp->tag());
    printf("%d %d\n", rp->scale(1, 2, 3.5, 4), r.scale(1, 2, 3.5, 4));
    printf("%d %d %d %d\n", rp->pick(5), rp->pick(2.5), r.pick(2.5), shapes[0]->pick(7));
    Rect copy = *rp;                                 /* a Rect, even though *rp is a Square */
    printf("%d %d\n", copy.perimeter(), copy.tag());
    Rect r2;
    r2.w = 9;
    *rp = r2;                                        /* members copied, q stays a Square */
    printf("%d %d %d\n", q.perimeter(), q.tag(), q.w);
    printf("%d %d\n", perim(*rp), copyOf(*rp).perimeter());  /* copies of a Square seen as a Rect */
    printf("%d\n", depth(&q, 5));
    Fast f;
    f.n = 0;
    Counter &c = f;
    c.step();
    c += 2;
    Counter plainC;
    plainC.n = 0;
    plainC.step();
    printf("%d %d\n", f.n, plainC.n);
    return 0;
}
