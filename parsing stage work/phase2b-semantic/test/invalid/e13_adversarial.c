/* invalid: corner cases found while trying to break the analyzer */
enum E { ZERO, ONE };
class A {
public:
    int x;
    int get() { return x; }
    int noCapture() { auto f = []() { return x; }; return f(); }   // error: member 'x' needs 'this'
    int noCapture2() { auto f = []() { return get(); }; return f(); }   // error: calling member function 'get' needs 'this'
private:
    int helper() { return 1; }
};
class B : public A {
public:
    int sum() { return x + 1; }   // error: reference to non-static member function 'x' must be called
    int x() { return 0; }         /* hides the inherited field A::x */
};
int h(long a) { return 1; }
int h(double a) { return 2; }
void k(void *p) { }

int main() {
    A a;
    char c = 'a';
    int x = 1;
    B *pb = &a;                   // error: cannot initialize variable 'pb' of type 'class B *'
    int v = a.get(1);             // error: function 'get' expects 0 arguments but 1 was provided
    v = a.helper();               // error: 'helper' is a private member of 'class A'
    switch (c) {
        case 'a': break;
        case 97: break;           // error: duplicate case value '97'
        case ONE: break;
        case 1: break;            // error: duplicate case value '1'
    }
    v = h(x);                     // error: call to overloaded function 'h(int)' is ambiguous
    k(h);                         // error: reference to overloaded function 'h' is ambiguous
    int (*pa)[3] = &x;            // error: cannot initialize variable 'pa' of type 'int (*)[3]' with a value of type 'int *'
    return v;
}
