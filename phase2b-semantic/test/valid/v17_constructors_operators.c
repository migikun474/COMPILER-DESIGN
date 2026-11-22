/* valid: default constructors (in and out of class), operator overloading,
   arrays of objects, functional casts, Class::member */
class Vec {
public:
    int x;
    int y;
    Vec();                              /* declared here, defined below */
    Vec operator+(Vec o) { Vec r; r.x = x + o.x; r.y = y + o.y; return r; }   /* the class name inside its own body */
    Vec operator-() { Vec r; r.x = -x; r.y = -y; return r; }
    int operator==(Vec o) { return x == o.x && y == o.y; }
    int operator[](int i) { return i == 0 ? x : y; }
    Vec &operator+=(Vec o) { x += o.x; y += o.y; return *this; }
    Vec &operator++() { x++; return *this; }
    Vec operator++(int) { Vec old = *this; x++; return old; }
    int operator()(int k) { return x * k; }
    static int dims();
    Vec *self() { Vec *p = this; return p; }   /* `Vec *` inside class Vec */
};
Vec::Vec() { x = 0; y = 0; }
int Vec::dims() { return 2; }
Vec make(int a, int b) { Vec v; v.x = a; v.y = b; return v; }
Vec operator*(Vec v, int k) { return make(v.x * k, v.y * k); }   /* a non-member operator */

int main(int argc, char **argv) {
    Vec a = make(1, 2);
    Vec b = make(3, 4);
    Vec e;                              /* the default constructor */
    Vec t = Vec();                      /* a default-constructed temporary */
    Vec c = a + b;                      /* Vec::operator+ */
    Vec d = -c;
    Vec g = a * 2;                      /* ::operator* */
    a += b;
    ++a;
    a++;
    g = d;                              /* memberwise copy */
    int same = (a == b) + a[0] + a(3) + Vec::dims() + c.self()->y;
    Vec row[3];                         /* each element default-constructed */
    int w(7);                           /* direct initialization of a scalar */
    double half = (double) w / 2;
    return same + g.x + w + half + e.x + t.y + row[1].x;
}
