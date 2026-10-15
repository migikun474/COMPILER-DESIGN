/* invalid: the other side of v27 */
class Shape {
public:
    virtual int area() = 0;
    int plain() = 0;                          // error: is declared '= 0' but is not virtual
};
virtual int loose();                          // error: 'virtual' is only allowed on member functions
int freeConst() const;                        // error: a 'const' qualifier is only allowed on member functions
class Base { public: virtual int f() { return 1; } };
class Bad : public Base { public: double f() { return 2; } };   // error: overrides a virtual function but its return type differs
class Meters { public: int v; explicit Meters(int x) : v(x) { } };
int use(Meters m) { return m.v; }
class Secret { int hidden; public: Secret() : hidden(1) { } };
class Holder {
    int n;
public:
    Holder() : n(0), missing(2) { }           // error: is neither a member nor a direct base
    int value() { return n; }
};
struct Point { int x, y; Point(int a) : x(a), y(a) { } };
struct Line { Point a; Line() { } };          // error: has no default constructor
class Poly { public: virtual int g() { return 0; } };
int peek(Secret &s) { return s.hidden; }      // error: is a private member
int jump(int k) {
    if (k) goto out;                          // error: jump to label 'out' crosses the initialization of 'y'
    int y = 2;
out:
    return k;
}
int cases(int k) {
    switch (k) {
    case 1:
        int z = 3;
        return z;
    case 2:                                   // error: jump to case label crosses the initialization of 'z'
        return 2;
    }
    return 0;
}
int main() {
    Shape s;                                  // error: cannot have the abstract type
    Meters m = 5;                             // error: cannot initialize variable 'm'
    int r = use(4);                           // error: argument 1 of 'use'
    const Holder h;
    r = h.value();                            // error: is not a const member function
    Poly p = {};                              // error: cannot be initialized with a brace list
    return r;
}
