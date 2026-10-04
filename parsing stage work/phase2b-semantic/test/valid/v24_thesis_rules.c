/* Rules from Papaspyrou's formal semantics of C, checked at compile time.
   A wrong constant makes an array dimension negative. */
#include <stdio.h>

/* constants have values of their own type (val[tau]) */
int u1[-1 < 0u ? -1 : 1];                       /* -1 converts to 4294967295u: false */
int u2[(unsigned)-1 / 2147483647u == 2u ? 1 : -1];
int u3[~0u == 4294967295u ? 1 : -1];
int u4[(unsigned char)300 == 44 ? 1 : -1];
int u5[(int)4294967297LL == 1 ? 1 : -1];
int u6[(1u << 31) > 0 ? 1 : -1];
int u7[-2147483647 - 1 < 0 ? 1 : -1];
int u8[(char)200 == -56 ? 1 : -1];
int u9[sizeof(3000000000) == 8 && sizeof(0xFFFFFFFF) == 4 ? 1 : -1]; /* long long, unsigned int */

/* linkage: one object, composite type */
extern int table[];
int table[4] = { 1, 2, 3, 4 };
int table_ok[sizeof(table) == 16 ? 1 : -1];
extern int counter;
int counter = 0;
extern int counter;
int bump(void) { extern int counter; return ++counter; }
int total = 10;
int read_total(void) { extern int total; return total; }

struct Mutable { int a, b; };

int main() {
    register int r = 2;
    int i = 0, j = 0, a[4] = { 0 };
    struct Mutable m1 = { 1, 2 }, m2 = { 3, 4 };
    m1 = m2;                         /* no const member: assignable */

    /* well-defined: sequence points in between */
    i = i + 1;
    i += 2;
    i = (i++, i);
    j = i && i++;
    j = i ? i++ : i--;
    a[i % 4] = j;
    for (i = 0; i < 3; i++, j++) {}
    j = sizeof(i++) + i;

    /* default argument promotions: char/short -> int, float -> double */
    char c = 'x'; short s = 1; float f = 1.5f; long l = 2; long long ll = 3; double d = 0;
    printf("%c %d %hd %f %ld %lld %zu\n", c, c, s, f, l, ll, sizeof(int));
    scanf("%d %f %lf %c", &i, &f, &d, &c);
    unsigned u = -1;                 /* deliberate: not reported */
    return r + j + bump() + read_total() + table[0] + (int)u + m1.a;
}
