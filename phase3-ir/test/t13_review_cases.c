/* t13 -- cases found by the code review of the generator: each one was
   wrong before it was fixed */
#include <stdio.h>
#include <stdarg.h>

double half(const double &v) { return v / 2; }       /* const T & bound to another type */

class A { public: int a; A() { a = 1; } int ga() { return a; } };
class B { public: int b; B() { b = 2; } int gb() { return b; } };
class C : public A, public B {                        /* B is not at offset 0 */
public:
    int c;
    C() { c = 3; }
    int sum() { return a + b + c; }
};
int takeB(B *p) { return p ? p->b : -1; }

class Cnt {
public:
    static int made;
    int id;
    Cnt() { made++; id = made; }
};
int Cnt::made = 5;                                    /* the member starts at 5, not 0 */

class Dog {
public:
    int id;
    Dog(int n) { id = n; }
    ~Dog() { printf("~Dog(%d)\n", id); }
};

double chosen = 1 > 0 ? 2.5 : 1.5;                    /* a conditional constant initializer */

int vsum(int n, va_list ap) {                         /* a va_list handed to another function */
    int s = 0;
    while (n-- > 0) s += va_arg(ap, int);
    return s;
}
int total(int n, ...) {
    va_list ap;
    va_start(ap, n);
    int s = vsum(n, ap);
    va_end(ap);
    return s;
}

int one() { return 1; }

int main() {
    int k = 5;
    printf("%.2f %.2f\n", half(k), half(3));

    C c;
    B *pb = &c;
    C *none = 0;
    B *nb = none;                                     /* a null pointer stays null */
    printf("%d %d %d %d %d %d %d\n", c.sum(), c.gb(), pb->b, takeB(&c), c.ga(), nb == 0, takeB(nb));
    A first(c);                                       /* only the A part is copied */
    int guard = 77;
    printf("%d %d\n", first.a, guard);

    Cnt x, y;
    printf("%d %d %d\n", Cnt::made, x.id, y.id);
    printf("%.1f %d\n", chosen, total(3, 1, 2, 3));

    {
        Dog d(1);
        k ? one() : 0;                                /* the block still ends with ~Dog(1) */
    }
    printf("after the block\n");
    {
        Dog last(2);
    }
    return 0;
}
