/* t27 -- object rules of the reduced C++ subset (D35): objects passed and
   returned by value are copied as blocks (there are no copy constructors),
   c ? a : b as an lvalue, const on a typedef'd array, arrays of objects
   built by the default constructor, a global object built before main,
   friends */

class Counted {
public:
    int v;
    Counted() { v = 1; }
};
int take(Counted c) { c.v = 50; return c.v; }      /* changes only the copy */
Counted give(Counted &c) { return c; }             /* the result is a copy */
Counted fresh(int x) { Counted local; local.v = x; return local; }

class Dog {
    int secret;
public:
    int id;
    Dog() { id = 0; secret = 42; printf("Dog()\n"); }
    friend int peek(const Dog &d);
};
int peek(const Dog &d) { return d.secret; }         /* a friend reads a private member */
Dog keeper;                                         /* built before main runs */

typedef int Row[4];
const int primes[4] = {2, 3, 5, 7};
int sum(const Row r) { int s = 0; for (int i = 0; i < 4; i++) s += r[i]; return s; }

struct Account { int id; double balance; };
Account &richer(Account &a, Account &b) { return a.balance >= b.balance ? a : b; }
int &pick(int which, int &a, int &b) { return which ? a : b; }

int main() {
    printf("start of main\n");
    Counted a;
    printf("%d %d\n", take(a), a.v);
    Counted b = give(a);
    b.v = 7;
    Counted c = fresh(5);
    printf("%d %d %d\n", a.v, b.v, c.v);

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
        printf("%d %d\n", pack[2].id, peek(pack[0]));
    }
    printf("%d %d\n", keeper.id, peek(keeper));
    return 0;
}
