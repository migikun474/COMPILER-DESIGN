/* t24 -- references and const: aliases, reference parameters and
   results, references to structs, arrays and pointers */
#include <stdio.h>

struct Account { int id; double balance; };

void deposit(Account &a, double amount) { a.balance += amount; }
double peek(const Account &a) { return a.balance; }
Account &richer(Account &a, Account &b) { return a.balance >= b.balance ? a : b; }

void minmax(const int values[], int n, int &lo, int &hi) {
    lo = hi = values[0];
    for (int i = 1; i < n; i++) {
        if (values[i] < lo) lo = values[i];
        if (values[i] > hi) hi = values[i];
    }
}

void advance(int *&p, int steps) { p += steps; }         /* a reference to a pointer */
int &element(int a[], int i) { return a[i]; }
int scale(const int &v, const double &factor) { return (int) (v * factor); }
void rotate(int &a, int &b, int &c) { int t = a; a = b; b = c; c = t; }

int main() {
    int x = 1, y = 2, z = 3;
    int &rx = x;
    int &rrx = rx;                              /* a reference to what rx names */
    rrx += 10;
    rotate(x, y, z);
    printf("%d %d %d %d\n", x, y, z, rx);

    int data[5] = {8, -3, 15, 0, 7}, lo, hi;
    minmax(data, 5, lo, hi);
    element(data, 3) = 99;
    element(data, 0)++;
    int *p = data;
    advance(p, 2);
    *p += 1;
    printf("%d %d %d %d %d\n", lo, hi, data[3], data[0], data[2]);

    Account a = {1, 100.5}, b = {2, 250.0};
    deposit(a, 200);
    richer(a, b).balance -= 50;                 /* modifies whichever is richer */
    Account &best = richer(a, b);
    printf("%.1f %.1f %d %.1f\n", a.balance, b.balance, best.id, peek(best));

    const int limit = 40;
    const double rate = 1.25;
    short small = 7;
    printf("%d %d %d\n", scale(limit, rate), scale(small, 2), scale(3 + 4, 0.5));
    const char *msg = "const data";
    const char &first = msg[0];
    printf("%c %c\n", first, *(msg + 6));
    return rx + lo;
}
