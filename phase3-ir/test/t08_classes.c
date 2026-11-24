/* t08 -- classes: construction order (base, member objects, body), a
   static member, operators (+, +=, ==, []), an array of objects, objects
   inside an object, a derived class hiding a base function and calling it
   back through Base::, this, a friend, a global object built before main,
   by-value copies (block copies: no copy constructors). Expected: g++. */
class Part { public: int id; Part() { id = 7; printf("Part "); } };
class Vec {
public:
    int x, y;
    static int made;
    Vec() { x = 0; y = 0; made++; }
    Vec operator+(Vec &o) { Vec r; r.x = x + o.x; r.y = y + o.y; return r; }
    Vec &operator+=(int k) { x += k; y += k; return *this; }
    int operator==(Vec &o) { return x == o.x && y == o.y; }
    int &operator[](int i) { return i == 0 ? x : y; }
    int operator()(int k) { return x * k; }
    friend int peek(Vec &v);
};
int Vec::made = 0;
int peek(Vec &v) { return v.x * 100 + v.y; }
class Base { public: int b; Base() { b = 1; printf("Base "); } int area() { return 10; } };
class Plain : public Base { public: int extra; };   /* no constructor: Base's runs */
class Shape : public Base {
public:
    Part p;
    Shape() { b = b + 1; printf("Shape\n"); }
    int area() { return Base::area() + this->b; }
};
Vec origin;
int twice(Vec v) { v.x = v.x * 2; return v.x; }
int main() {
    Shape s;
    printf("%d %d %d\n", s.area(), s.p.id, s.b);
    Vec a, b;
    a += 3;
    b.x = 1; b.y = 2;
    Vec c = a + b;
    printf("%d %d %d %d\n", c[0], c[1], c == a, peek(c));
    printf("%d %d\n", twice(c), c.x);
    c[1] = 9;
    Plain pl;
    printf("%d %d %d %d\n", c.y, c(3), Vec().x, pl.b);
    Vec many[3];
    many[2] += 5;
    printf("%d %d %d\n", many[2].y, Vec::made, origin.x);
    return 0;
}
