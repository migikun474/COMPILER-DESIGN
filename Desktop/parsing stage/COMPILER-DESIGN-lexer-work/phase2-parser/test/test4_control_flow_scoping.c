/* Control flow + nested scoping: a local variable inside the for-loop
 * body shadows nothing here, but note how the loop variable `i` and the
 * outer `total` are both resolved to INT via the scope stack (pushed
 * on '{' and on the for-loop's own declaration, popped on the
 * matching '}'). */

int sum_to(int n) {
    int total;
    total = 0;
    for (int i = 1; i <= n; i = i + 1) {
        total = total + i;
    }
    return total;
}

int classify(int n) {
    switch (n) {
        case 0:
            return 0;
        case 1:
            return 1;
        default:
            break;
    }
    return -1;
}

int main() {
    int n;
    n = 5;
    int s;
    s = sum_to(n);
    int c;
    c = classify(n);
    printf("%d %d\n", s, c);
    return 0;
}
