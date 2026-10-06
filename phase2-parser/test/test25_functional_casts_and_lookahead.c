/* test25 -- constructs that need more than one token of lookahead, settled
   by the scanner (see parenGroupIsExpression and the declarator-list
   tracking in scanner_support.cpp): keyword and class functional
   casts, statements starting with a temporary (`Dog(4).bark();`), typedef
   names redeclared after a comma, constant-expression designators, and
   `sizeof(int) * 2` read as (sizeof(int)) * 2. A fully valid program. */
typedef int T;
typedef int U;
const int FIRST = 0, THIRD = 2;
class Dog {
public:
    int legs;
    Dog(int n) { legs = n; }
    Dog() { legs = 4; }
    int bark() { return legs; }
};
int take(Dog d) { return d.legs; }
int twice(int v) { return v * 2; }
int main() {
    int x = 3;
    double d = double(x) / 2;          /* 1: keyword functional casts */
    int i = int(d) + int(2.5);
    char c = char(65);
    long big = long(x) * 2;
    int(x) + 1;                        /* 1: a statement starting with one */
    Dog(4).bark();                     /* 2: a statement starting with a temporary */
    Dog().bark();
    Dog(x).bark();
    int y = take(Dog(5)) + take(Dog(x));
    Dog (spot);                        /* still a declaration, as in C++ */
    Dog rex(3);
    int a, T;                          /* 3: T redeclared after a comma */
    T = 5;
    int k = 2, U = T + 1, m;
    const int N = 2;
    int arr[4] = {[N] = 7, [FIRST] = 1, [THIRD + 1] = 9};   /* 4: designators by constant expression */
    int g = twice(1);
    int *ip = (int *) 0;
    int s = sizeof(int) * 2 + sizeof(int (*)[4]);
    return x + i + c + big + y + spot.legs + rex.legs + a + T + k + U + m + arr[3] + g + s + d;
}
