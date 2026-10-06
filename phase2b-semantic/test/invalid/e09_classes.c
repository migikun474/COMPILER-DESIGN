/* invalid classes: access modifiers, this, inheritance, methods */
class Base {
public:
    int pub;
    void work() { }
    int method();
    static int util() { return this->pub; }   // error: 'this' cannot be used in a static member function
    static int util2() { return pub; }        // error: invalid use of non-static member 'pub' in a static member function
protected:
    int prot;
private:
    int priv;
    void hidden() { }
};

class Derived : public Base {
public:
    int peek() { return priv; }   // error: 'priv' is a private member of 'class Base' and is not accessible from class 'Derived'
    int ok() { return prot + pub; }
    foo(int x) { }                // error: member function 'foo' must declare a return type
    ~Other() { }                  // error: destructor name '~Other' does not match the class name 'Derived'
};

class Hidden : private Base {
public:
    int inside() { return pub; }  /* fine: private inheritance still lets Hidden itself use it */
};

class Loop : public Loop { };     // error: 'Loop' cannot inherit from itself
class FromUnknown : public Ghost { };   // error: base class 'Ghost' is not a declared class or struct

int Base::method(int extra) { return extra; }   // error: does not match any declaration in class 'Base'
int Nowhere::method() { return 0; }             // error: use of undeclared class 'Nowhere'

int free_function() {
    return this->pub;             // error: invalid use of 'this' outside of a non-static member function
}

int main() {
    Base b;
    Derived d;
    Hidden h;
    b.pub = 1;
    b.prot = 2;                   // error: 'prot' is a protected member of 'class Base' and is not accessible outside the class
    b.priv = 3;                   // error: 'priv' is a private member of 'class Base'
    b.hidden();                   // error: 'hidden' is a private member of 'class Base'
    d.prot = 4;                   // error: 'prot' is a protected member of 'class Base'
    h.pub = 5;                    // error: is not accessible outside the class because of non-public inheritance
    b.work;                       // error: reference to member function 'work' must be called
    b.work(1);                    // error: function 'work' expects 0 arguments but 1 was provided
    b.nothing();                  // error: no member named 'nothing' in 'class Base'
    return b.pub;
}
