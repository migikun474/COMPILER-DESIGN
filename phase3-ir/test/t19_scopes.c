/* t19 -- scopes and lifetimes: shadowing, nested blocks, static and
   global variables, the same name in different functions */
#include <stdio.h>

int x = 100;
int counter = 0;
static int hidden = 7;

int next() { static int n = 10; n += 5; return n; }
int twice() { static int calls; calls++; return calls * 2; }

int shadow(int x) {
    int r = x;                    /* the parameter hides the global */
    {
        int x = 3;                /* a block hides the parameter */
        r += x;
        {
            int x = 4;
            r += x;
        }
        r += x;
    }
    return r + x;
}

int useGlobal() { return x + hidden; }

void changeGlobal() { x = x + 1; counter++; }

int loops() {
    int total = 0;
    for (int i = 0; i < 3; i++) {
        int i2 = i * i;
        for (int i = 10; i < 12; i++) total += i;     /* an inner i */
        total += i2;
    }
    int i = 50;                   /* i again, after the loop */
    return total + i;
}

int main() {
    printf("%d %d %d\n", shadow(1), useGlobal(), x);
    changeGlobal();
    changeGlobal();
    int x = 5;                    /* a local hides the global from here on */
    printf("%d %d %d\n", x, useGlobal(), counter);
    int n1 = next(), n2 = next();     /* separate: argument order is unspecified in C */
    printf("%d %d\n", n1, n2);
    int a = twice(), b = twice(), c = twice();
    printf("%d %d %d\n", a, b, c);
    printf("%d\n", loops());
    {
        int counter = -1;         /* hides the global counter */
        counter--;
        printf("%d\n", counter);
    }
    printf("%d\n", counter);
    return x;
}
