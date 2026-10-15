/* member initializer lists, const member functions, friends, explicit
   and converting constructors (arguments, references, returns).
   Expected output: g++. */
#include <stdio.h>

class Point {
  public:
    int x, y;
    Point(int a) : x(a), y(a * 2) { printf("(P%d) ", a); }   /* converting: int -> Point */
    Point(int a, int b) : x(a), y(b) { }
    int sum() const { return x + y; }
};

class Line {
    Point from, to;           /* no default constructor: the list must build them */
    int &uses;                /* a reference member */
    int count;
  public:
    Line(Point a, Point b, int &u) : to(b), from(a), uses(u), count() { uses++; } /* built in declaration order */
    int length() const { return to.x - from.x; }
    int width() const { return count; }
    friend int peek(const Line &l);
    friend class Inspector;
};

int peek(const Line &l) { return l.from.y + l.to.y; }       /* a friend reads private members */

class Inspector {
  public:
    int look(Line &l) { l.count = 9; return l.uses + l.count; }
};

class Counter {
    int n;
  public:
    Counter() : n(0) { }
    int get() const { return n; }      /* chosen for a const object */
    int get() { return n + 100; }      /* preferred for a non-const one */
    void add(int k) { n += k; }
};

class Meters {
  public:
    int v;
    explicit Meters(int x) : v(x) { }  /* never an implicit conversion */
};
int useMeters(Meters m) { return m.v; }

class Box {
  public:
    int w;
    Box(int a) : w(a) { printf("[+%d] ", w); }
    Box(const Box &o) : w(o.w + 100) { printf("[copy %d] ", w); }
    ~Box() { printf("[-%d] ", w); }
};
int byValue(Box b) { return b.w; }
int byRef(const Box &b) { return b.w * 2; }
Box makeBox(int k) { return k * 3; }   /* converted at the return */
int pick(int a) { return a; }
int pick(Box b) { return b.w + 1000; }  /* an int argument prefers pick(int) */

class Base {
  public:
    int tag;
    Base(int t) : tag(t) { printf("<B%d> ", t); }
};
class Derived : public Base {
  public:
    int extra;
    Derived(int e) : Base(e * 10), extra(e) { printf("<D%d> ", e); }
};

int area(Point p) { return p.x * p.y; }

int main() {
    int uses = 0;
    Line l(Point(1, 5), 4, uses);
    printf("| %d %d %d %d\n", l.length(), l.width(), peek(l), uses);
    Inspector in;
    int seen = in.look(l);             /* separate statements: argument order is unspecified */
    printf("%d %d\n", seen, l.width());

    Counter c;
    const Counter &rc = c;
    c.add(3);
    printf("%d %d\n", c.get(), rc.get());

    Meters m(7);
    printf("%d\n", useMeters(m));
    printf("%d | ", byValue(5));
    printf("%d | ", byRef(6));
    printf("%d | ", pick(7));
    Box b = makeBox(4);
    printf("%d\n", b.w);

    Derived d(3);
    int a = area(6);
    int sum = Point(2).sum();
    printf("%d %d | %d %d\n", d.tag, d.extra, a, sum);
    return 0;
}
