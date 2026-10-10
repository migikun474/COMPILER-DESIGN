/* valid: constructor calls, out-of-class constructors/destructors,
   operator overloading, arrays of objects, functional casts, Class::member */
class Vec {
public:
    int x;
    int y;
    Vec(int a, int b) { x = a; y = b; }
    Vec(int a);                         /* declared here, defined below */
    Vec() { x = 0; y = 0; }
    ~Vec();
    Vec operator+(Vec o) { return Vec(x + o.x, y + o.y); }   /* the class name inside its own body */
    Vec operator-() { return Vec(-x, -y); }
    int operator==(Vec o) { return x == o.x && y == o.y; }
    int operator[](int i) { return i == 0 ? x : y; }
    Vec &operator+=(Vec o) { x += o.x; y += o.y; return *this; }
    Vec &operator++() { x++; return *this; }
    Vec operator++(int) { Vec old = *this; x++; return old; }
    int operator()(int k) { return x * k; }
    static int dims();
    Vec *self() { Vec *p = this; return p; }   /* `Vec *` inside class Vec */
};
Vec::Vec(int a) { x = a; y = a; }
Vec::~Vec() { }
int Vec::dims() { return 2; }
Vec operator*(Vec v, int k) { return Vec(v.x * k, v.y * k); }   /* a non-member operator */

int main(int argc, char **argv) {
    Vec a(1, 2);                        /* direct initialization */
    Vec b = Vec(3, 4);                  /* a temporary */
    Vec e;                              /* the default constructor */
    Vec f = 5;                          /* converting constructor Vec(int) */
    Vec c = a + b;                      /* Vec::operator+ */
    Vec d = -c;
    Vec g = a * 2;                      /* ::operator* */
    a += b;
    ++a;
    a++;
    g = d;                              /* memberwise copy */
    int same = (a == b) + a[0] + a(3) + Vec::dims() + c.self()->y;
    Vec row[3];                         /* needs the default constructor */
    int w(7);                           /* direct initialization of a scalar */
    double half = (double) w / 2;
    return same + g.x + w + half + e.x + f.y;
}
