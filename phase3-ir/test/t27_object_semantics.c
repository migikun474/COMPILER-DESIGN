/* t27 -- C++ object rules found missing by the second code review:
   copy constructors for by-value arguments and results, converting
   constructors from another class, c ? a : b as an lvalue, const on a
   typedef'd array, arrays of objects, destructors of static objects */
#include <stdio.h>

class Counted {
public:
    int v;
    Counted(int x) { v = x; }
    Counted(const Counted &o) { v = o.v + 100; printf("copy of %d\n", o.v); }
};
int take(Counted c) { return c.v; }                 /* the argument is copied */
Counted give(Counted &c) { return c; }             /* the result is a copy */
Counted fresh(int x) { Counted local(x); return local; }   /* a returned local is not copied */

class Other { public: int n; Other() { n = 7; } };
class Vec {
public:
    int x;
    Vec(Other o) { x = o.n * 2; }
    Vec(int k) { x = k; }
};

class Dog {
public:
    int id;
    Dog() { id = 0; }
    Dog(int n) { id = n; }
    ~Dog() { printf("~Dog %d\n", id); }
};
Dog keeper(9);                                      /* destroyed when main returns */

typedef int Row[4];
const int primes[4] = {2, 3, 5, 7};
int sum(const Row r) { int s = 0; for (int i = 0; i < 4; i++) s += r[i]; return s; }

struct Account { int id; double balance; };
Account &richer(Account &a, Account &b) { return a.balance >= b.balance ? a : b; }
int &pick(int which, int &a, int &b) { return which ? a : b; }

int main() {
    Counted a(1);
    printf("%d\n", take(a));
    Counted b = give(a);
    Counted c = fresh(5);
    printf("%d %d %d\n", a.v, b.v, c.v);

    Other o;
    Vec f = o, g = 5;
    printf("%d %d\n", f.x, g.x);

    int x = 1, y = 2;
    int &r = x > y ? x : y;
    r = 20;
    (x < y ? x : y) = 10;
    pick(1, x, y) += 5;
    Account p = {1, 10.5}, q = {2, 99.0};
    richer(p, q).balance -= 9;
    printf("%d %d %.1f %.1f\n", x, y, p.balance, q.balance);
    printf("%d\n", sum(primes));

    {
        Dog pack[3];
        for (int i = 0; i < 3; i++) pack[i].id = i + 1;
    }                                               /* ~Dog 3, 2, 1 */
    printf("end of main\n");
    return 0;
}
