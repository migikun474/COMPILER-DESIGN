/* valid: single inheritance, friends, default constructors that also
   run the base's, brace elision, and the flow checks that only warn */
class Shape {
public:
    int kind;
    Shape() { kind = 1; }
    int sides() { return 0; }
};
class Square : public Shape {
    int side;
public:
    Square() { side = 3; }                        /* Shape() runs first */
    int area() { return side * side; }
    friend int peek(const Square &q);
    friend class Auditor;
};
int peek(const Square &q) { return q.side; }
class Auditor { public: int check(const Square &q) { return q.side; } };
class Tile : public Square { public: int color; };   /* a chain of single inheritance */
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
    Square q;
    Shape *s = &q;                                /* derived pointer to base pointer */
    Tile t;
    Auditor a;
    int r = q.area() + s->sides() + s->kind + peek(q) + a.check(q) + t.area() + global.b + grid[1][1];
    return r + sign(0) + dead(1);
}
