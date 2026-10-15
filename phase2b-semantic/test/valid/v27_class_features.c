/* valid: virtual functions and abstract classes, const member functions,
   friends, explicit and converting constructors, member initializer
   lists, brace elision, and the flow checks that only warn */
class Shape {
public:
    virtual int area() const = 0;
    virtual int sides() const { return 0; }
    virtual ~Shape() { }
};
class Square : public Shape {
    int side;
public:
    explicit Square(int s) : side(s) { }
    int area() const { return side * side; }      /* overrides: virtual without the keyword */
    friend int peek(const Square &q);
    friend class Auditor;
};
int peek(const Square &q) { return q.side; }
class Auditor { public: int check(const Square &q) { return q.side; } };
class Meters { public: int v; Meters(int x) : v(x) { } };
int twice(Meters m) { return m.v * 2; }           /* twice(4) converts */
Meters back(int k) { return k; }                  /* so does the return */
struct Pair { int a[2]; int b; };
struct Pair global = {1, 2, 3};                   /* braces elided: {{1, 2}, 3} */
int grid[][2] = {1, 2, 3, 4};                     /* two rows */
int sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;                         // warning: control reaches end of non-void function 'sign' on some path
}
int dead(int x) {
    return x;
    x++;                                          // warning: code will never be executed
}
int main() {
    Square q(3);
    const Shape &s = q;
    Auditor a;
    int r = s.area() + s.sides() + peek(q) + a.check(q) + twice(4) + back(5).v + global.b + grid[1][1];
    return r + sign(0) + dead(1);
}
