/* invalid: what virtual functions and abstract classes do not allow (D44) */
class Shape {
public:
    int id;
    virtual int area() = 0;
    virtual int sides() { return 0; }
    virtual static int count() { return 0; }    // error: static member function 'count' cannot be virtual
};
class Rect : public Shape {
public:
    int area() { return 6; }
    double sides() { return 4.0; }              // error: overrides a virtual function but its return type differs
};
virtual int helper() { return 1; }              // error: 'virtual' can only be used on a member function
class Holder { public: Shape inside; };         // error: field 'inside' has abstract type 'class Shape'
int byValue(Shape s) { return 0; }              // error: parameter 1 of 'byValue' has abstract type
Shape make();                                   // error: the return type of 'make' has abstract type
class Circle : public Shape {
public:
    virtual int radius();
};
virtual int Circle::radius() { return 1; }      // error: 'virtual' is only allowed on the declaration inside the class

int main() {
    Shape s;                                    // error: variable 's' has abstract type 'class Shape' (pure virtual function 'area()' is not overridden)
    Shape many[2];                              // error: variable 'many' has abstract type
    Circle c;                                   // error: variable 'c' has abstract type 'class Circle'
    Rect r = { 1 };                             // error: cannot be initialized with a brace list
    int n = Shape().id;                         // error: the object 'T()' has abstract type
    return n;
}
