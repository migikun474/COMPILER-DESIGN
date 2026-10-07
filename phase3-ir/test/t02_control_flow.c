/* t02 -- if/else, while, do-while, for, until, switch, break, continue, goto */
#include <stdio.h>
#ifdef __cplusplus
#define until(c) while (!(c))
#endif

int classify(int n) {
    switch (n) {
        case 0: return 100;
        case 1:
        case 2: n = n + 10;              /* falls through */
        case 3: n = n * 2; break;
        default: n = -1;
    }
    return n;
}

int main() {
    int i, total = 0;
    for (i = 0; i < 10; i++) {
        if (i == 2) continue;
        if (i == 8) break;
        total += i;
    }
    printf("for: %d %d\n", i, total);

    int n = 5, fact = 1;
    while (n > 1) { fact = fact * n; n = n - 1; }
    printf("while: %d\n", fact);

    do { n = n + 3; } while (n < 10);
    printf("do: %d\n", n);

    until (n >= 20) { n += 4; }
    printf("until: %d\n", n);

    for (i = 0; i < 6; i++) printf("%d ", classify(i));
    printf("\n");

    for (i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (j > i) break;
            printf("%d%d ", i, j);
        }
    }
    printf("\n");

    int count = 0;
again:
    count++;
    if (count < 4) goto again;
    if (count == 4) goto done;
    count = 99;
done:
    printf("goto: %d\n", count);

    int x = 3;
    if (x > 5) printf("big\n");
    else if (x > 2) printf("medium\n");
    else printf("small\n");

    for (;;) {
        x--;
        switch (x) {
            case 1: continue;
            default: break;
        }
        if (x <= 0) break;
    }
    printf("x: %d\n", x);
    return total;
}
