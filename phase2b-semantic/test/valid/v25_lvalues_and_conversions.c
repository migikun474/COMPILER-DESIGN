/* valid: rules added after the second code review -- a conditional of two
   lvalues is an lvalue, const reaches the elements of a typedef'd array,
   a converting constructor may take an object of another class */
typedef int Row[4];
const int primes[4] = {2, 3, 5, 7};
int sum(const Row r) { return r[0] + r[3]; }          /* const Row is const int[4] */

struct Account { int id; double balance; };
struct Account &richer(struct Account &a, struct Account &b) { return a.balance >= b.balance ? a : b; }
int &pick(int which, int &a, int &b) { return which ? a : b; }

class Other { public: int n; Other() { n = 7; } };
class Vec {
public:
    int x;
    Vec(Other o) { x = o.n; }
    Vec(int k) { x = k; }
};

int main() {
    int x = 1, y = 2;
    int &r = x > y ? x : y;                           /* binds to x or y, not to a temporary */
    r = 20;
    (x < y ? x : y) = 10;                             /* assignable */
    (x ? x : y)++;
    int *p = &(x ? x : y);
    pick(1, x, y) += 5;
    struct Account a = {1, 10.5}, b = {2, 99.0};
    richer(a, b).balance -= 9;
    double d = x ? x : 2.5;                           /* different types: an ordinary value */
    Other o;
    Vec f = o, g = 5;
    return sum(primes) + *p + (int) d + f.x + g.x;
}
