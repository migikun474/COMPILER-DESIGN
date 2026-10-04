/* valid: classes, objects, inheritance, access modifiers, methods,
   this, out-of-class definitions, constructors */
class Shape {
public:
    int sides;
    int area() { return sides * scale(); }    /* calls a member declared later */
    int perimeter();
    static int count();
protected:
    int scale() { return factor; }
    int factor;
private:
    int secret;
};

int Shape::perimeter() { return this->sides * factor; }
int Shape::count() { return 4; }

class Square : public Shape {
public:
    Square(int s) { sides = 4; factor = s; }   /* protected base member, used in a derived class */
    ~Square() { }
    int side() { return factor + scale(); }
};

class Counter {
    int value;                    /* class members are private by default */
public:
    void inc() { value++; }
    int get() { return value; }
};

struct Plain { int a; };          /* struct members are public by default */

int main() {
    Square sq(3);                 /* Square's only constructor takes the side length */
    sq.sides = 4;
    Shape *base = &sq;            /* derived pointer -> base pointer */
    Counter c;
    c.inc();
    struct Plain pl;
    pl.a = 1;
    Shape *made = new Shape;
    int total = base->area() + made->perimeter() + sq.side() + c.get() + pl.a + base->count();   /* static method through an object */
    delete made;
    return total;
}
