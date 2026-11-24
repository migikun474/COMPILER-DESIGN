/* invalid: the reduced C++ subset (D35) -- default constructors only,
   single inheritance, no slicing, no nested or local classes, no lazily
   built static objects -- plus access and jump-over-initialization checks */
class Base { public: int b; };
class Other { public: int o; };
class Two : public Base, public Other { };    // error: 'Two' cannot have a second base class 'Other': only single inheritance is supported
class Derived : public Base { public: int d; };
class Point {
public:
    int x;
    Point(int a) { x = a; }                   // error: constructor 'Point' cannot take parameters: only default constructors 'Point()' are supported
};
class Counter {
    int n;
public:
    Counter() { n = 0; }
    int value() { return n; }
    class Inner { int i; };                   // error: nested class 'Inner' is not supported: define it outside 'Counter'
};
class Secret { int hidden; public: Secret() { hidden = 1; } };
int peek(Secret &s) { return s.hidden; }      // error: is a private member
int byValue(Base b) { return b.b; }
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
int statics() {
    static Counter c;                         // error: static local 'c' of type 'class Counter' is not supported: its class has a constructor
    return 0;
}
int locals() {
    class Local { public: int f() { return 1; } };   // error: a class cannot be defined inside a function (no local classes)
    return 0;
}
int main() {
    Derived d;
    Base b = d;                               // error: object slicing is not supported
    b = d;                                    // error: object slicing is not supported
    int r = byValue(d);                       // error: no object slicing
    Counter c(3);                             // error: 'class Counter' cannot be constructed from 1 argument: only default construction is supported
    Counter copy(c);                          /* fine: a copy of c's bytes */
    const Counter k;
    r = k.value();                            // error: member function 'value' cannot be called on a const object (there are no const member functions)
    return r + copy.value();
}
int conds(int a, int b) {
    if (a = b) return 1;                      // warning: assignment used as the condition of 'if'; did you mean '=='?
    while (a = 0) { }                         // warning: assignment used as the condition of 'while'
    if ((a = b)) return 4;                    /* extra parentheses: the assignment is meant, no warning (gcc) */
    while ((a = 0)) { }
    return a == b ? 1 : (a = 2) ? 2 : 3;      /* parenthesized as well: no warning, as in gcc */
}
