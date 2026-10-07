/* valid: function overloading, references */
int combine(int a, int b) { return a + b; }
int combine(char a, char b) { return a - b; }
double combine(double a, double b) { return a * b; }
int combine(int a, int b, int c) { return a + b + c; }
int pick(int a) { return a; }
int pick(double a) { return 2; }

void bump(int &r) { r = r + 1; }

int main() {
    int x = 5, y = 10;
    int r = combine(1, 2);        /* exact match: (int, int) */
    char p = 'p', q = 'q';
    r = combine(p, q);            /* exact match: (char, char) */
    double d = combine(1.5, 2.5); /* exact match: (double, double) */
    r = combine(1, 2, 3);         /* chosen by argument count */
    r = pick('c');                /* pick(int): char->int promotion beats char->double conversion */
    r = pick(2.5f);               /* pick(double): float->double promotion */

    int &alias = x;               /* reference */
    alias = 7;
    bump(x);

    auto sum = x + y;             /* `auto` deduces int */
    return r + sum + d;
}
